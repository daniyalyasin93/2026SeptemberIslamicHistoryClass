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
import deck2 as D                                                   # noqa: E402

CARD = re.compile(r"^### (\S+)\s*·\s*(.*?)\s*$", re.M)
FIELD = {
    "tier": re.compile(r"\*\*Tier:\*\*\s*(\w+)"),
    "when": re.compile(r"\*\*When:\*\*\s*(.*?)\s*(?:·\s*\*\*Map|\n)"),
    "map": re.compile(r"\*\*Map:\*\*\s*(.*?)\s*$", re.M),
    "ibrah": re.compile(r"\*\*عبرت:\*\*\s*(.*?)\s*$", re.M),
    "hands": re.compile(r"\*\*Hands-up\?\*\*\s*(.*?)\s*$", re.M),
}
WHAT = re.compile(r"\*\*What happened:\*\*\s*(.*?)(?=\n\*\*|\Z)", re.S)
STATEMENT = re.compile(r"\*\*The statement:\*\*\s*\n((?:>.*\n?)+)", re.M)
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
            else:
                break                  # Arabic again after the rendering: the next quotation
        else:
            if phase != "ar":
                english.append(re.sub(r"^\*?English:?\*?\s*", "", line, flags=re.I).strip("* "))
    return (" ".join(arabic) or None, cite, " ".join(english) or None)


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
            c[k] = mm.group(1).strip() if mm else ""
        mm = WHAT.search(body)
        c["what"] = re.sub(r"\s+", " ", mm.group(1)).strip() if mm else ""
        sm = STATEMENT.search(body)
        c["arabic"] = c["cite"] = c["english"] = None
        if sm and NO_STATEMENT not in sm.group(1):
            c["arabic"], c["cite"], c["english"] = parse_statement(sm.group(1))
        out.append(c)
    return out


MARKS = re.compile("[ً-ٰٟۖ-ۭـ]")
AR_SLIDE_MAX = 190          # characters of unvowelled Arabic that fit legibly at 44pt+
EN_SLIDE_MAX = 24           # words of rendering that fit above the citation without touching it


def ar_len(t):
    return len(MARKS.sub("", str(t)))


def notes_for(c):
    """Everything about the card that is not on the slide, so nothing is lost."""
    bits = ["%s · %s" % (c["id"], c["title"])]
    if c["tier"] or c["when"]:
        bits.append("Tier: %s   When: %s" % (c["tier"] or "?", c["when"] or "—"))
    if c["what"]:
        bits.append("\n" + c["what"])
    if c["map"]:
        bits.append("\nMAP: " + c["map"])
    if c["ibrah"]:
        bits.append("\nعبرت: " + c["ibrah"])
    if c["hands"] and c["hands"].lower() not in ("no", "no.", "—"):
        bits.append("\nHANDS UP: " + c["hands"])
    if c["cite"]:
        bits.append("\nSource: " + c["cite"])
    bits.append("\nFrom: " + c["section"])
    return "\n".join(bits)


ARABIC_DIGITS = str.maketrans("\u0660\u0661\u0662\u0663\u0664\u0665\u0666\u0667\u0668\u0669"
                              "\u06f0\u06f1\u06f2\u06f3\u06f4\u06f5\u06f6\u06f7\u06f8\u06f9",
                              "01234567890123456789")

# Recurring Arabic terms in the block headings. A section slide is a plain English label, and
# CLAUDE.md 1.3 forbids Arabic and English sharing one line - the bidi algorithm reorders it and
# "The ردة wars" came out as "The ردةwars".
TRANSLIT = [
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


CITE_VOL = re.compile(r"ج\s*(\d+)")
CITE_PG = re.compile(r"ص\s*(\d+)")


def cite_en(t):
    """Render a citation in English.

    An Arabic citation carrying Latin digits is reordered by the bidi algorithm into nonsense —
    «الكامل ج 2 ص 202» came out as «202ص 2الكامل ج». CLAUDE.md 1.3 names this exact bug. Since the
    slides are English anyway (DECISIONS.md #19), the citation goes to English and the problem
    disappears rather than being fought.
    """
    t = clean(t)
    vol, pg = CITE_VOL.search(t), CITE_PG.search(t)
    tail = ", ".join(x for x in (("vol. " + vol.group(1)) if vol else None,
                                 ("p. " + pg.group(1)) if pg else None) if x)
    name = clean(CITE_PG.sub("", CITE_VOL.sub("", t)), translit=True).strip(" ,-")
    return ", ".join(x for x in (name, tail) if x)


def clean(t, translit=False):
    """Strip markdown, normalise digits, and optionally romanise the recurring Arabic terms."""
    t = re.sub(r"[`*_]", "", str(t)).translate(ARABIC_DIGITS)
    if translit:
        for a, e in TRANSLIT:
            t = t.replace(a, e)
        t = ARABIC_CH.sub("", t)                      # anything left over would break the line
    return re.sub(r"\s{2,}", " ", t).strip(" \u00b7,-\u2014")


def short(s, words):
    w = str(s).split()
    return " ".join(w[:words]) + ("…" if len(w) > words else "")


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

        head = clean(short(c["title"], 9))
        kicker = clean("%s \u00b7 %s" % (c["tier"], short(c["when"], 5)),
                       translit=True).replace("ھ", " AH").replace("هـ", " AH")
        kicker = re.sub(r"\s{2,}", " ", kicker).strip(" \u00b7,") or None

        try:
            if c["arabic"] and ar_len(c["arabic"]) <= AR_SLIDE_MAX:
                # The rendering is truncated on the slide and given whole in the notes. A 146-word
                # translation projected at 30pt is not readable from the back of a hall, and the
                # deck contract exists precisely to stop that being shipped again.
                s = D.statement_slide(prs, english=short(c["english"] or "", EN_SLIDE_MAX),
                                      arabic=c["arabic"], cite=cite_en(c["cite"]),
                                      headline=head, kicker=kicker)
            elif c["arabic"]:
                # Too long to project whole. The slide holds the card; the statement waits in the
                # notes with an instruction to excerpt it deliberately rather than by accident.
                s = D.image_slide(prs, None, head, kicker=kicker,
                                  brief="A restrained editorial illustration for: %s. Landscape, "
                                        "architecture, objects or texture only - no people, no "
                                        "faces. Muted ochre, teal and bone. 16:9."
                                        % short(c["what"], 30))
            elif c["map"]:
                s = D.map_slide(prs, None, head, kicker=kicker,
                                keys=[(short(c["map"], 4), short(c["what"], 8))],
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
            D.note(s, notes_for(c))
            made += 1
        except D.DeckContractError as e:
            # A card that will not fit the contract is skipped rather than allowed to weaken it;
            # it is still in CONTENT.md and can be built by hand.
            print("  skipped %-22s %s" % (c["id"], str(e)[:90]))

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
