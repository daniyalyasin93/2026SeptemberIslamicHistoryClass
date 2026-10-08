# SHAMELA LOG — every Arabic page used, and what it was used for
Running register. **Nothing from Shamela enters an artifact without a line in this table.**
Fetch: `python tools/shamela.py get <book> <index>` · Locate: `python tools/shamela.py toc <book> --find "<text>"`
All pages cached under `sources/shamela/<book>/<index>.txt` — the cache header records the URL,
the volume-and-printed-page, and the chapter, so any citation can be re-checked offline.
> ⚠ **Cite the volume and printed page** (`⁨ج۷ ص۱۳۴⁩`), never the Shamela index. The index is an
> internal sequential number and means nothing to a reader holding the book.
## Approved sources — the safe list
Stay inside this list for general narrative. All of them are named and relied on by the course's own
⁨مقدمہ⁩, so using them is staying inside the course's frame rather than stepping outside it.
| id | Work | Standing |
|---|---|---|
| **30097** | ⁨البدایہ والنہایہ⁩ — ⁨ابن کثیر رحمہ اللہ⁩ (⁨ط دار ابن كثير⁩) | ✅ Primary Arabic narrative. The ⁨مقدمہ⁩'s own recommendation — reason applied alongside chains |
| **10906** | ⁨سیر أعلام النبلاء⁩ — ⁨الذہبی رحمہ اللہ⁩ (⁨ط الرسالة⁩) | ✅ Primary for ⁨تعارف⁩ profiles. The most carefully sifted of the biographical works |
| **21712** | ⁨الکامل فی التاریخ⁩ — ⁨ابن الاثیر رحمہ اللہ⁩ | ✅ For sequence and year-by-year corroboration |
| **12320** | ⁨تاریخ ابن خلدون⁩ — ⁨كتاب العبر وديوان المبتدأ والخبر⁩ | ⚖ **Judgement and framing only** (`DECISIONS.md` #29). Never the sole authority for a date, name, number or wording — his early narrative follows ⁨الطبری⁩, so citing him alone for a fact is citing ⁨الطبری⁩ at one remove. Never for the ⁨مشاجرات⁩. Attribute by name when used |
| **34** | ⁨الإعلان بالتوبيخ⁩ — ⁨السخاوی رحمہ اللہ⁩ | ✅ For the ⁨فوائد⁩ and the value of history |
| 9783 | ⁨تاریخ الطبری⁩ | ⚠️ **Corroboration only, never alone.** The raw well — collects with chains and does not sift. Presence in ⁨طبری⁩ is not authenticity; the ⁨مقدمہ⁩ devotes p.۷۱ to this. **Never** for anything touching the ⁨مشاجرات⁩ |
**Not to be used** without a specific decision: works of contested attribution, and anything the
⁨مقدمہ⁩ flags for sectarian lean (it names ⁨یعقوبی⁩ and ⁨مسعودی⁩ at p.۴۶).
---
## Pages fetched
### Session 3 — «⁨پہلا امتحان⁩» (۲۳–⁨۴۰ھ⁩)
**1,569 pages fetched in one sweep on 2026-09-12** so the research pass read the whole window
off disk and a dropped connection could not strand it. Every page is under
`sources/shamela/<book>/<index>.txt` with its URL, volume and printed page in the header.
| Book | Volume & page | Chapter | Used for | Status |
|---|---|---|---|---|
| ⁨البدایہ⁩ 30097 | **⁨ج۷ ص۲۵۸⁩–۲۷۹** | ⁨آخر سنة ۲۳⁩ · ⁨وفاة عمر ؓ وصفته وزوجاته⁩ | The hinge out of session 2 | cached |
| ⁨البدایہ⁩ 30097 | **⁨ج۷ ص۲۸۰⁩–۲۸۶** | ⁨خلافة أمير المؤمنين عثمان بن عفان ؓ⁩, ⁨سنة ۲۴⁩ | The ⁨بيعة⁩, and the terms | cached |
| ⁨البدایہ⁩ 30097 | **⁨ج۷ ص۲۸۷⁩–۲۹۸** | ⁨سنوات ۲۵⁩–۳۱ · ⁨إفريقية⁩ · ⁨الأندلس⁩ · ⁨قبرص⁩ · ⁨مقتل يزدجرد⁩ | The conquests and the first fleet | cached |
| ⁨البدایہ⁩ 30097 | **⁨ج۷ ص۲۹۹⁩–۳۱۳** | ⁨سنوات ۳۲⁩–۳۴ · ⁨ذكر من توفي من الأعيان⁩ | The first complaints; the generation thins | cached |
| ⁨البدایہ⁩ 30097 | **⁨ج۷ ص۳۱۴⁩–۳۳۳** | ⁨سنة ۳۵⁩ · ⁨مجيء الأحزاب⁩ · ⁨ذكر حصر عثمان ؓ⁩ | The siege | cached |
| ⁨البدایہ⁩ 30097 | **⁨ج۷ ص۳۳۴⁩–۳۵۶** | ⁨صفة قتله ؓ⁩ · ⁨ما رثي به⁩ | The killing | cached |
| ⁨البدایہ⁩ 30097 | **⁨ج۷ ص۳۵۷⁩–۳۸۷** | ⁨فضائل عثمان ؓ⁩ · ⁨سيرته⁩ · ⁨خطبه⁩ · ⁨مناقبه⁩ · ⁨زوجاته⁩ | The man himself | cached |
| ⁨البدایہ⁩ 30097 | **⁨ج۷ ص۳۸۸⁩–۳۹۳** | ⁨من توفي في زمان دولة عثمان ؓ⁩ | The obituaries | cached |
| ⁨البدایہ⁩ 30097 | **⁨ج۷ ص۳۹۴⁩–۴۰۲** | ⁨خلافة أمير المؤمنين علي بن أبي طالب ؓ⁩ · ⁨ذكر بيعته⁩ | The ⁨بيعة⁩ of 35 AH | cached |
| ⁨البدایہ⁩ 30097 | **⁨ج۷ ص۴۰۳⁩–۴۳۵** | ⁨ابتداء وقعة الجمل⁩ · ⁨مسير علي ؓ إلى البصرة⁩ | ⁨الجمل⁩ | cached |
| ⁨البدایہ⁩ 30097 | **⁨ج۷ ص۴۳۶⁩–۴۶۳** | ⁨وقعة صفين⁩ · ⁨مقتل عمار بن ياسر ؓ⁩ | ⁨صفين⁩ | cached |
| ⁨البدایہ⁩ 30097 | **⁨ج۷ ص۴۶۴⁩–۴۸۸** | ⁨رفع المصاحف⁩ · ⁨قصة التحكيم⁩ · ⁨خروج الخوارج⁩ · ⁨اجتماع الحكمين⁩ | ⁨التحكيم⁩ and ⁨النهروان⁩ | cached |
| ⁨البدایہ⁩ 30097 | **⁨ج۷ ص۴۸۹⁩–۵۲۰** | ⁨ما ورد في الخوارج من الأحاديث الشريفة⁩ | The ⁨خوارج⁩ in the prophetic reports | cached |
| ⁨البدایہ⁩ 30097 | **⁨ج۷ ص۵۲۱⁩–۵۳۷** | ⁨سنتا ۳۸⁩–۳۹ · ⁨ذكر من توفي من الأعيان⁩ | ⁨مصر⁩, the raids, the fraying | cached |
| ⁨البدایہ⁩ 30097 | **⁨ج۷ ص۵۳۸⁩–۵۵۲** | ⁨سنة ۴۰⁩ · ⁨ذكر مقتل علي ؓ⁩ · ⁨صفة مقتله⁩ | The killing of ⁨علي ؓ⁩ | cached |
| ⁨البدایہ⁩ 30097 | **⁨ج۷ ص۵۵۳⁩–۵۹۵** | ⁨باب ذكر شيء من فضائل علي ؓ⁩ | The ⁨فضائل⁩, with ⁨ابن كثير⁩'s gradings | cached |
| ⁨البدایہ⁩ 30097 | **⁨ج۷ ص۵۹۶⁩–۶۱۴** | ⁨سيرته ومواعظه وقضاياه وخطبه⁩ · ⁨غريبة من الغرائب⁩ | His own words | cached |
| ⁨البدایہ⁩ 30097 | **⁨ج۷ ص۶۱۵⁩–۱** | ⁨خلافة الحسن بن علي ؓ⁩ | The handover | cached |
| ⁨البدایہ⁩ 30097 | **⁨ج۸ ص۵⁩–۲۱** | ⁨سنة ۴۱⁩ · ⁨أيام معاوية ؓ وملكه⁩ · ⁨فضله⁩ · ⁨خروج الخوارج عليه⁩ | ⁨عام الجماعة⁩ | cached |
| ⁨الکامل⁩ 21712 | **⁨ج۲ ص۴۵۳⁩–۵۲۵** | ⁨سنوات ۲۴⁩–۳۴, ⁨سنة بسنة⁩ | Year-by-year corroboration | cached |
| ⁨الکامل⁩ 21712 | **⁨ج۲ ص۵۲۶⁩–۵۵۳** | ⁨ذكر مسير من سار إلى حصر عثمان⁩ · ⁨ذكر مقتل عثمان⁩ · ⁨ذكر بعض سيرته⁩ | The siege and the killing | cached |
| ⁨الکامل⁩ 21712 | **⁨ج۲ ص۵۵۴⁩–۵۶۷** | ⁨ذكر بيعة أمير المؤمنين علي بن أبي طالب⁩ · ⁨تفريق عماله⁩ | The ⁨بيعة⁩ | cached |
| ⁨الکامل⁩ 21712 | **⁨ج۲ ص۵۶۸⁩–۶۲۷** | ⁨ذكر ابتداء وقعة الجمل⁩ | ⁨الجمل⁩ | cached |
| ⁨الکامل⁩ 21712 | **⁨ج۲ ص۶۲۸⁩–۷۰۳** | ⁨ذكر ابتداء وقعة صفين⁩ · ⁨تتمة أمر صفين⁩ | ⁨صفين⁩ and the arbitration | cached |
| ⁨الکامل⁩ 21712 | **⁨ج۲ ص۷۰۴⁩–۷۳۱** | ⁨سنتا ۳۸⁩–۳۹ | The raids and the risings | cached |
| ⁨الکامل⁩ 21712 | **⁨ج۲ ص۷۳۲⁩–۷۵۵** | ⁨سرية بسر بن أبي أرطاة⁩ · ⁨ذكر مقتل أمير المؤمنين علي⁩ | 40 AH | cached |
| ⁨الکامل⁩ 21712 | **⁨ج۳ ص۵⁩–۲۲** | ⁨سنة ۴۱ وما بعدها⁩ | ⁨عام الجماعة⁩ | cached |
| ⁨ابن خلدون⁩ 12320 | **⁨ج۲ ص۵۷۳⁩–۶** | ⁨أمر الجمل⁩ · ⁨أمر صفين⁩ · ⁨أمر الخوارج⁩ · ⁨مقتل علي⁩ · ⁨بيعة الحسن وتسليمه الأمر⁩ | ⚖ Framing only — DECISIONS #29 | cached |
| ⁨سیر⁩ 10906 | **⁨جراشدون ص۱۴۹⁩–۲۲۲** | ⁨سيرة ذي النورين عثمان ؓ⁩ | The man, and the killing | cached |
| ⁨سیر⁩ 10906 | **⁨جراشدون ص۲۲۵⁩–۲۹۰** | ⁨سيرة أبي الحسنين علي ؓ⁩ | The man, and the killing | cached |
| ⁨سیر⁩ 10906 | ⁨ج۱⁩–⁨ج۳⁩, various | The ⁨تراجم⁩ of 32 figures of the window — ⁨طلحة ؓ⁩ · ⁨الزبير ؓ⁩ · ⁨عائشة ؓ⁩ · ⁨عبد الرحمن بن عوف ؓ⁩ · ⁨سعد ؓ⁩ · ⁨عمار ؓ⁩ · ⁨أبو ذر ؓ⁩ · ⁨ابن مسعود ؓ⁩ · ⁨عمرو بن العاص ؓ⁩ · ⁨أبو موسى ؓ⁩ · ⁨المغيرة ؓ⁩ · ⁨الأشتر⁩ · ⁨محمد بن أبي بكر ؓ⁩ · ⁨هاشم بن عتبة ؓ⁩ · ⁨حجر بن عدي⁩ · ⁨صعصعة⁩ · ⁨جرير ؓ⁩ · ⁨الأشعث ؓ⁩ · ⁨حذيفة ؓ⁩ · ⁨قيس بن سعد ؓ⁩ · ⁨معاوية ؓ⁩ · ⁨الحسن ؓ⁩ · ⁨ابن عباس ؓ⁩ · ⁨مروان⁩ · ⁨الوليد بن عقبة ؓ⁩ · ⁨سعيد بن العاص ؓ⁩ · ⁨ابن عامر ؓ⁩ · ⁨كعب الأحبار⁩ · ⁨عدي بن حاتم ؓ⁩ · ⁨أم كلثوم ؓ⁩ · ⁨أبي بن كعب ؓ⁩ · ⁨عبيدة السلماني⁩ | The profiles register | cached |
### Session 2 — «⁨بارہ سال⁩» (۱۱–⁨۲۳ھ⁩)
| Book | Volume & page | Chapter | Used for | Status |
|---|---|---|---|---|
| ⁨البدایہ⁩ 30097 | **⁨ج۵ ص۳۴۴⁩–۳۴۹** | ⁨قصة سقيفة بني ساعدة⁩ · ⁨ذكر اعتراف سعد بن عبادة⁩ | The succession, block 1 of the story | cached |
| ⁨البدایہ⁩ 30097 | **⁨ج۷ ص۱۷⁩–۲۷** | ⁨فصل في تصدي الصديق لقتال أهل الردة ومانعي الزكاة⁩ · ⁨خروجه إلى ذي القصة⁩ · ⁨مسيرة الأمراء⁩ | The ⁨ردہ⁩, and ⁨سیدنا ابوبکر ؓ⁩ standing alone | cached |
| ⁨البدایہ⁩ 30097 | **⁨ج۷ ص۸۵⁩–۹۵** | ⁨وقعة اليرموك⁩ | Byzantium loses Syria | cached |
| ⁨البدایہ⁩ 30097 | **⁨ج۷ ص۱۳۲⁩–۱۴۰** | ⁨فصل في غزوة القادسية⁩ · ⁨رستم والمغيرة بن شعبة⁩ · **⁨رستم وربعي بن عامر⁩** | Persia; the envoy's exchange | cached |
| ⁨سیر⁩ 10906 | **⁨راشدون ص۷⁩–۱۲** | ⁨أبو بكر الصديق خليفة رسول الله ﷺ⁩ | ⁨تعارف⁩ panel ۱ | cached |
| ⁨سیر⁩ 10906 | **⁨ج۱ ص۵⁩–۱۰** | ⁨أبو عبيدة بن الجراح عامر بن عبد الله⁩ | ⁨تعارف⁩ panel ۳ | cached |
| ⁨سیر⁩ 10906 | **⁨ج۱ ص۳۶۶⁩–۳۷۱** | ⁨خالد بن الوليد المخزومي⁩ | ⁨تعارف⁩ panel ۲ | cached |
### Session 1
| Book | Volume & page | Chapter | Used for | Status |
|---|---|---|---|---|
| ⁨الإعلان⁩ 34 | **⁨ص۱۱۱⁩** | ⁨فوائد التاريخ⁩ | The course epigraph, on the title slide | ✅ **in use** |
### Strand — ⁨سهيل بن عمرو ؓ⁩, the man who held Mecca (research note: `docs/research/suhayl-ibn-amr.md`)
Belongs to session 2 «⁨بارہ سال⁩» — Mecca's ⁨۱۱ھ⁩, running alongside ⁨المدینہ⁩'s.
| Book | Volume & page | Chapter | Used for | Status |
|---|---|---|---|---|
| ⁨سیر⁩ 10906 | **⁨ج۱ ص۱۹۲⁩–۱۹۳** | ⁨أبو جندل⁩ · ⁨عبد الله بن سهيل⁩ | The two sons; ⁨طاعون عمواس ۱۸ھ⁩ | cached |
| ⁨سیر⁩ 10906 | **⁨ج۱ ص۱۹۴⁩–۱۹۵** | ٢٥ - ⁨سهيل بن عمرو⁩ | ⁨خطیب قریش⁩; Islam at ⁨الفتح⁩; the two death reports; **⁨الذہبی⁩'s «⁨فَهَذَا لاَ يَسْتَقِيْمُ⁩»** | cached |
| ⁨البدایہ⁩ 30097 | **⁨ج۴ ص۱۱۴⁩–۱۱۵** | ⁨فداء أسرى بدر⁩ | **The teeth incident**, ⁨ابن کثیر⁩'s wording + his «⁨مرسلٌ بل معضلٌ⁩» grading | cached |
| ⁨البدایہ⁩ 30097 | **⁨ج۴ ص۳۸۰⁩–۳۸۲** | ⁨غزوة الحديبية⁩ | His role as Quraysh's negotiator | cached |
| ⁨البدایہ⁩ 30097 | **⁨ج۵ ص۳۹۷⁩–۳۹۸** | ⁨فصل⁩ (⁨بعد وفاته ﷺ⁩) | **Mecca wavers · ⁨عتاب ؓ⁩ hides · ⁨سہیل ؓ⁩ stands** | cached |
| ⁨البدایہ⁩ 30097 | **⁨ج۷ ص۱۲۷⁩** | ⁨المتوفون سنة ۱۳ھ⁩ | ⁨عتاب بن أسيد ؓ⁩ — governor at 20, kept in post by ⁨ابوبکر ؓ⁩ | cached |
| ⁨البدایہ⁩ 30097 | **⁨ج۷ ص۱۶۵⁩–۱۶۷** | ⁨المتوفون سنة ۱۵ھ⁩ | His obituary; the ⁨الیرموک⁩-year dispute | cached |
| ⁨الکامل⁩ 21712 | **⁨ج۲ ص۲۴⁩–۲۵** | ⁨غزوة بدر الكبرى⁩ | **The teeth incident — «⁨دَعْهُ يَا عُمَرُ؛ فَسَيَقُومُ مَقَامًا تَحْمَدُهُ عَلَيْهِ⁩»** | cached |
| ⁨الکامل⁩ 21712 | **⁨ج۲ ص۸۴⁩** | ⁨عمرة الحديبية⁩ | «⁨سُهِّلَ أَمْرُكُمْ⁩» | cached |
| ⁨الکامل⁩ 21712 | **⁨ج۲ ص۱۸۶⁩** | ⁨مرض رسول الله ﷺ ووفاته⁩ | **The Mecca speech, verbatim — the only safe-list source that carries it** | cached |
⚠ The «⁨يَا أَهْلَ مَكَّةَ، لَا تَكُونُوا آخِرَ مَنْ أَسْلَمَ وَأَوَّلَ مَنِ ارْتَدَّ⁩» text is
**⁨ابن الاثیر⁩'s, ⁨ج۲ ص۱۸۶⁩** — ⁨البدایہ⁩ carries only the substance of that stand, in different words.
Never caption the ⁨الکامل⁩ wording to ⁨ابن کثیر⁩. See the research note for both, side by side.
---
### Evening 3 — Yemen, start to end (2026-09-13)
Three notes: `al-aswad-al-ansi-and-yemen-before-the-ridda` (A) · `the-second-yemen-ridda-and-kinda-11-12ah` (B) ·
`kinda-the-kingdom-before-islam-and-the-house-of-al-ashath` (C). 17 pages newly fetched; the rest were cached.
| Book | Printed page | Chapter | What it supports | |
|---|---|---|---|---|
| ⁨البدایہ⁩ 30097 | ⁨ج۲ ص۴۱۱⁩ | ⁨فصل⁩ (⁨سبأ⁩) | A: Sayf b. Dhī Yazan recovers Yemen before the Prophet's ﷺ birth | cached |
| ⁨البدایہ⁩ 30097 | ⁨ج۵ ص۲۲⁩ | ⁨قصة ثمامة ووفد بني حنيفة⁩ | A: «⁨العنسي الذي قتله فيروز باليمن⁩», editor-restored from al-Bukhārī | cached |
| ⁨البدایہ⁩ 30097 | ⁨ج۷ ص۱۱⁩–۱۷ | ⁨مقتل الأسود العنسي⁩ · ⁨خروجه⁩ | A: Abnāʾ, Bādhām, governors, rising, letters, widow, the night, adhān, Muʿādh | cached |
| ⁨البدایہ⁩ 30097 | ⁨ج۷ ص۱۹⁩, ⁨ص۲۳⁩ | ⁨تصدي الصديق⁩ / ⁨ذي القصة⁩ | B: Kinda under al-Ashʿath (Ibn Isḥāq); al-Muhājir's ؓ commission | cached |
| ⁨البدایہ⁩ 30097 | ⁨ج۷ ص۴۱⁩–۴۳ | ⁨ردة أهل عمان ومهرة واليمن⁩ | A/B: Qays's motive; the Abnāʾ footnote; the span of the wars | cached |
| ⁨البدایہ⁩ 30097 | ⁨ج۷ ص۵۹⁩ | ⁨من توفي في هذه السنة⁩ | A: a month to Ṣanʿāʾ, 3–4 months, «⁨بليال، وقيل بليلة⁩» | cached |
| ⁨البدایہ⁩ 30097 | ⁨ج۷ ص۶۱⁩ | ⁨سنة ۱۲⁩ (footnote) | C: editor quoting al-Qāmūs — the four kings came with al-Ashʿath | cached |
| ⁨البدایہ⁩ 30097 | ⁨ج۷ ص۱۳۳⁩, ⁨ص۱۳۹⁩, ⁨ص۲۲۹⁩, ⁨ص۲۴۳⁩–۲۴۴ | ⁨القادسية⁩ / ⁨نهاوند⁩ / ⁨سنة ۲۱⁩ | B/C: al-Ashʿath and ʿAmr to Rustam; the three men (Jābir, via Sayf) | cached |
| ⁨البدایہ⁩ 30097 | ⁨ج۲ ص۵۰۷⁩ | ⁨امرؤ القيس⁩ | C: the Muʿallaqa (the ḥadīth here is very weak — not usable) | fetched |
| ⁨البدایہ⁩ 30097 | ⁨ج۵ ص۵۶⁩, ⁨ص۸۹⁩ | ⁨وفد كندة⁩ | C: «⁨بنو آكل المرار⁩»; «⁨كانوا ملوكا⁩»; the reply; ten-odd riders | fetched |
| ⁨البدایہ⁩ 30097 | ⁨ج۹ ص۱۷۸⁩–۱۷۹, ⁨ص۱۸۶⁩–۱۸۷ | ⁨فتنة ابن الأشعث⁩ · ⁨دير الجماجم⁩ | C: disputed date; the break; Shaʿbān 82; ʿAbd al-Malik's offer refused | fetched |
| ⁨الکامل⁩ 21712 | ⁨ج۱ ص۴۶۱⁩–۴۶۴ | ⁨مقتل حجر أبي امرئ القيس⁩ | C: Ḥujr Ākil al-Murār; al-Ḥārith and al-Ḥīra; Ḥujr killed by Banū Asad | fetched |
| ⁨الکامل⁩ 21712 | ⁨ج۲ ص۱۹۶⁩–۲۰۱ | ⁨أخبار الأسود العنسي باليمن⁩ | A: the whole chapter; Jishnas's first-person account | cached |
| ⁨الکامل⁩ 21712 | ⁨ج۲ ص۲۲۶⁩–۲۳۳ | ⁨ردة اليمن⁩ (⁨ثانية⁩) · ⁨ردة حضرموت وكندة⁩ | B/C: Ṣanʿāʾ deportation; ʿAmr and Qays at Medina; Tabūk and Umm Salama ؓ; «⁨وابنه⁩» (Shuraḥbīl's son); the four kings; al-Nujayr | cached |
| ⁨سیر⁩ 10906 | ⁨الراشدون ص۱۷⁩–۱۸, ⁨ص۲۸⁩–۳۲, ⁨ص۵۵⁩, ⁨ص۶۱⁩–۶۲ | ⁨أبو بكر الصديق⁩ · ⁨قصة الأسود⁩ | A/B: Sayf's version; al-Wāqidī's other account; the regret report; al-Nujayr under 12 AH | cached |
| ⁨سیر⁩ 10906 | ⁨ج۲ ص۳۷⁩–۴۳ | ⁨الأشعث بن قيس⁩ | B/C: ⁨صحبة⁩; pardon and marriage; "seventy"; «⁨إني ارتددت⁩»; d. 40 AH | cached |
| ⁨سیر⁩ 10906 | ⁨ج۳ ص۵۲۰⁩–۵۲۱ | ⁨قيس بن مكشوح⁩ | B: his notice — no ridda mentioned; eye lost at al-Yarmūk | fetched |
| ⁨سیر⁩ 10906 | ⁨ج۴ ص۱۸۳⁩–۱۸۴ | ⁨ابن الأشعث⁩ | C: full name; the scholars with him; Rutbīl; d. 84 AH | fetched |
| ⁨ابن خلدون⁩ 12320 | ⁨ج۲ ص۳۲۷⁩; ⁨ج۲ ص۴۸۱⁩–۴۸۴, ⁨ص۴۹۱⁩–۴۹۴; ⁨ج۳ ص۶۱⁩ | ⁨ملوك كندة⁩ · ⁨خبر العنسي⁩ · ⁨ردة اليمن⁩ · ⁨ابن الأشعث⁩ | framing only: Ḥujr over Maʿadd; «⁨كاهنا مشعوذا⁩»; al-Muhājir's illness; «⁨جيش الطواويس⁩» (not usable alone) | cached / fetched |
## Verified findings worth reusing
**The ⁨القاب⁩ are confirmed, not assumed.** ⁨الذہبی⁩ records both:
- سیدنا ابو عبیدہ ؓ — «شَهِدَ لَهُ النَّبِيُّ ﷺ بِالجَنَّةِ، وَسَمَّاهُ: **أَمِيْنَ الأُمَّةِ**» — سیر، ج۱ ص۶
- سیدنا خالد بن الولید ؓ — «وَسَمَّاهُ النَّبِيُّ ﷺ: **سَيْفَ اللهِ**» — سیر، ج۱ ص۳۶۶
**The ⁨سقيفة⁩ → ⁨ابو عبیدہ ؓ⁩ link.** ⁨الذہبی⁩ notes he was among those put forward at ⁨السقيفة⁩
«⁨لِكَمَالِ أَهْلِيَّتِهِ عِنْدَ أَبِي بَكْرٍ⁩» (⁨ج۱ ص۶⁩) — which ties the ⁨تعارف⁩ panel directly to the
evening's opening block instead of standing apart from it.
**The ⁨القادسية⁩ exchange** — ⁨البدایہ ج۷ ص۱۳۴⁩, the envoy answering ⁨رستم⁩:
> <div dir="rtl">⁨وَإِخْرَاجُ الْعِبَادِ مِنْ عِبَادَةِ الْعِبَادِ إِلَى عِبَادَةِ اللهِ⁩ … ⁨وَالنَّاسُ بَنُو آدَمَ، فَهُمْ إِخْوَةٌ لِأَبٍ وَأُمٍّ⁩</div>
Short, authentic, in ⁨ابن کثیر⁩, and it carries the whole point of the evening without any comment
from the speaker.
## 2026-09-19 — evening 4 content review (`DECISIONS.md` #43)
| Book | Index | Printed | Why |
|---|---|---|---|
| ⁨سیر أعلام النبلاء⁩ 10906 | 1735 | ⁨ج۱ ص۳۰۹⁩ | ⁨ثابت بن قيس بن شماس ؓ⁩ — his ⁨تراجم⁩ notice, «⁨خَطِيْبُ الأَنْصَارِ⁩ … ⁨وَلَمْ يَشْهَدْ بَدْراً، شَهِدَ أُحُداً، وَبَيْعَةَ الرُّضْوَانِ⁩». `RCT/E-RC18` |
| ⁨سیر أعلام النبلاء⁩ 10906 | 2429 | ⁨ج۲ ص۴۴۹⁩ | ⁨أبو قتادة الأنصاري ؓ⁩ — «⁨فَارِسُ رَسُوْلِ اللهِ ﷺ⁩ ⁨شَهِدَ أُحُداً وَالحُدَيْبِيَةَ⁩». `RCT/E-RC47` |
Both were fetched because the review found the men carrying cards with no notice anywhere in the
delivered series. No other page was fetched for evening 4 — every new card is drawn from pages already
in the cache.
### Evening-4 review fixes — 2026-09-22 (all three pages were already cached; nothing was fetched)
| Book | Index | Printed | Why |
|---|---|---|---|
| ⁨البدایہ والنہایہ⁩ 30097 | 3354 | ⁨ج۷ ص۲۰۸⁩ | ⁨شرحبيل بن حسنة ؓ⁩ — his notice, «⁨وحَسَنَةُ أمه، نسب إليها وغلب عليه ذلك. أسلم قديمًا وهاجر إلى الحبشة⁩ …». `RCT/E-RC15` beat 2 |
| ⁨سیر أعلام النبلاء⁩ 10906 | 1749 | ⁨ج۱ ص۳۲۳⁩ | ⁨عكرمة بن أبي جهل ؓ⁩ — «⁨الشَّرِيْفُ، الرَّئِيْسُ، الشَّهِيْدُ⁩». `RCT/E-RC15` beat 1 |
| ⁨البدایہ والنہایہ⁩ 30097 | 3168 | ⁨ج۷ ص۲۲⁩ | Khālid's ؓ orders: «⁨وأمره بطُلَيْحة بن خُوَيْلد، فإذا فرغَ سار إلى مالك بن نُوَيْرَةَ بالبطاح إن أقام له⁩». The *After Buzākha* bridge slide |
## 2026-09-22 — Part VI, the dead of al-Yamāma (`DECISIONS.md` #48)
Every page below was already cached from the household research notes; this is the register entry for
putting them on a slide face.
| Book | Index | Printed | Why |
|---|---|---|---|
| ⁨البدایہ والنہایہ⁩ 30097 | 3196 | ⁨ج۷ ص۵۰⁩ | ⁨سالم مولى أبي حذيفة ؓ⁩ — «⁨استقرئوا القرآنَ من أربعةٍ⁩» (`AHA/E-AS09`); the two hands and the two ⁨آیات⁩ (`AS15`); «⁨فأضجعوني بينهما⁩» (`AS16`) |
| ⁨سیر أعلام النبلاء⁩ 10906 | 1595 | ⁨ج۱ ص۱۶۹⁩ | «⁨وَقِيْلَ: إِنَّ سَالِماً وُجِدَ هُوَ وَمَوْلاَهُ أَبُو حُذَيْفَةَ⁩ …» — `AHA/E-AS17`. ⚠ the «⁨وقيل⁩» is carried into the delivery |
| ⁨سیر أعلام النبلاء⁩ 10906 | 1622 | ⁨ج۱ ص۱۹۶⁩ | «⁨لاَ تَسْتَعْمِلُوا البَرَاءَ عَلَى جَيْشٍ⁩ …» — `THO/E-HS14`. ⚠ the page opens with «⁨قِيْلَ⁩» |
| ⁨سیر أعلام النبلاء⁩ 10906 | 1624 | ⁨ج۱ ص۱۹۸⁩ | «⁨أَترَانِي أَمُوْتُ عَلَى فِرَاشِي؟⁩ …» — `THO/E-HS15`; the count moves between chains, so "ninety-odd" |
| ⁨البدایہ والنہایہ⁩ 30097 | 3225 | ⁨ج۷ ص۷۹⁩ | «⁨استَحَرّ القتلُ في القُرّاء يوم اليمامة⁩» (`ZIA/E-ZY17`) and the order to ⁨زيد بن ثابت ؓ⁩ (`RCT/E-RC37`) — ⁨صحيح البخاري⁩ ٤٩٨٦ |
## 2026-09-23 — Parts VII–VIII, the men beside them (`DECISIONS.md` #49)
All cached from the household research notes; this is the register entry for putting them on a face.
| Book | Index | Printed | Why |
|---|---|---|---|
| ⁨سیر أعلام النبلاء⁩ 10906 | 1724 | ⁨ج۱ ص۲۹۸⁩ | ⁨زيد بن الخطاب ؓ⁩ — the banner: «⁨فَوَقَعَتْ الرَّايَةُ، فَأَخَذَهَا سَالِمٌ مَوْلَى أَبِي حُذَيْفَةَ⁩» (`AHA/E-AS13`); and ⁨عمر's ؓ⁩ «⁨أَسْلَمَ قَبْلِي⁩ …» and the east wind (`RCT/E-RC23`) |
| ⁨البدایہ والنہایہ⁩ 30097 | 3194 | ⁨ج۷ ص۴۸⁩ | the pit: «⁨ما هكذا كنَّا نقاتلُ مع رسول الله ﷺ⁩ …» — ⁨ثابت بن قيس ؓ⁩ and ⁨سالم ؓ⁩ (`AHA/E-AS14`) |
| ⁨البدایہ والنہایہ⁩ 30097 | 3195 | ⁨ج۷ ص۴۹⁩ | ⁨أبو مريم الحنفي⁩ and «⁨أكرم زيدًا بيدي⁩» (`ZIA/E-ZY4`); the ⁨مؤاخاة⁩ pair with ⁨معن بن عدي ؓ⁩ (`ZY8`); ⁨حزن المخزومي ؓ⁩ and his household (`ZY14`) |
| ⁨سیر أعلام النبلاء⁩ 10906 | 1747 | ⁨ج۱ ص۳۲۱⁩ | ⁨معن بن عدي ؓ⁩ — «⁨حَتَّى أُصَدِّقَهُ مَيْتاً، كَمَا صَدَّقْتُهُ حَيّاً⁩» (`ZIA/E-ZY9`) |
| ⁨سیر أعلام النبلاء⁩ 10906 | 1208 | ⁨سیر الراشدون ص۶۰⁩ | ⁨أبو عقيل ؓ⁩ — the arrow, and the wounds found on him (`ZIA/E-ZY12`) |
| ⁨البدایہ والنہایہ⁩ 30097 | 3199 | ⁨ج۷ ص۵۳⁩ | ⁨عبد الله بن عبد الله بن أُبَيّ ؓ⁩ (`ZIA/E-ZY13`). ⚠ where he died is disputed — say "in this war" |
| ⁨البدایہ والنہایہ⁩ 30097 | 3198 | ⁨ج۷ ص۵۲⁩ | ⁨الطفيل بن عمرو الدوسي ؓ⁩ and his son (`ZIA/E-ZY16`). ⚠ only what he interpreted, never the dream's own words |
| ⁨البدایہ والنہایہ⁩ 30097 | 1402 | ⁨ج۳ ص۴۲۸⁩ | ⁨حبيب بن زيد ؓ⁩ in Musaylima's hands — «⁨لا أسمع⁩» (`ZIA/E-ZY15`). ⚠ SPEAKER'S DISCRETION |
## 2026-09-23 — what the missing-detail audit put on cards (`DECISIONS.md` #51)
| Book | Index | Printed | Why |
|---|---|---|---|
| ⁨سیر أعلام النبلاء⁩ 10906 | 2262 | ⁨ج۲ ص۲۸۲⁩ | «⁨وَابْنُهَا الآخَرُ عَبْدُ اللهِ بنُ زَيْدٍ المَازِنِيُّ … وَهُوَ الَّذِي قَتَلَ مُسَيْلِمَةَ الكَذَّابَ بِسَيْفِهِ⁩» — the new card `ZIA/E-ZY18`. ⚠ ONE of four names (`QA_BANK.md` §5.3) |
| ⁨سیر أعلام النبلاء⁩ 10906 | 2258 | ⁨ج۲ ص۲۷۸⁩ | ⁨أم عمارة رضي الله عنها⁩'s own record — «⁨وَجَاهَدَتْ، وَفَعَلَتِ الأَفَاعِيْلَ⁩ … ⁨وَقُطِعَتْ يَدُهَا فِي الجِهَادِ⁩». `ZIA/E-ZY15` beat 5 |
| ⁨سیر أعلام النبلاء⁩ 10906 | 2261 | ⁨ج۲ ص۲۸۱⁩ | twelve wounds at ⁨أحد⁩; the hand and eleven more at ⁨اليمامة⁩; ⁨أبو بكر ؓ⁩ visiting her. ⚠ ⁨البدایہ ج۳ ص۴۲۸⁩ gives twelve **from اليمامة** — give one book's figure with its caption, or say "covered in wounds" |
| ⁨سیر أعلام النبلاء⁩ 10906 | 2407 | ⁨ج۲ ص۴۲۷⁩ | ⁨زيد بن ثابت ؓ⁩ — «⁨الخَزْرَجِيُّ، النَّجَّارِيُّ، الأَنْصَارِيُّ، كَاتِبُ الوَحْيِ⁩». His ⁨تراجم⁩ notice, now `RCT/E-RC37` beat 3 |
| ⁨سیر أعلام النبلاء⁩ 10906 | 2007 | ⁨ج۲ ص۲۷⁩ | ⁨أبو طلحة ؓ⁩ — «⁨وَأَحَدُ أَعْيَانِ البَدْرِيِّيْنَ، وَأَحَدُ النُّقَبَاءِ الاثْنَيْ عَشَرَ لَيْلَةَ العَقَبَةِ⁩», and his own name ⁨زيد بن سهل⁩. His notice, now `THO/E-HS1` beat 1 |
| ⁨الکامل فی التاریخ⁩ 21712 | 906 | ⁨ج۲ ص۲۱۵⁩ | ⁨الرجال بن عنفوة⁩ — «⁨وَبَعَثَهُ مُعَلِّمًا لِأَهْلِ الْيَمَامَةِ⁩». **The pronoun is unattached: the sender is NOT named.** Read to correct `RCT/E-RC57` |
| ⁨سیر أعلام النبلاء⁩ 10906 | 2411 | ⁨ج۲ ص۴۳۱⁩ | the ⁨جمع⁩ dialogue in ⁨زيد بن ثابت ؓ⁩'s own words — «⁨كَيْفَ تَفْعَلُوْنَ شَيْئاً لَمْ يَفْعَلْهُ رَسُوْلُ اللهِ⁩ …» / «⁨هُوَ -وَاللهِ- خَيْرٌ⁩». The new card `RCT/E-RC65` |
| ⁨البدایہ والنہایہ⁩ 30097 | 3181 | ⁨ج۷ ص۳۵⁩ | Ibn Kathīr's own figures for the day — «⁨وقتل من المسلمين ستمئة، وقيل: خمسمئة، فالله أعلم⁩», with Banū Ḥanīfa «⁨قريبًا من عشرة آلاف، وقيل: أحد وعشرون ألفًا⁩». `ZIA/E-ZY17` beats 4–5, **given as approximate because the book gives them that way** |
| ⁨البدایہ والنہایہ⁩ 30097 | 3180, 3206 | ⁨ج۷ ص۳۴⁩, ⁨ج۷ ص۶۰⁩ | read for the ⁨محكم بن الطفيل⁩ question: he advised Banū Ḥanīfa into the garden, and «⁨أدرك عبد الرحمن بن أبي بكر محكمَ بن الطفيل فرماه بسهمٍ في عنقه وهو يخطب فقتله⁩». **Not yet carded — Daniyal's decision** |
| ⁨الکامل فی التاریخ⁩ 21712 | 909 | ⁨ج۲ ص۲۱۸⁩ | the terms at the forts — «⁨فَصَالَحَهُ عَلَى كُلِّ شَيْءٍ دُونَ النُّفُوسِ⁩», then «⁨عَلَى الذَّهَبِ وَالْفِضَّةِ وَالسِّلَاحِ وَنِصْفِ السَّبْيِ، وَقِيلَ⁩: ⁨رُبْعُهُ⁩»; why he settled; and Ibn al-Athīr's count of the dead (360 + 300; Banū Ḥanīfa 7,000 × 3). `RCT/E-RC67`, `ZIA/E-ZY17` beats 6–7 (2026-09-27, `DECISIONS.md` #61) |
| ⁨سیر أعلام النبلاء⁩ 10906 | 1196 | ⁨الراشدون ص۴۸⁩ | ʿUrwa's list of the terms — gold and silver, armour and horses, half the slaves, a walled garden from every village; Salama b. ʿUmayr's «⁨قاتلوا ولا تقاضوا⁩»; «⁨فأسلم سائرهم⁩»; al-Zuhrī's men in the fort, spared (⚠ the number-word is misprinted — no figure spoken). `RCT/E-RC67`, `RC68` |
| ⁨البدایہ والنہایہ⁩ 30097 | 3181 | ⁨ج۷ ص۳۵⁩ | «⁨فأسلموا عن آخرهم ورجعوا إلى الحق⁩», some captives returned, the rest sent to al-Ṣiddīq; ⚠ ʿAlī ؓ and the mother of Muḥammad b. al-Ḥanafiyya (on the page; not for the platform). `RCT/E-RC68` |
| ⁨البدایہ والنہایہ⁩ 30097 | 3182 | ⁨ج۷ ص۳۶⁩ | the delegation of Banū Ḥanīfa at Medina and Musaylima's rhymed prose; «⁨فيقال⁩: ⁨إن الصّدّيق قال لهم⁩: ⁨ويحكم، أينَ كانَ يذهبُ بقولكم؟ إن هذا الكلام لم يخرج من إلٍّ⁩» — hedged on the page. `RCT/E-RC69` |
| ⁨البدایہ والنہایہ⁩ 30097 | 3187 | ⁨ج۷ ص۴۱⁩ | Oman — Laqīṭ «⁨ذو التاج⁩ … ⁨فادّعى النُّبوَّة أيضًا⁩»; «⁨فبعثَ جيفر إلى الصديق فأخبره الخبر واستجاشه⁩»; the command arrangement and «⁨إن ينتهيا إلى رأي عكرمة⁩»; Dabā with the families behind. `RCT/E-RC70`, `RC29` |
| ⁨الکامل فی التاریخ⁩ 21712 | 910 | ⁨ج۲ ص۲۱۹⁩ | the order to gather the Qurʾān inside the account of the battle — «⁨لِئَلَّا يَذْهَبَ الْقُرْآنُ⁩», «⁨وَسَيَرِدُ مُبَيَّنًا سَنَةَ ثَلَاثِينَ⁩»; **no mention of al-Bukhārī on the page** (the correction to `RCT/E-RC37` beat 6 and to the jamʿ note §5.1, 2026-09-27, `DECISIONS.md` #66) |
| ⁨الکامل فی التاریخ⁩ 21712 | 917 | ⁨ج۲ ص۲۲۶⁩ | Dabā — «⁨وَاسْتَعْلَى لَقِيطٌ⁩ … ⁨مَوَادُّهُمُ الْعُظْمَى⁩» from Banū Nājiya (al-Khirrīt b. Rāshid) and ʿAbd al-Qays (Sayḥān b. Wuṣḥān), ten thousand killed (his figure); the fifth with ʿArfaja; Mahra — Shikhrīt «⁨فَأَجَابَهُ وَأَسْلَمَ⁩». `RCT/E-RC29`, `RC30`, `RC70` (logged late, 2026-09-27) |
| ⁨البدایہ والنہایہ⁩ 30097 | 3188 | ⁨ج۷ ص۴۲⁩ | the relief «⁨في الساعة الراهنة⁩»; Mahra's two forces — «⁨على أحدهما - وهم الأكثر - أميرٌ يُقالُ له: المصبح، أحد بني محارب⁩»; «⁨وكان هذا الاختلاف رحمة على المؤمنين⁩»; harder than Dabā; the fifth with Shikhrīt. `RCT/E-RC29`, `RC30` (2026-09-27) |
| ⁨سیر أعلام النبلاء⁩ 10906 | 1756 | ⁨ج۱ ص۳۳۰⁩ | al-Ḥārith b. Hishām «⁨مِنَ الصَّحَابَةِ الأَشْرَافِ، وَهُوَ أَخُو أَبِي جَهْلٍ⁩» — Umm Ḥakīm's ؓ father; evening 5's Tree C. `TMW/E-TRN7` (2026-09-27) |
| ⁨سیر أعلام النبلاء⁩ 10906 | 823 | ⁨السیرة ۲ ص۱۶۴⁩ | «⁨واستأذنت أم حكيم بنت الحارث بن هشام وهي يومئذ مسلمة، وهي تحت عكرمة بن أبي جهل⁩» — the safe-conduct. `TMW/E-TRN7` (logged late, 2026-09-27) |
| ⁨سیر أعلام النبلاء⁩ 10906 | 1299 | ⁨الراشدون ص۱۵۷⁩ | the ṣuḥuf with Ḥafṣa ؓ, borrowed by ʿUthmān ؓ and returned; Ḥudhayfa's report from the campaign toward Armenia. `ABU/E-Q5` (logged late; the report added to the card 2026-09-27) |
| ⁨سیر أعلام النبلاء⁩ 10906 | 1211 | ⁨الراشدون ص۶۳⁩ | «⁨حتى جمعه زيد في صحف⁩» — the year-by-year notice of the collection. `ABU/E-Q3` beat 6 (logged late, 2026-09-27) |
| ⁨سیر أعلام النبلاء⁩ 10906 | 1163 | ⁨الراشدون ص۱۵⁩ | ʿAlī ؓ: «⁨أعظم الناس أجرا في المصاحف أبو بكر⁩ …», «⁨إسناده حسن⁩». `ABU/E-Q4` (logged late, 2026-09-27) |
| ⁨سیر أعلام النبلاء⁩ 10906 | 2408 | ⁨ج۲ ص۴۲۸⁩ | Zayd b. Thābit ؓ, the boy of Banū al-Najjār with seventeen sūras; «⁨يَا زَيْدُ! تَعَلَّمْ لِي كِتَابَ يَهُوْدٍ⁩ …». `ABU/E-Q7` (logged late, 2026-09-27) |
| ⁨سیر أعلام النبلاء⁩ 10906 | 2409 | ⁨ج۲ ص۴۲۹⁩ | «⁨فَمَا مَضَى لِي نِصْفُ شَهْرٍ حَتَّى حَذَقْتُهُ⁩»; Syriac in seventeen days; «⁨إِذَا نَزَلَ عَلَيْهِ الوَحْيُ، بَعَثَ إِلَيَّ، فَكَتَبْتُهُ⁩». `ABU/E-Q7` (2026-09-27) |
| ⁨سیر أعلام النبلاء⁩ 10906 | 2412 | ⁨ج۲ ص۴۳۲⁩ | al-Shaʿbī: «⁨غَلَبَ زَيْدٌ النَّاسَ عَلَى اثْنَتَيْنِ: الفَرَائِضِ، وَالقُرْآنِ⁩». `ABU/E-Q7` (2026-09-27) |
| ⁨سیر أعلام النبلاء⁩ 10906 | 1591 | ⁨ج۱ ص۱۶۵⁩ | Abū Ḥudhayfa ؓ: Muslim before ⁨دار الأرقم⁩; Abyssinia twice; «⁨سَهْلَةُ بِنْتُ سُهَيْلِ بنِ عَمْرٍو⁩»; «⁨أُخْتُهُ أُمُّ مُعَاوِيَةَ؛ هِنْدُ بِنْتُ عُتْبَةَ⁩». Evening 5's house tree (`DECISIONS.md` #67, 2026-10-01) |
| ⁨سیر أعلام النبلاء⁩ 10906 | 1592 | ⁨ج۱ ص۱۶۶⁩ | martyred at al-Yamāma in 12 AH «⁨هُوَ وَمَوْلاَهُ سَالِمٌ⁩»; his brother Abū Hāshim b. ʿUtba ؓ — «⁨فَأَسْلَمَ يَوْمَ الفَتْحِ، وَحَسُنَ إِسْلاَمُهُ⁩», Muʿāwiya ؓ at his bedside. The house tree's notes (2026-10-01) |
| ⁨سیر أعلام النبلاء⁩ 10906 | 2086 | ⁨ج۲ ص۱۰۶⁩ | Abū Sufyān ؓ — «⁨رَأْسُ قُرَيْشٍ، وَقَائِدُهُمْ يَوْمَ أُحُدٍ، وَيَوْمَ الخَنْدَقِ⁩»; «⁨تَدَارَكَهُ اللهُ بِالإِسْلاَمِ يَوْمَ الفَتْحِ⁩». `TMW/E-TRN24`; the house tree (2026-10-01) |
| ⁨سیر أعلام النبلاء⁩ 10906 | 1620 | ⁨ج۱ ص۱۹۴⁩ | Suhayl b. ʿAmr ؓ — «⁨وَكَانَ خَطِيْبَ قُرَيْشٍ، وَفَصِيْحَهُم، وَمِنْ أَشْرَافِهِم⁩»; «⁨تَأَخَّرَ إِسْلاَمُهُ إِلَى يَوْمِ الفَتْحِ، ثُمَّ حَسُنَ إِسْلاَمُهُ⁩». The Suhayl note; the house tree (2026-10-01) |
| ⁨البدایہ والنہایہ⁩ 30097 | 3170 | ⁨ج۷ ص۲۴⁩ | The Khaybar feint — «⁨وأظهروا ذلك ليرعبوا الأعرابَ⁩». `RCT/E-RC79`, new 2026-10-07 |
| ⁨البدایہ والنہایہ⁩ 30097 | 3184 | ⁨ج۷ ص۳۸⁩ | Bahrayn: al-Mundhir b. Sāwā ؓ dies; the rising; ⁨جُواثى⁩ besieged and its verses; al-Jārūd ؓ and ʿAbd al-Qays. `RC24`, `RC71`, `ATA/E-TB24` |
| ⁨البدایہ والنہایہ⁩ 30097 | 3185 | ⁨ج۷ ص۳۹⁩ | al-Dahnāʾ as three questions, the fajr and the duʿāʾ; the trench month; al-Ḥuṭam's death and Qays b. ʿĀṣim's «⁨واسوأتاه⁩». `RC25`, `RC26`, `RC73`, `RC74` |
| ⁨البدایہ والنہایہ⁩ 30097 | 3186 | ⁨ج۷ ص۴۰⁩ | ⁨دارين⁩ — the duʿāʾ going into the water, printed in full; the would-be king taken and his Islam; the monk of Hajar. `RC27`, `RC75` |
| ⁨البدایہ والنہایہ⁩ 30097 | 2940 | ⁨ج۶ ص۲۳۱⁩ | The march to Bahrayn in the telling of Sahm b. Minjāb: **the words of the duʿāʾ** at the water and at the sea. `RCT/E-RC87` |
| ⁨البدایہ والنہایہ⁩ 30097 | 3207 | ⁨ج۷ ص۶۱⁩ | **The year-12 frame** — «⁨استُهلَّت هذه السنة … جَوّالون في البلاد يمينًا وشمالًا⁩»; the «⁨وقد قيل⁩» view on Juwāthā/Oman/Mahra; the four kings and their sister. `RCT/E-RC80`, new 2026-10-07 (`DECISIONS.md` #71) |
| ⁨البدایہ والنہایہ⁩ 30097 | 3208 | ⁨ج۷ ص۶۲⁩ | The order to Iraq; al-Wāqidī's two accounts of the route and «⁨قلت: والمشهور الأول⁩»; al-Madāʾinī's ⁨المحرم ۱۲ھ⁩, Quṭba b. Qatāda and al-Muthannā b. Ḥāritha. Evening 7's cliffhanger (`ISA/E-C1`) |
| ⁨الکامل فی التاریخ⁩ 21712 | 892 | ⁨ج۲ ص۲۰۱⁩ | Quḍāʿa struck on Usāma's ؓ return; **Ibn Masʿūd's ؓ verdict on the whole decision** — «⁨لَوْلَا أَنَّ اللَّهَ مَنَّ عَلَيْنَا بِأَبِي بَكْرٍ⁩». `RCT/E-RC76`; ⬜ the verdict is evening 7's closer and still needs a card |
| ⁨الکامل فی التاریخ⁩ 21712 | 906 | ⁨ج۲ ص۲۱۵⁩ | The northern sectors — Quḍāʿa and Wadīʿa. `RCT/E-RC76` |
| ⁨الکامل فی التاریخ⁩ 21712 | 913 | ⁨ج۲ ص۲۲۲⁩ | The Lakhmid restoration «⁨نَرُدُّ الْمُلْكَ⁩…»; al-Ḥuṭam b. Ḍubayʿa, ⁨القَطيف⁩, ⁨هَجَر⁩, ⁨الخَطّ⁩ with the ⁨زُطّ⁩ and ⁨السَّبابجة⁩; **«⁨مِمَّنْ لَمْ يَزَلْ مُشْرِكًا⁩» — the ridda here was not all ridda**. `RC71`, `RC72` |
| ⁨الکامل فی التاریخ⁩ 21712 | 914 | ⁨ج۲ ص۲۲۳⁩ | The al-Jārūd ؓ pincer at ⁨هَجَر⁩; Abū Hurayra ؓ on the march; «⁨ضوضاء هزيمة أو قتال⁩»; Ibn Ḥadhf and his uncle Abjar b. Bujayr. `RC25`, `RC26`, `RC73` |
| ⁨الکامل فی التاریخ⁩ 21712 | 915 | ⁨ج۲ ص۲۲۴⁩ | «⁨إلا أهل دارين⁩»; ʿUtayba b. al-Nahhās and al-Muthannā b. Ḥāritha sealing the roads; ʿAfīf b. al-Mundhir; «⁨وَضَرَبَ الْإِسْلَامُ فِيهَا بِجِرَانِهِ⁩»; the monk's three reasons; Thumāma ؓ and the cloak. `RC27`, `RC74`, `RC75`, `RC28` |
| ⁨الکامل فی التاریخ⁩ 21712 | 917 | ⁨ج۲ ص۲۲۶⁩ | The appointments behind §9.1's four actions — ʿAttāb b. Asīd ؓ and the rest. `RCT/E-RC77` |
| ⁨الکامل فی التاریخ⁩ 21712 | 918 | ⁨ج۲ ص۲۲۷⁩ | **The four coastal and highland sub-fronts, single-source**; and Najrān's delegation renewing its covenant — «⁨أَرْسَلُوا وَفْدًا لِيُجَدِّدُوا عَهْدَهُمْ⁩». `RCT/E-RC77`; ⬜ Najrān still needs `RC78` |
| ⁨سیر أعلام النبلاء⁩ 10906 | 1690 | ⁨ج۱ ص۲۶۴⁩ | al-ʿAlāʾ b. al-Ḥaḍramī ؓ — his notice, and the sixteen riders. `RCT/E-RC25` |
| ⁨الکامل فی التاریخ⁩ 21712 | 942 | ⁨ج۲ ص۲۵۱⁩ | Heraclius, in Jerusalem, tells the Romans to make peace for half of Syria; they refuse. `ISA/E-C22` |
| ⁨الکامل فی التاریخ⁩ 21712 | 975 | ⁨ج۲ ص۲۸۴⁩ | The search for a king among the women of Kisrā's house; Yazdagird, hidden in Shīrā's days. `ISA/E-C21` |
| ⁨البدایہ والنہایہ⁩ 30097 | 3212 | ⁨ج۷ ص۶۶⁩ | al-Madhār; Hurmuz had written “to Ardashīr and Shīrā”. `ISA/E-C21` |
| ⁨البدایہ والنہایہ⁩ 30097 | 3231 | ⁨ج۷ ص۸۵⁩ | The four columns alarm the Romans; they write to Heraclius. `ISA/E-C22` |
| ⁨البدایہ والنہایہ⁩ 30097 | 3232 | ⁨ج۷ ص۸۶⁩ | «⁨ويحكم إن هؤلاء أهل دين جديد⁩» — Heraclius's advice, and the snort. `ISA/E-C22` |
| ⁨الکامل فی التاریخ⁩ 21712 | 925 | ⁨ج۲ ص۲۳۴⁩ | The march to Iraq, two tellings; ʿIyāḍ b. Ghanm ؓ from the upper end; **al-Muthannā had asked leave to raid Iraq**. `ISA/E-C26`, `ISA/E-C1` |
| ⁨الکامل فی التاریخ⁩ 21712 | 926 | ⁨ج۲ ص۲۳۵⁩ | al-Qaʿqāʿ, *one man*; ten thousand and eight thousand; three columns to al-Ḥafīr; Hurmuz. `ISA/E-C27`, `ISA/E-C28` |
| ⁨الکامل فی التاریخ⁩ 21712 | 927–934 | ⁨ج۲ ص۲۳۶–۲۴۳⁩ | Fetched with the two above (the Iraq campaign of year 12); **not yet read for any card** |
| ⁨الکامل فی التاریخ⁩ 21712 | 939 | ⁨ج۲ ص۲۴۸⁩ | The first banner for Syria: Khālid b. Saʿīd ؓ, and why it was taken back. `ISA/E-C25` (held) |
| ⁨الکامل فی التاریخ⁩ 21712 | 940 | ⁨ج۲ ص۲۴۹⁩ | Where the letter found ʿAmr ؓ; al-Walīd given Jordan; Yazīd's ؓ force. `GSA/E-ST9`, `ISA/E-C7` |
| ⁨الکامل فی التاریخ⁩ 21712 | 942 | ⁨ج۲ ص۲۵۱⁩ | Shuraḥbīl ؓ put over al-Walīd's post; where the four camped. `ISA/E-C7` |
| ⁨البدایہ والنہایہ⁩ 30097 | 3228 | ⁨ج۷ ص۸۲⁩ | Year 13 opens: why Syria — the verse, Tabūk, Usāma's ؓ army. `ISA/E-C23` |
| ⁨البدایہ والنہایہ⁩ 30097 | 3229 | ⁨ج۷ ص۸۳⁩ | The sermon; the banners; each by a road of his own. `ISA/E-C24`, `ISA/E-C7` |
| ⁨البدایہ والنہایہ⁩ 30097 | 3210 | ⁨ج۷ ص۶۴⁩ | The whole letter to the marzubāns; the three columns (Sayf). `ISA/E-C2`, `ISA/E-C28` |
