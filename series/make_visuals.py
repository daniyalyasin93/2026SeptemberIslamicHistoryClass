"""Generate the slide visuals: maps with movement drawn on them, and timeline strips.

    python series/make_visuals.py

Every content slide gets a picture. Two families:

  visuals/map_<name>.png       a map with this session's movement drawn on it
  visuals/line_s<N>.png        the timeline strip with this session's span lit

Maps come in two VIEWS so a regional story is not a smudge on a continental map:
  WORLD   -12..80 E, 8..50 N   — the whole span, six anchor cities
  ARABIA   33..60 E, 11..34 N  — the peninsula, for the Ridda and the early campaigns

Both are built as SVG and rendered through headless Chrome.
"""
import json
import math
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "visuals")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

INK, TEAL, DEEP, GOLD = "#1C2321", "#104A43", "#0A322E", "#C49A45"
SEA, LAND, COAST, MAROON = "#DCE8E6", "#EFEADC", "#B9C7C3", "#7A2E2E"


class View(object):
    def __init__(self, bbox, width, lat0=None):
        self.bbox = bbox
        self.w = float(width)
        self.lat0 = lat0 if lat0 is not None else (bbox[1] + bbox[3]) / 2.0
        self.k = math.cos(math.radians(self.lat0))
        self.sx = (bbox[2] - bbox[0]) * self.k
        self.sy = bbox[3] - bbox[1]
        self.h = self.w * self.sy / self.sx

    def px(self, lon, lat):
        return ((lon - self.bbox[0]) * self.k / self.sx * self.w,
                (self.bbox[3] - lat) / self.sy * self.h)


WORLD = View((-12.0, 8.0, 80.0, 50.0), 1800, 30.0)
ARABIA = View((33.0, 11.0, 60.0, 34.0), 1800, 23.0)

PLACES = {
    "makkah": (39.83, 21.42), "madina": (39.61, 24.47), "dimashq": (36.31, 33.51),
    "baghdad": (44.36, 33.31), "qurtuba": (-4.78, 37.88), "qustantiniyya": (28.98, 41.01),
    "yarmuk": (35.90, 32.70), "qadisiyya": (44.30, 31.70), "madain": (44.58, 33.10),
    "fustat": (31.24, 30.05), "yamama": (47.30, 24.10), "granada": (-3.60, 37.18),
    "dihli": (77.20, 28.61), "sindh": (67.30, 24.80), "ayn_jalut": (35.35, 32.55),
    "vienna": (16.37, 48.20), "samarqand": (66.96, 39.65), "qahira": (31.24, 30.05),
    # Ridda theatre
    "dhu_alqassa": (40.30, 24.30), "buzakha": (41.70, 27.50), "bahrain": (50.20, 26.20),
    "daba": (56.27, 25.63), "sanaa": (44.21, 15.35), "tihama_yemen": (43.30, 14.00),
    "mashariq_sham": (37.00, 31.00), "najran": (44.13, 17.49), "tabuk": (36.57, 28.38),
}
WORLD_ANCHORS = [
    ("makkah", "Makkah", "below"), ("madina", "Madina", "above"),
    ("dimashq", "Damascus", "above"), ("baghdad", "Baghdad", "below"),
    ("qurtuba", "C\u00f3rdoba", "above"), ("qustantiniyya", "Constantinople", "above"),
]
ARABIA_ANCHORS = [("makkah", "Makkah", "below"), ("madina", "Madina", "above")]

PEGS = [
    (632, "Rashidun"), (661, ""), (750, "Abbasids"), (1099, "Crusades"),
    (1258, "Baghdad falls"), (1453, "Constantinople"), (1924, "Caliphate ends"), (1947, ""),
]


def land_paths(view):
    src = os.path.join(HERE, "data", "ne_50m_land.geojson")
    with open(src, encoding="utf-8") as f:
        gj = json.load(f)
    b = view.bbox
    out = []
    for feat in gj["features"]:
        g = feat.get("geometry") or {}
        t = g.get("type")
        rings = (g.get("coordinates") or []) if t == "Polygon" else \
                [r for poly in (g.get("coordinates") or []) for r in poly] if t == "MultiPolygon" else []
        for ring in rings:
            if not any(b[0] - 10 <= x <= b[2] + 10 and b[1] - 10 <= y <= b[3] + 10 for x, y in ring):
                continue
            pts, last = [], None
            for lon, lat in ring:
                p = tuple(round(v, 1) for v in view.px(lon, lat))
                if p != last:
                    pts.append(p); last = p
            if len(pts) >= 3:
                out.append("M" + "L".join("%g %g" % p for p in pts) + "Z")
    return out


def arrow(view, a, b, colour=MAROON, bow=0.22, width=7):
    (x1, y1), (x2, y2) = view.px(*PLACES[a]), view.px(*PLACES[b])
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    dx, dy = x2 - x1, y2 - y1
    cx, cy = mx - dy * bow, my + dx * bow
    ang = math.atan2(y2 - cy, x2 - cx)
    s = 20
    p1 = (x2 - s * math.cos(ang - 0.42), y2 - s * math.sin(ang - 0.42))
    p2 = (x2 - s * math.cos(ang + 0.42), y2 - s * math.sin(ang + 0.42))
    return ('<path d="M%.1f %.1f Q%.1f %.1f %.1f %.1f" fill="none" stroke="%s" stroke-width="%d" '
            'stroke-linecap="round" opacity=".9"/>'
            '<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="%s"/>'
            % (x1, y1, cx, cy, x2, y2, colour, width, x2, y2, p1[0], p1[1], p2[0], p2[1], colour))


def dot(view, place, label=None, colour=TEAL, r=9, side="above", sub=None, size=26):
    x, y = view.px(*PLACES[place])
    o = ['<circle cx="%.1f" cy="%.1f" r="%d" fill="%s"/>' % (x, y, r, colour)]
    if label:
        dy = -(r + 15) if side == "above" else (r + 29)
        o.append('<text x="%.1f" y="%.1f" text-anchor="middle" font-size="%d" font-weight="600" '
                 'font-family="Georgia, serif" fill="%s">%s</text>' % (x, y + dy, size, DEEP, label))
        if sub:
            o.append('<text x="%.1f" y="%.1f" text-anchor="middle" font-size="%d" '
                     'font-family="Georgia, serif" font-style="italic" fill="%s">%s</text>'
                     % (x, y + dy + (-int(size * .82) if side == "above" else int(size * .95)),
                        int(size * .72), MAROON, sub))
    return "".join(o)


def map_svg(view, layers=(), dots=(), caption=None, anchors=None):
    anchors = WORLD_ANCHORS if anchors is None else anchors
    o = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %g %g">' % (view.w, view.h),
         '<rect width="%g" height="%g" fill="%s"/>' % (view.w, view.h, SEA),
         '<g fill="%s" stroke="%s" stroke-width="1.1" stroke-linejoin="round">' % (LAND, COAST)]
    o += ['<path d="%s"/>' % d for d in land_paths(view)]
    o.append("</g>")
    o += list(layers)
    for key, lab, side in anchors:
        o.append(dot(view, key, lab, TEAL, 9, side))
    o += list(dots)
    if caption:
        o.append('<text x="34" y="%g" font-size="30" font-family="Georgia, serif" fill="%s" '
                 'font-style="italic">%s</text>' % (view.h - 30, DEEP, caption))
    o.append("</svg>")
    return "\n".join(o)


def line_svg(lo=None, hi=None):
    w, h, m = 1800.0, 190.0, 70.0
    span = 1947 - 632
    X = lambda y: m + (y - 632) / span * (w - 2 * m)
    o = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %g %g">' % (w, h),
         '<rect width="%g" height="%g" fill="#FAF7F0"/>' % (w, h)]
    if lo is not None:
        o.append('<rect x="%.1f" y="76" width="%.1f" height="26" fill="%s" opacity=".30"/>'
                 % (X(lo), max(6.0, X(hi) - X(lo)), GOLD))
    o.append('<line x1="%g" y1="89" x2="%g" y2="89" stroke="%s" stroke-width="3"/>' % (m, w - m, TEAL))
    STAGGER = {661: 1, 1947: 1}
    for yr, lab in PEGS:
        x, lit, row = X(yr), (lo is not None and lo <= yr <= hi), STAGGER.get(yr, 0)
        o.append('<circle cx="%.1f" cy="89" r="%d" fill="%s"/>' % (x, 9 if lit else 6, GOLD if lit else TEAL))
        if lab:
            o.append('<text x="%.1f" y="%d" text-anchor="middle" font-size="22" font-family="Georgia, serif" '
                     'fill="%s" font-weight="%s">%s</text>'
                     % (x, 52 - row * 28, DEEP if lit else "#5A6862", "700" if lit else "400", lab))
        o.append('<text x="%.1f" y="%d" text-anchor="middle" font-size="20" font-family="Georgia, serif" '
                 'fill="#5A6862">%d</text>' % (x, 126 + row * 26, yr))
    o.append("</svg>")
    return "\n".join(o)


def render(svg, name, w, h):
    os.makedirs(OUT, exist_ok=True)
    tmp = os.path.join(OUT, "_%s.svg" % name)
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(svg)
    png = os.path.join(OUT, "%s.png" % name)
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    "--window-size=%d,%d" % (int(w), int(h)),
                    "--screenshot=%s" % png, "file:///" + tmp.replace("\\", "/")],
                   check=False, capture_output=True)
    os.remove(tmp)
    return png, os.path.getsize(png)


def build_maps():
    W, A = WORLD, ARABIA
    out = {}

    out["s1_sweep"] = (W, map_svg(W, layers=[
        arrow(W, "madina", "dimashq", MAROON, 0.16),
        arrow(W, "dimashq", "qurtuba", MAROON, 0.14),
        arrow(W, "dimashq", "sindh", MAROON, -0.12),
        arrow(W, "baghdad", "qustantiniyya", TEAL, 0.18),
    ], dots=[dot(W, "sindh", "Sindh", TEAL, 8, "below")],
        caption="Fourteen centuries, one map"))

    # THE RIDDA — the columns going out, on the Arabian view.
    # Dhu al-Qassa is one march from Madina, so at this zoom the two labels collide; the origin
    # is drawn once, as Madina, with the staging point named in the sub-label instead.
    ridda_arrows = [
        ("madina", "buzakha", 0.10), ("madina", "yamama", -0.11),
        ("madina", "bahrain", -0.15), ("madina", "daba", -0.21),
        ("madina", "sanaa", 0.17), ("madina", "tihama_yemen", 0.27),
        ("madina", "mashariq_sham", 0.14),
    ]
    out["s2_ridda"] = (A, map_svg(A,
        layers=[arrow(A, a, b, MAROON, bow, 8) for a, b, bow in ridda_arrows],
        dots=[
            dot(A, "madina", "MADINA", GOLD, 14, "above", "the eleven banners are tied here", 32),
            dot(A, "buzakha", "Buzakha", MAROON, 9, "above", "Tulayha", 28),
            dot(A, "yamama", "Yamama", MAROON, 11, "below", "Musaylima", 30),
            dot(A, "bahrain", "Bahrain", MAROON, 9, "below", "al-Ala' b. al-Hadrami", 26),
            dot(A, "daba", "Daba", MAROON, 9, "below", "Hudhayfa", 26),
            dot(A, "sanaa", "San'a", MAROON, 9, "below", "al-Muhajir", 26),
            dot(A, "tihama_yemen", "Tihama", MAROON, 9, "below", "Suwayd b. Muqarrin", 26),
            dot(A, "mashariq_sham", "Marches of Sham", MAROON, 9, "above", "Khalid b. Sa'id", 26),
        ],
        anchors=[("makkah", "Makkah", "below")],
        caption="632–633: eleven banners go out"))

    out["s2_twelve"] = (W, map_svg(W, layers=[
        arrow(W, "madina", "yarmuk", MAROON, 0.18),
        arrow(W, "madina", "qadisiyya", MAROON, -0.16),
        arrow(W, "madina", "fustat", MAROON, 0.20),
    ], dots=[
        dot(W, "yarmuk", "Yarmuk", MAROON, 8, "below"),
        dot(W, "qadisiyya", "Qadisiyya", MAROON, 8, "below"),
        dot(W, "fustat", "Fustat", MAROON, 8, "above"),
    ], caption="Then outward: Syria, Iraq, Egypt"))

    out["blank"] = (W, map_svg(W, caption=None))
    out["arabia_blank"] = (A, map_svg(A, anchors=ARABIA_ANCHORS, caption=None))
    return out


LINES = {"line_full": (None, None), "line_s1": (632, 1947), "line_s2": (632, 644),
         "line_s3": (644, 661), "line_s4": (661, 750), "line_s5": (750, 1492),
         "line_s6": (1099, 1260), "line_s7": (1299, 1924), "line_s8": (711, 1707),
         "line_s9": (1857, 1947)}

if __name__ == "__main__":
    for name, (view, svg) in build_maps().items():
        p, sz = render(svg, "map_" + name, view.w, view.h)
        print("%-24s %7.1f KB" % (os.path.basename(p), sz / 1024))
    for name, (lo, hi) in LINES.items():
        p, sz = render(line_svg(lo, hi), name, 1800, 190)
        print("%-24s %7.1f KB" % (os.path.basename(p), sz / 1024))
