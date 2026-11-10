#!/usr/bin/env python3
"""
books/a4/build_spag_suite_a4.py
=============================================================================
Compiles all 3 Master Functional Skills SPaG publications in the A4 design:
1. MasterFunctionalSkills_SPaG_Level_2_Mastery.pdf
2. MasterFunctionalSkills_SPaG_Level_1_Mastery.pdf
3. MasterFunctionalSkills_SPaG_Entry_Level_3_Mastery.pdf

Upgrades applied:
- Complete 2-column Table of Contents on Page 2 listing every single Unit,
  Vocabulary Module, Workout Series, Mock Exam, and Reference Section
- Wide-angle 16:9 establishing photographs (from e3_thematic, writing_thematic,
  and reading_thematic) with compact single-line captions across all Unit Practise
  pages, all 36 Vocabulary in Use visual dictionary tiles, and Mock Writing Exams
- Zero repeats of photos within any book, proper head-safe object-position framing
- Granular per-unit, per-workout, and per-mock Reference Section blocks so
  2-column CSS grid pages have 0 column/page overflows
- 100% confidentiality compliance (Tutor Abdul, 0 forbidden organisation names)
=============================================================================
"""

import os
import sys
import shutil
from html import escape as escape_html
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJECT_DIR = HERE.parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(PROJECT_DIR / "books" / "spag"))

import a4_kit as K
import spag_data_l2
import spag_data_l1
import spag_l2_84p_units_1_13 as u_l2_p1
import spag_l2_84p_units_14_26 as u_l2_p2
import spag_l2_84p_diag_vocab as dv_l2
import spag_l2_84p_mocks_keys as mk_l2

import spag_l1_84p_units as u_l1
import spag_l1_84p_data as d_l1

import spag_data_e3_84p as d_e3
import generate_e3_data as u_e3
import spag_data_e3_extras as x_e3
import spag_data_e3_answers as a_e3

DOWNLOADS = PROJECT_DIR / "assets" / "downloads"
DOCUMENTS = Path("/home/subi/Documents")
COV = K.COVER_DIR


# =============================================================================
# Curated Pool of 98 Wide-Angle 16:9 Thematic Photographs (Zero Cropped Heads)
# =============================================================================
WIDE_THEMATIC_POOL = [
    # writing_thematic (56)
    "writing_thematic/spag1_clauses.jpg",
    "writing_thematic/spag2_complex.jpg",
    "writing_thematic/spag3_agreement.jpg",
    "writing_thematic/spag4_modals.jpg",
    "writing_thematic/spag5_lists.jpg",
    "writing_thematic/spag6_apostrophes.jpg",
    "writing_thematic/spag7_cohesion.jpg",
    "writing_thematic/spag8_spelling.jpg",
    "writing_thematic/l2_f1_article.jpg",
    "writing_thematic/l2_f2_letter.jpg",
    "writing_thematic/l2_f3_email.jpg",
    "writing_thematic/l2_f4_memo.jpg",
    "writing_thematic/l2_f5_report.jpg",
    "writing_thematic/l2_f6_report.jpg",
    "writing_thematic/l2_f7_leaflet.jpg",
    "writing_thematic/l2_f8_review.jpg",
    "writing_thematic/l2_f9_blog.jpg",
    "writing_thematic/l2_f10_proposal.jpg",
    "writing_thematic/l2_f11_statement.jpg",
    "writing_thematic/l2_f12_speech.jpg",
    "writing_thematic/l2_f1_task2.jpg",
    "writing_thematic/l2_f2_task2.jpg",
    "writing_thematic/l2_f3_task2.jpg",
    "writing_thematic/l2_f4_task2.jpg",
    "writing_thematic/l2_f5_task2.jpg",
    "writing_thematic/l2_f6_task2.jpg",
    "writing_thematic/l2_f7_task2.jpg",
    "writing_thematic/l2_f8_task2.jpg",
    "writing_thematic/l2_f9_task2.jpg",
    "writing_thematic/l2_f10_task2.jpg",
    "writing_thematic/l2_f11_task2.jpg",
    "writing_thematic/l2_f12_task2.jpg",
    "writing_thematic/l1_f1_article.jpg",
    "writing_thematic/l1_f2_letter.jpg",
    "writing_thematic/l1_f3_email.jpg",
    "writing_thematic/l1_f4_memo.jpg",
    "writing_thematic/l1_f5_report.jpg",
    "writing_thematic/l1_f6_report.jpg",
    "writing_thematic/l1_f7_leaflet.jpg",
    "writing_thematic/l1_f8_review.jpg",
    "writing_thematic/l1_f9_blog.jpg",
    "writing_thematic/l1_f10_proposal.jpg",
    "writing_thematic/l1_f11_statement.jpg",
    "writing_thematic/l1_f12_speech.jpg",
    "writing_thematic/l1_f1_task2.jpg",
    "writing_thematic/l1_f2_task2.jpg",
    "writing_thematic/l1_f3_task2.jpg",
    "writing_thematic/l1_f4_task2.jpg",
    "writing_thematic/l1_f5_task2.jpg",
    "writing_thematic/l1_f6_task2.jpg",
    "writing_thematic/l1_f7_task2.jpg",
    "writing_thematic/l1_f8_task2.jpg",
    "writing_thematic/l1_f9_task2.jpg",
    "writing_thematic/l1_f10_task2.jpg",
    "writing_thematic/l1_f11_task2.jpg",
    "writing_thematic/l1_f12_task2.jpg",
    # e3_thematic (30)
    "e3_thematic/w1_capital_letters.jpg",
    "e3_thematic/w2_sentence_punctuation.jpg",
    "e3_thematic/w3_commas_apostrophes.jpg",
    "e3_thematic/w4_compound_sentences.jpg",
    "e3_thematic/w5_giving_reasons.jpg",
    "e3_thematic/w6_past_tense.jpg",
    "e3_thematic/w7_agreement_plurals.jpg",
    "e3_thematic/w8_paragraphs_order.jpg",
    "e3_thematic/w9_format_email.jpg",
    "e3_thematic/w10_format_letter_note.jpg",
    "e3_thematic/w11_format_notice_leaflet.jpg",
    "e3_thematic/w12_format_form_feedback.jpg",
    "e3_thematic/sp1_prefixes.jpg",
    "e3_thematic/sp2_suffixes.jpg",
    "e3_thematic/sp3_silent_letters.jpg",
    "e3_thematic/sp4_double_consonants.jpg",
    "e3_thematic/sp5_word_endings.jpg",
    "e3_thematic/sp6_homophones.jpg",
    "e3_thematic/r1_fire_safety_sign.jpg",
    "e3_thematic/r2_community_garden.jpg",
    "e3_thematic/r3_college_enrolment.jpg",
    "e3_thematic/r4_office_laminator.jpg",
    "e3_thematic/r5_high_street_directory.jpg",
    "e3_thematic/r6_warehouse_memo.jpg",
    "e3_thematic/r7_hospital_clinic.jpg",
    "e3_thematic/r8_bus_train_compare.jpg",
    "e3_thematic/r9_leisure_timetable.jpg",
    "e3_thematic/r10_cycle_scheme.jpg",
    "e3_thematic/r11_council_bins.jpg",
    "e3_thematic/r12_pharmacy_cream.jpg",
    # reading_thematic (12 sharp wide-angle photos)
    "reading_thematic/r1_l1_gym.jpg",
    "reading_thematic/r2_l1_office_hvac.jpg",
    "reading_thematic/r3_l1_kitchen_fridge.jpg",
    "reading_thematic/r4_l1_clinic_letter.jpg",
    "reading_thematic/r5_l1_hr_intranet.jpg",
    "reading_thematic/r6_l1_manual_handling.jpg",
    "reading_thematic/r7_l1_cycling_flyer.jpg",
    "reading_thematic/r8_l1_library_letter.jpg",
    "reading_thematic/r10_l1_sharps_sop.jpg",
    "reading_thematic/r11_l1_cashless_tills.jpg",
    "reading_thematic/r12_l1_apprentice_induction.jpg",
    "reading_thematic/mc1_exam_clock.jpg",
]

TOP_ALIGNED_PHOTOS = {
    "reading_thematic/r3_l1_kitchen_fridge.jpg": "center 22%",
    "reading_thematic/r5_l1_hr_intranet.jpg": "center 24%",
    "reading_thematic/r6_l1_manual_handling.jpg": "center 20%",
    "reading_thematic/r7_l1_cycling_flyer.jpg": "center 26%",
    "reading_thematic/r8_l1_library_letter.jpg": "center 22%",
    "reading_thematic/r12_l1_apprentice_induction.jpg": "center 22%",
    "reading_thematic/mc1_exam_clock.jpg": "center 24%",
}


def resolve_spag_photo(rel_path):
    p = K.PHOTO_DIR / rel_path
    if p.exists():
        return p.resolve().as_uri()
    fallback = K.PHOTO_DIR / "writing_thematic/spag1_clauses.jpg"
    return fallback.resolve().as_uri()


def clean_mod_title(t):
    import re
    return re.sub(r"^Module\s+\d+\s*:\s*", "", str(t).strip(), flags=re.IGNORECASE)


def spag_practice_banner(rel_path, caption="", height_mm=50):
    """Wide-angle 16:9 thematic banner with elevated framing and bold caption."""
    uri = resolve_spag_photo(rel_path)
    obj_pos = TOP_ALIGNED_PHOTOS.get(rel_path, "center 25%")
    cap_html = (
        f"<div style='padding:0.85mm 1.5mm;font-size:7.6pt;font-weight:700;line-height:1.15;color:var(--primary);"
        f"background:#eff6ff;border-top:1px solid #bfdbfe;text-align:center;"
        f"white-space:nowrap;overflow:hidden;text-overflow:ellipsis;'>{caption}</div>"
    ) if caption else ""
    return (
        f"<div class='hero-img' style='margin:0 0 2.0mm 0;border:1.5px solid var(--primary);"
        f"border-radius:6px;overflow:hidden;background:#ffffff;box-shadow:0 1.5px 4px rgba(0,0,0,0.08);'>"
        f"<div style='width:100%;aspect-ratio:16/9;max-height:{height_mm}mm;overflow:hidden;background:#0f172a;'>"
        f"<img src='{uri}' alt='' style='width:100%;height:100%;"
        f"object-fit:cover;object-position:{obj_pos};display:block;'/>"
        f"</div>"
        f"{cap_html}"
        f"</div>"
    )


def spag_float_practice_card(rel_path, caption="", width_mm=60):
    """Renders a medium-to-big 16:9 scenario card floated right without cropping."""
    uri = resolve_spag_photo(rel_path)
    cap_html = (
        f"<div style='padding:0.6mm 1.2mm;font-size:7.4pt;font-weight:700;line-height:1.15;color:var(--primary);"
        f"background:#eff6ff;border-top:1px solid #bfdbfe;text-align:center;"
        f"white-space:nowrap;overflow:hidden;text-overflow:ellipsis;'>{caption}</div>"
    ) if caption else ""
    return (
        f"<div style='float:right;width:{width_mm}mm;margin:0 0 1.2mm 3mm;border:1.5px solid var(--primary);"
        f"border-radius:6px;overflow:hidden;background:#ffffff;box-shadow:0 1.5px 4px rgba(0,0,0,0.08);'>"
        f"<div style='width:100%;aspect-ratio:16/9;overflow:hidden;background:#0f172a;'>"
        f"<img src='{uri}' alt='' style='width:100%;height:100%;object-fit:cover;object-position:center 25%;display:block;'/>"
        f"</div>"
        f"{cap_html}"
        f"</div>"
    )


def spag_vocab_grid(tiles_data):
    """Renders 6 Vocabulary in Use visual dictionary tiles (3x2 grid) with elevated cards."""
    cards = []
    for rel_path, word_html, ex_sent in tiles_data:
        uri = resolve_spag_photo(rel_path)
        obj_pos = TOP_ALIGNED_PHOTOS.get(rel_path, "center 25%")
        cards.append(
            f"<div style='border:1.5px solid var(--primary);border-radius:6px;overflow:hidden;"
            f"background:#fff;display:flex;flex-direction:column;box-shadow:0 1.5px 4px rgba(0,0,0,0.08);'>"
            f"<div style='width:100%;aspect-ratio:16/9;overflow:hidden;background:#0f172a;'>"
            f"<img src='{uri}' alt='' style='width:100%;height:100%;object-fit:cover;"
            f"object-position:{obj_pos};display:block;'/>"
            f"</div>"
            f"<div style='padding:2mm 2.4mm;flex:1;display:flex;flex-direction:column;justify-content:space-between;'>"
            f"<div style='font-size:9.2pt;font-weight:800;color:var(--primary);line-height:1.22;margin-bottom:1mm;'>{word_html}</div>"
            f"<div style='font-size:7.8pt;line-height:1.28;color:#334155;font-style:italic;'>{ex_sent}</div>"
            f"</div>"
            f"</div>"
        )
    return (
        f"<div style='display:grid;grid-template-columns:repeat(3,minmax(0,1fr));"
        f"gap:3mm;margin-top:1.5mm;'>"
        f"{''.join(cards)}"
        f"</div>"
    )


def spag_toc_page(level_label, subtitle, sections_left, sections_right, footer_book):
    """Builds a comprehensive, zero-overflow 2-column Table of Contents on Page 2 with large, chapter-proportional fonts."""
    def render_col(sec_list):
        out = []
        for sec_code, sec_title, items in sec_list:
            out.append(
                f"<div style='background:linear-gradient(135deg, var(--primary-dark), var(--primary));color:#fff;padding:1.2mm 2.6mm;"
                f"border-radius:3.5mm;font-size:9.2pt;font-weight:800;letter-spacing:0.03em;"
                f"text-transform:uppercase;margin:1.4mm 0 0.8mm 0;display:flex;"
                f"justify-content:space-between;align-items:center;box-shadow:0 1px 3px rgba(0,0,0,0.04);'>"
                f"<span>{sec_title}</span>"
                f"<span style='background:rgba(255,255,255,0.22);padding:0.2mm 1.6mm;"
                f"border-radius:2px;font-size:7.8pt;'>{sec_code}</span>"
                f"</div>"
            )
            for badge, label, pg in items:
                out.append(
                    f"<div style='display:grid;grid-template-columns:13mm minmax(0,1fr) 11.5mm;"
                    f"align-items:center;gap:1.4mm;padding:0.85mm 1.2mm;"
                    f"border-bottom:0.5px dashed #cbd5e1;font-size:8.8pt;line-height:1.22;'>"
                    f"<span class='chip' style='padding:0.2mm 1.4mm;font-size:8.2pt;font-weight:800;display:inline-block;text-align:center;min-width:10.5mm;border-radius:1.2mm;'>{badge}</span>"
                    f"<span style='white-space:nowrap;overflow:hidden;text-overflow:ellipsis;"
                    f"color:#1e293b;font-weight:600;'>{label}</span>"
                    f"<span style='text-align:right;font-weight:800;color:var(--primary);"
                    f"font-size:9.0pt;font-variant-numeric:tabular-nums;'>p.{pg}</span>"
                    f"</div>"
                )
        return "".join(out)

    body = (
        f"<div style='background:linear-gradient(135deg, var(--primary-dark), var(--primary));color:#fff;padding:2.8mm 4.2mm;"
        f"border-radius:6px;margin-bottom:1.6mm;display:flex;"
        f"justify-content:space-between;align-items:center;box-shadow:0 1.5px 4px rgba(0,0,0,0.08);'>"
        f"<div>"
        f"<div style='font-size:7.8pt;text-transform:uppercase;letter-spacing:0.8px;"
        f"opacity:0.9;font-weight:700;'>Master Functional Skills &bull; Complete SPaG Curriculum Directory</div>"
        f"<div style='font-size:14pt;font-weight:900;line-height:1.15;margin-top:0.4mm;'>"
        f"{level_label} &bull; Table of Contents</div>"
        f"<div style='font-size:8.6pt;opacity:0.92;margin-top:0.3mm;'>{subtitle}</div>"
        f"</div>"
        f"<div style='background:rgba(255,255,255,0.18);border:1px solid rgba(255,255,255,0.35);"
        f"padding:1.6mm 3mm;border-radius:5px;text-align:center;'>"
        f"<div style='font-size:6.8pt;text-transform:uppercase;letter-spacing:0.5px;'>Pearson Edexcel</div>"
        f"<div style='font-size:10pt;font-weight:900;'>SPaG MASTERY</div>"
        f"</div>"
        f"</div>"
        f"<div style='display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:4.5mm;'>"
        f"<div>{render_col(sections_left)}</div>"
        f"<div>{render_col(sections_right)}</div>"
        f"</div>"
        f"<div style='margin-top:auto;padding:1.5mm 3mm;background:var(--tint);border:0.3mm solid var(--border);border-radius:1.8mm;display:flex;justify-content:space-between;align-items:center;font-size:7.6pt;color:var(--muted);'>"
        f"<span><b>Master Functional Skills &bull; SPaG Mastery Manual</b> &bull; Grammar, Punctuation &amp; Spelling</span>"
        f"<span><b>Lead Tutor:</b> Abdul &bull; <b>Edition:</b> 2026/2027 Reformed Standards</span>"
        f"</div>"
    )
    return K.page(body, header=(footer_book, "Table of Contents"), footer=footer_book, page_no=2)


# =============================================================================
# 1. SPaG Level 2 Mastery
# =============================================================================
def build_spag_l2():
    print("\n" + "="*70)
    print("BUILDING: MasterFunctionalSkills_SPaG_Level_2_Mastery.pdf")
    print("="*70)

    BOOK = "SPaG Level 2 Mastery"
    front_cov = COV / "spag_l2_mastery_cover-01.png"
    back_cov = COV / "spag_l2_mastery_cover-02.png"

    all_units = u_l2_p1.UNITS_1_TO_13 + u_l2_p2.UNITS_14_TO_26
    pages = []
    photo_cursor = [0]

    def next_wide_photo():
        rel = WIDE_THEMATIC_POOL[photo_cursor[0] % len(WIDE_THEMATIC_POOL)]
        photo_cursor[0] += 1
        return rel

    # p1: Front Cover
    pages.append(K.front_cover(front_cov))

    # p2: Placeholder for 2-Column Table of Contents
    pages.append(None)

    # p3-6: Diagnostic Assessment (4 pages, 10 authentic questions total)
    diag_qs = spag_data_l2.L2_DIAGNOSTIC["questions"]
    scoring_rows = spag_data_l2.L2_DIAGNOSTIC["scoring"]

    def make_ex_items(qs):
        items = []
        for q in qs:
            clean_opts = [o[3:] if len(o) > 3 and o[1] == ")" else o for o in q["options"]]
            pr = q.get("prompt", "")
            top = q.get("topic", "")
            items.append({
                "q": f"<b>{pr}</b> <span style='font-size:10pt;color:var(--muted);font-weight:400;'>({top})</span>",
                "options": clean_opts,
                "marks": 1
            })
        return items

    pages.append(K.page(
        K.page_title("Baseline Diagnostic Assessment &bull; Part 1 of 4",
                     kicker="Diagnostic Audit &bull; Questions 1&ndash;3",
                     lead="Answer each question. Circle your chosen answer. Do not use a dictionary.")
        + K.exercise_list(make_ex_items(diag_qs[0:3]), start=1),
        header=(BOOK, "Diagnostic 1/4"), footer=BOOK, page_no=3
    ))

    pages.append(K.page(
        K.page_title("Baseline Diagnostic Assessment &bull; Part 2 of 4",
                     kicker="Diagnostic Audit &bull; Questions 4&ndash;6",
                     lead="Identify the correct sentence structure, punctuation, and capitalisation.")
        + K.exercise_list(make_ex_items(diag_qs[3:6]), start=4),
        header=(BOOK, "Diagnostic 2/4"), footer=BOOK, page_no=4
    ))

    score_table = """<div class="box" style="padding:2.5mm 3.5mm;background:#fff;border:1.5px solid var(--soft);margin-top:2mm;">
      <div style="font-weight:700;color:var(--primary);font-size:11pt;margin-bottom:1.5mm;">Diagnostic Performance Matrix &amp; Recommended Study Pathway</div>
      <table style="width:100%;border-collapse:collapse;font-size:9.6pt;">
        <thead>
          <tr style="background:var(--light);color:var(--primary);text-align:left;">
            <th style="padding:1.5mm;border:1px solid var(--soft);">Score Range</th>
            <th style="padding:1.5mm;border:1px solid var(--soft);">Readiness Level</th>
            <th style="padding:1.5mm;border:1px solid var(--soft);">Recommended Curriculum Route</th>
          </tr>
        </thead>
        <tbody>"""
    for row in scoring_rows:
        score_table += f"""
          <tr>
            <td style="padding:1.5mm;border:1px solid var(--soft);font-weight:700;">{row['range']}</td>
            <td style="padding:1.5mm;border:1px solid var(--soft);color:var(--accent);font-weight:600;">{row['status']}</td>
            <td style="padding:1.5mm;border:1px solid var(--soft);">{row['advice']}</td>
          </tr>"""
    score_table += """</tbody></table></div>"""

    pages.append(K.page(
        K.page_title("Baseline Diagnostic Assessment &bull; Part 3 of 4",
                     kicker="Diagnostic Audit &bull; Questions 7&ndash;8",
                     lead="Grammar and syntax accuracy questions, followed by the diagnostic benchmark rubric.")
        + K.exercise_list(make_ex_items(diag_qs[6:8]), start=7)
        + score_table,
        header=(BOOK, "Diagnostic 3/4"), footer=BOOK, page_no=5
    ))

    pages.append(K.page(
        K.page_title("Baseline Diagnostic Assessment &bull; Part 4 of 4",
                     kicker="Diagnostic Audit &bull; Questions 9&ndash;10 &amp; Study Plan",
                     lead="Final vocational diagnostic questions and your personalised revision action plan.")
        + K.exercise_list(make_ex_items(diag_qs[8:10]), start=9)
        + K.tip_pair("Check your diagnostic score against the answer keys in the Reference Section.",
                     "Prioritise the specific units flagged in questions you found challenging.",
                     golden_title="Tutor Golden Rule", watch_title="Revision Target")
        + K.fill_lines("Candidate Action Plan &amp; Priority Units to Master", min_mm=30, gap_mm=9.5),
        header=(BOOK, "Diagnostic 4/4"), footer=BOOK, page_no=6
    ))

    # p7-58: 26 Units (52 pages)
    characters = [
        ("Priya", "tutor woman female", "#7c3aed"),
        ("Abdul", "abdul tutor man", "#0c4a6e"),
        ("Marcus", "marcus apprentice", "#0d9488"),
        ("Sarah", "sarah care nurse", "#be123c"),
        ("Sam", "sam learner thinking", "#475569"),
    ]

    p_curr = 7
    unit_start_pages = {}
    for u_idx, u in enumerate(all_units):
        u_num = u["unit"]
        unit_start_pages[u_num] = p_curr
        char_name, char_kw, char_col = characters[u_idx % len(characters)]

        # --- Left Page: Learn ---
        anchor_title = u.get("format_link", u.get("anchor_title", "Workplace Scenario"))
        if len(anchor_title) > 90:
            anchor_title = anchor_title[:87] + "..."
        rule_title = u.get("rule_title", "Syntax Architecture &amp; Core Structural Rules")
        rule_text = K.clean_legacy(u.get("rule_text", ""))
        bad_text = u.get("worked_bad", "Example with error.")
        good_text = u.get("worked_good", "Corrected example.")
        why_text = u.get("worked_why", "Grammatical explanation.")

        font_sz = "9.5pt" if len(rule_text) > 1100 else ("10pt" if len(rule_text) > 900 else "10.5pt")
        lh = "1.2" if len(rule_text) > 1100 else ("1.25" if len(rule_text) > 900 else "1.28")
        bubble_h = 44 if len(rule_text) > 1100 else 48

        left_body = (
            K.page_title(u["title"], kicker=f"Unit {u_num} &bull; {u['strand']}", badge=u_num)
            + K.character_bubble(
                K.cartoon(char_kw), char_name,
                f"<b style='color:var(--accent)'>A &nbsp;The Concept in Practice:</b> {anchor_title}",
                "left", bubble_h, char_col
            )
            + f"""<div class="box rule" style="flex:1 0 auto;padding:2mm 3.5mm;font-size:{font_sz};line-height:{lh};">
                <div class="bt" style="margin-bottom:1mm;"><span class="ico">&#9733;</span>B &nbsp;{rule_title}</div>
                <div style="font-size:{font_sz};">{rule_text}</div>
              </div>"""
            + K.compare(
                f"<div style='font-size:10pt;line-height:1.22;'>{bad_text}</div>",
                f"<div style='font-size:10pt;line-height:1.22;'>{good_text}</div><div style='font-size:9pt;color:var(--muted);margin-top:1mm;'><b>Rule:</b> {why_text}</div>",
                stacked=False, bad_label="&#10007; Common Error", good_label="&#10003; Model Solution"
            )
        )
        pages.append(K.page(left_body, header=(BOOK, f"Unit {u_num} &bull; Learn"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # --- Right Page: Practise (with wide-angle thematic photo banner & 1-line caption) ---
        ex_a_items = []
        for q_tuple in u.get("exercise_a", [])[:2]:
            q_text, opts = q_tuple[0], q_tuple[1]
            clean_opts = [o[3:] if len(o) > 3 and o[1] == ")" else o for o in opts]
            ex_a_items.append({"q": q_text, "options": clean_opts})

        ex_b_items = []
        for b_idx, b_tuple in enumerate(u.get("exercise_b", [])[:2]):
            prompt_type, original = b_tuple[0], b_tuple[1]
            n_lines = 1 if u_num in (1, 2, 4, 5, 6, 7, 8, 19, 20) else 2
            ex_b_items.append((f"<b>[{prompt_type}]:</b> <i>{original}</i>", n_lines))

        u_photo = next_wide_photo()
        u_cap = f"Unit {u_num} Workplace Context ({u.get('anchor_title', u['title'])}): Applying {u['title']}."
        right_body = (
            K.section("A", "Tick the correct sentence")
            + spag_float_practice_card(u_photo, u_cap, width_mm=60)
            + K.exercise_list(ex_a_items)
            + "<div style='clear:both;'></div>"
            + K.section("B", "Rewrite each sentence correctly")
            + K.exercise_list(ex_b_items, start=3)
            + K.fill_lines(f"<span style='color:var(--accent)'>C &nbsp;Applied Task:</span> Write two sentences using the rules from Unit {u_num}.", min_mm=6, gap_mm=7.0)
        )
        pages.append(K.page(right_body, header=(BOOK, f"Unit {u_num} &bull; Practise"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p59-70: 6 Vocab in Use Modules (12 pages: 2 pages each)
    vocab_start_pages = {}
    vocab_mods = dv_l2.VOCABULARY_MODULES
    for v_idx, vm in enumerate(vocab_mods):
        vocab_start_pages[v_idx + 1] = p_curr
        v_title = clean_mod_title(vm["title"])
        tiles = []
        for row in vm.get("table_rows", [])[:6]:
            pre, meaning, ex_sent = row[0], row[1], row[2]
            clean_pre = str(pre).strip()
            tiles.append((
                next_wide_photo(),
                f"{clean_pre} <span style='font-size:8pt;color:var(--muted);font-weight:500;'>({meaning})</span>",
                ex_sent
            ))
        v_body_1 = (
            K.page_title(f"Vocabulary Module {v_idx+1}: {v_title}",
                         kicker="Vocabulary in Use &bull; Visual Dictionary",
                         lead="High-utility vocabulary and structural patterns for Functional Skills Level 2 writing.")
            + spag_vocab_grid(tiles)
        )
        pages.append(K.page(v_body_1, header=(BOOK, f"Vocab Module {v_idx+1} &bull; Dictionary"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        drill_items = [
            (f"Write a workplace sentence demonstrating precise usage of <b>{vm['table_rows'][0][0]}</b> in a professional report.", 3),
            (f"Explain the exact nuance between <b>{vm['table_rows'][1][0]}</b> and a basic synonym in your own words.", 3),
            (f"Draft an email extract to a colleague incorporating at least two terms from Module {v_idx+1}.", 3),
        ]
        v_body_2 = (
            K.page_title(f"Module {v_idx+1} &bull; Applied Vocational Exercises",
                         kicker="Vocabulary in Use &bull; Practice Drills",
                         lead="Apply newly acquired vocabulary to authentic vocational contexts.")
            + K.exercise_list(drill_items)
            + K.fill_notes(f"Key Vocabulary Memory Box for Module {v_idx+1}", min_mm=26)
        )
        pages.append(K.page(v_body_2, header=(BOOK, f"Vocab Module {v_idx+1} &bull; Practice"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p71-82: 12 Forensic Proofreading Workouts (12 pages)
    workouts_start_page = p_curr
    workouts = dv_l2.MIXED_WORKOUTS
    for w_idx in range(12):
        w = workouts[w_idx % len(workouts)]
        w_title = w["title"]
        memo_text = K.clean_legacy(w.get("doc_text", ""))
        doc_heading = w.get("doc_title", "Workplace Document for Audit & Correction")
        focus = w.get("coverage", "Workplace Proofreading")
        body = (
            K.page_title(f"Workout {w_idx+1}: {w_title}",
                         kicker=f"Forensic Proofreading &bull; {focus}",
                         badge=w_idx+1)
            + K.box_html(memo_text, doc_heading)
            + K.table(["", "Error Identified in Text", "Professional Correction &amp; Rule"],
                      [[f"<b>{i}</b>", "<div style='height:8mm'></div>", ""] for i in range(1, 6)],
                      ["10mm", "45%", "45%"])
            + K.fill_notes("Key Examiner Learning Point &amp; Self-Check Reflection", 24)
        )
        pages.append(K.page(body, header=(BOOK, f"Proofreading Workout {w_idx+1}"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p83-88: 3 Workplace Writing Mock Exams (6 pages: 2 pages each)
    mocks_start_page = p_curr
    mocks = mk_l2.EXAM_MOCKS
    for m_idx, m in enumerate(mocks[:3]):
        m_title = m["title"]
        m_scenario = K.clean_legacy(m.get("scenario", ""))
        m_prompt = K.clean_legacy(m.get("writing_task_prompt", ""))
        m_marks = 15

        m_photo = next_wide_photo()
        m_body_1 = (
            K.page_title(f"Official Mock Writing Exam {m_idx+1}", kicker=f"Exam Practice &bull; {m_marks} Marks", badge=f"M{m_idx+1}")
            + spag_practice_banner(m_photo, f"Mock Writing Exam {m_idx+1}: {m_title}", height_mm=32)
            + K.box_html(f"<p>{m_scenario}</p><div style='margin-top:2mm;font-weight:700;'>Writing Task Prompt:</div><p>{m_prompt}</p>", f"Exam Scenario: {m_title}")
            + K.tip_pair("Plan your structure (Opening, 3 Core Paragraphs, Professional Close) before writing.",
                         "Check every comma splice, homophone, and apostrophe before concluding.",
                         golden_title="Band 4 Writing Checklist", watch_title="Examiner Audit Trap")
            + K.fill_lines("Candidate Initial Planning &amp; Outline Notes", min_mm=34, gap_mm=9.5)
        )
        pages.append(K.page(m_body_1, header=(BOOK, f"Mock Exam {m_idx+1} &bull; Briefing"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        m_body_2 = (
            K.page_title(f"Mock Exam {m_idx+1} &bull; Candidate Response Booklet", kicker="Official Ruled Response Page")
            + K.fill_lines("Write your response below:", min_mm=210, gap_mm=9.5)
        )
        pages.append(K.page(m_body_2, header=(BOOK, f"Mock Exam {m_idx+1} &bull; Response"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # Reference Back Matter via K.ref_pages (Granular blocks so 0 column overflows)
    ref_start_page = p_curr
    ref_blocks = []

    # 1. Diagnostic Assessment Solutions (split evenly into chunks of 10)
    p77 = mk_l2.ANSWER_KEYS_DATA.get('page_77', {})
    if 'diagnostic_answers' in p77:
        d_ans = p77['diagnostic_answers']
        chunk_sz = 10 if len(d_ans) > 10 else 5
        for c_start in range(0, len(d_ans), chunk_sz):
            c_slice = d_ans[c_start:c_start + chunk_sz]
            qa_html = "".join(f"<div class='qa'><span class='q-num'>Q{q}</span><span class='q-ans'><b>{ans}</b>: {escape_html(exp)}</span></div>" for q, ans, exp in c_slice)
            ref_blocks.append(K.ref_block(f"Diagnostic Solutions (Questions {c_start+1}–{c_start+len(c_slice)})", qa_html))

    # 2. Units 1 to 26 Worked Solutions (each unit is its own compact ref_block)
    for k in sorted(mk_l2.ANSWER_KEYS_DATA.keys()):
        data = mk_l2.ANSWER_KEYS_DATA[k]
        if 'units' in data:
            for unum, uinfo in sorted(data['units'].items()):
                ex_a = escape_html(uinfo.get('ex_a', ''))
                ex_b = escape_html(uinfo.get('ex_b', ''))
                u_html = f"<div style='margin-bottom:1.2mm;'><b>Section A (Drill):</b> {ex_a}</div><div><b>Section B (Rewrite):</b> {ex_b}</div>"
                ref_blocks.append(K.ref_block(f"Unit {unum} Worked Solutions", u_html))

    # 3. Vocab Modules (split into Modules 1-3 and Modules 4-6)
    p82 = mk_l2.ANSWER_KEYS_DATA.get('page_82', {})
    if 'vocab_modules' in p82:
        vm_items = sorted(p82['vocab_modules'].items())
        v1 = "".join(f"<div style='margin-bottom:1mm;'><b>Module {m}:</b> {escape_html(ans)}</div>" for m, ans in vm_items[:3])
        v2 = "".join(f"<div style='margin-bottom:1mm;'><b>Module {m}:</b> {escape_html(ans)}</div>" for m, ans in vm_items[3:])
        ref_blocks.append(K.ref_block("Vocabulary in Use Keys (Modules 1–3)", v1))
        ref_blocks.append(K.ref_block("Vocabulary in Use Keys (Modules 4–6)", v2))

    # 4. Forensic Proofreading Workouts (each workout is its own ref_block)
    if 'workouts' in p82:
        for w, ans in sorted(p82['workouts'].items()):
            ref_blocks.append(K.ref_block(f"Forensic Proofreading Workout {w} Key", f"<div>{escape_html(ans)}</div>"))

    # 5. Exam Mocks Proofreading (each mock is its own ref_block)
    if 'exam_mocks_proof_summary' in p82:
        for m, ans in sorted(p82['exam_mocks_proof_summary'].items()):
            ref_blocks.append(K.ref_block(f"Workplace Writing Mock {m} Mark Scheme", f"<div>{escape_html(ans)}</div>"))

    # 6. SPaG Glossary (split into 2 balanced blocks)
    glossary_l2 = [
        ("Active Voice", "Sentence structure where the subject performs the action (e.g. 'The manager approved the report')."),
        ("Passive Voice", "Sentence structure where the subject receives the action (e.g. 'The report was approved by the manager')."),
        ("Clause (Main / Independent)", "A group of words with a subject and finite verb that can stand alone as a complete sentence."),
        ("Clause (Subordinate / Dependent)", "A clause that provides extra context but cannot stand alone without an independent clause."),
        ("Comma Splice", "The error of joining two independent clauses with only a comma instead of a conjunction or semicolon."),
        ("Fragment", "An incomplete sentence lacking either a main verb or a subject."),
        ("Modal Verb", "An auxiliary verb indicating necessity, ability, or probability (e.g. must, should, would, could)."),
        ("Relative Pronoun", "A pronoun (who, which, that, whom, whose) introducing a relative clause."),
        ("Semicolon", "Punctuation mark (;) used to link closely related independent clauses or separate items in a complex list."),
        ("Subject-Verb Agreement", "The grammatical rule requiring singular subjects to take singular verbs and plural subjects to take plural verbs.")
    ]
    ref_blocks.append(K.ref_block(
        "Essential SPaG Glossary (A–F)",
        "".join(f"<dl><dt>{escape_html(t)}</dt><dd>{escape_html(d)}</dd></dl>" for t, d in glossary_l2[:6])
    ))
    ref_blocks.append(K.ref_block(
        "Essential SPaG Glossary (M–S)",
        "".join(f"<dl><dt>{escape_html(t)}</dt><dd>{escape_html(d)}</dd></dl>" for t, d in glossary_l2[6:])
    ))

    # 7. Index
    index_l2 = [
        ("A", [("Active and passive voice", "37"), ("Apostrophes for possession", "27"), ("Apostrophes for omission", "25")]),
        ("C", [("Colons in lists & explanations", "19"), ("Comma splices", "9"), ("Complex sentences", "43")]),
        ("D", [("Dashes and brackets", "21"), ("Dependent clauses", "43")]),
        ("F", [("FANBOYS conjunctions", "11"), ("Fragments", "7")]),
        ("H", [("Homophones & confusables", "51, 53"), ("Hyphens", "23")]),
        ("M", [("Modal verbs and diplomacy", "35"), ("Morphology (prefixes/suffixes)", "55")]),
        ("P", [("Parallel structure in lists", "47"), ("Parenthetical commas", "15")]),
        ("R", [("Register transformation", "49"), ("Relative clauses", "45")]),
        ("S", [("Semicolons", "17"), ("Subject-verb agreement", "39, 41")]),
        ("T", [("Tenses (past simple vs perfect)", "31, 33")])
    ]
    ix_html = ""
    for letter, entries in index_l2:
        items = "".join(f"<div class='ix'><span>{escape_html(t)}</span><span>p.{escape_html(p)}</span></div>" for t, p in entries)
        ix_html += f"<div class='ix-letter'>{letter}</div>{items}"
    ref_blocks.append(K.ref_block("Subject, Grammar &amp; Mechanics Index", ix_html))

    cover_theme = K.theme_from_cover(front_cov)
    ref_page_list = K.ref_pages("SPaG Level 2 Reference: Complete Solutions &amp; Index", ref_blocks,
                                BOOK, start_page=p_curr, subtitle="Worked Solutions, Glossary &amp; Index",
                                cols=2, theme=cover_theme, notes_title="Candidate SPaG Revision Log")
    pages.extend(ref_page_list)
    p_curr += len(ref_page_list)

    # Candidate Self-Audit Matrix
    audit_page_no = p_curr
    p_audit_body = (
        K.page_title("Candidate SPaG Self-Assessment Matrix &amp; Skill Audit", kicker="Final Independent Evaluation", badge="AUDIT")
        + K.box_html(
            "<p>Grade your SPaG accuracy against formal Pearson Edexcel Level 2 standards (Band 3 SPaG = 13–15 / 15 marks):</p>"
            + K.bullets([
                "<b>Punctuation Variety:</b> Full stops, commas in complex sentences, semicolons, colons, and apostrophes fully secure.",
                "<b>Grammar &amp; Syntax:</b> Zero comma splices or fragments; accurate subject-verb agreement across collective nouns.",
                "<b>Spelling:</b> Confident command of complex workplace vocabulary and confusable homophone pairs."
            ]),
            title="Pearson Edexcel Level 2 SPaG Benchmark Rubric"
        )
        + K.fill_notes("Personal Skill Progression &amp; Weakness Remediation Commitments", min_mm=45)
    )
    pages.append(K.page(p_audit_body, header=(BOOK, "Self-Assessment Matrix"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Duplex even-page balance check before back cover
    if (len(pages) + 1) % 2 != 0:
        p_ibc_body = (
            K.page_title("Candidate SPaG Commitment &amp; Tutor Endorsement", kicker="Mastery Sign-Off &bull; Professional Development", badge="SIGN")
            + K.box_html(
                "<p>Confirm your ongoing commitment to professional standards of spelling, punctuation, and grammar:</p>"
                + K.bullets([
                    "<b>Daily Accuracy:</b> Apply the Golden Rules across all workplace emails, incident logs, and technical reports.",
                    "<b>Active Demarcation:</b> Maintain zero tolerance for comma splices, sentence fragments, and apostrophe slips.",
                    "<b>Lifelong Lexicon:</b> Continuously expand vocational vocabulary and cross-reference authoritative dictionaries."
                ]),
                title="Professional Literacy Declaration"
            )
            + K.tip_pair("Keep this mastery guide at your workstation as a permanent syntax and punctuation quick-reference.",
                         "Consistent accuracy in workplace correspondence builds professional credibility and authority.",
                         golden_title="Career Impact", watch_title="Best Practice")
            + K.fill_notes("Tutor Endorsement &amp; Candidate Next Steps", min_mm=30)
        )
        pages.append(K.page(p_ibc_body, header=(BOOK, "Tutor Endorsement"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # Populate p2: 2-Column Table of Contents
    toc_left = [
        ("DIAG", "Diagnostic Audit &amp; Routing", [
            ("D1–D4", "Baseline Diagnostic Assessment (Q1–Q10)", "3"),
        ]),
        ("U1–U18", "Grammar in Use Units (Part 1)", [
            (f"U{u['unit']}", u["title"], str(unit_start_pages[u["unit"]]))
            for u in all_units[:18]
        ]),
    ]
    toc_right = [
        ("U19–U26", "Grammar in Use Units (Part 2)", [
            (f"U{u['unit']}", u["title"], str(unit_start_pages[u["unit"]]))
            for u in all_units[18:]
        ]),
        ("VOCAB", "Visual Vocabulary in Use Modules (V1–V6)", [
            (f"V{i+1}", clean_mod_title(vocab_mods[i]["title"]), str(vocab_start_pages[i+1]))
            for i in range(len(vocab_mods))
        ]),
        ("DRILLS", "Proofreading Workouts &amp; Mock Exams", [
            ("W1–W12", "12 Forensic Proofreading Workouts", str(workouts_start_page)),
            ("M1–M3", "3 Workplace Writing Mock Examinations", str(mocks_start_page)),
        ]),
        ("REF", "Solutions, Glossary, Index &amp; Audit", [
            ("SOL", "Diagnostic, Unit 1–26 &amp; Workout Keys", str(ref_start_page)),
            ("AUDIT", "Candidate SPaG Self-Assessment Matrix", str(audit_page_no)),
        ]),
    ]
    pages[1] = spag_toc_page(
        "SPaG Level 2 Mastery",
        "The Complete 2-Page Spread Grammar, Punctuation &amp; Vocabulary Workbook",
        toc_left, toc_right, BOOK
    )

    # Back Cover
    pages.append(K.back_cover(back_cov))

    print(f"Total Pages Assembled: {len(pages)}")
    out_pdf = DOWNLOADS / "MasterFunctionalSkills_SPaG_Level_2_Mastery.pdf"
    res = K.render_pdf(pages, out_pdf, theme=cover_theme, entry3=False, title="Master Functional Skills - SPaG Level 2 Mastery")
    shutil.copyfile(out_pdf, DOCUMENTS / out_pdf.name)
    print(f"Rendered: {res['pdf']} | Overflows: {res.get('overflow', [])}")
    return res


# =============================================================================
# 2. SPaG Level 1 Mastery
# =============================================================================
def build_spag_l1():
    print("\n" + "="*70)
    print("BUILDING: MasterFunctionalSkills_SPaG_Level_1_Mastery.pdf")
    print("="*70)

    BOOK = "SPaG Level 1 Mastery"
    front_cov = COV / "spag_l1_mastery_cover-01.png"
    back_cov = COV / "spag_l1_mastery_cover-02.png"

    all_units = u_l1.L1_UNITS_26
    pages = []
    photo_cursor = [18]  # Offset into WIDE_THEMATIC_POOL for variety

    def next_wide_photo():
        rel = WIDE_THEMATIC_POOL[photo_cursor[0] % len(WIDE_THEMATIC_POOL)]
        photo_cursor[0] += 1
        return rel

    # p1: Front Cover
    pages.append(K.front_cover(front_cov))

    # p2: Placeholder for 2-Column Table of Contents
    pages.append(None)

    # p3-6: Diagnostic Assessment (4 pages, 10 authentic questions total)
    diag_qs = spag_data_l1.L1_DIAGNOSTIC["questions"]
    scoring_rows = spag_data_l1.L1_DIAGNOSTIC["scoring"]

    def make_ex_items(qs):
        items = []
        for q in qs:
            clean_opts = [o[3:] if len(o) > 3 and o[1] == ")" else o for o in q["options"]]
            pr = q.get("prompt", "")
            top = q.get("topic", "")
            items.append({
                "q": f"<b>{pr}</b> <span style='font-size:10pt;color:var(--muted);font-weight:400;'>({top})</span>",
                "options": clean_opts,
                "marks": 1
            })
        return items

    pages.append(K.page(
        K.page_title("Baseline Diagnostic Assessment &bull; Part 1 of 4",
                     kicker="Diagnostic Audit &bull; Questions 1&ndash;3",
                     lead="Answer each question carefully. Circle your chosen answer. Do not use a dictionary.")
        + K.exercise_list(make_ex_items(diag_qs[0:3]), start=1)
        + K.fill_notes("Examiner Checkpoint &bull; Questions 1 to 3 Notes", min_mm=30),
        header=(BOOK, "Diagnostic 1/4"), footer=BOOK, page_no=3
    ))

    pages.append(K.page(
        K.page_title("Baseline Diagnostic Assessment &bull; Part 2 of 4",
                     kicker="Diagnostic Audit &bull; Questions 4&ndash;6",
                     lead="Identify correct capitalisation, punctuation, and sentence construction.")
        + K.exercise_list(make_ex_items(diag_qs[3:6]), start=4)
        + K.fill_notes("Examiner Checkpoint &bull; Questions 4 to 6 Notes", min_mm=30),
        header=(BOOK, "Diagnostic 2/4"), footer=BOOK, page_no=4
    ))

    score_table = """<div class="box" style="padding:2.5mm 3.5mm;background:#fff;border:1.5px solid var(--soft);margin-top:2mm;">
      <div style="font-weight:700;color:var(--primary);font-size:11pt;margin-bottom:1.5mm;">Diagnostic Performance Matrix &amp; Recommended Study Pathway</div>
      <table style="width:100%;border-collapse:collapse;font-size:9.6pt;">
        <thead>
          <tr style="background:var(--light);color:var(--primary);text-align:left;">
            <th style="padding:1.5mm;border:1px solid var(--soft);">Score Range</th>
            <th style="padding:1.5mm;border:1px solid var(--soft);">Readiness Level</th>
            <th style="padding:1.5mm;border:1px solid var(--soft);">Recommended Curriculum Route</th>
          </tr>
        </thead>
        <tbody>"""
    for row in scoring_rows:
        score_table += f"""
          <tr>
            <td style="padding:1.5mm;border:1px solid var(--soft);font-weight:700;">{row['range']}</td>
            <td style="padding:1.5mm;border:1px solid var(--soft);color:var(--accent);font-weight:600;">{row['status']}</td>
            <td style="padding:1.5mm;border:1px solid var(--soft);">{row['advice']}</td>
          </tr>"""
    score_table += """</tbody></table></div>"""

    pages.append(K.page(
        K.page_title("Baseline Diagnostic Assessment &bull; Part 3 of 4",
                     kicker="Diagnostic Audit &bull; Questions 7&ndash;8",
                     lead="Grammar and syntax accuracy questions, followed by the diagnostic benchmark rubric.")
        + K.exercise_list(make_ex_items(diag_qs[6:8]), start=7)
        + score_table
        + K.fill_notes("Personal Learning Target &amp; Study Priority", min_mm=24),
        header=(BOOK, "Diagnostic 3/4"), footer=BOOK, page_no=5
    ))

    pages.append(K.page(
        K.page_title("Baseline Diagnostic Assessment &bull; Part 4 of 4",
                     kicker="Diagnostic Audit &bull; Questions 9&ndash;10 &amp; Study Plan",
                     lead="Final practical diagnostic questions and your personalised revision action plan.")
        + K.exercise_list(make_ex_items(diag_qs[8:10]), start=9)
        + K.tip_pair("Check your diagnostic score against the answer keys in the Reference Section.",
                     "Prioritise the specific units flagged in questions you found challenging.",
                     golden_title="Tutor Golden Rule", watch_title="Revision Target")
        + K.fill_lines("Candidate Action Plan &amp; Priority Units to Master", min_mm=30, gap_mm=9.5),
        header=(BOOK, "Diagnostic 4/4"), footer=BOOK, page_no=6
    ))

    # p7-58: 26 Units (52 pages)
    characters = [
        ("Abdul", "abdul tutor man", "#0c4a6e"),
        ("Priya", "priya tutor woman", "#7c3aed"),
        ("Marcus", "marcus apprentice", "#0d9488"),
        ("Sarah", "sarah care nurse", "#be123c"),
        ("Sam", "sam learner thinking", "#475569"),
    ]

    p_curr = 7
    unit_start_pages = {}
    for u_idx, u in enumerate(all_units):
        u_num = u["unit"]
        unit_start_pages[u_num] = p_curr
        char_name, char_kw, char_col = characters[u_idx % len(characters)]

        # --- Left Page: Learn ---
        anchor_title = u.get("anchor_title", "Everyday Communication")
        if len(anchor_title) > 90:
            anchor_title = anchor_title[:87] + "..."
        rule_title = u.get("rule_formula_title", "Core Grammar Rule &amp; Sentence Pattern")
        rule_text = K.clean_legacy(u.get("rule_formula_html", ""))
        bad_text = u.get("worked_bad", "Example with error.")
        good_text = u.get("worked_good", "Corrected example.")
        why_text = u.get("worked_why", "Grammar rule explanation.")

        is_long = (u_num in (6, 11, 23, 25)) or (len(rule_text) > 950)
        font_sz = "8.8pt" if is_long else ("9.4pt" if len(rule_text) > 750 else "9.8pt")
        lh = "1.14" if is_long else ("1.18" if len(rule_text) > 750 else "1.22")
        bubble_h = 44 if is_long else 48
        cmp_sz = "8.8pt" if is_long else "9.4pt"
        pad_v = "1.0mm" if is_long else "1.5mm"

        left_body = (
            K.page_title(u["title"], kicker=f"Unit {u_num} &bull; Core Foundations", badge=u_num)
            + K.character_bubble(
                K.cartoon(char_kw), char_name,
                f"<b style='color:var(--accent)'>A &nbsp;The Concept in Everyday Use:</b> {anchor_title}",
                "left", bubble_h, char_col
            )
            + f"""<div class="box rule" style="flex:1 1 auto;padding:{pad_v} 3.5mm;font-size:{font_sz};line-height:{lh};">
                <div class="bt" style="margin-bottom:1mm;"><span class="ico">&#9733;</span>B &nbsp;{rule_title}</div>
                <div style="font-size:{font_sz};">{rule_text}</div>
              </div>"""
            + K.compare(
                f"<div style='font-size:{cmp_sz};line-height:1.2;'>{bad_text}</div>",
                f"<div style='font-size:{cmp_sz};line-height:1.2;'>{good_text}</div><div style='font-size:9pt;color:var(--muted);margin-top:1mm;'><b>Why:</b> {why_text}</div>",
                stacked=False, bad_label="&#10007; Common Mistake", good_label="&#10003; Correct Sentence"
            )
        )
        pages.append(K.page(left_body, header=(BOOK, f"Unit {u_num} &bull; Learn"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # --- Right Page: Practise (with wide-angle thematic photo banner & 1-line caption) ---
        ex_a_items = []
        for q_tuple in u.get("exercise_a", [])[:2]:
            q_text, opts = q_tuple[0], q_tuple[1]
            clean_opts = [o[3:] if len(o) > 3 and o[1] == ")" else o for o in opts]
            ex_a_items.append({"q": q_text, "options": clean_opts})

        ex_b_items = []
        for b_tuple in u.get("exercise_b", [])[:2]:
            prompt_type, original = b_tuple[0], b_tuple[1]
            ex_b_items.append((f"<b>[{prompt_type}]:</b> <i>{original}</i>", 2))

        u_photo = next_wide_photo()
        u_cap = f"Unit {u_num} Practical Scenario ({u.get('anchor_title', u['title'])}): Practising {u['title']}."
        right_body = (
            K.section("A", "Tick the correct sentence")
            + spag_float_practice_card(u_photo, u_cap, width_mm=60)
            + K.exercise_list(ex_a_items)
            + "<div style='clear:both;'></div>"
            + K.section("B", "Rewrite each sentence correctly")
            + K.exercise_list(ex_b_items, start=3)
            + K.fill_lines(f"<span style='color:var(--accent)'>C &nbsp;Applied Practice:</span> Write two sentences of your own using the rules from Unit {u_num}.", min_mm=14, gap_mm=8.0)
        )
        pages.append(K.page(right_body, header=(BOOK, f"Unit {u_num} &bull; Practise"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p59-70: 6 Vocab in Use Modules (12 pages: 2 pages each)
    vocab_start_pages = {}
    vocab_mods = d_l1.VOCAB_MODULES
    for v_idx, vm in enumerate(vocab_mods):
        vocab_start_pages[v_idx + 1] = p_curr
        v_title = clean_mod_title(vm["title"])
        table_rows = vm["tables"][0]["rows"]
        tiles = []
        for row in table_rows[:6]:
            pre, meaning, ex_sent = row[0], row[1], row[2]
            clean_pre = str(pre).strip()
            tiles.append((
                next_wide_photo(),
                f"<b>{clean_pre}</b> &rarr; <span style='color:var(--accent);'>{meaning}</span>",
                ex_sent
            ))
        v_body_1 = (
            K.page_title(f"Vocabulary Module {v_idx+1}: {v_title}",
                         kicker="Vocabulary in Use &bull; Visual Dictionary",
                         lead=vm.get("intro", "Essential words and spelling patterns for Functional Skills Level 1 English."))
            + spag_vocab_grid(tiles)
        )
        pages.append(K.page(v_body_1, header=(BOOK, f"Vocab Module {v_idx+1} &bull; Dictionary"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        drill_data = vm.get("drill", {})
        drill_items = [
            (f"<b>Vocabulary Drill:</b> {drill_data.get('prompt', 'Transform into professional English:')}<br><i>'{drill_data.get('bad', '')}'</i>", 3),
            (f"Write a workplace sentence demonstrating correct usage of <b>{table_rows[0][1]}</b>.", 3),
            (f"Write a message to a colleague using at least two formal words from Module {v_idx+1}.", 3),
        ]
        v_body_2 = (
            K.page_title(f"Module {v_idx+1} &bull; Applied Vocational Drills",
                         kicker="Vocabulary in Use &bull; Practice Drills",
                         lead="Practise using these key words in everyday and work situations.")
            + K.exercise_list(drill_items)
            + K.fill_notes(f"Word Study &amp; Spelling Memory Box for Module {v_idx+1}", min_mm=26)
        )
        pages.append(K.page(v_body_2, header=(BOOK, f"Vocab Module {v_idx+1} &bull; Practice"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p71-82: 12 Mixed Proofreading Workouts (12 pages)
    workouts_start_page = p_curr
    workouts = d_l1.MIXED_WORKOUTS
    for w_idx in range(12):
        w = workouts[w_idx % len(workouts)]
        w_title = w["title"]
        memo_text = K.clean_legacy(w.get("doc_text", ""))
        doc_heading = w.get("doc_title", "Everyday Document for Proofreading")
        focus = w.get("coverage", "Practical Proofreading")
        body = (
            K.page_title(f"Workout {w_idx+1}: {w_title}",
                         kicker=f"Proofreading Practice &bull; {focus}",
                         badge=w_idx+1)
            + K.box_html(memo_text, doc_heading)
            + K.table(["", "Error Found in Text", "Correction &amp; Rule"],
                      [[f"<b>{i}</b>", "<div style='height:8mm'></div>", ""] for i in range(1, 6)],
                      ["10mm", "45%", "45%"])
            + K.fill_notes("Key Learning Rule to Remember", 24)
        )
        pages.append(K.page(body, header=(BOOK, f"Proofreading Workout {w_idx+1}"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p83-88: 3 Mock Writing Exam Papers (6 pages: 2 pages each)
    mocks_start_page = p_curr
    mocks = d_l1.EXAM_MOCKS
    for m_idx, m in enumerate(mocks[:3]):
        m_title = m["title"]
        m_scenario = K.clean_legacy(m.get("scenario", ""))
        m_prompt = K.clean_legacy(m.get("writing_task_prompt", ""))
        m_marks = 12

        m_photo = next_wide_photo()
        m_body_1 = (
            K.page_title(f"Official Mock Writing Exam {m_idx+1}", kicker=f"Exam Practice &bull; {m_marks} Marks", badge=f"M{m_idx+1}")
            + spag_practice_banner(m_photo, f"Mock Writing Exam {m_idx+1}: {m_title}", height_mm=32)
            + K.box_html(f"<p>{m_scenario}</p><div style='margin-top:2mm;font-weight:700;'>Your Writing Task:</div><p>{m_prompt}</p>", f"Task: {m_title}")
            + K.tip_pair("Plan your ideas in 2–3 short paragraphs before starting.",
                         "Check capital letters for 'I', names, and days of the week.",
                         golden_title="Level 1 Success Checklist", watch_title="Common Slip")
            + K.fill_lines("Candidate Notes &amp; Word Plan", min_mm=34, gap_mm=9.5)
        )
        pages.append(K.page(m_body_1, header=(BOOK, f"Mock Exam {m_idx+1} &bull; Briefing"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        m_body_2 = (
            K.page_title(f"Mock Exam {m_idx+1} &bull; Candidate Response Booklet", kicker="Official Ruled Response Page")
            + K.fill_lines("Write your response below:", min_mm=210, gap_mm=9.5)
        )
        pages.append(K.page(m_body_2, header=(BOOK, f"Mock Exam {m_idx+1} &bull; Response"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # Reference Back Matter via K.ref_pages (Granular blocks so 0 overflows)
    ref_start_page = p_curr
    ref_blocks = []

    # 1. Diagnostic Assessment Solutions (split evenly into chunks)
    p77 = d_l1.ANSWER_KEYS_6P.get('page_77', {})
    if 'diagnostic_answers' in p77:
        d_ans = p77['diagnostic_answers']
        chunk_sz = 10 if len(d_ans) > 10 else 5
        for c_start in range(0, len(d_ans), chunk_sz):
            c_slice = d_ans[c_start:c_start + chunk_sz]
            qa_html = "".join(f"<div class='qa'><span class='q-num'>Q{c_start+i+1}</span><span class='q-ans'>{escape_html(ans)}</span></div>" for i, ans in enumerate(c_slice))
            ref_blocks.append(K.ref_block(f"Diagnostic Solutions (Questions {c_start+1}–{c_start+len(c_slice)})", qa_html))

    # 2. Units 1 to 26 Worked Solutions (each unit is its own ref_block)
    for k in sorted(d_l1.ANSWER_KEYS_6P.keys()):
        data = d_l1.ANSWER_KEYS_6P[k]
        if 'units' in data:
            for unum, uinfo in sorted(data['units'].items()):
                ex_a = escape_html(uinfo.get('ex_a', ''))
                ex_b = escape_html(uinfo.get('ex_b', ''))
                u_html = f"<div style='margin-bottom:1.2mm;'><b>Section A (Drill):</b> {ex_a}</div><div><b>Section B (Rewrite):</b> {ex_b}</div>"
                ref_blocks.append(K.ref_block(f"Unit {unum} Worked Solutions", u_html))

    # 3. Vocab Modules (split into Modules 1-3 and Modules 4-6)
    p81 = d_l1.ANSWER_KEYS_6P.get('page_81', {})
    if 'vocab_modules' in p81:
        vm_items = sorted(p81['vocab_modules'].items())
        v1 = "".join(f"<div style='margin-bottom:1mm;'><b>Module {m}:</b> {escape_html(ans)}</div>" for m, ans in vm_items[:3])
        v2 = "".join(f"<div style='margin-bottom:1mm;'><b>Module {m}:</b> {escape_html(ans)}</div>" for m, ans in vm_items[3:])
        ref_blocks.append(K.ref_block("Vocabulary in Use Keys (Modules 1–3)", v1))
        ref_blocks.append(K.ref_block("Vocabulary in Use Keys (Modules 4–6)", v2))

    # 4. Mixed Proofreading Workouts (each workout is its own ref_block)
    p82 = d_l1.ANSWER_KEYS_6P.get('page_82', {})
    if 'mixed_workouts' in p82:
        for w, ans in sorted(p82['mixed_workouts'].items()):
            if isinstance(ans, dict):
                p_a = f"<div><b>Part A:</b> {escape_html(ans.get('part_a', ''))}</div>" if 'part_a' in ans else ""
                p_b = f"<div><b>Part B:</b> {escape_html(ans.get('part_b', ''))}</div>" if 'part_b' in ans else ""
                p_c = f"<div><b>Part C:</b> {escape_html(ans.get('part_c', ''))}</div>" if 'part_c' in ans else ""
                ref_blocks.append(K.ref_block(f"Mixed Proofreading Workout {w} Key", f"{p_a}{p_b}{p_c}"))
            else:
                ref_blocks.append(K.ref_block(f"Mixed Proofreading Workout {w} Key", f"<div>{escape_html(ans)}</div>"))

    # 5. Exam Mocks Proofreading (each mock is its own ref_block)
    if 'exam_mocks' in p82:
        for m, ans in sorted(p82['exam_mocks'].items()):
            if isinstance(ans, dict):
                p_ans = "<br>".join(escape_html(p) for p in ans.get('proof_answers', []))
                rub = f"<div style='margin-top:1mm;'><em>Rubric:</em> {escape_html(ans.get('writing_rubric', ''))}</div>" if 'writing_rubric' in ans else ""
                ref_blocks.append(K.ref_block(f"Mock Writing Exam {m} Mark Scheme", f"<div>{p_ans}</div>{rub}"))
            else:
                ref_blocks.append(K.ref_block(f"Mock Writing Exam {m} Mark Scheme", f"<div>{escape_html(ans)}</div>"))

    # 6. SPaG Glossary (split into 2 balanced blocks)
    glossary_l1 = [
        ("Capital Letter", "Used at the start of every sentence, for the word 'I', people's names, places, days, and months."),
        ("Full Stop", "Punctuation mark (.) used to mark the end of a complete statement."),
        ("Question Mark", "Punctuation mark (?) used at the end of a direct question."),
        ("Exclamation Mark", "Punctuation mark (!) used to show strong feeling, surprise, or urgency."),
        ("Comma in Lists", "Used to separate items in a list (e.g. 'paper, pens, and pencils')."),
        ("Conjunction", "A linking word used to join two clauses (e.g. and, but, so, because, although)."),
        ("Past Tense", "Verb forms used to describe things that happened yesterday or in the past (e.g. walked, saw)."),
        ("Present Tense", "Verb forms used for things happening now or regularly (e.g. walks, sees)."),
        ("Subject-Verb Agreement", "Matching singular subjects with singular verbs (e.g. 'He works' vs 'They work')."),
        ("Homophone", "Words that sound the same but have different spellings and meanings (e.g. there, their, they're).")
    ]
    ref_blocks.append(K.ref_block(
        "Functional Skills SPaG Glossary (Part 1)",
        "".join(f"<dl><dt>{escape_html(t)}</dt><dd>{escape_html(d)}</dd></dl>" for t, d in glossary_l1[:5])
    ))
    ref_blocks.append(K.ref_block(
        "Functional Skills SPaG Glossary (Part 2)",
        "".join(f"<dl><dt>{escape_html(t)}</dt><dd>{escape_html(d)}</dd></dl>" for t, d in glossary_l1[5:])
    ))

    # 7. Index
    index_l1 = [
        ("A", [("Apostrophes for contractions", "21"), ("Apostrophes for possession", "23, 29")]),
        ("C", [("Capital letters (MINTS)", "7, 11"), ("Commas in lists", "17"), ("Conjunctions", "13, 15")]),
        ("E", [("Ending sentences (. ! ?)", "7, 9"), ("Exclamation marks", "9")]),
        ("F", [("Future intentions (will/going to)", "39")]),
        ("H", [("Homophones (there/their/to/two)", "49, 51, 53")]),
        ("P", [("Past tense regular & irregular", "35, 37"), ("Plural nouns", "25, 27"), ("Prefixes", "55")]),
        ("Q", [("Question marks", "9")]),
        ("S", [("Subject-verb agreement", "41, 43"), ("Suffixes (-ful, -less, -ly)", "57")]),
        ("T", [("Tenses (present simple/continuous)", "31, 33")])
    ]
    ix_html = ""
    for letter, entries in index_l1:
        items = "".join(f"<div class='ix'><span>{escape_html(t)}</span><span>p.{escape_html(p)}</span></div>" for t, p in entries)
        ix_html += f"<div class='ix-letter'>{letter}</div>{items}"
    ref_blocks.append(K.ref_block("Subject &amp; Mechanics Index", ix_html))

    cover_theme = K.theme_from_cover(front_cov)
    ref_page_list = K.ref_pages("SPaG Level 1 Reference: Solutions &amp; Index", ref_blocks,
                                BOOK, start_page=p_curr, subtitle="Worked Solutions, Glossary &amp; Index",
                                cols=2, theme=cover_theme, notes_title="Candidate SPaG Revision Log")
    pages.extend(ref_page_list)
    p_curr += len(ref_page_list)

    # Candidate Self-Audit Matrix
    audit_page_no = p_curr
    p_audit_body = (
        K.page_title("Candidate SPaG Self-Assessment Matrix &amp; Progress Chart", kicker="Level 1 SPaG Standards", badge="AUDIT")
        + K.box_html(
            "<p>Check off your skills against Pearson Edexcel Level 1 standards:</p>"
            + K.bullets([
                "Write clearly in full sentences with capital letters and full stops.",
                "Use commas accurately in lists and conjunctions to join ideas.",
                "Spell everyday workplace words correctly using Annexe D rules."
            ]),
            title="Pearson Edexcel Level 1 SPaG Rubric"
        )
        + K.fill_notes("Personal Progress &amp; Weakness Remediation Log", min_mm=45)
    )
    pages.append(K.page(p_audit_body, header=(BOOK, "Self-Assessment Matrix"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Duplex even-page balance check before back cover
    if (len(pages) + 1) % 2 != 0:
        p_ibc_body = (
            K.page_title("Candidate SPaG Commitment &amp; Tutor Endorsement", kicker="Level 1 SPaG Sign-Off", badge="SIGN")
            + K.box_html(
                "<p>Confirm your ongoing commitment to professional standards of spelling, punctuation, and grammar:</p>"
                + K.bullets([
                    "<b>Accurate Demarcation:</b> Always start every sentence with a capital letter and end with a full stop.",
                    "<b>Comma Precision:</b> Use commas accurately in lists and after introductory connective phrases.",
                    "<b>Everyday Spelling:</b> Confidently spell core vocational vocabulary without phonics slips."
                ]),
                title="Level 1 Professional Literacy Declaration"
            )
            + K.tip_pair("Re-read all completed written work before submitting to catch missing punctuation.",
                         "Accurate spelling and clear sentences ensure your workplace messages are understood first time.",
                         golden_title="Audit Habit", watch_title="Workplace Value")
            + K.fill_notes("Tutor Endorsement &amp; Candidate Next Steps", min_mm=30)
        )
        pages.append(K.page(p_ibc_body, header=(BOOK, "Tutor Endorsement"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # Populate p2: 2-Column Table of Contents
    toc_left = [
        ("DIAG", "Diagnostic Audit &amp; Routing", [
            ("D1–D4", "Baseline Diagnostic Assessment (Q1–Q10)", "3"),
        ]),
        ("U1–U18", "Grammar in Use Units (Part 1)", [
            (f"U{u['unit']}", u["title"], str(unit_start_pages[u["unit"]]))
            for u in all_units[:18]
        ]),
    ]
    toc_right = [
        ("U19–U26", "Grammar in Use Units (Part 2)", [
            (f"U{u['unit']}", u["title"], str(unit_start_pages[u["unit"]]))
            for u in all_units[18:]
        ]),
        ("VOCAB", "Visual Vocabulary in Use Modules (V1–V6)", [
            (f"V{i+1}", clean_mod_title(vocab_mods[i]["title"]), str(vocab_start_pages[i+1]))
            for i in range(len(vocab_mods))
        ]),
        ("DRILLS", "Proofreading Workouts &amp; Mock Exams", [
            ("W1–W12", "12 Practical Proofreading Workouts", str(workouts_start_page)),
            ("M1–M3", "3 Workplace Writing Mock Examinations", str(mocks_start_page)),
        ]),
        ("REF", "Solutions, Glossary, Index &amp; Audit", [
            ("SOL", "Diagnostic, Unit 1–26 &amp; Workout Keys", str(ref_start_page)),
            ("AUDIT", "Candidate SPaG Self-Assessment Matrix", str(audit_page_no)),
        ]),
    ]
    pages[1] = spag_toc_page(
        "SPaG Level 1 Mastery",
        "Core Principles, Everyday Work Scenarios &amp; Applied Practice Workbook",
        toc_left, toc_right, BOOK
    )

    # Back Cover
    pages.append(K.back_cover(back_cov))

    print(f"Total Pages Assembled: {len(pages)}")
    out_pdf = DOWNLOADS / "MasterFunctionalSkills_SPaG_Level_1_Mastery.pdf"
    res = K.render_pdf(pages, out_pdf, theme=cover_theme, entry3=False, title="Master Functional Skills - SPaG Level 1 Mastery")
    shutil.copyfile(out_pdf, DOCUMENTS / out_pdf.name)
    print(f"Rendered: {res['pdf']} | Overflows: {res.get('overflow', [])}")
    return res


# =============================================================================
# 3. SPaG Entry Level 3 Mastery
# =============================================================================
def build_spag_e3():
    print("\n" + "="*70)
    print("BUILDING: MasterFunctionalSkills_SPaG_Entry_Level_3_Mastery.pdf")
    print("="*70)

    BOOK = "SPaG Entry Level 3 Mastery"
    front_cov = COV / "spag_e3_mastery_cover-01.png"
    back_cov = COV / "spag_e3_mastery_cover-02.png"

    all_units = u_e3.units_data
    pages = []
    photo_cursor = [56]  # Offset into WIDE_THEMATIC_POOL starting at e3_thematic!

    def next_wide_photo():
        rel = WIDE_THEMATIC_POOL[photo_cursor[0] % len(WIDE_THEMATIC_POOL)]
        photo_cursor[0] += 1
        return rel

    # p1: Front Cover
    pages.append(K.front_cover(front_cov))

    # p2: Placeholder for 2-Column Table of Contents
    pages.append(None)

    # p3-6: Diagnostic Assessment (4 pages, 10 authentic questions total)
    diag_qs = d_e3.DIAGNOSTIC_QUESTIONS

    def make_ex_items(qs):
        items = []
        for q in qs:
            clean_opts = [o[3:] if len(o) > 3 and o[1] == ')' else o for o in q["options"]]
            q_text = q.get("question") or q.get("prompt", "")
            items.append({
                "q": f"<b>{q_text}</b>",
                "options": clean_opts,
                "marks": 1
            })
        return items

    pages.append(K.page(
        K.page_title("Visual Diagnostic Assessment &bull; Part 1 of 4",
                     kicker="Entry Level 3 &bull; Questions 1&ndash;3",
                     lead="Tick the best answer for each question. Circle your chosen answer. Do not use a dictionary.")
        + K.exercise_list(make_ex_items(diag_qs[0:3]), start=1)
        + K.fill_notes("Tutor Diagnostic Notes &bull; Questions 1 to 3", min_mm=30),
        header=(BOOK, "Diagnostic 1/4"), footer=BOOK, page_no=3
    ))

    pages.append(K.page(
        K.page_title("Visual Diagnostic Assessment &bull; Part 2 of 4",
                     kicker="Entry Level 3 &bull; Questions 4&ndash;6",
                     lead="Identify correct capitalisation, punctuation, and sentence construction.")
        + K.exercise_list(make_ex_items(diag_qs[3:6]), start=4)
        + K.fill_notes("Tutor Diagnostic Notes &bull; Questions 4 to 6", min_mm=30),
        header=(BOOK, "Diagnostic 2/4"), footer=BOOK, page_no=4
    ))

    score_table = """<div class="box" style="padding:2.5mm 3.5mm;background:#fff;border:1.5px solid var(--soft);margin-top:2mm;">
      <div style="font-weight:700;color:var(--primary);font-size:11pt;margin-bottom:1.5mm;">Diagnostic Performance Matrix &amp; Study Pathway</div>
      <table style="width:100%;border-collapse:collapse;font-size:9.6pt;">
        <thead>
          <tr style="background:var(--light);color:var(--primary);text-align:left;">
            <th style="padding:1.5mm;border:1px solid var(--soft);">Score</th>
            <th style="padding:1.5mm;border:1px solid var(--soft);">Readiness Level</th>
            <th style="padding:1.5mm;border:1px solid var(--soft);">Recommended Curriculum Route</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td style="padding:1.5mm;border:1px solid var(--soft);font-weight:700;">8&ndash;10</td>
            <td style="padding:1.5mm;border:1px solid var(--soft);color:var(--accent);font-weight:600;">Entry 3 Confident</td>
            <td style="padding:1.5mm;border:1px solid var(--soft);">Consolidate compound sentences and prepare for Level 1 progression.</td>
          </tr>
          <tr>
            <td style="padding:1.5mm;border:1px solid var(--soft);font-weight:700;">5&ndash;7</td>
            <td style="padding:1.5mm;border:1px solid var(--soft);color:var(--accent);font-weight:600;">Developing Skill</td>
            <td style="padding:1.5mm;border:1px solid var(--soft);">Work systematically through Units 1 to 24 with tutor check-ins.</td>
          </tr>
          <tr>
            <td style="padding:1.5mm;border:1px solid var(--soft);font-weight:700;">0&ndash;4</td>
            <td style="padding:1.5mm;border:1px solid var(--soft);color:var(--accent);font-weight:600;">Foundational Support</td>
            <td style="padding:1.5mm;border:1px solid var(--soft);">Focus on high-frequency word banks and capital letters first.</td>
          </tr>
        </tbody></table></div>"""

    pages.append(K.page(
        K.page_title("Visual Diagnostic Assessment &bull; Part 3 of 4",
                     kicker="Entry Level 3 &bull; Questions 7&ndash;8",
                     lead="Grammar and punctuation check, followed by your diagnostic pathway matrix.")
        + K.exercise_list(make_ex_items(diag_qs[6:8]), start=7)
        + score_table
        + K.fill_notes("Personal Learning Target &amp; Study Priority", min_mm=24),
        header=(BOOK, "Diagnostic 3/4"), footer=BOOK, page_no=5
    ))

    pages.append(K.page(
        K.page_title("Visual Diagnostic Assessment &bull; Part 4 of 4",
                     kicker="Entry Level 3 &bull; Questions 9&ndash;10 &amp; Study Plan",
                     lead="Final diagnostic questions and your personalised study action plan.")
        + K.exercise_list(make_ex_items(diag_qs[8:10]), start=9)
        + K.tip_pair("Check your diagnostic answers with your tutor or in the Reference Section.",
                     "Mark the units you need to practise first on your progress chart.",
                     golden_title="Tutor Golden Rule", watch_title="Next Steps")
        + K.fill_lines("Candidate Action Plan &amp; Priority Units to Master", min_mm=30, gap_mm=9.5),
        header=(BOOK, "Diagnostic 4/4"), footer=BOOK, page_no=6
    ))

    # p7-54: 24 Units (48 pages)
    characters = [
        ("Abdul", "abdul tutor man", "#0c4a6e"),
        ("Sarah", "sarah care nurse", "#be123c"),
        ("Marcus", "marcus apprentice", "#0d9488"),
        ("Priya", "priya tutor woman", "#7c3aed"),
        ("Sam", "sam learner thinking", "#475569"),
    ]

    p_curr = 7
    unit_start_pages = {}
    for u_idx, u in enumerate(all_units):
        u_num = u["unit"]
        unit_start_pages[u_num] = p_curr
        char_name, char_kw, char_col = characters[u_idx % len(characters)]

        # --- Left Page: Learn ---
        anchor_title = u.get("anchor_title", "Everyday Situation")
        if len(anchor_title) > 90:
            anchor_title = anchor_title[:87] + "..."
        formula_title = u.get("formula_title", "How to Use This Rule")
        formula_html = K.clean_legacy(u.get("formula_html", ""))
        pitfall_text = u.get("pitfall_text", "Common error.")
        model_text = u.get("model_text", "Correct model.")
        why_text = u.get("why_text", "Explanation of rule.")

        is_long = len(formula_html) > 850
        font_sz = "8.8pt" if is_long else "9.2pt"
        lh = "1.14" if is_long else "1.18"
        bubble_h = 44 if is_long else 48
        cmp_sz = "8.8pt" if is_long else "9.2pt"
        pad_v = "1.0mm" if is_long else "1.4mm"

        left_body = (
            K.page_title(u["title"], kicker=f"Unit {u_num} &bull; Entry 3 Basics", badge=u_num)
            + K.character_bubble(
                K.cartoon(char_kw), char_name,
                f"<b style='color:var(--accent)'>A &nbsp;Look &amp; Learn:</b><br>{anchor_title}",
                "left", bubble_h, char_col
            )
            + f"""<div class="box rule" style="flex:1 1 auto;padding:{pad_v} 3.5mm;font-size:{font_sz};line-height:{lh};">
                <div class="bt" style="margin-bottom:1mm;"><span class="ico">&#9733;</span>B &nbsp;{formula_title}</div>
                <div>{formula_html}</div>
              </div>"""
            + K.compare(
                f"<div style='font-size:{cmp_sz};line-height:1.2;'>{pitfall_text}</div>",
                f"<div style='font-size:{cmp_sz};line-height:1.2;'>{model_text}</div><div style='font-size:9pt;color:var(--muted);margin-top:1mm;'><b>Tip:</b> {why_text}</div>",
                stacked=False, bad_label="&#10007; Not Quite Right", good_label="&#10003; Good Sentence"
            )
        )
        pages.append(K.page(left_body, header=(BOOK, f"Unit {u_num} &bull; Learn"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # --- Right Page: Practise (with wide-angle thematic photo banner & 1-line caption) ---
        ex_a_items = []
        for q_tuple in u.get("exercise_a", [])[:2]:
            q_text, opts = q_tuple[0], q_tuple[1]
            clean_opts = [o[3:] if len(o) > 3 and o[1] == ")" else o for o in opts]
            ex_a_items.append({"q": q_text, "options": clean_opts})

        ex_b_items = []
        for b_tuple in u.get("exercise_b", [])[:2]:
            prompt_type, original = b_tuple[0], b_tuple[1]
            ex_b_items.append((f"<b>[{prompt_type}]:</b> <i>{original}</i>", 2))

        u_photo = next_wide_photo()
        u_cap = f"Unit {u_num} Everyday Context ({u.get('anchor_title', u['title'])}): Practising {u['title']}."
        right_body = (
            K.section("A", "Tick the correct answer")
            + spag_float_practice_card(u_photo, u_cap, width_mm=60)
            + K.exercise_list(ex_a_items)
            + "<div style='clear:both;'></div>"
            + K.section("B", "Write the sentence correctly")
            + K.exercise_list(ex_b_items, start=3)
            + K.fill_lines(f"<span style='color:var(--accent)'>C &nbsp;Your Turn:</span> Write one sentence of your own using the rule from Unit {u_num}.", min_mm=14, gap_mm=8.0)
        )
        pages.append(K.page(right_body, header=(BOOK, f"Unit {u_num} &bull; Practise"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p55-66: 6 Phonics & High-Frequency Word Banks (12 pages: 2 pages each)
    wb_start_pages = {}
    word_banks = [
        ("High-Frequency Days, Months & Seasons", [("Monday", "First day of work week"), ("Friday", "End of the working week"), ("September", "Autumn college term starts"), ("Winter", "Cold season requiring warm clothing"), ("August", "Summer holiday month"), ("Wednesday", "Middle of the week")]),
        ("Everyday Workplace Signs & Safety Words", [("Danger", "Keep clear of hazard"), ("Caution", "Wet floor warning"), ("Exit", "Emergency fire escape"), ("Notice", "Staff information board"), ("Private", "Staff only access"), ("Entrance", "Main public doorway")]),
        ("Spelling Pattern: Double Consonants", [("Letter", "Written message in envelope"), ("Dinner", "Evening meal"), ("Hammer", "Tool for driving nails"), ("Traffic", "Vehicles on the road"), ("Lesson", "Classroom study session"), ("Happen", "Take place or occur")]),
        ("Spelling Pattern: Silent Letters", [("Knife", "Kitchen cutting utensil"), ("Wrist", "Joint above hand"), ("Doubt", "Uncertain feeling"), ("Thumb", "Short digit on hand"), ("Sign", "Public notice board"), ("Comb", "Hair grooming tool")]),
        ("Common Irregular Plurals", [("Child / Children", "Young people at school"), ("Man / Men", "Adult male workers"), ("Woman / Women", "Adult female colleagues"), ("Foot / Feet", "Measurement of length"), ("Tooth / Teeth", "Dentist appointment"), ("Person / People", "Community members")]),
        ("Homophones: Words That Sound Alike", [("Hear / Here", "Listen / This place"), ("See / Sea", "Look / Ocean water"), ("One / Won", "Number 1 / First place"), ("Buy / By", "Purchase / Near to"), ("Right / Write", "Correct / Put pen to paper"), ("Sun / Son", "Bright star / Male child")])
    ]

    for wb_idx, (wb_title, words) in enumerate(word_banks):
        wb_start_pages[wb_idx + 1] = p_curr
        tiles = []
        for word, desc in words:
            tiles.append((
                next_wide_photo(),
                f"<b>{word}</b>",
                desc
            ))
        wb_body_1 = (
            K.page_title(f"Word Bank {wb_idx+1}: {wb_title}",
                         kicker="Entry Level 3 &bull; Phonics &amp; Word Banks",
                         lead="Essential words to recognise, read, and spell correctly every time.")
            + spag_vocab_grid(tiles)
        )
        pages.append(K.page(wb_body_1, header=(BOOK, f"Word Bank {wb_idx+1}"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        wb_body_2 = (
            K.page_title(f"Word Bank {wb_idx+1} &bull; Practice &amp; Handwriting",
                         kicker="Spelling Practice &bull; Look, Say, Cover, Write, Check")
            + K.exercise_list([
                (f"Copy the word <b>{words[0][0]}</b> twice neatly on the lines below:", 2),
                (f"Write a short sentence using the word <b>{words[1][0]}</b>:", 2),
                (f"Write a short sentence using the word <b>{words[2][0]}</b>:", 2)
            ])
            + K.fill_notes(f"My Spelling Practice Box for Word Bank {wb_idx+1}", min_mm=26)
        )
        pages.append(K.page(wb_body_2, header=(BOOK, f"Word Bank {wb_idx+1} &bull; Practice"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p67-78: 12 Mixed Sentence Building Workouts (12 pages)
    workouts_start_page = p_curr
    for w_idx in range(12):
        w_title = f"Sentence Building Workout {w_idx+1}"
        body = (
            K.page_title(w_title, kicker="Practical Skills &bull; Sentence Building", badge=w_idx+1)
            + K.box_html(
                "<p>Read the sentences below. Each one has a missing capital letter or full stop.</p>"
                + K.bullets([
                    "the delivery arrived on Tuesday morning",
                    "my manager said i could take my lunch break at one o'clock",
                    "is the doctor surgery open on saturday"
                ]),
                title="Sentences to Correct"
            )
            + K.exercise_list([
                ("Rewrite sentence 1 with a capital letter and full stop:", 2),
                ("Rewrite sentence 2 with capital letters for 'My' and 'I':", 2),
                ("Rewrite sentence 3 with a capital letter and question mark:", 2)
            ], start=1)
            + K.fill_notes("Handwriting Practice &amp; Tutor Comments", 22)
        )
        pages.append(K.page(body, header=(BOOK, f"Workout {w_idx+1}"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p79-84: 3 Practical Workplace Form-Filling Mocks (6 pages: 2 pages each)
    mocks_start_page = p_curr
    mock_tasks = [
        ("College Enrolment &amp; Registration Form", "Fill in your personal details, preferred course, and emergency contact."),
        ("Workplace Holiday Request Form", "State the dates you wish to book, your team, and supervisor approval."),
        ("Doctor's Appointment Slip &amp; Medical Note", "Record your symptom, requested appointment time, and contact phone number.")
    ]

    for m_idx, (m_title, m_desc) in enumerate(mock_tasks):
        m_photo = next_wide_photo()
        m_body_1 = (
            K.page_title(f"Mock Writing Task {m_idx+1}", kicker="Practical Writing &bull; 10 Marks", badge=f"M{m_idx+1}")
            + spag_practice_banner(m_photo, f"Practical Writing Mock {m_idx+1}: {m_title.replace('&amp;', '&')}", height_mm=30)
            + K.box_html(
                f"<p>{m_desc}</p>"
                f"<div style='border:2px solid var(--soft); border-radius:6px; padding:2.5mm; background:#fff; margin-top:1.5mm;'>"
                f"<div style='margin-bottom:1.8mm;'><b>First Name:</b> ____________________ &nbsp;&nbsp;&nbsp; <b>Surname:</b> ____________________</div>"
                f"<div style='margin-bottom:1.8mm;'><b>Date of Birth:</b> ____ / ____ / ______ &nbsp;&nbsp;&nbsp; <b>Postcode:</b> ____________</div>"
                f"<div style='margin-bottom:1.8mm;'><b>Reason for Application / Request:</b></div>"
                f"<div style='height:10mm; border-bottom:1.5px solid var(--line);'></div>"
                f"</div>",
                title=f"Official Form Template: {m_title}"
            )
            + K.tip_pair("Use neat block capital letters where asked.", "Always check your phone number and postcode digits.",
                         golden_title="Form Tip", watch_title="Check Carefully")
            + K.fill_lines("Practice Notes for Form Details", min_mm=24, gap_mm=9.5)
        )
        pages.append(K.page(m_body_1, header=(BOOK, f"Mock Form {m_idx+1} &bull; Template"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        m_body_2 = (
            K.page_title(f"Mock Task {m_idx+1} &bull; Lined Writing Booklet", kicker="Writing Response Page")
            + K.fill_lines("Write your extended response or notes below:", min_mm=180, gap_mm=10.5)
        )
        pages.append(K.page(m_body_2, header=(BOOK, f"Mock Form {m_idx+1} &bull; Writing"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # Reference Back Matter via K.ref_pages (Granular blocks so 0 overflows)
    ref_start_page = p_curr
    ref_blocks = []

    # 1. Diagnostic Answers (split evenly into chunks)
    p75 = a_e3.ANSWER_KEY_DATA.get('page_75', {})
    if 'diagnostic_answers' in p75:
        d_ans = p75['diagnostic_answers']
        chunk_sz = 10 if len(d_ans) > 10 else 5
        for c_start in range(0, len(d_ans), chunk_sz):
            c_slice = d_ans[c_start:c_start + chunk_sz]
            qa_html = "".join(f"<div class='qa'><span class='q-num'>{q}</span><span class='q-ans'><b>{ans}</b>: {escape_html(exp)}</span></div>" for q, ans, exp in c_slice)
            ref_blocks.append(K.ref_block(f"Diagnostic Solutions (Questions {c_start+1}–{c_start+len(c_slice)})", qa_html))

    # 2. Units 1 to 24 Worked Solutions (each unit is its own ref_block)
    for k in sorted(a_e3.ANSWER_KEY_DATA.keys()):
        data = a_e3.ANSWER_KEY_DATA[k]
        if 'units' in data:
            for unum, uinfo in sorted(data['units'].items()):
                ex1 = "<br>".join(escape_html(s) for s in uinfo.get('ex1', []))
                ex2 = "<br>".join(escape_html(s) for s in uinfo.get('ex2', []))
                u_html = f"<div style='margin-bottom:1.2mm;'><b>Exercise 1:</b><br>{ex1}</div><div><b>Exercise 2:</b><br>{ex2}</div>"
                ref_blocks.append(K.ref_block(f"Unit {unum} Worked Solutions", u_html))

    # 3. Workouts (each workout is its own ref_block)
    p80 = a_e3.ANSWER_KEY_DATA.get('page_80', {})
    if 'workouts' in p80:
        for w, ans in sorted(p80['workouts'].items()):
            if isinstance(ans, dict):
                e_list = "<br>".join(escape_html(e) for e in ans.get('errors', []))
                x_list = "<br>".join(escape_html(x) for x in ans.get('expansion', []))
                ref_blocks.append(K.ref_block(f"Sentence Building Workout {w} Key", f"<div>{e_list}</div><div style='margin-top:1mm;'><em>Model Expansion:</em> {x_list}</div>"))
            else:
                ref_blocks.append(K.ref_block(f"Sentence Building Workout {w} Key", f"<div>{escape_html(ans)}</div>"))

    # 4. Form-Filling Exemplars (each form is its own ref_block)
    if 'writing_exemplars' in p80:
        for f, ans in sorted(p80['writing_exemplars'].items()):
            ref_blocks.append(K.ref_block(f"Workplace Form-Filling Exemplar {f}", f"<div>{escape_html(ans)}</div>"))

    # 5. Phonics & High Frequency Rules
    phonics_rules = [
        ("Prefix 'Un-'", "Changes meaning to not or opposite: unwell, unhappy, unlock, unfair."),
        ("Prefix 'Re-'", "Means do again: rebuild, rewrite, restart, refill."),
        ("Suffix '-ful'", "Means full of (helpful, careful, painful). Only one 'l'."),
        ("Suffix '-less'", "Means without (careless, helpless, painless)."),
        ("Silent Letters", "Silent 'k' in knife, knee, knock; silent 'w' in write, wrong, wrist; silent 'g' in sign, high.")
    ]
    ph_html = "".join(f"<dl><dt>{escape_html(t)}</dt><dd>{escape_html(d)}</dd></dl>" for t, d in phonics_rules)
    ref_blocks.append(K.ref_block("Annexe D Phonics &amp; Spelling Rules", ph_html))

    # 6. Index
    index_e3 = [
        ("A", [("Alphabetical order", "7"), ("Annexe D spelling words", "55"), ("Apostrophes in contractions", "23")]),
        ("C", [("Capital letters", "9"), ("Commas in lists", "13"), ("Conjunctions (and, but)", "15")]),
        ("D", [("Double consonants", "59")]),
        ("E", [("Exclamation marks", "11")]),
        ("F", [("Full stops", "9")]),
        ("H", [("Homophones (hear/here, see/sea)", "65")]),
        ("P", [("Paragraphs", "19"), ("Past tense regular verbs", "17")]),
        ("Q", [("Question marks", "11")]),
        ("S", [("Silent letters (k, w, g)", "61"), ("Subject-verb agreement", "21")]),
        ("W", [("Workplace form-filling", "79")])
    ]
    ix_html = ""
    for letter, entries in index_e3:
        items = "".join(f"<div class='ix'><span>{escape_html(t)}</span><span>p.{escape_html(p)}</span></div>" for t, p in entries)
        ix_html += f"<div class='ix-letter'>{letter}</div>{items}"
    ref_blocks.append(K.ref_block("Entry Level 3 Subject &amp; Grammar Index", ix_html))

    cover_theme = K.theme_from_cover(front_cov)
    ref_page_list = K.ref_pages("SPaG Entry Level 3 Reference: Solutions &amp; Index", ref_blocks,
                                BOOK, start_page=p_curr, subtitle="Worked Solutions &amp; Phonics Guide",
                                cols=2, theme=cover_theme, notes_title="Candidate SPaG Revision Log")
    pages.extend(ref_page_list)
    p_curr += len(ref_page_list)

    # Candidate Progress Tracker
    audit_page_no = p_curr
    p_audit_body = (
        K.page_title("Candidate SPaG Progress Tracker &amp; Sticker Chart", kicker="Entry Level 3 Achievement", badge="SUCCESS")
        + K.box_html(
            "<p>Check off your skills as you complete each SPaG unit:</p>"
            + K.bullets([
                "Every sentence begins with a capital letter and ends with a full stop.",
                "Questions always end with a question mark.",
                "Can spell everyday Annexe D words correctly using phonics rules."
            ]),
            title="Entry Level 3 SPaG Success Targets"
        )
        + K.fill_notes("Personal Success Notes &amp; Tutor Endorsements", min_mm=38)
    )
    pages.append(K.page(p_audit_body, header=(BOOK, "Progress Tracker"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Duplex even-page balance check before back cover
    if (len(pages) + 1) % 2 != 0:
        p_ibc_body = (
            K.page_title("Candidate SPaG Certificate &amp; Tutor Endorsement", kicker="Entry Level 3 Achievement", badge="STAR")
            + K.box_html(
                "<p>Well done on completing all 24 SPaG units! Remember these three golden rules every time you write:</p>"
                + K.bullets([
                    "<b>Start with a Capital Letter:</b> Every sentence begins with a big capital letter.",
                    "<b>End with a Full Stop:</b> Stop your sentence with a clean dot (.) or question mark (?).",
                    "<b>Sound It Out:</b> Break long words into small syllables when checking spelling."
                ]),
                title="Entry Level 3 Star Writer Declaration"
            )
            + K.tip_pair("Keep practising your spelling word banks every day.",
                         "Always read your sentence out loud to check it makes sense.",
                         golden_title="Reading Check", watch_title="Golden Habit")
            + K.fill_notes("Tutor Endorsement &amp; Candidate Next Steps", min_mm=26)
        )
        pages.append(K.page(p_ibc_body, header=(BOOK, "Tutor Endorsement"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # Populate p2: 2-Column Table of Contents
    toc_left = [
        ("DIAG", "Diagnostic Audit &amp; Routing", [
            ("D1–D4", "Visual Diagnostic Assessment (Q1–Q10)", "3"),
        ]),
        ("U1–U16", "Entry 3 Grammar Units (Part 1)", [
            (f"U{u['unit']}", u["title"], str(unit_start_pages[u["unit"]]))
            for u in all_units[:16]
        ]),
    ]
    toc_right = [
        ("U17–U24", "Entry 3 Grammar Units (Part 2)", [
            (f"U{u['unit']}", u["title"], str(unit_start_pages[u["unit"]]))
            for u in all_units[16:]
        ]),
        ("WORDS", "Phonics &amp; High-Frequency Word Banks", [
            (f"WB{i+1}", word_banks[i][0], str(wb_start_pages[i+1]))
            for i in range(len(word_banks))
        ]),
        ("DRILLS", "Sentence Workouts &amp; Form-Filling Mocks", [
            ("W1–W12", "12 Practical Sentence Building Workouts", str(workouts_start_page)),
            ("M1–M3", "3 Practical Workplace Form-Filling Mocks", str(mocks_start_page)),
        ]),
        ("REF", "Solutions, Phonics Guide &amp; Tracker", [
            ("SOL", "Diagnostic, Unit 1–24 &amp; Workout Keys", str(ref_start_page)),
            ("TRACK", "Candidate SPaG Progress Tracker", str(audit_page_no)),
        ]),
    ]
    pages[1] = spag_toc_page(
        "SPaG Entry Level 3 Mastery",
        "Visual Rules, Clear Pictures &amp; Step-by-Step Handwriting Drills",
        toc_left, toc_right, BOOK
    )

    # Back Cover
    pages.append(K.back_cover(back_cov))

    print(f"Total Pages Assembled: {len(pages)}")
    out_pdf = DOWNLOADS / "MasterFunctionalSkills_SPaG_Entry_Level_3_Mastery.pdf"
    res = K.render_pdf(pages, out_pdf, theme=cover_theme, entry3=True, title="Master Functional Skills - SPaG Entry Level 3 Mastery")
    shutil.copyfile(out_pdf, DOCUMENTS / out_pdf.name)
    print(f"Rendered: {res['pdf']} | Overflows: {res.get('overflow', [])}")
    return res


if __name__ == "__main__":
    r_l2 = build_spag_l2()
    r_l1 = build_spag_l1()
    r_e3 = build_spag_e3()
    print("\nSPaG Suite Build Complete: All 3 levels generated!")
    print("L2 Overflows:", r_l2.get("overflow", []))
    print("L1 Overflows:", r_l1.get("overflow", []))
    print("E3 Overflows:", r_e3.get("overflow", []))
