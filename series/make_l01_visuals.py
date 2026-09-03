"""Session 1 visuals — the three nested timelines, the Medina clan chart, and the maps.

    python series/make_l01_visuals.py

Session 1 orients the room in TIME and then in SPACE, so almost every slide in the first half
is one of these pictures. See docs/specs/2026-09-03-L01-v3-spec.md.

THE NESTED TIMELINES are the load-bearing device. Each one shrinks to a shaded sliver at the
right-hand edge of the next, and a bracket joins the sliver to the panel it came from — so the
audience *watches* the scale change instead of being told about it:

    visuals/l01_tl1_pakistan.png    1947 -> now
    visuals/l01_tl2_ummah.png       622  -> now, with tl1 as a sliver.  Carries THE WHOLE ARC
    visuals/l01_tl3_prophets.png    -3000 -> now, with tl2 as a sliver
    visuals/l01_tl_stack.png        all three, for the worksheet

Timeline 3 is epistemically constrained and the picture has to say so. Our sources do NOT fix
dates for Adam, Nuh, Ibrahim, Musa or Dawud (alayhim al-salam). Anything shown there is a
conventional estimate from general scholarship, it is drawn hollow and labelled "approx.", and
Adam and Nuh go off-scale at the left edge behind a break mark with no number invented for them.
See DECISIONS.md #16 — the honest caption is a better teaching point than a fabricated date.

LANGUAGE: these are English-labelled on purpose. Urdu and Arabic go on the .pptx via deckkit,
where the font and complex-script runs are set properly; SVG text has no reliable bidi and
mixing scripts here is what mangled the first artifacts (CLAUDE.md 1.3). That includes the
honorifics: U+FDFA renders as a smudge at Georgia's size, so the labels here read "The Prophet
passes away" and the deck slide beside the image carries «وفاتِ نبی کریم ﷺ» properly set.
The honorific is never dropped from an audience-facing slide (CLAUDE.md 1.2) — only from the PNG.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_visuals import (ARABIA, COAST, DEEP, GOLD, INK, LAND, MAROON, OUT, SEA, TEAL,
                          View, arrow, dot, land_paths, map_svg, render)

CREAM = "#FAF7F0"
MUTED = "#5A6862"
FAINT = "#B9C7C3"
SERIF = "Georgia, 'Traditional Arabic', 'Times New Roman', serif"

# ---------------------------------------------------------------------------
# Certainty labels, exactly as docs/research/INDEX.md defines them.
#   "S"  [SOURCED]                 a page was read; it is in the research notes
#   "T"  [STANDARD]                conventional, not yet page-cited HERE -> (to verify)
#   "E"  [CONVENTIONAL-ESTIMATE]   general scholarship; our sources do not fix it
# Anything marked "E" is drawn hollow and captioned "approx." on the slide itself.
# ---------------------------------------------------------------------------

# --- Timeline 1: the room's own lifetime -----------------------------------
TL1 = [
    (1947, "Pakistan", "T"), (1956, "Constitution", "T"), (1965, "War", "T"),
    (1971, "Separation", "T"), (1977, "Zia", "T"), (1988, "Return to elections", "T"),
    (1998, "Nuclear tests", "T"), (2001, "9/11", "T"), (2010, "", "T"), (2026, "Tonight", "T"),
]

# --- Timeline 2: the whole arc. This is the only place the room sees all of it -
# (gregorian, label, hijri-or-None, certainty)
TL2 = [
    (622, "Hijra", 1, "T"),
    (632, "The Prophet passes away", 11, "S"),
    (661, "Umayyads", 41, "T"),
    (711, "Sindh and Spain", 92, "T"),
    (750, "Abbasids · Baghdad", 132, "T"),
    (929, "Córdoba", 316, "T"),
    (1099, "Crusades", 492, "T"),
    (1187, "Hattin", 583, "T"),
    (1258, "Baghdad falls", 656, "S"),
    (1260, "Ayn Jalut", 658, "T"),
    (1299, "Ottomans", 699, "T"),
    (1453, "Constantinople", 857, "T"),
    (1492, "Granada", 897, "T"),
    (1526, "Mughals", 932, "T"),
    (1857, "", None, "T"),
    (1924, "Caliphate ends", 1342, "T"),
    (1947, "Pakistan", None, "T"),
]

# --- Timeline 3: distance, not chronology ----------------------------------
# NOTHING here is claimed from our sources. Every entry is "E" and is drawn hollow.
# Adam and Nuh (as) carry no number at all and sit off-scale behind the break mark.
TL3 = [
    (-1900, "Ibrahim", "E", "conventional estimate"),
    (-1250, "Musa", "E", "conventional estimate"),
    (-1000, "Dawud · Sulayman", "E", "conventional estimate"),
    (1, "Isa", "E", "conventional estimate"),
    (622, "Hijra", "T", None),
    (2026, "Tonight", "T", None),
]
TL3_OFFSCALE = "Adam and Nuh — off this scale entirely, and no source fixes them"
TL3_HONORIFIC = "عليهم السلام"   # carried once, as its own Arabic run, at the foot of the panel

NOW = 2026


# ===========================================================================
# Timeline rendering
# ===========================================================================

def _frame(w, h):
    return ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %g %g">' % (w, h),
            '<rect width="%g" height="%g" fill="%s"/>' % (w, h, CREAM)]


def _txt(x, y, s, size=22, fill=MUTED, anchor="middle", weight="400", style="normal"):
    return ('<text x="%.1f" y="%.1f" text-anchor="%s" font-size="%d" font-family="%s" '
            'fill="%s" font-weight="%s" font-style="%s">%s</text>'
            % (x, y, anchor, size, SERIF, fill, weight, style, s))


def _yr(y):
    """Year label a lay reader can take in at a glance: 1947, 622, 1900 BC."""
    if y < 0:
        return "%d BC" % abs(y)
    return "1 CE" if y == 1 else "%d" % y


def _slots(xs, gap=190.0, nrows=3):
    """Assign each peg a (side, row) so no two label blocks ever overlap.

    Labels alternate ABOVE and BELOW the axis, and each side has `nrows` stagger rows — four
    slots in all. That is what makes the dense early centuries of the Ummah line readable;
    a single row of seventeen pegs is an unreadable smear, and the smear was the first thing
    wrong with this graphic.
    """
    slots = [(side, r) for r in range(nrows) for side in (-1, 1)]
    last = {s: -1e9 for s in slots}
    out = []
    for x in xs:
        pick = next((s for s in slots if x - last[s] >= gap),
                    min(slots, key=lambda s: last[s]))
        last[pick] = x
        out.append(pick)
    return out


def timeline_svg(pegs, lo, hi, title, subtitle=None, inset=None, inset_label=None,
                 offscale=None, caption=None, w=1800.0, h=700.0):
    """One panel. `inset` is the (lo, hi) span of the PREVIOUS timeline, drawn as a full-height
    shaded column at the right-hand edge — that column is the whole of the last slide."""
    m, axis = 96.0, 342.0
    top = 150.0
    bot = h - (86.0 if caption else 28.0)
    span = float(hi - lo)
    X = lambda y: m + (y - lo) / span * (w - 2 * m)
    o = _frame(w, h)

    o.append(_txt(m, 58, title, 40, DEEP, "start", "700"))
    if subtitle:
        o.append(_txt(m, 94, subtitle, 23, MUTED, "start", "400", "italic"))

    # The previous timeline, shrunk to a column. Drawn first so everything else sits on top;
    # full height rather than a bracket, which is what kept colliding with the peg labels.
    if inset:
        ix, iw = X(inset[0]), max(5.0, X(inset[1]) - X(inset[0]))
        o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" opacity=".20"/>'
                 % (ix, top, iw, bot - top, GOLD))
        o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="none" stroke="%s" '
                 'stroke-width="2.5"/>' % (ix, top, iw, bot - top, GOLD))
        if inset_label:
            anchor, lx = ("middle", ix + iw / 2.0)
            if iw < 320:                      # too narrow to hold the caption — set it outside
                anchor, lx = "end", ix - 14
            o.append(_txt(lx, top - 12, inset_label, 21, "#8A6A28", anchor, "700"))

    o.append('<line x1="%g" y1="%.1f" x2="%g" y2="%.1f" stroke="%s" stroke-width="3.5"/>'
             % (m, axis, w - m, axis, TEAL))

    # Break mark at the left edge — the line does not begin here, it just stops being drawable.
    if offscale:
        for dx in (-6.0, 12.0):
            o.append('<path d="M %.1f %.1f l 15 -24 l -15 -24" fill="none" stroke="%s" '
                     'stroke-width="3.5" stroke-linecap="round"/>' % (m + dx, axis + 24, TEAL))

    xs = [X(p[0]) for p in pegs]
    BLOCK, GAP = 58.0, 28.0          # height of one name+year block, and its clearance from the axis
    lowest = axis
    for peg, x, (side, row) in zip(pegs, xs, _slots(xs)):
        yr, lab, cert = peg[0], peg[1], peg[2]
        hijri = peg[3] if len(peg) > 3 and isinstance(peg[3], int) else None
        est = (cert == "E")

        if est:  # hollow, dashed = our sources do not fix this date
            o.append('<circle cx="%.1f" cy="%.1f" r="9" fill="%s" stroke="%s" stroke-width="3" '
                     'stroke-dasharray="3 3"/>' % (x, axis, CREAM, MAROON))
        else:
            o.append('<circle cx="%.1f" cy="%.1f" r="8" fill="%s"/>' % (x, axis, GOLD))

        # The name and its year travel together, so a crowded stretch never separates them.
        base = axis + side * (GAP + row * BLOCK)
        name_y = base - 22 if side < 0 else base + 22
        year_y = base if side < 0 else base
        # Keep wide labels inside the canvas: near a margin, anchor to the edge instead.
        half = 7.0 * len(lab or "")
        anc, tx = "middle", x
        if x - half < 8:
            anc, tx = "start", 8.0
        elif x + half > w - 8:
            anc, tx = "end", w - 8.0
        if lab:
            o.append(_txt(tx, name_y, lab, 23, MAROON if est else DEEP, anc,
                          "400" if est else "700"))
        # "approx." rides inside the year string rather than on its own line — as a separate
        # line it collided with the name on the below-axis side.
        ytxt = _yr(yr) + (" · %d AH" % hijri if hijri else "") + (" approx." if est else "")
        o.append(_txt(tx, year_y, ytxt, 20, MAROON if est else MUTED, anc, "400",
                      "italic" if est else "normal"))
        o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.4" '
                 'opacity=".45"/>'
                 % (x, axis + side * 11, x, base - side * 14, TEAL))
        lowest = max(lowest, base + 30 if side > 0 else axis)

    # The off-scale note gets its own clear line, under everything else.
    if offscale:
        o.append(_txt(m, lowest + 42, offscale, 22, MAROON, "start", "400", "italic"))

    if caption:
        o.append('<line x1="%g" y1="%.1f" x2="%g" y2="%.1f" stroke="%s" stroke-width="2"/>'
                 % (m, h - 62, w - m, h - 62, GOLD))
        o.append(_txt(m, h - 26, caption, 24, DEEP, "start", "400", "italic"))
    o.append("</svg>")
    return "\n".join(o)


def stack_svg(w=1800.0, h=2240.0):
    """All three panels on one sheet — this is the worksheet the audience takes home."""
    o = _frame(w, h)
    o.append(_txt(w / 2, 66, "Three ways to look at the same moment", 40, DEEP, "middle", "700"))
    o.append(_txt(w / 2, 104, "each line is the whole of the line above it", 23, MUTED,
                  "middle", "400", "italic"))
    panels = [
        (TL1_ARGS, 130), (TL2_ARGS, 830), (TL3_ARGS, 1530),
    ]
    for (args, _), y in panels:
        inner = timeline_svg(*args[0], **dict(args[1], h=700.0))
        body = inner.split("\n", 2)[2].rsplit("</svg>", 1)[0]
        o.append('<g transform="translate(0,%d)">%s</g>' % (y, body))
    o.append("</svg>")
    return "\n".join(o)


TL1_ARGS = (([TL1, 1947, NOW, "Pakistan"],
             dict(subtitle="the part you remember, or your parents do",
                  caption="Seventy-nine years. Now hold that thought.")), None)
TL2_ARGS = (([[(g, l, c, hj) for g, l, hj, c in TL2], 622, NOW, "The Ummah"],
             dict(subtitle="Hijra to tonight",
                  inset=(1947, NOW), inset_label="all of Pakistan",
                  caption="Fourteen centuries. Everything this course covers is on this line.")), None)
TL3_ARGS = (([TL3, -3000, NOW, "Before that"],
             dict(subtitle="the order is known; the dates are not",
                  inset=(622, NOW), inset_label="all of the last line",
                  offscale=TL3_OFFSCALE,
                  caption="Hollow markers are estimates from general scholarship — our sources do not fix "
                          "them.   عليهم السلام")), None)


# ===========================================================================
# The Medina clan chart — the load-bearing infographic of the evening
# ===========================================================================

# Filled from docs/research/medina-ansar-structure.md and muhajirun-quraysh-structure.md.
# A name appears here ONLY if a page supports it. `chief` is left None where the research
# note could not establish one — an empty box is honest; an invented name is not.
ANSAR = {
    "root": "THE ANṢĀR",
    "note": "of al-Azd — Qaḥṭān, southern",
    "branches": [
        ("al-Aws", [("Banū ʿAbd al-Ashhal", "Usayd b. Ḩuḍayr"),
                    ("Banū ʿAmr b. ʿAwf", None),
                    ("Banū Ḥāritha", None)]),
        ("al-Khazraj", [("Banū Sāʿida", "Saʿd b. ʿUbāda"),
                        ("Banū al-Najjār", None),
                        ("Banū Salima", None),
                        ("Banū al-Ḥārith", None)]),
    ],
}
MUHAJIRUN = {
    "root": "THE MUHĀJIRŪN",
    "note": "of Quraysh — ʿAdnān, northern",
    "branches": [
        ("Quraysh", [("Banū Hāshim", None),
              ("Banū Taym", "Abū Bakr al-Ṣiddīq"),
              ("Banū ʿAdī", "ʿUmar al-Fārūq"),
              ("Banū Umayya", None),
              ("Banū Makhzūm", None),
              ("Banū al-Ḥārith b. Fihr", "Abū ʿUbayda"),
              ("Banū ʿAmir b. Luʿayy", "Suhayl b. ʿAmr")]),
    ],
}


def clan_chart_svg(blank=False, w=1800.0, h=900.0):
    """The chart. `blank=True` prints the worksheet version with the chief boxes empty —
    that is session 1's hand-writing ritual (DECISIONS.md #15)."""
    o = _frame(w, h)
    o.append(_txt(w / 2, 62, "Who was in Medina" if not blank else "Who was in Medina — fill in the chiefs",
                  40, DEEP, "middle", "700"))
    o.append(_txt(w / 2, 100, "Two peoples, and neither of them was one bloc", 23, MUTED,
                  "middle", "400", "italic"))
    # The honorific, once, as its own Arabic run — never as a combining mark after Latin letters.
    o.append(_txt(w - 90, 100, "رضي الله عنهم",
                  26, MAROON, "end", "400"))

    def block(x0, width, data, y0):
        oo = []
        oo.append('<rect x="%.1f" y="%.1f" width="%.1f" height="66" rx="6" fill="%s"/>'
                  % (x0, y0, width, DEEP))
        oo.append(_txt(x0 + width / 2, y0 + 32, data["root"], 27, CREAM, "middle", "700"))
        oo.append(_txt(x0 + width / 2, y0 + 55, data["note"], 18, "#BFD3CF"))
        y = y0 + 96
        for bname, clans in data["branches"]:
            if bname:
                oo.append('<rect x="%.1f" y="%.1f" width="%.1f" height="40" rx="4" fill="%s"/>'
                          % (x0, y, width, TEAL))
                oo.append(_txt(x0 + width / 2, y + 27, bname, 23, CREAM, "middle", "700"))
                y += 52
            for cname, chief in clans:
                oo.append('<rect x="%.1f" y="%.1f" width="%.1f" height="46" rx="4" fill="#FFFFFF" '
                          'stroke="%s" stroke-width="1.6"/>' % (x0, y, width, FAINT))
                oo.append(_txt(x0 + 16, y + 30, cname, 22, INK, "start", "400"))
                if chief and not blank:
                    oo.append(_txt(x0 + width - 16, y + 30, chief, 21, MAROON, "end", "700"))
                elif blank:
                    oo.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
                              'stroke-width="1.5" stroke-dasharray="5 5"/>'
                              % (x0 + width * 0.52, y + 34, x0 + width - 16, y + 34, FAINT))
                y += 54
            y += 10
        return oo, y

    left, _ = block(90, 780, ANSAR, 140)
    right, _ = block(930, 780, MUHAJIRUN, 140)
    o.extend(left)
    o.extend(right)

    o.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="2"/>'
             % (90, h - 92, w - 90, h - 92, GOLD))
    o.append(_txt(90, h - 56, "Shortly before the Hijra, al-Aws and al-Khazraj had been at war "
                              "— yawm Buʿāth.", 24, DEEP, "start", "400", "italic"))
    o.append(_txt(90, h - 24, "That is why “who leads” was a live question in that "
                              "courtyard, and not an abstract one.", 24, MAROON, "start"))
    o.append("</svg>")
    return "\n".join(o)


# ===========================================================================
# The maps
# ===========================================================================

WORLD632 = View((-14.0, 8.0, 78.0, 52.0), 1800, 32.0)

# Governors at 11 AH. Filled from docs/research/governors-at-11h.md — a seat appears here
# only where the research note could cite a page. Coordinates are PLACEMENT ONLY and are
# never a claim about a site (MAPS.md).
GOV_SEATS = [
    ("makkah", "Makkah", "below"),
    ("madina", "Madina", "above"),
    ("taif", "al-Ta'if", "below"),
    ("sanaa", "San'a", "below"),
    ("najran", "Najran", "below"),
    ("bahrain", "al-Bahrayn", "above"),
    ("daba", "Uman", "above"),
    ("hadramawt", "Hadramawt", "below"),
    ("yamama", "al-Yamama", "above"),
]

EXTRA_PLACES = {"taif": (40.42, 21.27), "hadramawt": (48.80, 15.60)}


def build():
    os.makedirs(OUT, exist_ok=True)
    made = []

    for name, (args, _) in [("l01_tl1_pakistan", TL1_ARGS),
                            ("l01_tl2_ummah", TL2_ARGS),
                            ("l01_tl3_prophets", TL3_ARGS)]:
        svg = timeline_svg(*args[0], **args[1])
        made.append(render(svg, name, 1800, 700))

    made.append(render(stack_svg(), "l01_tl_stack", 1800, 2240))
    made.append(render(clan_chart_svg(False), "l01_clanchart", 1800, 900))
    made.append(render(clan_chart_svg(True), "l01_clanchart_blank", 1800, 900))
    return made


if __name__ == "__main__":
    for p, sz in build():
        print("%-30s %7.1f KB" % (os.path.basename(p), sz / 1024))
