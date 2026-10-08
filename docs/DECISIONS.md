# DECISIONS — append-only log

Every settled decision, with its date and its reason. **Append; never rewrite history.** When a
decision is replaced, add a new entry and mark the old one *superseded by #N*.

**Why this file exists:** a decision that lives only in a chat transcript is re-litigated from
scratch every session, at full token cost, and often re-decided differently. If a question took
more than a minute to settle, it belongs here.

**How to use it:** read this file before proposing any change to the series shape, the register,
the sourcing rules or the artifact pipeline. If your proposal contradicts an entry here, say so
explicitly and give a reason — do not quietly reverse it.

---

## Index

| # | Date | Decision | Status |
|---|---|---|---|
| 1 | 2026-08-26 | Venue, organisation and question policy | active |
| 2 | 2026-08-26 | Series shape: whole arc first, then zoom | **superseded in part by #12** |
| 3 | 2026-08-26 | Sourcing is just-in-time, per session | active |
| 4 | 2026-08-26 | Register: dignified, classical ⁨تراجم⁩; no invented alqāb, no emblems | active |
| 5 | 2026-08-26 | The safe Sunni source list; Ṭabarī corroboration-only | active |
| 6 | 2026-08-27 | English carries the slides | active |
| 7 | 2026-08-27 | Noto Nastaliq Urdu; never Jameel Noori | active |
| 8 | 2026-08-27 | Latin digits on slides, always | active |
| 9 | 2026-08-27 | Method content cut to a minimum; no recurring methodology slot | active |
| 10 | 2026-08-27 | No bare-text slides | active |
| 11 | 2026-09-03 | *⁨تاریخِ امت⁩* vols 2–4 are not OCR'd; build on the Arabic spine meanwhile | active |
| 12 | 2026-09-03 | **Session 1 rebuilt: orientation + Medina + Saqifah, not a 1400-year sprint** | active |
| 13 | 2026-09-03 | The whole arc survives as **pegs on the grand timeline**, not as narrative | active |
| 14 | 2026-09-03 | **The guardrail moves to session 1**, carried by the ⁨حدیث⁩/⁨تاریخ⁩/⁨فقہ⁩ distinction | active |
| 15 | 2026-09-03 | **No separate ⁨تعارف⁩ block in session 1**; people introduced inside the story | active |
| 16 | 2026-09-03 | Prophets timeline: approximate centuries, explicitly labelled as outside the sources | active |
| 17 | 2026-09-03 | Worksheets printed and handed out; marked in the room only if time permits | active |
| 18 | 2026-09-03 | **Research is catalogued in `docs/research/` and never re-derived** | active |
| 37 | 2026-09-16 | One slide per event: every card carries Beats | **point 3 superseded by #39** |
| 39 | 2026-09-19 | **Back to one slide per card; beats move to the speaker notes** | active |
| 40 | 2026-09-19 | Speaker notes are speaking points; card id and tier are out of them | active |
| 41 | 2026-09-19 | The Umm Tamīm ؓ connection is recorded, and is not spoken | active |
| 42 | 2026-09-19 | **Evening 4 runs in chronological order; Kinda is last** | active |
| 43 | 2026-09-19 | **Nothing walks on stage un-introduced** — `check_introductions.py` is the gate | active |
| 44 | 2026-09-22 | **Evening 4 is cut to Parts I–IV, ending at STOP C**; Kinda rolls to evening 5 | active |
| 45 | 2026-09-22 | **Bridge slides at the seams** — a deck is read as a story, not card by card | active |
| 46 | 2026-09-22 | Evening 4 review: authored face excerpts, no spoilers in the notes, maps rendered by the build | active |
| 47 | 2026-09-22 | **Evening 4 carries an overflow Part V behind the planned close** | **in-place closes superseded by #59** |
| 48 | 2026-09-22 | Part VI — the dead of al-Yamāma behind Part V; the muṣḥaf is the last word | active |
| 49 | 2026-09-23 | The whole al-Yamāma household pool goes in; what is not reached opens evening 5 | active |
| 50 | 2026-09-23 | The households go in as well — Parts IX–XI, behind the close | **"behind the close" superseded by #57** |
| 51 | 2026-09-23 | The missing-detail audit — four notes read against the 82 cards | active |
| 52 | 2026-09-23 | The dialogue over the ⁨جمع⁩, and Ibn Kathīr's numbers as he gives them | active |
| 53 | 2026-09-23 | One more close, where the map actually moves — STOP D | **superseded by #59 from evening 5** |
| 54 | 2026-09-23 | The garden card — who called them in, and whose son killed him | active |
| 55 | 2026-09-24 | Evening 4's deck is hand-finished and protected (`S04.FINAL`) | active |
| 56 | 2026-09-27 | **What evening 4 taught** — four reports from the lectern | active |
| 57 | 2026-09-27 | **Evening 5: the houses are told where their men fall; Oman and Mahra close it** | active |
| 58 | 2026-09-27 | **Maps build up on clicks** — troops move as the speaker speaks | active |
| 59 | 2026-09-27 | **Checkpoints, not mid-evening closes**; one real close | active |
| 60 | 2026-09-27 | **The lectern is the deck's notes; the home reading is one PDF of them** | active |
| 61 | 2026-09-27 | **Every card answers the question the room will ask next** | active |
| 62 | 2026-09-27 | **One flashback per man** — the houses cut to what makes a death land | active |
| 63 | 2026-09-27 | **Where a card moves, its map is its slide** — never a map, then the card again | active |
| 64 | 2026-09-27 | **A map fades what a click has finished with; the road stays** | active |
| 65 | 2026-09-27 | **Each house opens on a family tree**; its notes keep every cut story | active |
| 66 | 2026-09-27 | **The Qurʾān's collection told whole; Ḥaḍramawt ends ʿIkrima's ؓ road**; Bahrayn after | active |
| 67 | 2026-10-01 | **The family trees are editable org charts**; the house of ʿUtba grows to its famous in-laws | active |
| 68 | 2026-10-01 | **Face headlines are names, not sentences** — the dead of al-Yamāma headed by the Companion's name | active |
| 69 | 2026-10-01 | **A front closes on its map before the next opens** — Oman settled before Mahra | active |

---

## 1 · Venue, organisation and question policy — 2026-08-26

DHA **Islamabad**. Host: **Tanzeem-e-Islami**, who also review sensitive material. **No recording,
no filming.** **No questions during the 45 minutes** — written slips into a box at the door, speaker
stays 15 minutes afterwards for one-to-one. Identical in all ten sessions. No session falls in ⁨محرم⁩.
The book is named openly to the room.

**Why:** settled with the host. The no-live-questions rule is also the speaker's main protection
against being pushed to adjudicate the ⁨مشاجرات⁩ from the floor.

**Implication:** ⁨خلافت⁩ → ⁨ملوکیت⁩ (session 4) and the ending of the caliphate in ۱۹۲۴ (session 7) sit
close to the host organisation's own reason for existing. Narrate what the book narrates; let the
quoted authorities carry every conclusion; decline to adjudicate.

## 2 · Series shape: whole arc first, then zoom — 2026-08-26

Session 1 gives the complete 1400-year shape so every later session has somewhere to hang.

**Superseded in part by #12** — the *job* (orientation) is kept; the *method* (narrative sprint)
is replaced. See #12 and #13.

## 3 · Sourcing is just-in-time, per session — 2026-08-26

Each session is gated on its own source. The architecture must not depend on holding every volume.

**Why:** OCR costs money and time; a design that needs all volumes up front cannot start.

## 4 · Register — 2026-08-26

Dignified, never theatrical. Classical ⁨تراجم⁩ format for people. **Never** cast / character /
villain / hero / episode / trailer / plot twist for real figures on any audience-facing artifact.
Honorifics always. **Never invent a ⁨لقب⁩ or a tagline for a Companion** — use only what the tradition
gave. **No emblems, sigils, icons or assigned objects for people.**

**Why:** mature religious audience. Entertainment framing applied to the Ṣaḥāba ؓ is disrespectful
and will cost the speaker the room.

## 5 · The safe Sunni source list — 2026-08-26

General narrative use: **⁨البدایہ والنہایہ⁩ (30097)**, **⁨سیر أعلام النبلاء⁩ (10906)**,
**⁨الکامل⁩ (21712)**, **⁨الإعلان بالتوبيخ⁩ (34)**. All four are named and relied on by the course's own
⁨مقدمہ⁩, so citing them stays inside the course's frame.

**⁨تاریخ الطبری⁩ (9783) is corroboration only, never alone**, and never for anything touching the
⁨مشاجرات⁩ — it collects with chains and does not sift, and presence in Ṭabarī is not authenticity
(⁨مقدمہ⁩ p.۷۱). ⁨یعقوبی⁩ and ⁨مسعودی⁩ are flagged for sectarian lean (p.۴۶) and are not used without a
specific decision.

## 6 · English carries the slides — 2026-08-27

Headlines, structure, labels and translations in English. Urdu appears only where it does real work,
always with an English rendering beside it. Arabic quotations stay in Naskh with an English
translation beneath.

**Why:** DHA Islamabad audience reads English faster than Urdu. The first decks were rejected partly
for being unreadable at the back of the room.

## 7 · Urdu font — 2026-08-27

**`Noto Nastaliq Urdu`.** **Never `Jameel Noori Nastaleeq`** — the only cut on this machine is the
*Kasheeda* variant, which elongated letters and rendered every Urdu line stretched and gappy.
Arabic uses **`Traditional Arabic`** (Naskh). **Nastaliq for Qurʾān is non-standard.**

**Why:** a real, observed rendering defect in the first decks, not a preference.

## 8 · Latin digits on slides — 2026-08-27

Always, in English contexts. Urdu-Indic digits mixed with Latin punctuation get reordered by the
bidi algorithm into nonsense. Never put Urdu and English in the same line or table cell.

**Why:** a real bug in both the first handout and the first decks.

## 9 · Method content cut to a minimum — 2026-08-27

The weekly «⁨کیسے پتا چلا؟⁩» segment was cut as too academic. What survived: one four-minute
"two ways of knowing the past" slide in session 1, plus the ⁨سفیان ثوری⁩ quotation.
**Do not reintroduce a recurring methodology slot.**

*Note:* #14 puts a short method block back into session 1 — but as the **guardrail**, not as a
recurring slot. #9 stands for sessions 2–10.

## 10 · No bare-text slides — 2026-08-27

Every content slide carries a map, the timeline strip, a large statement, or a sourced quotation.
**Why:** the first decks were rejected as "too dry" and they were.

## 11 · *⁨تاریخِ امت⁩* vols 2–4 are not OCR'd — 2026-09-03

The three large volume PDFs have **no usable text layer**. Daniyal will OCR them himself and has
not yet. Meanwhile, build from the **Arabic spine on Shamela** — ⁨البدایہ، سیر، الکامل، الإعلان⁩ —
which is inside the course's own frame.

**Do not plan any session around vols 2–4 until Daniyal says the OCR is done.**

Also settled: `sources/pdf/*_text.pdf` (00–25in, jm) are scans of ⁨سیر أعلام النبلاء⁩ with a badly
garbled OCR layer. **Use Shamela 10906 instead.** Those PDFs are for eyeballing page images only.

## 12 · Session 1 rebuilt — 2026-09-03

**Session 1 is no longer a 1400-year narrative sprint.** It is now:

> **orientation in time and space → the power structure of Medina → ⁨سقيفة بني ساعدة⁩ → the map of
> Arabia on the eve of the ⁨ردة⁩, as next week's question.**

**Why (Daniyal's proposal, and the reasons it was accepted):**

- A 45-minute race through fourteen centuries is the most praised and least remembered lecture
  format there is. Nothing sticks because nothing is concrete.
- The nested zoom-out — Pakistan → the Ummah → the prophets — anchors the unfamiliar to the
  audience's own lived timeline, and does the orientation job *better* than a narrative can, because
  it is visual, scale-aware, and lands on a sheet of paper they keep.
- ⁨سقيفة⁩ is narrated everywhere and understood almost nowhere, because nobody first explains who
  ⁨الأوس⁩ and ⁨الخزرج⁩ were or why the Anṣār had a claim at all. **Teaching Medina's clan structure
  before the event is the single strongest idea in the rebuild.**
- Ending the evening the night before the ⁨ردة⁩ hands session 2 its opening cleanly. **Nothing
  renumbers** — L02 «⁨بارہ سال⁩» already opens on the ⁨ردة⁩.

**Cost accepted:** a one-off attendee no longer hears the whole story narrated. Mitigated by #13.

## 13 · The whole arc survives as pegs, not narrative — 2026-09-03

The grand Ummah timeline in session 1 carries **the full arc as marked pegs** — ⁨۱۱ھ⁩ · ⁨۱۳۲ھ بغداد⁩ ·
⁨۶۵۶ھ منگول⁩ · ⁨۸۵۷ھ قسطنطنیہ⁩ · ۱۹۲۴ · ۱۹۴۷ — so the objective in the v2 spec ("a usable mental map of
Islamic history") is still met on the night.

**Why:** the audience gets the empty shelf in week 1 and fills it over ten weeks, instead of watching
the contents race past once. This is a scaffold, not a summary.

## 14 · The guardrail moves to session 1 — 2026-09-03

The guardrail — **⁨تاریخِ اسلام⁩ = ⁨تاریخِ مسلمین⁩**, and the fiqh that studying the ⁨مشاجرات⁩ without
need is ⁨مکروہ⁩ — was scheduled for session 3, deliberately ahead of anything sensitive.
**⁨سقيفة⁩ is now in session 1, so the guardrail comes with it.**

Its vehicle is Daniyal's own proposed opening, the **⁨حدیث⁩ / ⁨تاریخ⁩ / ⁨فقہ⁩** distinction: in fiqh a
report must be authentic to bind; in ⁨تاریخ⁩ we record what was reported in order to fix sequence.
**Therefore a ⁨تاریخ⁩ report is neither a ruling nor a creed, and we do not judge between Companions.**

**Why:** ⁨سقيفة⁩ is the most contested episode after ⁨کربلا⁩. In a Tanzeem-e-Islami room with written
question slips it *will* draw questions on ⁨علی ؓ⁩'s bayʿah, ⁨فدک⁩, and whether the Anṣār were wronged.
Sixty seconds at the top of the evening turns a safety problem into the session's intellectual spine.

Session 3 still installs the **fuller** fiqh treatment for the ⁨مشاجرات⁩ proper. #14 does not replace it.

## 15 · No separate ⁨تعارف⁩ block in session 1 — 2026-09-03

Daniyal's call. Instead of a detached seven-minute ⁨تعارف⁩, the people are introduced **as the
dynamics of ⁨سقيفة⁩ are explained** — each one named where he becomes load-bearing, with his clan.

**Why:** in this session the people *are* the content. A separate block would introduce them twice.

**The retention ritual is preserved, not dropped:** session 1's hand-writing exercise becomes the
**Medina clan chart worksheet** — the audience writes the chiefs' names into the tree themselves.
Same mechanism (handwriting), applied to the evening's actual substance.

**Scope:** session 1 only. The fixed 45-minute shape in `CLAUDE.md` §2 resumes at session 2.

## 16 · Prophets timeline uses labelled approximate centuries — 2026-09-03

The third timeline shows the prophets by **approximate century**, purely to convey distance from our
own time. Every such date carries the label **`[CONVENTIONAL-ESTIMATE]`** and the slide says plainly
that these are estimates from general scholarship which **our Islamic sources do not fix**.
⁨آدم ؑ⁩ and ⁨نوح ؑ⁩ go **off-scale** — no number is invented for them.

**Why:** Daniyal wants the sense of distance, and rule §1.1 forbids stating what cannot be traced.
The honest caption — *the order is known from revelation, the dates are not* — is itself a better
teaching point than a fake number, and it reinforces the method message the evening opens with.

## 17 · Worksheets go home; marking in the room is optional — 2026-09-03

The timeline and map worksheets are printed and handed out. **One peg is marked live if time
permits**; the rest is taken home. Daniyal's call.

**Why:** the plan as proposed was ~75 minutes of material in a 45-minute slot, and doing the
worksheets in the room was the most expensive block that did not carry new content.

## 18 · Research is catalogued and never re-derived — 2026-09-03

Daniyal's standing instruction. **Every substantial research pass writes a durable, page-cited note
to `docs/research/`, indexed in `docs/research/INDEX.md`.** Before any research, grep the index.

**Why:** the same sourcing was being re-derived across sessions at full token cost, and re-derived
answers drift — two artifacts end up disagreeing about a date or a page.

**Note:** this deliberately **overrides** the global convention of keeping research in `.claude/`
(which is gitignored). These notes are **committed**, because they are as much a course asset as the
catalogue is, and they must survive a machine change. See `CLAUDE.md` §0.

## 19 · English carries every artifact; Daniyal translates the Urdu himself — 2026-09-06

Daniyal's call, after session 1: *"build the lecture in english (with arabic statements from the
original sources, your urdu is not good, i will translate myself)."*

**Every artifact this repo generates is written in English** — slide headlines and body, the
briefing, the cue sheet, the worksheet, the content pool, the research notes. **Arabic appears only
as verbatim quotation from a source**, in `Traditional Arabic` Naskh, with an English rendering
beneath it. **No Urdu is generated by the tooling or by Claude at all.** Daniyal renders whatever
Urdu he wants, at the lectern or by hand-editing the deck.

**Why:** machine-composed Urdu was reading as stilted to a native speaker, and the register damage
was worse than the benefit. English was already carrying the slides (`CLAUDE.md` §1.3, settled
2026-08-27); this extends the same rule to the scripts and packs. Existing Urdu session *titles*
(«⁨بارہ سال⁩» and the rest) stay as they are — they were chosen by Daniyal, not generated.

**This supersedes** the parts of `CLAUDE.md` §1.3 that had Claude producing Urdu prose. The rule
that Urdu, when it does appear, is in Arabic script and never Roman is **unchanged**.

## 20 · A session ships as an over-built pool, not a finished lecture — 2026-09-06

Daniyal's call: *"add the content for both, with more and more events, maps, great statements and
dialogues, and i will filter myself in the final produced version."*

The per-session deliverable is **`CONTENT.md` — a numbered pool of event cards**, each carrying:
what happened · the date with its certainty label · the map move · the verbatim Arabic
statement or dialogue with its `shamela.ws` link · one ⁨عبرت⁩ line · and a tier tag
**`CORE` / `GOOD` / `CUT`**. Daniyal deletes rows; what survives is the lecture.

**Consequence, accepted deliberately:** where a session's pool overflows its slot, the overflow
**rolls into the next session** rather than being compressed. The ten-session arc in `CLAUDE.md` §3
is therefore a **sequence, not a schedule** — sessions may exceed ten. Coverage is never bought by
speeding up. This is the direct fix for the session-1 feedback *"it shouldn't feel like a history
speed-run."*

**Corollary:** because the stopping point is unknown at build time, **closing artifacts are built
for every plausible stopping point**, not just one.

## 21 · Slides: white ground, hard type floor, no bullet slides — Gemini supplies the visuals — 2026-09-06

Session-1 feedback from both managers: *"text-heavy with font size unreadable on ladies side"*,
*"more visual/graphical content"*, and Daniyal: *"the slides you made were ugly, i have in general
lost hope that you can make good slides."*

The division of labour is now explicit. **Claude produces the words and the structure; Gemini
produces the pictures; Daniyal merges.** Therefore:

- **Background is flat white `#FFFFFF`** on every slide. Series identity comes from a teal
  `#104A43` title bar and a gold `#C49A45` rule, **not** from a coloured ground. A flat white
  ground is the one colour Gemini reproduces exactly, so a generated image drops in with no seam.
- **`SLIDES.md` carries a paste-ready `IMAGE BRIEF:` for every visual slide** — the prompt Daniyal
  gives Gemini, including the `#FFFFFF` instruction and the target aspect ratio.
- **`build.py` enforces, and fails the build on violation:** nothing below **24pt**; body **28pt**;
  a key statement **44pt+**; **≤20 words** of body text per slide.
- **Bullet-list slides do not exist.** Every content slide is one of four kinds: a full-bleed
  image or map · a large statement (Arabic Naskh + English beneath) · a diagram · the timeline strip.
- The deck ships **editable** with correctly-sized image placeholder boxes, never flattened.

## 22 · The lectern carries a one-page cue sheet; prose lives in the briefing — 2026-09-06

Feedback: *"the script you wrote had a lot of text, so it was hard for me to follow"*, and from the
managers: *"Do not read from script. In notes, one can have the key headings, names and dates
written before one, but not full sentences."*

- **`CUE.pdf` — one page. Headings, names, dates, map cues, and the ⁨عبرت⁩ lines. No sentences.**
  This is the only paper on the lectern.
- **`BRIEFING.pdf` — the prose.** Read twice at home so the story can be told rather than read.
  It never goes to the lectern.
- **The prose speaker script (`Script.md`) is retired** as a delivery artifact. Its narrative
  substance moves into the briefing; its beats move into the cue sheet.

## 23 · The bookend pair — a session's closing two slides open the next one — 2026-09-06

Daniyal's proposal, extended. Every session ends with, in order:

1. **The Line**, with *tonight's* events lit up on it and nothing else — the summary as a picture.
2. **The Map**, showing where the ummah stands **now** against where it stood when the room walked
   in — the evening's change, visible.
3. **Tonight's ⁨عبرت⁩ lines, all on one screen.**
4. Next week's question → **a loud ⁨السلام علیکم⁩, then the dua**, so the room knows it has ended.

**Those same first two slides open the following session**, unchanged. This is what discharges the
managers' *"Start of next lecture: summary of last lecture; realignment in terms of which point in
history we are"* — at zero extra build cost, and it makes continuity something the room sees rather
than something the speaker asserts.

The worksheet's blank timeline strip is **the same strip** shown filled at the close, so the
mid-lecture activity and the closing summary reinforce each other.

## 24 · No live Q&A. Interaction is hands-up plus a silent worksheet — 2026-09-06

The managers asked for both an *"Interactive activity"* and a *"QA session"*. Daniyal's call:
**the activity yes, the Q&A no** — *"map activity could also be done, or timeline activity. no qa
like which could de rail the lecture."*

What is built into the runtime: **three planned hands-up / "guess the year" beats** inside the
narrative (~60 seconds each), and **one 90-second silent worksheet fill** at a fixed point, where
the room marks the blank Arabia map and the blank timeline strip.

The standing Tanzeem policy (`CLAUDE.md` §1.5) is **unchanged**: no questions during the session,
written slips into the box at the door, speaker stays 15 minutes afterwards.

**Why:** an open floor in this room, on this material, is exactly where the ⁨مشاجرات⁩ surface without
⁨اصول⁩ and the evening is lost. The visible interactivity the managers want is obtainable without
handing over control of the room.

## 25 · Every Arabic quotation carries its shamela.ws link, and notes render to PDF — 2026-09-06

Feedback: *"the extensive shamela researched documents, they were good reading, you should do more
of that. however in the .md files the arabic is v hard to read... also references for whatever you
write preferably shamela links should be close at hand."*

- **In `.md`:** Arabic sits on its own line, in its own blockquote, **never inline in an English
  sentence**, with the printed page **and the direct `shamela.ws` URL** immediately beneath it.
- **`tools/render_note.py`** renders any research note to an A4 PDF — Arabic in `Traditional Arabic`
  at a size that can actually be read, English in `Segoe UI`, links live. The `.md` stays canonical
  and greppable; the PDF is what gets read.
- The research-note format is otherwise **kept and expanded** — it is the part of session 1's
  preparation that Daniyal rated highest.

## 26 · One ⁨سبق⁩ line per major event, spoken and on screen — 2026-09-06

Feedback from the floor, endorsed by a manager: *"we should still try to derive lessons or
relatability from at least 25-50% of the events discussed."* Daniyal's choice among the options:
**one line per event**, not a single lesson built to all evening.

After each major event: **one sentence of ⁨عبرت⁩, on its own slide, said plainly, then move on.**
Roughly four or five an evening. All of them reappear together on the closing summary screen, and
each has a line in the worksheet. Every line is added to `docs/catalogue/LESSONS.md`.

**Why one-per-event rather than fewer-and-deeper:** with Tanzeem in the room, a lesson developed
into an explicit present-day parallel is the highest-risk sentence of the evening. A plain ⁨عبرت⁩
drawn from the event itself carries the relatability the audience asked for without inviting the
speaker to adjudicate anything.

## 27 · The weekly «⁨کیسے پتا چلا؟⁩» slot is retired from the session shape — 2026-09-06

`CLAUDE.md` had been contradicting itself since 2026-08-27: §1.7 recorded that the weekly method
segment was **cut as too academic**, while §2 still allotted it three minutes and §3 still said the
whole muqaddima was "redistributed across the weekly «⁨کیسے پتا چلا؟⁩» slot." The session-1 feedback
settles it in the direction §1.7 already pointed — *"proceed calmly… teach history like a canvas of
stories"* leaves no room for a recurring three-minute methodology block.

**The slot is gone from the shape.** What survives: session 1's "two ways of knowing the past"
slide, the ⁨سفیان ثوری⁩ quotation, and **a source remark spoken inside the story** at the moment a
listener would naturally ask "how do we know that?" — never as its own agenda item.

**Why:** the method content was the driest three minutes of the evening and it was competing for
time with exactly the thing the room asked for more of. `docs/catalogue/HOWWEKNOW.md` is kept — it
is now a bank the narrative draws on, not a slot the narrative must feed.

## 28 · People are met inside the story, in every session — 2026-09-06

Decision #15 removed the standalone seven-minute ⁨تعارف⁩ block from session 1 and introduced each
figure at the point he became load-bearing. It was scoped to session 1. **It is now the rule for
every session.**

**The retention ritual is preserved and moves to paper.** The worksheet prints, for each principal
figure of the evening, the classical ⁨تراجم⁩ notice's first three lines — `name + ⁨لقب⁩` · `dates`
(⁨ھ⁩ and ⁨عیسوی⁩, plus a point on the Line) · what he did in one sentence — and leaves **«⁨ایک واقعہ⁩»**
blank for the listener to fill during the 90-second silent worksheet beat (`DECISIONS.md` #24).

**Why:** a seven-minute block of biography in the middle of a 45-minute narrative is the single
most speed-run-inducing structure in the old shape — it forces the story to be told faster to pay
for it. Introducing a man where he matters is also simply better storytelling, which is what the
managers asked for. The mechanism that actually produced retention was the **handwriting**, not
the stage block, and the handwriting is kept.

## 29 · ⁨تاریخ ابن خلدون⁩ joins the source list — for judgement, never as the sole authority — 2026-09-06

Daniyal's call: *"are you also using tareekh ibn khuldun as a source as well? his judgements on
events could be interesting."* He is right, and the reason he is right is the reason the addition
needs a boundary.

**Added:** **`12320` — ⁨تاریخ ابن خلدون⁩ (⁨كتاب العبر وديوان المبتدأ والخبر⁩)**.

**Standing: analysis and framing. Never the sole authority for a fact.**

- **Use him for** the shape of a thing — why the ⁨ردة⁩ took the form it did, what a conquest cost the
  society that made it, why an institution appeared when it did. This is what he is unmatched at
  and it is precisely what a lecture that must carry a ⁨سبق⁩ needs. It is also the thing the four
  narrative works deliberately do *not* do.
- **Do not use him alone for** a date, a name, a number, a chain, or the wording of a saying. For
  the early period his narrative largely follows ⁨الطبری⁩, so citing him alone for a fact is citing
  ⁨الطبری⁩ at one remove — which `CLAUDE.md` §4 already forbids. Any fact taken from him must also be
  found in ⁨البدایہ⁩, ⁨سیر⁩, or ⁨الکامل⁩, and cited from there.
- **Never for the ⁨مشاجرات⁩.** Same rule as ⁨الطبری⁩, for the same reason.

**Where he is in the book, for the 11–23 AH window** (cached 2026-09-06, so this costs nothing to
re-check): indices **1276–1370** — ⁨بعث أسامة⁩ 1280 · ⁨خبر السقيفة⁩ 1284 · the ⁨ردة⁩ 1286–1303 · Iraq
1304–1310 · Shām 1311–1313 · ⁨خلافة عمر⁩ 1314 · ⁨القادسية⁩ 1321 · ⁨المدائن⁩ 1333 · ⁨أجنادين⁩ and
⁨بيت المقدس⁩ 1340 · ⁨عام الرمادة⁩ and ⁨طاعون عمواس⁩ 1350 · ⁨مصر⁩ 1351 · ⁨نهاوند⁩ 1353 · ⁨مقتل عمر والشورى⁩ 1365.

**Why the boundary rather than a plain "yes":** the whole point of `CLAUDE.md` §4's safe list is
that the course's own ⁨مقدمہ⁩ names the works it relies on, so citing them keeps the lecture inside
its own declared frame rather than importing an outside authority the room has not been told about.
Ibn Khaldūn is not in that frame. Bringing him in for *interpretation*, openly labelled as
interpretation, is defensible from the platform — "Ibn Khaldūn reads it this way" is an honest
sentence. Bringing him in for a *fact* would quietly widen the evidentiary base without saying so.

**On the slide and in the room:** when a judgement of his is used, it is attributed to him by name.
It is never presented as what happened; it is presented as how he read what happened.

## 30 · A slide face carries only what the room may see — and every deck ships a PDF — 2026-09-10

Daniyal's standing instruction, given after reading the decks:

> *"in the pptx you build, ever. always make sure there is nothing which can not be presented to
> audience, like ai markers etc. or guidelines to me, you can put that in the notes for the slides,
> also please always export a pdf preview as well."*

### 30.1 Nothing on a slide face but the lecture

**Production apparatus never appears on a slide. It goes in the SPEAKER NOTES.** That includes:
certainty labels (`[SOURCED]`, `[STANDARD]`, `[CONVENTIONAL-ESTIMATE]`, `(to verify)`) · tier tags
(`CORE`, `GOOD`, `CUT`, `Tier:`) · card ids (`RCT/E-RC20`, `E-HS4`) and cross-references between
cards · build markers (`CUT-IF-SHORT`) · instructions to the speaker (`[HANDS]`, `WORKSHEET`,
"speaker's discretion") · `n/a` and other not-applicable markers · `IMAGE BRIEF` text · the words
Claude, Gemini, AI-generated, LLM · and raw URLs, since a slide cites the **printed page**, not a
link.

**This is enforced, not remembered.** `series/deck2.py` carries a `FORBIDDEN` list and `audit()`
raises on any match found in a slide's text, so the build fails rather than shipping it. The one
exemption is the image placeholder, which is named `PLACEHOLDER::…` precisely so the audit can see
that it is scaffolding meant to be deleted — and `save()` reports how many are still unfilled.

**Why it is a build rule and not a review item.** This is exactly the class of defect that survives
every review and then appears on a projector in front of two hundred people. When the rule was
first written, a single build of `L02_ALL.pptx` was found to be putting `[SOURCED]`, `CORE ·`,
`(to verify)` and `n/a` on slide faces — and four separate rounds of fixing were needed before the
audit went quiet, because each round revealed another field nobody had thought about. A human
reviewer would not have caught the fourth one.

### 30.2 Every deck ships a PDF beside it

`deck2.save()` now writes `<deck>.pdf` alongside `<deck>.pptx`, every time, via PowerPoint.

**Why:** Daniyal reads and checks on a phone and on other machines, where a `.pptx` is not
viewable and PowerPoint is not to hand. A deck nobody can open is a deck nobody checks — and every
defect session 1's audience reported was one a single glance would have caught. `series/preview.py`
also exports per-slide PNGs and a contact sheet, which is what Claude itself should look at before
claiming a deck is right.

## 31 · The existing tribal worksheets stay in use — 2026-09-10

`L02_baarah_saal/tribal-relationships-worksheets.pdf` and `tribale_worksheet_small.pdf` were checked
link by link against the cached pages. They follow **Ibn Isḥāq's genealogy as ⁨البدایہ⁩ records it**
(⁨ج۲ ص۴۰۲⁩–⁨۴۱۱، ص۴۷۵⁩–۴۷۹), and every tribe on them sits where at least one classical authority puts
it. **Daniyal's decision: keep them as they are. No rebuild.**

**Why:** the bar for a worksheet is that it can be defended from the books, and it can. Where the
book records a second view, the sheet shows Ibn Isḥāq's.

**Worth knowing if a question comes up** (these are not changes to the sheet):
- ⁨أنمار⁩ (⁨خثعم⁩ · ⁨بجيلة⁩): Ibn Hishām also records a Yemeni line to ⁨كهلان بن سبأ⁩, and Ibn Kathīr says
  the Sabaʾ ḥadīth supports it (⁨ج۲ ص۴۷۶⁩).
- ⁨إياد⁩: Ibn Hishām makes him ⁨إياد بن نزار⁩ (⁨ج۲ ص۴۷۵⁩–۴۷۶). ⁨قضاعة⁩: the ⁨قحطانی⁩ view is at ⁨ج۲ ص۴۰۳⁩–۴۰۴.
- ⁨حمير⁩ and ⁨مذحج⁩ are two of ⁨سبأ⁩'s ten in the ḥadīth (⁨ج۲ ص۴۰۷⁩). The sheet's dashed lines from ⁨قحطان⁩
  are true, but the book puts both under ⁨سبأ⁩.
- ⁨قريش⁩ = ⁨بنو النضر⁩ is **Ibn Kathīr's own verdict** (⁨ج۲ ص۴۷۹⁩). The research note's line that he
  "records both without adjudicating" is wrong on that point.
- ⁨طيئ⁩, ⁨عنس⁩, ⁨سليم⁩ and the four ⁨غطفان⁩ branches follow the standard genealogy but are not on any page
  in our cache.

## 32 · Citations are verified by a script, not by a second model — 2026-09-13

Until now the way a research note's Arabic was checked was to send a second agent over it to re-grep
every quotation. That is the most expensive verification in the project, and the session-3 pass
showed it is also not reliable: **`tools/check_citations.py`, run over the eleven notes that had
already passed an adversarial model re-check, found 115 defects in 1,211 quotations** — 64 where the
quoted Arabic is on no cached page of the book it cites, 34 where it runs past the page it names,
16 wrong printed pages, and one citation resting on ⁨تاریخ الطبری⁩ alone, which `CLAUDE.md` §4 forbids.

**The check is not a judgement call.** The quoted Arabic either occurs on the cited page or it does
not; the printed page either matches the cached file's own header or it does not. So it is string
work, and it is now done by a script, for nothing:

```
python tools/check_citations.py                 # every note
python tools/check_citations.py docs/research/siffin.md
```

It reports `TEXT_ABSENT` · `TEXT_PARTIAL` (starts on the cited page, runs past it) · `PRINTED_WRONG`
· `PAGE_MISSING` · `BOOK_BANNED`. Matching ignores everything a typesetter can vary — harakat,
tatweel, editorial brackets, footnote markers, punctuation, whitespace — and folds the letter forms
Shamela varies (⁨أ إ آ ٱ⁩ / ⁨ى ي⁩ / ⁨ة ه⁩ / ⁨ؤ ئ⁩), so a real quotation passes and a half-remembered one
does not. A quotation broken by … is split there and each piece checked separately.

**The model is now only ever asked to fix what the script flags.** On the session-3 pass that was
20 quotations out of 1,489 — and the thirteen of those that could not be found on any of the 3,335
cached pages, nor on a freshly fetched window of ±6 pages around the citation, are Arabic the model
composed rather than copied. That is the failure this project cannot tolerate (`CLAUDE.md` §1.1),
it is invisible to a reviewer reading for sense, and it is caught in seconds by a substring test.

**Standing rule: no note is finished until `check_citations.py` reports zero problems for it, and
an unlocatable quotation is deleted rather than repaired.** Never write Arabic to fix Arabic.

**Not yet done:** the 115 defects in the 11-23 AH notes. They are inherited by
`L02_baarah_saal/CONTENT.md` and therefore by `L02_ALL.pptx`, so they must be cleared before session
2 is delivered — see `docs/STATUS.md`.

## 33 · Pools are by era; evenings are numbered deliveries that draw from them — 2026-09-13

Evening 2 as delivered (`L02_ALL_DY.pptx`) covered only the ⁨ردة⁩ up to ⁨بزاخة⁩ — a fraction of the
11–23 AH pool — and ran **37 minutes**, short of the 45-minute slot. The folder names `L02_baarah_saal`
and `L03_pehla_imtihan` promised one era per evening; delivery does not work that way, and the arc
table in `CLAUDE.md` §3 had silently stopped describing what the room will hear.

**Settled:**

1. **The pools stay where they are and are renamed only in meaning.** `L02_baarah_saal/CONTENT.md` is
   the **11–23 AH pool**; `L03_pehla_imtihan/CONTENT.md` is the **23–41 AH pool**. No card id, note,
   citation or tool moves — moving 2,000+ cards would buy tidiness at the risk of every cross-reference.
2. **An evening is a numbered delivery folder, `SNN_<slug>/`**, which holds a `RUNSHEET.md` (ordered
   card ids, minutes, tiers — Daniyal cuts here) and, after the cut, the six artifacts of spec v4 §1.
3. **`docs/catalogue/DELIVERED.md` is the ledger** of which card ids were spoken on which evening. The
   next evening opens from its last row. Unspoken cards stay available to any later evening.
4. **Depth, not breadth.** Evening 2 spent one card per event. From evening 3 each episode is told
   through several cards (backstory, the scene, the dialogue, the aftermath), mined from pages already
   cached — the sources carry far more narrative than the pools had drawn out.
5. New research for the ⁨ردة⁩ is appended to the 11–23 AH pool (its note slugs are added to
   `ORDER_L02` in `tools/build_content.py`), even where a card reaches before 11 AH (backstory) or
   after 23 AH (a forward pointer, e.g. ⁨ابن الأشعث⁩).

**Evening 3 = Yemen, start to end** — al-Aswad al-ʿAnsī in depth, the second Yemen ⁨ردة⁩, and
Ḥaḍramawt/Kinda to al-Ashʿath at al-Nujayr, with a short Kinda backstory. Told by front rather than
in strict date order (Kinda runs into 12 AH); the Line shows the flashback explicitly.

## 34 · Evening 3 is Parts I–II; built straight from the runsheet — 2026-09-16

**Daniyal's cut, after reading the three notes:** evening 3 is **al-Aswad al-ʿAnsī (Part I) and the
second Yemen ⁨ردة⁩ to Qays and ʿAmr sent home (Part II)** — ≈ 59 minutes of material, ≈ 42 CORE, for
34 story minutes. **The Kinda block is rolled forward**, untouched, under its own heading in
`S03_yemen/RUNSHEET.md`.

**How the evening is built, and why:**

1. **`RUNSHEET.md` is the running order and every artifact reads it.** `tools/build_full_deck.py` gained
   `runsheet()` (only tables under `## Part` headings count — moving a block under another heading is how
   a cut is made) and `card_slide()`. The deck, the cue sheet and the briefing all take their card list from
   it, so a strike in the runsheet reaches all three on the next build. `pack_data.py` refuses to build if
   the cue beats and the runsheet disagree.
2. **The Line for an evening this short is drawn in DATE BANDS, not to scale** (`S03_yemen/timeline.json`
   → `make_timeline.py`). The sources give "10 AH", "after Ḥajjat al-Wadāʿ", "some nights before, or one
   night" — never a day. Distance inside a band means order only. Two lanes (Medina/Najd above, Yemen
   below) so the flashback is visible rather than explained.
3. **Maps are Map Studio scenes written to `s03-*` files by `S03_yemen/make_maps.py`**, never by
   re-running `tools/make_scenes.py`, which would overwrite the seventeen session-2 scenes Daniyal may
   have nudged by hand. Kahf Khubbān and Shaʿūb are **not located** in our sources and are said so in
   words, not placed as dots.
4. **Two slide-face defects found at the contact sheet and fixed at the root.** A qualified label —
   `[SOURCED, disputed]` — reached a slide face, because both `build_full_deck.LABEL` and `deck2.FORBIDDEN`
   matched only the bare `[SOURCED]`; both now match qualified forms. And AW13's statement (words the
   widow said *to the guards* to save their lives, calling al-Aswad a prophet) is kept off the face; the
   slide carries one sentence of the card's own narrative instead.
5. **The ligature ﷿ (U+FDFF, ⁨عز وجل⁩) is left exactly as the source has it**, although Traditional Arabic
   draws it as an empty box: it has no Unicode decomposition, no permitted font on this machine carries it,
   and spelling it out would be writing Arabic into a quotation. The one slide affected (RC32) is flagged
   in its speaker notes for Daniyal to decide by hand.

## 35 · A finding that is not on a card does not exist on stage; the speaker notes carry the whole card — 2026-09-16

Daniyal asked where the Prophet's ﷺ arrangement for Yemen had gone — Bādhām, on his Islam, given the
deputyship of the whole of Yemen and not removed until he died (⁨البدایہ ج۷ ص۱۳⁩). It was in the al-Aswad
note's body (§1.2), quoted and page-cited, and on **no card** — only as an "Also on the page" line under
E-AW02. Two defects compounded:

1. **Notes → cards lost material.** An audit of the two Yemen notes found **82 quoted findings in the note
   bodies that were on no card in either pool** (47 al-Aswad, 35 second ridda). The research agents had
   carded the scenes they judged central and left the rest in the body.
2. **Cards → speaker notes lost more.** `build_full_deck.notes_for()` copied only the named fields
   (What happened, Map, ⁨عبرت⁩, Hands-up, source). Everything after Hands-up — "Also on the page",
   cross-references, ⚠ teaching warnings, second quotations — was silently dropped from every deck built
   from a pool, evening 2's included. **Fixed at the root:** cards now carry an `extra` field and the notes
   print it in full, with the statement's full rendering.

**Settled:** every quoted finding in a note body must sit on a card — as its statement, in its "Also on the
page", or as a card of its own. The two Yemen notes were re-carded to that rule: **4 new cards** (E-AW19 the
Bādhām arrangement, E-AW20 the al-Bukhārī line, E-YK17 Fayrūz's ؓ war and the families brought back, E-YK18
"every day routed or taken prisoner") and **29 existing cards enriched**; 7 quotations were left uncarded
because each is already an existing card's statement. A card whose statement must not be projected carries
`⚠ NOT FOR THE SLIDE FACE`, which `S03_yemen/build.py` now honours automatically. Two corrections came out
of the pass: the Khālid b. Saʿīd ؓ – ʿAmr duel is on ⁨الکامل ج۲ ص۲۲۹⁩, not Ibn Khaldūn only; and no page says
which of Banū ʿUqayl and ʿAkk turned back which convoy, so the map no longer pairs them.

## 36 · The Ḥaḍramawt/Kinda ridda goes back into evening 3 as Part III — 2026-09-16

The first cut (#34) moved the whole of the old Part III out, reading "the Kinda material" as everything in
it. Daniyal asked why the slides said nothing of Kinda, Ḥaḍramawt and the rebellion over the zakāt, and chose
to put it back. His reason was that Qays and ʿAmr being sent to Medina does not make sense without it. **The
page says otherwise about ʿAmr** — ⁨الکامل ج۲ ص۲۲۹⁩ closes his and Qays's story at **Najrān**, before the
Ḥaḍramawt war («⁨فسار المهاجر من نجران⁩» comes after it) — but the decision stands on a stronger reason: the
evening tells the room that the Prophet ﷺ appointed al-Muhājir ؓ over **Kinda** (E-YK04), and without Part
III that thread leads nowhere. ʿAmr, Qays and al-Ashʿath do meet again, in E-YK16, at al-Qādisiyya.

**Settled:** evening 3 = Parts I–III, to STOP C — 45 cards, ≈ 86 min (66 CORE) for 34 story minutes. Only
the **Kinda kingship backstory** (E-KD01–07) stays rolled forward. STOP A and STOP B closing sets are built
and hidden. Two Map Studio scenes (`s03-07-hadramawt-and-kinda`, `s03-08-al-ashath-to-medina`) and a STOP C
closing scene; al-Nujayr and Maḥjar al-Zurqān are named in words, not placed, because no page locates them.

**A parser defect found on the way, fixed at the root.** `build_full_deck.FIELD` read ⁨عبرت⁩, Map, When and
Hands-up only to the end of their first line; cards are hard-wrapped, so every wrapped field was cut
mid-sentence on slides and in notes ("…and then heard the news that"). The fields now run to the next
field or blank line. All 1,839 cards re-parse with no empty ⁨عبرت⁩ line.

## 37 · One slide per event: every card carries Beats — 2026-09-16

> **Point 3 superseded by #39 (2026-09-19).** The deck is no longer one slide per beat; beats moved to the
> speaker notes after evening 3 was delivered from the 356-slide deck. Points 1, 2, 4 and 5 stand.

Daniyal, looking at evening 3: *"these are still less slides than the events described in content … having a
separate slide for everything that I need to tell broadly helps in making sure we don't forget stuff."* His
example was Ziyād b. Labīd's ؓ first engagement after the Shadhra quarrel — a night attack that lived inside
one card (E-YK08) with six other events, and so had no slide of its own. A slide per card hid most of the story.

**Settled — and it outranks the 45-slide instinct of the earlier decks:**

1. **Every card carries a `**Beats:**` list** in its research note, immediately after **What happened**: one
   line per event, turn, speech or decision in the card's own text, `n. Headline — one face line`, headline ≤ 8
   words, face line ≤ 20, English only, no apparatus, disputed reports marked as disputed and never resolved.
   `**Quote after beat:** N` says where the card's Arabic quotation slide falls in the telling.
2. **Beats live in the notes, not in the evening folder**, so the trove keeps them: any later evening that draws
   the card gets the same slides. `tools/build_full_deck.py` parses them (`beats`, `quote_after`, `beat_slide()`).
3. **The deck is one slide per beat plus the card's quotation slide.** The speaker notes of every beat slide list
   all the card's beats with the current one marked, so the whole card is one glance away.
4. **Overlap on one evening is handled in the runsheet, never by deleting beats**: a Note cell `SKIP BEATS 3,4`
   drops those beats from that evening only.
5. Deck length is no longer a target. The slot is still 45 minutes; the cut is still made at the lectern and
   whatever is not reached rolls forward (#20). The beats exist so that what IS told is told whole.

The first evening built this way (S03) was then reviewed end to end by a four-lens multi-agent pass
(completeness · fidelity/register · slide-face visual QA · continuity), each finding checked by a separate
skeptic before any fix was applied.

**Outcome of the first beats pass and review (same night).** 45 cards now carry 282 beats; S03 is 361 slides
(8 hidden). The four-lens review raised 75 findings; the verifiers confirmed 73; 61 were applied (runsheet
`SKIP BEATS` on 14 rows for events two cards tell twice, plain face dates on 23 cards, a new opening map, beat
wording that names the book when reports differ, timeline and map corrections). Three corrections of our own
making came out of it and are recorded here so they are not re-made:
- **ʿAmr b. Maʿdī Karib is ؓ after his return.** The second-ridda note says so from Ibn Kathīr's «﵁» (⁨البدایہ ج۷
  ⁨ص۲۴۴⁩⁩). The instruction given to the beats agents ("no honorific for ʿAmr") was wrong and had stripped it from
  E-YK16 at al-Qādisiyya; restored. Qays b. Makshūḥ stays without one — no page states his Companionship.
- **Arabic on slides is now marked `lang="ar-SA"`** (`series/deck2.py`). Without it PowerPoint placed colons,
  dashes and "!" on the wrong side of Arabic words (e.g. «⁨له⁩ :⁨وهرز⁩»). Every deck picks this up on rebuild.
- **The opening Line gave away the first [HANDS] answer** ("Ṣanʿāʾ in 25 nights"); its short label is now
  "Najrān, then Ṣanʿāʾ".

## 38 · Evening 3's deck is final and hand-finished; the repo carries a compressed copy — 2026-09-17

Daniyal finished `S03_yemen/S03.pptx` by hand (356 slides, 13 hidden; ten Map Studio maps placed at
3840×2160) and declared it final. Two consequences:

1. **A rebuild must never overwrite it.** `S03_yemen/S03.FINAL` marks it; while that file exists `build.py`
   writes `S03_rebuild.pptx` instead. Any later change to the evening is made by hand in the deck, or rebuilt
   to `S03_rebuild.pptx` and merged by hand.
2. **The finished deck is 131 MB and GitHub refuses files over 100 MB.** Daniyal chose a compressed copy over
   Git LFS: `S03_repo.pptx` is the same deck with the ten maps downscaled to 1920×1080 PNG (26.8 MB, verified to
   open in PowerPoint and to export the same 343 pages), and `S03.pdf` is exported from the final deck. The 131 MB
   original stays on this machine and is no longer tracked. Same principle as evening 2's video-embedded deck.

Also added the same day: `S03_recap.pptx` (`build_recap.py`) — "The story so far", 16 slides pasted in before
Part III at slide 238.

## 39 · Back to one slide per card — the beat-per-slide deck is retired — 2026-09-19

**Supersedes #37 (point 3 only).** Evening 3 was delivered from the 356-slide beats deck and the shape
failed in the room. Daniyal, the same evening: *"the too many slides with sometimes repeated text bored
the audience. And I had to skip many of them at times because I had already told the story on the first
slide of that event."*

Two distinct defects, and they compound:

1. **Repetition.** A card's beats are successive moments of one scene, so consecutive beat slides restate
   the same situation in slightly different words. The room reads the slide, hears the same thing said, and
   disengages.
2. **Forced skipping at the lectern.** A speaker who tells an event well tells it whole, from its first
   slide. The remaining beat slides for that event are then already spent, and he is visibly clicking past
   his own deck — which costs more authority than a missing slide ever did.

**Settled:**

1. **The deck is one slide per card** (plus the card's quotation slide and its maps/images), as evenings 1
   and 2 were built. `tools/build_full_deck.card_slide` is the builder; `beat_slide` is no longer called by
   an evening's `build.py`.
2. **Beats stay in the research notes, and they move to the speaker notes.** #37's real purpose — *"having a
   separate slide for everything I need to tell broadly helps in making sure we don't forget stuff"* — is
   served by putting the card's full beat list in the **speaker notes of that card's one slide**, and in
   `BRIEFING.pdf`. The completeness check survives; only its projection is withdrawn. Beats are also what
   `CUE.pdf` is built from.
3. **The screen carries the picture; the speaker carries the sequence.** A card's slide is a map, an image,
   a large statement or a sourced quotation — never the narration of the beat the speaker is on.
4. **Density target, from evenings 1–3 as actually delivered:** about **one slide per spoken minute**, i.e.
   **40–55 slides for a 45-minute evening**, 25–30 cards. Evening 2 ran 26 cards / 39 slides in 37 minutes.
   This is a sanity check, not a quota — #20 (over-build and cut at the lectern) still governs the *pool*,
   which is over-built as ever; it is the *deck* that is now built at spoken density.
5. **Evening 3's deck is untouched.** It was delivered; it stays as delivered (#38). This decision governs
   evening 4 onward.

**What #37 keeps:** points 1, 2, 4 and 5 — every card still carries a `**Beats:**` list in its note, beats
live in the notes so any later evening inherits them, the runsheet's `SKIP BEATS` still drops an event a
second card tells, and deck length is still not bought by speeding up.

## 40 · Speaker notes are speaking points, not a card dump — 2026-09-19

Daniyal, choosing evening 4: *"The speaker notes should be structured to tell me speaking points. Maybe we
can remove the unnecessary info from speaker notes like card id etc."*

Until today `notes_for()` opened every slide's notes with the card id, the tier and the `When` line, then
the prose, and buried the beats. The first thing the eye met in the notes pane mid-sentence was production
apparatus that cannot be acted on at a lectern.

**The notes pane is now ordered the way the lectern needs it:**

```
SAY —            the card's beats, numbered, one line each; the quotation's place marked
QUOTE —          the Arabic, the English rendering, the citation
عبرت —           the one line
HANDS UP —       only if the card carries one
MAP —            what the map does on this slide
⚠                a delivery warning, if the card has one — above the prose, never below it
BACKGROUND —     the card's prose and everything after the Hands-up line. Read at home, not aloud
```

**Card id, tier and the source section are gone from the notes.** Traceability lives in the evening's
`RUNSHEET.md` and `SLIDES.md`, which is where it is read from anyway — never at the lectern.

Two parser defects fixed in the same pass, both of which had been silently losing note content:

- **A field no longer ends at any bold run, only at the next known field label.** `**Map:**` and `**⁨عبرت⁩:**`
  routinely continue onto a line beginning with a bold place name («**⁨اليمامة⁩**. The enemy camp is at …»)
  and were being cut there. Every MAP note in every deck built before today is truncated at that point.
- **The English rendering is no longer double-quoted**, and a trailing `---` no longer produces an empty
  BACKGROUND block.

## 41 · The Umm Tamīm ؓ connection is recorded, and is not spoken — 2026-09-19

Found in the evening-4 content review. Ibn Kathīr names the widow of Mālik b. Nuwayra ؓ whom Khālid ؓ
married as **⁨أم تميم ابنة المنهال⁩** («⁨واصطفى خالد امرأةَ مالكِ بن نُوَيْرة وهي أم تميم ابنة المنهال⁩»,
⁨البدایہ ج۷ ص۳۰⁩ · https://shamela.ws/book/30097/3176), and names the woman in Khālid's ؓ own tent at
⁨عقرباء⁩ — the one Mujjāʿa protects, and who then protects him — as **⁨أم تميم امرأة خالد⁩**
(⁨ج۷ ص۳۳⁩ · https://shamela.ws/book/30097/3179). Same book, three pages apart, same name.

So on the books' own naming, the woman at the centre of the al-Buṭāḥ dispute is the woman in the tent
at al-Yamāma, and ʿUmar's ؓ words in `RCT/E-RC49` have already put her in the room.

**Settled: the connection is not made from the platform.** It is not needed for any event, it adds
nothing the room must have, and drawing the line invites exactly the adjudication `CLAUDE.md` §1.6
forbids — from a room that will already be holding its breath through Part II. The cards stay as they
are: `E-RC49` quotes ʿUmar ؓ as the books have him; `E-RC16` and `E-RC17` name Umm Tamīm ؓ as Khālid's ؓ
wife, which is what their own pages say.

**But it is written down here, and a prepared answer goes in `QA_BANK.md`,** because this is the
connection an attentive listener makes unaided, and a question slip about it is likely. The answer is
the same as the rest of the episode: the books record it, they do not comment on it, and we do not
adjudicate between Companions.

**Daniyal can overturn this.** If he wants it said, it is said the way everything else in Part II is
said — as what the books record, with no inference drawn.

## 42 · Evening 4 runs in chronological order — 2026-09-19

Daniyal, after the content review: *"And structure the evening in chronological order. We can do the
kinda ridda at end of session and start with butah if that makes more sense."*

The first cut ran Kinda → al-Buṭāḥ → al-Yamāma, which is **late → early → middle**: al-Nujayr is the
last siege of the war and al-Buṭāḥ is Khālid's ؓ stop immediately after Buzākha. The review found that
the flashback seam was unmarked and that three cards referred forward to material told later.

**Settled: the evening runs in the order the sources establish** — campaign note §12.2, `[SOURCED as
sequence]`: Buzākha → **al-Buṭāḥ** → recalled to Medina → **al-Yamāma** → … → **Ḥaḍramawt/Kinda, last**.
The claimants (Musaylima, Sajāḥ) are introduced in a short Part I *before* the campaign reaches them,
so that nothing later refers forward.

**Three defects the reorder fixed by itself:** `E-RC45`'s forward reference to Sajāḥ and Musaylima;
the unmarked jump back in time; and `E-RC52`'s naming of al-Yamāma as the place Zayd ؓ fell, which is
now flagged on the card as a spoiler to withhold.

**The cost, stated plainly.** Ḥaḍramawt/Kinda now sits at the end of ~80 minutes and **will not be
reached on evening 4** — a third deferral. That is the price of chronological order, and it is
recorded at the top of `S04_kinda_butah_yamama/RUNSHEET.md` so the choice is visible every time the
cut is made. If Kinda must be spoken next, Part V moves to the front and this decision is superseded.

## 43 · Every figure who carries a card gets his one-breath notice — 2026-09-19

The evening-4 review found five men carrying cards with no ⁨تراجم⁩ notice anywhere in the delivered
series: **al-Ashʿath b. Qays** (seven cards, introduced only in an optional block), **Ziyād b. Labīd ؓ**
(five cards, one clause on evening 3), **Thābit b. Qays ؓ** (the only man at al-Yamāma without one),
**Abū Qatāda ؓ** (whose testimony is the crux of al-Buṭāḥ), and **Mālik b. Nuwayra ؓ**.

This is `DECISIONS.md` #28 applied as a **check**, not a principle: before an evening is built, every
name that carries a card is tested against `docs/catalogue/DELIVERED.md`, and a name the room has not
met gets its notice on the card where it becomes load-bearing.

Added for evening 4: `TSY/E-YK19` (al-Ashʿath, a card of its own, **not cut even when the Kinda
flashback is**); a first beat on `TSY/E-YK07` for Ziyād ؓ; the ⁨سیر⁩ notices for Thābit ؓ
(⁨خطيب الأنصار⁩ — ج۱ ص۳۰۹) and Abū Qatāda ؓ (⁨فارس رسول الله ﷺ⁩ — ج۲ ص۴۴۹), both fetched for this pass.

### 43.1 · The check is mechanical, and it covers four kinds of thing — added 2026-09-19

`tools/check_introductions.py` makes #43 a gate rather than a memory. It walks an evening's
`RUNSHEET.md` in running order and reports every proper name appearing **for the first time in the
series** — in no card listed in `DELIVERED.md`, and in no earlier card of the same evening. The
runsheet answers every row in a `## Introductions checked` table; the tool exits non-zero while a row
is unanswered, and **"no notice needed" is a valid answer**. The rule is that somebody looked.

**The question is asked of four kinds of thing, not only people** — because the evening-4 review
caught one of each: a **person** with no ⁨تراجم⁩ notice (al-Ashʿath b. Qays), an **event** every later
card assumed but no card told (the army leaving Medina for al-Yamāma), a **term** carrying a line's
whole force with no gloss and no page (⁨البسوس⁩), and **forward references** to evenings not yet given
(⁨القادسية⁩, ⁨اليرموك⁩, ⁨عثمان ؓ⁩). The rule and the table are in `CLAUDE.md` §2.

Two limits, both stated in the tool's own docstring: a name introduced only inside an **optional
block is not introduced** — the notice belongs on a card that is never cut; and **evening 1's card
ids were never recorded**, so nothing from the orientation evening is in the known set.

## 44 · Evening 4 is cut to Parts I–IV, ending at STOP C — 2026-09-22

Daniyal, asked for the cut the runsheet had been waiting on: **Parts I–IV, ending at STOP C** — the two
claimants, al-Buṭāḥ and the reckoning at Medina, the road to al-Yamāma, and the day at ʿAqrabāʾ up to
«⁨امتازوا⁩». 31 cards. The runsheet had recommended stopping at STOP B (Parts I–III, 20 cards) with Part IV
as overflow; he took the longer evening.

**Why that is the right size, not an over-reach.** The runsheet's budget is ≈ 1.7 min a card, which puts
Parts I–IV at ≈ 57.5 minutes against 34 story minutes. But that budget is not the room's pace: **evening 3
spoke 32 cards in the slot** (`DELIVERED.md`). Thirty-one cards is an evening at the pace the room has
actually shown.

**What the cut settles.**
- **The deck ends visibly at STOP C** (slides 47–50: the Line, the map, «Tonight», next week), and those
  two closing slides open evening 5 (#23). **STOP A and STOP B are built and hidden** at the end of the deck;
  `CUE.pdf` prints their slide numbers, so an early close is a typed number, not a hunt. **STOP D is gone**
  with Part V.
- **Parts V and VI leave the deck.** They stay in `S04_kinda_butah_yamama/RUNSHEET.md`, whole, under
  *Rolled forward to evening 5* as `###` headings, so `build.py` and `check_introductions.py` do not read them
  and evening 5 can lift the tables unchanged.
- **Ḥaḍramawt/Kinda is deferred a third time** — evening 3's Part III, evening 4's Part V, now evening 5.
  #42 stands: chronological order, Kinda last. The bookend-IN line no longer promises "at the end of the
  evening we come back south"; it says Ḥaḍramawt stays grey tonight.
- **The worksheet beat moves to STOP B** — on the room's pace that is where 0:26 falls — and its three
  people are Mālik b. Nuwayra ؓ, Mujjāʿa b. Murāra and Thābit b. Qays ؓ (al-Ashʿath left with Kinda).
- **The closing «Tonight» slide draws across the evening** — `ATA/E-TB15`, `RCT/E-RC50`, `RC58`, `RC19` —
  and no closing set uses `RC54`'s line, whose "It worked" gives away a day the room has not seen decided.

**If the evening runs short,** drop GOOD cards in the order the runsheet gives (#2, #5, #4, #18, #21, #30);
if that is not enough, close at STOP B and Part IV opens evening 5. Part II is still all or nothing.

## 45 · Bridge slides at the seams — 2026-09-22

Daniyal, reviewing `S04.pptx` "from story telling perspective": *"there is fast shift between slides,
without filling in the missing details in between which would be narrative or story discontinuity, we
might need to add a few slides to fill this in. for example when khalid started towards butah, a brief
summary would have to be given that he was at buzakha and was told to go to butah."*

One slide per card (#39) made every card clean and left the joins between them unspoken. The room hears
a sequence of scenes; the speaker knows how one leads to the next, and the slides did not show it.

**Settled: every deck is read as a story before it is finished**, and wherever consecutive slides jump
in time, place or thread, a **bridge slide** goes in. A bridge is not a card. It is three steps — where
we were, what happened, where we are going — drawn only from the cards (and, where a card does not carry
it, from a page already in the cache), with the sentence to say in its notes. Evening 4 has five, built
by `S04_kinda_butah_yamama/build.py` (`BRIDGE_BEFORE`) and listed in its runsheet:

| Before | Bridge | The seam |
|---|---|---|
| #1 | *Tonight: back to the north* | evening 3 ended in the Yemen; tonight opens on a letter from al-Yamāma, a year earlier |
| #7 | *After Buzākha* | the orders tied at Dhū al-Qaṣṣa — «⁨وأمره بطُلَيْحة … فإذا فرغَ سار إلى مالك بن نُوَيْرَةَ بالبطاح إن أقام له⁩» (⁨البدایہ ج۷ ص۲۲⁩) — Daniyal's own example |
| #16 | *Back to the mosque, 11 AH* | #15 closes years later, in ʿUmar's ؓ caliphate |
| #17 | *Meanwhile, at al-Yamāma* | the two commanders who were on that road before Khālid ؓ |
| #21 | *Where we are* | the re-entry after the worksheet, for anyone who has just come in |

**The usual seams**, to look for on every evening: a flashback or a flash-forward; a second front told
after the first; the first card of each Part; and the re-entry after the worksheet pause. The cue sheet
marks each bridge with «»» and the briefing lists their spoken lines.

## 46 · Evening 4 review: what it changed — 2026-09-22

A six-lens review of the finished evening (five lenses completed; `max-four-agents`: fan-out is now
capped at four) found 73 defects; each was checked against the files before it was fixed. The ones that
change how evenings are built, not just this one:

- **The slide face is an authored excerpt, not a blind cut.** The builder cut every English rendering at
  24 words, so the room read *"…he had meant nothing but…"* under a complete Arabic line, and Part II's
  faces were one-sided — slide 20 showed Abū Qatāda's ؓ testimony and cut the other half of the patrol.
  Where a quotation does not fit, `build.py` now carries a `FACE_QUOTE`: the Arabic and the English cut at
  the same clause, every cut marked «…», and **the build refuses any segment that is not the card's own
  words** (`check_face_quotes`). The notes keep the whole quotation. Evening 4 has 20. The shared
  `statement_slide` now measures type properly and never lets English run onto the citation.
- **#11 is four accounts side by side, not one.** Its face had projected Ibn al-Athīr's gloss alone — the
  account that clears Khālid ؓ — at the centre of a part that is never a verdict. It is now a 2 × 2 grid
  of the four, from the campaign note's §5.7(d) table.
- **No spoilers in the speaker's own lines.** Beats had Thābit ؓ die at #2, Musaylima die at #3, and
  RC54's ⁨عبرت⁩ say *"It worked"* at #19. Pool cards `TB16`, `TB12`, `RC53`, `RC54` and `RC19` are reworded;
  the early-close Lines no longer draw tonight's untold events; the worksheet (in the room's hands at STOP
  B) no longer prints two Part IV events.
- **Two words that take sides are gone.** *"A later caliph"* for Muʿāwiya ؓ called him caliph, which
  §17.4 of the QA bank does not; the face now ends before his name and the beat says "for many years".
  The watchword «⁨يا محمداه⁩» at #30 is off the face and the cue — a live proof-text in this country —
  and has a prepared answer (`QA_BANK.md` §6.11, **for Tanzeem-e-Islami to review**). *"Dowry"* at #5 is
  "the price he paid" (§6.10).
- **ʿIkrima ؓ and Shuraḥbīl b. Ḥasana ؓ get their one-breath notices** on `RCT/E-RC15` (never cut),
  page-cited: ⁨سیر ج۱ ص۳۲۳⁩ and ⁨البدایہ ج۷ ص۲۰۸⁩.
- **The introductions gate could not see** names beginning Ḥ, Ḍ, Ṣ, Ṭ, Ẓ, nor any name after Abū, Banū or
  Umm (it took the known word as a parent), and it counted evening 3's *unspoken* Kinda cards as
  delivered. All three fixed in `tools/check_introductions.py`; the fourteen names it then found are
  answered in the runsheet.
- **Maps are rendered by the pipeline** (`tools/render_scene.py`, headless Map Studio) and placed as
  JPEGs; the title box is off (its type was 5–9pt on the slide); a missing render makes the build exit
  non-zero. `S04.pdf` now includes the hidden slides, so the cue sheet's "type 56" is page 56.

**Left open, for Daniyal:** Umm Tamīm carries ؓ on `RC17`, the cue sheet and #41, and none on `RC16`; no
page we hold settles her Companionship either way.

## 47 · The planned close stays in place, and the story goes on behind it — 2026-09-22

Daniyal, after reading the built deck: *"i think i will run out of material with the current s04. I think
we should build more slides, continue the story, we should still keep the slides that give summary end of
current version, so that if i can i stop there, but there should slides afterwards to that if i need to i
can continue."*

#44 cut the evening to Parts I–IV and 31 cards, and #20 has always said to build ~70 minutes for the
45-minute slot. Thirty-one cards at the room's real pace is not 70 minutes, and an evening that runs out
of material is worse than one that runs over: the speaker fills, and filling is where a stage-frightened
speaker gets into trouble.

**Settled: the deck holds both endings, in this order.**

| Slides | |
|---|---|
| … 51 | Parts I–IV, ending at «⁨امتازوا⁩» |
| **52–55** | **the STOP C close, in its place** — the Line, the map, the four ⁨عبرت⁩ lines, next week |
| 56–64 | **Part V**, the overflow: the garden · the death of Musaylima · the terms at the forts · Zayd ؓ and his brother · the Qurʾān gathered |
| **65–68** | **the STOP D close** — the same four slides for the fuller ending |
| 69–76 | STOP A and STOP B, hidden, for an early close |

**Stopping needs no jump; going on is one typed number.** The close sits where the evening is planned to
end, so if the clock has run out he simply closes. If it has not, `CUE.pdf` prints the number of Part V's
first slide (56 today) beside the STOP C row, and a bridge slide re-anchors the room on the other side.

**What it costs, and why it is still right.** Whatever Part V reaches is spoken, so evening 5 starts from
wherever this stops (`DELIVERED.md`, #33) — and evening 5 still has Ḥaḍramawt/Kinda, which is last (#42).
Part V ends on the collection of the Qurʾān, which is the strongest ending the ⁨ردة⁩ arc has; if it is
spoken tonight it is not available to evening 5, and that is an acceptable trade for an evening that
cannot run dry.

**Also settled here:** the five Part V cards (`RC20`, `RC21`, `RC22`, `RC23`, `RC37`) had no `**Beats:**`
list — they predate #37 — so the lectern would have fallen back to prose. Beats were written for all five
from each card's own text, in the pool and in the research note, and `check_citations` is still silent.


---

## 48. Part VI — the dead of al-Yamāma sit behind Part V, and the muṣḥaf is the last word

**2026-09-22, Daniyal: "is this a good point to have slides covering the various families that we
researched? Zayd b. al-Khaṭṭāb? Umm Sulaym — Anas — al-Barāʾ b. Mālik?"** Yes — here, and only here.

**Why here.** The books give one reason for the ⁨جمع القرآن⁩: «⁨استَحَرّ القتلُ في القُرّاء⁩» — the killing
ran hot among the reciters. Part V already ended on the order to Zayd b. Thābit ؓ, so the room was being
given the *reason* as a sentence and the *order* as an event, with nobody in between. Part VI puts one
reciter in between. It is eight cards, all page-cited, none needing a map:

| # | Card | What it adds |
|---|---|---|
| 36 | `AHA/E-AS09` | Sālim ؓ is one of four the Prophet ﷺ named to take the Qurʾān from |
| 37 | `AHA/E-AS15` | Both hands gone, and the āya Abū Bakr ؓ had read to Medina the year before |
| 38 | `AHA/E-AS16` | «⁨فأضجعوني بينهما⁩» — lay me down between them |
| 39 | `AHA/E-AS17` | ⁨الذہبی⁩'s «⁨وقيل⁩»: how the two were found. The hedge is carried across |
| 40–41 | `THO/E-HS14`, `HS15` | The man who went over the wall lived — and ʿUmar ؓ would not give him an army |
| 42 | `ZIA/E-ZY17` | **The number nobody can give.** The card exists to stop a wrong figure being said |
| 43 | `RCT/E-RC37` | The order at Medina. The last word of the evening |

**What was NOT taken, and why.** `ZIA/E-ZY2` (Zayd ؓ at the banner and his vow of silence) was in the
first cut of this part and was removed: it is `RCT/E-RC60`'s own event, already told at #28, and the room
would have heard the same vow twice in one evening. `ZY5`/`ZY6` (ʿUmar's ؓ «⁨سبقني إلى الحُسَنيين⁩» and the
east wind) stay out for the same reason — `RC23` carries both already. `AHA/E-AS05` and `AS10` are
⚠ SPEAKER'S DISCRETION and are in no deck. **The other ~48 household cards (`THO`, `AHA`, `ZIA`) remain a
pool for the evening that carries the dead** — they are not spent here.

**The escape hatch.** Part VI can be abandoned at any point without hurrying it: `CUE.pdf` prints the
slide number of `RC37` beside the beat that opens the part. One typed number takes the muṣḥaf card and
the STOP D close. This is the same mechanism as the early closes (#44, #47), used forwards.

**Beats and honorifics.** The eight cards predate #37 and had no `**Beats:**` list; beats were written
for each from its own text, in the pool **and** in the three research notes. Nothing was composed: every
beat line is the card's content, and no ⁨لقب⁩ was invented (§1.2).

**Introductions (#43).** The gate answered four new rows: ʿUtba b. Rabīʿa (part of Abū Ḥudhayfa's ؓ name —
and **Badr is not told from the platform**), al-Arqam, al-ʿAbshamī (not spoken), and Tustar.

---

## 49. The whole al-Yamāma household pool goes in tonight; what is not reached opens evening 5

**2026-09-23, Daniyal: "why not we add all household cards here during Yamāma before moving ahead? If
it spills we will keep covering in next session?"** That is the house rule (#20, #33), so yes — with one
line drawn, and the line is **the field**, not the household.

**What went in (12 cards, Parts VI–VIII, #36–#55).** Everything the approved books put *on that field*
or in its immediate aftermath: the banner falling from Zayd ؓ to Sālim ؓ (`AS13`), the four reciters
(`AS09`), the pit (`AS14`), the two hands and the āya (`AS15`), «⁨فأضجعوني بينهما⁩» (`AS16`), how they
were found (`AS17`), ʿUmar ؓ eleven years later (`AS18`), the estate sent back (`AS19`), the ⁨مؤاخاة⁩
pairs who died together (`ZY8`, `ZY9`), the man who killed Zayd ؓ and became a Muslim (`ZY4`), Abū
ʿAqīl ؓ (`ZY12`), the son of the head of the hypocrites (`ZY13`), four men of one Meccan household
(`ZY14`), Ḥabīb b. Zayd ؓ and his mother (`ZY15`), and al-Ṭufayl ؓ and his son (`ZY16`).

**What stayed out, and why.** About 36 household cards are **not** at al-Yamāma: Uḥud, Ḥunayn, Biʾr
Maʿūna, the dower, Bayruḥāʾ, Qubāʾ, Abyssinia, Tustar. Importing them would move the evening off its own
point on the Line and force forward and backward references the room cannot carry (#43). They stay a
pool for **the evening that carries the households**, which is where they belong.

**Nine cards were rejected as duplicates** of what this evening already tells — this is the check that
matters when a pool is raided late: `AS11` = `RC59` · `AS12` = `RC61` · `ZY2` = `RC60` (the same vow,
word for word) · `HS16` = `RC20` · `ZY3` = `RC57` · `ZY11` ≈ `RC18` · `ZY5`/`ZY6` are inside `RC23` ·
`ZY7` = `RC52` · `ZY1` is `RC23` beat 2.

**Shape.** Part VI is the banner; Part VII is the men beside them; Part VIII is what was left —
al-Barāʾ ؓ, the number nobody can give, and the order at Medina. **#55 is the last word in every version
of the evening**, and it is always one typed number away: `CUE.pdf` prints `RC37`'s slide number beside
the beat that opens Part VI. Nothing in here is compressed to fit; whatever is not reached opens evening
5, which still owes the room Ḥaḍramawt and Kinda (#42).

**What it cost the cue sheet.** Thirty beats do not fit on one page, and a two-page cue card is not a cue
card (§1.7). The overflow no longer sits in the Run column: `series/pack.py` renders it as a **full-width
band under the columns** — *"If the clock is kind — behind the close"* — one digest line per part with
that part's ⚠ digest. The planned evening keeps its own beats and its type at **11pt**; the same words
in a narrow column had forced 10pt.

---

## 50. The households go in as well — Parts IX–XI, behind the close

**2026-09-23, Daniyal: "wouldn't it be better to give complete backstory for the families and
individuals, instead of dropping some cards? My suggestion might be wrong, so think about it."**

**The advice given, recorded because it was not taken.** The evening already gives backstory thirteen
times, one breath each, at the moment a man becomes load-bearing (#28) — `RC59` has Qubāʾ and the night
the Prophet ﷺ went out to listen; `RC61` has the father who fell at Badr on the other side. What the
remaining cards add is not *who these men were* but **other events**: Uḥud (3), Biʾr Maʿūna (4), Ḥunayn
(8), Abyssinia, Tustar (17–20). Telling those inside an 11–12 AH evening teaches the room that the Line
is decoration — and the Line is the one thing this course has that a good sīra evening does not. The
recommendation was a take-home sheet plus a households evening of their own.

**Daniyal chose to import them, and that is the call that stands.** The room is his. What the build does
is limit the cost:

- **They sit BEHIND the STOP D close**, as Parts IX–XI (#56–#81). The evening's own story still ends on
  the muṣḥaf at #55, and the close is emitted in place there (`CLOSE_D_AFTER`) exactly as STOP C is
  (#47). So the Line never moves backwards *inside* the evening's arc.
- **Three honest uses, in order of likelihood:** evening 5's opening; the fifteen minutes the speaker
  stays after the close anyway (`CLAUDE.md` §1.5); or a room that is still hungry at STOP D.
- **There is no STOP E.** Nothing on the Line or the map moves during backstory, so to finish from
  anywhere in Parts IX–XI the speaker types the STOP D close's number again. `CUE.pdf` prints it.
- **Tell a house, not a card.** `HS1`–`HS3` alone is a whole house in three cards. Never open a house
  and leave it at one.

**26 cards, not 36.** Nine were already rejected as duplicates (#49), and `ZY2` with them.

**What the faces needed.** `AS05` and `AS10` carry "⚠ SPEAKER'S DISCRETION" **in their research
titles**, which would have put production apparatus on a projector (#30) — both are overridden in
`FACE_TITLE`. `HS5`, `HS12` and `HS13` quote across a **page break**, so the card parser returns no
English at all for them; each face is authored in `FACE_QUOTE` from the card's two blockquotes, and the
two that span pages now carry the span on the face through a new `FACE_CITE` (⁨ج۲ ص۳۰۶–۳۰۷⁩,
⁨ج۲ ص۳۱۶–۳۱۷⁩) instead of citing only the first page.

**A real bug this exposed.** `planned_ids()` excluded the overflow with `not part.startswith("Part V")`
— which also swallowed **Parts IX, X and XI**, putting the houses back on the 45-minute clock and making
it run backwards. It is now an explicit whitelist of Parts I–IV.

**The cue sheet holds.** One page at **11pt**: the planned evening is still cued beat by beat, and the
whole overflow — 50 cards — is five digest lines in the band, the houses being one of them.

---

## 51. The missing-detail audit — four notes read against the 82 cards

**2026-09-23, Daniyal: "is there any missing detail? I think Umm ʿUmāra might have missing detail" —
and then "do this check with other stuff in S04."** He was right about her, and the sweep that followed
found more. Four notes were read against the evening's card list under #35 ("a finding in a note body
that is on no card does not exist on stage").

**Fixed in this pass:**

| What | Where it was wrong |
|---|---|
| **Her other son** | ⁨الذہبی⁩, **in Umm ʿUmāra's ؓ own notice**, says ʿAbd Allāh b. Zayd ؓ — Ḥabīb's ؓ brother — killed Musaylima with his sword (⁨سیر ج۲ ص۲۸۲⁩). The evening told her son's death and Musaylima's death and never joined them. Now `ZIA/E-ZY18`, **framed as one of four names** (`QA_BANK.md` §5.3), with `RC21`'s row cross-referring |
| **Her own record** | «⁨وَجَاهَدَتْ، وَفَعَلَتِ الأَفَاعِيْلَ⁩», twelve wounds at ⁨أحد⁩ (⁨ج۲ ص۲۸۱⁩) — she was on the card only as a list of battles. Now `ZY15` beat 5, with the ⚠ that the two books differ on the ⁨اليمامة⁩ count |
| **`RC57` named a sender the sources do not** | The card said **"Abū Bakr ؓ had sent him"** of ⁨الرجال بن عنفوة⁩. ⁨الکامل ج۲ ص۲۱۵⁩ is the only approved page with the clause and **its pronoun is unattached**. The Zayd note §2.6 had already caught and corrected this in its own draft; the ridda note §6.7 had not, and the card followed the ridda note. **Both are now corrected.** §1.1: wrong is worse than absent |
| **`RC18` stated a kinship the page qualifies** | Thābit ؓ as brother by his mother to ʿAbdallāh b. Rawāḥa ؓ sits on the **second** of two reports, «⁨وقيل⁩» (⁨سیر ج۱ ص۳۰۹⁩). Now carried with the «⁨وقيل⁩» attached |
| **The final card named a man with no notice** | `RC37` said "Zayd b. Thābit ؓ is to gather the Qurʾān" and never said who he was — on the last slide of the evening. Now beat 3: of the Khazraj, of Banū al-Najjār, **the Prophet's ﷺ own scribe of the revelation** (⁨سیر ج۲ ص۴۲۷⁩) |
| **Abū Ṭalḥa ؓ carried six cards with no notice** | Now `HS1` beat 1: a man of Badr, one of the twelve ⁨نقباء⁩ of ⁨العقبة⁩ (⁨سیر ج۲ ص۲۷⁩). ⚠ **his own name is Zayd b. Sahl — the evening has three Zayds**, and the introductions table now says so |

**What the audit also surfaced and did NOT go in** (reported to Daniyal, his call): ⁨محكم بن الطفيل⁩
calling Banū Ḥanīfa into the garden and being killed by **⁨عبد الرحمن بن أبي بكر ؓ⁩** (three books);
Abū Bakr ؓ and Zayd's ؓ own dialogue over the ⁨جمع⁩ (⁨سیر ج۲ ص۴۳۱⁩); the ⁨اليمامة⁩ terms in words; Ibn
Kathīr's two Muslim totals for the same day; Banū Ḥanīfa's own dead; and why the Line runs 11→12 AH.

**Method note.** Four agents read one or two notes each against the card list; **every finding acted on
here was re-verified by hand against the cached page before anything was written.** Two of the six fixes
above are corrections to cards that had already passed every other gate — the citation checker cannot
see a sender the source does not name.

---

## 52. The dialogue over the ⁨جمع⁩, and Ibn Kathīr's numbers as he gives them

**2026-09-23, Daniyal: "add the Abū Bakr and Zayd dialogue, and also add the figure of Ibn Kathīr,
cite as approximate value."** Both from #51's audit; both verified against the cached pages first.

**The dialogue is its own card, `RCT/E-RC65`, at #56 — the run-up to the ending, not the ending.**
⁨سیر ج۲ ص۴۳۱⁩, in Zayd's ؓ own words: why he was chosen («⁨إِنَّكَ رَجُلٌ شَابٌّ عَاقِلٌ لاَ نَتَّهِمُكَ⁩ …
⁨قَدْ كُنْتَ تَكْتُبَ الوَحْيَ⁩»), the order, **his objection** («⁨كَيْفَ تَفْعَلُوْنَ شَيْئاً لَمْ يَفْعَلْهُ
رَسُوْلُ اللهِ⁩»), and the three-word answer («⁨هُوَ -وَاللهِ- خَيْرٌ⁩»). #57 still ends the evening.

⚠ **ʿUmar ؓ is named inside Zayd's ؓ own sentence on that page. That is the page's wording, not a claim
about who proposed it — the "ʿUmar ؓ proposed it" account is not on this page and is not told here.**

**The honorific is spelled out in the quotation** because ⁨سیر⁩ prints it that way and a quotation is
verbatim or it is not a quotation; `check_citations` caught the ﷺ substitution immediately.

**The figures go on `ZIA/E-ZY17` as the book gives them** (⁨البدایہ ج۷ ص۳۵⁩): «⁨وقتل من المسلمين ستمئة،
وقيل: خمسمئة، **فالله أعلم**⁩», and the 450 of ⁨ج۷ ص۵۵⁩ twenty pages later. The card now says in its own
beats that **Ibn Kathīr's figures are approximate and that he says so**. That is stronger than the card
was before, not weaker: it was presenting one of his three numbers as *the* number.

**A collision worth recording.** The new card was first written as `RCT/E-RC38` — an id **already in
use** by a different card (⁨عمر ؓ⁩ to Quraysh, the framing card). The pool silently kept the later one
and `check_face_quotes` failed with what looked like a quotation error. **Before adding a card, list
the ids in use.** Renamed to `RCT/E-RC65`.

---

## 53. One more close, where the map actually moves — STOP D at #34

**2026-09-23, Daniyal: "we can put in summary slides/maps after checkpoints within this deck, so that
if time runs out we have stopping locations at multiple points."** Right in principle — it is #23
("build the closing pair for **every** stopping point"), and the overflow had grown to ~85 minutes with
no close of its own between #31 and #57.

**But a close is not a checkpoint. It is an ending**, and it has to pass two tests: it answers "what did
tonight mean?" and sets next week's question, **and its Line and its map have actually moved.** Applied
to the overflow, that leaves exactly one place:

| Candidate | Verdict |
|---|---|
| **After #34 — the terms at the forts** | **YES.** al-Yamāma is taken: the map goes blue, the Line gains the garden and the death of Musaylima. A real ending |
| After #43, #51 (ends of Parts VI, VII) | No. The story moves through *people*, not territory — the map and the Line are identical to #34's. A close there would show the same two pictures again |
| Parts IX–XI (the households) | No. Backstory: nothing on the Line moves at all. They reuse the final close (#50) |

**So: STOP D after #34, and the old STOP D becomes STOP E.** Five stops now — A (#15, hidden),
B (#20, hidden), C (#31, in place), **D (#34, in place)**, E (#57, in place) — plus the hatch, which is
what covers everywhere else: **one typed number takes the room to the muṣḥaf and STOP E from any point
in Parts V–XI, so the ending is never skipped.**

**The Line had to be split to do it.** `m05` (the Qurʾān gathered) was in `part5` with the garden and
the death of Musaylima; it now has its own group `part6`, so **STOP D lights the battle without lighting
the ending** and STOP E adds it. Both closes share one map scene, because between #34 and #57 the map
genuinely does not move.

**STOP D's four ⁨عبرت⁩ lines are the evening as it stands at #34** — `RC50`, `RC58`, `RC20`, `RC22` —
and **no line from Parts VI–VIII appears there**, because the room has not been told about the dead.

⚠ **Caught while building it:** the first draft of STOP D's next-week question said *"four hundred and
more of the men who carried the Qurʾān did not come back"*. That is a reciter count, and `ZIA/E-ZY17`
exists precisely to stop one being said: 450 is Ibn Kathīr's figure for **reciters, Companions and
others together**. Rewritten without a number.

---

## 54. The garden card — who called them in, and whose son killed him

**2026-09-23, Daniyal: "add the garden card."** The climax of the evening — Banū Ḥanīfa falling back
into ⁨حديقة الموت⁩ and the gate closing — was being told with **a nameless man** shutting it, and with
**the caliph's own son on that field** and the room never hearing it. Four approved pages carry it, and
the finding had been sitting in `ridda-campaign-the-conduct-of-the-wars.md` §6.6 on no card (#35).

`RCT/E-RC66`, now **#32**, immediately before the garden card it sets up:

| What | Page |
|---|---|
| The call: «⁨يَا بَنِي حَنِيفَةَ، الْحَدِيقَةَ الْحَدِيقَةَ! فَدَخَلُوهَا وَأَغْلَقُوا عَلَيْهِمْ بَابَهَا⁩» | ⁨الکامل ج۲ ص۲۱۷⁩ |
| The killing: «⁨وأدرك عبد الرحمن بن أبي بكر محكمَ بن الطفيل فرماه بسهمٍ في عنقه وهو يخطب فقتله⁩» | ⁨البدایہ ج۷ ص۳۴⁩ |
| Ibn Kathīr again, calling him Musaylima's ⁨وزير⁩ and counsellor | ⁨البدایہ ج۷ ص۶۰⁩ |
| The same killing **from ابن إسحاق** | ⁨سیر الراشدون ص۴۹⁩ |

**The face takes الکامل's wording deliberately.** The ⁨البدایہ⁩ page carries «⁨لعنه الله⁩» against both
men; **the evening narrates, it does not curse**, so that page supplies the killing clause only and the
imprecations are in neither the quotation nor the delivery.

**ʿAbd al-Raḥmān b. Abī Bakr ؓ is introduced here as Abū Bakr's ؓ son on that field, and nothing more.**
His own earlier story is not opened from the platform — it is not needed for this card, and it is not
on it. The runsheet's introductions table says so.

**Knock-ons:** the re-entry bridge past STOP C and the "into the garden" map slide both moved from
`RC20` to `RC66`, which now opens Part V; the overflow's hands-up beat opens on `RC66` and carries
`RC20`'s [HANDS] 4 inside it; STOP D is now after **#35**, STOP E after **#58**.

---

## 55. Evening 4's deck is hand-finished, and protected — 2026-09-24

*Recorded 2026-09-27: `S04.FINAL` and `S04_kinda_butah_yamama/pack_data.py` both cite #55, and the entry was
never written. This is it, from the commit that made it (`f644a3d`).*

Daniyal finished `S04.pptx` by hand: 142 slides against the build's 139, **his own maps** — *"some of the
maps had errors from you, and I want Muslim forces to be always in dark green"* — four more slides hidden,
and some closing lines rewritten in his own words. **That file is the source of truth for what the room
sees.** `S04.FINAL` says so and says **do not run `build.py`** for this evening; `pack_data.py` reads the
deck instead of the pool while the marker exists. The deck is 118 MB, over GitHub's limit, so it is
git-ignored; the repo carries `S04_share.pptx` (`tools/share_deck.py`: hidden slides dropped, notes kept,
images recompressed) and `S04.pdf`. Same principle as #38. **Caught doing it:** the printed cue sheet
carried the built deck's jump numbers, every one three slides off his deck's.

---

## 56. What evening 4 taught — 2026-09-27

Evening 4 was delivered to **STOP D** (his slide 67): Parts I–V, 34 cards (`DELIVERED.md`). Daniyal
reported four things, and each one changes how every evening from 5 on is built:

1. **The maps stood still.** *"If we had more maps and animated moving of troops as I speak it might have
   been more interesting. Atm its like a show map and say what happens in the map in later slides."* A map
   slide showed one finished picture; the cards that told it came after, as text. The build had rendered
   every intermediate step and placed only the last. → #58.
2. **The battle ended abruptly — and the treaty had no terms.** *"In the last slides we didn't even discuss
   the terms of treaty, it wasn't even in my learning material, so I was totally lost on that. We just
   mentioned Mujjāʿa's trick."* `RC22` said *"he settles on terms"* and never what they were; three approved
   pages give them (⁨الکامل ج۲ ص۲۱۸⁩ · ⁨سیر الراشدون ص۴۸⁩ · ⁨البدایہ ج۷ ص۳۵⁩). → #61, and evening 5 opens on them.
3. **The stop markers felt out of place.** *"Maybe the notes should carry more script to explain to me."*
   The STOP C slides' notes were build notes — *"BOOKEND OUT STOP C — the Line. Re-used verbatim…"*,
   *"MAP: tools/mapstudio/scenes/s04-close-stop-c.json at step 1"* — nothing to say. → #59.
4. **Only the deck goes to the lectern.** *"I have never used any of your artifacts like cuesheet, etc. I
   just use the pptx and its notes to deliver the lecture."* → #60.

**Also learned: he tells things from memory that are on no card** — Waḥshī ؓ at Uḥud and the Prophet's ﷺ
words to him, al-Barāʾ's ؓ eighty-odd wounds, Sālim ؓ leading the prayer at Qubāʾ. `DELIVERED.md` now has
a *Told from memory* list for each evening, **and the next evening does not tell those things again.**
Ask for it after every evening.

---

## 57. Evening 5: the houses are told where their men fall, and Oman and Mahra close it — 2026-09-27

The first plan put ~10 of the al-Yamāma dead in the evening and everything else — the rest of the dead,
the three houses, Kinda's kings — **behind the close**. Daniyal: *"I think we will gloss over a lot of
details with this, and miss material we have already collected … I think we should put them up at
appropriate places within the story, not at end."* He is right, and it is the books' own form: Ibn Kathīr
closes each year with the lives of those who died in it, and the *Siyar* is built man by man. **A life told
at the death is not a digression.** "Behind the close" would in practice have meant never.

**Settled — `S05_yamama_dead_oman_mahra/RUNSHEET.md`:**

- **Evening 5** = how the day ended (the terms; *"they became Muslims to the last man"*) → **the house of
  Umm Sulaym ؓ, told at the gate al-Barāʾ ؓ opened** → the men beside them → the banner and the reciters,
  **with the house of Abū Ḥudhayfa ؓ and Sālim ؓ told before they fall** → Medina and the Qurʾān →
  **ʿIkrima's ؓ road: his own story, then Oman and Mahra.** Daniyal added Oman and Mahra: *"a lot of this
  stuff I have mentioned from memory"* — the evening had less new material than it looked.
- **The reciters are told last** because their deaths are the one reason the books give for the
  collection (#48): the order of Part IV and Part V is that argument.
- **al-Barāʾ ؓ died at Tustar, not at al-Yamāma**; the tradition would tell his house there. It is told
  now, at the gate, while the room remembers him — and ends on Tustar, framed as a war not yet reached.
- **Evening 6** = Bahrayn → **Ḥaḍramawt, told from the beginning**, with Kinda's kings woven in where the
  room first asks *"who are Kinda?"* → Ibn Kathīr's summing-up. Ḥaḍramawt moves a fourth time, knowingly:
  it has never had the room to be told whole, and now it does.
- **Supersedes #50's "behind the close."** #50's own worry — flashbacks teaching the room that the Line is
  decoration — is answered in the build: every flashback is opened and closed aloud by a bridge, and each
  house gets **its own lane on the Line**, running into al-Yamāma.
- **Size:** 58 cards, 90.5 minutes budgeted; CORE 39. **Suggested cut `✂` on 22 cards → 36**, the size of
  evening 4 as spoken, which reaches Mahra. The cut is Daniyal's.

---

## 58. Maps build up on clicks — 2026-09-27

Chosen from three (#56.1): **built on clicks** over stage-by-stage fades (reliable, but nothing moves) and
video clips (smoothest, but fixed timing, large, and not editable by hand).

- **One slide per map, and it stays up while the speaker tells it.** Each click is a beat: an arrow wipes on
  in its direction of travel; an army's banner travels along its arrow; a territory fades to green; a mark
  with Map Studio's *Hide after step* fades out. The notes carry `▶ CLICK n` on the beat it belongs to.
- **Map Studio** gains one field — an army may name the arrow it follows — and `tools/render_scene.py`
  gains a **layer export**: the ground as one picture (terrain, places, starting territory, legend, scale),
  every mark as its own transparent picture cut to its size, and a manifest of where each sits, its step,
  its `until`, and its route.
- **The build writes PowerPoint's click animations itself** (python-pptx has no API for them).
- **One green for Muslim forces: `#2CB020`**, from his own garden map — his evening-4 maps used three.
- **The trial first.** One map (the garden at ʿAqrabāʾ) is built alone, played in PowerPoint, exported to
  video and checked frame by frame, **and shown to Daniyal before any other map is built.**
- **His maps stay his.** Fix in Map Studio and save into `tools/mapstudio/scenes/` before hand-finishing, or
  fix in PowerPoint: each mark is its own picture, and *Change Picture* keeps its animation.
- ⚠ His STOP D map colours the whole east green; by the books Oman and Mahra were still being fought. The
  bookend uses his map unchanged (#23); the Oman map shows the east still fighting, with one sentence.

---

## 59. Checkpoints, not mid-evening closes — 2026-09-27

Chosen from three (#56.3): **checkpoints and one real close**, over fully-scripted in-place closes and
closes hidden at the back of the deck.

- **A checkpoint is two slides in the flow** — the Line and the map, *where we stand* — and its notes are a
  script: two or three lines to say on each, a **⏱ time check**, a **CARRYING ON** sentence into the next
  part, and an **OUT OF TIME** ending: three closing lines, next week's question, ⁨السلام علیکم⁩, the dua.
  If the evening stops there, the next one opens on those two slides (#23 unchanged). It also re-anchors
  anyone who came in late.
- **«Tonight» and «Next week» appear only at the real close.** «Tonight» is **headings** — Daniyal rewrote
  evening 4's lesson slides as a list of what was covered — with one lesson line each in the notes, so #26's
  spoken ⁨عبرت⁩ stays.
- **Supersedes the in-place four-slide closes of #47 and #53, and the hidden early closes, from evening 5
  on.** No typed slide numbers either way.
- **Build notes leave the notes pane entirely.** File paths and step numbers live in the runsheet.

---

## 60. The lectern is the deck's notes; the home reading is one PDF of them — 2026-09-27

#56.4. A second artifact at the lectern does not get used, and a phone beside a laptop did not work.

- **`CUE.pdf` is no longer built** (supersedes #22's cue sheet). What it carried moves into each slide's
  notes, in the order the eye needs it: **⚠** a delivery warning · **SAY** — the beats, with `▶ CLICK` ·
  **⏱** (checkpoints only) · the quotation · the lesson line · the hands-up question · **BACKGROUND** last.
- **`BRIEFING.pdf` is replaced by the notes book** — every slide with its full notes beneath it, rendered
  by this repo's own HTML → PDF path (PowerPoint's notes-page export cuts long notes off), readable on a
  phone. It is the exact script he will deliver from.
- **The worksheet is dropped, and the 90-second pause with it** — assumed 2026-09-27 and not objected to;
  reversible. Supersedes the worksheet beat of #17 and #24.
- **The research notes stay the deeper reading**, and their PDFs are **re-rendered before any reading list
  is given**: the ones on disk dated from 7 September, before the corrections of the 19th and 23rd.

---

## 61. Every card answers the question the room will ask next — 2026-09-27

`RC22` passed every gate this repo has — the citations were exact, the card well formed, every name
introduced — and still left the speaker *"totally lost"*: it said *"he settles on terms"* and never what they
were. **No existing check can see a missing answer.**

**Settled:** every card is read for **the next question the room will ask** — *what were the terms, what did
the letter say, how many, what happened to them* — and the answer goes on the card, or the card says the
books do not give it. The runsheet carries a **"Questions the room will ask"** table beside *Introductions
checked*. This is #43 extended from names to content: #43 asks *who is this?*; #61 asks *and then what?*

---

## 62. One flashback per man — 2026-09-27

Daniyal, on the first evening-5 build: *"too much backstory on the families and we will not be able to keep
audience interest."* The numbers agreed with him. The two houses were 32 of the 55 cards. At the pace evening 4
was actually spoken (34 cards in the slot), the evening stopped in the middle of the second house and never
reached the Qurʾān, or Oman and Mahra, which were the reasons for the evening.

**Settled:** a house earns a card only where it makes a death on the field land harder. **One short flashback
per man, told where he falls** (#57's rule, now with a budget). The houses went from 16 and 16 cards to 5 and 9,
and the three weakest men-beside-them cards (each resting on a "the books differ" warning) left too.
**Nothing is deleted:** the cards stay in the pool, and every one of their stories is a line on a family tree
(#65). The runsheet lists where each one went.

## 63. Where a card moves, its map is its slide — 2026-09-27

Daniyal: *"at some places, we have a click click map, and the story should be ideally be said along with them,
but there are slides later which have the same thing."* The first build put a map in front of the card, with
its own intro and click lines, and then told the card again on the card's slide. **That broke the v5 spec as
written** (§2.2.4: *the card's notes carry* `▶ CLICK`) — a build fault, not a design question.

**Settled:** a card that moves is told on its map. The map slide carries the card's headline and date; its notes
are the card's own beats, with `▶ CLICK n` inserted before the beat each click lands on. The build refuses a
click on a beat the runsheet skips, and it still fails when a slide's clicks and its `▶ CLICK` lines disagree.
**A card with an Arabic quotation keeps one more slide after the map, for the words only**: its notes are the
quotation, its rendering and the lesson line. The story is not told twice, and the authority of the Arabic
(CLAUDE.md §1.4) is not thrown away. The first build's one map that is not a card's own, *last week in one
minute* before `RC67`, stays as it was.

## 64. A map fades what a click has finished with; the road stays — 2026-09-27

Daniyal: *"some of the click click maps become too crowded, we might need to use the mode that old markers
dissapear at later step."* The Oman map ended with ten captions on screen.

**Settled:** on every map, a caption fades on the click after its own, and so do spent arrows, a battle mark
once the story has moved on, and a banner that has travelled on. This is Map Studio's *hide after step*
(`until`), which `series/anim.py` already played as an exit fade. **The road itself stays**, so the last click
of a route map still shows the whole journey. The house maps also lost the legs whose cards left (#62).
**Known limit:** a static export (the deck's PDF, the PNG previews) shows every layer at once. In the show they
come and go; **the notes book shows each click's true picture.**

## 65. Each house opens on a family tree — 2026-09-27

Daniyal: *"an organogram showing the familial relationships would be nice"* — and *"we dont want to loose well
researched details."* The two requests are one answer.

**Settled:** each house opens on one diagram slide, built in `build.py` (boxes and lines, no generated image):
the house of Umm Sulaym ؓ, ʿUtba's house (Abū Ḥudhayfa ؓ and Sālim ؓ), ʿIkrima ؓ and Umm Ḥakīm ؓ, and Kinda.
**The face carries names and lines only**, about twenty words. **The notes give every relative one sourced
sentence** — the core lines first, then *"if the room is with you"* — and the BACKGROUND keeps, for home, the
beats of every card #62 moved off the running order. **Every line drawn is cited** in the runsheet's tree table.

**Two lines the trees refuse to draw:**
1. **Umm Sulaym ؓ to al-Barāʾ ؓ.** Daniyal asked that she be named *the mother of Anas and al-Barāʾ*. Our pages
   name her Anas's ؓ mother only; the house note §X.14 searched 10906, 30097 and 21712 for al-Barāʾ's mother and
   found none. So the tree draws al-Barāʾ ؓ as Mālik's son and Anas's ؓ elder brother, and the notes say
   *"Anas's mother"*. If a page is found — in the four books, or in a fifth Daniyal admits — the line goes in.
2. **Sālim ؓ as "adopted".** The adoption is `AS10`, which Daniyal struck as speaker's discretion; the tree
   says *freed slave* (`AS09`'s own words).

And Kinda's tree keeps `KD06`'s rule: **the old kingdom and the ridda sit side by side, with no line between.**

## 66. The Qurʾān's collection told whole; Ḥaḍramawt ends ʿIkrima's ؓ road — 2026-09-27

Daniyal: *"we also skipped all info about the collection of quran, this was a natural place to put this in"*;
*"maybe including kinda and hadramawt might be good"*; *"make sure you have got all the details of oman and mahra
and rest."*

**Settled:**
1. **Part V tells the collection whole:** the count (`ZY17`), the man sent for, as a boy (`Q7`), the order and
   the objection (`RC65`), what it was gathered from (`Q3`), ʿAlī's ؓ judgement (`Q4`), where the ṣuḥuf went
   (`Q5`, framed as a look ahead), and the ending (`RC37`). The jamʿ cards had sat in the pool **with no beats**,
   and so never reached a deck; they now have them. `Q1`, `Q2` and `Q6` are not run (they repeat `ZY17` and
   `RC65`, or give a second list of four beside `AS09`'s) — the note says so on each.
2. **Ḥaḍramawt and Kinda are Part VII**, as the end of the road Part VI is already on. The campaign note §12.2
   gives Ḥaḍramawt as last, as sequence, and our cards put ʿIkrima ؓ at the siege of al-Nujayr. It had been
   carried forward twice, from evening 3 and then evening 4. **Bahrayn moves after it**, to be told as
   *"meanwhile, in the east"*. Its cards have no beats yet and §7 carries findings on no card.
3. **The completeness pass.** §8's details that were on no card are now on `RC70`, `RC29` and `RC30`: Laqīṭ's old
   name and following, Ibn Kathīr's *"at that very hour"*, the relief's commanders, al-Muṣabbaḥ's clan and larger
   force. Umm Ḥakīm's ؓ father is on `TRN7`, and the Zayd b. Thābit ؓ notice lines are on `Q7`.
4. **Two corrections to cards written in this repo.** `RC37` said both books point at al-Bukhārī; ⁨الکامل ج۲ ص۲۱۹⁩
   does not (and the jamʿ note §5.1's "do not cite al-Kāmil for the jamʿ" was too strong: that page carries the
   order and its reason). `Q5` said *twenty-odd years later*, which is on no page.

**The price, stated plainly:** at evening 4's pace the evening now closes at Checkpoint 1, after the Qurʾān.
Oman, Mahra and Ḥaḍramawt are built behind it, and open evening 6 if not reached. The runsheet names the six
cards to strike if Daniyal wants Oman and Mahra that night.

---

## 67. The family trees are editable org charts; the house of ʿUtba grows to its famous in-laws — 2026-10-01

Daniyal, on the house tree of evening 5 (slide 27): *"make a greater organogram, that is editable as well with
me and add their other famous relatives: hind bint utba, abu sufyan... sohail bin amr."*

**Settled:**
1. **Every tree is an editable org chart.** Each box is a named PowerPoint shape (*person: Hind*), and every
   line is a connector glued to its two boxes — a child's line runs from the parent's foot to the child's head
   as an elbow, a marriage is a gold line between neighbours, Sālim's ؓ tie a dashed grey one. Move a box and
   its lines follow. The first build drew free-floating lines, which came apart the moment a box was moved.
2. **The house of ʿUtba b. Rabīʿa** now carries Rabīʿa → ʿUtba and Shayba; ʿUtba's children al-Walīd, Abū
   Ḥudhayfa ؓ and Hind ؓ; Hind ؓ ═ Abū Sufyān ؓ and their son Muʿāwiya ؓ; Abū Ḥudhayfa ؓ ═ Sahla ؓ, daughter of
   Suhayl b. ʿAmr ؓ; and Sālim ؓ. Every line is page-cited in the runsheet's tree table — Hind as *Umm Muʿāwiya*
   on ⁨سیر ج۱ ص۱۶۵⁩, Abū Sufyān's ؓ notice on ⁨ج۲ ص۱۰۶⁩, Suhayl's ؓ on ⁨ج۱ ص۱۹۴⁩.
3. **Daniyal chose what goes on the face.** Muʿāwiya ؓ yes; Abū Hāshim b. ʿUtba ؓ and Sālim's ؓ wife (al-Walīd's
   daughter, ⁨البدایہ ج۷ ص۵۰⁩) in the notes only; **Muḥammad b. Abī Ḥudhayfa off the tree** — his later life is
   ⁨مشاجرات⁩ material (the house note §1).
4. **Forward references stay framed.** Abū Sufyān ؓ and Muʿāwiya ؓ are *"names for evenings we have not
   reached"*; the notes say nothing of what came later. Hind's verses against her brother are not read out.
5. **A names-only diagram is the one slide allowed past the twenty-word body cap** (#21): about thirty words, all
   names and a three-line key.

The other three trees were rebuilt on the same engine, each with a real root box (al-Naḍr and Milḥān; Hishām b.
al-Mughīra) in place of the first build's unlabelled sibling bars.

---

## 68. Face headlines are names, not sentences — 2026-10-01

Daniyal: *"in the dead of yamama name the slides with the name of sahabi instead of an obscure english sentence.
I am going to deliver this mostly in urdu with mix of english, so obscure english sentences don't make much
sense."*

**Settled:** a card about a person is headed by the person's name. The ⁨لقب⁩ the tradition gave may follow it
(§1.2); where one man has several slides, a plain word or two tells them apart — *Sālim ؓ at Qubāʾ*, *Sālim ؓ —
the banner*, *Abū Ḥudhayfa ؓ at Badr*. Never an English sentence: the room hears Urdu, and a sentence on the face
in a language the speaker is not using is noise. **Card titles stay as the researchers wrote them** — they are
the index of the pool — and the face is set in each evening's `build.py` `FACE_TITLE`. Applied to evening 5's
Parts II–IV (twenty-one cards); standing for every evening from here.

Also today, after the same conversation: **a deck Daniyal has saved edits into is never rebuilt over** — see #67's
guard, and `CLAUDE.md` §1.7. The rule exists because a rebuild destroyed half an hour of his work this morning.

---

## 69. A front closes on its map before the next opens — 2026-10-01

Daniyal: *"dont you think that the transition from oman to mahra is rather sudden? there is no proper closing of
oman."* It was: Dabā ended on *the rebels broken*, the settlement of Oman was one line at the foot of the
notes, and the next slide was already Mahra.

**Settled:** every front gets its closing on its own map before the story moves — what became of the defeated,
who stayed, what went to Medina — and the hand-over names the men who carried on. For Oman: three clicks on the
Oman scene between Dabā's words slide and Mahra — Oman settled and Ḥudhayfa stays · the fifth to Medina with
ʿArfaja · ʿIkrima ؓ on to Mahra with Nājiya and ʿAbd al-Qays, the men who had come to the rescue. The card
(`RC29`) carries the closing as beats 7–8 with both books' lines; Dabā's own slide stops at beat 6 and Mahra's
starts at its beat 2, so nothing is told twice (#63). **Standing for evening 6:** Mahra, Ḥaḍramawt and Bahrayn
each close the same way before the next opens.

Also corrected on the way: *ten thousand* killed at Dabā is both books' figure (⁨البدایہ ج۷ ص۴۲⁩ has it too), not
Ibn al-Athīr's alone; and the books part on ʿArfaja — ⁨الکامل⁩ has Ḥudhayfa staying, ⁨البدایہ⁩ has ʿArfaja returning
to his companions — so the notes say both, each as its book's.

---

## 70. The Ridda's fighting ends on evening 6; evening 7 is the hinge — 2026-10-07

Daniyal, after delivering evening 5 to Checkpoint 2: *"aim is to wrap up ridda and hang on a cliff hanger to
the start of persian and roman invasion at end of session 7"* — and, on the shape offered: *"we must not miss
any detail or gloss over"*, *"the older background of ikrima needs not be mentioned"*, *"the maps and animation
approach of season 5 and the functionality we built, please do use that."*

**The arithmetic that forced the choice.** The Ridda remainder *as built* is Part VII of evening 5 — 13 cards,
24 min — plus five Bahrayn cards with **no beats**, plus `RC35` and `RC36`. That is **one evening, not two**. To
land the cliffhanger at the end of evening 7 without compressing anything, the slack is spent on the two things
the repo already owed: **Bahrayn told whole**, and **the Ridda's own closing reckoning**, which has never been
carded at all.

**Settled:**

1. **Evening 6 = the last two fronts, and the fighting ends.** Part I is Ḥaḍramawt and Kinda — evening 5's
   Part VII, unreached, and **already production-complete** (maps rendered and placed with named click layers,
   notes written). Part II is **Bahrayn told whole**, as *"meanwhile, in the east"* — because ⁨البدایہ ج۷ ص۶۱⁩
   puts the year-12 fronts side by side and the campaign note §12.2 makes Bahrayn concurrent with al-Yamāma and
   with Oman/Mahra, and **Ḥaḍramawt last**. Part III is over-build (#20): the fronts nobody tells.
2. **Evening 7 = the hinge, «⁨اس کے بعد کیا تھا⁩».** The peninsula in one colour · who did **not** break away ·
   the Ridda's last word · why it did not break again · what the two empires looked like · and the two letters
   that leave Medina. **It closes at the threshold and crosses nothing** — `ISA/E-C9` onward is al-Yarmūk and is
   not touched.
3. **The cliffhanger is honest chronology, and this is the page that makes it so.** Ibn Kathīr opens his year-12
   chapter in his own voice, unhedged: «⁨استُهلَّت هذه السنة، وجيوشُ الصديق وأُمراؤه الذين بعثهم لقتال أهل الرّدّة
   جَوّالون في البلاد يمينًا وشمالًا، لتمهيد قواعد الإسلام⁩» — ⁨البدایہ ج۷ ص۶۱⁩. On the next page the march to Iraq
   is dated into the same month. **⚠ That dating is al-Madāʾinī's, by isnād, as Ibn Kathīr transmits it** —
   «⁨وقد ذكر المدائني بإسناده أن خالدًا توجّه إلى العراق في المحرم سنة اثنتي عشرة⁩», ⁨ج۷ ص۶۲⁩. Say *"al-Madāʾinī
   dates it to Muḥarram 12"*, never *"it was Muḥarram 12"*. **The route was disputed too, on the same page:**
   al-Wāqidī gives two accounts — straight on from al-Yamāma, or back to Medina and then the Kufa road to
   al-Ḥīra — and Ibn Kathīr rules «⁨قلت: والمشهور الأول⁩». Tell it that way.
   ⚠ *Earlier in this entry a line «لمَّا فَرَغ خالدُ بن الوليد من اليمامة» was attributed to ⁨ص۶۲⁩ as Ibn
   Kathīr's undated framing. **It is not on that page** and has been removed — checked against the cache,
   `sources/shamela/30097/3208.txt`.*
4. **ʿIkrima's ؓ own background is not told, in any evening.** He deleted `TMW/E-TRN6`, `TRN7`, `TRN8` and
   Tree C from his deck and has now made it standing. He was introduced on evening 4 (`RC15`) and that stands.
   **This narrows #62** for this man: no flashback, not even where he falls. `TRN10`–`TRN12`, `TRN22`, `TRN23`
   (his death in Syria) stay held, and are not a licence to reopen the Mecca material.
   ⚠ One consequence to fix: evening 5's bridge slide 53 still says aloud *"But first, who he was"* — the cards
   that answered it are gone.
5. **#68 is extended to Part VII, and that is evening 6's largest writing job.** Sixteen slides across eleven
   cards carry English sentences, questions, quotations and relative clauses where a name belongs — including
   four consecutive slides about al-Ashʿath with his name on none of them. The eleven replacement faces are in
   `S06_hadramawt_bahrayn/RUNSHEET.md`; they go into that evening's `build.py` `FACE_TITLE`.
6. **The map pipeline is unchanged and is reused as built.** `make_maps.py` → `tools/render_scene.py --layers`
   → `series/anim.py`, maps building on clicks (#58), a moving card's map *is* its slide (#63), captions fading
   when their move is done (#64), **a front closing on its own map before the next opens (#69)** — which now
   governs Bahrayn too. `tools/mapstudio/scenes/bahrain-darin.json` **already exists on the same schema** but
   has all ten objects on `step: 1`: it needs steps and `until` authored, not a new scene. Evening 7's bases
   likewise exist — `southern-fronts`, `13ah-where-we-stand`, `iraq-hira`, `syria-ajnadayn`.
7. **One real research gap, and it is evening 7's only one.** The condition of the two empires in 11–12 AH is
   **nowhere in this repo** — not Sasanian succession after Khosrau II, not Heraclius's war of 602–628 or his
   recovery of the Cross, nothing on how either state looked to Arabia. `docs/PRIMER.md` has one unsourced
   sentence and `maps/world_632_kandg.png` is a video frame (`MAPS.md` §: for slide drama only). **A page-cited
   note is owed before evening 7 is built.** Two assets reduce its size: the Persian court-killing is **already
   spoken** (evening 3, `AAA/E-AW01`, `AW02` — Kisrā killed by his own sons), so Persia's instability is a
   callback, not new material; and `ISA/E-C2`'s own cached page carries a contemporaneous Muslim reading of
   Persia's condition in Arabic — «⁨فالحمد لله الذي فض خدمتكم وسلبَ مُلْككم ووهنَ كيدكَم⁩», ⁨البدایہ ج۷ ص۶۴⁩.
8. **`ISA/E-C2` needs one correction before it can be the cliffhanger.** Its body opens *"Khālid ؓ had taken
   al-Ḥīra"*, which is past the threshold and is **not what ⁨ج۷ ص۶۴⁩ supports** — that page precedes al-Ḥīra
   (⁨ص۶۹–۷۱⁩) in Ibn Kathīr's own order, and the al-Ḥīra link in the source is only that al-Shaʿbī was read the
   letter by Banū Buqayla *of* al-Ḥīra. Rewrite the opening sentence and the card is a clean threshold.
9. **No ISA or QMA card has a `Beats:` list, and nor do the Bahrayn five, `RC35`, `RC36`, `RC39`, `TB22`,
   `TB24`, `TB25`, `TB10`, `TB13`, `TB06` or any of the 26 Ibn Khaldūn cards.** Beats are what reach the notes
   (#39, #60), so **every card either evening uses must be given beats first.** This is now the standing first
   step of building any evening from this pool.
10. **The arc may run past evening 7, and that is not a failure** (#20). The room objected to speeding up after
    session 1. If evening 6 does not reach Bahrayn, Bahrayn opens evening 7 and the hinge moves to evening 8.

---

## 71. An evening changes direction once, and says so when it does — 2026-10-07

Daniyal, on the first evening-6 order: *"when you put in the missing pieces, the order makes sense, going back
and forth in timeline unnecessarily again and again maybe would give bad impression."* The draft changed
direction four times — a 10 AH flashback, then 11–12, then forward years, then back to 11 for Bahrayn, then
back again to early 11 for the uncarded fronts.

**Settled, and standing for every evening:**

1. **One direction change per evening, and it is announced aloud.** Evening 6 has exactly one — the 10 AH
   Kinda delegation — and the speaker says *"before any of this"* before it.
2. **Concurrent fronts are told in the sources' own sequence, not in the order they were researched.** The
   campaign note §12.2 has Bahrayn as *"meanwhile"* and **Ḥaḍramawt last**, so Bahrayn now comes first and
   the last front closes the evening's fighting — which also deletes the *"meanwhile"* reversal the draft had.
3. **Forward references go at the end, where nothing follows them.** `YK16` and `PG41` sat mid-evening and
   dragged the room forward and back. This narrows the ↪ device of #28: a look ahead may still be framed and
   spoken, but not between two cards that then return to the earlier year.
4. **Retrospective material belongs in a retrospective evening.** The uncarded fronts (Quḍāʿa, §9.1's four
   coastal actions, Najrān's covenant, Thaqīf, the Azd) moved to evening 7, whose whole mode is looking back.
5. **A statement about a whole period is not a timeline step, and may open an evening.** Hence `RCT/E-RC80`.

**`RCT/E-RC80`, the new frame card** — Daniyal asked for this Arabic on a card: Ibn Kathīr's own unhedged
sentence opening his year-12 chapter, that the year began with al-Ṣiddīq's ؓ armies *"roving the land right
and left"*, ⁨البدایہ ج۷ ص۶۱⁩ (cached, 30097/3207). It is told over Arabia with **every front lit at once** and
one grey patch left, and it is the licence for the evening's shape: ⁨يمينًا وشمالًا⁩ is the point. It carries
the standing ⚠ that **the books do not fix the months inside 11–12 AH**, so the order is the course's, not
theirs. **The same card returns at evening 7 as the hinge** — the bookend device of #23 applied inside the arc.

---

## 72. Two evenings in one deck, and Daniyal picks the stop on the night — 2026-10-07

Daniyal: *"I think you should try to build the material for both this session and next in one slide pptx,
I will decide where to stop based on available time."*

This is #20 ("build ~70 minutes for the 45-minute slot and let Daniyal cut") taken one step further, and it
is the pattern evening 4 already used — Parts I–IV planned, Parts V–XI built behind the close (#47–#50).
What is new is that the stop is **chosen at the lectern, not in the runsheet.**

**Settled:**

1. **`S06` is one deck covering what were planned as evenings 6 and 7** — 44 cards, ~82.5 min budgeted,
   ≈ 60 min at his measured pace. Ten parts.
2. **Four checkpoints, and the deck is built so any of them can be the end** (#59). Each is a Line + map pair
   with a scripted carry-on *and* a scripted ending, and whichever is used opens the next evening verbatim
   (#23). The runsheet's *"four stops"* table says what each one leaves behind:
   **CP1** Dārīn, 15 cards · **CP2** al-Nujayr, 24 · **CP3** `PG41`, 28 — *the natural evening* ·
   **CP4** `RC35`, 38 — *the Ridda finished, Arabia in one colour* · the close, 44.
3. **No typed slide numbers and no hidden early closes.** #59 already retired those; a checkpoint is simply
   two slides in the flow, and he carries on or stops.
4. **The deck ends at Checkpoint 4 until two things are done:** the two-empires research note (Part IX) and
   beats for the `ISA`/`GSA` cards (Part X). ⚠ **Checkpoint 4 is a complete evening on its own** — the Ridda
   finished, with the peninsula in one colour — so a deck that stops there is not a deck with a hole in it.
5. **Ordering is unchanged and still governs** (#71): one announced step back (Part III, 10 AH) and one
   announced turn outward (Part IX). Everything else runs forward, and the retrospective material is
   gathered into Part VI rather than scattered among the fronts.

**Two answers from Daniyal recorded the same day, both in `docs/catalogue/DELIVERED.md`:**

- **What he told from memory on evening 5: he does not recall.** So that evening has **no spent-material
  list**, and #56 cannot be applied to it. The exposure is small — evening 6 opens on fronts the room has not
  heard of — but the lesson is a process one: **the note has to be made on the night, in the margin of the
  runsheet, not asked for afterwards.**
- **Evening 5's slides 11–13 are his own maps and diagrams**, deliberately picture-only. Not unfinished
  slides, and not to be "fixed".

---

## 73. Feedback becomes a gate: `docs/VISION.md` and `tools/check_vision.py` — 2026-10-08

Daniyal, after studying evening 6's slides 1–25: *"You need to fix the comments but more importantly we need to
make the system that generates our content always within the vision given my feedback."*

**What the review found was not twenty slide faults but five causes, each repeated:**

| Cause | What it produced | Root, once looked for |
|---|---|---|
| Notes he cannot deliver from | 540–2,091 words under one slide | the pane dumped every sub-note above the beats — and **the parser silently dropped any beat not written `Cue — detail`: 49 of 288, 17%**. The line he asked for at slide 16 was on the card |
| Faces that assume knowledge | *"who said this?"* · *"taken by who?"* · *"where or what is al Khatt??"* · a title that *"will make no sense"* | no rule required a speaker, an agent, a gloss, or a name |
| Maps that do not move with the story | a stale icon, an unexplained arrow, 10px captions, a title box over the march | the scene was hand-placed. Evening 5's scenes already had the box off and the text doubled; nothing made the new one inherit either. Its captions had no `size`, so the painter fell back to 10px |
| Images with no brief | *"where is the description…?"* | the build wrote an IMAGE BRIEF into the notes and the next call overwrote it; and the "brief" was the story's first thirty words |
| Order | *"didn't this happen before slide 20?"* | a card's statement belonged to the card after it |

**Settled:**

1. **`docs/VISION.md` is the house style as numbered rules**, each with the words of his that produced it and the
   check that enforces it. It is read before anything is generated.
2. **`tools/check_vision.py` is the gate**, and `build.py` runs it. Run on the deck he had just reviewed, it
   reproduced his comments unprompted — *"the key 'al-Qaṭīf, Hajar' — 'taken' does not say who did it"* — and found
   **578 breaches of 17 rules**. After the rebuild: none.
3. **Notes are two tiers** (`series/notes2.py`): a SAY block of short spaced cues, then a drawn rule, then the
   detail. Beats are written `Cue — detail`; the parser now keeps every beat.
4. **Maps are written through `series/mapkit.py`**, whose helpers satisfy the map rules by construction, and which
   refuses to save a scene that breaks one. Frames are computed from the projection (equirectangular at 30°N —
   `view.cx` is longitude × cos 30°, which is why setting it by trial had taken three renders).
5. **A face names things**: `FACE_SPEAKER`, `FACE_SCENE`, `FACE_WHEN`, `FACE_CUT`, `IMAGE_BRIEF` in `build.py`;
   `deck2.statement_slide` takes a speaker and scene lines; the build refuses a placeholder with no authored brief.
6. **Moments of faith get a slide of their own** (`IMAN`), and reading a page includes looking for the line that
   could be said aloud to a room (VISION D2 — his second message of the day).
7. **The gate is not the eye.** It passed a close-up with three forces on one spot. Looking caught it; rule M15
   (nothing printed over anything else) was written because of it, and found six more collisions on a map not yet
   looked at. **Every new map's rendered steps are opened before hand-over; what the eye catches is the next rule.**

**Two things he should confirm.** (a) **The year of the Prophet's ﷺ letter to al-Mundhir b. Sāwā.** He asked for
the opening map to be titled *8 Hijri*. The embassy is on a page — ⁨البدایہ ج۴ ص۵۱۷⁩, from Ibn Isḥāq — **but no
page we hold gives its year.** The slide says *"in the Prophet's ﷺ lifetime"* and the note says the year is
commonly put at 8 AH. (b) **I2** — image briefs ask for places, animals and objects, never a person or a face — is
a default proposed for this room, not something he has said.

---

## 74. Four corrections from the page-cited Bahrayn sequence — 2026-10-08

`docs/research/bahrayn-the-front-as-a-sequence.md` was written the same day as #73 and read after the first rebuild.
It corrects four things that rebuild had put on slides or maps. **Each was a detail supplied where a page was silent.**

1. **The year of the embassy to al-Mundhir b. Sāwā.** #73 said no page we hold gives it. One does:
   ⁨الکامل ج۲ ص۹۱⁩ sets the envoys under **year 6**, then adds *"and it is said that his sending was in the year
   eight"*; ⁨البدایہ ج۵ ص۱۹⁩ has *"before the conquest of Mecca"*. So Daniyal's *"8 hijri"* is the «⁨قيل⁩» view, not the
   main one. The slide says **"before the conquest of Mecca"**; the note gives both years.
2. **No page says a *letter* went to al-Mundhir** — every page says al-ʿAlāʾ ؓ was *sent*. The map caption now
   reads *"sent by the Prophet ﷺ"*.
3. **al-ʿAlāʾ ؓ forded the strait on horseback; he did not sail.** ⁨البدایہ ج۷ ص۴۰⁩: *"walking on what was like
   soft sand with water over it."* The map had given him a ship. It is a strait forded, not a sea parted, and the
   notes say so.
4. **Two things on no safe-list page:** that al-Jārūd ؓ was *inside* Juwāthā (his token no longer says so), and
   the words *"Lakhmid"* and *"al-Ḥīra"* — the page names the man's fathers, al-Nuʿmān b. al-Mundhir, and no more.
   The cue now says *"a king of the old royal house"*.

**The lesson is VISION D3, and it cut the other way this time:** the rules that make a slide vivid — an icon for
every force, a caption for every click — are exactly the rules that tempt a builder to fill a silence. **Read the
front's sequence note before scripting its maps**, not after.

---

## 75. The close-up builder; diagrams say so; and the rest of the Bahrayn note reaches the cards — 2026-10-08

**What was asked.** Daniyal, of the system built under #73: *"did you also build something for closeup map
builder?"* It had been half built — helpers for a march, a siege, a trench, and close-ups framed by hand.

**What was found first, by looking.** The vision gate was green and most of the rendered frames had never been
opened. Opening them found: three names running off the edge of the theatre map; flags over other men's names;
banners standing in the sea; **Juwāthā drawn 22 km east of the site usually given for it**; **Dārīn in two different
places on two maps**; and a Hajar close-up with al-Ḥuṭam camped at Hajar and al-ʿAlāʾ ؓ to the west of it — where
⁨الکامل ج۲ ص۲۲۳⁩ has al-ʿAlāʾ ؓ camped *at* Hajar and coming down on al-Ḥuṭam "from the side next to Hajar".
The collision check had passed all of it, because it estimated a banner as a circle and a letter as half an em.

**What was decided.**

1. **Close-ups are built, not framed** — `mapkit.closeup(slug, title, centre, radius_km, parent=)`. A town comes in
   from the parent map at the parent's coordinates (`bring`). Names choose their own side (`settle`); a caption given
   no position finds the free spot nearest its subject; a force that leaves takes its road with it. The whole table
   is in `docs/VISION.md` §5.
2. **A diagram says it is one.** Where the page gives only *sides* — the trench month at Hajar, the fort at
   al-Nujayr, the strait at Dārīn — the close-up is made with `diagram=True`: no scale bar, the words **"a diagram —
   not to scale"** on its face, and nothing placed by coordinates. This is §0.1's rule for a
   `[CONVENTIONAL-ESTIMATE]` — labelled on the slide itself — applied to geography. **Reason:** a scale bar under
   trenches forty kilometres long is a claim, and no page makes it.
3. **One place, one spot** (M12): a town is drawn in the same place on every map of an evening. One gazetteer at
   the head of `scenes.py`. Juwāthā is now at the mosque of Jawāthā (25.47 N, 49.68 E), 12 km from Hajar.
   **Tārūt, where Dārīn stands, is drawn three times its size and set off the shore — on every map alike —** because
   at these scales it would be a dot under al-Qaṭīf's own; the script says so.
4. **The collision check uses the painter's own arithmetic**, read out of `tools/mapstudio/src/render.js`.
5. **Three deck-level rules**, in `tools/check_vision.py`: **M2** a siege ring on a wide map owes its place a
   close-up; **M7** a slide that tells a siege has one drawn; **M12** one place, one spot. **M10** now covers
   lettering and flags. **F4** lets a quotation straight after another at the same place inherit its scene.
6. **The siege of al-Nujayr has a close-up** (`s06-nujayr`, before `TSY/E-YK12`), every move one clause of
   ⁨الکامل ج۲ ص۲۳۱⁩. The "three roads" are ⁨الطبری⁩'s alone and are **not drawn**. `TSY/E-YK11` skips its beats 5–7
   in the runsheet so that nothing is said twice.
7. **The Bahrayn sequence note's §0 had eighteen corrections; #74 applied four.** The rest are now on the cards
   (`RC24`, `RC25`, `RC26`, `RC27`, `RC71`–`RC74`, `TB24`): *came down at*, never *took*; the ṣadaqa *divided out*,
   not *held back*; *clans of Tamīm*, not *the Abnāʾ*; al-ʿAlāʾ ؓ camps **at Hajar**; **the man they made king is
   taken on the night of the trenches, not at Dārīn**; the assault goes **over the trench**, not "from both sides";
   the two books do **not** give the water the same depth; a doubtful word under `RC73`'s second quotation is
   flagged. **New card `RCT/E-RC87`**: the words of the duʿāʾ at al-Dahnāʾ, from the *other* telling
   (⁨البدایہ ج۶ ص۲۳۱⁩), under its own page and marked "in another telling" on its face.

8. **A map key's label is measured, not estimated** (`series/deck2.py`). The contact sheet showed a wrapped name —
   *Banū Muʿāwiya*, *al-Mundhir b. Sāwā ؓ* — printed over the line beneath it, on three slides. The layout had
   guessed 0.21in a character. It now measures the label in Georgia, and an honorific never wraps alone.

**Why it matters beyond this evening.** #74's lesson was *read the front's sequence note before scripting its
maps*. This is the same lesson from the other side: **read it to the end.** A short list of eighteen was applied
as a list of four because the first four were the ones that had been asked about.

**Not done.** `S06_notes.pdf`, the home-reading book of #60, has not been made for this evening. The Ḥaḍramawt regional map is still evening 5's hand-placed scene, brought up to the rules
(`settle`, owners for every arrow) rather than re-scripted. `PEOPLE.md` promotions; Parts IX–X.

