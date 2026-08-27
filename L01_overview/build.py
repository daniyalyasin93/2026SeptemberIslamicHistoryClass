"""Build L01 "The Whole Map" — fourteen centuries in one evening.

    python L01_overview/build.py

English carries the slides; Urdu appears only where it works, always with English beside it.
Latin digits throughout — mixing Urdu-Indic digits with Latin punctuation makes the bidi
algorithm reorder the line into nonsense. Depth lives in Script.md, not here.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "series"))
from deckkit import *  # noqa: F401,F403
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt


def paradigms(prs):
    """The 'how we know' material, cut down to one slide. Not a methodology lecture."""
    s = blank(prs, CREAM)
    eyebrow(s, "how do we know any of this?")
    text(s, "Two ways of knowing the past", Inches(0.85), Inches(1.0), Inches(11.6), Inches(0.9),
         size=38, color=TEAL, font=EN)
    band(s, Inches(2.15), Inches(0.04), GOLD, Inches(0.85), Inches(11.6))

    for x, head, body, col in [
        (0.85, "The modern method",
         "Dig, infer, connect the dots.\nNo chain of transmission.\nNo rule for accepting or\nrejecting a report.", MUTED),
        (7.1, "The Islamic method",
         "Every report carries a chain\nback to an eyewitness — and\nevery narrator in that chain\nhas a documented life.", DARK),
    ]:
        text(s, head, Inches(x), Inches(2.5), Inches(5.4), Inches(0.6),
             size=25, color=(TEAL if col == DARK else MUTED), font=EN, bold=False)
        text(s, body, Inches(x), Inches(3.25), Inches(5.4), Inches(2.4),
             size=21, color=col, font=EN, spacing=1.45)

    text(s, "So when you hear “there is no historical basis for that” — ask which method is speaking.",
         Inches(0.85), Inches(5.85), Inches(11.6), Inches(0.6),
         size=19, color=MAROON, font=EN, italic=True)
    note(s, "0:33 (4 min). THE ONLY METHODOLOGY IN THE WHOLE COURSE - keep it to four minutes.\n"
            "Do not teach isnad as a technical subject. The point is only: there are two different\n"
            "ways of deciding what is true about the past, and ours has a mechanism the other lacks.\n"
            "Be fair, not mocking - they work hard, they simply have no isnad system.\n"
            "Then go straight to the Sufyan quotation and stop.")
    return s


def build(path):
    prs = deck()

    # 1
    s = title_slide(prs, "Lessons from History", "تاریخ سے سبق",
                    "Fourteen centuries in one evening",
                    "SESSION 1  ·  632 – 1947  ·  DHA ISLAMABAD")
    note(s, "0:00 AGHAZ (3 min). Workbooks and pens are already on the chairs.\n"
            "FIRST INSTRUCTION OF THE COURSE: 'apna naam likh lijiye.' Give a real 30 seconds.\n"
            "THEN THE NARRATOR PARAGRAPH - do not skip, do not rush:\n"
            "  'main mu'arrikh nahin hoon. hum ek kitab parh rahe hain - Tareekh-e-Ummat.'\n"
            "This is your shield for all ten weeks.")

    # 2 — the opening scene
    s = statement_slide(prs, "656 AH", "Baghdad falls. The libraries burn.",
                        kicker="one night, in the middle of our story", bg=DARK, fg=GOLD)
    note(s, "0:03 OPENING SCENE (5 min). STAND STILL. No map yet. Tell it plainly, do not raise\n"
            "your voice. [SOURCE: the Mongol volume - the taking of Baghdad, the caliph, and what\n"
            "the chroniclers record of the libraries. Say nothing the book does not say.]\n"
            "END: walk to the BANNER and mark one filled square at 656. Room copies it. PEN-DOWN 1.\n"
            "Then the two questions - AND DO NOT ANSWER THEM.")

    # 3 — the whole line
    s = statement_slide(prs, "That night sits in the middle.",
                        "Not at the end. So how much came before — and how much after?",
                        line="line_full", kicker="you are here")
    note(s, "Point at the BANNER, not the screen. They have just marked 656 themselves and can see\n"
            "blank line on both sides. Let them sit with it.")

    # 4 — the map
    s = map_slide(prs, "map_s1_sweep", "The whole map, once",
                  "six cities to remember", line=None)
    note(s, "0:08 THE STORY (20 min) begins here. Six moves, ~3 min each.\n"
            "Introduce the six anchor cities FIRST - they are the furniture for all ten weeks.\n"
            "Then walk the arrows: out of Arabia, west to Cordoba, east to Sindh, north to\n"
            "Constantinople.")

    # 5-10 — the six moves
    moves = [
        ("One city. One generation.", "Madina, 632. Nobody expected what came next.",
         "line_s2", "move 1", CREAM,
         "Move 1. The Prophet (peace be upon him) has died. At this moment nobody would have\n"
         "predicted anything that follows."),
        ("Spain and Sindh — the same decade.", "West to the Atlantic, east to the Indus, at once.",
         "line_s4", "move 2", CREAM,
         "Move 2. THE STRIKING FACT. Say it slowly - nobody expects it.\n"
         "PEN-DOWN 2: 'do teer kheenchiye - ek maghrib, ek mashriq.' [verify 92-93 AH]"),
        ("Two capitals at once.", "Baghdad translating the world; Cordoba building a library.",
         "line_s5", "move 3", CREAM,
         "Move 3. [trim to one sentence first if running long.]"),
        ("The capital falls — and it does not end.", "The books and the scholars had already moved to Cairo.",
         "line_s6", "move 4", DARK,
         "Move 4. Now the opening mark gets its meaning. THE KEY IDEA OF THE WHOLE EVENING:\n"
         "a civilisation survived losing its capital because it had moved what mattered.\n"
         "PEN-DOWN 3. [SOURCE: what actually survived 656 and where it went.]"),
        ("1453 — a door opens.", "Constantinople. And in the east, Sindh leads on to Delhi.",
         "line_s7", "move 5", CREAM,
         "Move 5. The recovery. [verify 1453]"),
        ("1924 … and then 1947.", "The last caliphate ends. And the story arrives here.",
         "line_s9", "move 6", DARK,
         "Move 6. SOBER. No present-day politics - the venue has ruled it out.\n"
         "PEN-DOWN 4, the last mark.\n"
         "If asked about 1924 -> SEVENTH session. About 1947 -> NINTH. Do not mix them up."),
    ]
    for big, sub, line, kick, bg, nt in moves:
        s = statement_slide(prs, big, sub, line=line, kicker=kick, bg=bg,
                            fg=(GOLD if bg == DARK else TEAL))
        note(s, nt)

    # 11 — taaruf divider
    s = statement_slide(prs, "Three people", "Each one has their own evening later in the course.",
                        kicker="تعارف  ·  who you are meeting", bg=TEAL, fg=CREAM)
    note(s, "0:28 TAARUF (7 min). SAY FIRST: all three get their own session; tonight is an\n"
            "introduction only. READ EACH FROM THE PRINTED CARD - never from memory.\n"
            "Workbook prints the first lines and leaves ONE INCIDENT blank for them to write.")

    people = [
        ("Umar ibn al-Khattab", "سیدنا عمر الفاروق ؓ", "AL-FARUQ — the one who separates truth from falsehood",
         "الفاروق", "SECOND CALIPH  ·  COMES BACK IN SESSION 2",
         "In his time Persia was ended and Byzantium lost Syria and Egypt — and he built the\nadministration that governed it.",
         "[SOURCE: Siyar A'lam al-Nubala — dates and one incident, read off the page]",
         "Meets them properly next week. Do not spend his material tonight."),
        ("Hulagu Khan", "ہلاکو خان", "", "", "COMES BACK IN SESSION 6",
         "The Mongol commander who took Baghdad in 656 AH and ended the Abbasid caliphate there.",
         "[SOURCE: the Mongol volume]",
         "WARNING: his incident must NOT be the fall of Baghdad - that was tonight's opening scene\n"
         "and the segment would simply repeat itself. Pick something else."),
        ("Mehmed the Conqueror", "سلطان محمد فاتح", "", "", "COMES BACK IN SESSION 7",
         "Took Constantinople in 1453, thirty-nine years before Granada was lost in the west.",
         "[SOURCE: no work on the shelf reaches the Ottomans — blocked until a volume arrives]",
         "BLOCKED for sourcing. If you have nothing verified by the night, introduce only the\n"
         "two you do have and say the third comes in session 7."),
    ]
    for en, ur, lq_en, lq_ur, dates, did, cite, nt in people:
        s = person_slide(prs, en, ur, lq_en, lq_ur, dates, did, "—", cite)
        note(s, nt)

    # 14-15 — the one methodology moment
    paradigms(prs)
    s = quote_slide(
        prs,
        "لَمَّا اسْتَعْمَلَ الرُّوَاةُ الْكَذِبَ اسْتَعْمَلْنَاهُمُ التَّارِيخَ",
        "“When narrators began inventing, we used dates against them.”",
        "SUFYAN AL-THAWRI  ·  TAREEKH-E-UMMAT, MUQADDIMA, p.57",
        label="how a forgery dies",
        urdu="جب راوی جھوٹی روایتیں گھڑنے لگے تو ہم نے تاریخ سے کام لیا")
    note(s, "0:37 (2 min). DEMONSTRATE FIRST, then show this.\n"
            "'Suppose someone tells you Mehmed the Conqueror wrote to Hulagu Khan.'\n"
            "Point at THEIR OWN sheet - two centuries apart. Dead. No Arabic needed, no isnad\n"
            "needed; the timeline alone killed it. THEN put this up, read once, and STOP.")

    # 16 — aaj ki baat
    s = blank(prs, CREAM)
    eyebrow(s, "آج کی بات  ·  today's point — not mine")
    text(s, "Shams-ul-Haq Afghani", Inches(0.85), Inches(1.05), Inches(7.5), Inches(0.7),
         size=30, color=TEAL, font=EN)
    text(s, "مولانا شمس الحق افغانی رحمہ اللہ", Inches(7.6), Inches(1.0), Inches(4.9), Inches(0.7),
         size=24, color=TEAL, font=UR, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True, spacing=1.9)
    text(s, "Four things a people needs in order to rise —", Inches(0.85), Inches(1.95),
         Inches(11.6), Inches(0.5), size=20, color=MUTED, font=EN, italic=True)
    for i, (en, ur) in enumerate([
            ("Connection to its own past", "ماضی سے ارتباط"),
            ("Unity of thought and action", "وحدتِ فکر و عمل"),
            ("Building the means of strength", "فراہمیِ اسبابِ قوت"),
            ("Sustained effort", "جہدِ مسلسل")]):
        y = 2.55 + i * 0.78
        text(s, "%d" % (i + 1), Inches(0.9), Inches(y), Inches(0.5), Inches(0.6),
             size=22, color=GOLD, font=SANS, bold=True)
        text(s, en, Inches(1.5), Inches(y), Inches(6.2), Inches(0.6),
             size=25, color=(DARK if i == 0 else INK), font=EN, bold=(i == 0))
        text(s, ur, Inches(7.8), Inches(y - 0.06), Inches(4.7), Inches(0.7),
             size=22, color=(DARK if i == 0 else MUTED), font=UR, cs=UR,
             align=PP_ALIGN.RIGHT, is_rtl=True, spacing=1.8)
    text(s, "TAREEKH-E-UMMAT, MUQADDIMA, p.53", Inches(0.85), Inches(5.95), Inches(11.6), Inches(0.4),
         size=13, color=TEAL, font=SANS)
    note(s, "0:39 (4 min). The slide is headed by the ATTRIBUTION, not the claim. It is not your view.\n"
            "[SOURCE: exact wording of the four and the reference the book gives - read by eye]\n"
            "Read them. ONE sentence: the FIRST is connection to the past, and the other three rest\n"
            "on it - which is why tonight began with the whole line instead of the first year.\n"
            "THEN STOP. 90 SECONDS OF SILENCE while they write their own line.\n"
            "Two volunteers max. Say 'shukriya' and NOTHING else - do not improve on what they said.")

    # 17 — close
    s = statement_slide(prs, "Next week: twelve years.",
                        "632 to 644. All of it inside that one narrow bracket.",
                        line="line_s2", kicker="اگلے ہفتے", bg=DARK, fg=CREAM)
    note(s, "0:43 (3 min). Hold up the workbook: the only thing to bring back.\n"
            "Draw a bracket on the BANNER around 11-23 AH so they SEE how narrow next week is.\n"
            "TAKE-HOME, say once and leave unanswered:\n"
            "  'koi tareekh ki baat kahe - to ab aap sab se pehle kya poochhenge?'\n"
            "  (want: when? and who said it?)")

    # 18 — sources
    s = blank(prs, CREAM)
    eyebrow(s, "sources  ·  show only if asked")
    text(s, "Tareekh-e-Ummat\nMaulana Muhammad Ismail Rehan  —  muqaddima, pp. 53, 57\n\n"
            "al-I'lan bi'l-Tawbikh\nal-Sakhawi  —  p. 111",
         Inches(0.9), Inches(1.9), Inches(11.5), Inches(3.2),
         size=24, color=INK, font=EN, spacing=1.6)
    text(s, "Every claim tonight traces to a printed page you could open yourself.",
         Inches(0.9), Inches(5.4), Inches(11.5), Inches(0.5),
         size=19, color=MAROON, font=EN, italic=True)
    note(s, "Keep for credibility. Show only if someone asks where something came from.")

    return save(prs, path)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    print("saved:", build(os.path.join(here, "L01.pptx")))
