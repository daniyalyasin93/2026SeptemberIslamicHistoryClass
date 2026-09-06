"""Session 2 visuals — «Baarah Saal», Abu Bakr al-Siddiq's caliphate, 11-13 AH.

    python series/make_l02_visuals.py

Builds the eleven assets named in the session-2 map contract, into series/visuals/:

    map_s2_open_11ah.png        bookend IN  — Arabia at 11 AH, the two empires at the edges
    map_s2_usama.png            Jaysh Usama: Madina north to Ubna / the Syrian marches, and back
    map_s2_ridda_eleven.png     the columns leaving Dhu al-Qassa
    map_s2_buzakha.png          Khalid's line of march to Buzakha; Asad / Ghatafan country lit
    map_s2_yamama.png           Aqraba' and Hadiqat al-Mawt
    map_s2_darin.png            al-Bahrayn: Juwatha, and the crossing to Darin
    map_s2_arabia_12ah.png      Arabia whole again — no arrows, one colour
    map_s2_iraq_sham_13ah.png   Iraq (al-Hira), then the desert march west into Syria
    map_s2_close_13ah.png       bookend OUT — 13 AH solid, 11 AH dashed beneath
    map_s2_close_23ah.png       23 AH solid, 11 AH dashed  (built now, for a later session)
    line_s2_lit.png             bookend OUT — the series line with only 11-13 AH lit

Everything on these maps is drawn from the **Map:** line of the matching card in
L02_baarah_saal/SPINE.md. Nothing is added that the spine does not carry.

DESIGN NOTES, deliberate:
  * Every bbox is chosen so the render comes out near 4:3 — these sit in the left column of a
    16:9 slide (~7.25in x 5.42in). Session 1's maps were near-square and floated in their box.
  * Labels are large (30-48px at 1800px wide) and few. Projected, not printed.
  * Labels are ASCII-transliterated. Georgia has no glyph for the Arabic honorific, and a
    tofu box on a projected map is worse than no honorific — the deck and the script carry
    the honorifics. This follows the precedent already set in make_visuals.py.
  * Territorial extents are SCHEMATIC and every map carrying one says so on its face.
  * Sites the sources do not fix (Quraqir, Suwa, Buzakha, Aqraba', Darin) are placed
    approximately and the map says so.

The projection, the land data, the palette and the render pipeline all come from
series/make_visuals.py. Nothing in that file is edited; the gazetteer is extended at runtime.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import make_visuals as mv
from make_visuals import View, map_svg, render, line_svg
from make_visuals import TEAL, DEEP, GOLD, MAROON

CREAM = "#FAF7F0"
GREY = "#8A9490"
SLATE = "#5A6862"


# --------------------------------------------------------------------------- gazetteer
# Approximate modern coordinates, for PLACEMENT ONLY. Never a claim about a site.
# Marked "approx" below are places our sources do not fix.
L02_PLACES = {
    # Hijaz and the road north
    "jurf":          (39.58, 24.55),   # al-Jurf, one march outside Madina
    "dhu_khushub":   (39.35, 25.10),   # approx
    "ubna":          (35.78, 31.32),   # approx — in the Balqa'
    "balqa":         (35.90, 31.90),
    # the Ridda theatre
    "dhu_qassa":     (40.30, 24.30),   # one day's ride from Madina
    "ajaa_salma":    (41.05, 27.30),   # the two mountains of Tayyi'
    "buzakha_l2":    (41.40, 27.70),   # approx
    "sumayra":       (42.55, 26.90),   # approx
    "najd":          (42.30, 26.20),   # region label
    "qudaa":         (38.60, 29.60),   # region label, approx
    "sham_marches":  (36.50, 31.40),   # region label
    "sham":          (36.60, 33.20),   # region label
    "yamama_l2":     (47.30, 24.15),   # approx
    "aqraba":        (47.05, 24.45),   # approx
    "hadiqa":        (46.32, 25.06),   # approx
    "bahrayn_reg":   (49.59, 25.38),   # Hajar
    "juwatha":       (49.75, 25.42),   # approx
    "embark":        (49.96, 26.28),
    "darin":         (50.22, 26.66),   # approx — an island anchorage
    "uman":          (56.27, 25.62),   # Daba
    "mahra":         (52.50, 16.50),   # region label
    "hadramawt":     (48.80, 15.90),   # region label
    "yaman":         (44.21, 15.35),   # San'a
    "tihama":        (43.30, 14.00),   # region label
    "najran_l2":     (44.22, 17.49),
    # outward, 12-13 AH
    "lower_furat":   (47.90, 30.30),
    "hira":          (44.35, 31.90),   # approx
    "quraqir":       (42.20, 32.50),   # approx — a desert water
    "suwa":          (39.40, 33.90),   # approx — a desert water
    "tadmur":        (38.28, 34.55),
    "yarmuk_l2":     (35.95, 32.72),   # approx
    "nihawand":      (48.38, 34.19),
}
mv.PLACES.update(L02_PLACES)


# --------------------------------------------------------------------------- views
# Each bbox is fitted so height/width lands near 0.75 (4:3), with the action filling it.
def _fit(view):
    return "%s  %dx%d  ratio %.3f" % (view.bbox, view.w, view.h, view.h / view.w)


V_THEATRE = View((29.5, 11.0, 63.5, 34.5), 1800, 22.75)   # 11 AH / 13 AH bookend pair
V_ARABIA = View((32.0, 11.5, 62.0, 33.0), 1800, 22.25)    # the peninsula, tight
V_USAMA = View((32.0, 22.0, 48.5, 33.0), 1800, 27.50)     # Madina to the Balqa'
V_BUZAKHA = View((33.8, 24.6, 47.3, 33.6), 1800, 29.10)   # Najd, with al-Sham in frame
V_YAMAMA = View((45.3, 22.9, 49.7, 25.9), 1800, 24.30)    # al-Yamama, close
V_DARIN = View((48.4, 24.6, 52.6, 27.4), 1800, 26.00)     # al-Bahrayn coast
V_IRAQSHAM = View((33.5, 23.0, 53.0, 36.0), 1800, 29.50)  # Iraq and al-Sham
V_WIDE23 = View((24.0, 11.5, 66.3, 40.0), 1800, 25.75)    # 23 AH, for a later session


# --------------------------------------------------------------------------- extents
# SCHEMATIC. Coarse outlines drawn so the room can see change between two evenings.
# They are not a source claim about a frontier, and every map using one says so.
_SOUTH_ARABIA = [
    (51.50, 24.60), (55.30, 23.40), (56.55, 25.40), (57.60, 24.60), (58.90, 23.50),
    (59.80, 22.50), (57.80, 19.00), (55.00, 17.00), (52.20, 15.00), (48.00, 14.00),
    (45.00, 12.70), (43.30, 12.70), (42.50, 15.50), (40.50, 19.50), (39.00, 21.40),
    (38.00, 23.50),
]

EXT_11AH = [
    (34.40, 28.20), (35.60, 29.40), (37.50, 30.20), (39.60, 30.60), (41.80, 30.60),
    (44.00, 30.40), (46.50, 29.80), (47.90, 29.20), (50.20, 26.60),
] + _SOUTH_ARABIA + [(36.50, 25.50), (35.20, 26.80)]

EXT_13AH = [
    (34.30, 29.40), (34.80, 31.30), (35.30, 32.40), (36.20, 32.80), (37.40, 32.00),
    (39.00, 31.60), (41.00, 31.60), (43.00, 32.30), (44.60, 32.20), (45.60, 31.60),
    (47.00, 30.60), (48.20, 30.20), (50.20, 26.60),
] + _SOUTH_ARABIA + [(36.50, 25.50), (35.20, 27.60)]

EXT_23AH = [
    (29.00, 31.40), (31.50, 31.50), (33.50, 31.30), (34.50, 31.70), (35.50, 33.30),
    (36.50, 34.60), (37.60, 36.40), (40.00, 37.00), (43.00, 37.20), (45.50, 37.50),
    (48.00, 37.00), (50.50, 36.80), (53.00, 36.60), (56.00, 35.80), (58.50, 33.50),
    (60.50, 30.50), (59.00, 27.50), (57.00, 26.80), (56.55, 25.40), (57.60, 24.60),
    (58.90, 23.50), (59.80, 22.50), (57.80, 19.00), (55.00, 17.00), (52.20, 15.00),
    (48.00, 14.00), (45.00, 12.70), (43.30, 12.70), (42.50, 15.50), (40.50, 19.50),
    (39.00, 21.40), (38.00, 23.50), (36.50, 25.50), (35.00, 27.60), (34.20, 28.60),
    (32.60, 24.20), (30.80, 24.20), (29.60, 28.00),
]


# --------------------------------------------------------------------------- primitives
def txt(x, y, s, size=32, colour=DEEP, weight="700", anchor="middle",
        italic=False, halo=8, spacing=None):
    """Text with a cream halo so it stays legible over land, sea or a shaded region."""
    extra = ""
    if italic:
        extra += ' font-style="italic"'
    if spacing:
        extra += ' letter-spacing="%d"' % spacing
    return ('<text x="%.1f" y="%.1f" text-anchor="%s" font-family="Georgia, serif" '
            'font-size="%d" font-weight="%s"%s fill="%s" paint-order="stroke" '
            'stroke="%s" stroke-width="%d" stroke-linejoin="round">%s</text>'
            % (x, y, anchor, size, weight, extra, colour, CREAM, halo, s))


def at(view, key, s, size=32, colour=DEEP, weight="700", anchor="middle",
       italic=False, dx=0, dy=0, spacing=None):
    """Free text placed at a lon/lat (key or tuple), with an optional pixel nudge."""
    lonlat = mv.PLACES[key] if isinstance(key, str) else key
    x, y = view.px(*lonlat)
    return txt(x + dx, y + dy, s, size, colour, weight, anchor, italic, spacing=spacing)


def pin(view, key, label=None, colour=TEAL, r=13, side="above", sub=None, size=34,
        sub_colour=MAROON, dx=0, dy=0):
    lonlat = mv.PLACES[key] if isinstance(key, str) else key
    x, y = view.px(*lonlat)
    o = ['<circle cx="%.1f" cy="%.1f" r="%d" fill="%s" stroke="%s" stroke-width="3"/>'
         % (x, y, r, colour, CREAM)]
    if label:
        if side == "above":
            tx, ty, anc = x + dx, y + dy - (r + 16), "middle"
            sy = ty - size * 0.92
        elif side == "below":
            tx, ty, anc = x + dx, y + dy + (r + size), "middle"
            sy = ty + size * 0.92
        elif side == "left":
            tx, ty, anc = x + dx - (r + 14), y + dy + size * 0.34, "end"
            sy = ty + size * 0.92
        else:
            tx, ty, anc = x + dx + (r + 14), y + dy + size * 0.34, "start"
            sy = ty + size * 0.92
        o.append(txt(tx, ty, label, size, DEEP, "700", anc))
        if sub:
            o.append(txt(tx, sy, sub, int(size * 0.66), sub_colour, "600", anc, italic=True))
    return "".join(o)


def poly(view, coords, fill=None, opacity=1.0, stroke=None, width=5, dash=None):
    pts = [view.px(lon, lat) for lon, lat in coords]
    d = "M" + "L".join("%.1f %.1f" % p for p in pts) + "Z"
    a = ['<path d="%s"' % d]
    a.append(' fill="%s" fill-opacity="%.2f"' % (fill, opacity) if fill else ' fill="none"')
    if stroke:
        a.append(' stroke="%s" stroke-width="%d" stroke-linejoin="round"' % (stroke, width))
        if dash:
            a.append(' stroke-dasharray="%s"' % dash)
    a.append("/>")
    return "".join(a)


def blob(view, lon, lat, dlon, dlat, fill=GOLD, opacity=0.24, stroke=None, width=4, dash=None):
    cx, cy = view.px(lon, lat)
    rx = abs(view.px(lon + dlon, lat)[0] - cx)
    ry = abs(view.px(lon, lat + dlat)[1] - cy)
    a = ['<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="%s" fill-opacity="%.2f"'
         % (cx, cy, rx, ry, fill, opacity)]
    if stroke:
        a.append(' stroke="%s" stroke-width="%d"' % (stroke, width))
        if dash:
            a.append(' stroke-dasharray="%s"' % dash)
    a.append("/>")
    return "".join(a)


def box(view, lon, lat, dlon, dlat, fill=MAROON, opacity=0.5, stroke=None, width=6, rx=14):
    cx, cy = view.px(lon, lat)
    rxp = abs(view.px(lon + dlon, lat)[0] - cx)
    ryp = abs(view.px(lon, lat + dlat)[1] - cy)
    a = ['<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%d" fill="%s" '
         'fill-opacity="%.2f"' % (cx - rxp, cy - ryp, 2 * rxp, 2 * ryp, rx, fill, opacity)]
    if stroke:
        a.append(' stroke="%s" stroke-width="%d"' % (stroke, width))
    a.append("/>")
    return "".join(a)


def route(view, keys, colour=MAROON, width=9, dash=None, head=True, opacity=0.92, headsize=26):
    """A smoothed multi-point route with an arrowhead. Keys are gazetteer names or (lon, lat)."""
    pts = [view.px(*(mv.PLACES[k] if isinstance(k, str) else k)) for k in keys]
    d = "M%.1f %.1f" % pts[0]
    if len(pts) == 2:
        d += " L%.1f %.1f" % pts[1]
    else:
        for i in range(1, len(pts) - 1):
            mx = (pts[i][0] + pts[i + 1][0]) / 2.0
            my = (pts[i][1] + pts[i + 1][1]) / 2.0
            d += " Q%.1f %.1f %.1f %.1f" % (pts[i][0], pts[i][1], mx, my)
        d += " L%.1f %.1f" % pts[-1]
    o = ['<path d="%s" fill="none" stroke="%s" stroke-width="%d" stroke-linecap="round" '
         'stroke-linejoin="round" opacity="%.2f"%s/>'
         % (d, colour, width, opacity, ' stroke-dasharray="%s"' % dash if dash else "")]
    if head:
        (x1, y1), (x2, y2) = pts[-2], pts[-1]
        ang = math.atan2(y2 - y1, x2 - x1)
        p1 = (x2 - headsize * math.cos(ang - 0.42), y2 - headsize * math.sin(ang - 0.42))
        p2 = (x2 - headsize * math.cos(ang + 0.42), y2 - headsize * math.sin(ang + 0.42))
        o.append('<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="%s" opacity="%.2f"/>'
                 % (x2, y2, p1[0], p1[1], p2[0], p2[1], colour, opacity))
    return "".join(o)


def bar(view, lon, lat, dlon, dlat, colour=TEAL, width=14):
    """A short thick stroke — used for closing a road."""
    x1, y1 = view.px(lon - dlon, lat - dlat)
    x2, y2 = view.px(lon + dlon, lat + dlat)
    return ('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%d" '
            'stroke-linecap="round"/>' % (x1, y1, x2, y2, colour, width))


def caption(view, text, note=None, size=44):
    o = [txt(44, view.h - 46, text, size, DEEP, "600", "start", italic=True, halo=10)]
    if note:
        o.append(txt(view.w - 44, view.h - 34, note, 26, SLATE, "400", "end", italic=True, halo=8))
    return "".join(o)


def legend(view, items, x=48, y=None, sw=72, gap=56, size=31):
    y = (view.h - 150) if y is None else y
    o = []
    for i, (kind, colour, lab) in enumerate(items):
        yy = y + i * gap
        if kind == "fill":
            o.append('<rect x="%.1f" y="%.1f" width="%d" height="28" rx="5" fill="%s" '
                     'fill-opacity="0.45" stroke="%s" stroke-width="3"/>'
                     % (x, yy - 22, sw, colour, DEEP))
        else:
            o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
                     'stroke-width="7" stroke-dasharray="20 14"/>'
                     % (x, yy - 8, x + sw, yy - 8, colour))
        o.append(txt(x + sw + 18, yy, lab, size, DEEP, "700", "start"))
    return "".join(o)


SCHEMATIC = "extent shown schematically"
APPROX = "sites placed approximately"


# --------------------------------------------------------------------------- the maps
def m_open_11ah():
    v = V_THEATRE
    layers = [poly(v, EXT_11AH, fill=TEAL, opacity=0.34, stroke=DEEP, width=5)]
    dots = [
        txt(48, 68, "BYZANTINE ROME", 38, GREY, "700", "start", spacing=5),
        txt(v.w - 48, 68, "SASANIAN PERSIA", 38, GREY, "700", "end", spacing=5),
        pin(v, "madina", "MADINA", GOLD, 17, "above", None, 44),
        pin(v, "makkah", "Makkah", TEAL, 12, "below", None, 34),
        caption(v, "11 AH / 632 CE - where the map stood", SCHEMATIC),
    ]
    return v, map_svg(v, layers=layers, dots=dots, anchors=[])


def m_usama():
    v = V_USAMA
    out = ["madina", "jurf", "dhu_khushub", "tabuk", "ubna"]
    back = ["ubna", (37.80, 29.60), (39.60, 26.80), "madina"]
    layers = [
        route(v, out, MAROON, 11),
        route(v, back, MAROON, 9, dash="28 18"),
    ]
    dots = [
        txt(48, 68, "BYZANTINE ROME", 36, GREY, "700", "start", spacing=5),
        pin(v, "ubna", "Ubna", MAROON, 16, "above", "the marches of al-Balqa'", 40),
        pin(v, "tabuk", "Tabuk", TEAL, 11, "left", None, 32),
        pin(v, "dhu_khushub", "Dhu Khushub", TEAL, 10, "left", None, 30),
        pin(v, "madina", "MADINA", GOLD, 17, "left", None, 44),
        at(v, (40.55, 24.66), "al-Jurf, one march out", 34, DEEP, "700", anchor="start"),
        at(v, (40.55, 24.66), "he walked the army out from here", 29, MAROON, "600",
           anchor="start", italic=True, dy=42),
        at(v, (37.4, 28.6), "out", 34, MAROON, "700", italic=True),
        at(v, (39.4, 28.2), "back", 34, MAROON, "700", italic=True),
        caption(v, "Out and back: forty days, some say seventy", APPROX),
    ]
    return v, map_svg(v, layers=layers, dots=dots, anchors=[])


def m_ridda_eleven():
    v = V_ARABIA
    targets = ["sham_marches", "qudaa", "najd", "yamama_l2", "bahrayn_reg", "uman",
               "mahra", "hadramawt", "yaman", "tihama"]
    layers = [route(v, ["dhu_qassa", t], MAROON, 9, headsize=28) for t in targets]
    dots = [
        pin(v, "sham_marches", "the marches of al-Sham", MAROON, 11, "above", None, 30),
        pin(v, "qudaa", "Quda'a", MAROON, 11, "above", None, 30),
        pin(v, "najd", "Najd", MAROON, 11, "above", None, 32),
        pin(v, "yamama_l2", "al-Yamama", MAROON, 12, "right", None, 32),
        pin(v, "bahrayn_reg", "al-Bahrayn", MAROON, 11, "right", None, 30),
        pin(v, "uman", "Uman", MAROON, 11, "right", None, 30),
        pin(v, "mahra", "Mahra", MAROON, 11, "below", None, 30),
        pin(v, "hadramawt", "Hadramawt", MAROON, 11, "below", None, 30),
        pin(v, "yaman", "al-Yaman", MAROON, 11, "left", None, 30),
        pin(v, "tihama", "Tihama", MAROON, 11, "left", None, 30),
        pin(v, "madina", "Madina", TEAL, 11, "above", None, 30, dx=-30),
        pin(v, "dhu_qassa", "DHU AL-QASSA", GOLD, 18, "below",
            "one day's ride from Madina", 42),
        caption(v, "The commanders separate: each to his own front", APPROX),
    ]
    return v, map_svg(v, layers=layers, dots=dots, anchors=[])


def m_buzakha():
    v = V_BUZAKHA
    layers = [
        blob(v, 41.30, 27.25, 1.95, 1.55, GOLD, 0.30, GOLD, 5),
        blob(v, 42.85, 25.85, 1.00, 0.72, GOLD, 0.14, MAROON, 4, "16 12"),
        route(v, ["sumayra", (42.00, 26.65), "buzakha_l2"], MAROON, 8, opacity=0.62),
        route(v, ["ajaa_salma", "buzakha_l2"], MAROON, 15),
        route(v, ["buzakha_l2", (39.30, 30.60), "sham"], MAROON, 6, dash="20 15", opacity=0.8),
    ]
    dots = [
        at(v, (41.30, 28.55), "ASAD and GHATAFAN", 40, DEEP, "700", spacing=3),
        at(v, (42.85, 25.85), "Banu Amir", 32, DEEP, "700"),
        at(v, (42.85, 25.85), "watching", 26, MAROON, "600", italic=True, dy=34),
        at(v, (38.10, 31.10), "Tulayha gets away,", 32, MAROON, "700", italic=True),
        at(v, (38.10, 31.10), "to al-Sham", 32, MAROON, "700", italic=True, dy=40),
        pin(v, "sham", "al-Sham", TEAL, 12, "above", None, 34),
        pin(v, "ajaa_salma", "Aja and Salma", TEAL, 13, "left", None, 32, dy=34),
        pin(v, "sumayra", "Sumayra", TEAL, 12, "right", "Tulayha moves up", 30),
        pin(v, "buzakha_l2", "BUZAKHA", MAROON, 19, "right", "the field", 44),
        caption(v, "Buzakha: Khalid's line of march", APPROX),
    ]
    return v, map_svg(v, layers=layers, dots=dots, anchors=[])


def m_yamama():
    v = V_YAMAMA
    gx, gy = v.px(*mv.PLACES["hadiqa"])
    gw = abs(v.px(mv.PLACES["hadiqa"][0] + 0.18, mv.PLACES["hadiqa"][1])[0] - gx)
    gh = abs(v.px(mv.PLACES["hadiqa"][0], mv.PLACES["hadiqa"][1] + 0.16)[1] - gy)
    # four walls with a gap in the south wall - the gate
    garden = (
        '<path d="M%.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f" '
        'fill="%s" fill-opacity="0.10" stroke="%s" stroke-width="11" stroke-linejoin="round"/>'
        % (gx - 26, gy + gh, gx - gw, gy + gh, gx - gw, gy - gh, gx + gw, gy - gh,
           gx + gw, gy + gh, gx + 26, gy + gh, MAROON, MAROON))
    layers = [
        blob(v, 48.10, 24.55, 0.72, 0.48, GOLD, 0.30, GOLD, 5),
        box(v, 47.05, 24.45, 0.28, 0.19, MAROON, 0.52, MAROON, 6),
        garden,
        route(v, [(45.55, 24.62), (46.15, 24.55), (46.75, 24.48)], MAROON, 14),
        route(v, [(48.75, 23.25), (48.15, 23.55), (47.55, 23.92)], MAROON, 7,
              dash="20 15", opacity=0.5),
        route(v, [(48.30, 23.15), (47.85, 23.50), (47.20, 23.86)], MAROON, 7,
              dash="20 15", opacity=0.5),
        # the gate arrow is in PIXELS, not lon/lat — drawn directly
        '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="13" '
        'stroke-linecap="round"/>'
        % (gx, gy + gh + 104, gx, gy + gh + 14, TEAL),
        '<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="%s"/>'
        % (gx, gy + gh - 10, gx - 20, gy + gh + 26, gx + 20, gy + gh + 26, TEAL),
    ]
    dots = [
        at(v, (47.50, 25.62), "AL-YAMAMA", 46, GREY, "700", spacing=6),
        at(v, (45.58, 24.72), "Khalid b. al-Walid", 34, MAROON, "700", anchor="start"),
        at(v, (48.85, 23.35), "the earlier approach", 30, MAROON, "600", italic=True,
           anchor="start"),
        at(v, (48.10, 24.55), "the cultivated country", 33, DEEP, "700"),
        at(v, (48.10, 24.55), "the households behind them", 29, DEEP, "600",
           italic=True, dy=38),
        at(v, (47.05, 24.10), "no line of retreat", 31, MAROON, "700", italic=True),
        at(v, "aqraba", "AQRABA", 42, DEEP, "700", dy=-125),
        at(v, "aqraba", "the camp", 29, MAROON, "600", italic=True, dy=-90),
        txt(gx, gy - gh - 84, "Hadiqat al-Mawt", 36, DEEP, "700"),
        txt(gx, gy - gh - 46, "the gate, opened from the inside", 27, MAROON, "600",
            italic=True),
        caption(v, "Aqraba', and the walled garden", APPROX),
    ]
    return v, map_svg(v, layers=layers, dots=dots, anchors=[])


def m_darin():
    v = V_DARIN
    # the land roads in behind the coast, each one closed with a bar across it
    roads = [[(48.55, 25.05), (49.20, 25.60), "embark"],
             [(48.60, 26.05), (49.25, 26.20), "embark"],
             [(49.30, 24.75), (49.70, 25.50), "embark"]]
    layers = [route(v, r, GREY, 6, dash="4 16", head=False, opacity=0.85) for r in roads]
    layers += [
        bar(v, 48.98, 25.42, 0.13, -0.11, TEAL, 17),
        bar(v, 48.95, 26.12, 0.05, 0.17, TEAL, 17),
        bar(v, 49.53, 25.19, 0.15, -0.08, TEAL, 17),
        route(v, ["embark", (50.02, 26.50), "darin"], MAROON, 8, dash="22 16", opacity=0.7),
        route(v, ["embark", (50.16, 26.42), "darin"], TEAL, 15),
        route(v, ["darin", (50.02, 26.55), "embark"], TEAL, 9, dash="22 16"),
    ]
    dots = [
        at(v, (48.63, 26.95), "AL-BAHRAYN", 42, GREY, "700", anchor="start", spacing=5),
        at(v, (48.55, 24.95), "every land road", 32, TEAL, "700", anchor="start"),
        at(v, (48.55, 24.95), "closed first", 32, TEAL, "700", anchor="start", dy=38),
        at(v, (50.55, 26.95), "a day and a night", 30, DEEP, "600", italic=True, anchor="start"),
        at(v, (50.55, 26.95), "by sea, and back the same day", 30, DEEP, "600",
           italic=True, anchor="start", dy=36),
        pin(v, "juwatha", "Juwatha", TEAL, 14, "below", None, 36),
        pin(v, "embark", "the coast", TEAL, 12, "left", None, 30),
        pin(v, "darin", "DARIN", MAROON, 17, "above", "the anchorage they fled to", 42),
        caption(v, "The roads sealed, then straight across the water", APPROX),
    ]
    return v, map_svg(v, layers=layers, dots=dots, anchors=[])


def m_arabia_12ah():
    v = V_ARABIA
    layers = [poly(v, EXT_11AH, fill=TEAL, opacity=0.44, stroke=DEEP, width=6)]
    bx, by = 0.40 * v.w, v.h - 124
    bracket = ('<rect x="%.1f" y="%.1f" width="%.1f" height="66" rx="10" fill="%s" '
               'fill-opacity="0.88"/>' % (bx, by, 0.44 * v.w, GOLD))
    dots = [
        pin(v, "madina", "MADINA", GOLD, 18, "above", None, 44),
        pin(v, "makkah", "Makkah", DEEP, 13, "below", None, 34),
        pin(v, "najran_l2", "Najran", GOLD, 14, "below", "under a covenant", 34),
        bracket,
        txt(bx + 0.22 * v.w, by + 48, "11 AH  -  12 AH", 42, DEEP, "700"),
        caption(v, "Arabia whole again", SCHEMATIC),
    ]
    return v, map_svg(v, layers=layers, dots=dots, anchors=[])


def m_iraq_sham_13ah():
    v = V_IRAQSHAM
    layers = [
        route(v, ["yamama_l2", (48.40, 27.30), "lower_furat"], MAROON, 11),
        route(v, ["lower_furat", (46.30, 31.20), "hira"], MAROON, 11),
        route(v, ["hira", "quraqir", "suwa", "tadmur"], MAROON, 12, dash="34 20"),
    ]
    dots = [
        txt(48, 68, "BYZANTINE ROME", 36, GREY, "700", "start", spacing=5),
        txt(v.w - 48, 68, "SASANIAN PERSIA", 36, GREY, "700", "end", spacing=5),
        pin(v, "yamama_l2", "al-Yamama", TEAL, 13, "below", None, 34),
        pin(v, "lower_furat", "the lower Euphrates", MAROON, 13, "right", None, 32),
        pin(v, "hira", "AL-HIRA", MAROON, 16, "right", None, 40),
        pin(v, "quraqir", "Quraqir", MAROON, 12, "below", None, 30),
        pin(v, "suwa", "Suwa", MAROON, 12, "left", None, 30),
        pin(v, "tadmur", "Tadmur", MAROON, 15, "above", "he comes out behind them", 38),
        pin(v, "yarmuk_l2", "the Yarmuk", TEAL, 14, "below", "where the Romans gathered", 34),
        pin(v, "dimashq", "Damascus", TEAL, 10, "left", None, 28),
        at(v, (43.6, 34.6), "no road:", 32, MAROON, "700", italic=True),
        at(v, (43.6, 34.6), "nine days, or five nights", 32, MAROON, "700",
           italic=True, dy=40),
        caption(v, "Iraq, then the desert crossing into Syria",
                "Quraqir and Suwa placed approximately"),
    ]
    return v, map_svg(v, layers=layers, dots=dots, anchors=[])


def m_close_13ah():
    v = V_THEATRE
    layers = [
        poly(v, EXT_13AH, fill=TEAL, opacity=0.40, stroke=DEEP, width=6),
        poly(v, EXT_11AH, fill=None, stroke=MAROON, width=7, dash="24 16"),
    ]
    dots = [
        pin(v, "madina", "MADINA", GOLD, 17, "below", None, 44),
        pin(v, "makkah", "Makkah", TEAL, 11, "below", None, 30),
        pin(v, "hira", "al-Hira", TEAL, 12, "right", None, 32),
        pin(v, "yarmuk_l2", "the Yarmuk", TEAL, 12, "above", None, 32),
        legend(v, [("fill", TEAL, "13 AH  /  634 CE"),
                   ("dash", MAROON, "11 AH  /  632 CE")], y=v.h - 212),
        caption(v, "Two years and three months", SCHEMATIC),
    ]
    return v, map_svg(v, layers=layers, dots=dots, anchors=[])


def m_close_23ah():
    v = V_WIDE23
    layers = [
        poly(v, EXT_23AH, fill=TEAL, opacity=0.40, stroke=DEEP, width=6),
        poly(v, EXT_11AH, fill=None, stroke=MAROON, width=7, dash="24 16"),
    ]
    dots = [
        pin(v, "madina", "MADINA", GOLD, 16, "below", None, 40),
        pin(v, "makkah", "Makkah", TEAL, 10, "below", None, 28),
        pin(v, "dimashq", "Damascus", TEAL, 12, "above", None, 32),
        pin(v, "fustat", "Fustat", TEAL, 12, "below", None, 32),
        pin(v, "madain", "al-Mada'in", TEAL, 12, "below", None, 32),
        pin(v, "nihawand", "Nihawand", TEAL, 12, "above", None, 30),
        legend(v, [("fill", TEAL, "23 AH  /  644 CE"),
                   ("dash", MAROON, "11 AH  /  632 CE")], y=v.h - 212),
        caption(v, "Twelve years later", SCHEMATIC),
    ]
    return v, map_svg(v, layers=layers, dots=dots, anchors=[])


MAPS = [
    ("map_s2_open_11ah", m_open_11ah),
    ("map_s2_usama", m_usama),
    ("map_s2_ridda_eleven", m_ridda_eleven),
    ("map_s2_buzakha", m_buzakha),
    ("map_s2_yamama", m_yamama),
    ("map_s2_darin", m_darin),
    ("map_s2_arabia_12ah", m_arabia_12ah),
    ("map_s2_iraq_sham_13ah", m_iraq_sham_13ah),
    ("map_s2_close_13ah", m_close_13ah),
    ("map_s2_close_23ah", m_close_23ah),
]


# --------------------------------------------------------------------------- the line
def line_lit_svg(lo=632, hi=634):
    """The series line with only tonight's span lit. line_svg() does the strip; this veils
    the rest of the series back and puts a gold marker on 11-13 AH."""
    svg = line_svg(lo, hi)
    w, m = 1800.0, 70.0
    span = 1947 - 632
    X = lambda y: m + (y - 632) / span * (w - 2 * m)
    x0, x1 = X(lo), X(hi)
    label = "Rashidun"
    extra = [
        # veil the whole series back, then re-draw tonight's span at full strength
        '<rect x="0" y="0" width="%g" height="190" fill="%s" opacity="0.52"/>' % (w, CREAM),
        '<rect x="%.1f" y="58" width="%.1f" height="62" rx="12" fill="%s" opacity="0.42"/>'
        % (x0 - 24, max(48.0, x1 - x0 + 48), GOLD),
        '<circle cx="%.1f" cy="89" r="16" fill="none" stroke="%s" stroke-width="4"/>'
        % (x0, GOLD),
        '<circle cx="%.1f" cy="89" r="9" fill="%s"/>' % (x0, GOLD),
        '<text x="%.1f" y="52" text-anchor="middle" font-family="Georgia, serif" '
        'font-size="22" font-weight="700" fill="%s">%s</text>' % (x0, DEEP, label),
        '<text x="%.1f" y="126" text-anchor="middle" font-family="Georgia, serif" '
        'font-size="20" fill="%s">632</text>' % (x0, SLATE),
        '<text x="%.1f" y="182" text-anchor="middle" font-family="Georgia, serif" '
        'font-size="24" font-weight="700" fill="%s">11-13 AH</text>' % (x0, DEEP),
    ]
    return svg.replace("</svg>", "\n".join(extra) + "\n</svg>")


if __name__ == "__main__":
    print("views:")
    for nm, vw in (("THEATRE", V_THEATRE), ("ARABIA", V_ARABIA), ("USAMA", V_USAMA),
                   ("BUZAKHA", V_BUZAKHA), ("YAMAMA", V_YAMAMA), ("DARIN", V_DARIN),
                   ("IRAQSHAM", V_IRAQSHAM), ("WIDE23", V_WIDE23)):
        print("  %-9s %s" % (nm, _fit(vw)))
    print("")
    for name, fn in MAPS:
        view, svg = fn()
        path, size = render(svg, name, view.w, view.h)
        print("%-28s %5d x %-5d %8.1f KB"
              % (os.path.basename(path), int(view.w), int(view.h), size / 1024.0))
    path, size = render(line_lit_svg(632, 634), "line_s2_lit", 1800, 190)
    print("%-28s %5d x %-5d %8.1f KB" % (os.path.basename(path), 1800, 190, size / 1024.0))
