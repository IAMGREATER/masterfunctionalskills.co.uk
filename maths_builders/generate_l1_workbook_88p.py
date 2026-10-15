#!/usr/bin/env python3
"""
books/maths_builders/generate_l1_workbook_88p.py
Constructs the complete 88-page MasterFunctionalSkills_Maths_Level_1_Companion_Workbook.pdf
Includes 34 topic practice drill pages, three 4-page Checkpoint Assessments,
3 Synoptic Workplace Case Studies, TWO Full Realistic Mock Exams (16 pages),
and 20 pages of comprehensive answer keys and formal marking schemes ([P1], [M1], [A1], [B1]).
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

def build_l1_companion_workbook():
    front_img = os.path.join(BOOKS_IMG_DIR, "maths_l1_companion_cover_page-1.png")
    back_img = os.path.join(BOOKS_IMG_DIR, "maths_l1_companion_cover_page-2.png")
    out_name = "MasterFunctionalSkills_Maths_Level_1_Companion_Workbook.pdf"
    target_downloads = os.path.join(DOWNLOADS_DIR, out_name)
    target_documents = os.path.join(DOCUMENTS_DIR, out_name)

    pages = []

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
        return wrap_page(content, page_num, f"{strand_name} Checkpoint Review", part_label, "Maths Level 1 Companion Practice Workbook")

    # Helper for Mock Exam pages
    def mock_page(mock_num, sec_title, page_num, q_list):
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
          <h2 style="margin:0; font-size:11pt; color:var(--theme);">Official Mock Exam {mock_num} &bull; {sec_title}</h2>
          <span style="font-size:7.5pt; font-weight:700; color:#475569;">Functional Skills Maths Level 1</span>
        </div>
        {items_html}
        """
        return wrap_page(content, page_num, f"Official Mock Exam {mock_num} &bull; {sec_title}", "Standard Exam Simulation", "Maths Level 1 Companion Practice Workbook")

    # Helper for Mark Scheme pages
    def mark_scheme_page(title, sub_title, page_num, tables_html):
        content = f"""
        <div style="border-bottom:1.5px solid var(--theme); padding-bottom:3px; margin-bottom:6px;">
          <h2 style="margin:0; font-size:11pt; color:var(--theme);">{title}</h2>
          <div style="font-size:7.5pt; color:#64748b;"><strong>{sub_title}</strong> &bull; Marking Codes: [P1] Process &bull; [M1] Method &bull; [A1] Accuracy &bull; [B1] Independent</div>
        </div>
        {tables_html}
        """
        return wrap_page(content, page_num, title, sub_title, "Maths Level 1 Companion Practice Workbook")

    # PAGE 1: Front Cover
    pages.append(f"""
    <div class="page cover-full-page">
      <img src="file://{front_img}" class="cover-full-img" alt="Level 1 Companion Workbook Front Cover">
    </div>
    """)

    # PAGE 2: Inside Cover & How to Use this Workbook
    p2 = """
    <h1>Maths Level 1 Companion Practice Workbook</h1>
    <div style="font-size:8.5pt; color:#475569; margin-bottom:8px;"><strong>Companion Practice Resource:</strong> Master Functional Skills &bull; Pearson Edexcel Functional Skills Mathematics Level 1</div>

    <div class="box-concept">
      <h3 style="margin-top:0;">Active Pen-to-Paper Learning</h3>
      <p>This companion practice workbook is created to build real mathematical confidence. Solving problems with a pen on paper trains your brain for exam day, developing accuracy, calculation speed, and clear presentation of workings.</p>
    </div>

    <h2>How This Workbook Is Structured</h2>
    <div class="grid-2col">
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8;">1. Graded Topic Practice</h3>
        <p>&bull; <strong>Warm-Up:</strong> Procedural arithmetic practice.<br>
        &bull; <strong>Workplace Applications:</strong> Practical scenarios from care, retail, and construction.<br>
        &bull; <strong>Exam Challenge:</strong> Realistic exam-style tasks.</p>
      </div>
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8;">2. Dedicated Workspaces</h3>
        <p>&bull; <strong>Ruled Lines:</strong> Clear lined spaces for written working.<br>
        &bull; <strong>5mm Squared Grids:</strong> Squared boxes for column arithmetic.<br>
        &bull; <strong>Answer Lines:</strong> Highlighted blanks with unit requirements.</p>
      </div>
    </div>

    <h2>Understanding Examiner Mark Scheme Codes</h2>
    <table class="cgp-table">
      <tr>
        <th style="width:20%;">Mark Code</th>
        <th style="width:25%;">Official Meaning</th>
        <th>What Examiners Look For in Your Working Out</th>
      </tr>
      <tr>
        <td><span class="mark-badge">[M1] / [M2]</span></td>
        <td><strong>Method Mark</strong></td>
        <td>Awarded for using a correct calculation method (e.g. column addition or bus stop division), even if a mental arithmetic slip occurs.</td>
      </tr>
      <tr>
        <td><span class="mark-badge">[A1] / [A2]</span></td>
        <td><strong>Accuracy Mark</strong></td>
        <td>Awarded for the correct numerical answer following correct method. Dependent on preceding method marks.</td>
      </tr>
      <tr>
        <td><span class="mark-badge">[B1] / [B2]</span></td>
        <td><strong>Independent Mark</strong></td>
        <td>Awarded for standalone facts, correct units stated, comparison conclusions, or correct graph labels.</td>
      </tr>
    </table>
    """
    pages.append(wrap_page(p2, 2, "Master Functional Skills &bull; Practice Workbook", "Workbook Overview", "Maths Level 1 Companion Practice Workbook"))

    # =========================================================================
    # MODULE 1: NUMBER & NUMBER SYSTEMS (PAGES 3 - 17)
    # 11 Practice Pages + 4 Checkpoint Pages
    # =========================================================================

    p3 = """
    <h2>Place Value, Ordering Numbers &amp; Negatives</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Standards: L1.1, L1.2 &bull; Whole numbers up to 1,000,000, thermometer temperatures &amp; bank balances</div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 1: Warm-Up Drills</span><span class="q-marks">[4 Marks]</span></div>
      <p>a) Write in figures: 'Forty-two thousand, five hundred and eight' &emsp; b) Write in words: $306,420$.<br>
      c) Put in order, coldest first: $+3^\\circ\\text{C}, -6^\\circ\\text{C}, -14^\\circ\\text{C}, +1^\\circ\\text{C}, -2^\\circ\\text{C}$.</p>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 2: Warehouse Cold Store Monitoring</span><span class="q-marks">[3 Marks]</span></div>
      <p>A cold storage room is at <strong>$-16^\\circ\\text{C}$</strong>. A refrigeration fault causes the temperature to rise by <strong>$9^\\circ\\text{C}$</strong>. What is the new temperature?</p>
      <div class="grid-workspace" style="height:55px;"><span class="workspace-hint">Show number line jump</span></div>
      <div class="answer-line">New Temperature: <span class="answer-blank"></span> °C [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 3: Bank Account Overdraft</span><span class="q-marks">[3 Marks]</span></div>
      <p>A bank balance is $-£240$. A customer pays in wages of $+£650$ and pays a phone bill of $£85$. Calculate the final balance.</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Show calculations</span></div>
      <div class="answer-line">Balance: £ <span class="answer-blank"></span> [M1, A1]</div>
    </div>
    """
    pages.append(wrap_page(p3, 3, "Module 1: Number & Number Systems", "Practice: Place Value", "Maths Level 1 Companion Practice Workbook"))

    p4 = """
    <h2>Addition &amp; Subtraction Column Methods</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Standards: L1.3 &bull; Column addition, carrying digits, column subtraction with borrowing</div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 1: Column Addition &amp; Subtraction Warm-Up</span><span class="q-marks">[4 Marks]</span></div>
      <p>Calculate without a calculator: a) $1,458 + 2,385$ &emsp; b) $4,000 - 1,675$.</p>
      <div class="grid-workspace" style="height:55px;"><span class="workspace-hint">Show vertical columns</span></div>
      <div class="answer-line">a) <span class="answer-blank" style="min-width:100px;"></span> &emsp; b) <span class="answer-blank" style="min-width:100px;"></span></div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 2: Hospital Supply Delivery</span><span class="q-marks">[3 Marks]</span></div>
      <p>A dispensary receives three boxes of medical masks: 450 in box A, 625 in box B, and 380 in box C. How many masks are there in total?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Add all three boxes</span></div>
      <div class="answer-line">Total Masks: <span class="answer-blank"></span> [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 3: Retail Stock Deduction</span><span class="q-marks">[3 Marks]</span></div>
      <p>A retailer had 1,500 laptops in the central warehouse. During November, 642 laptops were dispatched. How many laptops remain?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Show subtraction method</span></div>
      <div class="answer-line">Remaining: <span class="answer-blank"></span> laptops [M1, A1]</div>
    </div>
    """
    pages.append(wrap_page(p4, 4, "Module 1: Number & Number Systems", "Practice: Addition & Subtraction", "Maths Level 1 Companion Practice Workbook"))

    p5 = """
    <h2>Multiplication &amp; Bus Stop Division Non-Calc</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Standards: L1.3 &bull; Multi-digit column multiplication, bus stop division, inverse checks</div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 1: Written Calculation Warm-Up</span><span class="q-marks">[4 Marks]</span></div>
      <p>Calculate: a) $236 \\times 18$ &emsp; b) $952 \\div 7$.</p>
      <div class="grid-workspace" style="height:55px;"><span class="workspace-hint">Show full working</span></div>
      <div class="answer-line">a) <span class="answer-blank" style="min-width:100px;"></span> &emsp; b) <span class="answer-blank" style="min-width:100px;"></span></div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 2: Packaging Pallet Quantities</span><span class="q-marks">[3 Marks]</span></div>
      <p>A food factory packs 24 tins of soup per cardboard carton. A supermarket orders 35 cartons. How many tins is this in total?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Multiply 24 by 35</span></div>
      <div class="answer-line">Total Tins: <span class="answer-blank"></span> [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 3: Banquet Hall Seating Plan</span><span class="q-marks">[3 Marks]</span></div>
      <p>An event coordinator has 432 guests attending a charity gala. Each round table seats 8 guests. How many tables are required?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Divide 432 by 8</span></div>
      <div class="answer-line">Tables Needed: <span class="answer-blank"></span> [M1, A1]</div>
    </div>
    """
    pages.append(wrap_page(p5, 5, "Module 1: Number & Number Systems", "Practice: Multi & Division", "Maths Level 1 Companion Practice Workbook"))

    p6 = """
    <h2>Multiplying &amp; Dividing by 10, 100, 1000</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Standards: L1.3 &bull; Shifting decimal digits, place value patterns, zeros as placeholders</div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 1: Powers of 10 Warm-Up</span><span class="q-marks">[4 Marks]</span></div>
      <p>Calculate: a) $34 \\times 100$ &emsp; b) $5.8 \\times 10$ &emsp; c) $4,200 \\div 100$ &emsp; d) $65 \\div 10$.</p>
      <div class="answer-line">a) <span class="answer-blank" style="min-width:60px;"></span> b) <span class="answer-blank" style="min-width:60px;"></span> c) <span class="answer-blank" style="min-width:60px;"></span> d) <span class="answer-blank" style="min-width:60px;"></span></div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 2: Bulk Stationery Purchase</span><span class="q-marks">[3 Marks]</span></div>
      <p>A school buys 100 packs of dry-wipe markers at $£3.45$ per pack. How much does the school pay in total?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Shift decimal 2 places right</span></div>
      <div class="answer-line">Total Cost: £ <span class="answer-blank"></span> [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 3: Factory Production Line Sharing</span><span class="q-marks">[3 Marks]</span></div>
      <p>A bolt machine produces 8,500 washers. They are packed into 100 equal plastic bags. How many washers go in each bag?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Divide by 100</span></div>
      <div class="answer-line">Washers per Bag: <span class="answer-blank"></span> [M1, A1]</div>
    </div>
    """
    pages.append(wrap_page(p6, 6, "Module 1: Number & Number Systems", "Practice: Powers of 10", "Maths Level 1 Companion Practice Workbook"))

    p7 = """
    <h2>Order of Operations (BIDMAS) &amp; Expressions</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Standards: L1.11, L1.12 &bull; Precedence of brackets, division, multiplication, addition &amp; subtraction</div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 1: BIDMAS Warm-Up Drills</span><span class="q-marks">[4 Marks]</span></div>
      <p>Evaluate: a) $14 + 3 \\times 5$ &emsp; b) $(18 - 6) \\div 3$ &emsp; c) $25 - 4 \\times 2 + 1$ &emsp; d) $4^2 - 10$.</p>
      <div class="answer-line">a) <span class="answer-blank" style="min-width:60px;"></span> b) <span class="answer-blank" style="min-width:60px;"></span> c) <span class="answer-blank" style="min-width:60px;"></span> d) <span class="answer-blank" style="min-width:60px;"></span></div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 2: Equipment Hire Formula</span><span class="q-marks">[3 Marks]</span></div>
      <p>Tool hire cost: $\\text{Cost} = £30 + (£15 \\times \\text{days})$. Calculate the total hire cost for 4 days.</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Multiply days by rate first</span></div>
      <div class="answer-line">Hire Cost: £ <span class="answer-blank"></span> [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 3: Carpet Fitter Pricing Rule</span><span class="q-marks">[3 Marks]</span></div>
      <p>A carpet fitter charges: $\\text{Price} = £40\\text{ call-out} + (£12 \\times \\text{square metres carpeted})$. Room is $20\\text{ m}^2$. Find total charge.</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Substitute and calculate</span></div>
      <div class="answer-line">Total Charge: £ <span class="answer-blank"></span> [M1, A1]</div>
    </div>
    """
    pages.append(wrap_page(p7, 7, "Module 1: Number & Number Systems", "Practice: BIDMAS", "Maths Level 1 Companion Practice Workbook"))

    p8 = """
    <h2>Fractions: Equivalences &amp; Simplifying</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Standards: L1.5 &bull; Identifying equivalent fractions, dividing by HCF, simplest form</div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 1: Simplifying Fractions Warm-Up</span><span class="q-marks">[4 Marks]</span></div>
      <p>Simplify fully: a) $\\frac{14}{21}$ &emsp; b) $\\frac{20}{50}$ &emsp; c) $\\frac{18}{24}$ &emsp; d) $\\frac{15}{45}$.</p>
      <div class="answer-line">a) <span class="answer-blank" style="min-width:60px;"></span> b) <span class="answer-blank" style="min-width:60px;"></span> c) <span class="answer-blank" style="min-width:60px;"></span> d) <span class="answer-blank" style="min-width:60px;"></span></div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 2: Equivalence Grid Missing Values</span><span class="q-marks">[3 Marks]</span></div>
      <p>Find missing values: a) $\\frac{2}{3} = \\frac{?}{15}$ &emsp; b) $\\frac{5}{8} = \\frac{20}{?}$ &emsp; c) $\\frac{?}{10} = \\frac{12}{20}$.</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Find multiplier</span></div>
      <div class="answer-line">a) <span class="answer-blank" style="min-width:60px;"></span> b) <span class="answer-blank" style="min-width:60px;"></span> c) <span class="answer-blank" style="min-width:60px;"></span> [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 3: Ordering Fractions</span><span class="q-marks">[3 Marks]</span></div>
      <p>Put in order starting with the smallest: $\\frac{1}{2}, \\frac{3}{8}, \\frac{3}{4}, \\frac{5}{16}$. Show common denominator working.</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Convert all to 16ths</span></div>
      <div class="answer-line">Order: <span class="answer-blank" style="min-width:180px;"></span> [M1, A1]</div>
    </div>
    """
    pages.append(wrap_page(p8, 8, "Module 1: Number & Number Systems", "Practice: Fractions Basics", "Maths Level 1 Companion Practice Workbook"))

    p9 = """
    <h2>Fractions of Amounts</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Standards: L1.5 &bull; Divide by denominator, multiply by numerator, real workplace portions</div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 1: Rapid Fraction Calculations</span><span class="q-marks">[4 Marks]</span></div>
      <p>Calculate: a) $\\frac{1}{3}$ of $£45$ &emsp; b) $\\frac{1}{5}$ of $80\\text{ kg}$ &emsp; c) $\\frac{3}{4}$ of $£60$ &emsp; d) $\\frac{2}{7}$ of $35\\text{ m}$.</p>
      <div class="answer-line">a) £ <span class="answer-blank" style="min-width:50px;"></span> b) <span class="answer-blank" style="min-width:50px;"></span> kg c) £ <span class="answer-blank" style="min-width:50px;"></span> d) <span class="answer-blank" style="min-width:50px;"></span> m</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 2: Pharmacy Pill Inventory</span><span class="q-marks">[3 Marks]</span></div>
      <p>A pharmacy technician has 240 antibiotic capsules. In one morning, $\\frac{3}{8}$ are dispensed. How many capsules remain?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Calculate 3/8 then subtract</span></div>
      <div class="answer-line">Remaining: <span class="answer-blank"></span> capsules [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 3: Apprentice Monthly Budget</span><span class="q-marks">[3 Marks]</span></div>
      <p>An apprentice earns $£1,200$ per month. She spends $\\frac{1}{4}$ on rent and $\\frac{1}{3}$ on food and travel. How much is left?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Calculate each fraction</span></div>
      <div class="answer-line">Remaining: £ <span class="answer-blank"></span> [M1, A1]</div>
    </div>
    """
    pages.append(wrap_page(p9, 9, "Module 1: Number & Number Systems", "Practice: Fractions of Amounts", "Maths Level 1 Companion Practice Workbook"))

    p10 = """
    <h2>Decimals &amp; Workplace Financial Calculations</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Standards: L1.6 &bull; Adding and subtracting money, decimal place value, change calculations</div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 1: Decimal Arithmetic Drills</span><span class="q-marks">[4 Marks]</span></div>
      <p>Calculate: a) $15.45 + 8.90$ &emsp; b) $50 - 24.35$ &emsp; c) $6.4 \\times 5$ &emsp; d) $18.60 \\div 3$.</p>
      <div class="answer-line">a) <span class="answer-blank" style="min-width:60px;"></span> b) <span class="answer-blank" style="min-width:60px;"></span> c) <span class="answer-blank" style="min-width:60px;"></span> d) <span class="answer-blank" style="min-width:60px;"></span></div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 2: Cafe Till Receipt</span><span class="q-marks">[3 Marks]</span></div>
      <p>A customer buys: 2 coffees at $£2.85$ each, 1 sandwich for $£4.50$, and 1 muffin for $£2.20$. How much change from a $£20$ note?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Sum items and subtract from £20</span></div>
      <div class="answer-line">Change: £ <span class="answer-blank"></span> [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 3: Tradesperson Materials Invoice</span><span class="q-marks">[3 Marks]</span></div>
      <p>An electrician buys: $25\\text{ m}$ of cable at $£1.40/\\text{m}$, 4 switches at $£3.75$ each, and 1 junction box at $£6.50$. Find total cost.</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Show itemised costs</span></div>
      <div class="answer-line">Total Cost: £ <span class="answer-blank"></span> [M1, A1]</div>
    </div>
    """
    pages.append(wrap_page(p10, 10, "Module 1: Number & Number Systems", "Practice: Decimals & Money", "Maths Level 1 Companion Practice Workbook"))

    p11 = """
    <h2>Percentages: Benchmark Mental Finding &amp; Increases</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Standards: L1.7 &bull; Finding 10%, 25%, 50% and 5% without calculators, sales discounts</div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 1: Benchmark Percentage Drills</span><span class="q-marks">[4 Marks]</span></div>
      <p>Find: a) $50\\%$ of $£84$ &emsp; b) $25\\%$ of $60\\text{ kg}$ &emsp; c) $10\\%$ of $£350$ &emsp; d) $5\\%$ of $£180$.</p>
      <div class="answer-line">a) £ <span class="answer-blank" style="min-width:50px;"></span> b) <span class="answer-blank" style="min-width:50px;"></span> kg c) £ <span class="answer-blank" style="min-width:50px;"></span> d) £ <span class="answer-blank" style="min-width:50px;"></span></div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 2: Retail Clearance Discount</span><span class="q-marks">[3 Marks]</span></div>
      <p>A mountain bike originally costs $£320.00$. It is discounted by $25\\%$ in an autumn sale. What is the new sale price?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Divide by 4 then subtract</span></div>
      <div class="answer-line">Sale Price: £ <span class="answer-blank"></span> [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 3: Annual Salary Increment</span><span class="q-marks">[3 Marks]</span></div>
      <p>A care assistant earns $£21,000$ per year. She receives a $5\\%$ pay rise. What is her new annual salary?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Find 5% and add to salary</span></div>
      <div class="answer-line">New Salary: £ <span class="answer-blank"></span> [M1, A1]</div>
    </div>
    """
    pages.append(wrap_page(p11, 11, "Module 1: Number & Number Systems", "Practice: Percentages", "Maths Level 1 Companion Practice Workbook"))

    p12 = """
    <h2>Fractions, Decimals &amp; Percentages Equivalence</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Standards: L1.8 &bull; Converting between representations, ordering mixed FDP sets</div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 1: Complete Equivalence Table</span><span class="q-marks">[4 Marks]</span></div>
      <p>Fill in blanks: a) Fraction $\\frac{1}{2} =$ Decimal _________ = _________ %<br>
      b) Decimal $0.25 =$ Fraction _________ = _________ %</p>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 2: Comparing Different Formats</span><span class="q-marks">[3 Marks]</span></div>
      <p>Which is larger: <strong>$\\frac{3}{5}$</strong> or <strong>$65\\%$</strong>? Convert both to percentages or decimals to prove your answer.</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">3/5 = 6/10 = 60%</span></div>
      <div class="answer-line">Larger Value: <span class="answer-blank"></span> [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 3: Ordering Mixed FDP</span><span class="q-marks">[3 Marks]</span></div>
      <p>Put in order starting with smallest: $0.3, \\frac{1}{4}, 35\\%, 0.28, \\frac{2}{5}$.</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Convert all to percentages first</span></div>
      <div class="answer-line">Order: <span class="answer-blank" style="min-width:180px;"></span> [M1, A1]</div>
    </div>
    """
    pages.append(wrap_page(p12, 12, "Module 1: Number & Number Systems", "Practice: FDP Equivalence", "Maths Level 1 Companion Practice Workbook"))

    p13 = """
    <h2>Simple Ratio &amp; Recipe Scaling</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Standards: L1.9 &bull; Ratio sharing $a : b$, recipe multipliers, proportional quantities</div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 1: Ratio Sharing Warm-Up</span><span class="q-marks">[4 Marks]</span></div>
      <p>a) Share $£60$ in ratio $2 : 1$. &emsp; b) Share $40\\text{ kg}$ in ratio $3 : 5$.</p>
      <div class="grid-workspace" style="height:55px;"><span class="workspace-hint">Find 1 part</span></div>
      <div class="answer-line">a) <span class="answer-blank" style="min-width:100px;"></span> &emsp; b) <span class="answer-blank" style="min-width:100px;"></span></div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 2: Fruit Punch Recipe</span><span class="q-marks">[3 Marks]</span></div>
      <p>A party punch mixes orange juice and lemonade in ratio $3 : 2$. An event host makes $15\\text{ litres}$ of punch. How much orange juice is needed?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">5 parts total</span></div>
      <div class="answer-line">Orange Juice: <span class="answer-blank"></span> litres [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 3: Concrete Mortar Mixture</span><span class="q-marks">[3 Marks]</span></div>
      <p>A builder mixes sand and cement in ratio $4 : 1$. He uses $36\\text{ kg}$ of sand. How much cement must he add?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Sand is 4 parts</span></div>
      <div class="answer-line">Cement Needed: <span class="answer-blank"></span> kg [M1, A1]</div>
    </div>
    """
    pages.append(wrap_page(p13, 13, "Module 1: Number & Number Systems", "Practice: Simple Ratio", "Maths Level 1 Companion Practice Workbook"))

    # STRAND 1 CHECKPOINT ASSESSMENT (PAGES 14 TO 17: 4 full pages)
    chk1_p1 = [
        (1, 2, "Work out without a calculator: $418 \\times 16$. Show your full column method.", 75),
        (2, 2, "A bank account is overdrawn by $-£145$. A credit of $£500$ is added. What is the new balance?", 65),
        (3, 2, "Simplify fully: a) $\\frac{15}{20}$ &emsp; b) Convert $\\frac{2}{5}$ to a percentage.", 70)
    ]
    pages.append(checkpoint_page("Strand 1: Number & Number Systems", "Part 1 &bull; Non-Calculator (Q1-Q3)", 14, "6 Marks", chk1_p1))

    chk1_p2 = [
        (4, 2, "Divide 1,368 by 6 without a calculator. Show your bus stop division.", 75),
        (5, 2, "Evaluate: $15 - 3 \\times 4 + 2$.", 65),
        (6, 2, "Share $£140$ in the ratio $4 : 3$. What is the larger share?", 70)
    ]
    pages.append(checkpoint_page("Strand 1: Number & Number Systems", "Part 1 &bull; Non-Calculator (Q4-Q6)", 15, "6 Marks", chk1_p2))

    chk1_p3 = [
        (7, 3, "A microwave costs $£150$. It is discounted by $20\\%$ in a sale. What is the sale price?", 80),
        (8, 3, "A recipe for 4 people requires $320\\text{ g}$ of flour. How much flour is needed for 7 people?", 80),
        (9, 3, "A delivery depot has 400 parcels. In the morning they deliver $\\frac{5}{8}$ of them. How many parcels remain?", 80)
    ]
    pages.append(checkpoint_page("Strand 1: Number & Number Systems", "Part 2 &bull; Calculator Allowed (Q7-Q9)", 16, "9 Marks", chk1_p3))

    chk1_p4 = [
        (10, 3, "A painter charges: $£40\\text{ call-out} + (£25 \\times \\text{hours})$. He works for 5 hours. How much is the bill?", 80),
        (11, 3, "Pack A has 4 light bulbs for $£5.20$. Pack B has 6 bulbs for $£7.20$. Which pack is cheaper per bulb?", 80),
        (12, 3, "A gardener orders 18 paving slabs at $£8.50$ each. Delivery is $£20.00$. He has $£170.00$. Does he have enough money?", 80)
    ]
    pages.append(checkpoint_page("Strand 1: Number & Number Systems", "Part 2 &bull; Calculator Allowed (Q10-Q12)", 17, "9 Marks", chk1_p4))

    # =========================================================================
    # MODULE 2: MEASURES, SHAPE & SPACE (PAGES 18 - 34)
    # 13 Practice Pages + 4 Checkpoint Pages
    # =========================================================================

    p18 = """
    <h2>Metric Units of Length &amp; Conversions</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Standards: L1.17 &bull; Millimetres, centimetres, metres, kilometres</div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 1: Length Conversion Warm-Up</span><span class="q-marks">[4 Marks]</span></div>
      <p>Convert: a) $4.5\\text{ m}$ to cm &emsp; b) $250\\text{ cm}$ to m &emsp; c) $65\\text{ mm}$ to cm &emsp; d) $3.2\\text{ km}$ to m.</p>
      <div class="answer-line">a) <span class="answer-blank" style="min-width:60px;"></span> b) <span class="answer-blank" style="min-width:60px;"></span> c) <span class="answer-blank" style="min-width:60px;"></span> d) <span class="answer-blank" style="min-width:60px;"></span></div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 2: Joinery Skirting Trim</span><span class="q-marks">[3 Marks]</span></div>
      <p>A joiner has a $3\\text{ m}$ strip of timber trim. He cuts three pieces: $85\\text{ cm}$, $90\\text{ cm}$, and $65\\text{ cm}$. How many cm remain?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Convert 3 m to 300 cm</span></div>
      <div class="answer-line">Remaining: <span class="answer-blank"></span> cm [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 3: Athletics Track Laps</span><span class="q-marks">[3 Marks]</span></div>
      <p>One lap of a running track is $400\\text{ metres}$. How many complete laps must an athlete run to cover $5\\text{ kilometres}$?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Convert 5 km to 5000 m</span></div>
      <div class="answer-line">Laps: <span class="answer-blank"></span> laps [M1, A1]</div>
    </div>
    """
    pages.append(wrap_page(p18, 18, "Module 2: Measures, Shape & Space", "Practice: Length", "Maths Level 1 Companion Practice Workbook"))

    p19 = """
    <h2>Metric Units of Weight &amp; Liquid Capacity</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Standards: L1.17 &bull; Grams, kilograms, tonnes, millilitres, litres</div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 1: Weight &amp; Capacity Warm-Up</span><span class="q-marks">[4 Marks]</span></div>
      <p>Convert: a) $3.2\\text{ kg}$ to grams &emsp; b) $750\\text{ ml}$ to litres &emsp; c) $4,500\\text{ g}$ to kg &emsp; d) $1.5\\text{ L}$ to ml.</p>
      <div class="answer-line">a) <span class="answer-blank" style="min-width:60px;"></span> b) <span class="answer-blank" style="min-width:60px;"></span> c) <span class="answer-blank" style="min-width:60px;"></span> d) <span class="answer-blank" style="min-width:60px;"></span></div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 2: Bakery Ingredient Mass</span><span class="q-marks">[3 Marks]</span></div>
      <p>A baker has $5\\text{ kg}$ of sugar. He uses $1,250\\text{ g}$ for bread and $850\\text{ g}$ for pastries. How many grams of sugar remain?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">5 kg = 5000 g</span></div>
      <div class="answer-line">Remaining: <span class="answer-blank"></span> g [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 3: Clinic Liquid Medicine</span><span class="q-marks">[3 Marks]</span></div>
      <p>A patient requires $20\\text{ ml}$ of medicine 3 times per day for 7 days. How many $150\\text{ ml}$ bottles must be dispensed?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Calculate total ml needed</span></div>
      <div class="answer-line">Bottles Needed: <span class="answer-blank"></span> [M1, A1]</div>
    </div>
    """
    pages.append(wrap_page(p19, 19, "Module 2: Measures, Shape & Space", "Practice: Weight & Capacity", "Maths Level 1 Companion Practice Workbook"))

    p20 = """
    <h2>Imperial Approximations &amp; Miles to Kilometres</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Standards: L1.17 &bull; Using $5\\text{ miles} \\approx 8\\text{ km}$, $1\\text{ kg} \\approx 2.2\\text{ lbs}$, $1\\text{ inch} \\approx 2.5\\text{ cm}$</div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 1: Imperial Conversion Warm-Up</span><span class="q-marks">[4 Marks]</span></div>
      <p>Using standard approximations: a) $25\\text{ miles}$ to km &emsp; b) $40\\text{ km}$ to miles &emsp; c) $10\\text{ inches}$ to cm.</p>
      <div class="answer-line">a) <span class="answer-blank" style="min-width:70px;"></span> km &emsp; b) <span class="answer-blank" style="min-width:70px;"></span> mi &emsp; c) <span class="answer-blank" style="min-width:70px;"></span> cm</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 2: Luggage Weight Allowance</span><span class="q-marks">[3 Marks]</span></div>
      <p>An airline allows $44\\text{ lbs}$ of baggage. A passenger's suitcase weighs $18\\text{ kg}$. Using $1\\text{ kg} = 2.2\\text{ lbs}$, is it within limit?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Multiply 18 by 2.2</span></div>
      <div class="answer-line">Weight: <span class="answer-blank" style="min-width:70px;"></span> lbs &emsp; Within Limit? <span class="answer-blank" style="min-width:60px;"></span> [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 3: European Road Trip Distance</span><span class="q-marks">[3 Marks]</span></div>
      <p>A driver in France travels 120 kilometres. How many miles is this? (Use $8\\text{ km} = 5\\text{ miles}$)</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Divide by 8 then times 5</span></div>
      <div class="answer-line">Distance: <span class="answer-blank"></span> miles [M1, A1]</div>
    </div>
    """
    pages.append(wrap_page(p20, 20, "Module 2: Measures, Shape & Space", "Practice: Imperial Units", "Maths Level 1 Companion Practice Workbook"))

    p21 = """
    <h2>Time: 12-Hour, 24-Hour &amp; Work Schedules</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Standards: L1.18 &bull; Train timetables, elapsed shift durations, 24-hour clock conversions</div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 1: Time Conversion Drills</span><span class="q-marks">[4 Marks]</span></div>
      <p>Convert to 24-hour format: a) $8:40\\text{ am}$ &emsp; b) $3:25\\text{ pm}$ &emsp; c) $9:10\\text{ pm}$ &emsp; d) $11:55\\text{ pm}$.</p>
      <div class="answer-line">a) <span class="answer-blank" style="min-width:60px;"></span> b) <span class="answer-blank" style="min-width:60px;"></span> c) <span class="answer-blank" style="min-width:60px;"></span> d) <span class="answer-blank" style="min-width:60px;"></span></div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 2: Train Commute Duration</span><span class="q-marks">[3 Marks]</span></div>
      <p>A commuter boards a train at 07:42. The train arrives at destination at 09:15. How long was the journey?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Jump to 08:00 then to 09:15</span></div>
      <div class="answer-line">Journey Duration: <span class="answer-blank"></span> [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 3: Night Shift Hours &amp; Unpaid Break</span><span class="q-marks">[3 Marks]</span></div>
      <p>A warehouse security guard works from 21:30 to 06:00. He takes a 45-minute unpaid meal break. How many paid hours did he work?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Find total span and deduct break</span></div>
      <div class="answer-line">Paid Working Hours: <span class="answer-blank"></span> [M1, A1]</div>
    </div>
    """
    pages.append(wrap_page(p21, 21, "Module 2: Measures, Shape & Space", "Practice: Time & Timetables", "Maths Level 1 Companion Practice Workbook"))

    p22 = """
    <h2>Perimeter of Rectangles &amp; Simple Polygons</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Standards: L1.19 &bull; Adding side lengths, fencing gardens, skirting boards</div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 1: Perimeter Warm-Up</span><span class="q-marks">[4 Marks]</span></div>
      <p>Find perimeter: a) Rectangle $8\\text{ m} \\times 5\\text{ m}$ &emsp; b) Square of side $7.5\\text{ cm}$ &emsp; c) Equilateral triangle of side $9\\text{ cm}$.</p>
      <div class="answer-line">a) <span class="answer-blank" style="min-width:70px;"></span> m &emsp; b) <span class="answer-blank" style="min-width:70px;"></span> cm &emsp; c) <span class="answer-blank" style="min-width:70px;"></span> cm</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 2: Skirting Board with Doorway</span><span class="q-marks">[3 Marks]</span></div>
      <p>A living room is $5.5\\text{ m}$ long and $4.0\\text{ m}$ wide. There is a doorway opening of $1.0\\text{ m}$ where no skirting is fitted. Find skirting length.</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Perimeter minus doorway</span></div>
      <div class="answer-line">Skirting Length: <span class="answer-blank"></span> metres [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 3: Garden Fence Cost</span><span class="q-marks">[3 Marks]</span></div>
      <p>A rectangular vegetable patch is $9\\text{ m}$ by $4\\text{ m}$. Wire fencing costs $£3.50$ per metre. Calculate the total cost to fence the patch.</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Calculate perimeter then cost</span></div>
      <div class="answer-line">Total Cost: £ <span class="answer-blank"></span> [M1, A1]</div>
    </div>
    """
    pages.append(wrap_page(p22, 22, "Module 2: Measures, Shape & Space", "Practice: Perimeter", "Maths Level 1 Companion Practice Workbook"))

    p23 = """
    <h2>Area of Rectangles &amp; Flooring Costs</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Standards: L1.20 &bull; Area formula $A = l \\times w$, square metres, carpeting &amp; tiles</div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 1: Area Formula Warm-Up</span><span class="q-marks">[4 Marks]</span></div>
      <p>Find area: a) Rectangle $7\\text{ m} \\times 4\\text{ m}$ &emsp; b) Square with side $9\\text{ cm}$ &emsp; c) Classroom $12\\text{ m} \\times 8\\text{ m}$.</p>
      <div class="answer-line">a) <span class="answer-blank" style="min-width:70px;"></span> m² &emsp; b) <span class="answer-blank" style="min-width:70px;"></span> cm² &emsp; c) <span class="answer-blank" style="min-width:70px;"></span> m²</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 2: Bedroom Carpet Cost</span><span class="q-marks">[3 Marks]</span></div>
      <p>A bedroom measures $4.5\\text{ m}$ by $3.0\\text{ m}$. Carpet costs $£16.00$ per square metre. How much does it cost to carpet the room?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Area = 4.5 × 3.0</span></div>
      <div class="answer-line">Carpet Cost: £ <span class="answer-blank"></span> [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 3: Wall Paint Tin Coverage</span><span class="q-marks">[3 Marks]</span></div>
      <p>A feature wall is $6.5\\text{ m}$ long and $2.4\\text{ m}$ high. A tin of emulsion covers $10\\text{ m}^2$. How many tins are needed to paint 1 coat?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Calculate area then round up tins</span></div>
      <div class="answer-line">Tins Needed: <span class="answer-blank"></span> tins [M1, A1]</div>
    </div>
    """
    pages.append(wrap_page(p23, 23, "Module 2: Measures, Shape & Space", "Practice: Rectangle Area", "Maths Level 1 Companion Practice Workbook"))

    p24 = """
    <h2>Compound Area: L-Shaped Rooms</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Standards: L1.20 &bull; Splitting shapes into two rectangles, summing partial areas</div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 1: Split &amp; Sum Warm-Up</span><span class="q-marks">[4 Marks]</span></div>
      <p>An L-shape splits into: Rectangle A ($6\\text{ m} \\times 4\\text{ m}$) and Rectangle B ($3\\text{ m} \\times 2\\text{ m}$). Find total area.</p>
      <div class="grid-workspace" style="height:55px;"><span class="workspace-hint">Add partial areas</span></div>
      <div class="answer-line">Total Area: <span class="answer-blank"></span> m² [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 2: Hallway Vinyl Flooring</span><span class="q-marks">[3 Marks]</span></div>
      <p>An L-shaped hallway has outer dimensions $8\\text{ m}$ and $5\\text{ m}$, with cutout $4\\text{ m} \\times 3\\text{ m}$. Find floor area.</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Total area minus cutout or split</span></div>
      <div class="answer-line">Floor Area: <span class="answer-blank"></span> m² [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 3: Turfing an L-Shaped Garden</span><span class="q-marks">[3 Marks]</span></div>
      <p>The garden has area $48\\text{ m}^2$. Turf rolls cover $1\\text{ m}^2$ each and cost $£4.20$. Delivery is $£15.00$. Find total cost.</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Calculate turf + delivery</span></div>
      <div class="answer-line">Total Cost: £ <span class="answer-blank"></span> [M1, A1]</div>
    </div>
    """
    pages.append(wrap_page(p24, 24, "Module 2: Measures, Shape & Space", "Practice: Compound Area", "Maths Level 1 Companion Practice Workbook"))

    p25 = """
    <h2>Volume of Cuboids &amp; Water Cisterns</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Standards: L1.21 &bull; Formula $V = l \\times w \\times h$, litres conversion ($1000\\text{ cm}^3 = 1\\text{ L}$)</div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 1: Volume Calculation Warm-Up</span><span class="q-marks">[4 Marks]</span></div>
      <p>Calculate volume: a) Cuboid $5\\text{ cm} \\times 4\\text{ cm} \\times 10\\text{ cm}$ &emsp; b) Container $2\\text{ m} \\times 1.5\\text{ m} \\times 0.8\\text{ m}$.</p>
      <div class="grid-workspace" style="height:55px;"><span class="workspace-hint">Multiply 3 dimensions</span></div>
      <div class="answer-line">a) <span class="answer-blank" style="min-width:80px;"></span> cm³ &emsp; b) <span class="answer-blank" style="min-width:80px;"></span> m³</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 2: Fish Aquarium Capacity</span><span class="q-marks">[3 Marks]</span></div>
      <p>An aquarium is $60\\text{ cm}$ long, $30\\text{ cm}$ wide, and $40\\text{ cm}$ deep. How many litres of water does it hold?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Volume in cm³ ÷ 1000</span></div>
      <div class="answer-line">Capacity: <span class="answer-blank"></span> litres [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 3: Garden Compost Delivery</span><span class="q-marks">[3 Marks]</span></div>
      <p>A raised planter is $3.0\\text{ m}$ long, $1.2\\text{ m}$ wide, and $0.5\\text{ m}$ deep. Compost bags hold $50\\text{ litres}$ ($0.05\\text{ m}^3$). How many bags to fill?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Planter volume ÷ bag volume</span></div>
      <div class="answer-line">Bags Needed: <span class="answer-blank"></span> bags [M1, A1]</div>
    </div>
    """
    pages.append(wrap_page(p25, 25, "Module 2: Measures, Shape & Space", "Practice: Volume", "Maths Level 1 Companion Practice Workbook"))

    p26 = """
    <h2>2D Geometry: Triangles &amp; Angle Types</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Standards: L1.22, L1.23 &bull; Acute, right, obtuse angles, triangle angle sum 180°</div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 1: Classify Angles</span><span class="q-marks">[4 Marks]</span></div>
      <p>Classify: a) $35^\\circ$ &emsp; b) $90^\\circ$ &emsp; c) $125^\\circ$ &emsp; d) $180^\\circ$.</p>
      <div class="answer-line">a) <span class="answer-blank" style="min-width:60px;"></span> b) <span class="answer-blank" style="min-width:60px;"></span> c) <span class="answer-blank" style="min-width:60px;"></span> d) <span class="answer-blank" style="min-width:60px;"></span></div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 2: Missing Angle in Triangle</span><span class="q-marks">[3 Marks]</span></div>
      <p>A right-angled triangle has one acute angle measuring $38^\\circ$. Calculate the size of the other acute angle.</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">180 - (90 + 38)</span></div>
      <div class="answer-line">Missing Angle: <span class="answer-blank"></span> ° [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 3: Isosceles Triangle Angles</span><span class="q-marks">[3 Marks]</span></div>
      <p>An isosceles triangle has an apex angle of $40^\\circ$. The two base angles are equal. Calculate the size of each base angle.</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">(180 - 40) ÷ 2</span></div>
      <div class="answer-line">Base Angle: <span class="answer-blank"></span> ° [M1, A1]</div>
    </div>
    """
    pages.append(wrap_page(p26, 26, "Module 2: Measures, Shape & Space", "Practice: 2D Geometry", "Maths Level 1 Companion Practice Workbook"))

    p27 = """
    <h2>3D Solids: Faces, Edges &amp; Packaging Nets</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Standards: L1.24, L1.25 &bull; Identifying solids, counting vertices/edges, folding nets</div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 1: 3D Properties Warm-Up</span><span class="q-marks">[4 Marks]</span></div>
      <p>State faces, edges, vertices: a) Cube &emsp; b) Triangular prism &emsp; c) Square-based pyramid.</p>
      <div class="answer-line">Cube: <span class="answer-blank" style="min-width:60px;"></span> Prism: <span class="answer-blank" style="min-width:60px;"></span> Pyramid: <span class="answer-blank" style="min-width:60px;"></span></div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 2: Cardboard Packaging Net</span><span class="q-marks">[3 Marks]</span></div>
      <p>A package is made from a net with 6 rectangular faces arranged in 3 matching pairs. Name the 3D solid.</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Identify solid from net</span></div>
      <div class="answer-line">Solid: <span class="answer-blank"></span> [B1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 3: Cylinder Properties</span><span class="q-marks">[3 Marks]</span></div>
      <p>How many flat faces, curved faces, and straight edges does a closed cylinder have?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">State properties</span></div>
      <div class="answer-line">Properties: <span class="answer-blank" style="min-width:180px;"></span> [B2]</div>
    </div>
    """
    pages.append(wrap_page(p27, 27, "Module 2: Measures, Shape & Space", "Practice: 3D Shapes", "Maths Level 1 Companion Practice Workbook"))

    p28 = """
    <h2>Scale Plans &amp; Room Layouts</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Standards: L1.26 &bull; Reading scales like $1\\text{ cm} = 2\\text{ m}$, grid maps, measuring real lengths</div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 1: Scale Multipliers Warm-Up</span><span class="q-marks">[4 Marks]</span></div>
      <p>Scale $1\\text{ cm} = 3\\text{ m}$: a) $4\\text{ cm}$ on map = real length? &emsp; b) $18\\text{ m}$ real = map length in cm?</p>
      <div class="answer-line">a) <span class="answer-blank" style="min-width:80px;"></span> m &emsp; b) <span class="answer-blank" style="min-width:80px;"></span> cm</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 2: Classroom Scale Drawing</span><span class="q-marks">[3 Marks]</span></div>
      <p>On a plan drawn to $1 : 50$, a classroom is $14\\text{ cm}$ long and $10\\text{ cm}$ wide. What are its real dimensions in metres?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Multiply by 50 then divide by 100</span></div>
      <div class="answer-line">Real Length: <span class="answer-blank" style="min-width:70px;"></span> m &emsp; Width: <span class="answer-blank" style="min-width:70px;"></span> m [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 3: Furniture Grid Placement</span><span class="q-marks">[3 Marks]</span></div>
      <p>On a squared grid where 1 grid square $= 0.5\\text{ m}$, a bookcase measures $1.5\\text{ m}$ wide. How many grid squares wide is the bookcase?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">1.5 ÷ 0.5</span></div>
      <div class="answer-line">Squares Wide: <span class="answer-blank"></span> squares [M1, A1]</div>
    </div>
    """
    pages.append(wrap_page(p28, 28, "Module 2: Measures, Shape & Space", "Practice: Scale Plans", "Maths Level 1 Companion Practice Workbook"))

    p29 = """
    <h2>8-Point Compass &amp; Map Navigation</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Standards: L1.27 &bull; Cardinal and intercardinal compass directions, turns and routes</div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 1: Compass Direction Drills</span><span class="q-marks">[4 Marks]</span></div>
      <p>State direction: a) Opposite of North-East &emsp; b) Facing North, turn $90^\\circ$ clockwise &emsp; c) Facing East, turn $180^\\circ$.</p>
      <div class="answer-line">a) <span class="answer-blank" style="min-width:70px;"></span> b) <span class="answer-blank" style="min-width:70px;"></span> c) <span class="answer-blank" style="min-width:70px;"></span></div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 2: Delivery Van Route</span><span class="q-marks">[3 Marks]</span></div>
      <p>A delivery van leaves the depot travelling East for $6\\text{ miles}$, then turns South for $8\\text{ miles}$. In what direction is depot from the van?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Opposite of South-East</span></div>
      <div class="answer-line">Direction: <span class="answer-blank"></span> [B1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 3: Hiking Navigation Map</span><span class="q-marks">[3 Marks]</span></div>
      <p>A hiker walks North-West for $4\\text{ km}$. To return directly back to her starting point, in which compass direction must she walk?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Find opposite direction</span></div>
      <div class="answer-line">Return Direction: <span class="answer-blank"></span> [B1]</div>
    </div>
    """
    pages.append(wrap_page(p29, 29, "Module 2: Measures, Shape & Space", "Practice: Compass Directions", "Maths Level 1 Companion Practice Workbook"))

    p30 = """
    <h2>Compound Measures: Average Speed in Miles per Hour</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Standards: L1.18 &bull; Speed formula: $\\text{Speed} = \\text{Distance} \\div \\text{Time}$ using whole hours and half hours</div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 1: Speed Formula Warm-Up</span><span class="q-marks">[4 Marks]</span></div>
      <p>Find speed: a) $120\\text{ miles}$ in 2 hours &emsp; b) $90\\text{ miles}$ in 1.5 hours &emsp; c) $150\\text{ km}$ in 3 hours.</p>
      <div class="answer-line">a) <span class="answer-blank" style="min-width:70px;"></span> mph &emsp; b) <span class="answer-blank" style="min-width:70px;"></span> mph &emsp; c) <span class="answer-blank" style="min-width:70px;"></span> km/h</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 2: Courier Van Journey</span><span class="q-marks">[3 Marks]</span></div>
      <p>A courier drives $165\\text{ miles}$ in 3 hours. Calculate her average speed in miles per hour.</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Divide distance by time</span></div>
      <div class="answer-line">Average Speed: <span class="answer-blank"></span> mph [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 3: Journey Time Prediction</span><span class="q-marks">[3 Marks]</span></div>
      <p>A truck travels at an average speed of $50\\text{ mph}$. How many hours will it take to complete a $200\\text{ mile}$ motorway delivery?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Time = Distance ÷ Speed</span></div>
      <div class="answer-line">Journey Time: <span class="answer-blank"></span> hours [M1, A1]</div>
    </div>
    """
    pages.append(wrap_page(p30, 30, "Module 2: Measures, Shape & Space", "Practice: Average Speed", "Maths Level 1 Companion Practice Workbook"))

    # STRAND 2 CHECKPOINT ASSESSMENT (PAGES 31 TO 34: 4 full pages)
    chk2_p1 = [
        (1, 2, "Convert: a) $3.6\\text{ m}$ to cm &emsp; b) $850\\text{ g}$ to kg.", 75),
        (2, 2, "A film starts at 19:15 and finishes at 21:05. How long was the film in hours and minutes?", 65),
        (3, 2, "Calculate the perimeter of a rectangle measuring $9\\text{ m}$ by $4.5\\text{ m}$.", 70)
    ]
    pages.append(checkpoint_page("Strand 2: Measures, Shape & Space", "Part 1 &bull; Non-Calculator (Q1-Q3)", 31, "6 Marks", chk2_p1))

    chk2_p2 = [
        (4, 2, "Calculate the area of a square garden plot of side $7\\text{ m}$.", 75),
        (5, 2, "A water jug holds $1.5\\text{ litres}$. Glasses hold $250\\text{ ml}$. How many full glasses can be poured?", 65),
        (6, 2, "State the number of edges and vertices on a triangular prism.", 70)
    ]
    pages.append(checkpoint_page("Strand 2: Measures, Shape & Space", "Part 1 &bull; Non-Calculator (Q4-Q6)", 32, "6 Marks", chk2_p2))

    chk2_p3 = [
        (7, 3, "A carpet costs $£16.50$ per square metre. A room is $5.0\\text{ m}$ by $4.2\\text{ m}$. Calculate the carpet cost.", 80),
        (8, 3, "A delivery truck travels 35 miles. Using $5\\text{ miles} = 8\\text{ km}$, convert the distance into kilometres.", 80),
        (9, 3, "A storage tank measures $1.4\\text{ m}$ long, $0.8\\text{ m}$ wide, and $0.5\\text{ m}$ high. How many litres does it hold?", 80)
    ]
    pages.append(checkpoint_page("Strand 2: Measures, Shape & Space", "Part 2 &bull; Calculator Allowed (Q7-Q9)", 33, "9 Marks", chk2_p3))

    chk2_p4 = [
        (10, 3, "A retail assistant works 30 hours at $£11.40/\\text{hr}$, plus 5 hours overtime at time-and-a-half ($£17.10/\\text{hr}$). Find total gross wage.", 80),
        (11, 3, "On a map with scale $1\\text{ cm} = 20\\text{ m}$, the length of a running track is $8.5\\text{ cm}$. What is the real length in metres?", 80),
        (12, 3, "An L-shaped patio has two parts: $5\\text{ m} \\times 4\\text{ m}$ and $3\\text{ m} \\times 2\\text{ m}$. Paving slabs cover $1\\text{ m}^2$ each and cost $£6.20$. Find total cost.", 80)
    ]
    pages.append(checkpoint_page("Strand 2: Measures, Shape & Space", "Part 2 &bull; Calculator Allowed (Q10-Q12)", 34, "9 Marks", chk2_p4))

    # =========================================================================
    # MODULE 3: HANDLING INFORMATION & DATA (PAGES 35 - 48)
    # 10 Practice Pages + 4 Checkpoint Pages
    # =========================================================================

    p35 = """
    <h2>Tally Charts &amp; Frequency Tables</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Standards: L1.28 &bull; Tally groups of 5, raw counts, completing workplace data records</div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 1: Complete Tally Table</span><span class="q-marks">[4 Marks]</span></div>
      <p>30 customers surveyed: Red (12), Blue (11), Green (7). Write tally marks and verify the total.</p>
      <div class="grid-workspace" style="height:55px;"><span class="workspace-hint">Draw 5-bar bundles</span></div>
      <div class="answer-line">Total Verified: <span class="answer-blank"></span> [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 2: Clinic Appointment Audit</span><span class="q-marks">[3 Marks]</span></div>
      <p>A dental practice logs attendance: Attended (45), Cancelled (10), No-show (5). What fraction of appointments were attended? Simplify.</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">45 ÷ 60</span></div>
      <div class="answer-line">Fraction: <span class="answer-blank"></span> [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 3: Vehicle Service Type</span><span class="q-marks">[3 Marks]</span></div>
      <p>A garage logs MOTs: Pass first time 28, Minor fail 14, Major fail 8. What percentage passed first time?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">28 ÷ 50 × 100</span></div>
      <div class="answer-line">Pass Rate: <span class="answer-blank"></span> % [M1, A1]</div>
    </div>
    """
    pages.append(wrap_page(p35, 35, "Module 3: Handling Information & Data", "Practice: Tally Charts", "Maths Level 1 Companion Practice Workbook"))

    p36 = """
    <h2>Bar Charts: Constructing &amp; Reading</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Standards: L1.29 &bull; Vertical scale accuracy, bar labels, modal category identification</div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 1: Read Bar Chart Warm-Up</span><span class="q-marks">[4 Marks]</span></div>
      <p>Bar heights: Dept A 40, Dept B 65, Dept C 55, Dept D 80. Identify: a) Highest dept &emsp; b) Total across all 4 depts.</p>
      <div class="answer-line">a) <span class="answer-blank" style="min-width:80px;"></span> &emsp; b) <span class="answer-blank" style="min-width:80px;"></span></div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 2: Difference Between Categories</span><span class="q-marks">[3 Marks]</span></div>
      <p>From Task 1, how many more staff are in Dept D compared to Dept A?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">80 - 40</span></div>
      <div class="answer-line">Difference: <span class="answer-blank"></span> [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 3: Scale Increment Check</span><span class="q-marks">[3 Marks]</span></div>
      <p>A student draws a bar chart with vertical values: 0, 5, 10, 20, 25, 30. Identify the mistake and explain why it is wrong.</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Missing 15; unequal increments</span></div>
      <div class="answer-line">Error Explanation: <span class="answer-blank" style="min-width:180px;"></span> [B2]</div>
    </div>
    """
    pages.append(wrap_page(p36, 36, "Module 3: Handling Information & Data", "Practice: Bar Charts", "Maths Level 1 Companion Practice Workbook"))

    p37 = """
    <h2>Dual Bar Charts &amp; Comparisons</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Standards: L1.29 &bull; Comparing two sets of bars, legends/keys, comparative statements</div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 1: Dual Chart Reading</span><span class="q-marks">[4 Marks]</span></div>
      <p>Sales (Week 1 vs Week 2): Mon (30 vs 40), Tue (25 vs 35), Wed (45 vs 50). Find total sales in Week 2.</p>
      <div class="grid-workspace" style="height:55px;"><span class="workspace-hint">Sum Week 2 bars</span></div>
      <div class="answer-line">Week 2 Total: <span class="answer-blank"></span> [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 2: Day of Greatest Improvement</span><span class="q-marks">[3 Marks]</span></div>
      <p>On which day did sales increase the most between Week 1 and Week 2? What was the increase?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Compare differences</span></div>
      <div class="answer-line">Day: <span class="answer-blank" style="min-width:70px;"></span> &emsp; Increase: <span class="answer-blank" style="min-width:70px;"></span> [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 3: Comparative Workplace Statement</span><span class="q-marks">[3 Marks]</span></div>
      <p>Write two comparative sentences summarizing the sales performance across both weeks.</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">State general trend and specific figure</span></div>
      <div class="answer-line">Summary: <span class="answer-blank" style="min-width:180px;"></span> [B2]</div>
    </div>
    """
    pages.append(wrap_page(p37, 37, "Module 3: Handling Information & Data", "Practice: Dual Charts", "Maths Level 1 Companion Practice Workbook"))

    p38 = """
    <h2>Pictograms &amp; Symbol Keys</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Standards: L1.30 &bull; Interpreting full, half and quarter symbols using the key</div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 1: Pictogram Reading Drills</span><span class="q-marks">[4 Marks]</span></div>
      <p>Key: 1 circle = 10 items. Find items for: a) 3 circles &emsp; b) $4\\frac{1}{2}$ circles &emsp; c) $2\\frac{1}{4}$ circles.</p>
      <div class="answer-line">a) <span class="answer-blank" style="min-width:60px;"></span> b) <span class="answer-blank" style="min-width:60px;"></span> c) <span class="answer-blank" style="min-width:60px;"></span></div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 2: Library Book Borrowing</span><span class="q-marks">[3 Marks]</span></div>
      <p>Key: 1 star = 8 books borrowed. Friday shows 4 stars. Saturday shows $5\\frac{1}{2}$ stars. Total borrowed over both days?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Multiply stars by 8</span></div>
      <div class="answer-line">Total Books: <span class="answer-blank"></span> [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 3: Drawing Pictogram Symbols</span><span class="q-marks">[3 Marks]</span></div>
      <p>Key: 1 square = 6 bicycles sold. A bike shop sold 21 bicycles on Sunday. How many symbols should be drawn?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">21 ÷ 6</span></div>
      <div class="answer-line">Symbols: <span class="answer-blank"></span> [M1, A1]</div>
    </div>
    """
    pages.append(wrap_page(p38, 38, "Module 3: Handling Information & Data", "Practice: Pictograms", "Maths Level 1 Companion Practice Workbook"))

    p39 = """
    <h2>Line Graphs &amp; Continuous Trends</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Standards: L1.31 &bull; Tracking continuous trends, reading points, temperature and sales</div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 1: Temperature Graph Reading</span><span class="q-marks">[4 Marks]</span></div>
      <p>Temperatures: 08:00 ($14^\\circ\\text{C}$), 10:00 ($18^\\circ\\text{C}$), 12:00 ($22^\\circ\\text{C}$). Estimate temp at 09:00 and 11:00.</p>
      <div class="answer-line">09:00: <span class="answer-blank" style="min-width:70px;"></span> °C &emsp; 11:00: <span class="answer-blank" style="min-width:70px;"></span> °C</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 2: Daily Sales Trend</span><span class="q-marks">[3 Marks]</span></div>
      <p>A coffee stall records daily takings: Mon $£120$, Tue $£150$, Wed $£140$, Thu $£180$, Fri $£210$. Describe the overall trend.</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">General increase over week</span></div>
      <div class="answer-line">Trend Description: <span class="answer-blank" style="min-width:180px;"></span> [B1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 3: Conversion Graph Reading</span><span class="q-marks">[3 Marks]</span></div>
      <p>A currency graph shows $£10 = $13 US Dollars. How many dollars do you receive for $£60$?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Multiply by 6</span></div>
      <div class="answer-line">Dollars: $ <span class="answer-blank"></span> [M1, A1]</div>
    </div>
    """
    pages.append(wrap_page(p39, 39, "Module 3: Handling Information & Data", "Practice: Line Graphs", "Maths Level 1 Companion Practice Workbook"))

    p40 = """
    <h2>Pie Charts: Benchmark Proportions</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Standards: L1.32 &bull; Halves, quarters, tenths, calculating category totals</div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 1: Sector Proportions Warm-Up</span><span class="q-marks">[4 Marks]</span></div>
      <p>In a pie chart of 160 people: a) What number is $\\frac{1}{2}$? &emsp; b) What number is $\\frac{1}{4}$? &emsp; c) What number is $\\frac{3}{4}$?</p>
      <div class="answer-line">a) <span class="answer-blank" style="min-width:60px;"></span> b) <span class="answer-blank" style="min-width:60px;"></span> c) <span class="answer-blank" style="min-width:60px;"></span></div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 2: Staff Transport Survey</span><span class="q-marks">[3 Marks]</span></div>
      <p>A pie chart shows transport for 120 staff: Half drive, quarter bus, quarter walk. How many staff walk to work?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">120 ÷ 4</span></div>
      <div class="answer-line">Walk to Work: <span class="answer-blank"></span> staff [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 3: Household Budget Pie Chart</span><span class="q-marks">[3 Marks]</span></div>
      <p>A monthly income of $£2,400$ is shown on a pie chart: Rent is a half circle ($180^\\circ$), Food is a quarter ($90^\\circ$). Find rent and food totals.</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Calculate 1/2 and 1/4 of £2,400</span></div>
      <div class="answer-line">Rent: £ <span class="answer-blank" style="min-width:70px;"></span> &emsp; Food: £ <span class="answer-blank" style="min-width:70px;"></span> [M1, A1]</div>
    </div>
    """
    pages.append(wrap_page(p40, 40, "Module 3: Handling Information & Data", "Practice: Pie Charts", "Maths Level 1 Companion Practice Workbook"))

    p41 = """
    <h2>The Mean Average</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Standards: L1.33 &bull; Formula: Sum of values ÷ count of values, representative values</div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 1: Calculate Mean Warm-Up</span><span class="q-marks">[4 Marks]</span></div>
      <p>Calculate the mean of: a) $6, 10, 8, 12$ &emsp; b) $15, 20, 25, 30, 10$.</p>
      <div class="grid-workspace" style="height:55px;"><span class="workspace-hint">Add and divide by count</span></div>
      <div class="answer-line">a) <span class="answer-blank" style="min-width:80px;"></span> &emsp; b) <span class="answer-blank" style="min-width:80px;"></span></div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 2: Weekly Delivery Runs</span><span class="q-marks">[3 Marks]</span></div>
      <p>A delivery driver makes parcel drops over 5 days: Mon 32, Tue 40, Wed 36, Thu 44, Fri 38. Calculate mean daily drops.</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Sum = 190; 190 ÷ 5</span></div>
      <div class="answer-line">Mean Drops: <span class="answer-blank"></span> drops [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 3: Working Backwards from Mean</span><span class="q-marks">[3 Marks]</span></div>
      <p>Three friends have a mean age of 24. A fourth friend joins who is 28. What is the new mean age of all 4 friends?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Old sum = 3 × 24 = 72; New sum = 72 + 28</span></div>
      <div class="answer-line">New Mean Age: <span class="answer-blank"></span> years [M1, A1]</div>
    </div>
    """
    pages.append(wrap_page(p41, 41, "Module 3: Handling Information & Data", "Practice: Mean", "Maths Level 1 Companion Practice Workbook"))

    p42 = """
    <h2>The Range: Consistency &amp; Spread</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Standards: L1.34 &bull; Highest minus lowest value, measuring variation and reliability</div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 1: Calculate Range Warm-Up</span><span class="q-marks">[4 Marks]</span></div>
      <p>Find range: a) $12, 19, 8, 25, 14$ &emsp; b) $45, 52, 48, 61, 42, 55$.</p>
      <div class="answer-line">a) <span class="answer-blank" style="min-width:80px;"></span> &emsp; b) <span class="answer-blank" style="min-width:80px;"></span></div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 2: Call Centre Waiting Times</span><span class="q-marks">[3 Marks]</span></div>
      <p>Customer call wait times (minutes): $4, 12, 6, 18, 5, 9$. Calculate the range of waiting times.</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">18 - 4</span></div>
      <div class="answer-line">Range: <span class="answer-blank"></span> minutes [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 3: Production Consistency Comparison</span><span class="q-marks">[3 Marks]</span></div>
      <p>Line A: Mean output 50, Range 4. Line B: Mean output 50, Range 22. Explain which line is more consistent.</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Smaller range indicates reliability</span></div>
      <div class="answer-line">Consistent Line: Line <span class="answer-blank" style="min-width:40px;"></span> Reason: <span class="answer-blank" style="min-width:140px;"></span> [B2]</div>
    </div>
    """
    pages.append(wrap_page(p42, 42, "Module 3: Handling Information & Data", "Practice: Range", "Maths Level 1 Companion Practice Workbook"))

    p43 = """
    <h2>The Probability Scale: 0 to 1</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Standards: L1.35 &bull; Words (impossible, unlikely, evens, likely, certain), fractions, decimals</div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 1: Probability Scale Matching</span><span class="q-marks">[4 Marks]</span></div>
      <p>Assign 0, 0.25, 0.5, 0.75, or 1 to: a) Certain event &emsp; b) Even chance &emsp; c) Impossible event &emsp; d) Likely event.</p>
      <div class="answer-line">a) <span class="answer-blank" style="min-width:50px;"></span> b) <span class="answer-blank" style="min-width:50px;"></span> c) <span class="answer-blank" style="min-width:50px;"></span> d) <span class="answer-blank" style="min-width:50px;"></span></div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 2: Rolling a 6-Sided Dice</span><span class="q-marks">[3 Marks]</span></div>
      <p>A fair dice is rolled. What is the probability of rolling: a) A 4? &emsp; b) An even number? &emsp; c) A number less than 5?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">Fractions out of 6</span></div>
      <div class="answer-line">a) <span class="answer-blank" style="min-width:60px;"></span> b) <span class="answer-blank" style="min-width:60px;"></span> c) <span class="answer-blank" style="min-width:60px;"></span> [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 3: Colored Counters in a Bag</span><span class="q-marks">[3 Marks]</span></div>
      <p>A bag contains 6 red, 4 yellow, and 10 blue counters. A counter is picked at random. Find P(Yellow) as a fraction in simplest form.</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">4 ÷ 20</span></div>
      <div class="answer-line">P(Yellow): <span class="answer-blank"></span> [M1, A1]</div>
    </div>
    """
    pages.append(wrap_page(p43, 43, "Module 3: Handling Information & Data", "Practice: Probability Scale", "Maths Level 1 Companion Practice Workbook"))

    p44 = """
    <h2>Listing Outcomes &amp; Sample Space</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Standards: L1.36 &bull; Systematic listing, 2-way tables, meal deals, coin and dice outcomes</div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 1: Coin &amp; Dice Outcomes</span><span class="q-marks">[4 Marks]</span></div>
      <p>A coin is flipped (H, T) and a 4-sided spinner is spun (1, 2, 3, 4). List all possible outcomes systematically.</p>
      <div class="grid-workspace" style="height:55px;"><span class="workspace-hint">H1, H2, H3...</span></div>
      <div class="answer-line">Total Outcomes: <span class="answer-blank"></span> [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 2: Meal Deal Combinations</span><span class="q-marks">[3 Marks]</span></div>
      <p>A cafe meal deal offers: Sandwich (Ham, Cheese), Drink (Water, Juice), Snack (Crisps, Fruit). How many combinations are possible?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">2 × 2 × 2</span></div>
      <div class="answer-line">Combinations: <span class="answer-blank"></span> [M1, A1]</div>
    </div>
    <div class="q-card">
      <div class="q-header"><span class="q-num">Task 3: Probability from Sample Space</span><span class="q-marks">[3 Marks]</span></div>
      <p>From the meal deal in Task 2, what is the probability that a randomly chosen customer picks Water as their drink?</p>
      <div class="ruled-workspace" style="height:55px;"><span class="workspace-hint">4 out of 8</span></div>
      <div class="answer-line">Probability: <span class="answer-blank"></span> [M1, A1]</div>
    </div>
    """
    pages.append(wrap_page(p44, 44, "Module 3: Handling Information & Data", "Practice: Listing Outcomes", "Maths Level 1 Companion Practice Workbook"))

    # STRAND 3 CHECKPOINT ASSESSMENT (PAGES 45 TO 48: 4 full pages)
    chk3_p1 = [
        (1, 2, "Test marks: $14, 18, 12, 16, 20$. Calculate: a) Mean &emsp; b) Range.", 75),
        (2, 2, "A spinner has 8 equal sections numbered 1 to 8. What is the probability of spinning a number less than 4?", 65),
        (3, 2, "A tally chart records: <s>||||</s> <s>||||</s> <s>||||</s> |. Write the total frequency.", 70)
    ]
    pages.append(checkpoint_page("Strand 3: Handling Information & Data", "Part 1 &bull; Non-Calculator (Q1-Q3)", 45, "6 Marks", chk3_p1))

    chk3_p2 = [
        (4, 2, "A bag holds 5 red balls and 15 yellow balls. What is P(Red) as a fraction in simplest form?", 75),
        (5, 2, "A bar chart shows drink sales: Tea 30, Coffee 45, Juice 15. What is the modal drink?", 65),
        (6, 2, "A conversion graph shows $£10 = 12\\text{ Euros}$. How many Euros do you get for $£40$?", 70)
    ]
    pages.append(checkpoint_page("Strand 3: Handling Information & Data", "Part 1 &bull; Non-Calculator (Q4-Q6)", 46, "6 Marks", chk3_p2))

    chk3_p3 = [
        (7, 3, "Daily calls handled by an agent: Mon 28, Tue 34, Wed 30, Thu 36, Fri 32. Calculate mean daily calls.", 80),
        (8, 3, "In a pie chart of 160 students, the sector for 'Science' has a right angle ($90^\\circ$). How many students chose Science?", 80),
        (9, 3, "In a pictogram, 1 star = 6 awards. Year 7 has 4 stars. Year 8 has $3\\frac{1}{2}$ stars. Total awards won?", 80)
    ]
    pages.append(checkpoint_page("Strand 3: Handling Information & Data", "Part 2 &bull; Calculator Allowed (Q7-Q9)", 47, "9 Marks", chk3_p3))

    chk3_p4 = [
        (10, 3, "Shift 1 mean output is 45, range is 3. Shift 2 mean output is 45, range is 14. Write two comparison sentences.", 80),
        (11, 3, "A box holds 25 electronic components: 2 are faulty. What is the probability that a component picked is NOT faulty?", 80),
        (12, 3, "A survey asked 50 shoppers their favourite fruit: Apple 22, Banana 18, Orange 10. What percentage chose Apple?", 80)
    ]
    pages.append(checkpoint_page("Strand 3: Handling Information & Data", "Part 2 &bull; Calculator Allowed (Q10-Q12)", 48, "9 Marks", chk3_p4))

    # =========================================================================
    # SYNOPTIC WORKPLACE CASE STUDY CHALLENGES (PAGES 49 - 51)
    # Multi-strand integrated problem solving
    # =========================================================================

    p49 = """
    <h2>Synoptic Case Study 1: Healthcare Ward Inventory</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Integrated Strands: Addition, Multiplication, Percentages, Decimals &amp; Metric Capacity</div>

    <div class="box-concept">
      <h3 style="margin-top:0;">Context: NHS General Medical Ward Operations</h3>
      <p>Senior Care Assistant Jack coordinates supply orders and patient hydration logs across an 18-bed hospital ward.</p>
    </div>

    <div class="q-card">
      <div class="q-header"><span class="q-num">Part A: Fluid Intake Monitoring</span><span class="q-marks">[4 Marks]</span></div>
      <p>A patient is monitored for daily fluid intake. During the day, she drinks:<br>
      &bull; Morning: 2 cups of tea ($200\\text{ ml}$ each)<br>
      &bull; Lunch: 1 glass of water ($250\\text{ ml}$)<br>
      &bull; Afternoon: 1 cup of soup ($180\\text{ ml}$)<br>
      &bull; Evening: 3 glasses of water ($250\\text{ ml}$ each)<br>
      a) What was her total fluid intake in millilitres?<br>
      b) The doctor's target is $2.0\\text{ litres}$ per day. Did she meet the target? By how many ml was she over or under?</p>
      <div class="ruled-workspace" style="height:65px;"><span class="workspace-hint">Show step-by-step additions and comparison</span></div>
      <div class="answer-line">a) Total: <span class="answer-blank" style="min-width:80px;"></span> ml &emsp; b) Met Target? <span class="answer-blank" style="min-width:60px;"></span> by <span class="answer-blank" style="min-width:70px;"></span> ml [M1, A1, M1, A1]</div>
    </div>

    <div class="q-card">
      <div class="q-header"><span class="q-num">Part B: Ward Stock Order &amp; Discount</span><span class="q-marks">[4 Marks]</span></div>
      <p>Jack orders medical supplies: 15 boxes of latex gloves at $£4.50$ per box, and 8 packs of hand wipes at $£3.25$ per pack. The supplier gives a $10\\%$ discount on orders over $£80$. Calculate the final total cost of the order.</p>
      <div class="ruled-workspace" style="height:65px;"><span class="workspace-hint">Calculate subtotal, check if > £80, apply 10% discount</span></div>
      <div class="answer-line">Final Cost: £ <span class="answer-blank" style="min-width:140px;"></span> [M1, M1, A1, B1]</div>
    </div>
    """
    pages.append(wrap_page(p49, 49, "Synoptic Workplace Challenge", "Case Study 1 &bull; NHS Healthcare", "Maths Level 1 Companion Practice Workbook"))

    p50 = """
    <h2>Synoptic Case Study 2: Construction Timber &amp; Paving</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Integrated Strands: Perimeter, Area, Scale Plans &amp; Material Budgets</div>

    <div class="box-concept">
      <h3 style="margin-top:0;">Context: Landscaping a Community Centre Patio</h3>
      <p>A builder is laying a rectangular stone patio and installing a security fence around a play area.</p>
    </div>

    <div class="q-card">
      <div class="q-header"><span class="q-num">Part A: Patio Paving Slabs</span><span class="q-marks">[4 Marks]</span></div>
      <p>The patio measures $6\\text{ m}$ long by $4\\text{ m}$ wide.<br>
      a) What is the area of the patio in square metres?<br>
      b) Square paving slabs measure $0.5\\text{ m}$ by $0.5\\text{ m}$ ($0.25\\text{ m}^2$ each). How many paving slabs are needed?<br>
      c) Slabs are sold in packs of 10 at $£35.00$ per pack. How many packs must be bought, and what is the cost?</p>
      <div class="ruled-workspace" style="height:65px;"><span class="workspace-hint">Area = l × w; Slabs = Area ÷ 0.25</span></div>
      <div class="answer-line">a) <span class="answer-blank" style="min-width:60px;"></span> m² &emsp; b) <span class="answer-blank" style="min-width:60px;"></span> slabs &emsp; c) £ <span class="answer-blank" style="min-width:70px;"></span> [M1, A1, M1, A1]</div>
    </div>

    <div class="q-card">
      <div class="q-header"><span class="q-num">Part B: Fencing Perimeter &amp; Gate</span><span class="q-marks">[4 Marks]</span></div>
      <p>The builder fences a rectangular play area measuring $12\\text{ m}$ by $8\\text{ m}$. There is a $2\\text{ m}$ metal gate that does not require wooden fencing. Wooden fencing costs $£8.50$ per metre. Calculate the cost of the wooden fencing.</p>
      <div class="ruled-workspace" style="height:65px;"><span class="workspace-hint">Calculate perimeter, deduct 2m gate, multiply by £8.50</span></div>
      <div class="answer-line">Fencing Cost: £ <span class="answer-blank" style="min-width:140px;"></span> [M1, M1, A1, B1]</div>
    </div>
    """
    pages.append(wrap_page(p50, 50, "Synoptic Workplace Challenge", "Case Study 2 &bull; Construction", "Maths Level 1 Companion Practice Workbook"))

    p51 = """
    <h2>Synoptic Case Study 3: Supermarket Logistics</h2>
    <div style="font-size:7.8pt; color:#64748b; margin-bottom:4px;">Integrated Strands: Volume, Weight, Ratios, Speed &amp; Journey Times</div>

    <div class="box-concept">
      <h3 style="margin-top:0;">Context: Regional Distribution Fleet Operations</h3>
      <p>A transport manager schedules deliveries from the regional warehouse to five local express stores.</p>
    </div>

    <div class="q-card">
      <div class="q-header"><span class="q-num">Part A: Delivery Route &amp; Arrival Time</span><span class="q-marks">[4 Marks]</span></div>
      <p>A delivery lorry departs the depot at 06:45. It travels $90\\text{ miles}$ at an average speed of $45\\text{ mph}$. The driver then takes 30 minutes to unload at the store. At what time is unloading completed?</p>
      <div class="ruled-workspace" style="height:65px;"><span class="workspace-hint">Time = Distance ÷ Speed; Add driving time and unloading</span></div>
      <div class="answer-line">Unload Finished: <span class="answer-blank" style="min-width:140px;"></span> [M1, M1, A1, B1]</div>
    </div>

    <div class="q-card">
      <div class="q-header"><span class="q-num">Part B: Cargo Payload Weight Check</span><span class="q-marks">[4 Marks]</span></div>
      <p>The lorry carries 8 pallets of canned food. Each pallet weighs $350\\text{ kg}$. The lorry's maximum payload limit is $3.0\\text{ tonnes}$.<br>
      a) What is the total weight of the 8 pallets in kilograms?<br>
      b) Convert $3.0\\text{ tonnes}$ to kilograms.<br>
      c) Is the lorry within its safe legal load limit? Show your comparison.</p>
      <div class="ruled-workspace" style="height:65px;"><span class="workspace-hint">8 × 350; 1 tonne = 1000 kg</span></div>
      <div class="answer-line">a) <span class="answer-blank" style="min-width:70px;"></span> kg &emsp; b) <span class="answer-blank" style="min-width:70px;"></span> kg &emsp; c) Within Limit? <span class="answer-blank" style="min-width:60px;"></span> [M1, A1, M1, A1]</div>
    </div>
    """
    pages.append(wrap_page(p51, 51, "Synoptic Workplace Challenge", "Case Study 3 &bull; Supermarket Logistics", "Maths Level 1 Companion Practice Workbook"))

    # =========================================================================
    # OFFICIAL MOCK EXAMINATION 1 (PAGES 52 - 59: 8 pages)
    # =========================================================================

    p52 = """
    <h2>Official Mock Examination 1 &bull; Candidate Instructions</h2>
    <div style="font-size:8.5pt; color:#475569; margin-bottom:8px;"><strong>Paper Reference:</strong> FS-MATH-L1-MOCK-01 &bull; Pearson Edexcel Specification Aligned</div>

    <div class="box-concept">
      <h3 style="margin-top:0;">Examination Overview &amp; Candidate Rules</h3>
      <table class="cgp-table">
        <tr><th>Paper Section</th><th>Time Allowed</th><th>Marks Available</th><th>Permitted Equipment</th></tr>
        <tr><td><strong>Section A: Non-Calculator</strong></td><td>25 minutes</td><td>14 marks</td><td>Black ballpoint pen, pencil, eraser, ruler. (NO CALCULATOR)</td></tr>
        <tr><td><strong>Section B: Calculator Allowed</strong></td><td>1 hour 30 minutes</td><td>42 marks</td><td>Pen, pencil, ruler, protractor, electronic calculator.</td></tr>
        <tr><td><strong>Total Full Paper</strong></td><td><strong>1 hour 55 minutes</strong></td><td><strong>56 marks</strong></td><td><strong>Pass Mark: ~36 marks (65%)</strong></td></tr>
      </table>
    </div>

    <div class="grid-2col" style="margin-top:8px;">
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8;">Tips for Section A (Non-Calculator)</h3>
        <p>&bull; Spend about 1.5 minutes per mark.<br>
        &bull; Set out your column addition, subtraction, and multiplication neatly.<br>
        &bull; Use inverse operations to check your answers.<br>
        &bull; Make sure fractions are simplified where requested.</p>
      </div>
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8;">Tips for Section B (Calculator Allowed)</h3>
        <p>&bull; Always write down the calculation you type into the calculator.<br>
        &bull; State the correct units for all measurements ($£$, m, $\\text{m}^2$, kg, L).<br>
        &bull; Check that money answers have two decimal digits ($£15.50$, not $£15.5$).<br>
        &bull; Attempt every question!</p>
      </div>
    </div>
    """
    pages.append(wrap_page(p52, 52, "Official Mock Examination 1", "Candidate Instructions", "Maths Level 1 Companion Practice Workbook"))

    # Mock 1 Section A (Pages 53-54)
    m1_p53 = [
        (1, 3, "Calculate without using a calculator: $324 \\times 18$. Show your full column method.", 80, "Answer"),
        (2, 2, "A bank account is overdrawn at $-£120$. A wage credit of $£450$ is paid in. What is the new balance?", 75, "Balance"),
        (3, 2, "Simplify fully: $\\frac{18}{30}$.", 75, "Answer")
    ]
    pages.append(mock_page(1, "Section A (Non-Calculator)", 53, m1_p53))

    m1_p54 = [
        (4, 3, "Work out: $1,152 \\div 6$ without using a calculator. Show your bus stop division.", 80, "Answer"),
        (5, 2, "Evaluate: $24 - 4 \\times 5 + 3$.", 75, "Answer"),
        (6, 2, "Share $£80$ in the ratio $3 : 1$. What is the smaller share?", 75, "Smaller Share")
    ]
    pages.append(mock_page(1, "Section A (Non-Calculator)", 54, m1_p54))

    # Mock 1 Section B (Pages 55-59)
    m1_p55 = [
        (7, 3, "A jacket costs $£60.00$. It is reduced by $15\\%$ in a sale. Calculate the sale price.", 80, "Sale Price"),
        (8, 3, "A soup recipe serves 4 people and requires $600\\text{ ml}$ of stock. How much stock is needed for 6 people?", 80, "Stock Needed"),
        (9, 3, "A cyclist rides 25 miles. Using $5\\text{ miles} = 8\\text{ km}$, convert this distance to kilometres.", 80, "Distance in km")
    ]
    pages.append(mock_page(1, "Section B (Calculator Allowed)", 55, m1_p55))

    m1_p56 = [
        (10, 4, "A landscape gardener lays turf on a lawn measuring $7.5\\text{ m}$ by $5.0\\text{ m}$. Turf rolls cover $1\\text{ m}^2$ each and cost $£4.20$. Delivery is $£15.00$. Find total cost.", 95, "Total Cost"),
        (11, 4, "A warehouse assistant works 35 basic hours at $£11.00/\\text{hr}$, plus 4 hours overtime at time-and-a-half ($£16.50/\\text{hr}$). What is his total gross pay?", 95, "Gross Pay"),
        (12, 4, "A water cistern measures $1.2\\text{ m}$ long, $0.8\\text{ m}$ wide, and $0.5\\text{ m}$ deep. How many litres of water does it hold? ($1\\text{ m}^3 = 1000\\text{ litres}$)", 95, "Capacity in Litres")
    ]
    pages.append(mock_page(1, "Section B (Calculator Allowed)", 56, m1_p56))

    m1_p57 = [
        (13, 4, "A bus leaves the terminal at 08:35 and arrives at the retail park at 09:22. How long did the journey take?", 95, "Journey Time"),
        (14, 4, "Test scores of 5 apprentices: $12, 16, 14, 18, 15$. Calculate: a) The mean score &emsp; b) The range.", 95, "Mean & Range")
    ]
    pages.append(mock_page(1, "Section B (Calculator Allowed)", 57, m1_p57))

    m1_p58 = [
        (15, 5, "On a scale plan ($1 : 50$), a meeting room measures $10\\text{ cm}$ by $8\\text{ cm}$. Calculate the real perimeter of the room in metres, and the real area in square metres.", 115, "Perimeter & Area"),
        (16, 5, "A dental practice audits 80 patients: 50 are adults. 35 adults had a check-up. 20 children had a check-up. Construct a two-way table. What is the probability that a patient chosen at random had a check-up?", 115, "Probability")
    ]
    pages.append(mock_page(1, "Section B (Calculator Allowed)", 58, m1_p58))

    m1_p59 = [
        (17, 4, "In a pie chart of 120 staff, the sector for 'Walk to work' is a right angle ($90^\\circ$). How many staff walk to work? What fraction is this?", 100, "Walk to work"),
        (18, 4, "A bag contains 6 blue counters, 4 red counters, and 10 yellow counters. A counter is chosen at random. Find: a) P(Blue) in simplest form &emsp; b) P(Not Red).", 100, "Probabilities")
    ]
    pages.append(mock_page(1, "Section B (Calculator Allowed)", 59, m1_p59))

    # =========================================================================
    # OFFICIAL MOCK EXAMINATION 2 (PAGES 60 - 67: 8 pages)
    # =========================================================================

    p60 = """
    <h2>Official Mock Examination 2 &bull; Candidate Instructions</h2>
    <div style="font-size:8.5pt; color:#475569; margin-bottom:8px;"><strong>Paper Reference:</strong> FS-MATH-L1-MOCK-02 &bull; Pearson Edexcel Specification Aligned</div>

    <div class="box-concept">
      <h3 style="margin-top:0;">Examination Overview &amp; Candidate Rules</h3>
      <table class="cgp-table">
        <tr><th>Paper Section</th><th>Time Allowed</th><th>Marks Available</th><th>Permitted Equipment</th></tr>
        <tr><td><strong>Section A: Non-Calculator</strong></td><td>25 minutes</td><td>14 marks</td><td>Black ballpoint pen, pencil, eraser, ruler. (NO CALCULATOR)</td></tr>
        <tr><td><strong>Section B: Calculator Allowed</strong></td><td>1 hour 30 minutes</td><td>42 marks</td><td>Pen, pencil, ruler, protractor, electronic calculator.</td></tr>
        <tr><td><strong>Total Full Paper</strong></td><td><strong>1 hour 55 minutes</strong></td><td><strong>56 marks</strong></td><td><strong>Pass Mark: ~36 marks (65%)</strong></td></tr>
      </table>
    </div>

    <div class="grid-2col" style="margin-top:8px;">
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8;">Final Preparation Reminders</h3>
        <p>&bull; Read each question carefully and underline numbers and units.<br>
        &bull; Show all stages of working in the ruled boxes.<br>
        &bull; Check addition and multiplication using inverse operations.<br>
        &bull; Keep your handwriting clear and legible.</p>
      </div>
      <div class="box-formula">
        <h3 style="margin-top:0; color:#1d4ed8;">Passing Benchmark Guidance</h3>
        <p>&bull; <strong>Target Pass Score:</strong> 36 marks out of 56 (approx. 65%).<br>
        &bull; A strong performance in Section A sets a solid foundation.<br>
        &bull; Section B offers generous method marks &mdash; always show your steps!</p>
      </div>
    </div>
    """
    pages.append(wrap_page(p60, 60, "Official Mock Examination 2", "Candidate Instructions", "Maths Level 1 Companion Practice Workbook"))

    # Mock 2 Section A (Pages 61-62)
    m2_p61 = [
        (1, 3, "Work out without a calculator: $256 \\times 23$. Show your full column method.", 80, "Answer"),
        (2, 2, "A freezer compartment is at $-14^\\circ\\text{C}$. The temperature rises by $6^\\circ\\text{C}$. What is the new temperature?", 75, "New Temp"),
        (3, 2, "Simplify fully: $\\frac{12}{28}$.", 75, "Answer")
    ]
    pages.append(mock_page(2, "Section A (Non-Calculator)", 61, m2_p61))

    m2_p62 = [
        (4, 3, "Work out: $1,476 \\div 9$ without using a calculator. Show your bus stop division.", 80, "Answer"),
        (5, 2, "Evaluate: $30 - 5 \\times 4 + 6$.", 75, "Answer"),
        (6, 2, "Share $£90$ in the ratio $4 : 1$. What is the larger share?", 75, "Larger Share")
    ]
    pages.append(mock_page(2, "Section A (Non-Calculator)", 62, m2_p62))

    # Mock 2 Section B (Pages 63-67)
    m2_p63 = [
        (7, 3, "A television costs $£240.00$. It is discounted by $25\\%$ in a sale. Calculate the sale price.", 80, "Sale Price"),
        (8, 3, "A pancake recipe for 4 people requires $200\\text{ g}$ flour and $2$ eggs. How much flour and how many eggs are needed for 10 people?", 80, "Flour & Eggs"),
        (9, 3, "A delivery van travels 50 miles. Using $5\\text{ miles} = 8\\text{ km}$, convert 50 miles to kilometres.", 80, "Distance in km")
    ]
    pages.append(mock_page(2, "Section B (Calculator Allowed)", 63, m2_p63))

    m2_p64 = [
        (10, 4, "A landscape gardener lays turf on a rectangular lawn measuring $9.0\\text{ m}$ by $4.5\\text{ m}$. Turf rolls cover $1\\text{ m}^2$ each and cost $£4.80$. Delivery is $£18.00$. Calculate the total cost.", 95, "Total Cost"),
        (11, 4, "A care worker works 32 basic hours at $£11.25/\\text{hr}$, plus 6 hours overtime at time-and-a-half ($£16.88/\\text{hr}$). What is her total gross pay?", 95, "Gross Pay"),
        (12, 4, "A water cistern measures $1.5\\text{ m}$ long, $0.6\\text{ m}$ wide, and $0.4\\text{ m}$ high. How many litres of water does it hold when full?", 95, "Capacity in Litres")
    ]
    pages.append(mock_page(2, "Section B (Calculator Allowed)", 64, m2_p64))

    m2_p65 = [
        (13, 4, "A train departs Leeds at 14:25 and arrives in York at 15:02. How long did the journey take?", 95, "Journey Time"),
        (14, 4, "Daily sales by a sales assistant: Mon 18, Tue 24, Wed 20, Thu 28, Fri 25. Calculate: a) The mean daily sales &emsp; b) The range.", 95, "Mean & Range")
    ]
    pages.append(mock_page(2, "Section B (Calculator Allowed)", 65, m2_p65))

    m2_p66 = [
        (15, 5, "On a scale plan ($1 : 100$), a workshop measures $8\\text{ cm}$ by $6\\text{ cm}$. Calculate the real perimeter of the workshop in metres, and the real area in square metres.", 115, "Perimeter & Area"),
        (16, 5, "A veterinary clinic audits 120 animals: 70 are dogs. 42 dogs received a rabies vaccine. 28 cats received a rabies vaccine. Construct a two-way table. What is the probability that an animal chosen at random was vaccinated?", 115, "Probability")
    ]
    pages.append(mock_page(2, "Section B (Calculator Allowed)", 66, m2_p66))

    m2_p67 = [
        (17, 4, "A pie chart shows favourite sports of 80 students: Half chose Football ($180^\\circ$), quarter chose Basketball ($90^\\circ$), quarter chose Tennis. How many students chose Football?", 100, "Football"),
        (18, 4, "A box holds 8 blue pens, 5 black pens, and 7 green pens. A pen is chosen at random. Find: a) P(Black) as a fraction &emsp; b) P(Not Blue).", 100, "Probabilities")
    ]
    pages.append(mock_page(2, "Section B (Calculator Allowed)", 67, m2_p67))

    # =========================================================================
    # ANSWER KEYS & DETAILED MARK SCHEMES (PAGES 68 - 87: 20 pages)
    # =========================================================================

    ans_p68 = """
    <h3 style="color:var(--theme); margin-top:2px;">Module 1 Practice Answers (Pages 3-8)</h3>
    <table class="cgp-table" style="font-size:7.4pt;">
      <tr><th style="width:12%;">Page / Topic</th><th style="width:25%;">Task 1 (Warm-Up)</th><th style="width:30%;">Task 2 (Workplace)</th><th>Task 3 (Exam Challenge)</th></tr>
      <tr><td>P3: Place Value</td><td>a) 42,508 &ensp; b) Three hundred and six thousand...</td><td>New Temp: <strong>-7°C</strong></td><td>Balance: <strong>£325.00</strong></td></tr>
      <tr><td>P4: Add/Sub</td><td>a) 3,843 &ensp; b) 2,325</td><td>Total: <strong>1,455 masks</strong></td><td>Remaining: <strong>858 laptops</strong></td></tr>
      <tr><td>P5: Mult/Div</td><td>a) 4,248 &ensp; b) 136</td><td>Total: <strong>840 tins</strong></td><td>Tables: <strong>54 tables</strong></td></tr>
      <tr><td>P6: Powers 10</td><td>a) 3,400 &ensp; b) 58 &ensp; c) 42 &ensp; d) 6.5</td><td>Total: <strong>£345.00</strong></td><td>Washers: <strong>85 washers</strong></td></tr>
      <tr><td>P7: BIDMAS</td><td>a) 29 &ensp; b) 4 &ensp; c) 18 &ensp; d) 6</td><td>Hire Cost: <strong>£90.00</strong></td><td>Charge: <strong>£280.00</strong></td></tr>
      <tr><td>P8: Fractions</td><td>a) 2/3 &ensp; b) 2/5 &ensp; c) 3/4 &ensp; d) 1/3</td><td>a) 10 &ensp; b) 32 &ensp; c) 6</td><td>Order: 5/16, 3/8, 1/2, 3/4</td></tr>
    </table>
    """
    pages.append(mark_scheme_page("Practice Drills Answer Keys", "Module 1 (Pages 3-8)", 68, ans_p68))

    ans_p69 = """
    <h3 style="color:var(--theme); margin-top:2px;">Module 1 Practice Answers (Pages 9-13)</h3>
    <table class="cgp-table" style="font-size:7.4pt;">
      <tr><th style="width:12%;">Page / Topic</th><th style="width:25%;">Task 1 (Warm-Up)</th><th style="width:30%;">Task 2 (Workplace)</th><th>Task 3 (Exam Challenge)</th></tr>
      <tr><td>P9: Fract Amounts</td><td>a) £15 &ensp; b) 16 kg &ensp; c) £45 &ensp; d) 10 m</td><td>Remaining: <strong>150 capsules</strong></td><td>Remaining: <strong>£500.00</strong></td></tr>
      <tr><td>P10: Decimals</td><td>a) 24.35 &ensp; b) 25.65 &ensp; c) 32.0 &ensp; d) 6.20</td><td>Change: <strong>£7.60</strong></td><td>Total Cost: <strong>£56.50</strong></td></tr>
      <tr><td>P11: Percentages</td><td>a) £42 &ensp; b) 15 kg &ensp; c) £35 &ensp; d) £9</td><td>Sale Price: <strong>£240.00</strong></td><td>New Salary: <strong>£22,050.00</strong></td></tr>
      <tr><td>P12: FDP Equiv</td><td>a) 0.5, 50% &ensp; b) 1/4, 25%</td><td>Larger: <strong>65% (65% > 60%)</strong></td><td>Order: 1/4 (25%), 0.28, 0.3, 35%, 2/5</td></tr>
      <tr><td>P13: Ratio</td><td>a) £40, £20 &ensp; b) 15 kg, 25 kg</td><td>Orange: <strong>9 litres</strong></td><td>Cement: <strong>9 kg</strong></td></tr>
    </table>
    """
    pages.append(mark_scheme_page("Practice Drills Answer Keys", "Module 1 (Pages 9-13)", 69, ans_p69))

    ans_p70 = """
    <h3 style="color:var(--theme); margin-top:2px;">Module 2 Practice Answers (Pages 18-24)</h3>
    <table class="cgp-table" style="font-size:7.4pt;">
      <tr><th style="width:12%;">Page / Topic</th><th style="width:25%;">Task 1 (Warm-Up)</th><th style="width:30%;">Task 2 (Workplace)</th><th>Task 3 (Exam Challenge)</th></tr>
      <tr><td>P18: Length</td><td>a) 450cm &ensp; b) 2.5m &ensp; c) 6.5cm &ensp; d) 3200m</td><td>Remaining: <strong>60 cm</strong></td><td>Laps: <strong>12.5 laps</strong></td></tr>
      <tr><td>P19: Weight/Cap</td><td>a) 3200g &ensp; b) 0.75L &ensp; c) 4.5kg &ensp; d) 1500ml</td><td>Remaining: <strong>2,900 g</strong></td><td>Bottles: <strong>3 bottles</strong> (420 ml)</td></tr>
      <tr><td>P20: Imperial</td><td>a) 40 km &ensp; b) 25 mi &ensp; c) 25 cm</td><td>39.6 lbs; <strong>Yes, within limit</strong></td><td>Distance: <strong>75 miles</strong></td></tr>
      <tr><td>P21: Time</td><td>a) 08:40 &ensp; b) 15:25 &ensp; c) 21:10 &ensp; d) 23:55</td><td>Duration: <strong>1 hour 33 minutes</strong></td><td>Paid Hours: <strong>7 hours 45 mins</strong></td></tr>
      <tr><td>P22: Perimeter</td><td>a) 26 m &ensp; b) 30 cm &ensp; c) 27 cm</td><td>Length: <strong>18.0 metres</strong></td><td>Total Cost: <strong>£91.00</strong></td></tr>
      <tr><td>P23: 2D Area</td><td>a) 28 m² &ensp; b) 81 cm² &ensp; c) 96 m²</td><td>Carpet: <strong>£216.00</strong></td><td>Tins: <strong>2 tins</strong> (15.6 m²)</td></tr>
      <tr><td>P24: Comp Area</td><td>Total Area: <strong>30 m²</strong></td><td>Floor Area: <strong>28 m²</strong></td><td>Total Cost: <strong>£216.60</strong></td></tr>
    </table>
    """
    pages.append(mark_scheme_page("Practice Drills Answer Keys", "Module 2 (Pages 18-24)", 70, ans_p70))

    ans_p71 = """
    <h3 style="color:var(--theme); margin-top:2px;">Module 2 Practice Answers (Pages 25-30)</h3>
    <table class="cgp-table" style="font-size:7.4pt;">
      <tr><th style="width:12%;">Page / Topic</th><th style="width:25%;">Task 1 (Warm-Up)</th><th style="width:30%;">Task 2 (Workplace)</th><th>Task 3 (Exam Challenge)</th></tr>
      <tr><td>P25: Volume</td><td>a) 200 cm³ &ensp; b) 2.4 m³</td><td>Capacity: <strong>72 litres</strong></td><td>Bags: <strong>36 bags</strong> (1.8 m³)</td></tr>
      <tr><td>P26: Angles</td><td>a) Acute &ensp; b) Right &ensp; c) Obtuse &ensp; d) Straight</td><td>Missing: <strong>52°</strong></td><td>Base Angles: <strong>70° each</strong></td></tr>
      <tr><td>P27: 3D Shapes</td><td>Cube: 6,12,8 &ensp; Prism: 5,9,6 &ensp; Pyr: 5,8,5</td><td>Solid: <strong>Cuboid</strong></td><td>2 flat circular, 1 curved, 2 edges</td></tr>
      <tr><td>P28: Scales</td><td>a) 12 m &ensp; b) 6 cm</td><td>Real: <strong>7 m by 5 m</strong></td><td>Width: <strong>3 grid squares</strong></td></tr>
      <tr><td>P29: Compass</td><td>a) South-West &ensp; b) East &ensp; c) West</td><td>Direction: <strong>North-West</strong></td><td>Direction: <strong>South-East</strong></td></tr>
      <tr><td>P30: Speed</td><td>a) 60 mph &ensp; b) 60 mph &ensp; c) 50 km/h</td><td>Average Speed: <strong>55 mph</strong></td><td>Time: <strong>4 hours</strong></td></tr>
    </table>
    """
    pages.append(mark_scheme_page("Practice Drills Answer Keys", "Module 2 (Pages 25-30)", 71, ans_p71))

    ans_p72 = """
    <h3 style="color:var(--theme); margin-top:2px;">Module 3 Practice Answers (Pages 35-44)</h3>
    <table class="cgp-table" style="font-size:7.4pt;">
      <tr><th style="width:12%;">Page / Topic</th><th style="width:25%;">Task 1 (Warm-Up)</th><th style="width:30%;">Task 2 (Workplace)</th><th>Task 3 (Exam Challenge)</th></tr>
      <tr><td>P35: Tally</td><td>Total Verified: <strong>30</strong></td><td>Fraction: <strong>3/4</strong></td><td>Pass Rate: <strong>56%</strong></td></tr>
      <tr><td>P36: Bar Charts</td><td>a) Dept D (80) &ensp; b) 240</td><td>Difference: <strong>40</strong></td><td>Missing 15; scale non-linear</td></tr>
      <tr><td>P37: Dual Charts</td><td>Week 2 Total: <strong>125</strong></td><td>Tuesday (+10)</td><td>Week 2 sales consistently higher</td></tr>
      <tr><td>P38: Pictograms</td><td>a) 30 &ensp; b) 45 &ensp; c) 22.5 (or 22)</td><td>Total Books: <strong>76 books</strong></td><td>Symbols: <strong>3.5 symbols</strong></td></tr>
      <tr><td>P39: Line Graphs</td><td>09:00: 16°C &ensp; 11:00: 20°C</td><td>Steady upward sales trend</td><td>Dollars: <strong>$78</strong></td></tr>
      <tr><td>P40: Pie Charts</td><td>a) 80 &ensp; b) 40 &ensp; c) 120</td><td>Walk: <strong>30 staff</strong></td><td>Rent: £1,200; Food: £600</td></tr>
      <tr><td>P41: Mean</td><td>a) 9 &ensp; b) 20</td><td>Mean Drops: <strong>38 drops</strong></td><td>New Mean: <strong>25 years</strong></td></tr>
      <tr><td>P42: Range</td><td>a) 17 &ensp; b) 19</td><td>Range: <strong>14 minutes</strong></td><td>Line A (range 4 vs 22)</td></tr>
      <tr><td>P43: Probability</td><td>a) 1 &ensp; b) 0.5 &ensp; c) 0 &ensp; d) 0.75</td><td>a) 1/6 &ensp; b) 1/2 &ensp; c) 4/6 (2/3)</td><td>P(Yellow): <strong>1/5</strong> (0.2)</td></tr>
      <tr><td>P44: Outcomes</td><td>Total Outcomes: <strong>8</strong></td><td>Combinations: <strong>8</strong></td><td>Probability: <strong>1/2</strong></td></tr>
    </table>
    """
    pages.append(mark_scheme_page("Practice Drills Answer Keys", "Module 3 (Pages 35-44)", 72, ans_p72))

    ans_p73 = """
    <h3 style="color:var(--theme); margin-top:2px;">Synoptic Case Studies Answers (Pages 49-51)</h3>
    <table class="cgp-table" style="font-size:7.4pt;">
      <tr><th style="width:18%;">Case Study</th><th style="width:38%;">Part A Solutions &amp; Marking Method</th><th>Part B Solutions &amp; Marking Method</th></tr>
      <tr>
        <td><strong>Case Study 1:<br>NHS Healthcare</strong></td>
        <td>a) Total fluid: (2×200) + 250 + 180 + (3×250) = 400 + 250 + 180 + 750 = <strong>1,580 ml</strong> [M1, A1]<br>
        b) Target is 2.0 L = 2,000 ml. Did NOT meet target; under by 2000 - 1580 = <strong>420 ml</strong> [M1, A1].</td>
        <td>Gloves: 15 × £4.50 = £67.50. Wipes: 8 × £3.25 = £26.00.<br>
        Subtotal: 67.50 + 26.00 = £93.50 [M1].<br>
        Order is over £80 &rarr; 10% discount: 0.10 × 93.50 = £9.35 [M1].<br>
        Final total: 93.50 - 9.35 = <strong>£84.15</strong> [A1, B1].</td>
      </tr>
      <tr>
        <td><strong>Case Study 2:<br>Construction</strong></td>
        <td>a) Patio area: 6 × 4 = <strong>24 m²</strong> [M1, A1].<br>
        b) Slabs needed: 24 ÷ 0.25 = <strong>96 slabs</strong> [M1, A1].<br>
        c) Packs: 96 ÷ 10 = 9.6 &rarr; 10 packs; Cost = 10 × £35 = <strong>£350.00</strong> [M1, A1].</td>
        <td>Perimeter: 2 × (12 + 8) = 2 × 20 = 40 m [M1].<br>
        Deduct 2 m gate: 40 - 2 = 38 m [M1].<br>
        Cost: 38 × £8.50 = <strong>£323.00</strong> [A1, B1].</td>
      </tr>
      <tr>
        <td><strong>Case Study 3:<br>Logistics</strong></td>
        <td>Driving time: 90 ÷ 45 = 2.0 hours [M1].<br>
        Departs 06:45 + 2h drive = 08:45 [M1].<br>
        Add 30 mins unloading: 08:45 + 30m = <strong>09:15</strong> [A1, B1].</td>
        <td>a) Total weight: 8 × 350 = <strong>2,800 kg</strong> [M1, A1].<br>
        b) 3.0 tonnes = <strong>3,000 kg</strong> [B1].<br>
        c) 2,800 kg &le; 3,000 kg &rarr; <strong>Yes, within limit</strong> by 200 kg [A1].</td>
      </tr>
    </table>
    """
    pages.append(mark_scheme_page("Synoptic Case Studies Answers", "Integrated Scenarios (Pages 49-51)", 73, ans_p73))

    # Pages 74-79: Strand Checkpoints 1, 2, 3 Mark Schemes (6 pages)
    ms_p74 = """
    <h3 style="color:var(--theme); margin-top:2px;">Strand 1 Checkpoint &bull; Non-Calculator Mark Scheme (Pages 14-15)</h3>
    <table class="cgp-table" style="font-size:7.4pt;">
      <tr><th style="width:8%;">Q</th><th style="width:12%;">Marks</th><th style="width:25%;">Correct Answer</th><th>Mark Scheme &amp; Detailed Method Guidance</th></tr>
      <tr><td>1</td><td>2</td><td><strong>6,688</strong></td><td><strong>[M1]</strong> 418 × 6 = 2,508; 418 × 10 = 4,180 <strong>[A1]</strong> 2508 + 4180 = 6,688.</td></tr>
      <tr><td>2</td><td>2</td><td><strong>£355.00</strong></td><td><strong>[M1]</strong> -145 + 500 <strong>[A1]</strong> £355.00.</td></tr>
      <tr><td>3</td><td>2</td><td><strong>3/4; 40%</strong></td><td><strong>[B1]</strong> 15/20 = 3/4 <strong>[B1]</strong> 2/5 = 4/10 = 40%.</td></tr>
      <tr><td>4</td><td>2</td><td><strong>228</strong></td><td><strong>[M1]</strong> 6 into 13 = 2 r 1; 6 into 16 = 2 r 4; 6 into 48 = 8 <strong>[A1]</strong> 228.</td></tr>
      <tr><td>5</td><td>2</td><td><strong>5</strong></td><td><strong>[M1]</strong> Multiplication first: 3 × 4 = 12; 15 - 12 + 2 <strong>[A1]</strong> 5.</td></tr>
      <tr><td>6</td><td>2</td><td><strong>£80.00</strong></td><td><strong>[M1]</strong> 4+3 = 7 parts; 140 ÷ 7 = 20; 4 × 20 <strong>[A1]</strong> £80.00.</td></tr>
    </table>
    """
    pages.append(mark_scheme_page("Checkpoint Mark Scheme", "Strand 1 Checkpoint &bull; Non-Calc (Q1-Q6)", 74, ms_p74))

    ms_p75 = """
    <h3 style="color:var(--theme); margin-top:2px;">Strand 1 Checkpoint &bull; Calculator Mark Scheme (Pages 16-17)</h3>
    <table class="cgp-table" style="font-size:7.4pt;">
      <tr><th style="width:8%;">Q</th><th style="width:12%;">Marks</th><th style="width:25%;">Correct Answer</th><th>Mark Scheme &amp; Detailed Method Guidance</th></tr>
      <tr><td>7</td><td>3</td><td><strong>£120.00</strong></td><td><strong>[P1]</strong> 20% of 150 = £30 <strong>[M1]</strong> 150 - 30 <strong>[A1]</strong> £120.00.</td></tr>
      <tr><td>8</td><td>3</td><td><strong>560 g</strong></td><td><strong>[P1]</strong> 320 ÷ 4 = 80 g per person <strong>[M1]</strong> 80 × 7 <strong>[A1]</strong> 560 g.</td></tr>
      <tr><td>9</td><td>3</td><td><strong>150 parcels</strong></td><td><strong>[P1]</strong> 400 ÷ 8 = 50; 50 × 5 = 250 delivered <strong>[M1]</strong> 400 - 250 <strong>[A1]</strong> 150 parcels.</td></tr>
      <tr><td>10</td><td>3</td><td><strong>£165.00</strong></td><td><strong>[P1]</strong> 5 × 25 = £125 <strong>[M1]</strong> 125 + 40 <strong>[A1]</strong> £165.00.</td></tr>
      <tr><td>11</td><td>3</td><td><strong>Pack B is cheaper</strong></td><td><strong>[P1]</strong> Pack A: 5.20 ÷ 4 = £1.30; Pack B: 7.20 ÷ 6 = £1.20 <strong>[M1]</strong> Compare <strong>[A1]</strong> Pack B by 10p/bulb.</td></tr>
      <tr><td>12</td><td>3</td><td><strong>No (needs £173)</strong></td><td><strong>[P1]</strong> Slabs: 18 × 8.50 = £153.00 <strong>[M1]</strong> 153 + 20 = £173.00 <strong>[A1]</strong> £173 > £170, so £3 short.</td></tr>
    </table>
    """
    pages.append(mark_scheme_page("Checkpoint Mark Scheme", "Strand 1 Checkpoint &bull; Calculator (Q7-Q12)", 75, ms_p75))

    ms_p76 = """
    <h3 style="color:var(--theme); margin-top:2px;">Strand 2 Checkpoint &bull; Non-Calculator Mark Scheme (Pages 31-32)</h3>
    <table class="cgp-table" style="font-size:7.4pt;">
      <tr><th style="width:8%;">Q</th><th style="width:12%;">Marks</th><th style="width:25%;">Correct Answer</th><th>Mark Scheme &amp; Detailed Method Guidance</th></tr>
      <tr><td>1</td><td>2</td><td><strong>360 cm; 0.85 kg</strong></td><td><strong>[B1]</strong> 360 cm <strong>[B1]</strong> 0.85 kg.</td></tr>
      <tr><td>2</td><td>2</td><td><strong>1h 50m (110 mins)</strong></td><td><strong>[M1]</strong> 19:15 to 20:15 = 1h; 20:15 to 21:05 = 50m <strong>[A1]</strong> 1 hour 50 minutes.</td></tr>
      <tr><td>3</td><td>2</td><td><strong>27 metres</strong></td><td><strong>[M1]</strong> 2 × (9 + 4.5) = 2 × 13.5 <strong>[A1]</strong> 27 metres.</td></tr>
      <tr><td>4</td><td>2</td><td><strong>49 m²</strong></td><td><strong>[M1]</strong> 7 × 7 <strong>[A1]</strong> 49 m².</td></tr>
      <tr><td>5</td><td>2</td><td><strong>6 full glasses</strong></td><td><strong>[M1]</strong> 1500 ÷ 250 <strong>[A1]</strong> 6 glasses.</td></tr>
      <tr><td>6</td><td>2</td><td><strong>9 edges, 6 vertices</strong></td><td><strong>[B1]</strong> 9 edges <strong>[B1]</strong> 6 vertices.</td></tr>
    </table>
    """
    pages.append(mark_scheme_page("Checkpoint Mark Scheme", "Strand 2 Checkpoint &bull; Non-Calc (Q1-Q6)", 76, ms_p76))

    ms_p77 = """
    <h3 style="color:var(--theme); margin-top:2px;">Strand 2 Checkpoint &bull; Calculator Mark Scheme (Pages 33-34)</h3>
    <table class="cgp-table" style="font-size:7.4pt;">
      <tr><th style="width:8%;">Q</th><th style="width:12%;">Marks</th><th style="width:25%;">Correct Answer</th><th>Mark Scheme &amp; Detailed Method Guidance</th></tr>
      <tr><td>7</td><td>3</td><td><strong>£346.50</strong></td><td><strong>[P1]</strong> Area = 5.0 × 4.2 = 21 m² <strong>[M1]</strong> 21 × £16.50 <strong>[A1]</strong> £346.50.</td></tr>
      <tr><td>8</td><td>3</td><td><strong>56 km</strong></td><td><strong>[P1]</strong> (35 ÷ 5) × 8 = 7 × 8 <strong>[M1]</strong> Calculation <strong>[A1]</strong> 56 km.</td></tr>
      <tr><td>9</td><td>3</td><td><strong>560 litres</strong></td><td><strong>[P1]</strong> Volume = 1.4 × 0.8 × 0.5 = 0.56 m³ <strong>[M1]</strong> 0.56 × 1000 <strong>[A1]</strong> 560 litres.</td></tr>
      <tr><td>10</td><td>3</td><td><strong>£427.50</strong></td><td><strong>[P1]</strong> Basic: 30 × 11.40 = £342; OT: 5 × 17.10 = £85.50 <strong>[M1]</strong> 342 + 85.50 <strong>[A1]</strong> £427.50.</td></tr>
      <tr><td>11</td><td>3</td><td><strong>170 metres</strong></td><td><strong>[P1]</strong> 8.5 × 20 <strong>[M1]</strong> Calculation <strong>[A1]</strong> 170 metres.</td></tr>
      <tr><td>12</td><td>3</td><td><strong>£161.20</strong></td><td><strong>[P1]</strong> Area: (5×4) + (3×2) = 20 + 6 = 26 m² <strong>[M1]</strong> 26 × £6.20 <strong>[A1]</strong> £161.20.</td></tr>
    </table>
    """
    pages.append(mark_scheme_page("Checkpoint Mark Scheme", "Strand 2 Checkpoint &bull; Calculator (Q7-Q12)", 77, ms_p77))

    ms_p78 = """
    <h3 style="color:var(--theme); margin-top:2px;">Strand 3 Checkpoint &bull; Non-Calculator Mark Scheme (Pages 45-46)</h3>
    <table class="cgp-table" style="font-size:7.4pt;">
      <tr><th style="width:8%;">Q</th><th style="width:12%;">Marks</th><th style="width:25%;">Correct Answer</th><th>Mark Scheme &amp; Detailed Method Guidance</th></tr>
      <tr><td>1</td><td>2</td><td><strong>Mean = 16; Range = 8</strong></td><td><strong>[M1]</strong> Sum = 80; 80 ÷ 5 = 16 <strong>[A1]</strong> Range = 20 - 12 = 8.</td></tr>
      <tr><td>2</td><td>2</td><td><strong>3/8</strong></td><td><strong>[M1]</strong> Outcomes: 1, 2, 3; 3/8 <strong>[A1]</strong> 3/8.</td></tr>
      <tr><td>3</td><td>2</td><td><strong>16</strong></td><td><strong>[B1]</strong> 5 + 5 + 5 + 1 = 16.</td></tr>
      <tr><td>4</td><td>2</td><td><strong>5/20 (1/4)</strong></td><td><strong>[M1]</strong> Total = 20; 5/20 <strong>[A1]</strong> 1/4.</td></tr>
      <tr><td>5</td><td>2</td><td><strong>Coffee</strong></td><td><strong>[B1]</strong> Highest bar = Coffee (45).</td></tr>
      <tr><td>6</td><td>2</td><td><strong>48 Euros</strong></td><td><strong>[M1]</strong> £40 = 4 × £10; 4 × 12 Euros <strong>[A1]</strong> 48 Euros.</td></tr>
    </table>
    """
    pages.append(mark_scheme_page("Checkpoint Mark Scheme", "Strand 3 Checkpoint &bull; Non-Calc (Q1-Q6)", 78, ms_p78))

    ms_p79 = """
    <h3 style="color:var(--theme); margin-top:2px;">Strand 3 Checkpoint &bull; Calculator Mark Scheme (Pages 47-48)</h3>
    <table class="cgp-table" style="font-size:7.4pt;">
      <tr><th style="width:8%;">Q</th><th style="width:12%;">Marks</th><th style="width:25%;">Correct Answer</th><th>Mark Scheme &amp; Detailed Method Guidance</th></tr>
      <tr><td>7</td><td>3</td><td><strong>32 calls</strong></td><td><strong>[P1]</strong> Sum = 28+34+30+36+32 = 160 <strong>[M1]</strong> 160 ÷ 5 <strong>[A1]</strong> 32 calls.</td></tr>
      <tr><td>8</td><td>3</td><td><strong>40 students</strong></td><td><strong>[P1]</strong> 90° = 1/4 <strong>[M1]</strong> 160 ÷ 4 <strong>[A1]</strong> 40 students.</td></tr>
      <tr><td>9</td><td>3</td><td><strong>45 awards</strong></td><td><strong>[P1]</strong> Y7: 4 × 6 = 24; Y8: 3.5 × 6 = 21 <strong>[M1]</strong> 24 + 21 <strong>[A1]</strong> 45 awards.</td></tr>
      <tr><td>10</td><td>3</td><td><strong>Shift 1 more consistent</strong></td><td><strong>[P1]</strong> Identical mean (45) <strong>[M1]</strong> Shift 1 range 3 vs Shift 2 range 14 <strong>[A1]</strong> Valid consistency statement.</td></tr>
      <tr><td>11</td><td>3</td><td><strong>0.92 (23/25)</strong></td><td><strong>[P1]</strong> Good components: 25 - 2 = 23 <strong>[M1]</strong> 23 ÷ 25 <strong>[A1]</strong> 0.92 (or 92%).</td></tr>
      <tr><td>12</td><td>3</td><td><strong>44%</strong></td><td><strong>[P1]</strong> (22 ÷ 50) <strong>[M1]</strong> × 100 <strong>[A1]</strong> 44%.</td></tr>
    </table>
    """
    pages.append(mark_scheme_page("Checkpoint Mark Scheme", "Strand 3 Checkpoint &bull; Calculator (Q7-Q12)", 79, ms_p79))

    # Pages 80-83: Mock Exam 1 Mark Scheme (4 pages)
    ms_m1_80 = """
    <h3 style="color:var(--theme); margin-top:2px;">Official Mock Exam 1 &bull; Section A Mark Scheme (Pages 53-54)</h3>
    <table class="cgp-table" style="font-size:7.4pt;">
      <tr><th style="width:8%;">Q</th><th style="width:12%;">Marks</th><th style="width:25%;">Correct Answer</th><th>Mark Scheme &amp; Detailed Method Guidance</th></tr>
      <tr><td>1</td><td>3</td><td><strong>5,832</strong></td><td><strong>[M1]</strong> 324 × 8 = 2,592 <strong>[M1]</strong> 324 × 10 = 3,240 <strong>[A1]</strong> 2592 + 3240 = 5,832.</td></tr>
      <tr><td>2</td><td>2</td><td><strong>£330.00</strong></td><td><strong>[M1]</strong> -120 + 450 <strong>[A1]</strong> £330.00.</td></tr>
      <tr><td>3</td><td>2</td><td><strong>3/5</strong></td><td><strong>[M1]</strong> Divide top and bottom by 6 <strong>[A1]</strong> 3/5.</td></tr>
      <tr><td>4</td><td>3</td><td><strong>192</strong></td><td><strong>[M1]</strong> 6 into 11 = 1 r 5; 6 into 55 = 9 r 1; 6 into 12 = 2 <strong>[A1]</strong> 192.</td></tr>
      <tr><td>5</td><td>2</td><td><strong>7</strong></td><td><strong>[M1]</strong> 4 × 5 = 20; 24 - 20 + 3 <strong>[A1]</strong> 7.</td></tr>
      <tr><td>6</td><td>2</td><td><strong>£20.00</strong></td><td><strong>[M1]</strong> 3+1 = 4 parts; 80 ÷ 4 = 20; 1 × 20 <strong>[A1]</strong> £20.00.</td></tr>
    </table>
    """
    pages.append(mark_scheme_page("Mock Exam 1 Mark Scheme", "Section A (Non-Calculator)", 80, ms_m1_80))

    ms_m1_81 = """
    <h3 style="color:var(--theme); margin-top:2px;">Official Mock Exam 1 &bull; Section B Mark Scheme (Pages 55-56)</h3>
    <table class="cgp-table" style="font-size:7.2pt;">
      <tr><th style="width:6%;">Q</th><th style="width:8%;">Marks</th><th style="width:22%;">Correct Answer</th><th>Mark Scheme &amp; Detailed Method Guidance</th></tr>
      <tr><td>7</td><td>3</td><td><strong>£51.00</strong></td><td><strong>[M1]</strong> 10% = £6.00; 5% = £3.00; 15% = £9.00 <strong>[M1]</strong> 60 - 9 <strong>[A1]</strong> £51.00.</td></tr>
      <tr><td>8</td><td>3</td><td><strong>900 ml</strong></td><td><strong>[M1]</strong> Scale factor: 6 ÷ 4 = 1.5 <strong>[M1]</strong> 600 × 1.5 <strong>[A1]</strong> 900 ml.</td></tr>
      <tr><td>9</td><td>3</td><td><strong>40 km</strong></td><td><strong>[M1]</strong> 25 ÷ 5 = 5 <strong>[M1]</strong> 5 × 8 <strong>[A1]</strong> 40 km.</td></tr>
      <tr><td>10</td><td>4</td><td><strong>£172.50</strong></td><td><strong>[P1]</strong> Area = 7.5 × 5.0 = 37.5 m² <strong>[M1]</strong> 37.5 × £4.20 = £157.50 <strong>[M1]</strong> Add delivery: 157.50 + 15.00 <strong>[A1]</strong> £172.50.</td></tr>
      <tr><td>11</td><td>4</td><td><strong>£451.00</strong></td><td><strong>[P1]</strong> Basic: 35 × 11.00 = £385.00 <strong>[M1]</strong> OT: 4 × 16.50 = £66.00 <strong>[M1]</strong> 385 + 66 <strong>[A1]</strong> £451.00.</td></tr>
      <tr><td>12</td><td>4</td><td><strong>480 litres</strong></td><td><strong>[P1]</strong> Volume = 1.2 × 0.8 × 0.5 = 0.48 m³ <strong>[M1]</strong> 0.48 × 1000 <strong>[A1]</strong> 480 litres.</td></tr>
    </table>
    """
    pages.append(mark_scheme_page("Mock Exam 1 Mark Scheme", "Section B (Questions 7-12)", 81, ms_m1_81))

    ms_m1_82 = """
    <h3 style="color:var(--theme); margin-top:2px;">Official Mock Exam 1 &bull; Section B Mark Scheme (Pages 57-58)</h3>
    <table class="cgp-table" style="font-size:7.2pt;">
      <tr><th style="width:6%;">Q</th><th style="width:8%;">Marks</th><th style="width:22%;">Correct Answer</th><th>Mark Scheme &amp; Detailed Method Guidance</th></tr>
      <tr><td>13</td><td>4</td><td><strong>47 minutes</strong></td><td><strong>[M1]</strong> 08:35 to 09:00 = 25 mins <strong>[M1]</strong> 09:00 to 09:22 = 22 mins <strong>[A1]</strong> 25 + 22 = 47 minutes.</td></tr>
      <tr><td>14</td><td>4</td><td><strong>Mean = 15; Range = 6</strong></td><td><strong>[P1]</strong> Sum = 12+16+14+18+15 = 75 <strong>[M1]</strong> Mean: 75 ÷ 5 = 15 <strong>[M1]</strong> Range: 18 - 12 = 6 <strong>[A1]</strong> Correct values.</td></tr>
      <tr><td>15</td><td>5</td><td><strong>18 m; 20 m²</strong></td><td><strong>[P1]</strong> Real L = 10 × 50 = 500 cm = 5 m; Real W = 8 × 50 = 400 cm = 4 m <strong>[M1]</strong> Perimeter: 2 × (5 + 4) = 18 m <strong>[M1]</strong> Area: 5 × 4 = 20 m² <strong>[A1]</strong> Perimeter = 18 m <strong>[A1]</strong> Area = 20 m².</td></tr>
      <tr><td>16</td><td>5</td><td><strong>0.6875 (55/80 or 68.75%)</strong></td><td><strong>[P1]</strong> Table: Total checkups = 35 + 20 = 55 <strong>[M1]</strong> Total patients = 80 <strong>[M1]</strong> Fraction = 55 / 80 <strong>[A1]</strong> 55/80 = 11/16 = 0.6875 (accept 68.8% or 55/80).</td></tr>
    </table>
    """
    pages.append(mark_scheme_page("Mock Exam 1 Mark Scheme", "Section B (Questions 13-16)", 82, ms_m1_82))

    ms_m1_83 = """
    <h3 style="color:var(--theme); margin-top:2px;">Official Mock Exam 1 &bull; Section B Mark Scheme (Page 59)</h3>
    <table class="cgp-table" style="font-size:7.2pt;">
      <tr><th style="width:6%;">Q</th><th style="width:8%;">Marks</th><th style="width:22%;">Correct Answer</th><th>Mark Scheme &amp; Detailed Method Guidance</th></tr>
      <tr><td>17</td><td>4</td><td><strong>30 staff; 1/4</strong></td><td><strong>[P1]</strong> Right angle = 90° = 1/4 of 360° <strong>[M1]</strong> 120 ÷ 4 = 30 staff <strong>[A1]</strong> 30 staff <strong>[B1]</strong> Fraction is 1/4.</td></tr>
      <tr><td>18</td><td>4</td><td><strong>a) 3/10 &ensp; b) 16/20 (4/5)</strong></td><td><strong>[P1]</strong> Total counters = 6 + 4 + 10 = 20 <strong>[M1]</strong> Blue: 6/20 = 3/10 <strong>[M1]</strong> Not red: 20 - 4 = 16; 16/20 = 4/5 <strong>[A1]</strong> Both correct.</td></tr>
    </table>
    <div class="box-concept" style="margin-top:10px;">
      <h3 style="margin-top:0;">Mock 1 Candidate Grade Boundaries</h3>
      <p style="margin:0;"><strong>Distinction Standard (46 &ndash; 56 marks):</strong> Excellent procedural arithmetic and multi-step practical reasoning.<br>
      <strong>Pass Standard (36 &ndash; 45 marks):</strong> Secure qualification pass &bull; Ready for the live Pearson Edexcel examination.<br>
      <strong>Near Pass (30 &ndash; 35 marks):</strong> Focus revision on L-shaped areas, time jumps, and inverse checking.</p>
    </div>
    """
    pages.append(mark_scheme_page("Mock Exam 1 Mark Scheme", "Section B (Questions 17-18)", 83, ms_m1_83))

    # Pages 84-87: Mock Exam 2 Mark Scheme (4 pages)
    ms_m2_84 = """
    <h3 style="color:var(--theme); margin-top:2px;">Official Mock Exam 2 &bull; Section A Mark Scheme (Pages 61-62)</h3>
    <table class="cgp-table" style="font-size:7.4pt;">
      <tr><th style="width:8%;">Q</th><th style="width:12%;">Marks</th><th style="width:25%;">Correct Answer</th><th>Mark Scheme &amp; Detailed Method Guidance</th></tr>
      <tr><td>1</td><td>3</td><td><strong>5,888</strong></td><td><strong>[M1]</strong> 256 × 3 = 768 <strong>[M1]</strong> 256 × 20 = 5,120 <strong>[A1]</strong> 768 + 5120 = 5,888.</td></tr>
      <tr><td>2</td><td>2</td><td><strong>-8°C</strong></td><td><strong>[M1]</strong> -14 + 6 <strong>[A1]</strong> -8°C.</td></tr>
      <tr><td>3</td><td>2</td><td><strong>3/7</strong></td><td><strong>[M1]</strong> Divide top and bottom by 4 <strong>[A1]</strong> 3/7.</td></tr>
      <tr><td>4</td><td>3</td><td><strong>164</strong></td><td><strong>[M1]</strong> 9 into 14 = 1 r 5; 9 into 57 = 6 r 3; 9 into 36 = 4 <strong>[A1]</strong> 164.</td></tr>
      <tr><td>5</td><td>2</td><td><strong>16</strong></td><td><strong>[M1]</strong> 5 × 4 = 20; 30 - 20 + 6 <strong>[A1]</strong> 16.</td></tr>
      <tr><td>6</td><td>2</td><td><strong>£72.00</strong></td><td><strong>[M1]</strong> 4+1 = 5 parts; 90 ÷ 5 = 18; 4 × 18 <strong>[A1]</strong> £72.00.</td></tr>
    </table>
    """
    pages.append(mark_scheme_page("Mock Exam 2 Mark Scheme", "Section A (Non-Calculator)", 84, ms_m2_84))

    ms_m2_85 = """
    <h3 style="color:var(--theme); margin-top:2px;">Official Mock Exam 2 &bull; Section B Mark Scheme (Pages 63-64)</h3>
    <table class="cgp-table" style="font-size:7.2pt;">
      <tr><th style="width:6%;">Q</th><th style="width:8%;">Marks</th><th style="width:22%;">Correct Answer</th><th>Mark Scheme &amp; Detailed Method Guidance</th></tr>
      <tr><td>7</td><td>3</td><td><strong>£180.00</strong></td><td><strong>[M1]</strong> 25% of 240 = £60.00 <strong>[M1]</strong> 240 - 60 <strong>[A1]</strong> £180.00.</td></tr>
      <tr><td>8</td><td>3</td><td><strong>500g flour; 5 eggs</strong></td><td><strong>[M1]</strong> Multiplier: 10 ÷ 4 = 2.5 <strong>[A1]</strong> Flour: 200 × 2.5 = 500 g <strong>[A1]</strong> Eggs: 2 × 2.5 = 5 eggs.</td></tr>
      <tr><td>9</td><td>3</td><td><strong>80 km</strong></td><td><strong>[M1]</strong> 50 ÷ 5 = 10 <strong>[M1]</strong> 10 × 8 <strong>[A1]</strong> 80 km.</td></tr>
      <tr><td>10</td><td>4</td><td><strong>£212.40</strong></td><td><strong>[P1]</strong> Area = 9.0 × 4.5 = 40.5 m² <strong>[M1]</strong> 40.5 × £4.80 = £194.40 <strong>[M1]</strong> Add delivery: 194.40 + 18.00 <strong>[A1]</strong> £212.40.</td></tr>
      <tr><td>11</td><td>4</td><td><strong>£461.28</strong></td><td><strong>[P1]</strong> Basic: 32 × 11.25 = £360.00 <strong>[M1]</strong> OT: 6 × 16.88 = £101.28 <strong>[M1]</strong> 360 + 101.28 <strong>[A1]</strong> £461.28.</td></tr>
      <tr><td>12</td><td>4</td><td><strong>360 litres</strong></td><td><strong>[P1]</strong> Volume = 1.5 × 0.6 × 0.4 = 0.36 m³ <strong>[M1]</strong> 0.36 × 1000 <strong>[A1]</strong> 360 litres.</td></tr>
    </table>
    """
    pages.append(mark_scheme_page("Mock Exam 2 Mark Scheme", "Section B (Questions 7-12)", 85, ms_m2_85))

    ms_m2_86 = """
    <h3 style="color:var(--theme); margin-top:2px;">Official Mock Exam 2 &bull; Section B Mark Scheme (Pages 65-66)</h3>
    <table class="cgp-table" style="font-size:7.2pt;">
      <tr><th style="width:6%;">Q</th><th style="width:8%;">Marks</th><th style="width:22%;">Correct Answer</th><th>Mark Scheme &amp; Detailed Method Guidance</th></tr>
      <tr><td>13</td><td>4</td><td><strong>37 minutes</strong></td><td><strong>[M1]</strong> 14:25 to 15:00 = 35 mins <strong>[M1]</strong> 15:00 to 15:02 = 2 mins <strong>[A1]</strong> 35 + 2 = 37 minutes.</td></tr>
      <tr><td>14</td><td>4</td><td><strong>Mean = 23; Range = 10</strong></td><td><strong>[P1]</strong> Sum = 18+24+20+28+25 = 115 <strong>[M1]</strong> Mean: 115 ÷ 5 = 23 <strong>[M1]</strong> Range: 28 - 18 = 10 <strong>[A1]</strong> Correct values.</td></tr>
      <tr><td>15</td><td>5</td><td><strong>28 m; 48 m²</strong></td><td><strong>[P1]</strong> Real L = 8 × 100 = 800 cm = 8 m; Real W = 6 × 100 = 600 cm = 6 m <strong>[M1]</strong> Perimeter: 2 × (8 + 6) = 28 m <strong>[M1]</strong> Area: 8 × 6 = 48 m² <strong>[A1]</strong> Perimeter = 28 m <strong>[A1]</strong> Area = 48 m².</td></tr>
      <tr><td>16</td><td>5</td><td><strong>0.5833 (70/120 or 58.3%)</strong></td><td><strong>[P1]</strong> Total vaccinated = 42 + 28 = 70 <strong>[M1]</strong> Total animals = 120 <strong>[M1]</strong> Fraction = 70 / 120 <strong>[A1]</strong> 70/120 = 7/12 ≈ 0.583 (58.3%).</td></tr>
    </table>
    """
    pages.append(mark_scheme_page("Mock Exam 2 Mark Scheme", "Section B (Questions 13-16)", 86, ms_m2_86))

    ms_m2_87 = """
    <h3 style="color:var(--theme); margin-top:2px;">Official Mock Exam 2 &bull; Section B Mark Scheme (Page 67)</h3>
    <table class="cgp-table" style="font-size:7.2pt;">
      <tr><th style="width:6%;">Q</th><th style="width:8%;">Marks</th><th style="width:22%;">Correct Answer</th><th>Mark Scheme &amp; Detailed Method Guidance</th></tr>
      <tr><td>17</td><td>4</td><td><strong>40 students</strong></td><td><strong>[P1]</strong> Half circle = 180° = 1/2 of 80 <strong>[M1]</strong> 80 ÷ 2 = 40 students <strong>[A1]</strong> 40 students.</td></tr>
      <tr><td>18</td><td>4</td><td><strong>a) 5/20 (1/4) &ensp; b) 12/20 (3/5)</strong></td><td><strong>[P1]</strong> Total pens = 8 + 5 + 7 = 20 <strong>[M1]</strong> Black: 5/20 = 1/4 <strong>[M1]</strong> Not blue: 20 - 8 = 12; 12/20 = 3/5 <strong>[A1]</strong> Both correct.</td></tr>
    </table>
    <div class="box-concept" style="margin-top:10px;">
      <h3 style="margin-top:0;">Mock 2 Candidate Readiness Conclusion</h3>
      <p style="margin:0;">Congratulations on completing the Master Functional Skills Maths Level 1 Companion Practice Workbook! Scoring 36 or higher across both sections demonstrates firm readiness for your official Pearson Edexcel Functional Skills Level 1 qualification.</p>
    </div>
    """
    pages.append(mark_scheme_page("Mock Exam 2 Mark Scheme", "Section B (Questions 17-18)", 87, ms_m2_87))

    # PAGE 88: Back Cover
    pages.append(f"""
    <div class="page cover-full-page">
      <img src="file://{back_img}" class="cover-full-img" alt="Level 1 Companion Workbook Back Cover">
    </div>
    """)

    # Verify total page count in memory
    total_pages = len(pages)
    print(f"Total HTML pages assembled: {total_pages}")
    assert total_pages == 88, f"Expected 88 pages, got {total_pages}"

    # Combine into full HTML document
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Maths Level 1 Companion Practice Workbook - Master Functional Skills</title>
{get_shared_css(theme_color="#002046", accent_color="#0284c7", light_bg="#f0f7ff")}
</head>
<body>
{''.join(pages)}
</body>
</html>
"""

    temp_html = os.path.join(SCRATCH_DIR, "maths_l1_workbook_88p.html")
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"Building {out_name} via Chromium headless...")
    cmd = [
        CHROME_BIN,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--user-data-dir=/tmp/chr_l1_wb_88",
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
            print(f"Level 1 Companion Workbook PDF Result: {line}")
            return line

if __name__ == "__main__":
    build_l1_companion_workbook()
