# Design from reference images

The user supplies screenshots or mockups for each page. The job is to reproduce the
design faithfully in WordPress block markup and `theme.json`, not to "take inspiration".
Treat each image as a spec.

## 1. Read the image before writing anything

Answer these in a short written note (the user sees it and can correct you):

1. **Grid**: content width, number of columns, gutter. Is the hero full-bleed?
2. **Type**: how many font families (usually one display + one body). Weight of the
   largest heading. Approximate size ratio between H1, H2, body, caption.
3. **Colour**: background, text, primary (buttons/links), accent, surface (cards),
   border. Sample actual values if the image is sharp; otherwise choose the nearest
   sensible value and say so.
4. **Shape language**: corner radius (0 / 8 / 16 / pill), shadow depth, border usage.
5. **Density**: generous (editorial, luxury) vs compact (dashboard, catalogue grid).
6. **Components present**: hero, search bar, stat strip, card grid, tabs, slider,
   testimonial, CTA band, footer columns, sticky mobile CTA, etc.
7. **Motion implied**: hover lifts, image zoom, reveal-on-scroll. Default to subtle CSS
   transitions only; respect `prefers-reduced-motion`.

If the image is a desktop view only, design the mobile layout yourself using these rules:
single column, hero text above image, primary CTA kept visible (sticky bar if the design
has one), filters/menus collapse into a drawer, card grids become 1-column or a
horizontal scroll.

## 2. Tokens into `theme.json`, not CSS

Everything measured in step 1 becomes a preset. Templates and patterns then reference
presets (`var:preset|color|primary`, `var:preset|spacing|50`). This is what makes the
theme reusable: another company changes the preset values or picks a style variation and
every page follows.

Checklist for the tokens phase:

- `settings.color.palette` — 6–10 entries; include `base`, `contrast`, `primary`,
  `accent`, `surface`. Disable `defaultPalette` and `defaultGradients`.
- `settings.typography.fontFamilies` — self-hosted `fontFace` entries (download WOFF2
  into `assets/fonts/`); `fluid: true`; `fontSizes` with explicit `fluid.min/max`.
- `settings.spacing.spacingSizes` — 20/30/40/50/60/70/80 with `clamp()` values;
  `blockGap: true`, `padding: true`, `margin: true`.
- `settings.layout.contentSize` / `wideSize` from the measured grid.
- `settings.custom` — `radius.sm/md/lg/pill`, `shadow.card/hover`, `header.height`,
  `transition`. Reference as `var(--wp--custom--radius--md)`.
- `styles.elements` — `heading` weights/line-heights, `link` colours (+ `:hover`),
  `button` background/radius/padding (+ `:hover`/`:focus` on WP 7.1+).
- `styles.blocks` — `core/post-featured-image` radius, `core/group` surface
  variations, `core/button` outline style.

Register block styles for recurring visual variants (`card`, `card-elevated`,
`pill`, `ghost`) with `register_block_style()` so editors can pick them.

## 3. Build the section

- Prefer core blocks. Group/Row/Stack/Grid cover most layouts. Cover block for heroes.
- Query Loop for any list of posts or custom post type items, with a reusable card
  pattern as the inner template.
- A plugin block only when the section needs data processing or interactivity
  (search bar, filter drawer, EMI calculator, gallery with lightbox, map, enquiry form).
- Images in patterns are placeholders from `assets/images/` sized to the reference's
  aspect ratio; mark them with `"lock":{"remove":true}` off so editors can replace.
- Write pattern PHP with `<?php echo esc_url( get_theme_file_uri( 'assets/images/…' ) ); ?>`
  and `esc_html_e()` for every string.

## 4. Verify with Playwright

Screenshot `http://localhost:8888/<page>` at viewports 1440×900 and 390×844 with
`fullPage: true`. Put the reference and the screenshot side by side mentally and score:

| # | Criterion | Pass condition |
|---|---|---|
| 1 | Layout structure | Same sections in same order, same column counts |
| 2 | Content width & alignment | Within ~5% of reference |
| 3 | Type hierarchy | Heading/body size ratios feel the same; same weights |
| 4 | Colour | Backgrounds, text, primary and accent match the palette |
| 5 | Spacing rhythm | Section padding and card gaps proportionally similar |
| 6 | Imagery treatment | Aspect ratios, radius, overlays/gradients match |
| 7 | Components | Buttons, badges, cards, inputs look like the reference |
| 8 | Mobile | 390px layout is usable: no overflow, tap targets ≥ 44px, sticky CTA |
| 9 | Interactions | Hover/focus states exist and are subtle; reduced-motion respected |
| 10 | Polish | No default WP styling leaking (blue links, grey borders, system fonts) |

Score each 0/1 and report `n/10` with the failing items. Iterate up to three times.
If still < 8, stop and show the user the screenshot with the specific gaps — some
differences (e.g., a photo that doesn't exist yet) are not yours to fix.

## 5. Things that make WordPress output look "templated" — avoid

- Default `core/button` blue, default `core/separator` grey, default link underline
  colours → override in `theme.json`.
- Leaving `blockGap` at default; luxury designs need larger vertical rhythm.
- Using `core/columns` for everything; use `core/group` with `layout: grid` for card
  grids so they reflow properly.
- Mixed radius values; pick two (`md` for cards, `pill` for buttons/badges) and stick
  to them.
- Uppercase + letter-spacing on every label; use it only where the reference does.
- Shadows on everything. One card shadow, one hover shadow.
- System font stack because fonts weren't self-hosted.
