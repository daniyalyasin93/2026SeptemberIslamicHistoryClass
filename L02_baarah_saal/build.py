"""Build L02 "Twelve Years" — 632 to 644.

    python L02_baarah_saal/build.py

English carries the slides; Arabic quotations in Naskh with an English translation beneath,
Urdu only where it earns its place. Latin digits throughout.
Sources: al-Bidaya wa'l-Nihaya (Ibn Kathir) and Siyar A'lam al-Nubala (al-Dhahabi) — both named
and recommended in the muqaddima, so this stays inside the course's own frame.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "series"))
from deckkit import *  # noqa: F401,F403
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt


NL = chr(10)


def build(path):
    prs = deck()

    # 1
    s = title_slide(prs, "Twelve Years", "بارہ سال",
                    "From a city under guard to two broken empires",
                    "SESSION 2  ·  632 – 644  ·  DHA ISLAMABAD")
    note(s, "0:00 AGHAZ (3 min). Line + map up. On the BANNER, draw the bracket around 11-23 AH so\n"
            "they see how narrow tonight is. 'pichhle hafte chaudah sau saal. aaj - barah.'\n"
            "30 seconds for newcomers: we are reading a book; I am not a historian.")

    # 2 — opening scene
    s = statement_slide(prs, "Madina is under armed guard at night.",
                        "Weeks after the Prophet ﷺ died.",
                        kicker="632", bg=DARK, fg=CREAM)
    note(s, "0:03 OPENING SCENE (5 min). STAND STILL.\n"
            "Name the officers of the night watch SLOWLY - this is the whole effect:\n"
            "  Ali, Zubayr, Talha, Sa'd b. Abi Waqqas, Abd al-Rahman b. Awf, Ibn Mas'ud\n"
            "  (radiyallahu anhum).\n"
            "'These are the names we read in fadail - and they are standing watch on the passes.'\n"
            "VERIFIED: al-Bidaya ج7 ص18.\n"
            "[ASK] How many roads does one man have in front of him at such a moment?")

    # 3 — the real question
    s = blank(prs, CREAM)
    eyebrow(s, "what they actually said")
    text(s, "“Prayer, yes. Zakat, no.”", Inches(0.85), Inches(1.5), Inches(11.6), Inches(1.1),
         size=46, color=TEAL, font=EN)
    text(s, "Many of the tribes were not denying prayer. Some argued from the Qur’an itself —",
         Inches(0.85), Inches(2.75), Inches(11.6), Inches(0.6),
         size=21, color=INK, font=EN, italic=True)
    text(s, "﴿خُذْ مِنْ أَمْوَالِهِمْ صَدَقَةً … وَصَلِّ عَلَيْهِمْ إِنَّ صَلَاتَكَ سَكَنٌ لَهُمْ﴾",
         Inches(0.7), Inches(3.5), Inches(11.9), Inches(0.9),
         size=30, color=DARK, font=AR, cs=AR, align=PP_ALIGN.CENTER, is_rtl=True)
    text(s, "“…and pray for them; your prayer is a comfort for them.”\nSo, they said: we pay only to one whose prayer is a comfort for us.",
         Inches(0.85), Inches(4.5), Inches(11.6), Inches(1.1),
         size=21, color=INK, font=EN, align=PP_ALIGN.CENTER, spacing=1.35, italic=True)
    text(s, "AL-TAWBA 9:103  ·  AL-BIDAYA WA'L-NIHAYA, vol. 7 p. 18",
         Inches(0.85), Inches(5.85), Inches(11.6), Inches(0.4),
         size=13, color=TEAL, font=SANS, align=PP_ALIGN.CENTER)
    note(s, "Move 2 (4 min). THE DISTINCTION EVERYONE MISSES - say it slowly.\n"
            "The question was never whether Islam is true. It was whether anything survives the\n"
            "Prophet (peace be upon him). VERIFIED al-Bidaya ج7 ص18.")

    # 4 — the poetry
    s = quote_slide(
        prs,
        "أَطَعْنَا رَسُولَ اللهِ إِذْ كَانَ بَيْنَنَا … فَوَاعَجَبًا مَا بَالُ مُلْكِ أَبِي بَكْرِ",
        "“We obeyed the Messenger of God while he was among us —\nso what, we wonder, is this rule of Abu Bakr?”",
        "A VERSE FROM THE TIME  ·  AL-BIDAYA WA'L-NIHAYA, vol. 7 p. 18",
        label="one line opens the whole problem")
    note(s, "This single verse states the real question better than any explanation. Read it, let it\n"
            "sit, move on. VERIFIED ج7 ص18.")

    # 5-7 — the peak
    s = quote_slide(
        prs,
        "عَلَامَ تُقَاتِلُ النَّاسَ؟",
        "“On what basis are you fighting these people?”\nThe Prophet ﷺ said to fight until they testify there is no god but God…",
        "UMAR IBN AL-KHATTAB  ·  AL-BIDAYA WA'L-NIHAYA, vol. 7 p. 18",
        label="the decision  ·  1 of 3")
    note(s, "0:16 THE PEAK OF THE EVENING (5 min). SLOW RIGHT DOWN.\n"
            "First: a group of Companions advised leaving them until iman settled. Abu Bakr refused\n"
            "(ج7 ص18). THEN Umar himself questioned it - and Umar was not a soft man.")

    s = quote_slide(
        prs,
        "وَاللهِ لَأُقَاتِلَنَّ مَنْ فَرَّقَ بَيْنَ الصَّلَاةِ وَالزَّكَاةِ",
        "“By God, I will fight whoever separates prayer from zakat.”\nEven if they withheld from me a kid goat they used to give the Messenger ﷺ.",
        "ABU BAKR AL-SIDDIQ  ·  AL-BIDAYA vol. 7 p. 18  ·  narrated by the collections except Ibn Majah",
        label="the decision  ·  2 of 3")
    note(s, "Read it. Then STOP for three full seconds. DO NOT COMMENT.")

    s = quote_slide(
        prs,
        "فَعَرَفْتُ أَنَّهُ الْحَقُّ",
        "“When I saw that God had opened Abu Bakr’s heart to this,\nI knew that it was the truth.”",
        "UMAR IBN AL-KHATTAB  ·  AL-BIDAYA WA'L-NIHAYA, vol. 7 p. 18",
        label="the decision  ·  3 of 3")
    note(s, "SAY NOTHING AFTER THIS. Do not explain it, do not draw the lesson - the room draws it,\n"
            "and Umar (radiyallahu anhu) has already drawn it for you.\n"
            "The strongest thirty seconds of the whole ten weeks, and every word belongs to someone\n"
            "else. THEN: PEN-DOWN - mark 632 on the line.")

    # 8 — Abu Bakr rides out
    s = quote_slide(
        prs,
        "وَاللهِ لَا أَفْعَلُ، وَلَأُوَاسِيَنَّكُمْ بِنَفْسِي",
        "“By God I will not. I will share it with you in person.”\nWhen the Companions asked him to stay behind and send someone else.",
        "ABU BAKR AL-SIDDIQ  ·  AL-BIDAYA WA'L-NIHAYA, vol. 7 p. 21",
        label="he rode out himself")
    note(s, "0:21 (2 min). He went out with his sword drawn, and ALI took hold of his camel's reins:\n"
            "  'Where to, O Caliph of the Messenger of God? I say to you what the Messenger said at\n"
            "   Uhud: sheathe your sword, and do not afflict us with the loss of yourself.'\n"
            "  (al-Bidaya ج7 ص22, al-Daraqutni; also from Aisha radiyallahu anha)\n"
            "STATE IT AND MOVE ON. If anyone in the room carries an assumption about those two, this\n"
            "answers it without you arguing anything.")

    # 9 — THE RIDDA MAP
    s = map_slide(prs, "map_s2_ridda", "Eleven banners", "632 – 633", line=None)
    note(s, "0:23 (6 min). WALK THE ARROWS ONE AT A TIME - this is the map moment of the evening.\n"
            "Eleven commissions, each written separately, all moving out from Dhu al-Qassa.\n"
            "Name only the four or five the room can hold: Khalid to Buzakha against Tulayha;\n"
            "Yamama against Musaylima; al-Ala' b. al-Hadrami to Bahrain; al-Muhajir to San'a.\n"
            "THE INSTRUCTION IN THE LETTER, worth saying aloud: the sign is the adhan - if they\n"
            "call it back, hold off from them (ج7 ص24).\n"
            "PEN-DOWN once the arrows are drawn.")

    # 9a — not one thing: what the Ridda actually was
    s = blank(prs, CREAM)
    eyebrow(s, "it was not one thing")
    text(s, "Four different problems, called by one name",
         Inches(0.85), Inches(1.0), Inches(11.6), Inches(0.9),
         size=34, color=TEAL, font=EN)
    band(s, Inches(2.02), Inches(0.04), GOLD, Inches(0.85), Inches(11.6))
    cols = [
        ("Rival prophecy", "Musaylima at Yamama" + NL + "Tulayha of Banu Asad" + NL + "al-Aswad al-Ansi, Yemen", MAROON),
        ("Withheld the zakat", "The delegations who came" + NL + "affirming prayer" + NL + "Uyayna and Ghatafan", MAROON),
        ("Political secession", "Tribes breaking away from" + NL + "Madina rather than from" + NL + "the religion", MUTED),
        ("HELD LOYAL", "Quraysh · Thaqif" + NL + "Aws and Khazraj" + NL + "Tayyi · Abd al-Qays", TEAL),
    ]
    for i, (head, body, col) in enumerate(cols):
        x = 0.85 + i * 3.02
        text(s, head, Inches(x), Inches(2.42), Inches(2.85), Inches(0.7),
             size=19, color=col, font=SANS, bold=True)
        text(s, body, Inches(x), Inches(3.2), Inches(2.85), Inches(2.0),
             size=17, color=INK, font=EN, spacing=1.4)
    text(s, "Only the first group left Islam. That distinction is the whole evening.",
         Inches(0.85), Inches(5.5), Inches(11.6), Inches(0.6),
         size=20, color=MAROON, font=EN, italic=True)
    note(s, "SAY THIS BEFORE THE MAP. It stops the Ridda being heard as everyone apostatised." + NL +
            "The fourth column is the one that matters - large parts of Arabia never wavered." + NL +
            "VERIFIED in al-Bidaya: Tayyi came over through Adi b. Hatim, who brought 500 fighters" + NL +
            "and then a thousand riders of Jadila (vol.7 p.25); Uyayna and Ghatafan backed Tulayha" + NL +
            "and both men later returned to Islam (vol.7 p.26)." + NL +
            "[VERIFY the remaining tribe assignments against Tareekh-e-Ummat before delivery -" + NL +
            " the grouping came from the earlier classification artifact, not from a read page.]")
    # 9b — the payoff that closes the opening scene
    s = statement_slide(prs, "Three zakat caravans reach Madina in one night.",
                        "Announced by the same men who had been standing guard on the passes.",
                        line="line_s2", kicker="sixty nights after the Prophet’s passing", bg=CREAM, fg=TEAL)
    note(s, "THIS CLOSES THE LOOP ON YOUR OPENING SCENE - say so explicitly." + NL +
            "One at the beginning of the night, one in the middle, one at the end:" + NL +
            "  Safwan's      -> announced by Sa'd ibn Abi Waqqas" + NL +
            "  al-Zibriqan's -> announced by Abd al-Rahman ibn Awf" + NL +
            "  Adi ibn Hatim's -> announced by Ibn Mas'ud, or Abu Qatada al-Ansari" + NL +
            "The zakat is arriving after all. The argument has become a fact, and you never had" + NL +
            "to make it. VERIFIED: al-Bidaya vol.7 p.21.")
    # 10 — the conquests map
    s = map_slide(prs, "map_s2_twelve", "Then outward", "632 – 644", line=None)
    note(s, "0:29 (4 min). Three arrows only, quickly:\n"
            "  Yarmuk -> Byzantium out of Syria [al-Bidaya ج7 ص85-95 cached, outline only]\n"
            "  Qadisiyya -> Persia [ج7 ص132-140]\n"
            "  Fustat -> Egypt\n"
            "Do not linger - the weight of the evening was the decision, not the conquests.")

    # 9 — the envoy
    s = quote_slide(
        prs,
        "وَإِخْرَاجُ الْعِبَادِ مِنْ عِبَادَةِ الْعِبَادِ إِلَى عِبَادَةِ اللهِ\nوَالنَّاسُ بَنُو آدَمَ، فَهُمْ إِخْوَةٌ لِأَبٍ وَأُمٍّ",
        "“To bring people out of the worship of servants into the worship of God…\nand people are the children of Adam — brothers of one father and mother.”",
        "THE ENVOY, IN RUSTAM'S COURT  ·  AL-BIDAYA WA'L-NIHAYA, vol. 7 p. 134",
        label="what they said they were for")
    note(s, "This does the work of a paragraph of explanation. Read it and move on.")

    # 10 — taaruf divider
    s = statement_slide(prs, "Three people", "All three verified from Siyar A'lam al-Nubala.",
                        kicker="تعارف  ·  who you are meeting", bg=TEAL, fg=CREAM)
    note(s, "0:28 TAARUF (7 min). Read from the printed card, never from memory.")

    people = [
        ("Abu Bakr al-Siddiq", "سیدنا ابوبکر الصدیق ؓ", "", "",
         "FIRST CALIPH  ·  632 – 634",
         "Held the community together when much of Arabia broke away, and had the Qur’an gathered\ninto a single written collection.",
         "He accepted Islam owning forty thousand dinars — and the Prophet ﷺ said: “No wealth ever\nbenefited me as Abu Bakr’s wealth benefited me.”",
         "SIYAR A'LAM AL-NUBALA, Rashidun p. 8  ·  the figure is from Urwa ibn al-Zubayr",
         "EXTRA if you have room: Aisha (radiyallahu anha) - alone among the Muhajirun, his father\n"
         "accepted Islam too. And Amr ibn al-As asking which man the Prophet loved most: 'Abu Bakr'."),
        ("Khalid ibn al-Walid", "سیدنا خالد بن الولید ؓ", "SAYF ALLAH — the Sword of God", "سیف اللہ",
         "MIGRATED AS A MUSLIM, SAFAR 8 AH  ·  COMMANDER, RIDDA AND SYRIA",
         "Commanded the Ridda campaigns, then the Syrian front through to Yarmuk.",
         "At Mu’ta all three commanders the Prophet ﷺ had appointed were killed — Zayd, Ja’far, and\nIbn Rawaha. The army stood with no commander. He took the banner on the spot, and the victory came.",
         "SIYAR A'LAM AL-NUBALA, vol. 1 p. 366",
         "THE LAQAB IS THE PROPHET'S OWN (peace be upon him): 'wa sammahu al-Nabi: Sayf Allah'.\n"
         "Say that explicitly - it was not given by admirers later."),
        ("Abu Ubayda ibn al-Jarrah", "سیدنا ابو عبیدہ بن الجراح ؓ", "AMIN AL-UMMA — the Trustee of this Community", "امین الامۃ",
         "COMMANDER IN SYRIA AFTER KHALID",
         "Narrated few hadith and fought many battles; took Syria after Khalid.",
         "At Saqifa, Abu Bakr himself put his name forward for the succession — “for the completeness\nof his fitness”, as al-Dhahabi records it.",
         "SIYAR A'LAM AL-NUBALA, vol. 1 p. 6",
         "Also the Prophet's own naming (peace be upon him), and he was given the news of Paradise.\n"
         "This incident ties straight back to tonight's opening block rather than standing apart."),
    ]
    for en, ur, lq_en, lq_ur, dates, did, inc, cite, nt in people:
        s = person_slide(prs, en, ur, lq_en, lq_ur, dates, did, inc, cite)
        note(s, nt)

    # 14 — how we know, kept short
    s = blank(prs, CREAM)
    eyebrow(s, "how do we know?")
    text(s, "How the Qur’an was gathered", Inches(0.85), Inches(1.4), Inches(11.6), Inches(1.0),
         size=40, color=TEAL, font=EN)
    text(s, "A text secured by procedure — not by chance, and not by one man’s memory.",
         Inches(0.85), Inches(2.6), Inches(11.6), Inches(0.7),
         size=23, color=INK, font=EN, italic=True)
    text(s, "[ SOURCE: Tareekh-e-Ummat — the Abu Bakr chapter ]",
         Inches(0.85), Inches(3.8), Inches(11.6), Inches(0.5),
         size=17, color=MAROON, font=SANS)
    note(s, "0:35 (3 min). THREE MINUTES, no more - this is the only method content tonight.\n"
            "[SOURCE: Take this from Rehan sahib's Urdu, NOT from Arabic pages we selected. It is\n"
            "doctrinally weighty and the course narrates his book.]")

    # 15 — aaj ki baat
    s = blank(prs, CREAM)
    eyebrow(s, "آج کی بات  ·  today's point — not mine")
    text(s, "al-Hasan al-Basri and Qatada", Inches(0.85), Inches(1.05), Inches(11.6), Inches(0.7),
         size=30, color=TEAL, font=EN)
    text(s, "﴿فَسَوْفَ يَأْتِي اللَّهُ بِقَوْمٍ يُحِبُّهُمْ وَيُحِبُّونَهُ﴾",
         Inches(0.7), Inches(2.15), Inches(11.9), Inches(1.0),
         size=34, color=DARK, font=AR, cs=AR, align=PP_ALIGN.CENTER, is_rtl=True)
    text(s, "“God will bring a people whom He loves and who love Him.”",
         Inches(0.85), Inches(3.3), Inches(11.6), Inches(0.6),
         size=24, color=INK, font=EN, align=PP_ALIGN.CENTER, italic=True)
    text(s, "The ones meant, they said, are Abu Bakr and his companions —\nin exactly this fight.",
         Inches(0.85), Inches(4.15), Inches(11.6), Inches(1.1),
         size=25, color=DARK, font=EN, align=PP_ALIGN.CENTER, spacing=1.35)
    text(s, "AL-MA'IDA 5:54  ·  AL-BIDAYA WA'L-NIHAYA, vol. 7 p. 19",
         Inches(0.85), Inches(5.6), Inches(11.6), Inches(0.4),
         size=13, color=TEAL, font=SANS, align=PP_ALIGN.CENTER)
    note(s, "0:38 (4 min). ONE sentence and no more:\n"
            "  'jo kaam us din ek aadmi ne akele khare ho kar kiya - Quran us ki taraf ishara\n"
            "   karta hai.'\n"
            "THEN STOP. 90 SECONDS OF SILENCE while they write. Two volunteers max, 'shukriya',\n"
            "nothing else. ALTERNATE (do not use both): fa'ida 2 from the muqaddima, pp. 53-54.")

    # 16 — close
    s = statement_slide(prs, "Next week: the first test.",
                        "644 to 661. When the trouble came from inside, not outside.",
                        line="line_s3", kicker="اگلے ہفتے", bg=DARK, fg=CREAM)
    note(s, "0:42 (3 min). Next week OPENS with the principle - how such events are read with adab.\n"
            "TAKE-HOME, say once and leave unanswered:\n"
            "  'ek aadmi akela khara ho, aur sab us ke khilaf mashwara de rahe hon - to use kya\n"
            "   cheez sambhalti hai?'")

    # 17 — sources
    s = blank(prs, CREAM)
    eyebrow(s, "sources  ·  show only if asked")
    text(s, "al-Bidaya wa’l-Nihaya  —  Ibn Kathir\nvol. 5 pp. 344–349  ·  vol. 7 pp. 17–27, 85–95, 132–140\n\n"
            "Siyar A’lam al-Nubala  —  al-Dhahabi\nRashidun p. 8  ·  vol. 1 p. 6  ·  vol. 1 p. 366",
         Inches(0.9), Inches(1.8), Inches(11.5), Inches(3.2),
         size=23, color=INK, font=EN, spacing=1.6)
    text(s, "Both works are named and recommended in the muqaddima of our own source.",
         Inches(0.9), Inches(5.3), Inches(11.5), Inches(0.5),
         size=19, color=MAROON, font=EN, italic=True)
    note(s, "Show only if someone asks where something came from.")

    return save(prs, path)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    print("saved:", build(os.path.join(here, "L02.pptx")))
