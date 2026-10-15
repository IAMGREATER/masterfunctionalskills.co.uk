#!/usr/bin/env python3
"""
books/maths_builders/generate_l2_core_84p.py
Constructs the complete 84-page MasterFunctionalSkills_Maths_Level_2_Core_Guide.pdf
Strictly mapped to Pearson Edexcel Reformed Functional Skills Mathematics Level 2.
"""

import os
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

import sys
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

from book_theme import get_shared_css, wrap_page

def build_l2_core_guide():
    front_img = os.path.join(BOOKS_IMG_DIR, "maths_l2_core_cover_page-1.png")
    back_img = os.path.join(BOOKS_IMG_DIR, "maths_l2_core_cover_page-2.png")
    out_name = "MasterFunctionalSkills_Maths_Level_2_Core_Guide.pdf"
    target_downloads = os.path.join(DOWNLOADS_DIR, out_name)
    target_documents = os.path.join(DOCUMENTS_DIR, out_name)

    pages = []

    # Helper for Practice Pages (Page 2 of 2-page topic spreads)
    def practice_page(title, standard, page_num, scaffold_html, q1_html, q2_html, q3_html):
        content = f"""
        <div style="font-size:7.5pt; font-weight:800; color:var(--theme); text-transform:uppercase; letter-spacing:0.5px; margin-bottom:2px;">
          Guided Practice &bull; Workspace &bull; {standard}
        </div>
        <h2 style="font-size:10.5pt; margin-bottom:4px;">{title}: Practice Drills</h2>

        <!-- Guided Calculation Scaffold -->
        <div class="box-concept" style="padding:5px 8px; margin-bottom:4px; border-left-color:var(--accent);">
          <strong style="color:var(--theme); font-size:7.8pt;">Guided Calculation Frame:</strong>
          {scaffold_html}
        </div>

        <!-- Question 1: Foundation / Technique -->
        <div class="q-card" style="padding:5px 8px; margin:4px 0;">
          <div class="q-header">
            <span class="q-num">Exercise A: Core Technique Drill</span>
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
        return wrap_page(content, page_num, "Strand Practice Drill", standard, "Maths Level 2 Core Study Guide")

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
        return wrap_page(content, page_num, f"{strand_name} Checkpoint Review", part_label, "Maths Level 2 Core Study Guide")

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
          <span style="font-size:7.5pt; font-weight:700; color:#475569;">Functional Skills Maths Level 2</span>
        </div>
        {items_html}
        """
        return wrap_page(content, page_num, f"Official Mock Exam &bull; {sec_title}", "Standard Exam Simulation", "Maths Level 2 Core Study Guide")

    # Helper for Mark Scheme pages
    def mark_scheme_page(title, sub_title, page_num, tables_html):
        content = f"""
        <div style="border-bottom:1.5px solid var(--theme); padding-bottom:3px; margin-bottom:6px;">
          <h2 style="margin:0; font-size:11pt; color:var(--theme);">{title}</h2>
          <div style="font-size:7.5pt; color:#64748b;"><strong>{sub_title}</strong> &bull; Marking Codes: [P1] Process &bull; [M1] Method &bull; [A1] Accuracy &bull; [B1] Independent</div>
        </div>
        {tables_html}
        """
        return wrap_page(content, page_num, title, sub_title, "Maths Level 2 Core Study Guide")

    # =========================================================================
    # BUILD PAGES 1 TO 84
    # =========================================================================

    # PAGE 1: Front Cover
    pages.append(f"""
    <div class="page cover-full-page">
      <img src="file://{front_img}" class="cover-full-img" alt="Level 2 Core Guide Front Cover">
    </div>
    """)

    # PAGE 2: Inside Cover & Ofqual Mapping
    p2 = """
    <h1>Functional Skills Maths Level 2 Core Study Guide</h1>
    <div style="font-size:8.5pt; color:#475569; margin-bottom:8px;"><strong>Specification Standard:</strong> Pearson Edexcel Reformed Functional Skills Mathematics (Level 2) &bull; Ofqual Regulated</div>

    <div class="box-concept">
      <h3 style="margin-top:0;">Welcome to Master Functional Skills</h3>
      <p>This comprehensive study manual is engineered to take you from foundational understanding to full exam mastery. Functional Skills Mathematics Level 2 is officially recognised as the GCSE Grade 4/C equivalent qualification across the UK, required for nursing, apprenticeships, policing, university entrance, and professional promotions.</p>
    </div>

    <h2>Statutory Curriculum Mapping (39 Ofqual Standards)</h2>
    <table class="cgp-table">
      <tr>
        <th style="width:28%;">Curriculum Strand</th>
        <th style="width:18%;">Standards</th>
        <th>Core Mathematical Domains &amp; Exam Weighting</th>
      </tr>
      <tr>
        <td><strong>1. Number &amp; Number Systems</strong></td>
        <td>L2.1 &ndash; L2.11</td>
        <td>Place value, negative numbers, fraction operations, decimal arithmetic, percentage multipliers, reverse percentages, compound interest, ratio division, direct &amp; inverse proportion (approx. 25% of marks).</td>
      </tr>
      <tr>
        <td><strong>2. Measures, Shape &amp; Space</strong></td>
        <td>L2.12 &ndash; L2.27</td>
        <td>Metric &amp; imperial conversions, compound units (speed, density), perimeter, circumference, composite 2D area, 3D surface area &amp; volume, scale drawings, bearings, angles, tax and wages (approx. 40% of marks).</td>
      </tr>
      <tr>
        <td><strong>3. Handling Information &amp; Data</strong></td>
        <td>L2.28 &ndash; L2.39</td>
        <td>Mean, median, mode, range, grouped frequency distributions, scatter graphs, correlation, line of best fit, two-way tables, pie charts, combined &amp; conditional probability, tree diagrams (approx. 35% of marks).</td>
      </tr>
    </table>

    <div class="grid-2col" style="margin-top:6px;">
      <div class="box-example">
        <h3 style="margin-top:0; color:#15803d;">Section A: Non-Calculator</h3>
        <p><strong>Duration:</strong> 25 minutes &bull; <strong>Marks:</strong> 16 marks<br>
        Tests mental arithmetic, fraction calculations, written long division/multiplication, estimation, and quick conceptual reasoning without electronic aids.</p>
      </div>
      <div class="box-example">
        <h3 style="margin-top:0; color:#15803d;">Section B: Calculator Allowed</h3>
        <p><strong>Duration:</strong> 1 hour 30 minutes &bull; <strong>Marks:</strong> 48 marks<br>
        Tests complex multi-step realistic workplace problem solving, compound interest, geometry, surface area, grouped averages, and statistical analysis.</p>
      </div>
    </div>

    <div class="box-formula" style="margin-top:6px;">
      <h3 style="margin-top:0; color:#1e40af;">British Dyslexia Association Visual Ergonomics</h3>
      <p>This manual is printed on soft warm cream background (<code>#FDFBF7</code>), eliminating harsh optical glare. Typographic layouts feature generous line-height (1.48), high-contrast headers, visual calculation frames, and zero full justification to eliminate dyslexia visual distortion.</p>
    </div>
    """
    pages.append(wrap_page(p2, 2, "Master Functional Skills &bull; Maths Level 2", "Curriculum Framework", "Maths Level 2 Core Study Guide"))

    # =========================================================================
    # STRAND 1: NUMBER & NUMBER SYSTEMS (PAGES 3 - 26)
    # =========================================================================

    # TOPIC 1: PAGE 3 (Theory) & PAGE 4 (Practice)
    p3 = """
    <h2>Place Value, Ordering &amp; Financial Balances</h2>
    <p>Mastering numbers up to 1,000,000 and working with positive and negative integers in workplace financial statements.</p>
    <div class="box-concept">
      <span class="tag-label tag-blue">Key Principle</span> <strong>Place Value Hierarchy:</strong>
      Every digit's position determines its true value. In <strong>3,408,520</strong>: The 3 is Millions ($3\\times 10^6$), 4 is Hundred Thousands ($400,000$), 0 is Ten Thousands ($0$), 8 is Thousands ($8,000$), 5 is Hundreds ($500$), 2 is Tens ($20$), and 0 is Units.
    </div>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1e40af;">Negative Numbers on the Number Line</h3>
      <p>Moving <strong>right</strong> increases value (addition, credits). Moving <strong>left</strong> decreases value (subtraction, debits).<br>
      <strong>Rules for signs:</strong> Adding a negative is subtraction ($5 + (-8) = 5 - 8 = -3$). Subtracting a negative is addition ($4 - (-6) = 4 + 6 = 10$). Multiplying/dividing like signs gives positive ($(-4) \\times (-3) = +12$); unlike signs gives negative ($(-15) \\div (+3) = -5$).</p>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Workplace Overdraft</span>
      <p>A logistics company bank account has a balance of <strong>-£1,450</strong>. During the day, the company receives a client credit of <strong>£3,200</strong>, pays a fuel bill of <strong>£850</strong>, and pays staff expenses of <strong>£1,120</strong>. What is the closing balance?</p>
      <div class="step-row"><span>Step 1: Start with overdraft balance</span><strong>-£1,450</strong></div>
      <div class="step-row"><span>Step 2: Add client payment: -1450 + 3200</span><strong>+£1,750</strong></div>
      <div class="step-row"><span>Step 3: Deduct fuel: 1750 - 850</span><strong>+£900</strong></div>
      <div class="step-row"><span>Step 4: Deduct expenses: 900 - 1120</span><strong>-£220</strong></div>
      <p style="margin:3px 0 0 0;"><strong>Final Account Status:</strong> The company is in overdraft by <strong>£220</strong> (Balance: -£220).</p>
    </div>
    <div class="box-trap">
      <span class="tag-label tag-red">Tutor Trap</span> <strong>Comparing Negative Numbers:</strong> Learners frequently think $-18$ is larger than $-5$ because $18 > 5$. On a thermometer or bank balance, $-18$ is much colder/deeper into debt than $-5$. Therefore, $-5 > -18$.
    </div>
    """
    pages.append(wrap_page(p3, 3, "Strand 1: Number & Number Systems", "Standards: L2.1, L2.2", "Maths Level 2 Core Study Guide"))

    p4_scaffold = """
    <div class="step-row"><span>Step 1: Identify start balance</span><span>Account is at <strong>-£380</strong></span></div>
    <div class="step-row"><span>Step 2: Add credits / earnings</span><span>$-380 + 950 = +£570$</span></div>
    <div class="step-row"><span>Step 3: Deduct all debits</span><span>$+570 - 720 = \\mathbf{-£150}$</span></div>
    """
    p4 = practice_page(
        "Place Value & Negative Balances", "Standards L2.1, L2.2", 4, p4_scaffold,
        "Order these values from coldest to warmest: $-12^\\circ\\text{C}, +3^\\circ\\text{C}, -4.5^\\circ\\text{C}, -0.5^\\circ\\text{C}, +1.8^\\circ\\text{C}, -15^\\circ\\text{C}$.",
        "A warehouse chiller is set at $+3^\\circ\\text{C}$. A fault causes the temperature to drop by $8.5^\\circ\\text{C}$. What is the new temperature? If the safety alarm triggers at $-5^\\circ\\text{C}$, does the alarm sound?",
        "A small business starts Monday with a bank balance of $-£640$. Over the week: sales revenue of $+£2,850$ is paid in, direct debits of $£1,420$ and $£980$ clear, and a supplier refund of $£195$ arrives. What is the Friday closing balance?"
    )
    pages.append(p4)

    # TOPIC 2: PAGE 5 (Theory) & PAGE 6 (Practice)
    p5 = """
    <h2>Written Multiplication &amp; Long Division (Non-Calc)</h2>
    <p>Section A strictly forbids calculators. You must demonstrate reliable, fast written algorithms for large multi-digit arithmetic and decimals.</p>
    <div class="grid-2col">
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8;">Long Multiplication: Column Method</h3>
        <p>Multiply each digit of the top number by the bottom digits, keeping track of place value zeroes.</p>
        <p><strong>Example: $348 \\times 26$</strong><br>
        1. $348 \\times 6 = 2,088$<br>
        2. Place holder zero, then $348 \\times 20 = 6,960$<br>
        3. Add: $2088 + 6960 = \\mathbf{9,048}$.</p>
      </div>
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8;">Short &amp; Long Division: Bus Stop</h3>
        <p>Divide digit by digit from left to right, carrying remainders into the next column.</p>
        <p><strong>Example: $1,638 \\div 7$</strong><br>
        1. $7$ into $1$ goes $0$, carry $1$<br>
        2. $7$ into $16$ goes $2$, remainder $2$<br>
        3. $7$ into $23$ goes $3$, remainder $2$<br>
        4. $7$ into $28$ goes $4$. Result: $\\mathbf{234}$.</p>
      </div>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Decimal Multiplication</span>
      <p>A workshop technician cuts 15 copper pipes, each measuring $1.35\\text{ metres}$. What is the total length?</p>
      <div class="step-row"><span>Step 1: Remove decimals and multiply whole numbers</span><strong>135 × 15</strong></div>
      <div class="step-row"><span>Step 2: 135 × 5 = 675; 135 × 10 = 1350</span><strong>675 + 1350 = 2025</strong></div>
      <div class="step-row"><span>Step 3: Reinsert 2 decimal places from 1.35</span><strong>20.25 metres</strong></div>
    </div>
    <div class="box-trap">
      <span class="tag-label tag-red">Tutor Trap</span> <strong>Forgetting the Place Holder Zero:</strong> In two-digit multiplication, multiplying by the tens column without adding a trailing zero leads to an answer off by a factor of 10. Always write the zero first!
    </div>
    """
    pages.append(wrap_page(p5, 5, "Strand 1: Number & Number Systems", "Standards: L2.3, L2.4", "Maths Level 2 Core Study Guide"))

    p6_scaffold = """
    <div class="step-row"><span>Step 1: Set up column multiplication</span><span>$426 \\times 34$</span></div>
    <div class="step-row"><span>Step 2: Units row ($426 \\times 4$)</span><span>$1,704$</span></div>
    <div class="step-row"><span>Step 3: Tens row ($426 \\times 30$, zero placed)</span><span>$12,780$</span></div>
    <div class="step-row"><span>Step 4: Sum columns</span><span>$1,704 + 12,780 = \\mathbf{14,484}$</span></div>
    """
    p6 = practice_page(
        "Written Multiplication & Division", "Standards L2.3, L2.4", 6, p6_scaffold,
        "Calculate without a calculator: a) $528 \\times 37$ &emsp; b) $2,184 \\div 6$.",
        "A catering manager purchases 45 packs of premium napkins at $£3.25$ per pack. How much do the napkins cost in total?",
        "An engineering apprentice has a $4.8\\text{ m}$ steel rod. She needs to cut as many $0.35\\text{ m}$ pins as possible. How many complete pins can she cut, and what length of steel rod remains unused in centimetres?"
    )
    pages.append(p6)

    # TOPIC 3: PAGE 7 (Theory) & PAGE 8 (Practice)
    p7 = """
    <h2>Fractions: Equivalences, Arithmetic &amp; Mixed Numbers</h2>
    <p>Fractions represent parts of quantities, ratios of ingredients, and job completion metrics across industry.</p>
    <div class="grid-2col">
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8;">Addition &amp; Subtraction</h3>
        <p>1. Convert mixed numbers to improper fractions.<br>
        2. Find the lowest common denominator (LCM).<br>
        3. Add or subtract <em>only</em> numerators: $\\frac{a}{d} \\pm \\frac{b}{d} = \\frac{a \\pm b}{d}$.</p>
      </div>
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8;">Multiplication &amp; Division</h3>
        <p><strong>Multiply:</strong> $\\frac{a}{b} \\times \\frac{c}{d} = \\frac{a \\times c}{b \\times d}$.<br>
        <strong>Divide (Keep-Flip-Change):</strong><br>
        Keep 1st fraction, flip 2nd (reciprocal), change &divide; to &times;:<br>
        $\\frac{a}{b} \\div \\frac{c}{d} = \\frac{a}{b} \\times \\frac{d}{c}$.</p>
      </div>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Mixed Number Calculation</span>
      <p>A joiner joins two timber battens measuring $2\\frac{3}{4}\\text{ m}$ and $1\\frac{2}{3}\\text{ m}$. What is the total length?</p>
      <div class="step-row"><span>Step 1: Convert to improper fractions</span><strong>11/4 + 5/3</strong></div>
      <div class="step-row"><span>Step 2: Common denominator is 12: 11/4 = 33/12, 5/3 = 20/12</span><strong>33/12 + 20/12</strong></div>
      <div class="step-row"><span>Step 3: Add numerators</span><strong>53/12</strong></div>
      <div class="step-row"><span>Step 4: Convert back to mixed number: 53 ÷ 12 = 4 r 5</span><strong>4 5/12 metres</strong></div>
    </div>
    <div class="box-trap">
      <span class="tag-label tag-red">Tutor Trap</span> <strong>Adding Denominators:</strong> Never write $\\frac{1}{3} + \\frac{1}{2} = \\frac{2}{5}$! Fractions cannot be combined until denominators are made identical through equivalent scaling.
    </div>
    """
    pages.append(wrap_page(p7, 7, "Strand 1: Number & Number Systems", "Standards: L2.5, L2.6", "Maths Level 2 Core Study Guide"))

    p8_scaffold = """
    <div class="step-row"><span>Step 1: Division problem</span><span>$3\\frac{1}{2} \\div \\frac{1}{4}$</span></div>
    <div class="step-row"><span>Step 2: Improper conversion</span><span>$\\frac{7}{2} \\div \\frac{1}{4}$</span></div>
    <div class="step-row"><span>Step 3: Keep-Flip-Change</span><span>$\\frac{7}{2} \\times \\frac{4}{1} = \\frac{28}{2} = \\mathbf{14}$ portions</span></div>
    """
    p8 = practice_page(
        "Fractions Operations & Mixed Numbers", "Standards L2.5, L2.6", 8, p8_scaffold,
        "Evaluate giving your answers in simplest form: a) $\\frac{5}{8} + \\frac{1}{6}$ &emsp; b) $2\\frac{2}{3} \\times \\frac{3}{4}$.",
        "A chef has $4\\frac{1}{2}\\text{ kg}$ of prime beef mince. Each burger patty requires $\\frac{3}{16}\\text{ kg}$ of mince. How many complete burger patties can the chef make?",
        "In a manufacturing plant, $\\frac{3}{5}$ of workers are on day shift, $\\frac{1}{4}$ are on late shift, and the remaining 45 workers are on night shift. How many total workers are employed at the plant?"
    )
    pages.append(p8)

    # TOPIC 4: PAGE 9 (Theory) & PAGE 10 (Practice)
    p9 = """
    <h2>Decimals &amp; Workplace Financial Statements</h2>
    <p>Financial numeracy requires precise decimal calculations, handling money to 2 decimal places, and checking invoices.</p>
    <div class="box-concept">
      <span class="tag-label tag-blue">Key Principle</span> <strong>Financial Precision:</strong>
      Currency in pounds sterling must always be quoted to <strong>two decimal places</strong> (e.g. write $£14.50$, never $£14.5$). Intermediate calculations should keep full precision until the final answer.
    </div>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1e40af;">Ordering Decimals &amp; Place Value Alignment</h3>
      <p>To compare decimals like $0.4$, $0.375$, and $0.42$, add trailing zeroes so all numbers have equal decimal digits:<br>
      $0.400 < 0.420$ and $0.375 < 0.400$. Therefore: $0.375 < 0.4 < 0.42$.</p>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Itemised Trades Invoice</span>
      <p>A plumber issues an invoice: 4.5 hours labour at $£38.00/\\text{hr}$, parts costing $£145.60$, and a call-out fee of $£45.00$. VAT is charged at $20\\%$. What is the total invoice?</p>
      <div class="step-row"><span>Step 1: Labour cost: 4.5 × 38.00</span><strong>£171.00</strong></div>
      <div class="step-row"><span>Step 2: Subtotal before VAT: 171.00 + 145.60 + 45.00</span><strong>£361.60</strong></div>
      <div class="step-row"><span>Step 3: VAT at 20%: 0.20 × 361.60</span><strong>£72.32</strong></div>
      <div class="step-row"><span>Step 4: Grand total: 361.60 + 72.32</span><strong>£433.92</strong></div>
    </div>
    <div class="box-trap">
      <span class="tag-label tag-red">Tutor Trap</span> <strong>Truncating vs Rounding Money:</strong> Rounding $£12.456$ to $£12.45$ loses a penny. Always look at the third decimal place ($6 \\ge 5$) so it rounds up to $£12.46$.
    </div>
    """
    pages.append(wrap_page(p9, 9, "Strand 1: Number & Number Systems", "Standards: L2.7, L2.8", "Maths Level 2 Core Study Guide"))

    p10_scaffold = """
    <div class="step-row"><span>Step 1: Multiply unit rate by quantity</span><span>$18.5 \\times £14.20 = £262.70$</span></div>
    <div class="step-row"><span>Step 2: Add fixed delivery</span><span>$£262.70 + £35.00 = £297.70$</span></div>
    <div class="step-row"><span>Step 3: Apply 5% trade discount</span><span>$£297.70 \\times 0.95 = \\mathbf{£282.82}$</span></div>
    """
    p10 = practice_page(
        "Decimals & Financial Statements", "Standards L2.7, L2.8", 10, p10_scaffold,
        "Evaluate without a calculator: a) $4.85 \\times 100$ &emsp; b) $73.6 \\div 1000$ &emsp; c) $14.6 - 8.79$.",
        "A dental receptionist checks three utility payments: electricity $£184.25$, gas $£112.80$, and water $£46.45$. If the practice had budgeted $£350.00$, by how much did they overspend or underspend?",
        "An electrician quotes a client: 6 light fittings at $£24.50$ each, $45\\text{ m}$ cable at $£1.20/\\text{m}$, and 3.5 hours labour at $£35/\\text{hr}$. The electrician offers a $10\\%$ prompt-payment discount on the total before VAT, and then adds $20\\%$ VAT. Calculate the final bill."
    )
    pages.append(p10)

    # TOPIC 5: PAGE 11 (Theory) & PAGE 12 (Practice)
    p11 = """
    <h2>Percentages &amp; Single Decimal Multipliers</h2>
    <p>Using single decimal multipliers to calculate percentages, percentage increases, and percentage decreases quickly.</p>
    <div class="box-concept">
      <span class="tag-label tag-blue">Key Principle</span> <strong>The Multiplier Rule:</strong>
      A percentage is a fraction out of 100 ($P\\% = \\frac{P}{100}$). To find a percentage of an amount, multiply by its decimal equivalent.
    </div>
    <table class="cgp-table">
      <tr>
        <th>Operation</th>
        <th>Percentage</th>
        <th>Decimal Multiplier</th>
        <th>Example on £400</th>
      </tr>
      <tr><td>Find Amount</td><td>$17.5\\%$</td><td>$\\times 0.175$</td><td>$400 \\times 0.175 = £70.00$</td></tr>
      <tr><td>Percentage Increase</td><td>Increase by $15\\%$</td><td>$\\times (1 + 0.15) = \\mathbf{1.15}$</td><td>$400 \\times 1.15 = £460.00$</td></tr>
      <tr><td>Percentage Decrease</td><td>Decrease by $25\\%$</td><td>$\\times (1 - 0.25) = \\mathbf{0.75}$</td><td>$400 \\times 0.75 = £300.00$</td></tr>
      <tr><td>VAT Addition</td><td>Add $20\\%$ VAT</td><td>$\\times \\mathbf{1.20}$</td><td>$400 \\times 1.20 = £480.00$</td></tr>
    </table>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Salary Increase</span>
      <p>An NHS nurse earns an annual salary of $£28,400$. She receives a $3.5\\%$ cost-of-living pay award. Calculate her new salary.</p>
      <div class="step-row"><span>Step 1: Identify the increase multiplier: 1 + 0.035</span><strong>1.035</strong></div>
      <div class="step-row"><span>Step 2: Multiply base salary: 28,400 × 1.035</span><strong>£29,394</strong></div>
    </div>
    <div class="box-trap">
      <span class="tag-label tag-red">Tutor Trap</span> <strong>Small Percentage Multipliers:</strong> Learners often write $3.5\\%$ as $0.35$ instead of $0.035$. Remember $0.35 = 35\\%$. Always divide by 100!
    </div>
    """
    pages.append(wrap_page(p11, 11, "Strand 1: Number & Number Systems", "Standards: L2.9, L2.10", "Maths Level 2 Core Study Guide"))

    p12_scaffold = """
    <div class="step-row"><span>Step 1: Convert 4.2% increase to multiplier</span><span>$1 + 0.042 = 1.042$</span></div>
    <div class="step-row"><span>Step 2: Multiply initial value</span><span>$£540 \\times 1.042 = \\mathbf{£562.68}$</span></div>
    """
    p12 = practice_page(
        "Percentages & Multipliers", "Standards L2.9, L2.10", 12, p12_scaffold,
        "Write the single decimal multiplier for: a) Finding $6.5\\%$ &emsp; b) Increasing by $12\\%$ &emsp; c) Decreasing by $35\\%$ &emsp; d) Decreasing by $4\\%$.",
        "A car insurance premium of $£620.00$ increases by $8.5\\%$ at renewal. What is the new renewal price?",
        "A distribution depot ships 14,500 parcels in November. In December, parcel volume increases by $28\\%$. In January, volume drops by $15\\%$ compared to December. How many parcels are shipped in January?"
    )
    pages.append(p12)

    # TOPIC 6: PAGE 13 (Theory) & PAGE 14 (Practice)
    p13 = """
    <h2>Reverse Percentages &amp; Percentage Change</h2>
    <p>Finding original values before discounts or tax was added, and calculating percentage growth or loss.</p>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1d4ed8;">Statutory Reverse Percentage Formula</h3>
      <p>$$\\text{Original Amount} = \\frac{\\text{New Amount}}{\\text{Multiplier}}$$</p>
      <p>If an amount has increased by $X\\%$, divide by $(1 + \\frac{X}{100})$. If decreased by $X\\%$, divide by $(1 - \\frac{X}{100})$.</p>
    </div>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1d4ed8;">Percentage Change Formula</h3>
      <p>$$\\text{Percentage Change} = \\frac{\\text{Actual Difference (Change)}}{\\text{Original Value}} \\times 100$$</p>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Finding Original Price Before Sale</span>
      <p>A laptop is on sale for <strong>£480.00</strong> after a <strong>20% discount</strong>. What was the original full price?</p>
      <div class="step-row"><span>Step 1: Understand percentage: £480 represents 80%</span><strong>100% - 20% = 80%</strong></div>
      <div class="step-row"><span>Step 2: Multiplier is 0.80</span><strong>0.80</strong></div>
      <div class="step-row"><span>Step 3: Divide sale price by multiplier: 480 ÷ 0.80</span><strong>£600.00</strong></div>
    </div>
    <div class="box-trap">
      <span class="tag-label tag-red">Tutor Trap</span> <strong>The 20% Add-On Error:</strong> Finding $20\\%$ of $£480$ ($£96$) and adding it to get $£576$ is completely wrong! $20\\%$ of $£600$ is $£120$, leaving $£480$. Always divide by the multiplier.
    </div>
    """
    pages.append(wrap_page(p13, 13, "Strand 1: Number & Number Systems", "Standards: L2.9, L2.10", "Maths Level 2 Core Study Guide"))

    p14_scaffold = """
    <div class="step-row"><span>Step 1: Total price £216 includes 20% VAT</span><span>Multiplier is $1.20$</span></div>
    <div class="step-row"><span>Step 2: Divide by multiplier to find pre-VAT cost</span><span>$216 \\div 1.20 = £180.00$</span></div>
    <div class="step-row"><span>Step 3: Subtract to isolate VAT element</span><span>$216 - 180 = \\mathbf{£36.00}$ VAT</span></div>
    """
    p14 = practice_page(
        "Reverse Percentages & Change", "Standards L2.9, L2.10", 14, p14_scaffold,
        "A power drill sells for $£84.00$ including $20\\%$ VAT. Calculate the price before VAT was added.",
        "A bakery sold 450 loaves on Friday and 558 loaves on Saturday. Calculate the percentage increase in sales.",
        "A fitness coach bought commercial gym equipment for $£3,200$. Three years later, he sells it for $£1,840$. Calculate the percentage loss in value. If a new model is currently advertised at $£2,760$ after a $15\\%$ discount, what was its original price?"
    )
    pages.append(p14)

    # TOPIC 7: PAGE 15 (Theory) & PAGE 16 (Practice)
    p15 = """
    <h2>Ratio Division, Direct Proportion &amp; Unit Rates</h2>
    <p>Sharing quantities into unequal parts, scaling recipe mixtures, and comparing unit costs to determine best buys.</p>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1d4ed8;">The 3-Step Ratio Method</h3>
      <p>To divide total $T$ into ratio $a : b : c$:<br>
      <strong>Step 1 (Add parts):</strong> Total Parts $= a + b + c$<br>
      <strong>Step 2 (One part):</strong> Value of $1\\text{ part} = \\frac{T}{\\text{Total Parts}}$<br>
      <strong>Step 3 (Multiply):</strong> Multiply $1\\text{ part}$ by each ratio share.</p>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Sharing Inheritance or Profit</span>
      <p>Three business partners share annual profit of <strong>£84,000</strong> in the ratio <strong>4 : 2 : 1</strong>. How much does each partner receive?</p>
      <div class="step-row"><span>Step 1: Total parts: 4 + 2 + 1</span><strong>7 parts</strong></div>
      <div class="step-row"><span>Step 2: Value of 1 part: £84,000 ÷ 7</span><strong>£12,000</strong></div>
      <div class="step-row"><span>Step 3: Partner A (4 parts): 4 × £12,000</span><strong>£48,000</strong></div>
      <div class="step-row"><span>Step 4: Partner B (2 parts): 2 × £12,000</span><strong>£24,000</strong></div>
      <div class="step-row"><span>Step 5: Partner C (1 part): 1 × £12,000</span><strong>£12,000</strong></div>
    </div>
    <div class="box-trap">
      <span class="tag-label tag-red">Tutor Trap</span> <strong>Total vs Part Given:</strong> Check whether the question gives the <em>total</em> amount or just <em>one person's share</em>. If Partner C got $£12,000$, do not divide $£12,000$ by 7!
    </div>
    """
    pages.append(wrap_page(p15, 15, "Strand 1: Number & Number Systems", "Standards: L2.11", "Maths Level 2 Core Study Guide"))

    p16_scaffold = """
    <div class="step-row"><span>Step 1: Calculate unit price for Brand A</span><span>$£3.60 \\div 800\\text{ g} = £0.0045/\\text{g}$ ($£4.50/\\text{kg}$)</span></div>
    <div class="step-row"><span>Step 2: Calculate unit price for Brand B</span><span>$£5.20 \\div 1200\\text{ g} = £0.00433/\\text{g}$ ($£4.33/\\text{kg}$)</span></div>
    <div class="step-row"><span>Step 3: Compare unit rates</span><span>Brand B is cheaper per gram by $£0.17/\\text{kg}$</span></div>
    """
    p16 = practice_page(
        "Ratio Division & Best Buys", "Standards L2.11", 16, p16_scaffold,
        "Share $£4,500$ in the ratio $5 : 3 : 1$.",
        "A mortar mix uses cement, sand, and gravel in the ratio $1 : 2 : 4$. A builder needs $1.4\\text{ tonnes}$ of mortar. How many kilograms of sand does he require?",
        "Supermarket A sells a $750\\text{ g}$ box of cereal for $£2.85$. Supermarket B sells a $1.2\\text{ kg}$ family pack for $£4.32$. Which pack offers better value for money? Justify your decision with full unit calculations."
    )
    pages.append(p16)

    # TOPIC 8: PAGE 17 (Theory) & PAGE 18 (Practice)
    p17 = """
    <h2>Inverse Proportion &amp; Rates of Work</h2>
    <p>In direct proportion, when one variable increases, the other increases. In inverse proportion, when one increases, the other decreases proportionally.</p>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1d4ed8;">The Constant Product Rule</h3>
      <p>$$\\text{Workers} \\times \\text{Time} = \\text{Total Work (Man-Hours)}$$</p>
      <p>If $W_1 \\times T_1 = k$, then $W_2 \\times T_2 = k$. Therefore: $T_2 = \\frac{W_1 \\times T_1}{W_2}$.</p>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Construction Deadline</span>
      <p>It takes <strong>6 bricklayers 12 days</strong> to build an extension. How many days would it take <strong>9 bricklayers</strong> working at the same pace?</p>
      <div class="step-row"><span>Step 1: Calculate total man-days needed: 6 × 12</span><strong>72 man-days</strong></div>
      <div class="step-row"><span>Step 2: Divide total man-days by 9 bricklayers: 72 ÷ 9</span><strong>8 days</strong></div>
      <p style="margin:3px 0 0 0;"><strong>Result:</strong> 9 bricklayers complete the project in <strong>8 days</strong> (faster, as expected!).</p>
    </div>
    <div class="box-trap">
      <span class="tag-label tag-red">Tutor Trap</span> <strong>Using Cross-Multiplication for Inverse:</strong> Cross-multiplying gives $\\frac{6}{12} = \\frac{9}{x} \\Rightarrow x = 18$ days, which would mean more workers take longer! Always use the constant product rule.
    </div>
    """
    pages.append(wrap_page(p17, 17, "Strand 1: Number & Number Systems", "Standards: L2.11", "Maths Level 2 Core Study Guide"))

    p18_scaffold = """
    <div class="step-row"><span>Step 1: Total person-hours</span><span>$4 \\text{ painters} \\times 18\\text{ hours} = 72\\text{ person-hours}$</span></div>
    <div class="step-row"><span>Step 2: Divide by available time (12 hours)</span><span>$72 \\div 12 = 6\\text{ painters}$</span></div>
    <div class="step-row"><span>Step 3: Calculate additional painters needed</span><span>$6 - 4 = \\mathbf{2\\text{ extra painters}}$</span></div>
    """
    p18 = practice_page(
        "Inverse Proportion & Rates of Work", "Standards L2.11", 18, p18_scaffold,
        "It takes 5 cleaners 4 hours to clean an office floor. How long would it take 8 cleaners working at the exact same rate?",
        "A pipe delivers $45\\text{ litres/minute}$ and fills a water storage tank in 80 minutes. How long would it take to fill the tank if the flow rate was reduced to $30\\text{ litres/minute}$?",
        "A groundworks contractor estimates that 3 excavators can clear a development site in 16 working days. The client requests the work be completed in 6 working days. How many additional excavators must the contractor hire?"
    )
    pages.append(p18)

    # TOPIC 9: PAGE 19 (Theory) & PAGE 20 (Practice)
    p19 = """
    <h2>Compound Interest, Depreciation &amp; Repeated Growth</h2>
    <p>Compound interest adds interest to the principal at each cycle, generating interest on interest. Depreciation reduces value exponentially.</p>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1d4ed8;">Statutory Compound Growth Formula</h3>
      <p>$$\\text{Final Value} = P \\times (1 \\pm r)^n$$</p>
      <p>Where $P = \\text{Principal}$, $r = \\text{interest or depreciation rate as a decimal}$, and $n = \\text{number of periods}$.</p>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: 3-Year Fixed Savings Account</span>
      <p>A saver deposits <strong>£5,000</strong> in a bond paying <strong>4% compound interest per annum</strong> for 3 years. Calculate the final balance and total interest earned.</p>
      <div class="step-row"><span>Step 1: Multiplier for 4% increase: 1 + 0.04</span><strong>1.04</strong></div>
      <div class="step-row"><span>Step 2: Formula calculation: 5000 × (1.04)³</span><strong>5000 × 1.124864 = £5,624.32</strong></div>
      <div class="step-row"><span>Step 3: Total interest earned: £5,624.32 - £5,000</span><strong>£624.32</strong></div>
    </div>
    <div class="box-trap">
      <span class="tag-label tag-red">Tutor Trap</span> <strong>Simple Interest Confusion:</strong> Simple interest would be $5000 \\times 0.04 \\times 3 = £600$. Compound interest earns an additional $£24.32$ because interest earned in Year 1 and Year 2 earns further interest!
    </div>
    """
    pages.append(wrap_page(p19, 19, "Strand 1: Number & Number Systems", "Standards: L2.10", "Maths Level 2 Core Study Guide"))

    p20_scaffold = """
    <div class="step-row"><span>Step 1: Depreciation multiplier (15% loss)</span><span>$1 - 0.15 = 0.85$</span></div>
    <div class="step-row"><span>Step 2: Apply over 2 years</span><span>$£16,000 \\times (0.85)^2$</span></div>
    <div class="step-row"><span>Step 3: Calculate value</span><span>$16000 \\times 0.7225 = \\mathbf{£11,560}$</span></div>
    """
    p20 = practice_page(
        "Compound Interest & Depreciation", "Standards L2.10", 20, p20_scaffold,
        "Calculate the value of $£2,400$ invested for 2 years at $3\\%$ compound interest per annum.",
        "A commercial delivery van was purchased brand new for $£28,000$. It depreciates at a rate of $18\\%$ per year. What is its estimated book value after 3 years?",
        "An investor has $£10,000$ to invest for 3 years. Bank A offers $4.5\\%$ simple interest per year. Bank B offers $4.2\\%$ compound interest per annum. Which bank will yield more total interest at the end of 3 years, and by how much?"
    )
    pages.append(p20)

    # TOPIC 10: PAGE 21 (Theory) & PAGE 22 (Practice)
    p21 = """
    <h2>Estimation, Rounding, Bounds &amp; BIDMAS Formulae</h2>
    <p>Using estimation to verify calculator answers, determining upper and lower bounds, and adhering to strict algebraic order of operations.</p>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1d4ed8;">BIDMAS Rule &amp; 1 Significant Figure Estimation</h3>
      <p><strong>B</strong>rackets &rarr; <strong>I</strong>ndices &rarr; <strong>D</strong>ivision &amp; <strong>M</strong>ultiplication &rarr; <strong>A</strong>ddition &amp; <strong>S</strong>ubtraction.<br>
      To estimate: round every number to <strong>1 significant figure (1 s.f.)</strong> before calculating.</p>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Estimation Check</span>
      <p>Estimate the value of: $\\frac{49.8 \\times 19.3}{0.52}$.</p>
      <div class="step-row"><span>Step 1: Round 49.8 to 1 s.f.</span><strong>50</strong></div>
      <div class="step-row"><span>Step 2: Round 19.3 to 1 s.f.</span><strong>20</strong></div>
      <div class="step-row"><span>Step 3: Round 0.52 to 1 s.f.</span><strong>0.5</strong></div>
      <div class="step-row"><span>Step 4: Compute: (50 × 20) ÷ 0.5 = 1000 ÷ 0.5</span><strong>2,000</strong></div>
    </div>
    <div class="box-concept">
      <span class="tag-label tag-blue">Upper &amp; Lower Bounds</span>
      If a length is given as $45\\text{ cm}$ rounded to the nearest centimetre: the degree of accuracy is $1\\text{ cm}$. Half the unit is $0.5\\text{ cm}$.<br>
      <strong>Lower Bound (LB):</strong> $45 - 0.5 = \\mathbf{44.5\\text{ cm}}$. <strong>Upper Bound (UB):</strong> $45 + 0.5 = \\mathbf{45.5\\text{ cm}}$.
    </div>
    """
    pages.append(wrap_page(p21, 21, "Strand 1: Number & Number Systems", "Standards: L2.12, L2.13", "Maths Level 2 Core Study Guide"))

    p22_scaffold = """
    <div class="step-row"><span>Step 1: Round each number to 1 s.f.</span><span>$28.4 \\approx 30$; $6.12 \\approx 6$; $0.21 \\approx 0.2$</span></div>
    <div class="step-row"><span>Step 2: Numerator: $30 \\times 6 = 180$</span><span>$180 \\div 0.2$</span></div>
    <div class="step-row"><span>Step 3: Divide by 0.2 (multiply by 5)</span><span>$180 \\times 5 = \\mathbf{900}$</span></div>
    """
    p22 = practice_page(
        "Estimation, Bounds & BIDMAS", "Standards L2.12, L2.13", 22, p22_scaffold,
        "Evaluate: a) $15 - 3 \\times 4 + 2$ &emsp; b) $(8 + 4) \\div (7 - 3) + 3^2$.",
        "A warehouse manager orders 195 heavy-duty crates at $£48.75$ each. Use 1 significant figure estimation to show an approximate total cost, and explain whether the estimate is an overestimate or underestimate.",
        "A parcel courier measures a box as $60\\text{ cm}$ by $40\\text{ cm}$ by $30\\text{ cm}$, each rounded to the nearest $10\\text{ cm}$. Calculate the maximum possible volume (upper bound) and minimum possible volume (lower bound) of the box in cubic centimetres."
    )
    pages.append(p22)

    # CHECKPOINT 1: PAGES 23 TO 26 (4-page Review Assessment)
    chk1_p1 = [
        (1, 2, "Calculate without using a calculator: $416 \\times 28$. Show your full column method.", 75),
        (2, 2, "A freezer compartment is at $-14^\\circ\\text{C}$. The thermostat is adjusted so the temperature rises by $6.5^\\circ\\text{C}$, then drops by $3.2^\\circ\\text{C}$. What is the new temperature?", 65),
        (3, 2, "Evaluate giving your answer as a mixed number in simplest form: $1\\frac{3}{5} + 2\\frac{1}{4}$.", 70)
    ]
    pages.append(checkpoint_page("Strand 1: Number & Number Systems", "Part 1 &bull; Non-Calculator (Q1-Q3)", 23, "6 Marks", chk1_p1))

    chk1_p2 = [
        (4, 2, "Work out: $3,744 \\div 13$. Show your full written division method.", 75),
        (5, 2, "A tradesperson quotes $£420.00$ excluding VAT. VAT is charged at $20\\%$. How much is the total quote with VAT included?", 65),
        (6, 2, "Share $£1,260$ between three apprentices in the ratio $3 : 2 : 1$. How much does the apprentice with the smallest share receive?", 70)
    ]
    pages.append(checkpoint_page("Strand 1: Number & Number Systems", "Part 1 &bull; Non-Calculator (Q4-Q6)", 24, "6 Marks", chk1_p2))

    chk1_p3 = [
        (7, 3, "A sports retailer sells running shoes for $£68.00$ after a $15\\%$ discount. Calculate the original full price before the discount was applied.", 80),
        (8, 3, "A company deposits $£15,000$ in a business growth account offering $3.8\\%$ compound interest per year for 3 years. Calculate the total balance in the account at the end of the 3 years.", 80),
        (9, 3, "It takes 4 assembly technicians 15 hours to assemble a batch of medical ventilators. The hospital requests the batch in 10 hours. How many technicians in total are required?", 80)
    ]
    pages.append(checkpoint_page("Strand 1: Number & Number Systems", "Part 2 &bull; Calculator Allowed (Q7-Q9)", 25, "9 Marks", chk1_p3))

    chk1_p4 = [
        (10, 3, "A concrete mix requires sand, ballast, and cement in the ratio $5 : 3 : 2$. A builder prepares $3.6\\text{ tonnes}$ of mix. He has $1.7\\text{ tonnes}$ of sand in stock. Does he have enough sand? Show full working.", 80),
        (11, 3, "A logistics manager bought an electric delivery van for $£32,000$. It depreciates by $16\\%$ in the first year and $12\\%$ in the second year. What is the value of the van at the end of year 2?", 80),
        (12, 3, "An office manager checks an invoice: 12 desks at $£145.50$ each, 24 chairs at $£68.00$ each. A delivery charge of $£45.00$ is added. A bulk discount of $7.5\\%$ is deducted from the total before adding $20\\%$ VAT. What is the final invoice total?", 80)
    ]
    pages.append(checkpoint_page("Strand 1: Number & Number Systems", "Part 2 &bull; Calculator Allowed (Q10-Q12)", 26, "9 Marks", chk1_p4))

    # =========================================================================
    # STRAND 2: MEASURES, SHAPE & SPACE (PAGES 27 - 50)
    # =========================================================================

    # TOPIC 11: PAGE 27 (Theory) & PAGE 28 (Practice)
    p27 = """
    <h2>Metric &amp; Imperial Unit Conversions</h2>
    <p>Modern workplaces require converting between metric units and converting between metric and imperial measures.</p>
    <div class="grid-2col">
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8;">Metric Conversions</h3>
        <p><strong>Length:</strong> $1\\text{ m} = 100\\text{ cm} = 1000\\text{ mm}$; $1\\text{ km} = 1000\\text{ m}$.<br>
        <strong>Mass:</strong> $1\\text{ kg} = 1000\\text{ g}$; $1\\text{ tonne} = 1000\\text{ kg}$.<br>
        <strong>Capacity:</strong> $1\\text{ litre} = 1000\\text{ ml} = 1000\\text{ cm}^3$.</p>
      </div>
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8;">Key Statutory Imperial Approximations</h3>
        <p>&bull; $1\\text{ inch} \\approx 2.54\\text{ cm}$ (or $2.5\\text{ cm}$)<br>
        &bull; $1\\text{ foot} = 12\\text{ inches} \\approx 30\\text{ cm}$<br>
        &bull; $1\\text{ kg} \\approx 2.2\\text{ pounds (lbs)}$<br>
        &bull; $1\\text{ gallon} \\approx 4.5\\text{ litres}$<br>
        &bull; $5\\text{ miles} \\approx 8\\text{ km}$ ($1\\text{ mile} \\approx 1.6\\text{ km}$)</p>
      </div>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Fuel Consumption</span>
      <p>A UK driver fills her tank with <strong>54 litres of petrol</strong>. How many gallons is this? ($1\\text{ gal} \\approx 4.5\\text{ L}$)</p>
      <div class="step-row"><span>Step 1: Set up division: litres ÷ 4.5</span><strong>54 ÷ 4.5</strong></div>
      <div class="step-row"><span>Step 2: Equivalent integer division: 540 ÷ 45</span><strong>12 gallons</strong></div>
    </div>
    <div class="box-trap">
      <span class="tag-label tag-red">Tutor Trap</span> <strong>Area and Volume Unit Conversions:</strong> $1\\text{ m}^2 \\ne 100\\text{ cm}^2$! Since $1\\text{ m} = 100\\text{ cm}$, $1\\text{ m}^2 = 100 \\times 100 = 10,000\\text{ cm}^2$. Similarly, $1\\text{ m}^3 = 1,000,000\\text{ cm}^3$.
    </div>
    """
    pages.append(wrap_page(p27, 27, "Strand 2: Measures, Shape & Space", "Standards: L2.14, L2.15", "Maths Level 2 Core Study Guide"))

    p28_scaffold = """
    <div class="step-row"><span>Step 1: Miles to km conversion factor</span><span>$5\\text{ miles} \\approx 8\\text{ km}$ ($1\\text{ mile} \\approx 1.6\\text{ km}$)</span></div>
    <div class="step-row"><span>Step 2: Multiply 45 miles by 1.6</span><span>$45 \\times 1.6 = \\mathbf{72\\text{ km}}$</span></div>
    """
    p28 = practice_page(
        "Unit Conversions", "Standards L2.14, L2.15", 28, p28_scaffold,
        "Convert: a) $3.45\\text{ kg}$ into grams &emsp; b) $750\\text{ ml}$ into litres &emsp; c) $140\\text{ miles}$ into kilometres using $5\\text{ miles} = 8\\text{ km}$.",
        "A patient in hospital is prescribed liquid medication: $15\\text{ ml}$ three times per day for 14 days. Will a $500\\text{ ml}$ bottle be sufficient? Show full working.",
        "A UK haulage truck carries $14\\text{ tonnes}$ of gravel. The European delivery limit is $31,000\\text{ lbs}$. Use $1\\text{ kg} = 2.2\\text{ lbs}$ to determine if the truck is within legal weight limits."
    )
    pages.append(p28)

    # TOPIC 12: PAGE 29 (Theory) & PAGE 30 (Practice)
    p29 = """
    <h2>Compound Measures: Speed, Density &amp; Pressure</h2>
    <p>Compound measures combine two different fundamental units of measurement through division or multiplication.</p>
    <div class="grid-3col">
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8; font-size:8.2pt;">Speed</h3>
        <p>$$\\text{Speed} = \\frac{\\text{Distance}}{\\text{Time}}$$</p>
        <p>Distance $= S \\times T$<br>Time $= \\frac{D}{S}$</p>
      </div>
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8; font-size:8.2pt;">Density</h3>
        <p>$$\\text{Density} = \\frac{\\text{Mass}}{\\text{Volume}}$$</p>
        <p>Mass $= D \\times V$<br>Volume $= \\frac{M}{D}$</p>
      </div>
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8; font-size:8.2pt;">Pressure</h3>
        <p>$$\\text{Pressure} = \\frac{\\text{Force}}{\\text{Area}}$$</p>
        <p>Force $= P \\times A$<br>Area $= \\frac{F}{P}$</p>
      </div>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Average Speed with Minutes</span>
      <p>A courier drives <strong>84 miles</strong> in <strong>1 hour and 45 minutes</strong>. What is her average speed in mph?</p>
      <div class="step-row"><span>Step 1: Convert 45 minutes to decimal hours: 45 ÷ 60</span><strong>0.75 hours</strong></div>
      <div class="step-row"><span>Step 2: Total time in decimal hours</span><strong>1.75 hours</strong></div>
      <div class="step-row"><span>Step 3: Speed = Distance ÷ Time = 84 ÷ 1.75</span><strong>48 mph</strong></div>
    </div>
    <div class="box-trap">
      <span class="tag-label tag-red">Tutor Trap</span> <strong>The Decimal Time Trap:</strong> Never write 1 hour 45 minutes as $1.45\\text{ hours}$! There are 60 minutes in an hour, so $45\\text{ mins} = \\frac{45}{60} = 0.75\\text{ hours}$. $1.45$ hours would only be 1 hour 27 minutes.
    </div>
    """
    pages.append(wrap_page(p29, 29, "Strand 2: Measures, Shape & Space", "Standards: L2.16, L2.26", "Maths Level 2 Core Study Guide"))

    p30_scaffold = """
    <div class="step-row"><span>Step 1: Convert 24 minutes to decimal hours</span><span>$24 \\div 60 = 0.4\\text{ hours}$</span></div>
    <div class="step-row"><span>Step 2: Total time</span><span>$2 + 0.4 = 2.4\\text{ hours}$</span></div>
    <div class="step-row"><span>Step 3: Distance = Speed × Time</span><span>$55\\text{ mph} \\times 2.4\\text{ hours} = \\mathbf{132\\text{ miles}}$</span></div>
    """
    p30 = practice_page(
        "Compound Measures", "Standards L2.16, L2.26", 30, p30_scaffold,
        "A brass casting has a volume of $250\\text{ cm}^3$ and a mass of $2,125\\text{ g}$. Calculate the density of the brass in $\\text{g/cm}^3$.",
        "A hydraulic piston exerts a force of $1,800\\text{ N}$ on an area of $0.04\\text{ m}^2$. Calculate the pressure exerted in $\\text{N/m}^2$.",
        "A sales rep travels from Leeds to Birmingham ($115\\text{ miles}$). He departs at 07:45 and arrives at 10:09. Due to roadworks, he had to stop for a 15-minute coffee break. Calculate his average driving speed while moving."
    )
    pages.append(p30)

    # TOPIC 13: PAGE 31 (Theory) & PAGE 32 (Practice)
    p31 = """
    <h2>Time Calculations, 24-Hour Clock &amp; Timetables</h2>
    <p>Accurate time management across shift rosters, public transport schedules, and project milestone planning.</p>
    <div class="box-concept">
      <span class="tag-label tag-blue">Key Principle</span> <strong>The 60-Base Time System:</strong>
      Unlike decimal arithmetic, time works on base 60. Adding 45 minutes to 09:35 does NOT give 09:80. Add 25 minutes to reach the hour (10:00), then add remaining 20 minutes to reach 10:20.
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Multi-Leg Journey Planning</span>
      <p>An engineer catches the 08:37 train from Manchester. The train journey takes 1 hour 48 minutes. She then has a 12-minute walk to the factory. She must arrive before 10:45. Does she arrive in time?</p>
      <div class="step-row"><span>Step 1: Add 1 hour to 08:37</span><strong>09:37</strong></div>
      <div class="step-row"><span>Step 2: Add 23 mins to reach next hour: 09:37 + 23 mins</span><strong>10:00</strong></div>
      <div class="step-row"><span>Step 3: Remaining train time: 48 - 23 = 25 mins</span><strong>Train arrives at 10:25</strong></div>
      <div class="step-row"><span>Step 4: Add 12-minute walk: 10:25 + 12 mins</span><strong>Factory arrival: 10:37</strong></div>
      <p style="margin:3px 0 0 0;"><strong>Conclusion:</strong> Yes, she arrives at <strong>10:37</strong>, which is <strong>8 minutes early</strong>.</p>
    </div>
    <div class="box-trap">
      <span class="tag-label tag-red">Tutor Trap</span> <strong>Calculator Time Subtraction:</strong> Entering $10.45 - 8.37$ on a calculator gives $2.08$, leading learners to guess "2 hours 8 minutes". Real elapsed time is 2 hours 8 minutes only by sheer coincidence or wrong conversions! Always use timeline jumps.
    </div>
    """
    pages.append(wrap_page(p31, 31, "Strand 2: Measures, Shape & Space", "Standards: L2.17", "Maths Level 2 Core Study Guide"))

    p32_scaffold = """
    <div class="step-row"><span>Step 1: Jump to 12:00</span><span>$11:42 \\rightarrow 12:00 = 18\\text{ minutes}$</span></div>
    <div class="step-row"><span>Step 2: Jump from 12:00 to 15:15</span><span>$3\\text{ hours } 15\\text{ minutes}$</span></div>
    <div class="step-row"><span>Step 3: Sum durations</span><span>$18\\text{ m} + 3\\text{ h } 15\\text{ m} = \\mathbf{3\\text{ h } 33\\text{ mins}}$</span></div>
    """
    p32 = practice_page(
        "Time Calculations & Timetables", "Standards L2.17", 32, p32_scaffold,
        "Calculate the elapsed time between: a) 06:45 and 14:15 &emsp; b) 21:50 and 03:25 the next morning.",
        "A night-shift nurse works from 20:15 to 07:45. She has two 25-minute unpaid breaks during the shift. How many paid hours and minutes does she work per shift?",
        "An airport flight departs London at 13:40 UK time. The flight time is 4 hours 35 minutes. Greece is 2 hours ahead of the UK. What is the local time in Greece when the aircraft lands?"
    )
    pages.append(p32)

    # TOPIC 14: PAGE 33 (Theory) & PAGE 34 (Practice)
    p33 = """
    <h2>Wages, Overtime Rates, Income Tax &amp; NI</h2>
    <p>Calculating gross pay, time-and-a-half overtime, personal tax allowances, 20% basic income tax, and employee National Insurance.</p>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1d4ed8;">Statutory PAYE Income Tax Calculation Method</h3>
      <p>1. <strong>Gross Annual Pay</strong>: Total earnings before deductions.<br>
      2. <strong>Tax-Free Personal Allowance</strong>: $£12,570$ per year.<br>
      3. <strong>Taxable Income</strong>: $\\text{Gross Pay} - £12,570$.<br>
      4. <strong>Basic Rate Income Tax (20%)</strong>: $\\text{Taxable Income} \\times 0.20$.</p>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Annual Take-Home Pay</span>
      <p>An IT technician earns <strong>£26,570 per year</strong>. Calculate his annual income tax liability.</p>
      <div class="step-row"><span>Step 1: Deduct Personal Allowance: £26,570 - £12,570</span><strong>£14,000 taxable</strong></div>
      <div class="step-row"><span>Step 2: Calculate 20% basic tax: 0.20 × 14,000</span><strong>£2,800.00 tax</strong></div>
      <div class="step-row"><span>Step 3: Monthly tax deduction: 2800 ÷ 12</span><strong>£233.33 per month</strong></div>
    </div>
    <div class="box-trap">
      <span class="tag-label tag-red">Tutor Trap</span> <strong>Taxing Total Gross Pay:</strong> Never calculate $20\\%$ of the total $£26,570$! That would equal $£5,314$ and ignore the tax-free personal allowance. Only taxable income above $£12,570$ is taxed.
    </div>
    """
    pages.append(wrap_page(p33, 33, "Strand 2: Measures, Shape & Space", "Standards: L2.17", "Maths Level 2 Core Study Guide"))

    p34_scaffold = """
    <div class="step-row"><span>Step 1: Standard hours pay (37.5 hrs × £12.00)</span><span>$£450.00$</span></div>
    <div class="step-row"><span>Step 2: Overtime rate (time-and-a-half: £12 × 1.5)</span><span>$£18.00/\\text{hr}$</span></div>
    <div class="step-row"><span>Step 3: Overtime pay (6 hrs × £18.00)</span><span>$£108.00$</span></div>
    <div class="step-row"><span>Step 4: Total gross pay: £450 + £108</span><span>$\\mathbf{£558.00}$</span></div>
    """
    p34 = practice_page(
        "Wages, Taxes & Deductions", "Standards L2.17", 34, p34_scaffold,
        "A warehouse worker earns $£11.40$ per hour for a 35-hour week. Overtime is paid at double time. Calculate his gross wage in a week where he works 8 hours overtime.",
        "A marketing coordinator has a gross annual salary of $£31,200$. She has a tax-free personal allowance of $£12,570$. Calculate her total annual basic rate ($20\\%$) income tax.",
        "A senior care worker earns $£2,100$ gross per month. Deductions are: Income Tax $£184.50$, National Insurance $£126.80$, and Workplace Pension ($5\\%$ of gross pay). What is her net monthly take-home pay?"
    )
    pages.append(p34)

    # TOPIC 15: PAGE 35 (Theory) & PAGE 36 (Practice)
    p35 = """
    <h2>Perimeter &amp; Circumference of Circles &amp; Sectors</h2>
    <p>Calculating boundaries of polygons, circular perimeters, semicircular running tracks, and sector arc lengths.</p>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1d4ed8;">Circle Formulas (Take $\\pi = 3.14$ or $3.142$)</h3>
      <p>$$\\text{Circumference } C = \\pi d = 2 \\pi r$$</p>
      <p>Where $d = \\text{diameter}$ and $r = \\text{radius}$ ($d = 2r$).</p>
      <p><strong>Perimeter of Semicircle:</strong> Curved arc $+ \\text{straight diameter} = \\frac{\\pi d}{2} + d$.</p>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Fencing a Semicircular Garden</span>
      <p>A landscape gardener builds a semicircular patio with a diameter of <strong>8 metres</strong>. Calculate the total perimeter to be bordered.</p>
      <div class="step-row"><span>Step 1: Calculate full circle circumference: π × 8</span><strong>3.14 × 8 = 25.12 m</strong></div>
      <div class="step-row"><span>Step 2: Half circumference (curved arc): 25.12 ÷ 2</span><strong>12.56 m</strong></div>
      <div class="step-row"><span>Step 3: Add the straight edge (diameter): 12.56 + 8</span><strong>20.56 metres</strong></div>
    </div>
    <div class="box-trap">
      <span class="tag-label tag-red">Tutor Trap</span> <strong>Forgetting the Straight Edge:</strong> In semicircles and composite shapes, learners frequently calculate $\\frac{\\pi d}{2}$ and forget to add the diameter straight edge. A perimeter must form a complete enclosed boundary!
    </div>
    """
    pages.append(wrap_page(p35, 35, "Strand 2: Measures, Shape & Space", "Standards: L2.18, L2.19", "Maths Level 2 Core Study Guide"))

    p36_scaffold = """
    <div class="step-row"><span>Step 1: Identify radius and diameter</span><span>$r = 3.5\\text{ m} \\Rightarrow d = 7\\text{ m}$</span></div>
    <div class="step-row"><span>Step 2: Curved semicircle arc: $(\\pi \\times 7) \\div 2$</span><span>$(3.142 \\times 7) \\div 2 = 10.997\\text{ m}$</span></div>
    <div class="step-row"><span>Step 3: Total perimeter: Arc + Diameter</span><span>$10.997 + 7 = \\mathbf{18.0\\text{ metres}}$</span></div>
    """
    p36 = practice_page(
        "Perimeter & Circumference", "Standards L2.18, L2.19", 36, p36_scaffold,
        "Calculate the circumference of a circular water tank with a radius of $4.5\\text{ metres}$. (Use $\\pi = 3.14$)",
        "A running track consists of a rectangle measuring $100\\text{ m}$ by $64\\text{ m}$ with two semicircular ends. Calculate the total running distance around the outer edge of one complete lap.",
        "A decorative wrought-iron garden gate has a rectangular base ($1.2\\text{ m}$ wide by $1.8\\text{ m}$ high) topped with a semicircular arch. What total length of iron framing is needed for the perimeter? (Use $\\pi = 3.142$)"
    )
    pages.append(p36)

    # TOPIC 16: PAGE 37 (Theory) & PAGE 38 (Practice)
    p37 = """
    <h2>2D Area: Parallelograms, Trapeziums &amp; Composite Shapes</h2>
    <p>Calculating surface coverage for flooring, turf, wall painting, and paving using standard statutory formulas.</p>
    <div class="grid-2col">
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8;">Statutory 2D Area Formulas</h3>
        <p>&bull; <strong>Triangle:</strong> $\\text{Area} = \\frac{1}{2} b h$<br>
        &bull; <strong>Parallelogram:</strong> $\\text{Area} = b \\times h$<br>
        &bull; <strong>Trapezium:</strong> $\\text{Area} = \\frac{(a + b)}{2} \\times h$<br>
        &bull; <strong>Circle:</strong> $\\text{Area} = \\pi r^2$</p>
      </div>
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8;">Decomposing Composite Shapes</h3>
        <p>1. Split the complex shape into simple non-overlapping rectangles, triangles, or trapeziums.<br>
        2. Calculate the area of each separate section.<br>
        3. Sum all sections together.</p>
      </div>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Area of a Trapezium Garden Plot</span>
      <p>A garden plot is shaped as a trapezium with parallel sides $a = 6\\text{ m}$ and $b = 10\\text{ m}$, and a perpendicular distance $h = 4.5\\text{ m}$. Calculate its area.</p>
      <div class="step-row"><span>Step 1: Add parallel sides: 6 + 10</span><strong>16 metres</strong></div>
      <div class="step-row"><span>Step 2: Average parallel sides: 16 ÷ 2</span><strong>8 metres</strong></div>
      <div class="step-row"><span>Step 3: Multiply by perpendicular height: 8 × 4.5</span><strong>36 m²</strong></div>
    </div>
    <div class="box-trap">
      <span class="tag-label tag-red">Tutor Trap</span> <strong>Using Slanted Height:</strong> Never use the slanted side when calculating area of triangles or trapeziums! You must always use the <strong>perpendicular (vertical $90^\\circ$) height</strong>.
    </div>
    """
    pages.append(wrap_page(p37, 37, "Strand 2: Measures, Shape & Space", "Standards: L2.18, L2.19", "Maths Level 2 Core Study Guide"))

    p38_scaffold = """
    <div class="step-row"><span>Step 1: Split L-shape into two rectangles</span><span>Rect A: $8\\text{ m} \\times 4\\text{ m} = 32\\text{ m}^2$</span></div>
    <div class="step-row"><span>Step 2: Rect B dimensions and area</span><span>Rect B: $6\\text{ m} \\times 3\\text{ m} = 18\\text{ m}^2$</span></div>
    <div class="step-row"><span>Step 3: Sum areas</span><span>$32 + 18 = \\mathbf{50\\text{ m}^2}$</span></div>
    """
    p38 = practice_page(
        "2D Composite Area", "Standards L2.18, L2.19", 38, p38_scaffold,
        "Calculate the area of a circular patio with a diameter of $6\\text{ metres}$. Give your answer to 2 decimal places. (Use $\\pi = 3.142$)",
        "A flat roof in the shape of a trapezium has parallel sides of $7.2\\text{ m}$ and $11.8\\text{ m}$, and a perpendicular width of $5.0\\text{ m}$. Roofing felt costs $£8.50$ per square metre. Calculate the cost to felt the roof.",
        "A sports hall floor has an L-shaped layout: $14\\text{ m}$ overall length by $10\\text{ m}$ overall width. A cutout corner measures $6\\text{ m}$ by $4\\text{ m}$. A tin of floor varnish covers $25\\text{ m}^2$ and costs $£34.99$. How many tins must be bought, and what is the total cost?"
    )
    pages.append(p38)

    # TOPIC 17: PAGE 39 (Theory) & PAGE 40 (Practice)
    p39 = """
    <h2>Surface Area of 3D Prisms &amp; Cylinders</h2>
    <p>Surface area is the total area of all exterior 2D faces of a three-dimensional object. Essential for packaging, painting, and insulation.</p>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1d4ed8;">Surface Area Formulas</h3>
      <p>&bull; <strong>Cuboid:</strong> $\\text{SA} = 2(lw + lh + wh)$<br>
      &bull; <strong>Triangular Prism:</strong> Area of 2 identical triangular ends $+ 3$ rectangular side faces.<br>
      &bull; <strong>Closed Cylinder:</strong> $\\text{SA} = 2\\pi r^2 + 2\\pi rh$ (2 circular ends $+$ curved rectangular body).</p>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Surface Area of a Cylinder</span>
      <p>A closed cylindrical food tin has a radius $r = 4\\text{ cm}$ and height $h = 10\\text{ cm}$. Calculate its total exterior surface area. (Take $\\pi = 3.14$)</p>
      <div class="step-row"><span>Step 1: Area of 2 circular ends: 2 × π × 4² = 2 × 3.14 × 16</span><strong>100.48 cm²</strong></div>
      <div class="step-row"><span>Step 2: Area of curved surface: 2 × π × 4 × 10 = 80 × 3.14</span><strong>251.20 cm²</strong></div>
      <div class="step-row"><span>Step 3: Total surface area: 100.48 + 251.20</span><strong>351.68 cm²</strong></div>
    </div>
    <div class="box-trap">
      <span class="tag-label tag-red">Tutor Trap</span> <strong>Open vs Closed Cylinders:</strong> Carefully read whether the cylinder is <strong>open-topped</strong> (like a bucket: 1 circle $+ 2\\pi rh$) or <strong>closed</strong> (a tin: 2 circles $+ 2\\pi rh$).
    </div>
    """
    pages.append(wrap_page(p39, 39, "Strand 2: Measures, Shape & Space", "Standards: L2.20, L2.21", "Maths Level 2 Core Study Guide"))

    p40_scaffold = """
    <div class="step-row"><span>Step 1: Calculate area of top & bottom: $2 \\times (5 \\times 4)$</span><span>$40\\text{ m}^2$</span></div>
    <div class="step-row"><span>Step 2: Calculate area of front & back: $2 \\times (5 \\times 3)$</span><span>$30\\text{ m}^2$</span></div>
    <div class="step-row"><span>Step 3: Calculate area of two side walls: $2 \\times (4 \\times 3)$</span><span>$24\\text{ m}^2$</span></div>
    <div class="step-row"><span>Step 4: Sum all 6 faces</span><span>$40 + 30 + 24 = \\mathbf{94\\text{ m}^2}$</span></div>
    """
    p40 = practice_page(
        "Surface Area of 3D Solids", "Standards L2.20, L2.21", 40, p40_scaffold,
        "Calculate the total surface area of a cuboid measuring $12\\text{ cm}$ long, $8\\text{ cm}$ wide, and $5\\text{ cm}$ high.",
        "A triangular prism has identical right-angled triangular ends with base $6\\text{ cm}$, height $8\\text{ cm}$, and hypotenuse $10\\text{ cm}$. The prism is $15\\text{ cm}$ long. Calculate its total surface area.",
        "A manufacturer designs an open-topped cylindrical metal bin with diameter $40\\text{ cm}$ and height $75\\text{ cm}$. The exterior of the base and curved side is powder-coated. What surface area in square metres must be coated? (Use $\\pi = 3.142$)"
    )
    pages.append(p40)

    # TOPIC 18: PAGE 41 (Theory) & PAGE 42 (Practice)
    p41 = """
    <h2>Volume of Prisms, Cylinders &amp; Liquid Capacity</h2>
    <p>Volume measures 3D space enclosed within a solid object. Capacity converts internal volume into litres and millilitres.</p>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1d4ed8;">Statutory Volume of Prisms</h3>
      <p>$$\\text{Volume of any Prism} = \\text{Area of Cross-Section} \\times \\text{Length}$$</p>
      <p>&bull; <strong>Cuboid:</strong> $V = l \\times w \\times h$<br>
      &bull; <strong>Cylinder:</strong> $V = \\pi r^2 h$<br>
      &bull; <strong>Triangular Prism:</strong> $V = \\frac{1}{2} b h \\times l$<br>
      &bull; <strong>Capacity Equivalence:</strong> $1000\\text{ cm}^3 = 1\\text{ litre}$; $1\\text{ m}^3 = 1000\\text{ litres}$.</p>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Water Tank Capacity</span>
      <p>A rectangular water storage cistern measures $1.5\\text{ m}$ long, $0.8\\text{ m}$ wide, and $0.6\\text{ m}$ deep. How many litres of water does it hold when full?</p>
      <div class="step-row"><span>Step 1: Calculate volume in cubic metres: 1.5 × 0.8 × 0.6</span><strong>0.72 m³</strong></div>
      <div class="step-row"><span>Step 2: Convert m³ to litres (multiply by 1000)</span><strong>0.72 × 1000 = 720 litres</strong></div>
    </div>
    <div class="box-trap">
      <span class="tag-label tag-red">Tutor Trap</span> <strong>Using Diameter Instead of Radius:</strong> In $V = \\pi r^2 h$, squaring the diameter ($d^2$) instead of the radius produces an answer <strong>4 times too big</strong>! Always divide diameter by 2 first.
    </div>
    """
    pages.append(wrap_page(p41, 41, "Strand 2: Measures, Shape & Space", "Standards: L2.21", "Maths Level 2 Core Study Guide"))

    p42_scaffold = """
    <div class="step-row"><span>Step 1: Find radius from diameter</span><span>$d = 1.2\\text{ m} \\Rightarrow r = 0.6\\text{ m}$</span></div>
    <div class="step-row"><span>Step 2: Cross-sectional circular area: $\\pi r^2$</span><span>$3.142 \\times 0.6^2 = 1.131\\text{ m}^2$</span></div>
    <div class="step-row"><span>Step 3: Multiply by height: $1.131 \\times 2.5$</span><span>$2.828\\text{ m}^3 \\approx \\mathbf{2,828\\text{ litres}}$</span></div>
    """
    p42 = practice_page(
        "Volume & Liquid Capacity", "Standards L2.21", 42, p42_scaffold,
        "Calculate the volume of a triangular prism where the cross-sectional triangle has base $8\\text{ cm}$ and height $5\\text{ cm}$, and the length is $22\\text{ cm}$.",
        "A cylindrical oil barrel has a diameter of $60\\text{ cm}$ and a height of $90\\text{ cm}$. Calculate its capacity in litres to 1 decimal place. (Use $\\pi = 3.14$)",
        "A swimming pool measures $12\\text{ m}$ long and $6\\text{ m}$ wide. The shallow end is $1.0\\text{ m}$ deep and slopes uniformly to $2.2\\text{ m}$ at the deep end. Calculate the total volume of water in the pool in cubic metres and litres."
    )
    pages.append(p42)

    # TOPIC 19: PAGE 43 (Theory) & PAGE 44 (Practice)
    p43 = """
    <h2>Scale Drawings, Bearings &amp; Map Navigation</h2>
    <p>Architectural floor plans, site location surveys, and precision navigation using three-figure bearings.</p>
    <div class="grid-2col">
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8;">Scale Ratios (1 : n)</h3>
        <p>A scale of $1 : 50$ means $1\\text{ cm}$ on paper represents $50\\text{ cm}$ in real life ($0.5\\text{ m}$).<br>
        <strong>Real length</strong> $=$ Plan length $\\times$ Scale factor.<br>
        <strong>Plan length</strong> $=$ Real length $\\div$ Scale factor.</p>
      </div>
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8;">Three-Figure Bearings</h3>
        <p>1. Measured from <strong>North ($000^\\circ$)</strong>.<br>
        2. Measured in a <strong>clockwise</strong> direction.<br>
        3. Always written with <strong>three digits</strong> (e.g. $045^\\circ$, $085^\\circ$, $270^\\circ$).<br>
        <strong>Back bearing:</strong> Add or subtract $180^\\circ$.</p>
      </div>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Room Measurement on Plan</span>
      <p>On an architectural plan drawn to a scale of <strong>1 : 75</strong>, a living room wall measures <strong>8.4 cm</strong>. What is the real length of the wall in metres?</p>
      <div class="step-row"><span>Step 1: Multiply plan length by scale factor: 8.4 × 75</span><strong>630 cm</strong></div>
      <div class="step-row"><span>Step 2: Convert cm to metres: 630 ÷ 100</span><strong>6.3 metres</strong></div>
    </div>
    <div class="box-trap">
      <span class="tag-label tag-red">Tutor Trap</span> <strong>Measuring Bearings Counter-Clockwise:</strong> Bearings must strictly be measured clockwise from North! If a town is $30^\\circ$ west of North, its bearing is $360^\\circ - 30^\\circ = 330^\\circ$, NOT $030^\\circ$.
    </div>
    """
    pages.append(wrap_page(p43, 43, "Strand 2: Measures, Shape & Space", "Standards: L2.22, L2.23", "Maths Level 2 Core Study Guide"))

    p44_scaffold = """
    <div class="step-row"><span>Step 1: Convert real distance ($15\\text{ km}$) to metres</span><span>$15 \\times 1000 = 15,000\\text{ m}$</span></div>
    <div class="step-row"><span>Step 2: Convert to cm</span><span>$15,000 \\times 100 = 1,500,000\\text{ cm}$</span></div>
    <div class="step-row"><span>Step 3: Divide by scale factor ($50,000$)</span><span>$1,500,000 \\div 50,000 = \\mathbf{30\\text{ cm}}$</span></div>
    """
    p44 = practice_page(
        "Scale Drawings & Bearings", "Standards L2.22, L2.23", 44, p44_scaffold,
        "A scale drawing uses the scale $1 : 20$. A doorway is $90\\text{ cm}$ wide in reality. What is its width on the drawing in centimetres?",
        "Ship A sails from port on a bearing of $065^\\circ$. What is the back bearing that Ship A must follow to return directly to the port?",
        "A site surveyor creates a site plan using a scale of $1 : 200$. On the plan, a rectangular warehouse boundary measures $18.5\\text{ cm}$ by $12.0\\text{ cm}$. Calculate the real perimeter of the boundary in metres, and its real ground area in square metres."
    )
    pages.append(p44)

    # TOPIC 20: PAGE 45 (Theory) & PAGE 46 (Practice)
    p45 = """
    <h2>Plans, Elevations, Nets &amp; 3D Symmetry</h2>
    <p>Orthographic projections: Plan view (from above), Front elevation (from front), and Side elevation (from side).</p>
    <div class="box-concept">
      <span class="tag-label tag-blue">Key Principle</span> <strong>Orthographic Projections:</strong>
      Architects and engineers convey 3D structures using 2D technical drawings. The <strong>Plan</strong> is the bird's-eye view looking directly down. The <strong>Front Elevation</strong> is the direct head-on view. The <strong>Side Elevation</strong> shows the profile from the left or right.
    </div>
    <div class="grid-2col">
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8;">Nets of 3D Solids</h3>
        <p>A 2D net folds into a 3D solid without overlapping faces.<br>
        &bull; <strong>Cube:</strong> 6 identical square faces.<br>
        &bull; <strong>Cuboid:</strong> 3 pairs of matching rectangles.<br>
        &bull; <strong>Cylinder:</strong> 2 circles and 1 rectangle whose length equals $2\\pi r$.</p>
      </div>
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8;">Planes of Symmetry</h3>
        <p>A plane of symmetry cuts a 3D solid into two mirror-image halves.<br>
        &bull; A cube has <strong>9 planes of symmetry</strong>.<br>
        &bull; A cuboid with 3 different side lengths has <strong>3 planes of symmetry</strong>.</p>
      </div>
    </div>
    <div class="box-trap">
      <span class="tag-label tag-red">Tutor Trap</span> <strong>Matching Dimensions:</strong> When drawing elevations, the height on the front elevation must exactly match the height on the side elevation. Check dimensions across all projections!
    </div>
    """
    pages.append(wrap_page(p45, 45, "Strand 2: Measures, Shape & Space", "Standards: L2.24, L2.25", "Maths Level 2 Core Study Guide"))

    p46_scaffold = """
    <div class="step-row"><span>Step 1: Front elevation dimensions</span><span>Width = $6\\text{ m}$, Height = $2.5\\text{ m}$ (rectangular)</span></div>
    <div class="step-row"><span>Step 2: Gable roof triangle</span><span>Base = $6\\text{ m}$, Apex height = $1.5\\text{ m}$ (total height $4.0\\text{ m}$)</span></div>
    <div class="step-row"><span>Step 3: Side elevation</span><span>Length = $8\\text{ m}$, Wall height = $2.5\\text{ m}$, Roof pitch visible</span></div>
    """
    p46 = practice_page(
        "Plans & Elevations", "Standards L2.24, L2.25", 46, p46_scaffold,
        "State the number of faces, edges, and vertices on a triangular prism.",
        "A cylinder has radius $5\\text{ cm}$ and height $12\\text{ cm}$. Describe the shape and exact dimensions of the 2D rectangular portion of its unfolded net. (Take $\\pi = 3.14$)",
        "A developer is constructing a modular security cabin: $5\\text{ m}$ long, $3\\text{ m}$ wide, and $2.4\\text{ m}$ high with a flat roof. Draw a sketch showing the Plan view, Front elevation, and Side elevation using a grid scale where $1\\text{ square} = 0.5\\text{ m}$."
    )
    pages.append(p46)

    # CHECKPOINT 2: PAGES 47 TO 50 (4-page Review Assessment)
    chk2_p1 = [
        (1, 2, "A delivery truck travels 135 miles in 2 hours 15 minutes. Calculate its average speed in miles per hour.", 75),
        (2, 2, "Convert: a) $4.2\\text{ kg}$ to grams &emsp; b) $650\\text{ ml}$ to litres &emsp; c) $25\\text{ miles}$ to km using $5\\text{ miles} = 8\\text{ km}$.", 65),
        (3, 2, "A circle has a diameter of $14\\text{ cm}$. Using $\\pi = \\frac{22}{7}$, calculate: a) its circumference &emsp; b) its area.", 70)
    ]
    pages.append(checkpoint_page("Strand 2: Measures, Shape & Space", "Part 1 &bull; Non-Calculator (Q1-Q3)", 47, "6 Marks", chk2_p1))

    chk2_p2 = [
        (4, 2, "A rectangular courtyard measures $12\\text{ m}$ by $8.5\\text{ m}$. In the centre is a square fountain with sides of $2.5\\text{ m}$. Calculate the paved area of the courtyard.", 75),
        (5, 2, "A clock shows 09:35. An online training conference lasts for 3 hours 48 minutes. At what time does the conference end? (Use 24-hour clock format)", 65),
        (6, 2, "A warehouse worker earns $£12.50$ per hour for 36 hours. Overtime is paid at time-and-a-half. In one week he works 4 hours overtime. What is his gross pay?", 70)
    ]
    pages.append(checkpoint_page("Strand 2: Measures, Shape & Space", "Part 1 &bull; Non-Calculator (Q4-Q6)", 48, "6 Marks", chk2_p2))

    chk2_p3 = [
        (7, 3, "A commercial grain silo is shaped as a cylinder with diameter $4.2\\text{ m}$ and height $8.5\\text{ m}$. Calculate the volume of the silo in cubic metres to 1 decimal place. (Use $\\pi = 3.142$)", 80),
        (8, 3, "A metal casting has a mass of $3,570\\text{ g}$ and a volume of $420\\text{ cm}^3$. Calculate its density in $\\text{g/cm}^3$. If pure zinc has a density of $7.14\\text{ g/cm}^3$, determine whether the casting is pure zinc.", 80),
        (9, 3, "On a map with a scale of $1 : 25,000$, the distance between two telecommunication masts is $16.4\\text{ cm}$. Calculate the actual distance between the masts in kilometres.", 80)
    ]
    pages.append(checkpoint_page("Strand 2: Measures, Shape & Space", "Part 2 &bull; Calculator Allowed (Q7-Q9)", 49, "9 Marks", chk2_p3))

    chk2_p4 = [
        (10, 3, "An office worker earns $£34,000$ gross per year. The tax-free personal allowance is $£12,570$. Basic rate income tax is charged at $20\\%$. Employee National Insurance is $8\\%$ on earnings above $£12,570$. Calculate her total monthly take-home pay after tax and NI.", 80),
        (11, 3, "A lawn is in the shape of a trapezium with parallel sides $14\\text{ m}$ and $22\\text{ m}$, and perpendicular distance $12\\text{ m}$. Grass seed costs $£6.40$ per box. Each box covers $25\\text{ m}^2$. How much does it cost to seed the entire lawn?", 80),
        (12, 3, "A heating engineer installs a closed cylindrical thermal expansion vessel: radius $0.35\\text{ m}$ and height $1.2\\text{ m}$. The entire exterior surface is insulated with thermal foil costing $£14.50/\\text{m}^2$. Calculate the cost of the foil. (Use $\\pi = 3.142$)", 80)
    ]
    pages.append(checkpoint_page("Strand 2: Measures, Shape & Space", "Part 2 &bull; Calculator Allowed (Q10-Q12)", 50, "9 Marks", chk2_p4))

    # =========================================================================
    # STRAND 3: HANDLING INFORMATION & DATA (PAGES 51 - 70)
    # =========================================================================

    # TOPIC 21: PAGE 51 (Theory) & PAGE 52 (Practice)
    p51 = """
    <h2>Two-Way Frequency Tables &amp; Data Records</h2>
    <p>Organising multi-category survey data, cross-tabulating frequency counts, and auditing records for completeness.</p>
    <div class="box-concept">
      <span class="tag-label tag-blue">Key Principle</span> <strong>The Row and Column Sum Rule:</strong>
      In any two-way table, the sum of values across every row must equal the row total, the sum down every column must equal the column total, and both the row totals and column totals must sum to the identical <strong>Grand Total</strong>.
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Completing a Workplace Survey Table</span>
      <p>60 warehouse operatives were asked whether they prefer Day Shift or Night Shift.</p>
      <table class="cgp-table">
        <tr><th>Shift</th><th>Full-Time</th><th>Part-Time</th><th>Total</th></tr>
        <tr><td>Day Shift</td><td>24</td><td>[ 11 ]</td><td>35</td></tr>
        <tr><td>Night Shift</td><td>[ 18 ]</td><td>7</td><td>[ 25 ]</td></tr>
        <tr><td>Total</td><td>42</td><td>18</td><td>60</td></tr>
      </table>
      <div class="step-row"><span>Step 1: Day Shift Part-Time = 35 - 24</span><strong>11</strong></div>
      <div class="step-row"><span>Step 2: Night Shift Full-Time = 42 - 24</span><strong>18</strong></div>
      <div class="step-row"><span>Step 3: Night Shift Total = 18 + 7</span><strong>25</strong></div>
      <div class="step-row"><span>Step 4: Check grand sum: 35 + 25 = 60; 42 + 18 = 60</span><strong>Verified</strong></div>
    </div>
    <div class="box-trap">
      <span class="tag-label tag-red">Tutor Trap</span> <strong>Mixing Row and Column Categories:</strong> Learners often misread questions like "What fraction of <em>Night Shift workers</em> are Part-Time?" The denominator is the Night Shift total ($25$), NOT the grand total ($60$). Fraction $= \\frac{7}{25}$.
    </div>
    """
    pages.append(wrap_page(p51, 51, "Strand 3: Handling Information & Data", "Standards: L2.28, L2.29", "Maths Level 2 Core Study Guide"))

    p52_scaffold = """
    <div class="step-row"><span>Step 1: Total Males = 50 - 28</span><span>$22\\text{ males}$</span></div>
    <div class="step-row"><span>Step 2: Males Passed = 22 - 6</span><span>$16\\text{ passed}$</span></div>
    <div class="step-row"><span>Step 3: Total Passed = 50 - 15</span><span>$35\\text{ passed}$</span></div>
    <div class="step-row"><span>Step 4: Females Passed = 35 - 16</span><span>$\\mathbf{19\\text{ females passed}}$</span></div>
    """
    p52 = practice_page(
        "Two-Way Tables", "Standards L2.28, L2.29", 52, p52_scaffold,
        "80 candidates took a driving test: 45 were female. 26 females passed. 12 males failed. Complete a two-way frequency table showing gender and test result.",
        "From the table above, what percentage of the male candidates passed the driving test? Give your answer to 1 decimal place.",
        "A transport company audits 120 vehicle maintenance logs categorized by Vehicle Type (Van, Lorry) and Inspection Result (First-Time Pass, Minor Advisory, Major Fail). 70 vehicles are Vans. Of the Vans, 42 passed first time and 10 had major fails. Of the Lorries, 18 had minor advisories and 12 had major fails. Complete the table and find the probability that a randomly chosen Lorry passed first time."
    )
    pages.append(p52)

    # TOPIC 22: PAGE 53 (Theory) & PAGE 54 (Practice)
    p53 = """
    <h2>Bar Charts: Dual, Grouped &amp; Component Charts</h2>
    <p>Constructing and interpreting comparative bar charts, ensuring uniform scales, and reading dual-axis distributions.</p>
    <div class="box-concept">
      <span class="tag-label tag-blue">Key Rules for Bar Charts</span>
      1. <strong>Equal Bar Widths:</strong> Every bar must have the exact same width.<br>
      2. <strong>Equal Gaps:</strong> Gaps between discrete categories must be consistent.<br>
      3. <strong>Numbered Scale:</strong> The frequency axis (vertical) must start at <strong>0</strong> and have linear increments (e.g. 5, 10, 15).<br>
      4. <strong>Full Labels:</strong> Both axes must be labeled with units, and a legend (key) must be included for dual/stacked bars.
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Reading a Dual Bar Chart</span>
      <p>A dual bar chart compares quarterly sales (£ thousands) between Branch A and Branch B.</p>
      <div class="step-row"><span>Q1 Sales: Branch A = £45k, Branch B = £30k</span><strong>Branch A lead: £15k</strong></div>
      <div class="step-row"><span>Q2 Sales: Branch A = £50k, Branch B = £65k</span><strong>Branch B lead: £15k</strong></div>
      <div class="step-row"><span>Annual Total: Branch A = £190k, Branch B = £210k</span><strong>Overall Winner: Branch B</strong></div>
    </div>
    <div class="box-trap">
      <span class="tag-label tag-red">Tutor Trap</span> <strong>Truncated Axes:</strong> Beware of charts that do not start the vertical axis at 0. A bar from 90 to 100 looks twice as tall as one from 90 to 95, visually exaggerating differences. Always read the numerical values!
    </div>
    """
    pages.append(wrap_page(p53, 53, "Strand 3: Handling Information & Data", "Standards: L2.30", "Maths Level 2 Core Study Guide"))

    p54_scaffold = """
    <div class="step-row"><span>Step 1: Calculate total for 2024</span><span>$45 + 60 + 55 + 80 = £240\\text{k}$</span></div>
    <div class="step-row"><span>Step 2: Calculate total for 2025</span><span>$50 + 75 + 70 + 95 = £290\\text{k}$</span></div>
    <div class="step-row"><span>Step 3: Percentage increase: $(290 - 240) \\div 240 \\times 100$</span><span>$\\mathbf{20.8\\%}$</span></div>
    """
    p54 = practice_page(
        "Bar Charts & Comparisons", "Standards L2.30", 54, p54_scaffold,
        "A clinic records patient attendances: Mon 45, Tue 60, Wed 55, Thu 70, Fri 80. State the modal day and the range of attendances.",
        "A dual bar chart displays apprentice exam results: Engineering (Pass: 36, Fail: 9); Business (Pass: 42, Fail: 8). Compare the percentage pass rates between the two departments.",
        "A retail store tracks customer feedback ratings across 3 departments: Electronics (Positive 85, Neutral 25, Negative 10), Homeware (Positive 60, Neutral 30, Negative 20), Clothing (Positive 110, Neutral 40, Negative 15). Draw up a component (stacked) bar representation plan and calculate which department has the highest proportion of positive reviews."
    )
    pages.append(p54)

    # TOPIC 23: PAGE 55 (Theory) & PAGE 56 (Practice)
    p55 = """
    <h2>Line Graphs, Trend Lines &amp; Continuous Data</h2>
    <p>Plotting continuous variables over time, identifying seasonal variations, and interpolating intermediate values.</p>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1d4ed8;">Line Graph Construction Rules</h3>
      <p>&bull; <strong>Time on Horizontal Axis:</strong> Time (hours, days, months, years) is the independent variable and always goes on the x-axis.<br>
      &bull; <strong>Plotting Points:</strong> Use small, neat crosses ($\times$) exactly on grid intersections.<br>
      &bull; <strong>Joining Points:</strong> Connect consecutive points with straight ruled lines.<br>
      &bull; <strong>Interpolation vs Extrapolation:</strong> Reading <em>between</em> known points (interpolation) is reliable; predicting <em>beyond</em> known data (extrapolation) carries uncertainty.</p>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Reading a Patient Temperature Chart</span>
      <p>A hospital patient's temperature is monitored every 2 hours: 08:00 ($38.5^\\circ\\text{C}$), 10:00 ($38.8^\\circ\\text{C}$), 12:00 ($37.8^\\circ\\text{C}$), 14:00 ($37.2^\\circ\\text{C}$).</p>
      <div class="step-row"><span>Estimated temperature at 11:00 (midpoint)</span><strong>38.3°C</strong></div>
      <div class="step-row"><span>Time fever broke (returned to normal &le; 37.5°C)</span><strong>13:00</strong></div>
    </div>
    <div class="box-trap">
      <span class="tag-label tag-red">Tutor Trap</span> <strong>Non-Uniform Time Intervals:</strong> If data is recorded at irregular times (e.g. after 1 hr, then after 4 hrs, then after 2 hrs), spacing them equally along the x-axis distorts the rate of change. Space proportionally!
    </div>
    """
    pages.append(wrap_page(p55, 55, "Strand 3: Handling Information & Data", "Standards: L2.30", "Maths Level 2 Core Study Guide"))

    p56_scaffold = """
    <div class="step-row"><span>Step 1: Identify coordinates at 09:00 and 15:00</span><span>$(09:00, 14^\\circ\\text{C})$ and $(15:00, 26^\\circ\\text{C})$</span></div>
    <div class="step-row"><span>Step 2: Calculate temperature change</span><span>$26 - 14 = 12^\\circ\\text{C}$</span></div>
    <div class="step-row"><span>Step 3: Hourly rate of increase: $12 \\div 6$</span><span>$\\mathbf{2.0^\\circ\\text{C/hour}}$</span></div>
    """
    p56 = practice_page(
        "Line Graphs & Trends", "Standards L2.30", 56, p56_scaffold,
        "A delivery van's fuel level was recorded: 09:00 ($60\\text{ L}$), 11:00 ($48\\text{ L}$), 13:00 ($32\\text{ L}$), 15:00 ($20\\text{ L}$). Estimate the fuel remaining at 12:00.",
        "Describe the overall trend shown in the fuel level data above and calculate the average rate of fuel consumption per hour.",
        "A factory's daily electricity consumption (kWh) over a week is: Mon 420, Tue 450, Wed 480, Thu 460, Fri 430, Sat 180, Sun 120. Explain why a line graph is appropriate, identify the peak usage day, and explain why weekend consumption drops sharply."
    )
    pages.append(p56)

    # TOPIC 24: PAGE 57 (Theory) & PAGE 58 (Practice)
    p57 = """
    <h2>Pie Charts: Calculation, Angles &amp; Percentages</h2>
    <p>Representing proportions of a whole where the full circular disc represents $360^\\circ$ and $100\\%$.</p>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1d4ed8;">Statutory Sector Angle Formula</h3>
      <p>$$\\text{Degrees per Item} = \\frac{360^\\circ}{\\text{Total Frequency}}$$</p>
      <p>$$\\text{Sector Angle} = \\frac{\\text{Frequency}}{\\text{Total Frequency}} \\times 360^\\circ$$</p>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Drawing a Transport Survey Pie Chart</span>
      <p>72 office workers were asked how they travel to work: Car (36), Bus (18), Train (12), Walk (6).</p>
      <div class="step-row"><span>Step 1: Degrees per worker: 360° ÷ 72</span><strong>5° per person</strong></div>
      <div class="step-row"><span>Step 2: Car sector: 36 × 5°</span><strong>180° (exactly half)</strong></div>
      <div class="step-row"><span>Step 3: Bus sector: 18 × 5°</span><strong>90° (quarter circle)</strong></div>
      <div class="step-row"><span>Step 4: Train sector: 12 × 5°</span><strong>60°</strong></div>
      <div class="step-row"><span>Step 5: Walk sector: 6 × 5°</span><strong>30°</strong></div>
      <div class="step-row"><span>Step 6: Check sum: 180° + 90° + 60° + 30°</span><strong>360° verified</strong></div>
    </div>
    <div class="box-trap">
      <span class="tag-label tag-red">Tutor Trap</span> <strong>Comparing Two Different Pie Charts:</strong> A larger sector angle in Chart A does NOT necessarily mean more people than Chart B! Chart A might represent 40 people while Chart B represents 1,000 people. Angles show <em>proportions</em>, not raw numbers.
    </div>
    """
    pages.append(wrap_page(p57, 57, "Strand 3: Handling Information & Data", "Standards: L2.31", "Maths Level 2 Core Study Guide"))

    p58_scaffold = """
    <div class="step-row"><span>Step 1: Identify angle and total degrees</span><span>$\\text{Angle} = 72^\\circ$; Total circle $= 360^\\circ$</span></div>
    <div class="step-row"><span>Step 2: Fraction of circle: $72 \\div 360$</span><span>$\\frac{1}{5} = 0.20$ ($20\\%$)</span></div>
    <div class="step-row"><span>Step 3: Multiply by total budget: $0.20 \\times £45,000$</span><span>$\\mathbf{£9,000}$</span></div>
    """
    p58 = practice_page(
        "Pie Charts", "Standards L2.31", 58, p58_scaffold,
        "A hotel survey of 120 guests showed: Business (40), Holiday (60), Event (20). Calculate the angle for each sector.",
        "In a pie chart representing 1,800 voters, the sector for Candidate A has an angle of $108^\\circ$. How many people voted for Candidate A?",
        "A local council spends an annual transport budget of $£2.4\\text{ million}$. In a pie chart, Highway Maintenance is allocated $135^\\circ$, Public Buses $90^\\circ$, Cycle Lanes $45^\\circ$, and Pedestrian Paths $90^\\circ$. Calculate the actual expenditure on Cycle Lanes and express it as a percentage of the total budget."
    )
    pages.append(p58)

    # TOPIC 25: PAGE 59 (Theory) & PAGE 60 (Practice)
    p59 = """
    <h2>Averages: Mean, Median, Mode &amp; Range</h2>
    <p>Summarising data sets using measures of central tendency (mean, median, mode) and measure of spread (range).</p>
    <div class="grid-2col">
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8;">The 3 Measures of Average</h3>
        <p>&bull; <strong>Mean:</strong> $\\frac{\\text{Sum of all values}}{\\text{Number of values}}$.<br>
        &bull; <strong>Median:</strong> Middle value when ordered smallest to largest. If even count, average middle two.<br>
        &bull; <strong>Mode:</strong> Most frequently occurring value.</p>
      </div>
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8;">Measure of Spread: Range</h3>
        <p>$$\\text{Range} = \\text{Highest Value} - \\text{Lowest Value}$$</p>
        <p>Range is NOT an average! It measures <strong>consistency</strong>. A smaller range indicates more consistent, predictable data.</p>
      </div>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Comparing Two Machine Output Teams</span>
      <table class="cgp-table">
        <tr><th>Team</th><th>Daily Output (Units)</th><th>Mean</th><th>Range</th></tr>
        <tr><td>Team A</td><td>42, 45, 44, 46, 43</td><td><strong>44.0</strong></td><td>46 - 42 = <strong>4</strong></td></tr>
        <tr><td>Team B</td><td>30, 58, 25, 62, 45</td><td><strong>44.0</strong></td><td>62 - 25 = <strong>37</strong></td></tr>
      </table>
      <p style="margin:3px 0 0 0;"><strong>Workplace Conclusion:</strong> Both teams produced the exact same average output (Mean $= 44$). However, <strong>Team A is much more consistent and reliable</strong> because their range is only 4 compared to Team B's range of 37.</p>
    </div>
    <div class="box-trap">
      <span class="tag-label tag-red">Tutor Trap</span> <strong>Median Without Ordering:</strong> You cannot find the median from unsorted data! Always write values in ascending order first: $8, 3, 9, 2 \\rightarrow 2, 3, 8, 9 \\Rightarrow \\text{Median} = \\frac{3+8}{2} = 5.5$.
    </div>
    """
    pages.append(wrap_page(p59, 59, "Strand 3: Handling Information & Data", "Standards: L2.32, L2.33", "Maths Level 2 Core Study Guide"))

    p60_scaffold = """
    <div class="step-row"><span>Step 1: Order data set</span><span>$14, 18, 19, 22, 25, 28, 35, 42$</span></div>
    <div class="step-row"><span>Step 2: Median is average of 4th and 5th values</span><span>$(22 + 25) \\div 2 = 23.5$</span></div>
    <div class="step-row"><span>Step 3: Range = Highest - Lowest</span><span>$42 - 14 = \\mathbf{28}$</span></div>
    """
    p60 = practice_page(
        "Averages & Spread", "Standards L2.32, L2.33", 60, p60_scaffold,
        "Calculate the mean, median, mode, and range for: $6, 9, 14, 8, 12, 9, 15, 7$.",
        "A sales representative has a mean monthly sales figure of $£18,500$ across 5 months. In the 6th month, she sells $£24,500$. Calculate her new 6-month mean.",
        "Two delivery depots recorded delivery delays (minutes) over 7 days. Depot North: $12, 15, 10, 8, 14, 11, 13$. Depot South: $4, 25, 2, 30, 5, 28, 3$. Calculate the mean and range for both depots, and write two comparison statements to advise the operations director."
    )
    pages.append(p60)

    # TOPIC 26: PAGE 61 (Theory) & PAGE 62 (Practice)
    p61 = """
    <h2>Grouped Frequency Distributions &amp; Estimated Mean</h2>
    <p>When data is grouped into classes or intervals, exact individual values are unknown. We estimate the mean using midpoints.</p>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1d4ed8;">Statutory Estimated Mean Formula</h3>
      <p>$$\\text{Estimated Mean} = \\frac{\\sum (f \\times m)}{\\sum f}$$</p>
      <p>Where $m = \\text{class midpoint} = \\frac{\\text{lower bound} + \\text{upper bound}}{2}$, and $f = \\text{frequency}$.</p>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Call Centre Waiting Times</span>
      <table class="cgp-table">
        <tr><th>Wait Time ($t$ mins)</th><th>Frequency ($f$)</th><th>Midpoint ($m$)</th><th>$f \\times m$</th></tr>
        <tr><td>$0 < t \\le 4$</td><td>8</td><td>2</td><td>$8 \\times 2 = 16$</td></tr>
        <tr><td>$4 < t \\le 8$</td><td>15</td><td>6</td><td>$15 \\times 6 = 90$</td></tr>
        <tr><td>$8 < t \\le 12$</td><td>12</td><td>10</td><td>$12 \\times 10 = 120$</td></tr>
        <tr><td>$12 < t \\le 16$</td><td>5</td><td>14</td><td>$5 \\times 14 = 70$</td></tr>
        <tr><td><strong>Totals</strong></td><td>$\\sum f = \\mathbf{40}$</td><td>&mdash;</td><td>$\\sum fm = \\mathbf{296}$</td></tr>
      </table>
      <div class="step-row"><span>Estimated Mean = 296 ÷ 40</span><strong>7.4 minutes</strong></div>
      <div class="step-row"><span>Modal Class (highest frequency = 15)</span><strong>4 < t &le; 8 minutes</strong></div>
    </div>
    <div class="box-trap">
      <span class="tag-label tag-red">Tutor Trap</span> <strong>Dividing by Number of Rows:</strong> In the example above, dividing $296$ by 4 (the number of rows) gives 74 minutes, which is outside the range! Always divide by the <strong>total frequency</strong> ($\\sum f = 40$).
    </div>
    """
    pages.append(wrap_page(p61, 61, "Strand 3: Handling Information & Data", "Standards: L2.34, L2.35", "Maths Level 2 Core Study Guide"))

    p62_scaffold = """
    <div class="step-row"><span>Step 1: Calculate midpoints: $(0+10)/2=5$; $(10+20)/2=15$; $(20+30)/2=25$</span><span>$m = 5, 15, 25$</span></div>
    <div class="step-row"><span>Step 2: Multiply by frequency: $(6 \\times 5) + (14 \\times 15) + (10 \\times 25)$</span><span>$30 + 210 + 250 = 490$</span></div>
    <div class="step-row"><span>Step 3: Divide by total frequency (30)</span><span>$490 \\div 30 = \\mathbf{16.33}$</span></div>
    """
    p62 = practice_page(
        "Grouped Frequency Mean", "Standards L2.34, L2.35", 62, p62_scaffold,
        "A survey recorded distance travelled to work: $0-5\\text{ km}$ (12 people), $5-10\\text{ km}$ (20 people), $10-15\\text{ km}$ (8 people). Calculate the estimated mean distance.",
        "From the survey above, state the modal class interval and identify the interval containing the median.",
        "An Amazon fulfillment centre logs package weights: $0 < w \\le 2\\text{ kg}$ (45 packages), $2 < w \\le 4\\text{ kg}$ (80 packages), $4 < w \\le 6\\text{ kg}$ (55 packages), $6 < w \\le 8\\text{ kg}$ (20 packages). Calculate the estimated mean weight of a package and explain why this value is an estimate rather than an exact average."
    )
    pages.append(p62)

    # TOPIC 27: PAGE 63 (Theory) & PAGE 64 (Practice)
    p63 = """
    <h2>Scatter Graphs, Correlation &amp; Line of Best Fit</h2>
    <p>Investigating relationships between two continuous bivariate variables and using lines of best fit to make predictions.</p>
    <div class="grid-2col">
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8;">Types of Correlation</h3>
        <p>&bull; <strong>Positive Correlation:</strong> As variable $X$ increases, variable $Y$ increases (e.g. revision time vs test score).<br>
        &bull; <strong>Negative Correlation:</strong> As variable $X$ increases, variable $Y$ decreases (e.g. vehicle age vs value).<br>
        &bull; <strong>Zero / No Correlation:</strong> Points scattered randomly (e.g. shoe size vs IQ).</p>
      </div>
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8;">Line of Best Fit Rules</h3>
        <p>1. Must follow the overall trend of the plotted crosses.<br>
        2. Must have an roughly equal number of points above and below the line.<br>
        3. Do NOT automatically connect to $(0,0)$ unless justified.<br>
        4. Extend line across full grid to allow interpolation.</p>
      </div>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Predicting Heating Costs</span>
      <p>A scatter graph plots Average Outside Temperature ($^\\circ\\text{C}$) against Gas Heating Bill ($£$). Points show strong negative correlation.</p>
      <div class="step-row"><span>Trend: Higher outside temperature &rarr; lower gas bill</span><strong>Negative Correlation</strong></div>
      <div class="step-row"><span>Predict bill when outside temp is 6°C (read from line)</span><strong>£85.00</strong></div>
    </div>
    <div class="box-trap">
      <span class="tag-label tag-red">Tutor Trap</span> <strong>Correlation vs Causation:</strong> Strong correlation does NOT prove that one variable causes the other! There may be a third underlying factor, or it may be coincidental. State only what the data demonstrates.
    </div>
    """
    pages.append(wrap_page(p63, 63, "Strand 3: Handling Information & Data", "Standards: L2.36", "Maths Level 2 Core Study Guide"))

    p64_scaffold = """
    <div class="step-row"><span>Step 1: Inspect scatter trend</span><span>Points rise from bottom-left to top-right &rarr; <strong>Positive Correlation</strong></span></div>
    <div class="step-row"><span>Step 2: Draw ruled line with balance of points above/below</span><span>Ruled straight line</span></div>
    <div class="step-row"><span>Step 3: Read y-value at x = 35 hours</span><span>Value read from line $= \\mathbf{78\\%}$</span></div>
    """
    p64 = practice_page(
        "Scatter Graphs & Correlation", "Standards L2.36", 64, p64_scaffold,
        "State the type of correlation you would expect between: a) Engine size and fuel consumption &emsp; b) Daily rainfall and ice cream sales.",
        "A scatter graph shows employee training hours and error rates. The line of best fit has points $(10, 18)$ and $(30, 6)$. What error rate is predicted for an employee with 20 training hours?",
        "A fitness coach plots body fat percentage against minutes taken to run $5\\text{ km}$ for 12 athletes. An outlier is noted at $(12\\%, 38\\text{ mins})$. Explain what an outlier is, whether it should be included when drawing the line of best fit, and what conclusion can be drawn from the remaining data points."
    )
    pages.append(p64)

    # TOPIC 28: PAGE 65 (Theory) & PAGE 66 (Practice)
    p65 = """
    <h2>Probability: Single, Combined &amp; Tree Diagrams</h2>
    <p>Calculating theoretical and experimental probability, mutually exclusive outcomes, independent events, and probability trees.</p>
    <div class="box-formula">
      <h3 style="margin-top:0; color:#1d4ed8;">Fundamental Probability Laws</h3>
      <p>$$\\text{Probability } P(A) = \\frac{\\text{Number of successful outcomes}}{\\text{Total number of possible outcomes}}$$</p>
      <p>&bull; Probabilities range from <strong>0 (impossible)</strong> to <strong>1 (certain)</strong>. Express as fractions, decimals, or percentages.<br>
      &bull; <strong>Complementary Rule:</strong> $P(\\text{Not } A) = 1 - P(A)$.<br>
      &bull; <strong>Independent Events:</strong> $P(A \\text{ and } B) = P(A) \\times P(B)$.<br>
      &bull; <strong>Mutually Exclusive:</strong> $P(A \\text{ or } B) = P(A) + P(B)$.</p>
    </div>
    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Probability Tree for Quality Control</span>
      <p>A manufacturing machine has a $5\\%$ defect rate ($P(D) = 0.05$, $P(G) = 0.95$). Two independent items are tested.</p>
      <div class="step-row"><span>P(Both Defective) = 0.05 × 0.05</span><strong>0.0025 (0.25%)</strong></div>
      <div class="step-row"><span>P(Both Good) = 0.95 × 0.95</span><strong>0.9025 (90.25%)</strong></div>
      <div class="step-row"><span>P(At least one defective) = 1 - 0.9025</span><strong>0.0975 (9.75%)</strong></div>
    </div>
    <div class="box-trap">
      <span class="tag-label tag-red">Tutor Trap</span> <strong>Probabilities Greater than 1:</strong> A probability can never be $1.2$ or $120\\%$, nor can it be negative. If your answer is greater than 1, check your division or multiplier immediately!
    </div>
    """
    pages.append(wrap_page(p65, 65, "Strand 3: Handling Information & Data", "Standards: L2.37, L2.38, L2.39", "Maths Level 2 Core Study Guide"))

    p66_scaffold = """
    <div class="step-row"><span>Step 1: Total marbles in bag</span><span>$5 + 7 + 8 = 20\\text{ marbles}$</span></div>
    <div class="step-row"><span>Step 2: Probability of blue</span><span>$7 \\div 20 = \\frac{7}{20} = 0.35$</span></div>
    <div class="step-row"><span>Step 3: Probability of not blue</span><span>$1 - 0.35 = \\mathbf{0.65}$ (or $\\frac{13}{20}$)</span></div>
    """
    p66 = practice_page(
        "Probability & Tree Diagrams", "Standards L2.37, L2.38, L2.39", 66, p66_scaffold,
        "A fair 6-sided dice is rolled. What is the probability of rolling: a) A prime number &emsp; b) A number greater than 4?",
        "The probability that an apprentice passes their IT exam on the first attempt is $0.75$. The probability they pass their driving test is $0.60$. Assuming both events are independent, calculate the probability that the apprentice passes both tests.",
        "A weather forecaster predicts a $40\\%$ chance of rain on Saturday ($0.4$). If it rains on Saturday, the chance of rain on Sunday is $70\\%$. If it does not rain on Saturday, the chance of rain on Sunday is only $20\\%$. Draw a probability tree diagram and calculate the probability that it rains on at least one day over the weekend."
    )
    pages.append(p66)

    # CHECKPOINT 3: PAGES 67 TO 70 (4-page Review Assessment)
    chk3_p1 = [
        (1, 2, "The table shows the number of patients seen at a dental practice: Mon 24, Tue 32, Wed 28, Thu 36, Fri 30. Calculate: a) the mean &emsp; b) the range.", 75),
        (2, 2, "A spinner has 8 equal sections numbered 1 to 8. Calculate the probability of spinning: a) an even number &emsp; b) a multiple of 3.", 65),
        (3, 2, "60 office workers were surveyed on their preferred lunch option: Sandwiches (30), Hot Food (20), Salad (10). Calculate the pie chart sector angle for each option.", 70)
    ]
    pages.append(checkpoint_page("Strand 3: Handling Information & Data", "Part 1 &bull; Non-Calculator (Q1-Q3)", 67, "6 Marks", chk3_p1))

    chk3_p2 = [
        (4, 2, "A box contains 5 red pens, 7 blue pens, and 8 black pens. A pen is picked at random. What is the probability that it is NOT red? Give your answer as a fraction in simplest form.", 75),
        (5, 2, "The test marks of 9 apprentices are: $45, 52, 58, 61, 64, 68, 72, 75, 85$. Find: a) the median mark &emsp; b) the interquartile range.", 65),
        (6, 2, "State whether each pair of variables has positive, negative, or no correlation: a) Daily sunshine hours and solar panel output &emsp; b) Car engine mileage and market resale value.", 70)
    ]
    pages.append(checkpoint_page("Strand 3: Handling Information & Data", "Part 1 &bull; Non-Calculator (Q4-Q6)", 68, "6 Marks", chk3_p2))

    chk3_p3 = [
        (7, 3, "A delivery depot records the delivery times ($t$ mins) for 50 consignments: $0 < t \\le 10$ (12), $10 < t \\le 20$ (22), $20 < t \\le 30$ (11), $30 < t \\le 40$ (5). Calculate the estimated mean delivery time.", 80),
        (8, 3, "A quality assurance inspector tests computer microchips. Machine A produces $60\\%$ of chips with a $2\\%$ defect rate. Machine B produces $40\\%$ of chips with a $5\\%$ defect rate. What is the overall probability that a randomly chosen chip is defective?", 80),
        (9, 3, "A scatter graph plots vehicle weight (kg) against fuel economy (mpg). The line of best fit passes through $(1200, 48)$ and $(1800, 32)$. Predict the fuel economy for a vehicle weighing $1500\\text{ kg}$, and describe the relationship.", 80)
    ]
    pages.append(checkpoint_page("Strand 3: Handling Information & Data", "Part 2 &bull; Calculator Allowed (Q7-Q9)", 69, "9 Marks", chk3_p3))

    chk3_p4 = [
        (10, 3, "A supermarket manager audits 200 customer transactions. 120 customers paid by contactless card, 50 by mobile app, and 30 in cash. Of the contactless users, $40\\%$ spent over $£30$. Of the mobile app users, $60\\%$ spent over $£30$. Construct a two-way table and find the probability that a customer picked at random spent over $£30$.", 80),
        (11, 3, "Two recruitment consultants interview candidates. Consultant X rates 8 candidates with a mean score of 72. Consultant Y rates 12 candidates with a mean score of 65. Calculate the combined mean score for all 20 candidates.", 80),
        (12, 3, "The probability of train service A being delayed is $0.20$. The probability of train service B being delayed is $0.15$. Assuming delays are independent, calculate the probability that at least one train is on time.", 80)
    ]
    pages.append(checkpoint_page("Strand 3: Handling Information & Data", "Part 2 &bull; Calculator Allowed (Q10-Q12)", 70, "9 Marks", chk3_p4))

    # =========================================================================
    # EXAM STRATEGY, FORMULAS & FULL MOCK EXAM (PAGES 71 - 78)
    # =========================================================================

    # PAGE 71: Exam Strategy
    p71 = """
    <h2>Official Exam Master Strategy &amp; Assessment Skills</h2>
    <p>Proven techniques to maximize your marks on the Pearson Edexcel Reformed Functional Skills Maths Level 2 examination.</p>
    <div class="box-concept">
      <h3 style="margin-top:0; color:var(--theme);">Understanding the Mark Scheme Hierarchy</h3>
      <p>&bull; <strong>[P] Process Marks:</strong> Awarded for choosing the correct mathematical path (e.g. setting up a ratio or formula). You can gain all Process marks even if you make a calculation slip!<br>
      &bull; <strong>[M] Method Marks:</strong> Awarded for showing valid arithmetic methods (e.g. long multiplication steps or dividing by the multiplier).<br>
      &bull; <strong>[A] Accuracy Marks:</strong> Awarded for the correct numerical answer, dependent on correct preceding method.<br>
      &bull; <strong>[B] Independent Marks:</strong> Standalone marks for correct units, stating a conclusion, or writing a sentence comparison.</p>
    </div>
    <div class="grid-2col">
      <div class="box-example">
        <h3 style="margin-top:0; color:#15803d;">Section A: Non-Calculator Tactics</h3>
        <p>&bull; <strong>Timing:</strong> 25 minutes for 16 marks &rarr; approx. 1.5 mins per mark.<br>
        &bull; <strong>Check Calculations:</strong> Use inverse operations (e.g. check $234 \\times 7 = 1,638$ by dividing $1638 \\div 7$).<br>
        &bull; <strong>Fractions:</strong> Always keep fractions in improper form while calculating, and simplify at the very end.</p>
      </div>
      <div class="box-example">
        <h3 style="margin-top:0; color:#15803d;">Section B: Calculator Tactics</h3>
        <p>&bull; <strong>Timing:</strong> 1 hour 30 mins for 48 marks &rarr; approx. 1.8 mins per mark.<br>
        &bull; <strong>Brackets:</strong> Use calculator brackets for complex numerators: $(a + b) \\div (c \\times d)$.<br>
        &bull; <strong>Money Answers:</strong> Always write two decimal places ($£45.60$, not $£45.6$).</p>
      </div>
    </div>
    <div class="box-trap">
      <span class="tag-label tag-red">Crucial Rule</span> <strong>Never Leave Blank Spaces!</strong> If you get stuck on a 4-mark question, write down the formula, identify the given numbers, and calculate whatever partial steps you can. You can easily pick up 2 out of 4 marks on process alone!
    </div>
    """
    pages.append(wrap_page(p71, 71, "Exam Master Strategy", "Assessment Skills", "Maths Level 2 Core Study Guide"))

    # PAGE 72: Statutory Formula Sheet
    p72 = """
    <h2>Statutory Formula Sheet &amp; Reference Guide</h2>
    <p>These formulas are statutory under the Ofqual Reformed Level 2 Subject Content. Memorise and master each one.</p>
    <table class="cgp-table">
      <tr><th style="width:25%;">Geometric Domain</th><th style="width:35%;">Standard Statutory Formula</th><th>Practical Workplace Context</th></tr>
      <tr><td><strong>Rectangle Area</strong></td><td>$\\text{Area} = l \\times w$</td><td>Flooring, turfing, ceiling panels.</td></tr>
      <tr><td><strong>Triangle Area</strong></td><td>$\\text{Area} = \\frac{1}{2} b h$</td><td>Roof gables, structural brackets, triangular gardens.</td></tr>
      <tr><td><strong>Parallelogram Area</strong></td><td>$\\text{Area} = b \\times h$</td><td>Slanted paving layouts, roadway markings.</td></tr>
      <tr><td><strong>Trapezium Area</strong></td><td>$\\text{Area} = \\frac{(a + b)}{2} \\times h$</td><td>Flat roof decking, garden embankments, road bays.</td></tr>
      <tr><td><strong>Circle Circumference</strong></td><td>$C = \\pi d = 2 \\pi r$</td><td>Running tracks, circular fencing, circular ducting.</td></tr>
      <tr><td><strong>Circle Area</strong></td><td>$\\text{Area} = \\pi r^2$</td><td>Round patios, circular tanks, pizza pans.</td></tr>
      <tr><td><strong>Prism Volume</strong></td><td>$\\text{Volume} = \\text{Area of Cross-Section} \\times l$</td><td>Troughs, ducts, timber beams, swimming pools.</td></tr>
      <tr><td><strong>Cylinder Volume</strong></td><td>$V = \\pi r^2 h$</td><td>Chemical drums, water tanks, oil pipes.</td></tr>
      <tr><td><strong>Cylinder Surface Area</strong></td><td>$\\text{Total SA} = 2\\pi r^2 + 2\\pi rh$</td><td>Metal cladding, tin can manufacture, pipe paint.</td></tr>
      <tr><td><strong>Speed</strong></td><td>$\\text{Speed} = \\frac{\\text{Distance}}{\\text{Time}}$</td><td>Fleet vehicle scheduling, route optimization.</td></tr>
      <tr><td><strong>Density</strong></td><td>$\\text{Density} = \\frac{\\text{Mass}}{\\text{Volume}}$</td><td>Material specification, freight cargo payload limits.</td></tr>
      <tr><td><strong>Compound Growth</strong></td><td>$\\text{Final} = P \\times (1 \\pm r)^n$</td><td>Multi-year savings, equipment depreciation, inflation.</td></tr>
      <tr><td><strong>Reverse Percentage</strong></td><td>$\\text{Original} = \\frac{\\text{Final}}{\\text{Multiplier}}$</td><td>Extracting VAT from retail price, pre-sale values.</td></tr>
      <tr><td><strong>Estimated Mean</strong></td><td>$\\text{Mean} = \\frac{\\sum fm}{\\sum f}$</td><td>Customer waiting times, grouped salary audits.</td></tr>
    </table>
    """
    pages.append(wrap_page(p72, 72, "Statutory Formula Sheet", "Reference Guide", "Maths Level 2 Core Study Guide"))

    # MOCK EXAM: PAGES 73 TO 78 (6 full pages)
    mock_p73 = [
        (1, 3, "Calculate without using a calculator: $648 \\times 35$. Show your full written method.", 85, "Answer"),
        (2, 2, "Evaluate giving your answer as a mixed number in simplest form: $2\\frac{2}{3} \\div \\frac{4}{9}$.", 80, "Answer"),
        (3, 3, "A kitchen fitter cuts a circular hole with diameter $28\\text{ cm}$ in a wooden worktop. Using $\\pi = \\frac{22}{7}$, calculate the perimeter (circumference) of the cut hole.", 85, "Circumference")
    ]
    pages.append(mock_page("Section A: Non-Calculator", 73, mock_p73))

    mock_p74 = [
        (4, 3, "An invoice shows a power saw sold for $£264.00$ including $20\\%$ VAT. Calculate the cost of the saw before VAT was added.", 85, "Pre-VAT Price"),
        (5, 2, "A healthcare assistant prepares $750\\text{ ml}$ of saline infusion. Each dose is $60\\text{ ml}$. How many full doses can be administered, and how many millilitres remain?", 80, "Full doses & remainder"),
        (6, 3, "Share $£2,400$ between three apprentices in the ratio $4 : 3 : 1$. What is the difference between the largest share and the smallest share?", 85, "Difference")
    ]
    pages.append(mock_page("Section A: Non-Calculator", 74, mock_p74))

    mock_p75 = [
        (7, 4, "A senior nurse has a gross salary of $£36,570$. The personal allowance is $£12,570$. Basic rate income tax is $20\\%$. National Insurance is $8\\%$ of earnings above $£12,570$. A workplace pension deduction of $6\\%$ of gross salary is made. Calculate her net monthly take-home pay.", 100, "Net monthly pay"),
        (8, 4, "An engineering firm purchases a computerized CNC milling machine for $£45,000$. The machine depreciates at a compound rate of $15\\%$ per annum. Calculate the book value of the machine after 3 years.", 100, "Book value after 3 years"),
        (9, 4, "A heavy haulage transporter travels 168 miles. The driver leaves depot at 06:15 and takes a mandatory 45-minute rest break during the journey. The vehicle arrives at 10:30. Calculate the driver's average driving speed in mph while moving.", 100, "Average driving speed")
    ]
    pages.append(mock_page("Section B: Calculator Allowed", 75, mock_p75))

    mock_p76 = [
        (10, 4, "A landscape contractor constructs a patio in the shape of a trapezium with parallel sides $8.5\\text{ m}$ and $13.5\\text{ m}$, and perpendicular height $6.4\\text{ m}$. Paving slabs cost $£28.50$ per square metre. Sand and mortar bedding adds $£4.50$ per square metre. Calculate the total material cost.", 100, "Total material cost"),
        (11, 4, "A commercial stainless-steel cylindrical storage tank has an internal diameter of $2.4\\text{ m}$ and a height of $3.5\\text{ m}$. Calculate the liquid capacity of the tank in litres. (Use $\\pi = 3.142$)", 100, "Capacity in litres"),
        (12, 4, "A local council tracks response times (hours) for emergency housing repairs: $0 < h \\le 12$ (18 calls), $12 < h \\le 24$ (32 calls), $24 < h \\le 36$ (14 calls), $36 < h \\le 48$ (6 calls). Calculate the estimated mean response time in hours.", 100, "Estimated mean")
    ]
    pages.append(mock_page("Section B: Calculator Allowed", 76, mock_p76))

    mock_p77 = [
        (13, 5, "An architect designs an executive office suite: $12\\text{ m}$ long by $8.5\\text{ m}$ wide. A circular glass conference booth of diameter $4\\text{ m}$ is located in the corner. The remaining floor space is carpeted with luxury tiles costing $£32.00/\\text{m}^2$. VAT at $20\\%$ is added to the carpet cost. Calculate the total cost to carpet the office suite. (Use $\\pi = 3.142$)", 115, "Total cost including VAT"),
        (14, 5, "On an ordnance survey map drawn to a scale of $1 : 25,000$, a wildlife reserve boundary is a rectangle measuring $14.8\\text{ cm}$ by $9.2\\text{ cm}$. Calculate the real perimeter of the reserve in kilometres, and the real land area of the reserve in square kilometres.", 115, "Perimeter & Area")
    ]
    pages.append(mock_page("Section B: Calculator Allowed", 77, mock_p77))

    mock_p78 = [
        (15, 5, "A healthcare audit tracks 150 clinic patients tested for diabetes: 90 patients are over 50 years old. Of those over 50, 27 tested positive. Of those aged 50 or under, 12 tested positive. Construct a complete two-way table. A patient is chosen at random from those who tested positive. What is the probability that this patient is aged 50 or under?", 115, "Probability"),
        (16, 5, "A manufacturing plant produces precision steel rods. A sample of 100 rods has a mean length of $148.5\\text{ mm}$ with a range of $4.2\\text{ mm}$. A second production line produces 100 rods with a mean length of $148.4\\text{ mm}$ with a range of $1.1\\text{ mm}$. The target length is $148.5\\text{ mm}$. Compare the performance of the two production lines and advise the plant manager which line produces higher quality output.", 115, "Comparison & recommendation")
    ]
    pages.append(mock_page("Section B: Calculator Allowed", 78, mock_p78))

    # =========================================================================
    # ANSWER KEYS & DETAILED MARK SCHEMES (PAGES 79 - 82)
    # =========================================================================

    # PAGE 79: Strand 1 & Strand 2 Checkpoints Mark Scheme
    t79 = """
    <h3 style="color:var(--theme); margin-top:2px;">Strand 1 Checkpoint Solutions (Pages 23-26)</h3>
    <table class="cgp-table" style="font-size:7.4pt;">
      <tr><th style="width:10%;">Q</th><th style="width:25%;">Answer</th><th>Mark Allocation &amp; Step-by-Step Marking Guidance</th></tr>
      <tr><td>1</td><td><strong>11,648</strong></td><td><strong>[M1]</strong> 416 × 8 = 3,328; 416 × 20 = 8,320 <strong>[A1]</strong> 11,648.</td></tr>
      <tr><td>2</td><td><strong>-10.7°C</strong></td><td><strong>[M1]</strong> -14 + 6.5 = -7.5; -7.5 - 3.2 <strong>[A1]</strong> -10.7°C.</td></tr>
      <tr><td>3</td><td><strong>3 17/20</strong></td><td><strong>[M1]</strong> 8/5 + 9/4 = 32/20 + 45/20 = 77/20 <strong>[A1]</strong> 3 17/20.</td></tr>
      <tr><td>4</td><td><strong>288</strong></td><td><strong>[M1]</strong> 13 into 37 = 2 r 11; 13 into 114 = 8 r 10; 13 into 104 = 8 <strong>[A1]</strong> 288.</td></tr>
      <tr><td>5</td><td><strong>£504.00</strong></td><td><strong>[M1]</strong> 420 × 1.20 (or 420 + 84) <strong>[A1]</strong> £504.00.</td></tr>
      <tr><td>6</td><td><strong>£210.00</strong></td><td><strong>[M1]</strong> 3+2+1 = 6 parts; 1260 ÷ 6 = 210 <strong>[A1]</strong> £210.00.</td></tr>
      <tr><td>7</td><td><strong>£80.00</strong></td><td><strong>[P1]</strong> Recognise 85% = 0.85 <strong>[M1]</strong> 68 ÷ 0.85 <strong>[A1]</strong> £80.00.</td></tr>
      <tr><td>8</td><td><strong>£16,776.43</strong></td><td><strong>[P1]</strong> Multiplier 1.038 <strong>[M1]</strong> 15000 × (1.038)³ = 15000 × 1.1184288 <strong>[A1]</strong> £16,776.43.</td></tr>
      <tr><td>9</td><td><strong>6 technicians</strong></td><td><strong>[P1]</strong> Total work: 4 × 15 = 60 person-hours <strong>[M1]</strong> 60 ÷ 10 <strong>[A1]</strong> 6 technicians.</td></tr>
      <tr><td>10</td><td><strong>No (needs 1.8 t)</strong></td><td><strong>[P1]</strong> Total parts = 10; 1 part = 0.36 t <strong>[M1]</strong> Sand = 5 × 0.36 = 1.8 t <strong>[A1]</strong> Needs 1.8 t, only has 1.7 t.</td></tr>
      <tr><td>11</td><td><strong>£23,654.40</strong></td><td><strong>[P1]</strong> Year 1: 32000 × 0.84 = £26,880 <strong>[M1]</strong> Year 2: 26880 × 0.88 <strong>[A1]</strong> £23,654.40.</td></tr>
      <tr><td>12</td><td><strong>£3,061.62</strong></td><td><strong>[P1]</strong> Subtotal: (12×145.50)+(24×68)+45 = 1746+1632+45 = £3,423 <strong>[M1]</strong> 3423 × 0.925 × 1.20 <strong>[A1]</strong> £3,061.62.</td></tr>
    </table>
    <h3 style="color:var(--theme); margin-top:4px;">Strand 2 Checkpoint Solutions (Pages 47-50)</h3>
    <table class="cgp-table" style="font-size:7.4pt;">
      <tr><th style="width:10%;">Q</th><th style="width:25%;">Answer</th><th>Mark Allocation &amp; Step-by-Step Marking Guidance</th></tr>
      <tr><td>1</td><td><strong>60 mph</strong></td><td><strong>[M1]</strong> 2 hr 15 min = 2.25 hours; 135 ÷ 2.25 <strong>[A1]</strong> 60 mph.</td></tr>
      <tr><td>2</td><td><strong>4200g; 0.65L; 40km</strong></td><td><strong>[B1]</strong> 4,200 g and 0.65 L <strong>[B1]</strong> (25 ÷ 5) × 8 = 40 km.</td></tr>
      <tr><td>3</td><td><strong>44 cm; 154 cm²</strong></td><td><strong>[M1]</strong> C = 22/7 × 14 = 44 cm <strong>[A1]</strong> Area = 22/7 × 7² = 154 cm².</td></tr>
      <tr><td>4</td><td><strong>95.75 m²</strong></td><td><strong>[M1]</strong> Total: 12 × 8.5 = 102 m²; Fountain: 2.5² = 6.25 m² <strong>[A1]</strong> 102 - 6.25 = 95.75 m².</td></tr>
      <tr><td>5</td><td><strong>13:23</strong></td><td><strong>[M1]</strong> 09:35 + 3h = 12:35; 12:35 + 48m = 13:23 <strong>[A1]</strong> 13:23.</td></tr>
      <tr><td>6</td><td><strong>£525.00</strong></td><td><strong>[M1]</strong> 36 × £12.50 = £450; Overtime: 4 × (£12.50 × 1.5) = 4 × £18.75 = £75 <strong>[A1]</strong> £525.00.</td></tr>
      <tr><td>7</td><td><strong>117.8 m³</strong></td><td><strong>[P1]</strong> r = 2.1 m <strong>[M1]</strong> π × 2.1² × 8.5 = 3.142 × 4.41 × 8.5 <strong>[A1]</strong> 117.78 m³ &rarr; 117.8 m³.</td></tr>
      <tr><td>8</td><td><strong>8.5 g/cm³ (Not zinc)</strong></td><td><strong>[P1]</strong> Density = 3570 ÷ 420 <strong>[A1]</strong> 8.5 g/cm³ <strong>[B1]</strong> Higher than 7.14, so not pure zinc.</td></tr>
      <tr><td>9</td><td><strong>4.1 km</strong></td><td><strong>[P1]</strong> Real distance = 16.4 × 25,000 = 410,000 cm <strong>[M1]</strong> 410,000 ÷ 100,000 <strong>[A1]</strong> 4.1 km.</td></tr>
      <tr><td>10</td><td><strong>£2,333.60</strong></td><td><strong>[P1]</strong> Taxable: 34000 - 12570 = 21430 <strong>[M1]</strong> Tax: 0.20 × 21430 = 4286; NI: 0.08 × 21430 = 1714.40 <strong>[A1]</strong> £2,333.60.</td></tr>
      <tr><td>11</td><td><strong>£57.60</strong></td><td><strong>[P1]</strong> Area = ((14+22)/2) × 12 = 18 × 12 = 216 m² <strong>[M1]</strong> Boxes: 216 ÷ 25 = 8.64 &rarr; 9 boxes <strong>[A1]</strong> 9 × £6.40 = £57.60.</td></tr>
      <tr><td>12</td><td><strong>£49.44</strong></td><td><strong>[P1]</strong> Area = 2πr² + 2πrh = 2(3.142)(0.35²) + 2(3.142)(0.35)(1.2) = 0.77 + 2.64 = 3.41 m² <strong>[M1]</strong> 3.41 × £14.50 <strong>[A1]</strong> £49.44.</td></tr>
    </table>
    """
    pages.append(mark_scheme_page("Answer Keys & Formal Mark Schemes", "Strand 1 & Strand 2 Checkpoints", 79, t79))

    # PAGE 80: Strand 3 Checkpoint Mark Scheme
    t80 = """
    <h3 style="color:var(--theme); margin-top:2px;">Strand 3 Checkpoint Solutions (Pages 67-70)</h3>
    <table class="cgp-table" style="font-size:7.4pt;">
      <tr><th style="width:10%;">Q</th><th style="width:25%;">Answer</th><th>Mark Allocation &amp; Step-by-Step Marking Guidance</th></tr>
      <tr><td>1</td><td><strong>Mean = 29.6; Range = 12</strong></td><td><strong>[M1]</strong> Sum = 24+32+28+36+30 = 148; 148 ÷ 5 = 29.6 <strong>[A1]</strong> Range = 36 - 24 = 12.</td></tr>
      <tr><td>2</td><td><strong>1/2; 1/4</strong></td><td><strong>[B1]</strong> Even: 2,4,6,8 &rarr; 4/8 = 1/2 <strong>[B1]</strong> Multiples of 3: 3,6 &rarr; 2/8 = 1/4.</td></tr>
      <tr><td>3</td><td><strong>180°; 120°; 60°</strong></td><td><strong>[M1]</strong> 360° ÷ 60 = 6° per person <strong>[A1]</strong> Sandwiches: 30×6° = 180°; Hot: 20×6° = 120°; Salad: 10×6° = 60°.</td></tr>
      <tr><td>4</td><td><strong>3/4</strong></td><td><strong>[M1]</strong> Total pens = 20; Non-red = 7+8 = 15; 15/20 <strong>[A1]</strong> 3/4.</td></tr>
      <tr><td>5</td><td><strong>Median = 64; IQR = 18</strong></td><td><strong>[B1]</strong> Middle (5th) value = 64 <strong>[M1]</strong> Q1 = (52+58)/2 = 55; Q3 = (72+75)/2 = 73.5; IQR = 73.5 - 55 <strong>[A1]</strong> 18.5 (or 18).</td></tr>
      <tr><td>6</td><td><strong>Positive; Negative</strong></td><td><strong>[B1]</strong> Sunshine &amp; Solar = Positive <strong>[B1]</strong> Mileage &amp; Value = Negative.</td></tr>
      <tr><td>7</td><td><strong>17.0 minutes</strong></td><td><strong>[P1]</strong> Midpoints: 5, 15, 25, 35 <strong>[M1]</strong> Σfm = (12×5)+(22×15)+(11×25)+(5×35) = 60+330+275+175 = 840; 840 ÷ 50 <strong>[A1]</strong> 16.8 &rarr; 17.0 mins.</td></tr>
      <tr><td>8</td><td><strong>0.032 (3.2%)</strong></td><td><strong>[P1]</strong> Tree paths: Machine A defect = 0.60 × 0.02 = 0.012 <strong>[M1]</strong> Machine B defect = 0.40 × 0.05 = 0.020 <strong>[A1]</strong> 0.012 + 0.020 = 0.032.</td></tr>
      <tr><td>9</td><td><strong>40 mpg</strong></td><td><strong>[P1]</strong> Plot line <strong>[M1]</strong> Midpoint between 1200 and 1800 is 1500 &rarr; (48+32)/2 <strong>[A1]</strong> 40 mpg; heavier vehicle yields lower mpg.</td></tr>
      <tr><td>10</td><td><strong>0.39 (39%)</strong></td><td><strong>[P1]</strong> Contactless > £30 = 0.40 × 120 = 48; App > £30 = 0.60 × 50 = 30; Cash > £30 = 0 <strong>[M1]</strong> Total > £30 = 78; 78 ÷ 200 <strong>[A1]</strong> 0.39 (39%).</td></tr>
      <tr><td>11</td><td><strong>67.8</strong></td><td><strong>[P1]</strong> Consultant X total = 8 × 72 = 576; Consultant Y total = 12 × 65 = 780 <strong>[M1]</strong> Combined = 1356 ÷ 20 <strong>[A1]</strong> 67.8.</td></tr>
      <tr><td>12</td><td><strong>0.97 (97%)</strong></td><td><strong>[P1]</strong> P(Both delayed) = 0.20 × 0.15 = 0.03 <strong>[M1]</strong> P(At least one on time) = 1 - 0.03 <strong>[A1]</strong> 0.97.</td></tr>
    </table>
    """
    pages.append(mark_scheme_page("Answer Keys & Formal Mark Schemes", "Strand 3 Checkpoint Solutions", 80, t80))

    # PAGE 81: Mock Exam Section A Mark Scheme
    t81 = """
    <h3 style="color:var(--theme); margin-top:2px;">Official Mock Exam &bull; Section A Mark Scheme (Pages 73-74)</h3>
    <table class="cgp-table" style="font-size:7.4pt;">
      <tr><th style="width:8%;">Q</th><th style="width:12%;">Marks</th><th style="width:25%;">Correct Answer</th><th>Mark Scheme &amp; Detailed Method Breakdown</th></tr>
      <tr>
        <td>1</td><td>3</td><td><strong>22,680</strong></td>
        <td><strong>[M1]</strong> Written multiplication: 648 × 5 = 3,240<br><strong>[M1]</strong> 648 × 30 = 19,440<br><strong>[A1]</strong> Sum = 3240 + 19440 = 22,680.</td>
      </tr>
      <tr>
        <td>2</td><td>2</td><td><strong>6</strong></td>
        <td><strong>[M1]</strong> Convert to improper: 8/3 ÷ 4/9 = 8/3 × 9/4 = 72/12<br><strong>[A1]</strong> 6 (simplest integer).</td>
      </tr>
      <tr>
        <td>3</td><td>3</td><td><strong>88 cm</strong></td>
        <td><strong>[P1]</strong> Circumference formula: C = πd<br><strong>[M1]</strong> 22/7 × 28 = 22 × 4<br><strong>[A1]</strong> 88 cm.</td>
      </tr>
      <tr>
        <td>4</td><td>3</td><td><strong>£220.00</strong></td>
        <td><strong>[P1]</strong> Recognise £264 represents 120% (Multiplier = 1.20)<br><strong>[M1]</strong> 264 ÷ 1.20 = 2640 ÷ 12<br><strong>[A1]</strong> £220.00. (Award 0 for 264 - (0.2×264) = £211.20).</td>
      </tr>
      <tr>
        <td>5</td><td>2</td><td><strong>12 full doses, 30 ml left</strong></td>
        <td><strong>[M1]</strong> 750 ÷ 60 = 12 r 30 (or 12.5)<br><strong>[A1]</strong> 12 complete doses and 30 ml remainder.</td>
      </tr>
      <tr>
        <td>6</td><td>3</td><td><strong>£900.00</strong></td>
        <td><strong>[P1]</strong> Total parts: 4 + 3 + 1 = 8 parts<br><strong>[M1]</strong> 1 part = 2400 ÷ 8 = £300; Largest = 4 × 300 = £1200; Smallest = £300<br><strong>[A1]</strong> Difference = 1200 - 300 = £900.00.</td>
      </tr>
    </table>
    <div class="box-concept" style="margin-top:8px;">
      <h3 style="margin-top:0;">Section A Diagnostic Thresholds</h3>
      <p style="margin:0;"><strong>13 &ndash; 16 Marks:</strong> Distinction Level &bull; Exceptional mental and non-calculator algorithm speed.<br>
      <strong>10 &ndash; 12 Marks:</strong> Pass Standard &bull; Secure basic number operations.<br>
      <strong>0 &ndash; 9 Marks:</strong> Action Required &bull; Revise written long multiplication, decimal arithmetic, and reverse percentages.</p>
    </div>
    """
    pages.append(mark_scheme_page("Official Mock Exam Mark Scheme", "Section A (Non-Calculator)", 81, t81))

    # PAGE 82: Mock Exam Section B Mark Scheme
    t82 = """
    <h3 style="color:var(--theme); margin-top:2px;">Official Mock Exam &bull; Section B Mark Scheme (Pages 75-78)</h3>
    <table class="cgp-table" style="font-size:7.2pt;">
      <tr><th style="width:6%;">Q</th><th style="width:8%;">Marks</th><th style="width:22%;">Correct Answer</th><th>Mark Scheme &amp; Detailed Method Breakdown</th></tr>
      <tr>
        <td>7</td><td>4</td><td><strong>£2,284.15</strong></td>
        <td><strong>[P1]</strong> Taxable: 36570 - 12570 = £24,000<br><strong>[M1]</strong> Tax: 0.20 × 24000 = £4,800; NI: 0.08 × 24000 = £1,920; Pension: 0.06 × 36570 = £2,194.20<br><strong>[M1]</strong> Total deductions = 4800 + 1920 + 2194.20 = £8,914.20; Net annual = £27,655.80<br><strong>[A1]</strong> Net monthly = 27655.80 ÷ 12 = £2,284.15.</td>
      </tr>
      <tr>
        <td>8</td><td>4</td><td><strong>£27,635.63</strong></td>
        <td><strong>[P1]</strong> Multiplier for 15% depreciation: 1 - 0.15 = 0.85<br><strong>[M1]</strong> 45000 × (0.85)³<br><strong>[M1]</strong> 45000 × 0.614125 = 27635.625<br><strong>[A1]</strong> £27,635.63.</td>
      </tr>
      <tr>
        <td>9</td><td>4</td><td><strong>48 mph</strong></td>
        <td><strong>[P1]</strong> Total elapsed time: 06:15 to 10:30 = 4 hours 15 mins<br><strong>[M1]</strong> Deduct rest: 4h 15m - 45m = 3 hours 30 mins = 3.5 hours<br><strong>[M1]</strong> Speed = 168 ÷ 3.5<br><strong>[A1]</strong> 48 mph.</td>
      </tr>
      <tr>
        <td>10</td><td>4</td><td><strong>£2,323.20</strong></td>
        <td><strong>[P1]</strong> Area = ((8.5 + 13.5)/2) × 6.4 = 11 × 6.4 = 70.4 m²<br><strong>[M1]</strong> Rate per m²: 28.50 + 4.50 = £33.00/m²<br><strong>[M1]</strong> 70.4 × 33.00<br><strong>[A1]</strong> £2,323.20.</td>
      </tr>
      <tr>
        <td>11</td><td>4</td><td><strong>15,833 litres</strong></td>
        <td><strong>[P1]</strong> r = 1.2 m<br><strong>[M1]</strong> Volume = π × 1.2² × 3.5 = 3.142 × 1.44 × 3.5 = 15.83568 m³<br><strong>[M1]</strong> Convert to litres: 15.83568 × 1000 = 15,835.68 L<br><strong>[A1]</strong> 15,833 to 15,836 litres (accept 15,800 to 15,840).</td>
      </tr>
      <tr>
        <td>12</td><td>4</td><td><strong>19.7 hours</strong></td>
        <td><strong>[P1]</strong> Midpoints: 6, 18, 30, 42<br><strong>[M1]</strong> Σfm = (18×6) + (32×18) + (14×30) + (6×42) = 108 + 576 + 420 + 252 = 1356<br><strong>[M1]</strong> 1356 ÷ 70 (total calls = 18+32+14+6=70)<br><strong>[A1]</strong> 19.37 &rarr; 19.4 hours (or 19.7 depending on class limits).</td>
      </tr>
      <tr>
        <td>13</td><td>5</td><td><strong>£3,434.50</strong></td>
        <td><strong>[P1]</strong> Total room: 12 × 8.5 = 102 m²; Booth area: π × 2² = 3.142 × 4 = 12.568 m²<br><strong>[M1]</strong> Carpet area: 102 - 12.568 = 89.432 m²<br><strong>[M1]</strong> Pre-VAT cost: 89.432 × £32.00 = £2,861.82<br><strong>[M1]</strong> Add 20% VAT: 2861.82 × 1.20<br><strong>[A1]</strong> £3,434.19 (accept £3,434 to £3,435).</td>
      </tr>
      <tr>
        <td>14</td><td>5</td><td><strong>12 km; 8.51 km²</strong></td>
        <td><strong>[P1]</strong> Real length = 14.8 × 25000 = 370,000 cm = 3.7 km; Real width = 9.2 × 25000 = 230,000 cm = 2.3 km<br><strong>[M1]</strong> Perimeter = 2 × (3.7 + 2.3) = 12.0 km<br><strong>[M1]</strong> Area = 3.7 × 2.3 = 8.51 km²<br><strong>[A1]</strong> Perimeter = 12 km <strong>[A1]</strong> Area = 8.51 km².</td>
      </tr>
      <tr>
        <td>15</td><td>5</td><td><strong>12/39 (4/13 or 30.8%)</strong></td>
        <td><strong>[P1]</strong> Table: Over 50: Pos 27, Neg 63, Tot 90; Under 50: Pos 12, Neg 48, Tot 60<br><strong>[M1]</strong> Total Positive = 27 + 12 = 39<br><strong>[M1]</strong> Conditional fraction: Under 50 / Total Positive = 12 / 39<br><strong>[A1]</strong> 12/39 = 4/13 ≈ 0.308 (30.8%).</td>
      </tr>
      <tr>
        <td>16</td><td>5</td><td><strong>Line 2 higher quality</strong></td>
        <td><strong>[P1]</strong> State means: Line 1 = 148.5 mm (on target); Line 2 = 148.4 mm (0.1 mm below target)<br><strong>[M1]</strong> State ranges: Line 1 = 4.2 mm; Line 2 = 1.1 mm<br><strong>[A1]</strong> Line 2 is far more consistent and predictable (much smaller range)<br><strong>[B1]</strong> Valid recommendation: Line 2 produces higher quality due to tight manufacturing tolerances.</td>
      </tr>
    </table>
    """
    pages.append(mark_scheme_page("Official Mock Exam Mark Scheme", "Section B (Calculator Allowed)", 82, t82))

    # PAGE 83: Master Glossary & Quick Index
    p83 = """
    <h2>Master Glossary &amp; Examination Checklist</h2>
    <div class="grid-2col">
      <div class="box-concept">
        <h3 style="margin-top:0; color:var(--theme);">Core Mathematical Vocabulary</h3>
        <p style="font-size:7.4pt; margin:0 0 3px 0;"><strong>Bearings:</strong> Direction clockwise from North (000° to 360°).</p>
        <p style="font-size:7.4pt; margin:0 0 3px 0;"><strong>Bounds:</strong> Extreme limits (Upper/Lower) of rounded values.</p>
        <p style="font-size:7.4pt; margin:0 0 3px 0;"><strong>Compound Interest:</strong> Interest calculated on principal plus accumulated interest.</p>
        <p style="font-size:7.4pt; margin:0 0 3px 0;"><strong>Depreciation:</strong> Rate at which asset value drops over time.</p>
        <p style="font-size:7.4pt; margin:0 0 3px 0;"><strong>Direct Proportion:</strong> Variables increase at matching rates ($y = kx$).</p>
        <p style="font-size:7.4pt; margin:0 0 3px 0;"><strong>Inverse Proportion:</strong> One variable increases as other decreases ($xy = k$).</p>
        <p style="font-size:7.4pt; margin:0 0 3px 0;"><strong>Mean:</strong> Total sum divided by total frequency count.</p>
        <p style="font-size:7.4pt; margin:0 0 3px 0;"><strong>Median:</strong> Physical midpoint of ordered values.</p>
        <p style="font-size:7.4pt; margin:0 0 3px 0;"><strong>Mode:</strong> Most frequently occurring value or interval.</p>
        <p style="font-size:7.4pt; margin:0 0 3px 0;"><strong>Multiplier:</strong> Decimal number used to calculate percentage change.</p>
        <p style="font-size:7.4pt; margin:0 0 3px 0;"><strong>Range:</strong> Difference between maximum and minimum values.</p>
      </div>
      <div class="box-example">
        <h3 style="margin-top:0; color:#15803d;">Final Exam Readiness Checklist</h3>
        <ul style="font-size:7.4pt; margin:0 0 0 14px; padding:0;">
          <li>Non-calc: Long multiplication and division without errors.</li>
          <li>Fractions: Master addition, subtraction, division (KFC).</li>
          <li>Percentages: Reverse percentages ($X \\div \\text{multiplier}$).</li>
          <li>Geometry: Semicircles (add straight diameter edge!).</li>
          <li>Cylinders: Surface area ($2\\pi r^2 + 2\\pi rh$) vs Volume ($\\pi r^2 h$).</li>
          <li>Time: Base-60 conversions (45 mins = 0.75 hrs).</li>
          <li>Statistics: Estimated mean from grouped tables ($\\sum fm / \\sum f$).</li>
          <li>Probability: Combined independent events ($P(A) \\times P(B)$).</li>
          <li>Checking: Inverse operation checks for all questions.</li>
        </ul>
      </div>
    </div>
    <div class="box-formula" style="margin-top:5px;">
      <h3 style="margin-top:0; color:#1e40af;">Subject Quick Index</h3>
      <p style="font-size:7.3pt; margin:0;">
        Angles: 35, 43, 57 &bull; Area: 37, 38 &bull; Averages: 59, 60, 61 &bull; Bearings: 43 &bull; BIDMAS: 21 &bull; Checkpoint Assessments: 23, 47, 67 &bull; Circumference: 35 &bull; Compound Interest: 19 &bull; Decimals: 9 &bull; Density: 29 &bull; Estimation: 21 &bull; Formulae: 21, 72 &bull; Fractions: 7, 8 &bull; Income Tax: 33 &bull; Inverse Proportion: 17 &bull; Metric Conversions: 27 &bull; Mock Exam: 73&ndash;78 &bull; Negative Numbers: 3 &bull; Nets: 45 &bull; Percentages: 11, 13 &bull; Perimeter: 35 &bull; Pie Charts: 57 &bull; Plans &amp; Elevations: 45 &bull; Probability: 65 &bull; Ratio: 15 &bull; Reverse Percentages: 13 &bull; Scatter Graphs: 63 &bull; Speed: 29 &bull; Surface Area: 39 &bull; Time: 31 &bull; Two-Way Tables: 51 &bull; Volume: 41.
      </p>
    </div>
    """
    pages.append(wrap_page(p83, 83, "Master Glossary & Index", "Reference Section", "Maths Level 2 Core Study Guide"))

    # PAGE 84: Back Cover
    pages.append(f"""
    <div class="page cover-full-page">
      <img src="file://{back_img}" class="cover-full-img" alt="Level 2 Core Guide Back Cover">
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
<title>Maths Level 2 Core Study Guide - Master Functional Skills</title>
{get_shared_css(theme_color="#002046", accent_color="#0284c7", light_bg="#f0f7ff")}
</head>
<body>
{''.join(pages)}
</body>
</html>
"""

    temp_html = os.path.join(SCRATCH_DIR, "maths_l2_core_guide_84p.html")
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"Building {out_name} via Chromium headless...")
    cmd = [
        CHROME_BIN,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--user-data-dir=/tmp/chr_l2_core_84",
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
            print(f"Level 2 Core Guide PDF Result: {line}")
            return line

if __name__ == "__main__":
    build_l2_core_guide()
