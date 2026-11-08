# Profile README — maintenance notes

## Layout

```
README.md                 generated from scripts/README.tpl.md
assets/
  hero/                   animated hero + typewriter (SMIL, no JS)
  decorations/            section headers, label chips, divider, closing panel
  timeline/               vertical journey timeline
  capabilities/ focus/    card headers for "What I build" and "Currently exploring"
  stack/                  seven tech-stack rows
  projects/               three illustrations + framed Zameen screenshot
  process/                six-stage engineering workflow
  buttons/                link buttons
scripts/                  generator (Python) + font subsets source (OFL)
```

Every visual exists in `-dark.svg` and `-light.svg`; the README switches between them with
`<picture>` + `prefers-color-scheme`. Fonts (Inter, JetBrains Mono) are subset and embedded
inside each SVG, so nothing in the core design loads from an external host.

## Editing

1. Change text or data in `scripts/build_assets.py` / `scripts/build_assets_2.py`
   (hero phrases, timeline, stack, project illustrations) or copy in `scripts/README.tpl.md`.
2. Regenerate:

   ```bash
   pip install fonttools brotli pillow
   python scripts/build_assets.py
   python scripts/build_readme.py
   ```

3. Commit `README.md` and `assets/`.

Template macros: `[[pic:path|alt|width]]`, `[[btn:name|url|label]]`, `[[ext:key|alt]]`.

## External services (live data only)

| Card | Service | Notes |
|---|---|---|
| Stats, top languages | github-readme-stats.vercel.app | Public instance is best-effort and can rate-limit. Fix: deploy your own instance on Vercel with a `PAT_1` token and replace the host in `scripts/build_readme.py`. |
| Streak | streak-stats.demolab.com | Self-hostable if it becomes unreliable. |
| Activity graph | github-readme-activity-graph.vercel.app | Last 31 days of contributions. |
| Visitor counter | komarev.com/ghpvc | Counts page loads, not unique visitors. |

If any provider is down, only that card shows its alt text; the rest of the page is unaffected.

## Not included (by request)

No GitHub Actions and no contribution snake. Nothing in this repo needs secrets or extra
repository permissions.

## Licences

Inter and JetBrains Mono: SIL Open Font License (see `scripts/fonts/`).
Technology logos: Simple Icons (CC0); brand names belong to their owners.
