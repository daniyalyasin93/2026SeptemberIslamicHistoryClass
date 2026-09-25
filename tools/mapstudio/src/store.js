/* store.js — the scene, its history, and reading/writing it to disk.
 *
 * A scene is plain JSON: no functions, no cycles, no ids that mean anything outside
 * the file. That is deliberate — scenes live in tools/mapstudio/scenes/, get diffed
 * in git, and can be hand-edited when it is faster than clicking.
 */
(function (global) {
  'use strict';

  var SCHEMA = 1;
  var AUTOSAVE_KEY = 'mapstudio.autosave.v1';

  /* Seeded from the course palette so exports sit beside the decks without a clash. */
  var DEFAULT_FACTIONS = [
    { id: 'f1', name: 'Muslim forces',     ur: 'مسلم افواج',   color: '#22B694' },
    { id: 'f2', name: 'Byzantine Rome',    ur: 'روم',          color: '#DC5844' },
    { id: 'f3', name: 'Sasanian Persia',   ur: 'فارس',         color: '#9877D6' },
    { id: 'f4', name: 'Opposing tribes',   ur: 'مخالف قبائل',  color: '#E7A244' },
    { id: 'f5', name: 'Neutral / other',   ur: 'دیگر',         color: '#8FA6AF' }
  ];

  var TIERS = ['capital', 'city', 'town', 'fort'];
  var UNITS = ['mixed', 'infantry', 'cavalry', 'archer', 'naval'];
  var LABEL_POS = ['right', 'left', 'above', 'below'];

  var seq = 0;
  function uid(prefix) {
    seq += 1;
    return prefix + '_' + seq.toString(36) + '_' + (seq * 2654435761 % 100000).toString(36);
  }

  function blankScene() {
    return {
      schema: SCHEMA,
      meta: { title: 'Untitled map', subtitle: '', note: '', urduTitle: '' },
      view: MS_Proj.makeView(),
      factions: JSON.parse(JSON.stringify(DEFAULT_FACTIONS)),
      objects: [],
      underlay: null,
      style: {
        relief: true,
        reliefStrength: 0.85,
        rivers: true,
        markScale: 1,
        cartoucheScale: 1,
        graticule: true,
        grain: true,
        vignette: true,
        cartouche: true,
        legend: true,
        scalebar: true,
        urduLabels: true,
        aspect: '16:9'
      },
      steps: { count: 1, current: 1, mode: 'upto' }   // 'upto' | 'only'
    };
  }

  /* ---- object factories. Every object carries `step` and an id. ---- */

  function newSettlement(lon, lat, o) {
    o = o || {};
    return {
      id: uid('s'), type: 'settlement', lon: lon, lat: lat,
      name: o.name || 'New place', ur: o.ur || '', tier: o.tier || 'city',
      labelPos: o.labelPos || 'right', step: o.step || 1, note: ''
    };
  }

  function newArmy(lon, lat, o) {
    o = o || {};
    return {
      id: uid('a'), type: 'army', lon: lon, lat: lat,
      name: o.name || 'Commander', ur: o.ur || '', faction: o.faction || 'f1',
      strength: o.strength || '', unit: o.unit || 'mixed',
      labelPos: o.labelPos || 'right', step: o.step || 1, note: ''
    };
  }

  function newBattle(lon, lat, o) {
    o = o || {};
    return {
      id: uid('b'), type: 'battle', lon: lon, lat: lat,
      name: o.name || 'Battle', ur: o.ur || '', date: o.date || '',
      labelPos: o.labelPos || 'below', step: o.step || 1, note: ''
    };
  }

  function newArrow(pts, o) {
    o = o || {};
    return {
      id: uid('r'), type: 'arrow', pts: pts,
      faction: o.faction || 'f1', label: o.label || '', ur: o.ur || '',
      dashed: !!o.dashed, width: o.width || 14, step: o.step || 1
    };
  }

  function newTerritory(pts, o) {
    o = o || {};
    return {
      id: uid('t'), type: 'territory', pts: pts,
      faction: o.faction || 'f1', label: o.label || '', ur: o.ur || '',
      opacity: o.opacity === undefined ? 0.22 : o.opacity, step: o.step || 1
    };
  }

  function newLabel(lon, lat, o) {
    o = o || {};
    return {
      id: uid('l'), type: 'label', lon: lon, lat: lat,
      text: o.text || 'Label', ur: o.ur || '', size: o.size || 26,
      align: o.align || 'center', step: o.step || 1
    };
  }

  /* ---- the store ---- */

  function Store() {
    this.scene = blankScene();
    this.selection = null;
    this.past = [];
    this.future = [];
    this.listeners = [];
    this.dirty = false;
  }

  Store.prototype.on = function (fn) { this.listeners.push(fn); };

  Store.prototype.emit = function (what) {
    for (var i = 0; i < this.listeners.length; i++) this.listeners[i](what, this);
  };

  /* Call BEFORE a mutation. Snapshots are cheap next to a lost afternoon. */
  Store.prototype.checkpoint = function () {
    this.past.push(JSON.stringify(this.scene));
    if (this.past.length > 80) this.past.shift();
    this.future.length = 0;
    this.dirty = true;
  };

  Store.prototype.undo = function () {
    if (!this.past.length) return false;
    this.future.push(JSON.stringify(this.scene));
    this.scene = JSON.parse(this.past.pop());
    this.selection = null;
    this.emit('scene');
    return true;
  };

  Store.prototype.redo = function () {
    if (!this.future.length) return false;
    this.past.push(JSON.stringify(this.scene));
    this.scene = JSON.parse(this.future.pop());
    this.selection = null;
    this.emit('scene');
    return true;
  };

  Store.prototype.add = function (obj) {
    this.checkpoint();
    this.scene.objects.push(obj);
    this.scene.steps.count = Math.max(this.scene.steps.count, obj.step || 1);
    this.selection = obj.id;
    this.emit('scene');
    return obj;
  };

  Store.prototype.remove = function (id) {
    var i = this.indexOf(id);
    if (i < 0) return;
    this.checkpoint();
    this.scene.objects.splice(i, 1);
    if (this.selection === id) this.selection = null;
    this.emit('scene');
  };

  Store.prototype.indexOf = function (id) {
    for (var i = 0; i < this.scene.objects.length; i++) {
      if (this.scene.objects[i].id === id) return i;
    }
    return -1;
  };

  Store.prototype.get = function (id) {
    var i = this.indexOf(id);
    return i < 0 ? null : this.scene.objects[i];
  };

  Store.prototype.selected = function () {
    return this.selection ? this.get(this.selection) : null;
  };

  Store.prototype.faction = function (id) {
    var f = this.scene.factions;
    for (var i = 0; i < f.length; i++) if (f[i].id === id) return f[i];
    return f[f.length - 1] || { id: 'f0', name: '', color: '#888888' };
  };

  Store.prototype.raise = function (id) {
    var i = this.indexOf(id);
    if (i < 0 || i === this.scene.objects.length - 1) return;
    this.checkpoint();
    var o = this.scene.objects.splice(i, 1)[0];
    this.scene.objects.push(o);
    this.emit('scene');
  };

  Store.prototype.lower = function (id) {
    var i = this.indexOf(id);
    if (i <= 0) return;
    this.checkpoint();
    var o = this.scene.objects.splice(i, 1)[0];
    this.scene.objects.unshift(o);
    this.emit('scene');
  };

  /* Which objects are painted at the current step setting. An object shows
   * from its `step` onwards; an optional `until` hides it after that step, so a
   * step-1 army can be gone by step 3 without being deleted from step 1. */
  Store.prototype.visibleObjects = function () {
    var st = this.scene.steps;
    return this.scene.objects.filter(function (o) {
      var s = o.step || 1;
      if (st.mode === 'only') return s === st.current;
      return s <= st.current && (!o.until || st.current <= o.until);
    });
  };

  Store.prototype.maxStep = function () {
    var m = 1;
    for (var i = 0; i < this.scene.objects.length; i++) {
      var o = this.scene.objects[i];
      m = Math.max(m, o.step || 1);
      // Something hidden after step N needs step N+1 to exist, or the hiding is never seen.
      if (o.until) m = Math.max(m, o.until + 1);
    }
    return Math.max(m, this.scene.steps.count || 1);
  };

  /* ---- persistence ---- */

  Store.prototype.toJSON = function () {
    return JSON.stringify(this.scene, null, 2);
  };

  Store.prototype.load = function (text) {
    var data = typeof text === 'string' ? JSON.parse(text) : text;
    if (!data || !data.objects) throw new Error('That file is not a map studio scene.');
    var fresh = blankScene();
    // Merge onto a blank scene so older files missing new fields still open.
    data.meta = Object.assign(fresh.meta, data.meta || {});
    data.style = Object.assign(fresh.style, data.style || {});
    data.steps = Object.assign(fresh.steps, data.steps || {});
    data.view = Object.assign(fresh.view, data.view || {});
    data.factions = data.factions && data.factions.length ? data.factions : fresh.factions;
    data.schema = SCHEMA;
    this.past.length = 0;
    this.future.length = 0;
    this.scene = data;
    this.selection = null;
    this.dirty = false;
    this.emit('scene');
  };

  Store.prototype.autosave = function () {
    try { global.localStorage.setItem(AUTOSAVE_KEY, this.toJSON()); } catch (e) { /* private mode */ }
  };

  Store.prototype.restoreAutosave = function () {
    try {
      var t = global.localStorage.getItem(AUTOSAVE_KEY);
      if (!t) return false;
      this.load(t);
      return true;
    } catch (e) { return false; }
  };

  global.MS_Store = {
    Store: Store, blankScene: blankScene, uid: uid,
    TIERS: TIERS, UNITS: UNITS, LABEL_POS: LABEL_POS, DEFAULT_FACTIONS: DEFAULT_FACTIONS,
    newSettlement: newSettlement, newArmy: newArmy, newBattle: newBattle,
    newArrow: newArrow, newTerritory: newTerritory, newLabel: newLabel
  };
})(window);
