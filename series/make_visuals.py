"""Generate the slide visuals: maps with movement drawn on them, and timeline strips.

    python series/make_visuals.py

Every content slide gets a picture. Two families:

  visuals/map_<name>.png       the base map with this session's movement drawn on it
  visuals/line_s<N>.png        the timeline strip with this session's span lit

Both are built as SVG and rendered through headless Chrome, so the map is the same
projection and the same six anchor cities every single week.
"""
import json
import math
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "visuals")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

BBOX = (-12.0, 8.0, 80.0, 50.0)
LAT0 = 30.0
W = 1800.0
K = math.cos(math.radians(LAT0))
SPAN_X = (BBOX[2] - BBOX[0]) * K
SPAN_Y = BBOX[3] - BBOX[1]
H = W * SPAN_Y / SPAN_X

INK, TEAL, DEEP, GOLD = "#1C2321", "#104A43", "#0A322E", "#C49A45"
SEA, LAND, COAST, MAROON = "#DCE8E6", "#EFEADC", "#B9C7C3", "#7A2E2E"

# lon, lat
PLACES = {
    "makkah": (39.83, 21.42), "madina": (39.61, 24.47), "dimashq": (36.31, 33.51),
    "baghdad": (44.36, 33.31), "qurtuba": (-4.78, 37.88), "qustantiniyya": (28.98, 41.01),
    "yarmuk": (35.90, 32.70), "qadisiyya": (44.30, 31.70), "madain": (44.58, 33.10),
    "fustat": (31.24, 30.05), "yamama": (47.30, 24.10), "granada": (-3.60, 37.18),
    "dihli": (77.20, 28.61), "sindh": (67.30, 24.80), "ayn_jalut": (35.35, 32.55),
    "vienna": (16.37, 48.20), "samarqand": (66.96, 39.65), "qahira": (31.24, 30.05),
}
ANCHOR_LABELS = [
    ("makkah", "Makkah", "below"), ("madina", "Madina", "above"),
    ("dimashq", "Damascus", "above"), ("baghdad", "Baghdad", "below"),
    ("qurtuba", "C\u00f3rdoba", "above"), ("qustantiniyya", "Constantinople", "above"),
]

# eight printed pegs — CE year, English label
# 632 and 661 are 29 years apart and land almost on the same point at this scale, so only
# the first is labelled — the dot for 661 stays.
PEGS = [
    (632, "Rashidun"), (661, ""), (750, "Abbasids"), (1099, "Crusades"),
    (1258, "Baghdad falls"), (1453, "Constantinople"), (1924, "Caliphate ends"), (1947, ""),
]


def px(lon, lat):
    return ((lon - BBOX[0]) * K / SPAN_X * W, (BBOX[3] - lat) / SPAN_Y * H)


def land_paths():
    src = os.path.join(HERE, "data", "ne_50m_land.geojson")
    with open(src, encoding="utf-8") as f:
        gj = json.load(f)
    out = []
    for feat in gj["features"]:
        g = feat.get("geometry") or {}
        rings = (g.get("coordinates") or []) if g.get("type") == "Polygon" else \
                [r for poly in (g.get("coordinates") or []) for r in poly] if g.get("type") == "MultiPolygon" else []
        for ring in rings:
            if not any(BBOX[0] - 8 <= x <= BBOX[2] + 8 and BBOX[1] - 8 <= y <= BBOX[3] + 8 for x, y in ring):
                continue
            pts, last = [], None
            for lon, lat in ring:
                p = tuple(round(v, 1) for v in px(lon, lat))
                if p != last:
                    pts.append(p); last = p
            if len(pts) >= 3:
                out.append("M" + "L".join("%g %g" % p for p in pts) + "Z")
    return out


def arrow(a, b, colour=MAROON, bow=0.22, width=7):
    """Curved arrow from place a to place b, with a head. Bowed so overlapping routes stay readable."""
    (x1, y1), (x2, y2) = px(*PLACES[a]), px(*PLACES[b])
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    dx, dy = x2 - x1, y2 - y1
    cx, cy = mx - dy * bow, my + dx * bow
    # head angle from the control point so it sits along the curve
    ang = math.atan2(y2 - cy, x2 - cx)
    s = 20
    p1 = (x2 - s * math.cos(ang - 0.42), y2 - s * math.sin(ang - 0.42))
    p2 = (x2 - s * math.cos(ang + 0.42), y2 - s * math.sin(ang + 0.42))
    return (
        '<path d="M%.1f %.1f Q%.1f %.1f %.1f %.1f" fill="none" stroke="%s" stroke-width="%d" '
        'stroke-linecap="round" opacity=".92"/>'
        '<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="%s"/>'
        % (x1, y1, cx, cy, x2, y2, colour, width, x2, y2, p1[0], p1[1], p2[0], p2[1], colour)
    )


def dot(place, label=None, colour=TEAL, r=9, side="above"):
    x, y = px(*PLACES[place])
    o = ['<circle cx="%.1f" cy="%.1f" r="%d" fill="%s"/>' % (x, y, r, colour)]
    if label:
        dy = -24 if side == "above" else 38
        o.append('<text x="%.1f" y="%.1f" text-anchor="middle" font-size="26" font-weight="600" '
                 'font-family="Georgia, serif" fill="%s">%s</text>' % (x, y + dy, DEEP, label))
    return "".join(o)


def map_svg(layers=(), extra_dots=(), caption=None):
    o = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %g %g">' % (W, H),
         '<rect width="%g" height="%g" fill="%s"/>' % (W, H, SEA),
         '<g fill="%s" stroke="%s" stroke-width="1.1" stroke-linejoin="round">' % (LAND, COAST)]
    o += ['<path d="%s"/>' % d for d in land_paths()]
    o.append("</g>")
    o += list(layers)
    for key, lab, side in ANCHOR_LABELS:
        o.append(dot(key, lab, TEAL, 9, side))
    o += list(extra_dots)
    if caption:
        o.append('<text x="34" y="%g" font-size="30" font-family="Georgia, serif" fill="%s" '
                 'font-style="italic">%s</text>' % (H - 30, DEEP, caption))
    o.append("</svg>")
    return "\n".join(o)


def line_svg(lo=None, hi=None):
    """Timeline strip. lo/hi in CE light this session's span; omit for the full line."""
    w, h = 1800.0, 190.0
    m = 70.0
    span = 1947 - 632

    def X(y):
        return m + (y - 632) / span * (w - 2 * m)

    o = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %g %g">' % (w, h),
         '<rect width="%g" height="%g" fill="#FAF7F0"/>' % (w, h)]
    if lo is not None:
        o.append('<rect x="%.1f" y="76" width="%.1f" height="26" fill="%s" opacity=".30"/>'
                 % (X(lo), max(6.0, X(hi) - X(lo)), GOLD))
    o.append('<line x1="%g" y1="89" x2="%g" y2="89" stroke="%s" stroke-width="3"/>' % (m, w - m, TEAL))
    # 632/661 and 1924/1947 sit almost on top of each other at this scale, so stagger them
    STAGGER = {661: 1, 1947: 1}
    for yr, lab in PEGS:
        x = X(yr)
        lit = lo is not None and lo <= yr <= hi
        row = STAGGER.get(yr, 0)
        o.append('<circle cx="%.1f" cy="89" r="%d" fill="%s"/>' % (x, 9 if lit else 6, GOLD if lit else TEAL))
        if lab:
            o.append('<text x="%.1f" y="%d" text-anchor="middle" font-size="22" font-family="Georgia, serif" '
                     'fill="%s" font-weight="%s">%s</text>'
                     % (x, 52 - row * 28, DEEP if lit else "#5A6862", "700" if lit else "400", lab))
        o.append('<text x="%.1f" y="%d" text-anchor="middle" font-size="20" font-family="Georgia, serif" '
                 'fill="#5A6862">%d</text>' % (x, 126 + row * 26, yr))
    o.append("</svg>")
    return "\n".join(o)


def render(svg, name, height):
    os.makedirs(OUT, exist_ok=True)
    tmp = os.path.join(OUT, "_%s.svg" % name)
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(svg)
    png = os.path.join(OUT, "%s.png" % name)
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    "--default-background-color=00000000",
                    "--window-size=%d,%d" % (int(W if height > 400 else 1800), height),
                    "--screenshot=%s" % png, "file:///" + tmp.replace("\\", "/")],
                   check=False, capture_output=True)
    os.remove(tmp)
    return png, os.path.getsize(png)


MAPS = {
    # session 1 — the whole sweep, one arrow per era
    "s1_sweep": dict(layers=[
        arrow("madina", "dimashq", MAROON, 0.16),
        arrow("dimashq", "qurtuba", MAROON, 0.14),
        arrow("dimashq", "sindh", MAROON, -0.12),
        arrow("baghdad", "qustantiniyya", TEAL, 0.18),
    ], extra_dots=[dot("sindh", "Sindh", TEAL, 8, "below")],
        caption="Fourteen centuries, one map"),

    # session 2 — the twelve years
    "s2_twelve": dict(layers=[
        arrow("madina", "yamama", MAROON, 0.10),
        arrow("madina", "yarmuk", MAROON, 0.18),
        arrow("madina", "qadisiyya", MAROON, -0.16),
        arrow("madina", "fustat", MAROON, 0.20),
    ], extra_dots=[
        dot("yamama", "Yamama", MAROON, 8, "below"),
        dot("yarmuk", "Yarmuk", MAROON, 8, "below"),      # 'above' collided with Damascus
        dot("qadisiyya", "Qadisiyya", MAROON, 8, "below"),
        dot("fustat", "Fustat", MAROON, 8, "above"),
    ], caption="632\u2013644: twelve years"),

    "blank": dict(layers=[], extra_dots=[], caption=None),
}

LINES = {
    "line_full": (None, None),
    "line_s1": (632, 1947),
    "line_s2": (632, 644),
    "line_s3": (644, 661),
    "line_s4": (661, 750),
    "line_s5": (750, 1492),
    "line_s6": (1099, 1260),
    "line_s7": (1299, 1924),
    "line_s8": (711, 1707),
    "line_s9": (1857, 1947),
}

if __name__ == "__main__":
    for name, cfg in MAPS.items():
        p, sz = render(map_svg(**cfg), "map_" + name, int(H))
        print("%-22s %7.1f KB" % (os.path.basename(p), sz / 1024))
    for name, (lo, hi) in LINES.items():
        p, sz = render(line_svg(lo, hi), name, 190)
        print("%-22s %7.1f KB" % (os.path.basename(p), sz / 1024))
