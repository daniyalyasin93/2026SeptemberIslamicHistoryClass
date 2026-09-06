"""Export a deck to PNGs and a contact sheet, so a slide can be LOOKED AT before it is delivered.

    python series/preview.py L02_baarah_saal/L02.pptx           # -> ..._preview/ + ..._sheet.png
    python series/preview.py L02_baarah_saal/L02.pptx --slides 4 7 12

WHY THIS EXISTS. Session 1's decks were built blind — written in python-pptx, never rendered, and
seen for the first time by the audience. The verdict was "the slides you made were ugly", and the
specific failures (type too small for the back rows, boxes colliding, dead space) are all things a
single glance would have caught. python-pptx cannot rasterise, but PowerPoint is installed on this
machine and will export a deck to images from the command line, so there is no excuse for building
blind.

The contact sheet is the point: one image showing every slide at once makes an inconsistency
obvious in a way that clicking through a deck does not.

Requires PowerPoint (COM) and Pillow. Both are present on Daniyal's machine.
"""
import os
import subprocess
import sys
import glob

from PIL import Image

PPT_SAVE_AS_PNG = 18


def export(pptx, outdir=None):
    """PowerPoint -> one PNG per slide. Returns the directory of images."""
    pptx = os.path.abspath(pptx)
    outdir = os.path.abspath(outdir or os.path.splitext(pptx)[0] + "_preview")
    if os.path.isdir(outdir):
        for f in {f.lower() for f in glob.glob(os.path.join(outdir, "*.PNG")) +
                  glob.glob(os.path.join(outdir, "*.png"))}:
            os.remove(f)

    # SaveCopyAs, not SaveAs — SaveAs would repoint the open presentation at the image folder.
    ps = (
        "$ErrorActionPreference='Stop';"
        "$app = New-Object -ComObject PowerPoint.Application;"
        "$p = $app.Presentations.Open('%s', $true, $false, $false);"
        "$p.SaveCopyAs('%s', %d);"
        "$p.Close(); $app.Quit();"
        "[System.Runtime.InteropServices.Marshal]::ReleaseComObject($app) | Out-Null"
        % (pptx.replace("'", "''"), outdir.replace("'", "''"), PPT_SAVE_AS_PNG)
    )
    r = subprocess.run(["powershell", "-NoProfile", "-NonInteractive", "-Command", ps],
                       capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit("PowerPoint export failed:\n" + (r.stderr or r.stdout)[:1500])
    return outdir


def _n(path):
    d = "".join(c for c in os.path.basename(path) if c.isdigit())
    return int(d) if d else 0


def sheet(imgdir, out=None, cols=2, width=760, only=None):
    """Every slide on one page. This is the artifact worth looking at."""
    # On Windows the filesystem is case-insensitive, so globbing both "*.PNG" and "*.png"
    # returns every file twice. Dedupe on the lowercased path before sorting.
    found = glob.glob(os.path.join(imgdir, "*.PNG")) + glob.glob(os.path.join(imgdir, "*.png"))
    files = sorted({f.lower(): f for f in found}.values(), key=_n)
    if only:
        files = [f for f in files if _n(f) in set(only)]
    if not files:
        raise SystemExit("no slide images in " + imgdir)

    ims = [Image.open(f).convert("RGB") for f in files]
    th = int(width * ims[0].height / ims[0].width)
    rows = (len(ims) + cols - 1) // cols
    pad = 10
    # a mid grey ground, so a white slide's own edges are visible against it
    sh = Image.new("RGB", (cols * width + pad * (cols + 1), rows * th + pad * (rows + 1)),
                   (120, 120, 120))
    for i, im in enumerate(ims):
        r, c = divmod(i, cols)
        sh.paste(im.resize((width, th), Image.LANCZOS), (pad + c * (width + pad), pad + r * (th + pad)))
    out = out or os.path.join(os.path.dirname(imgdir.rstrip("\\/")),
                              os.path.basename(imgdir.rstrip("\\/")).replace("_preview", "") + "_sheet.png")
    sh.save(out)
    return out, len(ims)


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        raise SystemExit(__doc__)
    only = None
    if "--slides" in args:
        i = args.index("--slides")
        only = [int(a) for a in args[i + 1:]]
        args = args[:i]
    d = export(args[0])
    out, n = sheet(d, only=only)
    print("%-46s %d slides" % (os.path.relpath(out), n))
    print("%-46s per-slide PNGs" % os.path.relpath(d))
