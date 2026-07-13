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
