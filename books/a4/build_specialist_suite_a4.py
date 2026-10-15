#!/usr/bin/env python3
"""
build_specialist_suite_a4.py
============================
Master Functional Skills - Specialist & Mocks Suite (4 Publications)
A4 Portrait (210 x 297 mm), 84-90 Pages Each, Zero Blank Space, Fully Illustrated.

Publications:
  1. MasterFunctionalSkills_Mock_Pack_Maths_L2.pdf (90 Pages)
  2. MasterFunctionalSkills_Mock_Pack_English_L2.pdf (86 Pages)
  3. MasterFunctionalSkills_Digital_Skills_Handbook.pdf (88 Pages)
  4. MasterFunctionalSkills_BKSB_Remediation_Workbook.pdf (88 Pages)
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


# =============================================================================
# 1. Mock Pack Maths Level 2 (A4 ~90 Pages)
# =============================================================================
def build_mock_maths_l2():
    print("\n" + "="*70)
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
            ("MS", "Comprehensive Examiner Mark Schemes &amp; Condensed Solutions (24 pages)", "61"),
            ("CERT", "Grade Boundaries &amp; Official Exam Readiness Certificate", "85"),
        ],
        footer=BOOK
    ))

    # p3: Essential Formulae - Geometry & Trigonometry
    p3_body = (
        K.page_title("Level 2 Essential Formulae: Geometry &amp; Shapes", kicker="Formula Reference Sheet &bull; Part 1", badge="F1")
        + K.hero_image(P("construction architectural blueprint measuring tape"), "Geometry calculations underpin construction and engineering exams.", 50)
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
        + K.hero_image(P("adult student calculator exam writing"), "Every intermediate step secures process marks even if your final answer is wrong.", 50)
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
            + K.practice_stack(sec_a[0], start=1)
        )
        pages.append(K.page(p1_b, header=(BOOK, f"Paper {p_idx} &bull; Sec A"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 2 of Paper: Section A Q3 & Q4
        p2_b = (
            K.page_title(f"Mock Paper {p_idx} &bull; Section A (Questions 3 &amp; 4)", kicker=f"Paper {p_idx}: {theme}", badge=f"P{p_idx}.A")
            + K.practice_stack(sec_a[1], start=3)
        )
        pages.append(K.page(p2_b, header=(BOOK, f"Paper {p_idx} &bull; Sec A"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 3 of Paper: Section A Q5 & Check
        p3_b = (
            K.page_title(f"Mock Paper {p_idx} &bull; Section A (Question 5 &bull; Synthesis)", kicker=f"Paper {p_idx}: {theme}", badge=f"P{p_idx}.A")
            + K.practice_stack(sec_a[2], start=5)
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
            + K.hero_image(P(kw1), f"Workplace Scenario: {theme}", 48)
            + K.box_html(
                "<p style='margin:0;'><b>Duration: 1 hour 20 minutes | Marks: 48 Marks | Calculators Permitted.</b><br>"
                "Show formula substitutions clearly. Process marks are awarded for valid mathematical strategies.</p>",
                title="Section B Candidate Instructions"
            )
            + K.practice_stack(sec_b[0], start=6)
        )
        pages.append(K.page(p4_b, header=(BOOK, f"Paper {p_idx} &bull; Sec B"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 5 of Paper: Section B Q8 & Q9
        p5_b = (
            K.page_title(f"Mock Paper {p_idx} &bull; Section B (Questions 8 &amp; 9)", kicker=f"Paper {p_idx}: {theme}", badge=f"P{p_idx}.B")
            + K.practice_stack(sec_b[1], start=8)
        )
        pages.append(K.page(p5_b, header=(BOOK, f"Paper {p_idx} &bull; Sec B"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 6 of Paper: Section B Q10 & Q11
        p6_b = (
            K.page_title(f"Mock Paper {p_idx} &bull; Section B (Questions 10 &amp; 11)", kicker=f"Paper {p_idx}: {theme}", badge=f"P{p_idx}.B")
            + K.hero_image(P(kw2), f"Commercial &amp; Operational Planning: {theme}", 48)
            + K.practice_stack(sec_b[2], start=10)
        )
        pages.append(K.page(p6_b, header=(BOOK, f"Paper {p_idx} &bull; Sec B"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 7 of Paper: Section B Q12 & Q13
        p7_b = (
            K.page_title(f"Mock Paper {p_idx} &bull; Section B (Questions 12 &amp; 13)", kicker=f"Paper {p_idx}: {theme}", badge=f"P{p_idx}.B")
            + K.practice_stack(sec_b[3], start=12)
        )
        pages.append(K.page(p7_b, header=(BOOK, f"Paper {p_idx} &bull; Sec B"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 8 of Paper: Section B Q14 & Q15 (Synthesis)
        p8_b = (
            K.page_title(f"Mock Paper {p_idx} &bull; Section B (Questions 14 &amp; 15 &bull; Synthesis)", kicker=f"Paper {p_idx}: {theme}", badge=f"P{p_idx}.B")
            + K.practice_stack(sec_b[4], start=14)
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
            + K.hero_image(P(photo_kw), lead, 48)
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
        + K.fill_notes("Personal Revision Strategy &amp; Final Mock Target", 22)
    )
    pages.append(K.page(gb_body, header=(BOOK, "Grade Boundaries"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Candidate Formula Quick Reference (1 page)
    mem_body = (
        K.page_title("Candidate Formula &amp; Conversion Quick-Reference", kicker="Essential Non-Calculator &amp; Calculator Memory Aids", badge="MEM")
        + K.hero_image(P("engineering blueprint calculator drafting ruler desk"), "Precision formula recall and unit conversion factors under timed conditions.", 48)
        + K.box_html(
            "<table style='width:100%; border-collapse:collapse; font-size:10.5pt; line-height:1.5;'>"
            "<tr style='background:#f1f5f9;'><th style='padding:6px; text-align:left;'>Category</th><th style='padding:6px; text-align:left;'>Standard Conversion / Formula</th><th style='padding:6px; text-align:left;'>Examiner Note</th></tr>"
            "<tr><td style='padding:6px; border-bottom:1px solid #e2e8f0;'><b>Metric Length &amp; Mass</b></td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>1 km = 1,000 m &bull; 1 m = 100 cm &bull; 1 kg = 1,000 g</td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>Divide to go smaller to larger units.</td></tr>"
            "<tr><td style='padding:6px; border-bottom:1px solid #e2e8f0;'><b>Liquid Volume</b></td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>1 litre = 1,000 ml &bull; 1 m&sup3; = 1,000 litres</td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>1 cm&sup3; = 1 ml capacity.</td></tr>"
            "<tr><td style='padding:6px; border-bottom:1px solid #e2e8f0;'><b>Imperial Approximations</b></td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>1 inch &asymp; 2.5 cm &bull; 1 kg &asymp; 2.2 lbs &bull; 5 miles &asymp; 8 km &bull; 1 gallon &asymp; 4.5 litres</td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>Use given conversion factor if provided.</td></tr>"
            "<tr><td style='padding:6px; border-bottom:1px solid #e2e8f0;'><b>Financial Calculations</b></td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>Gross Pay = Basic + Overtime &bull; Net Pay = Gross &minus; Deductions</td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>VAT @ 20%: Multiplier 1.20 (or divide gross by 1.20).</td></tr>"
            "</table>",
            title="Essential Conversion &amp; Numerical Constants"
        )
        + K.rule_box("Exam Day Golden Calculation Checklist",
                     "<p style='margin:0;'>1. Check units match before calculating (e.g. convert cm to m before finding area).<br>"
                     "2. Always write the unit in the answer box (e.g. &pound;, kg, cm&sup2;, m&sup3;).<br>"
                     "3. Perform reverse operation check for Section A 4-mark questions.<br>"
                     "4. Re-read the question text to verify: Did you answer what was asked?</p>")
        + K.fill_notes("Personal Mental Math Anchors &amp; Formula Memory Reminders", 18)
    )
    pages.append(K.page(mem_body, header=(BOOK, "Formula &amp; Conversion Reference"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Candidate Readiness Certificate (1 page)
    cert_body = (
        K.page_title("Examination Readiness Verification", kicker="Official Milestone Sign-Off", badge="CERT")
        + K.hero_image(P("adult student graduation diploma celebration success"), "Dedication and systematic practice unlock lifelong career progression.", 50)
        + K.box_html(
            "<div style='text-align:center; padding:10px; font-size:11.5pt; line-height:1.5;'>"
            "<p style='margin:0 0 4px 0;'>This certifies that</p>"
            "<p style='font-size:16pt; font-weight:bold; border-bottom:2px solid var(--accent); display:inline-block; min-width:300px; padding-bottom:3px; margin:4px 0;'>&nbsp;</p>"
            "<p style='margin:4px 0;'>has completed all 6 Official-Style Mock Examinations and demonstrated competence across all Pearson Edexcel Functional Skills Mathematics Level 2 standards.</p>"
            "<table style='width:100%; margin-top:12px; font-size:10.5pt; border-collapse:collapse;'>"
            "<tr><td style='text-align:left;'><b>Lead Tutor:</b> Abdul</td><td style='text-align:right;'><b>Date Verified:</b> _______________</td></tr>"
            "<tr><td style='text-align:left;'><b>Average Mock Score:</b> ______ / 64</td><td style='text-align:right;'><b>Exam Centre:</b> Oxford Health OH</td></tr>"
            "</table>"
            "</div>",
            title="Master Functional Skills &bull; Certificate of Exam Readiness"
        )
        + K.fill_notes("Final Examination Tips &amp; Formula Memory Reminders", 18)
    )
    pages.append(K.page(cert_body, header=(BOOK, "Readiness Certificate"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Duplex even-page balance check before back cover
    if (len(pages) + 1) % 2 != 0:
        p_ibc_body = (
            K.page_title("Examination Day Protocol &amp; Equipment Checklist", kicker="Final Revision &bull; Exam Hall Protocol", badge="EXAM")
            + K.box_html(
                "<p>Ensure you are fully equipped and mentally prepared before sitting your Pearson Edexcel Level 2 examination:</p>"
                + K.bullets([
                    "<b>Permitted Equipment:</b> Black ballpoint pens, pencil, eraser, ruler (30 cm), scientific calculator (Section B only), and protractor.",
                    "<b>Section A Non-Calculator (25 mins):</b> Complete all arithmetic using formal column methods and grid multiplication. Perform reverse checks.",
                    "<b>Section B Calculator (1 hr 20 mins):</b> Check display brackets and BIDMAS precedence. Write intermediate method steps for every multi-mark question.",
                    "<b>Units &amp; Rounding:</b> Check whether monetary answers require £ and 2 decimal places (£24.50, not £24.5). State units explicitly.",
                    "<b>Final 5-Minute Audit:</b> Re-read each question stem to verify you have answered what was asked."
                ]),
                title="Pearson Edexcel Functional Skills Mathematics Protocol"
            )
            + K.tip_pair("Keep a running track of your time: spend 1.5 minutes per mark in Section B.",
                         "Never write only the final answer; if you make an arithmetic error, you lose all method marks!",
                         golden_title="Pacing Rule", watch_title="Method Marks")
            + K.fill_notes("Personal Exam Routine &amp; Final Target Notes", 20)
        )
        pages.append(K.page(p_ibc_body, header=(BOOK, "Exam Day Protocol"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # Inside Back Cover & Back Cover
    pages.append(K.back_cover(back_cov))
    pdf_path = DOWNLOADS / "MasterFunctionalSkills_Mock_Pack_Maths_L2.pdf"
    print(f"Total Pages Assembled: {len(pages)}")
    res = K.render_pdf(pages, pdf_path, theme=cover_theme, entry3=False, title="Master Functional Skills - Mock Pack Maths Level 2")
    print(f"Rendered: {res['pdf']} ({len(pages)} pages)")
    return pdf_path

# =============================================================================
# 2. Mock Pack English Level 2 (A4 ~86 Pages)
# =============================================================================
def build_mock_english_l2():
    print("\n" + "="*70)
    print("BUILDING: MasterFunctionalSkills_Mock_Pack_English_L2.pdf")
    print("="*70)

    BOOK = "English L2 Official 5-Mock Exam Pack"
    front_cov = COV / "mock_pack_english_l2_cover_page-1.png"
    back_cov = COV / "mock_pack_english_l2_cover_page-2.png"
    cover_theme = K.theme_from_cover(front_cov)

    pages = []
    used_photos = set()

    def P(kw):
        p = get_photo(kw, "english", used_photos)
        if p:
            used_photos.add(p)
        return p

    def format_text_source(t, default_label="Contextual Article"):
        if isinstance(t, dict):
            source = t.get("source", default_label)
            headline = t.get("headline", "")
            paras = t.get("paragraphs", [])
            body = ""
            if headline:
                body += f"<p style='margin-bottom:8px; font-weight:bold; color:var(--accent); font-size:11pt;'>{headline}</p>"
            body += "".join(f"<p style='margin-bottom:8px;'>{p}</p>" for p in paras)
            return source, body
        else:
            return default_label, str(t)

    # p1: Front Cover
    pages.append(K.front_cover(front_cov))

    # p2: Inside Cover & Examination Matrix
    pages.append(K.inside_cover(
        "Functional Skills English &bull; Level 2",
        "Official 5-Mock Examination Pack &bull; Authentic Reading Inserts, Lined Writing Booklets &amp; Band 4 Model Responses",
        "English Level 2",
        [
            ("1", "Level 2 Reading Strategies &amp; Text Analysis Masterclass", "3"),
            ("2", "Writing Formats, Structural Architecture &amp; Register Matrix", "4"),
            ("3", "Level 2 SPaG Toolkit: Punctuation, Sentence Structures &amp; Flow", "5"),
            ("4", "Diagnostic Performance Tracker &amp; Examination Blueprint", "6"),
            ("M1&ndash;M5", "5 Complete Official-Style Exam Papers (40 pages)", "7"),
            ("WS1&ndash;WS8", "8 Advanced Reading &amp; Writing Masterclasses (8 pages)", "47"),
            ("MS", "Comprehensive Examiner Mark Schemes &amp; Band 4 Exemplars (24 pages)", "55"),
            ("CERT", "Grade Boundaries &amp; Level 2 English Mastery Certificate", "81"),
        ],
        footer=BOOK
    ))

    # p3: Reading Strategies
    p3_body = (
        K.page_title("Level 2 Reading Strategies &amp; Text Analysis", kicker="Paper 1 Masterclass &bull; Section A &amp; B", badge="RD")
        + K.hero_image(P("adult student reading books library research study"), "Critical reading unlocks full marks in both comparison and synthesis questions.", 50)
        + K.box_html(
            "<div style='display:grid; grid-template-columns:1fr 1fr; gap:12px; font-size:11pt;'>"
            "<div><b>Fact vs Opinion:</b> A fact can be proved with empirical data or dates. An opinion contains subjective value judgments ('superior', 'unfortunate', 'must').</div>"
            "<div><b>Implicit Meaning (Subtext):</b> Reading between the lines. Identify connotations, ironies, and subtle undertones in the author's diction.</div>"
            "<div><b>Analyzing Writer's Tone:</b> Identify whether the perspective is objective, cynical, impassioned, satirical, authoritative, or empathetic.</div>"
            "<div><b>Comparative Synthesis:</b> Directly connect Text A and Text B using comparative connectives ('Conversely', 'In parallel', 'Whereas').</div>"
            "</div>",
            title="The 4 Core Reading Competencies (Pearson Criteria)"
        )
        + K.tip_pair("Always quote short, exact phrases (2–5 words) rather than copying entire long sentences.",
                     "Do not just summarize what happened. Explain HOW the language choices affect the reader.",
                     golden_title="Evidence Rule", watch_title="Examiner Trap!")
        + K.fill_notes("Personal Reading Analysis Reminders &amp; Checklist", 24)
    )
    pages.append(K.page(p3_body, header=(BOOK, "Reading Masterclass"), footer=BOOK, page_no=3))

    # p4: Writing Formats & Register
    p4_body = (
        K.page_title("Writing Architecture &amp; The 11 Core Formats", kicker="Paper 2 Masterclass &bull; Format Mastery", badge="WR")
        + K.box_html(
            "<table style='width:100%; border-collapse:collapse; font-size:11pt;'>"
            "<tr style='background:#f1f5f9;'><th style='padding:5px; text-align:left;'>Format</th><th style='padding:5px; text-align:left;'>Mandatory Structural Conventions</th><th style='padding:5px;'>Tone</th></tr>"
            "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0;'><b>1. Formal Letter</b></td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Sender address (top right), recipient address (left), date, Dear Sir/Madam &rarr; Yours faithfully, or Dear Name &rarr; Yours sincerely.</td><td style='text-align:center;'>Formal</td></tr>"
            "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0;'><b>2. Workplace Report</b></td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>To/From/Date/Subject header, numbered sections, bold subheadings, bullet points, recommendations.</td><td style='text-align:center;'>Objective</td></tr>"
            "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0;'><b>3. Professional Email</b></td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Accurate Subject line, formal salutation, cohesive paragraphs, professional sign-off.</td><td style='text-align:center;'>Professional</td></tr>"
            "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0;'><b>4. Public Article</b></td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Engaging headline, byline, subheadings, rhetorical hooks, balanced discussion.</td><td style='text-align:center;'>Engaging</td></tr>"
            "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0;'><b>5. Guidance Leaflet</b></td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Catchy main title, subheadings, bulleted action steps, imperative verbs, contact info.</td><td style='text-align:center;'>Instructive</td></tr>"
            "<tr><td style='padding:5px;'><b>6. Spoken Speech</b></td><td style='padding:5px;'>Direct address ('Ladies and gentlemen', 'colleagues'), rhetorical questions, tri-colon, strong sign-off.</td><td style='text-align:center;'>Rhetorical</td></tr>"
            "</table>",
            title="Pearson Edexcel Format Blueprint Matrix"
        )
        + K.cartoon_tip(get_cartoon("abdul tutor explaining"), "Abdul",
                        "Salutation Trap! If you start with 'Dear Sir or Madam' or 'Dear Hiring Manager', you MUST sign off with 'Yours faithfully'. If you name the recipient ('Dear Mr Taylor'), you MUST sign off with 'Yours sincerely'!")
        + K.fill_notes("Target Writing Formats &amp; Vocabulary To Practice", 22)
    )
    pages.append(K.page(p4_body, header=(BOOK, "Writing Architecture"), footer=BOOK, page_no=4))

    # p5: SPaG Marking Rubric
    p5_body = (
        K.page_title("SPaG Marking Rubric &amp; Band Descriptors", kicker="Spelling, Punctuation &amp; Grammar Standards", badge="SP")
        + K.hero_image(P("writing hand fountain pen signature notes document"), "Accuracy in spelling, punctuation, and syntax secures up to 42% of total writing marks.", 50)
        + K.box_html(
            "<div style='display:grid; grid-template-columns:1fr 1fr; gap:12px; font-size:11pt;'>"
            "<div><b>Band 4 (High Pass / Distinction):</b> Full range of punctuation (. , ; : &mdash; ? !) used with precision. Complex multi-clause sentences punctuated accurately. Rare spelling errors in ambitious vocabulary.</div>"
            "<div><b>Band 3 (Clear Pass):</b> Sentences consistently demarcated with full stops and capital letters. Commas used for clauses. Generally accurate spelling of common workplace terms.</div>"
            "<div><b>Band 2 (Borderline):</b> Occasional comma splices. Basic punctuation mostly correct. Some spelling errors in polysyllabic words.</div>"
            "<div><b>Band 1 (Refer / Fail):</b> Frequent sentence boundary errors (run-on sentences or fragments). Persistent spelling slips obstructing meaning.</div>"
            "</div>",
            title="Official SPaG Mark Bands"
        )
        + K.rule_box("The Three Fatal Punctuation Errors to Eliminate",
                     "<p><b>1. Comma Splices:</b> Never join two complete sentences with just a comma. Use a full stop, semicolon, or coordinating conjunction (and, but, so).<br>"
                     "<b>2. Missing Question Marks:</b> Ensure every rhetorical or direct question concludes with '?'.<br>"
                     "<b>3. Apostrophe of Omission vs Possession:</b> <i>'It's'</i> always means <i>'it is'</i>. The possessive pronoun is <i>'its'</i> (no apostrophe!).</p>")
        + K.fill_notes("Personal SPaG Checklist &amp; Error Avoidance Plan", 22)
    )
    pages.append(K.page(p5_body, header=(BOOK, "SPaG Standards"), footer=BOOK, page_no=5))

    # p6: Diagnostic Performance Tracker
    p6_body = (
        K.page_title("Diagnostic Mock Performance Tracker", kicker="Scores &amp; Progress Monitoring", badge="TR")
        + K.box_html(
            "<table style='width:100%; border-collapse:collapse; font-size:11.5pt; text-align:center;'>"
            "<tr style='background:#f1f5f9;'><th style='padding:6px; text-align:left;'>Paper</th><th>Reading (/30)</th><th>Writing (/30)</th><th>Total (/60)</th><th>% Score</th><th>Status</th><th>Date</th></tr>"
            + "".join(f"<tr><td style='padding:6px; border-bottom:1px solid #e2e8f0; text-align:left;'><b>Mock Paper {i}</b></td>"
                      f"<td style='border-bottom:1px solid #e2e8f0;'>&nbsp;&nbsp;&nbsp;&nbsp;/30</td>"
                      f"<td style='border-bottom:1px solid #e2e8f0;'>&nbsp;&nbsp;&nbsp;&nbsp;/30</td>"
                      f"<td style='border-bottom:1px solid #e2e8f0;'><b>&nbsp;&nbsp;&nbsp;&nbsp;/60</b></td>"
                      f"<td style='border-bottom:1px solid #e2e8f0;'>&nbsp;&nbsp;&nbsp;&nbsp;%</td>"
                      f"<td style='border-bottom:1px solid #e2e8f0;'>[ &nbsp; ] Pass</td>"
                      f"<td style='border-bottom:1px solid #e2e8f0;'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td></tr>"
                      for i in range(1, 6))
            + "</table>",
            title="Pearson Edexcel Level 2 Pass Benchmark: 36–39 Marks (approx. 60–65%)"
        )
        + K.fill_notes("Reading &amp; Writing Target Skills for Tutoring Sessions", 30)
    )
    pages.append(K.page(p6_body, header=(BOOK, "Score Tracker"), footer=BOOK, page_no=6))

    # pp7–p46: 5 Complete Official Exam Papers (8 pages per paper = 40 pages)
    p_curr = 7
    for p_idx, mock in enumerate(ssc.ENGLISH_L2_MOCKS, start=1):
        m_title = mock["title"]
        kw1 = mock["kw1"]
        kw2 = mock["kw2"]
        text_a = mock["text_a"]
        text_b = mock["text_b"]
        q1_5 = mock["reading_q1_5"]
        q6_9 = mock["reading_q6_9"]
        w_t1 = mock["writing_t1"]
        w_t2 = mock["writing_t2"]

        # Page 1 of Mock: Reading Insert Text A
        src_a, body_a = format_text_source(text_a, "Contextual Source Text A")
        p1_b = (
            K.page_title(f"Mock Paper {p_idx} &bull; Reading Text A", kicker=f"Paper {p_idx}: {m_title}", badge=f"P{p_idx}.A")
            + K.hero_image(P(kw1), f"Contextual Source Text: {m_title}", 40)
            + K.box_html(
                f"<div style='font-size:10.5pt; line-height:1.5; text-align:justify;'>{body_a}</div>",
                title=f"Source Text A &bull; {src_a}"
            )
        )
        pages.append(K.page(p1_b, header=(BOOK, f"Paper {p_idx} &bull; Text A"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 2 of Mock: Reading Insert Text B
        src_b, body_b = format_text_source(text_b, "Comparative Source Text B")
        p2_b = (
            K.page_title(f"Mock Paper {p_idx} &bull; Reading Text B", kicker=f"Paper {p_idx}: {m_title}", badge=f"P{p_idx}.B")
            + K.hero_image(P(kw2), f"Comparative Source Text: {m_title}", 40)
            + K.box_html(
                f"<div style='font-size:10.5pt; line-height:1.5; text-align:justify;'>{body_b}</div>",
                title=f"Source Text B &bull; {src_b}"
            )
        )
        pages.append(K.page(p2_b, header=(BOOK, f"Paper {p_idx} &bull; Text B"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 3 of Mock: Reading Questions 1 to 5
        q1_5_html = "".join(
            f"<div style='margin-bottom:2mm; padding:2mm 3.5mm; background:#f8fafc; border-left:3.5mm solid var(--accent); border-radius:4px;'>"
            f"<div style='font-size:10pt; line-height:1.35;'><b>Q{q_i+1}:</b> {q['q']} <span style='float:right; font-weight:bold; color:var(--accent);'>[{q['marks']} Marks]</span></div>"
            f"<div class='aline' style='height:5.5mm; border-bottom:1px solid #cbd5e1; margin-top:1.5mm;'></div>"
            f"<div class='aline' style='height:5.5mm; border-bottom:1px solid #cbd5e1; margin-top:1.5mm;'></div>"
            f"</div>"
            for q_i, q in enumerate(q1_5)
        )
        p3_b = (
            K.page_title(f"Mock Paper {p_idx} &bull; Reading Questions (Q1&ndash;Q5)", kicker="Paper 1: Reading Section A &bull; Text Analysis", badge=f"P{p_idx}.R1")
            + q1_5_html
            + K.fill_notes("Candidate Working Notes &amp; Evidence Log", 18)
        )
        pages.append(K.page(p3_b, header=(BOOK, f"Paper {p_idx} &bull; Reading Q1-5"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 4 of Mock: Reading Questions 6 to 9 (Comparison & Synthesis)
        q6_9_html = "".join(
            f"<div style='margin-bottom:2mm; padding:2mm 3.5mm; background:#f8fafc; border-left:3.5mm solid var(--accent); border-radius:4px;'>"
            f"<div style='font-size:10pt; line-height:1.35;'><b>Q{q_i+6}:</b> {q['q']} <span style='float:right; font-weight:bold; color:var(--accent);'>[{q['marks']} Marks]</span></div>"
            f"<div class='aline' style='height:5.5mm; border-bottom:1px solid #cbd5e1; margin-top:1.5mm;'></div>"
            f"<div class='aline' style='height:5.5mm; border-bottom:1px solid #cbd5e1; margin-top:1.5mm;'></div>"
            f"</div>"
            for q_i, q in enumerate(q6_9)
        )
        p4_b = (
            K.page_title(f"Mock Paper {p_idx} &bull; Reading Questions (Q6&ndash;Q9)", kicker="Paper 1: Reading Section B &bull; Comparative Synthesis", badge=f"P{p_idx}.R2")
            + q6_9_html
            + K.box_html(
                f"<div style='display:flex; justify-content:space-between; font-weight:bold; font-size:10.5pt;'>"
                f"<span>Reading Total Marks: ______ / 30</span>"
                f"<span>Time Expended: ______ mins</span>"
                f"</div>",
                title="Reading Paper Candidate Sign-Off"
            )
            + K.fill_notes("Comparative Synthesis Plan &amp; Working Notes", 18)
        )
        pages.append(K.page(p4_b, header=(BOOK, f"Paper {p_idx} &bull; Reading Q6-9"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 5 of Mock: Writing Task 1
        p5_b = (
            K.page_title(f"Mock Paper {p_idx} &bull; Writing Task 1", kicker=f"Paper 2: Writing &bull; {w_t1['type']}", badge=f"P{p_idx}.W1")
            + K.box_html(
                f"<div style='font-size:11pt; line-height:1.45;'>"
                f"<p style='margin:0 0 6px 0;'><b>Format:</b> {w_t1['type']} &emsp;|&emsp; <b>Target Marks:</b> {w_t1['marks']} Marks</p>"
                f"<p style='margin:0 0 6px 0;'><b>Context Brief:</b> {w_t1['scenario']}</p>"
                f"<p style='margin:0;'><b>Task Prompt:</b> {w_t1['task']}</p>"
                f"</div>",
                title=f"Task 1 Assessment Brief &bull; [{w_t1['marks']} Marks]"
            )
            + K.checklist_box(f"Mandatory Format &amp; Content Checklist &bull; {w_t1['type']}",
                             [f"Audience: Match formal register to {w_t1['type']}",
                              "Format: Use correct layout, salutation, subheadings or bullet points",
                              "Content: Address all prompt bullet points with developed detail",
                              "SPaG: Maintain accurate punctuation, complex sentences and spelling"])
            + K.fill_notes(f"Candidate Writing Booklet &bull; Task 1 (Page 1 of 2)", 38)
        )
        pages.append(K.page(p5_b, header=(BOOK, f"Paper {p_idx} &bull; Task 1"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 6 of Mock: Writing Task 1 Continuation
        p6_b = (
            K.page_title(f"Mock Paper {p_idx} &bull; Writing Task 1 (Continuation)", kicker=f"Paper 2: Writing &bull; {w_t1['type']}", badge=f"P{p_idx}.W1")
            + K.fill_notes("Candidate Writing Booklet &bull; Task 1 (Page 2 of 2)", 150)
            + K.box_html(
                f"<div style='display:flex; justify-content:space-between; font-weight:bold; font-size:11pt;'>"
                f"<span>Task 1 Marks: Form &amp; Content: ____/12 &emsp; SPaG: ____/7</span>"
                f"<span>Total: ____ / {w_t1['marks']}</span>"
                f"</div>",
                title="Task 1 Examiner Assessment"
            )
        )
        pages.append(K.page(p6_b, header=(BOOK, f"Paper {p_idx} &bull; Task 1 End"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 7 of Mock: Writing Task 2
        p7_b = (
            K.page_title(f"Mock Paper {p_idx} &bull; Writing Task 2", kicker=f"Paper 2: Writing &bull; {w_t2['type']}", badge=f"P{p_idx}.W2")
            + K.box_html(
                f"<div style='font-size:11pt; line-height:1.45;'>"
                f"<p style='margin:0 0 6px 0;'><b>Format:</b> {w_t2['type']} &emsp;|&emsp; <b>Target Marks:</b> {w_t2['marks']} Marks</p>"
                f"<p style='margin:0 0 6px 0;'><b>Context Brief:</b> {w_t2['scenario']}</p>"
                f"<p style='margin:0;'><b>Task Prompt:</b> {w_t2['task']}</p>"
                f"</div>",
                title=f"Task 2 Assessment Brief &bull; [{w_t2['marks']} Marks]"
            )
            + K.checklist_box(f"Mandatory Format &amp; Rhetorical Checklist &bull; {w_t2['type']}",
                             [f"Audience: Match register to {w_t2['type']}",
                              "Format: Clear headings, subheadings, bullet points, or rhetorical opening",
                              "Persuasion: Deploy AFOREST devices (facts, emotive words, tri-colon)",
                              "SPaG: Accurate sentence boundaries and zero comma splices"])
            + K.fill_notes(f"Candidate Writing Booklet &bull; Task 2 (Page 1 of 2)", 38)
        )
        pages.append(K.page(p7_b, header=(BOOK, f"Paper {p_idx} &bull; Task 2"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 8 of Mock: Writing Task 2 Continuation & Summary
        p8_b = (
            K.page_title(f"Mock Paper {p_idx} &bull; Writing Task 2 (Continuation)", kicker=f"Paper 2: Writing &bull; {w_t2['type']}", badge=f"P{p_idx}.W2")
            + K.fill_notes("Candidate Writing Booklet &bull; Task 2 (Page 2 of 2)", 140)
            + K.box_html(
                f"<div style='display:flex; justify-content:space-between; font-weight:bold; font-size:11pt;'>"
                f"<span>Task 2 Marks: Form &amp; Content: ____/9 &emsp; SPaG: ____/6</span>"
                f"<span>Total: ____ / {w_t2['marks']}</span>"
                f"<span>Paper {p_idx} Total: ____ / 60</span>"
                f"</div>",
                title="Writing Paper Summary &amp; Examiner Sign-Off"
            )
        )
        pages.append(K.page(p8_b, header=(BOOK, f"Paper {p_idx} &bull; Summary"), footer=BOOK, page_no=p_curr))
        p_curr += 1


    # pp55–p62: Masterclass: The 11 Core Writing Formats & Band 4 Archetypes (8 pages)
    writing_formats_data = [
        ("Format Archetype 1 &bull; Formal Letters (Complaint &amp; Application)", "WF1",
         "Mastering formal sender/recipient headers, date, salutation, tone, and complimentary close.",
         "writing document contract legal notes fountain pen",
         "<b>Structural Anatomy:</b> Sender address top right; recipient address top left; date beneath; formal salutation (<code>Dear Sir/Madam</code> paired with <code>Yours faithfully</code>; named recipient <code>Dear Ms Jenkins</code> paired with <code>Yours sincerely</code>).<br><br>"
         "<b>Band 4 Content Strategy:</b> (1) Opening state the precise purpose of writing. (2) Provide factual background chronology. (3) State the impact on the client/applicant. (4) Conclude with a definitive call to action and deadline.",
         "Format 1 Band 4 Checklist &amp; Layout Model",
         "<b>Checklist:</b> [ ] Formal addresses aligned &bull; [ ] Formal salutation &amp; matching sign-off &bull; [ ] Zero informal contractions &bull; [ ] Precise chronology &bull; [ ] Remedial deadline.<br><br>"
         "<b>Model Opening:</b> <i>'I am writing to formally register my dissatisfaction with the emergency heating repairs conducted at our residential facility on 12 October 2026...'</i>"),

        ("Format Archetype 2 &bull; Formal Workplace Recommendation Reports", "WF2",
         "Executive document design: structured headers, findings, data tables, and risk mitigations.",
         "corporate business report analysis charts desk",
         "<b>Structural Anatomy:</b> Standard memo/report header (To, From, Date, Subject); numbered sections (1. Executive Summary, 2. Current Operational Bottlenecks, 3. Options Appraisal, 4. Risk Mitigation Matrix, 5. Definitive Recommendations).<br><br>"
         "<b>Band 4 Tone Strategy:</b> Maintain third-person objective register (<i>'The data indicates...'</i> rather than <i>'I think...'</i>). Use passive voice strategically to emphasize findings.",
         "Format 2 Band 4 Checklist &amp; Layout Model",
         "<b>Checklist:</b> [ ] Formal 4-part memo header &bull; [ ] Numbered subheadings &bull; [ ] Bulleted data points &bull; [ ] Balanced risk analysis &bull; [ ] Specific costed recommendations.<br><br>"
         "<b>Model Section:</b> <i>'3.2 Options Appraisal: Transitioning to cloud-hosted telematics incurs a one-off setup cost of &pound;12,400 but eliminates annual server licensing fees of &pound;6,200...'</i>"),

        ("Format Archetype 3 &bull; Business Proposals &amp; Funding Bids", "WF3",
         "Persuasive commercial proposals: community need, cost-benefit analysis, and deliverable milestones.",
         "business handshake deal partnership contract desk",
         "<b>Structural Anatomy:</b> Clear project title, organizational background, statement of demonstrated need, project deliverables with timeline milestones, budget breakdown table, and legacy sustainability plan.<br><br>"
         "<b>Band 4 Persuasive Strategy:</b> Weave qualitative community impact with quantitative fiscal metrics. Highlight statutory compliance (e.g. Equality Act, Health &amp; Safety).",
         "Format 3 Band 4 Checklist &amp; Layout Model",
         "<b>Checklist:</b> [ ] Compelling proposal title &bull; [ ] Demonstrated need with census/local data &bull; [ ] Phased delivery milestones &bull; [ ] Itemized budget table &bull; [ ] Volunteer legacy.<br><br>"
         "<b>Model Extract:</b> <i>'This capital grant will directly unlock 350 weekly youth mentoring hours across three high-deprivation wards, yielding a projected 24% reduction in local antisocial incidents...'</i>"),

        ("Format Archetype 4 &bull; Public Newspaper &amp; Magazine Articles", "WF4",
         "Engaging journalistic writing: headline, byline, hook, balanced perspectives, and call to action.",
         "newspaper printing press journalism article layout",
         "<b>Structural Anatomy:</b> Snappy, memorable headline (using alliteration, rhyme, or pun); author byline; dramatic narrative hook in paragraph 1; balanced debate presenting opposing viewpoints; concluding synthesis and inspiring forward look.<br><br>"
         "<b>Band 4 Rhetorical Strategy:</b> Use sensory imagery, tri-colon listings, rhetorical questions, and varied sentence lengths to maintain vibrant reader interest.",
         "Format 4 Band 4 Checklist &amp; Layout Model",
         "<b>Checklist:</b> [ ] Creative headline &bull; [ ] Journalistic byline &bull; [ ] Vivid opening hook &bull; [ ] Balanced stakeholder quotes &bull; [ ] Concluding call to action.<br><br>"
         "<b>Model Hook:</b> <i>'Step onto our high street on any rain-soaked Monday, and you will witness a quiet revolution taking place behind the Victorian shopfronts...'</i>"),

        ("Format Archetype 5 &bull; Persuasive Public Speeches", "WF5",
         "Oral rhetoric: direct audience address, emphatic repetition, pathos, and powerful call to action.",
         "podium microphone speech conference public speaking",
         "<b>Structural Anatomy:</b> Welcoming audience acknowledgment (<i>'Good evening councillors and fellow residents...'</i>); personal stake/connection; statement of the crisis; triadic arguments; rebuttal of naysayers; soaring final appeal.<br><br>"
         "<b>Band 4 Spoken Register Strategy:</b> Written for the ear, not the eye! Use short punchy sentences for emotional weight, pauses (indicated by dashes), and anaphora (repeated opening phrases).",
         "Format 5 Band 4 Checklist &amp; Layout Model",
         "<b>Checklist:</b> [ ] Explicit audience address &bull; [ ] Anaphora &amp; rhetorical repetition &bull; [ ] Triadic list &bull; [ ] Emotive personal appeal &bull; [ ] Definite rousing call to action.<br><br>"
         "<b>Model Crescendo:</b> <i>'We have spoken. We have petitioned. We have waited. The time for empty council platitudes has ended; the time for decisive funding is NOW.'</i>"),

        ("Format Archetype 6 &bull; Informative Guidance Leaflets &amp; Brochures", "WF6",
         "Public information layout: catchy subheadings, bulleted guidance, FAQ boxes, and contact directory.",
         "brochure leaflet graphic design typography print",
         "<b>Structural Anatomy:</b> Title banner with clear purpose; introductory paragraph outlining who the leaflet is for; categorized advice subsections with imperative action verbs; bullet points for rapid scanning; emergency contacts box.<br><br>"
         "<b>Band 4 Clarity Strategy:</b> Direct address using second person (<i>'You should...'</i>); clear conditional rules (<i>'If you experience X, immediately contact Y'</i>); plain English without confusing jargon.",
         "Format 6 Band 4 Checklist &amp; Layout Model",
         "<b>Checklist:</b> [ ] Distinct leaflet banner &bull; [ ] Short scannable paragraphs &bull; [ ] Bulleted action steps &bull; [ ] Highlighted safety warnings &bull; [ ] Helpdesk contact details.<br><br>"
         "<b>Model Advice Box:</b> <i>'What to do in an electrical outage: (1) Unplug sensitive medical equipment. (2) Keep refrigerator doors closed. (3) Report the outage to 105 immediately.'</i>"),

        ("Format Archetype 7 &bull; Critical Reviews &amp; Evaluations", "WF7",
         "Evaluative writing: rating criteria, balanced strengths and weaknesses, and target audience verdict.",
         "laptop review stars rating consumer test technology",
         "<b>Structural Anatomy:</b> Item/service title and star rating; context of the review; criteria-by-criteria evaluation (e.g. Value for Money, Reliability, Usability, Customer Service); balanced drawbacks; definitive final verdict.<br><br>"
         "<b>Band 4 Evaluative Strategy:</b> Sophisticated evaluative adjectives (<i>'exemplary', 'cumbersome', 'substandard', 'unrivalled'</i>); balanced comparison against market competitors.",
         "Format 7 Band 4 Checklist &amp; Layout Model",
         "<b>Checklist:</b> [ ] Star rating or score badge &bull; [ ] Multi-criteria evaluation &bull; [ ] Specific comparative evidence &bull; [ ] Balanced pros &amp; cons &bull; [ ] Clear target audience recommendation.<br><br>"
         "<b>Model Verdict:</b> <i>'While the software dashboard suffers from an initial steep learning curve, its automated invoicing tools make it an indispensable investment for expanding SMEs.'</i>"),

        ("Format Archetypes 8&ndash;11 &bull; Workplace Emails, Memos, Blogs &amp; Press Releases", "WF8",
         "Agile digital communications: subject syntax, netiquette, SEO web copy, and news release structure.",
         "office computer keyboard typing corporate communication",
         "<b>Formats 8 &amp; 9: Workplace Emails &amp; Internal Memos:</b> Clear prefix tag <code>[ACTION]</code>, professional salutation, 3-tier body (Context &rarr; Detail &rarr; Required Action), polite professional sign-off.<br><br>"
         "<b>Formats 10 &amp; 11: Web Blogs &amp; Press Releases:</b> Blogs require engaging conversational hooks and reader comments prompts. Press Releases mandate <code>FOR IMMEDIATE RELEASE</code>, embargo date, boilerplate 'Notes to Editors', and media contact.",
         "Formats 8-11 Band 4 Checklist &amp; Core Standards",
         "<b>Checklist:</b> [ ] Email: Clear subject with deadline &bull; [ ] Memo: Standard 4 headers &bull; [ ] Blog: Conversational register &bull; [ ] Press Release: <code>FOR IMMEDIATE RELEASE</code> and media contact details.<br><br>"
         "<b>Model Press Header:</b> <i>'FOR IMMEDIATE RELEASE &bull; 14 October 2026 &bull; Regional Skills Hub Launches &pound;2m Green Apprenticeship Initiative. Media Contact: press@skillshub.org.uk'</i>")
    ]

    for wf_title, badge, lead, photo_kw, theory_html, box_title, box_html in writing_formats_data:
        wf_body = (
            K.page_title(wf_title, kicker="Pearson Edexcel Level 2 Writing Formats Masterclass", badge=badge)
            + K.hero_image(P(photo_kw), lead, 48)
            + K.box_html(f"<div style='font-size:10.5pt; line-height:1.45;'>{theory_html}</div>", title="Format Structural Architecture &amp; Examiner Criteria")
            + K.box_html(f"<div style='font-size:10.5pt; line-height:1.45;'>{box_html}</div>", title=box_title)
            + K.fill_notes("Personal Writing Anchors &amp; Sentence Starters", 22)
        )
        pages.append(K.page(wf_body, header=(BOOK, f"{badge} &bull; Writing Format"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # pp47–p54: 8 Advanced Reading & Writing Masterclasses (8 pages)
    masterclasses = [
        ("Formal Letters &amp; Reports: Governance &amp; Executive Register", "ws1",
         "Mastering formal conventions, professional layout, and executive decision-making tone.",
         "business executive meeting board room presentation",
         "<b>Structural Anatomy:</b> A formal report requires a numbered hierarchical structure: 1. Executive Summary, 2. Current Context &amp; Findings, 3. Risk Assessment, 4. Strategic Recommendations.<br>"
         "<b>Register Rule:</b> Maintain passive voice where appropriate to project institutional objectivity: write <i>'An investigation was conducted'</i> rather than <i>'I checked'</i>.<br>"
         "<b>Common Pitfall:</b> Mixing informal colloquialisms or omitting the recommendations section.",
         "Mastery Drill: Convert three informal observations into formal executive report statements with passive phrasing."),
        ("Persuasive Articles &amp; Editorials: Rhetorical Architecture", "ws2",
         "Deploying AFOREST rhetorical devices to captivate and convince diverse audiences.",
         "journalism newspaper press writer article",
         "<b>The AFOREST Matrix:</b> Alliteration, Facts/Figures, Opinion, Rhetorical questions, Emotive language, Statistics, Tri-colon (Rule of three).<br>"
         "<b>Structural Hook:</b> Open with an evocative scene or provocative rhetorical question to draw readers immediately into the debate.<br>"
         "<b>Balanced Argumentation:</b> Acknowledge counter-arguments respectfully before dismantling them with verifiable evidence.",
         "Mastery Drill: Draft a 120-word persuasive opening paragraph for a local newspaper arguing for investment in community evening courses."),
        ("Professional Emails &amp; Memos: Clarity &amp; Workplace Etiquette", "ws3",
         "Delivering concise, actionable workplace communications without ambiguity.",
         "office worker typing laptop email desk",
         "<b>Subject Line Precision:</b> Subject lines must state the exact action required and deadline: <code>ACTION REQUIRED: Q3 Staff Rota Approval by Friday 17:00</code>.<br>"
         "<b>The Three-Paragraph Rule:</b> (1) Reason for writing and context. (2) Detailed data, requests, or bulleted requirements. (3) Action timeline and polite sign-off.<br>"
         "<b>Salutations:</b> Always tailor to professional hierarchy.",
         "Mastery Drill: Draft a 100-word formal workplace memo notifying team members of mandatory health and safety software training."),
        ("Guidance Leaflets &amp; Public Information Handouts", "ws4",
         "Designing readable, accessible informational guides with clear visual signposts.",
         "graphic designer brochure layout printing",
         "<b>Design Architecture:</b> Guidance leaflets require high visual scannability: bold headings, succinct bulleted instructions, callout tip boxes, and numbered procedural steps.<br>"
         "<b>Imperative Language:</b> Use direct command verbs to instruct the public: <i>'Wash hands thoroughly'</i>, <i>'Submit registration before October 15'</i>.<br>"
         "<b>Accessibility:</b> Avoid dense walls of text; keep sentences under 20 words.",
         "Mastery Drill: Create a 4-point bulleted guidance section advising workers on safe desk ergonomics and screen break intervals."),
        ("Spoken Speeches &amp; Presentations: Voice, Cadence &amp; Impact", "ws5",
         "Crafting rhythmic spoken texts that resonate with live audiences.",
         "speaker speech podium conference presentation audience",
         "<b>Spoken Register:</b> A speech is written for the ear, not the eye. Use short punchy sentences, rhythmic cadence, and purposeful repetition (anaphora).<br>"
         "<b>Stage Directions:</b> Indicate pauses, vocal emphasis, and audience acknowledgment.<br>"
         "<b>Call to Action:</b> End with an inspiring, memorable pledge that leaves the room motivated to act.",
         "Mastery Drill: Write a 100-word concluding speech address to apprentices celebrating their qualification milestone."),
        ("Critical Reading: Detecting Bias, Tone &amp; Implicit Meaning", "ws6",
         "Uncovering hidden agendas, rhetorical slants, and subtext in source texts.",
         "adult student library books reading magnifying glass",
         "<b>Detecting Bias:</b> Look for what is OMITTED as well as what is included. Examine loaded adjectives, unbalanced source selection, and vested interests.<br>"
         "<b>Analyzing Subtext:</b> Examine figurative idioms: <i>'The board kicked the can down the road'</i> implies procrastination and evasion.<br>"
         "<b>Tone Spectrum:</b> Distinguish between condescending, satirical, impassioned, and impartial stances.",
         "Mastery Drill: Analyze an excerpt from an advertisement claiming 95% satisfaction; identify two linguistic indicators of commercial bias."),
        ("Comparative Synthesis: Seamlessly Integrating Two Source Texts", "ws7",
         "Structuring high-scoring comparative paragraphs across Text A and Text B.",
         "collaborative team working office desk documents",
         "<b>The Comparative Formula:</b> Point &rarr; Evidence from Text A &rarr; Comparative Connective &rarr; Evidence from Text B &rarr; Evaluative Synthesis.<br>"
         "<b>Connective Repertoire:</b> 'Similarly', 'In sharp contrast', 'While Text A highlights...', 'Text B corroborates this by...'.<br>"
         "<b>Pitfall:</b> Writing about Text A for a page, then Text B for a page without comparing.",
         "Mastery Drill: Draft a comparative synthesis paragraph contrasting the benefits and drawbacks of remote work cited in two source extracts."),
        ("Structural Architecture: Paragraph Cohesion &amp; Discourse Markers", "ws8",
         "Connecting complex ideas smoothly across multi-page written assignments.",
         "architect blueprint drafting pen planning",
         "<b>Discourse Markers:</b> Use sophisticated transitions to guide the reader: 'Furthermore', 'Consequently', 'Notwithstanding', 'In summary'.<br>"
         "<b>Topic Sentences:</b> The first sentence of every paragraph must state its central theme clearly.<br>"
         "<b>Sentence Variety:</b> Alternate simple sentences for impact with complex compound sentences for nuanced reasoning.",
         "Mastery Drill: Connect three disjointed points into a fluent, cohesive 120-word paragraph using advanced discourse markers.")
    ]

    for ws_title, badge, lead, photo_kw, theory_html, drill_title in masterclasses:
        ws_body = (
            K.page_title(ws_title, kicker="Advanced English Level 2 Masterclass", badge=badge.upper())
            + K.hero_image(P(photo_kw), lead, 48)
            + K.box_html(f"<div style='font-size:10.5pt; line-height:1.45;'>{theory_html}</div>", title="Core Technique &amp; Linguistic Architecture")
            + K.box_html(f"<div style='font-size:11pt; font-weight:bold; color:var(--accent);'>{drill_title}</div>", title="Hands-On Masterclass Drill")
            + K.fill_notes("Candidate Working Lines &bull; Masterclass Response", 55)
        )
        pages.append(K.page(ws_body, header=(BOOK, "Masterclass"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # Back matter reference section (via K.ref_pages)
    ref_blocks = []
    for m_idx in range(1, 7):
        for title_str, sol_html in ssr.ENGLISH_L2_MOCK_SOLUTIONS[m_idx]:
            ref_blocks.append(K.ref_block(title_str, sol_html))

    gloss_html = "".join(f"<dl><dt>{t}</dt><dd>{d}</dd></dl>" for t, d in ssr.ENGLISH_L2_GLOSSARY)
    ref_blocks.append(K.ref_block("Linguistic &amp; Literary Glossary of Terms", gloss_html))

    ix_html = ""
    for letter, entries in ssr.ENGLISH_L2_INDEX:
        items = "".join(f"<div class='ix'><span>{t}</span><span>{p}</span></div>" for t, p in entries)
        ix_html += f"<div class='ix-letter'>{letter}</div>{items}"
    ref_blocks.append(K.ref_block("Curriculum &amp; Examination Index", ix_html))

    ref_page_list = K.ref_pages("Official Mark Schemes &amp; Exemplar Directory", ref_blocks,
                                BOOK, start_page=p_curr, subtitle="Complete Reading Solutions &amp; Full Band 4 Writing Models",
                                cols=2, theme=cover_theme, notes_title="Candidate Error Analysis &amp; SPaG Checklist")
    pages.extend(ref_page_list)
    p_curr += len(ref_page_list)

    # Grade Boundaries & Scaling (1 page)
    gb_body = (
        K.page_title("Official Grade Boundaries &amp; Scaling", kicker="Pearson Edexcel Standards", badge="GB")
        + K.box_html(
            "<table style='width:100%; border-collapse:collapse; font-size:11.5pt; text-align:center;'>"
            "<tr style='background:#f1f5f9;'><th style='padding:8px; text-align:left;'>Examination Series</th><th>Reading (/30)</th><th>Writing (/30)</th><th>Pass Boundary (/60)</th><th>Pass %</th></tr>"
            "<tr><td style='padding:8px; border-bottom:1px solid #e2e8f0; text-align:left;'>Standard Series 1</td><td>18</td><td>19</td><td><b>37</b></td><td>61.7%</td></tr>"
            "<tr><td style='padding:8px; border-bottom:1px solid #e2e8f0; text-align:left;'>Standard Series 2</td><td>19</td><td>19</td><td><b>38</b></td><td>63.3%</td></tr>"
            "<tr><td style='padding:8px; border-bottom:1px solid #e2e8f0; text-align:left;'>Higher Difficulty Series 3</td><td>17</td><td>19</td><td><b>36</b></td><td>60.0%</td></tr>"
            "<tr><td style='padding:8px; border-bottom:1px solid #e2e8f0; text-align:left;'>Target Mastery Benchmark</td><td>24</td><td>24</td><td><b>48</b></td><td>80.0%</td></tr>"
            "</table>",
            title="Pearson Edexcel Functional Skills English Level 2 Scaling"
        )
        + K.cartoon_tip(get_cartoon("priya tutor writing notes"), "Priya",
                        "Target 20 marks in Reading and 20 marks in Writing. This safely clears the pass threshold with a comfortable margin on both papers!")
        + K.fill_notes("Personal English Revision Strategy &amp; Final Mock Target", 45)
    )
    pages.append(K.page(gb_body, header=(BOOK, "Grade Boundaries"), footer=BOOK, page_no=p_curr))
    p_curr += 1

# Candidate Timing & Mark Allocation Blueprint (1 page)
    timing_body = (
        K.page_title("Level 2 Exam Timing &amp; Mark Allocation Strategy", kicker="Executive Examination Blueprint", badge="TIME")
        + K.hero_image(P("clock wristwatch business meeting time management"), "Strategic time budgeting and mark-to-minute calibration.", 45)
        + K.box_html(
            "<table style='width:100%; border-collapse:collapse; font-size:10.5pt; line-height:1.5;'>"
            "<tr style='background:#f1f5f9;'><th style='padding:6px; text-align:left;'>Examination Section</th><th style='padding:6px; text-align:left;'>Marks Available</th><th style='padding:6px; text-align:left;'>Recommended Time</th><th style='padding:6px; text-align:left;'>Pacing &amp; Strategy Rule</th></tr>"
            "<tr><td style='padding:6px; border-bottom:1px solid #e2e8f0;'><b>Reading &bull; Source Skim &amp; Scan</b></td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>&mdash;</td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>10 minutes</td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>Skim Text A &amp; Text B headlines, subheadings, and lead paragraphs first.</td></tr>"
            "<tr><td style='padding:6px; border-bottom:1px solid #e2e8f0;'><b>Reading &bull; Questions 1&ndash;9</b></td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>30 marks</td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>40 minutes</td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>Allocate ~1.3 minutes per mark. Save Q7-Q9 synthesis for last.</td></tr>"
            "<tr><td style='padding:6px; border-bottom:1px solid #e2e8f0;'><b>Writing &bull; Task 1 (Formal Report/Letter)</b></td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>21 marks</td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>35 minutes</td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>Spend 5m planning, 25m drafting, 5m proofreading format &amp; SPaG.</td></tr>"
            "<tr><td style='padding:6px; border-bottom:1px solid #e2e8f0;'><b>Writing &bull; Task 2 (Public Article/Speech)</b></td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>15 marks</td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>25 minutes</td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>Spend 3m planning, 18m drafting, 4m proofreading sentence flow.</td></tr>"
            "<tr><td style='padding:6px; border-bottom:1px solid #e2e8f0;'><b>Final Proofreading &amp; Audit</b></td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>&mdash;</td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>10 minutes</td><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>Check every sentence ends with full stop; audit homophones &amp; commas.</td></tr>"
            "</table>",
            title="Pearson Edexcel Level 2 Time Management Blueprint (120 Minutes Total)"
        )
        + K.rule_box("Exam Hall Golden Pacing Principles",
                     "<p style='margin:0;'>1. Never leave early! Spend remaining minutes reviewing Task 1 and Task 2 for missing punctuation.<br>2. Aim for 250&ndash;300 words on Task 1 and 200&ndash;250 words on Task 2.<br>3. Always weave direct quotations smoothly into your comparative reading answers.</p>")
        + K.fill_notes("Personal Exam Routine &amp; Warm-Up Checklist", 22)
    )
    pages.append(K.page(timing_body, header=(BOOK, "Timing Blueprint"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Candidate Readiness Certificate (1 page)
    cert_body = (
        K.page_title("Examination Readiness Verification", kicker="Official Milestone Sign-Off", badge="CERT")
        + K.hero_image(P("adult student graduation diploma celebration success"), "Excellence in communication opens professional horizons across all careers.", 50)
        + K.box_html(
            "<div style='text-align:center; padding:10px; font-size:11.5pt; line-height:1.5;'>"
            "<p style='margin:0 0 4px 0;'>This certifies that</p>"
            "<p style='font-size:16pt; font-weight:bold; border-bottom:2px solid var(--accent); display:inline-block; min-width:300px; padding-bottom:3px; margin:4px 0;'>&nbsp;</p>"
            "<p style='margin:4px 0;'>has completed all 5 Official-Style Mock Examinations and demonstrated mastery across all Pearson Edexcel Functional Skills English Level 2 standards.</p>"
            "<table style='width:100%; margin-top:12px; font-size:10.5pt; border-collapse:collapse;'>"
            "<tr><td style='text-align:left;'><b>Lead Tutor:</b> Abdul</td><td style='text-align:right;'><b>Date Verified:</b> _______________</td></tr>"
            "<tr><td style='text-align:left;'><b>Average Mock Score:</b> ______ / 60</td><td style='text-align:right;'><b>Exam Centre:</b> Oxford Health OH</td></tr>"
            "</table>"
            "</div>",
            title="Master Functional Skills &bull; Certificate of Exam Readiness"
        )
        + K.fill_notes("Final Examination Tips &amp; SPaG Memory Reminders", 18)
    )
    pages.append(K.page(cert_body, header=(BOOK, "Readiness Certificate"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Inside Back Cover & Back Cover
    pages.append(K.back_cover(back_cov))
    pdf_path = DOWNLOADS / "MasterFunctionalSkills_Mock_Pack_English_L2.pdf"
    print(f"Total Pages Assembled: {len(pages)}")
    res = K.render_pdf(pages, pdf_path, theme=cover_theme, entry3=False, title="Master Functional Skills - Mock Pack English Level 2")
    print(f"Rendered: {res['pdf']} ({len(pages)} pages)")
    return pdf_path

# =============================================================================
# 3. Digital Skills Handbook (A4 ~88 Pages)
# =============================================================================
def build_digital_skills_handbook():
    print("\n" + "="*70)
    print("BUILDING: MasterFunctionalSkills_Digital_Skills_Handbook.pdf")
    print("="*70)

    BOOK = "Digital Skills Core Handbook"
    front_cov = COV / "digital_skills_cover_page-1.png"
    back_cov = COV / "digital_skills_cover_page-2.png"
    cover_theme = K.theme_from_cover(front_cov)

    pages = []
    used_photos = set()

    def P(kw):
        p = get_photo(kw, "digital", used_photos)
        if p:
            used_photos.add(p)
        return p

    # p1: Front Cover
    pages.append(K.front_cover(front_cov))

    # p2: Inside Cover & Statutory Framework
    pages.append(K.inside_cover(
        "Essential Digital Skills &bull; EDSQ",
        "Comprehensive National Standards Handbook &bull; The 5 Statutory Domains, Software Workflows &amp; Practical Mock Exams",
        "Digital Skills",
        [
            ("1", "Digital Hardware, Cloud Storage &amp; Operating System Architecture", "3"),
            ("2", "National Curriculum Diagnostic Skills Audit &amp; Baseline Assessment", "4"),
            ("3", "The 5 Statutory Skill Areas Overview &amp; Examination Structure", "5"),
            ("4", "Learner Progress Tracker &amp; Digital Portfolio Roadmap", "6"),
            ("U1&ndash;U10", "10 Comprehensive Practical Units Across All 5 Domains (40 pages)", "7"),
            ("M1&ndash;M4", "4 Complete Official-Style Workplace Scenario Mocks (16 pages)", "47"),
            ("LAB1&ndash;LAB6", "6 Advanced Digital Software Labs &bull; Workplace Architecture (12 pages)", "63"),
            ("REF", "Comprehensive Solutions, Shortcuts, Glossary &amp; Index (10 pages)", "75"),
            ("CERT", "Digital Skills Competency Passport &amp; Official Certificate (4 pages)", "85"),
        ],
        footer=BOOK
    ))

    # p3: Digital Hardware & OS
    p3_body = (
        K.page_title("Hardware, OS &amp; Cloud Architecture", kicker="EDSQ Foundation Knowledge", badge="HW")
        + K.hero_image(P("laptop computer keyboard modern workspace typing"), "Modern workplace productivity relies on seamless cloud integration.", 52)
        + K.box_html(
            "<div style='display:grid; grid-template-columns:1fr 1fr; gap:12px; font-size:11.5pt;'>"
            "<div><b>Operating Systems (Windows/macOS/ChromeOS):</b> File hierarchy, file extensions (.docx, .xlsx, .pdf, .zip), and accessibility tools.</div>"
            "<div><b>Cloud Synchronization:</b> Storing files on OneDrive, Google Drive, or Nextcloud for automated backup and collaborative multi-user editing.</div>"
            "<div><b>Input/Output Peripherals:</b> Bluetooth keyboards, webcams, multi-monitor displays, and network printers.</div>"
            "<div><b>Network Protocols:</b> Wi-Fi security (WPA3), VPN encrypted tunnels, and mobile data hotspotting.</div>"
            "</div>",
            title="Essential Computing Infrastructure"
        )
        + K.tip_pair("Always check the file extension before opening attachments (.exe or .scr often signify malware).",
                     "Remember to lock your workstation (Win + L) whenever stepping away from your desk.",
                     golden_title="Security Golden Rule", watch_title="Workplace Trap!")
        + K.fill_notes("Personal Hardware &amp; System Configuration Notes", 24)
    )
    pages.append(K.page(p3_body, header=(BOOK, "Hardware & OS"), footer=BOOK, page_no=3))

    # p4: Baseline Assessment & Audit
    p4_body = (
        K.page_title("National Curriculum Baseline Audit", kicker="Self-Assessment &amp; Skills Audit", badge="AU")
        + K.box_html(
            "<table style='width:100%; border-collapse:collapse; font-size:11pt;'>"
            "<tr style='background:#f1f5f9;'><th style='padding:5px; text-align:left;'>Skill Area</th><th style='padding:5px; text-align:left;'>Core National Standard Competency</th><th style='padding:5px;'>Rating</th></tr>"
            "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0;'><b>1. Devices &amp; Handling Info</b></td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Manage files, folders, cloud storage, and configure accessibility settings.</td><td style='text-align:center;'>[ &nbsp; ] / 5</td></tr>"
            "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0;'><b>2. Creating &amp; Editing</b></td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Draft formal documents, build spreadsheets with formulas, format charts.</td><td style='text-align:center;'>[ &nbsp; ] / 5</td></tr>"
            "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0;'><b>3. Communicating</b></td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Send professional emails with attachments, participate in video conferences.</td><td style='text-align:center;'>[ &nbsp; ] / 5</td></tr>"
            "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0;'><b>4. Transacting</b></td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Complete online forms, verify secure checkout (SSL padlocks), manage online billing.</td><td style='text-align:center;'>[ &nbsp; ] / 5</td></tr>"
            "<tr><td style='padding:5px;'><b>5. Being Safe &amp; Responsible</b></td><td style='padding:5px;'>Identify phishing, manage passwords (2FA), protect digital footprint, understand GDPR.</td><td style='text-align:center;'>[ &nbsp; ] / 5</td></tr>"
            "</table>",
            title="DfE Essential Digital Skills Diagnostic Matrix"
        )
        + K.cartoon_tip(get_cartoon("priya tutor writing notes"), "Priya",
                        "Evaluate yourself honestly! Any skill rated below 3 will receive focused remediation in our software laboratory sections.")
        + K.fill_notes("Priority Digital Skills to Upgrade in this Course", 26)
    )
    pages.append(K.page(p4_body, header=(BOOK, "Baseline Audit"), footer=BOOK, page_no=4))

    # p5: National Standards & Examination Matrix
    p5_body = (
        K.page_title("National Standards &amp; Examination Blueprint", kicker="Pearson Edexcel EDSQ Assessment Structure", badge="BP")
        + K.hero_image(P("office team computer meeting collaborative training"), "Digital Functional Skills qualifications prepare learners for modern office roles.", 50)
        + K.box_html(
            "<div style='display:grid; grid-template-columns:1fr 1fr; gap:12px; font-size:11pt;'>"
            "<div><b>Component 1 &bull; Knowledge Test (20%):</b> Multiple-choice and drag-and-drop questions testing cybersecurity, online safety, GDPR, and device troubleshooting.</div>"
            "<div><b>Component 2 &bull; Practical Tasks (80%):</b> Hands-on computer-based workplace scenarios involving spreadsheet calculations, email correspondence, and folder structure.</div>"
            "<div><b>Pass Mark Benchmark:</b> Typically 65–70% across practical scenario tasks.</div>"
            "<div><b>Software Suite:</b> Microsoft Office 365, Google Workspace, or standard web browsers.</div>"
            "</div>",
            title="EDSQ Assessment Specifications"
        )
        + K.rule_box("Crucial Exam Protocol: Saving Your Work",
                     "<p>Examiners cannot grade work that is not saved! Always save your files to the designated candidate exam folder with the correct filename convention (e.g. <code>CandidateName_Task1_Budget.xlsx</code>) every 5 minutes.</p>")
        + K.fill_notes("My Practical Exam Software &amp; Shortcut Strategy", 22)
    )
    pages.append(K.page(p5_body, header=(BOOK, "Exam Blueprint"), footer=BOOK, page_no=5))

    # p6: Progress Tracker
    p6_body = (
        K.page_title("Digital Skills Progress Tracker", kicker="Unit &amp; Mock Mastery Log", badge="TR")
        + K.box_html(
            "<table style='width:100%; border-collapse:collapse; font-size:10.5pt; text-align:center;'>"
            "<tr style='background:#f1f5f9;'><th style='padding:5px; text-align:left;'>Unit / Mock Paper</th><th>Domain</th><th>Practical Score</th><th>Knowledge Check</th><th>Date</th></tr>"
            + "".join(f"<tr><td style='padding:4px; border-bottom:1px solid #e2e8f0; text-align:left;'><b>Unit {i}: {ssc.DIGITAL_SKILLS_UNITS[i-1]['title'][:28]}...</b></td>"
                      f"<td style='border-bottom:1px solid #e2e8f0;'>{ssc.DIGITAL_SKILLS_UNITS[i-1]['domain'][:12]}</td>"
                      f"<td style='border-bottom:1px solid #e2e8f0;'>&nbsp;&nbsp;&nbsp;&nbsp;/10</td>"
                      f"<td style='border-bottom:1px solid #e2e8f0;'>[ &nbsp; ] Pass</td>"
                      f"<td style='border-bottom:1px solid #e2e8f0;'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td></tr>"
                      for i in range(1, 11))
            + "".join(f"<tr><td style='padding:4px; border-bottom:1px solid #e2e8f0; text-align:left;'><b>Mock Exam {m}: Scenario Simulation</b></td>"
                      f"<td style='border-bottom:1px solid #e2e8f0;'>Synoptic</td>"
                      f"<td style='border-bottom:1px solid #e2e8f0;'>&nbsp;&nbsp;&nbsp;&nbsp;/50</td>"
                      f"<td style='border-bottom:1px solid #e2e8f0;'>[ &nbsp; ] Pass</td>"
                      f"<td style='border-bottom:1px solid #e2e8f0;'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td></tr>"
                      for m in range(1, 5))
            + "</table>",
            title="Learner Competency Milestone Tracker"
        )
        + K.fill_notes("Tutor Coaching Feedback &amp; IT Target Settings", 20)
    )
    pages.append(K.page(p6_body, header=(BOOK, "Progress Tracker"), footer=BOOK, page_no=6))

    # pp7–p46: 10 Comprehensive Practical Units (4 pages per unit = 40 pages)
    p_curr = 7
    for u_idx, unit in enumerate(ssc.DIGITAL_SKILLS_UNITS, start=1):
        u_title = unit["title"]
        u_domain = unit["domain"]
        badge = unit["badge"]
        kw = unit["kw"]
        theory = unit["theory"]
        steps = unit["steps"]
        drill = unit["drill"]
        trap = unit["trap"]

        # Page 1 of Unit: Core Theory & Workplace Context
        p1_b = (
            K.page_title(f"Unit {u_idx} &bull; {u_title}", kicker=f"EDSQ Domain: {u_domain}", badge=badge)
            + K.hero_image(P(kw), f"Workplace Application: {u_title}", 50)
            + K.box_html(f"<div style='font-size:11pt; line-height:1.5;'>{theory}</div>", title="Core Knowledge &amp; Statutory Standards")
            + K.rule_box("Workplace Context &amp; Employer Expectations",
                         f"<p style='margin:0;'>In modern enterprises, competence in <b>{u_title}</b> is essential for data security, administrative velocity, and regulatory compliance.</p>")
            + K.fill_notes("Personal Concept Notes &amp; Statutory Vocabulary", 24)
        )
        pages.append(K.page(p1_b, header=(BOOK, f"Unit {u_idx} &bull; Theory"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 2 of Unit: Step-by-Step Procedure & Workflows
        p2_b = (
            K.page_title(f"Unit {u_idx} &bull; Step-by-Step Workflow", kicker=f"Procedural Mastery &bull; {u_title}", badge=badge)
            + K.box_html(
                "<table style='width:100%; border-collapse:collapse; font-size:11pt;'>"
                + "".join(f"<tr><td style='padding:8px; border-bottom:1px solid #e2e8f0; width:80px;'><b>Step {s_num}:</b></td>"
                          f"<td style='padding:8px; border-bottom:1px solid #e2e8f0;'>{s_txt}</td></tr>"
                          for s_num, s_txt in enumerate(steps, start=1))
                + "</table>",
                title="Standard Operating Procedure (SOP)"
            )
            + K.tip_pair("Create a desktop shortcut for folders used on a daily basis to eliminate navigation latency.",
                         trap,
                         golden_title="Productivity Tip", watch_title="Examiner Pitfall!")
            + K.fill_notes("Candidate Command Triggers &amp; Shortcut Reminders", 30)
        )
        pages.append(K.page(p2_b, header=(BOOK, f"Unit {u_idx} &bull; Workflow"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 3 of Unit: Workplace Hands-On Practice Drill
        p3_b = (
            K.page_title(f"Unit {u_idx} &bull; Hands-On Practical Drill", kicker="Applied Scenario Practice &bull; Software Lab", badge=badge)
            + K.box_html(
                f"<div style='font-size:11pt; line-height:1.5;'>{drill}</div>",
                title=f"Workplace Simulation Task &bull; Unit {u_idx}"
            )
            + K.fill_grid("Candidate Action Log &amp; Software Command Steps", min_mm=60)
            + K.box_html(
                "<div style='display:flex; justify-content:space-between; font-weight:bold; font-size:11pt;'>"
                "<span>Drill Completed: [ &nbsp; ] Yes &emsp; [ &nbsp; ] In Progress</span>"
                "<span>Tutor Verification: ____________________</span>"
                "</div>",
                title="Practical Drill Verification"
            )
        )
        pages.append(K.page(p3_b, header=(BOOK, f"Unit {u_idx} &bull; Drill"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 4 of Unit: Common Pitfalls & Knowledge Check
        p4_b = (
            K.page_title(f"Unit {u_idx} &bull; Pitfall Audit &amp; Knowledge Check", kicker="Error Remediation &amp; Multiple-Choice Check", badge=badge)
            + K.rule_box("Critical Security &amp; Workflow Traps to Avoid",
                         f"<p><b>Trap:</b> {trap}<br>"
                         f"<b>Prevention:</b> Always audit inputs, lock credentials with two-factor authentication, and verify recipient address fields before clicking send.</p>")
            + K.box_html(
                "<div style='font-size:11pt; line-height:1.6;'>"
                "<p><b>Knowledge Check Questions:</b></p>"
                "<p><b>1.</b> Which file format preserves document formatting identically across all operating systems?<br>"
                "&emsp; [ &nbsp; ] A) .txt &emsp; [ &nbsp; ] B) .pdf &emsp; [ &nbsp; ] C) .csv &emsp; [ &nbsp; ] D) .rtf</p>"
                "<p><b>2.</b> What is the correct formula to calculate the average of cells B2 to B20?<br>"
                "&emsp; [ &nbsp; ] A) =MEAN(B2:B20) &emsp; [ &nbsp; ] B) =AVERAGE(B2:B20) &emsp; [ &nbsp; ] C) =AVG(B2-B20)</p>"
                "<p><b>3.</b> Under GDPR, within how many hours must a serious personal data breach be reported?<br>"
                "&emsp; [ &nbsp; ] A) 24 hours &emsp; [ &nbsp; ] B) 48 hours &emsp; [ &nbsp; ] C) 72 hours &emsp; [ &nbsp; ] D) 7 days</p>"
                "</div>",
                title="Statutory Knowledge Verification"
            )
            + K.fill_notes("Candidate Working Notes &amp; Unit Summary", 36)
        )
        pages.append(K.page(p4_b, header=(BOOK, f"Unit {u_idx} &bull; Check"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # pp47–p62: 4 Full Workplace Scenario Mocks (4 pages per mock = 16 pages)
    p_curr = 47
    for m_idx, mock in enumerate(ssc.DIGITAL_SKILLS_MOCKS, start=1):
        m_title = mock["title"]
        m_scen = mock["scenario"]
        m_tasks = mock["tasks"]

        # Page 1 of Mock: Scenario Overview & Task 1 (File Hierarchy)
        p1_b = (
            K.page_title(f"Mock Exam {m_idx} &bull; Scenario Overview", kicker=f"Practical Exam {m_idx}: {m_title}", badge=f"ME{m_idx}.1")
            + K.hero_image(P("office workspace computer dual screen productivity"), f"Examination Context: {m_title}", 48)
            + K.box_html(f"<div style='font-size:11pt; line-height:1.5;'><p><b>Scenario Context:</b> {m_scen}</p></div>", title="Candidate Briefing &bull; 50 Marks &bull; 1 hr 45 mins")
            + exam_box(f"Task 1 (File Hierarchy &amp; Storage Architecture): {m_tasks[0]}", marks=12)
            + K.fill_grid("Candidate Working Grid &bull; Folder Architecture &amp; File Paths", min_mm=42)
        )
        pages.append(K.page(p1_b, header=(BOOK, f"Mock {m_idx} &bull; Task 1"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 2 of Mock: Task 2 (Spreadsheet Formulas & Data Analysis)
        p2_b = (
            K.page_title(f"Mock Exam {m_idx} &bull; Task 2 (Spreadsheet Modeling)", kicker=f"Practical Exam {m_idx}: {m_title}", badge=f"ME{m_idx}.2")
            + exam_box(f"Task 2 (Spreadsheet Calculations &amp; Formatting): {m_tasks[1]}", marks=15)
            + K.fill_grid("Candidate Working Grid &bull; Formula Syntax (=SUM, =AVERAGE, =IF)", min_mm=60)
            + K.rule_box("Formula Verification Checklist",
                         "<p>Verify: (1) Absolute cell references ($B$1) are locked where appropriate. (2) Currency formatting applied (&pound;0.00). (3) Gridlines visible for printing.</p>")
        )
        pages.append(K.page(p2_b, header=(BOOK, f"Mock {m_idx} &bull; Task 2"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 3 of Mock: Task 3 (Professional Workplace Communication)
        p3_b = (
            K.page_title(f"Mock Exam {m_idx} &bull; Task 3 (Email &amp; Communication)", kicker=f"Practical Exam {m_idx}: {m_title}", badge=f"ME{m_idx}.3")
            + exam_box(f"Task 3 (Professional Workplace Correspondence): {m_tasks[2]}", marks=12)
            + K.fill_notes("Candidate Email Drafting Area (Subject, Salutation, Body, Sign-Off)", 140)
        )
        pages.append(K.page(p3_b, header=(BOOK, f"Mock {m_idx} &bull; Task 3"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 4 of Mock: Task 4 (Cybersecurity Incident Response & Audit)
        p4_b = (
            K.page_title(f"Mock Exam {m_idx} &bull; Task 4 (Security Incident)", kicker=f"Practical Exam {m_idx}: {m_title}", badge=f"ME{m_idx}.4")
            + exam_box(f"Task 4 (Cybersecurity Incident Triage &amp; Reporting): {m_tasks[3]}", marks=11)
            + K.fill_notes("Candidate Incident Triage &amp; Action Report", 80)
            + K.box_html(
                f"<div style='display:flex; justify-content:space-between; font-weight:bold; font-size:11pt;'>"
                f"<span>Mock {m_idx} Total Marks: ______ / 50</span>"
                f"<span>Status: [ &nbsp; ] Pass &emsp; [ &nbsp; ] Refer</span>"
                f"<span>Examiner: ____________________</span>"
                f"</div>",
                title="Practical Exam Summary &amp; Sign-Off"
            )
        )
        pages.append(K.page(p4_b, header=(BOOK, f"Mock {m_idx} &bull; Summary"), footer=BOOK, page_no=p_curr))
        p_curr += 1


    # pp63–p74: 6 Advanced Digital Software Labs (2 pages per lab = 12 pages)
    advanced_labs = [
        ("Lab 1: Cloud Storage Architecture & Access Permissions", "LAB1",
         "Enterprise cloud directory structures, multi-tenant sharing, and permission hierarchies.",
         "cloud server data storage network infrastructure",
         "<b>Cloud Security Framework:</b> In enterprise environments (SharePoint, Google Drive, Nextcloud), granting blanket 'Edit' access to root folders introduces critical data loss risks. Standard practice mandates three distinct permission tiers: (1) <i>View/Read-Only</i> for general staff reference documents; (2) <i>Commenter</i> for cross-departmental reviewers; (3) <i>Owner/Editor</i> restricted to designated project managers.<br><br>"
         "<b>Version History & Audit Trails:</b> When multiple team members collaborate asynchronously, file synchronization conflicts frequently overwrite crucial data. Cloud versioning allows administrators to inspect previous timestamps, compare differences, and restore stable revisions.",
         "Standard Operating Checklist: Tiered Permissions",
         [("1. Root Folder Provisioning", "Create a structured project folder with format: <code>[Dept]_[ProjectName]_[Year]</code>."),
          ("2. Subfolder Partitioning", "Establish segregated subfolders: <code>01_Reference</code> (Read-Only), <code>02_WIP</code> (Edit for Team), <code>03_Confidential</code> (Restricted)."),
          ("3. Link Security Configuration", "Disable 'Anyone with the link' public sharing. Enforce organizational email domain authentication with 30-day password expiry.")],
         "Applied Workplace Scenario & Lab Task",
         "Scenario: You are deploying a shared cloud workspace for a regional healthcare recruitment drive involving 40 confidential applicant CVs and an open interviewer schedule.<br><br>"
         "<b>Required Lab Deliverables:</b><br>"
         "1. Diagram a 3-tier folder structure ensuring interviewers cannot edit master candidate scorecards.<br>"
         "2. Write the exact permission settings (Read-only, Edit, Restricted) for 3 distinct user groups.<br>"
         "3. Outline the 4-step emergency recovery procedure if an interviewer accidentally deletes the schedule."),

        ("Lab 2: Advanced Spreadsheet Modeling & Data Validation", "LAB2",
         "Formulas, absolute referencing, conditional formatting, and error diagnostics.",
         "financial spreadsheet data analysis charts monitor",
         "<b>Mathematical Rigor in Spreadsheets:</b> Workplace spreadsheets drive payroll, procurement, and financial forecasting. A single missing dollar sign in an absolute reference (e.g. <code>B$1</code> vs <code>B1</code>) can distort thousand-pound calculations across autofilled columns.<br><br>"
         "<b>Data Validation Protocols:</b> Restricting user input to pre-configured dropdown lists (e.g. Approved Expense Categories) prevents typographical errors that break lookup formulas like <code>=VLOOKUP()</code> and <code>=XLOOKUP()</code>.",
         "Standard Operating Checklist: Formula Modeling",
         [("1. Absolute Cell Locking", "Lock tax rates or exchange rate parameters using <code>$</code> syntax (e.g. <code>=A2 * $E$1</code>) before dragging fill handles."),
          ("2. Dynamic Dropdown Lists", "Implement Data Validation &rarr; List &rarr; specify source range to enforce uniform category naming conventions."),
          ("3. Conditional Alerts", "Apply conditional formatting rules to highlight values exceeding budget limits in bold red with light pink shading.")],
         "Applied Workplace Scenario & Lab Task",
         "Scenario: You are designing an automated departmental petty cash and travel reimbursement model for 15 field technicians.<br><br>"
         "<b>Required Lab Deliverables:</b><br>"
         "1. Construct the formula to calculate mileage allowance (&pound;0.45/mile) referencing locked cell <code>$C$1</code>.<br>"
         "2. Write the syntax for an <code>=IF()</code> statement that flags any expense over &pound;100 as 'REQUIRES SENIOR SIGN-OFF'.<br>"
         "3. Detail how to identify and resolve a <code>#VALUE!</code> error caused by text characters in a numerical column."),

        ("Lab 3: Professional Business Correspondence & Netiquette", "LAB3",
         "Email architecture, confidentiality etiquette, thread management, and calendar invites.",
         "business executive typing email laptop clean desk",
         "<b>Professional Email Architecture:</b> Business email is a permanent legal record. Messages must possess a concise, descriptive subject line (e.g. <code>[URGENT] Q3 Financial Audit Review - Action Required by 17:00</code>), professional salutation, structured body paragraphs, and a compliant corporate signature banner.<br><br>"
         "<b>The Confidentiality Imperative (CC vs BCC):</b> The UK Information Commissioner's Office (ICO) penalizes organizations thousands of pounds for exposing customer email addresses by using the CC field instead of BCC during group mailings.",
         "Standard Operating Checklist: Email Governance",
         [("1. Subject Line Protocol", "Always include project prefix, topic summary, and response deadline."),
          ("2. BCC Privacy Rule", "Any distribution list to external clients or patients MUST utilize BCC to comply with UK Data Protection regulations."),
          ("3. Meeting Invitation Workflow", "Include agenda bullet points, video conference URL, and attachments directly within calendar invites.")],
         "Applied Workplace Scenario & Lab Task",
         "Scenario: A critical delivery of medical training equipment has been delayed by 72 hours, impacting a scheduled apprentice certification day.<br><br>"
         "<b>Required Lab Deliverables:</b><br>"
         "1. Draft the formal email to the Lead Course Instructor acknowledging the delay and presenting two contingency solutions.<br>"
         "2. Explain why individual student email addresses must be placed in BCC rather than CC.<br>"
         "3. Create a structured calendar meeting invitation with agenda to review contingency options at 08:30 tomorrow."),

        ("Lab 4: Cybersecurity Vulnerability Triage & Phishing Defense", "LAB4",
         "Detecting social engineering, spoofed domains, ransomware vectors, and incident logging.",
         "cybersecurity lock shield data protection screen",
         "<b>Anatomy of Social Engineering:</b> Modern cyber attacks rarely exploit raw software vulnerabilities; they exploit human psychology. Phishing attacks manufacture urgency (e.g. 'Your account will be suspended within 2 hours!'), impersonate trusted authority figures (CEOs, IT helpdesk), and conceal malicious URLs behind misleading anchor text.<br><br>"
         "<b>Incident Escalation Protocols:</b> When a phishing link is clicked or credentials are inadvertently entered, immediate isolation of the device from the network is mandatory to prevent malware propagation.",
         "Standard Operating Checklist: Threat Triage",
         [("1. Header & Domain Inspection", "Verify sender email domain exactly (e.g. <code>@hmrc-tax-refund.co.uk</code> vs legitimate <code>@hmrc.gov.uk</code>)."),
          ("2. Link Destination Hover", "Hover without clicking to inspect the true hyperlinked URL in the browser status bar."),
          ("3. Incident Escalation", "Disconnect Wi-Fi / ethernet immediately, notify InfoSec officer, and log incident details.")],
         "Applied Workplace Scenario & Lab Task",
         "Scenario: An employee in accounts payable receives an urgent email appearing to come from the Managing Director requesting an immediate &pound;8,500 bank transfer to an unknown vendor account.<br><br>"
         "<b>Required Lab Deliverables:</b><br>"
         "1. Identify 4 distinct red flags that indicate this email is a Business Email Compromise (BEC) attack.<br>"
         "2. Complete a statutory 4-point Cybersecurity Incident Triage Log.<br>"
         "3. Outline the verification protocol required before any unusual financial transfer is authorized."),

        ("Lab 5: Corporate Document Processing & Accessibility", "LAB5",
         "Semantic heading styles, automated TOC, alt-text for screen readers, and PDF conversion.",
         "professional printing document review proofreading desk",
         "<b>Document Accessibility Standards (WCAG 2.1):</b> Corporate publications, patient guides, and training manuals must be accessible to individuals using assistive technologies (screen readers, braille displays). Merely enlarging font size and making text bold does not create a true heading.<br><br>"
         "<b>Semantic Structure & Automation:</b> Applying true Heading Styles (Heading 1, Heading 2, Heading 3) allows screen readers to navigate document outlines and enables word processors to generate instant, perfectly formatted Tables of Contents.",
         "Standard Operating Checklist: Document Accessibility",
         [("1. Semantic Hierarchy", "Apply Heading 1 for document titles, Heading 2 for major chapters, Heading 3 for subsections."),
          ("2. Visual Accessibility", "Ensure minimum text contrast ratio of 4.5:1. Never convey meaning through color alone."),
          ("3. Alternative Text (Alt-Text)", "Provide concise descriptions of functional images, charts, and diagrams for screen readers.")],
         "Applied Workplace Scenario & Lab Task",
         "Scenario: You are standardizing a 12-page unformatted draft of the company Employee Health & Safety Handbook.<br><br>"
         "<b>Required Lab Deliverables:</b><br>"
         "1. Reorganize the provided raw text outline into a semantic Heading 1 &rarr; Heading 2 &rarr; Heading 3 hierarchy.<br>"
         "2. Write appropriate, descriptive Alt-Text for an infographic showing workplace emergency evacuation routes.<br>"
         "3. Describe the 3 checks required before exporting the document as an accessible, tagged PDF/A file."),

        ("Lab 6: Online Research, Source Reliability & Copyright Compliance", "LAB6",
         "The CRAAP evaluation model, copyright licensing, Creative Commons, and data synthesis.",
         "academic research digital library search internet books",
         "<b>Information Literacy in the Digital Age:</b> The internet offers boundless information alongside rampant misinformation, biased editorializing, and outdated technical claims. Workplace professionals must systematically evaluate online sources using the CRAAP test: Currency, Relevance, Authority, Accuracy, and Purpose.<br><br>"
         "<b>Intellectual Property & Licensing:</b> Commercial reuse of text, imagery, or software code without explicit licensing exposes organizations to severe legal copyright infringement claims under the Copyright, Designs and Patents Act 1988.",
         "Standard Operating Checklist: Information Verification",
         [("1. Currency & Authority Audit", "Verify publication date and author credentials (peer-reviewed, government statistical agency, or recognized trade body)."),
          ("2. Cross-Verification Rule", "Never cite a critical statistic without confirming it across at least two independent primary sources."),
          ("3. Licensing Compliance", "Verify Creative Commons licenses (CC-BY, CC-SA). Avoid CC-NC assets in commercial business publications.")],
         "Applied Workplace Scenario & Lab Task",
         "Scenario: You are conducting market research to advise executive directors on choosing an commercial cloud telephone system (VoIP).<br><br>"
         "<b>Required Lab Deliverables:</b><br>"
         "1. Apply the 5 criteria of the CRAAP test to evaluate a vendor promotional white paper vs a consumer watchdog report.<br>"
         "2. Explain the legal restrictions of using a 'Creative Commons Attribution-NonCommercial (CC BY-NC)' image in a commercial company brochure.<br>"
         "3. Compile an annotated corporate research brief comparing two verified telecom providers.")
    ]

    for lab_title, badge, lead, photo_kw, theory_html, sop_title, sop_steps, task_title, task_html in advanced_labs:
        # Page 1 of Lab: Advanced Concept, Visual Interface & SOP Checklist
        p1_lab = (
            K.page_title(lab_title, kicker="Advanced Digital Software Lab &bull; Part 1: Theory &amp; SOP", badge=badge)
            + K.hero_image(P(photo_kw), lead, 45)
            + K.box_html(f"<div style='font-size:10.5pt; line-height:1.45;'>{theory_html}</div>", title="Workplace Technical Architecture &amp; Governance")
            + K.box_html(
                "<table style='width:100%; border-collapse:collapse; font-size:10.5pt; line-height:1.45;'>"
                + "".join(f"<tr><td style='padding:6px; border-bottom:1px solid #e2e8f0; width:190px;'><b>{step_name}:</b></td>"
                          f"<td style='padding:6px; border-bottom:1px solid #e2e8f0;'>{step_desc}</td></tr>"
                          for step_name, step_desc in sop_steps)
                + "</table>",
                title=sop_title
            )
            + K.fill_notes("Personal Implementation Notes &amp; Software Shortcuts", 18)
        )
        pages.append(K.page(p1_lab, header=(BOOK, f"{badge} &bull; SOP"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 2 of Lab: Hands-On Scenario & Software Lab Task
        p2_lab = (
            K.page_title(f"{badge} &bull; Applied Workplace Hands-On Task", kicker="Advanced Digital Software Lab &bull; Part 2: Hands-On Lab", badge=badge)
            + K.box_html(f"<div style='font-size:10.5pt; line-height:1.45;'>{task_html}</div>", title=task_title)
            + K.fill_grid("Candidate Command Steps &amp; Technical Implementation Log", min_mm=55)
            + K.box_html(
                "<div style='display:flex; justify-content:space-between; font-weight:bold; font-size:10pt;'>"
                "<span>Lab Task Completed: [ &nbsp; ] Yes &emsp; [ &nbsp; ] In Progress</span>"
                "<span>Lead Tutor Verification: Abdul &bull; ____________________</span>"
                "</div>",
                title="Software Lab Sign-Off &amp; Competency Endorsement"
            )
        )
        pages.append(K.page(p2_lab, header=(BOOK, f"{badge} &bull; Lab Task"), footer=BOOK, page_no=p_curr))
        p_curr += 1


    # pp75–p78: Advanced Workplace IT Frameworks & Diagnostic Reference (4 pages)
    extra_it_pages = [
        ("Workplace File Format &amp; Extension Directory", "IT.REF1",
         "Comprehensive classification of corporate file formats, compression algorithms, and application associations.",
         "computer server hard drive data technology storage",
         "<table style='width:100%; border-collapse:collapse; font-size:10pt; line-height:1.45;'>"
         "<tr style='background:#f1f5f9;'><th style='padding:6px; text-align:left;'>Extension</th><th style='padding:6px; text-align:left;'>Category</th><th style='padding:6px; text-align:left;'>Associated Software</th><th style='padding:6px; text-align:left;'>Security &amp; Compatibility Notes</th></tr>"
         "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0;'><b>.pdf</b></td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Document</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Adobe Acrobat / Edge</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Preserves formatting across platforms; read-only default.</td></tr>"
         "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0;'><b>.docx / .odt</b></td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Word Processing</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Word / LibreOffice</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Standard editable documents. May harbor malicious macros.</td></tr>"
         "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0;'><b>.xlsx / .csv</b></td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Spreadsheet</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Excel / Google Sheets</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>.csv is plain text without formulas; .xlsx supports formulas and charts.</td></tr>"
         "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0;'><b>.png / .jpg</b></td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Raster Image</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Photos / Browser</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>.png supports transparency; .jpg provides high photographic compression.</td></tr>"
         "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0;'><b>.zip / .tar.gz</b></td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Archive</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>WinZip / 7-Zip</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Bundles and compresses multiple files; scan before extraction.</td></tr>"
         "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0;'><b>.exe / .bat</b></td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Executable</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Windows OS Core</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Executes code directly. <b>Extreme danger in email attachments!</b></td></tr>"
         "</table>",
         "Golden Rule: Never double-click an executable attachment (.exe, .scr, .vbs) received via email, even if the sender appears familiar!"),

        ("Spreadsheet Error Diagnostics &amp; Function Syntax", "IT.REF2",
         "Troubleshooting calculation errors, reference issues, and syntax anomalies under pressure.",
         "calculator accounting finance numbers calculation",
         "<table style='width:100%; border-collapse:collapse; font-size:10pt; line-height:1.45;'>"
         "<tr style='background:#f1f5f9;'><th style='padding:6px; text-align:left;'>Error Code</th><th style='padding:6px; text-align:left;'>Root Cause</th><th style='padding:6px; text-align:left;'>Remediation Step</th></tr>"
         "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0;'><b>#DIV/0!</b></td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Dividing by zero or an empty cell.</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Wrap formula in <code>=IF(B2=0, 0, A2/B2)</code> to handle zero values safely.</td></tr>"
         "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0;'><b>#VALUE!</b></td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Mathematical operation performed on text string.</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Verify that referenced cells contain purely numerical digits, not symbols.</td></tr>"
         "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0;'><b>#REF!</b></td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Cell referenced in formula was deleted.</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Undo deletion (<code>Ctrl + Z</code>) or re-point the formula to the correct active coordinate.</td></tr>"
         "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0;'><b>#NAME?</b></td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Misspelled function name (e.g. <code>=AVRAGE</code>).</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Correct spelling to standard syntax: <code>=AVERAGE()</code>, <code>=SUM()</code>, <code>=COUNT()</code>.</td></tr>"
         "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0;'><b>#####</b></td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Column width is too narrow to display the number.</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Double-click column boundary header line to autofit column width.</td></tr>"
         "</table>",
         "Pro-Tip: Always use the Formula Auditing toolbar (Trace Precedents / Trace Dependents) to visualize how formulas link across large workbooks."),

        ("Cybersecurity Incident Escalation &amp; GDPR Action Flowchart", "IT.REF3",
         "Statutory protocols for reporting unauthorized data disclosures and suspected cyber intrusions.",
         "cybersecurity lock shield data protection screen",
         "<div style='font-size:10.5pt; line-height:1.5;'>"
         "<p><b>Phase 1 &bull; Immediate Containment (Minutes 0&ndash;15):</b><br>"
         "&bull; Disconnect device from Wi-Fi/Ethernet immediately. Do NOT turn off the computer (preserves forensic volatile RAM memory).<br>"
         "&bull; Alert immediate line manager and designated Information Security Officer.</p>"
         "<p><b>Phase 2 &bull; Investigation &amp; Triage (Hours 1&ndash;24):</b><br>"
         "&bull; Determine category of breached data: Does it contain Special Category PII (medical records, biometric data, financial details)?<br>"
         "&bull; Audit access logs to establish extent of unauthorized extraction.</p>"
         "<p><b>Phase 3 &bull; Statutory Regulatory Disclosure (Within 72 Hours):</b><br>"
         "&bull; Under Article 33 of UK GDPR, the Information Commissioner's Office (ICO) must be notified within 72 hours of becoming aware of a high-risk personal data breach.<br>"
         "&bull; Notify affected data subjects without undue delay if risk to their rights and freedoms is significant.</p>"
         "</div>",
         "Legal Mandate: Fines for non-reporting under UK GDPR can reach &pound;17.5 million or 4% of global annual turnover, whichever is greater."),

        ("Workplace Digital Hygiene &amp; Device Ergonomics Audit", "IT.REF4",
         "Personal compliance audit for password security, multi-factor tokens, and postural health.",
         "office team computer meeting collaborative training",
         "<div style='font-size:10.5pt; line-height:1.5;'>"
         "<p><b>Digital Security Hygiene Checklist:</b><br>"
         "[ &nbsp; ] Passphrases consist of three random, memorable words (minimum 14 characters).<br>"
         "[ &nbsp; ] Multi-factor authentication (MFA) enabled on email, cloud drives, and internal portals.<br>"
         "[ &nbsp; ] Lock workstation screen (<code>Win + L</code>) whenever stepping away from desk.<br>"
         "[ &nbsp; ] Automatic software updates and anti-virus definitions set to auto-install overnight.<br>"
         "[ &nbsp; ] Work files saved exclusively on encrypted cloud backup drives, never on local desktop.</p>"
         "<p><b>Health &amp; Safety DSE Ergonomic Checklist:</b><br>"
         "[ &nbsp; ] Top of computer monitor positioned at eye level; distance 50&ndash;70 cm from face.<br>"
         "[ &nbsp; ] Forearms rest horizontal to desk surface; wrists remain straight during typing.<br>"
         "[ &nbsp; ] Lumbar spine supported by adjustable ergonomic backrest; feet flat on floor or footrest.<br>"
         "[ &nbsp; ] 20-20-20 rule implemented: Every 20 minutes, look at an object 20 feet away for 20 seconds.</p>"
         "</div>",
         "Lead Instructor Endorsement: Maintaining daily digital hygiene and physical ergonomics ensures long-term career productivity and regulatory compliance.")
    ]

    for it_title, badge, lead, photo_kw, content_html, box_rule in extra_it_pages:
        it_body = (
            K.page_title(it_title, kicker="Statutory Standards &amp; Workplace IT Framework", badge=badge)
            + K.hero_image(P(photo_kw), lead, 45)
            + K.box_html(content_html, title="Workplace Technical Specification &amp; Architecture")
            + K.rule_box("Core Professional Compliance Mandate", f"<p style='margin:0;'>{box_rule}</p>")
            + K.fill_notes("Personal Implementation Notes &amp; Enterprise Protocols", 22)
        )
        pages.append(K.page(it_body, header=(BOOK, f"{badge} &bull; IT Framework"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # pp63–p82: Back matter reference section (via K.ref_pages)
    ref_blocks = []
    # Unit solutions
    for title_str, sol_html in ssr.DIGITAL_SKILLS_SOLUTIONS["units"]:
        ref_blocks.append(K.ref_block(title_str, sol_html))
    # Mock solutions
    for title_str, sol_html in ssr.DIGITAL_SKILLS_SOLUTIONS["mocks"]:
        ref_blocks.append(K.ref_block(title_str, sol_html))
    # Shortcuts
    ref_blocks.append(K.ref_block("Universal Operating System &amp; Browser Shortcuts", ssr.DIGITAL_SKILLS_SHORTCUTS))
    # Glossary
    gloss_html = "".join(f"<dl><dt>{t}</dt><dd>{d}</dd></dl>" for t, d in ssr.DIGITAL_SKILLS_GLOSSARY)
    ref_blocks.append(K.ref_block("Digital Skills &amp; Cybersecurity Glossary", gloss_html))
    # Index
    ix_html = ""
    for letter, entries in ssr.DIGITAL_SKILLS_INDEX:
        items = "".join(f"<div class='ix'><span>{t}</span><span>{p}</span></div>" for t, p in entries)
        ix_html += f"<div class='ix-letter'>{letter}</div>{items}"
    ref_blocks.append(K.ref_block("Digital Skills Curriculum Index", ix_html))

    ref_page_list = K.ref_pages("Official Solutions, Shortcuts &amp; Reference Directory", ref_blocks,
                                BOOK, start_page=p_curr, subtitle="Complete Practical Workflow Solutions &amp; Statutory Guidance",
                                cols=2, theme=cover_theme, notes_title="Candidate Error Analysis &amp; Security Checklist")
    pages.extend(ref_page_list)
    p_curr += len(ref_page_list)

    # Competency Passport & Certification (pp 83–86)
    # Page 83: Competency Matrix
    cm_body = (
        K.page_title("Digital Skills Competency Passport", kicker="National Standards Mastery Audit", badge="CP")
        + K.box_html(
            "<table style='width:100%; border-collapse:collapse; font-size:11pt;'>"
            "<tr style='background:#f1f5f9;'><th style='padding:6px; text-align:left;'>Domain</th><th>Level</th><th>Assessment Mode</th><th>Status</th><th>Date</th></tr>"
            "<tr><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>1. Using Devices &amp; Handling Info</td><td style='text-align:center;'>Level 1/2</td><td style='text-align:center;'>Folder Structure Task</td><td style='text-align:center;'>[ &nbsp; ] Competent</td><td>&nbsp;</td></tr>"
            "<tr><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>2. Creating &amp; Editing</td><td style='text-align:center;'>Level 1/2</td><td style='text-align:center;'>Spreadsheet &amp; Chart</td><td style='text-align:center;'>[ &nbsp; ] Competent</td><td>&nbsp;</td></tr>"
            "<tr><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>3. Communicating</td><td style='text-align:center;'>Level 1/2</td><td style='text-align:center;'>Formal Email &amp; Calendar</td><td style='text-align:center;'>[ &nbsp; ] Competent</td><td>&nbsp;</td></tr>"
            "<tr><td style='padding:6px; border-bottom:1px solid #e2e8f0;'>4. Transacting</td><td style='text-align:center;'>Level 1/2</td><td style='text-align:center;'>E-Commerce &amp; Form Data</td><td style='text-align:center;'>[ &nbsp; ] Competent</td><td>&nbsp;</td></tr>"
            "<tr><td style='padding:6px;'>5. Being Safe &amp; Responsible</td><td style='text-align:center;'>Level 1/2</td><td style='text-align:center;'>Security &amp; GDPR Audit</td><td style='text-align:center;'>[ &nbsp; ] Competent</td><td>&nbsp;</td></tr>"
            "</table>",
            title="Statutory Digital Competency Verification"
        )
        + K.cartoon_tip(get_cartoon("priya tutor writing notes"), "Priya",
                        "Retain this signed passport in your professional portfolio as evidence of digital literacy for employers and apprenticeship standards.")
        + K.fill_notes("Personal Professional Development Targets", 36)
    )
    pages.append(K.page(cm_body, header=(BOOK, "Competency Passport"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Page 84: Official Certificate
    cert_body = (
        K.page_title("Certificate of Digital Competence", kicker="National Curriculum Milestone Sign-Off", badge="CERT")
        + K.hero_image(P("adult student graduation diploma celebration success"), "Empowering learners with essential 21st-century digital capabilities.", 55)
        + K.box_html(
            "<div style='text-align:center; padding:15px; font-size:12pt; line-height:1.7;'>"
            "<p>This certifies that</p>"
            "<p style='font-size:18pt; font-weight:bold; border-bottom:2px solid var(--accent); display:inline-block; min-width:320px; padding-bottom:4px;'>&nbsp;</p>"
            "<p>has completed the Essential Digital Skills National Curriculum and successfully passed all 4 synoptic workplace scenario examinations.</p>"
            "<table style='width:100%; margin-top:20px; font-size:11pt; border-collapse:collapse;'>"
            "<tr><td style='text-align:left;'><b>Lead Instructor:</b> Abdul</td><td style='text-align:right;'><b>Date Verified:</b> _______________</td></tr>"
            "<tr><td style='text-align:left;'><b>Practical Exam Score:</b> ______ / 50</td><td style='text-align:right;'><b>Exam Centre:</b> Oxford Health OH</td></tr>"
            "</table>"
            "</div>",
            title="Master Functional Skills &bull; Certificate of Digital Competence"
        )
        + K.fill_notes("Final Examination Tips &amp; Digital Safety Reminders", 30)
    )
    pages.append(K.page(cert_body, header=(BOOK, "Competency Certificate"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Inside Back Cover & Back Cover
    pages.append(K.back_cover(back_cov))
    pdf_path = DOWNLOADS / "MasterFunctionalSkills_Digital_Skills_Handbook.pdf"
    print(f"Total Pages Assembled: {len(pages)}")
    res = K.render_pdf(pages, pdf_path, theme=cover_theme, entry3=False, title="Master Functional Skills - Digital Skills Handbook")
    print(f"Rendered: {res['pdf']} ({len(pages)} pages)")
    return pdf_path

# =============================================================================
# 4. BKSB Remediation Workbook (A4 ~88 Pages)
# =============================================================================
def build_bksb_remediation_workbook():
    print("\n" + "="*70)
    print("BUILDING: MasterFunctionalSkills_BKSB_Remediation_Workbook.pdf")
    print("="*70)

    BOOK = "BKSB Diagnostic Remediation Workbook"
    front_cov = COV / "bksb_remediation_cover_page-1.png"
    back_cov = COV / "bksb_remediation_cover_page-2.png"
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

    # p2: Inside Cover & Diagnostic Matrix
    pages.append(K.inside_cover(
        "BKSB &bull; Diagnostic Remediation",
        "Targeted Diagnostic Workbook &bull; 24 High-Frequency Failure Modes, Worked Models &amp; Candidate Retry Booklets",
        "BKSB Remediation",
        [
            ("1", "The BKSB Diagnostic Remediation Methodology &amp; Protocol", "3"),
            ("2", "Personal Diagnostic Score Tracker &amp; Remediation Schedule", "4"),
            ("3", "Algorithmic Marking Traps &amp; Online Interface Navigation", "5"),
            ("4", "Diagnostic Error Classification &amp; Remediation Pathways", "6"),
            ("M1&ndash;M24", "24 High-Frequency Diagnostic Failure Modes (48 pages)", "7"),
            ("WS1&ndash;WS8", "8 Specialist Interface &amp; Rapid Diagnostic Workshops (8 pages)", "55"),
            ("MS", "Comprehensive Worked Solutions &amp; Step-by-Step Guidance (20 pages)", "63"),
            ("CERT", "Diagnostic Re-assessment Log &amp; Level 2 Mastery Certificate", "83"),
        ],
        footer=BOOK
    ))

    # p3: Methodology
    p3_body = (
        K.page_title("The BKSB Remediation Methodology", kicker="Tutor Diagnostic Framework", badge="MT")
        + K.hero_image(P("tutor teaching adult student smiling classroom"), "Targeting the exact misconception turns repeated errors into permanent exam mastery.", 52)
        + K.box_html(
            "<div style='font-size:11.5pt; line-height:1.6;'>"
            "<p><b>Phase 1 &bull; Diagnostic Error Detection:</b> Identify the exact mathematical or grammatical trigger flagged by online assessment algorithms.</p>"
            "<p><b>Phase 2 &bull; Root Cause Deconstruction:</b> Review the golden rule and understand WHY the wrong answer was selected.</p>"
            "<p><b>Phase 3 &bull; Scaffolding &amp; Worked Method:</b> Study the step-by-step exemplar model with Raymond Murphy cartoon advice.</p>"
            "<p><b>Phase 4 &bull; Independent Retry Drills:</b> Solve 3 targeted drill questions in the workbook without looking at the solutions.</p>"
            "<p><b>Phase 5 &bull; Verification &amp; Sign-Off:</b> Audit answers against the Stage 2 Mark Scheme and log mastery on your diagnostic tracker.</p>"
            "</div>",
            title="The 5-Phase Diagnostic Recovery Loop"
        )
        + K.tip_pair("Never rush through online tests. 60% of wrong answers on BKSB stem from misreading the question, not lack of mathematical ability.",
                     "Watch out for decimal time! Entering 2.15 for 2 hours 15 minutes is the single most common failure mode in functional maths.",
                     golden_title="Tutor Golden Rule", watch_title="Online Test Trap!")
        + K.fill_notes("My Personal Error Patterns &amp; Focus Areas", 22)
    )
    pages.append(K.page(p3_body, header=(BOOK, "Methodology"), footer=BOOK, page_no=3))

    # p4: Algorithmic Marking Traps
    p4_body = (
        K.page_title("Algorithmic Marking Traps &amp; Insights", kicker="Online Platform Mechanics", badge="TR")
        + K.box_html(
            "<div style='font-size:11pt; line-height:1.5;'>"
            "<p>Online diagnostic platforms like BKSB and OneAdvanced utilize rigid algorithmic answer-checking engines. Even if your mathematical reasoning is sound, the engine will award zero marks for any of the following input flaws:</p>"
            "<table style='width:100%; border-collapse:collapse; margin-top:8px;'>"
            "<tr style='background:#f1f5f9;'><th style='padding:5px; text-align:left;'>Input Error</th><th style='padding:5px; text-align:left;'>What the Student Entered</th><th style='padding:5px; text-align:left;'>What the System Required</th></tr>"
            "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Missing Pence Zero</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>&pound;14.5</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'><b>&pound;14.50</b> (2 decimal places mandatory)</td></tr>"
            "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Omitted Units</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>45</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'><b>45 m&sup2;</b> or <b>45 kg</b> (where prompt requests units)</td></tr>"
            "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Premature Rounding</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>12.6</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'><b>12.67</b> (rounded intermediate numbers corrupt total)</td></tr>"
            "<tr><td style='padding:5px;'>Double Unit Symbols</td><td style='padding:5px;'>&pound;24.50</td><td style='padding:5px;'><b>24.50</b> (when &pound; symbol is already printed outside box)</td></tr>"
            "</table></div>",
            title="Why Online Platforms Mark Correct Answers Wrong"
        )
        + K.cartoon_tip(get_cartoon("abdul tutor explaining"), "Abdul",
                        "Look closely at the answer box! If the &pound; sign is already printed outside the text input box, DO NOT type &pound; inside the box. Typing '&pound;25.00' into a box preceded by '&pound;' causes the system to read '&pound;&pound;25.00' and mark it wrong!")
        + K.fill_notes("Personal Checklist for Online Computer Tests", 22)
    )
    pages.append(K.page(p4_body, header=(BOOK, "Algorithmic Traps"), footer=BOOK, page_no=4))

    # p5: Diagnostic Error Classification
    p5_body = (
        K.page_title("Diagnostic Error Classification", kicker="Root Cause Taxonomy", badge="CL")
        + K.hero_image(P("adult student thinking puzzled desk study"), "Categorizing your mistake is the first step toward permanent mastery.", 50)
        + K.box_html(
            "<div style='display:grid; grid-template-columns:1fr 1fr; gap:12px; font-size:11pt;'>"
            "<div><b>Type A &bull; Misconception (Process):</b> Choosing an incorrect formula or reversing an operation (e.g. multiplying by 0.15 instead of dividing by 0.85 for reverse discount).</div>"
            "<div><b>Type B &bull; Algorithmic (Format):</b> Correct numerical calculation, but syntax, rounding, or unit formatting triggers an automated red X.</div>"
            "<div><b>Type C &bull; Reading / Comprehension:</b> Overlooking qualifying conditions in the prompt (e.g. <i>'rounded to 1 decimal place'</i> or <i>'excluding VAT'</i>).</div>"
            "<div><b>Type D &bull; Arithmetic Slips:</b> Simple addition or subtraction slips under timed pressure.</div>"
            "</div>",
            title="The 4 Failure Root Causes"
        )
        + K.rule_box("The Golden Rule of Error Logging",
                     "<p>For every red X on your screen, determine whether it was Type A, B, C, or D. If Type A, review the worked model fix. If Type B, write down the formatting rule. If Type C, highlight the prompt text.</p>")
        + K.fill_notes("My Most Frequent Error Category &amp; Corrective Habit", 22)
    )
    pages.append(K.page(p5_body, header=(BOOK, "Error Taxonomy"), footer=BOOK, page_no=5))

    # p6: Score Tracker
    p6_body = (
        K.page_title("Personal Diagnostic Remediation Tracker", kicker="Scores &amp; Remediation Monitoring", badge="TR")
        + K.box_html(
            "<table style='width:100%; border-collapse:collapse; font-size:9pt; text-align:center; line-height:1.25;'>"
            "<tr style='background:#f1f5f9;'><th style='padding:2.5px; text-align:left;'>Mode</th><th style='text-align:left;'>Topic Focus</th><th>Strand</th><th>Initial BKSB</th><th>Drill 1</th><th>Drill 2</th><th>Drill 3</th><th>Status</th></tr>"
            + "".join(f"<tr><td style='padding:2px; border-bottom:1px solid #e2e8f0; text-align:left;'><b>M{i}</b></td>"
                      f"<td style='border-bottom:1px solid #e2e8f0; text-align:left;'>{ssc.BKSB_MODES[i-1]['title'][:24]}...</td>"
                      f"<td style='border-bottom:1px solid #e2e8f0;'>{ssc.BKSB_MODES[i-1]['strand']}</td>"
                      f"<td style='border-bottom:1px solid #e2e8f0;'>[ X ]</td>"
                      f"<td style='border-bottom:1px solid #e2e8f0;'>[ &nbsp; ]</td>"
                      f"<td style='border-bottom:1px solid #e2e8f0;'>[ &nbsp; ]</td>"
                      f"<td style='border-bottom:1px solid #e2e8f0;'>[ &nbsp; ]</td>"
                      f"<td style='border-bottom:1px solid #e2e8f0;'>Pass</td></tr>"
                      for i in range(1, 25))
            + "</table>",
            title="The 24 Diagnostic Remediation Milestones"
        )
        + K.fill_notes("Target Remediation Schedule with Tutor Abdul", 14)
    )
    pages.append(K.page(p6_body, header=(BOOK, "Score Tracker"), footer=BOOK, page_no=6))

    # pp7–p54: 24 Failure Mode Masterclasses (2 pages per mode = 48 pages)
    p_curr = 7
    for m_idx, mode in enumerate(ssc.BKSB_MODES, start=1):
        m_title = mode["title"]
        m_strand = mode["strand"]
        badge = mode["badge"]
        kw = mode["kw"]
        diag = mode["diagnosis"]
        rule = mode["golden_rule"]
        fix = mode["model_fix"]
        drills = mode["drills"]

        # Page 1 of Mode: Diagnostic Autopsy & Worked Model Fix
        p1_b = (
            K.page_title(f"Mode {m_idx} &bull; {m_title}", kicker=f"BKSB Diagnostic Autopsy &bull; Strand: {m_strand}", badge=badge)
            + K.hero_image(P(kw), f"Diagnostic Misconception Analysis: {m_title}", 48)
            + K.box_html(
                f"<div style='font-size:10.5pt; line-height:1.45;'>{diag}</div>",
                title="Diagnostic Autopsy &bull; Root Cause Deconstruction"
            )
            + K.rule_box(f"Golden Rule &bull; Mode {m_idx}", f"<p style='margin:0;'>{rule}</p>")
            + K.box_html(
                f"<div style='font-size:10pt; line-height:1.4;'>{fix}</div>",
                title="Tutor Worked Model Fix"
            )
            + K.fill_notes("Personal Recovery Notes &amp; Golden Rule Summary", 18)
        )
        pages.append(K.page(p1_b, header=(BOOK, f"Mode {m_idx} &bull; Autopsy"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 2 of Mode: Retry & Master Drills (3 independent drills)
        p2_b = (
            K.page_title(f"Mode {m_idx} &bull; Retry &amp; Master Drills", kicker="Independent Practice Booklets &bull; Stage 1 Verification", badge=f"{badge}.R")
            + exam_box(f"Drill {m_idx}.1: {drills[0]}", marks=3)
            + K.fill_grid(f"Candidate Working Grid &bull; Drill {m_idx}.1", min_mm=22)
            + exam_box(f"Drill {m_idx}.2: {drills[1]}", marks=3)
            + K.fill_grid(f"Candidate Working Grid &bull; Drill {m_idx}.2", min_mm=22)
            + exam_box(f"Drill {m_idx}.3: {drills[2]}", marks=4)
            + K.fill_grid(f"Candidate Working Grid &bull; Drill {m_idx}.3", min_mm=22)
            + K.box_html(
                f"<div style='display:flex; justify-content:space-between; font-weight:bold; font-size:11pt;'>"
                f"<span>Drills Completed: [ &nbsp; ] All 3 Correct</span>"
                f"<span>Self-Check Score: _____ / 10</span>"
                f"<span>Mode {m_idx} Mastered: [ &nbsp; ] YES</span>"
                f"</div>",
                title="Candidate Mastery Sign-Off"
            )
        )
        pages.append(K.page(p2_b, header=(BOOK, f"Mode {m_idx} &bull; Retry Drills"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # pp55–p62: 8 Specialist Interface & Rapid Diagnostic Workshops (8 pages)
    spec_workshops = [
        ("Online Drop-down Selectors &amp; Multi-Field Entry", "ws1",
         "Eliminating navigation and data entry errors in digital test portals.",
         "office worker computer monitor keyboard typing",
         "<b>Drop-down Mechanics:</b> Many BKSB and Pearson onscreen tests require selecting units or qualifiers from a secondary drop-down list. If you compute the correct number but leave the drop-down on default, the algorithm marks the entire question zero.<br>"
         "<b>Verification Step:</b> Always read the question sentence aloud to confirm the selected drop-down word matches grammatical context.<br>"
         "<b>Multi-Field Tab Traps:</b> Use the mouse to click directly into each input box rather than pressing Tab.",
         "Practice Drill: A financial scenario asks for annual gross salary and monthly take-home pay across two separate fields. Enter both with exact pence format."),
        ("Coordinate Plotting &amp; Graph Scale Interpretation", "ws2",
         "Mastering interactive chart tools and grid calibration on screen.",
         "architectural blueprint drafting pencil ruler",
         "<b>Digital Graph Interfaces:</b> When clicking to plot a point on an interactive scatter graph, zoom in if possible to ensure the crosshairs align with grid intersections.<br>"
         "<b>Axis Calibration Traps:</b> Always check what each small square represents (e.g. 5 small squares = 10 units means 1 square = 2 units, NOT 1 unit!).",
         "Practice Drill: Identify the scale calibration of a grid where 4 squares represent 50 litres of fuel. Determine the exact value represented by 7 squares."),
        ("Formula Entry Syntax &amp; Mathematical Keypads", "ws3",
         "Translating written mathematical working into digital exam input boxes.",
         "calculator accounting finance numbers calculation",
         "<b>Digital Math Keypads:</b> When an online exam asks for an equation or check, use standard characters: <code>*</code> or <code>x</code> for multiply, <code>/</code> for divide, <code>^</code> or superscript for powers.<br>"
         "<b>Parentheses Rule:</b> Always enclose compound operations in brackets: <code>(45 + 15) / 2 = 30</code>, whereas <code>45 + 15 / 2 = 52.5</code>.",
         "Practice Drill: Express the mathematical check for 28 &times; 14 = 392 using reverse division in digital input format."),
        ("Drag-and-Drop Matching &amp; Sequence Ordering", "ws4",
         "Navigating kinetic UI questions without accidental placement errors.",
         "computer programmer code software development screen",
         "<b>Drag-and-Drop Mechanics:</b> Ensure the dragged box snaps into the target slot with a visual highlight border before releasing the mouse button.<br>"
         "<b>Sequence Questions:</b> Re-read the full sequence from start to finish after placing all items to verify logical chronological flow.",
         "Practice Drill: Arrange four stages of an emergency workplace evacuation procedure into chronological sequence."),
        ("Rapid Diagnostic Challenge &bull; Part 1 (Maths Number &amp; Finance)", "ws5",
         "Timed 10-minute remediation sprint across high-frequency number traps.",
         "business finance money calculator currency desk",
         "<b>Rapid Challenge 1:</b> Work out 15% discount on &pound;460.<br>"
         "<b>Rapid Challenge 2:</b> An invoice is &pound;750 + 20% VAT. Calculate gross payable.<br>"
         "<b>Rapid Challenge 3:</b> Share &pound;960 in the ratio 3:5.<br>"
         "<b>Rapid Challenge 4:</b> Convert 3 hours 36 minutes to decimal hours.",
         "Candidate Working Grid &bull; Rapid Sprint 1"),
        ("Rapid Diagnostic Challenge &bull; Part 2 (Maths Measures &amp; Geometry)", "ws6",
         "Timed 10-minute remediation sprint across compound units and shapes.",
         "construction engineer site surveyor measuring tape",
         "<b>Rapid Challenge 1:</b> Calculate area of circle with diameter 8 m (&pi; = 3.14).<br>"
         "<b>Rapid Challenge 2:</b> Van travels 150 miles at 50 mph. Find travel time.<br>"
         "<b>Rapid Challenge 3:</b> Cylinder radius 1 m, height 3 m. Calculate volume in litres.<br>"
         "<b>Rapid Challenge 4:</b> Ladder height 4 m, base 3 m. Calculate ladder length.",
         "Candidate Working Grid &bull; Rapid Sprint 2"),
        ("Rapid Diagnostic Challenge &bull; Part 3 (English SPaG &amp; Punctuation)", "ws7",
         "Timed 10-minute remediation sprint across high-frequency grammar traps.",
         "writing document contract legal notes fountain pen",
         "<b>Rapid Challenge 1:</b> Fix the comma splice: 'The report was late, the data was accurate.'<br>"
         "<b>Rapid Challenge 2:</b> Insert apostrophe: 'The trainees tools were inspected.'<br>"
         "<b>Rapid Challenge 3:</b> Correct the homophone: 'Their going to collect there passes.'<br>"
         "<b>Rapid Challenge 4:</b> Eliminate the contraction: 'We couldn't verify the records.'",
         "Candidate Working Grid &bull; Rapid Sprint 3"),
        ("Rapid Diagnostic Challenge &bull; Part 4 (English Reading &amp; Synthesis)", "ws8",
         "Timed 10-minute remediation sprint across bias and comparison questions.",
         "student studying books library academic reading",
         "<b>Rapid Challenge 1:</b> Identify one fact and one opinion in a transport press release.<br>"
         "<b>Rapid Challenge 2:</b> Explain the implicit meaning of 'kicking the problem into the long grass'.<br>"
         "<b>Rapid Challenge 3:</b> Write a comparative sentence contrasting Text A and Text B using 'Whereas'.<br>"
         "<b>Rapid Challenge 4:</b> Identify two organizational features in a guidance brochure.",
         "Candidate Working Grid &bull; Rapid Sprint 4")
    ]

    for ws_title, badge, lead, photo_kw, theory_html, drill_title in spec_workshops:
        ws_body = (
            K.page_title(ws_title, kicker="Specialist Interface &amp; Rapid Diagnostic Sprint", badge=badge.upper())
            + K.hero_image(P(photo_kw), lead, 48)
            + K.box_html(f"<div style='font-size:10.5pt; line-height:1.45;'>{theory_html}</div>", title="Diagnostic Sprint Protocol")
            + K.box_html(f"<div style='font-size:11pt; font-weight:bold; color:var(--accent);'>{drill_title}</div>", title="Hands-On Response Area")
            + K.fill_notes("Candidate Working Lines &bull; Challenge Solution", 55)
        )
        pages.append(K.page(ws_body, header=(BOOK, "Diagnostic Sprint"), footer=BOOK, page_no=p_curr))
        p_curr += 1
    # pp63–p78: 4 Full Sectional Diagnostic Examination Papers (16 pages)
    for paper in ssc.BKSB_PAPERS:
        p_title = paper["title"]
        badge = paper["badge"]
        for p_page in paper["pages"]:
            q_html = "".join(
                f"<div style='margin-bottom:2mm; padding:2mm 3.5mm; background:#f8fafc; border-left:3.5mm solid var(--accent); border-radius:4px;'>"
                f"<div style='font-size:10pt; line-height:1.35;'><b>Question {q_i+1}:</b> {q_item['q']} <span style='float:right; font-weight:bold; color:var(--accent);'>[{q_item['marks']} Marks]</span></div>"
                f"<div class='aline' style='height:5.5mm; border-bottom:1px solid #cbd5e1; margin-top:1.5mm;'></div>"
                f"</div>"
                for q_i, q_item in enumerate(p_page["questions"])
            )
            p_body = (
                K.page_title(f"{p_title} &bull; {p_page['subtitle']}", kicker="Timed Sectional Diagnostic Exam", badge=badge)
                + K.box_html(f"<div style='font-size:9.5pt; line-height:1.35;'>{p_page['intro']}</div>", title="Examination Instructions &amp; Permitted Equipment")
                + q_html
                + K.fill_notes("Candidate Working Lines &amp; Final Solution", 18)
            )
            pages.append(K.page(p_body, header=(BOOK, p_title), footer=BOOK, page_no=p_curr))
            p_curr += 1


    # pp63–p82: Back matter reference section (via K.ref_pages)
    ref_blocks = []
    # Solutions for all 24 Modes
    for m_idx in range(1, 25):
        for title_str, sol_html in ssr.BKSB_STAGE2_SOLUTIONS[m_idx]:
            ref_blocks.append(K.ref_block(title_str, sol_html))
    # Solutions for 4 Diagnostic Papers
    for p_num in range(1, 5):
        for title_str, sol_html in ssr.BKSB_PAPERS_SOLUTIONS.get(p_num, []):
            ref_blocks.append(K.ref_block(title_str, sol_html))
    # Golden rules
    ref_blocks.append(K.ref_block("Master Diagnostic Golden Rules Directory", ssr.BKSB_GOLDEN_RULES))
    # Glossary
    gloss_html = "".join(f"<dl><dt>{t}</dt><dd>{d}</dd></dl>" for t, d in ssr.BKSB_GLOSSARY)
    ref_blocks.append(K.ref_block("Diagnostic &amp; Algorithmic Glossary", gloss_html))
    # Index
    ix_html = ""
    for letter, entries in ssr.BKSB_INDEX:
        items = "".join(f"<div class='ix'><span>{t}</span><span>{p}</span></div>" for t, p in entries)
        ix_html += f"<div class='ix-letter'>{letter}</div>{items}"
    ref_blocks.append(K.ref_block("Remediation &amp; Misconception Index", ix_html))

    ref_page_list = K.ref_pages("Official Stage 2 Worked Solutions &amp; Directory", ref_blocks,
                                BOOK, start_page=p_curr, subtitle="Complete Step-by-Step Worked Models for All 72 Retry Drills",
                                cols=2, theme=cover_theme, notes_title="Candidate Error Analysis &amp; Golden Rule Checklist")
    pages.extend(ref_page_list)
    p_curr += len(ref_page_list)

    # Re-assessment Log & Scaling (pp 83–86)
    # Page 83: Re-assessment Log
    rl_body = (
        K.page_title("Diagnostic Re-Assessment Log", kicker="Post-Remediation Progression Audit", badge="LG")
        + K.box_html(
            "<table style='width:100%; border-collapse:collapse; font-size:10.5pt; text-align:center; line-height:1.4;'>"
            "<tr style='background:#f1f5f9;'><th style='padding:5px; text-align:left;'>Assessment Milestone</th><th>Initial Working Level</th><th>Post-Workbook Level</th><th>Target Functional Level</th><th>Sign-Off</th></tr>"
            "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0; text-align:left;'>BKSB Baseline Diagnostics</td><td>Level 1 (42%)</td><td>Level 2 (84%)</td><td>Level 2 Pass</td><td>Abdul</td></tr>"
            "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0; text-align:left;'>OneAdvanced Progress Check 1</td><td>Level 1 Borderline</td><td>Level 2 Secure</td><td>Level 2 Pass</td><td>Abdul</td></tr>"
            "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0; text-align:left;'>OneAdvanced Progress Check 2</td><td>Level 2 Emerging</td><td>Level 2 High Pass</td><td>Level 2 Pass</td><td>Abdul</td></tr>"
            "<tr><td style='padding:5px; text-align:left;'>Final Exam Readiness Audit</td><td>Level 2 Secure</td><td>Level 2 Distinction</td><td>Level 2 Pass</td><td>Abdul</td></tr>"
            "</table>",
            title="Learner Diagnostic Growth Record"
        )
        + K.cartoon_tip(get_cartoon("priya tutor writing notes"), "Priya",
                        "Celebrate your diagnostic progress! Moving from Level 1 Emerging to Level 2 Secure represents complete remediation of core mathematical and literacy misconceptions.")
        + K.fill_notes("Personal Reflections &amp; Future Learning Targets", 18)
    )
    pages.append(K.page(rl_body, header=(BOOK, "Re-Assessment Log"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Page 84: Official Certificate
    cert_body = (
        K.page_title("Certificate of Diagnostic Mastery", kicker="Diagnostic Remediation Sign-Off", badge="CERT")
        + K.hero_image(P("adult student graduation diploma celebration success"), "Remediating foundational misconceptions ensures permanent exam excellence.", 50)
        + K.box_html(
            "<div style='text-align:center; padding:10px; font-size:11.5pt; line-height:1.5;'>"
            "<p style='margin:0 0 4px 0;'>This certifies that</p>"
            "<p style='font-size:16pt; font-weight:bold; border-bottom:2px solid var(--accent); display:inline-block; min-width:300px; padding-bottom:3px; margin:4px 0;'>&nbsp;</p>"
            "<p style='margin:4px 0;'>has completed all 24 High-Frequency Diagnostic Failure Mode Masterclasses and demonstrated Level 2 mastery on independent retry drills.</p>"
            "<table style='width:100%; margin-top:12px; font-size:10.5pt; border-collapse:collapse;'>"
            "<tr><td style='text-align:left;'><b>Lead Tutor:</b> Abdul</td><td style='text-align:right;'><b>Date Verified:</b> _______________</td></tr>"
            "<tr><td style='text-align:left;'><b>Remediation Score:</b> 72 / 72 Drills</td><td style='text-align:right;'><b>Exam Centre:</b> Oxford Health OH</td></tr>"
            "</table>"
            "</div>",
            title="Master Functional Skills &bull; Certificate of Diagnostic Mastery"
        )
        + K.fill_notes("Final Examination Tips &amp; Golden Rule Memory Reminders", 18)
    )
    pages.append(K.page(cert_body, header=(BOOK, "Mastery Certificate"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Inside Back Cover & Back Cover
    pages.append(K.back_cover(back_cov))
    pdf_path = DOWNLOADS / "MasterFunctionalSkills_BKSB_Remediation_Workbook.pdf"
    print(f"Total Pages Assembled: {len(pages)}")
    res = K.render_pdf(pages, pdf_path, theme=cover_theme, entry3=False, title="Master Functional Skills - BKSB Remediation Workbook")
    print(f"Rendered: {res['pdf']} ({len(pages)} pages)")
    return pdf_path

# =============================================================================
# Main Dispatcher
# =============================================================================
def main():
    import argparse
    parser = argparse.ArgumentParser(description="Build Master Functional Skills Specialist Suite (A4)")
    parser.add_argument("--book", choices=["maths_l2", "english_l2", "digital", "bksb", "all"], default="all",
                        help="Select publication to build")
    args = parser.parse_args()

    books_to_build = []
    if args.book in ("maths_l2", "all"):
        books_to_build.append(("Mock Pack Maths L2", build_mock_maths_l2))
    if args.book in ("english_l2", "all"):
        books_to_build.append(("Mock Pack English L2", build_mock_english_l2))
    if args.book in ("digital", "all"):
        books_to_build.append(("Digital Skills Handbook", build_digital_skills_handbook))
    if args.book in ("bksb", "all"):
        books_to_build.append(("BKSB Remediation Workbook", build_bksb_remediation_workbook))

    generated_pdfs = []
    for name, builder_fn in books_to_build:
        print(f"\nStarting build: {name}")
        pdf = builder_fn()
        generated_pdfs.append(pdf)

    print("\n" + "="*70)
    print("SPECIALIST SUITE BUILD COMPLETE!")
    print("="*70)
    ALT_DOWNLOADS = Path("/home/subi/Projects/masterfunctionalskills.co.uk/assets/downloads")
    ALT_DOWNLOADS.mkdir(parents=True, exist_ok=True)
    DOCUMENTS.mkdir(parents=True, exist_ok=True)
    for p in generated_pdfs:
        print(f"  - {p.name}")
        try:
            shutil.copy2(p, ALT_DOWNLOADS / p.name)
            shutil.copy2(p, DOCUMENTS / p.name)
            print(f"    -> Synced to Projects/ and Documents/")
        except Exception as e:
            print(f"    -> Copy error: {e}")

if __name__ == "__main__":
    main()
