# -*- coding: utf-8 -*-
"""Build L02.pptx — session 2. Abu Bakr al-Siddiq ؓ's caliphate entire, 11–13 AH / 632–634 CE.

    python L02_baarah_saal/build.py            build the deck
    python L02_baarah_saal/build.py --verify   check the Arabic against SPINE.md, build nothing

SPINE.md IS THE SOURCE, AND THIS FILE READS IT.
Every Arabic string on every slide is lifted out of `SPINE.md` at build time by `load_spine()`
and never retyped here. That is deliberate: a hand-copied Arabic string drifts by one vowel and
nobody notices until it is on a screen in front of two hundred people. SPINE.md says it is the
single source of the running order; this build takes it at its word. If a statement moves or is
re-worded there, the deck follows on the next build, and `verify()` fails loudly if a card the
deck needs has lost its statement.

REWOVEN 2026-09-10. SPINE.md now carries 64 cards, not 31: the four PEOPLE strands — the house
of Umm Sulaym ؓ (THO), Abu Hudhayfa ؓ and Salim ؓ (AHA), Zayd b. al-Khattab ؓ and the dead of
al-Yamama (ZIA), and the men who had fought against Islam (TMW) — are now inside the main
running order at the points their own research notes specify. This deck covers ALL 64.

THE OVER-BUILD IS MARKED, AND IT IS MARKED IN THE SPEAKER NOTES (DECISIONS.md #20 and #30).
SPINE.md stars 29 cards as the recommended 45-minute cut; the other 37 are the deliberate
over-build. Every slide belonging to an unstarred card carries "CUT-IF-SHORT" as the FIRST LINE
of its speaker note, and the build prints the full list of cuttable slide numbers when it
finishes. The marker is NOT on the slide face: DECISIONS.md #30 makes a slide face carry only
what the room may see, deck2 enforces it, and a build marker on a projector in front of two
hundred people is exactly the failure that rule exists to stop. Nothing is dropped here — this
file builds the whole pool and Daniyal deletes at the desk.

Where a quotation is too long to sit on one slide, the deck shows a CONTIGUOUS CLIP of it —
`_upto()` and `_after()` slice the string, they never edit it — and the clip is checked back
against SPINE.md like everything else. The English renderings below are ours: they are trimmed
from SPINE's own renderings so the block fits above the citation strip, and they carry no Arabic
script inline, because Arabic and Latin in one line is what mangled the first speaker scripts
(CLAUDE.md §1.3).

LANGUAGE (DECISIONS.md #19). English carries every slide. No generated Urdu anywhere. Arabic
appears only as verbatim source quotation, in Naskh, with an English rendering beneath it.
Citations are given in Latin transliteration with Latin digits — an Arabic book title sharing a
line with "vol. 7, p. 10" is exactly the bidi reordering bug CLAUDE.md §1.3 warns about.

LAYOUT NOTE. deck2's statement layout estimates the Arabic block's height, then places the
English beneath it and the citation at a fixed strip. A quotation past about 156 rendered
characters pushes the English into the citation, so `stmt()` drops the title bar for those slides
and lets the quotation carry the slide on its own — that is deck2's second statement layout, not
a workaround.

MAPS are not Gemini's job. The nine map files and the two Line strips named here are built by
`series/make_visuals.py` and all eleven already exist. The seven IMAGE BRIEFs are Gemini's, and
each one is non-figurative by design: no depiction of the Prophet ﷺ, of a Companion, or of any
identifiable face, ever — landscape, architecture, objects, texture, light only.
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(ROOT, "series"))

import deck2 as D  # noqa: E402

SPINE_PATH = os.path.join(HERE, "SPINE.md")
OUT = os.path.join(HERE, "L02.pptx")
BRIEFS = os.path.join(HERE, "IMAGE_BRIEFS.md")


# ============================================================================ SPINE.md
def load_spine():
    """Pull every card's verbatim Arabic statement out of SPINE.md, keyed by card number.

    Some cards wrap their statement in `<div dir="rtl">…</div>` for the markdown renderer, and a
    few put the saying inside straight quotes. The wrapper is stripped; the Arabic inside it is
    untouched, and what is kept is still a literal contiguous substring of the file, which is
    what `verify()` checks.
    """
    raw = io.open(SPINE_PATH, encoding="utf-8").read()
    lines = raw.split("\n")
    ar, cur = {}, None
    for i, ln in enumerate(lines):
        m = re.match(r"^### (\d+)\. ", ln)
        if m:
            cur = int(m.group(1))
        if ln.strip() == "**The statement:**" and cur is not None:
            block = []
            j = i + 1
            while j < len(lines) and lines[j].startswith(">"):
                body = lines[j][1:].strip()
                if body.startswith("—"):          # the em-dash citation line ends it
                    break
                block.append(body)
                j += 1
            if block:
                s = " ".join(block)
                s = re.sub(r'^<div dir="rtl">', "", s)
                s = re.sub(r"</div>$", "", s)
                ar[cur] = s.strip().strip('"').strip()
    return raw, ar


SPINE_RAW, AR = load_spine()


# --------------------------------------------------------------------------- contiguous clips
# These slice. They never edit a character, never re-order and never re-vowel, so the result stays
# a literal substring of SPINE.md and `verify()` can prove it. The anchors are punctuation counts
# rather than hand-typed Arabic wherever possible, so that no Arabic is retyped in this file.

def _upto(s, mark, k=1):
    """The prefix of `s` through the k-th occurrence of `mark`."""
    i = -1
    for _ in range(k):
        i = s.index(mark, i + 1)
    return s[:i + len(mark)]


def _after(s, mark, k=1):
    """Everything in `s` after the k-th occurrence of `mark`."""
    i = -1
    for _ in range(k):
        i = s.index(mark, i + 1)
    return s[i + len(mark):]


def clip(n, after=None, upto=None):
    """A contiguous slice of card n's statement. Slices only — never edits a character."""
    s = AR[n]
    if after:
        s = _after(s, after)
    if upto:
        s = _upto(s, upto)
    return s.strip()


# Card 17 runs to 296 rendered characters — two slides' worth. The deck shows the answer, which
# is the point of the card; the scene that leads into it is spoken, not printed. The reporting
# verb is dropped with it, so the slide opens on the words themselves rather than on a colon.
AR17 = _upto(_after(_after(AR[17], "؟. "), ": "), "،", 3).rstrip("، ")

# Card 19 carries the Siyar editor's inline page break in the middle of the sentence. The deck
# shows the clause before it and the rest is spoken.
AR19 = _upto(AR[19], "،", 2).rstrip("، ")

# Card 53's statement carries a "jalla jalaluhu" ligature that Traditional Arabic has no glyph
# for, and the Siyar editor's square-bracketed insertion, which the bidi algorithm mirrors into
# nonsense beside Latin punctuation. Both sit outside the clause the card exists for — the two
# restrictions — so the slide carries that clause and the rest is spoken.
AR53 = _after(AR[53], "،", 2).strip().rsplit(" ", 5)[0]

# Cards 22 and 26 close on the U+FD41 "radiya Allahu anhu" ligature, which NEITHER Traditional
# Arabic NOR Arabic Typesetting has a glyph for — it projects as an empty box. Both statements
# are complete without it, so the slide drops the final token and the honorific is spoken.
AR22 = AR[22].rsplit(" ", 1)[0]
AR26 = AR[26].rsplit(" ", 1)[0]

# Card 51's statement runs to 339 characters — three slides' worth. The deck shows the clause
# that is the point of it, exactly as printed, and the briefing carries the whole passage.
AR51 = clip(51, after="… ", upto="ولله الحمد.")


# ============================================================================ the running order
# SPINE.md's ★ — the 27 cards of the recommended 45-minute cut. Everything else is the
# deliberate over-build (DECISIONS.md #20) and is marked as cuttable in its speaker note.
STAR = {2, 3, 6, 7, 9, 11, 12, 14, 15, 21, 24, 28, 31, 32, 34, 37, 41, 42, 45, 46,
        50, 51, 52, 53, 56, 60, 61, 63, 64}

WHEN = {
    1:  "Shawwal 3 AH",                     2:  "11 AH",
    3:  "Rabi' al-Awwal 11 AH",             4:  "Rabi' al-Awwal 11 AH",
    5:  "late Rabi' al-Awwal 11 AH",        6:  "11 AH",
    7:  "11 AH",                            8:  "11 AH, the same night",
    9:  "11 AH",                            10: "11 AH",
    11: "11 AH",                            12: "11 AH",
    13: "11 AH",                            14: "11 AH, after Buzakha",
    15: "al-Yamama, 12 AH",                 16: "before Dar al-Arqam",
    17: "2 AH, after Badr",                 18: "before the hijra",
    19: "before the Prophet ﷺ reached Medina",
    20: "11–12 AH",                         21: "at Aqraba'",
    22: "al-Yamama, 12 AH",                 23: "Medina, after Surat al-Hujurat",
    24: "at Aqraba'",                       25: "al-Yamama, 12 AH",
    26: "al-Yamama, 12 AH",                 27: "al-Yamama, then Medina",
    28: "Uhud",                             29: "Uhud",
    30: "Medina or Basra, undated",         31: "Hadiqat al-Mawt",
    32: "Hadiqat al-Mawt",                  33: "al-Yamama, 12 AH",
    34: "al-Yamama, 12 AH",                 35: "after al-Yamama, 12 AH",
    36: "11 AH → 12 AH",                    37: "11–12 AH",
    38: "al-Yamama, 12 AH",                 39: "al-Yamama, 12 AH",
    40: "Medina, 12 AH",                    41: "the years after 12 AH",
    42: "12 AH, after the battle",          43: "al-Yamama, 11–12 AH",
    44: "the Prophet's ﷺ lifetime",         45: "12 AH",
    46: "12 AH",                            47: "11–12 AH",
    48: "11 AH",                            49: "his later life",
    50: "the end of the caliphate, or just after",
    51: "11 AH → 12 AH",                    52: "framing, not narrative",
    53: "Muharram 12 AH",                   54: "13 AH",
    55: "13 AH",                            56: "the morning of the Yarmuk",
    57: "the Yarmuk, 13 AH",                58: "the last days",
    59: "the last days",                    60: "the last day",
    61: "the last days",                    62: "the last hours",
    63: "13 AH",                            64: "23 AH, Medina",
}

CUT_HEAD = ("CUT-IF-SHORT — card %d is NOT in SPINE.md's starred 29-card cut. Delete this "
            "slide first when the evening is running long; nothing later depends on it.\n\n")

CUT_SLIDES = []                 # 1-based slide numbers of the over-build, printed on save
TALLY = {"star": 0, "cut": 0}


CAPTION_CHARS = 74      # one line of 24pt Segoe UI across the content width, and no more
KEY_CHARS = 20          # one line of 28pt Georgia bold in deck2's key column, and no more


def keys(*rows):
    """Map key lines, checked against the column deck2 actually gives them.

    deck2's key column is about 4.3 inches wide, which is roughly 24 characters of 24pt body
    text and 20 of 28pt bold label. It caps a key's sub-line at EIGHT WORDS, and eight words do
    not fit: a wrapped sub-line runs straight into the label under it, which is what made the
    Buzakha and Usama keys unreadable. So the cap here is characters, not words, and it depends
    on how many keys share the column — five keys leave one line each, four leave two.
    """
    sub_cap = 24 if len(rows) >= 5 else 46
    for label, sub in rows:
        if len(label) > KEY_CHARS:
            raise SystemExit("map key label is %d characters, the cap is %d: %r"
                             % (len(label), KEY_CHARS, label))
        if len(sub) > sub_cap:
            raise SystemExit("map key sub-line is %d characters; with %d keys the cap is %d, or "
                             "it wraps onto the key below it: %r"
                             % (len(sub), len(rows), sub_cap, sub))
    return list(rows)


def cap(s):
    """A caption, checked against the one line deck2 gives it.

    deck2's caption box is a single 24pt line at the foot of the slide. A caption that wraps
    puts its second line off the bottom edge of the slide, where it is invisible in PowerPoint
    and clipped in the PDF — which is exactly the kind of defect a glance at the preview is
    supposed to catch, so it is caught here instead.
    """
    if len(s) > CAPTION_CHARS:
        raise SystemExit("caption is %d characters, the cap is %d — it will wrap off the "
                         "bottom of the slide: %r" % (len(s), CAPTION_CHARS, s))
    return s


def kicker(n):
    """The kicker line for a card's slide — card number and date, and nothing else.

    The CUT-IF-SHORT marker is deliberately NOT here. DECISIONS.md #30 makes a slide face carry
    only what the room may see, and deck2's audit fails the build on a build marker in any text
    box. The marker goes in the speaker note instead — see `mark()`.
    """
    # The SPINE card number is OUR index, not the room's. It belongs in the speaker
    # note with the CUT-IF-SHORT marker, never on the face (DECISIONS.md #30).
    return WHEN[n] or None


def mark(prs, n, s, say=None):
    """Tally the slide, and write its speaker note with the CUT-IF-SHORT head where it belongs."""
    body = say or ""
    if n in STAR:
        TALLY["star"] += 1
    else:
        TALLY["cut"] += 1
        CUT_SLIDES.append(len(prs.slides._sldIdLst))
        body = (CUT_HEAD % n) + body
    if body:
        D.note(s, body)
    return s


def verify():
    """Every Arabic string that reaches a slide must be a literal substring of SPINE.md."""
    needed = [n for n in range(1, 65) if n != 32]     # card 32's quotation is card 31's, once
    missing = [n for n in needed if n not in AR]
    if missing:
        raise SystemExit("SPINE.md has no statement for card(s): %s" % missing)
    # A statement that wraps across several blockquote lines is stored here as one string, so
    # the file is flattened the same way before the comparison. Nothing else is touched.
    flat = re.sub(r"\n>\s*", " ", SPINE_RAW)
    clipped = (17, 19, 22, 26, 51, 53)
    on_slides = ([AR[n] for n in needed if n not in clipped]
                 + [AR17, AR19, AR22, AR26, AR51, AR53])
    bad = [s for s in on_slides if s not in flat]
    if bad:
        raise SystemExit("%d Arabic string(s) are not literal substrings of SPINE.md — the deck "
                         "has drifted from the source:\n%s" % (len(bad), bad[0][:80]))
    print("verify: %d Arabic statements, all literal substrings of SPINE.md" % len(on_slides))
    return True


# ============================================================================ citations
# Latin transliteration, Latin digits. Printed pages exactly as SPINE.md gives them.
BID = "al-Bidaya wa-l-Nihaya, vol. %s, p. %s"
KAM = "al-Kamil fi al-Tarikh, vol. 2, p. %s"
SIY = "Siyar A'lam al-Nubala', vol. %s, p. %s"
RAS = "Siyar A'lam al-Nubala' (al-Khulafa' al-Rashidun), p. %s"

CITE = {
    1:  BID % (4, 180),
    2:  BID % (5, 311),
    3:  BID % (7, 10),
    4:  KAM % 195,
    5:  BID % (7, 11),
    6:  BID % (7, 11),
    7:  KAM % 202,
    8:  KAM % 203,
    9:  KAM % 204,
    10: BID % (7, 24),
    11: BID % (7, 24),
    12: KAM % 205,
    13: RAS % 41,
    14: BID % (7, 27) + "  ·  Sahih al-Bukhari 7221",
    15: BID % (7, 49),
    16: SIY % (1, 164),
    17: "Siyar A'lam al-Nubala' (al-Sira al-Nabawiyya), p. 312",
    18: SIY % (1, 167),
    19: "Siyar A'lam al-Nubala', vol. 1, pp. 168–169",
    20: BID % (7, 33),
    21: BID % (7, 33),
    22: BID % (7, 34),
    23: SIY % (1, 310),
    24: SIY % (1, 311) + "  ·  Sahih al-Bukhari 2845",
    25: BID % (7, 34),
    26: BID % (7, 34),
    27: BID % (7, 48),
    28: BID % (4, 203),
    29: BID % (4, 203) + "  ·  Siyar (al-Sira al-Nabawiyya), vol. 1, p. 407",
    30: SIY % (1, 198),
    31: KAM % 218,
    33: RAS % 60,
    34: BID % (7, 50),
    35: SIY % (1, 169),
    36: BID % (3, 428),
    37: RAS % 48,
    38: BID % (4, 185),
    39: RAS % 48,
    40: BID % (7, 49),
    41: SIY % (1, 298),
    42: BID % (7, 79) + "  ·  Sahih al-Bukhari 4986",
    43: BID % (7, 35),
    44: BID % (7, 50),
    45: SIY % (2, 431),
    46: SIY % (2, 431),
    47: KAM % 224,
    48: BID % (7, 41),
    49: BID % (7, 127),
    50: BID % (7, 242),
    51: BID % (7, 43),
    52: "Ibn Khaldun · Tarikh Ibn Khaldun, vol. 1, p. 198 — as he reads it",
    53: BID % (7, 62),
    54: SIY % (1, 329),
    55: KAM % 253,
    56: BID % (7, 89),
    57: BID % (7, 92),
    58: KAM % 266,
    59: KAM % 267,
    60: RAS % 19,
    61: KAM % 266,
    62: KAM % 262,
    63: RAS % 19,
    64: BID % (7, 50),
}

# ============================================================================ renderings
# Trimmed from SPINE.md's own English renderings so the block clears the citation strip.
# Names transliterated: Arabic script never shares a line with Latin (CLAUDE.md §1.3).
EN = {
    1:  "They put Khalid b. al-Walid over the right wing of the cavalry, and Ikrima b. Abi Jahl "
        "b. Hisham over its left.",
    2:  "If you find fault with his command, you found fault with his father's command before "
        "him — and this one is among the dearest of people to me after him.",
    3:  "By Him in whose hand is Abu Bakr's soul — if I thought the wild beasts would snatch "
        "me away, I would still send out Usama's expedition.",
    4:  "May your mother lose you, son of al-Khattab! The Messenger of Allah ﷺ appointed him "
        "— and you order me to depose him?",
    5:  "Usama said: O successor of the Messenger of Allah, either you ride or I dismount. He "
        "said: By Allah, you shall not dismount, and I shall not ride.",
    6:  "He passed no tribe intending to break away but they said: were it not that these people "
        "have strength, men like these would not have gone out from among them.",
    7:  "The reserve came out at them with skins they had inflated … the Muslims' camels "
        "bolted with them on their backs and carried them back to Medina — and not one "
        "Muslim was thrown.",
    8:  "Dawn did not break until they and the enemy were on one ground … and the sun's rim "
        "had not risen before they turned their backs … and that was the first victory.",
    9:  "The commanders separated from Dhu al-Qassa, and each commander's troops joined him, and "
        "he gave each commander his commission.",
    10: "I have ordered my messenger to read his letter in every assembly of yours. The summons "
        "is the adhan: when they call it, hold off from them; if they do not, ask them what they "
        "owe.",
    11: "What an excellent servant of Allah and brother of the clan — Khalid b. al-Walid; a "
        "sword among the swords of Allah, drawn against the disbelievers and the hypocrites.",
    12: "He said to me: you have a mill like his mill, and a matter you will not forget. Uyayna "
        "said: Allah knows there will be a matter you will not forget. Withdraw, Banu Fazara "
        "— the man is a liar.",
    13: "Not one of us but would rather his companion died first — and we meet a people who "
        "would each rather die before his companion.",
    14: "Umar ؓ said: as for your saying, and you pay blood-money for our dead — our "
        "dead were killed upon the command of Allah; there is no blood-money for them.",
    15: "The Messenger of Allah ﷺ made him and Ma'n b. Adi al-Ansari brothers, and the two of "
        "them were killed together at al-Yamama.",
    16: "The great chief, the martyr, Abu Hudhayfa — son of the elder of the Jahiliyya, Utba "
        "b. Rabi'a — al-Qurashi, al-Abshami, the man of Badr.",
    17: "No, by Allah, I have not doubted my father nor where he fell. But I knew in him a "
        "judgement and a forbearance, and I used to hope he would accept Islam.",
    18: "Of the first forerunners, of the men of Badr, of those brought near, of the learned "
        "… his origin is from Istakhr.",
    19: "The Muhajirun camped at al-Usba beside Quba', and Salim, the freedman of Abu Hudhayfa, "
        "led them in prayer.",
    20: "Man — if you intend anything tomorrow for the people of Yamama, good or ill, keep "
        "this man alive … so Khalid kept him, in irons, and said: treat him well.",
    21: "Banu Hanifa entered Khalid b. al-Walid's own tent, minded to kill Umm Tamim — until "
        "Mujja'a gave her his protection.",
    22: "Bite down on your back teeth, strike into your enemy and go forward. By Allah, I will "
        "not speak until Allah routs them.",
    23: "He said: Thabit — are you not content to live praised, to be killed a martyr, and to "
        "enter the Garden?",
    24: "Get out of our faces so we can strike the enemy. Wretched is what you have accustomed "
        "your opponents to! This is not how we used to fight alongside the Messenger of Allah "
        "ﷺ.",
    25: "The Muhajirun said to Salim, the freedman of Abu Hudhayfa: do you fear we shall be "
        "broken from your side? He said: a wretched bearer of the Qur'an I should be, then.",
    26: "Abu Hudhayfa said: people of the Qur'an — adorn the Qur'an with deeds. And he charged "
        "into them until he drove them back, and he was struck down ؓ.",
    27: "And Abu Bakr executed his will after his death. And we know of no one else whose will "
        "was carried through after his death except Thabit b. Qays b. Shammas.",
    28: "Abu Amr, where to? Ah, the scent of Paradise — I find it this side of Uhud.",
    29: "Among the believers are men true to what they pledged to Allah.",
    30: "Do you see me dying in my bed? By Allah, I have killed ninety-odd.",
    31: "Company of Muslims — throw me over onto them into the garden. They said: we will "
        "not. He said: By Allah, you will throw me onto them in it!",
    33: "An arrow struck him on the day of al-Yamama and he pulled it out, bound himself up, "
        "took his sword and fought until he was killed — and many wounds were found on him.",
    34: "When he was struck down he said: what has become of Abu Hudhayfa? They said: he has "
        "been killed. He said: then lay me down between the two of them.",
    35: "And it is said: Salim was found, he and his patron Abu Hudhayfa, the head of one of "
        "them at the feet of the other, both struck down ؓ.",
    36: "Then he would say: do you testify that I am the Messenger of Allah? And he would say: "
        "I do not hear. So he began to cut him apart limb by limb until he died in his hands.",
    37: "From Wahshi: I never saw men more steadfast in the face of death than Musaylima's "
        "companions — then he mentioned that he had a share in killing Musaylima.",
    38: "Your Lord knows best which of us killed him. If I killed him, then I have killed the "
        "best of men after the Messenger of Allah ﷺ, and I have killed the worst of men.",
    39: "I have never seen anyone more steadfast in the face of death than Musaylima's men.",
    40: "When the killing of Zayd b. al-Khattab reached Umar he said: he outstripped me to the "
        "two good things — he accepted Islam before me, and he was martyred before me.",
    41: "He used to say: the east wind never blows but I find in it the scent of Zayd.",
    42: "…and that was after the killing had run hot among the reciters on the day of "
        "al-Yamama, as the hadith in Sahih al-Bukhari establishes.",
    43: "Six hundred of the Muslims were killed — and it is said five hundred — and "
        "Allah knows best. Among them were leaders of the Companions and men of standing.",
    44: "And he is one of the four of whom the Messenger of Allah ﷺ said: take the Qur'an from "
        "four — and he mentioned Salim, the freedman of Abu Hudhayfa, among them.",
    45: "I said: how will you do a thing the Messenger of Allah ﷺ did not do? He said: by "
        "Allah, it is good. And he did not stop coming back to me until Allah opened my breast.",
    46: "So I began to track down the Qur'an, gathering it from the parchments, the "
        "shoulder-blades, the palm-stalks, and the breasts of men.",
    47: "Allah has shown you of His signs on land so that you may take heed of them at sea. Rise "
        "against your enemy, and go straight across the sea.",
    48: "al-Siddiq wrote blaming him for his haste, and said: let me not see you, and let me not "
        "hear of you, except after you have proved yourself.",
    49: "He used to kiss the mushaf and weep and say: my Lord's speech, my Lord's speech … "
        "and it is said that no sin is known of him after he accepted Islam.",
    50: "Get away from me — you are the killer of the two righteous men. Allah honoured "
        "them at my hands.",
    51: "And matters continued so until there remained in the peninsula none but people obedient "
        "to Allah and His Messenger, and people under al-Siddiq's protection.",
    52: "The religious colouring takes away the rivalry and envy that are in people of asabiyya, "
        "and makes their direction one.",
    # Two lines, not three: this quotation is long enough to drop the title bar, and a third
    # line of English pushes the block down into the citation strip.
    53: "And he ordered him not to compel any man to march with him, and not to use any man "
        "who had apostatised.",
    54: "Abu Bakr tied his standard for him and walked beside him under his stirrup, seeing him "
        "off and instructing him — and that was only for his standing.",
    55: "By God, I have come to this water only once in my life — with my father, when I "
        "was a boy.",
    56: "Let us take the command in turn — one of us today, another tomorrow — and let "
        "me have today.",
    57: "Woe to you — are you frightening me with the Romans? Armies are made many by "
        "victory and few by abandonment, not by the number of men.",
    58: "He is better than your opinion of him — except that there is harshness in him. Abu "
        "Bakr said: that is because he sees me being gentle.",
    59: "Are you content with the one I have appointed over you? For I have not appointed over "
        "you a relative of mine. I have appointed Umar over you.",
    60: "We have nothing of the Muslims' fay' except this Abyssinian servant, this "
        "water-carrying camel, and the worn nap of this blanket.",
    61: "When death came to him he directed that land of his be sold and its price paid over in "
        "compensation for what he had taken of the Muslims' property.",
    62: "He said: the living have more need of the new than the dead — this is only for the "
        "decay.",
    63: "A'isha ؓ said: he died on the night of Tuesday, and was buried before morning came.",
    64: "And it is related of Umar that he said, when death was upon him: had Salim been alive "
        "I would not have made it a shura.",
}

# ============================================================================ the five عبرت
# Drawn from the acts themselves, in SPINE.md's own words. No present-day parallel, ever.
# The cue sheet and the worksheet must print exactly these five, in this order.
#
# CHANGED 2026-09-10, one line of five. The old fourth line was Ibn Khaldun's (card 52, "What
# changed in Arabia was not how many men there were, but which way they were all facing"). It is
# out, and card 15's line is in, for two reasons: DECISIONS.md #29 admits Ibn Khaldun for framing
# only, and an عبرت is the evening's own conclusion drawn from an event, not a borrowed
# judgement; and the rewoven ACT 3 is now 27 of the 64 cards and had no line of its own. Card 52
# keeps its slide and speaks its عبرت from the platform.
LESSONS = [
    "There is a kind of steadiness that is not stubbornness: it is refusing to treat an "
    "emergency as permission.",
    "The whole war was set moving from one camp, in one sitting, by a man who had just been "
    "told to go home.",
    "The tie was made in a year when they owned nothing, and it was still holding on the day "
    "they died.",
    "Preservation is not one heroic act; it is somebody doing a careful, unglamorous job "
    "properly.",
    "He kept an account of what was not his, and he closed it before he died.",
]


# ============================================================================ helper
LONG_AR = 156      # past this, the Arabic block pushes the English into the citation strip


def stmt(prs, n, headline=None, english=None, arabic=None, cite=None, say=None):
    """A statement slide from card n. A long quotation drops the title bar and carries itself."""
    ar = AR[n] if arabic is None else arabic
    k = kicker(n)
    if D._ar_len(ar) > LONG_AR:
        headline, k = None, None
    s = D.statement_slide(prs, english=english or EN[n], arabic=ar, cite=cite or CITE[n],
                          headline=headline, kicker=k)
    return mark(prs, n, s, say)


# ============================================================================ the deck
def build():
    prs = D.deck()

    # ---------------------------------------------------------------- 1  title
    D.title_slide(prs, "Two Years, Three Months", "11–13 AH  ·  632–634 CE",
                  "Session Two  ·  Abu Bakr al-Siddiq ؓ")

    # ---------------------------------------------------------------- 2-3  bookend IN
    s = D.timeline_slide(prs, "line_s1.png", "Where we stopped last week",
                         caption=cap("The whole line. Tonight is the first two years of it."),
                         kicker="Bookend in")
    D.note(s, "[BOOKEND IN] This is session 1's closing Line, unchanged. Do not explain it — "
              "let them recognise it. 'We came from here.'")

    s = D.map_slide(prs, "map_s2_open_11ah.png", "Arabia, the morning after",
                    kicker="11 AH",
                    keys=keys(("Medina", "the capital, and one field army"),
                          ("The tribes around it", "some broken away, some refusing the zakat"),
                          ("The army", "raised for the Syrian frontier, not yet gone"),
                          ("Byzantine ground", "north-west, well past Tabuk")))
    D.note(s, "[BOOKEND IN] Session 1's closing Map, unchanged. Where the room walked in.")

    # ================================================================ ACT 1
    D.section_slide(prs, "The army he would not call back",
                    "Act One  ·  11 AH  ·  the first ten days")

    s = D.statement_slide(prs, english="Two years and three months.",
                          headline="How long was he caliph?", size=54)
    D.note(s, "[HANDS 1] Ask it, take the show of hands, take two guesses, THEN advance. "
              "Everything tonight happens inside that span.")

    s = D.diagram_slide(prs, "The order of battle at Uhud", kicker=kicker(1),
                        rows=[("The right wing", "Khalid b. al-Walid, over the cavalry"),
                              ("The left wing", "Ikrima, the son of Abu Jahl"),
                              ("The army", "Abu Sufyan b. Harb, over all of it")],
                        caption=cap("All three of them command for Islam before the year 23."))
    mark(prs, 1, s,
         "[HANDS] Before naming them: who commanded the Meccan army at Uhud? Let the room "
         "answer, then give all three names. This card is the frame the whole 'men who had "
         "fought against it' strand hangs on — a man's place in one line of battle is not his "
         "place in the next.")

    stmt(prs, 1, headline="The two wings at Uhud",
         say="Ibn Ishaq records exactly who led that cavalry. Three thousand men, two hundred "
             "horses. Read the names off the page and stop there.")

    s = D.map_slide(prs, "map_s2_usama.png", "An army pointed north", kicker=kicker(2),
                    keys=keys(("Medina", "the army is raised here"),
                          ("Usama b. Zayd ؓ", "eighteen, and in command"),
                          ("al-Jurf", "the camp one march out"),
                          ("Dhu Khushub", "on the road north"),
                          ("Ubna, in the Balqa'", "Byzantine ground")))
    mark(prs, 2, s,
         "The first time the map points at Byzantine ground. In the ranks under an "
         "eighteen-year-old: Umar b. al-Khattab ؓ and the senior Muhajirun and Ansar. People "
         "said so out loud.")

    stmt(prs, 2, headline="The Prophet ﷺ answered them himself",
         say="He heard the objection, stood up, and answered it. His father is Zayd b. Haritha "
             "ؓ, who had commanded before him. Ask the room first: how old do you have to be "
             "before people will take an order from you?")

    stmt(prs, 3, headline="Do you call the army back?",
         say="[HANDS] Ask before you tell it: the capital is surrounded and your only army is "
             "marching away — do you call it back? Take the hands. Among those who advised "
             "recall: Umar b. al-Khattab ؓ. Then read the line.")

    stmt(prs, 4, headline="And you order me to depose him?",
         say="The Ansar's second request was not 'cancel the march' but 'give us an older "
             "commander'. Umar ؓ carried the message. He took him by the beard.")

    s = D.image_slide(prs, "l02_walk_out.png", "The caliph on foot", kicker=kicker(5),
                      caption=cap("He walked. The commander rode. His own beast was led behind, empty."),
                      brief="Restrained editorial illustration in muted ochre, bone and deep "
                            "teal. A wide dusty caravan track leaving a walled palm oasis at "
                            "first light, seen from ground level. Deep camel prints and bare "
                            "human footprints pressed side by side into the dust and running "
                            "away down the track. At the right edge, a saddled riderless camel "
                            "standing with its lead-rope hanging loose. Low raking dawn light, "
                            "long shadows, fine airborne dust, distant low hills. Absolutely no "
                            "people, no faces, no human figures anywhere in the image. 16:9 "
                            "landscape.")
    mark(prs, 5, s,
         "Only at the end did he ask a favour — and he asked it of Usama ؓ, because Usama ؓ "
         "was the commander and Umar ؓ was in his army: would you release Umar to me?")

    stmt(prs, 5, headline="Either you ride or I dismount")

    stmt(prs, 6, headline="Forty days, and what the tribes concluded",
         say="Marched late Rabi' al-Awwal 11 AH. Away forty days — some say seventy. It did "
             "not fight its way through; it simply passed. The books differ on the target: Ubna "
             "in the Balqa', or Quda'a clans, or a clash with Roman forces — say so. The "
             "month of the return is our arithmetic, not a dated report on any page read.")

    # ================================================================ ACT 2
    D.section_slide(prs, "Arabia comes apart", "Act Two  ·  11 AH")

    stmt(prs, 7, headline="The first engagement was a setback",
         say="[HANDS] Before telling it: a delegation comes to negotiate and goes home again "
             "— what have they taken with them besides your answer? They counted the men. "
             "Three days later the raid came at night. Half stayed back at Dhu Husa as a "
             "reserve. Say the setback plainly; the book does.")

    stmt(prs, 8, headline="That was the first victory",
         say="Same night as the reverse. The three brothers of Muqarrin on the right, the left "
             "and the rear. Marched in the dark. Camped at Dhu al-Qassa and left al-Nu'man b. "
             "Muqarrin ؓ there with a detachment.")

    s = D.map_slide(prs, "map_s2_ridda_eleven.png", "Eleven banners at Dhu al-Qassa",
                    kicker=kicker(9),
                    keys=keys(("Dhu al-Qassa", "one day's ride out"),
                          ("Eleven commanders", "each with written orders"),
                          ("North and east", "Najd, Yamama, Sham"),
                          ("East and south-east", "Bahrayn, Uman, Mahra"),
                          ("South", "Yemen, Tihama, Hadramawt")))
    mark(prs, 9, s,
         "[HANDS 2] Ask BEFORE this slide: Medina is one town — how many armies would you "
         "send out at once? Take the guesses, then show eleven arrows and count them with the "
         "room. He rode out a third time with his sword drawn and Ali ؓ at his camel's head; "
         "this time they would not let him go on. He tied the banners on that ground and went "
         "home. NOTE: Ibn Kathir announces eleven and prints ten; al-Kamil prints all eleven. "
         "Do NOT name the ninth commander — three sources give three forms of it. This is the "
         "biggest map moment of the evening.")

    stmt(prs, 9, headline="Eleven directions from one camp",
         say="Each commander's own troops came up and joined him on that ground, and then they "
             "separated. One camp, one sitting, eleven directions.")

    s = D.image_slide(prs, "l02_letter.png", "The letter went ahead of the armies",
                      kicker=kicker(10),
                      caption=cap("One wording, copied many times, carried ahead of the columns."),
                      brief="Restrained editorial still life in muted ochre, bone and deep teal. "
                            "A single sheet of aged parchment lying open on a plain scrubbed "
                            "wooden board, its writing suggested only as soft illegible strokes "
                            "— never readable letters of any script. Beside it a cut reed "
                            "pen and a small dark unglazed ink vessel; to one side a neat stack "
                            "of several identical folded and sealed letters waiting to be "
                            "carried. Soft directional daylight from one side, quiet shadows. No "
                            "people, no hands, no faces. 16:9 landscape.")
    mark(prs, 10, s,
         "The messenger was to read it aloud in every assembly of the tribe. CAUTION: the same "
         "letter carries a harsh clause. Do not quote it and do not deny it. If raised: it is "
         "on that page, transmitted by Sayf b. Umar; the operative test on the same page is the "
         "adhan; and the question is for the fuqaha'.")

    stmt(prs, 10, headline="The letter set one test",
         say="A test any man could apply from a distance — no lawyer, no court. Call the "
             "adhan when you halt. If they answer it, stop.")

    stmt(prs, 11, headline="A sword among the swords of Allah",
         say="Abu Bakr ؓ quoted this when he gave Khalid ؓ the ridda command. The man who "
             "transmits it is Wahshi b. Harb ؓ — twelve years earlier the two of them had "
             "been on the same side of the field at Uhud, and it was the other side. GRADING: "
             "say only 'Imam Ahmad records it'. The matn is graded hasan/sahih by its routes; "
             "this particular chain, through Harb b. Wahshi, is weak. Assert no grade from the "
             "platform.")

    s = D.map_slide(prs, "map_s2_buzakha.png", "Buzakha", kicker=kicker(12),
                    keys=keys(("Aja' and Salma", "Khalid ؓ starts here"),
                          ("Sumayra'", "Tulayha moves up"),
                          ("Buzakha", "Asad, Ghatafan, Fazara"),
                          ("Banu Amir", "armed nearby, watching"),
                          ("Then to al-Sham", "Tulayha's line of flight")))
    mark(prs, 12, s,
         "Tulayha sat wrapped in a cloak waiting for revelation while Uyayna b. Hisn did the "
         "fighting. Three times Uyayna broke off, walked back to the cloak, and asked whether "
         "Jibril had come.")

    stmt(prs, 12, headline="The man who walked off the field",
         say="[HANDS] Before telling it: he had followed this man, and was fighting for him that "
             "morning — what was the question that ended it? Tulayha's own exit is on the "
             "same page: a horse ready, a mount for his wife, and a line called back over his "
             "shoulder. Keep him alive in the room — he comes back in Act Five.")

    stmt(prs, 13, headline="What is defeating you?",
         say="[HANDS] Ask 'why did the ridda armies lose?' — take two or three answers, then "
             "read this. Tulayha asked one of his own men, and this is the answer he got. The "
             "difference was not in the numbers, and the losing side could see it.")

    stmt(prs, 14, headline="One clause struck out in public",
         say="Two options, named to their faces: a war of expulsion, or a humbling settlement. "
             "Ibn Mas'ud ؓ defines the first — that they be put out of their homes. "
             "The settlement: weapons and horses surrendered; compensation one way only; and "
             "blood-money for our dead. Umar ؓ interrupted at that clause, and approved the "
             "rest. No captives were taken at Buzakha.")

    # ================================================================ ACT 3
    D.section_slide(prs, "al-Yamama",
                    "Act Three  ·  11–12 AH  ·  the hardest day of the war")

    stmt(prs, 15, headline="Two brothers by appointment",
         say="[HANDS] Before telling it: you are given a brother — not born to you, assigned "
             "to you. How long would you expect that to last? The mu'akhah paired each Muhajir "
             "with a man of the Ansar. Zayd b. al-Khattab ؓ was paired with Ma'n b. Adi ؓ; "
             "both were killed at al-Yamama on the same day. Abu Hudhayfa ؓ and Abbad b. Bishr "
             "ؓ were paired the same way and died there too (al-Bidaya vol. 7 p. 55). This "
             "card is the frame of the act: tell the room to watch for households.")

    stmt(prs, 16, headline="The son of the elder of the Jahiliyya",
         say="[HANDS] Before it: who here has a relative who did not agree with the biggest "
             "decision they ever made? Leave the hands up one beat and move on — do not "
             "develop it. al-Dhahabi رحمہ اللہ opens the notice without softening anything: "
             "martyr, son of the elder of the Jahiliyya, man of Badr, in one sentence. He had "
             "accepted Islam before the Companions were meeting in the house of al-Arqam.")

    stmt(prs, 17, headline="Something about your father", arabic=AR17,
         say="After Badr the dead of Quraysh were put into the well, and Utba b. Rabi'a was "
             "dragged to it. The Prophet ﷺ looked at the face of his son and saw it had gone "
             "pale, and asked him whether something had entered him about his father. This is "
             "the answer. Then the Prophet ﷺ prayed for him and spoke kindly to him. He was "
             "not told that grief was a fault, and he did not pretend he had none. The opening "
             "sentence of the report is spoken, not printed — the slide carries the answer.")

    stmt(prs, 18, headline="Four titles, and one origin",
         say="[HANDS] Before it: where do you think the man who led the Muhajirun in prayer came "
             "from? Salim ؓ was a slave, his origin Istakhr in Persia. The woman of Abu "
             "Hudhayfa's ؓ household freed him and Abu Hudhayfa ؓ adopted him outright. "
             "al-Dhahabi رحمہ اللہ opens the notice with four descriptions in a row and not "
             "one of them is about where he came from.")

    stmt(prs, 19, headline="The imam at Quba'", arabic=AR19,
         say="The Muhajirun reached Medina before the Prophet ﷺ did, camped at al-Usba beside "
             "Quba', and had to pray. They put a freed slave in front because he had more of "
             "the Qur'an than any of them. Among the men praying behind him: Umar b. al-Khattab "
             "ؓ and Abu Salama b. Abd al-Asad ؓ. The Siyar editor's page break falls inside "
             "the sentence, so the slide carries the clause before it and the rest is spoken.")

    s = D.map_slide(prs, "map_s2_yamama.png", "Aqraba'", kicker=kicker(20),
                    keys=keys(("al-Yamama", "Khalid ؓ comes east"),
                          ("Aqraba'", "on the cultivated edge"),
                          ("Behind the line", "farmland and households"),
                          ("No line of retreat", "back is through his home"),
                          ("Forty thousand", "the men Musaylima had")))
    mark(prs, 20, s,
         "Point at the red block and say it: it has no line of retreat, and that was the "
         "intention. Ikrima ؓ and Shurahbil ؓ had approached earlier.")

    stmt(prs, 20, headline="Keep this one man alive",
         say="The night before, the vanguard picked up a raiding party coming home. He executed "
             "them and kept one alive on a stranger's advice: Mujja'a b. Murara, in irons, in "
             "the tent with Khalid's ؓ wife. That decision settled the end of the battle "
             "before it started.")

    stmt(prs, 21, headline="The line breaks",
         say="One of their leaders told them that if they lost, their women would be taken. The "
             "armies collided and the Muslim line broke; the bedouin contingents ran. The "
             "prisoner in irons in that tent stood up and gave Umm Tamim his protection. Later "
             "the same day Muslims came into the same tent meaning to kill him, and she gave "
             "him hers — Siyar (al-Khulafa' al-Rashidun) p. 47. The book keeps both halves.")

    stmt(prs, 22, headline="The banner, and the vow of silence", arabic=AR22,
         say="Zayd b. al-Khattab ؓ was carrying a banner and the line was going backwards. He "
             "said he would not speak again until either Allah routed them or he met Allah and "
             "put his case to Him himself. He went forward and did not stop going forward. The "
             "banner fell and Salim ؓ picked it up. CAUTION: three approved books give three "
             "different banner arrangements. Say 'he carried a banner' and never draw the "
             "diagram. al-Kamil vol. 2 p. 217 has a longer wording of the same vow — do not "
             "merge them.")

    stmt(prs, 23, headline="Are you not content to live praised?",
         say="Thabit b. Qays ؓ was the orator of the Ansar and had a very loud voice. When the "
             "verse came down forbidding the believers to raise their voices above the "
             "Prophet's ﷺ, he concluded he was of the people of the Fire, shut himself in his "
             "house and stopped coming. The Prophet ﷺ noticed he was missing and sent for the "
             "reason. The verse-and-house incident is Sahih Muslim 119 and Sahih al-Bukhari "
             "3613. PLAY THIS IMMEDIATELY BEFORE THE SHROUD — it is what makes the shroud land.")

    s = D.image_slide(prs, "l02_shroud_garments.png", "He put on his burial garments",
                      kicker=kicker(24),
                      caption=cap("Thabit b. Qays ؓ — burial perfume, while the line went backwards."),
                      brief="Restrained editorial still life in muted bone, ochre and deep teal. "
                            "Two plain undyed white cotton garments, freshly folded, resting on "
                            "a low rough wooden bench; beside them a small unglazed clay vessel "
                            "of perfume with its stopper set down alongside. Bare packed-earth "
                            "floor, plain mud-brick wall behind. Quiet dignified morning light "
                            "falling from a small high opening. No people, no hands, no faces, "
                            "no figures. 16:9 landscape.")
    mark(prs, 24, s,
         "Anas ؓ found him doing it and said: do you not see what is happening? He said: in a "
         "moment, nephew. Then he took the Ansar's banner, dug his feet in to the middle of his "
         "shins, and did not move until he was killed. On the same field, in the same minutes, "
         "the whole army was calling to each other: 'people of Surat al-Baqara — the sorcery "
         "is void today' (al-Bidaya vol. 7 p. 33).")

    stmt(prs, 24, headline="This is not how we used to fight",
         say="He did not tell them what to do. He told them what they had already been.")

    stmt(prs, 25, headline="A wretched bearer of the Qur'an",
         say="Salim ؓ was holding the banner of the Muhajirun — a banner the man before him "
             "had been killed carrying. He answered a question about his courage by naming what "
             "he carried. He is the man the Prophet ﷺ went out at night to listen to (Siyar "
             "vol. 1 p. 168).")

    stmt(prs, 26, headline="Adorn the Qur'an with deeds", arabic=AR26,
         say="Same field, same hour. He did not call them by tribe and he did not call them by "
             "clan. He called them the people of the Qur'an, and told them what to do about it. "
             "Then he charged, drove them back, and was struck down.")

    s = D.image_slide(prs, "l02_cooking_pot.png", "The armour in the cooking pot",
                      kicker=kicker(27),
                      caption=cap("An upturned pot at the far end of the camp, a pack-saddle on top."),
                      brief="Restrained editorial still life in muted ochre, bone and deep teal. "
                            "At the far edge of an emptied desert camp at dusk: a large "
                            "blackened cooking pot turned upside down on bare stony ground, "
                            "with a worn wooden camel pack-saddle set on top of it. Scuffed "
                            "sand, a few tent-peg holes, cold ashes at one side, the ground "
                            "running away flat behind. Long low light from one side, quiet blue "
                            "shadow. No people, no hands, no faces, no figures, no weapons "
                            "shown. 16:9 landscape.")
    mark(prs, 27, s,
         "Thabit b. Qays ؓ was killed at al-Yamama and his coat of mail was stolen off his "
         "body by a Muslim, who hid it. A man of the army saw him in a dream and was told where "
         "it was, and given three things to say to the caliph. The mail was exactly where he "
         "had said. REPORT THE CHAIN THE WAY THE BOOKS DO: Ibn Kathir says the account has "
         "other corroborating reports; his editor notes the daughter in the chain is unknown; "
         "and al-Haythami's line is the one to give aloud — the rest of the report is in the "
         "Sahih, the episode of the mail is not. Build no ruling about dreams on it.")

    stmt(prs, 27, headline="A will carried out after his death",
         say="What he sent back was a debt he owed, property he had, and a slave of his who was "
             "to be freed — and twice he told the man not to dismiss it as a dream and let it "
             "go to waste. In Medina Abu Bakr ؓ carried out the will of a man who was already "
             "dead. The long version, naming Khalid ؓ and the caliph, is Siyar vol. 1 p. 313.")

    stmt(prs, 28, headline="I find the scent of Paradise",
         say="[HANDS] Ask first: has anyone here ever missed something and spent years wishing "
             "they had been there? Anas b. al-Nadr ؓ had missed Badr and it weighed on him. At "
             "Uhud the line broke; he walked forward with his sword and met Sa'd b. Mu'adh ؓ "
             "on the way. Sa'd ؓ said afterwards that he himself could not do what that man "
             "had done. NOTE: the year is not fixed on the pages read — Siyar's chapter "
             "heading is 'the raid of Uhud, and it was in Shawwal'.")

    stmt(prs, 29, headline="Known by his fingertips",
         say="When the fighting stopped they went out to identify the dead. More than eighty "
             "wounds on him — sword, spear and arrow — and his own family could not tell "
             "who he was. His sister recognised her brother by his fingertips. CITATION "
             "CAUTION: the verse is quoted on the al-Bidaya page; the surah-and-verse reference "
             "is printed on the Siyar page, not on that one. Cite both, or check a mushaf "
             "before printing it.")

    stmt(prs, 30, headline="Do you see me dying in my bed?",
         say="Anas ؓ came in on his brother and found him singing over his bow, and asked him "
             "how long that was going to go on. The counts move between the chains — "
             "ninety-nine in one, ninety-odd in another, a hundred in a third. Say 'the reports "
             "give ninety-odd' and move on.")

    s = D.image_slide(prs, "l02_shut_gate.png", "The gate was shut from the inside",
                      kicker=kicker(31),
                      caption=cap("Eighty-odd wounds. Khalid ؓ was a month treating them. He survived."),
                      brief="Restrained editorial illustration in muted ochre and bone with deep "
                            "teal shadow. A high solid mud-brick wall running right across the "
                            "frame, with one heavy timber gate shut fast in it; the crowns of "
                            "date palms visible above the wall from inside; stony open ground in "
                            "the foreground. Seen from outside, straight on, the wall filling "
                            "most of the frame so that it reads as unclimbable. Hard midday "
                            "light, hard shadow at the foot of the wall. No people, no faces, no "
                            "figures. 16:9 landscape.")
    mark(prs, 31, s,
         "[HANDS] Before telling it: the gate is shut, the wall is solid, and there are "
         "thousands inside — what do you do? CAUTION: al-Bara' b. Malik ؓ SURVIVED. Ibn "
         "Khaldun appears to list him among the killed; Siyar contradicts it (vol. 1 p. 196). "
         "Do not say he died there.")

    stmt(prs, 31, headline="Throw me over onto them",
         say="They refused. He made them do it. Lifted on a shield raised on spear-shafts until "
             "he topped the wall, down among them alone, and fought his way to the gate.")

    s = D.diagram_slide(prs, "One house, Uhud and al-Yamama", kicker=kicker(32),
                        rows=[("The servant",
                               "Anas b. Malik ؓ, the Prophet's ﷺ servant for ten years"),
                              ("The brother",
                               "al-Bara' b. Malik ؓ, the man on the shield"),
                              ("The uncle",
                               "Anas b. al-Nadr ؓ, eighty-odd wounds at Uhud")],
                        caption=cap("One house. The same count of wounds, and one got up."))
    mark(prs, 32, s,
         "THE FAMILY SENTENCE — say it before or after, but say it: the man on that shield is "
         "Anas b. Malik's ؓ elder brother, the elder brother of the boy who served the Prophet "
         "ﷺ for ten years; their uncle came off the field at Uhud with the same count of "
         "wounds, and did not get up. (Siyar vol. 1 p. 195, al-Bidaya vol. 6 p. 396, Siyar "
         "vol. 1 p. 196, al-Bidaya vol. 4 p. 203.) CAUTION: do NOT add that his mother is the "
         "woman who asked for Islam as her dower — no page read names al-Bara's ؓ mother. "
         "The sentence is just as strong through the brother, and the brother is on the page. "
         "This card's quotation is the previous slide's and is not repeated here.")

    stmt(prs, 33, headline="The arrow he pulled out",
         say="Abu Aqil ؓ was one of the chiefs of the Ansar and a man of Badr. Two men who "
             "would not be carried: al-Bara' ؓ survived with eighty wounds, Abu Aqil ؓ did "
             "not survive. Tell them as a pair. CAUTION: the long famous version of this "
             "account — the night wound, the dead arm, the severed arm, the fourteen wounds, "
             "'who won?' — is NOT in any approved source. Tell only what is on the slide.")

    stmt(prs, 34, headline="Lay me down between them",
         say="Struck down, Salim ؓ asked what had become of Abu Hudhayfa ؓ, then about one "
             "other man, and then asked for one thing. CAUTION: the second man is 'so-and-so' "
             "in the source. Do not name him. And no approved source says they were buried in "
             "one grave.")

    stmt(prs, 35, headline="How they were found",
         say="CARRY THE 'IT IS SAID' ACROSS INTO THE DELIVERY: al-Dhahabi رحمہ اللہ introduces "
             "this with 'and it is said', which is his way of passing something on without "
             "vouching for it. Say 'it is said that…', never 'they were found'. Elsewhere, in "
             "the roll of the day's martyrs (Siyar vol. 1 p. 298), he lists the two of them "
             "first and in that order: the master and the freedman on one line.")

    stmt(prs, 36, headline="I do not hear",
         say="Habib b. Zayd ؓ was in Musaylima's hands. His mother was Umm Umara Nusayba bint "
             "Ka'b رضي الله عنها, who had been at al-Aqaba, at Uhud, at al-Hudaybiya and at "
             "Hunayn. When the army marched to al-Yamama she went with it. Her hand was cut off "
             "there. She came back to Medina covered in wounds, and Abu Bakr ؓ, while he was "
             "caliph, was seen coming to her to ask after her. NUMBER CAUTION: Siyar vol. 2 "
             "p. 281 says eleven wounds besides; al-Bidaya vol. 3 p. 428 says twelve. Give one "
             "figure with its caption, or say only 'covered in wounds'. Her other son Abd Allah "
             "b. Zayd ؓ is named in one of four accounts of who killed Musaylima — do not "
             "settle it.")

    stmt(prs, 37, headline="What Wahshi ؓ said afterwards",
         say="Wahshi b. Harb ؓ, who had killed Hamza ؓ at Uhud before he was a Muslim. "
             "His javelin went through and out the other side; a second man came up with a "
             "sword. Sources differ on who the second man was — say 'a second man'. "
             "Afterwards Khalid ؓ walked the dead with the prisoner to identify the body. "
             "CAUTION: do not use the anonymous ranking saying on the same Siyar page.")

    stmt(prs, 38, headline="The same spear, at al-Yamama",
         say="He took the same spear he had thrown at Uhud, saw a man standing in a gap in a "
             "wall, and did not know who it was. He would never claim the kill for himself. "
             "This is what he said about the two throws of his life.")

    stmt(prs, 39, headline="The witness against the enemy",
         say="He had spent his life among fighting men on both sides. His verdict on "
             "Musaylima's army was one sentence, and it was not the sentence anyone expects "
             "from the winning side. NOTE: this is the same sentence as the Wahshi ؓ card two "
             "slides back, given on its own. If the evening is running, cut this and keep that.")

    stmt(prs, 40, headline="He outstripped me to both",
         say="The news came back to Medina. What Umar ؓ said when he heard it was not about "
             "the battle. It was a count of two things and he had come second in both. Siyar "
             "vol. 1 p. 298 carries the second half as something he repeated.")

    s = D.image_slide(prs, "l02_east_wind.png", "The east wind", kicker=kicker(41),
                      caption=cap("al-Saba is the east wind. It comes from the direction of al-Yamama."),
                      brief="Restrained editorial landscape in muted ochre, bone and deep teal. "
                            "A wide empty stony plain seen low and level at the end of the day, "
                            "with fine dust and a few dry grass heads bent all one way by a "
                            "steady wind coming from the far horizon. No road, no building, no "
                            "animal. A low pale sky, long soft shadows, the air slightly hazy "
                            "with carried dust. Absolutely no people, no faces, no figures. "
                            "16:9 landscape.")
    mark(prs, 41, s,
         "The remark that the wind came from the direction of al-Yamama is the speaker's own "
         "— the books do not say it. Say it as your own or leave it out.")

    stmt(prs, 41, headline="I find in it the scent of Zayd",
         say="CAPTION CAUTION: al-Bidaya vol. 7 p. 50 has a different wording of the same "
             "remark. The slide carries the Siyar words under a Siyar caption. Do not print the "
             "Siyar words under an Ibn Kathir caption.")

    # ================================================================ ACT 4
    D.section_slide(prs, "What it cost, and what it produced", "Act Four  ·  12 AH")

    stmt(prs, 42, headline="The number nobody can give",
         say="[HANDS] Before telling it: how many men who had the whole Qur'an by heart died "
             "that day? What would you guess? — then give the honest answer: the books do not "
             "say. THIS IS THE CARD THAT STOPS A WRONG NUMBER BEING SAID. The figures the safe "
             "list does give run from 58 to more than 1,080, and none of them is a count of "
             "reciters. Anyone who says '450 reciters' has misread al-Bidaya vol. 7 p. 55.")

    stmt(prs, 43, headline="And Allah knows best",
         say="[HANDS] Ask first: if every copy of a book you loved lived only in people's "
             "memories, how many funerals would it take to lose it? Ibn Kathir's phrase is "
             "istaharra al-qatl fi al-qurra' — the killing ran hot among the reciters; the "
             "editor glosses istaharra as ishtadda. The dead in the garden and in the battle "
             "close to ten thousand, though some say twenty-one thousand. NEVER put a number of "
             "qurra' on the slide; no source we use gives one.")

    stmt(prs, 44, headline="Take the Qur'an from four",
         say="Ibn Kathir رحمہ اللہ, writing Salim's ؓ death notice, gives the reason the ummah "
             "remembered him. SLIDE RULE: Ibn Kathir's own text quotes only the opening clause. "
             "If the four names go on screen they must be captioned to Sahih Muslim 2464 as "
             "given in the editor's note on al-Bidaya vol. 7 p. 50 — never to Ibn Kathir.")

    stmt(prs, 45, headline="A thing the Messenger ﷺ did not do",
         say="Zayd b. Thabit ؓ of Banu al-Najjar: eleven years old when the Prophet ﷺ "
             "reached Medina, seventeen suras memorised before he was introduced, learned the "
             "Jews' script in a fortnight, wrote the revelation down as it came. His objection "
             "is the most serious objection there is.")

    s = D.image_slide(prs, "l02_four_materials.png", "There was no volume to copy from",
                      kicker=kicker(46),
                      caption=cap("Parchment, shoulder-blades, palm-stalks — and the breasts of men."),
                      brief="Restrained editorial still life in muted ochre, bone and deep teal, "
                            "laid out on a plain scrubbed wooden surface and seen from directly "
                            "above. Four kinds of thing set well apart from one another: strips "
                            "of aged parchment; two flat dried animal shoulder-blades; several "
                            "bare stripped date-palm stalks; and a few thin flat white stones. "
                            "Any marks on them suggested only as faint illegible strokes, never "
                            "readable letters of any script. Soft even daylight, quiet shadows, "
                            "generous empty space between the four groups. No people, no hands, "
                            "no faces. 16:9 landscape.")
    mark(prs, 46, s,
         "[HANDS] Say the four once, then ask the room to name them back to you. It is the one "
         "line in the evening everybody will remember. Ibn Kathir names al-likhaf — the thin "
         "white stones — where al-Dhahabi names al-riqa'. Cite both if you use both.")

    stmt(prs, 46, headline="He tracked it down, piece by piece",
         say="The verb in his own account is tatabba'a — to follow a thing up piece by "
             "piece. Then it was one set of suhuf, in one place, for the first time.")

    # ================================================================ ACT 5
    D.section_slide(prs, "Arabia whole again", "Act Five  ·  12 AH")

    s = D.map_slide(prs, "map_s2_darin.png", "Darin — into the water", kicker=kicker(47),
                    keys=keys(("al-Bahrayn", "the beaten take ship"),
                          ("The land roads", "closed behind them first"),
                          ("Darin", "a day and a night by sea"),
                          ("Across the water", "out and back in one day"),
                          ("What was lost", "one man's horse-fodder")))
    mark(prs, 47, s,
         "Both books describe the crossing the same way: they walked on something like soft "
         "sand with water over it, not deep enough to reach the camels' pads. al-Bidaya vol. 7 "
         "p. 40 prints the du'a they said going in.")

    stmt(prs, 47, headline="Go straight across the sea",
         say="He closed the roads behind the enemy before he opened one in front of himself.")

    stmt(prs, 48, headline="Not until you have proved yourself",
         say="Ikrima ؓ had one of the eleven banners and was sent against Musaylima with "
             "Shurahbil ؓ following. He attacked before Shurahbil ؓ arrived, wanting the "
             "victory on his own, and was badly handled. The caliph wrote to him — and then "
             "sent him on: Uman, Mahra, Yemen, Hadramawt. He fought in every one of them. He "
             "was corrected and kept, not corrected and dropped.")

    stmt(prs, 49, headline="My Lord's speech, my Lord's speech",
         say="The son of Abu Jahl kissed the Book and wept over it. WORDING CAUTION: 'kissed' "
             "is Ibn Kathir's word, which is what this slide cites. 'Held it to his face' is "
             "al-Darimi's wording and must not be said under a Bidaya caption. Imam Ahmad "
             "رحمہ اللہ later cited the habit as evidence in a question of law.")

    stmt(prs, 50, headline="Tulayha ؓ comes back",
         say="[HANDS] This is the payoff — ask it: last time we left Tulayha riding away from "
             "Buzakha. What do you think became of him? Take answers, then tell it. He escaped "
             "to Syria and lived among the Ghassanids, then returned to Islam and went to Mecca "
             "for umra. Ibn Kathir says twice that he could not bring himself to face Abu Bakr "
             "ؓ. Then he came to greet Umar ؓ. And Umar ؓ was pleased by his answer, and was "
             "satisfied with him.")

    s = D.map_slide(prs, "map_s2_arabia_12ah.png", "Arabia whole again", kicker=kicker(51),
                    keys=keys(("Every region", "no part untouched"),
                          ("The armies", "a support to believers"),
                          ("The fifth", "of the spoils, spent"),
                          ("Najran", "renewed its covenant"),
                          ("Just over a year", "late 11 AH to early 12")))
    mark(prs, 51, s,
         "This is Ibn Kathir's own summing-up, not ours. He does not describe a conquest. One "
         "colour, no arrows: hold on this map and let them look at it.")

    stmt(prs, 51, headline="What Ibn Kathir says it was", arabic=AR51,
         say="The armies were sent to hold up people who were already standing. The whole thing "
             "was over in a little more than a year. A contiguous clip of a 339-character "
             "passage; the whole passage, with its closing date sentence, is in the briefing.")

    stmt(prs, 52,
         say="[HANDS] Ask first: two years after the tribes broke apart, they were moving on two "
             "empires — what had changed? His answer multiplies nobody's numbers. SAY HIS "
             "NAME and say 'as he reads it': he never wrote this about the ridda; joining his "
             "chapter to the year eleven is ours. Ibn Khaldun is admitted for judgement and "
             "framing only (DECISIONS.md #29). His عبرت is spoken here and is deliberately NOT "
             "one of tonight's five lines.")

    s = D.statement_slide(prs, english="Mark three places on the map. Write three years into the "
                                       "boxes.",
                          headline="Ninety seconds", size=44)
    D.note(s, "[WORKSHEET] 90 seconds, silent. Say nothing at all while they write. Do not fill "
              "the silence. Watch the clock.")

    # ================================================================ ACT 6
    D.section_slide(prs, "Outward", "Act Six  ·  12–13 AH")

    stmt(prs, 53, headline="Two restrictions that are easy to miss", arabic=AR53,
         say="Muharram 12 AH. The letter did not say 'conquer Iraq'. It said: come at Iraq from "
             "its lower end. Then two restrictions that are easy to miss — no man compelled "
             "to march, and no man used who had apostatised, even if he has come back. The "
             "slide carries the two restrictions; the call, the jizya and the order to fight "
             "are on the same page and are spoken.")

    stmt(prs, 54, headline="He walked beside the stirrup",
         say="Yazid b. Abi Sufyan ؓ was one of four commanders appointed for Syria. He was "
             "called Yazid al-Khayr. He was the brother of Umm Habiba ؓ, the Mother of the "
             "Believers, and his father had led the army at Uhud. When Abu Bakr ؓ tied his "
             "standard he did not stand and watch him ride out. The caliph walked and the "
             "commander rode, and neither of them thought it strange.")

    s = D.map_slide(prs, "map_s2_iraq_sham_13ah.png", "Five days of waterless country",
                    kicker=kicker(55),
                    keys=keys(("al-Hira", "Iraq from its lower end"),
                          ("Quraqir", "strikes north-west"),
                          ("The Samawa", "nine days, five nights"),
                          ("Suwa and Tadmur", "out behind the Romans"),
                          ("The guide", "Rafi' b. Umayra al-Ta'i")))
    mark(prs, 55, s,
         "[HANDS] Ask: how do you carry water for an army across five days of desert with no "
         "wells? Take two answers, then tell them. The strongest camels made thirsty, then "
         "watered twice over, lips cut and mouths bound so they could not chew and lose the "
         "water; ten opened every day to water the horses. Length: al-Bidaya says nine days, "
         "al-Kamil and Siyar say five nights. Say both.")

    stmt(prs, 55, headline="Only once in my life",
         say="On the last stretch Rafi', whose eyes were bad, asked whether they could see a "
             "box-thorn bush the height of a seated man. They said no. He said: then by God you "
             "are dead, and I am dead with you. They looked again. It was there, cut to a stump. "
             "They dug at its root and found the spring.")

    stmt(prs, 56,
         say="Four commanders had come to the Yarmuk, each over his own men, nobody over all of "
             "them. He did not ask for the command; he proposed passing it round. They made him "
             "commander expecting it to last a long time. It lasted one day.")

    stmt(prs, 57, headline="Armies are made many by victory",
         say="[HANDS] Ask the room to guess the two army sizes. Take three guesses — then "
             "show that the books themselves give three different answers, and say why. A "
             "Christian Arab standing near him had said out loud what everyone could see.")

    # ================================================================ ACT 7
    D.section_slide(prs, "He dies", "Act Seven  ·  13 AH")

    stmt(prs, 58, headline="There is harshness in him",
         say="[HANDS] Before telling it: who here has worked with someone whose hardness was a "
             "response to somebody else's softness? He did not argue with the description. He "
             "explained it: when I was angry with a man, Umar ؓ showed me leniency; when I "
             "was gentle, he showed me severity.")

    stmt(prs, 59, headline="I have not appointed a relative over you",
         say="The document was finished and read out to the gathered people; Umar ؓ walked "
             "beside the freedman who carried it, telling the crowd to be quiet and listen. "
             "They said: we hear and we obey. Then he asked them a question nobody had asked "
             "him.")

    s = D.diagram_slide(prs, "What in the house was not his", kicker=kicker(60),
                        rows=[("A servant", "an Abyssinian, in the house"),
                              ("A camel", "used for carrying water"),
                              ("A blanket", "worn down to the nap")],
                        caption=cap("Send them to Umar when I die. And she did."))
    mark(prs, 60, s,
         "[HANDS] Before telling it: could you list, right now, everything in your house that "
         "is not yours? He called A'isha ؓ and told her that since the day he took charge of "
         "the Muslims' affair he had not eaten a dinar or a dirham of theirs — only the "
         "coarsest of their food, only the roughest of their clothing. Then he listed these "
         "three.")

    stmt(prs, 60, headline="He closed the account himself")

    stmt(prs, 61, headline="Sell my land and pay them back",
         say="The community had voted him a maintenance when he gave up trading — a man "
             "cannot run a market stall and a state at once. NUMBER CAUTION: the sources give "
             "6,000 dirhams a year, half a sheep a day, and 2,500. Put no figure on the slide. "
             "The instruction is the point, not the amount.")

    stmt(prs, 62, headline="The living need the new more",
         say="He gave instructions for his own washing — his wife Asma' bint Umays ؓ, "
             "and his son Abd al-Rahman ؓ. Then the shroud: use the two garments I am "
             "wearing, and buy one more to go with them.")

    s = D.diagram_slide(prs, "Three graves, one behind the other", kicker=kicker(63),
                        rows=[("The Prophet ﷺ", "the first of the three"),
                              ("Abu Bakr ؓ", "his head at the Prophet's ﷺ shoulders"),
                              ("Umar ؓ", "later, his head at Abu Bakr's waist")],
                        caption=cap("Four men went down: his son, Umar, Uthman and Talha."))
    mark(prs, 63, s,
         "One sentence in Siyar fixes all three positions. CAUTION: do NOT claim the burial was "
         "'in A'isha's ؓ house' from these pages — they say beside the Prophet ﷺ, and no "
         "more.")

    stmt(prs, 63, headline="Buried before morning came",
         say="Monday evening, eight nights remaining of Jumada al-Akhira 13 AH. Umar ؓ "
             "prayed over him in the Prophet's ﷺ mosque, four takbirs. Carried on the same "
             "bier the Prophet ﷺ had been carried on. He was sixty-three — the age at "
             "which the Prophet ﷺ died.")

    stmt(prs, 64, headline="Had Salim ؓ been alive",
         say="Eleven years after al-Yamama, Umar ؓ was dying of the assassin's wound and "
             "refused to name one man, setting up a council of six instead. SAY 'IT IS RELATED "
             "THAT…' — that is Ibn Kathir's own passive. Ibn Abd al-Barr رحمہ اللہ explains "
             "it: he would have gone by Salim's ؓ judgement about whom to appoint. A second, "
             "differently worded report in Siyar vol. 1 p. 170 names both Salim ؓ and Abu "
             "Ubayda ؓ, and al-Dhahabi weakens its chain on the page. Do not merge the two.")

    # ================================================================ the close
    s = D.timeline_slide(prs, "line_s2_lit.png", "What year are we in now?",
                         caption=cap("11 AH to 13 AH. Two years and three months."),
                         kicker="Bookend out")
    D.note(s, "[HANDS 3] Ask it before you advance, and let them answer. Then show the Line. "
              "This slide opens session 3 unchanged.")

    s = D.map_slide(prs, "map_s2_close_13ah.png", "Where we stand now", kicker="13 AH",
                    keys=keys(("Arabia", "whole, and under one authority"),
                          ("Iraq", "entered from its lower end"),
                          ("Syria", "the armies are on the Yarmuk"),
                          ("The dashed outline", "where the map stood when you walked in")))
    D.note(s, "[BOOKEND OUT] Hold on this one. Let them compare it with slide 3 themselves. "
              "This slide opens session 3 unchanged.")

    D.lessons_slide(prs, LESSONS, headline="Tonight")

    D.question_slide(prs, "He said the office would take much of that hardness away. "
                          "Next week — did it?")

    return prs


def runs(nums):
    """Collapse a sorted list of slide numbers into printable ranges."""
    out, i = [], 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1
        out.append(str(nums[i]) if j == i else "%d-%d" % (nums[i], nums[j]))
        i = j + 1
    return ", ".join(out)


# ============================================================================ main
if __name__ == "__main__":
    verify()
    if "--verify" in sys.argv:
        raise SystemExit(0)
    prs = build()
    D.save(prs, OUT)
    D.write_briefs(BRIEFS)
    n = len(prs.slides._sldIdLst)
    print("   %d slides carry the starred 29-card cut, %d are the over-build, %d are furniture"
          % (TALLY["star"], TALLY["cut"], n - TALLY["star"] - TALLY["cut"]))
    print("   delete these to reach 45 minutes: %s" % runs(CUT_SLIDES))
