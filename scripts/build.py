#!/usr/bin/env python3
"""Compile data/projects/*.yaml into dist/projects.json.

dist/projects.json is the machine-readable artifact the website consumes. It is
a build output — do not edit it by hand. Edit the YAML files under
data/projects/ (or this script) and re-run:

    python3 scripts/build.py

The output is deterministic (stable key order, stable entry order, no
timestamps) so it can be committed and diff-checked in CI. Run from the repo root.
"""

import glob
import json
import os
import sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

# Format version of dist/projects.json. Bump when the output shape changes so
# the site can guard against an incompatible feed.
SCHEMA_VERSION = 1

# Presentation order: category, then badge priority, then name. Mirrors the
# README so the feed arrives display-ready, and is fully deterministic.
CATEGORY_ORDER = {"Apps": 0, "Extensions": 1, "Interfaces": 2, "Tools": 3}
BADGE_ORDER = {"official": 0, "endorsed": 1}

# Explicit key order for each emitted entry (id first, badge last when present).
ENTRY_KEYS = ["id", "name", "description", "author", "category", "url", "badge"]


def load_projects():
    projects = []
    for path in sorted(glob.glob("data/projects/*.yaml")):
        with open(path) as fh:
            data = yaml.safe_load(fh)
        data["id"] = os.path.basename(path)[: -len(".yaml")]
        projects.append(data)
    return projects


def sort_key(p):
    return (
        CATEGORY_ORDER.get(p["category"], 99),
        BADGE_ORDER.get(p.get("badge"), 2),
        p["name"].lower(),
    )


def entry(p):
    return {k: p[k] for k in ENTRY_KEYS if k in p}


def main():
    if not os.path.isdir("data/projects"):
        sys.exit("error: run from the repository root (data/projects not found)")

    projects = sorted(load_projects(), key=sort_key)
    if not projects:
        sys.exit("error: no project files found under data/projects/")

    payload = {
        "version": SCHEMA_VERSION,
        "count": len(projects),
        "projects": [entry(p) for p in projects],
    }

    os.makedirs("dist", exist_ok=True)
    with open("dist/projects.json", "w") as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    print(f"Wrote dist/projects.json ({len(projects)} projects).")


if __name__ == "__main__":
    main()
