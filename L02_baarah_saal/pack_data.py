# -*- coding: utf-8 -*-
"""Session 2 — the lectern cue sheet and the audience worksheet.

    python L02_baarah_saal/pack_data.py        # -> CUE.pdf (one page) and WORKSHEET.pdf

Everything here is read off `L02_baarah_saal/SPINE.md`, which is the single source of the running
order (31 cards in 7 acts). Beat times follow the runtime shape in
`docs/specs/2026-09-06-L02-and-production-v4-spec.md` §2. The SPINE card numbers sit in a comment
against each beat, so the deck, the briefing and this file can be checked against each other line
by line.

THE عبرت LINES ARE THE DECK'S, NOT THIS FILE'S. `SLIDES.md` §"The five عبرت lines" says the cue
sheet and the worksheet must print exactly its five, in its order, and slide 59 puts the same five
on screen. `CUE["lessons"]` is a copy of that list; the worksheet rules five blank lines for the
room to write them in. If either list is ever edited, both change together, and `SLIDES.md` is the
one that decides (`DECISIONS.md` #26). The session title here is likewise the deck's slide-1
headline, **Two Years, Three Months**.

WHY THE CUES LOOK STARVED. `pack.cue()` renders, counts the pages Chrome actually produced, and
refuses anything but one. The first passes of this file spilled onto a second page even at the
10pt floor, so **cues were cut, not type shrunk** — 31 SPINE cards collapsed into 16 beats, each
one cue line, and it now holds one page at **11pt**. The measured limits, if this is ever edited:
the A4 landscape print box is 733px tall, the three columns get 667px of it, and one cue line in
the run column costs ~14px and holds ~55 characters before it wraps. The prose lives in the
briefing, which he reads at home; this page only keeps his place (`DECISIONS.md` #22).

LANGUAGE. English throughout (`DECISIONS.md` #19). No Urdu is generated anywhere in this file.
Arabic appears only as verbatim quotation already present in SPINE.md — every fragment is a
contiguous slice of a statement quoted there, and `verify_arabic()` re-checks all of them against
SPINE.md on each run. Inline Arabic is bidi-isolated by the `ar()` helper, so a mixed line cannot
be visually reordered — the defect `CLAUDE.md` §1.3 records from the first handout.

TWO STRINGS ARE NOT FROM SPINE.md, and are flagged here rather than left to be discovered:
  · الفاروق           — عمر ؓ's لقب
  · سيف الله المسلول   — خالد ؓ's لقب
Both are alqāb the tradition gave, listed in `CLAUDE.md` §1.2. `docs/catalogue/PEOPLE.md` carries
the page-cited form of خالد ؓ's as **سيف الله** («وَسَمَّاهُ النَّبِيُّ ﷺ: سَيْفَ اللهِ», سیر ج۱ ص۳۶۶); المسلول
is the conventional fuller form.
"""
import os
import re
import sys

ROOT = r"E:/Learning/IslamicHistoryLectures"
DIR = os.path.join(ROOT, "L02_baarah_saal")
sys.path.insert(0, os.path.join(ROOT, "series"))

import pack                                            # noqa: E402


# --------------------------------------------------------------------------------- helpers

def ar(s):
    """An inline Arabic fragment inside an English cue line.

    `unicode-bidi: isolate` is the point of the wrapper: without it the bidi algorithm reorders
    the fragments around the ' · ' separators and the line comes out scrambled. Sized in em so
    the cue sheet's auto-fit can still step the whole page down. Mirrors `.ar-i` in
    `tools/render_note.py`.
    """
    return ("<span dir=\"rtl\" style=\"font-family:'Traditional Arabic',serif;font-size:1.2em;"
            "line-height:1;unicode-bidi:isolate\">%s</span>" % s)


def arname(s):
    """A name, alone on its own line — never mixed with English (CLAUDE.md §1.3)."""
    return ("<span dir=\"rtl\" style=\"font-family:'Traditional Arabic',serif;font-size:1.25em;"
            "line-height:1.1\">%s</span>" % s)


# --------------------------------------------------------------------------------- the cue sheet

CUE = {
    "session": "2",
    "title": "Two Years, Three Months",
    "dates": "11–13 AH · 632–634 CE · the whole caliphate, end to end",
    "runtime": "45 min · no Q&A",

    # The running order. Cues are fragments — a place, a name, three words of a quotation, a map
    # move, a guardrail. Never a sentence: he tells it, he does not read it.
    "run": [
        {"t": "0:00", "name": "Where we stopped", "kind": "", "cues": [
            "Line + MAP as last week left them",
            "Arabia, 11 AH"]},

        {"t": "0:04", "name": "How long was he caliph?", "kind": "hands", "cues": [
            "take the count",
            "2 years 3 months"]},

        # cards 1–5 · ABU/E-U1, E-U3, E-U4, E-U5, E-U6
        {"t": "0:05", "name": "The army sent out", "kind": "", "cues": [
            "Usāma ؓ, 18 · " + ar("لو ظننت أن السباعَ تَخْطفني") + " · the beard · 40 days"]},

        # cards 6–7 · RCT/E-RC01, E-RC02
        {"t": "0:11", "name": "Night raid, then dawn", "kind": "", "cues": [
            "Dhū Ḥusā · skins · camels bolt",
            "formed up that night · " + ar("وَكَانَ أَوَّلَ الْفَتْحِ")]},

        {"t": "0:13", "name": "How many armies at once?", "kind": "hands", "cues": [
            "Medina is one town",
            "eleven"]},

        # cards 8–9 · RCT/E-RC05, E-RC06
        {"t": "0:14", "name": "Eleven banners", "kind": "", "cues": [
            "MAP — 11 arrows · count aloud",
            "⚠ never name the ninth"]},

        # cards 10–11 · RCT/E-RC09, E-RC10
        {"t": "0:16", "name": "Buzākha, and the terms", "kind": "", "cues": [
            "Ṭulayḥa in the cloak · " + ar("فَإِنَّهُ كَذَّابٌ"),
            "ʿUmar ؓ strikes a clause"]},

        # cards 12–15 · RCT/E-RC16, E-RC18, E-RC20, E-RC21
        {"t": "0:18", "name": "ʿAqrabāʾ, then the garden", "kind": "", "cues": [
            "Thābit ؓ's shroud · al-Barāʾ ؓ over the wall · ⚠ he lived"]},

        # cards 16–18 · ABU/E-Q1, E-Q2, E-Q3
        {"t": "0:22", "name": "The reciters, and the gathering", "kind": "", "cues": [
            "parchment · shoulder-blades · palm-stalks · breasts of men"]},

        # cards 19–21 · RCT/E-RC27, E-RC36, IKO/E-IKR1
        {"t": "0:24", "name": "Dārīn, and Arabia whole", "kind": "", "cues": [
            "sea crossing · MAP 12 AH · Ibn Khaldūn ⚠ as he reads it"]},

        {"t": "0:26", "name": "WORKSHEET — 90 seconds, silent", "kind": "act", "cues": [
            "three places · three years",
            "say nothing while they write"]},

        # cards 22–23 · ISA/E-C1, E-C5
        {"t": "0:28", "name": "Into Iraq, then the desert", "kind": "", "cues": [
            "call · jizya · fight · then Qurāqir → Suwā, no road"]},

        # cards 24–25 · ISA/E-C9, E-C10
        {"t": "0:33", "name": "Yarmūk — command by turns", "kind": "", "cues": [
            ar("فلنتعاور الإمارة") + " · let me have today",
            "it lasted one day · " + ar("وإنما تكثر الجنود بالنصر")]},

        # cards 26–31 · ABD/E-B3, E-B7, E-B9, E-B11, E-B14, E-B15
        {"t": "0:36", "name": "ʿUmar ؓ named, then the end", "kind": "", "cues": [
            ar("مَا اسْتَخْلَفْتُ عَلَيْكُمْ ذَا قَرَابَةٍ") + " · worn blanket · 63"]},

        {"t": "0:40", "name": "The close", "kind": "", "cues": [
            "Line · MAP 13/11 · HANDS: what year? · lessons · did it soften him?"]},

        {"t": "0:45", "name": "Salām, then the dua", "kind": "act", "cues": []},
    ],

    # Dates only where SPINE.md gives them. Where it gives none, none is printed.
    "names": [
        (arname("أبو بكر الصدیق ؓ"),
         "Caliph 11–13 AH · two years and three months · died Monday evening, 13 AH, aged 63"),
        (arname("عمر الفاروق ؓ"),
         "In Usāma's ؓ ranks, 11 AH · named successor, 13 AH"),
        (arname("خالد بن الوليد ؓ · سيف الله المسلول"),
         "Buzākha 11 AH · al-Yamāma 11–12 AH · Iraq Muḥarram 12 AH · Syria 13 AH"),
        (arname("أسامة بن زيد ؓ"),
         "Aged 18 · marched late Rabīʿ al-Awwal 11 AH · away 40 days, some say 70"),
        (arname("زيد بن ثابت ؓ"),
         "Aged 11 when the Prophet ﷺ reached Medina · gathered the Qur'an, 12 AH"),
        (arname("ثابت بن قيس ؓ"),
         "Killed at ʿAqrabāʾ, 11–12 AH · the Anṣār's banner"),
        (arname("البراء بن مالك ؓ"),
         "Ḥadīqat al-Mawt, 11–12 AH · brother of Anas ؓ · 80-odd wounds · survived"),
        (arname("العلاء بن الحضرمي ؓ"),
         "al-Baḥrayn · Juwāthā and the crossing to Dārīn, 11–12 AH"),
        (arname("مسيلمة الكذاب"),
         "c. 40,000 fighting men · killed at al-Yamāma, 11–12 AH"),
        (arname("طليحة بن خويلد"),
         "Buzākha, 11 AH · left the field and got away to Syria"),
    ],

    # The five عبرت lines, copied from SLIDES.md §"The five عبرت lines" — which says the cue sheet
    # and the worksheet must print exactly these five, in this order. They are SPINE.md's own
    # wording, from cards 2, 8, 18, 21 and 28. Slide 59 shows the same five and nothing else.
    "lessons": [
        "There is a kind of steadiness that is not stubbornness: it is refusing to treat an "
        "emergency as permission.",
        "The whole war was set moving from one camp, in one sitting, by a man who had just been "
        "told to go home.",
        "Preservation is not one heroic act; it is somebody doing a careful, unglamorous job "
        "properly.",
        "What changed in Arabia was not how many men there were, but which way they were all "
        "facing.",
        "He kept an account of what was not his, and he closed it before he died.",
    ],
}


# --------------------------------------------------------------------------------- the worksheet

WS = {
    "session": "2",
    "title": "Two Years, Three Months",
    "dates": "11–13 AH · 632–634 CE",

    "map": "map_arabia_blank.png",
    "map_task": "Mark three places as they are named, and write the name beside each.",

    "timeline_boxes": ["11 AH", "", "", "", "", "13 AH"],
    "tl_task": "The first box and the last are filled in. Write the year into three of the four "
               "empty boxes as we reach them.",

    # The three men who carry this evening: the caliph, the field commander, and the man who
    # gathered the Qur'an. Three lines printed; pack.worksheet() rules the fourth for «ایک واقعہ».
    "people": [
        {"name": arname("أبو بكر الصدیق ؓ"),
         "dates": "Caliph 11–13 AH / 632–634 CE — two years and three months",
         "did": "The first caliph: he sent out the army the Prophet ﷺ had raised, held Arabia "
                "together when much of it broke away, and had the Qur'an gathered into one "
                "written collection."},
        {"name": arname("خالد بن الوليد ؓ · سيف الله المسلول"),
         "dates": "Buzākha 11 AH · al-Yamāma 11–12 AH · Iraq 12 AH · Syria 13 AH",
         "did": "The field commander of the ridda campaigns, and then of the march into Iraq and "
                "across five days of waterless desert into Syria."},
        {"name": arname("زيد بن ثابت ؓ"),
         "dates": "Aged eleven when the Prophet ﷺ reached Medina · the gathering, 12 AH",
         "did": "He had written the revelation down as it came; after al-Yamāma he tracked the "
                "whole Qur'an down and gathered it into one set of ṣuḥuf."},
    ],

    "lesson_lines": ["", "", "", "", ""],

    "foot": "No questions during the session. Written slips into the box at the door — "
            "I will stay fifteen minutes afterwards.",
}


# --------------------------------------------------------------------------------- build

def verify_arabic():
    """Every Arabic fragment on the cue sheet must be a verbatim slice of SPINE.md.

    CLAUDE.md §1.4: never compose Arabic; only reproduce what the source carries. These fragments
    are hand-sliced out of quoted statements, and a hand-sliced string is exactly the kind of
    thing that silently loses a letter — so it is checked, not trusted.
    """
    with open(os.path.join(DIR, "SPINE.md"), encoding="utf-8") as f:
        spine = f.read()

    frags, bad = [], []
    for b in CUE["run"]:
        for c in b.get("cues", []):
            frags += re.findall(r"unicode-bidi:isolate\">(.*?)</span>", c)
    for s in frags:
        if s not in spine:
            bad.append(s)
    if bad:
        raise SystemExit("Arabic fragments not found verbatim in SPINE.md:\n  " + "\n  ".join(bad))
    print("%-34s %2d fragments verbatim in SPINE.md" % ("arabic check", len(frags)))


def verify_lessons():
    """The five عبرت lines must be SLIDES.md's five, in SLIDES.md's order.

    They are said aloud, shown on slide 59, and written by the room on the worksheet, so a drift
    of one word between the deck and the paper is visible to everyone in it. SLIDES.md decides;
    this file follows.
    """
    path = os.path.join(DIR, "SLIDES.md")
    if not os.path.exists(path):
        print("%-34s SLIDES.md missing — lessons unverified" % "lesson check")
        return
    with open(path, encoding="utf-8") as f:
        block = f.read().split("## The five")[1].split("\n## ")[0]
    deck = [l.strip() for l in re.findall(r"^\d\. (.+)$", block, re.M)]
    mine = [" ".join(l.split()) for l in CUE["lessons"]]
    if deck != mine:
        raise SystemExit("The عبرت lines differ from SLIDES.md. SLIDES.md decides:\n  "
                         + "\n  ".join("deck: %s\n  cue : %s" % (d, m)
                                       for d, m in zip(deck, mine) if d != m))
    print("%-34s %2d lines match SLIDES.md" % ("lesson check", len(deck)))


if __name__ == "__main__":
    verify_arabic()
    verify_lessons()
    pack.cue(os.path.join(DIR, "CUE.pdf"), CUE)
    pack.worksheet(os.path.join(DIR, "WORKSHEET.pdf"), WS)
