# -*- coding: utf-8 -*-
"""Build S06.pptx — evenings 6 and 7 in one deck (DECISIONS.md #72).

    python S06_hadramawt_bahrayn/build.py          # -> S06.pptx + S06.pdf

    Run make_timeline.py and make_maps.py first; this places what they render and will stop if either
    is missing rather than draw a placeholder onto a slide that reaches a projector.

WHAT THIS FILE IS. Evening 5's build draws every kind of slide this evening needs — the card faces, the
layered click maps, the family trees, the checkpoints, the close — so this one imports that module and
supplies only what differs: the paths, the faces (#68), which card each map belongs to, and where the
checkpoints fall. Nothing about how a slide is drawn lives here. That is deliberate: evening 5's deck is
delivered and its drawing is known good, and a second copy of it would drift.

WHERE THIS DECK STOPS. Parts I-VIII, ending after RCT/E-RC35 — the Ridda finished, with the peninsula in
one colour. Parts IX (the two empires) and X (the two letters) are NOT built: Part IX needs a page-cited
note that does not exist yet, and no ISA/GSA card in the pool carries beats. They sit under ### headings
in RUNSHEET.md, so neither this build nor check_introductions.py reads them.
"""
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "series"))
sys.path.insert(0, os.path.join(ROOT, "tools"))

_spec = importlib.util.spec_from_file_location(
    "s05_build", os.path.join(ROOT, "S05_yamama_dead_oman_mahra", "build.py"))
S5 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(S5)

D, B = S5.D, S5.B

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(errors="replace")

# ---------------------------------------------------------------------------- this evening's own paths
S5.HERE = HERE
S5.VIS = os.path.join(HERE, "visuals")
S5.MAPS = os.path.join(S5.VIS, "maps")
S5.BOOKEND = os.path.join(S5.VIS, "bookend")
S5.HASH_FILE = os.path.join(HERE, ".build", "deck.sha256")
VIS, MAPS, BOOKEND = S5.VIS, S5.MAPS, S5.BOOKEND

# ---------------------------------------------------------------------------- faces (#68: names, not sentences)
S5.FACE_TITLE.update({
    "KTK/E-KD05": "al-Ashʿath b. Qays — at Medina",
    "TSY/E-YK07": "Ziyād b. Labīd ؓ, in Ḥaḍramawt",
    "RCT/E-RC33": "Ziyād b. Labīd ؓ — and Shadhra",
    "TSY/E-YK08": "al-ʿAddāʾ, and Ḥāritha b. Surāqa",
    "TSY/E-YK09": "Shuraḥbīl b. al-Simṭ, and his son",
    "TSY/E-YK10": "The four kings — Mikhwaṣ, Mishraḥ, Jamad, Abḍaʿa",
    "TSY/E-YK19": "al-Ashʿath b. Qays — the column he stopped",
    "TSY/E-YK11": "al-Muhājir ؓ and ʿIkrima ؓ — to al-Nujayr",
    "TSY/E-YK12": "al-Ashʿath b. Qays — and Jaḥdam",
    "TSY/E-YK14": "Abū Bakr ؓ and al-Ashʿath, at Medina",
    "POT/E-PG40": "al-Ashʿath ؓ — pardoned, and married",
    "TSY/E-YK16": "Ṭulayḥa ؓ · ʿAmr b. Maʿdī Karib ؓ · Qays",
    "POT/E-PG41": "al-Ashʿath ؓ and Jarīr b. ʿAbd Allāh ؓ",
    # the frame, and the east
    "RCT/E-RC80": "The year opens with the armies still out",
    "RCT/E-RC79": "The march to Khaybar that never happened",
    "RCT/E-RC76": "Khālid b. Saʿīd ؓ — a banner, and no battle",
    "RCT/E-RC77": "Jundub b. Salmā, and three more",
    "RCT/E-RC71": "al-Mundhir b. Sāwā ؓ — and the king they fetched back",
    "RCT/E-RC72": "al-Ḥuṭam b. Ḍubayʿa",
    "RCT/E-RC24": "Juwātha",
    "ATA/E-TB24": "al-Jārūd b. al-Muʿallā ؓ",
    "RCT/E-RC25": "al-ʿAlāʾ b. al-Ḥaḍramī ؓ — the sixteen",
    "RCT/E-RC26": "Ibn Ḥadhf, at the trench",
    "RCT/E-RC73": "Abjar b. Bujayr — his uncle",
    "RCT/E-RC74": "Qays b. ʿĀṣim, over al-Ḥuṭam",
    "RCT/E-RC27": "Dārīn",
    "RCT/E-RC75": "The monk of Hajar",
    "RCT/E-RC28": "Thumāma b. Uthāl ؓ",
    # the retrospective
    "ATA/E-TB22": "Thaqīf, at al-Ṭāʾif",
    "RCT/E-RC78": "Najrān",
    "ATA/E-TB10": "Banū Tamīm — three answers",
    "ATA/E-TB13": "The verse from the other side",
    "ATA/E-TB25": "The Azd — Medina, and Oman",
    "RCT/E-RC36": "Ibn Kathīr, on the whole war",
    "RCT/E-RC81": "ʿAbd Allāh b. Masʿūd ؓ",
    "RCT/E-RC39": "Abū Bakr ؓ, and the men of Badr",
    "RCT/E-RC43": "The eleven banners",
    "RCT/E-RC35": "ʿUmar ؓ — the captives bought back",
    "IKO/E-IKR1": "Ibn Khaldūn — as he reads it",
})

# ---------------------------------------------------------------------------- the maps
_K = S5.MAP_FOR
MAP_FOR = {
    "RCT/E-RC72": ("bahrain-darin", 1, 3,
                   [("al-Qaṭīf, Hajar", "taken"), ("al-Khaṭṭ", "drawn in")],
                   [(2, "He takes al-Qaṭīf, then Hajar."),
                    (3, "And sends a force on to Dārīn.")]),
    "RCT/E-RC24": ("bahrain-darin", 4, 5,
                   [("Juwātha", "besieged"), ("ʿAbd al-Qays", "hold, behind al-Jārūd ؓ")],
                   [(2, "Juwātha is shut in — and ʿAbd al-Qays do not move.")]),
    "RCT/E-RC25": ("bahrain-darin", 6, 8,
                   [("The sixteen", "from Medina"), ("al-Dahnāʾ", "the camels, then the water")],
                   [(2, "Sixteen riders come in from the west."),
                    (4, "al-Dahnāʾ: the camels are gone — and then the water.")]),
    "RCT/E-RC26": ("bahrain-darin", 9, 11,
                   [("al-Jārūd ؓ", "comes up the other side"), ("Hajar", "a month, dug in")],
                   [(2, "al-Jārūd ؓ brings ʿAbd al-Qays up against him from the other side."),
                    (4, "Both sides dig in, and it holds for a month.")]),
    "RCT/E-RC27": ("bahrain-darin", 12, 14,
                   [("Dārīn", "a day and a night by ship"), ("The land roads", "closed behind them")],
                   [(2, "The beaten take ship for Dārīn."),
                    (4, "The land roads are closed behind them — and then they go straight across the water.")]),
}
for _cid in ("TSY/E-YK07", "TSY/E-YK08", "TSY/E-YK09", "TSY/E-YK10", "TSY/E-YK19", "TSY/E-YK11"):
    MAP_FOR[_cid] = _K[_cid]          # evening 5's own Ḥaḍramawt slices, unchanged
S5.MAP_FOR = MAP_FOR

S5.MAP_BRIDGE_BEFORE = MAP_BRIDGE_BEFORE = {}
S5.MAP_BRIDGE_QUOTE = {}

# ---------------------------------------------------------------------------- bridges and the tree
BRIDGE_BEFORE = {
    "RCT/E-RC71": ("Meanwhile, in the east", "11 AH, البحرين",
                   [("Last week", "we followed one man's road east, front by front"),
                    ("Tonight", "we go back once — to the front that started before all of them"),
                    ("Then", "forward, to the last one")],
                   "Put your finger on the map where we stopped last week. Now take it off, and put it here.\n"
                   "We are going back — not far, but back. While al-Yamāma was being fought, and while Oman "
                   "and Mahra were being fought, there was a front on the other side of Arabia that had "
                   "started before any of them. Tonight we tell it, and then we come forward to the last one."),
    "KTK/E-KD05": ("Before any of this", "10 AH, Medina",
                   [("Two years earlier", "a delegation comes to Medina"),
                    ("At its head", "a man the room will meet again tonight"),
                    ("Then", "forward again, and we do not go back")],
                   "One step back, and I will say when we take it. Two years before the Prophet ﷺ died, a "
                   "delegation came to Medina from a tribe in the south — and the man at its head is the man "
                   "this last front belongs to. After this we go forward, and we stay there."),
    "ATA/E-TB22": ("The same year, looked at sideways", "11 AH",
                   [("So far", "every front, one after another"),
                    ("Now", "the same months — and who did not break at all"),
                    ("The question", "what made the difference?")],
                   "Everything so far tonight has been a front. Now I want to stop moving forward and look at "
                   "the same months from the side — because a map that is all fire is a map that is lying. "
                   "Not everyone broke. Some of the people who held are the ones you would least expect."),
}
S5.BRIDGE_BEFORE = BRIDGE_BEFORE
TREES = {"KTK/E-KD05": S5.TREES["KTK/E-KD05"]}
S5.TREES = TREES

# ---------------------------------------------------------------------------- the four stops
CHECKPOINTS = {
    "RCT/E-RC28": dict(
        n=1, line="line_s06_cp1.png", scene=("s06-arabia", 2),
        keys=[("Bahrayn", "settled"), ("Ḥaḍramawt", "still to come")],
        say_line="Tonight so far: the year opened with the armies still out — and the front that started "
                 "before all of them, from Juwātha to Dārīn.",
        say_map="When you came in, there was one grey patch on the Gulf coast. It is green. One front is left.",
        clock="Past 0:24 here and you are ahead; past 0:36, close here.",
        carry="One front was left — and it began with a quarrel about camels.",
        question="One front was left, and the books say it began with one she-camel. Next week: how.",
        lessons=["RCT/E-RC72", "RCT/E-RC25", "RCT/E-RC27"]),
    "TSY/E-YK12": dict(
        n=2, line="line_s06_cp2.png", scene=("s06-arabia", 3),
        keys=[("al-Nujayr", "opened"), ("al-Ashʿath", "in bonds, for Medina")],
        say_line="Tonight: Bahrayn, and then the last front — from a camel to a fort.",
        say_map="Every front we have told is settled. And one man is on his way to Medina, in bonds.",
        clock="Past 0:36 here → close here. The judgement at Medina opens next week.",
        carry="He had left his own name off the paper. Now he stood in front of Abū Bakr ؓ.",
        question="A man who had led a whole tribe out of Islam stood in front of Abū Bakr ؓ, in bonds. Next "
                 "week: what Abū Bakr ؓ did with him.",
        lessons=["RCT/E-RC27", "TSY/E-YK10", "TSY/E-YK12"]),
    "POT/E-PG41": dict(
        n=3, line="line_s06_cp3.png", scene=("s06-arabia", 4),
        keys=[("Every front", "settled"), ("One man", "who came back")],
        say_line="Tonight: the last two fronts — and a man who stood in bonds and then stood up again.",
        say_map="When you came in, two patches were grey. The peninsula is one colour.",
        clock="Past 0:40 here → close here. This is the natural end of the evening.",
        carry="The fighting is over. Now I want to ask what the whole of it was.",
        question="Two years after the Prophet ﷺ died, every man in Arabia was on the same side. Next week: "
                 "what the books say the whole of it actually was.",
        lessons=["TSY/E-YK12", "TSY/E-YK14", "POT/E-PG41"]),
    "RCT/E-RC43": dict(
        n=4, line="line_s06_cp4.png", scene=("s06-arabia", 4),
        keys=[("The Ridda", "whole"), ("Eleven banners", "every sector settled")],
        say_line="Tonight: both fronts, and then the whole war looked at from the end of it.",
        say_map="Eleven banners went out of one sitting. Every one of those sectors is now this colour.",
        clock="Past 0:52 here → close here. This is the last checkpoint that is built.",
        carry="One thing is left, and it is what ʿUmar ؓ did about it years afterwards.",
        question="There were two empires on the other side of that desert. Next week: did either of them know?",
        lessons=["RCT/E-RC36", "RCT/E-RC81", "RCT/E-RC39"]),
}
S5.CHECKPOINTS = CHECKPOINTS

CLOSE_AFTER = "RCT/E-RC35"
S5.CLOSE_AFTER = CLOSE_AFTER
S5.TONIGHT = TONIGHT = [
    ("Right and left", "RCT/E-RC80"),
    ("The front that started first", "RCT/E-RC27"),
    ("The last front", "TSY/E-YK12"),
    ("The man who came back", "POT/E-PG41"),
    ("What the whole of it was", "RCT/E-RC81"),
]
S5.NEXT_WEEK = NEXT_WEEK = ("Two years after the Prophet ﷺ died, every man in Arabia was on the same side. "
                            "There were two empires on the other side of the desert. Did either of them know?")


# ---------------------------------------------------------------------------- the bookend
def bookend_images():
    """Evening 5's Checkpoint 2 pair — Daniyal's own slides 61-62, not the build's (#23)."""
    os.makedirs(BOOKEND, exist_ok=True)
    line, mp = os.path.join(BOOKEND, "cp2_line.png"), os.path.join(BOOKEND, "cp2_map.png")
    if not (os.path.exists(line) and os.path.exists(mp)):
        from pptx import Presentation
        prev = Presentation(os.path.join(ROOT, "S05_yamama_dead_oman_mahra", "S05.pptx"))
        slides = list(prev.slides)
        for idx, path in ((60, line), (61, mp)):              # his slides 61-62, zero-based
            pics = [sh for sh in slides[idx].shapes if sh.shape_type == 13]
            if not pics:
                raise SystemExit("no picture on S05.pptx slide %d — the bookend pair moved" % (idx + 1))
            open(path, "wb").write(max(pics, key=lambda sh: sh.width * sh.height).image.blob)
    return line, mp


S5.bookend_images = bookend_images


def the_close(prs, pool):
    """Evening 6's own close. Evening 5's is about its own evening, so it cannot be reused."""
    s = D.timeline_slide(prs, os.path.join(VIS, "line_s06_close.png"), "Tonight on the Line")
    D.note(s, "THE CLOSE — the Line.\n\nSAY — Tonight began with a sentence from Ibn Kathīr: the year opened "
              "with the armies still out, roving right and left. Then the front that had started before all of "
              "them — Juwātha, al-Dahnāʾ, the trench, and the crossing to Dārīn. Then back two years, to a "
              "delegation in Medina, and forward again to the last front and the fort at al-Nujayr. And then "
              "the whole of it, looked at from the end: who did not break, what Ibn Kathīr says it was, and "
              "what Ibn Masʿūd ؓ said they had very nearly done instead.")
    lines = ["Bahrayn — the front that started first — settled.",
             "Ḥaḍramawt — the last front — settled.",
             "And the peninsula in one colour, which is where the books leave it."]
    m, n = S5.layered_map(prs, "s06-arabia", 1, 4, "Where we stand", "12 AH",
                          [("Tonight", "the last two fronts, and the whole war"),
                           ("Next week", "the other side of the desert")])
    D.note(m, S5.map_notes("When you came in, two patches on this map were grey.", lines))
    if n != len(lines):
        raise SystemExit("the close map has %d clicks; its notes have %d" % (n, len(lines)))
    s = D.lessons_slide(prs, [h for h, _ in TONIGHT])
    D.note(s, "TONIGHT — say each heading, then its line:\n" + "\n".join(
        "%d. %s — %s" % (i, h, B.clean(pool[c]["ibrah"])) for i, (h, c) in enumerate(TONIGHT, 1)))
    q = D.question_slide(prs, NEXT_WEEK)
    D.note(q, "Ask it, and pause. Then a loud السلام علیکم — and the dua. The room must know it has ended.")


def build():
    pool = B.pool_cards()
    parts = B.runsheet(os.path.join(HERE, "RUNSHEET.md"))
    ids = [cid for _, rows in parts for cid, _ in rows]
    missing = [cid for cid in ids if cid not in pool]
    if missing:
        raise SystemExit("RUNSHEET.md names cards that are not in any pool: %s" % missing)
    for table, name in ((MAP_FOR, "MAP_FOR"), (TREES, "TREES"), (BRIDGE_BEFORE, "BRIDGE_BEFORE"),
                        (CHECKPOINTS, "CHECKPOINTS")):
        stray = [k for k in table if k not in ids]
        if stray:
            raise SystemExit("%s names cards the runsheet does not run: %s" % (name, stray))
    S5.check_face_quotes(pool)

    prs = D.deck()
    D.title_slide(prs, "Right and left", "11–12 AH", "Evening 6")

    line, mp = bookend_images()
    s = D.timeline_slide(prs, line, "Where we stopped")
    D.note(s, "BOOKEND IN — last week's closing Line, unchanged.\n\nSAY — Last week ended with Oman and Mahra "
              "settled, and one grey patch left on the map.")
    s = D.map_slide(prs, mp, "Where we stand", keys=[("Oman, Mahra", "settled"), ("Ḥaḍramawt", "still to come")],
                    kicker="From last week", map_frac=0.70)
    D.note(s, "BOOKEND IN — last week's closing map, unchanged.\n\nSAY — Tonight: the front that started "
              "before all of them — and then the last one.")

    made = clicks_total = bridges = maps = words_slides = trees = checkpoints = 0
    for part, rows in parts:
        D.section_slide(prs, B.clean(part.split(" — ")[0], translit=True),
                        B.clean(part.split(" — ", 1)[1] if " — " in part else "", translit=True) or None)
        for cid, rnote in rows:
            c = S5.face_card(pool[cid], cid)
            if cid in BRIDGE_BEFORE:
                head, kick, rows_, say = BRIDGE_BEFORE[cid]
                s = D.diagram_slide(prs, head, rows_, kicker=kick)
                D.note(s, "BRIDGE — say:\n" + say)
                bridges += 1
            if cid in TREES:
                S5.family_tree(prs, pool, TREES[cid])
                trees += 1
            off_face = "NOT FOR THE SLIDE FACE" in (c.get("extra") or "")
            if cid in MAP_FOR:
                scene, a, b, keys, clicks = MAP_FOR[cid]
                fq = S5.FACE_QUOTE.get(cid)
                words = bool(c["arabic"]) and not off_face and B.ar_len(fq[0] if fq else c["arabic"]) <= B.AR_SLIDE_MAX
                head = B.headline_for(B.short(B.face(c["title"]), 9))
                s, n = S5.layered_map(prs, scene, a, b, head, B.kicker_for(c), keys)
                notes, k = S5.map_card_notes(c, rnote, clicks, words)
                if n != k:
                    raise SystemExit("%s on %s %d-%d: %d clicks on the slide, %d ▶ CLICK lines in its notes"
                                     % (cid, scene, a, b, n, k))
                D.note(s, notes)
                maps += 1
                clicks_total += n
                if words:
                    w = B.card_slide(prs, c, face_quote=fq)
                    if w is not None:
                        D.note(w, S5.words_notes(c))
                        words_slides += 1
                made += 1
            else:
                face_text = B.short(c["what"].split(". ")[0].rstrip(".") + ".", 18) if off_face else None
                s = B.card_slide(prs, c, arabic_on_face=not off_face, face_text=face_text,
                                 face_quote=S5.FACE_QUOTE.get(cid))
                if s is not None:
                    D.note(s, S5.card_notes(c, rnote))
                    made += 1
            if cid in CHECKPOINTS:
                S5.checkpoint(prs, pool, CHECKPOINTS[cid])
                checkpoints += 1
            if cid == CLOSE_AFTER:
                the_close(prs, pool)

    if checkpoints != len(CHECKPOINTS):
        raise SystemExit("%d checkpoints emitted of %d — a checkpoint card left the runsheet"
                         % (checkpoints, len(CHECKPOINTS)))
    target = os.path.join(HERE, "S06.pptx")
    if S5.deck_has_uncommitted_changes(target):
        print("   !! S06.pptx differs from its committed version (Daniyal's edits?) - NOT overwritten.\n"
              "      This build is written to S06_NEW.pptx. Commit or discard the changes first.")
        target = os.path.join(HERE, "S06_NEW.pptx")
    out = D.save(prs, target)
    S5.remember_deck(out)
    import json
    os.makedirs(os.path.join(HERE, ".build"), exist_ok=True)
    with open(os.path.join(HERE, ".build", "slides.json"), "w", encoding="utf-8") as f:
        json.dump({str(i): S5.LAYERED[s.slide_id] for i, s in enumerate(prs.slides, 1)
                   if s.slide_id in S5.LAYERED}, f, ensure_ascii=False, indent=1)
    print("   %d of %d runsheet cards · %d maps (%d clicks) · %d words slides · %d trees · %d bridges · "
          "%d checkpoints · %d slides in all"
          % (made, len(ids), maps, clicks_total, words_slides, trees, bridges, checkpoints, len(prs.slides)))
    return out


if __name__ == "__main__":
    if os.path.exists(os.path.join(HERE, "S06.FINAL")):
        raise SystemExit("S06.FINAL exists: S06.pptx is hand-finished. Do not rebuild over it.")
    build()
