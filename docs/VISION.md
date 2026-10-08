# VISION — the house style, as rules a script can check

**Read this before generating anything. Run the gate before showing Daniyal anything.**

```bash
python tools/check_vision.py SNN_<slug>        # exits non-zero on any breach; build.py runs it itself
```

> Daniyal, 2026-10-08: *"You need to fix the comments but more importantly we need to make the system that
> generates our content always within the vision given my feedback. Making that system is important, be it for
> animations, closeup maps, framing, word choices etc."*

**Why this file exists.** His feedback had been arriving evening by evening and being fixed slide by slide. The
same complaints came back — notes he could not find his line in, English on a face that meant nothing to the
room, maps that did not move with the story. **A rule he has had to repeat is a rule nothing enforces.** So every
rule here names the words of his that produced it and the check that now enforces it. Where a rule cannot be
checked by a script it says *review*, and it is checked by eye on the rendered slides before hand-over.

**How to add a rule.** When he comments on a slide, find the general rule the comment is an instance of. Write it
here with his words. Add its check to `tools/check_vision.py`. Then fix the slide. Never the fix alone.

---

## 0. What the room is for

A usable map of Islamic history for mature adults — **and to bring them closer to the dīn.** He said the second
half outright on 2026-10-08, of al-ʿAlāʾ b. al-Ḥaḍramī ؓ at al-Dahnāʾ: *"this is good stuff for galvanizing the
imaan of audience and getting them closer to deen."* And of the Arabic sources: *"they could give some amazing
or catchy lines for motivating people and boosting their iman if delivered in arabic."*

So an evening is judged on three things: **can the room follow it** (who, where, in what order), **is every word
of it on a page**, and **does it leave them with something to hold** — a line of Arabic, a duʿāʾ, a man who came back.

## 1. Words and framing

| | Rule | His words | Enforced by |
|---|---|---|---|
| **W1** | A Companion is **named**, with the honorific. Never a common noun in place of the name — *one man, a man, the commander* — on a face, a bridge, a key or a map. | *"'we followed one man', this doesn't sit well with sahaba, maybe we can describe 'Ikrima R.A's journey'"* | gate `W1` |
| **W2** | No entertainment vocabulary for real people: cast, character, villain, hero, episode, plot twist. | CLAUDE.md §1.2; *"cast"* rejected, 2026-08 | `deck2.audit` |
| **W3** | The English under an Arabic quotation is a **rendering only**. No commentary on the face, and never the word *image* for a figure of speech. | *"what image?"* — of a rendering that said *"the image is a camel kneeling"* | gate `W3` |
| **W4** | English carries everything; Claude generates no Urdu; Arabic appears only as verbatim quotation. | DECISIONS #19 | review |

## 2. Titles and faces

| | Rule | His words | Enforced by |
|---|---|---|---|
| **F1** | The deck title and every part divider **names a place or a person**, or carries the source's own Arabic. Never an English abstraction. | *"the title slides will make no sense to audience … change it altogether to reflect locations or maybe use arabic"* | gate `F1` |
| **F2** | A card about a person is headed by the person's **name** — with the ⁨لقب⁩, or a plain word or two. Never a sentence. | #68: *"obscure english sentences don't make much sense"* | `FACE_TITLE`; review |
| **F3** | A face carries only what the room may see: no labels, ids, tiers, cross-references, URLs. | #30 | `deck2.audit` |
| **F4** | A quotation that has no map of its own in front of it carries **one or two scene lines** — who, where, what is happening — twenty words in all. | *"maybe more detail on the slide? one or two small lines? describing the stirrup and the horse?"* | gate `F4` |
| **F5** | White ground, 24pt floor, twenty body words, no bullet lists. | #21 | `deck2` |
| **F6** | The kicker says **when and where** — never a bare *"11"*. | found by the gate, 2026-10-08 | gate `F6` |

## 3. Quotations

| | Rule | His words | Enforced by |
|---|---|---|---|
| **Q1** | Every quotation **names its speaker on the face**, above the book and the page. | *"who said this?"* | gate `Q1` |
| **Q2** | Arabic is verbatim from a cached page, lifted by bytes, never composed and never retyped. | CLAUDE.md §1.1, §1.4 | `check_citations` |
| **Q3** | Arabic too long to project is **excerpted** at a clause — the card's own words — never replaced by a picture. | *"i would like the arabic from ibn kathir verbatim somewhere"* | `FACE_CUT`; `check_face_quotes` |

## 4. The notes pane — the lectern

He delivers from the speaker notes and nothing else (#60). Evening 6's first build put **540 to 2,091 words**
under a single slide.

| | Rule | His words | Enforced by |
|---|---|---|---|
| **N1** | The pane opens with a **SAY** block of short cues — twelve words a cue, twelve cues a slide, 130 words above the rule. Detail goes below a drawn line. | *"tooooo much description in notes, i will get lost trying to find what to say"* · *"i can't easily figure out what do i say"* | gate `N1` |
| **N2** | **A blank line between every cue.** PowerPoint's pane ignores a stored font size; a blank line is the one spacing it cannot take away. | *"notes are good but maybe increase spacing, it would be hard for me to read"* | gate `N2` |
| **N3** | The **first cue is the situation** — what the scene is a response to. | *"when you say 'he set a condition on them', it doesn't tell the background in a line"* | review |
| **N4** | At most **two warnings** above SAY, one line each — only those that change what he says. | (the same complaints) | gate `N4` |
| **N5** | **No beat is dropped.** Every numbered beat on a card reaches the notes. | the line he asked for at slide 16 was on the card; the parser had thrown it away, with 48 others | gate `N5`; parser fixed |
| **N6** | No production apparatus in the lectern tier: no file names, card ids, decision numbers. | #59, #60 | gate `N6` |

Beats are written **`Cue — detail`**. The cue is what he looks for; the detail is behind it, under the rule.
The pane is built by `series/notes2.py`.

## 5. Maps

He wants a map to tell the story the way a *Kings and Generals* or *Total War* video tells it.

| | Rule | His words | Enforced by |
|---|---|---|---|
| **M1** | A part **opens on a map of the situation** before any words slide: who held the ground, how it came into Islam, what changed. | *"a map should go first to describe the situation to the audience"* | gate `M1` |
| **M2** | **Two scales.** A theatre map for where; a **close-up** for a battle or a siege. | *"maybe a close up map? showing siege and month passing and trenches?"* | review |
| **M3** | A force's icon **travels** with it, along its arrow. | *"it should show the beaten moving in animation towards darin"* | gate `M3`; `mapkit.march` |
| **M4** | A force is in **one place at a time**; no icon is left where the force no longer is. | *"al jarud is still stuck at the bottom as if he is in the same place all this time"* | gate `M4`; `mapkit.march` |
| **M5** | **Every arrow says who is moving.** | *"the arrow here what does it mean? who went to al khatt here?"* | gate `M5` |
| **M6** | **Every force on the field has an icon — the enemy too.** | *"the enemy army should also have an icon, something to show it is there"* | `mapkit.force`; review |
| **M7** | A **siege is drawn as a siege**; trenches, closed roads and a sea passage are each drawn. | *"there should be some animation to describe a seige"* · *"closing all paths"* · *"the sea passage should be showing"* | `mapkit.siege / trench / sail`; review |
| **M8** | Map lettering is legible from the back of the hall: names 15pt, captions 18pt, as they fall on the slide. | *"the text is tooooo small"* — three times | gate `M8` |
| **M9** | **Nothing sits over the action.** No title box or legend inside the map; the slide's headline is the title. | *"al dahna journey becomes hidden behind the cartoush"* | gate `M9` |
| **M10** | Every mark is on the stage. | found by the gate | gate `M10` |
| **M11** | **Every key names who did the thing** — never a bare *taken*, *besieged*, *settled*. | *"al Qatif, Hajr taken... 'taken by who?'"* | gate `M11` |
| **M12** | **Every place named in a key is on the map**, or is glossed in a few words. | *"where or what is 'al Khatt'??"* | gate `M12` |
| **M13** | Maps build on clicks; a moving card's map is its slide; captions fade when their move is done; a front closes on its own map before the next opens. | #58, #63, #64, #69 | build asserts; `mapkit.say` |
| **M14** | One green for Muslim forces: `#2CB020`. | #58 | gate `M14` |
| **M15** | **Nothing is printed over anything else.** | #64: *"some of the click click maps become too crowded"* | gate `M15` |

**Maps are written, not drawn.** `series/mapkit.py` gives a march, a siege, a trench, a crossing and a caption as
helpers that satisfy the rules by construction: a march retires the icon it leaves behind in the same call; a
caption cannot be given no size. A scene that breaks a rule cannot be saved.

**What is sourced and what is schematic** is said in each scene's script and in the notes of its slide. *Who moved,
in what order, and what happened* is from the page. *Where* a mark stands is often schematic — the page that names
al-Khaṭṭ does not say where it is — and the slide's notes say so.

## 6. Order

| | Rule | His words | Enforced by |
|---|---|---|---|
| **O1** | An evening changes direction **once**, and says so aloud when it does. Forward references go last. | #71: *"going back and forth in timeline unnecessarily again and again maybe would give bad impression"* | review |
| **O2** | **Within a scene, slides run in the order things happened**, checked against the page. | *"didn't this happen before slide 20?"* | review, against the front's page-cited sequence |
| **O3** | **No side-material before the story starts.** | *"6-8 are unnecessary"* | review |

## 7. Images

| | Rule | His words | Enforced by |
|---|---|---|---|
| **I1** | Every image placeholder carries an **authored, paste-ready IMAGE BRIEF** at the foot of its notes, and the evening ships `IMAGE_BRIEFS.md` listing them all. | *"where is the escription that i should use to generate this image via image generator?"* | gate `I1`; build refuses a placeholder with no brief |
| **I2** | A brief asks for **places, animals and objects — never a person, never a face.** | proposed 2026-10-08 for this room; ⬜ Daniyal to confirm | gate `I2` |
| **I3** | White ground, so the picture sits on the slide with no seam. | #21 | the brief's house style |

## 8. The Line

| | Rule | His words | Enforced by |
|---|---|---|---|
| **L1** | **One or two strands, eight events at most.** Anything finer belongs on a map. | *"the timeline has to be simplified, atm its too many merged. maybe a short general timeline with one or two strands would be ok"* | gate `L1` |

## 9. Faith

| | Rule | His words | Enforced by |
|---|---|---|---|
| **D1** | A **duʿāʾ, a prayer and the manner of it, words of trust in Allah** recorded in the source get **a slide of their own** — the Arabic on the face, large — and are told slowly. | *"the duas and the manner of prayer as well should be described … the three arabic questiosn should have their own slide"* | gate `D1`; `IMAN` in `build.py` |
| **D2** | **Mine the pages for the line.** When a page is read, look for the short Arabic sentence that could be said aloud to a room — and card it as a statement, not as a sub-note. | *"they could give some amazing or catchy lines for motivating people and boosting their iman if delivered in arabic, please do consider this as well as part of vision"* | review, at carding |
| **D3** | Sourcing does not relax. Narrate it as the book narrates it, give the page, keep the caution to one line in the notes, and build no ruling on it. | CLAUDE.md §1.1, §1.6 | `check_citations`; review |

Evening 6's first pass at D2 found, on pages already cached: *"Then rejoice — by Allah, Allah does not abandon
those who are in a state like yours"* (⁨البدایہ ج۷ ص۳۹⁩), and *"Allah has shown you His signs on land, that you may
take heed by them at sea"* (⁨الکامل ج۲ ص۲۲۴⁩). Both had been sitting in sub-notes under a map.

## 10. Sourcing, and the shape of a deck

Unchanged, and enforced where they always were: airtight references (`check_citations`), well-formed cards
(`check_cards`), nobody on stage un-introduced (`check_introductions`), one slide per card at spoken density (#39),
the over-built pool and the measured pace (#20), a deck Daniyal has edited is his (#67).

---

## The gates, in the order to run them

```bash
python tools/check_citations.py L02_baarah_saal/CONTENT.md   # every Arabic quotation against its page
python tools/check_cards.py L02_baarah_saal                  # card structure
python tools/check_introductions.py SNN_<slug>               # every name, answered
python SNN_<slug>/scenes.py                                  # maps through mapkit: a rule-breaking scene cannot be saved
python SNN_<slug>/make_timeline.py && python SNN_<slug>/make_maps.py
python SNN_<slug>/build.py                                   # builds, then runs check_vision and reports
```

**And then look.** The gate passed a close-up that put three forces on one spot until rule M15 was written. It
checks what it has been taught to check. Open the rendered steps of every new map before hand-over; anything the
eye catches that the gate did not is the next rule.
