# RESEARCH INDEX — grep this before researching anything

**The rule (standing instruction, `docs/DECISIONS.md` #18):**

> **Before starting any research pass, grep this index. If a note already answers your question,
> read it and build on it. Only re-derive the parts that are genuinely stale or out of scope.**
> After any substantial pass, write a note here. Never leave findings only in a chat transcript.

Notes in this directory are **committed to the repo**. They are a course asset, not scratch — they
must survive a machine change, and they are what stops two artifacts disagreeing about a date.

---

## What a research note must contain

1. **The question** it was written to answer.
2. **The findings**, each carrying its **PRINTED page** (`ج5 ص246`, or `muqaddima p.۵۷`) — never a
   Shamela index, never a PDF page.
3. **Verbatim Arabic** exactly as fetched, wherever the source supplies it and a slide will use it.
4. **What could not be established**, and why. A stated gap is worth more than a confident guess.
5. **Which Shamela indices were fetched**, so the next session can read them off the cache for free.

## The absolute rule these notes exist to protect

Never fabricate a citation, date, title, hadith number, page or URL. **Wrong is worse than absent.**
If uncertain, write `(to verify)`. A note that says "could not establish" has done its job.

---

## The notes

| Note | Answers | For | Verified |
|---|---|---|---|
| `saqifah-bani-saida.md` | The full sequence of سقيفة بني ساعدة, who spoke and what each said, verbatim, from البدایہ | L01 | adversarial |
| `medina-ansar-structure.md` | الأوس / الخزرج, their sub-clans, the twelve نقباء, who led what at ۱۱ھ, يوم بُعاث | L01 | — |
| `muhajirun-quraysh-structure.md` | The بطون of قريش, which Companion belonged to each, السابقون vs الطلقاء | L01 | — |
| `suhayl-ibn-amr.md` | سهيل بن عمرو ؓ — the teeth incident at بدر, and the speech that held Mecca at ۱۱ھ | L01 | adversarial |
| `governors-at-11h.md` | The عمّال region by region at the Prophet's ﷺ death; جيش أسامہ ؓ; territorial extent | L01, L02 | — |
| `wafat-and-medina-11h.md` | The death of the Prophet ﷺ, عمر ؓ's reaction, أبو بكر ؓ's خطبة and آل عمران ۱۴۴ | L01 | adversarial |
| `tarikh-definition-and-the-guardrail.md` | What تاریخ is (السخاوي's own Arabic); حدیث/تاریخ/فقہ; the fiqh of the مشاجرات; تاریخِ اسلام = تاریخِ مسلمین; the forged Khaybar document | L01, L03 | — |
| `timeline-pegs.md` | Dated pegs for all three nested timelines, each with a certainty label | L01, all | — |
| `arabian-tribes-and-the-ridda-setup.md` | The tribal map of Arabia; عدنان vs قحطان; Ibn Kathīr's own four categories of the ردة; the four claimants; who did **not** break away; gazetteer; audit of the two existing ردة artifacts | **L02** | — |
| `saqifah-people-profiles.md` | Page-cited profiles of every man who spoke or was named at سقيفة | L01 | — |

*(Both strands previously listed here as "not written" completed on 2026-09-05 and are now rows in the table above.)*

**Certainty labels used across these notes:**

| Label | Meaning |
|---|---|
| `[SOURCED]` | Traceable to a page actually fetched and read. The page is given. |
| `[STANDARD]` | A universally agreed conventional date, not yet page-cited **in this repo**. Carries `(to verify)` and must be checked before it is printed. |
| `[CONVENTIONAL-ESTIMATE]` | An approximation from general scholarship that our Islamic sources **do not fix**. Must be labelled as such **on the slide itself**. |

---

## Where the *durable* facts live instead

Research notes are the **working record**. Once a fact is settled it is promoted into the catalogue,
and **the catalogue is what artifacts read from**:

| Fact type | Promote it to |
|---|---|
| A date | `docs/catalogue/TIMELINE.md` |
| A person, a لقب, a واقعہ | `docs/catalogue/PEOPLE.md` |
| A Shamela page used | `docs/catalogue/SHAMELA_LOG.md` |
| A hostile question and its safe answer | `docs/catalogue/QA_BANK.md` |
| A سبق line | `docs/catalogue/LESSONS.md` |
| A map asset | `docs/catalogue/MAPS.md` |
| A «کیسے پتا چلا؟» item | `docs/catalogue/HOWWEKNOW.md` |

**Never let two artifacts disagree.** A date, a لقب or a page number goes into `docs/catalogue/`
first; every artifact reads it from there.
