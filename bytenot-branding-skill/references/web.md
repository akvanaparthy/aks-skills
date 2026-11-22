# On the web

The guidelines are written for print and social. This file carries them onto websites and
interfaces. Everything here that the PDF does not state is an interpretation, built from its
rules and its application pages; when a choice here is contested, the PDF page decides.

## Contents
- Tokens
- Grounds and section rhythm
- Type
- Logo, symbol and bug
- Components
- Shape, pattern and photography
- Motion
- Accessibility
- Favicon and share images
- In the Bytenot site repository

## Tokens

Start from `assets/tokens.css`. It defines the eight colours, and for each ground the ink, the
display colour, the quiet step and the logo colours, selected with `data-ground`:

```html
<section data-ground="maroon"> ... </section>
```

Components read `--ground`, `--ink`, `--display`, `--logo-symbol` and `--logo-word`, so a
section changes ground without its contents knowing. There is no quieter step and no rule
colour: secondary text and hairlines use `--ink` at full strength. Never write a hex in a
component: a colour that is not a token is how off-palette values arrive.

## Grounds and section rhythm

A page is a sequence of surfaces. Decide the sequence first, as a table:

| Section | Ground | Text colour | Symbol or device |
| --- | --- | --- | --- |

Rules for the sequence:

- **Orange and Maroon lead.** Each should hold at least one full section, not only buttons and
  cards. Mint and Milk White carry the long reading in between.
- **Change ground when the subject changes.** Sections that are read sit on Milk White, Maroon
  or the Maroon tint; the Orange tint, the Mint shade and Grey are for ornament.
- **One text colour per section** (see colour.md). Decide per section whether it is a display
  section (few large words, display colour allowed) or a reading section (reading colour).
- **Long or small copy never sits on Orange**; put it in a white block, or on Maroon, Milk White
  or the Maroon tint.
- Neighbouring sections should differ clearly: avoid Mint beside Milk White, or a tint beside its
  parent, without a block or band between them.
- Check each row with `python scripts/brand_check.py pair <ground> <ink>`.

## Type

See typography.md for the three styles and their CSS. Additional points for interfaces:

- Everything is aligned left, including hero headlines, statements and footers. Centre a block on
  the page if the layout needs it, but the lines inside it start at one left edge.
- Sentence case for navigation, buttons, labels and headings.
- Use a Heading once or twice per page, Subheadings for section titles, Body for the rest.

## Logo, symbol and bug

See logo.md for files, minimum size, clear space and misuse.

- **Header.** Clear space is the logo's own height above and below, so a slim bar cannot hold the
  logo: use the symbol there (it needs its own height and width clear), and show the full logo
  where it has room, in the hero or at the head of a menu.
- **Footer.** One logo, still, with its clear space, on a ground from the matrix.
- **Once per view.** The logo is a signature; do not repeat it as decoration or tile it.
- Render it as inline SVG or an `<img>` of the file for that ground. Scale by height, keep the
  aspect ratio, and never set colours on it that the matrix does not give.
- Minimum 20px high for the logo and the wordmark.

## Components

- **Buttons.** A flat rectangle in the display or ink colour of the ground, label in the colour
  the matrix gives for that fill: Maroon button with Mint label, Mint button with Maroon label,
  Orange button with a Maroon or Mint label set large enough (Orange never reaches 4.5:1).
  Corners are rounded, in the spirit of the symbol; keep the radius consistent.
  No gradients, glows, bevels or drop shadows.
- **Links.** The section's text colour, underlined. Not a second colour.
- **Focus.** A 2px outline in the section's ink colour, offset 2px.
- **Forms.** Fields are a palette colour on a palette colour with a 1px edge in the ink colour. Errors are said with words and an icon in the ink colour; Orange may outline
  the field. Do not introduce red or green.
- **States.** Hover, active and disabled change shape, position or an underline, or swap to
  another given pairing. Never a fade and never a new shade.
- **Rules and borders.** The ink colour at full strength, 1px.

## Shape, pattern and photography

See imagery-and-elements.md.

- Build layout on a grid, with shapes that are soft and rounded like the symbol's. Illustrations
  and icons are drawn the same way: no pixel, bit or glyph look (owners' ruling, SKILL.md).
- A pattern is a panel or a band beside content. Nothing readable goes on top of it.
- Photographs are real, bright, in colour, of people working. Client work is shown as real
  screenshots. No stock, no generated people, no black and white.
- No gradients anywhere: not as backgrounds, overlays, text fills or image scrims. To make text
  readable over a photograph, put it on a solid block beside or below the image, as the posters
  do. A soft fade made with a mask is a gradient to the eye and is avoided the same way.
- No blur, glass, glow or drop-shadow effects on brand elements.

## Motion

The PDF is silent on motion. Keep it in the brand's character, calm and exact:

- Movement is smooth and fluid, the way the symbol's shapes run into one another: glide, merge,
  part, settle. Stepped, cell-by-cell and pixel effects read as technical; the owners do not
  want that look.
- The logo follows logo.md: whole, upright, undistorted.
- Type may move. While it does and where it comes to rest it is still Gabarito, in sentence
  case, unstretched, and readable; it rests aligned left.
- Colours cut or wipe between approved pairings; they do not cross-fade through off-palette
  mixtures across large areas for longer than a moment.
- Respect `prefers-reduced-motion`: the still state must be complete and on-brand by itself.

## Accessibility

- Reading text meets 4.5:1; large type and meaningful shapes meet 3:1. The matrix gives the
  figures. Orange type is display only.
- Colour is never the only signal: pair it with words, icons or shape.
- Targets are at least 24px; focus is always visible.

## Favicon and share images

- Favicon, app icon and avatars: the bug (`assets/logo/bug.svg`), or the app icon from the brand
  pack. Apple touch icons want a full square: Orange ground, Mint symbol.
- Share images follow the "statement on a field" recipe in applications.md: Maroon or Orange
  ground, one-colour logo top left with its clear space, tagline or page title left aligned, a
  pattern band or blocks on one edge.

## In the Bytenot site repository

- Tokens: `src/styles/tokens.css` (palette and type scale) and `src/styles/surface.css` (roles per
  `data-surface`). The grounds are named `paper` (Mint), `surface` (Milk White), `ink` (Maroon),
  `orange`, `orange-tint`, `maroon-tint` and `mint-shade`; a section card takes one as its
  `surface` prop. Brand shapes: `src/styles/brand.css`.
- Logo: `src/components/brand/logo.tsx` draws the vector and takes its colours from
  `--logo-symbol` and `--logo-word`.
- The original brand files are in `Branding/` at the repository root (not committed).
- After changing styles, run `python .agents/skills/bytenot-branding/scripts/brand_check.py scan src`
  and the project's own tests (`npm test`), which pin the palette, the type scale and contrast.
