# Session 2 — SLIDES

**Abu Bakr al-Siddiq ؓ's caliphate entire · 11–13 AH / 632–634 CE · 97 slides · all 64 cards**

Built by `python L02_baarah_saal/build.py` from `series/deck2.py`. **Do not hand-edit `L02.pptx` for
anything structural** — edit `build.py` and rebuild. The running order here is `SPINE.md`'s, card
for card, and **all 64 cards are represented**.

**Rewoven 2026-09-10.** The deck previously covered 31 cards. `SPINE.md` now carries 64: the four
PEOPLE strands — the house of أم سليم ؓ (`THO`), أبو حذيفة ؓ and سالم ؓ (`AHA`), زيد بن الخطاب ؓ
and the dead of اليمامة (`ZIA`), and the men who had fought against Islam (`TMW`) — are inside the
main order at the points their own research notes specify. Every slide built for the old 31 is
kept: its wording, its image brief and its cautions are unchanged except where a length fix was
forced (noted below). The card numbers moved, because `SPINE.md` renumbered; the deck follows
`SPINE.md`.

**Every Arabic string below is lifted out of `SPINE.md` at build time and is never retyped.**
`build.py --verify` fails the build if any of them stops being a literal substring of `SPINE.md`.
Where a quotation was too long for one slide — or carried a glyph no installed Naskh font has —
the deck shows a *contiguous clip* of it. A clip only ever slices; it never edits, re-orders or
re-vowels, and it is checked the same way. Six cards are clipped: **17, 19, 22, 26, 51, 53**, each
for a reason given at its slide.

**English carries every slide (`DECISIONS.md` #19).** No generated Urdu anywhere. Arabic appears
only as verbatim source quotation, in Naskh, with an English rendering beneath it. Citations are
Latin with Latin digits, because an Arabic book title on the same line as “vol. 7, p. 10” is the
bidi reordering bug `CLAUDE.md` §1.3 warns about.

---

## The starred cut, and where the marker lives

`SPINE.md` stars **27 cards** as the recommended 45-minute cut; the other **37** are the deliberate
over-build (`DECISIONS.md` #20). In the deck that comes out as:

| | Slides |
|---|---|
| Carry a **★** card | **37** |
| Are the over-build, **CUT-IF-SHORT** | **44** |
| Furniture (title, bookends, act openers, the hands-up beat, the worksheet, the close) | **16** |
| **Total** | **97** |

**The marker is in the SPEAKER NOTES, not on the slide face — and that is not a slip.** The brief
for this rebuild asked for `CUT-IF-SHORT · ` at the front of each unstarred slide's kicker.
`deck2` has since acquired a standing rule (`DECISIONS.md` #30, commit `aa09e5a`): *a slide face
carries only what the room may see; production apparatus goes in the speaker notes.* It is
**enforced** — the audit fails the build on the literal string `CUT-IF-SHORT` in any text box on
any slide. Weakening that rule to satisfy the older instruction would have put a build marker on a
projector in front of two hundred people, which is the exact failure the rule exists to stop. So:

- every over-build slide's speaker note **opens** with
  `CUT-IF-SHORT — card N is NOT in SPINE.md's starred 27-card cut. Delete this slide first…`;
- the build **prints the cuttable slide numbers** when it finishes;
- and they are listed here, once, so the cut can be made without opening a single note.

**Delete these 44 slides to reach the 45-minute cut:**

> **6–7, 11–13, 17, 20–21, 25, 29–34, 36–37, 40–43, 45–46, 50, 52–53, 55–57, 62–63, 68–71,
> 78–83, 85–86, 90**

Nothing later in the deck depends on any of them. Cutting all 44 leaves 53 slides: the 27 starred
cards and the 16 pieces of furniture.

---

## The five عبرت lines — **one of them changed**

**The cue sheet and the worksheet must print exactly these five, in this order.** They are
`SPINE.md`'s own عبرت wording, drawn from the events. No present-day parallel is drawn from any of
them, from the platform or in print.

1. There is a kind of steadiness that is not stubbornness: it is refusing to treat an emergency as permission.  *(card 3)*
2. The whole war was set moving from one camp, in one sitting, by a man who had just been told to go home.  *(card 9)*
3. **The tie was made in a year when they owned nothing, and it was still holding on the day they died.**  *(card 15 — NEW)*
4. Preservation is not one heroic act; it is somebody doing a careful, unglamorous job properly.  *(card 46)*
5. He kept an account of what was not his, and he closed it before he died.  *(card 60)*

> ### ⚠ What changed, and why — the cue sheet and worksheet must be reprinted
>
> **OUT:** *“What changed in Arabia was not how many men there were, but which way they were all
> facing.”* — Ibn Khaldūn's line, card 52.
> **IN:** card 15's line, above, at position 3.
>
> Two reasons, and both are rules already written down. **(a)** `DECISIONS.md` #29 admits Ibn
> Khaldūn **for judgement and framing only** — never as the authority for what happened. An عبرت
> is the evening's own conclusion drawn from a page-cited event; making a borrowed judgement one
> of the five put him in a load-bearing place the decision says he does not occupy. **(b)** The
> rewoven ACT 3 is now **27 of the 64 cards** — by far the largest movement of the evening — and
> it had no line at all. Card 15 is the card `SPINE.md` calls “the new opening for the whole
> اليمامة act”, and its line covers the whole household thread the act delivers: زيد ؓ and معن ؓ,
> أبو حذيفة ؓ and عباد ؓ, سالم ؓ asking to be laid down between them.
>
> **Card 52 loses nothing.** It keeps its slide (75), keeps its quotation, and Daniyal still speaks
> its عبرت from the platform — the speaker note says so. It is simply not one of the five printed
> lines.
>
> The other four are unchanged in wording and in order. Old line 3 is now line 4.

---

## Visual inventory

| Kind | Count | Notes |
|---|---|---|
| `statement_slide` | 65 | **63 verbatim Arabic quotations** + two English-only screens (5, 76) |
| `map_slide` | 9 | nine of the eleven session-2 assets |
| `image_slide` | 7 | **the seven Gemini jobs** — briefs below, and in the speaker notes |
| `diagram_slide` | 4 | Uḥud's order of battle · one house · the three things · the three graves |
| `section_slide` | 7 | one per act |
| `timeline_slide` | 2 | bookend in, bookend out |
| title / lessons / question | 3 | |

`map_s2_close_23ah.png` is built and is **not** in tonight's deck — it is the closing map for the
other stopping point (spec v4 §5). `map_s2_ridda.png`, `map_s2_twelve.png` and `line_s2.png` are
likewise unused tonight.

**Two new image briefs** were added with the people cards: the cooking pot (slide 42) and the east
wind (slide 58). Both are for cards whose `SPINE.md` entry says **Map: n/a** — they are about
people, not movement, so a picture or a large statement is the right slide, not a map.

**Image rule, non-negotiable:** every brief is non-figurative. No depiction of the Prophet ﷺ, of a
Companion, or of any identifiable face — landscape, architecture, objects, texture, light only.
`deck2` appends the flat-white line automatically; do not paste it twice.

---

## Guards added to `build.py`

Three defects in the old deck were invisible in PowerPoint and only showed in the printed preview.
They are now build failures, checked locally — none of them weakens `deck2`:

| Guard | Cap | What it stops |
|---|---|---|
| `cap()` on every caption | 74 characters | A caption that wraps puts its second line **off the bottom edge of the slide**. |
| `keys()` on every map key | label 20 chars · sub 24 chars with 5 keys, 46 with 4 | `deck2` caps a key's sub-line at eight words; eight words do not fit the 4.3-inch column, and the overflow lands on the label beneath it. This is what made the Buzākha and Usāma keys unreadable. |
| glyph check (run once, by hand) | — | Cards 22 and 26 closed on **U+FD41**, the ﵁ ligature, which **neither `Traditional Arabic` nor `Arabic Typesetting` has** — it projected as an empty box. Both statements are complete without it; the honorific is spoken. |

---

# The slides

Legend: **★** = a card in the starred 45-minute cut · **CUT** = over-build, marked in its speaker
note, listed above.

---

## 1 — title
**On screen:** `Session Two · Abu Bakr al-Siddiq ؓ` / **Two Years, Three Months** / `11–13 AH · 632–634 CE`
**You say:** two years · three months · that is the whole of it · name the book aloud
**Note:** Daniyal adds the Urdu session title by hand if he wants it on screen. Nothing Urdu is generated here.

## 2 — timeline · furniture
**Headline:** Where we stopped last week · kicker `Bookend in`
**On screen:** `line_s1.png`. Caption: “The whole line. Tonight is the first two years of it.”
**You say:** last week · the whole line · we came from here · tonight is this much of it
**Note:** [BOOKEND IN] Session 1's closing Line, unchanged. Do not explain it — let them recognise it.

## 3 — map · furniture
**Headline:** Arabia, the morning after · kicker `11 AH`
**On screen:** `map_s2_open_11ah.png`. Keys: **Medina** · **The tribes around it** · **The army** · **Byzantine ground**
**You say:** the morning after · one town · one army, and it is pointed away · the ring around it
**Note:** [BOOKEND IN] Session 1's closing Map, unchanged. Where the room walked in.

## 4 — section
**Headline:** The army he would not call back · `Act One · 11 AH · the first ten days`

## 5 — statement · furniture
**Headline:** How long was he caliph?
**On screen:** **Two years and three months.** (54pt, English only)
**You say:** [HANDS 1] ask it · take the hands · take two guesses · then advance · everything tonight is inside that

## 6 — diagram · CUT · card 1
**Headline:** The order of battle at Uhud
**On screen:** Three cards — **The right wing** · Khalid b. al-Walid, over the cavalry · **The left wing** · Ikrima, the son of Abu Jahl · **The army** · Abu Sufyan b. Harb, over all of it. Caption: “All three of them command for Islam before the year 23.”
**You say:** [HANDS] who commanded the Meccan army at Uhud? · let them answer · then all three names
**Note:** This is the frame the whole `TMW` strand hangs on. A man's place in one line of battle is not his place in the next.

## 7 — statement · CUT · card 1
**Headline:** The two wings at Uhud
**Cite:** al-Bidaya wa-l-Nihaya, vol. 4, p. 180
**You say:** Ibn Ishaq records exactly who led that cavalry · three thousand men · two hundred horses · read the names and stop there

## 8 — map · ★ · card 2
**Headline:** An army pointed north
**On screen:** `map_s2_usama.png`. Keys: **Medina** · **Usama b. Zayd ؓ** · **al-Jurf** · **Dhu Khushub** · **Ubna, in the Balqa'**
**You say:** his last weeks · eighteen years old · in the ranks under him: Umar ؓ and the senior men · first time the map points at Byzantine ground

## 9 — statement · ★ · card 2
**Headline:** The Prophet ﷺ answered them himself
**Cite:** al-Bidaya wa-l-Nihaya, vol. 5, p. 311
**You say:** people said it out loud · he heard it · he stood up · his father commanded before him

## 10 — statement · ★ · card 3
**Headline:** Do you call the army back?
**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 10
**You say:** [HANDS] ask first — capital surrounded, only army marching away · take the hands · among those advising recall: Umar ؓ · then read the line
**Note:** English trimmed by one clause so the block clears the citation strip. The full rendering is in the briefing.

## 11 — statement · CUT · card 4
**Headline:** And you order me to depose him?
**Cite:** al-Kamil fi al-Tarikh, vol. 2, p. 195
**You say:** not “cancel the march” — “give us an older commander” · Umar ؓ carried it · he came up off the ground · by the beard

## 12 — image · CUT · card 5
**Headline:** The caliph on foot
**On screen:** Caption: “He walked. The commander rode. His own beast was led behind, empty.”
**You say:** the caliph in the dust · the eighteen-year-old in the saddle · Abd al-Rahman b. Awf ؓ leading the empty beast · then one favour, asked of the commander
**IMAGE BRIEF:** Restrained editorial illustration in muted ochre, bone and deep teal. A wide dusty caravan track leaving a walled palm oasis at first light, seen from ground level. Deep camel prints and bare human footprints pressed side by side into the dust and running away down the track. At the right edge, a saddled riderless camel standing with its lead-rope hanging loose. Low raking dawn light, long shadows, fine airborne dust, distant low hills. Absolutely no people, no faces, no human figures anywhere in the image. 16:9 landscape.

## 13 — statement · CUT · card 5
**Headline:** Either you ride or I dismount
**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 11
**You say:** he offered to dismount · refused · rank is a place in an order

## 14 — statement · ★ · card 6
**Headline:** Forty days, and what the tribes concluded
**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 11
**You say:** marched late Rabi' al-Awwal · away forty days, some say seventy · it did not fight through, it passed · came back whole, and with spoil
**Note:** The books differ on the target — Ubna in the Balqa', or Quda'a clans, or a clash with Roman forces. Say so. The month of the return is our arithmetic, not a dated report.

## 15 — section
**Headline:** Arabia comes apart · `Act Two · 11 AH`

## 16 — statement · ★ · card 7
**Headline:** The first engagement was a setback
**Cite:** al-Kamil fi al-Tarikh, vol. 2, p. 202
**You say:** [HANDS] a delegation goes home — what did they take besides your answer? · they counted the men · three days · the night raid · the reserve at Dhu Husa · inflated skins · the camels bolted
**Note:** Tell the setback plainly. The book records it without embarrassment, and that is the عبرت.

## 17 — statement · CUT · card 8
**Headline:** That was the first victory
**Cite:** al-Kamil fi al-Tarikh, vol. 2, p. 203
**You say:** the same night · the three brothers of Muqarrin · marched in the dark · swords among them before the sun's rim · garrison at Dhu al-Qassa

## 18 — map · ★ · card 9
**Headline:** Eleven banners at Dhu al-Qassa
**On screen:** `map_s2_ridda_eleven.png`. Keys: **Dhu al-Qassa** · **Eleven commanders** · **North and east** · **East and south-east** · **South**
**You say:** [HANDS 2] ask BEFORE the slide — one town, how many armies at once? · then count the arrows with the room · he rode out a third time, sword drawn · Ali ؓ at his camel's head · they would not let him go on
**Note:** Ibn Kathir announces eleven and prints ten; al-Kamil prints all eleven — that is why a listener may have counted ten. **Do not name the ninth commander:** three sources give three forms of the name. The biggest map moment of the evening.

## 19 — statement · ★ · card 9  *(new — the card's own quotation, which the old deck did not carry)*
**Headline:** Eleven directions from one camp
**Cite:** al-Kamil fi al-Tarikh, vol. 2, p. 204
**You say:** each commander's troops joined him on that ground · then they separated · one camp, one sitting, eleven directions

## 20 — image · CUT · card 10
**Headline:** The letter went ahead of the armies
**On screen:** Caption: “One wording, copied many times, carried ahead of the columns.”
**You say:** before the armies, the letters · one wording · read aloud in every assembly · a test any man could apply from a distance
**Note:** The same letter carries a harsh clause. **Do not quote it and do not deny it.** If raised: it is on that page, transmitted by Sayf b. Umar; the operative test on the same page is the adhan; the question is for the fuqaha'.
**IMAGE BRIEF:** Restrained editorial still life in muted ochre, bone and deep teal. A single sheet of aged parchment lying open on a plain scrubbed wooden board, its writing suggested only as soft illegible strokes — never readable letters of any script. Beside it a cut reed pen and a small dark unglazed ink vessel; to one side a neat stack of several identical folded and sealed letters waiting to be carried. Soft directional daylight from one side, quiet shadows. No people, no hands, no faces. 16:9 landscape.

## 21 — statement · CUT · card 10
**Headline:** The letter set one test
**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 24
**You say:** no lawyer, no court · call the adhan when you halt · if they answer it, stop · if not, ask what they owe

## 22 — statement · ★ · card 11
**Headline:** A sword among the swords of Allah
**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 24
**You say:** he quoted it when he gave Khalid ؓ the ridda command · the man who transmits it is Wahshi b. Harb ؓ · twelve years earlier the two of them were on the same side at Uhud — and it was the other side
**Note:** **Grading.** Say only “Imam Ahmad records it.” The matn is graded hasan/sahih by its routes; this chain, through Harb b. Wahshi, is weak. Assert no grade from the platform.

## 23 — map · ★ · card 12
**Headline:** Buzakha
**On screen:** `map_s2_buzakha.png`. Keys: **Aja' and Salma** · **Sumayra'** · **Buzakha** · **Banu Amir** · **Then to al-Sham**
**You say:** wrapped in a cloak, waiting for revelation · Uyayna b. Hisn doing the fighting · Banu Amir armed, watching which way it goes · three times he broke off and walked back to the cloak

## 24 — statement · ★ · card 12
**Headline:** The man who walked off the field
**Cite:** al-Kamil fi al-Tarikh, vol. 2, p. 205
**You say:** [HANDS] he had followed this man, and was fighting for him that morning — what was the question that ended it? · twice: no · the third time: yes · and then what was said
**Note:** Tulayha's own exit is on the same page — a horse ready, a mount for his wife, a line called back over his shoulder. **Keep him alive in the room: he comes back at slide 72.**

## 25 — statement · CUT · card 13
**Headline:** What is defeating you?
**Cite:** Siyar A'lam al-Nubala' (al-Khulafa' al-Rashidun), p. 41
**You say:** [HANDS] “why did the ridda armies lose?” · take two or three answers · then read this · the difference was not in the numbers, and the losing side could see it

## 26 — statement · ★ · card 14
**Headline:** One clause struck out in public
**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 27 · Sahih al-Bukhari 7221
**You say:** two options, named to their faces · a war of expulsion, or a humbling settlement · weapons and horses · compensation one way only · and then Umar ؓ interrupted
**Note:** Ibn Mas'ud ؓ defines the first option — that they be put out of their homes (al-Kamil vol. 2 p. 201). **No captives were taken at Buzakha** (al-Kamil vol. 2 p. 206). Umar ؓ approved every other clause.

## 27 — section
**Headline:** al-Yamama · `Act Three · 11–12 AH · the hardest day of the war`

## 28 — statement · ★ · card 15  ← **عبرت line 3 comes from here**
**Headline:** Two brothers by appointment
**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 49
**You say:** [HANDS] you are given a brother — not born to you, assigned to you · how long would you expect that to last? · the mu'akhah · Zayd b. al-Khattab ؓ with Ma'n b. Adi ؓ · both killed at al-Yamama, the same day
**Note:** A second pair the same way — Abu Hudhayfa ؓ and Abbad b. Bishr ؓ, al-Bidaya vol. 7 p. 55. **This card is the frame of the act:** tell the room to watch for households, and the act then delivers four of them.

## 29 — statement · CUT · card 16
**Headline:** The son of the elder of the Jahiliyya
**Cite:** Siyar A'lam al-Nubala', vol. 1, p. 164
**You say:** [HANDS] who here has a relative who did not agree with the biggest decision they ever made? · leave the hands up one beat and move on — do not develop it · martyr, son of the elder of the Jahiliyya, man of Badr, in one sentence · he was Muslim before the house of al-Arqam

## 30 — statement · CUT · card 17  *(clipped)*
**Headline:** Something about your father
**Cite:** Siyar A'lam al-Nubala' (al-Sira al-Nabawiyya), p. 312
**You say:** after Badr the dead of Quraysh went into the well · the Prophet ﷺ looked at the face of his son and saw it had gone pale · and asked him · then prayed for him and spoke kindly to him
**Clip:** the report runs to 296 rendered characters. The slide carries **the answer**, which is the point of the card; the scene that leads into it, and the reporting verb, are spoken.

## 31 — statement · CUT · card 18
**Headline:** Four titles, and one origin
**Cite:** Siyar A'lam al-Nubala', vol. 1, p. 167
**You say:** [HANDS] where do you think the man who led the Muhajirun in prayer came from? · a slave, his origin Istakhr in Persia · freed by the woman of the household · adopted outright · four descriptions in a row, and not one is about where he came from

## 32 — statement · CUT · card 19  *(clipped)*
**Headline:** The imam at Quba'
**Cite:** Siyar A'lam al-Nubala', vol. 1, pp. 168–169
**You say:** the Muhajirun reached Medina before the Prophet ﷺ did · they camped at al-Usba beside Quba' and had to pray · they put a freed slave in front, because he had the most Qur'an · Umar ؓ was praying behind him
**Clip:** the Siyar editor's inline page break falls in the middle of the sentence. The slide carries the clause before it; the rest is spoken.

## 33 — map · CUT · card 20
**Headline:** Aqraba'
**On screen:** `map_s2_yamama.png`. Keys: **al-Yamama** · **Aqraba'** · **Behind the line** · **No line of retreat** · **Forty thousand**
**You say:** point at the red block · it has no line of retreat · that was the intention · Ikrima ؓ and Shurahbil ؓ had approached earlier

## 34 — statement · CUT · card 20
**Headline:** Keep this one man alive
**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 33
**You say:** the night before · a raiding party picked up coming home · one kept alive on a stranger's advice · Mujja'a b. Murara, in irons · treat him well
**Note:** That one decision settled the end of the battle before it started.

## 35 — statement · ★ · card 21
**Headline:** The line breaks
**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 33
**You say:** if we lose, your women are taken · the armies collided · the Muslim line broke · the bedouin ran · into Khalid's ؓ own tent · and the prisoner in irons stood up and gave her his protection
**Note:** The mirror is on the same day: Muslims came into the same tent meaning to kill him, and she gave him hers — Siyar (al-Khulafa' al-Rashidun) p. 47. The book keeps both halves.

## 36 — statement · CUT · card 22  *(clipped)*
**Headline:** The banner, and the vow of silence
**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 34
**You say:** he was carrying a banner and the line was going backwards · bite down on your back teeth · I will not speak until Allah routs them, or I meet Allah and put my case · the banner fell, and Salim ؓ picked it up
**Note:** **Three approved books give three different banner arrangements.** Say “he carried a banner” and never draw the diagram. al-Kamil vol. 2 p. 217 has a longer wording of the same vow — do not merge them.
**Clip:** the last token is the ﵁ ligature (U+FD41), which no installed Naskh font has. Dropped; the honorific is spoken.

## 37 — statement · CUT · card 23
**Headline:** Are you not content to live praised?
**Cite:** Siyar A'lam al-Nubala', vol. 1, p. 310
**You say:** the orator of the Ansar, and a very loud voice · the verse came down · he concluded he was of the people of the Fire · shut himself in his house · the Prophet ﷺ noticed he was missing
**Note:** The verse-and-house incident is Sahih Muslim 119 and Sahih al-Bukhari 3613. **Play this immediately before the shroud** — it is what makes the shroud land.

## 38 — image · ★ · card 24
**Headline:** He put on his burial garments
**On screen:** Caption: “Thabit b. Qays ؓ — burial perfume, while the line went backwards.”
**You say:** Anas ؓ found him doing it · do you not see what is happening? · in a moment, nephew · two white garments — the ones he was buried in
**Note:** On the same field in the same minutes, the whole army was calling to each other: “people of Surat al-Baqara — the sorcery is void today” (al-Bidaya vol. 7 p. 33). The three sayings of Salim ؓ, Zayd ؓ and Abu Hudhayfa ؓ now have slides of their own — 40, 36 and 41.
**IMAGE BRIEF:** Restrained editorial still life in muted bone, ochre and deep teal. Two plain undyed white cotton garments, freshly folded, resting on a low rough wooden bench; beside them a small unglazed clay vessel of perfume with its stopper set down alongside. Bare packed-earth floor, plain mud-brick wall behind. Quiet dignified morning light falling from a small high opening. No people, no hands, no faces, no figures. 16:9 landscape.

## 39 — statement · ★ · card 24
**Headline:** This is not how we used to fight
**Cite:** Siyar A'lam al-Nubala', vol. 1, p. 311 · Sahih al-Bukhari 2845
**You say:** past the men falling back · get out of my way · the Ansar's banner · feet dug in to the middle of his shins · he did not move

## 40 — statement · CUT · card 25
**Headline:** A wretched bearer of the Qur'an
**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 34
**You say:** holding the banner of the Muhajirun — a banner the man before him had been killed carrying · they asked him plainly · he answered a question about his courage by naming what he carried
**Note:** He is the man the Prophet ﷺ went out at night to listen to (Siyar vol. 1 p. 168).

## 41 — statement · CUT · card 26  *(clipped)*
**Headline:** Adorn the Qur'an with deeds
**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 34
**You say:** same field, same hour · not by tribe, not by clan · the people of the Qur'an · then he charged, drove them back, and was struck down
**Clip:** as slide 36 — the trailing ﵁ ligature has no glyph in any installed Naskh font. Dropped; the honorific is spoken.

## 42 — image · CUT · card 27
**Headline:** The armour in the cooking pot
**On screen:** Caption: “An upturned pot at the far end of the camp, a pack-saddle on top.”
**You say:** his coat of mail was stolen off his body and hidden · a man of the army saw him in a dream · at the far end of the camp, under an upturned pot with a pack-saddle on it · it was exactly there
**Note:** **Report the chain the way the books do.** Ibn Kathir says the account has other corroborating reports; his editor notes the daughter in the chain is unknown; and al-Haythami's line is the one to give aloud — the rest of the report is in the Sahih, the episode of the mail is not. **Build no ruling about dreams on it.**
**IMAGE BRIEF:** Restrained editorial still life in muted ochre, bone and deep teal. At the far edge of an emptied desert camp at dusk: a large blackened cooking pot turned upside down on bare stony ground, with a worn wooden camel pack-saddle set on top of it. Scuffed sand, a few tent-peg holes, cold ashes at one side, the ground running away flat behind. Long low light from one side, quiet blue shadow. No people, no hands, no faces, no figures, no weapons shown. 16:9 landscape.

## 43 — statement · CUT · card 27
**Headline:** A will carried out after his death
**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 48
**You say:** three things to say to the caliph — a debt he owed, property he had, a slave to be freed · twice he told the man not to let it go to waste · and in Medina Abu Bakr ؓ carried out the will of a man already dead
**Note:** The long version, naming Khalid ؓ and the caliph, is Siyar vol. 1 p. 313.

## 44 — statement · ★ · card 28
**Headline:** I find the scent of Paradise
**Cite:** al-Bidaya wa-l-Nihaya, vol. 4, p. 203
**You say:** [HANDS] has anyone here ever missed something and spent years wishing they had been there? · he had missed Badr · at Uhud the line broke · he walked forward and met Sa'd b. Mu'adh ؓ on the way
**Note:** Sa'd ؓ said afterwards that he himself could not do what that man had done. **The year is not fixed on the pages read** — Siyar's chapter heading is “the raid of Uhud, and it was in Shawwal”.

## 45 — statement · CUT · card 29
**Headline:** Known by his fingertips
**Cite:** al-Bidaya wa-l-Nihaya, vol. 4, p. 203 · Siyar (al-Sira al-Nabawiyya), vol. 1, p. 407
**You say:** more than eighty wounds — sword, spear and arrow · his own family could not tell who he was · his sister recognised her brother by his fingertips
**Note:** **Citation caution.** The verse is quoted on the al-Bidaya page; the surah-and-verse reference is printed on the Siyar page, not on that one. Both are on the slide's citation line. Check a mushaf before printing it anywhere else.

## 46 — statement · CUT · card 30
**Headline:** Do you see me dying in my bed?
**Cite:** Siyar A'lam al-Nubala', vol. 1, p. 198
**You say:** Anas ؓ came in on his brother and found him singing over his bow · how long is that going to go on? · and the answer was a question, and then a number
**Note:** The counts move between the chains — ninety-nine, ninety-odd, a hundred. Say “the reports give ninety-odd” and move on.

## 47 — image · ★ · card 31
**Headline:** The gate was shut from the inside
**On screen:** Caption: “Eighty-odd wounds. Khalid ؓ was a month treating them. He survived.”
**You say:** [HANDS] the gate is shut, the wall is solid, thousands inside — what do you do? · then let them answer · then tell it
**Note:** **al-Bara' b. Malik ؓ SURVIVED.** Ibn Khaldun appears to list him among the killed; Siyar contradicts it (vol. 1 p. 196). Do not say he died there.
**IMAGE BRIEF:** Restrained editorial illustration in muted ochre and bone with deep teal shadow. A high solid mud-brick wall running right across the frame, with one heavy timber gate shut fast in it; the crowns of date palms visible above the wall from inside; stony open ground in the foreground. Seen from outside, straight on, the wall filling most of the frame so that it reads as unclimbable. Hard midday light, hard shadow at the foot of the wall. No people, no faces, no figures. 16:9 landscape.

## 48 — statement · ★ · card 31
**Headline:** Throw me over onto them
**Cite:** al-Kamil fi al-Tarikh, vol. 2, p. 218
**You say:** they refused · he made them do it · lifted on a shield on spear-shafts · down among them alone · fought to the gate and opened it

## 49 — diagram · ★ · card 32
**Headline:** One house, Uhud and al-Yamama
**On screen:** Three cards — **The servant** · Anas b. Malik ؓ, the Prophet's ﷺ servant for ten years · **The brother** · al-Bara' b. Malik ؓ, the man on the shield · **The uncle** · Anas b. al-Nadr ؓ, eighty-odd wounds at Uhud. Caption: “One house. The same count of wounds, and one got up.”
**You say:** **THE FAMILY SENTENCE — say it before or after, but say it.** the man on that shield is Anas b. Malik's ؓ elder brother · the elder brother of the boy who served the Prophet ﷺ for ten years · their uncle came off the field at Uhud with the same count of wounds, and did not get up
**Note:** Siyar vol. 1 p. 195 · al-Bidaya vol. 6 p. 396 · Siyar vol. 1 p. 196 · al-Bidaya vol. 4 p. 203. ⚠ **Do NOT add that his mother is the woman who asked for Islam as her dower** — no page read names al-Bara's ؓ mother, and `SPINE.md` says so explicitly. The sentence is just as strong through the brother, and the brother is on the page. **This card's quotation is slide 48's** and is deliberately not repeated: the card is here for the family, not for the saying.

## 50 — statement · CUT · card 33
**Headline:** The arrow he pulled out
**Cite:** Siyar A'lam al-Nubala' (al-Khulafa' al-Rashidun), p. 60
**You say:** one of the chiefs of the Ansar, and a man of Badr · an arrow hit him and he pulled it out · bound himself up, took his sword, went back · many wounds on him afterwards
**Note:** Two men who would not be carried — tell them as a pair with slide 48: al-Bara' ؓ survived with eighty wounds; Abu Aqil ؓ did not. ⚠ **The long famous version — the night wound, the dead arm, the severed arm, the fourteen wounds, “who won?” — is NOT in any approved source.** Tell only what is on the slide.

## 51 — statement · ★ · card 34
**Headline:** Lay me down between them
**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 50
**You say:** struck down · what has become of Abu Hudhayfa? · killed · and so-and-so? · killed · then lay me down between the two of them
**Note:** ⚠ The second man is **“so-and-so”** in the source. **Do not name him.** And no approved source says they were buried in one grave.

## 52 — statement · CUT · card 35
**Headline:** How they were found
**Cite:** Siyar A'lam al-Nubala', vol. 1, p. 169
**You say:** **it is said that…** — carry al-Dhahabi's رحمہ اللہ own «وقيل» across into the delivery, never “they were found”
**Note:** Elsewhere, in the roll of the day's martyrs (Siyar vol. 1 p. 298), he lists the two of them first and in that order: the master and the freedman on one line.

## 53 — statement · CUT · card 36
**Headline:** I do not hear
**Cite:** al-Bidaya wa-l-Nihaya, vol. 3, p. 428
**You say:** Musaylima had Habib b. Zayd ؓ in his hands · do you testify that Muhammad ﷺ is the Messenger of Allah? — yes · and that I am? — I do not hear · limb by limb, and never more than that answer
**Note:** His mother was Umm Umara Nusayba bint Ka'b رضي الله عنها — al-Aqaba, Uhud, al-Hudaybiya, Hunayn. She marched to al-Yamama with the army. Her hand was cut off there, and Abu Bakr ؓ as caliph was seen coming to ask after her. **Number caution:** Siyar vol. 2 p. 281 says eleven wounds besides; al-Bidaya vol. 3 p. 428 says twelve — give one figure with its caption, or say only “covered in wounds”. Her other son Abd Allah b. Zayd ؓ is one of **four** accounts of who killed Musaylima — do not settle it.

## 54 — statement · ★ · card 37
**Headline:** What Wahshi ؓ said afterwards
**Cite:** Siyar A'lam al-Nubala' (al-Khulafa' al-Rashidun), p. 48
**You say:** standing in a gap in the wall · Wahshi b. Harb ؓ, who had killed Hamza ؓ at Uhud · a second man came up · and what he said afterwards was not about himself
**Note:** Sources differ on the second man — al-Bidaya names Abu Dujana ؓ, al-Kamil says only “a man of the Ansar”. **Say “a second man came up”.** Do not use the anonymous ranking saying on the same Siyar page.

## 55 — statement · CUT · card 38
**Headline:** The same spear, at al-Yamama
**Cite:** al-Bidaya wa-l-Nihaya, vol. 4, p. 185
**You say:** he took the same spear · saw a man in a gap in a wall and did not know who it was · he would never claim the kill · and this is what he said about the two throws of his life

## 56 — statement · CUT · card 39
**Headline:** The witness against the enemy
**Cite:** Siyar A'lam al-Nubala' (al-Khulafa' al-Rashidun), p. 48
**You say:** he had spent his life among fighting men on both sides · his verdict was one sentence · and it was not the sentence anyone expects from the winning side
**Note:** **This is the same sentence as slide 54, given on its own** — `SPINE.md` deliberately carries the card twice, once from the `RCT` strand and once from `TMW`. If the evening is running, cut this and keep 54.

## 57 — statement · CUT · card 40
**Headline:** He outstripped me to both
**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 49
**You say:** the news came back to Medina · what Umar ؓ said was not about the battle · it was a count of two things, and he had come second in both
**Note:** Siyar vol. 1 p. 298 carries the second half as something he repeated.

## 58 — image · ★ · card 41
**Headline:** The east wind
**On screen:** Caption: “al-Saba is the east wind. It comes from the direction of al-Yamama.”
**You say:** al-Saba is the east wind · it comes to Medina from that direction · and he used to say the same thing about it
**Note:** ⚠ **The remark that the wind came from the direction of al-Yamama is the speaker's own — the books do not say it.** Say it as your own, or leave it out.
**IMAGE BRIEF:** Restrained editorial landscape in muted ochre, bone and deep teal. A wide empty stony plain seen low and level at the end of the day, with fine dust and a few dry grass heads bent all one way by a steady wind coming from the far horizon. No road, no building, no animal. A low pale sky, long soft shadows, the air slightly hazy with carried dust. Absolutely no people, no faces, no figures. 16:9 landscape.

## 59 — statement · ★ · card 41
**Headline:** I find in it the scent of Zayd
**Cite:** Siyar A'lam al-Nubala', vol. 1, p. 298
**You say:** the Companions' grief is recorded as carefully as their victories, and by the same men
**Note:** ⚠ **Caption caution.** al-Bidaya vol. 7 p. 50 has a different wording of the same remark. The slide carries the Siyar words under a Siyar caption. **Do not print the Siyar words under an Ibn Kathir caption.**

## 60 — section
**Headline:** What it cost, and what it produced · `Act Four · 12 AH`

## 61 — statement · ★ · card 42
**Headline:** The number nobody can give
**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 79 · Sahih al-Bukhari 4986
**You say:** [HANDS] how many men who had the whole Qur'an by heart died that day? what would you guess? · then the honest answer: **the books do not say**
**Note:** **This is the card that stops a wrong number being said.** The figures the safe list does give run from 58 to more than 1,080, and none of them is a count of reciters. Anyone who says “450 reciters” has misread al-Bidaya vol. 7 p. 55.

## 62 — statement · CUT · card 43
**Headline:** And Allah knows best
**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 35
**You say:** [HANDS] if a book you loved lived only in people's memories — how many funerals to lose it? · the dead near ten thousand, some say twenty-one · six hundred Muslims, or five · and Allah knows best
**Note:** Ibn Kathir's phrase is *istaharra al-qatl fi al-qurra'* — the killing ran hot among the reciters; the editor glosses *istaharra* as *ishtadda*. **Never put a number of qurra' on a slide.**

## 63 — statement · CUT · card 44
**Headline:** Take the Qur'an from four
**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 50
**You say:** Ibn Kathir رحمہ اللہ, writing his death notice, gives the reason the ummah remembered him · one of four men the Prophet ﷺ named · and one of the four was a freed slave of the house of Abu Hudhayfa ؓ
**Note:** **Slide rule.** Ibn Kathir's own text quotes only the opening clause. If the four names go on screen they must be captioned to **Sahih Muslim 2464** as given in the editor's note on al-Bidaya vol. 7 p. 50 — **never to Ibn Kathir.**

## 64 — statement · ★ · card 45
**Headline:** A thing the Messenger ﷺ did not do
**Cite:** Siyar A'lam al-Nubala', vol. 2, p. 431
**You say:** Zayd b. Thabit ؓ, of Banu al-Najjar · eleven when the Prophet ﷺ reached Medina · seventeen suras before he was introduced · the Jews' script in a fortnight · wrote the revelation as it came · and he balked

## 65 — image · ★ · card 46
**Headline:** There was no volume to copy from
**On screen:** Caption: “Parchment, shoulder-blades, palm-stalks — and the breasts of men.”
**You say:** [HANDS] say the four once · then ask the room to name them back · it is the one line everybody will remember
**Note:** Ibn Kathir names *al-likhaf* — the thin white stones — where al-Dhahabi names *al-riqa'*. If both are wanted, say so and cite both.
**IMAGE BRIEF:** Restrained editorial still life in muted ochre, bone and deep teal, laid out on a plain scrubbed wooden surface and seen from directly above. Four kinds of thing set well apart from one another: strips of aged parchment; two flat dried animal shoulder-blades; several bare stripped date-palm stalks; and a few thin flat white stones. Any marks on them suggested only as faint illegible strokes, never readable letters of any script. Soft even daylight, quiet shadows, generous empty space between the four groups. No people, no hands, no faces. 16:9 landscape.

## 66 — statement · ★ · card 46  ← **عبرت line 4 comes from here**
**Headline:** He tracked it down, piece by piece
**Cite:** Siyar A'lam al-Nubala', vol. 2, p. 431
**You say:** no volume to copy from · the verb is *tatabba'a* — follow a thing up piece by piece · then one set of suhuf, in one place, for the first time

## 67 — section
**Headline:** Arabia whole again · `Act Five · 12 AH`

## 68 — map · CUT · card 47
**Headline:** Darin — into the water
**On screen:** `map_s2_darin.png`. Keys: **al-Bahrayn** · **The land roads** · **Darin** · **Across the water** · **What was lost**
**You say:** he did not chase them · he closed the land first · then brought them to the water's edge · and told them what he intended
**Note:** Both books describe the crossing the same way — walking on something like soft sand with water over it, not deep enough to reach the camels' pads. al-Bidaya vol. 7 p. 40 prints the du'a they said going in.

## 69 — statement · CUT · card 47
**Headline:** Go straight across the sea
**Cite:** al-Kamil fi al-Tarikh, vol. 2, p. 224
**You say:** signs on land, so take heed of them at sea · out and back the same day · he closed the roads behind them before he opened one in front of himself

## 70 — statement · CUT · card 48
**Headline:** Not until you have proved yourself
**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 41
**You say:** one of the eleven banners · he attacked before Shurahbil ؓ arrived, wanting the victory on his own, and was badly handled · the caliph wrote to him · and then sent him on: Uman, Mahra, Yemen, Hadramawt
**Note:** He was corrected and kept, not corrected and dropped.

## 71 — statement · CUT · card 49
**Headline:** My Lord's speech, my Lord's speech
**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 127
**You say:** the son of Abu Jahl kissed the Book and wept over it
**Note:** ⚠ **Wording caution.** *Kissed* — «يقبّل» — is Ibn Kathir's wording, which is what this slide cites. “Held it to his face” is al-Darimi's wording and **must not be said under a Bidaya caption.** Imam Ahmad رحمہ اللہ later cited the habit as evidence in a question of law.

## 72 — statement · ★ · card 50  *(no title bar — the quotation is long, so it carries the slide on its own)*
**On screen:** the exchange with Umar ؓ, and what Umar ؓ did about it
**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 242
**You say:** [HANDS] **this is the payoff** — last time we left Tulayha riding away from Buzakha. what do you think became of him? · take answers · then tell it · Syria, the Ghassanids, back to Islam, umra at Mecca · twice, Ibn Kathir says, he could not bring himself to face Abu Bakr ؓ · and Umar ؓ was pleased by his words, and was satisfied with him
**Note:** English trimmed to two lines so the block clears the citation strip; the closing clause is spoken.

## 73 — map · ★ · card 51
**Headline:** Arabia whole again
**On screen:** `map_s2_arabia_12ah.png`. Keys: **Every region** · **The armies** · **The fifth** · **Najran** · **Just over a year**
**You say:** one colour · no arrows · hold here and let them look at it · this is Ibn Kathir's own summing-up, not ours · he does not describe a conquest

## 74 — statement · ★ · card 51  *(clipped)*
**Headline:** What Ibn Kathir says it was
**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 43
**You say:** the armies were sent to hold up people already standing · obedience, or a covenant · Najran renewed theirs while Muslim tribes broke theirs · over in a little more than a year
**Clip:** a contiguous clip of a 339-character passage. The whole passage, including the closing date sentence, is in the briefing.

## 75 — statement · ★ · card 52  *(no title bar — the quotation is long, so it carries the slide on its own)*
**Cite:** Ibn Khaldun · Tarikh Ibn Khaldun, vol. 1, p. 198 — as he reads it
**You say:** [HANDS] two years after the tribes broke apart they were moving on two empires — what had changed? · he multiplies nobody's numbers · the direction is one · the object is equal in every eye
**Note:** **Say his name, and say “as he reads it” — it is on the citation line.** He never wrote this about the ridda; joining his chapter to the year eleven is ours, not his. Ibn Khaldun is admitted for judgement and framing only (`DECISIONS.md` #29). **His عبرت is spoken here and is deliberately not one of tonight's five printed lines** — see the note at the top of this file.

## 76 — statement · furniture
**Headline:** Ninety seconds
**On screen:** **Mark three places on the map. Write three years into the boxes.** (44pt, English only)
**You say:** [WORKSHEET] say nothing at all while they write · do not fill the silence · watch the clock
**Note:** The headline reads “Ninety seconds”, not “Worksheet”: `deck2` forbids an instruction to the speaker on a slide face (`DECISIONS.md` #30). The instruction is in the speaker note.

## 77 — section
**Headline:** Outward · `Act Six · 12–13 AH`

## 78 — statement · CUT · card 53  *(clipped)*
**Headline:** Two restrictions that are easy to miss
**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 62
**You say:** Muharram 12 AH · it did not say conquer Iraq · come at it from its lower end · call them; if they answer, what is yours is theirs; if not, the jizya; if not that, fight · and then the two restrictions
**Clip:** the full sentence carries the **جل جلاله** ligature, which `Traditional Arabic` has no glyph for, and the Siyar editor's square-bracketed insertion, which bidi mirrors into nonsense beside Latin punctuation. Both sit outside the clause the card exists for. The slide carries the two restrictions — which is exactly where the card's عبرت lands — and the rest is spoken.

## 79 — statement · CUT · card 54
**Headline:** He walked beside the stirrup
**Cite:** Siyar A'lam al-Nubala', vol. 1, p. 329
**You say:** Yazid b. Abi Sufyan ؓ, called Yazid al-Khayr · brother of Umm Habiba ؓ, the Mother of the Believers · his father had led the army at Uhud · and when the standard was tied, the caliph did not stand and watch him ride out
**Note:** The caliph walked and the commander rode, and neither of them thought it strange. Pair it with slide 12 if both survive the cut.

## 80 — map · CUT · card 55
**Headline:** Five days of waterless country
**On screen:** `map_s2_iraq_sham_13ah.png`. Keys: **al-Hira** · **Quraqir** · **The Samawa** · **Suwa and Tadmur** · **The guide**
**You say:** [HANDS] how do you carry water for an army across five days with no wells? · take two answers · then tell them · camels made thirsty, watered twice, mouths bound · ten opened every day for the horses
**Note:** Length: al-Bidaya says nine days, al-Kamil and Siyar say five nights. **Say both.**

## 81 — statement · CUT · card 55
**Headline:** Only once in my life
**Cite:** al-Kamil fi al-Tarikh, vol. 2, p. 253
**You say:** his eyes were bad · can you see a box-thorn bush the height of a seated man? · they said no · then by God you are dead, and I am dead with you · they looked again · cut to a stump · they dug at its root

## 82 — statement · CUT · card 56  *(no title bar — the quotation is long, so it carries the slide on its own)*
**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 89
**You say:** four commanders at the Yarmuk, nobody over all of them · he did not ask for the command · he proposed passing it round · they expected it to last a long time · it lasted one day
**Note:** English trimmed to two lines so the block clears the citation strip.

## 83 — statement · CUT · card 57
**Headline:** Armies are made many by victory
**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 92
**You say:** [HANDS] ask the room to guess the two army sizes · take three guesses · then show that the books give three different answers, and say why · a Christian Arab said out loud what everyone could see

## 84 — section
**Headline:** He dies · `Act Seven · 13 AH`

## 85 — statement · CUT · card 58
**Headline:** There is harshness in him
**Cite:** al-Kamil fi al-Tarikh, vol. 2, p. 266
**You say:** [HANDS] who here has worked with someone whose hardness answered somebody else's softness? · he did not argue with the description · he explained it · put the office in his hands and much of it goes

## 86 — statement · CUT · card 59
**Headline:** I have not appointed a relative over you
**Cite:** al-Kamil fi al-Tarikh, vol. 2, p. 267
**You say:** the document finished, and read out · Umar ؓ walking beside the man who carried it · we hear and we obey · then he asked them a question nobody had asked him

## 87 — diagram · ★ · card 60
**Headline:** What in the house was not his
**On screen:** Three cards — **A servant** · an Abyssinian, in the house · **A camel** · used for carrying water · **A blanket** · worn down to the nap. Caption: “Send them to Umar when I die. And she did.”
**You say:** [HANDS] could you list, right now, everything in your house that is not yours? · he called A'isha ؓ · not a dinar, not a dirham, since the day he took charge · the coarsest of their food · the roughest of their clothing · then he listed these three

## 88 — statement · ★ · card 60  ← **عبرت line 5 comes from here**
**Headline:** He closed the account himself
**Cite:** Siyar A'lam al-Nubala' (al-Khulafa' al-Rashidun), p. 19
**You say:** three things · and an instruction about all three · and she did it

## 89 — statement · ★ · card 61
**Headline:** Sell my land and pay them back
**Cite:** al-Kamil fi al-Tarikh, vol. 2, p. 266
**You say:** the community voted him a maintenance when he gave up trading · a man cannot run a market stall and a state · sell a piece of land · pay it in against every dirham
**Note:** **Number caution:** the sources give 6,000 dirhams a year, half a sheep a day, and 2,500. **No figure on the slide.** The instruction is the point, not the amount.

## 90 — statement · CUT · card 62
**Headline:** The living need the new more
**Cite:** al-Kamil fi al-Tarikh, vol. 2, p. 262
**You say:** his own washing · Asma' bint Umays ؓ, and his son Abd al-Rahman ؓ · the two garments I am wearing · buy one more

## 91 — diagram · ★ · card 63
**Headline:** Three graves, one behind the other
**On screen:** Three cards — **The Prophet ﷺ** · the first of the three · **Abu Bakr ؓ** · his head at the Prophet's ﷺ shoulders · **Umar ؓ** · later, his head at Abu Bakr's waist. Caption: “Four men went down: his son, Umar, Uthman and Talha.”
**You say:** he asked to be buried beside him · so they dug there · head at the shoulders · niche against niche
**Note:** One sentence in Siyar (al-Khulafa' al-Rashidun p. 19) fixes all three positions. **Do not claim the burial was “in A'isha's ؓ house” from these pages** — they say beside the Prophet ﷺ, and no more.

## 92 — statement · ★ · card 63
**Headline:** Buried before morning came
**Cite:** Siyar A'lam al-Nubala' (al-Khulafa' al-Rashidun), p. 19
**You say:** Monday evening, eight nights left of Jumada al-Akhira 13 AH · Umar ؓ prayed, four takbirs · the same bier · four men and a spade · sixty-three, the age at which the Prophet ﷺ died

## 93 — statement · ★ · card 64
**Headline:** Had Salim ؓ been alive
**Cite:** al-Bidaya wa-l-Nihaya, vol. 7, p. 50
**You say:** eleven years later · Umar ؓ dying of the assassin's wound · he refused to name one man and set up a council of six · **and it is related that** he said this
**Note:** ⚠ Say **“it is related that…”** — that is Ibn Kathir's own passive. Ibn Abd al-Barr رحمہ اللہ explains it: he would have gone by Salim's ؓ judgement about whom to appoint. A second, differently worded report at Siyar vol. 1 p. 170 names **both** Salim ؓ and Abu Ubayda ؓ, and al-Dhahabi weakens its chain on the page. **Do not merge the two.** This is the last slide of the story, and it closes the freedman's thread eleven years past the battle.

## 94 — timeline · furniture
**Headline:** What year are we in now? · kicker `Bookend out`
**On screen:** `line_s2_lit.png`. Caption: “11 AH to 13 AH. Two years and three months.”
**You say:** [HANDS 3] ask it before you advance · let them answer · then show the Line
**Note:** [BOOKEND OUT] This slide opens session 3 unchanged (`DECISIONS.md` #23).

## 95 — map · furniture
**Headline:** Where we stand now · kicker `13 AH`
**On screen:** `map_s2_close_13ah.png`. Keys: **Arabia** · **Iraq** · **Syria** · **The dashed outline**
**You say:** hold on this one · say nothing · let them compare it with slide 3 themselves
**Note:** [BOOKEND OUT] This slide opens session 3 unchanged (`DECISIONS.md` #23).

## 96 — lessons · furniture
**Headline:** Tonight
**On screen:** the five عبرت lines, in the order given at the top of this file, nothing else
**You say:** read them · do not explain them · no present-day parallel, from the platform or in print

## 97 — question · furniture
**Headline:** Next week
**On screen:** **He said the office would take much of that hardness away. Next week — did it?**
**You say:** end on the question · never a summary · then a loud salam · then the dua
**Note:** Written slips into the box at the door. No live Q&A. Fifteen minutes afterwards, one to one.

---

## What is still open

- **Seven Gemini images** — slides **12, 20, 38, 42, 47, 58, 65**. Until they land the deck carries
  a correctly-sized dashed placeholder on each, with the brief repeated in the speaker notes and
  collected in `IMAGE_BRIEFS.md`. Nothing is flattened; paste straight over the box and delete it.
  Five are the original briefs, unchanged; **the cooking pot (42) and the east wind (58) are new.**
- **The cue sheet and the worksheet must be regenerated** — عبرت line 3 changed (see the top of
  this file). `CUE.pdf` and `WORKSHEET.pdf` still print the old five and now disagree with the deck.
  Nothing else in either artifact is affected.
- **All nine maps and both Line strips are already rendered** and drop into the deck on build.
- `map_s2_close_23ah.png` is built and deliberately unused tonight — it is the closing map for the
  other stopping point.
- **The bookend pair for every stopping point** (`DECISIONS.md` #23) is still only built for the
  planned one. If Daniyal expects to stop inside ACT 3 — which is now plausible, since ACT 3 alone
  is 27 cards — a closing Line and closing Map for al-Yamama should be added before delivery.
