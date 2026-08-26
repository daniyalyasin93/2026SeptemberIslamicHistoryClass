# Maps Workflow — getting good maps into the decks

You have two reliable ways to get a map onto a slide. Both end with `insert_map.py`.

## Tooling (in this `tools/` folder)
- **`grab_frame.py`** — pulls one still frame from a YouTube map/animation video (yt-dlp downloads ~2s, ffmpeg extracts the frame).
- **`insert_map.py`** — drops any image into a chosen slide, fitted to a box (aspect ratio preserved). Re-runnable; writes a `.bak`.

Both are plain CLI scripts. Run them from the `tools/` folder.

---

## Path A — a static map (cleanest, recommended for most slides)
1. Download a map image into `../maps/`. Good free, citable sources:
   - **Wikimedia Commons** — search terms that reliably return usable historical maps:
     `"Sasanian Empire 620"`, `"Byzantine Empire 600"`, `"Rashidun Caliphate map"`,
     `"Age of the Caliphs"`, `"Umayyad Caliphate 750"`, `"Abbasid Caliphate 850"`,
     `"Mongol invasions map"`, `"Al-Andalus map"`.
     The widely-used green Caliphate-expansion series on Commons (often credited to user "Mohammad adil")
     is a solid starting point. **Always open the file page, confirm the licence allows your use, and
     confirm the map's accuracy before you rely on it** — never present a map as something it isn't.
   - **Your own annotation:** drop a blank base map and add city dots yourself in PowerPoint.
2. Insert it:
   ```
   python insert_map.py --deck ../Lecture1/Lecture1.pptx --slide 15 --image ../maps/world_632ce.png
   ```
3. Open the deck in PowerPoint; if the grey "INSERT MAP HERE" placeholder still peeks out, click it and
   delete it (or Send to Back). Add city labels (Makkah, Madina, Dimashq, Kufa, Córdoba…) as text boxes.

## Path B — a frame from a Kings & Generals (or similar) video
1. Find the moment you want (note the timestamp, e.g. 12:34).
2. Grab it:
   ```
   python grab_frame.py --url "https://youtu.be/VIDEO_ID" --time 12:34 --out ../maps/conquests_umar.png
   ```
3. Insert as in Path A. (For a closed lecture hall this is normally fine; check the video licence before
   any public/online redistribution, and credit the channel in your `..._Sources` slide.)

---

## Which slide takes a map? (the `--slide` numbers)
- **Lecture 1, slide 15** — world c. 11 AH: Byzantine Rome + Sasanian Persia + the Hijaz (placeholder ready).
- As later lectures are built, each map slide will carry a placeholder and a note telling you the slide number.

## Box presets (only if you want to override the default placeholder area)
Default box = `--x 0.7 --y 1.5 --w 8.4 --h 5.4` (matches the Lecture-1 placeholder). For a full-bleed map use
`--x 0.4 --y 1.3 --w 12.5 --h 5.8`.

## Reminder
Per project rule (memory: *references must be airtight*): cite the actual source of every map on your Sources
slide, and never attribute a map/frame to a source it didn't come from.
