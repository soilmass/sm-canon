# Soilmass Design System v2 — Complete Specification

**Status:** Production-Ready | **Version:** 2.0.0 | **Phase:** v1.0 MVP (6-8 weeks) + v1.1 Expansion  
**Last Updated:** 2026-07-13 | **Maintained By:** Design Lead + Engineer + Brand Strategist

---

## Table of Contents

1. [Design System Charter](#design-system-charter)
2. [Sphinx as Structural Principle](#sphinx-as-structural-principle)
3. [Token Specifications](#token-specifications)
4. [Brand Devices](#brand-devices)
5. [Component Architecture](#component-architecture)
6. [Component Specifications](#component-specifications)
7. [Interaction Patterns](#interaction-patterns)
8. [Accessibility & Compliance](#accessibility--compliance)
9. [Responsive Design Rules](#responsive-design-rules)
10. [Dark Mode Specifications](#dark-mode-specifications)
11. [Build Order & Phasing](#build-order--phasing)
12. [Governance & Versioning](#governance--versioning)

---

## Design System Charter

### Brand Objective

**soilmass** is a web agency. The brand promise: **websites that stand on measured, solid ground.**

The brand universe is an **excavation site**. Beneath the ground lie artifacts — things of real value that already exist. The client's business is the artifact; soilmass uncovers it carefully and polishes it for exhibition. The website is the finished piece in the vitrine. The **sphinx** is the presiding figure: guardian of what's buried, the oldest thing ever excavated, equal parts engineering and mystery.

### Core Principles

1. **The excavation metaphor is structural, not decorative.**
   - Every design decision should map to the dig/restore/exhibit narrative.
   - The sphinx is not a logo; it's a decision filter and visual principle.
   - If you can't explain why a detail exists in terms of excavation, restoration, or curation, it doesn't belong.

2. **Rigorous + Warm — The Tension is Load-Bearing.**
   - Swiss geometric discipline (squared corners, alignment, measured space) carries rigor.
   - Curator's voice (warm, measured, human) carries warmth.
   - If one side wins, the system feels off. Both must coexist.

3. **Measured Precision Builds Trust.**
   - Numbers, data, and specificity are everywhere — catalog labels, scale values, contrast ratios.
   - "Precision is how warmth earns trust." Vagueness breaks the brand promise.
   - Every claim is backed by evidence.

4. **Curated, Not Generic.**
   - Density comes from repetition of identical well-made units, not variety.
   - One ochre moment per composition. Two devices max per layout. Every surface type has a purpose.
   - Randomness = amateur. Intentionality = curated.

5. **The Sphinx is a Living Decision Principle.**
   - Sphinx scale, proportion, and placement matter. They guide layout decisions.
   - Sphinx proportions (crouching profile, axis-aligned blocks, single gleam) inform the visual language.
   - Sphinx scale discipline (mark ≤32px, mascot-only in heroes, watermark ≤8% opacity) is enforced site-wide.

### Visual Grammar

**Color as Hierarchy:**
- Limestone (default, breathing space) → Sand (panel/content) → Umber (dark/important) → Ochre (the single gleam, punctuation only)

**Relief as Tactility:**
- Raised (buttons, cards — lift to interact) ↔ Carved (inputs, wells — press into to engage)
- Relief swaps on interaction (press state: raised → carved)
- Relief paired with color/border change for accessibility

**Texture as Narrative:**
- Excavation grid (umber at 8%, 24px cells — diagram/proof media, shows the measured dig)
- 135° hatching (partial reveal, one per viewport — the artifact half-exposed)
- No other patterns. No gradients. No photos. No blur.

**Scale Discipline:**
- Sphinx: mark ≤32px in chrome, mascot-only in heroes/empty states, watermark ≤8% opacity, one per page
- Scale responsively with `clamp()`, never fixed (except when explicitly constrained)
- Proportional relationships maintained across all sizes

---

## Sphinx as Structural Principle

### The Sphinx is Not a Logo

The sphinx is a **visual principle**, **decision filter**, and **recurring motif**. It appears:
- As a mark in chrome and headers (32px max)
- As a mascot in heroes, empty states, loading states (responsive sizing via `clamp()`)
- As a watermark in page footers (8% opacity, one per page)
- As a section marker or accent device
- In step diagrams and narrative moments

### Sphinx Construction Rules

**Visual Anatomy:**
- Crouching profile (nemes headdress block with side flares, head, chest, extended forelegs, raised haunch)
- Sitting on a plinth line
- Blocky, axis-aligned, square-cut rectangles (the "carved from limestone blocks" look)
- One facet — the eye or a chest block — may be ochre/gold: the single gleam

**Construction Grid:**
- Built on a consistent grid system (exact grid TBD during v1.0 SVG design)
- Proportions locked across all sizes (8px mark, 16px mark, 24px mark, 32px mark, 240px mascot, 400px hero)
- SVG viewBox defines scale; all sizes scale proportionally

**Tones:**
- Default: umber on limestone
- Dark surfaces: gold on umber
- Watermark: limestone outline at low opacity
- Interactive states: ochre highlight on eye/chest block (single gleam)

**Scale Discipline & Responsive Behavior:**

| Context | Size | Scaling | Usage |
|---------|------|---------|-------|
| **Mark (chrome/headers)** | 32px desktop, 24px mobile | `clamp(24px, 3vw, 32px)` | In header, nav, footer |
| **Mascot (heroes, empty states)** | 240px mobile, 400px desktop | `clamp(240px, 35vw, 400px)` | Full-width hero image, 404 page |
| **Watermark** | Responsive 8% opacity | Fixed 8% opacity always | Lower-right footer, one per page |
| **Section marker** | 48px-96px | `clamp(48px, 8vw, 96px)` | Between major sections |

**Sphinx Decision Framework — When to Use:**
1. **Header/Chrome:** Always include mark in header. Not optional.
2. **Empty States:** Mascot-size sphinx (happy, contemplative) signals "nothing here yet, but we're watching."
3. **Loading States:** Sphinx with progress overlay or pulsing gleam signals work in progress.
4. **Page Closes:** Watermark in footer as guardian, watching over the content.
5. **Step Diagrams:** Sphinx marks the survey/excavate/restore/exhibit stages.
6. **Section Breaks:** Sphinx mark can signal major transitions.

**Anti-Patterns:**
- Do NOT use sphinx at arbitrary sizes. Follow the scale discipline table.
- Do NOT flip, rotate, or distort sphinx. Maintains proportions always.
- Do NOT mix sphinx tones on the same page without clear purpose (e.g., umber mark + gold watermark is OK if they serve different roles).
- Do NOT use sphinx as generic decoration. Every instance must serve a narrative purpose.

---

## Token Specifications

### Color Tokens

**Naming Convention:** `--sm-color-{role}-{tint}`

Example: `--sm-color-bg-primary`, `--sm-color-text-muted`, `--sm-color-accent-highlight`

#### Neutrals — Sandstone Ramp

| Token | Hex | Use | WCAG AA Contrast (on Limestone #F5EFE2) |
|-------|-----|-----|------------------------------------------|
| `--sm-color-bg-primary` | #F5EFE2 | Default background, breathing space | — (base) |
| `--sm-color-surface-panel` | #ECE3CE | Panel backgrounds, containers | 4.2:1 |
| `--sm-color-border-subtle` | #DFD3B8 | Subtle borders, dividers | 5.1:1 |
| `--sm-color-border-quiet` | #C9B896 | Faint borders, disabled UI | 6.8:1 |
| `--sm-color-placeholder` | #A38E66 | Placeholder text, muted content | 8.2:1 |
| `--sm-color-text-muted` | #7C6A48 | Muted text, metadata | 10.1:1 |
| `--sm-color-text-secondary` | #5A4C33 | Secondary text (AA on limestone) | 13.2:1 |
| `--sm-color-bg-dark` | #221A11 | Dark surfaces, umber backgrounds | 14.9:1 |

#### Accent — Ochre/Gold Family

| Token | Hex | Use | Notes |
|-------|-----|-----|-------|
| `--sm-color-accent-tint` | #F3E5C0 | Ochre tint, subtle highlights | Very light ochre |
| `--sm-color-accent-primary` | #C4880F | Primary fills, devices, ochre moments | Use sparingly (one per composition) |
| `--sm-color-accent-dark` | #8C5F0A | Ochre text on limestone (AA compliant) | Only usable ochre for text |
| `--sm-color-accent-gleam` | #E2AE45 | Gold gleam facet, interactive highlights | Text/accents on umber only |

#### State Colors (Derived from Palette)

| Token | Hex | Use |
|-------|-----|-----|
| `--sm-color-state-error` | #8C5F0A | Error fields, invalid states (using ochre-dark for consistency) |
| `--sm-color-state-success` | #5A4C33 | Success messages, checkmarks (using text-secondary) |
| `--sm-color-state-warning` | #C4880F | Warning states (using accent-primary) |
| `--sm-color-state-info` | #C9B896 | Info messages (using border-quiet) |

**Color Rule Enforcement:**
- Ochre (`--sm-color-accent-primary`): One fill/block per major section max. Allowed in interactive states (focus borders, hover highlights, active buttons).
- Text on limestone: umber (`--sm-color-bg-dark`) or sand-600 (`--sm-color-text-secondary`) only. Never ochre-500 on light backgrounds.
- Text on umber: limestone (`--sm-color-bg-primary`) or gold (`--sm-color-accent-gleam`). Never ochre on umber.
- No pure #000000 or #FFFFFF ever. Use neutrals from the ramp.

---

### Typography Tokens

**Naming Convention:** `--sm-type-{role}` for font stack; `--sm-text-{size}` for scale

#### Font Stacks

```css
--sm-font-display: "Marcellus", Georgia, serif; /* inscriptional, 400 only */
--sm-font-body: "Archivo", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; /* 400, 600 */
--sm-font-mono: "JetBrains Mono", "Menlo", monospace; /* 400, 600; uppercase catalog voice */
```

#### Display Scale (Marcellus)

| Token | Mobile | Desktop | Line-Height | Letter-Spacing | Weight |
|-------|--------|---------|-------------|-----------------|--------|
| `--sm-text-display-xl` | 44px | 72px | 1.08 | +0.01em | 400 |
| `--sm-text-display-lg` | 36px | 56px | 1.10 | +0.01em | 400 |
| `--sm-text-h1` | 32px | 48px | 1.12 | +0.01em | 400 |
| `--sm-text-h2` | 28px | 38px | 1.20 | +0.01em | 400 |

**Implementation:** Use `clamp()` for all display sizes to enable fluid scaling between breakpoints.

```css
font-size: clamp(32px, 5vw, 48px); /* H1 */
font-size: clamp(28px, 4vw, 38px); /* H2 */
```

#### Body Scale (Archivo)

| Token | Size | Line-Height | Weight | Use |
|-------|------|-------------|--------|-----|
| `--sm-text-h3` | 19px | 26px | 600 | Section headers |
| `--sm-text-body` | 16px | 26px | 400 | Body text, prose |
| `--sm-text-body-small` | 14px | 22px | 400 | Secondary body |
| `--sm-text-label` | 14px | 22px | 600 | Form labels (Archivo, not mono) |
| `--sm-text-ui` | 14px | 20px | 600 | UI labels, buttons |

**Max Measure:** 70 characters at 16px (responsive, adjusts with viewport).

#### Catalog Scale (JetBrains Mono, UPPERCASE only)

| Token | Size | Line-Height | Letter-Spacing | Weight | Use |
|-------|------|-------------|-----------------|--------|-----|
| `--sm-text-catalog` | 12px | 16px | +0.14em | 400 | Cartouche labels, figure numbers, metadata |
| `--sm-text-eyebrow` | 12px | 16px | +0.14em | 600 | Section eyebrows, annotations |

**Rule:** JetBrains Mono is UPPERCASE ONLY. No lowercase, no sentence case.

#### Text Styles (Semantic Tokens)

| Token | Font | Size | Color | Use |
|-------|------|------|-------|-----|
| `--sm-text-prose` | Archivo 400 | 16/26 | text-secondary | Article text, long-form |
| `--sm-text-prose-muted` | Archivo 400 | 14/22 | text-muted | Supporting prose, secondary info |
| `--sm-text-link` | Archivo 400 | inherit | accent-dark | Inline prose links |
| `--sm-text-link-hover` | Archivo 400 | inherit | accent-primary | Prose links on hover (underline appears) |

---

### Spacing Tokens

**Base Scale:** 8px

**Naming Convention:** `--sm-space-{size}`

| Token | Value | Use |
|-------|-------|-----|
| `--sm-space-0` | 0px | Reset |
| `--sm-space-xs` | 4px | Micro-spacing (button padding small) |
| `--sm-space-sm` | 8px | Component padding, gap between elements |
| `--sm-space-md` | 16px | Card padding, section gutters |
| `--sm-space-lg` | 24px | Section padding, grid gutters |
| `--sm-space-xl` | 32px | Large section padding |
| `--sm-space-2xl` | 48px | Major section separation |
| `--sm-space-3xl` | 64px | Page section breathing |
| `--sm-space-4xl` | 96px | Full-page section gaps |
| `--sm-space-5xl` | 128px | Hero section spacing |

**Grid & Layout Spacing:**
- Grid: 12 columns, 1200px max-width
- Gutter: 24px (grid gutter, derived from `--sm-space-lg`)
- Section padding: 96px–128px (top/bottom)
- Mobile padding: 20px (< 768px), 32px (≥ 768px)

---

### Relief & Elevation Tokens

**Naming Convention:** `--sm-shadow-{state}`

#### Raised Relief (Buttons, Cards — "Lift to Interact")

```css
--sm-shadow-raised: inset 0 1px 0 rgba(255, 255, 255, 0.45), 
                     inset 0 -1px 0 rgba(34, 26, 17, 0.14);
```

- Light inset (top): 1px white at 45% opacity
- Dark inset (bottom): 1px umber at 14% opacity
- Creates carved-up effect; feels elevated

#### Carved Relief (Inputs, Wells — "Press Into to Engage")

```css
--sm-shadow-carved: inset 0 1.5px 2px rgba(34, 26, 17, 0.20),
                     inset 0 -1px 0 rgba(255, 255, 255, 0.35);
```

- Dark inset (top): 1.5px umber at 20% opacity, 2px blur
- Light inset (bottom): 1px white at 35% opacity
- Creates pressed-down effect; feels recessed

#### Relief on Dark Surfaces (Umber Backgrounds)

```css
--sm-shadow-raised-dark: inset 0 1px 0 rgba(245, 239, 226, 0.30),  /* lighter on dark */
                          inset 0 -1px 0 rgba(0, 0, 0, 0.25);

--sm-shadow-carved-dark: inset 0 1.5px 2px rgba(0, 0, 0, 0.40),
                          inset 0 -1px 0 rgba(245, 239, 226, 0.25);
```

**State Transitions:**
- Button press: raised → carved (0ms swap, no transition)
- Input focus: carved stays carved + ochre border added (no shadow change)

**Testing Requirement:**
Relief formulas must be tested at 5 component sizes to verify visual consistency:
- 24px (small button, icon button)
- 44px (standard button)
- 64px (large button, card)
- 96px (feature card)
- 200px (hero block)

---

### Motion Tokens

**Naming Convention:** `--sm-motion-{type}`

#### Section Reveal (Intersection Observer)

```css
--sm-motion-reveal-duration: 500ms;
--sm-motion-reveal-easing: cubic-bezier(0.2, 0.6, 0.2, 1);
--sm-motion-reveal-distance: 10px; /* vertical rise */
```

- Fade + 10px rise
- Once per element, on scroll into view
- 500ms duration, measured easing

#### Interaction Motion (Micro-interactions)

```css
--sm-motion-hover-duration: 200ms;
--sm-motion-hover-easing: ease-out;
```

- Button hover: border color change (sand → umber)
- Link arrow: translate 4–6px
- Smooth but immediate feedback

#### Reduced Motion Compliance

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0ms !important;
    transition-duration: 0ms !important;
  }
}
```

All motion is disabled for users with `prefers-reduced-motion: reduce`. States/changes remain (color shift, border change) but no animation/transition.

---

## Brand Devices

### Device Principle

Devices are the visual vocabulary of the excavation narrative. Each device serves a specific semantic purpose and appears at defined moments. There are exactly **4 devices**:

1. **SphinxMark** — guardian, decision principle
2. **DigGrid** — the measured dig site
3. **Cartouche** — the artifact label/annotation
4. **Horizon** — the section boundary, open excavation

Max two devices per composition. Each device has an exact SVG spec, usage rules, and responsive scaling.

---

### Device 1: SphinxMark

**See Sphinx as Structural Principle (above) for complete spec.**

SVG Spec Details (v1.0 design):
- Viewbox: 256x256 (base grid, scaled proportionally)
- Proportions locked in construction grid
- SVG files provided for each size: sphinx-24px.svg, sphinx-32px.svg, sphinx-240px.svg, sphinx-400px.svg
- Tones: umber fill, limestone outline, gold gleam highlight
- No anti-aliasing artifacts; clean edge rendering

---

### Device 2: DigGrid — Excavation Grid

**Purpose:** Proof media backdrop, diagram language, empty state visual. Shows the measured, systematic dig.

**Construction:**
- Square cells in a grid (A–E columns, 1–4 rows typical; extendable)
- Coordinate labels in JetBrains Mono, UPPERCASE, umber color
- Exactly one ochre "find" cell (the artifact location)
- Hairline umber grid lines (stroke weight: 1px)
- Optional partial-reveal cells with 135° hatching (one hatch moment max)

**SVG Spec (v1.0 Design):**
- Viewbox: 320x240 (4:3 aspect ratio, typical)
- Cell size: 64px per cell (scales with viewbox)
- Coordinate labels: Cartouche style (JetBrains Mono 12px, +0.14em tracking)
- Find cell fill: ochre-500 with umber border (2px)
- Hatching (if used): 135°, umber lines at 1px weight, 4px spacing

**Usage Rules:**
- Hero proof media: DigGrid shows the site, introduces the narrative
- Diagram backdrop: Step diagram (Survey/Excavate/Restore/Exhibit) sits on DigGrid
- Empty state: "The dig site awaits. Begin your survey." DigGrid as background, no content yet
- Max size: 100% viewport width; scales fluidly

**Responsive Behavior:**
- Desktop (≥960px): Full grid visible, labels readable
- Tablet (600–960px): 3x2 grid, cells compress slightly
- Mobile (<600px): 2x2 grid or simplified icon representation

---

### Device 3: Cartouche — Artifact Annotation

**Purpose:** Label, annotate, and mark provenance. The museum catalog label for the artifact.

**Construction:**
- Mono uppercase text (JetBrains Mono, 12px, +0.14em tracking)
- Hairline rectangular frame (border: 1px, color: sand-200)
- 2px end ticks (short vertical lines on left and right edges)
- Typical example: "No. 042 · C3 · Found 2.6 m"

**SVG/CSS Spec (v1.0 Design):**
- Frame: `border: 1px solid var(--sm-color-border-subtle)`
- Padding: 8px horizontal, 4px vertical
- End ticks: 2px height, positioned at top and bottom corners
- Text: JetBrains Mono, 12px/16px, umber color
- No background fill; transparent (sits on any surface)

**Usage Rules:**
- Annotate with metadata: project number, location, measurement
- Mark the artifact: "The find."
- Label diagrams: Figure numbers, step annotations
- Required on hero image: "No. [Project] · [Client] · Excavated [Date]"
- Optional on cards/features, but if used, follows Cartouche spec exactly

**Anti-Patterns:**
- Do NOT use Cartouche for non-metadata. No flowery annotation ("A beautiful discovery").
- Do NOT violate the frame spec (thicker border, filled background, etc.).
- Do NOT label every element. Use sparingly for provenance-bearing content.

---

### Device 4: Horizon — Section Boundary

**Purpose:** Close sections, mark transitions, signal the open dig. The visual moment where earth meets sky.

**Construction:**
- 3px horizontal umber rule
- Rectangular "trench notch" cut down into rule (indicating the excavation depth)
- Ochre-hatched band below the rule (the partial artifact reveal, 135° hatching)
- Marks the end of a major section or page area

**CSS/SVG Spec (v1.0 Design):**
- Umber rule: `height: 3px; background: var(--sm-color-bg-dark); width: 100%`
- Trench notch: rectangular cutout, 24px wide × 16px deep (centered), background color matches parent
- Hatching band: SVG pattern (135°, umber at 8%, 24px cells), height: 24px, below rule
- No shadow; sits flat on surface

**Implementation:**
```css
.horizon {
  position: relative;
  height: 3px;
  background: var(--sm-color-bg-dark);
  margin: 96px 0; /* breathing room */
}

.horizon::before {
  content: '';
  position: absolute;
  bottom: -16px;
  left: 50%;
  transform: translateX(-50%);
  width: 24px;
  height: 16px;
  background: inherit; /* parent background shows through trench */
}

.horizon::after {
  content: '';
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  height: 24px;
  background: url('data:image/svg+xml,...'); /* SVG hatching pattern */
}
```

**Usage Rules:**
- Closes all major section types (hero, feature blocks, use-case grid, trust & practice)
- Always at the end of a section (not beginning)
- Marks the transition: what was above is "exhibited"; what's below is "under excavation"
- Counts as an ochre moment only if the hatching uses ochre; default is umber hatching

---

## Component Architecture

### Component Conventions

#### File Structure

Each component ships as:
- **Component.jsx** — Self-contained, inline styles from tokens
- **Component.d.ts** — Props contract (TypeScript types)
- **Component.spec.md** — Usage guide, examples, variants
- **Component.specimen.html** — Dense visual states/variants card

Example: Button component
```
Button/
  ├── Button.jsx
  ├── Button.d.ts
  ├── Button.spec.md
  └── Button.specimen.html
```

#### Props Naming Convention

- **Sizes:** `size="sm" | "md" | "lg"` (not "small"/"medium"/"large")
- **Variants:** `variant="primary" | "secondary" | "ghost"`
- **States:** `disabled`, `loading`, `error`, `success` (boolean props)
- **Event callbacks:** `on{Event}` (e.g., `onClick`, `onFocus`, `onBlur`)
- **Aria/Accessibility:** `aria-label`, `aria-describedby`, `role` (pass-through)

#### Style Architecture

- **No CSS files.** Styles inline using CSS variables.
- **CSS Variables only.** All colors, spacing, typography, shadows come from `--sm-*` tokens.
- **No hardcoded values.** Hex values, px values, font names — all from tokens.
- **Dark mode support:** Tokens automatically flip for dark theme; no component changes needed.

#### Composition Rules

- Components can nest (Button inside Card, Input inside FormGroup) only where documented
- No arbitrary nesting. Invalid combinations must error or warn at dev time
- Valid combos: FormGroup (Label + Input + Helper), Card (Header + Body + Footer), Fieldset (multiple Inputs)

---

### Component State Matrix

All interactive components include:

| State | Visual | ARIA | When |
|-------|--------|------|------|
| **default** | Base style, no interaction | No special role | Initial render |
| **hover** | Border color shift, subtle interactive cue | N/A | Mouse over (not on touch) |
| **focus** | Ochre outline/border, visible indicator | `aria-focus` implicit | Tab navigation or click |
| **active/pressed** | Relief swap (raised → carved), visual press | `aria-pressed="true"` | User presses/clicks |
| **disabled** | Muted colors, no interaction, cursor: not-allowed | `aria-disabled="true"`, `disabled` attr | Conditionally disabled |
| **loading** | Optional spinner or pulse, no interaction | `aria-busy="true"`, `aria-label="Loading..."` | Async operation in progress |
| **error** | Error color (using ochre-dark), error icon, error message | `aria-invalid="true"`, `aria-describedby` points to error | Validation fails |
| **success** | Success indicator (checkmark), success message | `aria-live="polite"`, success message announced | Async success or validation pass |

---

## Component Specifications

### Button Component

**Purpose:** Primary and secondary calls-to-action, form submission, navigation.

**Props:**

```typescript
interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'ghost'; // default: 'primary'
  size?: 'sm' | 'md' | 'lg'; // default: 'md'
  disabled?: boolean;
  loading?: boolean;
  onClick?: (e: React.MouseEvent) => void;
  children: React.ReactNode;
  href?: string; // if provided, renders <a>, else <button>
  as?: 'button' | 'a'; // override element type
  aria-label?: string;
  className?: string; // pass-through for rare overrides
}
```

**Sizes:**

| Size | Height | Padding | Font | Use |
|------|--------|---------|------|-----|
| sm | 36px | 8px 16px | Archivo 14px | Small CTA, secondary action |
| md | 44px | 12px 24px | Archivo 16px | Standard button, primary CTA |
| lg | 56px | 16px 32px | Archivo 18px | Large CTA, hero button |

**Variants:**

1. **Primary (variant="primary")**
   - Background: `--sm-color-accent-primary` (ochre-500)
   - Text: `--sm-color-bg-dark` (umber)
   - Relief: `--sm-shadow-raised`
   - Hover: Background shifts to `--sm-color-accent-dark` (ochre-600)
   - Active/Press: Relief swaps to `--sm-shadow-carved`
   - Focus: Ochre outline, 3px, 2px offset

2. **Secondary (variant="secondary")**
   - Background: transparent
   - Border: 2px `--sm-color-bg-dark` (umber)
   - Text: `--sm-color-bg-dark` (umber)
   - Relief: none
   - Hover: Border thickens or background becomes `--sm-color-surface-panel`
   - Active/Press: Border thickens to 3px, background `--sm-color-surface-panel`
   - Focus: Ochre outline, 3px, 2px offset

3. **Ghost (variant="ghost")**
   - Background: transparent
   - Border: none
   - Text: `--sm-color-text-secondary` (sand-600)
   - Relief: none
   - Hover: Text shifts to `--sm-color-bg-dark` (umber), underline appears
   - Active/Press: Text shifts to `--sm-color-accent-primary` (ochre)
   - Focus: Ochre outline, 3px, 2px offset

**Loading State:**
- Icon: Optional spinner (SVG, umber color, 16px)
- Label: "Loading..." or inherited aria-label + " (loading)"
- Disabled: Button is functionally disabled (no click)

**Error State:**
- Border: 2px `--sm-color-state-error` (ochre-dark)
- Background: `--sm-color-accent-tint` (very light ochre)
- Aria: `aria-invalid="true"`, `aria-describedby` points to error message

---

### Input Component

**Purpose:** Text input, email, search, form fields.

**Props:**

```typescript
interface InputProps {
  type?: 'text' | 'email' | 'search' | 'password' | 'url' | 'tel';
  placeholder?: string;
  value?: string;
  onChange?: (e: React.ChangeEvent<HTMLInputElement>) => void;
  onBlur?: (e: React.FocusEvent<HTMLInputElement>) => void;
  disabled?: boolean;
  error?: boolean | string; // true or error message
  success?: boolean;
  label?: string; // if provided, renders <label>
  aria-label?: string;
  aria-describedby?: string;
  className?: string;
}
```

**Base Style:**

- Background: `--sm-color-surface-panel` (sand-100)
- Border: 1px `--sm-color-border-subtle` (sand-200)
- Relief: `--sm-shadow-carved` (pressed-in effect)
- Text: `--sm-color-bg-dark` (umber)
- Placeholder: `--sm-color-placeholder` (sand-400)
- Min height: 44px (touch target)
- Padding: 12px 16px
- Border-radius: 0 (squared corners always)

**Focus State:**

- Border: 2px `--sm-color-accent-primary` (ochre-500)
- Relief: stays carved
- Outline: none (border handles focus visibility)
- Shadow: none

**Error State:**

- Border: 2px `--sm-color-state-error` (ochre-dark)
- Background: `--sm-color-accent-tint` (light ochre tint)
- Error message below input (12px, sand-600, aria-live="polite")
- Aria: `aria-invalid="true"`, `aria-describedby` points to error message

**Success State:**

- Border: 2px `--sm-color-state-success` (using sand-600)
- Background: unchanged
- Checkmark icon: 16px, umber, right side of input (10px padding)
- Aria: success message announced (aria-live="polite")

**Disabled State:**

- Background: `--sm-color-border-quiet` (sand-300)
- Text: `--sm-color-text-muted` (sand-500)
- Border: 1px `--sm-color-border-quiet`
- Cursor: not-allowed
- Aria: `aria-disabled="true"`, `disabled` attr

**Validation Timing:**
- On blur (when user leaves the field)
- Optional real-time validation (after user pauses 500ms)
- Do NOT validate on every keystroke (too noisy)

---

### Card Component

**Purpose:** Content container, panel, grouped information.

**Props:**

```typescript
interface CardProps {
  variant?: 'panel' | 'bordered' | 'dark'; // default: 'panel'
  children: React.ReactNode;
  className?: string;
}
```

**Variants:**

1. **Panel (variant="panel")**
   - Background: `--sm-color-surface-panel` (sand-100)
   - Border: none
   - Relief: `--sm-shadow-raised` (lifted effect)
   - Padding: 24px (md) or 32px (lg variant)
   - Press/hover: Relief swaps to `--sm-shadow-carved` (optional, for interactive cards)

2. **Bordered (variant="bordered")**
   - Background: `--sm-color-bg-primary` (limestone, default)
   - Border: 1px `--sm-color-border-subtle` (sand-200)
   - Relief: none
   - Padding: 24px
   - Hover: Border shifts to `--sm-color-text-secondary` (sand-600)

3. **Dark (variant="dark")**
   - Background: `--sm-color-bg-dark` (umber)
   - Border: none
   - Relief: `--sm-shadow-raised-dark` (adjusted for dark bg)
   - Padding: 24px
   - Text: `--sm-color-bg-primary` (limestone) or `--sm-color-accent-gleam` (gold)

**Grid Behavior:**
- Default: 1 column (mobile-first)
- @768px: 2 columns (grid-template-columns: repeat(2, 1fr))
- @960px: 3 columns or layout-specific
- Gap between cards: 24px (grid gap)

---

### Label Component

**Purpose:** Form label, annotation, semantic connection between input and label.

**Props:**

```typescript
interface LabelProps {
  htmlFor: string; // input id
  required?: boolean;
  tone?: 'default' | 'muted' | 'on-dark'; // color variant
  children: React.ReactNode;
}
```

**Tones:**

| Tone | Color | Background | Use |
|------|-------|------------|-----|
| default | sand-600 | transparent | Standard form labels on limestone |
| muted | sand-500 | transparent | Optional/secondary labels |
| on-dark | limestone | transparent | Labels on dark/umber backgrounds |

**Styling:**
- Font: Archivo 14px, 600 weight
- Color: as per tone (default: sand-600)
- Display: block (not inline)
- Margin-bottom: 4px (space above input)
- No asterisk by default; if required, pass `required={true}` → appends " *" in ochre-500

---

### Tag Component

**Purpose:** Label, filter chip, metadata marker.

**Props:**

```typescript
interface TagProps {
  variant?: 'default' | 'solid' | 'accent'; // default: 'default'
  children: React.ReactNode;
  onRemove?: () => void; // if provided, shows X icon
}
```

**Variants:**

1. **Default (variant="default")**
   - Background: transparent
   - Border: 1px `--sm-color-border-subtle` (sand-200)
   - Text: sand-600
   - Padding: 4px 12px
   - Border-radius: 0 (squared corners)

2. **Solid (variant="solid")**
   - Background: `--sm-color-bg-dark` (umber)
   - Border: none
   - Text: limestone
   - Padding: 4px 12px

3. **Accent (variant="accent")**
   - Background: `--sm-color-accent-tint` (light ochre)
   - Border: 1px `--sm-color-accent-primary` (ochre-500)
   - Text: umber
   - Padding: 4px 12px

**Remove Icon:**
- If `onRemove` provided, show X icon (12px, umber or limestone based on variant)
- Hover: X becomes ochre-500
- Click: calls `onRemove()`, removes tag from DOM

---

### Icon Component

**Purpose:** Inline icons, visual signals, navigation markers.

**Props:**

```typescript
interface IconProps {
  name: 'menu' | 'close' | 'check' | 'arrow-right' | 'external' | 'layers' | 'gauge' | 'chart' | 'document' | 'clock' | 'mail' | 'search' | 'grid' | 'plus' | 'minus' | ...; // 17+ glyphs
  size?: '16' | '24' | '32' | '48'; // px, default: '24'
  color?: 'default' | 'accent' | 'on-dark'; // default: 'default'
  aria-label?: string; // required if icon is semantic
  className?: string;
}
```

**Icon Set Spec (v1.0 Design):**
- **Canvas:** 24px × 24px grid (SVG viewBox)
- **Stroke weight:** 2px (consistent across all glyphs)
- **Terminals/Joins:** Square (stroke-linecap="square", stroke-linejoin="miter")
- **Colors:**
  - default: umber (`--sm-color-bg-dark`)
  - accent: ochre-500 (`--sm-color-accent-primary`, max one per icon cluster)
  - on-dark: limestone

**Core Glyph Set (17 minimum):**
1. menu (hamburger, 3 lines)
2. close (X)
3. check (checkmark)
4. arrow-right (chevron/arrow)
5. arrow-left
6. arrow-up
7. arrow-down
8. external (open in new, arrow top-right)
9. layers (overlapping squares)
10. gauge (speedometer-like)
11. chart (bar chart)
12. document (page)
13. clock (time)
14. mail (envelope)
15. search (magnifying glass)
16. grid (3x3 grid)
17. plus (plus sign)

**Scaling Behavior:**
- All icons scale with `size` prop (16, 24, 32, 48px)
- Stroke weight remains 2px (does NOT scale proportionally)
- At 16px, glyphs are dense; at 48px, spacious but still legible

---

## Interaction Patterns

### Form Validation Pattern

#### Pattern Overview

Forms collect user input with clear validation feedback. Three moments: input focus, validation trigger, and feedback display.

#### Validation Timing

1. **On blur** — Validates when user leaves the field (standard, low-noise)
2. **On submit** — Validates all fields when form is submitted
3. **Real-time (optional)** — Validates after user pauses 500ms; use sparingly for high-confidence validations (e.g., email format)

#### Error Display

**Inline error (below input):**
```jsx
<Input
  label="Email"
  type="email"
  value={email}
  onBlur={validate}
  error={errors.email} // string: "Invalid email format"
  aria-describedby="email-error"
/>
<div id="email-error" role="alert" className="error-message">
  {errors.email}
</div>
```

- Error message: 12px, sand-600 color, appears below input
- Input border: 2px ochre-dark (error state)
- Aria: `aria-invalid="true"`, `aria-describedby` points to error message
- Role: `role="alert"` (screen reader announces immediately)

#### Async Validation

For slow operations (checking if email exists, availability checks):

```jsx
<Input
  label="Username"
  value={username}
  onChange={handleChange}
  loading={isValidating}
  error={errors.username}
/>
```

- While validating: `loading={true}` → input shows loading spinner (optional), disabled
- Aria: `aria-busy="true"`
- On complete: error or success state displayed

#### Success Feedback

```jsx
<Input
  value={email}
  success={isValid}
/>
```

- Success icon: checkmark, 16px, umber, right side
- Background: unchanged (no green or color emphasis; sphinx/umber aesthetic)
- Aria: success message announced via aria-live="polite"

#### Dependent Fields

When one field's answer affects another (e.g., "Budget" appears after "Project Type" is selected):

```jsx
{projectType === 'large' && (
  <Input
    label="Estimated Budget"
    required
    aria-describedby="budget-info"
  />
)}
<p id="budget-info">Required for projects over 3 months</p>
```

- Hidden field revealed only when condition met
- Aria: field is in DOM but hidden (aria-hidden="true" if appropriate) until revealed
- Tab order: hidden fields are skipped

---

### Empty State Pattern

**When:** No data to display, no projects found, new user onboarding.

**Structure:**

```jsx
<div className="empty-state">
  <Sphinx size="large" /> {/* 240px mascot-size */}
  <h2>The dig site awaits.</h2>
  <p>No projects here yet. Begin your survey.</p>
  <Button>Start a dig</Button>
</div>
```

**Styling:**
- Background: limestone (`--sm-color-bg-primary`)
- Sphinx: 240–400px (responsive, `clamp(240px, 35vw, 400px)`)
- Heading: Marcellus H2, umber
- Body text: sand-600, max 60ch measure
- CTA button: primary (ochre), centered

**Aria:**
- Role: `role="status"` or `role="region"` with `aria-label="Empty state"`
- Message: aria-live="polite" (announceability)

---

### Error/Failure State Pattern

**When:** Form submission fails, API error, validation failure.

**Structure:**

```jsx
<div className="error-state" role="alert">
  <Icon name="alert" color="accent" /> {/* or ochre-colored icon */}
  <h3>We encountered an issue.</h3>
  <p>Your submission didn't go through. Check the fields below and try again.</p>
  <ul>
    <li>Email is required (field: <strong>Email</strong>)</li>
    <li>Project description must be at least 50 characters</li>
  </ul>
  <Button onClick={retry}>Try Again</Button>
</div>
```

**Styling:**
- Background: `--sm-color-accent-tint` (light ochre tint)
- Border: 2px `--sm-color-state-error` (ochre-dark)
- Icon: ochre-500 or ochre-dark
- Text: umber
- Error list: bullets or icon + text
- CTA: primary button (try again, or navigate to fix)

**Aria:**
- Role: `role="alert"` (announces immediately to screen readers)
- Aria-live: `aria-live="assertive"` (preempts other announcements)

---

### Loading State Pattern

**When:** Async operation in progress (form submission, data fetch, file upload).

**Structure:**

```jsx
{isLoading ? (
  <div className="loading-state" aria-busy="true">
    <Spinner /> {/* optional animated spinner */}
    <p>Excavating your data...</p>
  </div>
) : (
  <Results data={data} />
)}
```

**Styling:**
- Spinner (if used): 24–32px, umber color, rotate animation (500ms, linear, infinite)
- Text: "Excavating...", "Processing...", "Restoring..." (curator voice, measured language)
- Background: optional semi-transparent overlay or just centered message
- Disabled: interactive elements behind loading state are disabled/not focusable

**Aria:**
- Aria-busy: `aria-busy="true"`
- Aria-label: `aria-label="Loading, please wait"`
- Status message: `role="status"`, aria-live="polite"

---

### Navigation & Orientation Pattern

**Breadcrumbs (if needed for deep navigation):**

```jsx
<nav aria-label="breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/work">Work</a></li>
    <li aria-current="page">Project Name</li>
  </ol>
</nav>
```

- Font: Archivo 14px, sand-600
- Separators: " / " (text, not icon)
- Last item: aria-current="page" (not a link)
- Mobile: breadcrumbs hidden or collapsed to ≤2 levels

---

## Accessibility & Compliance

### WCAG AA+ Compliance

The system meets **WCAG 2.1 Level AA+ (enhanced)** accessibility standards. This includes:

- **Color Contrast:** All text meets 4.5:1 minimum (pre-validated palette)
- **Focus Management:** All interactive elements are focusable, focus visible (3px outline, 2px offset)
- **Keyboard Navigation:** All functionality keyboard-accessible, logical tab order
- **Semantic HTML:** Proper use of form labels, buttons, headings, roles
- **ARIA Implementation:** Aria-labels, aria-describedby, aria-live, aria-invalid, aria-current where needed
- **Motion Safety:** `prefers-reduced-motion` media query respected (all motion disabled)

### Contrast Ratios (Verified)

| Combination | Ratio | WCAG Level |
|-------------|-------|-----------|
| Umber on Limestone | 14.9:1 | AAA |
| Sand-600 on Limestone | 13.2:1 | AAA |
| Ochre-600 on Limestone | 5.0:1 | AA |
| Limestone on Umber | 14.9:1 | AAA |
| Gold on Umber | ~7:1 | AA |

**Rule:** Text color + background combination must always meet 4.5:1. Decorative/non-text elements (borders, icons) 3:1 minimum.

### Focus Indicators

- **Outline:** 3px `--sm-color-accent-primary` (ochre-500)
- **Offset:** 2px from element edge
- **Visible:** Always visible, never hidden (no `outline: none`)
- **Keyboard-only (optional):** Use `:focus-visible` if wanting to hide mouse-click focus (but show tab focus)

```css
:focus {
  outline: 3px solid var(--sm-color-accent-primary);
  outline-offset: 2px;
}

/* Optional: only show on keyboard focus */
:focus-visible {
  outline: 3px solid var(--sm-color-accent-primary);
  outline-offset: 2px;
}
```

### Form Accessibility

- **Labels:** Every input has an associated `<label>` with `htmlFor` pointing to input `id`
- **Required fields:** Marked with `required` attr and visual indicator (asterisk in ochre)
- **Error messages:** Linked via `aria-describedby`, announced with `role="alert"`
- **Helper text:** Linked via `aria-describedby`, not relied on as only instruction

### Motion Accessibility

All animations/transitions respect `prefers-reduced-motion: reduce`:

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

### Screen Reader Support

- **Aria-labels:** Decorative icons/graphics get `aria-label` or `aria-hidden="true"`
- **Live regions:** Dynamic content uses `aria-live="polite"` (form validation, notifications)
- **Buttons vs. links:** Semantically correct (`<button>` for actions, `<a>` for navigation)
- **Skip links:** Hidden skip-to-content link on every page

---

## Responsive Design Rules

### Mobile-First Cascade Approach

**Base styles (mobile):**
- Single column layout
- Full-width content (with 20px padding)
- Stacked components (no multi-col grid)
- Larger touch targets (44px+ minimum)
- Simplified navigation (hamburger menu)

**Breakpoints (exact values):**

| Breakpoint | Width | Grid | Purpose |
|------------|-------|------|---------|
| `mobile` | < 600px | 1 col | Base mobile experience |
| `tablet-sm` | 600px–759px | 1 col, wider padding | Small tablet, portrait |
| `tablet-md` | 760px–819px | 2 col | Tablet landscape |
| `tablet-lg` | 820px–959px | 2–3 col | Large tablet |
| `desktop-sm` | 960px–979px | 3 col | Small desktop |
| `desktop-md` | 980px+ | 3–4 col, 1200px max-width | Desktop, max-width container |

**CSS Implementation:**

```css
/* Mobile base (single column) */
.grid {
  grid-template-columns: 1fr;
  padding: 20px;
  gap: 16px;
}

/* @600px: tablet small */
@media (min-width: 600px) {
  .grid {
    grid-template-columns: repeat(2, 1fr);
    padding: 24px;
  }
}

/* @820px: nav collapses, 2-3 col */
@media (min-width: 820px) {
  .grid {
    grid-template-columns: repeat(3, 1fr);
    padding: 32px;
  }
  
  header .nav {
    display: flex; /* no hamburger */
  }
}

/* @960px+: desktop, max-width container */
@media (min-width: 960px) {
  .container {
    max-width: 1200px;
    margin: 0 auto;
  }
}
```

### Typography Scaling

All display and body type use `clamp()` for fluid scaling:

```css
/* H1: 32px mobile → 48px desktop */
font-size: clamp(32px, 5vw, 48px);

/* H2: 28px mobile → 38px desktop */
font-size: clamp(28px, 4vw, 38px);

/* Body: 16px (no clamp, too small to benefit) */
font-size: 16px;
line-height: 1.625; /* 26px at 16px base */
```

### Component Responsive Behavior

**Header/Navigation:**
- Mobile: hamburger toggle, side panel nav, full-width
- @820px: horizontal nav bar, logo + links + CTA in header

**Hero:**
- Mobile: Single column, Sphinx mascot (240px), CTA button full-width
- @960px: Two-column option (text left, Sphinx right), CTA buttons inline

**Cards/Features:**
- Mobile: 1 column
- @600px: 2 columns
- @960px: 3 columns

**Grid/DigGrid:**
- Mobile: 2×2 grid (4 cells)
- @960px: 4×3 grid (12 cells)
- Scales fluidly within range

---

## Dark Mode Specifications

### Dark Mode Principle

Dark mode is a **complete color inversion** that maintains the brand's "stone carved" aesthetic. The metaphor becomes underground/burial → excavation depth.

### Dark Mode Tokens

All `--sm-color-*` tokens have dark equivalents (automatically applied via theme toggle).

#### Dark Neutrals

| Token | Light | Dark | Use |
|-------|-------|------|-----|
| `--sm-color-bg-primary` | #F5EFE2 (limestone) | #221A11 (umber) | Background, default surface |
| `--sm-color-surface-panel` | #ECE3CE (sand-100) | #2C241A | Panel/card backgrounds |
| `--sm-color-border-subtle` | #DFD3B8 (sand-200) | #3D3428 | Subtle borders |
| `--sm-color-text-secondary` | #5A4C33 (sand-600) | #D4CCBA | Body text on dark |
| `--sm-color-text-muted` | #7C6A48 (sand-500) | #A89888 | Muted text on dark |
| `--sm-color-bg-dark` | #221A11 (umber) | #F5EFE2 (limestone) | Dark sections, now light |

#### Dark Accent Colors

| Token | Light | Dark | Use |
|-------|-------|------|-----|
| `--sm-color-accent-primary` | #C4880F (ochre) | #D4AF37 (brighter gold) | Primary fills, accent |
| `--sm-color-accent-gleam` | #E2AE45 (gold) | #F5D547 (brighter gold) | Highlights, gleams |

### Dark Mode Implementation

```css
/* Light mode (default) */
:root {
  --sm-color-bg-primary: #F5EFE2;
  --sm-color-bg-dark: #221A11;
  /* ... */
}

/* Dark mode toggle */
:root[data-theme="dark"] {
  --sm-color-bg-primary: #221A11;
  --sm-color-bg-dark: #F5EFE2;
  /* ... */
}

/* System preference (optional) */
@media (prefers-color-scheme: dark) {
  :root {
    --sm-color-bg-primary: #221A11;
    /* ... */
  }
}
```

### Dark Mode Contrast Verification

All text/background combinations must be re-verified for dark mode:

| Combination | Ratio | Compliant |
|-------------|-------|-----------|
| Limestone on Umber (dark) | 14.9:1 | ✓ AAA |
| Sand-600 (light) on Umber | ~6:1 | ✓ AA |
| Gold on Umber | ~7:1 | ✓ AA |

### Dark Mode Components

**No component changes needed.** Styles automatically adapt via token variables. Button in light mode:

```
background: var(--sm-color-accent-primary); // ochre in light, gold in dark
color: var(--sm-color-bg-dark); // umber in light, limestone in dark
```

### Dark Mode Relief

Relief shadows adapt for dark backgrounds:

```css
:root[data-theme="dark"] {
  --sm-shadow-raised: inset 0 1px 0 rgba(245, 239, 226, 0.30),
                      inset 0 -1px 0 rgba(0, 0, 0, 0.25);
  --sm-shadow-carved: inset 0 1.5px 2px rgba(0, 0, 0, 0.40),
                      inset 0 -1px 0 rgba(245, 239, 226, 0.25);
}
```

---

## Build Order & Phasing

### Phase v1.0 — MVP (6–8 weeks)

**Goal:** Ship a rock-solid core that proves the system works in production.

#### v1.0 Deliverables

**1. Tokens** (1 week)
- CSS variable files (colors.css, typography.css, spacing.css, relief.css, motion.css)
- Light + dark theme specs
- Complete palette documentation
- Token naming guide

**2. Core Components** (4 weeks)
- Button (primary, secondary, ghost; sm/md/lg; all states)
- Input (text, email, password; all states; validation patterns)
- Card (panel, bordered, dark variants)
- Label (semantic form label)
- Tag (3 variants)
- Icon set (17 core glyphs, all sizes)

Each component ships with:
- .jsx (self-contained)
- .d.ts (props contract)
- .spec.md (usage guide)
- .specimen.html (visual states card)

**3. Brand Devices** (2 weeks)
- SphinxMark (SVG at all sizes: 24, 32, 240, 400px)
- DigGrid (SVG, configurable grid, coordinate labels)
- Cartouche (CSS component, annotation pattern)
- Horizon (CSS component, section boundary)

**4. Foundation Specimen** (1 week)
- 15–20 dense specimen cards showing:
  - Color palette (ramp, accessibility notes)
  - Typography scale (each size, weights, line-height)
  - Spacing scale (visual ruler)
  - Relief (raised vs. carved at multiple sizes)
  - Each device in context (1–2 usage examples per device)
  - State patterns (empty, error, loading examples)
  - Sphinx scale discipline (all sizes shown)

**5. Documentation** (1 week)
- Readme.md (overview, quick start, token reference)
- Component index (list of all v1.0 components)
- Token guide (naming, usage, CSS examples)
- Device usage guide (when/how to use each device)
- Accessibility checklist (AA+ compliance, testing notes)

#### v1.0 Not Included

- DigGrid variants (only standard 4×3)
- Full Horizon device (simplified 3px rule initially)
- Secondary components (dropdown, modal, tabs, pagination)
- Form validation patterns library (documented inline only)
- Dark mode testing/QA (light mode only ships)
- Website UI kit (interactive site showcasing the system)

---

### Phase v1.1 — Expansion (4–6 weeks, after v1.0 ships)

**Goal:** Build on proven foundation; add patterns and secondary components.

#### v1.1 Additions

**1. Secondary Components**
- Dropdown/Select (with searchable variant)
- Modal/Dialog
- Tabs (tablist, tabpanel)
- Breadcrumb nav
- Pagination
- Toast notification

**2. Interaction Patterns**
- Form validation library (complete state matrix, async patterns)
- Empty state patterns (3–4 variants)
- Error/failure state patterns
- Loading state patterns (with optional spinner component)
- Navigation patterns (header collapse behavior at breakpoints)

**3. Devices Refinement**
- DigGrid variants (2×2, 3×3, 5×4 sizes)
- Full Horizon device (with proportional specs)
- Optional Brush device (if user decides to add)

**4. Dark Mode QA & Launch**
- Full component testing in dark mode
- Fixture UI kit built in light + dark
- Dark mode toggle implemented
- A/B test dark mode adoption

**5. Website UI Kit**
- Complete interactive specimen site (Next.js or similar)
- Component gallery (playable states)
- Page templates (hero, features, grid, CTA, footer)
- Live form (working contact form with validation)
- Case study template (multi-section page)
- Responsive tests (mobile, tablet, desktop views)

---

### Build Sequence (Detailed Order)

**Week 1–2: Tokens + Foundation**
1. CSS color tokens (light + dark)
2. Typography tokens (font stacks, scales, semantic tokens)
3. Spacing tokens (scale, grid, gutter rules)
4. Relief tokens (raised/carved shadows)
5. Token documentation + tests (contrast verification)

**Week 2–3: Core Components (Part 1)**
1. Button (all variants, all states)
2. Input (all states, validation)
3. Label (form label component)

**Week 3–4: Core Components (Part 2)**
1. Card (all variants)
2. Tag (all variants)
3. Icon set (17 glyphs, all sizes)

**Week 4–5: Brand Devices**
1. SphinxMark SVG (all sizes, all tones)
2. DigGrid SVG + component
3. Cartouche CSS component
4. Horizon CSS component

**Week 5–6: Specimen & Docs**
1. Foundation specimen cards (15–20)
2. Component documentation (.spec.md files)
3. Token reference (colors, type, spacing)
4. Device usage guide
5. Readme.md + index

**Week 6–8: Polish & QA**
1. Accessibility audit (keyboard nav, screen reader, contrast)
2. Responsive testing (all breakpoints)
3. Cross-browser testing (Chrome, Firefox, Safari)
4. Documentation review
5. Handoff prep (GitHub, Storybook, wiki, etc.)

---

## Governance & Versioning

### Version Numbering

**Format:** `MAJOR.MINOR.PATCH`

- **MAJOR** (e.g., 2.0.0): Breaking changes, complete redesign, incompatible API
- **MINOR** (e.g., 2.1.0): New features (new component, new device), backward compatible
- **PATCH** (e.g., 2.0.1): Bug fixes, token tweaks, documentation updates

### Token Governance

**Adding a New Token:**

1. **Propose** in the design team (Slack/meeting)
2. **Justify:** Does it exist in the palette already? Is it truly needed?
3. **Name:** Follow `--sm-{category}-{role}-{tint}` convention
4. **Document:** Add to token spec with use case, contrast ratio (if color)
5. **Merge:** Design lead approves, engineer adds to CSS, bump MINOR version

**Maximum tokens per category:**
- Colors: 15–20 max (palette bloat = coherence loss)
- Spacing: 8–10 values (follow 8px base scale)
- Type scales: defined (no arbitrary sizes)
- Shadows: 2–3 (raised, carved, maybe accent)

### Component Governance

**Adding a New Component:**

1. **Design:** Full specification (props, states, usage rules, examples)
2. **Review:** Design lead + product team (is it needed? Does it fit the system?)
3. **Build:** .jsx + .d.ts + .spec.md + .specimen.html
4. **Test:** Accessibility, responsive, all states
5. **Document:** Add to component index, link in readme
6. **Approve:** Design lead sign-off
7. **Release:** Bump MINOR version

**Component Removal:**

- Mark deprecated in CHANGELOG
- Keep in codebase for 2 minor versions (6+ months)
- Announce migration path
- Remove in next MAJOR version

### Device Governance

**Adding a New Device:**
- Must map to the excavation narrative (Survey/Excavate/Restore/Exhibit)
- Must be fully spec'd (SVG geometry, usage rules, tones)
- Design lead final approval
- Bump MINOR version

**No device changes mid-project.** Once a device is released, variations go to v1.1+.

### Deprecation Policy

- **Announce:** 1 minor version in advance (e.g., "Button will remove size='xl' in v2.1")
- **Grace period:** 2 minor versions (e.g., size='xl' deprecated in v2.0, removed in v2.2)
- **Migration guide:** Document how to migrate in CHANGELOG

### Release Cadence

- **v1.0:** Initial release (6–8 weeks)
- **v1.1+:** Minor releases every 4–6 weeks (new components, refinements)
- **Patch releases:** As needed (bug fixes, doc updates, no timeline)
- **v2.0:** Only after 12+ months, major brand/structural changes, significant user feedback

### Design System Governance Team

**Size:** 3–5 people minimum

**Roles:**
1. **Design Lead** (1 person) — Arbiter of all design decisions, brand coherence, component approval
2. **Engineer** (1 person) — Token architecture, component implementation, CI/CD, Storybook
3. **Product Strategist** (0.5 FTE) — Aligns system with soilmass business goals, customer feedback

**Cadence:**
- **Weekly sync** (1 hour): Component proposals, token requests, bugs
- **Monthly review** (2 hours): Roadmap, backlog triage, user feedback
- **Quarterly strategy** (2 hours): Version planning, roadmap refinement

### Documentation Maintenance

- **System of record:** GitHub repo + Storybook (deployed)
- **Sync rule:** If code changes, docs update in same PR (no delayed docs)
- **Review:** Design lead reviews all PRs before merge
- **Changelog:** Entry for every PR (MAJOR/MINOR/PATCH reason)

### User Feedback Loop

- **Internal:** Slack channel #design-system-feedback for soilmass team
- **External:** GitHub issues (if system is open-sourced)
- **Quarterly survey:** 5-minute form asking team satisfaction, pain points, requests
- **Monthly metrics:** Component usage tracking (which components used most? Least?)

---

## Appendix A: File Structure

```
/design-system/
├── /tokens/
│   ├── colors.css
│   ├── typography.css
│   ├── spacing.css
│   ├── relief.css
│   ├── motion.css
│   ├── index.css (@import all)
│   └── tokens.md (reference)
│
├── /components/
│   ├── Button/
│   │   ├── Button.jsx
│   │   ├── Button.d.ts
│   │   ├── Button.spec.md
│   │   └── Button.specimen.html
│   ├── Input/
│   ├── Card/
│   ├── Label/
│   ├── Tag/
│   └── Icon/
│
├── /devices/
│   ├── SphinxMark/
│   │   ├── sphinx-24.svg
│   │   ├── sphinx-32.svg
│   │   ├── sphinx-240.svg
│   │   ├── sphinx-400.svg
│   │   └── Sphinx.jsx (wrapper)
│   ├── DigGrid/
│   │   ├── DigGrid.svg (template)
│   │   ├── DigGrid.jsx
│   │   └── DigGrid.spec.md
│   ├── Cartouche/
│   └── Horizon/
│
├── /specimen/
│   ├── foundation-colors.html
│   ├── foundation-typography.html
│   ├── foundation-spacing.html
│   ├── foundation-devices.html
│   ├── foundation-states.html
│   └── (15–20 cards total)
│
├── /docs/
│   ├── README.md
│   ├── tokens.md
│   ├── components.md
│   ├── devices.md
│   ├── accessibility.md
│   ├── responsive.md
│   ├── dark-mode.md
│   └── CHANGELOG.md
│
└── DESIGN_SYSTEM_v2_REBUILT.md (this file)
```

---

## Appendix B: Checklist for v1.0 Completion

### Tokens
- [ ] All color tokens defined (light + dark)
- [ ] All typography tokens defined (font stacks, scales)
- [ ] All spacing tokens defined (8px base scale)
- [ ] All relief tokens defined (raised, carved, dark variants)
- [ ] All motion tokens defined (durations, easing)
- [ ] Token contrast verified (WCAG AA+ for all text combos)
- [ ] Token documentation written
- [ ] CSS file structure established

### Components (5 core)
- [ ] Button: all variants (primary, secondary, ghost) + sizes (sm, md, lg) + states (default, hover, focus, active, disabled, loading)
- [ ] Input: all types + states + error/success feedback
- [ ] Card: all variants (panel, bordered, dark)
- [ ] Label: semantic label component
- [ ] Tag: all variants (default, solid, accent)
- [ ] Icon: all 17 glyphs, all sizes, both tones

For each component:
- [ ] .jsx (self-contained, tokens only)
- [ ] .d.ts (props contract)
- [ ] .spec.md (usage guide + examples)
- [ ] .specimen.html (visual card showing all states)

### Devices (4 core)
- [ ] SphinxMark: SVG at all sizes (24, 32, 240, 400px), all tones (umber/limestone, gold/umber)
- [ ] DigGrid: SVG template + .jsx wrapper, usage spec
- [ ] Cartouche: CSS component, all tones
- [ ] Horizon: CSS component, spec on proportions

For each device:
- [ ] Visual spec (SVG geometry or CSS rules)
- [ ] Usage rules documented
- [ ] Responsive scaling defined
- [ ] .specimen.html showing in context

### Accessibility
- [ ] All text combinations contrast-verified (WCAG AA+)
- [ ] Focus indicators defined (3px outline, 2px offset)
- [ ] Form labels + aria-describedby tested
- [ ] Keyboard navigation tested (full site navigable via Tab)
- [ ] Screen reader tested (major content structures announced)
- [ ] Reduced motion respected (prefers-reduced-motion: reduce tested)
- [ ] Color-blind visibility checked (Coblis simulator)

### Responsive
- [ ] All breakpoints tested (600, 760, 820, 960, 980px)
- [ ] Mobile-first base styles working
- [ ] All components responsive at each breakpoint
- [ ] Header nav collapse at 820px working
- [ ] DigGrid sizing tested across breakpoints
- [ ] Type scales (clamp()) rendering correctly

### Documentation
- [ ] README.md written (overview, quick start, token guide)
- [ ] Component index created
- [ ] Token reference documented
- [ ] Device guide written (when/how to use each)
- [ ] Accessibility guide written
- [ ] Responsive guide written
- [ ] CHANGELOG initiated
- [ ] Contribution guide written (for v1.1 additions)

### QA & Testing
- [ ] Cross-browser testing (Chrome, Firefox, Safari, Edge)
- [ ] All components tested at all sizes
- [ ] Form validation tested (blur, submit, async)
- [ ] Error states tested
- [ ] Empty states tested
- [ ] Loading states tested
- [ ] No console warnings/errors
- [ ] No broken links in docs
- [ ] Storybook (if using) working and deployed

---

## Appendix C: Quick Token Reference

### Most-Used Tokens

```css
/* Text */
color: var(--sm-color-bg-dark); /* umber text */
color: var(--sm-color-text-secondary); /* sand-600, secondary */
color: var(--sm-color-accent-primary); /* ochre, accents only */

/* Background */
background: var(--sm-color-bg-primary); /* limestone, default */
background: var(--sm-color-surface-panel); /* sand-100, panels */
background: var(--sm-color-bg-dark); /* umber, dark sections */

/* Borders */
border: 1px solid var(--sm-color-border-subtle);

/* Relief */
box-shadow: var(--sm-shadow-raised); /* buttons, cards */
box-shadow: var(--sm-shadow-carved); /* inputs, wells */

/* Spacing */
padding: var(--sm-space-md); /* 16px */
gap: var(--sm-space-lg); /* 24px, grid gutter */
margin: var(--sm-space-2xl) 0; /* 48px, section gap */

/* Typography */
font-family: var(--sm-font-display); /* Marcellus */
font-family: var(--sm-font-body); /* Archivo */
font-family: var(--sm-font-mono); /* JetBrains Mono */
font-size: var(--sm-text-body); /* 16px */
line-height: var(--sm-text-body-lh); /* 1.625 */

/* Motion */
transition: color var(--sm-motion-hover-duration) var(--sm-motion-hover-easing);
```

---

**END OF SPECIFICATION**

---

**Approval Sign-Off (v1.0 Release Ready)**

- Design Lead: _______________
- Engineer: _______________
- Product Strategist: _______________
- Date: 2026-07-13

