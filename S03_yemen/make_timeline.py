# -*- coding: utf-8 -*-
"""Evening 3 — render the Line from timeline.json, one PNG per bookend.

    python S03_yemen/make_timeline.py                           # all three, default text size (1.5)
    python S03_yemen/make_timeline.py --text 1.8                # all three, bigger still
    python S03_yemen/make_timeline.py --text 1.8 --only line_s03_open

Writes S03_yemen/visuals/line_s03_open.png, line_s03_stop_a.png, line_s03_stop_b.png. Paste one into a
slide by hand, or re-run S03_yemen/build.py, which picks the same files up.

THE SOURCE OF TRUTH IS timeline.json — every event, its date band, its order, its lane, and which
render lights it. Edit a label or a date there; this file only draws.

WHY NOT series/make_visuals.line_svg. The series Line runs 632–1947 CE; at that scale the whole of
this evening is one pixel. Evening 3 needs months, and the sources do not give months reliably — they
give "10 AH", "after Ḥajjat al-Wadāʿ", "some nights before, or one night". So this Line is drawn in
DATE BANDS with events in their stated ORDER inside each band. Horizontal distance inside a band means
"came after", never "how long after". That is the honest scale for what we can actually source.

Two lanes, because the evening is a flashback: Medina and Najd on top (where evening 2 left the room,
at Buzākha), Yemen below (tonight). The flashback arrow runs from Buzākha back to the killing in Ṣanʿāʾ.

TEXT SIZE. `--text` multiplies every type size (1.0 = the original). At 1.3 and above each event and band
uses its "short" label from timeline.json, labels cycle through four rows instead of two, and the image
grows taller; labels are never cut off. The width stays fixed. The slide fits the image to its width, or
to its height if the image is too tall — so past about 2.0 the image gets tall enough to be scaled down
again and nothing is gained. If a label collides, shorten its "short" form in timeline.json.

Nothing on the image is apparatus (DECISIONS.md #30): no certainty labels, no card ids.
"""
import argparse
import json
import os
import subprocess
import textwrap
from xml.sax.saxutils import escape

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "visuals")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
INK, TEAL, DEEP, GOLD, MAROON, MUTED = "#1C2321", "#104A43", "#0A322E", "#C49A45", "#7A2E2E", "#8A948F"
W = 1800                                    # canvas width in px; --width overrides
FONT = "Georgia, 'Times New Roman', serif"


def honorifics(t):
    """ؓ and ﷺ are Arabic marks with no glyph in Georgia; set them in Traditional Arabic."""
    t = escape(t)
    for mark in ("\u0613", "\ufdfa"):
        t = t.replace(mark, '<tspan font-family="Traditional Arabic" font-size="1.35em">%s</tspan>' % mark)
    return t


def svg(data, render, text=1.0, width=W):
    ev = sorted(data["events"], key=lambda e: e["order"])
    lit = set(render["lit"])

    big = text >= 1.3                                 # large text uses each label's "short" form
    lab = lambda o: o.get("short", o["label"]) if big else o["label"]
    fs = 17 * text                                    # event label size
    lh = fs * 1.2                                     # its line height
    wrap = min(16, max(12, int(round(24 / text)))) if big else 16   # characters per label line
    rows = 4 if big else 2                            # label rows per lane, cycled (four keep neighbours apart)
    blocks = {e["id"]: textwrap.wrap(lab(e), wrap) for e in ev}     # never truncated
    block_h = max(len(v) for v in blocks.values()) * lh
    gap = block_h + 10 * text                         # vertical step between label rows
    head_fs = 19 * text
    lane_fs = 21 * text
    left, right = int(175 * min(text, 1.6)), 80

    # a band's width is its event count, but never less than 1.8 slots (more at large text), so a
    # one-event band can hold its own header; events sit evenly inside their band, in stated order
    bands = [b for b in data["bands"] if any(e["band"] == b["id"] for e in ev)]
    weight = {b["id"]: max(1.8 * max(1.0, text * 0.8), float(sum(1 for e in ev if e["band"] == b["id"])))
              for b in bands}
    slot = (width - left - right) / sum(weight.values())
    x, span, cur = {}, {}, float(left)
    for b in bands:
        mine = [e for e in ev if e["band"] == b["id"]]
        w = weight[b["id"]] * slot
        span[b["id"]] = (cur, cur + w)
        for i, e in enumerate(mine):
            x[e["id"]] = cur + w * (i + 0.5) / len(mine)
        cur += w
    # band headers wrap to their band's own width, so a wide band keeps its label on one line
    heads = {b["id"]: textwrap.wrap(lab(b), max(6, int((span[b["id"]][1] - span[b["id"]][0])
                                                       / (head_fs * 0.56)))) for b in bands}
    head_h = max(len(v) for v in heads.values()) * head_fs * 1.15 + 20

    medina_y = head_h + 30 + 22 * text + (rows - 1) * gap + block_h
    yemen_y = medina_y + 130 * max(1.0, text * 0.75)
    height = int(yemen_y + 34 * text + (rows - 1) * gap + block_h + 30)
    lane_y = {"medina": medina_y, "yemen": yemen_y}

    o = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d">'
         % (width, height, width, height),
         '<rect width="%d" height="%d" fill="#FFFFFF"/>' % (width, height)]

    # date bands: a header over the columns their events occupy
    for bi, b in enumerate(bands):
        x0, x1 = span[b["id"]]
        o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s"/>'
                 % (x0 + 2, head_h, x1 - x0 - 4, height - head_h - 12,
                    "#FAF7F0" if bi % 2 == 0 else "#F2EDE1"))
        hl = heads[b["id"]]
        for k, t in enumerate(hl):
            o.append('<text x="%.1f" y="%.1f" text-anchor="middle" font-size="%.1f" font-family="%s" '
                     'font-weight="700" fill="%s">%s</text>'
                     % ((x0 + x1) / 2, head_h - 12 - (len(hl) - 1 - k) * head_fs * 1.15, head_fs,
                        FONT, DEEP, honorifics(t)))

    # lanes
    for lane in data["lanes"]:
        y = lane_y[lane["id"]]
        o.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="%.1f"/>'
                 % (left - 10, y, width - right, y, TEAL, 3 * text))
        ll = textwrap.wrap(lane["label"], width=9)
        for k, t in enumerate(ll):
            o.append('<text x="%d" y="%.1f" text-anchor="end" font-size="%.1f" font-family="%s" '
                     'font-weight="700" fill="%s">%s</text>'
                     % (left - 20, y + lane_fs * 0.35 + (k - (len(ll) - 1) / 2.0) * lane_fs * 1.15,
                        lane_fs, FONT, TEAL, escape(t)))

    # events: Medina labels above its lane, Yemen labels below, cycling through the label rows
    count = {"medina": 0, "yemen": 0}
    for e in ev:
        on = e["group"] in lit
        cx, cy = x[e["id"]], lane_y[e["lane"]]
        r = count[e["lane"]] % rows
        count[e["lane"]] += 1
        if e["group"] == "later":
            o.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#FFFFFF" stroke="%s" stroke-width="2.5"/>'
                     % (cx, cy, 8 * text, MUTED))
        else:
            o.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/>'
                     % (cx, cy, (11 if on else 7) * text, GOLD if on else TEAL))
        ls = blocks[e["id"]]
        colour, weight_ = (INK, "700") if on else (MUTED, "400")
        if e["lane"] == "medina":
            base = cy - 22 * text - r * gap - (len(ls) - 1) * lh
            tick_end = cy - 22 * text - r * gap + fs * 0.3
        else:
            base = cy + 34 * text + r * gap
            tick_end = base - fs
        o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#C9C2B2" stroke-width="1"/>'
                 % (cx, cy, cx, tick_end))
        for k, t in enumerate(ls):
            o.append('<text x="%.1f" y="%.1f" text-anchor="middle" font-size="%.1f" font-family="%s" '
                     'font-weight="%s" fill="%s">%s</text>'
                     % (cx, base + k * lh, fs, FONT, weight_, colour, honorifics(t)))

    if render.get("flashback"):
        bx, ax = x["m05"], x["y07"]
        y0, y1 = medina_y + 14 * text, yemen_y - 14 * text
        m = 22 * text
        o.append('<defs><marker id="ah" markerUnits="userSpaceOnUse" markerWidth="%.1f" markerHeight="%.1f" '
                 'refX="%.1f" refY="%.1f" orient="auto"><path d="M0,0 L%.1f,%.1f L0,%.1f z" fill="%s"/>'
                 '</marker></defs>' % (m, m, m * 0.72, m / 2, m, m / 2, m, MAROON))
        o.append('<path d="M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" '
                 'stroke-width="%.1f" stroke-dasharray="10 7" marker-end="url(#ah)"/>'
                 % (bx, y0, bx, (y0 + y1) / 2, ax, (y0 + y1) / 2, ax, y1, MAROON, 3.5 * text))
        o.append('<text x="%.1f" y="%.1f" text-anchor="middle" font-size="%.1f" font-family="%s" '
                 'font-style="italic" fill="%s">back to Yemen</text>'
                 % ((bx + ax) / 2, (y0 + y1) / 2 - 8 * text, 19 * text, FONT, MAROON))
    o.append("</svg>")
    return "\n".join(o), width, height


def render_png(svg_text, name, width, height):
    os.makedirs(OUT, exist_ok=True)
    tmp = os.path.join(OUT, "_%s.html" % name)
    with open(tmp, "w", encoding="utf-8") as f:
        f.write('<!doctype html><meta charset="utf-8"><style>html,body{margin:0;background:#fff}</style>'
                + svg_text)
    png = os.path.join(OUT, name + ".png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    "--window-size=%d,%d" % (width, height), "--screenshot=%s" % png,
                    "file:///" + tmp.replace("\\", "/")], check=False, capture_output=True)
    os.remove(tmp)
    return png


def build(text=1.5, width=W, only=None):
    data = json.load(open(os.path.join(HERE, "timeline.json"), encoding="utf-8"))
    ids = {e["id"] for e in data["events"]}
    for need in ("m05", "y07"):
        assert need in ids, "flashback anchor %s missing from timeline.json" % need
    out = []
    for r in data["renders"]:
        if only and r["name"] not in only:
            continue
        svg_text, w, h = svg(data, r, text, width)
        out.append(render_png(svg_text, r["name"], w, h))
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Render the evening-3 Line images from timeline.json.")
    ap.add_argument("--text", type=float, default=1.5,
                    help="text size multiplier: 1.0 = small original, 1.5 = default, 1.8 = largest useful")
    ap.add_argument("--width", type=int, default=W, help="canvas width in px (default %d)" % W)
    ap.add_argument("--only", nargs="*", help="render only these, e.g. line_s03_open")
    a = ap.parse_args()
    for p in build(a.text, a.width, a.only):
        print("  %s   %.1f KB" % (p, os.path.getsize(p) / 1024.0))
