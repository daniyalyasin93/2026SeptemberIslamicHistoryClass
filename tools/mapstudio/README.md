# Map Studio

A campaign-map editor for the lecture series. Draw the ancient world, put settlements,
army banners, battles, campaign arrows and territory on it, and export a 4K PNG straight
into a deck.

**Open it by double-clicking `index.html`.** No server, no install, no build step. It is
plain HTML and JavaScript and it works offline.

---

## The 60-second version

1. Pick a region from the **Jump to region…** menu, or pan and zoom with drag and wheel.
2. Search the **Places** panel and click a name — the settlement lands on the right spot.
3. Press `A`, click the map, and set the faction and unit type on the right.
4. Press `R`, click a few waypoints, press `Enter` — you have a campaign arrow.
5. Type a title top-left, then **Export PNG**.

---

## The tools

| Key | Tool | What it makes |
|---|---|---|
| `V` | Select | Click to select, drag to move, drag a vertex to reshape a path |
| `S` | Settlement | Capital · city · town · fort, each a different mark |
| `A` | Army | Banner in the faction colour, with a unit silhouette, name and strength |
| `B` | Battle | Crossed swords with a name and a date |
| `R` | Arrow | Tapered campaign arrow, solid or dashed. `Enter` finishes, `Backspace` undoes a point |
| `T` | Territory | Semi-transparent faction control with a frontier line |
| `L` | Label | Free text — a region, a sea, a note |

Also: `Ctrl+Z` / `Ctrl+Shift+Z` undo and redo · `Ctrl+S` save · `Ctrl+E` export ·
`Delete` remove · `[` and `]` step back and forward · `Esc` deselect or cancel a path ·
`Alt+drag` or middle-drag to pan.

---

## The things worth knowing

**Mark size.** The *Look* panel has a **Mark size** slider that lifts every mark and label
together, and each object has its own **Size** slider on top of it. A map of the whole
caliphate needs bigger marks than a map of Najd to stay legible from the back of a hall —
that is the dial for it. Hit-testing follows the scale, so big marks stay clickable.

**Steps.** Every object carries a step number. Set the step slider to "everything up to
this step" and press **Export steps**: you get `title-step-01.png`, `-02`, `-03`… That is
how you build a map up across consecutive slides instead of dropping the finished thing on
the room at once. Chrome asks once to allow multiple downloads.

**Terrain.** The base map is Natural Earth: 1:50m coastlines, 1:50m shaded relief, rivers
and lakes. Mountains read as mountains. Turn it off, or dial **Relief strength** down, in
the *Look* panel.

**Underlay.** Drop any image on the map — a downloaded Wikimedia map, or a frame grabbed
with `tools/grab_frame.py` — and it becomes a background layer you can trace over. Drag to
move it, `Shift`+drag to scale, then untick *Move / scale it*. **Hide it before you
export**, unless you have the right to redistribute it.

**Territory captions** are drawn at the polygon's centre. When that lands somewhere
unhelpful, clear the territory's label and drop a free **Label** where you actually want it.

**Scenes are JSON.** Save writes a `.json` file — put it in `scenes/` and it lives in git,
diffs cleanly, and can be hand-edited when that is faster than clicking. Work is also
autosaved to browser storage, so a closed tab is not a lost afternoon. **New** clears it.

**The gazetteer is for placement, not for citation.** `data/places.js` holds ~120
approximate modern coordinates so you can type a name instead of hunting for a spot. They
are not a historical claim about a site. Entries the picker marks **site approximate** —
Yarmūk, Qādisiyya, Buzākha, Dībal, Ajnādayn and others — are genuinely disputed. Check
before any of them reaches a slide.

---

## Rebuilding the data

The three generated files under `data/` are committed so the tool works out of the box.
Regenerate them only if you change the bounding box or want a different resolution:

```bash
python tools/mapstudio/build_land.py       # coastlines   -> data/land.js   (~120 KB)
python tools/mapstudio/build_terrain.py    # relief+water -> data/relief.js, data/water.js
```

`build_terrain.py` downloads ~13 MB from Natural Earth on first run and caches it in
`.cache/`, which is gitignored. Re-runs are free.

The relief is embedded as a base64 `data:` URI rather than referenced as a `.jpg` for a
concrete reason: drawing a `file://` image onto a canvas taints it, and a tainted canvas
cannot be exported with `toBlob()` — PNG export would break silently. Do not "optimise"
this into a plain image file.

---

## Layout

```
index.html          the one screen
style.css           studio chrome
build_land.py       Natural Earth coastlines -> data/land.js
build_terrain.py    shaded relief, rivers, lakes -> data/relief.js, data/water.js
data/               generated data + the gazetteer
src/proj.js         projection, viewport, geometry helpers
src/store.js        scene state, undo, save/load, steps
src/tokens.js       the marks: banners, silhouettes, arrows, settlements
src/render.js       the painter — screen and export use the same function
src/ui.js           tools, panels, hit-testing, export
src/demo.js         the ?demo=1 sample scene, and a worked example of the JSON shape
scenes/             your saved maps
exports/            somewhere to keep the PNGs
```

The projection matches `series/make_basemap.py` — equirectangular, standard parallel 30°N —
so a Map Studio export sits beside the workbook base map without looking like a different
world.

## Sources and licence

Natural Earth (naturalearthdata.com), public domain: 1:50m land, 1:50m shaded relief
(`SR_50M`), 1:50m rivers and lake centrelines, 1:50m lakes. Credit the channel or the
Commons file for anything you import as an underlay, and check the licence before any
public use.
