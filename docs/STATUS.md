# STATUS — read this first, every session

> **2026-09-13 · RESUME POINT.** **Session 3 («⁨پہلا امتحان⁩», ۲۳–⁨۴۱ھ⁩) is researched in full** — 23
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
| **Sessions delivered** | **none.** Session 1 was scheduled 2 Sep 2026 and was **postponed** |
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
