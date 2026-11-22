#!/usr/bin/env python3
"""Checks work against the Bytenot brand guidelines. Standard library only.

    python brand_check.py scan <path> [<path> ...]   audit code, CSS, HTML and SVG
    python brand_check.py pair <ground> <ink>        is this pairing approved, and how readable is it
    python brand_check.py matrix                     every ground with its approved colours and contrast
    python brand_check.py logo --height H --top T --bottom B --left L --right R
                                                     minimum size and clear space for the logo

Colours are given by name (orange, maroon, mint, milk, orange-tint, maroon-tint,
mint-shade, grey) or as hex. Page numbers refer to the brand guidelines PDF.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

# The palette, exactly as the guidelines give it (pages 25-28).
PALETTE = {
    "orange": "#EB6140",        # Opulent Orange, the signature colour
    "maroon": "#4D1B1E",        # Maroon Oak
    "mint": "#E9FFEF",          # Mint Chiffon
    "milk": "#FCFCFC",          # Milk White
    "orange-tint": "#F8CABE",
    "maroon-tint": "#ECCACC",
    "mint-shade": "#ACC3B2",
    "grey": "#BFBFBF",
}

# For each ground: the symbol colour (page 27), the text colour (page 28) and
# the logo application (page 21). These are the only pairings: the owners have
# ruled that nothing else is put on a ground. `reading` is what may be used for
# text that has to be read; where the given text colour is under 3:1 the ground
# is for ornament and `reading` is empty.
GROUNDS = {
    "milk":        {"symbol": "orange", "display": "orange", "logo": ["orange symbol + maroon wordmark"],
                    "reading": ["maroon"]},
    "maroon":      {"symbol": "orange", "display": "orange", "logo": ["orange symbol + milk wordmark"],
                    "reading": ["milk"]},
    "orange":      {"symbol": "mint",   "display": "mint",   "logo": ["all mint", "all maroon"],
                    "reading": ["mint"]},
    "maroon-tint": {"symbol": "maroon", "display": "maroon", "logo": ["all maroon"],
                    "reading": ["maroon"]},
    "orange-tint": {"symbol": "orange", "display": "orange", "logo": ["all orange"],
                    "reading": []},
    "mint-shade":  {"symbol": "mint",   "display": "mint",   "logo": ["all mint"],
                    "reading": []},
    "grey":        {"symbol": "milk",   "display": "milk",   "logo": ["all milk"],
                    "reading": []},
    "mint":        {"symbol": "orange", "display": "orange", "logo": ["orange symbol + maroon wordmark"],
                    "reading": ["maroon"]},
}

# WCAG 2.2: 4.5:1 for body text, 3:1 for large text (24px regular or 18.66px bold
# and up) and for shapes that carry meaning.
AA_TEXT, AA_LARGE = 4.5, 3.0

# The logo's geometry in the artwork's own units, measured from the vector file.
SYMBOL_W, SYMBOL_H = 180.4, 225.4
LOGO_W = 950.1
MIN_LOGO_HEIGHT_PX = 20  # page 18

TEXT_EXTENSIONS = {".css", ".scss", ".sass", ".less", ".tsx", ".ts", ".jsx", ".js", ".mjs",
                   ".html", ".htm", ".svg", ".vue", ".svelte", ".astro", ".mdx"}
SKIP_DIRS = {"node_modules", ".next", ".git", "dist", "build", "out", "coverage", ".turbo",
             ".vercel", ".agents", ".claude", "Branding"}

APPROVED_WEIGHTS = {"400", "500", "700", "normal", "bold", "inherit", "initial", "unset"}
# Tracking in ems: +30, -20, -10 and 0 thousandths (pages 35-36).
APPROVED_TRACKING = {"0.03em", "-0.02em", "-0.01em", "0", "0em", "normal", "inherit"}
APPROVED_LEADING = {"0.9", "1", "1.3", "normal", "inherit"}
GENERIC_FAMILIES = {"sans-serif", "serif", "monospace", "system-ui", "ui-sans-serif", "ui-serif",
                    "ui-monospace", "inherit", "initial", "unset", "arial", "helvetica",
                    "helvetica neue", "segoe ui", "roboto", "liberation sans", "arimo"}


def to_rgb(value: str) -> tuple[int, int, int]:
    value = PALETTE.get(value.lower(), value).lstrip("#")
    if len(value) == 3:
        value = "".join(ch * 2 for ch in value)
    if len(value) not in (6, 8) or not re.fullmatch(r"[0-9a-fA-F]+", value):
        raise ValueError(f"not a palette name or hex colour: {value!r}")
    return tuple(int(value[i:i + 2], 16) for i in (0, 2, 4))


def luminance(rgb: tuple[int, int, int]) -> float:
    channels = []
    for v in rgb:
        c = v / 255
        channels.append(c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * channels[0] + 0.7152 * channels[1] + 0.0722 * channels[2]


def contrast(a: str, b: str) -> float:
    x, y = luminance(to_rgb(a)), luminance(to_rgb(b))
    return (max(x, y) + 0.05) / (min(x, y) + 0.05)


def palette_name(value: str) -> str | None:
    try:
        rgb = to_rgb(value)
    except ValueError:
        return None
    for name, hex_value in PALETTE.items():
        if to_rgb(hex_value) == rgb:
            return name
    return None


def grade(ratio: float) -> str:
    if ratio >= AA_TEXT:
        return "readable at any size"
    if ratio >= AA_LARGE:
        return "large type and shapes only"
    return "decoration only, too faint to be read"


# ------------------------------------------------------------------ matrix ----

def cmd_matrix(_args) -> int:
    print(f"{'Ground':<13}{'Symbol':<9}{'Text (page 28)':<23}{'For reading':<22}Logo")
    for ground, rule in GROUNDS.items():
        display = f"{rule['display']} {contrast(ground, rule['display']):.2f}:1"
        reading = ", ".join(f"{ink} {contrast(ground, ink):.2f}:1" for ink in rule["reading"]) or "ornament only"
        print(f"{ground:<13}{rule['symbol']:<9}{display:<23}{reading:<22}{'; '.join(rule['logo'])}")
    print("\nThese are the only pairings. If one cannot do the job, change the ground.")
    print("Mint is not used as a ground on the website; light grounds are Milk White.")
    return 0


# -------------------------------------------------------------------- pair ----

def cmd_pair(args) -> int:
    ground = palette_name(args.ground)
    ink = palette_name(args.ink)
    if ground is None:
        print(f"{args.ground} is not in the palette. On a colour outside it the logo is black or white"
              " (page 29), and nothing else of the brand belongs there.")
        return 1
    if ink is None:
        print(f"{args.ink} is not in the palette (page 29: do not use unapproved colours).")
        return 1
    rule = GROUNDS[ground]
    ratio = contrast(ground, ink)
    roles = [role for role in ("symbol", "display") if rule[role] == ink]
    if ink in rule["reading"]:
        roles.append("reading text")
    print(f"{ink} on {ground}: {ratio:.2f}:1, {grade(ratio)}")
    if roles:
        print(f"Given by the guidelines as: {', '.join(roles)}")
        return 0
    reading = " or ".join(rule["reading"]) or "nothing (this ground is for ornament)"
    print(f"Not a given pairing. On {ground} the guidelines put {rule['display']} text and a"
          f" {rule['symbol']} symbol; for reading text use {reading}. Do not invent a pairing:"
          " change the ground instead.")
    return 1


# -------------------------------------------------------------------- logo ----

def cmd_logo(args) -> int:
    height = args.height
    symbol_w = height * SYMBOL_W / SYMBOL_H
    problems = []
    if height < MIN_LOGO_HEIGHT_PX:
        problems.append(f"height {height:g}px is under the {MIN_LOGO_HEIGHT_PX}px minimum (page 18)")
    for side, gap, need in (("top", args.top, height), ("bottom", args.bottom, height),
                            ("left", args.left, symbol_w), ("right", args.right, symbol_w)):
        if gap is not None and gap < need:
            problems.append(f"{side}: {gap:g}px clear, needs {need:.0f}px")
    print(f"A logo {height:g}px tall is {height * LOGO_W / SYMBOL_H:.0f}px wide."
          f" Clear space (page 19): {height:.0f}px above and below, {symbol_w:.0f}px left and right.")
    if args.top is not None and args.bottom is not None:
        room = args.top + height + args.bottom
        print(f"In that {room:.0f}px of height the logo may be at most {room / 3:.0f}px tall.")
    if problems:
        print("Does not comply:\n  " + "\n  ".join(problems))
        return 1
    print("Complies.")
    return 0


# -------------------------------------------------------------------- scan ----

HEX = re.compile(r"(?<![\w&])#([0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3})(?![0-9a-zA-Z_-])")
COLOUR_FUNCTION = re.compile(r"\b(rgba?|hsla?|oklch|oklab|lab|lch)\(\s*[\d.]")
SHADE = re.compile(r"color-mix\(|(?<![\w-])opacity\s*:\s*0?\.\d")
GRADIENT = re.compile(r"\b(repeating-)?(linear|radial|conic)-gradient\(|<(linear|radial)Gradient\b")
FONT_FAMILY = re.compile(r"font-family\s*:\s*([^;}{]+)")
FONT_WEIGHT = re.compile(r"font-weight\s*:\s*([^;}{\s]+)")
TEXT_TRANSFORM = re.compile(r"text-transform\s*:\s*(uppercase|lowercase|capitalize)")
TEXT_ALIGN = re.compile(r"text-align\s*:\s*(center|right|justify|end)")
LETTER_SPACING = re.compile(r"letter-spacing\s*:\s*([^;}{\s]+)")
LINE_HEIGHT = re.compile(r"line-height\s*:\s*([^;}{\s]+)")
# Utility classes, looked for only inside a class or className attribute.
UTILITY = re.compile(r"(?<![\w-])(uppercase|lowercase|capitalize|text-center|text-right|text-justify|"
                     r"font-thin|font-extralight|font-light|font-semibold|font-extrabold|font-black|"
                     r"italic|font-mono|font-serif)(?![\w-])")
CLASS_ATTRIBUTE = re.compile(r"class(?:Name)?\s*=\s*(?:\{[^}]*\}|\"[^\"]*\"|'[^']*')")
GOOGLE_FONT = re.compile(r"import\s*\{([^}]+)\}\s*from\s*['\"]next/font/google['\"]")

RULES = {
    "colour": "Colour outside the palette (page 29). Use one of the eight, at full strength.",
    "shade": "A colour faded or mixed into a shade. Only the eight colours at full strength are allowed"
             " for text, lines and fills; confirm each of these is a depth effect (shadow, frosted bar).",
    "gradient": "Gradient (page 29: do not use gradients).",
    "typeface": "Typeface other than Gabarito (pages 32 and 37).",
    "weight": "Weight other than Regular 400, Medium 500 or Bold 700 (pages 33 and 36).",
    "case": "Forced case or italics (page 37: sentence case, never all caps or all lowercase).",
    "alignment": "Text not aligned left (page 37: always align to the left).",
    "tracking": "Tracking other than +30, -20, -10 or 0 (pages 35-36).",
    "leading": "Leading other than 90%, 100% or 130% (pages 34 and 36).",
}
# Tracking and leading vary for good reason in interface controls, so they are
# reported for a person to judge rather than counted as breaks.
REVIEW_ONLY = {"tracking", "leading", "shade"}


def utility_rule(name: str) -> str:
    if name.startswith("text-"):
        return "alignment"
    if name in ("font-mono", "font-serif"):
        return "typeface"
    if name.startswith("font-"):
        return "weight"
    return "case"


def scan_file(path: str, findings: list[dict]) -> None:
    try:
        with open(path, encoding="utf-8") as handle:
            lines = handle.read().splitlines()
    except (UnicodeDecodeError, OSError):
        return  # binary or unreadable: nothing to say about it

    def add(rule: str, number: int, detail: str) -> None:
        findings.append({"rule": rule, "file": path.replace(os.sep, "/"), "line": number, "detail": detail})

    for number, line in enumerate(lines, 1):
        if "brand-check-ignore" in line:
            continue
        for match in HEX.finditer(line):
            if palette_name(match.group(0)) is None:
                add("colour", number, match.group(0))
        function = COLOUR_FUNCTION.search(line)
        if function:
            add("colour", number, function.group(0) + "...)")
        if GRADIENT.search(line):
            add("gradient", number, line.strip()[:90])
        if SHADE.search(line):
            add("shade", number, line.strip()[:90])
        for match in FONT_FAMILY.finditer(line):
            families = [f.strip().strip("'\"").lower() for f in match.group(1).split(",")]
            odd = [f for f in families if f and not f.startswith("var(") and "gabarito" not in f
                   and f not in GENERIC_FAMILIES]
            if odd:
                add("typeface", number, ", ".join(odd))
        for match in GOOGLE_FONT.finditer(line):
            odd = [n.strip() for n in match.group(1).split(",") if n.strip() and n.strip() != "Gabarito"]
            if odd:
                add("typeface", number, ", ".join(odd))
        for match in FONT_WEIGHT.finditer(line):
            value = match.group(1).strip()
            if value not in APPROVED_WEIGHTS and not value.startswith("var("):
                add("weight", number, value)
        for match in TEXT_TRANSFORM.finditer(line):
            add("case", number, match.group(0))
        for match in TEXT_ALIGN.finditer(line):
            add("alignment", number, match.group(0))
        for match in LETTER_SPACING.finditer(line):
            value = match.group(1).strip()
            if value not in APPROVED_TRACKING and not value.startswith("var("):
                add("tracking", number, value)
        for match in LINE_HEIGHT.finditer(line):
            value = match.group(1).strip()
            if value not in APPROVED_LEADING and not value.startswith(("var(", "calc(")):
                add("leading", number, value)
        for attribute in CLASS_ATTRIBUTE.finditer(line):
            for match in UTILITY.finditer(attribute.group(0)):
                add(utility_rule(match.group(1)), number, match.group(1))


def cmd_scan(args) -> int:
    findings: list[dict] = []
    scanned = 0
    for root in args.paths:
        if os.path.isfile(root):
            scan_file(root, findings)
            scanned += 1
            continue
        if not os.path.isdir(root):
            print(f"No such path: {root}", file=sys.stderr)
            return 2
        for folder, dirs, files in os.walk(root):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            for name in files:
                if os.path.splitext(name)[1].lower() not in TEXT_EXTENSIONS:
                    continue
                if not args.include_tests and re.search(r"\.(test|spec)\.", name):
                    continue
                scan_file(os.path.join(folder, name), findings)
                scanned += 1

    hard = [f for f in findings if f["rule"] not in REVIEW_ONLY]
    if args.json:
        print(json.dumps(findings, indent=1))
        return 1 if hard else 0

    for rule, explanation in RULES.items():
        group = [f for f in findings if f["rule"] == rule]
        if not group:
            continue
        label = "REVIEW" if rule in REVIEW_ONLY else "BREAKS"
        print(f"\n{label}: {explanation}  [{len(group)}]")
        for f in group[: args.limit]:
            print(f"  {f['file']}:{f['line']}  {f['detail']}")
        if len(group) > args.limit:
            print(f"  ... and {len(group) - args.limit} more (raise --limit to see them)")
    print(f"\n{scanned} files scanned: {len(hard)} breaks, {len(findings) - len(hard)} to review.")
    print("This finds only what text can show. Logo clear space, pairings on the rendered page, one text"
          " colour per surface, photography and tone still need eyes: see SKILL.md, 'Reviewing work'.")
    return 1 if hard else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(dest="command", required=True)

    scan = commands.add_parser("scan", help="audit files for brand breaks")
    scan.add_argument("paths", nargs="+")
    scan.add_argument("--json", action="store_true", help="machine-readable findings")
    scan.add_argument("--limit", type=int, default=25, help="findings shown per rule (default 25)")
    scan.add_argument("--include-tests", action="store_true", help="also scan *.test.* and *.spec.* files")
    scan.set_defaults(run=cmd_scan)

    pair = commands.add_parser("pair", help="check one ground and ink pairing")
    pair.add_argument("ground")
    pair.add_argument("ink")
    pair.set_defaults(run=cmd_pair)

    matrix = commands.add_parser("matrix", help="print every approved pairing with its contrast")
    matrix.set_defaults(run=cmd_matrix)

    logo = commands.add_parser("logo", help="check the logo's size and clear space, in pixels")
    logo.add_argument("--height", type=float, required=True, help="rendered height of the logo")
    for side in ("top", "bottom", "left", "right"):
        logo.add_argument(f"--{side}", type=float,
                          help=f"distance to the nearest element or edge on the {side}")
    logo.set_defaults(run=cmd_logo)

    args = parser.parse_args()
    try:
        return args.run(args)
    except ValueError as error:
        print(error, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
