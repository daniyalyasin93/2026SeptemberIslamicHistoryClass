# -*- coding: utf-8 -*-
"""Evening 6 — the Line, rendered checkpoint by checkpoint.

    python S06_hadramawt_bahrayn/make_timeline.py
      -> S06_hadramawt_bahrayn/visuals/line_s06_cp1.png … cp4, and line_s06_close.png

The drawing is evening 5's, unchanged: its layout, its styles and its checks. Only the data differs, and
it lives in this folder's timeline.json. Importing the module rather than copying it means the two evenings
cannot drift apart in how the Line is drawn — which is the whole point of a bookend (DECISIONS.md #23).
"""
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

_spec = importlib.util.spec_from_file_location(
    "s05_timeline", os.path.join(ROOT, "S05_yamama_dead_oman_mahra", "make_timeline.py"))
T5 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(T5)

# the renderer reads and writes relative to its own folder; point both at this one
T5.HERE = HERE
T5.OUT = os.path.join(HERE, "visuals")
if hasattr(T5, "DATA"):
    T5.DATA = os.path.join(HERE, "timeline.json")

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(errors="replace")

if __name__ == "__main__":
    os.makedirs(T5.OUT, exist_ok=True)
    only = sys.argv[1] if len(sys.argv) > 1 else None
    T5.build(only=only) if only else T5.build()
