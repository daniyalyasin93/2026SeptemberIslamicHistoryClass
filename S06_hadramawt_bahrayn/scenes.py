# -*- coding: utf-8 -*-
"""Evening 6 — the maps, written as the story is told (docs/VISION.md §5).

    python S06_hadramawt_bahrayn/scenes.py        # writes tools/mapstudio/scenes/s06-*.json

One theatre map and three close-ups for Bahrayn, built with series/mapkit.py so that the rules Daniyal set
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
from mapkit import Scene, SCENES, STYLE, NAME, SAY, check_scene      # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

MEDINA, YAMAMA = (39.61, 24.47), (46.72, 24.63)
HAJAR, JUWATHA, QATIF = (49.588, 25.383), (49.90, 25.45), (50.01, 26.56)
KHATT, DARIN = (50.10, 26.16), (50.24, 26.66)
BAHRAYN = [(48.5, 27.4), (50.2, 27.3), (50.8, 26.2), (50.5, 24.7), (48.9, 24.6), (48.3, 25.8)]
ISLAND = [(50.16, 26.72), (50.30, 26.74), (50.34, 26.64), (50.26, 26.57), (50.15, 26.61)]


def theatre():
    """From Medina to the Gulf. The situation, then the rising, then al-ʿAlāʾ's ؓ road.

    At this scale a name is four degrees wide, so the map carries few of them and short ones; the captions
    stand in the empty north-west, where nothing happens."""
    cap = (42.6, 27.7)
    s = Scene("s06-bahrayn", "Bahrayn", box=(38.2, 53.2, 21.9, 29.0))
    s.place("Medina", *MEDINA, tier="capital", pos="left")
    s.place("Hajar", *HAJAR, tier="city", pos="below")
    s.name("al-Yamāma", 44.9, 25.75)
    s.name("al-Dahnāʾ", 47.7, 28.05)
    s.name("BAHRAYN", 51.4, 28.3)
    s.region("bahrayn", BAHRAYN, "f5")

    s.at(2, "The Prophet ﷺ sends al-ʿAlāʾ b. al-Ḥaḍramī ؓ to al-Mundhir b. Sāwā, who holds Bahrayn.")
    s.letter(MEDINA, HAJAR)
    s.say("a letter from the Prophet ﷺ", *cap)

    s.at(3, "Bahrayn comes under Islam, and al-Mundhir ؓ holds it for him.")
    s.turn("bahrayn", "f1")
    s.force("al-Mundhir ؓ", "f1", 51.3, 26.3, sub="holds Bahrayn", pos="right")

    s.at(4, "11 AH. The Prophet ﷺ dies — and shortly after him, al-Mundhir ؓ.")
    s.leave("al-Mundhir ؓ")
    s.say("al-Mundhir ؓ dies", *cap)

    s.at(5, "Rabīʿa turn — all of Bahrayn but al-Jārūd ؓ and those with him.")
    s.turn("bahrayn", "f4")
    s.force("al-Jārūd ؓ", "f1", 51.2, 24.1, sub="holds firm", pos="below")
    s.say("Rabīʿa turn", *cap)

    s.at(6, "al-Ḥuṭam b. Ḍubayʿa comes out, at the head of Bakr b. Wāʾil.")
    s.force("al-Ḥuṭam", "f4", 51.3, 26.5, sub="Bakr b. Wāʾil", pos="right")

    s.at(7, "al-ʿAlāʾ ؓ leaves Medina — sixteen riders, and a letter.")
    s.force("al-ʿAlāʾ ؓ", "f1", 40.9, 23.3, sub="sixteen riders", pos="below")

    s.at(8, "Thumāma b. Uthāl ؓ joins him, with the Muslims of Banū Ḥanīfa.")
    s.march("al-ʿAlāʾ ؓ", to=(45.6, 23.6), via=[(43.2, 23.7)], sub="+ Banū Ḥanīfa")

    s.at(9, "Qays b. ʿĀṣim joins, and others of Tamīm — a force the size of his own.")
    s.march("al-ʿAlāʾ ؓ", to=(46.9, 24.3), via=[(46.3, 23.8)], sub="+ Tamīm")

    s.at(10, "Into al-Dahnāʾ. He camps in the middle of it.")
    s.march("al-ʿAlāʾ ؓ", to=(47.6, 26.6), via=[(47.2, 25.4)], sub="an army now", pos="left")
    return s


def coast():
    """The Bahrayn coast: what al-Ḥuṭam did, in the order the page gives it."""
    s = Scene("s06-bahrayn-coast", "The coast of Bahrayn", box=(48.85, 50.95, 24.95, 27.05), relief=0.4)
    s.place("al-Qaṭīf", *QATIF, pos="above")
    s.place("Hajar", *HAJAR, tier="city", pos="left")
    s.place("Juwāthā", *JUWATHA, pos="right")
    s.place("al-Khaṭṭ", *KHATT, pos="right")
    s.region("darin", ISLAND, "f5", opacity=0.6)
    s.place("Dārīn", *DARIN, pos="right")
    s.force("al-Jārūd ؓ", "f1", 50.0, 25.2, sub="ʿAbd al-Qays, in Juwāthā", pos="right")

    s.at(2, "al-Ḥuṭam comes down on al-Qaṭīf.")
    s.march("al-Ḥuṭam", "f4", frm=(48.95, 26.9), to=(49.55, 26.38), via=[(49.25, 26.7)], sub="Bakr b. Wāʾil",
            pos="left")

    s.at(3, "Then on Hajar. He holds both.")
    s.march("al-Ḥuṭam", to=(49.36, 25.62), via=[(49.45, 26.1)])

    s.at(4, "al-Khaṭṭ is won over, with the Zuṭṭ and the Sabābija who live in it.")
    s.region("khatt", [(49.98, 26.28), (50.22, 26.28), (50.22, 26.04), (49.98, 26.04)], "f4", opacity=0.34)
    s.say("al-Khaṭṭ joins him", 50.45, 26.0)

    s.at(5, "He sends a force across the water, to Dārīn.")
    s.sail("his force", to=(50.62, 26.40), frm=(49.7, 25.75), via=[(50.0, 26.0), (50.35, 26.25)], faction="f4",
           sub="sent to Dārīn", pos="right")

    s.at(6, "And he besieges the Muslims in Juwāthā.")
    s.siege(JUWATHA[0], JUWATHA[1], "f4", r=0.12)
    s.say("Juwāthā, besieged", 50.5, 25.62)
    return s


def hajar():
    """Close-up: the trench month, the night, and the end of al-Ḥuṭam.

    A close-up is a diagram. Hajar and Juwāthā are where they are; the two camps and the trenches are set
    apart far enough to be read, which is further apart than any page puts them."""
    s = Scene("s06-bahrayn-hajar", "Hajar", box=(49.10, 50.26, 25.06, 25.74), relief=0.3)
    s.place("Hajar", *HAJAR, tier="city", pos="above")
    s.place("Juwāthā", 49.93, 25.50, pos="right")
    s.force("al-Ḥuṭam", "f4", 49.60, 25.27, sub="Bakr b. Wāʾil", pos="below")
    s.force("al-Jārūd ؓ", "f1", 50.02, 25.33, sub="ʿAbd al-Qays", pos="below")

    s.at(2, "al-ʿAlāʾ ؓ camps against him, on the Hajar side.")
    s.march("al-ʿAlāʾ ؓ", "f1", frm=(49.12, 25.20), to=(49.28, 25.34), via=[(49.19, 25.25)], sub="",
            pos="below")

    s.at(3, "He sends for al-Jārūd ؓ: bring ʿAbd al-Qays down on him from the other side.")
    s.march("al-Jārūd ؓ", to=(49.88, 25.28), via=[(49.96, 25.30)], pos="below")

    s.at(4, "Both sides dig trenches.")
    s.trench((49.44, 25.56), (49.44, 25.16))
    s.trench((49.76, 25.56), (49.76, 25.16))
    s.say("trenches", 49.60, 25.60)

    s.at(5, "A month. They fight by turns, and go back to their trenches.")
    s.say("a month", 49.60, 25.66, size=32)

    s.at(6, "A noise in the night. ʿAbd Allāh b. Ḥadhf goes to find out.")
    s.march("Ibn Ḥadhf", "f1", frm=(49.29, 25.47), to=(49.41, 25.50), via=[(49.35, 25.50)], sub="",
            pos="above", keep_road=False)
    s.say("a noise in the night", 49.98, 25.69)

    s.at(7, "They take him at the trench — and he calls for his uncle.")
    s.clash(49.44, 25.50)
    s.say("taken — he calls for his uncle", 49.98, 25.69)

    s.at(8, "Fed, and let go. He comes back: they are drunk.")
    s.march("Ibn Ḥadhf", to=(49.27, 25.52), via=[(49.34, 25.56)], sub="“they are drunk”", pos="above",
            keep_road=False)

    s.at(9, "The Muslims go in — from both sides.")
    s.leave("Ibn Ḥadhf")
    s.march("al-ʿAlāʾ ؓ", to=(49.50, 25.40), via=[(49.39, 25.37)], pos="left")
    s.march("al-Jārūd ؓ", to=(49.70, 25.36), via=[(49.80, 25.31)], pos="right")
    s.clash(HAJAR[0], HAJAR[1])

    s.at(10, "al-Ḥuṭam is killed. The camp is taken.")
    s.leave("al-Ḥuṭam")
    s.say("al-Ḥuṭam killed", 49.60, 25.20)
    return s


def darin():
    """Close-up: the flight, the roads closed, and the crossing. The island is drawn, and drawn large."""
    isl = [(50.55, 27.20), (50.98, 27.24), (51.08, 26.94), (50.84, 26.74), (50.52, 26.84)]
    s = Scene("s06-bahrayn-darin", "Dārīn", box=(47.3, 52.7, 25.1, 27.6), relief=0.4)
    s.place("Hajar", *HAJAR, tier="city", pos="left")
    s.region("darin", isl, "f4", opacity=0.6)
    s.place("Dārīn", 50.80, 27.02, pos="above")
    s.force("al-ʿAlāʾ ؓ", "f1", 50.0, 25.2, sub="", pos="right")
    s.force("the men of Dārīn", "f4", 51.55, 27.08, sub="never came to Hajar", pos="below")

    s.at(2, "The beaten make for Dārīn, and take ship.")
    s.sail("the beaten", to=(51.0, 26.38), frm=(49.66, 25.45), via=[(49.95, 25.95), (50.4, 26.2)], faction="f4",
           sub="by ship", pos="right")

    s.at(3, "al-ʿAlāʾ ؓ writes to the Muslims of Bakr b. Wāʾil: sit in wait on every road.")
    s.march("ʿUtayba b. al-Nahhās", "f1", frm=(47.35, 27.2), to=(48.2, 27.0), via=[(47.8, 27.12)],
            sub="on the roads", pos="below")
    s.march("al-Muthannā b. Ḥāritha", "f1", frm=(47.35, 26.2), to=(48.2, 26.1), via=[(47.8, 26.16)],
            sub="on the roads", pos="below")

    s.at(4, "al-ʿAlāʾ ؓ comes down to the shore.")
    s.march("al-ʿAlāʾ ؓ", to=(49.95, 26.42), via=[(49.55, 26.1)], pos="left")

    s.at(5, "Into the water — across the gulf.")
    s.sail("al-ʿAlāʾ ؓ", to=(50.42, 26.62), via=[(50.1, 26.5), (50.26, 26.56)], pos="below")
    s.say("by ship: a day and a night", 51.5, 25.55)

    s.at(6, "Dārīn falls. He is back the same day.")
    s.leave("the beaten")
    s.leave("the men of Dārīn")
    s.turn("darin", "f1", opacity=0.6)
    s.clash(50.80, 27.0)
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
            o["lon"], o["lat"] = 45.2, 15.7
    d["objects"], d["steps"] = out, {"count": 5, "current": 5, "mode": "upto"}
    return d


def kinda():
    """Evening 5's Ḥaḍramawt scene, brought up to the map rules: no in-map box, names that can be read."""
    d = json.load(open(os.path.join(SCENES, "s05-10-kinda.json"), encoding="utf-8"))
    d["style"] = dict(d["style"], cartouche=False, legend=False)
    own = {"r_0095": "the ṣadaqa", "r_0096": "the ṣadaqa", "r_0097": "Ziyād ؓ strikes by night",
           "r_0105": "al-Ashʿath", "r_0107": "the pursuit"}
    for o in d["objects"]:
        if o["type"] in ("settlement", "army", "battle"):
            o["scale"] = max(o.get("scale") or 1.0, NAME)
        if o["type"] == "label":
            o["size"] = max(o.get("size") or 0, 24)
        if o["type"] == "arrow":
            if o["id"] in own:
                o["label"] = own[o["id"]]            # M5: an arrow says who is moving
            elif o["id"] in ("r_0099", "r_0100", "r_0101", "r_0102", "r_0103"):
                o["note"] = "siege"                  # the five columns closing on the pastures at night
        # two marks evening 5 left printed over each other (M15)
        if o["type"] == "army" and o.get("name") == "al-Muhājir ؓ":
            o["lat"], o["lon"] = o["lat"] + 0.55, o["lon"] - 0.9
            o["labelPos"] = "left"
        if o["type"] == "label" and o.get("text") == "the captives taken back":
            o["lat"] = o["lat"] - 0.28
    return d


def main():
    made = []
    for build in (theatre, coast, hajar, darin):
        s = build()
        s.save()
        made.append((s.slug, s.step, s))
    for slug, d in (("s06-arabia", arabia()), ("s06-kinda", kinda())):
        with open(os.path.join(SCENES, slug + ".json"), "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=1)
        bad = check_scene(d, slug)
        made.append((slug, d["steps"]["count"], None))
        for b in bad:
            print("   !!", b)
    for slug, steps, _ in made:
        print("   %-20s %2d steps" % (slug, steps))
    return {slug: s for slug, _, s in made if s}


if __name__ == "__main__":
    main()
