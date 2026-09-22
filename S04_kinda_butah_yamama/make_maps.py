# -*- coding: utf-8 -*-
"""Evening 4 — Map Studio scenes for al-Buṭāḥ and al-Yamāma, rendered straight to PNG.

    python S04_kinda_butah_yamama/make_maps.py
      -> tools/mapstudio/scenes/s04-*.json                        (the scenes, editable in the tool)
      -> S04_kinda_butah_yamama/visuals/maps/<scene>-step-NN.png   (every step, rendered)

Built on tools/make_scenes.py (its gazetteer, projection and object factories), modelled on
S03_yemen/make_maps.py, and writes ONLY the s04-* files, so no earlier evening's scene — some nudged by
hand in the tool — is ever regenerated over. It also renders evening 3's s03-close-stop-b.json, unchanged,
because that is this evening's Bookend IN map (DECISIONS.md #23) and on evening 3 it was never exported.

WHY IT RENDERS AS WELL AS WRITES. On evening 3 the scenes were written and the PNGs were left for a hand
export that never happened: the STOP B closing slide reached the lectern with its placeholder still in it.
A scene that is not rendered is a map the room never sees. tools/render_scene.py drives the tool's own
painter headlessly, so the PNG is exactly what Export PNG would have produced.

WHAT EACH MAP MAY SHOW. Every route, arrow and label below comes from the **Map:** line of the card it
serves, and the card id sits beside it. A slide shows the LAST step of its range in build.py's MAP_BEFORE,
and a step may draw only what that card, or an earlier one, has told — never a later card's events. No
place a card does not name; where a card names a country rather than a town (al-Jazīra, Najd, Oman) it is
a free label, not a dot.

PLACEMENT IS APPROXIMATE, AND NOT A CLAIM. Coordinates are modern and for placement only, as in
make_scenes.py; every settlement the gazetteer marks approximate carries "site approximate" in its note
(the note travels with the scene file and is never drawn on the face). Two placements are this file's own:
  * ʿAqrabāʾ is moved from make_scenes' (45.35, 25.05) to (46.45, 24.90), in Wādī Ḥanīfa near al-Jubayla —
    the conventional modern identification. A CONVENTIONAL ESTIMATE, not page-cited here.
  * Ḥajr, the town of al-Yamāma (RCT/E-RC54: "name the town of اليمامة on the map: حَجْر"), is a new key,
    "Hajr al-Yamama", at (46.72, 24.63). It is NOT the gazetteer's "Hajar", which is al-Aḥsāʾ in Baḥrayn.
    "al-Yamāma" is used only as a country label near the town.

NO URDU IS GENERATED HERE (DECISIONS.md #19). urduLabels is off, as in every scene before it.

To nudge a map by hand: open the scene in tools/mapstudio/index.html, adjust, Save over the .json, then
    python tools/render_scene.py tools/mapstudio/scenes/<scene>.json --out-dir S04_kinda_butah_yamama/visuals/maps
Re-running this file regenerates the s04-* scenes and would undo the nudge.
"""
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "tools"))
import make_scenes as MS                                  # noqa: E402
import render_scene                                       # noqa: E402
from make_scenes import G, place, area, note              # noqa: E402

# a Windows console is cp1252: "→", "ؓ" and the Arabic in a progress line would crash the run
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(errors="replace")

OUT_PNG = os.path.join(HERE, "visuals", "maps")
BOOKEND_IN = os.path.join(MS.OUT, "s03-close-stop-b.json")   # evening 3's, rendered as it stands

# ---- placement, approximate (see the docstring) --------------------------------------------------
G["Aqraba"] = dict(G["Aqraba"], lon=46.45, lat=24.90)          # conventional estimate, not page-cited
G["Hajr al-Yamama"] = {"en": "Hajr al-Yamama", "ur": "", "lon": 46.72, "lat": 24.63,
                       "tier": "city", "approx": True}
# evening 3's own coordinate for Abyan (S03_yemen/make_maps.py), so the two maps agree
G.setdefault("Abyan", {"en": "Abyan", "ur": "", "lon": 45.37, "lat": 13.12, "tier": "town", "approx": True})

# The name the room reads, with the diacritics the slides carry.
NAMES = {"Madina": "Medina", "Buzakha": "Buzākha", "al-Butah": "al-Buṭāḥ", "Aqraba": "ʿAqrabāʾ",
         "Hajr al-Yamama": "Ḥajr", "Dhu al-Qassa": "Dhū al-Qaṣṣa"}


def pl(key, label_pos="right", step=1, tier=None):
    """A gazetteer place under the name the slides use."""
    o = place(key, label_pos, step, tier)
    o["name"] = NAMES.get(key, o["name"])
    return o


def spot(name, lon, lat, label_pos="right", step=1, tier="town"):
    """A marked point that is not a town — a camp, a tent. Always approximate."""
    return {"id": MS._uid("s"), "type": "settlement", "lon": lon, "lat": lat, "name": name, "ur": "",
            "tier": tier, "labelPos": label_pos, "step": step, "note": "site approximate"}


def force(name, lon, lat, faction="f1", strength="", label_pos="right", step=1, scale=1.0, unit="mixed"):
    """An army banner at a raw lon/lat (make_scenes.army() only offsets from a gazetteer place)."""
    o = {"id": MS._uid("a"), "type": "army", "lon": lon, "lat": lat, "name": name, "ur": "",
         "faction": faction, "strength": strength, "unit": unit, "labelPos": label_pos,
         "step": step, "note": ""}
    if scale != 1.0:
        o["scale"] = scale
    return o


def path(pts, label="", faction="f1", dashed=False, width=12, step=1, ls=1.4):
    """An arrow through raw lon/lat points (S03's helper). The label sits over the MIDDLE vertex —
    Map Studio puts it at pts[len // 2] — so a labelled arrow is given three points, not two.
    `ls` lifts the label without thickening the arrow: Map Studio scales both by the object's
    `scale`, so the width is divided by the same factor."""
    o = {"id": MS._uid("r"), "type": "arrow", "pts": [list(p) for p in pts], "faction": faction,
         "label": label, "ur": "", "dashed": dashed, "width": round(width / ls, 2), "step": step}
    if ls != 1.0:
        o["scale"] = ls
    return o


def at(obj, dlon, dlat):
    """Nudge a placed object so its label clears a crowded spot (S03's helper)."""
    obj["lon"] += dlon
    obj["lat"] += dlat
    return obj


def xy(key):
    return (G[key]["lon"], G[key]["lat"])


MED, BUZ, BUT, AQR, HAJR, DQ = (xy("Madina"), xy("Buzakha"), xy("al-Butah"), xy("Aqraba"),
                                xy("Hajr al-Yamama"), xy("Dhu al-Qassa"))
MAHRA, ABYAN, OMAN = xy("Mahra"), xy("Abyan"), xy("Nizwa")     # Oman: Nizwa, placement only
# evening 3's coastal line for ʿIkrima ؓ (s03-06-the-two-armies), reused point for point
S03_COAST = [[52.0, 16.5], [49.0, 14.4], [46.8, 13.5], [45.37, 13.12]]


# The ground at ʿAqrabāʾ, shared by s04-07 and the two closing maps so the three agree. The farmland lies
# EAST of the camp — behind it, as the army comes from the west — and holds Ḥajr. Schematic, not surveyed.
FARMS = [[46.60, 25.02], [47.02, 24.98], [47.10, 24.60], [46.90, 24.42], [46.62, 24.56], [46.56, 24.80]]
AQRABA_BOX = [45.3, 24.3, 47.3, 25.45]
# RC20's walled garden. No page locates it; it is drawn on the farmland edge behind the camp, small,
# and labelled — a shape to point at while the scene is told, not a site.
GARDEN = [[46.85, 24.72], [47.05, 24.71], [47.06, 24.55], [46.84, 24.56]]   # clear of Ḥajr
# RC19's three sections, one column in front of the ridge, labels towards the enemy
SECTIONS = [("Muhājirūn", 25.16), ("Anṣār", 25.02), ("the tribes", 24.88)]
SECTION_LON = 46.00

TIGHT = {"reliefStrength": 0.35}    # 1:50m relief blown up this far is blocks; keep it a whisper

# The south, for the STOP D map — the same schematic outlines evening 3 drew (S03_yemen/make_maps.py)
WEST_YEMEN = [[42.6, 17.8], [45.5, 17.8], [46.2, 15.0], [45.4, 12.8], [43.4, 12.7], [42.8, 14.5]]
HADRAMAWT = [[47.0, 17.0], [51.5, 17.2], [52.0, 15.6], [49.5, 14.2], [47.2, 14.0]]


def the_ground(step_farms=1, strength="Banū Ḥanīfa"):
    """ʿAqrabāʾ, Ḥajr, the red block standing on the camp, and the farmland behind it (RC54)."""
    return [
        pl("Aqraba", "below"), pl("Hajr al-Yamama", "below"),
        note(47.0, 25.36, "al-Yamāma", 28),
        force("Musaylima", AQR[0], AQR[1], "f4", strength, scale=1.2),
        area(FARMS, "f4", "", 0.20, step=step_farms),
        note(46.86, 24.80, "their farms", 26, step=step_farms),
        note(46.86, 24.73, "and families", 26, step=step_farms),
    ]


def scenes():
    S = []

    # ------------------------------------------------------------------ Part I
    # ATA/E-TB18 + TB19 — Sajāḥ. The slide before TB18 shows step 3. The arrow NEVER reaches Medina,
    # which is on the map for orientation only.
    S.append(("s04-01-sajah", "Sajāḥ", "11 AH — from al-Jazīra, and back", [34.5, 21.4, 52.0, 37.4], [
        pl("Madina", "left"),
        note(41.0, 36.0, "al-Jazīra", 30),                                     # TB18: from الجزيرة
        note(42.0, 26.2, "Najd", 30),                                          # TB18: down into نجد
        path([[41.3, 35.2], [42.3, 31.3], [43.8, 27.4]], "Sajāḥ", "f4", width=13, ls=1.5),   # TB18
        note(46.4, 27.8, "Tamīm", 26),                          # TB18: the tribe she gathered there
        path([[43.8, 27.4], [45.1, 26.4], [46.4, 25.0]], "", "f4", width=13, step=2),       # TB18/19
        note(47.4, 24.0, "al-Yamāma", 30, step=2),                             # TB19: اليمامة
        path([[46.9, 25.4], [46.9, 29.2], [45.0, 33.0], [42.4, 35.4]], "back north", "f4",
             dashed=True, width=12, step=3),                          # TB19: back north to الجزيرة
    ], {}))

    # RCT/E-RC64 — the Muslims already inside al-Yamāma. The slide shows step 2.
    S.append(("s04-02-al-yamama-before", "al-Yamāma", "11 AH — before the army came",
              [44.2, 23.3, 48.8, 26.1], [
                  pl("Hajr al-Yamama", "below"),                        # RC64: Ḥajr, which is al-Yamāma
                  note(47.6, 25.3, "al-Yamāma", 30),
                  force("Musaylima", HAJR[0] + 0.25, HAJR[1] + 0.12, "f4", "Banū Ḥanīfa", scale=1.3),
                  # RC64: a second, SMALL blue marker beside the large red one
                  force("Thumāma ؓ", HAJR[0] - 0.42, HAJR[1] - 0.30, "f1", "of Banū Ḥanīfa itself",
                        label_pos="left", step=2, scale=0.95),
                  # RC64: and Shuraḥbīl ؓ on the road outside, west of it
                  force("Shuraḥbīl ؓ", 45.20, 24.95, "f1", "on the road", label_pos="left", step=2),
              ], {"reliefStrength": 0.45}))

    # ------------------------------------------------------------------ Part II
    # RCT/E-RC44 (steps 1-2, the slide) and RC45 (step 3, available, on no slide)
    S.append(("s04-03-buzakha-to-al-butah", "To al-Buṭāḥ", "11 AH — Khālid ؓ, and the Anṣār",
              [39.6, 24.9, 46.2, 28.7], [
                  pl("Buzakha", "above"), pl("al-Butah", "below"),
                  path([BUZ, [42.9, 27.3], BUT], "Khālid ؓ", "f1", width=13),   # RC44: on from بُزاخة SE
                  note(45.35, 26.95, "Tamīm", 28),                            # RC44: in the Tamīm country
                  # RC44: the Anṣār detached for two days, then rejoining
                  force("the Anṣār", BUZ[0] - 0.15, BUZ[1] - 0.55, "f1", label_pos="left", step=2,
                        scale=0.95),
                  path([[BUZ[0] + 0.1, BUZ[1] - 0.66], [42.4, 26.72], [43.05, 27.08]], "two days later",
                       "f1", dashed=True, width=9, step=2),
                  # RC45: the camp of Banū Yarbūʿ standing apart, and the Tamīm chiefs coming in to Khālid ؓ
                  # from every side except that one
                  spot("Banū Yarbūʿ", BUT[0] + 0.55, BUT[1] - 0.45, "right", step=3),
                  path([[44.0, 27.6], [44.2, 27.1], [44.2, 26.55]], "", "f4", width=8, step=3, ls=1),
                  path([[45.5, 27.2], [44.9, 26.75], [44.42, 26.45]], "", "f4", width=8, step=3, ls=1),
                  path([[45.8, 26.2], [45.1, 26.25], [44.48, 26.30]], "", "f4", width=8, step=3, ls=1),
                  path([[43.3, 25.6], [43.7, 25.95], [44.05, 26.15]], "", "f4", width=8, step=3, ls=1),
                  note(44.9, 28.2, "the chiefs of Tamīm come in", 26, step=3),
              ], {}))

    # RCT/E-RC49 — the arrow returns to Medina: the first time in the campaign the map runs backwards.
    # Dashed, so it reads as a return. RC44's arrow is drawn beneath it so there is something to reverse.
    S.append(("s04-04-back-to-medina", "Back to Medina", "11 AH — the map runs backwards",
              [37.8, 22.6, 45.4, 28.6], [
                  pl("Madina", "left"), pl("Buzakha", "above"), pl("al-Butah", "right"),
                  path([BUZ, [42.9, 27.3], BUT], "", "f1", width=10, ls=1),                  # RC44
                  path([[44.05, 26.1], [42.2, 24.95], [39.85, 24.5]], "Khālid ؓ, sent for", "f1",
                       dashed=True, width=13),                                               # RC49
              ], {}))

    # ------------------------------------------------------------------ Part III
    # RCT/E-RC63 — the hinge. NOTE: RC16's own Map line starts Khālid's ؓ arrow at al-Buṭāḥ, but RC63 —
    # the hinge card, whose quotation has him sent out from the caliph's presence — is what this follows:
    # the arrow leaves Medina. Ḥajr is on the map because RC64 has already named it.
    S.append(("s04-05-medina-to-al-yamama", "Out again", "11 AH — Medina to al-Yamāma",
              [38.4, 22.4, 48.6, 28.6], [
                  pl("Madina", "left"), pl("Hajr al-Yamama", "below"),
                  note(47.4, 25.4, "al-Yamāma", 28),
                  path([[39.85, 24.6], [43.1, 25.05], [46.35, 24.75]], "Khālid ؓ", "f1", width=14),  # RC63
                  # RC63: a second, thinner arrow behind it — the reserve Abū Bakr ؓ put at his back
                  path([[39.85, 24.3], [42.4, 24.12], [44.9, 24.45]], "the reserve", "f1", dashed=True,
                       width=9, step=2),
                  # RC63: on the way, Sajāḥ's horsemen scatter off the map to the north
                  path([[44.3, 25.55], [44.0, 26.9], [43.5, 28.5]], "Sajāḥ's horsemen", "f4",
                       dashed=True, width=9, step=2),
                  path([[44.7, 25.6], [45.2, 27.0], [45.4, 28.5]], "", "f4", dashed=True, width=8, step=2,
                       ls=1),
              ], {}))

    # RCT/E-RC15 (steps 1-3, the slide) and RC53 (step 4, available, on no slide). ʿIkrima ؓ left with the
    # eleven banners from Dhū al-Qaṣṣa (evening 2). The long line keeps evening 3's coastal points.
    ik_back = [44.3, 23.0]
    sh_halt = [45.2, 24.95]            # the same halt s04-02 draws "on the road": one place on both maps
    S.append(("s04-06-two-commanders", "Two commanders", "11 AH — ʿIkrima ؓ and Shuraḥbīl ؓ",
              [35.5, 9.8, 60.6, 27.6], [
                  pl("Dhu al-Qassa", "left", tier="fort"), pl("Hajr al-Yamama", "right"),
                  note(49.5, 25.85, "al-Yamāma", 28),
                  # RC15: ʿIkrima's ؓ arrow reaches al-Yamāma and recoils
                  path([[DQ[0] + 0.2, DQ[1] - 0.1], [43.4, 23.7], [46.3, 24.35]], "ʿIkrima ؓ", "f1",
                       width=12),
                  path([[46.2, 24.05], [45.4, 23.35], ik_back], "", "f1", dashed=True, width=9, ls=1),
                  # RC15: Shuraḥbīl's ؓ arrow halts short of it on the road
                  path([[DQ[0] + 0.2, DQ[1] + 0.25], [42.2, 25.95], sh_halt], "Shuraḥbīl ؓ", "f1",
                       width=10, step=2),
                  # RC15: then a new, very long line — east to Oman, then along the southern edge by
                  # Mahra to Abyan. "That line is one man."
                  note(59.6, 21.2, "Oman", 30, step=3),
                  pl("Mahra", "above", step=3), pl("Abyan", "below", step=3),
                  path([ik_back, [46.0, 21.9], [50.5, 22.3], OMAN, [57.0, 20.0], [54.8, 17.4]] + S03_COAST,
                       "ʿIkrima ؓ, sent on", "f1", dashed=True, width=12, step=3),
                  # RC53 (optional, on no slide): Shuraḥbīl's ؓ halted arrow reaches al-Yamāma and recoils
                  path([sh_halt, [46.35, 24.78]], "", "f1", width=10, step=4, ls=1),
                  path([[46.2, 24.98], [45.5, 25.3], [44.6, 25.3]], "", "f1", dashed=True, width=8, step=4,
                       ls=1),
              ], {}))

    # RCT/E-RC54 (steps 1-2), RC16 (3), RC17 (4), RC19 (5). The slide before RC54 shows step 2 — the
    # ground only, before Khālid ؓ arrives; the slide before RC19 shows step 5.
    S.append(("s04-07-aqraba", "ʿAqrabāʾ", "11–12 AH — the ground Musaylima chose", AQRABA_BOX,
              # RC54: the enemy camp at ʿAqrabāʾ, forty thousand (three books), the town Ḥajr named;
              # step 2 the farmland and households BEHIND the red block — no line of retreat
              the_ground(step_farms=2, strength="Banū Ḥanīfa · about 40,000") + [
                  # RC16: the army arrives from the west and halts on a ridge facing them; the tent behind
                  path([[45.05, 24.95], [45.40, 24.97], [45.72, 24.96]], "", "f1", width=12, step=3, ls=1),
                  force("Khālid ؓ", 45.80, 24.95, "f1", label_pos="above", step=3, scale=1.1),
                  spot("Khālid's ؓ tent", 45.55, 24.70, "below", step=3),
                  # RC17: the blue block pushed backwards; a red spike reaches the tent
                  path([[45.84, 24.86], [45.62, 24.81], [45.40, 24.80]], "pushed back", "f1",
                       dashed=True, width=10, step=4),
                  path([[46.38, 24.80], [46.00, 24.63], [45.63, 24.68]], "", "f4", width=10, step=4, ls=1),
                  # RC19: «امتازوا» — the line re-formed, each under its own banner
              ] + [force(n, SECTION_LON, lat, "f1", step=5, scale=0.9) for n, lat in SECTIONS] + [
                  # RC20 (step 6): the red block falls back into a walled garden and the gate is shut
                  area(GARDEN, "f4", "", 0.40, step=6),
                  note(46.95, 24.49, "the garden — the gate shut", 24, step=6),
                  path([[46.62, 24.76], [46.80, 24.68]], "", "f4", width=10, step=6, ls=1),
                  # RC21 (step 7): al-Barāʾ ؓ goes over the wall, the gate opens, and it fills blue
                  area(GARDEN, "f1", "", 0.45, step=7),
                  note(46.95, 24.43, "opened from the inside", 24, step=7),
                  force("al-Barāʾ ؓ", 46.95, 24.64, "f1", label_pos="right", step=7, scale=0.95),
              ],
              TIGHT))

    # ------------------------------------------------------------------ closing maps
    # STOP A (after RC52) — Najd blue, al-Yamāma still red, and Khālid's ؓ arrow pointing into it.
    # Dashed: at STOP A it has not happened yet.
    S.append(("s04-close-stop-a", "Where we stand", "11 AH — Najd settled; al-Yamāma not yet",
              [38.0, 22.0, 48.8, 29.2], [
                  area([[39.0, 25.3], [40.2, 28.6], [42.8, 29.0], [45.2, 27.5], [45.4, 25.5],
                        [43.4, 24.2], [40.0, 23.8]], "f1", "", 0.24),
                  note(42.3, 26.3, "Najd", 30),
                  area([[45.8, 25.7], [47.9, 25.5], [48.2, 23.7], [46.3, 23.4], [45.75, 24.5]], "f4", "", 0.26),
                  note(47.05, 25.2, "al-Yamāma", 28),
                  pl("Madina", "left"), pl("Buzakha", "above"), pl("al-Butah", "above"),
                  pl("Hajr al-Yamama", "below"),
                  path([[39.85, 24.35], [42.8, 24.3], [45.95, 24.65]], "Khālid ؓ", "f1", dashed=True,
                       width=12),
              ], {}))

    # STOP B (after RC16) — the two blocks in position at ʿAqrabāʾ, the farmland behind the red one, the
    # tent behind the blue line; Najd settled behind them. Nothing has happened yet.
    S.append(("s04-close-stop-b", "Where we stand", "11–12 AH — the armies in position",
              [43.4, 23.8, 48.0, 26.7], [
                  area([[42.0, 27.0], [45.2, 26.9], [45.7, 25.6], [45.65, 24.0], [42.0, 23.6]], "f1", "", 0.22),
                  note(44.2, 25.1, "Najd", 30),
                  pl("al-Butah", "above"),
                  area(FARMS, "f4", "", 0.22),
                  pl("Aqraba", "below"), pl("Hajr al-Yamama", "below"),
                  note(47.3, 25.6, "al-Yamāma", 28),
                  force("Musaylima", AQR[0], AQR[1], "f4", "Banū Ḥanīfa", scale=1.1),
                  force("Khālid ؓ", 45.95, 24.93, "f1", label_pos="left"),
                  spot("the tent", 45.80, 24.68, "left"),
              ], {"reliefStrength": 0.5}))

    # STOP C (after RC19) — THE PLANNED END, and evening 5's opening map: the line re-formed into
    # labelled sections facing the red block, Ḥajr and the farmland behind. No outcome, no garden.
    S.append(("s04-close-stop-c", "Where we stand", "11–12 AH — the line re-formed; the day undecided",
              AQRABA_BOX,
              the_ground() + [force(n, SECTION_LON, lat, "f1", scale=0.9) for n, lat in SECTIONS],
              TIGHT))

    # STOP D (after RC37) — the end of Part V, and evening 5's opening map if the evening reaches it:
    # al-Yamāma blue at last, the north settled, the Yemen settled since evening 3 — and Ḥaḍramawt, the
    # one front left, still grey.
    S.append(("s04-close-stop-d", "Where we stand", "12 AH — al-Yamāma taken; Ḥaḍramawt still to come",
              [37.5, 11.8, 53.8, 29.2], [
                  area([[39.0, 25.3], [40.2, 28.6], [42.8, 29.0], [45.2, 27.5], [45.4, 25.5],
                        [43.4, 24.2], [40.0, 23.8]], "f1", "", 0.24),
                  note(42.3, 26.6, "Najd", 30),
                  area([[45.8, 25.7], [47.9, 25.5], [48.2, 23.7], [46.3, 23.4], [45.75, 24.5]], "f1", "", 0.26),
                  note(47.1, 24.9, "al-Yamāma", 28),
                  area(WEST_YEMEN, "f1", "", 0.22),     # Ṣanʿāʾ names it; a label here hits Ḥaḍramawt's
                  area(HADRAMAWT, "f5", "", 0.34),
                  note(50.3, 16.5, "Ḥaḍramawt", 30),
                  note(50.3, 15.7, "the last front", 24),
                  pl("Madina", "left"), pl("Hajr al-Yamama", "below"), pl("Sana", "left"),
              # no legend on this one: it sits over Ṣanʿāʾ and the Yemen label, and the slide's own key
              # says what the two colours mean — taken at last, and the last front
              ], {"legend": False}))
    return S


STYLE = {"relief": True, "reliefStrength": 0.85, "rivers": True,
         # 70% of a 16:9 slide, read from the back of a hall: every mark and label lifted together
         "markScale": 2.0,
         # no title box: the slide's own headline carries it, and at slide size its type came out at
         # 5-9pt (evening-4 review). The legend stays, alone and larger — it is what says orange is revolt
         "cartoucheScale": 2.0,
         "graticule": False, "grain": True, "vignette": True, "cartouche": False, "legend": True,
         "scalebar": True, "urduLabels": False, "aspect": "16:9"}


def build():
    os.makedirs(MS.OUT, exist_ok=True)
    made = []
    for slug, title, subtitle, bbox, objects, style in scenes():
        objects = [o for o in objects if o]
        steps = max([o.get("step", 1) for o in objects] + [1])
        scene = {
            "schema": 1,
            "meta": {"title": title, "subtitle": subtitle, "urduTitle": "",
                     "note": "Generated by S04_kinda_butah_yamama/make_maps.py from the Map: lines of the "
                             "evening-4 cards. Sites placed approximately (ʿAqrabāʾ and Ḥajr are "
                             "conventional estimates); country and tribe names are loose labels, not "
                             "territories; area outlines are schematic, not frontiers."},
            "view": MS.fit(bbox),
            "factions": MS.FACTIONS,
            "objects": objects,
            "underlay": None,
            "style": dict(STYLE, **style),
            "steps": {"count": steps, "current": steps, "mode": "upto"},
        }
        p = os.path.join(MS.OUT, slug + ".json")
        with open(p, "w", encoding="utf-8") as f:
            json.dump(scene, f, ensure_ascii=False, indent=2)
        made.append((p, len(objects), steps))
    return made


def render(scene_paths):
    os.makedirs(OUT_PNG, exist_ok=True)
    for p in scene_paths:
        slug = os.path.splitext(os.path.basename(p))[0]
        for old in glob.glob(os.path.join(OUT_PNG, slug + "-step-*.png")):
            os.remove(old)                  # a scene that lost a step must not leave its old PNG behind
        n = len(render_scene.render(p, OUT_PNG))
        print("  %-36s %d PNG(s)" % (slug, n))


if __name__ == "__main__":
    only = sys.argv[1:]                     # optional: slugs to re-render, e.g. s04-07-aqraba
    made = build()
    for p, n, steps in made:
        print("  %-36s %2d objects  %d step(s)" % (os.path.basename(p), n, steps))
    print("rendering -> %s" % os.path.relpath(OUT_PNG, ROOT))
    todo = [p for p, _, _ in made] + [BOOKEND_IN]
    if only:
        todo = [p for p in todo if any(o in os.path.basename(p) for o in only)]
    render(todo)
