# Thumbnails

Optional preview images for content entries. Images here are served from
GitHub's raw CDN — so the directory keeps content thumbnails self-contained, with
no third-party links to rot and nothing coupled to the netbird.io site.

To give a piece of content a custom thumbnail, drop an image named after the
content's slug (its `data/content/<slug>.yaml` filename):

    data/content/thumbnails/<slug>.png      # .png, .jpg, .jpeg, or .webp

The build wires it into the feed automatically — you do **not** set a thumbnail
field in the YAML. If you don't add an image:

- **YouTube videos** use their auto-derived YouTube thumbnail.
- **Everything else** uses the site's branded fallback tile.

Keep images reasonably sized — roughly 1280×720 and under ~500 KB.
