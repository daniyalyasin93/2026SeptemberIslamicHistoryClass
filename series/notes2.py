# -*- coding: utf-8 -*-
"""The lectern, in two tiers (docs/VISION.md §4).

Daniyal delivers from the speaker notes and nothing else (DECISIONS.md #60). Evening 6's first build put
540 to 2,091 words under a single slide, and his verdict was the one that matters: "tooooo much description
in notes, i will get lost trying to find what to say." The content was wanted. The layout buried it.

So a slide's notes are two tiers, and the line between them is drawn on the page:

    ⚠  one line                  only a warning that changes what he SAYS — two at most

    SAY

    1. a cue                     a few words. What comes next. He already knows the story.

    ▶ CLICK 1 — what moves       where a map moves, on the cue it moves with

    2. a cue

    ▶ NEXT SLIDE — the Arabic

    LESSON — one line
    ASK — the hands-up question

    ──────── DETAIL — only if you need it ────────
    1. the cue — and the full sentence behind it
    the quotation, whole, with its speaker and its page

    ──────── BACKGROUND — for home ────────
    everything else the card carries

    ──────── IMAGE BRIEF — paste into the image generator ────────

A blank line stands between every item in the top tier, because he asked for the spacing and because
PowerPoint's notes pane ignores a stored font size — a blank line is the only spacing it cannot take away.

The top tier is budgeted (TOP_WORDS, CUE_WORDS, CUES) and tools/check_vision.py fails a deck that exceeds
it. A card with more to say than the budget holds is two slides, not one long pane.
"""
import re

CUE_WORDS = 12        # a cue is a glance, not a sentence
CUES = 12             # more cues than this on one slide and the card wants splitting
TOP_WORDS = 130       # everything above the DETAIL rule
WARN_WORDS = 18

RULE = "─" * 8
DETAIL = "%s DETAIL — only if you need it %s" % (RULE, RULE)
BACKGROUND = "%s BACKGROUND — for home, not for the lectern %s" % (RULE, RULE)
BRIEF = "%s IMAGE BRIEF — paste into the image generator %s" % (RULE, RULE)
MARKERS = (DETAIL, BACKGROUND, BRIEF)


def words(s):
    return len(re.findall(r"\S+", s or ""))


def top_tier(notes):
    """The part of a notes pane the speaker reads at the lectern — everything above the first rule."""
    cut = len(notes)
    for m in MARKERS:
        i = notes.find(m)
        if i >= 0:
            cut = min(cut, i)
    return notes[:cut].strip()


def compose(c, skip=(), clicks=(), words_follow=False, quote_here=False, warn=(), brief=None,
            speaker=None, clean=lambda s: s, kind=None):
    """The notes of one card slide.

    c             the parsed card (tools/build_full_deck.pool_cards)
    skip          beat numbers the runsheet says to skip (SKIP BEATS 1,2)
    clicks        [(beat number, "what moves"), ...] — a click lands BEFORE that beat's cue
    words_follow  the card's Arabic is on the NEXT slide (a map card with a words slide after it)
    quote_here    the card's Arabic is on THIS slide's face
    warn          one-line warnings that change what he says; two at most reach the top
    brief         the paste-ready image brief, if this slide holds an image placeholder
    """
    skip = set(skip)
    by_beat = {}
    for k, (beat, what) in enumerate(clicks, 1):
        by_beat.setdefault(beat, []).append((k, what))

    top = []
    for w in list(warn)[:2]:
        top.append("⚠ " + clean(w).strip())
    if kind:
        top.append(kind)
    top.append("SAY")
    n = 0
    detail = []
    for i, (cue, det) in enumerate(c.get("beats") or [], 1):
        for k, what in by_beat.get(i, []):
            top.append("▶ CLICK %d — %s" % (k, clean(what)))
        if i in skip:
            continue
        n += 1
        top.append("%d. %s" % (n, clean(cue)))
        detail.append("%d. %s%s" % (n, clean(cue), (" — " + clean(det)) if det else ""))
        if quote_here and c.get("quote_after") == i and c.get("arabic"):
            top.append("   ↑ read the Arabic on the slide")
    if not n and c.get("what"):
        top.append(clean(c["what"]))
    if words_follow:
        top.append("▶ NEXT SLIDE — the Arabic, and its lesson")
    if c.get("ibrah") and not words_follow:
        top.append("LESSON — " + clean(c["ibrah"]))
    hands = (c.get("hands") or "").strip()
    if hands and not re.match(r"^(no\b|—$)", hands, re.I):
        top.append("ASK — " + clean(hands))

    out = ["\n\n".join(top)]

    low = []
    if detail:
        low.append("\n".join(detail))
    if c.get("arabic"):
        q = [c["arabic"]]
        if c.get("english"):
            en = c["english"].strip()
            q.append(en if en[:1] in '"“' else '"' + en + '"')
        q.append("— " + " · ".join(x for x in (speaker, c.get("cite")) if x))
        low.append("\n".join(q))
    if low:
        out.append(DETAIL + "\n\n" + "\n\n".join(low))

    extra = re.sub(r"(?m)^\s*-{3,}\s*$", "", c.get("extra") or "").strip()
    if extra:
        out.append(BACKGROUND + "\n\n" + clean(extra))
    if brief:
        out.append(BRIEF + "\n\n" + brief.strip())
    return "\n\n".join(out)


def words_slide(c, speaker=None, clean=lambda s: s):
    """The slide after a map, holding only the quotation: read it, render it, give the lesson."""
    top = ["READ the Arabic on the slide — then its English."]
    if speaker:
        top.append("WHO IS SPEAKING — " + clean(speaker))
    if c.get("ibrah"):
        top.append("LESSON — " + " ".join(clean(c["ibrah"]).split()[:40]))
    low = [c.get("arabic") or ""]
    if c.get("english"):
        low.append(c["english"].strip())
    if c.get("cite"):
        low.append("— " + c["cite"])
    return "\n\n".join(top) + "\n\n" + DETAIL + "\n\n" + "\n".join(x for x in low if x)


def plain(lines, brief=None):
    """A bridge, a checkpoint, a map that belongs to no card: cue lines, spaced, and nothing else."""
    out = "\n\n".join(x for x in lines if x)
    return out + ("\n\n" + BRIEF + "\n\n" + brief.strip() if brief else "")
