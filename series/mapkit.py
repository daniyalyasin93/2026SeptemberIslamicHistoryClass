# -*- coding: utf-8 -*-
"""Map scenes written as the story is told (docs/VISION.md §5-§6).

WHY THIS EXISTS. Evening 6's first Bahrayn map was authored by placing objects by hand, and Daniyal's review
of it (2026-10-08) was a list of things a helper would have made impossible:

    "the text is tooooo small"                      the captions had no `size`; the painter fell back to 10px
    "al dahna journey becomes hidden behind         the title box was on, bottom-left, over the march
     the cartouche"
    "al jarud is still stuck at the bottom as       a token was placed once and never moved
     if he is in the same place all this time"
    "the arrow here what does it mean? who went     an arrow from an earlier step, left on, with no owner
     to al khatt here?"
    "the enemy army should also have an icon"       only one side had been given a token
    "there should be some animation to describe     a siege had been drawn as a battle mark
     a siege"

Every one of those is a rule, and here each rule is a property of the helper rather than of the author's
attention. A march() cannot leave a token behind, because the same call retires the old one. A say() cannot
be small, because it has no way to be given no size. Nothing can sit under the title box, because there is
no title box — the slide's own headline is the title.

    s = Scene("s06-bahrayn-hajar", "Hajar", box=(48.9, 50.6, 24.9, 26.1))
    s.place("Hajar", 49.588, 25.383, tier="city")
    s.force("al-Ḥuṭam", "f4", 49.62, 25.42, sub="Bakr b. Wāʾil")
    s.at(2, "al-ʿAlāʾ ؓ comes in from the west")
    s.march("al-ʿAlāʾ ؓ", "f1", frm=(48.95, 25.30), to=(49.40, 25.36))
    s.at(3, "Both sides dig in")
    s.trench((49.47, 25.50), (49.47, 25.25))
    s.save(); s.check()

THE ENGINE'S LIMITS, which the helpers work inside (tools/mapstudio, series/anim.py):
  * six object types only — settlement, army, battle, arrow, label, territory. No line, ring or icon.
  * the first step of a slide's range is its ground and is NOT animated: ranges overlap by one step.
  * a token travels only along an arrow that enters on the same click, and only once.
  * everything on one click runs together; there is no delay and no sequence inside a click.
  * the coastline is 1:50m — small islands are absent and must be drawn (see island()).
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SCENES = os.path.join(ROOT, "tools", "mapstudio", "scenes")

K = math.cos(math.radians(30.0))            # the painter's projection: equirectangular, standard parallel 30N
STAGE_W, STAGE_H = 1600.0, 900.0
PT_PER_PX = 0.381                           # one stage pixel on a slide whose map takes 70% of the width
KM = 111.32                                 # one degree of latitude on the ground
CH = 0.56                                   # a letter's width in ems, in the painter's serif (measured off renders)
SIDES = ("right", "left", "above", "below")
BEARINGS = {"E": 0, "NE": 45, "N": 90, "NW": 135, "W": 180, "SW": -135, "S": -90, "SE": -45}
SCALEBAR = (STAGE_W - 270, STAGE_H - 86, STAGE_W - 16, STAGE_H - 20)

GREEN = "#2CB020"                           # DECISIONS #58 — one green for Muslim forces, on every map
FACTIONS = [
    {"id": "f1", "name": "Muslim forces", "ur": "", "color": GREEN},
    {"id": "f4", "name": "In revolt", "ur": "", "color": "#E7A244"},
    {"id": "f5", "name": "Not yet told", "ur": "", "color": "#9AA39E"},
    {"id": "f6", "name": "Under a covenant", "ur": "", "color": "#5B8FD6"},
]

MARK = 2.0             # style.markScale, as on every evening-4 and evening-5 scene
NAME = 1.5             # object scale for a settlement, a force, a battle: 14.5-15 px x 2 x 1.5 = ~17pt on the slide
SAY = 26               # a caption's size: x 2 = 52 px = ~20pt on the slide
MIN_NAME_PT, MIN_SAY_PT = 15.0, 18.0

STYLE = {"relief": True, "reliefStrength": 0.85, "rivers": True, "markScale": MARK, "cartoucheScale": 2.0,
         "graticule": False, "grain": True, "vignette": True,
         "cartouche": False,       # the slide's headline is the title; a box in the map only hides the map
         "legend": False,          # the slide's key panel says who is who
         "scalebar": True, "urduLabels": False, "aspect": "16:9"}


def frame(lon_min, lon_max, lat_min, lat_max, margin=0.06):
    """The view that fits a lon/lat box into the stage. view.cx is lon x cos(30), NOT longitude."""
    x0, x1, y0, y1 = lon_min * K, lon_max * K, -lat_max, -lat_min
    scale = min(STAGE_W / max(1e-6, x1 - x0), STAGE_H / max(1e-6, y1 - y0)) * (1.0 - 2.0 * margin)
    return {"cx": (x0 + x1) / 2.0, "cy": (y0 + y1) / 2.0, "scale": scale}


def visible_box(view):
    hw, hh = STAGE_W / 2 / view["scale"], STAGE_H / 2 / view["scale"]
    return ((view["cx"] - hw) / K, (view["cx"] + hw) / K, -(view["cy"] + hh), -(view["cy"] - hh))


class SceneError(Exception):
    pass


class Scene(object):
    def __init__(self, slug, title, box, subtitle="", relief=None, margin=0.06):
        self.slug, self.title, self.subtitle = slug, title, subtitle
        self.view = frame(*box, margin=margin)
        self.style = dict(STYLE)
        if relief is not None:
            self.style["reliefStrength"] = relief
        self.objs, self.step, self.n = [], 1, 0
        self.cues = {1: "the ground"}
        self.tokens = {}            # force name -> the army object now standing for it
        self.regions = {}           # key -> (pts, the territory object now showing)
        self.places = {}            # place name -> (lon, lat)
        self.kind, self.parent, self.centre, self.radius_km = "theatre", None, None, None
        self._done = False

    # ------------------------------------------------------------------ plumbing
    def _add(self, kind, role, **kw):
        self.n += 1
        o = {"id": "%s_%03d" % (kind[0], self.n), "type": kind, "step": self.step, "note": role}
        o.update(kw)
        self.objs.append(o)
        return o

    def at(self, step, cue):
        """Move to a step. The cue is what the speaker says as the click lands; it becomes ▶ CLICK n."""
        if step < self.step:
            raise SceneError("%s: steps run forward (%d after %d)" % (self.slug, step, self.step))
        self.step = step
        self.cues[step] = cue
        return self

    # ------------------------------------------------------------------ the ground
    def place(self, name, lon, lat, tier="town", pos="right", scale=NAME):
        self.places[name] = (lon, lat)
        return self._add("settlement", "place", lon=lon, lat=lat, name=name, ur="", tier=tier,
                         labelPos=pos, scale=scale)

    def bring(self, *names, **kw):
        """Places from the parent map, at the parent's own coordinates — two scales cannot then disagree."""
        lo0, lo1, la0, la1 = visible_box(self.view)
        for name in names:
            lon, lat = self.parent.places[name]
            if not (lo0 < lon < lo1 and la0 < lat < la1):
                raise SceneError("%s: %r is outside this frame — widen the close-up, or signpost() it"
                                 % (self.slug, name))
            self.place(name, lon, lat, **kw)

    # ------------------------------------------------------------------ where things are
    def where(self, what):
        """The coordinates of a place, or of a force now on the field, by name."""
        if not isinstance(what, str):
            return tuple(what)
        if what in self.tokens:
            return self.tokens[what]["lon"], self.tokens[what]["lat"]
        for s in (self, self.parent):
            if s is not None and what in s.places:
                return s.places[what]
        raise SceneError("%s: nothing called %r is on this map" % (self.slug, what))

    def near(self, what, bearing, km=None, px=None):
        """A point beside something — `km` on the ground, or `px` on the stage where the map is a diagram.

        This is how a camp is set down: s.force("al-ʿAlāʾ ؓ", "f1", *s.near("Hajar", "E", px=150)). A banner is
        about 110 px across on the stage, so two camps want 130 px between them, and a name wants more."""
        lon, lat = self.where(what)
        a = math.radians(BEARINGS[bearing] if isinstance(bearing, str) else bearing)
        deg = px / self.view["scale"] if px is not None else km / KM
        return lon + deg * math.cos(a) / K, lat + deg * math.sin(a)

    def spot(self, x, y):
        """The point under a stage pixel (0-1600 across, 0-900 down). For laying a diagram out."""
        return _ll(self.view, x, y)

    def signpost(self, name, lon=None, lat=None):
        """Something off the frame, named on the edge it lies beyond: "← Medina". A close-up says where it is."""
        if lon is None:
            lon, lat = self.where(name)
        cx, cy = STAGE_W / 2, STAGE_H / 2
        x, y = _px(self.view, lon, lat)
        dx, dy = x - cx, y - cy
        fx = (cx - 40) / abs(dx) if dx else 9e9
        fy = (cy - 60) / abs(dy) if dy else 9e9
        if min(fx, fy) >= 1:
            raise SceneError("%s: %r is inside the frame — place() it, do not signpost it" % (self.slug, name))
        f = min(fx, fy)
        if fx <= fy:                                               # it lies beyond a side
            text, align = ("%s →" % name, "right") if dx > 0 else ("← %s" % name, "left")
        else:
            text, align = ("↑ %s" % name, "center") if dy < 0 else ("↓ %s" % name, "center")
        plon, plat = _ll(self.view, cx + dx * f, cy + dy * f)
        return self._add("label", "signpost", lon=plon, lat=plat, text=text, ur="", size=24, align=align)

    def region(self, key, pts, faction, opacity=0.26, label=""):
        o = self._add("territory", "region:" + key, pts=[list(p) for p in pts], faction=faction,
                      label=label, ur="", opacity=opacity)
        self.regions[key] = (pts, o)
        return o

    def turn(self, key, faction, opacity=0.26):
        """A region changes hands: the old colour fades as the new one comes up, on the same click."""
        pts, old = self.regions[key]
        old["until"] = self.step - 1
        return self.region(key, pts, faction, opacity=opacity)

    def island(self, pts, name, lon, lat, pos="right"):
        """Land the 1:50m coastline does not carry (Tārūt, where Dārīn stands). Drawn, and said to be."""
        self._add("territory", "island", pts=[list(p) for p in pts], faction="f5", label="", ur="",
                  opacity=0.55)
        return self.place(name, lon, lat, pos=pos)

    # ------------------------------------------------------------------ forces
    def force(self, name, faction, lon, lat, sub="", unit="mixed", pos="right", scale=NAME):
        """A force is on the field from this step. Every side that is there gets one — the enemy too."""
        if name in self.tokens:
            raise SceneError("%s: %r is already on the field — march() it, do not place it twice"
                             % (self.slug, name))
        o = self._add("army", "force", lon=lon, lat=lat, name=name, ur="", faction=faction,
                      strength=sub, unit=unit, labelPos=pos, scale=scale)
        self.tokens[name] = o
        return o

    def march(self, name, faction=None, to=None, frm=None, via=(), sub=None, unit=None, pos=None,
              dashed=False, width=9.0, keep_road=True):
        """A force moves, on this click. Its token travels the arrow; the token it left is retired.

        A force not yet on the field may be marched in from `frm` (it comes on already moving)."""
        old = self.tokens.get(name)
        if old is None and frm is None:
            raise SceneError("%s: %r is not on the field — give frm=, or force() it first" % (self.slug, name))
        start = list(frm) if frm else [old["lon"], old["lat"]]
        mid = [list(p) for p in via] or [[(start[0] + to[0]) / 2.0, (start[1] + to[1]) / 2.0]]
        fac = faction or old["faction"]
        arrow = self._add("arrow", "march:" + name, pts=[start] + mid + [list(to)], faction=fac, label="",
                          ur="", dashed=dashed, width=width)
        if not keep_road:
            arrow["until"] = self.step
        if old is not None:
            old["until"] = self.step - 1
        tok = self._add("army", "force", lon=to[0], lat=to[1], name=name, ur="", faction=fac,
                        strength=(old or {}).get("strength", "") if sub is None else sub,
                        unit=unit or (old or {}).get("unit", "mixed"),
                        labelPos=pos or (old or {}).get("labelPos", "right"),
                        scale=(old or {}).get("scale", NAME), follows=arrow["id"])
        self.tokens[name] = tok
        return tok

    def sail(self, name, to, via, **kw):
        """A crossing by water: a dashed route, and the token becomes a ship while it is on it."""
        return self.march(name, to=to, via=via, dashed=True, unit="naval", **kw)

    def leave(self, name):
        """The force is gone from the field after the step before this one — beaten, scattered, or dead."""
        self.tokens.pop(name)["until"] = self.step - 1
        for o in self.objs:                       # and its road goes with it: an arrow nobody is on is a question
            if o["type"] == "arrow" and o.get("note") == "march:" + name and "until" not in o:
                o["until"] = self.step - 1

    # ------------------------------------------------------------------ what happens
    def siege(self, lon, lat, faction, r=0.10, arms=5, turn=0.5):
        """A siege is drawn as a siege: a ring round the place and columns closing on it from every side.
        `r` is in degrees of latitude; `turn` rotates the columns, to keep them off a neighbour."""
        ring = [[lon + r / K * math.cos(a), lat + r * math.sin(a)]
                for a in [2 * math.pi * i / 28 for i in range(28)]]
        made = [self._add("territory", "siege", pts=ring, faction=faction, label="", ur="", opacity=0.10)]
        for i in range(arms):
            a = 2 * math.pi * i / arms + turn
            out = [lon + 2.4 * r / K * math.cos(a), lat + 2.4 * r * math.sin(a)]
            mid = [lon + 1.7 * r / K * math.cos(a), lat + 1.7 * r * math.sin(a)]
            near = [lon + 1.15 * r / K * math.cos(a), lat + 1.15 * r * math.sin(a)]
            made.append(self._add("arrow", "siege", pts=[out, mid, near], faction=faction, label="", ur="",
                                  dashed=False, width=6.0))
        return made

    def lift(self, made):
        """The siege ends on this click."""
        for o in made:
            o["until"] = self.step - 1

    def trench(self, a, b, faction="f5", wide=0.012):
        """Dug-in lines between two camps. The engine has no line, so a trench is a thin bar of ground."""
        dx, dy = (b[0] - a[0]) * K, b[1] - a[1]
        ln = math.hypot(dx, dy) or 1.0
        ox, oy = -dy / ln * wide / K, dx / ln * wide
        pts = [[a[0] + ox, a[1] + oy], [b[0] + ox, b[1] + oy], [b[0] - ox, b[1] - oy], [a[0] - ox, a[1] - oy]]
        return self._add("territory", "trench", pts=pts, faction=faction, label="", ur="", opacity=0.75)

    def letter(self, a, b, faction="f1"):
        """A letter, a request, an order: a thin dashed line that is gone on the next click."""
        mid = [(a[0] + b[0]) / 2.0, (a[1] + b[1]) / 2.0 + 0.04 * abs(a[0] - b[0])]
        return self._add("arrow", "letter", pts=[list(a), mid, list(b)], faction=faction, label="", ur="",
                         dashed=True, width=5.0, until=self.step)

    def clash(self, lon, lat, name="", pos="below"):
        o = self._add("battle", "clash", lon=lon, lat=lat, name=name, ur="", date="", labelPos=pos, scale=NAME)
        o["until"] = self.step
        return o

    def say(self, text, lon=None, lat=None, hold=False, size=SAY, align="center", near=None):
        """A caption for this click. It fades on the next one unless held, so captions never pile up.

        Give it no position and it finds its own: the free spot nearest `near` (a place, a force, or a point;
        by default, whatever comes on with this click) where it covers no name, no mark and no arrow."""
        o = self._add("label", "say", lon=lon, lat=lat, text=text, ur="", size=size, align=align)
        if lon is None:
            o["align"], o["auto"] = "center", (list(self.where(near)) if near is not None else None)
        if not hold:
            o["until"] = self.step
        return o

    def name(self, text, lon, lat, size=24, align="center"):
        """A standing name on the ground — a region, a sea, a desert. It stays."""
        return self._add("label", "name", lon=lon, lat=lat, text=text, ur="", size=size, align=align)

    # ------------------------------------------------------------------ out
    def finish(self):
        """Names take the side where they cover nothing; captions with no position find one. Once."""
        if not self._done:
            self._done = True
            d = self.data()
            settle(d)
            place_captions(d, self.slug)
            settle(d)
        return self

    def data(self):
        return {"schema": 1,
                "meta": {"title": self.title, "subtitle": self.subtitle, "urduTitle": "", "kind": self.kind,
                         "parent": self.parent.slug if self.parent is not None else None,
                         "centre": list(self.centre) if self.centre else None, "radius_km": self.radius_km,
                         "note": "Written by series/mapkit.py. Edit the script that made it, not this file: "
                                 "regenerating overwrites a hand nudge."},
                "view": dict(self.view), "style": dict(self.style), "factions": [dict(f) for f in FACTIONS],
                "underlay": None, "objects": self.objs,
                "steps": {"count": self.step, "current": self.step, "mode": "upto"}}

    def save(self, draft=False):
        """Write the scene. A scene that breaks a map rule is not written — unless draft=True, which writes it
        and prints the breaches, so that it can be rendered and looked at while it is being laid out."""
        problems = self.check()
        if problems and not draft:
            raise SceneError("%s breaks the map rules:\n   %s" % (self.slug, "\n   ".join(problems)))
        for p in problems:
            print("   !!", p)
        path = os.path.join(SCENES, self.slug + ".json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.data(), f, ensure_ascii=False, indent=1)
        return path

    def clicks(self, a, b):
        """The ▶ CLICK lines of the slide showing steps a..b — one for every step after its ground."""
        return [self.cues[k] for k in range(a + 1, b + 1) if k in self.cues]

    def check(self):
        self.finish()
        bad = check_scene(self.data(), self.slug) + check_crowding(self.data(), self.slug)
        if self.parent is not None and self.kind == "closeup":
            bad += check_places({self.parent.slug: self.parent.data(), self.slug: self.data()})
        return bad


def closeup(slug, title, centre, radius_km, parent=None, diagram=False, relief=0.35, margin=0.06):
    """The second scale (VISION M2): everything within `radius_km` of `centre` is in the frame.

        hajar = closeup("s06-bahrayn-hajar", "Hajar", "Hajar", 40, parent=theatre)
        hajar.bring("Hajar")                       # from the parent, at the parent's coordinates
        hajar.signpost("Medina")                   # "← Medina" on the edge it lies beyond

    `centre` is a place on the parent, or (lon, lat). A close-up is a map: its places are where the parent
    has them, and it keeps its scale bar.

    diagram=True is for what the pages give only as SIDES — who lay next to whom, with no distance and no
    bearing (the trench month at Hajar). It carries no scale bar, it says "not to scale" on its face, and its
    marks are laid out with spot() and near(px=) rather than by coordinates. It claims an order, not a place."""
    lon, lat = parent.where(centre) if (parent is not None and isinstance(centre, str)) else centre
    dlat = radius_km / KM
    dlon = dlat * (STAGE_W / STAGE_H) / K
    s = Scene(slug, title, box=(lon - dlon, lon + dlon, lat - dlat, lat + dlat), relief=relief, margin=margin)
    s.kind, s.parent, s.centre, s.radius_km = ("diagram" if diagram else "closeup"), parent, (lon, lat), radius_km
    if diagram:
        s.style["scalebar"] = False
        tl = s.spot(STAGE_W - 370, STAGE_H - 44)
        s._add("label", "legend", lon=tl[0], lat=tl[1], text="a diagram — not to scale", ur="", size=24,
               align="center")
    return s


# ---------------------------------------------------------------------------------------- the rules
def _span(o, last):
    return o.get("step", 1), o.get("until", last)


def check_scene(d, slug=""):
    """The map rules of docs/VISION.md, on any scene — kit-made or hand-made. Returns the breaches."""
    bad, objs = [], d.get("objects", [])
    style, view = d.get("style", {}), d.get("view", {})
    last = max([d.get("steps", {}).get("count", 1)] + [o.get("step", 1) for o in objs])
    mark = style.get("markScale", 1.0)

    if style.get("cartouche"):
        bad.append("M9 the in-map title box is on — it covers the action; the slide's headline is the title")
    if style.get("legend"):
        bad.append("M9 the in-map legend is on — the slide's key panel says who is who")

    # M2 — two scales. A trench is a close-up's business and never a theatre map's. (A siege ring MAY stand on
    # a wider map, to say where — but then the deck owes the place a close-up: tools/check_vision.py, M2.)
    tall = STAGE_H / view["scale"] * KM if view.get("scale") else 0
    if tall > 330 and d.get("meta", {}).get("kind") not in ("closeup", "diagram"):
        if any(str(o.get("note", "")) == "trench" for o in objs):
            bad.append("M2 a trench is drawn on a map %d km from top to bottom — at that scale it is a scratch; "
                       "give it a close-up (mapkit.closeup)" % tall)

    lo0, lo1, la0, la1 = visible_box(view) if view.get("scale") else (-999, 999, -999, 999)
    for o in objs:
        t = o["type"]
        who = o.get("name") or o.get("text") or o["id"]
        if t == "label":
            if not o.get("size"):
                bad.append("M8 caption %r has no size — the painter falls back to 10px" % who)
            elif o["size"] * mark * o.get("scale", 1) * PT_PER_PX < MIN_SAY_PT:
                bad.append("M8 caption %r is %.0fpt on the slide; the floor is %.0fpt"
                           % (who, o["size"] * mark * o.get("scale", 1) * PT_PER_PX, MIN_SAY_PT))
        if t in ("settlement", "army", "battle") and (o.get("name") or t == "army"):
            pt = 14.5 * mark * o.get("scale", 1) * PT_PER_PX
            if pt < MIN_NAME_PT:
                bad.append("M8 %s %r is %.0fpt on the slide; the floor is %.0fpt" % (t, who, pt, MIN_NAME_PT))
        if t == "arrow" and (o.get("label") or "").strip():
            pt = 14 * mark * o.get("scale", 1) * PT_PER_PX
            if pt < MIN_NAME_PT:
                bad.append("M8 the words %r on an arrow are %.0fpt on the slide; the floor is %.0fpt"
                           % (o["label"], pt, MIN_NAME_PT))
        if o.get("lon") is not None and not (lo0 <= o["lon"] <= lo1 and la0 <= o["lat"] <= la1):
            bad.append("M10 %s %r is off the stage (%.2f, %.2f)" % (t, who, o["lon"], o["lat"]))

    # M5 — every arrow says who is moving
    # An arrow is owned if a banner travels it, if it carries words, if it is part of a siege or is a message
    # — or if it is one prong of a named force's move ("prong:Ziyād b. Labīd ؓ") and that force is on the map.
    followed = {o.get("follows") for o in objs if o["type"] == "army" and o.get("follows")}
    for o in objs:
        if o["type"] == "arrow" and o["id"] not in followed and not (o.get("label") or "").strip():
            note = str(o.get("note", ""))
            if note.startswith("prong:"):
                who, at = note[6:], o.get("step", 1)
                if not any(a["type"] == "army" and a.get("name") == who and a.get("step", 1) <= at <= a.get("until", last)
                           for a in objs):
                    bad.append("M5 arrow %s (step %s) is a prong of %r, who is not on the map at that step"
                               % (o["id"], at, who))
            elif note.startswith("said"):                 # a flow, not a force: the caption of its click says what
                if not any(c["type"] == "label" and c.get("step", 1) == o.get("step", 1) for c in objs):
                    bad.append("M5 arrow %s (step %s) leans on a caption, and no caption comes on with it"
                               % (o["id"], o.get("step")))
            elif not note.startswith(("siege", "letter")):
                bad.append("M5 arrow %s (step %s) has no owner: no force travels it and it carries no label"
                           % (o["id"], o.get("step")))

    # M4 — a force is in one place at a time
    by_name = {}
    for o in objs:
        if o["type"] == "army" and o.get("name"):
            by_name.setdefault(o["name"], []).append(o)
    for name, toks in by_name.items():
        toks.sort(key=lambda o: o.get("step", 1))
        for a, b in zip(toks, toks[1:]):
            if _span(a, last)[1] >= b.get("step", 1):
                bad.append("M4 %r stands in two places at step %d — its old token was never retired"
                           % (name, b.get("step", 1)))

    # M3 — a token that should travel, but cannot
    by_id = {o["id"]: o for o in objs}
    for o in objs:
        if o["type"] == "army" and o.get("follows"):
            arrow = by_id.get(o["follows"])
            if arrow is None:
                bad.append("M3 %r follows an arrow that does not exist" % o.get("name"))
            elif arrow.get("step") != o.get("step"):
                bad.append("M3 %r will not travel: its arrow enters on step %s, the token on step %s"
                           % (o.get("name"), arrow.get("step"), o.get("step")))
            elif len(arrow.get("pts", [])) < 3:
                bad.append("M3 %r travels a 2-point arrow — the token cuts the chord; give the route 3 points"
                           % o.get("name"))
    return ["%s: %s" % (slug, b) if slug else b for b in bad]


def check_ranges(d, ranges, slug=""):
    """A slide's first step is its ground and does not move, so a scene's slides overlap by one step."""
    bad, objs = [], d.get("objects", [])
    for (a, b), (c, _) in zip(ranges, ranges[1:]):
        if c != b:
            bad.append("%s: slides %d-%d then %d-…: ranges must overlap by one step, or step %d never animates"
                       % (slug, a, b, c, c))
    # a march on a slide's ground step does not travel — unless that step is also the last click of the
    # slide before it, which is what overlapping the ranges is for
    ends = {b for _, b in ranges}
    for i, (a, _) in enumerate(ranges):
        if i > 0 and a in ends:
            continue
        for o in objs:
            if o["type"] == "army" and o.get("follows") and o.get("step") == a:
                bad.append("%s: %r marches on step %d, which is a slide's ground — it will not travel"
                           % (slug, o.get("name"), a))
    return bad


# ---------------------------------------------------------------------------------------- crowding
# Where the painter puts things — the numbers are tools/mapstudio/src/render.js and tokens.js, not guesses.
# The first version of this estimate treated a banner as a circle and a letter as half an em, and passed
# three maps the eye rejected at once: a flag over a name, a name off the edge of the frame, a banner on a
# town's label. A check that is kinder than the painter is not a check.
def _px(view, lon, lat):
    return (lon * K - view["cx"]) * view["scale"] + STAGE_W / 2, (-lat - view["cy"]) * view["scale"] + STAGE_H / 2


def _ll(view, x, y):
    return ((x - STAGE_W / 2) / view["scale"] + view["cx"]) / K, -((y - STAGE_H / 2) / view["scale"] + view["cy"])


def _last(d):
    return max([d.get("steps", {}).get("count", 1)] + [o.get("step", 1) for o in d.get("objects", [])])


def _anchor(pos, x, y, rad, m):                       # render.js labelAnchor
    if pos == "left":
        return x - rad - 5 * m, y, "right"
    if pos == "above":
        return x, y - rad - 9 * m, "center"
    if pos == "below":
        return x, y + rad + 11 * m, "center"
    return x + rad + 5 * m, y, "left"


def _text(x, y, align, lines):
    """lines: [(string, font px, offset down from the anchor)]. Text is drawn with its middle on the anchor."""
    w = max(CH * f * len(s) for s, f, _ in lines)
    top = min(dy - f * 0.60 for _, f, dy in lines)
    bot = max(dy + f * 0.60 for _, f, dy in lines)
    x0 = x - w if align == "right" else (x - w / 2.0 if align == "center" else x)
    return x0, y + top, x0 + w, y + bot


def _boxes(o, view, mark, pos=None):
    """Where a mark and its lettering fall on the stage: [(x0, y0, x1, y1, kind, what)].
    kind is "text" (lettering), "banner" (a force), "flag", "place", "clash"."""
    m = mark * o.get("scale", 1)
    t = o["type"]
    if o.get("lon") is None and t != "arrow":
        return []
    if t == "label":
        f = (o.get("size") or 10) * m
        x, y = _px(view, o["lon"], o["lat"])
        return [_text(x, y, o.get("align") or "left", [(o.get("text", ""), f, 0)]) + ("text", o.get("text", ""))]
    if t == "arrow":
        if not (o.get("label") or "").strip():
            return []
        mid = o["pts"][len(o["pts"]) // 2]
        x, y = _px(view, mid[0], mid[1])
        return [_text(x, y - 15 * m, "center", [(o["label"], 14 * m, 0)]) + ("text", o["label"])]
    if t not in ("settlement", "army", "battle"):
        return []
    x, y = _px(view, o["lon"], o["lat"])
    name, pos, out = o.get("name") or "", pos or o.get("labelPos", "right"), []
    if t == "army":
        out.append((x - 18 * m, y - 18 * m, x + 18 * m, y + 20 * m, "banner", name or "a force"))
        out.append((x, y - 46 * m, x + 33 * m, y - 25 * m, "flag", (name or "a force") + "'s flag"))
        if name:
            ax, ay, al = _anchor(pos, x, y - 17 * m, 36 * m, m)
            lines = [(name, 15 * m, 0)] + ([(o["strength"], 12.5 * m, 17 * m)] if o.get("strength") else [])
            out.append(_text(ax, ay, al, lines) + ("text", name))
    elif t == "settlement":
        big = o.get("tier") == "capital"
        rad = (15 if big else 10 if o.get("tier") == "fort" else 8) * m
        out.append((x - rad * 0.7, y - rad * 0.7, x + rad * 0.7, y + rad * 0.7, "place", name or "a place"))
        if name:
            ax, ay, al = _anchor(pos, x, y, rad, m)
            out.append(_text(ax, ay, al, [(name, (17 if big else 14.5) * m, 0)]) + ("text", name))
    else:
        out.append((x - 21 * m, y - 21 * m, x + 21 * m, y + 21 * m, "clash", name or "a battle mark"))
        if name:
            ax, ay, al = _anchor(pos, x, y, 24 * m, m)
            lines = [(name, 15 * m, 0)] + ([(o["date"], 12.5 * m, 17 * m)] if o.get("date") else [])
            out.append(_text(ax, ay, al, lines) + ("text", name))
    return out


def _road(o, view, mark):
    """An arrow as a string of small boxes — something a name or a caption should keep off, where it can."""
    if o["type"] != "arrow":
        return []
    half = (o.get("width") or 14) * mark * o.get("scale", 1) / 2.0 + 6
    pts = [_px(view, p[0], p[1]) for p in o.get("pts", [])]
    out = []
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        n = max(1, int(math.hypot(x1 - x0, y1 - y0) / 28))
        for i in range(n + 1):
            x, y = x0 + (x1 - x0) * i / n, y0 + (y1 - y0) * i / n
            out.append((x - half, y - half, x + half, y + half, "road", "an arrow"))
    return out


def _over(a, b, pad=0.0):
    w = min(a[2], b[2]) - max(a[0], b[0]) - pad
    h = min(a[3], b[3]) - max(a[1], b[1]) - pad
    return w * h if w > 0 and h > 0 else 0.0


def _off(b, edge=6.0):
    """How much of a box hangs off the stage, in square pixels."""
    w, h = b[2] - b[0], b[3] - b[1]
    iw = min(b[2], STAGE_W - edge) - max(b[0], edge)
    ih = min(b[3], STAGE_H - edge) - max(b[1], edge)
    return w * h - max(0.0, iw) * max(0.0, ih)


def _everything(d, skip=None, roads=False):
    """Every box on the map with the steps it is there for: [(object id, first, last, box)]."""
    view, mark, last = d["view"], d.get("style", {}).get("markScale", 1.0), _last(d)
    out = []
    for o in d.get("objects", []):
        if o is skip or "auto" in o:
            continue
        span = (o.get("step", 1), o.get("until", last))
        for b in _boxes(o, view, mark) + (_road(o, view, mark) if roads else []):
            out.append((o["id"], span[0], span[1], b))
    if d.get("style", {}).get("scalebar"):
        out.append(("scalebar", 1, last, SCALEBAR + ("place", "the scale bar")))
    return out


def settle(d, keep=()):
    """Every name takes the side of its mark where it covers nothing and stays on the stage (M15, M10).

    A name that is in nobody's way is left where its author put it. Returns how many were moved. Works on any
    scene, kit-made or hand-made: settle(json.load(...)) is how an old scene is brought up to the rule."""
    view = d.get("view", {})
    if not view.get("scale"):
        return 0
    mark, last = d.get("style", {}).get("markScale", 1.0), _last(d)
    movable = [o for o in d.get("objects", [])
               if o["type"] in ("settlement", "army", "battle") and o.get("name") and o["id"] not in keep]

    def cost(o, pos):
        mine = [b for b in _boxes(o, view, mark, pos) if b[4] == "text"]
        s, u = o.get("step", 1), o.get("until", last)
        c = 0.0
        for b in mine:
            c += 40.0 * _off(b)
            for oid, fs, fu, fb in _everything(d, skip=o, roads=True):
                if max(s, fs) <= min(u, fu):
                    c += _over(b, fb, 2.0) * (0.3 if fb[4] == "road" else 1.0)
        return c

    moved = 0
    for _ in range(5):
        changed = False
        for o in sorted(movable, key=lambda q: q["id"]):
            cur = o.get("labelPos", "right")
            best, least = cur, cost(o, cur)
            if least <= 0:
                continue
            for pos in SIDES:
                if pos != cur:
                    c = cost(o, pos)
                    if c < least - 1e-6:
                        best, least = pos, c
            if best != cur:
                o["labelPos"], changed, moved = best, True, moved + 1
        if not changed:
            break
    return moved


def place_captions(d, slug=""):
    """A caption given no position takes the free spot nearest what it is about — clear of every name and
    mark that is on the map while it is, and off the arrows where there is room (M9, M15)."""
    view, objs = d.get("view", {}), d.get("objects", [])
    todo = [o for o in objs if o["type"] == "label" and "auto" in o]
    if not todo:
        return
    mark, last = d.get("style", {}).get("markScale", 1.0), _last(d)
    for o in todo:
        s, u = o.get("step", 1), o.get("until", last)
        f = o["size"] * mark * o.get("scale", 1)
        w, h = CH * f * len(o["text"]), f * 1.2
        target = o.get("auto")
        if target is None:                                  # the middle of whatever comes on with this click
            pts = [(q["lon"], q["lat"]) for q in objs
                   if q.get("step", 1) == s and q is not o and q.get("lon") is not None and q["type"] != "label"]
            pts += [tuple(q["pts"][-1]) for q in objs if q.get("step", 1) == s and q["type"] == "arrow"]
            if pts:
                target = (sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts))
        tx, ty = _px(view, target[0], target[1]) if target else (STAGE_W / 2, STAGE_H * 0.22)
        there = [(fb, fb[4] == "road") for _, fs, fu, fb in _everything(d, roads=True) if max(s, fs) <= min(u, fu)]
        best = None
        y = 44 + h / 2
        while y <= STAGE_H - 44 - h / 2:
            x = 44 + w / 2
            while x <= STAGE_W - 44 - w / 2:
                box = (x - w / 2 - 14, y - h / 2 - 12, x + w / 2 + 14, y + h / 2 + 12)
                score = math.hypot(x - tx, y - ty)
                for fb, road in there:
                    if _over(box, fb) > 0:
                        if not road:
                            score = None
                            break
                        score += 9.0
                if score is not None and (best is None or score < best[0]):
                    best = (score, x, y)
                x += 30
            y += 24
        if best is None:
            raise SceneError("%s: no room for the caption %r at step %d — shorten it, or thin the step"
                             % (slug, o["text"], s))
        o["lon"], o["lat"] = _ll(view, best[1], best[2])
        del o["auto"]


def settle_captions(d, slug=""):
    """A hand-placed scene brought up to the rule: a caption or a standing name that is printed over
    something, or hangs off the stage, moves to the nearest free spot. One that is clear is not touched."""
    view = d.get("view", {})
    if not view.get("scale"):
        return 0
    mark, last, moved = d.get("style", {}).get("markScale", 1.0), _last(d), 0
    for o in d.get("objects", []):
        if o["type"] != "label" or o.get("lon") is None:
            continue
        s, u = o.get("step", 1), o.get("until", last)
        mine = _boxes(o, view, mark)[0]
        size = (mine[2] - mine[0]) * (mine[3] - mine[1]) or 1.0
        hit = _off(mine) > 0.10 * size
        for oid, fs, fu, fb in _everything(d, skip=o):
            if max(s, fs) <= min(u, fu) and _over(mine, fb, 2.0) > 0.04 * min(size, (fb[2] - fb[0]) * (fb[3] - fb[1])):
                hit = True
                break
        if hit:
            o["auto"], o["align"] = [o["lon"], o["lat"]], "center"
            place_captions(d, slug)
            moved += 1
    return moved


def check_crowding(d, slug="", allow=0.04, banners=0.22):
    """M15 — nothing is printed over anything else — and M10 for lettering: no name runs off the stage.

    Daniyal on evening 5: "some of the click click maps become too crowded"; on evening 6 the first close-up
    put three forces on one spot. Lettering may not be covered by, or cover, anything that is on the map at
    the same step; two banners may touch, and may not stand on each other."""
    view = d.get("view", {})
    if not view.get("scale"):
        return []
    items = _everything(d)
    bad, seen = [], set()
    for oid, s, _, b in items:
        if b[4] in ("text", "banner", "flag") and _off(b) > 0.10 * (b[2] - b[0]) * (b[3] - b[1])                 and ("off", b[5]) not in seen:
            seen.add(("off", b[5]))
            bad.append("M10 %r %s (step %d)" % (b[5], "runs off the edge of the map" if b[4] == "text"
                                                else "is cut by the edge of the map", s))
    for i, (ia, sa, ua, a) in enumerate(items):
        for ib, sb, ub, b in items[i + 1:]:
            if ia == ib or max(sa, sb) > min(ua, ub):
                continue
            kinds = {a[4], b[4]}
            if "text" in kinds:
                limit = allow
            elif kinds == {"banner"}:
                limit = banners
            else:
                continue                      # a banner on its own town, a battle mark on a camp: meant
            area = _over(a, b, 2.0)
            small = min((a[2] - a[0]) * (a[3] - a[1]), (b[2] - b[0]) * (b[3] - b[1])) or 1.0
            key = tuple(sorted((a[5], b[5])))
            if area / small > limit and key not in seen:
                seen.add(key)
                first, second = (a, b) if a[4] == "text" else (b, a)
                bad.append("M15 %r is printed over %r at step %d" % (first[5], second[5], max(sa, sb)))
    return ["%s: %s" % (slug, x) if slug else x for x in bad]


def check_places(scenes):
    """One place, one spot: a town drawn on two maps of an evening is in the same place on both. A diagram is
    exempt — it claims an order, not a place — and says so on its face."""
    seen, bad = {}, []
    for slug in sorted(scenes):
        d = scenes[slug]
        if d.get("meta", {}).get("kind") == "diagram":
            continue
        for o in d.get("objects", []):
            if o["type"] != "settlement" or not o.get("name"):
                continue
            at = (round(o["lon"], 3), round(o["lat"], 3))
            was = seen.setdefault(o["name"], (at, slug))
            if was[0] != at:
                bad.append("%s: M12 %r is at %s here and at %s on %s — one place, one spot"
                           % (slug, o["name"], at, was[0], was[1]))
    return bad
