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

Where a quotation is too long to sit on one slide, the deck shows a CONTIGUOUS CLIP of it —
`clip()` slices the string, it never edits it — and the clip is checked back against SPINE.md
like everything else. The English renderings below are ours: they are trimmed from SPINE's own
renderings so the block fits above the citation strip, and they carry no Arabic script inline,
because Arabic and Latin in one line is what mangled the first speaker scripts (CLAUDE.md §1.3).

LANGUAGE (DECISIONS.md #19). English carries every slide. No generated Urdu anywhere. Arabic
appears only as verbatim source quotation, in Naskh, with an English rendering beneath it.
Citations are given in Latin transliteration with Latin digits — an Arabic book title sharing a
line with "vol. 7, p. 10" is exactly the bidi reordering bug CLAUDE.md §1.3 warns about.

LAYOUT NOTE. deck2's statement layout estimates the Arabic block's height, then places the
English beneath it and the citation at a fixed strip. A quotation past about 156 rendered
characters pushes the English into the citation, so `stmt()` drops the title bar for those three
slides and lets the quotation carry the slide on its own — that is deck2's second statement
layout, not a workaround.

MAPS are not Gemini's job. The nine map files named here are built by `series/make_visuals.py`;
until they exist each map slide carries a correctly-sized placeholder naming the file it wants.
The five IMAGE BRIEFs are Gemini's, and each one is non-figurative by design: no depiction of the
Prophet ﷺ, of a Companion, or of any identifiable face, ever.
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


# ============================================================================ SPINE.md
def load_spine():
    """Pull every card's verbatim Arabic statement out of SPINE.md, keyed by card number."""
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
                ar[cur] = " ".join(block)
    return raw, ar


SPINE_RAW, AR = load_spine()


def clip(n, after=None, upto=None):
    """A contiguous slice of card n's statement. Slices only — never edits a character."""
    s = AR[n]
    if after:
        s = s[s.index(after) + len(after):]
    if upto:
        s = s[:s.index(upto) + len(upto)]
    return s.strip()


# Card 20's statement runs to 339 characters — three slides' worth. The deck shows the clause
# that is the point of it, exactly as printed, and the briefing carries the whole passage.
AR20 = clip(20, after="… ", upto="ولله الحمد.")


def verify():
    """Every Arabic string that reaches a slide must be a literal substring of SPINE.md."""
    needed = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
              20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
    missing = [n for n in needed if n not in AR]
    if missing:
        raise SystemExit("SPINE.md has no statement for card(s): %s" % missing)
    # A statement that wraps across several blockquote lines is stored here as one string, so
    # the file is flattened the same way before the comparison. Nothing else is touched.
    flat = re.sub(r"\n>\s*", " ", SPINE_RAW)
    strings = [AR[n] for n in needed] + [AR20]
    bad = [s for s in strings if s not in flat]
    if bad:
        raise SystemExit("%d Arabic string(s) are not literal substrings of SPINE.md — the deck "
                         "has drifted from the source:\n%s" % (len(bad), bad[0][:80]))
    print("verify: %d Arabic statements, all literal substrings of SPINE.md" % len(strings))
    return True


# ============================================================================ citations
# Latin transliteration, Latin digits. Printed pages exactly as SPINE.md gives them.
CITE = {
    1:  "al-Bidaya wa-l-Nihaya, vol. 5, p. 311",
    2:  "al-Bidaya wa-l-Nihaya, vol. 7, p. 10",
    3:  "al-Kamil fi al-Tarikh, vol. 2, p. 195",
    4:  "al-Bidaya wa-l-Nihaya, vol. 7, p. 11",
    5:  "al-Bidaya wa-l-Nihaya, vol. 7, p. 11",
    6:  "al-Kamil fi al-Tarikh, vol. 2, p. 202",
    7:  "al-Kamil fi al-Tarikh, vol. 2, p. 203",
    9:  "al-Bidaya wa-l-Nihaya, vol. 7, p. 24",
    10: "al-Kamil fi al-Tarikh, vol. 2, p. 205",
    11: "al-Bidaya wa-l-Nihaya, vol. 7, p. 27  ·  Sahih al-Bukhari 7221",
    12: "al-Bidaya wa-l-Nihaya, vol. 7, p. 33",
    13: "Siyar A'lam al-Nubala', vol. 1, p. 311  ·  Sahih al-Bukhari 2845",
    14: "al-Kamil fi al-Tarikh, vol. 2, p. 218",
    15: "Siyar A'lam al-Nubala' (Sirat al-Khulafa' al-Rashidin), p. 48",
    16: "al-Bidaya wa-l-Nihaya, vol. 7, p. 35",
    17: "Siyar A'lam al-Nubala', vol. 2, p. 431",
    18: "Siyar A'lam al-Nubala', vol. 2, p. 431",
    19: "al-Kamil fi al-Tarikh, vol. 2, p. 224",
    20: "al-Bidaya wa-l-Nihaya, vol. 7, p. 43",
    21: "Ibn Khaldun · Tarikh Ibn Khaldun, vol. 1, p. 198 — as he reads it",
    22: "al-Bidaya wa-l-Nihaya, vol. 7, p. 62",
    23: "al-Kamil fi al-Tarikh, vol. 2, p. 253",
    24: "al-Bidaya wa-l-Nihaya, vol. 7, p. 89",
    25: "al-Bidaya wa-l-Nihaya, vol. 7, p. 92",
    26: "al-Kamil fi al-Tarikh, vol. 2, p. 266",
    27: "al-Kamil fi al-Tarikh, vol. 2, p. 267",
    28: "Siyar A'lam al-Nubala' (al-Rashidun), p. 19",
    29: "al-Kamil fi al-Tarikh, vol. 2, p. 266",
    30: "al-Kamil fi al-Tarikh, vol. 2, p. 262",
    31: "Siyar A'lam al-Nubala' (al-Rashidun), p. 19",
}

# ============================================================================ renderings
# Trimmed from SPINE.md's own English renderings so the block clears the citation strip.
# Names transliterated: Arabic script never shares a line with Latin (CLAUDE.md §1.3).
EN = {
    1:  "If you find fault with his command, you found fault with his father's command before "
        "him — and this one is among the dearest of people to me after him.",
    2:  "By Him in whose hand is Abu Bakr's soul — if I thought the wild beasts would snatch "
        "me away, I would still send out Usama's expedition as the Messenger of Allah ﷺ "
        "ordered it.",
    3:  "May your mother lose you, son of al-Khattab! The Messenger of Allah ﷺ appointed him "
        "— and you order me to depose him?",
    4:  "Usama said: O successor of the Messenger of Allah, either you ride or I dismount. He "
        "said: By Allah, you shall not dismount, and I shall not ride.",
    5:  "He passed no tribe intending to break away but they said: were it not that these people "
        "have strength, men like these would not have gone out from among them.",
    6:  "The reserve came out at them with skins they had inflated … the Muslims' camels "
        "bolted with them on their backs and carried them back to Medina — and not one "
        "Muslim was thrown.",
    7:  "Dawn did not break until they and the enemy were on one ground … and the sun's rim "
        "had not risen before they turned their backs … and that was the first victory.",
    9:  "I have ordered my messenger to read his letter in every assembly of yours. The summons "
        "is the adhan: when they call it, hold off from them; if they do not, ask them what they "
        "owe.",
    10: "He said to me: you have a mill like his mill, and a matter you will not forget. Uyayna "
        "said: Allah knows there will be a matter you will not forget. Withdraw, Banu Fazara "
        "— the man is a liar.",
    11: "Umar ؓ said: as for your saying, and you pay blood-money for our dead — our "
        "dead were killed upon the command of Allah; there is no blood-money for them.",
    12: "Man — if you intend anything tomorrow for the people of Yamama, good or ill, keep "
        "this man alive … so Khalid kept him, in irons, and said: treat him well.",
    13: "Get out of our faces so we can strike the enemy. Wretched is what you have accustomed "
        "your opponents to! This is not how we used to fight alongside the Messenger of Allah "
        "ﷺ.",
    14: "Company of Muslims — throw me over onto them into the garden. They said: we will "
        "not. He said: By Allah, you will throw me onto them in it!",
    15: "From Wahshi: I never saw men more steadfast in the face of death than Musaylima's "
        "companions — then he mentioned that he had a share in killing Musaylima.",
    16: "Six hundred of the Muslims were killed — and it is said five hundred — and "
        "Allah knows best. Among them were leaders of the Companions and men of standing.",
    17: "I said: how will you do a thing the Messenger of Allah ﷺ did not do? He said: by "
        "Allah, it is good. And he did not stop coming back to me until Allah opened my breast.",
    18: "So I began to track down the Qur'an, gathering it from the parchments, the "
        "shoulder-blades, the palm-stalks, and the breasts of men.",
    19: "Allah has shown you of His signs on land so that you may take heed of them at sea. Rise "
        "against your enemy, and go straight across the sea.",
    20: "And matters continued so until there remained in the peninsula none but people obedient "
        "to Allah and His Messenger, and people under al-Siddiq's protection.",
    21: "The religious colouring takes away the rivalry and envy that are in people of asabiyya, "
        "and makes their direction one.",
    22: "Win the people over and call them to God … and he ordered him not to compel anyone "
        "to march with him, and not to use any man who had apostatised.",
    23: "By God, I have come to this water only once in my life — with my father, when I "
        "was a boy.",
    24: "Let us take the command in turn: one of us today, another tomorrow, another the day "
        "after — and let me have charge of you today.",
    25: "Woe to you — are you frightening me with the Romans? Armies are made many by "
        "victory and few by abandonment, not by the number of men.",
    26: "He is better than your opinion of him — except that there is harshness in him. Abu "
        "Bakr said: that is because he sees me being gentle.",
    27: "Are you content with the one I have appointed over you? For I have not appointed over "
        "you a relative of mine. I have appointed Umar over you.",
    28: "We have nothing of the Muslims' fay' except this Abyssinian servant, this "
        "water-carrying camel, and the worn nap of this blanket.",
    29: "When death came to him he directed that land of his be sold and its price paid over in "
        "compensation for what he had taken of the Muslims' property.",
    30: "He said: the living have more need of the new than the dead — this is only for the "
        "decay.",
    31: "A'isha ؓ said: he died on the night of Tuesday, and was buried before morning came.",
}

# ============================================================================ the five عبرت
# Drawn from the acts themselves, in SPINE.md's own words. No present-day parallel, ever.
# The cue sheet and the worksheet must print exactly these five.
LESSONS = [
    "There is a kind of steadiness that is not stubbornness: it is refusing to treat an "
    "emergency as permission.",
    "The whole war was set moving from one camp, in one sitting, by a man who had just been "
    "told to go home.",
    "Preservation is not one heroic act; it is somebody doing a careful, unglamorous job "
    "properly.",
    "What changed in Arabia was not how many men there were, but which way they were all facing.",
    "He kept an account of what was not his, and he closed it before he died.",
]


# ============================================================================ helper
LONG_AR = 156      # past this, the Arabic block pushes the English into the citation strip


def stmt(prs, n, headline=None, kicker=None, english=None, arabic=None, cite=None, say=None):
    """A statement slide from card n. A long quotation drops the title bar and carries itself."""
    ar = AR[n] if arabic is None else arabic
    if D._ar_len(ar) > LONG_AR:
        headline, kicker = None, None
    s = D.statement_slide(prs, english=english or EN[n], arabic=ar,
                          cite=cite or CITE[n], headline=headline, kicker=kicker)
    if say:
        D.note(s, say)
    return s


# ============================================================================ the deck
def build():
    prs = D.deck()

    # ---------------------------------------------------------------- 1  title
    D.title_slide(prs, "Two Years, Three Months", "11–13 AH  ·  632–634 CE",
                  "Session Two  ·  Abu Bakr al-Siddiq ؓ")

    # ---------------------------------------------------------------- 2-3  bookend IN
    s = D.timeline_slide(prs, "line_s1.png", "Where we stopped last week",
                         caption="The whole line. Tonight is the first two years of it.",
                         kicker="Bookend in")
    D.note(s, "[BOOKEND IN] This is session 1's closing Line, unchanged. Do not explain it — "
              "let them recognise it. 'We came from here.'")

    s = D.map_slide(prs, "map_s2_open_11ah.png", "Arabia, the morning after",
                    kicker="11 AH",
                    keys=[("Medina", "the capital, and one field army"),
                          ("The tribes around it", "some broken away, some refusing the zakat"),
                          ("The army", "raised for the Syrian frontier, not yet gone"),
                          ("Byzantine ground", "north-west, well past Tabuk")])
    D.note(s, "[BOOKEND IN] Session 1's closing Map, unchanged. Where the room walked in.")

    # ================================================================ ACT 1
    D.section_slide(prs, "The army he would not call back",
                    "Act One  ·  11 AH  ·  the first ten days")

    s = D.statement_slide(prs, english="Two years and three months.",
                          headline="How long was he caliph?", size=54)
    D.note(s, "[HANDS 1] Ask it, take the show of hands, take two guesses, THEN advance. "
              "Everything tonight happens inside that span.")

    s = D.map_slide(prs, "map_s2_usama.png", "An army pointed north",
                    kicker="Card 1  ·  11 AH",
                    keys=[("Medina", "the army is raised in his last weeks"),
                          ("Usama b. Zayd ؓ", "eighteen years old, given the command"),
                          ("al-Jurf", "the camp one march outside the city"),
                          ("Dhu Khushub", "on the road north"),
                          ("Ubna, in the Balqa'", "Byzantine ground, well past Tabuk")])
    D.note(s, "The first time the map points at Byzantine ground. In the ranks under an "
              "eighteen-year-old: Umar b. al-Khattab ؓ and the senior Muhajirun and Ansar. "
              "People said so out loud.")

    stmt(prs, 1, headline="The Prophet ﷺ answered them himself",
         say="He heard the objection, stood up, and answered it. His father is Zayd b. Haritha "
             "ؓ, who had commanded before him.")

    stmt(prs, 2, headline="Do you call the army back?",
         say="[HANDS] Ask before you tell it: the capital is surrounded and your only army is "
             "marching away — do you call it back? Take the hands. Among those who advised "
             "recall: Umar b. al-Khattab ؓ. Then read the line.")

    stmt(prs, 3, headline="And you order me to depose him?",
         say="The Ansar's second request was not 'cancel the march' but 'give us an older "
             "commander'. Umar ؓ carried the message. He took him by the beard.")

    s = D.image_slide(prs, "l02_walk_out.png", "The caliph on foot",
                      kicker="Card 4  ·  late Rabi' al-Awwal 11 AH",
                      caption="He walked. The commander rode. His own beast was led behind, empty.",
                      brief="Restrained editorial illustration in muted ochre, bone and deep "
                            "teal. A wide dusty caravan track leaving a walled palm oasis at "
                            "first light, seen from ground level. Deep camel prints and bare "
                            "human footprints pressed side by side into the dust and running "
                            "away down the track. At the right edge, a saddled riderless camel "
                            "standing with its lead-rope hanging loose. Low raking dawn light, "
                            "long shadows, fine airborne dust, distant low hills. Absolutely no "
                            "people, no faces, no human figures anywhere in the image. 16:9 "
                            "landscape.")
    D.note(s, "Only at the end did he ask a favour — and he asked it of Usama ؓ, "
              "because Usama ؓ was the commander and Umar ؓ was in his army: would you "
              "release Umar to me?")

    stmt(prs, 4, headline="Either you ride or I dismount")

    stmt(prs, 5, headline="Forty days, and what the tribes concluded",
         say="Marched late Rabi' al-Awwal 11 AH. Away forty days — some say seventy. It did "
             "not fight its way through; it simply passed. The books differ on the target: Ubna "
             "in the Balqa', or Quda'a clans, or a clash with Roman forces — say so.")

    # ================================================================ ACT 2
    D.section_slide(prs, "Arabia comes apart", "Act Two  ·  11 AH")

    stmt(prs, 6, headline="The first engagement was a setback",
         say="[HANDS] Before telling it: a delegation comes to negotiate and goes home again "
             "— what have they taken with them besides your answer? They counted the men. "
             "Three days later the raid came at night. Half stayed back at Dhu Husa as a "
             "reserve. Say the setback plainly; the book does.")

    stmt(prs, 7, headline="That was the first victory",
         say="Same night as the reverse. The three brothers of Muqarrin on the right, the left "
             "and the rear. Marched in the dark. Camped at Dhu al-Qassa and left al-Nu'man b. "
             "Muqarrin ؓ there with a detachment.")

    s = D.map_slide(prs, "map_s2_ridda_eleven.png", "Eleven banners at Dhu al-Qassa",
                    kicker="Card 8  ·  the biggest map moment of the evening",
                    keys=[("Dhu al-Qassa", "one day's ride out from Medina"),
                          ("Eleven commanders", "each given an objective and written orders"),
                          ("North and east", "Najd, al-Yamama, al-Sham, Quda'a"),
                          ("East and south-east", "al-Bahrayn, Uman, Mahra"),
                          ("South", "Yemen, Tihama, Hadramawt")])
    D.note(s, "[HANDS 2] Ask BEFORE this slide: Medina is one town — how many armies would "
              "you send out at once? Take the guesses, then show eleven arrows and count them "
              "with the room. He rode out a third time with his sword drawn and Ali ؓ at "
              "his camel's head; this time they would not let him go on. He tied the banners on "
              "that ground and went home. NOTE: Ibn Kathir announces eleven and prints ten; "
              "al-Kamil prints all eleven. Do NOT name the ninth commander — three sources "
              "give three forms of it.")

    s = D.image_slide(prs, "l02_letter.png", "The letter went ahead of the armies",
                      kicker="Card 9  ·  11 AH",
                      caption="One wording, copied out many times, carried ahead of the columns.",
                      brief="Restrained editorial still life in muted ochre, bone and deep teal. "
                            "A single sheet of aged parchment lying open on a plain scrubbed "
                            "wooden board, its writing suggested only as soft illegible strokes "
                            "— never readable letters of any script. Beside it a cut reed "
                            "pen and a small dark unglazed ink vessel; to one side a neat stack "
                            "of several identical folded and sealed letters waiting to be "
                            "carried. Soft directional daylight from one side, quiet shadows. No "
                            "people, no hands, no faces. 16:9 landscape.")
    D.note(s, "The messenger was to read it aloud in every assembly of the tribe. CAUTION: the "
              "same letter carries a harsh clause. Do not quote it and do not deny it. If "
              "raised: it is on that page, transmitted by Sayf b. Umar; the operative test on "
              "the same page is the adhan; and the question is for the fuqaha'.")

    stmt(prs, 9, headline="The letter set one test",
         say="A test any man could apply from a distance — no lawyer, no court. Call the "
             "adhan when you halt. If they answer it, stop.")

    s = D.map_slide(prs, "map_s2_buzakha.png", "Buzakha", kicker="Card 10  ·  11 AH",
                    keys=[("Aja' and Salma", "Khalid ؓ moves from here"),
                          ("Sumayra'", "Tulayha moves up to meet him"),
                          ("Buzakha", "Asad and Ghatafan; seven hundred of Fazara"),
                          ("Banu Amir", "sitting armed nearby, waiting to see"),
                          ("Then north-west to al-Sham", "Tulayha's line of flight")])
    D.note(s, "Tulayha sat wrapped in a cloak waiting for revelation while Uyayna b. Hisn did "
              "the fighting. Three times Uyayna broke off, walked back to the cloak, and asked "
              "whether Jibril had come.")

    stmt(prs, 10, headline="The man who walked off the field",
         say="[HANDS] Before telling it: he had followed this man, and was fighting for him that "
             "morning — what was the question that ended it? Tulayha's own exit is on the "
             "same page: a horse ready, a mount for his wife, and a line called back over his "
             "shoulder.")

    stmt(prs, 11, headline="One clause struck out in public",
         say="Two options, named to their faces: a war of expulsion, or a humbling settlement. "
             "Ibn Mas'ud ؓ defines the first — that they be put out of their homes. "
             "The settlement: weapons and horses surrendered; compensation one way only; and "
             "blood-money for our dead. Umar ؓ interrupted at that clause, and approved the "
             "rest. No captives were taken at Buzakha.")

    # ================================================================ ACT 3
    D.section_slide(prs, "al-Yamama",
                    "Act Three  ·  11–12 AH  ·  the hardest day of the war")

    s = D.map_slide(prs, "map_s2_yamama.png", "Aqraba'", kicker="Card 12  ·  11–12 AH",
                    keys=[("al-Yamama", "Khalid ؓ comes east into it"),
                          ("Aqraba'", "on the edge of the cultivated country"),
                          ("Behind the line", "the farmland and the households"),
                          ("No line of retreat", "no man falls back except through his home"),
                          ("Forty thousand", "the fighting men Musaylima had")])
    D.note(s, "Point at the red block and say it: it has no line of retreat, and that was the "
              "intention. Ikrima ؓ and Shurahbil ؓ had approached earlier.")

    stmt(prs, 12, headline="Keep this one man alive",
         say="The night before, the vanguard picked up a raiding party coming home. He executed "
             "them and kept one alive on a stranger's advice: Mujja'a b. Murara, in irons, in "
             "the tent with Khalid's ؓ wife. That decision settled the end of the battle "
             "before it started.")

    s = D.image_slide(prs, "l02_shroud_garments.png", "He put on his burial garments",
                      kicker="Card 13  ·  at Aqraba'",
                      caption="Thabit b. Qays ؓ — rubbing himself with burial perfume, "
                              "while the line went backwards.",
                      brief="Restrained editorial still life in muted bone, ochre and deep teal. "
                            "Two plain undyed white cotton garments, freshly folded, resting on "
                            "a low rough wooden bench; beside them a small unglazed clay vessel "
                            "of perfume with its stopper set down alongside. Bare packed-earth "
                            "floor, plain mud-brick wall behind. Quiet dignified morning light "
                            "falling from a small high opening. No people, no hands, no faces, "
                            "no figures. 16:9 landscape.")
    D.note(s, "Anas ؓ found him doing it and said: do you not see what is happening? He "
              "said: in a moment, nephew. Then he took the Ansar's banner, dug his feet in to "
              "the middle of his shins, and did not move until he was killed. On the same field "
              "in the same minutes: Salim the freedman of Abu Hudhayfa ؓ (the man the "
              "Prophet ﷺ went out at night to listen to), Zayd b. al-Khattab ؓ, and "
              "Abu Hudhayfa ؓ — their words are in the briefing, in Arabic.")

    stmt(prs, 13, headline="This is not how we used to fight",
         say="He did not tell them what to do. He told them what they had already been.")

    s = D.image_slide(prs, "l02_shut_gate.png", "The gate was shut from the inside",
                      kicker="Card 14  ·  Hadiqat al-Mawt",
                      caption="Eighty-odd wounds. Khalid ؓ stayed a month treating them. He "
                              "survived.",
                      brief="Restrained editorial illustration in muted ochre and bone with deep "
                            "teal shadow. A high solid mud-brick wall running right across the "
                            "frame, with one heavy timber gate shut fast in it; the crowns of "
                            "date palms visible above the wall from inside; stony open ground in "
                            "the foreground. Seen from outside, straight on, the wall filling "
                            "most of the frame so that it reads as unclimbable. Hard midday "
                            "light, hard shadow at the foot of the wall. No people, no faces, no "
                            "figures. 16:9 landscape.")
    D.note(s, "[HANDS] Before telling it: the gate is shut, the wall is solid, and there are "
              "thousands inside — what do you do? CAUTION: al-Bara' b. Malik ؓ "
              "SURVIVED. Ibn Khaldun appears to list him among the killed; Siyar contradicts it. "
              "Do not say he died there.")

    stmt(prs, 14, headline="Throw me over onto them",
         say="They refused. He made them do it. Lifted on a shield raised on spear-shafts until "
             "he topped the wall, down among them alone, and fought his way to the gate.")

    stmt(prs, 15, headline="What Wahshi ؓ said afterwards",
         say="Wahshi b. Harb ؓ, who had killed Hamza ؓ at Uhud before he was a Muslim. "
             "His javelin went through and out the other side; a second man came up with a "
             "sword. Sources differ on who the second man was — say 'a second man'. "
             "Afterwards Khalid ؓ walked the dead with the prisoner to identify the body.")

    # ================================================================ ACT 4
    D.section_slide(prs, "What it cost, and what it produced", "Act Four  ·  12 AH")

    stmt(prs, 16, headline="And Allah knows best",
         say="[HANDS] Ask first: if every copy of a book you loved lived only in people's "
             "memories, how many funerals would it take to lose it? Ibn Kathir's phrase is "
             "istaharra al-qatl fi al-qurra' — the killing ran hot among the reciters. "
             "NEVER put a number of qurra' on the slide; no source we use gives one.")

    stmt(prs, 17, headline="A thing the Messenger ﷺ did not do",
         say="Zayd b. Thabit ؓ of Banu al-Najjar: eleven years old when the Prophet ﷺ "
             "reached Medina, seventeen suras memorised before he was introduced, learned the "
             "Jews' script in a fortnight, wrote the revelation down as it came. His objection "
             "is the most serious objection there is.")

    s = D.image_slide(prs, "l02_four_materials.png", "There was no volume to copy from",
                      kicker="Card 18  ·  12 AH",
                      caption="Parchment, shoulder-blades, palm-stalks — and the breasts of "
                              "men.",
                      brief="Restrained editorial still life in muted ochre, bone and deep teal, "
                            "laid out on a plain scrubbed wooden surface and seen from directly "
                            "above. Four kinds of thing set well apart from one another: strips "
                            "of aged parchment; two flat dried animal shoulder-blades; several "
                            "bare stripped date-palm stalks; and a few thin flat white stones. "
                            "Any marks on them suggested only as faint illegible strokes, never "
                            "readable letters of any script. Soft even daylight, quiet shadows, "
                            "generous empty space between the four groups. No people, no hands, "
                            "no faces. 16:9 landscape.")
    D.note(s, "[HANDS] Say the four once, then ask the room to name them back to you. It is the "
              "one line in the evening everybody will remember. Ibn Kathir names al-likhaf "
              "— the thin white stones — where al-Dhahabi names al-riqa'. Cite both if "
              "you use both.")

    stmt(prs, 18, headline="He tracked it down, piece by piece",
         say="The verb in his own account is tatabba'a — to follow a thing up piece by "
             "piece. Then it was one set of suhuf, in one place, for the first time.")

    # ================================================================ ACT 5
    D.section_slide(prs, "Arabia whole again", "Act Five  ·  12 AH")

    s = D.map_slide(prs, "map_s2_darin.png", "Darin — into the water",
                    kicker="Card 19  ·  11–12 AH",
                    keys=[("al-Bahrayn", "the beaten take ship from the coast"),
                          ("The land roads", "closed first, by Bakr b. Wa'il"),
                          ("Darin", "a day and a night out by sea"),
                          ("Straight across the water", "out and back in a single day"),
                          ("What was lost", "one man's horse-fodder, brought back to him")])
    D.note(s, "Both books describe the crossing the same way: they walked on something like "
              "soft sand with water over it, not deep enough to reach the camels' pads. "
              "al-Bidaya vol. 7 p. 40 prints the du'a they said going in.")

    stmt(prs, 19, headline="Go straight across the sea",
         say="He closed the roads behind the enemy before he opened one in front of himself.")

    s = D.map_slide(prs, "map_s2_arabia_12ah.png", "Arabia whole again",
                    kicker="11 AH → 12 AH",
                    keys=[("Every region", "no part of the peninsula was untouched"),
                          ("The armies", "sent to support believers already there"),
                          ("The fifth of the spoils", "came back to Medina and was spent"),
                          ("Najran", "renewed its covenant while others broke theirs"),
                          ("A little over one year", "late 11 AH into early 12 AH")])
    D.note(s, "This is Ibn Kathir's own summing-up, not ours. He does not describe a conquest. "
              "One colour, no arrows: hold on this map and let them look at it.")

    stmt(prs, 20, headline="What Ibn Kathir says it was", arabic=AR20,
         say="The armies were sent to hold up people who were already standing. The whole thing "
             "was over in a little more than a year. The full passage is in the briefing.")

    stmt(prs, 21,
         say="[HANDS] Ask first: two years after the tribes broke apart, they were moving on two "
             "empires — what had changed? His answer multiplies nobody's numbers. SAY HIS "
             "NAME and say 'as he reads it': he never wrote this about the ridda; joining his "
             "chapter to the year eleven is ours.")

    s = D.statement_slide(prs, english="Mark three places on the map. Write three years into the "
                                       "boxes.",
                          headline="Worksheet — 90 seconds", size=44)
    D.note(s, "[WORKSHEET] 90 seconds, silent. Say nothing at all while they write. Do not fill "
              "the silence. Watch the clock.")

    # ================================================================ ACT 6
    D.section_slide(prs, "Outward", "Act Six  ·  12–13 AH")

    stmt(prs, 22,
         say="Muharram 12 AH. The letter did not say 'conquer Iraq'. It said: come at Iraq from "
             "its lower end. Then two restrictions that are easy to miss — no man compelled "
             "to march, and no man used who had apostatised, even if he has come back.")

    s = D.map_slide(prs, "map_s2_iraq_sham_13ah.png", "Five days of waterless country",
                    kicker="Card 23  ·  13 AH",
                    keys=[("al-Hira", "Iraq entered from its lower end"),
                          ("Quraqir", "the march strikes north-west, off any road"),
                          ("The Samawa", "nine days say some; five nights say others"),
                          ("Suwa and Tadmur", "he comes out behind the Roman armies"),
                          ("The guide", "Rafi' b. Umayra al-Ta'i, whose eyes were bad")])
    D.note(s, "[HANDS] Ask: how do you carry water for an army across five days of desert with "
              "no wells? Take two answers, then tell them. The strongest camels made thirsty, "
              "then watered twice over, lips cut and mouths bound so they could not chew and "
              "lose the water; ten opened every day to water the horses. Length: al-Bidaya says "
              "nine days, al-Kamil and Siyar say five nights. Say both.")

    stmt(prs, 23, headline="Only once in my life",
         say="On the last stretch Rafi', whose eyes were bad, asked whether they could see a "
             "box-thorn bush the height of a seated man. They said no. He said: then by God you "
             "are dead, and I am dead with you. They looked again. It was there, cut to a stump. "
             "They dug at its root and found the spring.")

    stmt(prs, 24,
         say="Four commanders had come to the Yarmuk, each over his own men, nobody over all of "
             "them. He did not ask for the command; he proposed passing it round. They made him "
             "commander expecting it to last a long time. It lasted one day.")

    stmt(prs, 25, headline="Armies are made many by victory",
         say="[HANDS] Ask the room to guess the two army sizes. Take three guesses — then "
             "show that the books themselves give three different answers, and say why. A "
             "Christian Arab standing near him had said out loud what everyone could see.")

    # ================================================================ ACT 7
    D.section_slide(prs, "He dies", "Act Seven  ·  13 AH")

    stmt(prs, 26, headline="There is harshness in him",
         say="[HANDS] Before telling it: who here has worked with someone whose hardness was a "
             "response to somebody else's softness? He did not argue with the description. He "
             "explained it: when I was angry with a man, Umar ؓ showed me leniency; when I "
             "was gentle, he showed me severity.")

    stmt(prs, 27, headline="I have not appointed a relative over you",
         say="The document was finished and read out to the gathered people; Umar ؓ walked "
             "beside the freedman who carried it, telling the crowd to be quiet and listen. "
             "They said: we hear and we obey. Then he asked them a question nobody had asked "
             "him.")

    s = D.diagram_slide(prs, "What in the house was not his",
                        kicker="Card 28  ·  the last day",
                        rows=[("A servant", "an Abyssinian, in the house"),
                              ("A camel", "used for carrying water"),
                              ("A blanket", "worn down to the nap")],
                        caption="Send them to Umar when I die. And she did.")
    D.note(s, "He called A'isha ؓ and told her that since the day he took charge of the "
              "Muslims' affair he had not eaten a dinar or a dirham of theirs — only the "
              "coarsest of their food, only the roughest of their clothing. Then he listed "
              "these three.")

    stmt(prs, 28, headline="He closed the account himself")

    stmt(prs, 29, headline="Sell my land and pay them back",
         say="The community had voted him a maintenance when he gave up trading — a man "
             "cannot run a market stall and a state at once. NUMBER CAUTION: the sources give "
             "6,000 dirhams a year, half a sheep a day, and 2,500. Put no figure on the slide. "
             "The instruction is the point, not the amount.")

    stmt(prs, 30, headline="The living need the new more",
         say="He gave instructions for his own washing — his wife Asma' bint Umays ؓ, "
             "and his son Abd al-Rahman ؓ. Then the shroud: use the two garments I am "
             "wearing, and buy one more to go with them.")

    s = D.diagram_slide(prs, "Three graves, one behind the other",
                        kicker="Card 31  ·  13 AH",
                        rows=[("The Prophet ﷺ", "the first of the three"),
                              ("Abu Bakr ؓ", "his head at the Prophet's ﷺ shoulders"),
                              ("Umar ؓ", "later, his head at Abu Bakr's waist")],
                        caption="Four men went down: his son, Umar, Uthman and Talha.")
    D.note(s, "One sentence in Siyar fixes all three positions. CAUTION: do NOT claim the burial "
              "was 'in A'isha's ؓ house' from these pages — they say beside the "
              "Prophet ﷺ, and no more.")

    stmt(prs, 31, headline="Buried before morning came",
         say="Monday evening, eight nights remaining of Jumada al-Akhira 13 AH. Umar ؓ "
             "prayed over him in the Prophet's ﷺ mosque, four takbirs. Carried on the same "
             "bier the Prophet ﷺ had been carried on. He was sixty-three — the age at "
             "which the Prophet ﷺ died.")

    # ================================================================ the close
    s = D.timeline_slide(prs, "line_s2_lit.png", "What year are we in now?",
                         caption="11 AH to 13 AH. Two years and three months.",
                         kicker="Bookend out")
    D.note(s, "[HANDS 3] Ask it before you advance, and let them answer. Then show the Line. "
              "This slide opens session 3 unchanged.")

    s = D.map_slide(prs, "map_s2_close_13ah.png", "Where we stand now", kicker="13 AH",
                    keys=[("Arabia", "whole, and under one authority"),
                          ("Iraq", "entered from its lower end"),
                          ("Syria", "the armies are on the Yarmuk"),
                          ("The dashed outline", "where the map stood when you walked in")])
    D.note(s, "[BOOKEND OUT] Hold on this one. Let them compare it with slide 3 themselves. "
              "This slide opens session 3 unchanged.")

    D.lessons_slide(prs, LESSONS, headline="Tonight")

    D.question_slide(prs, "He said the office would take much of that hardness away. "
                          "Next week — did it?")

    return prs


# ============================================================================ main
if __name__ == "__main__":
    verify()
    if "--verify" in sys.argv:
        raise SystemExit(0)
    prs = build()
    D.save(prs, OUT)
