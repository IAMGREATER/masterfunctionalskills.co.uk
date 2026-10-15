#!/usr/bin/env python3
"""
build_spag_l1_84p.py
=============================================================================
Master Functional Skills: 84-Page Level 1 SPaG Mastery Publication Builder
Compiles: MasterFunctionalSkills_SPaG_Level_1_Mastery.pdf (Emerald Teal)

Theme:
  Primary: #0c4e45 | Secondary: #0d9488 | Accent: #14b8a6 | Amber: #fbbf24
  Canvas: Warm Cream (#FDFBF7) | Text: Deep Slate (#1F2937)

Architecture (Exact 84-Page Layout):
  Page 1: Full-Bleed Front Cover
  Page 2: Inside Cover & Dyslexia Statement
  Pages 3–6: Baseline Diagnostic Assessment & Murphy Study Guide (32 Qs + Routing Matrix)
  Pages 7–58: 26 Two-Page Murphy 'Grammar in Use' Units (52 pages)
  Pages 59–64: Vocabulary in Use Master Modules (6 pages)
  Pages 65–70: Murphy-Style Mixed Additional Exercises (6 pages)
  Pages 71–76: Official Exam Proofreading & Extended Writing Mocks (6 pages)
  Pages 77–82: Comprehensive Explanatory Answer Key with Examiner Mark Breakdown (6 pages)
  Page 83: Candidate Self-Audit Checklist & Progress Matrix (1 page)
  Page 84: High-Impact Back Cover (1 page)

Destinations:
  1. /home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk/assets/downloads/
  2. /home/subi/Documents/
=============================================================================
"""

import os
import sys
import time
import shutil
import subprocess

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from spag_styles import SHARED_CSS, LEVEL_THEMES
import spag_l1_84p_units
import spag_l1_84p_data

PROJECT_DIR = "/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk"
DOWNLOADS_DIR = os.path.join(PROJECT_DIR, "assets", "downloads")
DOCUMENTS_DIR = "/home/subi/Documents"
SCRATCH_DIR = os.path.join(PROJECT_DIR, "scratch", "spag_build_l1_84p")
CHROME_BIN = "/usr/lib/chromium/chromium"

os.makedirs(DOWNLOADS_DIR, exist_ok=True)
os.makedirs(DOCUMENTS_DIR, exist_ok=True)
os.makedirs(SCRATCH_DIR, exist_ok=True)

THEME = {
    "code": "Level 1",
    "level_code": "L1",
    "title": "Level 1 SPaG Mastery",
    "full_name": "Functional Skills English Level 1",
    "subtitle": "Complete 84-Page SPaG Comprehensive Self-Study & Exam Revision Manual",
    "primary": "#0c4e45",
    "secondary": "#0d9488",
    "accent": "#14b8a6",
    "amber": "#fbbf24",
    "tint": "#f0fdfa",
    "border_color": "#99f6e4",
    "badge_bg": "#0d9488",
    "badge_text": "#ffffff",
    "cover_grad_start": "#022420",
    "cover_grad_mid": "#0c4e45",
    "cover_grad_end": "#134e4a",
    "ofqual_code": "Functional Skills English Level 1 Writing (Ofqual Spec 2026/2027)",
    "file_stem": "MasterFunctionalSkills_SPaG_Level_1_Mastery"
}


# =============================================================================
# PAGE RENDERING FUNCTIONS
# =============================================================================

def render_front_cover(theme):
    """Page 1: Full-Bleed Front Cover."""
    return f"""
<div class="page cover-page" style="background: linear-gradient(145deg, {theme['cover_grad_start']} 0%, {theme['cover_grad_mid']} 55%, {theme['cover_grad_end']} 100%);">
  <div style="padding: 16mm 18mm 0 18mm;">
    <!-- Top Brand Header -->
    <div style="display:flex; justify-content:space-between; align-items:center; border-bottom: 1.5px solid rgba(255,255,255,0.25); padding-bottom:12px;">
      <div>
        <div style="font-family:'Montserrat',sans-serif; font-size:13pt; font-weight:900; letter-spacing:2.5px; color:#ffffff;">MASTER FUNCTIONAL SKILLS</div>
        <div style="font-size:7.5pt; font-weight:700; letter-spacing:1.5px; color:#fbbf24; margin-top:2px;">OFFICIAL OFQUAL SPECIFICATION &bull; 2026/2027 CURRICULUM</div>
      </div>
      <div style="background:{theme['badge_bg']}; color:#ffffff; font-family:'Montserrat',sans-serif; font-weight:900; font-size:8.5pt; padding:6px 14px; border-radius:20px; letter-spacing:1px; border:1px solid rgba(255,255,255,0.3); box-shadow:0 2px 8px rgba(0,0,0,0.3);">
        LEVEL 1 COMPREHENSIVE
      </div>
    </div>

    <!-- Knockout Level Graphic -->
    <div style="margin-top:20mm;">
      <div style="font-family:'Montserrat',sans-serif; font-size:38pt; font-weight:900; color:rgba(255,255,255,0.08); letter-spacing:4px; line-height:0.9; text-transform:uppercase;">
        LEVEL 1 SPAG
      </div>
      <div style="margin-top:-20px; font-family:'Montserrat',sans-serif; font-size:23pt; font-weight:900; color:#ffffff; line-height:1.15; letter-spacing:0.5px;">
        SPELLING, PUNCTUATION<br>&amp; GRAMMAR MASTERY
      </div>
      <div style="font-size:11.5pt; font-weight:600; color:#fde68a; margin-top:8px; letter-spacing:0.5px;">
        The Complete 84-Page 2-Page Spread Self-Study &amp; Revision Workbook
      </div>
      <div style="font-size:8.3pt; color:rgba(255,255,255,0.85); margin-top:6px; max-width:160mm; line-height:1.5;">
        Engineered with British Dyslexia Association accessibility standards, anti-glare warm cream paper (#FDFBF7), and the Raymond Murphy 'Grammar in Use' two-page pedagogical framework. 26 comprehensive units with progressive 4-tier drills, workplace proofreading scenarios, and complete explanatory answers.
      </div>
    </div>

    <!-- Key Feature Badges Grid -->
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:9px; margin-top:16mm;">
      <div style="background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.18); border-left:4px solid #38bdf8; border-radius:6px; padding:7px 11px;">
        <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:8pt; color:#ffffff;">26 MURPHY 2-PAGE SPREADS</div>
        <div style="font-size:7.4pt; color:rgba(255,255,255,0.8); margin-top:2px;">Theory and syntax formulas on the left; progressive 4-tier practice on the right.</div>
      </div>
      <div style="background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.18); border-left:4px solid #34d399; border-radius:6px; padding:7px 11px;">
        <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:8pt; color:#ffffff;">100% DYSLEXIA-FRIENDLY</div>
        <div style="font-size:7.4pt; color:rgba(255,255,255,0.8); margin-top:2px;">Soft #FDFBF7 cream background, Lexend font, ragged-right, generous line leading.</div>
      </div>
      <div style="background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.18); border-left:4px solid #f472b6; border-radius:6px; padding:7px 11px;">
        <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:8pt; color:#ffffff;">AUTHENTIC WORKPLACE SCENARIOS</div>
        <div style="font-size:7.4pt; color:rgba(255,255,255,0.8); margin-top:2px;">Health &amp; safety logs, customer service emails, and incident reports.</div>
      </div>
      <div style="background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.18); border-left:4px solid #fbbf24; border-radius:6px; padding:7px 11px;">
        <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:8pt; color:#ffffff;">FULL EXPLANATORY ANSWER KEY</div>
        <div style="font-size:7.4pt; color:rgba(255,255,255,0.8); margin-top:2px;">Comprehensive mark schemes, error logs, and examiner model answers.</div>
      </div>
    </div>

    <!-- Syllabus Breadth Pill Grid -->
    <div style="margin-top:14mm; background:rgba(0,0,0,0.22); border-radius:6px; padding:8px 12px; border:1px solid rgba(255,255,255,0.12);">
      <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.4pt; color:#fde68a; letter-spacing:0.8px; margin-bottom:5px;">COMPLETE 84-PAGE SYLLABUS ARCHITECTURE:</div>
      <div style="font-size:7.2pt; color:rgba(255,255,255,0.85); line-height:1.45;">
        &bull; 32-Item Diagnostic Assessment &amp; Routing Guide (pp. 3–6)<br>
        &bull; 26 Two-Page Raymond Murphy Grammar in Use Units (pp. 7–58)<br>
        &bull; 6 Vocabulary in Use Master Modules &amp; Spelling Banks (pp. 59–64)<br>
        &bull; 6 Mixed Multi-Topic Workout Spreads (pp. 65–70)<br>
        &bull; 3 Official Exam Proofreading &amp; Extended Writing Mocks (pp. 71–76)<br>
        &bull; Complete Explanatory Answer Key &amp; Mark Breakdown (pp. 77–82)<br>
        &bull; Candidate Self-Audit Checklist &amp; Progress Matrix (p. 83)
      </div>
    </div>
  </div>

  <!-- Bottom Strip -->
  <div style="background:rgba(0,0,0,0.45); padding:10mm 18mm; border-top:1px solid rgba(255,255,255,0.15); display:flex; justify-content:space-between; align-items:center;">
    <div>
      <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:8pt; letter-spacing:1px; color:#ffffff;">PEARSON EDEXCEL &bull; CITY &amp; GUILDS &bull; NCFE &bull; HIGHFIELD</div>
      <div style="font-size:7.2pt; color:rgba(255,255,255,0.7); margin-top:2px;">masterfunctionalskills.co.uk &bull; Complete 84-Page Comprehensive Manual</div>
    </div>
    <div style="text-align:right;">
      <span style="background:rgba(255,255,255,0.15); color:#ffffff; padding:4px 10px; border-radius:4px; font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.5pt; letter-spacing:0.5px;">2026/2027 EDITION</span>
    </div>
  </div>
</div>
"""


def render_inside_cover(theme):
    """Page 2: Inside Cover & Dyslexia Statement."""
    return f"""
<div class="page" style="--theme-primary:{theme['primary']}; --theme-secondary:{theme['secondary']};">
  <div class="unit-page-header">
    <div class="brand-title">MASTER FUNCTIONAL SKILLS &bull; PUBLISHING INFORMATION</div>
    <div class="strand-badge">{theme['full_name']}</div>
  </div>

  <div style="margin-bottom:8px;">
    <h1 style="font-family:'Montserrat',sans-serif; font-size:13.5pt; font-weight:900; color:{theme['primary']}; margin:0 0 2px 0;">
      Candidate &amp; Examination Centre Information
    </h1>
    <p style="font-size:7.9pt; color:#64748b; margin:0 0 6px 0;">Please record your learning details below before commencing the baseline diagnostic assessment.</p>
  </div>

  <!-- Candidate Details Form Box -->
  <div style="background:#ffffff; border:1.5px solid #cbd5e1; border-radius:6px; padding:9px 12px; margin-bottom:10px;">
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; font-size:8pt;">
      <div><strong>Candidate Full Name:</strong> <div style="border-bottom:1px dashed #94a3b8; height:18px; margin-top:2px;"></div></div>
      <div><strong>Candidate Reference / ULN:</strong> <div style="border-bottom:1px dashed #94a3b8; height:18px; margin-top:2px;"></div></div>
      <div><strong>Exam Centre Name:</strong> <div style="border-bottom:1px dashed #94a3b8; height:18px; margin-top:2px;"></div></div>
      <div><strong>Centre Number:</strong> <div style="border-bottom:1px dashed #94a3b8; height:18px; margin-top:2px;"></div></div>
      <div><strong>Course / Training Cohort:</strong> <div style="border-bottom:1px dashed #94a3b8; height:18px; margin-top:2px;"></div></div>
      <div><strong>Tutor / Assessor Name:</strong> <div style="border-bottom:1px dashed #94a3b8; height:18px; margin-top:2px;"></div></div>
    </div>
  </div>

  <!-- Dyslexia Architecture Statement -->
  <div class="card-anchor" style="border-left-color:{theme['primary']}; margin-bottom:8px;">
    <div class="card-title" style="color:{theme['primary']};">
      <span>DYSLEXIA-FRIENDLY ACCESSIBILITY &amp; TYPOGRAPHY STATEMENT</span>
    </div>
    <p style="margin:0 0 4px 0; font-size:7.9pt;">
      This publication has been developed strictly adhering to British Dyslexia Association and Ofqual educational accessibility guidelines. Reading efficiency, visual comfort, and cognitive ease are maximized through the following evidence-based features:
    </p>
    <ul style="margin:0 0 0 16px; padding:0; font-size:7.8pt; line-height:1.42;">
      <li><strong>Soft Cream Canvas (#FDFBF7):</strong> Completely eliminates the harsh optical glare and visual stress associated with high-contrast pure white backgrounds.</li>
      <li><strong>Lexend &amp; Atkinson Hyperlegible Typography:</strong> Designed with distinct character shapes to prevent common mirror-confusion traps (such as b/d/p/q).</li>
      <li><strong>Ragged-Right Left Alignment:</strong> Text is never justified, eradicating irregular spacing and disorienting 'rivers of white space' across paragraphs.</li>
      <li><strong>Generous Leading (1.48–1.52) &amp; Letter-Spacing (0.025em):</strong> Enhances horizontal eye tracking and prevents unintended line skipping.</li>
      <li><strong>Chunked Left-Bordered Cards:</strong> Distinct grammatical categories are color-coded (Context: Blue; Formula: Teal/Slate; Pitfall: Red; Golden Rule: Amber).</li>
    </ul>
  </div>

  <!-- The Murphy Method Box -->
  <div class="card-formula" style="margin-bottom:8px;">
    <div class="card-title">THE RAYMOND MURPHY 'GRAMMAR IN USE' 2-PAGE SPREAD METHOD</div>
    <p style="margin:0 0 4px 0; font-size:7.9pt;">
      Each unit is structured as an interconnected facing 2-page spread:
    </p>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:7px; font-size:7.6pt;">
      <div style="background:#f8fafc; padding:5px 7px; border-radius:4px; border:1px solid #e2e8f0;">
        <strong style="color:{theme['primary']};">LEFT-HAND PAGE (Theory &amp; Context):</strong><br>
        [A] Situational Workplace Anchor<br>
        [B] Syntax Architecture &amp; Formulas<br>
        [C] Compare &amp; Contrast (Pitfall vs Model vs Why)<br>
        [D] Examiner Golden Rule &amp; Mnemonic
      </div>
      <div style="background:#f8fafc; padding:5px 7px; border-radius:4px; border:1px solid #e2e8f0;">
        <strong style="color:{theme['primary']};">RIGHT-HAND PAGE (Progressive Drills):</strong><br>
        [Ex 1] Recognition / Binary Discrimination (4 Marks)<br>
        [Ex 2] Controlled Sentence Completion (3 Marks)<br>
        [Ex 3] Forensic Workplace Proofreading (4–5 Marks)<br>
        [Ex 4] Real-World Functional Writing Task (5 Marks)
      </div>
    </div>
  </div>

  <!-- Publishing & Copyright Notice -->
  <div style="margin-top:auto; font-size:7.1pt; color:#64748b; border-top:1px solid #e2e8f0; padding-top:5px;">
    <strong>Published by:</strong> Master Functional Skills (masterfunctionalskills.co.uk) &bull; London, United Kingdom.<br>
    &copy; 2026 Master Functional Skills. All rights reserved. Registered examination training provider and educational publisher. Calibrated for Pearson Edexcel, City &amp; Guilds, NCFE, and Highfield qualifications.
  </div>

  <div class="page-footer">
    <div>{theme['title']} &bull; Inside Cover &amp; Candidate Verification</div>
    <div class="page-num">Page 2</div>
  </div>
</div>
"""


def render_diagnostic_part1(theme, q_list):
    """Page 3: Diagnostic Assessment Part 1 (Qs 1 to 10)."""
    qs_html = ""
    for q in q_list[:10]:
        opts = " &nbsp; ".join([f"<span class='opt-box'><span class='opt-tick'></span> {opt}</span>" for opt in q["options"]])
        qs_html += f"""
        <div style="background:#ffffff; border:1px solid #e2e8f0; border-left:3.5px solid {theme['primary']}; border-radius:4px; padding:4px 8px; margin-bottom:5px; font-size:7.8pt;">
          <div style="display:flex; justify-content:space-between; margin-bottom:2px;">
            <strong>Question {q['num']}</strong>
            <span style="font-size:7.1pt; color:#64748b; font-weight:600;">{q['topic']}</span>
          </div>
          <div>{q['prompt']}</div>
          <div style="margin-top:3px;">{opts}</div>
        </div>
        """

    return f"""
<div class="page" style="--theme-primary:{theme['primary']}; --theme-secondary:{theme['secondary']};">
  <div class="unit-page-header">
    <div class="brand-title">BASELINE DIAGNOSTIC &bull; PART 1 (QUESTIONS 1 TO 10)</div>
    <div class="strand-badge">SPaG Audit: Units 1 to 8</div>
  </div>

  <div style="margin-bottom:6px;">
    <h1 style="font-family:'Montserrat',sans-serif; font-size:13pt; font-weight:900; color:{theme['primary']}; margin:0 0 2px 0;">
      Level 1 Baseline Diagnostic Assessment
    </h1>
    <p style="font-size:7.8pt; color:#64748b; margin:0 0 5px 0;">Complete all 32 diagnostic questions without assistance to pinpoint your exact SPaG strengths and revision priorities.</p>
  </div>

  <div style="display:flex; flex-direction:column; height:245mm; justify-content:flex-start;">
    {qs_html}
  </div>

  <div class="page-footer">
    <div>{theme['title']} &bull; Baseline Diagnostic Assessment (Part 1)</div>
    <div class="page-num">Page 3</div>
  </div>
</div>
"""


def render_diagnostic_part2(theme, q_list):
    """Page 4: Diagnostic Assessment Part 2 (Qs 11 to 20)."""
    qs_html = ""
    for q in q_list[10:20]:
        opts = " &nbsp; ".join([f"<span class='opt-box'><span class='opt-tick'></span> {opt}</span>" for opt in q["options"]])
        qs_html += f"""
        <div style="background:#ffffff; border:1px solid #e2e8f0; border-left:3.5px solid {theme['primary']}; border-radius:4px; padding:4px 8px; margin-bottom:5px; font-size:7.8pt;">
          <div style="display:flex; justify-content:space-between; margin-bottom:2px;">
            <strong>Question {q['num']}</strong>
            <span style="font-size:7.1pt; color:#64748b; font-weight:600;">{q['topic']}</span>
          </div>
          <div>{q['prompt']}</div>
          <div style="margin-top:3px;">{opts}</div>
        </div>
        """

    return f"""
<div class="page" style="--theme-primary:{theme['primary']}; --theme-secondary:{theme['secondary']};">
  <div class="unit-page-header">
    <div class="brand-title">BASELINE DIAGNOSTIC &bull; PART 2 (QUESTIONS 11 TO 20)</div>
    <div class="strand-badge">SPaG Audit: Units 9 to 17</div>
  </div>

  <div style="margin-bottom:6px;">
    <h1 style="font-family:'Montserrat',sans-serif; font-size:13pt; font-weight:900; color:{theme['primary']}; margin:0 0 2px 0;">
      Apostrophes, Plurals &amp; Verb Tenses
    </h1>
    <p style="font-size:7.8pt; color:#64748b; margin:0 0 5px 0;">Select one option per question. Tick the corresponding box carefully.</p>
  </div>

  <div style="display:flex; flex-direction:column; height:245mm; justify-content:flex-start;">
    {qs_html}
  </div>

  <div class="page-footer">
    <div>{theme['title']} &bull; Baseline Diagnostic Assessment (Part 2)</div>
    <div class="page-num">Page 4</div>
  </div>
</div>
"""


def render_diagnostic_part3(theme, q_list):
    """Page 5: Diagnostic Assessment Part 3 (Qs 21 to 32)."""
    qs_html = ""
    for q in q_list[20:32]:
        opts = " &nbsp; ".join([f"<span class='opt-box'><span class='opt-tick'></span> {opt}</span>" for opt in q["options"]])
        qs_html += f"""
        <div style="background:#ffffff; border:1px solid #e2e8f0; border-left:3.5px solid {theme['primary']}; border-radius:4px; padding:3.5px 7px; margin-bottom:4px; font-size:7.6pt;">
          <div style="display:flex; justify-content:space-between; margin-bottom:1px;">
            <strong>Question {q['num']}</strong>
            <span style="font-size:6.9pt; color:#64748b; font-weight:600;">{q['topic']}</span>
          </div>
          <div>{q['prompt']}</div>
          <div style="margin-top:2px;">{opts}</div>
        </div>
        """

    return f"""
<div class="page" style="--theme-primary:{theme['primary']}; --theme-secondary:{theme['secondary']};">
  <div class="unit-page-header">
    <div class="brand-title">BASELINE DIAGNOSTIC &bull; PART 3 (QUESTIONS 21 TO 32)</div>
    <div class="strand-badge">SPaG Audit: Units 18 to 26</div>
  </div>

  <div style="margin-bottom:5px;">
    <h1 style="font-family:'Montserrat',sans-serif; font-size:12.5pt; font-weight:900; color:{theme['primary']}; margin:0 0 1px 0;">
      Agreement, Homophones &amp; Morphology
    </h1>
    <p style="font-size:7.6pt; color:#64748b; margin:0 0 4px 0;">Final 12 questions auditing grammatical concord, homophone accuracy, and affix spelling.</p>
  </div>

  <div style="display:flex; flex-direction:column; height:245mm; justify-content:flex-start;">
    {qs_html}
  </div>

  <div class="page-footer">
    <div>{theme['title']} &bull; Baseline Diagnostic Assessment (Part 3)</div>
    <div class="page-num">Page 5</div>
  </div>
</div>
"""


def render_diagnostic_routing(theme, rubric, routing_map):
    """Page 6: Diagnostic Scoring Rubric, Routing Matrix & Murphy Guide."""
    rubric_html = ""
    for r in rubric:
        rubric_html += f"""
        <div style="background:#ffffff; border:1px solid #cbd5e1; border-left:4px solid {theme['secondary']}; border-radius:4px; padding:4px 8px; margin-bottom:5px; font-size:7.5pt;">
          <div style="display:flex; justify-content:space-between; font-weight:800; color:{theme['primary']}; margin-bottom:2px;">
            <span>{r['band']}</span>
            <span style="background:#f1f5f9; padding:1px 6px; border-radius:3px;">Score: {r['score_range']}</span>
          </div>
          <div style="color:#334155; margin-bottom:2px;">{r['description']}</div>
          <div style="color:{theme['primary']}; font-weight:600;"><strong>Recommended Path:</strong> {r['recommended_units']}</div>
        </div>
        """

    # Routing grid (32 questions in 4 columns)
    routing_rows = ""
    for i in range(0, len(routing_map), 4):
        chunk = routing_map[i:i+4]
        cells = ""
        for item in chunk:
            q_num, u_target, topic = item
            cells += f"<td style='padding:3px 5px; font-size:7.2pt; border:1px solid #cbd5e1;'><strong>Q{q_num}:</strong> <span style='color:{theme['primary']}; font-weight:700;'>{u_target}</span><br><span style='color:#64748b; font-size:6.8pt;'>{topic}</span></td>"
        routing_rows += f"<tr>{cells}</tr>"

    return f"""
<div class="page" style="--theme-primary:{theme['primary']}; --theme-secondary:{theme['secondary']};">
  <div class="unit-page-header">
    <div class="brand-title">DIAGNOSTIC SCORING &bull; MURPHY ROUTING MATRIX</div>
    <div class="strand-badge">Study Guide</div>
  </div>

  <div style="margin-bottom:6px;">
    <h1 style="font-family:'Montserrat',sans-serif; font-size:13pt; font-weight:900; color:{theme['primary']}; margin:0 0 2px 0;">
      Diagnostic Score Audit &amp; Unit Routing Guide
    </h1>
    <p style="font-size:7.8pt; color:#64748b; margin:0 0 5px 0;">Total your diagnostic score from Page 77 and identify your priority learning pathway.</p>
  </div>

  <!-- Scoring Rubric Cards -->
  <div style="margin-bottom:7px;">
    {rubric_html}
  </div>

  <!-- 32-Item Routing Matrix Table -->
  <div style="margin-bottom:7px;">
    <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:8pt; color:{theme['primary']}; margin-bottom:3px; text-transform:uppercase;">
      32-Item Diagnostic Question-to-Unit Mapping Grid
    </div>
    <table style="width:100%; border-collapse:collapse; background:#ffffff;">
      <tbody>
        {routing_rows}
      </tbody>
    </table>
  </div>

  <!-- The Murphy Study Guide Method -->
  <div class="card-formula" style="margin-top:auto;">
    <div class="card-title">HOW TO USE THE RAYMOND MURPHY 2-PAGE SPREADS FOR MAXIMUM EXAM SUCCESS</div>
    <div style="font-size:7.5pt; line-height:1.42; color:#334155;">
      <strong>Step 1 (Theory):</strong> Study the left-hand page. Read the situational workplace scenario [A] and structural formula [B]. Memorise the Examiner Golden Rule [D].<br>
      <strong>Step 2 (Controlled Practice):</strong> Complete Exercise 1 (Recognition) and Exercise 2 (Sentence Completion) on the right-hand page.<br>
      <strong>Step 3 (Forensic Proofreading):</strong> Scan Exercise 3. Find and correct the EXACT number of deliberate workplace errors.<br>
      <strong>Step 4 (Applied Writing):</strong> Write your response in Exercise 4 using the target grammatical structure. Check against the Complete Answer Key (pp. 77–82).
    </div>
  </div>

  <div class="page-footer">
    <div>{theme['title']} &bull; Diagnostic Scoring &amp; Study Guide</div>
    <div class="page-num">Page 6</div>
  </div>
</div>
"""


def render_unit_left_page(theme, unit_data, page_num):
    """Generates Unit Left Page (Odd: 7, 9, 11...): Theory & Visuals."""
    u_num = unit_data["unit"]
    u_title = unit_data["title"]
    fmt = unit_data.get("format", "Workplace Document")

    anchor_title = unit_data.get("anchor_title", f"Workplace Application: {fmt}")
    anchor_text = unit_data.get("anchor_text", "Accurate syntax is essential in this vocational format to maintain professional credibility.")
    formula_title = unit_data.get("rule_formula_title", "Syntax Architecture & Core Structural Rules")
    formula_html = unit_data.get("rule_formula_html", "")
    bad_text = unit_data.get("worked_bad", "Example with error.")
    good_text = unit_data.get("worked_good", "Corrected example.")
    why_text = unit_data.get("worked_why", "Clear grammatical rationale.")
    golden_rule = unit_data.get("golden_rule", "Always verify sentence boundaries and verb agreement before submitting exam scripts.")

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
    <div class="card-anchor">
      <div class="card-title">[A] Situational Workplace Anchor: {anchor_title}</div>
      <p style="margin:0; font-size:8pt;">{anchor_text}</p>
    </div>

    <div class="card-formula">
      <div class="card-title">[B] {formula_title}</div>
      <div style="font-size:7.9pt; line-height:1.45;">{formula_html}</div>
    </div>

    <div class="card-compare">
      <div class="compare-row-bad">
        <span class="compare-badge badge-bad">❌ Pitfall</span>
        <span style="font-size:7.9pt; color:#991b1b;">{bad_text}</span>
      </div>
      <div class="compare-row-good">
        <span class="compare-badge badge-good">✔️ Model</span>
        <span style="font-size:7.9pt; color:#166534; font-weight:600;">{good_text}</span>
      </div>
      <div class="compare-row-why">
        <span class="compare-badge badge-why">💡 Examiner Why</span>
        <span>{why_text}</span>
      </div>
    </div>

    <div class="card-golden">
      <div class="card-title">[D] Examiner Golden Rule &amp; Memory Hook</div>
      <p style="margin:0; font-size:7.8pt;">{golden_rule}</p>
    </div>
  </div>

  <div class="page-footer">
    <div>{theme['title']} &bull; Unit {u_num}: {u_title}</div>
    <div class="page-num">Page {page_num}</div>
  </div>
</div>
"""


def render_unit_right_page(theme, unit_data, page_num):
    """Generates Unit Right Page (Even: 8, 10, 12...): Progressive Drills."""
    u_num = unit_data["unit"]
    u_title = unit_data["title"]
    fmt = unit_data.get("format", "Workplace Document")

    # Ex 1: Recognition / Discrimination (4 Items)
    ex1_html = ""
    for idx, item in enumerate(unit_data.get("exercise_a", [])[:4], 1):
        q_text, opts, _ = item
        opts_rendered = " &nbsp; ".join([f"<span class='opt-box'><span class='opt-tick'></span> {opt}</span>" for opt in opts])
        ex1_html += f"""
        <div style="margin-bottom:3.5px; font-size:7.6pt;">
          <div><strong>{idx}.</strong> {q_text}</div>
          <div style="margin-top:1.5px;">{opts_rendered}</div>
        </div>
        """

    # Ex 2: Controlled Sentence Completion / Transformation (3 Items)
    ex2_html = ""
    for idx, item in enumerate(unit_data.get("exercise_b", [])[:3], 1):
        instruction, prompt, _ = item
        ex2_html += f"""
        <div style="margin-bottom:2.5px; font-size:7.6pt;">
          <strong>{idx}. [{instruction}]:</strong> <em>"{prompt}"</em>
          <div style="border-bottom:1px dashed #cbd5e1; height:12px; margin-top:1px;"></div>
        </div>
        """

    # Ex 3: Forensic Workplace Proofreading
    doc_title = unit_data.get("proofreading_title", f"Vocational Proofreading: {fmt}")
    doc_scenario = unit_data.get("proofreading_scenario", "Examine this workplace document. Identify the deliberate errors.")
    doc_text = unit_data.get("proofreading_text", "")
    err_count = unit_data.get("proofreading_err_count", 4)

    # Ex 4: Applied Writing Task
    writing_prompt = unit_data.get("writing_prompt", "Draft two complete sentences demonstrating the target SPaG rule.")

    return f"""
<div class="page" style="--theme-primary:{theme['primary']}; --theme-secondary:{theme['secondary']};">
  <div class="unit-page-header">
    <div class="brand-title">UNIT {u_num} &bull; 4-TIER PRACTICE DRILLS</div>
    <div class="strand-badge">{theme['code']} Drills</div>
  </div>

  <div class="unit-main-heading">
    <span class="unit-num-pill">UNIT {u_num} DRILLS</span>
    <h2 class="unit-title-text">{u_title}</h2>
  </div>

  <div style="display:flex; flex-direction:column; height:245mm; justify-content:space-between;">
    <!-- EXERCISE 1: RECOGNITION -->
    <div class="exercise-section">
      <div class="ex-header">
        <span class="ex-title">[EXERCISE 1] Recognition &amp; Discrimination</span>
        <span class="ex-marks">4 Marks</span>
      </div>
      <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:5px; padding:4px 7px;">
        {ex1_html}
      </div>
    </div>

    <!-- EXERCISE 2: CONTROLLED COMPLETION -->
    <div class="exercise-section">
      <div class="ex-header">
        <span class="ex-title">[EXERCISE 2] Controlled Sentence Completion</span>
        <span class="ex-marks">3 Marks</span>
      </div>
      <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:5px; padding:4px 7px;">
        {ex2_html}
      </div>
    </div>

    <!-- EXERCISE 3: FORENSIC PROOFREADING -->
    <div class="exercise-section">
      <div class="ex-header">
        <span class="ex-title">[EXERCISE 3] Forensic Workplace Proofreading</span>
        <span class="ex-marks">{err_count} Marks</span>
      </div>
      <div class="workplace-doc">
        <div class="doc-topbar">
          <span>{doc_title.upper()}</span>
          <span>EXACT ERRORS TO FIND: {err_count}</span>
        </div>
        <div class="doc-meta">
          <strong>Scenario:</strong> {doc_scenario}
        </div>
        <div class="doc-body" style="font-size:7.8pt;">
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
        <div class="task-lines" style="height:48px;"></div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div>{theme['title']} &bull; Unit {u_num}: Practice Drills</div>
    <div class="page-num">Page {page_num}</div>
  </div>
</div>
"""


def render_vocab_module_page(theme, mod_data):
    """Pages 59–64: Vocabulary in Use Master Modules."""
    p_num = mod_data["page"]
    m_num = mod_data["module"]
    title = mod_data["title"]
    subtitle = mod_data["subtitle"]
    intro = mod_data["intro"]

    tables_html = ""
    for t in mod_data["tables"]:
        heading = t["heading"]
        headers = t["headers"]
        th_cells = "".join([f"<th style='padding:3px 6px; font-size:7.2pt; border:1px solid #cbd5e1; background:{theme['primary']}; color:#ffffff;'>{h}</th>" for h in headers])
        rows_cells = ""
        for r in t["rows"]:
            td_cells = "".join([f"<td style='padding:3px 6px; font-size:7.3pt; border:1px solid #cbd5e1;'>{cell}</td>" for cell in r])
            rows_cells += f"<tr>{td_cells}</tr>"

        tables_html += f"""
        <div style="margin-bottom:6px;">
          <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.8pt; color:{theme['primary']}; margin-bottom:2px; text-transform:uppercase;">
            {heading}
          </div>
          <table style="width:100%; border-collapse:collapse; background:#ffffff;">
            <thead><tr>{th_cells}</tr></thead>
            <tbody>{rows_cells}</tbody>
          </table>
        </div>
        """

    drill = mod_data["drill"]
    drill_html = f"""
    <div style="background:#ffffff; border:1px solid #cbd5e1; border-left:4px solid {theme['amber']}; border-radius:5px; padding:5px 8px; margin-top:auto;">
      <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.6pt; color:#b45309; text-transform:uppercase; margin-bottom:2px;">
        VOCABULARY APPLICATION DRILL
      </div>
      <div style="font-size:7.4pt; margin-bottom:2px;"><strong>Task:</strong> {drill['prompt']}</div>
      <div style="font-size:7.3pt; color:#991b1b; margin-bottom:1px;">❌ <em>{drill['bad']}</em></div>
      <div style="font-size:7.3pt; color:#166534; font-weight:600;">✔️ <em>{drill['model']}</em></div>
    </div>
    """

    return f"""
<div class="page" style="--theme-primary:{theme['primary']}; --theme-secondary:{theme['secondary']};">
  <div class="unit-page-header">
    <div class="brand-title">VOCABULARY IN USE &bull; MODULE {m_num}</div>
    <div class="strand-badge">{theme['code']} Vocabulary</div>
  </div>

  <div style="margin-bottom:6px;">
    <h1 style="font-family:'Montserrat',sans-serif; font-size:12.5pt; font-weight:900; color:{theme['primary']}; margin:0 0 1px 0;">
      {title}
    </h1>
    <p style="font-size:7.6pt; color:#64748b; margin:0 0 4px 0;">{subtitle} &bull; {intro}</p>
  </div>

  <div style="display:flex; flex-direction:column; height:245mm; justify-content:space-between;">
    <div>
      {tables_html}
    </div>
    {drill_html}
  </div>

  <div class="page-footer">
    <div>{theme['title']} &bull; Vocabulary in Use (Module {m_num})</div>
    <div class="page-num">Page {p_num}</div>
  </div>
</div>
"""


def render_mixed_workout_page(theme, workout_data):
    """Pages 65–70: Murphy-Style Mixed Additional Exercises."""
    p_num = workout_data["page"]
    w_num = workout_data["workout_num"]
    title = workout_data["title"]
    coverage = workout_data["coverage"]
    intro = workout_data["intro"]

    drills = workout_data["drills"]
    part_a = drills[0]
    part_b = drills[1]
    part_c = drills[2]

    # Part A items
    pa_html = ""
    for idx, item in enumerate(part_a["items"], 1):
        q_text, opts, _ = item
        opts_rendered = " &nbsp; ".join([f"<span class='opt-box'><span class='opt-tick'></span> {opt}</span>" for opt in opts])
        pa_html += f"""
        <div style="margin-bottom:2.5px; font-size:7.4pt;">
          <strong>{idx}.</strong> {q_text}
          <div style="margin-top:1px;">{opts_rendered}</div>
        </div>
        """

    # Part B items
    pb_html = ""
    for idx, item in enumerate(part_b["items"], 1):
        instruction, prompt, _ = item
        pb_html += f"""
        <div style="margin-bottom:2px; font-size:7.4pt;">
          <strong>{idx}. [{instruction}]:</strong> <em>"{prompt}"</em>
          <div style="border-bottom:1px dashed #cbd5e1; height:11px; margin-top:1px;"></div>
        </div>
        """

    # Part C
    pc_html = f"""
    <div class="workplace-doc" style="margin-bottom:0;">
      <div class="doc-topbar">
        <span>{part_c['section'].upper()}</span>
        <span>EXACT ERRORS TO FIND: {part_c['err_count']}</span>
      </div>
      <div class="doc-meta" style="font-size:7.2pt;">
        <strong>Context:</strong> {part_c['scenario']}
      </div>
      <div class="doc-body" style="font-size:7.6pt; line-height:1.4;">
        {part_c['text']}
      </div>
    </div>
    """

    return f"""
<div class="page" style="--theme-primary:{theme['primary']}; --theme-secondary:{theme['secondary']};">
  <div class="unit-page-header">
    <div class="brand-title">MIXED WORKOUT &bull; WORKOUT {w_num}</div>
    <div class="strand-badge">{coverage}</div>
  </div>

  <div style="margin-bottom:5px;">
    <h1 style="font-family:'Montserrat',sans-serif; font-size:12.5pt; font-weight:900; color:{theme['primary']}; margin:0 0 1px 0;">
      {title}
    </h1>
    <p style="font-size:7.6pt; color:#64748b; margin:0 0 4px 0;">{intro}</p>
  </div>

  <div style="display:flex; flex-direction:column; height:245mm; justify-content:space-between;">
    <!-- Part A -->
    <div class="exercise-section">
      <div class="ex-header">
        <span class="ex-title">{part_a['section']}</span>
      </div>
      <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:4px; padding:3px 6px;">
        {pa_html}
      </div>
    </div>

    <!-- Part B -->
    <div class="exercise-section">
      <div class="ex-header">
        <span class="ex-title">{part_b['section']}</span>
      </div>
      <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:4px; padding:3px 6px;">
        {pb_html}
      </div>
    </div>

    <!-- Part C -->
    <div class="exercise-section" style="margin-top:auto;">
      <div class="ex-header">
        <span class="ex-title">[PART C] Forensic Multi-Error Proofreading ({part_c['err_count']} Marks)</span>
      </div>
      {pc_html}
    </div>
  </div>

  <div class="page-footer">
    <div>{theme['title']} &bull; Mixed Additional Workout {w_num}</div>
    <div class="page-num">Page {p_num}</div>
  </div>
</div>
"""


def render_exam_mock_proof_page(theme, mock_data):
    """Pages 71, 73, 75: Official Exam Proofreading Mocks."""
    p_num = mock_data["page_proof"]
    m_num = mock_data["mock_num"]
    title = mock_data["title"]
    subtitle = mock_data["subtitle"]
    fmt = mock_data["format"]

    scenario = mock_data["proof_scenario"]
    doc_meta = scenario["doc_meta"]
    text = scenario["text"]
    err_count = scenario["err_count"]

    # Candidate Error Table (6 rows)
    rows_html = ""
    for r in range(1, err_count + 1):
        rows_html += f"""
        <tr>
          <td style="text-align:center; font-weight:700; width:10%; border:1px solid #cbd5e1; padding:4px;">{r}</td>
          <td style="width:45%; border:1px solid #cbd5e1; padding:4px;"></td>
          <td style="width:45%; border:1px solid #cbd5e1; padding:4px;"></td>
        </tr>
        """

    return f"""
<div class="page" style="--theme-primary:{theme['primary']}; --theme-secondary:{theme['secondary']};">
  <div class="unit-page-header">
    <div class="brand-title">OFFICIAL EXAM MOCK &bull; TASK {m_num} (PART 1)</div>
    <div class="strand-badge">{fmt}</div>
  </div>

  <div style="margin-bottom:6px;">
    <h1 style="font-family:'Montserrat',sans-serif; font-size:12.5pt; font-weight:900; color:{theme['primary']}; margin:0 0 1px 0;">
      {title}
    </h1>
    <p style="font-size:7.6pt; color:#64748b; margin:0 0 5px 0;">{subtitle} &bull; Section A: Proofreading &amp; Error Identification</p>
  </div>

  <div style="display:flex; flex-direction:column; height:245mm; justify-content:space-between;">
    <!-- Workplace Scenario Box -->
    <div class="workplace-doc">
      <div class="doc-topbar">
        <span>{scenario['title']}</span>
        <span>EXACT ERRORS: {err_count}</span>
      </div>
      <div class="doc-meta" style="font-size:7.4pt;">
        <strong>Instructions:</strong> {scenario['context']}<br>
        <strong>Document Metadata:</strong> {doc_meta}
      </div>
      <div class="doc-body" style="font-size:8pt; line-height:1.48;">
        {text}
      </div>
    </div>

    <!-- Candidate Correction Table -->
    <div style="margin-top:auto;">
      <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.8pt; color:{theme['primary']}; margin-bottom:3px; text-transform:uppercase;">
        Candidate Error Identification Log Table (6 Marks)
      </div>
      <table style="width:100%; border-collapse:collapse; background:#ffffff;">
        <thead>
          <tr style="background:{theme['primary']}; color:#ffffff; font-size:7.2pt; text-transform:uppercase;">
            <th style="padding:4px; border:1px solid #cbd5e1; width:10%;">Err #</th>
            <th style="padding:4px; border:1px solid #cbd5e1; width:45%;">Incorrect Word / Punctuation</th>
            <th style="padding:4px; border:1px solid #cbd5e1; width:45%;">Corrected Replacement &amp; Grammar Rule</th>
          </tr>
        </thead>
        <tbody>
          {rows_html}
        </tbody>
      </table>
    </div>
  </div>

  <div class="page-footer">
    <div>{theme['title']} &bull; Exam Mock {m_num}: Proofreading Task</div>
    <div class="page-num">Page {p_num}</div>
  </div>
</div>
"""


def render_exam_mock_writing_page(theme, mock_data):
    """Pages 72, 74, 76: Official Exam Extended Writing with Ruled Writing Frames."""
    p_num = mock_data["page_writing"]
    m_num = mock_data["mock_num"]
    title = mock_data["title"]
    fmt = mock_data["format"]

    w_task = mock_data["writing_task"]
    prompt = w_task["prompt"]
    breakdown = w_task["marks_breakdown"]
    line_count = w_task.get("ruled_lines_count", 16)

    return f"""
<div class="page" style="--theme-primary:{theme['primary']}; --theme-secondary:{theme['secondary']};">
  <div class="unit-page-header">
    <div class="brand-title">OFFICIAL EXAM MOCK &bull; TASK {m_num} (PART 2)</div>
    <div class="strand-badge">{fmt} Writing Frame</div>
  </div>

  <div style="margin-bottom:6px;">
    <h1 style="font-family:'Montserrat',sans-serif; font-size:12.5pt; font-weight:900; color:{theme['primary']}; margin:0 0 1px 0;">
      {w_task['title']}
    </h1>
    <p style="font-size:7.6pt; color:#64748b; margin:0 0 4px 0;">{breakdown}</p>
  </div>

  <div style="display:flex; flex-direction:column; height:245mm; justify-content:space-between;">
    <!-- Writing Prompt & Requirements -->
    <div style="background:#ffffff; border:1.5px solid #cbd5e1; border-left:4px solid {theme['primary']}; border-radius:5px; padding:6px 9px;">
      <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.8pt; color:{theme['primary']}; margin-bottom:2px; text-transform:uppercase;">
        EXAMINATION WRITING PROMPT &amp; SPECIFICATION
      </div>
      <div style="font-size:7.8pt; line-height:1.42; color:#1e293b;">
        {prompt}
      </div>
    </div>

    <!-- Pre-Writing Plan Box -->
    <div style="background:#f8fafc; border:1px dashed #94a3b8; border-radius:4px; padding:4px 8px; font-size:7.3pt;">
      <strong style="color:{theme['primary']};">PRE-WRITING PLANNING SPACE (Audience, Register &amp; Key Points):</strong>
      <div style="border-bottom:1px dashed #cbd5e1; height:12px; margin-top:1px;"></div>
      <div style="border-bottom:1px dashed #cbd5e1; height:12px; margin-top:1px;"></div>
    </div>

    <!-- Ruled Examination Writing Frame -->
    <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:5px; padding:6px 10px; margin-top:auto;">
      <div style="display:flex; justify-content:space-between; font-size:7.2pt; color:#64748b; font-family:'Montserrat',sans-serif; font-weight:700; margin-bottom:4px; border-bottom:1px solid #e2e8f0; padding-bottom:2px;">
        <span>CANDIDATE RESPONSE WORKSPACE</span>
        <span>WORD COUNT GUIDELINE: 80–110 WORDS</span>
      </div>
      <div style="background: repeating-linear-gradient(transparent, transparent 18px, #cbd5e1 19px, #cbd5e1 20px); height:135mm; border-radius:2px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <div>{theme['title']} &bull; Exam Mock {m_num}: Extended Writing Task</div>
    <div class="page-num">Page {p_num}</div>
  </div>
</div>
"""


def render_answer_key_page(theme, page_num, key_data):
    """Pages 77–82: Comprehensive Explanatory Answer Key with Examiner Mark Breakdown."""
    title = key_data["title"]

    content_html = ""
    # Diagnostic answers (Page 77)
    if "diagnostic_answers" in key_data:
        diag_items = ""
        for i in range(0, len(key_data["diagnostic_answers"]), 2):
            left = key_data["diagnostic_answers"][i]
            right = key_data["diagnostic_answers"][i+1] if i+1 < len(key_data["diagnostic_answers"]) else ""
            diag_items += f"""
            <tr>
              <td style="padding:2.5px 5px; font-size:6.9pt; border:1px solid #cbd5e1; width:50%;">{left}</td>
              <td style="padding:2.5px 5px; font-size:6.9pt; border:1px solid #cbd5e1; width:50%;">{right}</td>
            </tr>
            """
        content_html += f"""
        <div style="margin-bottom:6px;">
          <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.8pt; color:{theme['primary']}; margin-bottom:2px; text-transform:uppercase;">
            Diagnostic Assessment Complete Answer Key (Questions 1 to 32)
          </div>
          <table style="width:100%; border-collapse:collapse; background:#ffffff;">
            <tbody>{diag_items}</tbody>
          </table>
        </div>
        """

    # Units answers
    if "units" in key_data:
        for u_num, u_ans in key_data["units"].items():
            content_html += f"""
            <div style="background:#ffffff; border:1px solid #cbd5e1; border-left:3.5px solid {theme['primary']}; border-radius:4px; padding:3.5px 7px; margin-bottom:4px; font-size:7.2pt;">
              <div style="font-weight:800; color:{theme['primary']}; margin-bottom:1px;">UNIT {u_num} DRILLS &amp; WORKPLACE PROOFREADING</div>
              <div><strong>[Ex 1 Recognition]:</strong> {u_ans['ex_a']} &bull; <strong>[Ex 2 Completion]:</strong> {u_ans['ex_b']}</div>
              <div style="color:#0f766e; margin-top:1px;"><strong>[Ex 3 Proofreading Errors]:</strong> {u_ans['proof']}</div>
            </div>
            """

    # Vocab modules (Page 81)
    if "vocab_modules" in key_data:
        content_html += f"""
        <div style="margin-top:6px; margin-bottom:4px;">
          <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.8pt; color:{theme['primary']}; margin-bottom:2px; text-transform:uppercase;">
            Vocabulary in Use Modules 1 to 6 Model Solutions
          </div>
        """
        for m_num, m_ans in key_data["vocab_modules"].items():
            content_html += f"""
            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-left:3px solid {theme['secondary']}; padding:3px 6px; margin-bottom:3px; font-size:7.1pt;">
              <strong>Module {m_num}:</strong> {m_ans}
            </div>
            """
        content_html += "</div>"

    # Mixed workouts (Page 82)
    if "mixed_workouts" in key_data:
        content_html += f"""
        <div style="margin-bottom:6px;">
          <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.8pt; color:{theme['primary']}; margin-bottom:2px; text-transform:uppercase;">
            Mixed Workouts 1 to 6 Multi-Topic Solutions
          </div>
        """
        for w_num, w_ans in key_data["mixed_workouts"].items():
            content_html += f"""
            <div style="background:#ffffff; border:1px solid #cbd5e1; border-left:3px solid {theme['secondary']}; padding:3px 6px; margin-bottom:3px; font-size:7.1pt;">
              <strong>Workout {w_num}:</strong> [Part A]: {w_ans['part_a']} | [Part B]: {w_ans['part_b']} | <span style="color:#0f766e;"><strong>[Part C Errors]:</strong> {w_ans['part_c']}</span>
            </div>
            """
        content_html += "</div>"

    # Exam mocks (Page 82)
    if "exam_mocks" in key_data:
        content_html += f"""
        <div style="margin-top:5px;">
          <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.8pt; color:{theme['primary']}; margin-bottom:2px; text-transform:uppercase;">
            Official Exam Mocks 1 to 3 Mark Schemes &amp; Writing Rubrics
          </div>
        """
        for m_num, m_ans in key_data["exam_mocks"].items():
            proof_str = " &bull; ".join(m_ans["proof_answers"])
            content_html += f"""
            <div style="background:#f8fafc; border:1px solid #cbd5e1; border-left:3.5px solid {theme['primary']}; padding:3.5px 6px; margin-bottom:3px; font-size:7pt;">
              <strong>Mock {m_num} (Proofreading 6 Marks):</strong> {proof_str}<br>
              <strong>Mock {m_num} (Writing 12 Marks):</strong> {m_ans['writing_rubric']}
            </div>
            """
        content_html += "</div>"

    return f"""
<div class="page" style="--theme-primary:{theme['primary']}; --theme-secondary:{theme['secondary']};">
  <div class="unit-page-header">
    <div class="brand-title">EXPLANATORY ANSWER KEY &bull; EXAMINER MARK BREAKDOWN</div>
    <div class="strand-badge">Page {page_num} of 84</div>
  </div>

  <div style="margin-bottom:6px;">
    <h1 style="font-family:'Montserrat',sans-serif; font-size:12.5pt; font-weight:900; color:{theme['primary']}; margin:0 0 1px 0;">
      {title}
    </h1>
    <p style="font-size:7.6pt; color:#64748b; margin:0 0 4px 0;">Full solutions, diagnostic mappings, proofreading error logs, and examiner marking criteria.</p>
  </div>

  <div style="display:flex; flex-direction:column; height:245mm; justify-content:flex-start;">
    {content_html}
  </div>

  <div class="page-footer">
    <div>{theme['title']} &bull; Complete Answer Key (Part {page_num - 76})</div>
    <div class="page-num">Page {page_num}</div>
  </div>
</div>
"""


def render_audit_page(theme, units_list):
    """Page 83: Candidate Self-Audit Checklist & Progress Matrix."""
    rows_html = ""
    for u in units_list:
        u_num = u["unit"]
        u_title = u["title"]
        rows_html += f"""
        <tr>
          <td style="font-weight:700; text-align:center; padding:2px 4px; border:1px solid #cbd5e1; font-size:6.9pt;">Unit {u_num}</td>
          <td style="padding:2px 5px; border:1px solid #cbd5e1; font-size:7pt;"><strong>{u_title}</strong></td>
          <td style="text-align:center; padding:2px 4px; border:1px solid #cbd5e1;">
            <span class="rag-pill rag-red"></span>
            <span class="rag-pill rag-amber"></span>
            <span class="rag-pill rag-green"></span>
          </td>
          <td style="border:1px solid #cbd5e1; padding:2px 4px;"></td>
          <td style="border:1px solid #cbd5e1; padding:2px 4px;"></td>
        </tr>
        """

    return f"""
<div class="page" style="--theme-primary:{theme['primary']}; --theme-secondary:{theme['secondary']};">
  <div class="unit-page-header">
    <div class="brand-title">CANDIDATE SELF-AUDIT &bull; PROGRESS MATRIX</div>
    <div class="strand-badge">26-Unit Tracking Grid</div>
  </div>

  <div style="margin-bottom:5px;">
    <h1 style="font-family:'Montserrat',sans-serif; font-size:12.5pt; font-weight:900; color:{theme['primary']}; margin:0 0 1px 0;">
      Level 1 SPaG Competency Self-Audit &amp; Assessor Sign-Off
    </h1>
    <p style="font-size:7.5pt; color:#64748b; margin:0 0 4px 0;">Track your mastery across all 26 units. Tick Red (Needs Revision), Amber (Developing), or Green (Mastered).</p>
  </div>

  <!-- Full 26-Unit Audit Table -->
  <table style="width:100%; border-collapse:collapse; background:#ffffff; margin-bottom:5px;">
    <thead>
      <tr style="background:{theme['primary']}; color:#ffffff; font-size:7pt; text-transform:uppercase;">
        <th style="padding:3px; border:1px solid #cbd5e1; width:12%;">Unit #</th>
        <th style="padding:3px; border:1px solid #cbd5e1; width:52%;">Topic &amp; Target Grammatical Competency</th>
        <th style="padding:3px; border:1px solid #cbd5e1; width:14%;">RAG Status</th>
        <th style="padding:3px; border:1px solid #cbd5e1; width:11%;">Date</th>
        <th style="padding:3px; border:1px solid #cbd5e1; width:11%;">Sign-off</th>
      </tr>
    </thead>
    <tbody>
      {rows_html}
    </tbody>
  </table>

  <!-- Final Assessment Declaration Box -->
  <div style="background:#f8fafc; border:1.5px solid #cbd5e1; border-radius:5px; padding:5px 8px; margin-top:auto; font-size:7.2pt;">
    <div style="font-family:'Montserrat',sans-serif; font-weight:800; color:{theme['primary']}; text-transform:uppercase; margin-bottom:2px;">
      TUTOR / ASSESSOR FINAL COMPETENCY VERIFICATION
    </div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:6px;">
      <div>Candidate Overall SPaG Competency: [ &nbsp; ] Pass Ready &nbsp; [ &nbsp; ] Further Practice Needed</div>
      <div>Assessor Signature: <span style="border-bottom:1px dashed #94a3b8; display:inline-block; width:120px;"></span></div>
    </div>
  </div>

  <div class="page-footer">
    <div>{theme['title']} &bull; Candidate Self-Audit &amp; Progress Matrix</div>
    <div class="page-num">Page 83</div>
  </div>
</div>
"""


def render_back_cover(theme):
    """Page 84: High-Impact Back Cover."""
    return f"""
<div class="page cover-page" style="background: linear-gradient(145deg, {theme['cover_grad_start']} 0%, {theme['cover_grad_mid']} 55%, {theme['cover_grad_end']} 100%);">
  <div style="padding: 16mm 18mm 0 18mm;">
    <!-- Top Header -->
    <div style="display:flex; justify-content:space-between; align-items:center; border-bottom: 1.5px solid rgba(255,255,255,0.25); padding-bottom:12px;">
      <div>
        <div style="font-family:'Montserrat',sans-serif; font-size:13pt; font-weight:900; letter-spacing:2.5px; color:#ffffff;">MASTER FUNCTIONAL SKILLS</div>
        <div style="font-size:7.5pt; font-weight:700; letter-spacing:1.5px; color:#fbbf24; margin-top:2px;">OFFICIAL EXAM REVISION &amp; SELF-STUDY SERIES</div>
      </div>
      <div style="background:{theme['badge_bg']}; color:#ffffff; font-family:'Montserrat',sans-serif; font-weight:900; font-size:8.5pt; padding:6px 14px; border-radius:20px; letter-spacing:1px; border:1px solid rgba(255,255,255,0.3);">
        COMPLETE 84 PAGES
      </div>
    </div>

    <!-- Main Overview -->
    <div style="margin-top:16mm;">
      <h2 style="font-family:'Montserrat',sans-serif; font-size:18pt; font-weight:900; color:#ffffff; line-height:1.2; margin:0 0 6px 0;">
        THE DEFINITIVE LEVEL 1 SPAG REVISION MANUAL
      </h2>
      <p style="font-size:8.5pt; color:rgba(255,255,255,0.9); line-height:1.5; max-width:165mm;">
        Master Functional Skills SPaG Level 1 Mastery is the United Kingdom's most thorough and accessible educational workbook for candidates preparing for Pearson Edexcel, City &amp; Guilds, NCFE, and Highfield Functional Skills English examinations.
      </p>
    </div>

    <!-- 3 Pillars Grid -->
    <div style="display:grid; grid-template-columns:1fr; gap:9px; margin-top:12mm;">
      <div style="background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.18); border-left:4px solid #38bdf8; border-radius:6px; padding:7px 11px;">
        <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:8.2pt; color:#ffffff;">RAYMOND MURPHY 'GRAMMAR IN USE' PEDAGOGY</div>
        <div style="font-size:7.4pt; color:rgba(255,255,255,0.85); margin-top:2px;">26 facing two-page spreads delivering structured situational theory [A], syntax formulas [B], compare &amp; contrast analysis [C], and progressive 4-tier drills.</div>
      </div>
      <div style="background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.18); border-left:4px solid #34d399; border-radius:6px; padding:7px 11px;">
        <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:8.2pt; color:#ffffff;">BRITISH DYSLEXIA ASSOCIATION COMPLIANT</div>
        <div style="font-size:7.4pt; color:rgba(255,255,255,0.85); margin-top:2px;">Specialist #FDFBF7 warm cream anti-glare canvas, Lexend typography, generous 1.5 leading, ragged-right alignment, and color-coded cognitive cards.</div>
      </div>
      <div style="background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.18); border-left:4px solid #fbbf24; border-radius:6px; padding:7px 11px;">
        <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:8.2pt; color:#ffffff;">EXHAUSTIVE PRACTICE &amp; EXAM PAPERS</div>
        <div style="font-size:7.4pt; color:rgba(255,255,255,0.85); margin-top:2px;">32-question diagnostic assessment, 6 vocabulary modules, 6 mixed multi-topic workouts, 3 official exam mocks with ruled writing frames, and a complete 6-page answer key.</div>
      </div>
    </div>

    <!-- Publishing Details & ISBN Barcode Box -->
    <div style="margin-top:14mm; display:flex; justify-content:space-between; align-items:flex-end; background:rgba(0,0,0,0.25); border:1px solid rgba(255,255,255,0.15); border-radius:6px; padding:10px 14px;">
      <div style="font-size:7.3pt; color:rgba(255,255,255,0.8); line-height:1.45;">
        <strong>Master Functional Skills English Series:</strong><br>
        &bull; Entry Level 3 Core Foundations (Ruby Crimson)<br>
        &bull; Level 1 Comprehensive Mastery (Emerald Teal) &mdash; <em>This Publication</em><br>
        &bull; Level 2 Advanced Mastery (Deep Navy)<br><br>
        <strong>Web:</strong> masterfunctionalskills.co.uk &bull; <strong>ISBN:</strong> 978-1-91684-26-8
      </div>
      <!-- Mock Barcode Container -->
      <div style="background:#ffffff; padding:4px 8px; border-radius:4px; text-align:center;">
        <div style="font-family:'Courier New',monospace; font-size:14pt; font-weight:900; letter-spacing:3px; color:#000000; line-height:1;">
          ||||| | |||| ||| |||| |
        </div>
        <div style="font-family:'Courier New',monospace; font-size:6pt; color:#000000; margin-top:1px;">
          978191684268
        </div>
      </div>
    </div>
  </div>

  <!-- Bottom Brand Bar -->
  <div style="background:rgba(0,0,0,0.45); padding:9mm 18mm; border-top:1px solid rgba(255,255,255,0.15); display:flex; justify-content:space-between; align-items:center;">
    <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:8pt; letter-spacing:1px; color:#ffffff;">
      MASTER FUNCTIONAL SKILLS &bull; LONDON, UNITED KINGDOM
    </div>
    <div style="font-size:7.2pt; color:rgba(255,255,255,0.7);">
      &copy; 2026 Master Functional Skills. All rights reserved.
    </div>
  </div>
</div>
"""


# =============================================================================
# MASTER BUILDER ASSEMBLY
# =============================================================================

def build_84p_book():
    print("=" * 80)
    print("MASTER FUNCTIONAL SKILLS: COMPILING 84-PAGE LEVEL 1 SPAG MASTERY PUBLICATION")
    print("=" * 80)
    start_time = time.time()

    pages_html = []

    # Page 1: Front Cover
    print("[1/84] Rendering Page 1: Front Cover...")
    pages_html.append(render_front_cover(THEME))

    # Page 2: Inside Cover & Dyslexia Statement
    print("[2/84] Rendering Page 2: Inside Cover & Dyslexia Statement...")
    pages_html.append(render_inside_cover(THEME))

    # Pages 3–6: Baseline Diagnostic Assessment & Routing Guide (4 pages)
    print("[3/84] Rendering Page 3: Diagnostic Assessment Part 1 (Qs 1–10)...")
    pages_html.append(render_diagnostic_part1(THEME, spag_l1_84p_data.L1_DIAGNOSTIC_32))

    print("[4/84] Rendering Page 4: Diagnostic Assessment Part 2 (Qs 11–20)...")
    pages_html.append(render_diagnostic_part2(THEME, spag_l1_84p_data.L1_DIAGNOSTIC_32))

    print("[5/84] Rendering Page 5: Diagnostic Assessment Part 3 (Qs 21–32)...")
    pages_html.append(render_diagnostic_part3(THEME, spag_l1_84p_data.L1_DIAGNOSTIC_32))

    print("[6/84] Rendering Page 6: Diagnostic Scoring & Murphy Routing Matrix...")
    pages_html.append(render_diagnostic_routing(THEME, spag_l1_84p_data.L1_DIAGNOSTIC_RUBRIC, spag_l1_84p_data.L1_ROUTING_MAP))

    # Pages 7–58: 26 Two-Page Units (52 pages)
    cur_p = 7
    for u in spag_l1_84p_units.L1_UNITS_26:
        u_num = u["unit"]
        print(f"[{cur_p}/84] Rendering Page {cur_p}: Unit {u_num} Left (Theory & Architecture)...")
        pages_html.append(render_unit_left_page(THEME, u, cur_p))
        cur_p += 1

        print(f"[{cur_p}/84] Rendering Page {cur_p}: Unit {u_num} Right (4-Tier Practice Drills)...")
        pages_html.append(render_unit_right_page(THEME, u, cur_p))
        cur_p += 1

    # Pages 59–64: Vocabulary in Use Master Modules (6 pages)
    for mod in spag_l1_84p_data.VOCAB_MODULES:
        print(f"[{cur_p}/84] Rendering Page {cur_p}: Vocabulary Module {mod['module']} ({mod['title'][:30]}...)...")
        pages_html.append(render_vocab_module_page(THEME, mod))
        cur_p += 1

    # Pages 65–70: Murphy-Style Mixed Additional Exercises (6 pages)
    for w in spag_l1_84p_data.MIXED_WORKOUTS:
        print(f"[{cur_p}/84] Rendering Page {cur_p}: Mixed Workout {w['workout_num']}...")
        pages_html.append(render_mixed_workout_page(THEME, w))
        cur_p += 1

    # Pages 71–76: Official Exam Mocks (6 pages: 3 mocks x 2 pages)
    for m in spag_l1_84p_data.EXAM_MOCKS:
        m_num = m["mock_num"]
        print(f"[{cur_p}/84] Rendering Page {cur_p}: Exam Mock {m_num} (Proofreading Scenario)...")
        pages_html.append(render_exam_mock_proof_page(THEME, m))
        cur_p += 1

        print(f"[{cur_p}/84] Rendering Page {cur_p}: Exam Mock {m_num} (Extended Writing Frame)...")
        pages_html.append(render_exam_mock_writing_page(THEME, m))
        cur_p += 1

    # Pages 77–82: Comprehensive Explanatory Answer Key (6 pages)
    for p_ans in range(77, 83):
        key_k = f"page_{p_ans}"
        key_data = spag_l1_84p_data.ANSWER_KEYS_6P[key_k]
        print(f"[{cur_p}/84] Rendering Page {cur_p}: Explanatory Answer Key (Part {p_ans - 76})...")
        pages_html.append(render_answer_key_page(THEME, cur_p, key_data))
        cur_p += 1

    # Page 83: Candidate Self-Audit Checklist & Progress Matrix (1 page)
    print(f"[{cur_p}/84] Rendering Page 83: Candidate Self-Audit & Progress Matrix...")
    pages_html.append(render_audit_page(THEME, spag_l1_84p_units.L1_UNITS_26))
    cur_p += 1

    # Page 84: High-Impact Back Cover (1 page)
    print(f"[{cur_p}/84] Rendering Page 84: High-Impact Back Cover...")
    pages_html.append(render_back_cover(THEME))

    total_rendered_pages = len(pages_html)
    print(f"\nTotal HTML Pages Assembled: {total_rendered_pages}")
    if total_rendered_pages != 84:
        raise ValueError(f"Page assembly error! Expected 84 pages, got {total_rendered_pages}")

    # Build full HTML document
    full_html = f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<title>{THEME['full_name']} &bull; SPaG Mastery Handbook (84-Page Comprehensive Edition)</title>
{SHARED_CSS}
</head>
<body>
{''.join(pages_html)}
</body>
</html>
"""

    temp_html_path = os.path.join(SCRATCH_DIR, f"temp_{THEME['file_stem']}.html")
    with open(temp_html_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Temporary HTML written to: {temp_html_path} ({os.path.getsize(temp_html_path) / 1024:.1f} KB)")

    # Output paths
    out_pdf_downloads = os.path.join(DOWNLOADS_DIR, f"{THEME['file_stem']}.pdf")
    out_pdf_documents = os.path.join(DOCUMENTS_DIR, f"{THEME['file_stem']}.pdf")

    print("\nExecuting Chromium Headless Compilation...")
    chrome_cmd = [
        CHROME_BIN,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--user-data-dir=/tmp/chr_spag_l1_84p",
        "--no-pdf-header-footer",
        f"--print-to-pdf={out_pdf_downloads}",
        temp_html_path
    ]
    sub_res = subprocess.run(chrome_cmd, capture_output=True, text=True)
    if sub_res.returncode != 0:
        print("Chromium error:", sub_res.stderr)
        raise RuntimeError("Chromium compilation failed.")

    # Replicate to Documents
    shutil.copy2(out_pdf_downloads, out_pdf_documents)

    # Clean up scratch HTML
    if os.path.exists(temp_html_path):
        os.remove(temp_html_path)

    # Verify page count with pdfinfo
    pdfinfo_res = subprocess.run(["pdfinfo", out_pdf_downloads], capture_output=True, text=True, check=True)
    actual_pages = None
    for line in pdfinfo_res.stdout.splitlines():
        if "Pages:" in line:
            actual_pages = int(line.split(":")[1].strip())
            break

    file_size_mb = os.path.getsize(out_pdf_downloads) / (1024 * 1024)
    elapsed = time.time() - start_time

    print("\n" + "=" * 80)
    print("VERIFICATION & PUBLICATION SUMMARY:")
    print("=" * 80)
    print(f"Target Output 1 : {out_pdf_downloads}")
    print(f"Target Output 2 : {out_pdf_documents}")
    print(f"File Size       : {file_size_mb:.2f} MB")
    print(f"Compilation Time: {elapsed:.2f} seconds")
    print(f"Actual Pages    : {actual_pages} (Target: Exactly 84 Pages)")

    if actual_pages != 84:
        raise ValueError(f"CRITICAL: PDF Page Count Mismatch! Expected 84 pages, got {actual_pages} pages!")

    print("STATUS          : SUCCESS - 100% PERFECT 84-PAGE COMPILATION CONFIRMED!")
    print("=" * 80)


if __name__ == "__main__":
    build_84p_book()
