"""Build L01 v3 — «وقت، جگہ، اور ایک رات».

    python L01_overview/build.py

Session 1 rebuilt 2026-09-03: orientation in time and space, then the clan structure of Medina,
then سقیفہ بنی ساعدہ, ending on the map of Arabia the night before the ردہ.
Spec: docs/specs/2026-09-03-L01-v3-spec.md · Decisions: docs/DECISIONS.md #12-#17

English carries the slides; Urdu appears only where it does real work, always with an English
rendering beside it, always in its own text box. Latin digits — mixing Urdu-Indic digits with
Latin punctuation makes the bidi algorithm reorder the line into nonsense.

Every Arabic line below is copied verbatim from a research note in docs/research/ and carries its
PRINTED page. Nothing here is typed from memory. Depth lives in Script.md and BRIEFING.md.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "series"))
from deckkit import *  # noqa: F401,F403
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt

BN = "al-Bidaya wa'l-Nihaya  ·  Ibn Kathir"
KAMIL = "al-Kamil fi'l-Tarikh  ·  Ibn al-Athir"


def ur(slide, txt, y, size=26, color=MUTED, x=0.9, w=11.5, h=1.0):
    """An Urdu line in its own box. Never inline with English — that is what mangles the render."""
    return text(slide, txt, Inches(x), Inches(y), Inches(w), Inches(h),
                size=size, color=color, font=UR, cs=UR,
                align=PP_ALIGN.RIGHT, is_rtl=True, spacing=1.95)


def build(path):
    prs = deck()

    # ---------------------------------------------------------------- 0:00  آغاز
    title_slide(prs, "One night, and the whole map",
                "وقت، جگہ، اور ایک رات",
                "Where we are in time · where we are on the map · and one night in Medina",
                "LESSONS FROM HISTORY  ·  SESSION 1 OF 10")

    s = statement_slide(prs, "Almost none of us could name three men\nwho were in that courtyard.",
                        kicker="the destination, named first", bg=DARK, fg=CREAM)
    text(s, "On a Monday in 11 AH, in a covered courtyard in Medina, a small number of men "
            "decided who would lead the Muslims after the Prophet ﷺ.",
         Inches(0.9), Inches(4.75), Inches(11.5), Inches(0.9), size=22, color=GOLD, font=EN, cs=AR,
         spacing=1.35)
    text(s, "Tonight we fix that. But not yet — first, when are we, and where?",
         Inches(0.9), Inches(5.75), Inches(11.5), Inches(0.6), size=21, color=CREAM, font=EN,
         italic=True)
    note(s, "0:00 (2 min). Say the Q&A policy here: no questions during the 45 minutes, slips into "
            "the box at the door, I stay 15 minutes afterwards. Say it once, apply it all ten weeks.")

    # ---------------------------------------------------------------- 0:02  تاریخ کیا ہے
    s = statement_slide(prs, "History is events —\nand the order they came in.",
                        kicker="what is tarikh?")
    text(s, "Every discipline asks what happened. Tarikh's own question is WHEN, and IN WHAT ORDER.",
         Inches(0.9), Inches(4.6), Inches(11.5), Inches(0.7), size=22, color=MAROON, font=EN,
         italic=True)
    ur(s, "تاریخ یعنی واقعات، "
          "اور ان کی ترتیب", 5.35, 28, TEAL)
    note(s, "0:02 (4 min). Definition from the muqaddima, printed pp.32-33 (al-Sakhawi's wording). "
            "Do not turn this into a methodology lecture — see DECISIONS.md #9.")

    quote_slide(prs,
        "لَمَّا اسْتَعْمَلَ "
        "الرُّوَاةُ الْكَذِبَ "
        "اسْتَعْمَلْنَاهُمُ "
        "التَّارِيخَ",
        "“When the transmitters began to deal in lies,\nwe dealt with them by means of dates.”",
        "Sufyan al-Thawri  ·  muqaddima, printed p.57  ·  verified",
        label="why the order matters")

    s = statement_slide(prs, "A forgery dies on a date.",
                        kicker="how chronology catches a lie", bg=TEAL, fg=CREAM)
    text(s, "A document was produced claiming the Prophet ﷺ exempted the people of Khaybar from taxes.\n"
            "Al-Khatib al-Baghdadi destroyed it without arguing about content at all:\n"
            "one witness named on it accepted Islam AFTER Khaybar; another had died BEFORE it.",
         Inches(0.9), Inches(4.5), Inches(11.5), Inches(1.6), size=20, color=GOLD, font=EN, cs=AR,
         spacing=1.4)
    note(s, "0:04. muqaddima printed p.58 - verified. This is why the whole course is built on a "
            "timeline. Keep it to 90 seconds.")

    # ------------------------------------------------------- THE GUARDRAIL (most important slide)
    s = blank(prs, DARK)
    eyebrow(s, "before we go any further", GOLD)
    text(s, "Three disciplines. One report. Three different jobs.",
         Inches(0.85), Inches(1.05), Inches(11.6), Inches(0.8), size=34, color=CREAM, font=EN)
    band(s, Inches(1.95), Inches(0.035), GOLD, Inches(0.85), Inches(11.6))
    for x, head, body in [
        (0.85, "HADITH", "A report must be authentic\nbefore it can bind.\nIt carries the deen."),
        (5.05, "FIQH", "A report is weighed for\nwhat it obliges.\nIt carries a ruling."),
        (9.25, "TARIKH", "A report is recorded to fix\nwhat happened, and\nin what order."),
    ]:
        text(s, head, Inches(x), Inches(2.35), Inches(3.7), Inches(0.5),
             size=20, color=GOLD, font=SANS, bold=True)
        text(s, body, Inches(x), Inches(2.95), Inches(3.7), Inches(1.9),
             size=19, color=CREAM, font=EN, spacing=1.45)
    band(s, Inches(5.05), Inches(0.02), GOLD, Inches(0.85), Inches(11.6))
    text(s, "So a tarikh report is not a ruling, and it is not a creed.",
         Inches(0.85), Inches(5.3), Inches(11.6), Inches(0.6), size=27, color=CREAM, font=EN)
    ur(s, "تاریخِ اسلام = تاریخِ "
          "مسلمین ۔ یہ مسلمانوں "
          "کی تاریخ ہے، دین کا "
          "ماخذ نہیں",
       5.95, 25, GOLD)
    note(s, "0:05. THE MOST IMPORTANT SLIDE IN THE DECK. Sixty seconds, said calmly, once. "
            "Finish with: we narrate what the books narrate, and we do not judge between the "
            "Companions. DECISIONS.md #14. Session 3 carries the fuller fiqh of the mushajarat.")

    # ---------------------------------------------------------------- 0:06  the three timelines
    map_slide(prs, "l01_tl1_pakistan", "You remember some of this",
              sub="TIMELINE 1  ·  1947 → tonight")
    note(prs.slides[-1], "0:06 (3 min). Name the pegs, do not discuss them. Hand out the worksheet "
                         "here. If short on time this block goes to 90 seconds.")

    map_slide(prs, "l01_tl2_ummah", "All of that is the last centimetre",
              sub="TIMELINE 2  ·  1 AH → tonight")
    note(prs.slides[-1], "0:09 (5 min). THE WHOLE ARC. This is the only place tonight the room sees "
                         "all fourteen centuries. Point at each peg and name the session it belongs "
                         "to. Everything this course covers is on this line.")

    map_slide(prs, "l01_tl3_prophets", "And all of THAT is the last centimetre",
              sub="TIMELINE 3  ·  the order is known; the dates are not")
    s = prs.slides[-1]
    note(s, "0:14 (3 min). CAREFUL AND HONEST. The hollow markers are conventional estimates from "
            "general scholarship. Our sources do NOT fix dates for Adam, Nuh, Ibrahim, Musa or "
            "Dawud. Adam and Nuh are off-scale with no number at all. Say: the order is known from "
            "revelation, the dates are not - and what we do not know, we do not claim. "
            "DECISIONS.md #16. This is the strongest credibility moment of the evening.")

    # ---------------------------------------------------------------- 0:17  the maps
    map_slide(prs, "map_blank", "The edge of the world, not its centre",
              sub="c. 11 AH / 632 CE")
    note(prs.slides[-1], "0:17 (4 min). Rome to the north-west, Persia to the north-east, and Arabia "
                         "between them. Place the six anchor cities. TO DO: a dedicated empires "
                         "overlay would be better than the blank base - see MAPS.md / mapstudio.")

    map_slide(prs, "map_arabia_blank", "Arabia itself", sub="tribes, and where they sat")
    note(prs.slides[-1], "0:21 (3 min). Makkah, Madina, al-Ta'if, al-Yamama, Najran, San'a, "
                         "al-Bahrayn, Uman, Hadramawt. Tribal blocs from "
                         "docs/research/arabian-tribes-and-the-ridda-setup.md.")

    # ---------------------------------------------------------------- 0:24  the clan chart
    map_slide(prs, "l01_clanchart", "Two peoples — and neither was one bloc",
              sub="MADINA, 11 AH")
    note(prs.slides[-1], "0:24 (6 min). THE LOAD-BEARING BLOCK. SHOW the chart; do NOT read it "
                         "aloud - eight sub-clans narrated will lose the room. Name FOUR men out "
                         "loud, each with his clan. The worksheet version is blank and they write "
                         "the chiefs in themselves - that is tonight's hand-writing ritual "
                         "(DECISIONS.md #15). Quraysh tree: al-Bidaya j2 p485, p493.")

    s = statement_slide(prs, "Shortly before the Hijra,\nal-Aws and al-Khazraj had been at war.",
                        kicker="yawm Buʿath")
    text(s, "That is why “who leads” was a live question in that courtyard, "
            "and not an abstract one.",
         Inches(0.9), Inches(4.7), Inches(11.5), Inches(0.7), size=23, color=MAROON, font=EN,
         italic=True)
    text(s, "The Ansar are of al-Azd — Qahtan, southern.      Quraysh are ʿAdnan, northern.\n"
            "An old fault line, and it was in the room.",
         Inches(0.9), Inches(5.45), Inches(11.5), Inches(1.0), size=20, color=MUTED, font=EN, cs=AR,
         spacing=1.4)
    note(s, "0:28. Thirty seconds each on Bu'ath and on Adnan/Qahtan. No more.")

    # ---------------------------------------------------------------- 0:30  the death, then سقیفہ
    s = statement_slide(prs, "Then, on a Monday, he died.",
                        kicker="11 AH", bg=MAROON, fg=CREAM)
    ur(s, "ربیع الاول، گیارہویں "
          "ہجری ۔ مدینہ میں",
       4.7, 28, CREAM)
    note(s, "0:30. al-Bidaya j5 p336-342. Umar (ra) stood and said he had not died. Abu Bakr (ra) "
            "rode in from al-Sunh, uncovered his blessed face, and then spoke.")

    quote_slide(prs,
        "مَنْ كَانَ يَعْبُدُ "
        "مُحَمَّدًا فَإِنَّ "
        "مُحَمَّدًا قَدْ مَاتَ، "
        "وَمَنْ كَانَ يَعْبُدُ "
        "اللَّهَ فَإِنَّ اللَّهَ "
        "حَيٌّ لَا يَمُوتُ",
        "“Whoever used to worship Muhammad — Muhammad has died.\n"
        "Whoever worships Allah — Allah is living and does not die.”",
        BN + "  ·  vol. 5, p. 340-341",
        label="abu bakr al-siddiq, that morning")
    note(prs.slides[-1], "He then recited Al Imran 144. Ibn Abbas (ra): it was as though the people "
                         "had never known the verse until that day. al-Bidaya j5 p340-342.")

    s = statement_slide(prs, "Before the burial,\nthey went to a courtyard.",
                        kicker="saqifat bani saʿida", bg=DARK, fg=CREAM)
    text(s, "Same day. Before he ﷺ was buried. Ibn Kathir says so in those words.\n\n"
            "Present:  Saʿd b. ʿUbada (ra) — ill, wrapped up, of Banu Saʿida "
            "·  Abu Bakr (ra)  ·  ʿUmar (ra)  ·  Abu ʿUbayda (ra)\n"
            "and the Ansar of both al-Aws and al-Khazraj.",
         Inches(0.9), Inches(4.5), Inches(11.5), Inches(1.7), size=20, color=GOLD, font=EN, cs=AR,
         spacing=1.4)
    note(s, "0:31. al-Bidaya j5 p343-345. NOTE: Sa'd b. 'Ubada (ra) gives NO speech in al-Bidaya - "
            "the famous speech is Ibn Hisham/Tabari, outside the safe list. Usayd b. Hudayr (ra) "
            "and Thabit b. Qays (ra) are NOT mentioned at the Saqifah at all. Do not place them "
            "there. See QA_BANK.md 1.9.")

    quote_slide(prs,
        "أنا جُذَيْلُهَا "
        "المُحَكَّك وعُذَيْقُهَا "
        "المُرَجَّب، منا أمير، "
        "ومنكم أمير، يا معشر "
        "قريش",
        "“One commander from us, and one from you — O company of Quraysh.”",
        "al-Hubab b. al-Mundhir (ra), of al-Khazraj  ·  " + BN +
        "  ·  vol. 5, p. 346",
        label="the proposal that was refused")

    quote_slide(prs,
        "فما ذكَرْتُم من خير "
        "فأنتم أهله، وما تَعْرف "
        "العربُ هذا الأمر إِلَّا "
        "لهذا الحيِّ من قُرَيش",
        "“Everything good you have mentioned — you are its people.\n"
        "But the Arabs will not recognise this authority except in this clan of Quraysh.”",
        "Abu Bakr al-Siddiq (ra)  ·  " + BN + "  ·  vol. 5, p. 346",
        label="what he argued")
    note(prs.slides[-1], "And he put forward TWO OTHER MEN, not himself - 'Umar (ra) and Abu "
                         "'Ubayda (ra). al-Bidaya j5 p346. Do NOT quote 'al-a'imma min Quraysh' - "
                         "it is not carried verbatim on these pages. QA_BANK.md 1.10.")

    s = statement_slide(prs, "An Ansari put out his hand first.",
                        kicker="the moment it turned")
    text(s, "Bashir b. Saʿd (ra) — of al-Khazraj, the father of al-Nuʿman b. Bashir (ra) —\n"
            "reached Abu Bakr's (ra) hand before ʿUmar (ra) could, and the people followed.",
         Inches(0.9), Inches(4.5), Inches(11.5), Inches(1.2), size=22, color=INK, font=EN,
         spacing=1.45)
    text(s, BN + "  ·  vol. 5, p. 347",
         Inches(0.9), Inches(5.9), Inches(11.5), Inches(0.4), size=14, color=TEAL, font=SANS)
    note(s, "0:35. It was not Quraysh who ended it. It was one of the Ansar. That is the shape of "
            "the whole evening - say it plainly and let it sit.")

    quote_slide(prs,
        "إِنَّ بيعةَ أبي بكر "
        "كانَتْ فَلْتَة، ألا "
        "وإنها كانَتْ كذلك، "
        "ألا إنَّ اللَّه وَقَى "
        "شَرَّها",
        "“Abu Bakr's bayʿa was sudden and unarranged — yes, so it was.\n"
        "And Allah protected us from its danger.”",
        "ʿUmar al-Faruq (ra), later, from the minbar  ·  " + BN +
        "  ·  vol. 5, p. 345",
        label="the whole account is his own — told against himself")
    note(prs.slides[-1], "CRITICAL: never quote 'falta' without the two clauses after it. In the "
                         "same breath he legislates against repeating it: whoever pledges to a man "
                         "without the consultation of the Muslims, there is no bay'a for him "
                         "(j5 p346). 'Falta' = sudden, unarranged - NOT illegitimate. QA_BANK.md 1.1.")

    # ---------------------------------------------------------------- سہیل — Mecca holds
    s = statement_slide(prs, "Seventeen years earlier,\nat Badr, a prisoner was brought in.",
                        kicker="and far away, in makkah", bg=TEAL, fg=CREAM)
    text(s, "Suhayl b. ʿAmr, the orator of Quraysh. ʿUmar (ra) asked permission to pull out "
            "his two front teeth,\nso that he could never stand and speak against the Prophet "
            "ﷺ again.",
         Inches(0.9), Inches(4.6), Inches(11.5), Inches(1.2), size=21, color=GOLD, font=EN, cs=AR,
         spacing=1.4)
    note(s, "0:37. al-Kamil j2 p24-25.")

    quote_slide(prs,
        "دَعْهُ يَا عُمَرُ؛ "
        "فَسَيَقُومُ مَقَامًا "
        "تَحْمَدُهُ عَلَيْهِ",
        "“Leave him, ʿUmar. He will yet stand somewhere\nand you will be glad of it.”",
        "The Prophet ﷺ, at Badr  ·  " + KAMIL + "  ·  vol. 2, p. 25",
        label="the answer he was given")
    note(prs.slides[-1], "When the news reached Makkah in 11 AH and the city began to waver, the "
                         "governor took cover - and Suhayl (ra) stood and addressed the people, and "
                         "Makkah held. al-Bidaya j5 p397-398, al-Kamil j2 p186. "
                         "HONESTY: this is maghazi reporting, NOT a sahih chain; Ibn Kathir grades "
                         "his own version mursal, indeed mu'dal. SAY SO. QA_BANK.md 2.3.")

    # ---------------------------------------------------------------- 0:38  the state at ۱۱ھ
    map_slide(prs, "map_arabia_blank", "This is the state, the night he died",
              sub="11 AH  ·  the governors, and how far it reached")
    note(prs.slides[-1], "0:38 (3 min). Deliver FLATLY, as a state of affairs. No commentary. "
                         "Governors from docs/research/governors-at-11h.md. Jaysh Usama (ra) is "
                         "already outside Madina. TO DO before delivery: build the labelled "
                         "governors map in tools/mapstudio and save the scene JSON.")

    # ---------------------------------------------------------------- 0:41  آج کا سبق
    s = statement_slide(prs, "Nearness of blood\nwas not the currency.", kicker="tonight's lesson")
    text(s, "Abu Bakr (ra) and Khalid (ra) meet the Prophet ﷺ at the same ancestor. ʿUmar (ra) is a "
            "generation further out.\nAbu ʿUbayda (ra) is further out than all of them — and it "
            "was Abu ʿUbayda (ra) whom al-Siddiq (ra) was minded to name.",
         Inches(0.9), Inches(4.55), Inches(11.5), Inches(1.3), size=20, color=MUTED, font=EN, cs=AR,
         spacing=1.4)
    text(s, "al-Bidaya vol. 2, pp. 485, 493   ·   al-Siyar vol. 1, pp. 5-6",
         Inches(0.9), Inches(5.95), Inches(11.5), Inches(0.4), size=14, color=TEAL, font=SANS)
    note(s, "0:41 (2 min). Everyone writes this into the workbook by hand. Wait for them. "
            "Final Urdu wording to be set in docs/catalogue/LESSONS.md before delivery.")

    # ---------------------------------------------------------------- 0:43  اگلے ہفتے
    s = blank(prs, DARK)
    eyebrow(s, "next week", GOLD)
    text(s, "Within months, most of that map\nhad broken away.",
         Inches(0.9), Inches(1.9), Inches(11.5), Inches(2.0), size=46, color=CREAM, font=EN,
         spacing=1.25)
    rule(s, Inches(0.9), Inches(4.15), Inches(2.6))
    ur(s, "کیوں؟ اور یہ واپس "
          "کیسے آیا؟", 4.55, 40, GOLD, w=11.5, h=1.2)
    text(s, "Why? And how did it come back?",
         Inches(0.9), Inches(5.85), Inches(11.5), Inches(0.6), size=24, color=CREAM, font=EN,
         italic=True)
    note(s, "0:43 (2 min). END ON THE QUESTION. Do NOT summarise. Put the map of Arabia back up "
            "behind this if you can. Then: slips in the box, I am here for fifteen minutes.")

    # ---------------------------------------------------------------- sources, if asked
    s = blank(prs, CREAM)
    eyebrow(s, "show only if asked")
    text(s, "Where tonight came from",
         Inches(0.85), Inches(1.0), Inches(11.6), Inches(0.8), size=34, color=TEAL, font=EN)
    band(s, Inches(1.95), Inches(0.035), GOLD, Inches(0.85), Inches(11.6))
    text(s, "al-Bidaya wa'l-Nihaya  —  Ibn Kathir      (the Saqifah, the wafat, the clan lines)\n"
            "Siyar Aʿlam al-Nubala  —  al-Dhahabi      (the biographical notices)\n"
            "al-Kamil fi'l-Tarikh  —  Ibn al-Athir      (Suhayl b. ʿAmr)\n"
            "Tarikh-e-Ummat-e-Muslima  —  Maulana Muhammad Ismaʿil Rehan   (the muqaddima)",
         Inches(0.85), Inches(2.25), Inches(11.6), Inches(2.5), size=20, color=INK, font=EN,
         spacing=1.75)
    ur(s, "البدایہ والنہایہ  ·  "
          "سیر أعلام النبلاء  ·  "
          "الکامل  ·  "
          "تاریخِ امتِ مسلمہ", 4.75, 24, TEAL)
    text(s, "All four are works this course's own muqaddima names and relies on.\n"
            "I am reading a book. I am not writing history.",
         Inches(0.85), Inches(5.4), Inches(11.6), Inches(1.0), size=20, color=MAROON, font=EN,
         italic=True, spacing=1.4)
    note(s, "Only if asked. Naming the frame openly is the defence - never claim a neutrality the "
            "course does not have. QA_BANK.md 2.2 and 2.4.")

    return save(prs, path)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, "L01.pptx")
    try:
        p = build(out)
    except PermissionError:
        p = build(os.path.join(here, "L01_NEW.pptx"))
        print("L01.pptx was locked by PowerPoint - wrote L01_NEW.pptx instead")
    print(p)
