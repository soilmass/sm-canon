# 01 — Logo

## Primary mark: the grade-gap wordmark

Lowercase `soilmass`, Archivo 900 (Black), letter-spacing −0.03em. A
horizontal "grade line" of background color cuts through the letters:

- Ink `#191714` (paper `#FAF9F6` on dark) from the top down to **81.5%** of
  the wordmark height.
- Background-colored gap from **81.5% to 85.6%** (≈4% of wordmark height).
- Earth ochre `#C98A12` from **85.6%** to the baseline — a thin footing.

Percentages are measured on the inked wordmark bounding box, ascender of "l"
included. Word recognition relies on the upper half of letterforms, so the
intact top 81.5% keeps the mark instantly legible; the ochre band below the
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
