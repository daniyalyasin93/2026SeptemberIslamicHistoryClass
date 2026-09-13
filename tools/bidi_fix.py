"""Make the mixed Arabic/English lines in the .md files readable in a plain Markdown preview.

    python tools/bidi_fix.py                       # every note + the catalogue
    python tools/bidi_fix.py docs/research/siffin.md
    python tools/bidi_fix.py --check               # report only, change nothing
    python tools/bidi_fix.py --strip <files>       # undo

THE PROBLEM. A research note is English prose with Arabic names, القاب and honorifics inside the
sentences — «عثمان ؓ» in the middle of a line, a book title, a printed page like «ج۷ ص۴۰۴». Markdown
has no idea any of that is right-to-left, so the Unicode bidi algorithm resolves the direction of
every neutral character — spaces, commas, full stops, brackets, digits, the · separator — from
whatever happens to sit beside it. The result in a preview is a paragraph whose punctuation has
migrated to the wrong end of the wrong clause, and page numbers reading backwards. The text is
correct in the file and unreadable on the screen, which is the worst of both.

THE FIX, and why it is this one. Each Arabic run gets wrapped in U+2068 FIRST STRONG ISOLATE and
U+2069 POP DIRECTIONAL ISOLATE. That tells the renderer: this run is its own bidi paragraph, take
its direction from its own first strong character, and do not let it reorder anything around it.
The characters are zero-width and invisible; nothing on the page changes except that it comes out
in the right order. Every conformant renderer honours them — browsers, GitHub, VS Code.

Alternatives rejected: putting every Arabic name on its own line would destroy the prose;
`<span dir>` tags only work where HTML is rendered and are noise in a diff; and leaving it to
`tools/render_note.py` (which does isolate correctly, into PDF) does not help the person reading
the .md in an editor, which is how these files actually get read while they are being written.

DOWNSTREAM. `tools/build_content.py` strips the isolates on the way into `CONTENT.md`, so nothing
reaches a slide, a cue sheet or a PDF with an invisible control character in it. Grep is unaffected
for any search inside an Arabic run; a search that spans the boundary between an Arabic run and the
English around it would need `--strip` first, which is why this is reversible.

Runs inside fenced code blocks are left alone, and so are lines that carry no Latin letters at all —
a blockquote of pure Arabic is already unambiguous and needs no help.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FSI, PDI = "⁨", "⁩"

# Arabic letters, Arabic-Indic digits, the honorific ligatures ﷺ/ﷻ and ؓ/﵁, and the punctuation
# that belongs to an Arabic run (« » ، ؛ ؟) — but NOT the spaces around it, which is the point.
AR = r"؀-ۿݐ-ݿࢠ-ࣿﭐ-﷿ﹰ-﻿"
RUN = re.compile(r"[%s]+(?:[  ][%s]+)*" % (AR, AR))
HAS_LETTER = re.compile(r"[ؠ-يٱ-ۓ]")
LATIN = re.compile(r"[A-Za-z]")
FENCE = re.compile(r"^\s*(```|~~~)")


def isolate_line(line):
    """Wrap each Arabic run in the line, unless the line is wholly Arabic or already wrapped."""
    if FSI in line or not LATIN.search(line):
        return line, 0
    n = [0]

    def wrap(m):
        run = m.group(0)
        if not HAS_LETTER.search(run):
            return run
        n[0] += 1
        return FSI + run + PDI

    return RUN.sub(wrap, line), n[0]


def process(text, strip=False):
    if strip:
        return text.replace(FSI, "").replace(PDI, ""), text.count(FSI)
    out, total, in_fence = [], 0, False
    for line in text.split("\n"):
        if FENCE.match(line):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        fixed, n = isolate_line(line)
        total += n
        out.append(fixed)
    return "\n".join(out), total


def targets(args):
    if args:
        return args
    found = []
    for sub in ("docs/research", "docs/catalogue", "docs"):
        d = os.path.join(ROOT, sub)
        if not os.path.isdir(d):
            continue
        for f in sorted(os.listdir(d)):
            p = os.path.join(d, f)
            if f.endswith(".md") and os.path.isfile(p) and p not in found:
                found.append(p)
    return found


def main():
    strip = "--strip" in sys.argv
    check = "--check" in sys.argv
    paths = targets([a for a in sys.argv[1:] if not a.startswith("-")])
    touched = runs = 0
    for p in paths:
        text = io.open(p, encoding="utf-8").read()
        new, n = process(text, strip)
        if n and new != text:
            touched += 1
            runs += n
            if not check:
                io.open(p, "w", encoding="utf-8", newline="\n").write(new)
        print("%-58s %6d runs%s" % (os.path.relpath(p, ROOT), n,
                                    "" if not check else "  (check only)"))
    print("\n%d files, %d Arabic runs %s" % (touched, runs,
                                             "would be isolated" if check else
                                             ("un-isolated" if strip else "isolated")))


if __name__ == "__main__":
    main()
