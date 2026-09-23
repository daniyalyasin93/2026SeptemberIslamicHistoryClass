# -*- coding: utf-8 -*-
"""Evening 4 — the lectern cue sheet, the audience worksheet, and the home briefing.

    python S04_kinda_butah_yamama/pack_data.py   # -> CUE.pdf (one page), WORKSHEET.pdf, BRIEFING.md + BRIEFING.pdf

The running order is RUNSHEET.md Parts I–IV, ending at STOP C (Daniyal's cut, 2026-09-22, DECISIONS.md #44).
Nothing on the cue sheet that can be read from somewhere else is typed here. The guards:

  * verify_arabic()   — every Arabic fragment on the cue sheet occurs, harakat aside, in the statement of the
                        card named beside it. Fragments are lifted from the pool, never typed from memory.
  * verify_coverage() — the beats name every card of Parts I–VIII, in runsheet order, and nothing
    else; 16–34 beats (the overflow behind the STOP C close is fourteen of them).
  * the CLOCK is computed from the runsheet's own Min column, scaled into the two story windows of the fixed
    shape (CLAUDE.md §2) and split at STOP B, where the worksheet falls on the room's pace.
  * the EARLY-CLOSE JUMPS are read from S04.pptx — the hidden slides whose notes open "BOOKEND OUT STOP A/B" —
    and the build fails if they are missing or not hidden.
  * the IBRAH column is the four lines of the deck's visible «Tonight» slide: the card ids are read from that
    slide's notes, the lines from the pool, and each line is checked against the slide's own text.
  * the WORKSHEET is the room's page: no Arabic script beyond the honorific marks, and no production apparatus.
  * BRIEFING.md is GENERATED from the cards themselves (their full pool text, in runsheet order, with the
    runsheet note on top), under a short opening written for this evening.

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
import bidi_fix                                                     # noqa: E402
sys.path.insert(0, HERE)
import build as S04                  # noqa: E402  — the bridges, one source for deck, cue and briefing

# a Windows console is cp1252: "→", "ؓ" and the Arabic in a progress line would crash the run
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(errors="replace")

RUNSHEET = os.path.join(HERE, "RUNSHEET.md")
DECK = os.path.join(HERE, "S04.pptx")
POOL = B.pool_cards()
PARTS = B.runsheet(RUNSHEET)
HARAKAT = re.compile("[ً-ْٰـ]")
ARABIC_LETTER = re.compile("[؀-ۿݐ-ݿࢠ-ࣿﭐ-﷏ﷰ-﷿ﹰ-﻿]")
HONORIFIC = re.compile("[ؓﷺ]")

# The fixed session shape, CLAUDE.md §2 (minutes from the start)
BOOKEND_IN, STORY_1, WORKSHEET_AT, STORY_2, CLOSE = 0, (4, 26), 26, (28, 40), 40


def ar(s):
    """An inline Arabic fragment inside an English cue line, isolated so bidi cannot reorder it."""
    return ("<span dir=\"rtl\" style=\"font-family:'Traditional Arabic',serif;font-size:1.4em;"
            "line-height:1;unicode-bidi:isolate\">%s</span>" % s)


# (card id, fragment) for every Arabic string on the cue sheet — checked by verify_arabic()
FRAG = {
    "half": ("ATA/E-TB15", "فإنّ لنا نِصْفَ الأمْرِ"),
    "patrol": ("RCT/E-RC47", "واختلفت السريةُ فيهم"),
    "erred": ("RCT/E-RC50", "تَأَوَّلَ فَأَخْطَأَ"),
    "honour": ("RCT/E-RC56", "اليوم يوم الغيرة"),
    "baqara": ("RCT/E-RC58", "يا أصحاب سورةِ البقرةِ"),
    "separate": ("RCT/E-RC19", "امْتَازُوا"),
    "throw": ("RCT/E-RC20", "أَلْقُونِي عَلَيْهِمْ"),
    "between": ("AHA/E-AS16", "فأضجعوني بينهما"),
    "banner": ("AHA/E-AS13", "فَوَقَعَتْ الرَّايَةُ، فَأَخَذَهَا سَالِمٌ"),
    "confirm": ("ZIA/E-ZY9", "أُصَدِّقَهُ مَيْتاً، كَمَا صَدَّقْتُهُ حَيّاً"),
    "honoured": ("ZIA/E-ZY4", "أكرم زيدًا بيدي"),
    "scent": ("RCT/E-RC23", "رِيْحَ زَيْدٍ"),
    "gathered": ("RCT/E-RC37", "من اللِّخاف والعُسُب وصدور الرجال"),
}
F = {k: ar(v[1]) for k, v in FRAG.items()}


# =========================================================================== what the runsheet and deck say

RUNSHEET_ROW = re.compile(r"^\|\s*(\d+)\s*\|\s*`([A-Z]+/E-[A-Z]+\d+)`[^|]*\|[^|]*\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*\|")
STOP_LINE = re.compile(r"STOP ([A-E]) — after #(\d+)")


def evening_ids():
    return [cid for _, rows in PARTS for cid, _ in rows]


def planned_ids():
    """Parts I–IV: the evening the clock is written for. Everything from Part V on sits behind the
    STOP C close and is outside the clock — named explicitly, because a prefix test on "Part V" also
    swallowed Parts IX–XI and put the houses back on the clock."""
    PLANNED = ("Part I", "Part II", "Part III", "Part IV")
    return [cid for part, rows in PARTS if part.split(" —")[0].strip() in PLANNED
            for cid, _ in rows]


def runsheet_rows():
    """{card id: (running number, budgeted minutes)} for the tables under '## Part' headings only."""
    out, live = {}, False
    for line in open(RUNSHEET, encoding="utf-8"):
        if line.startswith("## "):
            live = line.startswith("## Part")
            continue
        m = RUNSHEET_ROW.match(line) if live else None
        if m:
            out[m.group(2)] = (int(m.group(1)), float(m.group(3)))
    if list(out) != evening_ids():
        raise SystemExit("RUNSHEET minute rows and build_full_deck.runsheet() disagree on the evening's cards.")
    return out


def runsheet_stops():
    """{'A': (after #n, card id, clock threshold or None), ...} from the '⏸ STOP X — after #n' lines."""
    rows = runsheet_rows()
    by_n = {n: cid for cid, (n, _) in rows.items()}
    text = open(RUNSHEET, encoding="utf-8").read()
    live = text.split("\n## Rolled forward", 1)[0]
    out = {}
    for m in STOP_LINE.finditer(live):
        para = live[m.start():live.find("\n\n", m.start())]
        past = re.search(r"past (\d:\d\d)", para)
        out[m.group(1)] = (int(m.group(2)), by_n[int(m.group(2))], past.group(1) if past else None)
    for k in "ABCDE":
        if k not in out:
            raise SystemExit("RUNSHEET.md has no 'STOP %s — after #n' line." % k)
    return out


def deck_slides():
    """(jumps, tonight): the closing-set slide numbers by stop, and the visible «Tonight» slide."""
    from pptx import Presentation
    prs = Presentation(DECK)
    jumps, tonight = {}, []
    for i, s in enumerate(prs.slides, 1):
        notes = s.notes_slide.notes_text_frame.text.strip() if s.has_notes_slide else ""
        hidden = s._element.get("show") == "0"
        m = re.match(r"BOOKEND OUT STOP ([A-E])\b", notes)
        if m:
            jumps[m.group(1)] = (i, hidden)
        if "The true ending" in notes and not hidden:
            jumps["Q"] = i              # RC37's own slide: where Part VI is abandoned for the ending
        if notes.startswith("TONIGHT'S") and not hidden:
            text = " ".join(sh.text_frame.text for sh in s.shapes if sh.has_text_frame)
            # the notes carry the spoken lines, not card ids (#40); the ids are build.py's own list
            ids = (S04.LESSON_C, S04.LESSON_D, S04.LESSON_E)[len(tonight)]
            tonight.append((i, list(ids), text))
    for k in "AB":
        if k not in jumps:
            raise SystemExit("S04.pptx has no slide whose notes begin 'BOOKEND OUT STOP %s'." % k)
        if not jumps[k][1]:
            raise SystemExit("S04.pptx slide %d (STOP %s) is not hidden — an early close must be a jump." % (jumps[k][0], k))
    for k in "CDE":
        if k not in jumps or jumps[k][1]:
            raise SystemExit("S04.pptx must carry a VISIBLE STOP %s close (the planned end, and the end "
                             "of the overflow)." % k)
    if len(tonight) != 3:
        raise SystemExit("S04.pptx should carry three visible «Tonight» slides — STOP C, STOP D and "
                         "STOP E; found %d." % len(tonight))
    # where Part V starts: the slide after STOP C's four, which the cue sends the speaker to
    jumps["V"] = jumps["C"][0] + 4
    if "Q" not in jumps:
        raise SystemExit("No visible slide carries RC37's runsheet note, so Part VI has no way out.")
    return {k: (v[0] if isinstance(v, tuple) else v) for k, v in jumps.items()}, tonight[0]


def lessons_from_deck(tonight):
    num, ids, text = tonight
    flat = re.sub(r"\s+", " ", text)
    out = []
    for cid in ids:
        line = B.clean(POOL[cid]["ibrah"]).strip()
        if re.sub(r"\s+", " ", line) not in flat:
            raise SystemExit("The Ibrah of %s is not what slide %d shows." % (cid, num))
        out.append(line)
    if len(out) != 4:
        raise SystemExit("The «Tonight» slide names %d cards; the cue sheet expects four." % len(out))
    return out


def clocks(ws_after):
    """Each card's start, in minutes: the runsheet budget scaled into the two story windows.

    Part V is overflow, spoken only if the 45 minutes have not run out (#47), so it is outside the clock
    and its beats carry the marker "V" instead of a time."""
    rows, ids = runsheet_rows(), planned_ids()
    split = ids.index(ws_after) + 1
    out = {}
    for (lo, hi), chunk in ((STORY_1, ids[:split]), (STORY_2, ids[split:])):
        total, acc = sum(rows[c][1] for c in chunk), 0.0
        for c in chunk:
            out[c] = lo + acc * (hi - lo) / total
            acc += rows[c][1]
    return out


def hm(minutes):
    m = int(minutes + 0.5)
    return "%d:%02d" % (m // 60, m % 60)


# =========================================================================== the cue sheet

STOP = '<b style="color:#7A2E2E">STOP %s</b>'

# Headings, names, dates — no sentences (DECISIONS.md #22). A cue line ONLY for a warning or a jump: at one
# cue line per beat the sheet would not fit on one page even at 10pt, so the Arabic hooks ride in the beat
# names instead. The clock ("t") is filled in by build_run() for every beat that names cards.
BEATS = [
    {"t": hm(BOOKEND_IN), "name": "Line + MAP · back north to Khālid ؓ at Buzākha", "cards": []},
    {"name": "» back north · What does he ask for? · " + F["half"], "kind": "hands", "cards": ["ATA/E-TB15"]},
    {"name": "Palm-branch · Thābit ؓ, name only · Rabīʿa, Muḍar", "cards": ["ATA/E-TB16", "ATA/E-TB12"]},
    {"name": "Sajāḥ · Taghlib, not Tamīm · Thumāma ؓ · MAP", "cards": ["ATA/E-TB18", "ATA/E-TB19", "RCT/E-RC64"],
     "cues": ["⚠ nothing from pp. 29–30 · “the price he paid” · end on her Islam"]},
    {"name": "» after Buzākha · Anṣār hold back · Mālik ؓ apart · disperse", "cards": ["RCT/E-RC44", "RCT/E-RC45", "RCT/E-RC46"],
     "cues": ["⚠ PART II: between books, never a verdict · all or none"]},
    {"name": "Same story? · Abū Qatāda ؓ · " + F["patrol"], "kind": "hands", "cards": ["RCT/E-RC47"]},
    {"name": "One night, four accounts", "cards": ["RCT/E-RC48"],
     "cues": ["⚠ no cooking-pot · no verdict · side by side, then stop"]},
    {"name": "ʿUmar ؓ in the mosque · " + F["erred"] + " · Ibn Kathīr · Jadhīma", "cards": ["RCT/E-RC49", "RCT/E-RC50", "RCT/E-RC51"]},
    {"name": "ʿUmar ؓ and Mutammim", "cards": ["RCT/E-RC52"],
     "cues": ["⚠ not where Zayd ؓ fell"]},
    {"name": "» back to 11 AH · » meanwhile: ʿIkrima ؓ, Shuraḥbīl ؓ",
     "cards": ["RCT/E-RC63", "RCT/E-RC15", "RCT/E-RC53"]},
    {"name": "Villages behind his army? · 40,000 · MAP", "kind": "hands", "cards": ["RCT/E-RC54"]},
    {"name": "The prisoner in the tent · Mujjāʿa", "cards": ["RCT/E-RC16"],
     "cues": ["⚠ forty to sixty riders"]},
    {"t": hm(WORKSHEET_AT), "name": "WORKSHEET · 90 seconds, silent", "kind": "act", "cards": []},
    {"name": "» where we are · Order of battle · " + F["honour"], "cards": ["RCT/E-RC55", "RCT/E-RC56"],
     "cues": ["⚠ no diagram · “one of their leaders”"]},
    {"name": "The rout · two protections · al-Rajjāl", "cards": ["RCT/E-RC17", "RCT/E-RC57"],
     "cues": ["⚠ no ḥadīth for al-Rajjāl · Umm Tamīm ؓ: no link"]},
    {"name": F["baqara"] + " · Thābit's ؓ shroud", "cards": ["RCT/E-RC58", "RCT/E-RC18"]},
    {"name": "Sālim ؓ · Zayd ؓ · Abū Ḥudhayfa ؓ", "cards": ["RCT/E-RC59", "RCT/E-RC60", "RCT/E-RC61"]},
    {"name": "Khālid ؓ in the gap · " + F["separate"] + " · MAP",
     "cards": ["RCT/E-RC62", "RCT/E-RC19"]},
    {"t": hm(CLOSE), "name": "Line · MAP · Tonight · Next week", "cards": []},
    # Part V — the overflow, behind the STOP C close (#47). Spoken only if there is time.
    {"t": "V", "name": "» V · the garden · Musaylima killed · the forts · Zayd ؓ and ʿUmar ؓ",
     "cards": ["RCT/E-RC20", "RCT/E-RC21", "RCT/E-RC22", "RCT/E-RC23"], "kind": "hands",
     "cues": ["⚠ al-Barāʾ ؓ LIVED (80-odd wounds) · “a second man came up” · no ranking line · terms kept"]},
    # Parts VI-VIII are NOT cued beat by beat: 30 beats will not fit on one page, and the cue card is one
    # page or it is not a cue card (CLAUDE.md 1.7). Each part gets ONE digest line naming its cards in
    # order, with the part's ⚠ digest under it. The full beats live in the deck's own notes and BRIEFING.
    {"t": "V", "name": "» VI · banner → Sālim ؓ · one of four · the pit · hands + āya · «between them» · "
     "found together · 23 AH · the estate",
     "cards": ["AHA/E-AS13", "AHA/E-AS09", "AHA/E-AS14", "AHA/E-AS15", "AHA/E-AS16", "AHA/E-AS17",
               "AHA/E-AS18", "AHA/E-AS19"],
     "cues": ["⚠ no arrangement · four names off · pit = Thābit ؓ · 2nd man unnamed · no one grave · "
              "her name unread"]},
    {"t": "V", "name": "» VII · the pairs · Maʿn ؓ · <b>[HANDS]</b> the man who killed Zayd ؓ · the "
     "arrow · the chief's son · three generations · the mother · her other son · father and son",
     "cards": ["ZIA/E-ZY8", "ZIA/E-ZY9", "ZIA/E-ZY4", "ZIA/E-ZY12", "ZIA/E-ZY13", "ZIA/E-ZY14",
               "ZIA/E-ZY15", "ZIA/E-ZY18", "ZIA/E-ZY16"],
     "cues": ["⚠ no answer from ʿUmar ؓ · card's sentence only · “in this war” · ZY15 severe · "
              "ZY18 = 1 of 4 names · Yarmuk not yet"]},
    {"t": "V", "name": "» VIII · one who lived · ninety-odd · <b>[HANDS]</b> how many reciters? · "
     "«how do you do a thing he ﷺ did not do?» · THE QURʾĀN " + F["gathered"] + " → STOP E",
     "cards": ["THO/E-HS14", "THO/E-HS15", "ZIA/E-ZY17", "RCT/E-RC65", "RCT/E-RC37"],
     "cues": ["NO number exists · end on the Qurʾān, say nothing after it"]},
    # Parts IX-XI — the houses, PAST the close: evening 5's opening, or the fifteen minutes afterwards.
    # One line, not three: the cue card is one page (CLAUDE.md 1.7), and these are not tonight's evening.
    {"t": "V", "name": "» IX–XI, the houses · Umm Sulaym's ؓ (16) · Abū Ḥudhayfa ؓ + Sālim ؓ (9) · Thābit ؓ (1)",
     "cards": ["THO/E-HS1", "THO/E-HS2", "THO/E-HS3", "THO/E-HS4", "THO/E-HS5", "THO/E-HS6",
               "THO/E-HS8", "THO/E-HS11", "THO/E-HS12", "THO/E-HS9", "THO/E-HS10", "THO/E-HS7",
               "THO/E-HS13", "THO/E-HS17", "THO/E-HS18", "THO/E-HS19",
               "AHA/E-AS02", "AHA/E-AS01", "AHA/E-AS06", "AHA/E-AS07", "AHA/E-AS03", "AHA/E-AS04",
               "AHA/E-AS05", "AHA/E-AS10", "AHA/E-AS08", "ZIA/E-ZY10"],
     "cues": ["⚠ HS6 = Ibn Ishaq · do NOT name the child · no fleet and no commander · AS05/AS10 are "
              "YOUR call · narrate Badr, do not dwell"]},
]


def hon(s):
    """ؓ is a combining mark: on the space before it, it overhangs the space after it, and the next word
    runs into it ("Khālid ؓat"). A little right padding gives the gap back. Rendering only — the text is unchanged."""
    return s.replace(" ؓ", '<span style="padding-right:.3em"> ؓ</span>')


def build_run():
    """Fill in each beat's clock and attach the early-close jumps at the beat where each stop falls."""
    stops = runsheet_stops()
    jumps, _ = deck_slides()
    ws_after = stops["B"][1]                       # the worksheet falls at STOP B on the room's pace
    t = clocks(ws_after)
    run = []
    for b in BEATS:
        b = dict(b, cues=list(b.get("cues", [])))
        if b["cards"] and b["cards"][0] in t:
            b["t"] = hm(t[b["cards"][0]])
        for k in "AB":
            n, cid, past = stops[k]
            if cid in b["cards"]:
                if b["cards"][-1] != cid:
                    raise SystemExit("STOP %s falls inside a beat (after %s); it must end one." % (k, cid))
                when = ("past %s?" % past) if past else "short of time?"
                b["cues"].append("%s: %s type <b>%d</b> ↵" % (STOP % k, when, jumps[k]))
        if b.get("t") == "V":
            b["over"] = True                 # rendered dense: it is not part of the planned clock
            if not b["cards"][:1] == ["RCT/E-RC20"]:
                b["t"] = ""                  # only the first overflow beat carries the marker
        run.append(b)
    # going ON past the planned end is a typed number too: the close sits in the deck at that point
    for b in run:
        if b["cards"] and b["cards"][-1] == stops["C"][1]:
            b["cues"].append("%s in place · <b>going on? type %d</b> ↵"
                             % (STOP % "C", jumps["V"]))
    # STOP D sits IN PLACE after the terms at the forts: no number to type, but the speaker has to know
    # it is there, because the beat that holds it covers four cards
    for b in run:
        if stops["D"][1] in b["cards"]:
            b["cues"].append("%s is IN PLACE after the forts — a real ending if the clock is gone"
                             % (STOP % "D"))
    # Part VI can be abandoned at any point for the ending: one typed number, the same mechanism
    for b in run:
        if b["cards"][:1] == ["AHA/E-AS13"]:
            b["cues"].append("out of time anywhere below? <b>THE QURʾĀN: type %d</b> ↵" % jumps["Q"])
        if b["cards"][:1] == ["THO/E-HS1"]:
            b["cues"].append("these are PAST the close · to finish: <b>STOP E again, type %d</b> ↵"
                             % jumps["E"])
    # the worksheet beat must sit directly after the STOP B beat
    wi = next(i for i, b in enumerate(run) if b.get("kind") == "act")
    if not run[wi - 1]["cards"] or run[wi - 1]["cards"][-1] != ws_after:
        raise SystemExit("The WORKSHEET beat must follow the beat that ends at STOP B.")
    return run, stops, jumps


# One line each, facts only from the person's own cards (named in the trailing comment).
NAMES = [
    ("Musaylima", "Banū Ḥanīfa · 40,000 at ʿAqrabāʾ"),                  # RC64, RC54
    ("Sajāḥ", "Taghlib, from al-Jazīra · 11 AH"),                        # TB18
    ("al-Barāʾ b. Mālik ؓ", "Anas's ؓ brother · over the wall"),         # RC20
    ("Mālik b. Nuwayra ؓ", "Banū Yarbūʿ of Tamīm · al-Buṭāḥ, 11 AH"),    # RC45
    ("Abū Qatāda ؓ", "al-Ḥārith b. Ribʿī · the Prophet's ﷺ horseman"),   # RC47
    ("Mujjāʿa b. Murāra", "a chief of Banū Ḥanīfa · 11→12 AH"),          # RC16
    ("Thābit b. Qays ؓ", "orator of the Anṣār · Uḥud, Bayʿat al-Riḍwān"),  # RC18
    ("Sālim ؓ", "freedman of Abū Ḥudhayfa ؓ · Qubāʾ"),                   # RC59
    ("Zayd b. al-Khaṭṭāb ؓ", "ʿUmar's ؓ elder brother · one wing"),       # RC60
    ("Abū Ḥudhayfa ؓ", "his father fell at Badr, on the other side"),    # RC61
]


# =========================================================================== the worksheet

WS = {
    "session": "4",
    "title": "al-Buṭāḥ and al-Yamāma",
    "dates": "10–12 AH",
    "map": "map_arabia_blank.png",
    "map_task": "Madina (Medina) is printed. Mark al-Buṭāḥ and al-Yamāma (ʿAqrabāʾ) as they are named, and "
                "write the name beside each.",
    "timeline_boxes": ["end of 10 AH", "11 AH", "11 AH", "11→12 AH"],
    "tl_task": "Write the event above its date, in order, as we reach it: the letter from al-Yamāma · "
               "al-Buṭāḥ · Khālid ؓ at Medina · ʿAqrabāʾ.",
    # every word traceable to the cards named beside each (RC45–48, RC50 · RC16–17 · TB16, RC63, RC18)
    "people": [
        {"name": "Mālik b. Nuwayra ؓ",
         "dates": "Of Banū Yarbūʿ of Tamīm · al-Buṭāḥ, 11 AH",
         "did": "He told his own tribe to disperse and enter into this matter, then stood apart when the "
                "chiefs of Tamīm came in to Khālid ؓ, and was killed after a patrol took him — the books tell "
                "that night four ways, and Abū Bakr ؓ paid his blood-money."},
        {"name": "Mujjāʿa b. Murāra",
         "dates": "A chief of Banū Ḥanīfa · ʿAqrabāʾ, 11→12 AH",
         # only what the room has heard by STOP B, where the worksheet falls: the tent, not the rout
         "did": "Taken with a party of forty to sixty riders the night before the battle, he was kept alive, "
                "in irons, in Khālid's ؓ own tent."},
        {"name": "Thābit b. Qays ؓ",
         "dates": "The orator of the Anṣār · at Uḥud and Bayʿat al-Riḍwān · ʿAqrabāʾ, 11→12 AH",
         "did": "He stood beside the Prophet ﷺ when Musaylima came to Medina, and was put over the Anṣār "
                "for al-Yamāma."},
    ],
    "lesson_lines": ["", "", "", ""],
    "foot": "No questions during the session. Written slips into the box at the door — "
            "I will stay fifteen minutes afterwards.",
}

APPARATUS = re.compile(r"SOURCED|STANDARD|CONVENTIONAL|to verify|E-[A-Z]{2}\d|\[HANDS\]|\bn/a\b|Claude|Gemini|"
                       r"\bAI\b|https?:|IMAGE BRIEF|shamela|RUNSHEET|STOP [A-D]", re.I)


# =========================================================================== guards

def verify_arabic():
    bad = []
    for key, (cid, frag) in FRAG.items():
        src = HARAKAT.sub("", POOL[cid]["arabic"] or "")
        if HARAKAT.sub("", frag) not in src:
            bad.append("%s: «%s» is not in %s's statement" % (key, frag, cid))
    # and no Arabic script on the sheet that did not come through FRAG (honorific marks aside)
    for b in BEATS:
        for s in [b["name"]] + b.get("cues", []):
            for r in F.values():
                s = s.replace(r, "")
            if ARABIC_LETTER.search(HONORIFIC.sub("", s)):
                bad.append("Arabic script outside FRAG: %r" % s)
    for n, s in NAMES:
        if ARABIC_LETTER.search(HONORIFIC.sub("", n + s)):
            bad.append("Arabic script in the names column: %r" % n)
    if bad:
        raise SystemExit("Cue-sheet Arabic does not match the cards:\n  " + "\n  ".join(bad))
    print("%-34s %2d fragments, all found in their cards" % ("arabic", len(FRAG)))


def verify_coverage(run):
    want = evening_ids()
    have = [c for b in run for c in b.get("cards", [])]
    if have != want:
        raise SystemExit("Cue beats and RUNSHEET Parts I–IV differ.\n  not cued: %s\n  cued, not in the evening: %s"
                         "\n  (or the order differs)" % (sorted(set(want) - set(have)), sorted(set(have) - set(want))))
    if not 16 <= len(run) <= 34:
        raise SystemExit("The cue sheet holds 16-32 beats. It has %d." % len(run))
    # the numbered [HANDS] of Parts I–IV, and Part V's own (RC20's, marked [HANDS] 4 in the runsheet)
    kinds = [c for b in run if b.get("kind") == "hands" for c in b["cards"][:1]]
    if kinds != ["ATA/E-TB15", "RCT/E-RC47", "RCT/E-RC54", "RCT/E-RC20"]:
        raise SystemExit("The [HANDS] beats are TB15, RC47, RC54 and RC20 (RUNSHEET). The overflow's own "
                         "two — ZY4 and ZY17 — are marked inside the part digests. Cued: %s" % kinds)
    for mark in ("the man who killed Zayd", "how many reciters"):
        if not any("[HANDS]</b> " + mark[:12] in b["name"] for b in run):
            raise SystemExit("The overflow hands-up %r lost its [HANDS] mark on the cue sheet." % mark)
    clock = [b["t"] for b in run if ":" in b["t"]]          # "V" beats are outside the clock
    mins = [int(x.split(":")[0]) * 60 + int(x.split(":")[1]) for x in clock]
    if mins != sorted(mins):
        raise SystemExit("The clock runs backwards: %s" % clock)
    print("%-34s %2d cards covered by %d beats, in order" % ("coverage", len(want), len(run)))


def verify_worksheet():
    strings = [WS["title"], WS["dates"], WS["map_task"], WS["tl_task"], WS["foot"]] + WS["timeline_boxes"]
    for p in WS["people"]:
        strings += [p["name"], p["dates"], p["did"]]
    bad = [s for s in strings if ARABIC_LETTER.search(HONORIFIC.sub("", s)) or APPARATUS.search(s)]
    if bad:
        raise SystemExit("The worksheet is the room's page — Arabic script or apparatus in:\n  " + "\n  ".join(bad))
    if "ؓ" in WS["people"][1]["name"]:
        raise SystemExit("Mujjāʿa carries no honorific on our pages.")
    print("%-34s room-safe: English only, no apparatus" % "worksheet")


# =========================================================================== the briefing

def card_markdown(cid):
    """The card's full pool text, heading and all, from whichever pool holds it — laid out for reading.

    The pool writes a card's fields on consecutive lines, which Markdown runs into one paragraph: the beats
    were not a list and "Hands-up? no Cross-reference: …" read as one sentence. Each field now opens its own
    paragraph, and inline Arabic is isolated so a page like «ج۷ ص۳۳–۳۴» is not scrambled by the bidi
    algorithm (evening-4 review, 2026-09-22)."""
    for d in B.POOLS:
        txt = open(os.path.join(ROOT, d, "CONTENT.md"), encoding="utf-8").read()
        k = txt.find("\n### %s " % cid)
        if k >= 0:
            end = txt.find("\n### ", k + 5)
            nxt = txt.find("\n## ", k + 5)
            end = min(e for e in (end, nxt, len(txt)) if e > 0)
            md = txt[k + 1:end].strip().rstrip("-").strip()
            out = []
            for line in md.split("\n"):
                if out and out[-1] != "" and (re.match(r"\*\*[^*\n]{1,60}:?\*\*", line) or line.startswith("1. ")):
                    out.append("")
                out.append(line)
            return bidi_fix.process("\n".join(out))[0]
    raise SystemExit("card %s not found in any pool" % cid)


def briefing(stops, jumps):
    global NUM
    notes = {cid: n for _, rows in PARTS for cid, n in rows}
    NUM = {cid: i for i, cid in enumerate((c for _, r in PARTS for c, _ in r), 1)}
    rows = runsheet_rows()
    total = sum(m for _, m in rows.values())
    a, b = stops["A"], stops["B"]
    out = [
        "# Evening 4 — al-Buṭāḥ and al-Yamāma: speaker briefing", "",
        "Read this twice at home. Never at the lectern — the lectern carries CUE.pdf.", "",

        "**The evening.** Parts I–IV of `RUNSHEET.md`, %d cards, ending at STOP C (Daniyal's cut, 2026-09-22). "
        "It opens on evening 3's STOP B closing pair, unchanged — the Line at 11–12 AH with Yemen settled, and "
        "the map with Ṣanʿāʾ blue and Ḥaḍramawt still grey — and turns back north to Khālid ؓ, last seen at "
        "Buzākha. Ḥaḍramawt stays grey tonight. Part I introduces the two claimants still standing, Musaylima "
        "and Sajāḥ, so that nothing later has to refer forward. Part II is al-Buṭāḥ and the reckoning at Medina. "
        "Part III is the road to al-Yamāma, and ends with a prisoner in irons in Khālid's ؓ own tent. Part IV is "
        "the day at ʿAqrabāʾ, up to the order to separate out: the line has re-formed, every clan under its own "
        "banner, and the day is not yet decided. That is where the evening is planned to end, and its two "
        "closing slides open evening 5.\n\n"
        "**And behind that close, Part V** (#47): the rest of the day — the garden, the end of Musaylima, the "
        "terms at the forts, Zayd ؓ, and the order at Medina that gathered the Qurʾān. It is spoken only if "
        "there is time. The STOP C closing set stays in the deck where it is, so stopping needs no jump; "
        "going on is one typed slide number, and the cue sheet prints it." % len(rows), "",

        "**Size and pace.** About %g minutes as budgeted, for 34 story minutes. Evening 3 spoke 32 cards in "
        "the slot, so this is sized to the room's real pace, not the budget. The clock on the cue sheet is the "
        "budget scaled to that pace. If the clock runs ahead of the cards, drop GOOD cards in this order: "
        "#5, #4, #18, #21, #30, and #2 last — #26 closes the loop #2 opens. **Part II is all or nothing** — #7 to "
        "#15, or none of it." % total, "",

        "**The bridges.** Five slides are not cards: they close the seams where the story jumps in time, place "
        "or thread. Each shows three steps; say the line, then click on.", ""] + [
        "- Before #%d — *%s*: %s" % (NUM[cid], head, say.split("\n")[0])
        for cid, (head, _k, _r, say) in S04.BRIDGE_BEFORE.items()] + ["",

        "**The early closes.** STOP A falls after #%d (ʿUmar ؓ and Mutammim); STOP B after #%d (the prisoner in "
        "the tent). Their closing sets are hidden at the end of the deck: in the slide show, type **%d** and "
        "Enter for STOP A, **%d** and Enter for STOP B. If the clock is past %s at #%d, close at STOP B. On the "
        "room's pace STOP B is also where the worksheet falls: take the 90 silent seconds there, then open "
        "Part IV. If instead the clock is kind, type **%d** at the STOP C close and go on into Parts V–VIII, "
        "which end at STOP E. **You are not expected to reach the end of them.** If time runs out anywhere "
        "in there, do not hurry: type **%d**, take the muṣḥaf card and the close, and whatever was not "
        "reached opens evening 5."
        % (a[0], b[0], jumps["A"], jumps["B"], b[2] or "0:36", b[0], jumps["V"], jumps["Q"]), "",

        "**Parts VI–VIII — the dead of al-Yamāma (#36–#55).** This is what makes the ending land, and it "
        "is built to be stopped in the middle. The books give one reason for the ⁨جمع القرآن⁩ — that the "
        "killing ran hot among the reciters — and until the room has met a reciter that is a sentence, not "
        "a loss. Part IV has already put three of these men at the line (#28–#30).", "",
        "- **Part VI, the banner (#36–#43):** it falls from Zayd ؓ and Sālim ؓ picks it up (#36); Sālim ؓ is "
        "one of four the Prophet ﷺ named to take the Qurʾān from (#37); the pit (#38); both hands, and the "
        "āya Abū Bakr ؓ read to Medina the year before (#39); *lay me down between them* (#40); how they "
        "were found (#41); ʿUmar ؓ eleven years later (#42); the estate sent back (#43).",
        "- **Part VII, the men beside them (#44–#51):** the ⁨مؤاخاة⁩ pairs who died together, Maʿn ؓ, the man "
        "who killed Zayd ؓ and became a Muslim, Abū ʿAqīl ؓ, the son of the head of the hypocrites, four men "
        "of one Meccan household, Ḥabīb b. Zayd ؓ and his mother, and al-Ṭufayl ؓ and his son.",
        "- **Part VIII, what was left (#52–#55):** the man who went over the wall and lived, the number "
        "nobody can give, and the order at Medina. **#55 is the last word in every version of the "
        "evening.**", "",
        "**Nothing here is compressed to fit.** Whatever is not reached rolls into evening 5 "
        "(`DECISIONS.md` #20, #33), which still owes the room Ḥaḍramawt and Kinda.", "",

        "**Part II — how it is told.** al-Buṭāḥ and the reckoning at Medina (#7–#15) sits next to the disputes "
        "among the Companions. It is told straight, and it is told as a disagreement between books, never as a "
        "verdict. The guardrail installed in session 1 is what makes it tellable: a report of history is neither "
        "a ruling nor a creed, and we do not judge between Companions. The only verdicts on the page are Abū "
        "Bakr's ؓ, that Khālid ؓ interpreted and was mistaken (#13), and Ibn Kathīr's own sentence (#14) — "
        "neither is the speaker's. Close the part on consolation, not on blame (#15). **No questions from the "
        "floor.** Slips go into the box; the prepared answers are in `docs/catalogue/QA_BANK.md` §6.1, §6.2 and §6.9, "
        "the last being the entry on the woman in Khālid's ؓ tent at al-Yamāma (`DECISIONS.md` #41): the books give "
        "the same name in both places, and the connection is not made from the platform.", "",

        "**Say once, inside the story — at #10, as the patrol falls out.** This is where a listener asks "
        "\"how do we know?\", and the answer is the card itself: the disagreement is not between later "
        "historians, it is between the men who were standing there. Abū Qatāda ؓ testified that they had "
        "established the prayer; others in the same patrol said they had neither given the adhān nor prayed; "
        "and the books record both. So at #11 the four accounts go side by side, and we say what the card "
        "says: the books do not agree, and where they do not agree we record and we stop.", "",

        "**Things never to do.**", "",
        "- Do not choose one of the four accounts of the night at al-Buṭāḥ and tell it as what happened, and do "
        "not offer a defence or a charge that the books do not make.",
        "- Never speak the cooking-pot detail (al-Bidāya, vol. 7 p. 31). Graphic, adds nothing, turns an evening.",
        "- Never read, paraphrase or allude to the narrative of the two claimants' meeting (al-Bidāya, vol. 7 "
        "pp. 29–30). End Sajāḥ on her Islam in ʿUmar's ؓ days.",
        "- Do not connect the widow at al-Buṭāḥ with the woman in Khālid's ؓ tent at ʿAqrabāʾ. The books give "
        "the same name; the connection is not made from the platform (`DECISIONS.md` #41).",
        "- At #15, do not say where Zayd ؓ fell. #28 tells it, later the same evening.",
        "- At #20, say \"forty to sixty riders\". Do not fix a number.",
        "- At #22, say \"one of their leaders\". Three books name three men; do not pick.",
        "- At #24, do not use the ḥadīth attached to al-Rajjāl b. ʿUnfuwa — the editor marks its chain very weak.",
        "- At #21, no banner diagram. Three books arrange the same men three ways: name the men.",
        "- At #5, say \"the price he paid\", not \"dowry\" (`QA_BANK.md` §6.10). The face quotation ends before "
        "«إلى زمان معاوية» and beat 5 says \"for many years\": the room has not met him. Never \"a later "
        "caliph\" — it calls him caliph, which takes a side on khilāfa and mulk evenings before it is handled.",
        "- At #30, the watchword «يا محمداه» is off the face and off the cue: say it only as the army's battle-cry, "
        "recorded as history, or not at all (`QA_BANK.md` §6.11).",
        "- Four hands-up are asked BEFORE the click: #10 (the face shows both testimonies), and the maps before "
        "#6, #17 and #31, which show the answer. The notes say so on each slide.",
        "- The cards give Mujjāʿa b. Murāra, Mutammim and Sajāḥ no honorific. Do not add one.",
        "- **Part V, #32:** al-Barāʾ ؓ LIVED — eighty-odd wounds, and Khālid ؓ stayed a month treating "
     "them. Ibn Khaldūn seems to list him among the killed; the Siyar contradicts it. Never say he died there.",
        "- **Part V, #33:** say \"a second man came up\" — the books name different men (`QA_BANK.md` §5.3) "
     "— and do not use the Siyar line about \"the best of the people of the earth and the worst\".",
        "- **Part V, #33:** naming Waḥshī ؓ as the man who killed Ḥamza ؓ invites the obvious question. "
     "The prepared answer is `QA_BANK.md` §7.10: he was not a Muslim then, the Prophet ﷺ accepted his Islam, "
     "and the same spear killed Musaylima. Do not weigh or rank.",
        "- What is still held for evening 5, and is in this deck nowhere — not even in Part V: Ḥaḍramawt and "
        "Kinda; Thumāma's ؓ own story (one sentence of him at #6, no more); Bahrayn and Dārīn; and Ibn "
        "Kathīr's summing up of the whole war, which belongs after the last front, not before it.", "",
    ]
    n = 0
    for heading, part_rows in PARTS:
        out += ["## " + heading, ""]
        for cid, _ in part_rows:
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


# =========================================================================== build

def cue_data(run, lessons):
    return {
        "session": "4",
        "title": "al-Buṭāḥ and al-Yamāma",
        "dates": "10–12 AH · the two claimants, al-Buṭāḥ, the day at ʿAqrabāʾ",
        "runtime": "45 min · no Q&A",
        "run": [dict(b, name=hon(b["name"]), cues=[hon(c) for c in b.get("cues", [])]) for b in run],
        "names": [(hon(n), hon(s)) for n, s in NAMES],
        "lessons": [hon(x) for x in lessons],
    }


def ws_data():
    people = [{k: hon(v) for k, v in p.items()} for p in WS["people"]]
    return dict(WS, tl_task=hon(WS["tl_task"]), people=people)


if __name__ == "__main__":
    verify_arabic()
    run, stops, jumps = build_run()
    verify_coverage(run)
    verify_worksheet()
    _, tonight = deck_slides()
    lessons = lessons_from_deck(tonight)
    print("%-34s STOP A → %d · STOP B → %d · STOP C at %d · Tonight = slide %d"
          % ("deck", jumps["A"], jumps["B"], jumps["C"], tonight[0]))
    pack.cue(os.path.join(HERE, "CUE.pdf"), cue_data(run, lessons))
    pack.worksheet(os.path.join(HERE, "WORKSHEET.pdf"), ws_data())
    pack.briefing(briefing(stops, jumps))
