# Contributing a project

This list is the source of truth for the NetBird community projects directory.
Each project is one YAML file under [`data/projects/`](data/projects/). To add a
project, open a pull request that adds a single new file.

## Add a project

1. Copy the template below into `data/projects/<slug>.yaml`.
2. Pick the `<slug>` as a lowercase, hyphenated version of the project name
   (e.g. `netbird-traefik`). The filename is the project's stable id — keep it
   short and unlikely to change.
3. Fill in the fields and open a PR. CI validates your file against
   [`schema/project.schema.json`](schema/project.schema.json).

That is all you need to do. **`README.md` and `dist/projects.json` are generated**
from the data and are updated automatically after your PR merges — do not edit
them by hand. You do not need to run any scripts or build anything.

```yaml
name: My NetBird Project
description: >-
  One or two plain sentences describing what the project does and who it is for.
  No marketing language.
author: your-handle
category: Tools
url: https://github.com/your-handle/my-netbird-project
# badge: endorsed   # optional — see below; leave out for a standard listing
```

## Fields

| Field         | Required | Notes                                                                 |
| ------------- | -------- | --------------------------------------------------------------------- |
| `name`        | yes      | Display name of the project.                                          |
| `description` | yes      | 20–320 characters. One or two sentences, no fluff.                    |
| `author`      | yes      | Person or organization that maintains it.                             |
| `category`    | yes      | One of the four categories below.                                     |
| `url`         | yes      | `https://` link to the repository or homepage.                        |
| `badge`       | no       | Omit it. Maintainers set this.                                        |

### Categories

| Category     | Use it for                                                       |
| ------------ | ---------------------------------------------------------------- |
| `Apps`       | Running or deploying NetBird somewhere (images, clients, devices). |
| `Extensions` | Plugging NetBird into another tool or platform.                  |
| `Interfaces` | Ways to view or drive NetBird (CLIs, dashboards, exporters).     |
| `Tools`      | Automating or managing NetBird via code (libraries, IaC).        |

### Badges

`badge` is set by maintainers, not by submitters:

- **`official`** — built and maintained by the NetBird team.
- **`endorsed`** — a community project the NetBird team vouches for.
- **(omitted)** — a standard community listing.

Submit your project without a `badge`. If it is a fit for `endorsed`, a
maintainer will add it.

## What gets accepted

- The project must be related to NetBird and reachable at a working `https://` URL.
- The description must be accurate and free of marketing language.
- Keep one project per file, and one project per pull request.
