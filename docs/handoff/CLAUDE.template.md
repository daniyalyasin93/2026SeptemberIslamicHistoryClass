# ⬜ PROJECT NAME — ⬜ one-line description

> **This is a template.** Copy it to the new repo's `CLAUDE.md`, answer every ⬜, and delete this
> block and every parenthetical *(guidance)* line. Read `METHOD_HANDOFF.md` first — it carries the
> reasons; this file carries only the rules.

⬜ *One paragraph: the subject, the output, the audience, and what a reader or listener can do
afterwards that they could not before.*

**Author / speaker:** ⬜ *name, relevant strengths, relevant weaknesses. Say the weaknesses plainly —
they decide how much over-preparation the artifacts need.*

**Output:** ⬜ *a lecture series / a book / a reference work / a curriculum / other — precisely.*

---

## 0. Start here — never re-derive what is already written down

**Read these files before doing anything else. They are the whole context.**

| File | What it holds |
|---|---|
| `docs/STATUS.md` | Where everything stands *right now* — what is built, what is blocked, what is next |
| `docs/DECISIONS.md` | Every settled decision with its reason. **Append-only** |
| `docs/research/INDEX.md` | The research catalogue — grep it before researching anything |
| `docs/catalogue/SOURCES.md` | The tiered source list and why it is the list |
| ⬜ | ⬜ *the current production spec, once there is one* |

### 0.1 The research catalogue rule (standing instruction)

> **Before any research pass, grep `docs/research/INDEX.md`. If a note already answers the question,
> read it and build on it — re-derive only what is genuinely stale or out of scope. After any
> substantial pass, write a durable page-cited note into `docs/research/` and add its row to the
> index.**

Notes are **committed to the repo**. This deliberately overrides the global convention of keeping
research in a gitignored `.claude/` — these notes are the project's asset and must survive a machine
change. Each note must carry: the question · findings with **PRINTED** pages · verbatim Arabic
exactly as fetched · **what could not be established** · which Shamela indices were fetched.

**Readability is part of the format.** Arabic sits on its **own line, in its own blockquote** — never
inline inside an English sentence — with the printed page **and the direct `shamela.ws` URL**
immediately beneath it. Every note renders to an A4 PDF via `tools/render_note.py`; the `.md` stays
canonical and greppable, the PDF is what gets read.

Certainty labels, used everywhere: **`[SOURCED]`** (a page was read — give it) ·
**`[STANDARD]`** (conventional, not yet page-cited here — carries `(to verify)`) ·
**`[CONVENTIONAL-ESTIMATE]`** (general scholarship; our sources do not fix it — **must be labelled as
such on the artifact face itself**).

### 0.2 Preserve decisions, not conversations

Any decision that took more than a minute to settle goes into `docs/DECISIONS.md` **with its reason**,
the same day. A decision that lives only in a chat transcript gets re-litigated from scratch next
session, at full cost, and often gets re-decided differently.

Once a fact is settled, **promote it out of the research note into `docs/catalogue/`** — that is what
artifacts read from. Research notes are the working record; the catalogue is the source of truth.

### 0.3 Costs worth avoiding

- **Grep the cached TOCs before fetching:** ⬜ *`sources/shamela/<id>/_toc.tsv` for each primary work.*
- **A Shamela page fetched once is cached forever** under `sources/shamela/<book>/<index>.txt`.
  Check the cache before fetching.
- ⬜ *Any source here that is known-bad and must not be read — a garbled OCR layer, a volume with no
  text layer, a scan that exists only for eyeballing page images. Name the file and say why.*

---

## 1. Non-negotiable rules

### 1.1 References are airtight or absent

Never fabricate a citation, date, title, hadith number, page or URL. **Wrong is worse than absent.**
Cite only what traces to a source in `sources/`. If uncertain, write `(to verify)` — never state it.

**How to cite:** always the **PRINTED** page and volume (`ج۷ ص۱۳۴`) — the page in the physical book,
which is what a reader could look up. **Never the Shamela index**; it is an internal sequential
number and differs from the printed page (usually by one). `tools/shamela.py` reports both.

⬜ *If the repo holds scanned PDFs, paste the OCR caveat here: the text layer is reliable for
**locating and page-anchoring** and not for wording — **locate by grep, quote by eye** against the
page image before any verbatim use.*

### 1.2 Register: ⬜ *(e.g. dignified, never theatrical)*

⬜ *Who the audience is, in one line, and what that forbids.*

- **Never** use cast / character / villain / hero / episode / trailer / plot twist for real figures on
  any audience-facing artifact. Those words may exist only in planning chat.
- Honorifics always: ﷺ · ؓ for Companions · رحمہ اللہ for the ʿulamā.
- **Memorability comes from the tradition, not from invention.** Use the لقب the tradition already
  gave. Where a figure has none, use a plain factual descriptor from the source. **Never invent one.**
- **No emblems, sigils, icons or assigned objects for people.**
- Interest comes from real material told plainly, not from manufactured suspense.

### 1.3 Language and type

- ⬜ **The language policy.** *Which language carries every artifact; which appears only as verbatim
  quotation; what the model is and is not permitted to generate. Be absolute — a partial policy is
  re-litigated weekly. Template: "**⬜ carries everything.** Slides, scripts, briefings and research
  notes are written in ⬜. **Claude generates no ⬜ at all.** Arabic appears **only** as verbatim
  quotation from a source, in Naskh, with an English rendering beneath it."*
- **Arabic font: `Traditional Arabic`** (Naskh). Qurʾānic text and Arabic quotations stay Naskh;
  **Nastaliq for Qurʾān is non-standard.**
- ⬜ *If the repo carries Urdu:* **`Noto Nastaliq Urdu`**. Not `Jameel Noori Nastaleeq` unless the cut
  is verified — the common one is the *Kasheeda* variant, which renders every line stretched and gappy.
- **Latin digits in English contexts, always.** Arabic-Indic digits mixed with Latin punctuation get
  reordered by the bidi algorithm into nonsense.
- **Never put two scripts in the same line or the same table cell.** Give the non-Latin script its own
  block with `dir="rtl"`.
- Arabic/Urdu strings: single spaces only; never leave Latin letters inside an Arabic word.

### 1.4 Arabic carries authority — use it wherever the source supplies it

A real Arabic quotation is free credibility. Where the source gives a saying in Arabic, **put the
Arabic on the artifact in Naskh with the rendering beneath it** — not the rendering alone.

**Never compose Arabic ourselves.** Only reproduce what a source actually carries, and read it off the
page image before it reaches an audience face — a single garbled letter changes the word.

### 1.5 Standing context ⬜

⬜ *Venue / publisher / organisation · recording policy · question policy · deadlines · anything about
the setting that constrains content. In the origin repo this table is what stops the same logistical
question being asked four times.*

### 1.6 Content safety

Sunni framing, presented as such. No novel claims. When in doubt, narrate what the source narrates and
stop.

⬜ **The contested ground this subject contains, and the guardrail.** *Name it. Say what the guardrail
is, and **where it is installed — which must be before the material that needs it, never after**. Say
plainly that the position is never improvised on the spot and that the author defers to the place
where it is handled with اصول.*

---

## 1.7 Artifact rules learned the hard way

**An audience-facing face carries only what the audience may see.** Certainty labels, tier tags, unit
ids, cross-references, build markers, `n/a`, image-brief text, the words Claude/Gemini/AI, and raw
URLs are **production apparatus** and belong in the notes channel. Enforce this with a `FORBIDDEN`
list that **fails the build** — it is the class of defect that survives every human review and then
appears on a projector.

⬜ *If the output is a deck, paste the deck contract here: background, minimum type size, words per
face, permitted kinds, whether bullet lists exist, image placeholders. State the hard numbers — a
contract without numbers cannot be asserted in a build script.*

⬜ *If printables are produced:* they are **HTML + CSS → headless Chrome → A4 PDF, fonts base64-embedded
via `@font-face`** — never Markdown (it cannot keep two scripts apart), never a CDN webfont (no
network at the print shop means a silent fallback and the Arabic is destroyed).

**Over-prepare.** Build roughly **2×** what the slot or the page count needs and cut. Overflow rolls
forward; it is never compressed. Coverage is never bought by speeding up.

### Nothing walks on stage un-introduced — the standing check

**Before any deliverable is built, every name and every term it uses is tested against what the
audience has actually been told.**

```bash
python tools/check_introductions.py ⬜<target>      # exits non-zero while a row is unanswered
```

It reports every proper name appearing for the first time — in nothing previously delivered and in no
earlier unit of this one. **The deliverable answers every row** in a `## Introductions checked` table,
and **"no notice needed" is a valid answer** — the rule is that somebody looked.

**Run the same question over four kinds of thing:** **people** (a name carries units with no notice) ·
**events** (a unit depends on something that is on no unit) · **terms** (a line's force rests on
something unglossed) · **forward references** (the work names something from a part not yet given).

**Two traps the tool cannot see.** A name introduced only inside an optional block is not introduced —
the notice belongs on a unit that is never cut. And anything delivered before the ledger existed is
not in the known set; answer those rows by hand.

---

## 2. ⬜ The fixed shape

⬜ *The shape the output always takes — the session runsheet, the chapter skeleton, the entry
template. The furniture never changes; only the content does. That is what lets a newcomer catch up
and what stops the author from ever being lost. Give it as a block, with timings or lengths.*

---

## 3. ⬜ The arc

⬜ *The ordered table of parts: number · title · scope. Then state plainly whether it is a **sequence
or a schedule** — in the origin repo it is a sequence, parts may exceed the planned count, and that is
the intended behaviour.*

---

## 4. Layout and conventions

```
CLAUDE.md              this file
docs/catalogue/        the durable knowledge base — SINGLE SOURCE OF TRUTH
  SOURCES.md           the tiered list; what we hold; what is still to obtain
  SHAMELA_LOG.md       every Arabic page used, and what it was used for
  ⬜                    ⬜ the catalogue files this subject actually needs
docs/research/         page-cited notes + INDEX.md
docs/specs/            the design specs
sources/shamela/       the fetch cache — COMMITTED, not gitignored
sources/pdf/ text/     held PDFs and their page-marked extractions
tools/                 shamela.py + the gates
⬜                      ⬜ the per-deliverable folders
archive/               superseded work, kept as a parts bin
```

**Never let two artifacts disagree.** A date, a name or a page number goes into `docs/catalogue/`
first; every artifact reads it from there.

### The source list

⬜ *The tiered table — Spine / Primary / Judgement-only / Corroboration-only / Excluded — with the
justification from inside the subject's own frame, and a reason beside every exclusion. See
`METHOD_HANDOFF.md` §3.*

**Every Shamela page used gets a line in `docs/catalogue/SHAMELA_LOG.md`.** Nothing from Shamela
enters an artifact without one.

---

## 5. Build commands

```bash
# fetch a citable Arabic page from al-Maktaba al-Shamela (cached under sources/shamela/)
python tools/shamela.py get <book> <index>        # one page  -> reports the PRINTED page too
python tools/shamela.py range <book> <a> <b>      # a span
python tools/shamela.py toc <book> --find "<text>"  # whole TOC in one fetch, cached

# the gates — run before every commit that touches a note or a unit
python tools/check_citations.py                   # non-zero while any quotation is unverified
python tools/check_cards.py ⬜<pool>
python tools/check_introductions.py ⬜<target>
python tools/promote_catalogue.py                 # regenerate the extractable catalogue files

# render a note to a readable A4 PDF
python tools/render_note.py docs/research/<note>.md

# extract a scanned source to page-marked text (offset auto-detected)
python tools/extract_source.py sources/pdf/<f>.pdf sources/text/<f>.txt

# HTML -> A4 PDF, fonts base64-embedded
chrome.exe --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf=out.pdf file:///absolute/path/in.html
```

⬜ *Palette and faces, if there are artifacts with a look.*

**Verification that can be done by string comparison is never done by a model.** The quoted Arabic
either occurs on the cited page or it does not — that is string work, so a script does it for nothing,
and **the model is only ever asked to fix what the script flags**.

⬜ *Network reality on this machine: what resolves, what needs a browser User-Agent, what is blocked.
Re-test it rather than inheriting a stale note.*

⬜ **Book ids found so far:** *keep this list growing at the bottom of the file — it is the cheapest
thing here and the most re-derived.*
