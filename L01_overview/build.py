"""Build L01 v3 — «وقت، جگہ، اور ایک رات».

    python L01_overview/build.py            build the deck
    python L01_overview/build.py --verify   check the Arabic only, build nothing

Session 1 follows docs/specs/2026-09-03-L01-v3-spec.md §3 exactly: the evening names its
destination first, installs the guardrail at 0:02, spends eleven minutes on three nested
timelines and seven on three maps, teaches Medina's clan structure — and only then narrates
سقیفہ بنی ساعدہ, ending on the map of Arabia the night before the ردہ.

SOURCING. Nothing here is written from memory. Every Arabic string is a literal substring of a
research note in docs/research/, which took it verbatim from the Shamela cache; `verify()` runs
on every build and fails loudly if any of them drifts. Every English claim traces to a printed
page named in the same notes.

TYPESETTING (CLAUDE.md §1.3, all learned the hard way):
  * English carries the slide. Urdu appears only where it does real work, always in its own text
    box with the UR font — never in the same line or box as English.
  * Latin digits in every English context. Urdu-Indic digits only inside a pure Urdu block.
  * Honorifics are never dropped and never attach to Latin letters, so a Companion named on an
    English headline is paired with an Urdu-script name box carrying the ؓ.
  * Each citation is given twice: work and printed page in Latin for reading speed, and the
    ج/ص reference in Urdu script beneath it — so the two scripts never share a line.

THREE THINGS ARE FORBIDDEN HERE and must stay forbidden — QA_BANK.md 1.6, 1.8, 1.11: the
عصمت clause about فاطمہ ؓ (ج۵ ص۳۵۱), ابن کثیر's polemic (ج۵ ص۳۵۵), and the second inaugural
خطبہ (ج۷ ص۸, سيف بن عمر → طبری). None is quoted, paraphrased or alluded to.
Depth lives in Script.md and BRIEFING.md; this file is the projection surface only.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "series"))

from deckkit import *  # noqa: F401,F403
from make_visuals import ARABIA, PLACES, WORLD  # noqa: F401  (WORLD kept for map 1 overlays)
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt

# Two settlements the base map carries no coordinate for — same values as
# series/make_l01_visuals.py EXTRA_PLACES. PLACEMENT ONLY, never a claim about a site (MAPS.md).
PLACES = dict(PLACES, taif=(40.42, 21.27), hadramawt=(48.80, 15.60))


# ============================================================================ the Arabic
# Every string below is a literal substring of the note named beside it. Do not retype these
# by hand and do not "tidy" a vowel — run --verify after any edit.

BID = "docs/research/saqifah-bani-saida.md"          # البدایہ والنہایہ
GOV = "docs/research/governors-at-11h.md"            # البدایہ + سیر
TAR = "docs/research/tarikh-definition-and-the-guardrail.md"   # الإعلان بالتوبيخ
WAF = "docs/research/wafat-and-medina-11h.md"        # البدایہ
SUH = "docs/research/suhayl-ibn-amr.md"              # الکامل

# --- الإعلان بالتوبيخ، السخاوي رحمہ اللہ (ط الظفيري) -------------------------------------
AR_MAWDU = "وَأَمَّا مَوْضُوعُهُ فَالْإِنْسَانُ وَالزَّمَانُ."
AR_THAWRI = "لَمَّا اسْتَعْمَلَ الرّوَاةُ الْكَذِبَ، اسْتَعْمَلْنَا لَهُمُ التَّارِيخَ"
AR_HAFS = "إِذَا اتَّهَمْتُمُ الشَّيْخَ فَحَاسِبُوهُ بِالسِّنَّيْنَ"
AR_SEVEN = "أَنْتَ تَزْعُمُ أَنَّكَ سَمِعْتَ مِنْهُ بَعْدَ مَوْتِهِ بِسَبْعِ سِنِينَ"
AR_FORGED = "هَذَا مُزَوَّرٌ"
AR_KHAYBAR = ("فِيهِ شَهَادَةُ مُعَاوِيَةَ، وَهُوَ إِنَّمَا أَسْلَمَ عَامَ الْفَتْحِ،\n"
              "وَفَتْحُ خَيْبَرَ كَانَ فِي سَنَةِ سَبْعٍ")

# --- البدایہ والنہایہ، ابن کثیر رحمہ اللہ (ط دار ابن كثير) -------------------------------
AR_WAFAT = ("فمَنْ كانَ منكم يَعْبُدُ محمدًا فإِنَّ محمدًا قد مات،\n"
            "ومن كان يَعْبُدُ اللَّهَ فإنَّ اللَّه حيٌّ لا يموتُ.")
AR_MUZAMMAL = ("وإذا بينَ ظَهرانيهم رجلٌ مُزَمَّلٌ، فقلت: منْ هذا؟\n"
               "قالوا: سعدُ بن عُبادة. فقلت: ما له؟ قالوا: وجعٌ.")
AR_KHATIB = "فنحنُ أنصارُ اللَّه وكتيبةُ الإسلام، وأنتم يا مَعْشَرَ المُهاجرين رَهْطٌ منّا"
AR_UMAR_SELF = ("واللَّهِ ما تركَ من كَلمةٍ أعْجَبَتني في تَزْويري\n"
                "إِلَّا قالها في بديهته وأفضل حتى سكت.")
AR_SIDDIQ = ("وما تَعْرف العربُ هذا الأمر إِلَّا لهذا الحيِّ من قُرَيش،\n"
             "هم أوسط العرب نسبًا ودارًا")
AR_HUBAB = "أنا جُذَيْلُها المُحَكَّك وعُذَيْقُها المُرَجَّب، منا أمير، ومنكم أمير، يا معشر قريش"
AR_HAND_A = "فقلت: ابسُطْ يَدَكَ يا أبا بكرٍ. فبَسَط يَدَه، فبايَعْتُه وبايَعَه المُهاجِرون، ثم بايَعَه الأنْصارُ"
AR_HAND_B = "وبَدَرَني رجلٌ من الأنصار، فضربَ على يده قبلَ أن أضربَ على يده"
AR_BASHIR = "هو بَشير بن سَعْدٍ، والد النعمان بن بَشير."
AR_RULE = "فمن بايعَ أميرًا عن غير مَشورة المُسلمين فلا بيعةَ له"
AR_TWO_STAGE = ("وكانت طائفة قد بايَعوه قبل ذلك في سَقيفة بني ساعدة،\n"
                "وكانت بيعة العامة على المِنْبَرِ.")
AR_SAAD = "صدقتَ، نحن الوزراءُ وأنتم الأمراءُ."
AR_ALI = ("ما اسْتَخْلَفَ رسولُ اللَّه ﷺ فأَسْتَخْلِفَ، ولكن إن يُردِ اللَّهُ بالنّاسِ خيرًا\n"
          "فَسَيجْمَعُهم بعدي على خيرهم، كما جَمَعَهم بعدَ نبيِّهم على خيرهم.")
AR_JURF = "فخرجوا إلى الجُرف فخيَّموا به"
AR_KHUSHUB = "فلما نزل بذي خُشُب قُبضَ رسولُ الله ﷺ"

# --- سیر أعلام النبلاء، الذہبی رحمہ اللہ (ط الرسالة) ------------------------------------
AR_UMMAL = "مَا أَحَدٌ أَحَقُّ بِالعَمْلِ مِنْ عُمَّالِ رَسُوْلِ اللهِ ﷺ ارْجِعُوا إِلَى أَعْمَالِكُم."

# --- الکامل فی التاریخ، ابن الاثیر رحمہ اللہ --------------------------------------------
AR_SUHAYL = "دَعْهُ يَا عُمَرُ؛ فَسَيَقُومُ مَقَامًا تَحْمَدُهُ عَلَيْهِ"

VERIFY = [
    (TAR, AR_MAWDU), (TAR, AR_THAWRI), (TAR, AR_HAFS), (TAR, AR_SEVEN),
    (TAR, AR_FORGED), (TAR, AR_KHAYBAR),
    (WAF, AR_WAFAT),
    (BID, AR_MUZAMMAL), (BID, AR_KHATIB), (BID, AR_UMAR_SELF), (BID, AR_SIDDIQ),
    (BID, AR_HUBAB), (BID, AR_HAND_A), (BID, AR_HAND_B), (BID, AR_BASHIR),
    (BID, AR_RULE), (BID, AR_TWO_STAGE), (BID, AR_SAAD), (BID, AR_ALI),
    (GOV, AR_UMMAL), (GOV, AR_JURF), (GOV, AR_KHUSHUB),
    (SUH, AR_SUHAYL),
]


def verify():
    """Every Arabic string that reaches a slide must still be verbatim in its research note."""
    root = os.path.join(HERE, "..")
    bad = 0
    for path, s in VERIFY:
        with open(os.path.join(root, path), encoding="utf-8") as f:
            body = f.read()
        if s.replace("\n", " ") not in body:
            print("MISMATCH  %s\n          %s" % (path, s[:70]))
            bad += 1
    print("verified %d/%d Arabic strings against docs/research/" % (len(VERIFY) - bad, len(VERIFY)))
    return bad == 0


# ============================================================================ furniture

def picture_slide(prs, image, headline, sub=None, bottom=7.38):
    """Full-bleed picture under a headline band. Returns (slide, image rect in inches).

    Sizes by WIDTH for wide pictures and by HEIGHT for near-square ones, exactly as
    deckkit.map_slide does — but hands back the placed rectangle, so pins are computed through
    the same projection the PNG was drawn with instead of guessed at.
    """
    s = blank(prs, CREAM)
    p = os.path.join(VIS, "%s.png" % image)
    top, rect = 0.95, None
    if os.path.exists(p):
        avail_h = bottom - top
        try:
            from PIL import Image as _Im
            with _Im.open(p) as im:
                iw, ih = im.size
        except Exception:
            iw, ih = 16, 9
        if iw / float(ih) >= 13.333 / avail_h:
            w_in, x_in = 13.333, 0.0
            h_in = w_in * ih / float(iw)
        else:
            h_in = avail_h
            w_in = h_in * iw / float(ih)
            x_in = (13.333 - w_in) / 2.0
        s.shapes.add_picture(p, Inches(x_in), Inches(top), width=Inches(w_in))
        rect = (x_in, top, w_in, h_in)
    band(s, 0, Inches(0.95), DARK)
    text(s, headline, Inches(0.7), Inches(0.16), Inches(8.6), Inches(0.7),
         size=30, color=CREAM, font=EN)
    if sub:
        text(s, sub, Inches(9.4), Inches(0.28), Inches(3.3), Inches(0.5),
             size=15, color=GOLD, font=SANS, align=PP_ALIGN.RIGHT)
    return s, rect


def footer(slide, en, ur=None, y=6.24, h=1.26):
    """The dark strip under a picture. English left, Urdu right — separate boxes, never one line."""
    band(slide, Inches(y), Inches(h), DARK)
    text(slide, en, Inches(0.7), Inches(y + 0.18), Inches(7.6), Inches(h - 0.28),
         size=19, color=CREAM, font=EN, spacing=1.3, italic=True)
    if ur:
        text(slide, ur, Inches(8.6), Inches(y + 0.1), Inches(4.1), Inches(h - 0.18),
             size=23, color=GOLD, font=UR, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True, spacing=1.85)


def pin(slide, rect, view, place, label, side="above", colour=TEAL, nudge=(0.0, 0.0), size=12):
    """A dot and its label, placed through the same projection the base PNG used."""
    if rect is None:
        return
    x_in, y_in, w_in, h_in = rect
    px, py = view.px(*PLACES[place])
    cx = x_in + px / view.w * w_in
    cy = y_in + py / view.h * h_in
    r = 0.05
    d = slide.shapes.add_shape(9, Inches(cx - r), Inches(cy - r), Inches(2 * r), Inches(2 * r))
    d.fill.solid(); d.fill.fore_color.rgb = colour; d.line.fill.background()
    d.shadow.inherit = False
    bw = 1.9
    dx = {"above": -bw / 2, "below": -bw / 2, "right": 0.11, "left": -bw - 0.11}[side]
    dy = {"above": -0.30, "below": 0.09, "right": -0.11, "left": -0.11}[side]
    al = {"above": PP_ALIGN.CENTER, "below": PP_ALIGN.CENTER,
          "right": PP_ALIGN.LEFT, "left": PP_ALIGN.RIGHT}[side]
    text(slide, label, Inches(cx + dx + nudge[0]), Inches(cy + dy + nudge[1]),
         Inches(bw), Inches(0.28), size=size, color=colour, font=EN, bold=True, align=al)


def sourced(prs, arabic, english, work_en, ref_ur, label=None, speaker_ur=None):
    """A page-cited Arabic quotation: Naskh on top, ENGLISH beneath, the reference twice.

    The attribution carries the claim; the speaker never does. `work_en` is the Latin citation,
    `ref_ur` the same reference in Urdu script — separate boxes, so the scripts never meet.
    """
    s = quote_slide(prs, arabic, english, work_en, label=label)
    if speaker_ur:
        text(s, speaker_ur, Inches(7.4), Inches(0.36), Inches(5.2), Inches(0.62),
             size=23, color=TEAL, font=UR, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True, spacing=1.8)
    text(s, ref_ur, Inches(0.7), Inches(5.66), Inches(11.9), Inches(0.55),
         size=16, color=MUTED, font=UR, cs=UR, align=PP_ALIGN.CENTER, is_rtl=True, spacing=1.85)
    return s


def triple(slide, items, y=2.3, size=20, head=30):
    """Three side-by-side blocks. The structure IS the picture — this is not a bullet list."""
    for i, (head_txt, body, colour, head_col) in enumerate(items):
        cx = 0.85 + i * 3.95
        rule(slide, Inches(cx), Inches(y), Inches(1.4), GOLD, Pt(2.5))
        text(slide, head_txt, Inches(cx), Inches(y + 0.18), Inches(3.6), Inches(0.7),
             size=head, color=head_col, font=EN)
        text(slide, body, Inches(cx), Inches(y + 1.05), Inches(3.65), Inches(2.2),
             size=size, color=colour, font=EN, spacing=1.4)


# ============================================================================ the deck

def build(path):
    prs = deck()

    # ------------------------------------------------------------- 1 · title
    s = title_slide(prs, "Time, place, and one night", "وقت، جگہ، اور ایک رات",
                    "Where we are in time · where we are on the map · and then one courtyard",
                    "LESSONS FROM HISTORY  ·  SESSION 1 OF 10  ·  DHA ISLAMABAD")
    note(s, "0:00. Workbooks and pens are already on the chairs.\n"
            "FIRST INSTRUCTION OF THE COURSE: write your name on the workbook. A real 30 seconds.\n"
            "THEN THE POLICY, said once and applied all ten weeks (CLAUDE.md 1.5): no questions\n"
            "during the 45 minutes; slips into the box at the door; I stay 15 minutes afterwards.\n"
            "THEN THE SHIELD, do not skip and do not rush it: I am not a historian. We are reading\n"
            "a book - Tareekh-e-Ummat - and tonight also three Arabic works that book's own\n"
            "muqaddima names and relies on.")

    # ------------------------------------------------------------- 2 · آغاز
    s = blank(prs, DARK)
    eyebrow(s, "aghaz  ·  the destination, named first", GOLD)
    text(s, "Monday, 12 Rabiʻ al-Awwal, 11 AH.",
         Inches(0.9), Inches(1.3), Inches(11.5), Inches(0.75), size=32, color=GOLD, font=EN)
    text(s, "In a covered courtyard in Medina, a small number of men\nsettled who would lead the "
            "Muslims after the Prophet ﷺ.",
         Inches(0.9), Inches(2.15), Inches(11.5), Inches(1.7),
         size=39, color=CREAM, font=EN, spacing=1.3)
    rule(s, Inches(0.9), Inches(4.1), Inches(2.6))
    text(s, "We have all heard the name.\nAlmost none of us could name three men who were there.",
         Inches(0.9), Inches(4.4), Inches(11.5), Inches(1.3),
         size=25, color=CREAM, font=EN, italic=True, spacing=1.35)
    text(s, "سقیفہ بنی ساعدہ", Inches(8.3), Inches(5.85), Inches(4.4), Inches(0.9),
         size=32, color=GOLD, font=UR, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True, spacing=1.9)
    text(s, "Saqifat Bani Saʿida", Inches(0.9), Inches(6.05), Inches(6.0), Inches(0.45),
         size=17, color=GOLD, font=SANS)
    note(s, "0:00 AGHAZ (2 min). Naming the destination FIRST is what turns the next twenty-four\n"
            "minutes from throat-clearing into build-up (spec 4, 0:00).\n"
            "Then: 'tonight we fix that. But not yet - first we have to know WHEN we are, and\n"
            "WHERE.' Say it and move. Do not begin the story here.\n"
            "SOURCE for the date: al-Bidaya j.5 p.343 and j.7 p.5 - Monday, 12 Rabi' al-Awwal,\n"
            "'ala al-mashhur. Say 'the well-known view', never 'the date'.")

    # ------------------------------------------------------------- 3 · what tarikh is
    s = blank(prs, CREAM)
    eyebrow(s, "tarikh kya hai  ·  what history is, and is not")
    text(s, "Events appear in many books.\nOnly one kind of book keeps them in order.",
         Inches(0.85), Inches(0.92), Inches(11.6), Inches(1.4),
         size=35, color=TEAL, font=EN, spacing=1.25)
    band(s, Inches(2.28), Inches(0.045), GOLD, Inches(0.85), Inches(11.6))
    triple(s, [
        ("Adab", "Collects the event so the reader\ntakes a lesson from it.\n"
                 "Not ordered by time.", MUTED, TEAL),
        ("Hadith", "Collects it for rulings, for the\nstanding of the chain, for the\nnames of "
                   "the narrators.\nOften no month, no year.", MUTED, TEAL),
        ("Tarikh", "Collects it so the sequence itself\nsurvives. Earlier before later,\n"
                   "year by year, month by month.", DARK, MAROON),
    ], y=2.58, size=19, head=29)
    text(s, "So its question is not “what happened” — every discipline asks that. Its question "
            "is WHEN, and IN WHAT ORDER.",
         Inches(0.85), Inches(5.9), Inches(11.6), Inches(0.6),
         size=21, color=MAROON, font=EN, italic=True)
    text(s, "کب، اور کس ترتیب سے؟", Inches(8.0), Inches(6.42), Inches(4.6), Inches(0.8),
         size=27, color=DARK, font=UR, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True, spacing=1.9)
    text(s, "TAREEKH-E-UMMAT  ·  MUQADDIMA  ·  PRINTED p. 33",
         Inches(0.85), Inches(6.6), Inches(6.6), Inches(0.4), size=13, color=TEAL, font=SANS)
    note(s, "0:02 TAREEKH KYA HAI (4 min), move 1 of 3. Ninety seconds, no more - this is NOT a\n"
            "methodology lecture (DECISIONS.md #9).\n"
            "SOURCE: the muqaddima makes exactly this three-way contrast itself at printed p.33\n"
            "(research note tarikh-definition-and-the-guardrail.md 4.1). al-Sakhawi says the same\n"
            "thing when he separates tarikh from tabaqat, al-I'lan pp.177-178.\n"
            "Do NOT quote the Urdu book's compressed Arabic definition - it is not what\n"
            "al-Sakhawi's printed text says (note 2.2). The next slide has his own words.")

    # ------------------------------------------------------------- 4 · موضوعه
    s = sourced(prs, AR_MAWDU,
                "“As for the subject-matter of history: man, and time.”",
                "AL-IʿLAN BI'L-TAWBIKH  ·  AL-SAKHAWI  ·  PRINTED p. 93",
                "الإعلان بالتوبيخ — السخاوی رحمہ اللہ — ص ۹۳",
                label="two words, and the whole discipline is in them",
                speaker_ur="علامہ سخاوی رحمہ اللہ")
    note(s, "0:02 block, still move 1. Read it once. Say the two words in Urdu - insaan aur\n"
            "zamaana - and let that be the definition they carry home.\n"
            "SOURCE: al-I'lan bi'l-Tawbikh, printed p.93, bab mawdu' al-tarikh wa fa'idatuh. The\n"
            "Urdu muqaddima prints the same line at p.33, so this is inside the course's own frame.\n"
            "The same page gives the benefit of the discipline: 'ma'rifat al-umur 'ala wajhiha' -\n"
            "knowing matters as they actually were. Worth saying; not worth a second slide.\n"
            "IF THE BLOCK IS RUNNING LONG this slide goes second, after the Hafs slide.")

    # ------------------------------------------------------------- 5 · Sufyan al-Thawri
    s = sourced(prs, AR_THAWRI,
                "“When the transmitters started using lies against us,\nwe used chronology "
                "against them.”",
                "AL-IʿLAN BI'L-TAWBIKH  ·  PRINTED p. 97   (also muqaddima p. 57)",
                "سفیان ثوری رحمہ اللہ — الإعلان بالتوبيخ ص ۹۷",
                label="why the order is a weapon", speaker_ur="سفیان ثوری رحمہ اللہ")
    note(s, "0:02 block, move 2 of 3. THE ANCHOR QUOTATION OF THE WHOLE COURSE.\n"
            "Read the Arabic once slowly, then the English once, then STOP. Do not explain it -\n"
            "the two slides after this ARE the explanation.\n"
            "SOURCE: al-I'lan printed p.97; the edition's takhrij is al-Khatib, al-Kifaya p.193.\n"
            "WORDING: al-Sakhawi prints 'ista'malna LAHUM al-tarikh'. The Urdu book prints\n"
            "'ista'malnaHUM al-tarikh'. We set al-Sakhawi's, because we hold his printed page\n"
            "(research note 3.3a). If anyone has the Urdu book open and notices, say exactly that.")

    # ------------------------------------------------------------- 6 · Hafs, and the method
    s = blank(prs, CREAM)
    eyebrow(s, "and here is how you actually do it")
    text(s, AR_HAFS, Inches(0.8), Inches(1.05), Inches(11.7), Inches(1.0),
         size=36, color=DARK, font=AR, cs=AR, align=PP_ALIGN.CENTER, is_rtl=True, spacing=1.4)
    text(s, "“When you suspect the shaykh, reckon him by the two ages.”",
         Inches(1.2), Inches(2.15), Inches(10.9), Inches(0.6),
         size=24, color=INK, font=EN, align=PP_ALIGN.CENTER, italic=True)
    text(s, "al-Sakhawi vowels the word and explains it himself, on the same page:\n"
            "compute his age, and the age of the man he claims to have written from.",
         Inches(1.2), Inches(2.85), Inches(10.9), Inches(0.9),
         size=19, color=MAROON, font=EN, align=PP_ALIGN.CENTER, spacing=1.3)
    band(s, Inches(3.98), Inches(1.72), DARK, Inches(0.85), Inches(11.6))
    text(s, AR_SEVEN, Inches(1.15), Inches(4.18), Inches(11.0), Inches(0.6),
         size=27, color=GOLD, font=AR, cs=AR, align=PP_ALIGN.CENTER, is_rtl=True, spacing=1.4)
    text(s, "“In what year did you write from Khalid b. Maʿdan?”  —  “The year 113.”\n"
            "“Then you are claiming you heard from him seven years after he died.”",
         Inches(1.15), Inches(4.85), Inches(11.0), Inches(0.85),
         size=19, color=CREAM, font=EN, align=PP_ALIGN.CENTER, spacing=1.3)
    text(s, "حفص بن غیاث القاضی رحمہ اللہ — الإعلان بالتوبيخ ص ۹۷",
         Inches(0.85), Inches(6.0), Inches(11.6), Inches(0.55),
         size=17, color=MUTED, font=UR, cs=UR, align=PP_ALIGN.CENTER, is_rtl=True, spacing=1.85)
    text(s, "AL-IʿLAN BI'L-TAWBIKH  ·  PRINTED p. 97  (the saying)  ·  p. 97 (Ismaʿil b. ʿAyyash)",
         Inches(0.85), Inches(6.58), Inches(11.6), Inches(0.4),
         size=13, color=TEAL, font=SANS, align=PP_ALIGN.CENTER)
    note(s, "0:02 block, move 2 continued. Sixty seconds, and the arithmetic is the point - let\n"
            "them do the subtraction in their own heads. 113 minus 106 is seven.\n"
            "SOURCE: al-I'lan printed p.97, both items (research note 3.3b and 3.4i). Isma'il b.\n"
            "'Ayyash was testing the man; al-Jadi' grades the chain jayyid.\n"
            "THE CORRECTION WORTH KNOWING: the Urdu book prints 'bi'l-sinin' and renders it loosely\n"
            "as 'check him by history'. al-Sakhawi's printed text has AL-SHAYKH in it and reads\n"
            "BI'L-SINNAYN - the DUAL of sinn, meaning age. Two ages, not the years. He vowels it\n"
            "himself on the page precisely so it is not misread.\n"
            "THE THIRD SAYING at the same page - 'nothing has helped against the liars like\n"
            "chronology' - is deliberately NOT here: the printed edition attributes it to Hassan\n"
            "b. Zayd, the Urdu book to Hammad b. Zayd, and we do not print a disputed attribution\n"
            "as if it were settled (note 3.3c). Say it without a name if you want it.")

    # ------------------------------------------------------------- 7 · the forged document
    s = blank(prs, CREAM)
    eyebrow(s, "and then it stopped a forgery in a court")
    text(s, "Baghdad, the year 447.", Inches(0.85), Inches(0.9), Inches(11.6), Inches(0.7),
         size=34, color=TEAL, font=EN)
    band(s, Inches(1.72), Inches(1.62), DARK, Inches(0.85), Inches(5.45))
    text(s, "A document is produced. It claims the\nProphet ﷺ remitted the jizya from the\n"
            "people of Khaybar. It carries the\nattestations of Companions.",
         Inches(1.15), Inches(1.9), Inches(4.9), Inches(1.35),
         size=18, color=CREAM, font=EN, spacing=1.32)
    text(s, "It reached the vizier. He laid it before the hafiz,\nAbu Bakr al-Khatib al-Baghdadi.",
         Inches(0.85), Inches(3.55), Inches(5.4), Inches(0.9),
         size=18, color=MUTED, font=EN, italic=True, spacing=1.3)
    text(s, AR_FORGED, Inches(0.85), Inches(4.6), Inches(5.4), Inches(0.8),
         size=40, color=MAROON, font=AR, cs=AR, align=PP_ALIGN.CENTER, is_rtl=True, spacing=1.3)
    text(s, "“This is a forgery.”", Inches(0.85), Inches(5.5), Inches(5.4), Inches(0.5),
         size=22, color=MAROON, font=EN, align=PP_ALIGN.CENTER, italic=True)
    text(s, AR_KHAYBAR, Inches(6.6), Inches(1.8), Inches(5.95), Inches(1.3),
         size=25, color=DARK, font=AR, cs=AR, align=PP_ALIGN.RIGHT, is_rtl=True, spacing=1.4)
    for i, line in enumerate([
            "One attestation is Muʿawiya's — and he accepted Islam in the Year of the Conquest, "
            "while Khaybar was taken in year 7.",
            "Another is Saʿd b. Muʿadh's — and he had already died, two years before Khaybar."]):
        y = 3.35 + i * 1.32
        rule(s, Inches(6.6), Inches(y), Inches(0.75), GOLD, Pt(2.5))
        text(s, line, Inches(6.6), Inches(y + 0.16), Inches(5.95), Inches(1.1),
             size=18, color=DARK, font=EN, spacing=1.3)
    text(s, "الخطیب البغدادی رحمہ اللہ — الإعلان بالتوبيخ ص ۱۰۱",
         Inches(6.6), Inches(6.02), Inches(5.95), Inches(0.5),
         size=16, color=MUTED, font=UR, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True, spacing=1.85)
    text(s, "No chain of narrators was examined. The calendar alone did it. That is why this "
            "course is built on a timeline —\nand why the next eleven minutes are three of them.",
         Inches(0.85), Inches(6.45), Inches(11.6), Inches(0.9),
         size=19, color=MAROON, font=EN, italic=True, spacing=1.3)
    note(s, "0:02 block, end of move 2 (90 sec). THE DEMONSTRATION. Tell it as a story, not as an\n"
            "argument. THE CLEANEST PROOF THAT CHRONOLOGY IS A TOOL, NOT BOOKKEEPING: it stopped a\n"
            "forged instrument from being enforced by a state.\n"
            "SOURCE: al-I'lan bi'l-Tawbikh printed p.101, and the principle stated one page earlier\n"
            "at p.100 - forgery is detected when a party to a document 'died before the date of the\n"
            "document'. The Urdu muqaddima carries the same story at p.58.\n"
            "TWO ACCOUNTS, ONE DIVERGENCE, DO NOT MERGE THEM (research note 6.3): al-Sakhawi says\n"
            "Sa'd b. Mu'adh (RA) died on the day of Banu Qurayza, two years before Khaybar; the\n"
            "Urdu book says he was martyred at al-Khandaq. Both are true of the same man and the\n"
            "slide says only what both agree on - he had already died, before Khaybar.\n"
            "Honorifics on the two Companions are spoken, not printed after Latin letters.")

    # ------------------------------------------------------------- 8 · three disciplines
    s = blank(prs, CREAM)
    eyebrow(s, "before we go any further")
    text(s, "Three disciplines. One report. Three different jobs.",
         Inches(0.85), Inches(0.95), Inches(11.6), Inches(0.8), size=35, color=TEAL, font=EN)
    band(s, Inches(1.92), Inches(0.045), GOLD, Inches(0.85), Inches(11.6))
    for i, (en_head, ur_head, body, colour) in enumerate([
            ("Hadith", "حدیث", "A report must be authentic\nbefore it can bind.\n"
                                "It carries the deen.", DARK),
            ("Fiqh", "فقہ", "A report is weighed for\nwhat it obliges.\n"
                             "It carries a ruling.", DARK),
            ("Tarikh", "تاریخ", "A report is recorded to fix\nwhat happened,\n"
                                 "and in what order.", MAROON)]):
        cx = 0.85 + i * 3.95
        text(s, en_head, Inches(cx), Inches(2.25), Inches(3.6), Inches(0.7),
             size=32, color=TEAL, font=EN)
        text(s, ur_head, Inches(cx), Inches(3.0), Inches(3.6), Inches(0.75),
             size=28, color=GOLD, font=UR, cs=UR, align=PP_ALIGN.LEFT, is_rtl=True, spacing=1.9)
        text(s, body, Inches(cx), Inches(3.95), Inches(3.65), Inches(1.7),
             size=20, color=colour, font=EN, spacing=1.35)
    text(s, "So a report can be perfectly well recorded as history and still be no ruling at all.",
         Inches(0.85), Inches(5.85), Inches(11.6), Inches(0.6),
         size=21, color=MAROON, font=EN, italic=True)
    text(s, "TAREEKH-E-UMMAT  ·  MUQADDIMA  ·  PRINTED pp. 33, 66",
         Inches(0.85), Inches(6.55), Inches(7.0), Inches(0.4), size=13, color=TEAL, font=SANS)
    note(s, "0:02 block, move 3 of 3 - THE GUARDRAIL, part one. NEVER CUT THIS BLOCK (spec 3).\n"
            "Sixty seconds, said calmly, once. Do not argue for it; state it and move.\n"
            "SOURCE: muqaddima p.33 and, for the difference in shara'it, p.66 - 'riwayat-e-tarikh\n"
            "aur riwayat-e-hadith mein farq'. In riwayat-e-hadith the sanad is weighed very\n"
            "heavily; in riwayat-e-tarikh it is obligatory only on specific occasions - and the\n"
            "FIRST of those occasions is a report touching the Prophet (peace be upon him) or the\n"
            "Companions (RA). Which is exactly tonight. Say that: the strictest setting is on.")

    # ------------------------------------------------------------- 9 · THE GUARDRAIL
    s = blank(prs, DARK)
    eyebrow(s, "the one sentence that keeps us safe for nine weeks", GOLD)
    text(s, "A tarikh report is not a ruling,\nand it is not a creed.",
         Inches(0.9), Inches(1.3), Inches(11.5), Inches(2.0),
         size=49, color=CREAM, font=EN, spacing=1.25)
    rule(s, Inches(0.9), Inches(3.45), Inches(2.6))
    text(s, "Islamic history is the history of Muslims — not of Islam.\nWe narrate what the books "
            "narrate, and we do not judge between the Companions.",
         Inches(0.9), Inches(3.78), Inches(11.5), Inches(1.3),
         size=23, color=GOLD, font=EN, italic=True, spacing=1.35)
    text(s, "یہ مسلمانوں کی تاریخ ہے، دین کا ماخذ نہیں۔\n"
            "ہم وہی بیان کرتے ہیں جو کتاب بیان کرتی ہے — اور صحابہ ؓ کے درمیان فیصلہ نہیں کرتے۔",
         Inches(1.3), Inches(5.15), Inches(11.1), Inches(1.7),
         size=26, color=CREAM, font=UR, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True, spacing=2.0)
    text(s, "MUQADDIMA  ·  PRINTED p. 61", Inches(0.9), Inches(6.92), Inches(6.0), Inches(0.4),
         size=12, color=GOLD, font=SANS)
    note(s, "0:02 block - THE GUARDRAIL, part two. THE MOST IMPORTANT SLIDE IN THE DECK.\n"
            "Read the Urdu aloud exactly as printed. It is word for word QA_BANK.md 0.1, so the\n"
            "version they hear tonight is the version they get again at the door.\n"
            "SOURCE: muqaddima printed p.61, which gives it a heading of its own - 'tareekh-e-Islam\n"
            "ya tareekh-e-Muslimeen'. The book's own conclusion, in its own words: the common books\n"
            "of Islamic history - Tabari, al-Bidaya, al-Kamil - should be read as the history of a\n"
            "PEOPLE, not the history of a religion. So a Muslim behaving badly in 250 AH is not\n"
            "evidence about Islam. Say that sentence; it is the whole payload.\n"
            "THEN STOP. Do not soften it, do not expand it, do not take a question on it.\n"
            "The fiqh of the mushajarat - makruh without need, haram if 'aqida is at risk, ja'iz\n"
            "and at need wajib in defence of the Companions (RA) - is muqaddima pp.52-53 and it is\n"
            "installed properly in SESSION 3, not tonight. If pushed, QA_BANK 0.2 verbatim.")

    # ------------------------------------------------------------- 10-12 · the timelines
    s, _ = picture_slide(prs, "l01_tl1_pakistan", "Seventy-nine years",
                         "timeline 1 of 3  ·  Pakistan", bottom=6.24)
    footer(s, "You remember some of this. Your parents remember all of it. Hold that length in "
              "your head — we are about to shrink it twice.")
    note(s, "0:06 TIMELINE 1 (3 min). Name the pegs; do NOT discuss them - no present-day politics,\n"
            "the venue has ruled it out (CLAUDE.md 1.5).\n"
            "Worksheet A is these same three panels on one A3 sheet; hand it out here.\n"
            "CUT ORDER: this is the FIRST thing to cut - down to 90 seconds, names only (spec 3).")

    s, _ = picture_slide(prs, "l01_tl2_ummah", "Fourteen centuries",
                         "timeline 2 of 3  ·  the Ummah", bottom=6.24)
    footer(s, "The whole of the last slide is the gold sliver at the right-hand edge. "
              "Everything this course covers is on this one line.")
    note(s, "0:09 TIMELINE 2 (5 min). THE LOAD-BEARING GRAPHIC OF THE FIRST HALF.\n"
            "Point at the gold column FIRST: 'that is the entire last slide'. Let it land before\n"
            "you say anything else.\n"
            "Then walk the pegs left to right and name the SESSION each one belongs to. Do not tell\n"
            "the stories. This is the only place tonight the room sees the whole arc, and it is why\n"
            "a one-off attendee still leaves with the shape of the course (DECISIONS.md #13).")

    s, _ = picture_slide(prs, "l01_tl3_prophets", "And before that",
                         "timeline 3 of 3  ·  the prophets", bottom=6.24)
    footer(s, "Hollow markers are estimates from general scholarship. Our sources do not fix "
              "them — so we do not print them as if they did.",
           "ترتیب معلوم ہے، تاریخیں نہیں")
    note(s, "0:14 TIMELINE 3 (3 min). CAREFUL AND HONEST - and the honesty IS the teaching point.\n"
            "Say the caption in both languages; the Urdu is on the slide: the order is known, the\n"
            "dates are not.\n"
            "Our sources do NOT fix dates for Adam, Nuh, Ibrahim, Musa or Dawud (alayhim al-salam).\n"
            "Adam and Nuh (alayhima al-salam) are OFF THE SCALE with no number invented at all; the\n"
            "hollow dashed markers are conventional estimates and are labelled 'approx.' on the\n"
            "image itself. DECISIONS.md #16, QA_BANK 2.1.\n"
            "'Tarteeb wahy se maloom hai. Tareekhein maloom nahin - aur jo maloom na ho, usay hum\n"
            "maloom nahin kehte.' This is the strongest credibility moment of the evening. Use it,\n"
            "then say 'that is the method of the whole course' and go to the maps.")

    # ------------------------------------------------------------- 13 · the world
    s, rect = picture_slide(prs, "map_blank", "The edge of the world, not its centre",
                            "map 1 of 3  ·  c. 11 AH / 632 CE", bottom=7.38)
    text(s, "ROMAN  ·  BYZANTINE", Inches(5.5), Inches(2.6), Inches(2.7), Inches(0.35),
         size=15, color=MAROON, font=SANS, bold=True, align=PP_ALIGN.CENTER)
    text(s, "SASANID PERSIA", Inches(8.5), Inches(3.55), Inches(2.5), Inches(0.35),
         size=15, color=MAROON, font=SANS, bold=True, align=PP_ALIGN.CENTER)
    text(s, "ARABIA", Inches(7.6), Inches(5.6), Inches(1.8), Inches(0.35),
         size=17, color=DARK, font=SANS, bold=True, align=PP_ALIGN.CENTER)
    text(s, "No borders are drawn — direction only.  The six cities marked are the anchor cities "
            "for all ten weeks.",
         Inches(0.5), Inches(6.98), Inches(12.3), Inches(0.4),
         size=15, color=MUTED, font=EN, italic=True)
    note(s, "0:17 MAP 1 (4 min). THE POINT: this was the edge of the known world, not its centre.\n"
            "Rome to the north-west, Persia to the north-east, Arabia between them - and all three\n"
            "are IN THE BOOK as facts on the ground, not as background colour:\n"
            "  * the state's northern frontier is Tabuk / Ayla, and beyond it Roman territory -\n"
            "    al-Bidaya j.4 p.670: Ayla, Jarba and Adhruh gave the jizya and hold the Prophet's\n"
            "    (peace be upon him) written aman;\n"
            "  * in Yemen the governor was Shahr b. Badhaam, son of Badhaam, the last PERSIAN\n"
            "    'amil, whose Islam the Prophet (peace be upon him) accepted - j.7 pp.13-14;\n"
            "  * Jaysh Usama (RA) was pointed at the marches of al-Balqa' in al-Sham - j.7 p.9.\n"
            "Say those three and the two empires stop being decoration.\n"
            "Then introduce the six anchor cities: furniture for all ten weeks.\n"
            "TO DO before delivery: a proper empires overlay would beat these three labels -\n"
            "see MAPS.md and tools/mapstudio.")

    # ------------------------------------------------------------- 14 · Arabia
    s, rect = picture_slide(prs, "map_arabia_blank", "Arabia itself",
                            "map 2 of 3  ·  the settlements", bottom=7.38)
    for place, lab, side, nud in [("taif", "al-Ta'if", "right", (0.06, 0.02)),
                                  ("yamama", "al-Yamama", "above", (0.0, 0.0)),
                                  ("bahrain", "al-Bahrayn", "above", (0.0, -0.02)),
                                  ("daba", "Uman", "above", (0.0, 0.0)),
                                  ("hadramawt", "Hadramawt", "below", (0.0, 0.0)),
                                  ("najran", "Najran", "left", (0.0, 0.0)),
                                  ("sanaa", "San'a", "below", (0.0, 0.0)),
                                  ("tabuk", "Tabuk", "left", (0.0, 0.0))]:
        pin(s, rect, ARABIA, place, lab, side, TEAL, nud)
    text(s, "Nine places.\nThey carry the next\ntwo sessions between\nthem.",
         Inches(0.42), Inches(1.35), Inches(2.65), Inches(1.9),
         size=20, color=TEAL, font=EN, spacing=1.35)
    text(s, "Makkah and Madina are\nalready marked. The rest\ngo on your sheet, by hand.",
         Inches(0.42), Inches(3.45), Inches(2.65), Inches(1.6),
         size=17, color=MUTED, font=EN, italic=True, spacing=1.35)
    text(s, "Tabuk and Ayla are\nwhere the state's writ\nstops and Roman\nterritory begins.",
         Inches(10.5), Inches(1.35), Inches(2.5), Inches(1.9),
         size=18, color=MAROON, font=EN, spacing=1.35)
    text(s, "AL-BIDAYA WA'L-NIHAYA\nVOL 4, PRINTED p. 670",
         Inches(10.5), Inches(3.4), Inches(2.5), Inches(0.8),
         size=11, color=TEAL, font=SANS, spacing=1.3)
    note(s, "0:21 MAP 2 (3 min). Names only. Do not tell any of their stories tonight - most of\n"
            "them are next week's material.\n"
            "SOURCE for the frontier: al-Bidaya j.4 p.670. Pin positions are PLACEMENT ONLY and are\n"
            "never a claim about a site (MAPS.md).\n"
            "Tribal blocs: docs/research/arabian-tribes-and-the-ridda-setup.md when it lands.\n"
            "CUT ORDER: SECOND thing to cut - merge into map 1 and simply point (spec 3).\n"
            "Then hand off: 'now one town on this map, properly' - and go to Medina.")

    # ------------------------------------------------------------- 15-16 · the clan chart
    s, _ = picture_slide(prs, "l01_clanchart", "Two peoples — and neither was one bloc",
                         "map 3 of 3  ·  madina ki sakht", bottom=6.24)
    footer(s, "The Ansar are of al-Azd — Qahtan, southern. Quraysh are ʿAdnan, northern. "
              "An old fault line, and it was in that courtyard.",
           "مدینہ کی ساخت")
    note(s, "0:24 THE CLAN CHART (6 min). THE LOAD-BEARING BLOCK. NEVER CUT IT (spec 3).\n"
            "THE CHART IS SHOWN, NOT READ ALOUD. Eight sub-clans narrated will lose the room.\n"
            "Say only these three things and nothing else:\n"
            "  1. yawm Bu'ath - al-Aws and al-Khazraj had been at war shortly before the Hijra.\n"
            "     THAT is why 'who leads' was a live question in that courtyard and not an\n"
            "     abstract one. Thirty seconds.\n"
            "  2. 'Adnan / Qahtan - the Ansar southern, Quraysh northern. Thirty seconds.\n"
            "  3. Name FOUR MEN out loud, each with his clan, and no more (spec 4):\n"
            "       Abu Bakr al-Siddiq (RA)      - Banu Taym, Quraysh\n"
            "       'Umar al-Faruq (RA)          - Banu 'Adi, Quraysh\n"
            "       Sa'd b. 'Ubada (RA)          - Banu Sa'ida, al-Khazraj. The courtyard was his\n"
            "                                      clan's - that is why it is called that.\n"
            "       al-Hubab b. al-Mundhir (RA)  - al-Khazraj\n"
            "     Every one of them speaks, or is spoken about, in the next eight minutes.\n"
            "AN EMPTY CHIEF BOX ON THE CHART IS HONEST - it means the research note could not cite\n"
            "a page. Say so if anyone asks. Quraysh lines: al-Bidaya j.2 pp.485, 493.")

    s, _ = picture_slide(prs, "l01_clanchart_blank", "Your sheet",
                         "worksheet C  ·  fill in the chiefs", bottom=6.24)
    footer(s, "Write the chiefs in. If we only get one done in the room, that is the plan — "
              "the sheet goes home with you, and so does the rest.")
    note(s, "0:24 block, last 90 seconds. THE HAND-WRITING RITUAL - this replaces the ta'aruf\n"
            "panels, for session 1 only (DECISIONS.md #15).\n"
            "Give them ONE name to write in the room and say plainly that the rest goes home (#17).\n"
            "Then: 'now - that courtyard.' From here on, every name belongs somewhere on that\n"
            "chart, and you keep pointing back at it.")

    # ------------------------------------------------------------- 17 · the order of the day
    s = blank(prs, CREAM)
    eyebrow(s, "saqifat bani saʿida  ·  the order of the day")
    text(s, "All of it happened between Monday morning\nand the night of Wednesday.",
         Inches(0.85), Inches(0.88), Inches(11.6), Inches(1.4),
         size=32, color=TEAL, font=EN, spacing=1.25)
    band(s, Inches(2.32), Inches(0.045), GOLD, Inches(0.85), Inches(11.6))
    steps = [
        ("MONDAY, FAJR", "Abu Bakr leads the prayer. The Prophet ﷺ lifts the curtain of the "
         "hujra, sees the rows behind him, and smiles. It was the last sight of him.",
         "j.5 p.343"),
        ("MONDAY, MID-MORNING", "The Prophet ﷺ passes away. Abu Bakr is out at al-Sunh, east "
         "of Medina, and is fetched back.", "j.5 p.343"),
        ("MONDAY, AFTER THAT", "He confirms it, and speaks beside the minbar. A group of the "
         "Companions give bayʿah there and then, in the mosque.", "j.5 p.343"),
        ("REST OF MONDAY", "The Ansar gather at the saqifa of Banu Saʿida. Three of the "
         "Muhajirun walk over, uninvited. This is our next eight minutes.",
         "j.5 p.348  ·  j.7 p.5"),
        ("TUESDAY MORNING", "The general bayʿah, in the mosque, from the minbar — the whole "
         "of the Muhajirun and the Ansar.", "j.5 p.349  ·  j.7 p.5"),
        ("NIGHT OF WEDNESDAY", "The burial. Ibn Kathir states plainly that everything above "
         "came before it.", "j.7 p.5  ·  j.5 p.348"),
    ]
    for i, (when, what, cite) in enumerate(steps):
        cx = 0.85 + (i % 3) * 3.95
        cy = 2.62 + (i // 3) * 2.16
        rule(s, Inches(cx), Inches(cy), Inches(0.65), GOLD, Pt(2.5))
        text(s, when, Inches(cx), Inches(cy + 0.13), Inches(3.7), Inches(0.3),
             size=12, color=MAROON, font=SANS, bold=True)
        text(s, what, Inches(cx), Inches(cy + 0.48), Inches(3.7), Inches(1.3),
             size=16, color=INK, font=EN, spacing=1.28)
        text(s, cite, Inches(cx), Inches(cy + 1.78), Inches(3.7), Inches(0.28),
             size=11, color=TEAL, font=SANS)
    text(s, "البدایہ والنہایہ — ابن کثیر رحمہ اللہ",
         Inches(7.9), Inches(6.9), Inches(4.7), Inches(0.5),
         size=15, color=MUTED, font=UR, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True, spacing=1.8)
    note(s, "0:30 SAQIFA (8 min) begins. Two minutes here; this table is the spine of the block.\n"
            "SOURCE: al-Bidaya j.5 pp.343-348 and j.7 p.5 (research note 1.1 and 5).\n"
            "SAY 'those present', or 'shurakaa' - NEVER actors, cast or characters (CLAUDE.md 1.2).\n"
            "Two facts they must carry away from this slide:\n"
            "  * a group had ALREADY given bay'ah in the mosque before anyone went to the saqifa;\n"
            "  * the whole bay'ah, both stages, was BEFORE THE BURIAL - Ibn Kathir says so in\n"
            "    those words at j.5 p.348.\n"
            "Honorifics are spoken on every name every time; they are not printed after Latin\n"
            "letters, which is why this table carries none.")

    # ------------------------------------------------------------- 18 · the khutba
    s = sourced(prs, AR_WAFAT,
                "“Whoever among you used to worship Muhammad — Muhammad has died. "
                "And whoever used to worship Allah — Allah is Living, and does not die.”",
                "AL-BIDAYA WA'L-NIHAYA  ·  VOL 5, PRINTED p. 341",
                "البدایہ والنہایہ — ج۵ ص۳۴۱",
                label="monday, beside the minbar", speaker_ur="سیدنا ابوبکر صدیق ؓ")
    note(s, "0:30 block. Say this quietly. Do not raise your voice; the words do not need help.\n"
            "SOURCE: al-Bidaya j.5 p.341, al-Zuhri from Abu Salama from Ibn 'Abbas (RA) - the\n"
            "Bukhari chain, 4452-4454. He then recited Al 'Imran 144, and Ibn 'Abbas (RA) said it\n"
            "was as though the people had never known the verse until that day.\n"
            "WORDING: keep 'amma ba'd, fa-' at the front and 'minkum' after 'kana'. Both are in\n"
            "the printed edition; the version circulating without them is NOT what Ibn Kathir\n"
            "prints (research note 3.3). Use this wording or none.\n"
            "A SECOND VERSION at j.5 p.340, from 'A'isha (RA), reverses the two clauses and puts\n"
            "al-Zumar 30 first. Do not blend the two - cite one page.")

    # ------------------------------------------------------------- 19 · what they found
    s = sourced(prs, AR_MUZAMMAL,
                "“And there among them was a man wrapped up. I said: who is this? They said: "
                "Saʿd b. ʿUbada. I said: what is wrong with him? They said: he is ill.”",
                "AL-BIDAYA WA'L-NIHAYA  ·  VOL 5, PRINTED p. 345",
                "البدایہ والنہایہ — ج۵ ص۳۴۵",
                label="what they found when they got there",
                speaker_ur="سیدنا عمر فاروق ؓ")
    note(s, "0:30 block. THIS IS 'UMAR (RA) DESCRIBING THE ROOM HIMSELF. The whole account is his\n"
            "own khutba, delivered at Medina in the last year of his caliphate; Ibn Kathir's\n"
            "footnote grades the isnad sahih and notes that the Jama'a all record it (note 1.2).\n"
            "Getting there: 'Umar (RA) proposed going over; two righteous men met them on the road\n"
            "and advised them not to; he insisted - 'wallahi la na'tiyannahum' (j.5 p.345). The two\n"
            "are named on the next page, j.5 p.346: 'Uwaym b. Sa'ida (RA) and Ma'n b. 'Adi (RA).\n"
            "SAY THIS OUT LOUD - QA_BANK 1.9, and it is a STRENGTH, not an embarrassment: the long\n"
            "speech everyone has heard from Sa'd b. 'Ubada (RA) is in Ibn Hisham and Tabari, which\n"
            "are OUTSIDE this course's safe list. In al-Bidaya he is present, ill and wrapped up,\n"
            "and is given no speech that day. I read you what is in this book.\n"
            "ALSO NOT THERE: Usayd b. Hudayr (RA) and Thabit b. Qays (RA) are not mentioned at the\n"
            "saqifa at all in j.5 pp.343-357 or j.7 pp.5-8. They stay on the clan chart as chiefs.\n"
            "DO NOT PLACE THEM IN THAT COURTYARD (research note 7).")

    # ------------------------------------------------------------- 20 · the Ansar open
    s = sourced(prs, AR_KHATIB,
                "“We are the helpers of Allah and the battalion of Islam; and you, O company "
                "of Muhajirun, are a group from among us.”",
                "AL-BIDAYA WA'L-NIHAYA  ·  VOL 5, PRINTED p. 345",
                "البدایہ والنہایہ — ج۵ ص۳۴۵",
                label="the ansar speak first", speaker_ur="خطیبِ انصار — نام مذکور نہیں")
    note(s, "0:30 block. HIS NAME IS NOT GIVEN in this narration, and not in the second one at\n"
            "j.5 p.350 either. Say so - it costs nothing and it is true (research note 7).\n"
            "The quotation is trimmed to its opening clause. What follows on the page is a\n"
            "complaint that some of the Muhajirun mean to cut the Ansar out of the matter, and\n"
            "Ibn Kathir's own footnotes gloss the two rare words in it. You do not need the rest.\n"
            "POINT BACK AT THE CLAN CHART. This is a claim being made by a people who had hosted\n"
            "the Hijra, and it is intelligible only if the room knows who the Ansar were.")

    # ------------------------------------------------------------- 21 · Umar against himself
    s = blank(prs, CREAM)
    eyebrow(s, "the most human line in the whole account")
    text(s, "ʿUmar had prepared a speech.\nHe never gave it.",
         Inches(0.85), Inches(0.95), Inches(11.6), Inches(1.5),
         size=38, color=TEAL, font=EN, spacing=1.25)
    text(s, "سیدنا عمر فاروق ؓ", Inches(8.3), Inches(0.95), Inches(4.3), Inches(0.7),
         size=25, color=TEAL, font=UR, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True, spacing=1.85)
    text(s, AR_UMAR_SELF, Inches(0.8), Inches(2.7), Inches(11.7), Inches(1.5),
         size=33, color=DARK, font=AR, cs=AR, align=PP_ALIGN.CENTER, is_rtl=True, spacing=1.45)
    text(s, "“By Allah, he did not leave out one phrase that had pleased me in what I had "
            "prepared —\nhe said it off the cuff, and better, until he had finished.”",
         Inches(1.0), Inches(4.45), Inches(11.3), Inches(1.2),
         size=23, color=INK, font=EN, align=PP_ALIGN.CENTER, italic=True, spacing=1.35)
    rule(s, Inches(5.9), Inches(5.8), Inches(1.5), GOLD, Pt(1.5))
    text(s, "AL-BIDAYA WA'L-NIHAYA  ·  VOL 5, PRINTED pp. 345–346",
         Inches(0.8), Inches(6.0), Inches(11.7), Inches(0.4),
         size=14, color=TEAL, font=SANS, align=PP_ALIGN.CENTER)
    text(s, "البدایہ والنہایہ — ج۵ ص۳۴۵–۳۴۶", Inches(0.8), Inches(6.45), Inches(11.7), Inches(0.5),
         size=16, color=MUTED, font=UR, cs=UR, align=PP_ALIGN.CENTER, is_rtl=True, spacing=1.85)
    note(s, "0:30 block. REMEMBER WHO IS TELLING THIS. It is 'Umar (RA), about himself, from the\n"
            "minbar, years later, in front of the people who were in the room. He is the one who\n"
            "says he had a speech ready and that Abu Bakr (RA) said all of it better, unprepared.\n"
            "That is why this account is trustworthy in a way an admirer's account never is - say\n"
            "that sentence, it is the 'how do we know' of the whole evening.\n"
            "Do not add a word of praise of your own. The report is already doing it.")

    # ------------------------------------------------------------- 22 · Abu Bakr
    s = sourced(prs, AR_SIDDIQ,
                "“The Arabs will not recognise this authority except in this clan of Quraysh; "
                "they are the middlemost of the Arabs in lineage and in dwelling.”",
                "AL-BIDAYA WA'L-NIHAYA  ·  VOL 5, PRINTED p. 346",
                "البدایہ والنہایہ — ج۵ ص۳۴۶",
                label="and then abu bakr spoke", speaker_ur="سیدنا ابوبکر صدیق ؓ")
    note(s, "0:30 block. THE DECISIVE ARABIC OF THE EVENING (research note 3.1).\n"
            "SAY THE SENTENCE BEFORE IT FIRST - it is on the same page and it is the shape of the\n"
            "man: 'whatever good you have mentioned of yourselves, you are its people.' He concedes\n"
            "the Ansar's merit in full, and only then argues.\n"
            "THEN THE FACT THAT CARRIES THE WHOLE BLOCK: he took the hand of 'Umar (RA) and the\n"
            "hand of Abu 'Ubayda b. al-Jarrah (RA), amin al-umma, and offered the Ansar whichever\n"
            "of the two they wished. HE PUT FORWARD TWO OTHER MEN, NOT HIMSELF. Same page.\n"
            "'Umar's (RA) reaction, same page again: he would sooner be brought forward and\n"
            "beheaded than lead a people among whom Abu Bakr (RA) was standing.\n"
            "DO NOT QUOTE 'al-a'imma min Quraysh' - it is not carried verbatim on these pages\n"
            "(QA_BANK 1.10). What Ibn Kathir does supply instead is this, and the marfu' hadith at\n"
            "j.5 p.348 which has shawahid in Bukhari 3495 and Muslim 1818.")

    # ------------------------------------------------------------- 23 · al-Hubab
    s = sourced(prs, AR_HUBAB,
                "“I am the rubbing-post and the propped palm. One amir from us and one amir "
                "from you, O company of Quraysh.”",
                "AL-BIDAYA WA'L-NIHAYA  ·  VOL 5, PRINTED p. 346",
                "البدایہ والنہایہ — ج۵ ص۳۴۶",
                label="the proposal that was not taken up",
                speaker_ur="سیدنا حباب بن المنذر ؓ — الخزرج")
    note(s, "0:30 block. al-Hubab b. al-Mundhir (RA), of al-Khazraj - point at the chart.\n"
            "Both images are proverbial and Ibn Kathir's own footnotes explain them: the JIDHL is\n"
            "the post set up for mangy camels to rub against - i.e. the man people are healed by\n"
            "consulting; the 'UDHAYQ AL-MURAJJAB is the prized date palm propped with stone or\n"
            "timber because its height and its load make it liable to fall. Malik's own gloss on\n"
            "the same page: 'ana dahiyatuha' - I am the one whose judgement is sought.\n"
            "He is named at the END of j.5 p.346, on the authority of Sa'id b. al-Musayyab.\n"
            "HIS LONGER SPEECH - the famous one - is NOT in al-Bidaya. Do not import it (note 3.3).\n"
            "NARRATE, DO NOT ADJUDICATE. The proposal was made; it was not taken up. Move on.")

    # ------------------------------------------------------------- 24 · two reports
    s = blank(prs, CREAM)
    eyebrow(s, "how it turned  ·  and what a history book does with a disagreement")
    text(s, "Two reports. Both in the book. We give both.",
         Inches(0.85), Inches(0.92), Inches(11.6), Inches(0.8), size=34, color=TEAL, font=EN)
    band(s, Inches(1.88), Inches(0.045), GOLD, Inches(0.85), Inches(11.6))
    for i, (head, ar, en) in enumerate([
            ("REPORT A  ·  VOL 5, PRINTED p. 346", AR_HAND_A,
             "“I said: hold out your hand, Abu Bakr. He held out his hand, and I gave him "
             "bayʿah; and the Muhajirun gave bayʿah, then the Ansar.”"),
            ("REPORT B  ·  VOL 5, PRINTED p. 347", AR_HAND_B,
             "“… and a man of the Ansar got ahead of me, and struck his hand before "
             "I could strike it.”")]):
        cx = 0.85 + i * 6.05
        text(s, head, Inches(cx), Inches(2.2), Inches(5.5), Inches(0.3),
             size=12, color=MAROON, font=SANS, bold=True)
        text(s, ar, Inches(cx), Inches(2.6), Inches(5.5), Inches(1.6),
             size=25, color=DARK, font=AR, cs=AR, align=PP_ALIGN.RIGHT, is_rtl=True, spacing=1.4)
        text(s, en, Inches(cx), Inches(4.32), Inches(5.5), Inches(1.4),
             size=18, color=INK, font=EN, italic=True, spacing=1.3)
    band(s, Inches(5.85), Inches(1.35), DARK)
    text(s, "And the book names him — Bashir b. Saʿd: an Ansari, of al-Khazraj, the father of "
            "al-Nuʿman b. Bashir.\nThe first hand extended to Abu Bakr was an Ansari hand.",
         Inches(0.9), Inches(6.05), Inches(9.4), Inches(1.0),
         size=19, color=CREAM, font=EN, spacing=1.3)
    text(s, "ج۵ ص۳۴۷", Inches(10.6), Inches(6.28), Inches(2.1), Inches(0.55),
         size=20, color=GOLD, font=UR, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True, spacing=1.8)
    note(s, "0:30 block. A METHOD MOMENT AS WELL AS A NARRATIVE ONE - give it two minutes.\n"
            "Report A is Malik / al-Zuhri (j.5 p.346). Report B is Ibn Ishaq (j.5 p.347), and the\n"
            "man is named on that same page on the authority of Muhammad b. Sa'd - Bashir b.\n"
            "Sa'd (RA), the father of al-Nu'man b. Bashir (RA).\n"
            "BOTH ARE IN THE BOOK. REPORT BOTH. DO NOT CHOOSE (research note 1.5). Say that out\n"
            "loud - it is the same discipline as the hollow markers on timeline 3, and the room\n"
            "should hear you doing it twice in one evening.\n"
            "IT WAS NOT QURAYSH WHO ENDED IT. IT WAS ONE OF THE ANSAR. Say it plainly, let it sit.\n"
            "AND WHAT ACTUALLY SETTLED IT, in Ibn Kathir's telling, is on the same page (j.5 p.347,\n"
            "Ibn Mas'ud (RA), isnad hasan): 'Umar (RA) asked the Ansar - do you not know that the\n"
            "Messenger of Allah (peace be upon him) ordered Abu Bakr to lead the people in prayer?\n"
            "Which of you would be content to go ahead of Abu Bakr? And the Ansar said: we seek\n"
            "refuge in Allah from going ahead of Abu Bakr. THE PRAYER SETTLED IT. Everything else\n"
            "was context - the ummah had already been standing behind him for days.")

    # ------------------------------------------------------------- 25 · the rule
    s = sourced(prs, AR_RULE,
                "“Whoever gives bayʿah to a man without the consultation of the Muslims "
                "— there is no bayʿah for him.”",
                "AL-BIDAYA WA'L-NIHAYA  ·  VOL 5, PRINTED p. 346",
                "البدایہ والنہایہ — ج۵ ص۳۴۶",
                label="the rule that day produced", speaker_ur="سیدنا عمر فاروق ؓ")
    note(s, "0:30 block. THE MOST USEFUL SINGLE LINE IN THE STRAND, and the reason 'Umar (RA) gave\n"
            "that khutba at all: he is legislating against a repeat of an improvised day.\n"
            "The clauses just before it, same page, are him explaining his own reasoning - they\n"
            "feared that if they left the gathering with no bay'ah, another would be made behind\n"
            "them, and then either they accept what they do not agree with or they oppose it and\n"
            "there is corruption.\n"
            "IF A SLIP SAYS 'FALTA' - QA_BANK 1.1, and answer it at the door, not from the podium.\n"
            "The word means SUDDEN, WITHOUT PRIOR ARRANGEMENT - not illegitimate. 'Umar (RA) said\n"
            "it and confirmed it, and in the same breath added that Allah protected them from its\n"
            "danger, and that there is nobody today like Abu Bakr (RA). NEVER quote 'falta' without\n"
            "the two clauses after it. DO NOT RAISE IT YOURSELF - it is not on any slide for that\n"
            "reason.")

    # ------------------------------------------------------------- 26 · two stages
    s = sourced(prs, AR_TWO_STAGE,
                "“A group had given him bayʿah before that, in the saqifa of Banu Saʿida; "
                "and the general bayʿah was on the minbar.”",
                "AL-BIDAYA WA'L-NIHAYA  ·  VOL 5, PRINTED p. 349",
                "البدایہ والنہایہ — ج۵ ص۳۴۹",
                label="the whole structure, in one sentence")
    note(s, "0:30 block. THE SINGLE BEST SLIDE LINE IN THE STRAND (research note 9, item 2).\n"
            "Ibn Kathir gives it from al-Zuhri from Anas (RA); the edition refers it to Bukhari\n"
            "7219. It is 'Umar (RA) speaking on the Tuesday - the morrow of the day the Messenger\n"
            "of Allah (peace be upon him) died - with Abu Bakr (RA) standing silent beside him.\n"
            "THE POINT: the saqifa was not the whole thing and was never presented as the whole\n"
            "thing. TWO STAGES - a particular bay'ah on Monday, a general one on Tuesday from the\n"
            "minbar, in the mosque, in front of everyone. Both before the burial.\n"
            "EXTRA IF TIME (read from the printed card, never from memory): Abu Bakr's (RA)\n"
            "inaugural khutba is on the same page, j.5 p.349, isnad sahih - 'I have been put in\n"
            "charge of you and I am not the best of you... obey me as long as I obey Allah and His\n"
            "Messenger; if I disobey them, you owe me no obedience.' Ibn Kathir's own gloss on the\n"
            "'not the best of you' clause, same page: it is humility and self-effacement, for they\n"
            "are agreed that he was the best of them.\n"
            "THE OTHER INAUGURAL KHUTBA at j.7 p.8 is Sayf b. 'Umar via Tabari. DO NOT USE IT\n"
            "(QA_BANK 1.11). This one does everything it would have done.")

    # ------------------------------------------------------------- 27 · Sa'd b. Ubada
    s = sourced(prs, AR_SAAD,
                "“You have spoken the truth. We are the ministers, and you are the commanders.”",
                "AL-BIDAYA WA'L-NIHAYA  ·  VOL 5, PRINTED p. 348",
                "البدایہ والنہایہ — ج۵ ص۳۴۸",
                label="and the man who was ill that day",
                speaker_ur="سیدنا سعد بن عبادہ ؓ — سیّدُ الخزرج")
    note(s, "0:30 block. REPORTED EXACTLY AS IBN KATHIR REPORTS IT - neither softened nor sharpened\n"
            "(spec 4, register rules).\n"
            "Ibn Kathir gives this its own section and titles it himself, j.5 p.347: 'dhikr i'tiraf\n"
            "Sa'd b. 'Ubada bi-sihhati ma qalahu al-Siddiq yawm al-saqifa'.\n"
            "THIS ONE LINE IS THE WHOLE of what al-Bidaya reports Sa'd (RA) as saying. The book does\n"
            "not say he gave bay'ah and does not say he refused.\n"
            "WHAT MAY BE SAID IF ASKED, AND NO MORE (QA_BANK 1.2): he later left Medina for al-Sham\n"
            "and died at Hawran; the year is disputed in the sources themselves - 14 to 16 AH\n"
            "(Siyar j.1 pp.277-278). The refusal story rests on al-Waqidi, and al-Dhahabi himself\n"
            "brands its chain in three words: 'isnaduha kama tara'.\n"
            "STATE THE ACCEPTANCE. SAY THE REST IS DISPUTED ON WEAK CHAINS. DO NOT ADJUDICATE.")

    # ------------------------------------------------------------- 28 · Ali (RA)
    s = sourced(prs, AR_ALI,
                "“The Messenger of Allah ﷺ appointed no successor, that I should appoint one. "
                "But if Allah intends good for the people, He will gather them after me upon the "
                "best of them — as He gathered them after their Prophet upon the best of them.”",
                "AL-BIDAYA WA'L-NIHAYA  ·  VOL 5, PRINTED p. 353",
                "البدایہ والنہایہ — ج۵ ص۳۵۳",
                label="the last word on that day belongs to him",
                speaker_ur="سیدنا علی المرتضیٰ ؓ")
    note(s, "0:30 block, LAST SLIDE OF IT. Add nothing after it. Let it close the block.\n"
            "Ibn Kathir grades this isnad JAYYID - al-Bayhaqi via al-Sha'bi from Abu Wa'il, 'Ali\n"
            "(RA) asked whether he would appoint a successor (research note 3.8b).\n"
            "WHY THIS ONE: it describes the outcome of the saqifa as Allah's own gathering, and it\n"
            "comes from the mouth in whose name the objection is usually made. Safest and strongest\n"
            "quotation in the whole strand for this room.\n"
            "IF A SLIP ASKS WHY 'ALI (RA) AND AL-ZUBAYR (RA) WERE NOT THERE - QA_BANK 1.3, and the\n"
            "answer is Ibn Kathir's own at j.5 pp.350-351: both gave bay'ah on the first day or the\n"
            "second, and their own stated grievance was procedural, not substantive - 'we were\n"
            "displeased only at being left out of the consultation, and we hold that Abu Bakr was\n"
            "the most deserving of it'.\n"
            "NEVER improvise on the mushajarat from the floor. Session 3, with usul. QA_BANK 0.2.")

    # ------------------------------------------------------------- 29 · the state
    s, rect = picture_slide(prs, "map_arabia_blank", "This is the state, the night he ﷺ died",
                            "11 AH  ·  delivered flatly", bottom=7.38)
    for place, lab, side, colour in [("taif", "al-Ta'if", "right", TEAL),
                                     ("najran", "Najran", "left", TEAL),
                                     ("hadramawt", "Hadramawt", "below", TEAL),
                                     ("bahrain", "al-Bahrayn", "above", TEAL),
                                     ("daba", "Uman", "above", TEAL),
                                     ("sanaa", "San'a", "below", MAROON),
                                     ("yamama", "al-Yamama", "above", MAROON),
                                     ("buzakha", "Najd", "above", MAROON)]:
        pin(s, rect, ARABIA, place, lab, side, colour)
    text(s, "A governor of the\nProphet ﷺ in place",
         Inches(0.42), Inches(1.4), Inches(2.65), Inches(0.85),
         size=17, color=TEAL, font=EN, bold=True, spacing=1.3)
    text(s, "Makkah · al-Ta'if\nNajran · Hadramawt\nal-Bahrayn · Uman\nand Medina itself",
         Inches(0.42), Inches(2.3), Inches(2.65), Inches(1.6),
         size=16, color=INK, font=EN, spacing=1.35)
    text(s, "Already gone —\nin his lifetime ﷺ",
         Inches(0.42), Inches(4.2), Inches(2.65), Inches(0.85),
         size=17, color=MAROON, font=EN, bold=True, spacing=1.3)
    text(s, "al-Yamama — Musaylima\nNajd — Tulayha\nSan'a — taken by\nal-Aswad al-ʿAnsi",
         Inches(0.42), Inches(5.1), Inches(2.65), Inches(1.6),
         size=16, color=MAROON, font=EN, spacing=1.35)
    text(s, "This is the map.\nNo commentary\ntonight.",
         Inches(10.55), Inches(1.4), Inches(2.45), Inches(1.3),
         size=19, color=TEAL, font=EN, spacing=1.35)
    text(s, "AL-BIDAYA WA'L-NIHAYA\nVOL 7, pp. 13–14, 17, 19,\n26, 37–41  ·  VOL 4, p. 642\n"
            "VOL 5, pp. 97–98",
         Inches(10.55), Inches(3.0), Inches(2.45), Inches(1.4),
         size=11, color=TEAL, font=SANS, spacing=1.3)
    note(s, "0:38 THE STATE AT 11 AH (3 min). DELIVERED FLATLY, AS A STATE OF AFFAIRS. NO COMMENTARY.\n"
            "Governors region by region, from docs/research/governors-at-11h.md §1. Name them with\n"
            "the honorific as you point; they are deliberately NOT printed on the slide:\n"
            "  Makkah      'Attab b. Asid (RA), with Mu'adh b. Jabal (RA) left beside him  j.4 p.642\n"
            "  al-Ta'if    'Uthman b. Abi al-'As (RA), set over his own people; Abu Bakr (RA)\n"
            "              confirmed him in place, and so did 'Umar (RA)          Siyar j.2 p.374\n"
            "  Najran      'Amr b. Hazm (RA) sent, beside their own chief         j.5 pp.97-98\n"
            "  Hadramawt   Ziyad b. Labid (RA)                                    j.7 p.14\n"
            "  al-Bahrayn  al-'Ala' b. al-Hadrami (RA), over al-Mundhir b. Sawa   j.7 pp.37-38\n"
            "  Uman        Jayfar and 'Abbad, the Azdi rulers                     j.7 p.41\n"
            "  San'a       Shahr b. Badhaam, confirmed - and KILLED by al-Aswad   j.7 p.14\n"
            "ALREADY LOST BEFORE THE DEATH, and say it plainly - it is next week's whole subject:\n"
            "  al-Yamama held by Musaylima al-Kadhdhab (j.7 p.19); Najd - Banu Asad and Ghatafan -\n"
            "  by Tulayha al-Asadi, who 'apostatised in the lifetime of the Prophet (peace be upon\n"
            "  him)' (j.7 p.26); Yemen taken by al-Aswad al-'Ansi (j.7 p.14).\n"
            "Pin placement is PLACEMENT ONLY, never a claim about a site (MAPS.md).\n"
            "TO DO before delivery: build the labelled governors map in tools/mapstudio and save\n"
            "the scene JSON, so this slide stops depending on hand-placed pins.")

    # ------------------------------------------------------------- 30 · the principle
    s = sourced(prs, AR_UMMAL,
                "“No one has a better right to the work than the Prophet's ﷺ own appointees. "
                "Go back to your posts.”",
                "SIYAR AʿLAM AL-NUBALAʼ  ·  AL-DHAHABI  ·  VOL 1, PRINTED p. 262",
                "سیر أعلام النبلاء — الذہبی رحمہ اللہ — ج۱ ص۲۶۲",
                label="and the rule that held it together",
                speaker_ur="سیدنا ابوبکر صدیق ؓ")
    note(s, "0:38 block. When the news reached the provinces, some of the 'ummal left their posts\n"
            "and came home. This was the answer, and it is THE WHOLE ADMINISTRATIVE PRINCIPLE OF\n"
            "11 AH IN ONE LINE: the Prophet's (peace be upon him) appointments stand.\n"
            "SOURCE: al-Dhahabi, Siyar j.1 p.262, in the notice of 'Amr b. Sa'id b. al-'As (RA).\n"
            "Visible as a fact on the ground at al-Ta'if - 'thumma aqarrahu Abu Bakr 'ala al-Ta'if,\n"
            "thumma 'Umar' (Siyar j.2 p.374).\n"
            "Say it once and go to the army. Do not draw a modern lesson from it.")

    # ------------------------------------------------------------- 31 · the army
    s = blank(prs, DARK)
    eyebrow(s, "and one more thing about that night", GOLD)
    text(s, "The field army was not in the capital.",
         Inches(0.9), Inches(1.1), Inches(11.5), Inches(0.9), size=41, color=CREAM, font=EN)
    rule(s, Inches(0.9), Inches(2.2), Inches(2.6))
    for i, (ar, en, cite) in enumerate([
            (AR_JURF, "Jaysh Usama had gone out and camped at al-Jurf, just outside Medina, "
                      "pointed north at the marches of al-Balqaʼ in al-Sham.",
             "VOL 7, PRINTED p. 9"),
            (AR_KHUSHUB, "A second report has it already moved on to Dhu Khushub, a day's "
                         "march out, when the Prophet ﷺ passed away.", "VOL 7, PRINTED p. 11")]):
        y = 2.55 + i * 1.72
        text(s, ar, Inches(8.1), Inches(y), Inches(4.5), Inches(0.7),
             size=26, color=GOLD, font=AR, cs=AR, align=PP_ALIGN.RIGHT, is_rtl=True, spacing=1.4)
        text(s, en, Inches(0.9), Inches(y + 0.02), Inches(6.9), Inches(1.2),
             size=21, color=CREAM, font=EN, spacing=1.3)
        text(s, cite, Inches(0.9), Inches(y + 1.12), Inches(6.9), Inches(0.3),
             size=11, color=GOLD, font=SANS, bold=True)
    text(s, "So on that night the state's army was outside its capital — and Medina's own guard "
            "posts were manned\nby the Companions who had stayed behind.",
         Inches(0.9), Inches(6.05), Inches(11.5), Inches(1.0),
         size=20, color=GOLD, font=EN, italic=True, spacing=1.3)
    note(s, "0:38 block, closing. Two reports again, and both are in the book. Give both.\n"
            "SOURCE: al-Bidaya j.7 p.9 (al-Jurf - the editor's footnote: the place near Medina where\n"
            "the Muslims camped when they meant to campaign) and j.7 p.11 (Dhu Khushub, a stage\n"
            "from Medina on the road to al-Sham).\n"
            "Medina's guard posts - al-anqab - j.7 p.18: 'Ali, al-Zubayr, Talha, Sa'd, 'Abd\n"
            "al-Rahman b. 'Awf and 'Abd Allah b. Mas'ud (radiya Allahu 'anhum). Honorific on each.\n"
            "THE FIGURE 700 is the only one the chapter gives (j.7 p.11) and Ibn Kathir pauses over\n"
            "its narrator. Say 'the number the book gives', or better, give no number at all.\n"
            "DO NOT tell the story of Abu Bakr (RA) sending it out anyway - that is next week's\n"
            "opening and it must not be spent tonight.")

    # ------------------------------------------------------------- 32 · آج کا سبق
    s = blank(prs, CREAM)
    eyebrow(s, "aaj ka sabaq  ·  write this one down")
    text(s, "The order in which things happened\nis the first thing to know\nand the last thing "
            "to guess.",
         Inches(0.9), Inches(1.1), Inches(11.5), Inches(3.0),
         size=43, color=TEAL, font=EN, spacing=1.3)
    text(s, "آج کا سبق", Inches(9.6), Inches(1.0), Inches(2.9), Inches(0.8),
         size=30, color=GOLD, font=UR, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True, spacing=1.9)
    rule(s, Inches(0.9), Inches(4.3), Inches(2.6))
    text(s, "جو پہلے ہوا، وہ پہلے جاننا ہے — اور تاریخوں میں اندازہ نہیں لگانا۔",
         Inches(1.3), Inches(4.6), Inches(11.1), Inches(0.9),
         size=27, color=DARK, font=UR, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True, spacing=2.0)
    text(s, "And: an institution's first test is the day its founder is gone.",
         Inches(0.9), Inches(5.85), Inches(11.5), Inches(0.6),
         size=22, color=MUTED, font=EN, italic=True)
    note(s, "0:41 AAJ KA SABAQ (2 min). Put it up, read it ONCE, then be quiet.\n"
            "NINETY SECONDS OF SILENCE while every person writes it into the workbook by hand.\n"
            "Two volunteers at most. Say 'shukriya' and NOTHING else - do not improve on what they\n"
            "said. Do not add a second lesson from the podium.\n"
            "(to verify) THE URDU WORDING IS NOT FINAL. docs/catalogue/LESSONS.md is still empty;\n"
            "the sense on this slide is the spec's own (§4, 0:41). Settle the Urdu into LESSONS.md\n"
            "before delivery and rebuild - this slide and the workbook must not disagree\n"
            "(CLAUDE.md 4).")

    # ------------------------------------------------------------- 33 · اگلے ہفتے
    s, rect = picture_slide(prs, "map_arabia_blank", "This is the state on the night he ﷺ died",
                            "agle hafte", bottom=6.24)
    for place, lab, side, colour in [("taif", "al-Ta'if", "right", TEAL),
                                     ("najran", "Najran", "left", TEAL),
                                     ("hadramawt", "Hadramawt", "below", TEAL),
                                     ("bahrain", "al-Bahrayn", "above", TEAL),
                                     ("daba", "Uman", "above", TEAL),
                                     ("sanaa", "San'a", "below", MAROON),
                                     ("yamama", "al-Yamama", "above", MAROON),
                                     ("buzakha", "Najd", "above", MAROON)]:
        pin(s, rect, ARABIA, place, lab, side, colour, size=11)
    band(s, Inches(6.24), Inches(1.26), DARK)
    text(s, "Within months, most of this map has broken away.",
         Inches(0.7), Inches(6.42), Inches(7.8), Inches(0.6),
         size=26, color=CREAM, font=EN)
    text(s, "کیوں؟ اور یہ واپس کیسے آیا؟", Inches(8.6), Inches(6.34), Inches(4.1), Inches(0.85),
         size=28, color=GOLD, font=UR, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True, spacing=1.9)
    note(s, "0:43 AGLE HAFTE (2 min). END ON THE QUESTION, NOT A SUMMARY (CLAUDE.md §2).\n"
            "Say only this: this is the state on the night the Prophet (peace be upon him) died.\n"
            "Within months, most of this has broken away.\n"
            "THEN THE QUESTION, and STOP TALKING: kyun? aur yeh wapas kaise aaya?\n"
            "Do not answer it. Do not hint at it. Do not summarise the evening.\n"
            "Hold up the workbook - the only thing to bring back. Then the two housekeeping lines:\n"
            "slips into the box, and I am here for fifteen minutes.")

    # ------------------------------------------------------------- 34 · sources
    s = blank(prs, CREAM)
    eyebrow(s, "sources  ·  show only if asked")
    text(s, "Where tonight came from",
         Inches(0.85), Inches(0.95), Inches(11.6), Inches(0.8), size=34, color=TEAL, font=EN)
    band(s, Inches(1.9), Inches(0.045), GOLD, Inches(0.85), Inches(11.6))
    text(s, "Tareekh-e-Ummat — Muhammad Ismaʿil Rehan\n"
            "        muqaddima, printed pp. 33, 52–53, 57, 58, 61, 66\n\n"
            "al-Iʿlan bi'l-Tawbikh — al-Sakhawi\n"
            "        printed pp. 93, 97, 100–101\n\n"
            "al-Bidaya wa'l-Nihaya — Ibn Kathir\n"
            "        vol. 5, pp. 340–353;  vol. 4, pp. 642, 670;  vol. 7, pp. 5–41\n\n"
            "Siyar Aʿlam al-Nubalaʼ — al-Dhahabi\n"
            "        vol. 1, pp. 262, 270–278;  vol. 2, p. 374",
         Inches(0.85), Inches(2.2), Inches(11.6), Inches(3.6),
         size=19, color=INK, font=EN, spacing=1.4)
    text(s, "All of these are works this course's own muqaddima names and relies on.\n"
            "I am reading a book. I am not writing history.",
         Inches(0.85), Inches(5.75), Inches(11.6), Inches(0.95),
         size=19, color=MAROON, font=EN, italic=True, spacing=1.35)
    text(s, "تاریخِ امت  ·  الإعلان بالتوبيخ  ·  البدایہ والنہایہ  ·  سیر أعلام النبلاء",
         Inches(0.85), Inches(6.72), Inches(11.6), Inches(0.6),
         size=18, color=MUTED, font=UR, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True, spacing=1.85)
    note(s, "NOT PART OF THE 45 MINUTES. Keep it for credibility and show it only if someone asks\n"
            "where something came from.\n"
            "Naming the frame openly is the defence - never claim a neutrality the course does not\n"
            "have (QA_BANK 2.2, 2.4). Tabari is corroboration only under CLAUDE.md §4 and was NOT\n"
            "used tonight for anything.")

    # ------------------------------------------------------------- 35 · EXTRA
    s = sourced(prs, AR_SUHAYL,
                "“Leave him, ʿUmar. He will yet take a stand you will be glad of.”",
                "AL-KAMIL FI'L-TARIKH  ·  IBN AL-ATHIR  ·  VOL 2, PRINTED p. 25",
                "الکامل فی التاریخ — ابن الاثیر رحمہ اللہ — ج۲ ص۲۵",
                label="EXTRA  ·  not in the 45 minutes  ·  hold in reserve",
                speaker_ur="سیدنا سہیل بن عمرو ؓ — بنو عامر بن لؤی")
    note(s, "EXTRA - NOT IN THE 45 MINUTES. The v3 spec's timetable has no room for it; it is here\n"
            "so it is prepared and not lost. Use it only if a block collapses, or at the door.\n"
            "THE STORY: at Badr, Suhayl b. 'Amr - the orator of Quraysh - was among the prisoners.\n"
            "'Umar (RA) asked leave to pull out his front teeth so he could never stand and speak\n"
            "against the Prophet (peace be upon him) again. This was the answer. Al-Kamil j.2\n"
            "pp.24-25. And when the news of the death reached Makkah in 11 AH and the city began\n"
            "to waver, it was Suhayl (RA) who stood and addressed the people, and Makkah held -\n"
            "al-Bidaya j.5 pp.397-398, al-Kamil j.2 p.186.\n"
            "TWO WORDINGS, DO NOT MERGE THEM: this is Ibn al-Athir's. Ibn Kathir's, at al-Bidaya\n"
            "j.4 p.114, is 'innahu 'asa an yaquma maqaman la tadhummuhu' - cite whichever page you\n"
            "quote and no blend of the two.\n"
            "ISNAD HONESTY, SAY IT IF ASKED - QA_BANK 2.3: this is maghazi reporting, not a sahih\n"
            "chain, and IBN KATHIR HIMSELF grades his own version 'mursal, indeed mu'dal'. Saying\n"
            "so is more impressive than a confident silence would be.")

    return save(prs, path)


if __name__ == "__main__":
    if "--verify" in sys.argv:
        sys.exit(0 if verify() else 1)
    if not verify():
        sys.exit("Arabic drifted from the research notes — fix before building.")
    out = build(os.path.join(HERE, "L01.pptx"))
    from pptx import Presentation as _P
    print("saved: %s  (%d slides)" % (out, len(_P(out).slides)))
