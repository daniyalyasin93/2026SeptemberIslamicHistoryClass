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
        return self._add("settlement", "place", lon=lon, lat=lat, name=name, ur="", tier=tier,
                         labelPos=pos, scale=scale)

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

    # ------------------------------------------------------------------ what happens
    def siege(self, lon, lat, faction, r=0.10, arms=5):
        """A siege is drawn as a siege: a ring round the place and columns closing on it from every side."""
        ring = [[lon + r / K * math.cos(a), lat + r * math.sin(a)]
                for a in [2 * math.pi * i / 28 for i in range(28)]]
        made = [self._add("territory", "siege", pts=ring, faction=faction, label="", ur="", opacity=0.10)]
        for i in range(arms):
            a = 2 * math.pi * i / arms + 0.5
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

    def say(self, text, lon, lat, hold=False, size=SAY, align="center"):
        """A caption for this click. It fades on the next one unless held, so captions never pile up."""
        o = self._add("label", "say", lon=lon, lat=lat, text=text, ur="", size=size, align=align)
        if not hold:
            o["until"] = self.step
        return o

    def name(self, text, lon, lat, size=24, align="center"):
        """A standing name on the ground — a region, a sea, a desert. It stays."""
        return self._add("label", "name", lon=lon, lat=lat, text=text, ur="", size=size, align=align)

    # ------------------------------------------------------------------ out
    def data(self):
        return {"schema": 1,
                "meta": {"title": self.title, "subtitle": self.subtitle, "urduTitle": "",
                         "note": "Written by series/mapkit.py. Edit the script that made it, not this file: "
                                 "regenerating overwrites a hand nudge."},
                "view": dict(self.view), "style": dict(self.style), "factions": [dict(f) for f in FACTIONS],
                "underlay": None, "objects": self.objs,
                "steps": {"count": self.step, "current": self.step, "mode": "upto"}}

    def save(self):
        problems = self.check()
        if problems:
            raise SceneError("%s breaks the map rules:\n   %s" % (self.slug, "\n   ".join(problems)))
        path = os.path.join(SCENES, self.slug + ".json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.data(), f, ensure_ascii=False, indent=1)
        return path

    def clicks(self, a, b):
        """The ▶ CLICK lines of the slide showing steps a..b — one for every step after its ground."""
        return [self.cues[k] for k in range(a + 1, b + 1) if k in self.cues]

    def check(self):
        return check_scene(self.data(), self.slug) + check_crowding(self.data(), self.slug)


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
        if "lon" in o and not (lo0 <= o["lon"] <= lo1 and la0 <= o["lat"] <= la1):
            bad.append("M10 %s %r is off the stage (%.2f, %.2f)" % (t, who, o["lon"], o["lat"]))

    # M5 — every arrow says who is moving
    followed = {o.get("follows") for o in objs if o["type"] == "army" and o.get("follows")}
    for o in objs:
        if o["type"] == "arrow" and o["id"] not in followed and not (o.get("label") or "").strip():
            if not str(o.get("note", "")).startswith(("siege", "letter")):
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
def _px(view, lon, lat):
    return (lon * K - view["cx"]) * view["scale"] + STAGE_W / 2, (-lat - view["cy"]) * view["scale"] + STAGE_H / 2


def _boxes(o, view, mark):
    """Roughly where a mark and its lettering fall on the stage: [(x0, y0, x1, y1, what)]. An estimate — the
    painter is the truth — but it is enough to catch one name printed over another."""
    m = mark * o.get("scale", 1)
    t = o["type"]
    if t == "label":
        f = (o.get("size") or 10) * m
        w = 0.50 * f * len(o.get("text", ""))
        x, y = _px(view, o["lon"], o["lat"])
        x0 = x - w / 2 if o.get("align", "left") == "center" else (x - w if o.get("align") == "right" else x)
        return [(x0, y - f * 0.6, x0 + w, y + f * 0.6, o.get("text", ""))]
    if t not in ("settlement", "army", "battle") or "lon" not in o:
        return []
    x, y = _px(view, o["lon"], o["lat"])
    r = (17.0 if t == "army" else 6.0) * m
    out = [(x - r, y - r, x + r, y + r, (o.get("name") or t) + " (mark)")] if t == "army" else []
    name = o.get("name") or ""
    if not name:
        return out
    f = (15.0 if t != "settlement" else 14.5) * m
    lines = [(name, f)] + ([(o["strength"], 12.5 * m)] if t == "army" and o.get("strength") else [])
    w = max(0.50 * ff * len(s) for s, ff in lines)
    h = sum(ff * 1.25 for _, ff in lines)
    pos, gap = o.get("labelPos", "right"), 6 * m
    if pos == "left":
        bx, by = x - r - gap - w, y - h / 2
    elif pos == "above":
        bx, by = x - w / 2, y - r - gap - h - (16 * m if t == "army" else 0)
    elif pos == "below":
        bx, by = x - w / 2, y + r + gap
    else:
        bx, by = x + r + gap, y - h / 2
    return out + [(bx, by, bx + w, by + h, name)]


def check_crowding(d, slug="", allow=0.18):
    """M15 — nothing is printed over anything else. Daniyal on evening 5: "some of the click click maps
    become too crowded"; on evening 6 the first close-up put three forces on one spot. Two things on the
    map at the same step may not overlap by more than `allow` of the smaller one."""
    view, objs = d.get("view", {}), d.get("objects", [])
    if not view.get("scale"):
        return []
    mark = d.get("style", {}).get("markScale", 1.0)
    last = max([d.get("steps", {}).get("count", 1)] + [o.get("step", 1) for o in objs])
    items = []
    for o in objs:
        for b in _boxes(o, view, mark):
            items.append((o["id"], o.get("step", 1), o.get("until", last), b))
    bad, seen = [], set()
    for i, (ia, sa, ua, a) in enumerate(items):
        for ib, sb, ub, b in items[i + 1:]:
            if ia == ib or max(sa, sb) > min(ua, ub):
                continue
            w = min(a[2], b[2]) - max(a[0], b[0])
            h = min(a[3], b[3]) - max(a[1], b[1])
            if w <= 0 or h <= 0:
                continue
            small = min((a[2] - a[0]) * (a[3] - a[1]), (b[2] - b[0]) * (b[3] - b[1])) or 1.0
            key = tuple(sorted((a[4], b[4])))
            if w * h / small > allow and key not in seen:
                seen.add(key)
                bad.append("M15 %r is printed over %r at step %d" % (a[4], b[4], max(sa, sb)))
    return ["%s: %s" % (slug, x) if slug else x for x in bad]
