"""Extract a Tareekh-e-Ummat PDF to page-marked, greppable UTF-8 text.

Every page gets a marker line carrying BOTH the pdf page and the *printed* page,
so any citation can be traced back and verified against the page image.

    python tools/extract_source.py sources/pdf/<file>.pdf sources/text/<file>.txt [--offset N]

If --offset is omitted it is auto-detected from the trailing page-number line
that this edition prints at the bottom of every page.
"""
import argparse, re, sys
import fitz

JUNK = re.compile(r"TELEGRAM\s+CHANNEL|t\.me/pasbanehaq", re.I)
NUM  = re.compile(r"^\d{1,4}$")


def page_lines(page):
    return [l.strip() for l in (page.get_text() or "").split("\n") if l.strip()]


def printed_no(lines):
    """The edition prints the page number as a bare-integer line near the foot."""
    for l in reversed(lines[-4:]):
        if NUM.match(l):
            return int(l)
    return None


def detect_offset(doc):
    """offset = printed - pdf_index, agreed by first and last detectable pages."""
    votes = []
    for i in list(range(min(4, doc.page_count))) + list(range(max(0, doc.page_count - 4), doc.page_count)):
        n = printed_no(page_lines(doc[i]))
        if n is not None:
            votes.append(n - (i + 1))
    if not votes:
        return None
    return max(set(votes), key=votes.count)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf"); ap.add_argument("txt")
    ap.add_argument("--offset", type=int, default=None)
    a = ap.parse_args()

    doc = fitz.open(a.pdf)
    off = a.offset if a.offset is not None else detect_offset(doc)
    if off is None:
        sys.exit("could not detect the printed-page offset; pass --offset explicitly")

    out, unsure = [], []
    for i, page in enumerate(doc):
        lines = [l for l in page_lines(page) if not JUNK.search(l)]
        printed = printed_no(lines)
        if printed is None:
            printed = i + 1 + off
            unsure.append(i + 1)
        elif printed != i + 1 + off:
            unsure.append(i + 1)
        lines = [l for l in lines if not (NUM.match(l) and int(l) == printed)]
        out.append("===== PDF p.%d | PRINTED p.%d =====" % (i + 1, printed))
        out.extend(lines)
        out.append("")

    with open(a.txt, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    msg = "%s -> %s | %d pages | printed %d-%d | offset %+d" % (
        a.pdf, a.txt, doc.page_count, 1 + off, doc.page_count + off, off)
    if unsure:
        msg += " | CHECK pdf pages: %s" % unsure
    sys.stdout.buffer.write((msg + "\n").encode("utf-8"))


if __name__ == "__main__":
    main()
