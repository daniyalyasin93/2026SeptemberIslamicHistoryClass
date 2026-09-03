"""Generate the course base map as SVG from Natural Earth land polygons.

    python series/make_basemap.py

One base map, same projection every week. Deliberately plain: land, sea, and the six
anchor cities. Everything else is drawn on by hand during the session, which is the point.

Two outputs:
  series/basemap.svg        the wall/slide version, cities labelled
  series/basemap_blank.svg  the workbook version, city dots only, no labels
"""
import json
import math
import os

BBOX = (-12.0, 8.0, 80.0, 50.0)          # lon0, lat0, lon1, lat1 — Córdoba to Delhi
LAT0 = 30.0                               # standard parallel
W = 1600.0

ANCHORS = [
    ("مکہ",        "Makkah",        39.83, 21.42, "below"),
    ("مدینہ",      "Madina",        39.61, 24.47, "above"),
    ("دمشق",       "Dimashq",       36.31, 33.51, "above"),
    ("بغداد",      "Baghdad",       44.36, 33.31, "below"),
    ("قرطبہ",      "Qurtuba",       -4.78, 37.88, "above"),
    ("قسطنطنیہ",   "Qustantiniyya", 28.98, 41.01, "above"),
]

K = math.cos(math.radians(LAT0))
SPAN_X = (BBOX[2] - BBOX[0]) * K
SPAN_Y = BBOX[3] - BBOX[1]
H = W * SPAN_Y / SPAN_X


def px(lon, lat):
    x = (lon - BBOX[0]) * K / SPAN_X * W
    y = (BBOX[3] - lat) / SPAN_Y * H
    return x, y


def rings(geom):
    t = geom["type"]
    if t == "Polygon":
        return geom["coordinates"]
    if t == "MultiPolygon":
        return [r for poly in geom["coordinates"] for r in poly]
    return []


def visible(ring):
    lon0, lat0, lon1, lat1 = BBOX
    return any(lon0 - 8 <= x <= lon1 + 8 and lat0 - 8 <= y <= lat1 + 8 for x, y in ring)


def path_for(ring):
    pts, last = [], None
    for lon, lat in ring:
        x, y = px(lon, lat)
        p = (round(x, 1), round(y, 1))
        if p != last:                      # drop duplicate points at this scale
            pts.append(p)
            last = p
    if len(pts) < 3:
        return ""
    return "M" + "L".join("%g %g" % p for p in pts) + "Z"


def land_paths(src):
    with open(src, encoding="utf-8") as f:
        gj = json.load(f)
    out = []
    for feat in gj["features"]:
        for ring in rings(feat.get("geometry") or {}):
            if visible(ring):
                d = path_for(ring)
                if d:
                    out.append(d)
    return out


def svg(paths, labelled):
    o = []
    o.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %g %g" '
             'font-family="Noto Nastaliq Urdu, serif">' % (W, H))
    o.append('<defs><clipPath id="fr"><rect x="0" y="0" width="%g" height="%g"/></clipPath></defs>' % (W, H))
    o.append('<g clip-path="url(#fr)">')
    o.append('<rect x="0" y="0" width="%g" height="%g" fill="#DCE8E6"/>' % (W, H))   # sea
    o.append('<g fill="#EFEADC" stroke="#B9C7C3" stroke-width="1.1" stroke-linejoin="round">')
    for d in paths:
        o.append('<path d="%s"/>' % d)
    o.append('</g>')

    for ur, en, lon, lat, side in ANCHORS:
        x, y = px(lon, lat)
        o.append('<circle cx="%.1f" cy="%.1f" r="7" fill="#104A43"/>' % (x, y))
        o.append('<circle cx="%.1f" cy="%.1f" r="13" fill="none" stroke="#104A43" '
                 'stroke-width="1.6" opacity=".45"/>' % (x, y))
        if labelled:
            # Nastaliq carries deep descenders, so the two labels need real separation
            ur_dy, en_dy = (-34, -62) if side == "above" else (58, 80)
            o.append('<text x="%.1f" y="%.1f" text-anchor="middle" font-size="30" '
                     'fill="#0A322E" direction="rtl">%s</text>' % (x, y + ur_dy, ur))
            o.append('<text x="%.1f" y="%.1f" text-anchor="middle" font-size="15" '
                     'font-family="Georgia, serif" fill="#5A6862" letter-spacing="1.4">%s</text>'
                     % (x, y + en_dy, en.upper()))
    o.append('</g>')
    o.append('<rect x="0.5" y="0.5" width="%g" height="%g" fill="none" stroke="#104A43" '
             'stroke-width="1" opacity=".5"/>' % (W - 1, H - 1))
    o.append('</svg>')
    return "\n".join(o)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "data", "ne_50m_land.geojson")
    paths = land_paths(src)
    for name, lab in [("basemap.svg", True), ("basemap_blank.svg", False)]:
        p = os.path.join(here, name)
        with open(p, "w", encoding="utf-8") as f:
            f.write(svg(paths, lab))
        print("%-20s %6.1f KB   %d land paths   %gx%g" % (name, os.path.getsize(p) / 1024, len(paths), W, round(H)))
