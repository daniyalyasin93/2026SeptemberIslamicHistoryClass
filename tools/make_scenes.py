"""Generate Map Studio scene files — one per battle or movement in session 2's scope.

    python tools/make_scenes.py            # -> tools/mapstudio/scenes/*.json

WHY. tools/mapstudio/ draws a far better map than series/make_visuals.py can: real shaded relief,
rivers, hand-placed marks, army and battle tokens, step-by-step build-ups. But it is a click-tool,
and building sixteen scenes by hand from a blank canvas is an evening's work. So the data comes
from here — every settlement, army, battle, route and territory already placed and named — and
Daniyal opens a scene, nudges what he wants, and exports. The tool does what it is good at; this
does what it is good at. Same split as Claude-writes-the-words / Gemini-draws-the-pictures.

HOW TO USE ONE. Open tools/mapstudio/index.html, press Open, choose a file from
tools/mapstudio/scenes/, then Export PNG. Scenes with more than one step export one PNG per step
if you want the build-up across slides.

WHAT THE SCENES ARE FOR, AND WHAT THEY ARE NOT. Coordinates come from the tool's own gazetteer
(tools/mapstudio/data/places.js), which its README is explicit about: approximate modern
coordinates FOR PLACEMENT ONLY, never a claim about a site. Several of these are genuinely
disputed — بزاخة, عقرباء, دارين, أجنادين, يرموك, قادسية — and every scene generated here carries
`sites placed approximately` in its note so the caveat travels with the file. A territory outline
is a schematic, not a frontier.

NO URDU IS GENERATED HERE (DECISIONS.md #19). Where the gazetteer already carries an `ur` for a
place, it is copied through — that is existing repo data, not something written now. `urduLabels`
is off by default so an export matches the English decks; turn it on in the tool and the labels
that exist will appear.

The routes are drawn from the **Map:** lines of the cards in L02_baarah_saal/CONTENT.md, which the
researchers wrote precisely so a map could be drawn from them. Where a card gives no route, none is
invented — the scene carries the places and lets the speaker point.
"""
import json
import math
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STUDIO = os.path.join(ROOT, "tools", "mapstudio")
OUT = os.path.join(STUDIO, "scenes")

# --- the projection, mirrored from tools/mapstudio/src/proj.js so the view opens framed ---------
LAT0, STAGE_W, STAGE_H = 30.0, 1600.0, 900.0
K = math.cos(math.radians(LAT0))


def fit(bbox, pad=0.94):
    """(cx, cy, scale) for a lon/lat bbox — the same arithmetic as MS_Proj.fitBBox."""
    w, s, e, n = bbox
    x0, x1, y0, y1 = w * K, e * K, -n, -s
    scale = min(STAGE_W / max(1e-6, x1 - x0), STAGE_H / max(1e-6, y1 - y0)) * pad
    return {"cx": (x0 + x1) / 2.0, "cy": (y0 + y1) / 2.0, "scale": scale}


# --- the gazetteer, read straight out of the tool's own data file -------------------------------
ENTRY = re.compile(r'\{\s*en:\s*"([^"]+)"\s*,\s*ur:\s*"([^"]*)"\s*,\s*lon:\s*([\d.\-]+)\s*,'
                   r'\s*lat:\s*([\d.\-]+)\s*,\s*tier:\s*"([^"]+)"([^}]*)\}')


def gazetteer():
    src = open(os.path.join(STUDIO, "data", "places.js"), encoding="utf-8").read()
    g = {}
    for en, ur, lon, lat, tier, rest in ENTRY.findall(src):
        g[en] = {"en": en, "ur": ur, "lon": float(lon), "lat": float(lat),
                 "tier": tier, "approx": "approx" in rest}
    return g


G = gazetteer()

# Places session 2 needs that the gazetteer does not carry. Every one is APPROXIMATE and marked so.
EXTRA = {
    "Dhu al-Qassa":  (40.30, 24.30, "town"), "Buzakha":     (41.70, 27.50, "town"),
    "Aqraba":        (45.35, 25.05, "town"), "Juwatha":     (49.90, 25.45, "town"),
    "Darin":         (50.06, 26.53, "town"), "Daba":        (56.27, 25.63, "town"),
    "al-Butah":      (44.20, 26.30, "town"), "Suwa":        (39.40, 33.20, "town"),
    "Quraqir":       (38.20, 32.10, "town"), "Tadmur":      (38.28, 34.55, "city"),
    "Sana":          (44.207, 15.354, "city"), "al-Nujayr": (48.30, 15.70, "fort"),
    "Mahra":         (52.00, 16.50, "town"), "Nizwa":       (57.533, 22.933, "city"),
    "Hajar":         (49.588, 25.383, "city"), "Sumayra":   (42.10, 27.20, "town"),
    "Jalula":        (45.15, 34.27, "town"), "al-Jabiya":   (36.05, 32.80, "town"),
    "Ubna":          (35.20, 31.55, "town"), "Marj al-Suffar": (36.25, 33.20, "town"),
    "Jerusalem":     (35.230, 31.778, "city"), "Najran":     (44.130, 17.491, "city"),
    "Yarmuk":        (35.950, 32.720, "town"), "Ajnadayn":   (34.900, 31.700, "town"),
    "Qadisiyya":     (44.300, 31.700, "town"), "Hira":       (44.350, 31.900, "city"),
    "Madain":        (44.581, 33.096, "capital"), "Kufa":     (44.400, 32.030, "city"),
    "Nihawand":      (48.377, 34.191, "town"), "Hamadan":    (48.515, 34.799, "city"),
    "Fustat / Cairo":(31.235, 30.045, "capital"), "Tabuk":    (36.566, 28.383, "town"),
    "Damascus":      (36.292, 33.513, "capital"), "Yamama":   (47.300, 24.150, "city"),
    "Madina":        (39.611, 24.471, "capital"), "Makkah":   (39.826, 21.423, "capital"),
}
for name, (lon, lat, tier) in EXTRA.items():
    G.setdefault(name, {"en": name, "ur": "", "lon": lon, "lat": lat, "tier": tier, "approx": True})


# --- object factories, matching tools/mapstudio/src/store.js -------------------------------------
_seq = [0]


def _uid(p):
    _seq[0] += 1
    return "%s_%s" % (p, format(_seq[0], "04d"))


def place(name, label_pos="right", step=1, tier=None):
    g = G[name]
    return {"id": _uid("s"), "type": "settlement", "lon": g["lon"], "lat": g["lat"],
            "name": g["en"], "ur": g["ur"], "tier": tier or g["tier"],
            "labelPos": label_pos, "step": step,
            "note": "site approximate" if g["approx"] else ""}


def army(name, at, faction="f1", unit="mixed", strength="", label_pos="right", step=1, off=(0, 0)):
    g = G[at]
    return {"id": _uid("a"), "type": "army", "lon": g["lon"] + off[0], "lat": g["lat"] + off[1],
            "name": name, "ur": "", "faction": faction, "strength": strength, "unit": unit,
            "labelPos": label_pos, "step": step, "note": ""}


def battle(name, at, date="", label_pos="below", step=1):
    g = G[at]
    return {"id": _uid("b"), "type": "battle", "lon": g["lon"], "lat": g["lat"],
            "name": name, "ur": "", "date": date, "labelPos": label_pos, "step": step,
            "note": "site approximate" if g["approx"] else ""}


def route(names, label="", faction="f1", dashed=False, width=14, step=1):
    pts = [[G[n]["lon"], G[n]["lat"]] for n in names]
    return {"id": _uid("r"), "type": "arrow", "pts": pts, "faction": faction,
            "label": label, "ur": "", "dashed": dashed, "width": width, "step": step}


def area(pts, faction="f1", label="", opacity=0.22, step=1):
    return {"id": _uid("t"), "type": "territory", "pts": pts, "faction": faction,
            "label": label, "ur": "", "opacity": opacity, "step": step}


def note(lon, lat, text, size=24, step=1, align="center"):
    return {"id": _uid("l"), "type": "label", "lon": lon, "lat": lat,
            "text": text, "ur": "", "size": size, "align": align, "step": step}


FACTIONS = [
    {"id": "f1", "name": "Muslim forces",    "ur": "", "color": "#22B694"},
    {"id": "f2", "name": "Byzantine Rome",   "ur": "", "color": "#DC5844"},
    {"id": "f3", "name": "Sasanian Persia",  "ur": "", "color": "#9877D6"},
    {"id": "f4", "name": "Tribes in revolt", "ur": "", "color": "#E7A244"},
    {"id": "f5", "name": "Held firm",        "ur": "", "color": "#8FA6AF"},
]

# Coarse schematic outlines. NOT frontiers — see the module docstring.
ARABIA_11 = [[38.2, 27.4], [42.5, 26.0], [45.0, 22.0], [44.5, 17.0], [43.2, 13.2],
             [39.0, 19.5], [37.2, 23.0]]
EXTENT_13 = [[36.0, 33.6], [40.0, 31.5], [45.6, 32.6], [48.5, 30.2], [50.5, 26.0],
             [57.0, 23.5], [52.0, 16.0], [43.0, 12.6], [38.6, 18.0], [34.8, 28.0]]
EXTENT_23 = [[27.0, 31.5], [34.0, 36.5], [40.0, 37.0], [48.0, 36.0], [56.0, 34.0],
             [61.0, 29.0], [57.5, 22.5], [52.0, 15.8], [43.0, 12.6], [36.0, 20.0],
             [30.5, 24.0], [25.5, 27.0]]
ROME = [[27.5, 41.0], [38.5, 38.5], [39.6, 34.2], [36.2, 29.6], [33.0, 31.0], [27.5, 36.5]]
PERSIA = [[41.5, 38.5], [54.0, 38.5], [59.0, 32.0], [53.0, 27.5], [46.0, 29.5], [42.5, 33.0]]


# ================================================================= the scenes
def scenes():
    S = []

    # ---------------------------------------------------------------- 11 AH, where the map stood
    S.append(("11ah-the-map-as-it-stood", "Arabia, the morning after",
              "11 AH / 632 CE — before any arrow is drawn", [28.0, 12.0, 62.0, 40.0], [
                  area(ROME, "f2", "Byzantine Rome", 0.18),
                  area(PERSIA, "f3", "Sasanian Persia", 0.18),
                  area(ARABIA_11, "f1", "", 0.24),
                  place("Madina", "left"), place("Makkah", "left"),
                  place("Damascus", "left"), place("Madain", "left"),
                  note(33.0, 38.5, "BYZANTINE ROME", 26), note(52.0, 36.5, "SASANIAN PERSIA", 26),
              ]))

    # ---------------------------------------------------------------- Jaysh Usama
    S.append(("usama-expedition", "The army he would not call back",
              "11 AH — out to the Syrian marches, and back", [33.0, 21.0, 45.0, 34.0], [
                  place("Madina", "left"), place("Tabuk", "right"), place("Ubna", "above"),
                  army("Usama b. Zayd", "Madina", unit="cavalry", off=(-0.5, 0.4)),
                  route(["Madina", "Tabuk", "Ubna"], "out", width=15),
                  route(["Ubna", "Tabuk", "Madina"], "back", dashed=True, width=11),
                  note(38.0, 22.2, "Forty days, some say seventy", 22),
              ]))

    # ---------------------------------------------------------------- the eleven columns
    S.append(("dhu-al-qassa-the-columns", "Eleven banners leave Dhu al-Qassa",
              "11 AH — the columns sent out", [33.0, 12.0, 60.0, 34.0], [
                  place("Madina", "left"), place("Dhu al-Qassa", "above", tier="fort"),
                  place("Buzakha", "above"), place("al-Butah", "right"), place("Yamama", "right"),
                  place("Hajar", "right"), place("Daba", "right"), place("Mahra", "below"),
                  place("Sana", "below"), place("al-Nujayr", "below"), place("Tabuk", "left"),
                  army("Khalid b. al-Walid", "Dhu al-Qassa", unit="cavalry", off=(-0.6, 0.6)),
                  route(["Dhu al-Qassa", "Buzakha"], "Khalid", width=16),
                  route(["Dhu al-Qassa", "Yamama"], "Ikrima / Shurahbil"),
                  route(["Dhu al-Qassa", "Hajar"], "al-Ala b. al-Hadrami"),
                  route(["Dhu al-Qassa", "Daba"], "Hudhayfa / Arfaja"),
                  route(["Dhu al-Qassa", "Mahra"], "Ikrima, after Yamama", dashed=True),
                  route(["Dhu al-Qassa", "Sana"], "al-Muhajir b. Abi Umayya"),
                  route(["Dhu al-Qassa", "al-Nujayr"], "Ziyad b. Labid"),
                  route(["Dhu al-Qassa", "Tabuk"], "Amr b. al-As"),
                  note(45.0, 32.0, "Ten destinations are named in the sources; "
                                   "the count of banners is given as eleven", 20),
              ]))

    # ---------------------------------------------------------------- Buzakha
    S.append(("buzakha", "Buzakha — the man who walked off the field",
              "11 AH — Asad and Ghatafan", [38.0, 24.0, 46.0, 31.0], [
                  place("Madina", "below"), place("Buzakha", "above"), place("Sumayra", "below"),
                  army("Khalid b. al-Walid", "Madina", unit="cavalry", off=(0.4, 0.6)),
                  army("Tulayha", "Buzakha", faction="f4", off=(0.5, 0.5)),
                  army("Uyayna b. Hisn", "Buzakha", faction="f4", off=(0.7, -0.6)),
                  route(["Madina", "Sumayra", "Buzakha"], "Khalid", width=16),
                  battle("Buzakha", "Buzakha", "11 AH"),
                  note(43.5, 29.6, "Tulayha gets away, northwest into Syria", 22),
              ]))

    # ---------------------------------------------------------------- Yamama
    S.append(("yamama-aqraba", "Aqraba and the Garden of Death",
              "12 AH — the hardest day of the war", [43.0, 22.0, 49.0, 27.5], [
                  place("Yamama", "right"), place("Aqraba", "below"),
                  army("Khalid b. al-Walid", "Aqraba", unit="mixed", off=(-1.1, 0.5)),
                  army("Musaylima", "Aqraba", faction="f4", off=(0.9, 0.3)),
                  battle("Aqraba", "Aqraba", "12 AH"),
                  note(46.4, 23.4, "Hadiqat al-Mawt — the walled garden", 22),
                  note(44.2, 26.6, "Ikrima and Shurahbil came first, and were thrown back", 20),
              ]))

    # ---------------------------------------------------------------- Bahrain and Darin
    S.append(("bahrain-darin", "Bahrain: Juwatha, Hajar, and the crossing to Darin",
              "11–12 AH", [46.0, 22.0, 54.0, 29.0], [
                  place("Juwatha", "below"), place("Hajar", "left"), place("Darin", "above"),
                  army("al-Ala b. al-Hadrami", "Hajar", off=(-0.8, 0.5)),
                  army("al-Hutam", "Hajar", faction="f4", off=(0.7, -0.5)),
                  battle("Hajar", "Hajar", "11 AH"),
                  route(["Hajar", "Darin"], "straight across the water", width=15),
                  route(["Darin", "Hajar"], "", dashed=True, width=10),
                  note(51.0, 24.4, "The land roads were closed first", 22),
                  note(50.6, 27.6, "A day and a night by ship", 20),
              ]))

    # ---------------------------------------------------------------- the southern fronts
    S.append(("southern-fronts", "Oman, Mahra, Yemen, Hadramawt",
              "11–12 AH — the fronts settled last", [42.0, 12.0, 60.0, 27.0], [
                  place("Daba", "above"), place("Nizwa", "right"), place("Mahra", "above"),
                  place("Sana", "left"), place("al-Nujayr", "below"), place("Najran", "left"),
                  battle("Daba", "Daba", "11 AH"), battle("al-Nujayr", "al-Nujayr", "12 AH"),
                  note(50.0, 25.0, "Relief came from inside the theatre", 20),
              ]))

    # ---------------------------------------------------------------- Iraq
    S.append(("iraq-hira", "Khalid enters Iraq",
              "12 AH — al-Hira and the lower Euphrates", [42.0, 27.0, 50.0, 34.0], [
                  place("Yamama", "below"), place("Hira", "above"), place("Madain", "above"),
                  army("Khalid b. al-Walid", "Yamama", unit="cavalry", off=(-0.6, 0.5)),
                  route(["Yamama", "Hira"], "Khalid, up the Euphrates", width=16),
                  battle("al-Hira", "Hira", "12 AH"),
                  area(PERSIA, "f3", "Sasanian Persia", 0.16),
              ]))

    # ---------------------------------------------------------------- the desert march
    S.append(("desert-march", "The march with no road",
              "13 AH — al-Hira to Tadmur", [34.0, 29.0, 46.0, 36.5], [
                  place("Hira", "below"), place("Quraqir", "below"), place("Suwa", "above"),
                  place("Tadmur", "above"), place("Damascus", "left"),
                  army("Khalid b. al-Walid", "Hira", unit="cavalry", off=(0.4, 0.6)),
                  route(["Hira", "Quraqir", "Suwa", "Tadmur"],
                        "no road: five nights", dashed=True, width=15),
                  note(39.5, 30.2, "He comes out behind them", 22),
              ]))

    # ---------------------------------------------------------------- Syria
    S.append(("syria-ajnadayn", "Four commanders, four roads",
              "13 AH — into Syria", [33.0, 28.0, 40.0, 35.5], [
                  place("Madina", "below"), place("Ajnadayn", "below"), place("Damascus", "right"),
                  place("al-Jabiya", "right"), place("Marj al-Suffar", "right"),
                  army("Abu Ubayda", "Damascus", off=(-1.4, 0.9)),
                  army("Amr b. al-As", "Ajnadayn", off=(-1.2, -0.5)),
                  army("Yazid b. Abi Sufyan", "al-Jabiya", off=(0.6, 0.6)),
                  route(["Madina", "Ajnadayn"], "the Syrian columns", width=14),
                  battle("Ajnadayn", "Ajnadayn", "13 AH"),
                  area(ROME, "f2", "Byzantine Rome", 0.16),
              ]))

    # ---------------------------------------------------------------- 13 AH extent
    S.append(("13ah-where-we-stand", "Where we stand now",
              "13 AH / 634 CE — at Abu Bakr's death", [28.0, 12.0, 62.0, 40.0], [
                  area(EXTENT_13, "f1", "", 0.26),
                  area(ARABIA_11, "f5", "11 AH", 0.0),
                  place("Madina", "left"), place("Makkah", "left"),
                  place("Hira", "above"), place("Ajnadayn", "left"),
                  note(45.0, 14.0, "The dashed outline is where the map stood at 11 AH", 20),
                  note(41.0, 37.5, "Two years and three months", 24),
              ]))

    # ---------------------------------------------------------------- the later set-pieces
    S.append(("yarmuk", "Yarmuk", "15 AH", [33.0, 29.0, 40.0, 36.0], [
        place("Yarmuk", "above"), place("Damascus", "right"), place("al-Jabiya", "below"),
        army("Khalid b. al-Walid", "Yarmuk", unit="cavalry", off=(-0.9, 0.5)),
        army("Byzantine army", "Yarmuk", faction="f2", off=(0.8, 0.5)),
        battle("Yarmuk", "Yarmuk", "15 AH"), area(ROME, "f2", "", 0.14),
    ]))
    S.append(("qadisiyya", "al-Qadisiyya", "15/16 AH", [41.0, 28.0, 49.0, 35.0], [
        place("Qadisiyya", "below"), place("Hira", "above"), place("Madain", "above"),
        army("Sad b. Abi Waqqas", "Qadisiyya", off=(-1.0, 0.5)),
        army("Rustam", "Qadisiyya", faction="f3", off=(0.9, 0.4)),
        battle("al-Qadisiyya", "Qadisiyya", "15/16 AH"), area(PERSIA, "f3", "", 0.14),
    ]))
    S.append(("madain-jalula", "al-Mada'in and Jalula", "16 AH", [42.0, 30.0, 49.0, 36.0], [
        place("Madain", "right"), place("Jalula", "above"), place("Kufa", "below"),
        route(["Qadisiyya", "Madain"], "across the Tigris", width=15),
        place("Qadisiyya", "below"), battle("Jalula", "Jalula", "16 AH"),
    ]))
    S.append(("bayt-al-maqdis", "Bayt al-Maqdis", "16/17 AH", [32.0, 28.0, 40.0, 35.0], [
        place("Jerusalem", "left"), place("al-Jabiya", "right"), place("Madina", "below"),
        army("Umar b. al-Khattab", "al-Jabiya", off=(0.8, 0.6)),
        route(["Madina", "al-Jabiya", "Jerusalem"], "the caliph comes himself", width=14),
    ]))
    S.append(("nahawand", "Nahawand", "21 AH", [42.0, 29.0, 54.0, 38.0], [
        place("Nihawand", "below"), place("Hamadan", "above"), place("Kufa", "left"),
        army("al-Numan b. Muqarrin", "Nihawand", off=(-1.1, 0.5)),
        army("Sasanian army", "Nihawand", faction="f3", off=(1.0, 0.4)),
        battle("Nahawand", "Nihawand", "21 AH"), area(PERSIA, "f3", "", 0.14),
    ]))
    S.append(("23ah-where-we-stand", "Where we stand now", "23 AH / 644 CE",
              [22.0, 10.0, 64.0, 42.0], [
                  area(EXTENT_23, "f1", "", 0.26), area(ARABIA_11, "f5", "11 AH", 0.0),
                  place("Madina", "below"), place("Damascus", "left"), place("Madain", "above"),
                  place("Fustat / Cairo", "left"), place("Nihawand", "right"),
                  note(43.0, 11.5, "The dashed outline is where the map stood at 11 AH", 20),
              ]))
    return S


def build():
    os.makedirs(OUT, exist_ok=True)
    made = []
    for slug, title, subtitle, bbox, objects in scenes():
        objects = [o for o in objects if o]
        steps = max([o.get("step", 1) for o in objects] + [1])
        scene = {
            "schema": 1,
            "meta": {"title": title, "subtitle": subtitle, "urduTitle": "",
                     "note": "Generated by tools/make_scenes.py from the Map: lines of "
                             "L02_baarah_saal/CONTENT.md. Territory outlines are SCHEMATIC, not "
                             "frontiers; sites placed approximately — several here are disputed. "
                             "Verify against the research note before this reaches a slide."},
            "view": fit(bbox),
            "factions": FACTIONS,
            "objects": objects,
            "underlay": None,
            "style": {"relief": True, "reliefStrength": 0.85, "rivers": True, "markScale": 1,
                      "cartoucheScale": 1, "graticule": False, "grain": True, "vignette": True,
                      "cartouche": True, "legend": True, "scalebar": True,
                      "urduLabels": False, "aspect": "16:9"},
            "steps": {"count": steps, "current": steps, "mode": "upto"},
        }
        p = os.path.join(OUT, slug + ".json")
        with open(p, "w", encoding="utf-8") as f:
            json.dump(scene, f, ensure_ascii=False, indent=2)
        made.append((slug, len(objects)))
    return made


if __name__ == "__main__":
    for slug, n in build():
        print("  %-34s %2d objects" % (slug + ".json", n))
    print("\n%d scenes in tools/mapstudio/scenes/" % len(build()))
    print("Open tools/mapstudio/index.html -> Open -> pick a scene -> Export PNG.")
