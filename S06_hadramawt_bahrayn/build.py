# -*- coding: utf-8 -*-
"""Build S06.pptx — evenings 6 and 7 in one deck (DECISIONS.md #72), inside the vision (docs/VISION.md).

    python S06_hadramawt_bahrayn/scenes.py          # the maps, written through series/mapkit.py
    python S06_hadramawt_bahrayn/make_timeline.py   # the Line — two strands
    python S06_hadramawt_bahrayn/make_maps.py       # render them
    python S06_hadramawt_bahrayn/build.py           # -> S06.pptx + S06.pdf + IMAGE_BRIEFS.md, then the gate

HOW A SLIDE IS DRAWN is evening 5's, imported: the card faces, the layered click maps, the family trees.
WHAT THIS EVENING SUPPLIES is everything Daniyal's review of 2026-10-08 made a rule of, as tables:

    FACE_TITLE     a name, never a sentence                      (#68)
    FACE_WHEN      the kicker: when AND where                    (VISION F6)
    FACE_SPEAKER   whose words a quotation is, on the face       (VISION Q1 — "who said this?")
    FACE_SCENE     one or two lines that give the room the picture (VISION F4)
    IMAGE_BRIEF    authored, paste-ready, for every placeholder  (VISION I1)
    LECTERN_WARN   the one or two warnings that change what he says (VISION N4)
    IMAN           the moments of faith that get a slide of their own (VISION D1)

The notes are series/notes2.py's two tiers — short cues first, the detail under a rule. The build ends by
running tools/check_vision.py and prints every breach; a deck with breaches is not ready to be shown.

WHERE THIS DECK STOPS. Parts I-VIII. Parts IX and X sit under the '## Held' heading in RUNSHEET.md.
"""
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "series"))
sys.path.insert(0, os.path.join(ROOT, "tools"))

_spec = importlib.util.spec_from_file_location(
    "s05_build", os.path.join(ROOT, "S05_yamama_dead_oman_mahra", "build.py"))
S5 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(S5)
import notes2 as N                                         # noqa: E402
import check_vision                                        # noqa: E402

D, B = S5.D, S5.B
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(errors="replace")

S5.HERE = HERE
S5.VIS = VIS = os.path.join(HERE, "visuals")
S5.MAPS = MAPS = os.path.join(VIS, "maps")
S5.BOOKEND = BOOKEND = os.path.join(VIS, "bookend")
S5.HASH_FILE = os.path.join(HERE, ".build", "deck.sha256")

TITLE = ("Bahrayn and Ḥaḍramawt", "11–12 AH — the last two fronts", "Evening 6")

# ------------------------------------------------------------------------------------------- faces
S5.FACE_TITLE.update({
    "RCT/E-RC80": "Arabia, as the year 12 opens",
    "RCT/E-RC71": "al-Mundhir b. Sāwā ؓ — and Rabīʿa",
    "ATA/E-TB24": "al-Jārūd b. al-Muʿallā ؓ",
    "RCT/E-RC72": "al-Ḥuṭam b. Ḍubayʿa",
    "RCT/E-RC24": "Juwāthā",
    "RCT/E-RC25": "al-ʿAlāʾ b. al-Ḥaḍramī ؓ — the sixteen",
    "RCT/E-RC82": "al-ʿAlāʾ ؓ at al-Dahnāʾ — three questions",
    "RCT/E-RC83": "al-ʿAlāʾ ؓ at al-Dahnāʾ — the prayer",
    "RCT/E-RC26": "Hajar — the trench month",
    "RCT/E-RC73": "ʿAbd Allāh b. Ḥadhf, and his uncle",
    "RCT/E-RC74": "Qays b. ʿĀṣim, and al-Ḥuṭam",
    "RCT/E-RC84": "ʿUtayba and al-Muthannā — the roads",
    "RCT/E-RC85": "al-ʿAlāʾ ؓ at the shore",
    "RCT/E-RC86": "al-ʿAlāʾ ؓ — the duʿāʾ",
    "RCT/E-RC87": "al-ʿAlāʾ ؓ at al-Dahnāʾ — the duʿāʾ",
    "RCT/E-RC27": "Dārīn",
    "RCT/E-RC75": "The monk of Hajar",
    "RCT/E-RC28": "Thumāma b. Uthāl ؓ",
    "KTK/E-KD05": "al-Ashʿath b. Qays — at Medina",
    "TSY/E-YK07": "Ziyād b. Labīd ؓ, in Ḥaḍramawt",
    "RCT/E-RC33": "Ziyād b. Labīd ؓ — and Shadhra",
    "TSY/E-YK08": "al-ʿAddāʾ, and Ḥāritha b. Surāqa",
    "TSY/E-YK09": "Shuraḥbīl b. al-Simṭ, and his son",
    "TSY/E-YK10": "The four kings — Mikhwaṣ, Mishraḥ, Jamad, Abḍaʿa",
    "TSY/E-YK19": "al-Ashʿath b. Qays — the column he stopped",
    "TSY/E-YK11": "al-Muhājir ؓ and ʿIkrima ؓ — to al-Nujayr",
    "TSY/E-YK12": "al-Ashʿath b. Qays — and Jaḥdam",
    "TSY/E-YK14": "Abū Bakr ؓ and al-Ashʿath, at Medina",
    "POT/E-PG40": "al-Ashʿath ؓ — pardoned, and married",
    "TSY/E-YK16": "Ṭulayḥa ؓ, ʿAmr ؓ and Qays",
    "POT/E-PG41": "al-Ashʿath ؓ and Jarīr b. ʿAbd Allāh ؓ",
    "ATA/E-TB22": "Thaqīf, at al-Ṭāʾif",
    "RCT/E-RC78": "Najrān",
    "ATA/E-TB10": "Banū Tamīm — three answers",
    "ATA/E-TB13": "The verse of the men who refused",
    "ATA/E-TB25": "The Azd — Medina, and Oman",
    "RCT/E-RC36": "Ibn Kathīr, on the whole war",
    "RCT/E-RC81": "ʿAbd Allāh b. Masʿūd ؓ",
    "RCT/E-RC39": "Abū Bakr ؓ, and the men of Badr",
    "RCT/E-RC43": "The eleven banners, from Dhū al-Qaṣṣa",
    "RCT/E-RC35": "ʿUmar ؓ — the captives bought back",
    "IKO/E-IKR1": "Ibn Khaldūn — as he reads it",
})

# the kicker: when AND where, six words at most — never a bare "11" (VISION F6)
S5.FACE_WHEN.update({
    "RCT/E-RC80": "12 AH, Arabia", "RCT/E-RC71": "11 AH, Bahrayn", "ATA/E-TB24": "11 AH, Bahrayn",
    "RCT/E-RC72": "11 AH, the coast of Bahrayn", "RCT/E-RC24": "11 AH, Juwāthā",
    "RCT/E-RC25": "11 AH, Medina to al-Dahnāʾ", "RCT/E-RC82": "11 AH, al-Dahnāʾ — night",
    "RCT/E-RC83": "11 AH, al-Dahnāʾ — dawn", "RCT/E-RC26": "11 AH, Hajar",
    "RCT/E-RC87": "11 AH, al-Dahnāʾ",
    "RCT/E-RC73": "11 AH, Hajar — one night", "RCT/E-RC74": "11 AH, Hajar — that night",
    "RCT/E-RC84": "11–12 AH, the coast of Bahrayn", "RCT/E-RC85": "11–12 AH, the shore",
    "RCT/E-RC86": "11–12 AH, the shore", "RCT/E-RC27": "11–12 AH, Dārīn",
    "RCT/E-RC75": "11–12 AH, Hajar", "RCT/E-RC28": "12 AH, the road from Dārīn",
    "ATA/E-TB22": "11 AH, al-Ṭāʾif", "RCT/E-RC78": "11–12 AH, Najrān", "ATA/E-TB10": "11 AH, Banū Tamīm",
    "ATA/E-TB13": "11 AH, the tribes", "ATA/E-TB25": "11 AH, Oman and Medina",
    "RCT/E-RC36": "12 AH, the whole peninsula", "RCT/E-RC81": "11 AH, Medina", "RCT/E-RC39": "11 AH, Medina",
    "RCT/E-RC43": "11 AH, Dhū al-Qaṣṣa", "RCT/E-RC35": "ʿUmar's ؓ caliphate, Medina",
    "IKO/E-IKR1": "Seven centuries later",
})

# whose words they are — on the face, above the book and the page (VISION Q1)
FACE_SPEAKER = {
    "RCT/E-RC80": "Ibn Kathīr, opening his chapter on the year 12",
    "RCT/E-RC71": "Ibn al-Athīr, on what Rabīʿa said",
    "ATA/E-TB24": "al-Jārūd b. al-Muʿallā ؓ, to his people",
    "RCT/E-RC72": "Ibn al-Athīr, on al-Ḥuṭam",
    "RCT/E-RC24": "ʿAbd Allāh b. Ḥadhf, besieged in Juwāthā",
    "RCT/E-RC25": "al-Dhahabī, from Ibn Saʿd",
    "RCT/E-RC82": "al-ʿAlāʾ b. al-Ḥaḍramī ؓ, to the army",
    "RCT/E-RC83": "Ibn Kathīr, on what al-ʿAlāʾ ؓ did at dawn",
    "RCT/E-RC87": "al-ʿAlāʾ b. al-Ḥaḍramī ؓ — in another telling, that of Sahm b. Minjāb",
    "RCT/E-RC26": "Ibn al-Athīr, on the trench month",
    "RCT/E-RC73": "Abjar b. Bujayr, to his sister's son",
    "RCT/E-RC74": "Qays b. ʿĀṣim, standing over al-Ḥuṭam",
    "RCT/E-RC84": "Ibn al-Athīr, on the letter al-ʿAlāʾ ؓ wrote",
    "RCT/E-RC85": "al-ʿAlāʾ b. al-Ḥaḍramī ؓ, to the army at the shore",
    "RCT/E-RC86": "al-ʿAlāʾ b. al-Ḥaḍramī ؓ, riding into the sea",
    "RCT/E-RC27": "Ibn al-Athīr, closing the chapter",
    "RCT/E-RC75": "A monk of Hajar, asked why he became a Muslim",
    "RCT/E-RC28": "Banū Qays b. Thaʿlaba, and Thumāma ؓ",
    "KTK/E-KD05": "The Prophet ﷺ, to the delegation of Kinda",
    "TSY/E-YK07": "Banū Walīʿa, to the men of Ḥaḍramawt",
    "RCT/E-RC33": "Ḥāritha b. Surāqa, to Ziyād b. Labīd ؓ",
    "TSY/E-YK08": "al-ʿAddāʾ, calling to his clan",
    "TSY/E-YK09": "Shuraḥbīl b. al-Simṭ and his son, to their clan",
    "TSY/E-YK10": "Ibn al-Athīr, on that night",
    "TSY/E-YK19": "Ibn al-Athīr, on al-Ashʿath",
    "TSY/E-YK11": "Ibn al-Athīr, on al-Nujayr",
    "TSY/E-YK12": "Ibn al-Athīr, on the writing",
    "TSY/E-YK14": "Abū Bakr ؓ, to al-Ashʿath",
    "POT/E-PG40": "al-Ashʿath ؓ, in the market at Medina",
    "TSY/E-YK16": "Jābir b. ʿAbd Allāh ؓ, of the army at al-Qādisiyya",
    "POT/E-PG41": "al-Ashʿath ؓ, of Jarīr b. ʿAbd Allāh ؓ",
    "ATA/E-TB22": "Ibn Kathīr, on Thaqīf",
    "RCT/E-RC78": "Ibn al-Athīr, on Najrān",
    "ATA/E-TB10": "Ibn Kathīr, on Banū Tamīm",
    "ATA/E-TB13": "A verse of the tribes that refused, as Ibn Kathīr records it",
    "ATA/E-TB25": "Ibn Kathīr, on Oman",
    "RCT/E-RC36": "Ibn Kathīr, summing up the war",
    "RCT/E-RC81": "ʿAbd Allāh b. Masʿūd ؓ",
    "RCT/E-RC39": "Abū Bakr ؓ — and, beside it, ʿUmar's ؓ view",
    "RCT/E-RC35": "ʿUmar ؓ, as caliph",
    "IKO/E-IKR1": "Ibn Khaldūn — as he reads it",
}

# the picture, in a line or two, for a quotation that has no map of its own in front of it (VISION F4)
FACE_SCENE = {
    "ATA/E-TB24": ["ʿAbd al-Qays were saying: had he been a prophet, he would not have died."],
    "RCT/E-RC24": ["Inside Juwāthā — besieged, and starving."],
    "RCT/E-RC82": ["Night, in the sands. The camels have bolted with all they had."],
    "RCT/E-RC83": ["Dawn. An army with nothing left but its clothes."],
    "RCT/E-RC74": ["al-Ḥuṭam mounts in the dark; his stirrup-leather parts.", "ʿAfīf b. al-Mundhir offers to set it right."],
    "RCT/E-RC85": ["The shore opposite Dārīn. The same men who were at al-Dahnāʾ."],
    "RCT/E-RC86": ["By ship, a day and a night. He rides his horse into the sea."],
    "RCT/E-RC75": ["He had been with the army through all of it."],
    "RCT/E-RC28": ["On the road home, wearing a cloak from the spoils. It had been al-Ḥuṭam's."],
    "KTK/E-KD05": ["The delegation of Kinda, in silk. al-Ashʿath claims a shared royal ancestor."],
    "RCT/E-RC33": ["A she-camel, branded for the ṣadaqa by mistake. Ziyād ؓ will not give her back."],
    "TSY/E-YK12": ["Inside al-Nujayr. al-Ashʿath writes the names of the men to be spared."],
    "TSY/E-YK14": ["al-Ashʿath, in bonds, argues that the truce covers him."],
    "POT/E-PG40": ["Pardoned, and married to Abū Bakr's ؓ sister."],
    "TSY/E-YK16": ["Years later. Three men who had once turned, now in the army."],
    "POT/E-PG41": ["A funeral, years later. al-Ashʿath ؓ steps back for Jarīr ؓ."],
    "ATA/E-TB22": ["al-Ṭāʾif. They had been Muslim for only two years."],
    "RCT/E-RC78": ["While Muslim tribes broke their word, a Christian community came to renew its own."],
    "ATA/E-TB10": ["One tribe, in one month."],
    "ATA/E-TB13": ["The men who withheld the zakāt, in their own words."],
    "ATA/E-TB25": ["The Azd of Oman — kin to the Anṣār of Medina."],
    "RCT/E-RC36": ["Ibn Kathīr has finished telling the war. He stops, and says what it was."],
    "RCT/E-RC81": ["Ibn al-Athīr opens his whole chapter on the war with these words."],
    "RCT/E-RC39": ["On who was given command — and who was not."],
    "RCT/E-RC35": ["Years later, the captives of these wars are still held."],
    "IKO/E-IKR1": ["A historian, seven centuries later, asks how it was possible."],
}

# the warnings that change what he SAYS. Two at most reach the top of the pane; the rest stay in BACKGROUND.
LECTERN_WARN = {
    "RCT/E-RC71": ["Name no king — three books give his name three ways."],
    "RCT/E-RC72": ["“Came down at” — the page does not say he took them.",
                   "The page does not say where al-Khaṭṭ is. The marker is approximate."],
    "RCT/E-RC24": ["Do not speak the fourth line of the verse — the two books differ."],
    "RCT/E-RC25": ["The page names who joined him, not his road. The road is drawn through their lands."],
    "RCT/E-RC82": ["Tell it as the book tells it — it comes through Sayf b. ʿUmar."],
    "RCT/E-RC83": ["Tell it as the book tells it — build no ruling on it."],
    "RCT/E-RC87": ["Another telling, on another page. Do not join it to the dawn prayer."],
    "RCT/E-RC26": ["A diagram: the page gives sides, no distances. Say “not to scale”."],
    "RCT/E-RC73": ["Do not say why they were drinking. No page does."],
    "RCT/E-RC74": ["Do not use Ibn Khaldūn on who killed him."],
    "RCT/E-RC84": ["The page says “on every road” — name no place for either man."],
    "RCT/E-RC86": ["Read the duʿāʾ slowly. It is the whole slide."],
    "RCT/E-RC27": ["A strait, forded — not a sea that parted. Say what the page says.",
                   "The island is drawn large, and off the shore. A diagram."],
    "RCT/E-RC28": ["Skip this slide if the room is heavy."],
    "TSY/E-YK08": ["al-Basūs: say only “an old war that had started the same way”."],
    "TSY/E-YK10": ["No source ties the old kingship to the ridda. Imply nothing."],
    "TSY/E-YK12": ["Say “11 or 12 AH” — the books differ."],
    "POT/E-PG40": ["Do not name Abū Bakr's ؓ sister — the books differ."],
    "RCT/E-RC39": ["A difference of judgement, not a dispute. Do not adjudicate."],
    "RCT/E-RC81": ["No isnād is given. Narrate it as what the book carries."],
    "IKO/E-IKR1": ["Say his name, and “as he reads it”. He never wrote this about the Ridda."],
}

# a duʿāʾ, a prayer, words of trust: each gets a slide of its own, in Arabic (VISION D1)
IMAN = ["RCT/E-RC82", "RCT/E-RC83", "RCT/E-RC87", "RCT/E-RC85", "RCT/E-RC86"]

STYLE = ("Restrained editorial illustration, muted ochre, deep teal and bone. Flat pure-white background "
         "(#FFFFFF) with no border, so it sits on a white slide with no seam. No text, no lettering, no map. "
         "No people and no faces — landscape, animals and objects only. 16:9.")
IMAGE_BRIEF = {
    "RCT/E-RC82": "Night in a sand desert. A scatter of pack-saddles, water-skins and folded tents left on the "
                  "sand, and the tracks of many camels running off into the dark; a few camels far away, small, "
                  "moving away from the viewer. A sky full of stars. Empty and still. " + STYLE,
    "RCT/E-RC83": "First light over a sand desert. In the foreground a wide, still pool of clear water lying in a "
                  "hollow between dunes, catching the dawn; in the distance a line of loaded camels walking back "
                  "toward it from several directions. " + STYLE,
    "RCT/E-RC74": "A saddled Arabian horse standing alone at night in a camp, head turned, with one stirrup-leather "
                  "broken and hanging loose from the saddle. A low tent edge and a dying fire behind it. " + STYLE,
    "RCT/E-RC43": "Eleven plain cloth banners on spear-shafts, planted upright in a row on open stony ground at "
                  "first light, each a different muted colour, stirring slightly in the wind; a low line of dark "
                  "hills behind. Nothing else on the ground. " + STYLE,
    "RCT/E-RC86": "A shallow, calm sea at dawn seen from a low sandy shore; the water is glassy and only "
                  "ankle-deep far out, with a flat low island on the horizon. Hoof-prints lead from the sand into "
                  "the water. " + STYLE,
}

# Arabic too long to project whole is EXCERPTED — the card's own words, cut at a clause — never replaced by a
# picture: the Arabic is what carries authority in this room (CLAUDE.md 1.4). Each entry is
# (first words, last words) of the Arabic and of its English, found in the card and lifted by bytes.
FACE_CUT = {
    "RCT/E-RC80": ("استهلت هذه السنة", "يمينا وشمالا",
                   "This year began", "roving the land right and left"),
    "RCT/E-RC36": ("ما من ناحية من جزيرة العرب", "من المؤمنين",
                   "There was no region", "believers were in that region"),
    "RCT/E-RC81": ("لقد قمنا بعد رسول الله", "وابنة لبون",
                   "We stood, after", "or a bint labūn"),
    "RCT/E-RC87": ("يا عليم", "نصيبا غيرنا",
                   "O All-Knowing", "but us"),
    "IKO/E-IKR1": ("أن الصبغة الدينية", "إلى الحق",
                   "the religious colouring", "towards the truth"),
}
_MARKS = re.compile("[ؐ-ًؚ-ٰٟۖ-ۜ۟-۪ۨ-ۭـ]")


def _cut(text, first, last, arabic):
    """The span of `text` from `first` to `last`, found with the harakat set aside and returned with them."""
    if not arabic:
        a = text.index(first)
        return text[a:text.index(last, a) + len(last)]
    keep, idx = [], []
    for k, ch in enumerate(text):
        if not _MARKS.match(ch):
            keep.append(ch)
            idx.append(k)
    bare = "".join(keep)
    a = bare.index(first)
    b = bare.index(last, a) + len(last)
    return text[idx[a]:idx[b - 1] + 1]


def face_cuts(pool):
    for cid, (a0, a1, e0, e1) in FACE_CUT.items():
        c = pool[cid]
        S5.FACE_QUOTE[cid] = (_cut(c["arabic"], a0, a1, True), _cut(c["english"], e0, e1, False))


# ------------------------------------------------------------------------------- quotations in parts
# VISION Q4. Daniyal, 2026-10-08: "Whenever the text is not fitting like for the dua … one part of dua per line
# and the new line. Also first Arabic one part. Then its translation. Then next Arabic. And so on. We can move
# part to next new slide."  So a rendering is NEVER cut off with "…". A quotation that does not fit one
# statement slide is set in parts — a clause of the Arabic, its rendering beneath it — over as many slides as it
# takes. Each entry names where every part but the last ENDS, as (Arabic words, English words); "|" starts a new
# slide. The parts are lifted out of the card by bytes: nothing here is retyped onto a face, and the build
# refuses a split that does not find its words, or a face whose rendering would still be cut.
PARTS = {
    "RCT/E-RC80": [("لقتال أهل الردة", "the people of the ridda")],
    "RCT/E-RC71": [("على الردة", "upon the ridda"), ("ومن تبعه", "those who followed him")],
    "ATA/E-TB24": [("كما ماتوا", "just as they died")],
    "RCT/E-RC72": [("في بكر بن وائل", "Bakr b. Wāʾil")],
    "RCT/E-RC24": [("أجمعينا", "young men of Medina")],
    "RCT/E-RC25": [("ستة عشر راكبا", "sixteen riders"), ("وكتب له كتابا", "wrote him a letter")],
    "RCT/E-RC82": [("ألستم المسلمين", "not the Muslims"), ("في سبيل الله", "the path of Allah"), "|",
                   ("أنصار الله", "helpers of Allah"), ("بلى", "Yes"), "|"],              # then: the glad tidings
    "RCT/E-RC83": [("وجثا الناس", "went down on theirs")],
    "RCT/E-RC87": [("يا عظيم", "O Tremendous"), ("نقاتل عدوك", "fight Your enemy"), "|", ("ونتوضأ", "make wuḍūʾ")],
    "RCT/E-RC26": [("والمشركون", "so did the mushrikūn"), ("إلى خندقهم", "back to their trench")],
    "RCT/E-RC84": [("من بكر بن وائل", "firm on their Islam"), ("وغيرهما", "and others"), "|"],   # then: the order
    "RCT/E-RC85": [("في البر", "signs on land"), ("بها في البحر", "at sea"), "|"],          # then: "so rise"
    "RCT/E-RC86": [("يا حكيم يا كريم", "O Wise, O Generous"), ("يا حي يا محيي", "O Giver of life"), "|",
                   ("والإكرام", "majesty and honour")],
    "RCT/E-RC75": [("بعدها", "would transform me")],
    "RCT/E-RC28": [("من المغنم", "from the spoils")],
    "KTK/E-KD05": [("بن كنانة", "b. Kināna")],
    "TSY/E-YK07": [("صلى الله عليه وسلم", "Messenger of Allah ﷺ")],
    "RCT/E-RC33": [("يهوديا", "if you were a Jew")],
    "TSY/E-YK08": [("وأضطهد", "wronged and trampled")],
    "TSY/E-YK09": [("التنقل", "to change sides"), ("ليلزمون الشبهة", "a doubtful position"), "|",
                   ("مخافة العار", "fear of the disgrace")],
    "TSY/E-YK10": [("حول نيرانهم", "round their fires")],
    "TSY/E-YK19": [("والسبي", "and the captives"), ("بالأشعث", "passed by al-Ashʿath")],
    "TSY/E-YK12": [("أو أقتلك", "shall I kill you")],
    "TSY/E-YK14": [("على من فيها", "named in it")],
    "POT/E-PG40": [("زوجني أخته", "his sister to me"), ("غير هذه", "other than this one"), "|"],
    "TSY/E-YK16": [("ثلاثة نفر", "suspect three men"), ("وزهدهم", "their abstinence"), "|"],      # then: the names
    "ATA/E-TB22": [("على الإسلام", "firm upon Islam")],
    "RCT/E-RC78": [("مع أبي بكر", "with Abū Bakr")],
    "ATA/E-TB10": [("أيام الردة", "days of the ridda"), "|", ("ومنع الزكاة", "withheld the zakāt"),
                   ("إلى الصديق", "to al-Ṣiddīq")],
    "ATA/E-TB13": [("كان بيننا …", "among us")],
    "ATA/E-TB25": [("الأزدي", "al-Azdī")],
    "RCT/E-RC36": [("لبعض الناس", "some of its people")],
    "RCT/E-RC81": [("بأبي بكر", "with Abū Bakr")],
    "RCT/E-RC39": [("بصالح أعمالهم", "their good deeds"), ("ينتصر بهم", "victory through them"), "|"],
    "IKO/E-IKR1": [("أهل العصبية", "عصبية")],
}
# the key beside an image placeholder: (four words at most, eight at most). Left to the builder it was the first
# four words of the card's map line and a "…" — "eleven arrows out of…" (slide 77).
FACE_KEY = {
    "RCT/E-RC43": ("Dhū al-Qaṣṣa", "eleven banners, tied by Abū Bakr ؓ"),
}
_AFTER = re.compile(r"[\s\-–—]*[!؟?.،؛,;:\"”»]+")        # the punctuation that closes a clause stays with it.
# An "…" is NOT closing punctuation: where the card marks an omission, the mark stays at the head of the part
# that follows it. (A verse's caesura, or a page turn, is put inside the key, and so leaves the face.)
_QUOTES = '"“”'


def _ends(text, keys, arabic, cid):
    """Cut `text` after each key, in order. Arabic keys are matched with the harakat set aside."""
    if arabic:
        keep, idx = [], []
        for k, ch in enumerate(text):
            if not _MARKS.match(ch):
                keep.append(ch)
                idx.append(k)
        bare = "".join(keep)
    out, pos, bpos = [], 0, 0
    for key in keys:
        if arabic:
            i = bare.find(key, bpos)
            if i < 0:
                raise SystemExit("PARTS[%r]: the Arabic %r is not in the card's statement after the part before it" % (cid, key))
            bpos = i + len(key)
            end = idx[bpos - 1] + 1
            while end < len(text) and _MARKS.match(text[end]):
                end += 1
        else:
            i = text.find(key, pos)
            if i < 0:
                raise SystemExit("PARTS[%r]: the English %r is not in the card's rendering after the part before it" % (cid, key))
            end = i + len(key)
        m = _AFTER.match(text, end)
        if m:
            end = m.end()
        out.append(text[pos:end])
        pos = end
        if arabic:
            bpos = sum(1 for k in idx if k < end)
    out.append(text[pos:])
    return out


def _tidy(part, arabic):
    part = " ".join(part.split()).strip(" -–—")
    part = part.lstrip("،؛,;").strip()
    part = part.rstrip("،؛…" if arabic else ",;").strip()
    if not arabic and sum(part.count(q) for q in _QUOTES) % 2:
        for q in _QUOTES:
            part = part.replace(q, "")
    return part.strip()


def parts_of(cid, c):
    """The card's statement — or its authored excerpt — as [[(arabic, english), …], …], one list a slide."""
    fq = S5.FACE_QUOTE.get(cid)
    ar, en = fq if fq else (c["arabic"], c["english"])
    en = clean(B.face(en)).strip()
    if en[:1] in _QUOTES and en[-1:] in _QUOTES:
        en = en[1:-1]
    spec = PARTS[cid]
    keys = [k for k in spec if k != "|"]
    ars = [_tidy(x, True) for x in _ends(ar, [k[0] for k in keys], True, cid)]
    ens = [_tidy(x, False) for x in _ends(en, [k[1] for k in keys], False, cid)]
    for a, e in zip(ars, ens):
        if not a or not e:
            raise SystemExit("PARTS[%r]: an empty part — %r / %r" % (cid, a, e))
    pairs = list(zip(ars, ens))
    if "|" not in spec:
        return pairs                      # paged by height
    groups, cur, k = [], [], 0
    for item in spec:
        if item == "|":
            groups.append(cur)
            cur = []
        else:
            cur.append(pairs[k])
            k += 1
    cur.append(pairs[k])
    groups.append(cur)
    return [g for g in groups if g]


def quote_slides(prs, c, cid, speaker=None, scene=None, **kw):
    """The card's quotation on the face: whole on one slide where it fits, in parts where it does not."""
    if cid in PARTS and c.get("arabic") and kw.get("arabic_on_face", True) and not kw.get("face_text"):
        return D.parts_slides(prs, parts_of(cid, c), cite=B.face(B.cite_en(c["cite"])),
                              headline=B.headline_for(B.short(B.face(c["title"]), 9)), kicker=B.kicker_for(c),
                              speaker=speaker, scene=scene)
    if cid in FACE_KEY:                       # an image slide's key is written, not cut out of the card
        c = dict(c, map=FACE_KEY[cid][0], what=FACE_KEY[cid][1])
    s = B.card_slide(prs, c, speaker=speaker, scene=scene, **kw)
    if s is None:
        return []
    for sh in s.shapes:
        txt = sh.text_frame.text.strip() if sh.has_text_frame else ""
        if txt.rstrip(_QUOTES).endswith("…") and (sh.name or "") not in ("headline", "kicker"):
            raise SystemExit("%s: its rendering is cut off on the face (%r). Give it PARTS[%r] — where each "
                             "clause ends, in Arabic and in English (VISION Q4)." % (cid, txt[-60:], cid))
    return [s]


def continued(slides, notes_first, c, cid):
    """Notes for a quotation that runs over more than one slide, and the marks the gate reads."""
    if len(slides) > 1:
        notes_first = notes_first.replace(
            N.DETAIL, "▶ NEXT SLIDE — the same words go on (%d slides in all)\n\n%s" % (len(slides), N.DETAIL), 1)
    D.note(slides[0], notes_first)
    for k, s in enumerate(slides[1:], 2):
        said = [sh.text_frame.text.strip() for sh in s.shapes if (sh.name or "").startswith("part-")]
        D.note(s, N.plain(["READ the Arabic — the same words, continued (slide %d of %d)." % (k, len(slides)),
                           "Each part: the Arabic, then its meaning."])
               + "\n\n" + N.DETAIL + "\n\n" + "\n".join(said))


# ------------------------------------------------------------------------------------------- maps
_K = S5.MAP_FOR
MAP_FOR = {
    "RCT/E-RC80": ("s06-arabia", 1, 2,
                   [("Bahrayn", "not yet told"), ("Ḥaḍramawt", "not yet told")],
                   [(3, "The two fronts we have not told: Bahrayn, and Ḥaḍramawt.")]),
    "RCT/E-RC71": ("s06-bahrayn", 3, 6,
                   [("al-Jārūd ؓ", "holds ʿAbd al-Qays to Islam"), ("al-Ḥuṭam", "leads Bakr b. Wāʾil out")],
                   [(2, "11 AH. al-Mundhir ؓ dies, shortly after the Prophet ﷺ."),
                    (3, "Rabīʿa turn — all of Bahrayn but al-Jārūd ؓ and those with him."),
                    (6, "al-Ḥuṭam b. Ḍubayʿa comes out, at the head of Bakr b. Wāʾil.")]),
    "RCT/E-RC72": ("s06-bahrayn-coast", 1, 5,
                   [("al-Ḥuṭam", "comes down at al-Qaṭīf and Hajar"), ("Juwāthā", "besieged by al-Ḥuṭam's men")],
                   [(2, "al-Ḥuṭam comes down at al-Qaṭīf and at Hajar."),
                    (3, "al-Khaṭṭ is won over, with the Zuṭṭ and the Sabābija who live in it."),
                    (4, "He sends a force across the water, to Dārīn."),
                    (5, "And he sends to Juwāthā, and besieges the Muslims in it.")]),
    "RCT/E-RC25": ("s06-bahrayn", 6, 10,
                   [("al-ʿAlāʾ ؓ", "sixteen riders, then an army"), ("al-Dahnāʾ", "he camps in the middle of it")],
                   [(2, "al-ʿAlāʾ ؓ leaves Medina."),
                    (3, "Thumāma ؓ joins, with Banū Ḥanīfa."),
                    (4, "Qays b. ʿĀṣim joins, and other clans of Tamīm."),
                    (5, "Into al-Dahnāʾ.")]),
    # the trench month is a DIAGRAM (mapkit.closeup(diagram=True)): the page gives sides, and nothing else
    "RCT/E-RC26": ("s06-bahrayn-hajar", 1, 6,
                   [("al-ʿAlāʾ ؓ", "camps at Hajar; comes down from that side"),
                    ("al-Jārūd ؓ", "brings ʿAbd al-Qays down from theirs")],
                   [(1, "al-ʿAlāʾ ؓ comes out of al-Dahnāʾ and camps at Hajar."),
                    (2, "He sends to al-Jārūd ؓ — and ʿAbd al-Qays come down on al-Ḥuṭam from their side."),
                    (3, "He comes down on him from the Hajar side. Every one gathers."),
                    (5, "Both sides dig trenches."),
                    (6, "A month. They fight by turns, and go back to their trenches.")]),
    "RCT/E-RC73": ("s06-bahrayn-hajar", 6, 9,
                   [("Ibn Ḥadhf", "seized by al-Ḥuṭam's men; freed by his uncle"), ("al-Ḥuṭam", "his camp is drunk")],
                   [(2, "A noise in the night. ʿAbd Allāh b. Ḥadhf goes to find out."),
                    (3, "They seize him at their trench — and he calls for his uncle."),
                    (7, "Fed, mounted, and let through. He tells al-ʿAlāʾ ؓ: they are drunk.")]),
    "RCT/E-RC74": ("s06-bahrayn-hajar", 9, 11,
                   [("al-ʿAlāʾ ؓ", "goes out at them, over the trench"), ("al-Ḥuṭam", "killed by Qays b. ʿĀṣim")],
                   [(1, "The Muslims go out at them, over the trench."),
                    (5, "al-Ḥuṭam is killed. The camp is taken.")]),
    "RCT/E-RC84": ("s06-bahrayn-flight", 1, 3,
                   [("the beaten", "take ship for Dārīn; the rest go home"),
                    ("ʿUtayba b. al-Nahhās", "and al-Muthannā b. Ḥāritha shut the roads")],
                   [(2, "The bulk of the beaten take ship for Dārīn. The rest go home."),
                    (3, "al-ʿAlāʾ ؓ writes to the Muslims of Bakr b. Wāʾil: sit in wait on every road.")]),
    "RCT/E-RC27": ("s06-bahrayn-darin", 1, 4,
                   [("al-ʿAlāʾ ؓ", "fords the strait, on horseback"), ("Dārīn", "taken by al-ʿAlāʾ ؓ, the same day")],
                   [(1, "al-ʿAlāʾ ؓ comes down to the shore."),
                    (2, "Into the water, on horseback — he fords the strait."),
                    (4, "Dārīn falls. He is back the same day.")]),
}
# evening 5's slices and clicks, on the rule-checked copy — with keys that name who did the thing
_KEYS = {
    "TSY/E-YK08": [("Ziyād b. Labīd ؓ", "with Ḥaḍramawt and al-Sakūn"), ("Banū Muʿāwiya", "of Kinda, come out for Ḥāritha")],
    "TSY/E-YK09": [("Banū Muʿāwiya", "each chief holds his own pasture"), ("Shuraḥbīl and his son", "go over to Ziyād ؓ")],
    "TSY/E-YK10": [("Ziyād b. Labīd ؓ", "strikes at night, from five sides"), ("the four kings", "killed by Ziyād's ؓ men, at their fires")],
    "TSY/E-YK19": [("the captives", "taken by Ziyād ؓ, on the road home"), ("al-Ashʿath b. Qays", "rises, and takes them back")],
}
for _cid in ("TSY/E-YK07", "TSY/E-YK08", "TSY/E-YK09", "TSY/E-YK10", "TSY/E-YK19", "TSY/E-YK11"):
    _sc, _a, _b, _keys, _clicks = _K[_cid]
    MAP_FOR[_cid] = ("s06-kinda", _a, _b, _KEYS.get(_cid, _keys), _clicks)
_sc, _a, _b, _keys, _clicks = MAP_FOR["TSY/E-YK11"]
MAP_FOR["TSY/E-YK11"] = (_sc, _a, _b, _keys, _clicks[:2] + [(4, "Kinda run for al-Nujayr. ʿIkrima ؓ brings up the main body.")])

# a map that belongs to no card: the situation, before the story (VISION M1)
MAP_BRIDGE_BEFORE = {
    "RCT/E-RC71": ("s06-bahrayn", 1, 3, "Bahrayn, in the Prophet's ﷺ lifetime", "Before the conquest of Mecca",
                   [("al-Mundhir b. Sāwā ؓ", "holds Bahrayn for the Prophet ﷺ"), ("Hajar", "its chief town")],
                   ["⚠ Ibn al-Athīr: year 6 — “or, it is said, 8”. Say “before the conquest of Mecca”.",
                    "SAY",
                    "1. Bahrayn is the whole Gulf coast of Arabia — not the island.",
                    "▶ CLICK 1 — The Prophet ﷺ sends al-ʿAlāʾ b. al-Ḥaḍramī ؓ to al-Mundhir b. Sāwā.",
                    "2. al-Mundhir: of ʿAbd al-Qays, the ruler of Bahrayn.",
                    "▶ CLICK 2 — Bahrayn comes under Islam; al-Mundhir ؓ holds it for him.",
                    "3. Remember al-ʿAlāʾ ؓ. Abū Bakr ؓ sends him to Bahrayn tonight."]),
}
# VISION M2: the siege gets the second scale. YK11's own slide tells the road and the battle on the wide map;
# this one tells the fort — beats 5-7 of YK11, which the runsheet skips there so that nothing is said twice.
MAP_BRIDGE_BEFORE["TSY/E-YK12"] = (
    "s06-nujayr", 1, 5, "al-Nujayr — the siege", "11 or 12 AH, Ḥaḍramawt",
    [("al-Muhājir ؓ", "with Ziyād ؓ, besieges Kinda in the fort"), ("ʿIkrima ؓ", "brings up the main body")],
    ["⚠ A diagram: the page gives no side to any commander. Say “not to scale”.",
     "SAY",
     "1. Kinda are inside al-Nujayr — the fort they had already repaired.",
     "▶ CLICK 1 — al-Muhājir ؓ comes down on them, with Ziyād ؓ. The Muslims besiege the fort.",
     "▶ CLICK 2 — ʿIkrima ؓ arrives with the main body. The siege grows hard.",
     "▶ CLICK 3 — Raiding parties spread out through the country, after the rest.",
     "▶ CLICK 4 — Those inside come out and fight. Many are killed — and they go back in.",
     "2. Their spirits sank, and they feared death. Next: what al-Ashʿath did."])
S5.MAP_FOR, S5.MAP_BRIDGE_BEFORE, S5.MAP_BRIDGE_QUOTE = MAP_FOR, MAP_BRIDGE_BEFORE, {}

# ------------------------------------------------------------------------------- Parts IX and X: the hinge
# docs/research/the-two-empires-at-the-hinge-12-13ah.md. Nothing here is general-knowledge history: the two
# zones on the map are outlines and say so, and every sentence on a face has a page of the four books under it.
S5.FACE_TITLE.update({
    "ISA/E-C21": "The house of Kisrā",
    "ISA/E-C1": "Khālid ؓ — the order to Iraq",
    "ISA/E-C7": "Syria — four commanders, four roads",
    "GSA/E-ST8": "Abū Bakr ؓ, to Yazīd b. Abī Sufyān ؓ",
    "GSA/E-ST9": "ʿAmr b. al-ʿĀṣ ؓ — one arrow",
    "ISA/E-C2": "Khālid ؓ — the letter to al-Madāʾin",
    "ISA/E-C22": "Heraclius, to the Romans",
})
S5.FACE_WHEN.update({
    "ISA/E-C21": "12–13 AH, al-Madāʾin", "ISA/E-C1": "Muḥarram 12 AH, al-Yamāma to Iraq",
    "ISA/E-C7": "Early 13 AH, Medina", "GSA/E-ST8": "13 AH, leaving Medina", "GSA/E-ST9": "13 AH, Medina",
    "ISA/E-C2": "12 AH, lower Iraq", "ISA/E-C22": "13 AH, Syria",
})
FACE_SPEAKER.update({
    "ISA/E-C21": "Ibn al-Athīr, on how Persia found its last king",
    "ISA/E-C1": "Ibn Kathīr, on what Abū Bakr ؓ ordered Khālid ؓ",
    "ISA/E-C7": "Yaʿqūb, peace be upon him, to his sons — Sūrat Yūsuf 67",
    "GSA/E-ST8": "Abū Bakr ؓ, to Yazīd b. Abī Sufyān ؓ",
    "GSA/E-ST9": "ʿAmr b. al-ʿĀṣ ؓ, to Abū Bakr ؓ",
    "ISA/E-C2": "Khālid b. al-Walīd ؓ, to the marzubāns of Persia",
    "ISA/E-C22": "Heraclius, to the Romans — as Ibn Kathīr reports it",
})
FACE_SCENE.update({
    "GSA/E-ST8": ["Abū Bakr ؓ, on foot, beside Yazīd's ؓ horse."],
    "GSA/E-ST9": ["Offered the Syrian command — and left free to keep the post he had."],
    "ISA/E-C22": ["The four columns are on the road. The Romans write to their emperor."],
})
LECTERN_WARN.update({
    "ISA/E-C21": ["Say the names as the page's. Do not reconcile them with other histories.",
                  "Stop before Rustam and al-Qādisiyya — later evenings."],
    "ISA/E-C1": ["Muḥarram 12 is al-Madāʾinī's date — say whose it is."],
    "ISA/E-C7": ["The provinces are given, not taken. Nothing is taken tonight."],
    "GSA/E-ST8": ["Abū Sufyān's ؓ son, Muʿāwiya's ؓ brother — say it plainly; nothing of what came later."],
    "ISA/E-C2": ["Do not say he had taken al-Ḥīra. The page says its people chose the jizya."],
    "ISA/E-C22": ["A Muslim historian's report of a Roman council. Narrate it as the book's.",
                  "Stop at “they refused”. The armies are the next evening."],
})
# the verse is quoted across a page turn; the card marks the turn, the face does not carry the mark
FACE_CUT["ISA/E-C7"] = ("وقال يابني", "متفرقة", "O my sons", "separate gates")
PARTS.update({
    "ISA/E-C21": [("من أهل بادوريا", "people of Bādūrayā"), ("وطلبوه منها", "asked her for him"), "|",
                  ("إلى أخواله", "brothers")],
    "ISA/E-C1": [("إلى الله \ufdff", "call them to God"), ("قاتلهم", "fight them"), "|",
                 ("على المسير معه", "to march with him")],
    "ISA/E-C7": [("لا تدخلوا …", "do not enter")],
    "GSA/E-ST8": [("وأخرجك", "bring you out"), ("عزلتك", "I will dismiss you"), "|"],
    "GSA/E-ST9": [("سهام الإسلام", "arrows of Islam"), ("والجامع لها", "who gathers them"), "|"],
    "ISA/E-C2": [("مني الذمة", "protection from me"), ("لا إله غيره", "there is no god")],
    "ISA/E-C22": [("أهل دين جديد", "a new religion"), ("لا قبل لأحد بهم", "strength to face them"), "|",
                  ("ويبقى لكم جبال الروم", "remain yours")],
})
MAP_BRIDGE_BEFORE["ISA/E-C21"] = (
    "s06-empires", 1, 3, "Persia and Rome — beyond Arabia", "12 AH, the other side of the desert",
    [("PERSIA", "al-Madāʾin — the house of Kisrā"), ("ROME", "Heraclius — Syria is his")],
    ["⚠ The two zones are outlines. No page we hold gives either empire's borders.",
     "SAY",
     "1. All of Arabia is one colour. Now look past it.",
     "▶ CLICK 1 — Persia. You know how its king died: by his own son.",
     "▶ CLICK 2 — Rome. Its emperor is Heraclius, and Syria is his.",
     "2. What our books say of each, and what each was told."])
MAP_FOR.update({
    "ISA/E-C1": ("s06-empires", 3, 4,
                 [("Khālid ؓ", "ordered to Iraq, from its lower end"), ("al-Madāʾin", "Persia's capital — he is not sent there")],
                 [(2, "Khālid ؓ leaves al-Yamāma for the lower end of Iraq.")]),
    "ISA/E-C7": ("s06-empires", 4, 5,
                 [("Medina", "four commanders leave by four roads"), ("Syria", "four provinces given, none yet taken")],
                 [(4, "Four commanders, four separate roads — toward Syria.")]),
    "ISA/E-C2": ("s06-empires", 5, 6,
                 [("Khālid ؓ", "writes to al-Madāʾin; he does not march"),
                  ("al-Madāʾin", "Kisrā's commanders, marzubāns and ministers")],
                 [(2, "A letter goes to al-Madāʾin — not an army.")]),
})
HINGE_AFTER = "ISA/E-C22"        # the second close: where the deck ends if the hinge is told
TONIGHT2 = [("Persia", "ISA/E-C21"), ("Iraq", "ISA/E-C1"), ("Syria", "ISA/E-C7"), ("Yazīd ؓ", "GSA/E-ST8"),
            ("Rome", "ISA/E-C22")]
NEXT_WEEK2 = ("The emperor of the Romans told them: make peace. They refused him. What did it cost them?")

BRIDGE_BEFORE = {
    "RCT/E-RC71": ("From ʿIkrima's ؓ journey, to Bahrayn", "11 AH, the Gulf coast",
                   [("Last week", "ʿIkrima's ؓ journey: Oman, then Mahra"),
                    ("Tonight", "Bahrayn — the front that began before them"),
                    ("Then", "Ḥaḍramawt, the last front")],
                   ["SAY",
                    "1. Last week: ʿIkrima's ؓ journey east — Oman, then Mahra.",
                    "2. Tonight we go back once: to Bahrayn, which began before any of them.",
                    "3. Then forward, to Ḥaḍramawt — and we do not go back again."]),
    "KTK/E-KD05": ("Kinda, two years earlier", "10 AH, Medina",
                   [("Two years earlier", "the delegation of Kinda comes to Medina"),
                    ("At its head", "al-Ashʿath b. Qays"),
                    ("Then", "forward again, to Ḥaḍramawt")],
                   ["SAY",
                    "1. One step back — and this is the only one tonight.",
                    "2. Two years before the Prophet ﷺ died: the delegation of Kinda, at Medina.",
                    "3. At its head, al-Ashʿath b. Qays. The last front is his."]),
    "ATA/E-TB22": ("Thaqīf, Najrān, the Azd", "11 AH — the same months",
                   [("So far", "Bahrayn, then Ḥaḍramawt: front after front"),
                    ("Now", "the same months — al-Ṭāʾif, Najrān, Oman"),
                    ("The question", "who did not break — and why?")],
                   ["SAY",
                    "1. So far tonight, every slide has been a front.",
                    "2. Now the same months, from the side: who did not break at all.",
                    "3. Some of them are the people you would least expect."]),
}
S5.BRIDGE_BEFORE = BRIDGE_BEFORE
S5.TREES = TREES = {"KTK/E-KD05": S5.TREES["KTK/E-KD05"]}

CHECKPOINTS = {
    "RCT/E-RC28": dict(
        n=1, line="line_s06_cp1.png", scene=("s06-arabia", 3),
        keys=[("Bahrayn", "held again, by al-ʿAlāʾ ؓ"), ("Ḥaḍramawt", "not yet told")],
        say=["Bahrayn is told: Juwāthā, al-Dahnāʾ, the trench, the sea.",
             "One patch on this map is still grey: Ḥaḍramawt."],
        clock="Past 0:36 here — close here.",
        carry="One front is left. It began with a quarrel about camels.",
        end="One front was left, and the books say it began with one she-camel. Next week: how."),
    "TSY/E-YK12": dict(
        n=2, line="line_s06_cp2.png", scene=("s06-arabia", 4),
        keys=[("al-Nujayr", "opened to Ziyād ؓ and al-Muhājir ؓ"), ("al-Ashʿath", "sent to Medina in bonds")],
        say=["Ḥaḍramawt is told: from a she-camel to a fort.",
             "Every front is settled. al-Ashʿath goes to Medina, in bonds."],
        clock="Past 0:40 here — close here.",
        carry="He had left his own name off the paper. Now he stands before Abū Bakr ؓ.",
        end="al-Ashʿath stood in front of Abū Bakr ؓ, in bonds. Next week: what Abū Bakr ؓ did with him."),
    "POT/E-PG41": dict(
        n=3, line="line_s06_cp3.png", scene=("s06-arabia", 5),
        keys=[("Arabia", "one colour, in two years"), ("al-Ashʿath ؓ", "pardoned by Abū Bakr ؓ")],
        say=["The last two fronts are told — and al-Ashʿath ؓ, who came back.",
             "The peninsula is one colour."],
        clock="Past 0:40 here — close here. This is the natural end.",
        carry="The fighting is over. Now: what do the books say the whole of it was?",
        end="Two years after the Prophet ﷺ died, all of Arabia was on one side. Next week: what the books "
            "say the whole of it was."),
    "RCT/E-RC35": dict(
        n=4, line="line_s06_cp4.png", scene=("s06-arabia", 5),
        keys=[("Dhū al-Qaṣṣa", "eleven banners, sent by Abū Bakr ؓ"), ("Arabia", "every sector settled")],
        say=["Both fronts — and then the whole war, seen from its end.",
             "Eleven banners left one sitting. Every sector is this colour now."],
        clock="Past 0:52 here — close here. This is the last checkpoint built.",
        carry="One question is left: why did it not break again?",
        end="There were two empires on the other side of that desert. Next week: did either of them know?"),
}
S5.CHECKPOINTS = CHECKPOINTS
CLOSE_AFTER = "IKO/E-IKR1"      # the last card: the close never comes before a card
TONIGHT = [("Bahrayn", "RCT/E-RC27"), ("al-Dahnāʾ", "RCT/E-RC82"), ("Ḥaḍramawt", "TSY/E-YK12"),
           ("al-Ashʿath ؓ", "POT/E-PG41"), ("Ibn Masʿūd ؓ, on the war", "RCT/E-RC81")]
NEXT_WEEK = ("Two years after the Prophet ﷺ died, all of Arabia was on one side. There were two empires on "
             "the other side of the desert. Did either of them know?")

# a part opens on a map of the situation (VISION M1) — unless it has no ground to show, and says why
NO_MAP_PARTS = {
    "Part V": "the judgement at Medina: a room, not a field",
    "Part VI": "three places at once, each with its own slide",
    "Part VII": "the war looked back on; there is nothing to move",
    "Part VIII": "one historian's reading",
}

META = {"slides": {}, "cards": [], "iman": IMAN, "no_map_parts": sorted(NO_MAP_PARTS)}
BRIEFS = []


def mark(prs, kind, **kw):
    META["slides"][str(len(prs.slides))] = dict(kind=kind, **kw)


def clean(s):
    return B.clean(S5.REF.sub("", s or "")).strip()


def skips(rnote):
    m = S5.SKIP.search(rnote or "")
    return {int(x) for x in re.findall(r"\d+", m.group(1))} if m else set()


def has_placeholder(s):
    return any((sh.name or "").startswith(D.SCAFFOLD) for sh in s.shapes)


def bookend_images():
    """Evening 5's Checkpoint 2 pair — Daniyal's own slides 61-62, not the build's (#23)."""
    os.makedirs(BOOKEND, exist_ok=True)
    line, mp = os.path.join(BOOKEND, "cp2_line.png"), os.path.join(BOOKEND, "cp2_map.png")
    if not (os.path.exists(line) and os.path.exists(mp)):
        from pptx import Presentation
        slides = list(Presentation(os.path.join(ROOT, "S05_yamama_dead_oman_mahra", "S05.pptx")).slides)
        for idx, path in ((60, line), (61, mp)):
            pics = [sh for sh in slides[idx].shapes if sh.shape_type == 13]
            if not pics:
                raise SystemExit("no picture on S05.pptx slide %d — the bookend pair moved" % (idx + 1))
            open(path, "wb").write(max(pics, key=lambda sh: sh.width * sh.height).image.blob)
    return line, mp


def checkpoint(prs, cp):
    s1 = D.timeline_slide(prs, os.path.join(VIS, cp["line"]), "Where we stand", kicker="So far tonight")
    D.note(s1, N.plain(["CHECKPOINT %d — the Line" % cp["n"], "SAY", "1. " + cp["say"][0],
                        "(Next slide: the map. The time check is there.)"]))
    mark(prs, "checkpoint")
    s2 = S5.static_map(prs, cp["scene"][0], cp["scene"][1], "Where we stand", "So far tonight", cp["keys"])
    D.note(s2, N.plain(["CHECKPOINT %d — the map" % cp["n"], "SAY", "1. " + cp["say"][1], "⏱ " + cp["clock"],
                        "CARRY ON — “%s”" % cp["carry"]])
           + "\n\n" + N.DETAIL + "\n\nOUT OF TIME — this is your ending. Stay on this map, and say:\n\n“"
           + cp["end"] + "”\n\nThen a loud السلام علیکم, and the dua. Next week opens on these two slides.")
    mark(prs, "checkpoint")


def the_close(prs, pool):
    s = D.timeline_slide(prs, os.path.join(VIS, "line_s06_close.png"), "Tonight on the Line")
    D.note(s, N.plain(["THE CLOSE — the Line", "SAY", "1. Bahrayn: Juwāthā, al-Dahnāʾ, the trench, the sea.",
                       "2. Kinda, two years earlier — then Ḥaḍramawt, to al-Nujayr.",
                       "3. Medina: al-Ashʿath, in bonds — and pardoned.",
                       "4. And the whole war — Ibn Kathīr, and Ibn Masʿūd ؓ."]))
    mark(prs, "close")
    lines = ["Bahrayn — held again.", "Ḥaḍramawt — the last front, taken.", "The peninsula, in one colour."]
    m, n = S5.layered_map(prs, "s06-arabia", 2, 5, "Where we stand", "12 AH, Arabia",
                          [("Bahrayn", "held again, by al-ʿAlāʾ ؓ"), ("Ḥaḍramawt", "taken by Ziyād ؓ and al-Muhājir ؓ")])
    if n != len(lines):
        raise SystemExit("the close map has %d clicks; its notes have %d" % (n, len(lines)))
    D.note(m, N.plain(["THE CLOSE — the map", "SAY", "1. When you came in, two patches here were grey."]
                      + ["▶ CLICK %d — %s" % (i, t) for i, t in enumerate(lines, 1)]))
    mark(prs, "map")
    s = D.lessons_slide(prs, [h for h, _ in TONIGHT])
    D.note(s, N.plain(["TONIGHT — say each name, then its line", "SAY"]
                      + ["%d. %s" % (i, h) for i, (h, _) in enumerate(TONIGHT, 1)])
           + "\n\n" + N.DETAIL + "\n\n"
           + "\n".join("%d. %s — %s" % (i, h, clean(pool[c]["ibrah"])) for i, (h, c) in enumerate(TONIGHT, 1)))
    mark(prs, "close")
    q = D.question_slide(prs, NEXT_WEEK)
    D.note(q, N.plain(["IF YOU STOP HERE — ask it, and pause. Then a loud السلام علیکم — and the dua.",
                       "IF YOU CARRY ON — ask it, and go straight on: Part IX is the answer."]))
    mark(prs, "close")


def hinge_close(prs, pool):
    """The second close: after Parts IX-X. The Line with the two orders on it, the map with nothing taken."""
    s = D.timeline_slide(prs, os.path.join(VIS, "line_s06_hinge.png"), "Tonight on the Line")
    D.note(s, N.plain(["THE CLOSE — the Line", "SAY", "1. The Ridda, whole: every front, one colour.",
                       "2. Muḥarram of year 12 — the order to Iraq.",
                       "3. Early in year 13 — four commanders, four roads.",
                       "4. And nothing taken yet."]))
    mark(prs, "close")
    m = D.map_slide(prs, os.path.join(HERE, "visuals", "maps", "s06-empires-step-06.png"), "Where we stand",
                    keys=[("Iraq", "Khālid ؓ at its lower end; a letter"),
                          ("Syria", "four commanders, four roads — nothing taken")],
                    kicker="13 AH, beyond Arabia", map_frac=0.70)
    D.note(m, N.plain(["THE CLOSE — the map", "SAY", "1. When you came in, the map ended at Arabia's edge.",
                       "2. East: one commander, and one letter.", "3. North: four commanders, on four roads.",
                       "4. Not a town has been taken."]))
    mark(prs, "close")
    s = D.lessons_slide(prs, [h for h, _ in TONIGHT2])
    D.note(s, N.plain(["TONIGHT — say each name, then its line", "SAY"]
                      + ["%d. %s" % (i, h) for i, (h, _) in enumerate(TONIGHT2, 1)])
           + "\n\n" + N.DETAIL + "\n\n"
           + "\n".join("%d. %s — %s" % (i, h, clean(pool[c]["ibrah"])) for i, (h, c) in enumerate(TONIGHT2, 1)))
    mark(prs, "close")
    q = D.question_slide(prs, NEXT_WEEK2)
    D.note(q, "Ask it, and pause. Then a loud السلام علیکم — and the dua. The room must know it has ended.")
    mark(prs, "close")


def fit(notes):
    """A pane written by evening 5's helpers (the family tree): keep its opening, rule off the rest."""
    if N.words(N.top_tier(notes)) <= N.TOP_WORDS:
        return notes
    lines, top = notes.split("\n"), []
    while lines and N.words("\n".join(top + [lines[0]])) <= 60:
        top.append(lines.pop(0))
    return "\n".join(top).strip() + "\n\n" + N.DETAIL + "\n\n" + "\n".join(lines).strip()


def build():
    pool = B.pool_cards()
    parts = B.runsheet(os.path.join(HERE, "RUNSHEET.md"))
    ids = [cid for _, rows in parts for cid, _ in rows]
    META["cards"] = ids
    missing = [cid for cid in ids if cid not in pool]
    if missing:
        raise SystemExit("RUNSHEET.md names cards that are not in any pool: %s" % missing)
    for table, name in ((MAP_FOR, "MAP_FOR"), (TREES, "TREES"), (BRIDGE_BEFORE, "BRIDGE_BEFORE"),
                        (CHECKPOINTS, "CHECKPOINTS"), (MAP_BRIDGE_BEFORE, "MAP_BRIDGE_BEFORE"), ({c: 1 for c in IMAN}, "IMAN")):
        stray = [k for k in table if k not in ids]
        if stray:
            raise SystemExit("%s names cards the runsheet does not run: %s" % (name, stray))
    face_cuts(pool)
    S5.check_face_quotes(pool)

    prs = D.deck()
    s = D.title_slide(prs, *TITLE)
    D.note(s, N.plain(["SAY", "1. السلام علیکم — evening six.", "2. Tonight: Bahrayn, and then Ḥaḍramawt — the last two fronts."]))
    mark(prs, "title")
    line, mp = bookend_images()
    s = D.timeline_slide(prs, line, "Where we stopped")
    D.note(s, N.plain(["BOOKEND IN — last week's Line, unchanged", "SAY",
                       "1. Last week ended with Oman and Mahra settled."]))
    mark(prs, "bookend")
    s = D.map_slide(prs, mp, "Where we stand", keys=[("Oman, Mahra", "settled by ʿIkrima ؓ and Ḥudhayfa"),
                                                      ("Ḥaḍramawt", "not yet told")],
                    kicker="From last week", map_frac=0.70)
    D.note(s, N.plain(["BOOKEND IN — last week's map, unchanged", "SAY",
                       "1. Tonight: Bahrayn — and then Ḥaḍramawt, the last front."]))
    mark(prs, "bookend")

    made = clicks_total = bridges = maps = words_slides = trees = checkpoints = 0
    for part, rows in parts:
        pname = part.split(" — ")[0].strip()
        sub = B.clean(part.split(" — ", 1)[1] if " — " in part else "", translit=True)
        s = D.section_slide(prs, B.clean(pname, translit=True), sub or None)
        D.note(s, N.plain(["SAY", "1. " + (sub or pname) + "."]))
        mark(prs, "section", part=pname)
        for cid, rnote in rows:
            c = S5.face_card(pool[cid], cid)
            speaker, scene = FACE_SPEAKER.get(cid), FACE_SCENE.get(cid)
            warn, skip = LECTERN_WARN.get(cid, ()), skips(rnote)
            if cid in BRIDGE_BEFORE:
                head, kick, rows_, say = BRIDGE_BEFORE[cid]
                s = D.diagram_slide(prs, head, rows_, kicker=kick)
                D.note(s, N.plain(["BRIDGE"] + say))
                mark(prs, "bridge")
                bridges += 1
            if cid in MAP_BRIDGE_BEFORE:
                sc, a, b, head, kick, keys, lines = MAP_BRIDGE_BEFORE[cid]
                s, n = S5.layered_map(prs, sc, a, b, head, kick, keys)
                k = sum(1 for x in lines if x.startswith("▶ CLICK"))
                if n != k:
                    raise SystemExit("%s %d-%d: %d clicks on the slide, %d ▶ CLICK lines" % (sc, a, b, n, k))
                D.note(s, N.plain(lines))
                mark(prs, "map")
                maps += 1
                clicks_total += n
            if cid in TREES:
                before = len(prs.slides)
                S5.family_tree(prs, pool, TREES[cid])
                t = prs.slides[len(prs.slides) - 1]
                D.note(t, fit(t.notes_slide.notes_text_frame.text))
                if len(prs.slides) > before:
                    mark(prs, "tree")
                trees += 1
            off_face = "NOT FOR THE SLIDE FACE" in (c.get("extra") or "")
            fq = S5.FACE_QUOTE.get(cid)
            if cid in MAP_FOR:
                sc, a, b, keys, clicks = MAP_FOR[cid]
                # a statement too long for one slide used to stay in the notes; in parts, it has a face (Q4)
                words = bool(c["arabic"]) and not off_face and (
                    cid in PARTS or B.ar_len(fq[0] if fq else c["arabic"]) <= B.AR_SLIDE_MAX)
                head = B.headline_for(B.short(B.face(c["title"]), 9))
                s, n = S5.layered_map(prs, sc, a, b, head, B.kicker_for(c), keys)
                if n != len(clicks):
                    raise SystemExit("%s on %s %d-%d: %d clicks on the slide, %d ▶ CLICK lines in its notes"
                                     % (cid, sc, a, b, n, len(clicks)))
                D.note(s, N.compose(c, skip=skip, clicks=clicks, words_follow=words, warn=warn,
                                    speaker=speaker, clean=clean))
                mark(prs, "map", card=cid)
                maps += 1
                clicks_total += n
                if words:
                    ws = quote_slides(prs, c, cid, speaker=speaker, face_quote=fq,
                                      scene=scene if cid in ("RCT/E-RC74",) else None)
                    if ws:
                        continued(ws, N.words_slide(c, speaker=speaker, clean=clean)
                                  + ("\n\n" + N.BRIEF + "\n\nOPTIONAL — a background image, if you want one:\n"
                                     + IMAGE_BRIEF[cid] if cid in IMAGE_BRIEF else ""), c, cid)
                        for k in range(len(ws)):
                            META["slides"][str(len(prs.slides) - len(ws) + 1 + k)] = dict(
                                kind="words" if k == 0 else "cont", card=cid)
                        words_slides += 1
                made += 1
            else:
                face_text = B.short(c["what"].split(". ")[0].rstrip(".") + ".", 18) if off_face else None
                ss = quote_slides(prs, c, cid, speaker=speaker, scene=scene, arabic_on_face=not off_face,
                                  face_text=face_text, face_quote=fq, brief=IMAGE_BRIEF.get(cid))
                s = ss[0] if ss else None
                if s is not None:
                    ph = has_placeholder(s)
                    if ph and cid not in IMAGE_BRIEF:
                        raise SystemExit("%s becomes an image placeholder and has no IMAGE_BRIEF — write one "
                                         "(VISION I1), or give it a FACE_QUOTE short enough for the face" % cid)
                    brief = IMAGE_BRIEF.get(cid)
                    continued(ss, N.compose(c, skip=skip, quote_here=not ph, warn=warn, speaker=speaker, clean=clean,
                                            brief=brief if (ph or cid in IMAN) else None), c, cid)
                    first = len(prs.slides) - len(ss) + 1
                    if brief and (ph or cid in IMAN):
                        BRIEFS.append((first, S5.FACE_TITLE.get(cid, c["title"]), brief,
                                       "placeholder" if ph else "optional background"))
                    for k in range(len(ss)):
                        META["slides"][str(first + k)] = dict(kind="card" if k == 0 else "cont", card=cid)
                    made += 1
            if cid in CHECKPOINTS:
                checkpoint(prs, CHECKPOINTS[cid])
                checkpoints += 1
            if cid == CLOSE_AFTER:
                the_close(prs, pool)
            if cid == HINGE_AFTER:
                hinge_close(prs, pool)

    if checkpoints != len(CHECKPOINTS):
        raise SystemExit("%d checkpoints emitted of %d" % (checkpoints, len(CHECKPOINTS)))
    target = os.path.join(HERE, "S06.pptx")
    if S5.deck_has_uncommitted_changes(target):
        print("   !! S06.pptx differs from its committed version (Daniyal's edits?) - NOT overwritten.\n"
              "      This build is written to S06_NEW.pptx.")
        target = os.path.join(HERE, "S06_NEW.pptx")
    out = D.save(prs, target)
    S5.remember_deck(out)
    os.makedirs(os.path.join(HERE, ".build"), exist_ok=True)
    with open(os.path.join(HERE, ".build", "slides.json"), "w", encoding="utf-8") as f:
        json.dump({str(i): S5.LAYERED[s.slide_id] for i, s in enumerate(prs.slides, 1)
                   if s.slide_id in S5.LAYERED}, f, ensure_ascii=False, indent=1)
    with open(os.path.join(HERE, ".build", "deck.json"), "w", encoding="utf-8") as f:
        json.dump(META, f, ensure_ascii=False, indent=1)
    with open(os.path.join(HERE, "IMAGE_BRIEFS.md"), "w", encoding="utf-8") as f:
        f.write("# Evening 6 — image briefs\n\nPaste each into the image generator as it stands. The same text "
                "is at the foot of that slide's notes.\n\n**House rule:** places, animals and objects only — "
                "never a person, never a face. White ground, so the picture sits on the slide with no seam.\n")
        for n, head, brief, kind in BRIEFS:
            f.write("\n## Slide %d — %s  *(%s)*\n\n%s\n" % (n, head, kind, brief))
    print("   %d of %d runsheet cards · %d maps (%d clicks) · %d words slides · %d trees · %d bridges · "
          "%d checkpoints · %d image briefs · %d slides in all"
          % (made, len(ids), maps, clicks_total, words_slides, trees, bridges, checkpoints, len(BRIEFS),
             len(prs.slides)))
    return out


if __name__ == "__main__":
    if os.path.exists(os.path.join(HERE, "S06.FINAL")):
        raise SystemExit("S06.FINAL exists: S06.pptx is hand-finished. Do not rebuild over it.")
    build()
    print("\n--- the vision gate (docs/VISION.md) ---")
    _, R = check_vision.check(HERE)
    by = {}
    for rule, _, _ in R.rows:
        by[rule] = by.get(rule, 0) + 1
    print("   every checkable rule holds" if not R.rows else
          "   %d breach(es): %s\n   run: python tools/check_vision.py %s"
          % (len(R.rows), "  ".join("%s=%d" % kv for kv in sorted(by.items())), os.path.basename(HERE)))
    sys.exit(1 if R.rows else 0)
