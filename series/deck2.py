"""deck2 — the v4 slide kit. White ground, hard type floor, no bullet slides.

    from series import deck2 as D
    prs = D.deck()
    D.title_slide(prs, "Twelve Years", "11-23 AH", "Session 2")
    D.image_slide(prs, "map_s2_ridda.png", "Eleven armies leave Medina")
    D.statement_slide(prs, arabic="...", english="...", cite="البدایہ ج۷ ص۲۹")
    D.save(prs, "L02.pptx")            # <- runs the audit; raises on any violation

WHY THIS EXISTS (DECISIONS.md #21). Session 1's deck came back with three verdicts that all point
the same way: "the slides you made were ugly", "text-heavy with font size unreadable on ladies
side", and "more visual/graphical content will be appreciated." The division of labour is now
explicit — Claude produces the words and the structure, Gemini produces the pictures, Daniyal
merges them. This module builds the half Claude is actually good at, and makes the other half easy
to drop in.

THREE THINGS IT DOES THAT deckkit.py DID NOT:

  1. WHITE GROUND, ALWAYS. Not a palette preference — a merge requirement. Pure #FFFFFF is the one
     colour a generated image reproduces exactly, so a Gemini picture drops onto the slide with no
     visible seam. Series identity moves to a teal title bar and a gold rule, which is also far
     more legible from the back of a hall than cream-on-cream was.

  2. A TYPE FLOOR THAT IS ENFORCED, NOT DOCUMENTED. Every run is checked on save. Nothing below
     24pt survives, body is 28pt, a statement is 44pt or more. The one exemption is scaffolding
     that is meant to be deleted — the image placeholders — and it is marked in the shape name so
     the audit can see it is deliberate.

  3. REAL IMAGE PLACEHOLDERS. A visual slide with no picture yet gets a correctly-sized, editable
     box carrying its own IMAGE BRIEF, and the brief is repeated in the speaker notes. Daniyal
     pastes the Gemini output straight over it. Nothing is flattened, ever.

SIX PERMITTED SLIDE KINDS. Anything that is only a line of text is not a slide.

    image_slide      a photograph or a generated illustration — the picture carries it
    map_slide        a map on the left, up to five key lines down the right
    statement_slide  one large quotation, Arabic Naskh over its English rendering
    diagram_slide    boxes and arrows built here, or a rendered diagram image
    timeline_slide   the Line, with a caption
    lessons_slide    the closing summary — the evening's عبرت lines together

    lessons_slide is the SINGLE deliberate exception to "no bullet-list slides". It exists because
    the close of the evening is a summary by design (DECISIONS.md #23), and a summary of five
    one-sentence lessons is a list whether or not we call it one. It is capped at six lines, each
    line must be a whole thought, and the type is 28pt — it cannot decay into a bullet slide.
"""
import os
import re

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.dml import MSO_LINE_DASH_STYLE
from pptx.oxml.ns import qn

# --------------------------------------------------------------------------- palette
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
TEAL = RGBColor(0x10, 0x4A, 0x43)
DARK = RGBColor(0x0A, 0x32, 0x2E)
GOLD = RGBColor(0xC4, 0x9A, 0x45)
CREAM = RGBColor(0xFA, 0xF7, 0xF0)
INK = RGBColor(0x1C, 0x23, 0x21)
MUTED = RGBColor(0x5A, 0x68, 0x62)
MAROON = RGBColor(0x7A, 0x2E, 0x2E)
RULE = RGBColor(0xD8, 0xD2, 0xC4)

_HAS_AR = re.compile("[؀-ۿﭐ-﷿ﹰ-﻿]")
AR = "Traditional Arabic"
# Traditional Arabic HAS NO GLYPH for U+0613 ؓ (رضي الله عنه) — verified against trado.ttf's
# cmap. Every ؓ in session 1 rendered as a dotted circle because of it. Arabic Typesetting
# ships with Windows, is also Naskh, and carries U+0610–U+0615 as well as ﷺ, so any run that
# contains an honorific sign is set in it instead. Quotations with no honorific keep
# Traditional Arabic, so the look of the Arabic on a statement slide does not change.
AR_HON = "Arabic Typesetting"
_HONORIFIC = re.compile("[\u0610-\u0615\u0617-\u061A]")       # Naskh. Nastaliq for Arabic is non-standard (CLAUDE.md 1.3)
EN = "Georgia"                  # English headlines
SANS = "Segoe UI"               # English body

# --------------------------------------------------------------------------- the contract
MIN_PT = 24                     # nothing on any slide is smaller than this. No exceptions.
BODY_PT = 28
STATEMENT_MIN_PT = 44
HEADLINE_PT = 40
MAX_BODY_WORDS = 20

W, H = Inches(13.333), Inches(7.5)
BAND_H = Inches(1.18)
MARGIN = Inches(0.62)
CONTENT_Y = Inches(1.52)
CONTENT_H = Inches(5.42)
CONTENT_W = W - 2 * MARGIN

VIS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "visuals")

# Shapes whose name begins with this are scaffolding: a box Daniyal deletes when he pastes the
# real picture over it. The audit skips them, and says so, rather than silently ignoring them.
SCAFFOLD = "PLACEHOLDER::"

_briefs = []                    # collected IMAGE BRIEFs, written beside the deck on save

# --------------------------------------------------------------------------- audience safety
# STANDING RULE (DECISIONS.md #30). A slide FACE carries only what the room may see. Production
# apparatus — certainty labels, tier tags, card ids, notes to the speaker, build markers — goes in
# the SPEAKER NOTES, never on the slide. This is enforced rather than remembered because it is the
# kind of thing that survives every review and then appears on a projector in front of 200 people.
FORBIDDEN = [
    (r"\[SOURCED\]|\[STANDARD\]|\[CONVENTIONAL-ESTIMATE\]", "a certainty label"),
    (r"\bCUT-IF-SHORT\b|\bCUT IF SHORT\b", "a build marker"),
    (r"\bTier\s*:|^\s*(?:CORE|GOOD|CUT)\b[^a-z]", "a tier tag"),   # anchored: "good." in a sentence is not a tier tag
    (r"\bE-[A-Z]{1,4}\d", "a card id"),
    (r"\b(?:RCT|ABU|ABD|ISA|QMA|BAM|UTS|NTS|GSA|IKO|THO|AHA|ZIA|TMW)/", "a card id"),
    (r"IMAGE BRIEF|IMAGE GOES HERE|placeholder|TODO|TBD|FIXME", "build scaffolding"),
    (r"\bClaude\b|\bGemini\b|\bChatGPT\b|\bAI[- ]generated\b|\bLLM\b", "an AI marker"),
    (r"\bspeaker'?s discretion\b|\bhands[- ]up\b|\[HANDS\]|\bWORKSHEET\b",
     "an instruction to the speaker"),
    (r"\bto verify\b|\(to verify\)", "an unresolved-source marker"),
    (r"\bn/a\b", "a placeholder value"),
    (r"shamela\.ws|https?://", "a URL — cite the printed page, not a link"),
]
_FORBIDDEN = [(re.compile(p, re.I | re.M), why) for p, why in FORBIDDEN]


class DeckContractError(AssertionError):
    """A slide violated the deck contract. The build fails rather than shipping it."""


# --------------------------------------------------------------------------- primitives

def set_cs(run, face):
    """Set the complex-script face too, or PowerPoint renders Arabic in the Latin font."""
    rPr = run._r.get_or_add_rPr()
    cs = rPr.find(qn("a:cs"))
    if cs is None:
        cs = rPr.makeelement(qn("a:cs"), {})
        rPr.append(cs)
    cs.set("typeface", face)


# Combining marks and tatweel. They inflate len() without occupying width, so measuring a
# vowelled quotation by raw length over-counted its lines by a third and pushed the English
# rendering down onto the citation.
_MARKS = re.compile("[ً-ٰٟۖ-ۭـ]")


def _ar_len(txt):
    return len(_MARKS.sub("", str(txt)))


def _count_words(txt):
    return len([w for w in str(txt).replace("\n", " ").split(" ") if w.strip()])


def text(slide, txt, x, y, w, h, size=BODY_PT, color=INK, font=EN, bold=False,
         align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, line=1.25, rtl=False,
         italic=False, scaffold=False, name=None):
    """A text box. Refuses anything under the type floor unless it is scaffolding."""
    if size < MIN_PT and not scaffold:
        raise DeckContractError(
            "%.0fpt is below the %dpt floor (DECISIONS.md #21) — text was %r. The back of the "
            "hall could not read session 1; raise the size or cut the words."
            % (size, MIN_PT, str(txt)[:60]))

    box = slide.shapes.add_textbox(x, y, w, h)
    if name:
        box.name = name
    tf = box.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Inches(0.04)
    tf.margin_top = tf.margin_bottom = 0

    for i, para_txt in enumerate(str(txt).split("\n")):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = line
        if rtl:
            pPr = p._p.get_or_add_pPr()
            pPr.set("rtl", "1")
            pPr.set("algn", "r")
        r = p.add_run()
        r.text = para_txt
        r.font.size = Pt(size)
        r.font.name = font
        r.font.bold = bold
        r.font.italic = italic
        r.font.color.rgb = color
        # Pick the complex-script face from what the run actually contains. A Latin headline
        # carrying ؓ or ﷺ still needs an Arabic face, and if it carries a Companion
        # honorific that face has to be one that HAS the glyph.
        if _HONORIFIC.search(para_txt):
            r.font.name = AR_HON if font == AR else font
            set_cs(r, AR_HON)
        elif font != AR and _HAS_AR.search(para_txt):
            set_cs(r, AR)
        else:
            set_cs(r, font)
    return box


def rect(slide, x, y, w, h, fill=None, line_color=None, line_w=Pt(1.5), dash=False, name=None):
    sh = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    if name:
        sh.name = name
    if fill is None:
        sh.fill.background()
    else:
        sh.fill.solid()
        sh.fill.fore_color.rgb = fill
    if line_color is None:
        sh.line.fill.background()
    else:
        sh.line.color.rgb = line_color
        sh.line.width = line_w
        if dash:
            sh.line.dash_style = MSO_LINE_DASH_STYLE.DASH
    sh.shadow.inherit = False
    return sh


def deck():
    prs = Presentation()
    prs.slide_width, prs.slide_height = W, H
    return prs


def blank(prs):
    """A white slide. Every slide in a v4 deck starts here."""
    s = prs.slides.add_slide(prs.slide_layouts[6])
    bg = s.background.fill
    bg.solid()
    bg.fore_color.rgb = WHITE
    return s


def note(slide, s):
    slide.notes_slide.notes_text_frame.text = str(s)


def header(slide, headline, kicker=None):
    """The teal title bar and the gold rule — the whole of the series identity."""
    rect(slide, 0, 0, W, BAND_H, fill=TEAL, name="band")
    rect(slide, 0, BAND_H, W, Pt(4.5), fill=GOLD, name="rule")

    if kicker:
        text(slide, kicker, MARGIN, Inches(0.10), CONTENT_W, Inches(0.32),
             size=MIN_PT, color=GOLD, font=SANS, bold=True)
        y, h = Inches(0.44), Inches(0.66)
    else:
        y, h = Inches(0.20), Inches(0.80)

    text(slide, headline, MARGIN, y, CONTENT_W, h, size=HEADLINE_PT, color=CREAM,
         font=EN, bold=True, anchor=MSO_ANCHOR.MIDDLE)
    return slide


# --------------------------------------------------------------------------- the five kinds

def title_slide(prs, title, dates, session):
    s = blank(prs)
    rect(s, 0, 0, W, H, fill=TEAL)
    rect(s, MARGIN, Inches(3.30), Inches(2.2), Pt(6), fill=GOLD)
    text(s, session, MARGIN, Inches(1.70), CONTENT_W, Inches(0.5),
         size=MIN_PT, color=GOLD, font=SANS, bold=True)
    text(s, title, MARGIN, Inches(2.20), CONTENT_W, Inches(1.1),
         size=60, color=WHITE, font=EN, bold=True)
    text(s, dates, MARGIN, Inches(3.70), CONTENT_W, Inches(0.7),
         size=32, color=CREAM, font=SANS)
    return s


def section_slide(prs, title, sub=None):
    s = blank(prs)
    rect(s, 0, Inches(2.9), W, Inches(1.7), fill=CREAM)
    rect(s, 0, Inches(2.9), Pt(9), Inches(1.7), fill=GOLD)
    text(s, title, Inches(0.95), Inches(3.05), W - Inches(1.6), Inches(0.8),
         size=46, color=DARK, font=EN, bold=True, anchor=MSO_ANCHOR.MIDDLE)
    if sub:
        text(s, sub, Inches(0.95), Inches(3.85), W - Inches(1.6), Inches(0.6),
             size=BODY_PT, color=MUTED, font=SANS)
    return s


def image_slide(prs, image, headline, caption=None, kicker=None, brief=None, full=False):
    """A picture carries the slide.

    `image` is a filename in series/visuals, or None. When it is None — or the file is not there
    yet — a correctly-sized dashed box goes down in its place carrying the IMAGE BRIEF, so the
    deck is complete and editable before Gemini has produced anything.
    """
    s = blank(prs)
    header(s, headline, kicker)

    y = CONTENT_Y
    h = CONTENT_H - (Inches(0.62) if caption else Inches(0))
    x, w = MARGIN, CONTENT_W
    if full:
        x, w, y = Inches(0), W, BAND_H + Pt(4.5)
        h = H - y - (Inches(0.62) if caption else Inches(0))

    path = image if image and os.path.isabs(image) else os.path.join(VIS, image or "")
    if image and os.path.exists(path):
        path = _trim(path)
        pic = s.shapes.add_picture(path, x, y, height=h)
        if pic.width > w:                       # fit to the narrower axis, keep the aspect
            pic.width, pic.height = w, Emu(int(pic.height * w / pic.width))
        pic.left = x + Emu(int((w - pic.width) / 2))
        pic.top = y + Emu(int((h - pic.height) / 2))
    else:
        _placeholder(s, x, y, w, h, brief or headline, image)

    if caption:
        if _count_words(caption) > MAX_BODY_WORDS:
            raise DeckContractError("caption is %d words, the cap is %d: %r"
                                    % (_count_words(caption), MAX_BODY_WORDS, caption))
        text(s, caption, MARGIN, H - Inches(0.70), CONTENT_W, Inches(0.5),
             size=MIN_PT, color=MUTED, font=SANS, align=PP_ALIGN.CENTER)

    if brief:
        _briefs.append((len(prs.slides._sldIdLst), headline, brief))
        note(s, "IMAGE BRIEF (paste into Gemini):\n\n%s\n\nFlat pure white #FFFFFF background, "
                "no border, no text in the image." % brief)
    return s


def _trim(path, tol=8):
    """Crop a uniform border off an image, cached beside it as .trim.png.

    Several of the map assets are rendered with an inch of white around them. Placed as-is, the
    map itself ends up filling a third of the slide and reads as a small picture on a big empty
    slide — which was one of the "too dry" complaints. Only acts when the border is genuinely
    uniform and removing it is worth doing.
    """
    try:
        from PIL import Image, ImageChops
    except ImportError:
        return path
    cache = os.path.splitext(path)[0] + ".trim.png"
    if os.path.exists(cache) and os.path.getmtime(cache) >= os.path.getmtime(path):
        return cache
    try:
        im = Image.open(path).convert("RGB")
        bg = Image.new("RGB", im.size, im.getpixel((0, 0)))
        diff = ImageChops.difference(im, bg).convert("L").point(lambda v: 255 if v > tol else 0)
        box = diff.getbbox()
        if not box:
            return path
        area_before = im.size[0] * im.size[1]
        area_after = (box[2] - box[0]) * (box[3] - box[1])
        if area_after > 0.94 * area_before:          # nothing meaningful to remove
            return path
        pad = int(0.012 * max(im.size))
        box = (max(0, box[0] - pad), max(0, box[1] - pad),
               min(im.size[0], box[2] + pad), min(im.size[1], box[3] + pad))
        im.crop(box).save(cache)
        return cache
    except Exception:                                # an asset we cannot read is not fatal
        return path


def _placeholder(s, x, y, w, h, brief, wanted):
    """Scaffolding. Deliberately ugly so it cannot be mistaken for a finished slide."""
    rect(s, x, y, w, h, fill=RGBColor(0xF4, 0xF2, 0xEC), line_color=GOLD, dash=True,
         name=SCAFFOLD + "box")
    text(s, "IMAGE GOES HERE", x, y + h / 2 - Inches(0.75), w, Inches(0.45),
         size=22, color=GOLD, font=SANS, bold=True, align=PP_ALIGN.CENTER,
         scaffold=True, name=SCAFFOLD + "label")
    text(s, (brief or "")[:220], x + Inches(0.6), y + h / 2 - Inches(0.20), w - Inches(1.2),
         Inches(1.2), size=14, color=MUTED, font=SANS, align=PP_ALIGN.CENTER,
         scaffold=True, name=SCAFFOLD + "brief")
    if wanted:
        text(s, "expected: series/visuals/%s" % wanted, x, y + h - Inches(0.44), w, Inches(0.3),
             size=11, color=MUTED, font=SANS, align=PP_ALIGN.CENTER,
             scaffold=True, name=SCAFFOLD + "path")


def map_slide(prs, image, headline, keys=(), caption=None, kicker=None, brief=None):
    """A map on the left, a short key down the right.

    The theatre of these campaigns — Egypt to Persia, Anatolia to Yemen — is very nearly square,
    and a square picture on a 16:9 slide leaves a third of the screen empty. Rather than letterbox
    it, the space carries a key: three to five places or forces, each one line, at full body size.
    It fills the slide with something the audience can actually use while looking at the map.
    """
    s = blank(prs)
    header(s, headline, kicker)

    if keys and len(keys) > 5:
        raise DeckContractError("%d key lines beside a map; five is the cap. More than that and "
                                "nobody reads the map." % len(keys))

    map_w = Emu(int(CONTENT_W * (0.60 if keys else 1.0)))
    map_h = CONTENT_H - (Inches(0.62) if caption else Inches(0))

    path = image if image and os.path.isabs(image) else os.path.join(VIS, image or "")
    if image and os.path.exists(path):
        path = _trim(path)
        pic = s.shapes.add_picture(path, MARGIN, CONTENT_Y, height=map_h)
        if pic.width > map_w:
            pic.width, pic.height = map_w, Emu(int(pic.height * map_w / pic.width))
        pic.left = MARGIN + Emu(int((map_w - pic.width) / 2))
        pic.top = CONTENT_Y + Emu(int((map_h - pic.height) / 2))
    else:
        _placeholder(s, MARGIN, CONTENT_Y, map_w, map_h, brief or headline, image)

    if keys:
        kx = MARGIN + map_w + Inches(0.34)
        kw = CONTENT_W - map_w - Inches(0.34)
        # distribute over the whole column: a fixed step collided the moment a
        # sub-line wrapped, which at a 24pt floor it very often does
        step = Emu(int((CONTENT_H - Inches(0.25)) / max(len(keys), 1)))
        for i, k in enumerate(keys):
            label, sub = (k if isinstance(k, (tuple, list)) else (k, None))
            y = CONTENT_Y + Inches(0.12) + Emu(int(i * step))
            rect(s, kx, y + Inches(0.06), Inches(0.06), Inches(0.34), fill=GOLD)
            text(s, label, kx + Inches(0.22), y, kw - Inches(0.22), Inches(0.5),
                 size=BODY_PT, color=DARK, font=EN, bold=True)
            if sub:
                # eight, not twenty: at the 24pt floor a longer line wraps, and a wrapped key
                # runs into the next one. The discipline belongs in the writing, not the layout.
                if _count_words(sub) > 8:
                    raise DeckContractError("map key line is %d words, cap is 8: %r"
                                            % (_count_words(sub), sub))
                text(s, sub, kx + Inches(0.22), y + Inches(0.46), kw - Inches(0.22),
                     step - Inches(0.46),
                     size=MIN_PT, color=MUTED, font=SANS, line=1.2)

    if caption:
        text(s, caption, MARGIN, H - Inches(0.70), CONTENT_W, Inches(0.5),
             size=MIN_PT, color=MUTED, font=SANS, align=PP_ALIGN.CENTER)

    if brief:
        _briefs.append((len(prs.slides._sldIdLst), headline, brief))
        note(s, "IMAGE BRIEF (paste into Gemini):\n\n%s\n\nFlat pure white #FFFFFF background, "
                "no border, no text in the image." % brief)
    return s


def statement_slide(prs, english, arabic=None, cite=None, headline=None, kicker=None,
                    size=None):
    """One large quotation. Arabic in Naskh on top, its English rendering beneath.

    Arabic carries authority in this room (CLAUDE.md 1.4), so where a source supplies the saying
    in Arabic it goes on the slide in Arabic — never the rendering alone.
    """
    s = blank(prs)
    if headline:
        header(s, headline, kicker)
        y = CONTENT_Y + Inches(0.25)
        avail = CONTENT_H - Inches(0.25)
    else:
        rect(s, 0, 0, Pt(9), H, fill=GOLD)
        y, avail = Inches(1.30), Inches(5.0)
    if cite:
        avail = avail - Inches(0.85)      # the citation strip is not free space to centre into

    # Measure the block, then centre it. Left top-anchored, a two-line quotation sat high with a
    # third of the slide dead beneath it — which reads as an unfinished slide, not a restrained one.
    ar_pt = size or (54 if arabic and _ar_len(arabic) < 62 else 44)
    ar_h = Inches(0.0)
    if arabic:
        if ar_pt < STATEMENT_MIN_PT:
            raise DeckContractError("a statement is %dpt or larger; got %d"
                                    % (STATEMENT_MIN_PT, ar_pt))
        per_line = 40 if ar_pt >= 54 else 52
        ar_lines = max(1, -(-_ar_len(arabic) // per_line))
        ar_h = Inches(0.30 + (0.98 if ar_pt >= 54 else 0.80) * ar_lines)

    en_pt = (size or 34) if not arabic else 30
    en_lines = max(1, -(-len(str(english)) // (58 if en_pt >= 34 else 66)))
    en_h = Inches(0.16 + (0.62 if en_pt >= 34 else 0.55) * en_lines)

    total = ar_h + en_h + (Inches(0.48) if arabic else Inches(0))
    y = y + Emu(max(0, int((avail - total) / 2)))
    top = CONTENT_Y + Inches(0.25) if headline else Inches(1.30)
    y = Emu(min(int(y), int(top + max(Emu(0), avail - total))))    # never push past the citation

    if arabic:
        text(s, arabic, MARGIN, y, CONTENT_W, ar_h, size=ar_pt, color=DARK, font=AR,
             align=PP_ALIGN.RIGHT, rtl=True, line=1.5)
        y = y + ar_h + Inches(0.14)
        rect(s, MARGIN, y, Inches(1.7), Pt(3), fill=GOLD)
        y = y + Inches(0.34)

    text(s, english, MARGIN, y, CONTENT_W, en_h, size=en_pt, color=INK,
         font=EN, italic=bool(arabic), line=1.30)

    if cite:
        text(s, cite, MARGIN, H - Inches(0.78), CONTENT_W, Inches(0.5),
             size=MIN_PT, color=MUTED, font=SANS)
    return s


def timeline_slide(prs, image, headline, caption=None, kicker=None):
    """The Line — fixed furniture. It opens and closes every session and must look identical.

    Sized to the FULL content width rather than fitted to the content height: the strip is about
    9:1, so height-fitting made it render at a fraction of the slide and the one graphic whose job
    is to re-anchor the room was the smallest thing on screen.
    """
    s = blank(prs)
    header(s, headline, kicker)

    path = image if image and os.path.isabs(image) else os.path.join(VIS, image or "")
    if image and os.path.exists(path):
        pic = s.shapes.add_picture(_trim(path), MARGIN, CONTENT_Y, width=CONTENT_W)
        avail = CONTENT_H - (Inches(0.62) if caption else Inches(0))
        if pic.height > avail:
            pic.height, pic.width = avail, Emu(int(pic.width * avail / pic.height))
            pic.left = MARGIN + Emu(int((CONTENT_W - pic.width) / 2))
        pic.top = CONTENT_Y + Emu(int((avail - pic.height) / 2))
    else:
        _placeholder(s, MARGIN, CONTENT_Y, CONTENT_W, Inches(1.6),
                     "The series timeline strip.", image)

    if caption:
        text(s, caption, MARGIN, H - Inches(0.70), CONTENT_W, Inches(0.5),
             size=MIN_PT, color=MUTED, font=SANS, align=PP_ALIGN.CENTER)
    return s


def diagram_slide(prs, headline, rows, kicker=None, caption=None):
    """Boxes and arrows, built here rather than generated. `rows` is a list of (label, sub) —
    each becomes a card across the slide. Use for a classification, a chain, a comparison."""
    s = blank(prs)
    header(s, headline, kicker)
    n = len(rows)
    if not 2 <= n <= 5:
        raise DeckContractError("a diagram slide carries 2-5 cards; got %d. More than five is a "
                                "list wearing a diagram's clothes." % n)
    gap = Inches(0.26)
    cw = Emu(int((CONTENT_W - gap * (n - 1)) / n))
    # cards fit their content instead of always running 4 inches deep
    longest = max((_count_words(sub or '') for _, sub in rows), default=0)
    card_h = Inches(2.5 + 0.20 * min(longest, 14))
    for i, (label, sub) in enumerate(rows):
        x = MARGIN + Emu(int(i * (cw + gap)))
        rect(s, x, CONTENT_Y, cw, card_h, fill=CREAM, name="card%d" % i)
        rect(s, x, CONTENT_Y, cw, Pt(7), fill=TEAL)
        text(s, label, x + Inches(0.20), CONTENT_Y + Inches(0.34), cw - Inches(0.40), Inches(1.2),
             size=32, color=DARK, font=EN, bold=True)
        if sub:
            if _count_words(sub) > MAX_BODY_WORDS:
                raise DeckContractError("diagram card is %d words, cap is %d: %r"
                                        % (_count_words(sub), MAX_BODY_WORDS, sub))
            text(s, sub, x + Inches(0.20), CONTENT_Y + Inches(1.55), cw - Inches(0.40),
                 Inches(2.2), size=MIN_PT, color=INK, font=SANS, line=1.32)
    if caption:
        text(s, caption, MARGIN, H - Inches(0.70), CONTENT_W, Inches(0.5),
             size=MIN_PT, color=MUTED, font=SANS, align=PP_ALIGN.CENTER)
    return s


def lessons_slide(prs, lessons, headline="Tonight", kicker=None):
    """The closing summary — the evening's عبرت lines together on one screen.

    The single deliberate exception to "no bullet-list slides" (see the module docstring). Capped
    at six, because a seventh would mean the evening had no shape.
    """
    if len(lessons) > 6:
        raise DeckContractError("%d lessons on the closing slide. Six is the cap — if the evening "
                                "produced more, it covered too much." % len(lessons))
    s = blank(prs)
    header(s, headline, kicker)

    # Distribute over the WHOLE content height rather than a fixed step. A fixed step assumed every
    # lesson was one line; the moment one wrapped, its neighbour's gold bar landed on top of it.
    n = max(len(lessons), 1)
    step = Emu(int((CONTENT_H - Inches(0.25)) / n))
    y0 = CONTENT_Y + Inches(0.12)
    for i, l in enumerate(lessons):
        y = y0 + Emu(int(i * step))
        rect(s, MARGIN, y + Inches(0.05), Inches(0.07), Inches(0.46), fill=GOLD)
        text(s, l, MARGIN + Inches(0.34), y, CONTENT_W - Inches(0.34), step,
             size=BODY_PT, color=INK, font=EN, anchor=MSO_ANCHOR.TOP, line=1.22)
    return s


def question_slide(prs, question, kicker="Next week"):
    """End on a question, never a summary (CLAUDE.md 2)."""
    s = blank(prs)
    rect(s, 0, 0, W, H, fill=DARK)
    rect(s, MARGIN, Inches(2.35), Inches(1.9), Pt(6), fill=GOLD)
    text(s, kicker, MARGIN, Inches(1.75), CONTENT_W, Inches(0.5),
         size=MIN_PT, color=GOLD, font=SANS, bold=True)
    text(s, question, MARGIN, Inches(2.85), CONTENT_W, Inches(2.6),
         size=46, color=WHITE, font=EN, line=1.28)
    return s


# --------------------------------------------------------------------------- the audit

def audit(prs):
    """Walk every run on every slide and enforce the contract. Called by save()."""
    bad, scaffolds = [], 0
    for i, slide in enumerate(prs.slides, 1):
        for shape in slide.shapes:
            if shape.name.startswith(SCAFFOLD):
                scaffolds += shape.name == SCAFFOLD + "box"
                continue
            if not shape.has_text_frame:
                continue
            words = 0
            face = shape.text_frame.text
            for rx, why in _FORBIDDEN:
                m = rx.search(face)
                if m:
                    bad.append("slide %d: %r is %s. It must not be on a slide FACE — put it in "
                               "the speaker notes (DECISIONS.md #30)."
                               % (i, m.group(0)[:40], why))
            for p in shape.text_frame.paragraphs:
                for r in p.runs:
                    pt = r.font.size.pt if r.font.size else None
                    if pt is None:
                        bad.append("slide %d: a run has no explicit size — it will inherit "
                                   "something small. Text: %r" % (i, r.text[:50]))
                    elif pt < MIN_PT:
                        bad.append("slide %d: %.0fpt < %dpt floor. Text: %r"
                                   % (i, pt, MIN_PT, r.text[:50]))
                    words += _count_words(r.text)
            # headline/statement boxes are allowed to be long; body boxes are not
            if shape.width < W * 0.98 and words > MAX_BODY_WORDS * 3:
                bad.append("slide %d: %d words in one box — far past the %d-word body cap. "
                           "This is the 'text-heavy' failure from session 1."
                           % (i, words, MAX_BODY_WORDS))
    if bad:
        raise DeckContractError(
            "the deck violates the contract in %d place(s):\n  - %s" % (len(bad), "\n  - ".join(bad)))
    return scaffolds


def save(prs, path, pdf=True):
    """Write the deck, and beside it a PDF preview — always (DECISIONS.md #30).

    Daniyal reads and checks on a phone and on other machines, where PowerPoint is not always to
    hand and a .pptx is not viewable. A deck nobody can open is a deck nobody checks, and session
    1's defects were all things a single glance would have caught.
    """
    scaffolds = audit(prs)
    try:
        prs.save(path)
    except PermissionError:                     # PowerPoint holds a lock on the open file
        path = os.path.splitext(path)[0] + "_NEW.pptx"
        prs.save(path)
    n = len(prs.slides._sldIdLst)
    print("%-34s %2d slides  %8.1f KB" % (os.path.basename(path), n, os.path.getsize(path) / 1024))
    if pdf:
        try:
            import sys as _sys
            _sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
            import preview as _preview
            p = _preview.to_pdf(path)
            print("%-34s %8.1f KB  (preview)" % (os.path.basename(p), os.path.getsize(p) / 1024))
        except Exception as e:                                   # noqa: BLE001
            print("   PDF preview not written: %s" % str(e)[:90])
    if scaffolds:
        print("   %d image placeholder(s) still to be filled — briefs are in the speaker notes."
              % scaffolds)
    return path


def write_briefs(path):
    """Write every IMAGE BRIEF collected during the build to a file Daniyal can work through."""
    if not _briefs:
        return None
    with open(path, "w", encoding="utf-8") as f:
        f.write("# Image briefs — paste each into Gemini, one at a time\n\n")
        f.write("Every brief already ends with the white-background instruction, so the returned\n"
                "image drops onto the slide with no seam. Keep the aspect ratio as stated.\n\n---\n\n")
        for n, headline, brief in _briefs:
            f.write("## Slide %d — %s\n\n```\n%s\n\nFlat pure white #FFFFFF background, no border, "
                    "no text in the image.\n```\n\n" % (n, headline, brief))
    print("%-34s %2d briefs" % (os.path.basename(path), len(_briefs)))
    return path
