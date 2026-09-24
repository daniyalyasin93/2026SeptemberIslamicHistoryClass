# -*- coding: utf-8 -*-
"""Make a shareable copy of a deck: no hidden slides, images recompressed, notes dropped by default.

    python tools/share_deck.py S04_kinda_butah_yamama/S04.pptx                 # for the room
    python tools/share_deck.py S04_kinda_butah_yamama/S04.pptx --keep-notes    # for the team

Why each of the three:

* **The notes are production apparatus.** They carry the ⚠ warnings, the card ids, "do not say",
  "SPEAKER'S DISCRETION", and the pointers into `QA_BANK.md`. `DECISIONS.md` #30 keeps that class of
  text off a slide face; a file handed to strangers is the same problem with a longer life — so they
  come out unless `--keep-notes` says otherwise. **For a review by the team they are the point**:
  the warnings are what a reviewer is being asked to check, so that is what the flag is for.
* **Hidden slides are alternates**, not content — the STOP A and STOP B closes. They do not appear in
  a slideshow, but anyone scrolling the file sees them and reads two endings that were never given.
* **The images are the size.** A hand-edited deck comes back from PowerPoint with its renders
  re-embedded at full resolution; the flat map and Line art quantises to a palette with no visible
  loss, which is where the megabytes go.

The source file is opened read-only and never written back — hand edits in it are not ours to lose.
"""
import io
import os
import shutil
import sys
import zipfile

from PIL import Image
from pptx import Presentation

if hasattr(sys.stdout, "reconfigure"):          # the console is cp1252; the report has ⚠ and ؓ in it
    sys.stdout.reconfigure(encoding="utf-8")

MAX_EDGE = 1920          # a 16:9 slide at 1920 is sharp on any screen and on most projectors
JPEG_Q = 85


def strip(src, dst, keep_notes=False):
    """Copy the deck, dropping hidden slides — and the notes too unless they are being kept."""
    shutil.copyfile(src, dst)
    prs = Presentation(dst)
    id_lst = prs.slides._sldIdLst
    hidden = noted = 0

    for sld_id in list(id_lst):
        rid = sld_id.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
        slide = prs.slides.get(int(sld_id.get('id')))
        if slide._element.get('show') == '0':
            id_lst.remove(sld_id)
            prs.part.drop_rel(rid)
            hidden += 1

    if not keep_notes:
        for slide in prs.slides:
            for rel_id, rel in list(slide.part.rels.items()):
                if rel.reltype.endswith('/notesSlide'):
                    slide.part.drop_rel(rel_id)
                    noted += 1

    prs.save(dst)
    return len(prs.slides._sldIdLst), hidden, noted


def shrink_media(path):
    """Rewrite the package with every ppt/media image downscaled and recompressed, names unchanged."""
    tmp = path + '.tmp'
    saved = 0
    with zipfile.ZipFile(path) as zin, zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            low = item.filename.lower()
            if low.startswith('ppt/media/') and low.endswith(('.png', '.jpg', '.jpeg')):
                try:
                    new = recompress(data, low)
                except Exception as exc:                      # a broken image is left exactly as it was
                    print('   ! left alone: %s (%s)' % (item.filename, exc))
                    new = data
                if len(new) < len(data):
                    saved += len(data) - len(new)
                    data = new
            zout.writestr(item, data)
    os.replace(tmp, path)
    return saved


def recompress(data, name):
    im = Image.open(io.BytesIO(data))
    im.load()
    if max(im.size) > MAX_EDGE:
        ratio = MAX_EDGE / float(max(im.size))
        im = im.resize((max(1, int(im.width * ratio)), max(1, int(im.height * ratio))), Image.LANCZOS)
    out = io.BytesIO()
    if name.endswith('.png'):
        # flat cartographic art: an adaptive 256-colour palette is visually identical and a fraction
        # of the size. Anything with real transparency keeps its alpha.
        if im.mode in ('RGBA', 'LA') and im.getchannel('A').getextrema()[0] < 255:
            im.quantize(colors=256, method=Image.FASTOCTREE).save(out, 'PNG', optimize=True)
        else:
            im.convert('RGB').quantize(colors=256, method=Image.MEDIANCUT).save(out, 'PNG', optimize=True)
    else:
        im.convert('RGB').save(out, 'JPEG', quality=JPEG_Q, optimize=True, progressive=True)
    return out.getvalue()


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    keep_notes = '--keep-notes' in sys.argv
    src = args[0]
    dst = args[1] if len(args) > 1 else src.replace('.pptx', '_share.pptx')
    before = os.path.getsize(src)
    slides, hidden, noted = strip(src, dst, keep_notes)
    saved = shrink_media(dst)
    after = os.path.getsize(dst)
    kept = sum(1 for s in Presentation(dst).slides if s.has_notes_slide)
    print('%-44s %7.1f MB  %d slides' % (os.path.basename(src), before / 1048576.0,
                                         slides + hidden))
    print('%-44s %7.1f MB  %d slides   (-%d hidden, %s, %.1f MB of images saved)'
          % (os.path.basename(dst), after / 1048576.0, slides, hidden,
             ('%d notes pages KEPT' % kept) if keep_notes else ('-%d notes pages' % noted),
             saved / 1048576.0))
    print('   %.0f%% smaller' % (100 * (1 - after / float(before))))
    if keep_notes:
        print('   ⚠ the notes carry the ⚠ warnings, card ids and "do not say" lines — this copy is '
              'for the team, not for the room')


if __name__ == '__main__':
    main()
