"""Assemble a session's CONTENT.md — the event pool Daniyal filters — from the research notes.

    python tools/build_content.py L02_baarah_saal --title "Twelve Years" --span "11-23 AH"

WHY THIS IS A SCRIPT AND NOT A JOB FOR THE MODEL. The eight L02 research notes run to roughly
10,000 lines. Reading them into a model context to compile the pool would be the single largest
avoidable token cost in this project, and it would buy nothing: every note already ends in a
machine-parsable `## EVENT CARDS` section written to a fixed shape (spec v4 §1.1). Concatenating
them is a text operation, so it is done as one.

The output is the artifact of DECISIONS.md #20: an over-built pool, tiered CORE / GOOD / CUT, that
Daniyal deletes rows from until what is left is the lecture. It is deliberately far longer than the
slot — the whole point is that the cutting is his, not ours.

Cards are emitted in NARRATIVE order (the order the evening would tell them), not in the order the
research happened, so the file can be read top to bottom as a draft running order.
"""
import argparse
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTES = os.path.join(ROOT, "docs", "research")

# The order the evening tells them. Notes not listed here are appended after, in filename order,
# so a new strand is never silently dropped.
ORDER = [
    ("arabian-tribes-and-the-ridda-setup", "Setting: the tribal map, and why the ردة took its shape"),
    ("ridda-campaign-the-conduct-of-the-wars", "The ردة wars: the campaign, front by front"),
    ("abu-bakr-usama-and-the-jam-of-the-quran", "جيش أسامة ؓ, and the Qur'an collected"),
    ("abu-bakr-death-and-the-succession-of-umar", "The death of أبو بكر ؓ, and the succession"),
    ("iraq-syria-and-yarmuk-12-15ah", "Iraq, Shām, and يرموك"),
    ("qadisiyya-madain-and-the-embassy", "القادسية, the embassy to رستم, and المدائن"),
    ("bayt-al-maqdis-and-the-umari-covenant", "بيت المقدس and the العهدة العمرية"),
    ("umar-the-state-diwan-calendar-and-the-two-trials", "عمر ؓ builds a state — and the two trials"),
    ("nahawand-the-shura-and-the-death-of-umar", "نهاوند, the assassination, and the شورى"),
    ("the-house-of-umm-sulaym", "The people: the house of أم سليم ؓ"),
    ("abu-hudhayfa-and-salim-mawla-abi-hudhayfa", "The people: أبو حذيفة ؓ and سالم ؓ"),
    ("zayd-ibn-al-khattab-and-the-dead-of-yamama", "The people: زيد بن الخطاب ؓ and the dead of اليمامة"),
    ("the-men-who-had-fought-against-it", "The people: the men who had fought against it"),
    ("great-statements-and-dialogues-11-23ah", "The statements bank — slide-ready, by speaker"),
    ("ibn-khaldun-on-the-ridda-the-conquests-and-method", "ابن خلدون: how he reads it (framing only)"),
]


# --------------------------------------------------------------------------------------------
# CHRONOLOGICAL ORDER
#
# The pool was first assembled note by note, so it came out grouped by RESEARCH STRAND — every
# ridda card, then every أسامة card, and so on. That is the order the research happened in, not the
# order the evening is told in, and Daniyal spotted it reading the file: a reader working down the
# page jumped from ۲۳ھ back to ۱۱ھ at every block boundary.
#
# So cards are now sorted by date. The dates are prose, written by fourteen different agents —
# «۱۱ھ, within days of the delegation's return», «1 المحرم 14ھ», «11ھ→12ھ», «13 AH, at his
# accession» — so the parse is deliberately forgiving and the result is APPROXIMATE, which is all a
# running order needs. Where two cards share a year and month, the original strand order is kept,
# so a sequence a researcher wrote in order stays in order.
#
# Cards with no date at all — Ibn Khaldūn's method and عصبية material, and much of the statements
# bank — are not forced into the timeline. They go to their own section at the end, where they
# belong: they are framing and reference, not events.
# --------------------------------------------------------------------------------------------

AR_DIGITS = str.maketrans("\u0660\u0661\u0662\u0663\u0664\u0665\u0666\u0667\u0668\u0669"
                          "\u06f0\u06f1\u06f2\u06f3\u06f4\u06f5\u06f6\u06f7\u06f8\u06f9",
                          "01234567890123456789")

# A year is digits followed by ھ / هـ / AH, or preceded by سنة. Take the EARLIEST year a card
# names, so a card spanning «۱۱ھ→۱۲ھ» sorts where it starts.
YEAR = re.compile(r"(\d{1,3})\s*(?:\u06be|\u0647\u0640|\u0647\b|AH|A\.H\.)", re.I)
YEAR_CE = re.compile(r"(6[2-9]\d)\s*(?:CE|AD)", re.I)

MONTHS = ["\u0645\u062d\u0631\u0645", "\u0635\u0641\u0631",
          "\u0631\u0628\u064a\u0639 \u0627\u0644\u0623\u0648\u0644", "\u0631\u0628\u064a\u0639 \u0627\u0644\u0622\u062e\u0631",
          "\u062c\u0645\u0627\u062f\u0649 \u0627\u0644\u0623\u0648\u0644", "\u062c\u0645\u0627\u062f\u0649 \u0627\u0644\u0622\u062e\u0631",
          "\u0631\u062c\u0628", "\u0634\u0639\u0628\u0627\u0646", "\u0631\u0645\u0636\u0627\u0646",
          "\u0634\u0648\u0627\u0644", "\u0630\u0648 \u0627\u0644\u0642\u0639\u062f\u0629", "\u0630\u0648 \u0627\u0644\u062d\u062c\u0629"]


def when_key(when):
    """(year, month) for a prose date, or None if the card is not dated."""
    if not when or re.match(r"\s*n\s*/?\s*a\b", str(when), re.I):
        return None
    t = str(when).translate(AR_DIGITS)
    years = [int(y) for y in YEAR.findall(t) if int(y) <= 200]
    if not years:
        ce = [int(y) for y in YEAR_CE.findall(t)]
        if not ce:
            return None
        years = [max(1, ce[0] - 621)]          # rough CE -> AH, only ever a tie-breaker
    month = 13
    for i, m in enumerate(MONTHS, 1):
        if m in t:
            month = min(month, i)
    return (min(years), month)


CARD = re.compile(r"^### (E-[^\s·]+)\s*·\s*(.*?)\s*$", re.M)
TIER = re.compile(r"\*\*Tier:\*\*\s*([A-Z]+)")
WHEN = re.compile(r"\*\*When:\*\*\s*(.*?)\s*(?:·|$)", re.M)
HANDS = re.compile(r"\*\*Hands-up\?\*\*\s*(.*?)\s*$", re.M)
NO_STATEMENT = "none in the sources we use"

# Rough delivery cost of a card, told calmly rather than rushed. Used only to show how far
# over-built the pool is, so the size of the cut is visible before it is made.
MINUTES = {"CORE": 2.0, "GOOD": 1.5, "CUT": 1.0}


def cards_in(path):
    """Split a note's EVENT CARDS section into (id, title, tier, when, has_statement, body)."""
    text = open(path, encoding="utf-8").read()
    # Notes head this section as either "# EVENT CARDS" or "## EVENT CARDS", so match the level
    # rather than a fixed string — a mismatch here silently dropped two thirds of the pool.
    m = re.search(r"^#{1,3}\s*EVENT CARDS.*$", text, re.M)
    if not m:
        return []
    # The cards run until the next heading of the SAME OR HIGHER level. Several notes carry
    # sections AFTER their cards — "WHERE EACH CARD BELONGS", "ADVERSARIAL RE-CHECK", "Promote to
    # the catalogue" — and reading to end-of-file swallowed them into the last card's body, which
    # then went into a slide's speaker notes and into CONTENT.md as if it were narrative.
    section = text[m.end():]
    stop = re.search(r"^#{1,2}\s+\S", section, re.M)
    if stop:
        section = section[:stop.start()]

    out, hits = [], list(CARD.finditer(section))
    for n, m in enumerate(hits):
        body = section[m.end():hits[n + 1].start() if n + 1 < len(hits) else len(section)].strip()
        tier = (TIER.search(body).group(1) if TIER.search(body) else "GOOD")
        when = (WHEN.search(body).group(1) if WHEN.search(body) else "")
        out.append({
            "id": m.group(1), "title": m.group(2), "tier": tier, "when": when,
            "statement": NO_STATEMENT not in body,
            "hands": bool(HANDS.search(body)) and "no" not in (HANDS.search(body).group(1) or "").lower(),
            "body": body,
        })
    return out


def _year_head(y):
    return "%d AH  ·  c. %d CE" % (y, y + 621) if y else "Undated"


def build(session_dir, title, span, out_name="CONTENT.md"):
    stems = {s: t for s, t in ORDER}
    found = {os.path.splitext(f)[0]: os.path.join(NOTES, f)
             for f in os.listdir(NOTES) if f.endswith(".md") and f != "INDEX.md"}

    ordered = [(s, stems[s], found[s]) for s, _ in ORDER if s in found]
    extra = sorted(k for k in found if k not in stems)
    ordered += [(k, k.replace("-", " "), found[k]) for k in extra]

    dated, undated, totals = [], [], {"CORE": 0, "GOOD": 0, "CUT": 0}
    index_rows, missing = [], [s for s, _ in ORDER if s not in found]

    seq = 0
    for stem, heading, path in ordered:
        cs = cards_in(path)
        if not cs:
            continue
        for c in cs:
            totals[c["tier"]] = totals.get(c["tier"], 0) + 1
        index_rows.append("| %s | %d | %d CORE · %d GOOD · %d CUT | %d | `%s.md` |"
                          % (heading, len(cs),
                             sum(1 for c in cs if c["tier"] == "CORE"),
                             sum(1 for c in cs if c["tier"] == "GOOD"),
                             sum(1 for c in cs if c["tier"] == "CUT"),
                             sum(1 for c in cs if c["statement"]), stem))
        # Two notes both used the E-U prefix, so ids are namespaced by note on the way out;
        # otherwise a filtered pool contains two different cards called E-U1.
        tag = "".join(w[0] for w in stem.split("-")[:3]).upper()
        for c in cs:
            seq += 1
            c["_seq"], c["_tag"], c["_stem"], c["_block"] = seq, tag, stem, heading
            (dated if when_key(c["when"]) else undated).append(c)

    dated.sort(key=lambda c: (when_key(c["when"]), c["_seq"]))

    def render(cs):
        return "\n\n".join(
            "### %s/%s · %s\n*%s*\n\n%s" % (c["_tag"], c["id"], c["title"], c["_block"], c["body"])
            for c in cs)

    blocks = []
    year = None
    run = []
    for c in dated:
        y = when_key(c["when"])[0]
        if y != year:
            if run:
                blocks.append("---\n\n## %s\n\n%s" % (_year_head(year), render(run)))
            year, run = y, []
        run.append(c)
    if run:
        blocks.append("---\n\n## %s\n\n%s" % (_year_head(year), render(run)))
    if undated:
        blocks.append("---\n\n## Undated — framing, method, and the statements bank\n\n"
                      "*These carry no date and are not forced into the timeline. They are "
                      "reference the narrative draws on, not events it tells.*\n\n" + render(undated))

    total = sum(totals.values())
    mins = sum(MINUTES.get(t, 1.5) * n for t, n in totals.items())

    head = """# %s — the event pool

**Session 2 · %s · a 45-minute slot.**

> **THIS FILE IS NOT THE LECTURE. IT IS THE POOL YOU CUT DOWN TO ONE.**
> `DECISIONS.md` #20. Delete the rows you do not want. What survives is the evening. Overflow is
> not compressed — it rolls into session 3. Coverage is never bought by speeding up, which is the
> one thing the room objected to last time.

**How to cut.** Read top to bottom; it is in APPROXIMATE CHRONOLOGICAL order, one heading per hijri year. Delete whole cards. Keep
roughly **%d cards** for a 45-minute slot told calmly — the rest is deliberate over-build.

| | |
|---|---|
| Cards in the pool | **%d** |
| If every card were told | **≈ %d minutes** |
| The slot | **45 minutes** |
| So you are cutting | **about %d%%** |

**Tier means:** `CORE` the evening breaks without it · `GOOD` include if time · `CUT` recorded so it
is never re-researched, not planned for delivery.

**Every card carries:** what happened, in tellable English · the date with its certainty label ·
the map move · a verbatim Arabic statement with its printed page and shamela link (or an explicit
"none in the sources we use") · one عبرت line · and whether it opens with a hands-up question.

## What is in the pool

| Research strand | Cards | Tiers | With a statement | Note |
|---|---|---|---|---|
%s

%s
## The cards
""" % (title, span, int(45 / 2.0), total, round(mins), max(0, round(100 * (1 - 45.0 / mins))),
       "\n".join(index_rows),
       ("\n> ⚠ **Not yet written:** %s\n" % ", ".join("`%s.md`" % m for m in missing)) if missing else "")

    out = os.path.join(ROOT, session_dir, out_name)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(head + "\n" + "\n\n".join(blocks) + "\n")

    print("%-42s %d cards  (%d CORE, %d GOOD, %d CUT)  ~%d min of material"
          % (os.path.relpath(out, ROOT), total, totals.get("CORE", 0), totals.get("GOOD", 0),
             totals.get("CUT", 0), round(mins)))
    if missing:
        print("   not yet written: " + ", ".join(missing))
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("session_dir")
    ap.add_argument("--title", default="Session")
    ap.add_argument("--span", default="")
    a = ap.parse_args()
    build(a.session_dir, a.title, a.span)
