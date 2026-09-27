# -*- coding: utf-8 -*-
"""Maps that build up on clicks while the speaker talks (DECISIONS.md #58).

    import anim
    s = D.map_slide(prs, manifest_base_png, headline, keys=..., map_frac=0.70, trim=False)
    placed = anim.place_layers(s, "…/s05-01-aqraba-r1-6-layers.json")
    clicks = anim.animate(s, placed)          # -> the number of clicks the slide now has

WHAT THE ROOM SEES. One slide, one map, and it stays up while that part is told. Each click is one beat:

    an arrow          wipes on along its route, from the edge it starts at
    an army that      appears at the start of the arrow it follows and travels along it, arriving where
      follows one       it is drawn — the troops moving as the speaker speaks
    anything else     fades in (a territory turning green, a label, a battle mark)
    a mark that       fades out on the click after its last step (Map Studio's "Hide after step")
      leaves

HOW. tools/render_scene.py --layers renders the ground once and every moving mark as its own
transparent picture, cut to its own box, with a manifest of where each sits and on which click it comes
and goes. This file puts each picture exactly over the ground, names it for its object so Daniyal can
move one or use Change Picture (the animation stays with the shape), and writes the slide's click timing
as PowerPoint's own XML — python-pptx has no API for animation.

WHY THE XML IS WRITTEN BY HAND AND CHECKED BY PLAYING IT. PowerPoint rejects malformed timing silently
or with a repair prompt. The shapes here are the ones PowerPoint itself writes for Wipe (preset 22),
Fade (10), Appear (1) and a custom motion path, and the evening-5 trial (spec §2.4) plays the result:
PowerPoint exports the slide to video and the frames are looked at.
"""
import json
import os

from lxml import etree
from pptx.util import Emu

P = "http://schemas.openxmlformats.org/presentationml/2006/main"

# direction of travel -> (presetSubtype, filter). PowerPoint names a wipe by the edge it starts FROM:
# an arrow travelling right is revealed from its left edge ("From Left", subtype 8).
WIPE = {"right": (8, "wipe(left)"), "left": (2, "wipe(right)"),
        "down": (1, "wipe(up)"), "up": (4, "wipe(down)")}

DUR_WIPE = 1600      # ms — slow enough to be seen as a march, not a flicker
DUR_MOVE = 1600
DUR_FADE = 600


def _direction(pts):
    (x0, y0), (x1, y1) = pts[0], pts[-1]
    dx, dy = x1 - x0, y1 - y0
    if abs(dx) >= abs(dy):
        return "right" if dx >= 0 else "left"
    return "down" if dy >= 0 else "up"


def place_layers(slide, manifest_path, base_name="map"):
    """Put every layer of the manifest exactly over the slide's ground picture (the shape named
    `base_name`). Returns [(layer, shape), …] in painting order."""
    with open(manifest_path, encoding="utf-8") as f:
        man = json.load(f)
    base = [s for s in slide.shapes if s.name == base_name]
    if not base:
        raise ValueError("no picture named %r on the slide — place the ground with deck2.map_slide(trim=False)"
                         % base_name)
    base = base[0]
    sx = base.width / float(man["width"])            # EMU per image pixel
    sy = base.height / float(man["height"])
    folder = os.path.dirname(os.path.abspath(manifest_path))
    placed = []
    for m in man["layers"]:
        x0, y0, x1, y1 = m["box"]
        pic = slide.shapes.add_picture(os.path.join(folder, m["file"]),
                                       Emu(int(base.left + x0 * sx)), Emu(int(base.top + y0 * sy)),
                                       width=Emu(int((x1 - x0) * sx)), height=Emu(int((y1 - y0) * sy)))
        pic.name = "map %s %s" % (m["type"], (m.get("name") or m["id"])[:40])
        m = dict(m, _sx=sx, _sy=sy)
        placed.append((m, pic))
    return placed


class _Ids:
    def __init__(self):
        self.n = 2                                   # 1 = the root, 2 = the main sequence

    def __call__(self):
        self.n += 1
        return self.n


def _vis(ids, spid, value, delay=0):
    return ('<p:set><p:cBhvr><p:cTn id="%d" dur="1" fill="hold"><p:stCondLst><p:cond delay="%d"/>'
            '</p:stCondLst></p:cTn><p:tgtEl><p:spTgt spid="%s"/></p:tgtEl><p:attrNameLst>'
            '<p:attrName>style.visibility</p:attrName></p:attrNameLst></p:cBhvr><p:to><p:strVal val="%s"/>'
            '</p:to></p:set>' % (ids(), delay, spid, value))


def _effect(ids, spid, node, preset, cls, sub, body):
    return ('<p:par><p:cTn id="%d" presetID="%d" presetClass="%s" presetSubtype="%d" fill="hold" grpId="0" '
            'nodeType="%s"><p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>%s</p:childTnLst>'
            '</p:cTn></p:par>' % (ids(), preset, cls, sub, node, body))


def _fade_in(ids, spid, node):
    return _effect(ids, spid, node, 10, "entr", 0,
                   _vis(ids, spid, "visible") +
                   '<p:animEffect transition="in" filter="fade"><p:cBhvr><p:cTn id="%d" dur="%d"/>'
                   '<p:tgtEl><p:spTgt spid="%s"/></p:tgtEl></p:cBhvr></p:animEffect>' % (ids(), DUR_FADE, spid))


def _wipe_in(ids, spid, node, direction):
    sub, flt = WIPE[direction]
    return _effect(ids, spid, node, 22, "entr", sub,
                   _vis(ids, spid, "visible") +
                   '<p:animEffect transition="in" filter="%s"><p:cBhvr><p:cTn id="%d" dur="%d"/>'
                   '<p:tgtEl><p:spTgt spid="%s"/></p:tgtEl></p:cBhvr></p:animEffect>' % (flt, ids(), DUR_WIPE, spid))


def _appear(ids, spid, node):
    return _effect(ids, spid, node, 1, "entr", 0, _vis(ids, spid, "visible"))


def _move(ids, spid, node, path):
    return _effect(ids, spid, node, 0, "path", 0,
                   '<p:animMotion origin="layout" path="%s" pathEditMode="relative" rAng="0" ptsTypes="">'
                   '<p:cBhvr><p:cTn id="%d" dur="%d" fill="hold"/><p:tgtEl><p:spTgt spid="%s"/></p:tgtEl>'
                   '<p:attrNameLst><p:attrName>ppt_x</p:attrName><p:attrName>ppt_y</p:attrName></p:attrNameLst>'
                   '</p:cBhvr></p:animMotion>' % (path, ids(), DUR_MOVE, spid))


def _fade_out(ids, spid, node):
    return _effect(ids, spid, node, 10, "exit", 0,
                   '<p:animEffect transition="out" filter="fade"><p:cBhvr><p:cTn id="%d" dur="%d"/>'
                   '<p:tgtEl><p:spTgt spid="%s"/></p:tgtEl></p:cBhvr></p:animEffect>' % (ids(), DUR_FADE, spid) +
                   _vis(ids, spid, "hidden", delay=DUR_FADE - 1))


def _route_path(m, pic, slide_w, slide_h):
    """A motion path, in slide fractions, from the start of the followed arrow to where the army is drawn."""
    ax, ay = m["at"]
    pts = [((x - ax) * m["_sx"] / slide_w, (y - ay) * m["_sy"] / slide_h) for x, y in m["route"]]
    segs = ["M %.4f %.4f" % pts[0]] + ["L %.4f %.4f" % p for p in pts[1:]] + ["L 0 0", "E"]
    return " ".join(segs)


def animate(slide, placed, slide_w, slide_h):
    """Write the click timing for the placed layers. Returns the number of clicks."""
    ids = _Ids()
    by_id = {m["id"]: (m, pic) for m, pic in placed}
    clicks = sorted({m["enter"] for m, _ in placed if m["enter"]} | {m["exit"] for m, _ in placed if m["exit"]})
    groups = []
    for k in clicks:
        eff = []
        for m, pic in placed:
            spid = pic.shape_id
            if m["enter"] == k:
                if m["type"] == "arrow" and m.get("pts"):
                    eff.append(("wipe", spid, _direction(m["pts"])))
                elif m["type"] == "army" and m.get("route") and by_id.get(m.get("follows"), (None,))[0] \
                        and by_id[m["follows"]][0]["enter"] == k:
                    eff.append(("appear", spid, None))
                    eff.append(("move", spid, _route_path(m, pic, slide_w, slide_h)))
                else:
                    eff.append(("fade", spid, None))
            if m["exit"] == k:
                eff.append(("out", spid, None))
        body = []
        for i, (kind, spid, arg) in enumerate(eff):
            node = "clickEffect" if i == 0 else "withEffect"
            body.append({"wipe": lambda: _wipe_in(ids, spid, node, arg),
                         "fade": lambda: _fade_in(ids, spid, node),
                         "appear": lambda: _appear(ids, spid, node),
                         "move": lambda: _move(ids, spid, node, arg),
                         "out": lambda: _fade_out(ids, spid, node)}[kind]())
        groups.append('<p:par><p:cTn id="%d" fill="hold"><p:stCondLst><p:cond delay="indefinite"/></p:stCondLst>'
                      '<p:childTnLst><p:par><p:cTn id="%d" fill="hold"><p:stCondLst><p:cond delay="0"/>'
                      '</p:stCondLst><p:childTnLst>%s</p:childTnLst></p:cTn></p:par></p:childTnLst></p:cTn></p:par>'
                      % (ids(), ids(), "".join(body)))
    xml = ('<p:timing xmlns:p="%s"><p:tnLst><p:par><p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot">'
           '<p:childTnLst><p:seq concurrent="1" nextAc="seek"><p:cTn id="2" dur="indefinite" nodeType="mainSeq">'
           '<p:childTnLst>%s</p:childTnLst></p:cTn><p:prevCondLst><p:cond evt="onPrev" delay="0"><p:tgtEl>'
           '<p:sldTgt/></p:tgtEl></p:cond></p:prevCondLst><p:nextCondLst><p:cond evt="onNext" delay="0"><p:tgtEl>'
           '<p:sldTgt/></p:tgtEl></p:cond></p:nextCondLst></p:seq></p:childTnLst></p:cTn></p:par></p:tnLst>'
           '</p:timing>' % (P, "".join(groups)))
    timing = etree.fromstring(xml)
    sld = slide._element
    for old in sld.findall("{%s}timing" % P):
        sld.remove(old)
    # schema order: cSld, clrMapOvr, transition, timing, extLst
    anchor = sld.find("{%s}transition" % P)
    if anchor is None:
        anchor = sld.find("{%s}clrMapOvr" % P)
    if anchor is not None:
        anchor.addnext(timing)
    else:
        sld.append(timing)
    return len(clicks)
