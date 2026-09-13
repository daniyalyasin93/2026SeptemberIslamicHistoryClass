"""Promote settled facts out of the research notes into docs/catalogue/ — the source of truth.

    python tools/promote_catalogue.py

WHY THIS EXISTS. CLAUDE.md §0.2: "Once a fact is settled, promote it out of the research note into
`docs/catalogue/` — that is what artifacts read from. Research notes are the working record; the
catalogue is the source of truth." And §4: "Never let two artifacts disagree. A date, a لقب or a
page number goes into docs/catalogue/ first; every artifact reads it from there."

That promotion had not happened. On 2026-09-10 the catalogue still looked as it did on 26 August —
TIMELINE.md 8 lines, LESSONS.md 10 lines — while 28,825 lines of page-cited research had landed in
docs/research/. Daniyal noticed the symptom from the other end: a great deal of researched material
was reaching neither deck.

WHAT THIS SCRIPT DOES, AND WHAT IT DELIBERATELY DOES NOT. Two of the catalogue files are pure
extraction and are rebuilt here at no model cost:

    LESSONS.md    every عبرت line in the pool, with the card and the session block it came from
    TIMELINE.md   every dated card, with its certainty label carried through unchanged

PEOPLE.md, QA_BANK.md and HOWWEKNOW.md are NOT written here. They need judgement — a تراجم notice
has to choose which واقعہ to carry, and a QA answer has to be phrased for a hostile room. Writing
them mechanically would produce something that looks like a catalogue and cannot be trusted as one,
which is worse than an empty file.

The files are REGENERATED, so this is safe to re-run after any research pass. Anything hand-written
below the marker line is preserved.
"""
import os
import re
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import build_full_deck as B                                          # noqa: E402

CAT = os.path.join(ROOT, "docs", "catalogue")
MARK = "<!-- GENERATED ABOVE THIS LINE by tools/promote_catalogue.py — edit below, not above -->"

# a date is worth a timeline row only if it actually fixes a point in time
YEAR = re.compile(r"\d{1,4}\s*(?:AH|ھ|CE|BC)|\bسنة\b|\b\d{1,4}\s*/\s*\d{3,4}\b")
LABEL = re.compile(r"\[(SOURCED|STANDARD|CONVENTIONAL-ESTIMATE)\]")


def keep_tail(path):
    """Whatever a human wrote below the marker survives regeneration."""
    if not os.path.exists(path):
        return ""
    t = open(path, encoding="utf-8").read()
    return t.split(MARK, 1)[1] if MARK in t else ""


def load(session_dir):
    return B.cards_of(os.path.join(ROOT, session_dir, "CONTENT.md"))


def lessons(cards):
    by = defaultdict(list)
    for c in cards:
        if c["ibrah"] and not B.is_na(c["ibrah"]):
            by[c["section"]].append((c["id"], B.clean(c["ibrah"]), c["tier"]))
    out = ["""# LESSONS — every عبرت line in the pool, with its source card

**This file is generated.** Run `python tools/promote_catalogue.py` after any research pass.

`CLAUDE.md` §0.2 — the catalogue is what artifacts read from; the research notes are the working
record. A سبق line that exists only inside a research note cannot be found when a later session
needs it, and two sessions end up drawing the same lesson in different words.

**Each line is drawn from the event itself.** None draws a present-day political parallel
(`DECISIONS.md` #26) — with an organisation in the room, the speaker narrates and does not
adjudicate. A deck uses at most **six** on its closing screen.
"""]
    for sec in sorted(by, key=lambda s: -len(by[s])):
        out.append("\n## %s\n" % sec)
        out.append("| Card | Tier | عبرت |")
        out.append("|---|---|---|")
        for cid, line, tier in by[sec]:
            out.append("| `%s` | %s | %s |" % (cid, tier or "—", line.replace("|", "\\|")))
    total = sum(len(v) for v in by.values())
    out.insert(1, "\n**%d lines across %d blocks.**\n" % (total, len(by)))
    return "\n".join(out), total


def timeline(cards):
    rows = []
    for c in cards:
        when = c["when"] or ""
        if B.is_na(when) or not YEAR.search(when):
            continue
        lab = LABEL.search(when)
        rows.append((B.clean(LABEL.sub("", when)).strip(" ·,-"),
                     lab.group(1) if lab else "—",
                     c["id"], B.clean(c["title"])))
    rows.sort(key=lambda r: (r[0]))
    out = ["""# TIMELINE — every dated event in the pool, with its certainty label

**This file is generated.** Run `python tools/promote_catalogue.py` after any research pass.

**The label is the point of this table.** `CLAUDE.md` §0.1:
`[SOURCED]` a page was read and is given · `[STANDARD]` conventional, not page-cited here, carries
`(to verify)` · `[CONVENTIONAL-ESTIMATE]` general scholarship our sources do not fix — **and that
must be said on the slide itself.** A date whose label is not `[SOURCED]` must never be stated flat
from the platform.

Where two rows disagree about the same event, that disagreement is real and is in the source note.
**Do not resolve it here.** Narrate what the sources narrate and say they differ.
"""]
    out.append("\n**%d dated cards.**\n" % len(rows))
    out.append("| When | Certainty | Card | Event |")
    out.append("|---|---|---|---|")
    for when, lab, cid, title in rows:
        out.append("| %s | `%s` | `%s` | %s |" % (when or "—", lab, cid, title.replace("|", "\\|")))
    return "\n".join(out), len(rows)


def write(name, body, tail):
    p = os.path.join(CAT, name)
    with open(p, "w", encoding="utf-8") as f:
        f.write(body + "\n\n" + MARK + (tail or "\n"))
    return p


# Every session's pool is promoted, not just session 2's — a سبق line or a date that exists only
# in one session's CONTENT.md cannot be found when a later session needs it, which is the exact
# failure this script was written to end.
SESSIONS = ["L02_baarah_saal", "L03_pehla_imtihan"]


if __name__ == "__main__":
    cards = []
    for _s in SESSIONS:
        if os.path.exists(os.path.join(ROOT, _s, "CONTENT.md")):
            cards += load(_s)
    for name, fn in (("LESSONS.md", lessons), ("TIMELINE.md", timeline)):
        tail = keep_tail(os.path.join(CAT, name))
        body, n = fn(cards)
        p = write(name, body, tail)
        print("%-34s %4d rows  %6.1f KB" % (os.path.relpath(p, ROOT), n, os.path.getsize(p) / 1024))
    print("\nPEOPLE.md, QA_BANK.md and HOWWEKNOW.md are NOT generated — they need judgement.")
