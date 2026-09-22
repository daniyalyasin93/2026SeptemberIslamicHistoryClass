# STATUS — read this first, every session

> **2026-09-22 · RESUME POINT — read this first. Evening 4 is BUILT and ready to deliver.**
> `S04_kinda_butah_yamama/`, Daniyal's cut **Parts I–IV to STOP C** (`DECISIONS.md` #44): 31 cards —
> **with Parts V and VI built behind that close as overflow** (#47, #48): 12 more cards, ~22 more minutes,
> ending on the collection of the Qurʾān. Stopping at STOP C needs no jump; going on is one typed number.
>
> | Artifact | State |
> |---|---|
> | `S04.pptx` + `S04.pdf` | **85 slides** (77 visible), 43 cards. Bookend IN = evening 3's STOP B pair. **7 bridge slides** at the story's seams (#45). **STOP C, the planned end, at 52–55**; Part V at **56–63**, Part VI at **64–73**; **STOP D at 74–77**. STOP A hidden at **78**, STOP B at **82** — type the number and Enter. The PDF includes the hidden slides, so its page n is slide n |
> | Maps | 11 scenes `tools/mapstudio/scenes/s04-*`, **rendered by `make_maps.py`** through `tools/render_scene.py` (headless) and placed as JPEGs. Renders are git-ignored; re-run to regenerate |
> | The Line | `timeline.json` → `make_timeline.py` → `visuals/line_s04_stop_a/b/c.png`. The opening Line is evening 3's own image, byte for byte |
> | `CUE.pdf` | one page, 11.0pt, 24 beats, jump numbers read from the deck. The overflow beats print dense (`.beat.over`) so carrying them does not shrink the planned evening's type |
> | `WORKSHEET.pdf` | 2 pages; nothing on it the room has not heard by STOP B |
> | `BRIEFING.pdf` | 71 pages: the evening, the bridges, the early closes, Part VI, Part II's guardrail, the never-do list, then all 43 cards |
>
> **Rebuild order:** `make_timeline.py` → `make_maps.py` → `build.py` → `pack_data.py` (all in
> `S04_kinda_butah_yamama/`). Gates, all clean: `tools/check_citations.py` (4,705 / 0),
> `tools/check_introductions.py S04_kinda_butah_yamama` (0 unanswered), `check_face_quotes` inside the build.
>
> **What the review changed** (#46): authored face excerpts instead of a blind 24-word cut; #11 as the four
> accounts side by side; spoilers out of the speaker's lines; «⁨يا محمداه⁩» off the face (**`QA_BANK.md`
> §6.11 — Tanzeem-e-Islami to review**); no "a later caliph"; notices for ʿIkrima ؓ and Shuraḥbīl ؓ;
> the introductions gate now sees Ḥ/Ḍ/Ṣ-initial names and names after Abū/Banū/Umm.
>
> **Daniyal's, before the evening:** (1) look through `S04.pdf` once; (2) decide Umm Tamīm's honorific
> (ؓ on `RC17` and the cue, none on `RC16` — no page settles it); (3) the ؓ-as-detached-mark look on English
> faces is still his call from evening 3; (4) `L02_baarah_saal/L02_ALL_DY.pptx` is modified to **128 MB** in
> the working tree — over GitHub's 100 MB limit: keep it out of any commit. **After the evening:** replace
> the evening-4 block in `DELIVERED.md` with the cards actually spoken — **and say which ending was used**,
> since Part V may or may not have been reached. Evening 5 opens on the closing pair of whichever stop was
> used, and carries Ḥaḍramawt/Kinda, which is still last (#42).

> **2026-09-19 (later) · RESUME POINT — read this first.** Evening 4 was **reviewed for content gaps and
> then restructured into CHRONOLOGICAL order** (`DECISIONS.md` #42): **the two claimants → al-Buṭāḥ →
> the road to al-Yamāma → the day begins → Ḥaḍramawt/Kinda last**, which is the sequence §12.2 of the
> campaign note establishes. `S04_kinda_butah_yamama/`: **51 cards in six parts, ≈ 89 min**, four
> stopping points, **`S04.pptx` = 89 slides** (12 hidden). The recommended cut is **Parts I–III to
> STOP B** — the armies in position and Mujjāʿa in irons in Khālid's ؓ tent.
>
> **⚠ The price of chronological order, and it is stated at the top of the runsheet:** Ḥaḍramawt/Kinda
> now sits at the end of ~80 minutes and **will not be reached on evening 4** — a third deferral. If
> Kinda must be spoken next, Part V moves back to the front and #42 is superseded.
>
> **The review found twelve gaps; all are closed.** Five men carried cards with no ⁨تراجم⁩ notice
> anywhere in the delivered series — **al-Ashʿath b. Qays** now has a card of his own (`TSY/E-YK19`,
> never cut), **Ziyād b. Labīd ؓ** a first beat on `TSY/E-YK07`, and **Thābit b. Qays ؓ**
> (⁨خطيب الأنصار⁩) and **Abū Qatāda ؓ** (⁨فارس رسول الله ﷺ⁩) their ⁨سیر⁩ notices, from the only two pages
> fetched for this pass. Two events were on no card and now are: **`RCT/E-RC63`**, the hinge that
> carries the army out of the mosque at Medina onto the road to al-Yamāma, and **`RCT/E-RC64`**,
> the Muslims of Banū Ḥanīfa already fighting Musaylima before any army arrived. `RCT/E-RC52` no
> longer spends al-Yamāma's grief a week early; `TSY/E-YK16` and `KTK/E-KD07` now frame their forward
> references; `TSY/E-YK08` carries a ⚠ that ⁨البسوس⁩ is **not page-cited here** and must be verified
> before it is spoken as fact; and `POT/E-PG40`/`PG41` no longer mix Arabic-script names into English
> prose. The **Umm Tamīm ؓ** finding is recorded and deliberately not spoken (#41), with a prepared
> answer at `QA_BANK.md` §6.9 (renumbered 2026-09-22 — it had been filed as a second §6.3). Pool **444 cards**; citations **4,703 / 0 problems**.
>
> **New standing gate (`CLAUDE.md` §2, `DECISIONS.md` #43):**
> `python tools/check_introductions.py SNN_<slug>` — walks an evening's runsheet in running order and
> reports every proper name appearing **for the first time in the series**. The runsheet answers each
> row in a `## Introductions checked` table; the tool exits non-zero while a row is unanswered, and
> **"no notice needed" is a valid answer**. Evening 4's table has **69 rows, all answered**. Ask the
> same question of **events, terms and forward references**, not only people — the evening-4 review
> caught one of each. **Run it on every evening before the deck is built.**
>
> **What evening 4 still needed — ALL DONE 2026-09-22, see the resume point above:**
> 1. `S04.pdf` — the build cannot write it in the container (no PowerShell/Chrome). Re-run
>    `python S04_kinda_butah_yamama/build.py` on Windows and it appears beside the deck.
> 2. **The Line images** — `visuals/line_s04_open.png` and `line_s04_stop_a/b/c/d.png`. Adapt
>    `S03_yemen/make_timeline.py` + `timeline.json`; until then those five slides show placeholders.
> 3. **Thirteen Map Studio scenes** (`s04-00`…`s04-11`) — briefs are in the slide notes and `IMAGE_BRIEFS.md`.
> 4. **`CUE.pdf`, `WORKSHEET.pdf`, `BRIEFING.pdf`** — adapt `S03_yemen/pack_data.py`, **after** the cut
>    is fixed, so the cue sheet is one page for the evening actually being given.

> **2026-09-17 · RESUME POINT — read this first.** **Evening 3's deck is FINAL** (`DECISIONS.md` #38): Daniyal's
> hand-finished `S03_yemen/S03.pptx` (356 slides, 13 hidden, maps placed) — 131 MB, kept local, **locked** by
> `S03_yemen/S03.FINAL` so `build.py` writes `S03_rebuild.pptx` instead. In git: `S03_repo.pptx` (maps at 1920 px,
> 26.8 MB) and `S03.pdf` (343 pp., from the final deck). The recap set "The story so far" is `S03_recap.pptx`
> (16 slides, pasted in at slide 238). **Next:** deliver evening 3; then replace its `DELIVERED.md` row with the
> cards actually spoken, and plan evening 4 from wherever it stopped (Part III and the Kinda kingship backstory
> are next in line if not reached; then Musaylima, Sajāḥ and al-Yamāma).
>
> **2026-09-16 (night) · RESUME POINT — read this first.** Evening 3 (`S03_yemen/`) is rebuilt **one slide per
> event** (`DECISIONS.md` #37): 45 cards carry Beats → **361 slides** (282 beat slides; STOP C at 350–353; STOP A/B
> closes hidden at 354–361). A four-lens review + verify + fix pass ran overnight (73 confirmed, 61 applied).
> Citations 4,669/0. **Daniyal to decide in the morning:** (1) slide 245 — the ﷿ ligature box on RC32's Arabic;
> (2) how ؓ should look on English slide faces (shows as a small detached mark; fix belongs in `series/deck2.py`);
> (3) two headlines wrap to two lines (slides 147, 248); (4) fill 21 image boxes — 20 Map Studio exports + the
> floor plan (slide 113). Rebuild order: `make_timeline.py` → `make_maps.py` → `build.py` → `pack_data.py` →
> `series/preview.py S03_yemen/S03.pptx` → `review_dump.py`.
>
> **2026-09-16 · RESUME POINT.** **Evening 3 is BUILT** (`S03_yemen/`, `DECISIONS.md` #34): Daniyal cut
> it to Parts I–II (al-Aswad + the second Yemen ⁨ردة⁩); Kinda rolls forward. `S03.pptx`/`.pdf` (50 slides),
> `CUE.pdf` (one page, 13pt), `WORKSHEET.pdf`, `BRIEFING.pdf`, 9 Map Studio scenes (`s03-*`), 3 Line images.
> **Re-carded the same day (`DECISIONS.md` #35), and Part III — Ḥaḍramawt/Kinda — put back (#36):** 45 cards /
> 75 slides, to STOP C; speaker notes carry every card in full. Only the Kinda kingship backstory is rolled forward.
> **Daniyal's to-do before the evening:** export the map scenes into the 12 marked placeholders; the
> floor-plan diagram (Gemini brief in `IMAGE_BRIEFS.md`); decide the ﷿ box on the RC32 slide. Rebuild order:
> `make_timeline.py` → `make_maps.py` → `build.py` → `pack_data.py`.
>
> **2026-09-13 (later) · earlier resume point.** **Evening 2 was
> delivered** from `L02_baarah_saal/L02_ALL_DY.pptx` and stopped after **⁨بزاخة⁩** (37 min, ran short).
> The folders are now **era pools**, and evenings are numbered deliveries (`DECISIONS.md` #33). Where the
> story has reached lives in `docs/catalogue/DELIVERED.md`. **Evening 3 = Yemen, start to end:**
> `S03_yemen/RUNSHEET.md` has 47 cards in order (≈93 min, ≈62 CORE) with three stopping points, and
> **awaits Daniyal's cut**. Three new notes (al-Aswad · second Yemen ⁨ردة⁩ + Kinda · Kinda backstory,
> 43 cards) are in the 11–23 pool; citations 4,581/0 problems. **Next:** after the cut, build
> SLIDES → deck → cue → briefing → worksheet into `S03_yemen/`.
>
> *(Earlier the same day:)* **Session 3 («⁨پہلا امتحان⁩», ۲۳–⁨۴۱ھ⁩) is researched in full** — 23
> page-cited notes, **1,459 event cards** in `L03_pehla_imtihan/CONTENT.md`. Read
> `docs/research/READING_ORDER.md` before the notes; it declares the order to read them in, which is
> deliberately not the order the evening tells them. Session 1 was delivered; session 2 is built.
> The date of the next session is **still not set**.

---

## 0. Where to pick up (2026-09-13)

**Session 3 — done and committed. Do not redo any of it.**

| | |
|---|---|
| Sources | **1,569 Shamela pages** cached for ۲۳–⁨۴۱ھ⁩ — ⁨البدایہ⁩ 30097 · ⁨الکامل⁩ 21712 · ⁨سیر⁩ 10906 · ⁨ابن خلدون⁩ 12320. Logged chapter by chapter in `docs/catalogue/SHAMELA_LOG.md` |
| Notes | **23**, in `docs/research/`, each ending in a machine-parsable `## EVENT CARDS` section |
| Pool | `L03_pehla_imtihan/CONTENT.md` — **1,459 cards** (802 CORE · 615 GOOD · 42 CUT), ≈2,568 minutes of material for a 45-minute slot |
| Citations | **4,410 quotations across every note in the repo: 0 problems** (`python tools/check_citations.py`) |
| Card structure | 1,459 cards, 2 problems (`python tools/check_cards.py L03_pehla_imtihan`) |
| Reading order | `docs/research/READING_ORDER.md`; numbered PDFs in `docs/research/read/` (git-ignored, rebuild with `python tools/reading_order.py --pdf`) |
| Catalogue | `LESSONS.md` 1,834 lines · `TIMELINE.md` 1,423 lines, both regenerated from both pools |
| QA | `docs/catalogue/QA_BANK.md` extended with 20 session-3 questions — the ones this window actually invites |

**What is NOT done for session 3.** No deck, no cue sheet, no briefing, no worksheet. The pool is
the deliverable so far; the six per-session artifacts (spec v4 §1) have not been built, and
**Daniyal has not yet cut the pool** — that cut is the next decision, and it is his.

**New tooling, all of it free to run:**

| Tool | Does |
|---|---|
| `tools/check_citations.py` | every Arabic quotation vs. the cached page it cites. **No note is finished until this is silent** (`DECISIONS.md` #32) |
| `tools/check_cards.py` | card fields, tiers, certainty labels, duplicate ids, apparatus leaking into a spoken narrative |
| `tools/bidi_fix.py` | wraps inline Arabic in U+2068/U+2069 so a Markdown preview stops scrambling mixed lines. Stripped again by `build_content.py` |
| `tools/reading_order.py` | `READING_ORDER.md` + numbered PDFs |

**⚠ Open, and it matters: the 11–23 AH notes were repaired, not re-verified by eye.** The checker
found 115 defects in them — quotations on no cached page, quotations running past the page cited,
wrong printed pages, one citation resting on ⁨الطبری⁩ alone. All are now cleared, but
`L02_ALL.pptx` was built **before** that, so **the deck still carries the old citations**. Rebuild
it from the corrected `CONTENT.md` before session 2 is delivered.

## 1. Where the series stands

| | |
|---|---|
| **Sessions delivered** | **1, 2 and 3** — see `docs/catalogue/DELIVERED.md` (evening 2 stopped after ⁨بزاخة⁩; evening 3 did not reach Part III, Ḥaḍramawt/Kinda) |
| **Next session date** | ⬜ **NOT SET** — needed for the print deadline and the build plan |
| **Session 1 status** | being **rebuilt** to the v3 shape (see `docs/specs/2026-09-03-L01-v3-spec.md`) |
| **Session 2 status** | built to the v2 shape, opens on the ⁨ردة⁩ — **still correct**, unaffected by the v3 rebuild |
| **Session 3 status** | **researched in full** (1,459 cards). No artifacts built yet; the pool awaits Daniyal's cut |
| **Sessions 4–10** | not started |

## 2. What is built, and where

| Artifact | Path | State |
|---|---|---|
| Series design (v2) | `docs/specs/2026-08-26-lessons-from-history-v2-design.md` | current for sessions 2–10 |
| Session 1 spec (v3) | `docs/specs/2026-09-03-L01-v3-spec.md` | **current for session 1** — supersedes the v2 session-1 row |
| Session 1 deck | `L01_overview/build.py` → **`L01_NEW.pptx`** | ✅ **26 slides, v3.** ⚠️ written as `L01_NEW.pptx` because PowerPoint held `L01.pptx` open — **close PowerPoint, delete the old `L01.pptx` and `~$L01.pptx`, rename `L01_NEW.pptx` → `L01.pptx`** |
| Session 1 cue card | `L01_overview/CueCard.md` | ✅ rebuilt to v3 |
| Session 1 drill | `L01_overview/DRILL.md` | ✅ rebuilt to v3, 15 questions incl. hostile |
| Session 1 handout | `series/handout_l01.html` → `.pdf` | ✅ 4 sides, fonts embedded |
| **Session 1 speaker script** | `L01_overview/Script.md` | ⬜ **NOT WRITTEN — still the old v2 session. This is the biggest remaining gap** |
| **Session 1 briefing** | `L01_overview/BRIEFING.md` | ⬜ **NOT WRITTEN** |
| Session 1 visuals | `series/make_l01_visuals.py` | ✅ 6 PNGs — 3 timelines, the stack, chart + blank |
| Font embedding | `series/embed_fonts.py` | ✅ new — base64 @font-face + A4 PDF render |
| Session 2 artifacts | `L02_baarah_saal/` | built, v2 shape |
| Speaker primer | `docs/PRIMER.md` | written |
| The Line + base map | `series/`, `series/visuals/` | built; regenerate with `python series/make_visuals.py` |
| Week-1 handout | `series/handout_w1.html` → `.pdf` | built to the v2 session 1 — **needs revising for v3** |
| Prospectus | `series/prospectus.html` → `.pdf` | built |
| Map editor | `tools/mapstudio/` | built; offline, double-click `index.html` |
| Ridda teaching artifacts | `tools/ridda-classification.html`, `tools/ridda-wars-map (1).html` | belong to session 2 |
| **Superseded v1 work** | `Lecture1/`, `Lecture2/`, `archive/` | **parts bin only.** Do not build on these |

## 3. Sources — what is usable *right now*

**Usable today:**

| Source | Path / access | Covers |
|---|---|---|
| *⁨تاریخِ امت⁩*, vol 1 — ⁨المقدمہ⁩ | `sources/text/TUM_v1_muqaddima.txt` | printed pp.۳۲–۷۸ |
| *⁨تاریخِ امت⁩*, vol 1 — ⁨خلافتِ راشدہ⁩ opening | `sources/text/TUM_v1_abubakr.txt` | printed pp.۴۵۶–۴۶۵ |
| ⁨البدایہ والنہایہ⁩ (⁨ابن كثير⁩) | Shamela **30097** via `tools/shamela.py` | everything |
| ⁨سیر أعلام النبلاء⁩ (⁨الذہبی⁩) | Shamela **10906** | everything |
| ⁨الکامل⁩ (⁨ابن الأثیر⁩) | Shamela **21712** | to ⁨۶۲۸ھ⁩ |
| ⁨الإعلان بالتوبيخ⁩ (⁨السخاوی⁩) | Shamela **34** | ⁨فوائد التاریخ⁩ from printed p.۱۱۱ |

**NOT usable — do not plan around these:**

- `sources/pdf/Tareekh e Ummat e Muslima … 2/3/4.pdf` — **no usable text layer. Daniyal must OCR
  these himself and has not yet.** Confirmed 2026-09-03. Assume they do not exist until he says so.
- `sources/pdf/*_text.pdf` (00–25in, jm) — these are **scans of ⁨سیر أعلام النبلاء⁩** with a badly
  garbled Arabic OCR layer. **Use Shamela 10906 instead** — it is typed, clean and page-accurate.
  These PDFs are only useful for eyeballing a page image.

**Consequence:** every session from 2 onward that needs the Urdu spine is blocked on Daniyal's OCR.
Sessions can still be built from the Arabic (Shamela) spine, which is inside the course's own frame.

## 4. The Shamela path — cost-saving notes

Cached TOCs already exist and should be **grepped before any fetch**:

```
sources/shamela/30097/_toc.tsv    3279 lines   index<TAB>chapter title
sources/shamela/10906/_toc.tsv    6157 lines
```

Chapter indices already located (saves the hunt):

| What | Book | Shamela index |
|---|---|---|
| مرض النبي ﷺ ووفاته | 30097 | 2495 · 2516 |
| أمور مهمة بعد وفاته ﷺ وقبل دفنه | 30097 | 2527 |
| **قصة سقيفة بني ساعدة** | 30097 | **2528** |
| اعتراف سعد بن عبادة ؓ | 30097 | 2531 |
| وقت الوفاة ومبلغ سنه ﷺ | 30097 | 2542 |
| ذكر ما أصاب المسلمين بوفاته ﷺ | 30097 | 2572 |
| الردة / ألوية الأمراء الأحد عشر | 30097 | 3163–3186 · 3231–3241 · 3278–3286 |
| أبو بكر الصديق ؓ | 10906 | 1155 |
| سهيل بن عمرو ؓ | 10906 | 1620 |
| سعد بن عبادة ؓ | 10906 | 1696 |
| ثابت بن قيس بن شماس ؓ | 10906 | 1734 |
| معاذ بن جبل ؓ | 10906 | 1869 |
| النعمان بن بشير ؓ | 10906 | 3019 |
| ⁨فوائد التاريخ⁩ (⁨السخاوي⁩) | 34 | 110 (= printed p.۱۱۱) |

`tools/shamela.py` caches to `sources/shamela/<book>/<index>.txt`. **A page fetched once is free
forever — check the cache before fetching.** The file header reports the printed ⁨ج⁩/⁨ص⁩; **cite that,
never the index.**

## 5. Blocked / open

| # | Open item | Blocks | Owner |
|---|---|---|---|
| 1 | **New session-1 date** | print deadline, whole build plan | Daniyal |
| 2 | **OCR of *⁨تاریخِ امت⁩* vols 2–4** (and the rest of vol 1) | sessions 3–7 Urdu spine | Daniyal |
| 3 | Headcount | print quantities | Daniyal |
| 4 | Karbala depth and framing | session 4 | conversation needed |
| 5 | South Asia source — does *⁨تاریخِ امت⁩* reach it? | sessions 8–9 | check on OCR |
| 6 | Sunan Ibn Majah number for «⁨إِذَا لَمْ تَسْتَحْيِ فَاصْنَعْ مَا شِئْتَ⁩»; Bukhari chapter for the hadith of the nations before us | `IBRAH.md` | both marked *(to verify)* — **may not be quoted with a number until checked** |

## 6. The next three things to do

1. **Write `L01_overview/Script.md`** — the full Urdu speaker script to the v3 spec. Everything
   else for session 1 exists; this is what is missing to deliver. Build it from
   `docs/research/*` + the deck's speaker notes (which already carry the timings and citations).
2. **Write `L01_overview/BRIEFING.md`** — the pre-session study pack.
3. Close PowerPoint and promote `L01_NEW.pptx` → `L01.pptx` (see §2).
4. Get the new session-1 date; update `CLAUDE.md`, this file, and the spec.
5. Build the labelled governors map in `tools/mapstudio` — slide 23 currently reuses the blank
   Arabia base.
