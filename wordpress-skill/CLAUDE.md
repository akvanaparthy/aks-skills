# Project: {Theme name} — WordPress theme

Copy this file to the root of a theme project and fill in the braces. Delete lines that
don't apply.

Read `.claude/skills/wordpress-skill/SKILL.md` before working here.

## What this is
- Block theme `{slug}` in `{path, e.g. theme/{slug}}`. Text domain `{slug}`.
- Companion plugin `{plugin-slug}` in `{path}` for custom post types / fields / blocks
  (delete if none).
- Target WordPress `{version}` / PHP `{version}`.
- Audience / purpose: `{one line — e.g. marketing site for a SaaS, reusable theme to sell}`.
- Reusable by other sites: `{yes / no}`. If yes: no brand data hard-coded; everything
  via `theme.json`, site blocks, settings, style variations.

## Environment
- Local WordPress: `{wp-env | WordPress Studio | LocalWP | Docker}` at `{http://localhost:8888}`,
  admin `{user}` / `{password}`.
- WP-CLI: `{npx wp-env run cli wp … | wp …}`.
- Live reload: `{browser-sync proxy / Studio preview / none}`.
- Screenshots: `{Playwright MCP | Chrome | I will paste screenshots}`.
- Validator: `node .claude/skills/wordpress-skill/scripts/validate_theme.mjs {theme-path} [--plugin {plugin-path}]`.

## Design input
- Reference images live in `{design/references/}`. Treat them as specs: note what you
  see, build, screenshot at ~1440px and ~390px, score 0–10, iterate ≤ 3 times, list gaps.
- Extracted design tokens are recorded in `{design/tokens.md}` and implemented in
  `theme.json`. New colours/sizes go into presets first, never raw values in markup.

## Rules
1. Core blocks first; custom blocks only for interactivity or data processing.
2. Data in the plugin, looks in the theme.
3. All strings translatable; all output escaped; all input sanitized.
4. Don't duplicate what an active SEO plugin outputs.
5. Ask before decisions that are expensive to reverse (URL structure, content model);
   otherwise decide, note it in `DECISIONS.md`, continue.
6. Run the validator and take screenshots before saying a task is done.

## Repo layout
```
{design/references/}
{theme/{slug}/}
{plugin/{plugin-slug}/}
{qa/screenshots/}
DECISIONS.md
QA.md
```
