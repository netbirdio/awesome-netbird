#!/usr/bin/env python3
"""Generate README.md from the project entries in data/projects/.

README.md is a build artifact — do not edit it by hand. Edit the YAML files
under data/projects/ (or this script) and re-run:

    python3 scripts/gen-readme.py

Run from the repository root.
"""

import glob
import os
import sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

# Category order and the one-line blurb shown under each section heading.
# Keep these in sync with schema/project.schema.json and CONTRIBUTING.md.
CATEGORIES = {
    "Apps": "Run or deploy NetBird somewhere — images, clients, and devices.",
    "Extensions": "Plug NetBird into another tool or platform.",
    "Interfaces": "View or drive NetBird — CLIs, dashboards, and exporters.",
    "Tools": "Automate or manage NetBird via code — libraries and infrastructure as code.",
}

BADGE_TAG = {"official": "`🟢 Official`", "endorsed": "`⭐ Endorsed`"}
# official first, then endorsed, then community; alphabetical within each.
BADGE_ORDER = {"official": 0, "endorsed": 1}


def load_projects():
    projects = []
    for path in sorted(glob.glob("data/projects/*.yaml")):
        with open(path) as fh:
            projects.append(yaml.safe_load(fh))
    return projects


def sort_key(p):
    return (BADGE_ORDER.get(p.get("badge"), 2), p["name"].lower())


def render(projects):
    total = len(projects)
    official = sum(1 for p in projects if p.get("badge") == "official")
    endorsed = sum(1 for p in projects if p.get("badge") == "endorsed")
    community = total - official - endorsed

    lines = []
    lines.append("# Awesome NetBird")
    lines.append("")
    lines.append(
        "> A curated list of community projects, tools, and integrations for "
        "[NetBird](https://netbird.io) — the open-source, WireGuard-based "
        "zero-configuration mesh VPN."
    )
    lines.append("")
    lines.append(
        "This list is the source of truth for the community projects directory on "
        "[netbird.io](https://netbird.io). Each entry lives in its own file under "
        "[`data/projects/`](data/projects/); the site reads from this repository, so "
        "adding a project here adds it to the website. To submit one, see "
        "[CONTRIBUTING.md](CONTRIBUTING.md)."
    )
    lines.append("")
    lines.append(
        f"**{total} projects** · 🟢 {official} official · ⭐ {endorsed} endorsed · "
        f"{community} community"
    )
    lines.append("")
    lines.append("## Contents")
    lines.append("")
    for name in CATEGORIES:
        count = sum(1 for p in projects if p["category"] == name)
        lines.append(f"- [{name}](#{name.lower()}) ({count})")
    lines.append("")
    lines.append(
        "**Legend:** `🟢 Official` built and maintained by the NetBird team · "
        "`⭐ Endorsed` a community project the NetBird team vouches for."
    )
    lines.append("")

    for name, blurb in CATEGORIES.items():
        rows = sorted((p for p in projects if p["category"] == name), key=sort_key)
        lines.append(f"## {name}")
        lines.append("")
        lines.append(f"_{blurb}_")
        lines.append("")
        for p in rows:
            tag = BADGE_TAG.get(p.get("badge"))
            tag = f" {tag}" if tag else ""
            lines.append(
                f"- **[{p['name']}]({p['url']})**{tag} — "
                f"{p['description']} _by {p['author']}_"
            )
        lines.append("")

    lines.append("## Contributing")
    lines.append("")
    lines.append(
        "Found a NetBird project that belongs here? Open a pull request adding one "
        "file under [`data/projects/`](data/projects/). See "
        "[CONTRIBUTING.md](CONTRIBUTING.md) for the format and review criteria."
    )
    lines.append("")
    return "\n".join(lines) + "\n"


def main():
    if not os.path.isdir("data/projects"):
        sys.exit("error: run this script from the repository root (data/projects not found)")
    projects = load_projects()
    if not projects:
        sys.exit("error: no projects found under data/projects/")
    with open("README.md", "w") as fh:
        fh.write(render(projects))
    print(f"Generated README.md from {len(projects)} projects.")


if __name__ == "__main__":
    main()
