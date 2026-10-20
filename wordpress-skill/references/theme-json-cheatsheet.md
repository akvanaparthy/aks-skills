# theme.json cheatsheet by WordPress version

Check the running version first: `npx wp-env run cli wp core version`.
Set `"$schema": "https://schemas.wp.org/trunk/theme.json"` for editor hints and keep
`"version": 3` (schema v3 has been current since WordPress 6.6; use a higher number
only if the target site's core docs say so).

| Feature | Available since | Notes |
|---|---|---|
| `settings.appearanceTools: true` | 6.1 | Turns on border/color/spacing/typography tools |
| `settings.useRootPaddingAwareAlignments` | 6.1 | Needed for full-bleed heroes with root padding |
| Fluid typography (`fluid: true`) | 6.1 | Per-size `fluid.min/max` from 6.5 |
| `spacingSizes` presets | 6.2 | |
| `shadow.presets` | 6.2 | |
| `styles.css` (custom CSS in theme.json) | 6.2 | Keep small; prefer presets |
| `behaviors`/lightbox → `blocks.core/image.lightbox` | 6.4 | Enable for gallery images |
| Block Bindings `core/post-meta` | 6.5 | Needs `show_in_rest` meta |
| Section styles (`styles.blocks.core/group.variations`) | 6.6 | Great for "surface" cards |
| `styles.elements.button` with `:hover`/`:focus`/`:active` | **7.1** | Before 7.1, do it in `style.css` |
| Responsive styles `@mobile` / `@tablet` keys under styles | **7.1** | Only for properties that go through block supports |
| `settings.viewport` custom breakpoints | **7.1** | Shared theme-wide; default ranges used if omitted |
| Navigation `-current` custom state | **7.1** | theme.json only, no UI |
| Text shadow in theme.json | **7.1** | |
| Tabs block, Playlist block | **7.1** | Tabs suits spec sheets, FAQs, feature groups |
| Site-level "Guidelines" (AI content rules) | 7.1 | Editorial, not a theme concern; mention in README |

If the target is 7.0: write hover/focus and responsive overrides in `style.css` using
the preset custom properties (`var(--wp--preset--color--primary)`), and keep a comment
block "move to theme.json when on 7.1+".

## Skeleton to copy

```json
{
  "$schema": "https://schemas.wp.org/trunk/theme.json",
  "version": 3,
  "settings": {
    "appearanceTools": true,
    "useRootPaddingAwareAlignments": true,
    "layout": { "contentSize": "72rem", "wideSize": "88rem" },
    "color": {
      "defaultPalette": false, "defaultGradients": false, "defaultDuotone": false,
      "palette": [
        { "slug": "base", "name": "Base", "color": "#ffffff" },
        { "slug": "contrast", "name": "Contrast", "color": "#101418" },
        { "slug": "primary", "name": "Primary", "color": "#0f3d3e" },
        { "slug": "primary-dark", "name": "Primary dark", "color": "#0a2a2b" },
        { "slug": "accent", "name": "Accent", "color": "#c8a24b" },
        { "slug": "surface", "name": "Surface", "color": "#f6f5f2" },
        { "slug": "surface-2", "name": "Surface 2", "color": "#ebe9e4" },
        { "slug": "border", "name": "Border", "color": "#dcd9d2" },
        { "slug": "success", "name": "Success", "color": "#1f7a4d" },
        { "slug": "warning", "name": "Warning", "color": "#b65c0b" }
      ]
    },
    "typography": {
      "fluid": true, "writingMode": true,
      "fontFamilies": [
        { "slug": "display", "name": "Display", "fontFamily": "\"Fraunces\", Georgia, serif",
          "fontFace": [ { "fontFamily": "Fraunces", "fontWeight": "300 700", "fontStyle": "normal", "fontDisplay": "swap", "src": [ "file:./assets/fonts/fraunces-var.woff2" ] } ] },
        { "slug": "body", "name": "Body", "fontFamily": "\"Inter\", \"Noto Sans\", system-ui, sans-serif",
          "fontFace": [ { "fontFamily": "Inter", "fontWeight": "400 700", "fontStyle": "normal", "fontDisplay": "swap", "src": [ "file:./assets/fonts/inter-var.woff2" ] } ] }
      ],
      "fontSizes": [
        { "slug": "x-small", "size": "0.8125rem", "fluid": false },
        { "slug": "small", "size": "0.9375rem", "fluid": false },
        { "slug": "medium", "size": "1.0625rem", "fluid": { "min": "1rem", "max": "1.125rem" } },
        { "slug": "large", "size": "1.375rem", "fluid": { "min": "1.25rem", "max": "1.5rem" } },
        { "slug": "x-large", "size": "1.875rem", "fluid": { "min": "1.625rem", "max": "2.125rem" } },
        { "slug": "xx-large", "size": "2.75rem", "fluid": { "min": "2.125rem", "max": "3.25rem" } },
        { "slug": "xxx-large", "size": "4rem", "fluid": { "min": "2.75rem", "max": "4.75rem" } }
      ]
    },
    "spacing": {
      "blockGap": true, "margin": true, "padding": true, "units": [ "px", "rem", "em", "vh", "vw", "%" ],
      "spacingSizes": [
        { "slug": "20", "name": "1", "size": "0.5rem" },
        { "slug": "30", "name": "2", "size": "clamp(0.75rem, 2vw, 1rem)" },
        { "slug": "40", "name": "3", "size": "clamp(1rem, 3vw, 1.5rem)" },
        { "slug": "50", "name": "4", "size": "clamp(1.5rem, 4vw, 2.5rem)" },
        { "slug": "60", "name": "5", "size": "clamp(2.5rem, 6vw, 4rem)" },
        { "slug": "70", "name": "6", "size": "clamp(3.5rem, 8vw, 6rem)" },
        { "slug": "80", "name": "7", "size": "clamp(5rem, 10vw, 8rem)" }
      ]
    },
    "shadow": { "defaultPresets": false, "presets": [
      { "slug": "card", "name": "Card", "shadow": "0 1px 2px rgba(16,20,24,.06), 0 8px 24px rgba(16,20,24,.06)" },
      { "slug": "hover", "name": "Hover", "shadow": "0 12px 32px rgba(16,20,24,.12)" } ] },
    "custom": {
      "radius": { "sm": "6px", "md": "14px", "lg": "24px", "pill": "999px" },
      "transition": "180ms cubic-bezier(.2,.8,.2,1)",
      "header": { "height": "4.5rem" }
    }
  },
  "styles": {
    "color": { "background": "var:preset|color|base", "text": "var:preset|color|contrast" },
    "typography": { "fontFamily": "var:preset|font-family|body", "fontSize": "var:preset|font-size|medium", "lineHeight": "1.6" },
    "spacing": { "padding": { "left": "var:preset|spacing|40", "right": "var:preset|spacing|40" }, "blockGap": "var:preset|spacing|50" },
    "elements": {
      "heading": { "typography": { "fontFamily": "var:preset|font-family|display", "fontWeight": "500", "lineHeight": "1.1", "letterSpacing": "-0.01em" } },
      "h1": { "typography": { "fontSize": "var:preset|font-size|xxx-large" } },
      "h2": { "typography": { "fontSize": "var:preset|font-size|xx-large" } },
      "link": { "color": { "text": "var:preset|color|primary" }, ":hover": { "color": { "text": "var:preset|color|primary-dark" } } },
      "button": {
        "color": { "background": "var:preset|color|primary", "text": "var:preset|color|base" },
        "border": { "radius": "var(--wp--custom--radius--pill)" },
        "spacing": { "padding": { "top": "0.8rem", "bottom": "0.8rem", "left": "1.5rem", "right": "1.5rem" } },
        "typography": { "fontWeight": "600" },
        ":hover": { "color": { "background": "var:preset|color|primary-dark" } },
        ":focus": { "outline": { "width": "2px", "style": "solid", "color": "var:preset|color|accent", "offset": "2px" } }
      }
    },
    "blocks": {
      "core/post-featured-image": { "border": { "radius": "var(--wp--custom--radius--md)" } },
      "core/group": { "variations": {
        "surface": { "color": { "background": "var:preset|color|surface" }, "border": { "radius": "var(--wp--custom--radius--md)" } } } }
    }
  },
  "templateParts": [
    { "name": "header", "title": "Header", "area": "header" },
    { "name": "footer", "title": "Footer", "area": "footer" }
  ],
  "customTemplates": [
    { "name": "page-landing", "title": "Landing (full-bleed)", "postTypes": [ "page" ] }
  ]
}
```

The `:hover` / `:focus` keys above require 7.1+. On 7.0 remove them and add
equivalent rules to `style.css`.

## Style variations

`styles/<name>.json` files containing only the overrides (palette, fonts). Ship:
`luxury-dark.json`, `clean-minimal.json`, `warm-earth.json`, `corporate-blue.json`.
Each also declares `"title"`. Users pick them in Styles → Browse styles; the choice is
stored in the DB, so changing the file later won't update sites that already picked it.

## Templates and parts to ship

Minimum: `templates/index.html`. Typical: `index`, `front-page`, `page`, `single`,
`archive`, `search`, `404`, plus `single-<cpt>` / `archive-<cpt>` / `taxonomy-<tax>`
for each custom post type the companion plugin registers, and custom page templates
(e.g. `page-landing`) declared in `customTemplates`.

`parts/`: `header`, `footer`, and anything repeated across templates (a sidebar, a
newsletter band). Keep `parts/` flat — subfolders are ignored. Repeated *inside* a
Query Loop (a card) should be a **pattern**, not a part.
