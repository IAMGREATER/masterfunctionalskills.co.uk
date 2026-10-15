#!/usr/bin/env python3
"""
write_specialist_builder.py
Constructs the complete, audit-compliant build_specialist_suite_a4.py.
"""

from pathlib import Path

OUT_FILE = Path(__file__).resolve().parent / "build_specialist_suite_a4.py"

def make_script():
    parts = []
    
    # Header & imports
    parts.append('''#!/usr/bin/env python3
"""
build_specialist_suite_a4.py
============================
Master Functional Skills - Specialist & Mocks Suite (4 Publications)
A4 Portrait (210 x 297 mm), 86-94 Pages Each, Zero Blank Space, Fully Illustrated.

Publications:
  1. MasterFunctionalSkills_Mock_Pack_Maths_L2.pdf (92 Pages)
  2. MasterFunctionalSkills_Mock_Pack_English_L2.pdf (86 Pages)
  3. MasterFunctionalSkills_Digital_Skills_Handbook.pdf (88 Pages)
  4. MasterFunctionalSkills_BKSB_Remediation_Workbook.pdf (90 Pages)
"""

import os
import sys
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import a4_kit as K
import specialist_suite_content as ssc
import specialist_suite_reference as ssr

PROJECT_DIR = HERE.parent.parent
DOWNLOADS = PROJECT_DIR / "assets" / "downloads"
DOCUMENTS = Path("/home/subi/Documents")
COV = K.COVER_DIR


def get_photo(keywords, theme=None, exclude=None):
    ex = exclude if exclude is not None else set()
    p = K.photo(keywords, theme, ex)
    if not p:
        p = K.photo(keywords, None, set()) or K.photo("office workspace computer", None, set())
    return p


def get_cartoon(keywords, exclude=None):
    ex = exclude if exclude is not None else set()
    c = K.cartoon(keywords, ex)
    if not c:
        c = K.cartoon(keywords, set()) or K.cartoon("explaining tutor", set())
    return c


def cartoon_tip(cartoon_path, name, text):
    return K.character_bubble(cartoon_path, name, text, side="left", height_mm=48)

K.cartoon_tip = cartoon_tip


def exam_box(text, marks=None):
    badge = f"<span style='float:right; font-weight:bold; color:var(--accent); margin-left:10px;'>[{marks} Marks]</span>" if marks else ""
    return f"<div class='cbox' style='margin-bottom:8px; padding:10px 14px; border-left:4px solid var(--accent); background:#f8fafc;'><div style='font-size:11.5pt; line-height:1.45;'>{badge}{text}</div></div>"

K.exam_box = exam_box
''')

    # 1. Mock Pack Maths Level 2
    parts.append('''
# =============================================================================
# 1. Mock Pack Maths Level 2 (A4 ~92 Pages)
# =============================================================================
def build_mock_maths_l2():
    print("\\n" + "="*70)
    print("BUILDING: MasterFunctionalSkills_Mock_Pack_Maths_L2.pdf")
    print("="*70)

    BOOK = "Maths L2 Official 6-Mock Exam Pack"
    front_cov = COV / "mock_pack_maths_l2_cover_page-1.png"
    back_cov = COV / "mock_pack_maths_l2_cover_page-2.png"
    cover_theme = K.theme_from_cover(front_cov)

    pages = []
    used_photos = set()

    def P(kw):
        p = get_photo(kw, "maths", used_photos)
        if p:
            used_photos.add(p)
        return p

    # p1: Front Cover
    pages.append(K.front_cover(front_cov))

    # p2: Inside Cover & Examination Blueprint
    pages.append(K.inside_cover(
        "Functional Skills Mathematics &bull; Level 2",
        "Official 6-Mock Examination Pack &bull; Complete Papers, Step-by-Step Mark Schemes &amp; Process Mark Rubrics",
        "Maths Level 2",
        [
            ("1", "Level 2 Essential Formulae: Geometry &amp; Trigonometry", "3"),
            ("2", "Level 2 Essential Formulae: Measures, Conversions &amp; Statistics", "4"),
            ("3", "Pearson Edexcel Exam Technique, Problem Solving &amp; Process Marks", "5"),
            ("4", "Diagnostic Performance Tracker &amp; Target Setting", "6"),
            ("M1&ndash;M6", "6 Complete Official-Style Exam Papers (48 pages)", "7"),
            ("WS1&ndash;WS6", "6 Advanced Exam Problem-Solving Workshops (6 pages)", "55"),
            ("MS", "Comprehensive Examiner Mark Schemes &amp; Condensed Solutions (26 pages)", "61"),
            ("CERT", "Grade Boundaries &amp; Official Exam Readiness Certificate", "87"),
        ],
        footer=BOOK
    ))

    # p3: Essential Formulae - Geometry & Trigonometry
    p3_body = (
        K.page_title("Level 2 Essential Formulae: Geometry &amp; Shapes", kicker="Formula Reference Sheet &bull; Part 1", badge="F1")
        + K.hero_image(P("construction architectural blueprint measuring tape"), "Geometry calculations underpin construction and engineering exams.", 48)
        + K.box_html(
            "<table style='width:100%; border-collapse:collapse; font-size:11.5pt;'>"
            "<tr><td style='padding:6px; border-bottom:1px solid #cbd5e1;'><b>Circumference of Circle:</b></td><td style='padding:6px; border-bottom:1px solid #cbd5e1;'><code>C = &pi;d = 2&pi;r</code> (use &pi; = 3.14 or 3.142)</td></tr>"
            "<tr><td style='padding:6px; border-bottom:1px solid #cbd5e1;'><b>Area of Circle:</b></td><td style='padding:6px; border-bottom:1px solid #cbd5e1;'><code>A = &pi;r&sup2;</code> (always square radius, NEVER multiply by 2!)</td></tr>"
            "<tr><td style='padding:6px; border-bottom:1px solid #cbd5e1;'><b>Area of Cylinder (Curved):</b></td><td style='padding:6px; border-bottom:1px solid #cbd5e1;'><code>Curved Surface Area = &pi;dh = 2&pi;rh</code></td></tr>"
            "<tr><td style='padding:6px; border-bottom:1px solid #cbd5e1;'><b>Volume of Cylinder:</b></td><td style='padding:6px; border-bottom:1px solid #cbd5e1;'><code>V = &pi;r&sup2;h</code> (Area of cross-section &times; height)</td></tr>"
            "<tr><td style='padding:6px; border-bottom:1px solid #cbd5e1;'><b>Volume of Triangular Prism:</b></td><td style='padding:6px; border-bottom:1px solid #cbd5e1;'><code>V = (&frac12; &times; base &times; height) &times; length</code></td></tr>"
            "<tr><td style='padding:6px;'><b>Pythagoras Theorem:</b></td><td style='padding:6px;'><code>a&sup2; + b&sup2; = c&sup2;</code> (where c is the hypotenuse)</td></tr>"
            "</table>",
            title="Geometric Formulae (Memorise for Section A &amp; B)"
        )
        + K.tip_pair("For semi-circles, divide circumference or area by 2. Add diameter if calculating perimeter.",
                     "Remember: &pi;r&sup2; is NOT (&pi;r)&sup2;. Square radius first, then multiply by &pi;.",
                     golden_title="Golden Geometry Rule", watch_title="Examiner Trap!")
        + K.fill_notes("Personal Geometry Notes &amp; Formula Memory Triggers", 24)
    )
    pages.append(K.page(p3_body, header=(BOOK, "Formulae &bull; Geometry"), footer=BOOK, page_no=3))

    # p4: Essential Formulae - Measures, Conversions & Statistics
    p4_body = (
        K.page_title("Level 2 Essential Formulae: Measures &amp; Statistics", kicker="Formula Reference Sheet &bull; Part 2", badge="F2")
        + K.box_html(
            "<table style='width:100%; border-collapse:collapse; font-size:11.5pt;'>"
            "<tr><td style='padding:6px; border-bottom:1px solid #cbd5e1;'><b>Speed, Distance &amp; Time:</b></td><td style='padding:6px; border-bottom:1px solid #cbd5e1;'><code>Speed = Distance &divide; Time</code> | <code>Time = Dist &divide; Speed</code></td></tr>"
            "<tr><td style='padding:6px; border-bottom:1px solid #cbd5e1;'><b>Density, Mass &amp; Volume:</b></td><td style='padding:6px; border-bottom:1px solid #cbd5e1;'><code>Density = Mass &divide; Volume</code> | <code>Mass = Density &times; Volume</code></td></tr>"
            "<tr><td style='padding:6px; border-bottom:1px solid #cbd5e1;'><b>Percentage Change:</b></td><td style='padding:6px; border-bottom:1px solid #cbd5e1;'><code>% Change = (Actual Change &divide; Original Value) &times; 100</code></td></tr>"
            "<tr><td style='padding:6px; border-bottom:1px solid #cbd5e1;'><b>Reverse Percentage:</b></td><td style='padding:6px; border-bottom:1px solid #cbd5e1;'><code>Original Value = New Value &divide; Decimal Multiplier</code></td></tr>"
            "<tr><td style='padding:6px; border-bottom:1px solid #cbd5e1;'><b>Estimated Mean (Grouped):</b></td><td style='padding:6px; border-bottom:1px solid #cbd5e1;'><code>Estimated Mean = &Sigma;(midpoint &times; frequency) &divide; &Sigma;(frequency)</code></td></tr>"
            "<tr><td style='padding:6px;'><b>Combined Probability:</b></td><td style='padding:6px;'><code>P(A and B) = P(A) &times; P(B)</code> (for independent events)</td></tr>"
            "</table>",
            title="Measures, Rates &amp; Statistics Matrix"
        )
        + K.cartoon_tip(get_cartoon("abdul tutor explaining"), "Abdul",
                        "Time Trap Alert! 2 hours 15 minutes is 2.25 hours, NOT 2.15 hours! Always convert minutes to decimal hours by dividing by 60 before using speed formulas.")
        + K.fill_notes("Key Conversion Facts (e.g. 1 m&sup3; = 1,000 litres, 1 gallon = 4.55 litres)", 28)
    )
    pages.append(K.page(p4_body, header=(BOOK, "Formulae &bull; Measures"), footer=BOOK, page_no=4))

    # p5: Exam Technique & Process Marks
    p5_body = (
        K.page_title("Exam Technique &amp; Securing Process Marks", kicker="Examiner Strategy Guide", badge="EX")
        + K.hero_image(P("adult student calculator exam writing"), "Every intermediate step secures process marks even if your final answer is wrong.", 46)
        + K.box_html(
            "<div style='display:grid; grid-template-columns:1fr 1fr; gap:12px; font-size:11.5pt;'>"
            "<div><b>[P] Process Marks:</b> Awarded for choosing the correct strategy (e.g. recognizing a 20% discount means multiplying by 0.80).</div>"
            "<div><b>[M] Method Marks:</b> Awarded for writing out standard formulas with given values substituted correctly.</div>"
            "<div><b>[A] Accuracy Marks:</b> Awarded strictly for the correct numerical calculation.</div>"
            "<div><b>[B] Independent Marks:</b> Awarded for correct units (&pound;, m&sup2;, kg), rounding, or valid written checks.</div>"
            "</div>",
            title="Pearson Mark Classification System"
        )
        + K.rule_box("How to Write a Guaranteed 1-Mark 'Check'",
                     "<p>When asked to <i>'Show a check of your answer'</i>, use one of two methods:<br>"
                     "<b>1. Reverse Operation (Inverse):</b> If <code>45 &times; 12 = 540</code>, write <code>Check: 540 &divide; 12 = 45</code>.<br>"
                     "<b>2. Estimation Check:</b> Round inputs to 1 significant figure: <code>Check: 48.2 &times; 9.8 &asymp; 50 &times; 10 = 500</code>.<br>"
                     "<b>Trap:</b> Simply rewriting <code>12 &times; 45 = 540</code> scores <b>0 marks</b>!</p>")
        + K.fill_notes("My Personal Exam Rules &amp; Timing Checklist", 22)
    )
    pages.append(K.page(p5_body, header=(BOOK, "Exam Technique &bull; Strategy"), footer=BOOK, page_no=5))

    # p6: Diagnostic Performance Tracker
    p6_body = (
        K.page_title("Diagnostic Mock Performance Tracker", kicker="Scores &amp; Progress Monitoring", badge="TR")
        + K.box_html(
            "<table style='width:100%; border-collapse:collapse; font-size:11.5pt; text-align:center;'>"
            "<tr style='background:#f1f5f9;'><th style='padding:6px; text-align:left;'>Paper</th><th>Sec A (/16)</th><th>Sec B (/48)</th><th>Total (/64)</th><th>% Score</th><th>Status</th><th>Date</th></tr>"
            + "".join(f"<tr><td style='padding:6px; border-bottom:1px solid #e2e8f0; text-align:left;'><b>Mock Paper {i}</b></td>"
                      f"<td style='border-bottom:1px solid #e2e8f0;'>&nbsp;&nbsp;&nbsp;&nbsp;/16</td>"
                      f"<td style='border-bottom:1px solid #e2e8f0;'>&nbsp;&nbsp;&nbsp;&nbsp;/48</td>"
                      f"<td style='border-bottom:1px solid #e2e8f0;'><b>&nbsp;&nbsp;&nbsp;&nbsp;/64</b></td>"
                      f"<td style='border-bottom:1px solid #e2e8f0;'>&nbsp;&nbsp;&nbsp;&nbsp;%</td>"
                      f"<td style='border-bottom:1px solid #e2e8f0;'>[ &nbsp; ] Pass</td>"
                      f"<td style='border-bottom:1px solid #e2e8f0;'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td></tr>"
                      for i in range(1, 7))
            + "</table>",
            title="Pearson Edexcel Level 2 Pass Benchmark: 38–42 Marks (approx. 60–65%)"
        )
        + K.fill_notes("Target Topics for Post-Mock Revision &amp; 1-to-1 Tutoring", 28)
    )
    pages.append(K.page(p6_body, header=(BOOK, "Score Tracker"), footer=BOOK, page_no=6))

    # pp7–p54: 6 Complete Official Exam Papers (8 pages per paper = 48 pages)
    p_curr = 7
    for p_idx, mock in enumerate(ssc.MATHS_L2_MOCKS, start=1):
        theme = mock["theme"]
        kw1 = mock["kw1"]
        kw2 = mock["kw2"]
        sec_a = mock["sec_a"]
        sec_b = mock["sec_b"]

        # Page 1 of Paper: Section A (Non-Calc) Q1 & Q2
        p1_b = (
            K.page_title(f"Mock Paper {p_idx} &bull; Section A (Non-Calculator)", kicker=f"Paper {p_idx}: {theme}", badge=f"P{p_idx}.A")
            + K.box_html(
                "<p style='margin:0;'><b>Duration: 25 minutes | Marks: 16 Marks | Calculators STRICTLY FORBIDDEN.</b><br>"
                "Show all intermediate calculation steps to secure method and process marks.</p>",
                title="Section A Candidate Instructions"
            )
            + exam_box(sec_a[0]["q1"], marks=sec_a[0]["m1"])
            + K.fill_grid(f"Candidate Working Grid &bull; Question 1 (Show all columnar steps)", min_mm=42)
            + exam_box(sec_a[0]["q2"], marks=sec_a[0]["m2"])
            + K.fill_grid(f"Candidate Working Grid &bull; Question 2", min_mm=42)
        )
        pages.append(K.page(p1_b, header=(BOOK, f"Paper {p_idx} &bull; Sec A"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 2 of Paper: Section A Q3 & Q4
        p2_b = (
            K.page_title(f"Mock Paper {p_idx} &bull; Section A (Questions 3 &amp; 4)", kicker=f"Paper {p_idx}: {theme}", badge=f"P{p_idx}.A")
            + exam_box(sec_a[1]["q3"], marks=sec_a[1]["m3"])
            + K.fill_grid("Candidate Working Grid &bull; Question 3 (Fraction Operations)", min_mm=45)
            + exam_box(sec_a[1]["q4"], marks=sec_a[1]["m4"])
            + K.fill_grid("Candidate Working Grid &bull; Question 4 (Reverse Percentage &amp; Check)", min_mm=45)
        )
        pages.append(K.page(p2_b, header=(BOOK, f"Paper {p_idx} &bull; Sec A"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 3 of Paper: Section A Q5 & Check
        p3_b = (
            K.page_title(f"Mock Paper {p_idx} &bull; Section A (Question 5 &bull; Synthesis)", kicker=f"Paper {p_idx}: {theme}", badge=f"P{p_idx}.A")
            + exam_box(sec_a[2]["q5"], marks=sec_a[2]["m5"])
            + K.fill_grid("Candidate Working Grid &bull; Question 5 (Multi-Step Ratio &amp; Units)", min_mm=60)
            + K.rule_box("Section A Verification Protocol",
                         "<p>Before time expires: (1) Re-check decimal alignment in Q1. (2) Confirm fraction is simplified to lowest terms in Q3. (3) Ensure inverse check is written for Q4.</p>")
            + K.box_html(
                f"<div style='display:flex; justify-content:space-between; font-weight:bold; font-size:11.5pt;'>"
                f"<span>Section A Score: ______ / 16</span>"
                f"<span>Time Expended: ______ mins</span>"
                f"</div>",
                title="Section A Candidate Sign-Off"
            )
        )
        pages.append(K.page(p3_b, header=(BOOK, f"Paper {p_idx} &bull; Sec A End"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 4 of Paper: Section B (Calculator) Q6 & Q7
        p4_b = (
            K.page_title(f"Mock Paper {p_idx} &bull; Section B (Calculator Permitted)", kicker=f"Paper {p_idx}: {theme}", badge=f"P{p_idx}.B")
            + K.hero_image(P(kw1), f"Workplace Scenario: {theme}", 40)
            + K.box_html(
                "<p style='margin:0;'><b>Duration: 1 hour 20 minutes | Marks: 48 Marks | Calculators Permitted.</b><br>"
                "Show formula substitutions clearly. Process marks are awarded for valid mathematical strategies.</p>",
                title="Section B Candidate Instructions"
            )
            + exam_box(sec_b[0]["q6"], marks=sec_b[0]["m6"])
            + K.fill_grid("Candidate Working Grid &bull; Question 6", min_mm=36)
            + exam_box(sec_b[0]["q7"], marks=sec_b[0]["m7"])
            + K.fill_grid("Candidate Working Grid &bull; Question 7", min_mm=36)
        )
        pages.append(K.page(p4_b, header=(BOOK, f"Paper {p_idx} &bull; Sec B"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 5 of Paper: Section B Q8 & Q9
        p5_b = (
            K.page_title(f"Mock Paper {p_idx} &bull; Section B (Questions 8 &amp; 9)", kicker=f"Paper {p_idx}: {theme}", badge=f"P{p_idx}.B")
            + exam_box(sec_b[1]["q8"], marks=sec_b[1]["m8"])
            + K.fill_grid("Candidate Working Grid &bull; Question 8 (Statistical Grouping)", min_mm=42)
            + exam_box(sec_b[1]["q9"], marks=sec_b[1]["m9"])
            + K.fill_grid("Candidate Working Grid &bull; Question 9 (Rates &amp; Economy)", min_mm=42)
        )
        pages.append(K.page(p5_b, header=(BOOK, f"Paper {p_idx} &bull; Sec B"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 6 of Paper: Section B Q10 & Q11
        p6_b = (
            K.page_title(f"Mock Paper {p_idx} &bull; Section B (Questions 10 &amp; 11)", kicker=f"Paper {p_idx}: {theme}", badge=f"P{p_idx}.B")
            + K.hero_image(P(kw2), f"Commercial &amp; Operational Planning: {theme}", 40)
            + exam_box(sec_b[2]["q10"], marks=sec_b[2]["m10"])
            + K.fill_grid("Candidate Working Grid &bull; Question 10 (3D Capacity)", min_mm=36)
            + exam_box(sec_b[2]["q11"], marks=sec_b[2]["m11"])
            + K.fill_grid("Candidate Working Grid &bull; Question 11 (Profit Margins)", min_mm=36)
        )
        pages.append(K.page(p6_b, header=(BOOK, f"Paper {p_idx} &bull; Sec B"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 7 of Paper: Section B Q12 & Q13
        p7_b = (
            K.page_title(f"Mock Paper {p_idx} &bull; Section B (Questions 12 &amp; 13)", kicker=f"Paper {p_idx}: {theme}", badge=f"P{p_idx}.B")
            + exam_box(sec_b[3]["q12"], marks=sec_b[3]["m12"])
            + K.fill_grid("Candidate Working Grid &bull; Question 12 (Probability)", min_mm=42)
            + exam_box(sec_b[3]["q13"], marks=sec_b[3]["m13"])
            + K.fill_grid("Candidate Working Grid &bull; Question 13 (Speed &amp; Decimal Time)", min_mm=42)
        )
        pages.append(K.page(p7_b, header=(BOOK, f"Paper {p_idx} &bull; Sec B"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 8 of Paper: Section B Q14 & Q15 (Synthesis)
        p8_b = (
            K.page_title(f"Mock Paper {p_idx} &bull; Section B (Questions 14 &amp; 15 &bull; Synthesis)", kicker=f"Paper {p_idx}: {theme}", badge=f"P{p_idx}.B")
            + exam_box(sec_b[4]["q14"], marks=sec_b[4]["m14"])
            + K.fill_grid("Candidate Working Grid &bull; Question 14 (Pythagoras)", min_mm=36)
            + exam_box(sec_b[4]["q15"], marks=sec_b[4]["m15"])
            + K.fill_grid("Candidate Working Grid &bull; Question 15 Comprehensive Solution", min_mm=42)
            + K.box_html(
                f"<div style='display:flex; justify-content:space-between; font-weight:bold; font-size:11.5pt;'>"
                f"<span>Paper {p_idx} Total Marks: ______ / 64</span>"
                f"<span>Examiner Sign-Off: ____________________</span>"
                f"<span>Date: ____________</span>"
                f"</div>",
                title="Candidate Paper Summary"
            )
        )
        pages.append(K.page(p8_b, header=(BOOK, f"Paper {p_idx} &bull; Summary"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # pp55–p60: 6 Advanced Process Mark Exam Workshops (6 pages)
    workshops = [
        ("Reverse Percentage &amp; VAT Deconstruction", "ws1",
         "Mastering the single-step multiplier division for pre-tax and pre-discount pricing.",
         "finance currency money calculator accounting",
         "A supplier quotes &pound;864.00 inclusive of 20% VAT. A junior trainee mistakenly calculates 20% of &pound;864 (&pound;172.80) and subtracts it to get &pound;691.20.<br>"
         "<b>Examiner Analysis:</b> This is a catastrophic zero-mark error. The VAT was added to the ORIGINAL price, not the final price.<br>"
         "<b>Correct Method:</b> Multiplier = 1.00 + 0.20 = 1.20. Original net price = &pound;864.00 &divide; 1.20 = <b>&pound;720.00</b>. True VAT = &pound;144.00.",
         "Practice Drill: A commercial vehicle was sold for &pound;14,950 after a 15% promotional markdown. Calculate the original list price before discount.",
         "Show your multi-step working and state the multiplier used."),
        ("Speed, Density &amp; Compound Measures Conversions", "ws2",
         "Eliminating decimal time errors and compound unit traps.",
         "warehouse forklift logistics delivery van",
         "Converting 2 hours 45 minutes into decimal hours.<br>"
         "<b>Trap:</b> Entering 2.45 into your calculator loses all subsequent accuracy marks.<br>"
         "<b>Method:</b> 45 minutes &divide; 60 = 0.75 hours. Therefore, time = <b>2.75 hours</b>.<br>"
         "For speed: Speed = Distance &divide; Time = 110 miles &divide; 2.75 hours = <b>40 mph</b>.",
         "Practice Drill: A delivery van travels 162 miles at an average speed of 54 mph. The driver leaves depot at 09:40 and takes a 25-minute break. Calculate arrival time.",
         "Candidate Working Grid &bull; Compound Time Drill"),
        ("Surface Area, Cylinders &amp; Composite Geometry", "ws3",
         "Managing two-dimensional nets and three-dimensional curved boundaries.",
         "construction architectural blueprint measuring tape",
         "Calculating total surface area of a closed industrial storage cylinder of radius r = 1.4 m and height h = 3.5 m.<br>"
         "<b>Formula:</b> Total Surface Area = 2&pi;r&sup2; + 2&pi;rh.<br>"
         "Circular ends = 2 &times; 3.142 &times; (1.4)&sup2; = 2 &times; 3.142 &times; 1.96 = 12.32 m&sup2;.<br>"
         "Curved body = 2 &times; 3.142 &times; 1.4 &times; 3.5 = 30.79 m&sup2;.<br>"
         "Total Area = 12.32 + 30.79 = <b>43.11 m&sup2;</b>.",
         "Practice Drill: A cylindrical water butt is open at the top. The diameter is 0.8 m and height is 1.5 m. Calculate exterior surface area requiring sealant.",
         "Candidate Working Grid &bull; Cylinder Geometry"),
        ("Grouped Frequency &amp; Estimated Mean Calculations", "ws4",
         "Securing full 4-mark process sequences from data tables.",
         "commercial business finance cash register",
         "To find estimated mean: (1) Find midpoints of each interval. (2) Multiply each midpoint by its frequency (fx). (3) Sum the fx column (&Sigma;fx). (4) Divide by total frequency (&Sigma;f).<br>"
         "<b>Crucial Trap:</b> Never divide by the number of rows or intervals (e.g. dividing by 4 or 5 scores zero marks).",
         "Practice Drill: The table shows package weights in kg: [0-4kg: 8], [5-9kg: 15], [10-14kg: 22], [15-19kg: 5]. Calculate the estimated mean weight.",
         "Candidate Working Grid &bull; Estimated Mean Table"),
        ("Scatter Diagrams, Trend Lines &amp; Correlation Reasoning", "ws5",
         "Accurate interpolation and distinguishing cause from association.",
         "medical laboratory clinical healthcare equipment",
         "Drawing a line of best fit: Must have an approximately equal number of points above and below the line, following the linear trend of the data points.<br>"
         "<b>Examiner Rule:</b> Never join the points dot-to-dot! Extend your line across the full range of plotted values to allow accurate interpolation.",
         "Practice Drill: A scatter graph plots engine size (litres) against fuel consumption (mpg). Identify the correlation type and estimate consumption for a 2.2 L engine.",
         "Candidate Working Grid &bull; Correlation Analysis"),
        ("Multi-Stage Decision Trees &amp; Independent Probability", "ws6",
         "Synthesising combined chances and commercial risk assessment.",
         "freight transport cargo container",
         "For independent events: P(A and B) = P(A) &times; P(B).<br>"
         "If quality inspection 1 has a 95% pass rate (0.95) and inspection 2 has a 98% pass rate (0.98), the probability that a product passes both audits is 0.95 &times; 0.98 = <b>0.931 (93.1%)</b>.<br>"
         "Probability of failing at least one audit = 1.00 - 0.931 = <b>0.069 (6.9%)</b>.",
         "Practice Drill: A transport firm operates two automated sorting conveyors. Machine X has an outage probability of 0.04. Machine Y has an outage probability of 0.05. Calculate the probability that both operate without failure.",
         "Candidate Working Grid &bull; Dual Probability Tree")
    ]

    for ws_title, badge, lead, photo_kw, theory_html, drill_title, grid_label in workshops:
        ws_body = (
            K.page_title(ws_title, kicker="Advanced Process Mark Masterclass", badge=badge.upper())
            + K.hero_image(P(photo_kw), lead, 40)
            + K.box_html(f"<div style='font-size:11pt; line-height:1.45;'>{theory_html}</div>", title="Exemplar Method &amp; Process Deconstruction")
            + exam_box(drill_title, marks=4)
            + K.fill_grid(grid_label, min_mm=42)
        )
        pages.append(K.page(ws_body, header=(BOOK, "Exam Workshop"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # Back matter reference section (via K.ref_pages)
    ref_blocks = []
    for m_idx in range(1, 7):
        for title_str, sol_html in ssr.MATHS_L2_MOCK_SOLUTIONS[m_idx]:
            ref_blocks.append(K.ref_block(title_str, sol_html))

    ref_blocks.append(K.ref_block("Official Pearson Level 2 Formulae Directory", ssr.MATHS_L2_FORMULAS))

    gloss_html = "".join(f"<dl><dt>{t}</dt><dd>{d}</dd></dl>" for t, d in ssr.MATHS_L2_GLOSSARY)
    ref_blocks.append(K.ref_block("Mathematical Glossary &amp; Examination Vocabulary", gloss_html))

    ix_html = ""
    for letter, entries in ssr.MATHS_L2_INDEX:
        items = "".join(f"<div class='ix'><span>{t}</span><span>{p}</span></div>" for t, p in entries)
        ix_html += f"<div class='ix-letter'>{letter}</div>{items}"
    ref_blocks.append(K.ref_block("Curriculum &amp; Problem Solving Index", ix_html))

    ref_page_list = K.ref_pages("Official Mark Schemes &amp; Reference Directory", ref_blocks,
                                BOOK, start_page=p_curr, subtitle="Complete Step-by-Step Worked Solutions &amp; Process Mark Guidance",
                                cols=2, theme=cover_theme, notes_title="Candidate Error Analysis &amp; Exam Checklist")
    pages.extend(ref_page_list)
    p_curr += len(ref_page_list)

    # Grade Boundaries & Scaling (1 page)
    gb_body = (
        K.page_title("Official Grade Boundaries &amp; Scaling", kicker="Pearson Edexcel Standards", badge="GB")
        + K.box_html(
            "<table style='width:100%; border-collapse:collapse; font-size:11.5pt; text-align:center;'>"
            "<tr style='background:#f1f5f9;'><th style='padding:8px; text-align:left;'>Examination Series</th><th>Section A (/16)</th><th>Section B (/48)</th><th>Pass Boundary (/64)</th><th>Pass %</th></tr>"
            "<tr><td style='padding:8px; border-bottom:1px solid #e2e8f0; text-align:left;'>Standard Series 1</td><td>9</td><td>29</td><td><b>38</b></td><td>59.4%</td></tr>"
            "<tr><td style='padding:8px; border-bottom:1px solid #e2e8f0; text-align:left;'>Standard Series 2</td><td>10</td><td>29</td><td><b>39</b></td><td>60.9%</td></tr>"
            "<tr><td style='padding:8px; border-bottom:1px solid #e2e8f0; text-align:left;'>Higher Difficulty Series 3</td><td>9</td><td>28</td><td><b>37</b></td><td>57.8%</td></tr>"
            "<tr><td style='padding:8px; border-bottom:1px solid #e2e8f0; text-align:left;'>Target Mastery Benchmark</td><td>12</td><td>36</td><td><b>48</b></td><td>75.0%</td></tr>"
            "</table>",
            title="Pearson Edexcel Functional Skills Mathematics Level 2 Scaling"
        )
        + K.cartoon_tip(get_cartoon("priya tutor writing notes"), "Priya",
                        "Aim for a minimum score of 42 marks across your practice mocks. This provides a safe 4-mark buffer above the highest official pass threshold!")
        + K.fill_notes("Personal Revision Strategy &amp; Final Mock Target", 45)
    )
    pages.append(K.page(gb_body, header=(BOOK, "Grade Boundaries"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Candidate Readiness Certificate (1 page)
    cert_body = (
        K.page_title("Examination Readiness Verification", kicker="Official Milestone Sign-Off", badge="CERT")
        + K.hero_image(P("adult student graduation diploma celebration success"), "Dedication and systematic practice unlock lifelong career progression.", 50)
        + K.box_html(
            "<div style='text-align:center; padding:15px; font-size:12pt; line-height:1.7;'>"
            "<p>This certifies that</p>"
            "<p style='font-size:18pt; font-weight:bold; border-bottom:2px solid var(--accent); display:inline-block; min-width:320px; padding-bottom:4px;'>&nbsp;</p>"
            "<p>has completed all 6 Official-Style Mock Examinations and demonstrated competence across all Pearson Edexcel Functional Skills Mathematics Level 2 standards.</p>"
            "<table style='width:100%; margin-top:20px; font-size:11pt; border-collapse:collapse;'>"
            "<tr><td style='text-align:left;'><b>Lead Tutor:</b> Abdul</td><td style='text-align:right;'><b>Date Verified:</b> _______________</td></tr>"
            "<tr><td style='text-align:left;'><b>Average Mock Score:</b> ______ / 64</td><td style='text-align:right;'><b>Exam Centre:</b> Oxford Health OH</td></tr>"
            "</table>"
            "</div>",
            title="Master Functional Skills &bull; Certificate of Exam Readiness"
        )
        + K.fill_notes("Final Examination Tips &amp; Formula Memory Reminders", 30)
    )
    pages.append(K.page(cert_body, header=(BOOK, "Readiness Certificate"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Inside Back Cover & Back Cover
    pages.append(K.inside_back_cover("Functional Skills Mathematics Level 2 &bull; 6-Mock Exam Pack", BOOK))
    pages.append(K.back_cover(back_cov))

    pdf_path = DOWNLOADS / "MasterFunctionalSkills_Mock_Pack_Maths_L2.pdf"
    K.render_book(pages, pdf_path, theme=cover_theme)
    print(f"Generated: {pdf_path} ({len(pages)} pages)")
    return pdf_path
''')

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write("".join(parts))
    print("write_specialist_builder.py stage 1 complete (Mock Maths L2 written)!")

if __name__ == "__main__":
    make_script()
