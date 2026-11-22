# Logo

Source: guidelines pages 13-22, and page 29 for colour.

## Contents
- The four elements
- Which file for which ground
- Minimum size
- Clear space
- Partnerships
- Misuse
- The logo in motion and on the web

## The four elements

"The logo, wordmark, symbol, and bug work together to form our full identity system." (p16)

| Element | What it is | When |
| --- | --- | --- |
| Logo | symbol + wordmark | first choice: "used most frequently because it carries the most detail" |
| Wordmark | "Bytenot" alone | next in order of usage |
| Symbol | the mark alone, "an open package" (p15) | next in order of usage; avatars, corners, tight spaces |
| Bug | the symbol in a disc | "kept for situations where it is specifically needed": app icon, favicon, profile picture |

The logo scales: "at larger scales, it conveys a more bold presence while smaller scales are more
reserved" (p17). Consider the audience, the goal and the tone when choosing a size.

The wordmark is drawn, not typed. Never rebuild it from the Gabarito font, and never set the word
"Bytenot" in running text to stand in for the logo.

## Which file for which ground

Files are in `assets/logo/`. Colour is fixed by the ground (see [colour.md](colour.md)).

| Ground | Logo | Symbol |
| --- | --- | --- |
| Milk White | `logo-on-light.svg` | `symbol-orange.svg` |
| Maroon | `logo-on-maroon.svg` (Orange symbol, Milk White wordmark) | `symbol-orange.svg` |
| Orange | `logo-mint.svg` or `logo-maroon.svg` | `symbol-mint.svg` |
| Maroon tint | `logo-maroon.svg` | `symbol-maroon.svg` |
| Mint shade | `logo-mint.svg` | `symbol-mint.svg` |
| Grey | `logo-milk.svg` | `symbol-milk.svg` |
| Off-palette colour or photo | `logo-black.svg` or `logo-white.svg` (p29) | black or white |

Also: `wordmark-maroon.svg`, `wordmark-milk.svg`, `bug.svg` (Orange disc, light symbol, as the
brand pack exports it).

The light logo is Milk White, by the owners' ruling and as the brand pack's logo files have it.

"On dark colours, use it primarily in light colours and on light colours use it primarily in
dark." (p21) On Maroon the guidelines show both the two-colour logo and an all-light one; the
all-light logo is the one their posters, cards and banner use.

The originals, with print formats, live in the project's `Branding/Logo/` folder.

## Minimum size

Logo and wordmark: no smaller than **20px high** (p18). Below that, use the symbol or the bug.
"Always use your best judgment when scaling identity elements."

## Clear space

"When placing additional elements around the identity elements, be sure not to crowd them." (p19)

| Element | Clear space on every side |
| --- | --- |
| Logo | the symbol's height above and below, the symbol's width left and right |
| Wordmark | the wordmark's cap height |
| Symbol | the symbol's own height and width |
| Bug | the bug's own height and width |

The symbol is as tall as the whole logo, so a logo needs its own height free above and below: it
can never be taller than a third of the space it sits in. The symbol's width is 0.8 of its height.

```bash
python scripts/brand_check.py logo --height 96 --top 120 --bottom 96 --left 80 --right 300
```

Treat the edge of a page, screen, card or image as an element: keep the same margin to it.

## Partnerships

Beside another brand, use the co-branding device (p20): our logo or symbol, then a small Orange
square as the divider, then the partner's mark. The guidelines call the divider "the diamond
shape from the symbol". In a lockup, "the logo and symbol [are] best used in black or white
colour".

## Misuse

Page 22, "Do not diminish the value of our identity":

1. Do not stretch or distort.
2. Do not use unapproved colours.
3. Do not outline.
4. Do not modify logo colour applications (for instance a Maroon symbol with an Orange wordmark).
5. Do not change logo placement (the symbol stays left of the wordmark, at its drawn distance).
6. Do not apply effects (shadows, glows, blurs, bevels).
7. Do not use low contrast combinations.
8. Do not rotate.

## The logo in motion and on the web

The PDF does not cover motion. These follow from the misuse list and are interpretations:

- The logo may appear, fade, slide as a whole, and scale uniformly. Its parts stay locked
  together at their drawn distance while it does.
- It never rotates, skews, stretches or bends along a path; its letters are never pulled apart,
  staggered or sent round a curve; it is never masked into an outline, blurred or given a shadow.
- A colour change follows the ground beneath it and lands on an approved application; it does not
  pass through an off-palette colour on the way.
- Kinetic typography is welcome, but it is typography: set it in Gabarito with real words such
  as the tagline. Do not animate the logo's own letterforms as if they were type, and do not set
  "Bytenot" in the font to imitate the wordmark.
- Clear space applies on screen exactly as on paper. A logo in a navigation bar needs its own
  height free above and below, which usually means the bar carries the symbol, not the logo.
