# Colour

Source: guidelines pages 23-29, plus what the application pages (47-61) show in use.

## Contents
- The palette
- How much of each
- The eight grounds and what goes on them
- Reading the matrix
- Rules that are never bent
- No shades
- Composing with the whole palette

## The palette

"Colour gives our identity its energy." (p24)

| Name | Hex | RGB | CMYK | Pantone |
| --- | --- | --- | --- | --- |
| Opulent Orange | `#EB6140` | 235, 97, 64 | 0, 59, 73, 8 | 2060 C |
| Maroon Oak | `#4D1B1E` | 77, 27, 30 | 0, 65, 61, 70 | 4102 C |
| Mint Chiffon | `#E9FFEF` | 233, 255, 239 | 9, 0, 6, 0 | 621 C |
| Milk White | `#FCFCFC` | 252, 252, 252 | 0, 0, 0, 1 | 663 C |
| Grey | `#BFBFBF` | 191, 191, 191 | | |
| Orange tint | `#F8CABE` | 248, 202, 190 | | |
| Maroon tint | `#ECCACC` | 236, 202, 204 | | |
| Mint shade | `#ACC3B2` | 172, 195, 178 | | |

The first five are the core palette (p25). The tints and the shade appear as grounds on pages 27
and 28. The PDF names only the first four; "Grey", "Orange tint", "Maroon tint" and "Mint shade"
are this skill's labels for the other four.

Opulent Orange is "our brand's signature colour, defining Bytenot's identity and helping
distinguish it from others" (p25).

## How much of each

Page 25 draws the core palette as blocks: Orange and Maroon take a quarter each, and Mint, Milk
White and Grey share the other half. Read that as intent: **Orange and Maroon lead together**,
Mint and Milk White give them room, Grey stays in the background.

The application pages bear this out. Posters, cards, banners and posts are built from large flat
fields of Orange and Maroon, with Mint as the third voice. A layout that is nearly all Mint with
Orange reduced to dots and hairlines is on-palette and still off-brand: it leaves out the colour
that the guidelines call the signature.

The tints and the shade are for range, "allowing us to express our brand personality and values
more fully" (p26): use them to give a long piece more than three rooms to walk through.

## The eight grounds and what goes on them

Pages 21, 27 and 28 fix what sits on each ground. "They were designed to work together, so they
should be used as intended." (p28)

| Ground | Symbol (p27) | Logo (p21) | Text (p28) | Contrast of that text |
| --- | --- | --- | --- | --- |
| Milk White `#FCFCFC` | Orange | Orange symbol + Maroon wordmark | Maroon for reading, Orange for display | 13.73:1, 3.24:1 |
| Maroon `#4D1B1E` | Orange | Orange symbol + Milk White wordmark | Milk White | 13.73:1 |
| Orange `#EB6140` | Mint | all Mint, or all Maroon | Mint | 3.17:1 |
| Maroon tint `#ECCACC` | Maroon | all Maroon | Maroon | 9.31:1 |
| Orange tint `#F8CABE` | Orange | all Orange | Orange | 2.25:1 |
| Mint shade `#ACC3B2` | Mint | all Mint | Mint | 1.79:1 |
| Grey `#BFBFBF` | Milk White | all Milk White | Milk White | 1.79:1 |
| Mint `#E9FFEF` (not used as a ground) | Orange | Orange symbol + Maroon wordmark | Orange | 3.17:1 |
| Anything else, photos | black or white | black or white (p29) | none | |

These are the only pairings. The owners have ruled that nothing else is to be put on a ground:
if a pairing cannot do the job, change the ground, not the colours on it. Two readings are
theirs: on Milk White, Maroon carries the reading (as the guidelines' own pages and the
wordmark do) and Orange the display; on Maroon the light colour is Milk White, not Mint.

Print this table with live contrast figures: `python scripts/brand_check.py matrix`.
Check one pairing: `python scripts/brand_check.py pair <ground> <ink>`.

## Reading the matrix

Contrast decides what a pairing can be used for, because page 28 also says "strong colour
contrast is essential for legibility and accessibility":

- 4.5:1 and up: any text. Milk White, Maroon and the Maroon tint are the grounds for sections
  that are read.
- 3:1 to 4.5:1: large type only (24px regular, or about 19px bold, and up). Orange is such a
  ground: a few large words in Mint, and anything to be read or filled in goes in a white block
  set into it, the way the posters set words into a block within a field.
- under 3:1: ornament. The Orange tint, the Mint shade and Grey are grounds for a symbol, a
  pattern or a block of colour, never for a section of text.

## Rules that are never bent

Page 29, "Do not diminish the value of colour in the brand":

1. No unapproved colours. Nothing outside the eight.
2. No gradients.
3. No low-contrast combinations (its example: Mint shade type on Orange).
4. No logo on a colour outside the palette; there, the logo is black or white.
5. No more than one text colour at once (its example: one sentence, half Orange, half Mint shade,
   on Maroon).
6. No changes to the logo's colour applications.

On rule 5: within one surface, pick one text colour and keep it. The Orange poster carries a
Maroon block whose words are all Orange; the Maroon poster's words are all Mint. A second colour
may arrive in the symbol, a pattern or a block, never in more type. Where a display headline in
Orange sits over Maroon reading text on Mint, that is two text colours on one surface: choose one.

## No shades

Only the eight colours, each at full strength. The owners have ruled out every shade made by
opacity, mixing or tinting, for text, lines, borders and fills, unless they ask for one.

- Secondary text is the ground's text colour, the same as primary text. Make the hierarchy with
  size and weight.
- Hairlines and borders are 1px of the text colour, as the guidelines' own ruled lines are.
- Hover, pressed and disabled states change shape, position or an underline, not strength.
- Never write `opacity`, `color-mix(... transparent)` or an alpha value on a colour that is
  read as text, line or fill. Depth effects (shadows, the frosted bar) are the one exception
  the owners have allowed to stay.

## Composing with the whole palette

What the application pages do, as moves you can reuse:

- **Flood a field.** A whole poster, card or post in Orange or in Maroon, type in one colour.
- **Block against block.** A Maroon square set into an Orange field, or the reverse, with the
  words inside the inner block (posters p49, cards p56).
- **Edge with pattern.** A strip or corner of the checker pattern closing a Maroon or Mint field
  (p48, banner p57).
- **Seat the symbol in a square.** An Orange square holding a Maroon symbol, or a Mint square
  holding a Maroon symbol, as a corner mark (p49, letterhead p54).
- **Let white breathe.** Milk White carries long reading and gives the two leads room.
- **Walk the palette.** Across a long piece, change ground from part to part so that Orange,
  Maroon, Mint, Milk White and a tint each get a turn, rather than alternating two.

Before settling a scheme, list each surface with its ground, its one text colour and its symbol
colour, and check every row against the matrix.
