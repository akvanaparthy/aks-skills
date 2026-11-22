# Typography

Source: guidelines pages 30-37.

## The typeface

**Gabarito**, and only Gabarito. "A light-hearted, geometric sans-serif" by Naipe Foundry
(Leandro Assis, Alvaro Franca, Felipe Casaprima), free on Google Fonts under the Open Font
License. Page 32 introduces it for headlines; page 36 sets body copy in it too, so it carries
everything.

Weights: Regular 400, Medium 500, Bold 700. "Use only the approved weights." (p33) Page 33 shows
Regular and Medium; Bold is the Heading weight on page 36. No light, semibold, extrabold or black,
and no italics.

## The three styles

Page 36. Every piece of text is one of these.

| Style | Weight | Case | Size (print) | Leading | Tracking |
| --- | --- | --- | --- | --- | --- |
| Heading | Bold | Sentence case | 144pt | 90% of the size | +30 |
| Subheading | Medium | Sentence case | 60pt | 100% of the size | -20 |
| Body | Regular | Sentence case | 18pt | 130% of the size | -10 |

- **Leading** is baseline to baseline: multiply the size by 0.9, 1.0 or 1.3 (p34).
- **Tracking** is in thousandths of an em: +30 is `0.03em`, -20 is `-0.02em`, -10 is `-0.01em`.
  "Smaller text should stay between 0 to -10." (p35)
- **Sentence case** always: capital first letter, the rest lower, proper nouns kept.
- **Align left** always (p37).
- "Make sure there is a clear and intentional difference between type sizes." (p36) The print
  sizes step 8 : 3.3 : 1. Keep steps that decisive; do not invent in-between sizes.

Page 36 prints the Subheading leading as "48pt (100%)" for 60pt type. The two disagree; page 34
states the rule as 100%, so 100% is what to use. Mention the discrepancy if it matters.

## Misuse

Page 37:

1. Do not set in all caps.
2. Do not set in all lowercase.
3. Do not use unapproved typefaces.
4. Do not use incorrect leading values.
5. Do not use incorrect tracking values.
6. Do not align text incorrectly. Always align to the left.

Colour of type is governed by the ground: see [colour.md](colour.md). One text colour per surface.

## On the web

```css
font-family: 'Gabarito', 'Gabarito Fallback', ui-sans-serif, system-ui, sans-serif;

/* Heading */    font-weight: 700; line-height: 0.9; letter-spacing: 0.03em;
/* Subheading */ font-weight: 500; line-height: 1;   letter-spacing: -0.02em;
/* Body */       font-weight: 400; font-size: 1.125rem; line-height: 1.3; letter-spacing: -0.01em;
```

Interpretations for screens, where the PDF gives print sizes only:

- Body is 18px (`1.125rem`). Smaller supporting text keeps Body's leading and tracking of 0 to
  -10; do not go below 14px.
- Heading and Subheading scale with the viewport (`clamp()`), holding their leading and tracking.
  Keep each at least a third larger than the style below it at every width.
- Small labels are Body at a smaller size, or Subheading weight: never capitals, never a
  monospace or second family.
- Interface controls (buttons, inputs, navigation) are Body or Subheading. A line of text in a
  control may take whatever height the control needs; that is the box, not the leading.
- A 90% leading clips nothing on one line, but on two it brings descenders close to ascenders:
  that is the intended look for Headings. Do not loosen it to "fix" it.
- Line length for reading text: about 45 to 75 characters.
- Load Regular, Medium and Bold only. Give the fallback face Gabarito's metrics so the page does
  not shift when the font arrives.
