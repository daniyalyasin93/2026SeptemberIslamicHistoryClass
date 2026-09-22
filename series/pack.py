"""The speaker pack: the one-page cue sheet, the briefing, and the audience worksheet.

    from series import pack
    pack.cue("L02_baarah_saal/CUE.pdf", CUE_DATA)          # asserts it fits on ONE page
    pack.briefing("L02_baarah_saal/BRIEFING.md")            # -> BRIEFING.pdf
    pack.worksheet("L02_baarah_saal/WORKSHEET.pdf", WS)

WHY THESE THREE, AND WHY SEPARATE (DECISIONS.md #22). Session 1 went to the lectern with a prose
script and the verdict was "the script you wrote had a lot of text, so it was hard for me to
follow", seconded by a manager: "Do not read from script. In notes, one can have the key headings,
names and dates written before one, but not full sentences."

So the prose and the cues are now different objects with different jobs:

    BRIEFING.pdf   prose. Read twice at home, so the story can be TOLD. Never at the lectern.
    CUE.pdf        one page. Headings, names, dates, map cues, عبرت lines. No sentences.
    WORKSHEET.pdf  the audience's page — the blank map and the blank timeline they fill in.

THE ONE-PAGE RULE IS ENFORCED, NOT ASSERTED. `cue()` renders, counts the pages Chrome actually
produced, and raises if there is more than one. A two-page cue card is not a cue card; it is a
script with worse formatting, and CLAUDE.md 1.7 has said so since the first deck.

Print sizes are print sizes: the 24pt floor in deck2 governs a projected slide read from the back
of a hall. This is A4 held at arm's length on a lectern, where 13pt bold is large and clear.
"""
import base64
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "tools"))
sys.path.insert(0, HERE)

import render_note                                   # noqa: E402
import embed_fonts                                   # noqa: E402

VIS = os.path.join(HERE, "visuals")
TEAL, GOLD, CREAM, INK, MUTED = "#104A43", "#C49A45", "#FAF7F0", "#1C2321", "#5A6862"
MAROON = "#7A2E2E"


def _img(name):
    """Base64 an image so the PDF prints identically anywhere, with no path resolution."""
    path = name if os.path.isabs(name) else os.path.join(VIS, name)
    if not os.path.exists(path):
        return None
    with open(path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode("ascii")


def _render(html, out, landscape=False):
    work = os.path.join(os.path.dirname(os.path.abspath(out)), ".build")
    os.makedirs(work, exist_ok=True)
    src = os.path.join(work, os.path.splitext(os.path.basename(out))[0] + ".html")
    with open(src, "w", encoding="utf-8") as f:
        f.write(html)
    pdf = embed_fonts.to_pdf(src)
    if os.path.abspath(pdf) != os.path.abspath(out):
        if os.path.exists(out):
            os.remove(out)
        os.replace(pdf, out)
    return out


# =========================================================================== the cue sheet

CUE_CSS = """
@page { size: A4 landscape; margin: 8mm 9mm; }
* { box-sizing: border-box; }
body { font-family: 'Segoe UI', Calibri, sans-serif; font-size: %(base)spt; color: %(ink)s;
       margin: 0; line-height: 1.28; -webkit-print-color-adjust: exact; print-color-adjust: exact; }

.top { display: flex; align-items: baseline; gap: 14px; border-bottom: 2.5pt solid %(teal)s;
       padding-bottom: 4px; margin-bottom: 7px; }
.top .n { background: %(teal)s; color: %(cream)s; font: 700 13pt 'Segoe UI'; padding: 2px 9px;
          border-radius: 3px; }
.top .t { font: 700 19pt Georgia, serif; color: %(teal)s; }
.top .d { color: %(muted)s; font-size: %(small)spt; }
.top .r { margin-left: auto; font: 700 12pt 'Segoe UI'; color: %(gold)s; }

.cols { display: flex; gap: 9px; }
.col { flex: 1; }
.col.run { flex: 1.45; }
/* A long evening (an overflow part behind the planned close) has more beats than one column holds at a
   readable size. Splitting the run into two columns keeps every beat AND keeps the type up: the
   alternative was 10pt, which on a lectern under stage light is not a cue sheet. */
.col.run.two { flex: 2.6; }
.col.run.two .beats { column-count: 2; column-gap: 13px; }
h2 { font: 700 9.5pt 'Segoe UI'; letter-spacing: .14em; text-transform: uppercase;
     color: %(gold)s; margin: 0 0 4px; border-bottom: .75pt solid #D8D2C4; padding-bottom: 2px; }

.beat { display: flex; gap: 7px; margin-bottom: 2.6px; break-inside: avoid; }
.beat .clock { font: 700 11pt Consolas, monospace; color: %(teal)s; min-width: 34px; }
.beat .what { flex: 1; }
.beat .name { font-weight: 700; }
.beat .cues { color: %(muted)s; font-size: %(small)spt; }
.beat.hands { background: #FBF3E0; border-left: 2.5pt solid %(gold)s; padding: 2px 5px;
              margin-left: -5px; }
.beat.act { background: #E6F0EE; border-left: 2.5pt solid %(teal)s; padding: 2px 5px;
            margin-left: -5px; }

.who { margin-bottom: 4px; break-inside: avoid; }
.who b { display: block; }
.who span { color: %(muted)s; font-size: %(small)spt; }
.ar { font-family: 'Traditional Arabic', serif; font-size: 15pt; direction: rtl; }

ol.lessons { margin: 0; padding-left: 15px; }
ol.lessons li { margin-bottom: 4.5px; break-inside: avoid; }

.foot { position: fixed; bottom: 0; left: 0; right: 0; display: flex; gap: 10px;
        border-top: 2.5pt solid %(maroon)s; padding-top: 4px; font: 700 12pt 'Segoe UI'; }
.foot div { flex: 1; text-align: center; color: %(maroon)s; }
.pad { height: 18px; }   /* clearance for the fixed footer, no more */
"""


def cue(out, d):
    """One page. Headings, names, dates, cues. If it spills, the build fails."""
    beats = []
    for b in d["run"]:
        kind = b.get("kind", "")
        cues = b.get("cues") or []
        beats.append(
            '<div class="beat %s"><div class="clock">%s</div><div class="what">'
            '<span class="name">%s</span>%s</div></div>'
            % (kind, b.get("t", ""), b["name"],
               ('<div class="cues">' + " &middot; ".join(cues) + "</div>") if cues else ""))

    who = "".join('<div class="who"><b>%s</b><span>%s</span></div>' % (n, s)
                  for n, s in d.get("names", []))
    lessons = "".join("<li>%s</li>" % l for l in d.get("lessons", []))

    shell = """<meta charset="utf-8"><title>%(title)s — cue</title>
<!--EMBED-FONTS-->
<style>%(css)s</style>
<div class="top">
  <span class="n">SESSION %(session)s</span>
  <span class="t">%(title)s</span>
  <span class="d">%(dates)s</span>
  <span class="r">%(runtime)s</span>
</div>
<div class="cols">
  <div class="col run%(wide)s"><h2>Run</h2><div class="beats">%(beats)s</div></div>
  <div class="col"><h2>Names &amp; dates</h2>%(who)s</div>
  <div class="col"><h2>Ibrah &mdash; one at a time</h2><ol class="lessons">%(lessons)s</ol></div>
</div>
<div class="pad"></div>
<div class="foot">
  <div>VOICE &mdash; LOUDER</div><div>PAUSE BETWEEN IDEAS</div>
  <div>POINTER</div><div>DON'T READ &mdash; TELL</div><div>END: SALAM, THEN DUA</div>
</div>
"""
    fields = {"title": d["title"], "session": d["session"], "dates": d["dates"],
              "runtime": d.get("runtime", ""), "beats": "".join(beats), "who": who,
              "wide": " two" if len(d["run"]) > 18 else "",
              "lessons": lessons}
    colours = {"ink": INK, "teal": TEAL, "gold": GOLD, "cream": CREAM,
               "muted": MUTED, "maroon": MAROON}

    # Auto-fit. Content varies session to session, so rather than hand-tune the CSS every week,
    # step the type down until it fits one page — and refuse below 10pt, because a cue sheet you
    # have to squint at on a lectern under stage light is worse than no cue sheet at all. The
    # chosen size is printed: if it lands at the floor, the session has too many cues, not too
    # small a page, and the fix is to cut cues.
    for base in (14.0, 13.5, 13.0, 12.5, 12.0, 11.5, 11.0, 10.5, 10.0):
        html = shell % dict(fields, css=CUE_CSS % dict(colours, base=base, small=base - 1.2))
        path = _render(html, out)
        if render_note.page_count(path) == 1:
            print("%-34s 1 page   %4.1fpt  %7.1f KB"
                  % (os.path.basename(path), base, os.path.getsize(path) / 1024))
            if base <= 10.5:
                print("   tight at %.1fpt — consider cutting cues rather than shrinking further."
                      % base)
            return path
    raise SystemExit(
        "CUE.pdf will not fit on one page even at 10pt. It must be ONE page — that is its entire "
        "purpose (CLAUDE.md 1.7). Cut cues, not type size: a cue card you cannot read at a glance "
        "is a script with worse formatting.")


# =========================================================================== the briefing

BRIEFING_CSS = render_note.CSS + """
/* Read at home, twice, in an armchair — so: bigger, looser, and broken by scene. */
@page { margin: 18mm 20mm; }
body { font-size: 12pt; line-height: 1.72; }
h2 { break-before: page; page-break-before: always; margin-top: 0; font-size: 17pt; }
h2:first-of-type { break-before: auto; page-break-before: auto; }
h3 { font-size: 13.5pt; margin-top: 1.6em; }
p { margin: .75em 0; }
blockquote p.ar { font-size: 22pt; }
.doc-head .kicker { color: %s; }
""" % TEAL


def briefing(md_path, out_dir=None):
    """The prose, as a book to read — not a script to read FROM."""
    p = render_note.render(md_path, css=BRIEFING_CSS, kicker="speaker briefing",
                           out_dir=out_dir,
                           work=os.path.join(os.path.dirname(os.path.abspath(md_path)), ".build"))
    print("%-34s %2d pages %8.1f KB"
          % (os.path.basename(p), render_note.page_count(p), os.path.getsize(p) / 1024))
    return p


# =========================================================================== the worksheet

WS_CSS = """
@page { size: A4; margin: 13mm 14mm; }
* { box-sizing: border-box; }
body { font-family: 'Segoe UI', Calibri, sans-serif; font-size: 11pt; color: %(ink)s; margin: 0;
       -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.hdr { border-bottom: 2.5pt solid %(teal)s; padding-bottom: 5px; margin-bottom: 10px; }
.hdr .k { font: 700 8.5pt 'Segoe UI'; letter-spacing: .16em; text-transform: uppercase; color: %(gold)s; }
.hdr h1 { font: 700 20pt Georgia, serif; color: %(teal)s; margin: 2px 0 0; }
.hdr .d { color: %(muted)s; }

h2 { font: 700 9.5pt 'Segoe UI'; letter-spacing: .14em; text-transform: uppercase; color: %(gold)s;
     margin: 14px 0 5px; border-bottom: .75pt solid #D8D2C4; padding-bottom: 2px; }
.task { font-size: 10.5pt; color: %(muted)s; margin-bottom: 6px; }
img { width: 100%%; display: block; }
.mapbox { border: .75pt solid #C9C3B5; padding: 4px; }

.tl { display: flex; gap: 5px; margin-top: 6px; }
.tl div { flex: 1; border: .75pt solid #B9C7C3; border-top: 2.5pt solid %(teal)s; height: 46px;
          border-radius: 2px; position: relative; }
.tl div span { position: absolute; bottom: 3px; left: 0; right: 0; text-align: center;
               font: 700 8.5pt 'Segoe UI'; color: %(muted)s; }

.who { border-left: 2.5pt solid %(gold)s; padding: 3px 0 3px 8px; margin-bottom: 9px;
       break-inside: avoid; }
.who b { font-size: 12pt; }
.who .meta { color: %(muted)s; font-size: 10pt; }
.who .blank { margin-top: 5px; font-size: 9.5pt; color: %(muted)s; }
.rule { border-bottom: .75pt solid #C9C3B5; height: 15px; }
ol.ib { margin: 0; padding-left: 16px; }
ol.ib li { margin-bottom: 3px; }
ol.ib .rule { margin-top: 2px; }
.ar { font-family: 'Traditional Arabic', serif; font-size: 15pt; }
.foot { margin-top: 12px; border-top: .75pt solid #D8D2C4; padding-top: 5px;
        font-size: 9.5pt; color: %(muted)s; }
"""


def worksheet(out, d):
    """The audience's page: the blank map and the blank timeline they fill in during the evening."""
    tl = "".join('<div><span>%s</span></div>' % (lbl or "&nbsp;") for lbl in d["timeline_boxes"])

    who = ""
    for p in d.get("people", []):
        who += ('<div class="who"><b>%s</b><div class="meta">%s</div>'
                '<div class="meta">%s</div>'
                '<div class="blank">One incident &mdash; write it as you hear it:</div>'
                '<div class="rule"></div><div class="rule"></div></div>'
                % (p["name"], p["dates"], p["did"]))

    ib = "".join('<li>%s<div class="rule"></div></li>' % (l or "&nbsp;")
                 for l in d.get("lesson_lines", [""] * 4))

    mapimg = _img(d["map"]) if d.get("map") else None
    html = """<meta charset="utf-8"><title>%(title)s — worksheet</title>
<!--EMBED-FONTS-->
<style>%(css)s</style>
<div class="hdr">
  <div class="k">Lessons from History &middot; Session %(session)s</div>
  <h1>%(title)s</h1>
  <div class="d">%(dates)s</div>
</div>

<h2>1 &middot; Where it happened</h2>
<div class="task">%(map_task)s</div>
<div class="mapbox">%(map)s</div>

<h2>2 &middot; When it happened</h2>
<div class="task">%(tl_task)s</div>
<div class="tl">%(tl)s</div>

<h2>3 &middot; Who</h2>
<div class="task">Three lines are printed. The fourth is yours &mdash; write the one incident you
want to remember about each man.</div>
%(who)s

<h2>4 &middot; Tonight's lessons</h2>
<div class="task">Write each one in your own words as it is said.</div>
<ol class="ib">%(ib)s</ol>

<div class="foot">%(foot)s</div>
""" % {"title": d["title"], "session": d["session"], "dates": d["dates"],
       "map": ('<img src="%s">' % mapimg) if mapimg
              else '<div style="height:250px"></div>',
       "map_task": d.get("map_task", "Mark and name three places as they are mentioned."),
       "tl_task": d.get("tl_task", "Write the year in each box as we reach it."),
       "tl": tl, "who": who, "ib": ib,
       "foot": d.get("foot", "Questions on a slip into the box at the door. "
                             "I will stay fifteen minutes afterwards."),
       "css": WS_CSS % {"ink": INK, "teal": TEAL, "gold": GOLD, "muted": MUTED}}

    path = _render(html, out)
    print("%-34s %2d pages %8.1f KB"
          % (os.path.basename(path), render_note.page_count(path), os.path.getsize(path) / 1024))
    return path
