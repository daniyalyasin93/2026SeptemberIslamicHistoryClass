# METHOD HANDOFF — starting a new repo on the same method, a different topic

**Written:** 2026-09-19 · **From:** `2026SeptemberIslamicHistoryClass` («تاریخ سے سبق»)
**For:** a *new, empty* repository whose subject is something else, but whose **method and source
grounding are the same** — page-cited Arabic from al-Maktaba al-Shamela, inside an Ahl al-Sunna
frame, with the citations checked by script rather than by trust.

> **Read this file top to bottom once before creating a single file in the new repo.** It is the
> distilled cost of four months of this one. Everything in it was paid for by a defect that reached
> an artifact — usually a projector — before anyone noticed.

---

## 0. What transfers, and what does not

The repo has two layers. Only one of them is about Islamic history.

| Layer | What it is | Transfers? |
|---|---|---|
| **The research layer** | Shamela fetching and caching · the source tier list · the research-note format · certainty labels · the catalogue · `check_citations.py` · the Arabic typography and bidi rules | **Yes, wholesale.** This is the method. |
| **The delivery layer** | 45-minute session shape · the bookend · `CONTENT.md` event cards · `build.py` → `.pptx` · `CUE.pdf` / `BRIEFING.pdf` / `WORKSHEET.pdf` · the deck contract | **Only if the new output is also a spoken lecture series.** |

So the first decision in the new repo is **what the output is**, because it decides how much of
this you take:

- **A lecture / teaching series** → take both layers. Copy nearly everything; §10 says what to rename.
- **A book, a paper, a dossier, a reference work, a fatwa file, a curriculum** → take the research
  layer only, and design your own unit of output (§6.3). Do **not** carry the event card across just
  because it is there; a card whose fields are `Map:` and `Hands-up?` in a repo that will never
  project a map is dead weight that every future session has to read past.

**What never transfers:** this repo's specific decisions about *this* course — venue, audience,
session order, the Urdu titles, the ten سبق. Start `DECISIONS.md` empty in the new repo. Copying
somebody else's settled decisions is how a repo acquires rules nobody can justify.

---

## 1. Day one — the skeleton

Create exactly this, and nothing else. Anything that is not on this list is scratch until it earns
a place.

```
CLAUDE.md                    ← from docs/handoff/CLAUDE.template.md, blanks filled (§13)
docs/
  STATUS.md                  ← where everything stands RIGHT NOW. Reverse-chronological resume points
  DECISIONS.md               ← append-only. Every settled decision + its reason + its date
  research/
    INDEX.md                 ← the catalogue of notes. Grepped before any research pass
    <topic-slug>.md          ← the notes themselves
  catalogue/
    SOURCES.md               ← the tiered source list; what is held, what is still needed
    SHAMELA_LOG.md           ← every Arabic page fetched, and what it was used for
    TIMELINE.md              ← every date used anywhere + its citation      (if the topic is historical)
    PEOPLE.md                ← the تراجم register, page-cited                (if the topic has people)
    QA_BANK.md               ← prepared answers to the hostile questions
    <your own>.md            ← whatever the topic's durable knowledge actually is
  specs/
    YYYY-MM-DD-<name>-spec.md
tools/
  shamela.py                 ← copied verbatim
  check_citations.py         ← copied, BANNED set edited
  render_note.py             ← copied, if notes are to be read as PDFs
  extract_source.py          ← copied, if there are scanned PDFs to page-mark
sources/
  shamela/<book>/<index>.txt ← the fetch cache. COMMITTED, not gitignored
  shamela/<book>/_toc.tsv    ← the cached table of contents
  pdf/  text/                ← held PDFs and their page-marked extractions
```

**Two of these are counter-intuitive and both are deliberate.**

**`docs/research/` is committed to git.** This overrides the usual convention of keeping research in
a gitignored `.claude/`. These notes are the asset — they must survive a machine change, a lost
session, and a model change. A finding that lives only in a chat transcript gets re-derived from
scratch, at full cost, and often comes back different.

**`sources/shamela/` is committed too.** The cache is what makes `check_citations.py` possible: the
checker compares the quoted Arabic against *the file the quotation was taken from*. If the cache is
not in the repo, the check cannot run on a fresh clone, and the citations go back to being trusted
instead of verified. It is small text; commit it.

---

## 2. The three standing rules

These are the whole method. If the new repo keeps nothing else, keep these.

### 2.1 Grep the index before researching anything

> Before any research pass, grep `docs/research/INDEX.md`. If a note already answers the question,
> read it and build on it — re-derive only what is genuinely stale or out of scope. After any
> substantial pass, write a durable page-cited note into `docs/research/` and add its row to the
> index.

The failure this prevents is not subtle: without it, session 6 re-fetches and re-reads what session 3
already established, spends the tokens, and arrives at a *slightly different* answer — and now two
artifacts disagree and nobody knows which is right.

### 2.2 References are airtight or absent

> Never fabricate a citation, date, title, hadith number, page or URL. **Wrong is worse than absent.**
> Cite only what traces to a source in `sources/`. If uncertain, write `(to verify)` — never state it.

A note that says "could not be established, and here is why" has done its job. A note that guesses
confidently has destroyed the value of every other note beside it, because now the reader has to
check all of them.

### 2.3 Settled facts are promoted out of the notes into the catalogue

Research notes are the **working record**. `docs/catalogue/` is the **source of truth**. Once a fact
is settled, it moves — and every downstream artifact reads it from the catalogue, never from a note.

This is the rule that stops two artifacts disagreeing about a date. It is also the rule most likely
to be skipped, because skipping it costs nothing today. In this repo it *was* skipped: on 2026-09-10
the catalogue still looked as it had six weeks earlier while 28,825 lines of page-cited research had
piled up beside it, and the symptom showed up from the far end — good researched material was
reaching no artifact at all. Build the promotion step into the routine from week one.

---

## 3. Source grounding — how to pick the Ahl al-Sunna spine for a new topic

This is the part people get wrong by treating the source list as a preference. It is not. **The list
is an argument, and it has to be defensible from inside the tradition the work claims to stand in.**

### 3.1 The tiering model

Every source in the new repo goes in exactly one tier, written into `docs/catalogue/SOURCES.md`
before the first fetch:

| Tier | Meaning | This repo's example |
|---|---|---|
| **Spine** | The named work the project is openly built on. Say so out loud to the audience/reader | *تاریخِ امت* (Urdu), with البدایہ والنہایہ as the Arabic spine |
| **Primary** | Cite alone, freely, for narrative and fact | البدایہ والنہایہ (30097) · سیر أعلام النبلاء (10906) · الکامل فی التاریخ (21712) · الإعلان بالتوبيخ (34) |
| **Judgement only** | Used for framing and interpretation, **never** as the sole authority for a date, name, number or wording. Attributed **by name** when used | تاریخ ابن خلدون (12320) |
| **Corroboration only** | Never alone. Presence in it is not authenticity | تاریخ الطبری (9783) |
| **Excluded** | Named, with the reason, so the exclusion is a decision and not an oversight | works the مقدمہ flags for sectarian lean — یعقوبی، مسعودی |

**Why the tiers and not just a list.** A flat list makes every source equally citable, and then the
weakest one in the list silently becomes the authority for the one fact only it carries. The tier is
what lets a *script* refuse a citation: `check_citations.py` flags `BOOK_BANNED` the moment a
quotation rests on the corroboration-only book alone.

### 3.2 The rules that travel unchanged, whatever the topic

1. **The list is justified from within the work's own frame.** In this repo every primary source is
   one the course's own مقدمہ names and relies on — so citing them is staying inside the course's
   frame, not stepping outside it. Do the same in the new repo: derive the list from an authority the
   *subject itself* already accepts, and write that derivation into `SOURCES.md`. A list justified
   only by "these are good books" will not survive the first hostile question.
2. **The spine is named openly.** The speaker/author says plainly what he is building on and that he
   is reading a book, not authoring the field. This is what buys the right to be wrong about a detail
   without the whole project collapsing.
3. **Sunni framing, presented as such.** No novel claims. When in doubt, narrate what the source
   narrates and stop.
4. **Every page used gets a line in `SHAMELA_LOG.md`.** Nothing from Shamela enters an artifact
   without one. It is a two-minute discipline that makes the whole corpus auditable.
5. **Contested ground gets a guardrail, installed *before* the material that needs it.** In this repo
   that is the مشاجرات: the حدیث/تاریخ/فقہ distinction is taught in session 1 because the material
   that needs it lands in session 1. Find the new topic's equivalent — every Sunni subject has one —
   and place it before, never after.
6. **Decline to adjudicate where the tradition declines to.** Narrate, let the quoted authorities
   carry the conclusion, and do not let the room push you into a ruling you did not come to give.

### 3.3 Choosing the list for a topic that is not history

The tier model holds; the books change. Work it in this order:

1. **Name the field's own recognised spine** — the work a Sunni scholar of that field would accept as
   a starting point, not the one that is easiest to fetch.
2. **Ask what class of evidence the field runs on**, because it decides the tiering:
   - *Narrative history* → the historian-chroniclers tier as above; the sifted ones outrank the
     collectors, and the collectors are corroboration only.
   - *Fiqh* → the madhhab's own مبسوط/متون tier above the later commentaries; a تخريج work for the
     ḥadīth underneath; never a modern digest as the authority for a school's position.
   - *ʿAqīda* → the primary مصنّفات of the salaf above the later kalām-inflected summaries; be
     explicit about which school of Sunni theology the framing is.
   - *Ḥadīth and its sciences* → the collections themselves for the matn, the رجال and علل works for
     the judgement, and **never** quote a grading you did not read in a grading work.
   - *Tafsīr* → the مأثور tier and the لغوي tier separated and labelled; a tafsīr's *opinion* is never
     cited as the verse's meaning.
   - *Sīra / تراجم* → the sifted biographical works primary; the مغازي collectors corroboration only.
3. **Write the exclusions down with reasons.** Unwritten exclusions get quietly reversed at 2 a.m.
4. **Cap it.** Four to six primary works is a source list. Twenty is a library, and a library cannot
   be tiered, logged, or defended.

### 3.4 Finding book ids on Shamela

`shamela.ws/book/<book_id>/<index>`. Get the id from the site's own search or the book's landing
page, then **cache its whole table of contents in one fetch** before fetching any page:

```bash
python tools/shamela.py toc 30097 --find "باب"      # 3,362 entries, one request, cached forever
```

Locating a chapter through the cached TOC costs one fetch for the entire book. Searching page by page
costs one fetch per chapter and was, before the TOC cache existed, the single largest avoidable cost
in this repo.

Ids carried over from here, if the new topic touches the same corpus: **30097** البدایہ والنہایہ ·
**10906** سیر أعلام النبلاء · **21712** الکامل فی التاریخ · **12320** تاریخ ابن خلدون ·
**34** الإعلان بالتوبيخ · **9783** تاریخ الطبری *(corroboration only)*.

---

## 4. Shamela mechanics — the things that will bite

**The index in the URL is not the printed page.** It is Shamela's internal sequential number and it is
usually **one lower** than the printed page. `tools/shamela.py` records **both** in the cached file
header. **Always cite the printed page and the volume** (`ج۷ ص۱۳۴`) — that is the page a reader
holding the physical book can turn to. A citation to a Shamela index means nothing to anyone.

**A page fetched once is cached forever** under `sources/shamela/<book>/<index>.txt`. Check the cache
before fetching. Grep the cached `_toc.tsv` before searching.

**The cached file header carries the URL, the volume-and-printed-page and the chapter**, which is what
makes a citation re-checkable offline and what `check_citations.py` reads to catch `PRINTED_WRONG`.

**Be a polite client.** The tool sleeps 1s between pages in a range. Leave that in.

**Harakat.** `--raw` strips vowel marks. Store the vowelled text; strip only for matching.

**Shamela's text is typed, not OCR'd** — that is exactly why it is used instead of paraphrasing out of
a scanned translation. But the folding of letter forms still varies (أ إ آ ٱ / ى ي / ة ه / ؤ ئ), which
is why the checker normalises them before comparing.

**If the new repo also holds scanned PDFs**, the OCR caveat from this repo applies and is brutal:

> The text layer garbles ligatures and honorifics — «حضور اکرم علی نیلم» is صلی اللہ علیہ وسلم;
> «رضی السنہ» is رضی اللہ عنہ. The text is reliable for **locating and page-anchoring** a passage and
> **not** for wording. **Locate by grep; quote by eye** against the page image before any verbatim use.

`tools/extract_source.py` page-marks an extraction so every page carries
`===== PDF p.N | PRINTED p.M =====` and auto-detects the printed-page offset. Copy it if there are
scans; it is topic-independent.

---

## 5. The research note format

This is the single most valuable artifact shape in the repo. Copy it exactly. Every note carries, in
this order:

1. **The question the note was written to answer.** Stated as a question, in full sentences. A note
   without one drifts into a topic dump that nobody can tell is finished.
2. **Scope, and the sister notes** — what this note deliberately does *not* cover, and where that
   lives instead. This is what stops two notes growing a contradictory overlap.
3. **Sources fetched** — book ids and indices, and separately **"read from the cache, not
   re-fetched"**. The next session reads the second list off the cache for free.
4. **Standing cautions** — a ⚠ block: which chains the material runs through, what the source itself
   says about its own reliability, and any wording that must be eyeballed against a page image before
   it is used.
5. **§0 — "The sentences this note licenses."** *Numbered, each with its certainty label and printed
   page.* This is the section every downstream artifact actually reads. Write it as the finished
   sentences a slide or a page may carry, not as a summary of the research.
6. **The body**, in numbered sections, with every verbatim Arabic quotation in **its own blockquote,
   on its own line**, followed immediately by the printed page **and the direct `shamela.ws` URL**,
   then the English rendering:

   ```markdown
   > كَانَ سُفَهَاءُ بَكْرٍ قَدْ غَلَبُوا عَلَى عُقَلَائِهَا …
   > — الکامل فی التاریخ ج۱ ص۴۶۲ · https://shamela.ws/book/21712/458
   > *English:* "The foolish men of Bakr had got the better of its wise men …"
   ```

   **Never inline Arabic inside an English sentence in a quotation block.** The three lines are three
   different things with three different text directions, and a renderer that fuses them produces
   the mangling that destroyed this repo's first speaker scripts.
7. **What could not be established**, and why. Non-optional. A stated gap outranks a confident guess.
8. **The output units** (`## EVENT CARDS`, or whatever §6.3 makes them) in a fixed, machine-parsable
   shape, so a script can assemble them without a model reading 10,000 lines of notes.

**Add the note's row to `docs/research/INDEX.md` in the same commit.** The index row carries: the
filename, what it answers (specific enough to grep), what it is for, and how it was verified.

### Certainty labels — used everywhere, without exception

| Label | Means |
|---|---|
| `[SOURCED]` | A page was read. **Give it.** |
| `[STANDARD]` | Conventional, not yet page-cited here. Carries `(to verify)` |
| `[CONVENTIONAL-ESTIMATE]` | General scholarship; our sources do not fix it. **Must be labelled as such on the artifact face itself** |

The third one is the one that matters. An estimate presented bare is a fabrication with extra steps.

---

## 6. The unit of output

### 6.1 Why there is a unit at all

Notes are too long and too shaped-for-reading to build from. So every note ends in a section of
small, uniform, numbered, machine-parsable **units**, each of which is the *only* place a fact is
authored. Everything downstream derives from them.

In this repo the unit is the **event card**, and the rule is absolute: **a finding in a note body
that is on no card does not exist on stage.**

### 6.2 The card, as this repo has it

```markdown
### <NOTE-PREFIX>/E-XX01 · <one-line title, tellable aloud>
**Tier:** CORE · **When:** <date> `[SOURCED]` · **Map:** <what moves on the map>
**What happened:** <3–6 sentences, plain, tellable>
**The statement:**
> ‹verbatim Arabic, own line›
> — البدایہ والنہایہ ج۷ ص۲۹ · https://shamela.ws/book/30097/NNNN
> *English:* "<rendering>"
**عبرت:** <one sentence — the lesson>
**Hands-up?** no
```

Tiers: **CORE** (it breaks without this) · **GOOD** (include if time) · **CUT** (recorded so it is
never re-researched; not planned for delivery). The CUT tier is doing real work — it is how a repo
stops paying twice for the same dead end.

### 6.3 Designing the unit for a different output

Keep the **shape** (id · one-line title · a tier · the substance · the verbatim source block · the
takeaway) and change the **fields** to what the new artifact actually consumes:

| If the output is… | The unit is… | Fields that replace `Map:` / `Hands-up?` |
|---|---|---|
| A lecture series | the event card | keep as is |
| A book or long paper | a **claim card** | `Chapter:` · `Function:` (argument / illustration / objection) · `Answers:` |
| A fatwa or ruling file | a **مسألة card** | `School:` · `Ruling:` · `Dissent:` · `Evidence tier:` |
| A reference work | an **entry** | `Headword:` · `Cross-refs:` · `Variants:` |
| A curriculum | a **learning unit** | `Prerequisite:` · `Assessed by:` · `Minutes:` |

Then **write a `check_cards.py` for your fields on the same day you fix them** (§7). A unit format
with no linter degrades within a fortnight, silently, and you find out when a downstream build reads
an empty field and prints nothing.

---

## 7. The mechanical gates — the highest-value idea in this repo

**Verification that can be done by string comparison is never done by a model.**

That is the load-bearing insight. This repo used to send a second model over each note to re-grep
every quotation. It was the single most expensive operation in the project and, being a model, it
was also sometimes just wrong. But the question is not a judgement call: *the quoted Arabic either
occurs on the cited page or it does not.* That is string work. So it is done by a script, for
nothing, and **the model is only ever asked to fix what the script flags.**

Build these four in the new repo. Each is ~200 lines.

### `check_citations.py` — copy verbatim, edit the BANNED set

Per quotation block, it flags:

| Code | Catches |
|---|---|
| `PAGE_MISSING` | the cited Shamela page is not in the cache at all |
| `TEXT_ABSENT` | the quoted Arabic is not on the cited page — *and reports which page it is really on* |
| `PRINTED_WRONG` | the printed ج/ص in the citation is not the one the cached file's header reports |
| `BOOK_BANNED` | the citation rests on a corroboration-only source alone |

Matching is deliberately forgiving about everything that is not a letter — harakat, tatweel,
editorial brackets, footnote markers, punctuation, whitespace — and folds the letter forms Shamela
varies. A quotation elided with `…` is split there and each piece checked separately. Fragments
under ~18 characters are not checked, because a short substring match proves nothing.

Exit code is non-zero while any problem stands. **Run it before every commit that touches a note.**

### `check_cards.py` — write for your own unit format

Flags `MISSING_FIELD`, `BAD_TIER`, `NO_LABEL` (a date with no certainty label), `DUPLICATE_ID`,
`STUB` (substance too short to be usable), and — most importantly — **`APPARATUS`**: production
apparatus that has leaked into text destined for an audience face.

### The apparatus rule, generalised

**An audience-facing face carries only what the audience may see.** Certainty labels, tier tags, unit
ids, cross-references, build markers, `n/a`, image-brief text, the words Claude/Gemini/AI, and raw
URLs are **production apparatus** and belong in the notes/apparatus channel, never on the face. This
is the class of defect that survives every human review and then appears on a projector. Enforce it
with a `FORBIDDEN` list that **fails the build**.

### `check_introductions.py` — the one nobody thinks of

It walks the deliverable in running order and reports every proper name (or term, or event, or
forward reference) appearing **for the first time in the series** — in nothing previously delivered
and in no earlier unit of this one. The deliverable answers every row in an
`## Introductions checked` table, and **"no notice needed" is a valid answer** — the rule is that
somebody looked.

Why it exists: a review here found five men carrying cards with **no introduction anywhere in the
delivered series**, including one who carried seven cards of an evening and whose only introduction
sat inside the block the runsheet said to cut first. **No other check in the repo could see it.** The
citations were perfect, the cards were well formed, and the room still met a stranger.

**Run the same question over four kinds of thing**, not just people:

| Kind | The failure it catches |
|---|---|
| **People** | a name carries units with no introduction |
| **Events** | a unit depends on something that is on no unit, so it was never told |
| **Terms** | a line's whole force rests on something unglossed |
| **Forward references** | the work names something from a part not yet given |

Two traps the tool cannot see: **a name introduced only inside an optional block is not introduced** —
the notice belongs on a unit that is never cut; and anything delivered before the ledger existed is
not in the known set, so those rows get answered by hand.

### `promote_catalogue.py` — regenerate what is pure extraction

Rebuild the catalogue files that are **pure extraction** from the units (in this repo: every lesson
line, and every dated unit with its certainty label carried through unchanged). Regenerate on every
run; preserve anything hand-written below a marker line.

**Do not generate the files that need judgement.** A biographical notice has to *choose* which
incident to carry; a prepared answer has to be phrased for a hostile room. Generating those
mechanically produces something that looks like a catalogue and cannot be trusted as one — which is
worse than an empty file.

---

## 8. Typography and bidi — non-negotiable, and topic-independent

Every one of these was a real, shipped defect here.

- **Arabic sits on its own line, in its own blockquote** — never inline inside an English sentence —
  with the printed page and the `shamela.ws` URL immediately beneath it.
- **Never put two scripts in the same line or the same table cell.** Give the non-Latin script its own
  block with `dir="rtl"`. Inline mixing is what mangled the first speaker scripts.
- **Latin digits in English contexts, always.** Urdu/Arabic-Indic digits mixed with Latin punctuation
  get reordered by the bidi algorithm into nonsense. This was a real bug in a handout *and* in a deck.
- **Arabic face: a Naskh** — here `Traditional Arabic`. **Nastaliq for Qurʾānic text is non-standard.**
- **If the repo carries Urdu: `Noto Nastaliq Urdu`.** Never `Jameel Noori Nastaleeq` unless you have
  verified the cut — the common one is the *Kasheeda* variant, which elongates letters and renders
  every line stretched and gappy.
- **Single spaces only** inside Arabic/Urdu strings; never leave Latin letters inside an Arabic word.
- **Printables are HTML + CSS → headless Chrome → A4 PDF, with fonts base64-embedded via `@font-face`.**
  Never Markdown: Markdown cannot keep two scripts apart and the result is unreadable. Never a CDN
  webfont: no network at the print shop means a silent fallback to a Latin serif and the Arabic is
  destroyed. Chrome subsets to the glyphs used, so the inline base64 does not bloat the output.
- **Render every research note to PDF** (`render_note.py`): the `.md` stays canonical and greppable —
  it is what git diffs and what grep searches — and the PDF is what actually gets read, with Arabic at
  a size chosen for reading rather than for fitting. In a plain Markdown viewer the findings here were
  good and unreadable, which is the same as not having them.

```bash
chrome.exe --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf=out.pdf file:///absolute/path/in.html
```

**Honorifics, always:** ﷺ · ؓ · رحمہ اللہ. And never invent an epithet for a real figure — use the
لقب the tradition already gave, or a plain factual descriptor from the source.

---

## 9. Register — the rules that keep the work dignified

Carry these into any repo whose subject is the tradition, whatever the output:

- **Never** use cast / character / villain / hero / episode / trailer / plot twist for real figures on
  any audience-facing artifact. Those words may exist in planning chat and nowhere else.
- **Memorability comes from the tradition, not from invention.**
- **No emblems, sigils, icons or assigned objects for people.**
- Interest comes from real material told plainly, not from manufactured suspense.
- **Over-prepare.** Build roughly **2× what the slot or the page count needs** and cut. Coverage is
  never bought by speeding up. Overflow rolls forward; it is never compressed.

---

## 10. The copy list

| File | Do what |
|---|---|
| `tools/shamela.py` | **Copy verbatim.** Zero changes needed |
| `tools/check_citations.py` | **Copy.** Edit `BANNED` to the new corroboration-only ids; leave the normalisation alone |
| `tools/render_note.py` | **Copy** if notes are read as PDFs. Needs `markdown` + Chrome + the fonts |
| `series/embed_fonts.py` | **Copy.** It owns the font policy and refuses the banned Nastaliq cut |
| `tools/extract_source.py` | **Copy** if there are scans. Edit the `JUNK` regex for your edition's header |
| `tools/check_cards.py` | **Rewrite** for your unit's fields. Keep the `APPARATUS` check exactly |
| `tools/check_introductions.py` | **Rewrite** the parsing; keep the idea and the four-kinds table |
| `tools/build_content.py` | **Rewrite.** Keep the principle: assembling units from notes is a *text* operation and must never cost a model context |
| `tools/promote_catalogue.py` | **Rewrite** for your catalogue. Keep the generated/hand-written marker line |
| `tools/reading_order.py` | **Copy the idea** if the notes have a reading order that differs from the narrative order — and it usually does: a reader needs the اصول before the material they govern; a listener needs the story in the order it happened |
| `series/deck2.py`, `deckkit.py`, `build_full_deck.py`, `pack.py`, `preview.py`, `make_*visuals.py` | **Only for a lecture output.** Otherwise leave behind |
| `docs/DECISIONS.md`, `docs/STATUS.md` | **Copy the *format*, start the content empty** |

---

## 11. The first-week runbook

**Day 1 — frame.** Fill in `CLAUDE.template.md` → `CLAUDE.md` (§13). Write `SOURCES.md` with the
tiered list **and its justification from inside the subject's own frame**. Open `DECISIONS.md` with
decision #1: what the output is, and who it is for. Create the skeleton (§1). Commit.

**Day 2 — tooling.** Copy `shamela.py`. Fetch and cache the TOC of each primary work
(`shamela.py toc <id>`). Copy `check_citations.py` and edit `BANNED`. Verify the whole loop on one
real page: fetch → quote in a scratch note → run the checker → watch it pass → corrupt one letter →
**watch it fail**. Do not skip that last step; a checker nobody has seen fail is not a checker.

**Day 3 — the first note.** Pick the narrowest genuinely useful question. Write one note in the §5
format, end to end, including the "could not be established" section. Add its `INDEX.md` row. Run the
checker. Render it to PDF and *read the PDF*.

**Day 4 — the unit.** Decide the unit format (§6.3), write ~20 units into that note, and write
`check_cards.py` for those exact fields **the same day**.

**Day 5 — the gates and the catalogue.** Write `promote_catalogue.py` for the extractable catalogue
files. Write `check_introductions.py` if the topic has people or terms. Run all four. Fix what they
flag — and nothing else.

**Day 6 — the first deliverable.** Build one small end-to-end artifact from the units. Not a good
one — a complete one. The point is to discover which fields the artifact actually needs, while
changing the unit format is still free.

**Day 7 — write it down.** Every decision that took more than a minute goes into `DECISIONS.md`
**with its reason**, the same day. Update `STATUS.md` with a resume point that a cold session could
start from.

---

## 12. Mistakes already paid for — do not re-buy them

1. **Research left in a chat transcript.** It is gone. Write the note.
2. **A flat source list.** The weakest source becomes the authority for whatever only it carries.
3. **Citing the Shamela index instead of the printed page.** Meaningless to a reader with the book.
4. **Trusting a second model to verify quotations.** Expensive, and wrong often enough to matter. It
   is string work — script it.
5. **Skipping the promotion step.** 28,825 lines of research and a catalogue frozen six weeks back;
   the symptom appeared as good material reaching no artifact.
6. **Apparatus on an audience face.** Survives every human review, then appears on a projector.
7. **Markdown for a two-script printable.** Unreadable. HTML → Chrome → PDF, fonts embedded.
8. **Arabic-Indic digits beside Latin punctuation.** Reordered into nonsense by bidi. Twice.
9. **A CDN webfont in a printable.** Silent fallback at the print shop, Arabic destroyed.
10. **One unit carrying nine events.** It cannot be cut, cannot be reordered, and cannot be checked.
    One unit, one thing.
11. **The opposite error, also paid for:** one unit *per beat*. An evening built that way ran to 356
    slides and bored the room. Keep beats **inside** the unit as a `Beats:` list that feeds the
    speaker notes; do not promote them to units.
12. **An introduction that lives inside an optional block.** The block gets cut and a stranger walks on.
13. **A name or term that was never introduced at all.** Invisible to every other check. Build
    `check_introductions.py`.
14. **Re-fetching a page that is already in the cache.** Check the cache. Grep the TOC.
15. **Quoting from an OCR text layer.** Locate by grep, quote by eye.

---

## 13. The blanks to fill before the first research pass

Copy `docs/handoff/CLAUDE.template.md` to the new repo's `CLAUDE.md` and answer every ⬜. Until they
are all answered, do not start researching — each unanswered blank is a decision that will otherwise
get made implicitly, differently, three times.

1. ⬜ **The subject**, in one paragraph, and **what a reader/listener can do afterwards that they
   could not before**.
2. ⬜ **The output**, precisely: a lecture series / a book / a reference work / a curriculum. This
   decides how much of the delivery layer you take.
3. ⬜ **The audience**, and their level. It sets the register and the glossing threshold.
4. ⬜ **The spine** — the named work built on, said openly.
5. ⬜ **The tiered source list**, with the justification from inside the subject's own frame (§3).
6. ⬜ **The excluded sources**, each with its reason.
7. ⬜ **The contested ground** the topic contains, the guardrail for it, and **where the guardrail is
   installed** — which must be before the material that needs it.
8. ⬜ **The unit of output** and its exact fields (§6.3).
9. ⬜ **The language policy.** Which language carries the artifacts; which appears only as verbatim
    quotation; what the model is and is not permitted to generate. In this repo: **English carries
    everything, and Claude generates no Urdu at all** — the speaker's own Urdu is better than any
    machine rendering, so he translates by hand. Decide this on day one; it is expensive to reverse.
10. ⬜ **The gates**, and the command line for each.

---

## 14. One paragraph, if only one thing survives

Fetch Arabic from Shamela into a committed cache; quote it verbatim in a blockquote of its own with
the **printed** page and the live link; label every claim `[SOURCED]` / `[STANDARD]` /
`[CONVENTIONAL-ESTIMATE]`; write what you could **not** establish; promote settled facts out of the
notes into a catalogue that every artifact reads from; end each note in small uniform units that are
the only place a fact is authored; and let a **script**, not a model, decide whether each quotation is
really on the page it cites. Everything else in this document is detail hanging off that sentence.
