# -*- coding: utf-8 -*-
"""Evening 6 — the map renders (DECISIONS.md #58).

    python S06_hadramawt_bahrayn/make_maps.py
      -> visuals/maps/<scene>-step-NN.png          whole steps, for the checkpoint maps
      -> visuals/maps/<scene>-r<a>-<b>-base.png    one slide's ground
      -> visuals/maps/<scene>-r<a>-<b>-layers.json its moving marks, and where each enters

UNLIKE EVENING 5, THIS BUILDS NO SCENES. Evening 5's make_maps.py generates its s05-* scenes from the
gazetteer; evening 6 uses scenes that already exist and were authored in Map Studio:

  bahrain-darin   14 steps — authored 2026-10-07; it had been a single static step since the v1 decks
  s05-10-kinda    16 steps — evening 5's, reused unchanged, so Ḥaḍramawt is drawn exactly as it was built
  s06-arabia       4 steps — copied from s05-09-arabia so the ground is identical, with this evening's steps

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
    ("bahrain-darin", 1, 3),      # RC72  al-Ḥuṭam takes al-Qaṭīf and Hajar
    ("bahrain-darin", 4, 5),      # RC24  Juwātha besieged, and ʿAbd al-Qays hold
    ("bahrain-darin", 6, 8),      # RC25  the sixteen riders, al-Dahnāʾ, and on to Hajar
    ("bahrain-darin", 9, 11),     # RC26  the pincer, the trench month, al-Ḥuṭam killed
    ("bahrain-darin", 12, 14),    # RC27  they take ship, the roads closed, the crossing
    ("s05-10-kinda", 1, 3),       # YK07  the ṣadaqa both ways, then refused
    ("s05-10-kinda", 3, 6),       # YK08  two camps, the night strike, Kinda rises
    ("s05-10-kinda", 6, 8),       # YK09  the pastures as strongholds, one man leaves
    ("s05-10-kinda", 8, 10),      # YK10  five sides, the four kings
    ("s05-10-kinda", 10, 13),     # YK19  the column home, al-Ashʿath across it
    ("s05-10-kinda", 13, 16),     # YK11  al-Muhājir ؓ ahead, al-Nujayr ringed
    ("s06-arabia", 1, 4),
]

WHOLE = ["s06-arabia"]            # the checkpoint maps are static steps, not click layers


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
