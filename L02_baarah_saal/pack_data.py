# -*- coding: utf-8 -*-
"""Session 2 — the lectern cue sheet and the audience worksheet.

    python L02_baarah_saal/pack_data.py        # -> CUE.pdf (one page) and WORKSHEET.pdf

Everything here is read off `L02_baarah_saal/SPINE.md`, which is the single source of the running
order. SPINE.md now carries **64 cards in 7 acts** — the deliberate over-build of `DECISIONS.md`
#20, roughly seventy minutes of material for a forty-five-minute slot.

THE CUE SHEET FOLLOWS THE ★ RECOMMENDED CUT ONLY — the 27 cards SPINE.md marks ★ — not all 64.
The other 37 are read at home in `BRIEFING.pdf` and cut at the desk; whatever does not fit rolls
forward to session 3 and is never compressed. Every beat below carries its ★ SPINE card numbers in
a comment, so the deck, the briefing and this file can be checked against each other line by line.

⚠ **ACT 6 (Iraq, the waterless march, the Yarmūk) carries no ★ card at all.** That is SPINE.md's
own reading and it is deliberate: in the recommended cut the evening goes from the worksheet
straight to the deathbed, and Iraq and الشام roll forward. So there is no ACT 6 beat on this page.
`BRIEFING.md` §ACT 6 says the same thing and tells him to drop the act whole rather than gut it.

THE عبرت LINES ARE THE DECK'S, NOT THIS FILE'S. `SLIDES.md` §"The five عبرت lines" says the cue
sheet and the worksheet must print exactly its five, in its order, and slide 59 puts the same five
on screen. `CUE["lessons"]` is a copy of that list, **unchanged by the 64-card reweave — SLIDES.md's
five are still the five**; the worksheet rules five blank lines for the room to write them in. If
either list is ever edited, both change together, and `SLIDES.md` is the one that decides
(`DECISIONS.md` #26). The session title here is likewise the deck's slide-1 headline,
**Two Years, Three Months**.

WHY THE CUES LOOK STARVED. `pack.cue()` renders, counts the pages Chrome actually produced, and
refuses anything but one. The first passes of this file spilled onto a second page even at the
10pt floor, so **cues were cut, not type shrunk** — the ★ cut's 27 cards collapse into **17 beats**,
one cue line each, and the four furniture beats (bookend in, the two hands-up beats, the worksheet)
carry their cue on the name line rather than under it. It now holds one page at **11pt**.

The measured limits, if this is ever edited: the A4 landscape print box is 733px tall, the run
column is the tall one and every rendered line in it — a beat's name, and each wrapped line of its
cues — costs the same. At 11pt the column holds about 29 of them; at the 10pt floor, about 33.
A cue line holds roughly 65 characters before it wraps, so a wrapped cue costs a whole beat. The
"Names & dates" column tops out at 11pt too, so shortening cues past that point buys nothing.
The prose lives in the briefing, which he reads at home; this page only keeps his place
(`DECISIONS.md` #22).

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

import pack

# the deck is the source of truth for the five عبرت lines
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import LESSONS                                   # noqa: E402                                            # noqa: E402


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

    # The ★ running order. Cues are fragments — a place, a name, three words of a quotation, a map
    # move, a guardrail. Never a sentence: he tells it, he does not read it.
    "run": [
        # The four furniture beats carry their cue on the name line: the cue sheet is one page and
        # that is the whole of its purpose (CLAUDE.md §1.7), and folding four labels saves the four
        # lines that were holding the type down at the 10pt floor.
        {"t": "0:00", "name": "Where we stopped · Line + MAP · Arabia 11 AH", "kind": "",
         "cues": []},

        {"t": "0:04", "name": "How long was he caliph? · 2 yrs 3 months", "kind": "hands",
         "cues": []},

        # ★ cards 2, 3, 6 · ABU/E-U1, E-U3, E-U6
        {"t": "0:05", "name": "The army he would not recall", "kind": "", "cues": [
            "Usāma ؓ, 18 · " + ar("لو ظننت أن السباعَ تَخْطفني") + " · 40 days · the ring thins"]},

        # ★ card 7 · RCT/E-RC01
        {"t": "0:08", "name": "Night raid on Medina", "kind": "", "cues": [
            "Dhū Ḥusā · skins · " + ar("وَلَمْ يُصْرَعْ مُسْلِمٌ") + " · ⚠ no distance"]},

        {"t": "0:10", "name": "How many armies at once? · eleven", "kind": "hands", "cues": []},

        # ★ card 9 · RCT/E-RC05
        {"t": "0:11", "name": "Eleven banners", "kind": "", "cues": [
            "MAP — 11 arrows, count aloud · ⚠ never name the ninth"]},

        # ★ cards 11, 12, 14 · TMW/E-TRN21, RCT/E-RC09, RCT/E-RC10
        {"t": "0:13", "name": "Khālid ؓ takes the command", "kind": "", "cues": [
            ar("سَيْفٌ مِنْ سُيُوفِ اللَّهِ") + " · Waḥshī ؓ tells it",
            "the cloak · " + ar("فَإِنَّهُ كَذَّابٌ") + " · ʿUmar ؓ strikes a clause"]},

        # ★ card 15 · ZIA/E-ZY8 — ACT 3 opens
        {"t": "0:17", "name": "Four households", "kind": "", "cues": [
            "muʾākhāt · Zayd ؓ + Maʿn ؓ · both fall at al-Yamāma"]},

        # ★ cards 21, 24 · RCT/E-RC17, RCT/E-RC18
        {"t": "0:19", "name": "The rout, then the shroud", "kind": "", "cues": [
            "Mujjāʿa in irons · perfume · shins · " + ar("مَا هَكَذَا كُنَّا نُقَاتِلُ")]},

        # ★ cards 28, 31, 32 · THO/E-HS4, RCT/E-RC20, THO/E-HS16 — the pairing
        {"t": "0:21", "name": "Uḥud, then the wall", "kind": "", "cues": [
            "Anas b. al-Naḍr ؓ 80-odd KILLED · al-Barāʾ ؓ 80-odd ⚠ LIVED"]},

        # ★ cards 34, 37, 41 · AHA/E-AS16, RCT/E-RC21, ZIA/E-ZY6
        {"t": "0:23", "name": "Sālim ؓ · Musaylima · the wind", "kind": "", "cues": [
            ar("فأضجعوني بينهما") + " · ⚠ \"a second man\" · " + ar("مَا هَبَّتِ الصَّبَا")]},

        {"t": "0:26", "name": "WORKSHEET — 90 sec, silent · say nothing", "kind": "act",
         "cues": []},

        # ★ cards 42, 45, 46 · ZIA/E-ZY17, ABU/E-Q2, E-Q3
        {"t": "0:28", "name": "The reciters, and the gathering", "kind": "", "cues": [
            "⚠ NO number · parchment · shoulder-blades · palm-stalks"]},

        # ★ cards 50, 51, 52 · TMW/E-TRN14, RCT/E-RC36, IKO/E-IKR1
        {"t": "0:32", "name": "Ṭulayḥa ؓ back · Arabia whole", "kind": "", "cues": [
            "what became of him? · MAP 12 AH · Ibn Khaldūn ⚠ as he reads it"]},

        # ★ cards 60, 61, 63, 64 · ABD/E-B9, E-B11, E-B15, AHA/E-AS18
        {"t": "0:36", "name": "The end, and after", "kind": "", "cues": [
            ar("مَا اسْتَخْلَفْتُ عَلَيْكُمْ") + " · camel, blanket · 63 · then Sālim ؓ, 23 AH"]},

        {"t": "0:40", "name": "The close", "kind": "", "cues": [
            "Line · MAP 13/11 · HANDS: what year? · lessons · next week"]},

        {"t": "0:45", "name": "Salām, then the dua", "kind": "act", "cues": []},
    ],

    # The evening's principals after the reweave — four households and the men who commanded.
    # Dates only where SPINE.md gives them. Where it gives none, none is printed.
    "names": [
        (arname("أبو بكر الصدیق ؓ"),
         "Caliph 11–13 AH · 2 years 3 months · died Monday night, aged 63"),
        (arname("خالد بن الوليد ؓ · سيف الله المسلول"),
         "Uḥud right wing 3 AH · Buzākha 11 · al-Yamāma 11–12 · Iraq 12 · Syria 13"),
        (arname("أسامة بن زيد ؓ"),
         "18 · marched Rabīʿ I 11 AH · away 40 days, some say 70"),
        (arname("زيد بن الخطاب ؓ"),
         "ʿUmar ؓ's brother, Muslim before him · al-Yamāma 12 AH"),
        (arname("سالم مولى أبي حذيفة ؓ"),
         "Iṣṭakhr · imām at Qubāʾ · one of four · al-Yamāma 12 AH"),
        (arname("أبو حذيفة ؓ"),
         "Son of ʿUtba b. Rabīʿa · Badr 2 AH · al-Yamāma 12 AH"),
        (arname("ثابت بن قيس ؓ"),
         "Orator of the Anṣār · their banner · ʿAqrabāʾ 11–12 AH"),
        (arname("البراء بن مالك ؓ"),
         "The wall, 11–12 AH · Anas ؓ's brother · 80-odd · LIVED"),
        (arname("أنس بن النضر ؓ"),
         "Uḥud 3 AH · 80+ wounds · killed · known by his fingertips"),
        (arname("طليحة ؓ"),
         "Buzākha 11 AH, got away · came back to Islam"),
        (arname("مسيلمة الكذاب"),
         "c. 40,000 men · al-Yamāma 11–12 AH"),
    ],

    # The five عبرت lines, copied from SLIDES.md §"The five عبرت lines" — which says the cue sheet
    # and the worksheet must print exactly these five, in this order. They are SPINE.md's own
    # wording, from ★ cards 3, 9, 46, 52 and 60 in the 64-card order. Slide 59 shows the same five
    # and nothing else. Checked against SLIDES.md by verify_lessons() on every run.
    # Imported from build.py, never copied (CLAUDE.md §4). The deck decides the عبرت lines
    # (DECISIONS.md #26); a second hand-kept copy here diverged the moment the deck changed one.
    "lessons": LESSONS,
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

    # Three households, not three offices. The reweave put four of them on one field in ACT 3 and
    # that is what the evening is now about, so the paper carries three of the four: the master and
    # his freedman as one entry, the man who was thrown over the wall, and ʿUmar ؓ's brother.
    # Three lines printed; pack.worksheet() rules the fourth for «ایک واقعہ».
    "people": [
        {"name": arname("أبو حذيفة ؓ · سالم مولى أبي حذيفة ؓ"),
         "dates": "Badr 2 AH · both killed at al-Yamāma, 12 AH",
         "did": "Master and freed slave. Sālim ؓ came from Iṣṭakhr in Persia and led the "
                "Muhājirūn in prayer at Qubāʾ, with ʿUmar ؓ behind him, because he had the most "
                "Qur'an of them. Abū Ḥudhayfa ؓ was the son of ʿUtba b. Rabīʿa, who fell at Badr "
                "fighting the Muslims. They were killed on the same morning, and Sālim ؓ asked to "
                "be laid down between them."},
        {"name": arname("البراء بن مالك ؓ"),
         "dates": "Ḥadīqat al-Mawt, al-Yamāma, 11–12 AH · brother of Anas b. Mālik ؓ",
         "did": "Banū Ḥanīfa shut themselves inside a walled garden. He made the Muslims throw "
                "him over the wall on a shield, went down among them alone, fought his way to the "
                "gate and opened it from the inside. He came out with eighty-odd wounds and "
                "lived; Khālid b. al-Walīd ؓ stayed a month treating them."},
        {"name": arname("زيد بن الخطاب ؓ"),
         "dates": "Paired with Maʿn b. ʿAdī ؓ at the muʾākhāt · killed at al-Yamāma, 12 AH",
         "did": "ʿUmar ؓ's brother, who accepted Islam before him. Carrying a banner at al-Yamāma "
                "he told the men to bite down and go forward, and vowed not to speak again until "
                "Allah routed them or he met Allah. When the news reached ʿUmar ؓ he said: he "
                "outstripped me to the two good things."},
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


def verify_star_cut():
    """The cue sheet must cover the ★ cut exactly — every ★ card, and no card that is not ★.

    SPINE.md marks the recommended forty-five-minute cut with ★ on the card heading. Each beat
    above annotates the ★ cards it carries in a `# ★ cards …` comment; this re-reads SPINE.md and
    compares the two sets, so a card promoted into or dropped out of the ★ cut cannot pass
    unnoticed and leave the lectern sheet quietly out of step with the running order.
    """
    with open(os.path.join(DIR, "SPINE.md"), encoding="utf-8") as f:
        star = {int(n) for n in re.findall(r"^### (\d+)\. ★ ", f.read(), re.M)}
    with open(os.path.abspath(__file__), encoding="utf-8") as f:
        mine = {int(n) for line in re.findall(r"#\s*★ cards? ([\d,\s]+)·", f.read())
                for n in re.findall(r"\d+", line)}
    if star != mine:
        raise SystemExit("The cue sheet's ★ coverage differs from SPINE.md.\n"
                         "  in SPINE, not on the page: %s\n"
                         "  on the page, not ★ in SPINE: %s"
                         % (sorted(star - mine), sorted(mine - star)))
    print("%-34s %2d ★ cards covered by %d beats"
          % ("star cut", len(star), len(CUE["run"])))
    if not 16 <= len(CUE["run"]) <= 20:
        raise SystemExit("The cue sheet holds 16-20 beats. It has %d." % len(CUE["run"]))


if __name__ == "__main__":
    verify_arabic()
    verify_lessons()
    verify_star_cut()
    pack.cue(os.path.join(DIR, "CUE.pdf"), CUE)
    pack.worksheet(os.path.join(DIR, "WORKSHEET.pdf"), WS)
