#!/usr/bin/env python3
"""Build assets/data/mfs-video-checks.json from video-solution.html + read-only VTTs."""

import glob
import json
import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, SCRIPT_DIR)

from video_checks_topics_bank import TOPIC_CHECKS_BANK
from video_checks_mocks_bank import EXACT_QUESTION_CCQS, LEGACY_MATHS_MOCK_CCQS

VERSION = "2026-11-20-v1"
FORBIDDEN_WORDS = ("nhs", "oxford health", "undefined", "nan")


def normalize_tutor(badge: str, section: str, title: str, slug: str) -> str:
    """Normalize tutor name to Sonya, Emma, or Subi."""
    hay = f"{badge} {section} {title} {slug}".lower()
    if "sonya" in hay or "sonia" in hay:
        return "Sonya"
    if "emma" in hay:
        return "Emma"
    if "subi" in hay:
        return "Subi"
    if "slc-task1" in slug or "slc-task2" in slug:
        return "Subi"
    return "Subi"


def detect_subject(category: str, series: str, slug: str) -> str:
    """Classify subject domain: maths, english, dfs, or slc."""
    s = f"{category} {series} {slug}".lower()
    if category == "slc" or "slc" in slug:
        return "slc"
    if "digital" in s or "dfs" in slug:
        return "dfs"
    if "english" in s:
        return "english"
    return "maths"


def parse_vtt_file(rel_path: str):
    """Read-only WebVTT parser returning [(start_sec, end_sec, label), ...]."""
    if not rel_path:
        return []
    full = os.path.join(ROOT_DIR, rel_path)
    if not os.path.exists(full):
        raise FileNotFoundError(f"Missing VTT referenced in catalog: {rel_path}")
    lines = open(full, encoding="utf-8", errors="ignore").read().splitlines()
    cues = []
    i = 0

    def to_sec(ts: str) -> float:
        ts = ts.strip().split()[0].replace(",", ".")
        parts = [float(x) for x in ts.split(":")]
        if len(parts) == 3:
            return parts[0] * 3600 + parts[1] * 60 + parts[2]
        return parts[0] * 60 + parts[1]

    while i < len(lines):
        if "-->" in lines[i]:
            p0, p1 = lines[i].split("-->", 1)
            start = to_sec(p0)
            end = to_sec(p1)
            i += 1
            text_lines = []
            while i < len(lines) and lines[i].strip():
                text_lines.append(lines[i].strip())
                i += 1
            label = " ".join(text_lines).strip()
            if label:
                cues.append((int(round(start)), int(round(end)), label))
        else:
            i += 1
    return cues


def parse_slc_benchmarks():
    """Extract exact jumpTopicTo timestamps from slc-the-exam.html for Task 1 & Task 2."""
    p = os.path.join(ROOT_DIR, "slc-the-exam.html")
    txt = open(p, encoding="utf-8").read()

    def extract_block(div_id: str, total_dur: int):
        m = re.search(rf'id="{div_id}"(.*?)</div>', txt, re.S)
        if not m:
            return []
        btns = re.findall(r'jumpTopicTo\((\d+)\)[^>]*>([^<]+)<', m.group(1))
        out = []
        for idx, (sec_s, raw_lbl) in enumerate(btns):
            sec = int(sec_s)
            lbl = re.sub(r"^\d+:\d+\s+", "", raw_lbl).strip()
            nxt = int(btns[idx + 1][0]) if idx + 1 < len(btns) else total_dur
            out.append((sec, max(nxt, sec + 1), lbl))
        return out

    return {
        "slc-task1-presentation-model": extract_block("topicTask1Jumps", 208),
        "slc-task2-discussion-model": extract_block("topicTask2Jumps", 205),
    }


def parse_walkthroughs():
    """Extract all 161 entries from MFS_WALKTHROUGHS in video-solution.html."""
    p = os.path.join(ROOT_DIR, "video-solution.html")
    txt = open(p, encoding="utf-8").read()
    m = re.search(
        r"const MFS_WALKTHROUGHS = \[(.*?)\];\s*\n\s*const TOPIC_FALLBACKS",
        txt,
        re.S,
    )
    if not m:
        raise RuntimeError("Could not locate MFS_WALKTHROUGHS in video-solution.html")
    block = m.group(1)
    entries = re.split(r"\n\s*\{\s*\n\s*(?=id:)", block)

    def get_f(e: str, name: str) -> str:
        fm = re.search(rf"{name}:\s*(['\"])((?:\\.|(?!\1).)*)\1", e)
        if not fm:
            return ""
        val = fm.group(2)
        val = re.sub(r"\\u([0-9a-fA-F]{4})", lambda x: chr(int(x.group(1), 16)), val)
        return val.replace("\\'", "'").replace('\\"', '"')

    items = []
    for e in entries:
        if "id:" not in e:
            continue
        items.append(
            {
                "id": get_f(e, "id"),
                "category": get_f(e, "category"),
                "series": get_f(e, "series"),
                "title": get_f(e, "title"),
                "fullTitle": get_f(e, "fullTitle"),
                "badge": get_f(e, "badge"),
                "section": get_f(e, "section"),
                "duration": get_f(e, "duration"),
                "vtt": get_f(e, "vtt"),
                "ytId": get_f(e, "ytId"),
                "worksheet": get_f(e, "worksheet"),
                "answers": get_f(e, "answers"),
                "markScheme": get_f(e, "markScheme"),
            }
        )
    return items


def is_intro_or_outro(label: str) -> bool:
    """Identify non-question intro/strategy/summary cues so auto-pause ignores them."""
    low = label.lower()
    if any(
        w in low
        for w in (
            "intro",
            "welcome",
            "briefing",
            "exam rules",
            "assessment overview",
            "assessment strategy",
            "exam structure",
            "mock structure",
            "exam strategy",
            "writing strategy",
            "strategy",
            "summary",
            "paper completed",
            "assessment completed",
            "writing recap",
            "next steps",
            "checklist",
        )
    ):
        # Note: 'SPaG & Length Check' in Writing mock IS a substantive check chapter
        if "spag" in low:
            return False
        return True
    return False


def match_cue(chapters, hints, fallback_idx):
    """Find best matching chapter index/timestamp from VTT cues."""
    if not chapters:
        return None, None, None
    for hint in hints:
        h = hint.lower()
        for ch in chapters:
            if h in ch["label"].lower():
                return ch["idx"], ch["start"], ch["label"]
    idx = min(max(fallback_idx, 0), len(chapters) - 1)
    ch = chapters[idx]
    return ch["idx"], ch["start"], ch["label"]


def build_topic_checks(slug, chapters):
    """Build 3-question 60-Second Concept Check anchored to VTT chapters."""
    specs = TOPIC_CHECKS_BANK[slug]
    checks = []
    for i, sp in enumerate(specs, start=1):
        c_idx, cue_sec, cue_lbl = match_cue(
            chapters, sp["cue_hints"], sp["fallback_idx"]
        )
        checks.append(
            {
                "id": f"q{i}",
                "stage": sp["stage"],
                "archetype": sp["archetype"],
                "chapterIdx": c_idx,
                "cueSec": cue_sec,
                "cueLabel": cue_lbl,
                "question": sp["question"],
                "options": list(sp["options"]),
                "correct": sp["correct"],
                "why": sp["why"],
            }
        )
    return checks


def generate_chapter_ccq(slug: str, subject: str, series: str, ch_label: str, q_num: int):
    """Generate a tailored Examiner Trap CCQ for any mock/past-paper VTT chapter."""
    low = ch_label.lower()

    # 1) Exact question lookup for Edexcel L2 P10B / P8B / L1 P10A / L1 P10B
    if slug in EXACT_QUESTION_CCQS and ch_label in EXACT_QUESTION_CCQS[slug]:
        d = EXACT_QUESTION_CCQS[slug][ch_label]
        return dict(d)

    # 2) Digital Functional Skills Mocks
    if subject == "dfs":
        if "$b$2" in low or "formula" in low or "vat" in low or "stock" in low:
            return {
                "archetype": "Spreadsheet Formula Trap",
                "question": f"In '{ch_label}', when copying a formula down rows that reference one fixed VAT rate or threshold cell (e.g. B2), what prevents broken rows?",
                "options": [
                    "Lock the fixed cell with $ signs ($B$2) before dragging down so only row numbers advance",
                    "Retype the raw number instead of a formula so autofill doesn't shift",
                    "Start the formula without an equals (=) sign",
                ],
                "correct": 0,
                "why": "Every spreadsheet calculation needs = and absolute cell locking ($B$2) for fixed lookup rates or tax cells.",
            }
        if "chart" in low or "sort" in low or "filter" in low or "currency" in low:
            return {
                "archetype": "Chart & Data Trap",
                "question": f"In '{ch_label}', what two mistakes commonly drop marks on spreadsheet sorting, currency formatting, and charts?",
                "options": [
                    "Sorting ONLY one column without expanding the full table, OR including the Total row inside the chart",
                    "Using Currency (£) with 2 decimal places",
                    "Adding clear axis labels and a chart title",
                ],
                "correct": 0,
                "why": "Always select the entire table range before sorting, exclude Totals from charts, and add clear chart titles and axis labels.",
            }
        if "email" in low or "signature" in low or "contacts" in low or "cloud" in low or "share" in low:
            return {
                "archetype": "Privacy & Email Trap",
                "question": f"In '{ch_label}', when emailing multiple external contacts or sharing a cloud folder, what protects personal data and earns full marks?",
                "options": [
                    "Use BCC when hiding external emails, set View-Only cloud access when editing isn't wanted, and include a clear Subject + Attachment",
                    "Put every recipient in To so everyone sees all addresses",
                    "Leave Subject blank and skip proofreading",
                ],
                "correct": 0,
                "why": "UK GDPR / DFS tasks penalise exposed email lists (use BCC), wrong cloud permissions, missing attachments, or blank Subject lines.",
            }
        if "document" in low or "flyer" in low or "slide" in low or "rename" in low or "image" in low:
            return {
                "archetype": "Layout & Save Trap",
                "question": f"In '{ch_label}', after formatting the document, flyer, or slide, what final check protects your task marks?",
                "options": [
                    "Confirm clean 1-page/slide hierarchy with readable contrast, Alt Text/captions if asked, and save with the EXACT requested filename & folder",
                    "Leave the starter filename unchanged",
                    "Let two lines spill onto an extra blank page",
                ],
                "correct": 0,
                "why": "Assessors check both visual layout fitness (no overflows, clean wrapping) and exact filename/folder compliance.",
            }
        if "form" in low or "utility" in low:
            return {
                "archetype": "Online Form Trap",
                "question": f"In '{ch_label}', before submitting an online form, what detail often costs easy marks?",
                "options": [
                    "Check date format (DD/MM/YYYY), required fields (*), postcode capitalisation, and take confirmation screenshot evidence if asked",
                    "Skip optional-looking boxes without reading instructions",
                    "Submit before checking spelling",
                ],
                "correct": 0,
                "why": "Onscreen forms require exact format compliance and evidence capture when prompted by the brief.",
            }
        if "folder" in low or "search" in low or "help" in low or "copyright" in low or "sources" in low:
            return {
                "archetype": "Copyright & File Trap",
                "question": f"In '{ch_label}', when sourcing online text/images or organising files, what rule must you follow?",
                "options": [
                    "Credit sources / check copyright licences, use clear descriptive filenames inside tidy folders, and verify file extensions (.pdf/.docx)",
                    "Use any copyrighted image with no attribution",
                    "Save everything unsorted into Downloads",
                ],
                "correct": 0,
                "why": "DFS exams test reliable source evaluation, copyright awareness, and structured folder/filename hygiene.",
            }
        return {
            "archetype": "Digital Knowledge Trap",
            "question": f"In '{ch_label}', when answering Part A onscreen knowledge questions, what strategy avoids careless drops?",
            "options": [
                "Read EVERY option carefully for absolutes ('always'/'never') and match security/GDPR rules (MFA, HTTPS, strong passphrases) directly to the scenario",
                "Pick the first option immediately",
                "Skip checking whether multiple checkboxes are required",
            ],
            "correct": 0,
            "why": "Part A questions often distinguish MFA, phishing cues, and UK GDPR obligations via subtle wording — check single vs multi-select too.",
        }

    # 3) English Reading & Writing Mocks
    if subject == "english":
        is_writing = "writing" in slug or any(
            w in low for w in ("task 1", "task 2", "activity 1", "activity 2", "question 1", "question 2", "spag")
        )
        if "comparison" in low or "both" in low or "section d" in low or "q14" in low or "q15" in low or "q19" in low or "q10" in low and "comparison" in low:
            return {
                "archetype": "Cross-Text Comparison Trap",
                "question": f"In '{ch_label}', what guarantees comparison marks instead of writing two disconnected summaries?",
                "options": [
                    "Link evidence from BOTH texts directly in the same point using comparative connectives ('whereas', 'similarly', 'in contrast')",
                    "Write everything about Text 1 only and leave Text 2 blank",
                    "State 'they are different' without naming ideas or quotes",
                ],
                "correct": 0,
                "why": "Examiners cannot award comparison marks unless both named sources are actively contrasted or linked with concrete details.",
            }
        if is_writing:
            if "spag" in low:
                return {
                    "archetype": "SPaG Proofreading Trap",
                    "question": f"In '{ch_label}', which 3-minute proofreading catch saves the highest-value Writing marks?",
                    "options": [
                        "Eliminating comma splices, checking homophones (their/there/they're, affect/effect), and confirming consistent verb tense",
                        "Adding extra exclamation marks",
                        "Counting only total word count",
                    ],
                    "correct": 0,
                    "why": "Roughly 40%+ of Writing marks assess SPaG — fixing run-on commas, homophones, and tense slips protects your pass grade.",
                }
            if any(w in low for w in ("letter", "complaint")):
                return {
                    "archetype": "Format & Sign-Off Trap",
                    "question": f"In '{ch_label}', what layout and sign-off pairing protects full Format marks for a formal letter?",
                    "options": [
                        "Addresses + Date + 'Dear Sir/Madam' → 'Yours faithfully' (or 'Dear Mr/Ms X' → 'Yours sincerely')",
                        "Email Subject header + 'Cheers'",
                        "Starting straight with Paragraph 1 and no addresses",
                    ],
                    "correct": 0,
                    "why": "Formal letters must include address layout, date, matched salutation/sign-off, and clear paragraphing addressing every prompt bullet.",
                }
            if any(w in low for w in ("email", "nomination")):
                return {
                    "archetype": "Format & Register Trap",
                    "question": f"In '{ch_label}', what three checks keep an Email task on-band?",
                    "options": [
                        "Clear specific Subject line, appropriate salutation/sign-off ('Kind regards'), and a dedicated paragraph per prompt bullet",
                        "Blank Subject line and text-speak",
                        "Writing sender street addresses like a posted letter",
                    ],
                    "correct": 0,
                    "why": "Emails require a focused Subject line, polite workplace register, and complete bullet coverage.",
                }
            if any(w in low for w in ("article", "blog", "feature", "review", "leaflet", "story")):
                return {
                    "archetype": "Format & Audience Trap",
                    "question": f"In '{ch_label}', what structural features signal an authentic Article / Leaflet / Review rather than a letter?",
                    "options": [
                        "Engaging Headline/Title, thematic subheadings, lively audience-matched paragraphs, and a strong closing takeaway (NO 'Yours sincerely'!)",
                        "'Dear Reader' and 'Yours faithfully'",
                        "One single 30-line block of text",
                    ],
                    "correct": 0,
                    "why": "Media/informational formats rely on headlines, subheadings, persuasive/engaging tone, and must never end with letter sign-offs.",
                }
            if any(w in low for w in ("report", "consultation", "proposal")):
                return {
                    "archetype": "Report Structure Trap",
                    "question": f"In '{ch_label}', what distinguishes a Formal Report or Proposal from an Email?",
                    "options": [
                        "Main Title, objective subheadings (Introduction, Findings, Recommendations), formal evidence, and zero email/letter greetings",
                        "Chatty anecdotes and emojis",
                        "To:/From:/CC: fields + 'Kind regards'",
                    ],
                    "correct": 0,
                    "why": "Reports need clear title + formal subheadings + structured recommendations in an objective register.",
                }
            if any(w in low for w in ("speech", "form")):
                return {
                    "archetype": "PAF & Audience Trap",
                    "question": f"In '{ch_label}', before drafting, what must you check from the prompt?",
                    "options": [
                        "Purpose, Audience & Format (direct spoken address for a speech, or exact instruction/format rules on a form) plus every bullet point",
                        "Ignore the audience and write informally",
                        "Skip checking required details",
                    ],
                    "correct": 0,
                    "why": "Matching PAF cues and ticking off every prompt bullet keeps both content and organisation marks safe.",
                }
        # Reading text chapters
        if "bias" in low or "opinion" in low:
            return {
                "archetype": "Fact vs Opinion / Bias Trap",
                "question": f"In '{ch_label}', when a sentence mixes a date/statistic with a praise word ('opened in 2022 as the best venue'), how do you answer accurately?",
                "options": [
                    "Separate the verifiable Fact ('opened in 2022') from the subjective Opinion/Bias ('best venue') — quote ONLY the asked part",
                    "Treat any sentence containing a number as 100% factual",
                    "Summarise the whole paragraph instead",
                ],
                "correct": 0,
                "why": "Examiners penalise lifting a mixed quote when asked strictly for a fact or an opinion.",
            }
        return {
            "archetype": "Source Evidence Trap",
            "question": f"In '{ch_label}', what two mistakes commonly cost marks on Reading comprehension questions?",
            "options": [
                "Pulling facts from the WRONG source document or outside knowledge, and copying quotes when 'your own words' are asked",
                "Checking which Document/Text the question names first",
                "Naming a feature + short quote + context effect",
            ],
            "correct": 0,
            "why": "Confirm the exact Document/Text letter first, check whether quotes or own words are requested, and always tie features to context.",
        }

    # 4) Maths Mock Walkthroughs (AQA, NCFE, C&G, Open Awards, TQUK, NOCN)
    # Match specific chapter keywords to the 4 Core CCQ Archetypes cleanly!
    if any(k in low for k in ("volume", "tin", "bath", "pool", "capacity", "milk", "units", "scale", "speed", "seconds", "conversion", "density", "soap", "sa", "prism")):
        return {
            "archetype": "Unit & Capacity Trap",
            "question": f"In '{ch_label}', what classic Maths trap catches candidates out on area, volume, speed, or scale calculations?",
            "options": [
                "Mixing incompatible units (cm vs m, mins vs decimal hours, cm³ vs litres) or forgetting to halve diameter into radius before πr²",
                "Writing the correct unit on the answer line",
                "Showing clear intermediate steps",
            ],
            "correct": 0,
            "why": "Always unify dimensions BEFORE multiplying (1,000 cm³ = 1 litre; 1 m³ = 1,000 litres; r = d ÷ 2; mins ÷ 60 = hours).",
        }
    if any(k in low for k in ("fence", "floor", "cake", "tiler", "pack", "fudge", "scaling", "playground", "heating", "extension", "estimate")):
        return {
            "archetype": "Rounding Direction Trap",
            "question": f"In '{ch_label}', when a calculation produces a decimal number of packs, tins, fence panels, or recipe ingredients, how must you round?",
            "options": [
                "Round UP for required materials/capacity (so nothing falls short) and DOWN only for max whole items under a cash/stock limit",
                "Always round to the nearest whole number even if 14.1 packs leaves an uncovered gap",
                "Ignore decimals after the point",
            ],
            "correct": 0,
            "why": "Real-world context dictates rounding direction: materials & transport round UP; fixed-budget counts round DOWN.",
        }
    if any(k in low for k in ("reverse", "check", "median", "mean", "tax", "ratio", "balance", "rates", "bidmas", "fraction")):
        if q_num % 2 == 1:
            return {
                "archetype": "Reverse Check Trap",
                "question": f"In '{ch_label}', how can you quickly verify a ratio split, reverse percentage, or estimated mean before moving on?",
                "options": [
                    "Run the inverse step: add ratio parts back to total, multiply original × % multiplier back to new price, or check Mean × Total Frequency = ∑(f × mid)",
                    "Repeat the exact same button presses in the same order",
                    "Round every input to 100 first",
                ],
                "correct": 0,
                "why": "An inverse calculation tests your logic in reverse and catches missed parts or calculator typos immediately.",
            }
        return {
            "archetype": "Yes/No Verdict Trap",
            "question": f"In '{ch_label}', when comparing two options, totals, or a customer's claim, what secures the final communication mark?",
            "options": [
                "An explicit Yes/No verdict sentence PLUS both calculated figures with exact units (£ to 2 d.p., %, mins, etc.)",
                "Writing a single bare number without stating Yes or No",
                "Writing 'Yes' without showing both values",
            ],
            "correct": 0,
            "why": "Examiners withhold the final mark unless your Yes/No verdict is backed by an explicit numerical comparison.",
        }
    if any(k in low for k in ("section a", "part a", "section 1", "q1-", "q4-")):
        return {
            "archetype": "Yes/No Verdict Trap",
            "question": f"In '{ch_label}', across short Section A / Part A questions, what loses the easiest marks?",
            "options": [
                "Skipping units (£, cm², %), writing £8.4 instead of £8.40, or dropping the Yes/No decision on short comparison items",
                "Writing step-by-step non-calculator working",
                "Checking BIDMAS operation order",
            ],
            "correct": 0,
            "why": "Short-answer questions punish missing units, 1-decimal-place money (£8.4), and bare numbers without Yes/No verdicts.",
        }

    # Balanced fallback rotation across the 4 Core Maths CCQ Archetypes
    cycle = [
        (
            "Unit & Capacity Trap",
            f"In '{ch_label}', before writing your final answer on the line, what unit check saves easy marks?",
            [
                "Verify every input shared the same unit (cm/m, g/kg, £/p, mins/hours) and include the exact asked unit (e.g. m², litres, £ to 2 d.p.)",
                "Leave the unit off if the question text mentioned it",
                "Combine cm and m directly in one multiplication",
            ],
            "Unit conversion mismatches and dropped money/area/capacity units are the #1 preventable Maths deduction.",
        ),
        (
            "Yes/No Verdict Trap",
            f"In '{ch_label}', when a multi-mark question asks 'Does she have enough?' or 'Is the manager right?', what MUST your final line state?",
            [
                "Both an explicit Yes/No statement AND the two calculated figures being compared with units",
                "Only the final difference in pounds",
                "Only 'Yes' or 'No' with no figures",
            ],
            "Interpretation marks require an explicit Yes/No decision linked to your calculated comparison.",
        ),
        (
            "Rounding Direction Trap",
            f"In '{ch_label}', if a real-life resource division gives a decimal (like 9.2 tins or 9.2 boxes), what decides whether to round UP or DOWN?",
            [
                "Round UP when covering an area/seating people (10 needed); round DOWN when capped by a strict cash budget or ribbon length (9 max)",
                "Always round .2 down to 9",
                "Always round .2 up regardless of context",
            ],
            "Always match rounding direction to physical reality — never leave people stranded or walls unpainted!",
        ),
        (
            "Reverse Check Trap",
            f"In '{ch_label}', how do you perform a genuine Reverse Calculation Check when asked?",
            [
                "Use the opposite operation starting from your answer (÷ to verify ×, + to verify −, or multiply mean × total frequency)",
                "Write 'Checked on calculator' without numbers",
                "Re-type the identical forward sum",
            ],
            "Check marks strictly require showing an inverse or alternative numerical verification step.",
        ),
    ]
    arch, q_txt, opts, why = cycle[(q_num - 1) % 4]
    return {
        "archetype": arch,
        "question": q_txt,
        "options": opts,
        "correct": 0,
        "why": why,
    }


def main():
    walkthroughs = parse_walkthroughs()
    slc_benchmarks = parse_slc_benchmarks()

    videos = {}
    by_ytid = {}

    topic_count = 0
    mock_count = 0
    total_checks = 0

    for item in walkthroughs:
        slug = item["id"]
        cat = item["category"]
        yt_id = item["ytId"]
        subject = detect_subject(cat, item["series"], slug)
        tutor = normalize_tutor(item["badge"], item["section"], item["title"], slug)

        # Resolve VTT cues (or SLC jump cues) read-only
        raw_cues = []
        if slug in slc_benchmarks:
            raw_cues = slc_benchmarks[slug]
        elif item["vtt"]:
            raw_cues = parse_vtt_file(item["vtt"])

        chapters = []
        for idx, (st, en, lbl) in enumerate(raw_cues):
            is_q = (cat == "past-papers") and not is_intro_or_outro(lbl)
            chapters.append(
                {
                    "idx": idx,
                    "start": st,
                    "end": en,
                    "label": lbl,
                    "isQuestion": is_q,
                }
            )

        if cat in ("topics", "e3-foundation", "slc"):
            mode = "topic"
            topic_count += 1
            if slug not in TOPIC_CHECKS_BANK:
                raise KeyError(f"Missing bespoke topic checks for: {slug}")
            checks = build_topic_checks(slug, chapters)
        elif cat == "past-papers":
            mode = "mock"
            mock_count += 1
            checks = []
            if chapters:
                q_chapters = [ch for ch in chapters if ch["isQuestion"]]
                for q_i, ch in enumerate(q_chapters, start=1):
                    ccq = generate_chapter_ccq(
                        slug, subject, item["series"], ch["label"], q_i
                    )
                    checks.append(
                        {
                            "id": f"c{ch['idx']}",
                            "stage": ch["label"],
                            "archetype": ccq["archetype"],
                            "chapterIdx": ch["idx"],
                            "cueSec": ch["start"],
                            "cueLabel": ch["label"],
                            "question": ccq["question"],
                            "options": ccq["options"],
                            "correct": ccq["correct"],
                            "why": ccq["why"],
                        }
                    )
            else:
                # Older Edexcel Maths L2 Past Papers (no VTT files yet)
                key = "sec_a" if "section-a" in slug else "sec_b"
                for q_i, ccq in enumerate(LEGACY_MATHS_MOCK_CCQS[key], start=1):
                    checks.append(
                        {
                            "id": f"m{q_i}",
                            "stage": f"Examiner Trap {q_i}",
                            "archetype": ccq["archetype"],
                            "chapterIdx": None,
                            "cueSec": None,
                            "cueLabel": None,
                            "question": ccq["question"],
                            "options": ccq["options"],
                            "correct": ccq["correct"],
                            "why": ccq["why"],
                        }
                    )
        else:
            raise ValueError(f"Unexpected category '{cat}' for {slug}")

        total_checks += len(checks)
        videos[slug] = {
            "id": slug,
            "ytId": yt_id,
            "mode": mode,
            "title": item["title"],
            "tutor": tutor,
            "subject": subject,
            "chapters": chapters,
            "checks": checks,
        }
        if yt_id:
            by_ytid[yt_id] = slug

    # Validation pass
    assert len(videos) == 126, f"Expected 126 videos, got {len(videos)}"

    # Check every ytId across all 245 topic pages + __mfsMasterclassParts resolves cleanly
    html_files = sorted(
        glob.glob(os.path.join(ROOT_DIR, "*.html"))
        + glob.glob(os.path.join(ROOT_DIR, "digital-skills", "*", "*.html"))
    )
    page_ytids = set()
    for hp in html_files:
        txt = open(hp, encoding="utf-8", errors="ignore").read()
        for m in re.finditer(r'id="topicMasterclassIframe"[^>]*data-ytid="([^"]+)"', txt):
            page_ytids.add(m.group(1))
        for m in re.finditer(r'"ytid":\s*"([^"]+)"', txt):
            page_ytids.add(m.group(1))

    missing_yt = [y for y in sorted(page_ytids) if y not in by_ytid]
    assert not missing_yt, f"Unresolved topic page ytIds: {missing_yt}"

    # Check every check record & confidentiality
    for slug, v in videos.items():
        assert len(v["checks"]) >= 1, f"No checks for {slug}"
        if v["mode"] == "topic":
            assert len(v["checks"]) == 3, f"Topic {slug} must have 3 checks"
        for ch in v["checks"]:
            assert 3 <= len(ch["options"]) <= 4, f"Bad option count on {slug}/{ch['id']}"
            assert len(set(ch["options"])) == len(ch["options"]), f"Duplicate options on {slug}/{ch['id']}"
            assert 0 <= ch["correct"] < len(ch["options"]), f"Bad correct index on {slug}/{ch['id']}"
            assert ch["why"].strip(), f"Empty why on {slug}/{ch['id']}"
            if ch["cueSec"] is not None:
                assert isinstance(ch["cueSec"], int) and ch["cueSec"] >= 0
            blob = " ".join([ch["question"], ch["why"], ch["archetype"], *ch["options"]]).lower()
            for fw in FORBIDDEN_WORDS:
                assert fw not in blob.split(), f"Forbidden token '{fw}' in {slug}/{ch['id']}"
                assert "oxford health" not in blob and "nhs" not in re.findall(r"[a-z]+", blob), (
                    f"Confidentiality check failed on {slug}/{ch['id']}"
                )

    out_dir = os.path.join(ROOT_DIR, "assets", "data")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "mfs-video-checks.json")
    payload = {"version": VERSION, "byYtId": by_ytid, "videos": videos}
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, separators=(",", ":"))

    kb = os.path.getsize(out_path) / 1024.0
    print(
        f"OK: {out_path} ({kb:.1f} KB) | videos={len(videos)} "
        f"(topic={topic_count}, mock={mock_count}) | total_checks={total_checks} | "
        f"topic_page_ytIds_verified={len(page_ytids)}"
    )


if __name__ == "__main__":
    main()
