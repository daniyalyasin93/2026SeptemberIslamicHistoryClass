# Spec — production pipeline v4, and session 2

**Date:** 2026-09-06 · **Status:** approved by Daniyal · **Supersedes:** the artifact conventions in
`2026-08-26-lessons-from-history-v2-design.md`; the session-1 spec
(`2026-09-03-L01-v3-spec.md`) is left intact as the record of what was delivered.

**Decisions this spec implements:** `docs/DECISIONS.md` **#19–#26**. Read those first — they carry
the reasons. This file carries the shapes.

---

## 0. Why v4 exists

Session 1 was delivered. It worked, and four things did not:

| What went wrong | Source | Fixed by |
|---|---|---|
| Ran short; ended just before the ردة | Daniyal | §2 — build 70 min for a 45 min slot |
| Slides ugly, text-heavy, unreadable from the back, too few graphics | Daniyal + both managers | §3 — white ground, type floor, Gemini visuals |
| The script was too wordy to follow at the lectern | Daniyal + manager 2 | §4 — one-page cue sheet, prose moves home |
| No ending, no interactive activity, no summary | Daniyal + both managers | §5 — the close, and the two interaction beats |
| Felt like a speed-run; too few lessons drawn | manager 2 + a man in the audience | §6 — the pool, and one عبرت per event |

Two things went **right** and are being expanded, not changed: the page-cited Shamela research
notes, and the fact that the deck is built from a script rather than hand-edited.

---

## 1. The six artifacts, per session

`LNN_<slug>/` now contains exactly these. Anything else is scratch.

| File | Audience | Built by | Rule |
|---|---|---|---|
| `CONTENT.md` | Daniyal, at the desk | hand + research | The **pool**. Numbered event cards. He deletes rows. |
| `SLIDES.md` | Daniyal → Gemini | hand, from `CONTENT.md` | One block per slide. Carries the `IMAGE BRIEF:` prompts. |
| `build.py` → `LNN.pptx` | the room | python-pptx | Editable. White ground. Placeholder boxes for Gemini images. |
| `CUE.html` → `CUE.pdf` | the lectern | Chrome headless | **One page. No sentences.** |
| `BRIEFING.html` → `BRIEFING.pdf` | Daniyal, at home | Chrome headless | The prose. Read twice. Never at the lectern. |
| `WORKSHEET.html` → `WORKSHEET.pdf` | the room | Chrome headless | Blank map + blank timeline strip + عبرت lines. |

**Language (decision #19):** all six are **English**. Arabic only as verbatim source quotation, in
`Traditional Arabic` Naskh, with an English rendering beneath. **No generated Urdu, anywhere.**
Daniyal translates at the lectern or by hand-editing the deck.

### 1.1 `CONTENT.md` — the event-card format

Every event in the period gets one card. This is the only place narrative facts are authored;
`SLIDES.md`, `CUE` and `BRIEFING` all derive from it.

```markdown
### E-14 · Khālid ؓ at Buzākha — Ṭulayḥa breaks
**Tier:** CORE · **When:** Rabīʿ al-Ākhir 11 AH `[SOURCED]` · **Map:** Buzākha lights; Asad/Ghaṭafān flip back
**What happened:** <3–6 sentences, plain, tellable>
**The statement:**
> ‹verbatim Arabic on its own line›
> — البدایہ والنہایہ ج۷ ص۲۹ · https://shamela.ws/book/30097/NNNN
> *English:* "<rendering>"
**عبرت:** <one sentence>
**Hands-up?** no
```

Tier tags: **`CORE`** (the evening breaks without it) · **`GOOD`** (include if time) ·
**`CUT`** (recorded so it is never re-researched; not planned for delivery).

### 1.2 `SLIDES.md` — the Gemini handoff

```markdown
## Slide 12 — statement
**Headline:** He would not negotiate the zakāt
**On screen:** ‹Arabic, 44pt› / ‹English rendering, 32pt›  — 14 words total
**You say:** Buzākha · Ṭulayḥa flees to Syria · the tribes come back in
**IMAGE BRIEF:** <paste-ready Gemini prompt, ends with:
  "Flat pure white #FFFFFF background, no border, no text in the image, 16:9.">
```

---

## 2. Runtime — 45-minute slot, ~70 minutes built

```
0:00  Bookend in — last week's closing Line + closing Map, unchanged     4
0:04  The story in scenes; the map moves; hands-up ×3                   22
0:26  Worksheet — 90 seconds, silent, they mark map and timeline         2
0:28  The story continues                                              12
0:40  Bookend out — the Line with tonight lit up                         1
0:41  Bookend out — the Map, now vs. when we walked in                   2
0:43  Tonight's عبرت lines, all on one screen                            1
0:44  Next week, as a question                                           1
0:45  Loud السلام علیکم → dua
```

**No Q&A** (decision #24). Written slips into the box; Daniyal stays 15 minutes afterwards.

**Over-build rule:** `CONTENT.md` holds ~70 minutes of `CORE`+`GOOD` material. The slot is 45.
Daniyal cuts. Overflow rolls to the next session (decision #20) — it is never compressed.

---

## 3. Deck rules, enforced in `build.py`

The build **raises and fails** on any violation. This is deliberate: session 1's defects were all
things a check would have caught.

| Rule | Value |
|---|---|
| Background | flat `#FFFFFF`, every slide |
| Identity | teal `#104A43` title bar, gold `#C49A45` rule — never a coloured ground |
| Minimum type anywhere | **24pt** |
| Body type | **28pt** |
| A key statement | **44pt+** |
| Headline | **40pt** |
| Body words per slide | **≤20** |
| Slide kinds permitted | full-bleed image/map · large statement · diagram · timeline strip |
| Bullet-list slides | **do not exist** |
| Image placeholders | real, correctly sized, editable — never flattened |

Arabic runs are set in `Traditional Arabic`; English in `Georgia` (headline) / `Segoe UI` (body).
Latin digits everywhere.

---

## 4. The lectern

`CUE.pdf` is **one A4 page**, landscape, three columns, ~18pt:

- Column 1: the running order — scene names, in order, with the clock time each should start.
- Column 2: names and dates only. No sentences.
- Column 3: the four or five عبرت lines, and the three hands-up cues marked `[HANDS]`.

Bottom strip: **`VOICE — LOUDER` · `PAUSE BETWEEN IDEAS` · `POINTER` · `END: salām, then dua`**
— the four speaking notes the managers gave, on the page he is already looking at.

---

## 5. The close, and the bookend (decision #23)

Three closing slides, then the ending ritual:

1. **The Line, tonight lit.** The full series timeline strip with only this session's pegs
   highlighted. Rendered by `series/make_visuals.py` as `line_sN_lit.png`.
2. **The Map, now vs. then.** Territory at the close of the evening, with the start-of-evening
   extent shown as a dashed outline beneath it. `map_sN_close.png`.
3. **The عبرت lines**, all of tonight's on one screen, nothing else.

**Slides 1 and 2 are re-used verbatim as slides 1 and 2 of the following session.**

**Because the stopping point is Daniyal's choice, both closing pairs are built for session 2:**
`line_s2_lit_13AH` / `map_s2_close_13AH` **and** `line_s2_lit_23AH` / `map_s2_close_23AH`.

---

## 6. Session 2 — «بارہ سال», 11–23 AH

**Starts exactly where session 1 stopped:** the morning after سقيفة, with the ردة about to break.
Session 1 showed the room a ردة map and stopped. Session 2 opens on it.

### 6.1 Coverage — the pool, not a syllabus

The pool spans **11–23 AH** in five blocks. Daniyal filters; a likely cut lands at 13 AH.

| Block | Span | Status |
|---|---|---|
| A · The ردة | 11–12 AH | **research already complete** — `arabian-tribes-and-the-ridda-setup.md` (785 lines, page-cited) |
| B · أبو بكر ؓ's other work | 11–13 AH | gap — جيش أسامة, the جمع of the Qur'an after يمامة, the letters, his death and the نص for عمر ؓ |
| C · The first conquests | 12–15 AH | gap — Iraq under خالد ؓ, the Syrian front, أجنادين, **يرموك**, **قادسية** |
| D · عمر ؓ's state | 15–23 AH | gap — بيت المقدس and the عهدة, the دیوان, the هجری calendar, the provinces, أمير المؤمنين |
| E · The end | 23 AH | gap — نهاوند, the شورى, the assassination |

### 6.2 What the pool must carry, beyond events

Daniyal's explicit ask: *"more and more events, maps, great statements and dialogues."* So every
`CORE` card must attempt all three, and say so when a source does not supply one:

- **A map move** — what changes on screen when this is told.
- **A verbatim Arabic statement or dialogue**, with printed page **and** shamela URL.
- **One عبرت line.**

Where no statement survives in the safe-list sources, the card says **"no statement in the
sources we use"** rather than reaching for a weaker one. `CLAUDE.md` §1.1 is not relaxed.

### 6.3 Maps required

Already built: `map_s2_ridda.png`, `map_s2_twelve.png`, `map_arabia_blank.png`, `basemap.svg`.

To build:

| Asset | Shows |
|---|---|
| `map_s2_open_11AH.png` | Territory the morning after سقيفة — the bookend-in map |
| `map_s2_usama.png` | جيش أسامة's route out and back |
| `map_s2_iraq.png` | خالد ؓ in Iraq, 12–13 AH |
| `map_s2_syria.png` | The Syrian front to أجنادين |
| `map_s2_yarmuk.png` | يرموك, 15 AH |
| `map_s2_qadisiyya.png` | قادسية, 15/16 AH |
| `map_s2_quds.png` | بيت المقدس, 16/17 AH |
| `map_s2_nahawand.png` | نهاوند, 21 AH |
| `map_s2_close_13AH.png` | Closing extent if the evening stops at أبو بكر ؓ |
| `map_s2_close_23AH.png` | Closing extent at عمر ؓ's death |

### 6.4 Interaction beats

- **`[HANDS] 1`** — before the ردة: *"hands up: how long did أبو بكر ؓ's whole caliphate last?"*
  Then the answer: **two years, three months.** Sets the "this is not a long time" frame.
- **`[HANDS] 2`** — before يرموك / قادسية: *"which two empires?"* Then the map.
- **`[HANDS] 3`** — before the close: *"what year are we in?"* — rehearses the timeline realignment.
- **Worksheet, 0:26, 90 seconds silent:** mark three places on the blank Arabia map; write the
  years into three of the six blank timeline boxes.

### 6.5 Research plan

Block A is done. Blocks B–E are the pass, run against the safe list only — البدایہ والنہایہ
(30097), سیر أعلام النبلاء (10906), الکامل (21712), الإعلان بالتوبيخ (34); الطبري (9783) for
corroboration only, never alone. Every page fetched gets a row in
`docs/catalogue/SHAMELA_LOG.md`; every note gets a row in `docs/research/INDEX.md` and is rendered
to PDF by `tools/render_note.py`.

---

## 7. New tooling

| Tool | Does |
|---|---|
| `tools/render_note.py` | research `.md` → A4 PDF, `Traditional Arabic` at readable size, live shamela links |
| `series/deckkit.py` (revised) | white-ground layouts, the four permitted slide kinds, the type-floor and word-count assertions |
| `series/make_visuals.py` (extended) | `line_sN_lit`, `map_sN_open`, `map_sN_close`, campaign maps |

---

## 8. Acceptance

Session 2 is done when:

- [ ] `CONTENT.md` holds ≥70 minutes of tiered, page-cited cards spanning 11–23 AH, each `CORE`
      card carrying a map move, an Arabic statement (or an explicit "none in our sources"), and an عبرت line.
- [ ] `SLIDES.md` has an `IMAGE BRIEF:` for every visual slide.
- [ ] `build.py` runs clean — meaning no slide violates the type floor or the 20-word rule, and no
      bullet-list slide exists.
- [ ] `CUE.pdf` is one page and contains no complete sentence.
- [ ] Both closing pairs (13 AH and 23 AH) are rendered.
- [ ] `WORKSHEET.pdf` prints the blank map and the blank timeline strip.
- [ ] Every research note has a PDF beside it and a row in `docs/research/INDEX.md`.
- [ ] Every Shamela page used has a row in `docs/catalogue/SHAMELA_LOG.md`.
- [ ] No artifact contains generated Urdu.
