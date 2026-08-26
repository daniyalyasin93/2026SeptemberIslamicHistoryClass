"""Build L01 «ایک نظر میں — پورا نقشہ».  python L01_overview/build.py

Slides are deliberately LIGHT — the depth lives in Script.md. Every slide carries its
speaker note. Re-run to regenerate; never hand-edit the .pptx for structural changes.
"""
import copy
import os
import sys

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Emu, Inches, Pt

TEAL, DARK, GOLD = RGBColor(0x10, 0x4A, 0x43), RGBColor(0x0A, 0x32, 0x2E), RGBColor(0xC4, 0x9A, 0x45)
CREAM, INK, MAROON = RGBColor(0xFA, 0xF7, 0xF0), RGBColor(0x1C, 0x23, 0x21), RGBColor(0x7A, 0x2E, 0x2E)
UR, AR, EN, ENB = "Jameel Noori Nastaleeq", "Traditional Arabic", "Georgia", "Segoe UI"

W, H = Inches(13.333), Inches(7.5)


def set_cs(run, face):
    """Complex-script typeface: Urdu/Arabic shape correctly while Latin keeps its own font."""
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


# ----------------------------------------------------------------------------- slides
def build(path):
    prs = deck()

    # 1 · title
    s = blank(prs, DARK)
    text(s, "تاریخ سے سبق", Inches(0.9), Inches(1.9), Inches(11.5), Inches(1.6),
         size=60, color=CREAM, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True, spacing=1.6)
    text(s, "Lessons from History  ·  نشست ۱", Inches(0.9), Inches(3.5), Inches(11.5), Inches(0.6),
         size=22, color=GOLD, font=EN)
    rule(s, Inches(0.9), Inches(4.35), Inches(3.2))
    text(s, "وَأَسْبَابِ مَبَادِئِ الدُّوَلِ وَإِقْبَالِهَا، ثُمَّ سَبَبِ انْقِرَاضِهَا",
         Inches(0.9), Inches(4.7), Inches(11.5), Inches(0.9),
         size=26, color=CREAM, cs=AR, align=PP_ALIGN.RIGHT, is_rtl=True)
    text(s, "علامہ سخاوی رحمہ اللہ  ·  الإعلان بالتوبيخ، ص۱۱۱",
         Inches(0.9), Inches(5.7), Inches(11.5), Inches(0.5),
         size=15, color=GOLD, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True)
    note(s, "0:00 AGHAZ (3 min). Names into workbooks first - 30 real seconds, do not talk over it.\n"
            "THEN THE NARRATOR PARAGRAPH - do not skip, do not rush. 'I am not a historian, I read a book.'\n"
            "This is your shield for ten weeks.")

    # 2 · opening scene — nothing on screen
    s = blank(prs, DARK)
    text(s, "۶۵۶ھ", Inches(0.9), Inches(3.0), Inches(11.5), Inches(1.4),
         size=72, color=GOLD, cs=UR, align=PP_ALIGN.CENTER)
    note(s, "0:03 OPENING SCENE (5 min). STAND STILL. No map, no movement. Tell Baghdad plainly.\n"
            "[SOURCE: the Mongol volume - the taking of Baghdad in 656, the caliph's name, and what the\n"
            "chroniclers record of the libraries. Say nothing the book does not say.]\n"
            "END: walk to the banner, mark ONE filled square at 656. 'aap bhi yehi nishaan laga lijiye'.\n"
            "PEN-DOWN 1. Then the two questions - DO NOT ANSWER THEM.")

    # 3 · the line
    s = blank(prs)
    eyebrow(s, "THE LINE  ·  وقت")
    text(s, "۱۱ھ ← ۱۹۴۷", Inches(0.9), Inches(2.6), Inches(11.5), Inches(1.2),
         size=54, color=TEAL, cs=UR, align=PP_ALIGN.CENTER)
    text(s, "آٹھ نشان  ·  چودہ سو سال  ·  ایک شام",
         Inches(0.9), Inches(4.0), Inches(11.5), Inches(0.7),
         size=24, color=INK, cs=UR, align=PP_ALIGN.CENTER, is_rtl=True)
    note(s, "Point at the banner, not the screen. The screen is scaffolding; the banner is the object.")

    # 4-9 · the six moves
    moves = [
        ("۱", "مدینہ، ۱۱ھ", "ایک شہر، ایک نسل",
         "Move 1. One city. Nobody expects what follows."),
        ("۲", "اندلس اور سندھ", "ایک ہی دہائی میں — مغرب اور مشرق",
         "Move 2. THE striking fact of the course. Say it slowly. Draw BOTH arrows.\n"
         "PEN-DOWN 2: 'do teer kheenchiye - ek maghrib, ek mashriq'. [verify 92-93 AH]"),
        ("۳", "بغداد اور قرطبہ", "ایک ہی صدیوں میں دو مرکز",
         "Move 3. Two capitals at once. [trim to one sentence first if running long]"),
        ("۴", "ٹوٹ", "بغداد گیا — کتابیں قاہرہ چلی گئیں",
         "Move 4. Now the opening mark gets its meaning. The civilisation survived because the\n"
         "books and the scholars had already moved. PEN-DOWN 3.\n"
         "[SOURCE: what actually survived 656 and where it went]"),
        ("۵", "قسطنطنیہ، ۸۵۷ھ", "اور مشرق میں سندھ سے دہلی تک",
         "Move 5. The recovery. [verify 857]"),
        ("۶", "۱۹۲۴ … ۱۹۴۷", "زوال، اور پھر — یہاں",
         "Move 6. Sober, no politics. PEN-DOWN 4 - the last mark.\n"
         "If asked about 1924 -> SEVENTH session. About 1947 -> NINTH. Do not mix them up."),
    ]
    for num, head, sub, nt in moves:
        s = blank(prs)
        text(s, num, Inches(0.9), Inches(0.6), Inches(1.2), Inches(1.0),
             size=40, color=GOLD, cs=UR, bold=True)
        rule(s, Inches(0.9), Inches(1.7), Inches(2.0))
        text(s, head, Inches(0.9), Inches(2.4), Inches(11.5), Inches(1.3),
             size=48, color=TEAL, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True, spacing=1.5)
        text(s, sub, Inches(0.9), Inches(4.0), Inches(11.5), Inches(0.9),
             size=26, color=INK, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True, spacing=1.5)
        note(s, nt)

    # 10 · taaruf divider
    s = blank(prs, TEAL)
    text(s, "تعارف", Inches(0.9), Inches(2.9), Inches(11.5), Inches(1.4),
         size=64, color=CREAM, cs=UR, align=PP_ALIGN.CENTER)
    text(s, "تین لوگ  ·  تینوں کی اپنی نشست آ رہی ہے",
         Inches(0.9), Inches(4.4), Inches(11.5), Inches(0.7),
         size=22, color=GOLD, cs=UR, align=PP_ALIGN.CENTER, is_rtl=True)
    note(s, "0:28 TAARUF (7 min). SAY FIRST: all three get their own session; tonight is introduction only.\n"
            "READ EACH FROM THE PRINTED CARD - never from memory.\n"
            "WARNING: Hulagu's waqi'a must NOT be the fall of Baghdad - that was tonight's opening scene.")

    for who, when in [("سیدنا عمر الفاروق ؓ", "اگلے ہفتے"),
                      ("ہلاکو خان", "چھٹی نشست"),
                      ("سلطان محمد فاتح", "ساتویں نشست")]:
        s = blank(prs)
        text(s, who, Inches(0.9), Inches(2.3), Inches(11.5), Inches(1.4),
             size=46, color=TEAL, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True, spacing=1.6)
        rule(s, Inches(9.6), Inches(3.9), Inches(2.8))
        text(s, when, Inches(0.9), Inches(4.2), Inches(11.5), Inches(0.7),
             size=22, color=GOLD, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True)
        note(s, "Four lines, read from the card: naam o nasab / sunain / one sentence / EK WAQI'A.\n"
                "[SOURCE: all four lines. The laqab field stays EMPTY until read off the page.]\n"
                "Workbook prints the first three and leaves 'ek waqi'a' blank for them to write.")

    # 14 · kaise pata chala
    s = blank(prs)
    eyebrow(s, "کیسے پتا چلا؟")
    text(s, "لَمَّا اسْتَعْمَلَ الرُّوَاةُ الْكَذِبَ اسْتَعْمَلْنَاهُمُ التَّارِيخَ",
         Inches(0.9), Inches(2.5), Inches(11.5), Inches(1.2),
         size=40, color=DARK, cs=AR, align=PP_ALIGN.CENTER, is_rtl=True)
    text(s, "جب راوی جھوٹی روایتیں گھڑنے لگے تو ہم نے اُن کی جانچ کے لیے تاریخ سے کام لیا",
         Inches(0.9), Inches(4.0), Inches(11.5), Inches(0.9),
         size=24, color=INK, cs=UR, align=PP_ALIGN.CENTER, is_rtl=True, spacing=1.5)
    text(s, "سفیان ثوری رحمہ اللہ  ·  تاریخِ امت، مقدمہ، ص۵۷",
         Inches(0.9), Inches(5.3), Inches(11.5), Inches(0.5),
         size=16, color=TEAL, cs=UR, align=PP_ALIGN.CENTER, is_rtl=True)
    note(s, "0:35 (3 min). FIRST the demonstration, THEN the slide.\n"
            "'Suppose someone says Muhammad al-Fatih wrote a letter to Hulagu.' Point at THEIR OWN sheet.\n"
            "Two centuries apart. Done. No Arabic needed, no isnad needed - the timeline alone killed it.\n"
            "THEN put this up, read once, STOP. Teach no further method tonight.")

    # 15 · aaj ki baat
    s = blank(prs)
    eyebrow(s, "آج کی بات")
    text(s, "مولانا شمس الحق افغانی رحمہ اللہ فرماتے ہیں",
         Inches(0.9), Inches(1.5), Inches(11.5), Inches(0.8),
         size=26, color=TEAL, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True)
    text(s, "ماضی سے ارتباط\nوحدتِ فکر و عمل\nفراہمیِ اسبابِ قوت\nجہدِ مسلسل",
         Inches(0.9), Inches(2.5), Inches(11.5), Inches(2.8),
         size=34, color=INK, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True, spacing=1.7)
    text(s, "تاریخِ امت، مقدمہ، ص۵۳",
         Inches(0.9), Inches(5.6), Inches(11.5), Inches(0.5),
         size=16, color=TEAL, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True)
    note(s, "0:38 (4 min). The slide is headed by the ATTRIBUTION, not the claim. It is not your view.\n"
            "[SOURCE: exact wording of the four + the reference the book gives - read by eye]\n"
            "Read the four. ONE sentence of connection: 'pehli cheez maazi se irtibaat hai, baaqi teenon\n"
            "isi par khari hain.' THEN STOP.\n"
            "90 SECONDS OF SILENCE while they write. Two volunteers max. Say 'shukriya' and NOTHING else -\n"
            "do not improve or build on what they said.")

    # 16 · close
    s = blank(prs, DARK)
    text(s, "اگلے ہفتے — بارہ سال", Inches(0.9), Inches(2.4), Inches(11.5), Inches(1.3),
         size=50, color=CREAM, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True, spacing=1.6)
    text(s, "۱۱ھ  ←  ۲۳ھ", Inches(0.9), Inches(3.9), Inches(11.5), Inches(0.8),
         size=30, color=GOLD, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True)
    rule(s, Inches(0.9), Inches(5.0), Inches(11.5), CREAM, Pt(1))
    text(s, "کوئی تاریخ کی بات کہے — تو اب آپ سب سے پہلے کیا پوچھیں گے؟",
         Inches(0.9), Inches(5.3), Inches(11.5), Inches(0.9),
         size=26, color=GOLD, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True)
    note(s, "0:42 (3 min). Hold up the workbook: 'yehi ek cheez agle hafte saath laani hai.'\n"
            "Draw a bracket on the banner around 11-23 AH so they SEE how narrow next week is.\n"
            "Say the take-home question ONCE, slowly, write it on the banner, and LEAVE IT UNANSWERED.\n"
            "(want: 'kab? aur kis ne kaha?')")

    # 17 · sources
    s = blank(prs)
    eyebrow(s, "SOURCES  ·  show only if asked")
    text(s, "تاریخِ امت — مولانا محمد اسماعیل ریحان\nمقدمہ، ص۵۳ · ص۵۷\n\n"
            "الإعلان بالتوبيخ — علامہ سخاوی رحمہ اللہ، ص۱۱۱",
         Inches(0.9), Inches(2.2), Inches(11.5), Inches(3.0),
         size=24, color=INK, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True, spacing=1.6)
    note(s, "Keep for credibility. Show only if someone asks where something came from.")

    try:
        prs.save(path)
    except PermissionError:
        alt = path.replace(".pptx", "_NEW.pptx")
        prs.save(alt)
        return alt
    return path


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    out = build(os.path.join(here, "L01.pptx"))
    print("saved:", out)
