# Session 2 — SLIDES

**Abu Bakr al-Siddiq ؓ's caliphate entire · 11–13 AH / 632–634 CE · 60 slides**

Built by `python L02_baarah_saal/build.py` from `series/deck2.py`. **Do not hand-edit `L02.pptx` for anything structural** — edit `build.py` and rebuild. The running order here is `SPINE.md`'s, card for card; all 31 cards are represented.

**Every Arabic string below is lifted out of `SPINE.md` at build time and is never retyped.** `build.py --verify` fails the build if any of them stops being a literal substring of `SPINE.md`. Where a quotation was too long for one slide the deck shows a *contiguous clip* of it — the clip is checked the same way.

**English carries every slide (DECISIONS.md #19).** No generated Urdu anywhere. Arabic appears only as verbatim source quotation, in Naskh, with an English rendering beneath it. Citations are Latin with Latin digits, because an Arabic book title on the same line as “vol. 7, p. 10” is the bidi reordering bug CLAUDE.md §1.3 warns about.

## The five عبرت lines

**The cue sheet and the worksheet must print exactly these five, in this order.** They are `SPINE.md`'s own عبرت wording, drawn from the events. No present-day parallel is drawn from any of them, from the platform or in print.

1. There is a kind of steadiness that is not stubbornness: it is refusing to treat an emergency as permission.
2. The whole war was set moving from one camp, in one sitting, by a man who had just been told to go home.
3. Preservation is not one heroic act; it is somebody doing a careful, unglamorous job properly.
4. What changed in Arabia was not how many men there were, but which way they were all facing.
5. He kept an account of what was not his, and he closed it before he died.

## Visual inventory

| Kind | Count | Notes |
|---|---|---|
| `map_slide` | 9 | nine of the ten session-2 map files |
| `statement_slide` | 32 | 30 verbatim Arabic quotations + two English-only screens |
| `image_slide` | 5 | **the five Gemini jobs** — briefs below, and in the speaker notes |
| `diagram_slide` | 2 | the three things in the house; the three graves |
| `timeline_slide` | 2 | bookend in, bookend out |
| `section_slide` | 7 | one per act |
| title / lessons / question | 3 | |

`map_s2_close_23ah.png` is built and is **not** in tonight's deck — it is the closing map for the other stopping point (spec v4 §5).

**Image rule, non-negotiable:** every brief is non-figurative. No depiction of the Prophet ﷺ, of a Companion, or of any identifiable face — landscape, architecture, objects, texture, light only. Each brief already ends with the flat-white line, which `deck2` appends automatically; do not paste it twice.

---

## Slide 1 — title
**Headline:** Two Years, Three Months
**On screen:** `Session Two · Abu Bakr al-Siddiq ؓ` / **Two Years, Three Months** / `11–13 AH · 632–634 CE`
**You say:** two years · three months · that is the whole of it · name the book aloud
**Note:** Daniyal adds the Urdu session title by hand if he wants it on screen. Nothing Urdu is generated here.

---

## Slide 2 — timeline
**Headline:** Where we stopped last week
**On screen:** `line_s1.png` — the whole series Line. Caption: “The whole line. Tonight is the first two years of it.”
**You say:** last week · the whole line · we came from here · tonight is this much of it
**Note:** [BOOKEND IN] Session 1's closing Line, unchanged. Do not explain it — let them recognise it.

---

## Slide 3 — map
**Headline:** Arabia, the morning after
**On screen:** `map_s2_open_11ah.png` · kicker `11 AH`. Keys: **Medina** — the capital, and one field army · **The tribes around it** — some broken away, some refusing the zakat · **The army** — raised for the Syrian frontier, not yet gone · **Byzantine ground** — north-west, well past Tabuk
**You say:** the morning after · one town · one army, and it is pointed away · the ring around it
**Note:** [BOOKEND IN] Session 1's closing Map, unchanged. Where the room walked in.

---

## Slide 4 — section
**Headline:** The army he would not call back
**On screen:** Sub: `Act One · 11 AH · the first ten days`
**You say:** act one · the first ten days

---

## Slide 5 — statement
**Headline:** How long was he caliph?
**On screen:** **Two years and three months.** (54pt, English only — no Arabic on this one)
**You say:** [HANDS 1] ask it · take the hands · take two guesses · then advance · everything tonight is inside that

---

## Slide 6 — map
**Headline:** An army pointed north
**On screen:** `map_s2_usama.png` · kicker `Card 1 · 11 AH`. Keys: **Medina** — the army is raised in his last weeks · **Usama b. Zayd ؓ** — eighteen years old, given the command · **al-Jurf** — the camp one march outside the city · **Dhu Khushub** — on the road north · **Ubna, in the Balqa'** — Byzantine ground, well past Tabuk
**You say:** his last weeks · eighteen years old · in the ranks under him: Umar ؓ and the senior men · first time the map points at Byzantine ground

---

## Slide 7 — statement
**Headline:** The Prophet ﷺ answered them himself
**On screen:**

> إن تَطْعُنوا في إمارَتِهِ فَقَدْ كُنْتُمْ تَطْعُنون في إمارةِ أبيه منْ قَبْلُ، وايْمُ اللَّهِ إن كان لخليقًا للإمارة، وإن كان لمنْ أحَبِّ النّاس إليَّ، وإنَّ هذا لمِنْ أحبِّ الناسِ إليَّ بَعْدَه

> *English:* “If you find fault with his command, you found fault with his father's command before him — and this one is among the dearest of people to me after him.”

**Cite:** al-Bidaya wa-l-Nihaya, vol. 5, p. 311
**You say:** people said it out loud · he heard it · he stood up · his father commanded before him

---

## Slide 8 — statement
**Headline:** Do you call the army back?
**On screen:**

> والذي نفس أبي بكر بيده لو ظننت أن السباعَ تَخْطفني لأنفذتُ بعثَ أسامةَ كما أمرَ به رسولُ الله ﷺ؛ ولو لم يبقَ في القرى غيري لأنفذته

> *English:* “By Him in whose hand is Abu Bakr's soul — if I thought the wild beasts would snatch me away, I would still send out Usama's expedition as the Messenger of Allah ﷺ ordered it.”

**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 10
**You say:** [HANDS] ask first — capital surrounded, only army marching away · take the hands · among those advising recall: Umar ؓ · then read the line

---

## Slide 9 — statement
**Headline:** And you order me to depose him?
**On screen:**

> ثَكِلَتْكَ أُمُّكَ يَا ابْنَ الْخَطَّابِ! اسْتَعْمَلَهُ رَسُولُ اللَّهِ - صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ - وَتَأْمُرُنِي أَنْ أَعْزِلَهُ؟!

> *English:* “May your mother lose you, son of al-Khattab! The Messenger of Allah ﷺ appointed him — and you order me to depose him?”

**Cite:** al-Kamil fi al-Tarikh, vol. 2, p. 195
**You say:** not “cancel the march” — “give us an older commander” · Umar ؓ carried it · he came up off the ground · by the beard

---

## Slide 10 — image
**Headline:** The caliph on foot
**On screen:** Full-width picture. Caption: “He walked. The commander rode. His own beast was led behind, empty.”
**You say:** the caliph in the dust · the eighteen-year-old in the saddle · Abd al-Rahman b. Awf ؓ leading the empty beast · and then one favour, asked of the commander
**IMAGE BRIEF:** Restrained editorial illustration in muted ochre, bone and deep teal. A wide dusty caravan track leaving a walled palm oasis at first light, seen from ground level. Deep camel prints and bare human footprints pressed side by side into the dust and running away down the track. At the right edge, a saddled riderless camel standing with its lead-rope hanging loose. Low raking dawn light, long shadows, fine airborne dust, distant low hills. Absolutely no people, no faces, no human figures anywhere in the image. 16:9 landscape.

---

## Slide 11 — statement
**Headline:** Either you ride or I dismount
**On screen:**

> فقال أسامةُ: يا خليفةَ رسولِ الله: إما أن تركبَ وإما أن أنزلَ، فقال: والله لستَ بنازلٍ ولستُ براكب

> *English:* “Usama said: O successor of the Messenger of Allah, either you ride or I dismount. He said: By Allah, you shall not dismount, and I shall not ride.”

**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 11
**You say:** he offered to dismount · refused · rank is a place in an order

---

## Slide 12 — statement
**Headline:** Forty days, and what the tribes concluded
**On screen:**

> فجعل لا يمرُّ بقبيل يريدون الارتداد إلَّا قالوا: لولا أن لهؤلاء قوةً ما خرجَ مثلُ هؤلاء من عندهم

> *English:* “He passed no tribe intending to break away but they said: were it not that these people have strength, men like these would not have gone out from among them.”

**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 11
**You say:** marched late Rabi' al-Awwal · away forty days, some say seventy · it did not fight through, it passed · came back whole, and with spoil
**Note:** The books differ on the target — Ubna in the Balqa', or Quda'a clans, or a clash with Roman forces. Say so. The month of the return is our arithmetic, not a dated report; do not state it as sourced.

---

## Slide 13 — section
**Headline:** Arabia comes apart
**On screen:** Sub: `Act Two · 11 AH`
**You say:** act two · the year eleven

---

## Slide 14 — statement
**Headline:** The first engagement was a setback
**On screen:**

> فَخَرَجَ عَلَيْهِمُ الرِّدْءُ بِأَنْحَاءَ قَدْ نَفَخُوهَا … فَنَفَرَتْ إِبِلُ الْمُسْلِمِينَ وَهُمْ عَلَيْهَا، وَرَجَعَتْ بِهِمْ إِلَى الْمَدِينَةِ، وَلَمْ يُصْرَعْ مُسْلِمٌ.

> *English:* “The reserve came out at them with skins they had inflated … the Muslims' camels bolted with them on their backs and carried them back to Medina — and not one Muslim was thrown.”

**Cite:** al-Kamil fi al-Tarikh, vol. 2, p. 202
**You say:** [HANDS] a delegation goes home — what did they take besides your answer? · they counted the men · three days · the night raid · the reserve at Dhu Husa · inflated skins · the camels bolted
**Note:** Tell the setback plainly. The book records it without embarrassment, and that is the عبرت.

---

## Slide 15 — statement
**Headline:** That was the first victory
**On screen:**

> فَمَا طَلَعَ الْفَجْرُ إِلَّا وَهُمْ وَالْعَدُوُّ عَلَى صَعِيدٍ وَاحِدٍ … فَمَا ذَرَّ قَرْنُ الشَّمْسِ حَتَّى وَلَّوْهُمُ الْأَدْبَارَ … وَكَانَ أَوَّلَ الْفَتْحِ.

> *English:* “Dawn did not break until they and the enemy were on one ground … and the sun's rim had not risen before they turned their backs … and that was the first victory.”

**Cite:** al-Kamil fi al-Tarikh, vol. 2, p. 203
**You say:** the same night · the three brothers of Muqarrin · marched in the dark · swords among them before the sun's rim · garrison left at Dhu al-Qassa

---

## Slide 16 — map
**Headline:** Eleven banners at Dhu al-Qassa
**On screen:** `map_s2_ridda_eleven.png` · kicker `Card 8 · the biggest map moment of the evening`. Keys: **Dhu al-Qassa** — one day's ride out from Medina · **Eleven commanders** — each given an objective and written orders · **North and east** — Najd, al-Yamama, al-Sham, Quda'a · **East and south-east** — al-Bahrayn, Uman, Mahra · **South** — Yemen, Tihama, Hadramawt
**You say:** [HANDS 2] ask BEFORE the slide — one town, how many armies at once? · then count the arrows with the room · he rode out a third time, sword drawn · Ali ؓ at his camel's head · they would not let him go on
**Note:** Ibn Kathir announces eleven and prints ten; al-Kamil prints all eleven — that is why a listener may have counted ten. **Do not name the ninth commander:** three sources give three forms of the name.

---

## Slide 17 — image
**Headline:** The letter went ahead of the armies
**On screen:** Full-width picture. Caption: “One wording, copied out many times, carried ahead of the columns.”
**You say:** before the armies, the letters · one wording · read aloud in every assembly · a test any man could apply from a distance
**Note:** The same letter carries a harsh clause. **Do not quote it and do not deny it.** If raised: it is on that page, transmitted by Sayf b. Umar; the operative test on the same page is the adhan; the question is for the fuqaha'.
**IMAGE BRIEF:** Restrained editorial still life in muted ochre, bone and deep teal. A single sheet of aged parchment lying open on a plain scrubbed wooden board, its writing suggested only as soft illegible strokes — never readable letters of any script. Beside it a cut reed pen and a small dark unglazed ink vessel; to one side a neat stack of several identical folded and sealed letters waiting to be carried. Soft directional daylight from one side, quiet shadows. No people, no hands, no faces. 16:9 landscape.

---

## Slide 18 — statement
**Headline:** The letter set one test
**On screen:**

> وقد أمرتُ رسولي أن يقرأ كتابه في كلِّ مَجْمعٍ لكم، والداعية الأذان، فإذا إذَّنَ المسلمون فأذنوا فكُفُّوا عنهم، وإن لم يُؤَذِّنوا فسلوهم ما عليهم.

> *English:* “I have ordered my messenger to read his letter in every assembly of yours. The summons is the adhan: when they call it, hold off from them; if they do not, ask them what they owe.”

**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 24
**You say:** no lawyer, no court · call the adhan when you halt · if they answer it, stop · if not, ask what they owe

---

## Slide 19 — map
**Headline:** Buzakha
**On screen:** `map_s2_buzakha.png` · kicker `Card 10 · 11 AH`. Keys: **Aja' and Salma** — Khalid ؓ moves from here · **Sumayra'** — Tulayha moves up to meet him · **Buzakha** — Asad and Ghatafan; seven hundred of Fazara · **Banu Amir** — sitting armed nearby, waiting to see · **Then north-west to al-Sham** — Tulayha's line of flight
**You say:** wrapped in a cloak, waiting for revelation · Uyayna b. Hisn doing the fighting · Banu Amir armed, watching which way it goes · three times he broke off and walked back to the cloak

---

## Slide 20 — statement
**Headline:** The man who walked off the field
**On screen:**

> قَالَ لِي: إِنَّ لَكَ رَحًا كَرَحَاهُ، وَحَدِيثًا لَا تَنْسَاهُ. فَقَالَ عُيَيْنَةُ: قَدْ عَلِمَ اللَّهُ أَنَّهُ سَيَكُونُ حَدِيثٌ لَا تَنْسَاهُ، انْصَرِفُوا يَا بَنِي فَزَارَةَ فَإِنَّهُ كَذَّابٌ.

> *English:* “He said to me: you have a mill like his mill, and a matter you will not forget. Uyayna said: Allah knows there will be a matter you will not forget. Withdraw, Banu Fazara — the man is a liar.”

**Cite:** al-Kamil fi al-Tarikh, vol. 2, p. 205
**You say:** [HANDS] he had followed this man, and was fighting for him that morning — what was the question that ended it? · twice: no · the third time: yes · and then what was said
**Note:** Tulayha's own exit is on the same page — a horse ready, a mount for his wife, and a line called back over his shoulder. It is in the briefing, in Arabic.

---

## Slide 21 — statement
**Headline:** One clause struck out in public
**On screen:**

> فَقَالَ عمر: أما قولك: تدون قتلانا، فإنّ قتلانا قتلوا على أمر الله لا ديات لهم … وقال عمر في الثاني: نعم ما رأيت.

> *English:* “Umar ؓ said: as for your saying, and you pay blood-money for our dead — our dead were killed upon the command of Allah; there is no blood-money for them.”

**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 27  ·  Sahih al-Bukhari 7221
**You say:** two options, named to their faces · a war of expulsion, or a humbling settlement · weapons and horses · compensation one way only · and then Umar ؓ interrupted
**Note:** Ibn Mas'ud ؓ defines the first option — that they be put out of their homes (al-Kamil vol. 2 p. 201). **No captives were taken at Buzakha** (al-Kamil vol. 2 p. 206). Umar ؓ approved every other clause.

---

## Slide 22 — section
**Headline:** al-Yamama
**On screen:** Sub: `Act Three · 11–12 AH · the hardest day of the war`
**You say:** act three · the hardest day

---

## Slide 23 — map
**Headline:** Aqraba'
**On screen:** `map_s2_yamama.png` · kicker `Card 12 · 11–12 AH`. Keys: **al-Yamama** — Khalid ؓ comes east into it · **Aqraba'** — on the edge of the cultivated country · **Behind the line** — the farmland and the households · **No line of retreat** — no man falls back except through his home · **Forty thousand** — the fighting men Musaylima had
**You say:** point at the red block · it has no line of retreat · that was the intention · Ikrima ؓ and Shurahbil ؓ had approached earlier

---

## Slide 24 — statement
**Headline:** Keep this one man alive
**On screen:**

> أيها الرجل إن كنتَ تريد بأهل اليمامة غدًا خيرًا أو شرًا فاستبق هذا الرجل … فاستبقاه خالد مقيدًا، وجعله في الخيمة مع امرأته، وقال: استوصي به خيرًا.

> *English:* “Man — if you intend anything tomorrow for the people of Yamama, good or ill, keep this man alive … so Khalid kept him, in irons, and said: treat him well.”

**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 33
**You say:** the night before · a raiding party picked up coming home · one kept alive on a stranger's advice · Mujja'a b. Murara, in irons · treat him well
**Note:** That one decision settled the end of the battle before it started.

---

## Slide 25 — image
**Headline:** He put on his burial garments
**On screen:** Full-width picture. Caption: “Thabit b. Qays ؓ — rubbing himself with burial perfume, while the line went backwards.”
**You say:** Anas ؓ found him doing it · do you not see what is happening? · in a moment, nephew · two white garments — the ones he was buried in
**Note:** On the same field in the same minutes: Salim the freedman of Abu Hudhayfa ؓ (the man the Prophet ﷺ went out at night to listen to), Zayd b. al-Khattab ؓ, and Abu Hudhayfa ؓ. Their words are in the briefing, in Arabic — they are not on a slide because our sources give no English rendering for them and we do not compose one.
**IMAGE BRIEF:** Restrained editorial still life in muted bone, ochre and deep teal. Two plain undyed white cotton garments, freshly folded, resting on a low rough wooden bench; beside them a small unglazed clay vessel of perfume with its stopper set down alongside. Bare packed-earth floor, plain mud-brick wall behind. Quiet dignified morning light falling from a small high opening. No people, no hands, no faces, no figures. 16:9 landscape.

---

## Slide 26 — statement
**Headline:** This is not how we used to fight
**On screen:**

> هَكَذَا عَنْ وُجُوْهِنَا نُقَارِعُ القَوْمَ، بِئْسَ مَا عَوَّدْتُم أَقْرَانَكُم، مَا هَكَذَا كُنَّا نُقَاتِلُ مَعَ رَسُوْلِ اللهِ ﷺ.

> *English:* “Get out of our faces so we can strike the enemy. Wretched is what you have accustomed your opponents to! This is not how we used to fight alongside the Messenger of Allah ﷺ.”

**Cite:** Siyar A'lam al-Nubala', vol. 1, p. 311  ·  Sahih al-Bukhari 2845
**You say:** past the men falling back · get out of my way · the Ansar's banner · feet dug in to the middle of his shins · he did not move

---

## Slide 27 — image
**Headline:** The gate was shut from the inside
**On screen:** Full-width picture. Caption: “Eighty-odd wounds. Khalid ؓ stayed a month treating them. He survived.”
**You say:** [HANDS] the gate is shut, the wall is solid, thousands inside — what do you do? · then let them answer · then tell it
**Note:** **al-Bara' b. Malik ؓ SURVIVED.** Ibn Khaldun appears to list him among the killed; Siyar contradicts it (vol. 1 p. 196). Do not say he died there.
**IMAGE BRIEF:** Restrained editorial illustration in muted ochre and bone with deep teal shadow. A high solid mud-brick wall running right across the frame, with one heavy timber gate shut fast in it; the crowns of date palms visible above the wall from inside; stony open ground in the foreground. Seen from outside, straight on, the wall filling most of the frame so that it reads as unclimbable. Hard midday light, hard shadow at the foot of the wall. No people, no faces, no figures. 16:9 landscape.

---

## Slide 28 — statement
**Headline:** Throw me over onto them
**On screen:**

> يَا مَعْشَرَ الْمُسْلِمِينَ، أَلْقُونِي عَلَيْهِمْ فِي الْحَدِيقَةِ. فَقَالُوا: لَا نَفْعَلُ، فَقَالَ: وَاللَّهِ لَتَطْرَحُنَّنِي عَلَيْهِمْ بِهَا! … وَقَاتَلَ عَلَى الْبَابِ وَفَتَحَهُ لِلْمُسْلِمِينَ.

> *English:* “Company of Muslims — throw me over onto them into the garden. They said: we will not. He said: By Allah, you will throw me onto them in it!”

**Cite:** al-Kamil fi al-Tarikh, vol. 2, p. 218
**You say:** they refused · he made them do it · lifted on a shield on spear-shafts · down among them alone · fought to the gate and opened it

---

## Slide 29 — statement
**Headline:** What Wahshi ؓ said afterwards
**On screen:**

> وَعَنْ وَحْشِيٍّ، قَالَ: لَمْ أَرَ قَطُّ أَصْبَرَ عَلَى الْمَوْتِ مِنْ أَصْحَابِ مُسَيْلِمَةَ، ثُمَّ ذَكَرَ أَنَّهُ شَارَكَ فِي قَتْلِ مُسَيْلِمَةَ.

> *English:* “From Wahshi: I never saw men more steadfast in the face of death than Musaylima's companions — then he mentioned that he had a share in killing Musaylima.”

**Cite:** Siyar A'lam al-Nubala' (Sirat al-Khulafa' al-Rashidin), p. 48
**You say:** standing in a gap in the wall · Wahshi b. Harb ؓ, who had killed Hamza ؓ at Uhud · a second man came up · and what he said afterwards was not about himself
**Note:** Sources differ on the second man — al-Bidaya names Abu Dujana ؓ, al-Kamil says only “a man of the Ansar”. **Say “a second man came up”.** Do not use the anonymous ranking saying on the same Siyar page.

---

## Slide 30 — section
**Headline:** What it cost, and what it produced
**On screen:** Sub: `Act Four · 12 AH`
**You say:** act four · the cost, and what came out of it

---

## Slide 31 — statement
**Headline:** And Allah knows best
**On screen:**

> وقتل من المسلمين ستمئة، وقيل: خمسمئة، فالله أعلم، وفيهم من سادات الصحابة، وأعيان الناس من يُذكر بعد

> *English:* “Six hundred of the Muslims were killed — and it is said five hundred — and Allah knows best. Among them were leaders of the Companions and men of standing.”

**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 35
**You say:** [HANDS] if a book you loved lived only in people's memories — how many funerals to lose it? · the dead near ten thousand, some say twenty-one · six hundred Muslims, or five · and Allah knows best
**Note:** Ibn Kathir's phrase is “istaharra al-qatl fi al-qurra'” — the killing ran hot among the reciters; the editor glosses istaharra as ishtadda. **Never put a number of qurra' on a slide — no source we use gives one.**

---

## Slide 32 — statement
**Headline:** A thing the Messenger ﷺ did not do
**On screen:**

> فَقُلْتُ: كَيْفَ تَفْعَلُوْنَ شَيْئاً لَمْ يَفْعَلْهُ رَسُوْلُ اللهِ -صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ-. قَالَ: هُوَ -وَاللهِ- خَيْرٌ. فَلَمْ يَزَلْ أَبُو بَكْرٍ يُرَاجِعُنِي حَتَّى شَرَحَ اللهُ صَدْرِي لِلَّذِي شَرَحَ لَهُ صَدْرَ أَبِي بَكْرٍ وَعُمَر

> *English:* “I said: how will you do a thing the Messenger of Allah ﷺ did not do? He said: by Allah, it is good. And he did not stop coming back to me until Allah opened my breast.”

**Cite:** Siyar A'lam al-Nubala', vol. 2, p. 431
**You say:** Zayd b. Thabit ؓ, of Banu al-Najjar · eleven when the Prophet ﷺ reached Medina · seventeen suras before he was introduced · the Jews' script in a fortnight · wrote the revelation as it came · and he balked

---

## Slide 33 — image
**Headline:** There was no volume to copy from
**On screen:** Full-width picture. Caption: “Parchment, shoulder-blades, palm-stalks — and the breasts of men.”
**You say:** [HANDS] say the four once · then ask the room to name them back · it is the one line everybody will remember
**Note:** Ibn Kathir names al-likhaf — the thin white stones — where al-Dhahabi names al-riqa'. If both are wanted, say so and cite both.
**IMAGE BRIEF:** Restrained editorial still life in muted ochre, bone and deep teal, laid out on a plain scrubbed wooden surface and seen from directly above. Four kinds of thing set well apart from one another: strips of aged parchment; two flat dried animal shoulder-blades; several bare stripped date-palm stalks; and a few thin flat white stones. Any marks on them suggested only as faint illegible strokes, never readable letters of any script. Soft even daylight, quiet shadows, generous empty space between the four groups. No people, no hands, no faces. 16:9 landscape.

---

## Slide 34 — statement
**Headline:** He tracked it down, piece by piece
**On screen:**

> فَكُنْتُ أَتَتَبَّعُ القُرْآنَ، أَجْمَعُهُ مِنَ الرِّقَاعِ، وَالأَكْتَافِ، وَالعُسُبِ، وَصُدُوْرِ الرِّجَالِ.

> *English:* “So I began to track down the Qur'an, gathering it from the parchments, the shoulder-blades, the palm-stalks, and the breasts of men.”

**Cite:** Siyar A'lam al-Nubala', vol. 2, p. 431
**You say:** no volume to copy from · the verb is tatabba'a — follow a thing up piece by piece · then one set of suhuf, in one place, for the first time

---

## Slide 35 — section
**Headline:** Arabia whole again
**On screen:** Sub: `Act Five · 12 AH`
**You say:** act five · and it closes

---

## Slide 36 — map
**Headline:** Darin — into the water
**On screen:** `map_s2_darin.png` · kicker `Card 19 · 11–12 AH`. Keys: **al-Bahrayn** — the beaten take ship from the coast · **The land roads** — closed first, by Bakr b. Wa'il · **Darin** — a day and a night out by sea · **Straight across the water** — out and back in a single day · **What was lost** — one man's horse-fodder, brought back to him
**You say:** he did not chase them · he closed the land first · then brought them to the water's edge · and told them what he intended
**Note:** Both books describe the crossing the same way — walking on something like soft sand with water over it, not deep enough to reach the camels' pads. al-Bidaya vol. 7 p. 40 prints the du'a they said going in.

---

## Slide 37 — statement
**Headline:** Go straight across the sea
**On screen:**

> قَدْ أَرَاكُمُ اللَّهُ مِنْ آيَاتِهِ فِي الْبَرِّ لِتَعْتَبِرُوا بِهَا فِي الْبَحْرِ، فَانْهَضُوا إِلَى عَدُوِّكُمْ وَاسْتَعْرِضُوا الْبَحْرَ.

> *English:* “Allah has shown you of His signs on land so that you may take heed of them at sea. Rise against your enemy, and go straight across the sea.”

**Cite:** al-Kamil fi al-Tarikh, vol. 2, p. 224
**You say:** signs on land, so take heed of them at sea · out and back the same day · he closed the roads behind them before he opened one in front of himself

---

## Slide 38 — map
**Headline:** Arabia whole again
**On screen:** `map_s2_arabia_12ah.png` · kicker `11 AH → 12 AH`. Keys: **Every region** — no part of the peninsula was untouched · **The armies** — sent to support believers already there · **The fifth of the spoils** — came back to Medina and was spent · **Najran** — renewed its covenant while others broke theirs · **A little over one year** — late 11 AH into early 12 AH
**You say:** one colour · no arrows · hold here and let them look at it · this is Ibn Kathir's own summing-up, not ours · he does not describe a conquest

---

## Slide 39 — statement
**Headline:** What Ibn Kathir says it was
**On screen:**

> ولم يزل الأمر كذلك حتى لم يبق بجزيرة العرب إلَّا أهل طاعة للّه ولرسوله، وأهل ذمة من الصديق، كأهل نجران وما جرى مجراهم ولله الحمد.

> *English:* “And matters continued so until there remained in the peninsula none but people obedient to Allah and His Messenger, and people under al-Siddiq's protection.”

**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 43
**You say:** the armies were sent to hold up people already standing · obedience, or a covenant · Najran renewed theirs while Muslim tribes broke theirs · over in a little more than a year
**Note:** A contiguous clip of a 339-character passage. The whole passage, including the closing date sentence, is in the briefing.

---

## Slide 40 — statement
**Headline:** Ibn Khaldun, as he reads it  *(no title bar — the quotation is long, so it carries the slide on its own)*
**On screen:**

> والسّبب في ذلك … أنّ الصّبغة الدّينيّة تذهب بالتنافس والتّحاسد الّذي في أهل العصبيّة وتفرد الوجهة إلى الحقّ فإذا حصل لهم الاستبصار في أمرهم لم يقف لهم شيء لأنّ الوجهة واحدة والمطلوب متساو عندهم وهم مستميتون عليه

> *English:* “The religious colouring takes away the rivalry and envy that are in people of asabiyya, and makes their direction one.”

**Cite:** Ibn Khaldun · Tarikh Ibn Khaldun, vol. 1, p. 198 — as he reads it
**You say:** [HANDS] two years after the tribes broke apart they were moving on two empires — what had changed? · he multiplies nobody's numbers · the direction is one · the object is equal in every eye
**Note:** **Say his name, and say “as he reads it” — it is on the citation line.** He never wrote this about the ridda; joining his chapter to the year eleven is ours, not his. Ibn Khaldun is admitted for judgement and framing only (DECISIONS.md #29).

---

## Slide 41 — statement
**Headline:** Worksheet — 90 seconds
**On screen:** **Mark three places on the map. Write three years into the boxes.** (44pt, English only)
**You say:** [WORKSHEET] say nothing at all while they write · do not fill the silence · watch the clock

---

## Slide 42 — section
**Headline:** Outward
**On screen:** Sub: `Act Six · 12–13 AH`
**You say:** act six · and Arabia stops being the whole board

---

## Slide 43 — statement
**Headline:** The order to Iraq  *(no title bar — the quotation is long, so it carries the slide on its own)*
**On screen:**

> وأن يَتألَّفَ الناسَ ويدعوهم إلى الله ﷿، فإن أجابوا وإلا أخذ منهم الجزيةَ فإن امتنعوا عن ذلك قاتلهم، وأمره أن لا يُكْرِه أحدًا على المسير معه، ولا يستعينُ بمنِ ارتدّ عن الإسلام وإن كان [قد] عاد إليه

> *English:* “Win the people over and call them to God … and he ordered him not to compel anyone to march with him, and not to use any man who had apostatised.”

**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 62
**You say:** Muharram 12 AH · it did not say conquer Iraq · come at it from its lower end · and then two restrictions that are easy to miss

---

## Slide 44 — map
**Headline:** Five days of waterless country
**On screen:** `map_s2_iraq_sham_13ah.png` · kicker `Card 23 · 13 AH`. Keys: **al-Hira** — Iraq entered from its lower end · **Quraqir** — the march strikes north-west, off any road · **The Samawa** — nine days say some; five nights say others · **Suwa and Tadmur** — he comes out behind the Roman armies · **The guide** — Rafi' b. Umayra al-Ta'i, whose eyes were bad
**You say:** [HANDS] how do you carry water for an army across five days with no wells? · take two answers · then tell them · camels made thirsty, watered twice, mouths bound · ten opened every day for the horses
**Note:** Length: al-Bidaya says nine days, al-Kamil and Siyar say five nights. **Say both.**

---

## Slide 45 — statement
**Headline:** Only once in my life
**On screen:**

> وَاللَّهِ مَا وَرَدْتُ هَذَا الْمَاءَ قَطُّ إِلَّا مَرَّةً وَاحِدَةً مَعَ أَبِي وَأَنَا غُلَامٌ

> *English:* “By God, I have come to this water only once in my life — with my father, when I was a boy.”

**Cite:** al-Kamil fi al-Tarikh, vol. 2, p. 253
**You say:** his eyes were bad · can you see a box-thorn bush the height of a seated man? · they said no · then by God you are dead, and I am dead with you · they looked again · cut to a stump · they dug at its root

---

## Slide 46 — statement
**Headline:** Let us take the command in turn  *(no title bar — the quotation is long, so it carries the slide on its own)*
**On screen:**

> إن هذا يوم من أيام الله، لا ينبغي فيه الفخر ولا البغي … فتعالوا فلنتعاور الإمارة فليكن عليها بعضُنا اليوم والآخر غدًا والآخر بعد غد، حتى يتأمَّر كلكم، ودعوني اليوم أليكم

> *English:* “Let us take the command in turn: one of us today, another tomorrow, another the day after — and let me have charge of you today.”

**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 89
**You say:** four commanders at the Yarmuk, nobody over all of them · he did not ask for the command · he proposed passing it round · they expected it to last a long time · it lasted one day

---

## Slide 47 — statement
**Headline:** Armies are made many by victory
**On screen:**

> ويلك، أتخوّفني بالروم؟ وإنما تكثر الجنود بالنصر، وتقل بالخذلان لا بعدد الرجال

> *English:* “Woe to you — are you frightening me with the Romans? Armies are made many by victory and few by abandonment, not by the number of men.”

**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 92
**You say:** [HANDS] ask the room to guess the two army sizes · take three guesses · then show that the books give three different answers, and say why · a Christian Arab said out loud what everyone could see

---

## Slide 48 — section
**Headline:** He dies
**On screen:** Sub: `Act Seven · 13 AH`
**You say:** act seven · he dies

---

## Slide 49 — statement
**Headline:** There is harshness in him
**On screen:**

> فَقَالَ: إِنَّهُ أَفْضَلُ مِنْ رَأْيِكَ إِلَّا أَنَّهُ فِيهِ غِلْظَةٌ. فَقَالَ أَبُو بَكْرٍ: ذَلِكَ لِأَنَّهُ يَرَانِي رَقِيقًا، وَلَوْ أَفْضَى الْأَمْرُ إِلَيْهِ لَتَرَكَ كَثِيرًا مِمَّا هُوَ عَلَيْهِ

> *English:* “He is better than your opinion of him — except that there is harshness in him. Abu Bakr said: that is because he sees me being gentle.”

**Cite:** al-Kamil fi al-Tarikh, vol. 2, p. 266
**You say:** [HANDS] who here has worked with someone whose hardness answered somebody else's softness? · he did not argue with the description · he explained it · put the office in his hands and much of it goes

---

## Slide 50 — statement
**Headline:** I have not appointed a relative over you
**On screen:**

> أَتَرْضُونَ بِمَنِ اسْتَخْلَفْتُ عَلَيْكُمْ؟ فَإِنِّي مَا اسْتَخْلَفْتُ عَلَيْكُمْ ذَا قَرَابَةٍ، وَإِنِّي قَدِ اسْتَخْلَفْتُ عَلَيْكُمْ عُمَرَ فَاسْمَعُوا لَهُ وَأَطِيعُوا، فَإِنِّي وَاللَّهِ مَا أَلَوْتُ مِنْ جُهْدِ الرَّأْيِ.

> *English:* “Are you content with the one I have appointed over you? For I have not appointed over you a relative of mine. I have appointed Umar over you.”

**Cite:** al-Kamil fi al-Tarikh, vol. 2, p. 267
**You say:** the document finished, and read out · Umar ؓ walking beside the man who carried it · we hear and we obey · then he asked them a question nobody had asked him

---

## Slide 51 — diagram
**Headline:** What in the house was not his
**On screen:** Three cards · kicker `Card 28 · the last day`: **A servant** — an Abyssinian, in the house · **A camel** — used for carrying water · **A blanket** — worn down to the nap. Caption: “Send them to Umar when I die. And she did.”
**You say:** he called A'isha ؓ · not a dinar, not a dirham, since the day he took charge · the coarsest of their food · the roughest of their clothing · then he listed these three

---

## Slide 52 — statement
**Headline:** He closed the account himself
**On screen:**

> وليس عندنا من فيء المسلمين شيء إلا هذا العبد الحبشي وهذا البعير الناضح وجرد هذه القطيفة، فإذا مت فابعثي بهن إلى عمر، ففعلت.

> *English:* “We have nothing of the Muslims' fay' except this Abyssinian servant, this water-carrying camel, and the worn nap of this blanket.”

**Cite:** Siyar A'lam al-Nubala' (al-Rashidun), p. 19
**You say:** three things · and an instruction about all three · and she did it

---

## Slide 53 — statement
**Headline:** Sell my land and pay them back
**On screen:**

> فَلَمَّا حَضَرَتْهُ الْوَفَاةُ أَوْصَى أَنْ تُبَاعَ أَرْضٌ لَهُ وَيُصْرَفَ ثَمَنُهَا عِوَضَ مَا أَخَذَهُ مِنْ مَالِ الْمُسْلِمِينَ.

> *English:* “When death came to him he directed that land of his be sold and its price paid over in compensation for what he had taken of the Muslims' property.”

**Cite:** al-Kamil fi al-Tarikh, vol. 2, p. 266
**You say:** the community voted him a maintenance when he gave up trading · a man cannot run a market stall and a state · sell a piece of land · pay it in against every dirham
**Note:** **Number caution:** the sources give 6,000 dirhams a year, half a sheep a day, and 2,500. **No figure on the slide.** The instruction is the point, not the amount.

---

## Slide 54 — statement
**Headline:** The living need the new more
**On screen:**

> وَقَالَ: الْحَيُّ أَحْوَجُ إِلَى الْجَدِيدِ مِنَ الْمَيِّتِ، إِنَّمَا هُوَ لِلْمُهْلَةِ وَالصَّدِيدِ.

> *English:* “He said: the living have more need of the new than the dead — this is only for the decay.”

**Cite:** al-Kamil fi al-Tarikh, vol. 2, p. 262
**You say:** his own washing · Asma' bint Umays ؓ, and his son Abd al-Rahman ؓ · the two garments I am wearing · buy one more

---

## Slide 55 — diagram
**Headline:** Three graves, one behind the other
**On screen:** Three cards · kicker `Card 31 · 13 AH`: **The Prophet ﷺ** — the first of the three · **Abu Bakr ؓ** — his head at the Prophet's ﷺ shoulders · **Umar ؓ** — later, his head at Abu Bakr's waist. Caption: “Four men went down: his son, Umar, Uthman and Talha.”
**You say:** he asked to be buried beside him · so they dug there · head at the shoulders · niche against niche
**Note:** One sentence in Siyar (al-Rashidun p. 19) fixes all three positions. **Do not claim the burial was “in A'isha's ؓ house” from these pages** — they say beside the Prophet ﷺ, and no more.

---

## Slide 56 — statement
**Headline:** Buried before morning came
**On screen:**

> وقالت عائشة: مات ليلة الثلاثاء، ودفن قبل أن يصبح.

> *English:* “A'isha ؓ said: he died on the night of Tuesday, and was buried before morning came.”

**Cite:** Siyar A'lam al-Nubala' (al-Rashidun), p. 19
**You say:** Monday evening, eight nights left of Jumada al-Akhira 13 AH · Umar ؓ prayed, four takbirs · the same bier · four men and a spade · sixty-three, the age at which the Prophet ﷺ died

---

## Slide 57 — timeline
**Headline:** What year are we in now?
**On screen:** `line_s2_lit.png` — only 11–13 AH lit, everything else greyed. Caption: “11 AH to 13 AH. Two years and three months.”
**You say:** [HANDS 3] ask it before you advance · let them answer · then show the Line
**Note:** [BOOKEND OUT] This slide opens session 3 unchanged (DECISIONS.md #23).

---

## Slide 58 — map
**Headline:** Where we stand now
**On screen:** `map_s2_close_13ah.png` · kicker `13 AH` — the 11 AH extent beneath it as a dashed outline. Keys: **Arabia** — whole, and under one authority · **Iraq** — entered from its lower end · **Syria** — the armies are on the Yarmuk · **The dashed outline** — where the map stood when you walked in
**You say:** hold on this one · say nothing · let them compare it with slide 3 themselves
**Note:** [BOOKEND OUT] This slide opens session 3 unchanged (DECISIONS.md #23).

---

## Slide 59 — lessons
**Headline:** Tonight
**On screen:** the five عبرت lines, in this order, nothing else:

1. There is a kind of steadiness that is not stubbornness: it is refusing to treat an emergency as permission.
2. The whole war was set moving from one camp, in one sitting, by a man who had just been told to go home.
3. Preservation is not one heroic act; it is somebody doing a careful, unglamorous job properly.
4. What changed in Arabia was not how many men there were, but which way they were all facing.
5. He kept an account of what was not his, and he closed it before he died.

**You say:** read them · do not explain them · no present-day parallel, from the platform or in print

---

## Slide 60 — question
**Headline:** Next week
**On screen:** **He said the office would take much of that hardness away. Next week — did it?**
**You say:** end on the question · never a summary · then a loud salam · then the dua
**Note:** Written slips into the box at the door. No live Q&A. Fifteen minutes afterwards, one to one.

---

## What is still open

- **Five Gemini images** — slides 10, 17, 25, 27, 33. Until they land the deck carries a correctly-sized dashed placeholder on each, with the brief repeated in the speaker notes. Nothing is flattened; paste straight over the box and delete it.
- **All ten maps and the lit Line are already rendered** and drop into the deck on build.
- `map_s2_close_23ah.png` is built and deliberately unused tonight — it is the closing map for the other stopping point.

