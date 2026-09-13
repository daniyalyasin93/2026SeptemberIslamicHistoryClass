"""Check every event card in a pool carries the fields the downstream artifacts read.

    python tools/check_cards.py L03_pehla_imtihan
    python tools/check_cards.py L02_baarah_saal L03_pehla_imtihan --quiet

WHY. A card is the only place a narrative fact is authored (spec v4 §1.1); `SLIDES.md`, the deck,
the cue sheet and the briefing all derive from it. `tools/build_content.py` is forgiving on the way
through — a card with no `**Tier:**` silently becomes GOOD, a card with no `**When:**` silently gets
an empty date — which is right for assembling a pool but wrong for trusting one. A missing عبرت line
is a slide that has nothing to say; a missing Map line is a map that does not move; an id that
repeats is two different cards that cannot both be cut.

So the pool is linted separately, here, and it costs nothing:

    MISSING_FIELD   Tier · When · Map · What happened · عبرت · Hands-up?
    BAD_TIER        not one of CORE / GOOD / CUT
    NO_LABEL        the When line carries no certainty label and no n/a
    DUPLICATE_ID    two cards with the same id
    APPARATUS       production apparatus on what will become a slide face (DECISIONS #30)
    STUB            What happened is under 120 characters — not enough to say aloud

APPARATUS is the one that matters most. `series/deck2.py` already refuses to build a deck with a
certainty label or a card id on a slide FACE, but it cannot see a card whose *narrative* carries
`[SOURCED]` or a cross-reference, because that goes into the speaker notes and from there into the
briefing. Catching it in the pool is catching it before it is copied four times.
"""
import io
import os
import re
import sys
import collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARD = re.compile(r"^### ([A-Z0-9/\-]+)\s*·\s*(.*?)\s*$", re.M)
TIERS = ("CORE", "GOOD", "CUT")
# A label may be qualified — `[SOURCED, disputed]`, `[STANDARD] (to verify)` — and a card that is a
# rule rather than an event legitimately has no date at all, so both forms are accepted.
LABEL = re.compile(r"\[(?:SOURCED|STANDARD|CONVENTIONAL-ESTIMATE)|n/a|[Nn]o date|"
                   r"not fixed|undated|not dated")
FIELDS = [("**Tier:**", "Tier"), ("**When:**", "When"), ("**Map:**", "Map"),
          ("**What happened:**", "What happened"), ("**عبرت:**", "عبرت"),
          ("**Hands-up?**", "Hands-up?")]
# Apparatus that must never ride inside the narrative a speaker reads out or a slide shows.
APPARATUS = re.compile(r"\[SOURCED\]|\[STANDARD\]|\[CONVENTIONAL-ESTIMATE\]|\(to verify\)|"
                       r"IMAGE BRIEF|CUT-IF-SHORT|\bGemini\b|\bClaude\b|AI-generated|"
                       r"shamela\.ws|Tier:|speaker's discretion")
ISOLATES = str.maketrans({"⁦": None, "⁧": None, "⁨": None, "⁩": None})


def cards_of(path):
    text = io.open(path, encoding="utf-8").read().translate(ISOLATES)
    hits = list(CARD.finditer(text))
    for n, m in enumerate(hits):
        end = hits[n + 1].start() if n + 1 < len(hits) else len(text)
        yield m.group(1), m.group(2), text[m.end():end], text[:m.start()].count("\n") + 1


def check(path):
    problems, ids, n = [], collections.Counter(), 0
    for cid, title, body, line in cards_of(path):
        n += 1
        ids[cid] += 1
        say = lambda kind, why: problems.append((line, cid, kind, why))       # noqa: E731

        for marker, name in FIELDS:
            if marker not in body:
                say("MISSING_FIELD", name)

        m = re.search(r"\*\*Tier:\*\*\s*([A-Za-z]+)", body)
        if m and m.group(1) not in TIERS:
            say("BAD_TIER", m.group(1))

        m = re.search(r"\*\*When:\*\*(.*?)\n", body, re.S)
        if m and not LABEL.search(m.group(1)):
            say("NO_LABEL", m.group(1).strip()[:50])

        m = re.search(r"\*\*What happened:\*\*(.*?)(?:\n\s*\*\*|\Z)", body, re.S)
        narrative = (m.group(1).strip() if m else "")
        if m and len(narrative) < 120:
            say("STUB", "%d chars" % len(narrative))
        bad = APPARATUS.search(narrative)
        if bad:
            say("APPARATUS", bad.group(0))

    for cid, c in ids.items():
        if c > 1:
            problems.append((0, cid, "DUPLICATE_ID", "appears %d times" % c))
    return n, problems


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    quiet = "--quiet" in sys.argv
    total = bad = 0
    for a in args or ["L03_pehla_imtihan"]:
        path = a if a.endswith(".md") else os.path.join(ROOT, a, "CONTENT.md")
        if not os.path.exists(path):
            print("no such pool: %s" % path)
            continue
        n, probs = check(path)
        total += n
        bad += len(probs)
        kinds = collections.Counter(p[2] for p in probs)
        print("%-30s %5d cards  %4d problems  %s"
              % (os.path.basename(os.path.dirname(path)), n, len(probs),
                 " ".join("%s=%d" % kv for kv in kinds.most_common()) or "clean"))
        if not quiet:
            for line, cid, kind, why in probs[:80]:
                out = "   %-14s %-18s %s\n" % (kind, cid, why)
                sys.stdout.buffer.write(out.encode("utf-8"))
            if len(probs) > 80:
                print("   … and %d more" % (len(probs) - 80))
    print("\n%d cards, %d problems" % (total, bad))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
