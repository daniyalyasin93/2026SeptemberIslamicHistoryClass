"""Build L02 «بارہ سال» (۱۱–۲۳ھ).  python L02_baarah_saal/build.py

Light slides; depth is in Script.md. Every quotation on screen carries its volume and page,
so a challenge from the floor is answered by pointing at the wall.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "series"))
from deckkit import *  # noqa: F401,F403
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches


def build(path):
    prs = deck()

    # 1 · title
    s = blank(prs, DARK)
    text(s, "بارہ سال", Inches(0.9), Inches(2.1), Inches(11.5), Inches(1.6),
         size=64, color=CREAM, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True, spacing=1.6)
    text(s, "نشست ۲  ·  ۱۱ھ – ۲۳ھ", Inches(0.9), Inches(3.9), Inches(11.5), Inches(0.7),
         size=24, color=GOLD, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True)
    rule(s, Inches(9.8), Inches(4.9), Inches(2.6))
    text(s, "ایک خطرے میں گھرے شہر سے — دو سلطنتوں کے گرنے تک",
         Inches(0.9), Inches(5.2), Inches(11.5), Inches(0.8),
         size=22, color=CREAM, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True)
    note(s, "0:00 AGHAZ (3 min). Line + map up. Draw the bracket around 11-23 AH on the banner so\n"
            "they SEE how narrow tonight is. 30-second note for newcomers: we are reading a book.")

    # 2 · opening scene
    s = blank(prs, DARK)
    text(s, "مدینہ — پہرے پر", Inches(0.9), Inches(2.9), Inches(11.5), Inches(1.3),
         size=54, color=GOLD, cs=UR, align=PP_ALIGN.CENTER, is_rtl=True)
    note(s, "0:03 OPENING SCENE (5 min). STAND STILL. Weeks after the Prophet (peace be upon him)\n"
            "died, Madina is under armed guard at night. Name the officers of the guard slowly:\n"
            "Ali, Zubayr, Talha, Sa'd b. Abi Waqqas, Abd al-Rahman b. Awf, Ibn Mas'ud (radiyallahu\n"
            "anhum). These are the names we read in fadail - and they are on night watch.\n"
            "VERIFIED: al-Bidaya ج7 ص18.\n"
            "[ASK] How many roads does one man have in front of him at such a moment?")

    # 3 · the refusal
    s = blank(prs)
    eyebrow(s, "۱۱ھ  ·  انکار")
    text(s, "نماز ہاں — زکوٰۃ نہیں",
         Inches(0.9), Inches(2.5), Inches(11.5), Inches(1.3),
         size=48, color=TEAL, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True, spacing=1.6)
    text(s, "﴿خُذْ مِنْ أَمْوَالِهِمْ صَدَقَةً … وَصَلِّ عَلَيْهِمْ إِنَّ صَلَاتَكَ سَكَنٌ لَهُمْ﴾",
         Inches(0.9), Inches(4.1), Inches(11.5), Inches(0.9),
         size=26, color=DARK, cs=AR, align=PP_ALIGN.RIGHT, is_rtl=True)
    text(s, "التوبة ۹:۱۰۳  ·  البدایہ والنہایہ، ج۷ ص۱۸",
         Inches(0.9), Inches(5.2), Inches(11.5), Inches(0.5),
         size=15, color=TEAL, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True)
    note(s, "Move 2 (4 min). THE KEY DISTINCTION - say it slowly. Many were not denying prayer.\n"
            "They said: prayer yes, zakat no. Some argued from 9:103 - we pay only to one whose\n"
            "prayer is a comfort for us. VERIFIED al-Bidaya ج7 ص18.")

    # 4 · the line of poetry
    s = quote_slide(
        prs,
        "أَطَعْنَا رَسُولَ اللهِ إِذْ كَانَ بَيْنَنَا … فَوَاعَجَبًا مَا بَالُ مُلْكِ أَبِي بَكْرِ",
        "ہم نے رسول اللہ ﷺ کی اطاعت کی جب وہ ہمارے درمیان تھے — تو اب یہ ابوبکر کی حکومت کیسی؟",
        "البدایہ والنہایہ، ج۷ ص۱۸", "اُس وقت کا ایک شعر")
    note(s, "One line of poetry opens the whole problem: the question was not whether Islam is true.\n"
            "It was whether anything survives the Prophet (peace be upon him). VERIFIED ج7 ص18.")

    # 5 · Umar's question
    s = quote_slide(
        prs,
        "عَلَامَ تُقَاتِلُ النَّاسَ؟ وَقَدْ قَالَ رَسُولُ اللهِ ﷺ:\n«أُمِرْتُ أَنْ أُقَاتِلَ النَّاسَ حَتَّى يَشْهَدُوا أَنْ لَا إِلَهَ إِلَّا اللهُ»",
        "آپ لوگوں سے کس بنیاد پر لڑ رہے ہیں؟ نبی ﷺ نے تو فرمایا تھا…",
        "سیدنا عمر بن الخطاب ؓ  ·  البدایہ والنہایہ، ج۷ ص۱۸", "فیصلہ  ·  ۱ / ۳")
    note(s, "0:16 THE PEAK OF THE EVENING (5 min). SLOW DOWN.\n"
            "First: a group of Companions advised leaving them be until iman settled. Abu Bakr\n"
            "refused (ج7 ص18). THEN Umar himself questioned it. Umar was not a soft man.")

    # 6 · Abu Bakr's answer
    s = quote_slide(
        prs,
        "وَاللهِ لَوْ مَنَعُونِي عَنَاقًا كَانُوا يُؤَدُّونَهُ إِلَى رَسُولِ اللهِ ﷺ لَأُقَاتِلَنَّهُمْ عَلَى مَنْعِهَا\nوَاللهِ لَأُقَاتِلَنَّ مَنْ فَرَّقَ بَيْنَ الصَّلَاةِ وَالزَّكَاةِ",
        "اللہ کی قسم! اگر یہ مجھ سے ایک بکری کا بچہ بھی روکیں گے جو وہ رسول اللہ ﷺ کو دیتے تھے، تو میں اُن سے لڑوں گا۔\nاللہ کی قسم، جو نماز اور زکوٰۃ میں فرق کرے گا، میں اُس سے لڑوں گا۔",
        "سیدنا ابوبکر الصدیق ؓ  ·  البدایہ والنہایہ، ج۷ ص۱۸  ·  رواہ الجماعۃ سوی ابن ماجہ", "فیصلہ  ·  ۲ / ۳")
    note(s, "Read it. Then STOP for three full seconds. Do not comment.")

    # 7 · Umar concedes
    s = quote_slide(
        prs,
        "فَمَا هُوَ إِلَّا أَنْ رَأَيْتُ اللهَ قَدْ شَرَحَ صَدْرَ أَبِي بَكْرٍ لِلْقِتَالِ، فَعَرَفْتُ أَنَّهُ الْحَقُّ",
        "بس جب میں نے دیکھا کہ اللہ نے ابوبکر کا سینہ اِس کے لیے کھول دیا — تو مجھے یقین ہو گیا کہ یہی حق ہے۔",
        "سیدنا عمر بن الخطاب ؓ  ·  البدایہ والنہایہ، ج۷ ص۱۸", "فیصلہ  ·  ۳ / ۳")
    note(s, "SAY NOTHING AFTER THIS. Do not explain it, do not draw the lesson - the room draws it.\n"
            "The strongest thirty seconds of the whole ten weeks, and every word is someone else's.\n"
            "THEN: PEN-DOWN. 'apni lakeer par 11 hijri ke paas nishaan lagaiye.'")

    # 8-10 · the three fronts
    for head, sub, nt in [
        ("لشکر نکلتے ہیں", "ذو القصہ سے — عرب سنبھل جاتا ہے",
         "Move 4 (3 min). Columns radiate out from Madina; draw the arrows. PEN-DOWN.\n"
         "[SOURCE: al-Bidaya ج7 ص22-27 cached - commanders and sequence, read by eye.\n"
         "DO NOT state a number of columns until the book gives it.]"),
        ("یرموک", "روم شام سے نکل جاتا ہے",
         "Move 5 (3 min). [SOURCE: al-Bidaya ج7 ص85-95 cached.] Map: arrow north, mark Dimashq."),
        ("قادسیہ", "اور فارس",
         "Move 6 (2 min). [trim to the quotation alone if running long.] Map: arrow east."),
    ]:
        s = blank(prs)
        text(s, head, Inches(0.9), Inches(2.5), Inches(11.5), Inches(1.3),
             size=50, color=TEAL, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True, spacing=1.6)
        text(s, sub, Inches(0.9), Inches(4.1), Inches(11.5), Inches(0.8),
             size=25, color=INK, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True, spacing=1.5)
        note(s, nt)

    # 11 · the envoy
    s = quote_slide(
        prs,
        "وَإِخْرَاجُ الْعِبَادِ مِنْ عِبَادَةِ الْعِبَادِ إِلَى عِبَادَةِ اللهِ\nوَالنَّاسُ بَنُو آدَمَ، فَهُمْ إِخْوَةٌ لِأَبٍ وَأُمٍّ",
        "اور بندوں کو بندوں کی غلامی سے نکال کر اللہ کی بندگی میں لانا۔\nاور لوگ سب آدم کی اولاد ہیں — ایک ہی ماں باپ کے بھائی۔",
        "رستم کے دربار میں  ·  البدایہ والنہایہ، ج۷ ص۱۳۴", "قادسیہ")
    note(s, "This does the work of a paragraph of explanation. Read it and move on. PEN-DOWN: arrow east.")

    # 12 · taaruf divider
    s = blank(prs, TEAL)
    text(s, "تعارف", Inches(0.9), Inches(3.0), Inches(11.5), Inches(1.4),
         size=64, color=CREAM, cs=UR, align=PP_ALIGN.CENTER)
    note(s, "0:28 TAARUF (7 min). Read from the card. All three verified from Siyar A'lam al-Nubala.")

    for nm, laqab, cite, nt in [
        ("سیدنا ابوبکر الصدیق ؓ", "",
         "سیر أعلام النبلاء، راشدون ص۸",
         "40,000 dinars when he accepted Islam (Urwa b. al-Zubayr gives the figure), and the\n"
         "Prophet (peace be upon him): 'ma nafa'ani malun ma nafa'ani malu Abi Bakr'.\n"
         "EXTRA: Aisha (radiyallahu anha) - alone among the Muhajirun, his father accepted Islam too."),
        ("سیدنا خالد بن الولید ؓ", "سیف اللہ",
         "سیر أعلام النبلاء، ج۱ ص۳۶۶",
         "THE LAQAB IS THE PROPHET'S OWN (peace be upon him): 'wa sammahu al-Nabi: Sayf Allah'.\n"
         "WAQI'A: at Mu'ta all three appointed commanders were martyred - Zayd, Ja'far dhu\n"
         "al-janahayn, Ibn Rawaha - and the army stood with no commander. He took the banner on\n"
         "the spot, charged, and the victory came."),
        ("سیدنا ابو عبیدہ بن الجراح ؓ", "امین الامۃ",
         "سیر أعلام النبلاء، ج۱ ص۶",
         "Also the Prophet's own naming (peace be upon him). WAQI'A that ties back to tonight's\n"
         "opening: at al-Saqifa, Abu Bakr himself put his name forward - 'li-kamali ahliyyatihi'."),
    ]:
        s = blank(prs)
        text(s, nm, Inches(0.9), Inches(2.2), Inches(11.5), Inches(1.4),
             size=44, color=TEAL, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True, spacing=1.7)
        if laqab:
            text(s, laqab, Inches(0.9), Inches(3.8), Inches(11.5), Inches(0.9),
                 size=32, color=GOLD, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True)
        text(s, cite, Inches(0.9), Inches(5.6), Inches(11.5), Inches(0.5),
             size=15, color=TEAL, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True)
        note(s, nt)

    # 16 · kaise pata chala
    s = blank(prs)
    eyebrow(s, "کیسے پتا چلا؟")
    text(s, "قرآن کی جمع", Inches(0.9), Inches(2.7), Inches(11.5), Inches(1.3),
         size=50, color=TEAL, cs=UR, align=PP_ALIGN.CENTER, is_rtl=True)
    note(s, "0:35 (3 min). How a text was secured by PROCEDURE rather than by chance.\n"
            "[SOURCE: Tareekh-e-Ummat, the Abu Bakr chapter. Take this from Rehan sahib's Urdu,\n"
            "NOT from Arabic pages we selected - it is doctrinally weighty and the course narrates\n"
            "his book.]")

    # 17 · aaj ki baat
    s = blank(prs)
    eyebrow(s, "آج کی بات")
    text(s, "امام حسن بصریؒ اور امام قتادہؒ فرماتے ہیں",
         Inches(0.9), Inches(1.4), Inches(11.5), Inches(0.8),
         size=25, color=TEAL, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True)
    text(s, "﴿مَنْ يَرْتَدَّ مِنْكُمْ عَنْ دِينِهِ فَسَوْفَ يَأْتِي اللَّهُ بِقَوْمٍ يُحِبُّهُمْ وَيُحِبُّونَهُ﴾",
         Inches(0.7), Inches(2.4), Inches(11.9), Inches(1.2),
         size=30, color=DARK, cs=AR, align=PP_ALIGN.CENTER, is_rtl=True)
    text(s, "اِس آیت میں مراد سیدنا ابوبکر ؓ اور اُن کے ساتھی ہیں —\nمرتدین اور مانعینِ زکوٰۃ سے اُن کے قتال میں",
         Inches(0.9), Inches(3.9), Inches(11.5), Inches(1.4),
         size=24, color=INK, cs=UR, align=PP_ALIGN.CENTER, is_rtl=True, spacing=1.6)
    text(s, "المائدة ۵:۵۴  ·  البدایہ والنہایہ، ج۷ ص۱۹",
         Inches(0.9), Inches(5.6), Inches(11.5), Inches(0.5),
         size=15, color=TEAL, cs=UR, align=PP_ALIGN.CENTER, is_rtl=True)
    note(s, "0:38 (4 min). ONE sentence and no more: 'jo kaam us din ek aadmi ne akele khare ho kar\n"
            "kiya - Quran us ki taraf ishara karta hai.' THEN STOP.\n"
            "90 SECONDS OF SILENCE while they write. Two volunteers max. 'shukriya', nothing else.\n"
            "ALTERNATE (do not use both): fa'ida 2 from the muqaddima, p.53-54.")

    # 18 · close
    s = blank(prs, DARK)
    text(s, "اگلے ہفتے — پہلا امتحان", Inches(0.9), Inches(2.4), Inches(11.5), Inches(1.3),
         size=48, color=CREAM, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True, spacing=1.6)
    text(s, "۲۳ھ  ←  ۴۰ھ", Inches(0.9), Inches(3.9), Inches(11.5), Inches(0.8),
         size=28, color=GOLD, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True)
    rule(s, Inches(0.9), Inches(5.0), Inches(11.5), CREAM, Pt(1))
    text(s, "ایک آدمی اکیلا کھڑا ہو، اور سب اُس کے خلاف مشورہ دے رہے ہوں — تو اُسے کیا چیز سنبھالتی ہے؟",
         Inches(0.9), Inches(5.3), Inches(11.5), Inches(0.9),
         size=22, color=GOLD, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True)
    note(s, "0:42 (3 min). Next week opens WITH the principle - how such events are read with adab.\n"
            "Say the take-home question once and leave it unanswered.")

    # 19 · sources
    s = blank(prs)
    eyebrow(s, "SOURCES  ·  show only if asked")
    text(s, "البدایہ والنہایہ — ابن کثیر رحمہ اللہ\nج۵ ص۳۴۴–۳۴۹ · ج۷ ص۱۷–۲۷ · ج۷ ص۸۵–۹۵ · ج۷ ص۱۳۲–۱۴۰\n\n"
            "سیر أعلام النبلاء — الذہبی رحمہ اللہ\nراشدون ص۸ · ج۱ ص۶ · ج۱ ص۳۶۶",
         Inches(0.9), Inches(2.0), Inches(11.5), Inches(3.4),
         size=22, color=INK, cs=UR, align=PP_ALIGN.RIGHT, is_rtl=True, spacing=1.6)
    note(s, "Both works are named and recommended in the muqaddima, so this stays inside the\n"
            "course's own frame. Show only if someone asks.")

    return save(prs, path)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    print("saved:", build(os.path.join(here, "L02.pptx")))
