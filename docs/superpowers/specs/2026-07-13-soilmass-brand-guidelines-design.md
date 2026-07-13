# soilmass brand guidelines — design spec

Date: 2026-07-13
Status: approved by Edison (visual companion session, all decisions validated interactively)
Revision 2 (2026-07-13, later session): concept pivot — "curated from the
deepest levels", tagline "The web, unearthed.", imagery register changed to
excavation/curation, sections 13–14 added. The implementation in
`guidelines/` and `index.html` predates this revision and is being rebuilt;
where they disagree, this spec governs.

## 1. Purpose & scope

Create the official brand guidelines for **soilmass**, a web agency. This is a
documentation project — a brand identity spec, **not** a code component
library. The identity is built from scratch; nothing pre-exists except the
name.

**Brand concept (rev 2):** "Curated from the deepest levels." soilmass digs —
through a client's business, users, and story — until it hits what nobody
else finds, then surfaces it, curated. Three layers, all load-bearing:
discovery that excavates the client's essence; craft selected from the
deepest level of care; presentation with a curator's register. Swiss
International Typographic Style remains the visual backbone (strict grid,
large confident type, generous whitespace), with excavation motifs — strata,
core samples, specimen plates, depth datums, catalogue annotations — as the
signature details. The visuals are rigorous and precise; the written voice is
deliberately warm and consultative. That contrast is intentional and must be
preserved.

**Audience:** broad — the brand must read as competence to both technical and
non-technical clients.

## 2. Deliverables

All inside `/home/edo/Public/soilmass/design-system` (git repo, initialized
with this spec):

```
guidelines/            # canonical, editable source of truth (markdown)
  00-overview.md       # brand concept, personality, tagline
  01-logo.md
  02-color.md
  03-typography.md
  04-layout-and-devices.md
  05-imagery-and-iconography.md
  06-voice-and-tone.md
  07-applications.md
assets/
  logo-light.svg       # two-tone wordmark for light backgrounds
  logo-dark.svg        # two-tone wordmark for dark backgrounds
  logo-mono.svg        # single-color fallback (gap retained)
  wordmark-small.svg   # solid "soilmass." small-size fallback
  favicon.svg          # ink tile with grade-gap "s"
index.html             # the styled guidelines page — the brand's first application
```

The markdown files are canonical: when guidelines change, edit markdown first,
then mirror into `index.html`. `index.html` presents the same content *styled
in the brand it documents* — it is simultaneously documentation and the proof
of the system.

## 3. Logo

**Primary mark — "grade-gap" wordmark.** Lowercase `soilmass` set in Archivo
Black (900), letter-spacing −0.03em. A horizontal "grade line" of background
color cuts through the letterforms:

- Ink (or paper, on dark) from the top of the letters down to **81.5%** of the
  wordmark height.
- A background-colored gap from **81.5% to 85.6%** (≈4% of wordmark height;
  equals 3% of the em).
- Earth ochre `#C98A12` from **85.6%** to the baseline — a thin footing of
  roughly 18% of the x-height letters' body.

All percentages are measured on the inked wordmark bounding box, ascender of
"l" included. (Derivation: the approved mockups cut at 71–74% of the CSS em
box; with Archivo's metrics — upm 1000, hhea ascent 878/descent 210 — that
grade line sits 124–94 font units above the baseline, which is 81.5–85.6% of
the inked bounding box. The favicon "s" tile uses 74.5–81.5% of the s-glyph
bounding box: same line, gap widened to ~7%.) (The ochre band on paper sits below AA contrast; that is
acceptable — logotypes are exempt under WCAG 1.4.3.)

Rationale (validated visually): word recognition relies on the upper half of
letterforms; keeping the top ~70% in a single dark color preserves full
legibility while the ochre band carries the "grounded / below grade" concept.

**Variants and size rules:**

| Context | Mark |
|---|---|
| ≥ 26 px tall | Two-tone grade-gap wordmark (light or dark version) |
| < 26 px tall | Solid fallback: single-color `soilmass` + ochre full stop (`soilmass.`) |
| Favicon / avatar | Dedicated tile: ink square, grade-gap lowercase "s" (paper + ochre). The tile's gap is optically enlarged to ~7% of the glyph height so it survives 16px rendering |
| Single-color reproduction | `logo-mono.svg`: one color, the 3% gap retained (the gap alone carries the concept) |

**Rules:**
- Clear space: ½ of the wordmark height on all sides, minimum.
- Never: recolor, rotate, add effects (shadows, gradients, outlines), place
  the two-tone mark on busy or low-contrast backgrounds, or stretch.
- SVG files must render correctly without the viewer having Archivo installed
  (text converted to outlines, or font subset embedded in the SVG).

## 4. Color

Warm stone neutrals + a single ochre accent. All values final:

**Neutrals**

| Token | Hex | Use |
|---|---|---|
| paper | `#FAF9F6` | default background |
| stone-100 | `#F0EEE8` | subtle panels, alternate sections |
| stone-200 | `#E8E5DE` | borders, dividers |
| stone-300 | `#D8D4CC` | disabled, faint rules |
| stone-400 | `#A8A29A` | placeholder, faint text on dark |
| stone-500 | `#78736A` | secondary text at large sizes only (4.47:1 — below AA-normal) |
| stone-600 | `#59544B` | secondary text, captions |
| ink | `#191714` | primary text, dark backgrounds |

**Ochre**

| Token | Hex | Use |
|---|---|---|
| ochre-100 | `#F7EBD3` | tint backgrounds, highlights |
| ochre-500 | `#C98A12` | graphic devices, logo band, fills, type on dark backgrounds only |
| ochre-600 | `#8F620B` | all ochre text on paper, any size (5.09:1, AA) |

**Rules:**
- Ochre is punctuation, never flood — one ochre moment per composition.
- Body text on paper is ink or stone-600 only.
- Ochre **text** on paper always uses ochre-600, at every size — ochre-500 on
  paper is 2.80:1 and fails AA even for large type. Ochre-500 type is allowed
  only on ink/dark backgrounds (6.07:1).
- Text on ochre-500 fills (buttons, highlights) is always ink (6.07:1) —
  never paper (2.80:1). Paper text is allowed on ochre-600 fills (5.09:1).
- No other hues. No pure white `#FFFFFF` or pure black `#000000`.

## 5. Typography

Fonts: **Archivo** (400 / 600 / 900) and **JetBrains Mono** (400 / 600), via
Google Fonts in `index.html`.

| Style | Size/leading (px, desktop) | Face | Notes |
|---|---|---|---|
| Display | 64 / 68 | Archivo 900 | −0.03em tracking |
| H1 | 40 / 44 | Archivo 900 | −0.02em |
| H2 | 28 / 34 | Archivo 600 | |
| H3 | 20 / 28 | Archivo 600 | |
| Body | 16 / 26 | Archivo 400 | max measure 70 characters |
| Small | 14 / 22 | Archivo 400 | stone-600 |
| Label | 12 / 16 | JetBrains Mono 400 | UPPERCASE, +0.12em; figures, captions, annotations |

Mobile: Display and H1 scale down fluidly (e.g. `clamp()`); scale below H2 is
unchanged. Labels ("FIG. 01 — …") are the mono voice of the brand and appear
wherever something is measured, numbered, or annotated.

## 6. Layout & graphic devices

- Spacing: 8px base — allowed steps 4, 8, 16, 24, 32, 48, 64, 96, 128.
- Grid: 12 columns, 1200px max content width, 24px gutters.
- **Square corners everywhere. No border radius, ever.**
- Signature devices (specified with exact construction in the guidelines):
  1. **Ground symbol** — 3px ink horizontal rule with 135° ochre hatching
     below (hatch: 2px lines, 4px gaps, ochre-500 at ~55% opacity).
  2. **Strata bars** — three left-aligned bars of increasing weight
     (5 / 8 / 12px), top bar ochre, lower bars ink.
  3. **Dimension callout** — end ticks + rule + centered mono label
     (ochre-600), used to annotate measurements.
  4. **Grid paper** — faint square grid background (ink at 8% opacity,
     24px cell) for diagram areas.

## 7. Imagery & iconography

**Graphic-first: no photography by default.** Visual interest comes from
drawn vector artwork in the excavation register.

**Primary graphic language (rev 2, directional — Edison has marked this
"still up in the air"; revisit before final art):** the **specimen plate** —
a single find (faceted ochre fragment or equivalent) presented like a plate
in an archaeology monograph: hairline double frame, ochre corner ticks,
centered subject, mono catalogue caption ("PLATE VII — FINDING Nº 3 ·
SURFACED FROM −42.0 M"). Case studies present each project as the next plate
in the catalogue. Sanctioned secondary moves: the core-sample column
(strata bands with the deepest band solid ochre, labeled as the find) and
the dashed ochre leader line that carries a find from depth to the surface.

**Photo escape hatch:** when a real photo is unavoidable (team headshots,
client work screenshots), apply the ochre duotone treatment — grayscale,
slight contrast boost, multiplied over ochre-500 — so any source photo becomes
on-brand. Screenshots of client work may alternatively be shown unfiltered
inside an ink browser-chrome frame.

**Icons:** geometric line style, 2px stroke, square terminals and joins, drawn
on a 24px grid, ink by default; a single element per icon may be ochre.

## 8. Voice & tone

**Warm & consultative** — a deliberate counterweight to the precise visuals.

- **Tagline (rev 2):** `The web, unearthed.` (replaces "Solid ground for the
  web."; the old line must not appear in rebuilt materials)
- Principles:
  1. Explain like a trusted engineer-neighbor.
  2. Precision earns warmth — show numbers when we have them.
  3. "You" before "we".
  4. No jargon without a plain-words translation.
- The guidelines include ✓/✗ example pairs (e.g. ✓ "We'll walk you through
  every layer of the build — and show you the numbers behind each decision."
  ✗ "We leverage cutting-edge synergies to deliver best-in-class digital
  experiences at scale.").

## 9. Applications (shown in index.html)

Four styled examples, each built with the real tokens:

1. **Website hero** — display type, tagline, ground symbol, one ochre CTA
   (ink text on ochre-500 fill, per the color rules).
2. **Business card** — front: two-tone wordmark; back: mono contact block on ink.
3. **Email signature** — HTML-safe: solid fallback wordmark, mono labels.
4. **Social banner** — dark, strata bars, tagline.

## 10. index.html requirements

- Single self-contained page: all CSS inline in the file; fonts from Google
  Fonts (the only external dependency); logo SVGs may be inlined.
- Fixed brand colors (paper background) — not OS-theme-aware; the brand book
  defines its own canvas.
- Nav/table of contents mirroring the eight guideline sections.
- Body text passes WCAG AA against its background throughout.
- Responsive to ~360px wide; no horizontal page scroll.

## 11. Out of scope

- No React/Vue/etc. component library, no npm package, no design tokens
  pipeline (JSON/Style Dictionary) — may come later as separate projects.
- No print PDF version.
- No website for soilmass itself — only the hero *example* in applications.

## 12. Success criteria

1. `guidelines/*.md` cover all sections with final values from this spec.
2. `index.html` opens in a browser and presents every section styled in-brand,
   including the four application examples.
3. Logo SVGs render correctly with fonts unavailable (outlines/embedded).
4. The two-tone wordmark, fallback, and favicon follow the size rules above.
5. All body-size text in `index.html` passes AA contrast.
6. (rev 2) No rebuilt material carries the old tagline or construction-era
   imagery; sections 13–14 are documented in the guidelines and demonstrated
   in `index.html`.

## 13. Composition & craft (added rev 2)

Rules that govern every layout, not just heroes. Approved interactively:

1. **Measure is law.** Display lines carry at most three words, broken
   editorially and balanced. Ledes run 45–55 characters. Nothing runs
   wall-to-wall.
2. **One graphic anchor per composition.** A drawn plate, a core sample, a
   strata field, or annotated type — type alone is forbidden.
3. **The annotation layer.** Every composition carries at least one mono
   annotation that measures something real (a span, a depth, a catalogue
   number).
4. **Asymmetry.** Compose on the 12-column grid with deliberate offset; two
   equal columns side-by-side are forbidden.
5. **Rhythm.** Adjacent sections alternate canvases (paper / stone-100 /
   ink); scale contrast of at least 4× between display and mono type is the
   aesthetic engine.
6. **Graphics are drawings, not decorations.** Every brand graphic is vector
   linework following drafting conventions (line weights 0.75 / 1.5 / 2.5,
   standard hatches, catalogue annotations) — never abstract filler shapes.

## 14. Motion & scrollytelling (added rev 2)

Scrollytelling is a brand primitive from day one. A working prototype was
validated in the visual companion session.

1. **Scroll is depth.** Pages descend: the further you scroll, the deeper
   below grade you are. Scroll progress may render as a depth datum.
2. **The canonical narrative is the dig (rev 2): descend → find → surface,
   curated.** Scroll stories assemble drawings in that order, max four beats.
3. **Drawings assemble, they don't animate.** Linework draws in, hatches
   fill, annotations arrive with their data. No bouncing, no parallax
   textures, no easing theatrics.
4. **Native scroll only.** Never hijack the wheel; sticky stages with normal
   scrolling. A beat must also read as a still.
5. **Reduced motion = the finished drawing.** With
   `prefers-reduced-motion`, every narrative shows its final state, static.
   Content never depends on motion.
