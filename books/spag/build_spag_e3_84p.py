#!/usr/bin/env python3
"""
build_spag_e3_84p.py
=============================================================================
Master Functional Skills: Dyslexia-Friendly SPaG Book Generator
Compiles the comprehensive 82-Page Entry Level 3 SPaG Mastery publication:
  - Theme: Crimson Ruby (#881337, #be123c, #e11d48, #fbbf24)
  - 100% Dyslexia-Friendly: Warm Cream Canvas (#FDFBF7), Deep Slate Text (#1F2937),
    Lexend & Atkinson Hyperlegible Sans-Serif Fonts, Ragged-Right (NEVER Justified),
    Line-Height 1.48–1.52, Chunked Left-Bordered Color Cards.
  - Raymond Murphy 'Grammar in Use' Facing Two-Page Spread per Unit:
    * Left Page: Situational Anchor [A], Structural Formula & Syntax [B],
                 Compare & Contrast [C], Examiner Golden Rule & Memory Hook [D]
    * Right Page: Exercise 1 (Recognition/Discrimination), Exercise 2 (Cloze/Transformation),
                  Exercise 3 (Forensic Workplace Proofreading), Exercise 4 (Applied Writing Task)

Exact 82-Page Architecture:
  * Page 1: Full-Bleed Front Cover (Crimson Ruby)
  * Page 2: Inside Cover & Dyslexia Statement
  * Pages 3–6: Baseline Diagnostic Assessment & Visual Study Selector (4 pages)
  * Pages 7–54: 24 Two-Page Murphy 'Grammar in Use' Units (48 pages)
  * Pages 55–62: Entry 3 High-Frequency Word Banks & Phonics Spelling Rules (8 pages)
  * Pages 63–68: Mixed Proofreading & Sentence Building Workouts (6 pages)
  * Pages 69–74: Practical Workplace Writing Tasks with Lined Working Frames (6 pages)
  * Pages 75–80: Complete Explanatory Answer Key with Step-by-Step Guidance (6 pages)
  * Page 81: Candidate Self-Audit Checklist (1 page)
  * Page 82: High-Impact Back Cover (1 page)

Output Destinations:
  - /home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk/assets/downloads/MasterFunctionalSkills_SPaG_Entry_Level_3_Mastery.pdf
  - /home/subi/Documents/MasterFunctionalSkills_SPaG_Entry_Level_3_Mastery.pdf
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

import spag_data_e3_84p
import generate_e3_data
import spag_data_e3_extras
import spag_data_e3_answers

PROJECT_DIR = "/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk"
DOWNLOADS_DIR = os.path.join(PROJECT_DIR, "assets", "downloads")
DOCUMENTS_DIR = "/home/subi/Documents"
SCRATCH_DIR = os.path.join(PROJECT_DIR, "scratch", "spag_build")
CHROME_BIN = "/usr/lib/chromium/chromium"

os.makedirs(DOWNLOADS_DIR, exist_ok=True)
os.makedirs(DOCUMENTS_DIR, exist_ok=True)
os.makedirs(SCRATCH_DIR, exist_ok=True)

THEME = spag_data_e3_84p.THEME_E3

# =============================================================================
# CSS STYLESHEET
# =============================================================================

CSS_STYLES = f"""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Lexend:wght@400;500;600;700;800;900&family=Montserrat:wght@700;800;900&display=swap');

  @page {{
    size: A4 portrait;
    margin: 0;
  }}

  * {{
    box-sizing: border-box;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }}

  body {{
    margin: 0;
    padding: 0;
    font-family: 'Lexend', 'Atkinson Hyperlegible', sans-serif;
    color: #1F2937;
    background: #ffffff;
    font-size: 8pt;
    line-height: 1.48;
    letter-spacing: 0.02em;
    text-align: left;
  }}

  .page {{
    width: 210mm;
    height: 297mm;
    max-height: 297mm;
    min-height: 297mm;
    page-break-after: always;
    break-after: page;
    position: relative;
    overflow: hidden;
    padding: 10mm 14mm 12mm 14mm;
    background: #FDFBF7;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
  }}

  .cover-page {{
    padding: 0 !important;
    background: #3b0413;
    color: #ffffff;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}

  .unit-page-header {{
    border-bottom: 2px solid {THEME['primary']};
    padding-bottom: 3px;
    margin-bottom: 6px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }}
  .unit-page-header .brand-title {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 7.8pt;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    color: {THEME['primary']};
  }}
  .unit-page-header .strand-badge {{
    font-size: 7.2pt;
    font-weight: 700;
    color: #475569;
    background: #f1f5f9;
    padding: 1.5px 6px;
    border-radius: 4px;
    border: 1px solid #cbd5e1;
  }}

  .unit-main-heading {{
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 5px;
  }}
  .unit-num-pill {{
    background: {THEME['primary']};
    color: #ffffff;
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 7.5pt;
    padding: 2px 8px;
    border-radius: 10px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    white-space: nowrap;
  }}
  .unit-title-text {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 10.5pt;
    color: {THEME['primary']};
    line-height: 1.2;
    margin: 0;
  }}

  .page-footer {{
    position: absolute;
    bottom: 5.5mm;
    left: 14mm;
    right: 14mm;
    border-top: 1px solid #cbd5e1;
    padding-top: 3px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 7.2pt;
    color: #64748b;
  }}
  .page-num {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    color: {THEME['primary']};
    background: #f1f5f9;
    padding: 1px 6px;
    border-radius: 4px;
    border: 1px solid #e2e8f0;
  }}

  /* Dyslexia-Friendly Left-Bordered Cards */
  .card-anchor {{
    background: #F0F9FF;
    border: 1px solid #BAE6FD;
    border-left: 4px solid #0284C7;
    border-radius: 5px;
    padding: 5px 9px;
    margin-bottom: 5px;
  }}
  .card-anchor .card-title {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 7.6pt;
    color: #0369a1;
    text-transform: uppercase;
    letter-spacing: 0.4px;
    margin-bottom: 2px;
  }}

  .card-formula {{
    background: #ffffff;
    border: 1px solid #E2E8F0;
    border-left: 4px solid {THEME['secondary']};
    border-radius: 5px;
    padding: 5px 9px;
    margin-bottom: 5px;
  }}
  .card-formula .card-title {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 7.6pt;
    color: {THEME['secondary']};
    text-transform: uppercase;
    letter-spacing: 0.4px;
    margin-bottom: 3px;
  }}

  .formula-strip {{
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    gap: 5px;
    margin: 3px 0;
    background: #f8fafc;
    padding: 4px 7px;
    border-radius: 4px;
    border: 1px dashed #cbd5e1;
  }}
  .fpill {{
    font-size: 7.4pt;
    font-weight: 700;
    padding: 1px 6px;
    border-radius: 3px;
    display: inline-block;
  }}
  .fpill-subj {{ background: #dbeafe; color: #1e40af; border: 1px solid #bfdbfe; }}
  .fpill-verb {{ background: #dcfce7; color: #166534; border: 1px solid #bbf7d0; }}
  .fpill-punct {{ background: #fef08a; color: #854d0e; border: 1px solid #fde047; font-weight: 800; }}
  .fpill-conn {{ background: #f3e8ff; color: #6b21a8; border: 1px solid #e9d5ff; }}
  .fpill-clause {{ background: #ffedd5; color: #9a3412; border: 1px solid #fed7aa; }}

  /* Compare & Contrast Box */
  .card-compare {{
    background: #ffffff;
    border: 1px solid #E2E8F0;
    border-radius: 5px;
    overflow: hidden;
    margin-bottom: 5px;
  }}
  .compare-row-bad {{
    background: #FEF2F2;
    border-left: 4px solid #DC2626;
    padding: 4px 8px;
    border-bottom: 1px solid #FEE2E2;
  }}
  .compare-row-good {{
    background: #F0FDF4;
    border-left: 4px solid #16A34A;
    padding: 4px 8px;
    border-bottom: 1px solid #DCFCE7;
  }}
  .compare-row-why {{
    background: #FFFBEB;
    border-left: 4px solid #D97706;
    padding: 4px 8px;
    font-size: 7.5pt;
    color: #92400e;
  }}
  .compare-badge {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 6.8pt;
    padding: 1px 5px;
    border-radius: 3px;
    display: inline-block;
    margin-right: 4px;
    text-transform: uppercase;
  }}
  .badge-bad {{ background: #fee2e2; color: #991b1b; }}
  .badge-good {{ background: #dcfce7; color: #166534; }}
  .badge-why {{ background: #fef3c7; color: #92400e; }}

  /* Golden Rule Card */
  .card-golden {{
    background: #FEFCE8;
    border: 1px solid #FEF08A;
    border-left: 4px solid #D97706;
    border-radius: 5px;
    padding: 5px 9px;
    margin-top: auto;
  }}
  .card-golden .card-title {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 7.6pt;
    color: #b45309;
    text-transform: uppercase;
    letter-spacing: 0.4px;
    margin-bottom: 2px;
  }}

  /* Right-Hand Exercises Layout */
  .exercise-section {{
    margin-bottom: 6px;
  }}
  .ex-header {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #f8fafc;
    border-left: 3.5px solid {THEME['secondary']};
    padding: 2.5px 7px;
    border-radius: 3px;
    margin-bottom: 4px;
  }}
  .ex-title {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 7.6pt;
    color: {THEME['primary']};
    text-transform: uppercase;
    letter-spacing: 0.3px;
  }}
  .ex-marks {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    font-size: 7pt;
    color: #475569;
  }}

  .opt-box {{
    display: inline-flex;
    align-items: center;
    gap: 4px;
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    padding: 1.5px 6px;
    border-radius: 3px;
    font-size: 7.4pt;
  }}
  .opt-tick {{
    width: 10px;
    height: 10px;
    border: 1.2px solid #94a3b8;
    border-radius: 2px;
    display: inline-block;
  }}

  .workplace-doc {{
    background: #ffffff;
    border: 1.2px solid #cbd5e1;
    border-radius: 5px;
    overflow: hidden;
    margin-bottom: 4px;
  }}
  .doc-topbar {{
    background: #f1f5f9;
    border-bottom: 1px solid #cbd5e1;
    padding: 3px 7px;
    font-size: 7.1pt;
    color: #475569;
    display: flex;
    justify-content: space-between;
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
  }}
  .doc-meta {{
    padding: 3px 7px;
    background: #f8fafc;
    border-bottom: 1px dashed #e2e8f0;
    font-size: 7.2pt;
    line-height: 1.35;
  }}
  .doc-body {{
    padding: 5px 8px;
    font-size: 7.7pt;
    line-height: 1.4;
    background: #ffffff;
  }}

  .applied-task-box {{
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 5px;
    padding: 5px 8px;
  }}
  .task-prompt {{
    font-size: 7.6pt;
    font-weight: 600;
    color: #1e293b;
    margin-bottom: 3px;
  }}
  .task-lines {{
    background: repeating-linear-gradient(
      transparent,
      transparent 17px,
      #e2e8f0 18px,
      #e2e8f0 19px
    );
    height: 57px;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
  }}

  /* Diagnostic and Tables */
  table.mfs-table {{
    width: 100%;
    border-collapse: collapse;
    margin: 4px 0;
    font-size: 7.6pt;
  }}
  table.mfs-table th, table.mfs-table td {{
    padding: 4px 6px;
    border: 1px solid #cbd5e1;
    text-align: left;
    vertical-align: top;
  }}
  table.mfs-table th {{
    background: {THEME['primary']};
    color: #ffffff;
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    font-size: 7.2pt;
    text-transform: uppercase;
  }}
  table.mfs-table tr:nth-child(even) {{
    background: #f8fafc;
  }}

  .rag-pill {{
    display: inline-block;
    width: 12px;
    height: 12px;
    border-radius: 2px;
    border: 1px solid #cbd5e1;
    margin-right: 2px;
  }}
  .rag-red {{ background: #fecaca; }}
  .rag-amber {{ background: #fef08a; }}
  .rag-green {{ background: #bbf7d0; }}
</style>
"""


# =============================================================================
# HELPER RENDERING FUNCTIONS
# =============================================================================

def render_front_cover():
    """Generates Page 1: Full-Bleed Front Cover."""
    return f"""
<div class="page cover-page" style="background: linear-gradient(145deg, {THEME['cover_grad_start']} 0%, {THEME['cover_grad_mid']} 55%, {THEME['cover_grad_end']} 100%);">
  <div style="padding: 16mm 16mm 0 16mm;">
    <!-- Top Header -->
    <div style="display:flex; justify-content:space-between; align-items:center; border-bottom: 1.5px solid rgba(255,255,255,0.25); padding-bottom:10px;">
      <div>
        <div style="font-family:'Montserrat',sans-serif; font-size:12.5pt; font-weight:900; letter-spacing:2.5px; color:#ffffff;">MASTER FUNCTIONAL SKILLS</div>
        <div style="font-size:7.2pt; font-weight:700; letter-spacing:1.5px; color:#fbbf24; margin-top:2px;">OFFICIAL OFQUAL SPECIFICATION &bull; ENTRY LEVEL 3 WRITING</div>
      </div>
      <div style="background:{THEME['badge_bg']}; color:#ffffff; font-family:'Montserrat',sans-serif; font-weight:900; font-size:8.5pt; padding:5px 14px; border-radius:20px; letter-spacing:1px; border:1px solid rgba(255,255,255,0.3); box-shadow:0 2px 8px rgba(0,0,0,0.3);">
        ENTRY LEVEL 3
      </div>
    </div>

    <!-- Knockout Title Graphic -->
    <div style="margin-top:20mm;">
      <div style="font-family:'Montserrat',sans-serif; font-size:36pt; font-weight:900; color:rgba(255,255,255,0.08); letter-spacing:4px; line-height:0.9; text-transform:uppercase;">
        E3 SPAG
      </div>
      <div style="margin-top:-20px; font-family:'Montserrat',sans-serif; font-size:23pt; font-weight:900; color:#ffffff; line-height:1.15; letter-spacing:0.5px;">
        SPELLING, PUNCTUATION<br>&amp; GRAMMAR MASTERY
      </div>
      <div style="font-size:11.5pt; font-weight:600; color:#fde68a; margin-top:7px; letter-spacing:0.5px;">
        The Complete 82-Page Two-Page Spread Self-Study &amp; Revision Workbook
      </div>
      <div style="font-size:8.2pt; color:rgba(255,255,255,0.85); margin-top:6px; max-width:160mm; line-height:1.5;">
        Calibrated strictly to Ofqual standards using Raymond Murphy 'Grammar in Use' pedagogy. Specially engineered with dyslexia-friendly typography, anti-glare cream canvas, and chunked cognitive layouts.
      </div>
    </div>

    <!-- Key Feature Badges Grid -->
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:9px; margin-top:16mm;">
      <div style="background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.18); border-left:4px solid #38bdf8; border-radius:6px; padding:7px 11px;">
        <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:8pt; color:#ffffff;">24 MURPHY 2-PAGE SPREADS</div>
        <div style="font-size:7.2pt; color:rgba(255,255,255,0.8); margin-top:2px;">Visual theory on the left; progressive 4-tier practice drills on the right.</div>
      </div>
      <div style="background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.18); border-left:4px solid #34d399; border-radius:6px; padding:7px 11px;">
        <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:8pt; color:#ffffff;">DYSLEXIA-FRIENDLY CANVAS</div>
        <div style="font-size:7.2pt; color:rgba(255,255,255,0.8); margin-top:2px;">Soft #FDFBF7 cream background, Lexend font, and left-aligned text.</div>
      </div>
      <div style="background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.18); border-left:4px solid #f472b6; border-radius:6px; padding:7px 11px;">
        <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:8pt; color:#ffffff;">FORENSIC PROOFREADING</div>
        <div style="font-size:7.2pt; color:rgba(255,255,255,0.8); margin-top:2px;">Authentic workplace memos, rotas, and logs with exact error counts.</div>
      </div>
      <div style="background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.18); border-left:4px solid #fbbf24; border-radius:6px; padding:7px 11px;">
        <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:8pt; color:#ffffff;">EXPLANATORY ANSWER KEY</div>
        <div style="font-size:7.2pt; color:rgba(255,255,255,0.8); margin-top:2px;">Full step-by-step guidance for every exercise, diagnostic, and mock.</div>
      </div>
    </div>
  </div>

  <!-- Bottom Bar -->
  <div style="background:rgba(0,0,0,0.35); padding:10mm 16mm; border-top:1px solid rgba(255,255,255,0.15); display:flex; justify-content:space-between; align-items:center;">
    <div style="font-size:7.2pt; color:rgba(255,255,255,0.75);">
      <strong>masterfunctionalskills.co.uk</strong> &bull; Functional Skills English Entry Level 3 (FS-ENG-E3)<br>
      Published by Master Functional Skills, London UK &bull; Official Study &amp; Assessment Publication
    </div>
    <div style="background:#ffffff; color:{THEME['primary']}; font-family:'Montserrat',sans-serif; font-weight:900; font-size:7.8pt; padding:4px 10px; border-radius:4px;">
      COMPLETE 82-PAGE EDITION
    </div>
  </div>
</div>
"""


def render_inside_cover():
    """Generates Page 2: Inside Cover & Dyslexia Statement."""
    return f"""
<div class="page">
  <div class="unit-page-header">
    <div class="brand-title">MASTER FUNCTIONAL SKILLS &bull; PUBLISHING INFORMATION</div>
    <div class="strand-badge">{THEME['full_name']}</div>
  </div>

  <div style="margin-bottom:8px;">
    <h1 style="font-family:'Montserrat',sans-serif; font-size:13.5pt; font-weight:900; color:{THEME['primary']}; margin:0 0 2px 0;">
      Candidate &amp; Examination Centre Information
    </h1>
    <p style="font-size:7.8pt; color:#64748b; margin:0 0 6px 0;">Please complete the details below before commencing the baseline diagnostic assessment.</p>
  </div>

  <!-- Candidate Details Form Box -->
  <div style="background:#ffffff; border:1.5px solid #cbd5e1; border-radius:5px; padding:8px 12px; margin-bottom:10px;">
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
  <div class="card-anchor" style="border-left-color:{THEME['primary']}; margin-bottom:8px;">
    <div class="card-title" style="color:{THEME['primary']};">
      <span>DYSLEXIA-FRIENDLY ACCESSIBILITY &amp; TYPOGRAPHY STATEMENT</span>
    </div>
    <p style="margin:0 0 4px 0; font-size:7.9pt;">
      This publication has been developed strictly adhering to British Dyslexia Association and Ofqual accessibility standards. Reading efficiency and cognitive ease are maximized through the following evidence-based features:
    </p>
    <ul style="margin:0 0 0 16px; padding:0; font-size:7.8pt; line-height:1.42;">
      <li><strong>Soft Cream Canvas (#FDFBF7):</strong> Eliminates the harsh optical glare and visual stress associated with high-contrast pure white paper.</li>
      <li><strong>Lexend &amp; Atkinson Hyperlegible Typography:</strong> Engineered with distinct character shapes to prevent common mirror-confusion traps (b/d/p/q).</li>
      <li><strong>Ragged-Right Left Alignment:</strong> Text is never justified, completely eradicating irregular letter spacing and disorienting 'rivers of white space'.</li>
      <li><strong>Generous Leading (1.5) &amp; Letter-Spacing (0.02em):</strong> Enhances horizontal tracking and prevents unintended line skipping.</li>
      <li><strong>Chunked Left-Bordered Cards:</strong> Key grammatical categories are color-coded (Context: Blue; Formula: Ruby; Pitfall: Red; Golden Rule: Amber).</li>
    </ul>
  </div>

  <!-- The Murphy Method Box -->
  <div class="card-formula" style="margin-bottom:8px;">
    <div class="card-title">THE RAYMOND MURPHY 'GRAMMAR IN USE' 2-PAGE SPREAD METHOD</div>
    <p style="margin:0 0 4px 0; font-size:7.9pt;">
      Each of the 24 core units is structured as an interconnected facing 2-page spread:
    </p>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; font-size:7.6pt;">
      <div style="background:#f8fafc; padding:5px 8px; border-radius:4px; border:1px solid #e2e8f0;">
        <strong style="color:{THEME['primary']};">LEFT-HAND PAGE (Theory &amp; Context):</strong><br>
        [A] Situational Workplace Anchor<br>
        [B] Syntax Architecture &amp; Formulas<br>
        [C] Compare &amp; Contrast (Bad vs Good vs Why)<br>
        [D] Examiner Golden Rule &amp; Mnemonic
      </div>
      <div style="background:#f8fafc; padding:5px 8px; border-radius:4px; border:1px solid #e2e8f0;">
        <strong style="color:{THEME['primary']};">RIGHT-HAND PAGE (Progressive Drills):</strong><br>
        [Ex 1] Recognition / Binary Discrimination<br>
        [Ex 2] Controlled Cloze / Sentence Completion<br>
        [Ex 3] Forensic Workplace Proofreading<br>
        [Ex 4] Real-World Functional Writing Task
      </div>
    </div>
  </div>

  <!-- Publishing Notice -->
  <div style="margin-top:auto; font-size:7.2pt; color:#64748b; border-top:1px solid #e2e8f0; padding-top:5px;">
    <strong>Published by:</strong> Master Functional Skills (masterfunctionalskills.co.uk) &bull; London, United Kingdom.<br>
    &copy; 2026 Master Functional Skills. All rights reserved. Registered UK examination training provider and educational publisher.
  </div>

  <div class="page-footer">
    <div>{THEME['title']} &bull; Inside Cover &amp; Candidate Verification</div>
    <div class="page-num">Page 2</div>
  </div>
</div>
"""


def render_diagnostic_part(questions_subset, part_num, page_num, section_name):
    """Renders Pages 3, 4, 5: 8 Questions per page."""
    q_items_html = ""
    for q in questions_subset:
        opts_html = " &nbsp; ".join([f"<span class='opt-box'><span class='opt-tick'></span> {opt}</span>" for opt in q["options"]])
        q_items_html += f"""
        <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:5px; padding:5px 8px; margin-bottom:5px;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:2px;">
            <span style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.6pt; color:{THEME['primary']};">QUESTION {q['q_num']} &bull; {q['topic']}</span>
            <span style="font-size:7pt; color:#64748b; font-weight:600;">Maps to Unit {q['unit']}</span>
          </div>
          <div style="font-size:7.9pt; font-weight:600; color:#1e293b; margin-bottom:3px;">{q['question']}</div>
          <div>{opts_html}</div>
        </div>
        """

    return f"""
<div class="page">
  <div class="unit-page-header">
    <div class="brand-title">BASELINE DIAGNOSTIC &bull; PART {part_num} ({section_name})</div>
    <div class="strand-badge">{THEME['code']} Diagnostic Audit</div>
  </div>

  <div style="margin-bottom:5px;">
    <h1 style="font-family:'Montserrat',sans-serif; font-size:12.5pt; font-weight:900; color:{THEME['primary']}; margin:0 0 2px 0;">
      Entry Level 3 SPaG Baseline Audit: Part {part_num}
    </h1>
    <p style="font-size:7.6pt; color:#64748b; margin:0 0 5px 0;">Answer all 8 questions. Tick the one option (A, B, or C) that is 100% correct in standard English.</p>
  </div>

  <div style="display:flex; flex-direction:column; justify-content:flex-start;">
    {q_items_html}
  </div>

  <div class="page-footer">
    <div>{THEME['title']} &bull; Baseline Diagnostic Audit (Part {part_num})</div>
    <div class="page-num">Page {page_num}</div>
  </div>
</div>
"""


def render_diagnostic_selector():
    """Generates Page 6: Visual Study Selector & RAG Action Matrix."""
    bands_html = ""
    for b in spag_data_e3_84p.DIAGNOSTIC_SCORING_BANDS:
        bands_html += f"""
        <div style="background:{b['bg']}; border:1px solid {b['border']}; border-left:4px solid {b['color']}; border-radius:5px; padding:5px 9px; margin-bottom:5px;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <strong style="color:{b['color']}; font-size:8.2pt; font-family:'Montserrat',sans-serif;">{b['range']} &bull; {b['band']}</strong>
          </div>
          <div style="font-size:7.6pt; color:#334155; margin-top:2px;">{b['summary']}</div>
          <div style="font-size:7.4pt; color:#475569; margin-top:2px;"><strong>Action:</strong> {b['action']}</div>
        </div>
        """

    # Table mapping all 24 questions to units
    rows_html = ""
    for q in spag_data_e3_84p.DIAGNOSTIC_QUESTIONS:
        rows_html += f"""
        <tr>
          <td style="text-align:center; font-weight:700; width:8%;">Q{q['q_num']}</td>
          <td style="font-weight:600; width:44%;">{q['topic']}</td>
          <td style="color:{THEME['primary']}; font-weight:700; width:22%;">Unit {q['unit']} (pp. {6+q['unit']*2-1}–{6+q['unit']*2})</td>
          <td style="text-align:center; width:13%;"><span class="opt-tick"></span> Correct</td>
          <td style="text-align:center; width:13%;"><span class="rag-pill rag-red"></span><span class="rag-pill rag-amber"></span><span class="rag-pill rag-green"></span></td>
        </tr>
        """

    return f"""
<div class="page">
  <div class="unit-page-header">
    <div class="brand-title">DIAGNOSTIC ANALYSIS &bull; VISUAL STUDY SELECTOR</div>
    <div class="strand-badge">{THEME['code']} Personal Action Plan</div>
  </div>

  <div style="margin-bottom:5px;">
    <h1 style="font-family:'Montserrat',sans-serif; font-size:12pt; font-weight:900; color:{THEME['primary']}; margin:0 0 2px 0;">
      Diagnostic Scoring Matrix &amp; Unit Selector
    </h1>
    <p style="font-size:7.6pt; color:#64748b; margin:0 0 5px 0;">Calculate your total score out of 24 marks using the Explanatory Answer Key on Page 75.</p>
  </div>

  <!-- Scoring Bands -->
  {bands_html}

  <!-- Visual Mapping Table -->
  <div style="margin-top:4px;">
    <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.8pt; color:{THEME['primary']}; margin-bottom:3px;">
      QUESTION-TO-UNIT REVISION PRIORITY MATRIX (UNITS 1 TO 24)
    </div>
    <div style="max-height:150mm; overflow:hidden;">
      <table class="mfs-table" style="font-size:6.9pt;">
        <thead>
          <tr>
            <th>Question</th>
            <th>SPaG Skill Tested</th>
            <th>Study Unit &amp; Pages</th>
            <th>My Result</th>
            <th>Confidence</th>
          </tr>
        </thead>
        <tbody>
          {rows_html}
        </tbody>
      </table>
    </div>
  </div>

  <div class="page-footer">
    <div>{THEME['title']} &bull; Visual Study Selector &amp; Diagnostic Matrix</div>
    <div class="page-num">Page 6</div>
  </div>
</div>
"""


def render_unit_left_page(unit_data, page_num):
    """Generates Unit Left Page (Odd: 7, 9, 11...): Theory & Syntax."""
    u_num = unit_data["unit"]
    u_title = unit_data["title"]
    fmt = unit_data.get("format", "Workplace Document")

    return f"""
<div class="page">
  <div class="unit-page-header">
    <div class="brand-title">UNIT {u_num} &bull; THEORY &amp; VISUAL ARCHITECTURE</div>
    <div class="strand-badge">{THEME['code']} &bull; {fmt}</div>
  </div>

  <div class="unit-main-heading">
    <span class="unit-num-pill">UNIT {u_num}</span>
    <h2 class="unit-title-text">{u_title}</h2>
  </div>

  <div style="display:flex; flex-direction:column; height:248mm; justify-content:space-between;">
    <!-- [A] Situational Anchor -->
    <div class="card-anchor">
      <div class="card-title">[A] Situational Workplace Anchor: {unit_data['anchor_title']}</div>
      <p style="margin:0; font-size:7.8pt;">{unit_data['anchor_text']}</p>
    </div>

    <!-- [B] Structural Syntax Formula -->
    <div class="card-formula">
      <div class="card-title">[B] {unit_data['formula_title']}</div>
      <div style="font-size:7.8pt; line-height:1.42;">{unit_data['formula_html']}</div>
    </div>

    <!-- [C] Compare & Contrast -->
    <div class="card-compare">
      <div class="compare-row-bad">
        <span class="compare-badge badge-bad">❌ Pitfall</span>
        <span style="font-size:7.8pt; color:#991b1b;">{unit_data['pitfall_text']}</span>
      </div>
      <div class="compare-row-good">
        <span class="compare-badge badge-good">✔️ Model</span>
        <span style="font-size:7.8pt; color:#166534; font-weight:600;">{unit_data['model_text']}</span>
      </div>
      <div class="compare-row-why">
        <span class="compare-badge badge-why">💡 Examiner Why</span>
        <span>{unit_data['why_text']}</span>
      </div>
    </div>

    <!-- [D] Examiner Golden Rule -->
    <div class="card-golden">
      <div class="card-title">[D] Examiner Golden Rule &amp; Memory Hook</div>
      <p style="margin:0; font-size:7.7pt;">{unit_data['golden_rule']}</p>
    </div>
  </div>

  <div class="page-footer">
    <div>{THEME['title']} &bull; Unit {u_num}: {u_title}</div>
    <div class="page-num">Page {page_num}</div>
  </div>
</div>
"""


def render_unit_right_page(unit_data, page_num):
    """Generates Unit Right Page (Even: 8, 10, 12...): 4-Tier Drills."""
    u_num = unit_data["unit"]
    fmt = unit_data.get("format", "Workplace Document")

    # Ex 1: Recognition / Discrimination
    ex1_html = ""
    for idx, item in enumerate(unit_data.get("exercise_a", [])[:4], 1):
        q_text, opts = item[0], item[1]
        opts_rendered = " &nbsp; ".join([f"<span class='opt-box'><span class='opt-tick'></span> {opt}</span>" for opt in opts])
        ex1_html += f"""
        <div style="margin-bottom:3px; font-size:7.6pt;">
          <div><strong>{idx}.</strong> {q_text}</div>
          <div style="margin-top:1.5px;">{opts_rendered}</div>
        </div>
        """

    # Ex 2: Controlled Sentence Completion / Transformation
    ex2_html = ""
    for idx, item in enumerate(unit_data.get("exercise_b", [])[:3], 1):
        task_label, prompt = item[0], item[1]
        ex2_html += f"""
        <div style="margin-bottom:2.5px; font-size:7.5pt;">
          <strong>{idx}.</strong> <span style="color:#475569;">({task_label}):</span> <em>"{prompt}"</em>
          <div style="border-bottom:1px dashed #cbd5e1; height:14px; margin-top:1px;"></div>
        </div>
        """

    # Ex 3: Forensic Workplace Proofreading
    doc_title = unit_data.get("proofreading_title", f"Applied Proofreading: {fmt}")
    doc_scenario = unit_data.get("proofreading_scenario", "Locate and correct all deliberate SPaG errors in the document below.")
    doc_text = unit_data.get("proofreading_text", "<p>Document text for proofreading.</p>")
    err_count = len(unit_data.get("proofreading_errors", [1,2,3,4,5]))

    # Ex 4: Applied Functional Writing Task
    writing_prompt = unit_data.get("writing_prompt", "Write two complete, correctly punctuated sentences suitable for this vocational workplace format.")

    return f"""
<div class="page">
  <div class="unit-page-header">
    <div class="brand-title">UNIT {u_num} &bull; GRADED PRACTICE DRILLS</div>
    <div class="strand-badge">{THEME['code']} Applied Drills</div>
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
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:4px; padding:4px 7px;">
      {ex1_html}
    </div>
  </div>

  <!-- EXERCISE 2: GUIDED COMPLETION -->
  <div class="exercise-section">
    <div class="ex-header">
      <span class="ex-title">[EXERCISE 2] Controlled Sentence Completion</span>
      <span class="ex-marks">3 Marks</span>
    </div>
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:4px; padding:4px 7px;">
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
    <div>{THEME['title']} &bull; Unit {u_num}: Practice Drills</div>
    <div class="page-num">Page {page_num}</div>
  </div>
</div>
"""


def render_phonics_page(data, page_num):
    """Renders Pages 55 to 58: Phonics Spelling Rules."""
    cloze_html = ""
    for prompt, ans in data.get("cloze_drills", []):
        cloze_html += f"""
        <div style="margin-bottom:3px; font-size:7.5pt;">
          &bull; {prompt} <span style="color:#64748b; font-size:7pt;">[Answer: {ans}]</span>
        </div>
        """

    content_html = ""
    if "examples_table" in data:
        rows = "".join([f"<tr><td><strong>{r[0]}</strong></td><td>{r[1]}</td><td>{r[2]}</td><td><em>{r[3]}</em></td></tr>" for r in data["examples_table"]])
        content_html = f"""
        <table class="mfs-table" style="font-size:7.3pt; margin-bottom:6px;">
          <thead><tr><th>Base Verb</th><th>Past (-ed)</th><th>Continuous (-ing)</th><th>Workplace Sentence Model</th></tr></thead>
          <tbody>{rows}</tbody>
        </table>
        <div class="card-anchor" style="font-size:7.6pt; margin-bottom:6px;">
          {data.get('contrast_note', '')}
        </div>
        """
    elif "drop_table" in data:
        drop_rows = "".join([f"<tr><td><strong>{r[0]}</strong></td><td>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td></tr>" for r in data["drop_table"]])
        keep_rows = "".join([f"<tr><td><strong>{r[0]}</strong></td><td>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td></tr>" for r in data["keep_table"]])
        content_html = f"""
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; margin-bottom:6px;">
          <div>
            <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.5pt; color:#b91c1c; margin-bottom:2px;">DROP 'E' BEFORE VOWEL SUFFIX</div>
            <table class="mfs-table" style="font-size:7.1pt;">
              <thead><tr><th>Base</th><th>Suffix</th><th>Word</th><th>Rule</th></tr></thead>
              <tbody>{drop_rows}</tbody>
            </table>
          </div>
          <div>
            <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.5pt; color:#15803d; margin-bottom:2px;">KEEP 'E' BEFORE CONSONANT SUFFIX</div>
            <table class="mfs-table" style="font-size:7.1pt;">
              <thead><tr><th>Base</th><th>Suffix</th><th>Word</th><th>Rule</th></tr></thead>
              <tbody>{keep_rows}</tbody>
            </table>
          </div>
        </div>
        """
    elif "ie_words" in data:
        ie_rows = "".join([f"<tr><td><strong>{r[0]}</strong></td><td><em>{r[1]}</em></td></tr>" for r in data["ie_words"]])
        cei_rows = "".join([f"<tr><td><strong>{r[0]}</strong></td><td><em>{r[1]}</em></td></tr>" for r in data["cei_words"]])
        content_html = f"""
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; margin-bottom:6px;">
          <div>
            <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.5pt; color:#1e40af; margin-bottom:2px;">'IE' FOR /EE/ SOUND (NO C)</div>
            <table class="mfs-table" style="font-size:7.1pt;">
              <thead><tr><th>Word</th><th>Example Sentence</th></tr></thead>
              <tbody>{ie_rows}</tbody>
            </table>
          </div>
          <div>
            <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.5pt; color:#b91c1c; margin-bottom:2px;">'EI' AFTER 'C' FOR /EE/ SOUND</div>
            <table class="mfs-table" style="font-size:7.1pt;">
              <thead><tr><th>Word</th><th>Example Sentence</th></tr></thead>
              <tbody>{cei_rows}</tbody>
            </table>
          </div>
        </div>
        <div class="card-golden" style="font-size:7.6pt; margin-bottom:6px;">
          {data.get('special_note', '')}
        </div>
        """
    elif "consonant_y_table" in data:
        cy_rows = "".join([f"<tr><td><strong>{r[0]}</strong></td><td>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td></tr>" for r in data["consonant_y_table"]])
        vy_rows = "".join([f"<tr><td><strong>{r[0]}</strong></td><td>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td></tr>" for r in data["vowel_y_table"]])
        content_html = f"""
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; margin-bottom:6px;">
          <div>
            <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.5pt; color:#b91c1c; margin-bottom:2px;">CONSONANT + Y &rarr; CHANGE TO 'I'</div>
            <table class="mfs-table" style="font-size:7.1pt;">
              <thead><tr><th>Base</th><th>Plural</th><th>Past</th><th>Rule</th></tr></thead>
              <tbody>{cy_rows}</tbody>
            </table>
          </div>
          <div>
            <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.5pt; color:#15803d; margin-bottom:2px;">VOWEL + Y &rarr; KEEP THE 'Y'</div>
            <table class="mfs-table" style="font-size:7.1pt;">
              <thead><tr><th>Base</th><th>Plural</th><th>Past</th><th>Rule</th></tr></thead>
              <tbody>{vy_rows}</tbody>
            </table>
          </div>
        </div>
        <div class="card-anchor" style="font-size:7.6pt; margin-bottom:6px;">
          {data.get('ing_exception', '')}
        </div>
        """

    return f"""
<div class="page">
  <div class="unit-page-header">
    <div class="brand-title">PHONICS &amp; ORTHOGRAPHY &bull; RULE {page_num-54}</div>
    <div class="strand-badge">{THEME['code']} Core Spelling Architecture</div>
  </div>

  <div style="margin-bottom:6px;">
    <h1 style="font-family:'Montserrat',sans-serif; font-size:12.5pt; font-weight:900; color:{THEME['primary']}; margin:0 0 2px 0;">
      {data['title']}
    </h1>
    <p style="font-size:7.7pt; color:#64748b; margin:0 0 4px 0;">{data['subtitle']}</p>
  </div>

  <div class="card-formula" style="margin-bottom:6px;">
    <div class="card-title">RULE PRINCIPLE &amp; PHONICS EXPLANATION</div>
    <div style="font-size:7.8pt;">{data['rule_summary']}</div>
  </div>

  {content_html}

  <!-- Practice Cloze Section -->
  <div class="exercise-section" style="margin-top:auto;">
    <div class="ex-header">
      <span class="ex-title">WORKPLACE PRACTICE CLOZE DRILLS</span>
      <span class="ex-marks">5 Marks</span>
    </div>
    <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:5px 8px;">
      {cloze_html}
    </div>
  </div>

  <div class="page-footer">
    <div>{THEME['title']} &bull; Phonics Spelling Rules (Rule {page_num-54})</div>
    <div class="page-num">Page {page_num}</div>
  </div>
</div>
"""


def render_word_bank_page(data, page_num):
    """Renders Pages 59 to 62: Master High-Frequency Word Banks."""
    tables_html = ""
    if "days" in data:
        days_rows = "".join([f"<tr><td><strong>{r[0]}</strong></td><td>{r[1]}</td><td>{r[2]}</td></tr>" for r in data["days"]])
        months_rows = "".join([f"<tr><td><strong>{r[0]}</strong></td><td>{r[1]}</td><td>{r[2]}</td></tr>" for r in data["months"]])
        time_rows = "".join([f"<tr><td><strong>{r[0]}</strong></td><td>{r[1]}</td></tr>" for r in data["time_terms"][:8]])
        tables_html = f"""
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; margin-bottom:6px;">
          <div>
            <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.5pt; color:{THEME['primary']}; margin-bottom:2px;">DAYS OF THE WEEK</div>
            <table class="mfs-table" style="font-size:7.1pt;">
              <thead><tr><th>Day</th><th>Phonics Chunk</th><th>Memory Guide</th></tr></thead>
              <tbody>{days_rows}</tbody>
            </table>
          </div>
          <div>
            <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.5pt; color:{THEME['primary']}; margin-bottom:2px;">MONTHS OF THE YEAR</div>
            <table class="mfs-table" style="font-size:7.1pt;">
              <thead><tr><th>Month</th><th>Phonics Chunk</th><th>Notes</th></tr></thead>
              <tbody>{months_rows}</tbody>
            </table>
          </div>
        </div>
        <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.5pt; color:{THEME['primary']}; margin-bottom:2px;">ESSENTIAL TIME &amp; SCHEDULING TERMS</div>
        <table class="mfs-table" style="font-size:7.1pt; margin-bottom:6px;">
          <thead><tr><th>Word</th><th>Meaning &amp; Functional Usage</th></tr></thead>
          <tbody>{time_rows}</tbody>
        </table>
        """
    elif "roles" in data:
        roles_rows = "".join([f"<tr><td><strong>{r[0]}</strong></td><td>{r[1]}</td></tr>" for r in data["roles"]])
        dept_rows = "".join([f"<tr><td><strong>{r[0]}</strong></td><td>{r[1]}</td></tr>" for r in data["departments"]])
        ops_rows = "".join([f"<tr><td><strong>{r[0]}</strong></td><td>{r[1]}</td></tr>" for r in data["operations"]])
        tables_html = f"""
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; margin-bottom:6px;">
          <div>
            <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.5pt; color:{THEME['primary']}; margin-bottom:2px;">WORKPLACE JOB ROLES</div>
            <table class="mfs-table" style="font-size:7.1pt;">
              <thead><tr><th>Job Title</th><th>Workplace Description</th></tr></thead>
              <tbody>{roles_rows}</tbody>
            </table>
          </div>
          <div>
            <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.5pt; color:{THEME['primary']}; margin-bottom:2px;">DEPARTMENTS &amp; FACILITIES</div>
            <table class="mfs-table" style="font-size:7.1pt;">
              <thead><tr><th>Department</th><th>Function</th></tr></thead>
              <tbody>{dept_rows}</tbody>
            </table>
          </div>
        </div>
        <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.5pt; color:{THEME['primary']}; margin-bottom:2px;">PROFESSIONAL OPERATIONS &amp; CONTRACTS</div>
        <table class="mfs-table" style="font-size:7.1pt; margin-bottom:6px;">
          <thead><tr><th>Term</th><th>Meaning &amp; Administrative Usage</th></tr></thead>
          <tbody>{ops_rows}</tbody>
        </table>
        """
    elif "hazards" in data:
        haz_rows = "".join([f"<tr><td><strong>{r[0]}</strong></td><td>{r[1]}</td></tr>" for r in data["hazards"]])
        ppe_rows = "".join([f"<tr><td><strong>{r[0]}</strong></td><td>{r[1]}</td></tr>" for r in data["ppe"]])
        emg_rows = "".join([f"<tr><td><strong>{r[0]}</strong></td><td>{r[1]}</td></tr>" for r in data["emergency_terms"]])
        tables_html = f"""
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; margin-bottom:6px;">
          <div>
            <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.5pt; color:{THEME['primary']}; margin-bottom:2px;">HAZARDS &amp; WARNING SIGNS</div>
            <table class="mfs-table" style="font-size:7.1pt;">
              <thead><tr><th>Sign / Term</th><th>Definition</th></tr></thead>
              <tbody>{haz_rows}</tbody>
            </table>
          </div>
          <div>
            <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.5pt; color:{THEME['primary']}; margin-bottom:2px;">PROTECTIVE EQUIPMENT (PPE)</div>
            <table class="mfs-table" style="font-size:7.1pt;">
              <thead><tr><th>Equipment</th><th>Safety Purpose</th></tr></thead>
              <tbody>{ppe_rows}</tbody>
            </table>
          </div>
        </div>
        <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.5pt; color:{THEME['primary']}; margin-bottom:2px;">EMERGENCY PROCEDURES &amp; FIRST AID</div>
        <table class="mfs-table" style="font-size:7.1pt; margin-bottom:6px;">
          <thead><tr><th>Procedure</th><th>Workplace Protocol</th></tr></thead>
          <tbody>{emg_rows}</tbody>
        </table>
        """
    elif "personal_fields" in data:
        p_rows = "".join([f"<tr><td><strong>{r[0]}</strong></td><td>{r[1]}</td></tr>" for r in data["personal_fields"]])
        a_rows = "".join([f"<tr><td><strong>{r[0]}</strong></td><td>{r[1]}</td></tr>" for r in data["administrative_terms"]])
        act_rows = "".join([f"<tr><td><strong>{r[0]}</strong></td><td>{r[1]}</td></tr>" for r in data["action_verbs"]])
        tables_html = f"""
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; margin-bottom:6px;">
          <div>
            <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.5pt; color:{THEME['primary']}; margin-bottom:2px;">PERSONAL IDENTITY FIELDS</div>
            <table class="mfs-table" style="font-size:7.1pt;">
              <thead><tr><th>Form Field</th><th>Instructions</th></tr></thead>
              <tbody>{p_rows}</tbody>
            </table>
          </div>
          <div>
            <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.5pt; color:{THEME['primary']}; margin-bottom:2px;">ADMINISTRATIVE PROCEDURES</div>
            <table class="mfs-table" style="font-size:7.1pt;">
              <thead><tr><th>Document Term</th><th>Explanation</th></tr></thead>
              <tbody>{a_rows}</tbody>
            </table>
          </div>
        </div>
        <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.5pt; color:{THEME['primary']}; margin-bottom:2px;">APPLICATION &amp; FORM ACTION VERBS</div>
        <table class="mfs-table" style="font-size:7.1pt; margin-bottom:6px;">
          <thead><tr><th>Action Verb</th><th>Requirement on Official Forms</th></tr></thead>
          <tbody>{act_rows}</tbody>
        </table>
        """

    return f"""
<div class="page">
  <div class="unit-page-header">
    <div class="brand-title">HIGH-FREQUENCY VOCABULARY &bull; BANK {page_num-58}</div>
    <div class="strand-badge">{THEME['code']} Master Word Banks</div>
  </div>

  <div style="margin-bottom:6px;">
    <h1 style="font-family:'Montserrat',sans-serif; font-size:12.5pt; font-weight:900; color:{THEME['primary']}; margin:0 0 2px 0;">
      {data['title']}
    </h1>
    <p style="font-size:7.7pt; color:#64748b; margin:0 0 4px 0;">{data['subtitle']}</p>
  </div>

  {tables_html}

  <div class="card-golden" style="margin-top:auto; font-size:7.6pt;">
    <div class="card-title">MASTER PROOFREADING CHALLENGE</div>
    <div>{data.get('challenge', '')}</div>
  </div>

  <div class="page-footer">
    <div>{THEME['title']} &bull; High-Frequency Word Banks (Bank {page_num-58})</div>
    <div class="page-num">Page {page_num}</div>
  </div>
</div>
"""


def render_mixed_workout_page(data, page_num):
    """Renders Pages 63 to 68: Mixed Proofreading & Sentence Building Workouts."""
    drills_html = ""
    for idx, (p, sol) in enumerate(data.get("expansion_drills", []), 1):
        drills_html += f"""
        <div style="margin-bottom:4px; font-size:7.6pt;">
          <strong>{idx}.</strong> <em>"{p}"</em>
          <div style="border-bottom:1px dashed #cbd5e1; height:15px; margin-top:2px;"></div>
        </div>
        """

    err_count = len(data.get("errors", []))

    return f"""
<div class="page">
  <div class="unit-page-header">
    <div class="brand-title">MIXED WORKOUT &bull; WORKOUT {page_num-62}</div>
    <div class="strand-badge">{THEME['code']} Mixed Applied SPaG</div>
  </div>

  <div style="margin-bottom:5px;">
    <h1 style="font-family:'Montserrat',sans-serif; font-size:12pt; font-weight:900; color:{THEME['primary']}; margin:0 0 2px 0;">
      {data['title']}
    </h1>
    <p style="font-size:7.6pt; color:#64748b; margin:0 0 5px 0;"><strong>Vocational Scenario:</strong> {data['scenario']}</p>
  </div>

  <!-- Part 1: Forensic Proofreading -->
  <div class="exercise-section">
    <div class="ex-header">
      <span class="ex-title">[PART 1] Forensic Workplace Proofreading</span>
      <span class="ex-marks">{err_count} Marks (Find {err_count} deliberate errors)</span>
    </div>
    <div class="workplace-doc">
      <div class="doc-topbar">
        <span>AUTHENTIC WORKPLACE COMMUNICATION</span>
        <span>EXACT ERRORS: {err_count}</span>
      </div>
      <div class="doc-body">
        {data['text']}
      </div>
    </div>
  </div>

  <!-- Part 2: Sentence Expansion & Combining -->
  <div class="exercise-section" style="margin-top:auto;">
    <div class="ex-header">
      <span class="ex-title">[PART 2] Sentence Combining &amp; Crafting Drills</span>
      <span class="ex-marks">4 Marks</span>
    </div>
    <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:5px; padding:6px 9px;">
      <div style="font-size:7.6pt; font-weight:600; color:#1e293b; margin-bottom:4px;">{data['expansion_prompt']}</div>
      {drills_html}
    </div>
  </div>

  <div class="page-footer">
    <div>{THEME['title']} &bull; Mixed SPaG Workout {page_num-62}</div>
    <div class="page-num">Page {page_num}</div>
  </div>
</div>
"""


def render_writing_task_page(data, page_num):
    """Renders Pages 69 to 74: Practical Workplace Writing Tasks with Lined Frames."""
    criteria_html = "".join([f"<li>{c}</li>" for c in data["criteria"]])

    return f"""
<div class="page">
  <div class="unit-page-header">
    <div class="brand-title">PRACTICAL WRITING &bull; TASK {data['task_num']}</div>
    <div class="strand-badge">{THEME['code']} &bull; {data['format']}</div>
  </div>

  <div style="margin-bottom:6px;">
    <h1 style="font-family:'Montserrat',sans-serif; font-size:12pt; font-weight:900; color:{THEME['primary']}; margin:0 0 2px 0;">
      {data['title']}
    </h1>
    <div class="card-anchor" style="margin-top:4px;">
      <div class="card-title">VOCATIONAL WRITING SCENARIO</div>
      <div style="font-size:7.8pt;">{data['scenario']}</div>
    </div>
  </div>

  <!-- Success Criteria Checklist -->
  <div class="card-formula" style="margin-bottom:8px;">
    <div class="card-title">EXAMINER SUCCESS CRITERIA CHECKLIST (MUST INCLUDE ALL 4)</div>
    <ul style="margin:2px 0 0 16px; padding:0; font-size:7.7pt; line-height:1.4;">
      {criteria_html}
    </ul>
  </div>

  <!-- Planning & Structure Box -->
  <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:4px; padding:5px 8px; margin-bottom:8px; font-size:7.4pt; color:#475569;">
    <strong>Guided Structure:</strong> [1] Greeting &bull; [2] Reason / Core Message (with 'because' or 'so') &bull; [3] Key Details &amp; Equipment / Shift dates &bull; [4] Polite Sign-off.
  </div>

  <!-- Lined Working Frame -->
  <div style="margin-top:auto;">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:3px;">
      <span style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.6pt; color:{THEME['primary']};">CANDIDATE RESPONSE WORKING FRAME</span>
      <span style="font-size:7pt; color:#64748b;">Write in full sentences using standard English</span>
    </div>
    <div style="background: repeating-linear-gradient(transparent, transparent 20px, #cbd5e1 21px, #cbd5e1 22px); height: 115mm; border: 1.5px solid #cbd5e1; border-radius: 5px; padding: 6px 10px;">
    </div>
  </div>

  <div class="page-footer">
    <div>{THEME['title']} &bull; Practical Workplace Writing Task {data['task_num']}</div>
    <div class="page-num">Page {page_num}</div>
  </div>
</div>
"""


def render_answer_key_page_75():
    """Generates Page 75: Diagnostic Q1-24 & Units 1 to 4."""
    data = spag_data_e3_answers.ANSWER_KEY_DATA["page_75"]

    # Diagnostic Q1-24 items
    diag_rows = ""
    for q, ans, reason in data["diagnostic_answers"]:
        diag_rows += f"""
        <div style="font-size:7.1pt; margin-bottom:2px; line-height:1.3;">
          <strong style="color:{THEME['primary']};">{q} [{ans}]:</strong> {reason}
        </div>
        """

    # Units 1 to 4 answers
    units_html = ""
    for u_num, u_data in data["units"].items():
        ex1_str = " &bull; ".join(u_data["ex1"])
        ex2_str = "<br>".join([f"&bull; {x}" for x in u_data["ex2"]])
        prf_str = "<br>".join([f"&bull; {x}" for x in u_data["proofreading"]])
        units_html += f"""
        <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:4px 7px; margin-bottom:4px; font-size:7.2pt;">
          <strong style="color:{THEME['primary']};">UNIT {u_num}:</strong>
          <div><strong>Ex 1:</strong> {ex1_str}</div>
          <div style="margin-top:1px;"><strong>Ex 2:</strong> {ex2_str}</div>
          <div style="margin-top:1px;"><strong>Ex 3 Proofreading:</strong> {prf_str}</div>
          <div style="margin-top:1px; color:#166534;"><strong>Ex 4 Model:</strong> <em>"{u_data['model_writing']}"</em></div>
        </div>
        """

    return f"""
<div class="page">
  <div class="unit-page-header">
    <div class="brand-title">EXPLANATORY ANSWER KEY &bull; PART 1</div>
    <div class="strand-badge">{THEME['code']} Answers &amp; Guidance</div>
  </div>

  <div style="margin-bottom:4px;">
    <h1 style="font-family:'Montserrat',sans-serif; font-size:11.5pt; font-weight:900; color:{THEME['primary']}; margin:0 0 2px 0;">
      Baseline Diagnostic (Q1–24) &amp; Units 1–4 Answers
    </h1>
    <p style="font-size:7.4pt; color:#64748b; margin:0 0 4px 0;">Compare your responses with the examiner explanations below to understand the grammatical rules.</p>
  </div>

  <!-- Diagnostic Q1-24 Container -->
  <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:5px; padding:5px 8px; margin-bottom:5px;">
    <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.5pt; color:{THEME['primary']}; margin-bottom:3px;">
      BASELINE DIAGNOSTIC ASSESSMENT &bull; ALL 24 QUESTIONS
    </div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:6px;">
      <div>{diag_rows[:len(diag_rows)//2]}</div>
      <div>{diag_rows[len(diag_rows)//2:]}</div>
    </div>
  </div>

  <!-- Units 1 to 4 -->
  <div style="display:flex; flex-direction:column; justify-content:flex-start;">
    {units_html}
  </div>

  <div class="page-footer">
    <div>{THEME['title']} &bull; Explanatory Answer Key (Part 1)</div>
    <div class="page-num">Page 75</div>
  </div>
</div>
"""


def render_answer_key_page_units(part_key, page_num):
    """Generates Pages 76, 77, 78, 79: Units Answers."""
    data = spag_data_e3_answers.ANSWER_KEY_DATA[part_key]
    part_num = page_num - 74

    units_html = ""
    for u_num, u_data in data["units"].items():
        ex1_str = " &bull; ".join(u_data["ex1"])
        ex2_str = "<br>".join([f"&bull; {x}" for x in u_data["ex2"]])
        prf_str = "<br>".join([f"&bull; {x}" for x in u_data["proofreading"]])
        units_html += f"""
        <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:4px 7px; margin-bottom:4px; font-size:7.2pt;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1px;">
            <strong style="color:{THEME['primary']}; font-size:7.6pt;">UNIT {u_num} COMPLETE SOLUTIONS</strong>
            <span style="font-size:6.8pt; color:#64748b;">Theory pp. {6+u_num*2-1} &bull; Drills pp. {6+u_num*2}</span>
          </div>
          <div><strong>Ex 1 (Recognition):</strong> {ex1_str}</div>
          <div style="margin-top:1px;"><strong>Ex 2 (Completion):</strong> {ex2_str}</div>
          <div style="margin-top:1px;"><strong>Ex 3 (Forensic Proofreading):</strong> {prf_str}</div>
          <div style="margin-top:1px; color:#166534;"><strong>Ex 4 (Applied Writing Model):</strong> <em>"{u_data['model_writing']}"</em></div>
        </div>
        """

    return f"""
<div class="page">
  <div class="unit-page-header">
    <div class="brand-title">EXPLANATORY ANSWER KEY &bull; PART {part_num}</div>
    <div class="strand-badge">{THEME['code']} Answers &amp; Guidance</div>
  </div>

  <div style="margin-bottom:5px;">
    <h1 style="font-family:'Montserrat',sans-serif; font-size:12pt; font-weight:900; color:{THEME['primary']}; margin:0 0 2px 0;">
      {data['title']}
    </h1>
    <p style="font-size:7.5pt; color:#64748b; margin:0 0 4px 0;">Full step-by-step model corrections for all recognition, cloze, proofreading, and functional writing tasks.</p>
  </div>

  <div style="display:flex; flex-direction:column; justify-content:space-between; height:245mm;">
    {units_html}
  </div>

  <div class="page-footer">
    <div>{THEME['title']} &bull; Explanatory Answer Key (Part {part_num})</div>
    <div class="page-num">Page {page_num}</div>
  </div>
</div>
"""


def render_answer_key_page_80():
    """Generates Page 80: Mixed Workouts & Writing Exemplars."""
    data = spag_data_e3_answers.ANSWER_KEY_DATA["page_80"]

    workouts_html = ""
    for w_num, w_data in data["workouts"].items():
        err_str = " &bull; ".join(w_data["errors"])
        exp_str = " &bull; ".join(w_data["expansion"])
        workouts_html += f"""
        <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:3px 6px; margin-bottom:3px; font-size:7pt;">
          <strong style="color:{THEME['primary']};">WORKOUT {w_num}:</strong><br>
          <strong>Errors:</strong> {err_str}<br>
          <strong>Combining:</strong> {exp_str}
        </div>
        """

    exemplars_html = ""
    for t_num, ex_text in data["writing_exemplars"].items():
        ex_preview = ex_text.replace('\n', '<br>')
        exemplars_html += f"""
        <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:4px; padding:3px 6px; margin-bottom:3px; font-size:6.9pt; line-height:1.35;">
          <strong style="color:#166534;">TASK {t_num} MODEL WRITING EXEMPLAR:</strong><br>
          <em>{ex_preview}</em>
        </div>
        """

    return f"""
<div class="page">
  <div class="unit-page-header">
    <div class="brand-title">EXPLANATORY ANSWER KEY &bull; PART 6</div>
    <div class="strand-badge">{THEME['code']} Mixed Workouts &amp; Writing Models</div>
  </div>

  <div style="margin-bottom:4px;">
    <h1 style="font-family:'Montserrat',sans-serif; font-size:11.5pt; font-weight:900; color:{THEME['primary']}; margin:0 0 2px 0;">
      Mixed Workouts 1–6 &amp; Practical Writing Exemplars
    </h1>
    <p style="font-size:7.4pt; color:#64748b; margin:0 0 4px 0;">Full error keys for all vocational mixed workouts and examiner-approved model responses for practical writing.</p>
  </div>

  <div style="display:grid; grid-template-columns:1fr 1fr; gap:6px; height:248mm;">
    <div>
      <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.4pt; color:{THEME['primary']}; margin-bottom:2px;">
        MIXED PROOFREADING WORKOUTS 1 TO 6
      </div>
      {workouts_html}
    </div>
    <div>
      <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.4pt; color:#166534; margin-bottom:2px;">
        PRACTICAL WRITING TASKS 1 TO 6 (EXEMPLARS)
      </div>
      {exemplars_html}
    </div>
  </div>

  <div class="page-footer">
    <div>{THEME['title']} &bull; Explanatory Answer Key (Part 6)</div>
    <div class="page-num">Page 80</div>
  </div>
</div>
"""


def render_audit_checklist_page():
    """Generates Page 81: Candidate Self-Audit Checklist."""
    data = spag_data_e3_answers.AUDIT_CHECKLIST_DATA

    rows_html = ""
    for u_code, u_title, u_doc in data["units"]:
        rows_html += f"""
        <tr>
          <td style="font-weight:700; color:{THEME['primary']}; width:12%;">{u_code}</td>
          <td style="font-weight:600; width:44%;">{u_title}</td>
          <td style="color:#64748b; font-size:7.1pt; width:22%;">{u_doc}</td>
          <td style="text-align:center; width:11%;"><span class="rag-pill rag-red"></span><span class="rag-pill rag-amber"></span><span class="rag-pill rag-green"></span></td>
          <td style="border-bottom:1px dashed #94a3b8; width:11%;"></td>
        </tr>
        """

    return f"""
<div class="page">
  <div class="unit-page-header">
    <div class="brand-title">CANDIDATE SELF-AUDIT &bull; FINAL MASTERY TRACKER</div>
    <div class="strand-badge">{THEME['code']} Progress Sign-Off</div>
  </div>

  <div style="margin-bottom:5px;">
    <h1 style="font-family:'Montserrat',sans-serif; font-size:12.5pt; font-weight:900; color:{THEME['primary']}; margin:0 0 2px 0;">
      Entry Level 3 SPaG Candidate Self-Audit Checklist
    </h1>
    <p style="font-size:7.6pt; color:#64748b; margin:0 0 5px 0;">Rate your confidence across all 24 curriculum units: Red (Need Revision), Amber (Developing), Green (Secure Mastery).</p>
  </div>

  <!-- Audit Table -->
  <table class="mfs-table" style="font-size:6.8pt; margin-bottom:6px;">
    <thead>
      <tr>
        <th>Unit</th>
        <th>Curriculum SPaG Topic</th>
        <th>Workplace Document Format</th>
        <th>Self RAG</th>
        <th>Tutor Sign-Off</th>
      </tr>
    </thead>
    <tbody>
      {rows_html}
    </tbody>
  </table>

  <!-- Final Commitment Block -->
  <div style="background:#ffffff; border:1.5px solid #cbd5e1; border-radius:5px; padding:6px 10px; margin-top:auto; font-size:7.4pt;">
    <strong style="color:{THEME['primary']}; font-family:'Montserrat',sans-serif;">FINAL CANDIDATE COMMITMENT &amp; EXAM READINESS DECLARATION:</strong><br>
    I confirm that I have completed all 24 two-page units, reviewed my diagnostic priorities, and practiced functional workplace writing tasks.
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:8px; margin-top:5px;">
      <div>Candidate Signature: <div style="border-bottom:1px dashed #94a3b8; height:15px; margin-top:2px;"></div></div>
      <div>Tutor / Assessor Signature: <div style="border-bottom:1px dashed #94a3b8; height:15px; margin-top:2px;"></div></div>
      <div>Completion Date: <div style="border-bottom:1px dashed #94a3b8; height:15px; margin-top:2px;"></div></div>
    </div>
  </div>

  <div class="page-footer">
    <div>{THEME['title']} &bull; Candidate Self-Audit Checklist</div>
    <div class="page-num">Page 81</div>
  </div>
</div>
"""


def render_back_cover():
    """Generates Page 82: High-Impact Full-Bleed Back Cover."""
    return f"""
<div class="page cover-page" style="background: linear-gradient(145deg, {THEME['cover_grad_start']} 0%, {THEME['cover_grad_mid']} 55%, {THEME['cover_grad_end']} 100%);">
  <div style="padding: 16mm 16mm 0 16mm;">
    <!-- Top Header -->
    <div style="display:flex; justify-content:space-between; align-items:center; border-bottom: 1.5px solid rgba(255,255,255,0.25); padding-bottom:10px;">
      <div>
        <div style="font-family:'Montserrat',sans-serif; font-size:12.5pt; font-weight:900; letter-spacing:2.5px; color:#ffffff;">MASTER FUNCTIONAL SKILLS</div>
        <div style="font-size:7.2pt; font-weight:700; letter-spacing:1.5px; color:#fbbf24; margin-top:2px;">OFFICIAL OFQUAL CURRICULUM SERIES</div>
      </div>
      <div style="background:{THEME['badge_bg']}; color:#ffffff; font-family:'Montserrat',sans-serif; font-weight:900; font-size:8pt; padding:4px 12px; border-radius:16px;">
        {THEME['title'].upper()}
      </div>
    </div>

    <!-- Main Back Cover Headline -->
    <div style="margin-top:14mm;">
      <div style="font-family:'Montserrat',sans-serif; font-size:20pt; font-weight:900; color:#ffffff; line-height:1.2;">
        THE DEFINITIVE DYSLEXIA-FRIENDLY<br>SPAG MASTERY SYSTEM
      </div>
      <div style="font-size:9pt; color:#fde68a; margin-top:6px; font-weight:600;">
        Built specifically for Entry Level 3 Functional Skills learners across the UK.
      </div>
      <p style="font-size:8pt; color:rgba(255,255,255,0.85); line-height:1.5; margin-top:6px; max-width:160mm;">
        Engineered from the ground up to eradicate exam anxiety and build durable workplace literacy. Combines the world-renowned Raymond Murphy two-page spread architecture with British Dyslexia Association visual ergonomics.
      </p>
    </div>

    <!-- 4 Key Value Pillars -->
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:9px; margin-top:10mm;">
      <div style="background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.18); border-radius:5px; padding:7px 11px;">
        <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.8pt; color:#38bdf8;">24 SYSTEMATIC UNITS</div>
        <div style="font-size:7.2pt; color:rgba(255,255,255,0.8); margin-top:2px;">Covers every Ofqual requirement: capital letters, punctuation, SVO, connectives, tenses, agreement, and plurals.</div>
      </div>
      <div style="background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.18); border-radius:5px; padding:7px 11px;">
        <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.8pt; color:#34d399;">PHONICS &amp; WORD BANKS</div>
        <div style="font-size:7.2pt; color:rgba(255,255,255,0.8); margin-top:2px;">8 dedicated pages of spelling rules (doubling, silent 'e', 'ie/ei') and high-yield workplace vocabulary.</div>
      </div>
      <div style="background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.18); border-radius:5px; padding:7px 11px;">
        <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.8pt; color:#f472b6;">AUTHENTIC PROOFREADING</div>
        <div style="font-size:7.2pt; color:rgba(255,255,255,0.8); margin-top:2px;">Realistic workplace documents from healthcare, logistics, catering, retail, facilities, and administration.</div>
      </div>
      <div style="background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.18); border-radius:5px; padding:7px 11px;">
        <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.8pt; color:#fbbf24;">FULL ANSWER EXPLANATIONS</div>
        <div style="font-size:7.2pt; color:rgba(255,255,255,0.8); margin-top:2px;">Step-by-step reasoning for all 24 units, baseline diagnostic, mixed workouts, and writing tasks.</div>
      </div>
    </div>
  </div>

  <!-- Bottom Details & Barcode -->
  <div style="background:rgba(0,0,0,0.4); padding:8mm 16mm; border-top:1px solid rgba(255,255,255,0.15); display:flex; justify-content:space-between; align-items:center;">
    <div style="font-size:7.2pt; color:rgba(255,255,255,0.75); line-height:1.4;">
      <strong>Master Functional Skills Series</strong> &bull; Subject Code: FS-ENG-E3<br>
      Suitable for Pearson Edexcel, City &amp; Guilds, NCFE, Highfield, and Open Awards.<br>
      Visit <strong>masterfunctionalskills.co.uk</strong> for interactive online tests and revision cards.
    </div>
    <div style="background:#ffffff; color:#000000; padding:6px 12px; border-radius:4px; font-family:'Courier New',monospace; font-size:8pt; font-weight:bold; text-align:center;">
      ISBN 978-1-916892-04-9<br>
      [ ||| | ||||| || ||| | ]
    </div>
  </div>
</div>
"""


# =============================================================================
# MASTER COMPILATION PIPELINE
# =============================================================================

def build_complete_book():
    """Generates the full 82-page HTML document and compiles to PDF."""
    print("=" * 70)
    print(f"COMPILING 82-PAGE {THEME['full_name'].upper()}")
    print("=" * 70)

    pages_html = []

    # Page 1: Cover
    print("Rendering Page 1: Front Cover...")
    pages_html.append(render_front_cover())

    # Page 2: Inside Cover
    print("Rendering Page 2: Inside Cover & Dyslexia Statement...")
    pages_html.append(render_inside_cover())

    # Pages 3 to 5: Diagnostic Part 1, 2, 3
    print("Rendering Pages 3–5: Baseline Diagnostic Assessment (24 Qs)...")
    qs = spag_data_e3_84p.DIAGNOSTIC_QUESTIONS
    pages_html.append(render_diagnostic_part(qs[0:8], 1, 3, "Capitals & Basic Punctuation"))
    pages_html.append(render_diagnostic_part(qs[8:16], 2, 4, "Sentence Building & Connectives"))
    pages_html.append(render_diagnostic_part(qs[16:24], 3, 5, "Tenses, Agreement & Spelling"))

    # Page 6: Visual Study Selector
    print("Rendering Page 6: Visual Study Selector & RAG Action Matrix...")
    pages_html.append(render_diagnostic_selector())

    # Pages 7 to 54: 24 Units (48 pages)
    print("Rendering Pages 7–54: 24 Murphy Two-Page Spread Units...")
    for idx, unit_data in enumerate(generate_e3_data.units_data, 1):
        left_p = 6 + (idx * 2) - 1
        right_p = 6 + (idx * 2)
        pages_html.append(render_unit_left_page(unit_data, left_p))
        pages_html.append(render_unit_right_page(unit_data, right_p))

    # Pages 55 to 58: Phonics Spelling Rules (4 pages)
    print("Rendering Pages 55–58: Phonics Spelling Rules 1 to 4...")
    for rule_data in spag_data_e3_extras.PHONICS_RULES_PAGES:
        p_num = rule_data["page_num"]
        pages_html.append(render_phonics_page(rule_data, p_num))

    # Pages 59 to 62: Master Word Banks (4 pages)
    print("Rendering Pages 59–62: Master High-Frequency Word Banks 1 to 4...")
    for bank_data in spag_data_e3_extras.WORD_BANKS_PAGES:
        p_num = bank_data["page_num"]
        pages_html.append(render_word_bank_page(bank_data, p_num))

    # Pages 63 to 68: Mixed Proofreading Workouts (6 pages)
    print("Rendering Pages 63–68: Mixed Workplace Proofreading Workouts 1 to 6...")
    for workout_data in spag_data_e3_extras.MIXED_WORKOUTS_PAGES:
        p_num = workout_data["page_num"]
        pages_html.append(render_mixed_workout_page(workout_data, p_num))

    # Pages 69 to 74: Practical Workplace Writing Tasks (6 pages)
    print("Rendering Pages 69–74: Practical Workplace Writing Tasks 1 to 6...")
    for task_data in spag_data_e3_extras.WRITING_TASKS_PAGES:
        p_num = task_data["page_num"]
        pages_html.append(render_writing_task_page(task_data, p_num))

    # Pages 75 to 80: Explanatory Answer Key (6 pages)
    print("Rendering Pages 75–80: Complete Explanatory Answer Key...")
    pages_html.append(render_answer_key_page_75())
    pages_html.append(render_answer_key_page_units("page_76", 76))
    pages_html.append(render_answer_key_page_units("page_77", 77))
    pages_html.append(render_answer_key_page_units("page_78", 78))
    pages_html.append(render_answer_key_page_units("page_79", 79))
    pages_html.append(render_answer_key_page_80())

    # Page 81: Candidate Self-Audit Checklist
    print("Rendering Page 81: Candidate Self-Audit Checklist & Final Mastery Tracker...")
    pages_html.append(render_audit_checklist_page())

    # Page 82: High-Impact Back Cover
    print("Rendering Page 82: High-Impact Back Cover...")
    pages_html.append(render_back_cover())

    print(f"\nTotal rendered pages count in memory: {len(pages_html)}")
    assert len(pages_html) == 82, f"Expected 82 pages, got {len(pages_html)}"

    # Assemble Full HTML Document
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{THEME['full_name']} &bull; SPaG Mastery Workbook (82-Page Edition)</title>
  {CSS_STYLES}
</head>
<body>
  {"".join(pages_html)}
</body>
</html>
"""

    temp_html_path = os.path.join(SCRATCH_DIR, f"{THEME['file_stem']}_82p.html")
    with open(temp_html_path, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"Saved complete HTML to: {temp_html_path} ({os.path.getsize(temp_html_path):,} bytes)")

    out_pdf_downloads = os.path.join(DOWNLOADS_DIR, f"{THEME['file_stem']}.pdf")
    out_pdf_documents = os.path.join(DOCUMENTS_DIR, f"{THEME['file_stem']}.pdf")

    print(f"Compiling PDF via Chromium headless: {out_pdf_downloads}...")
    start_time = time.time()

    cmd = [
        CHROME_BIN,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--user-data-dir=/tmp/chr_e3_82p_build",
        "--no-pdf-header-footer",
        f"--print-to-pdf={out_pdf_downloads}",
        temp_html_path
    ]

    subprocess.run(cmd, check=True)
    comp_time = time.time() - start_time
    print(f"Compilation finished in {comp_time:.1f} seconds.")

    # Copy to /home/subi/Documents
    shutil.copy2(out_pdf_downloads, out_pdf_documents)
    print(f"Copied to: {out_pdf_documents}")

    # Verify Page Count with pdfinfo
    res = subprocess.run(["pdfinfo", out_pdf_downloads], capture_output=True, text=True, check=True)
    page_count = None
    for line in res.stdout.splitlines():
        if "Pages:" in line:
            page_count = int(line.split(":")[1].strip())
            break

    file_size_mb = os.path.getsize(out_pdf_downloads) / (1024 * 1024)
    print(f"\n=======================================================")
    print(f"VERIFICATION SUMMARY FOR {THEME['file_stem']}.pdf:")
    print(f"  * Page Count: {page_count} Pages (Target: 80–84 pages)")
    print(f"  * File Size:  {file_size_mb:.2f} MB")
    print(f"  * Downloads:  {out_pdf_downloads}")
    print(f"  * Documents:  {out_pdf_documents}")
    print(f"=======================================================\n")

    if page_count < 80 or page_count > 84:
        raise ValueError(f"Page count {page_count} is outside target range 80–84!")

    return out_pdf_downloads, out_pdf_documents, page_count


if __name__ == "__main__":
    build_complete_book()
