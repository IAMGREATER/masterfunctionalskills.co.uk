"""
curriculum_visual_engine.py
=============================================================================
Central engine providing 100% valid XML SVG diagrams and wireframes for all
Master Functional Skills curriculum topics across Mathematics, English Writing,
Digital Skills, and BKSB Diagnostic Remediation.

Features:
- Pure UTF-8 encoding (no undeclared HTML entities like &bull; or &divide;)
- High-contrast, dyslexia-friendly palette matching Pearson Edexcel standards
- Scalable vector rendering with responsive viewBox
=============================================================================
"""

import xml.etree.ElementTree as ET

def get_grid_method_svg():
    return """<svg viewBox="0 0 540 260" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:540px; height:auto; font-family:'Plus Jakarta Sans', sans-serif;">
  <rect x="2" y="2" width="536" height="256" rx="12" fill="#ffffff" stroke="#bae6fd" stroke-width="2"/>
  <rect x="18" y="14" width="250" height="26" rx="6" fill="#e0f2fe"/>
  <text x="28" y="32" font-size="12" font-weight="800" fill="#0369a1">&#9998; WORKED METHOD: GRID MULTIPLICATION</text>
  <text x="285" y="32" font-size="13" font-weight="700" fill="#0f172a">Calculating 46 &#215; 35</text>

  <!-- Header Row -->
  <rect x="25" y="52" width="60" height="42" rx="6" fill="#0284c7"/>
  <text x="55" y="79" font-size="20" font-weight="800" fill="#ffffff" text-anchor="middle">&#215;</text>
  <rect x="95" y="52" width="145" height="42" rx="6" fill="#0284c7"/>
  <text x="167" y="72" font-size="11" font-weight="700" fill="#bae6fd" text-anchor="middle">TENS</text>
  <text x="167" y="88" font-size="16" font-weight="800" fill="#ffffff" text-anchor="middle">40</text>
  <rect x="250" y="52" width="110" height="42" rx="6" fill="#0284c7"/>
  <text x="305" y="72" font-size="11" font-weight="700" fill="#bae6fd" text-anchor="middle">UNITS</text>
  <text x="305" y="88" font-size="16" font-weight="800" fill="#ffffff" text-anchor="middle">6</text>
  <rect x="370" y="52" width="145" height="42" rx="6" fill="#0369a1"/>
  <text x="442" y="78" font-size="13" font-weight="800" fill="#ffffff" text-anchor="middle">ROW SUBTOTAL</text>

  <!-- Row 1: 30 -->
  <rect x="25" y="104" width="60" height="52" rx="6" fill="#f0f9ff" stroke="#bae6fd" stroke-width="1.5"/>
  <text x="55" y="128" font-size="10" font-weight="700" fill="#0284c7" text-anchor="middle">TENS</text>
  <text x="55" y="146" font-size="17" font-weight="800" fill="#0c4a6e" text-anchor="middle">30</text>
  <rect x="95" y="104" width="145" height="52" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="167" y="126" font-size="11" fill="#64748b" text-anchor="middle">30 &#215; 40 =</text>
  <text x="167" y="147" font-size="18" font-weight="800" fill="#0284c7" text-anchor="middle">1,200</text>
  <rect x="250" y="104" width="110" height="52" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="305" y="126" font-size="11" fill="#64748b" text-anchor="middle">30 &#215; 6 =</text>
  <text x="305" y="147" font-size="18" font-weight="800" fill="#0284c7" text-anchor="middle">180</text>
  <rect x="370" y="104" width="145" height="52" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="442" y="126" font-size="11" fill="#475569" text-anchor="middle">1,200 + 180 =</text>
  <text x="442" y="147" font-size="18" font-weight="800" fill="#0f172a" text-anchor="middle">1,380</text>

  <!-- Row 2: 5 -->
  <rect x="25" y="164" width="60" height="52" rx="6" fill="#f0f9ff" stroke="#bae6fd" stroke-width="1.5"/>
  <text x="55" y="188" font-size="10" font-weight="700" fill="#0284c7" text-anchor="middle">UNITS</text>
  <text x="55" y="206" font-size="17" font-weight="800" fill="#0c4a6e" text-anchor="middle">5</text>
  <rect x="95" y="164" width="145" height="52" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="167" y="186" font-size="11" fill="#64748b" text-anchor="middle">5 &#215; 40 =</text>
  <text x="167" y="207" font-size="18" font-weight="800" fill="#0284c7" text-anchor="middle">200</text>
  <rect x="250" y="164" width="110" height="52" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="305" y="186" font-size="11" fill="#64748b" text-anchor="middle">5 &#215; 6 =</text>
  <text x="305" y="207" font-size="18" font-weight="800" fill="#0284c7" text-anchor="middle">30</text>
  <rect x="370" y="164" width="145" height="52" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="442" y="186" font-size="11" fill="#475569" text-anchor="middle">200 + 30 =</text>
  <text x="442" y="207" font-size="18" font-weight="800" fill="#0f172a" text-anchor="middle">230</text>

  <!-- Final Footer -->
  <rect x="25" y="222" width="490" height="28" rx="6" fill="#dcfce7" stroke="#86efac" stroke-width="1.5"/>
  <text x="140" y="241" font-size="12" font-weight="700" fill="#166534">GRAND TOTAL: 1,380 + 230</text>
  <text x="442" y="242" font-size="15" font-weight="800" fill="#15803d" text-anchor="middle">= 1,610 &#10003;</text>
</svg>"""

def get_two_way_table_svg():
    return """<svg viewBox="0 0 540 260" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:540px; height:auto; font-family:'Plus Jakarta Sans', sans-serif;">
  <rect x="2" y="2" width="536" height="256" rx="12" fill="#ffffff" stroke="#bae6fd" stroke-width="2"/>
  <rect x="18" y="14" width="280" height="26" rx="6" fill="#e0f2fe"/>
  <text x="28" y="32" font-size="12" font-weight="800" fill="#0369a1">&#9998; STATISTICAL MODEL: TWO-WAY TABLE</text>
  <text x="315" y="32" font-size="12" font-weight="700" fill="#0f172a">Clinic Vaccination Status (N = 120)</text>

  <!-- Table Header -->
  <rect x="25" y="52" width="130" height="34" rx="4" fill="#0284c7"/>
  <text x="90" y="74" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">CATEGORY</text>
  <rect x="160" y="52" width="115" height="34" rx="4" fill="#0284c7"/>
  <text x="217" y="74" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">VACCINATED</text>
  <rect x="280" y="52" width="115" height="34" rx="4" fill="#0284c7"/>
  <text x="337" y="74" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">UNVACCINATED</text>
  <rect x="400" y="52" width="115" height="34" rx="4" fill="#0369a1"/>
  <text x="457" y="74" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">ROW TOTAL</text>

  <!-- Female Row -->
  <rect x="25" y="92" width="130" height="36" fill="#f8fafc" stroke="#e2e8f0"/>
  <text x="35" y="115" font-size="12" font-weight="700" fill="#0f172a">Female</text>
  <rect x="160" y="92" width="115" height="36" fill="#ffffff" stroke="#e2e8f0"/>
  <text x="217" y="115" font-size="14" font-weight="800" fill="#0284c7" text-anchor="middle">45</text>
  <rect x="280" y="92" width="115" height="36" fill="#fffbeb" stroke="#fde68a"/>
  <text x="337" y="115" font-size="14" font-weight="800" fill="#b45309" text-anchor="middle">25</text>
  <rect x="400" y="92" width="115" height="36" fill="#f1f5f9" stroke="#cbd5e1"/>
  <text x="457" y="115" font-size="14" font-weight="800" fill="#0f172a" text-anchor="middle">70</text>

  <!-- Male Row -->
  <rect x="25" y="132" width="130" height="36" fill="#f8fafc" stroke="#e2e8f0"/>
  <text x="35" y="155" font-size="12" font-weight="700" fill="#0f172a">Male</text>
  <rect x="160" y="132" width="115" height="36" fill="#ffffff" stroke="#e2e8f0"/>
  <text x="217" y="155" font-size="14" font-weight="800" fill="#0284c7" text-anchor="middle">25</text>
  <rect x="280" y="132" width="115" height="36" fill="#fffbeb" stroke="#fde68a"/>
  <text x="337" y="155" font-size="14" font-weight="800" fill="#b45309" text-anchor="middle">25</text>
  <rect x="400" y="132" width="115" height="36" fill="#f1f5f9" stroke="#cbd5e1"/>
  <text x="457" y="155" font-size="14" font-weight="800" fill="#0f172a" text-anchor="middle">50</text>

  <!-- Column Total Row -->
  <rect x="25" y="172" width="130" height="38" rx="0 0 0 6" fill="#0369a1"/>
  <text x="35" y="196" font-size="11" font-weight="800" fill="#ffffff">COLUMN TOTAL</text>
  <rect x="160" y="172" width="115" height="38" fill="#f1f5f9" stroke="#cbd5e1"/>
  <text x="217" y="196" font-size="15" font-weight="900" fill="#0369a1" text-anchor="middle">70</text>
  <rect x="280" y="172" width="115" height="38" fill="#f1f5f9" stroke="#cbd5e1"/>
  <text x="337" y="196" font-size="15" font-weight="900" fill="#0369a1" text-anchor="middle">50</text>
  <rect x="400" y="172" width="115" height="38" rx="0 0 6 0" fill="#dcfce7" stroke="#86efac" stroke-width="2"/>
  <text x="457" y="196" font-size="16" font-weight="900" fill="#15803d" text-anchor="middle">120 &#10003;</text>

  <!-- Verification Note -->
  <text x="25" y="235" font-size="10" font-weight="700" fill="#475569">Verification Rule: Row Sum (70 + 50 = 120) strictly equals Column Sum (70 + 50 = 120).</text>
</svg>"""

def get_grouped_frequency_svg():
    return """<svg viewBox="0 0 540 260" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:540px; height:auto; font-family:'Plus Jakarta Sans', sans-serif;">
  <rect x="2" y="2" width="536" height="256" rx="12" fill="#ffffff" stroke="#bae6fd" stroke-width="2"/>
  <rect x="18" y="14" width="310" height="26" rx="6" fill="#e0f2fe"/>
  <text x="28" y="32" font-size="12" font-weight="800" fill="#0369a1">&#9998; ESTIMATED MEAN: GROUPED FREQUENCY</text>

  <!-- Table Header -->
  <rect x="25" y="52" width="125" height="32" rx="4" fill="#0f766e"/>
  <text x="87" y="72" font-size="10" font-weight="800" fill="#ffffff" text-anchor="middle">TIME INTERVAL (t)</text>
  <rect x="155" y="52" width="90" height="32" rx="4" fill="#0f766e"/>
  <text x="200" y="72" font-size="10" font-weight="800" fill="#ffffff" text-anchor="middle">FREQ (f)</text>
  <rect x="250" y="52" width="110" height="32" rx="4" fill="#0f766e"/>
  <text x="305" y="72" font-size="10" font-weight="800" fill="#ffffff" text-anchor="middle">MIDPOINT (m)</text>
  <rect x="365" y="52" width="150" height="32" rx="4" fill="#115e59"/>
  <text x="440" y="72" font-size="10" font-weight="800" fill="#ffffff" text-anchor="middle">PRODUCT (f &#215; m)</text>

  <!-- Rows -->
  <rect x="25" y="88" width="125" height="30" fill="#f8fafc" stroke="#e2e8f0"/>
  <text x="87" y="108" font-size="11" fill="#0f172a" text-anchor="middle">0 &lt; t &#8804; 10</text>
  <rect x="155" y="88" width="90" height="30" fill="#ffffff" stroke="#e2e8f0"/>
  <text x="200" y="108" font-size="12" font-weight="700" fill="#0f172a" text-anchor="middle">4</text>
  <rect x="250" y="88" width="110" height="30" fill="#f0fdfa" stroke="#ccfbf1"/>
  <text x="305" y="108" font-size="12" font-weight="800" fill="#0d9488" text-anchor="middle">5</text>
  <rect x="365" y="88" width="150" height="30" fill="#ffffff" stroke="#e2e8f0"/>
  <text x="440" y="108" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">4 &#215; 5 = 20</text>

  <rect x="25" y="122" width="125" height="30" fill="#f8fafc" stroke="#e2e8f0"/>
  <text x="87" y="142" font-size="11" fill="#0f172a" text-anchor="middle">10 &lt; t &#8804; 20</text>
  <rect x="155" y="122" width="90" height="30" fill="#ffffff" stroke="#e2e8f0"/>
  <text x="200" y="142" font-size="12" font-weight="700" fill="#0f172a" text-anchor="middle">12</text>
  <rect x="250" y="122" width="110" height="30" fill="#f0fdfa" stroke="#ccfbf1"/>
  <text x="305" y="142" font-size="12" font-weight="800" fill="#0d9488" text-anchor="middle">15</text>
  <rect x="365" y="122" width="150" height="30" fill="#ffffff" stroke="#e2e8f0"/>
  <text x="440" y="142" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">12 &#215; 15 = 180</text>

  <rect x="25" y="156" width="125" height="30" fill="#f8fafc" stroke="#e2e8f0"/>
  <text x="87" y="176" font-size="11" fill="#0f172a" text-anchor="middle">20 &lt; t &#8804; 30</text>
  <rect x="155" y="156" width="90" height="30" fill="#ffffff" stroke="#e2e8f0"/>
  <text x="200" y="176" font-size="12" font-weight="700" fill="#0f172a" text-anchor="middle">8</text>
  <rect x="250" y="156" width="110" height="30" fill="#f0fdfa" stroke="#ccfbf1"/>
  <text x="305" y="176" font-size="12" font-weight="800" fill="#0d9488" text-anchor="middle">25</text>
  <rect x="365" y="156" width="150" height="30" fill="#ffffff" stroke="#e2e8f0"/>
  <text x="440" y="176" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">8 &#215; 25 = 200</text>

  <!-- Summary Box -->
  <rect x="25" y="196" width="490" height="48" rx="6" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>
  <text x="35" y="215" font-size="10.5" font-weight="700" fill="#166534">Total Frequency (&#931;f) = 24  &#8226;  Total Product (&#931;fm) = 20 + 180 + 200 = 400</text>
  <text x="35" y="233" font-size="11.5" font-weight="900" fill="#15803d">Estimated Mean = &#931;fm &#247; &#931;f = 400 &#247; 24 = 16.67 minutes &#10003;</text>
</svg>"""

def get_reverse_percentage_trap_svg():
    return """<svg viewBox="0 0 540 260" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:540px; height:auto; font-family:'Plus Jakarta Sans', sans-serif;">
  <rect x="2" y="2" width="536" height="256" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
  <rect x="14" y="12" width="512" height="30" rx="6" fill="#1d4ed8"/>
  <text x="24" y="32" font-size="12" font-weight="900" fill="#ffffff">DIAGNOSTIC TRAP AUTOPSY: REVERSE PERCENTAGES</text>

  <!-- Left: The Fatal Failure Trap -->
  <rect x="16" y="50" width="246" height="155" rx="8" fill="#fff1f2" stroke="#fca5a5" stroke-width="2"/>
  <rect x="26" y="58" width="226" height="24" rx="4" fill="#fee2e2"/>
  <text x="34" y="74" font-size="10" font-weight="900" fill="#991b1b">&#10005; FATAL TRAP (Adding % back)</text>
  <text x="26" y="100" font-size="9.5" fill="#881337">Sale price = &#163;120 after 20% discount.</text>
  <text x="26" y="118" font-size="9.5" fill="#881337">Candidate mistake: 20% of &#163;120 = &#163;24</text>
  <text x="26" y="136" font-size="10" font-weight="800" fill="#b91c1c">&#163;120 + &#163;24 = &#163;144.00 (WRONG!)</text>
  <rect x="24" y="148" width="230" height="46" rx="4" fill="#fee2e2"/>
  <text x="30" y="164" font-size="8.5" font-weight="800" fill="#991b1b">FATAL FLAW: The 20% discount was</text>
  <text x="30" y="178" font-size="8.5" font-weight="800" fill="#991b1b">subtracted from a LARGER original sum!</text>

  <!-- Right: The Golden Multiplier Rule -->
  <rect x="278" y="50" width="246" height="155" rx="8" fill="#f0fdf4" stroke="#86efac" stroke-width="2"/>
  <rect x="288" y="58" width="226" height="24" rx="4" fill="#dcfce7"/>
  <text x="296" y="74" font-size="10" font-weight="900" fill="#166534">&#10003; GOLDEN METHOD (Divide Multiplier)</text>
  <text x="288" y="100" font-size="9.5" fill="#14532d">&#163;120 represents 80% (100% - 20%).</text>
  <text x="288" y="118" font-size="9.5" fill="#14532d">Multiplier = 1.00 - 0.20 = 0.80</text>
  <text x="288" y="136" font-size="11.5" font-weight="900" fill="#15803d">&#163;120 &#247; 0.80 = &#163;150.00 &#10003;</text>
  <rect x="286" y="148" width="230" height="46" rx="4" fill="#dcfce7"/>
  <text x="294" y="164" font-size="8.5" font-weight="800" fill="#166534">VERIFICATION CHECK:</text>
  <text x="294" y="178" font-size="8.5" fill="#15803d">20% of &#163;150 = &#163;30. &#163;150 - &#163;30 = &#163;120 &#10003;</text>

  <!-- Footer Banner -->
  <rect x="14" y="214" width="512" height="34" rx="6" fill="#eff6ff" stroke="#bfdbfe"/>
  <text x="24" y="235" font-size="10" font-weight="800" fill="#1d4ed8">Examiner Golden Peg: Original Value = Final Value &#247; Decimal Multiplier</text>
</svg>"""

def get_file_tree_svg():
    return """<svg viewBox="0 0 520 260" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:520px; height:auto; font-family:'Plus Jakarta Sans', sans-serif;">
  <rect x="2" y="2" width="516" height="256" rx="10" fill="#090d16" stroke="#00e5ff" stroke-width="2"/>
  <rect x="12" y="12" width="496" height="30" rx="5" fill="#1e293b"/>
  <text x="24" y="32" font-size="11" font-weight="800" fill="#00e5ff">&#128193; OS DIRECTORY HIERARCHY &amp; CLOUD STORAGE PATH</text>

  <!-- Root Directory -->
  <rect x="24" y="52" width="160" height="28" rx="4" fill="#0284c7"/>
  <text x="34" y="70" font-size="10" font-weight="800" fill="#ffffff">&#128190; C:\\ (System Drive Root)</text>

  <!-- Branch lines -->
  <line x1="45" y1="80" x2="45" y2="230" stroke="#475569" stroke-width="2"/>
  
  <line x1="45" y1="105" x2="70" y2="105" stroke="#475569" stroke-width="2"/>
  <rect x="70" y="90" width="180" height="28" rx="4" fill="#1e293b" stroke="#38bdf8"/>
  <text x="80" y="108" font-size="10" font-weight="700" fill="#38bdf8">&#128193; Users\\Apprentice\\</text>

  <line x1="45" y1="145" x2="70" y2="145" stroke="#475569" stroke-width="2"/>
  <rect x="70" y="130" width="220" height="28" rx="4" fill="#1e293b" stroke="#38bdf8"/>
  <text x="80" y="148" font-size="10" font-weight="700" fill="#38bdf8">&#9729; OneDrive - NHS Trust\\</text>

  <!-- Sub-branch -->
  <line x1="120" y1="158" x2="120" y2="220" stroke="#475569" stroke-width="2"/>
  <line x1="120" y1="180" x2="140" y2="180" stroke="#475569" stroke-width="2"/>
  <rect x="140" y="168" width="180" height="24" rx="4" fill="#0f172a" stroke="#00e5ff"/>
  <text x="150" y="184" font-size="9.5" fill="#ffffff">&#128193; Functional_Skills\\</text>

  <line x1="120" y1="210" x2="140" y2="210" stroke="#475569" stroke-width="2"/>
  <rect x="140" y="198" width="260" height="24" rx="4" fill="#052e16" stroke="#4ade80"/>
  <text x="150" y="214" font-size="9.5" font-weight="700" fill="#4ade80">&#128196; Level_2_Spreadsheet_Task.xlsx</text>

  <!-- Rule Callout on Right -->
  <rect x="330" y="52" width="170" height="100" rx="6" fill="#1e293b" stroke="#475569"/>
  <text x="340" y="72" font-size="9.5" font-weight="800" fill="#fde047">PATH SYNTAX RULE:</text>
  <text x="340" y="90" font-size="8.5" fill="#94a3b8">Drive:\\Folder\\Subfolder\\File.ext</text>
  <text x="340" y="112" font-size="8.5" fill="#38bdf8">&#8226; Avoid special characters</text>
  <text x="340" y="128" font-size="8.5" fill="#38bdf8">&#8226; Use sensible version tags</text>
</svg>"""

def get_review_wireframe_svg():
    return """<svg viewBox="0 0 460 270" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:460px; height:auto; font-family:'Plus Jakarta Sans', sans-serif;">
  <rect x="2" y="2" width="456" height="266" rx="10" fill="#ffffff" stroke="#94a3b8" stroke-width="2"/>
  <!-- Header -->
  <rect x="14" y="12" width="432" height="34" rx="5" fill="#0f172a"/>
  <text x="24" y="32" font-size="11" font-weight="900" fill="#f59e0b">FORMAT 8: WORKPLACE &amp; SERVICE REVIEW</text>
  <text x="340" y="32" font-size="11" fill="#fde047">&#9733;&#9733;&#9733;&#9733;&#9734; (4/5)</text>

  <!-- Review Title & Author Line -->
  <text x="18" y="64" font-size="12" font-weight="900" fill="#0f172a">"Exceptional Patient Care, But Urgent Parking Upgrades Needed"</text>
  <text x="18" y="78" font-size="8.5" fill="#64748b">Reviewed by: Senior Healthcare Apprentice &#8226; Date: October 2026</text>

  <!-- Side-by-Side Evaluation: Strengths vs Areas for Improvement -->
  <rect x="16" y="90" width="205" height="100" rx="5" fill="#f0fdf4" stroke="#86efac"/>
  <text x="24" y="106" font-size="9.5" font-weight="800" fill="#166534">&#10003; POSITIVE STRENGTHS</text>
  <text x="24" y="122" font-size="8.5" fill="#14532d">&#8226; Compassionate, attentive staff</text>
  <text x="24" y="138" font-size="8.5" fill="#14532d">&#8226; Rapid 15-minute triage</text>
  <text x="24" y="154" font-size="8.5" fill="#14532d">&#8226; Clean, hygienic wards</text>

  <rect x="238" y="90" width="205" height="100" rx="5" fill="#fff1f2" stroke="#fca5a5"/>
  <text x="246" y="106" font-size="9.5" font-weight="800" fill="#991b1b">&#10005; AREAS FOR IMPROVEMENT</text>
  <text x="246" y="122" font-size="8.5" fill="#881337">&#8226; Visitor parking charges excessive</text>
  <text x="246" y="138" font-size="8.5" fill="#881337">&#8226; Inadequate wayfinding signs</text>
  <text x="246" y="154" font-size="8.5" fill="#881337">&#8226; Outdated cafe payment card reader</text>

  <!-- Final Verdict Callout -->
  <rect x="16" y="200" width="428" height="54" rx="5" fill="#eff6ff" stroke="#bfdbfe"/>
  <text x="24" y="218" font-size="9.5" font-weight="800" fill="#1d4ed8">BALANCED VERDICT &amp; RECOMMENDATION:</text>
  <text x="24" y="234" font-size="8.5" fill="#1e40af">"I highly recommend the clinical services, but hospital management must review site facilities."</text>
</svg>"""


def get_article_wireframe_svg():
    return """<svg viewBox="0 0 460 270" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:460px; height:auto; font-family:'Plus Jakarta Sans', sans-serif;">
  <rect x="2" y="2" width="456" height="266" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
  
  <!-- Magazine Banner -->
  <rect x="16" y="12" width="428" height="42" rx="6" fill="#003366"/>
  <text x="28" y="28" font-size="10" font-weight="800" fill="#38bdf8">CAREERS &amp; COMMUNITY FOCUS • LEVEL 2 MAGAZINE SPREAD</text>
  <text x="28" y="46" font-size="13.5" font-weight="900" fill="#ffffff">Why NHS Healthcare Apprenticeships Are Transforming Care</text>
  
  <!-- Byline -->
  <text x="18" y="68" font-size="9" font-weight="700" fill="#64748b">By Sarah Jenkins • Published 12 October 2026 • 4 min read</text>
  
  <!-- 2 Columns Layout (Spacious) -->
  <rect x="16" y="78" width="206" height="174" rx="6" fill="#f8fafc" stroke="#e2e8f0"/>
  <text x="26" y="96" font-size="10.5" font-weight="900" fill="#003366">1. Real Ward Experience</text>
  <rect x="26" y="104" width="186" height="7" rx="2" fill="#cbd5e1"/>
  <rect x="26" y="116" width="176" height="7" rx="2" fill="#cbd5e1"/>
  <rect x="26" y="128" width="180" height="7" rx="2" fill="#cbd5e1"/>
  
  <!-- Pull Quote Box -->
  <rect x="26" y="142" width="186" height="52" rx="5" fill="#eff6ff" stroke="#bfdbfe"/>
  <text x="34" y="160" font-size="9" font-style="italic" font-weight="700" fill="#1e40af">"Earning while learning gave me the"</text>
  <text x="34" y="173" font-size="9" font-style="italic" font-weight="700" fill="#1e40af">"confidence to step into a band 3 role."</text>
  <text x="34" y="186" font-size="8.5" font-weight="800" fill="#2563eb">— Marcus, Clinical Apprentice</text>
  
  <rect x="26" y="202" width="186" height="7" rx="2" fill="#cbd5e1"/>
  <rect x="26" y="214" width="165" height="7" rx="2" fill="#cbd5e1"/>
  <rect x="26" y="226" width="175" height="7" rx="2" fill="#cbd5e1"/>
  
  <!-- Column 2 (Right) -->
  <rect x="238" y="78" width="206" height="174" rx="6" fill="#f8fafc" stroke="#e2e8f0"/>
  <rect x="248" y="86" width="186" height="68" rx="5" fill="#e2e8f0" stroke="#cbd5e1"/>
  <text x="341" y="124" font-size="9.5" font-weight="800" fill="#64748b" text-anchor="middle">📷 [Vocational Healthcare Photo]</text>
  
  <text x="248" y="172" font-size="10.5" font-weight="900" fill="#003366">2. Actionable Career Steps</text>
  <circle cx="256" cy="186" r="3" fill="#003366"/><rect x="264" y="183" width="160" height="7" rx="2" fill="#cbd5e1"/>
  <circle cx="256" cy="200" r="3" fill="#003366"/><rect x="264" y="197" width="150" height="7" rx="2" fill="#cbd5e1"/>
  
  <rect x="248" y="218" width="186" height="24" rx="5" fill="#003366"/>
  <text x="341" y="234" font-size="9.5" font-weight="800" fill="#ffffff" text-anchor="middle">Enrol Today: www.mfs.org.uk</text>
</svg>"""


def get_letter_wireframe_svg():
    return """<svg viewBox="0 0 460 270" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:460px; height:auto; font-family:'Plus Jakarta Sans', sans-serif;">
  <rect x="2" y="2" width="456" height="266" rx="10" fill="#ffffff" stroke="#94a3b8" stroke-width="2"/>
  
  <!-- Sender Address block (Top Right, Spacious) -->
  <rect x="260" y="14" width="180" height="46" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-dasharray="4 3"/>
  <text x="272" y="32" font-size="10" font-weight="800" fill="#0f172a">Sender Address &amp; Date</text>
  <text x="272" y="48" font-size="9" fill="#64748b">Right-aligned, top right corner</text>
  
  <!-- Recipient Address block (Left Aligned, Lower than date) -->
  <rect x="20" y="45" width="180" height="42" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-dasharray="4 3"/>
  <text x="32" y="62" font-size="10" font-weight="800" fill="#0f172a">Recipient Name &amp; Address</text>
  <text x="32" y="77" font-size="9" fill="#64748b">Left-aligned, lower than date</text>
  
  <!-- Salutation -->
  <rect x="20" y="98" width="200" height="22" rx="4" fill="#e0f2fe"/>
  <text x="30" y="113" font-size="10.5" font-weight="800" fill="#0369a1">Dear Mr Davies, / Dear Sir/Madam,</text>
  
  <!-- Subject / Reference Line -->
  <rect x="20" y="128" width="280" height="22" rx="4" fill="#fef3c7"/>
  <text x="30" y="143" font-size="10" font-weight="900" fill="#92400e">RE: FORMAL COMPLAINT - REF #8492</text>
  
  <!-- Body Paragraph lines (Spacious) -->
  <rect x="20" y="158" width="420" height="9" rx="2" fill="#e2e8f0"/>
  <rect x="20" y="172" width="400" height="9" rx="2" fill="#e2e8f0"/>
  <rect x="20" y="186" width="410" height="9" rx="2" fill="#e2e8f0"/>
  
  <!-- Sign-off valediction -->
  <rect x="20" y="206" width="220" height="48" rx="6" fill="#dcfce7" stroke="#86efac"/>
  <text x="30" y="224" font-size="10.5" font-weight="800" fill="#166534">Yours sincerely, / Yours faithfully,</text>
  <text x="30" y="242" font-size="9.5" font-weight="700" fill="#15803d">[Full Candidate Name &amp; Job Title]</text>
</svg>"""


def get_email_wireframe_svg():
    return """<svg viewBox="0 0 460 270" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:460px; height:auto; font-family:'Plus Jakarta Sans', sans-serif;">
  <rect x="2" y="2" width="456" height="266" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
  
  <!-- Email Header Bar -->
  <rect x="2" y="2" width="456" height="34" rx="10 10 0 0" fill="#3b0764"/>
  <circle cx="20" cy="17" r="4.5" fill="#ef4444"/><circle cx="34" cy="17" r="4.5" fill="#f59e0b"/><circle cx="48" cy="17" r="4.5" fill="#10b981"/>
  <text x="68" y="22" font-size="12" font-weight="800" fill="#ffffff">New Workplace Message — Outlook / NHS Webmail</text>
  
  <!-- Header Fields -->
  <rect x="18" y="44" width="424" height="24" rx="5" fill="#f8fafc" stroke="#e2e8f0"/>
  <text x="28" y="60" font-size="10" font-weight="700" fill="#64748b">To: <tspan fill="#0f172a">department.manager@masterfunctionalskills.co.uk</tspan></text>
  
  <rect x="18" y="73" width="424" height="24" rx="5" fill="#f8fafc" stroke="#e2e8f0"/>
  <text x="28" y="89" font-size="10" font-weight="700" fill="#64748b">Subject: <tspan fill="#0f172a" font-weight="900">Proposal: Upgrading Apprentice Clinical Facilities</tspan></text>
  
  <!-- Salutation -->
  <text x="28" y="116" font-size="11" font-weight="800" fill="#3b0764">Dear Clinical Practice Team,</text>
  
  <!-- Message Body lines -->
  <rect x="28" y="126" width="404" height="9" rx="2" fill="#e2e8f0"/>
  <rect x="28" y="140" width="380" height="9" rx="2" fill="#e2e8f0"/>
  
  <!-- Action Points Bullets -->
  <circle cx="36" cy="162" r="3.5" fill="#3b0764"/><rect x="48" y="158" width="340" height="8" rx="2" fill="#cbd5e1"/>
  <circle cx="36" cy="178" r="3.5" fill="#3b0764"/><rect x="48" y="174" width="320" height="8" rx="2" fill="#cbd5e1"/>
  
  <!-- Sign-off & Attachment -->
  <text x="28" y="206" font-size="10.5" font-weight="700" fill="#475569">Kind regards,</text>
  <text x="28" y="222" font-size="11" font-weight="900" fill="#0f172a">Subi • Senior Lead Tutor</text>
  
  <rect x="28" y="234" width="220" height="22" rx="5" fill="#eff6ff" stroke="#bfdbfe"/>
  <text x="38" y="249" font-size="9.5" font-weight="700" fill="#1d4ed8">📎 Clinical_Proposal_Summary_v2.pdf</text>
</svg>"""


def get_report_wireframe_svg():
    return """<svg viewBox="0 0 460 270" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:460px; height:auto; font-family:'Plus Jakarta Sans', sans-serif;">
  <rect x="2" y="2" width="456" height="266" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
  
  <!-- Report Title Header -->
  <rect x="16" y="12" width="428" height="46" rx="5" fill="#0f172a"/>
  <text x="28" y="30" font-size="11.5" font-weight="900" fill="#38bdf8">INVESTIGATION REPORT: HEALTH &amp; SAFETY AUDIT</text>
  <text x="28" y="47" font-size="9" fill="#94a3b8">Target: Safety Executive • Date: October 2026 • Lead Tutor: Subi</text>
  
  <!-- Section 1.0: Executive Summary -->
  <rect x="16" y="66" width="428" height="48" rx="5" fill="#f8fafc" stroke="#e2e8f0"/>
  <text x="26" y="82" font-size="10.5" font-weight="900" fill="#0f172a">1.0 Executive Summary &amp; Scope</text>
  <rect x="26" y="89" width="408" height="7" rx="2" fill="#cbd5e1"/>
  <rect x="26" y="100" width="380" height="7" rx="2" fill="#cbd5e1"/>
  
  <!-- Section 2.0: Table of Findings -->
  <rect x="16" y="120" width="428" height="58" rx="5" fill="#f8fafc" stroke="#e2e8f0"/>
  <text x="26" y="136" font-size="10.5" font-weight="900" fill="#0f172a">2.0 Risk Assessment Matrix</text>
  <rect x="26" y="142" width="408" height="15" rx="3" fill="#e2e8f0"/>
  <text x="36" y="153" font-size="8.5" font-weight="800" fill="#475569">Inspection Zone | Hazard Noted | Severity Rating | Target Date</text>
  <rect x="26" y="159" width="408" height="15" rx="3" fill="#ffffff" stroke="#e2e8f0"/>
  <text x="36" y="170" font-size="8.5" fill="#0f172a">Ward 4 Store | Obstructed Fire Egress | HIGH | Immediate (24h)</text>
  
  <!-- Section 3.0: Recommendations -->
  <rect x="16" y="184" width="428" height="72" rx="5" fill="#eff6ff" stroke="#bfdbfe"/>
  <text x="26" y="200" font-size="10.5" font-weight="900" fill="#1e40af">3.0 Actionable Recommendations</text>
  <text x="36" y="215" font-size="9" font-weight="700" fill="#1e3a8a">• Clear all corridor emergency routes immediately (Priority 1)</text>
  <text x="36" y="229" font-size="9" font-weight="700" fill="#1e3a8a">• Deploy digital checklist app across shift handovers</text>
  <text x="36" y="243" font-size="9" font-weight="700" fill="#1e3a8a">• Complete follow-up audit with Lead Tutor Subi on Friday</text>
</svg>"""


def get_speech_wireframe_svg():
    return """<svg viewBox="0 0 480 280" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:480px; height:auto; font-family:'Plus Jakarta Sans', sans-serif;">
  <rect x="2" y="2" width="476" height="276" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
  <rect x="16" y="12" width="448" height="38" rx="6" fill="#0f766e"/>
  <text x="28" y="28" font-size="10.5" font-weight="800" fill="#a7f3d0">PRESENTATION &amp; SPEECH SCRIPT • FORMAT 5</text>
  <text x="28" y="42" font-size="9" fill="#ffffff">Rhetorical devices • Stage directions • Rule of three</text>
  
  <!-- Opening hook -->
  <rect x="16" y="58" width="448" height="44" rx="6" fill="#f0fdf4" stroke="#86efac"/>
  <text x="26" y="74" font-size="10.5" font-weight="900" fill="#166534">1. Engaging Rhetorical Opening Hook</text>
  <text x="26" y="92" font-size="9.5" font-style="italic" fill="#15803d">"Good morning colleagues. Imagine walking into a hospital ward where..." [Pause for effect]</text>
  
  <!-- Rule of Three & Body Points -->
  <rect x="16" y="110" width="448" height="82" rx="6" fill="#f8fafc" stroke="#e2e8f0"/>
  <text x="26" y="128" font-size="10.5" font-weight="900" fill="#0f172a">2. Core Message with Rule of Three &amp; Emotive Language</text>
  <text x="36" y="146" font-size="9.5" font-weight="700" fill="#0f766e">• Professional: Maintaining statutory safety standards at all times</text>
  <text x="36" y="162" font-size="9.5" font-weight="700" fill="#0f766e">• Compassionate: Putting patient dignity at the heart of our service</text>
  <text x="36" y="178" font-size="9.5" font-weight="700" fill="#0f766e">• Dedicated: Supporting apprentices as they progress into band 3 roles</text>
  
  <!-- Audience Interaction & Closing Call to Action -->
  <rect x="16" y="200" width="448" height="66" rx="6" fill="#eff6ff" stroke="#bfdbfe"/>
  <text x="26" y="216" font-size="10.5" font-weight="900" fill="#1e40af">3. Audience Engagement &amp; Memorable Call to Action</text>
  <text x="26" y="234" font-size="9.5" fill="#1e3a8a">"Together, we can achieve 100% compliance. Thank you for your time." [Slide: Q&amp;A]</text>
  <text x="26" y="252" font-size="9.5" font-weight="800" fill="#2563eb">"I would now like to welcome questions from the floor."</text>
</svg>"""


def get_leaflet_wireframe_svg():
    return """<svg viewBox="0 0 480 280" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:480px; height:auto; font-family:'Plus Jakarta Sans', sans-serif;">
  <rect x="2" y="2" width="476" height="276" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
  <!-- 3-Panel Fold Lines -->
  <line x1="160" y1="2" x2="160" y2="278" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="5 4"/>
  <line x1="320" y1="2" x2="320" y2="278" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="5 4"/>
  
  <!-- Panel 1: Inside Left (Information) -->
  <rect x="10" y="12" width="140" height="26" rx="4" fill="#0284c7"/>
  <text x="80" y="29" font-size="9.5" font-weight="900" fill="#ffffff" text-anchor="middle">1. WHY JOIN US?</text>
  <rect x="10" y="46" width="140" height="60" rx="4" fill="#f0f9ff"/>
  <text x="16" y="62" font-size="8.5" font-weight="800" fill="#0369a1">• Free accredited training</text>
  <text x="16" y="76" font-size="8.5" font-weight="800" fill="#0369a1">• Flexible shift rotas</text>
  <text x="16" y="90" font-size="8.5" font-weight="800" fill="#0369a1">• Expert 1-to-1 lead tutor</text>
  <rect x="10" y="114" width="140" height="152" rx="4" fill="#e2e8f0"/>
  <text x="80" y="190" font-size="9" font-weight="800" fill="#64748b" text-anchor="middle">📷 [Clinic Photo Spread]</text>
  
  <!-- Panel 2: Inside Middle (Course Modules) -->
  <rect x="170" y="12" width="140" height="26" rx="4" fill="#0369a1"/>
  <text x="240" y="29" font-size="9.5" font-weight="900" fill="#ffffff" text-anchor="middle">2. KEY MODULES</text>
  <rect x="170" y="46" width="140" height="24" rx="4" fill="#eff6ff"/>
  <text x="176" y="62" font-size="8.5" font-weight="800" fill="#1e40af">✓ Functional Maths L2</text>
  <rect x="170" y="74" width="140" height="24" rx="4" fill="#eff6ff"/>
  <text x="176" y="90" font-size="8.5" font-weight="800" fill="#1e40af">✓ English Writing Mastery</text>
  <rect x="170" y="102" width="140" height="24" rx="4" fill="#eff6ff"/>
  <text x="176" y="118" font-size="8.5" font-weight="800" fill="#1e40af">✓ Digital Skills (EDSQ)</text>
  <rect x="170" y="132" width="140" height="134" rx="4" fill="#f8fafc" stroke="#e2e8f0"/>
  <text x="240" y="156" font-size="9" font-weight="900" fill="#0f172a" text-anchor="middle">Student Testimonial</text>
  <text x="240" y="176" font-size="8" font-style="italic" fill="#475569" text-anchor="middle">"Passed first time with"</text>
  <text x="240" y="190" font-size="8" font-style="italic" fill="#475569" text-anchor="middle">"Subi's step-by-step drills!"</text>
  
  <!-- Panel 3: Front Cover & Contact (Right) -->
  <rect x="330" y="12" width="140" height="32" rx="4" fill="#070d1e"/>
  <text x="400" y="27" font-size="9.5" font-weight="900" fill="#38bdf8" text-anchor="middle">MASTER SKILLS</text>
  <text x="400" y="38" font-size="7.5" fill="#ffffff" text-anchor="middle">Master Functional Skills</text>
  <rect x="330" y="50" width="140" height="110" rx="4" fill="#e2e8f0"/>
  <text x="400" y="106" font-size="9" font-weight="800" fill="#64748b" text-anchor="middle">📷 [Learner Cover]</text>
  <rect x="330" y="168" width="140" height="98" rx="4" fill="#dcfce7" stroke="#86efac"/>
  <text x="400" y="186" font-size="9" font-weight="900" fill="#166534" text-anchor="middle">CONTACT &amp; ENROL</text>
  <text x="338" y="204" font-size="8" fill="#15803d">📞 01865 901000</text>
  <text x="338" y="220" font-size="8" fill="#15803d">✉️ training@mfs.org.uk</text>
  <text x="338" y="236" font-size="8" fill="#15803d">🌐 masterfunctionalskills.co.uk</text>
</svg>"""


def get_bksb_misconception_svg():
    return """<svg viewBox="0 0 540 280" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:540px; height:auto; font-family:'Plus Jakarta Sans', sans-serif;">
  <rect x="2" y="2" width="536" height="276" rx="14" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
  
  <!-- Header Banner -->
  <rect x="14" y="12" width="512" height="34" rx="8" fill="#1d4ed8"/>
  <text x="26" y="34" font-size="12" font-weight="900" fill="#ffffff">DIAGNOSTIC FAILURE MODE: REVERSE PERCENTAGES</text>
  
  <!-- Side by Side Boxes (Generous Width & Padding) -->
  <!-- Left Box: The Red Error Trap -->
  <rect x="16" y="54" width="246" height="175" rx="8" fill="#fff1f2" stroke="#fca5a5" stroke-width="2"/>
  <rect x="26" y="64" width="226" height="26" rx="5" fill="#fee2e2"/>
  <text x="36" y="81" font-size="10" font-weight="900" fill="#991b1b">✕ COMMON FAILURE TRAP (BKSB)</text>
  
  <text x="28" y="106" font-size="9.5" fill="#881337">Problem: Sale price = £120 after 20% discount.</text>
  <text x="28" y="124" font-size="10" font-weight="800" fill="#b91c1c">Faulty Working:</text>
  <text x="28" y="140" font-size="10" fill="#881337">20% of £120 = £24</text>
  <text x="28" y="156" font-size="10" fill="#881337">£120 + £24 = £144.00</text>
  
  <rect x="24" y="168" width="230" height="48" rx="5" fill="#fee2e2"/>
  <text x="32" y="184" font-size="9" font-weight="800" fill="#991b1b">FATAL FLAW: You cannot add 20% of the</text>
  <text x="32" y="198" font-size="9" font-weight="800" fill="#991b1b">discounted £120 to recover 100% original value!</text>
  <text x="32" y="210" font-size="8.5" fill="#b91c1c">The 20% was deducted from a LARGER starting sum.</text>

  <!-- Right Box: The Golden Rule Method -->
  <rect x="278" y="54" width="246" height="175" rx="8" fill="#f0fdf4" stroke="#86efac" stroke-width="2"/>
  <rect x="288" y="64" width="226" height="26" rx="5" fill="#dcfce7"/>
  <text x="298" y="81" font-size="10" font-weight="900" fill="#166534">✓ GOLDEN RULE METHOD (ABDUL)</text>
  
  <text x="290" y="106" font-size="9.5" fill="#14532d">Sale price £120 represents 80% (100% - 20%).</text>
  <text x="290" y="124" font-size="10" font-weight="800" fill="#15803d">Single-Step Multiplier Method:</text>
  <text x="290" y="140" font-size="10" fill="#14532d">Multiplier = 1.00 - 0.20 = 0.80</text>
  <text x="290" y="158" font-size="12" font-weight="900" fill="#15803d">£120 ÷ 0.80 = £150.00 ✓</text>
  
  <rect x="286" y="168" width="230" height="48" rx="5" fill="#dcfce7"/>
  <text x="294" y="184" font-size="9" font-weight="800" fill="#166534">VERIFICATION CHECK:</text>
  <text x="294" y="198" font-size="9" fill="#15803d">20% of £150 = £30.00.</text>
  <text x="294" y="210" font-size="9" font-weight="800" fill="#166534">£150 - £30 = £120. Perfectly verified! ✓</text>

  <!-- Footer Progress Bar -->
  <rect x="14" y="238" width="512" height="28" rx="6" fill="#eff6ff" stroke="#bfdbfe"/>
  <text x="26" y="256" font-size="10" font-weight="800" fill="#1d4ed8">Target Mastery Progression: Level 1 Emerging (42%) ➔ Level 2 Secure (84%) Sign-Off</text>
</svg>"""


def get_digital_gui_svg():
    return """<svg viewBox="0 0 480 280" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:480px; height:auto; font-family:'Plus Jakarta Sans', sans-serif;">
  <rect x="2" y="2" width="476" height="276" rx="10" fill="#090d16" stroke="#00e5ff" stroke-width="2"/>
  
  <!-- Top Menu Bar -->
  <rect x="2" y="2" width="476" height="30" rx="10 10 0 0" fill="#111827"/>
  <text x="16" y="20" font-size="11" font-weight="900" fill="#00e5ff">OS Desktop • Window Manager (Skill Area 1)</text>
  
  <!-- Window 1: File Explorer (Spacious Left) -->
  <rect x="14" y="42" width="220" height="190" rx="6" fill="#1e293b" stroke="#334155"/>
  <rect x="14" y="42" width="220" height="26" rx="6 6 0 0" fill="#0f172a"/>
  <text x="24" y="59" font-size="9.5" font-weight="800" fill="#94a3b8">📁 File Explorer — /Documents</text>
  
  <text x="24" y="86" font-size="9" font-weight="700" fill="#38bdf8">📁 MFS_Healthcare_Project/</text>
  <text x="36" y="104" font-size="8.5" fill="#cbd5e1">📄 Patient_Rota.xlsx</text>
  <text x="36" y="120" font-size="8.5" fill="#cbd5e1">📄 Handover_Notes.docx</text>
  
  <text x="24" y="142" font-size="9" font-weight="700" fill="#38bdf8">📁 Functional_Skills_Revision/</text>
  <text x="36" y="160" font-size="8.5" fill="#cbd5e1">📄 Mock_Exam_Maths_L2.pdf</text>
  <text x="36" y="176" font-size="8.5" fill="#cbd5e1">📄 Practice_Drills_Subi.docx</text>
  <text x="36" y="192" font-size="8.5" fill="#cbd5e1">📄 Diagnostic_Tracker.xlsx</text>
  
  <!-- Window 2: Web Browser (Spacious Right) -->
  <rect x="246" y="42" width="220" height="190" rx="6" fill="#0f172a" stroke="#00e5ff"/>
  <rect x="246" y="42" width="220" height="26" rx="6 6 0 0" fill="#1e293b"/>
  <!-- URL Bar with Padlock -->
  <rect x="256" y="47" width="200" height="16" rx="4" fill="#090d16" stroke="#334155"/>
  <text x="264" y="59" font-size="8" font-weight="800" fill="#10b981">🔒 https://masterfunctionalskills.co.uk</text>
  
  <rect x="256" y="78" width="200" height="48" rx="5" fill="#1e293b"/>
  <text x="266" y="98" font-size="10" font-weight="900" fill="#38bdf8">Digital Skills Mastery</text>
  <text x="266" y="114" font-size="8" fill="#94a3b8">Interactive learning &amp; exam portal</text>
  
  <rect x="256" y="136" width="94" height="42" rx="4" fill="#1e293b"/>
  <text x="266" y="158" font-size="8.5" font-weight="800" fill="#fbbf24">Level 1 EDSQ</text>
  <rect x="362" y="136" width="94" height="42" rx="4" fill="#1e293b"/>
  <text x="372" y="158" font-size="8.5" font-weight="800" fill="#10b981">Level 2 DFS</text>
  
  <!-- Taskbar at bottom -->
  <rect x="2" y="244" width="476" height="34" rx="0 0 10 10" fill="#030712" stroke="#1f2937"/>
  <rect x="12" y="248" width="24" height="24" rx="4" fill="#00e5ff"/>
  <text x="24" y="264" font-size="12" font-weight="900" fill="#090d16" text-anchor="middle">❖</text>
  <rect x="44" y="250" width="22" height="22" rx="4" fill="#1f2937"/>
  <rect x="72" y="250" width="22" height="22" rx="4" fill="#1f2937"/>
  <rect x="100" y="250" width="22" height="22" rx="4" fill="#1f2937"/>
  <text x="465" y="266" font-size="9" fill="#94a3b8" text-anchor="end">17:05 • 12 Oct 2026</text>
</svg>"""


def get_spreadsheet_wireframe_svg():
    return """<svg viewBox="0 0 480 280" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:480px; height:auto; font-family:'Plus Jakarta Sans', sans-serif;">
  <rect x="2" y="2" width="476" height="276" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
  <rect x="2" y="2" width="476" height="30" rx="10 10 0 0" fill="#15803d"/>
  <text x="16" y="20" font-size="11" font-weight="800" fill="#ffffff">Microsoft Excel / Google Sheets • Spreadsheet Anatomy</text>
  
  <!-- Formula Bar -->
  <rect x="12" y="40" width="70" height="22" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
  <text x="47" y="55" font-size="10" font-weight="800" fill="#0f172a" text-anchor="middle">C6</text>
  <rect x="90" y="40" width="378" height="22" rx="4" fill="#ffffff" stroke="#00e5ff" stroke-width="1.5"/>
  <text x="102" y="55" font-size="10" font-weight="800" fill="#15803d">fx <tspan fill="#0f172a" font-weight="700">=SUM(C2:C5) * 1.20</tspan></text>
  
  <!-- Column Headers -->
  <rect x="12" y="70" width="456" height="22" fill="#e2e8f0"/>
  <text x="30" y="85" font-size="9" font-weight="800" fill="#64748b" text-anchor="middle">#</text>
  <text x="110" y="85" font-size="9" font-weight="800" fill="#64748b">A: Item Description</text>
  <text x="260" y="85" font-size="9" font-weight="800" fill="#64748b">B: Quantity</text>
  <text x="380" y="85" font-size="9" font-weight="800" fill="#64748b">C: Total (£)</text>
  
  <!-- Rows (Spacious) -->
  <rect x="12" y="94" width="456" height="22" fill="#ffffff" stroke="#f1f5f9"/>
  <text x="30" y="109" font-size="8.5" fill="#94a3b8" text-anchor="middle">2</text>
  <text x="110" y="109" font-size="9" fill="#0f172a">Bandages (Box 50)</text>
  <text x="260" y="109" font-size="9" fill="#0f172a">14</text>
  <text x="380" y="109" font-size="9" font-weight="800" fill="#0f172a">£168.00</text>
  
  <rect x="12" y="118" width="456" height="22" fill="#f8fafc" stroke="#f1f5f9"/>
  <text x="30" y="133" font-size="8.5" fill="#94a3b8" text-anchor="middle">3</text>
  <text x="110" y="133" font-size="9" fill="#0f172a">Surgical Gloves (Box 100)</text>
  <text x="260" y="133" font-size="9" fill="#0f172a">25</text>
  <text x="380" y="133" font-size="9" font-weight="800" fill="#0f172a">£212.50</text>
  
  <rect x="12" y="142" width="456" height="22" fill="#ffffff" stroke="#f1f5f9"/>
  <text x="30" y="157" font-size="8.5" fill="#94a3b8" text-anchor="middle">4</text>
  <text x="110" y="157" font-size="9" fill="#0f172a">Digital Thermometer Units</text>
  <text x="260" y="157" font-size="9" fill="#0f172a">8</text>
  <text x="380" y="157" font-size="9" font-weight="800" fill="#0f172a">£156.00</text>
  
  <rect x="12" y="166" width="456" height="22" fill="#f8fafc" stroke="#f1f5f9"/>
  <text x="30" y="181" font-size="8.5" fill="#94a3b8" text-anchor="middle">5</text>
  <text x="110" y="181" font-size="9" fill="#0f172a">Syringe Packs (Pack 100)</text>
  <text x="260" y="181" font-size="9" fill="#0f172a">12</text>
  <text x="380" y="181" font-size="9" font-weight="800" fill="#0f172a">£84.00</text>
  
  <!-- Grand Total Row -->
  <rect x="12" y="190" width="456" height="28" fill="#dcfce7" stroke="#86efac" stroke-width="1.5"/>
  <text x="30" y="208" font-size="9" font-weight="900" fill="#166534" text-anchor="middle">6</text>
  <text x="110" y="208" font-size="10" font-weight="900" fill="#166534">GRAND TOTAL WITH VAT (20%)</text>
  <text x="380" y="208" font-size="11" font-weight="900" fill="#15803d">£744.60 ✓</text>
  
  <!-- Callout note -->
  <rect x="12" y="226" width="456" height="42" rx="5" fill="#eff6ff" stroke="#bfdbfe"/>
  <text x="22" y="242" font-size="8.5" font-weight="800" fill="#1d4ed8">💡 Key Functions: =SUM(range), =AVERAGE(range), =COUNT(range), =MAX/MIN(range)</text>
  <text x="22" y="258" font-size="8" fill="#475569">Formula rule: Always begin with an equals sign (=) or the spreadsheet treats entry as text.</text>
</svg>"""


def get_fact_vs_opinion_svg():
    return """<svg viewBox="0 0 540 250" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:540px; height:auto; font-family:'Plus Jakarta Sans', system-ui, sans-serif;">
  <rect x="2" y="2" width="536" height="246" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
  <rect x="16" y="12" width="280" height="24" rx="6" fill="#e0f2fe"/>
  <text x="26" y="28" font-size="11" font-weight="800" fill="#0369a1">✎ READING CRITERIA: FACT VS OPINION</text>
  <text x="306" y="28" font-size="11" font-weight="700" fill="#475569">Pearson Reading Core Standard</text>
  
  <!-- Left Box: Fact -->
  <rect x="16" y="46" width="246" height="188" rx="8" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>
  <rect x="16" y="46" width="246" height="28" rx="8" fill="#16a34a"/>
  <text x="139" y="65" font-size="12" font-weight="800" fill="#ffffff" text-anchor="middle">✓ OBJECTIVE FACT</text>
  
  <text x="26" y="94" font-size="10.5" font-weight="700" fill="#166534">• Can be proved true or false</text>
  <text x="26" y="112" font-size="10" fill="#15803d">• Backed by statistics, data, dates, records</text>
  <text x="26" y="130" font-size="10" fill="#15803d">• Unbiased, verifiable evidence</text>
  
  <rect x="24" y="146" width="230" height="76" rx="6" fill="#ffffff" stroke="#bbf7d0"/>
  <text x="32" y="164" font-size="10" font-weight="800" fill="#166534">Authentic Exam Example:</text>
  <text x="32" y="182" font-size="9.5" fill="#334155">"The clinic opens at 8:30am and treated</text>
  <text x="32" y="198" font-size="9.5" fill="#334155">420 patients in November."</text>
  <text x="32" y="214" font-size="9" font-weight="700" fill="#16a34a">→ Measurable fact verified by records.</text>

  <!-- Right Box: Opinion -->
  <rect x="278" y="46" width="246" height="188" rx="8" fill="#fff1f2" stroke="#fecdd3" stroke-width="1.5"/>
  <rect x="278" y="46" width="246" height="28" rx="8" fill="#e11d48"/>
  <text x="401" y="65" font-size="12" font-weight="800" fill="#ffffff" text-anchor="middle">✕ SUBJECTIVE OPINION</text>
  
  <text x="288" y="94" font-size="10.5" font-weight="700" fill="#9f1239">• Personal belief, judgment, or feeling</text>
  <text x="288" y="112" font-size="10" fill="#be123c">• Look for value words: 'best', 'dreadful'</text>
  <text x="288" y="130" font-size="10" fill="#be123c">• Cannot be scientifically proven</text>
  
  <rect x="286" y="146" width="230" height="76" rx="6" fill="#ffffff" stroke="#fecdd3"/>
  <text x="294" y="164" font-size="10" font-weight="800" fill="#9f1239">Authentic Exam Example:</text>
  <text x="294" y="182" font-size="9.5" fill="#334155">"Dr Evans is the most caring doctor in</text>
  <text x="294" y="198" font-size="9.5" fill="#334155">the entire healthcare trust."</text>
  <text x="294" y="214" font-size="9" font-weight="700" fill="#e11d48">→ Value judgment / subjective opinion.</text>
</svg>"""


def get_presentational_features_svg():
    return """<svg viewBox="0 0 540 260" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:540px; height:auto; font-family:'Plus Jakarta Sans', system-ui, sans-serif;">
  <rect x="2" y="2" width="536" height="256" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
  <rect x="16" y="12" width="300" height="24" rx="6" fill="#e0f2fe"/>
  <text x="26" y="28" font-size="11" font-weight="800" fill="#0369a1">✎ PRESENTATIONAL FEATURES ARCHITECTURE</text>
  <text x="326" y="28" font-size="11" font-weight="700" fill="#475569">Examiner Layout Checklist</text>

  <!-- Document Layout Simulation -->
  <rect x="16" y="46" width="350" height="200" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5"/>
  
  <!-- Main Heading -->
  <rect x="26" y="56" width="210" height="18" rx="3" fill="#0284c7"/>
  <text x="32" y="69" font-size="10" font-weight="800" fill="#ffffff">MAIN HEADLINE / BANNER</text>
  
  <!-- Subheading -->
  <rect x="26" y="82" width="140" height="12" rx="2" fill="#64748b"/>
  <text x="30" y="91" font-size="8.5" font-weight="700" fill="#ffffff">Subheading: Key Section</text>

  <!-- Body Text Lines -->
  <line x1="26" y1="104" x2="230" y2="104" stroke="#cbd5e1" stroke-width="3" stroke-linecap="round"/>
  <line x1="26" y1="114" x2="215" y2="114" stroke="#cbd5e1" stroke-width="3" stroke-linecap="round"/>
  <line x1="26" y1="124" x2="190" y2="124" stroke="#cbd5e1" stroke-width="3" stroke-linecap="round"/>

  <!-- Bullet points -->
  <circle cx="32" cy="140" r="3" fill="#0284c7"/>
  <line x1="40" y1="140" x2="220" y2="140" stroke="#94a3b8" stroke-width="3" stroke-linecap="round"/>
  <circle cx="32" cy="152" r="3" fill="#0284c7"/>
  <line x1="40" y1="152" x2="200" y2="152" stroke="#94a3b8" stroke-width="3" stroke-linecap="round"/>
  <circle cx="32" cy="164" r="3" fill="#0284c7"/>
  <line x1="40" y1="164" x2="210" y2="164" stroke="#94a3b8" stroke-width="3" stroke-linecap="round"/>

  <!-- Callout box -->
  <rect x="26" y="180" width="210" height="36" rx="4" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.2"/>
  <text x="32" y="194" font-size="8.5" font-weight="800" fill="#b45309">⚠ KEY NOTICE / CALLOUT BOX</text>
  <text x="32" y="208" font-size="8" fill="#78350f">Important warning or deadline information</text>

  <!-- Image and Caption Box on Right of Document -->
  <rect x="246" y="56" width="110" height="90" rx="4" fill="#e2e8f0" stroke="#cbd5e1"/>
  <rect x="256" y="66" width="90" height="55" rx="3" fill="#cbd5e1"/>
  <text x="301" y="97" font-size="9" font-weight="700" fill="#64748b" text-anchor="middle">[ PHOTO / GRAPHIC ]</text>
  <text x="301" y="135" font-size="7.5" font-style="italic" fill="#475569" text-anchor="middle">Figure 1: Explanatory Caption</text>

  <rect x="246" y="156" width="110" height="60" rx="4" fill="#ede9fe" stroke="#c4b5fd"/>
  <text x="301" y="172" font-size="8" font-weight="800" fill="#6d28d9" text-anchor="middle">SIDEBAR / CONTACT</text>
  <text x="301" y="188" font-size="7.5" fill="#5b21b6" text-anchor="middle">Tel: 01865 240000</text>
  <text x="301" y="202" font-size="7.5" fill="#5b21b6" text-anchor="middle">Email: info@hub.co.uk</text>

  <!-- Right Legend / Annotations -->
  <rect x="376" y="46" width="148" height="200" rx="6" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>
  <text x="450" y="66" font-size="11" font-weight="800" fill="#166534" text-anchor="middle">EXAM TERMINOLOGY</text>
  <text x="384" y="88" font-size="9.5" font-weight="700" fill="#0284c7">1. Headline / Heading</text>
  <text x="384" y="102" font-size="8.5" fill="#475569">Identifies overall topic</text>
  
  <text x="384" y="122" font-size="9.5" font-weight="700" fill="#64748b">2. Subheadings</text>
  <text x="384" y="136" font-size="8.5" fill="#475569">Divides text logically</text>

  <text x="384" y="156" font-size="9.5" font-weight="700" fill="#15803d">3. Bullet Points</text>
  <text x="384" y="170" font-size="8.5" fill="#475569">Lists key points clearly</text>

  <text x="384" y="190" font-size="9.5" font-weight="700" fill="#b45309">4. Callout Box / Border</text>
  <text x="384" y="204" font-size="8.5" fill="#475569">Emphasises urgent info</text>

  <text x="384" y="224" font-size="9.5" font-weight="700" fill="#6d28d9">5. Captions &amp; Sidebar</text>
  <text x="384" y="238" font-size="8.5" fill="#475569">Explains visual / contact</text>
</svg>"""


def get_text_types_purpose_svg():
    return """<svg viewBox="0 0 540 260" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:540px; height:auto; font-family:'Plus Jakarta Sans', system-ui, sans-serif;">
  <rect x="2" y="2" width="536" height="256" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
  <rect x="16" y="12" width="280" height="24" rx="6" fill="#e0f2fe"/>
  <text x="26" y="28" font-size="11" font-weight="800" fill="#0369a1">✎ 4 WRITER'S PURPOSES &amp; TEXT TYPES</text>
  <text x="306" y="28" font-size="11" font-weight="700" fill="#475569">Pearson Core Criteria</text>

  <!-- 4 Quadrants -->
  <!-- Q1: Inform -->
  <rect x="16" y="46" width="248" height="95" rx="8" fill="#f0f9ff" stroke="#bae6fd" stroke-width="1.5"/>
  <rect x="24" y="54" width="90" height="20" rx="4" fill="#0284c7"/>
  <text x="69" y="68" font-size="10" font-weight="800" fill="#ffffff" text-anchor="middle">TO INFORM</text>
  <text x="24" y="88" font-size="9.5" font-weight="700" fill="#0369a1">Goal: Give neutral facts &amp; details</text>
  <text x="24" y="104" font-size="9" fill="#334155">Examples: News reports, timetables, guides</text>
  <text x="24" y="120" font-size="8.5" font-style="italic" fill="#64748b">Clues: Dates, times, stats, third person, no bias</text>

  <!-- Q2: Persuade -->
  <rect x="276" y="46" width="248" height="95" rx="8" fill="#fdf2f8" stroke="#fbcfe8" stroke-width="1.5"/>
  <rect x="284" y="54" width="100" height="20" rx="4" fill="#db2777"/>
  <text x="334" y="68" font-size="10" font-weight="800" fill="#ffffff" text-anchor="middle">TO PERSUADE</text>
  <text x="284" y="88" font-size="9.5" font-weight="700" fill="#9d174d">Goal: Convince reader to act or agree</text>
  <text x="284" y="104" font-size="9" fill="#334155">Examples: Adverts, campaign letters, speeches</text>
  <text x="284" y="120" font-size="8.5" font-style="italic" fill="#64748b">Clues: Emotive language, rhetorical questions, rule of 3</text>

  <!-- Q3: Instruct -->
  <rect x="16" y="151" width="248" height="95" rx="8" fill="#f0fdf4" stroke="#bbf7d0" stroke-width="1.5"/>
  <rect x="24" y="159" width="100" height="20" rx="4" fill="#16a34a"/>
  <text x="74" y="173" font-size="10" font-weight="800" fill="#ffffff" text-anchor="middle">TO INSTRUCT</text>
  <text x="24" y="193" font-size="9.5" font-weight="700" fill="#166534">Goal: Tell the reader how to do something</text>
  <text x="24" y="209" font-size="9" fill="#334155">Examples: Operating manuals, directions, recipes</text>
  <text x="24" y="225" font-size="8.5" font-style="italic" fill="#64748b">Clues: Imperative verbs ('Press', 'Cut'), numbered steps</text>

  <!-- Q4: Advise / Explain -->
  <rect x="276" y="151" width="248" height="95" rx="8" fill="#fffbeb" stroke="#fde68a" stroke-width="1.5"/>
  <rect x="284" y="159" width="120" height="20" rx="4" fill="#d97706"/>
  <text x="344" y="173" font-size="10" font-weight="800" fill="#ffffff" text-anchor="middle">TO ADVISE / EXPLAIN</text>
  <text x="284" y="193" font-size="9.5" font-weight="700" fill="#92400e">Goal: Offer guidance, recommendations &amp; tips</text>
  <text x="284" y="209" font-size="9" fill="#334155">Examples: Health leaflets, advice columns, FAQs</text>
  <text x="284" y="225" font-size="8.5" font-style="italic" fill="#64748b">Clues: Modal verbs ('should', 'ought to'), clear recommendations</text>
</svg>"""


def get_comparing_texts_svg():
    return """<svg viewBox="0 0 540 250" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:540px; height:auto; font-family:'Plus Jakarta Sans', system-ui, sans-serif;">
  <rect x="2" y="2" width="536" height="246" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
  <rect x="16" y="12" width="280" height="24" rx="6" fill="#e0f2fe"/>
  <text x="26" y="28" font-size="11" font-weight="800" fill="#0369a1">✎ COMPARING TEXTS &amp; PERSPECTIVES</text>
  <text x="306" y="28" font-size="11" font-weight="700" fill="#475569">Level 1 &amp; Level 2 Reading Benchmark</text>

  <!-- Left Column: Text A -->
  <rect x="16" y="46" width="246" height="188" rx="8" fill="#f0f9ff" stroke="#bae6fd" stroke-width="1.5"/>
  <rect x="16" y="46" width="246" height="28" rx="8" fill="#0284c7"/>
  <text x="139" y="65" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">TEXT A (E.g. Bus Service Route 40)</text>
  <text x="26" y="92" font-size="9.5" font-weight="700" fill="#0369a1">Format:</text><text x="80" y="92" font-size="9.5" fill="#334155">Online timetable &amp; travel leaflet</text>
  <text x="26" y="110" font-size="9.5" font-weight="700" fill="#0369a1">Tone:</text><text x="80" y="110" font-size="9.5" fill="#334155">Informative, promoting low cost (£2.30)</text>
  <text x="26" y="128" font-size="9.5" font-weight="700" fill="#0369a1">Journey:</text><text x="80" y="128" font-size="9.5" fill="#334155">42 minutes (slower, multiple stops)</text>
  <text x="26" y="146" font-size="9.5" font-weight="700" fill="#0369a1">Perks:</text><text x="80" y="146" font-size="9.5" fill="#334155">Free Wi-Fi on board, regular departures</text>
  <rect x="22" y="160" width="234" height="66" rx="4" fill="#ffffff" stroke="#bae6fd"/>
  <text x="28" y="176" font-size="9" font-weight="700" fill="#0369a1">Writer's Main Argument:</text>
  <text x="28" y="192" font-size="8.5" fill="#334155">Bus travel is affordable, convenient, and</text>
  <text x="28" y="206" font-size="8.5" fill="#334155">accessible for everyday local commuters.</text>

  <!-- Right Column: Text B -->
  <rect x="278" y="46" width="246" height="188" rx="8" fill="#fdf4ff" stroke="#f0abfc" stroke-width="1.5"/>
  <rect x="278" y="46" width="246" height="28" rx="8" fill="#a21caf"/>
  <text x="401" y="65" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">TEXT B (E.g. City Express Train)</text>
  <text x="288" y="92" font-size="9.5" font-weight="700" fill="#701a75">Format:</text><text x="342" y="92" font-size="9.5" fill="#334155">Corporate promotional web page</text>
  <text x="288" y="110" font-size="9.5" font-weight="700" fill="#701a75">Tone:</text><text x="342" y="110" font-size="9.5" fill="#334155">Persuasive, focusing on speed &amp; comfort</text>
  <text x="288" y="128" font-size="9.5" font-weight="700" fill="#701a75">Journey:</text><text x="342" y="128" font-size="9.5" fill="#334155">16 minutes (fast, direct express)</text>
  <text x="288" y="146" font-size="9.5" font-weight="700" fill="#701a75">Perks:</text><text x="342" y="146" font-size="9.5" fill="#334155">Quiet coach, power sockets, higher price</text>
  <rect x="284" y="160" width="234" height="66" rx="4" fill="#ffffff" stroke="#f0abfc"/>
  <text x="290" y="176" font-size="9" font-weight="700" fill="#701a75">Writer's Main Argument:</text>
  <text x="290" y="192" font-size="8.5" fill="#334155">Train travel is premium and saves valuable</text>
  <text x="290" y="206" font-size="8.5" fill="#334155">time for busy business professionals.</text>
</svg>"""


def get_spag_sentence_structure_svg():
    return """<svg viewBox="0 0 540 250" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:540px; height:auto; font-family:'Plus Jakarta Sans', system-ui, sans-serif;">
  <rect x="2" y="2" width="536" height="246" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
  <rect x="16" y="12" width="280" height="24" rx="6" fill="#e0f2fe"/>
  <text x="26" y="28" font-size="11" font-weight="800" fill="#0369a1">✎ SPaG SENTENCE STRUCTURE BLUEPRINT</text>
  <text x="306" y="28" font-size="11" font-weight="700" fill="#475569">Entry 3 &amp; Level 1 Essential Rules</text>

  <!-- Box 1: MINTS Capital Letters -->
  <rect x="16" y="46" width="246" height="188" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <rect x="16" y="46" width="246" height="28" rx="8" fill="#0284c7"/>
  <text x="139" y="65" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">CAPITAL LETTERS: MINTS RULE</text>
  <text x="26" y="92" font-size="10" font-weight="700" fill="#0369a1">M</text><text x="42" y="92" font-size="9.5" fill="#334155">Months &amp; Days (Monday, July)</text>
  <text x="26" y="110" font-size="10" font-weight="700" fill="#0369a1">I</text><text x="42" y="110" font-size="9.5" fill="#334155">The pronoun 'I' (Always capitalised)</text>
  <text x="26" y="128" font-size="10" font-weight="700" fill="#0369a1">N</text><text x="42" y="128" font-size="9.5" fill="#334155">Names of people &amp; places (Sara, Oxford)</text>
  <text x="26" y="146" font-size="10" font-weight="700" fill="#0369a1">T</text><text x="42" y="146" font-size="9.5" fill="#334155">Titles (Dr, Manager, British Council)</text>
  <text x="26" y="164" font-size="10" font-weight="700" fill="#0369a1">S</text><text x="42" y="164" font-size="9.5" fill="#334155">Start of every sentence</text>
  <rect x="22" y="178" width="234" height="48" rx="4" fill="#ecfdf5" stroke="#a7f3d0"/>
  <text x="28" y="194" font-size="8.5" font-weight="700" fill="#065f46">Golden Exam Benchmark:</text>
  <text x="28" y="208" font-size="8" fill="#047857">"Every Monday, David and I visit Oxford."</text>
  <text x="28" y="220" font-size="7.5" fill="#047857">✓ All 4 capital rules applied correctly.</text>

  <!-- Box 2: End Punctuation & Commas -->
  <rect x="278" y="46" width="246" height="188" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <rect x="278" y="46" width="246" height="28" rx="8" fill="#0f172a"/>
  <text x="401" y="65" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">PUNCTUATION &amp; COMMAS</text>
  <text x="288" y="92" font-size="10" font-weight="700" fill="#0284c7">Full Stop (.)</text><text x="365" y="92" font-size="9.5" fill="#334155">Ends a complete thought</text>
  <text x="288" y="110" font-size="10" font-weight="700" fill="#0284c7">Question (?)</text><text x="365" y="110" font-size="9.5" fill="#334155">Requires an answer</text>
  <text x="288" y="128" font-size="10" font-weight="700" fill="#0284c7">Exclamation (!)</text><text x="365" y="128" font-size="9.5" fill="#334155">Urgent instruction / alert</text>
  <text x="288" y="146" font-size="10" font-weight="700" fill="#0284c7">Comma (,)</text><text x="365" y="146" font-size="9.5" fill="#334155">Separates items in a list</text>
  <rect x="284" y="162" width="234" height="64" rx="4" fill="#fff7ed" stroke="#fed7aa"/>
  <text x="290" y="178" font-size="8.5" font-weight="700" fill="#9a3412">Comma in Lists Rule:</text>
  <text x="290" y="194" font-size="8" fill="#7c2d12">"Please order paper, pens, folders, and ink."</text>
  <text x="290" y="208" font-size="7.5" font-weight="700" fill="#ea580c">Never join sentences with a comma alone!</text>
  <text x="290" y="220" font-size="7.5" fill="#9a3412">(Avoid comma splice: use 'and' or full stop)</text>
</svg>"""


def get_notice_poster_wireframe_svg():
    return """<svg viewBox="0 0 540 250" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:540px; height:auto; font-family:'Plus Jakarta Sans', system-ui, sans-serif;">
  <rect x="2" y="2" width="536" height="246" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
  <rect x="16" y="12" width="280" height="24" rx="6" fill="#e0f2fe"/>
  <text x="26" y="28" font-size="11" font-weight="800" fill="#0369a1">✎ FORMAT BLUEPRINT: NOTICE &amp; POSTER</text>
  <text x="306" y="28" font-size="11" font-weight="700" fill="#475569">Workplace Public Notice Architecture</text>

  <!-- Poster simulation frame -->
  <rect x="16" y="46" width="340" height="190" rx="6" fill="#fffbeb" stroke="#f59e0b" stroke-width="2"/>
  <!-- Header banner -->
  <rect x="24" y="54" width="324" height="32" rx="4" fill="#b45309"/>
  <text x="186" y="74" font-size="12" font-weight="800" fill="#ffffff" text-anchor="middle">ATTENTION: STAFF KITCHEN PROTOCOL</text>
  
  <!-- Bullet point section -->
  <text x="30" y="102" font-size="9" font-weight="700" fill="#78350f">Please follow these 3 workplace hygiene rules:</text>
  <circle cx="36" cy="118" r="3" fill="#b45309"/><text x="46" y="121" font-size="8.5" fill="#451a03">Wash, dry, and put away all mugs immediately.</text>
  <circle cx="36" cy="134" r="3" fill="#b45309"/><text x="46" y="137" font-size="8.5" fill="#451a03">Label all food items in the fridge with your name.</text>
  <circle cx="36" cy="150" r="3" fill="#b45309"/><text x="46" y="153" font-size="8.5" fill="#451a03">Friday 4pm: Unlabelled items will be cleared.</text>

  <!-- Highlight box -->
  <rect x="24" y="166" width="324" height="36" rx="4" fill="#fee2e2" stroke="#ef4444"/>
  <text x="186" y="182" font-size="9" font-weight="800" fill="#991b1b" text-anchor="middle">EMERGENCY CONTACT &amp; FIRST AID</text>
  <text x="186" y="195" font-size="8" fill="#7f1d1d" text-anchor="middle">Report facility issues to Building Manager: Ext 402</text>

  <text x="24" y="226" font-size="7.5" font-weight="600" fill="#92400e">Issue Date: 12 October 2026 • Operations Directorate</text>

  <!-- Right side checklist -->
  <rect x="368" y="46" width="156" height="190" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="446" y="66" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">NOTICE CHECKLIST</text>
  <text x="376" y="88" font-size="9" font-weight="700" fill="#0284c7">✓ Bold Eye-Catching Title</text>
  <text x="376" y="102" font-size="8" fill="#64748b">Must state topic instantly</text>
  <text x="376" y="122" font-size="9" font-weight="700" fill="#0284c7">✓ Bullet Points for Rules</text>
  <text x="376" y="136" font-size="8" fill="#64748b">Enables rapid reading</text>
  <text x="376" y="156" font-size="9" font-weight="700" fill="#0284c7">✓ Specific Action &amp; Time</text>
  <text x="376" y="170" font-size="8" fill="#64748b">Clear deadline / protocol</text>
  <text x="376" y="190" font-size="9" font-weight="700" fill="#0284c7">✓ Contact / Sign-off</text>
  <text x="376" y="204" font-size="8" fill="#64748b">Tells reader who to notify</text>
</svg>"""


def get_vocabulary_context_svg():
    return """<svg viewBox="0 0 540 250" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:540px; height:auto; font-family:'Plus Jakarta Sans', system-ui, sans-serif;">
  <rect x="2" y="2" width="536" height="246" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
  <rect x="16" y="12" width="300" height="24" rx="6" fill="#e0f2fe"/>
  <text x="26" y="28" font-size="11" font-weight="800" fill="#0369a1">✎ WORDS IN CONTEXT &amp; VOCABULARY</text>
  <text x="326" y="28" font-size="11" font-weight="700" fill="#475569">Context Clue Deduction Strategy</text>

  <!-- 3 Strategy Steps -->
  <!-- Step 1 -->
  <rect x="16" y="46" width="160" height="188" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <rect x="16" y="46" width="160" height="28" rx="8" fill="#0284c7"/>
  <text x="96" y="65" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">1. SURROUNDING CLUES</text>
  <text x="24" y="92" font-size="9.5" font-weight="700" fill="#0369a1">Look Before &amp; After:</text>
  <text x="24" y="108" font-size="8.5" fill="#334155">Read the whole sentence</text>
  <text x="24" y="122" font-size="8.5" fill="#334155">and adjoining sentences to</text>
  <text x="24" y="136" font-size="8.5" fill="#334155">grasp the overall sense.</text>
  <rect x="22" y="152" width="148" height="72" rx="4" fill="#ecfdf5" stroke="#a7f3d0"/>
  <text x="26" y="168" font-size="8" font-weight="700" fill="#065f46">Exam Tip:</text>
  <text x="26" y="182" font-size="8" fill="#047857">Look for conjunctions</text>
  <text x="26" y="196" font-size="8" fill="#047857">like 'however' (opposite)</text>
  <text x="26" y="210" font-size="8" fill="#047857">or 'also' (similar idea).</text>

  <!-- Step 2 -->
  <rect x="190" y="46" width="160" height="188" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <rect x="190" y="46" width="160" height="28" rx="8" fill="#0f172a"/>
  <text x="270" y="65" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">2. WORD MORPHOLOGY</text>
  <text x="198" y="92" font-size="9.5" font-weight="700" fill="#0284c7">Break the Word Apart:</text>
  <text x="198" y="108" font-size="8.5" fill="#334155">• Prefix: re- (again), un- (not)</text>
  <text x="198" y="122" font-size="8.5" fill="#334155">• Root: the base word meaning</text>
  <text x="198" y="136" font-size="8.5" fill="#334155">• Suffix: -ful, -less, -tion</text>
  <rect x="196" y="152" width="148" height="72" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
  <text x="200" y="168" font-size="8" font-weight="700" fill="#1e40af">Example:</text>
  <text x="200" y="182" font-size="8" fill="#1d4ed8">'Inaccessible':</text>
  <text x="200" y="196" font-size="8" fill="#1e3a8a">in- (not) + access (reach)</text>
  <text x="200" y="210" font-size="8" fill="#1e3a8a">+ ible (able to be) = Not able to reach.</text>

  <!-- Step 3 -->
  <rect x="364" y="46" width="160" height="188" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <rect x="364" y="46" width="160" height="28" rx="8" fill="#16a34a"/>
  <text x="444" y="65" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">3. SUBSTITUTION TEST</text>
  <text x="372" y="92" font-size="9.5" font-weight="700" fill="#166534">Swap with a Known Word:</text>
  <text x="372" y="108" font-size="8.5" fill="#334155">Replace the tricky word</text>
  <text x="372" y="122" font-size="8.5" fill="#334155">with your estimated synonym.</text>
  <text x="372" y="136" font-size="8.5" fill="#334155">Does the sentence still work?</text>
  <rect x="370" y="152" width="148" height="72" rx="4" fill="#fef3c7" stroke="#fde68a"/>
  <text x="374" y="168" font-size="8" font-weight="700" fill="#92400e">Golden Exam Rule:</text>
  <text x="374" y="182" font-size="8" fill="#78350f">Never leave a question blank.</text>
  <text x="374" y="196" font-size="8" fill="#78350f">A logical contextual guess</text>
  <text x="374" y="210" font-size="8" fill="#78350f">frequently earns the mark!</text>
</svg>"""
