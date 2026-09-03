/* tokens.js — the marks themselves: settlements, army banners, unit silhouettes,
 * battle marks, campaign arrows, territory fills, and haloed labels.
 *
 * Everything takes a `k` scale factor so the same code draws the 1600x900 screen
 * stage and a 3840x2160 export with identical proportions.
 *
 * House rules honoured here: no emblem is ever attached to a *person* — a banner
 * belongs to a faction and a silhouette describes a unit type. Urdu is drawn as its
 * own block, never inline with English.
 */
(function (global) {
  'use strict';

  var INK = '#0B141A';
  var CREAM = '#FBF4E2';
  var GOLD = '#F2BC52';
  var STEEL = '#C9D2D6';

  var SERIF = 'Georgia, "Palatino Linotype", "Book Antiqua", serif';
  var NASTALIQ = '"Noto Nastaliq Urdu", "Segoe UI", serif';

  /* ---------- colour helpers ---------- */

  function hexToRgb(hex) {
    var h = hex.replace('#', '');
    if (h.length === 3) h = h[0] + h[0] + h[1] + h[1] + h[2] + h[2];
    return [parseInt(h.slice(0, 2), 16), parseInt(h.slice(2, 4), 16), parseInt(h.slice(4, 6), 16)];
  }

  function rgba(hex, a) {
    var c = hexToRgb(hex);
    return 'rgba(' + c[0] + ',' + c[1] + ',' + c[2] + ',' + a + ')';
  }

  function shade(hex, amt) {
    var c = hexToRgb(hex);
    for (var i = 0; i < 3; i++) {
      c[i] = Math.round(amt < 0 ? c[i] * (1 + amt) : c[i] + (255 - c[i]) * amt);
      c[i] = Math.max(0, Math.min(255, c[i]));
    }
    return 'rgb(' + c[0] + ',' + c[1] + ',' + c[2] + ')';
  }

  /* ---------- text ---------- */

  /* Every label gets an ink halo. Without it, cream text over pale desert is mush. */
  function haloText(ctx, text, x, y, opts) {
    opts = opts || {};
    var k = opts.k || 1;
    ctx.save();
    ctx.font = opts.font || ('600 ' + (14 * k) + 'px ' + SERIF);
    ctx.textAlign = opts.align || 'left';
    ctx.textBaseline = opts.baseline || 'middle';
    ctx.lineJoin = 'round';
    ctx.miterLimit = 2;
    if (opts.direction) ctx.direction = opts.direction;
    ctx.strokeStyle = opts.halo || 'rgba(7,12,16,0.92)';
    ctx.lineWidth = (opts.haloWidth || 3.6) * k;
    ctx.strokeText(text, x, y);
    ctx.fillStyle = opts.color || CREAM;
    ctx.fillText(text, x, y);
    ctx.restore();
  }

  function urduText(ctx, text, x, y, opts) {
    opts = opts || {};
    var k = opts.k || 1;
    haloText(ctx, text, x, y, {
      k: k,
      font: (opts.size || 15) * k + 'px ' + NASTALIQ,
      align: opts.align || 'left',
      baseline: 'alphabetic',
      color: opts.color || rgba(GOLD, 0.95),
      halo: opts.halo,
      haloWidth: opts.haloWidth || 3.2,
      direction: 'rtl'
    });
  }

  /* ---------- settlements ---------- */

  var TIER_SIZE = { capital: 7.5, city: 5.6, town: 4.0, fort: 5.4 };

  function settlement(ctx, x, y, tier, k, sel) {
    var r = (TIER_SIZE[tier] || 5.6) * k;
    ctx.save();
    ctx.shadowColor = 'rgba(0,0,0,0.55)';
    ctx.shadowBlur = 6 * k;
    ctx.shadowOffsetY = 1.5 * k;

    if (tier === 'fort') {
      // A small crenellated tower: reads as a garrison, not a city.
      var w = r * 1.5, h = r * 1.55;
      ctx.beginPath();
      ctx.moveTo(x - w, y);
      ctx.lineTo(x - w, y - h * 0.62);
      ctx.lineTo(x - w * 0.55, y - h * 0.62);
      ctx.lineTo(x - w * 0.55, y - h);
      ctx.lineTo(x - w * 0.18, y - h);
      ctx.lineTo(x - w * 0.18, y - h * 0.62);
      ctx.lineTo(x + w * 0.18, y - h * 0.62);
      ctx.lineTo(x + w * 0.18, y - h);
      ctx.lineTo(x + w * 0.55, y - h);
      ctx.lineTo(x + w * 0.55, y - h * 0.62);
      ctx.lineTo(x + w, y - h * 0.62);
      ctx.lineTo(x + w, y);
      ctx.closePath();
      ctx.fillStyle = CREAM;
      ctx.fill();
      ctx.shadowColor = 'transparent';
      ctx.lineWidth = 1.2 * k;
      ctx.strokeStyle = INK;
      ctx.stroke();
    } else if (tier === 'capital') {
      // Ring, core, and four short rays. The busiest mark on the map, by design.
      ctx.beginPath();
      for (var i = 0; i < 4; i++) {
        var a = Math.PI / 4 + i * Math.PI / 2;
        ctx.moveTo(x, y);
        ctx.lineTo(x + Math.cos(a) * r * 2.05, y + Math.sin(a) * r * 2.05);
      }
      ctx.strokeStyle = GOLD;
      ctx.lineWidth = 1.9 * k;
      ctx.lineCap = 'round';
      ctx.stroke();
      ctx.beginPath();
      ctx.arc(x, y, r, 0, Math.PI * 2);
      ctx.fillStyle = CREAM;
      ctx.fill();
      ctx.shadowColor = 'transparent';
      ctx.lineWidth = 2.4 * k;
      ctx.strokeStyle = GOLD;
      ctx.stroke();
      ctx.beginPath();
      ctx.arc(x, y, r + 1.7 * k, 0, Math.PI * 2);
      ctx.strokeStyle = 'rgba(28,22,12,0.55)';
      ctx.lineWidth = 1.1 * k;
      ctx.stroke();
      ctx.beginPath();
      ctx.arc(x, y, r * 0.42, 0, Math.PI * 2);
      ctx.fillStyle = INK;
      ctx.fill();
    } else {
      ctx.beginPath();
      ctx.arc(x, y, r, 0, Math.PI * 2);
      ctx.fillStyle = tier === 'town' ? INK : CREAM;
      ctx.fill();
      ctx.shadowColor = 'transparent';
      ctx.lineWidth = (tier === 'town' ? 1.8 : 2.1) * k;
      ctx.strokeStyle = tier === 'town' ? CREAM : GOLD;
      ctx.stroke();
      ctx.beginPath();
      ctx.arc(x, y, r + 1.7 * k, 0, Math.PI * 2);
      ctx.strokeStyle = 'rgba(28,22,12,0.55)';
      ctx.lineWidth = 1.1 * k;
      ctx.stroke();
    }

    ctx.restore();
    if (sel) selectionRing(ctx, x, y, r * 2.6 + 4 * k, k);
  }

  /* ---------- unit silhouettes ---------- */

  /* Each glyph is drawn inside a unit box centred on the origin, then scaled. */
  function unitGlyph(ctx, cx, cy, size, unit, color, hole) {
    ctx.save();
    ctx.translate(cx, cy);
    ctx.scale(size, size);
    ctx.fillStyle = color;
    ctx.strokeStyle = color;
    ctx.lineWidth = 0.11;
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';

    if (unit === 'cavalry') {
      ctx.beginPath();                       // knight profile: the silhouette people read as "horse"
      ctx.moveTo(-0.30, 0.52);
      ctx.lineTo(-0.30, 0.10);
      ctx.bezierCurveTo(-0.34, -0.16, -0.16, -0.34, 0.00, -0.40);
      ctx.lineTo(-0.04, -0.56);
      ctx.lineTo(0.14, -0.38);
      ctx.lineTo(0.24, -0.50);
      ctx.lineTo(0.27, -0.28);
      ctx.bezierCurveTo(0.46, -0.17, 0.52, 0.01, 0.42, 0.12);
      ctx.lineTo(0.14, 0.19);
      ctx.bezierCurveTo(0.04, 0.28, 0.03, 0.40, 0.05, 0.52);
      ctx.closePath();
      ctx.fill();
    } else if (unit === 'archer') {
      ctx.lineWidth = 0.15;
      ctx.beginPath();                       // bow
      ctx.moveTo(-0.02, -0.46);
      ctx.quadraticCurveTo(0.46, 0.0, -0.02, 0.46);
      ctx.stroke();
      ctx.lineWidth = 0.12;
      ctx.beginPath();                       // nocked arrow
      ctx.moveTo(-0.44, 0);
      ctx.lineTo(0.18, 0);
      ctx.stroke();
      ctx.beginPath();
      ctx.moveTo(0.34, 0);
      ctx.lineTo(0.14, -0.15);
      ctx.lineTo(0.14, 0.15);
      ctx.closePath();
      ctx.fill();
    } else if (unit === 'naval') {
      ctx.beginPath();                       // hull
      ctx.moveTo(-0.52, 0.20);
      ctx.quadraticCurveTo(0, 0.62, 0.52, 0.20);
      ctx.quadraticCurveTo(0, 0.36, -0.52, 0.20);
      ctx.closePath();
      ctx.fill();
      ctx.lineWidth = 0.10;
      ctx.beginPath();                       // mast
      ctx.moveTo(-0.14, 0.24);
      ctx.lineTo(-0.14, -0.54);
      ctx.stroke();
      ctx.beginPath();                       // sail, the shape that says "ship"
      ctx.moveTo(-0.06, -0.50);
      ctx.quadraticCurveTo(0.44, -0.12, -0.06, 0.12);
      ctx.closePath();
      ctx.fill();
    } else if (unit === 'infantry') {
      ctx.beginPath();                       // shield
      ctx.moveTo(-0.33, -0.44);
      ctx.lineTo(0.33, -0.44);
      ctx.lineTo(0.33, 0.04);
      ctx.quadraticCurveTo(0.33, 0.36, 0, 0.50);
      ctx.quadraticCurveTo(-0.33, 0.36, -0.33, 0.04);
      ctx.closePath();
      ctx.fill();
      /* The sword is drawn in the roundel's own colour rather than punched out with
       * destination-out: that composite op clears the pixels outright, which left a
       * transparent hole straight through the banner and the map beneath it. */
      ctx.save();
      ctx.fillStyle = hole || 'rgba(20,30,36,0.92)';
      ctx.beginPath();                       // sword on the shield
      ctx.moveTo(-0.065, -0.28);
      ctx.lineTo(0.065, -0.28);
      ctx.lineTo(0.065, 0.18);
      ctx.lineTo(0, 0.34);
      ctx.lineTo(-0.065, 0.18);
      ctx.closePath();
      ctx.fill();
      ctx.beginPath();                       // crossguard
      ctx.rect(-0.24, -0.24, 0.48, 0.105);
      ctx.fill();
      ctx.restore();
    } else {                                  // mixed
      for (var i = 0; i < 3; i++) {
        var yy = -0.28 + i * 0.30;
        ctx.beginPath();
        ctx.moveTo(-0.40, yy + 0.13);
        ctx.lineTo(0, yy - 0.13);
        ctx.lineTo(0.40, yy + 0.13);
        ctx.lineWidth = 0.155;
        ctx.stroke();
      }
    }
    ctx.restore();
  }

  /* ---------- army banner ---------- */

  function armyToken(ctx, x, y, obj, faction, k, sel) {
    var col = faction.color;
    var poleH = 46 * k;
    var flagW = 33 * k;
    var flagH = 21 * k;

    ctx.save();

    // ground shadow anchors the token to the map
    ctx.beginPath();
    ctx.ellipse(x, y + 2 * k, 13 * k, 4.2 * k, 0, 0, Math.PI * 2);
    ctx.fillStyle = 'rgba(0,0,0,0.40)';
    ctx.fill();

    // pole
    ctx.beginPath();
    ctx.moveTo(x, y + 1 * k);
    ctx.lineTo(x, y - poleH);
    ctx.strokeStyle = '#2A2118';
    ctx.lineWidth = 2.4 * k;
    ctx.lineCap = 'round';
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(x - 0.5 * k, y + 1 * k);
    ctx.lineTo(x - 0.5 * k, y - poleH);
    ctx.strokeStyle = 'rgba(226,206,160,0.35)';
    ctx.lineWidth = 0.8 * k;
    ctx.stroke();

    // swallowtail pennant
    var top = y - poleH;
    ctx.beginPath();
    ctx.moveTo(x, top);
    ctx.lineTo(x + flagW, top + flagH * 0.10);
    ctx.lineTo(x + flagW * 0.74, top + flagH * 0.50);
    ctx.lineTo(x + flagW, top + flagH * 0.90);
    ctx.lineTo(x, top + flagH);
    ctx.closePath();
    var g = ctx.createLinearGradient(x, top, x + flagW, top + flagH);
    g.addColorStop(0, shade(col, 0.16));
    g.addColorStop(1, shade(col, -0.26));
    ctx.fillStyle = g;
    ctx.shadowColor = 'rgba(0,0,0,0.45)';
    ctx.shadowBlur = 5 * k;
    ctx.shadowOffsetY = 1.5 * k;
    ctx.fill();
    ctx.shadowColor = 'transparent';
    ctx.strokeStyle = 'rgba(10,16,20,0.75)';
    ctx.lineWidth = 1.1 * k;
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(x + 1.5 * k, top + flagH * 0.5);
    ctx.lineTo(x + flagW * 0.66, top + flagH * 0.5);
    ctx.strokeStyle = 'rgba(255,255,255,0.22)';
    ctx.lineWidth = 1.0 * k;
    ctx.stroke();

    // roundel at the foot, carrying the unit silhouette
    var rr = 16.5 * k;
    var ry = y - 16.5 * k;
    ctx.beginPath();
    ctx.arc(x, ry, rr, 0, Math.PI * 2);
    var rg = ctx.createRadialGradient(x - rr * 0.35, ry - rr * 0.4, rr * 0.1, x, ry, rr);
    rg.addColorStop(0, shade(col, 0.24));
    rg.addColorStop(1, shade(col, -0.34));
    ctx.fillStyle = rg;
    ctx.shadowColor = 'rgba(0,0,0,0.5)';
    ctx.shadowBlur = 5 * k;
    ctx.fill();
    ctx.shadowColor = 'transparent';
    ctx.lineWidth = 2.0 * k;
    ctx.strokeStyle = rgba(GOLD, 0.9);
    ctx.stroke();
    ctx.beginPath();
    ctx.arc(x, ry, rr - 2.4 * k, 0, Math.PI * 2);
    ctx.lineWidth = 1.1 * k;
    ctx.strokeStyle = 'rgba(8,14,18,0.42)';
    ctx.stroke();
    unitGlyph(ctx, x, ry, rr * 1.20, obj.unit || 'mixed', 'rgba(249,244,230,0.99)', shade(col, -0.62));

    ctx.restore();
    if (sel) selectionRing(ctx, x, y - poleH * 0.5, poleH * 0.85, k);
  }

  /* ---------- battle ---------- */

  function battleMark(ctx, x, y, k, sel) {
    var s = 13 * k;
    ctx.save();
    ctx.translate(x, y);

    // madder burst behind, so the mark reads even over dark territory fill
    ctx.beginPath();
    for (var i = 0; i < 12; i++) {
      var a = i * Math.PI / 6;
      var r = i % 2 ? s * 1.05 : s * 1.75;
      ctx[i ? 'lineTo' : 'moveTo'](Math.cos(a) * r, Math.sin(a) * r);
    }
    ctx.closePath();
    ctx.fillStyle = 'rgba(180,70,58,0.75)';
    ctx.shadowColor = 'rgba(0,0,0,0.5)';
    ctx.shadowBlur = 7 * k;
    ctx.fill();
    ctx.shadowColor = 'transparent';

    function sword(rot) {
      ctx.save();
      ctx.rotate(rot);
      ctx.beginPath();                       // blade
      ctx.moveTo(-0.10 * s, -1.15 * s);
      ctx.lineTo(0.10 * s, -1.15 * s);
      ctx.lineTo(0.10 * s, 0.45 * s);
      ctx.lineTo(0, 0.62 * s);
      ctx.lineTo(-0.10 * s, 0.45 * s);
      ctx.closePath();
      ctx.fillStyle = STEEL;
      ctx.fill();
      ctx.strokeStyle = 'rgba(10,16,20,0.8)';
      ctx.lineWidth = 0.9 * k;
      ctx.stroke();
      ctx.beginPath();                       // guard
      ctx.rect(-0.42 * s, -1.30 * s, 0.84 * s, 0.17 * s);
      ctx.fillStyle = GOLD;
      ctx.fill();
      ctx.stroke();
      ctx.restore();
    }
    sword(Math.PI * 0.78);
    sword(-Math.PI * 0.78);

    ctx.restore();
    if (sel) selectionRing(ctx, x, y, s * 2.1, k);
  }

  /* ---------- campaign arrow ---------- */

  function arrow(ctx, pts, color, width, dashed, k, sel) {
    if (pts.length < 2) return;
    var path = pts.length === 2 ? MS_Proj.bow(pts[0], pts[1]) : pts;
    var line = MS_Proj.smooth(path, 18);
    var w = width * k;

    if (dashed) {
      ctx.save();
      ctx.setLineDash([10 * k, 8 * k]);
      ctx.lineWidth = Math.max(3, w * 0.42);
      ctx.lineCap = 'butt';
      ctx.strokeStyle = rgba(color, 0.92);
      ctx.shadowColor = 'rgba(0,0,0,0.5)';
      ctx.shadowBlur = 6 * k;
      ctx.beginPath();
      ctx.moveTo(line[0][0], line[0][1]);
      for (var d = 1; d < line.length; d++) ctx.lineTo(line[d][0], line[d][1]);
      ctx.stroke();
      ctx.restore();
      arrowHead(ctx, line, color, w * 1.05, k);
      if (sel) selectionPath(ctx, line, k);
      return;
    }

    // Cumulative length, so the ribbon can taper and the head can be trimmed off.
    var cum = [0];
    for (var i = 1; i < line.length; i++) {
      cum.push(cum[i - 1] + MS_Proj.dist(line[i][0], line[i][1], line[i - 1][0], line[i - 1][1]));
    }
    var total = cum[cum.length - 1];
    var head = Math.min(w * 2.7, total * 0.30);
    var bodyEnd = total - head;

    var left = [], right = [];
    for (var j = 0; j < line.length; j++) {
      if (cum[j] > bodyEnd) break;
      var t = cum[j] / Math.max(1e-6, bodyEnd);
      var hw = (0.34 + 0.66 * Math.pow(t, 0.6)) * w * 0.5;
      var a = line[Math.max(0, j - 1)], b = line[Math.min(line.length - 1, j + 1)];
      var dx = b[0] - a[0], dy = b[1] - a[1];
      var len = Math.sqrt(dx * dx + dy * dy) || 1;
      var nx = -dy / len, ny = dx / len;
      left.push([line[j][0] + nx * hw, line[j][1] + ny * hw]);
      right.push([line[j][0] - nx * hw, line[j][1] - ny * hw]);
    }
    if (left.length < 2) { arrowHead(ctx, line, color, w, k); return; }

    ctx.save();
    ctx.beginPath();
    ctx.moveTo(left[0][0], left[0][1]);
    for (var l = 1; l < left.length; l++) ctx.lineTo(left[l][0], left[l][1]);
    for (var r = right.length - 1; r >= 0; r--) ctx.lineTo(right[r][0], right[r][1]);
    ctx.closePath();
    var mid = line[Math.floor(line.length / 2)];
    var gr = ctx.createLinearGradient(line[0][0], line[0][1], mid[0], mid[1]);
    gr.addColorStop(0, rgba(color, 0.62));
    gr.addColorStop(1, rgba(color, 0.97));
    ctx.fillStyle = gr;
    ctx.shadowColor = 'rgba(0,0,0,0.55)';
    ctx.shadowBlur = 8 * k;
    ctx.shadowOffsetY = 2 * k;
    ctx.fill();
    ctx.shadowColor = 'transparent';
    ctx.strokeStyle = 'rgba(8,14,18,0.55)';
    ctx.lineWidth = 1.1 * k;
    ctx.stroke();
    ctx.restore();

    arrowHead(ctx, line, color, w, k);
    if (sel) selectionPath(ctx, line, k);
  }

  function arrowHead(ctx, line, color, w, k) {
    var tip = line[line.length - 1];
    var prev = line[Math.max(0, line.length - 6)];
    var dx = tip[0] - prev[0], dy = tip[1] - prev[1];
    var len = Math.sqrt(dx * dx + dy * dy) || 1;
    var ux = dx / len, uy = dy / len;
    var nx = -uy, ny = ux;
    var hl = w * 2.5, hw = w * 1.25;
    var base = [tip[0] - ux * hl, tip[1] - uy * hl];

    ctx.save();
    ctx.beginPath();
    ctx.moveTo(tip[0], tip[1]);
    ctx.lineTo(base[0] + nx * hw, base[1] + ny * hw);
    ctx.lineTo(base[0] + ux * hl * 0.30, base[1] + uy * hl * 0.30);
    ctx.lineTo(base[0] - nx * hw, base[1] - ny * hw);
    ctx.closePath();
    ctx.fillStyle = rgba(color, 0.99);
    ctx.shadowColor = 'rgba(0,0,0,0.55)';
    ctx.shadowBlur = 8 * k;
    ctx.shadowOffsetY = 2 * k;
    ctx.fill();
    ctx.shadowColor = 'transparent';
    ctx.strokeStyle = 'rgba(8,14,18,0.55)';
    ctx.lineWidth = 1.1 * k;
    ctx.stroke();
    ctx.restore();
  }

  /* ---------- territory ---------- */

  function territory(ctx, pts, color, opacity, k, sel) {
    if (pts.length < 3) return;
    ctx.save();
    ctx.beginPath();
    ctx.moveTo(pts[0][0], pts[0][1]);
    for (var i = 1; i < pts.length; i++) ctx.lineTo(pts[i][0], pts[i][1]);
    ctx.closePath();
    ctx.fillStyle = rgba(color, opacity);
    ctx.fill();
    // a soft inner glow then a crisp frontier: reads as a claimed area, not a shape
    ctx.save();
    ctx.clip();
    ctx.strokeStyle = rgba(color, Math.min(0.9, opacity + 0.42));
    ctx.lineWidth = 14 * k;
    ctx.stroke();
    ctx.restore();
    ctx.strokeStyle = rgba(color, 0.95);
    ctx.lineWidth = 2.2 * k;
    ctx.setLineDash([]);
    ctx.stroke();
    ctx.restore();
    if (sel) selectionPath(ctx, pts.concat([pts[0]]), k);
  }

  /* ---------- selection affordances ---------- */

  function selectionRing(ctx, x, y, r, k) {
    ctx.save();
    ctx.beginPath();
    ctx.arc(x, y, r, 0, Math.PI * 2);
    ctx.strokeStyle = 'rgba(255,232,150,0.95)';
    ctx.lineWidth = 1.6 * k;
    ctx.setLineDash([5 * k, 4 * k]);
    ctx.stroke();
    ctx.restore();
  }

  function selectionPath(ctx, pts, k) {
    ctx.save();
    ctx.beginPath();
    ctx.moveTo(pts[0][0], pts[0][1]);
    for (var i = 1; i < pts.length; i++) ctx.lineTo(pts[i][0], pts[i][1]);
    ctx.strokeStyle = 'rgba(255,232,150,0.95)';
    ctx.lineWidth = 1.6 * k;
    ctx.setLineDash([5 * k, 4 * k]);
    ctx.stroke();
    ctx.restore();
  }

  function handle(ctx, x, y, k) {
    ctx.save();
    ctx.beginPath();
    ctx.rect(x - 3.5 * k, y - 3.5 * k, 7 * k, 7 * k);
    ctx.fillStyle = '#FFE896';
    ctx.strokeStyle = INK;
    ctx.lineWidth = 1.2 * k;
    ctx.fill();
    ctx.stroke();
    ctx.restore();
  }

  global.MS_Tokens = {
    INK: INK, CREAM: CREAM, GOLD: GOLD, STEEL: STEEL, SERIF: SERIF, NASTALIQ: NASTALIQ,
    rgba: rgba, shade: shade, haloText: haloText, urduText: urduText,
    settlement: settlement, unitGlyph: unitGlyph, armyToken: armyToken,
    battleMark: battleMark, arrow: arrow, territory: territory,
    selectionRing: selectionRing, selectionPath: selectionPath, handle: handle
  };
})(window);
