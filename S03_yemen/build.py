# -*- coding: utf-8 -*-
"""Build S03.pptx — evening 3, Yemen: al-Aswad al-ʿAnsī and the second Yemen ridda.

    python S03_yemen/make_timeline.py    # the Line images the bookends use (run first, or when dates move)
    python S03_yemen/make_maps.py        # the Map Studio scenes the map slides ask for
    python S03_yemen/build.py            # -> S03.pptx + S03.pdf + IMAGE_BRIEFS.md

RUNSHEET.md IS THE RUNNING ORDER, AND THIS FILE READS IT. Only the tables under `## Part` headings are
the evening (Daniyal's cut of 2026-09-16: Parts I–III, to STOP C — DECISIONS.md #34, #36). Each card comes
out of the era pools by id and becomes one slide through tools/build_full_deck.card_slide, the same
text-only path that built L02_ALL.pptx: the card's Arabic, rendering and citation on the face; its
narrative, date, map move, عبرت line and source in the notes. The runsheet's own Note column goes
into the notes first, so a [HANDS] beat or a ⚠ never has to be looked up.

WHAT THIS FILE ADDS AROUND THE CARDS.
  * Bookend IN — the opening Line (evening 2's events lit), evening 2's Buzākha map, and a map turning south.
  * A map slide wherever a Map Studio scene carries the story (MAP_BEFORE), with the scene file and
    steps in the notes. Maps are drawn in the tool, not here.
  * The floor-plan diagram before the room without a guard (a Gemini brief — it is not a map).
  * Bookend OUT for STOP C — the Line, the map, four عبرت lines, a question for next week.
  * The same closing set for STOP B and for STOP A, HIDDEN at the end of the deck (CLAUDE.md §2: a closing
    pair for every stopping point). Unhide and move one if the evening stops there.

TWO FACE RULES THIS FILE ENFORCES BEYOND deck2.audit().
  * AW13's statement is the widow telling the guards that al-Aswad is receiving revelation — words
    said to save lives, which must not be projected. It goes to the notes only (NO_FACE_ARABIC). An
    off-face card (AW13, and YK13 by its own ⚠ line) folds into its last beat before the quotation.
  * AW09's research title quotes al-Aswad's claim about "the angel"; a drop-in reading it cold would
    not know it is his claim. The face carries a plain headline instead (FACE_TITLE).
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "series"))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import deck2 as D                                                   # noqa: E402
import build_full_deck as B                                        # noqa: E402

VIS = os.path.join(HERE, "visuals")
SERIES_VIS = os.path.join(ROOT, "series", "visuals")
SCENES = "tools/mapstudio/scenes/"

NO_FACE_ARABIC = {"AAA/E-AW13"}
# AW13's face: one sentence of the card's own narrative, not the forbidden rendering. Used only if its last
# beat slide cannot be built; normally an off-face card folds into that beat (see build()).
FACE_TEXT = {"AAA/E-AW13": "At night they dug through the wall and went in."}
# plain headlines where the research title would mislead, mix scripts, or wrap into the body
FACE_TITLE = {
    "AAA/E-AW09": "Qays is summoned",
    "AAA/E-AW07": "His commanders, and Shahr's widow",
    "RCT/E-RC31": "Ṣanʿāʾ: the two women in the street",
    "ATA/E-TB27": '"No more than three days"',
    "RCT/E-RC32": "Abū Bakr ؓ judges the two men",
    "TSY/E-YK17": "The families brought back",
    "TSY/E-YK08": "The humbled man",
    "RCT/E-RC34": "al-Nujayr: the name he forgot to write",
    # AW05's title gives away [HANDS] 1 ("twenty-five to Ṣanʿāʾ") before the room is asked
    "AAA/E-AW05": '"You who rebel against us"',
    # TB26's title is Arabic only; the face carries its rendering instead
    "ATA/E-TB26": '"Al-ʿAnsī was killed last night"',
    # AW02's research title wraps English in «»; every other English face quote uses straight quotes
    "AAA/E-AW02": '"My Lord has killed your lord tonight"',
}
# the slide's date line is the first six words of a card's When — where that cut misleads, say it plainly.
# The cut counts a backticked certainty label as a word (so it ends in "…"), and «۱۱ھ» loses its ھ to the
# romaniser before " AH" is put in (so it reads a bare "11"). Every value below comes from the card's own When.
# AW19's When begins "the year 10 AH", which dates the Companions sent, not Bādhām's governorship.
FACE_WHEN = {
    "AAA/E-AW19": "from his Islam until his death",
    "ABU/E-U9": "end of Rabīʿ I, 11 AH",
    "ATA/E-TB17": "in the Prophet's ﷺ lifetime",
    "AAA/E-AW01": "shortly before the Prophet's ﷺ birth",
    "AAA/E-AW02": "in the Prophet's ﷺ Medinan years",
    "AAA/E-AW03": "the year 10 AH",
    "AAA/E-AW04": "after Ḥajjat al-Wadāʿ, 10 AH",
    # not "twenty-five nights": that is the answer to [HANDS] 1
    "AAA/E-AW05": "the first nights of his rising",
    "AAA/E-AW07": "during his three or four months",
    "AAA/E-AW08": "the Prophet's ﷺ last months",
    "AAA/E-AW09": "Ṣanʿāʾ, the days before the killing",
    "AAA/E-AW10": "Ṣanʿāʾ, the days before the killing",
    "AAA/E-AW11": "the last day before the killing",
    "AAA/E-AW13": "Rabīʿ I 11 AH",
    "AAA/E-AW15": "Rabīʿ I 11 AH",
    "AAA/E-AW16": "after the Prophet's ﷺ death",
    "AAA/E-AW20": "11 AH",
    "ATA/E-TB27": "Rabīʿ I 11 AH, Ṣanʿāʾ",
    "TSY/E-YK01": "after the Prophet's ﷺ death",
    "RCT/E-RC31": "11 AH, Yemen",
    "RCT/E-RC32": "11–12 AH",
    "TSY/E-YK04": "the Tabūk campaign, then 11 AH",
    "RCT/E-RC33": "11–12 AH, Ḥaḍramawt",
    "RCT/E-RC34": "11 or 12 AH",
    "TSY/E-YK16": "al-Qādisiyya to Nahāwand",
}
# YK10–13's When names الکامل and سیر in Arabic script; the face's romaniser drops them ("11 AH by 's arrangement")
for _cid in ("TSY/E-YK10", "TSY/E-YK11", "TSY/E-YK12", "TSY/E-YK13"):
    FACE_WHEN[_cid] = "11 or 12 AH"
# A rendering written with Arabic-script names inside the English scrambles under bidi, and the generic
# romaniser drops the names it does not know. U9 is the one such card tonight: romanised by hand, word
# for word from its pool rendering.
# The rest are verbatim excerpts of the card's own rendering, chosen so the face neither stops mid-clause
# nor runs a third line onto the citation. The full rendering stays in the notes.
FACE_ENGLISH = {
    "ABU/E-U9": "Abū Bakr ؓ sent out Usāma b. Zayd's ؓ army at the end of Rabīʿ al-Awwal, and news of "
                "al-Aswad's killing came at the end of Rabīʿ al-Awwal, after Usāma's ؓ departure — and that "
                "was the first victory Abū Bakr ؓ won, while he was in Medina.",
    # the pool loses TB17's rendering (its citation wraps onto an Arabic line, which ends the parse)
    "ATA/E-TB17": '"…the man of Ṣanʿāʾ and the man of al-Yamāma."',
    # AW15: both sides of the timing dispute must be on the face, not just the first
    "AAA/E-AW15": '"…some nights before the death of the Messenger of Allah ﷺ — and it is said, one night. '
                  'And Allah knows best."',
    "AAA/E-AW10": '"She said: or to kill him. I said: or to kill him. She said: yes — by Allah…"',
    "RCT/E-RC32": '"…he accepted their outward profession from them, entrusted their inward states to Allah…"',
    "AAA/E-AW14": '"…I bear witness that Muḥammad is the Messenger of Allah, and that ʿAbhala is a liar…"',
    "AAA/E-AW07": '"Her name was Zādh… a believer in Allah and His Messenger Muḥammad ﷺ, and one of the righteous."',
    "TSY/E-YK17": '"They met Qays short of Ṣanʿāʾ and fought hard; Qays\'s side was routed…"',
    "TSY/E-YK09": '"It is an ugly thing in free men to change sides…"',
    "TSY/E-YK16": '"We did suspect three men — and … found nothing to match their trustworthiness and their '
                  'abstinence…"',
    "ATA/E-TB27": '"…no more than three days before the news reached us of the death of the Messenger of Allah ﷺ."',
}
# a citation the pool parse cut short ("… Sahih al-Bukhari 4375, via" — the narrators were on the next line)
FACE_CITE = {"ATA/E-TB17": "al-Bidaya wa'l-Nihaya, vol. 5, p. 22 (Sahih al-Bukhari 4375)"}
# TB27's whole statement (238 characters) is over AR_SLIDE_MAX and would fall to an image placeholder. The
# face takes one verbatim clause of it, split at the card's own «، » — the clause FACE_ENGLISH renders.
FACE_ARABIC_CLAUSE = {"ATA/E-TB27": (3, "ثلاثةَ أيام")}
# al-Kāmil is cited in these cards with the Persian kāf (U+06A9), and tools/build_full_deck.TRANSLIT carries
# only the Arabic-kāf spellings, so cite_en dropped the book's name ("vol. 2, p. 196"). Added for this build;
# harmless once the shared table carries the same row.
_KAMIL = ("الکامل", "al-Kamil")
if _KAMIL not in B.TRANSLIT:
    B.TRANSLIT.append(_KAMIL)
# U+FDFF (the single-character ligature for عز وجل) has no glyph in Traditional Arabic or in any other
# permitted font on this machine — only the banned Jameel Noori Kasheeda carries it — and it has no Unicode
# decomposition. Spelling it out would be writing Arabic into a quotation, so the source text stays as
# it is and the slide is flagged in its notes for Daniyal to decide by hand.
LIGATURE_WARNING = ("⚠ FACE CHECK: this Arabic contains the ligature ﷿ (عز وجل), which projects as an "
                    "empty box in Traditional Arabic. Decide by hand before the evening.")

# card id -> (headline, scene file, steps, key rows) — the map slide goes BEFORE that card.
# A map may show the movement of the card it stands before, never a later card's: each scene is split
# across the cards whose events its steps draw.
MAP_BEFORE = {
    "AAA/E-AW01": ("The Persians of Yemen", "s03-01-the-persians-of-yemen.json", "1",
                   [("Ṣanʿāʾ", "the Abnāʾ")]),
    "AAA/E-AW02": ("The letter to Kisrā", "s03-01-the-persians-of-yemen.json", "2–3",
                   [("Kisrā", "the letter, and the order")]),
    "AAA/E-AW03": ("Yemen divided, 10 AH", "s03-02-yemen-in-10ah.json", "1–2",
                   [("Najrān", "ʿAmr b. Ḥazm ؓ"), ("Muʿādh ؓ", "the teacher")]),
    # steps 1–2 only: step 3 prints "25 nights", the answer to [HANDS] 1
    "AAA/E-AW05": ("al-Aswad rises", "s03-03-al-aswad-rises.json", "1–2",
                   [("Najrān", "first"), ("Ṣanʿāʾ", "then")]),
    "AAA/E-AW06": ("The governors scatter", "s03-03b-the-governors-scatter.json", "1–2",
                   [("Ḥaḍramawt", "Muʿādh ؓ, Abū Mūsā ؓ"), ("Medina", "ʿAmr b. Ḥazm ؓ")]),
    "AAA/E-AW08": ("The letters reach Ṣanʿāʾ", "s03-04-the-night-in-sana.json", "1–2",
                   [("Medina → Ṣanʿāʾ", "Wabr b. Yuḥannas")]),
    "ATA/E-TB26": ("Ṣanʿāʾ, Rabīʿ I 11 AH", "s03-04-the-night-in-sana.json", "3–4",
                   [("Ṣanʿāʾ", "al-Aswad killed")]),
    # the riders' news is U9's; TB26 has it reach the Prophet ﷺ that same night. No date on the key: the
    # reports differ on when it reached Medina.
    "ABU/E-U9": ("The news reaches Medina", "s03-04-the-night-in-sana.json", "5",
                 [("Ṣanʿāʾ → Medina", "the news")]),
    "TSY/E-YK01": ("Ṣanʿāʾ again, 11 AH", "s03-05-qays-and-the-abna.json", "1",
                   [("Ṣanʿāʾ", "Fayrūz ؓ · Qays")]),
    "RCT/E-RC31": ("Ṣanʿāʾ turns", "s03-05-qays-and-the-abna.json", "2",
                   [("Khawlān", "Fayrūz ؓ")]),
    "TSY/E-YK17": ("The convoys turned back", "s03-05-qays-and-the-abna.json", "3–4",
                   [("Aden", "the convoys"), ("Ṣanʿāʾ", "the clash")]),
    "TSY/E-YK05": ("Two armies come down", "s03-06-the-two-armies.json", "1–3",
                   [("Abyan", "ʿIkrima ؓ"), ("Najrān", "al-Muhājir ؓ")]),
    "TSY/E-YK07": ("Ḥaḍramawt and Kinda", "s03-07-hadramawt-and-kinda.json", "1",
                   [("Ḥaḍramawt", "Ziyād b. Labīd ؓ"), ("Kinda", "the zakāt camels")]),
    "TSY/E-YK10": ("Round their fires", "s03-07-hadramawt-and-kinda.json", "2–4",
                   [("Kinda", "the four kings"), ("al-Ashʿath", "rises")]),
    "TSY/E-YK11": ("The march on Kinda", "s03-07-hadramawt-and-kinda.json", "5–6",
                   [("al-Muhājir ؓ", "ahead, from Ṣanʿāʾ"), ("ʿIkrima ؓ", "the main body, behind him")]),
    "TSY/E-YK14": ("To Medina", "s03-08-al-ashath-to-medina.json", "1",
                   [("al-Ashʿath", "bound, to Abū Bakr ؓ")]),
}

# the عبرت lines for the closing slide, read from the cards so they cannot drift
# four, not six: these lines are sentences, and six of them overlap at the lessons slide's row height
LESSON_CARDS = ["AAA/E-AW10", "ATA/E-TB27", "TSY/E-YK01", "RCT/E-RC32"]        # STOP B
LESSON_CARDS_A = ["AAA/E-AW05", "AAA/E-AW10", "ATA/E-TB27", "AAA/E-AW16"]      # STOP A
LESSON_CARDS_C = ["AAA/E-AW10", "ATA/E-TB27", "RCT/E-RC32", "POT/E-PG41"]      # STOP C


def first_sentence(what, words=18):
    """The opening sentence of a card's narrative, short enough for a slide face."""
    s = what.split(". ")[0].rstrip(".") + "."
    return B.short(s, words)


def map_placeholder(prs, headline, scene, steps, keys, kicker=None):
    s = D.map_slide(prs, None, headline, keys=keys, kicker=kicker,
                    brief="MAP STUDIO, not Gemini: open %s%s, export step(s) %s, place here."
                          % (SCENES, scene, steps))
    D.note(s, "MAP: open %s%s in tools/mapstudio/index.html, export step(s) %s as PNG, and place them "
              "here (one slide per step if you want the build-up). Sites are approximate; tribal names "
              "are loose labels." % (SCENES, scene, steps))
    return s


def closing(prs, pool, line_png, scene, question, lesson_cards, keys, hidden=False, stop=""):
    made = []
    s = D.timeline_slide(prs, line_png, "Tonight on the Line")
    D.note(s, "BOOKEND OUT %s — the Line. Re-used verbatim as next evening's opening slide (DECISIONS.md #23)."
              % stop)
    made.append(s)
    made.append(map_placeholder(prs, "Where we stand", scene, "all", keys))
    lessons = [B.clean(pool[i]["ibrah"]) for i in lesson_cards]
    s = D.lessons_slide(prs, lessons)
    D.note(s, "TONIGHT'S عبرت — from " + ", ".join(lesson_cards))
    made.append(s)
    made.append(D.question_slide(prs, question))
    if hidden:
        for s in made:
            s._element.set("show", "0")
    return made


def build():
    pool = B.pool_cards()
    parts = B.runsheet(os.path.join(HERE, "RUNSHEET.md"))
    missing = [cid for _, rows in parts for cid, _ in rows if cid not in pool]
    if missing:
        raise SystemExit("RUNSHEET.md names cards that are not in any pool: %s" % missing)

    prs = D.deck()
    D.title_slide(prs, "Yemen", "10–12 AH", "Evening 3")

    # Bookend IN
    s = D.timeline_slide(prs, os.path.join(VIS, "line_s03_open.png"), "Where we stopped")
    D.note(s, "BOOKEND IN — or use evening 2's closing slide 39 from L02_ALL_DY.pptx, unchanged.\n"
              "Say: while Khālid ؓ was riding to Buzākha, the first of the four claims had already ended, "
              "far to the south. Tonight we go back and see how.")
    # evening 2's Buzākha map does not reach Yemen, so the turn south gets a map of its own
    s = D.map_slide(prs, os.path.join(SERIES_VIS, "map_s2_buzakha.png"), "Buzākha, 11 AH",
                    keys=[("Buzākha", "where we stopped")])
    D.note(s, "BOOKEND IN — the map the room last saw. Then turn to the south.")
    map_placeholder(prs, "Tonight: the south", "s03-00-turn-south.json", "1",
                    [("Buzākha", "where we stopped"), ("Ṣanʿāʾ", "tonight")])

    made = beats_made = 0
    no_beats = []
    for heading, rows in parts:
        title, _, rest = heading.partition(" — ")
        sub = rest.split(" (")[0] if rest else None
        sec = D.section_slide(prs, B.clean(sub or title, translit=True))
        if heading.startswith("Part III"):
            D.note(sec, "BRIDGE, one sentence: al-Muhājir ؓ did not stay in Ṣanʿāʾ — the Prophet ﷺ had appointed "
                        "him over Kinda, and Abū Bakr's ؓ order was to go on to that post afterwards.")
        for cid, runsheet_note in rows:
            if cid in MAP_BEFORE:
                h, scene, steps, keys = MAP_BEFORE[cid]
                map_placeholder(prs, h, scene, steps, keys)
            if cid == "AAA/E-AW12":
                d = D.image_slide(prs, None, "The one room without a guard",
                                  brief="A simple architectural floor plan seen from above: a walled house "
                                        "of several rooms, small guard marks ringing every room except one; "
                                        "that room's back wall faces a road. Line drawing, teal and ochre, "
                                        "no people, no text. 16:9.")
                D.note(d, "DIAGRAM for AAA/E-AW12 and AW13 — the floor plan the Map: line asks for.")
            c = pool[cid]
            if cid in FACE_TITLE:
                c = dict(c, title=FACE_TITLE[cid])
            if cid in FACE_WHEN:
                c = dict(c, when=FACE_WHEN[cid])
            if cid in FACE_ENGLISH:
                c = dict(c, english=FACE_ENGLISH[cid])
            if cid in FACE_CITE:
                c = dict(c, cite=FACE_CITE[cid])
            if cid in FACE_ARABIC_CLAUSE and c["arabic"]:
                k, must = FACE_ARABIC_CLAUSE[cid]
                clauses = c["arabic"].split("، ")
                if len(clauses) > k and must in clauses[k]:
                    c = dict(c, arabic=clauses[k])
                else:
                    print("   ⚠ %s: the Arabic clause for the face was not found; the card's statement is "
                          "unchanged" % cid)
            notes = ("RUNSHEET: " + B.clean(runsheet_note)) if runsheet_note else ""
            # notes_for() prints the face's short date; the card's own When, with its certainty label, stays in
            # the notes
            when_full = ("WHEN, as the card gives it: " + pool[cid]["when"]) if cid in FACE_WHEN else ""
            if when_full:
                notes = (notes + "\n\n" if notes else "") + when_full
            # a researcher's "⚠ NOT FOR THE SLIDE FACE" line keeps the statement in the notes only, and the
            # face carries the first sentence of the card's own narrative instead
            flagged = "NOT FOR THE SLIDE FACE" in (c.get("extra") or "")
            off_face = cid in NO_FACE_ARABIC or flagged
            face_text = FACE_TEXT.get(cid) or (first_sentence(c["what"]) if flagged else None)
            if c["arabic"] and "﷿" in c["arabic"] and not off_face:
                notes = LIGATURE_WARNING + ("\n" + notes if notes else "")
            # one slide per beat (DECISIONS.md #37), the card's quotation slide after beat `quote_after`.
            # A runsheet note "SKIP BEATS 3,4" drops beats another card on the same evening already tells;
            # the card keeps them for any other evening.
            sk = re.search(r"SKIP BEATS?:?\s*([\d,\s]+)", runsheet_note or "", re.I)
            skip = {int(x) for x in re.findall(r"\d+", sk.group(1))} if sk else set()
            qa = c["quote_after"]
            # the runsheet note ([HANDS], ⚠, "say 11 or 12 AH") rides on the card's FIRST BUILT slide — not on
            # beat 1, which a SKIP BEATS may have dropped. If every beat up to the quotation is skipped, the
            # card slide comes first and carries it.
            first = next((i for i in range(1, len(c["beats"]) + 1) if i not in skip), None)
            rs_note = ("RUNSHEET: " + B.clean(runsheet_note)) if runsheet_note else ""
            # An off-face card has no quotation to show, and its face sentence repeats one of its own beats. So
            # when the beat before the quotation is built, the card folds into it: that slide takes the card's
            # notes, and no separate card slide is made.
            fold = bool(off_face and c["beats"] and qa and qa not in skip)
            qa_slide = None
            for i in range(1, qa + 1):
                if i in skip:
                    continue
                extra = [rs_note] if rs_note and i == first else []
                if fold and i == qa:
                    extra += [x for x in (when_full, B.notes_for(c)) if x]
                s = B.beat_slide(prs, c, i, "\n\n".join(extra))
                beats_made += bool(s)
                if i == qa:
                    qa_slide = s
            if fold and qa_slide is not None:
                card_built = True
            else:
                card_built = bool(B.card_slide(prs, c, extra_notes=notes, arabic_on_face=not off_face,
                                               face_text=face_text))
            made += card_built
            for i in range(qa + 1, len(c["beats"]) + 1):
                if i not in skip:
                    beats_made += bool(B.beat_slide(prs, c, i, rs_note if rs_note and i == first
                                                    and not card_built else ""))
            if not c["beats"]:
                no_beats.append(cid)

    # STOP C closes the evening as planned; B and A are built too, hidden, for an evening that stops early
    closing(prs, pool, os.path.join(VIS, "line_s03_stop_c.png"), "s03-close-stop-c.json",
            "Of the four claimants, two are still to be told: Musaylima in al-Yamāma, Sajāḥ from al-Jazīra. "
            "What became of them?",
            LESSON_CARDS_C, [("The south", "restored"), ("al-Yamāma", "where the story goes next")],
            stop="STOP C")
    closing(prs, pool, os.path.join(VIS, "line_s03_stop_b.png"), "s03-close-stop-b.json",
            "Ḥaḍramawt had stayed quiet all this time. What made Kinda break?",
            LESSON_CARDS, [("Ṣanʿāʾ", "restored"), ("Ḥaḍramawt", "still to come")], hidden=True, stop="STOP B")
    closing(prs, pool, os.path.join(VIS, "line_s03_stop_a.png"), "s03-close-stop-a.json",
            "One of the three men who killed al-Aswad wanted Yemen for himself. What did he do?",
            LESSON_CARDS_A, [("Ṣanʿāʾ", "the news of the death arrives")], hidden=True, stop="STOP A")

    out = os.path.join(HERE, "S03.pptx")
    # S03.pptx is Daniyal's hand-finished deck (DECISIONS.md #38). While S03.FINAL exists a rebuild writes
    # beside it and never over it.
    if os.path.exists(os.path.join(HERE, "S03.FINAL")):
        out = os.path.join(HERE, "S03_rebuild.pptx")
        print("   S03.FINAL present: writing S03_rebuild.pptx, leaving the finished S03.pptx untouched")
    D.save(prs, out)
    D.write_briefs(os.path.join(HERE, "IMAGE_BRIEFS.md"))
    n = sum(len(r) for _, r in parts)
    print("   %d of %d runsheet cards became slides · %d beat slides · %d slides in all (8 hidden: the STOP A "
          "and STOP B closes)" % (made, n, beats_made, len(prs.slides)))
    if no_beats:
        print("   %d cards have no **Beats:** yet: %s" % (len(no_beats), " ".join(no_beats)))
    return out


if __name__ == "__main__":
    build()
