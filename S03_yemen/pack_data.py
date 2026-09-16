# -*- coding: utf-8 -*-
"""Evening 3 — the lectern cue sheet, the audience worksheet, and the home briefing.

    python S03_yemen/pack_data.py      # -> CUE.pdf (one page), WORKSHEET.pdf, BRIEFING.md + BRIEFING.pdf

The running order is RUNSHEET.md Parts I–III (Daniyal's cut, 2026-09-16). Three guards keep this file from
drifting away from it:

  * verify_arabic() — every Arabic fragment on the cue sheet must occur, harakat aside, in the statement
    of the card named beside it. Fragments are lifted from the pool, never typed from memory.
  * verify_coverage() — every card in Parts I–III must be named in some beat's `cards` list, and no beat
    may name a card outside them.
  * BRIEFING.md is GENERATED from the cards themselves (their full pool text, in runsheet order, with the
    runsheet note on top), so the prose Daniyal reads at home is exactly what the deck's notes carry.

English throughout (DECISIONS.md #19). Names are romanised; the only Arabic is verbatim from the cards.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "series"))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import pack                                                         # noqa: E402
import build_full_deck as B                                        # noqa: E402

POOL = B.pool_cards()
PARTS = B.runsheet(os.path.join(HERE, "RUNSHEET.md"))
HARAKAT = re.compile("[ً-ْٰـ]")


def ar(s):
    """An inline Arabic fragment inside an English cue line, isolated so bidi cannot reorder it."""
    return ("<span dir=\"rtl\" style=\"font-family:'Traditional Arabic',serif;font-size:1.2em;"
            "line-height:1;unicode-bidi:isolate\">%s</span>" % s)


# (card id, fragment) for every Arabic string below — checked by verify_arabic()
FRAG = {
    "rabbi": ("AAA/E-AW02", "ربِّي قد قتل الليلةَ ربَّه"),
    "kill": ("AAA/E-AW10", "أو قتله"),
    "tomorrow": ("AAA/E-AW11", "أنا قاتلُه غدًا"),
    "liar": ("AAA/E-AW14", "وأن عبهلة كذاب"),
    "yourland": ("TSY/E-YK03", "الْحَقُوا بِأَرْضِكُمْ"),
    "outward": ("RCT/E-RC32", "فقبل منهما علانيتهما"),
}
F = {k: ar(v[1]) for k, v in FRAG.items()}

CUE = {
    "session": "3",
    "title": "Yemen",
    "dates": "10–12 AH · al-Aswad al-ʿAnsī, and the second Yemen ridda",
    "runtime": "45 min · no Q&A",
    # A cue line only where it carries Arabic or a warning: at 20 two-line beats the sheet ran to two pages.
    "run": [
        {"t": "0:00", "name": "Where we stopped · Line + Buzākha → turn south", "cards": []},
        {"t": "0:03", "name": "Two bracelets · the Abnāʾ · Bādhām",
         "cards": ["ATA/E-TB17", "AAA/E-AW01", "AAA/E-AW02", "AAA/E-AW19"],
         "cues": [F["rabbi"] + " · kept over all Yemen"]},
        {"t": "0:07", "name": "Yemen divided · 10 AH · MAP", "cards": ["AAA/E-AW03"]},
        {"t": "0:09", "name": "ʿAbhala b. Kaʿb · Dhū al-Khimār", "cards": ["AAA/E-AW04"]},
        {"t": "0:11", "name": "Nights to Ṣanʿāʾ? · 25", "kind": "hands", "cards": ["AAA/E-AW05"]},
        {"t": "0:14", "name": "Governors scatter · commanders · letters", "cards": ["AAA/E-AW06", "AAA/E-AW07", "AAA/E-AW08"]},
        {"t": "0:20", "name": "Qays summoned · or kill him", "cards": ["AAA/E-AW09", "AAA/E-AW10"],
         "cues": [F["kill"]]},
        {"t": "0:24", "name": "A hundred beasts → WORKSHEET", "cards": ["AAA/E-AW11"], "cues": [F["tomorrow"]]},
        {"t": "0:28", "name": "The room · the lamp", "cards": ["AAA/E-AW12", "AAA/E-AW13"],
         "cues": ["⚠ who struck: books differ"]},
        {"t": "0:31", "name": "The dawn adhān · in al-Bukhārī", "cards": ["AAA/E-AW14", "AAA/E-AW20"], "cues": [F["liar"]]},
        {"t": "0:33", "name": "Nights before, or one", "cards": ["ATA/E-TB26", "AAA/E-AW15", "ABU/E-U9"],
         "cues": ["⚠ no verdict"]},
        {"t": "0:35", "name": "Days Muʿādh ؓ prayed? · 3", "kind": "hands", "cards": ["ATA/E-TB27", "AAA/E-AW16"]},
        {"t": "0:36", "name": "Qays turns · Khawlān", "cards": ["TSY/E-YK01", "RCT/E-RC31", "TSY/E-YK02", "TSY/E-YK03", "TSY/E-YK17"],
         "cues": [F["yourland"]]},
        {"t": "0:38", "name": "al-Muhājir ؓ · ʿIkrima ؓ · MAP", "cards": ["TSY/E-YK04", "TSY/E-YK05"]},
        {"t": "0:39", "name": "What will Abū Bakr ؓ do?", "kind": "hands", "cards": ["TSY/E-YK06", "TSY/E-YK18", "RCT/E-RC32"],
         "cues": [F["outward"]]},
        # Part III — past the 45-minute clock on any realistic pace: "III" marks beats reached only if cut
        {"t": "III", "name": "→ Kinda: the camels · Shadhra · MAP", "cards": ["TSY/E-YK07", "RCT/E-RC33", "TSY/E-YK08", "TSY/E-YK09"],
         "cues": ["al-Muhājir ؓ marches on from Ṣanʿāʾ · Ziyād b. Labīd ؓ"]},
        {"t": "III", "name": "Four kings · al-Nujayr · MAP", "cards": ["TSY/E-YK10", "TSY/E-YK11", "TSY/E-YK12", "RCT/E-RC34", "TSY/E-YK13"],
         "cues": ["⚠ say 11 or 12 AH · #41 off the slide"]},
        {"t": "III", "name": "al-Ashʿath at Medina · \"and I did\"", "cards": ["TSY/E-YK14", "POT/E-PG40", "TSY/E-YK16", "POT/E-PG41"]},
        {"t": "end", "name": "Line · MAP · Tonight · Next week", "cards": []},
    ],
    "names": [
        ("al-Aswad al-ʿAnsī", "Dhū al-Khimār · rose 10 AH · killed Rabīʿ I 11 AH"),
        ("Fayrūz al-Daylamī ؓ", "of the Abnāʾ · Khawlān"),
        ("Qays b. Makshūḥ", "one of the three · turned 11 AH"),
        ("al-Muhājir b. Abī Umayya ؓ", "Umm Salama's ؓ brother · 11 AH"),
        ("al-Ashʿath b. Qays ؓ", "Kinda · al-Nujayr, 11 or 12 AH · pardoned"),
    ],
    # the same four عبرت lines as the deck's STOP C closing slide (build.LESSON_CARDS_C), read from the cards
    "lessons": [B.clean(POOL[i]["ibrah"]) for i in ("AAA/E-AW10", "ATA/E-TB27", "RCT/E-RC32", "POT/E-PG41")],
}

WS = {
    "session": "3",
    "title": "Yemen",
    "dates": "10–12 AH",
    "map": "map_arabia_blank.png",
    "map_task": "Mark Ṣanʿāʾ, Najrān and Ḥaḍramawt as they are named, and write the name beside each.",
    "timeline_boxes": ["10 AH", "Rabīʿ I 11 AH", "Rabīʿ I 11 AH", "11 or 12 AH"],
    "tl_task": "Write the event above its date, in order, as we reach it: Ḥajjat al-Wadāʿ · al-Aswad killed · "
               "the Prophet ﷺ dies · al-Nujayr.",
    "people": [
        {"name": "al-Aswad al-ʿAnsī",
         "dates": "Rose after Ḥajjat al-Wadāʿ, 10 AH · killed in Ṣanʿāʾ, Rabīʿ I 11 AH",
         "did": "ʿAbhala b. Kaʿb of ʿAns, called Dhū al-Khimār. He came out with seven hundred men, took "
                "Najrān in ten nights and Ṣanʿāʾ in twenty-five, and was killed in his own house three or "
                "four months later."},
        {"name": "Fayrūz al-Daylamī ؓ",
         "dates": "Of the Abnāʾ, the Persians of Ṣanʿāʾ · Rabīʿ I 11 AH",
         "did": "He went first through the wall into the room where al-Aswad slept. When Qays b. Makshūḥ "
                "turned on the Abnāʾ, he escaped to his mother's people in Khawlān."},
        {"name": "al-Muhājir b. Abī Umayya ؓ",
         "dates": "Brother of Umm Salama ؓ · sent to the Yemen, 11 AH",
         "did": "He had stayed behind from Tabūk and was forgiven when his sister spoke for him. Abū Bakr ؓ "
                "sent him down through Najrān to Ṣanʿāʾ, and the Yemen was restored. Then he went on to his own "
                "post over Kinda, and with Ziyād b. Labīd ؓ besieged al-Nujayr."},
    ],
    "lesson_lines": ["", "", "", "", ""],
    "foot": "No questions during the session. Written slips into the box at the door — "
            "I will stay fifteen minutes afterwards.",
}


def evening_ids():
    return [cid for _, rows in PARTS for cid, _ in rows]


def verify_arabic():
    bad = []
    for key, (cid, frag) in FRAG.items():
        src = HARAKAT.sub("", POOL[cid]["arabic"] or "")
        if HARAKAT.sub("", frag) not in src:
            bad.append("%s: «%s» is not in %s's statement" % (key, frag, cid))
    if bad:
        raise SystemExit("Cue-sheet Arabic does not match the cards:\n  " + "\n  ".join(bad))
    print("%-34s %2d fragments, all found in their cards" % ("arabic", len(FRAG)))


def verify_coverage():
    want = set(evening_ids())
    have = {c for b in CUE["run"] for c in b.get("cards", [])}
    if want != have:
        raise SystemExit("Cue beats and RUNSHEET Parts I–III differ.\n  not cued: %s\n  cued, not in the evening: %s"
                         % (sorted(want - have), sorted(have - want)))
    if not 16 <= len(CUE["run"]) <= 20:
        raise SystemExit("The cue sheet holds 16-20 beats. It has %d." % len(CUE["run"]))
    print("%-34s %2d cards covered by %d beats" % ("coverage", len(want), len(CUE["run"])))


def card_markdown(cid):
    """The card's full pool text, heading and all, from whichever pool holds it."""
    for d in B.POOLS:
        txt = open(os.path.join(ROOT, d, "CONTENT.md"), encoding="utf-8").read()
        k = txt.find("\n### %s " % cid)
        if k >= 0:
            end = txt.find("\n### ", k + 5)
            nxt = txt.find("\n## ", k + 5)
            end = min(e for e in (end, nxt, len(txt)) if e > 0)
            return txt[k + 1:end].strip().rstrip("-").strip()
    raise SystemExit("card %s not found in any pool" % cid)


def briefing():
    notes = {cid: n for _, rows in PARTS for cid, n in rows}
    out = ["# Evening 3 — Yemen: speaker briefing", "",
           "Read this twice at home. Never at the lectern — the lectern carries CUE.pdf.", "",
           "**The evening.** Parts I, II and III of `RUNSHEET.md`: al-Aswad al-ʿAnsī from the Persians of "
           "Yemen to the dawn adhān in Ṣanʿāʾ, then Qays b. Makshūḥ's turn against the Abnāʾ and the two men "
           "judged at Medina, then Kinda, al-Nujayr and al-Ashʿath's pardon. About 86 minutes of material "
           "(66 CORE) for 34 story minutes: drop GOOD cards first.", "",
           "**Say once, inside the story, at #17 (\"Whom Fayrūz killed in Yemen\"):** almost all of this scene-by-scene "
           "detail reaches the books through one transmitter, Sayf b. ʿUmar; the killing itself and "
           "Fayrūz's name are in al-Bukhārī.", "",
           "**Three things never to do.** Do not choose between the reports of who struck the blow, who "
           "called the adhān, or whether it was nights or one night before the Prophet's ﷺ death. Do not "
           "project or read out the words al-Aswad's own people used of him to save their lives. Do not "
           "give Qays b. Makshūḥ or ʿAmr b. Maʿdī Karib an honorific — their standing is not settled on our "
           "pages.", ""]
    n = 0
    for heading, rows in PARTS:
        out += ["## " + heading, ""]
        for cid, _ in rows:
            n += 1
            md = card_markdown(cid)
            first, _, rest = md.partition("\n")
            out.append("### %d. %s" % (n, first[4:].split(" · ", 1)[-1]))
            out.append("")
            if notes.get(cid):
                out += ["**Runsheet:** " + notes[cid], ""]
            out += [rest.strip(), "", "---", ""]
    path = os.path.join(HERE, "BRIEFING.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print("%-34s %2d cards" % ("BRIEFING.md", n))
    return path


if __name__ == "__main__":
    verify_arabic()
    verify_coverage()
    pack.cue(os.path.join(HERE, "CUE.pdf"), CUE)
    pack.worksheet(os.path.join(HERE, "WORKSHEET.pdf"), WS)
    pack.briefing(briefing())
