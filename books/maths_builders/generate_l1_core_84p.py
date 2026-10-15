#!/usr/bin/env python3
"""
books/maths_builders/generate_l1_core_84p.py
Constructs the complete 84-page MasterFunctionalSkills_Maths_Level_1_Core_Guide.pdf
Strictly mapped to Pearson Edexcel Reformed Functional Skills Mathematics Level 1.
Features Raymond Murphy-style character vignettes with speech bubbles, annotated diagrams,
guided calculation scaffolding, 4-page strand checkpoints, realistic mock exam, and complete mark scheme.
"""

import os
import sys
import subprocess
import shutil

PROJECT_DIR = "/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk"
DOWNLOADS_DIR = os.path.join(PROJECT_DIR, "assets", "downloads")
DOCUMENTS_DIR = "/home/subi/Documents"
BOOKS_IMG_DIR = os.path.join(PROJECT_DIR, "assets", "img", "books")
SCRATCH_DIR = os.path.join(PROJECT_DIR, "scratch", "book_build_full")
CHROME_BIN = "/usr/lib/chromium/chromium"

os.makedirs(DOWNLOADS_DIR, exist_ok=True)
os.makedirs(DOCUMENTS_DIR, exist_ok=True)
os.makedirs(SCRATCH_DIR, exist_ok=True)

if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

from book_theme import get_shared_css, wrap_page

def build_l1_core_guide():
    front_img = os.path.join(BOOKS_IMG_DIR, "maths_l1_core_cover_page-1.png")
    back_img = os.path.join(BOOKS_IMG_DIR, "maths_l1_core_cover_page-2.png")
    out_name = "MasterFunctionalSkills_Maths_Level_1_Core_Guide.pdf"
    target_downloads = os.path.join(DOWNLOADS_DIR, out_name)
    target_documents = os.path.join(DOCUMENTS_DIR, out_name)

    pages = []

    # Character vignette helper (Murphy style)
    def tutor_vignette(character_icon, name, role, speech_text):
        return f"""
        <div style="display:flex; align-items:flex-start; gap:8px; margin:4px 0; background:#fffbeb; border:1px solid #fde68a; border-radius:6px; padding:4px 8px;">
          <div style="font-size:18pt; line-height:1; flex-shrink:0;">{character_icon}</div>
          <div style="font-size:7.4pt; color:#1e293b;">
            <strong style="color:var(--theme);">{name} ({role}):</strong> "{speech_text}"
          </div>
        </div>
        """

    # Helper for Practice Pages (Page 2 of 2-page topic spreads)
    def practice_page(title, standard, page_num, scaffold_html, q1_html, q2_html, q3_html):
        content = f"""
        <div style="font-size:7.5pt; font-weight:800; color:var(--theme); text-transform:uppercase; letter-spacing:0.5px; margin-bottom:2px;">
          Guided Practice &bull; Workspace &bull; {standard}
        </div>
        <h2 style="font-size:10.5pt; margin-bottom:4px;">{title}: Guided Practice Drills</h2>

        <!-- Guided Calculation Scaffold -->
        <div class="box-concept" style="padding:5px 8px; margin-bottom:4px; border-left-color:var(--accent);">
          <strong style="color:var(--theme); font-size:7.8pt;">Guided Calculation Frame:</strong>
          {scaffold_html}
        </div>

        <!-- Question 1: Foundation / Technique -->
        <div class="q-card" style="padding:5px 8px; margin:4px 0;">
          <div class="q-header">
            <span class="q-num">Exercise A: Foundation Technique Drill</span>
            <span class="q-marks">[2 Marks]</span>
          </div>
          <p style="font-size:7.8pt; margin:0 0 3px 0;">{q1_html}</p>
          <div class="ruled-workspace" style="height:48px;">
            <span class="workspace-hint">Show method &amp; intermediate working</span>
          </div>
          <div class="answer-line">Answer: <span class="answer-blank" style="min-width:140px;"></span></div>
        </div>

        <!-- Question 2: Intermediate Problem Solving -->
        <div class="q-card" style="padding:5px 8px; margin:4px 0;">
          <div class="q-header">
            <span class="q-num">Exercise B: Workplace Problem Solving</span>
            <span class="q-marks">[2 Marks]</span>
          </div>
          <p style="font-size:7.8pt; margin:0 0 3px 0;">{q2_html}</p>
          <div class="ruled-workspace" style="height:48px;">
            <span class="workspace-hint">Show full working and units</span>
          </div>
          <div class="answer-line">Answer: <span class="answer-blank" style="min-width:140px;"></span></div>
        </div>

        <!-- Question 3: Realistic Exam-Style Challenge -->
        <div class="q-card" style="padding:5px 8px; margin:4px 0;">
          <div class="q-header">
            <span class="q-num">Exercise C: Exam-Style Multi-Step Challenge</span>
            <span class="q-marks">[3 Marks]</span>
          </div>
          <p style="font-size:7.8pt; margin:0 0 3px 0;">{q3_html}</p>
          <div class="ruled-workspace" style="height:55px;">
            <span class="workspace-hint">State assumptions, calculations, and conclusion</span>
          </div>
          <div class="answer-line">Decision / Final Answer: <span class="answer-blank" style="min-width:180px;"></span></div>
        </div>
        """
        return wrap_page(content, page_num, "Strand Practice Drill", standard, "Maths Level 1 Core Revision Guide")

    # Helper for Checkpoint pages
    def checkpoint_page(strand_name, part_label, page_num, total_marks, q_list):
        items_html = ""
        for q_num, marks, q_text, box_height in q_list:
            items_html += f"""
            <div class="q-card" style="padding:6px 9px; margin:5px 0;">
              <div class="q-header">
                <span class="q-num">Question {q_num}</span>
                <span class="q-marks">[{marks} Marks]</span>
              </div>
              <p style="font-size:7.9pt; margin:0 0 4px 0;">{q_text}</p>
              <div class="ruled-workspace" style="height:{box_height}px;">
                <span class="workspace-hint">Show all your working clearly</span>
              </div>
              <div class="answer-line">Answer: <span class="answer-blank" style="min-width:160px;"></span></div>
            </div>
            """
        content = f"""
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1.5px solid var(--theme); padding-bottom:3px; margin-bottom:5px;">
          <div>
            <h2 style="margin:0; font-size:11pt; color:var(--theme);">{strand_name} Checkpoint Review</h2>
            <div style="font-size:7.5pt; color:#64748b;"><strong>{part_label}</strong> &bull; Total Available Marks: {total_marks}</div>
          </div>
          <div style="background:#eff6ff; border:1px solid #bfdbfe; border-radius:4px; padding:3px 8px; font-size:7.5pt; font-weight:700; color:#1e40af;">
            Passing Benchmark: 70%
          </div>
        </div>
        {items_html}
        """
        return wrap_page(content, page_num, f"{strand_name} Checkpoint Review", part_label, "Maths Level 1 Core Revision Guide")

    # Helper for Mock Exam pages
    def mock_page(sec_title, page_num, q_list):
        items_html = ""
        for q_num, marks, q_text, box_h, ans_prompt in q_list:
            items_html += f"""
            <div class="q-card" style="padding:6px 9px; margin:5px 0;">
              <div class="q-header">
                <span class="q-num">Question {q_num}</span>
                <span class="q-marks">[{marks} Marks]</span>
              </div>
              <p style="font-size:7.9pt; margin:0 0 4px 0;">{q_text}</p>
              <div class="ruled-workspace" style="height:{box_h}px;">
                <span class="workspace-hint">Show method, process and final values clearly</span>
              </div>
              <div class="answer-line">{ans_prompt}: <span class="answer-blank" style="min-width:180px;"></span></div>
            </div>
            """
        content = f"""
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1.5px solid var(--theme); padding-bottom:3px; margin-bottom:5px;">
          <h2 style="margin:0; font-size:11pt; color:var(--theme);">Official Mock Examination &bull; {sec_title}</h2>
          <span style="font-size:7.5pt; font-weight:700; color:#475569;">Functional Skills Maths Level 1</span>
        </div>
        {items_html}
        """
        return wrap_page(content, page_num, f"Official Mock Exam &bull; {sec_title}", "Standard Exam Simulation", "Maths Level 1 Core Revision Guide")

    # Helper for Mark Scheme pages
    def mark_scheme_page(title, sub_title, page_num, tables_html):
        content = f"""
        <div style="border-bottom:1.5px solid var(--theme); padding-bottom:3px; margin-bottom:6px;">
          <h2 style="margin:0; font-size:11pt; color:var(--theme);">{title}</h2>
          <div style="font-size:7.5pt; color:#64748b;"><strong>{sub_title}</strong> &bull; Marking Codes: [P1] Process &bull; [M1] Method &bull; [A1] Accuracy &bull; [B1] Independent</div>
        </div>
        {tables_html}
        """
        return wrap_page(content, page_num, title, sub_title, "Maths Level 1 Core Revision Guide")

    # =========================================================================
    # BUILD PAGES 1 TO 84
    # =========================================================================

    # PAGE 1: Front Cover
    pages.append(f"""
    <div class="page cover-full-page">
      <img src="file://{front_img}" class="cover-full-img" alt="Level 1 Core Guide Front Cover">
    </div>
    """)

    # PAGE 2: Inside Cover & Ofqual Mapping
    p2 = """
    <h1>Functional Skills Maths Level 1 Core Revision Guide</h1>
    <div style="font-size:8.5pt; color:#475569; margin-bottom:8px;"><strong>Specification Standard:</strong> Pearson Edexcel Reformed Functional Skills Mathematics (Level 1) &bull; Ofqual Regulated</div>

    <div class="box-concept">
      <h3 style="margin-top:0;">Your Journey to Level 1 Mathematics Success</h3>
      <p>Functional Skills Maths Level 1 provides the vital mathematical foundations required for employment, apprenticeships, college progression, and everyday adult life. This comprehensive revision manual explains each statutory standard with clear visual models, step-by-step calculation frames, and practical workplace examples.</p>
    </div>

    <h2>Reformed Level 1 Curriculum Framework</h2>
    <table class="cgp-table">
      <tr>
        <th style="width:28%;">Curriculum Strand</th>
        <th style="width:18%;">Standards</th>
        <th>Core Mathematical Domains &amp; Exam Weighting</th>
      </tr>
      <tr>
        <td><strong>1. Number &amp; Number Systems</strong></td>
        <td>L1.1 &ndash; L1.16</td>
        <td>Whole numbers up to 1,000,000, negative numbers in context, addition, subtraction, multiplication, division, fractions, decimals, percentages, simple ratios, rounding and order of operations (approx. 35% of marks).</td>
      </tr>
      <tr>
        <td><strong>2. Measures, Shape &amp; Space</strong></td>
        <td>L1.17 &ndash; L1.27</td>
        <td>Metric units (length, weight, capacity), money and wages, 12-hour and 24-hour time, perimeter, area of rectangles, volume of cuboids, 2D angles and polygons, 3D shapes, and scale plans (approx. 35% of marks).</td>
      </tr>
      <tr>
        <td><strong>3. Handling Information &amp; Data</strong></td>
        <td>L1.28 &ndash; L1.36</td>
        <td>Tally charts, frequency tables, bar charts, pictograms, line graphs, simple pie charts, mean average, range, probability scale from 0 to 1, and listing possible outcomes (approx. 30% of marks).</td>
      </tr>
    </table>

    <div class="grid-2col" style="margin-top:6px;">
      <div class="box-example">
        <h3 style="margin-top:0; color:#15803d;">Section A: Non-Calculator</h3>
        <p><strong>Duration:</strong> 25 minutes &bull; <strong>Marks:</strong> 14 marks<br>
        Tests mental arithmetic, fraction equivalences, written long multiplication/division, and basic number operations without electronic calculators.</p>
      </div>
      <div class="box-example">
        <h3 style="margin-top:0; color:#15803d;">Section B: Calculator Allowed</h3>
        <p><strong>Duration:</strong> 1 hour 30 minutes &bull; <strong>Marks:</strong> 42 marks<br>
        Tests multi-step practical tasks, compound shapes, cost calculations, time schedules, data interpretations, and probability.</p>
      </div>
    </div>

    """ + tutor_vignette("🧑‍🏫", "Tutor Marcus", "Senior Maths Educator", "Welcome! Don't worry if maths has been daunting in the past. We've broken down every topic into a 2-page spread: clear concept on the left, guided practice on the right. You can do this!") + """
    """
    pages.append(wrap_page(p2, 2, "Master Functional Skills &bull; Maths Level 1", "Curriculum Framework", "Maths Level 1 Core Revision Guide"))

    # =========================================================================
    # STRAND 1: NUMBER & NUMBER SYSTEMS (PAGES 3 - 26)
    # =========================================================================

    # TOPIC 1: PAGE 3 (Theory) & PAGE 4 (Practice)
    p3 = """
    <h2>Large Numbers up to 1,000,000 &amp; Negative Numbers</h2>
    <p>Reading, writing, ordering and comparing large integers, and working with positive and negative numbers in practical contexts.</p>
    <div class="box-concept">
      <span class="tag-label tag-blue">Key Principle</span> <strong>Place Value to One Million:</strong>
      In <strong>845,230</strong>: The 8 is Hundred Thousands ($800,000$), 4 is Ten Thousands ($40,000$), 5 is Thousands ($5,000$), 2 is Hundreds ($200$), 3 is Tens ($30$), and 0 is Units.
    </div>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1e40af;">Negative Numbers: Thermometers &amp; Bank Statements</h3>
      <p>Negative numbers are values below zero. Moving <strong>right</strong> on the number line is warmer or adding money (+). Moving <strong>left</strong> is colder or taking away money (-).<br>
      <strong>Comparing:</strong> $-15^\\circ\\text{C}$ is colder than $-4^\\circ\\text{C}$, so $-4 > -15$.</p>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Chiller Temperature Difference</span>
      <p>A supermarket walk-in freezer is at <strong>-18°C</strong>. The main fresh food aisle is at <strong>+6°C</strong>. What is the temperature difference?</p>
      <div class="step-row"><span>Step 1: Jump from -18°C up to 0°C</span><strong>18°C rise</strong></div>
      <div class="step-row"><span>Step 2: Jump from 0°C up to +6°C</span><strong>6°C rise</strong></div>
      <div class="step-row"><span>Step 3: Total difference: 18 + 6</span><strong>24°C difference</strong></div>
    </div>
    <div class="box-trap">
      <span class="tag-label tag-red">Tutor Trap</span> <strong>Negative Signs:</strong> Learners often calculate $6 - 18 = -12$ and forget that finding the difference means finding the total distance between two values on the line ($6 - (-18) = 6 + 18 = 24$).
    </div>
    """ + tutor_vignette("👩‍💼", "Priya", "Retail Supervisor", "In our warehouse, we use negative numbers daily for inventory stock shortages and freezer logs. Think of zero as the baseline!") + """
    """
    pages.append(wrap_page(p3, 3, "Strand 1: Number & Number Systems", "Standards: L1.1, L1.2", "Maths Level 1 Core Revision Guide"))

    p4_scaffold = """
    <div class="step-row"><span>Step 1: Start at current freezer temp</span><span>$-14^\\circ\\text{C}$</span></div>
    <div class="step-row"><span>Step 2: Add daytime temp rise (+5°C)</span><span>$-14 + 5 = -9^\\circ\\text{C}$</span></div>
    <div class="step-row"><span>Step 3: Subtract night-time drop (-4°C)</span><span>$-9 - 4 = \\mathbf{-13^\\circ\\text{C}}$</span></div>
    """
    p4 = practice_page(
        "Large & Negative Numbers", "Standards L1.1, L1.2", 4, p4_scaffold,
        "Write in words: a) $450,205$ &emsp; b) Write in figures: 'Three hundred and eight thousand, and forty-two'.",
        "Put these temperatures in order starting with the coldest: $+4^\\circ\\text{C}, -8^\\circ\\text{C}, 0^\\circ\\text{C}, -12^\\circ\\text{C}, +9^\\circ\\text{C}, -2^\\circ\\text{C}$.",
        "A business bank account has an overdraft balance of $-£340$. The owner pays in a client cheque for $£850$ and pays a supplier bill of $£620$. What is the closing balance of the account?"
    )
    pages.append(p4)

    # TOPIC 2: PAGE 5 (Theory) & PAGE 6 (Practice)
    p5 = """
    <h2>The Four Operations (+, &minus;, &times;, &divide;) Non-Calc</h2>
    <p>Section A strictly forbids calculators. You must show robust, reliable written column methods for all four arithmetic operations.</p>
    <div class="grid-2col">
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8;">Column Multiplication</h3>
        <p>Multiply by units, then tens (remember place-holder zero!), then add.<br>
        <strong>Example: $234 \\times 16$</strong><br>
        $234 \\times 6 = 1,404$<br>
        $234 \\times 10 = 2,340$<br>
        Add: $1,404 + 2,340 = \\mathbf{3,744}$.</p>
      </div>
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8;">Short 'Bus Stop' Division</h3>
        <p>Divide digit by digit from left to right, carrying remainders.<br>
        <strong>Example: $852 \\div 6$</strong><br>
        &bull; $6$ into $8$ goes $1$ remainder $2$<br>
        &bull; $6$ into $25$ goes $4$ remainder $1$<br>
        &bull; $6$ into $12$ goes $2$. Result: $\\mathbf{142}$.</p>
      </div>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Subtraction with Borrowing</span>
      <p>Subtract <strong>£1,458</strong> from <strong>£3,200</strong>.</p>
      <div class="step-row"><span>Align columns vertically</span><strong>3,200 - 1,458</strong></div>
      <div class="step-row"><span>Borrow from hundreds column: 3,190 + 10</span><strong>10 - 8 = 2 units</strong></div>
      <div class="step-row"><span>Tens column: 9 - 5</span><strong>4 tens</strong></div>
      <div class="step-row"><span>Hundreds: 1 - 4 (borrow from thousands: 11 - 4)</span><strong>7 hundreds</strong></div>
      <div class="step-row"><span>Thousands: 2 - 1</span><strong>1 thousand</strong></div>
      <div class="step-row"><span>Final difference</span><strong>£1,742</strong></div>
    </div>
    """ + tutor_vignette("🧑‍🔧", "Dave", "Maintenance Tech", "When I cut timber or cable, I always do a quick inverse check: if 3,744 ÷ 16 gives 234, I know my cut lengths are spot on!") + """
    """
    pages.append(wrap_page(p5, 5, "Strand 1: Number & Number Systems", "Standards: L1.3", "Maths Level 1 Core Revision Guide"))

    p6_scaffold = """
    <div class="step-row"><span>Step 1: Set up column multiplication</span><span>$318 \\times 24$</span></div>
    <div class="step-row"><span>Step 2: Multiply by 4 units</span><span>$318 \\times 4 = 1,272$</span></div>
    <div class="step-row"><span>Step 3: Multiply by 20 (zero placed)</span><span>$318 \\times 20 = 6,360$</span></div>
    <div class="step-row"><span>Step 4: Add totals</span><span>$1,272 + 6,360 = \\mathbf{7,632}$</span></div>
    """
    p6 = practice_page(
        "Four Operations (Non-Calc)", "Standards L1.3", 6, p6_scaffold,
        "Calculate without using a calculator: a) $456 + 1,289$ &emsp; b) $2,000 - 743$.",
        "A warehouse worker packs 18 boxes. Each box contains 24 bottles of shampoo. How many bottles are there in total? Show your column method.",
        "A catering manager divides 648 sandwich portions equally between 8 corporate lunch platters. How many sandwich portions go on each platter? Show a check using multiplication."
    )
    pages.append(p6)

    # TOPIC 3: PAGE 7 (Theory) & PAGE 8 (Practice)
    p7 = """
    <h2>Multiples, Factors, Primes &amp; Square Numbers</h2>
    <p>Understanding number properties aids mental arithmetic, simplifying fractions, and recognizing numerical patterns.</p>
    <div class="grid-2col">
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8;">Multiples &amp; Factors</h3>
        <p>&bull; <strong>Multiples:</strong> Numbers in a times table.<br>
        Multiples of 6: 6, 12, 18, 24, 30...<br>
        &bull; <strong>Factors:</strong> Numbers that divide into a target number exactly without a remainder.<br>
        Factors of 18: 1, 2, 3, 6, 9, 18.</p>
      </div>
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8;">Primes &amp; Square Numbers</h3>
        <p>&bull; <strong>Prime Number:</strong> Has exactly 2 factors (1 and itself).<br>
        First primes: 2, 3, 5, 7, 11, 13, 17, 19.<br>
        &bull; <strong>Square Number ($n^2$):</strong> Result of multiplying a number by itself.<br>
        $1, 4, 9, 16, 25, 36, 49, 64, 81, 100$.</p>
      </div>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Finding Common Factors</span>
      <p>A joiner has two wooden planks: $24\\text{ cm}$ and $36\\text{ cm}$. What is the longest equal length he can cut from both without waste?</p>
      <div class="step-row"><span>Factors of 24: 1, 2, 3, 4, 6, 8, 12, 24</span><strong>List factors</strong></div>
      <div class="step-row"><span>Factors of 36: 1, 2, 3, 4, 6, 9, 12, 18, 36</span><strong>List factors</strong></div>
      <div class="step-row"><span>Highest Common Factor (HCF)</span><strong>12 cm</strong></div>
    </div>
    <div class="box-trap">
      <span class="tag-label tag-red">Tutor Trap</span> <strong>Is 1 a Prime?</strong> 1 is NOT a prime number because it only has 1 factor (itself). A prime must have exactly 2 distinct factors! Also, 2 is the ONLY even prime number.
    </div>
    """
    pages.append(wrap_page(p7, 7, "Strand 1: Number & Number Systems", "Standards: L1.4", "Maths Level 1 Core Revision Guide"))

    p8_scaffold = """
    <div class="step-row"><span>Step 1: Square number definition</span><span>Multiply number by itself ($7 \\times 7$)</span></div>
    <div class="step-row"><span>Step 2: Calculate</span><span>$7^2 = 49$</span></div>
    <div class="step-row"><span>Step 3: Square root check</span><span>$\\sqrt{49} = \\mathbf{7}$</span></div>
    """
    p8 = practice_page(
        "Factors, Primes & Squares", "Standards L1.4", 8, p8_scaffold,
        "List all the factors of 28.",
        "From this list of numbers: 4, 7, 9, 15, 18, 23, 25, 30. Identify: a) The prime numbers &emsp; b) The square numbers.",
        "A landscaper has 60 square paving slabs. He wants to arrange them in a solid rectangular patio. List all the different rectangular arrangements he can make (e.g. 2 by 30)."
    )
    pages.append(p8)

    # TOPIC 4: PAGE 9 (Theory) & PAGE 10 (Practice)
    p9 = """
    <h2>Fractions: Equivalences, Simplifying &amp; Ordering</h2>
    <p>Fractions represent equal parts of a whole. Simplifying fractions and finding common denominators are vital exam skills.</p>
    <div class="grid-2col">
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8;">Equivalent Fractions</h3>
        <p>Multiply or divide the numerator and denominator by the exact same number.<br>
        $$\\frac{3}{4} = \\frac{3 \\times 2}{4 \\times 2} = \\frac{6}{8} = \\frac{3 \\times 5}{4 \\times 5} = \\frac{15}{20}$$</p>
      </div>
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8;">Simplifying to Lowest Terms</h3>
        <p>Divide top and bottom by their common factor until no further division is possible.<br>
        $$\\frac{18}{24} = \\frac{18 \\div 6}{24 \\div 6} = \\mathbf{\\frac{3}{4}}$$</p>
      </div>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Comparing Fractions</span>
      <p>Which is larger: <strong>$\\frac{3}{5}$</strong> or <strong>$\\frac{5}{8}$</strong>?</p>
      <div class="step-row"><span>Find common denominator for 5 and 8: 5 × 8</span><strong>40</strong></div>
      <div class="step-row"><span>Convert 3/5: (3 × 8) / (5 × 8)</span><strong>24/40</strong></div>
      <div class="step-row"><span>Convert 5/8: (5 × 5) / (8 × 5)</span><strong>25/40</strong></div>
      <div class="step-row"><span>Compare numerators: 25 > 24</span><strong>5/8 is larger</strong></div>
    </div>
    """ + tutor_vignette("🧑‍🍳", "Chef Sam", "Head Chef", "In the kitchen, if a recipe calls for 3/4 pint of cream and you only have an 1/8 pint measure, you need to know 3/4 = 6/8. It saves the dish!") + """
    """
    pages.append(wrap_page(p9, 9, "Strand 1: Number & Number Systems", "Standards: L1.5", "Maths Level 1 Core Revision Guide"))

    p10_scaffold = """
    <div class="step-row"><span>Step 1: Identify fraction</span><span>$\\frac{16}{24}$</span></div>
    <div class="step-row"><span>Step 2: Common factor is 8</span><span>Divide top and bottom by 8</span></div>
    <div class="step-row"><span>Step 3: Simplified fraction</span><span>$\\frac{16 \\div 8}{24 \\div 8} = \\mathbf{\\frac{2}{3}}$</span></div>
    """
    p10 = practice_page(
        "Fractions Equivalences", "Standards L1.5", 10, p10_scaffold,
        "Simplify fully: a) $\\frac{12}{18}$ &emsp; b) $\\frac{25}{100}$ &emsp; c) $\\frac{14}{35}$.",
        "Fill in the missing values: a) $\\frac{3}{5} = \\frac{?}{20}$ &emsp; b) $\\frac{4}{7} = \\frac{16}{?}$.",
        "Put these fractions in order of size, smallest first: $\\frac{1}{2}, \\frac{3}{8}, \\frac{3}{4}, \\frac{5}{16}$. Show your common denominator working clearly."
    )
    pages.append(p10)

    # TOPIC 5: PAGE 11 (Theory) & PAGE 12 (Practice)
    p11 = """
    <h2>Fractions of Amounts &amp; Finding Wholes</h2>
    <p>Calculating fractional shares of quantities, wages, materials, and time in workplace settings.</p>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1d4ed8;">The 2-Step Fraction Rule</h3>
      <p>To find $\\frac{a}{b}$ of an amount:<br>
      <strong>Step 1: Divide</strong> the amount by the denominator ($b$) to find $\\frac{1}{b}$.<br>
      <strong>Step 2: Multiply</strong> by the numerator ($a$).<br>
      $$\\text{Fraction of Amount} = (\\text{Amount} \\div b) \\times a$$</p>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Finding 3/8 of £480</span>
      <p>A charity raises $£480$. $\\frac{3}{8}$ is donated to a local foodbank. How much does the foodbank receive?</p>
      <div class="step-row"><span>Step 1: Find 1/8 by dividing by 8: 480 ÷ 8</span><strong>£60</strong></div>
      <div class="step-row"><span>Step 2: Multiply by numerator 3: £60 × 3</span><strong>£180</strong></div>
    </div>
    <div class="box-trap">
      <span class="tag-label tag-red">Tutor Trap</span> <strong>Dividing by Numerator First:</strong> Always divide by the bottom number (denominator) first! Dividing by the top gives the wrong size slice.
    </div>
    """ + tutor_vignette("🧑‍🏫", "Tutor Marcus", "Senior Maths Educator", "Remember: 'Divide by the bottom, times by the top!' Say it out loud three times before entering the exam room.") + """
    """
    pages.append(wrap_page(p11, 11, "Strand 1: Number & Number Systems", "Standards: L1.5", "Maths Level 1 Core Revision Guide"))

    p12_scaffold = """
    <div class="step-row"><span>Step 1: Divide by denominator 5</span><span>$£350 \\div 5 = £70$ (this is $\\frac{1}{5}$)</span></div>
    <div class="step-row"><span>Step 2: Multiply by numerator 3</span><span>$£70 \\times 3 = \\mathbf{£210}$</span></div>
    <div class="step-row"><span>Step 3: Subtract to find remainder if asked</span><span>$£350 - £210 = £140$</span></div>
    """
    p12 = practice_page(
        "Fractions of Amounts", "Standards L1.5", 12, p12_scaffold,
        "Calculate: a) $\\frac{1}{4}$ of $£68$ &emsp; b) $\\frac{2}{3}$ of $90\\text{ kg}$ &emsp; c) $\\frac{5}{8}$ of $320\\text{ litres}$.",
        "An office printer holds 500 sheets of paper. In one morning, staff use $\\frac{3}{10}$ of the paper. How many sheets were used, and how many remain?",
        "A garage mechanic earns $£1,800$ per month. He spends $\\frac{1}{3}$ on rent, $\\frac{1}{4}$ on food and utility bills, and saves the rest. How much money does he save each month?"
    )
    pages.append(p12)

    # TOPIC 6: PAGE 13 (Theory) & PAGE 14 (Practice)
    p13 = """
    <h2>Decimals, Money &amp; Place Value Arithmetic</h2>
    <p>Working with decimal places, lining up decimal points, and accurately calculating with money to 2 decimal places.</p>
    <div class="box-concept">
      <span class="tag-label tag-blue">Key Principle</span> <strong>The Decimal Point Stays Anchored:</strong>
      When adding or subtracting decimals, you must align the decimal points vertically in a straight column. Add trailing zeroes if numbers have different decimal lengths.
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Subtraction with Money</span>
      <p>A customer pays for items totaling <strong>£14.35</strong> with a <strong>£20 note</strong>. How much change is due?</p>
      <div class="step-row"><span>Align: 20.00 - 14.35</span><strong>Vertical alignment</strong></div>
      <div class="step-row"><span>Borrow across: 10 - 5</span><strong>5 pence</strong></div>
      <div class="step-row"><span>Tens: 9 - 3</span><strong>6</strong></div>
      <div class="step-row"><span>Pounds: 19 - 14</span><strong>5</strong></div>
      <div class="step-row"><span>Total change</span><strong>£5.65</strong></div>
    </div>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1e40af;">Multiplying and Dividing Decimals by 10, 100, 1000</h3>
      <p>&bull; <strong>$\\times 10$:</strong> Move decimal point 1 place RIGHT ($4.5 \\times 10 = 45$).<br>
      &bull; <strong>$\\times 100$:</strong> Move decimal point 2 places RIGHT ($3.25 \\times 100 = 325$).<br>
      &bull; <strong>$\\div 10$:</strong> Move decimal point 1 place LEFT ($45 \\div 10 = 4.5$).<br>
      &bull; <strong>$\\div 100$:</strong> Move decimal point 2 places LEFT ($68.4 \\div 100 = 0.684$).</p>
    </div>
    """
    pages.append(wrap_page(p13, 13, "Strand 1: Number & Number Systems", "Standards: L1.6", "Maths Level 1 Core Revision Guide"))

    p14_scaffold = """
    <div class="step-row"><span>Step 1: Align prices in column</span><span>$14.50 + 6.75 + 12.80$</span></div>
    <div class="step-row"><span>Step 2: Add decimals</span><span>$£34.05$</span></div>
    <div class="step-row"><span>Step 3: Subtract from £50 budget</span><span>$50.00 - 34.05 = \\mathbf{£15.95\\text{ change}}$</span></div>
    """
    p14 = practice_page(
        "Decimals & Money", "Standards L1.6", 14, p14_scaffold,
        "Calculate without a calculator: a) $14.8 + 6.35$ &emsp; b) $25 - 8.42$ &emsp; c) $3.6 \\times 100$ &emsp; d) $450 \\div 1000$.",
        "A hairdresser buys stock: shampoo $£8.45$, conditioner $£11.20$, and styling gel $£4.85$. What is the total cost?",
        "A builder purchases 6 identical bags of plaster. The total bill is $£53.70$. How much does one bag of plaster cost?"
    )
    pages.append(p14)

    # TOPIC 7: PAGE 15 (Theory) & PAGE 16 (Practice)
    p15 = """
    <h2>Percentages &amp; Key FDP Equivalences</h2>
    <p>Percentages mean 'out of 100'. Understanding benchmark percentages (10%, 25%, 50%) allows quick mental and written calculations.</p>
    <table class="cgp-table">
      <tr><th>Fraction</th><th>Decimal</th><th>Percentage</th><th>How to Calculate of an Amount</th></tr>
      <tr><td>$\\frac{1}{2}$</td><td>0.5</td><td>50%</td><td>Divide by 2</td></tr>
      <tr><td>$\\frac{1}{4}$</td><td>0.25</td><td>25%</td><td>Divide by 4 (or half and half again)</td></tr>
      <tr><td>$\\frac{3}{4}$</td><td>0.75</td><td>75%</td><td>Find 25% then multiply by 3</td></tr>
      <tr><td>$\\frac{1}{10}$</td><td>0.1</td><td>10%</td><td>Divide by 10</td></tr>
      <tr><td>$\\frac{1}{5}$</td><td>0.2</td><td>20%</td><td>Divide by 5 (or find 10% and double it)</td></tr>
      <tr><td>$\\frac{1}{100}$</td><td>0.01</td><td>1%</td><td>Divide by 100</td></tr>
    </table>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Finding 15% of £240</span>
      <p>A clothing store offers a <strong>15% sale discount</strong> on a coat priced at <strong>£240</strong>.</p>
      <div class="step-row"><span>Step 1: Find 10% (divide by 10): 240 ÷ 10</span><strong>£24.00</strong></div>
      <div class="step-row"><span>Step 2: Find 5% (half of 10%): £24 ÷ 2</span><strong>£12.00</strong></div>
      <div class="step-row"><span>Step 3: Add to get 15%: £24 + £12</span><strong>£36.00 discount</strong></div>
      <div class="step-row"><span>Step 4: Sale price: £240 - £36</span><strong>£204.00</strong></div>
    </div>
    """
    pages.append(wrap_page(p15, 15, "Strand 1: Number & Number Systems", "Standards: L1.7, L1.8", "Maths Level 1 Core Revision Guide"))

    p16_scaffold = """
    <div class="step-row"><span>Step 1: Find 10% of £360</span><span>$360 \\div 10 = £36$</span></div>
    <div class="step-row"><span>Step 2: Find 20% (double 10%)</span><span>$36 \\times 2 = £72$</span></div>
    <div class="step-row"><span>Step 3: Add for price increase</span><span>$£360 + £72 = \\mathbf{£432}$</span></div>
    """
    p16 = practice_page(
        "Percentages & Equivalences", "Standards L1.7, L1.8", 16, p16_scaffold,
        "Convert: a) $\\frac{3}{10}$ to a percentage &emsp; b) $45\\%$ to a decimal &emsp; c) $0.75$ to a fraction in simplest form.",
        "Calculate: a) $10\\%$ of $£450$ &emsp; b) $25\\%$ of $80\\text{ kg}$ &emsp; c) $5\\%$ of $£180$.",
        "A television normally costs $£480$. In a Black Friday sale, it is reduced by $30\\%$. Calculate the sale price of the television."
    )
    pages.append(p16)

    # TOPIC 8: PAGE 17 (Theory) & PAGE 18 (Practice)
    p17 = """
    <h2>Simple Ratios &amp; Recipe Scaling</h2>
    <p>Sharing quantities into given ratios, comparing mixtures, and scaling recipe quantities up or down.</p>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1d4ed8;">Sharing in a Given Ratio</h3>
      <p>1. <strong>Add</strong> the ratio parts: $\\text{Total Parts} = a + b$.<br>
      2. <strong>Divide</strong> the total amount by total parts to find the value of $1\\text{ part}$.<br>
      3. <strong>Multiply</strong> $1\\text{ part}$ by each ratio number.</p>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Sharing Tips in a Cafe</span>
      <p>Two waitstaff share <strong>£140</strong> in tips in the ratio <strong>4 : 3</strong>. How much does each receive?</p>
      <div class="step-row"><span>Step 1: Add parts: 4 + 3</span><strong>7 parts</strong></div>
      <div class="step-row"><span>Step 2: Value of 1 part: £140 ÷ 7</span><strong>£20</strong></div>
      <div class="step-row"><span>Step 3: Staff A (4 parts): 4 × £20</span><strong>£80</strong></div>
      <div class="step-row"><span>Step 4: Staff B (3 parts): 3 × £20</span><strong>£60</strong></div>
    </div>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1d4ed8;">Direct Recipe Scaling</h3>
      <p>To scale a recipe from serving 4 people to serving 10 people: find the multiplier $\\frac{10}{4} = 2.5$, then multiply each ingredient by $2.5$.</p>
    </div>
    """
    pages.append(wrap_page(p17, 17, "Strand 1: Number & Number Systems", "Standards: L1.9", "Maths Level 1 Core Revision Guide"))

    p18_scaffold = """
    <div class="step-row"><span>Step 1: Add ratio parts (1 + 4)</span><span>$5\\text{ parts}$</span></div>
    <div class="step-row"><span>Step 2: Value of 1 part ($2500\\text{ ml} \\div 5$)</span><span>$500\\text{ ml}$</span></div>
    <div class="step-row"><span>Step 3: Squash = 1 part; Water = 4 parts</span><span>$1 \\times 500 = 500\\text{ ml}$; $4 \\times 500 = \\mathbf{2,000\\text{ ml}}$</span></div>
    """
    p18 = practice_page(
        "Simple Ratio & Proportion", "Standards L1.9", 18, p18_scaffold,
        "Share $£72$ in the ratio $5 : 3$.",
        "A mortar mix uses cement and sand in the ratio $1 : 4$. A bricklayer uses $15\\text{ kg}$ of cement. How much sand does he need?",
        "A pancake recipe serves 4 people and requires: $200\\text{ g}$ flour, $2$ eggs, and $300\\text{ ml}$ milk. How much of each ingredient is needed to serve 10 people?"
    )
    pages.append(p18)

    # TOPIC 9: PAGE 19 (Theory) & PAGE 20 (Practice)
    p19 = """
    <h2>Estimation, Rounding &amp; Checking Answers</h2>
    <p>Rounding numbers to the nearest 10, 100, or 1000, and using estimation and inverse operations to check calculations.</p>
    <div class="box-concept">
      <span class="tag-label tag-blue">Rounding Rule</span> <strong>The 5 or More Rule:</strong>
      Look at the digit immediately to the right of your target rounding column. If it is <strong>5 or more, round UP</strong>. If it is <strong>less than 5, round DOWN</strong> (keep the digit same).
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Estimating a Shopping Basket</span>
      <p>Estimate the total cost of three items priced at: <strong>£19.45</strong>, <strong>£9.80</strong>, and <strong>£4.15</strong>.</p>
      <div class="step-row"><span>Round £19.45 to nearest £10</span><strong>£20</strong></div>
      <div class="step-row"><span>Round £9.80 to nearest £10</span><strong>£10</strong></div>
      <div class="step-row"><span>Round £4.15 to nearest £1</span><strong>£4</strong></div>
      <div class="step-row"><span>Estimated total: 20 + 10 + 4</span><strong>£34.00 (Exact is £33.40)</strong></div>
    </div>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1e40af;">Examiner Requirement: Showing a Check</h3>
      <p>Functional Skills exams always include 1-mark questions asking: <em>'Show a check of your answer.'</em><br>
      You must show an <strong>inverse operation</strong> (e.g. check $24 \\times 5 = 120$ by writing $120 \\div 5 = 24$) or a rounded estimate ($20 \\times 5 = 100$).</p>
    </div>
    """
    pages.append(wrap_page(p19, 19, "Strand 1: Number & Number Systems", "Standards: L1.10", "Maths Level 1 Core Revision Guide"))

    p20_scaffold = """
    <div class="step-row"><span>Step 1: Round 48 to nearest 10</span><span>$50$</span></div>
    <div class="step-row"><span>Step 2: Round 19 to nearest 10</span><span>$20$</span></div>
    <div class="step-row"><span>Step 3: Multiply rounded values</span><span>$50 \\times 20 = \\mathbf{1,000}$</span></div>
    """
    p20 = practice_page(
        "Estimation & Rounding", "Standards L1.10", 20, p20_scaffold,
        "Round $4,762$: a) to the nearest 10 &emsp; b) to the nearest 100 &emsp; c) to the nearest 1000.",
        "A cinema sells 385 tickets at $£9.50$ each. Use estimation to find an approximate total revenue.",
        "A delivery van has 12 boxes weighing $18.4\\text{ kg}$ each. Calculate the exact total weight, and show an inverse check of your answer."
    )
    pages.append(p20)

    # TOPIC 10: PAGE 21 (Theory) & PAGE 22 (Practice)
    p21 = """
    <h2>Order of Operations (BIDMAS) &amp; Simple Formulas</h2>
    <p>Mathematical calculations must be carried out in a specific statutory sequence: Brackets, Indices, Division/Multiplication, Addition/Subtraction.</p>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1d4ed8;">The BIDMAS Sequence</h3>
      <p>&bull; <strong>B</strong>rackets: First priority $(...)$<br>
      &bull; <strong>I</strong>ndices: Powers and roots ($3^2, \\sqrt{16}$)<br>
      &bull; <strong>D</strong>ivision &amp; <strong>M</strong>ultiplication: Work left to right<br>
      &bull; <strong>A</strong>ddition &amp; <strong>S</strong>ubtraction: Work left to right</p>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Using BIDMAS</span>
      <p>Evaluate: <strong>$15 - 3 \\times 4 + 2$</strong>.</p>
      <div class="step-row"><span>Step 1: Multiplication first: 3 × 4</span><strong>12</strong></div>
      <div class="step-row"><span>Step 2: Expression becomes: 15 - 12 + 2</span><strong>Left to right</strong></div>
      <div class="step-row"><span>Step 3: 15 - 12 = 3; then 3 + 2</span><strong>5</strong></div>
    </div>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1d4ed8;">Substituting into Formulas in Words</h3>
      <p>$$\\text{Total Cost} = \\text{Hire Charge} + (\\text{Days} \\times \\text{Daily Rate})$$</p>
      <p>If hire charge is $£30$, days is 4, and daily rate is $£15$: $\\text{Cost} = 30 + (4 \\times 15) = 30 + 60 = \\mathbf{£90}$.</p>
    </div>
    """
    pages.append(wrap_page(p21, 21, "Strand 1: Number & Number Systems", "Standards: L1.11, L1.12", "Maths Level 1 Core Revision Guide"))

    p22_scaffold = """
    <div class="step-row"><span>Step 1: Calculate multiplication part</span><span>$4 \\text{ hours} \\times £25 = £100$</span></div>
    <div class="step-row"><span>Step 2: Add fixed call-out fee</span><span>$£45 + £100$</span></div>
    <div class="step-row"><span>Step 3: Total charge</span><span>$\\mathbf{£145}$</span></div>
    """
    p22 = practice_page(
        "BIDMAS & Formulas", "Standards L1.11, L1.12", 22, p22_scaffold,
        "Evaluate: a) $10 + 4 \\times 2$ &emsp; b) $(12 - 4) \\div 2$ &emsp; c) $20 - 3^2 + 1$.",
        "A car hire company uses the formula: $\\text{Cost} = £40 + (£25 \\times \\text{number of days})$. Calculate the cost for a 5-day hire.",
        "A plumber charges using the rule: $\\text{Bill} = £50\\text{ call-out} + (£35 \\times \\text{hours worked})$. He works for 3.5 hours on a boiler. What is the total bill?"
    )
    pages.append(p22)

    # CHECKPOINT 1: PAGES 23 TO 26 (4-page Review Assessment)
    chk1_p1 = [
        (1, 2, "Calculate without using a calculator: $348 \\times 16$. Show your full written method.", 75),
        (2, 2, "A bank account is overdrawn at $-£185$. The customer pays in $£450$. What is the new balance?", 65),
        (3, 2, "Simplify fully: a) $\\frac{18}{24}$ &emsp; b) Write $\\frac{3}{5}$ as a percentage.", 70)
    ]
    pages.append(checkpoint_page("Strand 1: Number & Number Systems", "Part 1 &bull; Non-Calculator (Q1-Q3)", 23, "6 Marks", chk1_p1))

    chk1_p2 = [
        (4, 2, "Work out: $1,476 \\div 6$ without a calculator. Show your bus stop division.", 75),
        (5, 2, "Evaluate: $20 - 4 \\times 3 + 2$.", 65),
        (6, 2, "Share $£120$ in the ratio $3 : 1$. What is the larger share?", 70)
    ]
    pages.append(checkpoint_page("Strand 1: Number & Number Systems", "Part 1 &bull; Non-Calculator (Q4-Q6)", 24, "6 Marks", chk1_p2))

    chk1_p3 = [
        (7, 3, "A jacket costs $£80$. It is reduced by $15\\%$ in a sale. Calculate the sale price.", 80),
        (8, 3, "A recipe for 4 people requires $300\\text{ g}$ of rice. How much rice is needed for 9 people?", 80),
        (9, 3, "A delivery company has 350 parcels to deliver. In the morning they deliver $\\frac{3}{5}$ of the parcels. How many parcels remain to be delivered in the afternoon?", 80)
    ]
    pages.append(checkpoint_page("Strand 1: Number & Number Systems", "Part 2 &bull; Calculator Allowed (Q7-Q9)", 25, "9 Marks", chk1_p3))

    chk1_p4 = [
        (10, 3, "An electrician charges: $£45\\text{ call-out} + (£32 \\times \\text{hours})$. He works for 4.5 hours. How much is the bill?", 80),
        (11, 3, "A supermarket sells a 6-pack of cola for $£4.20$ and a 10-pack of the same cola for $£6.80$. Which pack is better value per can? Show your calculations.", 80),
        (12, 3, "A landscape gardener orders 24 bags of decorative gravel at $£6.75$ each. Delivery is $£25.00$. He has a budget of $£180.00$. Does he have enough money?", 80)
    ]
    pages.append(checkpoint_page("Strand 1: Number & Number Systems", "Part 2 &bull; Calculator Allowed (Q10-Q12)", 26, "9 Marks", chk1_p4))

    # =========================================================================
    # STRAND 2: MEASURES, SHAPE & SPACE (PAGES 27 - 50)
    # =========================================================================

    # TOPIC 11: PAGE 27 (Theory) & PAGE 28 (Practice)
    p27 = """
    <h2>Metric Units: Length, Mass &amp; Capacity</h2>
    <p>Converting between metric prefixes (kilo, centi, milli) by multiplying or dividing by 10, 100, or 1000.</p>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1d4ed8;">Statutory Metric Conversion Rules</h3>
      <p>&bull; <strong>Length:</strong> $1\\text{ km} = 1000\\text{ m}$; $1\\text{ m} = 100\\text{ cm}$; $1\\text{ cm} = 10\\text{ mm}$.<br>
      &bull; <strong>Mass:</strong> $1\\text{ kg} = 1000\\text{ g}$; $1\\text{ tonne} = 1000\\text{ kg}$.<br>
      &bull; <strong>Capacity:</strong> $1\\text{ litre} = 1000\\text{ ml} = 100\\text{ cl}$.</p>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Converting m to cm</span>
      <p>A joiner cuts a length of skirting board measuring <strong>2.45 metres</strong>. What is this length in centimetres?</p>
      <div class="step-row"><span>Rule: 1 metre = 100 centimetres</span><strong>Multiply by 100</strong></div>
      <div class="step-row"><span>Calculation: 2.45 × 100</span><strong>245 cm</strong></div>
    </div>
    <div class="box-trap">
      <span class="tag-label tag-red">Tutor Trap</span> <strong>Multiplying vs Dividing:</strong> When going from a <em>small unit to a large unit</em> (e.g. ml to litres), you must <strong>divide</strong> ($750\\text{ ml} \\div 1000 = 0.75\\text{ L}$). When going from <em>large to small</em>, <strong>multiply</strong>.
    </div>
    """
    pages.append(wrap_page(p27, 27, "Strand 2: Measures, Shape & Space", "Standards: L1.17", "Maths Level 1 Core Revision Guide"))

    p28_scaffold = """
    <div class="step-row"><span>Step 1: Identify conversion rule</span><span>$1\\text{ kg} = 1,000\\text{ g}$</span></div>
    <div class="step-row"><span>Step 2: Multiply by 1,000</span><span>$3.6 \\times 1,000 = \\mathbf{3,600\\text{ g}}$</span></div>
    """
    p28 = practice_page(
        "Metric Units", "Standards L1.17", 28, p28_scaffold,
        "Convert: a) $3.5\\text{ m}$ to cm &emsp; b) $450\\text{ ml}$ to litres &emsp; c) $2.8\\text{ kg}$ to grams &emsp; d) $65\\text{ mm}$ to cm.",
        "A chef needs $2.4\\text{ kg}$ of potatoes for a recipe. He has an open bag with $1,850\\text{ g}$. How many more grams does he need?",
        "A sports team drinks 12 bottles of water during a match. Each bottle contains $750\\text{ ml}$. How many total litres of water did the team drink?"
    )
    pages.append(p28)

    # TOPIC 12: PAGE 29 (Theory) & PAGE 30 (Practice)
    p29 = """
    <h2>Imperial Units: Feet, Inches, Miles &amp; Pints</h2>
    <p>Using common imperial units and standard UK statutory conversion approximations.</p>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1d4ed8;">Key Statutory Approximations</h3>
      <p>&bull; <strong>Length:</strong> $1\\text{ inch} \\approx 2.5\\text{ cm}$; $1\\text{ foot} = 12\\text{ inches} \\approx 30\\text{ cm}$.<br>
      &bull; <strong>Distance:</strong> $5\\text{ miles} \\approx 8\\text{ km}$ ($1\\text{ mile} \\approx 1.6\\text{ km}$).<br>
      &bull; <strong>Mass:</strong> $1\\text{ kg} \\approx 2.2\\text{ lbs}$.<br>
      &bull; <strong>Capacity:</strong> $1\\text{ pint} \\approx 568\\text{ ml}$ ($1\\text{ gallon} \\approx 4.5\\text{ litres}$).</p>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Converting Miles to Kilometres</span>
      <p>A UK driver sees a road sign: <strong>40 miles to Dover</strong>. How many kilometres is this?</p>
      <div class="step-row"><span>Step 1: Divide by 5 miles: 40 ÷ 5</span><strong>8 blocks of 5 miles</strong></div>
      <div class="step-row"><span>Step 2: Multiply by 8 km: 8 × 8 km</span><strong>64 kilometres</strong></div>
    </div>
    """ + tutor_vignette("🧑‍🏫", "Tutor Marcus", "Senior Maths Educator", "Remember the fraction for miles and km: 5 miles is 8 km. 5 to 8! If you drive 50 miles, that's 80 km.") + """
    """
    pages.append(wrap_page(p29, 29, "Strand 2: Measures, Shape & Space", "Standards: L1.17", "Maths Level 1 Core Revision Guide"))

    p30_scaffold = """
    <div class="step-row"><span>Step 1: Divide 25 miles by 5</span><span>$25 \\div 5 = 5$</span></div>
    <div class="step-row"><span>Step 2: Multiply by 8 km</span><span>$5 \\times 8 = \\mathbf{40\\text{ km}}$</span></div>
    """
    p30 = practice_page(
        "Imperial Conversions", "Standards L1.17", 30, p30_scaffold,
        "Using $1\\text{ inch} = 2.5\\text{ cm}$, convert: a) $6\\text{ inches}$ to cm &emsp; b) $20\\text{ cm}$ to inches.",
        "A package weighs $11\\text{ lbs}$. Using $1\\text{ kg} = 2.2\\text{ lbs}$, find its weight in kilograms.",
        "A road cyclist travels 35 miles on Saturday and 48 kilometres on Sunday. Which day did she ride further? (Use $5\\text{ miles} = 8\\text{ km}$)"
    )
    pages.append(p30)

    # TOPIC 13: PAGE 31 (Theory) & PAGE 32 (Practice)
    p31 = """
    <h2>Time: 12-Hour, 24-Hour &amp; Work Schedules</h2>
    <p>Converting between am/pm and 24-hour clock formats, calculating journey times, and reading timetables.</p>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1d4ed8;">24-Hour Clock Conversion</h3>
      <p>&bull; <strong>AM times:</strong> Add leading zero if needed ($8:30\\text{ am} \\rightarrow 08:30$).<br>
      &bull; <strong>PM times:</strong> Add 12 to the hours ($3:15\\text{ pm} \\rightarrow 15:15$; $10:45\\text{ pm} \\rightarrow 22:45$).<br>
      &bull; <strong>Midnight:</strong> $00:00$ &bull; <strong>Noon:</strong> $12:00$.</p>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Bus Journey Duration</span>
      <p>A bus leaves town at <strong>14:35</strong> and arrives at the retail park at <strong>15:20</strong>. How long did the trip take?</p>
      <div class="step-row"><span>Jump to 15:00: 14:35 to 15:00</span><strong>25 minutes</strong></div>
      <div class="step-row"><span>Jump to 15:20: 15:00 to 15:20</span><strong>20 minutes</strong></div>
      <div class="step-row"><span>Total duration: 25 + 20</span><strong>45 minutes</strong></div>
    </div>
    <div class="box-trap">
      <span class="tag-label tag-red">Tutor Trap</span> <strong>Subtracting Time Directly:</strong> Never do $15.20 - 14.35 = 0.85$ on a calculator! Time has 60 minutes in an hour, not 100. Always jump to the nearest hour.
    </div>
    """
    pages.append(wrap_page(p31, 31, "Strand 2: Measures, Shape & Space", "Standards: L1.18", "Maths Level 1 Core Revision Guide"))

    p32_scaffold = """
    <div class="step-row"><span>Step 1: Jump to 10:00</span><span>$09:25 \\rightarrow 10:00 = 35\\text{ minutes}$</span></div>
    <div class="step-row"><span>Step 2: Jump from 10:00 to 11:10</span><span>$1\\text{ hour } 10\\text{ minutes}$</span></div>
    <div class="step-row"><span>Step 3: Total journey time</span><span>$35\\text{ m} + 1\\text{ h } 10\\text{ m} = \\mathbf{1\\text{ h } 45\\text{ mins}}$</span></div>
    """
    p32 = practice_page(
        "Time & Timetables", "Standards L1.18", 32, p32_scaffold,
        "Convert to 24-hour clock: a) $7:15\\text{ am}$ &emsp; b) $4:30\\text{ pm}$ &emsp; c) $11:05\\text{ pm}$.",
        "A train departs London at 11:45 and arrives in Birmingham at 13:12. How long did the journey take in hours and minutes?",
        "A healthcare assistant starts her shift at 08:30 and finishes at 16:45. She has a 45-minute lunch break. How many hours and minutes of paid work did she complete?"
    )
    pages.append(p32)

    # TOPIC 14: PAGE 33 (Theory) & PAGE 34 (Practice)
    p33 = """
    <h2>Money: Wages, Discounts &amp; Best Value</h2>
    <p>Calculating hourly pay, basic overtime, finding discounts, and comparing unit prices in supermarket shopping.</p>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1d4ed8;">Wage Calculation Rule</h3>
      <p>$$\\text{Gross Pay} = \\text{Hours Worked} \\times \\text{Hourly Rate}$$</p>
      <p><strong>Overtime at time-and-a-half:</strong> Overtime rate $= \\text{Basic Rate} \\times 1.5$.</p>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Weekly Wage with Overtime</span>
      <p>A retail worker earns <strong>£11.00 per hour</strong> for 30 basic hours, and works <strong>4 hours overtime at time-and-a-half</strong>.</p>
      <div class="step-row"><span>Basic pay: 30 × £11.00</span><strong>£330.00</strong></div>
      <div class="step-row"><span>Overtime rate: £11.00 × 1.5</span><strong>£16.50/hr</strong></div>
      <div class="step-row"><span>Overtime pay: 4 × £16.50</span><strong>£66.00</strong></div>
      <div class="step-row"><span>Total gross wage: £330 + £66</span><strong>£396.00</strong></div>
    </div>
    """ + tutor_vignette("👩‍💼", "Priya", "Retail Supervisor", "When comparing deals like 'Buy 2 Get 1 Free' versus '25% Off', always calculate the cost per item. Don't be fooled by big sale signs!") + """
    """
    pages.append(wrap_page(p33, 33, "Strand 2: Measures, Shape & Space", "Standards: L1.18", "Maths Level 1 Core Revision Guide"))

    p34_scaffold = """
    <div class="step-row"><span>Step 1: Brand A unit cost ($£2.40 \\div 4$)</span><span>$£0.60\\text{ per tin}$</span></div>
    <div class="step-row"><span>Step 2: Brand B unit cost ($£3.30 \\div 6$)</span><span>$£0.55\\text{ per tin}$</span></div>
    <div class="step-row"><span>Step 3: Compare unit costs</span><span>Brand B is cheaper by $£0.05$ per tin</span></div>
    """
    p34 = practice_page(
        "Money & Best Buys", "Standards L1.18", 34, p34_scaffold,
        "A warehouse assistant works 35 hours at $£11.50$ per hour. What is his gross pay?",
        "A microwave originally priced at $£120.00$ is reduced by $15\\%$. Calculate the sale price.",
        "Pack A contains 4 rolls of kitchen towel for $£3.60$. Pack B contains 6 rolls of the same towel for $£4.80$. Which pack is better value per roll?"
    )
    pages.append(p34)

    # TOPIC 15: PAGE 35 (Theory) & PAGE 36 (Practice)
    p35 = """
    <h2>Perimeter of Rectilinear &amp; Compound Shapes</h2>
    <p>Perimeter is the total distance around the outside edge of a 2D shape. Used for skirting boards, fencing, and borders.</p>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1d4ed8;">Perimeter Rule</h3>
      <p>$$\\text{Perimeter} = \\text{Sum of ALL outer sides}$$</p>
      <p>&bull; <strong>Rectangle:</strong> $P = 2 \\times (l + w)$ or $2l + 2w$.<br>
      &bull; <strong>Square:</strong> $P = 4 \\times s$.</p>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: L-Shaped Room Perimeter</span>
      <p>An L-shaped room has outer measurements: length $8\\text{ m}$, width $6\\text{ m}$, cut-in $3\\text{ m}$ by $2\\text{ m}$.</p>
      <div class="step-row"><span>Top length</span><strong>8 m</strong></div>
      <div class="step-row"><span>Right side</span><strong>4 m (6 - 2)</strong></div>
      <div class="step-row"><span>Inward step</span><strong>3 m</strong></div>
      <div class="step-row"><span>Down step</span><strong>2 m</strong></div>
      <div class="step-row"><span>Bottom edge</span><strong>5 m (8 - 3)</strong></div>
      <div class="step-row"><span>Left side</span><strong>6 m</strong></div>
      <div class="step-row"><span>Total perimeter: 8 + 4 + 3 + 2 + 5 + 6</span><strong>28 metres</strong></div>
    </div>
    """
    pages.append(wrap_page(p35, 35, "Strand 2: Measures, Shape & Space", "Standards: L1.19", "Maths Level 1 Core Revision Guide"))

    p36_scaffold = """
    <div class="step-row"><span>Step 1: Formula for rectangle perimeter</span><span>$2 \\times (\\text{length} + \\text{width})$</span></div>
    <div class="step-row"><span>Step 2: Add length and width</span><span>$6.5\\text{ m} + 4.2\\text{ m} = 10.7\\text{ m}$</span></div>
    <div class="step-row"><span>Step 3: Double total</span><span>$10.7 \\times 2 = \\mathbf{21.4\\text{ metres}}$</span></div>
    """
    p36 = practice_page(
        "Perimeter Calculations", "Standards L1.19", 36, p36_scaffold,
        "Calculate the perimeter of a rectangle measuring $9.5\\text{ m}$ by $4.5\\text{ m}$.",
        "A square garden plot has sides of $7.5\\text{ m}$. Wooden fencing costs $£12.00$ per metre. How much does it cost to fence all 4 sides?",
        "An L-shaped lawn has edges: $12\\text{ m}, 8\\text{ m}, 5\\text{ m}, 3\\text{ m}, 7\\text{ m}, 5\\text{ m}$. Calculate the total perimeter to be bordered with edging tape."
    )
    pages.append(p36)

    # TOPIC 16: PAGE 37 (Theory) & PAGE 38 (Practice)
    p37 = """
    <h2>Area of Rectangles &amp; L-Shaped Floors</h2>
    <p>Area measures the 2D surface covered within a boundary. Vital for ordering carpets, tiles, paint, and turf.</p>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1d4ed8;">Area Formulas</h3>
      <p>&bull; <strong>Rectangle:</strong> $\\text{Area} = \\text{length} \\times \\text{width}$ ($A = l \\times w$).<br>
      &bull; Units: square metres ($\\text{m}^2$) or square centimetres ($\\text{cm}^2$).<br>
      &bull; <strong>L-shapes:</strong> Split into 2 simple rectangles, find each area, and add them together.</p>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Splitting an L-Shape</span>
      <p>An L-shaped kitchen floor has section A ($5\\text{ m} \\times 4\\text{ m}$) and section B ($3\\text{ m} \\times 2\\text{ m}$).</p>
      <div class="step-row"><span>Area of Section A: 5 × 4</span><strong>20 m²</strong></div>
      <div class="step-row"><span>Area of Section B: 3 × 2</span><strong>6 m²</strong></div>
      <div class="step-row"><span>Total Floor Area: 20 + 6</span><strong>26 m²</strong></div>
    </div>
    <div class="box-trap">
      <span class="tag-label tag-red">Tutor Trap</span> <strong>Perimeter vs Area:</strong> Perimeter is the fence (1D, measured in metres). Area is the grass inside (2D, measured in square metres). Never confuse them!
    </div>
    """
    pages.append(wrap_page(p37, 37, "Strand 2: Measures, Shape & Space", "Standards: L1.20", "Maths Level 1 Core Revision Guide"))

    p38_scaffold = """
    <div class="step-row"><span>Step 1: Calculate room area</span><span>$5\\text{ m} \\times 4\\text{ m} = 20\\text{ m}^2$</span></div>
    <div class="step-row"><span>Step 2: Multiply by price per m²</span><span>$20 \\times £18.50$</span></div>
    <div class="step-row"><span>Step 3: Total carpet cost</span><span>$\\mathbf{£370.00}$</span></div>
    """
    p38 = practice_page(
        "Area of Rectangles", "Standards L1.20", 38, p38_scaffold,
        "Calculate the area of a patio measuring $6.5\\text{ m}$ by $4.0\\text{ m}$.",
        "A bedroom floor is $4.5\\text{ m}$ by $3.2\\text{ m}$. Carpet costs $£15.00$ per square metre. How much does the carpet cost?",
        "An L-shaped meeting room is divided into two parts: $8\\text{ m} \\times 5\\text{ m}$ and $4\\text{ m} \\times 3\\text{ m}$. A tin of floor polish covers $25\\text{ m}^2$. How many tins must be bought to polish the entire floor?"
    )
    pages.append(p38)

    # TOPIC 17: PAGE 39 (Theory) & PAGE 40 (Practice)
    p39 = """
    <h2>Volume of Cuboids &amp; Liquid Capacity</h2>
    <p>Volume measures 3D space occupied by a solid. Essential for parcel packaging, shipping freight, and water tanks.</p>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1d4ed8;">Volume of a Cuboid</h3>
      <p>$$\\text{Volume} = \\text{length} \\times \\text{width} \\times \\text{height}$$</p>
      <p>&bull; Units: cubic centimetres ($\\text{cm}^3$) or cubic metres ($\\text{m}^3$).<br>
      &bull; <strong>Capacity Link:</strong> $1000\\text{ cm}^3 = 1\\text{ litre}$; $1\\text{ m}^3 = 1000\\text{ litres}$.</p>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Fish Tank Capacity</span>
      <p>A rectangular glass fish tank is <strong>60 cm long, 40 cm wide, and 30 cm deep</strong>. How many litres of water does it hold?</p>
      <div class="step-row"><span>Step 1: Calculate volume: 60 × 40 × 30</span><strong>72,000 cm³</strong></div>
      <div class="step-row"><span>Step 2: Convert to litres: divide by 1000</span><strong>72,000 ÷ 1000 = 72 litres</strong></div>
    </div>
    """ + tutor_vignette("🧑‍🔧", "Dave", "Maintenance Tech", "When installing cold water storage tanks, 1 cubic metre equals 1,000 litres. If you measure in metres, just multiply by 1,000 to get litres!") + """
    """
    pages.append(wrap_page(p39, 39, "Strand 2: Measures, Shape & Space", "Standards: L1.21", "Maths Level 1 Core Revision Guide"))

    p40_scaffold = """
    <div class="step-row"><span>Step 1: Formula for cuboid volume</span><span>$V = l \\times w \\times h$</span></div>
    <div class="step-row"><span>Step 2: Multiply dimensions</span><span>$2\\text{ m} \\times 1.5\\text{ m} \\times 1.0\\text{ m} = 3\\text{ m}^3$</span></div>
    <div class="step-row"><span>Step 3: Convert m³ to litres (×1000)</span><span>$3 \\times 1000 = \\mathbf{3,000\\text{ litres}}$</span></div>
    """
    p40 = practice_page(
        "Volume & Capacity", "Standards L1.21", 40, p40_scaffold,
        "Calculate the volume of a shoebox measuring $30\\text{ cm}$ long, $18\\text{ cm}$ wide, and $12\\text{ cm}$ high.",
        "A rectangular storage container measures $1.5\\text{ m}$ by $0.8\\text{ m}$ by $0.5\\text{ m}$. What is its volume in cubic metres?",
        "A water tank is $80\\text{ cm}$ long, $50\\text{ cm}$ wide, and $45\\text{ cm}$ high. How many litres of water does it hold when filled to the brim?"
    )
    pages.append(p40)

    # TOPIC 18: PAGE 41 (Theory) & PAGE 42 (Practice)
    p41 = """
    <h2>2D Geometry, Angles &amp; Polygons</h2>
    <p>Recognising 2D shapes, properties of triangles and quadrilaterals, and classifying angles.</p>
    <div class="grid-2col">
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8;">Angle Types</h3>
        <p>&bull; <strong>Acute:</strong> Less than $90^\\circ$.<br>
        &bull; <strong>Right Angle:</strong> Exactly $90^\\circ$ (square corner).<br>
        &bull; <strong>Obtuse:</strong> Between $90^\\circ$ and $180^\\circ$.<br>
        &bull; <strong>Straight Line:</strong> Exactly $180^\\circ$.<br>
        &bull; <strong>Full Turn:</strong> Exactly $360^\\circ$.</p>
      </div>
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8;">Types of Triangles</h3>
        <p>&bull; <strong>Equilateral:</strong> All 3 sides equal, all angles $60^\\circ$.<br>
        &bull; <strong>Isosceles:</strong> 2 sides equal, 2 angles equal.<br>
        &bull; <strong>Scalene:</strong> All 3 sides and angles different.<br>
        &bull; <strong>Right-Angled:</strong> Contains one $90^\\circ$ angle.</p>
      </div>
    </div>
    <div class="box-concept">
      <span class="tag-label tag-blue">Key Angle Fact</span> Angles in any triangle always add up to <strong>180°</strong>. Angles in any quadrilateral always add up to <strong>360°</strong>.
    </div>
    """
    pages.append(wrap_page(p41, 41, "Strand 2: Measures, Shape & Space", "Standards: L1.22, L1.23", "Maths Level 1 Core Revision Guide"))

    p42_scaffold = """
    <div class="step-row"><span>Step 1: Triangle angles add to 180°</span><span>$180^\\circ$</span></div>
    <div class="step-row"><span>Step 2: Add known angles (45° + 75°)</span><span>$120^\\circ$</span></div>
    <div class="step-row"><span>Step 3: Subtract from 180°</span><span>$180 - 120 = \\mathbf{60^\\circ}$</span></div>
    """
    p42 = practice_page(
        "2D Shapes & Angles", "Standards L1.22, L1.23", 42, p42_scaffold,
        "Name each angle type: a) $45^\\circ$ &emsp; b) $90^\\circ$ &emsp; c) $135^\\circ$ &emsp; d) $180^\\circ$.",
        "Two angles in a triangle are $55^\\circ$ and $65^\\circ$. Calculate the third angle.",
        "State the number of sides and lines of symmetry for: a) A regular hexagon &emsp; b) A rectangle &emsp; c) An equilateral triangle."
    )
    pages.append(p42)

    # TOPIC 19: PAGE 43 (Theory) & PAGE 44 (Practice)
    p43 = """
    <h2>3D Shapes, Nets, Faces, Edges &amp; Vertices</h2>
    <p>Identifying common 3D solids and understanding how 2D nets fold together to build 3D packages.</p>
    <table class="cgp-table">
      <tr><th>3D Shape</th><th>Faces</th><th>Edges</th><th>Vertices (Corners)</th><th>2D Faces Present</th></tr>
      <tr><td><strong>Cube</strong></td><td>6</td><td>12</td><td>8</td><td>6 identical squares</td></tr>
      <tr><td><strong>Cuboid</strong></td><td>6</td><td>12</td><td>8</td><td>3 pairs of matching rectangles</td></tr>
      <tr><td><strong>Triangular Prism</strong></td><td>5</td><td>9</td><td>6</td><td>2 triangles, 3 rectangles</td></tr>
      <tr><td><strong>Square Pyramid</strong></td><td>5</td><td>8</td><td>5</td><td>1 square base, 4 triangles</td></tr>
      <tr><td><strong>Cylinder</strong></td><td>3 (2 flat, 1 curved)</td><td>2</td><td>0</td><td>2 circles, 1 rolled rectangle</td></tr>
    </table>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Identifying a Net</span>
      <p>A flat cardboard packaging net has 2 triangular ends and 3 connected rectangles. What 3D solid does it fold into?</p>
      <div class="step-row"><span>End faces: 2 triangles</span><strong>Triangular prism ends</strong></div>
      <div class="step-row"><span>Side faces: 3 rectangles</span><strong>Prism side walls</strong></div>
      <div class="step-row"><span>Solid name</span><strong>Triangular Prism</strong></div>
    </div>
    """
    pages.append(wrap_page(p43, 43, "Strand 2: Measures, Shape & Space", "Standards: L1.24, L1.25", "Maths Level 1 Core Revision Guide"))

    p44_scaffold = """
    <div class="step-row"><span>Step 1: Identify solid</span><span>Cuboid has 6 rectangular faces</span></div>
    <div class="step-row"><span>Step 2: Count edges</span><span>$12\\text{ straight edges}$</span></div>
    <div class="step-row"><span>Step 3: Count vertices</span><span>$\\mathbf{8\\text{ corners (vertices)}}$</span></div>
    """
    p44 = practice_page(
        "3D Shapes & Nets", "Standards L1.24, L1.25", 44, p44_scaffold,
        "How many faces, edges, and vertices does a cube have?",
        "Describe the shapes that make up the net of a closed cylinder.",
        "A manufacturer designs a cardboard box in the shape of a triangular prism. How many rectangular faces does the net require?"
    )
    pages.append(p44)

    # TOPIC 20: PAGE 45 (Theory) & PAGE 46 (Practice)
    p45 = """
    <h2>Scale Plans &amp; 8-Point Compass Bearings</h2>
    <p>Reading scaled site maps, using grid scales, and navigating with North, South, East, West and intermediate directions.</p>
    <div class="grid-2col">
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8;">8-Point Compass Rose</h3>
        <p>&bull; <strong>Cardinal:</strong> North (N), South (S), East (E), West (W).<br>
        &bull; <strong>Intercardinal:</strong> North-East (NE), South-East (SE), South-West (SW), North-West (NW).<br>
        <em>Mnemonic:</em> <strong>N</strong>ever <strong>E</strong>at <strong>S</strong>hredded <strong>W</strong>heat (clockwise from top).</p>
      </div>
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8;">Simple Scales</h3>
        <p>A scale of $1\\text{ cm} = 2\\text{ m}$ means every centimetre on paper is 2 metres in real life.<br>
        &bull; $4\\text{ cm on plan} = 4 \\times 2 = \\mathbf{8\\text{ m real}}$.<br>
        &bull; $10\\text{ m real} = 10 \\div 2 = \\mathbf{5\\text{ cm on plan}}$.</p>
      </div>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Room Layout on a Grid</span>
      <p>On a grid where $1\\text{ square} = 0.5\\text{ m}$, a sofa is 4 squares long. What is its real length?</p>
      <div class="step-row"><span>Calculation: 4 × 0.5 m</span><strong>2.0 metres</strong></div>
    </div>
    """
    pages.append(wrap_page(p45, 45, "Strand 2: Measures, Shape & Space", "Standards: L1.26, L1.27", "Maths Level 1 Core Revision Guide"))

    p46_scaffold = """
    <div class="step-row"><span>Step 1: Identify scale factor</span><span>$1\\text{ cm} = 5\\text{ metres}$</span></div>
    <div class="step-row"><span>Step 2: Multiply map distance</span><span>$6.5 \\times 5 = \\mathbf{32.5\\text{ metres}}$</span></div>
    """
    p46 = practice_page(
        "Scale Plans & Compass", "Standards L1.26, L1.27", 46, p46_scaffold,
        "A map has a scale of $1\\text{ cm} = 10\\text{ m}$. A path is $4.5\\text{ cm}$ on the map. What is its real length?",
        "If you are facing North and turn $90^\\circ$ clockwise, which direction are you facing? What if you turn $180^\\circ$?",
        "On a scale plan of a warehouse ($1 : 100$), a storage bay measures $8\\text{ cm}$ by $5\\text{ cm}$. Calculate the real perimeter and real area of the bay in metres."
    )
    pages.append(p46)

    # CHECKPOINT 2: PAGES 47 TO 50 (4-page Review Assessment)
    chk2_p1 = [
        (1, 2, "Convert: a) $4.2\\text{ kg}$ to grams &emsp; b) $650\\text{ ml}$ to litres.", 75),
        (2, 2, "A train departs at 09:35 and arrives at 11:15. How long was the journey in hours and minutes?", 65),
        (3, 2, "Calculate the perimeter of a rectangle measuring $8\\text{ m}$ by $5.5\\text{ m}$.", 70)
    ]
    pages.append(checkpoint_page("Strand 2: Measures, Shape & Space", "Part 1 &bull; Non-Calculator (Q1-Q3)", 47, "6 Marks", chk2_p1))

    chk2_p2 = [
        (4, 2, "Calculate the area of a square patio with side length $6\\text{ m}$.", 75),
        (5, 2, "A bottle of medicine holds $250\\text{ ml}$. A patient takes $15\\text{ ml}$ per dose. How many full doses can be taken?", 65),
        (6, 2, "State the number of faces, edges, and vertices on a cuboid.", 70)
    ]
    pages.append(checkpoint_page("Strand 2: Measures, Shape & Space", "Part 1 &bull; Non-Calculator (Q4-Q6)", 48, "6 Marks", chk2_p2))

    chk2_p3 = [
        (7, 3, "A carpet costs $£18.50$ per square metre. A living room measures $5.4\\text{ m}$ by $4.0\\text{ m}$. Calculate the cost of the carpet.", 80),
        (8, 3, "A delivery driver travels 30 miles. Using $5\\text{ miles} = 8\\text{ km}$, convert this distance into kilometres.", 80),
        (9, 3, "A water cistern measures $1.2\\text{ m}$ long, $0.8\\text{ m}$ wide, and $0.6\\text{ m}$ high. How many litres of water does it hold? ($1\\text{ m}^3 = 1000\\text{ L}$)", 80)
    ]
    pages.append(checkpoint_page("Strand 2: Measures, Shape & Space", "Part 2 &bull; Calculator Allowed (Q7-Q9)", 49, "9 Marks", chk2_p3))

    chk2_p4 = [
        (10, 3, "A healthcare assistant works 32 basic hours at $£11.20/\\text{hr}$, plus 5 hours overtime at time-and-a-half ($£16.80/\\text{hr}$). What is her total pay?", 80),
        (11, 3, "On a map with scale $1\\text{ cm} = 50\\text{ m}$, the distance between two bus stops is $7.4\\text{ cm}$. What is the real distance in metres?", 80),
        (12, 3, "An L-shaped lawn has two sections: $6\\text{ m} \\times 4\\text{ m}$ and $3\\text{ m} \\times 2\\text{ m}$. Grass seed costs $£4.50$ per box. Each box covers $10\\text{ m}^2$. How much does it cost to seed the lawn?", 80)
    ]
    pages.append(checkpoint_page("Strand 2: Measures, Shape & Space", "Part 2 &bull; Calculator Allowed (Q10-Q12)", 50, "9 Marks", chk2_p4))

    # =========================================================================
    # STRAND 3: HANDLING INFORMATION & DATA (PAGES 51 - 70)
    # =========================================================================

    # TOPIC 21: PAGE 51 (Theory) & PAGE 52 (Practice)
    p51 = """
    <h2>Tally Charts &amp; Frequency Tables</h2>
    <p>Collecting raw data using tally marks grouped in bundles of five, and totaling frequencies accurately.</p>
    <div class="box-concept">
      <span class="tag-label tag-blue">The 5-Gate Rule</span> Tally marks are recorded as single vertical strokes. The fifth stroke crosses horizontally or diagonally through the four strokes (<s>||||</s>) to form a neat bundle of 5. This makes counting totals fast and error-free.
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Customer Survey Tally</span>
      <p>20 customers rated service: Good (11), Fair (6), Poor (3).</p>
      <table class="cgp-table">
        <tr><th>Rating</th><th>Tally</th><th>Frequency</th></tr>
        <tr><td>Good</td><td><s>||||</s> <s>||||</s> |</td><td>11</td></tr>
        <tr><td>Fair</td><td><s>||||</s> |</td><td>6</td></tr>
        <tr><td>Poor</td><td>|||</td><td>3</td></tr>
        <tr><td><strong>Total</strong></td><td>&mdash;</td><td><strong>20</strong></td></tr>
      </table>
    </div>
    """
    pages.append(wrap_page(p51, 51, "Strand 3: Handling Information & Data", "Standards: L1.28", "Maths Level 1 Core Revision Guide"))

    p52_scaffold = """
    <div class="step-row"><span>Step 1: Count tally bundles</span><span><s>||||</s> <s>||||</s> <s>||||</s> || = $5 + 5 + 5 + 2$</span></div>
    <div class="step-row"><span>Step 2: Total frequency</span><span>$\\mathbf{17}$</span></div>
    """
    p52 = practice_page(
        "Tally & Frequency", "Standards L1.28", 52, p52_scaffold,
        "Draw tally marks for: a) 8 &emsp; b) 14 &emsp; c) 19.",
        "A hotel receptionist logs room requests: Single (12), Double (18), Family (8). Complete a frequency table showing the tally and total.",
        "A cafe audits sandwich sales on Monday: Ham (24), Cheese (18), Tuna (12), Egg (6). What fraction of total sandwiches sold was Ham? Simplify your answer."
    )
    pages.append(p52)

    # TOPIC 22: PAGE 53 (Theory) & PAGE 54 (Practice)
    p53 = """
    <h2>Bar Charts &amp; Dual Comparative Charts</h2>
    <p>Drawing and interpreting bar charts with uniform bar widths, equal gaps, and accurate vertical scales.</p>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1d4ed8;">Rules for Bar Charts</h3>
      <p>&bull; Vertical frequency scale must start at <strong>0</strong> and have equal increments (e.g. 2, 4, 6 or 5, 10, 15).<br>
      &bull; Bars must be of <strong>equal width</strong> with <strong>equal gaps</strong> between categories.<br>
      &bull; Dual bar charts compare two groups side-by-side (include a clear key!).</p>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Reading a Bar Chart</span>
      <p>A bar chart displays daily attendance at a leisure centre: Mon 40, Tue 55, Wed 50, Thu 65, Fri 70.</p>
      <div class="step-row"><span>Highest attendance day (Mode)</span><strong>Friday (70)</strong></div>
      <div class="step-row"><span>Difference between Friday and Monday: 70 - 40</span><strong>30 visitors</strong></div>
    </div>
    """
    pages.append(wrap_page(p53, 53, "Strand 3: Handling Information & Data", "Standards: L1.29", "Maths Level 1 Core Revision Guide"))

    p54_scaffold = """
    <div class="step-row"><span>Step 1: Read bar heights</span><span>Group A = 45; Group B = 60</span></div>
    <div class="step-row"><span>Step 2: Difference</span><span>$60 - 45 = \\mathbf{15}$</span></div>
    """
    p54 = practice_page(
        "Bar Charts", "Standards L1.29", 54, p54_scaffold,
        "A bar chart shows car sales: Ford 25, Vauxhall 20, Toyota 30, BMW 15. State the most popular car make.",
        "From the car sales above, how many more Toyotas were sold than BMWs?",
        "A dual bar chart shows shoe sales for Men and Women across 4 sizes. Explain why a dual bar chart is better than two separate charts for comparing sales."
    )
    pages.append(p54)

    # TOPIC 23: PAGE 55 (Theory) & PAGE 56 (Practice)
    p55 = """
    <h2>Pictograms &amp; Symbol Keys</h2>
    <p>Representing data using pictures and symbols where each symbol represents a specific key value.</p>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1d4ed8;">The Importance of the Key</h3>
      <p>A pictogram is meaningless without a key. Always check the key first!<br>
      If &#9749; $= 4\\text{ cups of coffee}$:<br>
      &bull; 3 full symbols $= 3 \\times 4 = \\mathbf{12\\text{ cups}}$.<br>
      &bull; Half symbol $= 4 \\div 2 = \\mathbf{2\\text{ cups}}$.<br>
      &bull; Total for $3\\frac{1}{2}$ symbols $= 12 + 2 = \\mathbf{14\\text{ cups}}$.</p>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Car Wash Pictogram</span>
      <p>Key: &#128663; $= 10\\text{ cars washed}$. Tuesday shows $2\\frac{1}{2}$ symbols.</p>
      <div class="step-row"><span>2 full symbols: 2 × 10</span><strong>20 cars</strong></div>
      <div class="step-row"><span>Half symbol: 10 ÷ 2</span><strong>5 cars</strong></div>
      <div class="step-row"><span>Total washed on Tuesday</span><strong>25 cars</strong></div>
    </div>
    """
    pages.append(wrap_page(p55, 55, "Strand 3: Handling Information & Data", "Standards: L1.30", "Maths Level 1 Core Revision Guide"))

    p56_scaffold = """
    <div class="step-row"><span>Step 1: Check key value</span><span>Key: 1 symbol = 8 books</span></div>
    <div class="step-row"><span>Step 2: Multiply 4 full symbols</span><span>$4 \\times 8 = 32$</span></div>
    <div class="step-row"><span>Step 3: Add quarter symbol ($8 \\div 4 = 2$)</span><span>$32 + 2 = \\mathbf{34\\text{ books}}$</span></div>
    """
    p56 = practice_page(
        "Pictograms", "Standards L1.30", 56, p56_scaffold,
        "In a pictogram, &#9632; represents 6 vehicles. How many vehicles are represented by: a) 3 full squares &emsp; b) $2\\frac{1}{2}$ squares?",
        "A library uses a book symbol representing 10 books borrowed. On Thursday, 45 books were borrowed. How many symbols should be drawn?",
        "A bakery records pie sales: Steak 24, Chicken 16, Vegetable 8. Draw up a pictogram plan using a key of 1 symbol = 4 pies."
    )
    pages.append(p56)

    # TOPIC 24: PAGE 57 (Theory) & PAGE 58 (Practice)
    p57 = """
    <h2>Line Graphs &amp; Conversion Graphs</h2>
    <p>Plotting and reading continuous variables over time and using conversion lines to switch between currencies or units.</p>
    <div class="box-concept">
      <span class="tag-label tag-blue">Conversion Graphs</span>
      A straight line passing through $(0,0)$ allows direct conversion between two units. To convert: locate your known value on one axis, move straight to the line, and read the equivalent value on the opposite axis.
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Pounds to Euros Conversion</span>
      <p>A conversion graph shows $£10 = 12\\text{ Euros}$. Convert $£50$ to Euros.</p>
      <div class="step-row"><span>Scale factor: £50 is 5 times £10</span><strong>50 ÷ 10 = 5</strong></div>
      <div class="step-row"><span>Multiply Euros by 5: 12 × 5</span><strong>60 Euros</strong></div>
    </div>
    """
    pages.append(wrap_page(p57, 57, "Strand 3: Handling Information & Data", "Standards: L1.31", "Maths Level 1 Core Revision Guide"))

    p58_scaffold = """
    <div class="step-row"><span>Step 1: Read graph coordinates</span><span>$5\\text{ miles} = 8\\text{ km}$</span></div>
    <div class="step-row"><span>Step 2: Scale up to 20 miles</span><span>$20 \\div 5 = 4$ times larger</span></div>
    <div class="step-row"><span>Step 3: Multiply km</span><span>$8 \\times 4 = \\mathbf{32\\text{ km}}$</span></div>
    """
    p58 = practice_page(
        "Line Graphs", "Standards L1.31", 58, p58_scaffold,
        "A temperature line graph records: 09:00 ($12^\\circ\\text{C}$), 11:00 ($16^\\circ\\text{C}$), 13:00 ($20^\\circ\\text{C}$). Estimate temperature at 10:00.",
        "A conversion graph shows $£1 = $1.30 US Dollars. How many dollars do you receive for $£40$?",
        "A line graph shows patient heart rate over 4 hours. Explain why a line graph is better than a bar chart for displaying continuous physical measurements over time."
    )
    pages.append(p58)

    # TOPIC 25: PAGE 59 (Theory) & PAGE 60 (Practice)
    p59 = """
    <h2>Pie Charts: Fractions &amp; Proportions</h2>
    <p>Interpreting simple pie charts divided into standard benchmark fractions: halves, quarters, thirds, and tenths.</p>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1d4ed8;">Standard Benchmark Sectors</h3>
      <p>&bull; <strong>Half circle ($180^\\circ$):</strong> Represents $\\frac{1}{2}$ or $50\\%$ of total.<br>
      &bull; <strong>Quarter circle ($90^\\circ$):</strong> Represents $\\frac{1}{4}$ or $25\\%$ of total.<br>
      &bull; <strong>Three-quarters ($270^\\circ$):</strong> Represents $\\frac{3}{4}$ or $75\\%$ of total.</p>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Staff Commute Pie Chart</span>
      <p>80 employees were surveyed. In a pie chart, the sector for 'Drive to Work' is a right angle ($90^\\circ$). How many employees drive?</p>
      <div class="step-row"><span>Recognise right angle: 90° = 1/4 of circle</span><strong>1/4 of total</strong></div>
      <div class="step-row"><span>Calculate 1/4 of 80: 80 ÷ 4</span><strong>20 employees</strong></div>
    </div>
    """
    pages.append(wrap_page(p59, 59, "Strand 3: Handling Information & Data", "Standards: L1.32", "Maths Level 1 Core Revision Guide"))

    p60_scaffold = """
    <div class="step-row"><span>Step 1: Identify sector fraction</span><span>Half of circle = $\\frac{1}{2}$</span></div>
    <div class="step-row"><span>Step 2: Total surveyed</span><span>$120\\text{ people}$</span></div>
    <div class="step-row"><span>Step 3: Divide by 2</span><span>$120 \\div 2 = \\mathbf{60\\text{ people}}$</span></div>
    """
    p60 = practice_page(
        "Pie Charts", "Standards L1.32", 60, p60_scaffold,
        "In a pie chart of 200 people, a sector has a right angle ($90^\\circ$). How many people does this represent?",
        "A pie chart shows holiday choices for 60 students: $\\frac{1}{2}$ Beach, $\\frac{1}{4}$ City, $\\frac{1}{4}$ Activity. How many chose Beach?",
        "A company budget of $£40,000$ is split on a pie chart: Salaries ($180^\\circ$), Rent ($90^\\circ$), Utilities ($90^\\circ$). Calculate the amount spent on each category."
    )
    pages.append(p60)

    # TOPIC 26: PAGE 61 (Theory) & PAGE 62 (Practice)
    p61 = """
    <h2>The Mean Average: Calculating &amp; Comparing</h2>
    <p>The mean is the single balance value that summarizes a data set by distributing values equally.</p>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1d4ed8;">Statutory Mean Formula</h3>
      <p>$$\\text{Mean} = \\frac{\\text{Total Sum of all values}}{\\text{Total Number of values}}$$</p>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Finding Mean Test Score</span>
      <p>Five apprentices score: <strong>14, 18, 12, 16, 20</strong> on a health and safety quiz.</p>
      <div class="step-row"><span>Step 1: Add all scores: 14 + 18 + 12 + 16 + 20</span><strong>80</strong></div>
      <div class="step-row"><span>Step 2: Count number of scores</span><strong>5 scores</strong></div>
      <div class="step-row"><span>Step 3: Mean = 80 ÷ 5</span><strong>16 marks</strong></div>
    </div>
    """ + tutor_vignette("🧑‍🏫", "Tutor Marcus", "Senior Maths Educator", "Don't confuse Mean and Range! Mean is an average (a single typical score). Range is how spread out the scores are (biggest minus smallest).") + """
    """
    pages.append(wrap_page(p61, 61, "Strand 3: Handling Information & Data", "Standards: L1.33", "Maths Level 1 Core Revision Guide"))

    p62_scaffold = """
    <div class="step-row"><span>Step 1: Add values: $15 + 22 + 18 + 25$</span><span>$80$</span></div>
    <div class="step-row"><span>Step 2: Divide by count (4)</span><span>$80 \\div 4 = \\mathbf{20}$</span></div>
    """
    p62 = practice_page(
        "Mean Average", "Standards L1.33", 62, p62_scaffold,
        "Calculate the mean of: $8, 12, 15, 9, 16$.",
        "A sales rep logs daily phone calls: Mon 24, Tue 30, Wed 28, Thu 32, Fri 26. Find her mean daily calls.",
        "Four students have a mean test score of 15. A fifth student scores 25. Calculate the new mean score for all 5 students."
    )
    pages.append(p62)

    # TOPIC 27: PAGE 63 (Theory) & PAGE 64 (Practice)
    p63 = """
    <h2>The Range: Measuring Consistency &amp; Spread</h2>
    <p>The range measures the spread between the highest and lowest values. A smaller range indicates greater consistency.</p>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1d4ed8;">Range Formula</h3>
      <p>$$\\text{Range} = \\text{Highest Value} - \\text{Lowest Value}$$</p>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Comparing Two Workers</span>
      <p>Worker A: daily output $42, 45, 43, 44$. Range $= 45 - 42 = \\mathbf{3}$.<br>
      Worker B: daily output $30, 55, 32, 57$. Range $= 57 - 30 = \\mathbf{27}$.<br>
      <strong>Conclusion:</strong> Worker A is much more consistent because their range (3) is far smaller than Worker B's (27).</p>
    </div>
    """
    pages.append(wrap_page(p63, 63, "Strand 3: Handling Information & Data", "Standards: L1.34", "Maths Level 1 Core Revision Guide"))

    p64_scaffold = """
    <div class="step-row"><span>Step 1: Identify highest value</span><span>$38$</span></div>
    <div class="step-row"><span>Step 2: Identify lowest value</span><span>$14$</span></div>
    <div class="step-row"><span>Step 3: Subtract lowest from highest</span><span>$38 - 14 = \\mathbf{24}$</span></div>
    """
    p64 = practice_page(
        "The Range", "Standards L1.34", 64, p64_scaffold,
        "Find the range of: $18, 25, 12, 34, 29, 15$.",
        "A football team scores these goals in 6 matches: $2, 0, 4, 1, 3, 2$. Calculate: a) The mean goals &emsp; b) The range.",
        "Team A has mean delivery time 25 mins, range 4 mins. Team B has mean delivery time 25 mins, range 18 mins. Compare the teams in two sentences."
    )
    pages.append(p64)

    # TOPIC 28: PAGE 65 (Theory) & PAGE 66 (Practice)
    p65 = """
    <h2>The Probability Scale: 0 to 1 &amp; Likelihood</h2>
    <p>Probability measures how likely an event is to happen, measured on a scale from 0 (impossible) to 1 (certain).</p>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1d4ed8;">The Probability Scale</h3>
      <p>&bull; <strong>0:</strong> Impossible &bull; <strong>0.25 (1/4):</strong> Unlikely &bull; <strong>0.5 (1/2):</strong> Even chance (Evens)<br>
      &bull; <strong>0.75 (3/4):</strong> Likely &bull; <strong>1:</strong> Certain.<br>
      $$P(\\text{Event}) = \\frac{\\text{Number of successful outcomes}}{\\text{Total number of possible outcomes}}$$</p>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Rolling a Dice</span>
      <p>A fair 6-sided dice is rolled. What is the probability of rolling an odd number?</p>
      <div class="step-row"><span>Possible outcomes: 1, 2, 3, 4, 5, 6</span><strong>6 outcomes</strong></div>
      <div class="step-row"><span>Odd outcomes: 1, 3, 5</span><strong>3 outcomes</strong></div>
      <div class="step-row"><span>Probability = 3/6 = 1/2</span><strong>0.5 (Evens)</strong></div>
    </div>
    """
    pages.append(wrap_page(p65, 65, "Strand 3: Handling Information & Data", "Standards: L1.35, L1.36", "Maths Level 1 Core Revision Guide"))

    p66_scaffold = """
    <div class="step-row"><span>Step 1: Total items in bag ($4 + 6 = 10$)</span><span>$10\\text{ items}$</span></div>
    <div class="step-row"><span>Step 2: Favourable items (blue counters)</span><span>$4$</span></div>
    <div class="step-row"><span>Step 3: Fraction in simplest form</span><span>$\\frac{4}{10} = \\mathbf{\\frac{2}{5}}$ (or 0.4)</span></div>
    """
    p66 = practice_page(
        "Probability Scale", "Standards L1.35, L1.36", 66, p66_scaffold,
        "Match the probability: a) The sun rises tomorrow &emsp; b) Tossing a coin gives heads &emsp; c) Rolling an 8 on a standard 6-sided dice.",
        "A bag contains 5 red balls, 3 green balls, and 2 yellow balls. What is the probability of picking: a) A red ball &emsp; b) A yellow ball?",
        "A spinner has 8 equal sections numbered 1 to 8. List the probability of landing on: a) An even number &emsp; b) A number greater than 5 &emsp; c) The number 9."
    )
    pages.append(p66)

    # CHECKPOINT 3: PAGES 67 TO 70 (4-page Review Assessment)
    chk3_p1 = [
        (1, 2, "Test scores: $12, 18, 15, 11, 14$. Calculate: a) Mean &emsp; b) Range.", 75),
        (2, 2, "A spinner has 6 equal sections numbered 1 to 6. What is the probability of spinning an odd number?", 65),
        (3, 2, "A tally chart records: <s>||||</s> <s>||||</s> |||. Write the frequency number.", 70)
    ]
    pages.append(checkpoint_page("Strand 3: Handling Information & Data", "Part 1 &bull; Non-Calculator (Q1-Q3)", 67, "6 Marks", chk3_p1))

    chk3_p2 = [
        (4, 2, "In a bag there are 4 blue pens and 6 black pens. What is P(Blue) in simplest form?", 75),
        (5, 2, "A bar chart shows sandwich sales: Ham 15, Cheese 25, Tuna 10. What is the modal sandwich?", 65),
        (6, 2, "A conversion graph shows $£10 = 12\\text{ Euros}$. Convert $£30$ to Euros.", 70)
    ]
    pages.append(checkpoint_page("Strand 3: Handling Information & Data", "Part 1 &bull; Non-Calculator (Q4-Q6)", 68, "6 Marks", chk3_p2))

    chk3_p3 = [
        (7, 3, "A delivery depot records packages delivered: Mon 45, Tue 52, Wed 48, Thu 55, Fri 50. Calculate the mean daily deliveries.", 80),
        (8, 3, "In a pie chart representing 120 people, the sector for 'Public Transport' has a right angle ($90^\\circ$). How many people take public transport?", 80),
        (9, 3, "A pictogram uses a circle symbol &#9679; $= 8\\text{ cars}$. Monday shows 3 circles. Tuesday shows $2\\frac{1}{2}$ circles. How many cars in total were washed over both days?", 80)
    ]
    pages.append(checkpoint_page("Strand 3: Handling Information & Data", "Part 2 &bull; Calculator Allowed (Q7-Q9)", 69, "9 Marks", chk3_p3))

    chk3_p4 = [
        (10, 3, "Team Alpha mean score is 42, range is 5. Team Beta mean score is 42, range is 16. Write two comparison statements.", 80),
        (11, 3, "A box holds 20 light bulbs: 2 are defective. What is the probability that a bulb chosen at random is NOT defective? Give your answer as a decimal.", 80),
        (12, 3, "A survey asked 60 customers their preferred payment: Card (35), Cash (15), Phone App (10). What percentage preferred Card?", 80)
    ]
    pages.append(checkpoint_page("Strand 3: Handling Information & Data", "Part 2 &bull; Calculator Allowed (Q10-Q12)", 70, "9 Marks", chk3_p4))

    # =========================================================================
    # EXAM STRATEGY, FORMULAS & FULL MOCK EXAM (PAGES 71 - 78)
    # =========================================================================

    p71 = """
    <h2>Official Exam Master Strategy &amp; Assessment Skills</h2>
    <p>Practical rules to maximize your marks in the Pearson Edexcel Functional Skills Maths Level 1 exam.</p>
    <div class="box-concept">
      <h3 style="margin-top:0; color:var(--theme);">Understanding Examiner Mark Codes</h3>
      <p>&bull; <strong>[M] Method Marks:</strong> Awarded for showing the correct calculation (e.g. $45 \\times 6$). Even if your final multiplication is off, you secure the method mark!<br>
      &bull; <strong>[A] Accuracy Marks:</strong> Awarded for the correct numerical answer following correct method.<br>
      &bull; <strong>[B] Independent Marks:</strong> Awarded for units (e.g. $\\text{m}^2$ or $£$), drawing a bar accurately, or writing a comparison sentence.</p>
    </div>
    <div class="grid-2col">
      <div class="box-example">
        <h3 style="margin-top:0; color:#15803d;">Section A Non-Calc Tactics</h3>
        <p>&bull; 25 minutes for 14 marks &rarr; take your time!<br>
        &bull; Use column addition and subtraction.<br>
        &bull; Check subtraction using addition.<br>
        &bull; Simplify fractions at the end.</p>
      </div>
      <div class="box-example">
        <h3 style="margin-top:0; color:#15803d;">Section B Calculator Tactics</h3>
        <p>&bull; 1 hour 30 mins for 42 marks.<br>
        &bull; Write down the calculation you type.<br>
        &bull; Always write money as 2 decimal places ($£12.50$, not $£12.5$).<br>
        &bull; Don't leave any blanks!</p>
      </div>
    </div>
    """ + tutor_vignette("🧑‍🏫", "Tutor Marcus", "Senior Maths Educator", "If a question asks 'Show a check', do NOT skip it! It is an easy guaranteed mark: just write the inverse calculation!") + """
    """
    pages.append(wrap_page(p71, 71, "Exam Master Strategy", "Assessment Skills", "Maths Level 1 Core Revision Guide"))

    p72 = """
    <h2>Statutory Formula Sheet &amp; Reference Guide</h2>
    <p>Statutory facts and formulas for Functional Skills Mathematics Level 1.</p>
    <table class="cgp-table">
      <tr><th>Mathematical Domain</th><th>Statutory Formula / Definition</th><th>Practical Context</th></tr>
      <tr><td><strong>Rectangle Perimeter</strong></td><td>$P = 2l + 2w$ or $2(l + w)$</td><td>Fencing, skirting boards, frame borders.</td></tr>
      <tr><td><strong>Rectangle Area</strong></td><td>$\\text{Area} = \\text{length} \\times \\text{width}$</td><td>Carpeting, turfing, painting, paving.</td></tr>
      <tr><td><strong>Cuboid Volume</strong></td><td>$\\text{Volume} = l \\times w \\times h$</td><td>Box capacity, water tanks, gravel storage.</td></tr>
      <tr><td><strong>Mean Average</strong></td><td>$\\text{Mean} = \\text{Sum of values} \\div \\text{Count of values}$</td><td>Average weekly hours, test marks, customer wait.</td></tr>
      <tr><td><strong>The Range</strong></td><td>$\\text{Range} = \\text{Highest} - \\text{Lowest}$</td><td>Consistency check across production lines.</td></tr>
      <tr><td><strong>Simple Probability</strong></td><td>$P = \\text{Favourable} \\div \\text{Total Possible}$</td><td>Raffle tickets, picking colored items, dice.</td></tr>
      <tr><td><strong>Metric Conversion</strong></td><td>$1\\text{ m} = 100\\text{ cm}$; $1\\text{ kg} = 1000\\text{ g}$; $1\\text{ L} = 1000\\text{ ml}$</td><td>Recipe batching, medicine doses, material cuts.</td></tr>
      <tr><td><strong>Imperial Approximation</strong></td><td>$5\\text{ miles} \\approx 8\\text{ km}$; $1\\text{ kg} \\approx 2.2\\text{ lbs}$; $1\\text{ in} \\approx 2.5\\text{ cm}$</td><td>Road travel distances, freight cargo weights.</td></tr>
    </table>
    """
    pages.append(wrap_page(p72, 72, "Statutory Formula Sheet", "Reference Guide", "Maths Level 1 Core Revision Guide"))

    # MOCK EXAM: PAGES 73 TO 78 (6 full pages)
    mock_p73 = [
        (1, 3, "Work out without a calculator: $418 \\times 14$. Show your full column method.", 80, "Answer"),
        (2, 2, "A bank account balance is $-£160$. A wages payment of $+£520$ is paid in, and a bill of $£180$ is paid out. What is the new balance?", 75, "Balance"),
        (3, 3, "Calculate without using a calculator: $1,638 \\div 7$. Show your bus stop division.", 80, "Answer")
    ]
    pages.append(mock_page("Section A: Non-Calculator", 73, mock_p73))

    mock_p74 = [
        (4, 2, "Work out: $18 - 2 \\times 5 + 4$.", 75, "Answer"),
        (5, 2, "Simplify fully: $\\frac{16}{28}$.", 70, "Answer"),
        (6, 2, "Share $£150$ in the ratio $3 : 2$. What is the smaller share?", 75, "Smaller Share")
    ]
    pages.append(mock_page("Section A: Non-Calculator", 74, mock_p74))

    mock_p75 = [
        (7, 3, "A winter coat is priced at $£75.00$. It is discounted by $20\\%$ in a sale. Calculate the sale price.", 80, "Sale Price"),
        (8, 3, "A pancake recipe for 4 people requires $250\\text{ g}$ flour and $300\\text{ ml}$ milk. How much flour and milk are needed for 6 people?", 80, "Flour & Milk"),
        (9, 3, "A delivery van travels 45 miles. Using $5\\text{ miles} = 8\\text{ km}$, convert 45 miles into kilometres.", 80, "Distance in km")
    ]
    pages.append(mock_page("Section B: Calculator Allowed", 75, mock_p75))

    mock_p76 = [
        (10, 4, "A landscape gardener lays turf on a rectangular lawn measuring $8.5\\text{ m}$ by $6.0\\text{ m}$. Turf rolls cover $1\\text{ m}^2$ each and cost $£4.50$. Delivery is $£20.00$. Calculate the total cost.", 95, "Total Cost"),
        (11, 4, "A healthcare assistant works 30 basic hours at $£11.50/\\text{hr}$, plus 4 hours overtime at time-and-a-half ($£17.25/\\text{hr}$). What is her total gross pay?", 95, "Gross Pay"),
        (12, 4, "A water cistern measures $1.5\\text{ m}$ long, $0.8\\text{ m}$ wide, and $0.5\\text{ m}$ deep. How many litres of water does it hold when full? ($1\\text{ m}^3 = 1000\\text{ litres}$)", 95, "Capacity in Litres")
    ]
    pages.append(mock_page("Section B: Calculator Allowed", 76, mock_p76))

    mock_p77 = [
        (13, 4, "A train departs Manchester at 10:48 and arrives in Leeds at 12:05. How long did the train journey take in hours and minutes?", 95, "Journey Time"),
        (14, 4, "Daily parcel deliveries by a driver: Mon 38, Tue 45, Wed 42, Thu 49, Fri 46. Calculate: a) The mean daily deliveries &emsp; b) The range.", 95, "Mean & Range")
    ]
    pages.append(mock_page("Section B: Calculator Allowed", 77, mock_p77))

    mock_p78 = [
        (15, 5, "On a scale drawing of a garden ($1 : 50$), a patio measures $12\\text{ cm}$ by $8\\text{ cm}$. Calculate the real perimeter of the patio in metres, and the real area in square metres.", 115, "Perimeter & Area"),
        (16, 5, "A clinic audits 100 patients: 60 are female. 45 females had a flu vaccination. 25 males had a flu vaccination. Construct a two-way table. What is the probability that a patient chosen at random was vaccinated?", 115, "Probability")
    ]
    pages.append(mock_page("Section B: Calculator Allowed", 78, mock_p78))

    # =========================================================================
    # ANSWER KEYS & DETAILED MARK SCHEMES (PAGES 79 - 82)
    # =========================================================================

    t79 = """
    <h3 style="color:var(--theme); margin-top:2px;">Strand 1 Checkpoint Solutions (Pages 23-26)</h3>
    <table class="cgp-table" style="font-size:7.4pt;">
      <tr><th style="width:10%;">Q</th><th style="width:25%;">Answer</th><th>Mark Allocation &amp; Step-by-Step Marking Guidance</th></tr>
      <tr><td>1</td><td><strong>5,568</strong></td><td><strong>[M1]</strong> 348 × 4 = 1,392; 348 × 10 = 3,480 <strong>[A1]</strong> 1392 + 3480 = 5,568.</td></tr>
      <tr><td>2</td><td><strong>£265.00</strong></td><td><strong>[M1]</strong> -185 + 450 <strong>[A1]</strong> £265.00.</td></tr>
      <tr><td>3</td><td><strong>3/4; 60%</strong></td><td><strong>[B1]</strong> 18/24 = 3/4 <strong>[B1]</strong> 3/5 = 6/10 = 60%.</td></tr>
      <tr><td>4</td><td><strong>246</strong></td><td><strong>[M1]</strong> 6 into 14 = 2 r 2; 6 into 27 = 4 r 3; 6 into 36 = 6 <strong>[A1]</strong> 246.</td></tr>
      <tr><td>5</td><td><strong>10</strong></td><td><strong>[M1]</strong> Multiplication first: 4 × 3 = 12; 20 - 12 + 2 <strong>[A1]</strong> 10.</td></tr>
      <tr><td>6</td><td><strong>£90.00</strong></td><td><strong>[M1]</strong> 3+1 = 4 parts; 120 ÷ 4 = 30; 3 × 30 <strong>[A1]</strong> £90.00.</td></tr>
      <tr><td>7</td><td><strong>£68.00</strong></td><td><strong>[M1]</strong> 10% = £8.00; 20% = £16.00; 80 - 16 <strong>[A1]</strong> £68.00.</td></tr>
      <tr><td>8</td><td><strong>675 g</strong></td><td><strong>[M1]</strong> 300 ÷ 4 = 75 g per person; 75 × 9 <strong>[A1]</strong> 675 g.</td></tr>
      <tr><td>9</td><td><strong>140 parcels</strong></td><td><strong>[M1]</strong> 350 ÷ 5 = 70; Delivered = 70 × 3 = 210; 350 - 210 <strong>[A1]</strong> 140 parcels.</td></tr>
      <tr><td>10</td><td><strong>£189.00</strong></td><td><strong>[M1]</strong> 4.5 × 32 = 144; 144 + 45 <strong>[A1]</strong> £189.00.</td></tr>
      <tr><td>11</td><td><strong>Pack B is cheaper</strong></td><td><strong>[M1]</strong> Pack A: 4.20 ÷ 6 = 70p; Pack B: 6.80 ÷ 10 = 68p <strong>[A1]</strong> Pack B is 2p cheaper per can.</td></tr>
      <tr><td>12</td><td><strong>No (needs £187)</strong></td><td><strong>[M1]</strong> 24 × 6.75 = 162; 162 + 25 = £187.00 <strong>[A1]</strong> £187 > £180, so £7 short.</td></tr>
    </table>
    <h3 style="color:var(--theme); margin-top:4px;">Strand 2 Checkpoint Solutions (Pages 47-50)</h3>
    <table class="cgp-table" style="font-size:7.4pt;">
      <tr><th style="width:10%;">Q</th><th style="width:25%;">Answer</th><th>Mark Allocation &amp; Step-by-Step Marking Guidance</th></tr>
      <tr><td>1</td><td><strong>4200g; 0.65L</strong></td><td><strong>[B1]</strong> 4,200 g <strong>[B1]</strong> 0.65 litres.</td></tr>
      <tr><td>2</td><td><strong>1h 40m</strong></td><td><strong>[M1]</strong> 09:35 to 10:35 = 1h; 10:35 to 11:15 = 40m <strong>[A1]</strong> 1 hour 40 minutes.</td></tr>
      <tr><td>3</td><td><strong>27 metres</strong></td><td><strong>[M1]</strong> 2 × (8 + 5.5) = 2 × 13.5 <strong>[A1]</strong> 27 metres.</td></tr>
      <tr><td>4</td><td><strong>36 m²</strong></td><td><strong>[M1]</strong> 6 × 6 <strong>[A1]</strong> 36 m².</td></tr>
      <tr><td>5</td><td><strong>16 full doses</strong></td><td><strong>[M1]</strong> 250 ÷ 15 = 16.66 <strong>[A1]</strong> 16 full doses (10 ml left).</td></tr>
      <tr><td>6</td><td><strong>6 faces, 12 edges, 8 vertices</strong></td><td><strong>[B1]</strong> 6 faces <strong>[B1]</strong> 12 edges and 8 vertices.</td></tr>
      <tr><td>7</td><td><strong>£399.60</strong></td><td><strong>[M1]</strong> Area: 5.4 × 4.0 = 21.6 m²; 21.6 × £18.50 <strong>[A1]</strong> £399.60.</td></tr>
      <tr><td>8</td><td><strong>48 km</strong></td><td><strong>[M1]</strong> (30 ÷ 5) × 8 = 6 × 8 <strong>[A1]</strong> 48 km.</td></tr>
      <tr><td>9</td><td><strong>576 litres</strong></td><td><strong>[M1]</strong> Volume: 1.2 × 0.8 × 0.6 = 0.576 m³; 0.576 × 1000 <strong>[A1]</strong> 576 litres.</td></tr>
      <tr><td>10</td><td><strong>£442.40</strong></td><td><strong>[M1]</strong> Basic: 32 × 11.20 = £358.40; OT: 5 × 16.80 = £84.00 <strong>[A1]</strong> £442.40.</td></tr>
      <tr><td>11</td><td><strong>370 metres</strong></td><td><strong>[M1]</strong> 7.4 × 50 <strong>[A1]</strong> 370 metres.</td></tr>
      <tr><td>12</td><td><strong>£13.50 (3 boxes)</strong></td><td><strong>[M1]</strong> Area: (6×4) + (3×2) = 24 + 6 = 30 m²; Boxes: 30 ÷ 10 = 3 boxes; 3 × £4.50 <strong>[A1]</strong> £13.50.</td></tr>
    </table>
    """
    pages.append(mark_scheme_page("Answer Keys & Formal Mark Schemes", "Strand 1 & Strand 2 Checkpoints", 79, t79))

    t80 = """
    <h3 style="color:var(--theme); margin-top:2px;">Strand 3 Checkpoint Solutions (Pages 67-70)</h3>
    <table class="cgp-table" style="font-size:7.4pt;">
      <tr><th style="width:10%;">Q</th><th style="width:25%;">Answer</th><th>Mark Allocation &amp; Step-by-Step Marking Guidance</th></tr>
      <tr><td>1</td><td><strong>Mean = 14.8; Range = 7</strong></td><td><strong>[M1]</strong> Sum = 74; 74 ÷ 5 = 14.8 <strong>[A1]</strong> Range = 18 - 11 = 7.</td></tr>
      <tr><td>2</td><td><strong>3/6 (1/2 or Evens)</strong></td><td><strong>[M1]</strong> Odd outcomes: 1, 3, 5; 3/6 <strong>[A1]</strong> 1/2.</td></tr>
      <tr><td>3</td><td><strong>13</strong></td><td><strong>[B1]</strong> 5 + 5 + 3 = 13.</td></tr>
      <tr><td>4</td><td><strong>4/10 (2/5)</strong></td><td><strong>[M1]</strong> Total = 10; 4/10 <strong>[A1]</strong> 2/5.</td></tr>
      <tr><td>5</td><td><strong>Cheese</strong></td><td><strong>[B1]</strong> Highest bar = Cheese (25).</td></tr>
      <tr><td>6</td><td><strong>36 Euros</strong></td><td><strong>[M1]</strong> £30 = 3 × £10; 3 × 12 Euros <strong>[A1]</strong> 36 Euros.</td></tr>
      <tr><td>7</td><td><strong>50 packages</strong></td><td><strong>[M1]</strong> Sum = 45+52+48+55+50 = 250; 250 ÷ 5 <strong>[A1]</strong> 50 packages.</td></tr>
      <tr><td>8</td><td><strong>30 people</strong></td><td><strong>[M1]</strong> 90° = 1/4; 120 ÷ 4 <strong>[A1]</strong> 30 people.</td></tr>
      <tr><td>9</td><td><strong>44 cars</strong></td><td><strong>[M1]</strong> Mon: 3 × 8 = 24; Tue: 2.5 × 8 = 20; 24 + 20 <strong>[A1]</strong> 44 cars.</td></tr>
      <tr><td>10</td><td><strong>Alpha more consistent</strong></td><td><strong>[M1]</strong> Both have identical mean (42) <strong>[A1]</strong> Alpha is more consistent (range 5 vs 16).</td></tr>
      <tr><td>11</td><td><strong>0.90 (9/10)</strong></td><td><strong>[M1]</strong> Non-defective = 18; 18 ÷ 20 <strong>[A1]</strong> 0.90.</td></tr>
      <tr><td>12</td><td><strong>58.3% (35/60)</strong></td><td><strong>[M1]</strong> (35 ÷ 60) × 100 <strong>[A1]</strong> 58.3% (accept 58%).</td></tr>
    </table>
    """
    pages.append(mark_scheme_page("Answer Keys & Formal Mark Schemes", "Strand 3 Checkpoint Solutions", 80, t80))

    t81 = """
    <h3 style="color:var(--theme); margin-top:2px;">Official Mock Exam &bull; Section A Mark Scheme (Pages 73-74)</h3>
    <table class="cgp-table" style="font-size:7.4pt;">
      <tr><th style="width:8%;">Q</th><th style="width:12%;">Marks</th><th style="width:25%;">Correct Answer</th><th>Mark Scheme &amp; Detailed Method Breakdown</th></tr>
      <tr><td>1</td><td>3</td><td><strong>5,852</strong></td><td><strong>[M1]</strong> 418 × 4 = 1,672 <strong>[M1]</strong> 418 × 10 = 4,180 <strong>[A1]</strong> 1672 + 4180 = 5,852.</td></tr>
      <tr><td>2</td><td>2</td><td><strong>£180.00</strong></td><td><strong>[M1]</strong> -160 + 520 = 360; 360 - 180 <strong>[A1]</strong> £180.00.</td></tr>
      <tr><td>3</td><td>3</td><td><strong>234</strong></td><td><strong>[M1]</strong> 7 into 16 = 2 r 2 <strong>[M1]</strong> 7 into 23 = 3 r 2; 7 into 28 = 4 <strong>[A1]</strong> 234.</td></tr>
      <tr><td>4</td><td>2</td><td><strong>12</strong></td><td><strong>[M1]</strong> Multiply first: 2 × 5 = 10; 18 - 10 + 4 <strong>[A1]</strong> 12.</td></tr>
      <tr><td>5</td><td>2</td><td><strong>4/7</strong></td><td><strong>[M1]</strong> Divide top and bottom by 4 <strong>[A1]</strong> 4/7.</td></tr>
      <tr><td>6</td><td>2</td><td><strong>£60.00</strong></td><td><strong>[M1]</strong> 3+2 = 5 parts; 150 ÷ 5 = 30; 2 × 30 <strong>[A1]</strong> £60.00.</td></tr>
    </table>
    """
    pages.append(mark_scheme_page("Official Mock Exam Mark Scheme", "Section A (Non-Calculator)", 81, t81))

    t82 = """
    <h3 style="color:var(--theme); margin-top:2px;">Official Mock Exam &bull; Section B Mark Scheme (Pages 75-78)</h3>
    <table class="cgp-table" style="font-size:7.2pt;">
      <tr><th style="width:6%;">Q</th><th style="width:8%;">Marks</th><th style="width:22%;">Correct Answer</th><th>Mark Scheme &amp; Detailed Method Breakdown</th></tr>
      <tr><td>7</td><td>3</td><td><strong>£60.00</strong></td><td><strong>[M1]</strong> 0.20 × £75.00 = £15.00 <strong>[M1]</strong> 75 - 15 <strong>[A1]</strong> £60.00.</td></tr>
      <tr><td>8</td><td>3</td><td><strong>375g flour; 450ml milk</strong></td><td><strong>[M1]</strong> Multiplier: 6 ÷ 4 = 1.5 <strong>[A1]</strong> Flour: 250 × 1.5 = 375 g <strong>[A1]</strong> Milk: 300 × 1.5 = 450 ml.</td></tr>
      <tr><td>9</td><td>3</td><td><strong>72 km</strong></td><td><strong>[M1]</strong> 45 ÷ 5 = 9 <strong>[M1]</strong> 9 × 8 <strong>[A1]</strong> 72 km.</td></tr>
      <tr><td>10</td><td>4</td><td><strong>£249.50</strong></td><td><strong>[P1]</strong> Area = 8.5 × 6.0 = 51 m² <strong>[M1]</strong> 51 × £4.50 = £229.50 <strong>[M1]</strong> Add delivery: 229.50 + 20.00 <strong>[A1]</strong> £249.50.</td></tr>
      <tr><td>11</td><td>4</td><td><strong>£414.00</strong></td><td><strong>[P1]</strong> Basic: 30 × 11.50 = £345.00 <strong>[M1]</strong> OT: 4 × 17.25 = £69.00 <strong>[M1]</strong> 345 + 69 <strong>[A1]</strong> £414.00.</td></tr>
      <tr><td>12</td><td>4</td><td><strong>600 litres</strong></td><td><strong>[P1]</strong> Volume = 1.5 × 0.8 × 0.5 = 0.6 m³ <strong>[M1]</strong> Convert: 0.6 × 1000 <strong>[A1]</strong> 600 litres.</td></tr>
      <tr><td>13</td><td>4</td><td><strong>1h 17m (77 mins)</strong></td><td><strong>[M1]</strong> 10:48 to 11:00 = 12 mins <strong>[M1]</strong> 11:00 to 12:05 = 1 hour 5 mins <strong>[A1]</strong> 1 hour 17 minutes.</td></tr>
      <tr><td>14</td><td>4</td><td><strong>Mean = 44; Range = 11</strong></td><td><strong>[P1]</strong> Sum = 38+45+42+49+46 = 220 <strong>[M1]</strong> Mean: 220 ÷ 5 = 44 <strong>[M1]</strong> Range: 49 - 38 = 11 <strong>[A1]</strong> Correct values.</td></tr>
      <tr><td>15</td><td>5</td><td><strong>20 m; 24 m²</strong></td><td><strong>[P1]</strong> Real L = 12 × 50 = 600 cm = 6 m; Real W = 8 × 50 = 400 cm = 4 m <strong>[M1]</strong> Perimeter: 2 × (6 + 4) = 20 m <strong>[M1]</strong> Area: 6 × 4 = 24 m² <strong>[A1]</strong> Perimeter = 20 m <strong>[A1]</strong> Area = 24 m².</td></tr>
      <tr><td>16</td><td>5</td><td><strong>0.70 (70% or 7/10)</strong></td><td><strong>[P1]</strong> Table completed: Total vac = 45 + 25 = 70 <strong>[M1]</strong> Total patients = 100 <strong>[M1]</strong> Fraction = 70 / 100 <strong>[A1]</strong> 0.70 (70%).</td></tr>
    </table>
    """
    pages.append(mark_scheme_page("Official Mock Exam Mark Scheme", "Section B (Calculator Allowed)", 82, t82))

    # PAGE 83: Master Glossary & Quick Index
    p83 = """
    <h2>Level 1 Master Glossary &amp; Examination Checklist</h2>
    <div class="grid-2col">
      <div class="box-concept">
        <h3 style="margin-top:0; color:var(--theme);">Core Mathematical Vocabulary</h3>
        <p style="font-size:7.4pt; margin:0 0 3px 0;"><strong>Acute Angle:</strong> An angle less than 90°.</p>
        <p style="font-size:7.4pt; margin:0 0 3px 0;"><strong>Area:</strong> The 2D surface space inside a shape (length × width).</p>
        <p style="font-size:7.4pt; margin:0 0 3px 0;"><strong>BIDMAS:</strong> Sequence of operations: Brackets, Indices, Divide, Multiply, Add, Subtract.</p>
        <p style="font-size:7.4pt; margin:0 0 3px 0;"><strong>Cuboid:</strong> A 3D box with 6 rectangular faces.</p>
        <p style="font-size:7.4pt; margin:0 0 3px 0;"><strong>Denominator:</strong> The bottom number in a fraction (total equal parts).</p>
        <p style="font-size:7.4pt; margin:0 0 3px 0;"><strong>Equivalent:</strong> Having the exact same mathematical value.</p>
        <p style="font-size:7.4pt; margin:0 0 3px 0;"><strong>Mean:</strong> Total sum of items divided by total item count.</p>
        <p style="font-size:7.4pt; margin:0 0 3px 0;"><strong>Numerator:</strong> The top number in a fraction (parts considered).</p>
        <p style="font-size:7.4pt; margin:0 0 3px 0;"><strong>Obtuse Angle:</strong> An angle between 90° and 180°.</p>
        <p style="font-size:7.4pt; margin:0 0 3px 0;"><strong>Perimeter:</strong> Total distance around the outer boundary edge.</p>
        <p style="font-size:7.4pt; margin:0 0 3px 0;"><strong>Range:</strong> Difference between maximum and minimum values.</p>
        <p style="font-size:7.4pt; margin:0 0 3px 0;"><strong>Volume:</strong> 3D space occupied by a solid object.</p>
      </div>
      <div class="box-example">
        <h3 style="margin-top:0; color:#15803d;">Final Exam Readiness Checklist</h3>
        <ul style="font-size:7.4pt; margin:0 0 0 14px; padding:0;">
          <li>Non-calc: Column multiplication and bus-stop division.</li>
          <li>Fractions: Simplifying and finding fractions of amounts.</li>
          <li>Percentages: Benchmark mental finding (10%, 25%, 50%).</li>
          <li>Units: Metric conversions (cm to m, grams to kg, ml to L).</li>
          <li>Imperial: 5 miles is approximately 8 kilometres.</li>
          <li>Geometry: Perimeter (metres) vs Area (square metres).</li>
          <li>Time: Base-60 conversions (jumping through the hour).</li>
          <li>Data: Mean average (sum ÷ count) and Range (high - low).</li>
          <li>Checking: Inverse check calculation shown for check marks.</li>
        </ul>
      </div>
    </div>
    <div class="box-formula" style="margin-top:5px;">
      <h3 style="margin-top:0; color:#1e40af;">Subject Quick Index</h3>
      <p style="font-size:7.3pt; margin:0;">
        Angles: 41 &bull; Area: 37, 38 &bull; Averages: 61, 62 &bull; Bar Charts: 53 &bull; BIDMAS: 21 &bull; Checkpoints: 23, 47, 67 &bull; Compass: 45 &bull; Cuboid: 39 &bull; Decimals: 13 &bull; Equivalences: 15 &bull; Estimation: 19 &bull; Factors: 7 &bull; Formulas: 21, 72 &bull; Fractions: 9, 11 &bull; Imperial: 29 &bull; Line Graphs: 57 &bull; Mean: 61 &bull; Metric: 27 &bull; Mock Exam: 73&ndash;78 &bull; Money: 33 &bull; Multiples: 7 &bull; Negative Numbers: 3 &bull; Nets: 43 &bull; Percentages: 15 &bull; Perimeter: 35 &bull; Pictograms: 55 &bull; Pie Charts: 59 &bull; Place Value: 3 &bull; Primes: 7 &bull; Probability: 65 &bull; Range: 63 &bull; Ratio: 17 &bull; Rounding: 19 &bull; Scale Plans: 45 &bull; Tally Charts: 51 &bull; Time: 31 &bull; Volume: 39.
      </p>
    </div>
    """
    pages.append(wrap_page(p83, 83, "Level 1 Glossary & Index", "Reference Section", "Maths Level 1 Core Revision Guide"))

    # PAGE 84: Back Cover
    pages.append(f"""
    <div class="page cover-full-page">
      <img src="file://{back_img}" class="cover-full-img" alt="Level 1 Core Guide Back Cover">
    </div>
    """)

    # Verify total page count in memory
    total_pages = len(pages)
    print(f"Total HTML pages assembled: {total_pages}")
    assert total_pages == 84, f"Expected 84 pages, got {total_pages}"

    # Combine into full HTML document
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Maths Level 1 Core Revision Guide - Master Functional Skills</title>
{get_shared_css(theme_color="#002046", accent_color="#0284c7", light_bg="#f0f7ff")}
</head>
<body>
{''.join(pages)}
</body>
</html>
"""

    temp_html = os.path.join(SCRATCH_DIR, "maths_l1_core_guide_84p.html")
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"Building {out_name} via Chromium headless...")
    cmd = [
        CHROME_BIN,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--user-data-dir=/tmp/chr_l1_core_84",
        "--no-pdf-header-footer",
        f"--print-to-pdf={target_downloads}",
        temp_html
    ]
    subprocess.run(cmd, check=True)

    # Copy to ~/Documents/
    shutil.copy2(target_downloads, target_documents)
    print(f"Copied to {target_documents}")

    # Verify page count with pdfinfo
    out = subprocess.check_output(["pdfinfo", target_downloads]).decode()
    for line in out.splitlines():
        if "Pages:" in line:
            print(f"Level 1 Core Guide PDF Result: {line}")
            return line

if __name__ == "__main__":
    build_l1_core_guide()
