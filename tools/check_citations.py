"""Check every Arabic quotation in the research notes against the page it cites — mechanically.

    python tools/check_citations.py                      # every note
    python tools/check_citations.py docs/research/siffin.md ...
    python tools/check_citations.py --quiet              # counts only

WHY THIS EXISTS. `CLAUDE.md` §1.1: a citation is airtight or absent. The way that was enforced
until now was to send a second model over the note to re-grep every quotation — which is the single
most expensive verification in the project and, being a model, can also just be wrong. But the
check is not a judgement call: the quoted Arabic either occurs on the cited page or it does not,
and the printed page either matches the cached file's own header or it does not. That is string
work, so it is done here, for nothing, and the model is only ever asked to fix what this flags.

WHAT IT CHECKS, per quotation block:

    PAGE_MISSING   the cited shamela page is not in the cache at all
    TEXT_ABSENT    the quoted Arabic does not occur on the cited page
                   (and, when it is found elsewhere in the same book, the page it is really on)
    PRINTED_WRONG  the printed ج/ص in the citation is not the one the cached file reports
    BOOK_BANNED    the citation rests on تاریخ الطبری (9783), which is never used alone

Matching is deliberately forgiving about everything that is not a letter: harakat, tatweel,
editorial brackets, the printed edition's footnote markers, punctuation and every kind of
whitespace are stripped, and the letter forms that Shamela varies (أ إ آ ٱ / ى ي / ة ه / ؤ ئ) are
folded together. What is left is compared as a substring, so a real quotation passes and a
half-remembered one does not. A quotation broken by … is split there and each piece checked
separately, since that is how the notes elide.
"""
import io
import os
import re
import sys
import json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, "sources", "shamela")
NOTES = os.path.join(ROOT, "docs", "research")

BANNED = {"9783": "تاریخ الطبری — corroboration only, never alone (CLAUDE.md §4)"}
MIN_FRAGMENT = 18          # shorter than this and a substring match proves nothing

HARAKAT = re.compile(r"[ؐ-ًؚ-ٰٟۖ-ۭـ]")
ARABIC_ONLY = re.compile(r"[^ء-ي]")
# Two different Arabic-Indic digit blocks are in play: U+0660.. (Arabic) and U+06F0.. (Persian,
# which is the form the notes and the Urdu material actually use). Fold both to ASCII.
AR_DIGITS = {}
for _block in ("٠١٢٣٤٥٦٧٨٩", "۰۱۲۳۴۵۶۷۸۹"):
    AR_DIGITS.update({ord(a): ord(b) for a, b in zip(_block, "0123456789")})
URL_RE = re.compile(r"https?://shamela\.ws/book/(\d+)/(\d+)")
FOLD = str.maketrans({"أ": "ا", "إ": "ا", "آ": "ا", "ٱ": "ا", "ى": "ي", "ة": "ه", "ؤ": "و", "ئ": "ي"})


def norm(s):
    """Arabic letters only, folded — everything a typesetter can vary is thrown away."""
    s = HARAKAT.sub("", s).translate(FOLD)
    return ARABIC_ONLY.sub("", s)


def printed_of(header_line):
    """'PRINTED PAGE: ج7 ص404   (shamela index 3550)' -> ('7', '404'); 'ص121' -> ('', '121')."""
    m = re.search(r"PRINTED PAGE:\s*(.*?)\s*\(shamela", header_line)
    raw = m.group(1) if m else ""
    juz = re.search(r"ج\s*([^\s]+?)\s*(?:-|ص|$)", raw)
    page = re.search(r"(?:ص\s*)?(\d+)\s*$", raw)
    return (juz.group(1) if juz else "", page.group(1) if page else "")


class Book(object):
    """A book's cached pages, normalised once, so a miss can be traced to the right page."""
    _loaded = {}

    def __init__(self, book):
        self.book = book
        self.dir = os.path.join(CACHE, book)

    def page(self, idx):
        key = (self.book, idx)
        if key not in Book._loaded:
            path = os.path.join(self.dir, "%s.txt" % idx)
            if not os.path.exists(path):
                Book._loaded[key] = None
            else:
                text = io.open(path, encoding="utf-8").read()
                head, _, body = text.partition("=" * 72)
                Book._loaded[key] = (printed_of(head), norm(body or text))
        return Book._loaded[key]

    def find(self, fragment):
        """Which cached page of this book actually carries this fragment, if any."""
        for name in sorted(os.listdir(self.dir)):
            if not name.endswith(".txt"):
                continue
            idx = name[:-4]
            got = self.page(idx)
            if got and fragment in got[1]:
                return idx
        return None


def blocks_of(text):
    """Every quotation block: (line_no, arabic lines, citation line, book, index)."""
    out, lines = [], text.splitlines()
    for i, line in enumerate(lines):
        m = URL_RE.search(line)
        if not m or not line.lstrip().startswith(">"):
            continue
        arabic = []
        j = i - 1
        while j >= 0 and lines[j].lstrip().startswith(">"):
            prev = lines[j].lstrip()[1:].strip()
            if URL_RE.search(prev) or prev.startswith("*English:") or not prev:
                break
            arabic.insert(0, prev)
            j -= 1
        out.append((i + 1, arabic, line.strip(), m.group(1), m.group(2)))
    return out


def check_note(path):
    text = io.open(path, encoding="utf-8").read()
    problems, checked = [], 0
    for lineno, arabic, cite, book, idx in blocks_of(text):
        checked += 1
        where = "%s:%d" % (os.path.basename(path), lineno)
        if book in BANNED:
            problems.append((where, "BOOK_BANNED", BANNED[book], cite[:110]))
            continue
        bk = Book(book)
        got = bk.page(idx)
        if got is None:
            problems.append((where, "PAGE_MISSING", "no sources/shamela/%s/%s.txt" % (book, idx), cite[:110]))
            continue
        (juz, page), body = got

        cited = cite.translate(AR_DIGITS)
        cj = re.search(r"ج\s*(?:ـ\s*)?(?:ال)?([^\s·]+)", cited)
        cp = re.search(r"ص\s*(\d+)", cited)
        cpr = re.search(r"ص\s*(\d+)\s*[–—-]\s*(\d+)", cited)
        if cpr and page and page in (cpr.group(1), cpr.group(2)):
            cp = None
        if cp and page and cp.group(1) != page:
            problems.append((where, "PRINTED_WRONG",
                             "cites ص%s, page is ص%s" % (cp.group(1), page), cite[:110]))
        elif cj and juz and cj.group(1).strip("۔.ـ") != juz.strip("ـ").replace("ال", "", 1)                 and cj.group(1).strip("۔.ـ") != juz.strip("ـ"):
            problems.append((where, "PRINTED_WRONG",
                             "cites ج%s, page is ج%s" % (cj.group(1), juz), cite[:110]))

        # A quotation that legitimately runs over a page break is cited with a range (ص۴۶۶–۴۶۷) and
        # linked to one of the two pages, so the text is only ever half on the page the URL names.
        # Accept it against the neighbours as well, but only when the citation admits the range.
        spread = body
        if re.search(r"ص\s*\d+\s*[–—-]\s*\d+", cited):
            for nb in (str(int(idx) - 1), str(int(idx) + 1)):
                got_nb = bk.page(nb)
                if got_nb:
                    spread = (spread + got_nb[1]) if nb > idx else (got_nb[1] + spread)
            body = spread

        joined = " ".join(arabic)
        for frag in re.split(r"…|\.\.\.|\[\s*…\s*\]", joined):
            n = norm(frag)
            if len(n) < MIN_FRAGMENT:
                continue
            if n in body:
                continue
            # A quotation whose opening is on the cited page but whose tail is not has usually run
            # over a page break, or has been joined across an elision that was not marked. That is a
            # different defect from a quotation that is simply not there, so say which it is.
            head = n[:MIN_FRAGMENT * 3]
            if head in body:
                problems.append((where, "TEXT_PARTIAL",
                                 "opens on %s/%s but does not finish there — page break or unmarked elision"
                                 % (book, idx), frag[:110]))
                continue
            elsewhere = bk.find(n[:120])
            problems.append((where, "TEXT_ABSENT",
                             "not on %s/%s%s" % (book, idx,
                                                 ("; it is on %s/%s" % (book, elsewhere)) if elsewhere else
                                                 "; not found anywhere in the cached book"),
                             frag[:110]))
    return checked, problems


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    quiet = "--quiet" in sys.argv
    as_json = "--json" in sys.argv
    paths = args or sorted(os.path.join(NOTES, f) for f in os.listdir(NOTES)
                           if f.endswith(".md") and f != "INDEX.md")
    report, total, bad = {}, 0, 0
    for p in paths:
        n, probs = check_note(p)
        total += n
        bad += len(probs)
        report[os.path.basename(p)] = {"quotations": n, "problems": probs}
        if not quiet and not as_json:
            flag = "OK " if not probs else "!! "
            sys.stdout.write("%s%-56s %4d quotations  %3d problems\n"
                             % (flag, os.path.basename(p)[:56], n, len(probs)))
            for w, kind, why, what in probs:
                out = "     %-14s %s | %s\n" % (kind, why, what)
                sys.stdout.buffer.write(out.encode("utf-8"))
    if as_json:
        sys.stdout.buffer.write(json.dumps(report, ensure_ascii=False, indent=1).encode("utf-8"))
    else:
        print("\n%d quotations checked, %d problems" % (total, bad))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
