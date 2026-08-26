# "Lessons from History" — Series & Lecture 1 Design Spec

**Author:** Daniyal · **Date:** 2026-06-03 · **Venue:** weekly series, DHA (Tuesdays, ~30–45 min, ~10 sessions)
**Source text:** *Tareekh-e-Ummat* by Maulana Muhammad Ismail Rehan (Vol. 1: Muqaddima + Khilāfat-e-Rāshida)

---

## 1. Objectives (merged: yours + management)

1. Give a lay, educated audience a **digestible, enjoyable primer** on Islamic history **after the seerah** (seerah and everything before it is *out of scope* — already covered in the prior series).
2. Install a **mental timeline** ("where are we standing in history") and basic **geography/map** sense; correct the common, map-blind, era-blind "foolish mistakes."
3. Teach the **difference between Western and Islamic historiography** (why we can authenticate what they call "unverifiable") — lightly, not technically.
4. Navigate the ***mushājarāt* of the Sahaba** in a sound **Sunni** frame; present Sunni positions; **no controversial statements**.
5. Stay **rigorously referenced** (every claim traceable) — hence building the course around one strong, close-to-primary-sources book rather than self-authoring.
6. Serve the speaker's needs: **airtight preparation** against stage fright / running dry — full scripts, cue cards, timing.

**Delivery decisions:** Bilingual artifacts (English + Arabic-script terms on slides; full Urdu speaker script). Slides delivered as editable **PowerPoint `.pptx`**. Embellish with own maps + Kings-and-Generals video snips.

---

## 2. The lecture arc (post-seerah) — now 11 sessions

A dedicated "great books & scholars" session (L2) was added at the user's request, so the audience gets the
full flavour of the muqaddima (the giants, the mother-books, the rigour) in a fun way before the narrative.

| # | Title | Core | Map / Timeline |
|---|---|---|---|
| 1 | How do we know? | Methodology-as-thriller; Western vs Islamic historiography; master timeline; world map | Timeline (11 AH→today) + world map |
| 2 | **The Treasure House** | The two pillars; the four stages; the giant historians; the 5 mother-books; the detective science | — |
| 3 | The Rāshida & Abu Bakr ؓ | The 30-yr model; Ridda wars; Qur'an compilation; Fadak (gently) | Arabia |
| 4 | ʿUmar ؓ — the great expansion | Fall of Persia & Byzantium; the dīwān; administration | Conquest maps |
| 5 | ʿUthmān ؓ | Expansion; the standard muṣḥaf; onset of fitna | Empire extent |
| 6 | ʿAlī ؓ & the *mushājarāt* | Jamal, Siffīn — Sunni framework for Sahaba ikhtilāf | — |
| 7 | Khilāfa → Mulk | Ḥasan ؓ; ʿĀm al-Jamāʿah; the handover | — |
| 8 | The Umayyads | Muʿāwiyah → ʿUmar b. ʿAbd al-ʿAzīz; Spain to Sindh; Karbala (carefully) | Widest map |
| 9 | The Abbasids | Golden age; knowledge; historiography itself (ties back to L1–2) | Baghdad-centred |
| 10 | Andalus, Seljuks, Crusades, Mongols | Salāhuddīn; fall of Baghdad 1258 | — |
| 11 | Ottomans → decline → "where are we now" | Close timeline to today; *ʿibrah*; how to keep reading safely | Full timeline |

**Open decision — 10 vs 11 sessions:** management offered "about ten." If 10 is firm, the cleanest compression
is to merge L10+L11 (Andalus→Mongols→Ottomans→today) into a single closing session. Decide before L9.

Guardrail lectures (6 = mushājarāt, 8 = Karbala) come **after** L1 installs the *fiqh of studying fitna* +
husn al-ẓann, and L2 teaches "know your author's lens." Vol. 1 covers through ~L7; later lectures supplemented (sources flagged).

## 2a. Tooling & references discipline

- **Maps** (`tools/`): `grab_frame.py` (yt-dlp + ffmpeg → still frame from a video) and `insert_map.py`
  (fit an image into a slide). See `tools/MAPS_GUIDE.md`. Lecture 1 slide 15 has a ready map placeholder.
- **References are airtight or absent.** Never fabricate a citation, date, title, hadith number, or URL.
  Cite only what traces to the OCR'd source text or a verified primary source; mark anything uncertain
  "to verify." (Recorded permanently in project memory.)

**Timeline orientation peg:** far-left greyed band "Ādam → ʿĪsā ﷺ — centuries of prophets (not our scope)", kept qualitative (no shaky century-count). Bright spine runs 11 AH → 1447 AH/2026.

---

## 3. Lecture 1 — detailed design ("How do we know what really happened?")

Story-led; never announces "today we define history." ~40 min.

1. **Cold open — the forged document (5 min).** 5th-c. Baghdad; Jews present a parchment: Prophet ﷺ waived Khaybar jizya, signed by ʿAlī, Saʿd b. Muʿādh, Muʿāwiyah ؓ. al-Khaṭīb al-Baghdādī declares it forged: Muʿāwiyah accepted Islam *after* Khaybar; Saʿd b. Muʿādh died at Khandaq *before* it. → Hook: history has forensic rules; who owns them? (`Introduction.pdf` p.57–58)
2. **What history actually is (3 min).** Events *ordered in time*, about peoples/lands/figures. Same event in hadith vs poem vs *tarikh* — only tarikh time-orders.
3. **Two ways of knowing the past (10 min, the heart).** Western/modern: conjecture, no isnād, yet hold OT & Ramayana as "authentic." Islamic: isnād + matn + dirāyah + ʿIlm Asmā' al-Rijāl; we grade reports, reject even Wāqidī. Quote (Sufyān al-Thawrī): *"When liars began to forge, we used dates against them."*
4. **Master Timeline reveal — "you are here" (8 min).** Reveal pegs live; build a wall-banner reused weekly. Hijri-calendar origin story (ʿUmar ؓ; "Shaʿbān — which year?"; shūrā; chose Hijra "it separated truth from falsehood").
5. **Geography orientation (5 min).** Map: Makkah/Madina; Byzantine Rome & Sasanian Persia; Hijaz→Sham→Iraq→Egypt→Persia.
6. **Why it matters + the rules (5 min).** *ʿibrah* (*لقد كان في قصصهم عبرة*); fiqh of history — studying mushājarāt without need / with risk to belief is *makrūh*. Pre-frames the sensitive lectures.
7. **Close (2 min).** Tease L2 (the Rāshida begins). Leave banner up.

---

## 4. Lecture 1 deliverables

1. `Lecture1.pptx` — bilingual deck; live-timeline slides; map placeholders with suggested sources.
2. Full **Urdu speaker script** with timing markers + audience-interaction prompts.
3. **"If I blank" cue card** — 6 timeline pegs + 3 stories on one page.
4. **Advice sheet** — pacing, wall-banner, Q&A handling, controversy guardrails.

---

## 5. Key referenced anchors (Lecture 1)

- Forged document / al-Khaṭīb al-Baghdādī — `Introduction.pdf` p.57–58; al-Muntaẓam (Ibn al-Jawzī).
- Islamic vs other historiography — `Introduction.pdf` p.48–49.
- Hijri calendar / Nasī' — `Introduction.pdf` p.35–40; al-Shamārīkh (Suyūṭī); Tabari.
- Sources of history (4 مآخذ), riwāyah/dirāyah — `Introduction.pdf` p.62–64.
- Fiqh ruling on history / mushājarāt makrūh — `Introduction.pdf` p.52–53; al-Iʿlān bi'l-Tawbīkh (Sakhāwī).
- Importance via Qur'an/Hadith — `Introduction.pdf` p.51, 55–56.
