# MAPS — inventory

One schematic SVG base map, per-session variants by toggling layers. Six anchor cities:
مکہ · مدینہ · دمشق · بغداد · قرطبہ · قسطنطنیہ.

Raster frames from Kings & Generals via `tools/grab_frame.py` are for slide drama only —
print artifacts use the SVG.

| Asset | Shows | Used in | Licence / origin |
|---|---|---|---|
| `maps/world_632_kandg.png` | Two empires + the Hijaz, c.632 | (v1 deck) | K&G video frame |

## Map Studio — `tools/mapstudio/`

The campaign-map editor. Double-click `tools/mapstudio/index.html`; no server, works
offline. Place settlements, army banners, battles, campaign arrows and territory on a
Natural Earth base with real shaded relief, rivers and lakes, then export a 4K PNG or one
PNG per step for a build-up across slides. Scenes save as JSON into
`tools/mapstudio/scenes/` so a map is reproducible and diffable.

Same projection as `series/make_basemap.py` (equirectangular, standard parallel 30N), so
its exports sit beside the workbook base map. Full notes in `tools/mapstudio/README.md`.

**Caveat that matters:** the built-in gazetteer (`data/places.js`) is approximate modern
coordinates for placement only, never a claim about a site. Entries it marks *site
approximate* - Yarmuk, Qadisiyya, Buzakha, Dibal, Ajnadayn - are genuinely disputed.
