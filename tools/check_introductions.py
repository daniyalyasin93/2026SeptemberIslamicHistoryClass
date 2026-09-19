# -*- coding: utf-8 -*-
"""Who and what walks on stage tonight without ever having been introduced.

    python tools/check_introductions.py S04_kinda_butah_yamama
    python tools/check_introductions.py S04_kinda_butah_yamama --all   # show acknowledged ones too

WHY THIS EXISTS. The evening-4 content review (2026-09-19) found five men carrying cards with no
⁨تراجم⁩ notice anywhere in the delivered series — among them al-Ashʿath b. Qays, who carried seven
cards of an evening and whose only introduction sat inside the block the runsheet said to cut first.
That class of defect is invisible to every other check in this repo: the citations are perfect, the
cards are well formed, and the room still meets a stranger. `CLAUDE.md` §2 and `DECISIONS.md` #43
make the check a rule; this makes it mechanical.

WHAT IT DOES. It walks the evening's RUNSHEET.md in running order and reports, for each card, every
proper name that appears there **for the first time in the whole series** — that is, in no card
listed in `docs/catalogue/DELIVERED.md` and in no earlier card of this same evening.

⚠ **Evening 1's card ids were never recorded** (`DELIVERED.md` says so), so nothing the room met on
the orientation evening — Quraysh, the Anṣār, the Aws and the Khazraj, Saqīfa — is in the known set.
Those will be reported as first appearances. Answer them in the table with "met in evening 1".

WHAT IT DOES NOT DO. It cannot tell whether a name has been *introduced well*, or whether it needs a
notice at all (a name mentioned once in passing usually does not). That judgement is the builder's.
So the runsheet carries the answer, and this tool only asks the question:

    ## Introductions checked

    | Name | Card | How |
    |---|---|---|
    | al-Ashʿath b. Qays | `TSY/E-YK19` | Card of its own; never cut |
    | Ḍirār b. al-Azwar | `RCT/E-RC48` | Named in passing only — no notice needed |

Every first appearance must appear in that table before the evening is built. A name listed there is
silent; a name not listed is reported. **An entry saying "no notice needed" is a valid answer** — the
point is that somebody looked, not that every name gets a paragraph.

It is a reviewer's aid and it is deliberately noisy at the edges: transliterated Arabic names are
hard to tell from a capitalised English word, so expect a few false positives and strike them in the
table with "not a name".
"""
import argparse
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))

DELIVERED = os.path.join(ROOT, "docs", "catalogue", "DELIVERED.md")
CARD_ID = re.compile(r"`([A-Z]+/E-[A-Z]+\d+)`")

# One name token. Transliterated Arabic in this repo carries ā ī ū ḥ ṣ ḍ ṭ ẓ ʿ ʾ and friends; an
# English capital carries none, which is what tells the two apart.
TOKEN = re.compile(r"(?:al-)?[ʿʾA-Z][A-Za-zāīūēōḥṣḍṭẓġḳḫṯḏšʿʾʼ’\u0304\u0323-]*(?:'s|’s)?")
DIACRITIC = re.compile(r"[āīūēōḥṣḍṭẓġḳḫṯḏšʿʾ]")
MARKER = {"abu", "abi", "umm", "ibn", "banu", "b", "bin", "bint", "dhu", "al", "bani", "abd"}
# a segment start: a capital here proves nothing, because every sentence and every beat headline
# begins with one
SEG = re.compile(r"(?:^|[.!?:;—–\n(\[\"“]\s*|\s[-—]\s)")

# Ordinary English words that are capitalised mid-sentence often enough to be noise.
STOP = set("""Allah Prophet Messenger God Lord Islam Muslim Muslims Muslim's Companion Companions
Qur Quran Christians Christian Jews Jewish Arab Arabs Arabia Arabian Peninsula Bedouin History
Historian Historians Book Books Page Chapter Verse Sunni Shia English Arabic Urdu Say Said Speaker
Slide Card Beats Quote Source Map Tier Hands Note Notes Yes No One Two Three Four Five Six Seven
Eight Nine Ten Every Each All Most Many Some Few First Second Third Last Next Same Other Another
Day Night Year Years Month Months Week Morning Evening Tonight Today
He Him His She Her They Them Their We Us Our You Your It Its I Me My Who Whom Whose
That This These Those There And But So Then When While Where What If As At By For From In Into To Of
Commander Believers Grant Enough Lift Separate Disperse Today Yesterday Before After Most Both
Siyar Kamil Kāmil Bidāya Bidaya Nihāya Bukhārī Bukhari Muslim Ṭabarī Tabari Shamela""".split())
STOPF = None       # filled below, folded once


def _initf():
    global STOPF
    STOPF = {fold(x) for x in STOP}


def fold(s):
    """Strip diacritics, the possessive and case, so Khālid's and Khalid are one name."""
    s = re.sub(r"(?:'s|’s)$", "", s)
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^a-z]", "", s.lower())
    return re.sub(r"^al(?=.{3})", "", s)          # al-Yamāma and Yamāma are one place


_INIT = []


def name_tokens(text):
    if not _INIT:
        _initf(); _INIT.append(1)
    """[(token, context)] for every token that looks like a proper name.

    A token counts when it carries a transliteration diacritic, or begins with ʿ, ʾ or 'al-', or
    follows a name-marker (Abū, b., bint …). A bare English capital at the start of a sentence or a
    beat headline counts for nothing — which is what kept "Disperse" and "Including" out.
    """
    starts = {m.end() for m in SEG.finditer(text)}
    out, prev_name, prev_marker = [], None, False
    for m in TOKEN.finditer(text):
        tok = m.group(0)
        if len(tok.rstrip("'’s")) < 3:
            prev_name, prev_marker = None, fold(tok) in MARKER
            continue
        marked = prev_name is not None and prev_marker
        looks = bool(DIACRITIC.search(tok)) or tok.startswith(("al-", "ʿ", "ʾ"))
        k = fold(tok)
        if len(k) < 3:                       # a fragment, not a name: "ʾnā", "al-ʿ"
            prev_name, prev_marker = None, k in MARKER
            continue
        if k in STOPF:
            prev_name, prev_marker = None, k in MARKER
            continue
        # a bare English capital proves nothing at the start of a sentence or a beat headline
        if not looks and not marked and m.start() in starts:
            prev_name, prev_marker = None, k in MARKER
            continue
        # a patronymic is part of the name before it, not a new stranger: "ʿIkrima b. Abī Jahl" is
        # one man, and reporting "Jahl" separately is noise
        if marked and prev_name is not None:
            out.append((re.sub(r"(?:'s|’s)$", "", tok), None, prev_name))
        else:
            a = max(0, m.start() - 34); b = min(len(text), m.end() + 34)
            out.append((re.sub(r"(?:'s|’s)$", "", tok),
                        "…" + text[a:b].replace("\n", " ") + "…", None))
        prev_name, prev_marker = k, k in MARKER
    return out


def card_text(c):
    """Title, narrative and beats — each on its own line, so that a beat's face line counts as a
    sentence start and its opening capital proves nothing."""
    return "\n".join([c.get("title") or "", c.get("what") or ""] +
                     ["%s\n%s" % (h, t) for h, t in (c.get("beats") or [])])


def delivered_ids():
    if not os.path.exists(DELIVERED):
        return []
    return CARD_ID.findall(open(DELIVERED, encoding="utf-8").read())


def acknowledged(runsheet_path):
    """Names the runsheet's '## Introductions checked' table already answers for."""
    txt = open(runsheet_path, encoding="utf-8").read()
    m = re.search(r"##\s*Introductions checked\s*\n(.*?)(?=\n##\s|\Z)", txt, re.S)
    if not m:
        return None
    out = {}
    for line in m.group(1).splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3 or not cells[0] or set(cells[0]) <= set("-: "):
            continue
        if cells[1].lower() in ("card", "first card"):
            continue                      # the table's own header row, not an answer
        out[fold(cells[0])] = cells[2]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("evening", help="the evening folder, e.g. S04_kinda_butah_yamama")
    ap.add_argument("--all", action="store_true", help="list acknowledged first appearances too")
    a = ap.parse_args()

    import build_full_deck as B
    folder = os.path.join(ROOT, a.evening)
    rs = os.path.join(folder, "RUNSHEET.md")
    if not os.path.exists(rs):
        raise SystemExit("no RUNSHEET.md in %s" % a.evening)

    pool = B.pool_cards()
    known = set()
    for cid in delivered_ids():
        if cid in pool:
            for tok, _ctx, _par in name_tokens(card_text(pool[cid])):
                known.add(fold(tok))
    print("%d names known from %s (evenings already delivered)"
          % (len(known), os.path.relpath(DELIVERED, ROOT)))

    ack = acknowledged(rs)
    rows, unacked = [], 0
    for part, cards in B.runsheet(rs):
        for cid, _ in cards:
            c = pool.get(cid)
            if not c:
                continue
            for tok, ctx, parent in name_tokens(card_text(c)):
                k = fold(tok)
                if not k or k in known:
                    continue
                known.add(k)
                if parent is not None and parent in known:
                    continue          # a patronymic of a name the room already has
                answer = None if ack is None else ack.get(k)
                if answer and not a.all:
                    continue
                if not answer:
                    unacked += 1
                rows.append((part.split(" — ")[0], cid, tok, answer or "", ctx))

    if ack is None:
        print("\n⚠ RUNSHEET.md has no '## Introductions checked' table — every first appearance is "
              "listed below.\n  Add the table (see this file's docstring) and answer each row.")
    print("\n%-24s %-16s %-24s %s" % ("PART", "CARD", "FIRST APPEARANCE", "ANSWER"))
    print("-" * 100)
    for part, cid, tok, answer, ctx in rows:
        print("%-24s %-16s %-24s %s" % (part[:24], cid, tok[:24], answer[:32] or "⬜"))
        if not answer:
            print("%s%s" % (" " * 26, ctx[:96]))
    print("\n%d first appearance(s); %d with no answer in the runsheet." % (len(rows), unacked))
    return 1 if unacked else 0


if __name__ == "__main__":
    sys.exit(main())
