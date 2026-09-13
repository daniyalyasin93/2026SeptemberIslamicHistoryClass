# SOURCES — what we hold, what we still need

Single source of truth for citation. **Always cite the PRINTED page**, not the PDF page.
Extraction: `python tools/extract_source.py sources/pdf/<f>.pdf sources/text/<f>.txt`

## Held

| File | Work | PDF pages | **Printed pages** | Offset | Covers |
|---|---|---|---|---|---|
| `TUM_v1_muqaddima.pdf` | *Tareekh-e-Ummat*, vol. 1 — ⁨المقدمہ⁩ | 1–47 | **۳۲–۷۸** | +31 | The science of history: definition, calendar, ⁨نسیء⁩, the four stages, ⁨أسماء الرجال⁩, Islamic vs Western historiography, the fiqh of studying history, the great historians, the five mother-books |
| `TUM_v1_abubakr.pdf` | *Tareekh-e-Ummat*, vol. 1 — ⁨خلافتِ راشدہ⁩ opening | 1–10 | **۴۵۶–۴۶۵** | +455 | What ⁨خلافتِ راشدہ⁩ means; ⁨ابوبکر ؓ⁩ early life; the passing of ⁨سیدہ فاطمہ ؓ⁩ |

**This is a 10-page slice, not the Abu Bakr chapter.** Sessions 2 and 3 need the rest of vol. 1.

### OCR caveat (mandatory)

The text layer garbles ligatures and honorifics — «⁨حضور اکرم علی نیلم⁩» is ⁨صلی اللہ علیہ وسلم⁩,
«⁨رضی السنہ⁩» is ⁨رضی اللہ عنہ⁩. Reliable for **locating and page-anchoring**; **not** reliable for
wording. **Locate by grep, quote by eye** against the page image before any verbatim use.

## Verified anchors

| Claim | Printed page | Status |
|---|---|---|
| Forged Khaybar document; ⁨الخطیب بغدادی⁩'s two refutations (⁨معاویہ ؓ⁩ accepted Islam after Khaybar; ⁨سعد بن معاذ ؓ⁩ died at ⁨خندق⁩ before it) | **۵۸** | ✅ read in source |
| سفیان ثوری: «لما استعمل الرواة الكذب استعملناهم التاريخ» | **۵۷** | ✅ |
| حفص بن غیاث: «إذا اتهمتم فحاسبوه بالسنين» | **۵۷** | ✅ |
| حماد بن زید: «لم يستعن على الكذابين بمثل التاريخ» | **۵۷** | ✅ |
| Shāfiʿī wine-cup fabrication refuted by ⁨ابن حجر⁩ in ⁨لسان المیزان⁩ | **۵۷** | ✅ |
| Harms of reading history ⁨خلاف اصول⁩ | **۵۸–۶۰** | ✅ |
| Definition of ⁨تاریخ⁩; ⁨سخاوی⁩'s wording | **۳۲–۳۳** | ✅ |
| تاریخ ابن خلدون | **۷۷–۷۸** | ✅ |

## Needed, by session

| Session | Needs | Status |
|---|---|---|
| 1 «⁨ایک نظر میں⁩» | Nothing new — muqaddima + standard anchors | ✅ can build now |
| 2 «⁨بارہ سال⁩» | vol. 1 — ⁨ابوبکر ؓ⁩ chapter in full, ⁨ردہ⁩, ⁨جمعِ قرآن⁩, ⁨عمر ؓ⁩ chapter, ⁨فتوحات⁩ | ⬜ **needed first** |
| 3 «⁨پہلا امتحان⁩» | vol. 1 — ⁨عثمان ؓ⁩, ⁨علی ؓ⁩, ⁨مشاجرات⁩ | ⬜ |
| 4 «⁨خلافت سے بادشاہت تک⁩» | ⁨بنو امیہ⁩ volume | ⬜ |
| 5 «⁨دو دارالحکومت⁩» | ⁨عباسیہ⁩ + ⁨اندلس⁩ volume(s) | ⬜ |
| 6 «⁨قریبِ مرگ⁩» | ⁨صلیبی جنگیں⁩ + ⁨منگول⁩ volume | ⬜ |
| 7 «⁨آخری خلافت⁩» | ⁨عثمانیہ⁩ volume | ⬜ |
| 8 «⁨یہ ہم تک کیسے پہنچا⁩» | South Asia — check whether *Tareekh-e-Ummat* covers it; a named second Sunni source may be required | ⬜ **check coverage** |
| 9 «⁨۱۸۵۷ سے ۱۹۴۷ تک⁩» | as above | ⬜ |
| 10 «⁨سب کچھ جوڑ کر⁩» | Nothing new | ✅ |

## Acquisition note

Both held PDFs carry a `t.me/pasbanehaq1` header on every page and **already have a text layer**.
If the remaining volumes circulate from the same channel in the same form, **no paid OCR is
needed** — extraction is free. Check this before commissioning any OCR work.

## Second source

If *Tareekh-e-Ummat* does not reach a period, pick **one** named, reputable Sunni work and cite it
openly as the second spine rather than quietly mixing sources. Decision deferred until a gap is
actually hit — see `docs/specs/2026-08-26-lessons-from-history-v2-design.md` §9.
