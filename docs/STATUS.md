# STATUS — read this first, every session

> **2026-09-06 · RESUME POINT.** Session 1 has been **delivered**. The feedback from it rewrote how
> this repo produces a lecture — see `docs/DECISIONS.md` **#19–#29** and
> `docs/specs/2026-09-06-L02-and-production-v4-spec.md`. **Read those two before anything else.**
> Work is now on **session 2 (11–23 AH)**. If this session ended at a token limit, the "Where to
> pick up" block below says exactly where.

---

## 0. Where to pick up (2026-09-06)

**Done and committed — do not redo any of this:**

| | |
|---|---|
| `43a4235` | session 1 exactly as delivered (`L01_DY.pptx`, script, three research notes) |
| `52e323c` | production pipeline **v4** — DECISIONS #19–28, the L02 spec, `CLAUDE.md` rewritten |
| `ec1ec88` | `tools/render_note.py` — research notes → readable A4 PDF, Arabic in Naskh at reading size |
| `9de326e` | `series/deck2.py` (the deck contract, enforced) + `series/preview.py` (deck → PNG contact sheet) |
| `ef33547` | `series/pack.py` (cue sheet / briefing / worksheet) + DECISIONS #29 (Ibn Khaldūn) |

**The tooling is finished.** All six per-session artifacts can now be produced. What remains for
session 2 is **content**, not code.

**Raw sources are cached, so re-fetching costs nothing.** This was done deliberately in one sweep
so that a token limit cannot strand the work:

| Book | id | Pages cached | Covers |
|---|---|---|---|
| البدایہ والنہایہ | `30097` | ~515 | the whole window and more |
| سیر أعلام النبلاء | `10906` | ~279 | the تراجم |
| الکامل فی التاریخ | `21712` | ~178 | year-by-year |
| **تاریخ ابن خلدون** | `12320` | **1276–1370** | أسامة · السقيفة · the ردة · Iraq · Shām · قادسية · المدائن · بيت المقدس · عام الرمادة · طاعون عمواس · نهاوند · الشورى |
| تاریخ الطبری | `9783` | ~10 | corroboration only |

Everything is under `sources/shamela/<book>/<index>.txt`, each file carrying its URL, volume and
**printed** page in the header. **Daniyal can read these directly** — they are plain text, no tool
needed.

**Session 2 is BUILT.** Everything below is done and committed.

| Artifact | | |
|---|---|---|
| `L02_baarah_saal/L02_ALL.pptx` | **275 slides** | every one of the 263 researched cards, nothing dropped. Speaker notes carry the full narrative, date, map move, عبرت line, statement and source |
| `L02_baarah_saal/L02.pptx` | **60 slides** | the crafted session: أبو بكر ؓ's caliphate entire, 11–13 AH, 31 cards |
| `L02_baarah_saal/CUE.pdf` | **1 page** | headings, names, dates, cues. No sentences |
| `L02_baarah_saal/BRIEFING.pdf` | 34 pages | 10,500 words of prose, to read at home |
| `L02_baarah_saal/WORKSHEET.pdf` | 2 pages | blank Arabia map + blank timeline + «ایک واقعہ» lines |
| `L02_baarah_saal/CONTENT.md` · `SPINE.md` | | the pool, and the declared running order |
| `series/visuals/map_s2_*.png` | 11 assets | 4:3, tight-cropped, both closing pairs (13 AH and 23 AH) |

**Daniyal's call, still open:** which cards go in which session. The recommended cut lives in
`SPINE.md` and is a *suggestion in a separate file* — every card is in `L02_ALL.pptx` regardless.

**What is left for session 2**

1. **Daniyal filters.** Delete slides from `L02_ALL.pptx`, or start from `L02.pptx` and add.
2. **Gemini fills the image placeholders** — 5 in `L02.pptx`, 31 in `L02_ALL.pptx`. Every brief is
   in the slide's speaker notes and ends with the flat-white instruction, so an image drops on with
   no seam. Briefs are non-figurative by design: no depiction of the Prophet ﷺ or any Companion.
3. **Eyeball the Arabic before it is projected.** Everything is verified against Shamela's *text*,
   not against page images, and Shamela carries its own typesetting slips — four were found in one
   stretch. `CLAUDE.md` §1.1 stands: locate by grep, **quote by eye**.
4. **One open question from the map build:** card RC05's `Map:` line says *eleven* arrows leave
   ذو القصّة but names only **ten** destinations, and its [HANDS] cue asks the room to count along.
   Either an eleventh destination is added from the sources or the counting cue is reworded. The
   map itself prints no count, so it is safe either way.

**Sessions 3+ are already researched.** عمر ؓ's ~130 page-cited cards are in `CONTENT.md` and in
`L02_ALL.pptx`, tiered and quote-checked. No new research is needed to build them.

---

## 1. Where the series stands

| | |
|---|---|
| **Sessions delivered** | **none.** Session 1 was scheduled 2 Sep 2026 and was **postponed** |
| **Next session date** | ⬜ **NOT SET** — needed for the print deadline and the build plan |
| **Session 1 status** | being **rebuilt** to the v3 shape (see `docs/specs/2026-09-03-L01-v3-spec.md`) |
| **Session 2 status** | built to the v2 shape, opens on the ردة — **still correct**, unaffected by the v3 rebuild |
| **Sessions 3–10** | not started; blocked on sources (see §3) |

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
| *تاریخِ امت*, vol 1 — المقدمہ | `sources/text/TUM_v1_muqaddima.txt` | printed pp.۳۲–۷۸ |
| *تاریخِ امت*, vol 1 — خلافتِ راشدہ opening | `sources/text/TUM_v1_abubakr.txt` | printed pp.۴۵۶–۴۶۵ |
| البدایہ والنہایہ (ابن كثير) | Shamela **30097** via `tools/shamela.py` | everything |
| سیر أعلام النبلاء (الذہبی) | Shamela **10906** | everything |
| الکامل (ابن الأثیر) | Shamela **21712** | to ۶۲۸ھ |
| الإعلان بالتوبيخ (السخاوی) | Shamela **34** | فوائد التاریخ from printed p.۱۱۱ |

**NOT usable — do not plan around these:**

- `sources/pdf/Tareekh e Ummat e Muslima … 2/3/4.pdf` — **no usable text layer. Daniyal must OCR
  these himself and has not yet.** Confirmed 2026-09-03. Assume they do not exist until he says so.
- `sources/pdf/*_text.pdf` (00–25in, jm) — these are **scans of سیر أعلام النبلاء** with a badly
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
| فوائد التاريخ (السخاوي) | 34 | 110 (= printed p.۱۱۱) |

`tools/shamela.py` caches to `sources/shamela/<book>/<index>.txt`. **A page fetched once is free
forever — check the cache before fetching.** The file header reports the printed ج/ص; **cite that,
never the index.**

## 5. Blocked / open

| # | Open item | Blocks | Owner |
|---|---|---|---|
| 1 | **New session-1 date** | print deadline, whole build plan | Daniyal |
| 2 | **OCR of *تاریخِ امت* vols 2–4** (and the rest of vol 1) | sessions 3–7 Urdu spine | Daniyal |
| 3 | Headcount | print quantities | Daniyal |
| 4 | Karbala depth and framing | session 4 | conversation needed |
| 5 | South Asia source — does *تاریخِ امت* reach it? | sessions 8–9 | check on OCR |
| 6 | Sunan Ibn Majah number for «إِذَا لَمْ تَسْتَحْيِ فَاصْنَعْ مَا شِئْتَ»; Bukhari chapter for the hadith of the nations before us | `IBRAH.md` | both marked *(to verify)* — **may not be quoted with a number until checked** |

## 6. The next three things to do

1. **Write `L01_overview/Script.md`** — the full Urdu speaker script to the v3 spec. Everything
   else for session 1 exists; this is what is missing to deliver. Build it from
   `docs/research/*` + the deck's speaker notes (which already carry the timings and citations).
2. **Write `L01_overview/BRIEFING.md`** — the pre-session study pack.
3. Close PowerPoint and promote `L01_NEW.pptx` → `L01.pptx` (see §2).
4. Get the new session-1 date; update `CLAUDE.md`, this file, and the spec.
5. Build the labelled governors map in `tools/mapstudio` — slide 23 currently reuses the blank
   Arabia base.
