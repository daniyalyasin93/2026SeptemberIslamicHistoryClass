# «تاریخ سے سبق» — Lessons from History

A 10-session adult lecture series that gives non-specialists a **usable mental map of Islamic
history**: where events happened, in what order, how we know them, and what civilizational
lessons follow. Delivered aloud in Urdu at a DHA venue. Audience: mature adults, a regular
core plus weekly drop-ins.

**Speaker:** Daniyal — strong speaker, real stage fright, no formal history training.
Materials must be **over-prepared**: ~2× the material the slot needs, full Urdu scripts,
a one-page panic card, and a pre-written answer for every hostile question.

**First session: 2 September 2026.** Weekly thereafter. ~45 minutes.

---

## 1. Non-negotiable rules

### 1.1 References are airtight or absent

Never fabricate a citation, date, title, hadith number, page or URL. **Wrong is worse than absent.**
Cite only what traces to a source in `sources/`. If uncertain, write `(to verify)` — never state it.

**How to cite:** `sources/text/*.txt` is page-marked. Every page carries
`===== PDF p.N | PRINTED p.M =====`. Always cite the **PRINTED** page — that is the page number
in the physical book, which is what the audience could look up.

**OCR CAVEAT — this one matters.** The text layer is OCR output and it *garbles ligatures and
honorifics*: «حضور اکرم علی نیلم» is really صلی اللہ علیہ وسلم; «رضی السنہ» is رضی اللہ عنہ.
So the text is reliable for **locating and page-anchoring** a passage, but **any wording quoted
verbatim on a slide, script or handout must first be eyeballed against the page image** in the
source PDF. Locate by grep; quote by eye.

### 1.2 Register: dignified, never theatrical

The audience is mature adults. Interesting — but no theatrics.

- **Never** use cast / character / villain / hero / episode / trailer / plot twist for real
  figures, on any audience-facing artifact. Those words may exist only in planning chat.
- Honorifics always: ﷺ · ؓ for Companions · رحمہ اللہ for the ʿulamā.
- **Memorability comes from the tradition, not from invention.** Use the لقب the ummah already
  gave — الصدیق، الفاروق، ذو النورین، سیف اللہ المسلول، امین الامۃ. Where a figure has none, use a
  plain factual descriptor from the source. **Never invent a tagline for a Companion.**
- **No emblems, sigils, icons or assigned objects for people.** That device is juvenile here.
- Drama comes from real events told plainly, not from manufactured suspense.

### 1.3 Language and type

- **All Urdu in Urdu (Arabic) script. Never Roman Urdu.** Not on slides, not in scripts, not in chat.
- **Urdu font: `Jameel Noori Nastaleeq`** — installed as `Jameel Noori Nastaleeq Kasheeda.ttf` in
  the per-user font folder; its internal family name is `Jameel Noori Nastaleeq`, so that name
  resolves in both CSS and PowerPoint.
- **Arabic font: `Traditional Arabic`** (`C:\Windows\Fonts\trado.ttf`) — Naskh. Qurʾānic text and
  Arabic quotations stay Naskh; **Nastaliq for Qurʾān is non-standard.**
- Printables split by job: **English** for structure and geography (labels, dates, place names);
  **Urdu script** for everything human — names, the one-line سبق, the take-home question.
- Urdu/Arabic strings: single spaces only; never leave Latin letters inside an Arabic word.

### 1.4 Arabic carries authority — use it wherever the source supplies it

Arabic commands respect in this room, so a real Arabic quotation is free credibility. Where the
source gives a saying in Arabic, **put the Arabic on the slide in `Traditional Arabic` (Naskh) with
the Urdu rendering beneath it** — not the Urdu alone. The muqaddima is full of these and they were
being thrown away: سفیان ثوری «لَمَّا اسْتَعْمَلَ الرُّوَاةُ الْكَذِبَ اسْتَعْمَلْنَاهُمُ التَّارِيخَ» ·
حفص بن غیاث «إِذَا اتَّهَمْتُمْ فَحَاسِبُوهُ بِالسِّنِينَ» · حماد بن زید «لَمْ يُسْتَعَنْ عَلَى الْكَذَّابِينَ
بِمِثْلِ التَّارِيخِ» · «مَا أَشْبَهَ اللَّيْلَةَ بِالْبَارِحَةِ» (all printed p.۵۳–۵۷).

**Never compose Arabic ourselves.** Only reproduce what a source actually carries, and read it off
the page image before it reaches a slide — the OCR caveat in §1.1 applies doubly to Arabic, where a
single garbled letter changes the word.

### 1.5 Content safety

Sunni framing, presented as such. No novel claims. When in doubt, narrate what the book narrates
and stop. The guardrail — تاریخِ اسلام = تاریخِ مسلمین, and the fiqh that studying the مشاجرات
without need is مکروہ — is installed in **session 3**, before anything sensitive.
Never improvise a position on the Companions' disputes from the floor; defer warmly to the
session where it is handled with اصول.

---

## 2. The fixed session shape (45 min)

The furniture never changes; only the content does. This is deliberate — it is what lets a
drop-in catch up in 3 minutes, and what stops the speaker from ever being lost.

```
0:00  آغاز / re-anchor     3   The Line and the Map go up. "Last week here → tonight here."
0:03  Opening scene        5   A scene. Never a definition.
0:08  The story           20   The narrative, with the map moving as it goes.
0:28  تعارف                7   Exactly THREE people. Never more.
0:35  کیسے پتا چلا؟         3   How we know — one piece of the muqaddima.
0:38  آج کا سبق            4   One sentence of عبرت; everyone writes it in their workbook.
0:42  اگلے ہفتے            3   End on a question, not a summary.
```

**تعارف format** — the classical تراجم notice, four lines, nothing more:
`نام و نسب` (with the لقب) · `سنین` (ھ and عیسوی + point on the Line) · what they did, one
sentence · **`ایک واقعہ`** — one authentic incident from the source. The workbook prints the
first three and leaves «ایک واقعہ» blank for the listener to write. That act is the retention
mechanism.

---

## 3. The arc

| # | Session | Era |
|---|---|---|
| 1 | «ایک نظر میں — پورا نقشہ» — the whole line in one evening | ۱۱ھ → ۱۹۴۷ |
| 2 | «بارہ سال» — ابوبکر ؓ + عمر ؓ | ۱۱–۲۳ھ |
| 3 | «پہلا امتحان» — عثمان ؓ → علی ؓ · **the guardrail lands here** | ۲۳–۴۰ھ |
| 4 | «خلافت سے بادشاہت تک» — بنو امیہ · کربلا · سندھ and Spain in one decade | ۴۰–۱۳۲ھ |
| 5 | «دو دارالحکومت» — بغداد and قرطبہ: two golden ages, two collapses | ۱۳۲–۸۹۷ھ |
| 6 | «قریبِ مرگ» — صلیبی جنگیں + منگول · بغداد ۶۵۶ | ۴۹۲–۶۵۸ھ |
| 7 | «آخری خلافت» — عثمانیہ → ۱۹۲۴ | ۶۹۹–۱۳۴۲ھ |
| 8 | «یہ ہم تک کیسے پہنچا» — سندھ → دہلی → مغل | ۹۳–۱۱۱۹ھ |
| 9 | «۱۸۵۷ سے ۱۹۴۷ تک» | 1857–1947 |
| 10 | «سب کچھ جوڑ کر» — the completed map, the ten سبق, a reading path | — |

The **whole muqaddima** is redistributed across the weekly «کیسے پتا چلا؟» slot rather than
taught as a lecture. See `docs/catalogue/HOWWEKNOW.md`.

---

## 4. Layout and conventions

```
CLAUDE.md              this file
docs/PRIMER.md         Daniyal's one-time crash course, 1400 years
docs/catalogue/        the durable knowledge base — SINGLE SOURCE OF TRUTH
  SOURCES.md           what we hold, printed page ranges, what is still to obtain
  TIMELINE.md          every date used anywhere + its citation
  PEOPLE.md            the master تعارف register, page-cited
  HOWWEKNOW.md         the «کیسے پتا چلا؟» bank
  LESSONS.md           the ten سبق lines
  QA_BANK.md           safe Sunni answers to hostile questions
  MAPS.md              map inventory
docs/specs/            the series design + one spec per session
sources/pdf/           source PDFs
sources/text/          page-marked, greppable extractions
series/                the Line, the base map SVG, the workbook, the print pipeline
LNN_<slug>/            per session: BRIEFING · DRILL · script · cue card · deck · handouts
archive/               superseded work, kept as a parts bin
```

**Never let two artifacts disagree.** A date, a لقب or a page number goes into
`docs/catalogue/` first; every artifact reads it from there.

## 5. Build commands

```bash
# extract a new source volume to page-marked text (offset auto-detected)
python tools/extract_source.py sources/pdf/<file>.pdf sources/text/<file>.txt

# fetch a citable Arabic page from al-Maktaba al-Shamela (cached under sources/shamela/)
python tools/shamela.py get 34 110          # one page  -> reports the PRINTED page too
python tools/shamela.py range 34 108 115    # a span

# render an A4 printable: HTML -> PDF, fonts base64-embedded via @font-face
#   (headless Chrome; prints identically at any print shop)
chrome.exe --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf=out.pdf file:///absolute/path/in.html

# rebuild a deck (never hand-edit the .pptx for structural changes)
python LNN_<slug>/build.py
```

Decks are **python-pptx**, 16:9. Printables are **HTML+CSS → headless Chrome → A4 PDF**.
Palette: deep teal `#104A43` / `#0A322E`, gold `#C49A45`, cream `#FAF7F0`, ink `#1C2321`,
maroon `#7A2E2E` for caution. Serif `Georgia` for English headlines, `Segoe UI` for English body.

Build scripts fall back to `*_NEW.pptx` on `PermissionError` (PowerPoint holds a lock).

**Network reality (re-tested 2026-08-26 — the earlier "web is blocked" note was stale):**
general web, Wikipedia/Wikimedia and `shamela.ws` all resolve from this machine. Two quirks:
`sunnah.com` returns **403 to `WebFetch`** but serves fine to local `curl` with a browser
User-Agent; `commons.wikimedia.org` failed while `upload.wikimedia.org` and `en.wikipedia.org`
answered. YouTube remains reachable via yt-dlp.

**Arabic verification — `shamela.ws` is the standard path.** al-Maktaba al-Shamela carries the
classical corpus already typed and searchable (~7,180 books), so **Arabic quotations are verified
against the actual work rather than paraphrased out of the Urdu** (see §1.4). Use
`tools/shamela.py`; it caches to `sources/shamela/` so a citation once fetched is free to re-check
and the exact text used is reproducible. **Cite the PRINTED page the tool reports, not the Shamela
index** — they differ by one.

Book ids found so far: **34** = الإعلان بالتوبيخ لمن ذمّ أهل التاريخ (السخاوي) — its
**فوائد التاريخ** chapter begins at printed p.۱۱۱.
