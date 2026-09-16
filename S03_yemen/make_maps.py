# -*- coding: utf-8 -*-
"""Evening 3 — Map Studio scenes for Yemen, one per map beat in RUNSHEET.md Parts I–III.

    python S03_yemen/make_maps.py        # -> tools/mapstudio/scenes/s03-*.json

Built on tools/make_scenes.py (its gazetteer, projection and object factories) but writes ONLY the
s03-* files, so the seventeen session-2 scenes — some of them nudged by hand in the tool — are never
regenerated over.

Every route, arrow and label below comes from the **Map:** line of the card it serves (the card ids
are in the comments). Where a card gives no place — Kahf Khubbān, Shaʿūb — none is invented: the scene
says "not located" in words instead of putting a dot on the map. Places the gazetteer lacks are added
as APPROXIMATE modern coordinates for placement only, exactly as make_scenes.py does; tribal names
(Madhḥij, Hamdān, ʿAkk) are free labels over roughly the right country, not territories.

Open tools/mapstudio/index.html -> Open -> pick a scene -> step through -> Export PNG.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "tools"))
import make_scenes as MS                                            # noqa: E402
from make_scenes import G, place, army, battle, route, area, note  # noqa: E402

# Approximate, placement only. Marked approx so every settlement carries "site approximate".
EXTRA = {
    "Marib": (45.325, 15.463, "town"), "al-Janad": (44.13, 13.68, "town"),
    "Abyan": (45.37, 13.12, "town"), "Khawlan (mountains)": (44.65, 15.25, "town"),
    "Hadramawt": (48.60, 15.90, "town"), "Akk": (43.30, 15.60, "town"),
    "Hamdan": (43.95, 16.15, "town"), "al-Ahsa": (49.588, 25.383, "city"),
}
for name, (lon, lat, tier) in EXTRA.items():
    G.setdefault(name, {"en": name, "ur": "", "lon": lon, "lat": lat, "tier": tier, "approx": True})


def path(pts, label="", faction="f1", dashed=False, width=14, step=1):
    """An arrow through raw lon/lat points, for a sea lane or a line that stops short of a place."""
    return {"id": MS._uid("r"), "type": "arrow", "pts": [list(p) for p in pts], "faction": faction,
            "label": label, "ur": "", "dashed": dashed, "width": width, "step": step}


def at(obj, dlon, dlat):
    """Nudge a placed object so its label clears a crowded city."""
    obj["lon"] += dlon
    obj["lat"] += dlat
    return obj


YEMEN = [[42.6, 17.8], [45.5, 18.2], [49.5, 17.0], [52.0, 16.5], [51.5, 15.0], [45.2, 12.6],
         [43.4, 12.7], [42.8, 14.5]]
WEST_YEMEN = [[42.6, 17.8], [45.5, 17.8], [46.2, 15.0], [45.4, 12.8], [43.4, 12.7], [42.8, 14.5]]
HADRAMAWT = [[47.0, 17.0], [51.5, 17.2], [52.0, 15.6], [49.5, 14.2], [47.2, 14.0]]
YEMEN_BOX = [41.5, 11.8, 52.5, 19.0]


def scenes():
    S = []

    # Bookend IN — the turn from Buzākha, where evening 2 stopped, to the south
    S.append(("s03-00-turn-south", "Tonight: the south", "from Buzākha to Ṣanʿāʾ", [36.5, 11.5, 52.5, 29.0], [
        place("Buzakha", "right"), place("Madina", "left"), place("Sana", "left"),
        area(YEMEN, "f4", "Yemen", 0.20),
    ]))

    # ATA/E-TB17 is a statement slide; AAA/E-AW01 and AW02 are the first map.
    S.append(("s03-01-the-persians-of-yemen", "The Persians of Yemen",
              "before the Prophet's ﷺ birth, and the letter to Kisrā", [36.5, 11.5, 60.0, 34.5], [
                  place("Sana", "left"), place("Aden", "below"), place("Madina", "left"),
                  place("Madain", "above"),
                  # AW01: "a single arrow from Persia down the Gulf to Ṣanʿāʾ" — schematic sea lane
                  path([[55.8, 27.0], [58.4, 23.0], [55.0, 16.8], [46.5, 12.6], [44.3, 15.2]],
                       "Wahriz and Kisrā's men", "f3", dashed=True),
                  note(44.2, 17.2, "al-Abnāʾ", 26),
                  # AW02: Medina -> Kisrā (letter torn), Kisrā -> Ṣanʿāʾ (the order), two men and back
                  route(["Madina", "Madain"], "the letter to Kisrā", "f1", dashed=True, step=2),
                  route(["Madain", "Sana"], "Kisrā's order to Bādhām", "f3", dashed=True, step=2),
                  route(["Sana", "Madina"], "two envoys, and back", "f3", step=3),
              ]))

    # AAA/E-AW03 — Yemen broken into governors' districts; Muʿādh ؓ loops through all of them
    S.append(("s03-02-yemen-in-10ah", "Yemen divided", "10 AH — the governors, and a teacher on the road",
              YEMEN_BOX, [
                  place("Sana", "left"), place("Najran", "right"), place("Marib", "right"),
                  place("al-Janad", "left"), place("Zabid", "left"), place("Aden", "below"),
                  note(44.2, 14.9, "Shahr b. Bādhām", 18), note(44.2, 17.0, "ʿAmr b. Ḥazm ؓ", 18),
                  note(46.1, 15.1, "Abū Mūsā ؓ", 18), note(44.6, 13.4, "Yaʿlā b. Umayya ؓ", 18),
                  note(42.6, 13.9, "Khālid b. Saʿīd ؓ", 18),
                  note(43.9, 16.4, "Hamdān", 20), note(43.0, 15.6, "ʿAkk", 20),
                  note(48.6, 16.3, "Ḥaḍramawt — Ziyād b. Labīd ؓ", 20),
                  route(["Sana", "Marib", "Hadramawt", "al-Janad", "Sana"], "Muʿādh ؓ, the teacher",
                        "f1", dashed=True, width=10, step=2),
              ]))

    # AAA/E-AW04, AW05 — the rising and the twenty-five nights (framed on Yemen)
    S.append(("s03-03-al-aswad-rises", "al-Aswad rises", "after Ḥajjat al-Wadāʿ, 10 AH — al-Aswad al-ʿAnsī",
              [41.0, 11.8, 53.0, 21.0], [
                  place("Najran", "left"), place("Sana", "left"), place("Aden", "below"),
                  note(45.9, 14.2, "Madhḥij", 22),
                  note(49.6, 19.9, "Kahf Khubbān: in Yemen, not located", 18),
                  army("al-Aswad, 700 men", "Najran", "f4", step=2, off=(0.9, 0.2)),
                  note(45.6, 17.1, "10 nights", 20, step=2),
                  route(["Najran", "Sana"], "25 nights from his rising", "f4", step=3),
                  at(battle("Shaʿūb, outside Ṣanʿāʾ", "Sana", "Shahr b. Bādhām killed", step=3), 0.0, 0.35),
                  area(YEMEN, "f4", "", 0.20, step=4),
                  note(48.8, 18.9, "his hand reached from Ḥaḍramawt to al-Ṭāʾif, al-Aḥsāʾ and Aden",
                       16, step=4),
              ]))

    # AAA/E-AW06 — the governors scatter (framed wide, to Medina)
    S.append(("s03-03b-the-governors-scatter", "The governors scatter", "after Ṣanʿāʾ fell",
              [37.5, 11.8, 52.5, 25.8], [
                  area(YEMEN, "f4", "", 0.16),
                  place("Madina", "left"), place("Sana", "left"), place("Marib", "right"),
                  place("Najran", "right"), place("Zabid", "left"), place("Akk", "left"),
                  place("Taif", "left"), place("al-Ahsa", "right"),
                  route(["Sana", "Marib", "Hadramawt"], "Muʿādh ؓ and Abū Mūsā ؓ", "f1", step=2),
                  route(["Najran", "Madina"], "ʿAmr b. Ḥazm ؓ", "f1", dashed=True, step=2),
                  route(["Zabid", "Madina"], "Khālid b. Saʿīd ؓ", "f1", dashed=True, step=2),
                  route(["Sana", "Akk"], "", "f1", width=10, step=2),
                  note(41.6, 15.3, "the rest, to al-Ṭāhir in ʿAkk", 18, step=2),
              ]))

    # AAA/E-AW08 (the letters), AW14 (the dawn), ATA/E-TB26 + ABU/E-U9 (the news)
    S.append(("s03-04-the-night-in-sana", "The night in Ṣanʿāʾ", "the Prophet's ﷺ last months, to Rabīʿ I 11 AH",
              [38.5, 12.5, 48.5, 25.5], [
                  place("Madina", "left"), place("Sana", "left"), place("Najran", "right"),
                  route(["Madina", "Sana"], "Wabr b. Yuḥannas, with the letters", "f1"),
                  route(["Sana", "Hamdan"], "", "f5", dashed=True, width=8, step=2),
                  route(["Sana", "Najran"], "", "f5", dashed=True, width=8, step=2),
                  battle("al-Aswad killed", "Sana", "Rabīʿ I 11 AH", step=3),
                  note(45.8, 14.6, "the adhān at dawn", 20, step=3),
                  path([[44.21, 15.6], [44.22, 16.4]], "his horsemen, not yet gone", "f4",
                       dashed=True, width=10, step=4),
                  route(["Sana", "Madina"], "the news reaches Medina", "f5",
                        dashed=True, step=5),
              ]))

    # TSY/E-YK01, RCT/E-RC31, TSY/E-YK02, TSY/E-YK03 — Qays turns on the Abnāʾ
    S.append(("s03-05-qays-and-the-abna", "Go back to your own land", "11 AH — Qays b. Makshūḥ and the Abnāʾ",
              [42.0, 12.0, 47.5, 17.8], [
                  place("Sana", "left"), place("Aden", "below"), place("Najran", "right"),
                  army("Fayrūz ؓ", "Sana", "f1", off=(-0.75, 0.0)),
                  army("Qays b. Makshūḥ", "Sana", "f4", off=(0.1, -0.6)),
                  note(46.0, 17.2, "letters from Abū Bakr ؓ — and from Qays", 18),
                  note(42.9, 14.8, "Dādhawayh killed at a meal", 18, step=2),
                  place("Khawlan (mountains)", "right", step=2),
                  route(["Sana", "Khawlan (mountains)"], "Fayrūz ؓ and Jishnas", "f1", step=2),
                  route(["Sana", "Aden"], "families, to the ships", "f5", dashed=True, step=3),
                  path([[44.21, 15.40], [44.00, 16.70]], "families, overland", "f5", dashed=True, step=3),
                  # TSY/E-YK17: Banū ʿUqayl and ʿAkk turned the convoys back, but NO page says which tribe
                  # met which convoy, so neither is placed on a route (corrected 2026-09-16)
                  note(45.9, 13.6, "Banū ʿUqayl and ʿAkk turn both convoys back", 18, step=3),
                  at(battle("the clash short of Ṣanʿāʾ", "Sana", "", step=4), 0.35, 0.45),
                  army("Qays", "Najran", "f4", step=4, off=(0.6, -1.0)),
              ]))

    # TSY/E-YK05, TSY/E-YK06, RCT/E-RC32 — the two armies, and the two men sent north as prisoners
    S.append(("s03-06-the-two-armies", "Two armies come down on the Yemen", "11–12 AH",
              [38.0, 12.0, 53.5, 25.5], [
                  place("Makkah", "left"), place("Taif", "left"), place("Najran", "right"),
                  place("Sana", "left"), place("Abyan", "below"), place("Mahra", "above"),
                  place("Madina", "left"),
                  path([[52.0, 16.5], [49.0, 14.4], [46.8, 13.5], [45.37, 13.12]],
                       "ʿIkrima ؓ, along the coast", "f1"),
                  route(["Makkah", "Taif", "Najran"], "al-Muhājir ؓ", "f1"),
                  route(["Najran", "Madina"], "prisoners, sent north", "f4", dashed=True, step=2),
                  route(["Najran", "Sana"], "al-Muhājir ؓ", "f1", step=3),
              ]))

    # Part III — TSY/E-YK07, RCT/E-RC33, TSY/E-YK08, YK09, YK10 (the quarrel and the four kings), then
    # TSY/E-YK11, YK12, RCT/E-RC34 (the march, the battle, al-Nujayr). Maḥjar al-Zurqān and al-Nujayr are
    # NOT located in our sources: they are named in words, never placed as dots.
    S.append(("s03-07-hadramawt-and-kinda", "Ḥaḍramawt and Kinda", "11–12 AH — the zakāt, the four kings, al-Nujayr",
              [41.5, 11.8, 53.5, 19.5], [
                  place("Sana", "left"), place("Najran", "right"), place("Abyan", "below"),
                  note(49.4, 15.2, "Ḥaḍramawt", 24), note(47.4, 16.7, "Kinda", 24),
                  path([[48.9, 15.5], [47.8, 16.4]], "the zakāt camels", "f5", width=10),
                  area(HADRAMAWT, "f4", "", 0.22, step=2),
                  note(50.4, 17.8, "one she-camel: Shadhra", 18, step=2),
                  army("Ziyād b. Labīd ؓ · Ḥaḍramawt · al-Sakūn", "Hadramawt", "f1", step=3, off=(0.9, -0.7)),
                  army("Banū Muʿāwiya of Kinda", "Hadramawt", "f4", step=3, off=(-1.2, 0.8)),
                  battle("the four kings killed", "Hadramawt", "round their fires", step=4),
                  army("al-Ashʿath", "Hadramawt", "f4", step=4, off=(-0.3, 1.3)),
                  route(["Sana", "Hadramawt"], "al-Muhājir ؓ, ahead with the fastest men", "f1", width=8, step=5),
                  # YK11: al-Muhājir ؓ left ʿIkrima ؓ over his army on the road — the same road, a little
                  # behind; drawn just south of step 5 so the two labels clear each other
                  path([[44.4, 15.05], [46.4, 15.2], [48.2, 15.55]], "the main body, under ʿIkrima ؓ", "f1",
                       dashed=True, step=6),
                  note(49.0, 13.4, "Maḥjar al-Zurqān, then the fort of al-Nujayr — neither located", 16, step=6),
              ]))

    # TSY/E-YK14, POT/E-PG40 — al-Ashʿath taken to Medina, pardoned
    S.append(("s03-08-al-ashath-to-medina", "To Medina", "11–12 AH — al-Ashʿath before Abū Bakr ؓ",
              [37.5, 11.8, 53.5, 26.0], [
                  place("Madina", "left"), place("Sana", "left"),
                  note(49.4, 15.2, "Ḥaḍramawt", 22),
                  path([[48.6, 15.9], [45.0, 20.0], [39.9, 24.3]], "al-Ashʿath, bound, to Medina", "f4",
                       dashed=True),
              ]))

    # Closing pair, STOP C — the south one colour; al-Yamāma, where the story goes next
    S.append(("s03-close-stop-c", "Where we stand", "11–12 AH — the south restored; next, back to al-Yamāma",
              [37.5, 11.8, 56.0, 27.5], [
                  area(YEMEN, "f1", "the Yemen and Ḥaḍramawt", 0.22),
                  place("Sana", "left"), place("Madina", "left"), place("Yamama", "right"),
                  army("Musaylima", "Yamama", "f4", off=(0.5, 0.4)),
              ]))

    # Closing pair, STOP A — AAA/E-AW16: Ṣanʿāʾ blue, and a single red point appearing inside it
    S.append(("s03-close-stop-a", "Where we stand", "Rabīʿ I 11 AH — the news of the death reaches Ṣanʿāʾ",
              YEMEN_BOX, [
                  place("Sana", "left"), place("Najran", "right"), place("Aden", "below"),
                  army("Fayrūz ؓ · Muʿādh ؓ", "Sana", "f1", off=(-0.4, 0.3)),
                  army("Qays b. Makshūḥ", "Sana", "f4", off=(0.4, -0.3), step=2),
              ]))

    # Closing pair, STOP B — Ṣanʿāʾ blue, Ḥaḍramawt still grey
    S.append(("s03-close-stop-b", "Where we stand", "11–12 AH — Ṣanʿāʾ restored; Ḥaḍramawt still to come",
              [41.5, 11.8, 53.5, 19.5], [
                  area(WEST_YEMEN, "f1", "Ṣanʿāʾ and the highlands", 0.22),
                  area(HADRAMAWT, "f5", "Ḥaḍramawt", 0.30),
                  place("Sana", "left"), place("Najran", "right"), place("Aden", "below"),
              ]))
    return S


def build():
    os.makedirs(MS.OUT, exist_ok=True)
    made = []
    for slug, title, subtitle, bbox, objects in scenes():
        objects = [o for o in objects if o]
        steps = max([o.get("step", 1) for o in objects] + [1])
        scene = {
            "schema": 1,
            "meta": {"title": title, "subtitle": subtitle, "urduTitle": "",
                     "note": "Generated by S03_yemen/make_maps.py from the Map: lines of the evening-3 "
                             "cards. Sites placed approximately; tribal names are loose labels, not "
                             "territories; Kahf Khubbān and Shaʿūb are not located in our sources. "
                             "Verify against the research note before this reaches a slide."},
            "view": MS.fit(bbox),
            "factions": MS.FACTIONS,
            "objects": objects,
            "underlay": None,
            "style": {"relief": True, "reliefStrength": 0.85, "rivers": True, "markScale": 1,
                      "cartoucheScale": 1, "graticule": False, "grain": True, "vignette": True,
                      "cartouche": True, "legend": True, "scalebar": True,
                      "urduLabels": False, "aspect": "16:9"},
            "steps": {"count": steps, "current": steps, "mode": "upto"},
        }
        p = os.path.join(MS.OUT, slug + ".json")
        with open(p, "w", encoding="utf-8") as f:
            json.dump(scene, f, ensure_ascii=False, indent=2)
        made.append((slug, len(objects), steps))
    return made


if __name__ == "__main__":
    for slug, n, steps in build():
        print("  %-32s %2d objects  %d step(s)" % (slug + ".json", n, steps))
