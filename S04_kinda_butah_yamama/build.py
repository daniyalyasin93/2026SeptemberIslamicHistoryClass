# -*- coding: utf-8 -*-
"""Build S04.pptx — evening 4: the Kinda ridda, al-Buṭāḥ, and the road to al-Yamāma.

    python S04_kinda_butah_yamama/build.py          # -> S04.pptx + S04.pdf + IMAGE_BRIEFS.md

RUNSHEET.md IS THE RUNNING ORDER, AND THIS FILE READS IT. Only the tables under `## Part` headings are
the evening. Each card comes out of the era pools by id and becomes **ONE SLIDE** through
tools/build_full_deck.card_slide.

THIS DECK IS BUILT ONE SLIDE PER CARD (DECISIONS.md #39), NOT ONE SLIDE PER BEAT.
Evening 3 was delivered from a 356-slide beat deck and the shape failed in the room: consecutive beat
slides restated the same scene in slightly different words, and the speaker — who tells an event whole
from its first slide — was left visibly clicking past his own deck. So `beat_slide` is not called here.
The card's beats go into the **speaker notes** of its one slide, as the numbered SAY list that
`build_full_deck.notes_for` now prints first (#40). The screen carries the picture; the speaker carries
the sequence.

WHAT THIS FILE ADDS AROUND THE CARDS.
  * Bookend IN — evening 3's STOP B closing pair, unchanged (#23), and one sentence to turn to Kinda.
  * A map slide wherever a Map Studio scene carries the story (MAP_BEFORE). Maps are drawn in the tool.
  * Bookend OUT for STOP C, the planned end — the Line, the map, the عبرت lines, a question.
  * The same closing set for STOP A, STOP B and STOP D, HIDDEN at the end of the deck (CLAUDE.md §2:
    a closing pair for every stopping point). Unhide and move one if the evening stops elsewhere.

ONE FACE RULE THIS FILE ENFORCES BEYOND deck2.audit().
  * `ATA/E-TB19`'s research title and narrative are clean, but the pages behind it are not: the
    meeting of the two claimants at البدایہ ج۷ ص۲۹–۳۰ is explicitly obscene. The card's own ⚠ carries
    that; the face is given a plain headline so nothing on screen invites the question.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "series"))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import deck2 as D                                                   # noqa: E402
import build_full_deck as B                                         # noqa: E402

VIS = os.path.join(HERE, "visuals")
SCENES = "tools/mapstudio/scenes/"

# al-Kāmil is cited in these cards with the Persian kāf (U+06A9); the shared TRANSLIT table carries only
# the Arabic-kāf spellings, so cite_en dropped the book's name. Same row S03's build added.
for _pair in (("الکامل", "al-Kamil"), ("البُطاح", "al-Butah"), ("النُّجَير", "al-Nujayr"),
              ("عَقْرَباء", "Aqraba"), ("مالك بن نويرة", "Malik b. Nuwayra"),
              ("الرَّجّال بن عُنْفوة", "al-Rajjal b. Unfuwa")):
    if _pair not in B.TRANSLIT:
        B.TRANSLIT.append(_pair)

# Plain headlines where the research title would mislead, mix scripts, or wrap onto two lines.
FACE_TITLE = {
    "RCT/E-RC33": "The she-camel called Shadhra",
    "TSY/E-YK08": "The humbled man",
    "RCT/E-RC34": "al-Nujayr: the name he forgot to write",
    "KTK/E-KD02": "al-Hira given, al-Hira taken back",
    "KTK/E-KD03": '"Far from us in lineage"',
    "KTK/E-KD06": '"The four kings"',
    "KTK/E-KD07": "al-Ashath after the pardon",
    "RCT/E-RC44": "The Ansar who would not march",
    "RCT/E-RC45": "Malik b. Nuwayra, standing apart",
    "RCT/E-RC48": "One night, four accounts",
    "RCT/E-RC51": "The historian's own verdict",
    # nothing on the face may invite a question about the pages behind this card
    "ATA/E-TB19": "What her claim was worth",
    "ATA/E-TB12": '"A liar of Rabia"',
    "RCT/E-RC53": "And then it happened again",
    "RCT/E-RC55": "The order of battle",
    "RCT/E-RC57": "The man who made the lie believable",
    "RCT/E-RC62": "Khalid between the lines",
}
# The face's date line is the first six words of the card's When; where that cut misleads, say it plainly.
FACE_WHEN = {
    "TSY/E-YK07": "11 AH, Hadramawt",
    "RCT/E-RC33": "11–12 AH, Hadramawt",
    "RCT/E-RC34": "11 or 12 AH",
    "TSY/E-YK16": "al-Qadisiyya to Nahawand",
    "KTK/E-KD01": "before Islam — an estimate",
    "KTK/E-KD02": "before Islam — an estimate",
    "KTK/E-KD03": "before Islam — an estimate",
    "KTK/E-KD05": "10 AH",
    "KTK/E-KD07": "12–40 AH",
    "RCT/E-RC44": "11 AH",
    "RCT/E-RC45": "11 AH",
    "RCT/E-RC46": "11 AH",
    "RCT/E-RC47": "11 AH",
    "RCT/E-RC48": "11 AH — the books disagree",
    "RCT/E-RC49": "11 AH, Medina",
    "RCT/E-RC50": "11 AH, Medina",
    "RCT/E-RC51": "the historian's own comment",
    "RCT/E-RC52": "ʿUmar's ؓ caliphate",
    "ATA/E-TB15": "the end of the year 10",
    "ATA/E-TB16": "in the Prophet's ﷺ lifetime",
    "ATA/E-TB12": "11–12 AH, al-Yamama",
    "ATA/E-TB18": "11 AH",
    "ATA/E-TB19": "11 AH, and afterwards",
    "RCT/E-RC15": "11 AH, al-Yamama",
    "RCT/E-RC53": "11 AH, al-Yamama",
    "RCT/E-RC54": "11–12 AH",
    "RCT/E-RC16": "11–12 AH",
    "RCT/E-RC55": "11–12 AH — the books disagree",
    "RCT/E-RC56": "11–12 AH — attribution disputed",
    "RCT/E-RC17": "11–12 AH, Aqraba",
    "RCT/E-RC57": "11–12 AH, Aqraba",
    "RCT/E-RC58": "11–12 AH, Aqraba",
    "RCT/E-RC18": "11–12 AH, Aqraba",
    "RCT/E-RC59": "11–12 AH, Aqraba",
    "RCT/E-RC60": "11–12 AH, Aqraba",
    "RCT/E-RC61": "11–12 AH, Aqraba",
    "RCT/E-RC62": "11–12 AH, Aqraba",
    "RCT/E-RC19": "11–12 AH, Aqraba",
}

# card id -> (headline, scene file, steps, key rows). The map slide goes BEFORE that card, and shows only
# what that card's own events draw — never a later card's.
MAP_BEFORE = {
    "TSY/E-YK07": ("Hadramawt and Kinda", "s04-01-hadramawt-and-kinda.json", "1",
                   [("Hadramawt", "Ziyad b. Labid ؓ"), ("Kinda", "the zakat camels")]),
    "TSY/E-YK10": ("Round their fires", "s04-01-hadramawt-and-kinda.json", "2–4",
                   [("Kinda", "the four kings")]),
    "KTK/E-KD01": ("Kinda before Islam", "s04-02-kinda-before-islam.json", "1–2",
                   [("Yemen", "the house of Akil al-Murar"), ("Najd", "the tribes they were set over")]),
    "TSY/E-YK11": ("The march on Kinda", "s04-03-the-march-on-al-nujayr.json", "1–2",
                   [("al-Muhajir ؓ", "ahead, from Sanaa"), ("Ikrima ؓ", "the main body, behind him")]),
    "TSY/E-YK14": ("To Medina", "s04-04-al-ashath-to-medina.json", "1",
                   [("al-Ashath", "bound, to Abu Bakr ؓ")]),
    "RCT/E-RC44": ("From Buzakha to al-Butah", "s04-05-buzakha-to-al-butah.json", "1–2",
                   [("Buzakha", "where evening 2 stopped"), ("al-Butah", "the third stop in the orders")]),
    "RCT/E-RC49": ("Back to Medina", "s04-06-back-to-medina.json", "1",
                   [("al-Butah → Medina", "Khalid ؓ is sent for")]),
    "ATA/E-TB18": ("Sajah comes down from the north", "s04-07-sajah.json", "1–3",
                   [("al-Jazira", "where she came from"), ("al-Yamama", "where she turned back")]),
    "RCT/E-RC15": ("Two commanders sent ahead", "s04-08-the-road-to-al-yamama.json", "1–3",
                   [("Ikrima ؓ", "beaten, then sent south"), ("Shurahbil ؓ", "halted on the road")]),
    "RCT/E-RC54": ("Aqraba, and the ground behind it", "s04-09-aqraba.json", "1–2",
                   [("Aqraba", "the enemy camp"), ("the farmland", "behind their own line")]),
    "RCT/E-RC19": ("The line re-formed", "s04-09-aqraba.json", "3–4",
                   [("Muhajirun · Ansar · the tribes", "each under its own banner")]),
}

# The عبرت lines for each closing slide, read from the cards so they cannot drift.
# Four, not six: these lines are sentences, and six of them overlap at the lessons slide's row height.
LESSON_A = ["TSY/E-YK07", "TSY/E-YK09", "TSY/E-YK14", "POT/E-PG41"]                 # STOP A — Kinda closed
LESSON_B = ["TSY/E-YK14", "RCT/E-RC47", "RCT/E-RC50", "RCT/E-RC52"]                 # STOP B — al-Butah closed
LESSON_C = ["RCT/E-RC47", "RCT/E-RC50", "ATA/E-TB15", "RCT/E-RC54"]                 # STOP C — the planned end
LESSON_D = ["RCT/E-RC50", "RCT/E-RC54", "RCT/E-RC58", "RCT/E-RC19"]                 # STOP D — the day begins


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
    s = D.timeline_slide(prs, os.path.join(VIS, line_png), "Tonight on the Line")
    D.note(s, "BOOKEND OUT %s — the Line. Re-used verbatim as next evening's opening slide "
              "(DECISIONS.md #23)." % stop)
    made.append(s)
    made.append(map_placeholder(prs, "Where we stand", scene, "all", keys))
    s = D.lessons_slide(prs, [B.clean(pool[i]["ibrah"]) for i in lesson_cards])
    D.note(s, "TONIGHT'S عبرت — from " + ", ".join(lesson_cards))
    made.append(s)
    made.append(D.question_slide(prs, question))
    if hidden:
        for x in made:
            x._element.set("show", "0")
    return made


def build():
    pool = B.pool_cards()
    parts = B.runsheet(os.path.join(HERE, "RUNSHEET.md"))
    missing = [cid for _, rows in parts for cid, _ in rows if cid not in pool]
    if missing:
        raise SystemExit("RUNSHEET.md names cards that are not in any pool: %s" % missing)

    prs = D.deck()
    D.title_slide(prs, "Kinda, al-Butah, al-Yamama", "10–12 AH", "Evening 4")

    # Bookend IN — evening 3's STOP B pair, unchanged
    s = D.timeline_slide(prs, os.path.join(VIS, "line_s04_open.png"), "Where we stopped")
    D.note(s, "BOOKEND IN — or paste evening 3's STOP B Line slide from S03.pptx, unchanged "
              "(DECISIONS.md #23).\nSay: last week the south was settled as far as Ṣanʿāʾ — but "
              "al-Muhājir ؓ never stayed there. His appointment was over Kinda, and that is where "
              "tonight begins.")
    map_placeholder(prs, "Where we stand", "s04-00-where-we-stopped.json", "all",
                    [("Sanaa", "settled"), ("Hadramawt", "still grey")],
                    kicker="From last week")

    made = no_beats = 0
    for part, rows in parts:
        D.section_slide(prs, B.clean(part.split(" — ")[0], translit=True),
                        B.clean(part.split(" — ", 1)[1] if " — " in part else "", translit=True) or None)
        for cid, runsheet_note in rows:
            c = dict(pool[cid])
            if cid in FACE_TITLE:
                c["title"] = FACE_TITLE[cid]
            if cid in FACE_WHEN:
                c["when"] = FACE_WHEN[cid]
            if cid in MAP_BEFORE:
                head, scene, steps, keys = MAP_BEFORE[cid]
                map_placeholder(prs, head, scene, steps, keys)
            notes = ("RUNSHEET: " + B.clean(runsheet_note)) if runsheet_note else ""
            if cid in FACE_WHEN:
                notes = ((notes + "\n\n") if notes else "") + \
                        "WHEN, as the card gives it: " + pool[cid]["when"]
            # A researcher's "⚠ NOT FOR THE SLIDE FACE" keeps the statement in the notes only.
            off_face = "NOT FOR THE SLIDE FACE" in (c.get("extra") or "")
            face_text = B.short(c["what"].split(". ")[0].rstrip(".") + ".", 18) if off_face else None
            if B.card_slide(prs, c, extra_notes=notes, arabic_on_face=not off_face,
                            face_text=face_text):
                made += 1
            if not pool[cid]["beats"]:
                no_beats += 1

    # STOP C closes the evening as planned; A, B and D are built too, hidden, for another stopping point
    closing(prs, pool, "line_s04_stop_c.png", "s04-close-stop-c.json",
            "There is a man in irons in Khalid's ؓ own tent. Next week he saves a life, and then a life "
            "is saved for him.",
            LESSON_C, [("al-Yamama", "where the story goes next"), ("Najd", "settled behind the army")],
            stop="STOP C")
    closing(prs, pool, "line_s04_stop_a.png", "s04-close-stop-a.json",
            "Two of the four claimants are still to be told. One of them is in al-Yamama with forty "
            "thousand men. How did it get that far?",
            LESSON_A, [("the south", "restored"), ("al-Yamama", "still red")],
            hidden=True, stop="STOP A")
    closing(prs, pool, "line_s04_stop_b.png", "s04-close-stop-b.json",
            "Khalid ؓ keeps his command, and the last claimant is waiting in al-Yamama. Who was "
            "Musaylima, and why did forty thousand men follow him?",
            LESSON_B, [("Najd", "blue"), ("al-Yamama", "still red")],
            hidden=True, stop="STOP B")
    closing(prs, pool, "line_s04_stop_d.png", "s04-close-stop-d.json",
            "The line has been re-formed and the day is not yet decided. Where does an army go when "
            "it cannot retreat?",
            LESSON_D, [("Aqraba", "the day undecided")],
            hidden=True, stop="STOP D")

    D.save(prs, os.path.join(HERE, "S04.pptx"))
    D.write_briefs(os.path.join(HERE, "IMAGE_BRIEFS.md"))
    n = sum(len(r) for _, r in parts)
    print("   %d of %d runsheet cards became slides · %d slides in all (12 hidden: the STOP A, B and D "
          "closes)" % (made, n, len(prs.slides)))
    if no_beats:
        print("   ⚠ %d cards still have no **Beats:** — their notes fall back to the prose" % no_beats)


if __name__ == "__main__":
    build()
