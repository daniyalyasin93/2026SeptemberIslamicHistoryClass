"""Fetch pages from al-Maktaba al-Shamela (shamela.ws) as clean, citable Arabic text.

Shamela carries the classical Arabic corpus already typed and searchable, so Arabic
quotations for the lecture series can be verified against the actual work rather than
paraphrased from the Urdu. URL shape: https://shamela.ws/book/<book_id>/<page>

    python tools/shamela.py get 34 110              # one page
    python tools/shamela.py get 34 110 --raw        # without vowel marks
    python tools/shamela.py range 34 108 115        # a span of pages

Pages are cached under sources/shamela/<book_id>/<page>.txt, so a citation once fetched
costs nothing to re-check and the exact text used is reproducible.

The page number in the URL is Shamela's internal index; the printed page it displays is
usually one higher. BOTH are recorded in the cached file header — cite the printed one.
"""
import argparse
import io
import os
import re
import sys
import time
import urllib.request

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0 Safari/537.36")
CACHE = os.path.join("sources", "shamela")
HARAKAT = re.compile(r"[ؐ-ًؚ-ٰٟۖ-ۭ]")


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA,
                                               "Accept-Language": "ar,en;q=0.8"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def untag(fragment):
    """HTML fragment -> plain text, one line per block."""
    s = re.sub(r"<(?:br|/p|/div|/h\d)[^>]*>", "\n", fragment)
    s = re.sub(r"<[^>]+>", "", s)
    s = (s.replace("&nbsp;", " ").replace("&amp;", "&")
          .replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"'))
    lines = [re.sub(r"[ \t]+", " ", ln).strip() for ln in s.split("\n")]
    return "\n".join(ln for ln in lines if ln)


def grab(html, cls):
    m = re.search(r'<div[^>]*class="[^"]*\b%s\b[^"]*"[^>]*>(.*?)</div>' % cls,
                  html, flags=re.S)
    return untag(m.group(1)) if m else ""


def parse(html):
    head = grab(html, "page-header")
    title = ""
    mt = re.search(r"<title>(.*?)</title>", html, flags=re.S)
    if mt:
        title = untag(mt.group(1))
    printed = ""
    mp = re.search(r"^\s*ص(\d+)", title)
    if mp:
        printed = mp.group(1)
    return {
        "title": title,
        "printed": printed,
        "header": head,
        "body": grab(html, "nass"),
        "notes": grab(html, "hamesh"),
    }


def get(book, page, strip_harakat=False, force=False):
    path = os.path.join(CACHE, str(book), "%s.txt" % page)
    if os.path.exists(path) and not force:
        return io.open(path, encoding="utf-8").read()

    url = "https://shamela.ws/book/%s/%s" % (book, page)
    p = parse(fetch(url))
    body = p["body"]
    if strip_harakat:
        body = HARAKAT.sub("", body)

    out = [
        "SOURCE: %s" % url,
        "TITLE : %s" % p["title"],
        "PRINTED PAGE: %s   (shamela index %s)" % (p["printed"] or "?", page),
        "CHAPTER: %s" % p["header"].replace("\n", " / "),
        "=" * 72,
        body,
    ]
    if p["notes"]:
        out += ["", "-" * 24 + " الهامش " + "-" * 24, p["notes"]]
    text = "\n".join(out)

    os.makedirs(os.path.dirname(path), exist_ok=True)
    io.open(path, "w", encoding="utf-8").write(text)
    return text


def emit(s):
    sys.stdout.buffer.write((s + "\n").encode("utf-8"))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    g = sub.add_parser("get")
    g.add_argument("book"); g.add_argument("page", type=int)

    r = sub.add_parser("range")
    r.add_argument("book"); r.add_argument("start", type=int); r.add_argument("end", type=int)

    for p in (g, r):
        p.add_argument("--raw", action="store_true", help="strip vowel marks")
        p.add_argument("--force", action="store_true", help="refetch, ignore cache")

    a = ap.parse_args()
    pages = [a.page] if a.cmd == "get" else list(range(a.start, a.end + 1))
    for i, pg in enumerate(pages):
        if i:
            time.sleep(1.0)          # be a polite client
        try:
            emit(get(a.book, pg, a.raw, a.force))
            if len(pages) > 1:
                emit("\n" + "#" * 72 + "\n")
        except Exception as e:
            emit("ERROR on page %s: %s: %s" % (pg, type(e).__name__, e))


if __name__ == "__main__":
    main()
