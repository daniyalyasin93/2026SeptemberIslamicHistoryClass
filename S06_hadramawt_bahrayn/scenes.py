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
    s.force("al-Mundhir ؓ", "f1", 50.05, 26.1, sub="holds Bahrayn")

    s.at(4, "11 AH. The Prophet ﷺ dies — and shortly after him, al-Mundhir ؓ.")
    s.leave("al-Mundhir ؓ")
    s.say("al-Mundhir ؓ dies", near=(51.5, 26.0))

    s.at(5, "Rabīʿa turn. al-Jārūd ؓ brings his own tribe, ʿAbd al-Qays, back — and they hold.")
    s.turn("bahrayn", "f4")
    s.force("al-Jārūd ؓ", "f1", 50.15, 24.6, sub="ʿAbd al-Qays hold")
    s.say("Rabīʿa turn", near=(51.5, 26.6))

    s.at(6, "al-Ḥuṭam b. Ḍubayʿa comes out, at the head of Bakr b. Wāʾil.")
    s.force("al-Ḥuṭam", "f4", 48.3, 28.25, sub="Bakr b. Wāʾil")

    s.at(7, "al-ʿAlāʾ ؓ leaves Medina — sixteen riders, and a letter.")
    s.force("al-ʿAlāʾ ؓ", "f1", 40.9, 23.3, sub="sixteen riders")

    s.at(8, "Thumāma b. Uthāl ؓ joins him, with the Muslims of Banū Ḥanīfa.")
    s.march("al-ʿAlāʾ ؓ", to=(45.6, 23.6), via=[(43.2, 23.7)], sub="+ Banū Ḥanīfa")

    s.at(9, "Qays b. ʿĀṣim joins, and other clans of Tamīm — a force the size of his own.")
    s.march("al-ʿAlāʾ ؓ", to=(46.9, 24.3), via=[(46.3, 23.8)], sub="+ clans of Tamīm")

    s.at(10, "Into al-Dahnāʾ. He camps in the middle of it.")
    s.march("al-ʿAlāʾ ؓ", to=(47.5, 26.5), via=[(47.2, 25.4)], sub="an army now")
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
    s.force("al-Jārūd ؓ", "f1", 50.02, 25.33, sub="ʿAbd al-Qays")

    s.at(2, "al-Ḥuṭam comes down at al-Qaṭīf and at Hajar.")
    s.march("al-Ḥuṭam", "f4", frm=(49.35, 26.98), to=(49.47, 25.86), via=[(49.80, 26.52), (49.62, 26.15)],
            sub="Bakr b. Wāʾil")

    s.at(3, "al-Khaṭṭ is won over, with the Zuṭṭ and the Sabābija who live in it.")
    s.region("khatt", [(49.98, 26.28), (50.22, 26.28), (50.22, 26.04), (49.98, 26.04)], "f4", opacity=0.34)
    s.say("al-Khaṭṭ is won over", near=(50.75, 26.05))

    s.at(4, "He sends a force across the water, to Dārīn.")
    s.sail("his force", to=(50.56, 26.47), frm=(49.97, 26.40), via=[(50.25, 26.36)], faction="f4",
           sub="sent to Dārīn")

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
    s.force("al-Ḥuṭam", "f4", *at(960, 470), sub="Bakr b. Wāʾil")
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

    s.at(7, "A noise in the night. ʿAbd Allāh b. Ḥadhf goes to find out.")
    s.march("Ibn Ḥadhf", "f1", frm=at(600, 330), to=at(770, 330), via=[at(690, 322)], sub="", keep_road=False)
    s.say("a noise in the night", near=at(1000, 250))

    s.at(8, "They seize him at their trench — and he calls for his uncle.")
    s.say("seized — he calls for his uncle", near=at(1000, 250))

    s.at(9, "Fed, mounted, and let through. He tells al-ʿAlāʾ ؓ: they are drunk.")
    s.march("Ibn Ḥadhf", to=at(580, 300), via=[at(680, 290)], sub="“they are drunk”", keep_road=False)

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
    s.force("al-ʿAlāʾ ؓ", "f1", 49.80, 25.62, sub="holds the camp")
    s.force("the men of Dārīn", "f4", 50.66, 26.80, sub="never came to Hajar")

    s.at(2, "The bulk of the beaten take ship for Dārīn. The rest go home, to their own tribes' lands.")
    s.sail("the beaten", to=(50.56, 26.47), frm=(50.12, 25.80), via=[(50.42, 25.98), (50.52, 26.22)],
           faction="f4", sub="by ship")
    s.march("the rest", "f4", frm=(49.45, 25.75), to=(48.78, 26.22), via=[(49.12, 26.0)], sub="going home",
            dashed=True)

    s.at(3, "al-ʿAlāʾ ؓ writes to the Muslims of Bakr b. Wāʾil: sit in wait on every road.")
    # the banners carry the short name; the slide's key and the notes carry each man's name in full
    s.force("ʿUtayba", "f1", 48.46, 26.72, sub="on the roads")
    s.force("al-Muthannā", "f1", 48.46, 25.62, sub="on the roads")
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


def kinda():
    """Evening 5's Ḥaḍramawt scene, brought up to the map rules: no in-map box, names that can be read."""
    d = json.load(open(os.path.join(SCENES, "s05-10-kinda.json"), encoding="utf-8"))
    d["style"] = dict(d["style"], cartouche=False, legend=False)
    d.setdefault("meta", {})["kind"] = "theatre"
    # M5, every arrow says who is moving. Evening 5 drew thirteen arrows and gave four an owner. The ṣadaqa
    # arrows are a flow, and the caption of their click says so; every other one is a prong of a force that
    # is standing on the map when it is drawn.
    ziyad, ashath, muhajir = "Ziyād b. Labīd ؓ", "al-Ashʿath b. Qays", "al-Muhājir ؓ"
    his = {"r_0097": ziyad, "r_0099": ziyad, "r_0100": ziyad, "r_0101": ziyad, "r_0102": ziyad, "r_0103": ziyad,
           "r_0105": ashath, "r_0107": muhajir}
    ends = {"r_0106": [49.22, 15.66],            # al-Muhājir ؓ comes up BESIDE Ziyād ؓ, not onto his banner
            "r_0108": [47.86, 16.14]}            # and ʿIkrima ؓ clear of al-Nujayr's name
    for o in d["objects"]:
        if o["type"] in ("settlement", "army", "battle"):
            o["scale"] = max(o.get("scale") or 1.0, NAME)
        if o["type"] == "label":
            o["size"] = max(o.get("size") or 0, 24)
        if o["type"] == "arrow":
            if o["id"] in ("r_0095", "r_0096"):
                o["note"] = "said"
            elif o["id"] in his:
                o["note"] = "prong:" + his[o["id"]]
            if o["id"] in ends:
                o["pts"][-1] = list(ends[o["id"]])
        if o["id"] == "t_0137":
            o["note"] = "siege"                  # the ring round al-Nujayr: it says where; s06-nujayr says how
        if o["type"] == "army" and o.get("follows") in ends:
            o["lon"], o["lat"] = ends[o["follows"]]
    settle(d)                                        # names take the side where they cover nothing (M15)
    settle_captions(d, "s06-kinda")                  # and a caption that is on something moves off it
    settle(d)
    return d


NUJAYR = (48.30, 15.70)          # "a strong fort in the Yemen" is all the page says: evening 5's approximate site


def nujayr():
    """The siege of al-Nujayr — a DIAGRAM. Every move is one clause of ⁨الکامل ج۲ ص۲۳۱⁩, in its order:
    al-Muhājir ؓ came down on them; the Muslims besieged them; ʿIkrima ؓ arrived and the siege grew hard;
    raiding parties spread out; those inside came out, fought, lost many, and went back to their fort.
    The page gives no side to any commander and no size to the fort. Nothing here is placed by coordinates."""
    s = closeup("s06-nujayr", "al-Nujayr", NUJAYR, 26, diagram=True, relief=0.25)
    at = s.spot
    s.place("al-Nujayr", *at(800, 420), tier="fort", pos="above")
    s.force("Kinda", "f4", *at(905, 455), sub="inside the fort")

    s.at(2, "al-Muhājir ؓ comes down on them, with Ziyād ؓ. The Muslims besiege the fort.")
    ring = s.siege(*at(820, 440), faction="f1", r=190 / s.view["scale"], arms=0)
    s.march("al-Muhājir ؓ", "f1", frm=at(40, 300), to=at(430, 330), via=[at(230, 300)], sub="")
    s.march("Ziyād b. Labīd ؓ", "f1", frm=at(1560, 250), to=at(1230, 300), via=[at(1400, 260)], sub="")

    s.at(3, "ʿIkrima ؓ arrives with the main body. The siege grows hard.")
    s.march("ʿIkrima ؓ", "f1", frm=at(60, 800), to=at(560, 700), via=[at(300, 780)], sub="the main body")
    s.say("the siege grows hard", near=at(1150, 640))

    s.at(4, "Raiding parties spread out through the country, after the rest.")
    for k, (x, y) in enumerate([(120, 120), (1500, 520), (980, 860)]):
        o = s._add("arrow", "prong:al-Muhājir ؓ", pts=[list(at(430, 330)) if k == 0 else list(at(1230, 300)) if k == 1
                                                         else list(at(560, 700)),
                                                         list(at((x + 800) / 2, (y + 440) / 2 + (60 if k == 2 else -40))),
                                                         list(at(x, y))],
                   faction="f1", label="", ur="", dashed=True, width=6.0)
        o["until"] = s.step
    s.say("raiding parties", near=at(1300, 120))

    s.at(5, "Those inside come out and fight. Many are killed — and they go back to their fort.")
    s.clash(*at(680, 560))
    s.say("they come out — and go back in", near=at(1150, 640))
    return s


def main(draft=False):
    t = theatre()
    made, files = [], {}
    for s in (t, coast(t), hajar(t), flight(t), strait(t), nujayr()):
        s.save(draft=draft)
        files[s.slug] = s.data()
        made.append((s.slug, s.step, s))
    for slug, d in (("s06-arabia", arabia()), ("s06-kinda", kinda())):
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
