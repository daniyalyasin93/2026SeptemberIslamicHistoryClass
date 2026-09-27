# Spec — evening 5, and the production pipeline v5

**Date:** 2026-09-27 · **Status:** ✅ approved by Daniyal ("now make the slides") and built the same day · **Supersedes:** in
`2026-09-06-L02-and-production-v4-spec.md`, the one-page cue sheet (§4), the worksheet beat, and the
in-place closing sets. Everything else in v4 stands.

**Decisions this spec implements:** `docs/DECISIONS.md` **#56–#61**. They carry the reasons; this file
carries the shapes. **The running order is `S05_yamama_dead_oman_mahra/RUNSHEET.md`** — this spec does not
repeat it.

---

## 0. Why v5 exists

Evening 4 was delivered to STOP D. Four things did not work (#56):

| What went wrong | Fixed by |
|---|---|
| A map was shown finished, then told on later slides | §2 — maps build up on clicks |
| The battle ended abruptly; the treaty's terms were on no card and in no notes | §5 — four new cards, and the next-question check |
| The mid-evening closes felt out of place, and their notes had nothing to say | §3 — checkpoints, and one real close |
| The cue sheet and briefing were never used — only the deck and its notes | §4 — the notes carry everything; one notes PDF for home |

---

## 1. Evening 5

**`S05_yamama_dead_oman_mahra/`.** How the day at al-Yamāma ended → the houses, told where their men fall →
Medina and the Qurʾān → ʿIkrima's ؓ road to Oman and Mahra (#57).

| Part | Cards | Budget | CORE |
|---|---|---|---|
| I · How the day ended | 2 (both new) | 4 | 4 |
| II · The man who opened the gate — the house of Umm Sulaym ؓ | 18 | 25 | 13.5 |
| ✓ Checkpoint 1 | | | |
| III · The men beside them | 6 | 9 | 4.5 |
| IV · The banner and the reciters — with the house of Abū Ḥudhayfa ؓ and Sālim ؓ | 21 | 32 | 22.5 |
| V · Medina | 5 (one new) | 9.5 | 9.5 |
| ✓ Checkpoint 2 | | | |
| VI · ʿIkrima's ؓ road: Oman and Mahra | 6 (one new) | 11 | 11 |
| The close | | | |
| **Total** | **58** | **90.5** | **65.5** |

**Suggested cut:** `✂` on 22 cards leaves 36, budgeted at 61 minutes — evening 4 as spoken was 34 cards
budgeted at 66. **The cut is Daniyal's**, made in the runsheet before the build.

**Opening:** the Line and the map from Daniyal's own STOP D (`S04_share.pptx` slides 64–65 — his images),
unchanged (#23). **Evening 6:** Bahrayn → Ḥaḍramawt from Kinda's kings → Ibn Kathīr's summing-up.

---

## 2. Maps that build up on clicks (#58)

### 2.1 What the room sees

One slide per map; it stays up while that part is told. **Each click is one beat:**

| Mark | On its click |
|---|---|
| Arrow | wipes on along its route, from the end it starts at |
| Army that follows an arrow | appears at the arrow's start and travels along it, arriving where it is drawn |
| Army, settlement, battle, label | fades in |
| Territory | fades in (a front turning green) |
| Anything with *Hide after step* | fades out on the click after its last step |

### 2.2 How it is built

1. **Map Studio** (`tools/mapstudio/`) — one optional field on an army: **`follows`**, the id of the arrow it
   travels along. Old scenes open unchanged. Saving from the studio keeps the field (verified, not assumed).
2. **`tools/render_scene.py --layers`** — for each scene, writes:
   - `<scene>-base.png`: terrain, water, underlay, settlements and territories present from step 1, legend,
     scale bar, the finish — everything that does not move;
   - `<scene>-<object id>.png` for every mark that arrives after step 1 (or leaves before the end): that mark
     alone, on a transparent ground, **cropped to its own box**;
   - `<scene>-layers.json`: for each layer, its box on the stage, its type, `step`, `until`, and — for an
     arrow — its direction of travel; for a `follows` army, its route in stage coordinates.
   The painter is the studio's own (`src/render.js`), given a *layer* mode that skips the ground and draws
   one object. Same drawing, same projection — never a re-implementation.
3. **`series/anim.py`** (new) — places the base and every layer on a slide at their exact boxes, and writes
   PowerPoint's click-animation timing XML (python-pptx has no API for it): one click group per step, the
   effect per §2.1, motion paths in slide-relative units from the manifest. Each layer is its own picture
   named for its object, so Daniyal can move one, or *Change Picture*, and the animation stays.
4. **The card's notes** carry `▶ CLICK n — …` on the beat where the map moves. **The build fails** if a map
   slide has more click groups than `▶ CLICK` marks in its notes, or fewer.

**Colours:** Muslim forces `#2CB020` on every map (#58); the revolt keeps the studio's ochre; undecided
ground its grey.

### 2.3 The maps of evening 5

M1 the day at ʿAqrabāʾ (the trial) · M2 the house of Umm Sulaym ؓ, a life's route · M3 Abū Ḥudhayfa ؓ and
Sālim ؓ · M4 ʿIkrima's ؓ road · M5 Dabā · M6 Mahra · M7 the checkpoints and the close. Their clicks are in
the runsheet's *The moving maps* table. A route map returns across its part, **one more leg each time**,
built from the same scene at later steps.

### 2.4 The trial, before anything else

M1 is built alone into a one-slide test deck, then:
1. opened in PowerPoint through COM — **no repair prompt**;
2. exported by PowerPoint itself to a short video (`CreateVideo`), and frames pulled with ffmpeg at each
   click — **each arrow is seen partly drawn, then whole; the banner is seen mid-route**;
3. shown to Daniyal. **No other map is built until he has seen it.**

**Fallback, decided now:** if a motion path misbehaves, that army fades in at its arrival point instead
(the arrow still wipes). If PowerPoint rejects the timing XML outright, the evening falls back to the
stage-by-stage option — the step pictures stacked, fading one into the next — which needs no new tooling.

---

## 3. Checkpoints and the close (#59)

**A checkpoint** — two slides in the flow, faces titled *Where we stand*:

| Slide | Face | Notes |
|---|---|---|
| The Line | the Line, tonight's events so far lit | **SAY** — two or three lines: where tonight began, where we are |
| The map | the map as it now stands | **SAY** — *"When you came in… now…"* · **⏱** the time check · **CARRYING ON** — one sentence into the next part · **OUT OF TIME** — three closing lines, next week's question, السلام علیکم, the dua |

Evening 5 has two: after #20 (⏱ *past 0:20 → drop every ✂ card from here*) and after #52 (⏱ *past 0:38 →
close here*). If the evening stops at one, **evening 6 opens on its two slides** (#23).

**The close** — four slides after #58: the Line · the map · «Tonight» (up to four headings; one lesson line
each in the notes) · «Next week» (the question on the face; the salaam and the dua in the notes). **Every
one of the four carries its spoken script in the notes.**

**Gone:** in-place four-slide closes mid-evening, hidden closes at the back, and typed slide numbers.

---

## 4. The notes pane, and the notes book (#60)

**Order of every slide's notes** — the eye meets them top down, mid-sentence:

```
⚠  one line, only if the card carries a warning
SAY —        the beats, numbered, with ▶ CLICK n where the map moves; the quotation's place marked
⏱            checkpoints only
QUOTE —      the Arabic, the rendering, the citation
عبرت —       the one line
HANDS UP —   only if the card has one
BACKGROUND — the card's prose and extras, for home
```

**Nothing else goes in the pane** — no file paths, steps, scene names or "rendered by". That traceability
lives in the runsheet. `tools/build_full_deck.notes_for()` is changed to this order for every evening
built from now on.

**The notes book** — `S05_notes.pdf`: each slide's picture with its full notes beneath it, one slide after
another; on a map slide, **the picture for each click sits beside its `▶ CLICK` line**. HTML → headless
Chrome → PDF, fonts embedded (the existing path), sized for a phone. It replaces `BRIEFING.pdf`.

**Retired:** `CUE.pdf`, `BRIEFING.pdf`, `WORKSHEET.pdf` (the worksheet assumption is reversible).

---

## 5. Content work before the build

1. **Four new cards**, in `docs/research/ridda-campaign-the-conduct-of-the-wars.md` (and the pool):
   `RC67` the terms at the forts · `RC68` to the last man · `RC69` the delegation at Medina, and Musaylima's
   words · `RC70` Oman asked for help. Every quotation copied from a cached page; `check_citations` silent.
2. **Beats** for `RC29`, `RC30`, `TRN6`, `TRN7`, `TRN8` and the new four — from each card's own text; no
   composition.
3. **The next-question check** (#61), card by card, into the runsheet's *Questions the room will ask* table.
4. **`ZY17`** gains ⁨الکامل ج۲ ص۲۱۸⁩'s figures beside Ibn Kathīr's, each with its book.
5. **Introductions** re-run once the new cards are in the pool.

---

## 6. Files and build order

```
S05_yamama_dead_oman_mahra/
  RUNSHEET.md       the running order — Daniyal cuts here
  make_maps.py      writes tools/mapstudio/scenes/s05-*.json (never make_scenes.py)
  timeline.json     the Line: date bands, a main lane for 12 AH, one lane per house
  make_timeline.py  → visuals/line_s05_*.png
  build.py          → S05.pptx + S05.pdf   (bridges, map slides with clicks, checkpoints, the close)
  notes_book.py     → S05_notes.pdf
```

Rebuild order: `make_timeline.py` → `make_maps.py` (renders layers) → `build.py` → `notes_book.py`.

---

## 7. Gates

| Gate | Passes when |
|---|---|
| `tools/check_citations.py` | 0 problems |
| `tools/check_introductions.py S05_yamama_dead_oman_mahra` | 0 unanswered |
| `check_face_quotes` (inside the build) | every face excerpt is the card's own words |
| `deck2.audit()` (inside the build) | no apparatus on any slide face |
| click marks (inside the build) | every map slide: click groups = `▶ CLICK` marks |
| the animation trial (§2.4) | video frames show the moves, and Daniyal has seen M1 |
| `series/preview.py` contact sheet | looked at before the deck is called finished |

---

## 8. Open, for Daniyal

1. **The cut** — `✂` in the runsheet is a suggestion.
2. **`RC49`** (ʿUmar ؓ in the mosque) was hidden in his evening-4 deck — was it told?
3. **The green** — `#2CB020`, or darker.
4. **The worksheet** — dropped unless he says the room has used it.
5. **His `S04.pptx`** is not on this machine; the opening pair is taken from `S04_share.pptx`, which carries
   his images recompressed. If he wants the originals, the file goes back in `S04_kinda_butah_yamama/`.

---

## 9. The second pass — 2026-09-27 (`DECISIONS.md` #62–#66)

Daniyal saw the first build and asked for four changes, then three more. What changed, and where it lives:

| Change | Where |
|---|---|
| **One flashback per man** — the houses cut from 16 + 16 cards to 5 + 9 | the runsheet, Parts II and IV; the moved cards listed under *Moved out on the second pass* |
| **A moving card's map is its slide** — beats in the map's notes with `▶ CLICK n` on the beat; a words slide after it when the card quotes Arabic | `build.py` — `MAP_FOR`, `map_card_notes()`, `words_notes()`; the one recap map stays as `RECAP_BEFORE` |
| **Maps fade what a click has finished with; the road stays** | `make_maps.py` — `until` on captions, spent arrows, marks and banners |
| **A family tree opens each house** — names and lines on the face, one sourced sentence per person in the notes, the cut cards' beats in BACKGROUND | `build.py` — `TREES`, `family_tree()`; every line cited in the runsheet's tree table |
| **The Qurʾān's collection told whole** | Part V: `ZY17` → `Q7` → `RC65` → `Q3` → `Q4` → `Q5` → `RC37`; the jamʿ cards given beats |
| **Ḥaḍramawt and Kinda as Part VII** — the end of ʿIkrima's ؓ road | Part VII; one new scene, `s05-10-kinda`, sixteen steps over six card slides |
| **Nothing researched lost** | §8's details carded; `RC37` and `Q5` corrected; `TRN7`'s new line; the trees' BACKGROUND |

**Shape now:** 51 cards, seven parts, 95 slides: 14 maps (38 clicks), 13 words slides, 4 trees, 6 bridges, three
checkpoints (after `RC37`, `RC30`, `YK12`) and the close (after `PG41`, its map drawing ʿIkrima's ؓ whole road).
**Pace:** at evening 4's 34 cards, the evening closes at Checkpoint 1. The runsheet names six cards to strike to
reach Mahra.
