# soilmass Brand Guidelines Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the soilmass brand guidelines: eight canonical markdown files, five generated SVG logo assets, and a self-demonstrating `index.html` brand book.

**Architecture:** Static content, no build system. Python (`fonttools`) generates the logo SVGs from the Archivo variable font so they render as pure outlines with no font dependency. A small contrast-checker script enforces the spec's WCAG claims as an executable test. `index.html` is a single hand-written page using CSS custom properties for the tokens.

**Tech Stack:** Markdown, HTML/CSS (no JS needed), Python 3 + fonttools (tooling only), Google Fonts (Archivo, JetBrains Mono).

**Spec:** `docs/superpowers/specs/2026-07-13-soilmass-brand-guidelines-design.md` — read it before starting. All values below come from it verbatim.

## Global Constraints

- Colors — neutrals: paper `#FAF9F6`, stone-100 `#F0EEE8`, stone-200 `#E8E5DE`, stone-300 `#D8D4CC`, stone-400 `#A8A29A`, stone-500 `#78736A`, stone-600 `#59544B`, ink `#191714`; ochre-100 `#F7EBD3`, ochre-500 `#C98A12`, ochre-600 `#8F620B`. No other hues, no `#FFFFFF`, no `#000000`.
- Ochre **text** on paper always uses ochre-600 (any size). Ochre-500 type only on ink/dark. Text on ochre-500 fills is always ink. Paper text allowed on ochre-600 fills. stone-500 text at large sizes only.
- Fonts: Archivo 400/600/900 and JetBrains Mono 400/600 via Google Fonts (only external dependency of index.html).
- Type scale (desktop px, size/leading): Display 64/68 Archivo 900 −0.03em · H1 40/44 Archivo 900 −0.02em · H2 28/34 Archivo 600 · H3 20/28 Archivo 600 · Body 16/26 Archivo 400, max 70ch · Small 14/22 stone-600 · Label 12/16 JetBrains Mono 400 UPPERCASE +0.12em.
- Spacing steps: 4, 8, 16, 24, 32, 48, 64, 96, 128. Grid: 12 col / 1200px max / 24px gutters.
- **Square corners everywhere — `border-radius` must not appear in any file.**
- Logo geometry: ink (paper on dark) to 71% of wordmark height, background gap 71–74%, ochre `#C98A12` 74%–baseline; measured on the full bounding box, ascender included. Wordmark: lowercase `soilmass`, Archivo 900, tracking −0.03em. Favicon tile gap optically enlarged (~7% of glyph height).
- Tagline, exact copy: `Solid ground for the web.`
- Voice: warm & consultative (principles in spec §8).
- Git: commit after every task; messages end with `Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>`.

## File Structure

```
tools/
  check_contrast.py      # executable WCAG test for all documented color pairs
  build_logos.py         # generates assets/*.svg from the Archivo variable font
  fonts/                 # downloaded font binaries (gitignored)
  .venv/                 # python venv with fonttools (gitignored)
assets/
  logo-light.svg  logo-dark.svg  logo-mono.svg  wordmark-small.svg  favicon.svg
guidelines/
  00-overview.md  01-logo.md  02-color.md  03-typography.md
  04-layout-and-devices.md  05-imagery-and-iconography.md
  06-voice-and-tone.md  07-applications.md
index.html               # the styled brand book
```

---

### Task 1: Contrast checker + tooling setup

**Files:**
- Create: `tools/check_contrast.py`
- Modify: `.gitignore`

**Interfaces:**
- Produces: `python3 tools/check_contrast.py` → prints one `PASS <ratio> <description>` line per pair, exits 0 when all pass, 1 otherwise. Tasks 4 and 9 run it as their test.

- [ ] **Step 1: Extend .gitignore**

Append to `.gitignore` so it reads:

```
.superpowers/
tools/fonts/
tools/.venv/
```

- [ ] **Step 2: Write the failing test invocation**

Run: `python3 tools/check_contrast.py`
Expected: FAIL — `python3: can't open file ... No such file or directory`

- [ ] **Step 3: Write tools/check_contrast.py**

```python
#!/usr/bin/env python3
"""Executable WCAG AA test for every color pair the soilmass spec documents.

Spec: docs/superpowers/specs/2026-07-13-soilmass-brand-guidelines-design.md section 4.
Exit 0 = all pairs meet their required ratio; exit 1 otherwise.
"""
import sys

TOKENS = {
    "paper": "FAF9F6", "stone-100": "F0EEE8", "stone-200": "E8E5DE",
    "stone-300": "D8D4CC", "stone-400": "A8A29A", "stone-500": "78736A",
    "stone-600": "59544B", "ink": "191714",
    "ochre-100": "F7EBD3", "ochre-500": "C98A12", "ochre-600": "8F620B",
}

# (foreground, background, required ratio, rule being enforced)
PAIRS = [
    ("ink", "paper", 4.5, "body text on paper"),
    ("stone-600", "paper", 4.5, "secondary text on paper"),
    ("ochre-600", "paper", 4.5, "ochre text/links on paper, any size"),
    ("stone-500", "paper", 3.0, "stone-500 restricted to large text"),
    ("paper", "ink", 4.5, "text on dark sections"),
    ("stone-400", "ink", 4.5, "faint text on dark"),
    ("ochre-500", "ink", 4.5, "ochre type on dark"),
    ("ink", "ochre-500", 4.5, "button: ink text on ochre-500 fill"),
    ("paper", "ochre-600", 4.5, "paper text on ochre-600 fill"),
    ("ochre-600", "ochre-100", 4.5, "ochre text on tint background"),
    ("ink", "ochre-100", 4.5, "ink text on tint background"),
    ("stone-600", "stone-100", 4.5, "secondary text on panel"),
]


def channel(c: int) -> float:
    c /= 255
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def luminance(hexval: str) -> float:
    r, g, b = (int(hexval[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * channel(r) + 0.7152 * channel(g) + 0.0722 * channel(b)


def ratio(fg: str, bg: str) -> float:
    lf, lb = luminance(TOKENS[fg]), luminance(TOKENS[bg])
    hi, lo = max(lf, lb), min(lf, lb)
    return (hi + 0.05) / (lo + 0.05)


def main() -> int:
    failed = False
    for fg, bg, need, rule in PAIRS:
        r = ratio(fg, bg)
        ok = r >= need
        failed |= not ok
        print(f"{'PASS' if ok else 'FAIL'} {r:5.2f}:1 (need {need}) {fg} on {bg} — {rule}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run the test, verify it passes**

Run: `python3 tools/check_contrast.py; echo "exit=$?"`
Expected: 12 `PASS` lines, no `FAIL`, `exit=0`.

- [ ] **Step 5: Commit**

```bash
git add .gitignore tools/check_contrast.py
git commit -m "feat: add executable WCAG contrast test for brand color pairs

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
```

---

### Task 2: Logo SVG generation

**Files:**
- Create: `tools/build_logos.py`
- Create (generated): `assets/logo-light.svg`, `assets/logo-dark.svg`, `assets/logo-mono.svg`, `assets/wordmark-small.svg`, `assets/favicon.svg`

**Interfaces:**
- Consumes: nothing from other tasks.
- Produces: the five SVG files above, referenced by `index.html` (Tasks 6–9) via relative `assets/...` paths. All SVGs are pure `<path>` outlines (no `<text>`), each with a `viewBox`, scaling to any size.

- [ ] **Step 1: Set up venv and download the font**

```bash
python3 -m venv tools/.venv
tools/.venv/bin/pip -q install fonttools
mkdir -p tools/fonts assets
curl -fsSL -o "tools/fonts/Archivo[wdth,wght].ttf" \
  "https://github.com/google/fonts/raw/main/ofl/archivo/Archivo%5Bwdth%2Cwght%5D.ttf"
ls -l tools/fonts/
```

Expected: the TTF file present, size roughly 200–500 KB. If the URL 404s (Google occasionally reshuffles), find the current filename at https://github.com/google/fonts/tree/main/ofl/archivo and adjust — it must be the *variable* Archivo font with `wght` axis.

- [ ] **Step 2: Write the failing test invocation**

Run: `tools/.venv/bin/python tools/build_logos.py`
Expected: FAIL — file not found.

- [ ] **Step 3: Write tools/build_logos.py**

```python
#!/usr/bin/env python3
"""Generate the soilmass logo SVGs from the Archivo variable font.

Outputs pure-outline SVGs (no <text>) so they render identically everywhere.
Spec: docs/superpowers/specs/2026-07-13-soilmass-brand-guidelines-design.md section 3.
"""
from pathlib import Path

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

ROOT = Path(__file__).resolve().parent.parent
FONT = ROOT / "tools" / "fonts" / "Archivo[wdth,wght].ttf"
OUT = ROOT / "assets"

INK, PAPER, OCHRE = "#191714", "#FAF9F6", "#C98A12"
TRACKING_EM = -0.03   # spec: letter-spacing -0.03em
CUT_TOP = 0.71        # grade line starts at 71% of wordmark height
CUT_BOTTOM = 0.74     # ochre band starts at 74%
FAV_CUT_TOP = 0.685   # favicon gap optically enlarged to ~7%
FAV_CUT_BOTTOM = 0.755


def load_font() -> TTFont:
    font = TTFont(FONT)
    instantiateVariableFont(font, {"wght": 900, "wdth": 100}, inplace=True)
    return font


def layout(font, text):
    """Place glyphs with tracking. Returns ([(path_d, x_offset)], bbox) in
    font units, y-up. bbox = (xmin, ymin, xmax, ymax) of inked outlines."""
    upm = font["head"].unitsPerEm
    cmap = font.getBestCmap()
    glyphs = font.getGlyphSet()
    track = TRACKING_EM * upm
    x = 0.0
    placed = []
    xmin = ymin = xmax = ymax = None
    for ch in text:
        name = cmap[ord(ch)]
        spen = SVGPathPen(glyphs)
        glyphs[name].draw(spen)
        bpen = BoundsPen(glyphs)
        glyphs[name].draw(bpen)
        if bpen.bounds:
            bx0, by0, bx1, by1 = bpen.bounds
            xmin = bx0 + x if xmin is None else min(xmin, bx0 + x)
            xmax = bx1 + x if xmax is None else max(xmax, bx1 + x)
            ymin = by0 if ymin is None else min(ymin, by0)
            ymax = by1 if ymax is None else max(ymax, by1)
        placed.append((spen.getCommands(), x))
        x += glyphs[name].width + track
    return placed, (xmin, ymin, xmax, ymax)


def glyph_group(placed, fill):
    parts = [f'<path transform="translate({x:.1f} 0)" d="{d}"/>'
             for d, x in placed if d]
    return f'<g fill="{fill}">' + "".join(parts) + "</g>"


def flip(bbox):
    """SVG transform mapping font units (y-up) into a y-down viewBox at 0,0."""
    x0, y0, x1, y1 = bbox
    return f"matrix(1 0 0 -1 {-x0:.1f} {y1:.1f})"


def two_tone_svg(placed, bbox, top_fill, bottom_fill, prefix):
    x0, y0, x1, y1 = bbox
    w, h = x1 - x0, y1 - y0
    xf = flip(bbox)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}">'
        f'<defs>'
        f'<clipPath id="{prefix}-above"><rect x="0" y="0" width="{w:.0f}" height="{h * CUT_TOP:.1f}"/></clipPath>'
        f'<clipPath id="{prefix}-below"><rect x="0" y="{h * CUT_BOTTOM:.1f}" width="{w:.0f}" height="{h * (1 - CUT_BOTTOM):.1f}"/></clipPath>'
        f'</defs>'
        f'<g clip-path="url(#{prefix}-above)"><g transform="{xf}">{glyph_group(placed, top_fill)}</g></g>'
        f'<g clip-path="url(#{prefix}-below)"><g transform="{xf}">{glyph_group(placed, bottom_fill)}</g></g>'
        f'</svg>\n'
    )


def small_svg(placed, bbox):
    """Solid ink wordmark with ochre full stop — small-size fallback."""
    x0, y0, x1, y1 = bbox
    w, h = x1 - x0, y1 - y0
    xf = flip(bbox)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}">'
        f'<g transform="{xf}">'
        f'{glyph_group(placed[:-1], INK)}{glyph_group(placed[-1:], OCHRE)}'
        f'</g></svg>\n'
    )


def favicon_svg(font):
    placed, (x0, y0, x1, y1) = layout(font, "s")
    w, h = x1 - x0, y1 - y0
    size, target_h = 64, 38.0
    s = target_h / h
    ox = (size - w * s) / 2
    oy = (size - target_h) / 2
    xf = f"matrix({s:.4f} 0 0 {-s:.4f} {ox - x0 * s:.2f} {oy + y1 * s:.2f})"
    top = oy + target_h * FAV_CUT_TOP
    bot = oy + target_h * FAV_CUT_BOTTOM
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}">'
        f'<rect width="{size}" height="{size}" fill="{INK}"/>'
        f'<defs>'
        f'<clipPath id="fav-above"><rect x="0" y="0" width="{size}" height="{top:.1f}"/></clipPath>'
        f'<clipPath id="fav-below"><rect x="0" y="{bot:.1f}" width="{size}" height="{size - bot:.1f}"/></clipPath>'
        f'</defs>'
        f'<g clip-path="url(#fav-above)"><g transform="{xf}">{glyph_group(placed, PAPER)}</g></g>'
        f'<g clip-path="url(#fav-below)"><g transform="{xf}">{glyph_group(placed, OCHRE)}</g></g>'
        f'</svg>\n'
    )


def main():
    OUT.mkdir(exist_ok=True)
    font = load_font()
    placed, bbox = layout(font, "soilmass")
    (OUT / "logo-light.svg").write_text(two_tone_svg(placed, bbox, INK, OCHRE, "ll"))
    (OUT / "logo-dark.svg").write_text(two_tone_svg(placed, bbox, PAPER, OCHRE, "ld"))
    (OUT / "logo-mono.svg").write_text(two_tone_svg(placed, bbox, INK, INK, "lm"))
    placed_dot, bbox_dot = layout(font, "soilmass.")
    (OUT / "wordmark-small.svg").write_text(small_svg(placed_dot, bbox_dot))
    (OUT / "favicon.svg").write_text(favicon_svg(font))
    print(f"wrote 5 SVGs to {OUT}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run the generator**

Run: `tools/.venv/bin/python tools/build_logos.py`
Expected: `wrote 5 SVGs to .../assets`

- [ ] **Step 5: Verify the SVGs structurally**

```bash
python3 - <<'EOF'
import xml.etree.ElementTree as ET
from pathlib import Path
names = ["logo-light.svg", "logo-dark.svg", "logo-mono.svg",
         "wordmark-small.svg", "favicon.svg"]
for n in names:
    p = Path("assets") / n
    text = p.read_text()
    ET.fromstring(text)                      # well-formed XML
    assert "<path" in text, f"{n}: no outlines"
    assert "<text" not in text, f"{n}: contains <text> — font dependency!"
    assert "viewBox" in text, f"{n}: missing viewBox"
print("all 5 SVGs OK")
EOF
```

Expected: `all 5 SVGs OK`

- [ ] **Step 6: Verify visually**

Open `assets/logo-light.svg` and `assets/favicon.svg` in a browser (`xdg-open assets/logo-light.svg`). Check: reads "soilmass", grade gap is a thin clean horizontal slice in the lower third, ochre band below it; favicon "s" legible with visible gap.

- [ ] **Step 7: Commit**

```bash
git add tools/build_logos.py assets/
git commit -m "feat: generate outline logo SVGs from Archivo variable font

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
```

---

### Task 3: Guidelines — overview and voice

**Files:**
- Create: `guidelines/00-overview.md`
- Create: `guidelines/06-voice-and-tone.md`

**Interfaces:**
- Produces: section content that Task 9 mirrors into `index.html` sections `#overview` and `#voice`. Heading text and tagline strings must match exactly.

- [ ] **Step 1: Write guidelines/00-overview.md**

```markdown
# 00 — Overview

soilmass is a web agency. The name is a geotechnical term: the body of earth
an engineer tests before anything is built on it. That is the promise of the
brand — websites that stand on measured, solid ground.

**Tagline:** Solid ground for the web.

## Concept

Engineered foundations for the web. The visual language is Swiss
International Typographic Style — strict grid, large confident type,
generous whitespace — detailed with geotechnical motifs: grade lines,
hatching, strata, dimension annotations.

## Personality

| We are | We are not |
|---|---|
| Precise | Cold |
| Grounded | Rustic |
| Confident | Loud |
| Warm in words | Casual in form |

The tension is deliberate: rigorous visuals, warm and consultative voice.
Keep both; the brand breaks if either side wins.

## The system at a glance

- One typeface family for reading (Archivo), one for measuring (JetBrains Mono).
- Warm stone neutrals; a single ochre accent used as punctuation, never flood.
- Square corners everywhere. No border radius, ever.
- Diagrams before photographs.
```

- [ ] **Step 2: Write guidelines/06-voice-and-tone.md**

```markdown
# 06 — Voice & tone

soilmass writes the way a trusted engineer talks to a neighbor: warm,
plain, and precise. The visuals carry the rigor; the words carry the warmth.

**Tagline:** Solid ground for the web.

## Principles

1. **Explain like a trusted engineer-neighbor.** Expert, never superior.
2. **Precision earns warmth.** Show numbers when we have them: load times,
   scores, dates. Friendly claims backed by measurements.
3. **"You" before "we".** Lead with the client's situation, then our part.
4. **No jargon without a plain-words translation.** Technical terms are
   welcome when they are immediately explained.

## Sounds like us

> We'll walk you through every layer of the build — and show you the
> numbers behind each decision.

> Your homepage loads in 1.2 seconds. We think we can get it under one.

## Doesn't sound like us

> We leverage cutting-edge synergies to deliver best-in-class digital
> experiences at scale.

> Our bleeding-edge stack empowers holistic omnichannel journeys.

## Mechanics

- Sentence case everywhere, including headings. The wordmark is always lowercase.
- Contractions welcome. Exclamation marks are not.
- Numbers as digits (1.2 s, 14 pages, 99/100) — they are part of the brand.
```

- [ ] **Step 3: Verify**

```bash
grep -c "Solid ground for the web." guidelines/00-overview.md guidelines/06-voice-and-tone.md
```

Expected: count ≥ 1 in each file.

- [ ] **Step 4: Commit**

```bash
git add guidelines/
git commit -m "docs: add overview and voice & tone guidelines

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
```

---

### Task 4: Guidelines — logo and color

**Files:**
- Create: `guidelines/01-logo.md`
- Create: `guidelines/02-color.md`
- Test: `tools/check_contrast.py` (from Task 1)

**Interfaces:**
- Consumes: asset filenames from Task 2 (referenced by relative path).
- Produces: content mirrored into `index.html` sections `#logo` and `#color` (Task 7). Token names and hex values must match `tools/check_contrast.py` exactly.

- [ ] **Step 1: Write guidelines/01-logo.md**

```markdown
# 01 — Logo

## Primary mark: the grade-gap wordmark

Lowercase `soilmass`, Archivo 900 (Black), letter-spacing −0.03em. A
horizontal "grade line" of background color cuts through the letters:

- Ink `#191714` (paper `#FAF9F6` on dark) from the top down to **71%** of
  the wordmark height.
- Background-colored gap from **71% to 74%** (3% of wordmark height).
- Earth ochre `#C98A12` from **74%** to the baseline.

Percentages are measured on the full wordmark bounding box, ascender of "l"
included. Word recognition relies on the upper half of letterforms, so the
intact top 71% keeps the mark instantly legible; the ochre band below the
grade line is the brand story — mass below grade.

Files: `assets/logo-light.svg`, `assets/logo-dark.svg`.

## Variants and size rules

| Context | Use |
|---|---|
| ≥ 26 px tall | Two-tone grade-gap wordmark (light or dark version) |
| < 26 px tall | `assets/wordmark-small.svg` — solid ink `soilmass` + ochre full stop |
| Favicon / avatar | `assets/favicon.svg` — ink tile, grade-gap "s"; its gap is optically enlarged to ~7% of glyph height to survive 16 px rendering |
| Single-color print | `assets/logo-mono.svg` — one color, gap retained (the gap alone carries the concept) |

## Rules

- Clear space: at least ½ of the wordmark height on all sides.
- Never recolor, rotate, stretch, add effects, or place the two-tone mark on
  busy or low-contrast backgrounds.
- The ochre band sits below AA contrast on paper; that is acceptable —
  logotypes are exempt (WCAG 1.4.3).
- The SVGs are pure outlines and must stay that way: no `<text>` elements.
```

- [ ] **Step 2: Write guidelines/02-color.md**

```markdown
# 02 — Color

Warm stone neutrals plus one ochre accent. Nothing else — no other hues, no
pure white `#FFFFFF`, no pure black `#000000`.

## Neutrals

| Token | Hex | Use |
|---|---|---|
| paper | `#FAF9F6` | default background |
| stone-100 | `#F0EEE8` | subtle panels, alternate sections |
| stone-200 | `#E8E5DE` | borders, dividers |
| stone-300 | `#D8D4CC` | disabled, faint rules |
| stone-400 | `#A8A29A` | placeholder, faint text on dark |
| stone-500 | `#78736A` | secondary text at large sizes only (4.47:1) |
| stone-600 | `#59544B` | secondary text, captions |
| ink | `#191714` | primary text, dark backgrounds |

## Ochre

| Token | Hex | Use |
|---|---|---|
| ochre-100 | `#F7EBD3` | tint backgrounds, highlights |
| ochre-500 | `#C98A12` | graphic devices, logo band, fills, type on dark only |
| ochre-600 | `#8F620B` | all ochre text on paper, any size (5.09:1, AA) |

## Rules

1. **Ochre is punctuation, never flood.** One ochre moment per composition.
2. Body text on paper is ink or stone-600 only.
3. Ochre text on paper always uses ochre-600 — ochre-500 on paper is 2.80:1
   and fails AA even for large type. Ochre-500 type only on ink/dark (6.07:1).
4. Text on ochre-500 fills (buttons, highlights) is always ink (6.07:1),
   never paper (2.80:1). Paper text is allowed on ochre-600 fills (5.09:1).
5. Every documented combination is enforced by `tools/check_contrast.py` —
   run it after any palette change.
```

- [ ] **Step 3: Run the contrast test against the documented values**

Run: `python3 tools/check_contrast.py; echo "exit=$?"`
Expected: 12 `PASS` lines, `exit=0`.

- [ ] **Step 4: Cross-check hex values**

```bash
for hex in FAF9F6 F0EEE8 E8E5DE D8D4CC A8A29A 78736A 59544B 191714 F7EBD3 C98A12 8F620B; do
  grep -q "$hex" guidelines/02-color.md || echo "MISSING $hex"
done; echo done
```

Expected: only `done` — no `MISSING` lines.

- [ ] **Step 5: Commit**

```bash
git add guidelines/
git commit -m "docs: add logo and color guidelines

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
```

---

### Task 5: Guidelines — typography, layout, imagery, applications

**Files:**
- Create: `guidelines/03-typography.md`
- Create: `guidelines/04-layout-and-devices.md`
- Create: `guidelines/05-imagery-and-iconography.md`
- Create: `guidelines/07-applications.md`

**Interfaces:**
- Produces: content mirrored into `index.html` sections `#typography`, `#layout`, `#imagery`, `#applications` (Tasks 8–9). The device construction values (3px rule, 135° hatch, 5/8/12px strata, 8% grid) are consumed verbatim by the CSS in Task 6.

- [ ] **Step 1: Write guidelines/03-typography.md**

```markdown
# 03 — Typography

Two families, two jobs. **Archivo** reads; **JetBrains Mono** measures.
Both served from Google Fonts: Archivo 400/600/900, JetBrains Mono 400/600.

## Scale (desktop)

| Style | Size / leading | Face | Notes |
|---|---|---|---|
| Display | 64 / 68 | Archivo 900 | tracking −0.03em |
| H1 | 40 / 44 | Archivo 900 | tracking −0.02em |
| H2 | 28 / 34 | Archivo 600 | |
| H3 | 20 / 28 | Archivo 600 | |
| Body | 16 / 26 | Archivo 400 | max measure 70 characters |
| Small | 14 / 22 | Archivo 400 | stone-600 |
| Label | 12 / 16 | JetBrains Mono 400 | UPPERCASE, tracking +0.12em |

Mobile: Display and H1 scale down fluidly (clamp between roughly 60% and
100% of the desktop size); H2 and below are unchanged.

## Rules

- Labels are the mono voice: figure numbers (`FIG. 01`), captions, data,
  annotations — anything measured or numbered. Ochre labels use ochre-600
  on paper, ochre-500 on dark.
- Headings and UI text are sentence case. Only labels are uppercase.
- Never use Archivo 900 below H1 sizes; never set body text in the mono.
```

- [ ] **Step 2: Write guidelines/04-layout-and-devices.md**

```markdown
# 04 — Layout & graphic devices

## Layout

- Spacing base 8px. Allowed steps: 4, 8, 16, 24, 32, 48, 64, 96, 128.
- Grid: 12 columns, 1200px max content width, 24px gutters.
- **Square corners everywhere. No border radius, ever.**
- Whitespace is a material — sections breathe (96–128px vertical padding).

## Signature devices

1. **Ground symbol** — a 3px ink horizontal rule with a 16px band of 135°
   hatching below it (2px ochre-500 lines at 55% opacity, 4px gaps). Marks
   the foot of heroes and major sections.
2. **Strata bars** — three left-aligned stacked bars, widths equal, heights
   5 / 8 / 12px with 3px gaps; top bar ochre-500, lower two ink. Use as a
   compact brand signature where the wordmark is too much.
3. **Dimension callout** — 2px end ticks + rule + centered mono label in
   ochre-600 (ochre-500 on dark). Annotates real measurements in diagrams.
4. **Grid paper** — square grid background, ink at 8% opacity, 24px cells.
   Backdrop for diagrams and technical illustrations only.

Use at most two devices per composition; the ground symbol counts as the
composition's single ochre moment when hatched.
```

- [ ] **Step 3: Write guidelines/05-imagery-and-iconography.md**

```markdown
# 05 — Imagery & iconography

## Graphic-first

soilmass does not use photography by default. Visual interest comes from
the signature devices and from technical diagrams drawn in brand colors on
grid paper. If a layout feels empty, add a diagram or annotation — not a
stock photo.

## The photo escape hatch

When a real photograph is unavoidable (team headshots, client work):

- Apply the **ochre duotone**: desaturate to grayscale, boost contrast
  slightly, multiply over ochre-500. Any source photo becomes on-brand.
- Client work screenshots may instead be shown unfiltered inside an ink
  browser-chrome frame (square corners).

Never: full-color lifestyle photos, stock imagery, AI-generated scenes.

## Iconography

- Geometric line style: 2px stroke, square terminals and joins (no rounds).
- Drawn on a 24px grid; optical corrections allowed, decoration not.
- Ink by default. At most one element per icon may be ochre-500 (ochre-600
  if the icon sits on paper at small sizes).
```

- [ ] **Step 4: Write guidelines/07-applications.md**

```markdown
# 07 — Applications

Reference applications live in `index.html` (section 07), built with the
real tokens. Rules that generalize:

## Website hero

Display type + tagline + one ochre CTA (ink text on ochre-500 fill) +
ground symbol at the foot. Nothing else competes.

## Business card

Front: two-tone wordmark centered on paper, generous clear space. Back:
ink, mono contact block in paper text, strata bars bottom-left.
85.6 × 54 mm, square corners.

## Email signature

HTML-safe subset only: the small-size fallback wordmark (`soilmass.` solid),
Archivo unavailable in email clients falls back to Arial — acceptable here
only. Name, role, then mono-styled (monospace stack) URL and email in
ochre-600. No images, no banners.

## Social banner

Dark (ink) canvas, strata bars, tagline in Display type, dark-version
wordmark bottom-right. The one place ochre-500 type is encouraged — it
passes AA on ink.
```

- [ ] **Step 5: Verify key values present**

```bash
grep -q "64 / 68" guidelines/03-typography.md && \
grep -q "5 / 8 / 12px" guidelines/04-layout-and-devices.md && \
grep -q "ochre duotone" guidelines/05-imagery-and-iconography.md && \
grep -q "ink text on ochre-500 fill" guidelines/07-applications.md && echo OK
```

Expected: `OK`

- [ ] **Step 6: Commit**

```bash
git add guidelines/
git commit -m "docs: add typography, layout, imagery, and applications guidelines

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
```

---

### Task 6: index.html — skeleton, tokens CSS, nav, overview section

**Files:**
- Create: `index.html`

**Interfaces:**
- Consumes: `assets/logo-light.svg`, `assets/favicon.svg` (Task 2).
- Produces: the complete CSS design system (custom properties + classes `label`, `ground`, `strata`, `dim`, `grid-paper`, `swatches`, `btn`, `panel`, `dont`) and eight empty `<section>` shells with ids `overview logo color typography layout imagery voice applications` that Tasks 7–9 fill. **Later tasks insert content between the marker comments `<!-- §NN -->` and `<!-- /§NN -->` — do not rename ids or markers.**

- [ ] **Step 1: Write index.html**

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>soilmass — brand guidelines</title>
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;600;900&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>
:root{
  --paper:#FAF9F6; --stone-100:#F0EEE8; --stone-200:#E8E5DE; --stone-300:#D8D4CC;
  --stone-400:#A8A29A; --stone-500:#78736A; --stone-600:#59544B; --ink:#191714;
  --ochre-100:#F7EBD3; --ochre-500:#C98A12; --ochre-600:#8F620B;
  --sans:'Archivo',Arial,sans-serif; --mono:'JetBrains Mono',monospace;
}
*{margin:0;padding:0;box-sizing:border-box;border-radius:0}
html{scroll-behavior:smooth}
body{background:var(--paper);color:var(--ink);font:400 16px/26px var(--sans)}
main{max-width:1200px;margin:0 auto;padding:0 24px}
section{padding:96px 0;border-top:1px solid var(--stone-200)}
p{max-width:70ch}
p+p{margin-top:16px}
a{color:var(--ochre-600)}
h1{font:900 clamp(28px,5vw,40px)/1.1 var(--sans);letter-spacing:-.02em;margin-bottom:32px}
h2{font:600 28px/34px var(--sans);margin:48px 0 16px}
h3{font:600 20px/28px var(--sans);margin:32px 0 8px}
.display{font:900 clamp(40px,7vw,64px)/1.06 var(--sans);letter-spacing:-.03em}
.small{font:400 14px/22px var(--sans);color:var(--stone-600)}
.label{font:400 12px/16px var(--mono);text-transform:uppercase;letter-spacing:.12em;color:var(--ochre-600)}
.label--quiet{color:var(--stone-600)}
/* header */
header{position:sticky;top:0;background:var(--paper);border-bottom:1px solid var(--stone-200);z-index:9}
header .bar{max-width:1200px;margin:0 auto;padding:16px 24px;display:flex;align-items:center;gap:24px;flex-wrap:wrap}
header img{height:28px;display:block}
header nav{display:flex;gap:16px;flex-wrap:wrap}
header nav a{font:400 12px/16px var(--mono);text-transform:uppercase;letter-spacing:.12em;text-decoration:none}
/* devices */
.ground{border-top:3px solid var(--ink);height:16px;
  background:repeating-linear-gradient(135deg,transparent 0 4px,rgba(201,138,18,.55) 4px 6px)}
.strata span{display:block;width:44px;background:var(--ink)}
.strata span:nth-child(1){height:5px;background:var(--ochre-500)}
.strata span:nth-child(2){height:8px;margin-top:3px}
.strata span:nth-child(3){height:12px;margin-top:3px}
.dim{display:flex;align-items:center;color:var(--ochre-600)}
.dim i{width:2px;height:10px;background:currentColor}
.dim b{flex:1;height:2px;background:currentColor}
.dim .label{color:inherit;padding:0 8px}
.grid-paper{background-image:linear-gradient(rgba(25,23,20,.08) 1px,transparent 1px),
  linear-gradient(90deg,rgba(25,23,20,.08) 1px,transparent 1px);background-size:24px 24px}
/* components */
.btn{display:inline-block;background:var(--ochre-500);color:var(--ink);
  font:600 14px/1 var(--sans);padding:14px 24px;text-decoration:none}
.panel{background:var(--stone-100);padding:24px}
.dark{background:var(--ink);color:var(--paper)}
.cols{display:grid;gap:24px;grid-template-columns:repeat(auto-fit,minmax(260px,1fr))}
.swatches{display:grid;gap:8px;grid-template-columns:repeat(auto-fit,minmax(110px,1fr))}
.swatch .chip{height:56px;border:1px solid var(--stone-200)}
.swatch .hx{font:400 11px/16px var(--mono);color:var(--stone-600);margin-top:4px}
table{border-collapse:collapse;width:100%;margin:16px 0}
td,th{border:1px solid var(--stone-200);padding:8px 12px;text-align:left;font-size:14px;line-height:22px}
th{font-family:var(--mono);font-size:11px;text-transform:uppercase;letter-spacing:.12em;color:var(--stone-600)}
figure figcaption{margin-top:8px}
footer{border-top:1px solid var(--stone-200);padding:48px 24px;text-align:center}
@media (max-width:600px){section{padding:48px 0}}
</style>
</head>
<body>
<header>
  <div class="bar">
    <a href="#top"><img src="assets/logo-light.svg" alt="soilmass"></a>
    <nav>
      <a href="#overview">00 Overview</a><a href="#logo">01 Logo</a>
      <a href="#color">02 Color</a><a href="#typography">03 Type</a>
      <a href="#layout">04 Layout</a><a href="#imagery">05 Imagery</a>
      <a href="#voice">06 Voice</a><a href="#applications">07 Applications</a>
    </nav>
  </div>
</header>
<main id="top">

<section id="overview" style="border-top:0">
<!-- §00 -->
<p class="label">00 / Overview</p>
<p class="display" style="margin:24px 0">Solid ground<br>for the web.</p>
<p>soilmass is a web agency. The name is a geotechnical term: the body of
earth an engineer tests before anything is built on it. That is the promise
of the brand — websites that stand on measured, solid ground.</p>
<p>The visual language is Swiss International Typographic Style — strict
grid, large confident type, generous whitespace — detailed with geotechnical
motifs: grade lines, hatching, strata, dimension annotations. The visuals
carry the rigor; the words carry the warmth. Keep both; the brand breaks if
either side wins.</p>
<div class="ground" style="margin-top:48px"></div>
<!-- /§00 -->
</section>

<section id="logo"><!-- §01 --><!-- /§01 --></section>
<section id="color"><!-- §02 --><!-- /§02 --></section>
<section id="typography"><!-- §03 --><!-- /§03 --></section>
<section id="layout"><!-- §04 --><!-- /§04 --></section>
<section id="imagery"><!-- §05 --><!-- /§05 --></section>
<section id="voice"><!-- §06 --><!-- /§06 --></section>
<section id="applications"><!-- §07 --><!-- /§07 --></section>

</main>
<footer>
  <p class="label label--quiet">soilmass — brand guidelines · canonical source: /guidelines · generated assets: /assets</p>
</footer>
</body>
</html>
```

- [ ] **Step 2: Verify structure**

```bash
python3 - <<'EOF'
from html.parser import HTMLParser
from pathlib import Path
ids, ok = [], True
class P(HTMLParser):
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "section" and "id" in d: ids.append(d["id"])
text = Path("index.html").read_text()
P().feed(text)
expected = ["overview","logo","color","typography","layout","imagery","voice","applications"]
assert ids == expected, f"sections wrong: {ids}"
assert "border-radius:0" in text and text.count("border-radius") == 1, "border-radius leak"
print("skeleton OK:", ", ".join(ids))
EOF
```

Expected: `skeleton OK: overview, logo, color, ...` (all eight, in order).

- [ ] **Step 3: Open in browser**

Run: `xdg-open index.html` — header shows the two-tone wordmark at 28px, overview section renders Display type and the ground symbol.

- [ ] **Step 4: Commit**

```bash
git add index.html
git commit -m "feat: add brand book skeleton with token CSS and overview

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
```

---

### Task 7: index.html — logo and color sections

**Files:**
- Modify: `index.html` (fill `<!-- §01 -->` and `<!-- §02 -->` markers)

**Interfaces:**
- Consumes: CSS classes from Task 6; SVGs from Task 2.

- [ ] **Step 1: Fill the logo section**

Replace `<!-- §01 --><!-- /§01 -->` inside `<section id="logo">` with:

```html
<!-- §01 -->
<p class="label">01 / Logo</p>
<h1>The grade-gap wordmark</h1>
<p>Lowercase <strong>soilmass</strong>, Archivo 900, letter-spacing −0.03em.
A horizontal grade line of background color cuts the letters at 71–74% of
the wordmark height; below it, the mass sits in earth ochre. You read words
from the tops of letters, so the intact top 71% keeps the mark instantly
legible — the ochre band is the story, not the information.</p>
<div class="cols" style="margin-top:32px">
  <figure><div style="padding:48px 24px;border:1px solid var(--stone-200);text-align:center">
    <img src="assets/logo-light.svg" alt="soilmass wordmark, light version" style="height:56px;max-width:100%">
  </div><figcaption class="label label--quiet">On paper — assets/logo-light.svg</figcaption></figure>
  <figure><div class="dark" style="padding:48px 24px;text-align:center">
    <img src="assets/logo-dark.svg" alt="soilmass wordmark, dark version" style="height:56px;max-width:100%">
  </div><figcaption class="label label--quiet">On ink — assets/logo-dark.svg</figcaption></figure>
</div>
<h2>Variants &amp; size rules</h2>
<table>
  <tr><th>Context</th><th>Use</th></tr>
  <tr><td>≥ 26 px tall</td><td>Two-tone grade-gap wordmark</td></tr>
  <tr><td>&lt; 26 px tall</td><td><img src="assets/wordmark-small.svg" alt="soilmass." style="height:16px;vertical-align:middle"> solid fallback — wordmark-small.svg</td></tr>
  <tr><td>Favicon / avatar</td><td><img src="assets/favicon.svg" alt="favicon tile" style="height:24px;vertical-align:middle"> ink tile, grade-gap “s”, gap optically enlarged to ~7%</td></tr>
  <tr><td>Single color</td><td><img src="assets/logo-mono.svg" alt="mono wordmark" style="height:20px;vertical-align:middle"> one color, gap retained — logo-mono.svg</td></tr>
</table>
<h2>Rules</h2>
<p>Clear space: ½ wordmark height on all sides. Never recolor, rotate,
stretch, add effects, or place the two-tone mark on busy backgrounds.
The ochre band is exempt from text contrast rules (WCAG 1.4.3, logotypes).</p>
<!-- /§01 -->
```

- [ ] **Step 2: Fill the color section**

Replace `<!-- §02 --><!-- /§02 -->` inside `<section id="color">` with:

```html
<!-- §02 -->
<p class="label">02 / Color</p>
<h1>Warm stone, one ochre</h1>
<h2>Neutrals</h2>
<div class="swatches">
  <div class="swatch"><div class="chip" style="background:var(--paper)"></div><div class="hx">paper<br>#FAF9F6</div></div>
  <div class="swatch"><div class="chip" style="background:var(--stone-100)"></div><div class="hx">stone-100<br>#F0EEE8</div></div>
  <div class="swatch"><div class="chip" style="background:var(--stone-200)"></div><div class="hx">stone-200<br>#E8E5DE</div></div>
  <div class="swatch"><div class="chip" style="background:var(--stone-300)"></div><div class="hx">stone-300<br>#D8D4CC</div></div>
  <div class="swatch"><div class="chip" style="background:var(--stone-400)"></div><div class="hx">stone-400<br>#A8A29A</div></div>
  <div class="swatch"><div class="chip" style="background:var(--stone-500)"></div><div class="hx">stone-500<br>#78736A</div></div>
  <div class="swatch"><div class="chip" style="background:var(--stone-600)"></div><div class="hx">stone-600<br>#59544B</div></div>
  <div class="swatch"><div class="chip" style="background:var(--ink)"></div><div class="hx">ink<br>#191714</div></div>
</div>
<h2>Ochre</h2>
<div class="swatches" style="max-width:420px">
  <div class="swatch"><div class="chip" style="background:var(--ochre-100)"></div><div class="hx">ochre-100<br>#F7EBD3</div></div>
  <div class="swatch"><div class="chip" style="background:var(--ochre-500)"></div><div class="hx">ochre-500<br>#C98A12</div></div>
  <div class="swatch"><div class="chip" style="background:var(--ochre-600)"></div><div class="hx">ochre-600<br>#8F620B</div></div>
</div>
<h2>Rules</h2>
<p><strong>Ochre is punctuation, never flood</strong> — one ochre moment per
composition. Body text on paper is ink or stone-600 only. Ochre text on
paper always uses ochre-600 (ochre-500 on paper is 2.80:1 — fails AA at any
size); ochre-500 type is reserved for dark backgrounds (6.07:1). Text on
ochre-500 fills is always ink, never paper. Every documented pair is
enforced by <code>tools/check_contrast.py</code>.</p>
<div class="cols" style="margin-top:24px">
  <div class="panel"><p class="label" style="margin-bottom:8px">✓ Button</p><span class="btn">Start a project</span></div>
  <div class="panel dark" style="background:var(--ink)"><p class="label" style="color:var(--ochre-500);margin-bottom:8px">✓ Ochre type on dark</p><p class="display" style="font-size:28px;line-height:1.2;color:var(--ochre-500)">6.07:1</p></div>
</div>
<!-- /§02 -->
```

- [ ] **Step 3: Verify**

```bash
python3 -c "
from pathlib import Path
t = Path('index.html').read_text()
for hex in ('FAF9F6','F0EEE8','E8E5DE','D8D4CC','A8A29A','78736A','59544B','191714','F7EBD3','C98A12','8F620B'):
    assert hex in t, f'missing {hex}'
for a in ('logo-light.svg','logo-dark.svg','logo-mono.svg','wordmark-small.svg','favicon.svg'):
    assert a in t, f'missing {a}'
print('logo+color sections OK')"
```

Expected: `logo+color sections OK`. Then reload in browser — swatch grid and both wordmark panels render.

- [ ] **Step 4: Commit**

```bash
git add index.html
git commit -m "feat: add logo and color sections to brand book

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
```

---

### Task 8: index.html — typography, layout, imagery sections

**Files:**
- Modify: `index.html` (fill `<!-- §03 -->`, `<!-- §04 -->`, `<!-- §05 -->`)

**Interfaces:**
- Consumes: CSS classes from Task 6 (`label`, `ground`, `strata`, `dim`, `grid-paper`, `panel`, `cols`).

- [ ] **Step 1: Fill the typography section**

Replace `<!-- §03 --><!-- /§03 -->` with:

```html
<!-- §03 -->
<p class="label">03 / Typography</p>
<h1>Archivo reads, the mono measures</h1>
<div style="display:flex;flex-direction:column;gap:24px;margin-top:32px">
  <div><span class="display">Display 900</span> <span class="label label--quiet" style="margin-left:12px">64/68 · −0.03em</span></div>
  <div><span style="font:900 40px/44px var(--sans);letter-spacing:-.02em">Heading 1</span> <span class="label label--quiet" style="margin-left:12px">40/44 · Archivo 900</span></div>
  <div><span style="font:600 28px/34px var(--sans)">Heading 2</span> <span class="label label--quiet" style="margin-left:12px">28/34 · Archivo 600</span></div>
  <div><span style="font:600 20px/28px var(--sans)">Heading 3</span> <span class="label label--quiet" style="margin-left:12px">20/28 · Archivo 600</span></div>
  <div><p>Body — 16/26 Archivo 400. Maximum measure 70 characters, like this
  paragraph. Warm words, measured claims, numbers as digits.</p></div>
  <div><span class="small">Small — 14/22, stone-600, for captions and metadata.</span></div>
  <div><span class="label">Label — 12/16 JetBrains Mono · uppercase · +0.12em — fig. numbers, data, annotations</span></div>
</div>
<p style="margin-top:32px">Labels are the mono voice of the brand: anything
measured, numbered, or annotated. Headings are sentence case; only labels
are uppercase. Never use Archivo 900 below H1 sizes; never set body text in
the mono.</p>
<!-- /§03 -->
```

- [ ] **Step 2: Fill the layout section**

Replace `<!-- §04 --><!-- /§04 -->` with:

```html
<!-- §04 -->
<p class="label">04 / Layout &amp; devices</p>
<h1>Eight-pixel ground rules</h1>
<p>Spacing base 8px — allowed steps 4, 8, 16, 24, 32, 48, 64, 96, 128.
Twelve columns, 1200px max width, 24px gutters. Square corners everywhere:
no border radius, ever. Whitespace is a material — major sections breathe
with 96–128px of vertical padding.</p>
<h2>Signature devices</h2>
<div class="cols" style="margin-top:24px">
  <figure><div class="ground" style="margin-top:24px"></div>
    <figcaption class="label label--quiet" style="margin-top:16px">Ground symbol — 3px rule, 135° ochre hatch</figcaption></figure>
  <figure><div class="strata"><span></span><span></span><span></span></div>
    <figcaption class="label label--quiet" style="margin-top:16px">Strata bars — 5/8/12px, topsoil ochre</figcaption></figure>
  <figure><div class="dim"><i></i><b></b><span class="label">1200px</span><b></b><i></i></div>
    <figcaption class="label label--quiet" style="margin-top:16px">Dimension callout — annotates measurements</figcaption></figure>
  <figure><div class="grid-paper" style="height:56px;border:1px solid var(--stone-200)"></div>
    <figcaption class="label label--quiet" style="margin-top:16px">Grid paper — ink 8%, 24px cells</figcaption></figure>
</div>
<p style="margin-top:24px">Use at most two devices per composition; a
hatched ground symbol counts as the composition’s single ochre moment.</p>
<!-- /§04 -->
```

- [ ] **Step 3: Fill the imagery section**

Replace `<!-- §05 --><!-- /§05 -->` with:

```html
<!-- §05 -->
<p class="label">05 / Imagery &amp; iconography</p>
<h1>Diagrams before photographs</h1>
<p>soilmass does not use photography by default. Visual interest comes from
the signature devices and technical diagrams drawn in brand colors on grid
paper. If a layout feels empty, add a diagram or an annotation — not a
stock photo.</p>
<div class="grid-paper" style="border:1px solid var(--stone-200);padding:24px;margin:24px 0">
  <p class="label" style="margin-bottom:16px">Fig. 05 — a soilmass diagram</p>
  <div style="display:flex;align-items:flex-end;gap:16px">
    <div style="width:64px;height:88px;border:2px solid var(--ink)"></div>
    <div style="width:40px;height:56px;border:2px solid var(--ink)"></div>
    <div style="width:88px;height:72px;background:var(--ink)"></div>
    <span class="label">▼ load</span>
  </div>
  <div class="ground" style="margin-top:16px"></div>
</div>
<h2>The photo escape hatch</h2>
<p>When a real photo is unavoidable (headshots, client work): grayscale,
slight contrast boost, multiplied over ochre-500 — the ochre duotone. Client
screenshots may instead sit unfiltered in an ink browser-chrome frame.
Never full-color lifestyle or stock photography.</p>
<h2>Iconography</h2>
<p>Geometric line icons: 2px stroke, square terminals and joins, drawn on a
24px grid. Ink by default; at most one element per icon in ochre.</p>
<div style="display:flex;gap:24px;margin-top:16px">
  <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#191714" stroke-width="2" aria-label="strata icon"><path d="M3 7h18M3 12h18M3 17h18" stroke="#191714"/><path d="M3 7h18" stroke="#8F620B"/></svg>
  <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#191714" stroke-width="2" aria-label="ruler icon"><rect x="3" y="9" width="18" height="6"/><path d="M7 9v3M12 9v3M17 9v3" stroke="#8F620B"/></svg>
  <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#191714" stroke-width="2" aria-label="foundation icon"><rect x="6" y="4" width="12" height="10"/><path d="M3 18h18" stroke="#8F620B"/><path d="M9 14v4M15 14v4"/></svg>
</div>
<!-- /§05 -->
```

- [ ] **Step 4: Verify and eyeball**

```bash
python3 -c "
from pathlib import Path
t = Path('index.html').read_text()
for marker in ('/§03','/§04','/§05'):
    assert t.count(marker) == 1, marker
assert 'grid-paper' in t and 'strata' in t and 'Fig. 05' in t
print('sections 03-05 OK')"
```

Expected: `sections 03-05 OK`. Reload in browser: type specimen renders in real sizes, all four devices visible, diagram sits on grid paper.

- [ ] **Step 5: Commit**

```bash
git add index.html
git commit -m "feat: add typography, layout, and imagery sections to brand book

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
```

---

### Task 9: index.html — voice, applications, final verification

**Files:**
- Modify: `index.html` (fill `<!-- §06 -->`, `<!-- §07 -->`)
- Test: `tools/check_contrast.py`, structural checks

**Interfaces:**
- Consumes: everything prior. This completes the deliverable.

- [ ] **Step 1: Fill the voice section**

Replace `<!-- §06 --><!-- /§06 -->` with:

```html
<!-- §06 -->
<p class="label">06 / Voice &amp; tone</p>
<h1>Warm words, measured claims</h1>
<p>soilmass writes the way a trusted engineer talks to a neighbor: warm,
plain, and precise. Four principles: explain like a trusted
engineer-neighbor; precision earns warmth — show numbers when we have them;
“you” before “we”; no jargon without a plain-words translation.</p>
<div class="cols" style="margin-top:24px">
  <div class="panel">
    <p class="label" style="margin-bottom:8px">✓ Sounds like us</p>
    <p>“We’ll walk you through every layer of the build — and show you the
    numbers behind each decision.”</p>
  </div>
  <div class="panel">
    <p class="label label--quiet" style="margin-bottom:8px">✗ Doesn’t</p>
    <p class="small">“We leverage cutting-edge synergies to deliver
    best-in-class digital experiences at scale.”</p>
  </div>
</div>
<p style="margin-top:24px">Sentence case everywhere, including headings. The
wordmark is always lowercase. Contractions welcome; exclamation marks are
not. Numbers as digits — they are part of the brand.</p>
<!-- /§06 -->
```

- [ ] **Step 2: Fill the applications section**

Replace `<!-- §07 --><!-- /§07 -->` with:

```html
<!-- §07 -->
<p class="label">07 / Applications</p>
<h1>The system at work</h1>

<h2>Website hero</h2>
<div style="border:1px solid var(--stone-200)">
  <div style="display:flex;justify-content:space-between;align-items:center;padding:16px 24px;border-bottom:1px solid var(--stone-200)">
    <img src="assets/logo-light.svg" alt="soilmass" style="height:26px">
    <span class="label label--quiet">Work · Method · Contact</span>
  </div>
  <div style="padding:64px 24px">
    <p class="display">Solid ground<br>for the web.</p>
    <p style="margin-top:16px">Websites that stand on measured foundations —
    performance budgets, accessibility audits, structural markup.</p>
    <p style="margin-top:24px"><a class="btn" href="#applications">Start a project</a></p>
  </div>
  <div class="ground"></div>
</div>

<h2>Business card</h2>
<div class="cols">
  <div style="border:1px solid var(--stone-200);aspect-ratio:85.6/54;display:flex;align-items:center;justify-content:center">
    <img src="assets/logo-light.svg" alt="soilmass" style="height:15%">
  </div>
  <div class="dark" style="aspect-ratio:85.6/54;padding:8%;display:flex;flex-direction:column;justify-content:space-between">
    <div>
      <p style="font:600 16px/24px var(--sans)">Edison Steele</p>
      <p class="label" style="color:var(--ochre-500)">Founder</p>
      <p class="label" style="color:var(--stone-400);margin-top:8px">edison@soilmass.studio<br>soilmass.studio</p>
    </div>
    <div class="strata"><span></span><span></span><span></span></div>
  </div>
</div>

<h2>Email signature</h2>
<div class="panel" style="max-width:480px">
  <p style="font:900 18px/24px var(--sans);letter-spacing:-.03em">soilmass<span style="color:var(--ochre-600)">.</span></p>
  <p style="font:600 14px/22px var(--sans);margin-top:8px">Edison Steele · Founder</p>
  <p class="label" style="margin-top:4px">edison@soilmass.studio · soilmass.studio</p>
  <p class="small" style="margin-top:8px">Solid ground for the web.</p>
</div>

<h2>Social banner</h2>
<div class="dark" style="padding:48px 32px;display:flex;justify-content:space-between;align-items:flex-end;gap:24px;flex-wrap:wrap">
  <div>
    <div class="strata" style="margin-bottom:24px"><span></span><span></span><span></span></div>
    <p class="display" style="font-size:clamp(28px,5vw,48px)">Solid ground for the web.</p>
  </div>
  <img src="assets/logo-dark.svg" alt="soilmass" style="height:28px">
</div>
<!-- /§07 -->
```

- [ ] **Step 3: Full verification suite**

```bash
python3 tools/check_contrast.py && python3 - <<'EOF'
from html.parser import HTMLParser
from pathlib import Path
t = Path("index.html").read_text()
assert t.count("border-radius") == 1        # only the reset
assert "#FFFFFF" not in t.upper().replace("#FFF;", "")  # no pure white
assert "Solid ground" in t
for m in ("/§00","/§01","/§02","/§03","/§04","/§05","/§06","/§07"):
    assert t.count(m) == 1, f"marker {m}"
class P(HTMLParser):
    def __init__(self):
        super().__init__(); self.stack=[]; self.void={"img","br","meta","link","input","hr"}
    def handle_starttag(self,tag,attrs):
        if tag not in self.void: self.stack.append(tag)
    def handle_endtag(self,tag):
        assert self.stack and self.stack[-1]==tag, f"mismatch at {tag}"
        self.stack.pop()
p=P(); p.feed(t); assert not p.stack, f"unclosed: {p.stack}"
print("final checks OK")
EOF
```

Expected: 12 contrast `PASS` lines, then `final checks OK`.

- [ ] **Step 4: Browser walkthrough**

`xdg-open index.html` — scroll all eight sections at desktop width, then narrow the window to ~360px: no horizontal scrollbar, nav wraps, hero display type scales down via clamp.

- [ ] **Step 5: Commit**

```bash
git add index.html
git commit -m "feat: complete brand book with voice and application examples

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
```
