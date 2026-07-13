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
