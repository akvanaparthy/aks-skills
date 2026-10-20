# Handoff QA checklist

Use the sections that apply. Record results in the project's `QA.md`.

## WordPress compliance
- [ ] Theme Check plugin: 0 errors. Plugin Check on any companion plugin: 0 errors.
- [ ] `php -l` on all PHP; PHPCS `WordPress` / `WordPress-Theme` rulesets clean of errors.
- [ ] `scripts/validate_theme.mjs` passes.
- [ ] No plugin-territory code in the theme (CPT, taxonomy, meta, shortcode, block, REST).
- [ ] All strings translatable with the right text domain; `.pot` generated.
- [ ] Everything prefixed with the theme slug.
- [ ] `style.css` header complete; `readme.txt`; `screenshot.png` 1200×900.
- [ ] No block validation errors when activating the theme.
- [ ] Theme renders with companion plugin deactivated; plugin works on a default theme.

## Design parity
- [ ] Each reference image has a scored screenshot (≥ 8/10) at ~1440px and ~390px.
- [ ] Any dark/alternate style variation checked for contrast.

## Accessibility (WCAG 2.2 AA)
- [ ] Keyboard-operable navigation, menus, tabs, modals, galleries; visible focus.
- [ ] Skip link; landmarks; single H1; heading order.
- [ ] Contrast ≥ 4.5:1 text / 3:1 UI for every used palette pair.
- [ ] Forms labelled; errors and success announced.
- [ ] Meaningful `alt`; `prefers-reduced-motion` honoured.
- [ ] axe-core: 0 critical/serious.

## Performance
- [ ] Lighthouse mobile (throttled) on home, an archive, a single view: Performance ≥ 90; LCP ≤ 2.5 s, CLS ≤ 0.1, INP ≤ 200 ms.
- [ ] Fonts self-hosted, preloaded, `swap`.
- [ ] No jQuery; scripts load only where used.
- [ ] Responsive images with dimensions; hero `fetchpriority="high"`.
- [ ] Embeds click-to-load.

## Technical SEO (theme share)
- [ ] One H1 per template; breadcrumbs where sensible.
- [ ] No duplicate title/meta/schema when an SEO plugin is active.
- [ ] Internal search results `noindex`; archives/pagination crawlable.
- [ ] Sitemap includes public post types.

## Security
- [ ] Output escaped, input sanitized, nonces + capability checks on writes.
- [ ] No secrets in repo; `.gitignore` in place.

## Packaging
- [ ] Zip excludes `node_modules`, `vendor`, `src`, `.git`, dev configs; `unzip -l` reviewed.
- [ ] Versions bumped; CHANGELOG updated; README covers install, settings, customization, style variations.
- [ ] Fresh-install test on a clean WordPress: upload, activate, import demo content, compare to reference.
