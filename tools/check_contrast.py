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
    ("ochre-600", "stone-100", 4.5, "ochre labels on panels"),
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
