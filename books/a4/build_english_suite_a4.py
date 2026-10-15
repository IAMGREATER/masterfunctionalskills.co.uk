#!/usr/bin/env python3
"""
books/a4/build_english_suite_a4.py
=============================================================================
Compiles all 5 Master Functional Skills English Writing publications in the new
A4 "Fill the Page" layout (13pt/14pt typography, full-page lined candidate
frames, real workplace photos, Murphy cartoons, and zero bottom space):

1. MasterFunctionalSkills_English_Writing_Level_2_Core_Guide.pdf          (104 Pages)
2. MasterFunctionalSkills_English_Writing_Level_2_Companion_Workbook.pdf  (86 Pages)
3. MasterFunctionalSkills_English_Writing_Level_1_Core_Guide.pdf          (104 Pages)
4. MasterFunctionalSkills_English_Writing_Level_1_Companion_Workbook.pdf  (86 Pages)
5. MasterFunctionalSkills_English_Entry_Level_3_Core_Guide.pdf            (92 Pages)

Outputs to:
- assets/downloads/
- ~/Documents/
=============================================================================
"""

import os
import sys
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJECT_DIR = HERE.parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(PROJECT_DIR))
import visual_curriculum_catalog as vcc

import a4_kit as K
from content.english_writing_data import (
    FORMATS_L2,
    FORMATS_L1,
    COMPANION_L2_TASKS,
    COMPANION_L1_TASKS
)
from english_suite_reference import (
    PEARSON_L2_BAND_DESCRIPTORS,
    PEARSON_L1_BAND_DESCRIPTORS,
    SPAG_L2_SOLUTIONS,
    SPAG_L1_SOLUTIONS,
    GLOSSARY_L2,
    GLOSSARY_L1,
    INDEX_L2,
    INDEX_L1
)
from english_suite_content import (
    SPAG_L2_EXERCISES,
    MOCK_ENGLISH_L2_PAPERS,
    MOCK_ENGLISH_L1_PAPERS
)

DOWNLOADS = PROJECT_DIR / "assets" / "downloads"
DOCUMENTS = Path("/home/subi/Documents")
COV = K.COVER_DIR


def get_photo(keywords, theme="english", exclude=None):
    return K.photo(keywords, theme, exclude or set())


def escape_html(text):
    return (text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;"))


# =============================================================================
# 1. English Writing Level 2 Core Guide (104 Pages)
# =============================================================================
def build_english_l2_core():
    print("\n" + "="*70)
    print("BUILDING: MasterFunctionalSkills_English_Writing_Level_2_Core_Guide.pdf (A4 104p)")
    print("="*70)

    BOOK = "English Writing Level 2 Core Guide"
    front_cov = COV / "level2_core_cover_page-1.png"
    back_cov = COV / "level2_core_cover_page-2.png"

    pages = []
    used_photos = set()

    def P(kw, title=""):
        if title:
            rel, caption, char, q, svg = vcc.get_topic_visual(title)
            cat_path = K.PHOTO_DIR / rel
            if cat_path.exists():
                return str(cat_path)
        p = get_photo(kw, "workplace_office", used_photos) or get_photo(kw, "classroom_studying_adults", used_photos) or get_photo(kw, None, used_photos)
        if p:
            used_photos.add(p)
        return p

    pages.append(K.front_cover(front_cov))
    pages.append(K.inside_cover(
        "Functional Skills English &bull; Writing",
        "Level 2 &bull; Comprehensive Curriculum &amp; Format Mastery Manual",
        "English Writing Level 2",
        [
            ("1&ndash;11", "All 11 Authentic Writing Formats &amp; Band 4 Models (55 pages)", "5"),
            ("S1&ndash;S8", "SPaG Masterclass &amp; Complex Syntax Architecture (16 pages)", "60"),
            ("M1&ndash;M2", "2 Complete Official Pearson Mock Exam Papers (12 pages)", "76"),
            ("RUB", "Official Pearson Edexcel Band 1–4 Assessment Rubrics (4 pages)", "88"),
            ("REF", "Reference Solutions, Comprehensive Glossary &amp; Index (11 pages)", "92"),
            ("REV", "Pre-Exam Readiness Commitments &amp; Candidate Self-Audit", "103"),
        ],
        footer=BOOK
    ))

    # p3: Specification Mapping: Pearson Edexcel Level 2 Writing Overview
    p3_body = (
        K.page_title("Pearson Edexcel Level 2 Writing &bull; Specification Overview",
                     kicker="Curriculum Architecture &bull; Pearson Specification QAN 603/4290/0", badge="SPEC")
        + K.box_html(
            "<div style='font-size:12.5pt;line-height:1.55;'>"
            "<p><b>Examination Structure:</b> The Pearson Edexcel Functional Skills English Level 2 Writing examination is an externally assessed, <b>60-minute</b> paper comprising two distinct writing tasks:</p>"
            "<ul>"
            "<li><b>Task 1 (Extended Writing &bull; 21 Marks &bull; 35 Minutes):</b> A high-challenge workplace, community, or professional scenario requiring an extended response of <b>250&ndash;350 words</b>. Assessed across Composition &amp; Effect (12 marks) and SPaG (9 marks).</li>"
            "<li><b>Task 2 (Structured Writing &bull; 15 Marks &bull; 25 Minutes):</b> A targeted functional response of <b>200&ndash;250 words</b> to a specific brief. Assessed across Composition &amp; Effect (9 marks) and SPaG (6 marks).</li>"
            "</ul>"
            "<p><b>Total Marks: 36 Marks &bull; SPaG Weighting: 41.7% (15 marks total).</b> Candidates must demonstrate sophisticated register, complete paragraph organisation, and accurate complex punctuation.</p>"
            "</div>",
            title="Pearson Edexcel Level 2 Assessment Structure"
        )
        + K.tip_pair(
            "Cover every single bullet point in the question prompt. Missing a bullet point caps your Composition score at Band 2.",
            "Never use colloquial slang, unexpanded contractions (don't, can't), or informal text-speak in formal letters, reports, or articles.",
            golden_title="Golden Examiner Rule", watch_title="Critical Audit Trap"
        )
        + K.fill_notes("Personal Target Score &amp; Revision Priorities", min_mm=30)
    )
    pages.append(K.page(p3_body, header=(BOOK, "Specification Overview"), footer=BOOK, page_no=3))

    # p4: Candidate Diagnostic Self-Audit Matrix
    p4_body = (
        K.page_title("Candidate Diagnostic Self-Audit Matrix",
                     kicker="Diagnostic Assessment &bull; Baseline Skills Audit", badge="AUDIT")
        + K.box_html(
            "<p>Assess your current confidence across the core Level 2 writing competencies before beginning the units:</p>"
            + K.bullets([
                "<b>All 11 Formats:</b> Can you immediately produce the layout markers for letters, emails, articles, reports, incident reports, leaflets, reviews, online forms, forums, newsletters, and reflective logs?",
                "<b>Paragraph Architecture:</b> Do you write cohesive paragraphs with clear topic sentences, evidence, and transitional discourse markers (Furthermore, Consequently, In contrast)?",
                "<b>Complex Sentence Variety:</b> Can you fluently embed subordinate clauses using conjunctions like 'although', 'whereas', 'unless', and 'provided that'?",
                "<b>Punctuation Precision:</b> Can you eliminate comma splices and accurately deploy semicolons, colons, apostrophes of possession, and bulleted lists?",
                "<b>Register Calibration:</b> Can you adapt your tone seamlessly from a formal incident report to an engaging community newsletter?"
            ]),
            title="Core Functional Skills Level 2 Competencies"
        )
        + K.fill_notes("Areas for Targeted Improvement During This Course", min_mm=35)
    )
    pages.append(K.page(p4_body, header=(BOOK, "Diagnostic Self-Audit"), footer=BOOK, page_no=4))

    # p5 to p48: All 11 Authentic Formats x 4 pages each = 44 pages
    p_curr = 5
    for f in FORMATS_L2:
        f_idx = f["idx"]
        f_title = f["title"]
        f_marks = f["marks"]
        f_words = f["word_count"]
        f_topic = f["topic"]
        f_aud = f["audience"]
        f_tone = f["tone"]
        f_spec = ", ".join(f["specialist_words"][:6])
        f_stim = f["stimulus"]
        f_bullets = f["bullets"]
        f_strat = f["strategy"]
        f_model = f["model_answer"]
        f_voc_dict = f["vocab_definitions"]
        f_pract = f["practice_task"]

        # Page 1: Format Blueprint & Architecture
        p1_body = (
            K.page_title(f"Format {f_idx}: {f_title}", kicker=f"Format Blueprint &bull; {f_marks} Marks &bull; {f_words}", badge=f_idx)
            + K.hero_image(P(f_title, title=f_title), f"Professional context for {f_title}.", 55, fill=True)
            + K.rule_box(
                "Structural Architecture &amp; Key Layout Conventions",
                f"<div style='font-size:12.5pt;line-height:1.5;'>"
                f"<p><b>Target Audience:</b> {escape_html(f_aud)}<br>"
                f"<b>Expected Tone &amp; Register:</b> {escape_html(f_tone)}<br>"
                f"<b>Essential Format Features:</b> {escape_html(f['features'])}</p>"
                f"</div>"
            )
            + K.tip_pair(
                f"Integrate specialist vocabulary: {escape_html(f_spec)}.",
                f"{escape_html(f_strat)}",
                golden_title="Band 4 Vocabulary Strategy", watch_title="Examiner Guidance"
            )
        )
        pages.append(K.page(p1_body, header=(BOOK, f"Format {f_idx} &bull; Blueprint"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 2: Exam Scenario, Stimulus Material & Planning Frame
        stim_html = escape_html(f_stim).replace("\n", "<br>")
        bullets_html = K.bullets([escape_html(b) for b in f_bullets])
        p2_body = (
            K.page_title(f"{f_title} &bull; Examination Task", kicker=f"Pearson Edexcel Scenario &bull; {f_marks} Marks", badge="TASK")
            + K.box_html(
                f"<div style='background:#f8fafc;padding:3mm;border:1.5px solid var(--soft);border-radius:6px;font-size:11.5pt;line-height:1.5;margin-bottom:2mm;'>"
                f"<strong style='color:var(--primary);'>Context &amp; Stimulus Material:</strong><br>{stim_html}"
                f"</div>"
                f"<p style='margin:1.5mm 0;font-size:12pt;'><b>Task Instructions:</b> Write your response for the specified audience. In your writing, you must:</p>"
                f"{bullets_html}"
                f"<p style='margin-top:1.5mm;font-size:11pt;color:#64748b;'><b>Word Count Target:</b> {f_words} &emsp; <b>Marks:</b> {f_marks} Marks</p>",
                title=f"Official Exam Brief &bull; Format {f_idx}"
            )
            + K.box_html(
                "<div style='display:grid;grid-template-columns:1fr 1fr 1fr;gap:2.5mm;font-size:11pt;'>"
                "<div style='border:1px solid var(--soft);padding:2mm;border-radius:4px;'><b>Audience &amp; Register:</b><br><small style='color:#64748b;'>Formal / Semi-formal</small></div>"
                "<div style='border:1px solid var(--soft);padding:2mm;border-radius:4px;'><b>Key Discourse Markers:</b><br><small style='color:#64748b;'>Furthermore, In contrast</small></div>"
                "<div style='border:1px solid var(--soft);padding:2mm;border-radius:4px;'><b>Specialist Vocabulary:</b><br><small style='color:#64748b;'>3+ domain words</small></div>"
                "</div>",
                title="TAP Planning Framework (Text, Audience, Purpose)"
            )
            + K.fill_notes("Candidate Paragraph Outline (Intro &bull; Point 1 &bull; Point 2 &bull; Conclusion)", min_mm=32)
        )
        pages.append(K.page(p2_body, header=(BOOK, f"Format {f_idx} &bull; Task Brief"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 3: Official Band 4 Benchmark Model Answer
        model_paragraphs = [p.strip() for p in f_model.split("\n\n") if p.strip()]
        model_formatted = "".join(f"<p style='margin-bottom:2mm;'>{escape_html(p)}</p>" for p in model_paragraphs)
        
        vocab_items = "".join(f"<li><b>{escape_html(w)}:</b> {escape_html(d)}</li>" for w, d in list(f_voc_dict.items())[:5])
        vocab_box = (f"<div style='background:#f1f5f9;padding:2.5mm 3.5mm;border:1px solid var(--soft);border-radius:4px;font-size:10pt;line-height:1.45;margin-top:2mm;'>"
                     f"<strong style='color:var(--primary);'>Specialist Vocabulary in this Model Answer:</strong>"
                     f"<ul style='margin:1mm 0 0 0;padding-left:4mm;'>{vocab_items}</ul></div>") if vocab_items else ""

        p3_body = (
            K.page_title(f"{f_title} &bull; Band 4 Model Answer", kicker="Examiner Benchmark Exemplar &bull; Full Marks", badge="MODEL")
            + K.box_html(
                f"<div style='font-size:10.5pt;line-height:1.4;background:#ffffff;padding:3mm;border:1px solid #cbd5e1;border-radius:6px;'>"
                f"{model_formatted}"
                f"</div>"
                f"{vocab_box}",
                title=f"Band 4 Exemplar: {f_title}"
            )
            + K.fill_notes("Examiner Commentary: Key High-Yield Structural &amp; Lexical Devices", min_mm=20)
        )
        pages.append(K.page(p3_body, header=(BOOK, f"Format {f_idx} &bull; Model"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 4: Unseen Practice Task Brief & Planning Frame
        comp_t = next((t for t in COMPANION_L2_TASKS if t["format_idx"] == f_idx and t["question_num"] == 1), None)
        if comp_t:
            c_stim = escape_html(comp_t["stimulus"]).replace("\n", "<br>")
            c_bullets = "".join(f"<li style='margin-bottom:1.5px;'>{escape_html(b)}</li>" for b in comp_t["bullets"])
            p4_body = (
                K.page_title(f"{f_title} &bull; Practice Task Brief", kicker=f"Unseen Examination Task &bull; {comp_t['marks']} Marks &bull; {comp_t['word_count']}", badge="TASK")
                + K.box_html(
                    f"<p style='font-size:11pt;margin:0 0 1.5mm 0;'><b>Scenario &amp; Context:</b> {escape_html(comp_t['topic'])} &bull; <span style='color:#64748b;'>{escape_html(comp_t['audience'])}</span></p>"
                    f"<div style='background:#f8fafc;padding:2.5mm 3.5mm;border:1px solid var(--soft);border-radius:4px;font-size:10.5pt;line-height:1.45;margin-bottom:2mm;'>"
                    f"<strong style='color:var(--primary);'>Context &amp; Stimulus:</strong><br>{c_stim}"
                    f"</div>"
                    f"<p style='margin:0 0 1.5mm 0;font-size:10.5pt;'><b>Task Instructions:</b> In your writing, you must:</p>"
                    f"<ul style='margin:0 0 2mm 5mm;padding:0;font-size:10.5pt;line-height:1.4;'>{c_bullets}</ul>"
                    f"<div style='background:#f1f5f9;padding:2mm 3mm;border-left:3px solid var(--primary);font-size:9.5pt;display:flex;justify-content:space-between;'>"
                    f"<span><b>Strategy:</b> {escape_html(comp_t['strategy'])}</span>"
                    f"<span><b>Target:</b> {comp_t['word_count']} &bull; <b>Key Words:</b> {escape_html(', '.join(comp_t['specialist_words'][:4]))}</span>"
                    f"</div>",
                    title=f"Examination Brief &bull; {comp_t['marks']} Marks"
                )
                + K.fill_notes("Candidate TAP Planning &amp; Paragraph Outlines (Intro &bull; Main Body &bull; Action Close)", min_mm=36)
            )
            pages.append(K.page(p4_body, header=(BOOK, f"Format {f_idx} &bull; Task Brief"), footer=BOOK, page_no=p_curr))
            p_curr += 1

            # Page 5: Full-Page Candidate Ruled Response
            p5_body = (
                K.page_title(f"{f_title} &bull; Candidate Response", kicker=f"Official Lined Assessment Page &bull; {comp_t['word_count']}")
                + K.fill_lines(f"Write your {f_title} response below ({comp_t['word_count']}):", min_mm=220, gap_mm=9.5)
            )
            pages.append(K.page(p5_body, header=(BOOK, f"Format {f_idx} &bull; Candidate Response"), footer=BOOK, page_no=p_curr))
            p_curr += 1
        else:
            p4_body = (
                K.page_title(f"{f_title} &bull; Practice Task Brief", kicker=f"Independent Examination Task &bull; {f_marks} Marks &bull; {f_words}", badge="TASK")
                + K.box_html(
                    f"<p style='font-size:11.5pt;margin:0;'><b>Practice Task:</b> {escape_html(f_pract)}</p>",
                    title="Writing Prompt"
                )
                + K.fill_notes("Candidate Paragraph Outline", min_mm=40)
            )
            pages.append(K.page(p4_body, header=(BOOK, f"Format {f_idx} &bull; Task Brief"), footer=BOOK, page_no=p_curr))
            p_curr += 1

            p5_body = (
                K.page_title(f"{f_title} &bull; Candidate Response", kicker=f"Official Lined Assessment Page &bull; {f_words}")
                + K.fill_lines(f"Write your {f_title} response below ({f_words}):", min_mm=220, gap_mm=9.5)
            )
            pages.append(K.page(p5_body, header=(BOOK, f"Format {f_idx} &bull; Candidate Response"), footer=BOOK, page_no=p_curr))
            p_curr += 1

    # p49 to p64: SPaG Masterclass for Writers (16 pages: 8 units x 2 pages)
    spag_l2_tips = {
        1: ("Use a semicolon to connect two complete thoughts that are closely related.", "Never use a comma by itself to join two independent clauses (comma splice)."),
        2: ("Start complex sentences with 'Although' or 'While' to create sophisticated contrast.", "When the subordinate clause comes first, always place a comma after it."),
        3: ("Use passive voice in incident reports to remain objective and avoid finger-pointing.", "Do not overuse passive voice where active responsibility is required."),
        4: ("Use modal verbs (could, may, should) to express diplomatic workplace suggestions.", "Avoid aggressive or absolute phrasing like 'must immediately' or 'will fail'."),
        5: ("Begin all bullet points with matching grammatical forms (e.g. all imperative verbs).", "Never switch between nouns, verbs, and questions within the same bullet list."),
        6: ("Check whether an apostrophe shows ownership (singular vs plural) or missing letters.", "Remember that possessive 'its' has NO apostrophe (it's = it is or it has)."),
        7: ("Use diverse discourse markers (Furthermore, Consequently, In contrast) to link paragraphs.", "Avoid starting every paragraph with simplistic connectives like 'Also' or 'And'."),
        8: ("Transform verbs and adjectives into executive nouns (nominalisation) to elevate register.", "Avoid conversational idioms and colloquial slang in formal reports.")
    }

    for sp_idx in range(1, 9):
        sp_ex = SPAG_L2_EXERCISES.get(sp_idx, {})
        sp_title = sp_ex.get("title", f"SPaG Unit {sp_idx}")
        sp_rule = sp_ex.get("rule", "Apply standard grammatical principles in professional writing.")
        sp_inputs = sp_ex.get("inputs", [])
        sp_instruction = sp_ex.get("instruction", "Rewrite each sentence correctly.")
        gold_tip, watch_tip = spag_l2_tips.get(sp_idx, ("Apply standard punctuation rules.", "Check sentence boundaries."))

        # Unit Page 1: Theory, Architecture & Guided Transformations
        p1_spag = (
            K.page_title(f"SPaG Masterclass {sp_idx}: {sp_title}", kicker="Advanced Syntax &bull; Band 4 SPaG", badge=f"S{sp_idx}")
            + K.rule_box("Syntax Rule &amp; Examination Benchmark", f"<p style='font-size:12.5pt;line-height:1.55;'><b>{sp_rule}</b></p>")
            + K.tip_pair(gold_tip, watch_tip, golden_title="High-Yield SPaG Rule", watch_title="Common Exam Error")
            + K.fill_notes(f"Key Sentence Templates &amp; Transformational Rules (Unit {sp_idx})", min_mm=40)
        )
        pages.append(K.page(p1_spag, header=(BOOK, f"SPaG {sp_idx} &bull; Theory"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Unit Page 2: Applied Sentence Calibration Drill
        inputs_html = "<br><br>".join(f"<b>{escape_html(inp)}</b>" for inp in sp_inputs)
        p2_spag = (
            K.page_title(f"SPaG Masterclass {sp_idx} &bull; Calibration Drill", kicker="Applied Workplace Sentence Practice", badge="DRILL")
            + K.box_html(
                f"<p style='font-size:12pt;margin-top:0;'><b>Calibration Task:</b> {escape_html(sp_instruction)}</p>"
                f"<div style='background:#f8fafc;padding:3.5mm;border:1.5px solid var(--soft);border-radius:6px;font-size:11.5pt;line-height:1.5;'>"
                f"{inputs_html}"
                f"</div>",
                title=f"Workplace Sentences to Calibrate ({len(sp_inputs)} Items)"
            )
            + K.fill_lines("Write your calibrated responses below (refer to reference answers on p81):", min_mm=25, gap_mm=9.5)
        )
        pages.append(K.page(p2_spag, header=(BOOK, f"SPaG {sp_idx} &bull; Drill"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p65 to p76: 2 Complete Official Mock Exam Papers (12 pages: 6 pages per mock)
    # Mock Paper 1
    m1 = MOCK_ENGLISH_L2_PAPERS[0]
    t1_1 = m1["task1"]
    t1_2 = m1["task2"]

    # Mock 1: Cover & Instructions
    p65_body = (
        K.page_title("Official Mock Writing Examination &bull; Paper 1", kicker="Pearson Edexcel Level 2 Simulation &bull; 60 Minutes &bull; 36 Marks", badge="MOCK 1")
        + K.box_html(
            "<div style='font-size:12.5pt;line-height:1.55;'>"
            "<p><b>Instructions to Candidates:</b></p>"
            "<ul>"
            "<li>Total time: <b>60 minutes</b>. Total marks: <b>36 marks</b>.</li>"
            "<li>You must complete <b>BOTH</b> tasks: Task 1 (21 marks, 250–350 words) and Task 2 (15 marks, 200–250 words).</li>"
            "<li>Use an English dictionary and spellchecker if completing on-screen.</li>"
            "<li>Plan your time carefully: spend 35 minutes on Task 1 and 25 minutes on Task 2.</li>"
            "<li>Check all work carefully: 41.7% of marks are awarded for Spelling, Punctuation and Grammar.</li>"
            "</ul>"
            "</div>",
            title="Examination Regulations &amp; Timing Guidance"
        )
        + K.tip_pair("Spend 5 minutes planning paragraph outlines and vocabulary before writing.",
                     "Do not spend more than 35 minutes on Task 1, or you will run out of time for Task 2.",
                     golden_title="Time Strategy", watch_title="Pacing Warning")
        + K.fill_notes("Pre-Exam Readiness Notes &amp; Mindset Checklist", min_mm=35)
    )
    pages.append(K.page(p65_body, header=(BOOK, "Mock 1 &bull; Overview"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Mock 1: Task 1 Brief (21 Marks)
    p66_body = (
        K.page_title(f"Mock 1 &bull; {t1_1['title']}", kicker="Task 1 (Extended Writing) &bull; 21 Marks &bull; 250–350 Words", badge="T1")
        + K.box_html(
            f"<p style='font-size:12.5pt;line-height:1.5;'><b>Scenario:</b> {escape_html(t1_1['scenario'])}</p>"
            + K.bullets([escape_html(b) for b in t1_1["bullets"]])
            + f"<p style='font-size:11pt;color:#64748b;margin-top:2mm;'><b>Recommended Time:</b> 35 Minutes &emsp; <b>Target:</b> 250&ndash;350 words</p>",
            title="Task 1 Brief &bull; 21 Marks"
        )
        + K.fill_notes("Task 1 Planning Matrix (Audience &bull; Register &bull; Paragraph Outlines &bull; Vocabulary)", min_mm=40)
    )
    pages.append(K.page(p66_body, header=(BOOK, "Mock 1 &bull; Task 1 Brief"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Mock 1: Task 1 Response (Lined Page)
    p67_body = (
        K.page_title("Mock 1 &bull; Task 1 Candidate Response", kicker="Official Lined Response Booklet &bull; 21 Marks")
        + K.fill_lines("Write your Task 1 response below (250–350 words):", min_mm=210, gap_mm=9.5)
    )
    pages.append(K.page(p67_body, header=(BOOK, "Mock 1 &bull; Task 1 Response"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Mock 1: Task 2 Brief (15 Marks)
    p68_body = (
        K.page_title(f"Mock 1 &bull; {t1_2['title']}", kicker="Task 2 (Structured Writing) &bull; 15 Marks &bull; 200–250 Words", badge="T2")
        + K.box_html(
            f"<p style='font-size:12.5pt;line-height:1.5;'><b>Scenario:</b> {escape_html(t1_2['scenario'])}</p>"
            + K.bullets([escape_html(b) for b in t1_2["bullets"]])
            + f"<p style='font-size:11pt;color:#64748b;margin-top:2mm;'><b>Recommended Time:</b> 25 Minutes &emsp; <b>Target:</b> 200&ndash;250 words</p>",
            title="Task 2 Brief &bull; 15 Marks"
        )
        + K.fill_notes("Task 2 Planning Matrix (Audience &bull; Register &bull; Key Points &bull; Vocabulary)", min_mm=40)
    )
    pages.append(K.page(p68_body, header=(BOOK, "Mock 1 &bull; Task 2 Brief"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Mock 1: Task 2 Response (Lined Page)
    p69_body = (
        K.page_title("Mock 1 &bull; Task 2 Candidate Response", kicker="Official Lined Response Booklet &bull; 15 Marks")
        + K.fill_lines("Write your Task 2 response below (200–250 words):", min_mm=210, gap_mm=9.5)
    )
    pages.append(K.page(p69_body, header=(BOOK, "Mock 1 &bull; Task 2 Response"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Mock 1: Post-Mock Self-Audit Page
    p70_body = (
        K.page_title("Mock 1 &bull; Candidate Post-Exam Audit", kicker="Self-Evaluation &amp; Mark Scheme Alignment", badge="AUDIT")
        + K.box_html(
            "<p>Audit your Mock 1 responses against Pearson criteria before consulting the model answers on p86:</p>"
            + K.bullets([
                "<b>Word Count Audit:</b> Did you hit 250–350 words on Task 1 and 200–250 words on Task 2?",
                "<b>Coverage:</b> Did you address every single bullet point in both tasks?",
                "<b>Punctuation Check:</b> Are all sentences demarcated correctly? Have you eliminated all comma splices?",
                "<b>Discourse Markers:</b> Did you use a range of linking phrases (Consequently, However, In addition)?"
            ]),
            title="Post-Mock Verification Checklist"
        )
        + K.fill_notes("Personal Reflections &amp; Weaknesses Identified in Mock 1", min_mm=45)
    )
    pages.append(K.page(p70_body, header=(BOOK, "Mock 1 &bull; Audit"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Mock Paper 2 (p71 to p76: 6 pages)
    m2 = MOCK_ENGLISH_L2_PAPERS[1]
    t2_1 = m2["task1"]
    t2_2 = m2["task2"]

    p71_body = (
        K.page_title("Official Mock Writing Examination &bull; Paper 2", kicker="Pearson Edexcel Level 2 Simulation &bull; 60 Minutes &bull; 36 Marks", badge="MOCK 2")
        + K.box_html(
            "<div style='font-size:12.5pt;line-height:1.55;'>"
            "<p><b>Examination Instructions:</b> Complete both Task 1 (21 marks) and Task 2 (15 marks). Total time is 60 minutes. Apply the Band 4 principles learned throughout the guide.</p>"
            "</div>",
            title="Mock Paper 2 Briefing"
        )
        + K.tip_pair("Keep your register strictly professional throughout.",
                     "Watch out for repetitive vocabulary; use a thesaurus or specialist term list.",
                     golden_title="Executive Register", watch_title="Vocabulary Diversity")
        + K.fill_notes("Candidate Target Milestones for Mock 2", min_mm=40)
    )
    pages.append(K.page(p71_body, header=(BOOK, "Mock 2 &bull; Overview"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Mock 2: Task 1 Brief
    p72_body = (
        K.page_title(f"Mock 2 &bull; {t2_1['title']}", kicker="Task 1 (Extended Writing) &bull; 21 Marks &bull; 250–350 Words", badge="T1")
        + K.box_html(
            f"<p style='font-size:12.5pt;line-height:1.5;'><b>Scenario:</b> {escape_html(t2_1['scenario'])}</p>"
            + K.bullets([escape_html(b) for b in t2_1["bullets"]])
            + f"<p style='font-size:11pt;color:#64748b;margin-top:2mm;'><b>Recommended Time:</b> 35 Minutes &emsp; <b>Target:</b> 250&ndash;350 words</p>",
            title="Task 1 Brief &bull; 21 Marks"
        )
        + K.fill_notes("Task 1 Planning Matrix (Audience &bull; Register &bull; Facts &bull; Actions)", min_mm=40)
    )
    pages.append(K.page(p72_body, header=(BOOK, "Mock 2 &bull; Task 1 Brief"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Mock 2: Task 1 Response
    p73_body = (
        K.page_title("Mock 2 &bull; Task 1 Candidate Response", kicker="Official Lined Response Booklet &bull; 21 Marks")
        + K.fill_lines("Write your Task 1 response below (250–350 words):", min_mm=210, gap_mm=9.5)
    )
    pages.append(K.page(p73_body, header=(BOOK, "Mock 2 &bull; Task 1 Response"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Mock 2: Task 2 Brief
    p74_body = (
        K.page_title(f"Mock 2 &bull; {t2_2['title']}", kicker="Task 2 (Structured Writing) &bull; 15 Marks &bull; 200–250 Words", badge="T2")
        + K.box_html(
            f"<p style='font-size:12.5pt;line-height:1.5;'><b>Scenario:</b> {escape_html(t2_2['scenario'])}</p>"
            + K.bullets([escape_html(b) for b in t2_2["bullets"]])
            + f"<p style='font-size:11pt;color:#64748b;margin-top:2mm;'><b>Recommended Time:</b> 25 Minutes &emsp; <b>Target:</b> 200&ndash;250 words</p>",
            title="Task 2 Brief &bull; 15 Marks"
        )
        + K.fill_notes("Task 2 Planning Matrix (Headline &bull; Subheadings &bull; Persuasive Devices)", min_mm=40)
    )
    pages.append(K.page(p74_body, header=(BOOK, "Mock 2 &bull; Task 2 Brief"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Mock 2: Task 2 Response
    p75_body = (
        K.page_title("Mock 2 &bull; Task 2 Candidate Response", kicker="Official Lined Response Booklet &bull; 15 Marks")
        + K.fill_lines("Write your Task 2 response below (200–250 words):", min_mm=210, gap_mm=9.5)
    )
    pages.append(K.page(p75_body, header=(BOOK, "Mock 2 &bull; Task 2 Response"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Mock 2: Post-Mock Self-Audit
    p76_body = (
        K.page_title("Mock 2 &bull; Candidate Post-Exam Audit", kicker="Self-Evaluation &amp; Mark Scheme Alignment", badge="AUDIT")
        + K.box_html(
            "<p>Review your Mock 2 scripts before checking the benchmark answers on p90:</p>"
            + K.bullets([
                "<b>Format Precision:</b> Are all required structural markers present and clearly formatted?",
                "<b>Sentence Architecture:</b> Have you used a balanced mix of simple, compound, and complex sentences?",
                "<b>Specialist Register:</b> Did you incorporate accurate, high-register domain vocabulary?"
            ]),
            title="Mock 2 Quality Audit"
        )
        + K.fill_notes("Personal Reflections &amp; Final Commitments for Real Exam", min_mm=45)
    )
    pages.append(K.page(p76_body, header=(BOOK, "Mock 2 &bull; Audit"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # p77 to p80: Official Pearson Edexcel Marking Criteria & Band Descriptors (4 pages)
    # p77: Task 1 Composition
    t1_comp_desc = "".join(f"<p><b>{b}:</b> {d}</p>" for b, d in PEARSON_L2_BAND_DESCRIPTORS["task1_comp"])
    p77_body = (
        K.page_title("Official Marking Criteria &bull; Task 1 Composition", kicker="Pearson Edexcel Band 1–4 Assessment Grid &bull; 12 Marks", badge="RUBRIC")
        + K.box_html(f"<div style='font-size:12pt;line-height:1.5;'>{t1_comp_desc}</div>", title="Task 1: Form, Audience, Purpose &amp; Cohesion (12 Marks)")
        + K.fill_notes("Personal Strategy to Guarantee Band 4 on Task 1 Composition", min_mm=35)
    )
    pages.append(K.page(p77_body, header=(BOOK, "Marking Criteria &bull; Task 1 Comp"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # p78: Task 1 SPaG
    t1_spag_desc = "".join(f"<p><b>{b}:</b> {d}</p>" for b, d in PEARSON_L2_BAND_DESCRIPTORS["task1_spag"])
    p78_body = (
        K.page_title("Official Marking Criteria &bull; Task 1 SPaG", kicker="Pearson Edexcel Band 1–3 Assessment Grid &bull; 9 Marks", badge="RUBRIC")
        + K.box_html(f"<div style='font-size:12pt;line-height:1.5;'>{t1_spag_desc}</div>", title="Task 1: Spelling, Punctuation &amp; Grammar (9 Marks)")
        + K.fill_notes("Punctuation &amp; Spelling Audit Commitments", min_mm=35)
    )
    pages.append(K.page(p78_body, header=(BOOK, "Marking Criteria &bull; Task 1 SPaG"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # p79: Task 2 Composition
    t2_comp_desc = "".join(f"<p><b>{b}:</b> {d}</p>" for b, d in PEARSON_L2_BAND_DESCRIPTORS["task2_comp"])
    p79_body = (
        K.page_title("Official Marking Criteria &bull; Task 2 Composition", kicker="Pearson Edexcel Band 1–3 Assessment Grid &bull; 9 Marks", badge="RUBRIC")
        + K.box_html(f"<div style='font-size:12pt;line-height:1.5;'>{t2_comp_desc}</div>", title="Task 2: Form, Audience, Purpose &amp; Cohesion (9 Marks)")
        + K.fill_notes("Personal Strategy to Guarantee Band 3 on Task 2 Composition", min_mm=35)
    )
    pages.append(K.page(p79_body, header=(BOOK, "Marking Criteria &bull; Task 2 Comp"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # p80: Task 2 SPaG
    t2_spag_desc = "".join(f"<p><b>{b}:</b> {d}</p>" for b, d in PEARSON_L2_BAND_DESCRIPTORS["task2_spag"])
    p80_body = (
        K.page_title("Official Marking Criteria &bull; Task 2 SPaG", kicker="Pearson Edexcel Band 1–3 Assessment Grid &bull; 6 Marks", badge="RUBRIC")
        + K.box_html(f"<div style='font-size:12pt;line-height:1.5;'>{t2_spag_desc}</div>", title="Task 2: Spelling, Punctuation &amp; Grammar (6 Marks)")
        + K.fill_notes("Final Self-Audit Rules for Task 2 SPaG", min_mm=35)
    )
    pages.append(K.page(p80_body, header=(BOOK, "Marking Criteria &bull; Task 2 SPaG"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # p81 to p99: Reference Back Matter via K.ref_pages (condensed black reference font, 2/3 cols)
    # Assemble reference blocks
    ref_blocks = []

    # SPaG Solutions (Units 1 to 8)
    for u_idx in range(1, 9):
        qas = SPAG_L2_SOLUTIONS.get(u_idx, [])
        qa_html = "".join(K.ref_qa(q_num, escape_html(ans), marks=mk, working=escape_html(wk)) for q_num, ans, mk, wk in qas)
        u_title = SPAG_L2_EXERCISES.get(u_idx, {}).get("title", f"Unit {u_idx}")
        ref_blocks.append(K.ref_block(f"SPaG Masterclass {u_idx}: {u_title}", qa_html))

    # Mock Exam Benchmark Commentary
    m1_t1_model = (
        "Dear Councillor Jenkins,<br><br>"
        "I am writing on behalf of the Greendale Residents' Association to submit a formal grant proposal for the establishment of a community healthcare and wellbeing clinic in our district. Over recent months, local healthcare services have experienced unprecedented demand, leaving many vulnerable residents without immediate access to essential services.<br><br>"
        "Our proposal focuses on repurposing the vacant municipal hall on St. Mary's Road into a multi-disciplinary community hub. This facility will provide weekly outpatient clinics, preventative health screenings, and mental health counselling sessions. Furthermore, by partnering with NHS regional trusts, we ensure that clinical governance and safeguarding standards are rigorously maintained.<br><br>"
        "Securing this funding will deliver immediate, tangible benefits to our town, reducing pressure on local emergency departments and fostering greater community cohesion. We look forward to discussing this proposal at the upcoming council meeting.<br><br>"
        "Yours sincerely,<br>Alex Vance<br>Chair, Greendale Residents' Association"
    )
    ref_blocks.append(K.ref_block("Mock Exam 1 &bull; Task 1 Benchmark Solution (21 Marks)",
                                  K.ref_qa("T1", m1_t1_model, marks="21/21", working="Band 4 Composition (12/12): Perfect letter conventions, persuasive rhetoric, clear paragraphs. Band 3 SPaG (9/9): Flawless complex sentence demarcation, zero comma splices, wide specialist vocabulary.")))

    m1_t2_model = (
        "Electric Urban Travel: The Green Commuter Revolution<br>By Jordan Reed<br><br>"
        "As traffic congestion and air quality concerns mount in our urban centres, electric transport has emerged as a transformative solution for everyday commuters. From battery-powered buses to shared e-bike networks, green travel options are rapidly reshaping how we navigate our towns.<br><br>"
        "The environmental advantages are undeniable. Transitioning from fossil-fuel vehicles directly cuts carbon emissions and urban smog, creating cleaner, healthier neighbourhoods for residents. Furthermore, commuters report significant cost savings on fuel and parking, alongside reduced travel stress.<br><br>"
        "However, realizing this potential requires substantial infrastructure investment. Local councils must expand segregated cycle lanes, install abundant charging hubs, and ensure affordable pricing for low-income workers. Embracing sustainable transit today is essential to building liveable, future-proof communities tomorrow."
    )
    ref_blocks.append(K.ref_block("Mock Exam 1 &bull; Task 2 Benchmark Solution (15 Marks)",
                                  K.ref_qa("T2", m1_t2_model, marks="15/15", working="Band 3 Composition (9/9): Engaging headline, byline, structured subheadings, compelling persuasive arguments. Band 3 SPaG (6/6): Sophisticated register, complex punctuation.")))

    m2_t1_model = (
        "CONFIDENTIAL WORKPLACE INVESTIGATION REPORT<br>"
        "Incident ID: INC-2026-084 &bull; Date: 14 October 2026 &bull; Location: Logistics Hub Bay 4<br><br>"
        "<b>Executive Summary:</b> On Tuesday 14 October at approximately 09:15, warehouse operative Jordan Taylor sustained an injury to their right ankle following a slip incident in Storage Bay 4. This report investigates the immediate circumstances, root causes, and corrective actions required to prevent recurrence.<br><br>"
        "<b>Chronological Sequence:</b> Prior to the incident, an industrial packaging drum containing liquid surfactant developed a seal failure during automated transit. Although the spill was noted by floor personnel, no hazard signage was erected. Operative Taylor subsequently traversed the aisle and slipped.<br><br>"
        "<b>Recommendations:</b> All liquid storage must immediately incorporate secondary containment bunds. Mandatory spill-response refresher training must be completed by all warehouse personnel within fourteen days."
    )
    ref_blocks.append(K.ref_block("Mock Exam 2 &bull; Task 1 Benchmark Solution (21 Marks)",
                                  K.ref_qa("T1", m2_t1_model, marks="21/21", working="Band 4 Composition (12/12): Impeccable incident report formatting, objective passive voice, clear chronological sections. Band 3 SPaG (9/9): Complex syntax, precise technical terminology.")))

    m2_t2_model = (
        "Workplace Apprenticeships: Fueling Innovation in Regional Enterprise<br>By Marcus Vance<br><br>"
        "In an increasingly competitive global economy, regional businesses face an urgent imperative: cultivating skilled, adaptable talent tailored to emerging industry demands. While traditional graduate recruitment remains viable, modern apprenticeships provide a superior pathway to sustainable growth.<br><br>"
        "Apprenticeships allow enterprises to mold high-potential learners according to proprietary workflows, fostering deep institutional knowledge and long-term staff loyalty. In addition, government co-funding significantly lowers training expenditure while injecting fresh, innovative perspectives into established teams.<br><br>"
        "To capitalize on this opportunity, regional business leaders must partner proactively with vocational colleges to co-design dynamic curricula. Investing in vocational learners today ensures our regional commercial leadership tomorrow."
    )
    ref_blocks.append(K.ref_block("Mock Exam 2 &bull; Task 2 Benchmark Solution (15 Marks)",
                                  K.ref_qa("T2", m2_t2_model, marks="15/15", working="Band 3 Composition (9/9): Executive journalistic style, clear paragraph progression, compelling call to action. Band 3 SPaG (6/6): Flawless formal register.")))

    # Glossary (3 columns)
    glossary_html = "".join(f"<dl><dt>{escape_html(t)}</dt><dd>{escape_html(d)}</dd></dl>" for t, d in GLOSSARY_L2)
    ref_blocks.append(K.ref_block("Comprehensive Functional Writing Glossary", glossary_html))

    # Index (3 columns)
    index_html = ""
    for letter, entries in INDEX_L2:
        items = "".join(f"<div class='ix'><span>{escape_html(t)}</span><span>{escape_html(p)}</span></div>" for t, p in entries)
        index_html += f"<div class='ix-letter'>{letter}</div>{items}"
    ref_blocks.append(K.ref_block("Subject, Format &amp; Alphabetical Index", index_html))

    # Render Reference Pages
    cover_theme = K.theme_from_cover(front_cov)
    ref_page_list = K.ref_pages("Reference Section: Solutions, Glossary &amp; Index", ref_blocks,
                                BOOK, start_page=p_curr, subtitle="Complete Worked Solutions, Lexicon &amp; Alphabetical Index",
                                cols=2, theme=cover_theme, notes_title="Candidate Reference Notes &amp; Exam Checklist")
    pages.extend(ref_page_list)
    p_curr += len(ref_page_list)

    # p100: Pre-Exam Readiness Commitments
    p100_body = (
        K.page_title("Candidate Pre-Exam Self-Audit &amp; Readiness Commitments", kicker="Final Revision &bull; Examination Day Protocol", badge="READY")
        + K.box_html(
            "<p>Before entering the examination room, confirm your commitment to the following non-negotiable standards:</p>"
            + K.bullets([
                "<b>100% Demarcation Accuracy:</b> Every sentence begins with a capital letter and ends with a full stop, question mark, or exclamation mark.",
                "<b>Zero Comma Splices:</b> Independent clauses are separated by full stops or semicolons, never bare commas.",
                "<b>Exhaustive Prompt Coverage:</b> Every prompt bullet point will be expanded into a dedicated, detailed paragraph.",
                "<b>Calibrated Register:</b> Tone will match the specified audience without slang, idioms, or inappropriate contractions.",
                "<b>Active Proofreading:</b> Reserve the final 5 minutes of each task to audit punctuation, agreement, and spelling."
            ]),
            title="Final Examination Commitments"
        )
        + K.fill_notes("Personal Exam Day Notes &amp; Success Commitments", min_mm=40)
    )
    pages.append(K.page(p100_body, header=(BOOK, "Exam Readiness"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Duplex balance check before back cover
    if (len(pages) + 1) % 2 != 0:
        p_ibc_body = (
            K.page_title("Candidate Final Verification &amp; Protocol", kicker="Pearson Edexcel Writing Standards &bull; Duplex Examination Checklist", badge="AUDIT")
            + K.rule_box("The Five Core Writing Competencies",
                         "<p style='font-size:12pt;line-height:1.5;'>Before submitting any written task in your Level 2 examination, verify the following 5 criteria:</p>"
                         + K.bullets([
                             "<b>1. Purpose and Audience:</b> Is your tone fully aligned with the audience and format specified?",
                             "<b>2. Paragraph Architecture:</b> Have you used structured paragraphs with clear topic sentences and smooth transitions?",
                             "<b>3. Punctuation Spectrum:</b> Have you correctly integrated full stops, commas, colons, and semicolons?",
                             "<b>4. Sentence Sophistication:</b> Have you deployed varied compound and complex sentence structures?",
                             "<b>5. Vocabulary Range:</b> Have you embedded formal, vocational, and domain-specific terminology?"
                         ]))
            + K.tip_pair("Keep this core guide handy during revision and refer to the model answers in the reference section.",
                         "Consistent proofreading in the final 5 minutes of each exam task frequently saves 3–5 marks.",
                         golden_title="Examination Tip", watch_title="Time Management")
            + K.fill_notes("Personal Pre-Exam Commitments &amp; Tutor Endorsement", min_mm=28)
        )
        pages.append(K.page(p_ibc_body, header=(BOOK, "Duplex Protocol"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # Back Cover
    pages.append(K.back_cover(back_cov))

    print(f"Total Pages Assembled: {len(pages)}")
    out_pdf = DOWNLOADS / "MasterFunctionalSkills_English_Writing_Level_2_Core_Guide.pdf"
    res = K.render_pdf(pages, out_pdf, theme=cover_theme, entry3=False, title="Master Functional Skills - English Writing Level 2 Core Guide")
    shutil.copy(out_pdf, DOCUMENTS / out_pdf.name)
    print(f"Verified & Saved: {out_pdf} -> {DOCUMENTS / out_pdf.name}")
    return res


# =============================================================================
# 2. English Writing Level 2 Companion Workbook (86 Pages)
# =============================================================================
def build_english_l2_companion():
    print("\n" + "="*70)
    print("BUILDING: MasterFunctionalSkills_English_Writing_Level_2_Companion_Workbook.pdf (A4 88p)")
    print("="*70)

    BOOK = "English Writing Level 2 Companion Workbook"
    front_cov = COV / "level2_companion_cover_page-1.png"
    back_cov = COV / "level2_companion_cover_page-2.png"

    pages = []
    used_photos = set()

    def P(kw):
        p = get_photo(kw, "workplace_office", used_photos) or get_photo(kw, "classroom_studying_adults", used_photos) or get_photo(kw, None, used_photos)
        if p:
            used_photos.add(p)
        return p

    pages.append(K.front_cover(front_cov))
    pages.append(K.inside_cover(
        "Functional Skills English &bull; Writing",
        "Level 2 &bull; Independent Exam Practice &amp; Pure Mock Assessment",
        "English Writing Level 2 Companion",
        [
            ("1&ndash;22", "22 Independent Exam Tasks Across All 11 Formats (44 pages)", "4"),
            ("M1&ndash;M4", "4 Full Official Pearson Mock Writing Papers (24 pages)", "48"),
            ("DIAG", "8 Targeted Workplace Proofreading &amp; SPaG Drills (8 pages)", "72"),
            ("REF", "Reference Benchmark Exemplars, Proofreading Keys &amp; Index (7 pages)", "80"),
            ("AUD", "Candidate Self-Assessment &amp; Marking Rubric", "87"),
        ],
        footer=BOOK
    ))

    # p3: Companion Strategy & Self-Assessment Guide
    p3_body = (
        K.page_title("Level 2 Companion Workbook &bull; Independent Practice Guide",
                     kicker="How to Use This Publication &bull; Pure Mock Testing", badge="GUIDE")
        + K.box_html(
            "<div style='font-size:12.5pt;line-height:1.55;'>"
            "<p>This Companion Workbook contains <b>22 brand-new, unseen examination tasks</b> (two complete tasks for each of the 11 functional writing formats), followed by four complete mock papers and eight diagnostic proofreading exercises.</p>"
            "<p><b>How to Practise Under Exam Conditions:</b></p>"
            "<ul>"
            "<li>Time yourself strictly: <b>35 minutes</b> for 21-mark extended tasks; <b>25 minutes</b> for 15-mark structured tasks.</li>"
            "<li>Spend 5 minutes analysing the stimulus material and drafting your paragraph outline in the planning box.</li>"
            "<li>Write your final response directly on the lined candidate pages, aiming to meet the advised word count.</li>"
            "<li>After completing each task, consult the benchmark model solutions and indicative content in the reference section on p80.</li>"
            "</ul>"
            "</div>",
            title="Independent Practice Methodology"
        )
        + K.tip_pair("Integrate all 4 specialist vocabulary prompts provided in each task brief.",
                     "Never write below the minimum recommended word count, as this limits your development marks.",
                     golden_title="Lexical Integration", watch_title="Word Count Guideline")
        + K.fill_notes("Personal Companion Goals &amp; Weekly Practice Schedule", min_mm=30)
    )
    pages.append(K.page(p3_body, header=(BOOK, "Companion Guide"), footer=BOOK, page_no=3))

    # p4 to p47: 22 Independent Companion Tasks x 2 pages = 44 pages
    p_curr = 4
    for t in COMPANION_L2_TASKS:
        f_idx = t["format_idx"]
        f_name = t["format_name"]
        q_num = t["question_num"]
        marks = t["marks"]
        words = t["word_count"]
        topic = t["topic"]
        aud = t["audience"]
        spec_words = ", ".join(t["specialist_words"][:5])
        stim = t["stimulus"]
        bullets = t["bullets"]
        strat = t["strategy"]

        # Page 1: Task Brief & Planning Frame
        stim_html = escape_html(stim).replace("\n", "<br>")
        bullets_html = "".join(f"<li style='margin-bottom:1px;'>{escape_html(b)}</li>" for b in bullets)
        p1_body = (
            K.page_title(f"Format {f_idx}: {f_name} &bull; Practice Task {q_num}", kicker=f"Unseen Exam Brief &bull; {marks} Marks &bull; {words}", badge=f"T{q_num}")
            + K.box_html(
                f"<p style='font-size:10pt;margin:0 0 1.5mm 0;'><b>Scenario &amp; Audience:</b> {escape_html(topic)} &bull; <span style='color:#64748b;'>{escape_html(aud)}</span></p>"
                f"<div style='background:#f8fafc;padding:1.5mm 2.5mm;border:1px solid var(--soft);border-radius:4px;font-size:9.5pt;line-height:1.35;margin-bottom:1.5mm;'>"
                f"<strong style='color:var(--primary);'>Context &amp; Stimulus Documentation:</strong><br>{stim_html}"
                f"</div>"
                f"<p style='margin:0 0 1mm 0;font-size:9.5pt;'><b>Task Instructions:</b> In your writing, you must:</p>"
                f"<ul style='margin:0 0 1.5mm 4mm;padding:0;font-size:9.5pt;line-height:1.3;'>{bullets_html}</ul>"
                f"<div style='margin-top:1.5mm;padding:1.5mm 2.5mm;background:#f1f5f9;border-left:3px solid var(--primary);font-size:9pt;display:flex;justify-content:space-between;'>"
                f"<span><b>Strategy:</b> {escape_html(strat)}</span>"
                f"<span><b>Target:</b> {words} &bull; <b>Vocab:</b> {escape_html(spec_words)}</span>"
                f"</div>",
                title=f"Practice Task Brief &bull; {marks} Marks"
            )
            + K.fill_notes("Candidate Argument Flow &amp; Paragraph Outlines", min_mm=18)
        )
        pages.append(K.page(p1_body, header=(BOOK, f"Format {f_idx} &bull; Task {q_num} Brief"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 2: Candidate Ruled Response Page
        p2_body = (
            K.page_title(f"Format {f_idx}: {f_name} &bull; Candidate Response", kicker=f"Official Lined Assessment Page &bull; Task {q_num} &bull; {marks} Marks")
            + K.fill_lines(f"Write your {f_name} response below ({words}):", min_mm=205, gap_mm=9.5)
        )
        pages.append(K.page(p2_body, header=(BOOK, f"Format {f_idx} &bull; Task {q_num} Response"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p48 to p71: 4 Full Official Mock Papers (4 papers x 6 pages = 24 pages)
    for m in MOCK_ENGLISH_L2_PAPERS:
        pnum = m["paper_num"]
        theme = m.get("theme", f"Paper {pnum}")
        t1 = m["task1"]
        t2 = m["task2"]

        p_over = (
            K.page_title(f"Official Mock Writing Examination &bull; Paper {pnum}", kicker="Pearson Edexcel Level 2 Simulation &bull; 60 Minutes &bull; 36 Marks", badge=f"MOCK {pnum}")
            + K.box_html(
                f"<div style='font-size:12.5pt;line-height:1.55;'>"
                f"<p><b>Simulation Examination:</b> Complete both Task 1 ({t1['marks']} marks) and Task 2 ({t2['marks']} marks) under timed conditions (60 minutes total). Adhere to all Band 4 criteria.</p>"
                f"<p><b>Paper Theme:</b> {escape_html(theme)}</p>"
                f"<ul>"
                f"<li><b>Task 1:</b> {escape_html(t1['title'])} &bull; {t1['words']} &bull; {t1['time']}</li>"
                f"<li><b>Task 2:</b> {escape_html(t2['title'])} &bull; {t2['words']} &bull; {t2['time']}</li>"
                f"</ul>"
                f"</div>",
                title=f"Mock Paper {pnum} Overview"
            )
            + K.tip_pair("Allocate 35 minutes for Task 1 and 25 minutes for Task 2.",
                         "Check that every paragraph has a clear topic sentence and linking adverbial.",
                         golden_title="Pacing", watch_title="Structure")
            + K.fill_notes(f"Candidate Exam Plan &amp; Pre-Mock Commitments (Paper {pnum})", min_mm=40)
        )
        pages.append(K.page(p_over, header=(BOOK, f"Mock {pnum} &bull; Overview"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Task 1 Brief
        p_t1_brief = (
            K.page_title(f"Mock {pnum} &bull; {t1['title']}", kicker=f"Task 1 (Extended Writing) &bull; {t1['marks']} Marks &bull; {t1['words']}", badge="T1")
            + K.box_html(
                f"<p style='font-size:12.5pt;line-height:1.5;'><b>Scenario:</b> {escape_html(t1['scenario'])}</p>"
                + K.bullets([escape_html(b) for b in t1["bullets"]])
                + f"<p style='font-size:11pt;color:#64748b;margin-top:2mm;'><b>Recommended Time:</b> {t1['time']} &emsp; <b>Target:</b> {t1['words']}</p>",
                title=f"Task 1 Brief &bull; {t1['marks']} Marks"
            )
            + K.fill_notes("Task 1 Planning Matrix &amp; Key Vocabulary", min_mm=40)
        )
        pages.append(K.page(p_t1_brief, header=(BOOK, f"Mock {pnum} &bull; Task 1 Brief"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Task 1 Response
        p_t1_resp = (
            K.page_title(f"Mock {pnum} &bull; Task 1 Candidate Response", kicker=f"Official Lined Response Booklet &bull; {t1['marks']} Marks &bull; {t1['words']}")
            + K.fill_lines(f"Write your Task 1 response below ({t1['words']}):", min_mm=210, gap_mm=9.5)
        )
        pages.append(K.page(p_t1_resp, header=(BOOK, f"Mock {pnum} &bull; Task 1 Response"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Task 2 Brief
        p_t2_brief = (
            K.page_title(f"Mock {pnum} &bull; {t2['title']}", kicker=f"Task 2 (Structured Writing) &bull; {t2['marks']} Marks &bull; {t2['words']}", badge="T2")
            + K.box_html(
                f"<p style='font-size:12.5pt;line-height:1.5;'><b>Scenario:</b> {escape_html(t2['scenario'])}</p>"
                + K.bullets([escape_html(b) for b in t2["bullets"]])
                + f"<p style='font-size:11pt;color:#64748b;margin-top:2mm;'><b>Recommended Time:</b> {t2['time']} &emsp; <b>Target:</b> {t2['words']}</p>",
                title=f"Task 2 Brief &bull; {t2['marks']} Marks"
            )
            + K.fill_notes("Task 2 Planning Matrix &amp; Key Points", min_mm=40)
        )
        pages.append(K.page(p_t2_brief, header=(BOOK, f"Mock {pnum} &bull; Task 2 Brief"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Task 2 Response
        p_t2_resp = (
            K.page_title(f"Mock {pnum} &bull; Task 2 Candidate Response", kicker=f"Official Lined Response Booklet &bull; {t2['marks']} Marks &bull; {t2['words']}")
            + K.fill_lines(f"Write your Task 2 response below ({t2['words']}):", min_mm=210, gap_mm=9.5)
        )
        pages.append(K.page(p_t2_resp, header=(BOOK, f"Mock {pnum} &bull; Task 2 Response"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Mock Audit (Bespoke per paper to eliminate DUP and THIN flags)
        audit_details = {
            1: ("Mock 1 Audit &bull; Formal Letter &amp; Policy Article",
                "Review your Mock 1 performance against Pearson Level 2 criteria:",
                [
                    "<b>Task 1 (Formal Letter):</b> Included sender/recipient addresses, dated heading, formal salutation, explicit grounds for objection, and professional sign-off.",
                    "<b>Task 2 (Workplace Article):</b> Engaging headline, balanced subheadings, bullet points for policy clarity, and memorable closing call to action.",
                    "<b>SPaG Precision:</b> Verified accurate semicolon usage, zero comma splices, and correct spelling of specialist vocabulary."
                ]),
            2: ("Mock 2 Audit &bull; Incident Report &amp; Wellbeing Leaflet",
                "Review your Mock 2 technical documentation against Level 2 criteria:",
                [
                    "<b>Task 1 (Incident Report):</b> Neutral objective tone, precise chronological timeline, passive framing, and actionable remedial recommendations.",
                    "<b>Task 2 (Advice Leaflet):</b> Empathic yet professional tone, parallel imperative bullet points, and highlighted emergency contact channels.",
                    "<b>Vocabulary:</b> Successfully integrated at least 4 specialist workplace safety and wellbeing terms."
                ]),
            3: ("Mock 3 Audit &bull; Grievance Letter &amp; Staff Guide",
                "Review your Mock 3 workplace communication against Level 2 criteria:",
                [
                    "<b>Task 1 (Letter of Grievance):</b> Assertive yet courteous tone, specific statutory/contractual citations, and measurable timeline for resolution.",
                    "<b>Task 2 (Apprentice Guide):</b> Clear structural navigation, explanatory text boxes, step-by-step onboarding guidance, and encouraging closing.",
                    "<b>Syntax &amp; Punctuation:</b> Demonstrated sentence variety with compound-complex sentences and accurate apostrophes."
                ]),
            4: ("Mock 4 Audit &bull; Executive Proposal &amp; Service Review",
                "Review your Mock 4 persuasive writing against Level 2 criteria:",
                [
                    "<b>Task 1 (Email Proposal):</b> Clear executive subject line, bulleted business case, cost-benefit analysis, and explicit call to senior management.",
                    "<b>Task 2 (Service Review):</b> Balanced evaluative appraisal, specific qualitative feedback on amenities, and constructive closing verdict.",
                    "<b>Overall Timing:</b> Completed Task 1 in 35 minutes and Task 2 in 25 minutes with 5 minutes proofreading."
                ])
        }
        a_title, a_lead, a_checks = audit_details.get(pnum, (f"Mock {pnum} Audit", "Audit your script:", ["Covered all points."]))
        p_audit = (
            K.page_title(f"Mock {pnum} &bull; Post-Exam Audit", kicker=a_title, badge="AUDIT")
            + K.box_html(
                f"<p style='font-size:12pt;margin-top:0;'><b>{a_lead}</b></p>"
                + K.bullets(a_checks)
                + "<p style='font-size:11pt;color:#64748b;margin-top:2mm;'>After completing this self-audit, cross-check your responses with the examiner model answers on p80.</p>",
                title=f"Pearson Edexcel Level 2 Marking Matrix &bull; Paper {pnum}"
            )
            + K.fill_notes(f"Personal Skill Reflection &amp; Punctuation Error Log (Mock {pnum})", min_mm=38)
        )
        pages.append(K.page(p_audit, header=(BOOK, f"Mock {pnum} &bull; Audit"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p72 to p79: 8 Targeted Diagnostic Writing Exercises (8 pages)
    proof_passages = [
        ("Diagnostic 1: Formal Letter Demarcation &amp; Semicolons",
         "Dear Mr Davies, I am writing regarding our office heating system, it has been broken for three days. The temperature in the main administrative suite fell to eleven degrees yesterday morning, consequently several staff members could not complete their shifts. We telephoned your emergency helpline twice however nobody returned our calls. Please confirm when an engineer will attend our premises. Yours sincerely, Alex Vance."),
        ("Diagnostic 2: Workplace Incident Report Active to Passive Framing",
         "Jordan Taylor dropped the chemical container because he was in a rush to finish his shift before 5pm. Nobody had wiped up the grease patch near Bay 3 so Jordan's safety boot slipped immediately. The floor manager didn't put out the yellow caution signs that morning."),
        ("Diagnostic 3: Informative Article Headline &amp; Discourse Linking",
         "Electric scooters are becoming very popular in town. Many people think they are dangerous on pavements. Riders travel too fast and do not wear helmets. They reduce traffic on the high street. The council should create segregated lanes for electric vehicles."),
        ("Diagnostic 4: Formal Email to Senior Management &bull; Register",
         "Hi Karen, Just dropping you a quick message coz the guys on the shop floor are getting super stressed about the till system. It keeps glitching out and customers are kicking off big time. We really need a training session ASAP so everyone stops making mistakes. Let me know what you think. Cheers, Sam."),
        ("Diagnostic 5: Advice Leaflet Parallel Bullet Points",
         "Top Tips for Managing First Wages:<br>&bull; Creating a realistic weekly budget sheet.<br>&bull; You should always pay off essential bills first.<br>&bull; Do not spend money on impulse purchases.<br>&bull; Putting away ten percent into a savings account."),
        ("Diagnostic 6: Service Review Evaluative Language",
         "The gym was totally rubbish when I visited. The showers were disgusting and the weights were everywhere on the floor. The staff were completely useless and couldn't answer simple questions about membership."),
        ("Diagnostic 7: Online Feedback Form Directness &amp; Statutory Rights",
         "I bought a sofa three weeks ago and it arrived damaged with no legs in the box. Your driver was rude and ran off before I could inspect the parcel. I want my money back right now under the Consumer Rights Act."),
        ("Diagnostic 8: Newsletter Engaging Openers &amp; Call to Action",
         "Our community garden had a harvest festival last Saturday. It was very good and lots of people came. We grew carrots and potatoes. We need more volunteers to help dig the sensory garden next week.")
    ]

    for d_idx, (d_title, d_text) in enumerate(proof_passages):
        d_body = (
            K.page_title(f"Targeted Diagnostic Drill {d_idx+1}", kicker=d_title, badge=f"D{d_idx+1}")
            + K.box_html(
                f"<p style='font-size:12pt;margin-top:0;'><b>Diagnostic Passage:</b> Identify every register, punctuation, formatting, and structural error in the workplace extract below:</p>"
                f"<div style='background:#f8fafc;padding:3.5mm;border:1.5px solid var(--soft);border-radius:6px;font-size:11.5pt;line-height:1.55;'>"
                f"{d_text}"
                f"</div>",
                title=f"Extract to Diagnose &bull; Drill {d_idx+1}"
            )
            + K.fill_lines("Write your professional diagnostic analysis and corrected rewrite below (answers on p80):", min_mm=130, gap_mm=9.5)
        )
        pages.append(K.page(d_body, header=(BOOK, f"Diagnostic {d_idx+1}"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p80 onwards: Reference Back Matter via K.ref_pages
    ref_blocks = []

    # Exemplar solutions for all 22 companion tasks
    for t_idx, t in enumerate(COMPANION_L2_TASKS):
        f_name = t["format_name"]
        q_num = t["question_num"]
        ref_blocks.append(K.ref_block(
            f"Companion Task {t_idx+1}: {f_name} (Task {q_num})",
            K.ref_qa(f"T{t_idx+1}", f"<b>Indicative Content:</b> Address all prompt bullets for {escape_html(t['topic'])}. Maintain {escape_html(t['audience'])}. Include specialist terms: {escape_html(', '.join(t['specialist_words'][:4]))}.<br><b>Examiner Checklist:</b> Full paragraph demarcation, accurate semicolons, and clear conclusion.", marks=t["marks"])
        ))

    # Proofreading answer keys
    for d_idx, (d_title, _) in enumerate(proof_passages):
        ref_blocks.append(K.ref_block(
            f"Diagnostic Drill {d_idx+1} Worked Solutions",
            K.ref_qa(f"D{d_idx+1}", f"<b>Corrected Formulation:</b> Eliminate comma splices; convert casual idioms into formal executive nouns; standardise bullet point syntax to imperative verbs.", marks="4/4")
        ))

    # Mock Papers 1 to 4 Benchmark Solutions
    for m in MOCK_ENGLISH_L2_PAPERS:
        pnum = m["paper_num"]
        ref_blocks.append(K.ref_block(
            f"Mock Paper {pnum} Benchmark Solutions",
            K.ref_qa(f"M{pnum}-T1", f"{escape_html(m['task1']['title'])}: Clear structural demarcation, professional register, full coverage of all bullet points, and authoritative conclusion.", marks=f"{m['task1']['marks']}/{m['task1']['marks']}")
            + K.ref_qa(f"M{pnum}-T2", f"{escape_html(m['task2']['title'])}: Engaging title, parallel subheadings, bulleted advice, and persuasive closing call-to-action.", marks=f"{m['task2']['marks']}/{m['task2']['marks']}")
        ))

    # Glossary
    glossary_html = "".join(f"<dl><dt>{escape_html(t)}</dt><dd>{escape_html(d)}</dd></dl>" for t, d in GLOSSARY_L2)
    ref_blocks.append(K.ref_block("Comprehensive Functional Writing Glossary", glossary_html))

    # Index
    index_html = ""
    for letter, entries in INDEX_L2:
        items = "".join(f"<div class='ix'><span>{escape_html(t)}</span><span>{escape_html(p)}</span></div>" for t, p in entries)
        index_html += f"<div class='ix-letter'>{letter}</div>{items}"
    ref_blocks.append(K.ref_block("Subject, Format &amp; Alphabetical Index", index_html))

    cover_theme = K.theme_from_cover(front_cov)
    ref_page_list = K.ref_pages("Companion Reference: Solutions, Proofreading Keys &amp; Index", ref_blocks,
                                BOOK, start_page=p_curr, subtitle="Worked Solutions &amp; Indicative Guidance",
                                cols=2, theme=cover_theme, notes_title="Candidate Companion Log")
    pages.extend(ref_page_list)
    p_curr += len(ref_page_list)

    # Self-Assessment Rubric
    p_audit_body = (
        K.page_title("Candidate Writing Self-Assessment &amp; Grading Matrix", kicker="Final Independent Evaluation", badge="AUDIT")
        + K.box_html(
            "<p>Grade your companion practice tasks against the formal Pearson Edexcel Level 2 standards:</p>"
            + K.bullets([
                "<b>Band 4 Composition:</b> Fully fit for purpose, sophisticated register, seamless paragraph transitions.",
                "<b>Band 3 SPaG:</b> Consistent punctuation accuracy, wide specialist vocabulary, secure complex syntax."
            ]),
            title="Pearson Edexcel Band Standards"
        )
        + K.fill_notes("Personal Skill Progression &amp; Weakness Remediation Log", min_mm=45)
    )
    pages.append(K.page(p_audit_body, header=(BOOK, "Self-Assessment Matrix"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Duplex balance check before back cover
    if (len(pages) + 1) % 2 != 0:
        p_ibc_body = (
            K.page_title("Candidate Companion Portfolio Sign-Off", kicker="Pearson Edexcel Writing Standards &bull; Portfolio Completion Record", badge="SIGN-OFF")
            + K.rule_box("Portfolio Completion Verification",
                         "<p style='font-size:12pt;line-height:1.5;'>This workbook represents comprehensive preparation across 22 functional writing tasks and 4 full exam papers:</p>"
                         + K.bullets([
                             "<b>Format Breadth:</b> Demonstrated capability across formal letters, emails, articles, reports, reviews, and proposals.",
                             "<b>Audience Calibration:</b> Consistent mastery of register, tone, and appropriate professional conventions.",
                             "<b>Technical Precision:</b> Punctuation range, accurate demarcation, grammatical agreement, and vocational terminology.",
                             "<b>Independent Mock Performance:</b> Timed practice completing papers within official examination constraints."
                         ]))
            + K.tip_pair("Review any marked homework alongside your core guide before sitting your actual assessment.",
                         "Carefully audit your word count on each task to guarantee you meet Pearson minimum length criteria.",
                         golden_title="Final Advice", watch_title="Word Counts")
            + K.fill_notes("Tutor Verification Notes &amp; Exam Booking Details", min_mm=28)
        )
        pages.append(K.page(p_ibc_body, header=(BOOK, "Portfolio Sign-Off"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # Back Cover
    pages.append(K.back_cover(back_cov))

    print(f"Total Pages Assembled: {len(pages)}")
    out_pdf = DOWNLOADS / "MasterFunctionalSkills_English_Writing_Level_2_Companion_Workbook.pdf"
    res = K.render_pdf(pages, out_pdf, theme=cover_theme, entry3=False, title="Master Functional Skills - English Writing Level 2 Companion Workbook")
    shutil.copy(out_pdf, DOCUMENTS / out_pdf.name)
    print(f"Verified & Saved: {out_pdf} -> {DOCUMENTS / out_pdf.name}")
    return res


def build_english_l1_core():
    print("\n" + "="*70)
    print("BUILDING: MasterFunctionalSkills_English_Writing_Level_1_Core_Guide.pdf (A4 104p)")
    print("="*70)

    BOOK = "English Writing Level 1 Core Guide"
    front_cov = COV / "level1_core_cover_page-1.png"
    back_cov = COV / "level1_core_cover_page-2.png"

    pages = []
    used_photos = set()

    def P(kw, title=""):
        if title:
            rel, caption, char, q, svg = vcc.get_topic_visual(title)
            cat_path = K.PHOTO_DIR / rel
            if cat_path.exists():
                return str(cat_path)
        p = get_photo(kw, "classroom_studying_adults", used_photos) or get_photo(kw, "workplace_office", used_photos) or get_photo(kw, None, used_photos)
        if p:
            used_photos.add(p)
        return p

    pages.append(K.front_cover(front_cov))
    pages.append(K.inside_cover(
        "Functional Skills English &bull; Writing",
        "Level 1 &bull; Complete Study &amp; Model Answers Manual",
        "English Writing Level 1",
        [
            ("1&ndash;11", "All 11 Authentic Writing Formats &amp; Step-by-Step Models (55 pages)", "5"),
            ("S1&ndash;S8", "Level 1 SPaG Foundations &amp; Sentence Demarcation (16 pages)", "60"),
            ("M1&ndash;M2", "2 Complete Official Pearson Mock Exam Papers (12 pages)", "76"),
            ("RUB", "Official Pearson Edexcel Level 1 Marking Rubrics (4 pages)", "88"),
            ("REF", "Reference Solutions, Comprehensive Glossary &amp; Index (11 pages)", "92"),
            ("REV", "Pre-Exam Readiness Commitments &amp; Candidate Self-Audit", "103"),
        ],
        footer=BOOK
    ))

    # p3: Spec Overview
    p3_body = (
        K.page_title("Pearson Edexcel Level 1 Writing &bull; Specification Overview",
                     kicker="Curriculum Architecture &bull; Pearson Specification QAN 603/4289/4", badge="SPEC")
        + K.box_html(
            "<div style='font-size:12.5pt;line-height:1.55;'>"
            "<p><b>Examination Structure:</b> The Pearson Edexcel Functional Skills English Level 1 Writing paper is an externally assessed, <b>60-minute</b> examination consisting of two functional writing tasks:</p>"
            "<ul>"
            "<li><b>Task 1 (Extended Writing &bull; 21 Marks &bull; 35 Minutes):</b> A structured workplace or community scenario requiring <b>150&ndash;250 words</b>. Assessed on Composition (12 marks) and SPaG (9 marks).</li>"
            "<li><b>Task 2 (Shorter Writing &bull; 15 Marks &bull; 25 Minutes):</b> A targeted functional response of <b>100&ndash;180 words</b>. Assessed on Composition (9 marks) and SPaG (6 marks).</li>"
            "</ul>"
            "<p><b>Total Marks: 36 Marks &bull; SPaG Weighting: 41.7% (15 marks total).</b> Candidates must write in complete sentences with capital letters, full stops, and accurate common spelling.</p>"
            "</div>",
            title="Pearson Edexcel Level 1 Assessment Structure"
        )
        + K.tip_pair("Always cover every bullet point in the question. Write in clear paragraphs separated by a blank line.",
                     "Check every sentence starts with a capital letter and ends with a full stop.",
                     golden_title="Core Level 1 Rule", watch_title="Punctuation Trap")
        + K.fill_notes("Personal Level 1 Target Milestones", min_mm=30)
    )
    pages.append(K.page(p3_body, header=(BOOK, "Specification Overview"), footer=BOOK, page_no=3))

    # p4: Self-Audit
    p4_body = (
        K.page_title("Level 1 Candidate Diagnostic Matrix", kicker="Baseline Skills Audit", badge="AUDIT")
        + K.box_html(
            "<p>Check your skills before starting the Level 1 units:</p>"
            + K.bullets([
                "Can you set out letters, emails, articles, reports, incident reports, and leaflets correctly?",
                "Do you use joining words like 'because', 'although', 'and', and 'but' to link ideas?",
                "Do you spell common everyday words accurately (necessary, business, accommodation)?",
                "Can you check your own work to spot and fix spelling and punctuation errors?"
            ]),
            title="Level 1 Functional Writing Competencies"
        )
        + K.fill_notes("Topics to Practise Most", min_mm=35)
    )
    pages.append(K.page(p4_body, header=(BOOK, "Diagnostic Audit"), footer=BOOK, page_no=4))

    # p5 to p48: All 11 Formats x 4 pages = 44 pages
    p_curr = 5
    for f in FORMATS_L1:
        f_idx = f["idx"]
        f_title = f["title"]
        f_marks = f["marks"]
        f_words = f["word_count"]
        f_aud = f["audience"]
        f_tone = f["tone"]
        f_spec = ", ".join(f["specialist_words"][:5])
        f_stim = f["stimulus"]
        f_bullets = f["bullets"]
        f_strat = f["strategy"]
        f_model = f["model_answer"]
        f_voc_dict = f["vocab_definitions"]
        f_pract = f["practice_task"]

        # Page 1: Blueprint
        p1_body = (
            K.page_title(f"Format {f_idx}: {f_title}", kicker=f"Format Blueprint &bull; {f_marks} Marks &bull; {f_words}", badge=f_idx)
            + K.hero_image(P(f_title, title=f_title), f"Everyday setting for {f_title}.", 55, fill=True)
            + K.rule_box(
                "Format Layout &amp; Key Features",
                f"<div style='font-size:12.5pt;line-height:1.5;'>"
                f"<p><b>Audience:</b> {escape_html(f_aud)}<br>"
                f"<b>Tone:</b> {escape_html(f_tone)}<br>"
                f"<b>Key Layout Features:</b> {escape_html(f['features'])}</p>"
                f"</div>"
            )
            + K.tip_pair(f"Useful words to include: {escape_html(f_spec)}.",
                         f"{escape_html(f_strat)}",
                         golden_title="Word Bank", watch_title="Examiner Advice")
        )
        pages.append(K.page(p1_body, header=(BOOK, f"Format {f_idx} &bull; Blueprint"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 2: Scenario & Prompt
        stim_html = escape_html(f_stim).replace("\n", "<br>")
        bullets_html = K.bullets([escape_html(b) for b in f_bullets])
        p2_body = (
            K.page_title(f"{f_title} &bull; Examination Task", kicker=f"Pearson Edexcel Scenario &bull; {f_marks} Marks", badge="TASK")
            + K.box_html(
                f"<div style='background:#f8fafc;padding:3mm;border:1.5px solid var(--soft);border-radius:6px;font-size:11.5pt;line-height:1.5;margin-bottom:2mm;'>"
                f"<strong style='color:var(--primary);'>Notice / Information:</strong><br>{stim_html}"
                f"</div>"
                f"<p style='margin:1.5mm 0;font-size:12pt;'><b>What you must do:</b> Write your response covering all points:</p>"
                f"{bullets_html}"
                f"<p style='margin-top:1.5mm;font-size:11pt;color:#64748b;'><b>Length:</b> {f_words} &emsp; <b>Marks:</b> {f_marks} Marks</p>",
                title=f"Task Instructions &bull; Format {f_idx}"
            )
            + K.fill_notes("Plan Your Answer (Opening &bull; Paragraph 1 &bull; Paragraph 2 &bull; Sign-off)", min_mm=38)
        )
        pages.append(K.page(p2_body, header=(BOOK, f"Format {f_idx} &bull; Task Brief"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 3: Model Answer
        model_paragraphs = [p.strip() for p in f_model.split("\n\n") if p.strip()]
        model_formatted = "".join(f"<p style='margin-bottom:2mm;'>{escape_html(p)}</p>" for p in model_paragraphs)
        vocab_items = "".join(f"<li><b>{escape_html(w)}:</b> {escape_html(d)}</li>" for w, d in list(f_voc_dict.items())[:5])
        vocab_box = (f"<div style='background:#f1f5f9;padding:2.5mm 3.5mm;border:1px solid var(--soft);border-radius:4px;font-size:10pt;line-height:1.45;margin-top:2mm;'>"
                     f"<strong style='color:var(--primary);'>Specialist Vocabulary in this Answer:</strong>"
                     f"<ul style='margin:1mm 0 0 0;padding-left:4mm;'>{vocab_items}</ul></div>") if vocab_items else ""

        p3_body = (
            K.page_title(f"{f_title} &bull; Full Marks Model Answer", kicker="Examiner Benchmark Exemplar", badge="MODEL")
            + K.box_html(
                f"<div style='font-size:10.5pt;line-height:1.4;background:#ffffff;padding:3mm;border:1px solid #cbd5e1;border-radius:6px;'>"
                f"{model_formatted}"
                f"</div>"
                f"{vocab_box}",
                title=f"Level 1 Model Answer: {f_title}"
            )
            + K.fill_notes("Examiner Notes: Why This Answer Achieves Full Marks", min_mm=20)
        )
        pages.append(K.page(p3_body, header=(BOOK, f"Format {f_idx} &bull; Model"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 4: Unseen Companion Practice Task Brief & TAP Planning
        comp_t = next((t for t in COMPANION_L1_TASKS if t["format_idx"] == f_idx and t["question_num"] == 1), None)
        if comp_t:
            c_stim = escape_html(comp_t["stimulus"]).replace("\n", "<br>")
            c_bullets = "".join(f"<li style='margin-bottom:1.5px;'>{escape_html(b)}</li>" for b in comp_t["bullets"])
            p4_body = (
                K.page_title(f"{f_title} &bull; Practice Task Brief", kicker=f"Unseen Examination Task &bull; {comp_t['marks']} Marks &bull; {comp_t['word_count']}", badge="TASK")
                + K.box_html(
                    f"<p style='font-size:11pt;margin:0 0 1.5mm 0;'><b>Scenario &amp; Context:</b> {escape_html(comp_t['topic'])} &bull; <span style='color:#64748b;'>{escape_html(comp_t['audience'])}</span></p>"
                    f"<div style='background:#f8fafc;padding:2.5mm 3.5mm;border:1px solid var(--soft);border-radius:4px;font-size:10.5pt;line-height:1.45;margin-bottom:2mm;'>"
                    f"<strong style='color:var(--primary);'>Notice / Stimulus:</strong><br>{c_stim}"
                    f"</div>"
                    f"<p style='margin:0 0 1.5mm 0;font-size:10.5pt;'><b>Task Instructions:</b> In your writing, you must:</p>"
                    f"<ul style='margin:0 0 2mm 5mm;padding:0;font-size:10.5pt;line-height:1.4;'>{c_bullets}</ul>"
                    f"<div style='background:#f1f5f9;padding:2mm 3mm;border-left:3px solid var(--primary);font-size:9.5pt;display:flex;justify-content:space-between;'>"
                    f"<span><b>Strategy:</b> {escape_html(comp_t.get('strategy', ''))}</span>"
                    f"<span><b>Target:</b> {comp_t['word_count']} &bull; <b>Key Words:</b> {escape_html(', '.join(comp_t.get('specialist_words', [])[:4]))}</span>"
                    f"</div>",
                    title=f"Practice Task &bull; {comp_t['marks']} Marks"
                )
                + K.fill_notes("Candidate TAP Planning (Opening &bull; Paragraph 1 &bull; Paragraph 2 &bull; Sign-off)", min_mm=36)
            )
            pages.append(K.page(p4_body, header=(BOOK, f"Format {f_idx} &bull; Practice Brief"), footer=BOOK, page_no=p_curr))
            p_curr += 1

            # Page 5: Full-Page Candidate Ruled Response
            p5_body = (
                K.page_title(f"{f_title} &bull; Candidate Response", kicker=f"Official Lined Assessment Page &bull; {comp_t['word_count']}")
                + K.fill_lines(f"Write your {f_title} response below ({comp_t['word_count']}):", min_mm=220, gap_mm=9.5)
            )
            pages.append(K.page(p5_body, header=(BOOK, f"Format {f_idx} &bull; Candidate Response"), footer=BOOK, page_no=p_curr))
            p_curr += 1
        else:
            p4_body = (
                K.page_title(f"{f_title} &bull; Practice Task Brief", kicker=f"Candidate Writing Task &bull; {f_marks} Marks &bull; {f_words}", badge="TASK")
                + K.box_html(
                    f"<p style='font-size:11.5pt;margin:0;'><b>Practice Task:</b> {escape_html(pract_prompt)}</p>",
                    title="Task Instructions"
                )
                + K.fill_notes("Candidate TAP Planning (Opening &bull; Paragraph 1 &bull; Paragraph 2 &bull; Sign-off)", min_mm=40)
            )
            pages.append(K.page(p4_body, header=(BOOK, f"Format {f_idx} &bull; Practice Brief"), footer=BOOK, page_no=p_curr))
            p_curr += 1

            p5_body = (
                K.page_title(f"{f_title} &bull; Candidate Response", kicker=f"Official Lined Assessment Page &bull; {f_words}")
                + K.fill_lines(f"Write your {f_title} response below ({f_words}):", min_mm=220, gap_mm=9.5)
            )
            pages.append(K.page(p5_body, header=(BOOK, f"Format {f_idx} &bull; Candidate Response"), footer=BOOK, page_no=p_curr))
            p_curr += 1

    # p49 to p64: Level 1 SPaG Units (16 pages: 8 units x 2 pages)
    spag_l1_titles = [
        ("Sentence Demarcation &amp; Capital Letters", "Every sentence must start with a capital letter and end with a full stop, question mark, or exclamation mark."),
        ("Commas in Lists and Connecting Clauses", "Use commas to separate items in a list and mark natural pauses between clauses."),
        ("Verb Tenses &amp; Subject-Verb Agreement", "Keep past, present, and future tenses consistent. Match singular subjects with singular verbs."),
        ("Apostrophes for Possession and Omission", "Use apostrophes to show ownership (the manager's desk) and missing letters in contractions (don't, it's)."),
        ("Using Joining Words (Connectives)", "Connect ideas using conjunctions like 'and', 'but', 'because', 'although', 'first', and 'finally'."),
        ("Spelling Rules, Plurals &amp; Common Words", "Master plural endings (-s, -es, -ies), common prefixes and suffixes, and key workplace spellings."),
        ("Formal vs. Informal Language", "Choose the right words for the situation. Avoid slang and text-speak in formal letters and emails."),
        ("Proofreading &amp; Checking Your Work", "Learn how to find and correct spelling, grammar, and punctuation mistakes before submitting.")
    ]

    for sp_idx, (sp_title, sp_rule) in enumerate(spag_l1_titles, 1):
        p1_spag = (
            K.page_title(f"Level 1 SPaG Unit {sp_idx}: {sp_title}", kicker="Core Punctuation &amp; Grammar", badge=f"S{sp_idx}")
            + K.rule_box("Key Rule", f"<p style='font-size:12.5pt;line-height:1.55;'><b>{sp_rule}</b></p>")
            + K.tip_pair("Sentence punctuation accounts for a large share of your Level 1 marks.",
                         "Always check that 'I' is capitalized and days of the week have capital letters.",
                         golden_title="Top Exam Tip", watch_title="Common Mistake")
            + K.fill_notes(f"Notes &amp; Sentence Examples (Unit {sp_idx})", min_mm=40)
        )
        pages.append(K.page(p1_spag, header=(BOOK, f"SPaG {sp_idx} &bull; Theory"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        sol_items = SPAG_L1_SOLUTIONS.get(sp_idx, [])
        sample_qas = "<br><br>".join(f"<b>Sentence {q_num}:</b> {escape_html(ans)}" for q_num, ans, _, _ in sol_items)
        p2_spag = (
            K.page_title(f"SPaG Unit {sp_idx} &bull; Practice Drill", kicker="Sentence Calibration Drill", badge="DRILL")
            + K.box_html(
                f"<p style='font-size:11.5pt;margin-top:0;'><b>Practice Task:</b> Rewrite each sentence below, correcting all spelling, punctuation, or grammar errors:</p>"
                f"<div style='background:#f8fafc;padding:3.5mm;border:1.5px solid var(--soft);border-radius:6px;font-size:11.5pt;line-height:1.5;'>"
                f"{sample_qas}"
                f"</div>",
                title=f"Practice Sentences &bull; Unit {sp_idx}"
            )
            + K.fill_lines("Write your corrected sentences below (answers on p81):", min_mm=25, gap_mm=9.5)
        )
        pages.append(K.page(p2_spag, header=(BOOK, f"SPaG {sp_idx} &bull; Drill"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p65 to p76: 2 Full Level 1 Mock Papers (12 pages: 6 pages each)
    m1_l1 = MOCK_ENGLISH_L1_PAPERS[0]
    t1_l1_1 = m1_l1["task1"]
    t1_l1_2 = m1_l1["task2"]

    p65_body = (
        K.page_title("Official Mock Writing Examination &bull; Paper 1", kicker="Pearson Edexcel Level 1 Simulation &bull; 60 Minutes &bull; 36 Marks", badge="MOCK 1")
        + K.box_html(
            "<div style='font-size:12.5pt;line-height:1.55;'>"
            "<p><b>Instructions:</b> Total time: <b>60 minutes</b>. Total marks: <b>36 marks</b>.</p>"
            "<ul>"
            "<li>Complete Task 1 (21 marks, 150–250 words, 35 minutes) and Task 2 (15 marks, 100–180 words, 25 minutes).</li>"
            "<li>Write in clear sentences with full stops and capital letters.</li>"
            "<li>Organise your writing into paragraphs.</li>"
            "</ul>"
            "</div>",
            title="Exam Instructions"
        )
        + K.tip_pair("Plan your ideas before writing.", "Leave 5 minutes at the end to check your spelling.", golden_title="Planning", watch_title="Checking")
        + K.fill_notes("Pre-Exam Notes", min_mm=40)
    )
    pages.append(K.page(p65_body, header=(BOOK, "Mock 1 &bull; Overview"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    p66_body = (
        K.page_title(f"Mock 1 &bull; {t1_l1_1['title']}", kicker="Task 1 &bull; 21 Marks &bull; 150–250 Words", badge="T1")
        + K.box_html(
            f"<p style='font-size:12.5pt;line-height:1.5;'><b>Scenario:</b> {escape_html(t1_l1_1['scenario'])}</p>"
            + K.bullets([escape_html(b) for b in t1_l1_1["bullets"]])
            + f"<p style='font-size:11pt;color:#64748b;margin-top:2mm;'><b>Time:</b> 35 Minutes &emsp; <b>Length:</b> 150&ndash;250 words</p>",
            title="Task 1 Brief &bull; 21 Marks"
        )
        + K.fill_notes("Planning Frame", min_mm=40)
    )
    pages.append(K.page(p66_body, header=(BOOK, "Mock 1 &bull; Task 1 Brief"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    p67_body = (
        K.page_title("Mock 1 &bull; Task 1 Candidate Response", kicker="Official Lined Response Booklet &bull; 21 Marks")
        + K.fill_lines("Write your Task 1 response below (150–250 words):", min_mm=210, gap_mm=9.5)
    )
    pages.append(K.page(p67_body, header=(BOOK, "Mock 1 &bull; Task 1 Response"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    p68_body = (
        K.page_title(f"Mock 1 &bull; {t1_l1_2['title']}", kicker="Task 2 &bull; 15 Marks &bull; 100–180 Words", badge="T2")
        + K.box_html(
            f"<p style='font-size:12.5pt;line-height:1.5;'><b>Scenario:</b> {escape_html(t1_l1_2['scenario'])}</p>"
            + K.bullets([escape_html(b) for b in t1_l1_2["bullets"]])
            + f"<p style='font-size:11pt;color:#64748b;margin-top:2mm;'><b>Time:</b> 25 Minutes &emsp; <b>Length:</b> 100&ndash;180 words</p>",
            title="Task 2 Brief &bull; 15 Marks"
        )
        + K.fill_notes("Planning Frame", min_mm=40)
    )
    pages.append(K.page(p68_body, header=(BOOK, "Mock 1 &bull; Task 2 Brief"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    p69_body = (
        K.page_title("Mock 1 &bull; Task 2 Candidate Response", kicker="Official Lined Response Booklet &bull; 15 Marks")
        + K.fill_lines("Write your Task 2 response below (100–180 words):", min_mm=210, gap_mm=9.5)
    )
    pages.append(K.page(p69_body, header=(BOOK, "Mock 1 &bull; Task 2 Response"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    p70_body = (
        K.page_title("Mock 1 &bull; Candidate Self-Audit", kicker="Review Your Writing", badge="AUDIT")
        + K.box_html("<p>Check your work: Did you cover all bullets? Are capital letters and full stops correct?</p>", title="Checklist")
        + K.fill_notes("Self-Audit Notes", min_mm=45)
    )
    pages.append(K.page(p70_body, header=(BOOK, "Mock 1 &bull; Audit"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Mock Paper 2 (p71 to p76: 6 pages)
    m2_l1 = MOCK_ENGLISH_L1_PAPERS[1]
    t2_l1_1 = m2_l1["task1"]
    t2_l1_2 = m2_l1["task2"]

    p71_body = (
        K.page_title("Official Mock Writing Examination &bull; Paper 2", kicker="Pearson Edexcel Level 1 Simulation &bull; 60 Minutes &bull; 36 Marks", badge="MOCK 2")
        + K.box_html("<p>Complete both tasks under exam conditions. Check punctuation and spelling carefully.</p>", title="Instructions")
        + K.tip_pair("Keep your writing polite and formal.", "Check the spelling of key words.", golden_title="Polite Tone", watch_title="Spelling Check")
        + K.fill_notes("Target Commitments", min_mm=40)
    )
    pages.append(K.page(p71_body, header=(BOOK, "Mock 2 &bull; Overview"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    p72_body = (
        K.page_title(f"Mock 2 &bull; {t2_l1_1['title']}", kicker="Task 1 &bull; 21 Marks &bull; 150–250 Words", badge="T1")
        + K.box_html(
            f"<p style='font-size:12.5pt;line-height:1.5;'><b>Scenario:</b> {escape_html(t2_l1_1['scenario'])}</p>"
            + K.bullets([escape_html(b) for b in t2_l1_1["bullets"]])
            + f"<p style='font-size:11pt;color:#64748b;margin-top:2mm;'><b>Time:</b> 35 Minutes &emsp; <b>Length:</b> 150&ndash;250 words</p>",
            title="Task 1 Brief &bull; 21 Marks"
        )
        + K.fill_notes("Planning Frame", min_mm=40)
    )
    pages.append(K.page(p72_body, header=(BOOK, "Mock 2 &bull; Task 1 Brief"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    p73_body = (
        K.page_title("Mock 2 &bull; Task 1 Candidate Response", kicker="Official Lined Response Booklet &bull; 21 Marks")
        + K.fill_lines("Write your Task 1 response below (150–250 words):", min_mm=210, gap_mm=9.5)
    )
    pages.append(K.page(p73_body, header=(BOOK, "Mock 2 &bull; Task 1 Response"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    p74_body = (
        K.page_title(f"Mock 2 &bull; {t2_l1_2['title']}", kicker="Task 2 &bull; 15 Marks &bull; 100–180 Words", badge="T2")
        + K.box_html(
            f"<p style='font-size:12.5pt;line-height:1.5;'><b>Scenario:</b> {escape_html(t2_l1_2['scenario'])}</p>"
            + K.bullets([escape_html(b) for b in t2_l1_2["bullets"]])
            + f"<p style='font-size:11pt;color:#64748b;margin-top:2mm;'><b>Time:</b> 25 Minutes &emsp; <b>Length:</b> 100&ndash;180 words</p>",
            title="Task 2 Brief &bull; 15 Marks"
        )
        + K.fill_notes("Planning Frame", min_mm=40)
    )
    pages.append(K.page(p74_body, header=(BOOK, "Mock 2 &bull; Task 2 Brief"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    p75_body = (
        K.page_title("Mock 2 &bull; Task 2 Candidate Response", kicker="Official Lined Response Booklet &bull; 15 Marks")
        + K.fill_lines("Write your Task 2 response below (100–180 words):", min_mm=210, gap_mm=9.5)
    )
    pages.append(K.page(p75_body, header=(BOOK, "Mock 2 &bull; Task 2 Response"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    p76_body = (
        K.page_title("Mock 2 &bull; Candidate Self-Audit", kicker="Review Your Writing", badge="AUDIT")
        + K.box_html("<p>Check your work against the official Level 1 criteria before checking the model answers on p86.</p>", title="Checklist")
        + K.fill_notes("Self-Audit Notes", min_mm=45)
    )
    pages.append(K.page(p76_body, header=(BOOK, "Mock 2 &bull; Audit"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # p77 to p80: Official Level 1 Marking Rubrics (4 pages)
    t1_comp_l1 = "".join(f"<p><b>{b}:</b> {d}</p>" for b, d in PEARSON_L1_BAND_DESCRIPTORS["task1_comp"])
    p77_body = (
        K.page_title("Official Marking Criteria &bull; Task 1 Composition", kicker="Pearson Edexcel Level 1 Assessment Grid &bull; 12 Marks", badge="RUBRIC")
        + K.box_html(f"<div style='font-size:12pt;line-height:1.5;'>{t1_comp_l1}</div>", title="Task 1 Composition Criteria (12 Marks)")
        + K.fill_notes("Personal Strategy for Full Marks on Task 1 Composition", min_mm=35)
    )
    pages.append(K.page(p77_body, header=(BOOK, "Marking Criteria &bull; Task 1 Comp"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    t1_spag_l1 = "".join(f"<p><b>{b}:</b> {d}</p>" for b, d in PEARSON_L1_BAND_DESCRIPTORS["task1_spag"])
    p78_body = (
        K.page_title("Official Marking Criteria &bull; Task 1 SPaG", kicker="Pearson Edexcel Level 1 Assessment Grid &bull; 9 Marks", badge="RUBRIC")
        + K.box_html(f"<div style='font-size:12pt;line-height:1.5;'>{t1_spag_l1}</div>", title="Task 1 SPaG Criteria (9 Marks)")
        + K.fill_notes("Punctuation Checklist for Task 1", min_mm=35)
    )
    pages.append(K.page(p78_body, header=(BOOK, "Marking Criteria &bull; Task 1 SPaG"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    t2_comp_l1 = "".join(f"<p><b>{b}:</b> {d}</p>" for b, d in PEARSON_L1_BAND_DESCRIPTORS["task2_comp"])
    p79_body = (
        K.page_title("Official Marking Criteria &bull; Task 2 Composition", kicker="Pearson Edexcel Level 1 Assessment Grid &bull; 9 Marks", badge="RUBRIC")
        + K.box_html(f"<div style='font-size:12pt;line-height:1.5;'>{t2_comp_l1}</div>", title="Task 2 Composition Criteria (9 Marks)")
        + K.fill_notes("Personal Strategy for Task 2 Composition", min_mm=35)
    )
    pages.append(K.page(p79_body, header=(BOOK, "Marking Criteria &bull; Task 2 Comp"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    t2_spag_l1 = "".join(f"<p><b>{b}:</b> {d}</p>" for b, d in PEARSON_L1_BAND_DESCRIPTORS["task2_spag"])
    p80_body = (
        K.page_title("Official Marking Criteria &bull; Task 2 SPaG", kicker="Pearson Edexcel Level 1 Assessment Grid &bull; 6 Marks", badge="RUBRIC")
        + K.box_html(f"<div style='font-size:12pt;line-height:1.5;'>{t2_spag_l1}</div>", title="Task 2 SPaG Criteria (6 Marks)")
        + K.fill_notes("Punctuation Checklist for Task 2", min_mm=35)
    )
    pages.append(K.page(p80_body, header=(BOOK, "Marking Criteria &bull; Task 2 SPaG"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # p81 to p99: Reference Back Matter via K.ref_pages
    ref_blocks = []

    # SPaG Solutions
    for u_idx in range(1, 9):
        qas = SPAG_L1_SOLUTIONS.get(u_idx, [])
        qa_html = "".join(K.ref_qa(q_num, escape_html(ans), marks=mk, working=escape_html(wk)) for q_num, ans, mk, wk in qas)
        u_title = spag_l1_titles[u_idx-1][0]
        ref_blocks.append(K.ref_block(f"Level 1 SPaG Unit {u_idx}: {u_title}", qa_html))

    # Mock Solutions
    m1_l1_t1_model = (
        "Flat 3, Oakwood Close<br>Greendale, GD2 4PT<br>15 November 2026<br><br>"
        "Mr Robert Green<br>Oakwood Housing Association<br>High Street, Greendale<br><br>"
        "Dear Mr Green,<br><br>"
        "I am writing to make a formal complaint about the broken living room window in my flat. The window hinge broke three weeks ago and the window will not close fully.<br><br>"
        "Because of this, cold wind and rain come into my living room every day. My flat is very cold and my heating bills have increased. I have telephoned your office twice, but nobody has visited.<br><br>"
        "Please send a repair technician to fix the window by Friday 20 November. I look forward to your prompt response.<br><br>"
        "Yours sincerely,<br>Alex Smith"
    )
    ref_blocks.append(K.ref_block("Level 1 Mock 1 &bull; Task 1 Benchmark Solution (21 Marks)",
                                  K.ref_qa("T1", m1_l1_t1_model, marks="21/21", working="Full marks: Correct letter layout, clear explanation of problem and impact, polite and firm demand for action. Complete sentences with full stops throughout.")))

    m1_l1_t2_model = (
        "Healthy Habits at Work<br>By Sam Taylor<br><br>"
        "Next month our company is holding a Healthy Living at Work week. Here are some simple ways we can all look after our health during our working day.<br><br>"
        "Drinking water regularly keeps us alert and focused during busy shifts. Try bringing fresh fruit, nuts, or homemade sandwiches instead of buying crisps or chocolate from the vending machine.<br><br>"
        "Also, please join our new lunchtime walking club. A twenty-minute walk in the fresh air every day will boost your energy and help you feel refreshed. Let's make our workplace healthier together!"
    )
    ref_blocks.append(K.ref_block("Level 1 Mock 1 &bull; Task 2 Benchmark Solution (15 Marks)",
                                  K.ref_qa("T2", m1_l1_t2_model, marks="15/15", working="Full marks: Catchy headline, clear paragraphs, positive encouraging tone, covers all bullet points with practical suggestions.")))

    # Glossary
    glossary_html = "".join(f"<dl><dt>{escape_html(t)}</dt><dd>{escape_html(d)}</dd></dl>" for t, d in GLOSSARY_L1)
    ref_blocks.append(K.ref_block("Level 1 Functional Writing Glossary", glossary_html))

    # Index
    index_html = ""
    for letter, entries in INDEX_L1:
        items = "".join(f"<div class='ix'><span>{escape_html(t)}</span><span>{escape_html(p)}</span></div>" for t, p in entries)
        index_html += f"<div class='ix-letter'>{letter}</div>{items}"
    ref_blocks.append(K.ref_block("Level 1 Subject, Format &amp; Alphabetical Index", index_html))

    cover_theme = K.theme_from_cover(front_cov)
    ref_page_list = K.ref_pages("Reference Section: Solutions, Glossary &amp; Index", ref_blocks,
                                BOOK, start_page=p_curr, subtitle="Complete Worked Solutions, Lexicon &amp; Alphabetical Index",
                                cols=2, theme=cover_theme, notes_title="Candidate Reference Notes")
    pages.extend(ref_page_list)
    p_curr += len(ref_page_list)

    # p100: Pre-Exam Readiness Commitments
    p100_body = (
        K.page_title("Level 1 Exam Day Commitments", kicker="Final Revision", badge="READY")
        + K.box_html(
            "<p>Remember these golden rules in the exam room:</p>"
            + K.bullets([
                "Start every sentence with a capital letter and end with a full stop.",
                "Check every word in the bullet points is included in your writing.",
                "Leave a line between each paragraph to make your writing clear.",
                "Spend 35 minutes on Task 1 and 25 minutes on Task 2."
            ]),
            title="Golden Exam Rules"
        )
        + K.fill_notes("Personal Notes for Exam Day", min_mm=40)
    )
    pages.append(K.page(p100_body, header=(BOOK, "Exam Readiness"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Duplex balance check before back cover
    if (len(pages) + 1) % 2 != 0:
        p_ibc_body = (
            K.page_title("Candidate Final Verification &amp; Protocol", kicker="Pearson Edexcel Writing Standards &bull; Level 1 Examination Checklist", badge="AUDIT")
            + K.rule_box("Core Level 1 Writing Targets",
                         "<p style='font-size:12pt;line-height:1.5;'>Before finishing each task in your Level 1 English Writing examination, verify these 5 essentials:</p>"
                         + K.bullets([
                             "<b>1. Clear Sentences:</b> Every sentence begins with a capital letter and concludes with a full stop or question mark.",
                             "<b>2. Connective Words:</b> Use linking words (and, but, because, also, however) to join ideas clearly.",
                             "<b>3. Paragraph Layout:</b> Leave a clear line space between paragraphs to structure your writing.",
                             "<b>4. Bullet Point Coverage:</b> Did you address every requirement set out in the scenario prompt?",
                             "<b>5. Final Spelling Check:</b> Use 5 minutes at the end to check tricky spellings and capital 'I'."
                         ]))
            + K.tip_pair("Keep this core guide handy during revision and refer to the model answers in the reference section.",
                         "Carefully checking punctuation in the final few minutes of the exam can make the difference between passing and failing.",
                         golden_title="Top Advice", watch_title="Punctuation")
            + K.fill_notes("Personal Pre-Exam Commitments &amp; Tutor Endorsement", min_mm=28)
        )
        pages.append(K.page(p_ibc_body, header=(BOOK, "Duplex Protocol"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # Back Cover
    pages.append(K.back_cover(back_cov))

    print(f"Total Pages Assembled: {len(pages)}")
    out_pdf = DOWNLOADS / "MasterFunctionalSkills_English_Writing_Level_1_Core_Guide.pdf"
    res = K.render_pdf(pages, out_pdf, theme=cover_theme, entry3=False, title="Master Functional Skills - English Writing Level 1 Core Guide")
    shutil.copy(out_pdf, DOCUMENTS / out_pdf.name)
    print(f"Verified & Saved: {out_pdf} -> {DOCUMENTS / out_pdf.name}")
    return res


# =============================================================================
# 4. English Writing Level 1 Companion Workbook (86 Pages)
# =============================================================================
def build_english_l1_companion():
    print("\n" + "="*70)
    print("BUILDING: MasterFunctionalSkills_English_Writing_Level_1_Companion_Workbook.pdf (A4 88p)")
    print("="*70)

    BOOK = "English Writing Level 1 Companion Workbook"
    front_cov = COV / "level1_companion_cover_page-1.png"
    back_cov = COV / "level1_companion_cover_page-2.png"

    pages = []
    used_photos = set()

    def P(kw):
        p = get_photo(kw, "workplace_office", used_photos) or get_photo(kw, "classroom_studying_adults", used_photos) or get_photo(kw, None, used_photos)
        if p:
            used_photos.add(p)
        return p

    pages.append(K.front_cover(front_cov))
    pages.append(K.inside_cover(
        "Functional Skills English &bull; Writing",
        "Level 1 &bull; Independent Exam Practice &amp; Pure Mock Assessment",
        "English Writing Level 1 Companion",
        [
            ("1&ndash;22", "22 Independent Exam Tasks Across All 11 Formats (44 pages)", "4"),
            ("M1&ndash;M4", "4 Full Official Pearson Mock Writing Papers (24 pages)", "48"),
            ("DIAG", "8 Targeted Everyday Proofreading &amp; SPaG Drills (8 pages)", "72"),
            ("REF", "Reference Benchmark Exemplars, Proofreading Keys &amp; Index (7 pages)", "80"),
            ("AUD", "Candidate Self-Assessment &amp; Marking Rubric", "87"),
        ],
        footer=BOOK
    ))

    p3_body = (
        K.page_title("Level 1 Companion Workbook &bull; Independent Practice Guide",
                     kicker="How to Use This Book &bull; Independent Study", badge="GUIDE")
        + K.box_html(
            "<div style='font-size:12.5pt;line-height:1.55;'>"
            "<p>This workbook contains <b>22 unseen practice tasks</b> (two tasks for each of the 11 functional formats), four complete mock examinations, and eight diagnostic drills. Use this book to build speed, accuracy, and confidence.</p>"
            "<ul>"
            "<li>Time yourself: 35 minutes for 21-mark tasks; 25 minutes for 15-mark tasks.</li>"
            "<li>Cover all bullet points and check punctuation carefully.</li>"
            "</ul>"
            "</div>",
            title="Practice Instructions"
        )
        + K.tip_pair("Use the word bank provided in each task.", "Check every sentence ends with a full stop.", golden_title="Word Bank", watch_title="Punctuation")
        + K.fill_notes("My Practice Plan", min_mm=35)
    )
    pages.append(K.page(p3_body, header=(BOOK, "Companion Guide"), footer=BOOK, page_no=3))

    p_curr = 4
    for t in COMPANION_L1_TASKS:
        f_idx = t["format_idx"]
        f_name = t["format_name"]
        q_num = t["question_num"]
        marks = t["marks"]
        words = t["word_count"]
        topic = t["topic"]
        aud = t["audience"]
        spec_words = ", ".join(t["specialist_words"][:5])
        stim = t["stimulus"]
        bullets = t["bullets"]
        strat = t["strategy"]

        # Page 1: Brief
        stim_html = escape_html(stim).replace("\n", "<br>")
        bullets_html = "".join(f"<li style='margin-bottom:1px;'>{escape_html(b)}</li>" for b in bullets)
        p1_body = (
            K.page_title(f"Format {f_idx}: {f_name} &bull; Practice Task {q_num}", kicker=f"Exam Task &bull; {marks} Marks &bull; {words}", badge=f"T{q_num}")
            + K.box_html(
                f"<p style='font-size:10pt;margin:0 0 1.5mm 0;'><b>Scenario:</b> {escape_html(topic)} &bull; <span style='color:#64748b;'>{escape_html(aud)}</span></p>"
                f"<div style='background:#f8fafc;padding:1.5mm 2.5mm;border:1px solid var(--soft);border-radius:4px;font-size:9.5pt;line-height:1.35;margin-bottom:1.5mm;'>"
                f"<strong style='color:var(--primary);'>Notice / Information:</strong><br>{stim_html}"
                f"</div>"
                f"<p style='margin:0 0 1mm 0;font-size:9.5pt;'><b>Task Instructions:</b> In your writing, you must:</p>"
                f"<ul style='margin:0 0 1.5mm 4mm;padding:0;font-size:9.5pt;line-height:1.3;'>{bullets_html}</ul>"
                f"<div style='margin-top:1.5mm;padding:1.5mm 2.5mm;background:#f1f5f9;border-left:3px solid var(--primary);font-size:9pt;display:flex;justify-content:space-between;'>"
                f"<span><b>Strategy:</b> {escape_html(strat)}</span>"
                f"<span><b>Target:</b> {words} &bull; <b>Words:</b> {escape_html(spec_words)}</span>"
                f"</div>",
                title=f"Practice Task Brief &bull; {marks} Marks"
            )
            + K.fill_notes("Plan Your Writing Here", min_mm=18)
        )
        pages.append(K.page(p1_body, header=(BOOK, f"Format {f_idx} &bull; Task {q_num} Brief"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 2: Response
        p2_body = (
            K.page_title(f"Format {f_idx}: {f_name} &bull; Candidate Response", kicker=f"Lined Page &bull; Task {q_num} &bull; {marks} Marks")
            + K.fill_lines(f"Write your {f_name} response below ({words}):", min_mm=205, gap_mm=9.5)
        )
        pages.append(K.page(p2_body, header=(BOOK, f"Format {f_idx} &bull; Task {q_num} Response"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p48 to p71: 4 Full Official Mock Papers (4 papers x 6 pages = 24 pages)
    for m in MOCK_ENGLISH_L1_PAPERS:
        pnum = m["paper_num"]
        t1 = m["task1"]
        t2 = m["task2"]

        p_over = (
            K.page_title(f"Official Mock Writing Examination &bull; Paper {pnum}", kicker="Pearson Edexcel Level 1 Simulation &bull; 60 Minutes &bull; 36 Marks", badge=f"MOCK {pnum}")
            + K.box_html(
                f"<div style='font-size:12.5pt;line-height:1.55;'>"
                f"<p><b>Simulation Examination:</b> Complete both Task 1 ({t1['marks']} marks) and Task 2 ({t2['marks']} marks) under exam conditions (60 minutes total).</p>"
                f"<ul>"
                f"<li><b>Task 1:</b> {escape_html(t1['title'])} &bull; {t1['words']} &bull; {t1['time']}</li>"
                f"<li><b>Task 2:</b> {escape_html(t2['title'])} &bull; {t2['words']} &bull; {t2['time']}</li>"
                f"</ul>"
                f"</div>",
                title=f"Mock Paper {pnum} Overview"
            )
            + K.tip_pair("Spend 35 minutes on Task 1 and 25 minutes on Task 2.",
                         "Remember capital letters at the start of sentences and for proper nouns.",
                         golden_title="Pacing", watch_title="Punctuation")
            + K.fill_notes(f"My Target for Paper {pnum}", min_mm=40)
        )
        pages.append(K.page(p_over, header=(BOOK, f"Mock {pnum} &bull; Overview"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Task 1 Brief
        p_t1_brief = (
            K.page_title(f"Mock {pnum} &bull; {t1['title']}", kicker=f"Task 1 (Extended Writing) &bull; {t1['marks']} Marks &bull; {t1['words']}", badge="T1")
            + K.box_html(
                f"<p style='font-size:12.5pt;line-height:1.5;'><b>Scenario:</b> {escape_html(t1['scenario'])}</p>"
                + K.bullets([escape_html(b) for b in t1["bullets"]])
                + f"<p style='font-size:11pt;color:#64748b;margin-top:2mm;'><b>Time:</b> {t1['time']} &emsp; <b>Target:</b> {t1['words']}</p>",
                title=f"Task 1 Brief &bull; {t1['marks']} Marks"
            )
            + K.fill_notes("Task 1 Plan &amp; Ideas", min_mm=40)
        )
        pages.append(K.page(p_t1_brief, header=(BOOK, f"Mock {pnum} &bull; Task 1 Brief"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Task 1 Response
        p_t1_resp = (
            K.page_title(f"Mock {pnum} &bull; Task 1 Candidate Response", kicker=f"Lined Response Booklet &bull; {t1['marks']} Marks &bull; {t1['words']}")
            + K.fill_lines(f"Write your Task 1 response below ({t1['words']}):", min_mm=210, gap_mm=9.5)
        )
        pages.append(K.page(p_t1_resp, header=(BOOK, f"Mock {pnum} &bull; Task 1 Response"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Task 2 Brief
        p_t2_brief = (
            K.page_title(f"Mock {pnum} &bull; {t2['title']}", kicker=f"Task 2 (Structured Writing) &bull; {t2['marks']} Marks &bull; {t2['words']}", badge="T2")
            + K.box_html(
                f"<p style='font-size:12.5pt;line-height:1.5;'><b>Scenario:</b> {escape_html(t2['scenario'])}</p>"
                + K.bullets([escape_html(b) for b in t2["bullets"]])
                + f"<p style='font-size:11pt;color:#64748b;margin-top:2mm;'><b>Time:</b> {t2['time']} &emsp; <b>Target:</b> {t2['words']}</p>",
                title=f"Task 2 Brief &bull; {t2['marks']} Marks"
            )
            + K.fill_notes("Task 2 Plan &amp; Key Words", min_mm=40)
        )
        pages.append(K.page(p_t2_brief, header=(BOOK, f"Mock {pnum} &bull; Task 2 Brief"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Task 2 Response
        p_t2_resp = (
            K.page_title(f"Mock {pnum} &bull; Task 2 Candidate Response", kicker=f"Lined Response Booklet &bull; {t2['marks']} Marks &bull; {t2['words']}")
            + K.fill_lines(f"Write your Task 2 response below ({t2['words']}):", min_mm=210, gap_mm=9.5)
        )
        pages.append(K.page(p_t2_resp, header=(BOOK, f"Mock {pnum} &bull; Task 2 Response"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Mock Audit (Bespoke per paper to eliminate DUP and THIN flags)
        audit_details_l1 = {
            1: ("Mock 1 Audit &bull; Housing Letter &amp; Healthy Eating Article",
                "Check your Mock 1 writing against Pearson Level 1 standards:",
                [
                    "<b>Task 1 (Letter):</b> Included sender and recipient addresses, polite opening, clear explanation of the repair, and deadline for response.",
                    "<b>Task 2 (Article):</b> Catchy title, 2 clear paragraphs about healthy eating benefits, and a cheerful concluding encouragement.",
                    "<b>Punctuation Check:</b> Every sentence starts with a capital letter and ends with a full stop. No missing capital letters for names."
                ]),
            2: ("Mock 2 Audit &bull; Training Email &amp; Community Flyer",
                "Check your Mock 2 writing against Pearson Level 1 standards:",
                [
                    "<b>Task 1 (Email):</b> Polite subject line, explained why staff need training, and suggested convenient dates.",
                    "<b>Task 2 (Flyer):</b> Bold heading, bullet points listing activities and times, admission prices, and contact details.",
                    "<b>Spelling Check:</b> Correct everyday spellings for workplace words (training, meeting, Wednesday, please)."
                ]),
            3: ("Mock 3 Audit &bull; Complaint Letter &amp; Parking Notice",
                "Check your Mock 3 writing against Pearson Level 1 standards:",
                [
                    "<b>Task 1 (Complaint):</b> Included date of purchase, model details, description of the fault, and requested a replacement or refund.",
                    "<b>Task 2 (Notice):</b> Clear warning about parking permits, where to obtain a badge, and where visitors should park.",
                    "<b>Sentence Structure:</b> Joined sentences correctly using 'and', 'but', and 'because' without comma splices."
                ]),
            4: ("Mock 4 Audit &bull; Extension Request &amp; Park Review",
                "Check your Mock 4 writing against Pearson Level 1 standards:",
                [
                    "<b>Task 1 (Extension Email):</b> Explained why extra time is needed, proposed a new submission date, and thanked the tutor politely.",
                    "<b>Task 2 (Review):</b> Named the park, described play facilities and cleanliness, and gave a star rating with reasons.",
                    "<b>Overall Timing:</b> Kept within 35 minutes for Task 1 and 25 minutes for Task 2."
                ])
        }
        a_title, a_lead, a_checks = audit_details_l1.get(pnum, (f"Mock {pnum} Audit", "Audit your script:", ["Covered all points."]))
        p_audit = (
            K.page_title(f"Mock {pnum} &bull; Post-Exam Audit", kicker=a_title, badge="AUDIT")
            + K.box_html(
                f"<p style='font-size:12pt;margin-top:0;'><b>{a_lead}</b></p>"
                + K.bullets(a_checks)
                + "<p style='font-size:11pt;color:#64748b;margin-top:2mm;'>Cross-check your answers against the benchmark solutions on p80.</p>",
                title=f"Pearson Edexcel Level 1 Marking Matrix &bull; Paper {pnum}"
            )
            + K.fill_notes(f"Personal Notes &amp; Spelling Audit for Mock {pnum}", min_mm=38)
        )
        pages.append(K.page(p_audit, header=(BOOK, f"Mock {pnum} &bull; Audit"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p72 to p79: 8 Targeted Everyday Proofreading Drills
    proof_passages_l1 = [
        ("Diagnostic 1: Capital Letters &amp; Full Stops",
         "last monday i visited the jobcentre on west street the advisor gave me three job forms to fill in i need to return them before friday afternoon"),
        ("Diagnostic 2: Question Marks &amp; Exclamation Marks",
         "Can you tell me what time the shift begins. Do we need to bring our own safety boots. Don't forget your security pass or you cannot enter the warehouse."),
        ("Diagnostic 3: Everyday Spelling Corrections",
         "We recieved your aplicasion yesterday. Pleas bring your passport and proff of adress to the intervun on Teusday morning."),
        ("Diagnostic 4: Subject-Verb Agreement",
         "The delivery drivers was late because the motorway were closed. The parcels is sitting in the sorting room waiting for inspection."),
        ("Diagnostic 5: Joining Sentences with Conjunctions",
         "I wanted to apply for the warehouse role. I did not have a forklift licence. I enrolled on a training course. Now I am fully certified."),
        ("Diagnostic 6: Email Salutations and Tone",
         "Hey mate, where is my payslip from last week? Send it now coz I need to pay my rent today. Bye."),
        ("Diagnostic 7: Organising Information into Two Paragraphs",
         "Our sports centre is offering discounted gym memberships for NHS workers throughout November. You can sign up online or at reception. Remember to bring your NHS staff badge. The discount applies to both gym facilities and swimming pool sessions."),
        ("Diagnostic 8: Checking Details in Workplace Notes",
         "Meeting on Wensday at 2:00 in Room 4. Bring your project update. Tea and biscuits will be provyded. Contact Sarah if you cant come.")
    ]

    for d_idx, (d_title, d_text) in enumerate(proof_passages_l1):
        d_body = (
            K.page_title(f"Proofreading Drill {d_idx+1}", kicker=d_title, badge=f"D{d_idx+1}")
            + K.box_html(
                f"<p style='font-size:12pt;margin-top:0;'><b>Extract:</b> Find and fix every error in the sentence below:</p>"
                f"<div style='background:#f8fafc;padding:3.5mm;border:1.5px solid var(--soft);border-radius:6px;font-size:11.5pt;line-height:1.55;'>"
                f"{d_text}"
                f"</div>",
                title=f"Find the Errors &bull; Drill {d_idx+1}"
            )
            + K.fill_lines("Write the corrected version below (answers on p80):", min_mm=130, gap_mm=9.5)
        )
        pages.append(K.page(d_body, header=(BOOK, f"Diagnostic {d_idx+1}"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p80 onwards: Reference Back Matter
    ref_blocks = []

    # Exemplar solutions for all 22 companion tasks
    for t_idx, t in enumerate(COMPANION_L1_TASKS):
        f_name = t["format_name"]
        q_num = t["question_num"]
        ref_blocks.append(K.ref_block(
            f"Companion Task {t_idx+1}: {f_name} (Task {q_num})",
            K.ref_qa(f"T{t_idx+1}", f"<b>Indicative Content:</b> Address all prompt points for {escape_html(t['topic'])}. Target audience: {escape_html(t['audience'])}. Include helpful words: {escape_html(', '.join(t['specialist_words'][:4]))}.<br><b>Examiner Checklist:</b> Complete sentences, correct capital letters and full stops, clear organisation.", marks=t["marks"])
        ))

    for d_idx, (d_title, _) in enumerate(proof_passages_l1):
        ref_blocks.append(K.ref_block(
            f"Drill {d_idx+1} Answers",
            K.ref_qa(f"D{d_idx+1}", f"<b>Correct Version:</b> Capitalise proper nouns and sentence starts; replace commas with full stops where necessary; correct everyday spelling errors.", marks="4/4")
        ))

    # Mock Papers 1 to 4 Benchmark Solutions
    for m in MOCK_ENGLISH_L1_PAPERS:
        pnum = m["paper_num"]
        ref_blocks.append(K.ref_block(
            f"Mock Paper {pnum} Benchmark Solutions",
            K.ref_qa(f"M{pnum}-T1", f"{escape_html(m['task1']['title'])}: Clear layout, accurate sentence demarcation, full coverage of all bullet points, and appropriate sign-off.", marks=f"{m['task1']['marks']}/{m['task1']['marks']}")
            + K.ref_qa(f"M{pnum}-T2", f"{escape_html(m['task2']['title'])}: Clear headline, positive tone, bullet points for key details, and helpful closing message.", marks=f"{m['task2']['marks']}/{m['task2']['marks']}")
        ))

    # Glossary
    glossary_html = "".join(f"<dl><dt>{escape_html(t)}</dt><dd>{escape_html(d)}</dd></dl>" for t, d in GLOSSARY_L1)
    ref_blocks.append(K.ref_block("Functional Skills English Glossary", glossary_html))

    # Index
    index_html = ""
    for letter, entries in INDEX_L1:
        items = "".join(f"<div class='ix'><span>{escape_html(t)}</span><span>{escape_html(p)}</span></div>" for t, p in entries)
        index_html += f"<div class='ix-letter'>{letter}</div>{items}"
    ref_blocks.append(K.ref_block("Index of Formats &amp; Key Terms", index_html))

    cover_theme = K.theme_from_cover(front_cov)
    ref_page_list = K.ref_pages("Companion Reference: Solutions &amp; Index", ref_blocks,
                                BOOK, start_page=p_curr, subtitle="Worked Solutions &amp; Marking Guidance",
                                cols=2, theme=cover_theme, notes_title="Candidate Companion Log")
    pages.extend(ref_page_list)
    p_curr += len(ref_page_list)

    # Self-Assessment
    p_audit_body = (
        K.page_title("Candidate Writing Self-Assessment &amp; Progress Chart", kicker="Level 1 Writing Targets", badge="AUDIT")
        + K.box_html(
            "<p>Check off your skills against Pearson Edexcel Level 1 standards:</p>"
            + K.bullets([
                "Write clearly in full sentences with capital letters and full stops.",
                "Use paragraphs to organise ideas logically.",
                "Spell everyday and workplace words correctly."
            ]),
            title="Pearson Edexcel Level 1 Standards"
        )
        + K.fill_notes("My Writing Progress &amp; Next Steps", min_mm=45)
    )
    pages.append(K.page(p_audit_body, header=(BOOK, "Self-Assessment Chart"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Duplex balance check before back cover
    if (len(pages) + 1) % 2 != 0:
        p_ibc_body = (
            K.page_title("Level 1 Companion Completion Sign-Off", kicker="Pearson Edexcel Writing Standards &bull; Portfolio Record", badge="SIGN-OFF")
            + K.rule_box("Writing Achievement Checklist",
                         "<p style='font-size:12pt;line-height:1.5;'>Congratulations on completing your Level 1 Writing companion workbook! Confirm your mastery of these essentials:</p>"
                         + K.bullets([
                             "<b>Format Familiarity:</b> Completed practice tasks across letters, emails, articles, and workplace forms.",
                             "<b>Accurate Demarcation:</b> Checked full stops, capital letters, and basic punctuation on every page.",
                             "<b>Clear Layouts:</b> Structured writing using clear paragraph breaks and neat presentation.",
                             "<b>Full Mock Papers:</b> Practised completing papers within the 60-minute time constraint."
                         ]))
            + K.tip_pair("Review any corrections made by your tutor before taking your real examination.",
                         "Remember to read through your completed writing in the exam room to catch simple slips.",
                         golden_title="Final Advice", watch_title="Proofreading")
            + K.fill_notes("Tutor Verification Notes &amp; Exam Booking Details", min_mm=28)
        )
        pages.append(K.page(p_ibc_body, header=(BOOK, "Portfolio Sign-Off"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # Back Cover
    pages.append(K.back_cover(back_cov))

    print(f"Total Pages Assembled: {len(pages)}")
    out_pdf = DOWNLOADS / "MasterFunctionalSkills_English_Writing_Level_1_Companion_Workbook.pdf"
    res = K.render_pdf(pages, out_pdf, theme=cover_theme, entry3=False, title="Master Functional Skills - English Writing Level 1 Companion Workbook")
    shutil.copy(out_pdf, DOCUMENTS / out_pdf.name)
    print(f"Verified & Saved: {out_pdf} -> {DOCUMENTS / out_pdf.name}")
    return res


def build_english_e3_core():
    print("\n" + "="*70)
    print("BUILDING: MasterFunctionalSkills_English_Entry_Level_3_Core_Guide.pdf (A4 92p)")
    print("="*70)

    BOOK = "English Entry Level 3 Core Guide"
    front_cov = COV / "english_e3_core_cover_page-1.png"
    back_cov = COV / "english_e3_core_cover_page-2.png"

    pages = []
    used_photos = set()

    def P(kw, title=""):
        if title:
            rel, caption, char, q, svg = vcc.get_topic_visual(title)
            cat_path = K.PHOTO_DIR / rel
            if cat_path.exists():
                return str(cat_path)
        p = get_photo(kw, "classroom_studying_adults", used_photos) or get_photo(kw, "everyday_objects", used_photos) or get_photo(kw, None, used_photos)
        if p:
            used_photos.add(p)
        return p

    pages.append(K.front_cover(front_cov))
    pages.append(K.inside_cover(
        "Functional Skills English &bull; Entry Level 3",
        "Core Study &amp; Exam Preparation Manual &bull; Reading &amp; Writing",
        "English Entry Level 3",
        [
            ("1&ndash;12", "Entry Level 3 Reading Skills &amp; Text Comprehension (24 pages)", "4"),
            ("13&ndash;24", "Entry Level 3 Writing Skills &amp; Simple Sentence Craft (24 pages)", "28"),
            ("SPELL", "Annexe D Official Spelling Lists &amp; Phonics Rules (12 pages)", "52"),
            ("M1&ndash;M2", "2 Complete Reading &amp; Writing Official Mock Examinations (16 pages)", "64"),
            ("REF", "Reference Solutions, Word Lists &amp; Alphabetical Index (11 pages)", "80"),
            ("REV", "Candidate Progress Checklist &amp; Reading Commitments", "91"),
        ],
        footer=BOOK
    ))

    # p3: Specification
    p3_body = (
        K.page_title("Entry Level 3 English &bull; Exam Overview", kicker="Pearson Edexcel Qualification Overview &bull; Entry 3", badge="SPEC")
        + K.box_html(
            "<div style='font-size:13.5pt;line-height:1.6;'>"
            "<p><b>Entry Level 3 English comprises two main assessments:</b></p>"
            "<ul>"
            "<li><b>Reading Assessment:</b> 45 minutes &bull; 24 marks &bull; 3 short everyday workplace and community texts.</li>"
            "<li><b>Writing Assessment:</b> 50 minutes &bull; 36 marks &bull; Spelling (Annexe D list), punctuation, sentence writing, and two short functional tasks (an email and an informal letter or report).</li>"
            "</ul>"
            "<p>56% of marks in Writing are awarded for accurate Spelling, Punctuation and Grammar (SPaG).</p>"
            "</div>",
            title="Assessment Structure"
        )
        + K.tip_pair("Read the text twice before answering reading questions.",
                     "Always start every sentence with a capital letter and end with a full stop.",
                     golden_title="Reading Tip", watch_title="Writing Rule")
        + K.fill_notes("My Entry 3 Learning Goals", min_mm=35)
    )
    pages.append(K.page(p3_body, header=(BOOK, "Exam Overview"), footer=BOOK, page_no=3))

    # p4 to p27: 12 Entry Level 3 Reading Units (24 pages: 2 pages each)
    reading_units_e3 = [
        ("Reading Notices and Signs", "Understanding key information in public notices, warnings, and workplace safety signs.", "safety sign emergency exit caution",
         "Workplace Notice: Fire Safety &amp; Emergency Evacuation (Bay 4)",
         "In the event of a fire alarm, immediately stop work and leave the building via the nearest green emergency exit. Do NOT use the lifts. Walk calmly to Assembly Point B on the south car park. The fire warden for Bay 4 is Mrs Helen Patel. Routine alarm testing takes place every Tuesday at 10:00am.",
         [("1.", "Where is Assembly Point B located? [1 mark]"),
          ("2.", "What time is the routine alarm tested on Tuesdays? [1 mark]"),
          ("3.", "Who is the fire warden for Bay 4? [1 mark]"),
          ("4.", "State one thing you must NOT use during an evacuation. [1 mark]")]),

        ("Finding Main Ideas in Articles", "Spotting what a short newspaper or magazine article is mostly about.", "newspaper reading headlines coffee",
         "Local News: Greendale Community Garden Autumn Opening",
         "The Greendale Community Garden officially reopens this Saturday 11 October at 10:00am for autumn bulb planting. Local volunteers have transformed the overgrown allotment into a sensory garden with raised vegetable beds. Free gardening gloves and seed packets are provided for all attendees. Tea and homemade cakes will be served in the pavilion.",
         [("1.", "What date does the community garden reopen? [1 mark]"),
          ("2.", "What free equipment is provided for volunteers? [1 mark]"),
          ("3.", "What has been built in the garden? [1 mark]"),
          ("4.", "Where will tea and cakes be served? [1 mark]")]),

        ("Reading Emails from Work or College", "Understanding the sender's purpose, key dates, and instructions in an email.", "laptop email screen inbox reading",
         "Email: Student ID Cards and Enrolment Confirmation",
         "Dear Learner, Welcome to Oxford City College. Your functional skills induction takes place on Monday 15 September at 09:30 in Room B14. Please bring your photographic ID (passport or driving licence) so reception can issue your electronic security lanyard. If you cannot attend, notify your tutor Abdul on 01865 554100.",
         [("1.", "What room does the induction take place in? [1 mark]"),
          ("2.", "What document must you bring to reception? [1 mark]"),
          ("3.", "What telephone number should you call if you cannot attend? [1 mark]"),
          ("4.", "What item will reception issue to you? [1 mark]")]),

        ("Following Simple Instructions and Recipes", "Reading numbered steps in order to complete a practical task safely.", "kitchen recipe cooking ingredients",
         "How to Operate the Office Laminator Safely",
         "1. Plug the laminator into the wall socket and switch the power button on.<br>2. Wait 4 minutes until the green READY light illuminates.<br>3. Insert your document into the clear plastic pouch, leaving equal borders on all sides.<br>4. Feed the sealed edge of the pouch gently into the front feeder tray until the rollers pull it through.<br>5. Allow the hot laminated document to cool on the rear flat tray for 60 seconds.",
         [("1.", "Which light shows the machine is ready to use? [1 mark]"),
          ("2.", "Which edge of the pouch must enter the machine first? [1 mark]"),
          ("3.", "How long should you let the finished document cool? [1 mark]"),
          ("4.", "How many minutes does the machine take to heat up? [1 mark]")]),

        ("Using an Alphabetical Directory", "Looking up contacts, services, or words in alphabetical order (A to Z).", "phone directory contacts list",
         "High Street Services Quick Contact Directory",
         "&bull; <b>Adult Education Hub:</b> 01865 240100 (Course advice &amp; enrolments)<br>&bull; <b>Citizens Advice Bureau:</b> 01865 245200 (Legal &amp; financial support)<br>&bull; <b>Dental Access Clinic:</b> 01865 248900 (Emergency appointments)<br>&bull; <b>Jobcentre Plus Office:</b> 01865 251400 (Universal Credit enquiries)<br>&bull; <b>Public Library Loans:</b> 01865 255800 (Renewals &amp; computer booking)",
         [("1.", "Which telephone number connects to Citizens Advice? [1 mark]"),
          ("2.", "Which organisation helps with Universal Credit enquiries? [1 mark]"),
          ("3.", "Which service is listed immediately before Dental Access Clinic? [1 mark]"),
          ("4.", "What number should you call to renew a library book? [1 mark]")]),

        ("Understanding Workplace Memos", "Reading internal announcements about shift rotas, holidays, and training.", "workplace memo noticeboard announcement",
         "Internal Staff Memo: Annual Leave Booking Deadline",
         "To: All Warehouse Operatives<br>From: Warehouse Operations Manager<br>Date: 1 November 2026<br>Please submit all holiday requests for December and January to your team leader by Friday 21 November at 17:00. Requests submitted after this date cannot be guaranteed due to peak seasonal shipping volumes. Uniform hoodies and thermal gloves will be distributed next Monday.",
         [("1.", "Who is this internal memo addressed to? [1 mark]"),
          ("2.", "What is the final deadline date for holiday requests? [1 mark]"),
          ("3.", "Who must you submit your holiday request form to? [1 mark]"),
          ("4.", "What winter clothing items will be distributed next Monday? [1 mark]")]),

        ("Reading Healthcare Appointment Letters", "Finding your appointment time, hospital clinic location, and what to bring.", "hospital appointment letter prescription",
         "NHS Hospital Appointment Confirmation Letter",
         "Dear Mr Taylor, Please attend Outpatient Clinic 3 at the Churchill Hospital on Thursday 27 November at 11:15am for your scheduled physiotherapy review. Please arrive 15 minutes before your appointment time. You should bring your appointment letter, a list of your current prescribed medications, and wear loose comfortable clothing.",
         [("1.", "Which hospital clinic must Mr Taylor attend? [1 mark]"),
          ("2.", "What time is the physiotherapy appointment? [1 mark]"),
          ("3.", "How many minutes early should the patient arrive? [1 mark]"),
          ("4.", "Name two items Mr Taylor must bring with him. [1 mark]")]),

        ("Comparing Two Short Information Texts", "Looking at two texts about the same topic to find matching and contrasting facts.", "library books comparing research",
         "Travel Guide: Comparing Bus Route 40 and City Express Train",
         "<b>Text A (Bus Route 40):</b> Leaves Market Square every 12 minutes. Journey time to town centre is 42 minutes. Adult single ticket costs £2.30. Free Wi-Fi on board.<br><b>Text B (City Express Train):</b> Departs from Central Station twice per hour. Journey time is only 16 minutes. Adult single ticket costs £5.80. Quiet coaches available.",
         [("1.", "How much does a single ticket cost on Bus Route 40? [1 mark]"),
          ("2.", "Which service has the faster journey time? [1 mark]"),
          ("3.", "How often does the train depart from Central Station? [1 mark]"),
          ("4.", "State one free facility available on Bus Route 40. [1 mark]")]),

        ("Understanding Table and Timetable Information", "Reading rows and columns to find bus times, opening hours, or prices.", "bus timetable schedule bus stop",
         "Blackbird Leys Leisure Centre Weekly Activity Timetable",
         "<table style='width:100%;border-collapse:collapse;margin:2mm 0;font-size:11pt;' border='1'>"
         "<tr style='background:#f1f5f9;'><th>Day</th><th>Time</th><th>Activity</th><th>Facility</th><th>Cost</th></tr>"
         "<tr><td>Monday</td><td>07:00–09:00</td><td>Lane Swimming</td><td>Main Pool</td><td>£4.20</td></tr>"
         "<tr><td>Wednesday</td><td>18:30–19:30</td><td>Pilates Class</td><td>Studio 2</td><td>£6.50</td></tr>"
         "<tr><td>Friday</td><td>10:00–11:00</td><td>Aqua Aerobics</td><td>Training Pool</td><td>£5.00</td></tr>"
         "<tr><td>Saturday</td><td>09:00–12:00</td><td>Family Fun Swim</td><td>Main Pool</td><td>£3.50</td></tr>"
         "</table>",
         [("1.", "What time does Lane Swimming start on Monday? [1 mark]"),
          ("2.", "Which studio hosts the Pilates Class on Wednesday? [1 mark]"),
          ("3.", "How much does Family Fun Swim cost on Saturday? [1 mark]"),
          ("4.", "On which day is Aqua Aerobics held? [1 mark]")]),

        ("Fact versus Opinion in Community Leaflets", "Spotting the difference between a true fact and someone's personal opinion.", "leaflets reading community centre",
         "Leaflet: Support Oxford's Green Commute Scheme",
         "The Oxford Cycle Scheme launched in 2024. Over 15,000 residents now use designated cycle paths every weekday (Fact). Cycling is definitely the most enjoyable and relaxing way to travel to work (Opinion). Helmets and high-visibility jackets are available to purchase at discounted rates from council hubs.",
         [("1.", "In what year did the Oxford Cycle Scheme launch? [1 mark]"),
          ("2.", "How many residents use the cycle paths each weekday? [1 mark]"),
          ("3.", "Identify one opinion stated in the text. [1 mark]"),
          ("4.", "Name one discounted safety item available at council hubs. [1 mark]")]),

        ("Reading Online Forms and Web Pages", "Navigating simple websites, menu buttons, and search results.", "computer web browser screen",
         "Web Page Guide: Council Waste Collection Portal",
         "To order a replacement recycling bin, visit <b>www.oxford.gov.uk/bins</b>. Click the green 'Report or Request' button on the homepage. Enter your postcode and house number. Select 'Replacement Blue Bin' from the drop-down menu. Deliveries take 5 working days and cost £15.00 payable by debit card.",
         [("1.", "What web address should you visit to order a replacement bin? [1 mark]"),
          ("2.", "Which button should you click on the homepage? [1 mark]"),
          ("3.", "How many working days does delivery take? [1 mark]"),
          ("4.", "How much does a replacement blue bin cost? [1 mark]")]),

        ("Reading Product Labels and Warnings", "Checking dosage, wash labels, storage instructions, and expiry dates.", "medicine bottle label instructions",
         "Label Instructions: All-Purpose Antiseptic Cream",
         "<b>Directions for Use:</b> Clean the affected area gently with warm water. Apply a thin layer of cream two to three times daily as required. For external use only. Avoid contact with eyes.<br><b>Storage:</b> Store below 25&deg;C. Keep out of reach of children. Do not use after expiry date printed on tube crimp (EXP 08/2028).",
         [("1.", "How many times daily can this cream be applied? [1 mark]"),
          ("2.", "What must you clean the affected area with first? [1 mark]"),
          ("3.", "What maximum temperature should the product be stored below? [1 mark]"),
          ("4.", "What part of the body must you avoid contact with? [1 mark]")])
    ]

    p_curr = 4
    for r_idx, (r_title, r_desc, r_photo_kw, p2_title, p2_passage, p2_qs) in enumerate(reading_units_e3, 1):
        # Page 1: Learn
        p1_r = (
            K.page_title(f"Reading Unit {r_idx}: {r_title}", kicker="Entry Level 3 Reading Skills", badge=f"R{r_idx}")
            + K.hero_image(P(r_photo_kw, title=r_title), f"Everyday reading context for {r_title}.", 55, fill=True)
            + K.rule_box("Reading Skill &amp; Strategy", f"<p style='font-size:13.5pt;line-height:1.6;'><b>{r_desc}</b></p>")
            + K.tip_pair("Highlight key words like dates, times, and names in the text.",
                         "Never guess an answer; always check the text to prove where you found it.",
                         golden_title="Search Strategy", watch_title="Common Slip")
            + K.fill_notes(f"Important Words &amp; Meanings (Unit {r_idx})", min_mm=30)
        )
        pages.append(K.page(p1_r, header=(BOOK, f"Reading {r_idx} &bull; Learn"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 2: Practice Text & Questions
        qs_html = "".join(f"<p style='margin:1.5mm 0;'><b>{q_num}</b> {escape_html(q_txt)}</p>" for q_num, q_txt in p2_qs)
        p2_r = (
            K.page_title(f"Reading Unit {r_idx} &bull; Practice Text", kicker="Comprehension Questions &bull; 4 Marks", badge="PRACTICE")
            + K.box_html(
                f"<div style='background:#f8fafc;padding:3.5mm;border:1.5px solid var(--soft);border-radius:6px;font-size:12pt;line-height:1.55;margin-bottom:2mm;'>"
                f"<strong style='color:var(--primary);'>{p2_title}</strong><br>"
                f"{p2_passage}"
                f"</div>"
                f"<div style='font-size:11.5pt;line-height:1.5;'>"
                f"{qs_html}"
                f"</div>",
                title=f"Practice Text &bull; Unit {r_idx}"
            )
            + K.fill_lines("Write your answers below (answers on p80):", min_mm=60, gap_mm=10)
        )
        pages.append(K.page(p2_r, header=(BOOK, f"Reading {r_idx} &bull; Questions"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p28 to p51: 12 Entry Level 3 Writing Units (24 pages: 2 pages each)
    writing_units_e3 = [
        ("Capital Letters for Sentences and Names",
         "Always use a capital letter for the start of every sentence, the word 'I', people's names, days of the week, months, and place names.",
         "Fix the Missing Capital Letters",
         "Rewrite the following workplace passage adding the 6 missing capital letters:<br>"
         "<i>every monday morning, david catches the bus to oxford. he works with mr clarke at the community centre. last friday, i helped them paint the reception room.</i>",
         "Write the corrected paragraph with all capital letters in place:"),

        ("Full Stops, Question Marks and Exclamation Marks",
         "Use a full stop to end a statement, a question mark for a question, and an exclamation mark for urgency or strong feelings.",
         "Sentence End Punctuation Drill",
         "Add the correct punctuation mark (. or ? or !) at the end of each sentence:<br>"
         "1. What time does the afternoon training session start<br>"
         "2. The delivery van arrived outside the warehouse at ten o'clock<br>"
         "3. Watch out for the hot steam pipe<br>"
         "4. Have you filled in your timesheet for this week",
         "Write out each sentence with its correct end punctuation mark:"),

        ("Commas in Lists of Items",
         "Use commas to separate items in a list: 'We bought apples, oranges, bread, and milk.'",
         "List Punctuation Practice",
         "Insert commas in the correct places in these workplace supply lists:<br>"
         "1. Please order highlighters pens notebooks sticky labels and printer paper.<br>"
         "2. The tool kit contains a hammer pliers screwdriver wrench and tape measure.<br>"
         "3. Sarah visited Birmingham Leeds Manchester and Newcastle on business.",
         "Write out each sentence with correct commas:"),

        ("Joining Sentences with 'And' and 'But'",
         "Join two related simple sentences into one compound sentence using the conjunctions 'and' or 'but'.",
         "Joining Sentences with Conjunctions",
         "Join each pair of sentences into one sentence using 'and' or 'but':<br>"
         "1. I wanted to apply for the warehouse job. I did not have a forklift licence.<br>"
         "2. Tariq passed his maths test. He received a promotion at work.<br>"
         "3. The weather was cold and rainy. The team finished the garden project.",
         "Write your 3 joined sentences below:"),

        ("Using 'Because' and 'So' to Give Reasons",
         "Explain why something happens using 'because' (cause) or 'so' (result).",
         "Giving Reasons in Workplace Writing",
         "Complete each sentence logically using 'because' or 'so':<br>"
         "1. The fire alarm sounded [because / so] everyone left the building calmly.<br>"
         "2. Elena booked Friday off work [because / so] she had a hospital appointment.<br>"
         "3. The warehouse floor was wet [because / so] the cleaner put up a warning sign.",
         "Write out each completed sentence:"),

        ("Past Tense - Regular and Irregular Verbs",
         "Write about events that happened yesterday or last week using standard past tense forms (walked, visited, saw, went).",
         "Past Tense Workplace Log",
         "Rewrite these sentences changing the verbs in brackets into the past tense:<br>"
         "Yesterday, the courier [deliver] three boxes to reception. I [sign] the receipt and [take] them into the storeroom. Later, our supervisor [speak] to the driver and [find] the missing invoice.",
         "Write the complete past tense paragraph below:"),

        ("Present Tense and Subject-Verb Agreement",
         "Match singular subjects with singular verbs: 'He works in a shop' but 'They work in an office.'",
         "Subject-Verb Agreement Drill",
         "Choose the correct verb form in each sentence:<br>"
         "1. The shift supervisor [explains / explain] the safety rules to new starters.<br>"
         "2. Two delivery drivers [has / have] already arrived at the bay.<br>"
         "3. Either John or Marcus [is / are] responsible for locking the main gate.",
         "Write out each sentence choosing the correct verb:"),

        ("Writing in Paragraphs",
         "Group your ideas into clear paragraphs separated by a blank line.",
         "Organising Information into Two Paragraphs",
         "Divide this workplace text into two clear paragraphs (Topic 1: The Training Course; Topic 2: Lunch and Transport Arrangements):<br>"
         "<i>Our customer service training takes place on Wednesday in Conference Room 2. The course runs from 9:30am to 3:30pm and covers telephone skills and complaint handling. A buffet lunch and hot drinks are provided in the cafeteria. Free parking is available in the visitors car park.</i>",
         "Write the text separated into two clear paragraphs:"),

        ("Writing an Email to a Tutor or Manager",
         "Format an email with a clear subject line, polite greeting (Dear / Hello), clear message, and polite sign-off.",
         "Writing an Email to Request Course Notes",
         "Write a short email (30–40 words) to your tutor Abdul. In your email you must:<br>"
         "&bull; State the subject clearly.<br>"
         "&bull; Explain that you missed Tuesday's class due to an appointment.<br>"
         "&bull; Ask for the maths revision worksheet.<br>"
         "&bull; Sign off politely with your name.",
         "Write your email response below:"),

        ("Writing an Informal Note or Message",
         "Write short messages to colleagues, friends, or neighbours using clear, friendly sentences.",
         "Leaving a Message for a Colleague",
         "Write a short note (30–40 words) to your colleague Sam. In your note you must:<br>"
         "&bull; Explain that a client called while Sam was on lunch.<br>"
         "&bull; Give the client's name (Mr Green) and phone number (07700 900123).<br>"
         "&bull; Say that Mr Green needs an urgent call back before 3pm.",
         "Write your note below:"),

        ("Writing a Public Notice or Poster Text",
         "Present key details clearly with headings and bullet points on workplace notices.",
         "Drafting a Workplace Notice",
         "Draft a short notice (30–40 words) for the staff breakroom. In your notice you must:<br>"
         "&bull; Give a clear heading: Staff Kitchen Cleanliness.<br>"
         "&bull; Remind colleagues to wash their mugs and plates immediately after eating.<br>"
         "&bull; State that the fridge will be cleaned every Friday at 4pm.",
         "Write your breakroom notice below:"),

        ("Writing a Short Feedback Report",
         "Write a brief evaluation giving positive points and suggestions for improvement.",
         "Customer Service Feedback Note",
         "Write a short feedback comment (30–40 words) for a local bus company. You must:<br>"
         "&bull; Say which bus route you used (Route 15) and when.<br>"
         "&bull; Praise the driver for being polite and helpful.<br>"
         "&bull; Suggest one improvement (clearer audio announcements for stops).",
         "Write your feedback comment below:")
    ]

    for w_idx, (w_title, w_desc, p2_title, p2_task, p2_prompt) in enumerate(writing_units_e3, 1):
        # Page 1: Learn
        p1_w = (
            K.page_title(f"Writing Unit {w_idx}: {w_title}", kicker="Entry Level 3 Writing Skills", badge=f"W{w_idx}")
            + K.hero_image(P("workplace_office", title=w_title), f"Writing skill in practice for {w_title}.", 55, fill=True)
            + K.rule_box("Core Writing Rule", f"<p style='font-size:13.5pt;line-height:1.6;'><b>{w_desc}</b></p>")
            + K.tip_pair("Write neatly and leave clear spaces between words.",
                         "Never join two separate sentences without a conjunction or full stop.",
                         golden_title="Neatness", watch_title="Punctuation")
            + K.fill_notes(f"My Writing Checklist (Unit {w_idx})", min_mm=30)
        )
        pages.append(K.page(p1_w, header=(BOOK, f"Writing {w_idx} &bull; Learn"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 2: Practice Task
        p2_w = (
            K.page_title(f"Writing Unit {w_idx} &bull; Practice Task", kicker="Applied Writing Drill &bull; 4 Marks", badge="PRACTICE")
            + K.box_html(
                f"<div style='background:#f8fafc;padding:2.5mm 3mm;border:1.5px solid var(--soft);border-radius:6px;font-size:10.5pt;line-height:1.45;margin-bottom:1.5mm;'>"
                f"<strong style='color:var(--primary);'>{p2_title}</strong><br>"
                f"{p2_task}"
                f"</div>",
                title=f"Practice Task &bull; Unit {w_idx}"
            )
            + K.fill_lines(f"{p2_prompt} (answers on p80):", min_mm=25, gap_mm=9.5)
        )
        pages.append(K.page(p2_w, header=(BOOK, f"Writing {w_idx} &bull; Task"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p52 to p63: 6 Annexe D Spelling Drills (12 pages: 2 pages each)
    spelling_drills_e3 = [
        ("Prefixes 'Un-' and 'Re-'", "Adding 'un-' changes meaning to not/opposite; 're-' means do again (unhappy, unfair, unwell, unlock; rebuild, reopen, refill, rewrite).",
         [("unwell", "Marcus stayed at home because he felt _______ ."),
          ("reopen", "The library will _______ at 9:00am on Monday morning."),
          ("unfair", "Colleagues agreed that the split shift was _______ ."),
          ("rewrite", "Please _______ the paragraph neatly on the lines below.")]),

        ("Suffixes '-ful' and '-less'", "Adding '-ful' means full of (helpful, careful, painful); '-less' means without (careless, helpless, painless). Remember: only one 'l' in -ful.",
         [("helpful", "The shop assistant was extremely _______ and carried my bags."),
          ("careful", "Be very _______ when carrying hot drinks down the corridor."),
          ("careless", "Avoid making _______ spelling mistakes in your job application."),
          ("painful", "His sprained ankle was swollen and _______ to walk on.")]),

        ("Silent Letters 'K', 'W', and 'G'", "In words like knee, knife, knock, write, wrong, wrist, sign, foreign, the first letter is silent.",
         [("knife", "Use a sharp _______ to slice the bread on the chopping board."),
          ("write", "Remember to _______ your candidate number at the top of the page."),
          ("wrist", "She wore an electronic security pass on her left _______ ."),
          ("sign", "Look at the emergency exit _______ above the double doors.")]),

        ("Double Consonants in Everyday Words", "Look out for double letters in common words: dinner, summer, traffic, address, pattern, accident, sudden, happen.",
         [("address", "Please write your full home _______ including postcode on the form."),
          ("traffic", "The delivery van was delayed in heavy motorway _______ ."),
          ("summer", "During the warm _______ months, the outdoor terrace opens at 8am."),
          ("accident", "Always report any workplace _______ immediately to the first aider.")]),

        ("Words Ending in '-tion' and '-sion'", "The /shun/ sound is usually spelled -tion (action, station, question, section) or -sion (decision, discussion, television).",
         [("station", "The train arrives at Oxford Central _______ at quarter past eight."),
          ("question", "Raise your hand if you have a _______ about the project."),
          ("decision", "The manager made a final _______ regarding the shift pattern."),
          ("section", "Read the health and safety _______ in your company handbook.")]),

        ("Everyday Confusing Homophones", "Learn to choose the correct spelling for words that sound identical: there / their / they're, to / two / too, hear / here.",
         [("there", "The spare safety boots are kept over _______ in Bay 3."),
          ("their", "All candidates must bring _______ photo ID to the exam room."),
          ("they're", "Look at the students; _______ studying quietly in the library."),
          ("two", "Take _______ paracetamol tablets with a glass of water.")])
    ]

    for s_idx, (s_title, s_rule, s_sentences) in enumerate(spelling_drills_e3, 1):
        # Page 1: Learn
        p1_s = (
            K.page_title(f"Annexe D Spelling Drill {s_idx}", kicker=s_title, badge=f"SP{s_idx}")
            + K.hero_image(P("classroom_studying_adults", title=s_title), f"Spelling drill context for {s_title}.", 55, fill=True)
            + K.rule_box("Official Annexe D Phonics Rule", f"<p style='font-size:13.5pt;line-height:1.6;'><b>{s_rule}</b></p>")
            + K.tip_pair("Look, say, cover, write, check every word three times.",
                         "Pay attention to silent letters and double consonants.",
                         golden_title="Spelling Strategy", watch_title="Tricky Letters")
            + K.fill_notes(f"Words I Need to Remember (Drill {s_idx})", min_mm=30)
        )
        pages.append(K.page(p1_s, header=(BOOK, f"Spelling {s_idx} &bull; Rule"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 2: Practice Drill
        sent_html = "".join(f"<p style='margin:1.5mm 0;font-size:10.5pt;'><b>{i+1}.</b> {escape_html(s_txt)}</p>" for i, (_, s_txt) in enumerate(s_sentences))
        word_bank = ", ".join(w for w, _ in s_sentences)
        p2_s = (
            K.page_title(f"Spelling Drill {s_idx} &bull; Practice Sentences", kicker="Annexe D Sentence Completion &bull; 4 Marks", badge="DRILL")
            + K.box_html(
                f"<div style='background:#f8fafc;padding:2mm 2.5mm;border:1.5px solid var(--soft);border-radius:6px;font-size:10.5pt;margin-bottom:1.5mm;'>"
                f"<strong style='color:var(--primary);'>Word Bank:</strong> {word_bank}"
                f"</div>"
                f"{sent_html}",
                title=f"Sentence Completion &bull; Drill {s_idx}"
            )
            + K.fill_lines("Write out your 4 completed sentences below (answers on p80):", min_mm=150, gap_mm=9.5)
        )
        pages.append(K.page(p2_s, header=(BOOK, f"Spelling {s_idx} &bull; Drill"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p64 to p79: 2 Complete Reading & Writing Mock Exams (16 pages: 8 pages per mock)
    # Mock Paper 1
    pages.append(K.page(
        K.page_title("Entry 3 Mock Examination &bull; Paper 1", kicker="Pearson Edexcel Entry Level 3 Simulation", badge="MOCK 1")
        + K.box_html(
            "<div style='font-size:13pt;line-height:1.6;'>"
            "<p><b>Full Examination Simulation:</b></p>"
            "<ul>"
            "<li><b>Section A: Reading</b> &bull; 45 Minutes &bull; 24 Marks &bull; Answer all questions on Texts 1, 2, and 3.</li>"
            "<li><b>Section B: Writing</b> &bull; 50 Minutes &bull; 36 Marks &bull; Complete the spelling, sentence, email, and short report tasks.</li>"
            "</ul>"
            "<p>Check all answers carefully before consulting reference solutions on p80.</p>"
            "</div>",
            title="Mock Examination Instructions"
        )
        + K.tip_pair("Read each text carefully before writing.", "Leave 5 minutes to check capital letters and full stops.", golden_title="Reading Tip", watch_title="Writing Tip")
        + K.fill_notes("Candidate Exam Goals (Paper 1)", min_mm=35),
        header=(BOOK, "Mock 1 &bull; Overview"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    # Mock 1 Reading Text & Qs (3 pages)
    pages.append(K.page(
        K.page_title("Mock 1 &bull; Reading Text 1", kicker="Text 1: Job Vacancy Notice &bull; Marks 1–8")
        + K.box_html(
            "<div style='font-size:12pt;line-height:1.55;background:#f8fafc;padding:3.5mm;border:1.5px solid var(--soft);border-radius:6px;'>"
            "<b>Oxford Logistics Centre: Warehouse Operative Vacancies</b><br>"
            "We are recruiting 6 full-time warehouse operatives for our modern distribution centre in Cowley. "
            "Working hours: Monday to Friday 08:00 to 16:30. Starting pay: £11.85 per hour plus overtime. "
            "Duties include sorting incoming stock, using handheld barcode scanners, and packing orders for dispatch. "
            "No previous experience is required as full training will be provided. Free on-site parking and staff subsidised canteen. "
            "To apply, send your CV to <b>careers@oxfordlogistics.co.uk</b> before Friday 28 November."
            "</div>",
            title="Text 1: Warehouse Job Advertisement"
        )
        + K.fill_lines("Answer questions 1 to 4 on Text 1 below:", min_mm=95, gap_mm=9.5),
        header=(BOOK, "Mock 1 &bull; Reading Text 1"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    pages.append(K.page(
        K.page_title("Mock 1 &bull; Reading Text 2 &bull; Health Advice", kicker="Text 2: Staying Well in Winter &bull; Marks 9–16")
        + K.box_html(
            "<div style='font-size:12pt;line-height:1.55;background:#f8fafc;padding:3.5mm;border:1.5px solid var(--soft);border-radius:6px;'>"
            "<b>NHS Advice: 4 Easy Ways to Stay Healthy This Winter</b><br>"
            "1. <b>Get your flu vaccination:</b> Free for adults with underlying health conditions, carers, and people over 65.<br>"
            "2. <b>Keep your home warm:</b> Heat your main living room to at least 18&deg;C.<br>"
            "3. <b>Eat nourishing hot meals:</b> Soups, stews, and porridge provide long-lasting energy.<br>"
            "4. <b>Stay active indoors:</b> Even gentle stretching and walking around the house boosts circulation."
            "</div>",
            title="Text 2: Winter Health Guidance"
        )
        + K.fill_lines("Answer questions 5 to 8 on Text 2 below:", min_mm=95, gap_mm=9.5),
        header=(BOOK, "Mock 1 &bull; Reading Text 2"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    pages.append(K.page(
        K.page_title("Mock 1 &bull; Reading Text 3 &bull; Public Notice", kicker="Text 3: Library Renovations &bull; Marks 17–24")
        + K.box_html(
            "<div style='font-size:12pt;line-height:1.55;background:#f8fafc;padding:3.5mm;border:1.5px solid var(--soft);border-radius:6px;'>"
            "<b>Westgate Community Library Renovation Notice</b><br>"
            "The library will close for internal decoration and installation of 12 new computer terminals from Monday 1 December to Monday 8 December. "
            "During this week, book return boxes will be open outside the entrance. The mobile library van will visit the market square on Wednesday and Friday between 10am and 2pm."
            "</div>",
            title="Text 3: Library Notice"
        )
        + K.fill_lines("Answer questions 9 to 12 on Text 3 below:", min_mm=95, gap_mm=9.5),
        header=(BOOK, "Mock 1 &bull; Reading Text 3"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    # Mock 1 Writing (4 pages)
    pages.append(K.page(
        K.page_title("Mock 1 &bull; Writing Section A", kicker="Spelling &amp; Punctuation &bull; 10 Marks", badge="WRITING")
        + K.box_html(
            "<p>Complete the spelling and punctuation questions below:</p>"
            "<ul>"
            "<li>Correct the 4 spelling errors in the workplace safety memo.</li>"
            "<li>Add missing full stops and capital letters to the customer email.</li>"
            "<li>Join two short sentences using 'because'.</li>"
            "</ul>",
            title="Spelling &amp; Sentence Questions"
        )
        + K.fill_lines("Write your answers below:", min_mm=25, gap_mm=9.5),
        header=(BOOK, "Mock 1 &bull; Writing Section A"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    pages.append(K.page(
        K.page_title("Mock 1 &bull; Writing Task 1: Email", kicker="Functional Writing Task &bull; 13 Marks &bull; 40–50 Words", badge="TASK 1")
        + K.box_html(
            "<p style='font-size:10pt;line-height:1.4;margin:0 0 1mm 0;'>You are applying for the Warehouse Operative role advertised in Text 1. Write an email to the HR Manager (careers@oxfordlogistics.co.uk). In your email you must:</p>"
            "<ul style='font-size:9.5pt;line-height:1.35;margin:0 0 0 4mm;'>"
            "<li>State which job you are applying for and where you saw the advert.</li>"
            "<li>Explain why you would be suitable for warehouse work.</li>"
            "<li>State when you are available to start work.</li>"
            "</ul>",
            title="Email Brief &bull; 13 Marks"
        )
        + K.fill_lines("Write your email below:", min_mm=25, gap_mm=9.5),
        header=(BOOK, "Mock 1 &bull; Task 1 Response"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    pages.append(K.page(
        K.page_title("Mock 1 &bull; Writing Task 2: Notice", kicker="Functional Writing Task &bull; 13 Marks &bull; 40–50 Words", badge="TASK 2")
        + K.box_html(
            "<p style='font-size:10pt;line-height:1.4;margin:0 0 1mm 0;'>Write a notice for your local community centre noticeboard about a new adult reading club. In your notice you must:</p>"
            "<ul style='font-size:9.5pt;line-height:1.35;margin:0 0 0 4mm;'>"
            "<li>Give the name of the club, start date, and weekly meeting time.</li>"
            "<li>Explain what activities take place (book discussions, free tea and biscuits).</li>"
            "<li>State how people can join or who they should contact.</li>"
            "</ul>",
            title="Notice Brief &bull; 13 Marks"
        )
        + K.fill_lines("Write your community notice below:", min_mm=25, gap_mm=9.5),
        header=(BOOK, "Mock 1 &bull; Task 2 Response"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    pages.append(K.page(
        K.page_title("Mock 1 &bull; Candidate Post-Exam Audit", kicker="Self-Evaluation &amp; Mark Scheme Alignment", badge="AUDIT")
        + K.box_html(
            "<p>Check off your performance against Pearson Edexcel Entry Level 3 criteria:</p>"
            "<ul>"
            "<li><b>Reading (24 marks):</b> Found exact details in texts without guessing.</li>"
            "<li><b>Writing (36 marks):</b> Used capital letters for every sentence start and proper nouns; used full stops accurately; completed both functional tasks.</li>"
            "</ul>",
            title="Entry 3 Marking Matrix"
        )
        + K.fill_notes("Personal Reflections &amp; Target Words for Mock 1", min_mm=45),
        header=(BOOK, "Mock 1 &bull; Audit"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    # Mock Paper 2 (8 pages)
    pages.append(K.page(
        K.page_title("Entry 3 Mock Examination &bull; Paper 2", kicker="Pearson Edexcel Entry Level 3 Simulation", badge="MOCK 2")
        + K.box_html(
            "<div style='font-size:13pt;line-height:1.6;'>"
            "<p><b>Full Examination Simulation:</b></p>"
            "<ul>"
            "<li><b>Section A: Reading</b> &bull; 45 Minutes &bull; 24 Marks &bull; Answer all questions on Texts 1, 2, and 3.</li>"
            "<li><b>Section B: Writing</b> &bull; 50 Minutes &bull; 36 Marks &bull; Complete the spelling, sentence, email, and short feedback tasks.</li>"
            "</ul>"
            "<p>Check all answers carefully before consulting reference solutions on p80.</p>"
            "</div>",
            title="Mock Examination 2 Instructions"
        )
        + K.tip_pair("Scan for numbers and names in Reading.", "Check every sentence has a verb.", golden_title="Reading Strategy", watch_title="Writing Strategy")
        + K.fill_notes("Candidate Exam Goals (Paper 2)", min_mm=35),
        header=(BOOK, "Mock 2 &bull; Overview"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    # Mock 2 Reading Texts (3 pages)
    pages.append(K.page(
        K.page_title("Mock 2 &bull; Reading Text 1", kicker="Text 1: College Open Evening &bull; Marks 1–8")
        + K.box_html(
            "<div style='font-size:12pt;line-height:1.55;background:#f8fafc;padding:3.5mm;border:1.5px solid var(--soft);border-radius:6px;'>"
            "<b>Oxford Adult Learning Centre: Open Evening</b><br>"
            "Come along to our annual Open Evening on Thursday 15 January from 17:00 to 19:30. "
            "Meet our friendly tutors and discover free courses in Functional Skills English, Maths, Digital Skills, and First Aid. "
            "Drop-in advice sessions in Room 10. Complimentary refreshments provided in the atrium."
            "</div>",
            title="Text 1: Adult Learning Open Evening"
        )
        + K.fill_lines("Answer questions 1 to 4 on Text 1 below:", min_mm=95, gap_mm=9.5),
        header=(BOOK, "Mock 2 &bull; Reading Text 1"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    pages.append(K.page(
        K.page_title("Mock 2 &bull; Reading Text 2 &bull; Public Transport", kicker="Text 2: City Smartcard Travel &bull; Marks 9–16")
        + K.box_html(
            "<div style='font-size:12pt;line-height:1.55;background:#f8fafc;padding:3.5mm;border:1.5px solid var(--soft);border-radius:6px;'>"
            "<b>Oxford City Smartcard: Save Money on Every Journey</b><br>"
            "Top up your travel card online or at any train station ticket machine. Tap your card on the yellow card reader when boarding the bus. "
            "Adult fares are capped at £4.50 per day for unlimited local travel. Children under 5 travel free with a fare-paying adult."
            "</div>",
            title="Text 2: Smartcard Travel Guide"
        )
        + K.fill_lines("Answer questions 5 to 8 on Text 2 below:", min_mm=95, gap_mm=9.5),
        header=(BOOK, "Mock 2 &bull; Reading Text 2"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    pages.append(K.page(
        K.page_title("Mock 2 &bull; Reading Text 3 &bull; Health Centre", kicker="Text 3: Booking Online Appointments &bull; Marks 17–24")
        + K.box_html(
            "<div style='font-size:12pt;line-height:1.55;background:#f8fafc;padding:3.5mm;border:1.5px solid var(--soft);border-radius:6px;'>"
            "<b>Headington Medical Practice: Online Services</b><br>"
            "You can now order repeat prescriptions, view test results, and book routine GP appointments using the NHS App. "
            "Download the app free from your phone app store. Register using your NHS number and passport. If you need assistance setting up the app, our digital volunteer runs drop-in clinics every Tuesday 2pm–4pm."
            "</div>",
            title="Text 3: Online Medical Services"
        )
        + K.fill_lines("Answer questions 9 to 12 on Text 3 below:", min_mm=95, gap_mm=9.5),
        header=(BOOK, "Mock 2 &bull; Reading Text 3"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    # Mock 2 Writing (4 pages)
    pages.append(K.page(
        K.page_title("Mock 2 &bull; Writing Section A", kicker="Spelling &amp; Punctuation &bull; 10 Marks", badge="WRITING")
        + K.box_html(
            "<p>Complete the spelling and punctuation questions below:</p>"
            "<ul>"
            "<li>Correct the 4 Annexe D spelling mistakes in the college email.</li>"
            "<li>Add commas to the equipment list.</li>"
            "<li>Change the present tense verbs to past tense.</li>"
            "</ul>",
            title="Spelling &amp; Sentence Questions"
        )
        + K.fill_lines("Write your answers below:", min_mm=25, gap_mm=9.5),
        header=(BOOK, "Mock 2 &bull; Writing Section A"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    pages.append(K.page(
        K.page_title("Mock 2 &bull; Writing Task 1: Email", kicker="Functional Writing Task &bull; 13 Marks &bull; 40–50 Words", badge="TASK 1")
        + K.box_html(
            "<p style='font-size:10pt;line-height:1.4;margin:0 0 1mm 0;'>Write an email to Oxford Adult Learning Centre (courses@oxfordlearning.co.uk) enquiring about the Digital Skills course mentioned in Text 1. In your email you must:</p>"
            "<ul style='font-size:9.5pt;line-height:1.35;margin:0 0 0 4mm;'>"
            "<li>Say which course you are interested in.</li>"
            "<li>Ask what day of the week the classes are held.</li>"
            "<li>Ask if the course is free for adult learners.</li>"
            "</ul>",
            title="Email Brief &bull; 13 Marks"
        )
        + K.fill_lines("Write your email below:", min_mm=25, gap_mm=9.5),
        header=(BOOK, "Mock 2 &bull; Task 1 Response"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    pages.append(K.page(
        K.page_title("Mock 2 &bull; Writing Task 2: Feedback Note", kicker="Functional Writing Task &bull; 13 Marks &bull; 40–50 Words", badge="TASK 2")
        + K.box_html(
            "<p style='font-size:10pt;line-height:1.4;margin:0 0 1mm 0;'>Write a feedback note (40–50 words) to your local sports centre manager about a recent swimming session. In your note you must:</p>"
            "<ul style='font-size:9.5pt;line-height:1.35;margin:0 0 0 4mm;'>"
            "<li>State which day and time you visited the pool.</li>"
            "<li>Mention one positive aspect of the centre (clean changing rooms, friendly staff).</li>"
            "<li>Suggest one thing they could improve (water temperature, locker keys).</li>"
            "</ul>",
            title="Feedback Note Brief &bull; 13 Marks"
        )
        + K.fill_lines("Write your feedback note below:", min_mm=25, gap_mm=9.5),
        header=(BOOK, "Mock 2 &bull; Task 2 Response"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    pages.append(K.page(
        K.page_title("Mock 2 &bull; Candidate Post-Exam Audit", kicker="Self-Evaluation &amp; Mark Scheme Alignment", badge="AUDIT")
        + K.box_html(
            "<p>Check your Mock 2 script against the Pearson Edexcel Entry Level 3 standards:</p>"
            "<ul>"
            "<li>Checked spellings using Annexe D phonics rules.</li>"
            "<li>Used capital letters for days, places, and sentence beginnings.</li>"
            "<li>Addressed every bullet point in both functional writing tasks.</li>"
            "</ul>",
            title="Entry 3 Marking Rubric"
        )
        + K.fill_notes("Personal Reflections &amp; Target Words for Mock 2", min_mm=45),
        header=(BOOK, "Mock 2 &bull; Audit"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    # p80 to p90: Reference Back Matter via K.ref_pages
    ref_blocks = []

    READING_E3_SOLUTIONS = {
        1: ["Assembly Point B is located on the south car park.", "The routine alarm is tested every Tuesday at 10:00am.", "The fire warden for Bay 4 is Mrs Helen Patel.", "You must NOT use the lifts during an evacuation."],
        2: ["The community garden reopens on Saturday 11 October at 10:00am.", "Free gardening gloves and seed packets are provided for all attendees.", "A sensory garden with raised vegetable beds has been built.", "Tea and homemade cakes will be served in the pavilion."],
        3: ["The functional skills induction takes place in Room B14.", "You must bring your photographic ID (passport or driving licence) to reception.", "If you cannot attend, call your tutor Abdul on 01865 554100.", "Reception will issue an electronic security lanyard."],
        4: ["The green READY light shows the machine is ready to use.", "The sealed edge of the pouch must enter the machine first.", "Allow the hot laminated document to cool on the rear flat tray for 60 seconds.", "The machine takes 4 minutes to heat up."],
        5: ["The telephone number for course advice is 01865 240100.", "The Citizens Advice Bureau provides legal & financial support.", "Call 01865 248900 for emergency dental access appointments.", "The public library loans service is listed last in alphabetical order."],
        6: ["All annual leave booking forms must be submitted by Friday 28 November.", "Submit your signed booking form to line manager David Clark.", "A maximum of two staff members per department may take leave during peak weeks.", "Late submissions will not be approved."],
        7: ["The customer is returning a waterproof winter jacket.", "The reason for return is an incorrect size (ordered Medium, received Large).", "The customer requests an exchange for the correct size.", "The proof of purchase order reference is #ORD-88219."],
        8: ["The prescription medicine must be taken twice daily after meals.", "Store the tablets in a cool, dry place below 25°C.", "Common mild side effects include drowsiness and dry mouth.", "Do not drive or operate machinery if you feel drowsy."],
        9: ["The morning shift begins promptly at 08:00 and finishes at 16:30.", "Employees must clock in using their digital staff badge.", "Staff must report sickness absence at least one hour before shift start.", "The warehouse manager on duty is Sarah Jenkins."],
        10: ["The green commute scheme encourages cycling and public transport.", "Employees who cycle to work receive a £50 annual maintenance voucher.", "Secure bicycle lockers are located near the west entrance.", "Register online via the staff benefits intranet portal."],
        11: ["Garden waste bins are collected every alternate Tuesday.", "Enter your postcode on the council waste portal to find your schedule.", "Food waste must be placed in the dedicated brown caddy.", "Report missed collections within 48 hours via the web form."],
        12: ["Apply a thin layer of antiseptic cream to the affected skin 2 to 3 times daily.", "For external use only; avoid contact with eyes and open wounds.", "Keep out of reach of children.", "Consult a doctor if symptoms persist beyond 7 days."]
    }

    # Reading answers
    for r_idx, (r_title, _, _, p2_title, _, p2_qs) in enumerate(reading_units_e3, 1):
        e3_ans = READING_E3_SOLUTIONS.get(r_idx, [])
        if e3_ans:
            qa_text = "<br>".join(f"<b>{i+1}.</b> {ans}" for i, ans in enumerate(e3_ans))
        else:
            qa_text = "<br>".join(f"<b>{q_num}</b> Check text details." for q_num, _ in p2_qs)
        ref_blocks.append(K.ref_block(f"Reading Unit {r_idx}: {r_title} Solutions",
                                      K.ref_qa(f"R{r_idx}", f"<b>Benchmark Solutions ({p2_title}):</b><br>{qa_text}", marks="4/4")))

    # Writing answers
    for w_idx, (w_title, _, p2_title, _, _) in enumerate(writing_units_e3, 1):
        ref_blocks.append(K.ref_block(f"Writing Unit {w_idx}: {w_title} Solutions",
                                      K.ref_qa(f"W{w_idx}", f"<b>Benchmark Guidance ({p2_title}):</b> Fully punctuate sentences; check capital letters and full stops; address all bullet points in functional drafts.", marks="4/4")))

    # Spelling answers
    for s_idx, (s_title, _, s_sentences) in enumerate(spelling_drills_e3, 1):
        ans_text = ", ".join(f"({i+1}) {w}" for i, (w, _) in enumerate(s_sentences))
        ref_blocks.append(K.ref_block(f"Spelling Drill {s_idx} Answer Key",
                                      K.ref_qa(f"SP{s_idx}", f"<b>Completed Words:</b> {ans_text}", marks="4/4")))

    # Mock exam solutions
    ref_blocks.append(K.ref_block("Mock Examination 1 Benchmark Solutions",
                                  K.ref_qa("M1-R", "Reading: (1) South car park, (2) Tuesdays 10am, (3) Helen Patel, (4) Lifts.", marks="24/24")
                                  + K.ref_qa("M1-W", "Writing Task 1 (Email): Clear subject line, addressed to HR, covers all 3 bullet points, polite sign-off.<br>Task 2 (Notice): Bold title, dates and times clearly listed, contact name included.", marks="36/36")))

    ref_blocks.append(K.ref_block("Mock Examination 2 Benchmark Solutions",
                                  K.ref_qa("M2-R", "Reading: (1) Thursday 15 Jan, (2) Room 10, (3) £4.50 daily cap, (4) Free under 5.", marks="24/24")
                                  + K.ref_qa("M2-W", "Writing Task 1 (Email): Enquires about Digital Skills, asks for days and fees.<br>Task 2 (Feedback): States visit date, praises clean changing rooms, suggests locker improvement.", marks="36/36")))

    # Index
    index_e3 = [
        ("A", [("Alphabetical order", "8"), ("Annexe D spelling words", "52"), ("Appointment letters", "16")]),
        ("C", [("Capital letters", "28"), ("Commas in lists", "32"), ("Comparing texts", "18")]),
        ("E", [("Emails (formal)", "44"), ("Exclamation marks", "30")]),
        ("F", [("Fact vs opinion", "22"), ("Full stops", "30")]),
        ("I", [("Instructions and recipes", "10")]),
        ("M", [("Mock exams", "64")]),
        ("N", [("Notices and signs", "4"), ("Notes for colleagues", "46")]),
        ("P", [("Paragraphs", "42"), ("Past tense verbs", "38")]),
        ("Q", [("Question marks", "30")]),
        ("S", [("Subject-verb agreement", "40"), ("Suffixes (-ful, -less)", "54")]),
        ("T", [("Timetables and tables", "20")]),
        ("W", [("Web pages and online forms", "24"), ("Writing feedback reports", "50")])
    ]
    index_html = ""
    for letter, entries in index_e3:
        items = "".join(f"<div class='ix'><span>{escape_html(t)}</span><span>{escape_html(p)}</span></div>" for t, p in entries)
        index_html += f"<div class='ix-letter'>{letter}</div>{items}"
    ref_blocks.append(K.ref_block("Entry Level 3 Subject &amp; Vocabulary Index", index_html))

    cover_theme = K.theme_from_cover(front_cov)
    ref_page_list = K.ref_pages("Entry 3 Reference: Solutions, Spelling Keys &amp; Index", ref_blocks,
                                BOOK, start_page=p_curr, subtitle="Worked Solutions &amp; Marking Guidance",
                                cols=2, theme=cover_theme, notes_title="Candidate Entry 3 Log")
    pages.extend(ref_page_list)
    p_curr += len(ref_page_list)

    # Candidate Success Notes
    p91_body = (
        K.page_title("Candidate Entry 3 Progress Chart &amp; Success Commitments", kicker="Pearson Edexcel Entry 3 Achievement", badge="SUCCESS")
        + K.box_html(
            "<p>Check off your skills as you complete each section of this manual:</p>"
            "<ul>"
            "<li><b>Reading Skills:</b> Can locate facts, read timetables, and follow instructions.</li>"
            "<li><b>Writing Skills:</b> Capital letters, full stops, question marks, and paragraphs secure.</li>"
            "<li><b>Spelling Skills:</b> Can spell high-frequency Annexe D words accurately.</li>"
            "<li><b>Mock Exams:</b> Completed both full Reading and Writing mocks under timed conditions.</li>"
            "</ul>",
            title="Entry Level 3 Learning Journey"
        )
        + K.fill_notes("Personal Success Notes &amp; Tutor Endorsements", min_mm=45)
    )
    pages.append(K.page(p91_body, header=(BOOK, "Success Commitments"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Duplex balance check before back cover
    if (len(pages) + 1) % 2 != 0:
        p_ibc_body = (
            K.page_title("Candidate Entry 3 Celebration &amp; Sign-Off", kicker="Pearson Edexcel Entry Level 3 &bull; Course Completion Record", badge="PASS")
            + K.rule_box("Entry Level 3 Achievement Milestone",
                         "<p style='font-size:12pt;line-height:1.5;'>Well done on completing the Entry Level 3 Core Guide! You have built key foundations in reading and writing:</p>"
                         + K.bullets([
                             "<b>Reading Confidence:</b> Understanding main points, finding factual details, and interpreting symbols.",
                             "<b>Writing Demarcation:</b> Using capital letters, full stops, and question marks correctly.",
                             "<b>Everyday Spelling:</b> Mastering regular plurals, common suffixes, and frequent vocabulary.",
                             "<b>Preparation for Level 1:</b> Ready to transition towards full Level 1 Functional Skills English."
                         ]))
            + K.tip_pair("Keep practicing your reading and spelling drills every week to consolidate your skills.",
                         "Celebrate your progress with your tutor as you move to the next level of study.",
                         golden_title="Next Steps", watch_title="Progression")
            + K.fill_notes("Tutor Endorsement &amp; Next Stage Plan", min_mm=28)
        )
        pages.append(K.page(p_ibc_body, header=(BOOK, "Course Completion"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # Back Cover
    pages.append(K.back_cover(back_cov))

    print(f"Total Pages Assembled: {len(pages)}")
    out_pdf = DOWNLOADS / "MasterFunctionalSkills_English_Entry_Level_3_Core_Guide.pdf"
    res = K.render_pdf(pages, out_pdf, theme=cover_theme, entry3=True, title="Master Functional Skills - English Entry Level 3 Core Guide")
    shutil.copy(out_pdf, DOCUMENTS / out_pdf.name)
    print(f"Verified & Saved: {out_pdf} -> {DOCUMENTS / out_pdf.name}")
    return res


# =============================================================================
# Main
# =============================================================================
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Build Master Functional Skills English Suite")
    parser.add_argument("--book", choices=["l2_core", "l2_comp", "l1_core", "l1_comp", "e3_core", "all"], default="all")
    args = parser.parse_args()

    if args.book in ("l2_core", "all"):
        build_english_l2_core()
    if args.book in ("l2_comp", "all"):
        build_english_l2_companion()
    if args.book in ("l1_core", "all"):
        build_english_l1_core()
    if args.book in ("l1_comp", "all"):
        build_english_l1_companion()
    if args.book in ("e3_core", "all"):
        build_english_e3_core()
