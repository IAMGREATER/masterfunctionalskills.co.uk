#!/usr/bin/env python3
"""
build_spag_l2_84p.py
=============================================================================
Master Functional Skills: 84-Page Level 2 SPaG Mastery Publication Generator
Full Raymond Murphy 'English Grammar in Use' Two-Page Spread Architecture
Strictly 100% Dyslexia-Friendly & British Dyslexia Association Educational Publishing.

Exact 84-Page Architectural Layout:
- Page 1: Full-Bleed Front Cover (Deep Navy theme)
- Page 2: Inside Cover & Dyslexia Statement & Candidate Verification
- Pages 3–6: Comprehensive Baseline Diagnostic Assessment (40 Tagged Questions) & Murphy Study Guide
- Pages 7–58: 26 Two-Page Murphy 'Grammar in Use' Units (2 pages per unit = 52 pages)
- Pages 59–64: Vocabulary in Use Master Modules (6 pages)
- Pages 65–70: Murphy-Style Mixed Additional Workouts (6 pages)
- Pages 71–76: Official Exam Proofreading & Extended Writing Mocks with Ruled Writing Frames (6 pages)
- Pages 77–82: Comprehensive Explanatory Answer Key with Examiner Mark Breakdown (6 pages)
- Page 83: Candidate Self-Audit Checklist & Progress Matrix (1 page)
- Page 84: High-Impact Full-Bleed Back Cover (1 page)

Target Output Destinations:
- /home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk/assets/downloads/MasterFunctionalSkills_SPaG_Level_2_Mastery.pdf
- /home/subi/Documents/MasterFunctionalSkills_SPaG_Level_2_Mastery.pdf
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

import spag_l2_84p_units_1_13 as u_part1
import spag_l2_84p_units_14_26 as u_part2
import spag_l2_84p_diag_vocab as dv
import spag_l2_84p_mocks_keys as mk

PROJECT_DIR = "/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk"
DOWNLOADS_DIR = os.path.join(PROJECT_DIR, "assets", "downloads")
DOCUMENTS_DIR = "/home/subi/Documents"
SCRATCH_DIR = os.path.join(PROJECT_DIR, "scratch", "spag_build")
CHROME_BIN = "/usr/lib/chromium/chromium"

os.makedirs(DOWNLOADS_DIR, exist_ok=True)
os.makedirs(DOCUMENTS_DIR, exist_ok=True)
os.makedirs(SCRATCH_DIR, exist_ok=True)

# Theme tokens for Deep Navy Level 2
THEME = {
    "code": "L2",
    "level_title": "LEVEL 2 MASTERY",
    "full_title": "Functional Skills English Level 2",
    "sub_title": "The Comprehensive 84-Page SPaG Self-Study & Revision Manual",
    "primary": "#002046",
    "secondary": "#1e3a8a",
    "accent": "#2563eb",
    "amber": "#fbbf24",
    "amber_dark": "#b45309",
    "cream_bg": "#FDFBF7",
    "text_dark": "#1F2937",
    "border_light": "#cbd5e1",
    "card_bg": "#ffffff",
    "file_stem": "MasterFunctionalSkills_SPaG_Level_2_Mastery"
}

CUSTOM_CSS = f"""
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
    color: {THEME['text_dark']};
    background: #ffffff;
    font-size: 8.1pt;
    line-height: 1.46;
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
    padding: 10mm 13mm 11mm 13mm;
    background: {THEME['cream_bg']};
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
  }}

  .cover-page {{
    padding: 0 !important;
    background: #002046;
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
    padding: 2px 7px;
    border-radius: 4px;
    border: 1px solid #cbd5e1;
  }}

  .unit-main-heading {{
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 6px;
  }}
  .unit-num-pill {{
    background: {THEME['primary']};
    color: #ffffff;
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 7.8pt;
    padding: 3px 9px;
    border-radius: 12px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    white-space: nowrap;
  }}
  .unit-title-text {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 11pt;
    color: {THEME['primary']};
    line-height: 1.2;
    margin: 0;
  }}

  .page-footer {{
    position: absolute;
    bottom: 5.5mm;
    left: 13mm;
    right: 13mm;
    border-top: 1px solid #cbd5e1;
    padding-top: 3px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 7.1pt;
    color: #64748b;
  }}
  .page-num {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    color: {THEME['primary']};
    background: #e2e8f0;
    padding: 1px 7px;
    border-radius: 4px;
  }}

  /* Dyslexia Cards */
  .card-anchor {{
    background: #F0F9FF;
    border: 1px solid #BAE6FD;
    border-left: 4.5px solid #0284C7;
    border-radius: 6px;
    padding: 6px 9px;
    margin-bottom: 6px;
  }}
  .card-anchor .card-title {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 7.8pt;
    color: #0369a1;
    text-transform: uppercase;
    letter-spacing: 0.4px;
    margin-bottom: 2px;
  }}

  .card-formula {{
    background: #ffffff;
    border: 1px solid #E2E8F0;
    border-left: 4.5px solid {THEME['secondary']};
    border-radius: 6px;
    padding: 6px 9px;
    margin-bottom: 6px;
  }}
  .card-formula .card-title {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 7.8pt;
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
    margin: 4px 0;
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

  /* Compare Card */
  .card-compare {{
    background: #ffffff;
    border: 1px solid #E2E8F0;
    border-radius: 6px;
    overflow: hidden;
    margin-bottom: 6px;
  }}
  .compare-row-bad {{
    background: #FEF2F2;
    border-left: 4.5px solid #DC2626;
    padding: 5px 9px;
    border-bottom: 1px solid #FEE2E2;
  }}
  .compare-row-good {{
    background: #F0FDF4;
    border-left: 4.5px solid #16A34A;
    padding: 5px 9px;
    border-bottom: 1px solid #DCFCE7;
  }}
  .compare-row-why {{
    background: #FFFBEB;
    border-left: 4.5px solid #D97706;
    padding: 5px 9px;
    font-size: 7.7pt;
    color: #92400e;
  }}
  .compare-badge {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 7.1pt;
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
    border-left: 4.5px solid #D97706;
    border-radius: 6px;
    padding: 6px 9px;
    margin-top: auto;
  }}
  .card-golden .card-title {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 7.8pt;
    color: #b45309;
    text-transform: uppercase;
    letter-spacing: 0.4px;
    margin-bottom: 2px;
  }}

  /* Right-hand Exercises Layout */
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
    font-size: 7.7pt;
    color: {THEME['primary']};
    text-transform: uppercase;
    letter-spacing: 0.3px;
  }}
  .ex-marks {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    font-size: 7.1pt;
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
    font-size: 7.6pt;
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
    border: 1.5px solid #cbd5e1;
    border-radius: 5px;
    overflow: hidden;
    margin-bottom: 4px;
  }}
  .doc-topbar {{
    background: #f1f5f9;
    border-bottom: 1px solid #cbd5e1;
    padding: 3px 7px;
    font-size: 7.2pt;
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
    padding: 6px 9px;
    font-size: 7.8pt;
    line-height: 1.42;
    background: #ffffff;
  }}

  .applied-task-box {{
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 5px;
    padding: 5px 8px;
  }}
  .task-prompt {{
    font-size: 7.7pt;
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
    height: 48px;
    border: 1px solid #e2e8f0;
    border-radius: 3px;
  }}

  /* Diagnostic Questions Box */
  .diag-item {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 4px 7px;
    margin-bottom: 4px;
    font-size: 7.6pt;
  }}
  .diag-header {{
    display: flex;
    justify-content: space-between;
    font-weight: 700;
    margin-bottom: 2px;
  }}
  .diag-tag {{
    color: {THEME['secondary']};
    font-size: 7.1pt;
    font-weight: 800;
    background: #eff6ff;
    padding: 1px 5px;
    border-radius: 3px;
    border: 1px solid #bfdbfe;
  }}

  /* Tables */
  table.mfs-table {{
    width: 100%;
    border-collapse: collapse;
    margin: 5px 0;
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
# INDIVIDUAL PAGE GENERATORS
# =============================================================================

def render_page_1():
    """Page 1: Full-Bleed Front Cover (Deep Navy theme)"""
    return f"""
<div class="page cover-page" style="background: linear-gradient(145deg, #01142d 0%, #002046 55%, #0a2540 100%);">
  <div style="padding: 18mm 18mm 0 18mm;">
    <!-- Top Header -->
    <div style="display:flex; justify-content:space-between; align-items:center; border-bottom: 1.5px solid rgba(255,255,255,0.25); padding-bottom:12px;">
      <div>
        <div style="font-family:'Montserrat',sans-serif; font-size:13pt; font-weight:900; letter-spacing:2.5px; color:#ffffff;">MASTER FUNCTIONAL SKILLS</div>
        <div style="font-size:7.5pt; font-weight:700; letter-spacing:1.5px; color:#fbbf24; margin-top:2px;">OFFICIAL OFQUAL CURRICULUM SPECIFICATION &bull; LEVEL 2 ENGLISH</div>
      </div>
      <div style="background:{THEME['accent']}; color:#ffffff; font-family:'Montserrat',sans-serif; font-weight:900; font-size:8.5pt; padding:6px 14px; border-radius:20px; letter-spacing:1px; border:1px solid rgba(255,255,255,0.3); box-shadow:0 2px 8px rgba(0,0,0,0.3);">
        LEVEL 2 MASTERY
      </div>
    </div>

    <!-- Title Block -->
    <div style="margin-top:24mm;">
      <div style="font-family:'Montserrat',sans-serif; font-size:42pt; font-weight:900; color:rgba(255,255,255,0.08); letter-spacing:4px; line-height:0.9; text-transform:uppercase;">
        SPAG LEVEL 2
      </div>
      <div style="margin-top:-24px; font-family:'Montserrat',sans-serif; font-size:26pt; font-weight:900; color:#ffffff; line-height:1.15; letter-spacing:0.5px;">
        SPELLING, PUNCTUATION<br>&amp; GRAMMAR MASTERY
      </div>
      <div style="font-size:12.5pt; font-weight:700; color:#fbbf24; margin-top:10px; letter-spacing:0.5px;">
        The Comprehensive 84-Page Self-Study &amp; Revision Manual
      </div>
      <div style="font-size:8.5pt; color:rgba(255,255,255,0.85); margin-top:6px; max-width:165mm; line-height:1.5;">
        Engineered specifically for Pearson Edexcel, City &amp; Guilds, Highfield, and NCFE candidates. Built upon the Raymond Murphy 'English Grammar in Use' two-page facing spread architecture and McCarthy/Redman vocabulary frameworks.
      </div>
    </div>

    <!-- 4 Value Pillar Grid -->
    <div style="display:grid; grid-template-columns: 1fr 1fr; gap:12px; margin-top:20mm;">
      <div style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.15); border-radius:6px; padding:10px 12px;">
        <div style="font-family:'Montserrat',sans-serif; font-size:8.5pt; font-weight:800; color:#fbbf24;">26 TWO-PAGE MURPHY UNITS</div>
        <div style="font-size:7.5pt; color:rgba(255,255,255,0.8); margin-top:2px;">Facing theory, syntax formulas, contrast tables, and 4-tier progressive practice drills.</div>
      </div>
      <div style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.15); border-radius:6px; padding:10px 12px;">
        <div style="font-family:'Montserrat',sans-serif; font-size:8.5pt; font-weight:800; color:#fbbf24;">40-QUESTION DIAGNOSTIC</div>
        <div style="font-size:7.5pt; color:rgba(255,255,255,0.8); margin-top:2px;">Comprehensive baseline assessment routing every question directly to target study units.</div>
      </div>
      <div style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.15); border-radius:6px; padding:10px 12px;">
        <div style="font-family:'Montserrat',sans-serif; font-size:8.5pt; font-weight:800; color:#fbbf24;">VOCABULARY &amp; WORKOUTS</div>
        <div style="font-size:7.5pt; color:rgba(255,255,255,0.8); margin-top:2px;">6 Vocabulary in Use master modules plus 6 mixed multi-topic reinforcement workouts.</div>
      </div>
      <div style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.15); border-radius:6px; padding:10px 12px;">
        <div style="font-family:'Montserrat',sans-serif; font-size:8.5pt; font-weight:800; color:#fbbf24;">6 OFFICIAL EXAM MOCKS</div>
        <div style="font-size:7.5pt; color:rgba(255,255,255,0.8); margin-top:2px;">Forensic proofreading challenges and 150-word extended writing frames with full solutions.</div>
      </div>
    </div>
  </div>

  <!-- Bottom Strip -->
  <div style="padding:14mm 18mm 16mm 18mm; background:rgba(0,0,0,0.35); border-top:1px solid rgba(255,255,255,0.15); display:flex; justify-content:space-between; align-items:center;">
    <div style="font-size:7.5pt; color:rgba(255,255,255,0.7);">
      <strong>100% Dyslexia-Friendly Architecture:</strong> Cream Canvas (#FDFBF7) &bull; Lexend Typography &bull; Ragged Right
    </div>
    <div style="font-family:'Montserrat',sans-serif; font-size:8.5pt; font-weight:900; color:#fbbf24; letter-spacing:1px;">
      masterfunctionalskills.co.uk
    </div>
  </div>
</div>
"""

def render_page_2():
    """Page 2: Inside Cover & Dyslexia Statement & Candidate Verification"""
    return f"""
<div class="page" style="--theme-primary:{THEME['primary']}; --theme-secondary:{THEME['secondary']};">
  <div class="unit-page-header">
    <div class="brand-title">INSIDE COVER &bull; CANDIDATE VERIFICATION &amp; METHODOLOGY</div>
    <div class="strand-badge">Level 2 Curriculum Standard</div>
  </div>

  <div style="margin-bottom:8px;">
    <h1 style="font-family:'Montserrat',sans-serif; font-size:13pt; font-weight:900; color:{THEME['primary']}; margin:0 0 2px 0;">
      Candidate &amp; Examination Centre Information
    </h1>
    <p style="font-size:7.8pt; color:#64748b; margin:0 0 6px 0;">Please complete the candidate details below before commencing the baseline diagnostic assessment.</p>
  </div>

  <!-- Candidate Details Form Box -->
  <div style="background:#ffffff; border:1.5px solid #cbd5e1; border-radius:6px; padding:8px 12px; margin-bottom:8px;">
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; font-size:8pt;">
      <div><strong>Candidate Full Name:</strong> <div style="border-bottom:1px dashed #94a3b8; height:18px; margin-top:2px;"></div></div>
      <div><strong>Candidate Reference / ULN:</strong> <div style="border-bottom:1px dashed #94a3b8; height:18px; margin-top:2px;"></div></div>
      <div><strong>Exam Centre Name:</strong> <div style="border-bottom:1px dashed #94a3b8; height:18px; margin-top:2px;"></div></div>
      <div><strong>Centre Number:</strong> <div style="border-bottom:1px dashed #94a3b8; height:18px; margin-top:2px;"></div></div>
      <div><strong>Awarding Body:</strong> <div style="font-size:7.6pt; color:#475569; margin-top:4px;">Pearson Edexcel / City &amp; Guilds / Highfield / NCFE</div></div>
      <div><strong>Assessor / Tutor Name:</strong> <div style="border-bottom:1px dashed #94a3b8; height:18px; margin-top:2px;"></div></div>
    </div>
  </div>

  <!-- Dyslexia Architecture Statement -->
  <div class="card-anchor" style="border-left-color:{THEME['primary']}; margin-bottom:8px;">
    <div class="card-title" style="color:{THEME['primary']};">
      DYSLEXIA-FRIENDLY ACCESSIBILITY &amp; TYPOGRAPHY STATEMENT
    </div>
    <p style="margin:0 0 4px 0; font-size:7.9pt;">
      This publication has been developed strictly adhering to British Dyslexia Association (BDA) and Ofqual accessibility standards. Reading fluency and cognitive ease are maximized through the following evidence-based features:
    </p>
    <ul style="margin:0 0 0 14px; padding:0; font-size:7.7pt; line-height:1.42;">
      <li><strong>Soft Warm Cream Canvas (#FDFBF7):</strong> Eliminates optical glare and visual stress associated with high-contrast pure white paper.</li>
      <li><strong>Lexend &amp; Atkinson Hyperlegible Fonts:</strong> Engineered with distinct character shapes to prevent common letter-mirroring traps (b/d/p/q).</li>
      <li><strong>Ragged-Right Left Alignment:</strong> Text is never justified, eradicating irregular letter spacing and disorienting 'rivers of white space'.</li>
      <li><strong>Generous Leading (1.48–1.52) &amp; Letter-Spacing (0.02em):</strong> Enhances horizontal tracking and prevents accidental line skipping.</li>
      <li><strong>Chunked Left-Bordered Cards:</strong> Grammatical categories are color-coded (Context: Blue; Formula: Slate; Pitfall: Red; Golden Rule: Amber).</li>
    </ul>
  </div>

  <!-- The Raymond Murphy Method -->
  <div class="card-formula" style="margin-bottom:8px;">
    <div class="card-title">THE RAYMOND MURPHY 'GRAMMAR IN USE' TWO-PAGE SPREAD ARCHITECTURE</div>
    <p style="margin:0 0 4px 0; font-size:7.9pt;">
      Each unit is structured as an interconnected facing two-page spread:
    </p>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:6px; font-size:7.5pt;">
      <div style="background:#f8fafc; padding:5px 7px; border-radius:4px; border:1px solid #e2e8f0;">
        <strong style="color:{THEME['primary']};">LEFT-HAND PAGE (Theory &amp; Formula):</strong><br>
        [A] Situational Workplace Anchor<br>
        [B] Syntax Architecture &amp; Formulas<br>
        [C] Compare &amp; Contrast (Pitfall vs Model vs Why)<br>
        [D] Examiner Golden Rule &amp; Memory Hook
      </div>
      <div style="background:#f8fafc; padding:5px 7px; border-radius:4px; border:1px solid #e2e8f0;">
        <strong style="color:{THEME['primary']};">RIGHT-HAND PAGE (Progressive Drills):</strong><br>
        [Ex 1] Recognition &amp; Discrimination<br>
        [Ex 2] Controlled Cloze / Transformation<br>
        [Ex 3] Forensic Workplace Proofreading<br>
        [Ex 4] Real-World Applied Writing Task
      </div>
    </div>
  </div>

  <!-- Publishing & Copyright Notice -->
  <div style="margin-top:auto; font-size:7.1pt; color:#64748b; border-top:1px solid #e2e8f0; padding-top:4px;">
    <strong>Published by:</strong> Master Functional Skills (masterfunctionalskills.co.uk) &bull; London, United Kingdom.<br>
    &copy; 2026 Master Functional Skills. All rights reserved. Registered examination training provider and educational publisher.
  </div>

  <div class="page-footer">
    <div>{THEME['level_title']} &bull; Inside Cover &amp; Methodology</div>
    <div class="page-num">Page 2</div>
  </div>
</div>
"""

def render_diagnostic_page(page_idx, questions_subset, page_num):
    """Pages 3-6: Renders 10 diagnostic questions per page."""
    q_html = ""
    for q in questions_subset:
        opts_html = " &nbsp; ".join([f"<span class='opt-box'><span class='opt-tick'></span> {opt}</span>" for opt in q["options"]])
        q_html += f"""
        <div class="diag-item">
          <div class="diag-header">
            <span><strong>Q{q['num']}.</strong> {q['prompt']}</span>
            <span class="diag-tag">[Routes to Unit {q['routes_to']}]</span>
          </div>
          <div style="margin-top:2px;">{opts_html}</div>
        </div>
        """

    bottom_box = ""
    if page_num == 6:
        bottom_box = f"""
        <div style="margin-top:4px; background:#EFF6FF; border:1px solid #BFDBFE; border-radius:5px; padding:5px 8px; font-size:7.4pt;">
          <div style="font-family:'Montserrat',sans-serif; font-weight:800; color:{THEME['primary']}; margin-bottom:2px;">
            DIAGNOSTIC SCORING MATRIX &bull; RAYMOND MURPHY STUDY PATHWAYS
          </div>
          <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:6px;">
            <div style="background:#ffffff; padding:3px 5px; border-radius:3px; border:1px solid #cbd5e1;">
              <strong style="color:#dc2626;">0–24 Marks (Foundation Need):</strong> Work through all 26 Units sequentially from Unit 1 to 26 before attempting Mocks.
            </div>
            <div style="background:#ffffff; padding:3px 5px; border-radius:3px; border:1px solid #cbd5e1;">
              <strong style="color:#d97706;">25–34 Marks (Targeted Priority):</strong> Complete tagged units for missed questions, then undertake Mixed Workouts 1–6.
            </div>
            <div style="background:#ffffff; padding:3px 5px; border-radius:3px; border:1px solid #cbd5e1;">
              <strong style="color:#16a34a;">35–40 Marks (Exam Ready):</strong> Complete Vocabulary Modules 1–6 and execute all 6 Official Exam Mocks.
            </div>
          </div>
        </div>
        """

    return f"""
<div class="page" style="--theme-primary:{THEME['primary']}; --theme-secondary:{THEME['secondary']};">
  <div class="unit-page-header">
    <div class="brand-title">BASELINE DIAGNOSTIC &bull; 40-QUESTION CURRICULUM AUDIT</div>
    <div class="strand-badge">Part {page_idx} of 4 &bull; Q{questions_subset[0]['num']} to Q{questions_subset[-1]['num']}</div>
  </div>

  <div style="margin-bottom:5px;">
    <h2 style="font-family:'Montserrat',sans-serif; font-size:11pt; font-weight:900; color:{THEME['primary']}; margin:0 0 1px 0;">
      Level 2 Baseline Diagnostic Assessment
    </h2>
    <p style="font-size:7.6pt; color:#64748b; margin:0;">
      Answer each question carefully. Every question routes directly to a dedicated study unit in this manual.
    </p>
  </div>

  <div style="display:flex; flex-direction:column; flex:1; justify-content:space-between;">
    {q_html}
    {bottom_box}
  </div>

  <div class="page-footer">
    <div>{THEME['level_title']} &bull; Diagnostic Assessment &bull; Questions {questions_subset[0]['num']}–{questions_subset[-1]['num']}</div>
    <div class="page-num">Page {page_num}</div>
  </div>
</div>
"""

def render_unit_left(unit_data, page_num):
    """Renders Left Page of Murphy Two-Page Spread."""
    u_num = unit_data["unit"]
    u_title = unit_data["title"]
    fmt = unit_data.get("format", "Workplace Document")

    anchor_title = unit_data.get("anchor_title", f"Workplace Scenario: {fmt}")
    anchor_text = unit_data.get("anchor_text", "Accurate syntax is essential in this vocational format.")
    rule_title = unit_data.get("rule_title", "Syntax Architecture & Core Structural Rules")
    rule_text = unit_data.get("rule_text", "")
    bad_text = unit_data.get("worked_bad", "Example with error.")
    good_text = unit_data.get("worked_good", "Corrected example.")
    why_text = unit_data.get("worked_why", "Grammatical explanation.")
    golden_rule = unit_data.get("golden_rule", "Verify sentence boundaries and verb agreement before submitting scripts.")

    return f"""
<div class="page" style="--theme-primary:{THEME['primary']}; --theme-secondary:{THEME['secondary']};">
  <div class="unit-page-header">
    <div class="brand-title">UNIT {u_num} &bull; THEORY &amp; VISUAL ARCHITECTURE</div>
    <div class="strand-badge">{unit_data.get('strand', 'SPaG Standard')}</div>
  </div>

  <div class="unit-main-heading">
    <span class="unit-num-pill">UNIT {u_num}</span>
    <h2 class="unit-title-text">{u_title}</h2>
  </div>

  <div style="display:flex; flex-direction:column; flex:1; justify-content:space-between;">
    <div class="card-anchor">
      <div class="card-title">[A] Situational Workplace Anchor: {anchor_title}</div>
      <p style="margin:0; font-size:7.9pt;">{anchor_text}</p>
    </div>

    <div class="card-formula">
      <div class="card-title">[B] {rule_title}</div>
      <div style="font-size:7.8pt; line-height:1.42;">{rule_text}</div>
    </div>

    <div class="card-compare">
      <div class="compare-row-bad">
        <span class="compare-badge badge-bad">❌ Pitfall</span>
        <span style="font-size:7.8pt; color:#991b1b;">{bad_text}</span>
      </div>
      <div class="compare-row-good">
        <span class="compare-badge badge-good">✔️ Model</span>
        <span style="font-size:7.8pt; color:#166534; font-weight:600;">{good_text}</span>
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
    <div>{THEME['level_title']} &bull; Unit {u_num}: {u_title}</div>
    <div class="page-num">Page {page_num}</div>
  </div>
</div>
"""

def render_unit_right(unit_data, page_num):
    """Renders Right Page of Murphy Two-Page Spread."""
    u_num = unit_data["unit"]
    fmt = unit_data.get("format", "Workplace Document")

    # Ex 1: Recognition
    ex1_html = ""
    for idx, item in enumerate(unit_data.get("exercise_a", [])[:4], 1):
        q_text, opts = item[0], item[1]
        opts_rendered = " &nbsp; ".join([f"<span class='opt-box'><span class='opt-tick'></span> {opt}</span>" for opt in opts])
        ex1_html += f"""
        <div style="margin-bottom:3px; font-size:7.5pt;">
          <div><strong>{idx}.</strong> {q_text}</div>
          <div style="margin-top:1.5px;">{opts_rendered}</div>
        </div>
        """

    # Ex 2: Cloze / Transformation
    ex2_html = ""
    for idx, item in enumerate(unit_data.get("exercise_b", [])[:3], 1):
        prompt_type, original, solution = item[0], item[1], item[2]
        ex2_html += f"""
        <div style="margin-bottom:3px; font-size:7.5pt;">
          <strong>{idx}. [{prompt_type}]:</strong> <em>'{original}'</em>
          <div style="border-bottom:1px dashed #cbd5e1; height:15px; margin-top:1px;"></div>
        </div>
        """

    # Ex 3: Forensic Proofreading
    doc_title = unit_data.get("proofreading_title", f"Applied Proofreading: {fmt}")
    doc_scenario = unit_data.get("proofreading_scenario", "Locate and correct deliberate SPaG errors.")
    doc_text = unit_data.get("proofreading_text", "")
    err_count = len(unit_data.get("proofreading_errors", [1,2,3,4,5]))

    # Ex 4: Applied Writing
    writing_prompt = unit_data.get("writing_prompt", "Write three complete, correctly punctuated sentences for this workplace format.")

    return f"""
<div class="page" style="--theme-primary:{THEME['primary']}; --theme-secondary:{THEME['secondary']};">
  <div class="unit-page-header">
    <div class="brand-title">UNIT {u_num} &bull; PROGRESSIVE PRACTICE DRILLS</div>
    <div class="strand-badge">Applied Workplace Drills</div>
  </div>

  <div class="unit-main-heading">
    <span class="unit-num-pill">UNIT {u_num}</span>
    <h2 class="unit-title-text">Practice Drills &amp; Forensic Proofreading</h2>
  </div>

  <div style="display:flex; flex-direction:column; flex:1; justify-content:space-between;">
    <!-- EXERCISE 1 -->
    <div class="exercise-section">
      <div class="ex-header">
        <span class="ex-title">[EXERCISE 1] Recognition &amp; Discrimination</span>
        <span class="ex-marks">4 Marks</span>
      </div>
      <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:4px; padding:4px 7px;">
        {ex1_html}
      </div>
    </div>

    <!-- EXERCISE 2 -->
    <div class="exercise-section">
      <div class="ex-header">
        <span class="ex-title">[EXERCISE 2] Controlled Sentence Completion &amp; Transformation</span>
        <span class="ex-marks">3 Marks</span>
      </div>
      <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:4px; padding:4px 7px;">
        {ex2_html}
      </div>
    </div>

    <!-- EXERCISE 3 -->
    <div class="exercise-section">
      <div class="ex-header">
        <span class="ex-title">[EXERCISE 3] Forensic Workplace Proofreading Scenario</span>
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

    <!-- EXERCISE 4 -->
    <div class="exercise-section">
      <div class="ex-header">
        <span class="ex-title">[EXERCISE 4] Applied Functional Writing Task</span>
        <span class="ex-marks">5 Marks</span>
      </div>
      <div class="applied-task-box">
        <div class="task-prompt">{writing_prompt}</div>
        <div class="task-lines"></div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div>{THEME['level_title']} &bull; Unit {u_num}: Practice Drills</div>
    <div class="page-num">Page {page_num}</div>
  </div>
</div>
"""

def render_vocab_module(mod_data, page_num):
    """Pages 59-64: Vocabulary in Use Master Modules."""
    tbl_headers = "".join([f"<th>{h}</th>" for h in mod_data["table_headers"]])
    tbl_rows = ""
    for r in mod_data["table_rows"]:
        cells = "".join([f"<td>{c}</td>" for c in r])
        tbl_rows += f"<tr>{cells}</tr>"

    ex_html = ""
    for idx, (prompt, sol) in enumerate(mod_data["exercises"], 1):
        ex_html += f"""
        <div style="margin-bottom:2.5px; font-size:7.5pt;">
          <strong>{idx}.</strong> {prompt}
        </div>
        """

    return f"""
<div class="page" style="--theme-primary:{THEME['primary']}; --theme-secondary:{THEME['secondary']};">
  <div class="unit-page-header">
    <div class="brand-title">VOCABULARY IN USE &bull; MASTER MODULE {mod_data['module']}</div>
    <div class="strand-badge">Lexical Architecture</div>
  </div>

  <div class="unit-main-heading">
    <span class="unit-num-pill">MODULE {mod_data['module']}</span>
    <h2 class="unit-title-text">{mod_data['title']}</h2>
  </div>

  <div style="display:flex; flex-direction:column; flex:1; justify-content:space-between;">
    <div class="card-formula">
      <div class="card-title">{mod_data['theory_title']}</div>
      <div style="font-size:7.8pt; line-height:1.42;">{mod_data['theory_text']}</div>
    </div>

    <div style="margin-bottom:5px;">
      <table class="mfs-table">
        <thead><tr>{tbl_headers}</tr></thead>
        <tbody>{tbl_rows}</tbody>
      </table>
    </div>

    <div class="exercise-section">
      <div class="ex-header">
        <span class="ex-title">[APPLIED DRILLS] Practical Word Formation &amp; Collocation</span>
        <span class="ex-marks">6 Marks</span>
      </div>
      <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:4px; padding:5px 8px;">
        {ex_html}
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div>{THEME['level_title']} &bull; Vocabulary Master Module {mod_data['module']}</div>
    <div class="page-num">Page {page_num}</div>
  </div>
</div>
"""

def render_workout_page(workout_data, page_num):
    """Pages 65-70: Murphy-Style Mixed Additional Workouts."""
    w_num = workout_data["workout"]

    # Drill 1
    d1_html = ""
    for idx, (item, note) in enumerate(workout_data["drill_1_items"], 1):
        d1_html += f"""
        <div style="margin-bottom:2.5px; font-size:7.5pt;">
          <strong>{idx}.</strong> {item}
        </div>
        """

    # Drill 2
    d2_html = ""
    for idx, (prompt, sol) in enumerate(workout_data["drill_2_items"], 1):
        d2_html += f"""
        <div style="margin-bottom:2.5px; font-size:7.5pt;">
          <strong>{idx}.</strong> {prompt}
          <div style="border-bottom:1px dashed #cbd5e1; height:15px; margin-top:1px;"></div>
        </div>
        """

    return f"""
<div class="page" style="--theme-primary:{THEME['primary']}; --theme-secondary:{THEME['secondary']};">
  <div class="unit-page-header">
    <div class="brand-title">MIXED WORKOUT &bull; SYNTHESIS SPREAD {w_num}</div>
    <div class="strand-badge">{workout_data['coverage'].split(':')[0]}</div>
  </div>

  <div class="unit-main-heading">
    <span class="unit-num-pill">WORKOUT {w_num}</span>
    <h2 class="unit-title-text">{workout_data['title']}</h2>
  </div>

  <div style="display:flex; flex-direction:column; flex:1; justify-content:space-between;">
    <div style="background:#EFF6FF; border:1px solid #BFDBFE; border-radius:4px; padding:4px 7px; font-size:7.4pt; margin-bottom:5px;">
      <strong>Curriculum Coverage:</strong> {workout_data['coverage']}
    </div>

    <!-- DRILL 1 -->
    <div class="exercise-section">
      <div class="ex-header">
        <span class="ex-title">{workout_data['drill_1_title']}</span>
        <span class="ex-marks">5 Marks</span>
      </div>
      <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:4px; padding:4px 7px;">
        {d1_html}
      </div>
    </div>

    <!-- DRILL 2 -->
    <div class="exercise-section">
      <div class="ex-header">
        <span class="ex-title">{workout_data['drill_2_title']}</span>
        <span class="ex-marks">4 Marks</span>
      </div>
      <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:4px; padding:4px 7px;">
        {d2_html}
      </div>
    </div>

    <!-- DRILL 3: FORENSIC PROOFREADING -->
    <div class="exercise-section">
      <div class="ex-header">
        <span class="ex-title">{workout_data['drill_3_title']}</span>
        <span class="ex-marks">5 Marks</span>
      </div>
      <div class="workplace-doc">
        <div class="doc-topbar">
          <span>{workout_data['doc_title']}</span>
          <span>EXACT ERRORS: 5</span>
        </div>
        <div class="doc-body" style="font-size:7.6pt; line-height:1.4;">
          {workout_data['doc_text']}
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div>{THEME['level_title']} &bull; Additional Mixed Workout {w_num}</div>
    <div class="page-num">Page {page_num}</div>
  </div>
</div>
"""

def render_mock_page(mock_data, page_num):
    """Pages 71-76: Official Exam Proofreading & Extended Writing Mocks with Ruled Writing Frames."""
    m_num = mock_data["mock_num"]

    return f"""
<div class="page" style="--theme-primary:{THEME['primary']}; --theme-secondary:{THEME['secondary']};">
  <div class="unit-page-header">
    <div class="brand-title">OFFICIAL EXAM MOCK &bull; ASSESSMENT MOCK {m_num}</div>
    <div class="strand-badge">{mock_data['board_style'].split('Functional')[0]}</div>
  </div>

  <div class="unit-main-heading">
    <span class="unit-num-pill">MOCK {m_num}</span>
    <h2 class="unit-title-text">{mock_data['title']}</h2>
  </div>

  <div style="display:flex; flex-direction:column; flex:1; justify-content:space-between;">
    <div style="background:#f8fafc; border:1px solid #e2e8f0; border-left:4px solid {THEME['primary']}; border-radius:4px; padding:4px 7px; font-size:7.4pt; margin-bottom:5px;">
      <strong>Vocational Scenario:</strong> {mock_data['scenario']}
    </div>

    <!-- PART 1: PROOFREADING -->
    <div class="exercise-section">
      <div class="ex-header">
        <span class="ex-title">[PART 1] Forensic Workplace Proofreading</span>
        <span class="ex-marks">5 Marks</span>
      </div>
      <div class="workplace-doc">
        <div class="doc-topbar">
          <span>{mock_data['proofreading_title']}</span>
          <span>EXACT ERRORS TO IDENTIFY &amp; CORRECT: {mock_data['proofreading_target']}</span>
        </div>
        <div class="doc-body" style="font-size:7.6pt; line-height:1.4;">
          {mock_data['proofreading_text']}
        </div>
      </div>
    </div>

    <!-- PART 2: EXTENDED WRITING FRAME -->
    <div class="exercise-section">
      <div class="ex-header">
        <span class="ex-title">[PART 2] Applied Workplace Extended Writing Task</span>
        <span class="ex-marks">10 Marks &bull; Approx. 150 Words</span>
      </div>
      <div class="applied-task-box">
        <div class="task-prompt">{mock_data['writing_task_prompt']}</div>
        <div style="background: repeating-linear-gradient(transparent, transparent 18px, #e2e8f0 19px, #e2e8f0 20px); height: 95px; border: 1px solid #e2e8f0; border-radius: 4px; margin-top:4px;"></div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div>{THEME['level_title']} &bull; Official Exam Mock {m_num}</div>
    <div class="page-num">Page {page_num}</div>
  </div>
</div>
"""

def render_answer_key_page_77():
    """Page 77: Diagnostic Answers + Units 1 to 4."""
    data = mk.ANSWER_KEYS_DATA["page_77"]
    diag = data["diagnostic_answers"]
    
    col1_rows = ""
    for qnum, ans, rat in diag[:20]:
        col1_rows += f"<tr><td style='font-weight:700;'>Q{qnum}</td><td style='font-weight:800; color:{THEME['primary']};'>{ans}</td><td style='font-size:6.7pt;'>{rat}</td></tr>"

    col2_rows = ""
    for qnum, ans, rat in diag[20:]:
        col2_rows += f"<tr><td style='font-weight:700;'>Q{qnum}</td><td style='font-weight:800; color:{THEME['primary']};'>{ans}</td><td style='font-size:6.7pt;'>{rat}</td></tr>"

    u_html = ""
    for unum in [1, 2, 3, 4]:
        udata = data["units"][unum]
        u_html += f"""
        <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:3px; padding:2px 5px; margin-bottom:2.5px; font-size:7pt;">
          <strong>Unit {unum}:</strong> <em>Ex 1:</em> {udata['ex_a']} &bull; <em>Ex 2:</em> {udata['ex_b']}<br>
          <span style="color:#0369a1;"><strong>Ex 3 Proofreading:</strong> {udata['ex_3_proof']}</span>
        </div>
        """

    return f"""
<div class="page" style="--theme-primary:{THEME['primary']}; --theme-secondary:{THEME['secondary']};">
  <div class="unit-page-header">
    <div class="brand-title">EXPLANATORY ANSWER KEY &bull; PART 1 OF 6</div>
    <div class="strand-badge">Diagnostic &amp; Units 1–4</div>
  </div>

  <div class="unit-main-heading">
    <span class="unit-num-pill">ANSWERS</span>
    <h2 class="unit-title-text">{data['title']}</h2>
  </div>

  <div style="display:flex; flex-direction:column; flex:1; justify-content:space-between;">
    <div>
      <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.4pt; color:{THEME['primary']}; margin-bottom:2px;">
        40-QUESTION DIAGNOSTIC ASSESSMENT &bull; COMPLETE ANSWER KEY &amp; RATIONALE
      </div>
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:6px;">
        <table class="mfs-table" style="margin:0; font-size:6.8pt;">
          <thead><tr><th style="width:12%;">Q#</th><th style="width:10%;">Ans</th><th>Examiner Rationale</th></tr></thead>
          <tbody>{col1_rows}</tbody>
        </table>
        <table class="mfs-table" style="margin:0; font-size:6.8pt;">
          <thead><tr><th style="width:12%;">Q#</th><th style="width:10%;">Ans</th><th>Examiner Rationale</th></tr></thead>
          <tbody>{col2_rows}</tbody>
        </table>
      </div>
    </div>

    <div style="margin-top:3px;">
      <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:7.4pt; color:{THEME['primary']}; margin-bottom:2px;">
        UNITS 1 TO 4 EXPLANATORY KEYS
      </div>
      {u_html}
    </div>
  </div>

  <div class="page-footer">
    <div>{THEME['level_title']} &bull; Answer Key Part 1</div>
    <div class="page-num">Page 77</div>
  </div>
</div>
"""

def render_answer_key_generic(page_num, key_id):
    """Pages 78-82: Units, Vocab, Workouts, and Mocks."""
    data = mk.ANSWER_KEYS_DATA[key_id]
    u_html = ""
    for unum, udata in data["units"].items():
        u_html += f"""
        <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:4px; padding:3px 6px; margin-bottom:3.5px; font-size:7.2pt;">
          <div style="font-weight:800; color:{THEME['primary']}; margin-bottom:1px;">UNIT {unum} ANSWER KEY</div>
          <div><strong>Ex 1:</strong> {udata['ex_a']} &bull; <strong>Ex 2:</strong> {udata['ex_b']}</div>
          <div style="color:#0369a1; margin-top:1px;"><strong>Ex 3 Proofreading:</strong> {udata['ex_3_proof']}</div>
        </div>
        """

    extra_html = ""
    if "vocab_modules" in data:
        extra_html += f"""
        <div style="margin-top:4px; background:#f8fafc; border:1px solid #cbd5e1; border-radius:4px; padding:4px 6px; font-size:7.1pt;">
          <div style="font-weight:800; color:{THEME['primary']}; margin-bottom:2px;">VOCABULARY MASTER MODULES 1 TO 6 &bull; SOLUTIONS</div>
          <div><strong>Mod 1:</strong> {data['vocab_modules'][1]} &bull; <strong>Mod 2:</strong> {data['vocab_modules'][2]}</div>
          <div><strong>Mod 3:</strong> {data['vocab_modules'][3]} &bull; <strong>Mod 4:</strong> {data['vocab_modules'][4]}</div>
          <div><strong>Mod 5:</strong> {data['vocab_modules'][5]} &bull; <strong>Mod 6:</strong> {data['vocab_modules'][6]}</div>
        </div>
        """

    if "workouts" in data:
        extra_html += f"""
        <div style="margin-top:3px; background:#EFF6FF; border:1px solid #BFDBFE; border-radius:4px; padding:4px 6px; font-size:7.1pt;">
          <div style="font-weight:800; color:{THEME['primary']}; margin-bottom:2px;">MIXED ADDITIONAL WORKOUTS 1 TO 6 &bull; DRILL &amp; PROOFREADING SOLUTIONS</div>
          <div><strong>W1:</strong> {data['workouts'][1]}</div>
          <div><strong>W2:</strong> {data['workouts'][2]}</div>
          <div><strong>W3:</strong> {data['workouts'][3]}</div>
          <div><strong>W4:</strong> {data['workouts'][4]}</div>
          <div><strong>W5:</strong> {data['workouts'][5]}</div>
          <div><strong>W6:</strong> {data['workouts'][6]}</div>
        </div>
        """

    if "exam_mocks_proof_summary" in data:
        extra_html += f"""
        <div style="margin-top:3px; background:#FEFCE8; border:1px solid #FEF08A; border-radius:4px; padding:4px 6px; font-size:7.1pt;">
          <div style="font-weight:800; color:#b45309; margin-bottom:2px;">OFFICIAL EXAM MOCKS 1 TO 6 &bull; PROOFREADING CORRECTIONS</div>
          <div><strong>Mock 1:</strong> {data['exam_mocks_proof_summary'][1]}</div>
          <div><strong>Mock 2:</strong> {data['exam_mocks_proof_summary'][2]}</div>
          <div><strong>Mock 3:</strong> {data['exam_mocks_proof_summary'][3]}</div>
          <div><strong>Mock 4:</strong> {data['exam_mocks_proof_summary'][4]}</div>
          <div><strong>Mock 5:</strong> {data['exam_mocks_proof_summary'][5]}</div>
          <div><strong>Mock 6:</strong> {data['exam_mocks_proof_summary'][6]}</div>
        </div>
        """

    return f"""
<div class="page" style="--theme-primary:{THEME['primary']}; --theme-secondary:{THEME['secondary']};">
  <div class="unit-page-header">
    <div class="brand-title">EXPLANATORY ANSWER KEY &bull; {data['title'].upper()}</div>
    <div class="strand-badge">Level 2 Examiner Mark Scheme</div>
  </div>

  <div class="unit-main-heading">
    <span class="unit-num-pill">KEY</span>
    <h2 class="unit-title-text">{data['title']}</h2>
  </div>

  <div style="display:flex; flex-direction:column; flex:1; justify-content:space-between;">
    <div>
      {u_html}
    </div>
    {extra_html}
  </div>

  <div class="page-footer">
    <div>{THEME['level_title']} &bull; Explanatory Answer Key</div>
    <div class="page-num">Page {page_num}</div>
  </div>
</div>
"""

def render_page_83(units_list):
    """Page 83: Candidate Self-Audit Checklist & Progress Matrix."""
    rows = ""
    for u in units_list:
        rows += f"""
        <tr>
          <td style="font-weight:700; width:12%;">Unit {u['unit']}</td>
          <td style="font-weight:600; width:52%; font-size:7.2pt;">{u['title']}</td>
          <td style="text-align:center; width:12%;"><span class="rag-pill rag-red"></span><span class="rag-pill rag-amber"></span><span class="rag-pill rag-green"></span></td>
          <td style="text-align:center; width:12%;"><span class="rag-pill rag-red"></span><span class="rag-pill rag-amber"></span><span class="rag-pill rag-green"></span></td>
          <td style="width:12%; border-bottom:1px dashed #cbd5e1;"></td>
        </tr>
        """

    return f"""
<div class="page" style="--theme-primary:{THEME['primary']}; --theme-secondary:{THEME['secondary']};">
  <div class="unit-page-header">
    <div class="brand-title">STUDENT SELF-AUDIT &bull; 26-UNIT PROGRESS MATRIX</div>
    <div class="strand-badge">Ofqual Candidate Verification</div>
  </div>

  <div class="unit-main-heading">
    <span class="unit-num-pill">AUDIT</span>
    <h2 class="unit-title-text">Candidate Self-Audit Checklist &amp; Exam Readiness Matrix</h2>
  </div>

  <div style="margin-bottom:4px; font-size:7.4pt; color:#475569;">
    Track your learning progress using the RAG rating system: <strong>Red</strong> = Needs Tutor Input &bull; <strong>Amber</strong> = Review Required &bull; <strong>Green</strong> = Secure Mastery.
  </div>

  <div style="flex:1; overflow:hidden;">
    <table class="mfs-table" style="font-size:6.9pt;">
      <thead>
        <tr>
          <th>Unit</th>
          <th>Syllabus Topic &amp; Focus Area</th>
          <th style="text-align:center;">Theory [A–D]</th>
          <th style="text-align:center;">Drills [1–4]</th>
          <th>Tutor Sign</th>
        </tr>
      </thead>
      <tbody>
        {rows}
      </tbody>
    </table>
  </div>

  <div style="margin-top:4px; background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:4px 8px; font-size:7.3pt; display:flex; justify-content:space-between; align-items:center;">
    <div><strong>Overall Exam Readiness Score:</strong> _______ / 100%</div>
    <div><strong>Assessor Final Sign-Off:</strong> ____________________________</div>
    <div><strong>Date:</strong> ____ / ____ / 2026</div>
  </div>

  <div class="page-footer">
    <div>{THEME['level_title']} &bull; Candidate Progress Matrix</div>
    <div class="page-num">Page 83</div>
  </div>
</div>
"""

def render_page_84():
    """Page 84: High-Impact Full-Bleed Back Cover."""
    return f"""
<div class="page cover-page" style="background: linear-gradient(145deg, #01142d 0%, #002046 55%, #0a2540 100%);">
  <div style="padding: 18mm 18mm 0 18mm;">
    <!-- Top Brand Header -->
    <div style="display:flex; justify-content:space-between; align-items:center; border-bottom: 1.5px solid rgba(255,255,255,0.25); padding-bottom:12px;">
      <div>
        <div style="font-family:'Montserrat',sans-serif; font-size:13pt; font-weight:900; letter-spacing:2.5px; color:#ffffff;">MASTER FUNCTIONAL SKILLS</div>
        <div style="font-size:7.5pt; font-weight:700; letter-spacing:1.5px; color:#fbbf24; margin-top:2px;">THE UK BENCHMARK IN VOCATIONAL ENGLISH PUBLISHING</div>
      </div>
      <div style="background:{THEME['accent']}; color:#ffffff; font-family:'Montserrat',sans-serif; font-weight:900; font-size:8.5pt; padding:6px 14px; border-radius:20px; letter-spacing:1px; border:1px solid rgba(255,255,255,0.3);">
        LEVEL 2 SPAG
      </div>
    </div>

    <!-- Main Features Summary -->
    <div style="margin-top:20mm;">
      <h2 style="font-family:'Montserrat',sans-serif; font-size:22pt; font-weight:900; color:#ffffff; line-height:1.2; letter-spacing:0.5px; margin:0 0 10px 0;">
        Why Functional Skills English Level 2 Candidates Succeed with This Manual
      </h2>
      <p style="font-size:8.5pt; color:rgba(255,255,255,0.85); line-height:1.5; max-width:165mm; margin:0 0 16mm 0;">
        Functional Skills English Level 2 requires far more than basic punctuation. Examiners demand sophisticated complex sentences, nuanced subordination, professional register calibration, and zero tolerance for sentence fragments, comma splices, or dangling modifiers. This 84-page manual provides the complete scaffolding required to guarantee exam success.
      </p>

      <div style="display:grid; grid-template-columns: 1fr 1fr; gap:12px;">
        <div style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.15); border-radius:6px; padding:10px 12px;">
          <div style="font-family:'Montserrat',sans-serif; font-size:8.5pt; font-weight:800; color:#fbbf24;">THE RAYMOND MURPHY METHOD</div>
          <div style="font-size:7.5pt; color:rgba(255,255,255,0.8); margin-top:2px;">
            Facing two-page spreads isolate single grammatical targets. Clear formulas on the left lead directly into progressive 4-tier drills on the right.
          </div>
        </div>
        <div style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.15); border-radius:6px; padding:10px 12px;">
          <div style="font-family:'Montserrat',sans-serif; font-size:8.5pt; font-weight:800; color:#fbbf24;">100% DYSLEXIA-FRIENDLY</div>
          <div style="font-size:7.5pt; color:rgba(255,255,255,0.8); margin-top:2px;">
            Printed on soft cream canvas with Atkinson Hyperlegible and Lexend fonts, ragged-right alignment, and high-contrast color cards.
          </div>
        </div>
        <div style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.15); border-radius:6px; padding:10px 12px;">
          <div style="font-family:'Montserrat',sans-serif; font-size:8.5pt; font-weight:800; color:#fbbf24;">AUTHENTIC WORKPLACE TASKS</div>
          <div style="font-size:7.5pt; color:rgba(255,255,255,0.8); margin-top:2px;">
            Real-world scenarios from the NHS, engineering, logistics, local government, construction, and corporate business administration.
          </div>
        </div>
        <div style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.15); border-radius:6px; padding:10px 12px;">
          <div style="font-family:'Montserrat',sans-serif; font-size:8.5pt; font-weight:800; color:#fbbf24;">OFFICIAL EXAM ALIGNMENT</div>
          <div style="font-size:7.5pt; color:rgba(255,255,255,0.8); margin-top:2px;">
            Strictly mapped to Pearson Edexcel, City &amp; Guilds, Highfield, and NCFE writing standards with comprehensive explanatory answer keys.
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Bottom Bar with ISBN & Publisher -->
  <div style="padding:14mm 18mm 16mm 18mm; background:rgba(0,0,0,0.4); border-top:1px solid rgba(255,255,255,0.15); display:flex; justify-content:space-between; align-items:center;">
    <div>
      <div style="font-size:7.5pt; color:rgba(255,255,255,0.85); font-weight:700;">
        Master Functional Skills Publishing &bull; London, UK
      </div>
      <div style="font-size:7pt; color:rgba(255,255,255,0.6); margin-top:2px;">
        ISBN 978-1-916892-44-6 &bull; Publication Code: MFS-SPAG-L2-84P-2026
      </div>
    </div>
    <div style="text-align:right;">
      <div style="background:#ffffff; color:#0f172a; padding:6px 12px; border-radius:4px; font-family:'Montserrat',sans-serif; font-size:7.5pt; font-weight:800; display:inline-block;">
        masterfunctionalskills.co.uk
      </div>
    </div>
  </div>
</div>
"""

# =============================================================================
# MASTER COMPILER FUNCTION
# =============================================================================

def build_pdf():
    print("=" * 80)
    print("BUILDING 84-PAGE FUNCTIONAL SKILLS LEVEL 2 SPAG MASTERY PUBLICATION")
    print("=" * 80)
    start_time = time.time()

    pages_html = []

    # 1. Page 1: Front Cover
    print("[1/84] Generating Page 1: Full-Bleed Front Cover...")
    pages_html.append(render_page_1())

    # 2. Page 2: Inside Cover
    print("[2/84] Generating Page 2: Inside Cover & Dyslexia Statement...")
    pages_html.append(render_page_2())

    # 3. Pages 3–6: 40-Question Diagnostic Assessment (4 pages)
    print("[3-6/84] Generating Pages 3–6: 40-Question Baseline Diagnostic Assessment...")
    all_diag = dv.DIAGNOSTIC_QUESTIONS
    pages_html.append(render_diagnostic_page(1, all_diag[0:10], 3))
    pages_html.append(render_diagnostic_page(2, all_diag[10:20], 4))
    pages_html.append(render_diagnostic_page(3, all_diag[20:30], 5))
    pages_html.append(render_diagnostic_page(4, all_diag[30:40], 6))

    # 4. Pages 7–58: 26 Units × 2 pages = 52 pages
    all_units = u_part1.UNITS_1_TO_13 + u_part2.UNITS_14_TO_26
    current_page = 7
    print(f"[7-58/84] Generating Pages 7–58: 26 Two-Page Murphy Units (52 pages total)...")
    for u in all_units:
        # Left page: Theory & Formulas
        pages_html.append(render_unit_left(u, current_page))
        current_page += 1
        # Right page: Practice Drills
        pages_html.append(render_unit_right(u, current_page))
        current_page += 1

    # 5. Pages 59–64: 6 Vocabulary Modules (6 pages)
    print("[59-64/84] Generating Pages 59–64: 6 Vocabulary in Use Master Modules...")
    for mod in dv.VOCABULARY_MODULES:
        pages_html.append(render_vocab_module(mod, current_page))
        current_page += 1

    # 6. Pages 65–70: 6 Mixed Workouts (6 pages)
    print("[65-70/84] Generating Pages 65–70: 6 Murphy-Style Mixed Additional Workouts...")
    for w in dv.MIXED_WORKOUTS:
        pages_html.append(render_workout_page(w, current_page))
        current_page += 1

    # 7. Pages 71–76: 6 Official Exam Mocks (6 pages)
    print("[71-76/84] Generating Pages 71–76: 6 Official Exam Proofreading & Extended Writing Mocks...")
    for mock in mk.EXAM_MOCKS:
        pages_html.append(render_mock_page(mock, current_page))
        current_page += 1

    # 8. Pages 77–82: 6 Explanatory Answer Key Pages (6 pages)
    print("[77-82/84] Generating Pages 77–82: Comprehensive Explanatory Answer Keys...")
    pages_html.append(render_answer_key_page_77())
    pages_html.append(render_answer_key_generic(78, "page_78"))
    pages_html.append(render_answer_key_generic(79, "page_79"))
    pages_html.append(render_answer_key_generic(80, "page_80"))
    pages_html.append(render_answer_key_generic(81, "page_81"))
    pages_html.append(render_answer_key_generic(82, "page_82"))

    # 9. Page 83: Candidate Self-Audit Checklist
    print("[83/84] Generating Page 83: Candidate Self-Audit Checklist & Progress Matrix...")
    pages_html.append(render_page_83(all_units))

    # 10. Page 84: High-Impact Back Cover
    print("[84/84] Generating Page 84: High-Impact Back Cover...")
    pages_html.append(render_page_84())

    total_pages_generated = len(pages_html)
    print(f"\nTotal HTML Pages Assembled: {total_pages_generated} (Target: Exactly 84)")
    if total_pages_generated != 84:
        raise ValueError(f"Page assembly error! Expected 84 pages, got {total_pages_generated}")

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Master Functional Skills • SPaG Level 2 Mastery (84 Pages)</title>
  {CUSTOM_CSS}
</head>
<body>
{''.join(pages_html)}
</body>
</html>
"""

    temp_html_path = os.path.join(SCRATCH_DIR, "MasterFunctionalSkills_SPaG_Level_2_Mastery_84p.html")
    with open(temp_html_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"HTML master document written to: {temp_html_path} ({os.path.getsize(temp_html_path)/1024:.1f} KB)")

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
        "--user-data-dir=/tmp/chr_spag_84p_build",
        "--no-pdf-header-footer",
        f"--print-to-pdf={out_pdf_downloads}",
        temp_html_path
    ]
    subprocess.run(chrome_cmd, check=True)

    # Replicate to Documents directory
    shutil.copy2(out_pdf_downloads, out_pdf_documents)

    # Clean up temp HTML
    if os.path.exists(temp_html_path):
        os.remove(temp_html_path)

    # Verify with pdfinfo
    res = subprocess.run(["pdfinfo", out_pdf_downloads], capture_output=True, text=True, check=True)
    actual_pages = None
    for line in res.stdout.splitlines():
        if "Pages:" in line:
            actual_pages = int(line.split(":")[1].strip())
            break

    file_size_mb = os.path.getsize(out_pdf_downloads) / (1024 * 1024)
    elapsed = time.time() - start_time

    print("\n" + "=" * 80)
    print(f"COMPILATION COMPLETE IN {elapsed:.2f}s!")
    print(f"Primary Target Output:    {out_pdf_downloads}")
    print(f"Secondary Target Output:  {out_pdf_documents}")
    print(f"Verified PDF Page Count:  {actual_pages} Pages (Target: 84 Pages)")
    print(f"Output File Size:         {file_size_mb:.2f} MB")
    print("=" * 80)

    if actual_pages != 84:
        raise ValueError(f"PDF verification failed! Expected 84 pages, got {actual_pages}")


if __name__ == "__main__":
    build_pdf()
