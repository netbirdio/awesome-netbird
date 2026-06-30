#!/usr/bin/env python3
"""Generate README.md from the entries under data/.

README.md is a build artifact — do not edit it by hand. Edit the YAML files
under data/ (or this script) and re-run:

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

# Project categories and the one-line blurb shown under each heading.
# Keep these in sync with schema/project.schema.json and CONTRIBUTING.md.
PROJECT_CATEGORIES = {
    "Apps": "Run or deploy NetBird somewhere — images, clients, and devices.",
    "Extensions": "Plug NetBird into another tool or platform.",
    "Interfaces": "View or drive NetBird — CLIs, dashboards, and exporters.",
    "Tools": "Automate or manage NetBird via code — libraries and infrastructure as code.",
}

BADGE_TAG = {"official": "`🟢 Official`", "endorsed": "`⭐ Endorsed`"}
# official first, then endorsed, then community; alphabetical within each.
BADGE_ORDER = {"official": 0, "endorsed": 1}

# Content types and their README section headings, in display order.
# Keep these in sync with schema/content.schema.json and CONTRIBUTING.md.
CONTENT_SECTIONS = {
    "video": "Videos",
    "article": "Articles",
    "blog": "Blog posts",
    "misc": "More",
}


def load(name):
    items = []
    for path in sorted(glob.glob(f"data/{name}/*.yaml")):
        with open(path) as fh:
            data = yaml.safe_load(fh)
        data["id"] = os.path.basename(path)[: -len(".yaml")]
        items.append(data)
    return items


def project_sort_key(p):
    return (BADGE_ORDER.get(p.get("badge"), 2), p["name"].lower())


def content_sort_key(c):
    # Featured first, then alphabetical. The JSON feed orders by publish date;
    # the README is a coarse human index, so a stable A–Z is plenty here.
    return (0 if c.get("featured") else 1, c["title"].lower())


def render(projects, content):
    lines = []
    lines.append("# Awesome NetBird")
    lines.append("")
    lines.append(
        "> A curated list of community projects and content for "
        "[NetBird](https://netbird.io) — the open-source, WireGuard-based "
        "zero-configuration mesh VPN."
    )
    lines.append("")
    lines.append(
        "This repository is the source of truth for the community directory on "
        "[netbird.io](https://netbird.io). Each entry lives in its own file under "
        "[`data/`](data/); the site reads from this repository, so adding an entry "
        "here adds it to the website. To submit one, see "
        "[CONTRIBUTING.md](CONTRIBUTING.md)."
    )
    lines.append("")
    lines.append(
        f"**{len(projects)} projects** · **{len(content)} pieces of content**"
    )
    lines.append("")

    lines.append("## Contents")
    lines.append("")
    lines.append(f"- [Projects](#projects) ({len(projects)})")
    lines.append(f"- [Content](#content) ({len(content)})")
    lines.append("")

    # --- Projects -----------------------------------------------------------
    lines.append("## Projects")
    lines.append("")
    lines.append(
        "**Legend:** `🟢 Official` built and maintained by the NetBird team · "
        "`⭐ Endorsed` a community project the NetBird team vouches for."
    )
    lines.append("")
    for name, blurb in PROJECT_CATEGORIES.items():
        rows = sorted((p for p in projects if p["category"] == name), key=project_sort_key)
        if not rows:
            continue
        lines.append(f"### {name}")
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

    # --- Content ------------------------------------------------------------
    lines.append("## Content")
    lines.append("")
    lines.append(
        "_Community videos, articles, and posts about NetBird. ⭐ marks featured items._"
    )
    lines.append("")
    for ctype, heading in CONTENT_SECTIONS.items():
        rows = sorted((c for c in content if c.get("type") == ctype), key=content_sort_key)
        if not rows:
            continue
        lines.append(f"### {heading}")
        lines.append("")
        for c in rows:
            star = " ⭐" if c.get("featured") else ""
            lines.append(f"- **[{c['title']}]({c['url']})**{star} — _by {c['source']}_")
        lines.append("")

    lines.append("## Contributing")
    lines.append("")
    lines.append(
        "Found a NetBird project or piece of content that belongs here? "
        "Open a pull request adding one file under [`data/`](data/). See "
        "[CONTRIBUTING.md](CONTRIBUTING.md) for the format and review criteria."
    )
    lines.append("")
    return "\n".join(lines) + "\n"


def main():
    if not os.path.isdir("data/projects"):
        sys.exit("error: run this script from the repository root (data/projects not found)")
    projects = load("projects")
    if not projects:
        sys.exit("error: no projects found under data/projects/")
    content = load("content")
    with open("README.md", "w") as fh:
        fh.write(render(projects, content))
    print(
        f"Generated README.md from {len(projects)} projects "
        f"and {len(content)} content items."
    )


if __name__ == "__main__":
    main()
