# -*- coding: utf-8 -*-
"""Build S04.pptx — evening 4: al-Buṭāḥ and al-Yamāma.

    python S04_kinda_butah_yamama/make_timeline.py  # -> visuals/line_s04_*.png   (the Line)
    python S04_kinda_butah_yamama/make_maps.py      # -> scenes + visuals/maps/*.png (the maps)
    python S04_kinda_butah_yamama/build.py          # -> S04.pptx + S04.pdf + IMAGE_BRIEFS.md
    python S04_kinda_butah_yamama/pack_data.py      # -> CUE.pdf, WORKSHEET.pdf, BRIEFING.pdf

THE CUT IS MADE (Daniyal, 2026-09-22 — DECISIONS.md #44): Parts I–IV, ending at STOP C — and PART V
sits BEHIND that close as overflow (#47), so the evening cannot run dry. The STOP C closing set is
emitted in its place, after #31, and the deck goes on: Part V, then the STOP D close. Stopping at STOP C
needs no jump; going on past it is one typed slide number, which CUE.pdf prints.
Ḥaḍramawt/Kinda stays in RUNSHEET.md under "Rolled forward to evening 5", below a `###` heading, so
`runsheet()` does not read it and it is not in this deck.

RUNSHEET.md IS THE RUNNING ORDER, AND THIS FILE READS IT. Only the tables under `## Part` headings are
the evening. Each card comes out of the era pools by id and becomes **ONE SLIDE** through
tools/build_full_deck.card_slide.

THE ORDER IS CHRONOLOGICAL (DECISIONS.md #42), and that is what fixed the seams the first cut had:
the two claimants are introduced before the campaign reaches them, so no card refers forward; the
hinge card E-RC63 carries the army out of the mosque at Medina and onto the road; and Ḥaḍramawt/Kinda
stands where the sources put it — last.

THIS DECK IS BUILT ONE SLIDE PER CARD (DECISIONS.md #39), NOT ONE SLIDE PER BEAT.
Evening 3 was delivered from a 356-slide beat deck and the shape failed in the room: consecutive beat
slides restated the same scene in slightly different words, and the speaker — who tells an event whole
from its first slide — was left visibly clicking past his own deck. So `beat_slide` is not called here.
The card's beats go into the **speaker notes** of its one slide, as the numbered SAY list that
`build_full_deck.notes_for` now prints first (#40). The screen carries the picture; the speaker carries
the sequence.

WHAT THIS FILE ADDS AROUND THE CARDS.
  * Bookend IN — evening 3's STOP B closing pair, unchanged (#23), and one sentence to turn to Kinda.
  * A map slide wherever a Map Studio scene carries the story (MAP_BEFORE). Maps are drawn in the tool.
  * Bookend OUT for STOP C, the planned end — the Line, the map, the عبرت lines, a question. These are
    the slides that open evening 5 (#23).
  * The same closing set for STOP A and STOP B, HIDDEN at the end of the deck (CLAUDE.md §2: a closing
    pair for every stopping point). To close early, type the slide number and press Enter — CUE.pdf
    prints the numbers.

MAPS ARE RENDERED, NOT HAND-EXPORTED. make_maps.py writes the Map Studio scenes and renders every step
through tools/render_scene.py into visuals/maps/<scene>-step-NN.png. A map slide picks up the image for
the LAST step of its range; where no image exists yet it falls back to a placeholder with the brief.
To nudge a map by hand: open the scene in tools/mapstudio/index.html, adjust, Save over the .json, and
re-render it with tools/render_scene.py (re-running make_maps.py regenerates the s04-* scenes and would
undo the nudge).

ONE FACE RULE THIS FILE ENFORCES BEYOND deck2.audit().
  * `ATA/E-TB19`'s research title and narrative are clean, but the pages behind it are not: the
    meeting of the two claimants at البدایہ ج۷ ص۲۹–۳۰ is explicitly obscene. The card's own ⚠ carries
    that; the face is given a plain headline so nothing on screen invites the question.
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "series"))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import deck2 as D                                                   # noqa: E402
import build_full_deck as B                                         # noqa: E402

VIS = os.path.join(HERE, "visuals")
MAPS = os.path.join(VIS, "maps")
SCENES = "tools/mapstudio/scenes/"

# Names the shared TRANSLIT table does not yet carry (it has al-Kāmil, al-Buṭāḥ and ʿAqrabāʾ already).
for _pair in (("النُّجَير", "al-Nujayr"), ("مالك بن نويرة", "Malik b. Nuwayra"),
              ("الرَّجّال بن عُنْفوة", "al-Rajjal b. Unfuwa")):
    if _pair not in B.TRANSLIT:
        B.TRANSLIT.append(_pair)

# Plain headlines where the research title would mislead, mix scripts, or wrap onto two lines.
FACE_TITLE = {
    "RCT/E-RC33": "The she-camel called Shadhra",
    "TSY/E-YK08": "The humbled man",
    "RCT/E-RC34": "al-Nujayr: the name he forgot to write",
    "KTK/E-KD02": "al-Hira given, al-Hira taken back",
    "KTK/E-KD03": '"Far from us in lineage"',
    "KTK/E-KD06": '"The four kings"',
    "KTK/E-KD07": "al-Ashath after the pardon",
    "RCT/E-RC44": "The Anṣār who would not march",
    "RCT/E-RC45": "Mālik b. Nuwayra ؓ stands apart",           # no comma after ؓ: it is a combining mark
    "RCT/E-RC48": "One night, four accounts",
    "RCT/E-RC51": "The historian's own verdict",
    # nothing on the face may invite a question about the pages behind this card
    "ATA/E-TB19": "What her claim was worth",
    "ATA/E-TB12": '"A liar of Rabīʿa"',
    # the research title runs past the nine-word headline cap and would be cut with an ellipsis
    "RCT/E-RC47": "The patrol could not agree",
    "RCT/E-RC15": "ʿIkrima ؓ goes too early",
    "RCT/E-RC59": '"A wretched bearer of the Qurʾān"',
    # not "the order that turned the day": STOP C, three slides on, says the day is not yet decided
    "RCT/E-RC19": "Every clan under its own banner",
    # the research title wraps the headline onto a second line; the name moves to the kicker (FACE_WHEN)
    "ATA/E-TB16": "Musaylima at Medina",
    "RCT/E-RC61": '"Adorn the Qurʾān with deeds"',
    # the title ends in عَقْرَباء, which the shared table romanises without its diacritics
    "RCT/E-RC16": "The tent and the prisoner",
    "RCT/E-RC53": "And then it happened again",
    "RCT/E-RC55": "The order of battle",
    "RCT/E-RC57": "The man who made the lie believable",
    "RCT/E-RC62": "Khālid ؓ between the lines",
    "RCT/E-RC63": "Excused, and sent to al-Yamāma",
    "RCT/E-RC64": "There were Muslims inside already",
    # Part V
    "RCT/E-RC20": "Ḥadīqat al-Mawt — over the wall",
    # Parts VI–VIII — al-Dhahabī رحمہ اللہ gives AS17 with «وقيل»; the hedge belongs on the face itself
    "AHA/E-AS17": "It is said they were found together",
    "AHA/E-AS13": "The banner changed hands",
    "AHA/E-AS14": "Two men who dug a pit",
    "ZIA/E-ZY4": "The man who killed Zayd ؓ",
    # Parts IX–XI. AS05 and AS10 carry "⚠ SPEAKER'S DISCRETION" in the research title — off the face.
    "AHA/E-AS05": "The sentence he feared for ten years",
    "AHA/E-AS10": "The adoption undone",
    "AHA/E-AS08": "He took his cloak and went out to listen",
    "THO/E-HS12": "Why he came to that house",
    # the card title is the whole question; the face takes the half that carries it
    "RCT/E-RC65": "«A thing the Prophet ﷺ did not do»",
    "RCT/E-RC21": "The death of Musaylima",
    "RCT/E-RC23": "Zayd b. al-Khaṭṭāb ؓ and his brother",       # no comma after ؓ: a combining mark
    "TSY/E-YK19": "al-Ashath b. Qays comes into it",
}
# The face's date line is the first six words of the card's When; where that cut misleads, say it plainly.
FACE_WHEN = {
    "TSY/E-YK07": "11 AH, Hadramawt",
    "RCT/E-RC33": "11–12 AH, Hadramawt",
    "RCT/E-RC34": "11 or 12 AH",
    "TSY/E-YK16": "al-Qadisiyya to Nahawand",
    "KTK/E-KD01": "before Islam — an estimate",
    "KTK/E-KD02": "before Islam — an estimate",
    "KTK/E-KD03": "before Islam — an estimate",
    "KTK/E-KD05": "10 AH",
    "KTK/E-KD07": "12–40 AH",
    "RCT/E-RC44": "11 AH",
    "RCT/E-RC45": "11 AH",
    "RCT/E-RC46": "11 AH",
    "RCT/E-RC47": "11 AH",
    "RCT/E-RC48": "11 AH — the books disagree",
    "RCT/E-RC49": "11 AH, Medina",
    "RCT/E-RC50": "11 AH, Medina",
    "RCT/E-RC51": "the historian's own comment",
    "RCT/E-RC52": "ʿUmar's ؓ caliphate",
    "ATA/E-TB15": "End of 10 AH",
    "ATA/E-TB16": "in the Prophet's ﷺ lifetime",
    "ATA/E-TB12": "11–12 AH, al-Yamāma",
    "ATA/E-TB18": "11 AH",
    "ATA/E-TB19": "11 AH, and afterwards",
    "RCT/E-RC15": "11 AH, al-Yamāma",
    "RCT/E-RC53": "11 AH, al-Yamāma",
    "RCT/E-RC54": "11–12 AH",
    "RCT/E-RC16": "11–12 AH",
    "RCT/E-RC55": "11–12 AH — the books disagree",
    "RCT/E-RC56": "11–12 AH — attribution disputed",
    "RCT/E-RC17": "11–12 AH, ʿAqrabāʾ",
    "RCT/E-RC57": "11–12 AH, ʿAqrabāʾ",
    "RCT/E-RC58": "11–12 AH, ʿAqrabāʾ",
    "RCT/E-RC18": "11–12 AH, ʿAqrabāʾ",
    "RCT/E-RC60": "11–12 AH, ʿAqrabāʾ",
    "RCT/E-RC61": "The other wing: Abū Ḥudhayfa ؓ",            # the kicker is cut at six words
    "RCT/E-RC59": "Sālim ؓ with the Muhājirūn's banner",
    "RCT/E-RC62": "11–12 AH, ʿAqrabāʾ",
    "RCT/E-RC19": "11–12 AH, ʿAqrabāʾ",
    "RCT/E-RC63": "11 AH, Medina",
    "RCT/E-RC64": "11 AH, before Khālid ؓ arrived",
    "RCT/E-RC20": "11–12 AH, ʿAqrabāʾ",
    "RCT/E-RC21": "11–12 AH, ʿAqrabāʾ",
    "RCT/E-RC22": "12 AH, the forts of al-Yamāma",
    "RCT/E-RC23": "12 AH, Rabīʿ I",
    "RCT/E-RC37": "12 AH, Medina",
    # Part VI
    "AHA/E-AS09": "In the Prophet's ﷺ lifetime",
    "AHA/E-AS15": "12 AH, at al-Yamāma",
    "AHA/E-AS16": "12 AH, at al-Yamāma",
    "AHA/E-AS17": "12 AH, after al-Yamāma",
    "THO/E-HS14": "ʿUmar's ؓ caliphate, 13–23 AH",
    "THO/E-HS15": "Undated",
    "ZIA/E-ZY17": "12 AH, after the battle",
    "AHA/E-AS13": "12 AH, at al-Yamāma",
    "AHA/E-AS14": "12 AH, at al-Yamāma",
    "AHA/E-AS18": "23 AH, Medina",
    "AHA/E-AS19": "After 12 AH",
    "ZIA/E-ZY8": "Medina, and 12 AH",
    "ZIA/E-ZY9": "11 AH Medina → 12 AH al-Yamāma",
    "ZIA/E-ZY4": "12 AH, and after it at Medina",
    "ZIA/E-ZY12": "12 AH, at al-Yamāma",
    "ZIA/E-ZY13": "12 AH, at al-Yamāma",
    "ZIA/E-ZY14": "12 AH, at al-Yamāma",
    "ZIA/E-ZY15": "11–12 AH",
    "ZIA/E-ZY16": "12 AH, and al-Yarmūk after it",
    "ZIA/E-ZY18": "12 AH, at al-Yamāma",
    "RCT/E-RC65": "12 AH, Medina",
    # Parts IX–XI — backstory, so every date line says plainly how far back we have gone
    "THO/E-HS1": "Before the Hijra, at Medina",
    "THO/E-HS2": "1 AH, soon after the Hijra",
    "THO/E-HS3": "1–11 AH",
    "THO/E-HS4": "Uḥud, 3 AH",
    "THO/E-HS5": "Uḥud, 3 AH",
    "THO/E-HS6": "Uḥud, 3 AH",
    "THO/E-HS7": "Ḥunayn, 8 AH",
    "THO/E-HS8": "Uḥud, 3 AH",
    "THO/E-HS9": "At Medina",
    "THO/E-HS10": "At Medina",
    "THO/E-HS11": "Biʾr Maʿūna, 4 AH",
    "THO/E-HS12": "After Biʾr Maʿūna, 4 AH",
    "THO/E-HS13": "In the Prophet's ﷺ lifetime",
    "THO/E-HS17": "Tustar, 17–20 AH",
    "THO/E-HS18": "Tustar, the same morning",
    "THO/E-HS19": "The caliphate of ʿUthmān ؓ",
    "AHA/E-AS01": "Mecca, before the Hijra",
    "AHA/E-AS02": "Mecca, before the house of al-Arqam",
    "AHA/E-AS03": "Badr, 2 AH",
    "AHA/E-AS04": "Badr, 2 AH",
    "AHA/E-AS05": "Badr, 2 AH",
    "AHA/E-AS06": "Before the Hijra",
    "AHA/E-AS07": "Before the Prophet ﷺ reached Medina",
    "AHA/E-AS08": "At Medina",
    "AHA/E-AS10": "At Medina",
    "ZIA/E-ZY10": "Medina, after al-Ḥujurāt",
    "TSY/E-YK19": "11 AH, Hadramawt",
}

# card id -> (headline, scene file, steps, key rows). The map slide goes BEFORE that card, and shows only
# what that card's own events draw — never a later card's. The Part V–VI rows left with the cut (#44);
# the FACE_TITLE / FACE_WHEN rows for those cards stay above, inert, so the cards read the same when
# they are built on evening 5.
MAP_BEFORE = {
    "ATA/E-TB18": ("Sajāḥ comes down from the north", "s04-01-sajah.json", "1–3",
                   [("al-Jazīra", "where she came from"), ("al-Yamāma", "where she turned back")]),
    "RCT/E-RC64": ("al-Yamāma before the army came", "s04-02-al-yamama-before.json", "1–2",
                   [("Ḥajr", "the town"), ("Thumāma ؓ", "of Banū Ḥanīfa itself")]),
    "RCT/E-RC44": ("From Buzākha to al-Buṭāḥ", "s04-03-buzakha-to-al-butah.json", "1–2",
                   [("Buzākha", "where evening 2 stopped"), ("al-Buṭāḥ", "the third stop in the orders")]),
    "RCT/E-RC49": ("Back to Medina", "s04-04-back-to-medina.json", "1",
                   [("To Medina", "Khālid ؓ is sent for")]),
    "RCT/E-RC63": ("Out again, to al-Yamāma", "s04-05-medina-to-al-yamama.json", "1–2",
                   [("To al-Yamāma", "the army, and the reserve behind it")]),
    "RCT/E-RC15": ("Two commanders sent ahead", "s04-06-two-commanders.json", "1–3",
                   [("ʿIkrima ؓ", "beaten, then sent on to Oman"), ("Shuraḥbīl ؓ", "halted on the road")]),
    "RCT/E-RC54": ("ʿAqrabāʾ, and the ground behind it", "s04-07-aqraba.json", "1–2",
                   [("ʿAqrabāʾ", "the enemy camp"), ("The farmland", "behind their own line")]),
    "RCT/E-RC19": ("The line re-formed", "s04-07-aqraba.json", "4–5",
                   [("Clan by clan", "Muhājirūn, Anṣār, the tribes")]),
    "RCT/E-RC20": ("Into the garden", "s04-07-aqraba.json", "6",
                   [("The garden", "the gate shut behind them")]),
    "RCT/E-RC21": ("The gate opens", "s04-07-aqraba.json", "7",
                   [("al-Barāʾ ؓ", "over the wall, and the gate"), ("al-Yamāma", "taken")]),
}

# THE FACE EXCERPT for a quotation too long to project whole (review, 2026-09-22). The builder used to cut
# every rendering at 24 words, blind, and the room read "…he had meant nothing but…" under a complete
# Arabic line. Each excerpt below keeps the clause the card exists for, cuts the Arabic and the English at
# the same place, and marks every cut with "…". check_face_quotes() refuses a build in which any segment
# is not the card's own words. The notes still carry the whole quotation. Cards not listed fit whole.
FACE_QUOTE = {
    # the reply, not the letter: the room should not read a claim with nothing on screen answering it
    "ATA/E-TB15": ("فإنَّ الأرضَ لله يُورِثُها منْ يَشاءُ من عباده والعاقبة للمتقين",
                   "…the earth belongs to Allah; He gives it in inheritance to whomever He wills of His "
                   "servants; and the outcome is for those who fear Him."),
    "ATA/E-TB16": ("لو سألتني هذه القطعة ما أعطيتكها",
                   "If you asked me for this piece, I would not give it to you…"),
    "ATA/E-TB12": ("فقال أشهد أنَّك كذّابٌ وأن محمدًا صادقٌ، ولكن كذّابَ رَبيعة أحبُّ إلينا من صادقِ مُضَر",
                   "He said: I bear witness that you are a liar and that Muḥammad ﷺ is truthful — but a liar "
                   "of Rabīʿa is dearer to us than a truthful man of Muḍar."),
    "ATA/E-TB18": ("إذ أقبلت سجاح … التغلبية من الجزيرة، وهي من نصارى العرب، وقد ادَّعتِ النبوَّة",
                   "…Sajāḥ … al-Taghlibiyya came forward from al-Jazīra — and she was of the Christians of "
                   "the Arabs — having claimed prophethood."),
    # ends before «إلى زمان معاوية»: the room has not met him (runsheet, Introductions checked)
    "ATA/E-TB19": ("فكرَّتْ راجعةً إلى الجزيرة بعدما قبضَتْ من مسيلمة نصفَ خراجِ أرضِهِ",
                   "…she went back to al-Jazīra after she had taken from Musaylima half the kharāj of his "
                   "land…"),
    "RCT/E-RC46": ("إِنَّا دُعِينَا إِلَى هَذَا الْأَمْرِ فَأَبْطَأْنَا عَنْهُ فَلَمْ نُفْلِحْ … فَتَفَرَّقُوا وَادْخُلُوا فِي هَذَا الْأَمْرِ",
                   "…we were called to this matter and we were slow to it and did not prosper … Disperse, and "
                   "enter into this matter."),
    # both halves of the patrol: Part II is a disagreement, never one side of it
    "RCT/E-RC47": ("فشهد أبو قتادة - الحارث بن ربعي الأنصاري - أنهم أقاموا الصلاةَ، وقال آخرون: إنهم لم يُؤَذّنوا ولا صَلّوا",
                   "…Abū Qatāda al-Anṣārī — al-Ḥārith b. Ribʿī — testified that they had established the "
                   "prayer, and others said they had neither given the adhān nor prayed."),
    "RCT/E-RC52": ("فَقَالَ مُتَمِّمٌ: … لَوْ كَانَ أَخِي صُرِعَ مَصْرَعَ أَخِيكَ لَمَا بَكَيْتُهُ. فَقَالَ عُمَرُ: مَا عَزَّانِي أَحَدٌ بِأَحْسَنَ",
                   "Mutammim said: … had my brother fallen where your brother fell, I would not have wept for "
                   "him. ʿUmar said: No one has ever consoled me better…"),
    "RCT/E-RC63": ("لما رضيَ الصدِّيقُ عن خالد بن الوليد وعذَرَهُ بما اعتذرَ به، بعثَه إلى قتالِ بني حنيفة باليمامة",
                   "When the Ṣiddīq was satisfied with Khālid b. al-Walīd and accepted the excuse he made, he "
                   "sent him to fight Banū Ḥanīfa at al-Yamāma."),
    # the Ḥudhayfa of this letter is not Abū Ḥudhayfa ؓ of #29; the face does not name him
    "RCT/E-RC15": ("لَا أَرَيَنَّكَ وَلَا تَرَانِي، لَا تَرْجِعَنَّ فَتُوهِنَ النَّاسَ … فَقَاتِلْ أَهْلَ عُمَانَ وَمَهْرَةَ",
                   "Let me not see you and do not you see me. Do not come back and weaken the people … fight "
                   "the people of ʿUmān and Mahra…"),
    "RCT/E-RC16": ("أيها الرجل إن كنتَ تريد بأهل اليمامة غدًا خيرًا أو شرًا فاستبق هذا الرجل",
                   "Man — if you intend anything tomorrow for the people of Yamāma, good or ill, keep this man "
                   "alive…"),
    # all three banners: the card's point is that the books name the men and not the chart
    "RCT/E-RC55": ("ورايةُ المهاجرين مع سالم … ورايةُ الأنصار مع ثابت بن قيس … والعرب على راياتها",
                   "The Muhājirūn's banner was with Sālim … the Anṣār's banner with Thābit b. Qays … and the "
                   "Arabs each under their own banners."),
    # his answer is the slide's title; the automatic cut took it off the face
    "RCT/E-RC59": ("أتخشى أن نؤتى من قبلك؟ فقال: بئس حامل القرآن أنا إذًا.",
                   "…Do you fear we shall be broken from your side? He said: A wretched bearer of the Qurʾān I "
                   "should be, then."),
    "RCT/E-RC56": ("اليوم يوم الغيرة، اليوم إن هُزمتم تُستنكح النساء سَبيّاتٍ … فقاتلوا عن أحسابكم، وامنعوا نساءكم.",
                   "Today is the day of honour. Today, if you are routed, the women will be taken as captives … "
                   "So fight for your own standing, and protect your women."),
    "RCT/E-RC17": ("فكانت جولة … حتى دخلت بنو حنيفة خيمةَ خالد بن الوليد وهمّوا بقتل أم تميم، حتى أجارها مجاعة",
                   "There was a rout … Banū Ḥanīfa entered Khālid b. al-Walīd's own tent and were minded to "
                   "kill Umm Tamīm — until Mujjāʿa gave her his protection…"),
    # the face does not project the claim about the Prophet ﷺ; the speaker tells it
    "RCT/E-RC57": ("فَكَانَ أَعْظَمَ فِتْنَةً عَلَى بَنِي حَنِيفَةَ مِنْ مُسَيْلِمَةَ … فَصَدَّقُوهُ وَاسْتَجَابُوا لَهُ",
                   "He was a greater fitna upon Banū Ḥanīfa than Musaylima … and they believed him and answered "
                   "him."),
    "RCT/E-RC18": ("هَكَذَا عَنْ وُجُوْهِنَا نُقَارِعُ القَوْمَ … مَا هَكَذَا كُنَّا نُقَاتِلُ مَعَ رَسُوْلِ اللهِ ﷺ.",
                   "Get out of our faces so we can strike the enemy … This is not how we used to fight "
                   "alongside the Messenger of Allah ﷺ."),
    "RCT/E-RC60": ("والله لا أتكلَّمُ حتى يهزمهم اللهُ أو ألقىَ اللهَ فأكلِّمه بحجَّتي",
                   "…By Allah, I will not speak until Allah routs them, or I meet Allah and speak to Him with "
                   "my case."),
    # the watchword stays in the notes, the speaker's to say or not (runsheet #30)
    "RCT/E-RC62": ("أنا ابن الوليد العَوْد، أنا ابن عامر وزيد … وجعل لا يبرز لهم أحدٌ إلا قتله",
                   "I am the son of al-Walīd the seasoned; I am the son of ʿĀmir and Zayd … and no one came out "
                   "against him but he killed him."),
    # the letter, and what he did with it — the cut had left the face on the order to kill
    "RCT/E-RC22": ("وَوَصَلَ كِتَابُ أَبِي بَكْرٍ إِلَى خَالِدٍ أَنْ يَقْتُلَ كُلَّ مُحْتَلِمٍ … فَوَفَى لَهُمْ وَلَمْ يَغْدِرْ.",
                   "And Abū Bakr's letter reached Khālid, ordering him to kill every man who had reached "
                   "puberty … so he kept faith with them and did not betray them."),
    # the dialogue: the order, the objection, the three words. The honorific is spelled out because
    # that is how the سیر page prints it, and the quotation is verbatim or it is not a quotation.
    "RCT/E-RC65": ("فَتَتَبَّعِ القُرْآنَ، فَاجْمَعْهُ. فَقُلْتُ: كَيْفَ تَفْعَلُوْنَ شَيْئاً لَمْ يَفْعَلْهُ رَسُوْلُ اللهِ … قَالَ: هُوَ -وَاللهِ- خَيْرٌ.",
                   "…so follow the Qurʾān up and gather it. I said: How do you do a thing the Messenger "
                   "of Allah ﷺ did not do? … He said: By Allah, it is good."),
    # the order itself. The reciters clause is ZY17's face, one slide earlier (#43).
    "RCT/E-RC37": ("أمرَ الصديق زيدَ بن ثابتٍ أن يجمعَ القرآن من اللِّخاف والعُسُب وصدور الرجال",
                   "…al-Ṣiddīq ordered Zayd b. Thābit to gather the Qurʾān from the flat stones and the "
                   "palm-stalks and the breasts of men."),
    # ——— Part VI. ZY2 is not here: it is RC60's own event, told at #28.
    # ⚠ the four names stay off the face: ابن کثیر quotes only the opening clause (QA_BANK §5.3)
    "AHA/E-AS09": ("قال فيهم رسول الله ﷺ: \"استقرئوا القرآنَ من أربعةٍ\" فذكر منهم سالمًا مولى أبي حذيفة",
                   "…of whom the Messenger of Allah ﷺ said: 'Take the Qurʾān from four' — and he "
                   "mentioned Sālim, the freedman of Abū Ḥudhayfa."),
    # both cut at the same place, and the āya is never cut in the middle
    "AHA/E-AS15": ("… فاحتضنها وهو يقول: ﴿وَمَا مُحَمَّدٌ إِلَّا رَسُولٌ قَدْ خَلَتْ مِنْ قَبْلِهِ الرُّسُلُ﴾",
                   "…so he clasped it to his chest, saying: ﴾Muḥammad is no more than a Messenger; "
                   "messengers have passed away before him﴿."),
    # ⚠ «فلان» stays «so-and-so»: the second man is not named on the page, so he is not named here
    "AHA/E-AS16": ("ما فعل أبو حُذَيْفة؟ قالوا: قُتل … قال: فأضجعوني بينهما",
                   "What has become of Abū Ḥudhayfa? They said: He has been killed … He said: Then lay "
                   "me down between the two of them."),
    "AHA/E-AS17": ("وَقِيْلَ: إِنَّ سَالِماً وُجِدَ هُوَ وَمَوْلاَهُ أَبُو حُذَيْفَةَ، رَأْسُ أَحَدِهِمَا عِنْدَ رِجْلَي الآخَرِ صَرِيْعَيْنِ",
                   "And it is said: Sālim was found, he and his patron Abū Ḥudhayfa, the head of one of "
                   "them at the feet of the other."),
    # the hand-off, which is the whole card; the first clause is beat 1
    "AHA/E-AS13": ("… ثُمَّ قَاتَلَ حَتَّى قُتِلَ، فَوَقَعَتْ الرَّايَةُ، فَأَخَذَهَا سَالِمٌ مَوْلَى أَبِي حُذَيْفَةَ",
                   "…and then fought until he was killed. The banner fell — and Sālim, the freedman of "
                   "Abū Ḥudhayfa, took it up."),
    "AHA/E-AS14": ("ما هكذا كنَّا نقاتلُ مع رسول الله ﷺ … فقاتلا حتى قُتلا",
                   "This is not how we used to fight alongside the Messenger of Allah ﷺ … and fought "
                   "until they were killed."),
    "AHA/E-AS18": ("قال لما احتُضِر: لو كانَ سالمٌ حيًّا لما جعلتها شُورى",
                   "…when death was upon him: Had Sālim been alive I would not have made it a shūrā."),
    # ⚠ the cut is where the name is: the printed page gives it two ways, so it is not read aloud (§4.2)
    "AHA/E-AS19": ("وقد بعثَ عمرُ بميراثه إلى مولاته التي أعْتَقَتْه … فردَّتْه وقالتْ: إنّما أعْتَقَتْهُ سائبةٌ",
                   "ʿUmar sent his inheritance to the woman who had freed him … and she sent it back and "
                   "said: I freed him only as sāʾiba."),
    "ZIA/E-ZY9": ("مَا أُحِبُّ أَنِّي مُتُّ قَبْلَهُ حَتَّى أُصَدِّقَهُ مَيْتاً، كَمَا صَدَّقْتُهُ حَيّاً",
                  "…do not wish that I had died before him — so that I may confirm him dead as I "
                  "confirmed him alive."),
    "ZIA/E-ZY4": ("وقال لعمر: يا أميرَ المؤمنين إن الله أكرم زيدًا بيدي ولم يُهنِّي على يده.",
                  "…said to ʿUmar: Commander of the Faithful — Allah honoured Zayd at my hand, and did "
                  "not disgrace me at his."),
    "ZIA/E-ZY12": ("فنزعه، وتحزم وأخذ السيف وقاتل حتى قتل، فوجد به جراحات كثيرة.",
                   "…he pulled it out, bound himself up, took his sword and fought until he was killed — "
                   "and many wounds were found on him."),
    # ⚠ the face stops before «لضرب عنقه»: the card's point is the record, not the sentence
    "ZIA/E-ZY13": ("وكان أبوه رأسَ المنافقين، وكان أشدَّ الناس على أبيه",
                   "His father was the head of the hypocrites, and he was the hardest of all people on "
                   "his father."),
    "ZIA/E-ZY14": ("لا أغيّرُ اسمًا سمانيه أبواي، فلم تزل الحزونة فينا … استُشهد يومَ اليمامة",
                   "I will not change a name my parents gave me. So the roughness never left us … He was "
                   "martyred on the day of al-Yamāma."),
    # ⚠ what was done to him is told in the beats, not projected: the face carries the question and the answer
    "ZIA/E-ZY15": ("أتشهدُ أني رسولُ اللَّه؟ فيقول: لا أسمع",
                   "Do you testify that I am the Messenger of Allah? And he would say: I do not hear."),
    # ——— Parts IX–XI ———
    "THO/E-HS1": ("وَلَكِنَّكَ كَافِرٌ، فَإِنْ تُسْلِمْ فَذَلِكَ مَهْرِي، لاَ أَسْأَلُكَ غَيْرَهُ.",
                  "…but you are a disbeliever. If you accept Islam, that is my dower — I ask you for "
                  "nothing else."),
    "THO/E-HS3": ("خدمته صلى الله عليه وسلم عشر سنين، فوالله ما قال لي: أف قط",
                  "I served him ﷺ ten years, and by Allah he never said 'uff' to me once."),
    # the verse as the page quotes it; the reference itself is checked against a muṣḥaf, not printed here
    "THO/E-HS5": ("﴿مِنَ الْمُؤْمِنِينَ رِجَالٌ صَدَقُوا مَا عَاهَدُوا اللَّهَ عَلَيْهِ﴾",
                  "Among the believers are men true to what they pledged to Allah."),
    "THO/E-HS8": ("لاَ تُشْرِفْ، لاَ يُصِيْبُكَ سَهْمٌ، نَحْرِي دُوْنَ نَحْرِكَ.",
                  "…do not look out, lest an arrow strike you. My throat before your throat."),
    "THO/E-HS10": ("إِنَّ أَحَبَّ أَمْوَالِي إِلَيَّ بَيْرُحَاءُ، وَإِنَّهَا صَدَقَةٌ للهِ … فَقَالَ: (بَخٍ! ذَلِكَ مَالٌ رَابِحٌ",
                   "The dearest of my property to me is Bayruḥāʾ, and it is a ṣadaqa for Allah … He "
                   "said: 'Bakhkh! That is profitable property."),
    # the ellipsis is the page break, not an omission — the clause runs over ج۲ ص۳۰۶–۳۰۷
    "THO/E-HS12": ("إِنِّي أَرْحَمُهَا، قُتِلَ … أَخُوْهَا مَعِي",
                   "I have compassion for her — her brother was killed with me."),
    "THO/E-HS13": ("عُرِضَ عَلَيَّ نَاسٌ مِنْ أُمَّتِي يَرْكَبُوْنَ ظَهْرَ هَذَا البَحْرِ كَالمُلُوْكِ … عَلَى الأَسِرَّةِ",
                   "People of my umma were shown to me riding the back of this sea like kings … upon "
                   "thrones."),
    "THO/E-HS17": ("اللَّهُمَّ اهْزِمْهُمْ لَنَا وَاسْتَشْهِدْنِي.",
                   "…O Allah, defeat them for us, and take me as a martyr."),
    "THO/E-HS18": ("فما صلوا الصبح إلا بعد طلوع الشمس فما أحب أن لي بتلك الصلاة حمرَ النعم.",
                   "did not pray Ṣubḥ until after sunrise — and I would not wish red camels in exchange "
                   "for that prayer."),
    "AHA/E-AS01": ("فاستأجروا سفينةً بنصف دينار إلى الحبشة … وأبو حُذيفة بن عتبة، وامرأته سهلة بنت سُهيل",
                   "So they hired a ship for half a dinar to Abyssinia … and Abū Ḥudhayfa b. ʿUtba and "
                   "his wife Sahla bt. Suhayl"),
    "AHA/E-AS02": ("السَّيِّدُ الكَبِيْرُ، الشَّهِيْدُ، أَبُو حُذَيْفَةَ ابْنُ شَيْخِ الجَاهِلِيَّةِ: عُتْبَةَ بنِ رَبِيْعَةَ … البَدْرِيُّ",
                   "The great chief, the martyr, Abū Ḥudhayfa — son of the elder of the Jāhiliyya, "
                   "ʿUtba b. Rabīʿa — … the man of Badr."),
    "AHA/E-AS04": ("لعلك قد دخلك من شأن أبيك شيء … ما شككت في أبي ولا في مصرعه",
                   "Perhaps something has entered you about the matter of your father? … I have not "
                   "doubted my father nor where he fell."),
    "AHA/E-AS05": ("ولا أزالُ منها خائفًا إلّا أن تُكفّرها عنّي الشهادةُ، فقُتل يوم اليمامة شهيدًا",
                   "…I shall not stop fearing it unless martyrdom wipes it away from me. And he was "
                   "killed a martyr on the day of al-Yamāma."),
    "AHA/E-AS07": ("فَأَمَّهُم سَالِمٌ مَوْلَى أَبِي حُذَيْفَةَ، لأَنَّهُ كَانَ … أَكْثَرَهُم قُرْآناً، فِيْهِم عُمَرُ",
                   "Sālim, the freedman of Abū Ḥudhayfa, led them in prayer, because he had the most "
                   "Qurʾān of them — among them ʿUmar."),
    "AHA/E-AS08": ("فَإِذَا هُوَ سَالِمٌ مَوْلَى أَبِي حُذَيْفَةَ … (الحَمْدُ لِلِّهِ الَّذِي جَعَلَ فِي أُمَّتِي مِثْلَكَ)",
                   "…and it was Sālim, the freedman of Abū Ḥudhayfa … 'Praise be to Allah, who has put "
                   "the like of you in my ummah.'"),
    # ⚠ the niece's name stays off the face; the beats carry it
    "AHA/E-AS10": ("وقد تَبنّاهُ أبو حُذَيْفة وزوَّجَهُ بابنةِ أخيه … فلما أنزل الله ﴿ادْعُوهُمْ لِآبَائِهِمْ﴾",
                   "Abū Ḥudhayfa had adopted him and married him to his brother's daughter … Then Allah "
                   "sent down: ﴾Call them by their fathers﴿."),
    # ⚠ ONE of four names (QA_BANK §5.3): the face says so in its own headline, and the notes repeat it
    "ZIA/E-ZY18": ("وَابْنُهَا الآخَرُ عَبْدُ اللهِ بنُ زَيْدٍ المَازِنِيُّ … وَهُوَ الَّذِي قَتَلَ مُسَيْلِمَةَ الكَذَّابَ بِسَيْفِهِ.",
                   "Her other son, ʿAbd Allāh b. Zayd al-Māzinī … and he is the one who killed "
                   "Musaylima the liar with his sword."),
    # ⚠ only what he interpreted, never the dream's own words
    "ZIA/E-ZY16": ("بأنه سيقتل ويدفن، وأن ابنه يحرص على الشهادةِ فلا ينالُها عامَه ذلك",
                   "…that he would be killed and buried, and that his son would press for martyrdom and "
                   "not attain it that year."),
    "RCT/E-RC19": ("امْتَازُوا أَيُّهَا النَّاسُ لِنَعْلَمَ بَلَاءَ كُلِّ حَيٍّ … قَالَ بَعْضُهُمْ لِبَعْضٍ: الْيَوْمَ يُسْتَحَى مِنَ الْفِرَارِ.",
                   "Separate out, people, so we may know what each clan is worth … they said to one another: "
                   "Today, running is shameful."),
}

# A card whose face is the four accounts side by side, not one of them. #11 used to project Ibn
# al-Athīr's gloss alone — the account that clears Khālid ؓ — at the centre of a part that is never a
# verdict. Rows are (label, sub); every word is the card's own or the campaign note's §5.7(d) table.
FACE_DIAGRAM = {
    "RCT/E-RC48": ([("The cold night", "al-Bidāya: the crier's \"warm your prisoners\" taken as an order "
                                        "to kill. al-Kāmil: only warmth was meant"),
                    ("Summoned", "al-Bidāya, \"it is said\": reproached over Sajāḥ and the zakāt, then an "
                                 "order to strike"),
                    ("Heard, then ordered", "Siyar: Abū Qatāda ؓ spoke for him; Khālid ؓ disliked what was "
                                            "said, and ordered the blow"),
                    ("Quarter given?", "Siyar, from al-Zuhrī: arms laid down; Abū Qatāda ؓ said quarter was "
                                       "given, the rest said not")],
                   "Four accounts in the books. We record them, and we do not choose."),
}

# BRIDGES — the seams between cards (Daniyal, 2026-09-22: "fast shift between slides, without filling in
# the missing details in between"). One slide before the card named, and before its map if it has one,
# so the room hears where it is before it sees where it goes. Three steps each —
# where we were, what happened, where we are going — every line from the cards named in the comment,
# and the sentence to say in the notes.
BRIDGE_BEFORE = {
    # evenings 2 and 3 as delivered (DELIVERED.md), then TB15/TB18 — the turn back north
    "ATA/E-TB15": ("Tonight: back to the north", "Where the story stands", [
        ("Evening 2", "Khālid ؓ at Buzākha, in Najd: Ṭulayḥa walked off the field"),
        ("Evening 3", "The south: al-Aswad killed in Ṣanʿāʾ, the Yemen restored; Ḥaḍramawt still to come"),
        ("Tonight", "Two claimants still standing in the north: Musaylima at al-Yamāma, and Sajāḥ")],
        "While the south was being settled, the war in the north had never stopped. Two claimants were "
        "still standing: Musaylima of Banū Ḥanīfa at al-Yamāma, and Sajāḥ, coming down from al-Jazīra. "
        "We meet them first, before the armies reach them."),
    # RC05 (the orders at Dhū al-Qaṣṣa), RC09-RC11 (Buzākha, delivered), RC44 — البدایہ ج۷ ص۲۲
    "RCT/E-RC44": ("After Buzākha", "11 AH", [
        ("The orders", "Tied at Dhū al-Qaṣṣa: Ṭulayḥa first; when done, Mālik b. Nuwayra ؓ at al-Buṭāḥ"),
        ("Buzākha", "Done: Ṭulayḥa walked off the field, and the tribes around him came back"),
        ("al-Buṭāḥ", "Next in the orders: the Tamīm country, and Mālik b. Nuwayra ؓ")],
        "We left Khālid ؓ at Buzākha. His orders, tied at Dhū al-Qaṣṣa, were Ṭulayḥa first — and when he "
        "had finished, Mālik b. Nuwayra ؓ at al-Buṭāḥ, if he held out against him. Buzākha was done. So "
        "the army turns towards al-Buṭāḥ.\nThe orders, al-Bidāya vol. 7 p. 22: «عقدَ لخالد بن الوليد وأمره "
        "بطُلَيْحة بن خُوَيْلد، فإذا فرغَ سار إلى مالك بن نُوَيْرَةَ بالبطاح إن أقام له» "
        "(https://shamela.ws/book/30097/3168)."),
    # RC48-RC50 (Part II as told), RC63 — out of the flash-forward and back to 11 AH
    "RCT/E-RC63": ("Back to the mosque, 11 AH", "11 AH, Medina", [
        ("al-Buṭāḥ", "Mālik b. Nuwayra ؓ killed: a night the books tell four ways"),
        ("Medina", "ʿUmar ؓ objects in the mosque; Abū Bakr ؓ: he interpreted, and was mistaken"),
        ("Next", "One claimant still standing: Musaylima, at al-Yamāma")],
        "That consolation came years later, in ʿUmar's ؓ own caliphate. Now back to 11 AH, and to the "
        "mosque at Medina where we left Khālid ؓ being answered for — and then sent straight out again."),
    # RC05, RC15, RC53 — the two commanders who were on this road before Khālid ؓ
    "RCT/E-RC15": ("Meanwhile, at al-Yamāma", "11 AH, before Khālid ؓ arrived", [
        ("One banner", "Of the eleven banners, ʿIkrima ؓ had the one sent against Musaylima"),
        ("Behind him", "Shuraḥbīl b. Ḥasana ؓ, sent to follow him"),
        ("First there", "Both reached al-Yamāma before Khālid ؓ and the main army")],
        "Khālid ؓ was not the first to be sent against Musaylima. Back at Dhū al-Qaṣṣa one of the eleven "
        "banners had gone to ʿIkrima ؓ, with Shuraḥbīl ؓ sent after him — and both reached al-Yamāma "
        "before Khālid ؓ did. Here is what happened to them."),
    # RC49-RC50, RC15/RC53, RC54, RC16 — the re-entry after the worksheet, for anyone who has just come in
    # RC19 (where the close leaves the room), RC20 — the re-entry when the evening goes past STOP C
    "RCT/E-RC20": ("Past the close: the day is decided", "11–12 AH, ʿAqrabāʾ", [
        ("Where we stopped", "The line re-formed, every clan under its own banner, and the day undecided"),
        ("What happens next", "Banū Ḥanīfa give way — and fall back into a walled garden"),
        ("What this last part is", "The garden, the end of Musaylima, the terms at the forts, and one order at Medina")],
        "We have just closed, and we are going on. Where we left it: the line had re-formed, every clan "
        "under its own banner, and the day was not decided. Now it is decided — and what comes out of it "
        "is the reason you can hold a muṣḥaf tonight."),
    # RC59-RC61 (the three at the line, Part IV), RC23 — back to them, and to what came of it
    "AHA/E-AS09": ("The men who did not come back", "11–12 AH, ʿAqrabāʾ", [
        ("At the line", "Sālim ؓ carried the Muhājirūn's banner; Zayd ؓ and Abū Ḥudhayfa ؓ held the wings"),
        ("All three", "Killed on that field, on the same day"),
        ("Still to tell", "What happened at that banner, and the order it led to at Medina")],
        "We met these three at the line: Sālim ؓ with the banner of the Muhājirūn, and on the wings "
        "Zayd b. al-Khaṭṭāb ؓ and Abū Ḥudhayfa ؓ. All three were killed on that field. Now we go back "
        "to the banner itself — because what the books put next to the order given at Medina is what "
        "happened to the man holding it."),
    # AS13-AS19 (the banner thread), ZY8 — the same field, the men beside them
    "ZIA/E-ZY8": ("The same field, the men beside them", "12 AH, ʿAqrabāʾ", [
        ("So far", "The banner: Zayd ؓ, then Sālim ؓ, then the pit, then the two found together"),
        ("Now", "The rest of that line — the pairs, the chiefs, the households"),
        ("Why it is told", "The books name them one by one, and so do we")],
        "That is the banner. But the banner is not the whole line. The books go through that field name "
        "by name, and what they record is not a casualty list — it is households. Here are some of "
        "them."),
    # RC37 and the close, then HS1 — the evening has finished; this is the house those men came from
    "THO/E-HS1": ("Where these men came from", "Before the Hijra, at Medina", [
        ("We have closed", "The evening's story ended at Medina, with the order to gather the Qurʾān"),
        ("What follows is older", "Mecca, Uḥud, Biʾr Maʿūna, Ḥunayn — years before tonight"),
        ("Why", "The men who held the line at ʿAqrabāʾ came out of these houses")],
        "We have finished; the Line does not move again tonight. What follows is older than everything "
        "we have told — it is the houses those men came out of, and we go back to before the Hijra to "
        "start it."),
    # HS19 (the end of that house), AS02 — the second house
    "AHA/E-AS02": ("The second house", "Mecca, before the house of al-Arqam", [
        ("That was one house", "Umm Sulaym's ؓ — Anas ؓ, al-Barāʾ ؓ, and Abū Ṭalḥa ؓ"),
        ("This is another", "A chief's son of Quraysh, and a freed slave of Persia"),
        ("Where they end", "Both of them on the field you have already seen")],
        "That was one house. Here is the other one — and it begins in Mecca, with a man whose father "
        "was one of the great men of Quraysh, and with a slave who came from Persia."),
    # ZY16 (the last of the field), HS14 — the man who went over the wall, and lived
    "THO/E-HS14": ("And one man who lived", "After the battle", [
        ("The garden", "The man who asked to be thrown over the wall was al-Barāʾ b. Mālik ؓ"),
        ("He lived", "Eighty-odd wounds, and Khālid ؓ stayed a month treating them"),
        ("What is left", "What was said about him afterwards — and then the count")],
        "One more, and he is the one who lived. The man who asked to be thrown over the wall of the "
        "garden came out of it with eighty-odd wounds, and Khālid ؓ stayed a month treating him. Here "
        "is what was said about him afterwards."),
    "RCT/E-RC55": ("Where we are", "The night before ʿAqrabāʾ", [
        ("Medina", "Khālid ؓ answered for al-Buṭāḥ, and was kept in command"),
        ("The road", "ʿIkrima ؓ and Shuraḥbīl ؓ beaten ahead of him; forty thousand at ʿAqrabāʾ"),
        ("The tent", "A prisoner in irons in Khālid's ؓ own tent: Mujjāʿa of Banū Ḥanīfa")],
        "After the worksheet — and for anyone who has just come in. Khālid ؓ was called to Medina over "
        "al-Buṭāḥ and kept in command. The two commanders sent ahead of him were both beaten. Forty "
        "thousand men of Banū Ḥanīfa wait at ʿAqrabāʾ, with their farms behind them — and there is a "
        "prisoner in Khālid's ؓ own tent. Morning comes."),
}

# Two cards quote across a page break, so the card's first citation covers only the first clause.
# The face carries the span; the notes and the research note carry both pages separately.
FACE_CITE = {
    "THO/E-HS12": "سیر أعلام النبلاء ج۲ ص۳۰۶–۳۰۷",
    "THO/E-HS13": "سیر أعلام النبلاء ج۲ ص۳۱۶–۳۱۷",
}


# A spare hands-up that asks the room to vote between two Companions' positions has no place in Part II.
NO_HANDS = {"RCT/E-RC50", "THO/E-HS14", "ZIA/E-ZY8"}

# The planned end is not the end of the deck: its closing set goes in after this card, and Part V follows.
CLOSE_C_AFTER = "RCT/E-RC19"

# Two closes sit inside the overflow (#53). STOP D is after the terms at the forts: al-Yamāma is taken,
# the map changes colour, and that is a legitimate end to an evening. STOP E is the full ending after the
# muṣḥaf — and the households (Parts IX–XI) sit behind IT, for evening 5 or for the fifteen minutes the
# speaker stays anyway (#50).
CLOSE_D_AFTER = "RCT/E-RC22"
CLOSE_E_AFTER = "RCT/E-RC37"


def grid_slide(prs, headline, rows, kicker=None, caption=None):
    """Four cards in a 2 x 2 grid: D.diagram_slide puts them in one row, and at a quarter of the slide
    width each the labels broke mid-word ("Summone/d") and the text ran into the caption."""
    s = D.blank(prs)
    D.header(s, headline, kicker)
    gap = D.Inches(0.24)
    cw = D.Emu(int((D.CONTENT_W - gap) / 2))
    ch = D.Emu(int((D.CONTENT_H - D.Inches(0.62) - gap) / 2))
    for i, (label, sub) in enumerate(rows):
        x = D.MARGIN + D.Emu(int((i % 2) * (cw + gap)))
        y = D.CONTENT_Y + D.Emu(int((i // 2) * (ch + gap)))
        D.rect(s, x, y, cw, ch, fill=D.CREAM, name="card%d" % i)
        D.rect(s, x, y, cw, D.Pt(7), fill=D.TEAL)
        D.text(s, label, x + D.Inches(0.22), y + D.Inches(0.16), cw - D.Inches(0.44), D.Inches(0.55),
               size=28, color=D.DARK, font=D.EN, bold=True)
        if D._count_words(sub) > D.MAX_BODY_WORDS:
            raise D.DeckContractError("grid card is %d words, cap is %d: %r"
                                      % (D._count_words(sub), D.MAX_BODY_WORDS, sub))
        D.text(s, sub, x + D.Inches(0.22), y + D.Inches(0.72), cw - D.Inches(0.44), ch - D.Inches(0.8),
               size=D.MIN_PT, color=D.INK, font=D.SANS, line=1.25)
    if caption:
        D.text(s, caption, D.MARGIN, D.H - D.Inches(0.70), D.CONTENT_W, D.Inches(0.5),
               size=D.MIN_PT, color=D.MUTED, font=D.SANS, align=D.PP_ALIGN.CENTER)
    return s


def check_face_quotes(pool):
    """Every segment of every face excerpt is the card's own words — the Arabic harakat aside, the English
    with ﷺ/ؓ aside. A build that fails here has composed something; fix the excerpt, not this check."""
    marks = re.compile("[\u064b-\u0652\u0670\u0640]")
    card = {}
    for d in B.POOLS:
        txt = open(os.path.join(ROOT, d, "CONTENT.md"), encoding="utf-8").read()
        for m in re.finditer(r"^### (\S+) ", txt, re.M):
            end = txt.find("\n### ", m.end())
            card[m.group(1)] = txt[m.end():end if end > 0 else len(txt)]

    def norm(s, arabic):
        s = re.sub(r"(?m)^>\s?", "", s).replace("\u201c", '"').replace("\u201d", '"')
        s = s.replace("\ufdfa", "").replace("\u0613", "").replace("*", "")
        s = marks.sub("", s) if arabic else s
        return re.sub(r"\s+", " ", s)

    bad = []
    for cid, (ar, en) in FACE_QUOTE.items():
        body = card[cid]
        for seg in re.split(r"\s*\u2026\s*", ar):
            seg = seg.strip(" .\u060c")
            if seg and norm(seg, True) not in norm(body, True):
                bad.append("%s Arabic: %s" % (cid, seg))
        for seg in re.split(r"\s*\u2026\s*", en):
            seg = seg.strip(' .,;:"')
            if seg and norm(seg, False) not in norm(body, False):
                bad.append("%s English: %s" % (cid, seg))
    if bad:
        raise SystemExit("FACE_QUOTE is not the card's own words:\n  " + "\n  ".join(bad))


# The عبرت lines for each closing slide, read from the cards so they cannot drift.
# Four, not six: these lines are sentences, and six of them overlap at the lessons slide's row height.
# The planned end draws across the whole evening — Parts I and II, then the two lines of the day
# itself. No closing set uses RC54's line: its "It worked" gives away a day the room has not yet seen
# decided.
LESSON_A = ["ATA/E-TB15", "RCT/E-RC47", "RCT/E-RC50", "RCT/E-RC52"]      # STOP A — al-Butah closed
# not RC16's line at STOP B: "settled the end of the battle" answers the question the close is asking
LESSON_B = ["ATA/E-TB15", "RCT/E-RC47", "RCT/E-RC50", "RCT/E-RC15"]      # STOP B — the armies in position
LESSON_C = ["ATA/E-TB15", "RCT/E-RC50", "RCT/E-RC58", "RCT/E-RC19"]      # STOP C — THE PLANNED END
# STOP D — al-Yamāma taken. The dead have not been told yet, so no line from Parts VI–VIII is used
# here: RC50 (the caliph's three-in-one decision), RC58 (what re-formed the line), RC20 (the wall) and
# RC22 (the terms kept against the letter) are the evening as it stands at #34.
LESSON_D = ["RCT/E-RC50", "RCT/E-RC58", "RCT/E-RC20", "RCT/E-RC22"]
# STOP E — the full ending: RC58 and RC37 are the two halves of one sentence, and AS15 is the man it
# happened to.
LESSON_E = ["RCT/E-RC58", "RCT/E-RC20", "AHA/E-AS15", "RCT/E-RC37"]


def map_image(scene, steps):
    """visuals/maps/<scene>-step-NN for the last step of `steps` ("1–3" -> 03; "all" -> the highest
    step rendered), as a JPEG. None until make_maps.py has rendered it, and the slide keeps its
    placeholder.

    The deck gets a quality-90 JPEG, not the PNG: a Map Studio render is shaded relief and grain, which
    PNG cannot compress — 3–4 MB a map, and the first build with maps in it was a 42 MB deck. The PNGs
    stay beside it as the masters (git-ignored; make_maps.py re-renders them)."""
    slug = os.path.splitext(scene)[0]
    if steps == "all":
        found = sorted(glob.glob(os.path.join(MAPS, slug + "-step-[0-9][0-9].png")))
        png = found[-1] if found else None
    else:
        png = os.path.join(MAPS, "%s-step-%02d.png" % (slug, int(re.findall(r"\d+", steps)[-1])))
    if not png or not os.path.exists(png):
        return None
    jpg = os.path.splitext(png)[0] + ".jpg"
    if not os.path.exists(jpg) or os.path.getmtime(jpg) < os.path.getmtime(png):
        from PIL import Image
        Image.open(png).convert("RGB").save(jpg, "JPEG", quality=90, optimize=True)
    return jpg


UNRENDERED = []


def map_placeholder(prs, headline, scene, steps, keys, kicker=None, hands_first=None):
    image = map_image(scene, steps)
    if not image:
        UNRENDERED.append("%s (step %s)" % (scene, steps))
    s = D.map_slide(prs, image, headline, keys=keys, kicker=kicker, map_frac=0.70,
                    brief="MAP STUDIO, not Gemini: open %s%s, export step(s) %s, place here."
                          % (SCENES, scene, steps))
    first = ("HANDS UP FIRST — ask it before you click to this map, because the map shows the answer:\n"
             + hands_first + "\n\n") if hands_first else ""
    if image:
        D.note(s, first + "MAP: %s%s at step %d, rendered by make_maps.py. The earlier steps are beside it "
                  "in visuals/maps/ if you want the build-up across slides. Sites are approximate; tribal "
                  "names are loose labels." % (SCENES, scene, int(image[-6:-4])))
    else:
        D.note(s, first + "MAP: open %s%s in tools/mapstudio/index.html, export step(s) %s as PNG, and place "
                  "them here (one slide per step if you want the build-up). Sites are approximate; "
                  "tribal names are loose labels." % (SCENES, scene, steps))
    return s


def closing(prs, pool, line_png, scene, question, lesson_cards, keys, hidden=False, stop=""):
    made = []
    s = D.timeline_slide(prs, os.path.join(VIS, line_png), "Tonight on the Line")
    D.note(s, "BOOKEND OUT %s — the Line. Re-used verbatim as next evening's opening slide "
              "(DECISIONS.md #23)." % stop)
    made.append(s)
    made.append(map_placeholder(prs, "Where we stand", scene, "all", keys))
    lines = [B.clean(pool[i]["ibrah"]) for i in lesson_cards]
    s = D.lessons_slide(prs, lines)
    D.note(s, "TONIGHT'S عبرت — say each one, then move on:\n" + "\n".join("%d. %s" % (k, l)
                                                                            for k, l in enumerate(lines, 1)))
    made.append(s)
    s = D.question_slide(prs, question)
    D.note(s, "Ask it, and pause. Then the salām, loudly — and the dua. The room must know it has ended.")
    made.append(s)
    if hidden:
        for x in made:
            x._element.set("show", "0")
    return made


def build():
    pool = B.pool_cards()
    parts = B.runsheet(os.path.join(HERE, "RUNSHEET.md"))
    missing = [cid for _, rows in parts for cid, _ in rows if cid not in pool]
    if missing:
        raise SystemExit("RUNSHEET.md names cards that are not in any pool: %s" % missing)

    prs = D.deck()
    D.title_slide(prs, "al-Buṭāḥ and al-Yamāma", "10–12 AH", "Evening 4")

    # Bookend IN — evening 3's STOP B pair, unchanged
    s = D.timeline_slide(prs, os.path.join(VIS, "line_s04_open.png"), "Where we stopped")
    D.note(s, "BOOKEND IN — evening 3's STOP B Line: the same image its closing slide showed "
              "(DECISIONS.md #23).\nSay: while all of that was happening in the south, the northern war "
              "had never stopped. Tonight we go back to Khālid ؓ, who we last saw at Buzākha. The one "
              "province still grey on your map, Ḥaḍramawt, stays grey tonight — we come back to it when "
              "the northern war has caught up.\n"
              "The map does a loop tonight, and that loop is the truth of the campaign: eleven armies "
              "were moving at once, not one after another.")
    # evening 3's own STOP B scene, unchanged. Its closing map slide was never filled, so it is rendered.
    map_placeholder(prs, "Where we stand", "s03-close-stop-b.json", "all",
                    [("Ṣanʿāʾ", "restored"), ("Ḥaḍramawt", "still to come")],   # evening 3's own keys
                    kicker="From last week")

    check_face_quotes(pool)
    made = no_beats = bridges = 0
    closes = []
    for part, rows in parts:
        D.section_slide(prs, B.clean(part.split(" — ")[0], translit=True),
                        B.clean(part.split(" — ", 1)[1] if " — " in part else "", translit=True) or None)
        for cid, runsheet_note in rows:
            c = dict(pool[cid])
            if cid in FACE_TITLE:
                c["title"] = FACE_TITLE[cid]
            if cid in FACE_WHEN:
                c["when"] = FACE_WHEN[cid]
            if cid in NO_HANDS:
                c["hands"] = "no"
            if cid in FACE_CITE:
                c["cite"] = FACE_CITE[cid]
            if cid in BRIDGE_BEFORE:
                head, kick, rows_, say = BRIDGE_BEFORE[cid]
                s = D.diagram_slide(prs, head, rows_, kicker=kick)
                D.note(s, "BRIDGE — say:\n" + say)
                bridges += 1
            if cid in MAP_BEFORE:
                head, scene, steps, keys = MAP_BEFORE[cid]
                hands = c["hands"] if re.match(r"Before (telling it|beat 1)", c["hands"] or "") else None
                map_placeholder(prs, head, scene, steps, keys, hands_first=hands)
            notes = ("RUNSHEET: " + B.clean(runsheet_note)) if runsheet_note else ""
            # the card's own When, apparatus stripped, at the END of the notes (#40): the face carries
            # FACE_WHEN, and the speaker needs the precise wording only when he reads at home
            tail = ("WHEN, as the card gives it: "
                    + B.clean(B.LABEL.sub("", pool[cid]["when"])).replace("\u06be", " AH")) \
                if cid in FACE_WHEN else ""
            if cid in FACE_DIAGRAM:
                rows_, caption = FACE_DIAGRAM[cid]
                head = B.headline_for(B.short(B.face(c["title"]), 9))
                s = grid_slide(prs, head, rows_, kicker=c["when"], caption=caption)
                D.note(s, ((notes + "\n\n") if notes else "") + B.notes_for(dict(c, quote_after=None))
                       + ("\n\n" + tail if tail else ""))
                made += 1
                continue
            # A researcher's "⚠ NOT FOR THE SLIDE FACE" keeps the statement in the notes only.
            off_face = "NOT FOR THE SLIDE FACE" in (c.get("extra") or "")
            face_text = B.short(c["what"].split(". ")[0].rstrip(".") + ".", 18) if off_face else None
            if B.card_slide(prs, c, extra_notes=notes, arabic_on_face=not off_face,
                            face_text=face_text, face_quote=FACE_QUOTE.get(cid), tail_notes=tail):
                made += 1
            if not pool[cid]["beats"]:
                no_beats += 1
            if cid == CLOSE_D_AFTER:
                # the map has moved — al-Yamāma is blue — so this close earns its own Line and its own
                # question. It does not mention the dead: the room has not been told about them yet.
                closes.append(closing(prs, pool, "line_s04_stop_d.png", "s04-close-stop-d.json",
                                      "The last claimant is dead and the north is closed. But the men "
                                      "who carried the Qurʾān did not all come back — and next week "
                                      "begins with what that cost.",
                                      LESSON_D, [("al-Yamāma", "taken"),
                                                 ("Ḥaḍramawt", "the last front")],
                                      stop="STOP D"))
            if cid == CLOSE_E_AFTER:
                closes.append(closing(prs, pool, "line_s04_stop_e.png", "s04-close-stop-d.json",
                                      "One province on your map is still grey. The last front of the "
                                      "war is Ḥaḍramawt — and it begins with a quarrel over one "
                                      "she-camel.",
                                      LESSON_E, [("al-Yamāma", "taken at last"),
                                                 ("Ḥaḍramawt", "the last front")],
                                      stop="STOP E"))
            if cid == CLOSE_C_AFTER:
                # STOP C in its place: the planned end, with Part V behind it (#47)
                closes.append(closing(prs, pool, "line_s04_stop_c.png", "s04-close-stop-c.json",
                                      "The line has been re-formed and the day is not yet decided. Where "
                                      "does an army go when it cannot retreat?",
                                      LESSON_C, [("ʿAqrabāʾ", "the line re-formed"),
                                                 ("Ḥajr", "the town behind them")],
                                      stop="STOP C"))

    # A and B are hidden, for an earlier stop. STOP D was emitted in its place, after the muṣḥaf.
    closing(prs, pool, "line_s04_stop_a.png", "s04-close-stop-a.json",
            "Khālid ؓ keeps his command, and the last claimant is waiting in al-Yamāma with forty "
            "thousand men. What happens when the army reaches him?",
            LESSON_A, [("Najd", "Buzākha and al-Buṭāḥ behind him"), ("al-Yamāma", "still in revolt")],
            hidden=True, stop="STOP A")
    closing(prs, pool, "line_s04_stop_b.png", "s04-close-stop-b.json",
            "There is a man in irons in Khālid's ؓ own tent. Next week he saves a life, and then a life "
            "is saved for him.",
            LESSON_B, [("al-Yamāma", "the armies in position"), ("Najd", "settled behind them")],
            hidden=True, stop="STOP B")

    D.save(prs, os.path.join(HERE, "S04.pptx"))
    briefs = os.path.join(HERE, "IMAGE_BRIEFS.md")
    if not D.write_briefs(briefs) and os.path.exists(briefs):
        os.remove(briefs)                      # nothing left to draw: a stale to-do list is worse than none
    n = sum(len(r) for _, r in parts)
    if len(closes) != 3:
        raise SystemExit("Three closes are emitted in place: %s (C), %s (D) and %s (E) must each be in "
                         "a Part of RUNSHEET.md. Emitted: %d."
                         % (CLOSE_C_AFTER, CLOSE_D_AFTER, CLOSE_E_AFTER, len(closes)))
    hidden = sum(1 for s in prs.slides if s._element.get("show") == "0")
    print("   %d of %d runsheet cards became slides · %d bridges · %d slides in all (%d hidden: the STOP A "
          "and B closes)" % (made, n, bridges, len(prs.slides), hidden))
    if no_beats:
        print("   ⚠ %d cards still have no **Beats:** — their notes fall back to the prose" % no_beats)
    if UNRENDERED:
        # the evening-3 failure: a placeholder that reaches the lectern. The deck is written; say so loudly.
        raise SystemExit("%d map(s) not rendered — run make_maps.py first, then build again:\n  %s"
                         % (len(UNRENDERED), "\n  ".join(UNRENDERED)))


if __name__ == "__main__":
    build()
