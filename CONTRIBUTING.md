# Contributing

This repository is the source of truth for the NetBird community directory on
[netbird.io](https://netbird.io): **projects** and **content**. Each entry is
one YAML file under [`data/`](data/). To add something, open a pull request that
adds a single new file.

`README.md` and the `dist/*.json` feeds are **generated** from the data and are
updated automatically after your PR merges — do not edit them by hand. CI
validates every file against the schemas in [`schema/`](schema/); you do not
need to run or build anything locally.

Pick the filename `<slug>` as a lowercase, hyphenated name (e.g.
`netbird-traefik`). The filename is the entry's stable id — keep it short and
unlikely to change.

## Add a project

Copy the template into `data/projects/<slug>.yaml`:

```yaml
name: My NetBird Project
description: >-
  One or two plain sentences describing what the project does and who it is for.
  No marketing language.
author: your-handle
category: Tools
url: https://github.com/your-handle/my-netbird-project
# badge: endorsed   # optional — maintainers set this; leave it out
```

| Field         | Required | Notes                                                  |
| ------------- | -------- | ------------------------------------------------------ |
| `name`        | yes      | Display name of the project.                           |
| `description` | yes      | 20–320 characters. One or two sentences, no fluff.     |
| `author`      | yes      | Person or organization that maintains it.              |
| `category`    | yes      | One of the four categories below.                      |
| `url`         | yes      | `https://` link to the repository or homepage.         |
| `badge`       | no       | Omit it. Maintainers set this.                         |

### Project categories

| Category     | Use it for                                                        |
| ------------ | ----------------------------------------------------------------- |
| `Apps`       | Running or deploying NetBird somewhere (images, clients, devices).|
| `Extensions` | Plugging NetBird into another tool or platform.                   |
| `Interfaces` | Ways to view or drive NetBird (CLIs, dashboards, exporters).      |
| `Tools`      | Automating or managing NetBird via code (libraries, IaC).         |

### Badges

`badge` is set by maintainers, not submitters:

- **`official`** — built and maintained by the NetBird team.
- **`endorsed`** — a community project the NetBird team vouches for.
- **(omitted)** — a standard community listing.

## Add content

A video, article, blog post, or other piece about NetBird. One file per item in
`data/content/<slug>.yaml`. For YouTube videos, **omit the thumbnail** — it is
derived from the URL automatically, so all you really paste is a link.

```yaml
title: "NetBird Setup Guide"
type: video                  # video | article | blog | misc
source: Your Channel
url: https://www.youtube.com/watch?v=VIDEO_ID
publish_date: 2026-05-01     # optional (YYYY-MM-DD); enables date ordering/filtering
# featured: true             # maintainers set this to pin it to the featured row
```

| Field          | Required | Notes                                                               |
| -------------- | -------- | ------------------------------------------------------------------- |
| `title`        | yes      | Title as published.                                                 |
| `type`         | yes      | One of `video`, `article`, `blog`, `misc`.                          |
| `source`       | yes      | Creator, channel, or publication that produced it.                  |
| `url`          | yes      | `https://` link to the content.                                     |
| `publish_date` | no       | `YYYY-MM-DD`. Recommended — drives ordering and date filtering.     |
| `featured`     | no       | Omit it. Maintainers set this to pin an item to the featured row.   |

**Thumbnails.** You do not set a thumbnail in the YAML, and third-party image
URLs are not allowed. YouTube videos get their thumbnail automatically. Every
non-YouTube item (an article, blog, or misc entry) **must** ship an image at
`data/content/thumbnails/<slug>.png` (`.png`, `.jpg`, `.jpeg`, or `.webp`, named
after your file's slug) — the build wires it in, and `validate.py` rejects a
non-YouTube entry that has none. Keep images roughly 1280×720 and under ~500 KB.
See [`data/content/thumbnails/`](data/content/thumbnails/).

## What gets accepted

- Must be related to NetBird and reachable at a working `https://` URL.
- Accurate and free of marketing language.
- One entry per file, and one entry per pull request.
- `badge` (projects) and `featured` (content) are set by maintainers, not submitters.
