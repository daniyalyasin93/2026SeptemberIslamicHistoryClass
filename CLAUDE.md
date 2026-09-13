# «تاریخ سے سبق» — Lessons from History

A 10-session adult lecture series that gives non-specialists a **usable mental map of Islamic
history**: where events happened, in what order, how we know them, and what civilizational
lessons follow. Delivered aloud in Urdu at a DHA venue. Audience: mature adults, a regular
core plus weekly drop-ins.

**Speaker:** Daniyal — strong speaker, real stage fright, no formal history training.
Materials must be **over-prepared**: ~2× the material the slot needs, full Urdu scripts,
a one-page panic card, and a pre-written answer for every hostile question.

**First session: ⬜ date to be set** — 2 September 2026 was **postponed** and no new date is fixed.
Weekly thereafter. ~45 minutes.

---

## 0. Start here — never re-derive what is already written down

**Read these three files before doing anything else. They are the whole context.**

| File | What it holds |
|---|---|
| `docs/STATUS.md` | Where everything stands *right now* — what is built, what is blocked, what is next |
| `docs/DECISIONS.md` | Every settled decision with its reason. **Append-only** |
| `docs/research/INDEX.md` | The research catalogue — grep it before researching anything |
| `docs/specs/2026-09-06-L02-and-production-v4-spec.md` | **The current production pipeline** — the six per-session artifacts, the deck contract, the runtime |

### 0.1 The research catalogue rule (standing instruction)

> **Before any research pass, grep `docs/research/INDEX.md`. If a note already answers the question,
> read it and build on it — re-derive only what is genuinely stale or out of scope. After any
> substantial pass, write a durable page-cited note into `docs/research/` and add its row to the
> index.**

Notes are **committed to the repo**. This deliberately overrides the global convention of keeping
research in a gitignored `.claude/` — these notes are a course asset and must survive a machine
change. Each note must carry: the question · findings with **PRINTED** pages · verbatim Arabic
exactly as fetched · **what could not be established** · which Shamela indices were fetched.

**Readability is part of the format (`DECISIONS.md` #25).** Arabic sits on its **own line, in its
own blockquote** — never inline inside an English sentence — with the printed page **and the direct
`shamela.ws` URL** immediately beneath it. Every note is rendered to an A4 PDF by
`tools/render_note.py` (Arabic in `Traditional Arabic` at a size that can be read); the `.md` stays
canonical and greppable, the PDF is what gets read.

Certainty labels, used everywhere: **`[SOURCED]`** (a page was read — give it) ·
**`[STANDARD]`** (conventional, not yet page-cited here — carries `(to verify)`) ·
**`[CONVENTIONAL-ESTIMATE]`** (general scholarship; our sources do not fix it — **must be labelled
as such on the slide itself**).

### 0.2 Preserve decisions, not conversations

Any decision that took more than a minute to settle goes into `docs/DECISIONS.md` **with its
reason**, the same day. A decision that lives only in a chat transcript gets re-litigated from
scratch next session, at full cost, and often gets re-decided differently.

Once a fact is settled, **promote it out of the research note into `docs/catalogue/`** — that is
what artifacts read from. Research notes are the working record; the catalogue is the source of
truth.

### 0.3 Costs worth avoiding

- **Grep the cached TOCs before fetching**: `sources/shamela/30097/_toc.tsv`,
  `sources/shamela/10906/_toc.tsv`. `docs/STATUS.md` §4 lists the chapter indices already located.
- **A Shamela page fetched once is cached forever** under `sources/shamela/<book>/<index>.txt`.
  Check the cache before fetching.
- **`sources/pdf/*_text.pdf` (00–25in, jm) are scans of سیر with a garbled OCR layer — do not read
  them.** Use Shamela **10906**. They are only for eyeballing a page image.
- ***تاریخِ امت* vols 2–4 have no usable text layer.** Daniyal will OCR them himself; until he says
  so, **do not plan any session around them** — build on the Arabic spine.

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
- **Urdu font: `Noto Nastaliq Urdu`** (installed 2026-08-27, per-user, registered).
  **Do NOT use `Jameel Noori Nastaleeq`** — the only cut on this machine is the *Kasheeda* variant,
  which elongates letters and rendered every Urdu line stretched and gappy. This was a real defect
  in the first decks.
- **Arabic font: `Traditional Arabic`** (`C:\Windows\Fonts\trado.ttf`) — Naskh. Qurʾānic text and
  Arabic quotations stay Naskh; **Nastaliq for Qurʾān is non-standard.**
- **ENGLISH CARRIES EVERYTHING** (settled 2026-08-27, extended 2026-09-06 — `DECISIONS.md` #19).
  Slides, scripts, briefings, cue sheets, worksheets **and research notes are written in English**.
  **Claude generates no Urdu at all.** Daniyal's own Urdu is better than any machine rendering; he
  translates at the lectern or by hand-editing the deck. Arabic appears **only** as verbatim
  quotation from a source, in Naskh, with an English rendering beneath it. Urdu session *titles*
  («بارہ سال» and the rest) stay — Daniyal chose them, they were not generated.
- **Latin digits on slides and in English contexts, always.** Urdu-Indic digits mixed with Latin
  punctuation get reordered by the bidi algorithm into nonsense. This was a real bug in both the
  first handout and the first decks.
- **Never put Urdu and English in the same line or the same table cell.** Give Urdu its own block
  with `dir="rtl"`. Inline mixing is what mangled the first speaker scripts.
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

### 1.5 Venue and standing policy (settled 2026-08-26)

| | |
|---|---|
| **Venue** | DHA **Islamabad** |
| **Organisation** | **Tanzeem-e-Islami** — they also review the sensitive material |
| **Recording** | **Not permitted.** No filming, no clips |
| **Questions** | **None during the 45 minutes.** Written slips into a box at the door; speaker stays 15 minutes afterwards for one-to-one. Identical in all ten sessions |
| **محرم** | **No clash** — none of the ten dates falls in محرم, so کربلا in session 4 is not being delivered into محرم |
| **The book** | Named openly to the room. The speaker says plainly that the course is based on *تاریخِ امت* and that he is reading a book, not authoring history |
| **Headcount** | ⬜ still needed, for print quantities |

**What Tanzeem-e-Islami implies for content.** The audience is religiously committed and
Qur'an-literate, and **خلافت → ملوکیت (session 4) and the ending of the caliphate in ۱۹۲۴
(session 7) sit close to the organisation's own reason for existing.** Those evenings will carry
more charge than the others. The response is not to soften them and not to lean into them: narrate
what the book narrates, let the quoted authorities carry every conclusion, and decline to
adjudicate. The room may want the speaker to draw the inference; he does not.

### 1.6 Content safety

Sunni framing, presented as such. No novel claims. When in doubt, narrate what the book narrates
and stop. The guardrail — تاریخِ اسلام = تاریخِ مسلمین, and the fiqh that studying the مشاجرات
without need is مکروہ — is installed in **session 1** (moved there 2026-09-03, `DECISIONS.md` #14,
because سقيفة now lands in session 1 and the guardrail must precede it). Its vehicle is the
**حدیث / تاریخ / فقہ** distinction in the opening block: in fiqh a report must be authentic to
bind; in تاریخ we record what was reported in order to fix sequence — **so a تاریخ report is
neither a ruling nor a creed, and we do not judge between Companions.** Session 3 still carries the
fuller fiqh treatment of the مشاجرات proper.
Never improvise a position on the Companions' disputes from the floor; defer warmly to the
session where it is handled with اصول.

---

## 1.7 Artifact rules learned the hard way

**The deck contract (`DECISIONS.md` #21). Claude writes the words; Gemini draws the pictures;
Daniyal merges them.** `build.py` asserts these and **fails the build** on violation:

| Rule | Value |
|---|---|
| Background | flat `#FFFFFF` on every slide — identity comes from a teal title bar and a gold rule, never a coloured ground |
| Minimum type anywhere | **24pt** · body **28pt** · a key statement **44pt+** · headline **40pt** |
| Body words per slide | **≤20** |
| Permitted slide kinds | full-bleed image/map · large statement · diagram · timeline strip |
| Bullet-list slides | **do not exist** |
| Image placeholders | real, correctly sized, editable — never flattened |

White is not a palette choice, it is a merge requirement: it is the one colour Gemini reproduces
exactly, so a generated image drops in with no seam. `SLIDES.md` carries a paste-ready
**`IMAGE BRIEF:`** for every visual slide.

**The lectern carries `CUE.pdf` — one page, headings, names, dates, no complete sentences**
(`DECISIONS.md` #22). Prose lives in `BRIEFING.pdf` and is read at home. The prose speaker script
is retired as a delivery artifact.

**A SLIDE FACE CARRIES ONLY WHAT THE ROOM MAY SEE (`DECISIONS.md` #30).** Certainty labels, tier
tags, card ids, cross-references, build markers, `[HANDS]` cues, `n/a`, IMAGE BRIEF text, the words
Claude/Gemini/AI, and raw URLs are **production apparatus and belong in the speaker notes**.
`deck2.audit()` enforces this with a `FORBIDDEN` list and **fails the build** on any match — this is
the class of defect that survives every review and then appears on a projector.

**Every deck ships a PDF beside it.** `deck2.save()` writes `<deck>.pdf` automatically, because
Daniyal checks on a phone and on machines without PowerPoint. `series/preview.py` also exports
per-slide PNGs and a contact sheet — **look at the contact sheet before calling a deck finished.**

- **No bare-text slides.** Every content slide carries a map, the timeline strip, a large statement,
  or a sourced quotation. If it is only a line of text, it is not a slide — the first decks were
  rejected as "too dry" and they were.
- **Speaker packs are HTML → A4 PDF, never Markdown.** Markdown cannot keep Urdu and English apart
  and the result is unreadable. See `L01_overview/speaker.html`.
- **The cue card must fit on ONE page.** That is its entire purpose.
- **Method content is minimal, and there is no methodology slot.** The weekly «کیسے پتا چلا؟»
  segment was cut on 2026-08-27 as too academic, and that cut is now carried through into the
  session shape itself (`DECISIONS.md` #27). What survives: one four-minute "two ways of knowing
  the past" slide in session 1, the سفیان ثوری quotation, and a source remark **spoken inside the
  story** at the moment a listener would naturally ask "how do we know that?" Never a recurring slot.
- Regenerate visuals with `python series/make_visuals.py`; decks import `series/deckkit.py`.

## 2. The fixed session shape (45 min)

The furniture never changes; only the content does. This is deliberate — it is what lets a
drop-in catch up in 3 minutes, and what stops the speaker from ever being lost.

> **Session 1 is the one exception.** It is the orientation evening and runs its own shape —
> see `docs/specs/2026-09-03-L01-v3-spec.md`. In particular it has **no separate تعارف block**;
> the people are introduced inside the story, where each becomes load-bearing
> (`DECISIONS.md` #15). **The fixed shape below governs sessions 2–10.**

```
0:00  Bookend IN       4   Last week's CLOSING Line + CLOSING Map, unchanged. "We came from here."
0:04  The story       22   Scenes, not coverage. The map moves. People are met inside the story.
                          One عبرت line after each major event. Three [HANDS] beats.
0:26  Worksheet        2   90 seconds, silent. Mark the map; fill the timeline boxes.
0:28  The story       12   Continues.
0:40  Bookend OUT      1   The Line, with tonight's events lit up and nothing else.
0:41  Bookend OUT      2   The Map — where we stand NOW vs. when the room walked in.
0:43  Tonight's عبرت   1   Every line from tonight, together on one screen.
0:44  Next week        1   A question, never a summary.
0:45  A loud السلام علیکم, then the dua. The room must know it has ended.
```

**The bookend (`DECISIONS.md` #23).** The two closing slides at 0:40–0:42 are re-used **verbatim**
as the two opening slides of the following session. That is the whole re-anchor mechanism: the
room *sees* the continuity instead of being told about it. Build a session's closing pair for
**every** stopping point Daniyal might cut to, not just the planned one.

**Build ~70 minutes of material for the 45-minute slot** and let Daniyal cut (`DECISIONS.md` #20).
Overflow rolls into the next session; it is never compressed. **No live Q&A** (#24) — interaction
is the three [HANDS] beats and the silent worksheet.

**People are met inside the story, not in a block** (`DECISIONS.md` #28 — session 1's practice,
now the rule for every session). Each figure is named at the moment he becomes load-bearing, with
his clan, and given the classical تراجم notice **in one breath**: `name + لقب` · `dates` (ھ and
عیسوی, and a point on the Line) · what he did, one sentence.

**The retention ritual survives and moves to paper.** The worksheet prints those three lines for
each of the evening's principal figures and leaves **«ایک واقعہ»** blank for the listener to write
during the 90-second worksheet beat. The act of writing is the mechanism; a seven-minute block on
stage was never the mechanism.

---

## 3. The arc

| # | Session | Era |
|---|---|---|
| 1 | «وقت، جگہ، اور ایک رات» — orientation in time and space · Medina's clans · سقیفہ · the eve of the ردہ | the whole line as **pegs**; the narrative stops at ۱۱ھ |
| 2 | «بارہ سال» — ابوبکر ؓ + عمر ؓ | ۱۱–۲۳ھ |
| 3 | «پہلا امتحان» — عثمان ؓ → علی ؓ · **the guardrail lands here** | ۲۳–۴۰ھ |
| 4 | «خلافت سے بادشاہت تک» — بنو امیہ · کربلا · سندھ and Spain in one decade | ۴۰–۱۳۲ھ |
| 5 | «دو دارالحکومت» — بغداد and قرطبہ: two golden ages, two collapses | ۱۳۲–۸۹۷ھ |
| 6 | «قریبِ مرگ» — صلیبی جنگیں + منگول · بغداد ۶۵۶ | ۴۹۲–۶۵۸ھ |
| 7 | «آخری خلافت» — عثمانیہ → ۱۹۲۴ | ۶۹۹–۱۳۴۲ھ |
| 8 | «یہ ہم تک کیسے پہنچا» — سندھ → دہلی → مغل | ۹۳–۱۱۱۹ھ |
| 9 | «۱۸۵۷ سے ۱۹۴۷ تک» | 1857–1947 |
| 10 | «سب کچھ جوڑ کر» — the completed map, the ten سبق, a reading path | — |

**The arc is a sequence, not a schedule** (`DECISIONS.md` #20). Each session ships an over-built
pool and Daniyal cuts; whatever does not fit rolls forward. **Sessions may therefore exceed ten,
and that is the intended behaviour** — coverage is never bought by speeding up, which is what the
room objected to after session 1. The eras below are the *order*; the week numbers are not a promise.

**Pools by era, evenings by number** (`DECISIONS.md` #33). `L02_baarah_saal/CONTENT.md` is the
**11–23 AH pool** and `L03_pehla_imtihan/CONTENT.md` the **23–41 AH pool** — whatever their folder
names say. An evening is a numbered delivery folder `SNN_<slug>/` that picks card ids out of a pool.
**Where the story has actually reached lives only in `docs/catalogue/DELIVERED.md`** — read its last
row before planning any evening. Evening 2 stopped after بزاخة (37 min, ran short); evening 3 is
`S03_yemen/`.

The **muqaddima** is no longer delivered in a weekly slot (`DECISIONS.md` #27). Its material is
drawn on **inside the story**, one remark at the moment a listener would ask "how do we know that?"
The bank still lives in `docs/catalogue/HOWWEKNOW.md`.

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
  DELIVERED.md         the ledger: which card ids were spoken on which evening
docs/specs/            the series design + one spec per session
sources/pdf/           source PDFs
sources/text/          page-marked, greppable extractions
series/                the Line, the base map SVG, the workbook, the print pipeline
L02_baarah_saal/       the 11–23 AH POOL (CONTENT.md) + evening 2's artifacts as built
L03_pehla_imtihan/     the 23–41 AH POOL (CONTENT.md)
SNN_<slug>/            per evening (DECISIONS #33): RUNSHEET.md (card ids to cut), then six artifacts (spec v4 §1):
  CONTENT.md             (pools only) numbered event cards, tiered CORE/GOOD/CUT
  SLIDES.md              one block per slide + the paste-ready IMAGE BRIEF for Gemini
  build.py -> LNN.pptx   editable, white ground, image placeholders. Never hand-edit for structure
  CUE.pdf                ONE page for the lectern. Headings, names, dates. No sentences
  BRIEFING.pdf           the prose. Read twice at home. Never at the lectern
  WORKSHEET.pdf          blank map + blank timeline strip + the «ایک واقعہ» lines
archive/               superseded work, kept as a parts bin
```

**Never let two artifacts disagree.** A date, a لقب or a page number goes into
`docs/catalogue/` first; every artifact reads it from there.

**Stay inside the safe Sunni list.** For general narrative use only **البدایہ والنہایہ (30097)**,
**سیر أعلام النبلاء (10906)**, **الکامل (21712)** and **الإعلان بالتوبيخ (34)** — all four are named
and relied on by the course's own مقدمہ, so citing them stays inside the course's frame.
**تاریخ ابن خلدون (12320)** is admitted for **judgement and framing only** — never as the sole
authority for a date, name, number or wording, and never for the مشاجرات (`DECISIONS.md` #29). When
one of his readings is used it is attributed to him **by name**, as how he read the event, never as
what happened. His 11–23ھ window is cached at indices ۱۲۷۶–۱۳۷۰.
**تاریخ الطبری (9783) is corroboration only, never alone**, and never for anything touching the
مشاجرات — it collects with chains and does not sift, and presence in طبری is not authenticity
(مقدمہ p.۷۱). Works the مقدمہ flags for sectarian lean (یعقوبی، مسعودی — p.۴۶) are not used without
a specific decision. **Every Shamela page used gets a line in `docs/catalogue/SHAMELA_LOG.md`.**

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
