# ACQUISITION — what to obtain, in what order, and what not to pay for

## Read this first: most of this needs no OCR at all

Two different problems are being conflated.

- **The Urdu volumes** (*Tareekh-e-Ummat*) are scanned books. These are the only things that might
  need OCR — **and both volumes we already hold came with a text layer already attached**, from the
  `t.me/pasbanehaq1` channel. Check the channel for the rest before paying anyone.
- **The Arabic classics are not a scanning problem.** Every major work below already exists as
  **typed digital text** in the Arabic scholarly digital libraries (al-Maktaba al-Shāmila and the
  like) — searchable, copyable, volume-and-page referenced. There is nothing to OCR. Downloading
  the typed edition takes minutes and costs nothing.

**Test any PDF before commissioning work on it:**

```bash
python -c "import fitz,sys; d=fitz.open(sys.argv[1]); print(sum(len((p.get_text() or '').strip()) for p in d),'chars of text in',d.page_count,'pages')" FILE.pdf
```

A few hundred characters per page means it is already text — run `tools/extract_source.py` on it and
you are done. Near zero means it is images, and only then is OCR the question.

---

## Tier 1 — blocking right now

| # | What | Unlocks | Urgency |
|---|---|---|---|
| 1 | **_Tareekh-e-Ummat_ vol. 1, the rest of خلافتِ راشدہ** — the ابوبکر ؓ chapter in full (ردہ، جمعُ القرآن، فدک), the عمر ؓ chapter (فتوحات، دیوان، تقویم), عثمان ؓ, علی ؓ | **Sessions 2 and 3** | **Blocking.** Session 2 is 14 days out |
| 2 | **_Tareekh-e-Ummat_, all remaining volumes** — confirm the volume count and what each covers from the publisher's own listing before assuming | Sessions 4–7, and possibly 8–9 | Within 3 weeks |

We currently hold printed pp. ۳۲–۷۸ (المقدمہ) and pp. ۴۵۶–۴۶۵ — a ten-page slice. That is all.

---

## Tier 2 — the Arabic spine · **you no longer need to acquire these**

**UPDATE 2026-08-26: `shamela.ws` is directly reachable from this machine**, and every work below
is in it, already typed and searchable. There is nothing to download, store or OCR — pages are
fetched on demand and cached:

```bash
python tools/shamela.py get 34 110       # الإعلان بالتوبيخ, the فوائد التاريخ chapter
python tools/shamela.py range 34 108 120 # a span
```

Already retrieved and cached: **book 34 = الإعلان بالتوبيخ لمن ذمّ أهل التاريخ (السخاوي)**, whose
**باب فوائد التاريخ begins at printed p.۱۱۱** — the chapter Rehan sahib draws his whole فوائد list
from. The course epigraph now comes from it in the original Arabic (see `IBRAH.md`).

So this tier is a **lookup list, not a shopping list.** Book ids get recorded here as they are found.

**Why this matters:** Arabic quotation carries authority in the room in a way an Urdu paraphrase
does not. Every work below is one the muqaddima *itself* names and relies on, so quoting them is
staying inside the course's own frame, not going outside it.

**Highest value, in order:**

| Work | Author | Why this one |
|---|---|---|
| **الإعلان بالتوبيخ لمن ذمّ أهل التاريخ** | السخاوي | **The highest-value single acquisition.** This is the book Rehan sahib quotes throughout pp.۵۱–۵۶ for the فوائد, the fiqh grading, and the historian's conditions. Owning it gives the **Arabic originals of the exact quotations the course already uses** |
| **مقدمة ابن خلدون** | ابن خلدون | The classical treatment of why civilisations rise and fall — precisely the "civilizational lessons" material, from an authority, so no conclusion has to be ours |
| **البداية والنهاية** | ابن كثير | The muqaddima's own recommendation as the soundest readable narrative history. **The natural second spine wherever _Tareekh-e-Ummat_ runs out** |
| **سير أعلام النبلاء** | الذهبي | The model for the تعارف format we adopted — biographical notices with dates and one defining incident. Sessions 2–7 draw their profiles from here |

**Get these as the course reaches them:**

| Work | Author | Used for |
|---|---|---|
| الكامل في التاريخ | ابن الأثير | Year-by-year narrative, sessions 4–6 |
| تاريخ الإسلام | الذهبي | The most carefully sifted of the large histories |
| تاريخ الرسل والملوك (تاريخ الطبري) | الطبري | The raw well — everything with its chain. **Use with the muqaddima's own caution: presence in Ṭabarī is not authenticity** |
| الإصابة في تمييز الصحابة | ابن حجر | Companion biographies, sessions 2–3 |
| الاستيعاب · أسد الغابة | ابن عبد البر · ابن الأثير | Companion biographies, corroboration |
| لسان الميزان | ابن حجر | Holds the Shāfiʿī wine-cup refutation the muqaddima cites (p.۵۷) |
| تاريخ بغداد | الخطيب البغدادي | The scholar behind the forged-Khaybar-document episode (p.۵۸) |
| الطبقات الكبرى | ابن سعد | Sessions 2–3 |
| فتوح البلدان | البلاذري | The conquests city by city, session 2 |
| المنتظم · مرآة الزمان | ابن الجوزي · سبط ابن الجوزي | The two works the muqaddima calls overlooked |

**Death-dates:** the muqaddima carries its own list of these at pp.۶۷–۷۸. Take every date from
there before it appears on a slide. Do not take a death-date from memory or from a website.

---

## Tier 3 — the South Asia gap (sessions 8 and 9)

*Tareekh-e-Ummat*'s coverage of the subcontinent is unconfirmed. **Check this first** — if Rehan
sahib covers it, the course keeps one spine and nothing else is needed.

If he does not, one named Sunni work is chosen and stated openly to the audience. Candidates worth
checking, in order:

| Work | Author | Covers | Check |
|---|---|---|---|
| **تاریخ اسلام** | اکبر شاہ خان نجیب آبادی | A standard Urdu general history; its later volume treats India | Confirm the volume and its coverage |
| **تاریخ دعوت و عزیمت** | سید ابو الحسن علی ندوی | The reformers — شاہ ولی اللہ, سرہندی and after. Fits session 9 exactly | Confirm which volumes |
| **حجة الله البالغة** | شاہ ولی اللہ | Session 9's central figure in his own words (Arabic) | Optional but strong |

The final choice should be run past a scholar you trust before it is named to the audience.

---

## Tier 4 — verification, not reading

For checking āyah and hadith references before they reach a slide: a reliable muṣḥaf reference, and
صحیح البخاری / صحیح مسلم in a numbered edition. Two references in `IBRAH.md` are already waiting on
this — the سنن ابن ماجہ number for «إِذَا لَمْ تَسْتَحْيِ فَاصْنَعْ مَا شِئْتَ», and the البخاری chapter for
the hadith of the nations before us. **Both are currently marked "verify" and neither may be quoted
with a number until checked.**

---

## Order of work

1. Check `t.me/pasbanehaq1` for the remaining *Tareekh-e-Ummat* volumes → run the text test above
2. Download the four Tier-2 priority works as typed Arabic text
3. Confirm whether *Tareekh-e-Ummat* reaches South Asia; if not, decide Tier 3
4. Only then consider paying for OCR — and only for Urdu volumes that fail the text test
