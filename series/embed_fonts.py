"""Base64-embed the Urdu and Arabic faces into a printable, then render it to A4 PDF.

    python series/embed_fonts.py series/handout_l01.html          # -> handout_l01.pdf
    python series/embed_fonts.py series/handout_l01.html --css    # print the @font-face block only

WHY THIS EXISTS. CLAUDE.md 5 says printables are "HTML + CSS -> headless Chrome -> A4 PDF, fonts
base64-embedded via @font-face so a print shop renders it identically". The handouts were in fact
pulling Nastaliq from the Google Fonts CDN, which means:

  * no network at the print shop  ->  silent fallback to a Latin serif, and the Urdu is destroyed;
  * Google's Noto Nastaliq webfont is not necessarily the same cut as the installed desktop face,
    so the proof and the print can differ.

Embedding removes both failure modes. Chrome subsets to the glyphs actually used when it writes the
PDF, so the inline base64 does not bloat the final file.

FONT POLICY (CLAUDE.md 1.3), enforced here rather than left to a hand-written CSS stack:
  Urdu   -> Noto Nastaliq Urdu.  NEVER Jameel Noori Nastaleeq: the only cut on this machine is the
            Kasheeda variant, which elongates letters and rendered every Urdu line stretched and
            gappy. That was a real defect in the first decks and the first handout.
  Arabic -> Traditional Arabic (Naskh). Nastaliq for Qur'anic text is non-standard.

Put `<!--EMBED-FONTS-->` in the <head> of a printable and this replaces it with the @font-face
block. A file with no marker still renders; it just does not get embedded faces.
"""
import base64
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

FACES = [
    # (css family name, absolute path, weight, style)
    ("Noto Nastaliq Urdu",
     os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Windows\Fonts\NotoNastaliqUrdu-Regular.ttf"),
     "400", "normal"),
    ("Traditional Arabic", r"C:\Windows\Fonts\trado.ttf", "400", "normal"),
    ("Traditional Arabic", r"C:\Windows\Fonts\tradbdo.ttf", "700", "normal"),
]

BANNED = "Jameel Noori Nastaleeq"


def face_css():
    out, missing = [], []
    for family, path, weight, style in FACES:
        if not os.path.exists(path):
            missing.append((family, path))
            continue
        with open(path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("ascii")
        out.append("@font-face{font-family:'%s';font-weight:%s;font-style:%s;font-display:block;"
                   "src:url(data:font/ttf;base64,%s) format('truetype')}" % (family, weight, style, b64))
    return "<style>\n" + "\n".join(out) + "\n</style>", missing


def embed(path):
    with open(path, encoding="utf-8") as f:
        html = f.read()

    if BANNED in html:
        raise SystemExit("%s still references %s — forbidden by CLAUDE.md 1.3. Fix the font "
                         "stack before rendering." % (os.path.basename(path), BANNED))

    css, missing = face_css()
    for family, p in missing:
        sys.stderr.write("WARNING: %s not found at %s — falling back to the installed face.\n"
                         % (family, p))

    if "<!--EMBED-FONTS-->" in html:
        html = html.replace("<!--EMBED-FONTS-->", css)
    else:
        sys.stderr.write("WARNING: no <!--EMBED-FONTS--> marker in %s; rendering without "
                         "embedded faces.\n" % os.path.basename(path))
    return html


def to_pdf(path):
    # Chrome resolves neither `--print-to-pdf` nor a `file:///` URL against OUR cwd, so a relative
    # argument — exactly the form this file's own docstring documents — used to build the URL
    # `file:///series/handout.html` (drive root), print Chrome's error page as a single 23 KB page,
    # and drop the PDF somewhere else. Everything handed to Chrome is absolute from here on.
    path = os.path.abspath(path)
    html = embed(path)
    tmp = os.path.join(os.path.dirname(path), "_embedded_" + os.path.basename(path))
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(html)
    pdf = os.path.splitext(path)[0] + ".pdf"
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    "--print-to-pdf=%s" % pdf, "file:///" + tmp.replace("\\", "/")],
                   check=False, capture_output=True)
    os.remove(tmp)
    return pdf


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    if "--css" in sys.argv:
        print(face_css()[0][:400] + "\n... (truncated)")
        raise SystemExit(0)
    p = to_pdf(sys.argv[1])
    print("%-40s %8.1f KB" % (os.path.basename(p), os.path.getsize(p) / 1024))
