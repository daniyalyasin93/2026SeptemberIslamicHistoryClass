# SHAMELA LOG — every Arabic page used, and what it was used for

Running register. **Nothing from Shamela enters an artifact without a line in this table.**
Fetch: `python tools/shamela.py get <book> <index>` · Locate: `python tools/shamela.py toc <book> --find "<text>"`
All pages cached under `sources/shamela/<book>/<index>.txt` — the cache header records the URL,
the volume-and-printed-page, and the chapter, so any citation can be re-checked offline.

> ⚠ **Cite the volume and printed page** (`ج۷ ص۱۳۴`), never the Shamela index. The index is an
> internal sequential number and means nothing to a reader holding the book.

## Approved sources — the safe list

Stay inside this list for general narrative. All of them are named and relied on by the course's own
مقدمہ, so using them is staying inside the course's frame rather than stepping outside it.

| id | Work | Standing |
|---|---|---|
| **30097** | البدایہ والنہایہ — ابن کثیر رحمہ اللہ (ط دار ابن كثير) | ✅ Primary Arabic narrative. The مقدمہ's own recommendation — reason applied alongside chains |
| **10906** | سیر أعلام النبلاء — الذہبی رحمہ اللہ (ط الرسالة) | ✅ Primary for تعارف profiles. The most carefully sifted of the biographical works |
| **21712** | الکامل فی التاریخ — ابن الاثیر رحمہ اللہ | ✅ For sequence and year-by-year corroboration |
| **34** | الإعلان بالتوبيخ — السخاوی رحمہ اللہ | ✅ For the فوائد and the value of history |
| 9783 | تاریخ الطبری | ⚠️ **Corroboration only, never alone.** The raw well — collects with chains and does not sift. Presence in طبری is not authenticity; the مقدمہ devotes p.۷۱ to this. **Never** for anything touching the مشاجرات |

**Not to be used** without a specific decision: works of contested attribution, and anything the
مقدمہ flags for sectarian lean (it names یعقوبی and مسعودی at p.۴۶).

---

## Pages fetched

### Session 2 — «بارہ سال» (۱۱–۲۳ھ)

| Book | Volume & page | Chapter | Used for | Status |
|---|---|---|---|---|
| البدایہ 30097 | **ج۵ ص۳۴۴–۳۴۹** | قصة سقيفة بني ساعدة · ذكر اعتراف سعد بن عبادة | The succession, block 1 of the story | cached |
| البدایہ 30097 | **ج۷ ص۱۷–۲۷** | فصل في تصدي الصديق لقتال أهل الردة ومانعي الزكاة · خروجه إلى ذي القصة · مسيرة الأمراء | The ردہ, and سیدنا ابوبکر ؓ standing alone | cached |
| البدایہ 30097 | **ج۷ ص۸۵–۹۵** | وقعة اليرموك | Byzantium loses Syria | cached |
| البدایہ 30097 | **ج۷ ص۱۳۲–۱۴۰** | فصل في غزوة القادسية · رستم والمغيرة بن شعبة · **رستم وربعي بن عامر** | Persia; the envoy's exchange | cached |
| سیر 10906 | **راشدون ص۷–۱۲** | أبو بكر الصديق خليفة رسول الله ﷺ | تعارف panel ۱ | cached |
| سیر 10906 | **ج۱ ص۵–۱۰** | أبو عبيدة بن الجراح عامر بن عبد الله | تعارف panel ۳ | cached |
| سیر 10906 | **ج۱ ص۳۶۶–۳۷۱** | خالد بن الوليد المخزومي | تعارف panel ۲ | cached |

### Session 1

| Book | Volume & page | Chapter | Used for | Status |
|---|---|---|---|---|
| الإعلان 34 | **ص۱۱۱** | فوائد التاريخ | The course epigraph, on the title slide | ✅ **in use** |

---

## Verified findings worth reusing

**The القاب are confirmed, not assumed.** الذہبی records both:

- سیدنا ابو عبیدہ ؓ — «شَهِدَ لَهُ النَّبِيُّ ﷺ بِالجَنَّةِ، وَسَمَّاهُ: **أَمِيْنَ الأُمَّةِ**» — سیر، ج۱ ص۶
- سیدنا خالد بن الولید ؓ — «وَسَمَّاهُ النَّبِيُّ ﷺ: **سَيْفَ اللهِ**» — سیر، ج۱ ص۳۶۶

**The سقيفة → ابو عبیدہ ؓ link.** الذہبی notes he was among those put forward at السقيفة
«لِكَمَالِ أَهْلِيَّتِهِ عِنْدَ أَبِي بَكْرٍ» (ج۱ ص۶) — which ties the تعارف panel directly to the
evening's opening block instead of standing apart from it.

**The القادسية exchange** — البدایہ ج۷ ص۱۳۴, the envoy answering رستم:

> <div dir="rtl">وَإِخْرَاجُ الْعِبَادِ مِنْ عِبَادَةِ الْعِبَادِ إِلَى عِبَادَةِ اللهِ … وَالنَّاسُ بَنُو آدَمَ، فَهُمْ إِخْوَةٌ لِأَبٍ وَأُمٍّ</div>

Short, authentic, in ابن کثیر, and it carries the whole point of the evening without any comment
from the speaker.
