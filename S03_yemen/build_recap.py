# -*- coding: utf-8 -*-
"""Evening 3 — "The story so far": the recap set that sits before Part III (Ḥaḍramawt and Kinda).

    python S03_yemen/build_recap.py      # -> S03_yemen/S03_recap.pptx + .pdf

A SEPARATE deck, because Daniyal hand-edits S03.pptx and a rebuild would overwrite his changes. He pastes
these slides in at the Part III boundary (slide 238 of his edited deck, 2026-09-17).

WHAT IT SUMS UP: RUNSHEET Parts I and II — al-Aswad al-ʿAnsī, then Qays b. Makshūḥ's turn and the two men
judged at Medina. Every line below condenses the text of the cards named in its slide's speaker notes;
nothing here is new, and nothing adjudicates (where the reports differ, the line says so). The deck
contract holds: no bullet lists, ≤ 20 words a card, 2–5 cards a diagram — deck2 refuses the build otherwise.
Two or three cards a slide, with one-line labels: at four or five cards the 32pt labels wrap into the text.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "series"))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import deck2 as D                                                   # noqa: E402
import build_full_deck as B                                        # noqa: E402

VIS = os.path.join(HERE, "visuals")

# (headline, rows, cards summarised) — rows are (label, one line of 20 words or fewer)
CHAIN = [
    ("Yemen before al-Aswad", [
        ("The Abnāʾ", "Persians Kisrā sent with Sayf b. Dhī Yazan; they stayed, and their sons held Yemen."),
        ("Bādhām", "Kisrā's governor accepted Islam; the Prophet ﷺ kept him over all Yemen until he died."),
        ("The division", "In 10 AH: Shahr over Ṣanʿāʾ, governors over the districts, Muʿādh ؓ teaching among them all."),
    ], "AAA/E-AW01 · AAA/E-AW02 · AAA/E-AW19 · AAA/E-AW03"),
    ("al-Aswad al-ʿAnsī rises", [
        ("ʿAbhala", "Dhū al-Khimār, of ʿAns in Madhḥij; he came out after Ḥajjat al-Wadāʿ, 10 AH, with seven hundred men."),
        ("Najrān, then Ṣanʿāʾ", "Najrān in ten nights; Shahr killed outside Ṣanʿāʾ; the city his in twenty-five."),
    ], "AAA/E-AW04 · AAA/E-AW05"),
    ("His months in Ṣanʿāʾ", [
        ("The governors scatter", "Muʿādh ؓ and Abū Mūsā ؓ to Ḥaḍramawt; others to Medina and to ʿAkk."),
        ("Three or four months", "He held Yemen; the Muslims who stayed dealt with him warily."),
    ], "AAA/E-AW06 · AAA/E-AW07 · AAA/E-AW15"),
    ("Ṣanʿāʾ: the plan", [
        ("The letters", "The Prophet ﷺ wrote to the men of Ṣanʿāʾ: fight him, in the open or by stealth."),
        ("The plan", "Fayrūz, Dādhawayh and Qays; Shahr's widow told them of the one room without a guard."),
    ], "AAA/E-AW08 · AAA/E-AW09 · AAA/E-AW10 · AAA/E-AW11 · AAA/E-AW12"),
    ("Ṣanʿāʾ: the night, Rabīʿ I 11 AH", [
        ("The night", "Through the wall, and al-Aswad was killed. The reports differ on the details."),
        ("The dawn", "The adhān from the wall, with a new sentence: and that ʿAbhala is a liar."),
    ], "AAA/E-AW13 · AAA/E-AW14"),
    ("How we know, and when", [
        ("In al-Bukhārī", "al-ʿAnsī, whom Fayrūz killed in Yemen."),
        ("Nights before", "He was killed before the Prophet ﷺ died; the news reached Medina at the end of Rabīʿ I."),
        ("Three days", "Muʿādh ؓ led them in prayer three days — then came the news of the Prophet's ﷺ death."),
    ], "AAA/E-AW20 · ATA/E-TB26 · AAA/E-AW15 · ABU/E-U9 · ATA/E-TB27"),
    ("Ṣanʿāʾ again, 11 AH", [
        ("Qays turns", "One of the three wanted Yemen for himself; two letters went to the same five chiefs."),
        ("The Abnāʾ driven out", "Dādhawayh killed at a meal; Fayrūz ؓ escaped to Khawlān; the families were deported."),
    ], "AAA/E-AW16 · TSY/E-YK01 · RCT/E-RC31 · TSY/E-YK02 · TSY/E-YK03"),
    ("The Yemen restored", [
        ("Fayrūz's ؓ war", "The families were brought back, and Qays was beaten short of Ṣanʿāʾ."),
        ("Two armies", "ʿIkrima ؓ along the coast to Abyan; al-Muhājir ؓ through Najrān to Ṣanʿāʾ."),
    ], "TSY/E-YK17 · TSY/E-YK04 · TSY/E-YK05"),
    ("Judged at Medina", [
        ("Qays", "Charged with killing the servants of Allah; he denied it, and the blood was let go."),
        ("ʿAmr", "b. Maʿdī Karib: every day routed or taken prisoner? He answered: I will turn to it, and not go back."),
        ("Sent home", "Abū Bakr ؓ accepted what they showed, left what was inside them to Allah, and released them."),
    ], "TSY/E-YK06 · TSY/E-YK18 · RCT/E-RC32"),
    ("Who we have met", [
        ("al-Aswad", "ʿAbhala of ʿAns, Dhū al-Khimār; rose 10 AH, killed in Ṣanʿāʾ, Rabīʿ I 11 AH."),
        ("Fayrūz ؓ", "Of the Abnāʾ; went first through the wall; escaped Qays to Khawlān."),
        ("Qays", "b. Makshūḥ: al-Aswad's commander, one of the three; turned; sent home by Abū Bakr ؓ."),
    ], "AAA/E-AW04 · AAA/E-AW13 · TSY/E-YK02 · AAA/E-AW07 · RCT/E-RC32"),
    ("And two Companions", [
        ("Muʿādh ؓ", "The teacher of Yemen; he led the prayer in Ṣanʿāʾ for three days."),
        ("al-Muhājir ؓ", "Umm Salama's ؓ brother; the Prophet ﷺ had appointed him over Kinda."),
    ], "AAA/E-AW03 · ATA/E-TB27 · TSY/E-YK04"),
]

LESSONS = ["AAA/E-AW10", "ATA/E-TB27", "TSY/E-YK01", "RCT/E-RC32"]      # the same four as the STOP B close


def build():
    pool = B.pool_cards()
    prs = D.deck()

    s = D.section_slide(prs, "The story so far", "al-Aswad al-ʿAnsī, and the second ridda of Ṣanʿāʾ")
    D.note(s, "RECAP before Part III — paste in at the Part III boundary (slide 238 of the edited S03).")

    s = D.timeline_slide(prs, os.path.join(VIS, "line_s03_stop_b.png"), "So far tonight")
    D.note(s, "The Line as it stands at STOP B: Parts I and II lit. Re-render with S03_yemen/make_timeline.py.")

    for headline, rows, cards in CHAIN:
        s = D.diagram_slide(prs, headline, rows)
        D.note(s, "RECAP · summarises " + cards + "\n\nEach card's own slide and speaker notes carry the "
                  "full telling and the source.")

    s = D.map_slide(prs, None, "Where we stand", keys=[("Ṣanʿāʾ", "restored"), ("Ḥaḍramawt", "still to come")],
                    brief="MAP STUDIO, not Gemini: open tools/mapstudio/scenes/s03-close-stop-b.json, export, place here.")
    D.note(s, "MAP: tools/mapstudio/scenes/s03-close-stop-b.json — Ṣanʿāʾ blue, Ḥaḍramawt still grey.")

    s = D.lessons_slide(prs, [B.clean(pool[i]["ibrah"]) for i in LESSONS], headline="The lessons so far")
    D.note(s, "عبرت lines from " + ", ".join(LESSONS) + " — the same four as the STOP B close.")

    s = D.statement_slide(prs, english="The Prophet ﷺ had appointed al-Muhājir ؓ over Kinda. From Ṣanʿāʾ, "
                                       "he went on to his post.", headline="Next: Ḥaḍramawt and Kinda")
    D.note(s, "BRIDGE into Part III (TSY/E-YK04; al-Kāmil vol. 2, p. 229). Then the Ḥaḍramawt map.")

    out = os.path.join(HERE, "S03_recap.pptx")
    D.save(prs, out)
    return out


if __name__ == "__main__":
    build()
