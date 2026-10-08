# -*- coding: utf-8 -*-
"""Can the font draw it? Every Arabic character on a slide must have a glyph in the font it is set in.

    python series/glyphs.py SNN_<slug>/SNN.pptx          # every character a face or its notes cannot draw
    python series/glyphs.py --fix SNN_<slug>/SNN.pptx    # spell the honorific ligatures out, in place

WHY THIS EXISTS (docs/VISION.md Q5, DECISIONS.md #79). Daniyal, 2026-10-08: "there seems to be some errors in
arabic on slide 104". The page of Ibn Kathīr prints «عز وجل» as one calligraphic sort, and Shamela types that
sort as ONE character, U+FDFF. Traditional Arabic has no glyph for it. PowerPoint drew an empty box — and,
because one character in the run had sent it looking for another font, set every letter of that line apart
from its neighbours. One missing glyph, a whole line of broken Arabic.

It was the third time. Evening 2 cut the character off by hand (L02_baarah_saal/build.py, cards 22, 26, 53);
evening 3 left the box and flagged it "for Daniyal to decide" (#34.5). Nothing checked, so evening 6 walked
into it again — and the 23–41 AH pool carries «﵁» on thirty-eight cards.

So, two things, and both are in this file:

  * SPELLED — the honorific ligatures no font on this machine can draw, each with the words it is the
    ligature OF. The pool keeps the page's bytes; the face and the notes get the words. Nothing is added to
    the quotation: U+FDFF is, by its name in the Unicode standard, ARABIC LIGATURE AZZA WA JALL. The table is
    closed, and every row is checked against that name when this module is imported.
  * gaps() — every Arabic character on every face, tested against the cmap of the font its run is set in.
    deck2.audit() calls it, so a deck with a character that cannot be drawn is never written.

Latin is not tested. A transliterated ḥ that Georgia lacks is borrowed from another font, letter by letter,
and reads; an Arabic letter cannot be borrowed without breaking the word it is joined into.
"""
import os
import re
import sys
import unicodedata

# The ligature -> (its name in the Unicode standard, the words it stands for). Only the ones that occur in the
# pools: anything else stops the build in gaps(), and is given a row here by somebody who has looked at it.
SPELLED = {
    "\ufd40": ("RAHIMAHU ALLAAH", "رحمه الله"),
    "\ufd41": ("RADI ALLAAHU ANH", "رضي الله عنه"),
    "\ufd42": ("RADI ALLAAHU ANHAA", "رضي الله عنها"),
    "\ufd43": ("RADI ALLAAHU ANHUM", "رضي الله عنهم"),
    "\ufd44": ("RADI ALLAAHU ANHUMAA", "رضي الله عنهما"),
    "\ufd47": ("ALAYHI AS-SALAAM", "عليه السلام"),
    "\ufd4a": ("ALAYHI AS-SALAATU WAS-SALAAM", "عليه الصلاة والسلام"),
    "\ufdff": ("AZZA WA JALL", "عز وجل"),
}
for _ch, (_name, _words) in SPELLED.items():
    if unicodedata.name(_ch) != "ARABIC LIGATURE " + _name:
        raise AssertionError("glyphs.SPELLED: U+%04X is %s, not %s" % (ord(_ch), unicodedata.name(_ch), _name))

_LIGATURE = re.compile("(.?)([%s])(.?)" % "".join(SPELLED), re.S)
_ARABIC = re.compile("[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]")
# what the system reaches for when a notes pane meets Arabic: a character in none of these is drawn by nothing
FALLBACK = ("Traditional Arabic", "Arabic Typesetting", "Segoe UI")
A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"


def spell(text):
    """`text` with every honorific ligature in SPELLED written as its words, a space kept on either side."""
    text = str(text)
    if not any(ch in text for ch in SPELLED):
        return text

    def words(m):
        before, ch, after = m.group(1), m.group(2), m.group(3)
        return (before + ("" if not before or before.isspace() else " ") + SPELLED[ch][1]
                + (" " if after.isalnum() or after in SPELLED else "") + after)

    while any(ch in text for ch in SPELLED):             # two ligatures side by side overlap one match
        text = _LIGATURE.sub(words, text, count=1)
    return text


# --------------------------------------------------------------------------- the fonts on this machine

def _registry():
    out = {}
    try:
        import winreg
    except ImportError:                                   # not Windows: nothing is installed that we can vouch for
        return out
    for hive, base in ((winreg.HKEY_LOCAL_MACHINE, os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts")),
                       (winreg.HKEY_CURRENT_USER, "")):
        try:
            key = winreg.OpenKey(hive, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts")
        except OSError:
            continue
        i = 0
        while True:
            try:
                name, val, _ = winreg.EnumValue(key, i)
            except OSError:
                break
            i += 1
            path = val if os.path.isabs(val) else os.path.join(base, val)
            for family in name.split(" (")[0].split(" & "):
                out.setdefault(family.strip(), path)      # the regular cut is registered under the bare name
    return out


_REG, _CMAP = None, {}


def cmap(face):
    """The code points `face` has a glyph for, or None when the font is not installed here."""
    global _REG
    if face not in _CMAP:
        if _REG is None:
            _REG = _registry()
        path = _REG.get(face or "")
        if not path or not os.path.exists(path):
            _CMAP[face] = None
        else:
            try:
                from fontTools.ttLib import TTFont
            except ImportError:
                raise SystemExit("series/glyphs.py needs fontTools to read a font's cmap: pip install fonttools")
            kw = {"fontNumber": 0} if path.lower().endswith(".ttc") else {}
            _CMAP[face] = frozenset(TTFont(path, lazy=True, **kw).getBestCmap() or ())
    return _CMAP[face]


def _tested(ch):
    return bool(_ARABIC.match(ch)) and unicodedata.category(ch) != "Cf"


def _faces(run):
    rpr = run._r.find(A + "rPr")
    lat = cs = None
    if rpr is not None:
        e = rpr.find(A + "latin")
        lat = e.get("typeface") if e is not None else None
        e = rpr.find(A + "cs")
        cs = e.get("typeface") if e is not None else None
    return cs or lat


def gaps(prs):
    """[(slide no, where, character, font)] — every Arabic character a slide cannot draw.

    On a face: the character is not in the cmap of the font its run is set in (`where` is the box's name).
    In the notes: no font the system would fall back on has it (`where` is "notes")."""
    out = []
    for n, slide in enumerate(prs.slides, 1):
        for sh in slide.shapes:
            if not sh.has_text_frame:
                continue
            for p in sh.text_frame.paragraphs:
                for r in p.runs:
                    face = _faces(r)
                    have = cmap(face)
                    for ch in sorted(set(r.text)):
                        if _tested(ch) and (have is None or ord(ch) not in have):
                            out.append((n, sh.name or "a text box", ch, face if have is not None
                                        else "%s (not installed)" % face))
        if slide.has_notes_slide:
            for ch in sorted(set(slide.notes_slide.notes_text_frame.text)):
                if _tested(ch) and not any(ord(ch) in (cmap(f) or ()) for f in FALLBACK):
                    out.append((n, "notes", ch, "any font"))
    return out


def describe(gap):
    n, where, ch, face = gap
    row = (" — it is an honorific ligature: give it a row in series/glyphs.py SPELLED"
           if unicodedata.name(ch, "").startswith("ARABIC LIGATURE") and ch not in SPELLED else "")
    return ("slide %d (%s): «%s» U+%04X %s has no glyph in %s — PowerPoint draws a box and breaks the joining "
            "of the whole line%s" % (n, where, ch, ord(ch), unicodedata.name(ch, "?"), face, row))


def fix(path):
    """Spell the ligatures out in a deck that already exists — every run on every face, and the notes — and
    change nothing else. The way to mend a deck Daniyal has edited (DECISIONS.md #67): his file, in place."""
    from pptx import Presentation
    prs = Presentation(path)
    changed = 0
    for slide in prs.slides:
        frames = [sh.text_frame for sh in slide.shapes if sh.has_text_frame]
        if slide.has_notes_slide:
            frames.append(slide.notes_slide.notes_text_frame)
        for tf in frames:
            for p in tf.paragraphs:
                for r in p.runs:
                    new = spell(r.text)
                    if new != r.text:
                        r.text, changed = new, changed + 1
    if changed:
        prs.save(path)
    return changed, gaps(prs)


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    args = [a for a in sys.argv[1:] if a != "--fix"]
    if not args:
        raise SystemExit(__doc__)
    if "--fix" in sys.argv:
        lock = os.path.join(os.path.dirname(os.path.abspath(args[0])), "~$" + os.path.basename(args[0]))
        if os.path.exists(lock):
            raise SystemExit("%s is open in PowerPoint — close it first; nothing was changed." % args[0])
        done, left = fix(args[0])
        print("%d run(s) respelled in %s" % (done, args[0]))
    else:
        from pptx import Presentation
        left = gaps(Presentation(args[0]))
    for g in left:
        print(describe(g))
    print("every Arabic character can be drawn" if not left else "%d character(s) cannot be drawn" % len(left))
    sys.exit(1 if left else 0)
