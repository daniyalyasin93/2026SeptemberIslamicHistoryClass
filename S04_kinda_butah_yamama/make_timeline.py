# -*- coding: utf-8 -*-
"""Evening 4 — render the Line from timeline.json, one PNG per closing stop.

    python S04_kinda_butah_yamama/make_timeline.py                        # all three, default text size (1.5)
    python S04_kinda_butah_yamama/make_timeline.py --text 1.8             # bigger still
    python S04_kinda_butah_yamama/make_timeline.py --only line_s04_stop_c

Writes S04_kinda_butah_yamama/visuals/line_s04_stop_a.png, line_s04_stop_b.png, line_s04_stop_c.png, and
deletes each one's stale .trim.png cache so the next deck build re-trims it. build.py picks the files up.

It does NOT write visuals/line_s04_open.png. That file is evening 3's line_s03_stop_b.png, byte for byte
(the bookend-IN rule, DECISIONS.md #23) and must never be redrawn here.

THE SOURCE OF TRUTH IS timeline.json — every event, its date band, its column, its lane, and which
render lights it. Edit a label or a date there; this file only draws.

Adapted from S03_yemen/make_timeline.py, and drawn in the same language so the evening-4 closing
Lines read as the continuation of the evening-4 opening one: DATE BANDS, events in stated ORDER inside
a band, horizontal distance meaning "came after" and never "how long after". What is new:

  * ANY NUMBER OF LANES, top to bottom as timeline.json lists them (evening 3 hard-coded two).
  * COLUMNS. An event's `col` is its step inside its band. Two events on different lanes that share a
    column are events the cards do not order against each other. Evening 3 had one global order and
    so had to put one of two unordered events first; this does not.
  * LABELS ABOVE OR BELOW their lane (`side`; default: the top lane above, every other lane below), and
    label rows assigned automatically so neighbours never touch.
  * LINKS in place of evening 3's single hard-wired flashback arrow: any number of arrows between two
    events, each drawn only once its `when_lit` group is lit.
  * Wrapping by MEASURED WIDTH (PIL, the same Georgia the browser draws with) instead of character
    counts, and a COLLISION CHECK: labels, headers and arrows are tested against each other and the
    canvas edge, and the script exits non-zero on any overlap. Look at the PNG as well.

STYLES. A lit group draws gold and bold. The group "delivered" (an earlier evening) draws as a small
teal dot with a muted label. Every other unlit group — tonight's later parts at STOP A and B, and
"later" (rolled to evening 5) — draws hollow: still to come.

TEXT SIZE. `--text` multiplies every type size (1.0 = S03's original). At 1.3 and above each event and band
uses its "short" label. The width stays fixed; the height follows from the label rows.

Nothing on the image is apparatus (DECISIONS.md #30): no certainty labels, no card ids, no notes.
"""
import argparse
import json
import os
import subprocess
import sys
from xml.sax.saxutils import escape

# a Windows console is cp1252: "→", "ؓ" and the Arabic in a progress line would crash the run
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "visuals")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
FONTS = r"C:\Windows\Fonts"
INK, TEAL, DEEP, GOLD, MAROON, MUTED = "#1C2321", "#104A43", "#0A322E", "#C49A45", "#7A2E2E", "#8A948F"
W = 1800                                    # canvas width in px; --width overrides
FONT = "Georgia, 'Times New Roman', serif"
RADI, SALLA = "\u0613", "\ufdfa"  # the two honorifics: no glyph in Georgia; set in Traditional Arabic
MARKS = (RADI, SALLA)
MARK_EM = 1.35

try:
    from PIL import ImageFont
except ImportError:                          # measuring falls back to an average glyph width
    ImageFont = None
_font_cache = {}


def _font(kind, size):
    """PIL font for measuring: kind is 'reg', 'bold', 'ital' or 'arabic'."""
    if ImageFont is None:
        return None
    key = (kind, round(size * 4))
    if key not in _font_cache:
        name = {"reg": "georgia.ttf", "bold": "georgiab.ttf", "ital": "georgiai.ttf",
                "arabic": "trado.ttf"}[kind]
        _font_cache[key] = ImageFont.truetype(os.path.join(FONTS, name), max(1, int(round(size))))
    return _font_cache[key]


def measure(t, size, kind="bold"):
    """Rendered width of one line in px, honorific marks measured in Traditional Arabic as honorifics()
    sets them (ؓ carries its own no-break space, which replaces the space before it)."""
    if ImageFont is None:
        return len(t) * size * (0.56 if kind == "bold" else 0.52)
    t = t.replace(" " + RADI, RADI)
    w, run = 0.0, ""
    for ch in t:
        if ch in MARKS:
            w += _font(kind, size).getlength(run) if run else 0.0
            w += _font("arabic", size * MARK_EM).getlength("\u00a0" + ch if ch == RADI else ch)
            run = ""
        else:
            run += ch
    return w + (_font(kind, size).getlength(run) if run else 0.0)


def wrap(t, size, max_w, kind="bold"):
    """Greedy word wrap by measured width. Never truncates; a single over-long word gets its own line."""
    lines, cur = [], ""
    for word in t.split():
        trial = (cur + " " + word).strip()
        if cur and measure(trial, size, kind) > max_w:
            lines.append(cur)
            cur = word
        else:
            cur = trial
    if cur:
        lines.append(cur)
    # a mark that wrapped onto a line by itself belongs with the word before it
    fixed = []
    for ln in lines:
        if fixed and ln in MARKS:
            fixed[-1] += " " + ln
        elif fixed and ln.split()[0] in MARKS:
            fixed[-1] += " " + ln.split()[0]
            rest = ln.split(None, 1)[1] if len(ln.split()) > 1 else ""
            if rest:
                fixed.append(rest)
        else:
            fixed.append(ln)
    return fixed


def honorifics(t):
    """ؓ and ﷺ are Arabic marks with no glyph in Georgia; set them in Traditional Arabic.

    ؓ is a combining mark, and Traditional Arabic hangs it as high as it would sit over an Arabic
    letter — at 1.35em that is a whole line up, so on a wrapped label the mark of line 2 drew beside
    line 1 (evening 3's Line has exactly that defect at "al-Muhājir ؓ"). Here it is carried on its own
    no-break space and shifted down to sit as a superscript after the name. ﷺ is a spacing glyph and
    sits on the baseline as it is.
    """
    t = escape(t).replace(" " + RADI, RADI)
    t = t.replace(RADI, '<tspan font-family="Traditional Arabic" font-size="%.2fem" baseline-shift="-0.3em">'
                  '\u00a0%s</tspan>' % (MARK_EM, RADI))
    t = t.replace(SALLA, '<tspan font-family="Traditional Arabic" font-size="%.2fem">%s</tspan>'
                  % (MARK_EM, SALLA))
    return t


def _overlap(a, b, pad=0.0):
    return not (a[2] + pad <= b[0] or b[2] + pad <= a[0] or a[3] + pad <= b[1] or b[3] + pad <= a[1])


def layout(data, render, text=1.5, width=W):
    """Place every band, lane, event label and link. Returns a dict the drawing pass reads."""
    lanes = [l["id"] for l in data["lanes"]]
    lit = set(render["lit"])
    # tonight's parts not yet told at this stop are not drawn at all: at STOP A a hollow "ʿIkrima ؓ and
    # Shuraḥbīl ؓ beaten" or "The line breaks" told the room what it had not heard (#23: tonight's events
    # lit, and nothing else). Earlier evenings stay, and so does "later" — Ḥaḍramawt, already grey.
    ev = sorted((e for e in data["events"] if e["group"] in lit or e["group"] in ("delivered", "later")),
                key=lambda e: e["order"])
    big = text >= 1.3
    lab = lambda o: o.get("short", o["label"]) if big else o["label"]

    fs = 17 * text                                    # event label size
    lh = fs * 1.2                                     # its line height
    head_fs, lane_fs, link_fs = 19 * text, 21 * text, 17 * text
    left, right = int(175 * min(text, 1.6)), 60
    tick = 20 * text                                  # dot-to-label distance
    rgap = 12 * text                                  # vertical gap between two label rows on one side
    lane_gap = 34 * text                              # clear space between one lane's labels and the next's

    # --- bands and columns: a band is as wide as its column count, never less than its min_slots ---
    bands = [b for b in data["bands"] if any(e["band"] == b["id"] for e in ev)]
    ncols = {b["id"]: max(e["col"] for e in ev if e["band"] == b["id"]) for b in bands}
    weight = {b["id"]: max(float(b.get("min_slots", 1.8)), float(ncols[b["id"]])) for b in bands}
    slot = (width - left - right) / sum(weight.values())
    span, cur = {}, float(left)
    for b in bands:
        span[b["id"]] = (cur, cur + weight[b["id"]] * slot)
        cur += weight[b["id"]] * slot
    x = {}
    for e in ev:
        x0, x1 = span[e["band"]]
        x[e["id"]] = x0 + (x1 - x0) * (e["col"] - 0.5) / ncols[e["band"]]

    # band headers wrap to their band's own width
    heads = {b["id"]: wrap(lab(b), head_fs, span[b["id"]][1] - span[b["id"]][0] - 16) for b in bands}
    head_h = max(len(v) for v in heads.values()) * head_fs * 1.15 + 18 * text

    # --- labels: wrap to two columns' width, so labels one column apart can sit in alternate rows ---
    # (an event with room around it may take `wrap_slots` columns instead; the collision check has the last word)
    side, block, bw = {}, {}, {}
    for e in ev:
        li = lanes.index(e["lane"])
        side[e["id"]] = e.get("side", "above" if li == 0 else "below")
        max_w = max(float(e.get("wrap_slots", 2)) * slot - 14 * text, 6 * fs)
        block[e["id"]] = wrap(lab(e), fs, max_w)
        bw[e["id"]] = max(measure(t, fs) for t in block[e["id"]])
    bh = lambda eid: (len(block[eid]) - 1) * lh + fs * 1.05    # ink height of a label block

    # rows: per lane and side, in x order, the lowest row whose labels this one does not touch
    row, rows_used = {}, {}
    for ln in lanes:
        for sd in ("above", "below"):
            placed = []                                           # (row, x0, x1)
            for e in sorted((e for e in ev if e["lane"] == ln and side[e["id"]] == sd),
                            key=lambda e: x[e["id"]]):
                if "row" in e:
                    r = e["row"]
                else:
                    x0, x1 = x[e["id"]] - bw[e["id"]] / 2, x[e["id"]] + bw[e["id"]] / 2
                    r = 0
                    while any(pr == r and not (x1 + 18 * text <= px0 or px1 + 18 * text <= x0)
                              for pr, px0, px1 in placed):
                        r += 1
                row[e["id"]] = r
                placed.append((r, x[e["id"]] - bw[e["id"]] / 2, x[e["id"]] + bw[e["id"]] / 2))
            rows_used[(ln, sd)] = max([p[0] for p in placed], default=-1) + 1
    step = max(bh(e["id"]) for e in ev) + rgap                  # one label row

    def extent(ln, sd):
        mine = [e["id"] for e in ev if e["lane"] == ln and side[e["id"]] == sd]
        if not mine:
            return 14 * text                                     # the dot's own radius and a margin
        return max(tick + row[i] * step + bh(i) for i in mine)

    lane_y, y = {}, head_h + 16 * text
    for k, ln in enumerate(lanes):
        y += extent(ln, "above") if k == 0 else extent(lanes[k - 1], "below") + lane_gap + extent(ln, "above")
        lane_y[ln] = y
    height = int(lane_y[lanes[-1]] + extent(lanes[-1], "below") + 22 * text)

    # label boxes (x0, y0, x1, y1), clamped inside the canvas
    boxes = {}
    for e in ev:
        i, cy = e["id"], lane_y[e["lane"]]
        cx = min(max(x[i], bw[i] / 2 + 6), width - bw[i] / 2 - 6)
        if side[i] == "above":
            y1 = cy - tick - row[i] * step
            boxes[i] = (cx - bw[i] / 2, y1 - bh(i), cx + bw[i] / 2, y1)
        else:
            y0 = cy + tick + row[i] * step
            boxes[i] = (cx - bw[i] / 2, y0, cx + bw[i] / 2, y0 + bh(i))

    # links: drawn once their group is lit
    links = []
    for L in data.get("links", []):
        if L.get("when_lit") and L["when_lit"] not in lit:
            continue
        a, b = L["from"], L["to"]
        ea = next(e for e in ev if e["id"] == a)
        eb = next(e for e in ev if e["id"] == b)
        links.append(dict(L, x1=x[a], y1=lane_y[ea["lane"]], x2=x[b], y2=lane_y[eb["lane"]]))

    return dict(ev=ev, lit=lit, lab=lab, fs=fs, lh=lh, head_fs=head_fs, lane_fs=lane_fs, link_fs=link_fs,
                left=left, right=right, tick=tick, text=text, width=width, height=height, bands=bands,
                span=span, heads=heads, head_h=head_h, x=x, lanes=lanes, lane_y=lane_y, side=side,
                block=block, bw=bw, boxes=boxes, links=links, lane_gap=lane_gap)


def _link_path(L, g):
    """SVG path for a link, plus sample points along it for the collision check."""
    t, r = g["text"], 13 * g["text"]
    x1, y1, x2, y2 = L["x1"], L["y1"], L["x2"], L["y2"]
    down = 1 if y2 > y1 else -1
    y1, y2 = y1 + down * r, y2 - down * (r + 2 * t)
    if L.get("route") == "corridor":
        # down a little, along a corridor just clear of the upper lane's dots, then down onto the target
        yc = y1 + down * 12 * t
        rad = 14 * t
        sx = 1 if x2 > x1 else -1
        d = ("M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f"
             % (x1, y1, x1, yc - down * rad, x1, yc, x1 + sx * rad, yc, x2 - sx * rad, yc,
                x2, yc, x2, yc + down * rad, x2, y2))
        pts = ([(x1, y1 + (yc - y1) * k / 10.0) for k in range(11)]
               + [(x1 + (x2 - x1) * k / 30.0, yc) for k in range(31)]
               + [(x2, yc + (y2 - yc) * k / 20.0) for k in range(21)])
    else:
        ym = (y1 + y2) / 2
        d = "M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f" % (x1, y1, x1, ym, x2, ym, x2, y2)
        pts = []
        for k in range(41):
            s = k / 40.0
            px = (1 - s) ** 3 * x1 + 3 * (1 - s) ** 2 * s * x1 + 3 * (1 - s) * s ** 2 * x2 + s ** 3 * x2
            py = (1 - s) ** 3 * y1 + 3 * (1 - s) ** 2 * s * ym + 3 * (1 - s) * s ** 2 * ym + s ** 3 * y2
            pts.append((px, py))
    return d, pts


def _link_label(L, g, pts):
    """Link label, set beside the start of the arrow on the side away from the target."""
    if not L.get("label"):
        return None
    t = g["text"]
    w = measure(L["label"], g["link_fs"], "ital")
    sx = 1 if L["x2"] > L["x1"] else -1
    down = 1 if L["y2"] > L["y1"] else -1
    ax = L["x1"] - sx * 10 * t                       # just behind the arrow's start
    ay = L["y1"] + down * (g["tick"] + g["link_fs"] * 1.0)
    x0 = ax - w if sx > 0 else ax
    return dict(x=ax, y=ay, anchor="end" if sx > 0 else "start",
                box=(x0, ay - g["link_fs"] * 0.8, x0 + w, ay + g["link_fs"] * 0.25))


def check(g, name):
    """Every label, header, link label and arrow against every other and the canvas edge."""
    problems = []
    W_, H_ = g["width"], g["height"]
    items = [("label " + i, b) for i, b in g["boxes"].items()]
    for b in g["bands"]:
        x0, x1 = g["span"][b["id"]]
        for k, t in enumerate(g["heads"][b["id"]]):
            w = measure(t, g["head_fs"])
            if w > x1 - x0 - 4:
                problems.append("band header '%s' is wider than its band" % t)
    for L in g["links"]:
        d, pts = _link_path(L, g)
        lb = _link_label(L, g, pts)
        if lb:
            items.append(("link label %s>%s" % (L["from"], L["to"]), lb["box"]))
        for nm, bx in items:
            if nm.startswith("label ") and nm[6:] in (L["from"], L["to"]):
                continue
            if nm.startswith("link label %s>%s" % (L["from"], L["to"])):
                continue
            if any(bx[0] - 4 <= px <= bx[2] + 4 and bx[1] - 4 <= py <= bx[3] + 4 for px, py in pts):
                problems.append("arrow %s>%s crosses %s" % (L["from"], L["to"], nm))
    for k, (n1, b1) in enumerate(items):
        if b1[0] < 2 or b1[2] > W_ - 2 or b1[1] < g["head_h"] or b1[3] > H_ - 2:
            problems.append("%s runs off the canvas or into the band headers %s" % (n1, tuple(round(v) for v in b1)))
        for n2, b2 in items[k + 1:]:
            if _overlap(b1, b2, pad=6):
                problems.append("%s overlaps %s" % (n1, n2))
    # a label must not sit on another lane's line
    for i, b in g["boxes"].items():
        for ln, y in g["lane_y"].items():
            if b[1] - 4 <= y <= b[3] + 4:
                problems.append("label %s sits on the %s lane" % (i, ln))
    for p in problems:
        print("  COLLISION in %s: %s" % (name, p))
    return problems


def svg(data, render, text=1.5, width=W):
    g = layout(data, render, text, width)
    ev, lit, x, lane_y, t = g["ev"], g["lit"], g["x"], g["lane_y"], text
    width, height, fs, lh = g["width"], g["height"], g["fs"], g["lh"]

    o = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d">'
         % (width, height, width, height),
         '<rect width="%d" height="%d" fill="#FFFFFF"/>' % (width, height)]

    # date bands: a shaded column under a header
    for bi, b in enumerate(g["bands"]):
        x0, x1 = g["span"][b["id"]]
        o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s"/>'
                 % (x0 + 2, g["head_h"], x1 - x0 - 4, height - g["head_h"] - 10,
                    "#FAF7F0" if bi % 2 == 0 else "#F2EDE1"))
        hl = g["heads"][b["id"]]
        for k, s in enumerate(hl):
            o.append('<text x="%.1f" y="%.1f" text-anchor="middle" font-size="%.1f" font-family="%s" '
                     'font-weight="700" fill="%s">%s</text>'
                     % ((x0 + x1) / 2, g["head_h"] - 12 * t - (len(hl) - 1 - k) * g["head_fs"] * 1.15,
                        g["head_fs"], FONT, DEEP, honorifics(s)))

    # lanes, with their names in the left margin
    for lane in data["lanes"]:
        y = lane_y[lane["id"]]
        o.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="%.1f"/>'
                 % (g["left"] - 10, y, width - g["right"] - 2, y, TEAL, 3 * t))
        ll = lane.get("lines") or wrap(lane["label"], g["lane_fs"], g["left"] - 34)
        for k, s in enumerate(ll):
            o.append('<text x="%d" y="%.1f" text-anchor="end" font-size="%.1f" font-family="%s" '
                     'font-weight="700" fill="%s">%s</text>'
                     % (g["left"] - 20, y + g["lane_fs"] * 0.35 + (k - (len(ll) - 1) / 2.0) * g["lane_fs"] * 1.15,
                        g["lane_fs"], FONT, TEAL, escape(s)))

    # links under the dots
    if g["links"]:
        m = 20 * t
        o.append('<defs><marker id="ah" markerUnits="userSpaceOnUse" markerWidth="%.1f" markerHeight="%.1f" '
                 'refX="%.1f" refY="%.1f" orient="auto"><path d="M0,0 L%.1f,%.1f L0,%.1f z" fill="%s"/>'
                 '</marker></defs>' % (m, m, m * 0.72, m / 2, m, m / 2, m, MAROON))
    for L in g["links"]:
        d, pts = _link_path(L, g)
        o.append('<path d="%s" fill="none" stroke="%s" stroke-width="%.1f" stroke-dasharray="10 7" '
                 'marker-end="url(#ah)"/>' % (d, MAROON, 3.2 * t))
        lb = _link_label(L, g, pts)
        if lb:
            o.append('<text x="%.1f" y="%.1f" text-anchor="%s" font-size="%.1f" font-family="%s" '
                     'font-style="italic" fill="%s">%s</text>'
                     % (lb["x"], lb["y"], lb["anchor"], g["link_fs"], FONT, MAROON, honorifics(L["label"])))

    # events: tick, dot, label
    for e in ev:
        i = e["id"]
        on = e["group"] in lit
        told = on or e["group"] == "delivered"
        cx, cy = x[i], lane_y[e["lane"]]
        bx0, by0, bx1, by1 = g["boxes"][i]
        above = g["side"][i] == "above"
        o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#C9C2B2" stroke-width="1.2"/>'
                 % (cx, cy, cx, (by1 + 2 * t) if above else (by0 - 2 * t)))
        if not told:
            o.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#FFFFFF" stroke="%s" stroke-width="%.1f"/>'
                     % (cx, cy, 8 * t, MUTED, 1.8 * t))
        else:
            o.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/>'
                     % (cx, cy, (11 if on else 7) * t, GOLD if on else TEAL))
        colour, weight_ = (INK, "700") if on else (MUTED, "400")
        ls = g["block"][i]
        tx = (bx0 + bx1) / 2
        first = (by1 - fs * 0.22 - (len(ls) - 1) * lh) if above else (by0 + fs * 0.80)
        for k, s in enumerate(ls):
            o.append('<text x="%.1f" y="%.1f" text-anchor="middle" font-size="%.1f" font-family="%s" '
                     'font-weight="%s" fill="%s">%s</text>'
                     % (tx, first + k * lh, fs, FONT, weight_, colour, honorifics(s)))
    o.append("</svg>")
    return "\n".join(o), g


def render_png(svg_text, name, width, height):
    os.makedirs(OUT, exist_ok=True)
    tmp = os.path.join(OUT, "_%s.html" % name)
    with open(tmp, "w", encoding="utf-8") as f:
        f.write('<!doctype html><meta charset="utf-8"><style>html,body{margin:0;background:#fff}</style>'
                + svg_text)
    png = os.path.join(OUT, name + ".png")
    before = os.path.getmtime(png) if os.path.exists(png) else 0
    proc = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                           "--window-size=%d,%d" % (width, height), "--screenshot=%s" % png,
                           "file:///" + tmp.replace("\\", "/")], check=False, capture_output=True)
    os.remove(tmp)
    if proc.returncode != 0 or not os.path.exists(png) or os.path.getmtime(png) <= before:
        # last week's PNG left in place would be reported as written and placed on the closing slide
        raise SystemExit("make_timeline: Chrome did not write %s (exit %s)." % (png, proc.returncode))
    trim = os.path.splitext(png)[0] + ".trim.png"      # deck2._trim's cache; stale once the PNG changes
    if os.path.exists(trim):
        os.remove(trim)
    return png


def validate(data):
    """The JSON's own promises: known lanes/bands/groups, cards and certainty on every event, links resolve."""
    lanes = {l["id"] for l in data["lanes"]}
    bands = {b["id"] for b in data["bands"]}
    ids = [e["id"] for e in data["events"]]
    assert len(ids) == len(set(ids)), "duplicate event id"
    groups = {g for r in data["renders"] for g in r["lit"]} | {"delivered", "later"}
    cells = set()
    for e in data["events"]:
        assert e["lane"] in lanes and e["band"] in bands, "event %s: unknown lane or band" % e["id"]
        assert e.get("cards") and e.get("when") and e.get("certainty"), "event %s: cards/when/certainty" % e["id"]
        assert e["group"] in groups, "event %s: group %s is lit by no render" % (e["id"], e["group"])
        cell = (e["band"], e["col"], e["lane"])
        assert cell not in cells, "event %s: two events in one lane share a column" % e["id"]
        cells.add(cell)
    for L in data.get("links", []):
        assert L["from"] in ids and L["to"] in ids, "link %s>%s: unknown event" % (L["from"], L["to"])
    for r in data["renders"]:
        assert r["name"] != "line_s04_open", "line_s04_open is evening 3's closing Line (DECISIONS #23)"


def build(text=1.5, width=W, only=None):
    data = json.load(open(os.path.join(HERE, "timeline.json"), encoding="utf-8"))
    validate(data)
    out, bad = [], 0
    for r in data["renders"]:
        if only and r["name"] not in only:
            continue
        svg_text, g = svg(data, r, text, width)
        bad += len(check(g, r["name"]))
        out.append((render_png(svg_text, r["name"], g["width"], g["height"]), g["width"], g["height"]))
    return out, bad


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Render the evening-4 Line images from timeline.json.")
    ap.add_argument("--text", type=float, default=1.5,
                    help="text size multiplier: 1.0 = S03's small original, 1.5 = default, 1.8 = largest useful")
    ap.add_argument("--width", type=int, default=W, help="canvas width in px (default %d)" % W)
    ap.add_argument("--only", nargs="*", help="render only these, e.g. line_s04_stop_c")
    a = ap.parse_args()
    files, bad = build(a.text, a.width, a.only)
    for p, w, h in files:
        print("  %s   %d x %d   %.1f KB" % (p, w, h, os.path.getsize(p) / 1024.0))
    if bad:
        print("  %d collision(s) - fix timeline.json (a 'short' label, a 'side', a 'col') and re-run" % bad)
        sys.exit(1)
