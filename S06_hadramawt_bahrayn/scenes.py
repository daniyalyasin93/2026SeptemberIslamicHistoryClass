# -*- coding: utf-8 -*-
"""Evening 6 — the maps, written as the story is told (docs/VISION.md §5).

    python S06_hadramawt_bahrayn/scenes.py        # writes tools/mapstudio/scenes/s06-*.json

One theatre map, two close-ups and two diagrams for Bahrayn, built with series/mapkit.py so that the rules Daniyal set
on 2026-10-08 hold by construction: a situation map first, every force an icon (the enemy too), tokens that
travel with the story, a siege drawn as a siege, text that can be read, and nothing over the action.

WHAT IS SOURCED AND WHAT IS SCHEMATIC. Who moved, in what order, and what happened is from the pages cited on
the cards (⁨الکامل ج۲ ص۲۲۱–۲۲۴⁩, ⁨البدایہ ج۷ ص۳۷–۴۰⁩, ⁨ج۴ ص۵۱۷⁩). WHERE things are drawn is schematic:
  * al-Khaṭṭ — the page names it and the peoples in it; it does not say where it is. The marker is approximate.
  * Dārīn — the coastline data carries no small islands, so the island is drawn, and drawn larger than life.
  * al-ʿAlāʾ's ؓ road — the page names who joined him, not the road. It is drawn through their country.
  * the men who closed the roads — the page says "on every road" and names no place for either man.
Each of these is said in the notes of its slide. None of them is a claim.
"""
import copy
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "series"))
from mapkit import (Scene, SCENES, NAME, SAY, closeup, settle, settle_captions, check_scene,      # noqa: E402
                    check_crowding, check_places)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ONE GAZETTEER: a place is drawn at the same spot on every map of the evening (mapkit.check_places).
MEDINA = (39.611, 24.471)
HAJAR = (49.588, 25.383)        # al-Hufūf, the site usually given  [CONVENTIONAL-ESTIMATE]
JUWATHA = (49.68, 25.47)        # the mosque of Jawāthā, 12 km north-east of it  [CONVENTIONAL-ESTIMATE]
QATIF = (50.01, 26.56)
KHATT = (50.10, 26.16)          # "on the sea-coast" is all the page says: the marker is approximate
DARIN = (50.24, 26.66)          # drawn: see ISLAND
BAHRAYN = [(48.5, 27.4), (50.2, 27.3), (50.8, 26.2), (50.5, 24.7), (48.9, 24.6), (48.3, 25.8)]
# Tārūt, where Dārīn stands, is 6 km across and a stone's throw from al-Qaṭīf; the coastline data does not
# carry it and at these scales it would be a dot under al-Qaṭīf's own. It is drawn three times its size and
# set off the shore — on every map alike — so that it can be seen to be an island.
ISLAND = [(50.16, 26.72), (50.30, 26.74), (50.34, 26.64), (50.26, 26.57), (50.15, 26.61)]


def theatre():
    """From Medina to the Gulf. The situation, then the rising, then al-ʿAlāʾ's ؓ road.

    At this scale a banner is a hundred kilometres across, so each stands on land beside what it is about,
    never in the water; the names find their own sides and the captions their own room (mapkit.settle)."""
    s = Scene("s06-bahrayn", "Bahrayn", box=(38.2, 53.2, 21.9, 29.0))
    s.place("Medina", *MEDINA, tier="capital")
    s.place("Hajar", *HAJAR, tier="city", pos="below")
    s.name("al-Yamāma", 44.9, 25.3)
    s.name("al-Dahnāʾ", 45.6, 28.0)
    s.name("BAHRAYN", 50.3, 27.75)                    # over the head of the tint it names — the coast, not the island
    s.region("bahrayn", BAHRAYN, "f5")

    s.at(2, "The Prophet ﷺ sends al-ʿAlāʾ b. al-Ḥaḍramī ؓ to al-Mundhir b. Sāwā, who holds Bahrayn.")
    s.letter(MEDINA, HAJAR)
    s.say("sent by the Prophet ﷺ", near=(45.0, 26.4))

    s.at(3, "Bahrayn comes under Islam, and al-Mundhir ؓ holds it for him.")
    s.turn("bahrayn", "f1")
    s.force("al-Mundhir ؓ", "f1", 50.05, 26.1)
    s.cut()

    s.at(4, "11 AH. The Prophet ﷺ dies — and shortly after him, al-Mundhir ؓ.")
    s.leave("al-Mundhir ؓ")
    s.say("al-Mundhir ؓ dies", near=(51.5, 26.0))

    s.at(5, "Rabīʿa turn. al-Jārūd ؓ brings his own tribe, ʿAbd al-Qays, back — and they hold.")
    s.turn("bahrayn", "f4")
    s.force("al-Jārūd ؓ", "f1", 50.15, 24.6)
    s.say("Rabīʿa turn", near=(51.5, 26.6))

    s.at(6, "al-Ḥuṭam b. Ḍubayʿa comes out, at the head of Bakr b. Wāʾil.")
    s.force("al-Ḥuṭam", "f4", 48.3, 28.25)
    s.cut()

    s.at(7, "al-ʿAlāʾ ؓ leaves Medina — sixteen riders, and a letter.")
    s.force("al-ʿAlāʾ ؓ", "f1", 40.9, 23.3, sub="sixteen riders")

    s.at(8, "Thumāma b. Uthāl ؓ joins him, with the Muslims of Banū Ḥanīfa.")
    s.march("al-ʿAlāʾ ؓ", to=(45.6, 23.6), via=[(43.2, 23.7)], sub="+ Banū Ḥanīfa", trail=True)

    s.at(9, "Qays b. ʿĀṣim joins, and other clans of Tamīm — a force the size of his own.")
    s.march("al-ʿAlāʾ ؓ", to=(46.9, 24.3), via=[(46.3, 23.8)], sub="+ clans of Tamīm", trail=True)

    s.at(10, "Into al-Dahnāʾ. He camps in the middle of it.")
    s.march("al-ʿAlāʾ ؓ", to=(47.5, 26.5), via=[(47.2, 25.4)], sub="an army now", trail=True)
    return s


def coast(t):
    """The Bahrayn coast: what al-Ḥuṭam did, as the page gives it — «نزل» "came down at", never "took"."""
    s = closeup("s06-bahrayn-coast", "The coast of Bahrayn", (49.9, 26.0), 117, parent=t, relief=0.4)
    s.bring("Hajar", tier="city")
    s.place("Juwāthā", *JUWATHA)
    s.place("al-Qaṭīf", *QATIF, pos="left")
    s.place("al-Khaṭṭ", *KHATT)
    s.island(ISLAND, "Dārīn", *DARIN, pos="above")
    # his tribe's own ground is all the page gives: beside Juwāthā, and the face says neither inside nor out
    s.force("al-Jārūd ؓ", "f1", 50.02, 25.33)

    s.at(2, "al-Ḥuṭam comes down at al-Qaṭīf and at Hajar.")
    s.march("al-Ḥuṭam", "f4", frm=(49.35, 26.98), to=(49.47, 25.86), via=[(49.80, 26.52), (49.62, 26.15)], sub="")

    s.at(3, "al-Khaṭṭ is won over, with the Zuṭṭ and the Sabābija who live in it.")
    s.region("khatt", [(49.98, 26.28), (50.22, 26.28), (50.22, 26.04), (49.98, 26.04)], "f4", opacity=0.34)
    s.say("al-Khaṭṭ is won over", near=(50.75, 26.05))

    s.at(4, "He sends a force across the water, to Dārīn.")
    s.sail("al-Ḥuṭam's force", to=(50.56, 26.47), frm=(49.97, 26.40), via=[(50.25, 26.36)], faction="f4", sub="")

    s.at(5, "And he sends to Juwāthā, and besieges the Muslims in it.")
    s.siege(JUWATHA[0], JUWATHA[1], "f4", r=0.06, arms=4, turn=0.26)
    s.say("Juwāthā, besieged", near=(49.2, 25.15))
    return s


def hajar(t):
    """The trench month, the night, and the end of al-Ḥuṭam — a DIAGRAM, and it says so on its face.

    The page gives sides and nothing else (⁨الکامل ج۲ ص۲۲۳⁩): al-ʿAlāʾ ؓ camped at Hajar and came down on
    al-Ḥuṭam "from the side next to Hajar"; al-Jārūd ؓ brought ʿAbd al-Qays down on him "from the side next to
    him". So the picture is a line of four — Hajar · al-ʿAlāʾ ؓ · al-Ḥuṭam · ʿAbd al-Qays — and Juwāthā,
    their own ground, beyond. No distance and no bearing is on any page; Hajar and Juwāthā in truth lie in one
    oasis, 12 km apart, and four camps cannot be drawn there. So nothing here is placed by coordinates."""
    s = closeup("s06-bahrayn-hajar", "Hajar", (49.05, 25.42), 30, parent=t, diagram=True, relief=0.3)
    at = s.spot
    s.place("Hajar", *at(205, 470), tier="city")
    s.place("Juwāthā", *at(1395, 330))
    s.name("← al-Dahnāʾ", *at(150, 250))
    ring = s.siege(*at(1395, 330), faction="f4", r=74 / s.view["scale"], arms=4, turn=0.6)
    s.force("al-Ḥuṭam", "f4", *at(960, 470))
    s.force("al-Jārūd ؓ", "f1", *at(1330, 660), sub="ʿAbd al-Qays")

    s.at(2, "al-ʿAlāʾ ؓ comes out of al-Dahnāʾ and camps at Hajar.")
    s.march("al-ʿAlāʾ ؓ", "f1", frm=at(30, 690), to=at(345, 560), via=[at(190, 650)], sub="")

    s.at(3, "He sends to al-Jārūd ؓ: bring ʿAbd al-Qays down on him from your side.")
    s.letter(at(345, 560), at(1330, 660))
    s.march("al-Jārūd ؓ", to=at(1160, 520), via=[at(1250, 600)])

    s.at(4, "And he comes down on him from the Hajar side. Every one gathers: to al-Ḥuṭam, or to al-ʿAlāʾ ؓ.")
    s.lift(ring)
    s.leave("al-Jārūd ؓ")                    # "the Muslims gathered to al-ʿAlāʾ" — no page tracks him after this
    s.march("al-ʿAlāʾ ؓ", to=at(545, 470), via=[at(450, 510)], sub="all the Muslims")
    s.say("every one gathers", near=at(960, 250))

    s.at(5, "Both sides dig trenches.")
    mine = s.trench(at(690, 270), at(690, 690), faction="f1")
    theirs = s.trench(at(810, 270), at(810, 690), faction="f4")
    s.say("trenches", near=at(750, 200))

    s.at(6, "A month. They fight by turns, and go back to their trenches.")
    s.say("a month", near=at(750, 200), size=32)

    s.cut()
    s.at(7, "A noise in the night. ʿAbd Allāh b. Ḥadhf goes to find out.")
    s.march("Ibn Ḥadhf", "f1", frm=at(600, 330), to=at(770, 330), via=[at(690, 322)], sub="", keep_road=False)
    s.say("a noise in the night", near=at(1000, 250))

    s.at(8, "They seize him at their trench — and he calls for his uncle.")
    s.say("seized — he calls for his uncle", near=at(1000, 250))

    s.at(9, "Fed, mounted, and let through. He tells al-ʿAlāʾ ؓ: they are drunk.")
    s.march("Ibn Ḥadhf", to=at(580, 300), via=[at(680, 290)], sub="“they are drunk”", keep_road=False)

    s.cut()
    s.at(10, "The Muslims go out at them, over the trench.")
    s.leave("Ibn Ḥadhf")
    theirs["until"] = 9
    mine["until"] = 9                        # they have gone over it; the picture is the camp now
    s.march("al-ʿAlāʾ ؓ", to=at(830, 480), via=[at(690, 500)], sub="", pos="above")
    s.clash(*at(1075, 395))

    s.at(11, "al-Ḥuṭam is killed. The camp is taken.")
    s.leave("al-Ḥuṭam")
    s.say("al-Ḥuṭam killed", near=at(1000, 470))
    return s


def flight(t):
    """After the night: the bulk of the beaten take ship for Dārīn, the rest go home — and the roads are shut.

    The page names two of the men who shut them and says "on every road". It names no road and gives no man a
    place: the two banners stand inland, on the way home, and that is all they claim."""
    s = closeup("s06-bahrayn-flight", "The flight", (49.9, 26.0), 117, parent=t, relief=0.4)
    s.bring("Hajar", tier="city")
    s.place("al-Qaṭīf", *QATIF, pos="left")
    s.region("darin", ISLAND, "f4", opacity=0.55)
    s.place("Dārīn", *DARIN, pos="above")
    s.force("al-ʿAlāʾ ؓ", "f1", 49.80, 25.62)
    s.force("the men of Dārīn", "f4", 50.66, 26.80, sub="never came to Hajar")

    s.at(2, "The bulk of the beaten take ship for Dārīn. The rest go home, to their own tribes' lands.")
    s.sail("the beaten", to=(50.56, 26.47), frm=(50.12, 25.80), via=[(50.42, 25.98), (50.52, 26.22)],
           faction="f4", sub="by ship")
    s.march("the rest", "f4", frm=(49.45, 25.75), to=(48.78, 26.22), via=[(49.12, 26.0)], sub="going home",
            dashed=True)

    s.at(3, "al-ʿAlāʾ ؓ writes to the Muslims of Bakr b. Wāʾil: sit in wait on every road.")
    # the banners carry the short name; the slide's key and the notes carry each man's name in full
    s.force("ʿUtayba", "f1", 48.46, 26.72)
    s.force("al-Muthannā", "f1", 48.46, 25.62)
    s.say("the roads are shut", near=(48.6, 25.1))
    return s


def strait(t):
    """The crossing — a DIAGRAM of the shore, the water and the island; the island is drawn (see ISLAND).

    He FORDED it, on horseback: "walking on what was like soft sand with water over it" (⁨البدایہ ج۷ ص۴۰⁩).
    Not a ship, and not a parted sea. "A day and a night" is what the page says the passage took SHIPS."""
    s = closeup("s06-bahrayn-darin", "Dārīn", (50.20, 26.62), 24, parent=t, diagram=True, relief=0.4)
    at = s.spot
    s.place("al-Qaṭīf", *QATIF, pos="left")
    s.region("darin", ISLAND, "f4", opacity=0.55)
    s.place("Dārīn", *DARIN)
    s.name("↓ Hajar", *at(300, 852))
    s.force("the men of Dārīn", "f4", 50.29, 26.715, sub="and the beaten")

    s.at(2, "al-ʿAlāʾ ؓ comes down to the shore.")
    s.march("al-ʿAlāʾ ؓ", "f1", frm=at(330, 880), to=at(430, 690), via=[at(360, 780)], sub="")

    s.at(3, "Into the water, on horseback — he fords the strait.")
    s.march("al-ʿAlāʾ ؓ", to=(50.165, 26.575), via=[at(560, 640), at(680, 570)], dashed=True, unit="cavalry")
    s.say("for ships: a day and a night", near=at(1150, 700))

    s.at(4, "Dārīn falls. He is back the same day.")
    s.leave("the men of Dārīn")
    s.turn("darin", "f1", opacity=0.55)
    s.clash(50.30, 26.72)
    s.say("Dārīn falls", near=at(1150, 400))
    return s


def arabia():
    """The checkpoint map: evening 5's ground, byte for byte, with this evening's steps."""
    d = json.load(open(os.path.join(SCENES, "s05-09-arabia.json"), encoding="utf-8"))
    d["meta"]["title"], d["meta"]["subtitle"] = "The peninsula, front by front", "11–12 AH"
    d["style"] = dict(d["style"], cartouche=False, legend=False)
    out, grey, green_h = [], None, None
    for o in d["objects"]:
        o = copy.deepcopy(o)
        if o["type"] == "territory" and o.get("faction") == "f4":
            continue                                   # Oman and Mahra were settled last week
        if o["type"] == "arrow" or o.get("text") == "ʿIkrima's ؓ road":
            continue
        if o["type"] == "territory" and o.get("faction") == "f1" and o.get("step") == 2:
            o["step"] = 1
        elif o["type"] == "territory" and o.get("faction") == "f1" and o.get("step") == 3:
            o["step"], green_h = 4, o                  # Ḥaḍramawt turns green on step 4
        elif o["type"] == "territory" and o.get("faction") == "f5":
            if o.get("until") == 2:
                o["until"] = 3                         # Ḥaḍramawt, not yet told, through step 3
            else:
                o["until"], grey = 2, o                # Bahrayn, not yet told, through step 2
        if o["type"] == "label":
            o["size"] = max(o.get("size") or 0, 24)
        if o["type"] == "settlement":
            o["scale"] = NAME
        out.append(o)
    green = dict(copy.deepcopy(grey), id="t_s06_bahrayn", faction="f1", step=3)
    green.pop("until", None)
    out.append(green)

    def cap(text, lon, lat, step, until=None):
        o = {"id": "l_s06_%d" % len(out), "type": "label", "lon": lon, "lat": lat, "text": text, "ur": "",
             "size": SAY, "align": "center", "step": step, "note": "say"}
        if until:
            o["until"] = until
        out.append(o)

    cap("not yet told", 55.0, 29.6, 2, 2)
    cap("not yet told", 50.3, 13.6, 2, 2)
    cap("Bahrayn, held again", 55.2, 29.6, 3, 3)
    cap("Ḥaḍramawt, the last front", 50.6, 13.6, 4, 4)
    cap("one colour", 46.5, 29.3, 5)
    for o in out:
        if o["type"] == "label" and o.get("text") == "the Yemen":
            o["lon"], o["lat"] = 43.9, 15.0
    d["objects"], d["steps"] = out, {"count": 5, "current": 5, "mode": "upto"}
    return d


KINDA = [(46.3, 17.2), (48.4, 17.1), (48.5, 15.3), (47.6, 14.8), (46.2, 15.1)]
HADRAMAWT = [(48.55, 17.2), (51.1, 17.3), (51.2, 15.4), (49.9, 14.7), (48.6, 15.25)]
PASTURES = [(46.85, 16.60), (47.30, 16.82), (47.78, 16.62), (47.02, 16.12), (47.58, 16.16)]


def hadramawt():
    """Ḥaḍramawt and Kinda, from the quarrel over the ṣadaqa to the walls of al-Nujayr — sixteen steps, the
    same sixteen evening 5 drew by hand, now written: every banner travels its road, every arrow has an owner.

    WHAT IS SCHEMATIC. The two countries are zones, not borders. The five pastures, the field of Maḥjar
    al-Zurqān and the fort of al-Nujayr are sites the page names and does not place: evening 5's approximate
    positions are kept. Nobody's camp is on a page."""
    s = Scene("s06-kinda", "Ḥaḍramawt and Kinda", box=(45.6, 51.6, 14.5, 17.4))
    s.name("Kinda", 46.80, 16.98)
    s.name("Ḥaḍramawt", 50.45, 16.98)
    s.region("kinda", KINDA, "f5")
    s.region("hadramawt", HADRAMAWT, "f5")
    s.force("Ziyād b. Labīd ؓ", "f1", 49.90, 15.60)

    s.at(2, "The arrangement: ṣadaqa carried both ways.")
    s.flow([(50.0, 16.75), (48.5, 17.0), (47.4, 16.75)])
    s.flow([(47.4, 15.75), (48.5, 15.52), (50.0, 15.8)])
    s.say("ṣadaqa, both ways", near=(48.5, 16.3))

    s.at(3, "“Carry it yourselves” — and it was not carried.")
    s.say("not carried", near=(48.5, 16.3))

    s.cut()
    s.at(4, "Two great camps face each other.")
    s.march("Ziyād b. Labīd ؓ", to=(49.05, 16.05), via=[(49.5, 15.8)], sub="")
    s.force("Banū Muʿāwiya", "f4", 47.55, 16.20)

    s.at(5, "A strike by night.")
    s.prong("Ziyād b. Labīd ؓ", [(48.80, 16.12), (48.30, 16.28), (47.92, 16.26)])
    s.say("by night", near=(48.35, 16.75))

    s.at(6, "Kinda roused: no ṣadaqa.")
    s.turn("kinda", "f4", opacity=0.34)
    s.say("no ṣadaqa", near=(47.0, 15.5))

    s.cut()
    s.at(7, "Each chief takes his own pasture as a stronghold.")
    s.leave("Banū Muʿāwiya")
    s.sites(PASTURES, until=9)
    s.say("their pastures, as strongholds", near=(47.3, 15.4))

    s.at(8, "One man and his son walk out, to Ziyād's ؓ camp.")
    s.march("Shuraḥbīl and his son", "f1", frm=(47.78, 16.62), to=(48.50, 16.52), via=[(48.15, 16.62)], sub="",
            keep_road=False)

    s.cut()
    s.at(9, "They ring the pastures in the dark — from five sides.")
    s.leave("Shuraḥbīl and his son")
    for a, m, z in [((47.30, 17.03), (47.30, 16.77), (47.30, 16.55)), ((48.02, 16.61), (47.70, 16.54), (47.43, 16.48)),
                    ((47.80, 15.95), (47.57, 16.18), (47.39, 16.36)), ((46.80, 15.95), (47.02, 16.18), (47.21, 16.36)),
                    ((46.56, 16.59), (46.89, 16.53), (47.17, 16.48))]:
        s.prong("Ziyād b. Labīd ؓ", [a, m, z])
    s.say("from five sides", near=(47.3, 15.4))

    s.at(10, "The four kings are killed.")
    s.clash(47.30, 16.45, name="the four kings", pos="above", stay=True)

    s.cut()
    s.at(11, "The column turns for home.")
    s.march("the column", "f1", frm=(47.45, 16.25), to=(48.28, 15.66), via=[(47.90, 15.92)],
            sub="property, and captives", keep_road=False)

    s.at(12, "Its road passes one man: al-Ashʿath b. Qays.")
    s.force("al-Ashʿath b. Qays", "f4", 48.62, 15.22)

    s.at(13, "He takes the captives back.")
    s.leave("the column")
    s.prong("al-Ashʿath b. Qays", [(48.58, 15.36), (48.46, 15.52), (48.33, 15.63)])
    s.say("the captives taken back", near=(48.3, 15.9))

    s.cut()
    s.at(14, "al-Muhājir ؓ rides ahead with the fastest men.")
    s.march("al-Muhājir ؓ", "f1", frm=(45.2, 15.25), to=(49.78, 15.42), via=[(46.6, 14.98), (48.5, 14.85)], sub="")
    s.say("from Ṣanʿāʾ", near=(46.4, 15.6))

    s.at(15, "Maḥjar al-Zurqān: Kinda breaks, and runs.")
    s.leave("al-Ashʿath b. Qays")
    s.leave("Ziyād b. Labīd ؓ")              # he marches with al-Muhājir ؓ now: one banner, and it says so
    s.force("Kinda", "f4", 46.75, 15.45, sub="")
    s.march("al-Muhājir ؓ", to=(47.55, 15.25), via=[(48.8, 15.2)], sub="with Ziyād ؓ")
    s.clash(47.05, 15.05, name="Maḥjar al-Zurqān", pos="below")

    s.at(16, "Kinda run for al-Nujayr. ʿIkrima ؓ brings up the main body.")
    s.place("al-Nujayr", *NUJAYR, tier="fort", pos="below")
    s.siege(48.42, 15.78, "f1", r=0.42, arms=0)
    s.march("Kinda", to=(48.62, 15.92), via=[(47.7, 15.78)], sub="")
    s.march("al-Muhājir ؓ", to=(48.95, 15.38), via=[(48.4, 15.22)], sub="")
    s.march("ʿIkrima ؓ", "f1", frm=(45.2, 15.05), to=(47.45, 15.42), via=[(46.3, 14.85), (46.95, 15.1)],
            sub="", dashed=True)
    return s


NUJAYR = (48.30, 15.70)          # "a strong fort in the Yemen" is all the page says: evening 5's approximate site


def nujayr():
    """The siege of al-Nujayr — a DIAGRAM. Every move is one clause of ⁨الکامل ج۲ ص۲۳۱⁩, in its order:
    al-Muhājir ؓ came down on them; the Muslims besieged them; ʿIkrima ؓ arrived and the siege grew hard;
    raiding parties spread out; those inside came out, fought, lost many, and went back to their fort.
    The page gives no side to any commander and no size to the fort. Nothing here is placed by coordinates."""
    s = closeup("s06-nujayr", "al-Nujayr", NUJAYR, 26, diagram=True, relief=0.25)
    at = s.spot
    s.place("al-Nujayr", *at(800, 420), tier="fort", pos="above")
    s.force("Kinda", "f4", *at(905, 455))

    s.at(2, "al-Muhājir ؓ comes down on them, with Ziyād ؓ. The Muslims besiege the fort.")
    ring = s.siege(*at(820, 440), faction="f1", r=190 / s.view["scale"], arms=0)
    s.march("al-Muhājir ؓ", "f1", frm=at(40, 300), to=at(430, 330), via=[at(230, 300)], sub="")
    s.march("Ziyād b. Labīd ؓ", "f1", frm=at(1560, 250), to=at(1230, 300), via=[at(1400, 260)], sub="")

    s.at(3, "ʿIkrima ؓ arrives with the main body. The siege grows hard.")
    s.march("ʿIkrima ؓ", "f1", frm=at(60, 800), to=at(560, 700), via=[at(300, 780)], sub="")
    s.say("the siege grows hard", near=at(1150, 640))

    s.at(4, "Raiding parties spread out through the country, after the rest.")
    for frm, mid, to in (((430, 330), (270, 190), (120, 120)), ((1230, 300), (1380, 440), (1500, 520)),
                         ((560, 700), (800, 800), (980, 860))):
        s.prong("al-Muhājir ؓ", [at(*frm), at(*mid), at(*to)], dashed=True, width=6.0)
    s.say("raiding parties", near=at(1300, 120))

    s.at(5, "Those inside come out and fight. Many are killed — and they go back to their fort.")
    s.clash(*at(680, 560))
    s.say("they come out — and go back in", near=at(1150, 640))
    return s


ARABIA = [(35.0, 28.6), (37.0, 25.2), (39.0, 21.0), (42.6, 16.2), (43.4, 12.9), (45.2, 13.0), (48.6, 14.1),
          (52.2, 16.4), (55.4, 17.6), (58.6, 20.4), (59.7, 22.5), (56.4, 25.6), (55.3, 24.3), (51.6, 24.2),
          (50.7, 25.4), (50.0, 26.8), (48.6, 28.6), (47.6, 29.6), (46.2, 29.2), (43.5, 30.4), (40.0, 31.6), (37.5, 30.6)]
PERSIA = [(44.0, 37.2), (48.0, 38.6), (54.0, 38.2), (61.0, 36.6), (62.5, 31.0), (61.0, 26.2), (57.2, 27.0),
          (54.0, 26.8), (51.4, 28.0), (50.2, 30.0), (48.4, 30.4), (47.4, 30.3), (45.4, 31.4), (43.6, 32.6),
          (41.6, 34.6), (42.2, 36.6)]
ROME = [(27.2, 40.9), (32.0, 41.8), (36.5, 41.4), (41.0, 40.4), (42.4, 38.6), (42.2, 36.8), (41.4, 34.8),
        (39.6, 33.2), (38.2, 32.2), (36.6, 30.4), (35.4, 29.4), (34.9, 29.5), (34.3, 31.3), (35.0, 32.8),
        (35.7, 34.6), (35.9, 36.2), (36.2, 36.7), (34.6, 36.6), (32.5, 36.1), (30.5, 36.3), (28.5, 36.7),
        (27.3, 37.4), (27.0, 39.0)]
MADAIN, JERUSALEM = (44.58, 33.09), (35.22, 31.78)


def empires():
    """The other side of the desert: Persia and Rome, and the first two moves toward them. Nothing is taken.

    WHAT IS SCHEMATIC, and the face says so: both zones. No page we hold gives either empire's extent
    (docs/research/the-two-empires-at-the-hinge-12-13ah.md, X); they are outlines for the eye. The three
    towns are where they are. The four roads are four roads because the page says four; it names none."""
    s = Scene("s06-empires", "Persia and Rome", box=(27, 63, 13, 40), relief=0.6)
    s.region("arabia", ARABIA, "f1", opacity=0.22)
    s.region("persia", PERSIA, "f7", opacity=0.20)
    s.region("rome", ROME, "f8", opacity=0.20)
    s.name("ARABIA", 45.5, 21.2)
    s.name("PERSIA", 56.5, 35.4)
    s.name("ROME", 33.6, 38.9)
    s.name("Syria", 36.4, 36.6)
    s.name("Iraq", 44.0, 31.3)
    s.name("in outline — not borders", *s.spot(390, 856))
    s.place("Medina", *MEDINA, tier="capital", pos="below")
    s.place("al-Madāʾin", *MADAIN, tier="city", pos="above")
    s.place("Jerusalem", *JERUSALEM, tier="city", pos="left")

    s.at(2, "Persia. You know how its king died: by his own son.")
    s.say("killed by his own son", near=(55.5, 30.5))

    s.at(3, "Rome. Its emperor is Heraclius, and Syria is his.")
    s.say("Heraclius", near=(33.5, 36.6))

    s.cut()
    s.at(4, "Khālid ؓ leaves al-Yamāma for the lower end of Iraq.")
    s.march("Khālid ؓ", "f1", frm=(46.7, 24.6), to=(48.3, 28.8), via=[(48.0, 26.8)])

    s.cut()
    s.at(5, "A letter goes to al-Madāʾin — before any army does.")
    s.letter(s.where("Khālid ؓ"), MADAIN, width=8.0)
    s.say("a letter", near=(47.6, 32.4))

    # Iraq first, then Syria: the order of the years (12, then 13), and the order Daniyal's rule asks for — the
    # story changes direction as seldom as it can. Until 2026-10-08 the roads were drawn before the letter.
    s.cut()
    s.at(6, "Then Syria: four commanders, each by a road of his own.")
    for via, to in (((37.2, 27.4), (36.0, 30.2)), ((38.0, 27.8), (36.9, 30.9)), ((38.9, 28.2), (37.8, 31.5)),
                    ((39.7, 28.6), (38.7, 32.2))):
        s.flow([MEDINA, via, to])
    s.say("four roads", near=(41.6, 28.6))
    return s


# The two fronts beyond Arabia. Every town here is where general geography puts it  [CONVENTIONAL-ESTIMATE];
# what a page names and does not place is said so in the card (al-Ḥafīr; the country of Quḍāʿa).
YAMAMA = (46.7, 24.6)
UBULLA = (47.80, 30.52)
HAFIR = (47.30, 30.05)          # named on الکامل ج۲ ص۲۳۵ and البدایہ ج۷ ص۶۴; placed by no page we hold
HIRA = (44.45, 31.89)
TABUK = (36.57, 28.38)
DAMASCUS = (36.29, 33.51)
HIMS = (36.72, 34.73)


# Where each banner and each loose name stands. At this scale a banner with its flag and its name is three
# degrees across, so none of them can stand ON the place it is about: each stands beside it, on land, where it
# covers nothing. The positions were found by search against the kit's own crowding rule, not by eye.
IRAQ_AT = {
    "muthanna_raiding": (41.6, 29.2), "khalid_yamama": (47.0, 25.2),
    "muthanna": (45.29, 29.02), "adi": (44.52, 27.48), "khalid": (47.6, 27.3), "hurmuz": (50.3, 32.2),
    "khalid_hira": (42.21, 31.42),
    "n_yamama": (45.4, 24.0), "n_persia": (54.6, 30.6), "n_hafir": (47.84, 29.76), "c_iyad": (37.5, 33.3),
}
SYRIA_AT = {
    "amr_qudaa": (39.0, 27.3), "amr_medina": (41.2, 25.4), "yazid_out": (37.2, 29.2),
    "n_syria": (40.5, 34.6), "n_qudaa": (36.6, 27.3), "c_tabuk": (34.6, 27.4), "c_usama": (38.6, 30.6),
}
CAMPS_AT = {
    "yazid": (35.93, 31.39), "shurahbil": (35.3, 32.55), "ubayda": (36.6, 32.5), "amr": (34.95, 30.48),
}


def _road(a, b, bow):
    """Three points from a to b, bowed sideways by `bow` degrees — a road of its own, not a chord."""
    dx, dy = b[0] - a[0], b[1] - a[1]
    n = (dx * dx + dy * dy) ** 0.5 or 1.0
    ox, oy = -dy / n * bow, dx / n * bow
    return [(a[0] + dx * 0.35 + ox, a[1] + dy * 0.35 + oy), (a[0] + dx * 0.72 + ox * 0.6, a[1] + dy * 0.72 + oy * 0.6)]


def iraq(at=None):
    """The opening of Iraq: the man already on the frontier, the order, three columns and one meeting-place —
    and, a year on, the letter. Nothing is fought here: the scene stops where the columns close, and says so.

    WHAT IS SCHEMATIC. The three roads (the pages say three, and name none); where each column halts, which is
    beside al-Ḥafīr and not on it; al-Muthannā's raid, which the page gives as a fact and not as a place.
    al-Ḥafīr is named by both books and placed by neither: it is a name on this map, and has no dot."""
    P = dict(IRAQ_AT, **(at or {}))
    s = Scene("s06-iraq", "Iraq", box=(38.4, 54.0, 23.2, 34.4), relief=0.5)
    s.region("arabia", ARABIA, "f1", opacity=0.18)
    s.region("persia", PERSIA, "f7", opacity=0.18)
    s.place("Medina", *MEDINA, tier="capital", pos="below")
    s.place("al-Madāʾin", *MADAIN, tier="city", pos="above")
    s.place("al-Ḥīra", *HIRA, tier="town", pos="left")
    s.place("al-Ubulla", *UBULLA, tier="town", pos="right")
    s.name("al-Yamāma", *P["n_yamama"])
    s.name("PERSIA", *P["n_persia"])
    s.name("roads in outline", *s.spot(250, 856))

    s.at(2, "al-Muthannā b. Ḥāritha is already here — raiding the edge of the Sawād, with Abū Bakr's ؓ leave.")
    m = P["muthanna_raiding"]
    s.force("al-Muthannā", "f1", m[0], m[1], pos="left")
    s.prong("al-Muthannā", [(m[0] + 0.8, m[1] + 0.5), (m[0] + 1.8, m[1] + 1.3), (44.0, 31.3)])

    s.cut()
    s.at(3, "The order reaches Khālid ؓ at al-Yamāma: to Iraq, from its lower end — beginning with al-Ubulla.")
    k = P["khalid_yamama"]
    s.force("Khālid ؓ", "f1", k[0], k[1], pos="right")
    s.letter(MEDINA, (k[0] - 0.9, k[1]))
    s.at(4, "And ʿIyāḍ b. Ghanm ؓ is ordered in from the upper end — to meet him.")
    s.say("ʿIyāḍ b. Ghanm ؓ", near=P["c_iyad"])

    s.cut()
    s.at(5, "al-Muthannā first, two days ahead — toward al-Ḥafīr.")
    s.name("al-Ḥafīr", *P["n_hafir"])
    s.march("al-Muthannā", to=P["muthanna"], via=_road(m, P["muthanna"], -0.5))
    s.at(6, "Then ʿAdī b. Ḥātim ؓ — a day behind, by a road of his own.")
    s.march("ʿAdī ؓ", "f1", frm=(k[0] - 1.0, k[1] + 0.5), to=P["adi"], via=_road((k[0] - 1.0, k[1] + 0.5), P["adi"], 0.5),
            pos="left")
    s.at(7, "Khālid ؓ last. One meeting-place for all three: al-Ḥafīr.")
    s.march("Khālid ؓ", to=P["khalid"], via=_road(k, P["khalid"], -0.5))
    s.at(8, "Hurmuz, lord of that frontier, writes to his king — and hurries to meet them.")
    h = P["hurmuz"]
    s.force("Hurmuz", "f7", h[0], h[1], pos="right")
    s.letter((h[0] - 0.9, h[1] + 0.2), MADAIN, faction="f7")

    s.cut()
    s.at(9, "A year later — the fighting is another evening's. Khālid ؓ is at al-Ḥīra; it has chosen the jizya.")
    s.leave("Hurmuz")
    s.leave("al-Muthannā")
    s.leave("ʿAdī ؓ")
    s.march("Khālid ؓ", to=P["khalid_hira"], via=_road(P["khalid"], P["khalid_hira"], 0.6))
    s.at(10, "He writes to al-Madāʾin — to Kisrā's commanders, his frontier governors and his ministers.")
    s.letter(s.where("Khālid ؓ"), MADAIN, width=8.0)
    return s


def syria(at=None):
    """The opening of Syria, wide: the road the Prophet ﷺ had taken, the letter that found ʿAmr ؓ, and the first
    of the four riding out of Medina. Where the four camped is the close-up's business (syria_camps).

    WHAT IS SCHEMATIC. The country of Quḍāʿa — the page names the tribes and no place. Yazīd's ؓ road is the one
    road a page names: by Tabūk."""
    P = dict(SYRIA_AT, **(at or {}))
    s = Scene("s06-syria", "Syria", box=(31.0, 45.0, 23.6, 35.6), relief=0.5)
    s.region("arabia", ARABIA, "f1", opacity=0.18)
    s.region("rome", ROME, "f8", opacity=0.18)
    s.place("Medina", *MEDINA, tier="capital", pos="below")
    s.place("Tabūk", *TABUK, tier="town", pos="right")
    s.place("Jerusalem", *JERUSALEM, tier="city", pos="left")
    s.place("Damascus", *DAMASCUS, tier="city", pos="right")
    s.name("SYRIA", *P["n_syria"])

    s.at(2, "Tabūk: the Prophet ﷺ led the Muslims this far toward Syria himself, in fierce heat.")
    s.say("the year of Tabūk", near=P["c_tabuk"])
    s.at(3, "And before he died, he sent Usāma b. Zayd ؓ toward these borders.")
    s.say("Usāma's ؓ army", near=P["c_usama"])

    s.cut()
    s.at(4, "A letter from Medina finds ʿAmr b. al-ʿĀṣ ؓ among Quḍāʿa, collecting the ṣadaqa.")
    s.name("Quḍāʿa", *P["n_qudaa"])
    q = P["amr_qudaa"]
    s.force("ʿAmr ؓ", "f1", q[0], q[1], pos="right")
    s.letter(MEDINA, (q[0] + 0.4, q[1] - 0.5))
    s.at(5, "He names a deputy, and comes to Medina.")
    s.march("ʿAmr ؓ", to=P["amr_medina"], via=_road(q, P["amr_medina"], 0.4))

    s.cut()
    out = (MEDINA[0] - 0.3, MEDINA[1] + 0.6)
    s.at(6, "Yazīd b. Abī Sufyān ؓ rides out first, by Tabūk — and Abū Bakr ؓ walks beside him.")
    s.march("Yazīd ؓ", "f1", frm=out, to=P["yazid_out"], via=[(38.1, 26.8), (TABUK[0] + 0.45, TABUK[1] - 0.15)])
    return s


def syria_camps(parent, at=None):
    """Where the four camped — the second scale. Each banner comes up from the south by a road of its own and
    halts beside the camp the page names for it: al-Balqāʾ, Jordan (or Buṣrā), al-Jābiya, al-ʿAraba.

    WHAT IS SCHEMATIC. The roads, and the exact spot of each banner: a banner and its name are sixty kilometres
    across even here, and al-Jābiya, Jordan and Buṣrā lie within a hundred of each other. Each stands inside the
    country the page names, clear of its neighbours."""
    P = dict(CAMPS_AT, **(at or {}))
    c = closeup("s06-syria-camps", "Syria — where they camped", (36.0, 31.9), 250, parent=parent, relief=0.45)
    c.region("rome", ROME, "f8", opacity=0.16)
    c.bring("Jerusalem", tier="city", pos="left")
    c.bring("Damascus", tier="city", pos="right")
    c.signpost("Medina")

    def up(name, key, via, cue, pos):
        c.at(c.step + 1, cue)
        c.march(name, "f1", frm=via[0], to=P[key], via=via[1:], pos=pos)

    # Yazīd first; Shuraḥbīl "followed him"; then Abū ʿUbayda (Ibn Isḥāq, البدایہ ج۷ ص۸۴). The banner beside
    # al-Jābiya stands east of it, and Shuraḥbīl's in the Jordan country west of it — so that no road has to
    # cross another man's banner to reach its own.
    up("Yazīd ؓ", "yazid", [(36.5, 29.9), (36.45, 30.5), (36.15, 31.0)],
       "Yazīd b. Abī Sufyān ؓ, first — he camps at al-Balqāʾ. Damascus is named for him.", "right")
    up("Shuraḥbīl ؓ", "shurahbil", [(35.85, 29.8), (35.55, 30.9), (35.45, 31.9)],
       "Shuraḥbīl b. Ḥasana ؓ, after him — Jordan; some say Buṣrā.", "left")
    up("Abū ʿUbayda ؓ", "ubayda", [(37.7, 30.0), (37.45, 31.2), (37.05, 32.0)],
       "Abū ʿUbayda ؓ — he camps at al-Jābiya. Ḥimṣ is named for him.", "right")
    up("ʿAmr ؓ", "amr", [(35.75, 29.5), (35.45, 29.75), (35.15, 30.1)],
       "ʿAmr b. al-ʿĀṣ ؓ — al-ʿAraba: Palestine.", "left")
    return c

def main(draft=False):
    t = theatre()
    made, files = [], {}
    sy = syria()
    for s in (t, coast(t), hajar(t), flight(t), strait(t), hadramawt(), nujayr(), empires(), iraq(), sy,
              syria_camps(sy)):
        s.save(draft=draft)
        files[s.slug] = s.data()
        made.append((s.slug, s.step, s))
    for slug, d in (("s06-arabia", arabia()),):
        with open(os.path.join(SCENES, slug + ".json"), "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=1)
        files[slug] = d
        made.append((slug, d["steps"]["count"], None))
        for b in check_scene(d, slug) + check_crowding(d, slug):
            print("   !!", b)
    for b in check_places(files):
        print("   !!", b)
    for slug, steps, _ in made:
        print("   %-20s %2d steps" % (slug, steps))
    return {slug: s for slug, _, s in made if s}


if __name__ == "__main__":
    main(draft="--draft" in sys.argv)
