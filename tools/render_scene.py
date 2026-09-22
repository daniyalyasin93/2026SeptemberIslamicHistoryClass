# -*- coding: utf-8 -*-
"""Render Map Studio scenes to PNG with no human in the loop.

    python tools/render_scene.py <scene.json> [more.json ...] --out-dir DIR [--scale 1.2] [--step N]

      -> DIR/<slug>-step-01.png, -step-02.png, ... one per step up to the scene's highest step
         (the higher of any object's `step` and `steps.count`), or only step N with --step.

WHY. Map Studio (tools/mapstudio/) draws the series' best maps — shaded relief, rivers, army
banners, tapered campaign arrows, step-by-step build-ups — but it is a click-tool: a scene only
becomes a picture when somebody opens index.html, loads the JSON, steps through it and presses
Export. On evening 3 nobody did. The STOP B closing slide went to the lectern with its placeholder
still in it, and the scene sat in tools/mapstudio/scenes/ fully drawn and never seen. A scene that is
not rendered is a map the room never sees. This makes rendering part of the build, like the Line.

HOW. The studio's painter is already separate from its UI: data/*.js, src/proj.js, src/store.js,
src/tokens.js and src/render.js only define globals (MS_Proj, MS_Store, MS_Tokens, MS_Render), and
ui.js's own exportPNG is just "a canvas of STAGE_W*scale x STAGE_H*scale, wait for whenReady(), call
render()". So this writes a throwaway HTML page that loads exactly those scripts by absolute
file:/// URL (never ui.js or demo.js), inlines the scene, waits for the shaded relief AND the fonts
the painter asks for, renders each step, and writes canvas.toDataURL() into the DOM. Headless Chrome
dumps the DOM; the data URLs are decoded here. The PNG is therefore THE SAME DRAWING the browser tool
exports — same function, same projection, same marks — not a re-implementation of it.

Scale 1.2 is 1920 x 1080: plenty for a map that fills 60% of a projected 16:9 slide. Use 2.4 for 4K.

It fails loudly — a non-zero exit and the reason — when Chrome returns no image, rather than leaving
last week's PNG in place to be mistaken for this week's.
"""
import argparse
import base64
import glob
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

# a Windows console is cp1252: "→", "ؓ" and the Arabic in a progress line would crash the run
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(errors="replace")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STUDIO = os.path.join(ROOT, "tools", "mapstudio")
CHROME = os.environ.get("CHROME", r"C:\Program Files\Google\Chrome\Application\chrome.exe")

# The renderer only: the order index.html loads them in, minus demo.js and ui.js.
SCRIPTS = ["data/land.js", "data/relief.js", "data/water.js", "data/places.js",
           "src/proj.js", "src/store.js", "src/tokens.js", "src/render.js"]

PAGE = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>render_scene</title></head>
<body>
%(scripts)s
<script>
(function () {
  'use strict';
  var SCENE = %(scene)s;
  var STEPS = %(steps)s;          // [] = every step 1..maxStep
  var SCALE = %(scale)s;

  function out(id, text) {
    var pre = document.createElement('pre');
    pre.id = id;
    pre.textContent = text;
    document.body.appendChild(pre);
  }
  window.onerror = function (msg, src, line) { out('error', msg + ' @ ' + src + ':' + line); };

  function fontsFor(T, urdu) {
    // Every face render.js/tokens.js asks for, at the weights it asks for them.
    var faces = ['400 16px ', '600 16px ', '700 16px ', 'italic 600 16px '].map(function (w) {
      return w + T.SERIF;
    });
    if (urdu) faces.push('16px ' + T.NASTALIQ);
    return Promise.all(faces.map(function (f) {
      return document.fonts.load(f).catch(function () { return null; });
    })).then(function () { return document.fonts.ready; });
  }

  try {
    var P = MS_Proj, R = MS_Render, T = MS_Tokens;
    var store = new MS_Store.Store();
    store.load(SCENE);
    store.scene.steps.mode = 'upto';
    var max = store.maxStep();
    var steps = STEPS.length ? STEPS : Array.from({length: max}, function (_, i) { return i + 1; });

    Promise.all([R.whenReady(), fontsFor(T, store.scene.style.urduLabels !== false)])
      .then(function (res) {
        if (store.scene.style.relief !== false && !res[0]) throw new Error('shaded relief did not load');
        steps.forEach(function (n) {
          if (n < 1 || n > max) throw new Error('step ' + n + ' is outside 1..' + max);
          store.scene.steps.current = n;
          var c = document.createElement('canvas');
          c.width = Math.round(P.STAGE_W * SCALE);
          c.height = Math.round(P.STAGE_H * SCALE);
          R.render(c.getContext('2d'), store, {k: SCALE, showSelection: false, images: {}});
          out('step-' + String(n).padStart(2, '0'), c.toDataURL('image/png'));
        });
        out('done', String(max));
      })
      .catch(function (e) { out('error', String(e && e.stack || e)); });
  } catch (e) {
    out('error', String(e && e.stack || e));
  }
})();
</script>
</body></html>
"""

STEP_RE = re.compile(r'<pre id="step-(\d+)">data:image/png;base64,([A-Za-z0-9+/=]+)</pre>')
ERR_RE = re.compile(r'<pre id="error">(.*?)</pre>', re.S)


def _file_url(path):
    return "file:///" + os.path.abspath(path).replace("\\", "/")


def render(scene_path, out_dir, scale=1.2, step=None):
    """Render one scene. Returns the list of PNG paths written. Raises SystemExit on failure."""
    scene_path = os.path.abspath(scene_path)
    with open(scene_path, encoding="utf-8") as f:
        scene = json.load(f)
    slug = os.path.splitext(os.path.basename(scene_path))[0]

    if not os.path.exists(CHROME):
        raise SystemExit("render_scene: Chrome not found at %s (set CHROME to override)" % CHROME)

    # "</" inside an inline <script> would close it; JSON allows "<\/" for exactly this reason.
    scene_js = json.dumps(scene, ensure_ascii=False).replace("</", "<\\/")
    page_html = PAGE % {
        "scripts": "\n".join('<script src="%s"></script>' % _file_url(os.path.join(STUDIO, s))
                             for s in SCRIPTS),
        "scene": scene_js,
        "steps": json.dumps([int(step)] if step else []),
        "scale": repr(float(scale)),
    }

    work = tempfile.mkdtemp(prefix="render_scene_")
    try:
        page = os.path.join(work, slug + ".html")
        with open(page, "w", encoding="utf-8") as f:
            f.write(page_html)
        try:
            proc = subprocess.run(
                [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                 "--allow-file-access-from-files", "--no-first-run", "--no-default-browser-check",
                 "--user-data-dir=" + os.path.join(work, "profile"),
                 "--virtual-time-budget=30000", "--dump-dom", _file_url(page)],
                capture_output=True, timeout=240)
        except subprocess.TimeoutExpired:
            raise SystemExit("render_scene: %s: Chrome did not finish in 240 s. Nothing written." % slug)
    finally:
        shutil.rmtree(work, ignore_errors=True)

    dom = proc.stdout.decode("utf-8", "replace")
    err = ERR_RE.search(dom)
    if err:
        raise SystemExit("render_scene: %s: the page reported an error:\n%s"
                         % (slug, html.unescape(err.group(1))))
    found = STEP_RE.findall(dom)
    if not found:
        tail = proc.stderr.decode("utf-8", "replace").strip()[-800:]
        raise SystemExit("render_scene: %s: Chrome returned no image (exit %s). Nothing written.\n%s"
                         % (slug, proc.returncode, tail))
    if '<pre id="done">' not in dom:
        raise SystemExit("render_scene: %s: the render did not finish inside the time budget; "
                         "only %d step(s) came back. Nothing written." % (slug, len(found)))

    os.makedirs(out_dir, exist_ok=True)
    if not step:
        # a whole-scene render replaces the scene's step PNGs: a hand-nudge that removed a step must not
        # leave the old higher step behind for build.py's "all" to pick up
        for old in glob.glob(os.path.join(out_dir, slug + "-step-[0-9][0-9].*")):
            os.remove(old)
    written = []
    for n, b64 in found:
        path = os.path.join(out_dir, "%s-step-%02d.png" % (slug, int(n)))
        with open(path, "wb") as f:
            f.write(base64.b64decode(b64))
        written.append(path)
    return written


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("scenes", nargs="+", help="Map Studio scene .json file(s)")
    ap.add_argument("--out-dir", required=True, help="where the PNGs go")
    ap.add_argument("--scale", type=float, default=1.2, help="1.2 = 1920x1080 (default); 2.4 = 4K")
    ap.add_argument("--step", type=int, default=None, help="render only this step")
    a = ap.parse_args(argv)
    for s in a.scenes:
        paths = render(s, a.out_dir, a.scale, a.step)
        print("  %-40s %d PNG(s)" % (os.path.basename(s), len(paths)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
