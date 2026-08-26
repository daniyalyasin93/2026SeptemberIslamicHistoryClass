# -*- coding: utf-8 -*-
"""
grab_frame.py — pull a single still frame from a YouTube video at a timestamp.
Uses yt-dlp (downloads only a ~2s section) + ffmpeg (extracts the frame). Both must be on PATH.

Examples:
  python grab_frame.py --url "https://youtu.be/XXXX" --time 12:34 --out ../maps/conquests.png
  python grab_frame.py --url "https://youtu.be/XXXX" --time 754 --dur 1 --height 720 --out frame.png

Use this for Kings & Generals / map-animation videos. CHECK the video's licence before reusing
frames publicly; for a private lecture in a hall this is normally fine, but never claim a frame is
from a source it isn't (see memory: references-must-be-airtight).
"""
import argparse, os, subprocess, sys, tempfile, glob, shutil

def parse_ts(s):
    parts = str(s).split(":")
    if not all(p.strip().isdigit() for p in parts):
        sys.exit(f"Bad --time '{s}'. Use seconds (754) or H:M:S (12:34 / 1:02:03).")
    sec = 0
    for p in parts:
        sec = sec * 60 + int(p)
    return sec

def run(cmd):
    print("+", " ".join(str(c) for c in cmd))
    r = subprocess.run(cmd)
    if r.returncode != 0:
        sys.exit(f"Command failed ({r.returncode}): {cmd[0]}")

def main():
    ap = argparse.ArgumentParser(description="Grab one still frame from a YouTube video.")
    ap.add_argument("--url", required=True)
    ap.add_argument("--time", required=True, help="timestamp: seconds or H:M:S")
    ap.add_argument("--out", required=True, help="output image path (.png/.jpg)")
    ap.add_argument("--dur", type=int, default=2, help="seconds of section to fetch (default 2)")
    ap.add_argument("--height", type=int, default=1080, help="max video height (default 1080)")
    ap.add_argument("--keep-clip", action="store_true")
    a = ap.parse_args()

    start = parse_ts(a.time)
    end = start + max(1, a.dur)
    out = os.path.abspath(a.out)
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    tmp = tempfile.mkdtemp(prefix="grabframe_")
    try:
        clip_tmpl = os.path.join(tmp, "clip.%(ext)s")
        run(["yt-dlp",
             "-f", f"bestvideo[height<={a.height}]/best[height<={a.height}]/best",
             "--download-sections", f"*{start}-{end}",
             "--force-keyframes-at-cuts",
             "-o", clip_tmpl, a.url])
        clips = [f for f in glob.glob(os.path.join(tmp, "clip.*")) if not f.endswith(".part")]
        if not clips:
            sys.exit("yt-dlp produced no clip — check the URL / network.")
        clip = clips[0]
        # first frame of the fetched section == the requested timestamp
        run(["ffmpeg", "-y", "-i", clip, "-frames:v", "1", "-q:v", "2", out])
        print("\nSaved frame ->", out)
        print("Next: insert it into a slide, e.g.")
        print(f'  python insert_map.py --deck ../Lecture1/Lecture1.pptx --slide 15 --image "{out}"')
        if a.keep_clip:
            dest = os.path.splitext(out)[0] + os.path.splitext(clip)[1]
            shutil.copy(clip, dest); print("Kept clip ->", dest)
    finally:
        if not a.keep_clip:
            shutil.rmtree(tmp, ignore_errors=True)

if __name__ == "__main__":
    main()
