"""
spag_styles.py - Visual & Accessibility Design Tokens for Master Functional Skills SPaG Books
Strictly Dyslexia-Friendly Architecture:
- Canvas: Warm Cream (#FAF8F5 / #FDFBF7) across all interior reading pages.
- Text: Deep Slate (#1F2937) for WCAG AAA contrast without harsh glare.
- Typography: Lexend, Atkinson Hyperlegible, sans-serif.
- Leading: 1.48 - 1.52, letter-spacing 0.025em. Ragged right (NEVER justified).
"""

LEVEL_THEMES = {
    "L2": {
        "code": "L2",
        "title": "Level 2 Mastery",
        "full_name": "Functional Skills English Level 2",
        "subtitle": "Complete 100-Page SPaG Mastery & Proofreading Handbook",
        "page_count_label": "Complete 100-Page Curriculum Manual",
        "total_pages": 100,
        "primary": "#002046",
        "secondary": "#1e3a8a",
        "accent": "#2563eb",
        "tint": "#eff6ff",
        "border_color": "#bfdbfe",
        "badge_bg": "#2563eb",
        "badge_text": "#ffffff",
        "cover_grad_start": "#020f26",
        "cover_grad_mid": "#002046",
        "cover_grad_end": "#0f172a",
        "ofqual_code": "Level 2 Writing (FS-ENG-L2)",
        "file_stem": "MasterFunctionalSkills_SPaG_Level_2_Mastery",
    },
    "L1": {
        "code": "L1",
        "title": "Level 1 Mastery",
        "full_name": "Functional Skills English Level 1",
        "subtitle": "Complete 100-Page SPaG Foundations & Practical Writing Handbook",
        "page_count_label": "Complete 100-Page Curriculum Manual",
        "total_pages": 100,
        "primary": "#0c4e45",
        "secondary": "#0d9488",
        "accent": "#14b8a6",
        "tint": "#f0fdfa",
        "border_color": "#99f6e4",
        "badge_bg": "#0d9488",
        "badge_text": "#ffffff",
        "cover_grad_start": "#022420",
        "cover_grad_mid": "#0c4e45",
        "cover_grad_end": "#134e4a",
        "ofqual_code": "Level 1 Writing (FS-ENG-L1)",
        "file_stem": "MasterFunctionalSkills_SPaG_Level_1_Mastery",
    },
    "E3": {
        "code": "E3",
        "title": "Entry Level 3 Mastery",
        "full_name": "Functional Skills English Entry Level 3",
        "subtitle": "Complete 96-Page SPaG Core Foundations & Building Blocks Handbook",
        "page_count_label": "Complete 96-Page Curriculum Manual",
        "total_pages": 96,
        "primary": "#881337",
        "secondary": "#be123c",
        "accent": "#e11d48",
        "tint": "#fff1f2",
        "border_color": "#fecdd3",
        "badge_bg": "#be123c",
        "badge_text": "#ffffff",
        "cover_grad_start": "#3b0413",
        "cover_grad_mid": "#881337",
        "cover_grad_end": "#4c0519",
        "ofqual_code": "Entry Level 3 Writing (FS-ENG-E3)",
        "file_stem": "MasterFunctionalSkills_SPaG_Entry_Level_3_Mastery",
    }
}

SHARED_CSS = """
<style>
  @import url('https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Lexend:wght@400;500;600;700;800;900&family=Montserrat:wght@700;800;900&display=swap');

  @page {
    size: A4 portrait;
    margin: 0;
  }

  * {
    box-sizing: border-box;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }

  body {
    margin: 0;
    padding: 0;
    font-family: 'Lexend', 'Atkinson Hyperlegible', sans-serif;
    color: #1F2937;
    background: #ffffff;
    font-size: 8.4pt;
    line-height: 1.48;
    letter-spacing: 0.025em;
    text-align: left;
  }

  .page {
    width: 210mm;
    height: 297mm;
    max-height: 297mm;
    min-height: 297mm;
    page-break-after: always;
    break-after: page;
    position: relative;
    overflow: hidden;
    padding: 12mm 15mm 13mm 15mm;
    background: #FDFBF7;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
  }

  /* Full Bleed Covers */
  .cover-page {
    padding: 0 !important;
    background: #0f172a;
    color: #ffffff;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  /* Header & Footer */
  .unit-page-header {
    border-bottom: 2px solid var(--theme-primary, #002046);
    padding-bottom: 4px;
    margin-bottom: 8px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }
  .unit-page-header .brand-title {
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 8pt;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    color: var(--theme-primary, #002046);
  }
  .unit-page-header .strand-badge {
    font-size: 7.5pt;
    font-weight: 700;
    color: #475569;
    background: #f1f5f9;
    padding: 2px 7px;
    border-radius: 4px;
    border: 1px solid #cbd5e1;
  }

  .unit-main-heading {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 7px;
  }
  .unit-num-pill {
    background: var(--theme-primary, #002046);
    color: #ffffff;
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 8pt;
    padding: 3px 10px;
    border-radius: 12px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    white-space: nowrap;
  }
  .unit-title-text {
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 11.5pt;
    color: var(--theme-primary, #002046);
    line-height: 1.2;
    margin: 0;
  }

  .page-footer {
    position: absolute;
    bottom: 6.5mm;
    left: 15mm;
    right: 15mm;
    border-top: 1px solid #cbd5e1;
    padding-top: 4px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 7.3pt;
    color: #64748b;
  }
  .page-num {
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    color: var(--theme-primary, #002046);
    background: #e2e8f0;
    padding: 1px 7px;
    border-radius: 4px;
  }

  /* Chunked Dyslexia Left-Bordered Cards */
  .card-anchor {
    background: #F0F9FF;
    border: 1px solid #BAE6FD;
    border-left: 4.5px solid #0284C7;
    border-radius: 6px;
    padding: 7px 10px;
    margin-bottom: 7px;
  }
  .card-anchor .card-title {
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 8pt;
    color: #0369a1;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 3px;
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .card-formula {
    background: #ffffff;
    border: 1px solid #E2E8F0;
    border-left: 4.5px solid var(--theme-secondary, #1e3a8a);
    border-radius: 6px;
    padding: 7px 10px;
    margin-bottom: 7px;
  }
  .card-formula .card-title {
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 8pt;
    color: var(--theme-secondary, #1e3a8a);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 4px;
  }

  .formula-strip {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    gap: 6px;
    margin: 5px 0;
    background: #f8fafc;
    padding: 6px 8px;
    border-radius: 5px;
    border: 1px dashed #cbd5e1;
  }
  .fpill {
    font-size: 7.8pt;
    font-weight: 700;
    padding: 2px 7px;
    border-radius: 4px;
    display: inline-block;
  }
  .fpill-subj { background: #dbeafe; color: #1e40af; border: 1px solid #bfdbfe; }
  .fpill-verb { background: #dcfce7; color: #166534; border: 1px solid #bbf7d0; }
  .fpill-punct { background: #fef08a; color: #854d0e; border: 1px solid #fde047; font-weight: 800; }
  .fpill-conn { background: #f3e8ff; color: #6b21a8; border: 1px solid #e9d5ff; }
  .fpill-clause { background: #ffedd5; color: #9a3412; border: 1px solid #fed7aa; }

  /* Compare & Contrast Box */
  .card-compare {
    background: #ffffff;
    border: 1px solid #E2E8F0;
    border-radius: 6px;
    overflow: hidden;
    margin-bottom: 7px;
  }
  .compare-row-bad {
    background: #FEF2F2;
    border-left: 4.5px solid #DC2626;
    padding: 6px 10px;
    border-bottom: 1px solid #FEE2E2;
  }
  .compare-row-good {
    background: #F0FDF4;
    border-left: 4.5px solid #16A34A;
    padding: 6px 10px;
    border-bottom: 1px solid #DCFCE7;
  }
  .compare-row-why {
    background: #FFFBEB;
    border-left: 4.5px solid #D97706;
    padding: 6px 10px;
    font-size: 8pt;
    color: #92400e;
  }
  .compare-badge {
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 7.3pt;
    padding: 1px 6px;
    border-radius: 3px;
    display: inline-block;
    margin-right: 5px;
    text-transform: uppercase;
  }
  .badge-bad { background: #fee2e2; color: #991b1b; }
  .badge-good { background: #dcfce7; color: #166534; }
  .badge-why { background: #fef3c7; color: #92400e; }

  /* Golden Rule Card */
  .card-golden {
    background: #FEFCE8;
    border: 1px solid #FEF08A;
    border-left: 4.5px solid #D97706;
    border-radius: 6px;
    padding: 7px 10px;
    margin-top: auto;
  }
  .card-golden .card-title {
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 8pt;
    color: #b45309;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 2px;
    display: flex;
    align-items: center;
    gap: 6px;
  }

  /* Right-Hand Exercises Layout */
  .exercise-section {
    margin-bottom: 8px;
  }
  .ex-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #f8fafc;
    border-left: 3.5px solid var(--theme-secondary, #1e3a8a);
    padding: 3px 8px;
    border-radius: 3px;
    margin-bottom: 5px;
  }
  .ex-title {
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 8pt;
    color: var(--theme-primary, #002046);
    text-transform: uppercase;
    letter-spacing: 0.3px;
  }
  .ex-marks {
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    font-size: 7.3pt;
    color: #475569;
  }

  /* Graded Exercise Blocks */
  .q-item {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 5px;
    padding: 5px 8px;
    margin-bottom: 5px;
    font-size: 8.2pt;
  }
  .q-prompt {
    font-weight: 600;
    margin-bottom: 3px;
    color: #1e293b;
  }
  .q-options {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    font-size: 8pt;
  }
  .opt-box {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    padding: 2px 7px;
    border-radius: 4px;
    cursor: default;
  }
  .opt-tick {
    width: 12px;
    height: 12px;
    border: 1.5px solid #94a3b8;
    border-radius: 2px;
    display: inline-block;
  }

  /* Exercise 3: Forensic Workplace Document Container */
  .workplace-doc {
    background: #ffffff;
    border: 1.5px solid #cbd5e1;
    border-radius: 6px;
    overflow: hidden;
    margin-bottom: 5px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
  }
  .doc-topbar {
    background: #f1f5f9;
    border-bottom: 1px solid #cbd5e1;
    padding: 4px 8px;
    font-size: 7.4pt;
    color: #475569;
    display: flex;
    justify-content: space-between;
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
  }
  .doc-meta {
    padding: 4px 8px;
    background: #f8fafc;
    border-bottom: 1px dashed #e2e8f0;
    font-size: 7.5pt;
    line-height: 1.35;
  }
  .doc-body {
    padding: 7px 10px;
    font-size: 8.1pt;
    line-height: 1.45;
    background: #ffffff;
  }
  .error-count-banner {
    background: #fff7ed;
    border: 1px solid #fed7aa;
    color: #9a3412;
    padding: 3px 8px;
    font-size: 7.4pt;
    font-weight: 700;
    border-radius: 4px;
    margin-bottom: 4px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  /* Exercise 4: Applied Functional Writing Box */
  .applied-task-box {
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    padding: 6px 9px;
  }
  .task-prompt {
    font-size: 8pt;
    font-weight: 600;
    color: #1e293b;
    margin-bottom: 4px;
  }
  .task-criteria {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 4px 7px;
    font-size: 7.4pt;
    color: #475569;
    margin-bottom: 5px;
  }
  .task-lines {
    background: repeating-linear-gradient(
      transparent,
      transparent 18px,
      #e2e8f0 19px,
      #e2e8f0 20px
    );
    height: 60px;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
  }

  /* Tables for Diagnostics, Audits, Mocks */
  table.mfs-table {
    width: 100%;
    border-collapse: collapse;
    margin: 6px 0;
    font-size: 8pt;
  }
  table.mfs-table th, table.mfs-table td {
    padding: 5px 7px;
    border: 1px solid #cbd5e1;
    text-align: left;
    vertical-align: top;
  }
  table.mfs-table th {
    background: var(--theme-primary, #002046);
    color: #ffffff;
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    font-size: 7.5pt;
    text-transform: uppercase;
  }
  table.mfs-table tr:nth-child(even) {
    background: #f8fafc;
  }

  .rag-pill {
    display: inline-block;
    width: 14px;
    height: 14px;
    border-radius: 3px;
    border: 1px solid #cbd5e1;
    margin-right: 2px;
  }
  .rag-red { background: #fecaca; }
  .rag-amber { background: #fef08a; }
  .rag-green { background: #bbf7d0; }

  /* Two Column Layout */
  .grid-2col {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-bottom: 6px;
  }
</style>
"""
