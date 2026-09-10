"""Pull a chosen running order out of CONTENT.md into SPINE.md — the cards that become the lecture.

    python tools/extract_spine.py L02_baarah_saal

WHY. CONTENT.md is the over-built pool (DECISIONS.md #20) — 263 cards, ~464 minutes. The deck, the
briefing, the cue sheet and the worksheet are all written against a much smaller running order, and
every one of those artifacts needs the SAME running order or they will disagree. So the order is
declared once, here, and every builder reads SPINE.md.

Editing the running order means editing SPINE below and re-running. Nothing else changes.

The spine is a RECOMMENDATION, not a decision. Daniyal cuts further at the desk; the other 230-odd
cards stay in CONTENT.md and roll into later sessions rather than being compressed into this one.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --------------------------------------------------------------------------------------------
# SESSION 2 — «بارہ سال» becomes أبو بكر ؓ's caliphate entire: 11–13 AH, ending on his death.
#
# WHY THIS CUT. The room's verdict on session 1 was that it felt like a speed-run, and twelve years
# across two caliphates in forty-five minutes is exactly that. أبو بكر ؓ's caliphate ran two years
# and three months; it is a complete arc with a beginning (an army he would not recall), a crisis
# (Arabia breaks), a consequence (the Qur'an is bound), and an ending (he dies and hands over). It
# can be told slowly. عمر ؓ's 130 researched cards are not lost — they become sessions 3 and 4.
#
# Acts are the shape of the evening, not headings the audience sees.
# --------------------------------------------------------------------------------------------
# A card marked with a leading "*" is in the RECOMMENDED 45-MINUTE CUT. Everything else is the
# over-build (DECISIONS.md #20) and is there to be deleted. The four people strands are woven in
# at the exact points their own notes' "where each card belongs" tables specify — a household is
# only worth researching if the room meets it inside the story, not in an appendix.
SPINE = [
    ("ACT 1 \u00b7 The army he would not call back",
     "11 AH \u00b7 the first ten days", [
         "TMW/E-TRN1",   # أحد order of battle - the frame, planted BEFORE خالد ؓ is first named
         "*ABU/E-U1",    # the appointment nobody liked
         "*ABU/E-U3",    # "I will not untie a knot the Prophet ﷺ tied"
         "ABU/E-U4",     # the beard, and the man who would not be deposed
         "ABU/E-U5",     # the caliph on foot beside the mounted commander
         "*ABU/E-U6",    # forty days, and what the tribes concluded
     ]),

    ("ACT 2 \u00b7 Arabia comes apart",
     "11 AH", [
         "*RCT/E-RC01",  # the night raid on Medina - while the army is away
         "RCT/E-RC02",   # the counter-attack before dawn
         "*RCT/E-RC05",  # eleven banners at ذو القصّة   <- the map opens
         "RCT/E-RC06",   # the letter that went ahead of the armies
         "*TMW/E-TRN21", # the سيف الله hadith - said as خالد ؓ is given the command
         "*RCT/E-RC09",  # بُزاخة - the man who walked off the field
         "TMW/E-TRN13",  # بزاخة, the question
         "*RCT/E-RC10",  # the terms at Medina, and عمر ؓ's objection
     ]),

    ("ACT 3 \u00b7 اليمامة",
     "11\u201312 AH \u00b7 the hardest day of the war", [
         "*ZIA/E-ZY8",   # two brothers by appointment - tells the room to watch for households
         "AHA/E-AS02",   # أبو حذيفة ؓ, son of the elder of the جاهلية
         "AHA/E-AS04",   # the face at the well
         "AHA/E-AS06",   # سالم ؓ, from إصطخر
         "AHA/E-AS07",   # the imām at قباء - he carried the most Qur'ān
         "RCT/E-RC16",   # the tent and the prisoner - عَقْرَباء
         "*RCT/E-RC17",  # the line breaks
         "ZIA/E-ZY2",    # زيد بن الخطاب ؓ - the banner and the vow
         "ZIA/E-ZY10",   # "are you not content to live praised?"
         "*RCT/E-RC18",  # ثابت بن قيس ؓ puts on his shroud
         "AHA/E-AS11",   # "a wretched bearer of the Qur'ān"
         "AHA/E-AS12",   # "adorn the Qur'ān with deeds"
         "ZIA/E-ZY11",   # the armour in the cooking pot - and أبو بكر ؓ's ruling
         "*THO/E-HS4",   # أنس بن النضر ؓ at أحد - "I find the scent of Paradise"
         "THO/E-HS5",    # known by his fingertips
         "THO/E-HS15",   # "do you see me dying in my bed?"
         "*RCT/E-RC20",  # حديقة الموت - البراء ؓ over the wall
         "*THO/E-HS16",  # whose son he is - the family sentence, same beat as the wall
         "ZIA/E-ZY12",   # أبو عقيل ؓ, the arrow he pulled out
         "*AHA/E-AS16",  # "lay me down between them"
         "AHA/E-AS17",   # how they were found
         "ZIA/E-ZY15",   # the mother at اليمامة
         "*RCT/E-RC21",  # the death of مسيلمة, and what وحشي ؓ said afterwards
         "TMW/E-TRN4",   # the same spear
         "TMW/E-TRN5",   # وحشي ؓ on مسيلمة's men
         "ZIA/E-ZY5",    # «سبقني إلى الحسنيين»
         "*ZIA/E-ZY6",   # the east wind - عمر ؓ on his brother
     ]),

    ("ACT 4 \u00b7 What اليمامة cost, and what it produced",
     "12 AH", [
         "*ZIA/E-ZY17",  # the number nobody can give - the honesty beat, BEFORE the collection
         "ABU/E-Q1",     # the killing ran hot among the reciters
         "AHA/E-AS09",   # take the Qur'ān from four - the sentence that makes the next card land
         "*ABU/E-Q2",    # "how can we do a thing the Messenger ﷺ did not do?"
         "*ABU/E-Q3",    # parchment, shoulder-blades, palm-stalks, and the breasts of men
     ]),

    ("ACT 5 \u00b7 Arabia whole again",
     "12 AH", [
         "RCT/E-RC27",   # دارين - into the water
         "TMW/E-TRN9",   # عكرمة ؓ - "not until you have proved yourself"
         "TMW/E-TRN10",  # the muṣḥaf
         "*TMW/E-TRN14", # طليحة ؓ comes back - the evening must NOT end with him fleeing
         "*RCT/E-RC36",  # what Ibn Kathīr says the whole war was
         "*IKO/E-IKR1",  # ⭐ Ibn Khaldūn: the call does not add numbers, it removes rivalry
     ]),

    ("ACT 6 \u00b7 Outward",
     "12\u201313 AH", [
         "ISA/E-C1",     # the order to Iraq
         "TMW/E-TRN19",  # أبو بكر ؓ walks beside the stirrup
         "ISA/E-C5",     # the march across the waterless desert
         "ISA/E-C9",     # خالد ؓ hands the command round
         "ISA/E-C10",    # "armies are made many by victory"
     ]),

    ("ACT 7 \u00b7 He dies",
     "13 AH", [
         "ABD/E-B3",     # he asks عبد الرحمن بن عوف ؓ about عمر ؓ
         "ABD/E-B7",     # "I have not appointed a relative over you"
         "*ABD/E-B9",    # the list of what he owned
         "*ABD/E-B11",   # sell my land and pay them back
         "ABD/E-B14",    # the shroud
         "*ABD/E-B15",   # Monday night, and a grave already dug beside another
         "*AHA/E-AS18",  # "had Sālim ؓ been alive" - ۱۲ھ still being counted in ۲۳ھ
     ]),
]

# The three planned interaction beats (DECISIONS.md #24). Placed by act, not by clock, so that
# moving a card does not orphan them.
HANDS = {
    "ABU/E-U1": "Hands up — how long do you think أبو بكر ؓ was caliph, in total? "
                "(Two years and three months. Everything tonight happens inside that.)",
    "RCT/E-RC05": "Hands up — Medina is one town. How many armies would you send out at once?",
}
WORKSHEET_AFTER = "IKO/E-IKR1"      # the 90-second silent fill lands at the end of ACT 5
FINAL_HANDS = "Hands up — what year are we in now?"

CARD = re.compile(r"^### (\S+)\s*·\s*(.*?)\s*$", re.M)


def main(session_dir):
    src = os.path.join(ROOT, session_dir, "CONTENT.md")
    txt = open(src, encoding="utf-8").read()
    hits = list(CARD.finditer(txt))
    pool = {}
    for i, m in enumerate(hits):
        body = txt[m.end():hits[i + 1].start() if i + 1 < len(hits) else len(txt)].rstrip()
        pool[m.group(1)] = (m.group(2), body)

    out, n, missing, starred = [], 0, [], []
    out.append("""# Session 2 — the running order

**أبو بكر الصدیق ؓ's caliphate entire: 11–13 AH / 632–634 CE.** A 45-minute slot; this is about
70 minutes of material, deliberately (`DECISIONS.md` #20).

> **THIS FILE IS THE SINGLE SOURCE OF THE RUNNING ORDER.** The deck, the briefing, the cue sheet
> and the worksheet are all built from it, so they cannot disagree. To change the order, edit
> `tools/extract_spine.py` and re-run it — never edit this file by hand.

**Why this cut.** The room said session 1 felt like a speed-run. Twelve years across two caliphates
in forty-five minutes is exactly that. أبو بكر ؓ was caliph for two years and three months, and that
is a complete arc: an army he refused to recall, Arabia breaking apart, the Qur'an bound as a
consequence, and a death that hands the whole thing on. عمر ؓ's 130 researched cards are not lost —
they become sessions 3 and 4, already page-cited and waiting in `CONTENT.md`.

**Interaction (`DECISIONS.md` #24):** two hands-up beats inside the story, one at the close, and a
90-second silent worksheet fill at the end of ACT 5. No live Q&A.
""")

    for act, when, ids in SPINE:
        out.append("\n---\n\n## %s\n\n*%s*\n" % (act, when))
        for cid in ids:
            star = cid.startswith("*")
            cid = cid.lstrip("*")
            if cid not in pool:
                missing.append(cid)
                continue
            n += 1
            title, body = pool[cid]
            if cid in HANDS:
                out.append("\n> 🖐 **[HANDS]** %s\n" % HANDS[cid])
            out.append("\n### %d. %s%s · %s\n%s\n"
                       % (n, "\u2605 " if star else "", cid, title, body))
            if star:
                starred.append(cid)
            if cid == WORKSHEET_AFTER:
                out.append("\n> ✍ **[WORKSHEET — 90 seconds, silent]** Mark three places on the "
                           "blank map. Write the years into three of the six timeline boxes. "
                           "Say nothing while they write.\n")

    out.append("\n---\n\n## The close\n\n"
               "1. **The Line**, with tonight's events lit up and nothing else.\n"
               "2. **The Map**, at 13 AH, against where it stood when the room walked in.\n"
               "   *(Both of these open session 3 unchanged — `DECISIONS.md` #23.)*\n"
               "3. **Tonight's عبرت lines**, all on one screen.\n"
               "4. **[HANDS]** %s\n"
               "5. Next week, as a question.\n"
               "6. A loud السلام علیکم, then the dua.\n" % FINAL_HANDS)

    dst = os.path.join(ROOT, session_dir, "SPINE.md")
    with open(dst, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print("%-38s %d cards, ~%d min   |   \u2605 recommended cut: %d cards, ~%d min"
          % (os.path.relpath(dst, ROOT), n, round(n * 2.2), len(starred),
             round(len(starred) * 2.2)))
    if missing:
        print("   MISSING FROM POOL: " + ", ".join(missing))
    return dst


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "L02_baarah_saal")
