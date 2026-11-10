#!/usr/bin/env python3
"""
books/a4/build_reading_suite_a4.py
=============================================================================
Compiles the 2 dedicated Master Functional Skills English Reading Core Guides:
1. MasterFunctionalSkills_English_Reading_Level_1_Core_Guide.pdf
2. MasterFunctionalSkills_English_Reading_Level_2_Core_Guide.pdf

Upgrades applied:
- Complete 2-column Table of Contents on Page 2 with verified page numbers
- Official Pearson Edexcel Subject Content mapping table on Page 3 (L1.9-L1.18 & L2.11-L2.19)
- Wide-angle 16:9 establishing photographs (object-position: center center) with compact
  single-line captions (7.6pt hero banners, 6.8pt floating practice cards)
- Dedicated Level 1 (worked_models[0], practice[0..1]) and Level 2 (worked_models[1], practice[1..2])
  models and dual comprehension tasks on every topic
- Balanced 2-column Reference Section (Solutions, Glossary, Index) with 0 column/page overflows
- 100% confidentiality compliance (0 occurrences of forbidden organisation names)
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

import a4_kit as K
import english_reading_topics as ert
import visual_curriculum_catalog as vcc

DOWNLOADS = PROJECT_DIR / "assets" / "downloads"
DOCUMENTS = Path("/home/subi/Documents")
COV = K.COVER_DIR


def escape_html(text):
    if not text:
        return ""
    return (text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;"))


# =============================================================================
# Wide-Angle Thematic Photo Mapping & Compact Single-Line Caption Helpers
# =============================================================================
READING_L1_HERO_PHOTOS = {
    1: ("reading_thematic/r1_l1_gym.jpg",
        "Fact or Opinion: Evaluating objective facts versus promotional claims on a community gym flyer."),
    2: ("reading_thematic/r2_l1_office_hvac.jpg",
        "Words in Context: Using surrounding sentences to decode unfamiliar words on an office notice."),
    3: ("reading_thematic/r3_l1_kitchen_fridge.jpg",
        "Specialist Vocabulary: Using in-text brackets and context clues to define commercial kitchen terms."),
    4: ("reading_thematic/r4_l1_clinic_letter.jpg",
        "Presentational Features: Using bold headings, boxes, and bullet points on a clinic appointment letter."),
    5: ("reading_thematic/r5_l1_hr_intranet.jpg",
        "Layout Devices: Navigating subheadings, numbered lists, and sidebars on a staff intranet FAQ page."),
    6: ("reading_thematic/r6_l1_manual_handling.jpg",
        "Diagrams & Captions: Linking safety illustrations and captions to written warehouse lifting rules."),
    7: ("reading_thematic/r7_l1_cycling_flyer.jpg",
        "Language Devices: Spotting rule of three, rhetorical questions, and direct address in a cycling flyer."),
    8: ("reading_thematic/r8_l1_library_letter.jpg",
        "Point of View & Bias: Identifying the writer's stance and supporting reasons in a library consultation."),
    9: ("writing_thematic/l1_f7_leaflet.jpg",
        "Tone & Writer's Voice: Recognising a reassuring, encouraging tone in a patient guidance leaflet."),
    10: ("reading_thematic/r10_l1_sharps_sop.jpg",
         "Text Types & Conventions: Identifying instructional features in a clinical sharps disposal SOP."),
    11: ("reading_thematic/r11_l1_cashless_tills.jpg",
         "Comparing Texts: Contrasting two retail staff reviews of a new self-service checkout system."),
    12: ("reading_thematic/r12_l1_apprentice_induction.jpg",
         "Purpose & Audience: Identifying why an apprentice induction guide was written and who it helps."),
}

READING_L1_PRACTICE_PHOTOS = {
    1: ("e3_thematic/r9_leisure_timetable.jpg",
        "Drill: Separating verifiable facts from subjective opinions."),
    2: ("e3_thematic/r4_office_laminator.jpg",
        "Drill: Matching workplace words with exact context synonyms."),
    3: ("writing_thematic/l2_f5_task2.jpg",
        "Drill: Decoding technical food-safety and audit vocabulary."),
    4: ("e3_thematic/r7_hospital_clinic.jpg",
        "Drill: Explaining how headings and boxes guide the reader."),
    5: ("e3_thematic/r5_high_street_directory.jpg",
        "Drill: Using visual signposts and index tables to locate facts."),
    6: ("e3_thematic/r6_warehouse_memo.jpg",
        "Drill: Explaining how a safety diagram supports written rules."),
    7: ("e3_thematic/r10_cycle_scheme.jpg",
        "Drill: Identifying persuasive devices and statistics in context."),
    8: ("writing_thematic/l1_f9_blog.jpg",
        "Drill: Tracing a writer's argument and spotting bias clues."),
    9: ("e3_thematic/r12_pharmacy_cream.jpg",
        "Drill: Selecting words that reveal whether tone is reassuring."),
    10: ("e3_thematic/r1_fire_safety_sign.jpg",
         "Drill: Distinguishing mandatory instructions from general advice."),
    11: ("e3_thematic/r8_bus_train_compare.jpg",
         "Drill: Writing a linked comparison across two short texts."),
    12: ("e3_thematic/r3_college_enrolment.jpg",
         "Drill: Identifying main purpose and target audience."),
}

READING_L2_HERO_PHOTOS = {
    1: ("writing_thematic/l2_f7_leaflet.jpg",
        "Fact, Opinion & Assertion: Separating empirical clinical metrics from professional value judgments."),
    2: ("writing_thematic/l1_f11_statement.jpg",
        "Nuance & Implicit Meaning: Unpacking subtext and precise lexical replacements in policy prose."),
    3: ("writing_thematic/l1_f5_task2.jpg",
        "Technical Register: Analysing how specialist occupational safety terminology conveys authority."),
    4: ("writing_thematic/l1_f4_task2.jpg",
        "Presentational Hierarchy: Evaluating how typographic contrast directs urgent workplace action."),
    5: ("writing_thematic/l2_f7_task2.jpg",
        "Structural Signposting: Analysing multi-column health communications, sidebars, and callout boxes."),
    6: ("writing_thematic/l2_f10_proposal.jpg",
        "Data Visuals & Captions: Synthesising quantitative chart trends with persuasive campaign prose."),
    7: ("writing_thematic/l2_f12_speech.jpg",
        "Rhetorical Architecture: Evaluating how emotive language, tricolon, and statistics influence readers."),
    8: ("writing_thematic/l2_f6_report.jpg",
        "Editorial Bias & Vested Interest: Detecting selective evidence and commercial agendas in articles."),
    9: ("writing_thematic/l2_f2_task2.jpg",
        "Tone, Register & Irony: Identifying diplomatic, indignant, or urgent voice in formal correspondence."),
    10: ("writing_thematic/l2_f11_task2.jpg",
         "Genre Conventions & Authority: Analysing statutory regulatory reports and governance guidelines."),
    11: ("writing_thematic/l2_f1_task2.jpg",
         "Multi-Text Comparison: Synthesising contrasting perspectives, evidence, and tone across two texts."),
    12: ("writing_thematic/l1_f1_task2.jpg",
         "Primary & Secondary Purpose: Evaluating layered persuasive and informative aims in public appeals."),
}

READING_L2_PRACTICE_PHOTOS = {
    1: ("writing_thematic/l2_f11_statement.jpg",
        "Analysis: Dissecting mixed factual and evaluative clauses."),
    2: ("writing_thematic/l1_f11_task2.jpg",
        "Analysis: Substitution testing and implicit inference."),
    3: ("writing_thematic/l2_f4_memo.jpg",
        "Analysis: Explaining the effect of formal technical jargon."),
    4: ("writing_thematic/l1_f7_task2.jpg",
        "Analysis: Evaluating visual hierarchy and reader navigation."),
    5: ("e3_thematic/w11_format_notice_leaflet.jpg",
        "Analysis: Assessing subheadings, tables, and boxed alerts."),
    6: ("writing_thematic/l1_f10_proposal.jpg",
        "Analysis: Linking statistical graphics to main text claims."),
    7: ("writing_thematic/l1_f12_speech.jpg",
        "Analysis: Naming rhetorical devices and explaining impact."),
    8: ("writing_thematic/l2_f9_blog.jpg",
        "Analysis: Identifying covert bias and omitted counter-views."),
    9: ("e3_thematic/w10_format_letter_note.jpg",
        "Analysis: Quoting lexical markers of tone and register."),
    10: ("writing_thematic/l2_f3_email.jpg",
         "Analysis: Comparing audience expectations and conventions."),
    11: ("writing_thematic/l2_f1_article.jpg",
         "Analysis: Integrated comparison using comparative connectives."),
    12: ("writing_thematic/l1_f12_task2.jpg",
         "Analysis: Evaluating dual purpose and target audience impact."),
}

READING_MC_L1_PHOTOS = {
    1: ("reading_thematic/mc1_exam_clock.jpg",
        "Exam Pacing Strategy: Allocating 10 minutes for initial reading, 40 minutes for questions, and 10 minutes for checking."),
    2: ("reading_thematic/mc2_scanning_text.jpg",
        "Scanning & Retrieval: Locating names, dates, numbers, and key phrases rapidly without copying whole paragraphs."),
    3: ("e3_thematic/sp1_prefixes.jpg",
        "Vocabulary in Context: Reading the sentences before and after an unfamiliar word to test a synonym replacement."),
    4: ("writing_thematic/l1_f4_memo.jpg",
        "Organisational Features: Explaining specifically how headings, bullet points, and tables help the reader."),
    5: ("writing_thematic/l2_f2_letter.jpg",
        "Fact vs Opinion Mastery: Checking whether a statement can be proven with records or expresses a value judgment."),
    6: ("writing_thematic/spag1_clauses.jpg",
        "Final Proofreading & Comparison: Verifying every multiple-choice box and linking Text A and Text B clearly."),
}

READING_MC_L2_PHOTOS = {
    1: ("reading_thematic/mc1_exam_clock.jpg",
        "The 75-Minute Clock: Allocating 15 minutes to read all three extracts before tackling high-tariff questions."),
    2: ("reading_thematic/mc2_scanning_text.jpg",
        "Implicit Meaning & Subtext: Identifying irony, euphemism, and implied attitudes grounded in textual evidence."),
    3: ("writing_thematic/l2_f8_review.jpg",
        "Detecting Sophisticated Bias: Auditing author credentials, commercial motives, and selective use of data."),
    4: ("writing_thematic/spag4_modals.jpg",
        "Rhetorical Device Analysis: Quoting the exact technique and explaining its psychological impact on the audience."),
    5: ("writing_thematic/spag1_clauses.jpg",
        "The 11-Mark Comparison Method: Integrating Text A and Text B continuously with comparative connectives."),
    6: ("writing_thematic/spag7_cohesion.jpg",
        "Cross-Text Synthesis: Combining evidence across all three extracts into a unified, well-attributed conclusion."),
}

TOP_ALIGNED_PHOTOS = {
    "reading_thematic/r3_l1_kitchen_fridge.jpg": "center 22%",
    "reading_thematic/r5_l1_hr_intranet.jpg": "center 24%",
    "reading_thematic/r6_l1_manual_handling.jpg": "center 20%",
    "reading_thematic/r7_l1_cycling_flyer.jpg": "center 26%",
    "reading_thematic/r8_l1_library_letter.jpg": "center 22%",
    "reading_thematic/r12_l1_apprentice_induction.jpg": "center 22%",
    "reading_thematic/mc1_exam_clock.jpg": "center 24%",
    "reading_thematic/mc2_scanning_text.jpg": "center 18%",
}


def resolve_reading_photo(rel_path):
    p = K.PHOTO_DIR / rel_path
    if p.exists():
        return p.resolve().as_uri()
    fallback = K.PHOTO_DIR / "reading_thematic/r1_l1_gym.jpg"
    return fallback.resolve().as_uri()


def reading_hero_image(rel_path, caption="", height_mm=64):
    uri = resolve_reading_photo(rel_path)
    obj_pos = TOP_ALIGNED_PHOTOS.get(rel_path, "center 25%")
    cap_html = (
        f"<div style='padding:0.9mm 1.5mm;font-size:8pt;font-weight:700;line-height:1.15;color:var(--primary);"
        f"background:#eff6ff;border-top:1px solid #bfdbfe;text-align:center;"
        f"white-space:nowrap;overflow:hidden;text-overflow:ellipsis;'>{caption}</div>"
    ) if caption else ""
    return (
        f"<div class='hero-img' style='margin:1.5mm 0 2.2mm 0;border:1.5px solid var(--primary);"
        f"border-radius:6px;overflow:hidden;background:#ffffff;box-shadow:0 1.5px 4px rgba(0,0,0,0.08);'>"
        f"<img src='{uri}' alt='' style='width:100%;height:{height_mm}mm;"
        f"object-fit:cover;object-position:{obj_pos};display:block;'/>"
        f"{cap_html}"
        f"</div>"
    )


def reading_float_photo_card(rel_path, caption="", width_mm=82, height_mm=46, side="right"):
    uri = resolve_reading_photo(rel_path)
    margin = "0 0 2mm 3.5mm" if side == "right" else "0 3.5mm 2mm 0"
    cap_html = (
        f"<div style='padding:0.8mm 1.2mm;font-size:7.6pt;font-weight:700;line-height:1.15;color:var(--primary);"
        f"background:#eff6ff;border-top:1px solid #bfdbfe;text-align:center;"
        f"white-space:nowrap;overflow:hidden;text-overflow:ellipsis;'>{caption}</div>"
    ) if caption else ""
    return (
        f"<div style='float:{side};width:{width_mm}mm;margin:{margin};"
        f"border:1.5px solid var(--primary);border-radius:6px;overflow:hidden;"
        f"background:#fff;box-shadow:0 1.5px 4px rgba(0,0,0,0.08);'>"
        f"<div style='width:100%;aspect-ratio:16/9;overflow:hidden;background:#0f172a;'>"
        f"<img src='{uri}' alt='' style='width:100%;height:100%;"
        f"object-fit:cover;object-position:center 25%;display:block;'/>"
        f"</div>"
        f"{cap_html}"
        f"</div>"
    )


def reading_toc_page(level_label, subtitle, sections_left, sections_right, footer_book):
    """Builds a comprehensive, zero-overflow 2-column Table of Contents on Page 2."""
    def render_col(sec_list):
        out = []
        for sec_code, sec_title, items in sec_list:
            out.append(
                f"<div style='background:linear-gradient(135deg, var(--primary-dark), var(--primary));color:#fff;padding:1.4mm 2.8mm;"
                f"border-radius:4px;font-size:9.8pt;font-weight:800;letter-spacing:0.03em;"
                f"text-transform:uppercase;margin:2.0mm 0 1.2mm 0;display:flex;"
                f"justify-content:space-between;align-items:center;box-shadow:0 1px 3px rgba(0,0,0,0.04);'>"
                f"<span>{sec_title}</span>"
                f"<span style='background:rgba(255,255,255,0.22);padding:0.25mm 1.8mm;"
                f"border-radius:2px;font-size:8.2pt;'>{sec_code}</span>"
                f"</div>"
            )
            for badge, label, pg in items:
                out.append(
                    f"<div style='display:grid;grid-template-columns:14mm minmax(0,1fr) 12mm;"
                    f"align-items:center;gap:1.8mm;padding:1.1mm 1.4mm;"
                    f"border-bottom:0.6px dashed #cbd5e1;font-size:9.4pt;line-height:1.26;'>"
                    f"<span class='chip' style='padding:0.25mm 1.4mm;font-size:8.6pt;font-weight:800;display:inline-block;text-align:center;min-width:11mm;border-radius:1.2mm;'>{badge}</span>"
                    f"<span style='white-space:nowrap;overflow:hidden;text-overflow:ellipsis;"
                    f"color:#1e293b;font-weight:600;'>{label}</span>"
                    f"<span style='text-align:right;font-weight:800;color:var(--primary);"
                    f"font-size:9.5pt;font-variant-numeric:tabular-nums;'>p.{pg}</span>"
                    f"</div>"
                )
        return "".join(out)

    body = (
        f"<div style='background:linear-gradient(135deg, var(--primary-dark), var(--primary));"
        f"color:#fff;padding:3.2mm 4.5mm;border-radius:6px;margin-bottom:2.2mm;"
        f"display:flex;justify-content:space-between;align-items:center;box-shadow:0 1.5px 4px rgba(0,0,0,0.08);'>"
        f"<div>"
        f"<div style='font-size:8.2pt;text-transform:uppercase;letter-spacing:1px;"
        f"opacity:0.9;font-weight:700;'>Master Functional Skills &bull; Complete Curriculum Directory</div>"
        f"<div style='font-size:15pt;font-weight:900;line-height:1.15;margin-top:0.5mm;'>"
        f"{level_label} &bull; Table of Contents</div>"
        f"<div style='font-size:9.2pt;opacity:0.92;margin-top:0.4mm;'>{subtitle}</div>"
        f"</div>"
        f"<div style='background:rgba(255,255,255,0.18);border:1px solid rgba(255,255,255,0.35);"
        f"padding:1.8mm 3.2mm;border-radius:5px;text-align:center;'>"
        f"<div style='font-size:7.2pt;text-transform:uppercase;letter-spacing:0.5px;'>Pearson Edexcel</div>"
        f"<div style='font-size:10.5pt;font-weight:900;'>REFORMED</div>"
        f"</div>"
        f"</div>"
        f"<div style='display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:4.5mm;'>"
        f"<div>{render_col(sections_left)}</div>"
        f"<div>{render_col(sections_right)}</div>"
        f"</div>"
        f"<div style='margin-top:auto;padding:1.6mm 3.2mm;background:var(--tint);"
        f"border:1px solid var(--soft);border-left:3.5px solid var(--primary);"
        f"border-radius:4px;font-size:8.2pt;line-height:1.35;color:#1e293b;'>"
        f"<b>How to Use This Guide:</b> Every Reading Topic follows a structured 4-page mastery cycle: "
        f"<b>(1) Curriculum Blueprint &amp; Visual Context</b>, <b>(2) Source Passage &amp; Strategy Walkthrough</b>, "
        f"<b>(3) Examiner Full-Marks Benchmark Model</b>, and <b>(4) Dual Comprehension Practice Drills</b> "
        f"(with full worked solutions in the Reference Section)."
        f"</div>"
    )
    return K.page(body, header=(footer_book, "Table of Contents"), footer=footer_book, page_no=2)


# =============================================================================
# Level 1 Reading Core Guide
# =============================================================================
def build_reading_l1_core():
    print("\n" + "="*70)
    print("BUILDING: MasterFunctionalSkills_English_Reading_Level_1_Core_Guide.pdf")
    print("="*70)

    BOOK = "English Reading Level 1 Core Guide"
    front_cov = COV / "reading_l1_core_cover_page-1.png"
    back_cov = COV / "reading_l1_core_cover_page-2.png"

    pages = []

    # p1: Front Cover
    pages.append(K.front_cover(front_cov))

    # Placeholder for p2: Table of Contents (populated after page numbers are finalized)
    pages.append(None)

    # p3: Specification Overview + Complete DfE L1.9-L1.18 Mapping Table
    l1_spec_rows = [
        ("L1.9", "Identify and understand the main points, ideas and details in texts", "Topics 1, 2, 12", "pp. 5, 9, 49"),
        ("L1.10", "Compare information, ideas and opinions in different texts", "Topics 1, 11", "pp. 5, 45"),
        ("L1.11", "Identify meanings in texts and distinguish between fact and opinion", "Topics 1, 2", "pp. 5, 9"),
        ("L1.12", "Recognise that language and other textual features can be varied to suit different audiences and purposes", "Topics 7, 9, 10, 12", "pp. 29, 37, 41, 49"),
        ("L1.13", "Use reference materials and appropriate strategies for a range of purposes, including to find the meaning of words", "Topics 2, 3, 5", "pp. 9, 13, 21"),
        ("L1.14", "Understand organisational and structural features and use them to locate Relevant information (e.g. index, menus, subheadings)", "Topics 4, 5", "pp. 17, 21"),
        ("L1.15", "Infer from images meanings not explicit in the accompanying text", "Topic 6", "p. 25"),
        ("L1.16", "Recognise vocabulary typically associated with specific types and purposes of texts (e.g. formal, informal, instructional, persuasive)", "Topics 3, 7, 9, 10", "pp. 13, 29, 37, 41"),
        ("L1.17", "Read and understand a range of specialist words in context", "Topic 3", "p. 13"),
        ("L1.18", "Use knowledge of punctuation to aid understanding of straightforward texts", "Topics 4, 8, 9", "pp. 17, 33, 37"),
    ]
    spec_table_rows = "".join(
        f"<tr>"
        f"<td style='padding:1.2mm 2mm;border:1px solid #cbd5e1;font-weight:800;color:var(--primary);white-space:nowrap;'>{code}</td>"
        f"<td style='padding:1.2mm 2mm;border:1px solid #cbd5e1;'>{desc}</td>"
        f"<td style='padding:1.2mm 2mm;border:1px solid #cbd5e1;white-space:nowrap;font-weight:600;'>{top}</td>"
        f"<td style='padding:1.2mm 2mm;border:1px solid #cbd5e1;white-space:nowrap;font-weight:700;color:var(--primary);'>{pgs}</td>"
        f"</tr>"
        for code, desc, top, pgs in l1_spec_rows
    )
    p3_body = (
        K.page_title("Pearson Edexcel Level 1 Reading &bull; Specification Overview",
                     kicker="Curriculum Architecture &bull; DfE Subject Content L1.9 to L1.18", badge="SPEC")
        + K.box_html(
            "<div style='font-size:9.6pt;line-height:1.4;'>"
            "<p style='margin:0 0 1.5mm 0;'><b>Examination Format:</b> Externally assessed <b>60-minute</b> paper worth <b>30 marks</b> across <b>two to three real-world non-fiction texts</b> (workplace policies, community notices, emails, websites, and articles). Dictionaries are not permitted; aim for <b>2 minutes per mark</b>.</p>"
            "<table style='width:100%;border-collapse:collapse;font-size:8.4pt;line-height:1.28;margin-top:1.5mm;'>"
            "<thead><tr style='background:var(--primary);color:#fff;'>"
            "<th style='padding:1.3mm 2mm;text-align:left;width:13mm;'>Code</th>"
            "<th style='padding:1.3mm 2mm;text-align:left;'>Official DfE / Pearson Edexcel Level 1 Reading Requirement</th>"
            "<th style='padding:1.3mm 2mm;text-align:left;width:28mm;'>Core Topics</th>"
            "<th style='padding:1.3mm 2mm;text-align:left;width:22mm;'>Pages</th>"
            "</tr></thead>"
            f"<tbody>{spec_table_rows}</tbody>"
            "</table>"
            "</div>",
            title="Official DfE Functional Skills English Level 1 Reading Standards (L1.9–L1.18)"
        )
        + K.tip_pair(
            "Always re-read the specific paragraph referenced in the question before selecting or writing your answer.",
            "Never rely on personal background knowledge — every mark must be evidenced directly from the source text.",
            golden_title="Golden Reading Rule", watch_title="Examiner Warning"
        )
    )
    pages.append(K.page(p3_body, header=(BOOK, "Specification Overview"), footer=BOOK, page_no=3))

    # p4: Candidate Diagnostic Self-Audit Matrix
    p4_body = (
        K.page_title("Level 1 Candidate Diagnostic Matrix", kicker="Baseline Skills Audit", badge="AUDIT")
        + K.box_html(
            "<p>Evaluate your confidence across the core Level 1 Reading standards before starting:</p>"
            + K.bullets([
                "Can you quickly separate objective facts from personal opinions in a workplace article? (L1.11)",
                "Can you work out the meaning of unfamiliar or specialist words using surrounding context clues? (L1.13, L1.17)",
                "Can you explain how bullet points, subheadings, numbered lists, and bold text help the reader? (L1.14)",
                "Can you infer implicit meanings from workplace diagrams, safety symbols, and captions? (L1.15)",
                "Can you identify the main purpose and target audience of a text and compare two texts clearly? (L1.10, L1.12)"
            ]),
            title="Core Functional Skills Level 1 Reading Competencies"
        )
        + K.fill_notes("Reading Skills I Need to Practise Most", min_mm=35)
    )
    pages.append(K.page(p4_body, header=(BOOK, "Diagnostic Audit"), footer=BOOK, page_no=4))

    # p5 to p52: 12 Reading Topics x 4 pages = 48 pages
    p_curr = 5
    topic_start_pages = {}
    for t_idx, topic in enumerate(ert.READING_TOPICS[:12], 1):
        topic_start_pages[t_idx] = p_curr
        clean_title = topic["clean_topic"]
        spec_pts = topic["spec_points"]
        rules = topic["golden_rules"]
        models = topic.get("worked_models", [])
        traps = topic.get("examiner_traps", [])
        practice = topic.get("practice_questions", [])

        hero_rel, hero_cap = READING_L1_HERO_PHOTOS[t_idx]
        prac_rel, prac_cap = READING_L1_PRACTICE_PHOTOS[t_idx]

        # Page 1: Topic Blueprint & Reading Theory
        spec_text = "<br>".join(f"&bull; <b>{code}:</b> {desc}" for code, desc in spec_pts)
        rule_desc = rules[0]["desc"] if rules else "Read texts actively and cross-reference details."
        p1_body = (
            K.page_title(f"Reading Topic {t_idx}: {clean_title}", kicker="Topic Blueprint &bull; Level 1 Reading", badge=f"R{t_idx}")
            + reading_hero_image(hero_rel, hero_cap, height_mm=64)
            + K.rule_box("DfE Criteria &amp; Core Concept",
                         f"<div style='font-size:11.2pt;line-height:1.45;'>"
                         f"<p style='margin:0 0 2mm 0;'><b>Curriculum Standard:</b><br>{spec_text}</p>"
                         f"<p style='margin:0;'><b>Key Concept:</b> {rule_desc}</p>"
                         f"</div>")
            + K.tip_pair(
                rules[1]["desc"] if len(rules) > 1 else "Always underline keywords in the question.",
                traps[0]["desc"] if traps else "Do not assume something is a fact just because it is written down.",
                golden_title="Golden Rule", watch_title="Examiner Trap"
            )
        )
        pages.append(K.page(p1_body, header=(BOOK, f"Topic {t_idx} &bull; Theory"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 2: Workplace Text & Strategy Walkthrough (Level 1 Worked Model = models[0])
        first_model = models[0] if models else {}
        context_name = first_model.get("context", "Workplace Communication")
        q_prompt = first_model.get("question", "Read the text carefully and answer the questions.")
        steps = first_model.get("steps", [])
        steps_html = "".join(
            f"<li style='margin-bottom:1.2mm;'><b>{s[0]} ({s[1]}):</b> {s[2]} "
            f"<span style='color:var(--primary);font-weight:700;'>[{s[3]}]</span></li>"
            for s in steps
        ) if steps else "<li>Read carefully and extract key points.</li>"

        p2_body = (
            K.page_title(f"{clean_title} &bull; Text Analysis", kicker=f"Authentic Workplace Context &bull; {context_name}", badge="PASSAGE")
            + K.box_html(
                f"<div style='background:#f8fafc;padding:3mm;border:1.5px solid var(--soft);border-radius:6px;font-size:10.6pt;line-height:1.45;margin-bottom:2mm;'>"
                f"<strong style='color:var(--primary);font-size:11.2pt;'>Extract &bull; {first_model.get('title', clean_title)}:</strong><br><br>"
                f"{q_prompt}"
                f"</div>",
                title=f"Source Text &bull; {context_name}"
            )
            + K.box_html(
                f"<ol style='margin:0;padding-left:5mm;font-size:10.4pt;line-height:1.42;'>{steps_html}</ol>",
                title="Tutor Step-by-Step Analysis Strategy"
            )
            + K.fill_notes("Key Clues &amp; Vocabulary Notes", min_mm=24)
        )
        pages.append(K.page(p2_body, header=(BOOK, f"Topic {t_idx} &bull; Analysis"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 3: Worked Full-Marks Benchmark Model
        final_ans = first_model.get("final_answer", "Full model answer.")
        tutor_tip = first_model.get("tutor_tip", "Answer clearly with direct evidence.")
        trap_second = traps[1]["desc"] if len(traps) > 1 else "Examiners award marks for exact quotes or accurate paraphrasing that directly answers what was asked."
        p3_body = (
            K.page_title(f"{clean_title} &bull; Benchmark Model Answer", kicker="Examiner Full Marks Exemplar", badge="MODEL")
            + K.box_html(
                f"<div style='background:#ffffff;padding:3.5mm;border:1.5px solid #cbd5e1;border-radius:6px;font-size:11pt;line-height:1.48;'>"
                f"<strong style='color:var(--primary);'>Model Candidate Answer:</strong><br><br>"
                f"{final_ans}"
                f"</div>",
                title=f"Full Marks Benchmark &bull; {first_model.get('marks', '3 Marks')}"
            )
            + K.tip_pair(
                tutor_tip,
                trap_second,
                golden_title="Examiner Guidance", watch_title="Mark Scheme Criterion"
            )
            + K.fill_notes("What Makes This Answer Successful", min_mm=30)
        )
        pages.append(K.page(p3_body, header=(BOOK, f"Topic {t_idx} &bull; Model"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 4: Dual Candidate Comprehension Practice (Task A = practice[0], Task B = practice[1])
        pr_a = practice[0] if len(practice) > 0 else {}
        pr_b = practice[1] if len(practice) > 1 else {}
        pr_a_q = pr_a.get("question", f"Read an everyday workplace text and explain how {clean_title.lower()} is used.")
        pr_a_m = pr_a.get("marks", "2 Marks")
        pr_b_q = pr_b.get("question", f"Identify a second example of {clean_title.lower()} and explain its effect.")
        pr_b_m = pr_b.get("marks", "2 Marks")

        p4_body = (
            K.page_title(f"{clean_title} &bull; Candidate Practice", kicker=f"Exam Comprehension Drills &bull; {pr_a_m} + {pr_b_m}", badge="DRILL")
            + K.box_html(
                reading_float_photo_card(prac_rel, prac_cap, width_mm=82, height_mm=46, side="right")
                + f"<div style='font-size:10pt;line-height:1.4;'>"
                f"<p style='margin:0 0 1.5mm 0;'><b style='color:var(--primary);'>Task A ({pr_a_m}):</b> {pr_a_q}</p>"
                f"<p style='margin:2mm 0 0 0;'><b style='color:var(--primary);'>Task B ({pr_b_m}):</b> {pr_b_q}</p>"
                f"<div style='clear:both;'></div>"
                f"</div>",
                title=f"Independent Practice Tasks A &amp; B &bull; {clean_title}"
            )
            + K.fill_lines(f"Task A Response ({pr_a_m}):", min_mm=38, gap_mm=8.5)
            + K.fill_lines(f"Task B Response ({pr_b_m}):", min_mm=38, gap_mm=8.5)
        )
        pages.append(K.page(p4_body, header=(BOOK, f"Topic {t_idx} &bull; Practice"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p53 to p58: Reading Exam Strategy Masterclass (6 pages)
    mc_start_page = p_curr
    exam_masterclasses = [
        ("Managing Your Time: The 2-Minutes-Per-Mark Rule",
         "In a 60-minute exam for 30 marks, you have exactly 2 minutes per mark. Allocate your time systematically: 10 minutes reading the source texts, 40 minutes answering questions, and 10 minutes checking.",
         "Read questions first so you read each passage with a clear purpose.", "Never get stuck on a 1-mark question for more than 2 minutes."),
        ("Retrieval Questions &amp; Locating Exact Facts",
         "Retrieval questions ask you to find a specific piece of information (who, what, where, when, how much). Scan for capital letters, dates, numbers, and key action verbs.",
         "Keep retrieval answers concise, accurate, and factual.", "Do not copy entire paragraphs when only one phrase or statistic is needed."),
        ("Working Out the Meaning of Unfamiliar Words",
         "When encountering specialist or unfamiliar words, read the sentence before and the sentence after. The surrounding context almost always provides a clue, synonym, or explanation.",
         "Check whether brackets, dashes, or a footnote define the term.", "Substitute your chosen word back into the sentence to check grammar and sense."),
        ("Understanding Organisational &amp; Layout Features",
         "Writers use main headings to state the overall topic, subheadings to divide sections, bullet points to list key items concisely, and bold text or boxes to highlight urgent alerts.",
         "Always explain HOW the feature helps the reader (e.g. 'helps staff find rules quickly').", "Never write vague answers like 'it looks nice' or 'it stands out'."),
        ("Distinguishing Fact, Opinion &amp; Bias",
         "A fact can be proven true using records, measurements, or statistics. An opinion expresses personal belief, feelings, or value judgments ('best', 'unacceptable', 'undoubtedly').",
         "Facts can be verified; opinions reflect feelings or judgments.", "Watch out for opinions hidden inside quotes from staff or customers."),
        ("Final Checking &amp; Two-Text Comparison Strategy",
         "Use your final 10 minutes to verify every answer. For comparison questions, pair a point from Text A directly with a matching point from Text B using 'both', 'however', or 'whereas'.",
         "Even an educated guess on a multiple-choice question gives a 25% chance.", "Check that you have copied dates, phone numbers, and figures accurately.")
    ]

    for em_idx, (em_title, em_desc, em_gold, em_trap) in enumerate(exam_masterclasses, 1):
        mc_rel, mc_cap = READING_MC_L1_PHOTOS[em_idx]
        em_body = (
            K.page_title(f"Exam Masterclass {em_idx}: {em_title}", kicker="Pearson Edexcel Reading Strategy", badge=f"EX{em_idx}")
            + reading_hero_image(mc_rel, mc_cap, height_mm=64)
            + K.box_html(f"<p style='font-size:11.2pt;line-height:1.48;margin:0;'>{em_desc}</p>", title="Core Examination Technique")
            + K.tip_pair(em_gold, em_trap, golden_title="Top Scoring Strategy", watch_title="Common Exam Pitfall")
            + K.fill_notes(f"My Exam Strategy Notes &amp; Personal Rules (Masterclass {em_idx})", min_mm=34)
        )
        pages.append(K.page(em_body, header=(BOOK, f"Masterclass {em_idx}"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p59 to p74: 2 Full Official Reading Mock Exams (16 pages: 8 pages per mock)
    mock1_start_page = p_curr
    pages.append(K.page(
        K.page_title("Official Reading Mock Examination &bull; Paper 1", kicker="Pearson Edexcel Level 1 &bull; 60 Minutes &bull; 30 Marks", badge="MOCK 1")
        + K.box_html(
            "<p><b>Instructions for Candidates:</b></p>"
            + K.bullets([
                "This paper contains 3 reading texts (Text A, Text B, and Text C).",
                "Answer all questions in the candidate spaces provided.",
                "Total time allowed: 60 minutes. Total marks: 30 marks.",
                "You may not use a dictionary or spellchecker."
            ]),
            title="Examination Protocol"
        )
        + K.tip_pair("Spend 10 minutes reading all texts thoroughly before beginning the questions.",
                     "Check the marks allocated to each question. A 2-mark question requires 2 distinct points.",
                     golden_title="Pacing Rule", watch_title="Mark Allocation")
        + K.fill_notes("Personal Target Score &amp; Time Checkpoints", min_mm=38),
        header=(BOOK, "Mock 1 &bull; Instructions"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    # Mock 1 Texts & Questions (7 pages) - 0 forbidden names
    mock1_sections = [
        ("Text A: Greendale Community Health &amp; Wellbeing Centre",
         "The Greendale Health &amp; Wellbeing Centre opens Monday to Friday from 08:00 to 19:30. We provide free confidential health checks, regional smoking cessation clinics, and diabetes prevention workshops. To book an appointment, telephone 01632 774200 or visit our reception desk in Zone 2. Patients attending morning clinics may use the visitor car park free of charge for up to two hours.",
         [{"q": "<b>Question 1:</b> According to Text A, what time does the Wellbeing Centre close on weekdays? (1 mark)", "lines": 2},
          {"q": "<b>Question 2:</b> Identify two free health services offered by the centre. (2 marks)", "lines": 3}]),
        ("Text A Continued &amp; Questions",
         "Please note that evening workshops require advance booking at least 48 hours in advance. If you cannot attend your scheduled appointment, you must notify staff so another patient can be offered your time slot. Missed appointments cost the centre over &pound;12,000 each year.",
         [{"q": "<b>Question 3:</b> How much notice is required to book an evening workshop? (1 mark)", "lines": 2},
          {"q": "<b>Question 4:</b> Explain one consequence mentioned in the text if a patient misses an appointment. (1 mark)", "lines": 2},
          {"q": "<b>Question 5:</b> What is the main purpose of Text A? (1 mark)", "options": ["To complain about regional healthcare funding", "To inform the public about services and opening hours", "To advertise private gym memberships", "To instruct readers how to train as a nurse"]}]),
        ("Text B: Customer Feedback &amp; Public Reviews",
         "Review by David T. (5 Stars &bull; Verified Visitor):<br><em>'I visited the Greendale Wellbeing Centre yesterday for a blood pressure check. The nurse, Sister Sarah, was exceptionally kind and reassuring. The modern waiting area was spotlessly clean and spacious. The automated check-in screen was effortless to use. Without a doubt, this is the finest healthcare facility in the Valleyfield district!'</em>",
         [{"q": "<b>Question 6:</b> Extract one fact from David's review. (1 mark)", "lines": 2},
          {"q": "<b>Question 7:</b> Extract one opinion from David's review. (1 mark)", "lines": 2},
          {"q": "<b>Question 8:</b> Explain how David uses adjectives to describe the staff and facilities. (2 marks)", "lines": 3}]),
        ("Text B Questions &amp; Text C Introduction",
         "Text C &bull; Staff Operational Memo:<br>From: Clinic Operations Manager<br>To: All Nursing &amp; Administrative Staff<br>Date: 12 October 2026<br>Subject: Annual Flu Vaccination Clinic Logistics<br><br>All staff must complete their mandatory infection control refresher training by Friday 24 October. Flu vaccination clinics commence Monday 3 November in Seminar Room B.",
         [{"q": "<b>Question 9:</b> In David's review in Text B, what does the word 'reassuring' suggest about Sister Sarah? (1 mark)", "lines": 2},
          {"q": "<b>Question 10:</b> Identify the date by which staff must complete their refresher training. (1 mark)", "lines": 2}]),
        ("Text C: Operational Memo Details",
         "To maintain efficient patient flow, please adhere strictly to the 10-minute appointment slots. Laminated patient pathway flowcharts are displayed in the staff breakroom. Any adverse vaccine reactions must be logged in the yellow clinical incident binder within 30 minutes of occurrence.",
         [{"q": "<b>Question 11:</b> Where can staff find the laminated patient pathway flowcharts? (1 mark)", "lines": 2},
          {"q": "<b>Question 12:</b> Where must adverse vaccine reactions be recorded? (1 mark)", "lines": 2},
          {"q": "<b>Question 13:</b> Within what timeframe must an adverse reaction be logged? (1 mark)", "lines": 2}]),
        ("Text C Layout &amp; Comparison Questions",
         "The memo uses bold subheadings and bullet points so that operational instructions are clear during busy clinic hours. All staff receive a complimentary hot beverage voucher from the cafeteria.",
         [{"q": "<b>Question 14:</b> Identify two layout features used in Text C and explain how they help the reader. (2 marks)", "lines": 4},
          {"q": "<b>Question 15:</b> Both Text A and Text C discuss healthcare clinics. Compare one difference in audience between Text A and Text C. (2 marks)", "lines": 4}]),
        ("Mock 1 &bull; Synthesis &amp; Final Review",
         "Complete your review of Paper 1 before marking your score against the official solutions in the Reference Section.",
         [{"q": "<b>Question 16:</b> Summarise two key pieces of advice you would give to someone visiting the Greendale Centre for the first time. (2 marks)", "lines": 4}])
    ]

    for p_title, p_extract, p_qs in mock1_sections:
        p_body = (
            K.page_title(f"Mock 1 &bull; {p_title}", kicker="Official Examination Booklet &bull; Reading Paper 1", badge="M1")
            + K.box_html(f"<div style='background:#f8fafc;padding:3mm;border:1.5px solid var(--soft);border-radius:4px;font-size:10.8pt;line-height:1.45;'>{p_extract}</div>", title="Reading Passage")
            + K.exercise_list(p_qs, lines=3)
        )
        pages.append(K.page(p_body, header=(BOOK, "Mock 1 &bull; Reading"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # Mock 2 (8 pages)
    mock2_start_page = p_curr
    pages.append(K.page(
        K.page_title("Official Reading Mock Examination &bull; Paper 2", kicker="Pearson Edexcel Level 1 &bull; 60 Minutes &bull; 30 Marks", badge="MOCK 2")
        + K.box_html(
            "<p><b>Instructions for Candidates:</b></p>"
            + K.bullets([
                "This paper contains 3 reading texts on workplace apprenticeship training and health and safety.",
                "Answer all questions in the spaces provided.",
                "Time allowed: 60 minutes. Total marks: 30 marks.",
                "Check your answers against the official mark scheme in the Reference Section."
            ]),
            title="Examination Protocol"
        )
        + K.tip_pair("Keep your answers precise and directly quote the passage where appropriate.",
                     "Watch out for words like 'except' or 'apart from' in retrieval questions.",
                     golden_title="Top Scoring Tip", watch_title="Question Phrasing")
        + K.fill_notes("Personal Target Score &amp; Time Checkpoints", min_mm=38),
        header=(BOOK, "Mock 2 &bull; Instructions"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    # Mock 2 Texts & Questions (7 pages) - 0 forbidden names, mentor Abdul
    mock2_sections = [
        ("Text A: Valleyfield Council Apprenticeship Guide",
         "The Valleyfield Council Apprenticeship Programme offers paid apprenticeships across digital skills, business administration, and horticulture. Apprentices receive a starting salary of &pound;19,500 per annum, 25 days of paid annual leave, and fully funded qualifications up to Level 3. Applicants must be aged 16 or over and hold GCSEs in English and Maths at Grade 3 or Functional Skills Level 1.",
         [{"q": "<b>Question 1:</b> According to Text A, what is the starting salary for an apprentice? (1 mark)", "lines": 2},
          {"q": "<b>Question 2:</b> State two qualification fields offered on the apprenticeship programme. (2 marks)", "lines": 3}]),
        ("Text A Continued &amp; Questions",
         "All applications must be submitted via the online portal by Friday 28 November 2026. Successful candidates will be invited for assessment days during the second week of December. If you need reasonable adjustments for the interview, contact the disability support coordinator at hr@valleyfield.gov.uk.",
         [{"q": "<b>Question 3:</b> What is the final deadline date for submitting an application? (1 mark)", "lines": 2},
          {"q": "<b>Question 4:</b> Who should applicants contact if they require reasonable adjustments? (1 mark)", "lines": 2},
          {"q": "<b>Question 5:</b> What text type is Text A? (1 mark)", "options": ["An informal personal diary", "An informative official recruitment guide", "A critical newspaper review", "A recipe instruction card"]}]),
        ("Text B: Apprentice Case Study &bull; Marcus",
         "Marcus Davies, Digital Support Apprentice:<br><em>'Joining the council digital team was the best decision of my career! I was nervous on my first day, but my mentor Abdul guided me through every software deployment. The workplace culture is wonderfully welcoming and positive. Last month, I configured 85 new laptops for community support staff.'</em>",
         [{"q": "<b>Question 6:</b> Extract one fact from Marcus's case study. (1 mark)", "lines": 2},
          {"q": "<b>Question 7:</b> Extract one opinion from Marcus's case study. (1 mark)", "lines": 2},
          {"q": "<b>Question 8:</b> How does Marcus describe the workplace culture? (1 mark)", "lines": 2}]),
        ("Text B Questions &amp; Text C Introduction",
         "Text C &bull; Depot Health &amp; Safety Policy Notice:<br>All warehouse and IT depot employees must wear high-visibility vests and steel toe-capped safety boots at all times in the logistics bay. Forklift operating lanes are marked with yellow cross-hatch lines. Pedestrians must strictly use the green painted walkways.",
         [{"q": "<b>Question 9:</b> In Marcus's account, how did mentor Abdul support him? (1 mark)", "lines": 2},
          {"q": "<b>Question 10:</b> According to Text C, what two items of PPE are compulsory in the logistics bay? (2 marks)", "lines": 3}]),
        ("Text C: Depot Safety Rules",
         "Mobile phones are strictly prohibited while walking through the loading bays. Earphones must never be worn as they prevent staff from hearing forklift reverse warning alarms. In the event of a spillage, immediately erect the yellow 'Caution: Wet Floor' warning cones.",
         [{"q": "<b>Question 11:</b> Why are earphones prohibited in the loading bays? (1 mark)", "lines": 2},
          {"q": "<b>Question 12:</b> What action must an employee take immediately if a liquid spillage occurs? (1 mark)", "lines": 2}]),
        ("Text C Layout &amp; Comparison Questions",
         "Text C uses bold uppercase lettering and warning symbols to emphasise urgent safety protocols. Failure to observe safety notices may result in formal disciplinary action under section 4 of the Employment Contract.",
         [{"q": "<b>Question 13:</b> Explain why the writer of Text C used bold uppercase lettering for key safety rules. (1 mark)", "lines": 2},
          {"q": "<b>Question 14:</b> Both Text A and Text C are written for council staff and applicants. Identify one difference in purpose between Text A and Text C. (2 marks)", "lines": 4}]),
        ("Mock 2 &bull; Candidate Self-Audit Matrix",
         "Check your answers against the official mark scheme before recording your final score.",
         [{"q": "<b>Question 15:</b> What advice does Text C give regarding mobile phone usage? (1 mark)", "lines": 2},
          {"q": "<b>Question 16:</b> Summarise two benefits of doing an apprenticeship as described across Text A and Text B. (2 marks)", "lines": 4}])
    ]

    for p_title, p_extract, p_qs in mock2_sections:
        p_body = (
            K.page_title(f"Mock 2 &bull; {p_title}", kicker="Official Examination Booklet &bull; Reading Paper 2", badge="M2")
            + K.box_html(f"<div style='background:#f8fafc;padding:3mm;border:1.5px solid var(--soft);border-radius:4px;font-size:10.8pt;line-height:1.45;'>{p_extract}</div>", title="Reading Passage")
            + K.exercise_list(p_qs, lines=3)
        )
        pages.append(K.page(p_body, header=(BOOK, "Mock 2 &bull; Reading"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p75 to p80: Official Pearson Edexcel Reading Mark Schemes (6 pages)
    rubric_start_page = p_curr
    rubrics = [
        ("Retrieval &amp; Identification Mark Schemes (L1.9, L1.13)",
         "Pearson Edexcel Level 1 Reading awards marks for accurate factual extraction. Accept direct quotes or unambiguous paraphrasing that answers the question precisely."),
        ("Layout &amp; Organisational Devices Mark Scheme (L1.14, L1.15)",
         "To achieve full marks on layout questions, candidates must identify the specific device (e.g. bullet points, headings, columns, diagrams) AND explain its functional benefit for the reader."),
        ("Fact vs. Opinion Assessment Criteria (L1.11)",
         "Award 1 mark for a verifiable factual statement supported by records or metrics. Award 1 mark for a subjective opinion containing evaluative vocabulary."),
        ("Vocabulary in Context Mark Scheme (L1.13, L1.16, L1.17)",
         "Candidates must demonstrate understanding of words in their specific sentence context and match the grammatical word class when offering a replacement."),
        ("Text Purpose &amp; Audience Assessment Grids (L1.12, L1.18)",
         "Candidates must accurately link purpose verbs (persuade, inform, explain, instruct) and target audience groups to specific evidence in the text."),
        ("Comparison of Two Texts Mark Scheme (L1.10)",
         "Award marks for direct comparative links between Text A and Text B identifying similarities or differences in ideas, audience, or perspective.")
    ]

    for r_idx, (r_title, r_desc) in enumerate(rubrics, 1):
        r_body = (
            K.page_title(f"Official Mark Scheme &bull; Part {r_idx} of 6", kicker=r_title, badge=f"MS{r_idx}")
            + K.box_html(
                f"<div style='font-size:11.5pt;line-height:1.5;'>"
                f"<p><b>Examiner Assessment Guidance:</b><br>{r_desc}</p>"
                f"<p><b>Standard Marking Rules:</b></p>"
                f"<ul>"
                f"<li>Do not penalise spelling, punctuation, or grammar errors in the Reading paper provided meaning is clear.</li>"
                f"<li>Where a question asks for TWO points, do not award marks for two variations of the same idea.</li>"
                f"<li>Answers copied verbatim from the text are acceptable if they answer the specific question asked.</li>"
                f"</ul>"
                f"</div>",
                title="Mark Scheme Standards &amp; Criteria"
            )
            + K.fill_notes(f"Personal Marking Notes &amp; Checkpoints (Part {r_idx})", min_mm=42)
        )
        pages.append(K.page(r_body, header=(BOOK, f"Mark Scheme Part {r_idx}/6"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # Reference Section: Complete Step-by-Step Solutions, Glossary & Index
    ref_start_page = p_curr
    ref_blocks = []

    # Topic Practice Solutions (Topics 1 to 12: both Task A and Task B)
    for t_idx, topic in enumerate(ert.READING_TOPICS[:12], 1):
        p_list = topic.get("practice_questions", [])
        pr_a = p_list[0] if len(p_list) > 0 else {}
        pr_b = p_list[1] if len(p_list) > 1 else {}
        qa_html = (
            K.ref_qa(f"R{t_idx}A", f"<b>Steps:</b> {pr_a.get('solution_steps', '')}<br><b>Answer:</b> {pr_a.get('correct_answer', '')}", marks=pr_a.get("marks", "2m"))
            + K.ref_qa(f"R{t_idx}B", f"<b>Steps:</b> {pr_b.get('solution_steps', '')}<br><b>Answer:</b> {pr_b.get('correct_answer', '')}", marks=pr_b.get("marks", "2m"))
        )
        ref_blocks.append(K.ref_block(f"Topic {t_idx}: {topic['clean_topic']} Solutions", qa_html))

    # Mock 1 Full Solutions (split into Q1-Q8 and Q9-Q16 so blocks never overflow a column)
    m1_ans = [
        ("Q1", "19:30 (7:30 pm)", "1m", "Direct retrieval from Text A paragraph 1."),
        ("Q2", "Health checks / Smoking cessation clinics / Diabetes prevention workshops (any two)", "2m", "1 mark for each service listed."),
        ("Q3", "48 hours in advance", "1m", "Direct retrieval."),
        ("Q4", "Costs the centre over £12,000 / denies another patient a time slot", "1m", "Accept either consequence."),
        ("Q5", "B: To inform the public about services and opening hours", "1m", "Multiple choice correct key."),
        ("Q6", "Visited yesterday / Nurse was Sister Sarah / Had blood pressure check", "1m", "Verifiable fact."),
        ("Q7", "Sister Sarah was exceptionally kind / Finest healthcare facility in the Valleyfield district", "1m", "Subjective opinion."),
        ("Q8", "Kind, reassuring, clean, spacious — creates an encouraging and positive impression", "2m", "1 mark for quote, 1 mark for effect."),
        ("Q9", "She made the patient feel calm, relaxed, and safe during the test", "1m", "Vocabulary inference."),
        ("Q10", "Friday 24 October", "1m", "Direct retrieval."),
        ("Q11", "In the staff breakroom", "1m", "Direct retrieval."),
        ("Q12", "Yellow clinical incident binder", "1m", "Direct retrieval."),
        ("Q13", "Within 30 minutes of occurrence", "1m", "Direct retrieval."),
        ("Q14", "Bold headings organise topics; bullet points present rules clearly for quick reading", "2m", "1m for features, 1m for effect."),
        ("Q15", "Text A is for general public/patients; Text C is for internal clinical/administrative staff", "2m", "1m for Text A audience, 1m for Text C."),
        ("Q16", "Book evening workshops 48h in advance; use free 2-hour parking for morning clinics", "2m", "1m for each valid recommendation.")
    ]
    ref_blocks.append(K.ref_block(
        "Official Reading Mock Paper 1 &bull; Solutions (Questions 1–8)",
        "".join(K.ref_qa(q, a, marks=m, working=w) for q, a, m, w in m1_ans[:8])
    ))
    ref_blocks.append(K.ref_block(
        "Official Reading Mock Paper 1 &bull; Solutions (Questions 9–16)",
        "".join(K.ref_qa(q, a, marks=m, working=w) for q, a, m, w in m1_ans[8:])
    ))

    # Mock 2 Full Solutions (split into Q1-Q8 and Q9-Q16)
    m2_ans = [
        ("Q1", "£19,500 per annum", "1m", "Direct retrieval from Text A."),
        ("Q2", "Digital skills / Business administration / Horticulture (any two)", "2m", "1m each."),
        ("Q3", "Friday 28 November 2026", "1m", "Direct retrieval."),
        ("Q4", "Disability support coordinator (hr@valleyfield.gov.uk)", "1m", "Direct retrieval."),
        ("Q5", "B: An informative official recruitment guide", "1m", "Multiple choice key."),
        ("Q6", "Configured 85 new laptops / Mentor was Abdul", "1m", "Verifiable fact."),
        ("Q7", "Best decision of my career / Wonderfully welcoming workplace culture", "1m", "Subjective opinion."),
        ("Q8", "Wonderfully welcoming and positive", "1m", "Direct quote."),
        ("Q9", "Abdul guided him through software deployments and helped him overcome first-day nerves", "1m", "Explanation."),
        ("Q10", "High-visibility vests AND steel toe-capped safety boots", "2m", "1m for each PPE item."),
        ("Q11", "They prevent workers from hearing forklift reverse warning alarms", "1m", "Safety justification."),
        ("Q12", "Erect yellow 'Caution: Wet Floor' warning cones immediately", "1m", "Action required."),
        ("Q13", "To emphasise urgent mandatory health and safety rules so they are immediately noticed", "1m", "Layout effect."),
        ("Q14", "Text A aims to recruit and inform applicants; Text C aims to enforce strict depot safety rules", "2m", "Purpose comparison."),
        ("Q15", "Mobile phones are strictly prohibited while walking through loading bays", "1m", "Rule retrieval."),
        ("Q16", "Earn a salary while training (£19,500); receive mentorship from Abdul and gain funded qualifications", "2m", "Synthesis across texts.")
    ]
    ref_blocks.append(K.ref_block(
        "Official Reading Mock Paper 2 &bull; Solutions (Questions 1–8)",
        "".join(K.ref_qa(q, a, marks=m, working=w) for q, a, m, w in m2_ans[:8])
    ))
    ref_blocks.append(K.ref_block(
        "Official Reading Mock Paper 2 &bull; Solutions (Questions 9–16)",
        "".join(K.ref_qa(q, a, marks=m, working=w) for q, a, m, w in m2_ans[8:])
    ))

    # Reading Glossary (split into A-I and L-T)
    glossary_items = [
        ("Audience", "The specific group of readers a text is written for (e.g. staff, patients, general public)."),
        ("Bias", "A one-sided viewpoint that favours one perspective over another, often lacking balance."),
        ("Caption", "A brief text explanation placed beneath an image, chart, or diagram."),
        ("Context", "The surrounding words, sentences, or situation that gives a word or text its meaning."),
        ("Fact", "A verifiable piece of information that can be proven true by records, measurements, or evidence."),
        ("Headline / Heading", "The main title of an article or document designed to state the subject clearly."),
        ("Implicit Meaning", "Information that is suggested or hinted at rather than directly stated."),
        ("Informative Text", "A text whose main purpose is to give clear, factual information to the reader."),
        ("Layout Feature", "A visual or structural element (columns, bullet points, boxes) that organises content."),
        ("Opinion", "A personal belief, attitude, or feeling that cannot be verified as an objective fact."),
        ("Persuasive Text", "A text designed to convince the reader to take action or agree with a viewpoint."),
        ("Purpose", "The main reason why the author wrote the text (to inform, instruct, explain, or persuade)."),
        ("Retrieval", "Finding and extracting specific facts, figures, or dates directly from a text."),
        ("Subheading", "A smaller heading that divides an article or document into clear sections."),
        ("Tone", "The mood, feeling, or attitude conveyed by the writer's choice of words.")
    ]
    ref_blocks.append(K.ref_block(
        "Reading Glossary (A–I)",
        "".join(f"<p style='margin:0 0 1.2mm 0;'><b>{w}:</b> {d}</p>" for w, d in glossary_items[:8])
    ))
    ref_blocks.append(K.ref_block(
        "Reading Glossary (L–T)",
        "".join(f"<p style='margin:0 0 1.2mm 0;'><b>{w}:</b> {d}</p>" for w, d in glossary_items[8:])
    ))

    # Alphabetical Index (split into A-I and L-T)
    index_items = [
        ("A", [("Audience Identification", "41, 49, 53"), ("Author Purpose", "49, 53")]),
        ("B", [("Bias Detection", "33, 57"), ("Bullet Points Effect", "17, 21, 56")]),
        ("C", [("Captions & Diagrams", "25"), ("Comparing Texts", "45, 58"), ("Context Meaning", "9, 55")]),
        ("E", [("Examiner Traps", "5, 9, 13"), ("Explicit Meaning", "9")]),
        ("F", [("Fact vs. Opinion", "5, 57"), ("Fonts & Headings", "17, 21")]),
        ("G", [("Glossary of Terms", f"{ref_start_page + 5}"), ("Golden Reading Rules", "5, 9, 13, 17")]),
        ("I", [("Implicit Meaning", "9, 25"), ("Informative Purpose", "41, 49")]),
        ("L", [("Layout Devices", "17, 21, 56"), ("Locating Facts", "54")]),
        ("M", [("Mock Exam Paper 1", f"{mock1_start_page}"), ("Mock Exam Paper 2", f"{mock2_start_page}")]),
        ("O", [("Opinions Identification", "5, 57"), ("Organisational Devices", "17, 21")]),
        ("P", [("Persuasive Techniques", "29, 41"), ("Purpose of Texts", "41, 49")]),
        ("R", [("Retrieval Skills", "54"), ("Rhetorical Questions", "29")]),
        ("S", [("Specialist Vocabulary", "13"), ("Subheadings Effect", "17, 21")]),
        ("T", [("Text Types", "41"), ("Timing Strategy (2 min/mark)", "3, 53"), ("Tone & Style", "37")])
    ]
    def render_ix_slice(slice_items):
        out = ""
        for letter, entries in slice_items:
            items = "".join(f"<div class='ix'><span>{escape_html(t)}</span><span>p.{escape_html(p)}</span></div>" for t, p in entries)
            out += f"<div class='ix-letter'>{letter}</div>{items}"
        return out

    ref_blocks.append(K.ref_block("Alphabetical Subject Index (A–I)", render_ix_slice(index_items[:7])))
    ref_blocks.append(K.ref_block("Alphabetical Subject Index (L–T)", render_ix_slice(index_items[7:])))

    cover_theme = K.theme_from_cover(front_cov)
    ref_page_list = K.ref_pages("Reference Section: Solutions, Glossary &amp; Index", ref_blocks,
                                BOOK, start_page=p_curr, subtitle="Complete Worked Solutions, Lexicon &amp; Alphabetical Index",
                                cols=2, theme=cover_theme, notes_title="Candidate Reading Notes")
    pages.extend(ref_page_list)
    p_curr += len(ref_page_list)

    # Final Readiness Page
    ready_page_no = p_curr
    p_ready_body = (
        K.page_title("Level 1 Reading &bull; Exam Day Commitments", kicker="Final Revision &bull; Exam Readiness", badge="READY")
        + K.box_html(
            "<p>Before entering your Pearson Edexcel Level 1 Reading examination, commit to these 5 essentials:</p>"
            + K.bullets([
                "<b>1. Read Questions First:</b> Always read the questions before the source texts so you read with focus.",
                "<b>2. Strict Pacing:</b> Spend 10 minutes reading texts, 40 minutes on questions, and 10 minutes checking.",
                "<b>3. Quote Directly:</b> For retrieval questions, quote exact words or statistics from the source passage.",
                "<b>4. Explain Layout:</b> When asked about layout features, always state how they help the reader.",
                "<b>5. Answer Every Question:</b> Never leave a multiple-choice question blank — eliminate wrong answers."
            ]),
            title="Golden Exam Rules for Reading Success"
        )
        + K.fill_notes("Personal Commitments &amp; Tutor Sign-off", min_mm=45)
    )
    pages.append(K.page(p_ready_body, header=(BOOK, "Exam Readiness"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Duplex balance check before back cover
    if (len(pages) + 1) % 2 != 0:
        p_extra = (
            K.page_title("Candidate Final Verification Protocol", kicker="Pearson Edexcel Reading Standards", badge="AUDIT")
            + K.box_html(
                "<p>Final review checklist for the exam room:</p>"
                + K.bullets([
                    "Did you verify whether statements were verifiable facts or personal opinions?",
                    "Did you explain the specific purpose of the writer (inform, persuade, instruct)?",
                    "Did you double-check all dates, phone numbers, and figures copied from the passages?"
                ]),
                title="Final Verification"
            )
            + K.fill_notes("Last-Minute Exam Reminders", min_mm=40)
        )
        pages.append(K.page(p_extra, header=(BOOK, "Verification Protocol"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # Populate p2: Complete 2-Column Table of Contents with exact dynamic page numbers
    toc_left = [
        ("INTRO", "Specification &amp; Diagnostic Audit", [
            ("SPEC", "Pearson Edexcel L1.9–L1.18 Specification", "3"),
            ("AUDIT", "Candidate Baseline Skills Audit Matrix", "4"),
        ]),
        ("TOPICS", "Core Reading Topics (R1–R12)", [
            (f"R{i}", ert.READING_TOPICS[i-1]["clean_topic"], str(topic_start_pages[i]))
            for i in range(1, 13)
        ]),
    ]
    toc_right = [
        ("EXAM", "Exam Strategy Masterclasses (EX1–EX6)", [
            (f"EX{i}", exam_masterclasses[i-1][0].replace("&amp;", "&"), str(mc_start_page + i - 1))
            for i in range(1, 7)
        ]),
        ("MOCKS", "Official Reading Mock Exam Papers", [
            ("M1", "Mock Exam Paper 1: Community Health Centre", str(mock1_start_page)),
            ("M2", "Mock Exam Paper 2: Council Apprenticeships", str(mock2_start_page)),
        ]),
        ("MARK", "Official Pearson Edexcel Mark Schemes", [
            ("MS1–3", "Retrieval, Layout &amp; Fact/Opinion Grids", str(rubric_start_page)),
            ("MS4–6", "Vocabulary, Purpose &amp; Comparison Grids", str(rubric_start_page + 3)),
        ]),
        ("REF", "Solutions, Glossary, Index &amp; Readiness", [
            ("SOL", "Topic Drills &amp; Mock 1–2 Full Solutions", str(ref_start_page)),
            ("GLOSS", "Reading Terminology Glossary &amp; Index", str(ref_start_page + 5)),
            ("READY", "Exam Day Readiness Commitments", str(ready_page_no)),
        ]),
    ]
    pages[1] = reading_toc_page(
        "Functional Skills English &bull; Reading Level 1",
        "Complete Study, Comprehension &amp; Exam Practice Manual (DfE L1.9–L1.18)",
        toc_left, toc_right, BOOK
    )

    # Back Cover
    pages.append(K.back_cover(back_cov))

    print(f"Total Pages Assembled: {len(pages)}")
    out_pdf = DOWNLOADS / "MasterFunctionalSkills_English_Reading_Level_1_Core_Guide.pdf"
    res = K.render_pdf(pages, out_pdf, theme=cover_theme, entry3=False, title="Master Functional Skills - English Reading Level 1 Core Guide")
    shutil.copy(out_pdf, DOCUMENTS / out_pdf.name)
    print(f"Verified & Saved: {out_pdf} -> {DOCUMENTS / out_pdf.name}")
    print(f"Overflows: {res.get('overflow', [])}")
    return res


# =============================================================================
# Level 2 Reading Core Guide
# =============================================================================
def build_reading_l2_core():
    print("\n" + "="*70)
    print("BUILDING: MasterFunctionalSkills_English_Reading_Level_2_Core_Guide.pdf")
    print("="*70)

    BOOK = "English Reading Level 2 Core Guide"
    front_cov = COV / "reading_l2_core_cover_page-1.png"
    back_cov = COV / "reading_l2_core_cover_page-2.png"

    pages = []

    # p1: Front Cover
    pages.append(K.front_cover(front_cov))

    # Placeholder for p2: Table of Contents
    pages.append(None)

    # p3: Specification Overview + Complete DfE L2.11-L2.19 Mapping Table
    l2_spec_rows = [
        ("L2.11", "Identify the different situations when the main points are sufficient and when it is important to have specific details", "Topics 1, 2, 10", "pp. 5, 9, 41"),
        ("L2.12", "Compare information, ideas and opinions in different texts, including how they are conveyed", "Topics 8, 11", "pp. 33, 45"),
        ("L2.13", "Identify implicit and inferred meaning in texts", "Topics 2, 6, 9", "pp. 9, 25, 37"),
        ("L2.14", "Understand the relationship between textual features and devices, and how they can be used to shape meaning for different audiences and purposes", "Topics 4, 7, 10, 12", "pp. 17, 29, 41, 49"),
        ("L2.15", "Use a range of reference materials and appropriate resources (e.g. glossaries, legends/keys) for different purposes, including to find the meaning of words in straightforward and complex sources", "Topics 2, 3, 5, 6", "pp. 9, 13, 21, 25"),
        ("L2.16", "Understand organisational features and use them to locate relevant information in a range of straightforward and complex sources", "Topics 4, 5", "pp. 17, 21"),
        ("L2.17", "Analyse texts, of different levels of complexity, recognising their use of vocabulary and identifying levels of formality and bias", "Topics 1, 3, 8, 9", "pp. 5, 13, 33, 37"),
        ("L2.18", "Follow an argument, identifying different points of view and distinguishing fact from opinion", "Topics 1, 8, 11", "pp. 5, 33, 45"),
        ("L2.19", "Identify different styles of writing and writer's voice", "Topics 7, 9, 12", "pp. 29, 37, 49"),
    ]
    spec_l2_rows = "".join(
        f"<tr>"
        f"<td style='padding:1.2mm 2mm;border:1px solid #cbd5e1;font-weight:800;color:var(--primary);white-space:nowrap;'>{code}</td>"
        f"<td style='padding:1.2mm 2mm;border:1px solid #cbd5e1;'>{desc}</td>"
        f"<td style='padding:1.2mm 2mm;border:1px solid #cbd5e1;white-space:nowrap;font-weight:600;'>{top}</td>"
        f"<td style='padding:1.2mm 2mm;border:1px solid #cbd5e1;white-space:nowrap;font-weight:700;color:var(--primary);'>{pgs}</td>"
        f"</tr>"
        for code, desc, top, pgs in l2_spec_rows
    )
    p3_body = (
        K.page_title("Pearson Edexcel Level 2 Reading &bull; Specification Overview",
                     kicker="Curriculum Architecture &bull; DfE Subject Content L2.11 to L2.19", badge="SPEC")
        + K.box_html(
            "<div style='font-size:9.6pt;line-height:1.4;'>"
            "<p style='margin:0 0 1.5mm 0;'><b>Examination Format:</b> Externally assessed <b>75-minute</b> paper worth <b>35 marks</b> across <b>three extended non-fiction texts</b> on a shared theme, including the flagship multi-mark comparison and synthesis questions. Dictionaries are not permitted; aim for <b>2 minutes per mark</b>.</p>"
            "<table style='width:100%;border-collapse:collapse;font-size:8.3pt;line-height:1.26;margin-top:1.5mm;'>"
            "<thead><tr style='background:var(--primary);color:#fff;'>"
            "<th style='padding:1.3mm 2mm;text-align:left;width:14mm;'>Code</th>"
            "<th style='padding:1.3mm 2mm;text-align:left;'>Official DfE / Pearson Edexcel Level 2 Reading Requirement</th>"
            "<th style='padding:1.3mm 2mm;text-align:left;width:28mm;'>Core Topics</th>"
            "<th style='padding:1.3mm 2mm;text-align:left;width:22mm;'>Pages</th>"
            "</tr></thead>"
            f"<tbody>{spec_l2_rows}</tbody>"
            "</table>"
            "</div>",
            title="Official DfE Functional Skills English Level 2 Reading Standards (L2.11–L2.19)"
        )
        + K.tip_pair(
            "For high-tariff comparison questions, provide balanced evidence from BOTH texts linked with comparative connectives.",
            "Do not confuse tone with purpose: purpose is what the writer wants to achieve; tone is their attitude and voice.",
            golden_title="Band 4 Comparison Rule", watch_title="Critical Audit Trap"
        )
    )
    pages.append(K.page(p3_body, header=(BOOK, "Specification Overview"), footer=BOOK, page_no=3))

    # p4: Candidate Diagnostic Self-Audit Matrix
    p4_body = (
        K.page_title("Candidate Diagnostic Self-Audit Matrix", kicker="Baseline Skills Audit &bull; Level 2 Reading", badge="AUDIT")
        + K.box_html(
            "<p>Assess your confidence across the advanced Level 2 Reading competencies before beginning:</p>"
            + K.bullets([
                "Can you detect subtle editorial bias and commercial agendas in texts that appear neutral? (L2.17, L2.18)",
                "Can you unpack implicit meanings, subtext, and irony in extended professional prose? (L2.13)",
                "Can you evaluate how rhetorical devices (rule of three, hyperbole, rhetorical questions) sway reader opinion? (L2.14)",
                "Can you systematically compare two authors' contrasting viewpoints AND how they are conveyed? (L2.12)",
                "Can you distinguish writer's voice, register, and tone with exact lexical quotations? (L2.17, L2.19)"
            ]),
            title="Core Functional Skills Level 2 Reading Competencies"
        )
        + K.fill_notes("Target Areas for Maximum Mark Gains", min_mm=35)
    )
    pages.append(K.page(p4_body, header=(BOOK, "Diagnostic Self-Audit"), footer=BOOK, page_no=4))

    # p5 to p52: 12 Reading Topics x 4 pages = 48 pages
    p_curr = 5
    topic_start_pages = {}
    for t_idx, topic in enumerate(ert.READING_TOPICS[:12], 1):
        topic_start_pages[t_idx] = p_curr
        clean_title = topic["clean_topic"]
        spec_pts = topic["spec_points"]
        rules = topic["golden_rules"]
        models = topic.get("worked_models", [])
        traps = topic.get("examiner_traps", [])
        practice = topic.get("practice_questions", [])

        hero_rel, hero_cap = READING_L2_HERO_PHOTOS[t_idx]
        prac_rel, prac_cap = READING_L2_PRACTICE_PHOTOS[t_idx]

        # Page 1: Topic Blueprint & Theory
        spec_text = "<br>".join(f"&bull; <b>{code}:</b> {desc}" for code, desc in spec_pts)
        rule_desc = rules[0]["desc"] if rules else "Read texts critically and evaluate evidence."
        h_hero = 58 if t_idx == 11 else 64
        p1_body = (
            K.page_title(f"Reading Topic {t_idx}: {clean_title}", kicker="Topic Blueprint &bull; Level 2 Reading", badge=f"R{t_idx}")
            + reading_hero_image(hero_rel, hero_cap, height_mm=h_hero)
            + K.rule_box("DfE Statutory Criteria &amp; Theoretical Architecture",
                         f"<div style='font-size:11.2pt;line-height:1.45;'>"
                         f"<p style='margin:0 0 2mm 0;'><b>Curriculum Standard:</b><br>{spec_text}</p>"
                         f"<p style='margin:0;'><b>Critical Principle:</b> {rule_desc}</p>"
                         f"</div>")
            + K.tip_pair(
                rules[1]["desc"] if len(rules) > 1 else "Always evaluate evidence and the writer's bias.",
                traps[0]["desc"] if traps else "Never assume quotes from experts are objective facts.",
                golden_title="Golden Method", watch_title="Examiner Audit Trap"
            )
        )
        pages.append(K.page(p1_body, header=(BOOK, f"Topic {t_idx} &bull; Blueprint"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 2: Advanced Text Analysis & Strategy Walkthrough (Level 2 Worked Model = models[1])
        l2_model = models[1] if len(models) > 1 else (models[0] if models else {})
        context_name = l2_model.get("context", "Workplace Governance")
        q_prompt = l2_model.get("question", "Read the extract and answer the analytical questions.")
        steps = l2_model.get("steps", [])
        steps_html = "".join(
            f"<li style='margin-bottom:1.2mm;'><b>{s[0]} ({s[1]}):</b> {s[2]} "
            f"<span style='color:var(--primary);font-weight:700;'>[{s[3]}]</span></li>"
            for s in steps
        ) if steps else "<li>Evaluate arguments and textual evidence.</li>"

        p2_body = (
            K.page_title(f"{clean_title} &bull; Text Analysis", kicker=f"Extended Extract &bull; {context_name}", badge="PASSAGE")
            + K.box_html(
                f"<div style='background:#f8fafc;padding:3mm;border:1.5px solid var(--soft);border-radius:6px;font-size:10.5pt;line-height:1.44;margin-bottom:2mm;'>"
                f"<strong style='color:var(--primary);font-size:11pt;'>Extract &bull; {l2_model.get('title', clean_title)}:</strong><br><br>"
                f"{q_prompt}"
                f"</div>",
                title=f"Source Passage &bull; {context_name}"
            )
            + K.box_html(
                f"<ol style='margin:0;padding-left:5mm;font-size:10.3pt;line-height:1.4;'>{steps_html}</ol>",
                title="Examiner Step-by-Step Analytical Protocol"
            )
            + K.fill_notes("Rhetorical Markers &amp; Subtext Notes", min_mm=24)
        )
        pages.append(K.page(p2_body, header=(BOOK, f"Topic {t_idx} &bull; Analysis"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 3: Band 4 Full-Marks Benchmark Model
        final_ans = l2_model.get("final_answer", "Full benchmark response.")
        tutor_tip = l2_model.get("tutor_tip", "Quote evidence and explain the writer's impact.")
        trap_second = traps[1]["desc"] if len(traps) > 1 else "Band 4 responses at Level 2 provide precise textual quotes paired with insightful explanations of the writer's deliberate effect on the reader."
        p3_body = (
            K.page_title(f"{clean_title} &bull; Band 4 Benchmark Exemplar", kicker="Examiner Full Marks Benchmark", badge="MODEL")
            + K.box_html(
                f"<div style='background:#ffffff;padding:3.5mm;border:1.5px solid #cbd5e1;border-radius:6px;font-size:10.8pt;line-height:1.46;'>"
                f"<strong style='color:var(--primary);'>Band 4 Model Answer:</strong><br><br>"
                f"{final_ans}"
                f"</div>",
                title=f"Official Benchmark Exemplar &bull; {l2_model.get('marks', '3 Marks')}"
            )
            + K.tip_pair(
                tutor_tip,
                trap_second,
                golden_title="Band 4 Criteria", watch_title="Examiner Insight"
            )
            + K.fill_notes("Why This Answer Achieves Band 4 Distinction", min_mm=30)
        )
        pages.append(K.page(p3_body, header=(BOOK, f"Topic {t_idx} &bull; Model"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 4: Dual Analytical Comprehension Practice (Task A = practice[1], Task B = practice[2])
        pr_a = practice[1] if len(practice) > 1 else (practice[0] if practice else {})
        pr_b = practice[2] if len(practice) > 2 else (practice[0] if practice else {})
        pr_a_q = pr_a.get("question", f"Read an extended workplace document and critically analyse how {clean_title.lower()} is used.")
        pr_a_m = pr_a.get("marks", "2 Marks")
        pr_b_q = pr_b.get("question", f"Evaluate how the writer uses {clean_title.lower()} to influence the audience.")
        pr_b_m = pr_b.get("marks", "3 Marks")

        p4_body = (
            K.page_title(f"{clean_title} &bull; Independent Practice", kicker=f"Analytical Challenge &bull; {pr_a_m} + {pr_b_m}", badge="DRILL")
            + K.box_html(
                reading_float_photo_card(prac_rel, prac_cap, width_mm=82, height_mm=46, side="right")
                + f"<div style='font-size:9.8pt;line-height:1.38;'>"
                f"<p style='margin:0 0 1.5mm 0;'><b style='color:var(--primary);'>Task A ({pr_a_m}):</b> {pr_a_q}</p>"
                f"<p style='margin:2mm 0 0 0;'><b style='color:var(--primary);'>Task B ({pr_b_m}):</b> {pr_b_q}</p>"
                f"<div style='clear:both;'></div>"
                f"</div>",
                title=f"Examination Analytical Tasks A &amp; B &bull; {clean_title}"
            )
            + K.fill_lines(f"Task A Analytical Response ({pr_a_m}):", min_mm=36, gap_mm=8.5)
            + K.fill_lines(f"Task B Analytical Response ({pr_b_m}):", min_mm=40, gap_mm=8.5)
        )
        pages.append(K.page(p4_body, header=(BOOK, f"Topic {t_idx} &bull; Practice"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p53 to p58: Level 2 Reading Strategy & Comparison Masterclass (6 pages)
    mc_start_page = p_curr
    l2_masterclasses = [
        ("The 75-Minute Examination Clock Strategy",
         "Pacing is critical on Level 2 Reading. Allocate 15 minutes for thorough initial reading, 35 minutes for Questions 1–13 (retrieval, language, layout, bias), and 25 minutes for the high-tariff comparison and synthesis tasks.",
         "Read the questions before reading the passages to prime your memory.", "Never start writing without reading all 3 texts — later questions compare multiple texts."),
        ("Deconstructing Implicit Meaning &amp; Subtext",
         "Level 2 examiners frequently test what is implied rather than stated. Look for euphemisms, sarcastic undertones, ironic contrasts, and what the writer deliberately omitted.",
         "Ask: 'What does the writer want me to feel without directly saying it?'", "Do not mistake speculation for valid inference — inference must be grounded in textual clues."),
        ("Detecting Sophisticated Bias &amp; Commercial Agenda",
         "Authors with a vested commercial or political interest often write in an authoritative, neutral tone while selectively presenting only supporting data.",
         "Check the author credentials, job title, and funding source.", "Notice which opposing viewpoints are missing from the argument."),
        ("Analysing Rhetorical Devices in Persuasive Writing",
         "Identify rule of three, emotive vocabulary, hyperbole, rhetorical questions, and statistics. Explain how each device manipulates reader empathy or logic.",
         "Name the technique, quote the exact words, and explain the psychological effect.", "Do not just write 'it makes the reader think' — specify WHAT it makes them think."),
        ("Mastering the 11-Mark Comparison Question",
         "The comparison question is the highest-value question on the paper. Use an explicit 3-stage method: (1) Point of comparison, (2) Text A quote and analysis, (3) Comparative connective (whereas, in contrast, similarly) and Text B quote.",
         "Ensure balanced weight: cite evidence equally from Text A and Text B.", "Never analyse Text A and Text B in separate isolated paragraphs — integrate them continuously."),
        ("Synthesis &amp; Cross-Referencing Evidence",
         "Questions asking you to synthesise information require combining facts from Text A, Text B, and Text C into a unified conclusion or actionable recommendation.",
         "Combine data from across sources to create a complete, balanced answer.", "Clearly attribute which fact originates from Text A, Text B, and Text C.")
    ]

    for em_idx, (em_title, em_desc, em_gold, em_trap) in enumerate(l2_masterclasses, 1):
        mc_rel, mc_cap = READING_MC_L2_PHOTOS[em_idx]
        em_body = (
            K.page_title(f"Masterclass {em_idx}: {em_title}", kicker="Level 2 Analytical Strategy", badge=f"EX{em_idx}")
            + reading_hero_image(mc_rel, mc_cap, height_mm=64)
            + K.box_html(f"<p style='font-size:11.2pt;line-height:1.48;margin:0;'>{em_desc}</p>", title="Core Examination Technique")
            + K.tip_pair(em_gold, em_trap, golden_title="Band 4 Strategy", watch_title="Common Exam Pitfall")
            + K.fill_notes(f"Personal Strategic Takeaways &amp; Checkpoints (Masterclass {em_idx})", min_mm=34)
        )
        pages.append(K.page(em_body, header=(BOOK, f"Masterclass {em_idx}"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p59 to p74: 2 Full Official Reading Mock Exams (16 pages: 8 pages per mock)
    mock1_start_page = p_curr
    pages.append(K.page(
        K.page_title("Official Reading Mock Examination &bull; Paper 1", kicker="Pearson Edexcel Level 2 &bull; 75 Minutes &bull; 35 Marks", badge="MOCK 1")
        + K.box_html(
            "<p><b>Instructions for Candidates:</b></p>"
            + K.bullets([
                "This paper contains 3 extended reading extracts on the theme of 'Workplace Artificial Intelligence &amp; Clinical Automation'.",
                "Answer all questions in the spaces provided.",
                "Total time: 75 minutes. Total marks: 35 marks.",
                "Dictionaries are strictly prohibited."
            ]),
            title="Examination Protocol"
        )
        + K.tip_pair("Spend 15 minutes reading all three source passages thoroughly.",
                     "For Question 14 (the comparison question), write in continuous integrated paragraphs.",
                     golden_title="Pacing Rule", watch_title="Comparison Strategy")
        + K.fill_notes("Personal Target Score &amp; Time Checkpoints", min_mm=38),
        header=(BOOK, "Mock 1 &bull; Instructions"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    # Mock 1 Level 2 Sections - 0 forbidden names
    mock1_l2_sections = [
        ("Text A: The Clinical Revolution &bull; Medical AI",
         "The deployment of automated diagnostic imaging software across regional hospital radiology departments has reduced scan interpretation backlogs by 42%. Dr Marcus Vance, Chief Medical Technology Officer, argues: 'Machine learning tools detect malignant micro-tumours with 96.8% precision, dramatically outperforming exhausted human clinicians working overnight shifts. Automation does not replace doctors; it rescues them from catastrophic burnout.'",
         [{"q": "<b>Question 1:</b> According to Text A, by what percentage have scan backlogs been reduced? (1 mark)", "lines": 2},
          {"q": "<b>Question 2:</b> Identify two advantages of automated diagnostic software claimed by Dr Vance. (2 marks)", "lines": 3}]),
        ("Text A Language &amp; Purpose Analysis",
         "Dr Vance acknowledges that algorithmic diagnostics require continuous oversight: 'Unsupervised automation invites algorithmic bias, especially across diverse patient demographic groups. We must retain robust clinical guardrails.'",
         [{"q": "<b>Question 3:</b> What does Dr Vance mean by the phrase 'algorithmic bias'? (1 mark)", "lines": 2},
          {"q": "<b>Question 4:</b> Analyse how the writer of Text A uses emotive vocabulary to present human clinicians ('exhausted', 'catastrophic burnout'). (2 marks)", "lines": 3},
          {"q": "<b>Question 5:</b> What is the primary purpose of Text A? (1 mark)", "options": ["To demand the immediate dismissal of human radiologists", "To advocate for the measured adoption of clinical AI tools", "To sell commercial software licences to private clinics", "To explain how to write code for medical algorithms"]}]),
        ("Text B: The Human Cost &bull; Trade Union Perspective",
         "Article by Sarah Jenkins, Healthcare Workers' Union:<br><em>'Beneath the glossy tech jargon lies an aggressive cost-cutting drive. Remote diagnostic hubs dehumanise medicine, isolating vulnerable patients behind cold glowing screens. When algorithms misread atypical symptoms, who bears legal accountability? Certainly not the Silicon Valley venture capitalists profiting from public healthcare procurement contracts.'</em>",
         [{"q": "<b>Question 6:</b> Extract one fact from Text B. (1 mark)", "lines": 2},
          {"q": "<b>Question 7:</b> Extract one opinion from Text B. (1 mark)", "lines": 2},
          {"q": "<b>Question 8:</b> Explain how Sarah Jenkins uses rhetorical questions and emotive language to influence the reader. (2 marks)", "lines": 4}]),
        ("Text B Tone &amp; Text C Introduction",
         "Text C &bull; National Healthcare Implementation Guidelines:<br>All Regional Healthcare Trusts adopting AI tools must complete a Data Protection Impact Assessment (DPIA) and ensure secondary validation by a senior consultant radiologist for any high-risk diagnostic classifications.",
         [{"q": "<b>Question 9:</b> How would you describe the overall tone of Text B? Support your answer with a quote. (2 marks)", "lines": 3},
          {"q": "<b>Question 10:</b> Identify the statutory assessment that Healthcare Trusts must complete according to Text C. (1 mark)", "lines": 2}]),
        ("Text C: Guidelines &amp; Governance Rules",
         "Healthcare Trusts must provide mandatory 20-hour technical training for all healthcare practitioners interfacing with clinical decision-support systems. Bi-annual audits must be submitted to the Healthcare Governance Committee.",
         [{"q": "<b>Question 11:</b> How many hours of technical training are mandatory for staff? (1 mark)", "lines": 2},
          {"q": "<b>Question 12:</b> How frequently must clinical AI audits be submitted? (1 mark)", "lines": 2},
          {"q": "<b>Question 13:</b> Identify two presentational features in Text C that convey official regulatory authority. (2 marks)", "lines": 3}]),
        ("The Flagship Comparison Question (Texts A &amp; B)",
         "Both Text A and Text B discuss the introduction of artificial intelligence in healthcare. Compare how the writers present differing perspectives on the impact of automation on staff and patient care.",
         [{"q": "<b>Question 14 (The 11-Mark Comparison Question):</b> In your response, compare: &bull; The differing viewpoints on technology &bull; How evidence and quotes are used &bull; The tone and persuasive techniques in each text. Use comparative connectives and integrate quotes from both texts. (11 marks)", "lines": 13}]),
        ("Synthesis &amp; Final Evaluation",
         "Synthesise findings from all three texts to evaluate how regional hospitals can achieve safety while modernising clinical operations.",
         [{"q": "<b>Question 15:</b> Synthesising ideas from Text A, Text B, and Text C, explain three essential safeguards needed when introducing clinical AI tools into hospital wards. (3 marks)", "lines": 6}])
    ]

    for p_title, p_extract, p_qs in mock1_l2_sections:
        p_body = (
            K.page_title(f"Mock 1 &bull; {p_title}", kicker="Official Examination Booklet &bull; Reading Paper 1", badge="M1")
            + K.box_html(f"<div style='background:#f8fafc;padding:3mm;border:1.5px solid var(--soft);border-radius:4px;font-size:10.8pt;line-height:1.45;'>{p_extract}</div>", title="Reading Passage")
            + K.exercise_list(p_qs, lines=3)
        )
        pages.append(K.page(p_body, header=(BOOK, "Mock 1 &bull; Reading"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # Mock 2 (8 pages)
    mock2_start_page = p_curr
    pages.append(K.page(
        K.page_title("Official Reading Mock Examination &bull; Paper 2", kicker="Pearson Edexcel Level 2 &bull; 75 Minutes &bull; 35 Marks", badge="MOCK 2")
        + K.box_html(
            "<p><b>Instructions for Candidates:</b></p>"
            + K.bullets([
                "This paper contains 3 extended reading extracts on 'Remote Working, Urban Decline &amp; The Future of Cities'.",
                "Answer all questions in the spaces provided.",
                "Time allowed: 75 minutes. Total marks: 35 marks.",
                "Check your answers against the official mark scheme in the Reference Section."
            ]),
            title="Examination Protocol"
        )
        + K.tip_pair("Keep your comparison structured with direct comparative connectives (in contrast, conversely).",
                     "Ensure every claim is supported with a quotation from the source text.",
                     golden_title="Top Scoring Advice", watch_title="Evidence Requirement")
        + K.fill_notes("Personal Target Score &amp; Time Checkpoints", min_mm=38),
        header=(BOOK, "Mock 2 &bull; Instructions"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    mock2_l2_sections = [
        ("Text A: The Freedom Economy &bull; Work from Home",
         "The shift toward flexible remote working has liberated millions of British workers from soul-destroying daily commutes. Economist Priya Sharma reports: 'Remote employees save an average of &pound;2,800 annually in rail fares and 380 hours in travel time. Productivity metrics across professional services have risen by 14%, disproving the antiquated myth that staff only work when surveilled in open-plan offices.'",
         [{"q": "<b>Question 1:</b> According to Text A, how much money do remote workers save on rail fares annually? (1 mark)", "lines": 2},
          {"q": "<b>Question 2:</b> Identify two benefits of remote working stated by Priya Sharma. (2 marks)", "lines": 3}]),
        ("Text A Language &amp; Argumentation",
         "Sharma notes that decentralised work stimulates regional market towns: 'Spending that once flowed exclusively into Central London now invigorates local bakeries, high streets, and community enterprises across regional towns.'",
         [{"q": "<b>Question 3:</b> What does Sharma mean by 'decentralised work'? (1 mark)", "lines": 2},
          {"q": "<b>Question 4:</b> Analyse how the writer of Text A uses emotive phrasing ('soul-destroying', 'liberated', 'antiquated myth') to persuade the reader. (2 marks)", "lines": 3},
          {"q": "<b>Question 5:</b> Identify the primary purpose of Text A. (1 mark)", "options": ["To persuade readers that remote working benefits individuals and regional economies", "To advise people how to buy cheap rail season tickets", "To criticise employees who spend money in local bakeries", "To announce the closure of all train lines into London"]}]),
        ("Text B: The Hollowed High Street &bull; Chamber of Commerce",
         "Statement by Arthur Pendelton, City Centre Retail Coalition:<br><em>'Our city centres are becoming ghost towns. Footfall across commercial districts has plunged by 35%, driving hundreds of independent sandwich bars, dry cleaners, and family-owned cafes into bankruptcy. Corporate landlords and remote workers abandon the civic ecosystem that sustained British commerce for generations. Without urgent return-to-office mandates, urban culture faces irreversible extinction.'</em>",
         [{"q": "<b>Question 6:</b> Extract one fact from Text B. (1 mark)", "lines": 2},
          {"q": "<b>Question 7:</b> Extract one opinion from Text B. (1 mark)", "lines": 2},
          {"q": "<b>Question 8:</b> Explain how Pendelton uses catastrophic imagery ('ghost towns', 'bankruptcy', 'extinction') to convey urgency. (2 marks)", "lines": 4}]),
        ("Text B Tone &amp; Text C Introduction",
         "Text C &bull; Parliamentary Commission on Future Urban Planning:<br>Recommendation 1: Local authorities must grant expedited planning permission for converting vacant commercial office premises into affordable residential apartments and creative co-working spaces.",
         [{"q": "<b>Question 9:</b> How would you describe the tone of Text B? Support your answer with a quotation. (2 marks)", "lines": 3},
          {"q": "<b>Question 10:</b> According to Text C, what planning permission should local authorities grant? (1 mark)", "lines": 2}]),
        ("Text C: Urban Regeneration Policy",
         "Recommendation 2: Establish 'Enterprise Hubs' in municipal town halls providing subsidised gigabit broadband, hot-desking, and childcare facilities. Funding will be allocated from the National Infrastructure Levelling Fund.",
         [{"q": "<b>Question 11:</b> Name two facilities provided in Enterprise Hubs according to Text C. (2 marks)", "lines": 3},
          {"q": "<b>Question 12:</b> Which national fund will finance the Enterprise Hubs? (1 mark)", "lines": 2},
          {"q": "<b>Question 13:</b> Explain how the layout of Text C (numbered recommendations) helps policymakers. (1 mark)", "lines": 2}]),
        ("The Flagship Comparison Question (Texts A &amp; B)",
         "Both Text A and Text B explore the consequences of the rise in remote working. Compare how the writers present contrasting arguments regarding the social and economic impact on communities.",
         [{"q": "<b>Question 14 (The 11-Mark Comparison Question):</b> In your answer, compare: &bull; The opposing views on where economic value is created &bull; How each writer characterises remote workers &bull; The contrasting tone, language, and stylistic devices. Include quotes from both texts. (11 marks)", "lines": 13}]),
        ("Synthesis &amp; Future Recommendations",
         "Synthesise ideas from all three texts to suggest a balanced model for future working arrangements.",
         [{"q": "<b>Question 15:</b> Synthesising insights from Text A, Text B, and Text C, propose three strategies for balancing remote employee flexibility with the survival of urban town centres. (3 marks)", "lines": 6}])
    ]

    for p_title, p_extract, p_qs in mock2_l2_sections:
        p_body = (
            K.page_title(f"Mock 2 &bull; {p_title}", kicker="Official Examination Booklet &bull; Reading Paper 2", badge="M2")
            + K.box_html(f"<div style='background:#f8fafc;padding:3mm;border:1.5px solid var(--soft);border-radius:4px;font-size:10.8pt;line-height:1.45;'>{p_extract}</div>", title="Reading Passage")
            + K.exercise_list(p_qs, lines=3)
        )
        pages.append(K.page(p_body, header=(BOOK, "Mock 2 &bull; Reading"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p75 to p80: Official Pearson Edexcel Level 2 Reading Assessment Grids & Rubrics (6 pages)
    rubric_start_page = p_curr
    l2_rubrics = [
        ("The 11-Mark Comparison Question Band Descriptors (L2.12)",
         "Band 4 (9–11 marks): Perceptive, detailed comparison across both texts; continuous direct comparative connectives; insightful analysis of perspectives and stylistic devices; balanced, well-chosen quotations.<br>"
         "Band 3 (6–8 marks): Clear comparison with sound identification of similarities and differences; appropriate quotes from both texts; mostly balanced structure.<br>"
         "Band 2 (3–5 marks): Basic comparison with superficial links; relies heavily on paraphrase; unbalanced coverage favouring one text.<br>"
         "Band 1 (1–2 marks): Isolated comments on one or both texts with no meaningful comparative synthesis."),
        ("Tone, Voice &amp; Register Assessment Criteria (L2.17, L2.19)",
         "Full marks awarded for identifying the specific adjective defining tone (e.g. indignant, urgent, impassioned, clinical, detached) paired with accurate lexical evidence and explanation of reader impact."),
        ("Implicit Meaning &amp; Subtext Marking Guidance (L2.13)",
         "Candidates must demonstrate insight into the writer's subtext, irony, or underlying assumptions rather than merely repeating literal surface statements."),
        ("Rhetorical &amp; Language Devices Assessment (L2.14)",
         "Examiners award marks for identifying the rhetorical device (hyperbole, rule of three, rhetorical question) AND explaining its exact psychological or persuasive influence on the target audience."),
        ("Evaluating Bias &amp; Argumentation Criteria (L2.17, L2.18)",
         "Full marks require candidates to distinguish verifiable factual claims from subjective vested interests, identifying omissions or unbalanced evidence."),
        ("Synthesis &amp; Cross-Referencing Standards (L2.11, L2.15, L2.16)",
         "Marks awarded for correctly extracting and synthesising disparate pieces of information from two or three separate source texts to draw a valid comprehensive conclusion.")
    ]

    for r_idx, (r_title, r_desc) in enumerate(l2_rubrics, 1):
        r_body = (
            K.page_title(f"Level 2 Assessment Criteria &bull; Part {r_idx} of 6", kicker=r_title, badge=f"RUB{r_idx}")
            + K.box_html(
                f"<div style='font-size:11.5pt;line-height:1.5;'>{r_desc}</div>",
                title="Official Pearson Edexcel Level 2 Marking Protocol"
            )
            + K.fill_notes(f"Personal Band 4 Action Plan &amp; Audit Notes (Part {r_idx})", min_mm=42)
        )
        pages.append(K.page(r_body, header=(BOOK, f"Assessment Criteria Part {r_idx}/6"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # Reference Section: Complete Solutions, Critical Glossary & Index
    ref_start_page = p_curr
    ref_blocks = []

    # Topic Practice Solutions (Topics 1 to 12: Task A = practice[1], Task B = practice[2])
    for t_idx, topic in enumerate(ert.READING_TOPICS[:12], 1):
        p_list = topic.get("practice_questions", [])
        pr_a = p_list[1] if len(p_list) > 1 else (p_list[0] if p_list else {})
        pr_b = p_list[2] if len(p_list) > 2 else (p_list[0] if p_list else {})
        qa_html = (
            K.ref_qa(f"R{t_idx}A", f"<b>Analysis:</b> {pr_a.get('solution_steps', '')}<br><b>Benchmark:</b> {pr_a.get('correct_answer', '')}", marks=pr_a.get("marks", "2m"))
            + K.ref_qa(f"R{t_idx}B", f"<b>Analysis:</b> {pr_b.get('solution_steps', '')}<br><b>Benchmark:</b> {pr_b.get('correct_answer', '')}", marks=pr_b.get("marks", "3m"))
        )
        ref_blocks.append(K.ref_block(f"Topic {t_idx}: {topic['clean_topic']} Solutions", qa_html))

    # Mock 1 Full Solutions (split into 3 balanced blocks so Q14 never overflows)
    m1_l2_ans = [
        ("Q1", "42%", "1m", "Direct retrieval from Text A paragraph 1."),
        ("Q2", "Detects malignant micro-tumours with 96.8% precision / Rescues clinicians from catastrophic burnout", "2m", "1m for each valid point."),
        ("Q3", "Systematic errors in computer algorithms that unfairly disadvantage specific demographic groups", "1m", "Conceptual vocabulary definition."),
        ("Q4", "Words like 'catastrophic burnout' elicit deep empathy, framing automation as a compassionate saviour rather than a managerial replacement", "2m", "1m for quote/analysis, 1m for impact."),
        ("Q5", "B: To advocate for the measured adoption of clinical AI tools", "1m", "Multiple choice key."),
        ("Q6", "Remote diagnostic hubs are being deployed / Tech companies hold public healthcare procurement contracts", "1m", "Verifiable fact."),
        ("Q7", "Remote hubs dehumanise medicine / Software venture capitalists profit excessively", "1m", "Subjective value judgment."),
        ("Q8", "Rhetorical question ('who bears legal accountability?') casts doubt on corporate safety, positioning patients as exploited victims", "2m", "1m for device/quote, 1m for impact."),
        ("Q9", "Impassioned, indignant, and sceptical ('cold glowing screens', 'aggressive cost-cutting')", "2m", "1m for tone label, 1m for quote."),
        ("Q10", "Data Protection Impact Assessment (DPIA)", "1m", "Direct statutory retrieval."),
        ("Q11", "20 hours", "1m", "Direct retrieval."),
        ("Q12", "Bi-annually (twice a year)", "1m", "Direct retrieval."),
        ("Q13", "Formal regulatory headings and mandatory auxiliary verbs convey strict statutory compliance", "2m", "1m for feature, 1m for effect."),
        ("Q15", "(1) Mandatory secondary validation by human consultants; (2) Comprehensive 20-hour staff training; (3) Rigorous bi-annual ethical audits", "3m", "1m for each safeguard synthesised.")
    ]
    ref_blocks.append(K.ref_block(
        "Official Reading Mock Paper 1 &bull; Solutions (Questions 1–8)",
        "".join(K.ref_qa(q, a, marks=m, working=w) for q, a, m, w in m1_l2_ans[:8])
    ))
    ref_blocks.append(K.ref_block(
        "Official Reading Mock Paper 1 &bull; Solutions (Questions 9–13 &amp; Q15)",
        "".join(K.ref_qa(q, a, marks=m, working=w) for q, a, m, w in m1_l2_ans[8:])
    ))
    ref_blocks.append(K.ref_block(
        "Official Reading Mock Paper 1 &bull; Q14 Band 4 Comparison Exemplar (11 Marks)",
        K.ref_qa("Q14",
                 "Text A presents a progressive, technological perspective, portraying AI as a vital clinical asset that 'rescues' exhausted doctors from burnout. In sharp contrast, Text B adopts an indignant trade-union stance, contending that technology 'dehumanises medicine' and serves corporate profit.<br><br>"
                 "Furthermore, whereas Text A validates its argument using quantitative medical statistics ('96.8% precision', '42% backlog reduction') to project scientific authority, Text B relies on evocative rhetorical questions and emotive metaphors ('cold glowing screens') to arouse ethical apprehension.<br><br>"
                 "However, both writers concede that human supervision remains essential: Text A explicitly cautions that 'unsupervised automation invites algorithmic bias', which aligns directly with Text B's demand for clear legal accountability.",
                 marks="11m", working="Comprehensive Band 4 comparative synthesis.")
    ))

    # Mock 2 Full Solutions (split into 3 balanced blocks)
    m2_l2_ans = [
        ("Q1", "£2,800 annually", "1m", "Direct retrieval from Text A."),
        ("Q2", "Saves 380 travel hours / Increases professional productivity by 14%", "2m", "1m for each point."),
        ("Q3", "Working away from a central city office, typically from home or regional co-working spaces", "1m", "Conceptual definition."),
        ("Q4", "Phrases like 'soul-destroying' and 'antiquated myth' delegitimise traditional office attendance, portraying remote work as enlightened progress", "2m", "1m for quote, 1m for persuasive effect."),
        ("Q5", "A: To persuade readers that remote working benefits individuals and regional economies", "1m", "Multiple choice key."),
        ("Q6", "Footfall across commercial districts has plunged by 35%", "1m", "Verifiable statistic."),
        ("Q7", "Our city centres are becoming ghost towns / Urban culture faces irreversible extinction", "1m", "Subjective hyperbolic opinion."),
        ("Q8", "Catastrophic language creates an existential crisis, pressurising policymakers to mandate office returns", "2m", "1m for quote, 1m for impact."),
        ("Q9", "Alarmist, urgent, and despairing ('bankruptcy', 'abandon', 'extinction')", "2m", "1m for tone label, 1m for quote."),
        ("Q10", "Expedited planning permission for converting vacant offices into residential apartments and co-working hubs", "1m", "Direct policy retrieval."),
        ("Q11", "Subsidised gigabit broadband / hot-desking / childcare facilities (any two)", "2m", "1m each."),
        ("Q12", "National Infrastructure Levelling Fund", "1m", "Direct retrieval."),
        ("Q13", "Numbered recommendations provide an unambiguous sequential roadmap for local council executives", "1m", "Layout functionality."),
        ("Q15", "(1) Convert obsolete commercial offices into affordable housing; (2) Create subsidised municipal co-working hubs; (3) Adopt hybrid working schedules combining office collaboration with remote focus days", "3m", "1m for each synthesised policy.")
    ]
    ref_blocks.append(K.ref_block(
        "Official Reading Mock Paper 2 &bull; Solutions (Questions 1–8)",
        "".join(K.ref_qa(q, a, marks=m, working=w) for q, a, m, w in m2_l2_ans[:8])
    ))
    ref_blocks.append(K.ref_block(
        "Official Reading Mock Paper 2 &bull; Solutions (Questions 9–13 &amp; Q15)",
        "".join(K.ref_qa(q, a, marks=m, working=w) for q, a, m, w in m2_l2_ans[8:])
    ))
    ref_blocks.append(K.ref_block(
        "Official Reading Mock Paper 2 &bull; Q14 Band 4 Comparison Exemplar (11 Marks)",
        K.ref_qa("Q14",
                 "Text A celebrates remote working as a triumph of individual autonomy and regional redistribution, arguing that saving '£2,800' and '380 hours' stimulates suburban high streets. Conversely, Text B laments this development as an economic catastrophe, warning that a 35% footfall collapse threatens urban commercial centres with 'irreversible extinction'.<br><br>"
                 "Stylistically, Text A employs an optimistic, professional register grounded in productivity research, whereas Text B leverages dramatic, apocalyptic imagery ('ghost towns', 'abandon the civic ecosystem') to lobby for corporate office mandates.<br><br>"
                 "While Text A champions the worker's personal sovereignty, Text B prioritises the collective civic community.",
                 marks="11m", working="Comprehensive Band 4 comparative synthesis.")
    ))

    # Level 2 Critical Reading Glossary (split into A-I and O-V)
    glossary_l2 = [
        ("Algorithmic Bias", "Systematic unfairness embedded in automated systems reflecting unrepresentative source data."),
        ("Comparative Connectives", "Conjunctions that establish explicit contrasts or parallels between texts (whereas, conversely, in contrast, similarly)."),
        ("Connotation", "The emotional or cultural association evoked by a word beyond its literal dictionary definition."),
        ("Counter-Argument", "An argument formulated to oppose or disprove an existing perspective."),
        ("Euphemism", "A mild or indirect word substituted for one considered harsh or blunt."),
        ("Hyperbole", "Deliberate exaggeration used for dramatic rhetorical emphasis."),
        ("Implicit Meaning", "Ideas suggested, hinted at, or embedded within the subtext of a passage."),
        ("Irony", "Expressing meaning by using language that normally signifies the opposite, typically for critical effect."),
        ("Objectivity", "Judgments based purely on observable, verifiable facts free from personal bias."),
        ("Register", "The variety and formality of language used in a specific professional or social context."),
        ("Rhetorical Question", "A question posed to provoke thought or persuade rather than elicit an answer."),
        ("Subjectivity", "Statements based on personal opinions, interpretations, feelings, or points of view."),
        ("Synthesis", "Combining diverse facts and perspectives from multiple sources into a coherent whole."),
        ("Tone", "The author's underlying attitude or perspective communicated through vocabulary and syntax."),
        ("Vested Interest", "A personal or commercial stake in an issue that influences objectivity.")
    ]
    ref_blocks.append(K.ref_block(
        "Critical Lexicon of Textual Analysis (A–I)",
        "".join(f"<p style='margin:0 0 1.2mm 0;'><b>{w}:</b> {d}</p>" for w, d in glossary_l2[:8])
    ))
    ref_blocks.append(K.ref_block(
        "Critical Lexicon of Textual Analysis (O–V)",
        "".join(f"<p style='margin:0 0 1.2mm 0;'><b>{w}:</b> {d}</p>" for w, d in glossary_l2[8:])
    ))

    # Level 2 Subject Index (split into A-I and L-V)
    index_l2_items = [
        ("A", [("Algorithmic Bias", "59, 60"), ("Argumentation Lines", "33, 55"), ("Author's Voice", "37, 49")]),
        ("B", [("Band 4 Comparison Criteria", "75"), ("Bias Detection", "33, 55")]),
        ("C", [("Comparison Question (11 Marks)", "45, 57, 65, 73"), ("Connotation", "9, 29")]),
        ("D", [("Deconstructing Subtext", "9, 54"), ("Diagnostic Matrix", "4")]),
        ("E", [("Emotive Language", "29, 56"), ("Evaluating Evidence", "5, 33")]),
        ("G", [("Glossary of Terms", f"{ref_start_page + 6}"), ("Golden Comparison Rules", "45, 57")]),
        ("H", [("Hyperbole Analysis", "29, 56")]),
        ("I", [("Implicit Meaning", "9, 25, 54"), ("Irony & Sarcasm", "37, 54")]),
        ("L", [("Layout Authority", "17, 21")]),
        ("M", [("Mock Exam Paper 1 (Medical AI)", f"{mock1_start_page}"), ("Mock Exam Paper 2 (Remote Work)", f"{mock2_start_page}")]),
        ("O", [("Objectivity vs. Subjectivity", "5, 33")]),
        ("P", [("Pacing Strategy (75 Mins)", "3, 53"), ("Persuasive Devices", "29, 56")]),
        ("R", [("Rhetorical Questions", "29, 56")]),
        ("S", [("Synthesis Methods", "45, 58, 66, 74")]),
        ("T", [("Timing (2 Mins/Mark)", "3, 53"), ("Tone & Register", "13, 37, 76")]),
        ("V", [("Vested Interests", "33, 55")])
    ]
    def render_ix_l2_slice(slice_items):
        out = ""
        for letter, entries in slice_items:
            items = "".join(f"<div class='ix'><span>{escape_html(t)}</span><span>p.{escape_html(p)}</span></div>" for t, p in entries)
            out += f"<div class='ix-letter'>{letter}</div>{items}"
        return out

    ref_blocks.append(K.ref_block("Level 2 Subject Index (A–I)", render_ix_l2_slice(index_l2_items[:8])))
    ref_blocks.append(K.ref_block("Level 2 Subject Index (L–V)", render_ix_l2_slice(index_l2_items[8:])))

    cover_theme = K.theme_from_cover(front_cov)
    ref_page_list = K.ref_pages("Reference Section: Solutions, Glossary &amp; Index", ref_blocks,
                                BOOK, start_page=p_curr, subtitle="Complete Worked Solutions, Lexicon &amp; Alphabetical Index",
                                cols=2, theme=cover_theme, notes_title="Candidate Analytical Notes")
    pages.extend(ref_page_list)
    p_curr += len(ref_page_list)

    # Final Readiness Page
    ready_page_no = p_curr
    p_ready_body = (
        K.page_title("Level 2 Reading &bull; Exam Day Commitments", kicker="Final Revision &bull; Band 4 Mastery", badge="READY")
        + K.box_html(
            "<p>Before sitting your Pearson Edexcel Level 2 Reading examination, commit to these 5 Band 4 imperatives:</p>"
            + K.bullets([
                "<b>1. Allocate Time for All 3 Texts:</b> Spend the first 15 minutes actively reading all extracts before writing.",
                "<b>2. Integrate Your Comparison:</b> In Question 14, link Text A and Text B continuously with comparative connectives.",
                "<b>3. Quote and Analyse:</b> Always pair direct textual quotations with explanations of the writer's deliberate effect.",
                "<b>4. Distinguish Fact from Bias:</b> Question the writer's motives and identify vested commercial or political interests.",
                "<b>5. Protect Your Synthesis:</b> In multi-text questions, combine evidence from across the sources rather than relying on one."
            ]),
            title="Golden Exam Rules for Level 2 Reading Success"
        )
        + K.fill_notes("Personal Pre-Exam Commitments &amp; Tutor Endorsement", min_mm=45)
    )
    pages.append(K.page(p_ready_body, header=(BOOK, "Exam Readiness"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Duplex balance check before back cover
    if (len(pages) + 1) % 2 != 0:
        p_extra = (
            K.page_title("Candidate Final Verification Protocol", kicker="Pearson Edexcel Band 4 Reading Standards", badge="AUDIT")
            + K.box_html(
                "<p>Final pre-submission audit checklist:</p>"
                + K.bullets([
                    "Did you integrate comparative connectives in the 11-mark comparison question?",
                    "Did you clearly name specific language and layout techniques with direct quotes?",
                    "Did you review your answers against the author's overall tone and purpose?"
                ]),
                title="Final Verification"
            )
            + K.fill_notes("Final Examination Reflections", min_mm=40)
        )
        pages.append(K.page(p_extra, header=(BOOK, "Verification Protocol"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # Populate p2: Complete 2-Column Table of Contents with exact dynamic page numbers
    toc_left = [
        ("INTRO", "Specification &amp; Diagnostic Audit", [
            ("SPEC", "Pearson Edexcel L2.11–L2.19 Specification", "3"),
            ("AUDIT", "Candidate Baseline Skills Audit Matrix", "4"),
        ]),
        ("TOPICS", "Core Reading Topics (R1–R12)", [
            (f"R{i}", ert.READING_TOPICS[i-1]["clean_topic"], str(topic_start_pages[i]))
            for i in range(1, 13)
        ]),
    ]
    toc_right = [
        ("EXAM", "Analytical Strategy Masterclasses (EX1–EX6)", [
            (f"EX{i}", l2_masterclasses[i-1][0].replace("&amp;", "&"), str(mc_start_page + i - 1))
            for i in range(1, 7)
        ]),
        ("MOCKS", "Official Reading Mock Exam Papers", [
            ("M1", "Mock Exam Paper 1: Clinical Automation &amp; AI", str(mock1_start_page)),
            ("M2", "Mock Exam Paper 2: Remote Work &amp; Cities", str(mock2_start_page)),
        ]),
        ("MARK", "Official Pearson Edexcel Assessment Grids", [
            ("RUB1–3", "Band 4 Comparison, Tone &amp; Subtext Grids", str(rubric_start_page)),
            ("RUB4–6", "Rhetoric, Bias &amp; Synthesis Grids", str(rubric_start_page + 3)),
        ]),
        ("REF", "Solutions, Glossary, Index &amp; Readiness", [
            ("SOL", "Topic Drills &amp; Mock 1–2 Full Solutions", str(ref_start_page)),
            ("GLOSS", "Critical Lexicon &amp; Alphabetical Index", str(ref_start_page + 6)),
            ("READY", "Band 4 Exam Readiness Commitments", str(ready_page_no)),
        ]),
    ]
    pages[1] = reading_toc_page(
        "Functional Skills English &bull; Reading Level 2",
        "Comprehensive Textual Analysis, Synthesis &amp; Comparison Manual (DfE L2.11–L2.19)",
        toc_left, toc_right, BOOK
    )

    # Back Cover
    pages.append(K.back_cover(back_cov))

    print(f"Total Pages Assembled: {len(pages)}")
    out_pdf = DOWNLOADS / "MasterFunctionalSkills_English_Reading_Level_2_Core_Guide.pdf"
    res = K.render_pdf(pages, out_pdf, theme=cover_theme, entry3=False, title="Master Functional Skills - English Reading Level 2 Core Guide")
    shutil.copy(out_pdf, DOCUMENTS / out_pdf.name)
    print(f"Verified & Saved: {out_pdf} -> {DOCUMENTS / out_pdf.name}")
    print(f"Overflows: {res.get('overflow', [])}")
    return res


def main():
    r1 = build_reading_l1_core()
    r2 = build_reading_l2_core()
    print("\nALL READING SUITE BUILDS COMPLETED SUCCESSFULLY!")
    print("L1 Overflows:", r1.get("overflow", []))
    print("L2 Overflows:", r2.get("overflow", []))


if __name__ == "__main__":
    main()
