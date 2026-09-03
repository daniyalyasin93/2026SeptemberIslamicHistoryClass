/* ui.js — tools, panels, hit-testing, export.
 *
 * The app is deliberately one screen: a 16:9 stage that is exactly what gets
 * exported, a tool rail on the left, and everything you can change on the right.
 * Nothing is hidden behind a menu, because this gets used while preparing a talk,
 * not while learning software.
 */
(function (global) {
  'use strict';

  var P = MS_Proj, S = MS_Store, T = MS_Tokens, R = MS_Render;

  var store = new S.Store();
  var canvas, ctx, dpr = 1;
  var tool = 'select';
  var draft = null;            // in-progress arrow/territory points, in geo
  var drag = null;             // {mode, id, ...}
  var images = {};             // dataURL -> HTMLImageElement
  var needsDraw = true;
  var statusTimer = null;

  var $ = function (sel) { return document.querySelector(sel); };
  var $$ = function (sel) { return Array.prototype.slice.call(document.querySelectorAll(sel)); };

  function el(tag, attrs, kids) {
    var e = document.createElement(tag);
    if (attrs) Object.keys(attrs).forEach(function (k) {
      if (k === 'text') e.textContent = attrs[k];
      else if (k === 'html') e.innerHTML = attrs[k];
      else if (k.slice(0, 2) === 'on') e.addEventListener(k.slice(2), attrs[k]);
      else if (attrs[k] !== null && attrs[k] !== undefined) e.setAttribute(k, attrs[k]);
    });
    (kids || []).forEach(function (c) { e.appendChild(c); });
    return e;
  }

  function status(msg, kind) {
    var s = $('#status');
    s.textContent = msg;
    s.className = kind || '';
    clearTimeout(statusTimer);
    statusTimer = setTimeout(function () { s.textContent = hintFor(tool); s.className = 'dim'; }, 4200);
  }

  function invalidate() { needsDraw = true; }

  /* ---------------- canvas plumbing ---------------- */

  function sizeCanvas() {
    dpr = Math.min(2, global.devicePixelRatio || 1);
    canvas.width = Math.round(P.STAGE_W * dpr);
    canvas.height = Math.round(P.STAGE_H * dpr);
    invalidate();
  }

  function toStageCoords(ev) {
    var r = canvas.getBoundingClientRect();
    return [
      (ev.clientX - r.left) / r.width * P.STAGE_W,
      (ev.clientY - r.top) / r.height * P.STAGE_H
    ];
  }

  function frame() {
    if (needsDraw) {
      needsDraw = false;
      R.render(ctx, store, { k: dpr, showSelection: true, images: images });
      drawDraft();
    }
    requestAnimationFrame(frame);
  }

  /* The in-progress arrow/territory, drawn on top of the finished render. */
  function drawDraft() {
    if (!draft || !draft.pts.length) return;
    ctx.save();
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    var pts = draft.pts.map(function (p) { return P.toStage(store.scene.view, p[0], p[1]); });
    if (draft.hover) pts = pts.concat([draft.hover]);
    var f = store.faction(draft.faction || store.scene.factions[0].id);
    if (draft.kind === 'territory' && pts.length >= 3) {
      T.territory(ctx, pts, f.color, 0.18, 1, false);
    } else if (pts.length >= 2) {
      T.arrow(ctx, pts, f.color, 12, false, 1, false);
    }
    ctx.save();
    ctx.setLineDash([4, 4]);
    ctx.strokeStyle = 'rgba(255,232,150,0.85)';
    ctx.lineWidth = 1.2;
    ctx.beginPath();
    ctx.moveTo(pts[0][0], pts[0][1]);
    for (var i = 1; i < pts.length; i++) ctx.lineTo(pts[i][0], pts[i][1]);
    ctx.stroke();
    ctx.restore();
    for (var j = 0; j < pts.length; j++) T.handle(ctx, pts[j][0], pts[j][1], 1);
    ctx.restore();
  }

  /* ---------------- hit testing ---------------- */

  function stagePts(obj) {
    return obj.pts.map(function (p) { return P.toStage(store.scene.view, p[0], p[1]); });
  }

  function hitTest(sx, sy) {
    var objs = store.visibleObjects();
    var base = R.markScale(store.scene);
    for (var i = objs.length - 1; i >= 0; i--) {
      var o = objs[i];
      var m = base * (o.scale || 1);
      if (o.type === 'arrow') {
        var ap = stagePts(o);
        var line = P.smooth(ap.length === 2 ? P.bow(ap[0], ap[1]) : ap, 12);
        if (P.distToPolyline(sx, sy, line) < (o.width || 14) * m * 0.6 + 7) return o;
      } else if (o.type === 'territory') {
        var tp = stagePts(o);
        if (P.pointInPolygon(sx, sy, tp) || P.distToPolyline(sx, sy, tp.concat([tp[0]])) < 8) return o;
      } else if (o.type === 'army') {
        var p = P.toStage(store.scene.view, o.lon, o.lat);
        if (sx > p[0] - 19 * m && sx < p[0] + 38 * m && sy > p[1] - 62 * m && sy < p[1] + 12 * m) return o;
      } else {
        var q = P.toStage(store.scene.view, o.lon, o.lat);
        var rad = (o.type === 'label' ? Math.max(18, o.size) : o.type === 'battle' ? 22 : 15) * m;
        if (P.dist(sx, sy, q[0], q[1]) < rad) return o;
      }
    }
    return null;
  }

  function hitVertex(obj, sx, sy) {
    if (!obj || !obj.pts) return -1;
    var p = stagePts(obj);
    for (var i = 0; i < p.length; i++) if (P.dist(sx, sy, p[i][0], p[i][1]) < 9) return i;
    return -1;
  }

  /* ---------------- tools ---------------- */

  var TOOLS = [
    { id: 'select', key: 'V', name: 'Select', hint: 'Click to select. Drag to move. Drag empty space to pan, wheel to zoom.' },
    { id: 'settlement', key: 'S', name: 'Settlement', hint: 'Click to place a settlement. It stays in this tool so you can place several.' },
    { id: 'army', key: 'A', name: 'Army', hint: 'Click to place an army banner, then set its faction and unit type on the right.' },
    { id: 'battle', key: 'B', name: 'Battle', hint: 'Click to mark a battle. Give it a name and a date.' },
    { id: 'arrow', key: 'R', name: 'Arrow', hint: 'Click each waypoint, then Enter (or double-click) to finish. Backspace undoes a point, Esc cancels.' },
    { id: 'territory', key: 'T', name: 'Territory', hint: 'Click around the area, then Enter (or double-click) to close it.' },
    { id: 'label', key: 'L', name: 'Label', hint: 'Click to drop free text - a region name, a sea, a note.' }
  ];

  function hintFor(id) {
    for (var i = 0; i < TOOLS.length; i++) if (TOOLS[i].id === id) return TOOLS[i].hint;
    return '';
  }

  function setTool(id) {
    if (draft) cancelDraft();
    tool = id;
    $$('#tools button').forEach(function (b) {
      b.classList.toggle('active', b.dataset.tool === id);
    });
    canvas.style.cursor = id === 'select' ? 'default' : 'crosshair';
    status(hintFor(id), 'dim');
  }

  function cancelDraft() { draft = null; invalidate(); }

  function commitDraft() {
    if (!draft) return;
    var min = draft.kind === 'territory' ? 3 : 2;
    if (draft.pts.length >= min) {
      var o = draft.kind === 'territory'
        ? S.newTerritory(draft.pts, { step: store.scene.steps.current })
        : S.newArrow(draft.pts, { step: store.scene.steps.current });
      store.add(o);
      buildInspector();
    }
    draft = null;
    invalidate();
  }

  /* ---------------- pointer ---------------- */

  function onDown(ev) {
    if (ev.button === 1 || ev.altKey) {                 // middle or alt: pan
      drag = { mode: 'pan', x: ev.clientX, y: ev.clientY };
      return;
    }
    var s = toStageCoords(ev);
    var geo = P.toGeo(store.scene.view, s[0], s[1]);

    if (tool === 'arrow' || tool === 'territory') {
      if (!draft) draft = { kind: tool, pts: [], faction: store.scene.factions[0].id };
      draft.pts.push(geo);
      invalidate();
      return;
    }

    if (tool !== 'select') {
      var made;
      if (tool === 'settlement') made = S.newSettlement(geo[0], geo[1], { step: store.scene.steps.current });
      else if (tool === 'army') made = S.newArmy(geo[0], geo[1], { step: store.scene.steps.current });
      else if (tool === 'battle') made = S.newBattle(geo[0], geo[1], { step: store.scene.steps.current });
      else made = S.newLabel(geo[0], geo[1], { step: store.scene.steps.current });
      store.add(made);
      buildInspector();
      invalidate();
      return;
    }

    // select tool
    var sel = store.selected();
    var vi = hitVertex(sel, s[0], s[1]);
    if (vi >= 0) {
      store.checkpoint();
      drag = { mode: 'vertex', id: sel.id, index: vi };
      return;
    }
    var hit = hitTest(s[0], s[1]);
    if (hit) {
      store.selection = hit.id;
      store.checkpoint();
      drag = { mode: 'move', id: hit.id, last: geo };
      buildInspector();
      invalidate();
      return;
    }
    if (store.scene.underlay && store.scene.underlay.adjust) {
      store.checkpoint();
      drag = { mode: 'underlay', last: geo, scale: ev.shiftKey };
      return;
    }
    store.selection = null;
    buildInspector();
    drag = { mode: 'pan', x: ev.clientX, y: ev.clientY };
    invalidate();
  }

  function onMove(ev) {
    var s = toStageCoords(ev);
    if (draft) { draft.hover = s; invalidate(); }

    if (!drag) return;
    if (drag.mode === 'pan') {
      var r = canvas.getBoundingClientRect();
      var f = P.STAGE_W / r.width;
      P.panBy(store.scene.view, (ev.clientX - drag.x) * f, (ev.clientY - drag.y) * f);
      drag.x = ev.clientX; drag.y = ev.clientY;
      invalidate();
      return;
    }
    var geo = P.toGeo(store.scene.view, s[0], s[1]);
    var o = drag.id ? store.get(drag.id) : null;
    if (drag.mode === 'vertex' && o) {
      o.pts[drag.index] = geo;
      invalidate();
    } else if (drag.mode === 'move' && o) {
      var dlon = geo[0] - drag.last[0], dlat = geo[1] - drag.last[1];
      if (o.pts) o.pts = o.pts.map(function (p) { return [p[0] + dlon, p[1] + dlat]; });
      else { o.lon += dlon; o.lat += dlat; }
      drag.last = geo;
      invalidate();
    } else if (drag.mode === 'underlay') {
      var u = store.scene.underlay;
      var dl = geo[0] - drag.last[0], da = geo[1] - drag.last[1];
      if (drag.scale) {
        u.lon1 += dl * 2; u.lat0 -= da * 2;
      } else {
        u.lon0 += dl; u.lon1 += dl; u.lat0 += da; u.lat1 += da;
      }
      drag.last = geo;
      invalidate();
    }
  }

  function onUp() {
    if (drag && drag.mode !== 'pan') { store.dirty = true; scheduleAutosave(); }
    drag = null;
  }

  function onWheel(ev) {
    ev.preventDefault();
    var s = toStageCoords(ev);
    P.zoomAt(store.scene.view, ev.deltaY < 0 ? 1.12 : 1 / 1.12, s[0], s[1]);
    invalidate();
  }

  function onDouble(ev) {
    if (draft) { ev.preventDefault(); commitDraft(); }
  }

  /* ---------------- panels ---------------- */

  function row(label, control) {
    return el('label', { class: 'row' }, [el('span', { text: label }), control]);
  }

  function textInput(value, oninput, opts) {
    var a = Object.assign({ type: 'text', value: value === undefined ? '' : value }, opts || {});
    var i = el('input', a);
    i.addEventListener('input', function () { oninput(i.value); });
    return i;
  }

  function urduInput(value, oninput) {
    var i = textInput(value, oninput, { dir: 'rtl', class: 'urdu', placeholder: 'اردو' });
    return i;
  }

  function selectInput(options, value, onchange, labels) {
    var s = el('select');
    options.forEach(function (o, idx) {
      s.appendChild(el('option', { value: o, text: labels ? labels[idx] : o, selected: o === value ? '' : null }));
    });
    s.addEventListener('change', function () { onchange(s.value); });
    s.value = value;
    return s;
  }

  function change(fn) {
    return function (v) {
      store.checkpoint();
      fn(v);
      invalidate();
      scheduleAutosave();
    };
  }

  function buildInspector() {
    var box = $('#inspector');
    box.innerHTML = '';
    var o = store.selected();
    box.appendChild(el('h3', { text: o ? 'Selected — ' + o.type : 'Nothing selected' }));
    if (!o) {
      box.appendChild(el('p', { class: 'muted', text: 'Pick a tool on the left and click the map, or click something already placed.' }));
      return;
    }

    var factionIds = store.scene.factions.map(function (f) { return f.id; });
    var factionNames = store.scene.factions.map(function (f) { return f.name; });

    if (o.type === 'label') {
      box.appendChild(row('Text', textInput(o.text, change(function (v) { o.text = v; }))));
    } else if (o.type === 'arrow' || o.type === 'territory') {
      box.appendChild(row('Label', textInput(o.label, change(function (v) { o.label = v; }))));
    } else {
      box.appendChild(row('Name', textInput(o.name, change(function (v) { o.name = v; }))));
    }
    box.appendChild(row('Urdu', urduInput(o.ur, change(function (v) { o.ur = v; }))));

    if (o.type === 'settlement') {
      box.appendChild(row('Kind', selectInput(S.TIERS, o.tier, change(function (v) { o.tier = v; }))));
    }
    if (o.type === 'army') {
      box.appendChild(row('Faction', selectInput(factionIds, o.faction, change(function (v) { o.faction = v; }), factionNames)));
      box.appendChild(row('Unit', selectInput(S.UNITS, o.unit, change(function (v) { o.unit = v; }))));
      box.appendChild(row('Strength', textInput(o.strength, change(function (v) { o.strength = v; }), { placeholder: 'e.g. 4,000' })));
    }
    if (o.type === 'battle') {
      box.appendChild(row('Date', textInput(o.date, change(function (v) { o.date = v; }), { placeholder: 'e.g. 12 AH / 633 CE' })));
    }
    if (o.type === 'arrow') {
      box.appendChild(row('Faction', selectInput(factionIds, o.faction, change(function (v) { o.faction = v; }), factionNames)));
      box.appendChild(row('Width', rangeInput(6, 30, 1, o.width, change(function (v) { o.width = +v; }))));
      box.appendChild(row('Dashed', checkInput(o.dashed, change(function (v) { o.dashed = v; }))));
    }
    if (o.type === 'territory') {
      box.appendChild(row('Faction', selectInput(factionIds, o.faction, change(function (v) { o.faction = v; }), factionNames)));
      box.appendChild(row('Opacity', rangeInput(0.05, 0.6, 0.01, o.opacity, change(function (v) { o.opacity = +v; }))));
    }
    if (o.type === 'label') {
      box.appendChild(row('Size', rangeInput(14, 60, 1, o.size, change(function (v) { o.size = +v; }))));
      box.appendChild(row('Align', selectInput(['center', 'left', 'right'], o.align, change(function (v) { o.align = v; }))));
    }
    if (o.labelPos !== undefined) {
      box.appendChild(row('Label side', selectInput(S.LABEL_POS, o.labelPos, change(function (v) { o.labelPos = v; }))));
    }
    if (o.type !== 'territory') {
      box.appendChild(row('Size', rangeInput(0.5, 3, 0.05, o.scale === undefined ? 1 : o.scale,
        change(function (v) { o.scale = +v; }))));
    }
    box.appendChild(row('Step', numberInput(1, 40, o.step, change(function (v) {
      o.step = Math.max(1, +v || 1);
      store.scene.steps.count = store.maxStep();
      buildSteps();
    }))));

    box.appendChild(el('div', { class: 'btnrow' }, [
      el('button', { text: 'Bring forward', onclick: function () { store.raise(o.id); } }),
      el('button', { text: 'Send back', onclick: function () { store.lower(o.id); } }),
      el('button', {
        class: 'danger', text: 'Delete', onclick: function () {
          store.remove(o.id); buildInspector(); invalidate(); scheduleAutosave();
        }
      })
    ]));
  }

  function rangeInput(min, max, step, value, oninput) {
    var i = el('input', { type: 'range', min: min, max: max, step: step, value: value });
    i.addEventListener('input', function () { oninput(i.value); });
    return i;
  }

  function numberInput(min, max, value, oninput) {
    var i = el('input', { type: 'number', min: min, max: max, value: value });
    i.addEventListener('input', function () { oninput(i.value); });
    return i;
  }

  function checkInput(value, onchange) {
    var i = el('input', { type: 'checkbox', checked: value ? '' : null });
    i.addEventListener('change', function () { onchange(i.checked); });
    return i;
  }

  function buildSteps() {
    var box = $('#steps');
    box.innerHTML = '';
    var st = store.scene.steps;
    var max = store.maxStep();
    box.appendChild(el('h3', { text: 'Steps' }));
    box.appendChild(el('p', { class: 'muted', text: 'Give each object a step number, then export one PNG per step to build the map up across consecutive slides.' }));
    var readout = el('strong', { text: 'Step ' + st.current + ' of ' + max });
    box.appendChild(el('div', { class: 'btnrow' }, [
      el('button', { text: '‹ Prev', onclick: function () { st.current = Math.max(1, st.current - 1); buildSteps(); invalidate(); } }),
      readout,
      el('button', { text: 'Next ›', onclick: function () { st.current = Math.min(Math.max(max, st.count), st.current + 1); st.count = Math.max(st.count, st.current); buildSteps(); invalidate(); } })
    ]));
    box.appendChild(row('Show', selectInput(['upto', 'only'], st.mode, function (v) {
      st.mode = v; invalidate();
    }, ['everything up to this step', 'only this step'])));
  }

  function buildFactions() {
    var box = $('#factions');
    box.innerHTML = '';
    box.appendChild(el('h3', { text: 'Factions' }));
    store.scene.factions.forEach(function (f, idx) {
      var color = el('input', { type: 'color', value: f.color });
      color.addEventListener('input', function () { f.color = color.value; invalidate(); scheduleAutosave(); });
      var name = el('input', { type: 'text', value: f.name });
      name.addEventListener('input', function () { f.name = name.value; invalidate(); buildInspector(); scheduleAutosave(); });
      var del = el('button', {
        class: 'mini danger', text: '×', title: 'Remove faction', onclick: function () {
          if (store.scene.factions.length <= 1) return;
          store.checkpoint();
          store.scene.factions.splice(idx, 1);
          buildFactions(); buildInspector(); invalidate();
        }
      });
      box.appendChild(el('div', { class: 'faction' }, [color, name, del]));
    });
    box.appendChild(el('button', {
      class: 'wide', text: '+ Add faction', onclick: function () {
        store.checkpoint();
        store.scene.factions.push({ id: S.uid('f'), name: 'New faction', ur: '', color: '#8C6BB1' });
        buildFactions(); buildInspector();
      }
    }));
  }

  function buildGazetteer() {
    var box = $('#gazetteer');
    box.innerHTML = '';
    box.appendChild(el('h3', { text: 'Places' }));
    var results = el('div', { class: 'results' });
    var search = el('input', { type: 'search', placeholder: 'Search 120 places…' });

    function draw() {
      var q = search.value.trim().toLowerCase();
      results.innerHTML = '';
      var list = (global.MS_PLACES || []).filter(function (p) {
        return !q || p.en.toLowerCase().indexOf(q) >= 0 || p.ur.indexOf(search.value.trim()) >= 0;
      }).slice(0, q ? 40 : 14);
      list.forEach(function (p) {
        var b = el('button', { class: 'place' }, [
          el('span', { text: p.en }),
          el('span', { class: 'urdu', dir: 'rtl', text: p.ur })
        ]);
        if (p.approx) b.appendChild(el('em', { text: 'site approximate' }));
        b.addEventListener('click', function () {
          var made;
          if (tool === 'army') made = S.newArmy(p.lon, p.lat, { step: store.scene.steps.current });
          else if (tool === 'battle') made = S.newBattle(p.lon, p.lat, { name: p.en, ur: p.ur, step: store.scene.steps.current });
          else made = S.newSettlement(p.lon, p.lat, { name: p.en, ur: p.ur, tier: p.tier, step: store.scene.steps.current });
          store.add(made);
          buildInspector();
          invalidate();
          status('Placed ' + p.en + (p.approx ? ' — site approximate, check before you present it.' : ''), p.approx ? 'warn' : '');
        });
        results.appendChild(b);
      });
      if (!list.length) results.appendChild(el('p', { class: 'muted', text: 'No match.' }));
    }
    search.addEventListener('input', draw);
    box.appendChild(search);
    box.appendChild(results);
    box.appendChild(el('p', { class: 'muted small', text: 'Coordinates are for placement only, not a claim about a site. Entries marked "site approximate" are genuinely disputed.' }));
    draw();
  }

  function buildStyle() {
    var box = $('#stylepanel');
    box.innerHTML = '';
    box.appendChild(el('h3', { text: 'Look' }));
    var st = store.scene.style;

    /* One slider that lifts every mark and label together. A map of the whole
     * caliphate needs bigger marks than a map of Najd to stay legible from the
     * back of a hall, and this is that dial. */
    if (st.markScale === undefined) st.markScale = 1;
    box.appendChild(row('Mark size', rangeInput(0.5, 3, 0.05, st.markScale, function (v) {
      st.markScale = +v; invalidate(); scheduleAutosave();
    })));
    if (st.cartoucheScale === undefined) st.cartoucheScale = 1;
    box.appendChild(row('Cartouche size', rangeInput(0.6, 2.2, 0.05, st.cartoucheScale, function (v) {
      st.cartoucheScale = +v; invalidate(); scheduleAutosave();
    })));
    if (st.reliefStrength === undefined) st.reliefStrength = 0.85;
    box.appendChild(row('Relief strength', rangeInput(0, 1, 0.05, st.reliefStrength, function (v) {
      st.reliefStrength = +v; invalidate(); scheduleAutosave();
    })));
    [
      ['relief', 'Shaded relief'],
      ['rivers', 'Rivers and lakes'],
      ['baseMap', 'Draw the base map'],
      ['graticule', 'Graticule'],
      ['grain', 'Paper grain'],
      ['vignette', 'Vignette'],
      ['cartouche', 'Title cartouche'],
      ['legend', 'Legend'],
      ['scalebar', 'Scale bar and north'],
      ['urduLabels', 'Show Urdu labels']
    ].forEach(function (pair) {
      if (st[pair[0]] === undefined) st[pair[0]] = true;
      box.appendChild(row(pair[1], checkInput(st[pair[0]], function (v) { st[pair[0]] = v; invalidate(); scheduleAutosave(); })));
    });

    box.appendChild(el('h3', { text: 'Underlay' }));
    box.appendChild(el('p', { class: 'muted small', text: 'Drop an image on the map to trace over it — a downloaded map, or a frame grabbed with tools/grab_frame.py. Hide it before exporting.' }));
    var u = store.scene.underlay;
    if (!u) {
      box.appendChild(el('p', { class: 'muted', text: 'No underlay loaded.' }));
    } else {
      box.appendChild(row('Visible', checkInput(u.visible, function (v) { u.visible = v; invalidate(); })));
      box.appendChild(row('Opacity', rangeInput(0.05, 1, 0.05, u.opacity, function (v) { u.opacity = +v; invalidate(); })));
      box.appendChild(row('Move / scale it', checkInput(u.adjust, function (v) { u.adjust = v; status(v ? 'Drag the map to move the underlay; hold Shift while dragging to scale it.' : hintFor(tool)); })));
      box.appendChild(el('div', { class: 'btnrow' }, [
        el('button', { text: 'Fit to view', onclick: function () { fitUnderlayToView(); } }),
        el('button', { class: 'danger', text: 'Remove', onclick: function () { store.checkpoint(); store.scene.underlay = null; buildStyle(); invalidate(); } })
      ]));
    }
  }

  function fitUnderlayToView() {
    var u = store.scene.underlay;
    if (!u) return;
    var nw = P.toGeo(store.scene.view, P.STAGE_W * 0.08, P.STAGE_H * 0.08);
    var se = P.toGeo(store.scene.view, P.STAGE_W * 0.92, P.STAGE_H * 0.92);
    u.lon0 = nw[0]; u.lat1 = nw[1]; u.lon1 = se[0]; u.lat0 = se[1];
    invalidate();
  }

  function buildLayers() {
    var box = $('#layers');
    box.innerHTML = '';
    var objs = store.scene.objects;
    box.appendChild(el('h3', { text: 'Objects (' + objs.length + ')' }));
    if (!objs.length) {
      box.appendChild(el('p', { class: 'muted', text: 'Nothing placed yet.' }));
      return;
    }
    var list = el('div', { class: 'layerlist' });
    objs.slice().reverse().forEach(function (o) {
      var name = o.name || o.text || o.label || '(' + o.type + ')';
      var b = el('button', {
        class: 'layer' + (store.selection === o.id ? ' on' : ''),
        onclick: function () { store.selection = o.id; buildInspector(); buildLayers(); invalidate(); }
      }, [
        el('span', { class: 'tag tag-' + o.type, text: o.type[0].toUpperCase() }),
        el('span', { class: 'nm', text: name }),
        el('span', { class: 'st', text: 'step ' + (o.step || 1) })
      ]);
      list.appendChild(b);
    });
    box.appendChild(list);
  }

  function buildRegions() {
    var sel = $('#region');
    sel.innerHTML = '';
    sel.appendChild(el('option', { value: '', text: 'Jump to region…' }));
    P.REGIONS.forEach(function (r) { sel.appendChild(el('option', { value: r.id, text: r.name })); });
    sel.addEventListener('change', function () {
      var r = P.REGIONS.filter(function (x) { return x.id === sel.value; })[0];
      if (r) { P.fitBBox(store.scene.view, r.bbox); invalidate(); }
      sel.value = '';
    });
  }

  function refreshAll() {
    $('#title').value = store.scene.meta.title || '';
    $('#subtitle').value = store.scene.meta.subtitle || '';
    $('#urdutitle').value = store.scene.meta.urduTitle || '';
    buildInspector(); buildSteps(); buildFactions(); buildStyle(); buildLayers();
    loadUnderlayImage();
    invalidate();
  }

  /* ---------------- files ---------------- */

  function safeName() {
    var t = (store.scene.meta.title || 'map').toLowerCase()
      .replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');
    return t || 'map';
  }

  function download(blob, filename) {
    var url = URL.createObjectURL(blob);
    var a = el('a', { href: url, download: filename });
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    setTimeout(function () { URL.revokeObjectURL(url); }, 4000);
  }

  function saveScene() {
    download(new Blob([store.toJSON()], { type: 'application/json' }), safeName() + '.json');
    store.dirty = false;
    status('Saved. Move it into tools/mapstudio/scenes/ to keep it with the project.');
  }

  function openSceneFile(file) {
    var fr = new FileReader();
    fr.onload = function () {
      try {
        store.load(fr.result);
        refreshAll();
        status('Opened ' + file.name);
      } catch (e) {
        status('Could not open that file: ' + e.message, 'warn');
      }
    };
    fr.readAsText(file);
  }

  function loadUnderlayImage() {
    var u = store.scene.underlay;
    if (!u || images[u.src]) return;
    var img = new Image();
    img.onload = invalidate;
    img.src = u.src;
    images[u.src] = img;
  }

  function addUnderlay(file) {
    var fr = new FileReader();
    fr.onload = function () {
      store.checkpoint();
      var src = fr.result;
      var img = new Image();
      img.onload = function () {
        images[src] = img;
        // Fit the image into the current view, preserving its own aspect ratio.
        var nw = P.toGeo(store.scene.view, P.STAGE_W * 0.08, P.STAGE_H * 0.08);
        var se = P.toGeo(store.scene.view, P.STAGE_W * 0.92, P.STAGE_H * 0.92);
        var boxW = se[0] - nw[0], boxH = nw[1] - se[1];
        var ar = img.naturalWidth / img.naturalHeight;
        var w = boxW, h = boxW / ar / P.K;
        if (h > boxH) { h = boxH; w = boxH * ar * P.K; }
        var cx = (nw[0] + se[0]) / 2, cy = (nw[1] + se[1]) / 2;
        store.scene.underlay = {
          src: src, opacity: 0.72, visible: true, adjust: true,
          lon0: cx - w / 2, lon1: cx + w / 2, lat0: cy - h / 2, lat1: cy + h / 2
        };
        buildStyle();
        invalidate();
        status('Underlay placed. Drag to move it, Shift+drag to scale, then untick "Move / scale it".');
      };
      images[src] = img;
      img.src = src;
    };
    fr.readAsDataURL(file);
  }

  /* ---------------- export ---------------- */

  function renderToBlob(scale) {
    return R.whenReady().then(function () { return rasterise(scale); });
  }

  function rasterise(scale) {
    var c = document.createElement('canvas');
    c.width = Math.round(P.STAGE_W * scale);
    c.height = Math.round(P.STAGE_H * scale);
    var cx = c.getContext('2d');
    R.render(cx, store, { k: scale, showSelection: false, images: images });
    return new Promise(function (resolve) { c.toBlob(resolve, 'image/png'); });
  }

  function exportPNG() {
    var scale = +$('#exportscale').value;
    status('Rendering ' + Math.round(P.STAGE_W * scale) + '×' + Math.round(P.STAGE_H * scale) + '…');
    renderToBlob(scale).then(function (blob) {
      download(blob, safeName() + '.png');
      status('Exported ' + safeName() + '.png');
    });
  }

  function exportSteps() {
    var scale = +$('#exportscale').value;
    var max = store.maxStep();
    var keep = store.scene.steps.current;
    var i = 1;
    status('Exporting ' + max + ' steps…');
    function next() {
      if (i > max) {
        store.scene.steps.current = keep;
        buildSteps();
        invalidate();
        status('Exported ' + max + ' step images. Chrome may have asked once to allow multiple downloads.');
        return;
      }
      store.scene.steps.current = i;
      renderToBlob(scale).then(function (blob) {
        download(blob, safeName() + '-step-' + String(i).padStart(2, '0') + '.png');
        i += 1;
        setTimeout(next, 350);
      });
    }
    next();
  }

  /* ---------------- autosave ---------------- */

  var autosaveTimer = null;
  function scheduleAutosave() {
    clearTimeout(autosaveTimer);
    autosaveTimer = setTimeout(function () { store.autosave(); }, 900);
  }

  /* ---------------- keyboard ---------------- */

  function onKey(ev) {
    var t = ev.target.tagName;
    if (t === 'INPUT' || t === 'TEXTAREA' || t === 'SELECT') return;
    var k = ev.key;

    if ((ev.ctrlKey || ev.metaKey) && k.toLowerCase() === 'z') {
      ev.preventDefault();
      if (ev.shiftKey) store.redo(); else store.undo();
      refreshAll();
      return;
    }
    if ((ev.ctrlKey || ev.metaKey) && k.toLowerCase() === 's') { ev.preventDefault(); saveScene(); return; }
    if ((ev.ctrlKey || ev.metaKey) && k.toLowerCase() === 'e') { ev.preventDefault(); exportPNG(); return; }
    if (ev.ctrlKey || ev.metaKey) return;

    if (k === 'Escape') { cancelDraft(); store.selection = null; buildInspector(); invalidate(); return; }
    if (k === 'Enter') { commitDraft(); return; }
    if (k === 'Backspace' && draft) { draft.pts.pop(); invalidate(); return; }
    if ((k === 'Delete' || k === 'Backspace') && store.selection) {
      store.remove(store.selection); buildInspector(); buildLayers(); invalidate(); return;
    }
    if (k === '[') { var st = store.scene.steps; st.current = Math.max(1, st.current - 1); buildSteps(); invalidate(); return; }
    if (k === ']') { var s2 = store.scene.steps; s2.current = Math.min(store.maxStep(), s2.current + 1); buildSteps(); invalidate(); return; }

    for (var i = 0; i < TOOLS.length; i++) {
      if (TOOLS[i].key.toLowerCase() === k.toLowerCase()) { setTool(TOOLS[i].id); return; }
    }
  }

  /* ---------------- boot ---------------- */

  function buildToolRail() {
    var rail = $('#tools');
    TOOLS.forEach(function (t) {
      var b = el('button', { 'data-tool': t.id, title: t.name + '  (' + t.key + ')' }, [
        el('span', { class: 'ico ico-' + t.id }),
        el('span', { class: 'lbl', text: t.name }),
        el('span', { class: 'key', text: t.key })
      ]);
      b.addEventListener('click', function () { setTool(t.id); });
      rail.appendChild(b);
    });
  }

  function wireTopBar() {
    $('#title').addEventListener('input', function () { store.scene.meta.title = this.value; invalidate(); scheduleAutosave(); });
    $('#subtitle').addEventListener('input', function () { store.scene.meta.subtitle = this.value; invalidate(); scheduleAutosave(); });
    $('#urdutitle').addEventListener('input', function () { store.scene.meta.urduTitle = this.value; invalidate(); scheduleAutosave(); });
    $('#btn-save').addEventListener('click', saveScene);
    $('#btn-export').addEventListener('click', exportPNG);
    $('#btn-export-steps').addEventListener('click', exportSteps);
    $('#btn-new').addEventListener('click', function () {
      if (store.scene.objects.length && !confirm('Start a new map? Anything unsaved is lost.')) return;
      store.load(JSON.stringify(S.blankScene()));
      refreshAll();
      status('New map.');
    });
    $('#file-open').addEventListener('change', function () {
      if (this.files[0]) openSceneFile(this.files[0]);
      this.value = '';
    });
    $('#file-underlay').addEventListener('change', function () {
      if (this.files[0]) addUnderlay(this.files[0]);
      this.value = '';
    });
  }

  function wireDrop() {
    ['dragenter', 'dragover'].forEach(function (e) {
      document.addEventListener(e, function (ev) { ev.preventDefault(); $('#stagewrap').classList.add('dropping'); });
    });
    ['dragleave', 'drop'].forEach(function (e) {
      document.addEventListener(e, function (ev) { ev.preventDefault(); $('#stagewrap').classList.remove('dropping'); });
    });
    document.addEventListener('drop', function (ev) {
      var f = ev.dataTransfer.files[0];
      if (!f) return;
      if (/\.json$/i.test(f.name)) openSceneFile(f);
      else if (/^image\//.test(f.type)) addUnderlay(f);
      else status('Drop a .json scene or an image to trace over.', 'warn');
    });
  }

  function start() {
    canvas = $('#stage');
    ctx = canvas.getContext('2d');
    buildToolRail();
    buildRegions();
    wireTopBar();
    wireDrop();

    canvas.addEventListener('mousedown', onDown);
    global.addEventListener('mousemove', onMove);
    global.addEventListener('mouseup', onUp);
    canvas.addEventListener('wheel', onWheel, { passive: false });
    canvas.addEventListener('dblclick', onDouble);
    canvas.addEventListener('contextmenu', function (ev) {
      if (draft) { ev.preventDefault(); draft.pts.pop(); invalidate(); }
    });
    global.MS_onTerrainLoad = invalidate;
    global.addEventListener('keydown', onKey);
    global.addEventListener('resize', invalidate);
    global.addEventListener('beforeunload', function (ev) {
      if (store.dirty) { ev.preventDefault(); ev.returnValue = ''; }
    });

    store.on(function () { buildLayers(); scheduleAutosave(); });

    /* URL parameters exist so a screenshot can be scripted:
     *   ?demo=1&region=caliphate&mark=1.6&step=3   */
    var params = new URLSearchParams(global.location.search);
    if (params.get('demo') && global.MS_Demo) {
      store.load(JSON.stringify(MS_Demo.scene()));
    }
    if (params.get('region')) {
      var reg = P.REGIONS.filter(function (r) { return r.id === params.get('region'); })[0];
      if (reg) P.fitBBox(store.scene.view, reg.bbox);
    }
    if (params.get('mark')) store.scene.style.markScale = parseFloat(params.get('mark'));
    if (params.get('step')) store.scene.steps.current = parseInt(params.get('step'), 10) || 1;
    if (!params.get('demo') && store.restoreAutosave()) {
      status('Restored your last session. Use New to start clean.');
    }

    sizeCanvas();
    refreshAll();
    setTool('select');
    frame();

    // Nastaliq metrics differ enough that a pre-font render looks wrong; redraw once ready.
    if (document.fonts && document.fonts.ready) {
      document.fonts.load('16px "Noto Nastaliq Urdu"').catch(function () { });
      document.fonts.ready.then(function () { invalidate(); document.body.classList.add('fonts-ready'); });
    } else {
      document.body.classList.add('fonts-ready');
    }
  }

  global.MS_UI = { start: start, store: function () { return store; } };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})(window);
