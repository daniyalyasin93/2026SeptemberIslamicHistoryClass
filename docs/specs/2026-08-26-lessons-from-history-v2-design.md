# «تاریخ سے سبق» — Series Design v2

**Author:** Daniyal · **Written:** 2026-08-26 · **First session:** 2026-09-02
**Supersedes:** `docs/specs/2026-06-03-lessons-from-history-design.md`
**Source text:** *Tareekh-e-Ummat*, Maulana Muhammad Ismail Rehan

---

## 1. Objective

> A 10-session adult lecture series that gives non-specialists a **usable mental map of Islamic
> history**: where events happened, in what order, how we know them, and what civilizational
> lessons follow.

Success is not "they enjoyed it." Success is: **a year later, a person who attended can place an
event on a timeline and point at a map**, name a handful of figures with one true incident each,
and knows to ask "کس نے کہا؟" before believing a historical claim.

## 2. Why v1 was replaced

v1 was diagnosed as theory-heavy. The specific failures:

| v1 | Problem |
|---|---|
| Session 1 = the whole muqaddima, 22 slides of historiography | The opening evening decides whether a voluntary audience returns, and it contained no events |
| Method taught as a subject | "How we know" is the *third* clause of the objective, but got the *first* session and 20% of the series |
| 7 of 11 sessions on the first 100 years | Left 1300 years to two sessions; a "mental map" of Islamic history cannot end at 100 AH |
| Nothing on Muslim South Asia | The audience is Pakistani; the series never reached them |
| No audience artifacts | Retention rested entirely on listening. Nothing was carried home, nothing was written by hand |
| No learner track for the speaker | The speaker has no formal history training and nothing in the repo addressed that |
| No versioning, no `CLAUDE.md`, no catalogue | Every session re-derived context from scratch |

**Kept from v1** (moved to `archive/`, harvested not discarded): the three «کیسے پتا چلا؟» stories,
the Urdu speaking voice in the scripts, the map tooling in `tools/`, the timeline-banner idea, and
the two Ridda HTML teaching artifacts — which now belong to session 2.

## 3. Decisions taken (with rationale)

| Decision | Chosen | Why |
|---|---|---|
| Series shape | **Whole arc first, then zoom** | Session 1 gives the complete shape, so every later session has somewhere to hang. Also the most dramatic evening available, which fixes the v1 opening problem |
| Arc weighting | **Balanced sweep, compressed to reach 1947** | The objective demands the full length; ʿibrah requires seeing a civilisation both rise *and* fall |
| Compression | **Rāshidūn 3→2 sessions AND Abbasids+Andalus merged** | Buys a tenth evening for consolidation — the strongest available retention device, and the easiest session to deliver |
| Method delivery | **3 minutes weekly, never a lecture** | The whole muqaddima still gets taught; it arrives in the week each piece is actually needed |
| Audience artifact | **One stapled A4 workbook** | Ownership drives return attendance; hand-writing drives retention |
| Printable language | **Bilingual, split by job** | English for structure/geography (typesets cleanly, scans fast); Urdu script for everything human |
| Sourcing | **Just-in-time per session** | OCR costs money; the architecture must not depend on holding all volumes now |
| Register | **Dignified, classical تراجم format** | Mature audience; entertainment framing is disrespectful applied to the Sahaba ؓ |

## 4. The retention system

Two objects the audience physically holds; three rituals that happen every week. Content changes
weekly; the furniture never does.

### 4.1 The two objects

**THE LINE** — one A4 landscape timeline with 8 fixed pegs (۱۱ھ → ۱۹۴۷). Every attendee marks
tonight's session on it **in their own handwriting**, every week, ten times. The physical act is
what installs the timeline — not the narration. A long printed banner of the same line hangs
behind the speaker and is extended with a marker each week.

**THE MAP** — one base map, same projection, same six anchor cities (مکہ · مدینہ · دمشق · بغداد ·
قرطبہ · قسطنطنیہ), every week. Each session adds one arrow or one shaded region. The workbook
version is deliberately **half-blank so it is drawn by hand**; self-drawn maps are remembered,
printed ones are not.

### 4.2 The three weekly rituals

- **«تعارف» (7 min)** — exactly three people, never more. Classical تراجم notice format:
  `نام و نسب` with the لقب the tradition gave · `سنین` · what they did in one sentence ·
  **`ایک واقعہ`**, one authentic incident from the source. The workbook prints the first three
  lines and leaves «ایک واقعہ» blank for the listener to write.
- **«کیسے پتا چلا؟» (3 min)** — one piece of the muqaddima per week, in the week it is needed.
- **«آج کا سبق» (4 min)** — one sentence of عبرت, written down by the listener. Ten sentences by
  the end, in their own hand, forms the civilizational spine.

### 4.3 The fixed 45-minute shape

```
0:00  آغاز / re-anchor     3   The Line and the Map go up. "Last week here → tonight here."
0:03  Opening scene        5   A scene. Never a definition.
0:08  The story           20   The narrative, with the map moving as it goes.
0:28  تعارف                7   Three people.
0:35  کیسے پتا چلا؟         3
0:38  آج کا سبق            4   Everyone writes.
0:42  اگلے ہفتے            3   End on a question.
```

Two side effects, both deliberate: the re-anchor ritual catches **drop-ins in 3 minutes** because
it is physical rather than a verbal recap; and the unchanging shape means the speaker always knows
where he is — if he blanks during the story, he moves to تعارف.

## 5. The arc

Dates below are standard anchors, **not citations**. Each is checked against the relevant volume at
build time and page-cited there. Where the source differs, the source wins.

| # | Session | «تعارف» — three people | Map movement | The سبق |
|---|---|---|---|---|
| 1 | **«ایک نظر میں — پورا نقشہ»** ۱۱ھ→۱۹۴۷ | عمر الفاروق ؓ · ہلاکو خان · سلطان محمد فاتح | The whole basin; six anchor cities placed | A civilisation is not a straight line — it rises, breaks and comes back. Knowing where you stand on it is the first defence |
| 2 | **«بارہ سال»** ۱۱–۲۳ھ | ابوبکر الصدیق ؓ · خالد بن الولید ؓ *سیف اللہ المسلول* · ابو عبیدہ بن الجراح ؓ *امین الامۃ* | مدینہ threatened → Arabia held → یرموک · قادسیہ · مصر | An institution survives its founder only when someone will stand alone for it |
| 3 | **«پہلا امتحان»** ۲۳–۴۰ھ | عثمان ذو النورین ؓ · علی ؓ · معاویہ ؓ | کوفہ · بصرہ · فسطاط · دمشق become the new centres | **The guardrail:** تاریخِ اسلام = تاریخِ مسلمین, and the fiqh — studying the مشاجرات without need is مکروہ |
| 4 | **«خلافت سے بادشاہت تک»** ۴۰–۱۳۲ھ | حسن بن علی ؓ *عام الجماعۃ* · عمر بن عبد العزیز رحمہ اللہ · محمد بن قاسم | Widest extent — سندھ and Spain in the same decade, ۹۲–۹۳ھ | How a consultative office becomes a hereditary throne, and what is lost |
| 5 | **«دو دارالحکومت»** ۱۳۲–۸۹۷ھ | ہارون الرشید · امام احمد بن حنبل رحمہ اللہ · عبد الرحمن الداخل | Baghdad and Córdoba, the same century — then both endings | A civilisation is measured by what it reads, and by whether its scholars can say no to its rulers |
| 6 | **«قریبِ مرگ»** ۴۹۲–۶۵۸ھ | صلاح الدین ایوبی رحمہ اللہ · ہلاکو خان · الظاہر بیبرس | The Levant, then the Mongol sweep; بغداد ۶۵۶; Cairo becomes the refuge | A civilisation can lose its capital and survive — if it keeps its books and its scholars |
| 7 | **«آخری خلافت»** ۶۹۹–۱۳۴۲ھ | سلطان محمد فاتح · سلطان سلیمان · سلطان عبد الحمید ثانی | Anatolia → قسطنطنیہ ۸۵۷ → Vienna → the long retreat → ۱۹۲۴ | Length is not health. A state can outlive every rival and still hollow out |
| 8 | **«یہ ہم تک کیسے پہنچا»** ۹۳–۱۱۱۹ھ | *(to be set from source)* | سندھ → غزنوی و غوری → سلطنتِ دہلی → مغل | *(to be set)* |
| 9 | **«۱۸۵۷ سے ۱۹۴۷ تک»** | شاہ ولی اللہ رحمہ اللہ · *(two more, to be set)* | The subcontinent; ۱۸۵۷; ۱۹۴۷ | *(to be set)* |
| 10 | **«سب کچھ جوڑ کر»** | The three historians they should now go read | The completed map goes back up | The ten سبق, collected and read aloud together |

### The weekly «کیسے پتا چلا؟» rotation

| Week | The 3 minutes | Source anchor |
|---|---|---|
| 1 | Why dates are the first question — سفیان ثوری: «جب راوی جھوٹی روایات گھڑنے لگے تو ہم نے تاریخ سے کام لیا» | muqaddima **p.۵۷** ✅ verified |
| 2 | How the Qurʾān was gathered after یمامہ | Abu Bakr extract, pp.۴۵۶–۴۶۵ (locate) |
| 3 | **The forged Khaybar document** — الخطیب بغدادی kills it on dates | muqaddima **p.۵۸** ✅ verified |
| 4 | Why we grade narrators — أسماء الرجال; why even واقدی is dropped | muqaddima p.۴۳–۴۵ |
| 5 | The five mother-books, and the two Ṭabarīs | muqaddima p.۶۹–۷۸ |
| 6 | What actually survived ۶۵۶ | *(needs a later volume)* |
| 7 | How to read a number in a chronicle sceptically | *(to source)* |
| 8 | روایہ vs درایہ — chain plus reason | muqaddima p.۶۳–۶۴ |
| 9 | Reading history "خلاف اصول" and what it does to a reader | muqaddima **p.۵۸–۶۰** ✅ verified |
| 10 | Where you go next, and how to check what you read | muqaddima p.۶۹–۷۸ |

Spare, if one is cut: the Shāfiʿī wine cup (muqaddima **p.۵۷** ✅ verified), the Hijri calendar
«کس سال کا شعبان؟» (p.۳۶–۳۷), النسیء (p.۳۸–۴۰).

## 6. Artifacts — three tracks

### Track ۱ — what the audience takes home

**THE WORKBOOK** — one stapled A4 booklet, ~28 pages, printed in **two halves** (Part 1 at
session 1, Part 2 at session 6) to match just-in-time sourcing.

| Pages | Contents |
|---|---|
| 1 | Cover — «یہ کتاب ______ کی ہے» |
| 2–3 | **THE LINE** — full-spread, 8 pegs printed, the rest blank. Written on every week |
| 4–5 | **THE MAP** — full-spread base map, six anchor cities, otherwise empty |
| 6–25 | Two pages per session ×10. Left = that week's **map worksheet**. Right = three تعارف panels (first three lines printed, «ایک واقعہ» blank) + «آج کا سبق: ______» |
| 26 | The ten سبق, collected in their own handwriting |

Companions: a weekly single-sheet **catch-up page** for drop-ins (the Line + Map + "you are here"
+ one line per session so far), and a bound **«تعارف نامہ»** — all thirty profiles as a reference
booklet — handed out at session 10.

### Track ۲ — what the speaker studies beforehand

- **`docs/PRIMER.md`** — the whole 1400 years for the teacher, ~25 A4 pages, read once before
  session 1. Sourced claims are page-cited; general orientation is explicitly flagged as such.
- **`LNN/BRIEFING.md`** — per session, 3–5× the material that will be used, every claim page-cited.
- **`LNN/DRILL.md`** — 15 self-test questions with answers. Confidence against stage fright comes
  from being tested, not from re-reading.
- **`docs/catalogue/QA_BANK.md`** — pre-written safe Sunni answers to hostile and sensitive
  questions, growing all term.

### Track ۳ — what the speaker holds while speaking

Light `.pptx`; full Urdu script with timings, `[ASK]` prompts and `EXTRA` blocks; a one-page A4
lectern cue card.

### Production

| Artifact | Pipeline |
|---|---|
| Workbook, cue card, تعارف نامہ, catch-up sheet | **HTML + CSS → headless Chrome → A4 PDF**, fonts base64-embedded via `@font-face` so a print shop renders it identically |
| Slides | **python-pptx**, 16:9 |
| Maps | One hand-built **schematic SVG** base, per-session variants by toggling layers. Deliberately simplified — metro-map logic beats geographic accuracy for memory. K&G video frames remain for slide drama |

## 7. Reference discipline

The mechanism, not the aspiration:

1. Every source PDF is extracted by `tools/extract_source.py` into `sources/text/*.txt` with
   `===== PDF p.N | PRINTED p.M =====` markers.
2. Every citation names the **PRINTED** page — the number in the physical book.
3. Any claim in any artifact must be greppable to a printed page, or carry `(to verify)`.
4. **OCR caveat:** the text layer garbles ligatures and honorifics. It is reliable for *locating*
   a passage; **verbatim quotations must be read off the page image before use.** Locate by grep,
   quote by eye.

Verified so far: forged Khaybar document → **printed p.۵۸**; سفیان ثوری quote, حفص بن غیاث, حماد بن
زید, and the Shāfiʿī wine-cup refutation → **printed p.۵۷**.

## 8. Build plan — seven days to session 1

| Day | Work | Gate |
|---|---|---|
| Wed 26 Aug | Phase 0: git, `CLAUDE.md`, catalogue skeleton, source extraction, this spec | ✅ |
| Thu 27 Aug | `docs/PRIMER.md` — **delivered early so there are five days to absorb it** · the Line · the base map SVG | Daniyal starts reading |
| Fri 28 Aug | Session 1: `BRIEFING.md` → script → deck | |
| Sat 29 Aug | Session 1 cue card, `DRILL.md`, `QA_BANK.md` seed · **week-1 handout to print** | to the printer |
| Sun 30 Aug | Rehearsal pass; revise from what actually breaks when said aloud | |
| Mon 1 Sep | Buffer; wall banner | |
| **Tue/Wed 2 Sep** | **Session 1 delivered** | |

**Week-1 print is not the full workbook.** A single A3 folded to A4 — cover · the Line spread ·
the Map spread · session 1 page — is the workbook's first signature and is printable in a day.
The full Part 1 follows by session 3 and the first sheet tucks inside it. This de-risks the
seven-day window.

After session 1, each subsequent session runs the same loop, gated on its source:
**obtain volume → extract → research note → briefing → script → deck → printables.**

## 9. Open decisions

| # | Decision | When |
|---|---|---|
| 1 | **Karbala** — depth and framing in session 4. Needs its own conversation | before session 4 is written |
| 2 | Sessions 8–9 (South Asia) — the three people and the سبق for each | needs a South Asia source; Tareekh-e-Ummat's coverage to be checked |
| 3 | Which volumes to obtain, in what order, and whether the `t.me` channel already carries them **with a text layer** (would remove the OCR cost entirely) | before session 4 |
| 4 | Headcount, for print quantities | before Sat 29 Aug |
| 5 | Day of week — memory says Tuesday, 2 Sep 2026 is a Wednesday | confirm |

## 10. Risks

| Risk | Mitigation |
|---|---|
| **Seven days is tight** | Session 1 needs no new sources — it is the overview, built on the muqaddima we already hold and standard anchors. Week-1 print reduced to a 4-page signature |
| **Sources for sessions 5–9 don't exist in the repo** | Just-in-time acquisition, one session ahead; each session gated on its own source checkpoint |
| **OCR garbling produces a wrong quotation** | Locate by grep, quote by eye — mandatory, recorded in `CLAUDE.md` |
| **A sensitive question from the floor** | `QA_BANK.md` written *before* each session; guardrail installed in session 3; never improvise a position on the مشاجرات |
| **Speaker blanks** | Fixed session shape; every block independently rehearsable; ~2× material; one-page cue card |
| **Attendance churn** | 3-minute physical re-anchor each week; weekly catch-up sheet for drop-ins |
