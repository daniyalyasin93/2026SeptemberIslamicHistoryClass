/* render.js — one painter for both the screen stage and the PNG export.
 *
 * render(ctx, store, opts) draws the whole scene into a 1600x900 logical stage.
 * opts.k is applied as a single canvas transform rather than threaded through every
 * dimension, so line widths, fonts, shadows and the projection all agree and a 4x
 * export is the same drawing at a bigger transform.
 *
 * Paint order: sea, land, shaded relief, lakes and rivers, graticule, underlay,
 * territory, arrows, settlements, battles, armies, free labels, cartouche,
 * scale bar, grain, vignette.
 */
(function (global) {
  'use strict';

  var T = MS_Tokens;
  var P = MS_Proj;

  var SEA_DEEP = '#0B3242';
  var SEA_MID = '#155F76';
  var SEA_SHALLOW = '#2F97AC';
  var LAND_LO = '#9C8B58';
  var LAND_HI = '#C9B67C';
  var COAST = '#4A4128';
  var RIVER = 'rgba(96,180,208,0.72)';

  var grainTile = null;

  /* The relief is a data: URI in data/relief.js, not a file:// image. A file image
   * would taint the canvas and break toBlob(), which is how PNG export works. */
  var relief = null;
  var reliefReady = null;

  function initRelief() {
    if (relief || !global.MS_RELIEF) return;
    relief = new Image();
    reliefReady = new Promise(function (resolve) {
      relief.onload = function () {
        resolve(true);
        if (typeof global.MS_onTerrainLoad === 'function') global.MS_onTerrainLoad();
      };
      relief.onerror = function () { resolve(false); };
    });
    relief.src = global.MS_RELIEF.src;
  }

  function whenReady() {
    initRelief();
    return reliefReady || Promise.resolve(false);
  }

  /* Deterministic noise, so two exports of the same scene are identical. */
  function makeGrain() {
    var n = 140;
    var c = document.createElement('canvas');
    c.width = n; c.height = n;
    var g = c.getContext('2d');
    var img = g.createImageData(n, n);
    var seed = 20260903;
    for (var i = 0; i < n * n; i++) {
      seed = (seed * 1664525 + 1013904223) >>> 0;
      var v = 104 + ((seed >>> 24) % 48);   // narrow band: texture, not television static
      img.data[i * 4] = v;
      img.data[i * 4 + 1] = v;
      img.data[i * 4 + 2] = v;
      img.data[i * 4 + 3] = 255;
    }
    g.putImageData(img, 0, 0);
    return c;
  }

  function landPath(ctx, view, W, H) {
    var rings = (global.MS_LAND && MS_LAND.rings) || [];
    ctx.beginPath();
    for (var r = 0; r < rings.length; r++) {
      var flat = rings[r];
      var started = false;
      var minx = Infinity, maxx = -Infinity, miny = Infinity, maxy = -Infinity;
      var proj = new Array(flat.length / 2);
      for (var i = 0, j = 0; i < flat.length; i += 2, j++) {
        var p = P.toStage(view, flat[i], flat[i + 1]);
        proj[j] = p;
        if (p[0] < minx) minx = p[0];
        if (p[0] > maxx) maxx = p[0];
        if (p[1] < miny) miny = p[1];
        if (p[1] > maxy) maxy = p[1];
      }
      if (maxx < -40 || minx > W + 40 || maxy < -40 || miny > H + 40) continue;
      for (var m = 0; m < proj.length; m++) {
        if (!started) { ctx.moveTo(proj[m][0], proj[m][1]); started = true; }
        else ctx.lineTo(proj[m][0], proj[m][1]);
      }
      ctx.closePath();
    }
  }

  function drawBase(ctx, scene, W, H, k) {
    var view = scene.view;

    var sg = ctx.createLinearGradient(0, 0, 0, H);
    sg.addColorStop(0, SEA_DEEP);
    sg.addColorStop(0.55, SEA_MID);
    sg.addColorStop(1, '#0F4A5C');
    ctx.fillStyle = sg;
    ctx.fillRect(0, 0, W, H);

    var glow = ctx.createRadialGradient(W * 0.5, H * 0.42, 0, W * 0.5, H * 0.42, W * 0.62);
    glow.addColorStop(0, 'rgba(96,196,206,0.16)');
    glow.addColorStop(1, 'rgba(96,196,206,0)');
    ctx.fillStyle = glow;
    ctx.fillRect(0, 0, W, H);

    if (scene.style.baseMap === false) return;

    // coastal shelf: the land silhouette blurred outward reads as shallow water
    ctx.save();
    ctx.shadowColor = T.rgba(SEA_SHALLOW, 0.95);
    ctx.shadowBlur = 26 * k;
    ctx.fillStyle = 'rgba(0,0,0,1)';
    landPath(ctx, view, W, H);
    ctx.fill('evenodd');
    ctx.restore();

    // land body, with the relief modelled inside it
    ctx.save();
    landPath(ctx, view, W, H);
    var lg = ctx.createLinearGradient(0, 0, 0, H);
    lg.addColorStop(0, LAND_HI);
    lg.addColorStop(1, LAND_LO);
    ctx.fillStyle = lg;
    ctx.fill('evenodd');
    ctx.clip('evenodd');

    drawRelief(ctx, scene, W, H, k);

    ctx.save();
    ctx.translate(0, -3 * k);
    landPath(ctx, view, W, H);
    ctx.fillStyle = 'rgba(255,248,220,0.06)';
    ctx.fill('evenodd');
    ctx.restore();
    ctx.restore();

    drawWater(ctx, scene, W, H, k);

    // coastline last, so rivers reaching the sea are tidied by it
    ctx.save();
    landPath(ctx, view, W, H);
    ctx.strokeStyle = T.rgba(COAST, 0.85);
    ctx.lineWidth = 1.25 * k;
    ctx.lineJoin = 'round';
    ctx.stroke();
    ctx.strokeStyle = 'rgba(226,206,160,0.16)';
    ctx.lineWidth = 0.6 * k;
    ctx.stroke();
    ctx.restore();
  }

  /* Shaded relief over the flat land colour. The raster is centred on mid-grey at
   * build time, so 'overlay' leaves plains alone and only models ground that has
   * actual relief — mountains read as mountains, deserts stay flat. */
  function drawRelief(ctx, scene, W, H, k) {
    if (scene.style.relief === false) return;
    initRelief();
    if (!relief || !relief.complete || !relief.naturalWidth) return;
    var b = global.MS_RELIEF.bbox;
    var a = P.toStage(scene.view, b[0], b[3]);
    var c = P.toStage(scene.view, b[2], b[1]);
    ctx.save();
    ctx.globalCompositeOperation = 'overlay';
    ctx.globalAlpha = scene.style.reliefStrength === undefined ? 0.85 : scene.style.reliefStrength;
    ctx.imageSmoothingQuality = 'high';
    ctx.drawImage(relief, a[0], a[1], c[0] - a[0], c[1] - a[1]);
    ctx.restore();
  }

  function drawWater(ctx, scene, W, H, k) {
    if (scene.style.rivers === false || !global.MS_WATER) return;
    var view = scene.view;
    var w = MS_WATER;
    var i, j, p;

    // lakes read as sea, not as holes punched in the land
    ctx.save();
    for (var l = 0; l < w.lakes.length; l++) {
      var f = w.lakes[l];
      ctx.beginPath();
      for (i = 0; i < f.length; i += 2) {
        p = P.toStage(view, f[i], f[i + 1]);
        if (i === 0) ctx.moveTo(p[0], p[1]); else ctx.lineTo(p[0], p[1]);
      }
      ctx.closePath();
      ctx.fillStyle = T.rgba(SEA_MID, 0.92);
      ctx.fill();
      ctx.strokeStyle = 'rgba(120,200,224,0.5)';
      ctx.lineWidth = 0.8 * k;
      ctx.stroke();
    }
    ctx.restore();

    // rivers: heavier as you zoom in, and heavier for the bigger rivers
    var zoom = Math.max(0.45, Math.min(3.2, view.scale / 26));
    ctx.save();
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';
    ctx.strokeStyle = RIVER;
    for (var r = 0; r < w.rivers.length; r++) {
      var riv = w.rivers[r];
      var lw = zoom * Math.max(0.55, (9 - riv.r) * 0.26) * k;
      if (lw < 0.35) continue;
      ctx.lineWidth = lw;
      ctx.beginPath();
      var pts = riv.p;
      for (j = 0; j < pts.length; j += 2) {
        var q = P.toStage(view, pts[j], pts[j + 1]);
        if (j === 0) ctx.moveTo(q[0], q[1]); else ctx.lineTo(q[0], q[1]);
      }
      ctx.stroke();
    }
    ctx.restore();
  }

  function drawGraticule(ctx, scene, W, H, k) {
    if (!scene.style.graticule) return;
    var view = scene.view;
    var nw = P.toGeo(view, 0, 0);
    var se = P.toGeo(view, W, H);
    var steps = [1, 2, 5, 10, 20];
    var step = 20;
    for (var s = 0; s < steps.length; s++) {
      if (steps[s] * view.scale >= 88) { step = steps[s]; break; }
    }
    ctx.save();
    ctx.strokeStyle = 'rgba(226,206,160,0.085)';
    ctx.lineWidth = 0.9 * k;
    ctx.beginPath();
    var lon0 = Math.floor(nw[0] / step) * step;
    for (var lon = lon0; lon <= se[0] + step; lon += step) {
      var a = P.toStage(view, lon, nw[1]), b = P.toStage(view, lon, se[1]);
      ctx.moveTo(a[0], a[1]); ctx.lineTo(b[0], b[1]);
    }
    var lat0 = Math.floor(se[1] / step) * step;
    for (var lat = lat0; lat <= nw[1] + step; lat += step) {
      var c = P.toStage(view, nw[0], lat), d = P.toStage(view, se[0], lat);
      ctx.moveTo(c[0], c[1]); ctx.lineTo(d[0], d[1]);
    }
    ctx.stroke();
    ctx.restore();
  }

  function drawUnderlay(ctx, scene, W, H, k, images) {
    var u = scene.underlay;
    if (!u || !u.visible) return;
    var img = images[u.src];
    if (!img || !img.complete || !img.naturalWidth) return;
    var a = P.toStage(scene.view, u.lon0, u.lat1);
    var b = P.toStage(scene.view, u.lon1, u.lat0);
    ctx.save();
    ctx.globalAlpha = u.opacity === undefined ? 0.7 : u.opacity;
    ctx.drawImage(img, a[0], a[1], b[0] - a[0], b[1] - a[1]);
    ctx.restore();
  }

  function labelAnchor(pos, x, y, rad, k) {
    if (pos === 'left') return { x: x - rad - 5 * k, y: y, align: 'right', urduAlign: 'right' };
    if (pos === 'above') return { x: x, y: y - rad - 9 * k, align: 'center', urduAlign: 'center' };
    if (pos === 'below') return { x: x, y: y + rad + 11 * k, align: 'center', urduAlign: 'center' };
    return { x: x + rad + 5 * k, y: y, align: 'left', urduAlign: 'left' };
  }

  /* Mark sizing. style.markScale lifts every mark and its label at once — that is
   * what keeps a wide map legible from the back of a hall — and each object can
   * carry its own `scale` on top, so one column can be made to dominate. */
  function markScale(scene) {
    return scene.style.markScale === undefined ? 1 : scene.style.markScale;
  }

  function drawObjects(ctx, store, W, H, k, opts) {
    var scene = store.scene;
    var view = scene.view;
    var objs = store.visibleObjects();
    var sel = opts.showSelection ? store.selection : null;
    var showUrdu = scene.style.urduLabels !== false;
    var base = markScale(scene);

    function stage(lon, lat) { return P.toStage(view, lon, lat); }
    function pts(list) { return list.map(function (p) { return stage(p[0], p[1]); }); }
    function mk(o) { return k * base * (o.scale || 1); }

    var i, o, p, f, m;

    for (i = 0; i < objs.length; i++) {
      o = objs[i];
      if (o.type !== 'territory') continue;
      f = store.faction(o.faction);
      T.territory(ctx, pts(o.pts), f.color, o.opacity, k * base, sel === o.id);
    }
    for (i = 0; i < objs.length; i++) {
      o = objs[i];
      if (o.type !== 'territory' || !o.label) continue;
      m = mk(o);
      var cen = P.centroid(pts(o.pts));
      T.haloText(ctx, o.label.toUpperCase(), cen[0], cen[1], {
        k: m, align: 'center',
        font: '600 ' + (17 * m) + 'px ' + T.SERIF,
        color: 'rgba(244,236,214,0.92)', haloWidth: 4.2
      });
      if (showUrdu && o.ur) T.urduText(ctx, o.ur, cen[0], cen[1] + 26 * m, { k: m, align: 'center', size: 16 });
    }

    for (i = 0; i < objs.length; i++) {
      o = objs[i];
      if (o.type !== 'arrow') continue;
      f = store.faction(o.faction);
      T.arrow(ctx, pts(o.pts), f.color, (o.width || 14) * base * (o.scale || 1), o.dashed, k, sel === o.id, o.flip);
    }
    for (i = 0; i < objs.length; i++) {
      o = objs[i];
      if (o.type !== 'arrow' || !o.label) continue;
      m = mk(o);
      var lp = pts(o.pts);
      var mid = lp[Math.floor(lp.length / 2)];
      T.haloText(ctx, o.label, mid[0], mid[1] - 15 * m, {
        k: m, align: 'center', font: 'italic 600 ' + (14 * m) + 'px ' + T.SERIF
      });
    }

    for (i = 0; i < objs.length; i++) {
      o = objs[i];
      if (o.type !== 'settlement') continue;
      m = mk(o);
      p = stage(o.lon, o.lat);
      T.settlement(ctx, p[0], p[1], o.tier, m, sel === o.id);
      var rad = (o.tier === 'capital' ? 15 : o.tier === 'fort' ? 10 : 8) * m;
      var an = labelAnchor(o.labelPos, p[0], p[1], rad, m);
      var big = o.tier === 'capital';
      T.haloText(ctx, o.name, an.x, an.y, {
        k: m, align: an.align,
        font: (big ? '700 ' : '600 ') + ((big ? 17 : 14.5) * m) + 'px ' + T.SERIF,
        color: big ? '#FFF3D6' : T.CREAM
      });
      if (showUrdu && o.ur) {
        T.urduText(ctx, o.ur, an.x, an.y + (big ? 24 : 21) * m, { k: m, align: an.urduAlign, size: big ? 17 : 15 });
      }
    }

    for (i = 0; i < objs.length; i++) {
      o = objs[i];
      if (o.type !== 'battle') continue;
      m = mk(o);
      p = stage(o.lon, o.lat);
      T.battleMark(ctx, p[0], p[1], m, sel === o.id);
      var ban = labelAnchor(o.labelPos, p[0], p[1], 24 * m, m);
      T.haloText(ctx, o.name, ban.x, ban.y, {
        k: m, align: ban.align, font: '700 ' + (15 * m) + 'px ' + T.SERIF, color: '#FFD9CF'
      });
      if (o.date) {
        T.haloText(ctx, o.date, ban.x, ban.y + 17 * m, {
          k: m, align: ban.align, font: '600 ' + (12.5 * m) + 'px ' + T.SERIF, color: T.rgba(T.GOLD, 0.95)
        });
      }
      if (showUrdu && o.ur) T.urduText(ctx, o.ur, ban.x, ban.y + (o.date ? 40 : 23) * m, { k: m, align: ban.urduAlign, size: 15 });
    }

    for (i = 0; i < objs.length; i++) {
      o = objs[i];
      if (o.type !== 'army') continue;
      m = mk(o);
      p = stage(o.lon, o.lat);
      f = store.faction(o.faction);
      T.armyToken(ctx, p[0], p[1], o, f, m, sel === o.id);
      var aan = labelAnchor(o.labelPos, p[0], p[1] - 17 * m, 36 * m, m);
      T.haloText(ctx, o.name, aan.x, aan.y, {
        k: m, align: aan.align, font: '700 ' + (15 * m) + 'px ' + T.SERIF
      });
      var below = aan.y + 17 * m;
      if (o.strength) {
        T.haloText(ctx, o.strength, aan.x, below, {
          k: m, align: aan.align, font: '600 ' + (12.5 * m) + 'px ' + T.SERIF, color: T.rgba(T.GOLD, 0.95)
        });
        below += 17 * m;
      }
      if (showUrdu && o.ur) T.urduText(ctx, o.ur, aan.x, below + 6 * m, { k: m, align: aan.urduAlign, size: 15 });
    }

    for (i = 0; i < objs.length; i++) {
      o = objs[i];
      if (o.type !== 'label') continue;
      m = k * base * (o.scale || 1);
      p = stage(o.lon, o.lat);
      T.haloText(ctx, o.text, p[0], p[1], {
        k: m, align: o.align,
        font: '700 ' + (o.size * m) + 'px ' + T.SERIF,
        color: '#FFF3D6', haloWidth: 4.6
      });
      if (showUrdu && o.ur) {
        T.urduText(ctx, o.ur, p[0], p[1] + (o.size + 12) * m, { k: m, align: o.align, size: o.size * 0.85 });
      }
      if (sel === o.id) T.selectionRing(ctx, p[0], p[1], o.size * m, m);
    }

    if (opts.showSelection && store.selection) {
      var s = store.get(store.selection);
      if (s && s.pts) {
        var hp = pts(s.pts);
        for (var h = 0; h < hp.length; h++) T.handle(ctx, hp[h][0], hp[h][1], k);
      }
    }
  }

  function drawCartouche(ctx, store, W, H, k) {
    var scene = store.scene;
    if (!scene.style.cartouche && !scene.style.legend) return;

    var used = {};
    store.visibleObjects().forEach(function (o) { if (o.faction) used[o.faction] = true; });
    var legend = scene.style.legend
      ? scene.factions.filter(function (f) { return used[f.id]; })
      : [];

    var title = (scene.meta.title || '').trim();
    var sub = (scene.meta.subtitle || '').trim();
    var urdu = (scene.meta.urduTitle || '').trim();
    var hasHead = scene.style.cartouche && (title || sub || urdu);
    if (!hasHead && !legend.length) return;

    k = k * (scene.style.cartoucheScale === undefined ? 1 : scene.style.cartoucheScale);

    var padX = 20 * k, padY = 16 * k;
    var x = 34 * k, y = H - 34 * k;
    var lineH = 22 * k;

    var bw = 0;
    ctx.save();
    ctx.font = '700 ' + (26 * k) + 'px ' + T.SERIF;
    if (title) bw = Math.max(bw, ctx.measureText(title).width);
    ctx.font = '600 ' + (14 * k) + 'px ' + T.SERIF;
    if (sub) bw = Math.max(bw, ctx.measureText(sub).width);
    ctx.font = (18 * k) + 'px ' + T.NASTALIQ;
    if (urdu) bw = Math.max(bw, ctx.measureText(urdu).width);
    ctx.font = '600 ' + (14 * k) + 'px ' + T.SERIF;
    for (var i = 0; i < legend.length; i++) bw = Math.max(bw, ctx.measureText(legend[i].name).width + 30 * k);
    ctx.restore();

    var bh = padY * 2;
    if (hasHead) {
      if (title) bh += 32 * k;
      if (sub) bh += 20 * k;
      if (urdu) bh += 30 * k;
    }
    if (legend.length) bh += (hasHead ? 14 * k : 0) + legend.length * lineH;

    var bx = x, by = y - bh, bwid = bw + padX * 2;

    ctx.save();
    ctx.beginPath();
    ctx.rect(bx, by, bwid, bh);
    ctx.fillStyle = 'rgba(8,16,21,0.74)';
    ctx.shadowColor = 'rgba(0,0,0,0.55)';
    ctx.shadowBlur = 18 * k;
    ctx.fill();
    ctx.shadowColor = 'transparent';
    ctx.strokeStyle = T.rgba(T.GOLD, 0.42);
    ctx.lineWidth = 1.2 * k;
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(bx, by);
    ctx.lineTo(bx + bwid, by);
    ctx.strokeStyle = T.rgba(T.GOLD, 0.85);
    ctx.lineWidth = 2.4 * k;
    ctx.stroke();
    ctx.restore();

    var cy = by + padY;
    if (hasHead) {
      if (title) {
        cy += 22 * k;
        T.haloText(ctx, title, bx + padX, cy, {
          k: k, font: '700 ' + (26 * k) + 'px ' + T.SERIF, color: '#FFF3D6', haloWidth: 2.4
        });
        cy += 10 * k;
      }
      if (sub) {
        cy += 14 * k;
        T.haloText(ctx, sub, bx + padX, cy, {
          k: k, font: '600 ' + (14 * k) + 'px ' + T.SERIF, color: 'rgba(226,214,185,0.80)', haloWidth: 2
        });
        cy += 6 * k;
      }
      if (urdu) {
        cy += 24 * k;
        T.urduText(ctx, urdu, bx + padX, cy, { k: k, size: 18, haloWidth: 2.4 });
        cy += 6 * k;
      }
      if (legend.length) cy += 14 * k;
    }

    for (var j = 0; j < legend.length; j++) {
      var ly = cy + lineH * j + lineH * 0.5;
      ctx.save();
      ctx.beginPath();
      ctx.rect(bx + padX, ly - 5 * k, 16 * k, 10 * k);
      ctx.fillStyle = legend[j].color;
      ctx.fill();
      ctx.strokeStyle = 'rgba(10,16,20,0.7)';
      ctx.lineWidth = 1 * k;
      ctx.stroke();
      ctx.restore();
      T.haloText(ctx, legend[j].name, bx + padX + 24 * k, ly, {
        k: k, font: '600 ' + (14 * k) + 'px ' + T.SERIF, color: 'rgba(238,229,206,0.94)', haloWidth: 2
      });
    }
  }

  function drawScalebar(ctx, scene, W, H, k) {
    if (!scene.style.scalebar) return;
    var kmPerWorld = 111.32;
    var kmPerPx = kmPerWorld / scene.view.scale;
    var raw = 190 * kmPerPx;
    var mag = Math.pow(10, Math.floor(Math.log(raw) / Math.LN10));
    var nice = [1, 2, 2.5, 5, 10];
    var km = mag;
    for (var i = 0; i < nice.length; i++) {
      if (nice[i] * mag >= raw * 0.55) { km = nice[i] * mag; break; }
    }
    var px = km / kmPerPx;

    var x = W - 44 * k - px * k;
    var y = H - 46 * k;

    ctx.save();
    ctx.lineCap = 'butt';
    for (var s = 0; s < 4; s++) {
      ctx.beginPath();
      ctx.rect(x + (px * k / 4) * s, y, px * k / 4, 6 * k);
      ctx.fillStyle = s % 2 ? 'rgba(10,16,20,0.85)' : 'rgba(242,234,214,0.92)';
      ctx.fill();
      ctx.strokeStyle = 'rgba(242,234,214,0.85)';
      ctx.lineWidth = 1 * k;
      ctx.stroke();
    }
    ctx.restore();
    T.haloText(ctx, km.toLocaleString('en-US') + ' km', x + px * k / 2, y - 10 * k, {
      k: k, align: 'center', font: '600 ' + (12 * k) + 'px ' + T.SERIF,
      color: 'rgba(238,229,206,0.9)', haloWidth: 3
    });

    var nx = W - 44 * k, ny = y - 46 * k;
    ctx.save();
    ctx.beginPath();
    ctx.moveTo(nx, ny - 17 * k);
    ctx.lineTo(nx + 6.5 * k, ny + 8 * k);
    ctx.lineTo(nx, ny + 3 * k);
    ctx.lineTo(nx - 6.5 * k, ny + 8 * k);
    ctx.closePath();
    ctx.fillStyle = 'rgba(242,234,214,0.9)';
    ctx.strokeStyle = 'rgba(10,16,20,0.8)';
    ctx.lineWidth = 1 * k;
    ctx.fill();
    ctx.stroke();
    ctx.restore();
    T.haloText(ctx, 'N', nx, ny + 19 * k, {
      k: k, align: 'center', font: '700 ' + (12 * k) + 'px ' + T.SERIF,
      color: 'rgba(238,229,206,0.9)', haloWidth: 3
    });
  }

  function drawFinish(ctx, scene, W, H, k) {
    if (scene.style.grain) {
      if (!grainTile) grainTile = makeGrain();
      ctx.save();
      ctx.globalAlpha = 0.075;
      ctx.globalCompositeOperation = 'overlay';
      ctx.fillStyle = ctx.createPattern(grainTile, 'repeat');
      ctx.fillRect(0, 0, W, H);
      ctx.restore();
    }
    if (scene.style.vignette) {
      var v = ctx.createRadialGradient(W / 2, H / 2, Math.min(W, H) * 0.32, W / 2, H / 2, Math.max(W, H) * 0.78);
      v.addColorStop(0, 'rgba(0,0,0,0)');
      v.addColorStop(1, 'rgba(0,0,0,0.26)');
      ctx.save();
      ctx.fillStyle = v;
      ctx.fillRect(0, 0, W, H);
      ctx.restore();
    }
    ctx.save();
    ctx.strokeStyle = 'rgba(226,206,160,0.22)';
    ctx.lineWidth = 2 * k;
    ctx.strokeRect(1 * k, 1 * k, W - 2 * k, H - 2 * k);
    ctx.restore();
  }

  function render(ctx, store, opts) {
    opts = opts || {};
    var sc = opts.k || 1;
    ctx.setTransform(sc, 0, 0, sc, 0, 0);
    var k = 1;
    var W = P.STAGE_W, H = P.STAGE_H;
    var scene = store.scene;

    ctx.save();
    ctx.clearRect(0, 0, W, H);
    drawBase(ctx, scene, W, H, k);
    drawGraticule(ctx, scene, W, H, k);
    drawUnderlay(ctx, scene, W, H, k, opts.images || {});
    drawObjects(ctx, store, W, H, k, opts);
    drawCartouche(ctx, store, W, H, k);
    drawScalebar(ctx, scene, W, H, k);
    drawFinish(ctx, scene, W, H, k);
    ctx.restore();
  }

  initRelief();

  global.MS_Render = { render: render, labelAnchor: labelAnchor, whenReady: whenReady, markScale: markScale };
})(window);
