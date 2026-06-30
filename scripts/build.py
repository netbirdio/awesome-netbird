#!/usr/bin/env python3
"""Compile data/<collection>/*.yaml into dist/<collection>.json.

The dist/*.json files are the machine-readable artifacts the website consumes.
They are build outputs — do not edit them by hand. Edit the YAML files under
data/ (or this script) and re-run:

    python3 scripts/build.py

Each output is deterministic (stable key order, stable entry order, no
timestamps) so it can be committed and diff-checked in CI. Run from the repo root.
"""

import datetime
import glob
import json
import os
import re
import sys
from urllib.parse import parse_qs, urlsplit

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

# Format version shared by every dist/*.json feed. Bump when an output shape
# changes so the site can guard against an incompatible feed.
SCHEMA_VERSION = 1

# --- projects ---------------------------------------------------------------
# Presentation order: category, then badge priority, then name. Mirrors the
# README so the feed arrives display-ready, and is fully deterministic.
CATEGORY_ORDER = {"Apps": 0, "Extensions": 1, "Interfaces": 2, "Tools": 3}
BADGE_ORDER = {"official": 0, "endorsed": 1}


def project_sort_key(p):
    return (
        CATEGORY_ORDER.get(p["category"], 99),
        BADGE_ORDER.get(p.get("badge"), 2),
        p["name"].lower(),
    )


# --- content ----------------------------------------------------------------
# Optional, repo-hosted thumbnails live in data/content/thumbnails/<slug>.<ext>
# and are served from GitHub's raw CDN — no third-party links, no netbird.io
# coupling. A committed image wins; otherwise YouTube videos get their auto
# thumbnail; items with neither carry no thumbnail and the site renders a branded
# fallback tile.
THUMBNAIL_DIR = "data/content/thumbnails"
THUMBNAIL_EXTS = (".png", ".jpg", ".jpeg", ".webp")
RAW_BASE = "https://raw.githubusercontent.com/netbirdio/awesome-netbird/main"


def repo_thumbnail(slug):
    """Return the raw-CDN URL for a committed thumbnails/<slug>.<ext>, or None.

    Extensions are checked in a fixed order, so the result is deterministic even
    if (against the validator's rules) two images share a slug.
    """
    for ext in THUMBNAIL_EXTS:
        if os.path.isfile(os.path.join(THUMBNAIL_DIR, slug + ext)):
            return f"{RAW_BASE}/{THUMBNAIL_DIR}/{slug}{ext}"
    return None


def youtube_thumbnail(url):
    """Return the maxresdefault thumbnail URL for a YouTube link, else None.

    Pure string parsing (no network), so the build stays deterministic. Handles
    watch?v=, youtu.be/, /shorts/, /embed/, and /live/ URL shapes.
    """
    parts = urlsplit(url)
    host = (parts.hostname or "").lower()
    vid = None
    if host == "youtu.be" or host.endswith(".youtu.be"):
        vid = parts.path.lstrip("/").split("/")[0]
    elif host == "youtube.com" or host.endswith(".youtube.com"):
        qs = parse_qs(parts.query)
        if "v" in qs and qs["v"]:
            vid = qs["v"][0]
        else:
            m = re.match(r"^/(?:shorts|embed|live|v)/([^/?#]+)", parts.path)
            if m:
                vid = m.group(1)
    if vid and re.fullmatch(r"[A-Za-z0-9_-]{6,20}", vid):
        return f"https://img.youtube.com/vi/{vid}/maxresdefault.jpg"
    return None


def enrich_content(c):
    """Resolve the thumbnail. thumbnail is a computed output, not a YAML input:
    a committed repo image wins, else a YouTube auto-thumbnail, else none."""
    thumb = repo_thumbnail(c["id"]) or youtube_thumbnail(c["url"])
    if thumb:
        c["thumbnail"] = thumb
    else:
        c.pop("thumbnail", None)
    return c


def date_desc_key(d):
    """Sort key fragment: dated entries first (newest first), then undated."""
    if not d:
        return (1, 0, 0, 0)
    y, m, day = (int(part) for part in d.split("-"))
    return (0, -y, -m, -day)


def content_sort_key(c):
    # Featured first, then newest by publish date, then slug for a stable tie-break.
    return (0 if c.get("featured") else 1, date_desc_key(c.get("publish_date")), c["id"])


# --- collection registry ----------------------------------------------------
# name = data/<name>/ dir, dist/<name>.json file, and top-level list key.
COLLECTIONS = [
    {
        "name": "projects",
        "sort_key": project_sort_key,
        "keys": ["id", "name", "description", "author", "category", "url", "badge"],
    },
    {
        "name": "content",
        "sort_key": content_sort_key,
        "keys": ["id", "type", "title", "source", "url", "thumbnail", "publish_date", "featured"],
        "enrich": enrich_content,
    },
]


def normalize_dates(data):
    """Coerce YAML date values to ISO 'YYYY-MM-DD' strings.

    PyYAML parses an unquoted `2026-03-14` into a datetime.date, but the feed
    and schema want plain strings — so a contributor's pasted date works whether
    or not they quote it.
    """
    for key, value in list(data.items()):
        if isinstance(value, datetime.datetime):
            data[key] = value.date().isoformat()
        elif isinstance(value, datetime.date):
            data[key] = value.isoformat()
    return data


def load_collection(name):
    items = []
    for path in sorted(glob.glob(f"data/{name}/*.yaml")):
        with open(path) as fh:
            data = yaml.safe_load(fh)
        data["id"] = os.path.basename(path)[: -len(".yaml")]
        items.append(normalize_dates(data))
    return items


def entry(item, keys):
    return {k: item[k] for k in keys if k in item}


def build_collection(cfg):
    name = cfg["name"]
    items = load_collection(name)
    if "enrich" in cfg:
        items = [cfg["enrich"](i) for i in items]
    items = sorted(items, key=cfg["sort_key"])

    payload = {
        "version": SCHEMA_VERSION,
        "count": len(items),
        name: [entry(i, cfg["keys"]) for i in items],
    }

    os.makedirs("dist", exist_ok=True)
    with open(f"dist/{name}.json", "w") as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    print(f"Wrote dist/{name}.json ({len(items)} {name}).")
    return items


def main():
    if not os.path.isdir("data/projects"):
        sys.exit("error: run from the repository root (data/projects not found)")

    counts = {cfg["name"]: len(build_collection(cfg)) for cfg in COLLECTIONS}

    if not counts.get("projects"):
        sys.exit("error: no project files found under data/projects/")


if __name__ == "__main__":
    main()
