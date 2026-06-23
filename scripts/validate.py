#!/usr/bin/env python3
"""Validate every project entry under data/projects/.

Checks, per file:
  - filename is a lowercase, hyphenated slug (the stable id)
  - parses as YAML
  - conforms to schema/project.schema.json

And across all files:
  - no duplicate project URLs
  - no duplicate project names

Exits non-zero with a list of problems if anything fails. Run from the repo root:

    python3 scripts/validate.py
"""

import glob
import os
import re
import sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

try:
    import json
    import jsonschema
except ImportError:
    sys.exit("jsonschema is required: pip install jsonschema")

SCHEMA_PATH = "schema/project.schema.json"
SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def main():
    if not os.path.isdir("data/projects"):
        sys.exit("error: run from the repository root (data/projects not found)")

    with open(SCHEMA_PATH) as fh:
        schema = json.load(fh)
    validator = jsonschema.Draft7Validator(schema)

    errors = []
    urls = {}
    names = {}

    paths = sorted(glob.glob("data/projects/*.yaml"))
    if not paths:
        sys.exit("error: no project files found under data/projects/")

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

        for err in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
            loc = ".".join(str(p) for p in err.path) or "(root)"
            errors.append(f"{path}: {loc}: {err.message}")

        url = data.get("url")
        if url:
            if url in urls:
                errors.append(f"{path}: duplicate url, also in {urls[url]}")
            else:
                urls[url] = path

        name = data.get("name")
        if name:
            key = name.lower()
            if key in names:
                errors.append(f"{path}: duplicate name '{name}', also in {names[key]}")
            else:
                names[key] = path

    if errors:
        print(f"✗ {len(errors)} problem(s) found:\n", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)

    print(f"✓ {len(paths)} project file(s) valid.")


if __name__ == "__main__":
    main()
