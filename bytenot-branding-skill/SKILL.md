---
name: bytenot-branding
description: Applies and enforces Bytenot's brand guidelines - the logo and its clear space, the eight-colour palette and its approved pairings, Gabarito typography, patterns, photography and voice. Use for anything made in Bytenot's name or in the Bytenot codebase - websites, landing pages, UI components, CSS or design tokens, social posts, decks, documents, emails, ads, share images and copy; whenever choosing or changing colours, fonts, logo placement or layout; and for brand audits, creative direction, and questions such as "is this on brand" or "which colour goes on this", even when the guidelines are not mentioned.
---

# Bytenot branding

Bytenot is a software studio: "Worry not about your tech." Its identity is fixed by a 62-page
guidelines PDF. This skill is that PDF made usable: the rules, the approved pairings, the files,
and a checker.

## The PDF is the authority

"Please follow it as written. Small changes made on personal preference add up, and they make a
young brand harder to recognise and harder to trust." (p2)

So: the PDF outranks this skill, and both outrank taste. When they seem to disagree, or a case
is not covered, open the page and look. The PDF is at
`Branding/Brand Guidelines/Bytenot Brand Guidelines Small Size.pdf` in the Bytenot repository
(read it by page number), and the pages that settle most questions are described in
[references/guideline-pages.md](references/guideline-pages.md).

Where the PDF is silent, decide from the nearest thing it does show, **say that it is an
interpretation**, and let the person overrule it. The reference files mark every such case.

## The owner's rulings

The owners have decided these points. They outrank this skill's interpretations and are not to
be reopened:

- **Only the eight colours, at full strength.** No shade made by opacity, mixing or tinting, for
  text, lines, borders or fills, unless the owner asks for one by name. Secondary text, hairlines
  and borders take the ground's text colour itself; hierarchy comes from size and weight.
  Shadows, the frosted navigation bar and similar depth effects are allowed to stay.
- **Only the given pairings.** What sits on a ground is what pages 21, 27 and 28 show for it
  (table below). Do not invent a pairing because it reads better: choose a different ground.
- **Milk White, not Mint, for light grounds.** Mint Chiffon is not used as a background.
- **On Maroon, text and the wordmark are Milk White**, with an Orange symbol. No Mint text there.
- **On Orange, symbol, logo and text are Mint**, as the guidelines' images show.
- **Reading sections sit on Milk White, Maroon or the Maroon tint.** The Orange tint, the Mint
  shade and Grey take tone-on-tone text that cannot be read, so they are for ornament only.
- **The footer's closing logo is large.** The clear-space rule is not applied to it.
- **The statement's reveal** brings each word in Orange and cools it to Maroon.
- **Shapes are soft, like the symbol's.** The symbol is made of squares with smooth, rounded
  corners that run fluidly into one another. Illustrations, icons, motion and interface shapes
  take after that: rounded, flowing, friendly. Do not build things out of pixels, bits, bytes
  or hard-edged glyphs. "Making it so bit/byte, glyph will make it too technical, we don't
  want it like that." (Interpretation: the two patterns on page 47 stay as the PDF draws them
  where a pattern is used, but they are one device, not the house style.)
- **Motion is smooth, one thing turning into the next.** No transitions made of blocks, bits or
  pixels. When a picture changes, its parts travel and reshape into the new picture.

When asked about one property (colour, say), change that property only. Do not also resize,
move or restyle. When a rule and readability collide, ask; do not improvise.

## Think in three roles

The rules keep work correct. These keep it good. Ask all three before showing anything:

- **Creative director.** Is it made well, and does it look like the guidelines' own posters,
  cards and banner: flat fields of Orange and Maroon, one idea per surface? Are its shapes soft
  and rounded like the symbol's, and does it feel warm rather than technical?
- **Brand strategist.** With the logo covered, is it still unmistakably Bytenot? Does it prove
  ownership, craft, clarity or calm, rather than claim them?
- **Head of marketing.** One audience (an owner who cannot read code), one message, one next
  step. Is the promise of no worry felt at once, and is the proof real?

A layout can pass every rule and still fail these, most often by being timid: nearly all white,
with Orange, the signature colour, reduced to dots.

## The system at a glance

**Colour** (full detail: [references/colour.md](references/colour.md))

| Name | Hex | Role |
| --- | --- | --- |
| Opulent Orange | `#EB6140` | the signature; leads with Maroon |
| Maroon Oak | `#4D1B1E` | leads with Orange; the dark reading colour |
| Milk White | `#FCFCFC` | the light ground; the light text and logo colour |
| Mint Chiffon | `#E9FFEF` | in the palette; not used as a ground or text colour on the site |
| Grey | `#BFBFBF` | neutral backdrop |
| Orange tint | `#F8CABE` | range |
| Maroon tint | `#ECCACC` | range |
| Mint shade | `#ACC3B2` | range |

What goes on each ground is fixed. "They were designed to work together, so they should be used
as intended." (p28)

| Ground | Symbol | Logo | Text |
| --- | --- | --- | --- |
| Milk White | Orange | Orange symbol + Maroon wordmark | Maroon for reading, Orange for display |
| Maroon | Orange | Orange symbol + Milk White wordmark | Milk White |
| Orange | Mint | all Mint, or all Maroon | Mint, short and large |
| Maroon tint | Maroon | all Maroon | Maroon |
| Orange tint | Orange | all Orange | Orange: ornament only, too faint to read |
| Mint shade | Mint | all Mint | Mint: ornament only, too faint to read |
| Grey | Milk White | all Milk White | Milk White: ornament only, too faint to read |
| Off-palette, photos | black or white | black or white | none |

Orange type never reaches 4.5:1, so on Milk White it is for a few large words and Maroon carries
the reading. "Ornament only" pairings are under 3:1: use those grounds for a symbol, a pattern
or a block, never for a section of text.

**Type** (full detail: [references/typography.md](references/typography.md))

Gabarito only. Sentence case. Aligned left.

| Style | Weight | Leading | Tracking |
| --- | --- | --- | --- |
| Heading | Bold 700 | 90% | +30 (`0.03em`) |
| Subheading | Medium 500 | 100% | -20 (`-0.02em`) |
| Body, 18px | Regular 400 | 130% | -10 (`-0.01em`) |

**Logo** (full detail: [references/logo.md](references/logo.md))

Logo first, then wordmark or symbol, the bug only where an icon is needed. At least 20px high.
Clear space: the symbol's height above and below, its width left and right, so a logo is never
taller than a third of the room it sits in. Files for every ground are in `assets/logo/`.

## Never

From the misuse pages (22, 29, 37, 44). These are not style preferences:

- **Colour.** No colour outside the eight, and no shade of one. No gradients. No low-contrast
  pairings. No pairing the guidelines do not show. No more than one text colour on a surface.
- **Logo.** No stretching, rotating, outlining, effects, recolouring or rearranging. No logo on
  an off-palette colour unless it is black or white. Never typed in the font.
- **Type.** No all caps, no all lowercase, no other typeface, no other weights, no centred or
  right-aligned text, no leading or tracking other than the three styles'.
- **Photography.** No obvious stock, no staged or sombre images, no black and white, no low
  resolution, nothing off topic.

## Making something

1. **Read what applies.** Colour and logo files for any visual work; add typography.md for
   layouts, [references/foundation.md](references/foundation.md) for any words,
   [references/imagery-and-elements.md](references/imagery-and-elements.md) for photographs,
   patterns and grids, [references/applications.md](references/applications.md) for posters,
   social, stationery and other formats, and [references/web.md](references/web.md) for
   websites and interfaces.
2. **Plan the surfaces before drawing.** List each surface with its ground, its one text colour,
   and its symbol or device. Give Orange and Maroon the leading parts; walk the palette instead
   of alternating two colours.
3. **Check the plan**: `python scripts/brand_check.py pair <ground> <ink>` for each row, or
   `python scripts/brand_check.py matrix` to see them all.
4. **Build from the system's own parts**: `assets/tokens.css`, `assets/logo/`, `assets/patterns/`,
   the recipes in applications.md, the lines in foundation.md.
5. **Check the result** as below, fix, and check again.
6. **Say what was interpreted.** List any decision the PDF does not make.

## Reviewing work

1. Run the checker on anything text-based:
   ```bash
   python scripts/brand_check.py scan <path>
   ```
   It reports off-palette colours, gradients, other typefaces and weights, forced case, text that
   is not left aligned, and unusual leading or tracking, with file and line.
2. Look at the rendered result. The script cannot see these, so check each by eye:
   - every surface's ground, text colour, symbol and logo against the matrix
   - one text colour per surface
   - logo size and clear space: `python scripts/brand_check.py logo --height ...`
   - the logo is whole, upright and undistorted, in motion too
   - Orange and Maroon carry real area; the palette's range is used
   - shapes are soft and rounded like the symbol's; nothing reads as pixels, bits or a technical
     glyph; any pattern is one of the two, with nothing readable on top
   - photographs are real, bright and in colour
   - the words sound like page 5 of the guidelines
3. Report in this form, most serious first:

```markdown
## Brand review: <what was reviewed>

**Verdict:** on brand / needs changes / off brand, in one sentence.

### Breaks the guidelines
| # | Where | What | Guideline | Fix |
| --- | --- | --- | --- | --- |

### Follows the rules but weakens the brand
<creative director, strategist and marketer findings, each with a concrete change>

### Interpretations to confirm
<decisions the PDF does not make>
```

Cite the page for every break. Do not soften a break into a suggestion, and do not present a
preference as a break.

## Where the PDF is silent or disagrees with itself

- **Rule pages outrank mock-ups.** One social post centres its headline and one poster capitalises
  each line; pages 36-37 say sentence case, aligned left. Follow the rule pages.
- **Tone-on-tone grounds.** Page 28 gives the Orange tint, the Mint shade and Grey text that is
  under 3:1, while asking for accessible contrast. The owners' answer: keep the pairing, and
  keep reading text off those grounds.
- **Weights.** Page 33 lists Regular and Medium; page 36 sets Headings in Bold. All three are used.
- **Subheading leading** is printed as "48pt (100%)" for 60pt type. Page 34 says 100%.
- **The light colour.** The PDF's pages draw light elements in Mint; the brand pack's exported
  logo files use Milk White. The owners' answer: Milk White on Maroon, Mint on Orange.
- **Motion, websites and tone of voice** are not covered. web.md, logo.md and foundation.md give
  interpretations, each marked.

When one of these matters to the task, tell the person which reading was used.

## Page index of the PDF

| Pages | Section |
| --- | --- |
| 4-12 | Brand foundation: story, vision, mission, values, goals, services |
| 13-22 | Logo: elements, scaling, minimum size, clear space, partnerships, colour, misuse |
| 23-29 | Colour: primary, values, symbol and type on each ground, misuse |
| 30-37 | Typography: Gabarito, weights, leading, tracking, hierarchy, misuse |
| 38-44 | Photography: three principles, misuse |
| 45-50 | Elements: patterns, layouts, grids |
| 51-61 | Applications: posters, stationery, social, cards, banner, signage |
