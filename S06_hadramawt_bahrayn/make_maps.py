# -*- coding: utf-8 -*-
"""Evening 6 — the map renders (DECISIONS.md #58).

    python S06_hadramawt_bahrayn/make_maps.py
      -> visuals/maps/<scene>-step-NN.png          whole steps, for the checkpoint maps
      -> visuals/maps/<scene>-r<a>-<b>-base.png    one slide's ground
      -> visuals/maps/<scene>-r<a>-<b>-layers.json its moving marks, and where each enters

UNLIKE EVENING 5, THIS BUILDS NO SCENES. Evening 5's make_maps.py generates its s05-* scenes from the
gazetteer; evening 6 uses scenes that already exist and were authored in Map Studio:

  s06-bahrayn, -coast, -hajar, -flight, -darin   written by scenes.py through series/mapkit.py
  s06-kinda    evening 5's Ḥaḍramawt scene, brought up to the map rules by scenes.py
  s06-arabia   evening 5's checkpoint ground, with this evening's steps

Run scenes.py first: it writes the scene files this renders.

So this file is a render list, not a drawing. Edit the scenes in tools/mapstudio/ (double-click index.html)
and re-run; the slide ranges below are what build.py places, and the two must agree.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "tools"))
import render_scene                                           # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(errors="replace")

SCENES = os.path.join(ROOT, "tools", "mapstudio", "scenes")
OUT_PNG = os.path.join(HERE, "visuals", "maps")

# every map slide of the evening, as (scene, first step, last step) — build.py's MAP_FOR must match
SLIDES = [
    ("s06-arabia", 1, 2),             # RC80  the year opens: the two fronts not yet told
    ("s06-bahrayn", 1, 3),            # the situation: the Prophet's ﷺ letter, and Bahrayn under Islam
    ("s06-bahrayn", 3, 6),            # RC71  al-Mundhir ؓ dies, Rabīʿa turn, al-Ḥuṭam comes out
    ("s06-bahrayn-coast", 1, 5),      # RC72  al-Qaṭīf and Hajar, al-Khaṭṭ, the force to Dārīn, Juwāthā besieged
    ("s06-bahrayn", 6, 10),           # RC25  sixteen riders, the men who joined, into al-Dahnāʾ
    ("s06-bahrayn-hajar", 1, 6),      # RC26  the line of four, the trenches, a month          (a diagram)
    ("s06-bahrayn-hajar", 6, 9),      # RC73  the noise, Ibn Ḥadhf, his uncle, and back
    ("s06-bahrayn-hajar", 9, 11),     # RC74  over the trench, and al-Ḥuṭam
    ("s06-bahrayn-flight", 1, 3),     # RC84  the beaten take ship, the rest go home; the roads are shut
    ("s06-bahrayn-darin", 1, 4),      # RC27  to the shore, into the water, Dārīn            (a diagram)
    ("s06-kinda", 1, 3), ("s06-kinda", 3, 6), ("s06-kinda", 6, 8),
    ("s06-kinda", 8, 10), ("s06-kinda", 10, 13), ("s06-kinda", 13, 16),
    ("s06-nujayr", 1, 5),             # the siege, before YK12                              (a diagram)
    ("s06-arabia", 2, 5),             # the close
]

# whole steps: the checkpoint maps, and every scene step by step for the notes book and for the eye
WHOLE = ["s06-arabia", "s06-bahrayn", "s06-bahrayn-coast", "s06-bahrayn-hajar", "s06-bahrayn-flight",
         "s06-bahrayn-darin", "s06-kinda", "s06-nujayr"]


def main(only=None):
    os.makedirs(OUT_PNG, exist_ok=True)
    for slug in WHOLE:
        if only and only not in slug:
            continue
        n = render_scene.render(os.path.join(SCENES, slug + ".json"), OUT_PNG)
        print("   %-16s whole: %s" % (slug, n))
    seen = {}
    for slug, a, b in SLIDES:
        if only and only not in slug:
            continue
        man = render_scene.render_layers(os.path.join(SCENES, slug + ".json"), OUT_PNG, a, b)
        import json
        with open(man, encoding="utf-8") as f:
            k = len({x["enter"] for x in json.load(f)["layers"] if x["enter"]})
        seen["%s %d-%d" % (slug, a, b)] = k
        print("   %-16s %2d-%-2d  %d click(s)" % (slug, a, b, k))
    print("\n   build.py's MAP_FOR must carry exactly this many ▶ CLICK lines per slide:")
    for k, v in seen.items():
        print("     %-24s %d" % (k, v))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
