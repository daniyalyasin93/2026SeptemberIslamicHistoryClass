# STATUS — read this first, every session

**Purpose of this file:** a new session should be fully oriented after reading *only*
`CLAUDE.md` + this file + `docs/DECISIONS.md`. If you find yourself re-deriving something,
it belongs here and did not get written down. Fix that before continuing.

**Last updated:** 2026-09-03 (session 1 v3 build)

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
