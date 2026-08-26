# -*- coding: utf-8 -*-
"""
insert_map.py — drop an image (a map) into a specific slide, fitted into a box (aspect preserved).
Places the picture on top of the placeholder area on that slide. Re-runnable.

Examples:
  python insert_map.py --deck ../Lecture1/Lecture1.pptx --slide 15 --image ../maps/world_632ce.png
  python insert_map.py --deck ../Lecture1/Lecture1.pptx --slide 15 --image map.png --x 0.7 --y 1.5 --w 8.4 --h 5.4

Defaults match the map placeholder on Lecture 1, slide 15. Slide numbers are 1-based.
A .bak copy is written unless --no-backup. Use --out to write a separate file.
"""
import argparse, os, shutil, sys
from pptx import Presentation
from pptx.util import Inches
try:
    from PIL import Image
except ImportError:
    Image = None

def main():
    ap = argparse.ArgumentParser(description="Insert a fitted image into a pptx slide.")
    ap.add_argument("--deck", required=True)
    ap.add_argument("--slide", type=int, required=True, help="1-based slide number")
    ap.add_argument("--image", required=True)
    ap.add_argument("--x", type=float, default=0.7, help="box left, inches")
    ap.add_argument("--y", type=float, default=1.5, help="box top, inches")
    ap.add_argument("--w", type=float, default=8.4, help="box width, inches")
    ap.add_argument("--h", type=float, default=5.4, help="box height, inches")
    ap.add_argument("--out", default=None)
    ap.add_argument("--no-backup", action="store_true")
    a = ap.parse_args()

    for f in (a.deck, a.image):
        if not os.path.exists(f):
            sys.exit(f"Not found: {f}")
    prs = Presentation(a.deck)
    slides = list(prs.slides)
    if not (1 <= a.slide <= len(slides)):
        sys.exit(f"--slide {a.slide} out of range (deck has {len(slides)} slides)")
    slide = slides[a.slide - 1]

    box_w, box_h = Inches(a.w), Inches(a.h)
    if Image is not None:
        iw, ih = Image.open(a.image).size
        scale = min(box_w / iw, box_h / ih)
        w, h = int(iw * scale), int(ih * scale)
        x = int(Inches(a.x) + (box_w - w) / 2)
        y = int(Inches(a.y) + (box_h - h) / 2)
        slide.shapes.add_picture(a.image, x, y, width=w, height=h)
    else:
        # no PIL: fill the box (may distort); install Pillow for aspect-correct fit
        slide.shapes.add_picture(a.image, Inches(a.x), Inches(a.y), width=box_w, height=box_h)

    out = a.out or a.deck
    if out == a.deck and not a.no_backup:
        shutil.copy(a.deck, a.deck + ".bak")
        print("Backup ->", a.deck + ".bak")
    prs.save(out)
    print(f"Inserted '{os.path.basename(a.image)}' into slide {a.slide} -> {out}")
    print("Tip: open in PowerPoint and send the placeholder box behind / delete it if it still shows.")

if __name__ == "__main__":
    main()
