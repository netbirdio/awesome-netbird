#!/usr/bin/env python3
"""Validate every entry under data/.

Checks, per file:
  - filename is a lowercase, hyphenated slug (the stable id)
  - parses as YAML
  - conforms to the collection's JSON schema

And across the files in each collection:
  - no duplicate urls (projects, content)
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
        except yaml.YAMLError as exc:
            errors.append(f"{path}: invalid YAML: {exc}")
            continue

        if not isinstance(data, dict):
            errors.append(f"{path}: top-level value must be a mapping")
            continue

        normalize_dates(data)

        for err in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
            loc = ".".join(str(p) for p in err.path) or "(root)"
            errors.append(f"{path}: {loc}: {err.message}")

        url = data.get("url")
        if url:
            msg = url_error(url)
            if msg:
                errors.append(f"{path}: url: {msg}")
            if cfg["unique_url"]:
                if url in urls:
                    errors.append(f"{path}: duplicate url, also in {urls[url]}")
                else:
                    urls[url] = path

        field = cfg["unique_field"]
        value = data.get(field)
        if value:
            key = value.lower()
            if key in keys:
                errors.append(f"{path}: duplicate {field} '{value}', also in {keys[key]}")
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
