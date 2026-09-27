# -*- coding: utf-8 -*-
"""Evening 5 — Map Studio scenes, rendered as click-by-click layers (DECISIONS.md #58).

    python S05_yamama_dead_oman_mahra/make_maps.py            # every scene
    python S05_yamama_dead_oman_mahra/make_maps.py s05-01     # only the scenes whose slug contains it
      -> tools/mapstudio/scenes/s05-*.json                     (the scenes, editable in the tool)
      -> S05_yamama_dead_oman_mahra/visuals/maps/<scene>-step-NN.png           (every step, whole)
      -> S05_yamama_dead_oman_mahra/visuals/maps/<scene>-r<a>-<b>-*            (one slide's layers)

WHAT A MAP SLIDE IS NOW. Not a finished picture shown before the story is told, but the stage the story
is told on: the ground stays up, and each click brings on the next move — an arrow drawing itself along
its route, a banner travelling along it, a territory fading to green. SLIDES below lists every map slide
of the evening as (scene, first step, last step); build.py places each one and writes its clicks, and the
card's notes carry "▶ CLICK n" on the beat the click belongs to.

WHAT EACH MAP MAY SHOW. As on evening 4: every route and label comes from the Map: line and the beats of
the card it serves, and a step may draw only what that card, or an earlier one, has told. Placement is
approximate and schematic; sites the gazetteer marks approximate say so in the scene's notes.

ONE GREEN. Muslim forces are #2CB020 on every map — the green Daniyal chose on his evening-4 maps (#58).

Built on evening 4's make_maps.py — its gazetteer placements (ʿAqrabāʾ, Ḥajr), the garden, the sections —
loaded from its file so the two evenings draw the same ground. Writes ONLY s05-* files.
"""
import copy
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "tools"))
import make_scenes as MS                                  # noqa: E402
import render_scene                                       # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(errors="replace")

_spec = importlib.util.spec_from_file_location("s04_maps", os.path.join(ROOT, "S04_kinda_butah_yamama", "make_maps.py"))
M4 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(M4)
pl, spot, force, path, xy, note, area = M4.pl, M4.spot, M4.force, M4.path, M4.xy, M4.note, M4.area

OUT_PNG = os.path.join(HERE, "visuals", "maps")
GREEN = "#2CB020"
FACTIONS = [dict(f, color=GREEN) if f["id"] == "f1" else dict(f) for f in MS.FACTIONS]
# grey means "still to come" on these maps (Ḥaḍramawt at the close), never "held firm"
for _f in FACTIONS:
    if _f["id"] == "f5":
        _f["name"] = "Still to come"
M4.NAMES["Makkah"] = "Mecca"

AQR, HAJR = M4.AQR, M4.HAJR


def follow(army, arrow):
    """This banner travels along that arrow on the click they both appear (series/anim.py)."""
    army["follows"] = arrow["id"]
    return army


def until(obj, step):
    obj["until"] = step
    return obj


def scenes():
    S = []

    # ------------------------------------------------------------------ M1 — the day at ʿAqrabāʾ
    # The recap before RC67: evening 4 ended with al-Yamāma taken (RC66, RC20, RC21, RC22 — all spoken).
    # Step 1 is where evening 4's STOP C left the line; steps 2-6 retell the end in five clicks, and the
    # last click hands over to the terms (RC67). Every move is from those four cards' Map: lines.
    # SECOND PASS (#64): what a click has finished with fades on the next one — the captions, the spent
    # arrows, the section banners once the army is inside — so the last click is not a pile of words.
    retreat = until(path([AQR, [46.70, 24.78], [46.97, 24.66]], "", "f4", width=10, step=2, ls=1), 3)
    over = until(path([[46.10, 25.02], [46.48, 24.90], [46.82, 24.70]], "", "f1", width=8, step=3, ls=1), 4)
    pour = path([[46.10, 24.86], [46.50, 24.70], [46.90, 24.63]], "", "f1", width=14, step=4, ls=1)
    S.append(("s05-01-aqraba", "ʿAqrabāʾ", "12 AH — how the day ended", [45.55, 24.28, 47.30, 25.42],
              M4.the_ground(step_farms=1, strength="Banū Ḥanīfa")[:3] + [
                  # the ground's own Musaylima banner leaves as he falls back (click 1)…
                  until(force("Musaylima", AQR[0], AQR[1], "f4", "Banū Ḥanīfa", scale=1.2), 1),
                  area(M4.FARMS, "f4", "", 0.20), until(note(46.93, 24.96, "their farms", 24), 2),
                  force("Khālid ؓ", 45.80, 24.95, "f1", label_pos="above", scale=1.1),
              ] + [until(force(n, M4.SECTION_LON, lat, "f1", scale=0.9), 3) for n, lat in M4.SECTIONS] + [
                  # click 1 — RC66/RC20: they break and fall back into the walled garden; the gate shuts.
                  retreat,
                  follow(until(force("Musaylima", 47.00, 24.62, "f4", "", scale=0.95, label_pos="right",
                                     step=2), 4), retreat),
                  until(area(M4.GARDEN, "f4", "", 0.42, step=2), 3),
                  until(note(47.03, 24.86, "the gate shut", 22, step=2), 3),
                  # click 2 — RC20: al-Barāʾ ؓ over the wall
                  over,
                  follow(until(force("al-Barāʾ ؓ", 46.80, 24.68, "f1", label_pos="left", step=3, scale=0.85), 4),
                         over),
                  # click 3 — RC20: he opens the gate; the army pours in and the garden turns green
                  pour,
                  area(M4.GARDEN, "f1", "", 0.48, step=4),
                  until(note(47.03, 24.86, "opened from the inside", 22, step=4), 4),
                  # click 4 — RC21: Musaylima falls in a gap in the wall; his banner goes
                  {"id": MS._uid("b"), "type": "battle", "lon": 46.97, "lat": 24.58, "name": "Musaylima falls",
                   "date": "", "ur": "", "labelPos": "below", "step": 5, "note": ""},
                  # click 5 — RC22 → RC67: the survivors in the forts, round Ḥajr — the terms are the next card
                  area([[46.55, 24.70], [46.78, 24.70], [46.79, 24.54], [46.55, 24.54]], "f4", "", 0.30, step=6),
                  note(46.60, 24.44, "the forts", 24, step=6),
              ],
              M4.TIGHT))

    # ------------------------------------------------------------------ M2 — Tustar (HS17)
    # SECOND PASS: the house's life-route is gone with its cards (Tree A carries the house). What is left
    # is al-Barāʾ's ؓ own road: the gate at al-Yamāma, and — one click — Tustar, years later, dashed.
    S.append(("s05-02-tustar", "al-Barāʾ ؓ", "12 AH to Tustar, years later", [36.6, 19.2, 51.6, 33.4], [
                  pl("Madina", "left"),
                  path([MED, [43.2, 25.3], AQR], "", "f1", width=11, ls=1),
                  battle("The gate, 12 AH", AQR[0], AQR[1], "below"),
                  path([AQR, [47.6, 28.6], TUSTAR], "", "f1", dashed=True, width=9, step=2, ls=1),
                  spot("Tustar", TUSTAR[0], TUSTAR[1], "right", step=2, tier="city"),
                  note(48.9, 31.25, "years later", 24, step=2),
              ], {"legend": False}))

    # ------------------------------------------------------------------ M3 — Iṣṭakhr (AS06)
    # AS06 beat 1: "His origin was Iṣṭakhr, in Persia." The books give his origin, not his road — so no
    # line is drawn between Iṣṭakhr and Mecca: two points, and the distance between them, are the picture.
    S.append(("s05-03-salim", "Sālim ؓ", "from Iṣṭakhr, in Persia", [35.4, 18.0, 55.6, 31.6], [
                  pl("Makkah", "left"),
                  note(39.9, 22.35, "Abū Ḥudhayfa ؓ", 24),
                  pl("Madina", "left"),
                  spot("Iṣṭakhr, in Persia", ISTAKHR[0], ISTAKHR[1], "below", step=2, tier="city"),
                  note(ISTAKHR[0], ISTAKHR[1] + 0.9, "Sālim ؓ", 28, step=2),
              ], {"legend": False}))

    # ------------------------------------------------------------------ M4 — ʿIkrima ؓ before Islam
    # TRN6 the flight to the coast and the ship (steps 1-2) · TRN7 Umm Ḥakīm ؓ goes after him, and brings
    # him back (steps 2-4). Before his Islam he is drawn in grey with no legend, never in the revolt's ochre.
    flee = path([MECCA, [39.55, 21.05], COAST], "", "f5", width=9, step=2, ls=1)
    after = until(path([MECCA, [39.62, 21.30], COAST], "", "f1", dashed=True, width=7, step=3, ls=1), 3)
    back = path([COAST, [39.35, 21.55], MECCA], "", "f1", width=9, step=4, ls=1)
    S.append(("s05-04-ikrima-flight", "ʿIkrima ؓ", "8 AH — the Conquest of Mecca", [37.9, 19.6, 41.9, 22.9], [
                  pl("Makkah", "right"),
                  note(38.55, 20.35, "the sea", 26),
                  flee, until(follow(force("ʿIkrima", COAST[0], COAST[1], "f5", label_pos="left", step=2,
                                           scale=0.9), flee), 3),
                  after, until(note(39.70, 20.90, "Umm Ḥakīm ؓ", 22, step=3), 3),
                  back, follow(force("ʿIkrima ؓ", MECCA[0] - 0.02, MECCA[1] + 0.03, "f1", label_pos="above",
                                     step=4, scale=0.9), back),
              ], {"legend": False}))

    # ------------------------------------------------------------------ M5 — Oman asked for help (RC70)
    # One click per beat 2-6: the rulers pushed to the edges · the request · the two commanders from
    # Medina · ʿIkrima's ؓ line from al-Yamāma, joining at Rijām (a label: no page locates it) · letters to
    # the rebel's own chiefs. Each caption fades when the next move lands (#64).
    ask = until(path([[56.4, 23.5], [52.0, 25.4], [44.3, 25.9]], "", "f1", dashed=True, width=7, step=3, ls=1), 3)
    cols = path([[44.3, 26.6], [50.0, 26.8], RIJAM], "", "f1", width=10, step=4, ls=1)
    ikr = path([[46.9, 24.3], [51.0, 23.2], RIJAM], "", "f1", width=10, step=5, ls=1)
    S.append(("s05-05-oman", "Oman", "11→12 AH — a request, not an invasion", [44.0, 17.0, 60.2, 27.8], [
                  area(YAMAMA, "f1", "", 0.26), note(46.9, 25.0, "al-Yamāma", 24),
                  area(OMAN_A, "f4", "", 0.28), note(58.3, 21.3, "Oman", 30),
                  force("Laqīṭ", xy("Nizwa")[0], xy("Nizwa")[1], "f4", "the one with the crown", label_pos="right",
                        scale=0.95),
                  force("Jayfar and ʿAbbād", 56.45, 24.55, "f1", label_pos="left", step=2, scale=0.8),
                  until(note(57.55, 24.95, "to the edges", 22, step=2), 2),
                  ask, until(note(49.3, 25.95, "Jayfar asks for help", 22, step=3), 3),
                  cols, until(note(47.2, 27.25, "from Medina", 22, step=4), 4),
                  ikr, follow(force("ʿIkrima ؓ", RIJAM[0] - 0.25, RIJAM[1] - 0.05, "f1", label_pos="below",
                                     step=5, scale=0.85), ikr),
                  note(RIJAM[0], RIJAM[1] + 0.55, "Rijām", 22, step=5),
                  path([RIJAM, [55.9, 23.2], [57.1, 22.7]], "", "f1", dashed=True, width=6, step=6, ls=1),
                  note(56.4, 20.55, "letters to his chiefs", 22, step=6),
              ], {}))

    # ------------------------------------------------------------------ M6 — Dabā (RC29)
    # Laqīṭ at Dabā with the families and property behind him (as Musaylima did at ʿAqrabāʾ); the rulers at
    # Ṣuḥār; the Muslim line nearly breaks; relief from INSIDE the region — short arrows. Beats 3-6.
    adv = path([[56.66, 24.55], [56.55, 24.90], [56.45, 25.22]], "", "f1", width=11, step=2, ls=1)
    S.append(("s05-06-daba", "Dabā", "11→12 AH — the relief that came from inside", [55.15, 23.95, 57.65, 26.40], [
                  spot("Dabā", DABA[0], DABA[1], "right", tier="city"),
                  spot("Ṣuḥār", SUHAR[0], SUHAR[1], "right", tier="city"),
                  force("Laqīṭ", DABA[0] - 0.06, DABA[1] + 0.16, "f4", "", label_pos="left", scale=0.9),
                  area([[55.98, 26.14], [56.45, 26.16], [56.42, 25.90], [56.00, 25.92]], "f4", "", 0.22),
                  until(note(56.22, 26.24, "families behind", 20), 2),
                  force("Jayfar and ʿAbbād", SUHAR[0] - 0.05, SUHAR[1] + 0.1, "f1", label_pos="right", scale=0.8),
                  adv, follow(force("the Muslims", 56.45, 25.22, "f1", label_pos="right", step=2, scale=0.85), adv),
                  until(path([[56.18, 25.55], [56.30, 25.30], [56.42, 25.12]], "", "f4", width=10, step=3, ls=1), 4),
                  until(note(57.05, 24.95, "the line gives way", 22, step=3), 3),
                  path([[55.55, 24.75], [55.95, 25.05], [56.22, 25.35]], "", "f1", width=9, step=4, ls=1),
                  until(note(55.62, 24.62, "Banū Nājiya", 22, step=4), 4),
                  path([[56.95, 24.85], [56.62, 25.20], [56.40, 25.45]], "", "f1", width=9, step=4, ls=1),
                  until(note(57.12, 24.72, "ʿAbd al-Qays", 22, step=4), 4),
                  battle("the rebels broken", DABA[0] - 0.10, DABA[1] - 0.10, "left", step=5),
              ], {"legend": False}))

    # ------------------------------------------------------------------ M7 — Mahra (RC30)
    # Two forces under two chiefs at odds; ʿIkrima ؓ arrives; the letter — and the smaller chief comes over
    # on the same click; the larger refuses and is broken; the fifth goes to Medina with the man who came over.
    arrive = path([[55.4, 19.3], [54.3, 18.3], [53.35, 17.55]], "", "f1", width=10, step=2, ls=1)
    letter = until(path([[53.25, 17.45], [52.85, 17.30], [52.50, 17.20]], "", "f1", dashed=True, width=6,
                        step=3, ls=1), 3)
    fifth = path([[52.40, 17.35], [51.1, 18.1], [49.6, 18.6]], "", "f1", dashed=True, width=8, step=5, ls=1)
    S.append(("s05-07-mahra", "Mahra", "11→12 AH — the front won with a letter", [48.9, 14.9, 56.2, 19.9], [
                  note(54.2, 18.75, "Mahra", 30),
                  until(force("al-Muṣabbaḥ", 51.30, 16.80, "f4", "the larger force", label_pos="below", scale=1.0), 3),
                  until(force("Shikhrīt", 52.45, 17.15, "f4", "", label_pos="right", scale=0.8), 2),
                  arrive, follow(force("ʿIkrima ؓ", 53.35, 17.55, "f1", label_pos="right", step=2, scale=0.9), arrive),
                  letter, until(note(52.55, 17.98, "the letter", 20, step=3), 3),
                  force("Shikhrīt", 52.45, 17.15, "f1", "", label_pos="below", step=3, scale=0.8),
                  battle("harder than Dabā", 51.30, 16.80, "below", step=4),
                  fifth, note(50.5, 18.85, "the fifth, to Medina", 22, step=5),
              ], {}))

    # ------------------------------------------------------------------ M7b — the field (Part III's men)
    # Kept for the notes book of the first pass; no slide uses it now.
    S.append(("s05-08-field-origins", "One field", "12 AH — where the men of al-Yamāma came from",
              [37.4, 18.6, 48.6, 26.8], [
                  pl("Madina", "left"), pl("Makkah", "left"),
                  spot("Daws", DAWS[0], DAWS[1], "left", tier="town"),
                  path([MED, [43.2, 25.3], AQR], "", "f1", width=10, ls=1),
                  path([MECCA, [43.5, 22.6], AQR], "", "f1", width=8, ls=1),
                  path([DAWS, [44.0, 21.9], AQR], "", "f1", width=8, ls=1),
                  battle("al-Yamāma", AQR[0], AQR[1], "below"),
              ], {"legend": False}))

    # ------------------------------------------------------------------ M8 — Ḥaḍramawt and Kinda (Part VII)
    # One scene, sixteen steps, six slides — each the slide of the card it tells (#63):
    #   YK07 1→3 · YK08 3→6 · YK09 6→8 · YK10 8→10 · YK19 10→13 · YK11 13→16.
    # Every move is from those cards' Map: lines and beats. NOTHING HERE IS LOCATED BY OUR SOURCES except
    # Ṣanʿāʾ: the campaign note §13 — "draw zones and arrows, never points" — so the two zones are schematic,
    # the pastures are five unnamed marks, and Maḥjar al-Zurqān and al-Nujayr sit where the story needs them
    # (al-Nujayr at the gazetteer's approximate point). The scene's notes say so.
    zak1 = until(path([[50.0, 16.75], [48.5, 17.0], [47.4, 16.75]], "", "f1", dashed=True, width=6, step=2, ls=1), 2)
    zak2 = until(path([[47.4, 15.75], [48.5, 15.52], [50.0, 15.8]], "", "f1", dashed=True, width=6, step=2, ls=1), 2)
    CAMP = (49.00, 16.05)
    night = until(path([[48.85, 16.12], [48.25, 16.28], [47.85, 16.28]], "", "f1", width=8, step=5, ls=1), 5)
    PAST = [(46.85, 16.60), (47.30, 16.82), (47.78, 16.62), (47.02, 16.12), (47.58, 16.16)]
    KINGS = (47.30, 16.45)
    walk = until(path([PAST[2], [48.25, 16.52], [48.62, 16.38]], "", "f1", dashed=True, width=5, step=8, ls=1), 8)
    ring = [until(path([[KINGS[0] + dx, KINGS[1] + dy], [KINGS[0] + dx * 0.55, KINGS[1] + dy * 0.55],
                        [KINGS[0] + dx * 0.18, KINGS[1] + dy * 0.18]], "", "f1", width=7, step=9, ls=1), 9)
            for dx, dy in [(0.0, 0.58), (0.72, 0.16), (0.50, -0.50), (-0.50, -0.50), (-0.74, 0.14)]]
    column = until(path([[47.45, 16.25], [47.90, 15.92], [48.30, 15.66]], "", "f1", width=8, step=11, ls=1), 12)
    retake = until(path([[48.52, 15.40], [48.42, 15.55], [48.33, 15.63]], "", "f4", width=8, step=13, ls=1), 13)
    fast = path([SANA, [46.4, 15.0], [49.62, 15.52]], "", "f1", width=6, step=14, ls=1)
    zurqan = until(path([[49.45, 15.48], [48.60, 15.24], [47.92, 15.32]], "", "f1", width=9, step=15, ls=1), 15)
    body = path([SANA, [46.3, 14.85], [47.30, 15.62], [48.02, 15.98]], "", "f1", dashed=True, width=8, step=16, ls=1)
    S.append(("s05-10-kinda", "Ḥaḍramawt and Kinda", "11→12 AH — the last front", [45.9, 14.4, 51.3, 17.5], [
                  area(KINDA_Z, "f5", "", 0.26), note(46.80, 16.98, "Kinda", 30),
                  area(HADR_Z, "f5", "", 0.26), note(50.45, 16.98, "Ḥaḍramawt", 30),
                  force("Ziyād b. Labīd ؓ", 49.90, 15.60, "f1", label_pos="below", scale=0.9),
                  # YK07 — the ṣadaqa both ways (beat 2); then "carry it yourselves" (beat 6)
                  zak1, zak2, until(note(48.50, 17.32, "ṣadaqa, both ways", 22, step=2), 2),
                  until(note(48.50, 15.02, "not carried", 24, step=3), 3),
                  # YK08 — two camps (beat 5), a strike by night (beat 7), Kinda roused (beat 8)
                  until(force("Ḥaḍramawt, al-Sakūn", CAMP[0], CAMP[1], "f1", label_pos="right", step=4, scale=0.8), 13),
                  until(force("Banū Muʿāwiya", 47.60, 16.20, "f4", label_pos="below", step=4, scale=0.85), 6),
                  night, until(note(48.30, 16.58, "by night", 22, step=5), 5),
                  area(KINDA_Z, "f4", "", 0.34, step=6), until(note(47.35, 17.34, "no ṣadaqa", 24, step=6), 6),
                  # YK09 — the pastures held as strongholds (beat 1); one man and his son leave (beat 4)
              ] + [until(spot("", x, y, "right", step=7, tier="town"), 9) for x, y in PAST] + [
                  until(note(47.30, 14.98, "their pastures, as strongholds", 22, step=7), 7),
                  walk, until(follow(force("Shuraḥbīl and his son", 48.62, 16.38, "f1", label_pos="above", step=8,
                                           scale=0.7), walk), 8),
                  # YK10 — ringed from five sides (beat 1); the four kings killed (beat 4)
              ] + ring + [
                  until(note(47.05, 17.38, "from five sides", 22, step=9), 9),
                  battle("the four kings", KINGS[0], KINGS[1], "above", step=10),
                  # YK19 — the column turns for home (beat 1); al-Ashʿath on its road (beat 2); the captives
                  # taken back (beat 5)
                  column, until(follow(force("the captives", 48.30, 15.66, "f1", label_pos="right", step=11,
                                             scale=0.7), column), 12),
                  until(force("al-Ashʿath b. Qays", 48.55, 15.30, "f4", label_pos="below", step=12, scale=0.9), 14),
                  retake, until(note(49.25, 15.02, "the captives taken back", 22, step=13), 13),
                  # YK11 — al-Muhājir ؓ ahead from Ṣanʿāʾ (beat 2); Maḥjar al-Zurqān (beat 3); al-Nujayr, and
                  # ʿIkrima ؓ with the main body — the siege (beats 4-5). Ṣanʿāʾ is off the map to the west.
                  fast, follow(force("al-Muhājir ؓ", 49.62, 15.52, "f1", label_pos="above", step=14, scale=0.8), fast),
                  until(note(46.55, 14.72, "from Ṣanʿāʾ", 22, step=14), 15),
                  zurqan, battle("Maḥjar al-Zurqān", 47.72, 15.34, "below", step=15),
                  spot("al-Nujayr", NUJAYR[0], NUJAYR[1], "right", step=16, tier="fort"),
                  area(RING, "f1", "", 0.18, step=16),
                  body, follow(force("ʿIkrima ؓ", 48.02, 15.98, "f1", label_pos="above", step=16, scale=0.8), body),
              ], {"legend": False}))

    # ------------------------------------------------------------------ M9 — Arabia: checkpoints and the close
    # Step 1: al-Yamāma taken, the north and the Yemen settled; the east still fighting; Ḥaḍramawt still to
    # come (checkpoint 1). Step 2: Oman and Mahra green (checkpoint 2). Step 3: Ḥaḍramawt green (checkpoint 3).
    # Step 4 (the close's last click): ʿIkrima's ؓ whole road, al-Yamāma → Rijām → Dabā → Mahra → Abyan →
    # al-Nujayr — the campaign note §12.2's sequence, drawn schematically.
    road = path([AQR, [51.0, 23.2], RIJAM, [55.8, 24.7], DABA, [57.7, 22.2], [55.6, 18.9], [53.3, 17.2],
                 [49.0, 14.4], [46.8, 13.5], ABYAN, [46.4, 14.4], NUJAYR], "", "f1", dashed=True, width=8,
                step=4, ls=1)
    S.append(("s05-09-arabia", "Where we stand", "12 AH", [34.8, 11.6, 61.2, 31.4], [
                  area(NORTH, "f1", "", 0.22), note(41.0, 26.2, "Najd and the Ḥijāz", 24),
                  area(YAMAMA, "f1", "", 0.28), note(47.0, 24.7, "al-Yamāma", 22),
                  area(M4.WEST_YEMEN, "f1", "", 0.22), note(43.9, 14.2, "the Yemen", 22),
                  area(BAHRAYN, "f5", "", 0.30), note(49.9, 27.9, "Bahrayn", 24),
                  until(area(OMAN_A, "f4", "", 0.30), 1),
                  until(area(MAHRA_A, "f4", "", 0.30), 1),
                  note(57.4, 22.0, "Oman", 24), note(54.2, 18.6, "Mahra", 24),
                  until(area(M4.HADRAMAWT, "f5", "", 0.34), 2), note(50.0, 16.55, "Ḥaḍramawt", 24),
                  pl("Madina", "left"),
                  area(OMAN_A, "f1", "", 0.30, step=2), area(MAHRA_A, "f1", "", 0.30, step=2),
                  area(M4.HADRAMAWT, "f1", "", 0.30, step=3),
                  road, note(52.6, 12.9, "ʿIkrima's ؓ road", 24, step=4),
              ], {}))
    return S


def battle(name, lon, lat, label_pos="below", step=1):
    return {"id": MS._uid("b"), "type": "battle", "lon": lon, "lat": lat, "name": name, "date": "", "ur": "",
            "labelPos": label_pos, "step": step, "note": "site approximate"}


MED, MECCA = xy("Madina"), xy("Makkah")
BIR = (41.15, 25.55)           # Biʾr Maʿūna — site approximate: "between Banū ʿĀmir's land and Banū Sulaym's ḥarra"
TUSTAR = (48.85, 32.05)         # Tustar (Shushtar), Khūzistān — placement only
ISTAKHR = xy("Istakhr")
ABYSSINIA = (39.45, 15.6)       # the African shore — the ship's landfall, not a city
COAST = (39.18, 20.95)          # "somewhere in Tihāma" (TRN7) — the coast south of Mecca, schematic
DABA, SUHAR = xy("Daba"), xy("Sohar")
RIJAM = (54.2, 23.45)           # «قريب من عمان» (al-Kāmil 2:225–226) — a label, not a located site
DAWS = (41.45, 20.05)           # the Daws country in the Sarāt — placement only
SANA, NUJAYR, ABYAN = xy("Sana"), xy("al-Nujayr"), M4.ABYAN   # al-Nujayr: the gazetteer's approximate point
# Kinda and Ḥaḍramawt as two neighbouring zones (YK07's Map: line). Schematic — no page draws the boundary.
KINDA_Z = [[46.30, 17.20], [48.40, 17.10], [48.50, 15.30], [47.60, 14.80], [46.20, 15.10]]
HADR_Z = [[48.55, 17.20], [51.10, 17.30], [51.20, 15.40], [49.90, 14.70], [48.60, 15.25]]
RING = [[48.30, 15.92], [48.49, 15.81], [48.49, 15.59], [48.30, 15.48], [48.11, 15.59], [48.11, 15.81]]
YAMAMA = [[45.8, 25.7], [47.9, 25.5], [48.2, 23.7], [46.3, 23.4], [45.75, 24.5]]        # evening 4's outline
NORTH = [[36.2, 28.2], [38.8, 29.8], [44.4, 29.6], [46.2, 27.2], [45.6, 25.8], [45.0, 22.8], [43.4, 19.2],
         [41.6, 17.9], [39.2, 20.4], [37.6, 23.8]]
BAHRAYN = [[47.9, 28.4], [50.5, 26.9], [50.4, 24.6], [48.5, 25.0], [48.0, 26.6]]
OMAN_A = [[55.7, 26.3], [56.5, 24.3], [58.9, 23.5], [59.8, 22.4], [57.9, 20.1], [55.3, 21.9], [55.1, 24.4]]
MAHRA_A = [[52.2, 18.8], [55.0, 19.5], [56.6, 18.1], [53.5, 16.3], [52.2, 16.1]]


# Every map slide of the evening: (scene slug, first step, last step). The first step is the ground the
# slide opens on; each later step is one click.
SLIDES = [
    ("s05-01-aqraba", 1, 6),                                   # the recap before RC67
    ("s05-02-tustar", 1, 2),                                   # HS17
    ("s05-03-salim", 1, 2),                                    # AS06
    ("s05-04-ikrima-flight", 1, 2), ("s05-04-ikrima-flight", 2, 4),     # TRN6, TRN7
    ("s05-05-oman", 1, 6),                                     # RC70
    ("s05-06-daba", 1, 5),                                     # RC29
    ("s05-07-mahra", 1, 5),                                    # RC30
    ("s05-10-kinda", 1, 3), ("s05-10-kinda", 3, 6), ("s05-10-kinda", 6, 8),       # YK07, YK08, YK09
    ("s05-10-kinda", 8, 10), ("s05-10-kinda", 10, 13), ("s05-10-kinda", 13, 16),  # YK10, YK19, YK11
    ("s05-09-arabia", 1, 4),                                   # the close
]

STYLE = dict(M4.STYLE)


def build(only=()):
    os.makedirs(MS.OUT, exist_ok=True)
    made = []
    for slug, title, subtitle, bbox, objects, style in scenes():
        if only and not any(o in slug for o in only):
            continue
        objects = [o for o in objects if o]
        steps = max([o.get("step", 1) for o in objects] + [o.get("until", 0) + 1 for o in objects if o.get("until")] + [1])
        scene = {
            "schema": 1,
            "meta": {"title": title, "subtitle": subtitle, "urduTitle": "",
                     "note": "Generated by S05_yamama_dead_oman_mahra/make_maps.py from the Map: lines and beats "
                             "of the evening-5 cards. Sites placed approximately; outlines schematic, not "
                             "frontiers. Armies with a 'follows' field travel along that arrow on their click."},
            "view": MS.fit(bbox),
            "factions": copy.deepcopy(FACTIONS),
            "objects": objects,
            "underlay": None,
            "style": dict(STYLE, **style),
            "steps": {"count": steps, "current": steps, "mode": "upto"},
        }
        p = os.path.join(MS.OUT, slug + ".json")
        with open(p, "w", encoding="utf-8") as f:
            json.dump(scene, f, ensure_ascii=False, indent=2)
        made.append((slug, p, len(objects), steps))
    return made


def render(made):
    os.makedirs(OUT_PNG, exist_ok=True)
    paths = {slug: p for slug, p, _, _ in made}
    for slug, p, n, steps in made:
        render_scene.render(p, OUT_PNG)                    # the whole steps, for the notes book
        print("  %-30s %2d objects  %d step(s)" % (slug, n, steps))
    for slug, a, b in SLIDES:
        if slug in paths:
            m = render_scene.render_layers(paths[slug], OUT_PNG, a, b)
            with open(m, encoding="utf-8") as f:
                k = len({x["enter"] for x in json.load(f)["layers"] if x["enter"]})
            print("  %-30s steps %d-%d  -> %s" % (slug, a, b, os.path.basename(m)))


if __name__ == "__main__":
    render(build(sys.argv[1:]))
