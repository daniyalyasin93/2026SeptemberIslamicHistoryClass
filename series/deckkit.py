"""Shared python-pptx helpers for the lecture decks.

    import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "series"))
    from deckkit import *

Palette, fonts and slide furniture live here so ten decks cannot drift apart.
Slides stay LIGHT — depth belongs in the speaker script.
"""
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Emu, Inches, Pt

TEAL = RGBColor(0x10, 0x4A, 0x43)
DARK = RGBColor(0x0A, 0x32, 0x2E)
GOLD = RGBColor(0xC4, 0x9A, 0x45)
CREAM = RGBColor(0xFA, 0xF7, 0xF0)
INK = RGBColor(0x1C, 0x23, 0x21)
MAROON = RGBColor(0x7A, 0x2E, 0x2E)

UR = "Jameel Noori Nastaleeq"     # Urdu — Nastaliq
AR = "Traditional Arabic"          # Arabic — Naskh. Never Nastaliq for Qur'an/hadith.
EN = "Georgia"
ENB = "Segoe UI"

W, H = Inches(13.333), Inches(7.5)


def set_cs(run, face):
    """Complex-script typeface, so Urdu/Arabic shape correctly while Latin keeps its own font."""
    rPr = run._r.get_or_add_rPr()
    cs = rPr.find(qn("a:cs"))
    if cs is None:
        cs = rPr.makeelement(qn("a:cs"), {})
        rPr.append(cs)
    cs.set("typeface", face)


def rtl(par):
    par._p.get_or_add_pPr().set("rtl", "1")
    par.alignment = PP_ALIGN.RIGHT


def deck():
    p = Presentation()
    p.slide_width, p.slide_height = W, H
    return p


def blank(prs, bg=CREAM):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    r = s.shapes.add_shape(1, 0, 0, W, H)
    r.fill.solid(); r.fill.fore_color.rgb = bg; r.line.fill.background()
    r.shadow.inherit = False
    return s


def text(slide, txt, x, y, w, h, size=28, color=INK, font=EN, cs=UR,
         bold=False, align=PP_ALIGN.LEFT, is_rtl=False, spacing=1.0):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    for i, line in enumerate(txt.split("\n")):
        par = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        par.line_spacing = spacing
        run = par.add_run(); run.text = line
        f = run.font
        f.size, f.bold, f.name = Pt(size), bold, font
        f.color.rgb = color
        set_cs(run, cs)
        par.alignment = align
        if is_rtl:
            rtl(par)
    return tb


def rule(slide, x, y, w, color=GOLD, thick=Pt(2)):
    ln = slide.shapes.add_shape(1, x, y, w, Emu(int(thick)))
    ln.fill.solid(); ln.fill.fore_color.rgb = color; ln.line.fill.background()
    ln.shadow.inherit = False


def note(slide, s):
    slide.notes_slide.notes_text_frame.text = s


def eyebrow(slide, label):
    text(slide, label, Inches(0.9), Inches(0.5), Inches(8), Inches(0.4),
         size=12, color=TEAL, font=ENB, bold=True)


def quote_slide(prs, arabic, urdu, cite, label=None):
    """The house pattern for a sourced quotation: Arabic in Naskh, Urdu beneath, reference under it.

    Used wherever a conclusion is stated — the attribution carries it, never the speaker.
    """
    s = blank(prs)
    if label:
        eyebrow(s, label)
    text(s, arabic, Inches(0.7), Inches(1.9), Inches(11.9), Inches(1.9),
         size=34, color=DARK, cs=AR, align=PP_ALIGN.CENTER, is_rtl=True, spacing=1.35)
    text(s, urdu, Inches(0.7), Inches(4.0), Inches(11.9), Inches(1.5),
         size=23, color=INK, cs=UR, align=PP_ALIGN.CENTER, is_rtl=True, spacing=1.5)
    text(s, cite, Inches(0.7), Inches(5.9), Inches(11.9), Inches(0.5),
         size=15, color=TEAL, cs=UR, align=PP_ALIGN.CENTER, is_rtl=True)
    return s


def save(prs, path):
    """PowerPoint holds a lock on an open file — fall back rather than lose the build."""
    try:
        prs.save(path)
        return path
    except PermissionError:
        alt = path.replace(".pptx", "_NEW.pptx")
        prs.save(alt)
        return alt
