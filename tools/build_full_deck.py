"""Emit a slide for EVERY card in CONTENT.md — the whole pool as a deck, for Daniyal to cut.

    python tools/build_full_deck.py L02_baarah_saal

WHY THIS IS A SCRIPT AND NOT AGENTS. Daniyal's instruction: "do not leave any of the cards except
making the output for them, and leave it to me at the end, what to cover in what session." That is
263 cards. Having a model write slide copy for 263 cards would cost more than the whole rest of the
project, and it would add nothing — the research agents already wrote each card in tellable English,
with its verbatim Arabic, its citation, its map move and its عبرت line. Turning that into slides is
a text operation, so it is done as one, at no model cost.

WHAT YOU GET. One slide per card, in narrative order, with section dividers between blocks:

  * a card with a real map move        -> map_slide, the Map: line supplying the key
  * a card carrying an Arabic statement -> statement_slide, Arabic over its English rendering
  * anything else                       -> image_slide with an IMAGE BRIEF placeholder

The card's full narrative, its date, its عبرت line and its source note all go into the SPEAKER
NOTES of its slide, so nothing is lost when a slide is deleted and nothing has to be looked up.

This deck is a PARTS BIN, not a lecture. `L02.pptx` is the crafted session; this is `L02_ALL.pptx`,
every card, so Daniyal can drag any of them into any session he likes. It will be several hundred
slides and that is the point.
"""
import argparse
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "series"))
# every evening's build imports this module; a cp1252 console would crash on the first ʿ or ؓ it prints
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(errors="replace")
import deck2 as D                                                   # noqa: E402

CARD = re.compile(r"^### (\S+)\s*·\s*(.*?)\s*$", re.M)
# Fields run to the next "**Field**" line or a blank line, NOT to the end of the first line: cards are
# hard-wrapped at ~100 columns, and the one-line patterns cut every wrapped عبرت, Map, When and Hands-up
# mid-sentence (found 2026-09-16: "…and then heard the news that" on a closing slide).
# The card's own field labels. A field runs until the next one of these, so that a Map or عبرت
# line continuing onto "**اليمامة**. The enemy camp is at ..." is not cut at that bold run.
NEXT_FIELD = (r"\n?\*\*(?:Tier|When|Map|What happened|The statement|Hands-up\?|Beats|Quote after beat|عبرت):?\*\*")

FIELD = {
    "tier": re.compile(r"\*\*Tier:\*\*\s*(\w+)"),
    "when": re.compile(r"\*\*When:\*\*\s*(.*?)\s*(?:·\s*\n?\s*\*\*Map|\n\*\*|\n\s*\n)", re.S),
    "map": re.compile(r"\*\*Map:\*\*\s*(.*?)(?=" + NEXT_FIELD + r"|\n\s*\n|\Z)", re.S),
    "ibrah": re.compile(r"\*\*عبرت:\*\*\s*(.*?)(?=" + NEXT_FIELD + r"|\n\s*\n|\n---|\Z)", re.S),
    # the field also ends at the next bold heading ("no **Also on the page:** …"): until 2026-09-22 it
    # swallowed that block, and 20 of evening 4's 31 slides carried a false "HANDS UP — no …" cue
    "hands": re.compile(r"\*\*Hands-up\?\*\*\s*(.*?)(?=" + NEXT_FIELD
                        + r"|\n\s*\n|\n⚠|\n---|\n\*\*|\s\*\*[A-Z][^*\n]{1,60}\*\*|\Z)", re.S),
}
def is_na(v):
    """A card field the researcher marked not-applicable.

    It is metadata for us, never text for the room (DECISIONS.md #30). Several notes write it
    as "n/a", "n/a.", or "n/a - hold on the marker", so match the prefix, not the exact value.
    """
    return not str(v or "").strip() or bool(_NA.match(str(v)))


_NA = re.compile(r"\s*n\s*/?\s*a\b", re.I)


# Qualified labels too — "[SOURCED, disputed]" reached a slide face on 2026-09-16 because this matched only the bare form.
# "(to verify)" also comes with a reason attached — "*(to verify: the pages give the battle, not the year)*"
LABEL = re.compile(r"\[(?:SOURCED|STANDARD|CONVENTIONAL-ESTIMATE)[^\]]*\]|\*?\(to verify[^)]*\)\*?", re.I)
WHAT = re.compile(r"\*\*What happened:\*\*\s*(.*?)(?=" + NEXT_FIELD + r"|\Z)", re.S)
STATEMENT = re.compile(r"\*\*The statement:\*\*\s*\n((?:>.*\n?)+)", re.M)
# BEATS (DECISIONS.md #37): one line per event the speaker must tell, drawn only from the card's own text,
#   **Beats:**
#   1. Headline of eight words or fewer — one face line of twenty words or fewer
#   **Quote after beat:** 3
# One slide per beat; the card's quotation slide goes after beat n (0 = before the first).
BEATS = re.compile(r"\*\*Beats:\*\*[ \t]*\n((?:[ \t]*\d+\.[^\n]*\n?)+)")
BEAT_LINE = re.compile(r"^[ \t]*\d+\.\s*(.+?)\s+—\s+(.+?)\s*$", re.M)
QUOTE_AFTER = re.compile(r"\*\*Quote after beat:\*\*\s*(\d+)")
ARABIC_CH = re.compile("[؀-ۿݐ-ݿﭐ-﷿ﹰ-﻿]")
LATIN_CH = re.compile("[A-Za-z]")

NO_STATEMENT = "none in the sources we use"


def parse_statement(block):
    """Pull the FIRST quotation out of a statement block: Arabic, citation, English rendering.

    Two bugs lived here. The English was assigned rather than accumulated, so a two-line rendering
    put only its SECOND line on the slide and the sentence began mid-clause. And a card carrying
    two quotations had both Arabic runs concatenated into one, silently splicing two different
    sayings together. Both are fixed by reading the block as a small state machine and stopping at
    the end of the first quotation.
    """
    arabic, cite, english = [], None, []
    phase = "ar"                       # ar -> cite -> en, then stop at the next Arabic line
    for raw in block.split("\n"):
        line = raw.lstrip("> ").strip()
        if not line:
            continue
        ar, la = len(ARABIC_CH.findall(line)), len(LATIN_CH.findall(line))
        is_cite = line.startswith(("\u2014", "\u2013", "--")) or "shamela.ws" in line
        is_ar = ar > la and not is_cite

        if is_cite and cite is not None and not english and cite.count("(") > cite.count(")"):
            # "ص۲۳۲ (the ransom terms run on to" / "> ج۲ ص۲۳۳ · https://…)" — one citation, two lines
            cite = cite + " " + re.sub(r"\s*\u00b7?\s*https?://\S+", "", line).strip()
            continue
        if is_cite:
            if cite is None:
                # the URL is unreadable projected; the printed page is what a listener can look up
                cite = re.sub(r"\s*\u00b7?\s*https?://\S+", "", line).lstrip("\u2014\u2013- ").strip()
                phase = "en"
            else:
                break                  # a second citation means a second quotation: stop
        elif is_ar:
            if phase == "ar":
                arabic.append(line)
            elif phase == "en" and not english and re.search(r"(?:\bvia|\bfrom|,)\s*$", cite):
                # the citation broke off mid-phrase and wrapped: "— صحيح البخاري ٤٣٧٣, via" /
                # "> ابن عباس ؓ". Read as the next quotation, this line cost ATA/E-TB16 and E-TB17
                # their English rendering.
                cite = cite + " " + line
            else:
                break                  # Arabic again after the rendering: the next quotation
        else:
            if phase != "ar":
                english.append(re.sub(r"^\*?English:?\*?\s*", "", line, flags=re.I).strip("* "))
    strip = lambda v: re.sub(r"</?[a-zA-Z][^>]{0,120}>", "", v).strip() if v else v
    return (strip(" ".join(arabic)) or None, cite, strip(" ".join(english)) or None)


def cards_of(content_md):
    txt = open(content_md, encoding="utf-8").read()
    hits = list(CARD.finditer(txt))
    out = []
    for i, m in enumerate(hits):
        body = txt[m.end():hits[i + 1].start() if i + 1 < len(hits) else len(txt)]
        head = txt.rfind("\n## ", 0, m.start())
        section = txt[head + 4:txt.index("\n", head + 4)].strip() if head > 0 else "The cards"
        c = {"id": m.group(1), "title": m.group(2), "section": section}
        for k, rx in FIELD.items():
            mm = rx.search(body)
            c[k] = re.sub(r"\s+", " ", mm.group(1)).strip() if mm else ""
        mm = WHAT.search(body)
        c["what"] = re.sub(r"\s+", " ", mm.group(1)).strip() if mm else ""
        # Everything a researcher wrote AFTER the Hands-up line: "Also on the page", cross-references,
        # ⚠ teaching warnings, second quotations. notes_for() used to drop all of it, so a finding that
        # lived there never reached a speaker note (found 2026-09-16: Bādhām kept over all Yemen).
        hm = FIELD["hands"].search(body)
        tail = body[hm.end():] if hm else ""
        c["extra"] = re.sub(r"\n-{3,}\s*$", "", tail.strip()).strip()
        bm = BEATS.search(body)
        c["beats"] = [(h.strip(), t.strip()) for h, t in BEAT_LINE.findall(bm.group(1))] if bm else []
        qm = QUOTE_AFTER.search(body)
        c["quote_after"] = min(int(qm.group(1)), len(c["beats"])) if qm else len(c["beats"])
        sm = STATEMENT.search(body)
        c["arabic"] = c["cite"] = c["english"] = None
        if sm and NO_STATEMENT not in sm.group(1):
            c["arabic"], c["cite"], c["english"] = parse_statement(sm.group(1))
        out.append(c)
    return out


POOLS = ("L02_baarah_saal", "L03_pehla_imtihan")
RUNSHEET_ROW = re.compile(r"^\|\s*\d+\s*\|\s*`([A-Z]+/E-[A-Z]+\d+)`[^|]*\|[^|]*\|[^|]*\|[^|]*\|\s*(.*?)\s*\|\s*$")


def pool_cards():
    """Every card in every era pool, by full id (DECISIONS.md #33)."""
    out = {}
    for d in POOLS:
        for c in cards_of(os.path.join(ROOT, d, "CONTENT.md")):
            out[c["id"]] = c
    return out


def runsheet(path):
    """[(part heading, [(card id, runsheet note), ...]), ...] from the tables under '## Part' headings.

    Rows the speaker has moved under any other heading are not part of the evening and are ignored.
    """
    parts, cur = [], None
    for line in open(path, encoding="utf-8"):
        if line.startswith("## "):
            cur = (line[3:].strip(), []) if line.startswith("## Part") else None
            if cur:
                parts.append(cur)
            continue
        m = RUNSHEET_ROW.match(line) if cur else None
        if m:
            cur[1].append((m.group(1), m.group(2)))
    return parts



MARKS = re.compile("[ً-ٰٟۖ-ۭـ]")
AR_SLIDE_MAX = 180          # unvowelled Arabic that fits at 44pt: three lines of 60, and a line of English
EN_SLIDE_MAX = 24           # words of rendering that fit above the citation without touching it


def ar_len(t):
    return len(MARKS.sub("", str(t)))


def notes_for(c):
    """The lectern view of the card: speaking points first, apparatus last.

    DECISIONS.md #39/#40. Until 2026-09-19 this opened with the card id, the tier and the `When`
    line, and buried the beats — so the first thing the speaker's eye met in the notes pane was
    production apparatus he can do nothing with mid-sentence. The order is now the order he needs
    it in: what to SAY, then the quotation, then the one-line عبرت, then the cues, then background
    he read at home and does not read aloud. Card id, tier and section are gone; traceability
    lives in the evening's RUNSHEET.md and SLIDES.md.
    """
    bits = []
    if c["beats"]:
        say = ["SAY —"]
        for i, (head, line) in enumerate(c["beats"], 1):
            say.append("%d. %s — %s" % (i, head, line))
            if c.get("quote_after") == i and c["arabic"]:
                say.append("   ^ read the Arabic on the face here")
        bits.append("\n".join(say))
    elif c["what"]:
        bits.append("SAY —\n" + c["what"])

    if c["arabic"]:
        q = ["QUOTE — " + c["arabic"]]
        if c["english"]:
            # The note already writes the rendering inside quotation marks; do not double them.
            en = c["english"].strip()
            q.append(en if en[:1] in '"\u201c' else '"' + en + '"')
        if c["cite"]:
            q.append("— " + c["cite"])
        bits.append("\n".join(q))

    if c["ibrah"]:
        bits.append("عبرت — " + c["ibrah"])
    no = re.match(r"^no\b[\s.,;:\u2014\u2013-]*(.*)$", c["hands"] or "", re.I | re.S)
    if no:
        if no.group(1).strip("* "):
            bits.append("\u26a0 " + no.group(1).replace("**", "").strip("* "))
    elif c["hands"] and c["hands"] != "\u2014":
        bits.append("HANDS UP — " + c["hands"])
    if c["map"] and not is_na(c["map"]):
        bits.append("MAP — " + c["map"])

    extra = re.sub(r"(?m)^\s*-{3,}\s*$", "", c.get("extra") or "").strip()
    if extra:
        # A ⚠ box is a delivery instruction, not background: it goes above the prose, not below it.
        warn = [b for b in re.split(r"\n\s*\n", extra) if "⚠" in b]
        rest = [b for b in re.split(r"\n\s*\n", extra) if "⚠" not in b]
        if warn:
            bits.append("\n\n".join(w.strip() for w in warn))
        extra = "\n\n".join(r.strip() for r in rest).strip()

    tail = []
    if c["beats"] and c["what"]:
        tail.append(c["what"])
    if extra:
        tail.append(extra)
    if tail:
        bits.append("BACKGROUND (read at home, not aloud) —\n" + "\n\n".join(tail))

    return "\n\n".join(bits)


HON_KEEP = re.compile("[\u0610-\u0615\u0617-\u061A\uFDFA\uFDFB]")

ARABIC_DIGITS = str.maketrans("\u0660\u0661\u0662\u0663\u0664\u0665\u0666\u0667\u0668\u0669"
                              "\u06f0\u06f1\u06f2\u06f3\u06f4\u06f5\u06f6\u06f7\u06f8\u06f9",
                              "01234567890123456789")

# Recurring Arabic terms in the block headings. A section slide is a plain English label, and
# CLAUDE.md 1.3 forbids Arabic and English sharing one line - the bidi algorithm reorders it and
# "The ردة wars" came out as "The ردةwars".
TRANSLIT = [
    ("أبو عبيدة", "Abu Ubayda"),
    ("حديقة الموت", "Hadiqat al-Mawt"),
    ("ذو القصّة", "Dhu al-Qassa"),
    ("ذو القصة", "Dhu al-Qassa"),
    ("أم زمل", "Umm Zaml"),
    ("الجابية", "al-Jabiya"),
    ("الفُجاءة", "al-Fuja'a"),
    ("البُطاح", "al-Butah"),
    ("عَقْرَباء", "Aqraba"),
    ("بُزاخة", "Buzakha"),
    ("جُواثى", "Juwatha"),
    ("دارين", "Darin"),
    ("دَبا", "Daba"),
    ("الأبرق", "al-Abraq"),
    ("خالد", "Khalid"),
    ("أم سليم", "Umm Sulaym"),
    ("أبو حذيفة", "Abu Hudhayfa"),
    ("سالم", "Salim"),
    ("زيد بن الخطاب", "Zayd b. al-Khattab"),
    ("اليمامة", "al-Yamama"),
    ("العهدة العمرية", "the Umari Covenant"),
    ("أسامة", "Usama"),
    ("أبو بكر الصديق", "Abu Bakr al-Siddiq"),
    ("الردة", "Ridda"),
    ("\u0627\u0644\u0631\u062f\u0629", "Ridda"), ("\u0631\u062f\u0629", "Ridda"),
    ("\u062c\u064a\u0634 \u0623\u0633\u0627\u0645\u0629", "Jaysh Usama"),
    ("\u0623\u0628\u0648 \u0628\u0643\u0631", "Abu Bakr"), ("\u0639\u0645\u0631", "Umar"),
    ("\u064a\u0631\u0645\u0648\u0643", "Yarmuk"),
    ("\u0627\u0644\u0642\u0627\u062f\u0633\u064a\u0629", "al-Qadisiyya"),
    ("\u0631\u0633\u062a\u0645", "Rustam"),
    ("\u0627\u0644\u0645\u062f\u0627\u0626\u0646", "al-Mada'in"),
    ("\u0628\u064a\u062a \u0627\u0644\u0645\u0642\u062f\u0633", "Bayt al-Maqdis"),
    ("\u0627\u0644\u0639\u0647\u062f\u0629 \u0627\u0644\u0639\u0645\u0631\u064a\u0629", "the Umari Covenant"),
    ("\u0646\u0647\u0627\u0648\u0646\u062f", "Nahawand"),
    ("\u0627\u0644\u0634\u0648\u0631\u0649", "the shura"), ("\u0634\u0648\u0631\u0649", "shura"),
    ("\u0627\u0628\u0646 \u062e\u0644\u062f\u0648\u0646", "Ibn Khaldun"),
    ("\u0639\u0628\u0631\u062a", "ibrah"),
    ("الکامل فی التاریخ", "al-Kamil"),     # Persian kāf/yā spellings, as the notes write them
    ("الکامل", "al-Kamil"),
    ("الكامل فى التاريخ", "al-Kamil"),
    ("الكامل في التاريخ", "al-Kamil"),
    ("الكامل", "al-Kamil"),
    ("البدايه والنهايه", "al-Bidaya wa'l-Nihaya"),
    ("البداية والنهاية", "al-Bidaya wa'l-Nihaya"),
    ("البدایہ والنہایہ", "al-Bidaya wa'l-Nihaya"),
    ("سير أعلام النبلاء", "Siyar A'lam al-Nubala"),
    ("سیر أعلام النبلاء", "Siyar A'lam al-Nubala"),
    ("صحيح البخاري", "Sahih al-Bukhari"),
    ("صحيح مسلم", "Sahih Muslim"),
    ("تاريخ ابن خلدون", "Tarikh Ibn Khaldun"),
    ("مقدمة ابن خلدون", "the Muqaddima"),
    ("الإعلان بالتوبيخ", "al-I'lan bi'l-Tawbikh"),
]


CITE_VOL = re.compile(r"جـ?\s*(\d+)")
CITE_PG = re.compile(r"ص\s*(\d+(?:\s*[\u2013-]\s*\d+)?)")


def cite_en(t):
    """Render a citation in English.

    An Arabic citation carrying Latin digits is reordered by the bidi algorithm into nonsense —
    «الكامل ج 2 ص 202» came out as «202ص 2الكامل ج». CLAUDE.md 1.3 names this exact bug. Since the
    slides are English anyway (DECISIONS.md #19), the citation goes to English and the problem
    disappears rather than being fought.
    """
    t = clean(t)
    # What follows a " · " is the researcher's remark ("straddles the page break"), and a
    # ", via …" clause is the chain of narrators. Both belong in the notes, not in front of the room.
    t = re.split(r"\s+\u00b7\s+", t)[0]
    t = re.sub(r",?\s+(?:via|from)\b.*$", "", t)
    t = re.sub(r"\s*\([^()]*[A-Za-z][^()]*\)", "", t)          # "(opening words)", "(the page turn …)"
    t = re.sub(r"\s*\([^()]*$", "", t)                           # a remark the URL strip left unclosed
    # The volume and page belong to the book they cite — the first segment — so a second authority
    # ("— Sahih al-Bukhari 2845") follows the page instead of splitting the book from it.
    head, _, rest = t.partition(" \u2014 ")
    vol, pg = CITE_VOL.search(head), CITE_PG.search(head)
    pages = pg and re.sub(r"\s*[\u2013-]\s*", "\u2013", pg.group(1))
    tail = ", ".join(x for x in (("vol. " + vol.group(1)) if vol else None,
                                 (("pp. " if "\u2013" in pages else "p. ") + pages) if pg else None)
                     if x)
    name = clean(CITE_PG.sub("", CITE_VOL.sub("", head)), translit=True)
    name = re.sub(r"\s*\(\s*\)", "", name).strip(" ,-")          # a volume title with no romanisation
    out = ", ".join(x for x in (name, tail) if x)
    rest = clean(rest, translit=True).strip(" ,-") if rest else ""
    return out + (" \u2014 " + rest if rest else "")


TIER_LEAD = re.compile(r"^\s*(?:CORE|GOOD|CUT)\b\s*[\u2014\u2013:.\-]*\s*", re.I)
HTML_TAG = re.compile(r"</?[a-zA-Z][^>]{0,120}>")
CARD_REF = re.compile(r"\(?\s*(?:see\s+)?(?:[A-Z]{2,4}/)?E-[A-Z]{1,4}\d+[^)\n]{0,40}?\)?", re.I)


AR_WORD = re.compile("[\u0621-\u064A\u066E-\u06D3]{2,}")


def romanise(t):
    """Apply the transliteration table only — no stripping."""
    for a, e in TRANSLIT:
        t = t.replace(a, e)
    return t


def headline_for(title):
    """A projected headline must not mix scripts (CLAUDE.md 1.3) — unless the alternative is worse."""
    if AR_WORD.search(romanise(title)):
        return clean(title)                  # something has no romanisation: keep it whole
    return clean(title, translit=True)


def clean(t, translit=False):
    """Strip markdown, normalise digits, and optionally romanise the recurring Arabic terms.

    Also removes card cross-references. Researchers write "(see E-HS4)" inside a card's
    prose to point at another card; that is apparatus for us and meaningless to the room
    (DECISIONS.md #30).
    """
    # Some notes wrap their Arabic in <div dir="rtl"> … </div>. The tag is markup for a
    # rendered page, and it was printing literally on slides.
    t = HTML_TAG.sub("", str(t))
    t = CARD_REF.sub("", t)
    # a few notes wrote the tier into the card TITLE ("CUT - recorded so it is never...")
    t = TIER_LEAD.sub("", t)
    t = re.sub(r"[`*_]", "", t).translate(ARABIC_DIGITS)
    if translit:
        for a, e in TRANSLIT:
            t = t.replace(a, e)
        # Keep the honorific marks (ؓ ﷺ) — they are single glyphs, they read correctly
        # beside English, and deck2 sets them in a face that has them. Strip only
        # Arabic WORDS that had no transliteration.
        t = HON_KEEP.sub(lambda m: "\x00%d\x00" % ord(m.group(0)), t)
        t = ARABIC_CH.sub("", t)
        t = re.sub(r"\x00(\d+)\x00", lambda m: chr(int(m.group(1))), t)
        # stripping can leave a heading dangling — "The people: and", "and the dead of".
        # A section slide is projected, so a fragment is worse than a slightly blunt title.
        t = re.sub(r"\s{2,}", " ", t)
        t = re.sub(r"[\s,·:—–-]*\b(?:and|of|the|for|in|to)\b[\s,·:—–-]*$", "", t, flags=re.I)
        t = re.sub(r"^[\s,·:—–-]+|[\s,·:—–-]+$", "", t)
    return re.sub(r"\s{2,}", " ", t).strip(" \u00b7,-\u2014")


def face(v):
    """Text bound for a slide FACE. Empty if the researcher marked it n/a."""
    return "" if is_na(v) else str(v)


def short(s, words):
    w = str(s).split()
    return " ".join(w[:words]) + ("…" if len(w) > words else "")


def kicker_for(c):
    """The date line over a slide's headline. ONLY the date reaches the slide face: the tier, the
    certainty label and the card id are production apparatus and belong in the speaker notes
    (DECISIONS.md #30) — deck2's audit refuses a build that puts any of them in front of the room."""
    # strip the labels BEFORE the six-word cut: cut first, "*(to verify: the pages…*" lost its closing paren
    kicker = clean(short(LABEL.sub("", face(c["when"])), 6), translit=True).replace("ھ", " AH")
    return re.sub(r"\s{2,}", " ", kicker).strip(" ·,-") or None


def beat_slide(prs, c, i, extra_notes=""):
    """Beat i (1-based) of a card: its headline and one line, as a large statement. Returns the slide or None."""
    head, line = c["beats"][i - 1]
    try:
        s = D.statement_slide(prs, english=clean(line), headline=clean(head), kicker=kicker_for(c))
    except D.DeckContractError as e:
        print("  skipped %s beat %d  %s" % (c["id"], i, str(e)[:90]))
        return None
    listing = "\n".join("%s %d. %s — %s" % ("▶" if k == i else " ", k, h, t)
                        for k, (h, t) in enumerate(c["beats"], 1))
    D.note(s, (extra_notes + "\n\n" if extra_notes else "") +
           "BEAT %d of %d — %s · %s\n\n%s\n\nThe quotation and the full card are on the card's own slide."
           % (i, len(c["beats"]), c["id"], c["title"], listing))
    return s


def card_slide(prs, c, extra_notes="", arabic_on_face=True, face_text=None, face_quote=None,
               tail_notes=""):
    """One card -> one slide, by the rules in the module docstring. Returns the slide, or None.

    `arabic_on_face=False` keeps the statement in the speaker notes only: for a quotation that must
    not be projected, such as words a claimant's own people used of him to save their lives.
    `face_text` puts one plain English sentence on the face instead — use it with arabic_on_face=False
    when the card's own rendering is the thing that must not be shown.
    `face_quote` is an (arabic, english) excerpt authored for the face — both halves cut to the same
    clause, the evening's build checks they are the card's own words. The notes keep the whole quotation.
    """
    notes_c = c
    if face_quote:
        c = dict(c, arabic=face_quote[0], english=face_quote[1])
    if not arabic_on_face:
        c = dict(c, arabic=None)
    head = headline_for(short(face(c["title"]), 9))
    # ONLY the date reaches the slide face. The tier, the certainty label and the card id
    # are production apparatus and belong in the speaker notes (DECISIONS.md #30) — deck2's
    # audit now refuses a build that puts any of them in front of the room.
    # strip the labels BEFORE the six-word cut: cut first, "*(to verify: the pages\u2026*" lost its closing paren
    kicker = clean(short(LABEL.sub("", face(c["when"])), 6), translit=True).replace("\u06be", " AH")
    kicker = re.sub(r"\s{2,}", " ", kicker).strip(" \u00b7,-") or None

    try:
        if face_text:
            s = D.statement_slide(prs, english=face_text, headline=head, kicker=kicker)
        elif c["arabic"] and ar_len(c["arabic"]) <= AR_SLIDE_MAX:
            # The rendering is truncated on the slide and given whole in the notes. A 146-word
            # translation projected at 30pt is not readable from the back of a hall, and the
            # deck contract exists precisely to stop that being shipped again.
            # the whole rendering: statement_slide measures it and cuts at a clause only if it must.
            # A blind 24-word cut here threw away words that fitted ("…he had meant nothing but…").
            s = D.statement_slide(prs, english=clean(face(c["english"])),
                                  arabic=c["arabic"], cite=face(cite_en(c["cite"])),
                                  headline=head, kicker=kicker)
        elif c["arabic"]:
            # Too long to project whole. The slide holds the card; the statement waits in the
            # notes with an instruction to excerpt it deliberately rather than by accident.
            s = D.image_slide(prs, None, head, kicker=kicker,
                              brief="A restrained editorial illustration for: %s. Landscape, "
                                    "architecture, objects or texture only - no people, no "
                                    "faces. Muted ochre, teal and bone. 16:9."
                                    % short(c["what"], 30))
        elif not is_na(c["map"]):
            s = D.map_slide(prs, None, head, kicker=kicker,
                            keys=[(clean(short(face(c["map"]), 4)), clean(short(face(c["what"]), 8)))],
                            brief="A restrained editorial illustration for: %s. Landscape, "
                                  "architecture, objects or texture only — no people, no faces. "
                                  "Muted ochre, teal and bone. 16:9."
                                  % short(c["what"], 30))
        else:
            s = D.image_slide(prs, None, head, kicker=kicker,
                              brief="A restrained editorial illustration for: %s. Landscape, "
                                    "architecture, objects or texture only — no people, no "
                                    "faces. Muted ochre, teal and bone. 16:9."
                                    % short(c["what"], 30))
        D.note(s, (extra_notes + "\n\n" if extra_notes else "") + notes_for(notes_c)
               + ("\n\n" + tail_notes if tail_notes else ""))
        return s
    except D.DeckContractError as e:
        # A card that will not fit the contract is skipped rather than allowed to weaken it;
        # it is still in CONTENT.md and can be built by hand.
        print("  skipped %-22s %s" % (c["id"], str(e)[:90]))
        return None


def build(session_dir, out_name="L02_ALL.pptx"):
    content = os.path.join(ROOT, session_dir, "CONTENT.md")
    cards = cards_of(content)
    prs = D.deck()

    D.title_slide(prs, "Every card", "%d cards · the whole pool" % len(cards),
                  "Session 2 · parts bin")
    D.statement_slide(
        prs,
        english="This deck is not a lecture. It is one slide per researched card, in order, "
                "for you to delete from. Each slide's speaker notes carry the full narrative, "
                "the date, the map move, the عبرت line and the source.",
        headline="How to use this deck")

    section = None
    made = 0
    for c in cards:
        if c["section"] != section:
            section = c["section"]
            D.section_slide(prs, clean(section, translit=True))

        if card_slide(prs, c):
            made += 1

    out = os.path.join(ROOT, session_dir, out_name)
    D.save(prs, out)
    print("   %d of %d cards became slides" % (made, len(cards)))
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("session_dir")
    ap.add_argument("--out", default="L02_ALL.pptx")
    a = ap.parse_args()
    build(a.session_dir, a.out)
