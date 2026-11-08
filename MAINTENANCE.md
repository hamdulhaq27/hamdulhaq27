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
  analytics/              most-used-languages card (measured, not live)
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

## Languages card

`assets/analytics/languages-*.svg` is generated from measured data, not fetched live: the
public github-readme-stats instance was returning errors. Figures are non-blank source lines
per language across seven public repositories, measured Nov 2026 (notebook code cells count
as Python; dependencies, data, build output and generated files excluded). To refresh, update
`LANGS` and `LANG_SCOPE` in `scripts/build_assets_2.py` and regenerate.

## External service (live data)

| Card | Service | Notes |
|---|---|---|
| Contribution streak | streak-stats.demolab.com | Live. Self-hostable if it becomes unreliable. |

If it is ever down, only that card shows its alt text; the rest of the page is unaffected.

## Not included (by request)

No GitHub Actions and no contribution snake. Nothing in this repo needs secrets or extra
repository permissions.

## Licences

Inter and JetBrains Mono: SIL Open Font License (see `scripts/fonts/`).
Technology logos: Simple Icons (CC0); brand names belong to their owners.
