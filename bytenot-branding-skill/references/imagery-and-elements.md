# Photography, patterns and layout

Source: guidelines pages 38-50.

## Contents
- Photography principles
- Photography misuse
- Patterns
- Square shapes and the stepped mask
- Grids

## Photography principles

"Photography is a key part of our identity system... Every photo highlights humanity, the beauty
of our environment, and the real communities we serve. It should feel genuine and grounded,
capturing moments that reinforce our brand's warmth and trustworthiness." (p39)

"All photos should carry an editorial feel, capturing real moments, telling a story, and appearing
natural rather than overly staged or generic." (p40) Use the three principles as a checklist:

1. **Authentic** (p41). "Replace generic stock photos with real, transparent proof of your team,
   work environment, and actual processes. Subjects should look like everyday people, not
   polished models, to build trust and relatability."
2. **Uplifting** (p42). "Each image should convey a sense of joy, comfort, or satisfaction... the
   atmosphere should be positive. To evoke warmth and positivity, the lighting should be bright
   and open."
3. **Dynamic** (p43). "Clean, well-lit office environments featuring developers or designers
   working on dual monitors, laptops, and clean tech setups... This energy shows the brand is
   agile, hardworking, and always moving forward."

In practice: people at work with other people, colour, daylight, a real room.

## Photography misuse

Page 44:

1. Do not use obvious stock imagery.
2. Do not use low res photos.
3. Do not use staged photography.
4. Do not use sombre imagery.
5. Do not use black and white photography.
6. Do not use distracting or off topic imagery.

Generated images of people or offices that do not exist fail "authentic" for the same reason
stock does. If there is no real photograph, use pattern, colour and type instead, and say that a
real photograph is wanted.

Screenshots of real client work are honest proof and are welcome; show them whole and in colour.

## Patterns

A pattern is "an integral part of a brand's visual identity system alongside the logo, color
palette, typography, and imagery" (p47). There are two, both built from squares on a grid.

| Pattern | Colours | Repeat | File |
| --- | --- | --- | --- |
| Tall and short | Orange on Mint | 2 columns by 3 rows: a tall block (2 rows) in the second column, then a short block (1 row) in the first | `assets/patterns/pattern-orange-on-mint.svg`, tile `tile-tall-short.svg` |
| Two-tone | Orange and Maroon | 3 columns by 2 rows: Orange, Maroon, Orange over Maroon, Orange, Maroon | `assets/patterns/pattern-orange-and-maroon.svg`, tile `tile-two-tone.svg` |

Rules read from pages 47-49 and the applications:

- Cells are square and sit on the layout's grid; a pattern is never stretched, rotated or drawn
  with rounded or soft cells.
- Colours are fixed: Orange on Mint, or Orange with Maroon. No tints in a pattern, no gradient.
- A pattern works as a field (a panel of its own), a band along one edge, or a corner that breaks
  into loose squares (banner p57). It sits beside type, not under it.
- No text over a pattern. Words go on the plain field next to it.

CSS, for the tall-and-short pattern at any cell size:

```css
background-image: url("tile-tall-short.svg");
background-size: calc(var(--cell) * 2) calc(var(--cell) * 3);
```

## Square shapes and the stepped mask

**The owners' ruling comes first.** The symbol's squares have smooth, rounded corners and merge
fluidly into each other, and new work takes after that: soft, rounded, flowing shapes. A look
built from pixels, bits, bytes or hard-edged glyphs makes the brand feel technical, and the
owners do not want it. Read what follows as a record of what the PDF's pages show, not as an
instruction to make everything square.

"Square shapes still play a roll in how we create patterns and layouts." (p49) Everything is
built from squares and rectangles on the grid:

- **Blocks.** Flat squares and rectangles of Orange and Maroon, butted edge to edge, as on the
  business cards and the lanyard.
- **The symbol's square.** A small square of colour holding the symbol, set in a corner.
- **The stepped mask.** A photograph cropped to a silhouette of stacked squares, like a staircase
  or the symbol's own outline (posters p49 and p53, post p58). Steps are whole grid cells.
- On the PDF's pages the blocks have square corners. By the owners' ruling above, new
  illustrations, icons and interface shapes are rounded instead: rounded cards, pills and
  circles are welcome.

## Grids

"The grids provide guidance for creating compositions across different layouts." (p50)

| Layout | Grid (columns by rows) |
| --- | --- |
| Vertical | 9 by 12 |
| Square | 9 by 9 |
| Horizontal | 12 by 9 |

Cells are square. "The red line indicates the text margin, aligned to the centre of the first
square grid box": text starts half a cell in from every edge. Blocks, pattern cells and photo
steps snap to whole cells.

On the web, a 12-column grid with square units and a half-unit text margin keeps the same logic
(interpretation).
