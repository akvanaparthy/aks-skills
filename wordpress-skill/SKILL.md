---
name: wordpress-skill
description: Build or modify a modern WordPress block theme (and its companion plugin when data is involved) to current WordPress standards, optionally matching reference images or mockups. Use this skill whenever the user mentions a WordPress theme, block theme, FSE, theme.json, templates, patterns, style variations, turning a screenshot/design into WordPress, custom post types for a WordPress site, or getting a theme ready for a client or WordPress.org — even if they just say "make this page in WordPress" or "fix the styling of my theme".
compatibility: WordPress 6.6+ (some theme.json features need 7.1+), PHP 8.0+, Node 20+. Any local environment works (wp-env, WordPress Studio, LocalWP, Docker, Playground). Visual checks need a browser tool (Playwright MCP, Chrome, or screenshots pasted by the user).
---

# WordPress theme skill

How to build WordPress themes that look like the design, follow WordPress conventions,
and can be handed to a client or another site without rework. Industry-agnostic: the
same approach works for a portfolio, a store front, a SaaS marketing site, a news site,
or a listings site.

If the official `WordPress/agent-skills` pack is installed, lean on it for WordPress API
detail (`wp-block-themes`, `wp-block-development`, `wp-interactivity-api`,
`wp-plugin-development`). This skill is about the decisions and the workflow.

**Domain layers.** This skill is industry-neutral. If a domain layer skill is installed
(e.g. `real-estate-web` for property sites) and the project matches, load it after this
one; it adds the data model, page types and rules for that industry without changing
anything here.

## Principles

1. **Block theme by default.** Classic (PHP template) themes only when the user asks
   or the project already is one. Block themes: `theme.json` + `templates/*.html` +
   `parts/*.html` + `patterns/*.php` + `styles/*.json`.
2. **Design lives in `theme.json`, not CSS.** Colours, fonts, sizes, spacing, radii and
   shadows are presets. Templates reference presets. `style.css` holds only what
   `theme.json` can't express. This is what makes a theme re-skinnable.
3. **Presentation in the theme, data in a plugin.** Custom post types, taxonomies, meta,
   shortcodes, custom blocks and REST routes are "plugin territory" — the WordPress.org
   review rejects them in themes, and users lose content on theme switch. When a project
   needs them, create a small companion plugin. For a personal site where the user says
   they don't care, say so once and follow their call.
4. **Core blocks first.** Reach for a custom block only for real interactivity or data
   processing (filters, calculators, forms, galleries with lightbox, maps).
5. **Nothing hard-coded that belongs to one site.** Brand names, phone numbers, addresses,
   social URLs, colours, fonts. Use Site Logo/Title/Tagline blocks, `theme.json`,
   patterns with placeholder content, and style variations.
6. **Verify by looking.** Screenshot what you built and compare it to the reference.
   Don't report "done" from code alone.
7. **Design is a choice, not a default.** Before any tokens, write a 10-line design
   plan grounded in the site's subject and review it against the generated-page tells
   in `references/design-quality.md`. One memorable element, everything else quiet.
   Real copy, not placeholder slogans.
8. **Match the WordPress version.** Check `wp core version` (or ask) before using newer
   `theme.json` features; see `references/theme-json-cheatsheet.md`.

## Workflow

Adapt the order to the project. A new theme from designs usually goes: tokens → shell →
sections → data → polish. A fix to an existing theme skips straight to the section.

**Orient.** Find the theme root (`style.css` with a `Theme Name` header). Note the WP
version, whether it's a block or classic theme, which plugins supply data, and whether
a design system already exists in `theme.json`. If the environment isn't running, ask
how the user runs WordPress locally rather than assuming a tool.

**Design plan + tokens (new theme or redesign).** Write the short design plan
(`references/design-quality.md` §2), critique it for defaults, then — from the reference
image if there is one — extract a design system and write it as `theme.json` presets
before any template. Method and skeleton: `references/design-from-reference.md` and
`references/theme-json-cheatsheet.md`.

**Shell.** `style.css` header, `theme.json`, `templates/index.html`,
`parts/header.html`, `parts/footer.html`, a `functions.php` that does little more than
enqueue the stylesheet and register pattern categories / block styles.

**Sections.** One reference image (or one request) at a time: decide pattern vs template
vs template part, build with core blocks, screenshot at desktop and mobile widths, score
it against the rubric in `references/design-from-reference.md`, iterate up to three
times, then report gaps. Build order that avoids rework: header/footer → the component
reused most (a card, a post item) → home → archives/listings → single views → utility
pages (contact, 404, search).

**Data (when the site needs structured content).** Companion plugin with CPTs,
taxonomies and `register_post_meta()` (`show_in_rest => true`, schema, sanitize
callback). Display meta in templates through Block Bindings; add a custom binding source
when values need formatting. Lists via Query Loop. Interactive filtering via the
Interactivity API with a no-JS fallback. Details in `references/block-theme-standards.md`.

**Polish and handoff.** Style variations, i18n, accessibility, performance, Theme Check /
Plugin Check, README, zip. Run `references/qa-checklist.md` and
`node scripts/validate_theme.mjs <theme-dir> [--plugin <plugin-dir>]`.

## When reference images are provided

Treat them as specs, not inspiration. Write a short "what I see" note first (grid, type,
colours, components), build, then screenshot and compare. If only a desktop view is
given, design the mobile layout yourself and say what you decided. If a screenshot
tool isn't available, ask the user to paste screenshots — don't skip the check.

## SEO and discoverability (theme's share)

A theme's job is to be crawlable and fast: one `<h1>` per template, semantic landmarks,
breadcrumbs block where it fits, no render-blocking fonts, responsive images with
dimensions, server-rendered content, and no duplicate meta/schema output when an SEO
plugin is active. Structured-data strategy, metadata, robots/sitemap, snippet controls and
AI-search visibility are the `seo-aeo-geo` skill's job (same repo, `seo-aeo-geo-skill/`);
when it's installed, defer to its ground truth and priorities rather than this file's
notes — in particular, don't add FAQPage/HowTo schema or `llms.txt` as "SEO wins".

## Verification

- `scripts/validate_theme.mjs` passes (header fields, `theme.json` valid, no raw hex in
  markup, no external font CDNs, no plugin-territory code in the theme, text domain
  consistent, meta registered with `show_in_rest`).
- Screenshots at ~1440px and ~390px match the reference (score ≥ 8/10) or gaps are listed.
- The §10 self-critique in `references/design-quality.md` has been answered for the page;
  no generated-page tells are present by default.
- No PHP notices with `WP_DEBUG` on; no console errors.
- Templates render sensibly with empty/missing optional data.

## Failure modes

- `theme.json` changes not showing → caching; set `WP_DEVELOPMENT_MODE` to `theme` in
  local config, or the user has Site Editor customizations stored in the DB overriding
  the files ("Clear customizations").
- Bound block renders empty → meta not registered with `show_in_rest`/`single`, or
  wrong key.
- Template parts in subfolders are ignored → keep `parts/` flat.
- Styles differ between editor and front end → missing `editor-style` support or CSS
  written outside `theme.json`; prefer presets.
- "Invalid block" after theme switch → malformed block comments in templates/patterns;
  validate markup by inserting the pattern in the editor.

## References

- `references/design-quality.md` — the taste layer: subject-first planning, the list of generated-page tells, typography/colour/motion/copy rules, self-critique
- `references/design-from-reference.md` — reading a mockup, extracting tokens, the 10-point matching rubric, anti-"templated" tips
- `references/theme-json-cheatsheet.md` — feature availability by WP version, a complete `theme.json` skeleton, style variations, templates/parts list
- `references/block-theme-standards.md` — file structure, plugin/theme split, Block Bindings, Interactivity API, i18n, escaping, performance, accessibility, WordPress.org rules
- `references/qa-checklist.md` — handoff checklist
- `scripts/validate_theme.mjs` — static checks; run after every meaningful change
- `CLAUDE.md` — a project-instructions template to copy into a theme repo
