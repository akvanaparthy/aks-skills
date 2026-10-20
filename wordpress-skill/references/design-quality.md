# Design quality — avoiding generated-looking themes

A theme can be technically perfect and still look like every other AI-generated page.
This file is the taste layer. Read it before the tokens step and again before calling a
section finished. When a reference image exists, the image wins over everything here;
these rules fill the gaps the image leaves open.

## 1. Start from the subject, not from a template

Before choosing anything, write one line each: what the site is, who reads it, and the
one job the home page must do. The subject's own world supplies the visual vocabulary —
a bakery, a law firm, a kids' app and a hardware startup should not share a palette,
a typeface or a hero layout. If the brief doesn't say, propose a concrete subject and
confirm.

## 2. Two passes: plan, then build

**Pass 1 — a design plan (10 lines, written down in `design/tokens.md`):**

- Colour: 4–6 named values and their roles.
- Type: one family, or two clearly different ones, and their roles.
- Layout: a one-sentence concept + a tiny ASCII wireframe of the hero and one section;
  alignment decision (left / centred / mixed) stated.
- The one memorable element (a type treatment, an image crop, a layout move, an
  interaction). Everything else stays quiet.

Then review the plan: ask "would I have produced this same plan for any other site in
this category?" If yes for any line, change that line and say why. Only then write
`theme.json` and markup.

**Pass 2 — build, screenshot, critique.** After each section, look at the screenshot and
remove one thing (Chanel's rule). Check it against the tells below.

## 3. Current tells of a generated page (don't spend free choices on these)

These are legitimate when the brief asks for them. As defaults they read as machine-made:

- Warm cream background (~`#F4F1EA`) + high-contrast serif display + terracotta/clay accent.
- Near-black background + one acid-green or vermilion accent.
- Broadsheet pastiche: hairline rules, zero radius, dense columns, for a non-editorial subject.
- The SaaS card kit: everything chopped into identical rounded cards, one radius on all
  elements regardless of hierarchy, the same soft grey shadow under each, decorative
  gradient washes/blobs.
- Template chrome regardless of subject: tracked-out ALL-CAPS eyebrow above every
  heading; `A · B · C` meta strings; `WORD — fragment` labels; `#111`-style "black";
  monospace for small data labels; `→` glued to every link/button.
- One italic/coloured word inside every headline.
- Numbered markers (01 / 02 / 03) on content that isn't a sequence.
- Three-column "feature" grids with an icon, a bold label and two lines of copy.
- Fade-and-slide-up on every section and a hover lift on every card.
- Emoji as icons. Stock-photo-shaped placeholders with gradient overlays everywhere.
- Hero = big number + small label + supporting stats + gradient accent.

## 4. Typography carries the personality

- Pick the typeface for *this* subject, not the one you'd reach for anywhere. Prefer
  open-licence families you can self-host; say which you chose and why.
- One family can do everything with weight/size contrast; if two, make them clearly
  different (e.g. a wide grotesk + a narrow serif), never two similar sans.
- Set a real scale (fluid, 6–7 steps) with intentional weights and letter-spacing;
  headlines are a visual element, not just bigger body text.
- Body line length < 80 characters; serif body gets slightly more line-height.
- Sentence case for labels and buttons unless the brief's brand uses caps.

## 5. Structure is information

Borders, dividers, eyebrows, numbering, badges and cards must *encode* something
(grouping, sequence, status, hierarchy). If a device doesn't tell the reader anything,
remove it. Vary section rhythm: not every section needs the same padding, the same
container width, or the same centred heading + paragraph + grid shape. Let one section
break the grid (full-bleed image, asymmetric split, overlapping element) and keep the
rest disciplined.

## 6. Colour

4–6 colours, named by role. Pick one accent and use it for the few things that need
attention (primary action, active state). Backgrounds should mostly be the base; use the
surface colour to group, not to decorate. Check contrast per pair you actually use.
Dark mode / dark style variation is a separate palette, not an inversion.

## 7. Motion

Motion answers an action (open, expand, confirm, filter) and shows what changed. At most
one orchestrated page-load moment, on the hero, if any. No scroll-reveal on every
block. Honour `prefers-reduced-motion`. Transitions 150–250 ms with a real easing curve.

## 8. Copy is design

Placeholder copy makes a design look templated faster than anything. Write real-sounding,
specific copy for the subject ("Fresh sourdough, baked before 6 am" not "Quality
products for your needs"). Sentence case, active voice, buttons that say what happens
("Book a table", not "Submit"). Empty states and errors say what to do next.

## 9. Quality floor (always, without announcing it)

Responsive to 360px, keyboard focus visible, reduced motion, 4.5:1 contrast, no default
WordPress blue links or grey separators leaking through, no layout shift from fonts or
images, real `alt` text.

## 10. Self-critique prompts before "done"

- Could this section be dropped into a different company's site unchanged? If yes, it
  has no point of view yet.
- What is the one memorable thing on this page? If you can't name it, add one; if you
  name three, remove two.
- Which tells from §3 are present, and were they chosen or defaulted?
- Does the mobile screenshot look designed, or like the desktop collapsed?
- Did the screenshot actually get compared to the reference, element by element?
