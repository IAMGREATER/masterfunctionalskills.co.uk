#!/usr/bin/env python3
"""
build_sample_book_publications.py
Compiles comprehensive multi-page sample booklets (PDF) for:
- Maths Level 2 Core Study Guide
- Maths Level 1 Core Study Guide
- Essential Digital Skills (EDSQ) Practical Study Handbook
- BKSB / OneAdvanced Diagnostic Remediation Workbook
Using direct Chromium headless printing.
"""

import os
import subprocess

PROJECT_DIR = "/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk"
DOWNLOADS_DIR = os.path.join(PROJECT_DIR, "assets", "downloads")
BOOKS_IMG_DIR = os.path.join(PROJECT_DIR, "assets", "img", "books")
SCRATCH_DIR = os.path.join(PROJECT_DIR, "scratch", "book_samples")
os.makedirs(DOWNLOADS_DIR, exist_ok=True)
os.makedirs(SCRATCH_DIR, exist_ok=True)

SAMPLE_CSS = """
<style>
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800;900&family=Open+Sans:ital,wght@0,400;0,600;0,700;1,400&family=Oswald:wght@600;700&display=swap');
  @page {
    size: A4 portrait;
    margin: 0;
  }
  * {
    box-sizing: border-box;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
  body {
    margin: 0;
    padding: 0;
    font-family: 'Open Sans', Arial, sans-serif;
    color: #1e293b;
    background: #ffffff;
    font-size: 9.5pt;
    line-height: 1.5;
  }
  .page {
    width: 210mm;
    height: 297mm;
    page-break-after: always;
    break-after: page;
    position: relative;
    padding: 16mm 20mm 16mm 20mm;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }
  .cover-full-page {
    padding: 0 !important;
  }
  .cover-full-img {
    width: 210mm;
    height: 297mm;
    display: block;
    object-fit: cover;
  }
  .page-header {
    border-bottom: 2px solid var(--theme-color, #002855);
    padding-bottom: 8px;
    margin-bottom: 16px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .page-header-title {
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 8.5pt;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: var(--theme-color, #002855);
  }
  .page-header-strand {
    font-size: 8pt;
    font-weight: 700;
    color: #64748b;
  }
  .page-footer {
    position: absolute;
    bottom: 10mm;
    left: 20mm;
    right: 20mm;
    border-top: 1px solid #e2e8f0;
    padding-top: 8px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 7.8pt;
    color: #64748b;
  }
  .page-num {
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    color: var(--theme-color, #002855);
  }
  h2 {
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    color: var(--theme-color, #002855);
    font-size: 15pt;
    margin: 0 0 10px 0;
  }
  h3 {
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    color: #0f172a;
    font-size: 11pt;
    margin: 14px 0 6px 0;
  }
  .box-info {
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-left: 4px solid var(--theme-color, #002855);
    padding: 12px 14px;
    border-radius: 6px;
    margin: 12px 0;
  }
  .box-trap {
    background: #fef2f2;
    border: 1px solid #fecaca;
    border-left: 4px solid #ef4444;
    padding: 12px 14px;
    border-radius: 6px;
    margin: 12px 0;
    color: #991b1b;
  }
  .box-model {
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
    border-left: 4px solid #10b981;
    padding: 12px 14px;
    border-radius: 6px;
    margin: 12px 0;
  }
  .math-step {
    display: flex;
    justify-content: space-between;
    padding: 4px 0;
    border-bottom: 1px dashed #e2e8f0;
    font-size: 9.2pt;
  }
  .math-step strong {
    color: var(--theme-color, #002855);
  }
  .mark-badge {
    background: #002855;
    color: #ffffff;
    padding: 2px 7px;
    border-radius: 4px;
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 7.5pt;
  }
  table.content-table {
    width: 100%;
    border-collapse: collapse;
    margin: 14px 0;
    font-size: 8.8pt;
  }
  table.content-table th, table.content-table td {
    padding: 8px 10px;
    border: 1px solid #e2e8f0;
    text-align: left;
  }
  table.content-table th {
    background: var(--theme-color, #002855);
    color: #ffffff;
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
  }
  table.content-table tr:nth-child(even) {
    background: #f8fafc;
  }
</style>
"""

def generate_maths_l2_sample():
    front_img = os.path.join(BOOKS_IMG_DIR, "maths_l2_core_cover_page-1.png")
    back_img = os.path.join(BOOKS_IMG_DIR, "maths_l2_core_cover_page-2.png")
    
    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Maths Level 2 Core Study Guide - Sample</title>
{SAMPLE_CSS}
<style>
  :root {{ --theme-color: #002855; --accent: #38bdf8; }}
</style>
</head>
<body>

<!-- PAGE 1: FRONT COVER -->
<div class="page cover-full-page">
  <img src="file://{front_img}" class="cover-full-img">
</div>

<!-- PAGE 2: PUBLISHING & 39 STANDARDS SCHEME OF WORK -->
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Maths Level 2</div>
    <div class="page-header-strand">Ofqual Specification &bull; 39 Standards</div>
  </div>
  <h2>Statutory Subject Content Mapping</h2>
  <p>The Reformed Functional Skills Mathematics Level 2 specification covers 39 statutory learning outcomes across three core curriculum domains. Every section in this guide is mapped directly to these standards:</p>
  
  <table class="content-table">
    <tr>
      <th style="width:25%;">Domain</th>
      <th style="width:20%;">DfE Content Codes</th>
      <th>Key Focus Areas &amp; Examination Weighting</th>
    </tr>
    <tr>
      <td><strong>1. Using Numbers &amp; the Number System</strong></td>
      <td>L2.1 &ndash; L2.11</td>
      <td>Fractions, Decimals, Percentages, Ratio, Compound Interest, Section A Non-Calc Mental Strategies (25% marks).</td>
    </tr>
    <tr>
      <td><strong>2. Measures, Shape &amp; Space</strong></td>
      <td>L2.12 &ndash; L2.27</td>
      <td>Perimeter &amp; Circumference, Area of Compound Shapes, Prisms &amp; Cylinders Volume, Density, Speed &amp; Scale Drawings (40% marks).</td>
    </tr>
    <tr>
      <td><strong>3. Handling Data &amp; Information</strong></td>
      <td>L2.28 &ndash; L2.39</td>
      <td>Mean from Grouped Frequency Tables, Scatter Graphs &amp; Correlation, Probability Trees, Range &amp; Two-Way Tables (35% marks).</td>
    </tr>
  </table>

  <div class="box-info">
    <h3 style="margin-top:0; color:#002855;"><i class="fa-solid fa-calculator"></i> Exam Structure &amp; Timing</h3>
    <ul style="margin:0; padding-left:18px; line-height:1.6;">
      <li><strong>Section A (Non-Calculator):</strong> 25 Minutes &bull; 16 Marks (Mental arithmetic, long division, fraction operations)</li>
      <li><strong>Section B (Calculator):</strong> 1 Hour 30 Minutes &bull; 48 Marks (Multi-step workplace problem solving)</li>
      <li><strong>Total Qualification Standard:</strong> 64 Marks &bull; Typical Pass Boundary: 36&ndash;40 Marks (56&ndash;62%)</li>
    </ul>
  </div>

  <div class="page-footer">
    <div>Functional Skills Maths Level 2 &bull; Core Study &amp; Revision Guide</div>
    <div class="page-num">Page 2</div>
  </div>
</div>

<!-- PAGE 3: SECTION B MULTI-STEP EXEMPLAR (COMPOUND AREA & COST) -->
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Domain 2: Measures, Shape &amp; Space</div>
    <div class="page-header-strand">DfE Standard: L2.17 &amp; L2.18</div>
  </div>
  <h2>Stepped Model Solution: Compound Garden Tiling</h2>
  <div class="box-info">
    <strong>Exam Prompt (5 Marks):</strong><br>
    Sarah is laying artificial turf and paving slabs in an L-shaped garden. The total garden is 12m long by 8m wide, with a 4m by 5m patio cutout. 
    Turf costs &pound;8.50 per square metre. Sarah has a budget of &pound;650.<br>
    <em>Can Sarah afford to turf the remaining area? Show all your working.</em>
  </div>

  <div class="box-model">
    <h3 style="margin-top:0; color:#10b981;">Step-by-Step Examiner Benchmark Method:</h3>
    <div class="math-step">
      <span><strong>Step 1: Calculate Total Rectangle Area</strong><br>Area_total = 12m &times; 8m = 96 m&sup2;</span>
      <span class="mark-badge">[M1 Method Mark]</span>
    </div>
    <div class="math-step">
      <span><strong>Step 2: Calculate Cutout Patio Area</strong><br>Area_patio = 4m &times; 5m = 20 m&sup2;</span>
      <span class="mark-badge">[M1 Method Mark]</span>
    </div>
    <div class="math-step">
      <span><strong>Step 3: Subtract to Find Lawn Area to Turf</strong><br>Lawn Area = 96 m&sup2; &minus; 20 m&sup2; = 76 m&sup2;</span>
      <span class="mark-badge">[A1 Accuracy Mark]</span>
    </div>
    <div class="math-step">
      <span><strong>Step 4: Calculate Total Cost of Turf</strong><br>Cost = 76 &times; &pound;8.50 = &pound;646.00</span>
      <span class="mark-badge">[M1 Method Mark]</span>
    </div>
    <div class="math-step">
      <span><strong>Step 5: Compare with Budget &amp; State Clear Decision</strong><br>&pound;646.00 is less than &pound;650.00 (&pound;4 under budget). <strong>Yes, Sarah can afford it.</strong></span>
      <span class="mark-badge">[A1 Final Decision]</span>
    </div>
  </div>

  <div class="box-trap">
    <strong><i class="fa-solid fa-triangle-exclamation"></i> Official Examiner Trap Alert:</strong><br>
    Many candidates calculate the cost correctly as &pound;646.00 but fail to write the final concluding statement ("Yes, she can afford it"). In Pearson Edexcel and City &amp; Guilds mark schemes, the final accuracy mark is strictly conditional upon stating a definitive "Yes" or "No".
  </div>

  <div class="page-footer">
    <div>Functional Skills Maths Level 2 &bull; Core Study &amp; Revision Guide</div>
    <div class="page-num">Page 42</div>
  </div>
</div>

<!-- PAGE 4: BACK COVER -->
<div class="page cover-full-page">
  <img src="file://{back_img}" class="cover-full-img">
</div>

</body>
</html>
"""
    html_path = os.path.join(SCRATCH_DIR, "maths_l2_sample.html")
    pdf_path = os.path.join(DOWNLOADS_DIR, "MasterFunctionalSkills_Maths_Level_2_Core_Guide_Sample.pdf")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    cmd = [
        "/usr/lib/chromium/chromium",
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--user-data-dir=/tmp/chr_sample_m2",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]
    subprocess.run(cmd, check=True)
    print("Generated:", pdf_path)

def generate_maths_l1_sample():
    front_img = os.path.join(BOOKS_IMG_DIR, "maths_l1_core_cover_page-1.png")
    back_img = os.path.join(BOOKS_IMG_DIR, "maths_l1_core_cover_page-2.png")
    
    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Maths Level 1 Core Study Guide - Sample</title>
{SAMPLE_CSS}
<style>
  :root {{ --theme-color: #0c4e45; --accent: #facc15; }}
</style>
</head>
<body>

<!-- PAGE 1: FRONT COVER -->
<div class="page cover-full-page">
  <img src="file://{front_img}" class="cover-full-img">
</div>

<!-- PAGE 2: METRIC CONVERSIONS & TIME -->
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Maths Level 1</div>
    <div class="page-header-strand">Measures &bull; Metric Conversions</div>
  </div>
  <h2>Visual Metric Unit Conversion Ladder</h2>
  <p>In Level 1 exams, converting between millimeters, centimeters, meters, and kilometers is essential for perimeter and tiling questions. Use our conversion ladder:</p>

  <div class="box-model" style="border-left-color:#0c4e45; background:#f0fdfa;">
    <h3 style="margin-top:0; color:#0c4e45;">Length Conversion Rules:</h3>
    <ul style="line-height:1.8; font-size:10pt;">
      <li><strong>Millimeters to Centimeters:</strong> Divide by 10 (e.g. 50 mm &divide; 10 = 5 cm)</li>
      <li><strong>Centimeters to Meters:</strong> Divide by 100 (e.g. 350 cm &divide; 100 = 3.5 m)</li>
      <li><strong>Meters to Kilometers:</strong> Divide by 1000 (e.g. 2400 m &divide; 1000 = 2.4 km)</li>
    </ul>
  </div>

  <div class="box-info" style="border-left-color:#0c4e45;">
    <strong>Example Exam Prompt (3 Marks):</strong><br>
    A builder needs 4 pieces of timber, each 75 cm long. Timber is sold in 1-metre lengths.<br>
    <em>How many 1-metre lengths must the builder buy? Show your working.</em><br><br>
    <strong>Stepped Solution:</strong><br>
    Total length needed = 4 &times; 75 cm = 300 cm.<br>
    Convert cm to metres = 300 &divide; 100 = 3 metres.<br>
    <strong>Answer: 3 lengths of timber.</strong>
  </div>

  <div class="page-footer">
    <div>Functional Skills Maths Level 1 &bull; Core Study &amp; Revision Guide</div>
    <div class="page-num">Page 28</div>
  </div>
</div>

<!-- PAGE 3: BACK COVER -->
<div class="page cover-full-page">
  <img src="file://{back_img}" class="cover-full-img">
</div>

</body>
</html>
"""
    html_path = os.path.join(SCRATCH_DIR, "maths_l1_sample.html")
    pdf_path = os.path.join(DOWNLOADS_DIR, "MasterFunctionalSkills_Maths_Level_1_Core_Guide_Sample.pdf")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    cmd = [
        "/usr/lib/chromium/chromium",
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--user-data-dir=/tmp/chr_sample_m1",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]
    subprocess.run(cmd, check=True)
    print("Generated:", pdf_path)

def generate_digital_sample():
    front_img = os.path.join(BOOKS_IMG_DIR, "digital_skills_cover_page-1.png")
    back_img = os.path.join(BOOKS_IMG_DIR, "digital_skills_cover_page-2.png")
    
    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Essential Digital Skills Handbook - Sample</title>
{SAMPLE_CSS}
<style>
  :root {{ --theme-color: #0f172a; --accent: #06b6d4; }}
</style>
</head>
<body>

<!-- PAGE 1: FRONT COVER -->
<div class="page cover-full-page">
  <img src="file://{front_img}" class="cover-full-img">
</div>

<!-- PAGE 2: SKILL AREA 5 SAFE & SECURE ONLINE -->
<div class="page">
  <div class="page-header">
    <div class="page-header-title">National Digital Standards &bull; Level 1</div>
    <div class="page-header-strand">Skill Area 5: Being Safe &amp; Responsible Online</div>
  </div>
  <h2>Phishing Detection &amp; Online Safety Protocols</h2>
  <p>Skill Area 5 requires learners to identify suspicious communications, protect personal information, and demonstrate secure password protocols.</p>

  <div class="box-info" style="border-left-color:#06b6d4;">
    <h3 style="margin-top:0; color:#0f172a;">The 4 Red Flags of a Phishing Email:</h3>
    <ul style="line-height:1.7;">
      <li><strong>Mismatched Sender Address:</strong> The display name says "Your Bank", but the actual domain is `@secure-update-notice.xyz`.</li>
      <li><strong>Artificial Urgency:</strong> Demands immediate action: "Account will be suspended within 24 hours".</li>
      <li><strong>Generic Greeting:</strong> Uses "Dear Customer" instead of your actual registered name.</li>
      <li><strong>Suspicious Links:</strong> Hovering reveals a destination URL completely unrelated to the authentic organization.</li>
    </ul>
  </div>

  <div class="box-model" style="border-left-color:#10b981;">
    <h3 style="margin-top:0; color:#10b981;">Safe Response Procedure:</h3>
    <ol style="line-height:1.7;">
      <li>Never click direct links or open unverified attachments.</li>
      <li>Flag and report the email to your workplace IT administrator or spam filter.</li>
      <li>If in doubt, navigate to the organization's official website independently via browser bookmark.</li>
    </ol>
  </div>

  <div class="page-footer">
    <div>Essential Digital Skills (EDSQ) &bull; Practical Study Handbook</div>
    <div class="page-num">Page 48</div>
  </div>
</div>

<!-- PAGE 3: BACK COVER -->
<div class="page cover-full-page">
  <img src="file://{back_img}" class="cover-full-img">
</div>

</body>
</html>
"""
    html_path = os.path.join(SCRATCH_DIR, "digital_sample.html")
    pdf_path = os.path.join(DOWNLOADS_DIR, "MasterFunctionalSkills_Digital_Skills_Handbook_Sample.pdf")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    cmd = [
        "/usr/lib/chromium/chromium",
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--user-data-dir=/tmp/chr_sample_dig",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]
    subprocess.run(cmd, check=True)
    print("Generated:", pdf_path)

def generate_bksb_sample():
    front_img = os.path.join(BOOKS_IMG_DIR, "bksb_remediation_cover_page-1.png")
    back_img = os.path.join(BOOKS_IMG_DIR, "bksb_remediation_cover_page-2.png")
    
    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>BKSB Remediation Workbook - Sample</title>
{SAMPLE_CSS}
<style>
  :root {{ --theme-color: #1e3a8a; --accent: #f59e0b; }}
</style>
</head>
<body>

<!-- PAGE 1: FRONT COVER -->
<div class="page cover-full-page">
  <img src="file://{front_img}" class="cover-full-img">
</div>

<!-- PAGE 2: TWO-STAGE GAP REMEDIATION -->
<div class="page">
  <div class="page-header">
    <div class="page-header-title">BKSB / OneAdvanced Remediation Bridge</div>
    <div class="page-header-strand">Two-Stage Method &bull; Ratio &amp; Proportion</div>
  </div>
  <h2>The Two-Stage Diagnostic Remediation Routine</h2>
  <p>When an online diagnostic test flags a gap, passive reading rarely leads to retention. Our Two-Stage method forces active cognitive recall before revealing tutor solutions:</p>

  <div class="box-info" style="border-left-color:#f59e0b;">
    <h3 style="margin-top:0; color:#1e3a8a;">Stage 1: Independent Retry Challenge</h3>
    <p>A chemist mixes two cleaning liquids, Solution A and Solution B, in the ratio <strong>3 : 5</strong>. The total mixture has a volume of <strong>960 ml</strong>.<br>
    <em>Calculate the volume of Solution B in the mixture.</em></p>
    <div style="height:45px; border:1px dashed #cbd5e1; border-radius:4px; padding:8px; color:#94a3b8;">
      Learner Working Box (Attempt before checking Stage 2)...
    </div>
  </div>

  <div class="box-model" style="border-left-color:#10b981;">
    <h3 style="margin-top:0; color:#10b981;">Stage 2: Tutor Stepped Model &amp; Diagnostic Proof</h3>
    <ul style="line-height:1.7;">
      <li><strong>Step 1: Add ratio parts together:</strong> 3 + 5 = <strong>8 total parts</strong>.</li>
      <li><strong>Step 2: Find value of one part:</strong> 960 ml &divide; 8 = <strong>120 ml per part</strong>.</li>
      <li><strong>Step 3: Multiply by required share:</strong> Solution B has 5 parts &rarr; 5 &times; 120 ml = <strong>600 ml</strong>.</li>
      <li><strong>Verification Check:</strong> Solution A = 3 &times; 120 = 360 ml. 360 + 600 = 960 ml &check;.</li>
    </ul>
  </div>

  <div class="page-footer">
    <div>BKSB / OneAdvanced Remediation Workbook &bull; Levels 1 &amp; 2</div>
    <div class="page-num">Page 14</div>
  </div>
</div>

<!-- PAGE 3: BACK COVER -->
<div class="page cover-full-page">
  <img src="file://{back_img}" class="cover-full-img">
</div>

</body>
</html>
"""
    html_path = os.path.join(SCRATCH_DIR, "bksb_sample.html")
    pdf_path = os.path.join(DOWNLOADS_DIR, "MasterFunctionalSkills_BKSB_Remediation_Workbook_Sample.pdf")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    cmd = [
        "/usr/lib/chromium/chromium",
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--user-data-dir=/tmp/chr_sample_bksb",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]
    subprocess.run(cmd, check=True)
    print("Generated:", pdf_path)

def main():
    print("=== Compiling Sample Book Publications ===")
    generate_maths_l2_sample()
    generate_maths_l1_sample()
    generate_digital_sample()
    generate_bksb_sample()
    print("All sample book publications generated successfully!")

if __name__ == "__main__":
    main()
