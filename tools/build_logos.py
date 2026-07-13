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
CUT_TOP = 0.815      # grade line starts at 81.5% of inked wordmark height
CUT_BOTTOM = 0.856    # ochre band starts at 85.6%
FAV_CUT_TOP = 0.745   # favicon gap optically enlarged to ~7%
FAV_CUT_BOTTOM = 0.815


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
