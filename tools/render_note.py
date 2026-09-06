"""Render a research note (.md) to an A4 PDF whose Arabic can actually be read.

    python tools/render_note.py docs/research/saqifah-bani-saida.md
    python tools/render_note.py --all              # every note in docs/research/

WHY THIS EXISTS (DECISIONS.md #25). The research notes are the part of the session-1 preparation
Daniyal rated highest — and the part he could not comfortably read. In a .md viewer the Arabic
comes out at body size in whatever fallback face the editor picks, run together with English on
the same line, with the honorifics and harakat colliding. The findings were good and unreadable.

So: the .md stays canonical and greppable — it is what git diffs and what grep searches. The PDF
is what gets READ. Here every Arabic run is set in Traditional Arabic (Naskh) at a size chosen for
reading rather than for fitting, every quotation gets its own right-to-left panel with the printed
page and the live shamela.ws link beneath it, and the fonts are base64-embedded so the file renders
identically on any machine and at any print shop.

WHAT IT DOES TO THE MARKDOWN, and why:

  1. A multi-line blockquote is exploded so each line becomes its own paragraph. The note format
     stacks three different things inside one blockquote — the verbatim Arabic, the citation, the
     English rendering — and Markdown would otherwise fuse them into a single paragraph with a
     single text direction, which is exactly the mangling CLAUDE.md 1.3 forbids.
  2. Every block whose text is more Arabic than Latin is set dir="rtl" and given the Naskh face.
  3. Every Arabic run *inside* an English sentence — the names, the honorifics ؓ and ﷺ, a لقب — is
     wrapped and bidi-isolated, so it is legible without reordering the English around it.
  4. Bare URLs are linkified, so a shamela reference is one click from the page it cites.

Requires: `markdown` (pip install markdown) and Chrome. Font embedding is delegated to
series/embed_fonts.py, which owns the font policy and refuses the banned Nastaliq cut.
"""
import os
import re
import sys
import glob
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "series"))

import markdown                      # noqa: E402
import embed_fonts                   # noqa: E402

# Research notes are English plus verbatim Arabic and contain no Urdu at all (DECISIONS.md #19),
# so the Nastaliq face is dead weight here — embedding it cost about 700 KB in every PDF. Drop it
# and keep only the Naskh face the Arabic is actually set in.
embed_fonts.FACES = [f for f in embed_fonts.FACES if f[0] == "Traditional Arabic"]

NOTES = os.path.join(ROOT, "docs", "research")
WORK = os.path.join(NOTES, ".render")

# Arabic, Arabic Supplement, Extended-A, and both presentation-forms blocks. The honorific ؓ is
# U+0613 and ﷺ is U+FDFA, so both fall inside this set and travel with the text they belong to.
AR = r"؀-ۿݐ-ݿࢠ-ࣿﭐ-﷿ﹰ-﻿"
AR_CHAR = re.compile("[%s]" % AR)
AR_RUN = re.compile("[%s](?:[\\s‏‎ ]*[%s])*" % (AR, AR))
LATIN = re.compile(r"[A-Za-z]")
TAGSPLIT = re.compile(r"(<[^>]+>)")
BARE_URL = re.compile(r"(?<![\"'=>])(https?://[^\s<>\"')]+)")

BLOCK = re.compile(r"<(p|li|td|th|h[1-6])(\s[^>]*)?>(.*?)</\1>", re.S)


# --------------------------------------------------------------------------- markdown massaging

def explode_blockquotes(md):
    """Give every line of a multi-line blockquote its own paragraph.

    The note format writes a quotation as three stacked lines — Arabic, citation, rendering. In
    Markdown those are one paragraph, which means one text direction for all three and a mangled
    result. Inserting a bare `>` between them makes each its own <p>, so each can be typeset in
    the direction it actually needs.
    """
    out, prev_quote = [], False
    for line in md.split("\n"):
        is_quote = line.lstrip().startswith(">")
        bare = line.strip() in (">", "")
        if is_quote and prev_quote and not bare and out and out[-1].strip() not in (">", ""):
            out.append(">")
        out.append(line)
        prev_quote = is_quote and not bare
    return "\n".join(out)


# --------------------------------------------------------------------------- html post-processing

def on_text(html, fn):
    """Apply fn to the text between tags, never to the tags themselves."""
    return "".join(p if p.startswith("<") else fn(p) for p in TAGSPLIT.split(html))


def wrap_inline_arabic(html):
    return on_text(html, lambda t: AR_RUN.sub(lambda m: '<span class="ar-i">%s</span>' % m.group(0), t))


def linkify(html):
    return on_text(html, lambda t: BARE_URL.sub(r'<a href="\1">\1</a>', t))


def classify_blocks(html):
    """Set direction and role on each block from what it actually contains."""

    def one(m):
        tag, attrs, inner = m.group(1), m.group(2) or "", m.group(3)
        text = TAGSPLIT.sub("", inner)
        ar, la = len(AR_CHAR.findall(text)), len(LATIN.findall(text))
        stripped = text.strip()

        # A block flips to right-to-left only when it is ESSENTIALLY all Arabic. A simple
        # majority test is not enough: "Same page, السخاوي quotes الجوهري رحمہ اللہ:" carries more
        # Arabic letters than Latin ones and yet is an English sentence — flipping it reorders the
        # English into nonsense, which is the exact failure CLAUDE.md 1.3 was written about. So
        # Latin must be under a sixth of the letters, or absent, before the direction changes.
        rtl = ar > 0 and la <= max(2, 0.16 * (ar + la))

        is_cite = (stripped.startswith(("\u2014", "\u2013", "--"))
                   and ("shamela.ws" in text or "\u0635" in text or "\u062c" in text))
        is_tr = (stripped.lower().startswith(("english:", "english :"))
                 or inner.strip().lower().startswith("<em>english"))

        cls = []
        if is_cite:
            cls.append("cite")          # a citation stays small even when it is pure Arabic
        elif is_tr:
            cls.append("tr")
        if rtl and not (is_cite and la):
            cls.append("ar")
            attrs += ' dir="rtl"'

        if cls:
            attrs = ' class="%s"%s' % (" ".join(cls), attrs)
        return "<%s%s>%s</%s>" % (tag, attrs, inner, tag)

    return BLOCK.sub(one, html)


CSS = """
@page { size: A4; margin: 16mm 15mm 16mm 15mm; }
* { box-sizing: border-box; }
body {
  font-family: 'Segoe UI', 'Calibri', system-ui, sans-serif;
  font-size: 10.5pt; line-height: 1.58; color: #1C2321;
  margin: 0; -webkit-print-color-adjust: exact; print-color-adjust: exact;
}

/* ---- the title block ------------------------------------------------- */
.doc-head { border-bottom: 3px solid #104A43; padding-bottom: 10px; margin-bottom: 22px; }
.doc-head .kicker {
  font: 700 8pt 'Segoe UI', sans-serif; letter-spacing: .16em; text-transform: uppercase;
  color: #C49A45; margin-bottom: 5px;
}
.doc-head .file { font: 400 8.5pt Consolas, monospace; color: #6B7472; margin-top: 4px; }

/* ---- headings -------------------------------------------------------- */
h1, h2, h3, h4, h5, h6 {
  font-family: Georgia, 'Times New Roman', serif; color: #0A322E;
  line-height: 1.25; margin: 1.5em 0 .5em; break-after: avoid; page-break-after: avoid;
}
h1 { font-size: 20pt; margin-top: 0; }
h2 { font-size: 14.5pt; border-bottom: 1px solid #D8D2C4; padding-bottom: 4px; margin-top: 1.9em; }
h3 { font-size: 12pt; color: #104A43; }
h4, h5, h6 { font-size: 10.5pt; color: #104A43; }
h1.ar, h2.ar, h3.ar, h4.ar { font-family: 'Traditional Arabic', serif; font-size: 20pt; }

p { margin: .55em 0; orphans: 3; widows: 3; }
hr { border: 0; border-top: 1px solid #D8D2C4; margin: 1.8em 0; }
strong { color: #0A322E; }
a { color: #104A43; text-decoration: none; border-bottom: .5pt solid #A8BEB9; word-break: break-all; }
code {
  font: 9pt Consolas, monospace; background: #F2EFE7; padding: .5pt 3pt;
  border-radius: 2px; color: #7A2E2E;
}

/* ---- ARABIC. The whole reason this renderer exists. ------------------- */
/* Traditional Arabic sits small against Latin at the same nominal size, so both the block and the
   inline runs are scaled up deliberately. Line-height is generous because Naskh stacks marks
   above and below the baseline and a tight leading makes ؓ collide with the line above. */
.ar-i {
  font-family: 'Traditional Arabic', 'Segoe UI Historic', serif;
  font-size: 1.34em; line-height: 1; unicode-bidi: isolate;
}
.ar .ar-i, .ar-block .ar-i { font-size: 1em; }

p.ar, li.ar, td.ar, th.ar {
  font-family: 'Traditional Arabic', 'Segoe UI Historic', serif;
  font-size: 19pt; line-height: 1.95; color: #0A322E;
  text-align: right; direction: rtl;
  margin: .35em 0;
}

blockquote {
  margin: 1.1em 0; padding: 10px 14px 10px 16px;
  background: #FAF7F0; border-left: 3px solid #C49A45;
  break-inside: avoid; page-break-inside: avoid;
}
blockquote p { margin: .25em 0; }
blockquote p.ar { font-size: 20pt; margin: .1em 0 .35em; }
blockquote p.cite {
  font-size: 8.6pt; color: #5C6664; direction: ltr; text-align: left;
  border-top: .5pt dotted #D8D2C4; padding-top: 5px; margin-top: 7px;
}
blockquote p.cite .ar-i { font-size: 1.25em; }
blockquote p.cite.ar { direction: rtl; text-align: right; font-size: 13.5pt; line-height: 1.7;
                       font-family: 'Traditional Arabic', serif; }
p.cite.ar .ar-i { font-size: 1em; }
blockquote p.tr { font-size: 10pt; color: #3A4442; font-style: italic; }

/* ---- tables ---------------------------------------------------------- */
table { border-collapse: collapse; width: 100%; margin: 1em 0; font-size: 9.3pt;
        break-inside: avoid; page-break-inside: avoid; }
th { background: #104A43; color: #FAF7F0; font-weight: 600; text-align: left; }
th, td { border: .5pt solid #C9C3B5; padding: 5px 7px; vertical-align: top; }
tr:nth-child(even) td { background: #F7F5EF; }
td.ar, th.ar { font-size: 15pt; line-height: 1.7; }

ul, ol { margin: .55em 0; padding-left: 1.4em; }
li { margin: .28em 0; }

/* ---- the certainty labels, so they are visible at a glance ----------- */
code:where(:not(a code)) { white-space: nowrap; }
"""

LABEL_COLOURS = {
    "[SOURCED]": ("#0A322E", "#DCE9E5"),
    "[STANDARD]": ("#7A5A10", "#F5EBD2"),
    "[CONVENTIONAL-ESTIMATE]": ("#7A2E2E", "#F2DEDE"),
}


def colour_labels(html):
    def one(t):
        for lab, (fg, bg) in LABEL_COLOURS.items():
            t = t.replace(lab, '<span style="background:%s;color:%s;padding:1pt 4pt;'
                               'border-radius:2px;font-weight:600;font-size:8.5pt;'
                               'white-space:nowrap">%s</span>' % (bg, fg, lab))
        return t
    return on_text(html, one)


PAGE = """<meta charset="utf-8">
<title>%(title)s</title>
<!--EMBED-FONTS-->
<style>%(css)s</style>
<div class="doc-head">
  <div class="kicker">Lessons from History &middot; %(kicker)s</div>
  <div class="file">%(rel)s</div>
</div>
%(body)s
"""


def to_html(raw):
    """Markdown -> Arabic-aware HTML. The half of this module the speaker pack reuses."""
    body = markdown.markdown(
        explode_blockquotes(raw),
        extensions=["tables", "fenced_code", "sane_lists", "attr_list"],
    )
    body = classify_blocks(body)
    body = linkify(body)
    body = wrap_inline_arabic(body)
    return colour_labels(body)


def render(md_path, css=None, kicker="research note", out_dir=None, work=None):
    md_path = os.path.abspath(md_path)
    body = to_html(open(md_path, encoding="utf-8").read())

    stem = os.path.splitext(os.path.basename(md_path))[0]
    rel = os.path.relpath(md_path, ROOT).replace("\\", "/")
    title = re.search(r"<h1[^>]*>(.*?)</h1>", body, re.S)
    title = TAGSPLIT.sub("", title.group(1)).strip() if title else stem

    work = work or WORK
    os.makedirs(work, exist_ok=True)
    html_path = os.path.join(work, stem + ".html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(PAGE % {"title": title, "css": css or CSS, "rel": rel,
                        "kicker": kicker, "body": body})

    pdf = embed_fonts.to_pdf(html_path)
    final = os.path.join(out_dir or os.path.dirname(md_path), stem + ".pdf")
    shutil.move(pdf, final)
    return final


def page_count(pdf):
    """How many pages Chrome actually produced. The cue sheet must be exactly one."""
    blob = open(pdf, "rb").read()
    n = re.findall(rb"/Type\s*/Page[^s]", blob)
    return len(n) or len(re.findall(rb"/Count\s+(\d+)", blob) or [b"0"])


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--all"]
    if "--all" in sys.argv:
        args = sorted(glob.glob(os.path.join(NOTES, "*.md")))
    if not args:
        raise SystemExit(__doc__)
    for a in args:
        if os.path.basename(a).upper() == "INDEX.MD":
            continue
        try:
            p = render(a)
            print("%-58s %8.1f KB" % (os.path.relpath(p, ROOT), os.path.getsize(p) / 1024))
        except Exception as e:                                    # noqa: BLE001
            print("FAILED  %-50s %s" % (os.path.basename(a), e))
