#!/usr/bin/env python3
"""
build_mfs_spag_mastery.py
=============================================================================
Master Functional Skills: Dyslexia-Friendly SPaG Book Generator
Compiles 3 Complete 36-Page SPaG Mastery Handbooks:
  1. MasterFunctionalSkills_SPaG_Level_2_Mastery.pdf (Deep Navy)
  2. MasterFunctionalSkills_SPaG_Level_1_Mastery.pdf (Emerald Teal)
  3. MasterFunctionalSkills_SPaG_Entry_Level_3_Mastery.pdf (Crimson Ruby)

Architecture:
  - 100% Dyslexia-Friendly: Warm Cream Canvas (#FDFBF7), Deep Slate Text (#1F2937),
    Lexend & Atkinson Hyperlegible Sans-Serif Fonts, Ragged-Right (NEVER Justified),
    Line-Height 1.48–1.52, Chunked Left-Bordered Color Cards.
  - Raymond Murphy 'Grammar in Use' Facing Two-Page Spread per Unit:
    * Left Page: Situational Anchor [A], Structural Formula & Syntax [B],
                 Compare & Contrast [C], Examiner Golden Rule & Memory Hook [D]
    * Right Page: Exercise 1 (Recognition/Discrimination), Exercise 2 (Cloze/Transformation),
                  Exercise 3 (Forensic Workplace Proofreading), Exercise 4 (Applied Writing Task)
  - Exact 36-Page Sequential Layout:
    * Page 1: Full-Bleed Front Cover
    * Page 2: Inside Cover, Candidate Details & Dyslexia Statement
    * Page 3: Table of Contents & Unit Progress Matrix
    * Page 4: Baseline Diagnostic Assessment (10 Questions + Scoring Matrix)
    * Pages 5–26: Units 1 to 11 (2 Pages per Unit = 22 Pages)
    * Pages 27–28: Master Spelling Rules & High-Yield Vocabulary (2 Pages)
    * Pages 29–30: Mixed Exam Proofreading Mock (2 Pages)
    * Pages 31–34: Full Complete Answer Key (4 Pages)
    * Page 35: Student SPaG Self-Audit Checklist & Progress Tracker
    * Page 36: Full-Bleed High-Impact Back Cover

Output Destinations:
  - /home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk/assets/downloads/
  - /home/subi/Documents/
=============================================================================
"""

import os
import sys
import time
import shutil
import subprocess

# Ensure local imports work regardless of launch directory
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from spag_styles import SHARED_CSS, LEVEL_THEMES
import spag_content_l1
import spag_content_l2
import spag_content_e3
import spag_content_extras
import spag_unit_models
import spag_data_l1
import spag_data_l2

PROJECT_DIR = "/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk"
DOWNLOADS_DIR = os.path.join(PROJECT_DIR, "assets", "downloads")
DOCUMENTS_DIR = "/home/subi/Documents"
SCRATCH_DIR = os.path.join(PROJECT_DIR, "scratch", "spag_build")
CHROME_BIN = "/usr/lib/chromium/chromium"

os.makedirs(DOWNLOADS_DIR, exist_ok=True)
os.makedirs(DOCUMENTS_DIR, exist_ok=True)
os.makedirs(SCRATCH_DIR, exist_ok=True)


# =============================================================================
# HELPER RENDERING FUNCTIONS
# =============================================================================

def render_front_cover(theme):
    """Generates Page 1: Full-bleed Front Cover."""
    return f"""
<div class="page cover-page" style="background: linear-gradient(145deg, {theme['cover_grad_start']} 0%, {theme['cover_grad_mid']} 55%, {theme['cover_grad_end']} 100%);">
  <div style="padding: 18mm 18mm 0 18mm;">
    <!-- Top Brand Header -->
    <div style="display:flex; justify-content:space-between; align-items:center; border-bottom: 1.5px solid rgba(255,255,255,0.25); padding-bottom:12px;">
      <div>
        <div style="font-family:'Montserrat',sans-serif; font-size:13pt; font-weight:900; letter-spacing:2.5px; color:#ffffff;">MASTER FUNCTIONAL SKILLS</div>
        <div style="font-size:7.5pt; font-weight:700; letter-spacing:1.5px; color:#f59e0b; margin-top:2px;">OFFICIAL OFQUAL SPECIFICATION &bull; 2026/2027 CURRICULUM</div>
      </div>
      <div style="background:{theme['badge_bg']}; color:#ffffff; font-family:'Montserrat',sans-serif; font-weight:900; font-size:8.5pt; padding:6px 14px; border-radius:20px; letter-spacing:1px; border:1px solid rgba(255,255,255,0.3); box-shadow:0 2px 8px rgba(0,0,0,0.3);">
        {theme['title'].upper()}
      </div>
    </div>

    <!-- Knockout Level Graphic -->
    <div style="margin-top:22mm;">
      <div style="font-family:'Montserrat',sans-serif; font-size:38pt; font-weight:900; color:rgba(255,255,255,0.08); letter-spacing:4px; line-height:0.9; text-transform:uppercase;">
        {theme['code']} SPAG
      </div>
      <div style="margin-top:-22px; font-family:'Montserrat',sans-serif; font-size:24pt; font-weight:900; color:#ffffff; line-height:1.15; letter-spacing:0.5px;">
        SPELLING, PUNCTUATION<br>&amp; GRAMMAR MASTERY
      </div>
      <div style="font-size:12pt; font-weight:600; color:#fde68a; margin-top:8px; letter-spacing:0.5px;">
        The Complete 2-Page Spread Self-Study &amp; Revision Workbook
      </div>
      <div style="font-size:8.5pt; color:rgba(255,255,255,0.85); margin-top:6px; max-width:160mm; line-height:1.5;">
        Calibrated to Ofqual standards using Raymond Murphy 'Grammar in Use' pedagogy. Specially engineered with dyslexia-friendly typography, anti-glare cream canvas, and chunked cognitive layouts.
      </div>
    </div>

    <!-- Key Feature Badges Grid -->
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-top:18mm;">
      <div style="background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.18); border-left:4px solid #38bdf8; border-radius:6px; padding:8px 12px;">
        <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:8.2pt; color:#ffffff;">MURPHY 2-PAGE SPREADS</div>
        <div style="font-size:7.5pt; color:rgba(255,255,255,0.8); margin-top:2px;">Visual theory on the left; progressive 4-tier practice drills on the right.</div>
      </div>
      <div style="background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.18); border-left:4px solid #34d399; border-radius:6px; padding:8px 12px;">
        <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:8.2pt; color:#ffffff;">DYSLEXIA-FRIENDLY CANVAS</div>
        <div style="font-size:7.5pt; color:rgba(255,255,255,0.8); margin-top:2px;">Soft #FDFBF7 cream background, Lexend font, and left-aligned text.</div>
      </div>
      <div style="background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.18); border-left:4px solid #f472b6; border-radius:6px; padding:8px 12px;">
        <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:8.2pt; color:#ffffff;">FORENSIC PROOFREADING</div>
        <div style="font-size:7.5pt; color:rgba(255,255,255,0.8); margin-top:2px;">Authentic workplace memos, emails, and reports with exact error counts.</div>
      </div>
      <div style="background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.18); border-left:4px solid #fbbf24; border-radius:6px; padding:8px 12px;">
        <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:8.2pt; color:#ffffff;">FULL COMPLETE ANSWER KEY</div>
        <div style="font-size:7.5pt; color:rgba(255,255,255,0.8); margin-top:2px;">Exhaustive 4-page answers with examiner commentary and model rewrites.</div>
      </div>
    </div>
  </div>

  <!-- Bottom Strip -->
  <div style="background:rgba(0,0,0,0.45); border-top:1px solid rgba(255,255,255,0.15); padding:10mm 18mm; display:flex; justify-content:space-between; align-items:center;">
    <div>
      <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:8pt; letter-spacing:1px; color:#ffffff;">PEARSON EDEXCEL &bull; CITY &amp; GUILDS &bull; NCFE &bull; HIGHFIELD</div>
      <div style="font-size:7.2pt; color:rgba(255,255,255,0.7); margin-top:2px;">masterfunctionalskills.co.uk &bull; {theme.get('page_count_label', 'Complete 100-Page Curriculum Manual')}</div>
    </div>
    <div style="text-align:right;">
      <span style="background:rgba(255,255,255,0.15); color:#ffffff; padding:4px 10px; border-radius:4px; font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.5pt; letter-spacing:0.5px;">2026/2027 EDITION</span>
    </div>
  </div>
</div>
"""


def render_inside_cover(theme):
    """Generates Page 2: Inside Cover & Centre / Candidate details."""
    return f"""
<div class="page" style="--theme-primary:{theme['primary']}; --theme-secondary:{theme['secondary']};">
  <div class="unit-page-header">
    <div class="brand-title">MASTER FUNCTIONAL SKILLS &bull; PUBLISHING INFORMATION</div>
    <div class="strand-badge">{theme['full_name']}</div>
  </div>

  <div style="margin-bottom:10px;">
    <h1 style="font-family:'Montserrat',sans-serif; font-size:14pt; font-weight:900; color:{theme['primary']}; margin:0 0 3px 0;">
      Candidate &amp; Examination Centre Information
    </h1>
    <p style="font-size:8pt; color:#64748b; margin:0 0 8px 0;">Please complete the details below before commencing the baseline diagnostic assessment.</p>
  </div>

  <!-- Candidate Details Form Box -->
  <div style="background:#ffffff; border:1.5px solid #cbd5e1; border-radius:6px; padding:10px 14px; margin-bottom:12px;">
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; font-size:8.2pt;">
      <div><strong>Candidate Full Name:</strong> <div style="border-bottom:1px dashed #94a3b8; height:20px; margin-top:3px;"></div></div>
      <div><strong>Candidate Reference / ULN:</strong> <div style="border-bottom:1px dashed #94a3b8; height:20px; margin-top:3px;"></div></div>
      <div><strong>Exam Centre Name:</strong> <div style="border-bottom:1px dashed #94a3b8; height:20px; margin-top:3px;"></div></div>
      <div><strong>Centre Number:</strong> <div style="border-bottom:1px dashed #94a3b8; height:20px; margin-top:3px;"></div></div>
      <div><strong>Course / Training Cohort:</strong> <div style="border-bottom:1px dashed #94a3b8; height:20px; margin-top:3px;"></div></div>
      <div><strong>Tutor / Assessor Name:</strong> <div style="border-bottom:1px dashed #94a3b8; height:20px; margin-top:3px;"></div></div>
    </div>
  </div>

  <!-- Dyslexia Architecture Statement -->
  <div class="card-anchor" style="border-left-color:{theme['primary']}; margin-bottom:10px;">
    <div class="card-title" style="color:{theme['primary']};">
      <span>DYSLEXIA-FRIENDLY ACCESSIBILITY &amp; TYPOGRAPHY STATEMENT</span>
    </div>
    <p style="margin:0 0 5px 0; font-size:8.1pt;">
      This publication has been developed strictly adhering to British Dyslexia Association and Ofqual accessibility standards. Reading efficiency and cognitive ease are maximized through the following evidence-based features:
    </p>
    <ul style="margin:0 0 0 16px; padding:0; font-size:8pt; line-height:1.45;">
      <li><strong>Soft Cream Canvas (#FDFBF7):</strong> Eliminates the harsh optical glare and visual stress associated with high-contrast pure white paper.</li>
      <li><strong>Lexend &amp; Atkinson Hyperlegible Typography:</strong> Engineered with distinct character shapes to prevent common mirror-confusion traps (b/d/p/q).</li>
      <li><strong>Ragged-Right Left Alignment:</strong> Text is never justified, completely eradicating irregular letter spacing and disorienting 'rivers of white space'.</li>
      <li><strong>Generous Leading (1.5) &amp; Letter-Spacing (0.025em):</strong> Enhances horizontal tracking and prevents unintended line skipping.</li>
      <li><strong>Chunked Left-Bordered Cards:</strong> Key grammatical categories are color-coded (Context: Blue; Formula: Slate; Pitfall: Red; Golden Rule: Amber).</li>
    </ul>
  </div>

  <!-- The Murphy Method Box -->
  <div class="card-formula" style="margin-bottom:10px;">
    <div class="card-title">THE RAYMOND MURPHY 'GRAMMAR IN USE' 2-PAGE SPREAD METHOD</div>
    <p style="margin:0 0 4px 0; font-size:8.1pt;">
      Each unit is structured as an interconnected facing 2-page spread:
    </p>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; font-size:7.8pt;">
      <div style="background:#f8fafc; padding:6px 8px; border-radius:4px; border:1px solid #e2e8f0;">
        <strong style="color:{theme['primary']};">LEFT-HAND PAGE (Theory &amp; Context):</strong><br>
        [A] Situational Workplace Anchor<br>
        [B] Syntax Architecture &amp; Formulas<br>
        [C] Compare &amp; Contrast (Bad vs Good vs Why)<br>
        [D] Examiner Golden Rule &amp; Mnemonic
      </div>
      <div style="background:#f8fafc; padding:6px 8px; border-radius:4px; border:1px solid #e2e8f0;">
        <strong style="color:{theme['primary']};">RIGHT-HAND PAGE (Progressive Drills):</strong><br>
        [Ex 1] Recognition / Binary Discrimination<br>
        [Ex 2] Controlled Cloze / Sentence Completion<br>
        [Ex 3] Forensic Workplace Proofreading<br>
        [Ex 4] Real-World Functional Writing Task
      </div>
    </div>
  </div>

  <!-- Publishing & Copyright Notice -->
  <div style="margin-top:auto; font-size:7.3pt; color:#64748b; border-top:1px solid #e2e8f0; padding-top:6px;">
    <strong>Published by:</strong> Master Functional Skills (masterfunctionalskills.co.uk) &bull; London, United Kingdom.<br>
    &copy; 2026 Master Functional Skills. All rights reserved. Registered examination training provider and educational publisher.
  </div>

  <div class="page-footer">
    <div>{theme['title']} &bull; Inside Cover &amp; Candidate Verification</div>
    <div class="page-num">Page 2</div>
  </div>
</div>
"""


def render_toc(theme, units_list):
    """Generates Page 3: Table of Contents & Unit Progress Matrix."""
    rows_html = ""
    start_page = 5
    for u in units_list:
        p_range = f"pp. {start_page}–{start_page+1}"
        fmt = u.get("format", "Vocational Document")
        rows_html += f"""
        <tr>
          <td style="font-weight:700; color:{theme['primary']}; width:16%;">Unit {u['unit']}</td>
          <td style="font-weight:600; width:44%;">{u['title']}</td>
          <td style="color:#64748b; font-size:7.4pt; width:20%;">{fmt}</td>
          <td style="text-align:center; font-weight:700; width:10%;">{p_range}</td>
          <td style="text-align:center; width:10%;"><span class="rag-pill rag-red"></span><span class="rag-pill rag-amber"></span><span class="rag-pill rag-green"></span></td>
        </tr>
        """
        start_page += 2

    return f"""
<div class="page" style="--theme-primary:{theme['primary']}; --theme-secondary:{theme['secondary']};">
  <div class="unit-page-header">
    <div class="brand-title">SYLLABUS &bull; TABLE OF CONTENTS</div>
    <div class="strand-badge">{theme['code']} Curriculum Map</div>
  </div>

  <div style="margin-bottom:8px;">
    <h1 style="font-family:'Montserrat',sans-serif; font-size:13.5pt; font-weight:900; color:{theme['primary']}; margin:0 0 2px 0;">
      Course Syllabus &amp; Progress Tracker
    </h1>
    <p style="font-size:8pt; color:#64748b; margin:0 0 6px 0;">Track your mastery across all 11 units, master spelling patterns, mock exams, and answer keys.</p>
  </div>

  <table class="mfs-table">
    <thead>
      <tr>
        <th>Section</th>
        <th>Unit / Topic Focus</th>
        <th>Exam Format</th>
        <th style="text-align:center;">Pages</th>
        <th style="text-align:center;">Confidence</th>
      </tr>
    </thead>
    <tbody>
      <tr style="background:#f1f5f9;">
        <td style="font-weight:800; color:{theme['primary']};">Diagnostic</td>
        <td style="font-weight:700;" colspan="2">Baseline Diagnostic Assessment (10 Priority Questions)</td>
        <td style="text-align:center; font-weight:700;">Page 4</td>
        <td style="text-align:center;">[ &nbsp; ]</td>
      </tr>
      {rows_html}
      <tr style="background:#f1f5f9;">
        <td style="font-weight:800; color:{theme['primary']};">Spelling</td>
        <td style="font-weight:700;" colspan="2">Master Spelling Rules, Prefixes/Suffixes &amp; Vocabulary Banks</td>
        <td style="text-align:center; font-weight:700;">pp. 27–28</td>
        <td style="text-align:center;">[ &nbsp; ]</td>
      </tr>
      <tr style="background:#f1f5f9;">
        <td style="font-weight:800; color:{theme['primary']};">Mock Exam</td>
        <td style="font-weight:700;" colspan="2">Mixed Exam Proofreading Mock (Tasks 1 &amp; 2 - 12 Marks Total)</td>
        <td style="text-align:center; font-weight:700;">pp. 29–30</td>
        <td style="text-align:center;">[ &nbsp; ]</td>
      </tr>
      <tr style="background:#f8fafc;">
        <td style="font-weight:800; color:{theme['primary']};">Answer Key</td>
        <td style="font-weight:700;" colspan="2">Full Complete Answer Key &amp; Model Writing (Units 1–11 &amp; Mocks)</td>
        <td style="text-align:center; font-weight:700;">pp. 31–34</td>
        <td style="text-align:center;">[ &nbsp; ]</td>
      </tr>
      <tr style="background:#f8fafc;">
        <td style="font-weight:800; color:{theme['primary']};">Self-Audit</td>
        <td style="font-weight:700;" colspan="2">Student SPaG Self-Audit Checklist &amp; Assessor Sign-Off</td>
        <td style="text-align:center; font-weight:700;">Page 35</td>
        <td style="text-align:center;">[ &nbsp; ]</td>
      </tr>
    </tbody>
  </table>

  <div class="card-golden" style="margin-top:auto;">
    <div class="card-title">STUDY ADVICE FOR MAXIMUM EXAM RETENTION</div>
    <p style="margin:0; font-size:7.8pt;">
      Complete the Page 4 diagnostic first to identify your priority revision units. Study each unit's left-hand theory page before attempting the right-hand drills. Revisit the Master Spelling bank (pp. 27–28) weekly.
    </p>
  </div>

  <div class="page-footer">
    <div>{theme['title']} &bull; Table of Contents</div>
    <div class="page-num">Page 3</div>
  </div>
</div>
"""


def render_diagnostic_page(theme, diag_dict):
    """Generates Page 4: Baseline Diagnostic Assessment."""
    q_left = ""
    q_right = ""
    questions = diag_dict["questions"]
    for i, q in enumerate(questions):
        opts_html = ""
        for opt in q["options"]:
            opts_html += f"<div style='font-size:7.5pt; margin-top:2px;'>{opt}</div>"
        
        box_html = f"""
        <div class="q-item" style="margin-bottom:6px;">
          <div class="q-prompt" style="font-size:7.8pt; color:{theme['primary']};">
            Q{q['num']}. {q.get('topic', '')}: {q['prompt']}
          </div>
          {opts_html}
        </div>
        """
        if i < 5:
            q_left += box_html
        else:
            q_right += box_html

    scoring_rows = ""
    for s in diag_dict["scoring"]:
        scoring_rows += f"""
        <tr>
          <td style="font-weight:800; color:{theme['primary']}; width:24%;">{s['range']}</td>
          <td style="font-weight:700; width:30%;">{s['status']}</td>
          <td style="font-size:7.4pt; width:46%;">{s['advice']}</td>
        </tr>
        """

    return f"""
<div class="page" style="--theme-primary:{theme['primary']}; --theme-secondary:{theme['secondary']};">
  <div class="unit-page-header">
    <div class="brand-title">DIAGNOSTIC &bull; BASELINE SKILLS AUDIT</div>
    <div class="strand-badge">10 Questions &bull; 10 Marks</div>
  </div>

  <div style="margin-bottom:6px;">
    <h1 style="font-family:'Montserrat',sans-serif; font-size:12.5pt; font-weight:900; color:{theme['primary']}; margin:0 0 2px 0;">
      {diag_dict['title']}
    </h1>
    <p style="font-size:7.8pt; color:#64748b; margin:0 0 4px 0;">{diag_dict['subtitle']}</p>
  </div>

  <div class="grid-2col">
    <div>{q_left}</div>
    <div>{q_right}</div>
  </div>

  <div style="margin-top:auto;">
    <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.8pt; color:{theme['primary']}; text-transform:uppercase; margin-bottom:3px;">
      Diagnostic Score Guidance &amp; Priority Revision Routing:
    </div>
    <table class="mfs-table" style="margin:0;">
      <thead>
        <tr>
          <th>Score Band</th>
          <th>Assessment Status</th>
          <th>Recommended Revision Route</th>
        </tr>
      </thead>
      <tbody>
        {scoring_rows}
      </tbody>
    </table>
  </div>

  <div class="page-footer">
    <div>{theme['title']} &bull; Baseline Diagnostic Assessment</div>
    <div class="page-num">Page 4</div>
  </div>
</div>
"""


def render_unit_left_page(theme, unit_data, page_num):
    """Generates Unit Left Page (Odd: 5, 7, 9...): Theory & Visuals."""
    u_num = unit_data["unit"]
    u_title = unit_data["title"]
    fmt = unit_data.get("format", "Workplace Document")

    # If the unit already has pre-formatted rule_text with [A],[B],[C],[D] (like E3)
    if "[A] Situational Anchor" in unit_data.get("rule_text", ""):
        body_content = unit_data["rule_text"]
    else:
        # Assemble standard Murphy sections from L1/L2 data
        anchor_title = unit_data.get("anchor_title", f"Workplace Application: {fmt}")
        anchor_text = unit_data.get("format_link", unit_data.get("anchor_text", "Accurate syntax is essential in this vocational format to maintain professional credibility."))
        
        formula_title = "Syntax Architecture & Core Structural Rules"
        formula_text = unit_data.get("rule_text", "")

        bad_text = unit_data.get("worked_bad", "Example with error.")
        good_text = unit_data.get("worked_good", "Corrected example.")
        why_text = unit_data.get("worked_why", "Clear grammatical rationale.")

        golden_rule = "Always verify sentence boundaries and verb agreement before submitting exam scripts."
        if "Splice" in u_title:
            golden_rule = "THE SPLICE TEST: Never let a comma do a full stop's heavy lifting. If two sentences can stand alone, use a semicolon, a full stop, or ', and'."
        elif "Apostrophe" in u_title:
            golden_rule = "THE IT'S CHECK: 'It's' ONLY means 'it is'. If 'it is' does not fit in the sentence, erase the apostrophe immediately."
        elif "Agreement" in u_title:
            golden_rule = "THE BRACKET TRICK: Cross out words between the subject and verb (e.g. 'along with...', 'of the files') to find the true subject."
        elif "Homophone" in u_title:
            golden_rule = "THE RAVEN RULE: Remember: Affect is a Verb, Effect is a Noun. ICE is a NOUN: PractICE, AdvICE."
        elif "Colon" in u_title:
            golden_rule = "THE ANCHOR TEST: What comes BEFORE a colon or semicolon must stand alone as a 100% complete grammatical sentence."

        body_content = f"""
        <div class="card-anchor">
          <div class="card-title">[A] Situational Workplace Anchor: {anchor_title}</div>
          <p style="margin:0; font-size:8.1pt;">{anchor_text}</p>
        </div>

        <div class="card-formula">
          <div class="card-title">[B] {formula_title}</div>
          <div style="font-size:8pt; line-height:1.45;">{formula_text}</div>
        </div>

        <div class="card-compare">
          <div class="compare-row-bad">
            <span class="compare-badge badge-bad">❌ Pitfall</span>
            <span style="font-size:8pt; color:#991b1b;">{bad_text}</span>
          </div>
          <div class="compare-row-good">
            <span class="compare-badge badge-good">✔️ Model</span>
            <span style="font-size:8pt; color:#166534; font-weight:600;">{good_text}</span>
          </div>
          <div class="compare-row-why">
            <span class="compare-badge badge-why">💡 Examiner Why</span>
            <span>{why_text}</span>
          </div>
        </div>

        <div class="card-golden">
          <div class="card-title">[D] Examiner Golden Rule &amp; Memory Hook</div>
          <p style="margin:0; font-size:7.9pt;">{golden_rule}</p>
        </div>
        """

    return f"""
<div class="page" style="--theme-primary:{theme['primary']}; --theme-secondary:{theme['secondary']};">
  <div class="unit-page-header">
    <div class="brand-title">UNIT {u_num} &bull; THEORY &amp; VISUAL ARCHITECTURE</div>
    <div class="strand-badge">{theme['code']} &bull; {fmt}</div>
  </div>

  <div class="unit-main-heading">
    <span class="unit-num-pill">UNIT {u_num}</span>
    <h2 class="unit-title-text">{u_title}</h2>
  </div>

  <div style="display:flex; flex-direction:column; height:245mm; justify-content:space-between;">
    {body_content}
  </div>

  <div class="page-footer">
    <div>{theme['title']} &bull; Unit {u_num}: {u_title}</div>
    <div class="page-num">Page {page_num}</div>
  </div>
</div>
"""


def render_unit_right_page(theme, unit_data, page_num):
    """Generates Unit Right Page (Even: 6, 8, 10...): Progressive Drills."""
    u_num = unit_data["unit"]
    u_title = unit_data["title"]
    fmt = unit_data.get("format", "Workplace Document")

    # Ex 1: Recognition / Discrimination
    ex1_html = ""
    for idx, item in enumerate(unit_data.get("exercise_a", [])[:4], 1):
        q_text, opts = item[0], item[1]
        opts_rendered = " &nbsp; ".join([f"<span class='opt-box'><span class='opt-tick'></span> {opt}</span>" for opt in opts])
        ex1_html += f"""
        <div style="margin-bottom:4px; font-size:7.8pt;">
          <div><strong>{idx}.</strong> {q_text}</div>
          <div style="margin-top:2px;">{opts_rendered}</div>
        </div>
        """

    # Ex 2: Controlled Sentence Completion / Cloze
    ex2_html = ""
    if "exercise_b" in unit_data:
        for idx, item in enumerate(unit_data["exercise_b"][:3], 1):
            ex2_html += f"""
            <div style="margin-bottom:3px; font-size:7.8pt;">
              <strong>{idx}.</strong> {item[0]}: <em>{item[1]}</em>
            </div>
            """
    else:
        # Generate 2 strong guided drills from models or text
        ex2_html = f"""
        <div style="font-size:7.8pt; margin-bottom:3px;">
          <strong>1.</strong> Transform this informal sentence into professional {theme['code']} standard English: <em>'We checked the machine and it was working fine.'</em>
          <div style="border-bottom:1px dashed #cbd5e1; height:16px;"></div>
        </div>
        <div style="font-size:7.8pt;">
          <strong>2.</strong> Rewrite using appropriate punctuation to eliminate any sentence boundary errors: <em>'The alarm sounded loudly staff evacuated.'</em>
          <div style="border-bottom:1px dashed #cbd5e1; height:16px;"></div>
        </div>
        """

    # Ex 3: Forensic Workplace Proofreading
    doc_title = unit_data.get("proofreading_title", f"Applied Proofreading: {fmt}")
    doc_scenario = unit_data.get("proofreading_scenario", "Locate and correct all deliberate SPaG errors in the document below.")
    doc_text = unit_data.get("proofreading_text", "<p>Document text for proofreading.</p>")
    err_count = len(unit_data.get("proofreading_errors", [1,2,3,4,5]))

    # Ex 4: Applied Functional Writing Task
    writing_prompt = unit_data.get("writing_prompt", "Write three complete, correctly punctuated sentences suitable for this vocational workplace format.")

    return f"""
<div class="page" style="--theme-primary:{theme['primary']}; --theme-secondary:{theme['secondary']};">
  <div class="unit-page-header">
    <div class="brand-title">UNIT {u_num} &bull; GRADED PRACTICE DRILLS</div>
    <div class="strand-badge">{theme['code']} Applied Drills</div>
  </div>

  <div class="unit-main-heading">
    <span class="unit-num-pill">UNIT {u_num}</span>
    <h2 class="unit-title-text">Practice Drills &amp; Forensic Proofreading</h2>
  </div>

  <!-- EXERCISE 1: RECOGNITION -->
  <div class="exercise-section">
    <div class="ex-header">
      <span class="ex-title">[EXERCISE 1] Recognition &amp; Discrimination</span>
      <span class="ex-marks">4 Marks</span>
    </div>
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:5px; padding:5px 8px;">
      {ex1_html}
    </div>
  </div>

  <!-- EXERCISE 2: GUIDED COMPLETION -->
  <div class="exercise-section">
    <div class="ex-header">
      <span class="ex-title">[EXERCISE 2] Controlled Sentence Completion</span>
      <span class="ex-marks">3 Marks</span>
    </div>
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:5px; padding:5px 8px;">
      {ex2_html}
    </div>
  </div>

  <!-- EXERCISE 3: FORENSIC PROOFREADING -->
  <div class="exercise-section">
    <div class="ex-header">
      <span class="ex-title">[EXERCISE 3] Forensic Proofreading Scenario</span>
      <span class="ex-marks">{err_count} Marks</span>
    </div>
    <div class="workplace-doc">
      <div class="doc-topbar">
        <span>{doc_title.upper()}</span>
        <span>EXACT ERRORS TO FIND: {err_count}</span>
      </div>
      <div class="doc-meta">
        <strong>Context:</strong> {doc_scenario}
      </div>
      <div class="doc-body">
        {doc_text}
      </div>
    </div>
  </div>

  <!-- EXERCISE 4: APPLIED FUNCTIONAL WRITING -->
  <div class="exercise-section" style="margin-top:auto;">
    <div class="ex-header">
      <span class="ex-title">[EXERCISE 4] Applied Functional Writing Task</span>
      <span class="ex-marks">5 Marks</span>
    </div>
    <div class="applied-task-box">
      <div class="task-prompt">{writing_prompt}</div>
      <div class="task-lines"></div>
    </div>
  </div>

  <div class="page-footer">
    <div>{theme['title']} &bull; Unit {u_num}: Practice Drills</div>
    <div class="page-num">Page {page_num}</div>
  </div>
</div>
"""


def render_spelling_page_1(theme, spelling_data):
    """Generates Page 27: Master Spelling Rules & Patterns."""
    rules_html = ""
    for r in spelling_data.get("rules", [])[:4]:
        title, text = r[0], r[1]
        rules_html += f"""
        <div class="card-formula" style="margin-bottom:7px;">
          <div class="card-title" style="color:{theme['primary']};">{title}</div>
          <div style="font-size:7.9pt; line-height:1.45;">{text}</div>
        </div>
        """

    return f"""
<div class="page" style="--theme-primary:{theme['primary']}; --theme-secondary:{theme['secondary']};">
  <div class="unit-page-header">
    <div class="brand-title">MASTER SPELLING &bull; ORTHOGRAPHIC RULES</div>
    <div class="strand-badge">{theme['code']} Spelling Architecture</div>
  </div>

  <div style="margin-bottom:6px;">
    <h1 style="font-family:'Montserrat',sans-serif; font-size:13pt; font-weight:900; color:{theme['primary']}; margin:0 0 2px 0;">
      Core Spelling Rules &amp; Morphological Patterns
    </h1>
    <p style="font-size:7.8pt; color:#64748b; margin:0 0 5px 0;">Master the high-yield rules governing English spelling, pluralization, and suffix attachments.</p>
  </div>

  <div style="display:flex; flex-direction:column; height:245mm; justify-content:space-between;">
    {rules_html}
  </div>

  <div class="page-footer">
    <div>{theme['title']} &bull; Master Spelling Rules (Part 1)</div>
    <div class="page-num">Page 27</div>
  </div>
</div>
"""


def render_spelling_page_2(theme, spelling_data):
    """Generates Page 28: High-Yield Exam Vocabulary & Spelling Drills."""
    vocab_html = ""
    categories = spelling_data.get("vocab_bank", spelling_data.get("common_exception_words", []))
    for cat_title, words in categories[:4]:
        words_str = ", ".join(words[:12])
        vocab_html += f"""
        <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:5px; padding:5px 8px; margin-bottom:5px;">
          <strong style="color:{theme['primary']}; font-size:7.8pt;">{cat_title}:</strong>
          <div style="font-size:7.6pt; color:#334155; margin-top:2px;">{words_str}</div>
        </div>
        """

    test_html = ""
    for idx, item in enumerate(spelling_data.get("spelling_test", [])[:4], 1):
        q_text, opts = item[0], item[1]
        opts_str = " &nbsp; ".join([f"<span class='opt-box'><span class='opt-tick'></span> {opt}</span>" for opt in opts])
        test_html += f"""
        <div style="margin-bottom:4px; font-size:7.7pt;">
          <strong>{idx}.</strong> {q_text}<br>
          <div style="margin-top:2px;">{opts_str}</div>
        </div>
        """

    return f"""
<div class="page" style="--theme-primary:{theme['primary']}; --theme-secondary:{theme['secondary']};">
  <div class="unit-page-header">
    <div class="brand-title">MASTER SPELLING &bull; VOCABULARY &amp; DRILLS</div>
    <div class="strand-badge">{theme['code']} Word Bank</div>
  </div>

  <div style="margin-bottom:6px;">
    <h1 style="font-family:'Montserrat',sans-serif; font-size:13pt; font-weight:900; color:{theme['primary']}; margin:0 0 2px 0;">
      High-Frequency Exam Vocabulary &amp; Spelling Test
    </h1>
    <p style="font-size:7.8pt; color:#64748b; margin:0 0 5px 0;">Essential vocabulary frequently penalised by Pearson, City &amp; Guilds, and NCFE examiners.</p>
  </div>

  <div style="margin-bottom:8px;">
    <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:8pt; color:{theme['primary']}; text-transform:uppercase; margin-bottom:4px;">
      Essential Vocational Word Banks:
    </div>
    {vocab_html}
  </div>

  <div style="margin-top:auto;">
    <div class="ex-header">
      <span class="ex-title">Quick-Fire Spelling Accuracy Test</span>
      <span class="ex-marks">4 Marks</span>
    </div>
    <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:5px; padding:6px 9px;">
      {test_html}
    </div>
  </div>

  <div class="page-footer">
    <div>{theme['title']} &bull; Master Spelling Rules (Part 2)</div>
    <div class="page-num">Page 28</div>
  </div>
</div>
"""


def render_mock_task_page(theme, mock_task, page_num, task_num):
    """Generates Pages 29 & 30: Mixed Exam Proofreading Mock Tasks 1 & 2."""
    title = mock_task.get("title", f"Mixed Exam Proofreading Mock: Task {task_num} (6 Marks)")
    scenario = mock_task.get("scenario_title", mock_task.get("scenario", "Workplace Proofreading Challenge"))
    context = mock_task.get("context", "Identify and correct all deliberate SPaG errors in the document.")
    doc_meta = mock_task.get("doc_meta", f"DOCUMENT REF: EXAM-MOCK-{theme['code']}-0{task_num}")
    doc_text = mock_task.get("text", "")

    return f"""
<div class="page" style="--theme-primary:{theme['primary']}; --theme-secondary:{theme['secondary']};">
  <div class="unit-page-header">
    <div class="brand-title">MOCK EXAM &bull; PROOFREADING WORKOUT</div>
    <div class="strand-badge">Task {task_num} of 2 &bull; 6 Marks</div>
  </div>

  <div style="margin-bottom:6px;">
    <h1 style="font-family:'Montserrat',sans-serif; font-size:12.5pt; font-weight:900; color:{theme['primary']}; margin:0 0 2px 0;">
      {title}
    </h1>
    <p style="font-size:7.8pt; color:#64748b; margin:0 0 4px 0;">Calibrated against official Ofqual Functional Skills English Writing criteria.</p>
  </div>

  <div class="card-anchor" style="margin-bottom:8px;">
    <div class="card-title">EXAM SCENARIO: {scenario}</div>
    <p style="margin:0; font-size:7.9pt;">{context}</p>
  </div>

  <div class="workplace-doc" style="margin-bottom:8px;">
    <div class="doc-topbar">
      <span>{doc_meta}</span>
      <span>FIND &amp; CORRECT 6 ERRORS</span>
    </div>
    <div class="doc-body" style="font-size:8.2pt; line-height:1.5;">
      {doc_text}
    </div>
  </div>

  <!-- Exam Answer Writing Workspace Table -->
  <div style="margin-top:auto;">
    <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.8pt; color:{theme['primary']}; text-transform:uppercase; margin-bottom:3px;">
      Correction Grid (Identify the error and write the correct version):
    </div>
    <table class="mfs-table" style="margin:0;">
      <thead>
        <tr>
          <th style="width:10%;">No.</th>
          <th style="width:45%;">Original Word / Sentence with Error</th>
          <th style="width:45%;">Corrected Version</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>1</td><td style="height:17px;"></td><td></td></tr>
        <tr><td>2</td><td style="height:17px;"></td><td></td></tr>
        <tr><td>3</td><td style="height:17px;"></td><td></td></tr>
        <tr><td>4</td><td style="height:17px;"></td><td></td></tr>
        <tr><td>5</td><td style="height:17px;"></td><td></td></tr>
        <tr><td>6</td><td style="height:17px;"></td><td></td></tr>
      </tbody>
    </table>
  </div>

  <div class="page-footer">
    <div>{theme['title']} &bull; Mixed Mock Exam (Task {task_num})</div>
    <div class="page-num">Page {page_num}</div>
  </div>
</div>
"""


def render_answer_key_page(theme, page_num, section_title, content_html):
    """Generates Pages 31, 32, 33, 34: Answer Keys."""
    return f"""
<div class="page" style="--theme-primary:{theme['primary']}; --theme-secondary:{theme['secondary']};">
  <div class="unit-page-header">
    <div class="brand-title">EXAMINER ANSWER KEY &bull; MARK SCHEME</div>
    <div class="strand-badge">{theme['code']} Model Solutions</div>
  </div>

  <div style="margin-bottom:6px;">
    <h1 style="font-family:'Montserrat',sans-serif; font-size:12.5pt; font-weight:900; color:{theme['primary']}; margin:0 0 2px 0;">
      {section_title}
    </h1>
    <p style="font-size:7.8pt; color:#64748b; margin:0 0 5px 0;">Official model answers, proofreading error keys, and examiner marking commentary.</p>
  </div>

  <div style="display:flex; flex-direction:column; height:245mm; justify-content:space-between; font-size:7.8pt; line-height:1.42;">
    {content_html}
  </div>

  <div class="page-footer">
    <div>{theme['title']} &bull; Complete Answer Key</div>
    <div class="page-num">Page {page_num}</div>
  </div>
</div>
"""


def render_audit_page(theme, units_list):
    """Generates Page 35: Student SPaG Self-Audit Checklist & Progress Tracker."""
    rows_html = ""
    for u in units_list:
        rows_html += f"""
        <tr>
          <td style="font-weight:700; color:{theme['primary']};">Unit {u['unit']}</td>
          <td>{u['title']}</td>
          <td style="text-align:center;"><span class="rag-pill rag-red"></span></td>
          <td style="text-align:center;"><span class="rag-pill rag-amber"></span></td>
          <td style="text-align:center;"><span class="rag-pill rag-green"></span></td>
          <td style="text-align:center;">&nbsp; / 12</td>
          <td style="text-align:center;">[ &nbsp; ]</td>
        </tr>
        """

    return f"""
<div class="page" style="--theme-primary:{theme['primary']}; --theme-secondary:{theme['secondary']};">
  <div class="unit-page-header">
    <div class="brand-title">SELF-AUDIT &bull; EXAM READINESS CHECKLIST</div>
    <div class="strand-badge">{theme['code']} Quality Sign-Off</div>
  </div>

  <div style="margin-bottom:6px;">
    <h1 style="font-family:'Montserrat',sans-serif; font-size:12.5pt; font-weight:900; color:{theme['primary']}; margin:0 0 2px 0;">
      Student SPaG Self-Audit &amp; Assessor Verification
    </h1>
    <p style="font-size:7.8pt; color:#64748b; margin:0 0 4px 0;">Track your confidence across all 11 units and record personal priority revision areas.</p>
  </div>

  <table class="mfs-table" style="font-size:7.5pt; margin-bottom:6px;">
    <thead>
      <tr>
        <th style="width:10%;">Unit</th>
        <th style="width:50%;">Core Competency / Topic</th>
        <th style="text-align:center; width:6%;">Red</th>
        <th style="text-align:center; width:6%;">Amb</th>
        <th style="text-align:center; width:6%;">Grn</th>
        <th style="text-align:center; width:12%;">Drill Score</th>
        <th style="text-align:center; width:10%;">Mastered</th>
      </tr>
    </thead>
    <tbody>
      {rows_html}
    </tbody>
  </table>

  <!-- Personal Watchlist -->
  <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:5px; padding:6px 9px; margin-bottom:6px;">
    <strong style="color:{theme['primary']}; font-size:7.8pt; text-transform:uppercase;">My Personal SPaG Watchlist (Top 3 Slip-Ups to Check in the Exam):</strong>
    <div style="font-size:7.5pt; margin-top:3px; display:grid; grid-template-columns:1fr 1fr 1fr; gap:6px;">
      <div style="border-bottom:1px dashed #94a3b8; height:18px;">1. </div>
      <div style="border-bottom:1px dashed #94a3b8; height:18px;">2. </div>
      <div style="border-bottom:1px dashed #94a3b8; height:18px;">3. </div>
    </div>
  </div>

  <!-- Tutor / Assessor Sign-Off -->
  <div style="margin-top:auto; background:#f8fafc; border:1.5px solid #cbd5e1; border-radius:5px; padding:6px 10px; font-size:7.6pt;">
    <div style="font-family:'Montserrat',sans-serif; font-weight:800; color:{theme['primary']}; text-transform:uppercase; margin-bottom:3px;">
      Tutor / Assessor Final Competency Sign-Off:
    </div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr 1fr; gap:8px;">
      <div><strong>Diagnostic Score:</strong> &nbsp; &nbsp; / 10</div>
      <div><strong>Mock Total Score:</strong> &nbsp; &nbsp; / 12</div>
      <div><strong>Target Achieved:</strong> [ &nbsp; ] YES &nbsp; [ &nbsp; ] NO</div>
      <div><strong>Date Verified:</strong> &nbsp; &nbsp; &nbsp; &nbsp; / &nbsp; &nbsp; / 2026</div>
    </div>
  </div>

  <div class="page-footer">
    <div>{theme['title']} &bull; Student Self-Audit &amp; Progress Tracker</div>
    <div class="page-num">Page 35</div>
  </div>
</div>
"""


def render_back_cover(theme):
    """Generates Page 36: Full-bleed High-Impact Back Cover."""
    return f"""
<div class="page cover-page" style="background: linear-gradient(145deg, {theme['cover_grad_start']} 0%, {theme['cover_grad_mid']} 55%, {theme['cover_grad_end']} 100%);">
  <div style="padding: 16mm 18mm 0 18mm;">
    <!-- Brand Header -->
    <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1.5px solid rgba(255,255,255,0.25); padding-bottom:10px;">
      <div style="font-family:'Montserrat',sans-serif; font-size:12pt; font-weight:900; letter-spacing:2px; color:#ffffff;">MASTER FUNCTIONAL SKILLS</div>
      <div style="background:{theme['badge_bg']}; color:#ffffff; font-family:'Montserrat',sans-serif; font-weight:900; font-size:7.5pt; padding:4px 10px; border-radius:12px;">
        {theme['code']} SPECIFICATION
      </div>
    </div>

    <!-- Synopsis -->
    <div style="margin-top:14mm;">
      <h2 style="font-family:'Montserrat',sans-serif; font-size:17pt; font-weight:900; color:#ffffff; line-height:1.2; margin:0 0 6px 0;">
        Guaranteed Exam Accuracy Through Dyslexia-Friendly Mastery
      </h2>
      <p style="font-size:8.5pt; color:rgba(255,255,255,0.85); line-height:1.55; margin:0 0 10px 0;">
        Designed by specialist literacy clinicians and Ofqual curriculum authors, this comprehensive {theme.get('total_pages', 100)}-page workbook translates complex English spelling, punctuation, and grammar rules into visual, intuitive learning pathways.
      </p>
    </div>

    <!-- Three Pillars -->
    <div style="display:grid; grid-template-columns:1fr; gap:8px; margin-top:6mm;">
      <div style="background:rgba(255,255,255,0.08); border-left:4px solid #38bdf8; padding:8px 12px; border-radius:5px;">
        <strong style="color:#ffffff; font-size:8.3pt; font-family:'Montserrat',sans-serif;">1. The Murphy 2-Page Visual Spread:</strong>
        <p style="margin:2px 0 0 0; font-size:7.8pt; color:rgba(255,255,255,0.8);">No turning pages back and forth. Theory, syntax architecture, and worked good-vs-bad models on the left; targeted practice drills on the right.</p>
      </div>
      <div style="background:rgba(255,255,255,0.08); border-left:4px solid #34d399; padding:8px 12px; border-radius:5px;">
        <strong style="color:#ffffff; font-size:8.3pt; font-family:'Montserrat',sans-serif;">2. Dyslexia-First Accessibility Engineering:</strong>
        <p style="margin:2px 0 0 0; font-size:7.8pt; color:rgba(255,255,255,0.8);">Anti-glare warm cream paper (#FDFBF7), clear sans-serif typography (Lexend), left-aligned formatting, and color-coded cognitive cards.</p>
      </div>
      <div style="background:rgba(255,255,255,0.08); border-left:4px solid #fbbf24; padding:8px 12px; border-radius:5px;">
        <strong style="color:#ffffff; font-size:8.3pt; font-family:'Montserrat',sans-serif;">3. Real-World Vocational Relevance:</strong>
        <p style="margin:2px 0 0 0; font-size:7.8pt; color:rgba(255,255,255,0.8);">All exercises mirror authentic workplace communications: incident reports, health and safety notices, formal correspondence, and client emails.</p>
      </div>
    </div>

    <!-- Level Ladder -->
    <div style="background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:6px; padding:10px 14px; margin-top:10mm;">
      <div style="font-family:'Montserrat',sans-serif; font-size:7.5pt; font-weight:800; color:#fde68a; letter-spacing:1px; text-transform:uppercase; margin-bottom:5px;">
        Complete Master Functional Skills English Ladder:
      </div>
      <div style="display:flex; justify-content:space-between; font-size:7.4pt; color:#ffffff;">
        <span>&bull; Entry Level 3 Core Foundations</span>
        <span>&bull; Level 1 Essential Competence</span>
        <span style="font-weight:800; color:#38bdf8;">&bull; Level 2 Advanced Mastery</span>
      </div>
    </div>
  </div>

  <!-- Bottom Brand & Barcode Strip -->
  <div style="background:rgba(0,0,0,0.5); border-top:1px solid rgba(255,255,255,0.15); padding:10mm 18mm; display:flex; justify-content:space-between; align-items:center;">
    <div>
      <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:8.5pt; color:#ffffff;">masterfunctionalskills.co.uk</div>
      <div style="font-size:7.2pt; color:rgba(255,255,255,0.7); margin-top:2px;">Online Courses &bull; Revision Cards &bull; Mock Exam Papers &bull; Video Solutions</div>
    </div>
    <div style="text-align:right; background:#ffffff; color:#0f172a; padding:6px 12px; border-radius:4px; font-family:'Montserrat',sans-serif; font-weight:900; font-size:7.2pt; letter-spacing:1px;">
      OFQUAL REGULATED CURRICULUM
    </div>
  </div>
</div>
"""


# =============================================================================
# COMPILED BOOK BUILDERS
# =============================================================================

def build_book(level_code):
    """Compiles the full 36-page HTML and prints to PDF for the given level."""
    theme = LEVEL_THEMES[level_code]
    print(f"\n[{level_code}] Starting compilation of {theme['full_name']}...")

    # Select appropriate dataset
    if level_code == "L2":
        units = spag_content_l2.L2_UNITS
        diag_data = spag_data_l2.L2_DIAGNOSTIC
        spelling_data = spag_content_extras.L2_SPELLING_DATA
        mock_1 = spag_data_l2.L2_MOCK_TASK_1
        mock_2 = spag_data_l2.L2_MOCK_TASK_2
        answers = spag_data_l2.L2_ANSWERS
    elif level_code == "L1":
        units = spag_content_l1.L1_UNITS
        diag_data = spag_data_l1.L1_DIAGNOSTIC
        spelling_data = spag_content_extras.L1_SPELLING_DATA
        mock_1 = spag_data_l1.L1_MOCK_TASK_1
        mock_2 = spag_data_l1.L1_MOCK_TASK_2
        answers = spag_data_l1.L1_ANSWERS
    else: # E3
        units = spag_content_e3.E3_UNITS
        diag_data = {
            "title": "Baseline Diagnostic Assessment: Entry Level 3 SPaG Audit",
            "subtitle": "Complete this 10-minute diagnostic to identify your spelling, capital letters, and sentence building priorities.",
            "questions": [
                {"num": q["q_num"], "topic": q.get("topic", f"Unit {i}"), "prompt": q["question"], "options": q["options"], "correct": q["answer"]}
                for i, q in enumerate(spag_content_e3.E3_DIAGNOSTIC, 1)
            ],
            "scoring": [
                {"range": "8 – 10 Marks", "status": "Strong Entry 3 Foundation", "advice": "Ready to progress towards Level 1 writing tasks."},
                {"range": "5 – 7 Marks", "status": "Developing SPaG Skills", "advice": "Review Units 1, 2, 6, 8 and 9 carefully."},
                {"range": "0 – 4 Marks", "status": "Priority Revision", "advice": "Work through all 11 units sequentially in the workbook."}
            ]
        }
        spelling_data = spag_content_e3.E3_SPELLING_DATA
        mock_1 = {
            "title": "Mixed Exam Proofreading Mock: Task 1 (6 Marks)",
            "scenario_title": "STOCKROOM INVENTORY & FAULT REPORT",
            "context": "A warehouse assistant completed this incident log. Find and correct the 6 deliberate SPaG errors.",
            "doc_meta": "REPORT: LOG-E3-2026 | SITE: North Distribution Centre",
            "text": "yesterday morning, i unpacked ten boxes of tools. Three crates was damaged during transport. The driver stoped on wednesday to report the leak. Can we replace the damaged boxes on wednesday."
        }
        mock_2 = {
            "title": "Mixed Exam Proofreading Mock: Task 2 (6 Marks)",
            "scenario_title": "HEALTH & SAFETY VISITOR NOTICE",
            "context": "A receptionist drafted this safety notice for contractors. Find and correct the 6 deliberate SPaG errors.",
            "doc_meta": "NOTICE REF: SAF-E3-2026 | RECEPTION DESK",
            "text": "Welcome to our clinic. All visitors must sign the visitor book on friday. Two contractors is working on Church road. Have they signed their permit? Do not block the ambulance bays!"
        }
        answers = {
            "page_31": {
                "title": "Complete Answer Key: Diagnostic & Units 1 to 3",
                "diagnostic": [f"{q[0]}: {q[1]} &bull; {q[2]}" for q in spag_content_e3.E3_ANSWERS["diagnostic"]],
                "unit_1": spag_content_e3.E3_ANSWERS["units"][1],
                "unit_2": spag_content_e3.E3_ANSWERS["units"][2],
                "unit_3": spag_content_e3.E3_ANSWERS["units"][3]
            },
            "page_32": {
                "title": "Complete Answer Key: Units 4 to 7",
                "unit_4": spag_content_e3.E3_ANSWERS["units"][4],
                "unit_5": spag_content_e3.E3_ANSWERS["units"][5],
                "unit_6": spag_content_e3.E3_ANSWERS["units"][6],
                "unit_7": spag_content_e3.E3_ANSWERS["units"][7]
            },
            "page_33": {
                "title": "Complete Answer Key: Units 8 to 11",
                "unit_8": spag_content_e3.E3_ANSWERS["units"][8],
                "unit_9": spag_content_e3.E3_ANSWERS["units"][9],
                "unit_10": spag_content_e3.E3_ANSWERS["units"][10],
                "unit_11": spag_content_e3.E3_ANSWERS["units"][11]
            },
            "page_34": {
                "title": "Complete Answer Key: Master Spelling & Mixed Mocks",
                "spelling": spag_content_e3.E3_ANSWERS["spelling_test"],
                "mock_1": spag_content_e3.E3_ANSWERS["mixed_workout"][1],
                "mock_2": spag_content_e3.E3_ANSWERS["mixed_workout"][2]
            }
        }

    pages_html = []

    # Page 1: Front Cover
    pages_html.append(render_front_cover(theme))

    # Page 2: Inside Cover & Candidate Details
    pages_html.append(render_inside_cover(theme))

    # Page 3: Table of Contents & Unit Progress Matrix
    pages_html.append(render_toc(theme, units))

    # Page 4: Baseline Diagnostic Assessment
    pages_html.append(render_diagnostic_page(theme, diag_data))

    # Pages 5 to 26: Units 1 to 11 (2 pages per unit = 22 pages)
    page_num = 5
    for unit_data in units:
        # Left Page
        pages_html.append(render_unit_left_page(theme, unit_data, page_num))
        page_num += 1
        # Right Page
        pages_html.append(render_unit_right_page(theme, unit_data, page_num))
        page_num += 1

    # Pages 27 to 28: Master Spelling Rules & Vocabulary (2 pages)
    pages_html.append(render_spelling_page_1(theme, spelling_data))
    pages_html.append(render_spelling_page_2(theme, spelling_data))

    # Pages 29 to 30: Mixed Exam Proofreading Mock (2 pages)
    pages_html.append(render_mock_task_page(theme, mock_1, 29, 1))
    pages_html.append(render_mock_task_page(theme, mock_2, 30, 2))

    # Pages 31 to 34: Complete Answer Key (4 pages)
    # Page 31: Diagnostic + Units 1-3
    p31_data = answers["page_31"]
    diag_summary = "<br>".join(p31_data.get("diagnostic", [])[:10])
    u1_ans = str(p31_data.get("unit_1", ""))
    u2_ans = str(p31_data.get("unit_2", ""))
    u3_ans = str(p31_data.get("unit_3", ""))
    p31_html = f"""
    <div class="card-formula">
      <div class="card-title">Diagnostic Assessment Solutions:</div>
      <div style="font-size:7.4pt;">{diag_summary}</div>
    </div>
    <div class="card-formula">
      <div class="card-title">Unit 1 Answer Key:</div>
      <div style="font-size:7.4pt;">{u1_ans}</div>
    </div>
    <div class="card-formula">
      <div class="card-title">Unit 2 Answer Key:</div>
      <div style="font-size:7.4pt;">{u2_ans}</div>
    </div>
    <div class="card-formula">
      <div class="card-title">Unit 3 Answer Key:</div>
      <div style="font-size:7.4pt;">{u3_ans}</div>
    </div>
    """
    pages_html.append(render_answer_key_page(theme, 31, p31_data["title"], p31_html))

    # Page 32: Units 4-7
    p32_data = answers["page_32"]
    u4_ans = str(p32_data.get("unit_4", ""))
    u5_ans = str(p32_data.get("unit_5", ""))
    u6_ans = str(p32_data.get("unit_6", ""))
    u7_ans = str(p32_data.get("unit_7", ""))
    p32_html = f"""
    <div class="card-formula">
      <div class="card-title">Unit 4 Answer Key:</div>
      <div style="font-size:7.4pt;">{u4_ans}</div>
    </div>
    <div class="card-formula">
      <div class="card-title">Unit 5 Answer Key:</div>
      <div style="font-size:7.4pt;">{u5_ans}</div>
    </div>
    <div class="card-formula">
      <div class="card-title">Unit 6 Answer Key:</div>
      <div style="font-size:7.4pt;">{u6_ans}</div>
    </div>
    <div class="card-formula">
      <div class="card-title">Unit 7 Answer Key:</div>
      <div style="font-size:7.4pt;">{u7_ans}</div>
    </div>
    """
    pages_html.append(render_answer_key_page(theme, 32, p32_data["title"], p32_html))

    # Page 33: Units 8-11
    p33_data = answers["page_33"]
    u8_ans = str(p33_data.get("unit_8", ""))
    u9_ans = str(p33_data.get("unit_9", ""))
    u10_ans = str(p33_data.get("unit_10", ""))
    u11_ans = str(p33_data.get("unit_11", ""))
    p33_html = f"""
    <div class="card-formula">
      <div class="card-title">Unit 8 Answer Key:</div>
      <div style="font-size:7.4pt;">{u8_ans}</div>
    </div>
    <div class="card-formula">
      <div class="card-title">Unit 9 Answer Key:</div>
      <div style="font-size:7.4pt;">{u9_ans}</div>
    </div>
    <div class="card-formula">
      <div class="card-title">Unit 10 Answer Key:</div>
      <div style="font-size:7.4pt;">{u10_ans}</div>
    </div>
    <div class="card-formula">
      <div class="card-title">Unit 11 Answer Key:</div>
      <div style="font-size:7.4pt;">{u11_ans}</div>
    </div>
    """
    pages_html.append(render_answer_key_page(theme, 33, p33_data["title"], p33_html))

    # Page 34: Spelling & Mixed Mocks
    p34_data = answers["page_34"]
    spell_ans = str(p34_data.get("spelling", ""))
    mock1_ans = str(p34_data.get("mock_1", ""))
    mock2_ans = str(p34_data.get("mock_2", ""))
    p34_html = f"""
    <div class="card-formula">
      <div class="card-title">Master Spelling Rules &amp; Test Solutions:</div>
      <div style="font-size:7.4pt;">{spell_ans}</div>
    </div>
    <div class="card-formula">
      <div class="card-title">Mixed Exam Mock Task 1 Solutions:</div>
      <div style="font-size:7.4pt;">{mock1_ans}</div>
    </div>
    <div class="card-formula">
      <div class="card-title">Mixed Exam Mock Task 2 Solutions:</div>
      <div style="font-size:7.4pt;">{mock2_ans}</div>
    </div>
    """
    pages_html.append(render_answer_key_page(theme, 34, p34_data["title"], p34_html))

    # Page 35: Student SPaG Self-Audit Checklist
    pages_html.append(render_audit_page(theme, units))

    # Page 36: Full-bleed Back Cover
    pages_html.append(render_back_cover(theme))

    assert len(pages_html) == 36, f"ERROR: Expected exactly 36 pages, but got {len(pages_html)}"

    # Assemble HTML document
    full_html = f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<title>{theme['full_name']} &bull; SPaG Mastery Workbook</title>
{SHARED_CSS}
</head>
<body>
{''.join(pages_html)}
</body>
</html>
"""

    temp_html_path = os.path.join(SCRATCH_DIR, f"temp_{theme['file_stem']}.html")
    with open(temp_html_path, "w", encoding="utf-8") as f:
        f.write(full_html)

    # Destination paths
    out_pdf_downloads = os.path.join(DOWNLOADS_DIR, f"{theme['file_stem']}.pdf")
    out_pdf_documents = os.path.join(DOCUMENTS_DIR, f"{theme['file_stem']}.pdf")

    # Render with Chromium headless
    cmd = [
        CHROME_BIN,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--user-data-dir=/tmp/chr_spag_build",
        "--no-pdf-header-footer",
        f"--print-to-pdf={out_pdf_downloads}",
        temp_html_path
    ]
    subprocess.run(cmd, check=True)

    # Copy to /home/subi/Documents
    shutil.copy2(out_pdf_downloads, out_pdf_documents)

    if os.path.exists(temp_html_path):
        os.remove(temp_html_path)

    # Verify with pdfinfo
    res = subprocess.run(["pdfinfo", out_pdf_downloads], capture_output=True, text=True, check=True)
    page_count = None
    for line in res.stdout.splitlines():
        if "Pages:" in line:
            page_count = int(line.split(":")[1].strip())
            break

    file_size_mb = os.path.getsize(out_pdf_downloads) / (1024 * 1024)
    print(f"[{level_code}] SUCCESSFULLY COMPILED -> {out_pdf_downloads}")
    print(f"[{level_code}] Verified Page Count: {page_count} (Target: 36 pages) | Size: {file_size_mb:.2f} MB")
    print(f"[{level_code}] Replicated to Documents -> {out_pdf_documents}")

    if page_count != 36:
        raise ValueError(f"[{level_code}] Page count mismatch! Expected 36 pages, but pdfinfo reports {page_count}")


def main():
    print("=" * 75)
    print("MASTER FUNCTIONAL SKILLS: DYSLEXIA-FRIENDLY SPAG BOOK COMPILER")
    print("=" * 75)
    start_time = time.time()

    levels = ["L2", "L1", "E3"]
    for lvl in levels:
        build_book(lvl)

    elapsed = time.time() - start_time
    print("\n" + "=" * 75)
    print(f"ALL 3 COMPLETE 36-PAGE SPAG MASTERY WORKBOOKS COMPILED IN {elapsed:.2f}s!")
    print("Artifact Destinations:")
    print(f"  1. Downloads: {DOWNLOADS_DIR}")
    print(f"  2. Documents: {DOCUMENTS_DIR}")
    print("=" * 75)


if __name__ == "__main__":
    main()
