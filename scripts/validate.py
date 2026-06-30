#!/usr/bin/env python3
"""Validate every entry under data/.

Checks, per file:
  - filename is a lowercase, hyphenated slug (the stable id)
  - parses as YAML
  - conforms to the collection's JSON schema
  - any publish_date is a real calendar date (not just YYYY-MM-DD shaped)

And across the files in each collection:
  - no duplicate urls (projects, content), compared after light normalization
  - no duplicate display name / title

Exits non-zero with a list of problems if anything fails. Run from the repo root:

    python3 scripts/validate.py
"""

import datetime
import glob
import json
import os
import re
import sys
from urllib.parse import urlsplit

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

try:
    import jsonschema
except ImportError:
    sys.exit("jsonschema is required: pip install jsonschema")

SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def normalize_dates(data):
    """Coerce YAML date values to ISO 'YYYY-MM-DD' strings before validation.

    PyYAML parses an unquoted `2026-03-14` into a datetime.date; the schema wants
    a string, so we normalize first and a contributor need not quote the date.
    """
    for key, value in list(data.items()):
        if isinstance(value, datetime.datetime):
            data[key] = value.date().isoformat()
        elif isinstance(value, datetime.date):
            data[key] = value.isoformat()
    return data

# Per-collection rules. `name` is the data/<name>/ dir; `schema` is its schema;
# `unique_field` is deduped case-insensitively; `unique_url` dedupes the url.
COLLECTIONS = [
    {
        "name": "projects",
        "schema": "schema/project.schema.json",
        "unique_field": "name",
        "unique_url": True,
        "required": True,
    },
    {
        "name": "content",
        "schema": "schema/content.schema.json",
        "unique_field": "title",
        "unique_url": True,
        "required": False,
    },
]


def url_error(url):
    """Return a problem string if url is not a usable https URL, else None.

    The schemas declare `format: uri`, but jsonschema only enforces it when the
    optional rfc3987 package is installed — so we validate explicitly here to
    guarantee the check runs everywhere.
    """
    if not isinstance(url, str):
        return "must be a string"
    if any(ch.isspace() for ch in url):
        return "must not contain whitespace"
    parts = urlsplit(url)
    if parts.scheme != "https":
        return "must use https://"
    if not parts.hostname or "." not in parts.hostname:
        return "must include a valid host"
    return None


def canonical_url(url):
    """Return a normalized key for duplicate detection — NOT a rewritten url.

    Lowercases the host and drops a leading 'www.' and a trailing slash, so
    https://Example.com/foo/ and https://example.com/foo collapse to one key.
    The query is kept (it can be significant, e.g. a youtube watch?v=ID). The
    youtube watch-vs-youtu.be forms are intentionally left distinct for now.
    """
    parts = urlsplit(url)
    host = (parts.hostname or "").lower()
    if host.startswith("www."):
        host = host[4:]
    key = host + parts.path.rstrip("/")
    if parts.query:
        key += "?" + parts.query
    return key


def validate_collection(cfg, errors):
    name = cfg["name"]
    if not os.path.isdir(f"data/{name}"):
        if cfg["required"]:
            errors.append(f"data/{name}: required directory is missing")
        return 0

    with open(cfg["schema"]) as fh:
        schema = json.load(fh)
    validator = jsonschema.Draft7Validator(schema)

    urls = {}
    keys = {}
    paths = sorted(glob.glob(f"data/{name}/*.yaml"))
    if not paths and cfg["required"]:
        errors.append(f"data/{name}: no entries found")

    for path in paths:
        slug = os.path.basename(path)[: -len(".yaml")]
        if not SLUG_RE.match(slug):
            errors.append(f"{path}: filename '{slug}' is not a lowercase, hyphenated slug")

        try:
            with open(path) as fh:
                data = yaml.safe_load(fh)
        except (yaml.YAMLError, ValueError) as exc:
            # ValueError covers an unquoted out-of-range date (e.g. 2026-13-45),
            # which PyYAML rejects while constructing the date object — that is
            # not a YAMLError, so without this it would crash the validator.
            errors.append(f"{path}: could not parse YAML: {exc}")
            continue

        if not isinstance(data, dict):
            errors.append(f"{path}: top-level value must be a mapping")
            continue

        normalize_dates(data)

        schema_errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
        for err in schema_errors:
            loc = ".".join(str(p) for p in err.path) or "(root)"
            errors.append(f"{path}: {loc}: {err.message}")
        if schema_errors:
            # Entry doesn't match its schema. The checks below assume schema-valid
            # types (a string url and unique field, a YYYY-MM-DD publish_date);
            # running them on bad input would be redundant with the errors above
            # at best and a traceback at worst (urlsplit() or .lower() on a
            # non-string). The schema errors already say what to fix — re-run once
            # the entry conforms.
            continue

        # Past this point the entry conforms to its schema, so the fields below
        # are the types their schema declares.

        # publish_date matches the YYYY-MM-DD shape; confirm it is a real calendar
        # date too, so e.g. 2026-99-99 is caught rather than silently mis-sorted.
        publish_date = data.get("publish_date")
        if publish_date is not None:
            try:
                datetime.date.fromisoformat(publish_date)
            except ValueError:
                errors.append(
                    f"{path}: publish_date: '{publish_date}' is not a real calendar date"
                )

        # url_error still matters for a schema that declares `format: uri` without
        # a strict pattern; dedupe only a URL that passed it, so canonical_url()
        # never sees a non-string.
        url = data.get("url")
        if url:
            msg = url_error(url)
            if msg:
                errors.append(f"{path}: url: {msg}")
            elif cfg["unique_url"]:
                key = canonical_url(url)
                if key in urls:
                    errors.append(f"{path}: duplicate url, also in {urls[key]}")
                else:
                    urls[key] = path

        value = data.get(cfg["unique_field"])
        if value:
            key = value.lower()
            if key in keys:
                errors.append(
                    f"{path}: duplicate {cfg['unique_field']} '{value}', also in {keys[key]}"
                )
            else:
                keys[key] = path

    return len(paths)


THUMBNAIL_DIR = "data/content/thumbnails"
THUMBNAIL_EXTS = (".png", ".jpg", ".jpeg", ".webp")


def validate_thumbnails(errors):
    """Each file in data/content/thumbnails/ must be a supported image named after
    an existing content slug, with at most one image per slug. README.md /
    .gitkeep are ignored. (An orphaned image is dead weight; a typo'd slug
    silently never shows up — both are caught here.)"""
    if not os.path.isdir(THUMBNAIL_DIR):
        return
    content_slugs = {
        os.path.basename(p)[: -len(".yaml")] for p in glob.glob("data/content/*.yaml")
    }
    seen = {}
    for path in sorted(glob.glob(f"{THUMBNAIL_DIR}/*")):
        base = os.path.basename(path)
        if base in ("README.md", ".gitkeep"):
            continue
        name, ext = os.path.splitext(base)
        if ext.lower() not in THUMBNAIL_EXTS:
            errors.append(
                f"{THUMBNAIL_DIR}/{base}: unsupported file type (use .png, .jpg, .jpeg, or .webp)"
            )
            continue
        if not SLUG_RE.match(name):
            errors.append(f"{THUMBNAIL_DIR}/{base}: '{name}' is not a lowercase, hyphenated slug")
        elif name not in content_slugs:
            errors.append(f"{THUMBNAIL_DIR}/{base}: no matching data/content/{name}.yaml")
        if name in seen:
            errors.append(f"{THUMBNAIL_DIR}/{base}: duplicate image for '{name}', also {seen[name]}")
        else:
            seen[name] = base


def main():
    if not os.path.isdir("data/projects"):
        sys.exit("error: run from the repository root (data/projects not found)")

    errors = []
    total = sum(validate_collection(cfg, errors) for cfg in COLLECTIONS)
    validate_thumbnails(errors)

    if errors:
        print(f"✗ {len(errors)} problem(s) found:\n", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)

    print(f"✓ {total} entry file(s) valid.")


if __name__ == "__main__":
    main()
