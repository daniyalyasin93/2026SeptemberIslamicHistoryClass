/* proj.js — projection, viewport and small geometry helpers.
 *
 * One projection for the whole series: equirectangular with a standard parallel at
 * 30N, the same maths as series/make_basemap.py, so a map made here sits beside the
 * workbook base map without looking like a different world.
 *
 * Three coordinate spaces:
 *   geo     lon/lat degrees
 *   world   projected, y-down, independent of zoom
 *   stage   pixels on the 1600x900 logical stage
 *
 * No imports/exports: the studio runs from file:// where ES modules are blocked.
 */
(function (global) {
  'use strict';

  var LAT0 = 30.0;
  var K = Math.cos(LAT0 * Math.PI / 180);

  var STAGE_W = 1600;
  var STAGE_H = 900;

  /* Region presets. Each is a geographic bbox the view can be fitted to. */
  var REGIONS = [
    { id: 'hijaz',     name: 'Hijaz and Najd',        bbox: [33.0, 14.0, 58.0, 32.0] },
    { id: 'sham-iraq', name: 'Sham and Iraq',         bbox: [28.0, 26.0, 52.0, 40.0] },
    { id: 'rashidun',  name: 'The early conquests',   bbox: [24.0, 11.0, 68.0, 43.0] },
    { id: 'caliphate', name: 'The whole caliphate',   bbox: [-14.0, 8.0, 80.0, 46.0] },
    { id: 'medit',     name: 'The Mediterranean',     bbox: [-12.0, 27.0, 42.0, 48.0] },
    { id: 'iran',      name: 'Iran and Khurasan',     bbox: [42.0, 24.0, 76.0, 44.0] },
    { id: 'hind',      name: 'Sindh and Hind',        bbox: [60.0, 20.0, 92.0, 38.0] },
    { id: 'anatolia',  name: 'Anatolia and the Rum',  bbox: [18.0, 30.0, 50.0, 48.0] }
  ];

  function lonToWorld(lon) { return lon * K; }
  function latToWorld(lat) { return -lat; }
  function worldToLon(wx) { return wx / K; }
  function worldToLat(wy) { return -wy; }

  /* view = {cx, cy, scale} : world units at stage centre, stage px per world unit */
  function makeView() {
    var v = { cx: 0, cy: 0, scale: 20 };
    fitBBox(v, REGIONS[2].bbox);
    return v;
  }

  function fitBBox(view, bbox, pad) {
    pad = pad === undefined ? 0.94 : pad;
    var x0 = lonToWorld(bbox[0]), x1 = lonToWorld(bbox[2]);
    var y0 = latToWorld(bbox[3]), y1 = latToWorld(bbox[1]);
    var sx = STAGE_W / Math.max(1e-6, x1 - x0);
    var sy = STAGE_H / Math.max(1e-6, y1 - y0);
    view.scale = Math.min(sx, sy) * pad;
    view.cx = (x0 + x1) / 2;
    view.cy = (y0 + y1) / 2;
    return view;
  }

  function toStage(view, lon, lat) {
    return [
      (lonToWorld(lon) - view.cx) * view.scale + STAGE_W / 2,
      (latToWorld(lat) - view.cy) * view.scale + STAGE_H / 2
    ];
  }

  function toGeo(view, sx, sy) {
    var wx = (sx - STAGE_W / 2) / view.scale + view.cx;
    var wy = (sy - STAGE_H / 2) / view.scale + view.cy;
    return [worldToLon(wx), worldToLat(wy)];
  }

  /* Zoom keeping the geo point under (sx,sy) pinned there. */
  function zoomAt(view, factor, sx, sy) {
    var before = toGeo(view, sx, sy);
    view.scale = Math.max(3, Math.min(4000, view.scale * factor));
    var after = toGeo(view, sx, sy);
    view.cx += lonToWorld(before[0]) - lonToWorld(after[0]);
    view.cy += latToWorld(before[1]) - latToWorld(after[1]);
    return view;
  }

  function panBy(view, dxStage, dyStage) {
    view.cx -= dxStage / view.scale;
    view.cy -= dyStage / view.scale;
    return view;
  }

  /* --- geometry helpers, all in stage pixels --- */

  function dist(ax, ay, bx, by) {
    var dx = ax - bx, dy = ay - by;
    return Math.sqrt(dx * dx + dy * dy);
  }

  function distToSegment(px, py, ax, ay, bx, by) {
    var vx = bx - ax, vy = by - ay;
    var len2 = vx * vx + vy * vy;
    if (len2 < 1e-9) return dist(px, py, ax, ay);
    var t = Math.max(0, Math.min(1, ((px - ax) * vx + (py - ay) * vy) / len2));
    return dist(px, py, ax + t * vx, ay + t * vy);
  }

  function distToPolyline(px, py, pts) {
    var best = Infinity;
    for (var i = 0; i < pts.length - 1; i++) {
      best = Math.min(best, distToSegment(px, py, pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1]));
    }
    return best;
  }

  function pointInPolygon(px, py, pts) {
    var inside = false;
    for (var i = 0, j = pts.length - 1; i < pts.length; j = i++) {
      var xi = pts[i][0], yi = pts[i][1], xj = pts[j][0], yj = pts[j][1];
      if ((yi > py) !== (yj > py) && px < (xj - xi) * (py - yi) / (yj - yi) + xi) inside = !inside;
    }
    return inside;
  }

  function centroid(pts) {
    var x = 0, y = 0;
    for (var i = 0; i < pts.length; i++) { x += pts[i][0]; y += pts[i][1]; }
    return [x / pts.length, y / pts.length];
  }

  /* Resample a polyline into a smooth Catmull-Rom curve. Used by campaign arrows so
   * a three-click path reads as a sweep rather than a dogleg. */
  function smooth(pts, perSeg) {
    if (pts.length < 3) return pts.slice();
    perSeg = perSeg || 16;
    var p = [pts[0]].concat(pts, [pts[pts.length - 1]]);
    var out = [];
    for (var i = 1; i < p.length - 2; i++) {
      var p0 = p[i - 1], p1 = p[i], p2 = p[i + 1], p3 = p[i + 2];
      for (var s = 0; s < perSeg; s++) {
        var t = s / perSeg, t2 = t * t, t3 = t2 * t;
        out.push([
          0.5 * ((2 * p1[0]) + (-p0[0] + p2[0]) * t + (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t2 + (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t3),
          0.5 * ((2 * p1[1]) + (-p0[1] + p2[1]) * t + (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t2 + (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t3)
        ]);
      }
    }
    out.push(pts[pts.length - 1]);
    return out;
  }

  /* A two-point arrow gets a gentle bow so it never reads as a ruler line. */
  function bow(a, b, amount) {
    var mx = (a[0] + b[0]) / 2, my = (a[1] + b[1]) / 2;
    var dx = b[0] - a[0], dy = b[1] - a[1];
    var len = Math.sqrt(dx * dx + dy * dy) || 1;
    var k = (amount === undefined ? 0.16 : amount) * len;
    return [a, [mx - dy / len * k, my + dx / len * k], b];
  }

  global.MS_Proj = {
    LAT0: LAT0, K: K, STAGE_W: STAGE_W, STAGE_H: STAGE_H, REGIONS: REGIONS,
    makeView: makeView, fitBBox: fitBBox, toStage: toStage, toGeo: toGeo,
    zoomAt: zoomAt, panBy: panBy,
    dist: dist, distToSegment: distToSegment, distToPolyline: distToPolyline,
    pointInPolygon: pointInPolygon, centroid: centroid, smooth: smooth, bow: bow
  };
})(window);
