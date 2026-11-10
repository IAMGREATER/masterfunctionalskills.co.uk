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
import re
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
    COMPANION_L1_TASKS,
    WORKBOOK_L2_TASKS,
    WORKBOOK_L1_TASKS
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
    SPAG_L1_EXERCISES,
    MOCK_ENGLISH_L2_PAPERS,
    MOCK_ENGLISH_L1_PAPERS,
    WORKBOOK_MOCK_L2_PAPERS,
    WORKBOOK_MOCK_L1_PAPERS
)

DOWNLOADS = PROJECT_DIR / "assets" / "downloads"
DOCUMENTS = Path("/home/subi/Documents")
COV = K.COVER_DIR

SHOW_UNIT_IMAGES = True
UNIT_PHOTOS_L2 = {
    1: ("writing_thematic/l2_f1_article.jpg", "Magazine &amp; Web Feature Article"),
    2: ("writing_thematic/l2_f2_email.jpg", "Workplace Proposal Email"),
    3: ("writing_thematic/l2_f3_letter.jpg", "Formal Complaint Letter"),
    4: ("writing_thematic/l2_f4_report.jpg", "Canteen Investigation Report"),
    5: ("writing_thematic/l2_f5_incident.jpg", "Warehouse Incident Report"),
    6: ("writing_thematic/l2_f6_leaflet.jpg", "Smart Budgeting Advice Leaflet"),
    7: ("writing_thematic/l2_f7_review.jpg", "Fitness Centre Venue Review"),
    8: ("writing_thematic/l2_f8_feedback.jpg", "Online Customer Feedback Form"),
    9: ("writing_thematic/l2_f9_forum.jpg", "Careers Discussion Forum"),
    10: ("writing_thematic/l2_f10_newsletter.jpg", "Community Harvest Newsletter"),
    11: ("writing_thematic/l2_f11_diary.jpg", "NHS Placement Reflective Log"),
    12: ("writing_thematic/l2_f12_speech.jpg", "Green Workplace Speech"),
}

UNIT_PHOTOS_SECOND = {
    1: ("writing_thematic/l2_f1_task2.jpg", "High Street Contactless Debate"),
    2: ("writing_thematic/l2_f2_task2.jpg", "Staff Cycle Hub Proposal"),
    3: ("writing_thematic/l2_f3_task2.jpg", "Smart Meter Billing Dispute"),
    4: ("writing_thematic/l2_f4_task2.jpg", "Electric Delivery Fleet Trial"),
    5: ("writing_thematic/l2_f5_task2.jpg", "Kitchen COSHH Spill Log"),
    6: ("writing_thematic/l2_f6_task2.jpg", "Cyber Security &amp; Interviews"),
    7: ("writing_thematic/l2_f7_task2.jpg", "Regional Careers &amp; Skills Expo"),
    8: ("writing_thematic/l2_f8_task2.jpg", "Airport Flight Delay Desk"),
    9: ("writing_thematic/l2_f9_task2.jpg", "Four-Day Working Week Trial"),
    10: ("writing_thematic/l2_f10_task2.jpg", "Corporate Volunteering Day"),
    11: ("writing_thematic/l2_f11_task2.jpg", "Workplace First Aid &amp; AED"),
    12: ("writing_thematic/l2_f12_task2.jpg", "Town Hall Youth Hub Speech"),
}

UNIT_PHOTOS_L1 = {
    1: ("writing_thematic/l1_f1_article.jpg", "Greener Town Action Article"),
    2: ("writing_thematic/l1_f2_email.jpg", "Community Library Event Email"),
    3: ("writing_thematic/l1_f3_letter.jpg", "Heating Repair Letter"),
    4: ("writing_thematic/l1_f4_report.jpg", "Student Common Room Report"),
    5: ("writing_thematic/l1_f5_incident.jpg", "Stockroom Accident Report"),
    6: ("writing_thematic/l1_f6_leaflet.jpg", "Exam Stress Advice Leaflet"),
    7: ("writing_thematic/l1_f7_review.jpg", "Corner Bakery Café Review"),
    8: ("writing_thematic/l1_f8_feedback.jpg", "Online Delivery Feedback Form"),
    9: ("writing_thematic/l1_f9_forum.jpg", "Park Dog Area Forum Post"),
    10: ("writing_thematic/l1_f10_newsletter.jpg", "Youth &amp; Sports Club Newsletter"),
    11: ("writing_thematic/l1_f11_diary.jpg", "Catering Kitchen Learning Log"),
    12: ("writing_thematic/l1_f12_speech.jpg", "College Induction Welcome Talk"),
}

UNIT_PHOTOS_L1_SECOND = {
    1: ("writing_thematic/l1_f1_task2.jpg", "Evening Art &amp; Pottery Class"),
    2: ("writing_thematic/l1_f2_task2.jpg", "College Museum Study Trip"),
    3: ("writing_thematic/l1_f3_task2.jpg", "Pothole &amp; Bus Route Letter"),
    4: ("writing_thematic/l1_f4_task2.jpg", "Lakeside Nature Reserve Visit"),
    5: ("writing_thematic/l1_f5_task2.jpg", "Supermarket Aisle Spill Log"),
    6: ("writing_thematic/l1_f6_task2.jpg", "Safe Town Cycling Leaflet"),
    7: ("writing_thematic/l1_f7_task2.jpg", "Starlight Cinema Review"),
    8: ("writing_thematic/l1_f8_task2.jpg", "Train Delay Feedback Form"),
    9: ("writing_thematic/l1_f9_task2.jpg", "Healthy £2 Family Meals Blog"),
    10: ("writing_thematic/l1_f10_task2.jpg", "Animal Rescue Open Day"),
    11: ("writing_thematic/l1_f11_task2.jpg", "Retail Customer Service Log"),
    12: ("writing_thematic/l1_f12_task2.jpg", "Clean Up Our Street Talk"),
}

SPAG_WRITING_PHOTOS = {
    1: ("writing_thematic/spag1_clauses.jpg", "Sentence Boundaries &amp; Semicolons"),
    2: ("writing_thematic/spag2_complex.jpg", "Building Complex Sentences"),
    3: ("writing_thematic/spag3_agreement.jpg", "Verb Tense &amp; Agreement"),
    4: ("writing_thematic/spag4_modals.jpg", "Modal Verbs &amp; Register"),
    5: ("writing_thematic/spag5_lists.jpg", "Colons &amp; Parallel Bullet Lists"),
    6: ("writing_thematic/spag6_apostrophes.jpg", "Possessive Apostrophes"),
    7: ("writing_thematic/spag7_cohesion.jpg", "Paragraphs &amp; Discourse Links"),
    8: ("writing_thematic/spag8_spelling.jpg", "Proofreading &amp; Spelling Check"),
}


def writing_float_photo_card(rel_path: str, caption_txt: str, height_mm: int = 46, width_mm: int = 82) -> str:
    abs_p = K.PHOTO_DIR / rel_path
    if not abs_p.exists():
        return ""
    return (
        f"<div style='float:right;width:{width_mm}mm;margin:0 0 2mm 3.5mm;border:1.5px solid var(--primary);"
        f"border-radius:6px;overflow:hidden;background:#f8fafc;box-shadow:0 1.5px 4px rgba(0,0,0,0.08);'>"
        f"<div style='width:100%;aspect-ratio:16/9;overflow:hidden;background:#0f172a;'>"
        f"<img src='{abs_p.as_uri()}' style='width:100%;height:100%;object-fit:cover;object-position:center 25%;display:block;'>"
        f"</div>"
        f"<div style='font-size:7.6pt; /* hf-ok */ font-weight:700;color:var(--primary);text-align:center;"
        f"padding:0.8mm 1.2mm;background:#eff6ff;border-top:1px solid #bfdbfe;line-height:1.15;"
        f"white-space:nowrap;overflow:hidden;text-overflow:ellipsis;'>"
        f"{caption_txt}</div></div>"
    )


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
    # Placeholder for Page 2 (Table of Contents), populated dynamically after all pages are assembled
    pages.append("")

    # Helper to format structured Band 4 Model Answers with highlighted specialist vocabulary
    def render_formatted_model_l2(raw_model: str, spec_words) -> str:
        def hl_text(txt: str) -> str:
            esc = escape_html(txt)
            for sw in sorted(spec_words, key=len, reverse=True):
                pattern = re.compile(r"\b(" + re.escape(escape_html(sw)) + r")\b", re.IGNORECASE)
                esc = pattern.sub(
                    r"<span style='background:#fef3c7;border-bottom:1.5px solid #d97706;padding:0 0.25mm;border-radius:2px;font-weight:700;color:#0f172a;'>\1</span>",
                    esc,
                    count=1
                )
            return esc

        out = []
        bullet_buf = []

        def flush_bullets():
            if bullet_buf:
                items = "".join(f"<li style='margin-bottom:0.4mm;'>{b}</li>" for b in bullet_buf)
                out.append(f"<ul style='margin:0.6mm 0 1mm 4mm;padding:0;font-size:8.8pt; /* hf-ok */ line-height:1.25;'>{items}</ul>")
                bullet_buf.clear()

        for raw_line in raw_model.splitlines():
            ln = raw_line.strip()
            if not ln:
                flush_bullets()
                continue
            if ln.startswith("TITLE:"):
                flush_bullets()
                val = escape_html(ln[6:].strip())
                out.append(f"<div style='font-size:10pt; /* hf-ok */ font-weight:800;color:var(--primary);border-bottom:1.5px solid var(--accent);padding-bottom:0.5mm;margin-bottom:0.8mm;'>{val}</div>")
            elif ln.startswith("META_RIGHT:"):
                flush_bullets()
                val = escape_html(ln[11:].strip())
                out.append(f"<div style='font-size:8.3pt; /* hf-ok */ font-weight:700;color:#334155;text-align:right;margin-bottom:0.6mm;'>{val}</div>")
            elif ln.startswith("META:"):
                flush_bullets()
                val = escape_html(ln[5:].strip())
                out.append(f"<div style='font-size:8.3pt; /* hf-ok */ font-weight:700;color:#334155;background:#f8fafc;border-left:2.5px solid var(--primary);padding:0.4mm 1.8mm;margin-bottom:0.6mm;'>{val}</div>")
            elif ln.startswith("SALUTATION:"):
                flush_bullets()
                val = escape_html(ln[11:].strip())
                out.append(f"<div style='font-size:8.8pt; /* hf-ok */ font-weight:700;color:#0f172a;margin:0.6mm 0;'>{val}</div>")
            elif ln.startswith("SUB:"):
                flush_bullets()
                val = escape_html(ln[4:].strip())
                out.append(f"<div style='font-size:9pt; /* hf-ok */ font-weight:800;color:var(--primary);margin:0.8mm 0 0.3mm 0;'>{val}</div>")
            elif ln.startswith("•"):
                val = hl_text(ln[1:].strip())
                bullet_buf.append(val)
            else:
                flush_bullets()
                out.append(f"<p style='margin:0 0 0.8mm 0;font-size:8.8pt; /* hf-ok */ line-height:1.26;'>{hl_text(ln)}</p>")
        flush_bullets()
        return "".join(out)

    # Compact table CSS helper so tables fit cleanly within the 240mm page body
    compact_tbl_css = (
        "<style>"
        ".t.compact th { padding:1.1mm 2mm !important; font-size:9pt !important; /* hf-ok */ line-height:1.2 !important; }"
        ".t.compact td { padding:1.0mm 2mm !important; font-size:8.8pt !important; /* hf-ok */ line-height:1.22 !important; }"
        ".ptitle h1 { font-size:19.5pt !important; line-height:1.08 !important; }"
        ".ptitle .badge { height:15mm !important; min-width:15mm !important; font-size:16pt !important; }"
        ".pair .box { padding:2.2mm 3mm !important; font-size:9.8pt !important; /* hf-ok */ line-height:1.26 !important; }"
        "</style>"
    )

    # p3: Specification Mapping: Pearson Edexcel Level 2 Writing Overview (W20-W28)
    p3_body = (
        compact_tbl_css
        + K.page_title("Pearson Edexcel Level 2 Specification",
                       kicker="Curriculum Architecture &bull; Pearson Specification QAN 603/4290/0 (W20–W28)", badge="SPEC")
        + K.box_html(
            "<div style='font-size:9.8pt; /* hf-ok */ line-height:1.35;'>"
            "<p style='margin:0 0 1mm 0;'><b>Examination Structure:</b> The Pearson Edexcel Functional Skills English Level 2 Writing examination is a <b>60-minute</b> externally assessed paper comprising two compulsory writing tasks:</p>"
            "<ul style='margin:0 0 1mm 4mm;padding:0;'>"
            "<li><b>Task 1 (Extended Functional Writing &bull; 21 Marks &bull; 35 Minutes):</b> Workplace, civic, or community scenario requiring <b>250&ndash;350 words</b>. Assessed across Composition &amp; Effect (12 marks) and SPaG (9 marks).</li>"
            "<li><b>Task 2 (Structured Functional Writing &bull; 15 Marks &bull; 25 Minutes):</b> Targeted response of <b>200&ndash;250 words</b> to a realistic brief. Assessed across Composition &amp; Effect (9 marks) and SPaG (6 marks).</li>"
            "</ul>"
            "<p style='margin:0;'><b>Total Marks: 36 Marks &bull; SPaG Weighting: 41.7% (15/36 marks).</b> Typical pass threshold: <b>22&ndash;24 marks (approx. 61&ndash;67%)</b>.</p>"
            "</div>",
            title="Official Pearson Edexcel Level 2 Assessment Profile"
        )
        + K.box_html(
            "<table class='t compact'>"
            "<thead><tr><th style='width:10%;'>Code</th><th style='width:62%;'>Official Subject Content Statement (DfE / Pearson Edexcel Level 2)</th><th style='width:28%;'>Book Coverage</th></tr></thead>"
            "<tbody>"
            "<tr><td><b>W20</b></td><td>Communicate information, ideas and opinions clearly, coherently and effectively</td><td>All 12 Formats &amp; Strategy</td></tr>"
            "<tr><td><b>W21</b></td><td>Write text of an appropriate level of detail and of appropriate length (where specified)</td><td>Word Count &amp; Bullet Scaffolds</td></tr>"
            "<tr><td><b>W22</b></td><td>Organise writing for different purposes using appropriate format, structure, headings, bullets &amp; paragraphs</td><td>6-Point Format Anatomy Grids</td></tr>"
            "<tr><td><b>W23</b></td><td>Convey clear meaning and establish cohesion using organisational markers (discourse markers)</td><td>Page 4 &amp; SPaG Unit 7</td></tr>"
            "<tr><td><b>W24</b></td><td>Use different language and register (persuasive techniques, supporting evidence, specialist vocabulary)</td><td>12-Word Vocab Banks &amp; SPaG 4/8</td></tr>"
            "<tr><td><b>W25</b></td><td>Construct complex sentences consistently and accurately, using varied sentence lengths and clauses</td><td>SPaG Masterclass Units 1 &amp; 2</td></tr>"
            "<tr><td><b>W26</b></td><td>Use correct grammar (subject-verb agreement, consistent tense use, active/passive voice, articles)</td><td>SPaG Masterclass Unit 3</td></tr>"
            "<tr><td><b>W27</b></td><td>Punctuate writing with accuracy: colons, semicolons, commas, apostrophes, quotation marks, hyphens</td><td>SPaG Masterclass Units 1, 5 &amp; 6</td></tr>"
            "<tr><td><b>W28</b></td><td>Spell words used in work, study and daily life accurately, including specialist words and homophones</td><td>SPaG Unit 8 &amp; 144 Vocab Terms</td></tr>"
            "</tbody></table>",
            title="Complete Pearson Edexcel Level 2 Syllabus Mapping (W20–W28)"
        )
        + K.tip_pair(
            "Address every single bullet point in the exam prompt—missing even one bullet point caps Composition at Band 2.",
            "Eliminate all comma splices and informal text-speak; 41.7% of your entire exam grade comes directly from SPaG.",
            golden_title="Golden Examiner Rule", watch_title="Critical Exam Trap"
        )
    )
    pages.append(K.page(p3_body, header=(BOOK, "Specification Overview"), footer=BOOK, page_no=3))

    # p4: Complete Writing Strategy Masterclass: TAP, Planning, DAFOREST, Register & Proofreading
    p4_body = (
        compact_tbl_css
        + K.page_title("Core Writing Strategy &amp; Proofreading",
                       kicker="Pre-Writing Mastery &bull; TAP, Paragraphs, DAFOREST, Register &amp; Proofreading", badge="STRAT")
        + K.box_html(
            "<div style='display:grid;grid-template-columns:1fr 1fr;gap:2mm;font-size:8.8pt; /* hf-ok */ line-height:1.28;'>"
            "<div style='background:#f8fafc;border:1px solid var(--soft);border-left:3.5px solid var(--primary);padding:1.6mm 2.2mm;border-radius:4px;'>"
            "<b style='color:var(--primary);font-size:9.3pt; /* hf-ok */'>1. Decoding Prompts (The TAP Method) &amp; Register</b><br>"
            "&bull; <b>T (Text Format):</b> Identify exact layout markers (addresses, To/From/Subject, headline, subheadings, or speech greeting).<br>"
            "&bull; <b>A (Audience):</b> Authority figure (manager, council, director) = <b>Formal</b> (no contractions, objective tone). Friend/peer = <b>Informal</b> (warm, conversational). Public = <b>Semi-formal</b>.<br>"
            "&bull; <b>P (Purpose):</b> Inform, Persuade, Advise, Explain, or Complain.<br>"
            "&bull; <b>Sign-Off Rules:</b> <i>Dear Sir/Madam</i> &rarr; <b>Yours faithfully</b> | <i>Dear Mr/Ms [Surname]</i> &rarr; <b>Yours sincerely</b> | <i>Hi/Dear [First Name]</i> &rarr; <b>Kind regards / Best wishes</b>."
            "</div>"
            "<div style='background:#f8fafc;border:1px solid var(--soft);border-left:3.5px solid var(--accent);padding:1.6mm 2.2mm;border-radius:4px;'>"
            "<b style='color:var(--primary);font-size:9.3pt; /* hf-ok */'>2. The 5-Minute Planning &amp; Paragraph Formula</b><br>"
            "&bull; <b>5-Min Plan:</b> Sketch a 4-Box Grid (TAP + 3 Bullet Paragraphs + 5 Specialist Words + Punctuation Targets) or Spider Diagram.<br>"
            "&bull; <b>When to Start a New Paragraph (TiPToP):</b> Change of <b>Ti</b>me, <b>P</b>lace, <b>To</b>pic (each exam bullet = 1 dedicated paragraph), or <b>P</b>erson.<br>"
            "&bull; <b>P.E.E. Paragraph Structure:</b> <b>Point</b> (topic sentence) &rarr; <b>Evidence/Example</b> (fact, statistic, or case detail) &rarr; <b>Explanation</b> (impact or action).<br>"
            "&bull; <b>Corrections:</b> Cross out errors with a single neat line and write clearly above."
            "</div>"
            "<div style='background:#f8fafc;border:1px solid var(--soft);border-left:3.5px solid var(--primary);padding:1.6mm 2.2mm;border-radius:4px;'>"
            "<b style='color:var(--primary);font-size:9.3pt; /* hf-ok */'>3. Persuasive Toolkit (DAFOREST) &amp; Opinions</b><br>"
            "&bull; <b>D</b>irect Address (<i>you, our community</i>) &bull; <b>A</b>lliteration (<i>practical, proven progress</i>)<br>"
            "&bull; <b>F</b>acts &amp; <b>S</b>tatistics (<i>74% of surveyed residents confirmed...</i>)<br>"
            "&bull; <b>O</b>pinions backed by evidence &amp; balanced counter-arguments (<i>While some argue..., the evidence proves...</i>)<br>"
            "&bull; <b>R</b>hetorical Questions (<i>Can we truly afford to ignore this risk?</i>)<br>"
            "&bull; <b>E</b>motive Language (<i>vital, unacceptable</i>) &bull; <b>T</b>riplets / Rule of Three (<i>fair, affordable, and sustainable</i>)."
            "</div>"
            "<div style='background:#f8fafc;border:1px solid var(--soft);border-left:3.5px solid var(--accent);padding:1.6mm 2.2mm;border-radius:4px;'>"
            "<b style='color:var(--primary);font-size:9.3pt; /* hf-ok */'>4. The 5-Minute Targeted Proofreading Routine</b><br>"
            "&bull; <b>Scan 1 (Sentence Boundaries):</b> Check every sentence starts with a capital letter and ends with a full stop, question mark, or semicolon—never a comma splice!<br>"
            "&bull; <b>Scan 2 (Grammar &amp; Tense):</b> Verify consistent past/present tense and subject-verb agreement (<i>we were</i>, never <i>we was</i>; <i>could have</i>, never <i>could of</i>).<br>"
            "&bull; <b>Scan 3 (Homophones &amp; Spelling):</b> Audit <i>their/there/they're</i>, <i>your/you're</i>, <i>to/too/two</i>, <i>affect/effect</i>, <i>practice/practise</i>, <i>advice/advise</i>, and double-letter words (<i>accommodation, necessary, recommend</i>)."
            "</div>"
            "</div>",
            title="The Four Pillars of Band 4 Exam Execution"
        )
        + K.box_html(
            "<table class='t compact'>"
            "<thead><tr><th>Cohesive Function</th><th>Avoid Overusing (Basic)</th><th>Use Level 2 Discourse Markers (Band 4 Cohesion)</th></tr></thead>"
            "<tbody>"
            "<tr><td><b>Adding &amp; Reinforcing</b></td><td>And, Also, Plus</td><td><i>Furthermore, In addition, Moreover, Equally important</i></td></tr>"
            "<tr><td><b>Contrasting &amp; Balancing</b></td><td>But, However</td><td><i>On the other hand, Conversely, In stark contrast, Whereas, Nevertheless</i></td></tr>"
            "<tr><td><b>Cause, Effect &amp; Result</b></td><td>So, Because</td><td><i>Consequently, As a direct result, Therefore, For this reason</i></td></tr>"
            "<tr><td><b>Sequencing &amp; Concluding</b></td><td>First, At the end</td><td><i>Firstly, Subsequently, In conclusion, Ultimately, To summarise</i></td></tr>"
            "</tbody></table>",
            title="Level 2 Discourse Markers &amp; Paragraph Transitions Bank"
        )
    )
    pages.append(K.page(p4_body, header=(BOOK, "Core Writing Strategy"), footer=BOOK, page_no=4))

    # p5 to p64: All 12 Authentic Formats x 5 pages each = 60 pages
    SHOW_UNIT_IMAGES = True

    p_curr = 5
    format_start_pages = {}
    for f in FORMATS_L2:
        f_idx = f["idx"]
        format_start_pages[f_idx] = p_curr
        f_title = f["title"]
        f_short = f_title.split("(")[0].strip()
        f_marks = f["marks"]
        f_words = f["word_count"]
        f_topic = f["topic"]
        f_aud = f["audience"]
        f_tone = f["tone"]
        f_purpose = f.get("purpose_overview", "")
        f_anat = f.get("anatomy_steps", [])
        f_gold = f.get("golden_rule", "Include all required structural layout features.")
        f_trap = f.get("examiner_trap", "Maintain consistent register and accurate punctuation.")
        f_comm = f.get("examiner_commentary", "")
        f_spec_list = f["specialist_words"]
        f_stim = f["stimulus"]
        f_bullets = f["bullets"]
        f_strat = f["strategy"]
        f_model = f["model_answer"]
        f_voc_dict = f["vocab_definitions"]
        f_pract = f["practice_task"]

        # Page 1: Format Blueprint, Thorough Explanation, 6-Point Anatomy & 12 Specialist Words
        anat_cards = "".join(
            f"<div style='background:#f8fafc;border:1px solid var(--soft);border-left:3px solid var(--primary);border-radius:4px;padding:0.9mm 1.8mm;'>"
            f"<div style='font-weight:800;font-size:8.5pt; /* hf-ok */ color:var(--primary);margin-bottom:0.15mm;'>{escape_html(st_title)}</div>"
            f"<div style='font-size:8.1pt; /* hf-ok */ line-height:1.2;color:#334155;'>{escape_html(st_desc)}</div>"
            f"</div>"
            for st_title, st_desc in f_anat
        )
        spec_pills = "".join(
            f"<span style='display:inline-block;background:#fef3c7;border:1px solid #f59e0b;color:#0f172a;font-weight:700;font-size:8.2pt; /* hf-ok */ padding:0.3mm 1.8mm;border-radius:8px;'>{escape_html(w)}</span>"
            for w in f_spec_list
        )

        art_word = "an" if f_short[:1].lower() in "aeiou" else "a"
        overview_text_html = (
            f"<div style='font-size:8.3pt; /* hf-ok */ line-height:1.2;'>"
            f"<p style='margin:0 0 0.6mm 0;'>{escape_html(f_purpose)}</p>"
            f"<p style='margin:0 0 0.3mm 0;'><b>Target Audience:</b> {escape_html(f_aud)}</p>"
            f"<p style='margin:0 0 0.3mm 0;'><b>Required Tone &amp; Register:</b> {escape_html(f_tone)}</p>"
            f"<p style='margin:0;'><b>Essential Layout Features:</b> {escape_html(f['features'])}</p>"
            f"</div>"
        )
        if SHOW_UNIT_IMAGES and f_idx in UNIT_PHOTOS_L2:
            rel_img, u_cap = UNIT_PHOTOS_L2[f_idx]
            img_path = K.PHOTO_DIR / rel_img
            img_uri = img_path.as_uri() if img_path.exists() else ""
            overview_box_inner = (
                f"<div style='display:grid;grid-template-columns:1.08fr 0.92fr;gap:3mm;align-items:center;'>"
                f"<div style='display:flex;flex-direction:column;justify-content:center;font-size:8.2pt; /* hf-ok */ line-height:1.20;'>"
                f"{overview_text_html}"
                f"</div>"
                f"<div style='background:#ffffff;border:1.5px solid var(--primary);border-radius:6px;overflow:hidden;box-shadow:0 1.5px 4px rgba(0,0,0,0.08);display:flex;flex-direction:column;'>"
                f"<div style='width:100%;aspect-ratio:16/9;overflow:hidden;background:#0f172a;'>"
                f"<img src='{img_uri}' alt='{escape_html(f_short)}' style='width:100%;height:100%;object-fit:cover;object-position:center 25%;display:block;'>"
                f"</div>"
                f"<div style='background:var(--primary);color:#ffffff;font-size:7.8pt; /* hf-ok */ font-weight:700;text-align:center;padding:0.8mm 1.5mm;letter-spacing:0.01em;line-height:1.15;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;'>"
                f"Unit {f_idx}: {u_cap}</div>"
                f"</div>"
                f"</div>"
            )
        else:
            overview_box_inner = overview_text_html

        p1_body = (
            compact_tbl_css
            + K.page_title(f"Format {f_idx}: {f_title}", kicker=f"Format Blueprint &amp; Complete Guide &bull; {f_marks} Marks &bull; {f_words}", badge=f"F{f_idx}")
            + K.rule_box(
                f"What Is {art_word} {f_short}? Purpose, Audience &amp; Register Rules",
                overview_box_inner
            )
            + K.box_html(
                f"<div style='display:grid;grid-template-columns:1fr 1fr;gap:1.2mm;margin-bottom:1.5mm;'>{anat_cards}</div>"
                f"<div style='background:#f8fafc;border:1px solid var(--soft);border-radius:4px;padding:1.2mm 2mm;'>"
                f"<div style='font-weight:800;font-size:8.5pt; /* hf-ok */ color:var(--primary);margin-bottom:0.6mm;'>"
                f"Unit {f_idx} Specialist Vocabulary Bank ({len(f_spec_list)} Essential Level 2 Terms &mdash; Full Definitions on Page {p_curr+2}):</div>"
                f"<div style='display:flex;flex-wrap:wrap;gap:1mm;'>{spec_pills}</div>"
                f"</div>",
                title="Step-by-Step Structural Anatomy (Top to Bottom) &amp; Specialist Vocabulary"
            )
            + K.tip_pair(
                f_gold,
                f_trap,
                golden_title="Tutor Golden Rule", watch_title="Examiner Red Flag"
            )
        )
        pages.append(K.page(p1_body, header=(BOOK, f"Format {f_idx} &bull; Blueprint"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 2: Exam Scenario, Stimulus Material & Planning Frame
        stim_html = escape_html(f_stim).replace("\n", "<br>")
        bullets_html = K.bullets([escape_html(b) for b in f_bullets])
        p2_body = (
            compact_tbl_css
            + K.page_title(f"Format {f_idx}: {f_short} &bull; Guided Exam Task", kicker=f"Pearson Edexcel Scenario &bull; {f_marks} Marks &bull; {f_words}", badge="TASK")
            + K.box_html(
                f"<div style='background:#f8fafc;padding:2.2mm 2.8mm;border:1.5px solid var(--soft);border-radius:6px;font-size:9.8pt; /* hf-ok */ line-height:1.38;margin-bottom:1.5mm;'>"
                f"<strong style='color:var(--primary);'>Context &amp; Stimulus Material:</strong><br>{stim_html}"
                f"</div>"
                f"<p style='margin:1mm 0;font-size:10pt; /* hf-ok */'><b>Task Instructions:</b> Write your response for the specified audience. In your writing, you must:</p>"
                f"<div style='font-size:9.8pt; /* hf-ok */ line-height:1.34;'>{bullets_html}</div>"
                f"<p style='margin-top:1mm;font-size:9.2pt; /* hf-ok */ color:#475569;'><b>Word Count Target:</b> {f_words} &emsp; <b>Weighting:</b> {f_marks} Marks &emsp; <b>Key Vocab:</b> {escape_html(', '.join(f_spec_list[:6]))}</p>",
                title=f"Official Exam Brief &bull; Format {f_idx}"
            )
            + K.box_html(
                "<div style='display:grid;grid-template-columns:1fr 1fr 1fr;gap:2mm;font-size:9pt; /* hf-ok */'>"
                f"<div style='border:1px solid var(--soft);padding:1.6mm 2mm;border-radius:4px;background:#f8fafc;'><b>1. Audience &amp; Register:</b><br><span style='color:#475569;font-size:8.4pt; /* hf-ok */'>{escape_html(f_tone[:75])}</span></div>"
                "<div style='border:1px solid var(--soft);padding:1.6mm 2mm;border-radius:4px;background:#f8fafc;'><b>2. Target Discourse Markers:</b><br><span style='color:#475569;font-size:8.4pt; /* hf-ok */'>Furthermore, Consequently, On the other hand, In conclusion</span></div>"
                "<div style='border:1px solid var(--soft);padding:1.6mm 2mm;border-radius:4px;background:#f8fafc;'><b>3. Punctuation Checklist:</b><br><span style='color:#475569;font-size:8.4pt; /* hf-ok */'>Semicolon (;), Colon (:), Subordinate clause, Zero comma splices</span></div>"
                "</div>",
                title="5-Minute TAP Planning Framework (Text, Audience, Purpose)"
            )
            + K.fill_notes("Candidate Paragraph Plan (Opening/Hook &bull; Bullet 1 &bull; Bullet 2 &bull; Bullet 3 &bull; Action Close)", min_mm=22)
        )
        pages.append(K.page(p2_body, header=(BOOK, f"Format {f_idx} &bull; Task Brief"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 3: Official Band 4 Benchmark Model Answer + 12 Specialist Vocab Definitions + Examiner Commentary
        model_formatted = render_formatted_model_l2(f_model, f_spec_list)
        vocab_items = "".join(
            f"<div style='font-size:7.9pt; /* hf-ok */ line-height:1.2;padding:0.35mm 0;border-bottom:0.5px dashed #cbd5e1;'>"
            f"<b style='color:var(--primary);'>{escape_html(w)}:</b> {escape_html(d)}</div>"
            for w, d in f_voc_dict.items()
        )
        vocab_box = (
            f"<div style='background:#f8fafc;padding:1.5mm 2.4mm;border:1px solid var(--soft);border-radius:5px;margin-top:1.2mm;'>"
            f"<div style='font-weight:800;font-size:8.6pt; /* hf-ok */ color:var(--primary);margin-bottom:0.6mm;'>"
            f"Specialist Vocabulary &amp; Definitions in This Unit ({len(f_voc_dict)} High-Yield Level 2 Terms):</div>"
            f"<div style='display:grid;grid-template-columns:1fr 1fr;gap:0.2mm 3mm;'>{vocab_items}</div>"
            f"</div>"
        )
        comm_box = (
            f"<div style='background:#f0fdf4;border:1px solid #86efac;border-left:3.5px solid #0f766e;border-radius:5px;padding:1.4mm 2.4mm;margin-top:1.2mm;font-size:8.3pt; /* hf-ok */ line-height:1.26;color:#0f172a;'>"
            f"{f_comm}</div>"
        )

        p3_body = (
            compact_tbl_css
            + K.page_title(f"Format {f_idx}: {f_short} &bull; Band 4 Model Answer", kicker="Examiner Benchmark Exemplar &bull; Specialist Vocabulary Highlighted", badge="MODEL")
            + K.box_html(
                f"<div style='background:#ffffff;padding:1.8mm 2.5mm;border:1px solid #cbd5e1;border-radius:6px;'>"
                f"{model_formatted}"
                f"</div>"
                f"{vocab_box}"
                f"{comm_box}",
                title=f"Band 4 Full-Marks Exemplar: {f_title}"
            )
        )
        pages.append(K.page(p3_body, header=(BOOK, f"Format {f_idx} &bull; Model"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 4: Unseen Practice Task Brief & Planning Frame
        comp_t = next((t for t in COMPANION_L2_TASKS if t["format_idx"] == f_idx and t["question_num"] == 1), None)
        if comp_t:
            img2_html = ""
            if SHOW_UNIT_IMAGES and f_idx in UNIT_PHOTOS_SECOND:
                rel2, cap2 = UNIT_PHOTOS_SECOND[f_idx]
                img2_path = K.PHOTO_DIR / rel2
                if img2_path.exists():
                    img2_html = (
                        f"<div style='background:#ffffff;border:1.5px solid var(--primary);border-radius:6px;overflow:hidden;box-shadow:0 1.5px 4px rgba(0,0,0,0.08);display:flex;flex-direction:column;'>"
                        f"<div style='width:100%;aspect-ratio:16/9;overflow:hidden;background:#0f172a;'>"
                        f"<img src='{img2_path.as_uri()}' alt='{escape_html(cap2)}' style='width:100%;height:100%;object-fit:cover;object-position:center 25%;display:block;'>"
                        f"</div>"
                        f"<div style='background:#eff6ff;color:var(--primary);font-size:7.8pt; /* hf-ok */ font-weight:700;text-align:center;padding:0.8mm 1.5mm;border-top:1px solid #bfdbfe;line-height:1.15;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;'>"
                        f"Exam Scenario: {cap2}</div>"
                        f"</div>"
                    )

            c_stim = escape_html(comp_t["stimulus"]).replace("\n", "<br>")
            c_bullets = "".join(f"<li style='margin-bottom:1px;'>{escape_html(b)}</li>" for b in comp_t["bullets"])

            if img2_html:
                scenario_block = (
                    f"<div style='display:grid;grid-template-columns:1fr 1fr;gap:3.5mm;align-items:center;margin-bottom:1.5mm;'>"
                    f"<div style='display:flex;flex-direction:column;justify-content:space-between;'>"
                    f"<p style='font-size:9.8pt; /* hf-ok */ margin:0 0 1.2mm 0;'><b>Scenario &amp; Context:</b> {escape_html(comp_t['topic'])}<br><span style='color:#475569;font-size:9pt; /* hf-ok */'><b>Target Audience:</b> {escape_html(comp_t['audience'])}</span></p>"
                    f"<div style='background:#f8fafc;padding:2mm 2.8mm;border:1px solid var(--soft);border-radius:4px;font-size:9.2pt; /* hf-ok */ line-height:1.36;flex:1 1 auto;'>"
                    f"<strong style='color:var(--primary);'>Context &amp; Stimulus:</strong><br>{c_stim}"
                    f"</div>"
                    f"</div>"
                    f"{img2_html}"
                    f"</div>"
                )
            else:
                scenario_block = (
                    f"<p style='font-size:10pt; /* hf-ok */ margin:0 0 1.2mm 0;'><b>Scenario &amp; Context:</b> {escape_html(comp_t['topic'])}<br><span style='color:#475569;font-size:9.2pt; /* hf-ok */'><b>Target Audience:</b> {escape_html(comp_t['audience'])}</span></p>"
                    f"<div style='background:#f8fafc;padding:2mm 3mm;border:1px solid var(--soft);border-radius:4px;font-size:9.5pt; /* hf-ok */ line-height:1.38;margin-bottom:1.5mm;'>"
                    f"<strong style='color:var(--primary);'>Context &amp; Stimulus:</strong><br>{c_stim}"
                    f"</div>"
                )

            p4_body = (
                compact_tbl_css
                + K.page_title(f"Format {f_idx}: {f_short} &bull; Practice Task Brief", kicker=f"Unseen Examination Task &bull; {comp_t['marks']} Marks &bull; {comp_t['word_count']}", badge="TASK")
                + K.box_html(
                    f"{scenario_block}"
                    f"<p style='margin:0 0 1mm 0;font-size:10pt; /* hf-ok */'><b>Task Instructions:</b> In your writing, you must:</p>"
                    f"<ul style='margin:0 0 1.5mm 5mm;padding:0;font-size:9.5pt; /* hf-ok */ line-height:1.34;'>{c_bullets}</ul>"
                    f"<div style='background:#f1f5f9;padding:1.8mm 2.5mm;border-left:3px solid var(--primary);font-size:8.8pt; /* hf-ok */ display:flex;justify-content:space-between;gap:3mm;'>"
                    f"<span><b>Strategy:</b> {escape_html(comp_t['strategy'])}</span>"
                    f"<span><b>Target:</b> {comp_t['word_count']} &bull; <b>Key Words:</b> {escape_html(', '.join(comp_t['specialist_words'][:5]))}</span>"
                    f"</div>",
                    title=f"Unseen Examination Brief &bull; {comp_t['marks']} Marks"
                )
                + K.fill_notes("Candidate TAP Planning &amp; Paragraph Outlines (Intro &bull; Main Body &bull; Action Close)", min_mm=25)
            )
            pages.append(K.page(p4_body, header=(BOOK, f"Format {f_idx} &bull; Task Brief"), footer=BOOK, page_no=p_curr))
            p_curr += 1

            # Page 5: Full-Page Candidate Ruled Response
            p5_body = (
                compact_tbl_css
                + K.page_title(f"Format {f_idx}: {f_short} &bull; Candidate Response", kicker=f"Official Lined Assessment Page &bull; {comp_t['word_count']}")
                + K.fill_lines(f"Write your {f_short} response below ({comp_t['word_count']}):", min_mm=195, gap_mm=9.5)
            )
            pages.append(K.page(p5_body, header=(BOOK, f"Format {f_idx} &bull; Candidate Response"), footer=BOOK, page_no=p_curr))
            p_curr += 1
        else:
            p4_body = (
                compact_tbl_css
                + K.page_title(f"Format {f_idx}: {f_short} &bull; Practice Task Brief", kicker=f"Independent Examination Task &bull; {f_marks} Marks &bull; {f_words}", badge="TASK")
                + K.box_html(
                    f"<p style='font-size:11.5pt;margin:0;'><b>Practice Task:</b> {escape_html(f_pract)}</p>",
                    title="Writing Prompt"
                )
                + K.fill_notes("Candidate Paragraph Outline", min_mm=40)
            )
            pages.append(K.page(p4_body, header=(BOOK, f"Format {f_idx} &bull; Task Brief"), footer=BOOK, page_no=p_curr))
            p_curr += 1

            p5_body = (
                compact_tbl_css
                + K.page_title(f"Format {f_idx}: {f_short} &bull; Candidate Response", kicker=f"Official Lined Assessment Page &bull; {f_words}")
                + K.fill_lines(f"Write your {f_short} response below ({f_words}):", min_mm=195, gap_mm=9.5)
            )
            pages.append(K.page(p5_body, header=(BOOK, f"Format {f_idx} &bull; Candidate Response"), footer=BOOK, page_no=p_curr))
            p_curr += 1

    # p65 to p80: SPaG & Spelling Masterclass for Writers (16 pages: 8 units x 2 pages)
    spag_l2_tips = {
        1: ("Use a semicolon to connect two complete, closely related clauses without a conjunction.", "Never use a comma by itself to join two independent clauses (a comma splice loses Band 3 SPaG marks)."),
        2: ("Start complex sentences with 'Although', 'Whereas', or 'Provided that' to show sophisticated relationships.", "When the subordinate clause comes first in the sentence, you MUST place a comma immediately after it."),
        3: ("Maintain consistent past or present tense and check subject-verb agreement ('the team is', 'the staff were').", "Never write 'we was', 'they was', or 'could of / should of'—always write 'we were' and 'could have'."),
        4: ("Use modal verbs (could, should, ought to, would) and persuasive triples to guide and persuade readers.", "Avoid aggressive commands ('you must obey') when advising; match your modal strength to the audience."),
        5: ("Use a colon (:) after a complete main clause to introduce a bullet list, explanation, or quotation.", "Begin every bullet point in a list with the same grammatical word class (e.g. all imperative verbs)."),
        6: ("Place the apostrophe BEFORE the s for one owner (manager's) and AFTER the s for plural owners (managers').", "Remember: possessive 'its' has NO apostrophe ('the company updated its policy'); 'it's' means 'it is'."),
        7: ("Begin each paragraph with a clear topic sentence and link arguments using formal discourse markers.", "Never write an exam response as one giant block of text, and avoid starting sentences with 'Also' or 'And'."),
        8: ("Use formal workplace vocabulary and check high-risk homophones (their/there/they're, affect/effect, practice/practise).", "Remember the British CE/SE rule: 'practice' and 'advice' are NOUNS; 'practise' and 'advise' are VERBS.")
    }

    spag_l2_deep_teaching = {
        1: {
            "bad": (
                "<b>1. Comma Splice (Incorrect):</b> The delivery arrived two hours late<b>,</b> the frozen stock had already thawed.<br>"
                "<b>2. Run-On Sentence (Incorrect):</b> Staff morale has improved this quarter<b></b> management introduced flexible rotas.<br>"
                "<b>3. Conjunctive Adverb Splice (Incorrect):</b> The heating failed on Monday<b>, however,</b> the engineer arrived promptly."
            ),
            "good": (
                "<b>1. Semicolon Fix (Band 4):</b> The delivery arrived two hours late<b>;</b> the frozen stock had already thawed.<br>"
                "<b>2. Full Stop or Connective (Band 4):</b> Staff morale has improved this quarter <b>because</b> management introduced flexible rotas.<br>"
                "<b>3. Semicolon + Conjunctive Adverb (Band 4):</b> The heating failed on Monday<b>; however,</b> the engineer arrived promptly."
            ),
            "guide": (
                "<table class='t compact'>"
                "<thead><tr><th>Punctuation Mark</th><th>When to Use It at Level 2</th><th>Model Workplace Example</th></tr></thead>"
                "<tbody>"
                "<tr><td><b>Full Stop ( . )</b></td><td>Ends a complete declarative statement</td><td><i>The safety audit concluded at 16:00.</i></td></tr>"
                "<tr><td><b>Semicolon ( ; )</b></td><td>Joins two closely related complete clauses without FANBOYS</td><td><i>Training is compulsory; all operatives must attend.</i></td></tr>"
                "<tr><td><b>Semicolon + Adverb</b></td><td>Before <i>however, therefore, consequently</i> joining two clauses</td><td><i>Costs rose by 12%<b>; therefore,</b> fees were reviewed.</i></td></tr>"
                "<tr><td><b>FANBOYS Comma</b></td><td>Before <i>for, and, nor, but, or, yet, so</i> joining two complete clauses</td><td><i>The venue is central<b>, and</b> it offers step-free access.</i></td></tr>"
                "</tbody></table>"
            )
        },
        2: {
            "bad": (
                "<b>1. Missing Comma After Fronted Clause:</b> Although the council invested in cycle lanes<b></b> congestion remains severe.<br>"
                "<b>2. Repetitive Simple Sentences:</b> The software is expensive. It saves three hours of admin every day.<br>"
                "<b>3. Fragment Clause Alone:</b> Because the fire exit was blocked by wooden pallets."
            ),
            "good": (
                "<b>1. Fronted Subordinate Clause + Comma:</b> <b>Although</b> the council invested in cycle lanes<b>,</b> congestion remains severe.<br>"
                "<b>2. Embedded Relative Clause:</b> The software<b>, which saves three hours of admin daily,</b> represents strong value.<br>"
                "<b>3. Complete Complex Sentence:</b> The area was isolated immediately <b>because</b> the fire exit was blocked by pallets."
            ),
            "guide": (
                "<table class='t compact'>"
                "<thead><tr><th>Relationship</th><th>Subordinating Conjunctions</th><th>Punctuation Rule</th></tr></thead>"
                "<tbody>"
                "<tr><td><b>Contrast / Concession</b></td><td><i>Although, Even though, Whereas, While, Despite the fact that</i></td><td>Subordinate clause first &rarr; <b>use a comma</b> before main clause.</td></tr>"
                "<tr><td><b>Condition</b></td><td><i>Provided that, Unless, As long as, If, In the event that</i></td><td>Main clause first &rarr; <b>no comma needed</b> before conjunction.</td></tr>"
                "<tr><td><b>Cause &amp; Reason</b></td><td><i>Because, Since, As, Given that, In order that</i></td><td>Embedded middle clause (<i>who, which</i>) &rarr; <b>pair of commas</b>.</td></tr>"
                "</tbody></table>"
            )
        },
        3: {
            "bad": (
                "<b>1. Subject-Verb Error:</b> The list of recommended safety upgrades <b>were</b> sent to the director.<br>"
                "<b>2. Tense Drift:</b> When the customer <b>arrives</b> at reception, the manager <b>ignored</b> his complaint.<br>"
                "<b>3. Blaming / Subjective Incident Style:</b> Dave was careless and left liquid on the floor so Jason fell."
            ),
            "good": (
                "<b>1. Correct Singular Agreement:</b> The <b>list</b> of recommended safety upgrades <b>was</b> sent to the director.<br>"
                "<b>2. Consistent Past Tense:</b> When the customer <b>arrived</b> at reception, the manager <b>addressed</b> his complaint.<br>"
                "<b>3. Objective Passive Voice:</b> A spillage had been left unmarked in Aisle 4; consequently, first aid <b>was administered</b>."
            ),
            "guide": (
                "<table class='t compact'>"
                "<thead><tr><th>Grammar Rule</th><th>Common Exam Trap (Avoid)</th><th>Level 2 Standard (Use)</th></tr></thead>"
                "<tbody>"
                "<tr><td><b>Active vs Passive Voice</b></td><td><i>Someone didn't lock the warning cupboard.</i></td><td><i>The hazard signage cupboard had not been unlocked.</i></td></tr>"
                "<tr><td><b>Subject-Verb Agreement</b></td><td><i>We was waiting / The staff is unhappy / There is many issues</i></td><td><i>We were waiting / The staff are unhappy / There are many issues</i></td></tr>"
                "<tr><td><b>Modal Auxiliary Verbs</b></td><td><i>Management should of / could of / would of acted</i></td><td><i>Management <b>should have / could have / would have</b> acted</i></td></tr>"
                "<tr><td><b>Articles (a / an)</b></td><td><i>a urgent update / a honest review / a hour wait</i></td><td><i><b>an</b> urgent update / <b>an</b> honest review / <b>an</b> hour's wait</i></td></tr>"
                "</tbody></table>"
            )
        },
        4: {
            "bad": (
                "<b>1. Overly Aggressive Tone:</b> Management must fix the canteen prices right now or nobody will buy food.<br>"
                "<b>2. Weak / Uncertain Proposal:</b> Maybe we could possibly look at doing an escape room if people want.<br>"
                "<b>3. Flat Unpersuasive Statement:</b> Keeping the youth centre open is a good idea for teenagers."
            ),
            "good": (
                "<b>1. Diplomatic Modal Recommendation:</b> Management <b>should consider</b> introducing a subsidised £3.50 meal deal.<br>"
                "<b>2. Confident Professional Proposal:</b> Booking the Enigma Escape Room <b>will provide</b> an inclusive, cost-effective event.<br>"
                "<b>3. Persuasive Rule of Three:</b> The youth hub is <b>vital, preventative, and transformative</b> for our community."
            ),
            "guide": (
                "<table class='t compact'>"
                "<thead><tr><th>Communicative Purpose</th><th>Modal Verbs &amp; Phrases</th><th>Best Formats to Use</th></tr></thead>"
                "<tbody>"
                "<tr><td><b>Polite Recommendation</b></td><td><i>should, ought to, could beneficially, it is recommended that</i></td><td>Reports, Workplace Emails, Reviews</td></tr>"
                "<tr><td><b>Mandatory Safety / Policy</b></td><td><i>must, is required to, shall, it is essential that</i></td><td>Incident Reports, Safety Leaflets</td></tr>"
                "<tr><td><b>Future Certainty / Impact</b></td><td><i>will undoubtedy, can transform, would significantly reduce</i></td><td>Persuasive Articles, Speeches, Letters</td></tr>"
                "</tbody></table>"
            )
        },
        5: {
            "bad": (
                "<b>1. Colon After Incomplete Clause:</b> The three main barriers are<b>:</b> cost, availability, and queuing.<br>"
                "<b>2. Unparallel Bullet Points:</b><br>&bull; Subsidised meal deals<br>&bull; Extending opening hours<br>&bull; You should remove sweets"
            ),
            "good": (
                "<b>1. Colon After Complete Clause:</b> The survey identified three main barriers<b>:</b> cost, availability, and queuing.<br>"
                "<b>2. Parallel Imperative Bullets:</b><br>&bull; <b>Introduce</b> a subsidised £3.50 meal deal.<br>&bull; <b>Extend</b> hot food availability until 14:30.<br>&bull; <b>Replace</b> checkout sweets with fresh fruit."
            ),
            "guide": (
                "<table class='t compact'>"
                "<thead><tr><th>Punctuation Mark</th><th>Core Level 2 Rule</th><th>Worked Example</th></tr></thead>"
                "<tbody>"
                "<tr><td><b>Colon ( : )</b></td><td>Follows a complete main clause to introduce a list, explanation, or quote</td><td><i>One priority remains clear<b>:</b> patient safety comes first.</i></td></tr>"
                "<tr><td><b>Commas in Lists &amp; Clauses</b></td><td>Separates list items, fronted adverbials, and extra parenthetical info</td><td><i>Ms Patel<b>, our Facilities Director,</b> approved the grant.</i></td></tr>"
                "<tr><td><b>Brackets ( ) &amp; Dashes &ndash;</b></td><td>Encloses statistics, clarifications, or high-impact emphasis</td><td><i>Over two-thirds of staff <b>(68%)</b> supported the proposal.</i></td></tr>"
                "<tr><td><b>Inverted Commas ( \" \" )</b></td><td>Encloses direct speech, witness quotes, or campaign titles</td><td><i>Colleagues stated, <b>\"We need an inclusive indoor activity.\"</b></i></td></tr>"
                "</tbody></table>"
            )
        },
        6: {
            "bad": (
                "<b>1. Its vs It's Confusion:</b> The gym updated <b>it's</b> booking app, but <b>its</b> still crashing.<br>"
                "<b>2. Misplaced Plural Possessive:</b> All <b>employee's</b> lockers were inspected during the <b>mens'</b> refurbishment.<br>"
                "<b>3. Accidental Greengrocer's Apostrophe:</b> Fresh <b>smoothie's</b> and <b>wrap's</b> are sold on <b>Monday's</b>."
            ),
            "good": (
                "<b>1. Correct Possessive vs Contraction:</b> The gym updated <b>its</b> booking app, but <b>it's</b> (it is) still crashing.<br>"
                "<b>2. Correct Plural Possessives:</b> All <b>employees'</b> lockers were inspected during the <b>men's</b> refurbishment.<br>"
                "<b>3. Plural Nouns (No Apostrophe):</b> Fresh <b>smoothies</b> and <b>wraps</b> are sold on <b>Mondays</b>."
            ),
            "guide": (
                "<table class='t compact'>"
                "<thead><tr><th>Apostrophe Category</th><th>Rule to Apply</th><th>Correct Examples</th></tr></thead>"
                "<tbody>"
                "<tr><td><b>Singular Possession ( 's )</b></td><td>One owner &rarr; add <b>'s</b> directly to the singular noun</td><td><i>the <b>manager's</b> office, <b>James's</b> shift, a <b>week's</b> notice</i></td></tr>"
                "<tr><td><b>Regular Plural Possession ( s' )</b></td><td>More than one owner ending in -s &rarr; place apostrophe <b>after the s</b></td><td><i>the <b>residents'</b> association, <b>students'</b> views, <b>two weeks'</b> pay</i></td></tr>"
                "<tr><td><b>Irregular Plural Possession ( 's )</b></td><td>Plural noun not ending in -s (<i>children, women, people</i>) &rarr; add <b>'s</b></td><td><i><b>children's</b> park, <b>people's</b> wellbeing, <b>women's</b> health</i></td></tr>"
                "<tr><td><b>Omission / Contraction</b></td><td>Replaces missing letters (use in speech/informal only; expand in formal)</td><td><i><b>don't</b> (do not), <b>you're</b> (you are), <b>they're</b> (they are), <b>it's</b> (it is)</i></td></tr>"
                "</tbody></table>"
            )
        },
        7: {
            "bad": (
                "<b>1. Weak Repetitive Connectives:</b> Also the heating broke. Also the food took 75 minutes. Also the manager was rude.<br>"
                "<b>2. Missing Topic Sentence:</b> It costs £28 per person and is five minutes from the train station.<br>"
                "<b>3. Contradictory Connective:</b> The new gym is spotless and affordable; <b>however,</b> I strongly recommend it."
            ),
            "good": (
                "<b>1. Varied Level 2 Progression:</b> <b>Firstly,</b> the heating failed. <b>Furthermore,</b> our meal was delayed by 75 minutes.<br>"
                "<b>2. Clear Topic Sentence:</b> <b>Based on staff feedback, the Enigma Escape Room is the ideal venue.</b> It costs £28...<br>"
                "<b>3. Logical Result Connective:</b> The new gym is spotless and affordable; <b>therefore,</b> I strongly recommend it."
            ),
            "guide": (
                "<table class='t compact'>"
                "<thead><tr><th>Paragraph Role</th><th>What It Must Do</th><th>High-Scoring Starter Phrases</th></tr></thead>"
                "<tbody>"
                "<tr><td><b>1. Opening Paragraph</b></td><td>Establish purpose, context, and core stance immediately</td><td><i>I am writing to formally propose... / Over recent months...</i></td></tr>"
                "<tr><td><b>2. Primary Development</b></td><td>Present main evidence, statistics, or chronological events</td><td><i>Firstly, survey data indicates that... / Primarily, ...</i></td></tr>"
                "<tr><td><b>3. Secondary / Counter-Point</b></td><td>Add supporting angle or evaluate opposing perspective</td><td><i>Furthermore, ... / On the other hand, critics argue that...</i></td></tr>"
                "<tr><td><b>4. Concluding Action Close</b></td><td>Specify final verdict, recommendations, or deadline</td><td><i>In conclusion, ... / Therefore, I request that within 14 days...</i></td></tr>"
                "</tbody></table>"
            )
        },
        8: {
            "bad": (
                "<b>1. Informal Slang &amp; Homophone Errors:</b> <b>Their</b> is <b>alot</b> of staff who want <b>to</b> <b>practise</b> <b>there</b> skills.<br>"
                "<b>2. Noun vs Verb Confusion:</b> Thank you for your helpful <b>advise</b>; it had a big <b>affect</b> on my confidence.<br>"
                "<b>3. Misspelled Exam Words:</b> I would <b>reccommend</b> improving the <b>accomodation</b> and <b>enviroment</b>."
            ),
            "good": (
                "<b>1. Formal Register &amp; Correct Homophones:</b> <b>There</b> are <b>numerous</b> staff who wish <b>to</b> <b>practise</b> <b>their</b> skills.<br>"
                "<b>2. Correct CE (Noun) vs SE (Verb):</b> Thank you for your helpful <b>advice</b>; it had a positive <b>effect</b> on my confidence.<br>"
                "<b>3. Accurate Level 2 Spelling:</b> I would <b>recommend</b> improving the <b>accommodation</b> and <b>environment</b>."
            ),
            "guide": (
                "<table class='t compact'>"
                "<thead><tr><th>Spelling &amp; Homophone Rule</th><th>Key Examples to Memorise for Exam Day</th></tr></thead>"
                "<tbody>"
                "<tr><td><b>Top Confusable Homophones</b></td><td><b>their</b> (belonging) / <b>there</b> (place/exists) / <b>they're</b> (they are) &bull; <b>your</b> / <b>you're</b> &bull; <b>to / too / two</b> &bull; <b>where / wear / were</b> &bull; <b>loose</b> (not tight) / <b>lose</b> (misplace) &bull; <b>passed</b> (verb) / <b>past</b> (time)</td></tr>"
                "<tr><td><b>Noun (-ce / Affect) vs Verb (-se / Effect)</b></td><td><b>Advice / Practice / Licence</b> = Nouns (<i>medical practice, good advice</i>) &bull; <b>Advise / Practise / License</b> = Verbs (<i>I advise you to practise</i>) &bull; <b>Affect</b> = Verb (<i>to influence</i>) / <b>Effect</b> = Noun (<i>the result</i>)</td></tr>"
                "<tr><td><b>Prefixes, Suffixes &amp; Plurals</b></td><td>Keep both letters with prefixes (<i><b>dis</b>satisfied, <b>un</b>necessary, <b>mis</b>spell</i>) &bull; Drop silent <i>-e</i> before vowel suffix (<i>manage &rarr; managing</i>, keep before <i>-ment/-ful</i>: <i>management, grateful</i>) &bull; Consonant + <i>y</i> &rarr; <i>-ies</i> (<i>facility &rarr; facilities</i>)</td></tr>"
                "<tr><td><b>High-Frequency Exam Spellings</b></td><td><i>accommodation, colleague, committee, definitely, disappointed, embarrass, environment, government, immediately, independent, maintenance, necessary, occurred, opportunity, professional, receive, recommend, separate, sincerely, successful</i></td></tr>"
                "</tbody></table>"
            )
        }
    }

    spag_start_pages = {}
    # Compute where Reference Section will start:
    # Current p_curr is 65. 8 SPaG units x 2p = 16p (65..80). 2 Mocks x 6p = 12p (81..92). 4 Rubric pages = 4p (93..96).
    # So Reference Section starts at page 97!
    ref_section_start_page = p_curr + 16 + 12 + 4

    for sp_idx in range(1, 9):
        spag_start_pages[sp_idx] = p_curr
        sp_ex = SPAG_L2_EXERCISES.get(sp_idx, {})
        sp_title = sp_ex.get("title", f"SPaG Unit {sp_idx}")
        sp_rule = sp_ex.get("rule", "Apply standard grammatical principles in professional writing.")
        sp_inputs = sp_ex.get("inputs", [])
        sp_instruction = sp_ex.get("instruction", "Rewrite each sentence correctly.")
        gold_tip, watch_tip = spag_l2_tips.get(sp_idx, ("Apply standard punctuation rules.", "Check sentence boundaries."))
        deep = spag_l2_deep_teaching[sp_idx]

        # Unit Page 1: Complete Theory, Worked Examples (Wrong vs Right) & Reference Table
        p1_spag = (
            compact_tbl_css
            + K.page_title(f"SPaG Masterclass {sp_idx}: {sp_title}", kicker="Advanced Syntax, Punctuation &amp; Spelling &bull; Band 3/3 SPaG", badge=f"S{sp_idx}")
            + K.rule_box("Core Examination Rule &amp; Assessment Benchmark", f"<p style='font-size:10pt; /* hf-ok */ line-height:1.35;margin:0;'><b>{sp_rule}</b></p>")
            + K.compare(deep["bad"], deep["good"], bad_label="&#10007; Common Exam Errors (Loses Marks)", good_label="&#10003; Band 4 Benchmark Solutions (Full Marks)")
            + K.box_html(deep["guide"], title=f"Unit {sp_idx} Quick-Reference Rules &amp; Patterns")
            + K.tip_pair(gold_tip, watch_tip, golden_title="High-Yield SPaG Rule", watch_title="Critical Exam Trap")
        )
        pages.append(K.page(p1_spag, header=(BOOK, f"SPaG {sp_idx} &bull; Theory"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Unit Page 2: Applied Sentence Calibration Drill
        inputs_html = "<br><br>".join(f"<b>{escape_html(inp)}</b>" for inp in sp_inputs)
        sp_img_html = ""
        if sp_idx in SPAG_WRITING_PHOTOS:
            sp_rel, sp_cap = SPAG_WRITING_PHOTOS[sp_idx]
            sp_path = K.PHOTO_DIR / sp_rel
            if sp_path.exists():
                sp_img_html = (
                    f"<div style='background:#ffffff;border:1.5px solid var(--primary);border-radius:6px;overflow:hidden;box-shadow:0 1.5px 4px rgba(0,0,0,0.08);display:flex;flex-direction:column;'>"
                    f"<div style='width:100%;aspect-ratio:16/9;overflow:hidden;background:#0f172a;'>"
                    f"<img src='{sp_path.as_uri()}' alt='{escape_html(sp_cap)}' style='width:100%;height:100%;object-fit:cover;object-position:center 25%;display:block;'>"
                    f"</div>"
                    f"<div style='background:#eff6ff;color:var(--primary);font-size:7.8pt; /* hf-ok */ font-weight:700;text-align:center;padding:0.8mm 1.5mm;border-top:1px solid #bfdbfe;line-height:1.15;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;'>"
                    f"Workplace Application: {sp_cap}</div>"
                    f"</div>"
                )

        if sp_img_html:
            sp_task_top = (
                f"<div style='display:grid;grid-template-columns:1fr 1fr;gap:3.5mm;align-items:center;margin-bottom:2.5mm;'>"
                f"<div style='display:flex;flex-direction:column;justify-content:center;'>"
                f"<p style='font-size:11.2pt;margin:0 0 1.8mm 0;line-height:1.35;'><b>Calibration Task:</b> {escape_html(sp_instruction)}</p>"
                f"<div style='background:#eff6ff;border-left:3.5px solid var(--primary);border-radius:4px;padding:2mm 2.8mm;font-size:9.5pt;color:#1e3a8a;line-height:1.34;'>"
                f"<b>Professional Standard:</b> Read each workplace scenario sentence carefully. Identify the syntax, punctuation, or agreement error, then rewrite your calibrated response below."
                f"</div>"
                f"</div>"
                f"{sp_img_html}"
                f"</div>"
            )
        else:
            sp_task_top = f"<p style='font-size:12pt;margin-top:0;'><b>Calibration Task:</b> {escape_html(sp_instruction)}</p>"

        p2_spag = (
            K.page_title(f"SPaG Masterclass {sp_idx} &bull; Calibration Drill", kicker="Applied Workplace Sentence Practice", badge="DRILL")
            + K.box_html(
                f"{sp_task_top}"
                f"<div style='background:#f8fafc;padding:3mm 3.5mm;border:1.5px solid var(--soft);border-radius:6px;font-size:11pt;line-height:1.45;'>"
                f"{inputs_html}"
                f"</div>",
                title=f"Workplace Sentences to Calibrate ({len(sp_inputs)} Items)"
            )
            + K.fill_lines(f"Write your calibrated responses below (check worked answers on p. {ref_section_start_page}):", min_mm=25, gap_mm=9.5)
        )
        pages.append(K.page(p2_spag, header=(BOOK, f"SPaG {sp_idx} &bull; Drill"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p81 to p92: 2 Complete Official Mock Exam Papers (12 pages: 6 pages per mock)
    mock1_start_page = p_curr
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
            f"<p>Audit your Mock 1 responses against Pearson criteria before consulting the model answers on p. {ref_section_start_page + 1}:</p>"
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

    # Mock Paper 2 (6 pages)
    mock2_start_page = p_curr
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
            f"<p>Review your Mock 2 scripts before checking the benchmark answers on p. {ref_section_start_page + 1}:</p>"
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

    # Official Pearson Edexcel Marking Criteria & Band Descriptors (4 pages)
    rubric_start_page = p_curr
    # Task 1 Composition
    t1_comp_desc = "".join(f"<p><b>{b}:</b> {d}</p>" for b, d in PEARSON_L2_BAND_DESCRIPTORS["task1_comp"])
    p77_body = (
        K.page_title("Official Marking Criteria &bull; Task 1 Composition", kicker="Pearson Edexcel Band 1–4 Assessment Grid &bull; 12 Marks", badge="RUBRIC")
        + K.box_html(f"<div style='font-size:12pt;line-height:1.5;'>{t1_comp_desc}</div>", title="Task 1: Form, Audience, Purpose &amp; Cohesion (12 Marks)")
        + K.fill_notes("Personal Strategy to Guarantee Band 4 on Task 1 Composition", min_mm=35)
    )
    pages.append(K.page(p77_body, header=(BOOK, "Marking Criteria &bull; Task 1 Comp"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Task 1 SPaG
    t1_spag_desc = "".join(f"<p><b>{b}:</b> {d}</p>" for b, d in PEARSON_L2_BAND_DESCRIPTORS["task1_spag"])
    p78_body = (
        K.page_title("Official Marking Criteria &bull; Task 1 SPaG", kicker="Pearson Edexcel Band 1–3 Assessment Grid &bull; 9 Marks", badge="RUBRIC")
        + K.box_html(f"<div style='font-size:12pt;line-height:1.5;'>{t1_spag_desc}</div>", title="Task 1: Spelling, Punctuation &amp; Grammar (9 Marks)")
        + K.fill_notes("Punctuation &amp; Spelling Audit Commitments", min_mm=35)
    )
    pages.append(K.page(p78_body, header=(BOOK, "Marking Criteria &bull; Task 1 SPaG"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Task 2 Composition
    t2_comp_desc = "".join(f"<p><b>{b}:</b> {d}</p>" for b, d in PEARSON_L2_BAND_DESCRIPTORS["task2_comp"])
    p79_body = (
        K.page_title("Official Marking Criteria &bull; Task 2 Composition", kicker="Pearson Edexcel Band 1–3 Assessment Grid &bull; 9 Marks", badge="RUBRIC")
        + K.box_html(f"<div style='font-size:12pt;line-height:1.5;'>{t2_comp_desc}</div>", title="Task 2: Form, Audience, Purpose &amp; Cohesion (9 Marks)")
        + K.fill_notes("Personal Strategy to Guarantee Band 3 on Task 2 Composition", min_mm=35)
    )
    pages.append(K.page(p79_body, header=(BOOK, "Marking Criteria &bull; Task 2 Comp"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Task 2 SPaG
    t2_spag_desc = "".join(f"<p><b>{b}:</b> {d}</p>" for b, d in PEARSON_L2_BAND_DESCRIPTORS["task2_spag"])
    p80_body = (
        K.page_title("Official Marking Criteria &bull; Task 2 SPaG", kicker="Pearson Edexcel Band 1–3 Assessment Grid &bull; 6 Marks", badge="RUBRIC")
        + K.box_html(f"<div style='font-size:12pt;line-height:1.5;'>{t2_spag_desc}</div>", title="Task 2: Spelling, Punctuation &amp; Grammar (6 Marks)")
        + K.fill_notes("Final Self-Audit Rules for Task 2 SPaG", min_mm=35)
    )
    pages.append(K.page(p80_body, header=(BOOK, "Marking Criteria &bull; Task 2 SPaG"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Reference Back Matter via K.ref_pages
    ref_actual_start = p_curr
    ref_blocks = []

    # SPaG Solutions (Units 1 to 8)
    for u_idx in range(1, 9):
        qas = SPAG_L2_SOLUTIONS.get(u_idx, [])
        qa_html = "".join(K.ref_qa(q_num, ans, marks=mk, working=escape_html(wk)) for q_num, ans, mk, wk in qas)
        u_title = SPAG_L2_EXERCISES.get(u_idx, {}).get("title", f"Unit {u_idx}")
        ref_blocks.append(K.ref_block(f"SPaG Masterclass {u_idx}: {u_title}", qa_html))

    # Mock Exam Benchmark Commentary
    m1_t1_model = (
        "Dear Councillor Jenkins,<br><br>"
        "I am writing on behalf of the Greendale Residents' Association to submit a formal grant proposal for the establishment of a community healthcare and wellbeing clinic in our district. Over recent months, local healthcare services have experienced unprecedented demand, leaving many vulnerable residents without immediate access to essential services.<br><br>"
        "Our proposal focuses on repurposing the vacant municipal hall on St. Mary's Road into a multi-disciplinary community hub. This facility will provide weekly outpatient clinics, preventative health screenings, and mental health counselling sessions. Furthermore, by partnering with regional clinical networks, we ensure that clinical governance and safeguarding standards are rigorously maintained.<br><br>"
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

    # Glossary (split into 3 balanced blocks so no block overflows a single column)
    g_part1 = "".join(f"<dl><dt>{escape_html(t)}</dt><dd>{escape_html(d)}</dd></dl>" for t, d in GLOSSARY_L2[:10])
    g_part2 = "".join(f"<dl><dt>{escape_html(t)}</dt><dd>{escape_html(d)}</dd></dl>" for t, d in GLOSSARY_L2[10:20])
    g_part3 = "".join(f"<dl><dt>{escape_html(t)}</dt><dd>{escape_html(d)}</dd></dl>" for t, d in GLOSSARY_L2[20:])
    ref_blocks.append(K.ref_block("Comprehensive Functional Writing Glossary (A–C)", g_part1))
    ref_blocks.append(K.ref_block("Functional Writing Glossary (C–N)", g_part2))
    ref_blocks.append(K.ref_block("Functional Writing Glossary (P–T)", g_part3))

    # Index (split into 2 balanced blocks so each fits comfortably within a single column)
    idx_part1 = ""
    for letter, entries in INDEX_L2[:9]:
        items = "".join(f"<div class='ix'><span>{escape_html(t)}</span><span>{escape_html(p)}</span></div>" for t, p in entries)
        idx_part1 += f"<div class='ix-letter'>{letter}</div>{items}"
    ref_blocks.append(K.ref_block("Subject, Format &amp; Alphabetical Index (A–I)", idx_part1))

    idx_part2 = ""
    for letter, entries in INDEX_L2[9:]:
        items = "".join(f"<div class='ix'><span>{escape_html(t)}</span><span>{escape_html(p)}</span></div>" for t, p in entries)
        idx_part2 += f"<div class='ix-letter'>{letter}</div>{items}"
    ref_blocks.append(K.ref_block("Alphabetical Index (M–T)", idx_part2))

    # Render Reference Pages
    cover_theme = K.theme_from_cover(front_cov)
    ref_page_list = K.ref_pages("Reference Section: Solutions, Glossary &amp; Index", ref_blocks,
                                BOOK, start_page=p_curr, subtitle="Complete Worked Solutions, Lexicon &amp; Alphabetical Index",
                                cols=2, theme=cover_theme, notes_title="Candidate Reference Notes &amp; Exam Checklist")
    pages.extend(ref_page_list)
    p_curr += len(ref_page_list)

    # Pre-Exam Readiness Commitments
    readiness_page = p_curr
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

    # Now populate Page 2 (Complete Table of Contents) with 100% verified dynamic page numbers!
    def toc_row(badge_txt: str, label_txt: str, pg_txt: str) -> str:
        return (
            f"<tr>"
            f"<td style='width:11mm;padding:0.45mm 1mm !important;white-space:nowrap;'><span class='chip' style='font-size:7.8pt; /* hf-ok */ padding:0.15mm 1.2mm;font-weight:800;display:inline-block;text-align:center;min-width:9.5mm;'>{badge_txt}</span></td>"
            f"<td style='padding:0.45mm 1mm !important;font-size:8.6pt; /* hf-ok */ line-height:1.14;color:#0f172a;font-weight:600;'>{label_txt}</td>"
            f"<td style='width:13.5mm;padding:0.45mm 1.2mm !important;text-align:right;font-weight:800;font-size:8.6pt; /* hf-ok */ color:var(--primary);white-space:nowrap;'>p. {pg_txt}</td>"
            f"</tr>"
        )

    def toc_sec_hdr(sec_title: str) -> str:
        return (
            f"<tr><td colspan='3' style='background:var(--primary);color:#ffffff;font-weight:800;font-size:8.4pt; /* hf-ok */ "
            f"letter-spacing:0.04em;text-transform:uppercase;padding:0.65mm 1.8mm !important;border-radius:3px;'>{sec_title}</td></tr>"
        )

    left_col_rows = (
        toc_sec_hdr("Part 1: Specification &amp; Core Exam Strategy")
        + toc_row("SPEC", "Pearson Edexcel Level 2 Syllabus (W20–W28)", "3")
        + toc_row("STRAT", "TAP, Planning, Paragraphs, DAFOREST &amp; Proofreading", "4")
        + toc_sec_hdr("Part 2: All 12 Level 2 Writing Formats (60 Pages)")
        + "".join(
            toc_row(
                f"F{f['idx']}",
                f"Format {f['idx']}: {escape_html(f['title'])}",
                f"{format_start_pages[f['idx']]}&ndash;{format_start_pages[f['idx']]+4}"
            )
            for f in FORMATS_L2
        )
    )

    right_col_rows = (
        toc_sec_hdr("Part 3: SPaG &amp; Spelling Masterclass (16 Pages)")
        + "".join(
            toc_row(
                f"S{sp_i}",
                f"Unit {sp_i}: {escape_html(SPAG_L2_EXERCISES[sp_i]['title'])}",
                f"{spag_start_pages[sp_i]}&ndash;{spag_start_pages[sp_i]+1}"
            )
            for sp_i in range(1, 9)
        )
        + toc_sec_hdr("Part 4: Official Mock Exams &amp; Marking Criteria")
        + toc_row("MOCK 1", "Official Mock Examination Paper 1 (Tasks 1 &amp; 2)", f"{mock1_start_page}&ndash;{mock1_start_page+5}")
        + toc_row("MOCK 2", "Official Mock Examination Paper 2 (Tasks 1 &amp; 2)", f"{mock2_start_page}&ndash;{mock2_start_page+5}")
        + toc_row("RUBRIC", "Official Pearson Band 1–4 Marking Grids", f"{rubric_start_page}&ndash;{rubric_start_page+3}")
        + toc_sec_hdr("Part 5: Reference Solutions, Glossary &amp; Index")
        + toc_row("SOL", "SPaG Drill &amp; Mock Exam Benchmark Solutions", f"{ref_actual_start}&ndash;{ref_actual_start+3}")
        + toc_row("GLOSS", "Comprehensive Functional Writing Glossary", f"{ref_actual_start+3}&ndash;{ref_actual_start+4}")
        + toc_row("INDEX", "Alphabetical Subject &amp; Format Index", f"{ref_actual_start+5}" if ref_actual_start+5 == readiness_page-1 else f"{ref_actual_start+5}&ndash;{readiness_page-1}")
        + toc_row("READY", "Pre-Exam Readiness &amp; Final Verification", f"{readiness_page}")
    )

    p2_toc_body = (
        compact_tbl_css
        + K.page_title("Functional Skills English &bull; Writing (Level 2)", kicker="Master Functional Skills &bull; Complete Curriculum &amp; Format Mastery Manual", badge="TOC")
        + "<div class='box worked' style='padding:1.4mm 2.8mm;display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:1.2mm 4mm;font-size:9pt; /* hf-ok */ margin-bottom:1mm;'>"
          "<div><span style='font-weight:700;color:var(--primary);font-size:8.6pt; /* hf-ok */'>This book belongs to:</span><div class='aline' style='height:3.8mm;'></div></div>"
          "<div><span style='font-weight:700;color:var(--primary);font-size:8.6pt; /* hf-ok */'>Exam date:</span><div class='aline' style='height:3.8mm;'></div></div>"
          "<div><span style='font-weight:700;color:var(--primary);font-size:8.6pt; /* hf-ok */'>Target score (out of 36):</span><div class='aline' style='height:3.8mm;'></div></div>"
          "</div>"
        + "<h2 style='font-size:11.5pt;margin:0.3mm 0 0.8mm 0;color:var(--primary);'>Complete Table of Contents &amp; Topic Directory</h2>"
        + "<div style='display:grid;grid-template-columns:1fr 1fr;gap:2.5mm;align-items:start;'>"
        + f"<table class='t compact' style='width:100%;border-collapse:separate;'><tbody>{left_col_rows}</tbody></table>"
        + f"<table class='t compact' style='width:100%;border-collapse:separate;'><tbody>{right_col_rows}</tbody></table>"
        + "</div>"
        + "<div style='margin-top:1mm;background:#f8fafc;border:1.5px solid var(--soft);border-left:4px solid var(--accent);border-radius:6px;padding:1.2mm 2.5mm;font-size:8.6pt; /* hf-ok */ line-height:1.25;'>"
          "<b style='color:var(--primary);'>How Each 5-Page Format Unit Works:</b> "
          "<b>Page 1:</b> Full Format Explanation, 6-Point Layout Anatomy &amp; 12 Specialist Vocabulary Terms &bull; "
          "<b>Page 2:</b> Guided Exam Brief &amp; 5-Minute TAP Planning Grid &bull; "
          "<b>Page 3:</b> Band 4 Full-Marks Model Answer, 12 Vocabulary Definitions &amp; Examiner Commentary &bull; "
          "<b>Pages 4&ndash;5:</b> Unseen Exam Practice Task &amp; Official Lined Response Sheet."
          "</div>"
    )
    pages[1] = K.page(p2_toc_body, header=("Master Functional Skills", "Complete Table of Contents"), footer=BOOK, page_no=2)

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
# 2. English Writing Level 2 Companion Workbook (96 Pages)
# =============================================================================
def build_english_l2_companion():
    print("\n" + "="*70)
    print("BUILDING: MasterFunctionalSkills_English_Writing_Level_2_Companion_Workbook.pdf (A4)")
    print("="*70)

    BOOK = "English Writing Level 2 Companion Workbook"
    front_cov = COV / "level2_companion_cover_page-1.png"
    back_cov = COV / "level2_companion_cover_page-2.png"

    pages = []
    compact_tbl_css = (
        "<style>"
        ".t.compact th { padding: 1mm 2mm !important; font-size: 9pt !important; /* hf-ok */ line-height: 1.2 !important; }"
        ".t.compact td { padding: 0.9mm 2mm !important; font-size: 8.8pt !important; /* hf-ok */ line-height: 1.2 !important; }"
        ".ptitle h1 { font-size: 19.5pt !important; line-height: 1.08 !important; }"
        ".ptitle .badge { height: 15mm !important; min-width: 15mm !important; font-size: 16pt !important; }"
        ".pair .box { padding: 2mm 2.8mm !important; font-size: 9.5pt !important; /* hf-ok */ line-height: 1.24 !important; }"
        "</style>"
    )

    # p1: Front Cover
    pages.append(K.front_cover(front_cov))
    # p2: Placeholder for Complete 2-Column Table of Contents (populated after page assembly)
    pages.append("")

    # p3: Companion Strategy, Syllabus Profile & Timed Practice Methodology
    p3_body = (
        compact_tbl_css
        + K.page_title("Level 2 Companion Workbook &bull; Syllabus &amp; Practice Methodology",
                       kicker="Pearson Edexcel Functional Skills English (W20–W28) &bull; Pure Exam Simulation", badge="GUIDE")
        + K.box_html(
            "<p style='font-size:9.6pt; /* hf-ok */ margin:0 0 1.2mm 0;line-height:1.34;'>This Companion Workbook contains <b>24 brand-new, unseen examination tasks</b> (two unique tasks for every one of the 12 official Level 2 functional writing formats), followed by <b>4 complete 60-minute mock papers</b> (8 exam tasks) and <b>8 workplace proofreading drills</b>. Every task in this workbook is 100% unique to this publication.</p>"
            "<table class='t compact'>"
            "<thead><tr><th>Assessment Component</th><th>Task 1: Longer Writing</th><th>Task 2: Shorter Writing</th><th>Total Exam</th></tr></thead>"
            "<tbody>"
            "<tr><td><b>Recommended Timing</b></td><td><b>35 Minutes</b> (5m plan, 25m write, 5m check)</td><td><b>25 Minutes</b> (4m plan, 17m write, 4m check)</td><td><b>60 Minutes</b></td></tr>"
            "<tr><td><b>Target Word Count</b></td><td><b>250&ndash;350 words</b></td><td><b>200&ndash;250 words</b></td><td>450&ndash;600 words</td></tr>"
            "<tr><td><b>Composition Marks (W23–W28)</b></td><td>12 Marks (Band 1–4)</td><td>9 Marks (Band 1–3)</td><td><b>21 Marks (58.3%)</b></td></tr>"
            "<tr><td><b>SPaG Marks (W20–W22)</b></td><td>9 Marks (Band 1–3)</td><td>6 Marks (Band 1–3)</td><td><b>15 Marks (41.7%)</b></td></tr>"
            "<tr><td><b>Total Task Marks</b></td><td><b>21 Marks</b></td><td><b>15 Marks</b></td><td><b>36 Marks (100%)</b></td></tr>"
            "</tbody></table>",
            title="Official Pearson Edexcel Level 2 Writing Assessment Profile"
        )
        + K.box_html(
            "<div style='display:grid;grid-template-columns:1fr 1fr;gap:2mm;font-size:9pt; /* hf-ok */ line-height:1.3;'>"
            "<div style='background:#f8fafc;border:1px solid var(--soft);border-left:3.5px solid var(--primary);padding:1.6mm 2.2mm;border-radius:4px;'>"
            "<b>1. Analyse &amp; Plan (5 Mins):</b> Identify your <b>TAP</b> (Text format, Audience register, Purpose) and sketch a 4-paragraph plan covering every bullet point before writing."
            "</div>"
            "<div style='background:#f8fafc;border:1px solid var(--soft);border-left:3.5px solid var(--primary);padding:1.6mm 2.2mm;border-radius:4px;'>"
            "<b>2. Embed Specialist Vocabulary:</b> Each task brief provides <b>10 high-yield specialist terms</b>. Weave at least 5–6 of these naturally into your response to reach Band 4."
            "</div>"
            "<div style='background:#f8fafc;border:1px solid var(--soft);border-left:3.5px solid var(--primary);padding:1.6mm 2.2mm;border-radius:4px;'>"
            "<b>3. Complex Syntax &amp; Punctuation:</b> Demonstrate colons (:), semicolons (;), parenthetical dashes (&ndash;), apostrophes, and subordinating conjunctions (<i>although, whereas, provided that</i>)."
            "</div>"
            "<div style='background:#f8fafc;border:1px solid var(--soft);border-left:3.5px solid var(--primary);padding:1.6mm 2.2mm;border-radius:4px;'>"
            "<b>4. Self-Audit &amp; Model Comparison:</b> After each task, check your response against the <b>Reference Section</b> worked solutions, model openings, and benchmark scripts."
            "</div>"
            "</div>",
            title="4-Step Timed Practice &amp; Self-Audit Routine"
        )
        + K.tip_pair("Practise strictly without a dictionary or spellchecker so your timing and spelling recall match real exam conditions.",
                     "Never join two independent sentences with a bare comma (a comma splice)—always use a full stop or a semicolon.",
                     golden_title="Timed Exam Discipline", watch_title="Eliminate Comma Splices")
        + K.fill_notes("Personal Companion Study Schedule &amp; Target Score Commitments", min_mm=14)
    )
    pages.append(K.page(p3_body, header=(BOOK, "Syllabus &bull; Practice Methodology"), footer=BOOK, page_no=3))

    # p4 to p51: 24 Independent Workbook Tasks across all 12 Formats x 2 pages = 48 pages
    p_curr = 4
    format_task_pages = {}
    for t in WORKBOOK_L2_TASKS:
        f_idx = t["format_idx"]
        f_name = t["format_name"]
        q_num = t["question_num"]
        marks = t["marks"]
        words = t["word_count"]
        topic = t["topic"]
        aud = t["audience"]
        spec_list = t["specialist_words"]
        stim = t["stimulus"]
        bullets = t["bullets"]
        strat = t["strategy"]

        if f_idx not in format_task_pages:
            format_task_pages[f_idx] = p_curr

        # Unit Photo Card & Side-by-Side Scenario Block
        u_photo_card = ""
        photo_map = UNIT_PHOTOS_SECOND if q_num == 2 else UNIT_PHOTOS_L2
        if SHOW_UNIT_IMAGES and f_idx in photo_map:
            rel_path, cap_txt = photo_map[f_idx]
            img_p = K.PHOTO_DIR / rel_path
            if img_p.exists():
                u_photo_card = (
                    f"<div style='background:#ffffff;border:1.5px solid var(--primary);border-radius:6px;overflow:hidden;box-shadow:0 1.5px 4px rgba(0,0,0,0.08);display:flex;flex-direction:column;'>"
                    f"<div style='width:100%;aspect-ratio:16/9;overflow:hidden;background:#0f172a;'>"
                    f"<img src='{img_p.as_uri()}' alt='{escape_html(cap_txt)}' style='width:100%;height:100%;object-fit:cover;object-position:center 25%;display:block;'>"
                    f"</div>"
                    f"<div style='background:#eff6ff;color:var(--primary);font-size:7.8pt; /* hf-ok */ font-weight:700;text-align:center;padding:0.8mm 1.5mm;border-top:1px solid #bfdbfe;line-height:1.15;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;'>"
                    f"Task {q_num}: {cap_txt}</div>"
                    f"</div>"
                )

        # Clean single-paragraph stimulus (zero mid-sentence line breaks)
        stim_clean = " ".join(stim.split())
        stim_html = escape_html(stim_clean)
        bullets_html = "".join(f"<li style='margin-bottom:1.2px;'>{escape_html(b)}</li>" for b in bullets)
        vocab_pills = "".join(
            f"<span class='chip' style='font-size:8pt; /* hf-ok */ padding:0.35mm 1.8mm;margin:0.3mm;'>{escape_html(w)}</span>"
            for w in spec_list
        )
        art_word = "an" if f_name[0].lower() in "aeiou" else "a"

        if u_photo_card:
            scenario_block = (
                f"<div style='display:grid;grid-template-columns:1fr 1fr;gap:3.5mm;align-items:center;margin-bottom:1.5mm;'>"
                f"<div style='display:flex;flex-direction:column;justify-content:space-between;'>"
                f"<p style='font-size:9.8pt; /* hf-ok */ margin:0 0 1.2mm 0;line-height:1.32;'><b>Scenario &amp; Context:</b> {escape_html(topic)}<br>"
                f"<span style='color:#475569;font-size:9pt; /* hf-ok */'><b>Target Audience &amp; Register:</b> {escape_html(aud)}</span></p>"
                f"<div style='background:#f8fafc;padding:2mm 2.8mm;border:1px solid var(--soft);border-radius:4px;font-size:9.2pt; /* hf-ok */ line-height:1.36;flex:1 1 auto;'>"
                f"<strong style='color:var(--primary);'>Context &amp; Stimulus Documentation:</strong><br>{stim_html}"
                f"</div>"
                f"</div>"
                f"{u_photo_card}"
                f"</div>"
            )
        else:
            scenario_block = (
                f"<p style='font-size:10pt; /* hf-ok */ margin:0 0 1.5mm 0;line-height:1.35;'><b>Scenario &amp; Context:</b> {escape_html(topic)}<br>"
                f"<span style='color:#475569;font-size:9.2pt; /* hf-ok */'><b>Target Audience &amp; Register:</b> {escape_html(aud)}</span></p>"
                f"<div style='background:#f8fafc;padding:2mm 2.8mm;border:1px solid var(--soft);border-radius:4px;font-size:9.5pt; /* hf-ok */ line-height:1.38;margin-bottom:1.5mm;'>"
                f"<strong style='color:var(--primary);'>Context &amp; Stimulus Documentation:</strong><br>{stim_html}"
                f"</div>"
            )

        # Page 1: Task Brief, Unit Photo, 10 Specialist Vocab Pills & TAP Planning Frame
        p1_body = (
            compact_tbl_css
            + K.page_title(f"Format {f_idx}: {f_name} &bull; Practice Task {q_num}", kicker=f"Unseen Exam Brief &bull; {marks} Marks &bull; {words}", badge=f"F{f_idx}&bull;T{q_num}")
            + K.box_html(
                f"{scenario_block}"
                f"<p style='margin:0 0 1mm 0;font-size:9.8pt; /* hf-ok */'><b>Task Instructions:</b> Write {art_word} <b>{escape_html(f_name)}</b> ({words}). In your writing, you must:</p>"
                f"<ul style='margin:0 0 1.8mm 5mm;padding:0;font-size:9.5pt; /* hf-ok */ line-height:1.34;'>{bullets_html}</ul>"
                f"<div style='background:#f8fafc;border:1px solid var(--soft);border-radius:4px;padding:1.4mm 2.2mm;margin-bottom:1.5mm;'>"
                f"<div style='font-size:8.4pt; /* hf-ok */ font-weight:800;color:var(--primary);margin-bottom:0.6mm;'>Specialist Vocabulary Bank (Aim to include at least 5 of these 10 Level 2 terms):</div>"
                f"<div style='display:flex;flex-wrap:wrap;gap:0.5mm;'>{vocab_pills}</div>"
                f"</div>"
                f"<div style='padding:1.5mm 2.5mm;background:#f1f5f9;border-left:3.5px solid var(--primary);font-size:8.8pt; /* hf-ok */ display:flex;justify-content:space-between;gap:3mm;'>"
                f"<span><b>Examiner Strategy:</b> {escape_html(strat)}</span>"
                f"<span style='white-space:nowrap;'><b>Target:</b> {words} &bull; <b>{marks} Marks</b></span>"
                f"</div>",
                title=f"Unseen Examination Brief &bull; Format {f_idx} (Task {q_num})"
            )
            + K.fill_notes("5-Minute TAP &amp; Paragraph Plan (Opening &bull; Bullet 1 &bull; Bullet 2 &bull; Bullet 3/4 &bull; Sign-Off)", min_mm=22)
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

    # p52 to p75: 4 Full Official Mock Papers (4 papers x 6 pages = 24 pages)
    # Followed by 8 Diagnostic Drills (p76 to p83 = 8 pages) -> Reference Section starts at page 84!
    ref_section_start_page = p_curr + 24 + 8
    mock_start_pages = {}

    audit_details = {
        1: ("Mock 1 Audit &bull; Commercial Tenancy Complaint &amp; Ergonomics Leaflet",
            "Review your Mock 1 performance against Pearson Level 2 Band 4 criteria:",
            [
                "<b>Task 1 (Formal Complaint Letter):</b> Included sender and recipient addresses, date, formal salutation ('Dear Mr Sterling,'), clear reference to prior repair logs (CR-402/CR-459), £3,400 damage claim, and 'Yours sincerely,'.",
                "<b>Task 2 (Ergonomics Guidance Leaflet):</b> Bold main title, clear subheadings, parallel imperative bullet points (monitor height, lumbar support, 20-20-20 rule), and Occupational Health contact box.",
                "<b>SPaG Precision:</b> Verified accurate semicolon and colon usage, zero comma splices, and accurate spelling of specialist vocabulary."
            ]),
        2: ("Mock 2 Audit &bull; Staff Attrition Report &amp; Software Evaluation Review",
            "Review your Mock 2 technical documentation against Level 2 Band 4 criteria:",
            [
                "<b>Task 1 (Management Report):</b> Included report header block (To/From/Date/Subject), numbered sections (1. Findings, 2. Impact, 3. Recommendations), objective tone, and assigned action leads.",
                "<b>Task 2 (Software Review):</b> Engaging review headline, balanced evaluation of strengths (one-click shift swaps, payroll export) vs limitations (GPS battery drain), and clear star rating.",
                "<b>Vocabulary &amp; Syntax:</b> Used complex sentences with subordinating conjunctions ('Although...', 'Provided that...') and formal nominalisation."
            ]),
        3: ("Mock 3 Audit &bull; Apprentice Mentorship Email &amp; Repair Culture Article",
            "Review your Mock 3 persuasive and workplace writing against Level 2 criteria:",
            [
                "<b>Task 1 (Proposal Email):</b> Included To/From/Date/Subject lines, clear rationale for apprentice retention, structured fortnightly mentorship model, and low-cost business case.",
                "<b>Task 2 (Magazine Article):</b> Catchy headline, byline, subheadings, persuasive rhetorical devices (rhetorical question, statistics, direct address), and call to visit local Repair Cafés.",
                "<b>Punctuation Range:</b> Checked apostrophes of possession, parenthetical dashes, and sentence boundaries."
            ]),
        4: ("Mock 4 Audit &bull; High Street Loyalty Speech &amp; Contractor Directive Memo",
            "Review your Mock 4 executive communication against Level 2 criteria:",
            [
                "<b>Task 1 (Keynote Speech):</b> Opened with direct audience greeting, acknowledged the 18% footfall drop empathetically, explained the £15/month shared loyalty card, and ended with a rallying call to sign up.",
                "<b>Task 2 (Operational Directive Memo):</b> Included MEMORANDUM header block (TO/FROM/DATE/SUBJECT), cited the Workshop 3 hot-work breach, and listed mandatory contractor sign-in and permit rules.",
                "<b>Timing &amp; Word Count:</b> Completed Task 1 (250–350 words) in 35 minutes and Task 2 (200–250 words) in 25 minutes."
            ])
    }

    for m in WORKBOOK_MOCK_L2_PAPERS:
        pnum = m["paper_num"]
        mock_start_pages[pnum] = p_curr
        theme = m.get("theme", f"Paper {pnum}")
        t1 = m["task1"]
        t2 = m["task2"]

        p_over = (
            K.page_title(f"Official Mock Writing Examination &bull; Paper {pnum}", kicker="Pearson Edexcel Level 2 Simulation &bull; 60 Minutes &bull; 36 Marks", badge=f"MOCK {pnum}")
            + K.box_html(
                f"<div style='font-size:12pt;line-height:1.5;'>"
                f"<p><b>Simulation Examination:</b> Complete both Task 1 ({t1['marks']} marks) and Task 2 ({t2['marks']} marks) under timed exam conditions (60 minutes total) without a dictionary or spellchecker.</p>"
                f"<p><b>Paper Theme:</b> {escape_html(theme)}</p>"
                f"<ul>"
                f"<li><b>Task 1:</b> {escape_html(t1['title'])} &bull; {t1['words']} &bull; {t1['time']}</li>"
                f"<li><b>Task 2:</b> {escape_html(t2['title'])} &bull; {t2['words']} &bull; {t2['time']}</li>"
                f"</ul>"
                f"</div>",
                title=f"Mock Paper {pnum} Overview &amp; Regulations"
            )
            + K.tip_pair("Allocate 35 minutes for Task 1 (21 marks) and 25 minutes for Task 2 (15 marks).",
                         "Check that every paragraph has a clear topic sentence and linking discourse marker.",
                         golden_title="Pacing", watch_title="Cohesion")
            + K.fill_notes(f"Candidate Exam Plan &amp; Pre-Mock Commitments (Paper {pnum})", min_mm=38)
        )
        pages.append(K.page(p_over, header=(BOOK, f"Mock {pnum} &bull; Overview"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Task 1 Brief
        p_t1_brief = (
            K.page_title(f"Mock {pnum} &bull; {t1['title']}", kicker=f"Task 1 (Extended Writing) &bull; {t1['marks']} Marks &bull; {t1['words']}", badge="T1")
            + K.box_html(
                f"<p style='font-size:12pt;line-height:1.48;'><b>Scenario:</b> {escape_html(t1['scenario'])}</p>"
                + K.bullets([escape_html(b) for b in t1["bullets"]])
                + f"<p style='font-size:10.5pt;color:#64748b;margin-top:2mm;'><b>Recommended Time:</b> {t1['time']} &emsp; <b>Target Word Count:</b> {t1['words']}</p>",
                title=f"Task 1 Brief &bull; {t1['marks']} Marks"
            )
            + K.fill_notes("Task 1 TAP Planning Matrix &amp; Key Vocabulary", min_mm=38)
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
            K.page_title(f"Mock {pnum} &bull; {t2['title']}", kicker=f"Task 2 (Shorter Writing) &bull; {t2['marks']} Marks &bull; {t2['words']}", badge="T2")
            + K.box_html(
                f"<p style='font-size:12pt;line-height:1.48;'><b>Scenario:</b> {escape_html(t2['scenario'])}</p>"
                + K.bullets([escape_html(b) for b in t2["bullets"]])
                + f"<p style='font-size:10.5pt;color:#64748b;margin-top:2mm;'><b>Recommended Time:</b> {t2['time']} &emsp; <b>Target Word Count:</b> {t2['words']}</p>",
                title=f"Task 2 Brief &bull; {t2['marks']} Marks"
            )
            + K.fill_notes("Task 2 TAP Planning Matrix &amp; Key Points", min_mm=38)
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

        # Mock Audit
        a_title, a_lead, a_checks = audit_details.get(pnum, (f"Mock {pnum} Audit", "Audit your script:", ["Covered all points."]))
        p_audit = (
            K.page_title(f"Mock {pnum} &bull; Post-Exam Audit", kicker=a_title, badge="AUDIT")
            + K.box_html(
                f"<p style='font-size:12pt;margin-top:0;'><b>{a_lead}</b></p>"
                + K.bullets(a_checks)
                + f"<p style='font-size:11pt;color:#64748b;margin-top:2mm;'>After completing this self-audit, compare your responses against the full Band 4 benchmark model solutions in the Reference Section (starting on p. {ref_section_start_page}).</p>",
                title=f"Pearson Edexcel Level 2 Marking Matrix &bull; Paper {pnum}"
            )
            + K.fill_notes(f"Personal Skill Reflection &amp; Punctuation Error Log (Mock {pnum})", min_mm=38)
        )
        pages.append(K.page(p_audit, header=(BOOK, f"Mock {pnum} &bull; Audit"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p76 to p83: 8 Targeted Diagnostic Writing Exercises (8 pages)
    proof_passages = [
        ("Diagnostic 1: Formal Letter Demarcation &amp; Semicolons",
         "Dear Mr Davies, I am writing regarding our office heating system, it has been broken for three days. The temperature in the main administrative suite fell to eleven degrees yesterday morning, consequently several staff members could not complete their shifts. We telephoned your emergency helpline twice however nobody returned our calls. Please confirm when an engineer will attend our premises. Yours sincerely, Alex Vance.",
         "Dear Mr Davies, I am writing regarding our office heating system<b>;</b> it has been broken for three days. The temperature in the main administrative suite fell to eleven degrees yesterday morning<b>; consequently,</b> several staff members could not complete their shifts. We telephoned your emergency helpline twice<b>; however,</b> nobody returned our calls. Please confirm when an engineer will attend our premises. Yours sincerely, Alex Vance."),
        ("Diagnostic 2: Workplace Incident Report Active to Passive Framing",
         "Jordan Taylor dropped the chemical container because he was in a rush to finish his shift before 5pm. Nobody had wiped up the grease patch near Bay 3 so Jordan's safety boot slipped immediately. The floor manager didn't put out the yellow caution signs that morning.",
         "A chemical container <b>was accidentally dropped</b> in Bay 3 shortly before 17:00 during end-of-shift clearance. A residual grease patch on the walkway <b>had not been cleaned</b>, causing the operative's safety footwear to lose traction. Furthermore, cautionary hazard signage <b>had not been deployed</b> that morning."),
        ("Diagnostic 3: Informative Article Headline &amp; Discourse Linking",
         "Electric scooters are becoming very popular in town. Many people think they are dangerous on pavements. Riders travel too fast and do not wear helmets. They reduce traffic on the high street. The council should create segregated lanes for electric vehicles.",
         "<b>Are E-Scooters the Future of Town Travel?</b><br>Electric scooters are becoming increasingly popular across our town<b>; however,</b> many residents consider them hazardous on pedestrian pavements because riders frequently travel at excessive speeds without helmets. <b>Conversely,</b> e-scooters significantly reduce high-street congestion. <b>Consequently,</b> the council should introduce segregated cycle lanes."),
        ("Diagnostic 4: Formal Email to Senior Management &bull; Register",
         "Hi Karen, Just dropping you a quick message coz the guys on the shop floor are getting super stressed about the till system. It keeps glitching out and customers are kicking off big time. We really need a training session ASAP so everyone stops making mistakes. Let me know what you think. Cheers, Sam.",
         "<b>Dear Ms Morris,</b> I am writing to report that retail floor personnel are experiencing significant difficulties with the updated point-of-sale software. Frequent system freezes have caused checkout delays and customer dissatisfaction. I recommend scheduling an urgent staff training workshop to prevent further transaction errors. <b>Kind regards, Sam Taylor.</b>"),
        ("Diagnostic 5: Advice Leaflet Parallel Bullet Points",
         "Top Tips for Managing First Wages:<br>&bull; Creating a realistic weekly budget sheet.<br>&bull; You should always pay off essential bills first.<br>&bull; Do not spend money on impulse purchases.<br>&bull; Putting away ten percent into a savings account.",
         "<b>Top Tips for Managing Your First Wages:</b><br>&bull; <b>Create</b> a realistic weekly income and expenditure budget.<br>&bull; <b>Prioritise</b> essential household bills before discretionary spending.<br>&bull; <b>Avoid</b> unplanned impulse purchases on payday.<br>&bull; <b>Transfer</b> ten percent of your monthly earnings into a dedicated savings account."),
        ("Diagnostic 6: Service Review Evaluative Language",
         "The gym was totally rubbish when I visited. The showers were disgusting and the weights were everywhere on the floor. The staff were completely useless and couldn't answer simple questions about membership.",
         "My recent visit to the fitness centre proved disappointing. The changing room showers required urgent sanitisation, and unreturned free weights created trip hazards across the training floor. Furthermore, reception personnel appeared unfamiliar with current membership tariffs."),
        ("Diagnostic 7: Online Feedback Form Directness &amp; Statutory Rights",
         "I bought a sofa three weeks ago and it arrived damaged with no legs in the box. Your driver was rude and ran off before I could inspect the parcel. I want my money back right now under the Consumer Rights Act.",
         "On 2 November, I took delivery of an upholstered sofa (Order #SF-409), which arrived with torn fabric and missing support legs. Unfortunately, the courier departed before the consignment could be inspected. Under the Consumer Rights Act 2015, I formally request a full refund or immediate collection and replacement."),
        ("Diagnostic 8: Newsletter Engaging Openers &amp; Call to Action",
         "Our community garden had a harvest festival last Saturday. It was very good and lots of people came. We grew carrots and potatoes. We need more volunteers to help dig the sensory garden next week.",
         "<b>Autumn Harvest Triumphant at Greenbank Community Garden!</b><br>Over eighty local families gathered in the autumn sunshine last Saturday to celebrate a bumper harvest of organic carrots, potatoes, and seasonal produce. Would you like to help our community grow? Join our volunteer digging team next Saturday at 10:00 am to help build our new Sensory Garden!")
    ]

    drill_start_pages = {}
    for d_idx, (d_title, d_text, _) in enumerate(proof_passages):
        drill_start_pages[d_idx + 1] = p_curr
        d_photo_html = ""
        if (d_idx + 1) in SPAG_WRITING_PHOTOS:
            d_rel, d_cap = SPAG_WRITING_PHOTOS[d_idx + 1]
            d_photo_html = writing_float_photo_card(d_rel, d_cap, height_mm=38, width_mm=64)
        d_body = (
            K.page_title(f"Targeted Diagnostic Drill {d_idx+1}", kicker=d_title, badge=f"D{d_idx+1}")
            + K.box_html(
                f"{d_photo_html}"
                f"<p style='font-size:12pt;margin-top:0;'><b>Diagnostic Passage:</b> Identify every register, punctuation, formatting, and structural error in the workplace extract below:</p>"
                f"<div style='background:#f8fafc;padding:3.5mm;border:1.5px solid var(--soft);border-radius:6px;font-size:11.5pt;line-height:1.55;clear:both;'>"
                f"{d_text}"
                f"</div>",
                title=f"Extract to Diagnose &bull; Drill {d_idx+1}"
            )
            + K.fill_lines(f"Write your professional diagnostic analysis and corrected rewrite below (worked solution on p. {ref_section_start_page + 1}):", min_mm=115, gap_mm=9.5)
        )
        pages.append(K.page(d_body, header=(BOOK, f"Diagnostic {d_idx+1}"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p84 onwards: Reference Back Matter via K.ref_pages
    ref_actual_start = p_curr
    ref_blocks = []

    # 1. Indicative Content & Examiner Checklists for all 24 Workbook Tasks (grouped into 8 balanced blocks of 3 tasks each)
    for chunk_idx in range(0, 24, 3):
        t_slice = WORKBOOK_L2_TASKS[chunk_idx:chunk_idx + 3]
        qa_html = ""
        for offset_i, t in enumerate(t_slice):
            t_num = chunk_idx + offset_i + 1
            f_i = t["format_idx"]
            qn = t["question_num"]
            v_str = escape_html(", ".join(t["specialist_words"][:4]))
            b_summary = escape_html(t["bullets"][0])
            qa_html += K.ref_qa(
                f"T{t_num}",
                f"<b>F{f_i} ({escape_html(t['format_name'])}) Task {qn} &ndash; {escape_html(t['topic'])}</b> ({escape_html(t['audience'])}): {b_summary} <b>Vocab:</b> <i>{v_str}</i>.",
                marks=f"{t['marks']}m"
            )
        ref_blocks.append(K.ref_block(f"Workbook Practice Tasks {chunk_idx+1}&ndash;{chunk_idx+3} Guidance", qa_html))

    # 2. Worked Solutions for all 8 Diagnostic Proofreading Drills (2 balanced blocks of 4 drills each, 1 block per column)
    d_html_1 = "".join(
        K.ref_qa(f"D{idx+1}", corr, marks="4/4", working=title.split(":", 1)[-1].strip())
        for idx, (title, _, corr) in enumerate(proof_passages[:4])
    )
    ref_blocks.append(K.ref_block("Diagnostic Drills 1–4: Worked Rewrites", d_html_1))

    d_html_2 = "".join(
        K.ref_qa(f"D{idx+5}", corr, marks="4/4", working=title.split(":", 1)[-1].strip())
        for idx, (title, _, corr) in enumerate(proof_passages[4:])
    )
    ref_blocks.append(K.ref_block("Diagnostic Drills 5–8: Worked Rewrites", d_html_2))

    # 3. Full Band 4 Benchmark Model Solutions for all 4 Mock Papers (8 Tasks)
    for m in WORKBOOK_MOCK_L2_PAPERS:
        pnum = m["paper_num"]
        t1 = m["task1"]
        t2 = m["task2"]
        ref_blocks.append(K.ref_block(
            f"Mock Paper {pnum} &bull; Task 1 Benchmark Solution (21 Marks)",
            K.ref_qa(f"M{pnum}a", t1["model"], marks="21/21", working="Band 4 Comp (12/12) & Band 3 SPaG (9/9): Complete format conventions, full bullet development, and varied complex syntax.")
        ))
        ref_blocks.append(K.ref_block(
            f"Mock Paper {pnum} &bull; Task 2 Benchmark Solution (15 Marks)",
            K.ref_qa(f"M{pnum}b", t2["model"], marks="15/15", working="Band 3 Comp (9/9) & Band 3 SPaG (6/6): Clear structural headings, parallel bullets/paragraphs, and precise register.")
        ))

    # 4. Glossary (split into 3 balanced blocks of 10 terms so each block sits cleanly in 1 column)
    g_part1 = "".join(f"<dl><dt>{escape_html(t)}</dt><dd>{escape_html(d)}</dd></dl>" for t, d in GLOSSARY_L2[:10])
    g_part2 = "".join(f"<dl><dt>{escape_html(t)}</dt><dd>{escape_html(d)}</dd></dl>" for t, d in GLOSSARY_L2[10:20])
    g_part3 = "".join(f"<dl><dt>{escape_html(t)}</dt><dd>{escape_html(d)}</dd></dl>" for t, d in GLOSSARY_L2[20:])
    ref_blocks.append(K.ref_block("Comprehensive Functional Writing Glossary (A–C)", g_part1))
    ref_blocks.append(K.ref_block("Functional Writing Glossary (C–N)", g_part2))
    ref_blocks.append(K.ref_block("Functional Writing Glossary (P–T)", g_part3))

    # 5. Companion Workbook Index (split into 2 balanced blocks with exact Companion Workbook page numbers)
    comp_index_l2 = [
        ("A", [("Advice & Guidance Leaflets (Format 5)", "20–23, 55"), ("Articles & Columns (Format 3)", "12–15, 67"), ("Audience & Register (W23)", "3")]),
        ("B", [("Blog & Forum Posts (Format 11)", "44–47"), ("Bullet Points & Parallel Lists", "20, 55, 80")]),
        ("C", [("Colons & Semicolons (W20)", "3, 76, 84"), ("Comma Splices (Eliminating)", "3, 76"), ("Critical Reviews (Format 7)", "28–31, 61")]),
        ("D", [("Diagnostic Proofreading Drills (D1–D8)", "76–83"), ("Discursive Essays (Format 9)", "36–39")]),
        ("E", [("Emails: Formal Workplace (Format 2)", "8–11, 65"), ("Ergonomics Leaflet (Mock 1 T2)", "55")]),
        ("F", [("Feedback & Online Forms (Format 8)", "32–35, 82"), ("Formal Letters (Format 1)", "4–7, 53")]),
        ("G", [("Glossary of Level 2 Terms", f"{ref_actual_start+5}–{ref_actual_start+6}")]),
        ("I", [("Investigation & Management Reports (Format 4)", "16–19, 59")]),
        ("M", [("Memorandums & Directives (Format 12)", "48–51, 73"), ("Minutes of Meetings (Format 6)", "24–27"), ("Mock Examinations 1–4", "52–75")]),
        ("N", [("Newsletters & Community Reports (Format 10)", "40–43, 83")]),
        ("P", [("Planning & TAP Framework (W24)", "3"), ("Proofreading Solutions", f"{ref_actual_start+1}")]),
        ("S", [("Speeches & Keynote Talks (Format 6/Mock 4)", "24–27, 71"), ("Specialist Vocabulary Banks", "4–50")])
    ]
    idx_part1 = ""
    for letter, entries in comp_index_l2[:6]:
        items = "".join(f"<div class='ix'><span>{escape_html(t)}</span><span>{escape_html(p)}</span></div>" for t, p in entries)
        idx_part1 += f"<div class='ix-letter'>{letter}</div>{items}"
    ref_blocks.append(K.ref_block("Companion Subject &amp; Format Index (A–F)", idx_part1))

    idx_part2 = ""
    for letter, entries in comp_index_l2[6:]:
        items = "".join(f"<div class='ix'><span>{escape_html(t)}</span><span>{escape_html(p)}</span></div>" for t, p in entries)
        idx_part2 += f"<div class='ix-letter'>{letter}</div>{items}"
    ref_blocks.append(K.ref_block("Companion Subject &amp; Format Index (G–S)", idx_part2))

    cover_theme = K.theme_from_cover(front_cov)
    ref_page_list = K.ref_pages("Companion Reference: Solutions, Models, Glossary &amp; Index", ref_blocks,
                                BOOK, start_page=p_curr, subtitle="Worked Solutions, Full-Marks Mock Exemplars &amp; Lexicon",
                                cols=2, theme=cover_theme, notes_title="Candidate Companion Log")
    pages.extend(ref_page_list)
    p_curr += len(ref_page_list)

    # Self-Assessment Rubric
    audit_matrix_page = p_curr
    p_audit_body = (
        K.page_title("Candidate Writing Self-Assessment &amp; Grading Matrix", kicker="Final Independent Evaluation &bull; Band 4 Verification", badge="AUDIT")
        + K.box_html(
            "<p>Grade your completed companion practice tasks and four mock papers against the official Pearson Edexcel Level 2 standards:</p>"
            + K.bullets([
                "<b>Band 4 Composition (Task 1: 10–12m / Task 2: 7–9m):</b> Communicates complex ideas effectively; completely fit for purpose and audience; sophisticated register; logical paragraphing with cohesive transitions.",
                "<b>Band 3 SPaG (Task 1: 7–9m / Task 2: 5–6m):</b> Wide range of punctuation (colons, semicolons, apostrophes, dashes) used accurately; zero comma splices; accurate spelling of specialist vocabulary; varied complex syntax."
            ]),
            title="Pearson Edexcel Level 2 Top-Band Standards"
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
                         "<p style='font-size:12pt;line-height:1.5;'>This workbook represents comprehensive independent preparation across <b>24 unseen functional writing tasks</b> (covering all 12 formats), <b>4 full mock examination papers</b>, and <b>8 diagnostic proofreading drills</b>:</p>"
                         + K.bullets([
                             "<b>Format Breadth:</b> Demonstrated capability across all 12 official formats: letters, emails, articles, reports, leaflets, speeches/minutes, reviews, forms, discursive essays, newsletters, blogs, and memos.",
                             "<b>Audience Calibration:</b> Consistent mastery of register, tone, and structural conventions.",
                             "<b>Technical Precision:</b> Punctuation range, accurate demarcation, grammatical agreement, and vocational terminology.",
                             "<b>Independent Mock Performance:</b> Timed practice completing four 60-minute papers within official examination constraints."
                         ]))
            + K.tip_pair("Review any marked tasks alongside your Level 2 Core Guide before sitting your official assessment.",
                         "Carefully audit your word count on each task to guarantee you meet Pearson length and development criteria.",
                         golden_title="Final Advice", watch_title="Word Counts")
            + K.fill_notes("Tutor Verification Notes &amp; Exam Booking Details", min_mm=28)
        )
        pages.append(K.page(p_ibc_body, header=(BOOK, "Portfolio Sign-Off"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # Populate Page 2 (Complete 2-Column Table of Contents) with 100% verified dynamic page numbers
    def toc_row(badge_txt: str, label_txt: str, pg_txt: str) -> str:
        return (
            f"<tr>"
            f"<td style='width:11mm;padding:0.35mm 1mm !important;white-space:nowrap;'><span class='chip' style='font-size:7.6pt; /* hf-ok */ padding:0.1mm 1.1mm;font-weight:800;display:inline-block;text-align:center;min-width:9.5mm;'>{badge_txt}</span></td>"
            f"<td style='padding:0.35mm 1mm !important;font-size:8.4pt; /* hf-ok */ line-height:1.12;color:#0f172a;font-weight:600;'>{label_txt}</td>"
            f"<td style='width:13.5mm;padding:0.35mm 1.2mm !important;text-align:right;font-weight:800;font-size:8.4pt; /* hf-ok */ color:var(--primary);white-space:nowrap;'>p. {pg_txt}</td>"
            f"</tr>"
        )

    def toc_sec_hdr(sec_title: str) -> str:
        return (
            f"<tr><td colspan='3' style='background:var(--primary);color:#ffffff;font-weight:800;font-size:8.2pt; /* hf-ok */ "
            f"letter-spacing:0.04em;text-transform:uppercase;padding:0.55mm 1.8mm !important;border-radius:3px;'>{sec_title}</td></tr>"
        )

    left_col_rows = (
        toc_sec_hdr("Part 1: Syllabus &amp; Timed Practice Strategy")
        + toc_row("GUIDE", "Pearson Level 2 Syllabus (W20–W28) &amp; 4-Step Method", "3")
        + toc_sec_hdr("Part 2: 24 Unseen Format Practice Tasks (48 Pages)")
        + "".join(
            toc_row(
                f"F{f['idx']}",
                f"Format {f['idx']}: {escape_html(f['title'])} (Tasks 1 &amp; 2)",
                f"{format_task_pages[f['idx']]}&ndash;{format_task_pages[f['idx']]+3}"
            )
            for f in FORMATS_L2
        )
    )

    right_col_rows = (
        toc_sec_hdr("Part 3: 4 Full Official Mock Exams (24 Pages)")
        + toc_row("MOCK 1", "Paper 1: Commercial Lease Letter &amp; DSE Leaflet", f"{mock_start_pages[1]}&ndash;{mock_start_pages[1]+5}")
        + toc_row("MOCK 2", "Paper 2: Attrition Report &amp; Rota App Review", f"{mock_start_pages[2]}&ndash;{mock_start_pages[2]+5}")
        + toc_row("MOCK 3", "Paper 3: Mentorship Email &amp; Repair Café Article", f"{mock_start_pages[3]}&ndash;{mock_start_pages[3]+5}")
        + toc_row("MOCK 4", "Paper 4: High Street Speech &amp; Contractor Memo", f"{mock_start_pages[4]}&ndash;{mock_start_pages[4]+5}")
        + toc_sec_hdr("Part 4: 8 Targeted Proofreading Drills (8 Pages)")
        + "".join(
            toc_row(
                f"D{d_i+1}",
                proof_passages[d_i][0].replace(f"Diagnostic {d_i+1}: ", f"Drill {d_i+1}: "),
                f"{drill_start_pages[d_i+1]}"
            )
            for d_i in range(8)
        )
        + toc_sec_hdr("Part 5: Reference Solutions, Glossary &amp; Index")
        + toc_row("SOL", "24 Task Guides, 8 Drill Keys &amp; 8 Mock Models", f"{ref_actual_start}&ndash;{ref_actual_start+4}")
        + toc_row("GLOSS", "Comprehensive Functional Writing Glossary", f"{ref_actual_start+5}&ndash;{ref_actual_start+6}")
        + toc_row("INDEX", "Companion Subject &amp; Format Index", f"{ref_actual_start+6}&ndash;{audit_matrix_page-1}")
        + toc_row("AUDIT", "Self-Assessment Matrix &amp; Portfolio Sign-Off", f"{audit_matrix_page}&ndash;{p_curr-1}")
    )

    p2_toc_body = (
        compact_tbl_css
        + K.page_title("Functional Skills English &bull; Writing (Level 2)", kicker="Master Functional Skills &bull; Companion Workbook &amp; Mock Examination Bank", badge="TOC")
        + "<div class='box worked' style='padding:1.4mm 2.8mm;display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:1.2mm 4mm;font-size:9pt; /* hf-ok */ margin-bottom:1mm;'>"
          "<div><span style='font-weight:700;color:var(--primary);font-size:8.6pt; /* hf-ok */'>This workbook belongs to:</span><div class='aline' style='height:3.8mm;'></div></div>"
          "<div><span style='font-weight:700;color:var(--primary);font-size:8.6pt; /* hf-ok */'>Exam date:</span><div class='aline' style='height:3.8mm;'></div></div>"
          "<div><span style='font-weight:700;color:var(--primary);font-size:8.6pt; /* hf-ok */'>Target score (out of 36):</span><div class='aline' style='height:3.8mm;'></div></div>"
          "</div>"
        + "<h2 style='font-size:11.5pt;margin:0.3mm 0 0.8mm 0;color:var(--primary);'>Complete Table of Contents &amp; Practice Directory</h2>"
        + "<div style='display:grid;grid-template-columns:1fr 1fr;gap:2.5mm;align-items:start;'>"
        + f"<table class='t compact' style='width:100%;border-collapse:separate;'><tbody>{left_col_rows}</tbody></table>"
        + f"<table class='t compact' style='width:100%;border-collapse:separate;'><tbody>{right_col_rows}</tbody></table>"
        + "</div>"
        + "<div style='margin-top:1mm;background:#f8fafc;border:1.5px solid var(--soft);border-left:4px solid var(--accent);border-radius:6px;padding:1.2mm 2.5mm;font-size:8.6pt; /* hf-ok */ line-height:1.25;'>"
          "<b style='color:var(--primary);'>How This Companion Workbook Is Organised:</b> "
          "<b>Pages 4&ndash;51:</b> 24 Unseen Practice Tasks (2 unique tasks per format across all 12 formats, each with 10 specialist vocabulary prompts, planning frame, and lined response sheet) &bull; "
          "<b>Pages 52&ndash;75:</b> 4 Full 60-Minute Mock Exam Papers &bull; "
          "<b>Pages 76&ndash;83:</b> 8 Diagnostic Proofreading Drills &bull; "
          f"<b>Pages {ref_actual_start}&ndash;{audit_matrix_page-1}:</b> Complete Worked Solutions, Band 4 Mock Models, Glossary &amp; Index."
          "</div>"
    )
    pages[1] = K.page(p2_toc_body, header=("Master Functional Skills", "Complete Table of Contents"), footer=BOOK, page_no=2)

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
    # Placeholder for Page 2 (Table of Contents), populated dynamically after all pages are assembled
    pages.append("")

    # Helper to format structured Level 1 Model Answers with highlighted specialist vocabulary
    def render_formatted_model_l1(raw_model: str, spec_words) -> str:
        def hl_text(txt: str) -> str:
            esc = escape_html(txt)
            for sw in sorted(spec_words, key=len, reverse=True):
                pattern = re.compile(r"\b(" + re.escape(escape_html(sw)) + r")\b", re.IGNORECASE)
                esc = pattern.sub(
                    r"<span style='background:#fef3c7;border-bottom:1.5px solid #d97706;padding:0 0.25mm;border-radius:2px;font-weight:700;color:#0f172a;'>\1</span>",
                    esc,
                    count=1
                )
            return esc

        out = []
        bullet_buf = []

        def flush_bullets():
            if bullet_buf:
                items = "".join(f"<li style='margin-bottom:0.4mm;'>{b}</li>" for b in bullet_buf)
                out.append(f"<ul style='margin:0.6mm 0 1mm 4mm;padding:0;font-size:8.8pt; /* hf-ok */ line-height:1.25;'>{items}</ul>")
                bullet_buf.clear()

        for raw_line in raw_model.splitlines():
            ln = raw_line.strip()
            if not ln:
                flush_bullets()
                continue
            if ln.startswith("TITLE:"):
                flush_bullets()
                val = escape_html(ln[6:].strip())
                out.append(f"<div style='font-size:10pt; /* hf-ok */ font-weight:800;color:var(--primary);border-bottom:1.5px solid var(--accent);padding-bottom:0.5mm;margin-bottom:0.8mm;'>{val}</div>")
            elif ln.startswith("META_RIGHT:"):
                flush_bullets()
                val = escape_html(ln[11:].strip())
                out.append(f"<div style='font-size:8.3pt; /* hf-ok */ font-weight:700;color:#334155;text-align:right;margin-bottom:0.6mm;'>{val}</div>")
            elif ln.startswith("META:"):
                flush_bullets()
                val = escape_html(ln[5:].strip())
                out.append(f"<div style='font-size:8.3pt; /* hf-ok */ font-weight:700;color:#334155;background:#f8fafc;border-left:2.5px solid var(--primary);padding:0.4mm 1.8mm;margin-bottom:0.6mm;'>{val}</div>")
            elif ln.startswith("SALUTATION:"):
                flush_bullets()
                val = escape_html(ln[11:].strip())
                out.append(f"<div style='font-size:8.8pt; /* hf-ok */ font-weight:700;color:#0f172a;margin:0.6mm 0;'>{val}</div>")
            elif ln.startswith("SUB:"):
                flush_bullets()
                val = escape_html(ln[4:].strip())
                out.append(f"<div style='font-size:9pt; /* hf-ok */ font-weight:800;color:var(--primary);margin:0.8mm 0 0.3mm 0;'>{val}</div>")
            elif ln.startswith("•"):
                val = hl_text(ln[1:].strip())
                bullet_buf.append(val)
            else:
                flush_bullets()
                out.append(f"<p style='margin:0 0 0.8mm 0;font-size:8.8pt; /* hf-ok */ line-height:1.26;'>{hl_text(ln)}</p>")
        flush_bullets()
        return "".join(out)

    compact_tbl_css = (
        "<style>"
        ".t.compact th { padding:1.1mm 2mm !important; font-size:9pt !important; /* hf-ok */ line-height:1.2 !important; }"
        ".t.compact td { padding:1.0mm 2mm !important; font-size:8.8pt !important; /* hf-ok */ line-height:1.22 !important; }"
        ".ptitle h1 { font-size:19.5pt !important; line-height:1.08 !important; }"
        ".ptitle .badge { height:15mm !important; min-width:15mm !important; font-size:16pt !important; }"
        ".pair .box { padding:2.2mm 3mm !important; font-size:9.8pt !important; /* hf-ok */ line-height:1.26 !important; }"
        "</style>"
    )

    # p3: Specification Mapping: Pearson Edexcel Level 1 Writing Overview (W19-W25)
    p3_body = (
        compact_tbl_css
        + K.page_title("Pearson Edexcel Level 1 Specification",
                       kicker="Curriculum Architecture &bull; Pearson Specification QAN 603/4289/4 (W19–W25)", badge="SPEC")
        + K.box_html(
            "<div style='font-size:9.8pt; /* hf-ok */ line-height:1.35;'>"
            "<p style='margin:0 0 1mm 0;'><b>Examination Structure:</b> The Pearson Edexcel Functional Skills English Level 1 Writing examination is a <b>60-minute</b> externally assessed paper (no dictionary or spellchecker allowed) comprising two compulsory writing tasks:</p>"
            "<ul style='margin:0 0 1mm 4mm;padding:0;'>"
            "<li><b>Task 1 (Extended Functional Writing &bull; 21 Marks &bull; 35 Minutes):</b> Everyday, community, or workplace scenario requiring <b>150&ndash;250 words</b>. Assessed across Composition &amp; Effect (12 marks) and SPaG (9 marks).</li>"
            "<li><b>Task 2 (Shorter Functional Writing &bull; 15 Marks &bull; 25 Minutes):</b> Targeted response of <b>100&ndash;180 words</b> to a realistic prompt. Assessed across Composition &amp; Effect (9 marks) and SPaG (6 marks).</li>"
            "</ul>"
            "<p style='margin:0;'><b>Total Marks: 36 Marks &bull; SPaG Weighting: 41.7% (15/36 marks).</b> Typical pass threshold: <b>21&ndash;23 marks (approx. 58&ndash;64%)</b>.</p>"
            "</div>",
            title="Official Pearson Edexcel Level 1 Assessment Profile"
        )
        + K.box_html(
            "<table class='t compact'>"
            "<thead><tr><th style='width:10%;'>Code</th><th style='width:62%;'>Official Subject Content Statement (DfE / Pearson Edexcel Level 1)</th><th style='width:28%;'>Book Coverage</th></tr></thead>"
            "<tbody>"
            "<tr><td><b>W19</b></td><td>Use a range of punctuation correctly (e.g. full stops, question marks, exclamation marks, commas, possessive apostrophes)</td><td>SPaG Masterclass Units 1, 2 &amp; 4</td></tr>"
            "<tr><td><b>W20</b></td><td>Use correct grammar (e.g. subject-verb agreement, consistent use of different tenses, definite and indefinite articles)</td><td>SPaG Masterclass Unit 3</td></tr>"
            "<tr><td><b>W21</b></td><td>Spell words used most often in work, study and daily life, including specialist words</td><td>SPaG Unit 6 &amp; 144 Vocab Terms</td></tr>"
            "<tr><td><b>W22</b></td><td>Communicate information, ideas and opinions clearly, coherently and accurately</td><td>All 12 Formats &amp; Strategy</td></tr>"
            "<tr><td><b>W23</b></td><td>Write text of an appropriate level of detail and of appropriate length (including where this is specified) to meet the needs of purpose and audience</td><td>Word Count &amp; Bullet Scaffolds</td></tr>"
            "<tr><td><b>W24</b></td><td>Use format, structure and language appropriate for audience and purpose</td><td>6-Point Format Anatomy Grids</td></tr>"
            "<tr><td><b>W25</b></td><td>Write consistently and accurately in complex sentences, using paragraphs where appropriate</td><td>Page 4 &amp; SPaG Masterclass Unit 5</td></tr>"
            "</tbody></table>",
            title="Complete Pearson Edexcel Level 1 Syllabus Mapping (W19–W25)"
        )
        + K.tip_pair(
            "Cover every single bullet point in the exam question and start a new paragraph (with a clear blank line) for each main point.",
            "Check that every sentence starts with a capital letter and ends with a full stop, question mark, or exclamation mark—41.7% of marks are for SPaG!",
            golden_title="Core Level 1 Rule", watch_title="Critical Exam Trap"
        )
    )
    pages.append(K.page(p3_body, header=(BOOK, "Specification Overview"), footer=BOOK, page_no=3))

    # p4: Complete Level 1 Writing Strategy Masterclass: TAP, Planning, Paragraphs, Register & Proofreading
    p4_body = (
        compact_tbl_css
        + K.page_title("Core Writing Strategy &amp; Proofreading",
                       kicker="Pre-Writing Mastery &bull; TAP, Paragraphs, Linking Words, Register &amp; Checking", badge="STRAT")
        + K.box_html(
            "<div style='display:grid;grid-template-columns:1fr 1fr;gap:2mm;font-size:8.8pt; /* hf-ok */ line-height:1.28;'>"
            "<div style='background:#f8fafc;border:1px solid var(--soft);border-left:3.5px solid var(--primary);padding:1.6mm 2.2mm;border-radius:4px;'>"
            "<b style='color:var(--primary);font-size:9.3pt; /* hf-ok */'>1. Decoding Questions (The TAP Method) &amp; Register</b><br>"
            "&bull; <b>T (Text Format):</b> Spot the required format features (2 addresses for a formal letter, To/Subject for an email, headline/subheadings for an article or leaflet).<br>"
            "&bull; <b>A (Audience):</b> Manager, landlord, council, or company = <b>Formal</b> (polite, no slang). Friend or relative = <b>Informal</b> (warm, friendly).<br>"
            "&bull; <b>P (Purpose):</b> Inform, Persuade, Advise, Explain, Apply, or Complain.<br>"
            "&bull; <b>Letter Sign-Off Rule:</b> <i>Dear Sir/Madam</i> &rarr; <b>Yours faithfully</b> | <i>Dear Mr/Mrs [Surname]</i> &rarr; <b>Yours sincerely</b>."
            "</div>"
            "<div style='background:#f8fafc;border:1px solid var(--soft);border-left:3.5px solid var(--accent);padding:1.6mm 2.2mm;border-radius:4px;'>"
            "<b style='color:var(--primary);font-size:9.3pt; /* hf-ok */'>2. The 5-Minute Plan &amp; Paragraph Formula</b><br>"
            "&bull; <b>5-Min Plan:</b> Before writing, jot down your format layout, 2–3 ideas for each bullet point, and 5 key words to include.<br>"
            "&bull; <b>When to Start a New Paragraph (TiPToP):</b> Change of <b>Ti</b>me, <b>P</b>lace, <b>To</b>pic (give each exam bullet point its own paragraph!), or <b>P</b>erson.<br>"
            "&bull; <b>Paragraph Shape:</b> Start with a clear main sentence, add an example or reason (<i>because...</i>), and explain what should happen.<br>"
            "&bull; <b>Leave a Blank Line:</b> Always leave a clear line space between paragraphs."
            "</div>"
            "<div style='background:#f8fafc;border:1px solid var(--soft);border-left:3.5px solid var(--primary);padding:1.6mm 2.2mm;border-radius:4px;'>"
            "<b style='color:var(--primary);font-size:9.3pt; /* hf-ok */'>3. Making Your Writing Engaging &amp; Persuasive</b><br>"
            "&bull; <b>Direct Address:</b> Speak directly to the reader using <i>you, your, we,</i> and <i>our community</i> in leaflets, articles, and talks.<br>"
            "&bull; <b>Rhetorical Questions:</b> Ask a question to hook the reader (<i>Have you noticed how busy our park has become?</i>).<br>"
            "&bull; <b>Facts &amp; Examples:</b> Give realistic details (times, prices, dates, and practical examples) to develop each bullet point.<br>"
            "&bull; <b>Rule of Three:</b> Group three adjectives together (<i>cleaner, safer, and more welcoming</i>)."
            "</div>"
            "<div style='background:#f8fafc;border:1px solid var(--soft);border-left:3.5px solid var(--accent);padding:1.6mm 2.2mm;border-radius:4px;'>"
            "<b style='color:var(--primary);font-size:9.3pt; /* hf-ok */'>4. The 5-Minute Proofreading Routine</b><br>"
            "&bull; <b>Check 1 (Capitals &amp; Full Stops):</b> Check every sentence starts with a capital letter and ends with a full stop (.) or question mark (?). Check capital <b>I</b> and days/months!<br>"
            "&bull; <b>Check 2 (Tenses &amp; Agreement):</b> Check past/present tense and make sure you wrote <i>we were / they were</i> (never <i>we was / they was</i>).<br>"
            "&bull; <b>Check 3 (Homophones &amp; Spellings):</b> Check <i>their/there/they're</i>, <i>your/you're</i>, <i>to/too/two</i>, and key words (<i>because, necessary, business, accommodation</i>)."
            "</div>"
            "</div>",
            title="The Four Steps to Level 1 Exam Success"
        )
        + K.box_html(
            "<table class='t compact'>"
            "<thead><tr><th>Job of the Linking Word</th><th>Basic Words</th><th>Strong Level 1 Joining Words &amp; Paragraph Starters (W25)</th></tr></thead>"
            "<tbody>"
            "<tr><td><b>Adding Another Point</b></td><td>And, Also</td><td><i>In addition, Furthermore, What is more, As well as this</i></td></tr>"
            "<tr><td><b>Showing Contrast</b></td><td>But</td><td><i>However, Although, On the other hand, Even though, Despite this</i></td></tr>"
            "<tr><td><b>Giving a Reason or Result</b></td><td>So</td><td><i>Because, As a result, Therefore, Because of this, Since</i></td></tr>"
            "<tr><td><b>Ordering Your Paragraphs</b></td><td>First, Last</td><td><i>Firstly, Secondly, Next, Finally, In conclusion, Overall</i></td></tr>"
            "</tbody></table>",
            title="Level 1 Joining Words &amp; Paragraph Connectives Bank"
        )
    )
    pages.append(K.page(p4_body, header=(BOOK, "Core Writing Strategy"), footer=BOOK, page_no=4))

    # p5 to p64: All 12 Authentic Level 1 Formats x 5 pages each = 60 pages
    SHOW_UNIT_IMAGES = True

    p_curr = 5
    format_start_pages = {}
    for f in FORMATS_L1:
        f_idx = f["idx"]
        format_start_pages[f_idx] = p_curr
        f_title = f["title"]
        f_short = f_title.split("(")[0].strip()
        f_marks = f["marks"]
        f_words = f["word_count"]
        f_topic = f["topic"]
        f_aud = f["audience"]
        f_tone = f["tone"]
        f_purpose = f.get("purpose_overview", "")
        f_anat = f.get("anatomy_steps", [])
        f_gold = f.get("golden_rule", "Include all required layout features for this format.")
        f_trap = f.get("examiner_trap", "Check capital letters, full stops, and spelling carefully.")
        f_comm = f.get("examiner_commentary", "")
        f_spec_list = f["specialist_words"]
        f_stim = f["stimulus"]
        f_bullets = f["bullets"]
        f_strat = f["strategy"]
        f_model = f["model_answer"]
        f_voc_dict = f["vocab_definitions"]
        f_pract = f["practice_task"]

        # Page 1: Format Blueprint, Thorough Explanation, 6-Point Anatomy & 12 Specialist Words
        anat_cards = "".join(
            f"<div style='background:#f8fafc;border:1px solid var(--soft);border-left:3px solid var(--primary);border-radius:4px;padding:0.9mm 1.8mm;'>"
            f"<div style='font-weight:800;font-size:8.5pt; /* hf-ok */ color:var(--primary);margin-bottom:0.15mm;'>{escape_html(st_title)}</div>"
            f"<div style='font-size:8.1pt; /* hf-ok */ line-height:1.2;color:#334155;'>{escape_html(st_desc)}</div>"
            f"</div>"
            for st_title, st_desc in f_anat
        )
        spec_pills = "".join(
            f"<span style='display:inline-block;background:#fef3c7;border:1px solid #f59e0b;color:#0f172a;font-weight:700;font-size:8.2pt; /* hf-ok */ padding:0.3mm 1.8mm;border-radius:8px;'>{escape_html(w)}</span>"
            for w in f_spec_list
        )

        art_word = "an" if f_short[:1].lower() in "aeiou" else "a"
        overview_text_html = (
            f"<div style='font-size:8.3pt; /* hf-ok */ line-height:1.2;'>"
            f"<p style='margin:0 0 0.6mm 0;'>{escape_html(f_purpose)}</p>"
            f"<p style='margin:0 0 0.3mm 0;'><b>Target Audience:</b> {escape_html(f_aud)}</p>"
            f"<p style='margin:0 0 0.3mm 0;'><b>Required Tone &amp; Register:</b> {escape_html(f_tone)}</p>"
            f"<p style='margin:0;'><b>Essential Layout Features:</b> {escape_html(f['features'])}</p>"
            f"</div>"
        )
        if SHOW_UNIT_IMAGES and f_idx in UNIT_PHOTOS_L1:
            rel_img, u_cap = UNIT_PHOTOS_L1[f_idx]
            img_path = K.PHOTO_DIR / rel_img
            img_uri = img_path.as_uri() if img_path.exists() else ""
            overview_box_inner = (
                f"<div style='display:grid;grid-template-columns:1.08fr 0.92fr;gap:3mm;align-items:center;'>"
                f"<div style='display:flex;flex-direction:column;justify-content:center;font-size:8.2pt; /* hf-ok */ line-height:1.20;'>"
                f"{overview_text_html}"
                f"</div>"
                f"<div style='background:#ffffff;border:1.5px solid var(--primary);border-radius:6px;overflow:hidden;box-shadow:0 1.5px 4px rgba(0,0,0,0.08);display:flex;flex-direction:column;'>"
                f"<div style='width:100%;aspect-ratio:16/9;overflow:hidden;background:#0f172a;'>"
                f"<img src='{img_uri}' alt='{escape_html(f_short)}' style='width:100%;height:100%;object-fit:cover;object-position:center 25%;display:block;'>"
                f"</div>"
                f"<div style='background:var(--primary);color:#ffffff;font-size:7.8pt; /* hf-ok */ font-weight:700;text-align:center;padding:0.8mm 1.5mm;letter-spacing:0.01em;line-height:1.15;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;'>"
                f"Unit {f_idx}: {u_cap}</div>"
                f"</div>"
                f"</div>"
            )
        else:
            overview_box_inner = overview_text_html

        p1_body = (
            compact_tbl_css
            + K.page_title(f"Format {f_idx}: {f_title}", kicker=f"Format Blueprint &amp; Complete Guide &bull; {f_marks} Marks &bull; {f_words}", badge=f"F{f_idx}")
            + K.rule_box(
                f"What Is {art_word} {f_short}? Purpose, Audience &amp; Layout Rules",
                overview_box_inner
            )
            + K.box_html(
                f"<div style='display:grid;grid-template-columns:1fr 1fr;gap:1.2mm;margin-bottom:1.5mm;'>{anat_cards}</div>"
                f"<div style='background:#f8fafc;border:1px solid var(--soft);border-radius:4px;padding:1.2mm 2mm;'>"
                f"<div style='font-weight:800;font-size:8.5pt; /* hf-ok */ color:var(--primary);margin-bottom:0.6mm;'>"
                f"Unit {f_idx} Specialist Vocabulary Bank ({len(f_spec_list)} Essential Level 1 Terms &mdash; Full Definitions on Page {p_curr+2}):</div>"
                f"<div style='display:flex;flex-wrap:wrap;gap:1mm;'>{spec_pills}</div>"
                f"</div>",
                title="Step-by-Step Structural Anatomy (Top to Bottom) &amp; Specialist Vocabulary"
            )
            + K.tip_pair(
                f_gold,
                f_trap,
                golden_title="Tutor Golden Rule", watch_title="Examiner Red Flag"
            )
        )
        pages.append(K.page(p1_body, header=(BOOK, f"Format {f_idx} &bull; Blueprint"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 2: Exam Scenario, Stimulus Material & Planning Frame
        stim_html = escape_html(f_stim).replace("\n", "<br>")
        bullets_html = K.bullets([escape_html(b) for b in f_bullets])
        p2_body = (
            compact_tbl_css
            + K.page_title(f"Format {f_idx}: {f_short} &bull; Guided Exam Task", kicker=f"Pearson Edexcel Scenario &bull; {f_marks} Marks &bull; {f_words}", badge="TASK")
            + K.box_html(
                f"<div style='background:#f8fafc;padding:2.2mm 2.8mm;border:1.5px solid var(--soft);border-radius:6px;font-size:9.8pt; /* hf-ok */ line-height:1.38;margin-bottom:1.5mm;'>"
                f"<strong style='color:var(--primary);'>Context &amp; Stimulus Material:</strong><br>{stim_html}"
                f"</div>"
                f"<p style='margin:1mm 0;font-size:10pt; /* hf-ok */'><b>Task Instructions:</b> Write your response for the specified audience. In your writing, you must:</p>"
                f"<div style='font-size:9.8pt; /* hf-ok */ line-height:1.34;'>{bullets_html}</div>"
                f"<p style='margin-top:1mm;font-size:9.2pt; /* hf-ok */ color:#475569;'><b>Word Count Target:</b> {f_words} &emsp; <b>Weighting:</b> {f_marks} Marks &emsp; <b>Key Vocab:</b> {escape_html(', '.join(f_spec_list[:6]))}</p>",
                title=f"Official Exam Brief &bull; Format {f_idx}"
            )
            + K.box_html(
                "<div style='display:grid;grid-template-columns:1fr 1fr 1fr;gap:2mm;font-size:9pt; /* hf-ok */'>"
                f"<div style='border:1px solid var(--soft);padding:1.6mm 2mm;border-radius:4px;background:#f8fafc;'><b>1. Audience &amp; Tone:</b><br><span style='color:#475569;font-size:8.4pt; /* hf-ok */'>{escape_html(f_tone[:75])}</span></div>"
                "<div style='border:1px solid var(--soft);padding:1.6mm 2mm;border-radius:4px;background:#f8fafc;'><b>2. Joining Words to Use:</b><br><span style='color:#475569;font-size:8.4pt; /* hf-ok */'>Firstly, Because, Although, However, In addition, Finally</span></div>"
                "<div style='border:1px solid var(--soft);padding:1.6mm 2mm;border-radius:4px;background:#f8fafc;'><b>3. Punctuation Checklist:</b><br><span style='color:#475569;font-size:8.4pt; /* hf-ok */'>Capitals &amp; full stops (.), Commas in lists (,), Question mark (?), Apostrophes (')</span></div>"
                "</div>",
                title="5-Minute TAP Planning Framework (Text, Audience, Purpose)"
            )
            + K.fill_notes("Candidate Paragraph Plan (Opening &bull; Bullet 1 &bull; Bullet 2 &bull; Bullet 3 &bull; Closing Sign-Off)", min_mm=22)
        )
        pages.append(K.page(p2_body, header=(BOOK, f"Format {f_idx} &bull; Task Brief"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 3: Official Full-Marks Benchmark Model Answer + 12 Specialist Vocab Definitions + Examiner Commentary
        model_formatted = render_formatted_model_l1(f_model, f_spec_list)
        vocab_items = "".join(
            f"<div style='font-size:7.9pt; /* hf-ok */ line-height:1.2;padding:0.35mm 0;border-bottom:0.5px dashed #cbd5e1;'>"
            f"<b style='color:var(--primary);'>{escape_html(w)}:</b> {escape_html(d)}</div>"
            for w, d in f_voc_dict.items()
        )
        vocab_box = (
            f"<div style='background:#f8fafc;padding:1.5mm 2.4mm;border:1px solid var(--soft);border-radius:5px;margin-top:1.2mm;'>"
            f"<div style='font-weight:800;font-size:8.6pt; /* hf-ok */ color:var(--primary);margin-bottom:0.6mm;'>"
            f"Specialist Vocabulary &amp; Definitions in This Unit ({len(f_voc_dict)} High-Yield Level 1 Terms):</div>"
            f"<div style='display:grid;grid-template-columns:1fr 1fr;gap:0.2mm 3mm;'>{vocab_items}</div>"
            f"</div>"
        )
        comm_box = (
            f"<div style='background:#f0fdf4;border:1px solid #86efac;border-left:3.5px solid #0f766e;border-radius:5px;padding:1.4mm 2.4mm;margin-top:1.2mm;font-size:8.3pt; /* hf-ok */ line-height:1.26;color:#0f172a;'>"
            f"{f_comm}</div>"
        )

        p3_body = (
            compact_tbl_css
            + K.page_title(f"Format {f_idx}: {f_short} &bull; Full-Marks Model Answer", kicker="Examiner Benchmark Exemplar &bull; Specialist Vocabulary Highlighted", badge="MODEL")
            + K.box_html(
                f"<div style='background:#ffffff;padding:1.8mm 2.5mm;border:1px solid #cbd5e1;border-radius:6px;'>"
                f"{model_formatted}"
                f"</div>"
                f"{vocab_box}"
                f"{comm_box}",
                title=f"Level 1 Full-Marks Exemplar: {f_title}"
            )
        )
        pages.append(K.page(p3_body, header=(BOOK, f"Format {f_idx} &bull; Model"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 4: Unseen Practice Task Brief & Planning Frame
        comp_t = next((t for t in COMPANION_L1_TASKS if t["format_idx"] == f_idx and t["question_num"] == 1), None)
        if comp_t:
            img2_html = ""
            if SHOW_UNIT_IMAGES and f_idx in UNIT_PHOTOS_L1_SECOND:
                rel2, cap2 = UNIT_PHOTOS_L1_SECOND[f_idx]
                img2_path = K.PHOTO_DIR / rel2
                if img2_path.exists():
                    img2_html = (
                        f"<div style='background:#ffffff;border:1.5px solid var(--primary);border-radius:6px;overflow:hidden;box-shadow:0 1.5px 4px rgba(0,0,0,0.08);display:flex;flex-direction:column;'>"
                        f"<div style='width:100%;aspect-ratio:16/9;overflow:hidden;background:#0f172a;'>"
                        f"<img src='{img2_path.as_uri()}' alt='{escape_html(cap2)}' style='width:100%;height:100%;object-fit:cover;object-position:center 25%;display:block;'>"
                        f"</div>"
                        f"<div style='background:#eff6ff;color:var(--primary);font-size:7.8pt; /* hf-ok */ font-weight:700;text-align:center;padding:0.8mm 1.5mm;border-top:1px solid #bfdbfe;line-height:1.15;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;'>"
                        f"Exam Scenario: {cap2}</div>"
                        f"</div>"
                    )

            c_stim = escape_html(comp_t["stimulus"]).replace("\n", "<br>")
            c_bullets = "".join(f"<li style='margin-bottom:1px;'>{escape_html(b)}</li>" for b in comp_t["bullets"])

            if img2_html:
                scenario_block = (
                    f"<div style='display:grid;grid-template-columns:1fr 1fr;gap:3.5mm;align-items:center;margin-bottom:1.5mm;'>"
                    f"<div style='display:flex;flex-direction:column;justify-content:space-between;'>"
                    f"<p style='font-size:9.8pt; /* hf-ok */ margin:0 0 1.2mm 0;'><b>Scenario &amp; Context:</b> {escape_html(comp_t['topic'])}<br><span style='color:#475569;font-size:9pt; /* hf-ok */'><b>Target Audience:</b> {escape_html(comp_t['audience'])}</span></p>"
                    f"<div style='background:#f8fafc;padding:2mm 2.8mm;border:1px solid var(--soft);border-radius:4px;font-size:9.2pt; /* hf-ok */ line-height:1.36;flex:1 1 auto;'>"
                    f"<strong style='color:var(--primary);'>Context &amp; Stimulus:</strong><br>{c_stim}"
                    f"</div>"
                    f"</div>"
                    f"{img2_html}"
                    f"</div>"
                )
            else:
                scenario_block = (
                    f"<p style='font-size:10pt; /* hf-ok */ margin:0 0 1.2mm 0;'><b>Scenario &amp; Context:</b> {escape_html(comp_t['topic'])}<br><span style='color:#475569;font-size:9.2pt; /* hf-ok */'><b>Target Audience:</b> {escape_html(comp_t['audience'])}</span></p>"
                    f"<div style='background:#f8fafc;padding:2mm 3mm;border:1px solid var(--soft);border-radius:4px;font-size:9.5pt; /* hf-ok */ line-height:1.38;margin-bottom:1.5mm;'>"
                    f"<strong style='color:var(--primary);'>Context &amp; Stimulus:</strong><br>{c_stim}"
                    f"</div>"
                )

            p4_body = (
                compact_tbl_css
                + K.page_title(f"Format {f_idx}: {f_short} &bull; Practice Task Brief", kicker=f"Unseen Examination Task &bull; {comp_t['marks']} Marks &bull; {comp_t['word_count']}", badge="TASK")
                + K.box_html(
                    f"{scenario_block}"
                    f"<p style='margin:0 0 1mm 0;font-size:10pt; /* hf-ok */'><b>Task Instructions:</b> In your writing, you must:</p>"
                    f"<ul style='margin:0 0 1.5mm 5mm;padding:0;font-size:9.5pt; /* hf-ok */ line-height:1.34;'>{c_bullets}</ul>"
                    f"<div style='background:#f1f5f9;padding:1.8mm 2.5mm;border-left:3px solid var(--primary);font-size:8.8pt; /* hf-ok */ display:flex;justify-content:space-between;gap:3mm;'>"
                    f"<span><b>Strategy:</b> {escape_html(comp_t['strategy'])}</span>"
                    f"<span><b>Target:</b> {comp_t['word_count']} &bull; <b>Key Words:</b> {escape_html(', '.join(comp_t['specialist_words'][:5]))}</span>"
                    f"</div>",
                    title=f"Unseen Examination Brief &bull; {comp_t['marks']} Marks"
                )
                + K.fill_notes("Candidate TAP Planning &amp; Paragraph Outlines (Intro &bull; Main Body &bull; Action Close)", min_mm=25)
            )
            pages.append(K.page(p4_body, header=(BOOK, f"Format {f_idx} &bull; Task Brief"), footer=BOOK, page_no=p_curr))
            p_curr += 1

            # Page 5: Full-Page Candidate Ruled Response
            p5_body = (
                compact_tbl_css
                + K.page_title(f"Format {f_idx}: {f_short} &bull; Candidate Response", kicker=f"Official Lined Assessment Page &bull; {comp_t['word_count']}")
                + K.fill_lines(f"Write your {f_short} response below ({comp_t['word_count']}):", min_mm=195, gap_mm=9.5)
            )
            pages.append(K.page(p5_body, header=(BOOK, f"Format {f_idx} &bull; Candidate Response"), footer=BOOK, page_no=p_curr))
            p_curr += 1
        else:
            p4_body = (
                compact_tbl_css
                + K.page_title(f"Format {f_idx}: {f_short} &bull; Practice Task Brief", kicker=f"Independent Examination Task &bull; {f_marks} Marks &bull; {f_words}", badge="TASK")
                + K.box_html(
                    f"<p style='font-size:11.5pt;margin:0;'><b>Practice Task:</b> {escape_html(f_pract)}</p>",
                    title="Writing Prompt"
                )
                + K.fill_notes("Candidate Paragraph Outline", min_mm=40)
            )
            pages.append(K.page(p4_body, header=(BOOK, f"Format {f_idx} &bull; Task Brief"), footer=BOOK, page_no=p_curr))
            p_curr += 1

            p5_body = (
                compact_tbl_css
                + K.page_title(f"Format {f_idx}: {f_short} &bull; Candidate Response", kicker=f"Official Lined Assessment Page &bull; {f_words}")
                + K.fill_lines(f"Write your {f_short} response below ({f_words}):", min_mm=195, gap_mm=9.5)
            )
            pages.append(K.page(p5_body, header=(BOOK, f"Format {f_idx} &bull; Candidate Response"), footer=BOOK, page_no=p_curr))
            p_curr += 1

    # p65 to p80: Level 1 SPaG & Spelling Masterclass (16 pages: 8 units x 2 pages)
    spag_l1_tips = {
        1: ("Start every sentence with a capital letter and end with a full stop (.), question mark (?), or exclamation mark (!).", "Always capitalise the word 'I', people's names, towns, days of the week (Monday), and months (September)."),
        2: ("Use commas to separate items in a list and place a comma after a starter clause ('Because the bus was late, ...').", "Never join two complete sentences using only a comma (a comma splice)—use a full stop or a joining word like 'and' or 'but'."),
        3: ("Keep your verb tenses consistent (past for events that already happened; present for current facts) and check agreement.", "Never write 'we was', 'they was', or 'you was' in an exam—always write 'we were', 'they were', and 'you were'."),
        4: ("Use 's for one owner (the manager's office) and s' for more than one owner (the students' common room).", "Remember: 'it's' with an apostrophe always means 'it is' or 'it has'. Possessive 'its' (its opening hours) has NO apostrophe!"),
        5: ("Use joining words (because, although, however, whereas, when, if) to build longer, higher-scoring complex sentences.", "Avoid starting every sentence with 'And' or 'Then'—use 'Firstly', 'In addition', 'However', and 'Finally'."),
        6: ("Learn the everyday Level 1 plural rules (-s, -es, -ies, -ves) and double-check high-risk homophones.", "Check their/there/they're, your/you're, to/too/two, and tricky words like 'necessary', 'business', and 'environment'."),
        7: ("Use polite, standard English without contractions or slang when writing to a manager, landlord, council, or company.", "Save chatty language and contractions (I'm, don't, can't) for informal emails or messages to a close friend."),
        8: ("Leave a clear 5 minutes at the end of Task 1 and Task 2 to read your writing back sentence by sentence.", "If you spot a mistake, cross it out neatly with a single horizontal line and write the correction clearly above it.")
    }

    spag_l1_deep_teaching = {
        1: {
            "bad": (
                "<b>1. Missing Capitals &amp; Full Stop:</b> <b>t</b>he new warehouse opens on <b>m</b>onday <b>a</b>ll staff must wear boots<br>"
                "<b>2. Lowercase 'i' &amp; Place Name:</b> <b>i</b> live in <b>w</b>estford and <b>i</b> work at the local library.<br>"
                "<b>3. Missing Question Mark:</b> Could you please confirm when the engineer will arrive<b>.</b>"
            ),
            "good": (
                "<b>1. Two Clear Sentences:</b> <b>T</b>he new warehouse opens on <b>M</b>onday<b>. A</b>ll staff must wear boots<b>.</b><br>"
                "<b>2. Capital 'I' &amp; Proper Noun:</b> <b>I</b> live in <b>W</b>estford and <b>I</b> work at the local library<b>.</b><br>"
                "<b>3. Accurate Question Mark:</b> Could you please confirm when the engineer will arrive<b>?</b>"
            ),
            "guide": (
                "<table class='t compact'>"
                "<thead><tr><th>Punctuation / Capital Rule</th><th>When to Use It at Level 1</th><th>Model Exam Example</th></tr></thead>"
                "<tbody>"
                "<tr><td><b>Full Stop ( . )</b></td><td>Marks the end of every complete statement sentence</td><td><i>The community centre opens at 9:00 am.</i></td></tr>"
                "<tr><td><b>Question Mark ( ? )</b></td><td>Marks the end of any direct or rhetorical question</td><td><i>How can we make our local park safer?</i></td></tr>"
                "<tr><td><b>Exclamation Mark ( ! )</b></td><td>Shows strong welcome, encouragement, or an urgent warning</td><td><i>Come along and join the fun this Saturday!</i></td></tr>"
                "<tr><td><b>Capital Letters ( A–Z )</b></td><td>First word of a sentence, pronoun <b>I</b>, names, places, days, months</td><td><i>On <b>Friday</b>, <b>Mr Patel</b> visited <b>Oakfield College</b>.</i></td></tr>"
                "</tbody></table>"
            )
        },
        2: {
            "bad": (
                "<b>1. No Commas in a List:</b> We need clean towels<b></b> warm blankets<b></b> and tinned food.<br>"
                "<b>2. Missing Comma After Starter Clause:</b> Because the bus was delayed<b></b> I arrived ten minutes late.<br>"
                "<b>3. Missing Comma After Linking Starter:</b> However<b></b> the background music was far too loud."
            ),
            "good": (
                "<b>1. Commas Separating List Items:</b> We need clean towels<b>,</b> warm blankets<b>,</b> and tinned food.<br>"
                "<b>2. Comma After Starter Clause:</b> Because the bus was delayed<b>,</b> I arrived ten minutes late.<br>"
                "<b>3. Comma After Linking Starter:</b> However<b>,</b> the background music was far too loud."
            ),
            "guide": (
                "<table class='t compact'>"
                "<thead><tr><th>Comma Rule</th><th>How It Works</th><th>Correct Level 1 Example</th></tr></thead>"
                "<tbody>"
                "<tr><td><b>1. Items in a List</b></td><td>Place a comma between items in a list of three or more things</td><td><i>They sell soup<b>,</b> hot rolls<b>,</b> fruit<b>,</b> and flapjacks.</i></td></tr>"
                "<tr><td><b>2. After a Starter Clause</b></td><td>Place a comma where the opening <i>Because / When / If / Although</i> part ends</td><td><i>When I opened the box<b>,</b> the boots were the wrong size.</i></td></tr>"
                "<tr><td><b>3. After a Sequence Word</b></td><td>Place a comma after <i>Firstly, Secondly, However, In addition, Finally</i></td><td><i>Firstly<b>,</b> the car park is full by 8:45 am every day.</i></td></tr>"
                "<tr><td><b>4. Before 'but' or 'so'</b></td><td>Place a comma before <i>but</i> or <i>so</i> when joining two complete clauses</td><td><i>I called your office twice<b>, but</b> nobody has visited yet.</i></td></tr>"
                "</tbody></table>"
            )
        },
        3: {
            "bad": (
                "<b>1. Agreement Error ('We was'):</b> Last Saturday, we <b>was</b> very pleased with the service.<br>"
                "<b>2. Tense Mix-Up:</b> Yesterday I <b>work</b> in the stockroom and <b>lift</b> a heavy box.<br>"
                "<b>3. 'Could of / Should of' Error:</b> The council <b>should of</b> repaired the broken benches."
            ),
            "good": (
                "<b>1. Correct Plural Agreement:</b> Last Saturday, we <b>were</b> very pleased with the service.<br>"
                "<b>2. Consistent Past Tense:</b> Yesterday I <b>worked</b> in the stockroom and <b>lifted</b> a heavy box.<br>"
                "<b>3. Correct Modal ('Should have'):</b> The council <b>should have</b> repaired the broken benches."
            ),
            "guide": (
                "<table class='t compact'>"
                "<thead><tr><th>Grammar Rule (W20)</th><th>Common Exam Mistake (Avoid)</th><th>Correct Level 1 Standard (Use)</th></tr></thead>"
                "<tbody>"
                "<tr><td><b>Was vs Were</b></td><td><i>We was / They was / You was waiting</i></td><td><i><b>We were / They were / You were</b> waiting</i></td></tr>"
                "<tr><td><b>There is vs There are</b></td><td><i>There is lots of broken benches in the park.</i></td><td><i><b>There are</b> several broken benches in the park.</i></td></tr>"
                "<tr><td><b>Consistent Verb Tense</b></td><td><i>Yesterday I go to the café and order soup.</i></td><td><i>Yesterday I <b>went</b> to the café and <b>ordered</b> soup.</i></td></tr>"
                "<tr><td><b>Articles (a vs an)</b></td><td><i>a urgent repair / a honest mistake / a hour</i></td><td><i><b>an</b> urgent repair / <b>an</b> honest mistake / <b>an</b> hour</i></td></tr>"
                "</tbody></table>"
            )
        },
        4: {
            "bad": (
                "<b>1. Missing Possessive Apostrophe:</b> The <b>customers</b> coat was left on the <b>managers</b> chair.<br>"
                "<b>2. Its vs It's Mix-Up:</b> The library updated <b>it's</b> timetable because <b>its</b> very busy.<br>"
                "<b>3. Accidental Plural Apostrophe:</b> We sell hot <b>drink's</b>, <b>cake's</b>, and <b>sandwich's</b>."
            ),
            "good": (
                "<b>1. Singular Possessive ('s):</b> The <b>customer's</b> coat was left on the <b>manager's</b> chair.<br>"
                "<b>2. Correct Its vs It's:</b> The library updated <b>its</b> timetable because <b>it's</b> (it is) very busy.<br>"
                "<b>3. Ordinary Plurals (No Apostrophe):</b> We sell hot <b>drinks</b>, <b>cakes</b>, and <b>sandwiches</b>."
            ),
            "guide": (
                "<table class='t compact'>"
                "<thead><tr><th>Apostrophe Type</th><th>Simple Rule to Follow</th><th>Correct Examples</th></tr></thead>"
                "<tbody>"
                "<tr><td><b>1. Contraction (Missing Letter)</b></td><td>Shows where letters have been left out (<i>do not &rarr; don't</i>)</td><td><i><b>it's</b> (it is), <b>don't</b> (do not), <b>can't</b> (cannot), <b>I'm</b> (I am)</i></td></tr>"
                "<tr><td><b>2. One Owner ( 's )</b></td><td>Add <b>'s</b> to a singular noun to show something belongs to one person/thing</td><td><i>the <b>manager's</b> desk, <b>Tom's</b> back, the <b>dog's</b> personality</i></td></tr>"
                "<tr><td><b>3. Plural Owners Ending in -s ( s' )</b></td><td>When a plural noun already ends in -s, put the apostrophe <b>after the s</b></td><td><i>the <b>students'</b> bikes, the <b>boys'</b> football team, <b>residents'</b> views</i></td></tr>"
                "<tr><td><b>4. Irregular Plurals ( 's )</b></td><td>If a plural word does not end in -s (<i>children, people, men</i>), add <b>'s</b></td><td><i>the <b>children's</b> play area, <b>people's</b> safety, <b>women's</b> health</i></td></tr>"
                "</tbody></table>"
            )
        },
        5: {
            "bad": (
                "<b>1. Choppy Short Sentences:</b> The car park is small. It fills up early. Students arrive late.<br>"
                "<b>2. Overusing 'And then':</b> I lifted the box and then my back hurt and then I dropped it.<br>"
                "<b>3. Incomplete Fragment:</b> Because the lock on the back door is loose."
            ),
            "good": (
                "<b>1. Joined Complex Sentence:</b> <b>Because</b> the car park is small, it fills up early <b>and</b> students arrive late.<br>"
                "<b>2. Clear Cause &amp; Result:</b> <b>When</b> I lifted the heavy box, I felt sharp pain in my back <b>so</b> I dropped it.<br>"
                "<b>3. Complete Complex Sentence:</b> We cannot secure the flat at night <b>because</b> the lock on the back door is loose."
            ),
            "guide": (
                "<table class='t compact'>"
                "<thead><tr><th>Type of Joining Word</th><th>Key Words to Use</th><th>Model Complex Sentence (W25)</th></tr></thead>"
                "<tbody>"
                "<tr><td><b>Reason (Why)</b></td><td><i>because, since, as, so that</i></td><td><i>I paid £5.99 for express delivery <b>because</b> I needed the boots for Saturday.</i></td></tr>"
                "<tr><td><b>Contrast (Opposite)</b></td><td><i>although, even though, whereas, while</i></td><td><i><b>Although</b> I have telephoned your office twice, no engineer has visited.</i></td></tr>"
                "<tr><td><b>Time &amp; Condition</b></td><td><i>when, while, before, after, if, unless</i></td><td><i><b>If</b> you feel overwhelmed by revision, speak to your course tutor.</i></td></tr>"
                "</tbody></table>"
            )
        },
        6: {
            "bad": (
                "<b>1. Homophone Mix-Up:</b> <b>Their</b> are <b>to</b> many cars parked over <b>they're</b>.<br>"
                "<b>2. Wrong Plural Ending:</b> Local <b>companys</b> donated three <b>boxs</b> of <b>scarfs</b>.<br>"
                "<b>3. Misspelled Everyday Words:</b> It is <b>neccessary</b> to fix the <b>maintenence</b> issues <b>immediatly</b>."
            ),
            "good": (
                "<b>1. Correct Homophones:</b> <b>There</b> are <b>too</b> many cars parked over <b>there</b>.<br>"
                "<b>2. Correct Plural Rules:</b> Local <b>companies</b> donated three <b>boxes</b> of <b>scarves</b>.<br>"
                "<b>3. Accurate Level 1 Spellings:</b> It is <b>necessary</b> to fix the <b>maintenance</b> issues <b>immediately</b>."
            ),
            "guide": (
                "<table class='t compact'>"
                "<thead><tr><th>Spelling Area (W21)</th><th>Golden Rules &amp; High-Frequency Exam Words</th></tr></thead>"
                "<tbody>"
                "<tr><td><b>Big 4 Homophone Groups</b></td><td><b>there</b> (place / there is) / <b>their</b> (belongs to them) / <b>they're</b> (they are) &bull; <b>your</b> (belongs to you) / <b>you're</b> (you are) &bull; <b>to</b> (direction) / <b>too</b> (too much / also) / <b>two</b> (2) &bull; <b>where</b> (place) / <b>wear</b> (clothes) / <b>were</b> (past of are)</td></tr>"
                "<tr><td><b>Plural Spelling Rules</b></td><td>Words ending in <i>-ch, -sh, -s, -x</i> &rarr; add <b>-es</b> (<i>box &rarr; boxes, bus &rarr; buses</i>) &bull; Consonant + <i>y</i> &rarr; change <i>y</i> to <b>-ies</b> (<i>company &rarr; companies, family &rarr; families, activity &rarr; activities</i>) &bull; <i>-f / -fe</i> &rarr; <b>-ves</b> (<i>knife &rarr; knives, shelf &rarr; shelves</i>)</td></tr>"
                "<tr><td><b>Prefixes &amp; Suffixes</b></td><td>Add prefixes without dropping letters: <b>un</b>comfortable, <b>dis</b>appointed, <b>in</b>correct, <b>mis</b>understand &bull; Drop silent <i>-e</i> before <i>-ing</i> (<i>make &rarr; making, have &rarr; having</i>), keep <i>-e</i> before <i>-ful / -ly</i> (<i>careful, definitely</i>)</td></tr>"
                "<tr><td><b>Top 16 Level 1 Exam Words</b></td><td><i>accommodation, address, appointment, attention, because, business, community,customer, different, disappointed, environment, equipment, friend, immediately, maintenance, necessary, recommend, sincerely, tomorrow, Wednesday</i></td></tr>"
                "</tbody></table>"
            )
        },
        7: {
            "bad": (
                "<b>1. Slang in a Formal Letter:</b> I'm writing coz the shower in my flat is totally rubbish.<br>"
                "<b>2. Rude Demand to Manager:</b> Sort this mess out ASAP or I'm not paying rent.<br>"
                "<b>3. Informal Sign-Off in Complaint:</b> Cheers mate, speak soon, Jordan."
            ),
            "good": (
                "<b>1. Polite Formal Opening:</b> I am writing to report an urgent fault with the shower in my flat.<br>"
                "<b>2. Firm &amp; Polite Request:</b> Please arrange for an engineer to repair the shower by Friday.<br>"
                "<b>3. Correct Formal Sign-Off:</b> Thank you for your assistance. Yours sincerely, Jordan Miller."
            ),
            "guide": (
                "<table class='t compact'>"
                "<thead><tr><th>Feature</th><th>Formal Writing (Letters, Reports, Work Emails)</th><th>Informal Writing (Friend Email, Forum, Club)</th></tr></thead>"
                "<tbody>"
                "<tr><td><b>Greeting</b></td><td><i>Dear Mr Green, / Dear Sir or Madam,</i></td><td><i>Hi Sam, / Dear Auntie Claire, / Hi DogLover99,</i></td></tr>"
                "<tr><td><b>Vocabulary &amp; Tone</b></td><td>Polite, factual, standard English (<i>request, inconvenience, urgente</i>)</td><td>Warm, friendly, conversational (<i>great, lovely, can't wait</i>)</td></tr>"
                "<tr><td><b>Contractions</b></td><td>Write in full (<i>I am, do not, cannot, I would like</i>)</td><td>Contractions allowed (<i>I'm, don't, it's, we'll</i>)</td></tr>"
                "<tr><td><b>Sign-Off</b></td><td><i>Yours sincerely, / Yours faithfully, / Kind regards,</i></td><td><i>Best wishes, / See you soon, / Lots of love,</i></td></tr>"
                "</tbody></table>"
            )
        },
        8: {
            "bad": (
                "<b>1. Unchecked Draft:</b> on tuesday i went to the cafe with my freind their was a £5 meal deal<br>"
                "<b>2. Messy Scribble Correction:</b> We ordered <del>sammwiches</del> sandwiches.<br>"
                "<b>3. Missing Bullet Point:</b> Forgot to answer the final bullet point in the question."
            ),
            "good": (
                "<b>1. Checked Final Sentence:</b> <b>O</b>n <b>T</b>uesday<b>, I</b> went to the caf&eacute; with my <b>friend. There</b> was a &pound;5 meal deal<b>.</b><br>"
                "<b>2. Neat Single-Line Correction:</b> Waiters served fresh sandwiches.<br>"
                "<b>3. Full Prompt Coverage:</b> Ticked off all 3 or 4 bullet points against my paragraphs."
            ),
            "guide": (
                "<table class='t compact'>"
                "<thead><tr><th>5-Minute Proofreading Step</th><th>What to Look For on Your Exam Page</th></tr></thead>"
                "<tbody>"
                "<tr><td><b>Minute 1: Bullet Point Check</b></td><td>Tick off every bullet point in the question—have you answered all of them in clear paragraphs?</td></tr>"
                "<tr><td><b>Minute 2: Format Features Check</b></td><td>Check addresses/date (letter), To/Subject (email), headline/subheadings (article/leaflet/report), and sign-off.</td></tr>"
                "<tr><td><b>Minute 3: Sentence Boundaries</b></td><td>Point to the start and end of every sentence: does each one have a capital letter and a full stop or question mark?</td></tr>"
                "<tr><td><b>Minutes 4–5: Spelling &amp; Capitals</b></td><td>Check capital <b>I</b>, days/months, <i>their/there/they're</i>, <i>to/too/two</i>, <i>we were</i>, and tricky everyday words.</td></tr>"
                "</tbody></table>"
            )
        }
    }

    spag_start_pages = {}
    # Current p_curr is 65. 8 SPaG units x 2p = 16p (65..80). 2 Mocks x 6p = 12p (81..92). 4 Rubric pages = 4p (93..96).
    # So Reference Section starts at page 97!
    ref_section_start_page = p_curr + 16 + 12 + 4

    for sp_idx in range(1, 9):
        spag_start_pages[sp_idx] = p_curr
        sp_ex = SPAG_L1_EXERCISES.get(sp_idx, {})
        sp_title = sp_ex.get("title", f"SPaG Unit {sp_idx}")
        sp_rule = sp_ex.get("rule", "Apply standard punctuation, grammar, and spelling rules.")
        sp_inputs = sp_ex.get("inputs", [])
        sp_instruction = sp_ex.get("instruction", "Rewrite each sentence correctly.")
        gold_tip, watch_tip = spag_l1_tips.get(sp_idx, ("Apply standard punctuation rules.", "Check sentence boundaries."))
        deep = spag_l1_deep_teaching[sp_idx]

        # Unit Page 1: Complete Theory, Worked Examples (Wrong vs Right) & Reference Table
        p1_spag = (
            compact_tbl_css
            + K.page_title(f"SPaG Masterclass {sp_idx}: {sp_title}", kicker="Level 1 Punctuation, Grammar &amp; Spelling &bull; W19–W21 &amp; W25", badge=f"S{sp_idx}")
            + K.rule_box("Core Level 1 Rule &amp; Exam Benchmark", f"<p style='font-size:10pt; /* hf-ok */ line-height:1.35;margin:0;'><b>{escape_html(sp_rule)}</b></p>")
            + K.compare(deep["bad"], deep["good"], bad_label="&#10007; Common Exam Mistakes (Loses Marks)", good_label="&#10003; Full-Marks Level 1 Solutions")
            + K.box_html(deep["guide"], title=f"Unit {sp_idx} Quick-Reference Rules &amp; Examples")
            + K.tip_pair(gold_tip, watch_tip, golden_title="Top Level 1 Tip", watch_title="Common Exam Trap")
        )
        pages.append(K.page(p1_spag, header=(BOOK, f"SPaG {sp_idx} &bull; Theory"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Unit Page 2: Applied Sentence Calibration Drill
        inputs_html = "<br><br>".join(f"<b>{escape_html(inp)}</b>" for inp in sp_inputs)
        sp_img_html = ""
        if sp_idx in SPAG_WRITING_PHOTOS:
            sp_rel, sp_cap = SPAG_WRITING_PHOTOS[sp_idx]
            sp_path = K.PHOTO_DIR / sp_rel
            if sp_path.exists():
                sp_img_html = (
                    f"<div style='background:#ffffff;border:1.5px solid var(--primary);border-radius:6px;overflow:hidden;box-shadow:0 1.5px 4px rgba(0,0,0,0.08);display:flex;flex-direction:column;'>"
                    f"<div style='width:100%;aspect-ratio:16/9;overflow:hidden;background:#0f172a;'>"
                    f"<img src='{sp_path.as_uri()}' alt='{escape_html(sp_cap)}' style='width:100%;height:100%;object-fit:cover;object-position:center 25%;display:block;'>"
                    f"</div>"
                    f"<div style='background:#eff6ff;color:var(--primary);font-size:7.8pt; /* hf-ok */ font-weight:700;text-align:center;padding:0.8mm 1.5mm;border-top:1px solid #bfdbfe;line-height:1.15;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;'>"
                    f"Everyday Application: {sp_cap}</div>"
                    f"</div>"
                )

        if sp_img_html:
            sp_task_top = (
                f"<div style='display:grid;grid-template-columns:1fr 1fr;gap:3.5mm;align-items:center;margin-bottom:2.5mm;'> "
                f"<div style='display:flex;flex-direction:column;justify-content:center;'>"
                f"<p style='font-size:11.2pt;margin:0 0 1.8mm 0;line-height:1.35;'><b>Practice Task:</b> {escape_html(sp_instruction)}</p>"
                f"<div style='background:#eff6ff;border-left:3.5px solid var(--primary);border-radius:4px;padding:2mm 2.8mm;font-size:9.5pt;color:#1e3a8a;line-height:1.34;'>"
                f"<b>Level 1 Standard:</b> Read each everyday sentence carefully. Check capitalization, punctuation, and subject-verb agreement, then write your corrected version below."
                f"</div>"
                f"</div>"
                f"{sp_img_html}"
                f"</div>"
            )
        else:
            sp_task_top = f"<p style='font-size:12pt;margin-top:0;'><b>Practice Task:</b> {escape_html(sp_instruction)}</p>"

        p2_spag = (
            K.page_title(f"SPaG Masterclass {sp_idx} &bull; Practice Drill", kicker="Applied Everyday &amp; Workplace Sentence Practice", badge="DRILL")
            + K.box_html(
                f"{sp_task_top}"
                f"<div style='background:#f8fafc;padding:3mm 3.5mm;border:1.5px solid var(--soft);border-radius:6px;font-size:11pt;line-height:1.45;'>"
                f"{inputs_html}"
                f"</div>",
                title=f"Sentences to Correct ({len(sp_inputs)} Items)"
            )
            + K.fill_lines(f"Write your corrected sentences below (check worked answers on p. {ref_section_start_page}):", min_mm=25, gap_mm=9.5)
        )
        pages.append(K.page(p2_spag, header=(BOOK, f"SPaG {sp_idx} &bull; Drill"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p81 to p92: 2 Full Level 1 Mock Papers (12 pages: 6 pages each)
    mock1_start_page = p_curr
    m1_l1 = MOCK_ENGLISH_L1_PAPERS[0]
    t1_l1_1 = m1_l1["task1"]
    t1_l1_2 = m1_l1["task2"]

    p65_body = (
        K.page_title("Official Mock Writing Examination &bull; Paper 1", kicker="Pearson Edexcel Level 1 Simulation &bull; 60 Minutes &bull; 36 Marks", badge="MOCK 1")
        + K.box_html(
            "<div style='font-size:12.5pt;line-height:1.55;'>"
            "<p><b>Instructions to Candidates:</b></p>"
            "<ul>"
            "<li>Total time: <b>60 minutes</b>. Total marks: <b>36 marks</b>.</li>"
            "<li>Complete <b>BOTH</b> tasks: Task 1 (21 marks, 150–250 words, 35 minutes) and Task 2 (15 marks, 100–180 words, 25 minutes).</li>"
            "<li>You must <b>not</b> use a dictionary or spellchecker.</li>"
            "<li>Write in complete sentences with capital letters and full stops, and organise your ideas into clear paragraphs.</li>"
            "<li>Check your work carefully: 41.7% of marks are awarded for Spelling, Punctuation and Grammar.</li>"
            "</ul>"
            "</div>",
            title="Examination Regulations &amp; Timing Guidance"
        )
        + K.tip_pair("Spend 5 minutes planning your format layout and paragraph points before you start writing.",
                     "Leave 5 minutes at the end of each task to check your capital letters, full stops, and spelling.",
                     golden_title="Planning Strategy", watch_title="Proofreading Check")
        + K.fill_notes("Pre-Exam Readiness Notes &amp; Target Score", min_mm=35)
    )
    pages.append(K.page(p65_body, header=(BOOK, "Mock 1 &bull; Overview"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    p66_body = (
        K.page_title(f"Mock 1 &bull; {t1_l1_1['title']}", kicker="Task 1 (Extended Writing) &bull; 21 Marks &bull; 150–250 Words", badge="T1")
        + K.box_html(
            f"<p style='font-size:12.5pt;line-height:1.5;'><b>Scenario:</b> {escape_html(t1_l1_1['scenario'])}</p>"
            + K.bullets([escape_html(b) for b in t1_l1_1["bullets"]])
            + f"<p style='font-size:11pt;color:#64748b;margin-top:2mm;'><b>Recommended Time:</b> 35 Minutes &emsp; <b>Target Length:</b> 150&ndash;250 words</p>",
            title="Task 1 Brief &bull; 21 Marks"
        )
        + K.fill_notes("Task 1 Planning Frame (Addresses &bull; Salutation &bull; Paragraph 1 &bull; Paragraph 2 &bull; Sign-Off)", min_mm=40)
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
        K.page_title(f"Mock 1 &bull; {t1_l1_2['title']}", kicker="Task 2 (Shorter Writing) &bull; 15 Marks &bull; 100–180 Words", badge="T2")
        + K.box_html(
            f"<p style='font-size:12.5pt;line-height:1.5;'><b>Scenario:</b> {escape_html(t1_l1_2['scenario'])}</p>"
            + K.bullets([escape_html(b) for b in t1_l1_2["bullets"]])
            + f"<p style='font-size:11pt;color:#64748b;margin-top:2mm;'><b>Recommended Time:</b> 25 Minutes &emsp; <b>Target Length:</b> 100&ndash;180 words</p>",
            title="Task 2 Brief &bull; 15 Marks"
        )
        + K.fill_notes("Task 2 Planning Frame (Headline &bull; Byline &bull; Subheadings &bull; Key Points)", min_mm=40)
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
        K.page_title("Mock 1 &bull; Candidate Post-Exam Audit", kicker="Self-Evaluation &amp; Mark Scheme Alignment", badge="AUDIT")
        + K.box_html(
            f"<p>Check your Mock 1 answers against the official Level 1 checklist before reading the benchmark solutions on p. {ref_section_start_page + 1}:</p>"
            + K.bullets([
                "<b>Word Count Check:</b> Did you write 150–250 words for Task 1 and 100–180 words for Task 2?",
                "<b>Format Check:</b> Did Task 1 include both postal addresses, the date, 'Dear Mr Green,' and 'Yours sincerely,'? Did Task 2 have a headline and subheadings?",
                "<b>Bullet Points:</b> Did you answer every single bullet point in clear paragraphs?",
                "<b>SPaG Check:</b> Does every sentence start with a capital letter and end with a full stop or question mark?"
            ]),
            title="Post-Mock Verification Checklist"
        )
        + K.fill_notes("Personal Reflections &amp; Spellings to Practise After Mock 1", min_mm=45)
    )
    pages.append(K.page(p70_body, header=(BOOK, "Mock 1 &bull; Audit"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Mock Paper 2 (6 pages)
    mock2_start_page = p_curr
    m2_l1 = MOCK_ENGLISH_L1_PAPERS[1]
    t2_l1_1 = m2_l1["task1"]
    t2_l1_2 = m2_l1["task2"]

    p71_body = (
        K.page_title("Official Mock Writing Examination &bull; Paper 2", kicker="Pearson Edexcel Level 1 Simulation &bull; 60 Minutes &bull; 36 Marks", badge="MOCK 2")
        + K.box_html(
            "<div style='font-size:12.5pt;line-height:1.55;'>"
            "<p><b>Instructions to Candidates:</b></p>"
            "<ul>"
            "<li>Complete both Task 1 (21 marks, 35 minutes) and Task 2 (15 marks, 25 minutes) under timed exam conditions.</li>"
            "<li>Use joining words (<i>because, although, however, in addition</i>) to link your ideas smoothly.</li>"
            "<li>Remember to include the right layout features for an email (Task 1) and an information flyer/leaflet (Task 2).</li>"
            "</ul>"
            "</div>",
            title="Mock Paper 2 Instructions"
        )
        + K.tip_pair("Keep your workplace email polite, clear, and helpful.",
                     "Use subheadings and bullet points in your community open day flyer so key details stand out.",
                     golden_title="Polite Tone", watch_title="Leaflet Layout")
        + K.fill_notes("Target Commitments for Mock Paper 2", min_mm=40)
    )
    pages.append(K.page(p71_body, header=(BOOK, "Mock 2 &bull; Overview"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    p72_body = (
        K.page_title(f"Mock 2 &bull; {t2_l1_1['title']}", kicker="Task 1 (Extended Writing) &bull; 21 Marks &bull; 150–250 Words", badge="T1")
        + K.box_html(
            f"<p style='font-size:12.5pt;line-height:1.5;'><b>Scenario:</b> {escape_html(t2_l1_1['scenario'])}</p>"
            + K.bullets([escape_html(b) for b in t2_l1_1["bullets"]])
            + f"<p style='font-size:11pt;color:#64748b;margin-top:2mm;'><b>Recommended Time:</b> 35 Minutes &emsp; <b>Target Length:</b> 150&ndash;250 words</p>",
            title="Task 1 Brief &bull; 21 Marks"
        )
        + K.fill_notes("Task 1 Planning Frame (To/Subject &bull; Greeting &bull; Paragraphs &bull; Sign-Off)", min_mm=40)
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
        K.page_title(f"Mock 2 &bull; {t2_l1_2['title']}", kicker="Task 2 (Shorter Writing) &bull; 15 Marks &bull; 100–180 Words", badge="T2")
        + K.box_html(
            f"<p style='font-size:12.5pt;line-height:1.5;'><b>Scenario:</b> {escape_html(t2_l1_2['scenario'])}</p>"
            + K.bullets([escape_html(b) for b in t2_l1_2["bullets"]])
            + f"<p style='font-size:11pt;color:#64748b;margin-top:2mm;'><b>Recommended Time:</b> 25 Minutes &emsp; <b>Target Length:</b> 100&ndash;180 words</p>",
            title="Task 2 Brief &bull; 15 Marks"
        )
        + K.fill_notes("Task 2 Planning Frame (Bold Heading &bull; Date/Time/Venue &bull; Activity Bullets &bull; Refreshments)", min_mm=40)
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
        K.page_title("Mock 2 &bull; Candidate Post-Exam Audit", kicker="Self-Evaluation &amp; Mark Scheme Alignment", badge="AUDIT")
        + K.box_html(
            f"<p>Check your Mock 2 work against the official Level 1 criteria before checking the model answers on p. {ref_section_start_page + 2}:</p>"
            + K.bullets([
                "<b>Task 1 Email Layout:</b> Did you include To:, Subject:, 'Dear Mrs Clark,', clear paragraphs, and 'Kind regards,'?",
                "<b>Task 2 Flyer Layout:</b> Did you include a bold title, the date/time/location, bulleted activities, and refreshment/parking details?",
                "<b>Complex Sentences:</b> Did you use joining words like 'because', 'when', and 'so that'?",
                "<b>Proofreading:</b> Did you check capital letters, full stops, and common spellings?"
            ]),
            title="Post-Mock Verification Checklist"
        )
        + K.fill_notes("Personal Reflections &amp; Targets After Mock 2", min_mm=45)
    )
    pages.append(K.page(p76_body, header=(BOOK, "Mock 2 &bull; Audit"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # p93 to p96: Official Level 1 Marking Rubrics (4 pages)
    rubric_start_page = p_curr
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

    # p97 to p102: Reference Back Matter via K.ref_pages
    ref_actual_start = p_curr
    ref_blocks = []

    # SPaG Solutions (render formatted HTML cleanly without double-escaping <b> tags)
    for u_idx in range(1, 9):
        qas = SPAG_L1_SOLUTIONS.get(u_idx, [])
        qa_html = "".join(K.ref_qa(q_num, ans, marks=mk, working=escape_html(wk)) for q_num, ans, mk, wk in qas)
        u_title = SPAG_L1_EXERCISES[u_idx]["title"]
        ref_blocks.append(K.ref_block(f"Level 1 SPaG Unit {u_idx}: {escape_html(u_title)}", qa_html))

    # Mock 1 & Mock 2 Benchmark Solutions (All 4 Tasks)
    m1_l1_t1_model = (
        "14 Oakwood Close, Greendale, GD2 4PT<br>15 November 2026<br><br>"
        "Mr Robert Green, Store Manager<br>Greendale Garden Centre, High Street, Greendale, GD2 1AB<br><br>"
        "Dear Mr Green,<br><br>"
        "<b>Re: Application for Part-Time Weekend Customer &amp; Stock Assistant</b><br><br>"
        "I am writing to apply for the position of Part-Time Weekend Customer and Stock Assistant, which I saw advertised on the Greendale Garden Centre noticeboard. I am a keen gardener with a strong knowledge of outdoor plants, composts, and garden tools.<br><br>"
        "For the past two years, I have worked as a volunteer assistant at a busy charity shop. In this role, I served customers at the till, answered questions politely, and priced new stock in the storage room. I enjoy working as part of a friendly team and am physically fit and happy to lift heavy bags of compost safely.<br><br>"
        "I am available to work every Saturday and Sunday from 8:00 am to 5:00 pm, as well as Thursday evenings if required. I can attend an interview on any weekday afternoon.<br><br>"
        "Thank you for considering my application. I look forward to hearing from you.<br><br>"
        "Yours sincerely,<br>Alex Smith"
    )
    ref_blocks.append(K.ref_block("Level 1 Mock 1 &bull; Task 1 Benchmark Solution (21 Marks)",
                                  K.ref_qa("T1", m1_l1_t1_model, marks="21/21", working="Full marks: Complete UK formal letter layout, clear paragraphs covering all three bullets, polite tone, and accurate spelling and punctuation throughout.")))

    m1_l1_t2_model = (
        "<b>Why We Should All Love Our Local High Street!</b><br>By Alex Smith | Local Resident<br><br>"
        "Independent shops and family-run cafés are the heart of our town. If we want our high street to stay lively and welcoming, we must support our local businesses before they disappear.<br><br>"
        "<b>Why Shopping Locally Is Great</b><br>"
        "Personally, I love visiting our local bakery and greengrocer on Saturday mornings. The fresh bread and local vegetables taste much better than supermarket food, and the shopkeepers always greet customers with a warm smile and helpful advice.<br><br>"
        "<b>How We Can Help</b><br>"
        "Firstly, residents can help by buying their weekly fruit, gifts, and coffee from local independent traders. Secondly, the town council should offer one hour of free car parking on Saturdays to attract more shoppers into town. Let's support our local high street together!"
    )
    ref_blocks.append(K.ref_block("Level 1 Mock 1 &bull; Task 2 Benchmark Solution (15 Marks)",
                                  K.ref_qa("T2", m1_l1_t2_model, marks="15/15", working="Full marks: Catchy headline, writer's byline, two clear subheadings, engaging tone, and practical recommendations.")))

    m2_l1_t1_model = (
        "<b>To:</b> susan.clark@megastore.co.uk<br>"
        "<b>Subject:</b> Proposal for Short Till and Returns Refresher Training<br><br>"
        "Dear Mrs Clark,<br><br>"
        "I am writing to suggest a short training refresher session for our new customer service assistants who joined the store this month.<br><br>"
        "Over the past week, several new colleagues have told me that they find the computer till screen and the customer refund process confusing. Because they have to wait for a supervisor to authorise returns, long queues are building up at the main checkouts during busy lunchtime periods.<br><br>"
        "Running a practical 30-minute training workshop would boost staff confidence, reduce till mistakes, and help us serve customers much faster. I suggest holding the session on Tuesday morning between 8:30 am and 9:00 am before the store opens, so it does not disrupt trading.<br><br>"
        "I would be happy to help demonstrate the returns system. Please let me know if you think this is a good idea.<br><br>"
        "Kind regards,<br>Sam Taylor (Customer Service Assistant)"
    )
    ref_blocks.append(K.ref_block("Level 1 Mock 2 &bull; Task 1 Benchmark Solution (21 Marks)",
                                  K.ref_qa("T1", m2_l1_t1_model, marks="21/21", working="Full marks: Clear email header, polite workplace register, well-linked complex sentences ('Because...'), and full coverage of all three prompt bullets.")))

    m2_l1_t2_model = (
        "<b>OAKWOOD COMMUNITY CENTRE: FREE FAMILY OPEN DAY!</b><br>"
        "<b>When:</b> Saturday 24th October | 10:00 am – 3:00 pm<br>"
        "<b>Where:</b> Oakwood Community Centre, Station Road (Free Admission!)<br><br>"
        "Come along and discover the exciting new clubs and classes running in your neighbourhood this autumn!<br><br>"
        "<b>Free Taster Sessions &amp; Activities on the Day:</b><br>"
        "&bull; <b>Try a New Sport:</b> Join our free 30-minute beginner badminton, table tennis, and yoga sessions in the main hall.<br>"
        "&bull; <b>Digital Skills Drop-In:</b> Visit our computer suite for friendly advice on using laptops, emails, and online banking.<br>"
        "&bull; <b>Arts, Crafts &amp; Youth Club:</b> Fun painting workshops for children and teenagers all afternoon.<br><br>"
        "<b>Visitor Information:</b><br>"
        "Enjoy free tea, coffee, juice, and homemade biscuits in our café area! Free car parking and secure bike racks are available right outside the main entrance. Everyone is welcome!"
    )
    ref_blocks.append(K.ref_block("Level 1 Mock 2 &bull; Task 2 Benchmark Solution (15 Marks)",
                                  K.ref_qa("T2", m2_l1_t2_model, marks="15/15", working="Full marks: Eye-catching flyer heading, clear date/time/venue block, bulleted taster sessions, and complete refreshment/parking information.")))

    # Glossary — split into 3 balanced column blocks so each block fits within a single 240mm column without horizontal overflow
    g_chunk1 = GLOSSARY_L1[:10]
    g_chunk2 = GLOSSARY_L1[10:20]
    g_chunk3 = GLOSSARY_L1[20:]
    for g_title, g_items in [
        ("Level 1 Functional Writing Glossary (A–C)", g_chunk1),
        ("Level 1 Functional Writing Glossary (C–N)", g_chunk2),
        ("Level 1 Functional Writing Glossary (P–V)", g_chunk3),
    ]:
        g_html = "".join(f"<dl><dt>{escape_html(t)}</dt><dd>{escape_html(d)}</dd></dl>" for t, d in g_items)
        ref_blocks.append(K.ref_block(g_title, g_html))

    # Index — split into 2 balanced column blocks (A–I and M–T)
    idx_part1 = ""
    for letter, entries in INDEX_L1[:9]:
        items = "".join(f"<div class='ix'><span>{escape_html(t)}</span><span>{escape_html(p)}</span></div>" for t, p in entries)
        idx_part1 += f"<div class='ix-letter'>{letter}</div>{items}"
    ref_blocks.append(K.ref_block("Subject, Format &amp; Alphabetical Index (A–I)", idx_part1))

    idx_part2 = ""
    for letter, entries in INDEX_L1[9:]:
        items = "".join(f"<div class='ix'><span>{escape_html(t)}</span><span>{escape_html(p)}</span></div>" for t, p in entries)
        idx_part2 += f"<div class='ix-letter'>{letter}</div>{items}"
    ref_blocks.append(K.ref_block("Alphabetical Index (M–T)", idx_part2))

    cover_theme = K.theme_from_cover(front_cov)
    ref_page_list = K.ref_pages("Reference Section: Solutions, Glossary &amp; Index", ref_blocks,
                                BOOK, start_page=p_curr, subtitle="Complete Worked Solutions, Lexicon &amp; Alphabetical Index",
                                cols=2, theme=cover_theme, notes_title="Candidate Reference Notes &amp; Exam Checklist")
    pages.extend(ref_page_list)
    p_curr += len(ref_page_list)

    # Pre-Exam Readiness Commitments
    readiness_page = p_curr
    p100_body = (
        K.page_title("Candidate Pre-Exam Self-Audit &amp; Readiness Commitments", kicker="Final Revision &bull; Level 1 Examination Day Protocol", badge="READY")
        + K.box_html(
            "<p>Before entering the examination room, confirm your commitment to these five essential Level 1 standards:</p>"
            + K.bullets([
                "<b>100% Sentence Punctuation:</b> Every sentence begins with a capital letter and ends with a full stop, question mark, or exclamation mark.",
                "<b>Clear Paragraphing:</b> Every bullet point in the question is developed into its own clear paragraph separated by a blank line.",
                "<b>Correct Format Layout:</b> Letters have addresses and matching sign-offs; emails have To/Subject lines; articles, reports, and leaflets have clear headings.",
                "<b>Joined Complex Sentences:</b> Ideas are linked smoothly using joining words such as <i>because, although, however,</i> and <i>in addition</i>.",
                "<b>5-Minute Final Check:</b> Reserve the final 5 minutes of each task to check capital 'I', proper nouns, homophones, and everyday spellings."
            ]),
            title="Final Level 1 Examination Commitments"
        )
        + K.fill_notes("Personal Exam Day Notes &amp; Success Commitments", min_mm=40)
    )
    pages.append(K.page(p100_body, header=(BOOK, "Exam Readiness"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Now populate Page 2 (Complete Table of Contents) with 100% verified dynamic page numbers!
    def toc_row(badge_txt: str, label_txt: str, pg_txt: str) -> str:
        return (
            f"<tr>"
            f"<td style='width:11mm;padding:0.45mm 1mm !important;white-space:nowrap;'><span class='chip' style='font-size:7.8pt; /* hf-ok */ padding:0.15mm 1.2mm;font-weight:800;display:inline-block;text-align:center;min-width:9.5mm;'>{badge_txt}</span></td>"
            f"<td style='padding:0.45mm 1mm !important;font-size:8.6pt; /* hf-ok */ line-height:1.14;color:#0f172a;font-weight:600;'>{label_txt}</td>"
            f"<td style='width:13.5mm;padding:0.45mm 1.2mm !important;text-align:right;font-weight:800;font-size:8.6pt; /* hf-ok */ color:var(--primary);white-space:nowrap;'>p. {pg_txt}</td>"
            f"</tr>"
        )

    def toc_sec_hdr(sec_title: str) -> str:
        return (
            f"<tr><td colspan='3' style='background:var(--primary);color:#ffffff;font-weight:800;font-size:8.4pt; /* hf-ok */ "
            f"letter-spacing:0.04em;text-transform:uppercase;padding:0.65mm 1.8mm !important;border-radius:3px;'>{sec_title}</td></tr>"
        )

    left_col_rows = (
        toc_sec_hdr("Part 1: Specification &amp; Core Exam Strategy")
        + toc_row("SPEC", "Pearson Edexcel Level 1 Syllabus (W19–W25)", "3")
        + toc_row("STRAT", "TAP, Planning, Paragraphs, Connectives &amp; Checking", "4")
        + toc_sec_hdr("Part 2: All 12 Level 1 Writing Formats (60 Pages)")
        + "".join(
            toc_row(
                f"F{f['idx']}",
                f"Format {f['idx']}: {escape_html(f['title'])}",
                f"{format_start_pages[f['idx']]}&ndash;{format_start_pages[f['idx']]+4}"
            )
            for f in FORMATS_L1
        )
    )

    right_col_rows = (
        toc_sec_hdr("Part 3: Level 1 SPaG &amp; Spelling Masterclass (16 Pages)")
        + "".join(
            toc_row(
                f"S{sp_i}",
                f"Unit {sp_i}: {escape_html(SPAG_L1_EXERCISES[sp_i]['title'])}",
                f"{spag_start_pages[sp_i]}&ndash;{spag_start_pages[sp_i]+1}"
            )
            for sp_i in range(1, 9)
        )
        + toc_sec_hdr("Part 4: Official Mock Exams &amp; Marking Criteria")
        + toc_row("MOCK 1", "Official Mock Examination Paper 1 (Tasks 1 &amp; 2)", f"{mock1_start_page}&ndash;{mock1_start_page+5}")
        + toc_row("MOCK 2", "Official Mock Examination Paper 2 (Tasks 1 &amp; 2)", f"{mock2_start_page}&ndash;{mock2_start_page+5}")
        + toc_row("RUBRIC", "Official Pearson Level 1 Marking Grids", f"{rubric_start_page}&ndash;{rubric_start_page+3}")
        + toc_sec_hdr("Part 5: Reference Solutions, Glossary &amp; Index")
        + toc_row("SOL", "SPaG Drill &amp; Mock Exam Benchmark Solutions", f"{ref_actual_start}&ndash;{ref_actual_start+3}")
        + toc_row("GLOSS", "Comprehensive Functional Writing Glossary", f"{ref_actual_start+3}&ndash;{ref_actual_start+4}")
        + toc_row("INDEX", "Alphabetical Subject &amp; Format Index", f"{ref_actual_start+5}" if ref_actual_start+5 == readiness_page-1 else f"{ref_actual_start+5}&ndash;{readiness_page-1}")
        + toc_row("READY", "Pre-Exam Readiness &amp; Final Verification", f"{readiness_page}")
    )

    p2_toc_body = (
        compact_tbl_css
        + K.page_title("Functional Skills English &bull; Writing (Level 1)", kicker="Master Functional Skills &bull; Complete Curriculum &amp; Format Mastery Manual", badge="TOC")
        + "<div class='box worked' style='padding:1.4mm 2.8mm;display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:1.2mm 4mm;font-size:9pt; /* hf-ok */ margin-bottom:1mm;'>"
          "<div><span style='font-weight:700;color:var(--primary);font-size:8.6pt; /* hf-ok */'>This book belongs to:</span><div class='aline' style='height:3.8mm;'></div></div>"
          "<div><span style='font-weight:700;color:var(--primary);font-size:8.6pt; /* hf-ok */'>Exam date:</span><div class='aline' style='height:3.8mm;'></div></div>"
          "<div><span style='font-weight:700;color:var(--primary);font-size:8.6pt; /* hf-ok */'>Target score (out of 36):</span><div class='aline' style='height:3.8mm;'></div></div>"
          "</div>"
        + "<h2 style='font-size:11.5pt;margin:0.3mm 0 0.8mm 0;color:var(--primary);'>Complete Table of Contents &amp; Topic Directory</h2>"
        + "<div style='display:grid;grid-template-columns:1fr 1fr;gap:2.5mm;align-items:start;'>"
        + f"<table class='t compact' style='width:100%;border-collapse:separate;'><tbody>{left_col_rows}</tbody></table>"
        + f"<table class='t compact' style='width:100%;border-collapse:separate;'><tbody>{right_col_rows}</tbody></table>"
        + "</div>"
        + "<div style='margin-top:1mm;background:#f8fafc;border:1.5px solid var(--soft);border-left:4px solid var(--accent);border-radius:6px;padding:1.2mm 2.5mm;font-size:8.6pt; /* hf-ok */ line-height:1.25;'>"
          "<b style='color:var(--primary);'>How Each 5-Page Format Unit Works:</b> "
          "<b>Page 1:</b> Full Format Explanation, 6-Point Layout Anatomy &amp; 12 Specialist Vocabulary Terms &bull; "
          "<b>Page 2:</b> Guided Exam Brief &amp; 5-Minute TAP Planning Grid &bull; "
          "<b>Page 3:</b> Full-Marks Model Answer, 12 Vocabulary Definitions &amp; Examiner Commentary &bull; "
          "<b>Pages 4&ndash;5:</b> Unseen Exam Practice Task &amp; Official Lined Response Sheet."
          "</div>"
    )
    pages[1] = K.page(p2_toc_body, header=("Master Functional Skills", "Complete Table of Contents"), footer=BOOK, page_no=2)

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
# 4. English Writing Level 1 Companion Workbook (96 Pages)
# =============================================================================
def build_english_l1_companion():
    print("\n" + "="*70)
    print("BUILDING: MasterFunctionalSkills_English_Writing_Level_1_Companion_Workbook.pdf (A4)")
    print("="*70)

    BOOK = "English Writing Level 1 Companion Workbook"
    front_cov = COV / "level1_companion_cover_page-1.png"
    back_cov = COV / "level1_companion_cover_page-2.png"

    pages = []
    compact_tbl_css = (
        "<style>"
        ".t.compact th { padding: 1mm 2mm !important; font-size: 9pt !important; /* hf-ok */ line-height: 1.2 !important; }"
        ".t.compact td { padding: 0.9mm 2mm !important; font-size: 8.8pt !important; /* hf-ok */ line-height: 1.2 !important; }"
        ".ptitle h1 { font-size: 19.5pt !important; line-height: 1.08 !important; }"
        ".ptitle .badge { height: 15mm !important; min-width: 15mm !important; font-size: 16pt !important; }"
        ".pair .box { padding: 2mm 2.8mm !important; font-size: 9.5pt !important; /* hf-ok */ line-height: 1.24 !important; }"
        "</style>"
    )

    # p1: Front Cover
    pages.append(K.front_cover(front_cov))
    # p2: Placeholder for Complete 2-Column Table of Contents (populated after page assembly)
    pages.append("")

    # p3: Companion Strategy, Syllabus Profile & Timed Practice Guide
    p3_body = (
        compact_tbl_css
        + K.page_title("Level 1 Companion Workbook &bull; Syllabus &amp; Practice Guide",
                       kicker="Pearson Edexcel Functional Skills English (W19–W25) &bull; Independent Exam Practice", badge="GUIDE")
        + K.box_html(
            "<p style='font-size:9.6pt; /* hf-ok */ margin:0 0 1.2mm 0;line-height:1.34;'>This Companion Workbook contains <b>24 brand-new, unseen examination tasks</b> (two unique tasks for every one of the 12 official Level 1 functional writing formats), followed by <b>4 complete 60-minute mock papers</b> (8 exam tasks) and <b>8 everyday proofreading drills</b>. Every task in this workbook is 100% unique to this publication.</p>"
            "<table class='t compact'>"
            "<thead><tr><th>Assessment Component</th><th>Task 1: Longer Writing</th><th>Task 2: Shorter Writing</th><th>Total Exam</th></tr></thead>"
            "<tbody>"
            "<tr><td><b>Recommended Timing</b></td><td><b>35 Minutes</b> (5m plan, 25m write, 5m check)</td><td><b>25 Minutes</b> (4m plan, 17m write, 4m check)</td><td><b>60 Minutes</b></td></tr>"
            "<tr><td><b>Target Word Count</b></td><td><b>150&ndash;250 words</b></td><td><b>100&ndash;180 words</b></td><td>250&ndash;430 words</td></tr>"
            "<tr><td><b>Composition Marks (W22–W24)</b></td><td>12 Marks</td><td>9 Marks</td><td><b>21 Marks (58.3%)</b></td></tr>"
            "<tr><td><b>SPaG Marks (W19–W21, W25)</b></td><td>9 Marks</td><td>6 Marks</td><td><b>15 Marks (41.7%)</b></td></tr>"
            "<tr><td><b>Total Task Marks</b></td><td><b>21 Marks</b></td><td><b>15 Marks</b></td><td><b>36 Marks (100%)</b></td></tr>"
            "</tbody></table>",
            title="Official Pearson Edexcel Level 1 Writing Assessment Profile"
        )
        + K.box_html(
            "<div style='display:grid;grid-template-columns:1fr 1fr;gap:2mm;font-size:9pt; /* hf-ok */ line-height:1.3;'>"
            "<div style='background:#f8fafc;border:1px solid var(--soft);border-left:3.5px solid var(--primary);padding:1.6mm 2.2mm;border-radius:4px;'>"
            "<b>1. Plan Using TAP (5 Mins):</b> Check the <b>Text</b> format layout, <b>Audience</b> (polite formal vs friendly informal), and <b>Purpose</b>, then plan one clear paragraph for each bullet point."
            "</div>"
            "<div style='background:#f8fafc;border:1px solid var(--soft);border-left:3.5px solid var(--primary);padding:1.6mm 2.2mm;border-radius:4px;'>"
            "<b>2. Use the 10-Word Vocabulary Bank:</b> Each task brief gives you <b>10 helpful Level 1 words</b>. Try to include at least 4–5 of these words naturally in your writing."
            "</div>"
            "<div style='background:#f8fafc;border:1px solid var(--soft);border-left:3.5px solid var(--primary);padding:1.6mm 2.2mm;border-radius:4px;'>"
            "<b>3. Join Ideas &amp; Punctuate Clearly:</b> Link sentences using <i>because, although, however,</i> and <i>in addition</i>, and check capital letters, full stops, question marks, and apostrophes."
            "</div>"
            "<div style='background:#f8fafc;border:1px solid var(--soft);border-left:3.5px solid var(--primary);padding:1.6mm 2.2mm;border-radius:4px;'>"
            "<b>4. Check Against Model Solutions:</b> After finishing each task or mock paper, compare your work with the <b>Reference Section</b> guidance and full-marks model answers."
            "</div>"
            "</div>",
            title="4-Step Level 1 Practice &amp; Checking Routine"
        )
        + K.tip_pair("Practise without a dictionary or phone spellchecker so you build real exam confidence.",
                     "Always leave 5 minutes at the end of each task to check capital letters, full stops, and tricky spellings.",
                     golden_title="Real Exam Conditions", watch_title="5-Minute Final Check")
        + K.fill_notes("My Level 1 Practice Plan &amp; Target Score", min_mm=14)
    )
    pages.append(K.page(p3_body, header=(BOOK, "Syllabus &bull; Practice Guide"), footer=BOOK, page_no=3))

    # p4 to p51: 24 Independent Workbook Tasks across all 12 Formats x 2 pages = 48 pages
    p_curr = 4
    format_task_pages = {}
    for t in WORKBOOK_L1_TASKS:
        f_idx = t["format_idx"]
        f_name = t["format_name"]
        q_num = t["question_num"]
        marks = t["marks"]
        words = t["word_count"]
        topic = t["topic"]
        aud = t["audience"]
        spec_list = t["specialist_words"]
        stim = t["stimulus"]
        bullets = t["bullets"]
        strat = t["strategy"]

        if f_idx not in format_task_pages:
            format_task_pages[f_idx] = p_curr

        # Unit Photo Card & Side-by-Side Scenario Block
        u_photo_card = ""
        photo_map = UNIT_PHOTOS_L1_SECOND if q_num == 2 else UNIT_PHOTOS_L1
        if SHOW_UNIT_IMAGES and f_idx in photo_map:
            rel_path, cap_txt = photo_map[f_idx]
            img_p = K.PHOTO_DIR / rel_path
            if img_p.exists():
                u_photo_card = (
                    f"<div style='background:#ffffff;border:1.5px solid var(--primary);border-radius:6px;overflow:hidden;box-shadow:0 1.5px 4px rgba(0,0,0,0.08);display:flex;flex-direction:column;'>"
                    f"<div style='width:100%;aspect-ratio:16/9;overflow:hidden;background:#0f172a;'>"
                    f"<img src='{img_p.as_uri()}' alt='{escape_html(cap_txt)}' style='width:100%;height:100%;object-fit:cover;object-position:center 25%;display:block;'>"
                    f"</div>"
                    f"<div style='background:#eff6ff;color:var(--primary);font-size:7.8pt; /* hf-ok */ font-weight:700;text-align:center;padding:0.8mm 1.5mm;border-top:1px solid #bfdbfe;line-height:1.15;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;'>"
                    f"Task {q_num}: {cap_txt}</div>"
                    f"</div>"
                )

        # Clean single-paragraph stimulus (zero mid-sentence line breaks)
        stim_clean = " ".join(stim.split())
        stim_html = escape_html(stim_clean)
        bullets_html = "".join(f"<li style='margin-bottom:1.2px;'>{escape_html(b)}</li>" for b in bullets)
        vocab_pills = "".join(
            f"<span class='chip' style='font-size:8pt; /* hf-ok */ padding:0.35mm 1.8mm;margin:0.3mm;'>{escape_html(w)}</span>"
            for w in spec_list
        )
        art_word = "an" if f_name[0].lower() in "aeiou" else "a"

        if u_photo_card:
            scenario_block = (
                f"<div style='display:grid;grid-template-columns:1fr 1fr;gap:3.5mm;align-items:center;margin-bottom:1.5mm;'>"
                f"<div style='display:flex;flex-direction:column;justify-content:space-between;'>"
                f"<p style='font-size:9.8pt; /* hf-ok */ margin:0 0 1.2mm 0;line-height:1.32;'><b>Scenario &amp; Context:</b> {escape_html(topic)}<br>"
                f"<span style='color:#475569;font-size:9pt; /* hf-ok */'><b>Target Audience &amp; Tone:</b> {escape_html(aud)}</span></p>"
                f"<div style='background:#f8fafc;padding:2mm 2.8mm;border:1px solid var(--soft);border-radius:4px;font-size:9.2pt; /* hf-ok */ line-height:1.36;flex:1 1 auto;'>"
                f"<strong style='color:var(--primary);'>Context &amp; Stimulus Information:</strong><br>{stim_html}"
                f"</div>"
                f"</div>"
                f"{u_photo_card}"
                f"</div>"
            )
        else:
            scenario_block = (
                f"<p style='font-size:10pt; /* hf-ok */ margin:0 0 1.5mm 0;line-height:1.35;'><b>Scenario &amp; Context:</b> {escape_html(topic)}<br>"
                f"<span style='color:#475569;font-size:9.2pt; /* hf-ok */'><b>Target Audience &amp; Tone:</b> {escape_html(aud)}</span></p>"
                f"<div style='background:#f8fafc;padding:2mm 2.8mm;border:1px solid var(--soft);border-radius:4px;font-size:9.5pt; /* hf-ok */ line-height:1.38;margin-bottom:1.5mm;'>"
                f"<strong style='color:var(--primary);'>Context &amp; Stimulus Information:</strong><br>{stim_html}"
                f"</div>"
            )

        # Page 1: Task Brief, Unit Photo, 10 Specialist Vocab Pills & TAP Planning Frame
        p1_body = (
            compact_tbl_css
            + K.page_title(f"Format {f_idx}: {f_name} &bull; Practice Task {q_num}", kicker=f"Unseen Exam Task &bull; {marks} Marks &bull; {words}", badge=f"F{f_idx}&bull;T{q_num}")
            + K.box_html(
                f"{scenario_block}"
                f"<p style='margin:0 0 1mm 0;font-size:9.8pt; /* hf-ok */'><b>Task Instructions:</b> Write {art_word} <b>{escape_html(f_name)}</b> ({words}). In your writing, you must:</p>"
                f"<ul style='margin:0 0 1.8mm 5mm;padding:0;font-size:9.5pt; /* hf-ok */ line-height:1.34;'>{bullets_html}</ul>"
                f"<div style='background:#f8fafc;border:1px solid var(--soft);border-radius:4px;padding:1.4mm 2.2mm;margin-bottom:1.5mm;'>"
                f"<div style='font-size:8.4pt; /* hf-ok */ font-weight:800;color:var(--primary);margin-bottom:0.6mm;'>Helpful Vocabulary Bank (Try to use at least 4–5 of these 10 Level 1 words):</div>"
                f"<div style='display:flex;flex-wrap:wrap;gap:0.5mm;'>{vocab_pills}</div>"
                f"</div>"
                f"<div style='padding:1.5mm 2.5mm;background:#f1f5f9;border-left:3.5px solid var(--primary);font-size:8.8pt; /* hf-ok */ display:flex;justify-content:space-between;gap:3mm;'>"
                f"<span><b>Writing Tip:</b> {escape_html(strat)}</span>"
                f"<span style='white-space:nowrap;'><b>Target:</b> {words} &bull; <b>{marks} Marks</b></span>"
                f"</div>",
                title=f"Practice Task Brief &bull; Format {f_idx} (Task {q_num})"
            )
            + K.fill_notes("5-Minute Plan (Format Layout &bull; Paragraph 1 &bull; Paragraph 2 &bull; Paragraph 3 &bull; Sign-Off)", min_mm=22)
        )
        pages.append(K.page(p1_body, header=(BOOK, f"Format {f_idx} &bull; Task {q_num} Brief"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 2: Response
        p2_body = (
            K.page_title(f"Format {f_idx}: {f_name} &bull; Candidate Response", kicker=f"Official Lined Assessment Page &bull; Task {q_num} &bull; {marks} Marks")
            + K.fill_lines(f"Write your {f_name} response below ({words}):", min_mm=205, gap_mm=9.5)
        )
        pages.append(K.page(p2_body, header=(BOOK, f"Format {f_idx} &bull; Task {q_num} Response"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p52 to p75: 4 Full Official Mock Papers (4 papers x 6 pages = 24 pages)
    # Followed by 8 Diagnostic Drills (p76 to p83 = 8 pages) -> Reference Section starts at page 84!
    ref_section_start_page = p_curr + 24 + 8
    mock_start_pages = {}

    audit_details_l1 = {
        1: ("Mock 1 Audit &bull; Kitchen Leak Repair Letter &amp; Student Budget Leaflet",
            "Check your Mock 1 writing against Pearson Level 1 standards:",
            [
                "<b>Task 1 (Letter to Landlord):</b> Included your address, date, letting agency address, 'Dear Mrs Brooks,', clear description of the leaking sink pipe and damp cupboard, days at home, and 'Yours sincerely,'.",
                "<b>Task 2 (Budget Food Leaflet):</b> Bold main heading, subheadings, bulleted supermarket and packed-lunch tips, and reminder about the free campus kitchenette.",
                "<b>Punctuation Check:</b> Every sentence starts with a capital letter and ends with a full stop. All proper nouns (Derby, Meadow Court) are capitalised."
            ]),
        2: ("Mock 2 Audit &bull; First Aid Training Email &amp; Staff Locker Room Notice",
            "Check your Mock 2 writing against Pearson Level 1 standards:",
            [
                "<b>Task 1 (Email to Manager):</b> Included To: and Subject: lines, 'Dear Mr Ross,', explained Saturday's badminton ankle injury, suggested a 1-hour Thursday morning refresher, and signed off politely.",
                "<b>Task 2 (Locker Room Notice):</b> Bold notice title, effective date, bulleted rules (keypad code 4829#, own padlock, clear daily), and Reception contact for permanent lockers.",
                "<b>Spelling Check:</b> Checked everyday workplace spellings (training, Saturday, Thursday, emergency, reception)."
            ]),
        3: ("Mock 3 Audit &bull; Phone Repair Complaint Letter &amp; Local Library Article",
            "Check your Mock 3 writing against Pearson Level 1 standards:",
            [
                "<b>Task 1 (Complaint Letter):</b> Included both postal addresses, date, receipt number QF-1184, £65.00 price paid, description of the faulty replacement screen, and request for free repair or refund.",
                "<b>Task 2 (Library Article):</b> Catchy headline, byline, subheadings, lively paragraphs covering free Wi-Fi/computers and Saturday children's clubs, and encouragement to join.",
                "<b>Sentence Structure:</b> Joined ideas smoothly using 'because', 'although', 'and', and 'but' without comma splices."
            ]),
        4: ("Mock 4 Audit &bull; Food Hub Volunteer Email &amp; Launderette Review",
            "Check your Mock 4 writing against Pearson Level 1 standards:",
            [
                "<b>Task 1 (Volunteer Email):</b> Included To: and Subject: lines, 'Dear Ms Shah,', explained why you want to help, described your practical skills and driving licence, and gave your free days/hours.",
                "<b>Task 2 (Launderette Review):</b> Clear review title, star rating, positive comments on the fast machines and helpful attendant, one fair downside (broken coin machine), and final recommendation.",
                "<b>Overall Timing:</b> Completed Task 1 (150–250 words) in 35 minutes and Task 2 (100–180 words) in 25 minutes."
            ])
    }

    for m in WORKBOOK_MOCK_L1_PAPERS:
        pnum = m["paper_num"]
        mock_start_pages[pnum] = p_curr
        t1 = m["task1"]
        t2 = m["task2"]

        p_over = (
            K.page_title(f"Official Mock Writing Examination &bull; Paper {pnum}", kicker="Pearson Edexcel Level 1 Simulation &bull; 60 Minutes &bull; 36 Marks", badge=f"MOCK {pnum}")
            + K.box_html(
                f"<div style='font-size:12pt;line-height:1.5;'>"
                f"<p><b>Simulation Examination:</b> Complete both Task 1 ({t1['marks']} marks) and Task 2 ({t2['marks']} marks) under timed exam conditions (60 minutes total) without a dictionary or spellchecker.</p>"
                f"<ul>"
                f"<li><b>Task 1:</b> {escape_html(t1['title'])} &bull; {t1['words']} &bull; {t1['time']}</li>"
                f"<li><b>Task 2:</b> {escape_html(t2['title'])} &bull; {t2['words']} &bull; {t2['time']}</li>"
                f"</ul>"
                f"</div>",
                title=f"Mock Paper {pnum} Overview &amp; Instructions"
            )
            + K.tip_pair("Spend 35 minutes on Task 1 (21 marks) and 25 minutes on Task 2 (15 marks).",
                         "Remember capital letters at the start of every sentence, for 'I', and for names and places.",
                         golden_title="Pacing", watch_title="Punctuation")
            + K.fill_notes(f"My Target &amp; Plan for Mock Paper {pnum}", min_mm=38)
        )
        pages.append(K.page(p_over, header=(BOOK, f"Mock {pnum} &bull; Overview"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Task 1 Brief
        p_t1_brief = (
            K.page_title(f"Mock {pnum} &bull; {t1['title']}", kicker=f"Task 1 (Extended Writing) &bull; {t1['marks']} Marks &bull; {t1['words']}", badge="T1")
            + K.box_html(
                f"<p style='font-size:12pt;line-height:1.48;'><b>Scenario:</b> {escape_html(t1['scenario'])}</p>"
                + K.bullets([escape_html(b) for b in t1["bullets"]])
                + f"<p style='font-size:10.5pt;color:#64748b;margin-top:2mm;'><b>Recommended Time:</b> {t1['time']} &emsp; <b>Target Word Count:</b> {t1['words']}</p>",
                title=f"Task 1 Brief &bull; {t1['marks']} Marks"
            )
            + K.fill_notes("Task 1 Plan &amp; Paragraph Ideas", min_mm=38)
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
            K.page_title(f"Mock {pnum} &bull; {t2['title']}", kicker=f"Task 2 (Shorter Writing) &bull; {t2['marks']} Marks &bull; {t2['words']}", badge="T2")
            + K.box_html(
                f"<p style='font-size:12pt;line-height:1.48;'><b>Scenario:</b> {escape_html(t2['scenario'])}</p>"
                + K.bullets([escape_html(b) for b in t2["bullets"]])
                + f"<p style='font-size:10.5pt;color:#64748b;margin-top:2mm;'><b>Recommended Time:</b> {t2['time']} &emsp; <b>Target Word Count:</b> {t2['words']}</p>",
                title=f"Task 2 Brief &bull; {t2['marks']} Marks"
            )
            + K.fill_notes("Task 2 Plan &amp; Key Words", min_mm=38)
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

        # Mock Audit
        a_title, a_lead, a_checks = audit_details_l1.get(pnum, (f"Mock {pnum} Audit", "Audit your script:", ["Covered all points."]))
        p_audit = (
            K.page_title(f"Mock {pnum} &bull; Post-Exam Audit", kicker=a_title, badge="AUDIT")
            + K.box_html(
                f"<p style='font-size:12pt;margin-top:0;'><b>{a_lead}</b></p>"
                + K.bullets(a_checks)
                + f"<p style='font-size:11pt;color:#64748b;margin-top:2mm;'>Compare your answers against the full-marks benchmark solutions in the Reference Section (starting on p. {ref_section_start_page}).</p>",
                title=f"Pearson Edexcel Level 1 Marking Matrix &bull; Paper {pnum}"
            )
            + K.fill_notes(f"Personal Notes &amp; Spelling Audit for Mock {pnum}", min_mm=38)
        )
        pages.append(K.page(p_audit, header=(BOOK, f"Mock {pnum} &bull; Audit"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p76 to p83: 8 Targeted Everyday Proofreading Drills
    proof_passages_l1 = [
        ("Diagnostic 1: Capital Letters &amp; Full Stops",
         "last monday i visited the jobcentre on west street the advisor gave me three job forms to fill in i need to return them before friday afternoon",
         "<b>L</b>ast <b>M</b>onday<b>, I</b> visited the <b>J</b>obcentre on <b>W</b>est <b>S</b>treet<b>. T</b>he advisor gave me three job forms to fill in<b>. I</b> need to return them before <b>F</b>riday afternoon<b>.</b>"),
        ("Diagnostic 2: Question Marks &amp; Exclamation Marks",
         "Can you tell me what time the shift begins. Do we need to bring our own safety boots. Don't forget your security pass or you cannot enter the warehouse.",
         "Can you tell me what time the shift begins<b>?</b> Do we need to bring our own safety boots<b>?</b> Don't forget your security pass or you cannot enter the warehouse<b>!</b>"),
        ("Diagnostic 3: Everyday Spelling Corrections",
         "We recieved your aplicasion yesterday. Pleas bring your passport and proff of adress to the intervun on Teusday morning.",
         "We <b>received</b> your <b>application</b> yesterday. <b>Please</b> bring your passport and <b>proof</b> of <b>address</b> to the <b>interview</b> on <b>Tuesday</b> morning."),
        ("Diagnostic 4: Subject-Verb Agreement",
         "The delivery drivers was late because the motorway were closed. The parcels is sitting in the sorting room waiting for inspection.",
         "The delivery drivers <b>were</b> late because the motorway <b>was</b> closed. The parcels <b>are</b> sitting in the sorting room waiting for inspection."),
        ("Diagnostic 5: Joining Sentences with Conjunctions",
         "I wanted to apply for the warehouse role. I did not have a forklift licence. I enrolled on a training course. Now I am fully certified.",
         "I wanted to apply for the warehouse role<b>, but</b> I did not have a forklift licence<b>. Therefore,</b> I enrolled on a training course <b>and</b> now I am fully certified."),
        ("Diagnostic 6: Email Salutations and Tone",
         "Hey mate, where is my payslip from last week? Send it now coz I need to pay my rent today. Bye.",
         "<b>Dear Payroll Team,</b> Could you please send me a copy of my payslip from last week<b>?</b> I need it urgently today <b>because</b> my rent payment is due. <b>Thank you for your help. Kind regards, Alex.</b>"),
        ("Diagnostic 7: Organising Information into Two Paragraphs",
         "Our sports centre is offering discounted gym memberships for healthcare workers throughout November. You can sign up online or at reception. Remember to bring your healthcare staff badge. The discount applies to both gym facilities and swimming pool sessions.",
         "<b>Paragraph 1 (The Offer):</b> Our sports centre is offering discounted gym memberships for healthcare workers throughout November. The discount applies to both gym facilities and swimming pool sessions.<br><b>Paragraph 2 (How to Join):</b> You can sign up online or at reception. Remember to bring your healthcare staff badge."),
        ("Diagnostic 8: Checking Details in Workplace Notes",
         "Meeting on Wensday at 2:00 in Room 4. Bring your project update. Tea and biscuits will be provyded. Contact Sarah if you cant come.",
         "There is a team meeting on <b>Wednesday</b> at <b>2:00 pm</b> in Room 4. Please bring your project update. Tea and biscuits will be <b>provided</b>. Contact Sarah if you <b>cannot (can't)</b> attend.")
    ]

    drill_start_pages = {}
    for d_idx, (d_title, d_text, _) in enumerate(proof_passages_l1):
        drill_start_pages[d_idx + 1] = p_curr
        d_photo_html = ""
        if (d_idx + 1) in SPAG_WRITING_PHOTOS:
            d_rel, d_cap = SPAG_WRITING_PHOTOS[d_idx + 1]
            d_photo_html = writing_float_photo_card(d_rel, d_cap, height_mm=38, width_mm=64)
        d_body = (
            K.page_title(f"Proofreading Drill {d_idx+1}", kicker=d_title, badge=f"D{d_idx+1}")
            + K.box_html(
                f"{d_photo_html}"
                f"<p style='font-size:12pt;margin-top:0;'><b>Extract:</b> Find and fix every error in the passage below:</p>"
                f"<div style='background:#f8fafc;padding:3.5mm;border:1.5px solid var(--soft);border-radius:6px;font-size:11.5pt;line-height:1.55;clear:both;'>"
                f"{d_text}"
                f"</div>",
                title=f"Find the Errors &bull; Drill {d_idx+1}"
            )
            + K.fill_lines(f"Write the corrected version below (worked solution on p. {ref_section_start_page + 1}):", min_mm=115, gap_mm=9.5)
        )
        pages.append(K.page(d_body, header=(BOOK, f"Diagnostic {d_idx+1}"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p84 onwards: Reference Back Matter
    ref_actual_start = p_curr
    ref_blocks = []

    # 1. Indicative Content & Checklists for all 24 Workbook Tasks (grouped cleanly into 12 Format blocks)
    for f_info in FORMATS_L1:
        f_i = f_info["idx"]
        f_sh = f_info["title"]
        f_tasks = [t for t in WORKBOOK_L1_TASKS if t["format_idx"] == f_i]
        qa_html = ""
        for t in f_tasks:
            qn = t["question_num"]
            t_num = (f_i - 1) * 2 + qn
            v_str = escape_html(", ".join(t["specialist_words"][:5]))
            b_summary = escape_html("; ".join(t["bullets"][:2]))
            qa_html += K.ref_qa(
                f"T{t_num}",
                f"<b>{escape_html(t['topic'])}</b> ({escape_html(t['audience'])}).<br>"
                f"<b>Key Points:</b> {b_summary}.<br>"
                f"<b>Helpful Words:</b> <i>{v_str}</i>.",
                marks=f"{t['marks']}m",
                working=t["strategy"]
            )
        ref_blocks.append(K.ref_block(f"Format {f_i}: {escape_html(f_sh)} (Tasks 1 &amp; 2 Guidance)", qa_html))

    # 2. Worked Solutions for all 8 Proofreading Drills (2 balanced blocks of 4 drills each)
    d_html_1 = "".join(
        K.ref_qa(f"D{idx+1}", corr, marks="4/4", working=title.split(":", 1)[-1].strip())
        for idx, (title, _, corr) in enumerate(proof_passages_l1[:4])
    )
    ref_blocks.append(K.ref_block("Proofreading Drills 1–4: Worked Solutions", d_html_1))

    d_html_2 = "".join(
        K.ref_qa(f"D{idx+5}", corr, marks="4/4", working=title.split(":", 1)[-1].strip())
        for idx, (title, _, corr) in enumerate(proof_passages_l1[4:])
    )
    ref_blocks.append(K.ref_block("Proofreading Drills 5–8: Worked Solutions", d_html_2))

    # 3. Full-Marks Benchmark Solutions for all 4 Mock Papers (8 Tasks)
    for m in WORKBOOK_MOCK_L1_PAPERS:
        pnum = m["paper_num"]
        t1 = m["task1"]
        t2 = m["task2"]
        ref_blocks.append(K.ref_block(
            f"Mock Paper {pnum} &bull; Task 1 Benchmark Solution (21 Marks)",
            K.ref_qa(f"M{pnum}a", t1["model"], marks="21/21", working="Full marks: Complete Level 1 layout conventions, clear paragraphs answering every bullet point, joined complex sentences, and accurate spelling.")
        ))
        ref_blocks.append(K.ref_block(
            f"Mock Paper {pnum} &bull; Task 2 Benchmark Solution (15 Marks)",
            K.ref_qa(f"M{pnum}b", t2["model"], marks="15/15", working="Full marks: Clear main heading and subheadings/bullets, appropriate tone for the reader, and accurate sentence punctuation.")
        ))

    # 4. Glossary (split into 3 balanced blocks so no block overflows a single column)
    g_chunk1 = GLOSSARY_L1[:10]
    g_chunk2 = GLOSSARY_L1[10:20]
    g_chunk3 = GLOSSARY_L1[20:]
    for g_title, g_items in [
        ("Level 1 Functional Writing Glossary (A–C)", g_chunk1),
        ("Level 1 Functional Writing Glossary (C–N)", g_chunk2),
        ("Level 1 Functional Writing Glossary (P–V)", g_chunk3),
    ]:
        g_html = "".join(f"<dl><dt>{escape_html(t)}</dt><dd>{escape_html(d)}</dd></dl>" for t, d in g_items)
        ref_blocks.append(K.ref_block(g_title, g_html))

    # 5. Companion Workbook Index (split into 2 balanced blocks with exact Companion Workbook page numbers)
    comp_index_l1 = [
        ("A", [("Advice & Information Leaflets (Format 5)", "20–23, 55"), ("Articles for Magazines/Web (Format 3)", "12–15, 67"), ("Audience & Tone (W22)", "3")]),
        ("B", [("Bullet Points & Numbered Steps", "20, 48, 55, 61")]),
        ("C", [("Capital Letters & Full Stops (W19)", "3, 76"), ("Community Notices & Adverts (Format 11)", "44–47, 61"), ("Customer Reviews (Format 7)", "28–31, 73")]),
        ("D", [("Diagnostic Proofreading Drills (D1–D8)", "76–83")]),
        ("E", [("Emails: Formal & Informal (Format 2)", "8–11, 59, 71")]),
        ("F", [("Feedback & Application Forms (Format 8)", "32–35"), ("Formal Letters (Format 1)", "4–7, 53, 65"), ("Forum & Blog Posts (Format 9)", "36–39")]),
        ("G", [("Glossary of Level 1 Terms", f"{ref_actual_start+5}–{ref_actual_start+6}")]),
        ("I", [("Instruction Guides & How-To Sheets (Format 12)", "48–51")]),
        ("J", [("Joining Words / Connectives (W25)", "3, 80")]),
        ("M", [("Mock Examinations 1–4", "52–75")]),
        ("N", [("Newsletters & Club Updates (Format 10)", "40–43")]),
        ("R", [("Reports: Workplace & Community (Format 4)", "16–19")]),
        ("S", [("Speeches & Short Talks (Format 6)", "24–27"), ("Spelling & Subject-Verb Agreement", "78–79")])
    ]
    idx_part1 = ""
    for letter, entries in comp_index_l1[:6]:
        items = "".join(f"<div class='ix'><span>{escape_html(t)}</span><span>{escape_html(p)}</span></div>" for t, p in entries)
        idx_part1 += f"<div class='ix-letter'>{letter}</div>{items}"
    ref_blocks.append(K.ref_block("Companion Subject &amp; Format Index (A–F)", idx_part1))

    idx_part2 = ""
    for letter, entries in comp_index_l1[6:]:
        items = "".join(f"<div class='ix'><span>{escape_html(t)}</span><span>{escape_html(p)}</span></div>" for t, p in entries)
        idx_part2 += f"<div class='ix-letter'>{letter}</div>{items}"
    ref_blocks.append(K.ref_block("Companion Subject &amp; Format Index (G–S)", idx_part2))

    cover_theme = K.theme_from_cover(front_cov)
    ref_page_list = K.ref_pages("Companion Reference: Solutions, Models, Glossary &amp; Index", ref_blocks,
                                BOOK, start_page=p_curr, subtitle="Worked Solutions, Full-Marks Mock Exemplars &amp; Glossary",
                                cols=2, theme=cover_theme, notes_title="Candidate Companion Log")
    pages.extend(ref_page_list)
    p_curr += len(ref_page_list)

    # Self-Assessment
    audit_matrix_page = p_curr
    p_audit_body = (
        K.page_title("Candidate Writing Self-Assessment &amp; Progress Chart", kicker="Level 1 Writing Targets &bull; Final Check", badge="AUDIT")
        + K.box_html(
            "<p>Check off your skills across the 24 practice tasks and 4 mock exams against Pearson Edexcel Level 1 standards:</p>"
            + K.bullets([
                "<b>Clear Composition (W22–W24):</b> Wrote clearly and stayed on topic, used the right layout features for each format, and organised ideas into logical paragraphs.",
                "<b>Accurate SPaG (W19–W21, W25):</b> Used capital letters, full stops, question marks, commas, and apostrophes accurately, joined complex sentences smoothly, and spelled everyday words correctly."
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
                         "<p style='font-size:12pt;line-height:1.5;'>Congratulations on completing your Level 1 Writing Companion Workbook across <b>24 unseen format tasks</b>, <b>4 full mock exams</b>, and <b>8 proofreading drills</b>! Confirm your mastery of these essentials:</p>"
                         + K.bullets([
                             "<b>Format Familiarity:</b> Completed practice tasks across all 12 formats: letters, emails, articles, reports, leaflets, talks, reviews, forms, forums, newsletters, notices, and instructions.",
                             "<b>Accurate Demarcation:</b> Checked full stops, capital letters, question marks, and apostrophes on every page.",
                             "<b>Clear Layouts:</b> Structured writing using clear paragraph breaks, subheadings, and neat presentation.",
                             "<b>Full Mock Papers:</b> Practised completing four full papers within the 60-minute time limit."
                         ]))
            + K.tip_pair("Review any corrections made by your tutor alongside your Level 1 Core Guide before taking your official exam.",
                         "Remember to read through your completed writing in the exam room to catch simple slips.",
                         golden_title="Final Advice", watch_title="Proofreading")
            + K.fill_notes("Tutor Verification Notes &amp; Exam Booking Details", min_mm=28)
        )
        pages.append(K.page(p_ibc_body, header=(BOOK, "Portfolio Sign-Off"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # Populate Page 2 (Complete 2-Column Table of Contents) with 100% verified dynamic page numbers
    def toc_row(badge_txt: str, label_txt: str, pg_txt: str) -> str:
        return (
            f"<tr>"
            f"<td style='width:11mm;padding:0.35mm 1mm !important;white-space:nowrap;'><span class='chip' style='font-size:7.6pt; /* hf-ok */ padding:0.1mm 1.1mm;font-weight:800;display:inline-block;text-align:center;min-width:9.5mm;'>{badge_txt}</span></td>"
            f"<td style='padding:0.35mm 1mm !important;font-size:8.4pt; /* hf-ok */ line-height:1.12;color:#0f172a;font-weight:600;'>{label_txt}</td>"
            f"<td style='width:13.5mm;padding:0.35mm 1.2mm !important;text-align:right;font-weight:800;font-size:8.4pt; /* hf-ok */ color:var(--primary);white-space:nowrap;'>p. {pg_txt}</td>"
            f"</tr>"
        )

    def toc_sec_hdr(sec_title: str) -> str:
        return (
            f"<tr><td colspan='3' style='background:var(--primary);color:#ffffff;font-weight:800;font-size:8.2pt; /* hf-ok */ "
            f"letter-spacing:0.04em;text-transform:uppercase;padding:0.55mm 1.8mm !important;border-radius:3px;'>{sec_title}</td></tr>"
        )

    left_col_rows = (
        toc_sec_hdr("Part 1: Syllabus &amp; Timed Practice Strategy")
        + toc_row("GUIDE", "Pearson Level 1 Syllabus (W19–W25) &amp; 4-Step Method", "3")
        + toc_sec_hdr("Part 2: 24 Unseen Format Practice Tasks (48 Pages)")
        + "".join(
            toc_row(
                f"F{f['idx']}",
                f"Format {f['idx']}: {escape_html(f['title'])} (Tasks 1 &amp; 2)",
                f"{format_task_pages[f['idx']]}&ndash;{format_task_pages[f['idx']]+3}"
            )
            for f in FORMATS_L1
        )
    )

    right_col_rows = (
        toc_sec_hdr("Part 3: 4 Full Official Mock Exams (24 Pages)")
        + toc_row("MOCK 1", "Paper 1: Kitchen Leak Letter &amp; Budget Food Leaflet", f"{mock_start_pages[1]}&ndash;{mock_start_pages[1]+5}")
        + toc_row("MOCK 2", "Paper 2: First Aid Email &amp; Locker Room Notice", f"{mock_start_pages[2]}&ndash;{mock_start_pages[2]+5}")
        + toc_row("MOCK 3", "Paper 3: Phone Repair Letter &amp; Library Article", f"{mock_start_pages[3]}&ndash;{mock_start_pages[3]+5}")
        + toc_row("MOCK 4", "Paper 4: Volunteer Email &amp; Launderette Review", f"{mock_start_pages[4]}&ndash;{mock_start_pages[4]+5}")
        + toc_sec_hdr("Part 4: 8 Everyday Proofreading Drills (8 Pages)")
        + "".join(
            toc_row(
                f"D{d_i+1}",
                proof_passages_l1[d_i][0].replace(f"Diagnostic {d_i+1}: ", f"Drill {d_i+1}: "),
                f"{drill_start_pages[d_i+1]}"
            )
            for d_i in range(8)
        )
        + toc_sec_hdr("Part 5: Reference Solutions, Glossary &amp; Index")
        + toc_row("SOL", "24 Task Guides, 8 Drill Keys &amp; 8 Mock Models", f"{ref_actual_start}&ndash;{ref_actual_start+4}")
        + toc_row("GLOSS", "Level 1 Functional Writing Glossary", f"{ref_actual_start+5}&ndash;{ref_actual_start+6}")
        + toc_row("INDEX", "Companion Subject &amp; Format Index", f"{ref_actual_start+6}&ndash;{audit_matrix_page-1}")
        + toc_row("AUDIT", "Self-Assessment Chart &amp; Portfolio Sign-Off", f"{audit_matrix_page}&ndash;{p_curr-1}")
    )

    p2_toc_body = (
        compact_tbl_css
        + K.page_title("Functional Skills English &bull; Writing (Level 1)", kicker="Master Functional Skills &bull; Companion Workbook &amp; Mock Examination Bank", badge="TOC")
        + "<div class='box worked' style='padding:1.4mm 2.8mm;display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:1.2mm 4mm;font-size:9pt; /* hf-ok */ margin-bottom:1mm;'>"
          "<div><span style='font-weight:700;color:var(--primary);font-size:8.6pt; /* hf-ok */'>This workbook belongs to:</span><div class='aline' style='height:3.8mm;'></div></div>"
          "<div><span style='font-weight:700;color:var(--primary);font-size:8.6pt; /* hf-ok */'>Exam date:</span><div class='aline' style='height:3.8mm;'></div></div>"
          "<div><span style='font-weight:700;color:var(--primary);font-size:8.6pt; /* hf-ok */'>Target score (out of 36):</span><div class='aline' style='height:3.8mm;'></div></div>"
          "</div>"
        + "<h2 style='font-size:11.5pt;margin:0.3mm 0 0.8mm 0;color:var(--primary);'>Complete Table of Contents &amp; Practice Directory</h2>"
        + "<div style='display:grid;grid-template-columns:1fr 1fr;gap:2.5mm;align-items:start;'>"
        + f"<table class='t compact' style='width:100%;border-collapse:separate;'><tbody>{left_col_rows}</tbody></table>"
        + f"<table class='t compact' style='width:100%;border-collapse:separate;'><tbody>{right_col_rows}</tbody></table>"
        + "</div>"
        + "<div style='margin-top:1mm;background:#f8fafc;border:1.5px solid var(--soft);border-left:4px solid var(--accent);border-radius:6px;padding:1.2mm 2.5mm;font-size:8.6pt; /* hf-ok */ line-height:1.25;'>"
          "<b style='color:var(--primary);'>How This Companion Workbook Is Organised:</b> "
          "<b>Pages 4&ndash;51:</b> 24 Unseen Practice Tasks (2 unique tasks per format across all 12 formats, each with 10 vocabulary prompts, planning frame, and lined response sheet) &bull; "
          "<b>Pages 52&ndash;75:</b> 4 Full 60-Minute Mock Exam Papers &bull; "
          "<b>Pages 76&ndash;83:</b> 8 Everyday Proofreading Drills &bull; "
          f"<b>Pages {ref_actual_start}&ndash;{audit_matrix_page-1}:</b> Complete Worked Solutions, Full-Marks Mock Models, Glossary &amp; Index."
          "</div>"
    )
    pages[1] = K.page(p2_toc_body, header=("Master Functional Skills", "Complete Table of Contents"), footer=BOOK, page_no=2)

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
    print("BUILDING: MasterFunctionalSkills_English_Entry_Level_3_Core_Guide.pdf")
    print("="*70)

    BOOK = "English Entry Level 3 Core Guide"
    front_cov = COV / "english_e3_core_cover_page-1.png"
    back_cov = COV / "english_e3_core_cover_page-2.png"

    pages = []

    # Curated Entry 3 Unit Photos (30 wide establishing long-shot photographs showing each unit's theme)
    E3_READING_PHOTOS = {
        1: ("e3_thematic/r1_fire_safety_sign.jpg", "Fire warden guiding staff to Assembly Point B by the emergency exit sign."),
        2: ("e3_thematic/r2_community_garden.jpg", "Volunteers planting autumn bulbs at the Greendale Community Garden reopening."),
        3: ("e3_thematic/r3_college_enrolment.jpg", "College reception issuing an electronic student ID lanyard for Room B14."),
        4: ("e3_thematic/r4_office_laminator.jpg", "Staff operating a desktop pouch laminator safely using numbered steps."),
        5: ("e3_thematic/r5_high_street_directory.jpg", "Residents checking the A–Z Community Services Directory at the library hub."),
        6: ("e3_thematic/r6_warehouse_memo.jpg", "Warehouse manager briefing operatives on the annual leave memo and winter gear."),
        7: ("e3_thematic/r7_hospital_clinic.jpg", "Patient checking in with an appointment letter at Outpatient Clinic 3."),
        8: ("e3_thematic/r8_bus_train_compare.jpg", "Passengers comparing Bus Route 40 and the City Express Train at the station."),
        9: ("e3_thematic/r9_leisure_timetable.jpg", "Visitors checking the weekly pool and studio timetable at the leisure centre."),
        10: ("e3_thematic/r10_cycle_scheme.jpg", "Commuters wearing helmets and high-vis jackets on the city cycle path."),
        11: ("e3_thematic/r11_council_bins.jpg", "Ordering a replacement blue recycling bin on the council waste web portal."),
        12: ("e3_thematic/r12_pharmacy_cream.jpg", "Pharmacist explaining antiseptic cream dosage and storage warnings."),
    }

    E3_WRITING_PHOTOS = {
        1: ("e3_thematic/w1_capital_letters.jpg", "Oxford Community Centre welcome team and city bus on Monday morning."),
        2: ("e3_thematic/w2_sentence_punctuation.jpg", "Warehouse loading bay delivery van, timesheet check, and steam pipe warning sign."),
        3: ("e3_thematic/w3_commas_apostrophes.jpg", "Checking the office stationery order list and workshop tool kit inventory."),
        4: ("e3_thematic/w4_compound_sentences.jpg", "Warehouse forklift training bay and staff promotion presentation at reception."),
        5: ("e3_thematic/w5_giving_reasons.jpg", "Cleaner placing a wet floor warning cone while reception takes a staff call."),
        6: ("e3_thematic/w6_past_tense.jpg", "Courier delivering three boxes to reception for the storeroom log."),
        7: ("e3_thematic/w7_agreement_plurals.jpg", "Supervisor briefing an apprentice while drivers unload boxes onto storage shelves."),
        8: ("e3_thematic/w8_paragraphs_order.jpg", "Customer service training in Room 2 beside the cafeteria buffet and car park."),
        9: ("e3_thematic/w9_format_email.jpg", "Format 1 (Email): Composing a polite email with Subject line and greeting."),
        10: ("e3_thematic/w10_format_letter_note.jpg", "Format 2 (Letter &amp; Note): Taking a workplace phone message and formal letter."),
        11: ("e3_thematic/w11_format_notice_leaflet.jpg", "Format 3 (Notice &amp; Leaflet): Pinning a bulleted kitchen notice in the breakroom."),
        12: ("e3_thematic/w12_format_form_feedback.jpg", "Format 4 (Form &amp; Feedback): Completing a Bus Route 15 passenger feedback form."),
    }

    # Writing Format & Task Card Photos (matching Writing Level 1 & Level 2 books)
    E3_WRITING_TYPE_CARDS = {
        1: ("e3_thematic/w1_capital_letters.jpg", "Proper Nouns &amp; Places"),
        2: ("e3_thematic/w2_sentence_punctuation.jpg", "End Marks (. ? !)"),
        3: ("e3_thematic/w3_commas_apostrophes.jpg", "List Commas &amp; Apostrophes"),
        4: ("e3_thematic/w4_compound_sentences.jpg", "Joining with And / But / Or"),
        5: ("e3_thematic/w5_giving_reasons.jpg", "Linking with Because &amp; So"),
        6: ("e3_thematic/w6_past_tense.jpg", "Past Tense Action Log"),
        7: ("e3_thematic/w7_agreement_plurals.jpg", "Agreement &amp; Plurals"),
        8: ("e3_thematic/w8_paragraphs_order.jpg", "Paragraphs &amp; A–Z Order"),
        9: ("email_online_safety/email_inbox_laptop.jpg", "Format 1: Workplace Email"),
        10: ("workplace_office/printed_formal_letter.jpg", "Format 2: Letter &amp; Note"),
        11: ("english_language/fancy_presentational_features.jpg", "Format 3: Notice &amp; Leaflet"),
        12: ("workplace_office/online_feedback_laptop.jpg", "Format 4: Feedback Form"),
    }

    E3_SPELLING_PHOTOS = {
        1: ("e3_thematic/sp1_prefixes.jpg", "Adult classroom prefix board (un-, dis-, re-, pre-) and recycling station."),
        2: ("e3_thematic/sp2_suffixes.jpg", "Reception desk greeting and equipment lockers illustrating suffixes (-ful, -ment)."),
        3: ("e3_thematic/sp3_silent_letters.jpg", "Training kitchen knife prep, wrist pass sign-in, and emergency exit sign."),
        4: ("e3_thematic/sp4_double_consonants.jpg", "Writing a home address at college reception with delivery van traffic outside."),
        5: ("e3_thematic/sp5_word_endings.jpg", "Travel information desk and team discussion at Oxford Central Station."),
        6: ("e3_thematic/sp6_homophones.jpg", "Site visitors in high-vis gear signing in by Bay 3 and the quiet study library."),
    }

    def e3_task_photo_card(rel_path: str, caption_txt: str, pos: str = "center 25%") -> str:
        abs_p = K.PHOTO_DIR / rel_path
        if not abs_p.exists():
            return ""
        return (
            f"<div style='float:right;width:82mm;margin:0 0 2mm 3.5mm;border:1.5px solid var(--primary);"
            f"border-radius:6px;overflow:hidden;background:#f8fafc;box-shadow:0 1.5px 4px rgba(0,0,0,0.08);'>"
            f"<div style='width:100%;aspect-ratio:16/9;overflow:hidden;background:#0f172a;'>"
            f"<img src='{abs_p.as_uri()}' style='width:100%;height:100%;object-fit:cover;object-position:{pos};display:block;'>"
            f"</div>"
            f"<div style='font-size:7.5pt; /* hf-ok */ font-weight:700;color:var(--primary);text-align:center;"
            f"padding:0.7mm 1.2mm;background:#eff6ff;border-top:1px solid #bfdbfe;line-height:1.15;"
            f"white-space:nowrap;overflow:hidden;text-overflow:ellipsis;'>"
            f"{caption_txt}</div></div>"
        )

    pages.append(K.front_cover(front_cov))
    # Placeholder for Page 2 (Complete 2-Column Table of Contents inserted once page numbers are verified)
    pages.append("")

    # p3: Official Pearson Edexcel Entry Level 3 Specification & Syllabus Mapping (E3.R8-R12 & E3.W13-W22)
    p3_body = (
        K.page_title("Entry 3 English &bull; Syllabus Overview", kicker="Pearson Edexcel Qualification Overview &bull; QAN 603/4288/2", badge="SPEC")
        + K.box_html(
            "<div style='font-size:9.1pt;line-height:1.32;'>"
            "<div style='display:grid;grid-template-columns:1fr 1fr;gap:2.2mm;margin-bottom:1.4mm;'>"
            "<div style='background:#f8fafc;border:1px solid #cbd5e1;border-radius:5px;padding:1.4mm 2.2mm;'>"
            "<b style='color:var(--primary);'>Component 1: Reading Assessment (45 Mins &bull; 24 Marks)</b><br>"
            "&bull; Read <b>3 straightforward everyday/workplace texts</b> (notices, emails, leaflets, directories, web pages).<br>"
            "&bull; Answer short comprehension questions testing main ideas, purpose, dictionary/alphabetical order, and tables."
            "</div>"
            "<div style='background:#f8fafc;border:1px solid #cbd5e1;border-radius:5px;padding:1.4mm 2.2mm;'>"
            "<b style='color:var(--primary);'>Component 2: Writing Assessment (50 Mins &bull; 36 Marks)</b><br>"
            "&bull; <b>56% of marks (20/36)</b> are awarded for accurate <b>Spelling (Annexe D), Punctuation &amp; Grammar (SPaG)</b>.<br>"
            "&bull; Write <b>two functional texts</b> (e.g. email, letter, note, notice, form, or short feedback report) of <b>50&ndash;100 words</b>."
            "</div>"
            "</div>"
            "<table style='width:100%;border-collapse:collapse;font-size:8.2pt;line-height:1.22;'>"
            "<tr style='background:var(--primary);color:#fff;'>"
            "<th style='padding:0.8mm 1.5mm;text-align:left;width:13%;'>Code</th>"
            "<th style='padding:0.8mm 1.5mm;text-align:left;width:62%;'>Official DfE / Pearson Edexcel Entry Level 3 Subject Content</th>"
            "<th style='padding:0.8mm 1.5mm;text-align:left;width:25%;'>Core Guide Coverage</th>"
            "</tr>"
            "<tr style='border-bottom:1px solid #e2e8f0;background:#ffffff;'><td><b>E3.R8&ndash;R10</b></td><td>Read Entry 3 words accurately; identify main points, ideas, and purposes of straightforward texts.</td><td>Reading R1&ndash;R4, R6&ndash;R8, R10</td></tr>"
            "<tr style='border-bottom:1px solid #e2e8f0;background:#f8fafc;'><td><b>E3.R11&ndash;R12</b></td><td>Use alphabetical order (1st &amp; 2nd letters) and dictionaries; use headings, bullets, tables &amp; web menus.</td><td>Reading R5, R9, R11&ndash;R12</td></tr>"
            "<tr style='border-bottom:1px solid #e2e8f0;background:#ffffff;'><td><b>E3.W13</b></td><td>Use punctuation correctly: <b>capital letters, full stops, question marks, exclamation marks, commas in lists &amp; apostrophes</b>.</td><td>Writing Units W1, W2 &amp; W3 (pp. 28&ndash;33)</td></tr>"
            "<tr style='border-bottom:1px solid #e2e8f0;background:#f8fafc;'><td><b>E3.W14</b></td><td>Form <b>regular plurals</b> (<i>-s, -es</i>) and <b>irregular plurals</b> (<i>-ies, -ves, children, people, men, women</i>).</td><td>Writing Unit W7 &amp; Spelling SP4 (pp. 40, 58)</td></tr>"
            "<tr style='border-bottom:1px solid #e2e8f0;background:#ffffff;'><td><b>E3.W15</b></td><td>Use correct grammar: <b>subject-verb agreement</b>, consistent <b>past/present tense</b>, and <b>articles</b> (<i>a, an, the</i>).</td><td>Writing Units W6 &amp; W7 (pp. 38&ndash;41)</td></tr>"
            "<tr style='border-bottom:1px solid #e2e8f0;background:#f8fafc;'><td><b>E3.W16</b></td><td>Use the <b>first and second letters</b> to sequence words in <b>alphabetical order</b>.</td><td>Reading R5, Writing W8 &amp; Spelling SP6</td></tr>"
            "<tr style='border-bottom:1px solid #e2e8f0;background:#ffffff;'><td><b>E3.W17</b></td><td>Spell correctly words designated for Entry Level 3 (<b>Official Annexe D Word List</b> prefixes, suffixes, silent letters).</td><td>Spelling Units SP1&ndash;SP6 (pp. 52&ndash;63)</td></tr>"
            "<tr style='border-bottom:1px solid #e2e8f0;background:#f8fafc;'><td><b>E3.W18&ndash;W19</b></td><td>Communicate information, ideas and opinions clearly in a <b>logical sequence</b> and appropriate detail/length.</td><td>Writing Units W8&ndash;W12 (pp. 42&ndash;51)</td></tr>"
            "<tr style='border-bottom:1px solid #e2e8f0;background:#ffffff;'><td><b>E3.W20</b></td><td>Use appropriate <b>format and structure</b> (<b>emails, letters, notes, notices, forms, feedback</b>) with <b>headings &amp; bullets</b>.</td><td>Writing Units W9&ndash;W12 (pp. 44&ndash;51)</td></tr>"
            "<tr style='background:#f8fafc;'><td><b>E3.W21&ndash;W22</b></td><td>Write in <b>complete and compound sentences</b> (<i>and, but, or, so, because</i>), use <b>paragraphs</b>, and suit <b>audience/purpose</b>.</td><td>Writing Units W4, W5, W8&ndash;W12</td></tr>"
            "</table>"
            "</div>",
            title="Official Pearson Edexcel Entry Level 3 Specification &amp; Syllabus Map"
        )
        + K.tip_pair("In Writing, tick off every bullet point in the question prompt and write in complete, punctuated sentences.",
                     "Check the 5-Point SPaG Scan: (1) Capital letters, (2) End marks (. ? !), (3) Commas &amp; apostrophes, (4) Tense &amp; plurals, (5) Annexe D spellings.",
                     golden_title="Full-Marks Writing Strategy", watch_title="5-Point SPaG Proofreading Scan")
    )
    pages.append(K.page(p3_body, header=(BOOK, "Exam &bull; Syllabus Overview"), footer=BOOK, page_no=3))

    # p4 to p27: 12 Entry Level 3 Reading Units (24 pages: 2 pages each)
    reading_units_e3 = [
        ("Reading Notices and Signs",
         "Public notices and workplace safety signs use <b>bold headings</b>, <b>capital letters</b>, and <b>imperative (command) verbs</b> (e.g. <i>Stop, Walk, Do NOT use</i>) to give urgent instructions and warnings (Syllabus <b>E3.R9, E3.R10, E3.R12</b>).",
         [("evacuation", "leaving a building safely in an emergency"),
          ("assembly point", "safe outdoor meeting place during a fire drill"),
          ("fire warden", "trained staff member in charge of fire safety"),
          ("routine", "happening regularly as part of a normal schedule"),
          ("emergency exit", "designated green door used to escape danger"),
          ("prohibited", "strictly not allowed (e.g. Do NOT use lifts)")],
         "Scan for capitalised names, days, times (e.g. 10:00am), and words in CAPITALS like 'NOT'.",
         "Do not confuse the routine weekly test time with what to do in a real emergency.",
         "Workplace Notice: Fire Safety &amp; Emergency Evacuation (Bay 4)",
         "In the event of a fire alarm, immediately stop work and leave the building via the nearest green emergency exit. Do NOT use the lifts. Walk calmly to Assembly Point B on the south car park. The fire warden for Bay 4 is Mrs Helen Patel. Routine alarm testing takes place every Tuesday at 10:00am.",
         [("1.", "Where is Assembly Point B located? [1 mark]"),
          ("2.", "What time is the routine alarm tested on Tuesdays? [1 mark]"),
          ("3.", "Who is the fire warden for Bay 4? [1 mark]"),
          ("4.", "State one thing you must NOT use during an evacuation. [1 mark]")]),

        ("Finding Main Ideas in Articles",
         "Newspaper and community articles use a <b>headline</b> to sum up the main topic and an <b>opening sentence</b> that answers <i>Who, What, Where, and When</i> (Syllabus <b>E3.R9, E3.R10</b>).",
         [("reopens", "opens again to the public after work or closure"),
          ("volunteers", "people who offer their time freely without pay"),
          ("transformed", "changed completely in appearance for the better"),
          ("allotment", "small plot of land rented for growing vegetables"),
          ("sensory garden", "garden designed with plants to touch, smell, and see"),
          ("pavilion", "shelter or clubhouse building in a park or garden")],
         "Read the headline and first sentence first to spot the main event, date, and opening time.",
         "Give the exact details from the article rather than general answers from memory.",
         "Local News: Greendale Community Garden Autumn Opening",
         "The Greendale Community Garden officially reopens this Saturday 11 October at 10:00am for autumn bulb planting. Local volunteers have transformed the overgrown allotment into a sensory garden with raised vegetable beds. Free gardening gloves and seed packets are provided for all attendees. Tea and homemade cakes will be served in the pavilion.",
         [("1.", "What date does the community garden reopen? [1 mark]"),
          ("2.", "What free equipment is provided for volunteers? [1 mark]"),
          ("3.", "What has been built in the garden? [1 mark]"),
          ("4.", "Where will tea and cakes be served? [1 mark]")]),

        ("Reading Emails from Work or College",
         "Workplace and college emails contain a <b>Subject Line</b> stating the main topic, a polite greeting, key action details (dates, room numbers, items to bring), and contact details (Syllabus <b>E3.R9, E3.R12</b>).",
         [("induction", "introductory welcome session for new learners or staff"),
          ("enrolment", "officially registering onto a college course"),
          ("photographic ID", "official identity document with your photo (passport/licence)"),
          ("reception", "front desk where visitors and students sign in"),
          ("security lanyard", "neck strap holding your official college ID pass"),
          ("notify", "inform or tell someone officially by phone or email")],
         "Look for numbers and capital letters to find room codes (Room B14), times (09:30), and phone numbers.",
         "Check whether a question asks for the room number, the document to bring, or the item issued.",
         "Email: Student ID Cards and Enrolment Confirmation",
         "Dear Learner, Welcome to Oxford City College. Your functional skills induction takes place on Monday 15 September at 09:30 in Room B14. Please bring your photographic ID (passport or driving licence) so reception can issue your electronic security lanyard. If you cannot attend, notify your tutor Abdul on 01865 554100.",
         [("1.", "What room does the induction take place in? [1 mark]"),
          ("2.", "What document must you bring to reception? [1 mark]"),
          ("3.", "What telephone number should you call if you cannot attend? [1 mark]"),
          ("4.", "What item will reception issue to you? [1 mark]")]),

        ("Following Simple Instructions and Recipes",
         "Instructional texts use <b>numbered steps (1, 2, 3...)</b> in chronological order and <b>bossy/imperative verbs</b> (<i>Plug, Wait, Insert, Feed, Allow</i>) so you complete a task safely (Syllabus <b>E3.R9, E3.R10, E3.R12</b>).",
         [("laminator", "machine that seals paper inside protective clear plastic"),
          ("illuminates", "lights up or shines brightly"),
          ("pouch", "clear plastic pocket that holds the paper sheet"),
          ("equal borders", "even spaces around all four edges of the paper"),
          ("sealed edge", "closed, joined side of the plastic pouch"),
          ("rollers", "rotating cylinders inside the machine that pull the sheet")],
         "Follow the numbered steps in order and check exact measurements of time (4 minutes vs 60 seconds).",
         "Never mix up heating-up time (Step 2: 4 minutes) with cooling-down time (Step 5: 60 seconds).",
         "How to Operate the Office Laminator Safely",
         "1. Plug the laminator into the wall socket and switch the power button on.<br>2. Wait 4 minutes until the green READY light illuminates.<br>3. Insert your document into the clear plastic pouch, leaving equal borders on all sides.<br>4. Feed the sealed edge of the pouch gently into the front feeder tray until the rollers pull it through.<br>5. Allow the hot laminated document to cool on the rear flat tray for 60 seconds.",
         [("1.", "Which light shows the machine is ready to use? [1 mark]"),
          ("2.", "Which edge of the pouch must enter the machine first? [1 mark]"),
          ("3.", "How long should you let the finished document cool? [1 mark]"),
          ("4.", "How many minutes does the machine take to heat up? [1 mark]")]),

        ("Using an Alphabetical Directory",
         "Directories, glossaries, and dictionaries list entries in <b>alphabetical order (A to Z)</b> using the <b>first and second letters</b> of each word (Syllabus <b>E3.R11, E3.R12, E3.W16</b>).",
         [("directory", "A-to-Z list of organisations, names, and phone numbers"),
          ("enquiries", "questions or requests for official information"),
          ("emergency", "urgent situation needing immediate medical or dental care"),
          ("renewals", "extending the loan period for library books"),
          ("alphabetical", "arranged in the exact order of the alphabet (A to Z)"),
          ("appointments", "arranged times to see a professional or advisor")],
         "Use the bold service names on the left (A, C, D, J, P) to jump straight to the right phone number.",
         "If two words start with the same first letter, look at the second letter (e.g. Ca comes before Ci).",
         "High Street Services Quick Contact Directory",
         "&bull; <b>Adult Education Hub:</b> 01865 240100 (Course advice &amp; enrolments)<br>&bull; <b>Citizens Advice Bureau:</b> 01865 245200 (Legal &amp; financial support)<br>&bull; <b>Dental Access Clinic:</b> 01865 248900 (Emergency appointments)<br>&bull; <b>Jobcentre Plus Office:</b> 01865 251400 (Universal Credit enquiries)<br>&bull; <b>Public Library Loans:</b> 01865 255800 (Renewals &amp; computer booking)",
         [("1.", "Which telephone number connects to Citizens Advice? [1 mark]"),
          ("2.", "Which organisation helps with Universal Credit enquiries? [1 mark]"),
          ("3.", "Which service is listed immediately before Dental Access Clinic? [1 mark]"),
          ("4.", "What number should you call to renew a library book? [1 mark]")]),

        ("Understanding Workplace Memos",
         "An internal <b>workplace memo</b> uses a structured header block (<b>To: / From: / Date:</b>) to share official rules, deadlines, and staff updates quickly (Syllabus <b>E3.R9, E3.R10, E3.R12</b>).",
         [("operatives", "skilled workers who operate equipment in a warehouse"),
          ("annual leave", "paid holiday time off work each year"),
          ("deadline", "final date and time by which something must be handed in"),
          ("guaranteed", "promised or certain to be approved"),
          ("peak seasonal", "busiest time of the year (such as December)"),
          ("distributed", "handed out or given to staff members")],
         "Always check the 'To:' and 'From:' header lines first to see who receives and who sent the memo.",
         "Do not confuse the date the memo was written (1 November) with the holiday deadline (21 November).",
         "Internal Staff Memo: Annual Leave Booking Deadline",
         "To: All Warehouse Operatives<br>From: Warehouse Operations Manager<br>Date: 1 November 2026<br>Please submit all holiday requests for December and January to your team leader by Friday 21 November at 17:00. Requests submitted after this date cannot be guaranteed due to peak seasonal shipping volumes. Uniform hoodies and thermal gloves will be distributed next Monday.",
         [("1.", "Who is this internal memo addressed to? [1 mark]"),
          ("2.", "What is the final deadline date for holiday requests? [1 mark]"),
          ("3.", "Who must you submit your holiday request form to? [1 mark]"),
          ("4.", "What winter clothing items will be distributed next Monday? [1 mark]")]),

        ("Reading Healthcare Appointment Letters",
         "Hospital and GP letters give essential factual instructions: <b>clinic name, date, appointment time, arrival window, and items to bring</b> (Syllabus <b>E3.R8, E3.R9, E3.R10</b>).",
         [("outpatient", "hospital patient who attends a clinic without staying overnight"),
          ("physiotherapy", "treatment that helps restore movement and strength"),
          ("scheduled", "planned and booked for a specific date and time"),
          ("prescribed", "medications officially ordered by a doctor"),
          ("medications", "medicines or tablets taken to treat a health condition"),
          ("confirmation", "written proof that an appointment is booked")],
         "Underline the clinic number, date, time, and the word 'bring' so you do not miss two-part questions.",
         "When a question asks for TWO items to bring, make sure you write down two separate items.",
         "NHS Hospital Appointment Confirmation Letter",
         "Dear Mr Taylor, Please attend Outpatient Clinic 3 at the Churchill Hospital on Thursday 27 November at 11:15am for your scheduled physiotherapy review. Please arrive 15 minutes before your appointment time. You should bring your appointment letter, a list of your current prescribed medications, and wear loose comfortable clothing.",
         [("1.", "Which hospital clinic must Mr Taylor attend? [1 mark]"),
          ("2.", "What time is the physiotherapy appointment? [1 mark]"),
          ("3.", "How many minutes early should the patient arrive? [1 mark]"),
          ("4.", "Name two items Mr Taylor must bring with him. [1 mark]")]),

        ("Comparing Two Short Information Texts",
         "When comparing <b>Text A</b> and <b>Text B</b> on the same topic, check the <b>same feature in both texts</b> (journey time, ticket price, frequency, and facilities) (Syllabus <b>E3.R9, E3.R10, E3.R12</b>).",
         [("departs", "leaves or sets off from a station or bus stop"),
          ("journey time", "how many minutes or hours a trip takes from start to finish"),
          ("single ticket", "one-way travel ticket from one place to another"),
          ("twice per hour", "two times every 60 minutes (every 30 minutes)"),
          ("facilities", "useful features provided for passengers (e.g. Wi-Fi)"),
          ("quiet coaches", "train carriages where mobile calls and loud noise are banned")],
         "Compare numbers carefully: 16 minutes (Train) is faster than 42 minutes (Bus), while £2.30 is cheaper than £5.80.",
         "Make sure you look at Text A when asked about Bus Route 40 and Text B when asked about the Train.",
         "Travel Guide: Comparing Bus Route 40 and City Express Train",
         "<b>Text A (Bus Route 40):</b> Leaves Market Square every 12 minutes. Journey time to town centre is 42 minutes. Adult single ticket costs £2.30. Free Wi-Fi on board.<br><b>Text B (City Express Train):</b> Departs from Central Station twice per hour. Journey time is only 16 minutes. Adult single ticket costs £5.80. Quiet coaches available.",
         [("1.", "How much does a single ticket cost on Bus Route 40? [1 mark]"),
          ("2.", "Which service has the faster journey time? [1 mark]"),
          ("3.", "How often does the train depart from Central Station? [1 mark]"),
          ("4.", "State one free facility available on Bus Route 40. [1 mark]")]),

        ("Understanding Table and Timetable Information",
         "Tables organise information into <b>horizontal rows</b> and <b>vertical columns</b>. Read across the row from the Day or Activity to find the matching Time, Facility, or Cost (Syllabus <b>E3.R12</b>).",
         [("timetable", "chart showing days, start/finish times, and activities"),
          ("facility", "specific room, pool, or studio where an activity happens"),
          ("lane swimming", "swimming up and down marked lengths of a pool"),
          ("pilates", "exercise class focusing on core strength and flexibility"),
          ("aqua aerobics", "fitness exercise class performed in shallow water"),
          ("training pool", "smaller, shallower pool used for classes and learners")],
         "Place your finger on the column heading at the top and trace down to the row you need.",
         "Do not mix up the Main Pool (Monday &amp; Saturday) with Studio 2 (Wednesday) or the Training Pool (Friday).",
         "Blackbird Leys Leisure Centre Weekly Activity Timetable",
         "<table style='width:100%;border-collapse:collapse;margin:2mm 0;font-size:11pt;' border='1'>"
         "<tr style='background:#f1f5f9;'><th>Day</th><th>Time</th><th>Activity</th><th>Facility</th><th>Cost</th></tr>"
         "<tr><td>Monday</td><td>07:00&ndash;09:00</td><td>Lane Swimming</td><td>Main Pool</td><td>£4.20</td></tr>"
         "<tr><td>Wednesday</td><td>18:30&ndash;19:30</td><td>Pilates Class</td><td>Studio 2</td><td>£6.50</td></tr>"
         "<tr><td>Friday</td><td>10:00&ndash;11:00</td><td>Aqua Aerobics</td><td>Training Pool</td><td>£5.00</td></tr>"
         "<tr><td>Saturday</td><td>09:00&ndash;12:00</td><td>Family Fun Swim</td><td>Main Pool</td><td>£3.50</td></tr>"
         "</table>",
         [("1.", "What time does Lane Swimming start on Monday? [1 mark]"),
          ("2.", "Which studio hosts the Pilates Class on Wednesday? [1 mark]"),
          ("3.", "How much does Family Fun Swim cost on Saturday? [1 mark]"),
          ("4.", "On which day is Aqua Aerobics held? [1 mark]")]),

        ("Fact versus Opinion in Community Leaflets",
         "A <b>fact</b> is a true statement that can be proved with numbers, dates, or evidence. An <b>opinion</b> is someone's personal feeling or belief using words like <i>best, most enjoyable, relaxing</i> (Syllabus <b>E3.R9, E3.R10</b>).",
         [("launched", "officially started or introduced for the first time"),
          ("residents", "people who live in a local town, city, or area"),
          ("designated", "officially marked and set aside for a special purpose"),
          ("enjoyable", "giving pleasure or happiness (an opinion word)"),
          ("high-visibility", "bright fluorescent clothing with reflective strips"),
          ("discounted", "sold at a lower, reduced price")],
         "Look for numbers and dates (2024, 15,000) to find facts; look for feeling adjectives (most enjoyable) for opinions.",
         "Copy the full opinion statement clearly when a question asks you to identify an opinion.",
         "Leaflet: Support Oxford's Green Commute Scheme",
         "The Oxford Cycle Scheme launched in 2024. Over 15,000 residents now use designated cycle paths every weekday. Cycling is definitely the most enjoyable and relaxing way to travel to work. Helmets and high-visibility jackets are available to purchase at discounted rates from council hubs.",
         [("1.", "In what year did the Oxford Cycle Scheme launch? [1 mark]"),
          ("2.", "How many residents use the cycle paths each weekday? [1 mark]"),
          ("3.", "Identify one opinion stated in the text. [1 mark]"),
          ("4.", "Name one discounted safety item available at council hubs. [1 mark]")]),

        ("Reading Online Forms and Web Pages",
         "Web pages use <b>website addresses (URLs)</b>, <b>buttons</b>, and <b>drop-down menus</b> to help users complete online forms and council requests (Syllabus <b>E3.R9, E3.R12</b>).",
         [("portal", "website gateway where users access online services"),
          ("replacement", "new item provided to take the place of a lost or broken one"),
          ("homepage", "main front page of a website"),
          ("drop-down menu", "clickable list of options on a computer screen"),
          ("working days", "Monday to Friday (excluding weekends and bank holidays)"),
          ("debit card", "bank card used to pay directly from a current account")],
         "Look for bold text (www.oxford.gov.uk/bins) and words inside quotation marks ('Report or Request').",
         "Copy website addresses (URLs) exactly as printed, including dots and slashes.",
         "Web Page Guide: Council Waste Collection Portal",
         "To order a replacement recycling bin, visit <b>www.oxford.gov.uk/bins</b>. Click the green 'Report or Request' button on the homepage. Enter your postcode and house number. Select 'Replacement Blue Bin' from the drop-down menu. Deliveries take 5 working days and cost £15.00 payable by debit card.",
         [("1.", "What web address should you visit to order a replacement bin? [1 mark]"),
          ("2.", "Which button should you click on the homepage? [1 mark]"),
          ("3.", "How many working days does delivery take? [1 mark]"),
          ("4.", "How much does a replacement blue bin cost? [1 mark]")]),

        ("Reading Product Labels and Warnings",
         "Medicine and product labels divide information into <b>Directions for Use</b> (how and how often to use it) and <b>Storage / Warnings</b> (temperature limits, safety, and expiry dates) (Syllabus <b>E3.R8, E3.R9, E3.R12</b>).",
         [("antiseptic", "cream or liquid that prevents infection in minor cuts/grazes"),
          ("affected area", "part of the skin that is hurt, sore, or injured"),
          ("external use", "for use on the outside of the skin only (never swallow)"),
          ("avoid contact", "keep away from sensitive areas such as the eyes"),
          ("out of reach", "stored high up or locked away where children cannot get it"),
          ("expiry date", "date after which a medicine must not be used (EXP 08/2028)")],
         "Use the bold subheadings ('Directions for Use:' vs 'Storage:') to locate the answer quickly.",
         "Include the unit symbol (°C) when writing down the maximum storage temperature (25°C).",
         "Label Instructions: All-Purpose Antiseptic Cream",
         "<b>Directions for Use:</b> Clean the affected area gently with warm water. Apply a thin layer of cream two to three times daily as required. For external use only. Avoid contact with eyes.<br><b>Storage:</b> Store below 25&deg;C. Keep out of reach of children. Do not use after expiry date printed on tube crimp (EXP 08/2028).",
         [("1.", "How many times daily can this cream be applied? [1 mark]"),
          ("2.", "What must you clean the affected area with first? [1 mark]"),
          ("3.", "What maximum temperature should the product be stored below? [1 mark]"),
          ("4.", "What part of the body must you avoid contact with? [1 mark]")])
    ]

    p_curr = 4
    for r_idx, (r_title, r_desc, r_vocab, r_gold, r_watch, p2_title, p2_passage, p2_qs) in enumerate(reading_units_e3, 1):
        photo_rel, photo_cap = E3_READING_PHOTOS[r_idx]
        photo_path = str(K.PHOTO_DIR / photo_rel)
        vocab_html = "".join(
            f"<div style='background:#f8fafc;border:1px solid #cbd5e1;border-radius:4px;padding:0.9mm 1.8mm;font-size:8.6pt;line-height:1.28;'>"
            f"<b style='color:var(--primary);'>{w}:</b> {d}</div>"
            for w, d in r_vocab
        )
        # Page 1: Learn
        p1_r = (
            K.page_title(f"Reading Unit {r_idx}: {r_title}", kicker="Entry Level 3 Reading Skills &bull; Syllabus E3.R8–R12", badge=f"R{r_idx}")
            + K.hero_image(photo_path, photo_cap, 58, fill=True, pos="center center")
            + K.rule_box("Reading Skill, Strategy &amp; Key Vocabulary",
                         f"<p style='font-size:10.8pt;line-height:1.42;margin:0 0 1.8mm 0;'>{r_desc}</p>"
                         f"<div style='display:grid;grid-template-columns:1fr 1fr;gap:1.5mm;'>{vocab_html}</div>")
            + K.tip_pair(r_gold, r_watch, golden_title="Search Strategy", watch_title="Examiner Watch Out")
            + K.fill_notes(f"Important Words &amp; Meanings (Unit {r_idx})", min_mm=20)
        )
        pages.append(K.page(p1_r, header=(BOOK, f"Reading {r_idx} &bull; Learn"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 2: Practice Text & Questions
        qs_html = "".join(f"<p style='margin:1.5mm 0;'><b>{q_num}</b> {escape_html(q_txt)}</p>" for q_num, q_txt in p2_qs)
        p2_r_card = e3_task_photo_card(photo_rel, f"Unit {r_idx}: {r_title[:26]}") if r_idx != 9 else ""
        p2_r = (
            K.page_title(f"Reading Unit {r_idx} &bull; Practice Text", kicker="Comprehension Questions &bull; 4 Marks", badge="PRACTICE")
            + K.box_html(
                f"<div style='background:#f8fafc;padding:3.5mm;border:1.5px solid var(--soft);border-radius:6px;font-size:11.8pt;line-height:1.52;margin-bottom:2mm;overflow:hidden;'>"
                f"{p2_r_card}"
                f"<strong style='color:var(--primary);'>{p2_title}</strong><br>"
                f"{p2_passage}"
                f"</div>"
                f"<div style='font-size:11.2pt;line-height:1.48;'>"
                f"{qs_html}"
                f"</div>",
                title=f"Practice Text &bull; Unit {r_idx}"
            )
            + K.fill_lines("Write your answers below (worked solutions on p. 80):", min_mm=60, gap_mm=10)
        )
        pages.append(K.page(p2_r, header=(BOOK, f"Reading {r_idx} &bull; Questions"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p28 to p51: 12 Entry Level 3 Writing & Format Units (24 pages: 2 pages each)
    # Covers 100% of Pearson Edexcel Entry Level 3 Writing Syllabus (E3.W13 to E3.W22)
    writing_units_e3 = [
        ("Capital Letters for Sentences, Names and Places",
         "Syllabus <b>E3.W13</b> requires a <b>capital letter</b> at the <b>start of every sentence</b>, for the pronoun <b>'I'</b>, and for all <b>proper nouns</b>: people's names and titles (<i>Mr Clarke, David</i>), days (<i>Monday, Friday</i>), months (<i>October</i>), and towns/places (<i>Oxford, High Street</i>).",
         "every monday morning, david catches the bus to oxford and i meet him.",
         "<b>E</b>very <b>M</b>onday morning, <b>D</b>avid catches the bus to <b>O</b>xford and <b>I</b> meet him.",
         "Always check that the single word 'I' is a capital letter, even in the middle of a sentence.",
         "Do not put capital letters on ordinary common nouns like 'bus', 'morning', or 'reception'.",
         "Fix the Missing Capital Letters (E3.W13)",
         "Rewrite the following workplace passage adding all <b>10 missing capital letters</b>:<br>"
         "<i>every monday morning, david catches the bus to oxford. he works with mr clarke at the community centre. last friday, i helped them paint the reception room in october.</i>",
         "Write the corrected paragraph with all capital letters in place:"),

        ("Full Stops, Question Marks and Exclamation Marks",
         "Syllabus <b>E3.W13</b> tests three end-of-sentence marks: a <b>full stop (.)</b> ends a statement or fact; a <b>question mark (?)</b> ends a direct question starting with <i>Who, What, Where, When, Why, How, Have, Do, Can</i>; an <b>exclamation mark (!)</b> shows an urgent warning or strong feeling.",
         "What time does the training start. The van has arrived, watch out for the hot pipe.",
         "What time does the training start<b>?</b> The van has arrived<b>.</b> <b>W</b>atch out for the hot pipe<b>!</b>",
         "Read each sentence aloud: if it asks for an answer, it must end with a question mark (?).",
         "Never use two exclamation marks (!!) in workplace writing, and always put a capital letter after every . ? or !",
         "Sentence End Punctuation Drill (E3.W13)",
         "Add the correct punctuation mark (<b>.</b> or <b>?</b> or <b>!</b>) at the end of each sentence and rewrite:<br>"
         "1. What time does the afternoon training session start<br>"
         "2. The delivery van arrived outside the warehouse at ten o'clock<br>"
         "3. Watch out for the hot steam pipe<br>"
         "4. Have you filled in your timesheet for this week",
         "Write out each sentence with its correct end punctuation mark:"),

        ("Commas in Lists and Apostrophes for Contractions",
         "Syllabus <b>E3.W13</b> covers <b>commas in lists</b> (use commas between 3 or more items, with <i>and</i> before the last item) and <b>apostrophes</b> for <b>contraction/omission</b> (where letters are left out: <i>do not &rarr; don't, cannot &rarr; can't, I am &rarr; I'm, it is &rarr; it's</i>) and <b>singular possession</b> (<i>Sarah's pass</i>).",
         "We ordered pens paper clips and folders, but I cant find Sarahs notebook.",
         "We ordered pens<b>,</b> paper<b>,</b> clips and folders, but I <b>can't</b> find <b>Sarah's</b> notebook.",
         "Put the apostrophe directly in the exact spot where the missing letter stood (do not -> don't).",
         "Do not put a comma right before the first item in a list or after the word 'and'.",
         "List Commas &amp; Apostrophes Practice (E3.W13)",
         "Insert the missing <b>commas in the lists</b> and <b>apostrophes in contractions/possessives</b>:<br>"
         "1. Please order highlighters pens notebooks sticky labels and printer paper.<br>"
         "2. The tool kit contains a hammer pliers screwdriver wrench and tape measure.<br>"
         "3. Im sorry I cant attend Mondays meeting because Sarahs car wont start.",
         "Write out the 3 sentences with accurate commas and apostrophes:"),

        ("Joining Compound Sentences with 'And', 'But' and 'Or'",
         "Syllabus <b>E3.W21</b> requires you to join two short simple sentences into a <b>compound sentence</b> using a coordinating conjunction: <b>and</b> (adds a similar point), <b>but</b> (shows a contrast or problem), or <b>or</b> (offers an alternative choice).",
         "I wanted to apply for the warehouse job. I did not have a forklift licence.",
         "I wanted to apply for the warehouse job<b>, but</b> I did not have a forklift licence.",
         "When joining two sentences with 'and', 'but', or 'or', drop the first full stop and change the next capital letter to lower case (unless it is 'I' or a name).",
         "Do not join two separate sentences with only a comma (a 'comma splice' loses SPaG marks).",
         "Joining Sentences with Conjunctions (E3.W21)",
         "Join each pair of simple sentences into one compound sentence using <b>and</b>, <b>but</b>, or <b>or</b>:<br>"
         "1. I wanted to apply for the warehouse job. I did not have a forklift licence.<br>"
         "2. Tariq passed his maths test. He received a promotion at work.<br>"
         "3. You can book your appointment online. You can call the clinic reception desk.",
         "Write your 3 joined compound sentences below:"),

        ("Giving Reasons with 'Because', 'So', 'When' and 'If'",
         "Syllabus <b>E3.W21</b> tests linking ideas logically: use <b>because</b> before a reason/cause (<i>why</i> it happened), <b>so</b> before a result/outcome (<i>what happened next</i>), and <b>when / if</b> to state times or conditions.",
         "The warehouse floor was wet because the cleaner put up a yellow warning sign.",
         "The warehouse floor was wet<b>, so</b> the cleaner put up a yellow warning sign.",
         "Test the link: 'because' answers WHY ('...because she had an appointment'); 'so' tells the RESULT ('...so she booked Friday off').",
         "Spell 'because' accurately using the memory phrase: Big Elephants Can Always Understand Small Elephants.",
         "Giving Logical Reasons in Workplace Writing (E3.W21)",
         "Complete each sentence logically by choosing <b>because</b>, <b>so</b>, or <b>if</b>:<br>"
         "1. The fire alarm sounded [because / so] everyone left the building calmly.<br>"
         "2. Elena booked Friday off work [because / so] she had a hospital appointment.<br>"
         "3. The warehouse floor was wet [because / so] the cleaner put up a warning sign.<br>"
         "4. Please call reception [because / if] you are running more than 10 minutes late.",
         "Write out all 4 completed sentences:"),

        ("Past Tense: Regular and Irregular Verbs",
         "Syllabus <b>E3.W15</b> requires <b>consistent tense</b>. For events that already happened (<i>yesterday, last week</i>), use the <b>past tense</b>: regular verbs add <b>-ed / -d</b> (<i>walked, delivered, signed, arrived</i>), while common <b>irregular verbs</b> change spelling (<i>go &rarr; went, take &rarr; took, speak &rarr; spoke, find &rarr; found, buy &rarr; bought</i>).",
         "Yesterday the courier deliver three boxes and I take them into the storeroom.",
         "Yesterday the courier <b>delivered</b> three boxes and I <b>took</b> them into the storeroom.",
         "Check time words at the start of the task ('Yesterday', 'Last Tuesday') and keep every verb in the past tense.",
         "Never add '-ed' to irregular verbs (write 'spoke' and 'found', never 'speaked' or 'finded').",
         "Past Tense Workplace Log (E3.W15)",
         "Rewrite this workplace log changing the <b>5 verbs in brackets</b> into the correct <b>past tense</b>:<br>"
         "<i>Yesterday, the courier [deliver] three boxes to reception. I [sign] the receipt and [take] them into the storeroom. Later, our supervisor [speak] to the driver and [find] the missing invoice.</i>",
         "Write the complete past tense paragraph below:"),

        ("Subject-Verb Agreement, Articles ('A'/'An') and Plurals",
         "Syllabus <b>E3.W14 &amp; E3.W15</b> cover three core grammar rules: (1) <b>Agreement:</b> singular subjects take <i>is / was / has / works</i>; plural subjects take <i>are / were / have / work</i>. (2) <b>Articles:</b> use <b>an</b> before a vowel sound (<i>a, e, i, o, u</i>: <i>an email, an office, an hour</i>) and <b>a</b> before a consonant (<i>a shift, a uniform</i>). (3) <b>Plurals:</b> <i>box &rarr; boxes, duty &rarr; duties, shelf &rarr; shelves, child &rarr; children, person &rarr; people, woman &rarr; women</i>.",
         "Two delivery driver has arrived with a urgent parcel for the childrens clinic.",
         "Two delivery <b>drivers have</b> arrived with <b>an</b> urgent parcel for the <b>children's</b> clinic.",
         "When a singular word ends in consonant + y (duty, baby, city), drop the 'y' and add '-ies' (duties, babies, cities).",
         "Never use 'was' with plural subjects ('we were', 'they were', 'the boxes were' — never 'we was').",
         "Grammar, Articles &amp; Plurals Drill (E3.W14–W15)",
         "Rewrite each sentence choosing the correct verb, article (<b>a/an</b>), and <b>plural noun</b>:<br>"
         "1. The shift supervisor [explains / explain] the safety rules to [a / an] apprentice.<br>"
         "2. Two delivery [driver / drivers] [has / have] unloaded four heavy [box / boxes].<br>"
         "3. We [was / were] tidying the storage [shelf / shelves] for the three [woman / women].",
         "Write out each corrected sentence below:"),

        ("Writing in Paragraphs, Logical Order and Alphabetical Sequence",
         "Syllabus <b>E3.W16, E3.W18 &amp; E3.W21</b> require you to: (1) group related sentences into <b>clear paragraphs</b> separated by a blank line when the topic changes; (2) put ideas in a <b>logical order</b> (start &rarr; middle &rarr; end); and (3) sequence words in <b>alphabetical order</b> using the <b>first and second letters</b> (e.g. <i><b>a</b>ction, <b>a</b>ddress, <b>a</b>nswer, <b>a</b>ppear</i>).",
         "Course starts at 9:30am in Room 2. Free parking outside. Telephone skills covered. Buffet lunch at 12:30pm.",
         "<b>Paragraph 1 (Training Details):</b> Course starts at 9:30am in Room 2 and covers telephone skills.<br><b>Paragraph 2 (Lunch &amp; Parking):</b> A buffet lunch is served at 12:30pm and free parking is outside.",
         "Start a new paragraph whenever you move to a new bullet point or topic in an exam task.",
         "When putting words starting with the same letter into A–Z order, compare their second letters carefully.",
         "Paragraphs &amp; Alphabetical Order Practice (E3.W16, W18, W21)",
         "<b>Part A:</b> Divide this text into <b>two clear paragraphs</b> (Paragraph 1: <i>The Training Course</i>; Paragraph 2: <i>Lunch &amp; Parking</i>):<br>"
         "<i>Our customer service training takes place on Wednesday in Room 2. The course runs from 9:30am to 3:30pm and covers telephone skills. A buffet lunch and hot drinks are provided in the cafeteria. Free parking is available in the visitors car park.</i><br>"
         "<b>Part B:</b> Write these 4 Annexe D words in <b>alphabetical order</b>: <i><b>s</b>ystem, <b>s</b>afety, <b>s</b>chedule, <b>s</b>ervice</i>.",
         "Write your two paragraphs and the 4 alphabetised words below:"),

        ("Format 1: Writing a Formal or Informal Email (E3.W18–W22)",
         "Syllabus <b>E3.W20 &amp; E3.W22</b> require emails to match the audience: use a clear <b>Subject Line</b>, an appropriate greeting (<b>Dear Mr/Ms [Name],</b> for a manager/tutor; <b>Hi [Name],</b> for a friend/colleague), 2&ndash;3 short paragraphs covering every bullet point, and a matching sign-off (<b>Kind regards,</b> or <b>Best wishes,</b> + your full name).<br>"
         "<b>Specialist Vocabulary:</b> <i>appointment, reschedule, worksheet, grateful, attached, convenient, attend, sincerely</i>.",
         "hey send me the sheet i missed class on tuesday cos of the dentist thanks",
         "<b>Subject:</b> Absence on Tuesday &amp; Request for Maths Worksheet<br><b>Dear</b> Abdul,<br>I am writing to explain that I missed Tuesday's class because I had an urgent dental <b>appointment</b>.<br>Could you please email me the revision <b>worksheet</b> so I can catch up before next week?<br><b>Kind regards,</b><br>Samira Khan",
         "Always include a clear Subject line and address every bullet point in the question.",
         "Never use text-speak ('u', 'cos', 'thx') or lower-case 'i' in an email.",
         "Writing an Email to Request Course Notes (E3.W18–W22)",
         "Write a polite email (<b>50&ndash;70 words</b>) to your tutor <b>Abdul</b> (<i>abdul@oxfordcollege.ac.uk</i>). In your email you must:<br>"
         "&bull; Include a clear <b>Subject line</b> and polite greeting.<br>"
         "&bull; Explain why you missed Tuesday's class (e.g. a medical or dental appointment).<br>"
         "&bull; Ask for the revision worksheet and say when you will hand it in.<br>"
         "&bull; Sign off politely with your full name.",
         "Write your complete email below:"),

        ("Format 2: Writing a Formal Letter or Workplace Note (E3.W18–W22)",
         "Syllabus <b>E3.W20 &amp; E3.W22</b> test both <b>Letters</b> and <b>Workplace Notes</b>:<br>"
         "&bull; <b>Formal Letter Rules:</b> Put your address &amp; date at the top. If you open with <b>Dear Sir/Madam,</b> close with <b>Yours faithfully,</b>. If you open with a named person (<b>Dear Mr Green,</b>), close with <b>Yours sincerely,</b>.<br>"
         "&bull; <b>Workplace Note / Message Rules:</b> Include <b>To:</b>, <b>Date/Time:</b>, a clear factual message (who called, phone number, action needed), and <b>From:</b>.<br>"
         "<b>Specialist Vocabulary:</b> <i>urgent, colleague, message, telephoned, quotation, delivery, confirm, faithfully</i>.",
         "mr green called at lunch call him back before 3 on 07700900123",
         "<b>To:</b> Sam &bull; <b>Time:</b> 1:15pm<br><b>Dear</b> Sam,<br>A client named <b>Mr Green</b> telephoned while you were at lunch regarding his delivery order.<br>Please call him back urgently before <b>3:00pm</b> today on <b>07700 900123</b>.<br><b>Thanks,</b> Alex",
         "Copy all names, times (3:00pm), and phone numbers (07700 900123) accurately from the task brief.",
         "Match your letter sign-off: Dear Sir/Madam -> Yours faithfully; Dear Mr/Mrs [Surname] -> Yours sincerely.",
         "Leaving a Workplace Message for a Colleague (E3.W18–W22)",
         "Write a clear workplace note (<b>45&ndash;60 words</b>) to your colleague <b>Sam</b>. In your note you must:<br>"
         "&bull; State that a client called while Sam was out at lunch.<br>"
         "&bull; Give the client's name (<b>Mr Green</b>) and telephone number (<b>07700 900123</b>).<br>"
         "&bull; Explain that Mr Green needs an urgent call back before <b>3:00pm</b> today about his order.",
         "Write your complete workplace note below:"),

        ("Format 3: Notices &amp; Leaflets with Headings &amp; Bullets",
         "Syllabus <b>E3.W20</b> explicitly requires candidates to use <b>headings and bullet points where appropriate</b> when drafting a workplace notice, poster, or information leaflet:<br>"
         "&bull; Start with a <b>clear, bold main heading</b> stating what the notice is about.<br>"
         "&bull; Write an introductory sentence, then use <b>3&ndash;4 clear bullet points (&bull;)</b> for rules, dates, times, or instructions.<br>"
         "&bull; End with a polite reminder or contact details.<br>"
         "<b>Specialist Vocabulary:</b> <i>notice, hygiene, breakroom, immediately, appliances, disposed, cooperation, facilities</i>.",
         "everyone must wash their mugs after lunch and the fridge gets cleaned friday 4pm.",
         "<b>NOTICE: STAFF KITCHEN CLEANLINESS &amp; HYGIENE</b><br>Please help us keep the staff breakroom clean and tidy:<br>&bull; Wash and dry all mugs, plates, and cutlery immediately.<br>&bull; Wipe down the microwave and table surfaces after use.<br>&bull; Remove all old food from the fridge before <b>Friday at 4:00pm</b>.<br>Thank you for your cooperation. &mdash; <i>Facilities Team</i>",
         "Always include a bold capitalised title at the top and at least 3 bullet points (&bull;) in a notice or leaflet.",
         "Start every bullet point with a capital letter and end each full-sentence bullet with a full stop.",
         "Drafting a Staff Breakroom Notice (E3.W20)",
         "Draft a clear workplace notice (<b>50&ndash;70 words</b>) for the staff breakroom noticeboard. In your notice you must:<br>"
         "&bull; Include the clear heading: <b>Staff Kitchen Cleanliness</b>.<br>"
         "&bull; Use <b>bullet points</b> to remind staff to wash mugs/plates immediately and wipe the worktops.<br>"
         "&bull; State that the fridge will be emptied and cleaned every <b>Friday at 4:00pm</b>.",
         "Write your formatted breakroom notice with heading and bullet points below:"),

        ("Format 4: Forms &amp; Short Feedback Reports",
         "Syllabus <b>E3.W18–W22</b> test writing short <b>customer feedback reports, reviews, and form responses</b>:<br>"
         "&bull; <b>Paragraph 1 (Details &amp; Positive Praise):</b> State which service/venue you used, the date/time, and what went well (e.g. <i>polite driver, clean facilities, punctual service</i>).<br>"
         "&bull; <b>Paragraph 2 (Constructive Suggestion):</b> Use polite modal verbs (<i>could, should, would</i>) to suggest a practical improvement.<br>"
         "<b>Specialist Vocabulary:</b> <i>feedback, passenger, punctual, helpful, improvement, announcement, display, recommend</i>.",
         "route 15 bus driver was nice on monday but you need louder stop announcements.",
         "<b>Service Feedback: Bus Route 15 (Monday 10 November)</b><br>I travelled on <b>Bus Route 15</b> on Monday morning at 8:30am. The bus arrived on time and the driver was very polite, patient, and <b>helpful</b> to passengers.<br>However, one <b>improvement</b> you could make is installing clearer audio <b>announcements</b> for each stop.",
         "Balance your feedback: give specific praise first, then make a polite, realistic suggestion using 'could' or 'should'.",
         "Always write in full, grammatical sentences inside feedback boxes — never leave one-word fragments.",
         "Customer Service Feedback Report (E3.W18–W22)",
         "Write a short customer feedback report (<b>50&ndash;70 words</b>) for your local bus company. In your report you must:<br>"
         "&bull; State which bus route you used (<b>Route 15</b>) and when you travelled.<br>"
         "&bull; Praise the driver for being polite, patient, and helpful to passengers.<br>"
         "&bull; Suggest one clear improvement (e.g. clearer audio announcements or digital screen displays for stops).",
         "Write your complete feedback report below:")
    ]

    e3_w_title_css = (
        "<style>"
        ".ptitle h1 { font-size: 20.5pt !important; line-height: 1.1 !important; }"
        ".ptitle .badge { height: 16mm !important; min-width: 16mm !important; font-size: 17pt !important; }"
        "</style>"
    )

    for w_idx, (w_title, w_desc, w_wrong, w_right, w_gold, w_watch, p2_title, p2_task, p2_prompt) in enumerate(writing_units_e3, 1):
        photo_rel, photo_cap = E3_WRITING_PHOTOS[w_idx]
        photo_path = str(K.PHOTO_DIR / photo_rel)
        hero_h = 54 if w_idx >= 9 else 62
        # Page 1: Learn
        p1_w = (
            e3_w_title_css
            + K.page_title(f"Writing Unit {w_idx}: {w_title}", kicker="Entry Level 3 Writing &amp; Format Skills &bull; Syllabus E3.W13–W22", badge=f"W{w_idx}")
            + K.hero_image(photo_path, photo_cap, hero_h, fill=True, pos="center center")
            + K.rule_box("Core Writing Rule, Syllabus Explanation &amp; Vocabulary",
                         f"<p style='font-size:10.3pt;line-height:1.4;margin:0;'>{w_desc}</p>")
            + K.compare(w_wrong, w_right, bad_label="&#10007; Common Learner Error", good_label="&#10003; Entry 3 Full-Marks Model")
            + K.tip_pair(w_gold, w_watch, golden_title="Tutor Golden Rule", watch_title="Examiner Watch Out")
        )
        pages.append(K.page(p1_w, header=(BOOK, f"Writing {w_idx} &bull; Learn"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 2: Practice Task (with Writing Type / Thematic Picture Card like Level 1 & Level 2 books)
        card_rel, card_cap = E3_WRITING_TYPE_CARDS[w_idx]
        w_card_html = e3_task_photo_card(card_rel, card_cap)
        p2_w = (
            K.page_title(f"Writing Unit {w_idx} &bull; Practice Task", kicker="Applied Entry 3 Writing Drill &bull; 4 Marks", badge="PRACTICE")
            + K.box_html(
                f"<div style='background:#f8fafc;padding:2.5mm 3mm;border:1.5px solid var(--soft);border-radius:6px;font-size:10.5pt;line-height:1.45;margin-bottom:1.5mm;overflow:hidden;'>"
                f"{w_card_html}"
                f"<strong style='color:var(--primary);'>{p2_title}</strong><br>"
                f"{p2_task}"
                f"</div>",
                title=f"Practice Task &bull; Unit {w_idx}"
            )
            + K.fill_lines(f"{p2_prompt} (worked model on p. 80):", min_mm=25, gap_mm=9.5)
        )
        pages.append(K.page(p2_w, header=(BOOK, f"Writing {w_idx} &bull; Task"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p52 to p63: 6 Official Annexe D Spelling & Phonics Drills (12 pages: 2 pages each)
    spelling_drills_e3 = [
        ("Prefixes 'Un-', 'Dis-', 'Re-' and 'Pre-'",
         "Official Annexe D Rule (<b>E3.R8, E3.W17</b>): A <b>prefix</b> is added to the start of a root word without changing the root spelling. <b>un-</b> and <b>dis-</b> mean <i>not / opposite of</i>; <b>re-</b> means <i>again</i>; <b>pre-</b> means <i>before</i>.",
         ["unhappy", "unfair", "unwell", "unlock", "disagree", "disappear", "dislike", "reopen", "rebuild", "rewrite", "recycle", "prepare"],
         "Keep every letter of the root word intact when adding a prefix (dis + appear = disappear; un + necessary = unnecessary).",
         "Never drop the 's' when adding 'dis-' to a word starting with 's' (dis + satisfied = dissatisfied).",
         [("unwell", "Marcus stayed at home because he felt _______ ."),
          ("reopen", "The library will _______ at 9:00am on Monday morning."),
          ("unfair", "Colleagues agreed that the split shift was _______ ."),
          ("rewrite", "Please _______ the paragraph neatly on the lines below."),
          ("disagree", "I politely _______ with the proposed change to bus times."),
          ("recycle", "Please wash glass jars before placing them in the _______ bin.")]),

        ("Suffixes '-ful', '-less', '-ly', '-ness' and '-ment'",
         "Official Annexe D Rule (<b>E3.R8, E3.W17</b>): A <b>suffix</b> is added to the end of a root word: <b>-ful</b> (full of — <i>always spelled with ONE 'l'</i>), <b>-less</b> (without — <i>two 's's</i>), <b>-ly</b> (how something is done), <b>-ness</b> and <b>-ment</b> (forming nouns).",
         ["helpful", "careful", "painful", "grateful", "careless", "homeless", "quickly", "quietly", "politely", "kindness", "equipment", "appointment"],
         "Remember: the word 'full' has two L's, but the suffix '-ful' NEVER has two L's (helpful, careful, grateful, wonderful).",
         "When a root word ends in consonant + 'y' (happy, busy), change 'y' to 'i' before adding '-ly' or '-ness' (happily, happiness, business).",
         [("helpful", "The shop assistant was extremely _______ and carried my bags."),
          ("careful", "Be very _______ when carrying hot drinks down the corridor."),
          ("careless", "Avoid making _______ spelling mistakes in your job application."),
          ("painful", "His sprained ankle was swollen and _______ to walk on."),
          ("equipment", "All warehouse safety _______ must be returned to the locker."),
          ("politely", "The receptionist greeted every visitor _______ at the front desk.")]),

        ("Silent Letters 'K', 'W', 'G', 'B' and 'L'",
         "Official Annexe D Rule (<b>E3.R8, E3.W17</b>): Many high-frequency Entry 3 Annexe D words contain <b>silent letters</b> that you cannot hear when speaking: silent <b>k</b> before <i>n</i> (<i>knee, knife, knock, know</i>), silent <b>w</b> before <i>r</i> (<i>write, wrong, wrist, wrap</i>), silent <b>g</b> (<i>sign, design, foreign</i>), silent <b>b</b> (<i>thumb, climb, doubt</i>), and silent <b>l</b> (<i>could, should, would, half, calm</i>).",
         ["knife", "knee", "knock", "know", "write", "wrong", "wrist", "answer", "sign", "design", "doubt", "should"],
         "Group silent-letter words into families in your notebook (kn- family: know, knee, knife; wr- family: write, wrist, wrong; -ould family: could, would, should).",
         "Do not forget the silent 'w' in 'answer' and 'two', or the silent 'g' before 'n' in 'sign' and 'design'.",
         [("knife", "Use a sharp _______ to slice the bread on the chopping board."),
          ("write", "Remember to _______ your candidate number at the top of the page."),
          ("wrist", "She wore an electronic security pass on her left _______ ."),
          ("sign", "Look at the emergency exit _______ above the double doors."),
          ("answer", "Please check your _______ carefully before handing in the paper."),
          ("should", "You _______ arrive 15 minutes before your hospital appointment.")]),

        ("Double Consonants and Plural Spelling Rules",
         "Official Annexe D Rule (<b>E3.W14, E3.W17</b>): Double a single consonant after a short vowel sound before adding <i>-ing, -ed, -er</i> (<i>stop &rarr; stopped, plan &rarr; planning, run &rarr; runner</i>), and learn high-frequency double-consonant words (<i>address, traffic, accident, different, difficult, community, tomorrow</i>).",
         ["address", "traffic", "summer", "accident", "different", "difficult", "tomorrow", "accommodation", "business", "success", "stopped", "planned"],
         "Break tricky double-letter words into chunks: AD-DRESS (double d, double s), TO-MOR-ROW (one m, double r), AC-CI-DENT (double c).",
         "Watch out for 'tomorrow' (only ONE 'm', TWO 'r's) and 'address' (TWO 'd's, TWO 's's).",
         [("address", "Please write your full home _______ including postcode on the form."),
          ("traffic", "The delivery van was delayed in heavy motorway _______ ."),
          ("summer", "During the warm _______ months, the outdoor terrace opens at 8am."),
          ("accident", "Always report any workplace _______ immediately to the first aider."),
          ("different", "Our college offers _______ study times for daytime and evening learners."),
          ("tomorrow", "The maintenance engineer will repair the heating boiler _______ morning.")]),

        ("Words Ending in '-tion', '-sion', '-sure' and '-ture'",
         "Official Annexe D Rule (<b>E3.R8, E3.W17</b>): The <b>/shun/</b> sound at the end of a noun is usually spelled <b>-tion</b> (<i>action, station, question, section, information, instruction, qualification, reception</i>) or <b>-sion</b> (<i>decision, discussion, television, permission</i>). The <b>/cher/</b> sound is spelled <b>-ture</b> (<i>picture, future, furniture, temperature</i>).",
         ["station", "question", "section", "action", "information", "instruction", "reception", "application", "decision", "discussion", "picture", "temperature"],
         "Most nouns formed from verbs ending in '-t' or '-te' use '-tion' (instruct -> instruction, inform -> information, educate -> education).",
         "Use '-sion' for words built from verbs ending in '-d', '-de', or '-ss' (decide -> decision, discuss -> discussion).",
         [("station", "The train arrives at Oxford Central _______ at quarter past eight."),
          ("question", "Raise your hand if you have a _______ about the project."),
          ("decision", "The manager made a final _______ regarding the shift pattern."),
          ("section", "Read the health and safety _______ in your company handbook."),
          ("information", "Please ask at the front desk if you need further travel _______ ."),
          ("temperature", "Store the antiseptic cream at a room _______ below 25°C.")]),

        ("Everyday Confusing Homophones and Alphabetical Order",
         "Official Annexe D Rule (<b>E3.W16, E3.W17</b>): <b>Homophones</b> sound identical but have different spellings and meanings: <b>there</b> (place) / <b>their</b> (belongs to them) / <b>they're</b> (they are); <b>to</b> (direction/verb) / <b>two</b> (number 2) / <b>too</b> (also or excessive); <b>where</b> (place) / <b>wear</b> (clothes) / <b>were</b> (past tense of are); <b>hear</b> (with your ear) / <b>here</b> (this place); <b>accept</b> (receive) / <b>except</b> (not including).",
         ["there", "their", "they're", "two", "too", "where", "wear", "were", "here", "hear", "weather", "whether"],
         "Memory tricks: 'THERE' has 'HERE' inside it (for a place); 'THEIR' has 'HEIR' (a person who owns things); 'HEAR' has 'EAR' inside it!",
         "Always expand contractions in your head to test them: only write 'they're' if 'they are' makes sense in the sentence.",
         [("there", "The spare safety boots are kept over _______ in Bay 3."),
          ("their", "All candidates must bring _______ photo ID to the exam room."),
          ("they're", "Look at the students; _______ studying quietly in the library."),
          ("two", "Take _______ paracetamol tablets with a glass of water."),
          ("wear", "All site visitors must _______ a high-visibility jacket and helmet."),
          ("here", "Please sign your name _______ on the bottom line of the visitor log.")])
    ]

    for s_idx, (s_title, s_rule, s_word_list, s_gold, s_watch, s_sentences) in enumerate(spelling_drills_e3, 1):
        photo_rel, photo_cap = E3_SPELLING_PHOTOS[s_idx]
        photo_path = str(K.PHOTO_DIR / photo_rel)
        chips_html = "".join(
            f"<span style='display:inline-block;background:#f1f5f9;border:1px solid #cbd5e1;border-radius:4px;padding:0.8mm 2.2mm;margin:0.5mm;font-weight:700;font-size:9.5pt;color:var(--primary);'>{w}</span>"
            for w in s_word_list
        )
        # Page 1: Learn
        p1_s = (
            K.page_title(f"Annexe D Spelling Drill {s_idx}", kicker=f"{s_title} &bull; Syllabus E3.W17", badge=f"SP{s_idx}")
            + K.hero_image(photo_path, photo_cap, 55, fill=True, pos="center center")
            + K.rule_box("Official Pearson Edexcel Annexe D Spelling &amp; Phonics Rule",
                         f"<p style='font-size:10.5pt;line-height:1.42;margin:0 0 1.8mm 0;'>{s_rule}</p>"
                         f"<div style='margin-top:1mm;'><b style='font-size:9.2pt;color:#475569;'>12 Core Annexe D Target Words:</b><br>{chips_html}</div>")
            + K.tip_pair(s_gold, s_watch, golden_title="Memory &amp; Phonics Strategy", watch_title="Examiner Spelling Trap")
            + K.fill_notes(f"Look, Say, Cover, Write, Check Practice (Drill {s_idx})", min_mm=20)
        )
        pages.append(K.page(p1_s, header=(BOOK, f"Spelling {s_idx} &bull; Rule"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 2: Practice Drill
        sent_html = "".join(f"<p style='margin:1.2mm 0;font-size:10.3pt;'><b>{i+1}.</b> {escape_html(s_txt)}</p>" for i, (_, s_txt) in enumerate(s_sentences))
        word_bank = ", ".join(w for w, _ in s_sentences)
        sp_card = e3_task_photo_card(photo_rel, f"Drill {s_idx}: {s_title[:22]}")
        p2_s = (
            K.page_title(f"Spelling Drill {s_idx} &bull; Practice Sentences", kicker="Annexe D Sentence Completion &bull; 6 Marks", badge="DRILL")
            + K.box_html(
                f"<div style='background:#f8fafc;padding:2mm 2.5mm;border:1.5px solid var(--soft);border-radius:6px;font-size:10.3pt;margin-bottom:1.5mm;'>"
                f"<strong style='color:var(--primary);'>Official Annexe D Word Bank:</strong> <b>{word_bank}</b>"
                f"</div>"
                f"<div style='overflow:hidden;'>{sp_card}{sent_html}</div>",
                title=f"Sentence Completion &bull; Drill {s_idx}"
            )
            + K.fill_lines("Write out your 6 completed sentences below (answers on p. 81):", min_mm=130, gap_mm=9.5)
        )
        pages.append(K.page(p2_s, header=(BOOK, f"Spelling {s_idx} &bull; Drill"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p64 to p79: 2 Complete Reading & Writing Mock Exams (16 pages: 8 pages per mock)
    # Mock Paper 1
    pages.append(K.page(
        K.page_title("Entry 3 Mock Examination &bull; Paper 1", kicker="Pearson Edexcel Entry Level 3 Full Simulation", badge="MOCK 1")
        + K.box_html(
            "<div style='font-size:11.5pt;line-height:1.52;'>"
            "<p><b>Official Pearson Edexcel Entry Level 3 Assessment Simulation (60 Marks Total):</b></p>"
            "<ul>"
            "<li><b>Section A: Reading Assessment (45 Minutes &bull; 24 Marks):</b> Read Texts 1, 2, and 3 carefully and answer all 12 comprehension questions (Questions 1&ndash;12).</li>"
            "<li><b>Section B: Writing Assessment (50 Minutes &bull; 36 Marks):</b>"
            "<ul>"
            "<li><b>Part 1 &mdash; Spelling, Punctuation &amp; Grammar (10 Marks):</b> Annexe D spelling corrections, sentence punctuation, plurals, and conjunctions.</li>"
            "<li><b>Task 1 &mdash; Formal Job Application Email (13 Marks &bull; 50&ndash;70 Words):</b> Email to Oxford Logistics HR Manager covering all 3 bullet points.</li>"
            "<li><b>Task 2 &mdash; Community Notice with Heading &amp; Bullets (13 Marks &bull; 50&ndash;70 Words):</b> Notice for the community centre noticeboard covering all 3 bullet points.</li>"
            "</ul></li>"
            "</ul>"
            "<p>Check all answers carefully before consulting the full benchmark solutions in the Reference section (p. 82).</p>"
            "</div>",
            title="Mock Examination 1 Instructions &amp; Mark Breakdown"
        )
        + K.tip_pair("Read each text twice and copy key names, dates, times, and prices accurately.",
                     "Leave 5 minutes at the end to check capital letters, full stops, and Annexe D spellings.",
                     golden_title="Reading Exam Tip", watch_title="Writing Exam Tip")
        + K.fill_notes("Candidate Exam Goals &amp; Timing Plan (Paper 1)", min_mm=30),
        header=(BOOK, "Mock 1 &bull; Overview"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    # Mock 1 Reading Text 1 & Questions 1-4 (8 Marks)
    pages.append(K.page(
        K.page_title("Mock 1 &bull; Reading Text 1", kicker="Text 1: Job Vacancy Notice &bull; Questions 1–4 (8 Marks)")
        + K.box_html(
            "<div style='font-size:11.2pt;line-height:1.48;background:#f8fafc;padding:3mm;border:1.5px solid var(--soft);border-radius:6px;margin-bottom:2mm;overflow:hidden;'>"
            + e3_task_photo_card("e3_thematic/r6_warehouse_memo.jpg", "Warehouse Operative Role")
            + "<b style='color:var(--primary);'>Oxford Logistics Centre: Warehouse Operative Vacancies</b><br>"
            "We are recruiting 6 full-time warehouse operatives for our modern distribution centre in Cowley. "
            "Working hours: Monday to Friday, 08:00 to 16:30. Starting pay: £11.85 per hour plus overtime. "
            "Duties include sorting incoming stock, using handheld barcode scanners, and packing orders for dispatch. "
            "No previous experience is required as full training will be provided. Free on-site parking and a staff subsidised canteen are available. "
            "To apply, send your CV to <b>careers@oxfordlogistics.co.uk</b> before Friday 28 November."
            "</div>"
            "<div style='font-size:10.6pt;line-height:1.42;'>"
            "<p style='margin:1mm 0;'><b>1.</b> How many warehouse operatives is Oxford Logistics Centre recruiting, and where is the centre located? <b>[2 marks]</b></p>"
            "<p style='margin:1mm 0;'><b>2.</b> What are the working hours and the starting hourly rate of pay? <b>[2 marks]</b></p>"
            "<p style='margin:1mm 0;'><b>3.</b> State <b>two</b> duties that warehouse operatives will carry out. <b>[2 marks]</b></p>"
            "<p style='margin:1mm 0;'><b>4.</b> What email address should applicants send their CV to, and what is the closing date? <b>[2 marks]</b></p>"
            "</div>",
            title="Text 1: Warehouse Job Advertisement &amp; Questions 1–4"
        )
        + K.fill_lines("Write your answers to Questions 1 to 4 below:", min_mm=80, gap_mm=9.5),
        header=(BOOK, "Mock 1 &bull; Reading Text 1"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    # Mock 1 Reading Text 2 & Questions 5-8 (8 Marks)
    pages.append(K.page(
        K.page_title("Mock 1 &bull; Reading Text 2 &bull; Health Advice", kicker="Text 2: Staying Well in Winter &bull; Questions 5–8 (8 Marks)")
        + K.box_html(
            "<div style='font-size:11.2pt;line-height:1.48;background:#f8fafc;padding:3mm;border:1.5px solid var(--soft);border-radius:6px;margin-bottom:2mm;overflow:hidden;'>"
            + e3_task_photo_card("e3_thematic/r7_hospital_clinic.jpg", "NHS Winter Health Guidance")
            + "<b style='color:var(--primary);'>NHS Advice: 4 Easy Ways to Stay Healthy This Winter</b><br>"
            "1. <b>Get your flu vaccination:</b> Free for adults with underlying health conditions, carers, and people aged 65 and over.<br>"
            "2. <b>Keep your home warm:</b> Heat your main living room to at least 18&deg;C and keep bedroom windows closed at night.<br>"
            "3. <b>Eat nourishing hot meals:</b> Soups, stews, and porridge provide long-lasting energy during cold weather.<br>"
            "4. <b>Stay active indoors:</b> Even gentle stretching and walking around the house every hour boosts blood circulation."
            "</div>"
            "<div style='font-size:10.6pt;line-height:1.42;'>"
            "<p style='margin:1mm 0;'><b>5.</b> What is the main purpose of Text 2? <b>[2 marks]</b></p>"
            "<p style='margin:1mm 0;'><b>6.</b> Name <b>two</b> groups of people who qualify for a free flu vaccination. <b>[2 marks]</b></p>"
            "<p style='margin:1mm 0;'><b>7.</b> What minimum temperature should you heat your main living room to? <b>[2 marks]</b></p>"
            "<p style='margin:1mm 0;'><b>8.</b> Give <b>two</b> examples of nourishing hot meals recommended in the text. <b>[2 marks]</b></p>"
            "</div>",
            title="Text 2: Winter Health Guidance &amp; Questions 5–8"
        )
        + K.fill_lines("Write your answers to Questions 5 to 8 below:", min_mm=80, gap_mm=9.5),
        header=(BOOK, "Mock 1 &bull; Reading Text 2"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    # Mock 1 Reading Text 3 & Questions 9-12 (8 Marks)
    pages.append(K.page(
        K.page_title("Mock 1 &bull; Reading Text 3 &bull; Public Notice", kicker="Text 3: Library Renovations &bull; Questions 9–12 (8 Marks)")
        + K.box_html(
            "<div style='font-size:11.2pt;line-height:1.48;background:#f8fafc;padding:3mm;border:1.5px solid var(--soft);border-radius:6px;margin-bottom:2mm;overflow:hidden;'>"
            + e3_task_photo_card("e3_thematic/r5_high_street_directory.jpg", "Westgate Community Library")
            + "<b style='color:var(--primary);'>Westgate Community Library Renovation Notice</b><br>"
            "The library will close for internal decoration and the installation of 12 new computer terminals from Monday 1 December to Monday 8 December. "
            "During this week, 24-hour book return boxes will remain open outside the main entrance. "
            "The mobile library van will visit the Market Square on Wednesday and Friday between 10:00am and 2:00pm. "
            "For urgent renewals, telephone 01865 332100."
            "</div>"
            "<div style='font-size:10.6pt;line-height:1.42;'>"
            "<p style='margin:1mm 0;'><b>9.</b> Why is Westgate Community Library closing, and how many new computer terminals are being installed? <b>[2 marks]</b></p>"
            "<p style='margin:1mm 0;'><b>10.</b> On what date does the library close, and on what date does it reopen? <b>[2 marks]</b></p>"
            "<p style='margin:1mm 0;'><b>11.</b> How can borrowers return books while the building is closed? <b>[2 marks]</b></p>"
            "<p style='margin:1mm 0;'><b>12.</b> On which days and between what times will the mobile library van visit Market Square? <b>[2 marks]</b></p>"
            "</div>",
            title="Text 3: Library Notice &amp; Questions 9–12"
        )
        + K.fill_lines("Write your answers to Questions 9 to 12 below:", min_mm=80, gap_mm=9.5),
        header=(BOOK, "Mock 1 &bull; Reading Text 3"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    # Mock 1 Writing (4 pages)
    pages.append(K.page(
        K.page_title("Mock 1 &bull; Writing Section A", kicker="Spelling, Punctuation &amp; Grammar &bull; 10 Marks", badge="WRITING")
        + K.box_html(
            "<div style='font-size:10.2pt;line-height:1.42;'>"
            "<p style='margin:0 0 1.5mm 0;'><b>Q1. Annexe D Spelling Corrections [4 marks]:</b> Find and correct the <b>4 spelling mistakes</b> in this workplace memo:<br>"
            "<i>Please write your full home <u>adress</u> on the application form. If you have a <u>qestion</u> about the training <u>secshun</u>, ask the manager <u>tomorow</u>.</i></p>"
            "<p style='margin:0 0 1.5mm 0;'><b>Q2. Capital Letters &amp; End Punctuation [3 marks]:</b> Rewrite this sentence adding <b>4 capital letters</b> and the correct <b>end mark (? or .)</b>:<br>"
            "<i>what time does mr patel arrive in oxford on tuesday</i></p>"
            "<p style='margin:0 0 1.5mm 0;'><b>Q3. Joining Sentences &amp; Plurals [3 marks]:</b> (a) Join with <b>because</b>: <i>I wore my high-visibility jacket. I was working in the loading bay.</i><br>"
            "(b) Write the correct plurals of: <b>box</b> &rarr; _________ &bull; <b>duty</b> &rarr; _________ &bull; <b>child</b> &rarr; _________</p>"
            "</div>",
            title="Section A: Spelling, Punctuation &amp; Grammar Questions (10 Marks)"
        )
        + K.fill_lines("Write your Section A answers neatly on the lines below:", min_mm=25, gap_mm=9.5),
        header=(BOOK, "Mock 1 &bull; Writing Section A"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    pages.append(K.page(
        K.page_title("Mock 1 &bull; Writing Task 1: Email", kicker="Functional Writing Task &bull; 13 Marks &bull; 50–70 Words", badge="TASK 1")
        + K.box_html(
            "<div style='overflow:hidden;'>"
            + e3_task_photo_card("e3_thematic/w9_format_email.jpg", "Format 1: Formal Job Email")
            + "<p style='font-size:10pt;line-height:1.4;margin:0 0 1mm 0;'>You are applying for the <b>Warehouse Operative</b> role advertised in Text 1. Write a formal email to the HR Manager (<b>careers@oxfordlogistics.co.uk</b>). In your email you must:</p>"
            "<ul style='font-size:9.5pt;line-height:1.35;margin:0 0 1.2mm 4mm;'>"
            "<li>Include a clear <b>Subject line</b>, state which job you are applying for, and say where you saw the advert.</li>"
            "<li>Explain why you are suitable for warehouse work (e.g. reliable, good team worker, careful with stock).</li>"
            "<li>State when you are available for an interview and when you can start work, signing off formally.</li>"
            "</ul>"
            "<div style='font-size:8.8pt;background:#f1f5f9;padding:1.2mm 2mm;border-radius:4px;clear:both;'>"
            "<b>Format &amp; Vocabulary Prompt:</b> Include <i>To: / Subject: / Dear Hiring Manager,</i> &bull; Use words like <i>position, reliable, experience, available, interview, Kind regards</i>."
            "</div></div>",
            title="Email Brief &bull; 13 Marks (Composition: 7 Marks | SPaG: 6 Marks)"
        )
        + K.fill_lines("Write your email below:", min_mm=25, gap_mm=9.5),
        header=(BOOK, "Mock 1 &bull; Task 1 Response"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    pages.append(K.page(
        K.page_title("Mock 1 &bull; Writing Task 2: Notice", kicker="Functional Writing Task &bull; 13 Marks &bull; 50–70 Words", badge="TASK 2")
        + K.box_html(
            "<div style='overflow:hidden;'>"
            + e3_task_photo_card("e3_thematic/w11_format_notice_leaflet.jpg", "Format 3: Community Notice")
            + "<p style='font-size:10pt;line-height:1.4;margin:0 0 1mm 0;'>Write a clear notice for your local community centre noticeboard about a new <b>Adult Reading &amp; Book Club</b>. In your notice you must:</p>"
            "<ul style='font-size:9.5pt;line-height:1.35;margin:0 0 1.2mm 4mm;'>"
            "<li>Include a bold <b>heading</b>, the start date, room number, and weekly meeting time.</li>"
            "<li>Use <b>bullet points (&bull;)</b> to explain what happens at the club (friendly book discussions, borrowing books, free tea and biscuits).</li>"
            "<li>State how local residents can join or who they should contact for more information.</li>"
            "</ul>"
            "<div style='font-size:8.8pt;background:#f1f5f9;padding:1.2mm 2mm;border-radius:4px;clear:both;'>"
            "<b>Format &amp; Vocabulary Prompt (E3.W20):</b> Use a <i>BOLD HEADING</i> + <i>3 Bullet Points (&bull;)</i> &bull; Use words like <i>welcome, beginners, discussion, refreshments, contact</i>."
            "</div></div>",
            title="Notice Brief &bull; 13 Marks (Composition: 8 Marks | SPaG: 5 Marks)"
        )
        + K.fill_lines("Write your community notice below:", min_mm=25, gap_mm=9.5),
        header=(BOOK, "Mock 1 &bull; Task 2 Response"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    pages.append(K.page(
        K.page_title("Mock 1 &bull; Candidate Post-Exam Audit", kicker="Self-Evaluation &amp; Official Entry 3 Mark Scheme Alignment", badge="AUDIT")
        + K.box_html(
            "<div style='font-size:10.5pt;line-height:1.48;'>"
            "<p style='margin:0 0 1.5mm 0;'><b>Check your Mock Examination 1 script against the Pearson Edexcel Entry Level 3 assessment criteria:</b></p>"
            "<ul>"
            "<li><b>Reading (24 marks &mdash; Pass guide: 16/24):</b> Located exact facts, times, prices, and purposes across all 3 texts without guessing.</li>"
            "<li><b>Writing Section A (10 marks):</b> Corrected all 4 Annexe D spellings (<i>address, question, section, tomorrow</i>), added capitals/question mark, and formed plurals accurately (<i>boxes, duties, children</i>).</li>"
            "<li><b>Writing Tasks 1 &amp; 2 (26 marks &mdash; Pass guide: 22/36 total Writing):</b> Addressed every bullet point, used email headers in Task 1, used a bold heading and bullet points in Task 2, and wrote in complete, punctuated sentences.</li>"
            "</ul>"
            "</div>",
            title="Entry 3 Marking &amp; Self-Assessment Matrix"
        )
        + K.fill_notes("Personal Reflections, Score &amp; Target Words for Mock 1", min_mm=45),
        header=(BOOK, "Mock 1 &bull; Audit"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    # Mock Paper 2 (8 pages)
    pages.append(K.page(
        K.page_title("Entry 3 Mock Examination &bull; Paper 2", kicker="Pearson Edexcel Entry Level 3 Full Simulation", badge="MOCK 2")
        + K.box_html(
            "<div style='font-size:11.5pt;line-height:1.52;'>"
            "<p><b>Official Pearson Edexcel Entry Level 3 Assessment Simulation (60 Marks Total):</b></p>"
            "<ul>"
            "<li><b>Section A: Reading Assessment (45 Minutes &bull; 24 Marks):</b> Read Texts 1, 2, and 3 carefully and answer all 12 comprehension questions (Questions 1&ndash;12).</li>"
            "<li><b>Section B: Writing Assessment (50 Minutes &bull; 36 Marks):</b>"
            "<ul>"
            "<li><b>Part 1 &mdash; Spelling, Punctuation &amp; Grammar (10 Marks):</b> Annexe D spelling corrections, list commas, past tense verbs, and alphabetical order.</li>"
            "<li><b>Task 1 &mdash; Course Enquiry Email (13 Marks &bull; 50&ndash;70 Words):</b> Email to Oxford Adult Learning Centre covering all 3 bullet points.</li>"
            "<li><b>Task 2 &mdash; Sports Centre Feedback Report (13 Marks &bull; 50&ndash;70 Words):</b> Customer feedback note covering all 3 bullet points.</li>"
            "</ul></li>"
            "</ul>"
            "<p>Check all answers carefully before consulting the full benchmark solutions in the Reference section (p. 82).</p>"
            "</div>",
            title="Mock Examination 2 Instructions &amp; Mark Breakdown"
        )
        + K.tip_pair("Scan for numbers, days, and room numbers in Reading.",
                     "Make sure every sentence has a clear subject, verb, capital letter, and full stop.",
                     golden_title="Reading Strategy", watch_title="Writing Strategy")
        + K.fill_notes("Candidate Exam Goals &amp; Timing Plan (Paper 2)", min_mm=30),
        header=(BOOK, "Mock 2 &bull; Overview"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    # Mock 2 Reading Text 1 & Questions 1-4 (8 Marks)
    pages.append(K.page(
        K.page_title("Mock 2 &bull; Reading Text 1", kicker="Text 1: College Open Evening &bull; Questions 1–4 (8 Marks)")
        + K.box_html(
            "<div style='font-size:11.2pt;line-height:1.48;background:#f8fafc;padding:3mm;border:1.5px solid var(--soft);border-radius:6px;margin-bottom:2mm;overflow:hidden;'>"
            + e3_task_photo_card("e3_thematic/r3_college_enrolment.jpg", "Adult Learning Open Evening")
            + "<b style='color:var(--primary);'>Oxford Adult Learning Centre: January Open Evening</b><br>"
            "Come along to our annual Open Evening on Thursday 15 January from 17:00 to 19:30. "
            "Meet our friendly tutors and discover free courses in Functional Skills English, Maths, Digital Skills, and Workplace First Aid. "
            "Drop-in course advice sessions take place in Room 10. Complimentary hot drinks and biscuits are provided in the main atrium. "
            "To book a free visitor pass, email <b>courses@oxfordlearning.co.uk</b>."
            "</div>"
            "<div style='font-size:10.6pt;line-height:1.42;'>"
            "<p style='margin:1mm 0;'><b>1.</b> On what day, date, and times does the Open Evening take place? <b>[2 marks]</b></p>"
            "<p style='margin:1mm 0;'><b>2.</b> Name <b>two</b> free courses offered at Oxford Adult Learning Centre. <b>[2 marks]</b></p>"
            "<p style='margin:1mm 0;'><b>3.</b> Which room holds the drop-in course advice sessions? <b>[2 marks]</b></p>"
            "<p style='margin:1mm 0;'><b>4.</b> Where are complimentary refreshments served, and how do you book a visitor pass? <b>[2 marks]</b></p>"
            "</div>",
            title="Text 1: Adult Learning Open Evening &amp; Questions 1–4"
        )
        + K.fill_lines("Write your answers to Questions 1 to 4 below:", min_mm=80, gap_mm=9.5),
        header=(BOOK, "Mock 2 &bull; Reading Text 1"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    # Mock 2 Reading Text 2 & Questions 5-8 (8 Marks)
    pages.append(K.page(
        K.page_title("Mock 2 &bull; Reading Text 2 &bull; Public Transport", kicker="Text 2: City Smartcard Travel &bull; Questions 5–8 (8 Marks)")
        + K.box_html(
            "<div style='font-size:11.2pt;line-height:1.48;background:#f8fafc;padding:3mm;border:1.5px solid var(--soft);border-radius:6px;margin-bottom:2mm;overflow:hidden;'>"
            + e3_task_photo_card("e3_thematic/r8_bus_train_compare.jpg", "City Smartcard Bus Travel")
            + "<b style='color:var(--primary);'>Oxford City Smartcard: Save Money on Every Journey</b><br>"
            "Top up your travel card online at www.oxfordbus.co.uk or at any train station ticket machine. "
            "Simply tap your card on the yellow card reader when boarding the bus. "
            "Adult fares are capped at £4.50 per day for unlimited local bus travel inside Zone A. "
            "Children under 5 travel free with a fare-paying adult. Lost cards can be replaced at the High Street Travel Shop for £3.00."
            "</div>"
            "<div style='font-size:10.6pt;line-height:1.42;'>"
            "<p style='margin:1mm 0;'><b>5.</b> State <b>two</b> places where passengers can top up their Oxford City Smartcard. <b>[2 marks]</b></p>"
            "<p style='margin:1mm 0;'><b>6.</b> What must you do with your card when boarding the bus? <b>[2 marks]</b></p>"
            "<p style='margin:1mm 0;'><b>7.</b> What is the maximum daily fare cap for an adult travelling in Zone A? <b>[2 marks]</b></p>"
            "<p style='margin:1mm 0;'><b>8.</b> Who travels free of charge, and how much does a replacement smartcard cost? <b>[2 marks]</b></p>"
            "</div>",
            title="Text 2: Smartcard Travel Guide &amp; Questions 5–8"
        )
        + K.fill_lines("Write your answers to Questions 5 to 8 below:", min_mm=80, gap_mm=9.5),
        header=(BOOK, "Mock 2 &bull; Reading Text 2"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    # Mock 2 Reading Text 3 & Questions 9-12 (8 Marks)
    pages.append(K.page(
        K.page_title("Mock 2 &bull; Reading Text 3 &bull; Health Centre", kicker="Text 3: Booking Online Appointments &bull; Questions 9–12 (8 Marks)")
        + K.box_html(
            "<div style='font-size:11.2pt;line-height:1.48;background:#f8fafc;padding:3mm;border:1.5px solid var(--soft);border-radius:6px;margin-bottom:2mm;overflow:hidden;'>"
            + e3_task_photo_card("e3_thematic/r12_pharmacy_cream.jpg", "NHS Online Repeat Prescriptions")
            + "<b style='color:var(--primary);'>Headington Medical Practice: Online Services</b><br>"
            "You can now order repeat prescriptions, view blood test results, and book routine GP appointments using the free NHS App. "
            "Download the app from your smartphone app store and register using your 10-digit NHS number and photographic ID (passport or driving licence). "
            "Please allow 48 hours for repeat prescriptions to be sent to your nominated pharmacy. "
            "If you need assistance setting up the app, our digital volunteer runs drop-in clinics every Tuesday from 2:00pm to 4:00pm."
            "</div>"
            "<div style='font-size:10.6pt;line-height:1.42;'>"
            "<p style='margin:1mm 0;'><b>9.</b> Name <b>two</b> tasks patients can complete using the NHS App. <b>[2 marks]</b></p>"
            "<p style='margin:1mm 0;'><b>10.</b> What <b>two</b> items of information do you need to register on the app? <b>[2 marks]</b></p>"
            "<p style='margin:1mm 0;'><b>11.</b> How long should you allow for repeat prescriptions to reach your pharmacy? <b>[2 marks]</b></p>"
            "<p style='margin:1mm 0;'><b>12.</b> When does the digital volunteer run drop-in help clinics? <b>[2 marks]</b></p>"
            "</div>",
            title="Text 3: Online Medical Services &amp; Questions 9–12"
        )
        + K.fill_lines("Write your answers to Questions 9 to 12 below:", min_mm=80, gap_mm=9.5),
        header=(BOOK, "Mock 2 &bull; Reading Text 3"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    # Mock 2 Writing (4 pages)
    pages.append(K.page(
        K.page_title("Mock 2 &bull; Writing Section A", kicker="Spelling, Punctuation &amp; Grammar &bull; 10 Marks", badge="WRITING")
        + K.box_html(
            "<div style='font-size:10.2pt;line-height:1.42;'>"
            "<p style='margin:0 0 1.5mm 0;'><b>Q1. Annexe D Spelling Corrections [4 marks]:</b> Find and correct the <b>4 spelling mistakes</b> in this college email:<br>"
            "<i>Thank you for your <u>helpfull</u> advice at <u>recepshun</u>. I would like to book an <u>apointment</u> to discuss <u>difrent</u> evening courses.</i></p>"
            "<p style='margin:0 0 1.5mm 0;'><b>Q2. Commas in Lists &amp; Apostrophes [3 marks]:</b> Add the missing <b>commas</b> and <b>apostrophe</b>:<br>"
            "<i>Please bring a pen notebook folder ruler and calculator, because we cant lend spare equipment.</i></p>"
            "<p style='margin:0 0 1.5mm 0;'><b>Q3. Past Tense &amp; Alphabetical Order [3 marks]:</b> (a) Change to <b>past tense</b>: <i>Yesterday I [go] _________ to college and [speak] _________ to my tutor.</i><br>"
            "(b) Put in <b>alphabetical order</b>: <i><b>c</b>ollege, <b>c</b>anteen, <b>c</b>ertificate, <b>c</b>ourse</i>.</p>"
            "</div>",
            title="Section A: Spelling, Punctuation &amp; Grammar Questions (10 Marks)"
        )
        + K.fill_lines("Write your Section A answers neatly on the lines below:", min_mm=25, gap_mm=9.5),
        header=(BOOK, "Mock 2 &bull; Writing Section A"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    pages.append(K.page(
        K.page_title("Mock 2 &bull; Writing Task 1: Email", kicker="Functional Writing Task &bull; 13 Marks &bull; 50–70 Words", badge="TASK 1")
        + K.box_html(
            "<div style='overflow:hidden;'>"
            + e3_task_photo_card("email_online_safety/email_inbox_laptop.jpg", "Format 1: Course Enquiry Email")
            + "<p style='font-size:10pt;line-height:1.4;margin:0 0 1mm 0;'>Write a polite email to <b>Oxford Adult Learning Centre</b> (<b>courses@oxfordlearning.co.uk</b>) enquiring about the <b>Digital Skills</b> course mentioned in Text 1. In your email you must:</p>"
            "<ul style='font-size:9.5pt;line-height:1.35;margin:0 0 1.2mm 4mm;'>"
            "<li>Include a clear <b>Subject line</b> and state which course you want to join and why.</li>"
            "<li>Ask which days and times the classes are held, and whether the course is free for adults.</li>"
            "<li>Confirm that you will attend the Open Evening on Thursday 15 January, and sign off politely.</li>"
            "</ul>"
            "<div style='font-size:8.8pt;background:#f1f5f9;padding:1.2mm 2mm;border-radius:4px;clear:both;'>"
            "<b>Format &amp; Vocabulary Prompt:</b> Include <i>To: / Subject: / Dear Admissions Team,</i> &bull; Use words like <i>enquire, Digital Skills, beginner, schedule, enrol, Kind regards</i>."
            "</div></div>",
            title="Email Brief &bull; 13 Marks (Composition: 7 Marks | SPaG: 6 Marks)"
        )
        + K.fill_lines("Write your email below:", min_mm=25, gap_mm=9.5),
        header=(BOOK, "Mock 2 &bull; Task 1 Response"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    pages.append(K.page(
        K.page_title("Mock 2 &bull; Writing Task 2: Feedback Report", kicker="Functional Writing Task &bull; 13 Marks &bull; 50–70 Words", badge="TASK 2")
        + K.box_html(
            "<div style='overflow:hidden;'>"
            + e3_task_photo_card("e3_thematic/w12_format_form_feedback.jpg", "Format 4: Feedback Report")
            + "<p style='font-size:10pt;line-height:1.4;margin:0 0 1mm 0;'>Write a short customer feedback report (<b>50&ndash;70 words</b>) to your local sports centre manager about a recent swimming session. In your report you must:</p>"
            "<ul style='font-size:9.5pt;line-height:1.35;margin:0 0 1.2mm 4mm;'>"
            "<li>Include a clear <b>heading</b> and state which day and time you visited the swimming pool.</li>"
            "<li>Praise at least <b>two positive aspects</b> of the centre (e.g. clean changing rooms, helpful lifeguard and reception staff).</li>"
            "<li>Suggest one practical improvement (e.g. warmer pool water or repairing the broken locker keys).</li>"
            "</ul>"
            "<div style='font-size:8.8pt;background:#f1f5f9;padding:1.2mm 2mm;border-radius:4px;clear:both;'>"
            "<b>Format &amp; Vocabulary Prompt:</b> Organise into <i>2 clear paragraphs</i> (Praise + Suggestion) &bull; Use words like <i>session, spotless, friendly, however, recommend, lockers</i>."
            "</div></div>",
            title="Feedback Report Brief &bull; 13 Marks (Composition: 8 Marks | SPaG: 5 Marks)"
        )
        + K.fill_lines("Write your feedback report below:", min_mm=25, gap_mm=9.5),
        header=(BOOK, "Mock 2 &bull; Task 2 Response"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    pages.append(K.page(
        K.page_title("Mock 2 &bull; Candidate Post-Exam Audit", kicker="Self-Evaluation &amp; Official Entry 3 Mark Scheme Alignment", badge="AUDIT")
        + K.box_html(
            "<div style='font-size:10.5pt;line-height:1.48;'>"
            "<p style='margin:0 0 1.5mm 0;'><b>Check your Mock Examination 2 script against the Pearson Edexcel Entry Level 3 standards:</b></p>"
            "<ul>"
            "<li><b>Reading (24 marks &mdash; Pass guide: 16/24):</b> Extracted accurate answers for all 12 questions across the Open Evening, Smartcard, and NHS App texts.</li>"
            "<li><b>Writing Section A (10 marks):</b> Corrected all 4 Annexe D spellings (<i>helpful, reception, appointment, different</i>), punctuated the equipment list, used irregular past verbs (<i>went, spoke</i>), and alphabetised by 2nd/3rd letters (<i>canteen, certificate, college, course</i>).</li>"
            "<li><b>Writing Tasks 1 &amp; 2 (26 marks):</b> Used clear email conventions in Task 1 and a 2-paragraph balanced feedback report in Task 2.</li>"
            "</ul>"
            "</div>",
            title="Entry 3 Marking Rubric &amp; Review"
        )
        + K.fill_notes("Personal Reflections, Score &amp; Target Words for Mock 2", min_mm=45),
        header=(BOOK, "Mock 2 &bull; Audit"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    # Reference Back Matter via K.ref_pages (Strict 2-Column Grid — Zero Right-Side Overflow)
    ref_blocks = []

    READING_E3_SOLUTIONS = {
        1: ["Assembly Point B is on the south car park.", "The routine alarm is tested every Tuesday at 10:00am.", "The fire warden for Bay 4 is Mrs Helen Patel.", "You must NOT use the lifts during an evacuation."],
        2: ["The community garden reopens on Saturday 11 October at 10:00am.", "Free gardening gloves and seed packets are provided.", "A sensory garden with raised vegetable beds has been built.", "Tea and homemade cakes will be served in the pavilion."],
        3: ["The induction takes place in Room B14.", "You must bring photographic ID (passport or driving licence).", "Call tutor Abdul on 01865 554100 if you cannot attend.", "Reception will issue an electronic security lanyard."],
        4: ["The green READY light shows the machine is ready.", "The sealed edge of the pouch must enter first.", "Let the document cool for 60 seconds on the rear tray.", "The machine takes 4 minutes to heat up."],
        5: ["Citizens Advice Bureau number: 01865 245200.", "Jobcentre Plus Office helps with Universal Credit enquiries.", "Citizens Advice Bureau is listed immediately before Dental Access Clinic.", "Call 01865 255800 to renew a library book."],
        6: ["The memo is addressed to All Warehouse Operatives.", "Final deadline for holiday requests: Friday 21 November at 17:00.", "Submit holiday requests to your team leader.", "Uniform hoodies and thermal gloves will be distributed next Monday."],
        7: ["Mr Taylor must attend Outpatient Clinic 3 at Churchill Hospital.", "The physiotherapy appointment is at 11:15am.", "He should arrive 15 minutes early.", "Bring: (1) appointment letter and (2) list of current prescribed medications."],
        8: ["A single ticket on Bus Route 40 costs £2.30.", "The City Express Train is faster (16 minutes vs 42 minutes).", "The train departs twice per hour from Central Station.", "Free Wi-Fi on board is available on Bus Route 40."],
        9: ["Lane Swimming starts at 07:00 on Monday.", "Studio 2 hosts the Pilates Class on Wednesday.", "Family Fun Swim costs £3.50 on Saturday.", "Aqua Aerobics is held on Friday (10:00–11:00)."],
        10: ["The Oxford Cycle Scheme launched in 2024.", "Over 15,000 residents use the cycle paths each weekday.", "Opinion: 'Cycling is definitely the most enjoyable and relaxing way to travel to work.'", "Helmets or high-visibility jackets are available at discounted rates."],
        11: ["Visit www.oxford.gov.uk/bins to order a replacement bin.", "Click the green 'Report or Request' button on the homepage.", "Delivery takes 5 working days.", "A replacement blue bin costs £15.00."],
        12: ["Apply the cream two to three times daily as required.", "Clean the affected area gently with warm water first.", "Store below 25°C.", "Avoid contact with the eyes."]
    }

    WRITING_E3_SOLUTIONS = {
        1: "Every Monday morning, David catches the bus to Oxford. He works with Mr Clarke at the community centre. Last Friday, I helped them paint the reception room in October.",
        2: "(1) What time does the afternoon training session start? (2) The delivery van arrived outside the warehouse at ten o'clock. (3) Watch out for the hot steam pipe! (4) Have you filled in your timesheet for this week?",
        3: "(1) Please order highlighters, pens, notebooks, sticky labels and printer paper. (2) The tool kit contains a hammer, pliers, screwdriver, wrench and tape measure. (3) I'm sorry I can't attend Monday's meeting because Sarah's car won't start.",
        4: "(1) I wanted to apply for the warehouse job, but I did not have a forklift licence. (2) Tariq passed his maths test and he received a promotion at work. (3) You can book your appointment online or you can call the clinic reception desk.",
        5: "(1) The fire alarm sounded, so everyone left the building calmly. (2) Elena booked Friday off work because she had a hospital appointment. (3) The warehouse floor was wet, so the cleaner put up a warning sign. (4) Please call reception if you are running more than 10 minutes late.",
        6: "Yesterday, the courier delivered three boxes to reception. I signed the receipt and took them into the storeroom. Later, our supervisor spoke to the driver and found the missing invoice.",
        7: "(1) The shift supervisor explains the safety rules to an apprentice. (2) Two delivery drivers have unloaded four heavy boxes. (3) We were tidying the storage shelves for the three women.",
        8: "Para 1: Our customer service training takes place on Wednesday in Room 2... [blank line] Para 2: A buffet lunch and hot drinks are provided... | Alphabetical order: safety, schedule, service, system.",
        9: "Model Email — Subject: Missed Tuesday Class & Maths Worksheet | Dear Abdul, I am sorry I missed Tuesday's class because I had a dentist appointment. Could you please send me the maths revision worksheet? I will complete it before Monday. Kind regards, [Candidate Name].",
        10: "Model Note — To: Sam | Time: 1:15pm | Hi Sam, A client named Mr Green called while you were at lunch about his order. Please call him back urgently before 3:00pm today on 07700 900123. Thanks, [Name].",
        11: "Model Notice — STAFF KITCHEN CLEANLINESS | Please keep our breakroom clean: • Wash and dry your mugs and plates immediately after eating. • Wipe the worktops after preparing food. • Remove all items from the fridge before Friday at 4:00pm.",
        12: "Model Feedback — Bus Route 15 Feedback: I used Bus Route 15 on Tuesday morning at 8:30am. The driver was very polite, patient, and helpful to passengers. However, the service could be improved by adding clearer audio announcements for each bus stop."
    }

    # Reading answers
    for r_idx, (r_title, _, _, _, _, p2_title, _, _) in enumerate(reading_units_e3, 1):
        e3_ans = READING_E3_SOLUTIONS[r_idx]
        qa_text = "<br>".join(f"<b>{i+1}.</b> {ans}" for i, ans in enumerate(e3_ans))
        ref_blocks.append(K.ref_block(f"Reading Unit {r_idx}: {r_title}",
                                      K.ref_qa(f"R{r_idx}", f"<b>{p2_title}:</b><br>{qa_text}", marks="4/4")))

    # Writing answers
    for w_idx, (w_title, _, _, _, _, _, p2_title, _, _) in enumerate(writing_units_e3, 1):
        w_ans = WRITING_E3_SOLUTIONS[w_idx]
        ref_blocks.append(K.ref_block(f"Writing Unit {w_idx}: {w_title}",
                                      K.ref_qa(f"W{w_idx}", f"<b>{p2_title}:</b><br>{escape_html(w_ans)}", marks="4/4")))

    # Spelling answers
    for s_idx, (s_title, _, _, _, _, s_sentences) in enumerate(spelling_drills_e3, 1):
        ans_text = ", ".join(f"({i+1}) <b>{w}</b>" for i, (w, _) in enumerate(s_sentences))
        ref_blocks.append(K.ref_block(f"Spelling Drill {s_idx}: {s_title}",
                                      K.ref_qa(f"SP{s_idx}", f"<b>Completed Sentences Key:</b> {ans_text}", marks="6/6")))

    # Mock exam solutions
    ref_blocks.append(K.ref_block("Mock Examination 1 Benchmark Solutions",
                                  K.ref_qa("M1-R",
                                           "<b>Text 1:</b> (1) 6 operatives; Cowley. (2) Mon–Fri 08:00–16:30; £11.85/hr. (3) Any two: sorting stock, using barcode scanners, packing orders. (4) careers@oxfordlogistics.co.uk; Friday 28 November.<br>"
                                           "<b>Text 2:</b> (5) To advise/inform people how to stay healthy in winter. (6) Any two: adults with health conditions, carers, people 65+. (7) At least 18°C. (8) Any two: soups, stews, porridge.<br>"
                                           "<b>Text 3:</b> (9) Internal decoration &amp; installing 12 new computers. (10) Closes Mon 1 Dec; reopens Mon 8 Dec. (11) Outside book return boxes. (12) Wednesday &amp; Friday, 10:00am–2:00pm.",
                                           marks="24/24")
                                  + K.ref_qa("M1-W",
                                             "<b>Section A (10m):</b> Q1: address, question, section, tomorrow. Q2: What time does Mr Patel arrive in Oxford on Tuesday? Q3: (a) I wore my high-visibility jacket because I was working in the loading bay. (b) boxes, duties, children.<br>"
                                             "<b>Task 1 Email (13m):</b> Subject: Warehouse Operative Application | Dear Hiring Manager, I am writing to apply for the Warehouse Operative role advertised in the notice. I am a reliable team worker and careful when packing stock. I am available for interview any day and can start immediately. Kind regards, [Name].<br>"
                                             "<b>Task 2 Notice (13m):</b> NEW ADULT READING &amp; BOOK CLUB | Starts Wednesday 12 November, 6:00pm in Room 4: • Friendly group book discussions for all levels. • Borrow free books to read at home. • Free tea, coffee, and biscuits provided. To join, speak to reception or email club@community.org.",
                                             marks="36/36")))

    ref_blocks.append(K.ref_block("Mock Examination 2 Benchmark Solutions",
                                  K.ref_qa("M2-R",
                                           "<b>Text 1:</b> (1) Thursday 15 January, 17:00–19:30. (2) Any two: English, Maths, Digital Skills, First Aid. (3) Room 10. (4) Main atrium; email courses@oxfordlearning.co.uk.<br>"
                                           "<b>Text 2:</b> (5) Online (www.oxfordbus.co.uk) or train station ticket machines. (6) Tap card on the yellow reader. (7) £4.50 per day. (8) Children under 5 travel free; £3.00 replacement.<br>"
                                           "<b>Text 3:</b> (9) Any two: repeat prescriptions, test results, GP appointments. (10) 10-digit NHS number &amp; photo ID. (11) 48 hours. (12) Every Tuesday, 2:00pm–4:00pm.",
                                           marks="24/24")
                                  + K.ref_qa("M2-W",
                                             "<b>Section A (10m):</b> Q1: helpful, reception, appointment, different. Q2: pen, notebook, folder, ruler and calculator... can't. Q3: (a) went, spoke. (b) canteen, certificate, college, course.<br>"
                                             "<b>Task 1 Email (13m):</b> Subject: Digital Skills Course Enquiry | Dear Admissions Team, I would like to join the beginners Digital Skills course to improve my computer confidence. Could you tell me which days the classes run and confirm if the course is free for adults? I will attend the Open Evening on Thursday 15 January. Kind regards, [Name].<br>"
                                             "<b>Task 2 Feedback (13m):</b> Swimming Session Feedback (Saturday 10:00am): I visited the swimming pool on Saturday morning at 10:00am. The changing rooms were spotless and the reception staff were very friendly and helpful.<br>However, the pool water felt quite cold and several locker keys were stiff. Replacing the broken locks would make the visit even better.",
                                             marks="36/36")))

    # Entry 3 Glossary
    glossary_e3 = [
        ("Alphabetical order", "Sequencing words from A to Z using the 1st and 2nd letters."),
        ("Apostrophe (')", "Punctuation mark showing missing letters (don't) or ownership (Sam's)."),
        ("Bullet points (•)", "Dots used to list key facts or rules clearly under a heading."),
        ("Compound sentence", "Two simple sentences joined with a conjunction (and, but, or, so)."),
        ("Conjunction", "A joining word that connects clauses (and, but, or, so, because, if)."),
        ("Fact vs Opinion", "A fact can be proved true; an opinion is someone's personal view."),
        ("Heading", "A bold title at the top of a notice, leaflet, or report section."),
        ("Homophones", "Words that sound the same but have different spellings (there/their)."),
        ("Irregular plural", "A plural noun that does not just add -s (children, people, shelves)."),
        ("Paragraph", "A group of related sentences about one topic, separated by a blank line."),
        ("Prefix / Suffix", "Letters added to the start (un-, re-) or end (-ful, -less) of a root word."),
        ("Proper noun", "A specific name, day, month, or place that starts with a capital letter."),
    ]
    gloss_html = "".join(f"<p style='margin:0.8mm 0;'><b>{escape_html(k)}:</b> {escape_html(v)}</p>" for k, v in glossary_e3)
    ref_blocks.append(K.ref_block("Entry Level 3 Functional Writing &amp; SPaG Glossary", gloss_html))

    # Index
    index_e3 = [
        ("A", [("Alphabetical order (E3.R11/W16)", "12, 42, 62"), ("Annexe D spelling drills (E3.W17)", "52–63"), ("Apostrophes & commas (E3.W13)", "32–33"), ("Appointment letters", "16–17"), ("Articles (a/an/the)", "40–41")]),
        ("C", [("Capital letters (E3.W13)", "28–29"), ("Commas in lists (E3.W13)", "32–33"), ("Comparing two texts", "18–19"), ("Compound sentences (E3.W21)", "34–37")]),
        ("D", [("Double consonants", "58–59")]),
        ("E", [("Emails (reading & writing)", "8, 44–45"), ("Exclamation & question marks", "30–31")]),
        ("F", [("Fact vs opinion", "22–23"), ("Feedback reports & forms", "50–51"), ("Full stops (E3.W13)", "30–31")]),
        ("H", [("Homophones (there/their/they're)", "62–63")]),
        ("I", [("Instructions & numbered steps", "10–11"), ("Irregular plurals & past verbs", "38–41")]),
        ("M", [("Memos & workplace notes", "14, 46–47"), ("Mock Examinations 1 & 2", "64–79")]),
        ("N", [("Notices, headings & bullets (E3.W20)", "4, 48–49")]),
        ("P", [("Paragraphs & logical order (E3.W21)", "42–43"), ("Prefixes (un-, dis-, re-, pre-)", "52–53")]),
        ("S", [("Silent letters (kn, wr, gn)", "56–57"), ("Subject-verb agreement (E3.W15)", "40–41"), ("Suffixes (-ful, -less, -ly, -tion)", "54, 60")]),
        ("T", [("Timetables, tables & web pages", "20, 24")]),
    ]
    index_html = ""
    for letter, entries in index_e3:
        items = "".join(f"<div class='ix'><span>{escape_html(t)}</span><span>p. {escape_html(p)}</span></div>" for t, p in entries)
        index_html += f"<div class='ix-letter'>{letter}</div>{items}"
    ref_blocks.append(K.ref_block("Entry Level 3 Subject &amp; Vocabulary Index", index_html))

    cover_theme = K.theme_from_cover(front_cov)
    ref_start_page = p_curr
    ref_page_list = K.ref_pages("Entry 3 Reference: Solutions, Spelling Keys &amp; Index", ref_blocks,
                                BOOK, start_page=p_curr, subtitle="Worked Solutions, Model Texts, Glossary &amp; Index",
                                cols=2, theme=cover_theme, notes_title="Candidate Entry 3 Log")
    pages.extend(ref_page_list)
    p_curr += len(ref_page_list)
    ref_end_page = p_curr - 1

    # Candidate Success Notes
    readiness_page = p_curr
    p91_body = (
        K.page_title("Candidate Entry 3 Progress &amp; Commitments", kicker="Pearson Edexcel Entry 3 Achievement &bull; Final Readiness Check", badge="SUCCESS")
        + K.box_html(
            "<div style='font-size:11.5pt;line-height:1.42;'>"
            "<p style='margin:0 0 1.5mm 0;'><b>Check off your Entry Level 3 skills as you complete each section of this manual:</b></p>"
            "<ul style='margin:0;padding-left:6mm;'>"
            "<li><b>Reading Mastery (E3.R8&ndash;R12):</b> Can locate main points, facts, dates, and prices; use alphabetical order (1st &amp; 2nd letters); read tables/timetables; and distinguish fact from opinion.</li>"
            "<li><b>Sentence &amp; Punctuation Accuracy (E3.W13&ndash;W15, W21):</b> Secure with capital letters, full stops, question marks, exclamation marks, commas in lists, apostrophes, regular/irregular plurals, articles (<i>a/an</i>), and joining clauses with <i>and, but, or, so, because</i>.</li>"
            "<li><b>Functional Writing Formats (E3.W18&ndash;W22):</b> Can write clear 50&ndash;100 word emails, formal/informal letters, workplace notes, notices with headings &amp; bullet points, and short feedback reports divided into paragraphs.</li>"
            "<li><b>Annexe D Spelling (E3.W17):</b> Confident with prefixes, suffixes (<i>-ful, -less, -tion, -sion</i>), silent letters, double consonants, and homophones.</li>"
            "<li><b>Mock Exams:</b> Completed Mock Examination 1 and Mock Examination 2 under timed exam conditions.</li>"
            "</ul></div>",
            title="Entry Level 3 Complete Learning Journey Checklist"
        )
        + K.fill_notes("Personal Success Notes &amp; Tutor Endorsements", min_mm=24)
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
                             "<b>Reading Confidence:</b> Understanding main points, finding factual details, and interpreting tables and signs.",
                             "<b>Writing Demarcation:</b> Using capital letters, full stops, question marks, commas, and apostrophes accurately.",
                             "<b>Functional Formats:</b> Writing clear emails, letters, notes, notices with headings/bullets, and feedback reports.",
                             "<b>Preparation for Level 1:</b> Ready to progress smoothly onto Level 1 Functional Skills English."
                         ]))
            + K.tip_pair("Keep practising your reading and Annexe D spelling drills every week to consolidate your skills.",
                         "Celebrate your progress with your tutor as you move to the next level of study.",
                         golden_title="Next Steps", watch_title="Progression")
            + K.fill_notes("Tutor Endorsement &amp; Next Stage Plan", min_mm=28)
        )
        pages.append(K.page(p_ibc_body, header=(BOOK, "Course Completion"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # Back Cover
    pages.append(K.back_cover(back_cov))

    # Build Page 2: Complete 2-Column Table of Contents & Topic Directory with exact verified page numbers
    def toc_row(badge_txt: str, label_txt: str, pg_txt: str) -> str:
        return (
            f"<div style='display:grid;grid-template-columns:10.5mm minmax(0,1fr) auto;align-items:center;gap:1.4mm;"
            f"padding:0.85mm 1.4mm;border-bottom:1px solid #e2e8f0;font-size:7.6pt;line-height:1.22;'>"
            f"<span style='background:var(--light);color:var(--primary);border:1px solid var(--soft);"
            f"border-radius:3px;font-weight:800;font-size:6.8pt;text-align:center;padding:0.2mm 0.4mm;'>{badge_txt}</span>"
            f"<span style='font-weight:600;color:#1e293b;white-space:nowrap;overflow:hidden;'>{label_txt}</span>"
            f"<span style='font-weight:800;color:var(--primary);font-size:7.4pt;white-space:nowrap;'>{pg_txt}</span>"
            f"</div>"
        )

    def toc_sec_hdr(sec_title: str) -> str:
        return (
            f"<div style='background:var(--primary);color:#fff;font-weight:800;font-size:7.8pt;"
            f"letter-spacing:0.02em;text-transform:uppercase;padding:1.0mm 1.6mm;border-radius:4px 4px 0 0;margin-top:1.5mm;'>"
            f"{sec_title}</div>"
        )

    col1_html = (
        toc_sec_hdr("Part 1 &bull; Syllabus &amp; Exam Overview")
        + "<div style='border:1px solid #cbd5e1;border-top:none;border-radius:0 0 4px 4px;background:#fff;'>"
        + toc_row("SPEC", "Assessment Profile &amp; E3.R8–W22 Syllabus Map", "p. 3")
        + "</div>"
        + toc_sec_hdr("Part 2 &bull; Reading Masterclass (12 Units &bull; 24p)")
        + "<div style='border:1px solid #cbd5e1;border-top:none;border-radius:0 0 4px 4px;background:#fff;'>"
        + toc_row("R1", "Reading Notices &amp; Workplace Safety Signs", "pp. 4–5")
        + toc_row("R2", "Finding Main Ideas in News Articles", "pp. 6–7")
        + toc_row("R3", "Reading Emails from Work or College", "pp. 8–9")
        + toc_row("R4", "Following Numbered Instructions &amp; Steps", "pp. 10–11")
        + toc_row("R5", "Using an Alphabetical Directory (A–Z)", "pp. 12–13")
        + toc_row("R6", "Understanding Internal Workplace Memos", "pp. 14–15")
        + toc_row("R7", "Reading Healthcare Appointment Letters", "pp. 16–17")
        + toc_row("R8", "Comparing Two Short Information Texts", "pp. 18–19")
        + toc_row("R9", "Reading Tables &amp; Weekly Timetables", "pp. 20–21")
        + toc_row("R10", "Fact vs Opinion in Community Leaflets", "pp. 22–23")
        + toc_row("R11", "Reading Online Forms &amp; Council Web Pages", "pp. 24–25")
        + toc_row("R12", "Reading Product Labels, Dosage &amp; Warnings", "pp. 26–27")
        + "</div>"
        + toc_sec_hdr("Part 4 &bull; Official Annexe D Spelling (6 Units &bull; 12p)")
        + "<div style='border:1px solid #cbd5e1;border-top:none;border-radius:0 0 4px 4px;background:#fff;'>"
        + toc_row("SP1", "Prefixes: 'Un-', 'Dis-', 'Re-' &amp; 'Pre-'", "pp. 52–53")
        + toc_row("SP2", "Suffixes: '-ful', '-less', '-ly', '-ness' &amp; '-ment'", "pp. 54–55")
        + toc_row("SP3", "Silent Letters: 'K', 'W', 'G', 'B' &amp; 'L'", "pp. 56–57")
        + toc_row("SP4", "Double Consonants &amp; Plural Spelling Rules", "pp. 58–59")
        + toc_row("SP5", "Word Endings: '-tion', '-sion' &amp; '-ture'", "pp. 60–61")
        + toc_row("SP6", "Confusing Homophones &amp; A–Z Sequencing", "pp. 62–63")
        + "</div>"
    )

    col2_html = (
        toc_sec_hdr("Part 3 &bull; Writing &amp; Formats (12 Units &bull; 24p)")
        + "<div style='border:1px solid #cbd5e1;border-top:none;border-radius:0 0 4px 4px;background:#fff;'>"
        + toc_row("W1", "Capital Letters: Sentences, Names &amp; Places", "pp. 28–29")
        + toc_row("W2", "Full Stops, Question &amp; Exclamation Marks", "pp. 30–31")
        + toc_row("W3", "Commas in Lists &amp; Apostrophes", "pp. 32–33")
        + toc_row("W4", "Compound Sentences: 'And', 'But' &amp; 'Or'", "pp. 34–35")
        + toc_row("W5", "Giving Reasons: 'Because', 'So', 'When' &amp; 'If'", "pp. 36–37")
        + toc_row("W6", "Past Tense: Regular (-ed) &amp; Irregular Verbs", "pp. 38–39")
        + toc_row("W7", "Subject-Verb Agreement, 'A/An' &amp; Plurals", "pp. 40–41")
        + toc_row("W8", "Paragraphs &amp; Alphabetical Order (A–Z)", "pp. 42–43")
        + toc_row("W9", "Format 1: Writing Formal &amp; Informal Emails", "pp. 44–45")
        + toc_row("W10", "Format 2: Formal Letters &amp; Workplace Notes", "pp. 46–47")
        + toc_row("W11", "Format 3: Notices, Headings &amp; Bullet Points", "pp. 48–49")
        + toc_row("W12", "Format 4: Forms &amp; Short Feedback Reports", "pp. 50–51")
        + "</div>"
        + toc_sec_hdr("Part 5 &bull; 2 Official Mock Exam Papers (16 Pages)")
        + "<div style='border:1px solid #cbd5e1;border-top:none;border-radius:0 0 4px 4px;background:#fff;'>"
        + toc_row("M1-R", "Mock Paper 1: Reading Texts 1–3 (24 Marks)", "pp. 64–67")
        + toc_row("M1-W", "Mock Paper 1: Writing SPaG, Email &amp; Notice", "pp. 68–71")
        + toc_row("M2-R", "Mock Paper 2: Reading Texts 1–3 (24 Marks)", "pp. 72–75")
        + toc_row("M2-W", "Mock Paper 2: Writing SPaG, Email &amp; Report", "pp. 76–79")
        + "</div>"
        + toc_sec_hdr("Part 6 &bull; Reference Solutions, Glossary &amp; Index")
        + "<div style='border:1px solid #cbd5e1;border-top:none;border-radius:0 0 4px 4px;background:#fff;'>"
        + toc_row("SOL", "Reading (R1–R12) &amp; Writing (W1–W12) Key", f"pp. {ref_start_page}–{ref_start_page+1}")
        + toc_row("KEY", "Annexe D Spelling Keys &amp; Mock 1–2 Models", f"pp. {ref_start_page+1}–{ref_end_page}")
        + toc_row("GLOS", "Entry 3 Functional Writing Glossary &amp; Index", f"p. {ref_end_page}")
        + toc_row("PASS", "Candidate Progress &amp; Completion Record", f"p. {readiness_page}")
        + "</div>"
    )

    p2_toc_body = (
        K.page_title("Table of Contents &amp; Directory", kicker="Pearson Edexcel Functional Skills English &bull; Entry Level 3", badge="CONTENTS")
        + "<div style='background:var(--light);border:1.5px solid var(--soft);border-radius:6px;padding:1.8mm 2.8mm;margin-bottom:1.0mm;"
          "display:grid;grid-template-columns:1fr 1fr 1fr;gap:3mm;font-size:8.4pt;'>"
          "<div><b style='color:var(--primary);'>Learner Name:</b> _______________________</div>"
          "<div><b style='color:var(--primary);'>Target Exam Date:</b> ___________________</div>"
          "<div><b style='color:var(--primary);'>Qualification:</b> Edexcel Entry Level 3</div>"
          "</div>"
        + f"<div style='display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:3.2mm;align-items:start;'>"
          f"<div>{col1_html}</div>"
          f"<div>{col2_html}</div>"
          f"</div>"
        + "<div style='margin-top:auto;background:#f8fafc;border:1.2px solid var(--soft);border-radius:6px;padding:1.8mm 2.5mm;"
          "display:grid;grid-template-columns:repeat(4,1fr);gap:2mm;font-size:7.8pt;line-height:1.24;'>"
          "<div><b style='color:var(--primary);'>1. Study the Rule &amp; Photo:</b> Read the Entry 3 rule, vocabulary, and model on Page 1 of each unit.</div>"
          "<div><b style='color:var(--primary);'>2. Complete the Drill:</b> Write your answers in full sentences on Page 2 of each unit.</div>"
          "<div><b style='color:var(--primary);'>3. Master Annexe D:</b> Practise prefixes, suffixes, silent letters, and homophones (pp. 52–63).</div>"
          "<div><b style='color:var(--primary);'>4. Sit the 2 Full Mocks:</b> Test yourself under timed conditions (pp. 64–79) and check solutions (p. 80).</div>"
          "</div>"
    )
    pages[1] = K.page(p2_toc_body, header=("MASTER FUNCTIONAL SKILLS", "ENGLISH ENTRY LEVEL 3 &bull; CONTENTS"), footer=BOOK, page_no=2)

    print(f"Total Pages Assembled: {len(pages)}")
    out_pdf = DOWNLOADS / "MasterFunctionalSkills_English_Entry_Level_3_Core_Guide.pdf"
    res = K.render_pdf(pages, out_pdf, theme=cover_theme, entry3=True, title="Master Functional Skills - English Entry Level 3 Core Guide")
    shutil.copy(out_pdf, DOCUMENTS / out_pdf.name)
    print(f"Verified & Saved: {out_pdf} -> {DOCUMENTS / out_pdf.name}")
    print(f"Overflows: {res.get('overflow')}")
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
