"""Declare the order the research notes are READ in, and render them numbered so a folder sorts right.

    python tools/reading_order.py                # write docs/research/READING_ORDER.md
    python tools/reading_order.py --pdf          # …and render numbered PDFs into docs/research/read/
    python tools/reading_order.py --pdf --only L03

WHY THIS IS NOT THE SAME AS THE NARRATIVE ORDER. `tools/build_content.py` holds ORDER_L02 and
ORDER_L03: the order the evening TELLS the material, which is what `CONTENT.md` is emitted in. That
is the wrong order to read the research in. A reader needs the اصول before the fitna it governs and
the dates before the events that hang off them, whereas a listener needs the story in the order it
happened. So the reading order is declared separately, here, and the difference is deliberate.

For session 3 the two differ in exactly two places, and both matter:

  · `the-mashajarat-and-how-to-narrate-it` is read FIRST, not fourth. It is the note that says what
    may and may not be said from the platform about a quarrel between Companions. Reading the
    narrative of the siege or of صفين before it is how a speaker ends up with an opinion he then has
    to unlearn.
  · `timeline-and-frontier-23-40ah` is read SECOND. Every note after it names years and places; read
    once, it gives them somewhere to sit.

The numbered PDFs exist because that is how these actually get read — in a file browser, on a phone,
away from the repo. `03-07 the-siege-and-the-killing-of-uthman.pdf` sorts into place on its own.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTES = os.path.join(ROOT, "docs", "research")
OUT = os.path.join(NOTES, "read")

READING = {
    "L01": ("«وقت، جگہ، اور ایک رات» — orientation, Medina's clans, سقیفہ", [
        "tarikh-definition-and-the-guardrail",
        "timeline-pegs",
        "muhajirun-quraysh-structure",
        "medina-ansar-structure",
        "wafat-and-medina-11h",
        "saqifah-bani-saida",
        "saqifah-people-profiles",
        "suhayl-ibn-amr",
        "governors-at-11h",
    ]),
    "L02": ("«بارہ سال» — ابوبکر ؓ and عمر ؓ, 11–23 AH", [
        "arabian-tribes-and-the-ridda-setup",
        "ridda-campaign-the-conduct-of-the-wars",
        "abu-bakr-usama-and-the-jam-of-the-quran",
        "abu-bakr-death-and-the-succession-of-umar",
        "iraq-syria-and-yarmuk-12-15ah",
        "qadisiyya-madain-and-the-embassy",
        "bayt-al-maqdis-and-the-umari-covenant",
        "umar-the-state-diwan-calendar-and-the-two-trials",
        "nahawand-the-shura-and-the-death-of-umar",
        "the-house-of-umm-sulaym",
        "abu-hudhayfa-and-salim-mawla-abi-hudhayfa",
        "zayd-ibn-al-khattab-and-the-dead-of-yamama",
        "the-men-who-had-fought-against-it",
        "great-statements-and-dialogues-11-23ah",
        "ibn-khaldun-on-the-ridda-the-conquests-and-method",
    ]),
    "L03": ("«پہلا امتحان» — عثمان ؓ → علی ؓ, 23–41 AH", [
        "the-mashajarat-and-how-to-narrate-it",
        "timeline-and-frontier-23-40ah",
        "uthman-the-man-and-the-caliphate-begins",
        "uthman-the-conquests-and-the-first-fleet",
        "uthman-the-mushaf-and-the-state",
        "the-grievances-against-uthman",
        "the-siege-and-the-killing-of-uthman",
        "ali-the-man-and-the-bayah",
        "the-battle-of-the-camel",
        "siffin",
        "the-arbitration-and-the-nahrawan",
        "the-khawarij-in-the-prophetic-reports",
        "egypt-and-the-fraying-of-the-command",
        "the-killing-of-ali",
        "the-caliphate-of-hasan-and-the-year-of-unity",
        "the-companions-who-stood-back",
        "the-fadail-of-ali-as-the-books-report-them",
        "the-deaths-of-the-generation-23-40ah",
        "people-of-the-fitna-profiles-i",
        "people-of-the-fitna-profiles-ii",
        "people-of-the-fitna-profiles-iii",
        "great-statements-and-dialogues-23-40ah",
        "ibn-khaldun-on-the-fitna",
    ]),
}

# One line per note saying what it is FOR — written here rather than scraped, because the reader is
# deciding what to read next and needs the point of the note, not its first sentence.
WHY = {
    "the-mashajarat-and-how-to-narrate-it": "**Read this first.** What may and may not be said from the platform about a quarrel between Companions, and the words that close the subject.",
    "timeline-and-frontier-23-40ah": "Every date in the window with its certainty label, the frontier at 23 · 35 · 41 AH, and the gazetteer. Read once, and the rest has somewhere to sit.",
    "uthman-the-man-and-the-caliphate-begins": "ذو النورين — who he was before 24 AH, the بيعة and its terms, his صفة and سيرة, and the فضائل the books record.",
    "uthman-the-conquests-and-the-first-fleet": "إفريقية, قبرص, the first sea battle, and the end of the Sasanian house — the empire still growing while the trouble starts.",
    "uthman-the-mushaf-and-the-state": "The توحيد المصاحف, and the administration: the mosque, the أذان, the عطاء, the ring in the well.",
    "the-grievances-against-uthman": "What was actually complained of, and by whom — the governors, أبو ذر ؓ, ابن مسعود ؓ, the deputations, and what the books themselves say about the reports.",
    "the-siege-and-the-killing-of-uthman": "شوال–ذو الحجة 35 AH: the siege, the water, the men he ordered to sheathe their swords, the killing, and ابن كثير's own refusals.",
    "ali-the-man-and-the-bayah": "Who علي ؓ was, how the بيعة was given and by whom, who held back and on what ground, and why the seat moved to الكوفة.",
    "the-battle-of-the-camel": "How it came about, how near it came to settling, who is reported to have started it, and عائشة ؓ's return with honour.",
    "siffin": "The letters, the water, the weeks of skirmishing, the death of عمار ؓ, and the مصاحف raised on the spears.",
    "the-arbitration-and-the-nahrawan": "التحكيم, دومة الجندل, the withdrawal to حروراء, ابن عباس ؓ's debate with them, and النهروان.",
    "the-khawarij-in-the-prophetic-reports": "The chapter of أحاديث about the خوارج — the richest run of verbatim Arabic in the window, and the safest.",
    "egypt-and-the-fraying-of-the-command": "مصر, the death of الأشتر and of محمد بن أبي بكر ؓ, the raids, and what was left of the command by 40 AH.",
    "the-killing-of-ali": "رمضان 40 AH — ابن ملجم, the night, what he said when struck, the وصية, and the concealed grave.",
    "the-caliphate-of-hasan-and-the-year-of-unity": "The بيعة to الحسن ؓ, the terms of the تسليم, عام الجماعة, and the hadith ابن كثير reads onto it.",
    "the-companions-who-stood-back": "The Companions who refused to fight, and their own stated reasons. The single safest and most useful strand in the session.",
    "the-fadail-of-ali-as-the-books-report-them": "The فضائل chapter with ابن كثير's verdict on each report — sound, weak, rejected. **For the Q&A box, not for the hall.**",
    "the-deaths-of-the-generation-23-40ah": "Who died, year by year. The generation that had seen him ﷺ thinning across exactly the years the fitna arrived.",
    "people-of-the-fitna-profiles-i": "تراجم notices — طلحة ؓ · الزبير ؓ · عائشة ؓ · ابن عوف ؓ · سعد ؓ · عمار ؓ · أبو ذر ؓ · ابن مسعود ؓ.",
    "people-of-the-fitna-profiles-ii": "تراجم notices — عمرو بن العاص ؓ · أبو موسى ؓ · المغيرة ؓ · الأشتر · محمد بن أبي بكر ؓ and the men of الكوفة and صفين.",
    "people-of-the-fitna-profiles-iii": "تراجم notices — معاوية ؓ · الحسن ؓ · ابن عباس ؓ · the governors · كعب الأحبار and the rest.",
    "great-statements-and-dialogues-23-40ah": "The slide-ready Arabic, by speaker. Go here when building the deck, not when learning the story.",
    "ibn-khaldun-on-the-fitna": "How ابن خلدون reads it — **framing only** (`DECISIONS.md` #29), never the authority for a fact.",
}

ISOLATES = str.maketrans({"⁦": None, "⁧": None, "⁨": None, "⁩": None})


def facts(stem):
    """(title, cards, quotations, KB) for a note, or None if it is not written yet."""
    p = os.path.join(NOTES, stem + ".md")
    if not os.path.exists(p):
        return None
    text = io.open(p, encoding="utf-8").read()
    plain = text.translate(ISOLATES)
    m = re.search(r"^#\s+(.+)$", plain, re.M)
    return (m.group(1).strip() if m else stem,
            len(re.findall(r"^### E-", plain, re.M)),
            plain.count("https://shamela.ws/book/"),
            len(text.encode("utf-8")) / 1024.0)


def build():
    lines = [
        "# READING ORDER — the order to read the research in",
        "",
        "> **This is not the order the evening tells the story in.** That order is declared in",
        "> `tools/build_content.py` (`ORDER_L02`, `ORDER_L03`) and is what `CONTENT.md` is emitted in.",
        "> A listener needs events in the order they happened; a reader needs the اصول before the",
        "> quarrel it governs, and the dates before the events that hang off them. Where the two",
        "> orders differ, it is on purpose.",
        "",
        "Regenerate with `python tools/reading_order.py`. Numbered PDFs, which sort correctly in a",
        "file browser or on a phone, are built by `python tools/reading_order.py --pdf` into",
        "`docs/research/read/`.",
        "",
        "**How long this is.** A note is between 20 and 60 minutes of careful reading. Nobody reads",
        "the whole session in one sitting, and nobody should: read to the end of the strand you are",
        "building, then stop.",
        "",
    ]
    only = None
    if "--only" in sys.argv:
        only = sys.argv[sys.argv.index("--only") + 1]
    todo = []
    for key in ("L03", "L02", "L01"):
        if only and key != only:
            continue
        label, stems = READING[key]
        lines += ["---", "", "## %s — %s" % (key, label), "",
                  "| # | Read | What it gives you | Cards | Quotations | Size |",
                  "|---|---|---|---|---|---|"]
        for i, stem in enumerate(stems, 1):
            f = facts(stem)
            n = "%s-%02d" % (key[1:], i)
            if not f:
                lines.append("| **%s** | `%s.md` | ⬜ **not written yet** | — | — | — |" % (n, stem))
                continue
            title, cards, quotes, kb = f
            lines.append("| **%s** | [`%s.md`](%s.md) | %s | %d | %d | %d KB |"
                         % (n, stem, stem, WHY.get(stem, title), cards, quotes, round(kb)))
            todo.append((n, stem))
        lines.append("")
    lines += [
        "---",
        "",
        "## If you only have an hour",
        "",
        "Read, in this order: **03-01** (the اصول — non-negotiable), **03-02** (the dates and the",
        "map), **03-16** (the Companions who stood back), and then whichever single evening you are",
        "about to build. That is enough to stand up and not be caught out.",
        "",
        "## Before any of it reaches a slide",
        "",
        "`python tools/check_citations.py` must report **zero problems** for the note. It compares",
        "every Arabic quotation against the cached Shamela page the citation names (`DECISIONS.md`",
        "#32). And `CLAUDE.md` §1.1 still stands on top of that: locate by grep, **quote by eye** —",
        "read the Arabic off a page image before it is projected.",
    ]
    p = os.path.join(NOTES, "READING_ORDER.md")
    io.open(p, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
    print("%-58s %d notes" % (os.path.relpath(p, ROOT), len(todo)))
    return todo


def pdfs(todo):
    sys.path.insert(0, os.path.join(ROOT, "tools"))
    import render_note
    os.makedirs(OUT, exist_ok=True)
    for n, stem in todo:
        src = os.path.join(NOTES, stem + ".md")
        try:
            made = render_note.render(src, out_dir=OUT)
            final = os.path.join(OUT, "%s %s.pdf" % (n, stem))
            if os.path.exists(final):
                os.remove(final)
            os.rename(made, final)
            print("  %-56s %7.1f KB" % (os.path.basename(final), os.path.getsize(final) / 1024))
        except Exception as e:                                        # noqa: BLE001
            print("  FAILED %-50s %s" % (stem, e))


if __name__ == "__main__":
    t = build()
    if "--pdf" in sys.argv:
        pdfs(t)
