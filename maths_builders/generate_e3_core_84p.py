#!/usr/bin/env python3
"""
books/maths_builders/generate_e3_core_84p.py
Constructs the complete 84-page MasterFunctionalSkills_Maths_Entry_Level_3_Core_Guide.pdf
Strictly mapped to Ofqual Reformed Functional Skills Mathematics Entry Level 3 Subject Content.
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

def build_e3_core_guide():
    front_img = os.path.join(BOOKS_IMG_DIR, "maths_e3_core_cover_page-1.png")
    back_img = os.path.join(BOOKS_IMG_DIR, "maths_e3_core_cover_page-2.png")
    out_name = "MasterFunctionalSkills_Maths_Entry_Level_3_Core_Guide.pdf"
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
            <span class="workspace-hint">State steps, calculations, and conclusion</span>
          </div>
          <div class="answer-line">Decision / Final Answer: <span class="answer-blank" style="min-width:180px;"></span></div>
        </div>
        """
        return wrap_page(content, page_num, "Strand Practice Drill", standard, "Maths Entry Level 3 Core Guide")

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
          <div style="background:#fff1f2; border:1px solid #fecaca; border-radius:4px; padding:3px 8px; font-size:7.5pt; font-weight:700; color:#991b1b;">
            Passing Benchmark: 70%
          </div>
        </div>
        {items_html}
        """
        return wrap_page(content, page_num, f"{strand_name} Checkpoint Review", part_label, "Maths Entry Level 3 Core Guide")

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
          <span style="font-size:7.5pt; font-weight:700; color:#475569;">Functional Skills Maths Entry 3</span>
        </div>
        {items_html}
        """
        return wrap_page(content, page_num, f"Official Mock Exam &bull; {sec_title}", "Standard Exam Simulation", "Maths Entry Level 3 Core Guide")

    # Helper for Mark Scheme pages
    def mark_scheme_page(title, sub_title, page_num, tables_html):
        content = f"""
        <div style="border-bottom:1.5px solid var(--theme); padding-bottom:3px; margin-bottom:6px;">
          <h2 style="margin:0; font-size:11pt; color:var(--theme);">{title}</h2>
          <div style="font-size:7.5pt; color:#64748b;"><strong>{sub_title}</strong> &bull; Marking Codes: [P1] Process &bull; [M1] Method &bull; [A1] Accuracy &bull; [B1] Independent</div>
        </div>
        {tables_html}
        """
        return wrap_page(content, page_num, title, sub_title, "Maths Entry Level 3 Core Guide")

    # =========================================================================
    # BUILD PAGES 1 TO 84
    # =========================================================================

    # PAGE 1: Front Cover
    pages.append(f"""
    <div class="page cover-full-page">
      <img src="file://{front_img}" class="cover-full-img" alt="Entry Level 3 Core Guide Front Cover">
    </div>
    """)

    # PAGE 2: Blueprint & Framework
    p2 = f"""
    <h2>Candidate Blueprint &amp; Accessibility Standards</h2>
    <p>Welcome to the <strong>Master Functional Skills Mathematics Entry Level 3 Core Revision Guide</strong>. This curriculum manual is engineered specifically for adult learners, vocational apprentices, and college students building rock-solid foundations in functional mathematics. Every concept is mapped strictly to the Ofqual Subject Content for Functional Skills Mathematics Entry 3.</p>

    <div class="box-concept" style="border-left-color:#991b1b; background:#fff1f2; margin:5px 0;">
      <h3 style="color:#991b1b; margin-top:0;">Dyslexia-Friendly Pedagogical Standards</h3>
      <p>This handbook strictly adheres to the British Dyslexia Association visual publishing guidelines:</p>
      <ul style="margin:4px 0 0 16px; padding:0; font-size:7.7pt;">
        <li><strong>Soft Warm Cream Background (#FDFBF7):</strong> Completely eliminates visual glare and screen-stress associated with bright white paper.</li>
        <li><strong>Specialist High-Legibility Typography:</strong> Set in Open Sans &amp; Lexend with generous letter spacing, engineered to eliminate letter-flipping.</li>
        <li><strong>Left-Aligned Ragged Margins:</strong> Never justified, preventing unpredictable white spaces ('rivers of white') that disrupt reading flow.</li>
        <li><strong>Color-Coded Visual Chunking:</strong> Every lesson is partitioned into visual cards with explicit step-by-step models and ruled workspaces.</li>
      </ul>
    </div>

    {tutor_vignette("👨‍🏫", "Tutor Marcus", "Senior Maths Specialist", "Entry Level 3 is your bridge to Level 1 and practical independence. We break every calculation down into bite-sized, visual steps so you never feel lost.")}

    <h3>Curriculum Structure &amp; Assessment Weightings</h3>
    <table class="cgp-table" style="font-size:7.5pt; margin:4px 0;">
      <thead>
        <tr><th>Curriculum Strand</th><th>Core Standards Covered</th><th>Key Skills &amp; Applications</th><th>Assessment Share</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Strand 1: Number &amp; Number Systems</strong></td>
          <td>E3.1 to E3.12</td>
          <td>Place value to 1,000, rounding, addition, subtraction, times tables, division with remainders, fractions.</td>
          <td>Approx. 40%</td>
        </tr>
        <tr>
          <td><strong>Strand 2: Measures, Shape &amp; Space</strong></td>
          <td>E3.13 to E3.22</td>
          <td>Money &amp; change, 12h/24h time, timetables, mm/cm/m/km, g/kg, ml/L, temperature, perimeter, 2D/3D shapes.</td>
          <td>Approx. 35%</td>
        </tr>
        <tr>
          <td><strong>Strand 3: Handling Information &amp; Data</strong></td>
          <td>E3.23 to E3.30</td>
          <td>Compass points &amp; grid maps, tally charts, frequency tables, pictograms, bar charts, sorting tables, probability.</td>
          <td>Approx. 25%</td>
        </tr>
      </tbody>
    </table>

    <div class="box-formula" style="border-left-color:#f59e0b; background:#fffbeb; margin-top:5px;">
      <h3 style="color:#b45309; margin-top:0;">Examination Format &amp; Marking Code</h3>
      <div style="font-size:7.5pt; color:#1e293b;">
        <strong>Section A: Non-Calculator</strong> (approx. 25 mins &bull; 10–12 marks) &bull; Mental strategies, column algorithms, fractions.<br>
        <strong>Section B: Calculator Allowed</strong> (approx. 65 mins &bull; 25–30 marks) &bull; Multi-step problem solving, timetables, bar charts, perimeter.<br>
        <strong>Marking Scheme Codes:</strong> <code>[P1]</code> Process, <code>[M1]</code> Method, <code>[A1]</code> Accuracy, <code>[B1]</code> Independent mark.
      </div>
    </div>
    """
    pages.append(wrap_page(p2, 2, "Master Functional Skills &bull; Maths Entry 3", "Candidate Blueprint", "Maths Entry Level 3 Core Guide"))

    # =========================================================================
    # STRAND 1: NUMBER & NUMBER SYSTEMS (Units 1 to 10 & Checkpoint)
    # =========================================================================

    # TOPIC 1: PAGE 3 (Theory) & PAGE 4 (Practice)
    p3 = f"""
    <h2>Unit 1: Numbers up to 1,000 &amp; Place Value</h2>
    <p>Understanding 3-digit whole numbers, reading and writing in figures and words, and recognizing the exact value of each digit.</p>

    <div class="box-concept">
      <span class="tag-label tag-blue">Key Principle</span> <strong>Hundreds (H), Tens (T), and Ones/Units (U):</strong>
      In any 3-digit number, position determines value. In the number <strong>748</strong>:
      <ul style="margin:3px 0 0 16px; padding:0; font-size:7.7pt;">
        <li><strong>7</strong> is in the Hundreds column = <strong>700</strong></li>
        <li><strong>4</strong> is in the Tens column = <strong>40</strong></li>
        <li><strong>8</strong> is in the Units column = <strong>8</strong></li>
      </ul>
      Partitioned: <code>700 + 40 + 8 = 748</code>. In words: <em>Seven hundred and forty-eight</em>.
    </div>

    {tutor_vignette("👩‍🔧", "Maya", "Business Trainee", "Don't ignore the zero! In 305, the 0 holds the tens column. Writing 35 means thirty-five, which is a massive error on an invoice!")}

    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Workplace Delivery Count</span>
      <p>A logistics depot logs an intake of <strong>409</strong> parcels. Write 409 in words and state the value of each digit.</p>
      <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:4px 8px; font-size:7.5pt; margin-top:3px;">
        1. <strong>4</strong> = 4 Hundreds (400).<br>
        2. <strong>0</strong> = 0 Tens (0).<br>
        3. <strong>9</strong> = 9 Units (9).<br>
        <strong>In words:</strong> Four hundred and nine.
      </div>
    </div>

    <div class="box-trap">
      <span class="tag-label tag-red">Common Exam Trap</span>
      Never hyphenate the hundreds! Write <em>five hundred and twenty-three</em>, NOT <em>five-hundred</em>. Only hyphenate tens and units (e.g. <em>twenty-three</em>, <em>forty-eight</em>).
    </div>
    """
    pages.append(wrap_page(p3, 3, "Strand 1: Number & Number Systems", "Standards: E3.1, E3.2", "Maths Entry Level 3 Core Guide"))

    p4_scaffold = """
    <div class="step-row"><span>Step 1: Draw Place Value Table</span><span>Hundreds (H) | Tens (T) | Units (U)</span></div>
    <div class="step-row"><span>Step 2: Place digits in columns for 682</span><span>H: 6 (600) &bull; T: 8 (80) &bull; U: 2 (2)</span></div>
    <div class="step-row"><span>Step 3: Combine in words</span><span>Six hundred and eighty-two</span></div>
    """
    p4 = practice_page(
        "Place Value to 1,000", "Standards E3.1, E3.2", 4, p4_scaffold,
        "Write the number <strong>682</strong> in words and partitioned into Hundreds, Tens, and Units.",
        "What is the exact value of the digit <strong>7</strong> in each number: a) 714 &emsp; b) 378 &emsp; c) 907?",
        "A stock room counts three boxes containing 500, 40, and 6 components. Write the combined total in digits and in words."
    )
    pages.append(p4)

    # TOPIC 2: PAGE 5 (Theory) & PAGE 6 (Practice)
    p5 = f"""
    <h2>Unit 2: Comparing, Ordering &amp; Number Lines</h2>
    <p>Comparing 3-digit values using mathematical symbols and positioning numbers accurately along a number line.</p>

    <div class="box-concept">
      <span class="tag-label tag-blue">Key Principle</span> <strong>Comparison Symbols:</strong>
      <ul style="margin:3px 0 0 16px; padding:0; font-size:7.7pt;">
        <li><strong>&gt;</strong> means <em>greater than</em> (e.g. <code>520 &gt; 410</code>)</li>
        <li><strong>&lt;</strong> means <em>less than</em> (e.g. <code>185 &lt; 290</code>)</li>
        <li><strong>=</strong> means <em>equal to</em> (e.g. <code>300 = 300</code>)</li>
      </ul>
      <strong>The Ordering Rule:</strong> Compare the <strong>Hundreds</strong> digit first. If identical, compare the <strong>Tens</strong>. If still identical, compare the <strong>Units</strong>.
    </div>

    {tutor_vignette("👷‍♂️", "Dave", "Site Electrician", "Think of the symbol as an arrow or crocodile mouth that always opens towards the larger number! 640 > 620.")}

    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Ordering Van Mileages</span>
      <p>Put these four van mileages in order from <strong>smallest to largest</strong>: 482 miles, 419 miles, 503 miles, 475 miles.</p>
      <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:4px 8px; font-size:7.5pt; margin-top:3px;">
        1. Compare hundreds: 419, 475, 482 all start with 4. 503 starts with 5 (largest).<br>
        2. Compare tens of the 400s: 1 ten (419) &lt; 7 tens (475) &lt; 8 tens (482).<br>
        <strong>Correct ascending order:</strong> 419 miles, 475 miles, 482 miles, 503 miles.
      </div>
    </div>

    <div class="box-trap">
      <span class="tag-label tag-red">Exam Watchout</span>
      Always read the question prompt carefully: does it ask for <em>smallest to largest</em> (ascending) or <em>largest to smallest</em> (descending)?
    </div>
    """
    pages.append(wrap_page(p5, 5, "Strand 1: Number & Number Systems", "Standard: E3.1", "Maths Entry Level 3 Core Guide"))

    p6_scaffold = """
    <div class="step-row"><span>Step 1: Check Hundreds column</span><span>Compare first digits of all values</span></div>
    <div class="step-row"><span>Step 2: Check Tens column if tied</span><span>Smaller tens digit comes first</span></div>
    <div class="step-row"><span>Step 3: Cross off each number as written</span><span>Ensures no numbers are missed</span></div>
    """
    p6 = practice_page(
        "Comparing & Ordering Numbers", "Standard E3.1", 6, p6_scaffold,
        "Insert the correct symbol (<strong>&gt;</strong>, <strong>&lt;</strong>, or <strong>=</strong>) between each pair: a) 429 ___ 492 &emsp; b) 801 ___ 799 &emsp; c) 650 ___ 650.",
        "Arrange these prices from cheapest to most expensive: &pound;345, &pound;299, &pound;380, &pound;289, &pound;305.",
        "A depot receives four pallet weights: 720 kg, 702 kg, 725 kg, 698 kg. Which pallet is the heaviest, and which is the lightest?"
    )
    pages.append(p6)

    # TOPIC 3: PAGE 7 (Theory) & PAGE 8 (Practice)
    p7 = f"""
    <h2>Unit 3: Rounding to Nearest 10 and 100</h2>
    <p>Approximating whole numbers to estimate practical costs, materials, and quantities quickly without a calculator.</p>

    <div class="box-concept">
      <span class="tag-label tag-blue">The Golden Rounding Rule</span>
      <ul style="margin:3px 0 0 16px; padding:0; font-size:7.7pt;">
        <li>Look at the digit immediately to the <strong>right</strong> of the target place value.</li>
        <li>If that digit is <strong>0, 1, 2, 3, or 4</strong> &rarr; <strong>Round DOWN</strong> (target digit stays the same).</li>
        <li>If that digit is <strong>5, 6, 7, 8, or 9</strong> &rarr; <strong>Round UP</strong> (add 1 to the target digit).</li>
        <li>Change all digits to the right into zeros!</li>
      </ul>
    </div>

    {tutor_vignette("👨‍🏫", "Tutor Marcus", "Senior Maths Specialist", "When rounding 247 to the nearest 100, look at the Tens digit (4), NOT the Units digit (7)! 4 means round down to 200.")}

    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Bus Journey Passengers</span>
      <p>A coach company carries <strong>247</strong> passengers. Round 247 to:<br>
      a) The nearest 10 &emsp; b) The nearest 100.</p>
      <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:4px 8px; font-size:7.5pt; margin-top:3px;">
        a) Nearest 10: Target digit is 4 (tens). Right digit is 7 (5 or more). Round up &rarr; <strong>250</strong>.<br>
        b) Nearest 100: Target digit is 2 (hundreds). Right digit is 4 (4 or less). Round down &rarr; <strong>200</strong>.
      </div>
    </div>

    <div class="box-trap">
      <span class="tag-label tag-red">Common Pitfall</span>
      Halfway numbers like 250 rounded to the nearest 100 always round <strong>UP</strong> to 300 because the tens digit is 5.
    </div>
    """
    pages.append(wrap_page(p7, 7, "Strand 1: Number & Number Systems", "Standard: E3.3", "Maths Entry Level 3 Core Guide"))

    p8_scaffold = """
    <div class="step-row"><span>Step 1: Identify target place value</span><span>Underline Tens digit or Hundreds digit</span></div>
    <div class="step-row"><span>Step 2: Inspect decider digit to right</span><span>0-4 = stay same; 5-9 = add 1</span></div>
    <div class="step-row"><span>Step 3: Fill right places with zeros</span><span>e.g. 384 to nearest 100 = 400</span></div>
    """
    p8 = practice_page(
        "Rounding to Nearest 10 & 100", "Standard E3.3", 8, p8_scaffold,
        "Round each number to the nearest 10: a) 58 &emsp; b) 143 &emsp; c) 875.",
        "Round each number to the nearest 100: a) 380 &emsp; b) 724 &emsp; c) 650.",
        "A warehouse orders 486 packing crates at &pound;8.80 each. Estimate the total number of crates to the nearest 100."
    )
    pages.append(p8)

    # TOPIC 4: PAGE 9 (Theory) & PAGE 10 (Practice)
    p9 = f"""
    <h2>Unit 4: Number Patterns, Sequences &amp; Odd/Even</h2>
    <p>Identifying number step rules, continuing patterns, and classifying integers as odd or even.</p>

    <div class="box-concept">
      <span class="tag-label tag-blue">Key Principle</span> <strong>Odd &amp; Even Properties:</strong>
      <ul style="margin:3px 0 0 16px; padding:0; font-size:7.7pt;">
        <li><strong>Even Numbers:</strong> End in <strong>0, 2, 4, 6, or 8</strong>. They can be divided exactly by 2 with no remainder.</li>
        <li><strong>Odd Numbers:</strong> End in <strong>1, 3, 5, 7, or 9</strong>. They leave a remainder of 1 when divided by 2.</li>
      </ul>
      <strong>Sequence Rule:</strong> Find the constant difference between terms by subtracting: <code>Term 2 &minus; Term 1</code>.
    </div>

    {tutor_vignette("👩‍⚕️", "Chloe", "Care Home Trainee", "Look only at the very last digit (units) to decide if a number is odd or even. 7,492 is even because it ends in 2!")}

    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Pallet Count Sequence</span>
      <p>Find the next two numbers in this sequence: <strong>150, 200, 250, 300, ___ , ___</strong>.</p>
      <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:4px 8px; font-size:7.5pt; margin-top:3px;">
        1. Find the step rule: 200 &minus; 150 = +50.<br>
        2. Add 50 to 300 &rarr; 350.<br>
        3. Add 50 to 350 &rarr; 400.<br>
        <strong>Next two numbers:</strong> 350 and 400.
      </div>
    </div>

    <div class="box-trap">
      <span class="tag-label tag-red">Exam Trap</span>
      Check if sequences are decreasing! In 90, 80, 70, the rule is &minus;10, so the next term is 60, not 80.
    </div>
    """
    pages.append(wrap_page(p9, 9, "Strand 1: Number & Number Systems", "Standard: E3.4", "Maths Entry Level 3 Core Guide"))

    p10_scaffold = """
    <div class="step-row"><span>Step 1: Check last digit (Units)</span><span>0, 2, 4, 6, 8 = Even &bull; 1, 3, 5, 7, 9 = Odd</span></div>
    <div class="step-row"><span>Step 2: Find step difference</span><span>Term 2 &minus; Term 1 (e.g. 28 &minus; 24 = +4)</span></div>
    <div class="step-row"><span>Step 3: Apply rule to missing positions</span><span>Keep the interval constant</span></div>
    """
    p10 = practice_page(
        "Sequences & Odd/Even Numbers", "Standard E3.4", 10, p10_scaffold,
        "Identify whether each number is Odd or Even: a) 234 &emsp; b) 781 &emsp; c) 950 &emsp; d) 417.",
        "Find the missing numbers in each sequence: a) 24, 28, 32, ___, 40 &emsp; b) 120, 110, 100, ___, 80.",
        "A machine packs items in batches of 25: 125, 150, 175, ___, ___. Write the next two terms and state if they are odd or even."
    )
    pages.append(p10)

    # TOPIC 5: PAGE 11 (Theory) & PAGE 12 (Practice)
    p11 = f"""
    <h2>Unit 5: Column Addition up to 3 Digits</h2>
    <p>Mastering formal written column addition with carrying (regrouping) from units to tens and tens to hundreds.</p>

    <div class="box-concept">
      <span class="tag-label tag-blue">The Column Alignment Rule</span>
      Always write numbers strictly aligned in columns: <strong>Hundreds (H) | Tens (T) | Units (U)</strong>.<br>
      Add from <strong>right to left</strong>: start with the Units column, then Tens, then Hundreds. If any column adds to 10 or more, carry the 1 into the next column on the left.
    </div>

    {tutor_vignette("👩‍🔧", "Maya", "Business Trainee", "Always write the carried digit clearly beneath the next column so you don't forget to add it in!")}

    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Equipment Invoices</span>
      <p>Calculate: <strong>&pound;368 + &pound;475</strong>.</p>
      <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:4px 8px; font-size:7.5pt; margin-top:3px;">
        <pre style="margin:0; font-family:monospace; font-size:8pt;">
    H  T  U
    3  6  8
  + 4  7  5
  ---------
  Units:     8 + 5 = 13  (write 3, carry 1 ten)
  Tens:      6 + 7 + 1 = 14 (write 4, carry 1 hundred)
  Hundreds:  3 + 4 + 1 = 8
  ---------
  Total:     8  4  3  (&pound;843)
        </pre>
      </div>
    </div>

    <div class="box-trap">
      <span class="tag-label tag-red">Common Pitfall</span>
      Misaligning single or two-digit numbers (e.g. lining up 45 under the hundreds column instead of tens and units) destroys the whole calculation.
    </div>
    """
    pages.append(wrap_page(p11, 11, "Strand 1: Number & Number Systems", "Standard: E3.5", "Maths Entry Level 3 Core Guide"))

    p12_scaffold = """
    <div class="step-row"><span>Step 1: Units column</span><span>8 + 5 = 13 &rarr; write 3, carry 1</span></div>
    <div class="step-row"><span>Step 2: Tens column</span><span>6 + 7 + 1 = 14 &rarr; write 4, carry 1</span></div>
    <div class="step-row"><span>Step 3: Hundreds column</span><span>3 + 4 + 1 = 8 &rarr; Result = 843</span></div>
    """
    p12 = practice_page(
        "Column Addition (3 Digits)", "Standard E3.5", 12, p12_scaffold,
        "Calculate using column addition: a) 243 + 155 &emsp; b) 487 + 236 &emsp; c) 609 + 294.",
        "A delivery driver covers 142 miles on Monday, 89 miles on Tuesday, and 215 miles on Wednesday. What is his total 3-day mileage?",
        "A workplace orders safety boots for &pound;175 and high-visibility coats for &pound;288. How much is spent altogether?"
    )
    pages.append(p12)

    # TOPIC 6: PAGE 13 (Theory) & PAGE 14 (Practice)
    p13 = f"""
    <h2>Unit 6: Column Subtraction with Exchanging</h2>
    <p>Finding the difference and taking amounts away using formal column subtraction with exchanging (borrowing).</p>

    <div class="box-concept">
      <span class="tag-label tag-blue">The Exchanging Rule</span>
      If the top digit is smaller than the bottom digit in any column, you <strong>cannot</strong> just reverse them! You must exchange 1 from the column to the left:
      <ul style="margin:3px 0 0 16px; padding:0; font-size:7.7pt;">
        <li>1 Ten exchanges for 10 Units.</li>
        <li>1 Hundred exchanges for 10 Tens.</li>
      </ul>
    </div>

    {tutor_vignette("👷‍♂️", "Dave", "Site Electrician", "If you have 2 &minus; 8, the answer is NOT 6! You must cross out the top tens digit, reduce it by 1, and make your 2 into 12. 12 &minus; 8 = 4.")}

    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Warehouse Stock Count</span>
      <p>A depot has <strong>632</strong> cartons. <strong>278</strong> are dispatched. How many remain?</p>
      <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:4px 8px; font-size:7.5pt; margin-top:3px;">
        <pre style="margin:0; font-family:monospace; font-size:8pt;">
    H  T  U
    5 12 12
    6  3  2
  - 2  7  8
  ---------
  Units:     12 &minus; 8 = 4 (borrowed from 3 tens &rarr; 2 left)
  Tens:      12 &minus; 7 = 5 (borrowed from 6 hundreds &rarr; 5 left)
  Hundreds:  5 &minus; 2 = 3
  ---------
  Remaining: 3  5  4 cartons
        </pre>
      </div>
    </div>

    <div class="box-trap">
      <span class="tag-label tag-red">Check With Addition</span>
      Always check your subtraction answer: <code>354 + 278 = 632</code>. If it equals the starting number, your answer is 100% correct!
    </div>
    """
    pages.append(wrap_page(p13, 13, "Strand 1: Number & Number Systems", "Standard: E3.6", "Maths Entry Level 3 Core Guide"))

    p14_scaffold = """
    <div class="step-row"><span>Step 1: Check units 2 &minus; 8</span><span>Cannot do &rarr; exchange 1 ten: 12 &minus; 8 = 4</span></div>
    <div class="step-row"><span>Step 2: Check tens 2 &minus; 7</span><span>Cannot do &rarr; exchange 1 hundred: 12 &minus; 7 = 5</span></div>
    <div class="step-row"><span>Step 3: Hundreds 5 &minus; 2</span><span>5 &minus; 2 = 3 &rarr; Answer = 354</span></div>
    """
    p14 = practice_page(
        "Column Subtraction (Exchanging)", "Standard E3.6", 14, p14_scaffold,
        "Calculate using column subtraction: a) 584 &minus; 231 &emsp; b) 742 &minus; 385 &emsp; c) 800 &minus; 347.",
        "A business bank account holds &pound;620. After paying an energy bill, the balance is &pound;455. How much was the bill?",
        "A manufacturing run requires 500 components. By midday, workers have assembled 318 components. How many more are needed?"
    )
    pages.append(p14)

    # TOPIC 7: PAGE 15 (Theory) & PAGE 16 (Practice)
    p15 = f"""
    <h2>Unit 7: Multiplication Facts &amp; Grid Method</h2>
    <p>Recall and apply times tables (2, 3, 4, 5, 8, 10) and multiply two-digit numbers by a single-digit integer.</p>

    <div class="box-concept">
      <span class="tag-label tag-blue">Times Table Mastery</span>
      Entry 3 requires rapid recall of the <strong>2, 3, 4, 5, 8, and 10</strong> times tables. Multiplication is repeated addition.<br>
      <strong>Grid Method for 2 Digits &times; 1 Digit:</strong> Partition the 2-digit number into Tens and Units before multiplying.
    </div>

    {tutor_vignette("👨‍🏫", "Tutor Marcus", "Senior Maths Specialist", "To multiply by 8, you can double, double, and double again! 8 &times; 15 = double 15 (30), double 30 (60), double 60 (120).")}

    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Soft Drink Orders</span>
      <p>A café orders <strong>8</strong> crates of drinks. Each crate holds <strong>24</strong> cans. How many cans altogether?</p>
      <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:4px 8px; font-size:7.5pt; margin-top:3px;">
        1. Partition 24 into 20 and 4.<br>
        2. Multiply Tens: <code>8 &times; 20 = 160</code>.<br>
        3. Multiply Units: <code>8 &times; 4 = 32</code>.<br>
        4. Add partial products: <code>160 + 32 = 192</code> cans.
      </div>
    </div>

    <div class="box-trap">
      <span class="tag-label tag-red">Place Value Reminder</span>
      When calculating <code>8 &times; 20</code>, think <code>8 &times; 2 = 16</code>, then multiply by 10 to get <code>160</code>.
    </div>
    """
    pages.append(wrap_page(p15, 15, "Strand 1: Number & Number Systems", "Standards: E3.7, E3.8", "Maths Entry Level 3 Core Guide"))

    p16_scaffold = """
    <div class="step-row"><span>Step 1: Partition 2-digit number</span><span>24 = 20 + 4</span></div>
    <div class="step-row"><span>Step 2: Multiply each part by 8</span><span>8 &times; 20 = 160 &bull; 8 &times; 4 = 32</span></div>
    <div class="step-row"><span>Step 3: Add together</span><span>160 + 32 = 192 cans</span></div>
    """
    p16 = practice_page(
        "Multiplication & Grid Method", "Standards E3.7, E3.8", 16, p16_scaffold,
        "Calculate these mental multiplication facts: a) 7 &times; 4 &emsp; b) 8 &times; 6 &emsp; c) 9 &times; 3 &emsp; d) 8 &times; 8.",
        "Use the grid or column method to calculate: a) 35 &times; 4 &emsp; b) 52 &times; 6.",
        "A garage fits 4 new tyres on each of 18 fleet cars. How many tyres are fitted in total?"
    )
    pages.append(p16)

    # TOPIC 8: PAGE 17 (Theory) & PAGE 18 (Practice)
    p17 = f"""
    <h2>Unit 8: Division &amp; Division with Remainders</h2>
    <p>Sharing amounts equally, grouping items into equal batches, and interpreting remainders in real-world problems.</p>

    <div class="box-concept">
      <span class="tag-label tag-blue">Short Division (Bus Stop Method)</span>
      To divide a 2-digit number by a single digit (e.g. <code>98 &divide; 4</code>):
      <ol style="margin:3px 0 0 16px; padding:0; font-size:7.7pt;">
        <li>How many 4s in 9? 2 with remainder 1. Write 2 above the line, carry 1 to make 18.</li>
        <li>How many 4s in 18? 4 with remainder 2 (since <code>4 &times; 4 = 16</code>).</li>
        <li>Result: <strong>24 remainder 2</strong>.</li>
      </ol>
    </div>

    {tutor_vignette("👩‍⚕️", "Chloe", "Care Home Trainee", "In real-world questions, think about what the remainder means! If 50 passengers need 8-seater vans, 6 vans leave 2 people behind &rarr; you must hire 7 vans!")}

    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Bakery Gift Boxes</span>
      <p>A bakery bakes <strong>75</strong> muffins. Each box holds <strong>6</strong> muffins.<br>
      a) How many full boxes can be packed? &emsp; b) How many muffins are leftover?</p>
      <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:4px 8px; font-size:7.5pt; margin-top:3px;">
        1. Divide 75 by 6: 6 goes into 7 once with remainder 1.<br>
        2. 6 goes into 15 twice (<code>2 &times; 6 = 12</code>) with remainder 3.<br>
        <strong>a) Full boxes:</strong> 12 boxes. &emsp; <strong>b) Leftover:</strong> 3 muffins.
      </div>
    </div>

    <div class="box-trap">
      <span class="tag-label tag-red">Division Verification</span>
      Check your answer: <code>(Quotient &times; Divisor) + Remainder = Original Number</code>. (12 &times; 6) + 3 = 72 + 3 = 75.
    </div>
    """
    pages.append(wrap_page(p17, 17, "Strand 1: Number & Number Systems", "Standard: E3.9", "Maths Entry Level 3 Core Guide"))

    p18_scaffold = """
    <div class="step-row"><span>Step 1: Divide tens digit</span><span>7 &divide; 6 = 1 remainder 1 (carry 1)</span></div>
    <div class="step-row"><span>Step 2: Divide units with carry</span><span>15 &divide; 6 = 2 remainder 3</span></div>
    <div class="step-row"><span>Step 3: State whole quotient &amp; remainder</span><span>12 full boxes with 3 leftover</span></div>
    """
    p18 = practice_page(
        "Division & Remainders", "Standard E3.9", 18, p18_scaffold,
        "Calculate without remainders: a) 84 &divide; 4 &emsp; b) 96 &divide; 3 &emsp; c) 70 &divide; 5.",
        "Calculate with remainders: a) 47 &divide; 5 &emsp; b) 85 &divide; 8.",
        "A courier has 58 parcels. His van can carry 8 parcels per trip. How many full trips does he make, and how many trips in total to deliver all parcels?"
    )
    pages.append(p18)

    # TOPIC 9: PAGE 19 (Theory) & PAGE 20 (Practice)
    p19 = f"""
    <h2>Unit 9: Inverse Operations &amp; Estimating Checks</h2>
    <p>Using opposite operations and rounded estimations to verify calculations and secure statutory exam check marks.</p>

    <div class="box-concept">
      <span class="tag-label tag-blue">Inverse Pairs &amp; Checking Marks</span>
      An inverse operation undoes a calculation. In Functional Skills exams, you are awarded marks specifically for showing a formal check:
      <ul style="margin:3px 0 0 16px; padding:0; font-size:7.7pt;">
        <li><strong>Addition &harr; Subtraction:</strong> Check <code>240 + 150 = 390</code> with <code>390 &minus; 150 = 240</code>.</li>
        <li><strong>Multiplication &harr; Division:</strong> Check <code>18 &times; 4 = 72</code> with <code>72 &divide; 4 = 18</code>.</li>
      </ul>
    </div>

    {tutor_vignette("👨‍🏫", "Tutor Marcus", "Senior Maths Specialist", "On your exam paper, when it says 'Show a check of your answer', never just repeat the exact same calculation! Always use the inverse or round to estimate.")}

    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Estimating Stock Value</span>
      <p>A store sells <strong>29</strong> jackets at <strong>&pound;48</strong> each. Estimate the total cost using rounded numbers, then show an inverse check.</p>
      <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:4px 8px; font-size:7.5pt; margin-top:3px;">
        1. Round to nearest 10: 29 &rarr; 30 jackets; &pound;48 &rarr; &pound;50.<br>
        2. Estimate: <code>30 &times; &pound;50 = &pound;1,500</code>.<br>
        3. Inverse check: <code>&pound;1,500 &divide; 30 = &pound;50</code>.
      </div>
    </div>

    <div class="box-trap">
      <span class="tag-label tag-red">Exam Warning</span>
      Writing 'I checked on my calculator' gets 0 marks! You must write down the numbers and operation.
    </div>
    """
    pages.append(wrap_page(p19, 19, "Strand 1: Number & Number Systems", "Standard: E3.10", "Maths Entry Level 3 Core Guide"))

    p20_scaffold = """
    <div class="step-row"><span>Step 1: Identify original calculation</span><span>e.g. 350 + 240 = 590</span></div>
    <div class="step-row"><span>Step 2: Choose inverse operation</span><span>Subtraction undoes addition: 590 &minus; 240</span></div>
    <div class="step-row"><span>Step 3: Confirm match with starting term</span><span>590 &minus; 240 = 350 (Verified)</span></div>
    """
    p20 = practice_page(
        "Inverse Operations & Checking", "Standard E3.10", 20, p20_scaffold,
        "Show how to check each calculation using the inverse operation: a) 420 + 170 = 590 &emsp; b) 18 &times; 5 = 90.",
        "A clerk calculates that 800 &minus; 265 = 535. Use addition to verify whether this answer is correct.",
        "An office manager buys 39 printer cartridges at &pound;19 each. Estimate the total cost by rounding both numbers to the nearest 10."
    )
    pages.append(p20)

    # TOPIC 10: PAGE 21 (Theory) & PAGE 22 (Practice)
    p21 = f"""
    <h2>Unit 10: Fractions: Unit, Non-Unit &amp; Amounts</h2>
    <p>Understanding fractions as equal parts of a whole, comparing unit fractions, and finding fractions of quantities.</p>

    <div class="box-concept">
      <span class="tag-label tag-blue">Fraction Foundations</span>
      A fraction has a <strong>Numerator</strong> (top number = parts taken) and a <strong>Denominator</strong> (bottom number = total equal parts).
      <ul style="margin:3px 0 0 16px; padding:0; font-size:7.7pt;">
        <li><strong>Unit Fractions:</strong> Numerator is 1 (e.g. &frac12;, &frac13;, &frac14;, &frac15;, 1/10).</li>
        <li><strong>Non-Unit Fractions:</strong> Numerator &gt; 1 (e.g. &frac23;, &frac34;).</li>
        <li><strong>Comparing:</strong> When numerators are 1, a <strong>larger denominator means a smaller piece</strong>! &frac14; is smaller than &frac12;.</li>
      </ul>
    </div>

    {tutor_vignette("👩‍🔧", "Maya", "Business Trainee", "To find &frac34; of an amount: first divide by the bottom number (4) to find one quarter, then multiply by the top number (3)!")}

    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Finding Fractions of Amounts</span>
      <p>A company employs <strong>48</strong> staff. <strong>&frac34;</strong> of the staff work full-time. How many staff work full-time?</p>
      <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:4px 8px; font-size:7.5pt; margin-top:3px;">
        1. Find &frac14; (divide by denominator 4): <code>48 &divide; 4 = 12</code>.<br>
        2. Find &frac34; (multiply by numerator 3): <code>12 &times; 3 = 36</code>.<br>
        <strong>Answer:</strong> 36 staff work full-time.
      </div>
    </div>

    <div class="box-trap">
      <span class="tag-label tag-red">Exam Trap</span>
      Never divide by the top number! The denominator (bottom) tells you how many equal shares to make.
    </div>
    """
    pages.append(wrap_page(p21, 21, "Strand 1: Number & Number Systems", "Standards: E3.11, E3.12", "Maths Entry Level 3 Core Guide"))

    p22_scaffold = """
    <div class="step-row"><span>Step 1: Divide by Denominator</span><span>48 &divide; 4 = 12 (one quarter)</span></div>
    <div class="step-row"><span>Step 2: Multiply by Numerator</span><span>12 &times; 3 = 36 (three quarters)</span></div>
    <div class="step-row"><span>Step 3: State final value with units</span><span>36 staff</span></div>
    """
    p22 = practice_page(
        "Fractions of Quantities", "Standards E3.11, E3.12", 22, p22_scaffold,
        "Calculate unit fractions of amounts: a) &frac12; of &pound;60 &emsp; b) &frac14; of 32 kg &emsp; c) &frac13; of 27 litres.",
        "Calculate non-unit fractions: a) &frac23; of 30 metres &emsp; b) &frac34; of &pound;40.",
        "A warehouse holds 120 boxes. &frac15; are damaged. How many boxes are damaged, and how many are undamaged?"
    )
    pages.append(p22)

    # -------------------------------------------------------------
    # STRAND 1 CHECKPOINT (PAGES 23, 24, 25, 26) - Total 30 Marks
    # -------------------------------------------------------------
    chk1_p1 = [
        ("1", 2, "Write the number <strong>749</strong> in words, and state the value of the digit 4.", 50),
        ("2", 2, "Put these numbers in order starting with the <strong>smallest</strong>: 604, 460, 640, 406.", 50),
        ("3", 2, "Round <strong>368</strong> to: a) the nearest 10 &emsp; b) the nearest 100.", 50)
    ]
    pages.append(checkpoint_page("Strand 1: Number &amp; Number Systems", "Part 1 &bull; Non-Calculator (Q1-Q3)", 23, "6 Marks", chk1_p1))

    chk1_p2 = [
        ("4", 2, "Calculate: <strong>385 + 247</strong> using formal column addition.", 52),
        ("5", 2, "Calculate: <strong>624 &minus; 278</strong> using formal column subtraction.", 52),
        ("6", 2, "Calculate: <strong>72 &divide; 4</strong> and show an inverse multiplication check.", 52)
    ]
    pages.append(checkpoint_page("Strand 1: Number &amp; Number Systems", "Part 1 &bull; Non-Calculator (Q4-Q6)", 24, "6 Marks", chk1_p2))

    chk1_p3 = [
        ("7", 2, "A supplier packs 8 boxes with 26 lightbulbs in each box. How many lightbulbs are packed in total?", 52),
        ("8", 3, "A catering kitchen bakes 94 rolls. Each bread basket holds 8 rolls. How many full baskets can be served, and how many rolls are left over?", 60),
        ("9", 3, "A delivery company has 80 parcels. <strong>&frac34;</strong> of the parcels are delivered in the morning. How many parcels are delivered in the morning?", 60)
    ]
    pages.append(checkpoint_page("Strand 1: Number &amp; Number Systems", "Part 2 &bull; Calculator Allowed (Q7-Q9)", 25, "8 Marks", chk1_p3))

    chk1_p4 = [
        ("10", 3, "A builder estimates that a project needs 485 concrete blocks. Blocks are sold in packs of 50. How many packs must the builder purchase so he does not run out?", 60),
        ("11", 3, "A retailer has an opening bank balance of &pound;750. They pay &pound;185 for stock and &pound;95 for electricity. What is the remaining bank balance?", 60),
        ("12", 4, "A training room has 60 trainee places. &frac23; are booked by healthcare staff and &frac15; are booked by retail staff. How many places are booked altogether?", 70)
    ]
    pages.append(checkpoint_page("Strand 1: Number &amp; Number Systems", "Part 2 &bull; Calculator Allowed (Q10-Q12)", 26, "10 Marks", chk1_p4))

    # =========================================================================
    # STRAND 2: MEASURES, SHAPE & SPACE (Units 11 to 20 & Checkpoint)
    # =========================================================================

    # TOPIC 11: PAGE 27 (Theory) & PAGE 28 (Practice)
    p27 = f"""
    <h2>Unit 11: Decimal Money: Calculating with &pound; &amp; p</h2>
    <p>Using decimal notation for money, converting pence to pounds, and formal column addition and subtraction of prices.</p>

    <div class="box-concept">
      <span class="tag-label tag-blue">Key Principle</span> <strong>The Decimal Point in Money:</strong>
      There are <strong>100 pence in 1 pound</strong> (<code>&pound;1 = 100p</code>).
      <ul style="margin:3px 0 0 16px; padding:0; font-size:7.7pt;">
        <li>Pence always occupies exactly <strong>two decimal places</strong>: 5p is written as <code>&pound;0.05</code> (NOT &pound;0.5, which is 50p!).</li>
        <li>Never write &pound; and p together (e.g. write <code>&pound;4.50</code> or <code>450p</code>, NEVER &pound;4.50p).</li>
        <li>When adding money, always <strong>line up the decimal points</strong> vertically.</li>
      </ul>
    </div>

    {tutor_vignette("👩‍🔧", "Maya", "Business Trainee", "Always append a trailing zero for whole ten pence! Write £3.40, never £3.4. Money must always show two decimal places!")}

    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Workshop Hardware Bill</span>
      <p>A customer buys a tin of paint for <strong>&pound;14.75</strong> and a paintbrush for <strong>&pound;3.50</strong>. Calculate the total cost.</p>
      <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:4px 8px; font-size:7.5pt; margin-top:3px;">
        <pre style="margin:0; font-family:monospace; font-size:8pt;">
    &pound; 1 4 . 7 5
  + &pound;   3 . 5 0
  -------------
  Pence:     5 + 0 = 5 &bull; 7 + 5 = 12 (write 2, carry 1)
  Pounds:    4 + 3 + 1 = 8 &bull; 1 + 0 = 1
  -------------
  Total:     &pound; 1 8 . 2 5
        </pre>
      </div>
    </div>

    <div class="box-trap">
      <span class="tag-label tag-red">Exam Trap</span>
      Never confuse <code>&pound;0.08</code> (8 pence) with <code>&pound;0.80</code> (80 pence).
    </div>
    """
    pages.append(wrap_page(p27, 27, "Strand 2: Measures, Shape & Space", "Standards: E3.13, E3.14", "Maths Entry Level 3 Core Guide"))

    p28_scaffold = """
    <div class="step-row"><span>Step 1: Line up decimal points</span><span>Keep pounds on left, pence on right</span></div>
    <div class="step-row"><span>Step 2: Add pence first</span><span>Carry across the decimal point if &ge; 100p</span></div>
    <div class="step-row"><span>Step 3: Include &pound; sign in answer</span><span>Always two decimal places (e.g. &pound;18.25)</span></div>
    """
    p28 = practice_page(
        "Calculating with Decimal Money", "Standards E3.13, E3.14", 28, p28_scaffold,
        "Convert each amount: a) 450p to &pound; &emsp; b) 85p to &pound; &emsp; c) &pound;6.05 to pence.",
        "Calculate the total: a) &pound;12.45 + &pound;6.30 &emsp; b) &pound;25.80 + &pound;14.95.",
        "A trainee buys lunch: a sandwich for &pound;3.75, an apple for &pound;0.65, and a bottle of juice for &pound;1.80. What is the total cost?"
    )
    pages.append(p28)

    # TOPIC 12: PAGE 29 (Theory) & PAGE 30 (Practice)
    p29 = f"""
    <h2>Unit 12: Everyday Money, Deals &amp; Giving Change</h2>
    <p>Calculating change from banknotes (&pound;5, &pound;10, &pound;20), comparing workplace special offers, and checking receipts.</p>

    <div class="box-concept">
      <span class="tag-label tag-blue">Key Principle</span> <strong>Calculating Change:</strong>
      To calculate change: <code>Change = Money Paid &minus; Cost of Items</code>.<br>
      You can subtract in columns using decimals (e.g. <code>&pound;20.00 &minus; &pound;14.35</code>) or count up from the cost to the note given.
    </div>

    {tutor_vignette("👷‍♂️", "Dave", "Site Electrician", "When subtracting from £10.00 or £20.00, write .00 and exchange across the zeros carefully, or count up: £14.35 + 65p = £15.00, + £5 = £20.00 &rarr; £5.65 change!")}

    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Paying with a &pound;20 Note</span>
      <p>A customer buys groceries costing <strong>&pound;13.65</strong> and pays with a <strong>&pound;20 note</strong>. How much change do they receive?</p>
      <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:4px 8px; font-size:7.5pt; margin-top:3px;">
        1. Write: <code>&pound;20.00 &minus; &pound;13.65</code>.<br>
        2. Count up method: 13.65 + 0.35 = &pound;14.00.<br>
        3. &pound;14.00 + &pound;6.00 = &pound;20.00.<br>
        4. Combine: <code>&pound;6.00 + &pound;0.35 = &pound;6.35</code> change.
      </div>
    </div>

    <div class="box-trap">
      <span class="tag-label tag-red">Exam Watchout</span>
      Always check the question: does it ask for the <em>total cost</em> or the <em>change received</em>?
    </div>
    """
    pages.append(wrap_page(p29, 29, "Strand 2: Measures, Shape & Space", "Standard: E3.14", "Maths Entry Level 3 Core Guide"))

    p30_scaffold = """
    <div class="step-row"><span>Step 1: Find total cost of purchase</span><span>Add all individual items together</span></div>
    <div class="step-row"><span>Step 2: Note the banknote tendered</span><span>e.g. &pound;10.00 or &pound;20.00</span></div>
    <div class="step-row"><span>Step 3: Subtract or count up to find change</span><span>&pound;20.00 &minus; &pound;13.65 = &pound;6.35</span></div>
    """
    p30 = practice_page(
        "Everyday Money & Giving Change", "Standard E3.14", 30, p30_scaffold,
        "Calculate the change from a &pound;10 note for a purchase of &pound;6.45.",
        "A customer buys two coffees at &pound;2.80 each and a cake for &pound;3.15. How much change do they receive from a &pound;20 note?",
        "Store A sells 3 packs of pens for &pound;6.00. Store B sells individual packs for &pound;2.25 each. Which store is cheaper for 3 packs, and by how much?"
    )
    pages.append(p30)

    # TOPIC 13: PAGE 31 (Theory) & PAGE 32 (Practice)
    p31 = f"""
    <h2>Unit 13: Time: 12-Hour Analogue &amp; Digital Clocks</h2>
    <p>Reading analogue clock faces to the nearest 5 minutes, understanding am and pm, and matching to 12-hour digital displays.</p>

    <div class="box-concept">
      <span class="tag-label tag-blue">Key Principle</span> <strong>Analogue Hands &amp; Divisions:</strong>
      <ul style="margin:3px 0 0 16px; padding:0; font-size:7.7pt;">
        <li><strong>Short Hand:</strong> Indicates the <strong>Hours</strong>.</li>
        <li><strong>Long Hand:</strong> Indicates the <strong>Minutes</strong> (each numbered number on the dial = 5 minutes).</li>
        <li>Past &amp; To: From 12 to 6 is <em>past the hour</em> (e.g. 10 past 3). From 6 to 12 is <em>to the next hour</em> (e.g. 20 to 4).</li>
        <li><strong>am:</strong> Midnight to 11:59 am (morning). <strong>pm:</strong> Midday/noon to 11:59 pm (afternoon/evening).</li>
      </ul>
    </div>

    {tutor_vignette("👩‍⚕️", "Chloe", "Care Home Trainee", "When the long hand points to 8, that is 40 minutes past the hour, or 20 minutes to the next hour! Both describe the exact same time.")}

    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Reading Clinic Appointment</span>
      <p>An analogue clock shows the long minute hand pointing to <strong>9</strong> and the short hour hand just before <strong>3</strong>.<br>
      Write this time in words and as a 12-hour digital display in the afternoon.</p>
      <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:4px 8px; font-size:7.5pt; margin-top:3px;">
        1. Minute hand on 9 = <code>9 &times; 5 = 45</code> minutes past 2, or <em>quarter to 3</em>.<br>
        2. Hour hand is approaching 3.<br>
        <strong>Words:</strong> Quarter to three. &emsp; <strong>Digital (pm):</strong> 2:45 pm.
      </div>
    </div>

    <div class="box-trap">
      <span class="tag-label tag-red">Common Trap</span>
      Never write 'quarter to 2' if the hands say 2:45. The hour hand is moving towards 3!
    </div>
    """
    pages.append(wrap_page(p31, 31, "Strand 2: Measures, Shape & Space", "Standard: E3.15", "Maths Entry Level 3 Core Guide"))

    p32_scaffold = """
    <div class="step-row"><span>Step 1: Check minute hand (long)</span><span>Count in 5s around the dial</span></div>
    <div class="step-row"><span>Step 2: Check hour hand (short)</span><span>Determine past which hour it has moved</span></div>
    <div class="step-row"><span>Step 3: Combine with am or pm</span><span>e.g. 2:45 pm or Quarter to 3</span></div>
    """
    p32 = practice_page(
        "12-Hour Analogue & Digital Clocks", "Standard E3.15", 32, p32_scaffold,
        "Write these analogue clock readings in 12-hour digital format: a) Ten past 8 in the morning &emsp; b) Half past 2 in the afternoon &emsp; c) Quarter to 6 in the evening.",
        "State the time in words when a digital clock reads: a) 10:40 am &emsp; b) 04:15 pm.",
        "A doctor's appointment starts at 11:25 am and finishes at 11:50 am. How many minutes did the consultation take?"
    )
    pages.append(p32)

    # TOPIC 14: PAGE 33 (Theory) & PAGE 34 (Practice)
    p33 = f"""
    <h2>Unit 14: Time: 24-Hour Clock &amp; Timetables</h2>
    <p>Converting between 12-hour and 24-hour formats and extracting timetable information for shift work and public transport.</p>

    <div class="box-concept">
      <span class="tag-label tag-blue">Key Principle</span> <strong>The 24-Hour Conversion Rule:</strong>
      24-hour time always uses <strong>4 digits</strong> with no 'am' or 'pm'.
      <ul style="margin:3px 0 0 16px; padding:0; font-size:7.7pt;">
        <li><strong>Morning (am):</strong> Add a leading zero if needed (e.g. 8:20 am &rarr; <code>08:20</code>).</li>
        <li><strong>Afternoon/Evening (pm):</strong> <strong>Add 12 to the hours</strong> (e.g. 4:15 pm &rarr; <code>4 + 12 = 16:15</code>).</li>
        <li>To convert 24-hour to pm: <strong>Subtract 12 from the hours</strong> (e.g. <code>21:30 &rarr; 9:30 pm</code>).</li>
      </ul>
    </div>

    {tutor_vignette("👨‍🏫", "Tutor Marcus", "Senior Maths Specialist", "Remember: 12:00 is midday (noon), and 00:00 is midnight. Timetables always read from left to right for stops along a single journey!")}

    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Bus Timetable Reading</span>
      <p>Look at the bus schedule:</p>
      <table class="cgp-table" style="font-size:7.2pt; margin:3px 0;">
        <tr><th>Stop</th><th>Bus 1</th><th>Bus 2</th><th>Bus 3</th></tr>
        <tr><td>Town Centre</td><td>07:45</td><td>08:15</td><td>08:45</td></tr>
        <tr><td>Hospital</td><td>08:05</td><td>08:35</td><td>09:05</td></tr>
        <tr><td>Business Park</td><td>08:25</td><td>08:55</td><td>09:25</td></tr>
      </table>
      <p>A worker must arrive at the Business Park by 09:00. Which latest bus can she catch from the Town Centre?</p>
      <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:4px 8px; font-size:7.5pt; margin-top:3px;">
        1. Target arrival: By 09:00 at Business Park.<br>
        2. Bus 2 arrives at 08:55 (on time). Bus 3 arrives at 09:25 (too late!).<br>
        <strong>Answer:</strong> She must catch <strong>Bus 2 at 08:15</strong>.
      </div>
    </div>

    <div class="box-trap">
      <span class="tag-label tag-red">Exam Trap</span>
      Never write '16:15 pm'. 24-hour time never includes am or pm.
    </div>
    """
    pages.append(wrap_page(p33, 33, "Strand 2: Measures, Shape & Space", "Standard: E3.16", "Maths Entry Level 3 Core Guide"))

    p34_scaffold = """
    <div class="step-row"><span>Step 1: Check am or pm</span><span>pm means add 12 to the hours</span></div>
    <div class="step-row"><span>Step 2: Format to 4 digits</span><span>e.g. 9:15 am &rarr; 09:15 &bull; 7:30 pm &rarr; 19:30</span></div>
    <div class="step-row"><span>Step 3: Read timetables along columns</span><span>Follow one column down for a single vehicle</span></div>
    """
    p34 = practice_page(
        "24-Hour Clock & Timetables", "Standard E3.16", 34, p34_scaffold,
        "Convert to 24-hour clock: a) 7:15 am &emsp; b) 3:45 pm &emsp; c) 10:20 pm.",
        "Convert to 12-hour clock (with am or pm): a) 06:40 &emsp; b) 14:15 &emsp; c) 23:05.",
        "A train departs at 13:40 and arrives at its destination at 15:15. How long did the train journey take in hours and minutes?"
    )
    pages.append(p34)

    # TOPIC 15: PAGE 35 (Theory) & PAGE 36 (Practice)
    p35 = f"""
    <h2>Unit 15: Time: Elapsed Time &amp; Duration</h2>
    <p>Calculating time differences, journey durations, shift start and end times, and working across the hour boundary.</p>

    <div class="box-concept">
      <span class="tag-label tag-blue">Key Principle</span> <strong>Bridging the Hour (60 Minutes in an Hour):</strong>
      Because there are <strong>60 minutes in 1 hour</strong> (not 100!), you cannot use ordinary column subtraction for time durations!
      <br><strong>The Number Line Bridging Method:</strong>
      <ol style="margin:3px 0 0 16px; padding:0; font-size:7.7pt;">
        <li>Step 1: Count minutes from start time up to the next full hour.</li>
        <li>Step 2: Count full hours between the whole hour markers.</li>
        <li>Step 3: Count remaining minutes to the end time.</li>
        <li>Step 4: Add all pieces together!</li>
      </ol>
    </div>

    {tutor_vignette("👩‍🔧", "Maya", "Business Trainee", "Never do 10.15 &minus; 9.45 = 0.70! Time is based on 60 minutes. From 9:45 to 10:00 is 15 mins, plus 15 mins to 10:15 = 30 minutes total!")}

    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Warehouse Shift Calculation</span>
      <p>A night shift begins at <strong>21:45</strong> and finishes at <strong>06:15</strong> the following morning. Calculate the total shift duration.</p>
      <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:4px 8px; font-size:7.5pt; margin-top:3px;">
        1. From 21:45 to 22:00 = 15 minutes.<br>
        2. From 22:00 to 06:00 (midnight to 6 am) = 8 hours.<br>
        3. From 06:00 to 06:15 = 15 minutes.<br>
        4. Total: <code>8 hours + (15 + 15 mins) = 8 hours and 30 minutes</code>.
      </div>
    </div>

    <div class="box-trap">
      <span class="tag-label tag-red">Exam Trap</span>
      Always state your final duration clearly in <strong>hours and minutes</strong>.
    </div>
    """
    pages.append(wrap_page(p35, 35, "Strand 2: Measures, Shape & Space", "Standard: E3.17", "Maths Entry Level 3 Core Guide"))

    p36_scaffold = """
    <div class="step-row"><span>Step 1: Bridge to next whole hour</span><span>e.g. 08:35 to 09:00 = 25 minutes</span></div>
    <div class="step-row"><span>Step 2: Count full hours</span><span>09:00 to 11:00 = 2 hours</span></div>
    <div class="step-row"><span>Step 3: Add remaining minutes</span><span>11:00 to 11:15 = 15 mins &rarr; Total = 2h 40m</span></div>
    """
    p36 = practice_page(
        "Elapsed Time & Durations", "Standard E3.17", 36, p36_scaffold,
        "Calculate the time difference between: a) 09:15 and 10:45 &emsp; b) 14:40 and 16:10.",
        "A film starts at 18:25 and lasts 2 hours and 15 minutes. What time does the film end?",
        "A delivery driver starts work at 07:50. She takes a 45-minute lunch break and finishes at 16:35. How many hours and minutes did she spend driving/working excluding lunch?"
    )
    pages.append(p36)

    # TOPIC 16: PAGE 37 (Theory) & PAGE 38 (Practice)
    p37 = f"""
    <h2>Unit 16: Metric Length: mm, cm, m &amp; km</h2>
    <p>Measuring accurately with rulers, choosing sensible metric units, and converting between mm, cm, m, and km.</p>

    <div class="box-concept">
      <span class="tag-label tag-blue">Key Conversions to Memorise</span>
      <ul style="margin:3px 0 0 16px; padding:0; font-size:7.7pt;">
        <li><strong>1 centimetre (cm) = 10 millimetres (mm)</strong> (Multiply cm by 10 to get mm; Divide mm by 10 to get cm).</li>
        <li><strong>1 metre (m) = 100 centimetres (cm)</strong> (Multiply m by 100 to get cm; Divide cm by 100 to get m).</li>
        <li><strong>1 kilometre (km) = 1,000 metres (m)</strong> (Multiply km by 1,000 to get m; Divide m by 1,000 to get km).</li>
      </ul>
    </div>

    {tutor_vignette("👷‍♂️", "Dave", "Site Electrician", "Always convert both numbers to the SAME unit before adding or comparing! You cannot subtract 65 cm from 2 metres until you turn 2m into 200 cm!")}

    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Cutting Timber</span>
      <p>A carpenter has a wooden plank <strong>2 metres</strong> long. He cuts off a piece measuring <strong>65 cm</strong>. What length of plank is left in centimetres?</p>
      <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:4px 8px; font-size:7.5pt; margin-top:3px;">
        1. Convert 2 m to cm: <code>2 &times; 100 = 200 cm</code>.<br>
        2. Subtract the cut piece: <code>200 &minus; 65 = 135 cm</code>.<br>
        <strong>Remaining length:</strong> 135 cm (or 1.35 m).
      </div>
    </div>

    <div class="box-trap">
      <span class="tag-label tag-red">Sensible Units</span>
      Thickness of a coin &rarr; <strong>mm</strong> &bull; Length of a pen &rarr; <strong>cm</strong> &bull; Height of a door &rarr; <strong>m</strong> &bull; Distance between towns &rarr; <strong>km</strong>.
    </div>
    """
    pages.append(wrap_page(p37, 37, "Strand 2: Measures, Shape & Space", "Standard: E3.18", "Maths Entry Level 3 Core Guide"))

    p38_scaffold = """
    <div class="step-row"><span>Step 1: Conversion factor</span><span>1 cm = 10 mm &bull; 1 m = 100 cm &bull; 1 km = 1,000 m</span></div>
    <div class="step-row"><span>Step 2: Convert to matching unit</span><span>2 m = 200 cm</span></div>
    <div class="step-row"><span>Step 3: Perform calculation with units</span><span>200 &minus; 65 = 135 cm</span></div>
    """
    p38 = practice_page(
        "Metric Length & Conversions", "Standard E3.18", 38, p38_scaffold,
        "Complete these conversions: a) 4 cm = ___ mm &emsp; b) 30 mm = ___ cm &emsp; c) 5 m = ___ cm.",
        "Convert to metres: a) 400 cm = ___ m &emsp; b) 2 km = ___ m &emsp; c) 1,500 m = ___ km.",
        "A roll of electrical cable is 30 metres long. Dave uses 8 metres on Monday and 14 metres on Tuesday. How many metres of cable are left on the roll?"
    )
    pages.append(p38)

    # TOPIC 17: PAGE 39 (Theory) & PAGE 40 (Practice)
    p39 = f"""
    <h2>Unit 17: Metric Weight &amp; Capacity: g, kg, ml, L</h2>
    <p>Reading measuring scales for mass and liquid volume, choosing appropriate metric units, and solving practical recipes.</p>

    <div class="box-concept">
      <span class="tag-label tag-blue">Key Principles &amp; Conversions</span>
      <ul style="margin:3px 0 0 16px; padding:0; font-size:7.7pt;">
        <li><strong>Mass/Weight:</strong> <strong>1 kilogram (kg) = 1,000 grams (g)</strong> (&frac12; kg = 500g, &frac14; kg = 250g).</li>
        <li><strong>Liquid Capacity:</strong> <strong>1 litre (L) = 1,000 millilitres (ml)</strong> (&frac12; L = 500ml, &frac14; L = 250ml).</li>
        <li><strong>Reading Scales:</strong> Count the number of unnumbered division marks between numbers to find the value of each mark.</li>
      </ul>
    </div>

    {tutor_vignette("👩‍⚕️", "Chloe", "Care Home Trainee", "Always check the scale intervals! If there are 5 gaps between 0 and 500 ml, each small mark is 500 &divide; 5 = 100 ml!")}

    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Care Home Liquid Doses</span>
      <p>A measuring jug has marked intervals of 100 ml. Liquid reaches 3 tick marks above 400 ml. What volume of liquid is in the jug?</p>
      <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:4px 8px; font-size:7.5pt; margin-top:3px;">
        1. Value of each tick mark = 100 ml.<br>
        2. 3 ticks above 400 ml = <code>400 + (3 &times; 100) = 400 + 300 = 700 ml</code>.<br>
        <strong>Volume:</strong> 700 ml (or 0.7 litres).
      </div>
    </div>

    <div class="box-trap">
      <span class="tag-label tag-red">Exam Trap</span>
      Half a kilogram is 500 grams, NOT 50 grams! 1,000 divided by 2 is 500.
    </div>
    """
    pages.append(wrap_page(p39, 39, "Strand 2: Measures, Shape & Space", "Standard: E3.19", "Maths Entry Level 3 Core Guide"))

    p40_scaffold = """
    <div class="step-row"><span>Step 1: Check interval value</span><span>Gap between numbers &divide; number of divisions</span></div>
    <div class="step-row"><span>Step 2: Read pointer or level</span><span>Base number + (ticks &times; interval)</span></div>
    <div class="step-row"><span>Step 3: State value with units</span><span>700 ml or 0.7 L</span></div>
    """
    p40 = practice_page(
        "Metric Weight & Capacity", "Standard E3.19", 40, p40_scaffold,
        "Complete these conversions: a) 3 kg = ___ g &emsp; b) 2,000 g = ___ kg &emsp; c) &frac12; kg = ___ g.",
        "Complete capacity conversions: a) 4 L = ___ ml &emsp; b) 2,500 ml = ___ L &emsp; c) &frac14; L = ___ ml.",
        "A baker has a 1 kg bag of flour. He uses 350g for bread and 250g for scones. How many grams of flour remain in the bag?"
    )
    pages.append(p40)

    # TOPIC 18: PAGE 41 (Theory) & PAGE 42 (Practice)
    p41 = f"""
    <h2>Unit 18: Temperature: Reading Scales in &deg;C</h2>
    <p>Reading thermometers in degrees Celsius (&deg;C), interpreting values above and below zero, and calculating temperature changes.</p>

    <div class="box-concept">
      <span class="tag-label tag-blue">Key Principle</span> <strong>Degrees Celsius (&deg;C) &amp; Below Zero:</strong>
      <ul style="margin:3px 0 0 16px; padding:0; font-size:7.7pt;">
        <li><strong>0&deg;C:</strong> The freezing point of water.</li>
        <li><strong>Positive Temperatures (+):</strong> Above zero (e.g. +18&deg;C room temperature, +30&deg;C hot summer day).</li>
        <li><strong>Negative Temperatures (&minus;):</strong> Below zero (e.g. &minus;5&deg;C winter frost, &minus;18&deg;C commercial food freezer).</li>
        <li><strong>Comparing:</strong> &minus;4&deg;C is warmer than &minus;12&deg;C. The larger the negative number, the colder it is!</li>
      </ul>
    </div>

    {tutor_vignette("👨‍🏫", "Tutor Marcus", "Senior Maths Specialist", "To find the temperature rise from &minus;6&deg;C to +8&deg;C: count 6 degrees up to 0, then 8 degrees above 0. 6 + 8 = 14 degrees total rise!")}

    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Walk-in Freezer Temperature</span>
      <p>A supermarket freezer is set at <strong>&minus;18&deg;C</strong>. During maintenance, the temperature rises by <strong>7&deg;C</strong>. What is the new temperature?</p>
      <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:4px 8px; font-size:7.5pt; margin-top:3px;">
        1. Start at &minus;18&deg;C.<br>
        2. Rising means moving right (warmer) towards zero.<br>
        3. Calculation: <code>&minus;18 + 7 = &minus;11&deg;C</code>.<br>
        <strong>New temperature:</strong> &minus;11&deg;C.
      </div>
    </div>

    <div class="box-trap">
      <span class="tag-label tag-red">Exam Trap</span>
      Never drop the minus sign! Writing 11&deg;C instead of &minus;11&deg;C is the difference between a warm room and a frozen food storage unit.
    </div>
    """
    pages.append(wrap_page(p41, 41, "Strand 2: Measures, Shape & Space", "Standard: E3.20", "Maths Entry Level 3 Core Guide"))

    p42_scaffold = """
    <div class="step-row"><span>Step 1: Locate starting temperature</span><span>&minus;18&deg;C on vertical thermometer</span></div>
    <div class="step-row"><span>Step 2: Apply change (rise = +, drop = &minus;)</span><span>&minus;18 + 7</span></div>
    <div class="step-row"><span>Step 3: State final value with &deg;C</span><span>&minus;11&deg;C</span></div>
    """
    p42 = practice_page(
        "Temperature & &deg;C Scales", "Standard E3.20", 42, p42_scaffold,
        "Put these temperatures in order from <strong>coldest to warmest</strong>: +5&deg;C, &minus;8&deg;C, 0&deg;C, &minus;3&deg;C, +12&deg;C.",
        "The temperature outside is &minus;2&deg;C. Inside an office it is 21&deg;C. What is the difference in temperature?",
        "At midnight, the temperature was &minus;4&deg;C. By midday, the temperature had risen by 9&deg;C. What was the midday temperature?"
    )
    pages.append(p42)

    # TOPIC 19: PAGE 43 (Theory) & PAGE 44 (Practice)
    p43 = f"""
    <h2>Unit 19: Perimeter of Simple Rectangular Shapes</h2>
    <p>Calculating the perimeter (total distance around the boundary) of rectangles, squares, and compound shapes on grids.</p>

    <div class="box-concept">
      <span class="tag-label tag-blue">Key Principle</span> <strong>Perimeter Formula:</strong>
      <strong>Perimeter</strong> is the total distance all the way around the outside edge of a 2D shape.
      <ul style="margin:3px 0 0 16px; padding:0; font-size:7.7pt;">
        <li><strong>Rectangle:</strong> <code>Perimeter = Length + Width + Length + Width</code> (or <code>2 &times; (Length + Width)</code>).</li>
        <li><strong>Square:</strong> <code>Perimeter = 4 &times; Side Length</code>.</li>
        <li>Perimeter is measured in units of length (e.g. <strong>cm</strong> or <strong>m</strong>), NOT square units!</li>
      </ul>
    </div>

    {tutor_vignette("👷‍♂️", "Dave", "Site Electrician", "Opposite sides of a rectangle are always equal in length! If the top is 6m and the left is 4m, the bottom is 6m and the right is 4m. Add all 4 sides!")}

    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Fencing a Garden Plot</span>
      <p>A rectangular plot of land measures <strong>8 metres long</strong> and <strong>5 metres wide</strong>. How many metres of fencing are needed to enclose the plot?</p>
      <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:4px 8px; font-size:7.5pt; margin-top:3px;">
        1. Identify all 4 sides: 8m, 5m, 8m, 5m.<br>
        2. Add together: <code>8 + 5 + 8 + 5 = 26 metres</code>.<br>
        (Or: <code>(8 + 5) &times; 2 = 13 &times; 2 = 26 metres</code>).<br>
        <strong>Perimeter:</strong> 26 metres.
      </div>
    </div>

    <div class="box-trap">
      <span class="tag-label tag-red">Exam Trap</span>
      Do NOT multiply length &times; width! That gives the Area, not the Perimeter. Perimeter is the distance walked around the edge.
    </div>
    """
    pages.append(wrap_page(p43, 43, "Strand 2: Measures, Shape & Space", "Standard: E3.21", "Maths Entry Level 3 Core Guide"))

    p44_scaffold = """
    <div class="step-row"><span>Step 1: Identify all 4 side lengths</span><span>Length = 8m, Width = 5m, Length = 8m, Width = 5m</span></div>
    <div class="step-row"><span>Step 2: Add all sides around the perimeter</span><span>8 + 5 + 8 + 5 = 26</span></div>
    <div class="step-row"><span>Step 3: State unit of length</span><span>26 metres (m)</span></div>
    """
    p44 = practice_page(
        "Perimeter of Rectangles & Grids", "Standard E3.21", 44, p44_scaffold,
        "Calculate the perimeter of each shape: a) A square with side length 7 cm &emsp; b) A rectangle measuring 9 m by 4 m.",
        "A rectangular notice board is 120 cm long and 80 cm high. An administrator puts decorative border tape all around the edge. How much tape is needed in centimetres?",
        "A rectangular lawn measures 10 metres by 6 metres. Wooden edging costs &pound;4 per metre. How much does it cost to put edging around the entire lawn?"
    )
    pages.append(p44)

    # TOPIC 20: PAGE 45 (Theory) & PAGE 46 (Practice)
    p45 = f"""
    <h2>Unit 20: 2D &amp; 3D Shapes, Faces, Edges &amp; Symmetry</h2>
    <p>Classifying polygons, identifying solid properties (faces, edges, vertices), and locating lines of symmetry.</p>

    <div class="box-concept">
      <span class="tag-label tag-blue">Key Principles &amp; Definitions</span>
      <ul style="margin:3px 0 0 16px; padding:0; font-size:7.7pt;">
        <li><strong>2D Polygons:</strong> Triangle (3 sides), Quadrilateral (4 sides), Pentagon (5 sides), Hexagon (6 sides), Octagon (8 sides).</li>
        <li><strong>3D Solids:</strong>
          <br>&bull; <strong>Cube &amp; Cuboid:</strong> 6 flat faces, 12 straight edges, 8 vertices (corners).
          <br>&bull; <strong>Cylinder:</strong> 2 flat circular faces, 1 curved surface, 2 curved edges, 0 vertices.
          <br>&bull; <strong>Sphere:</strong> 1 continuous curved surface, 0 edges, 0 vertices.
          <br>&bull; <strong>Cone:</strong> 1 flat circular face, 1 curved surface, 1 vertex.
        </li>
        <li><strong>Line of Symmetry:</strong> A fold line that divides a shape into two identical mirror-image halves.</li>
      </ul>
    </div>

    {tutor_vignette("👩‍🔧", "Maya", "Business Trainee", "A rectangle has only 2 lines of symmetry (horizontal and vertical through the centres). Diagonals of an ordinary rectangle are NOT lines of symmetry!")}

    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Packaging Identification</span>
      <p>A warehouse worker handles a package that has <strong>6 rectangular faces</strong>, <strong>12 straight edges</strong>, and <strong>8 vertices</strong>. What 3D shape is the package?</p>
      <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:4px 8px; font-size:7.5pt; margin-top:3px;">
        1. A 3D solid with 6 rectangular faces is a <strong>Cuboid</strong>.<br>
        2. (If all 6 faces were identical squares, it would be a Cube).<br>
        <strong>Answer:</strong> Cuboid.
      </div>
    </div>

    <div class="box-trap">
      <span class="tag-label tag-red">Exam Vocabulary</span>
      <strong>Vertices</strong> are corners (points). A single corner is called a <strong>vertex</strong>.
    </div>
    """
    pages.append(wrap_page(p45, 45, "Strand 2: Measures, Shape & Space", "Standard: E3.22", "Maths Entry Level 3 Core Guide"))

    p46_scaffold = """
    <div class="step-row"><span>Step 1: Count faces / flat surfaces</span><span>6 faces</span></div>
    <div class="step-row"><span>Step 2: Count edges &amp; vertices</span><span>12 edges &bull; 8 vertices</span></div>
    <div class="step-row"><span>Step 3: State correct 3D solid name</span><span>Cuboid (or Cube)</span></div>
    """
    p46 = practice_page(
        "2D & 3D Shapes & Symmetry", "Standard E3.22", 46, p46_scaffold,
        "Match each polygon to its number of straight sides: a) Triangle &emsp; b) Hexagon &emsp; c) Pentagon &emsp; d) Octagon.",
        "How many faces, edges, and vertices does a Cube have?",
        "Name a 3D shape that has a curved surface and no flat faces, and state how many lines of symmetry a standard square has."
    )
    pages.append(p46)

    # -------------------------------------------------------------
    # STRAND 2 CHECKPOINT (PAGES 47, 48, 49, 50) - Total 30 Marks
    # -------------------------------------------------------------
    chk2_p1 = [
        ("1", 2, "A customer buys a sandwich for &pound;3.65 and a drink for &pound;1.80. Calculate the total cost.", 50),
        ("2", 2, "How much change does a customer receive from a &pound;10 note after spending &pound;6.35?", 50),
        ("3", 2, "Convert these times to 24-hour clock: a) 8:20 am &emsp; b) 4:45 pm.", 50)
    ]
    pages.append(checkpoint_page("Strand 2: Measures, Shape &amp; Space", "Part 1 &bull; Non-Calculator (Q1-Q3)", 47, "6 Marks", chk2_p1))

    chk2_p2 = [
        ("4", 2, "A workshop clock shows quarter to four in the afternoon. Write this time as a 24-hour digital time.", 52),
        ("5", 2, "Convert these measurements: a) 4 cm to mm &emsp; b) 3 metres to cm &emsp; c) 2,000 g to kg.", 52),
        ("6", 2, "Calculate the perimeter of a rectangular workshop floor measuring 7 metres long and 4 metres wide.", 52)
    ]
    pages.append(checkpoint_page("Strand 2: Measures, Shape &amp; Space", "Part 1 &bull; Non-Calculator (Q4-Q6)", 48, "6 Marks", chk2_p2))

    chk2_p3 = [
        ("7", 2, "A train departs at 08:35 and arrives at 10:15. How long did the journey take in hours and minutes?", 52),
        ("8", 3, "A commercial freezer operates at &minus;19&deg;C. An alarm sounds if the temperature rises by more than 5&deg;C. What is the maximum permitted alarm temperature?", 60),
        ("9", 3, "A decorator needs to paint a border around a rectangular room measuring 6 metres by 5 metres. Border ribbon costs &pound;2.50 per metre. How much will the ribbon cost altogether?", 60)
    ]
    pages.append(checkpoint_page("Strand 2: Measures, Shape &amp; Space", "Part 2 &bull; Calculator Allowed (Q7-Q9)", 49, "8 Marks", chk2_p3))

    chk2_p4 = [
        ("10", 3, "A bottle of antiseptic liquid holds 500 ml. A healthcare assistant uses 45 ml for each cleaning task. How many full cleaning tasks can be completed?", 60),
        ("11", 3, "Identify this 3D solid: it has 6 flat square faces, 12 equal straight edges, and 8 vertices. State its name and how many lines of symmetry one of its faces has.", 60),
        ("12", 4, "A community café serves 45 customers. Each cup of tea uses 40 ml of milk. How many litres of milk are needed in total? (Hint: 1 litre = 1,000 ml).", 70)
    ]
    pages.append(checkpoint_page("Strand 2: Measures, Shape &amp; Space", "Part 2 &bull; Calculator Allowed (Q10-Q12)", 50, "10 Marks", chk2_p4))

    # =========================================================================
    # STRAND 3: HANDLING INFORMATION & DATA (Units 21 to 28 & Checkpoint)
    # =========================================================================

    # TOPIC 21: PAGE 51 (Theory) & PAGE 52 (Practice)
    p51 = f"""
    <h2>Unit 21: Position, Direction &amp; 4 Compass Points</h2>
    <p>Using the compass points (North, East, South, West), understanding turns (quarter, half, full), and describing directional travel.</p>

    <div class="box-concept">
      <span class="tag-label tag-blue">Key Principles &amp; Compass Points</span>
      <ul style="margin:3px 0 0 16px; padding:0; font-size:7.7pt;">
        <li><strong>The 4 Main Directions:</strong> <strong>North (N), East (E), South (S), West (W)</strong>.</li>
        <li><strong>Clockwise Mnemonic:</strong> <strong>N</strong>ever <strong>E</strong>at <strong>S</strong>hredded <strong>W</strong>heat (starts at top, turns clockwise to the right).</li>
        <li><strong>Turns:</strong>
          <br>&bull; Quarter turn (90&deg;): Facing N &rarr; turn clockwise &rarr; now facing <strong>East</strong>.
          <br>&bull; Half turn (180&deg;): Points in the exact opposite direction (e.g. North &harr; South).
          <br>&bull; Three-quarter turn (270&deg;) clockwise from North points <strong>West</strong>.
        </li>
      </ul>
    </div>

    {tutor_vignette("👷‍♂️", "Dave", "Site Electrician", "Clockwise turns in the direction clock hands move (to the right from 12). Anti-clockwise turns to the left!")}

    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Forklift Truck Navigation</span>
      <p>A forklift truck driver is facing <strong>North</strong> in a warehouse aisle. At an intersection, he makes a <strong>quarter turn clockwise</strong>. Which compass direction is he now facing?</p>
      <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:4px 8px; font-size:7.5pt; margin-top:3px;">
        1. Start facing North (pointing up).<br>
        2. Turning clockwise means rotating to the right.<br>
        3. A quarter turn (90&deg;) clockwise points directly to <strong>East</strong>.<br>
        <strong>Answer:</strong> East.
      </div>
    </div>

    <div class="box-trap">
      <span class="tag-label tag-red">Exam Trap</span>
      Never confuse East and West! East is on the right side of a standard map; West is on the left.
    </div>
    """
    pages.append(wrap_page(p51, 51, "Strand 3: Handling Information & Data", "Standard: E3.23", "Maths Entry Level 3 Core Guide"))

    p52_scaffold = """
    <div class="step-row"><span>Step 1: Identify initial facing direction</span><span>Facing North (0&deg; / 12 o'clock)</span></div>
    <div class="step-row"><span>Step 2: Determine turn direction &amp; angle</span><span>Clockwise quarter turn (90&deg; right)</span></div>
    <div class="step-row"><span>Step 3: State final compass heading</span><span>East (E)</span></div>
    """
    p52 = practice_page(
        "Compass Points & Turns", "Standard E3.23", 52, p52_scaffold,
        "Write the four compass points in clockwise order starting from North.",
        "If you are facing South and make a half turn (180&deg;), which direction are you now facing?",
        "A delivery van is travelling East. The driver makes a quarter turn anti-clockwise. Which direction is the van now heading?"
    )
    pages.append(p52)

    # TOPIC 22: PAGE 53 (Theory) & PAGE 54 (Practice)
    p53 = f"""
    <h2>Unit 22: Workplace Grid References &amp; Maps</h2>
    <p>Using coordinates, grid squares, and layout plans to locate equipment, navigate depots, and plan safe workplace routes.</p>

    <div class="box-concept">
      <span class="tag-label tag-blue">Key Principle</span> <strong>Reading Coordinates: "Along the Corridor, Up the Stairs"</strong>
      <ul style="margin:3px 0 0 16px; padding:0; font-size:7.7pt;">
        <li><strong>Horizontal Axis (X):</strong> Read the letter or number along the bottom first (along the corridor).</li>
        <li><strong>Vertical Axis (Y):</strong> Read the number up the side second (up the stairs).</li>
        <li>Coordinates are written in brackets or letter-number pairs: e.g. <code>(3, 4)</code> or <code>B3</code>.</li>
      </ul>
    </div>

    {tutor_vignette("👩‍🔧", "Maya", "Business Trainee", "Always check the axis labels! In a grid reference like C4, C is horizontal column, 4 is vertical row!")}

    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Logistics Grid Map</span>
      <p>A depot storage floor is mapped on a grid. Safety helmets are stored at <strong>(2, 5)</strong> and High-Vis jackets are at <strong>(6, 5)</strong>.<br>
      Which item is stored further to the East (right)?</p>
      <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:4px 8px; font-size:7.5pt; margin-top:3px;">
        1. Compare X coordinates (horizontal / East): Helmets = 2, High-Vis = 6.<br>
        2. 6 is greater than 2, meaning it is further to the right.<br>
        <strong>Answer:</strong> High-Vis jackets are further East.
      </div>
    </div>

    <div class="box-trap">
      <span class="tag-label tag-red">Common Trap</span>
      Never reverse the order! (2, 5) is completely different from (5, 2). Horizontal always comes first.
    </div>
    """
    pages.append(wrap_page(p53, 53, "Strand 3: Handling Information & Data", "Standard: E3.24", "Maths Entry Level 3 Core Guide"))

    p54_scaffold = """
    <div class="step-row"><span>Step 1: Read horizontal X coordinate</span><span>Count along bottom axis first</span></div>
    <div class="step-row"><span>Step 2: Read vertical Y coordinate</span><span>Count up the side axis second</span></div>
    <div class="step-row"><span>Step 3: Combine in brackets</span><span>(X, Y) e.g. (2, 5)</span></div>
    """
    p54 = practice_page(
        "Grid References & Workplace Maps", "Standard E3.24", 54, p54_scaffold,
        "A warehouse layout places Ladders at grid reference (4, 2) and Power Tools at (1, 6). Write down the horizontal and vertical positions for Ladders.",
        "A hospital floor plan has Wards labelled A to D along the bottom and Floors 1 to 4 up the side. Which ward is located at grid reference B3?",
        "A delivery robot moves on a factory grid from position (2, 1) to (2, 5). Describe the direction and distance in grid units that the robot moved."
    )
    pages.append(p54)

    # TOPIC 23: PAGE 55 (Theory) & PAGE 56 (Practice)
    p55 = f"""
    <h2>Unit 23: Data Collection: Tally &amp; Frequency Tables</h2>
    <p>Recording raw observations systematically with tally marks and compiling clean frequency totals for reporting.</p>

    <div class="box-concept">
      <span class="tag-label tag-blue">Key Principle</span> <strong>The Tally System (Groups of 5):</strong>
      Tally marks record occurrences as they happen.
      <ul style="margin:3px 0 0 16px; padding:0; font-size:7.7pt;">
        <li>Individual items are drawn as vertical strokes: <code>|</code> = 1, <code>||</code> = 2, <code>|||</code> = 3, <code>||||</code> = 4.</li>
        <li>The 5th item is drawn as a diagonal gate across the four strokes: <code><s>||||</s></code> = 5.</li>
        <li><strong>Frequency:</strong> The total number of items counted in each category (written in standard digits).</li>
      </ul>
    </div>

    {tutor_vignette("👩‍⚕️", "Chloe", "Care Home Trainee", "Always count tally marks in 5s first, then add the single strokes! <s>||||</s> <s>||||</s> ||| is 5 + 5 + 3 = 13.")}

    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Staff Lunch Survey</span>
      <p>A workplace canteen records choices: Soup (8), Salad (12), Pasta (6). Show how 12 is represented in tally marks and find the total responses.</p>
      <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:4px 8px; font-size:7.5pt; margin-top:3px;">
        1. 12 = two full gates of 5 plus 2 single strokes: <code><s>||||</s> <s>||||</s> ||</code>.<br>
        2. Total responses: <code>8 + 12 + 6 = 26</code> staff.<br>
        <strong>Total survey count:</strong> 26 responses.
      </div>
    </div>

    <div class="box-trap">
      <span class="tag-label tag-red">Exam Check</span>
      Always sum the frequency column to ensure no raw survey responses were accidentally omitted.
    </div>
    """
    pages.append(wrap_page(p55, 55, "Strand 3: Handling Information & Data", "Standard: E3.25", "Maths Entry Level 3 Core Guide"))

    p56_scaffold = """
    <div class="step-row"><span>Step 1: Group tallies into 5s</span><span><s>||||</s> = 5</span></div>
    <div class="step-row"><span>Step 2: Add extra strokes</span><span>5 + 5 + 2 = 12</span></div>
    <div class="step-row"><span>Step 3: Total the frequency column</span><span>8 + 12 + 6 = 26</span></div>
    """
    p56 = practice_page(
        "Tally Charts & Frequency Tables", "Standard E3.25", 56, p56_scaffold,
        "Draw the correct tally marks for these quantities: a) 7 &emsp; b) 14 &emsp; c) 19.",
        "A survey records hot drink orders: Tea: <s>||||</s> <s>||||</s> | &emsp; Coffee: <s>||||</s> <s>||||</s> <s>||||</s> &emsp; Water: <s>||||</s>. Write the frequency for each.",
        "How many more people chose Coffee than Tea in the hot drink survey above, and what was the grand total of drinks ordered?"
    )
    pages.append(p56)

    # TOPIC 24: PAGE 57 (Theory) & PAGE 58 (Practice)
    p57 = f"""
    <h2>Unit 24: Pictograms: Reading &amp; Interpreting Keys</h2>
    <p>Extracting numerical information from pictograms, calculating values from full and half symbols, and completing keys.</p>

    <div class="box-concept">
      <span class="tag-label tag-blue">Key Principle</span> <strong>The Pictogram Key:</strong>
      A pictogram uses pictures or symbols to represent data. You must <strong>always look at the key first</strong>!
      <ul style="margin:3px 0 0 16px; padding:0; font-size:7.7pt;">
        <li>If 1 symbol &square; = <strong>4 items</strong>:</li>
        <li>A half symbol represents <code>4 &divide; 2 = 2 items</code>.</li>
        <li>A quarter symbol represents <code>4 &divide; 4 = 1 item</code>.</li>
      </ul>
    </div>

    {tutor_vignette("👨‍🏫", "Tutor Marcus", "Senior Maths Specialist", "Never assume one symbol equals 1 person or 1 item! In Functional Skills exams, the key almost always equals 2, 4, 5, or 10 items!")}

    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Fleet Van Deliveries</span>
      <p>A pictogram shows daily parcel batches. The key states: <strong>&FilledSmallSquare; = 10 parcels</strong>.<br>
      Monday has 3 full squares. Tuesday has 2 and a half squares. How many parcels were delivered across both days?</p>
      <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:4px 8px; font-size:7.5pt; margin-top:3px;">
        1. Monday: <code>3 &times; 10 = 30</code> parcels.<br>
        2. Tuesday: <code>(2 &times; 10) + 5 = 20 + 5 = 25</code> parcels.<br>
        3. Combined total: <code>30 + 25 = 55</code> parcels.<br>
        <strong>Answer:</strong> 55 parcels.
      </div>
    </div>

    <div class="box-trap">
      <span class="tag-label tag-red">Exam Trap</span>
      Draw symbols neatly! If the symbol is a circle, half a symbol must be a clear semicircle, not a messy scribble.
    </div>
    """
    pages.append(wrap_page(p57, 57, "Strand 3: Handling Information & Data", "Standard: E3.26", "Maths Entry Level 3 Core Guide"))

    p58_scaffold = """
    <div class="step-row"><span>Step 1: Check the Key</span><span>1 symbol = 10 items &bull; Half symbol = 5 items</span></div>
    <div class="step-row"><span>Step 2: Multiply full symbols</span><span>3 &times; 10 = 30</span></div>
    <div class="step-row"><span>Step 3: Add fractional symbols</span><span>30 + 25 = 55</span></div>
    """
    p58 = practice_page(
        "Pictograms & Keys", "Standard E3.26", 58, p58_scaffold,
        "In a bookshop pictogram, 1 book symbol represents 8 books sold. How many books do 3 full symbols and 1 half symbol represent?",
        "A car sales depot sells 24 vehicles on Friday. If each &starf; represents 4 vehicles, how many star symbols must be drawn on the pictogram?",
        "A sports club records members: Football has 4 symbols, Tennis has 2 and a half symbols. If each symbol = 6 members, how many more members play Football than Tennis?"
    )
    pages.append(p58)

    # TOPIC 25: PAGE 59 (Theory) & PAGE 60 (Practice)
    p59 = f"""
    <h2>Unit 25: Bar Charts: Reading &amp; Interpreting Scales</h2>
    <p>Extracting data accurately from vertical and horizontal bar charts, reading between scale markings, and comparing categories.</p>

    <div class="box-concept">
      <span class="tag-label tag-blue">Key Principle</span> <strong>Anatomy of a Bar Chart:</strong>
      <ul style="margin:3px 0 0 16px; padding:0; font-size:7.7pt;">
        <li><strong>Vertical Axis (Frequency/Number):</strong> Shows the quantitative scale. Check the scale interval (e.g. 1s, 2s, 5s, 10s, 20s).</li>
        <li><strong>Horizontal Axis (Categories):</strong> Shows the distinct items or groups being compared.</li>
        <li><strong>Reading Between Lines:</strong> If grid lines go up in 10s (0, 10, 20, 30...), a bar halfway between 20 and 30 represents <strong>25</strong>.</li>
      </ul>
    </div>

    {tutor_vignette("👩‍🔧", "Maya", "Business Trainee", "Use a ruler laid flat across from the top of the bar to the vertical scale to ensure your reading is 100% accurate!")}

    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Gym Attendance</span>
      <p>A bar chart displays daily gym visitors: Mon (40), Tue (65), Wed (50), Thu (80), Fri (95).<br>
      a) Which day had the most visitors? &emsp; b) How many more visitors attended on Friday than on Wednesday?</p>
      <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:4px 8px; font-size:7.5pt; margin-top:3px;">
        a) Highest bar is Friday with 95 visitors &rarr; <strong>Friday</strong>.<br>
        b) Difference: <code>95 &minus; 50 = 45</code> visitors.<br>
        <strong>Answer:</strong> 45 more visitors.
      </div>
    </div>

    <div class="box-trap">
      <span class="tag-label tag-red">Exam Trap</span>
      Never guess bar heights! Always count the exact subdivisions between numbered grid lines.
    </div>
    """
    pages.append(wrap_page(p59, 59, "Strand 3: Handling Information & Data", "Standard: E3.27", "Maths Entry Level 3 Core Guide"))

    p60_scaffold = """
    <div class="step-row"><span>Step 1: Check axis scale interval</span><span>Lines go up in 10s (halfway = 5)</span></div>
    <div class="step-row"><span>Step 2: Read bar tops with ruler</span><span>Friday = 95 &bull; Wednesday = 50</span></div>
    <div class="step-row"><span>Step 3: Subtract to find difference</span><span>95 &minus; 50 = 45</span></div>
    """
    p60 = practice_page(
        "Reading Bar Charts", "Standard E3.27", 60, p60_scaffold,
        "A bar chart scale goes up in 5s: 0, 5, 10, 15, 20. What value is indicated by a bar resting halfway between 15 and 20?",
        "Staff absences in a depot: Sales (4), IT (2), Admin (6), Transport (8). Which department had the fewest absences, and what is the total number of absences?",
        "How many more staff were absent in Transport than in Sales?"
    )
    pages.append(p60)

    # TOPIC 26: PAGE 61 (Theory) & PAGE 62 (Practice)
    p61 = f"""
    <h2>Unit 26: Bar Charts: Constructing &amp; Labelling</h2>
    <p>Drawing official bar charts accurately with titles, labelled axes, evenly spaced scales, and equal-width bars.</p>

    <div class="box-concept">
      <span class="tag-label tag-blue">The 5 Rules of an Exam-Standard Bar Chart</span>
      In Functional Skills exams, drawing a bar chart can carry up to <strong>4 marks</strong>. You must include:
      <ol style="margin:3px 0 0 16px; padding:0; font-size:7.7pt;">
        <li><strong>Title:</strong> Clear and descriptive of the data shown.</li>
        <li><strong>Vertical Axis Label:</strong> Named (e.g. <em>Number of People</em>, <em>Sales (&pound;)</em>).</li>
        <li><strong>Evenly Spaced Numerical Scale:</strong> Starts at 0, goes up in consistent increments (e.g. 2, 4, 6... or 5, 10, 15...).</li>
        <li><strong>Horizontal Axis Label &amp; Categories:</strong> Every category clearly named beneath its bar.</li>
        <li><strong>Equal Width Bars &amp; Gaps:</strong> Use a ruler! All bars should be the same width with equal spaces between them.</li>
      </ol>
    </div>

    {tutor_vignette("👨‍🏫", "Tutor Marcus", "Senior Maths Specialist", "The most common lost mark on exam bar charts is forgetting to label the axes! Always write 'Frequency' on the side and the category name on the bottom!")}

    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Vehicle Breakdown Types</span>
      <p>Plot a bar chart for garage repairs: Battery (14), Tyres (10), Brakes (6). Scale starts at 0 and goes up in 2s.</p>
      <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:4px 8px; font-size:7.5pt; margin-top:3px;">
        1. Vertical axis: Mark 0, 2, 4, 6, 8, 10, 12, 14, 16. Label: 'Number of Vehicles'.<br>
        2. Horizontal axis: Mark Battery, Tyres, Brakes. Label: 'Repair Type'.<br>
        3. Draw bars: Battery up to 14, Tyres up to 10, Brakes up to 6.
      </div>
    </div>

    <div class="box-trap">
      <span class="tag-label tag-red">Exam Trap</span>
      Never join the bars together like a histogram! In discrete bar charts, leave a consistent gap between bars.
    </div>
    """
    pages.append(wrap_page(p61, 61, "Strand 3: Handling Information & Data", "Standard: E3.28", "Maths Entry Level 3 Core Guide"))

    p62_scaffold = """
    <div class="step-row"><span>Step 1: Write Title &amp; Axis Labels</span><span>'Garage Repairs' &bull; 'Number of Repairs'</span></div>
    <div class="step-row"><span>Step 2: Choose even scale from 0</span><span>0, 2, 4, 6, 8, 10, 12, 14, 16</span></div>
    <div class="step-row"><span>Step 3: Plot bars with ruler &amp; equal gaps</span><span>Battery = 14 &bull; Tyres = 10 &bull; Brakes = 6</span></div>
    """
    p62 = practice_page(
        "Constructing Bar Charts", "Standard E3.28", 62, p62_scaffold,
        "State four essential features that an examiner looks for when marking a newly drawn bar chart.",
        "A workplace canteen sells drinks: Tea (15), Coffee (25), Juice (10). If plotting on a grid with 10 squares height, what is the best scale interval to use (1s, 2s, or 5s)?",
        "Explain why a bar chart scale of '0, 5, 10, 12, 15, 20' is incorrect and would lose marks."
    )
    pages.append(p62)

    # TOPIC 27: PAGE 63 (Theory) & PAGE 64 (Practice)
    p63 = f"""
    <h2>Unit 27: Sorting Data: Lists, Tables &amp; Diagrams</h2>
    <p>Organising data using two-way tables, Carroll diagrams, and Venn diagrams to sort items according to two criteria.</p>

    <div class="box-concept">
      <span class="tag-label tag-blue">Key Principles &amp; Sorting Tools</span>
      <ul style="margin:3px 0 0 16px; padding:0; font-size:7.7pt;">
        <li><strong>Two-Way Tables:</strong> Organise numbers into rows and columns with total rows and columns.</li>
        <li><strong>Carroll Diagrams:</strong> A 2&times;2 grid sorting data into 'is' or 'is not' (e.g. Even vs Not Even; Over 100 vs Not Over 100).</li>
        <li><strong>Venn Diagrams:</strong> Overlapping circles where the overlapping section represents items meeting <strong>both</strong> criteria.</li>
      </ul>
    </div>

    {tutor_vignette("👩‍🔧", "Maya", "Business Trainee", "In a two-way table, always check that the row totals and column totals add up to the exact same grand total in the bottom-right corner!")}

    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Staff Training Completion</span>
      <table class="cgp-table" style="font-size:7.2pt; margin:3px 0;">
        <tr><th>Department</th><th>Completed</th><th>Pending</th><th>Total</th></tr>
        <tr><td>Depot</td><td>18</td><td>6</td><td>24</td></tr>
        <tr><td>Office</td><td>12</td><td>4</td><td>16</td></tr>
        <tr><td><strong>Total</strong></td><td><strong>30</strong></td><td><strong>10</strong></td><td><strong>40</strong></td></tr>
      </table>
      <p>How many staff are in the Office department, and how many total staff have completed training?</p>
      <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:4px 8px; font-size:7.5pt; margin-top:3px;">
        1. Office total row = <code>12 + 4 = 16</code> staff.<br>
        2. Completed column total = <code>18 + 12 = 30</code> staff.<br>
        <strong>Answers:</strong> 16 office staff; 30 staff completed.
      </div>
    </div>

    <div class="box-trap">
      <span class="tag-label tag-red">Exam Trap</span>
      Never confuse rows (horizontal) and columns (vertical) when extracting data from two-way tables.
    </div>
    """
    pages.append(wrap_page(p63, 63, "Strand 3: Handling Information & Data", "Standard: E3.29", "Maths Entry Level 3 Core Guide"))

    p64_scaffold = """
    <div class="step-row"><span>Step 1: Locate target row and column</span><span>Cross-reference category headers</span></div>
    <div class="step-row"><span>Step 2: Read intersection value</span><span>e.g. Office &amp; Completed = 12</span></div>
    <div class="step-row"><span>Step 3: Verify grand totals match</span><span>30 + 10 = 40 &bull; 24 + 16 = 40</span></div>
    """
    p64 = practice_page(
        "Sorting Data & Two-Way Tables", "Standard E3.29", 64, p64_scaffold,
        "Using the staff training table on the left: How many Depot staff have training pending?",
        "Complete the missing values in this table: 15 full-time staff and 8 part-time staff passed their driving assessment; 5 full-time and 4 part-time staff did not pass. How many total staff took the assessment?",
        "Sort these numbers into a Carroll diagram (Even / Not Even &bull; More than 50 / Not more than 50): 24, 55, 62, 37."
    )
    pages.append(p64)

    # TOPIC 28: PAGE 65 (Theory) & PAGE 66 (Practice)
    p65 = f"""
    <h2>Unit 28: Probability &amp; Practical Chance</h2>
    <p>Using the language of chance to evaluate everyday workplace risks, outcomes, and likelihood on a probability scale.</p>

    <div class="box-concept">
      <span class="tag-label tag-blue">Key Principle</span> <strong>The Probability Scale:</strong>
      Chance measures how likely an event is to happen. Entry Level 3 uses five standard terms:
      <ul style="margin:3px 0 0 16px; padding:0; font-size:7.7pt;">
        <li><strong>Impossible:</strong> Cannot ever happen (e.g. rolling an 8 on a standard 6-sided dice).</li>
        <li><strong>Unlikely:</strong> Small chance of occurring, but not impossible (e.g. winning the lottery).</li>
        <li><strong>Even Chance (Evens / 50:50):</strong> Exactly as likely to happen as not (e.g. tossing heads on an unbiased coin).</li>
        <li><strong>Likely:</strong> Good chance of occurring (e.g. rain in November in the UK).</li>
        <li><strong>Certain:</strong> 100% guaranteed to happen (e.g. the sun rising tomorrow).</li>
      </ul>
    </div>

    {tutor_vignette("👨‍🏫", "Tutor Marcus", "Senior Maths Specialist", "On an Entry 3 exam, use the exact statutory words: Impossible, Unlikely, Even Chance, Likely, or Certain. Don't write 'maybe' or 'pretty sure'!")}

    <div class="box-example">
      <span class="tag-label tag-green">Worked Example: Safety Glove Dispenser</span>
      <p>A box contains <strong>18 blue gloves</strong> and <strong>2 red gloves</strong>. A worker picks one glove without looking.<br>
      Describe the likelihood of picking: a) A blue glove &emsp; b) A red glove &emsp; c) A green glove.</p>
      <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:4px 8px; font-size:7.5pt; margin-top:3px;">
        a) 18 out of 20 are blue &rarr; <strong>Likely</strong>.<br>
        b) Only 2 out of 20 are red &rarr; <strong>Unlikely</strong>.<br>
        c) There are no green gloves in the box &rarr; <strong>Impossible</strong>.
      </div>
    </div>

    <div class="box-trap">
      <span class="tag-label tag-red">Exam Trap</span>
      Even chance only applies when outcomes are exactly 50:50 (equal numbers of choices).
    </div>
    """
    pages.append(wrap_page(p65, 65, "Strand 3: Handling Information & Data", "Standard: E3.30", "Maths Entry Level 3 Core Guide"))

    p66_scaffold = """
    <div class="step-row"><span>Step 1: Count total possible items</span><span>18 blue + 2 red = 20 total</span></div>
    <div class="step-row"><span>Step 2: Compare target item count to total</span><span>18/20 = most; 2/20 = few; 0 = none</span></div>
    <div class="step-row"><span>Step 3: Select official probability term</span><span>Impossible &bull; Unlikely &bull; Evens &bull; Likely &bull; Certain</span></div>
    """
    p66 = practice_page(
        "Probability & Vocabulary of Chance", "Standard E3.30", 66, p66_scaffold,
        "Match each scenario to its probability term (Impossible, Unlikely, Even Chance, Likely, Certain): a) Rolling a number less than 7 on a normal 6-sided dice &emsp; b) Tossing tails on a fair coin &emsp; c) Drawing a green counter from a bag of only red counters.",
        "A raffle sells 100 tickets. Marcus buys 85 tickets. How likely is it that Marcus wins the raffle prize?",
        "A bag contains 5 red balls and 5 yellow balls. What is the chance of selecting a red ball?"
    )
    pages.append(p66)

    # -------------------------------------------------------------
    # STRAND 3 CHECKPOINT (PAGES 67, 68, 69, 70) - Total 30 Marks
    # -------------------------------------------------------------
    chk3_p1 = [
        ("1", 2, "Name the four compass directions in clockwise order starting with North.", 50),
        ("2", 2, "If a forklift is travelling West and makes a quarter turn clockwise, which direction is it now facing?", 50),
        ("3", 2, "A storeroom map places First Aid at grid (3, 5) and Fire Extinguisher at (5, 2). Which item is higher up the vertical Y-axis?", 50)
    ]
    pages.append(checkpoint_page("Strand 3: Handling Information &amp; Data", "Part 1 &bull; Non-Calculator (Q1-Q3)", 67, "6 Marks", chk3_p1))

    chk3_p2 = [
        ("4", 2, "A worker records parcel weights: <s>||||</s> <s>||||</s> <s>||||</s> ||. Write the frequency in digits.", 52),
        ("5", 2, "In a pictogram, 1 circle represents 4 delivery vans. How many vans do 3 and a half circles represent?", 52),
        ("6", 2, "State whether the following event is Certain, Likely, Even Chance, Unlikely, or Impossible: Rolling an odd number on a standard 6-sided dice.", 52)
    ]
    pages.append(checkpoint_page("Strand 3: Handling Information &amp; Data", "Part 1 &bull; Non-Calculator (Q4-Q6)", 68, "6 Marks", chk3_p2))

    chk3_p3 = [
        ("7", 2, "A bar chart displays computer repair times: Mon (12), Tue (18), Wed (15), Thu (24). Which day had the most repairs, and what was the difference between Thu and Mon?", 52),
        ("8", 3, "A delivery company has 60 drivers. 42 drive electric vans and 18 drive diesel vans. What fraction of drivers drive diesel vans? Give your answer in simplest form (e.g. 1/something).", 60),
        ("9", 3, "A survey asks 50 employees if they travel by Bus or Train: 28 take the Bus, 15 take the Train, and 7 cycle. Complete a frequency table for this data and state the most common travel method.", 60)
    ]
    pages.append(checkpoint_page("Strand 3: Handling Information &amp; Data", "Part 2 &bull; Calculator Allowed (Q7-Q9)", 69, "8 Marks", chk3_p3))

    chk3_p4 = [
        ("10", 3, "In a warehouse raffle with 50 tickets, 45 tickets belong to depot staff and 5 belong to visitors. Use probability vocabulary to describe the likelihood of a depot worker winning.", 60),
        ("11", 3, "A two-way table shows shift choices: Morning shift has 24 full-time and 8 part-time staff. Afternoon shift has 16 full-time and 12 part-time staff. How many staff work in total?", 60),
        ("12", 4, "A company records quarterly customer compliments: Q1: 20, Q2: 35, Q3: 40, Q4: 25. Explain the steps to draw an accurate bar chart for this data including suitable scale intervals.", 70)
    ]
    pages.append(checkpoint_page("Strand 3: Handling Information &amp; Data", "Part 2 &bull; Calculator Allowed (Q10-Q12)", 70, "10 Marks", chk3_p4))

    # =========================================================================
    # PAGES 71 & 72: EXAM STRATEGY & REFERENCE FORMULAE
    # =========================================================================

    # PAGE 71: Exam Master Strategy
    p71 = f"""
    <h2>Entry Level 3 Exam Master Strategy &amp; Command Words</h2>
    <p>Essential examination tactics, time management rules, and command word definitions for Reformed Functional Skills Mathematics.</p>

    <div class="box-concept" style="border-left-color:var(--theme);">
      <h3 style="color:var(--theme); margin-top:0;">The Golden Rules of Entry 3 Exam Success</h3>
      <ul style="margin:4px 0 0 16px; padding:0; font-size:7.6pt;">
        <li><strong>Read the Question Twice:</strong> Underline the key numbers, the units requested, and the actual question asked.</li>
        <li><strong>Show Every Step of Working:</strong> You can gain <code>[P1]</code> Process and <code>[M1]</code> Method marks even if your final arithmetic has a small slip! A blank workspace gets 0 marks.</li>
        <li><strong>Always Write the Units:</strong> State &pound;, pence, cm, metres, kg, litres, or hours and minutes clearly.</li>
        <li><strong>Use Your Check Mark:</strong> When the paper asks you to 'Show a check', use the inverse operation or rounding. Never skip this free mark!</li>
        <li><strong>Keep an Eye on the Clock:</strong> Section A (Non-Calc) is 25 minutes. Section B (Calc) is 65 minutes. Do not get stuck on one question.</li>
      </ul>
    </div>

    {tutor_vignette("👨‍🏫", "Tutor Marcus", "Senior Maths Specialist", "On Section B, your calculator is your best friend—but always write down the sum you typed into the calculator! If you press the wrong button, the examiner can only give you marks for what is on paper!")}

    <h3>Ofqual Command Words Demystified</h3>
    <table class="cgp-table" style="font-size:7.4pt; margin:4px 0;">
      <thead>
        <tr><th>Command Word</th><th>What the Examiner Requires You to Do</th><th>Marking Implication</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Calculate / Work out</strong></td>
          <td>Perform the arithmetic operation (+, &minus;, &times;, &divide;) and give the numerical solution.</td>
          <td>Requires both method working and accurate final value.</td>
        </tr>
        <tr>
          <td><strong>Show a check</strong></td>
          <td>Use an inverse calculation (e.g. subtraction to check addition) or rounding to verify.</td>
          <td>Worth 1 explicit independent mark <code>[B1]</code>.</td>
        </tr>
        <tr>
          <td><strong>Compare</strong></td>
          <td>Look at two or more values, state which is larger/smaller, cheaper/more expensive.</td>
          <td>Must quote the actual numbers in your sentence!</td>
        </tr>
        <tr>
          <td><strong>State / Name</strong></td>
          <td>Give the exact name, label, direction, or term (e.g. <em>Cuboid</em>, <em>East</em>, <em>Likely</em>).</td>
          <td>Requires precise terminology; no calculation needed.</td>
        </tr>
      </tbody>
    </table>
    """
    pages.append(wrap_page(p71, 71, "Exam Master Strategy", "Assessment Skills", "Maths Entry Level 3 Core Guide"))

    # PAGE 72: Reference Guide & Key Conversions
    p72 = f"""
    <h2>Statutory Formula Sheet &amp; Conversions Reference</h2>
    <p>Key mathematical facts, measurement conversions, and equivalences required for Entry Level 3 Functional Skills Mathematics.</p>

    <div class="grid-2col" style="gap:8px; margin:4px 0;">
      <div>
        <div class="box-formula" style="margin-top:0;">
          <h3 style="color:#1e40af; margin-top:0; font-size:8pt;">Metric Length Conversions</h3>
          <ul style="margin:2px 0 0 14px; padding:0; font-size:7.4pt;">
            <li><strong>1 cm = 10 mm</strong></li>
            <li><strong>1 m = 100 cm</strong></li>
            <li><strong>1 km = 1,000 m</strong></li>
            <li>&frac12; m = 50 cm &bull; &frac14; m = 25 cm</li>
          </ul>
        </div>

        <div class="box-formula" style="border-left-color:#16a34a; background:#f0fdf4;">
          <h3 style="color:#15803d; margin-top:0; font-size:8pt;">Metric Mass &amp; Capacity</h3>
          <ul style="margin:2px 0 0 14px; padding:0; font-size:7.4pt;">
            <li><strong>1 kg = 1,000 g</strong> (&frac12; kg = 500g, &frac14; kg = 250g)</li>
            <li><strong>1 Litre = 1,000 ml</strong> (&frac12; L = 500ml, &frac14; L = 250ml)</li>
            <li>0.75 L = 750 ml &bull; 0.2 L = 200 ml</li>
          </ul>
        </div>
      </div>

      <div>
        <div class="box-formula" style="margin-top:0; border-left-color:#d97706; background:#fffbeb;">
          <h3 style="color:#b45309; margin-top:0; font-size:8pt;">Time &amp; Calendar Facts</h3>
          <ul style="margin:2px 0 0 14px; padding:0; font-size:7.4pt;">
            <li><strong>1 hour = 60 minutes</strong> (&frac12; h = 30m, &frac14; h = 15m)</li>
            <li><strong>1 day = 24 hours</strong></li>
            <li><strong>1 week = 7 days</strong> &bull; <strong>1 year = 52 weeks (365 days)</strong></li>
            <li>24h conversion: pm &rarr; add 12 (e.g. 4 pm = 16:00)</li>
          </ul>
        </div>

        <div class="box-formula" style="border-left-color:#9333ea; background:#faf5ff;">
          <h3 style="color:#7e22ce; margin-top:0; font-size:8pt;">Money &amp; Perimeter</h3>
          <ul style="margin:2px 0 0 14px; padding:0; font-size:7.4pt;">
            <li><strong>&pound;1 = 100 pence</strong></li>
            <li>Change = Money Paid &minus; Cost</li>
            <li><strong>Perimeter of Rectangle:</strong></li>
            <li><code>Perimeter = Length + Width + Length + Width</code></li>
          </ul>
        </div>
      </div>
    </div>

    <div class="box-concept" style="border-left-color:#2563eb; background:#eff6ff; margin-top:4px;">
      <h3 style="color:#1d4ed8; margin-top:0; font-size:8pt;">Fraction &amp; Decimal Equivalences Reference</h3>
      <table class="cgp-table" style="font-size:7.2pt; margin:2px 0;">
        <tr><th>Fraction</th><th>Words</th><th>Decimal Equivalent</th><th>Everyday Example</th></tr>
        <tr><td><strong>&frac12;</strong></td><td>One half</td><td>0.5</td><td>50p of &pound;1.00 &bull; 500g of 1kg</td></tr>
        <tr><td><strong>&frac14;</strong></td><td>One quarter</td><td>0.25</td><td>25p of &pound;1.00 &bull; 250ml of 1 Litre</td></tr>
        <tr><td><strong>&frac34;</strong></td><td>Three quarters</td><td>0.75</td><td>75p of &pound;1.00 &bull; 750m of 1 km</td></tr>
        <tr><td><strong>1/10</strong></td><td>One tenth</td><td>0.1</td><td>10p of &pound;1.00 &bull; 100g of 1 kg</td></tr>
      </table>
    </div>
    """
    pages.append(wrap_page(p72, 72, "Statutory Formula Sheet", "Reference Guide", "Maths Entry Level 3 Core Guide"))

    # =========================================================================
    # PAGES 73 TO 78: FULL REALISTIC MOCK EXAMINATION PAPER (42 Marks)
    # =========================================================================

    # Mock Exam Section A: Non-Calculator (Pages 73 & 74, 12 Marks, 25 Mins)
    mock_p73 = [
        ("1", 2, "Calculate: <strong>487 + 265</strong> using formal column addition.", 55, "Final Answer"),
        ("2", 2, "Calculate: <strong>632 &minus; 268</strong> using column subtraction, and write down an addition check.", 55, "Calculation &amp; Check"),
        ("3", 2, "A team has 36 members. <strong>&frac34;</strong> of the team attend a health and safety briefing. How many members attend the briefing?", 55, "Attending Members")
    ]
    pages.append(mock_page("Section A: Non-Calculator", 73, mock_p73))

    mock_p74 = [
        ("4", 2, "A customer buys a sandwich for &pound;3.45 and a coffee for &pound;2.80. She pays with a &pound;10 note. How much change does she receive?", 55, "Change Received"),
        ("5", 2, "A bus journey starts at 08:35 and arrives at 09:20. How many minutes did the journey take?", 55, "Journey Duration"),
        ("6", 2, "A rectangular storeroom measures 8 metres long and 5 metres wide. Calculate the perimeter of the storeroom in metres.", 55, "Perimeter")
    ]
    pages.append(mock_page("Section A: Non-Calculator", 74, mock_p74))

    # Mock Exam Section B: Calculator Allowed (Pages 75 to 78, 30 Marks, 65 Mins)
    mock_p75 = [
        ("7", 3, "A company orders 8 office chairs at &pound;45 each and a desk for &pound;185. What is the total cost of the order?", 55, "Total Cost"),
        ("8", 2, "A night shift begins at 21:30 and finishes at 06:00 the next morning. How many hours and minutes does the shift last?", 55, "Shift Duration"),
        ("9", 2, "A factory packs 92 mugs into gift boxes. Each box holds 6 mugs. How many full boxes can be packed, and how many mugs are left over?", 55, "Full Boxes &amp; Leftovers")
    ]
    pages.append(mock_page("Section B: Calculator Allowed", 75, mock_p75))

    mock_p76 = [
        ("10", 3, "A chef needs 1.5 kg of flour. He has three bags containing 450g, 550g, and 350g. Does he have enough flour in total? Show calculations to justify your answer.", 55, "Evaluation &amp; Working"),
        ("11", 2, "A bottle of liquid medicine contains 300 ml. A patient takes a 15 ml dose three times a day. How many days will the bottle last?", 55, "Number of Days"),
        ("12", 2, "At 06:00, the temperature in a cold storage unit was &minus;15&deg;C. By 14:00, the temperature had risen by 8&deg;C. What was the temperature at 14:00?", 55, "Temperature at 14:00")
    ]
    pages.append(mock_page("Section B: Calculator Allowed", 76, mock_p76))

    mock_p77 = [
        ("13", 3, "A pictogram records bicycle rentals where each &starf; represents 8 bicycles.<br>Monday has 3 full stars.<br>Tuesday has 2 and a half stars.<br>How many bicycles were rented in total over the two days?", 55, "Total Bicycles"),
        ("14", 2, "A delivery drone travels North from depot A to depot B, then turns 90&deg; clockwise. Which compass direction is the drone now travelling?", 55, "Compass Direction"),
        ("15", 3, "A bar chart shows staff absences across four quarters: Q1: 15, Q2: 25, Q3: 10, Q4: 30. What was the total number of absences for the whole year, and what is the difference between Q4 and Q3?", 55, "Total &amp; Difference")
    ]
    pages.append(mock_page("Section B: Calculator Allowed", 77, mock_p77))

    mock_p78 = [
        ("16", 2, "A survey of 40 apprentices records commute method: 18 travel by Train, 14 by Bus, and the rest Walk. How many apprentices walk to work?", 55, "Walking Apprentices"),
        ("17", 2, "A raffle ticket box holds 95 white tickets and 5 gold tickets. A ticket is picked at random. State the probability term that best describes the chance of picking a gold ticket.", 55, "Probability Term"),
        ("18", 4, "A landscape gardener lays turf for a lawn measuring 9 metres long by 6 metres wide. Turf rolls cost &pound;6 per metre of perimeter fence. The customer has a budget of &pound;200. Is the budget sufficient to fence the lawn perimeter? Show complete working and conclusion.", 65, "Budget Sufficiency &amp; Conclusion")
    ]
    pages.append(mock_page("Section B: Calculator Allowed", 78, mock_p78))

    # =========================================================================
    # PAGES 79 TO 82: COMPREHENSIVE ANSWER KEYS & FORMAL MARK SCHEMES
    # =========================================================================

    # PAGE 79: Strand 1 & Strand 2 Checkpoint Solutions
    t79 = """
    <div class="box-concept" style="padding:5px 8px; margin-bottom:5px;">
      <h3 style="margin:0 0 2px 0; color:var(--theme); font-size:8pt;">Strand 1 Checkpoint Solutions (Pages 23–26)</h3>
      <div style="font-size:7.2pt; line-height:1.35;">
        <strong>Q1:</strong> Seven hundred and forty-nine [1m]; 4 represents 4 tens or 40 [1m].<br>
        <strong>Q2:</strong> 406, 460, 604, 640 [2m].<br>
        <strong>Q3:</strong> a) 370 [1m]; b) 400 [1m].<br>
        <strong>Q4:</strong> 385 + 247: Units 5+7=12 (carry 1); Tens 8+4+1=13 (carry 1); Hundreds 3+2+1=6 &rarr; 632 [2m].<br>
        <strong>Q5:</strong> 624 &minus; 278: Exchanging across tens and hundreds gives 346 [2m].<br>
        <strong>Q6:</strong> 72 &divide; 4 = 18 [1m]; Check: 18 &times; 4 = 72 [1m].<br>
        <strong>Q7:</strong> 8 &times; 26 = 208 lightbulbs [2m].<br>
        <strong>Q8:</strong> 94 &divide; 8 = 11 remainder 6 &rarr; 11 full baskets [2m]; 6 rolls left over [1m].<br>
        <strong>Q9:</strong> 80 &divide; 4 = 20 [1m]; 20 &times; 3 = 60 parcels [2m].<br>
        <strong>Q10:</strong> 485 &divide; 50 = 9.7 &rarr; must round up to 10 full packs [3m].<br>
        <strong>Q11:</strong> &pound;185 + &pound;95 = &pound;280 [1m]; &pound;750 &minus; &pound;280 = &pound;470 [2m].<br>
        <strong>Q12:</strong> &frac23; of 60 = 40 [2m]; &frac15; of 60 = 12 [1m]; 40 + 12 = 52 places booked [1m].
      </div>
    </div>

    <div class="box-formula" style="padding:5px 8px; border-left-color:var(--accent);">
      <h3 style="margin:0 0 2px 0; color:#b45309; font-size:8pt;">Strand 2 Checkpoint Solutions (Pages 47–50)</h3>
      <div style="font-size:7.2pt; line-height:1.35;">
        <strong>Q1:</strong> &pound;3.65 + &pound;1.80 = &pound;5.45 [2m].<br>
        <strong>Q2:</strong> &pound;10.00 &minus; &pound;6.35 = &pound;3.65 change [2m].<br>
        <strong>Q3:</strong> a) 08:20 [1m]; b) 16:45 [1m].<br>
        <strong>Q4:</strong> 15:45 (3:45 pm + 12 hours) [2m].<br>
        <strong>Q5:</strong> a) 40 mm [1m]; b) 300 cm [1m]; c) 2 kg [1m].<br>
        <strong>Q6:</strong> 7 + 4 + 7 + 4 = 22 metres [2m].<br>
        <strong>Q7:</strong> 08:35 to 09:00 = 25m; 09:00 to 10:15 = 1h 15m &rarr; 1 hour 40 minutes [2m].<br>
        <strong>Q8:</strong> &minus;19&deg;C + 5&deg;C = &minus;14&deg;C [3m].<br>
        <strong>Q9:</strong> Perimeter = 6 + 5 + 6 + 5 = 22 m [1m]; 22 &times; &pound;2.50 = &pound;55.00 [2m].<br>
        <strong>Q10:</strong> 500 &divide; 45 = 11.11 &rarr; 11 full cleaning tasks [3m].<br>
        <strong>Q11:</strong> Cube [1m]; 4 lines of symmetry on a square face [2m].<br>
        <strong>Q12:</strong> 45 &times; 40 ml = 1,800 ml [2m]; 1,800 &divide; 1,000 = 1.8 litres [2m].
      </div>
    </div>
    """
    pages.append(mark_scheme_page("Answer Keys & Formal Mark Schemes", "Strands 1 &amp; 2 Checkpoint Solutions", 79, t79))

    # PAGE 80: Strand 3 Checkpoint & Drill Solutions
    t80 = """
    <div class="box-concept" style="padding:5px 8px; margin-bottom:5px;">
      <h3 style="margin:0 0 2px 0; color:var(--theme); font-size:8pt;">Strand 3 Checkpoint Solutions (Pages 67–70)</h3>
      <div style="font-size:7.2pt; line-height:1.35;">
        <strong>Q1:</strong> North, East, South, West [2m].<br>
        <strong>Q2:</strong> North (quarter turn clockwise from West points North) [2m].<br>
        <strong>Q3:</strong> First Aid (Y=5 is higher than Y=2) [2m].<br>
        <strong>Q4:</strong> 17 parcels [2m].<br>
        <strong>Q5:</strong> 3.5 &times; 4 = 14 delivery vans [2m].<br>
        <strong>Q6:</strong> Even Chance (3 odd numbers out of 6 on a dice: 1, 3, 5) [2m].<br>
        <strong>Q7:</strong> Thursday with 24 repairs [1m]; Difference: 24 &minus; 12 = 12 repairs [1m].<br>
        <strong>Q8:</strong> 18 out of 60 = 18/60 = 3/10 (or 0.3) [3m].<br>
        <strong>Q9:</strong> Bus: 28, Train: 15, Cycle: 7 [2m]; Most common: Bus [1m].<br>
        <strong>Q10:</strong> Likely (45 out of 50 tickets belong to depot staff) [3m].<br>
        <strong>Q11:</strong> Morning: 24+8=32; Afternoon: 16+12=28; Total = 32 + 28 = 60 staff [3m].<br>
        <strong>Q12:</strong> State: 1. Title; 2. Axes labelled (Quarter / Compliments); 3. Even scale in 5s (0 to 45); 4. Accurate bar heights with equal gaps [4m].
      </div>
    </div>

    <div class="box-tip" style="padding:5px 8px; border-left-color:#16a34a; background:#f0fdf4;">
      <h3 style="margin:0 0 2px 0; color:#15803d; font-size:8pt;">Guided Practice Drills Answer Key Summary</h3>
      <div style="font-size:7.2pt; line-height:1.35;">
        &bull; <strong>Unit 1 (p4):</strong> Ex A: Six hundred and eighty-two, 600+80+2. Ex B: a) 700 b) 70 c) 7. Ex C: 546.<br>
        &bull; <strong>Unit 3 (p8):</strong> Ex A: a) 60 b) 140 c) 880. Ex B: a) 400 b) 700 c) 700. Ex C: 500 crates.<br>
        &bull; <strong>Unit 5 (p12):</strong> Ex A: a) 398 b) 723 c) 903. Ex B: 446 miles. Ex C: &pound;463.<br>
        &bull; <strong>Unit 7 (p16):</strong> Ex A: a) 28 b) 48 c) 27 d) 64. Ex B: a) 140 b) 312. Ex C: 72 tyres.<br>
        &bull; <strong>Unit 10 (p22):</strong> Ex A: a) &pound;30 b) 8 kg c) 9 L. Ex B: a) 20 m b) &pound;30. Ex C: 24 damaged, 96 undamaged.<br>
        &bull; <strong>Unit 12 (p30):</strong> Ex A: &pound;3.55 change. Ex B: &pound;2.80&times;2 + &pound;3.15 = &pound;8.75; Change = &pound;11.25. Ex C: Store A (&pound;6.00 vs &pound;6.75, saves 75p).<br>
        &bull; <strong>Unit 15 (p36):</strong> Ex A: a) 1h 30m b) 1h 30m. Ex B: 20:40. Ex C: 8h 00m.<br>
        &bull; <strong>Unit 19 (p44):</strong> Ex A: a) 28 cm b) 26 m. Ex B: 400 cm. Ex C: 32 m &times; &pound;4 = &pound;128.
      </div>
    </div>
    """
    pages.append(mark_scheme_page("Answer Keys & Formal Mark Schemes", "Strand 3 &amp; Guided Drills Solutions", 80, t80))

    # PAGE 81: Mock Exam Mark Scheme - Section A (Non-Calculator)
    t81 = """
    <table class="cgp-table" style="font-size:7.4pt; margin:4px 0;">
      <thead>
        <tr><th style="width:8%;">Q</th><th style="width:40%;">Process &amp; Method Breakdown</th><th style="width:12%;">Mark</th><th style="width:40%;">Guidance &amp; Marking Code</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>1</strong></td>
          <td>487 + 265:<br>Units: 7+5=12; Tens: 8+6+1=15; Hundreds: 4+2+1=7 &rarr; <strong>752</strong></td>
          <td><code>[M1]<br>[A1]</code></td>
          <td><code>[M1]</code> for correct column alignment and carrying.<br><code>[A1]</code> for correct total 752.</td>
        </tr>
        <tr>
          <td><strong>2</strong></td>
          <td>632 &minus; 268 = <strong>364</strong><br>Check: 364 + 268 = 632 (or 632 &minus; 364 = 268)</td>
          <td><code>[M1]<br>[B1]</code></td>
          <td><code>[M1]</code> for correct subtraction with exchange.<br><code>[B1]</code> for valid inverse addition check.</td>
        </tr>
        <tr>
          <td><strong>3</strong></td>
          <td>36 &divide; 4 = 9<br>9 &times; 3 = <strong>27 members</strong></td>
          <td><code>[M1]<br>[A1]</code></td>
          <td><code>[M1]</code> for dividing by 4 or multiplying by 3/4.<br><code>[A1]</code> for 27.</td>
        </tr>
        <tr>
          <td><strong>4</strong></td>
          <td>Total cost: &pound;3.45 + &pound;2.80 = &pound;6.25<br>Change: &pound;10.00 &minus; &pound;6.25 = <strong>&pound;3.75</strong></td>
          <td><code>[P1]<br>[A1]</code></td>
          <td><code>[P1]</code> for finding total cost or subtracting from 10.<br><code>[A1]</code> for &pound;3.75 (accept 375p with unit).</td>
        </tr>
        <tr>
          <td><strong>5</strong></td>
          <td>08:35 to 09:00 = 25 minutes<br>09:00 to 09:20 = 20 minutes &rarr; 25 + 20 = <strong>45 minutes</strong></td>
          <td><code>[M1]<br>[A1]</code></td>
          <td><code>[M1]</code> for bridging hour or subtracting.<br><code>[A1]</code> for 45 minutes.</td>
        </tr>
        <tr>
          <td><strong>6</strong></td>
          <td>Perimeter = 8 + 5 + 8 + 5 (or 2 &times; 13) = <strong>26 metres</strong></td>
          <td><code>[M1]<br>[A1]</code></td>
          <td><code>[M1]</code> for summing all 4 sides.<br><code>[A1]</code> for 26 (with m or metres).</td>
        </tr>
      </tbody>
    </table>

    <div class="box-exam-tip" style="margin-top:6px;">
      <strong>Section A Score Interpretation:</strong><br>
      Section A total is <strong>12 marks</strong>. Target score for a comfortable pass is <strong>8 out of 12 (67%)</strong>. If you scored less than 8, review column arithmetic and money calculations in Units 5, 6, and 11.
    </div>
    """
    pages.append(mark_scheme_page("Official Mock Exam Mark Scheme", "Section A &bull; Non-Calculator (12 Marks)", 81, t81))

    # PAGE 82: Mock Exam Mark Scheme - Section B (Calculator Allowed)
    t82 = """
    <table class="cgp-table" style="font-size:7.2pt; margin:3px 0;">
      <thead>
        <tr><th style="width:7%;">Q</th><th style="width:42%;">Process &amp; Method Breakdown</th><th style="width:11%;">Mark</th><th style="width:40%;">Guidance &amp; Marking Code</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>7</strong></td>
          <td>8 &times; &pound;45 = &pound;360<br>&pound;360 + &pound;185 = <strong>&pound;545</strong></td>
          <td><code>[P1]<br>[M1]<br>[A1]</code></td>
          <td><code>[P1]</code> for 8 &times; 45; <code>[M1]</code> for adding 185; <code>[A1]</code> for &pound;545.</td>
        </tr>
        <tr>
          <td><strong>8</strong></td>
          <td>21:30 to 22:00 = 30m; 22:00 to 06:00 = 8h &rarr; <strong>8h 30m</strong></td>
          <td><code>[M1][A1]</code></td>
          <td><code>[M1]</code> for bridging across midnight; <code>[A1]</code> for 8 hours 30 mins.</td>
        </tr>
        <tr>
          <td><strong>9</strong></td>
          <td>92 &divide; 6 = 15.33 &rarr; <strong>15 full boxes</strong> and <strong>2 mugs leftover</strong></td>
          <td><code>[M1][A1]</code></td>
          <td><code>[M1]</code> for 92 &divide; 6; <code>[A1]</code> for 15 boxes and 2 remainder.</td>
        </tr>
        <tr>
          <td><strong>10</strong></td>
          <td>450 + 550 + 350 = 1,350g<br>1.5 kg = 1,500g &rarr; 1,350 &lt; 1,500 &rarr; <strong>No, needs 150g more</strong></td>
          <td><code>[P1]<br>[M1]<br>[A1]</code></td>
          <td><code>[P1]</code> for summing grams; <code>[M1]</code> for unit conversion; <code>[A1]</code> for 'No' with correct comparison.</td>
        </tr>
        <tr>
          <td><strong>11</strong></td>
          <td>Daily intake: 3 &times; 15 ml = 45 ml<br>300 &divide; 45 = 6.66 &rarr; <strong>6 full days</strong></td>
          <td><code>[M1][A1]</code></td>
          <td><code>[M1]</code> for 300 &divide; 45; <code>[A1]</code> for 6 days (7th day incomplete).</td>
        </tr>
        <tr>
          <td><strong>12</strong></td>
          <td>&minus;15 + 8 = <strong>&minus;7&deg;C</strong></td>
          <td><code>[M1][A1]</code></td>
          <td><code>[M1]</code> for adding 8 to &minus;15; <code>[A1]</code> for &minus;7&deg;C.</td>
        </tr>
        <tr>
          <td><strong>13</strong></td>
          <td>Mon: 3 &times; 8 = 24 &bull; Tue: 2.5 &times; 8 = 20 &rarr; 24 + 20 = <strong>44 bicycles</strong></td>
          <td><code>[P1][M1][A1]</code></td>
          <td><code>[P1]</code> for key multiplication; <code>[M1]</code> for adding days; <code>[A1]</code> for 44.</td>
        </tr>
        <tr>
          <td><strong>14</strong></td>
          <td>Facing North; 90&deg; clockwise turn &rarr; <strong>East</strong></td>
          <td><code>[M1][A1]</code></td>
          <td><code>[M1]</code> for understanding 90&deg; clockwise; <code>[A1]</code> for East.</td>
        </tr>
        <tr>
          <td><strong>15</strong></td>
          <td>Total: 15+25+10+30 = <strong>80</strong><br>Difference: 30 &minus; 10 = <strong>20</strong></td>
          <td><code>[P1]<br>[M1]<br>[A1]</code></td>
          <td><code>[P1]</code> for sum of 4 quarters; <code>[M1]</code> for subtraction; <code>[A1]</code> for 80 and 20.</td>
        </tr>
        <tr>
          <td><strong>16</strong></td>
          <td>18 + 14 = 32 &rarr; 40 &minus; 32 = <strong>8 apprentices</strong></td>
          <td><code>[M1][A1]</code></td>
          <td><code>[M1]</code> for subtracting sum from 40; <code>[A1]</code> for 8.</td>
        </tr>
        <tr>
          <td><strong>17</strong></td>
          <td>5 out of 100 tickets &rarr; <strong>Unlikely</strong></td>
          <td><code>[M1][A1]</code></td>
          <td><code>[M1]</code> for recognising low fraction; <code>[A1]</code> for 'Unlikely'.</td>
        </tr>
        <tr>
          <td><strong>18</strong></td>
          <td>Perimeter = 9+6+9+6 = 30 m<br>Cost: 30 &times; &pound;6 = &pound;180<br>&pound;180 &lt; &pound;200 &rarr; <strong>Yes, budget is sufficient (&pound;20 under)</strong></td>
          <td><code>[P1]<br>[M1]<br>[M1]<br>[A1]</code></td>
          <td><code>[P1]</code> for perimeter (30m); <code>[M1]</code> for cost (30 &times; 6); <code>[M1]</code> for &pound;180; <code>[A1]</code> for 'Yes' with correct justification.</td>
        </tr>
      </tbody>
    </table>

    <div class="box-concept" style="margin-top:4px; padding:4px 8px; border-left-color:var(--theme); background:#fff1f2;">
      <strong style="color:var(--theme); font-size:7.5pt;">Overall Mock Exam Pass Mark Guidance:</strong><br>
      <span style="font-size:7.2pt;">Total Exam Marks: <strong>42 Marks</strong> (Section A: 12 Marks + Section B: 30 Marks). The official pass mark standard is typically <strong>28 out of 42 (approx. 66%)</strong>. If you achieved 29 marks or higher across both sections, you are performing at full examination pass level!</span>
    </div>
    """
    pages.append(mark_scheme_page("Official Mock Exam Mark Scheme", "Section B &bull; Calculator Allowed (30 Marks)", 82, t82))

    # PAGE 83: Glossary & Quick Index
    p83 = f"""
    <h2>Entry Level 3 Mathematical Glossary &amp; Quick Index</h2>
    <p>Statutory mathematical terms, definitions, and page reference guide for rapid revision.</p>

    <div class="grid-2col" style="gap:8px; margin:4px 0;">
      <div class="box-concept" style="font-size:7.4pt; margin-top:0;">
        <h3 style="margin-top:0; color:var(--theme); font-size:8pt;">Index of Mathematical Terms</h3>
        <strong>Analogue Clock:</strong> Dial with moving hands (p.31)<br>
        <strong>Capacity:</strong> Amount of liquid held in ml or litres (p.39)<br>
        <strong>Carroll Diagram:</strong> 2&times;2 grid sorting data by criteria (p.63)<br>
        <strong>Compass Points:</strong> North, East, South, West directions (p.51)<br>
        <strong>Denominator:</strong> Bottom number of a fraction (p.21)<br>
        <strong>Even Number:</strong> Integer ending in 0, 2, 4, 6, 8 (p.9)<br>
        <strong>Frequency:</strong> Total number of occurrences (p.55)<br>
        <strong>Grid Method:</strong> Partitioning method for multiplication (p.15)<br>
        <strong>Inverse:</strong> Opposite mathematical operation (p.19)<br>
        <strong>Numerator:</strong> Top number of a fraction (p.21)<br>
        <strong>Odd Number:</strong> Integer ending in 1, 3, 5, 7, 9 (p.9)<br>
        <strong>Perimeter:</strong> Total distance around boundary of shape (p.43)
      </div>

      <div class="box-formula" style="font-size:7.4pt; margin-top:0;">
        <h3 style="margin-top:0; color:#1e40af; font-size:8pt;">Curriculum Unit Index</h3>
        &bull; <strong>Unit 1:</strong> Place Value to 1,000 (p.3)<br>
        &bull; <strong>Unit 3:</strong> Rounding to 10 &amp; 100 (p.7)<br>
        &bull; <strong>Unit 5:</strong> Column Addition (p.11)<br>
        &bull; <strong>Unit 6:</strong> Column Subtraction (p.13)<br>
        &bull; <strong>Unit 7:</strong> Multiplication Facts (p.15)<br>
        &bull; <strong>Unit 8:</strong> Division &amp; Remainders (p.17)<br>
        &bull; <strong>Unit 10:</strong> Fractions of Amounts (p.21)<br>
        &bull; <strong>Unit 11:</strong> Decimal Money (p.27)<br>
        &bull; <strong>Unit 14:</strong> 24-Hour Timetables (p.33)<br>
        &bull; <strong>Unit 16:</strong> Metric Length mm/cm/m (p.37)<br>
        &bull; <strong>Unit 19:</strong> Perimeter (p.43)<br>
        &bull; <strong>Unit 20:</strong> 2D/3D Shapes (p.45)<br>
        &bull; <strong>Unit 24:</strong> Pictograms &amp; Keys (p.57)<br>
        &bull; <strong>Unit 25:</strong> Bar Charts (p.59)<br>
        &bull; <strong>Unit 28:</strong> Probability (p.65)
      </div>
    </div>

    {tutor_vignette("👨‍🏫", "Tutor Marcus", "Senior Maths Specialist", "Congratulations on completing the entire Entry Level 3 Core Guide! You are now fully equipped with the skills and confidence to achieve your Functional Skills qualification and advance to Level 1.")}
    """
    pages.append(wrap_page(p83, 83, "Entry 3 Glossary &amp; Index", "Reference Section", "Maths Entry Level 3 Core Guide"))

    # PAGE 84: Back Cover
    pages.append(f"""
    <div class="page cover-full-page">
      <img src="file://{back_img}" class="cover-full-img" alt="Entry Level 3 Core Guide Back Cover">
    </div>
    """)

    print(f"Total HTML pages assembled: {len(pages)}")

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Master Functional Skills - Maths Entry Level 3 Core Guide</title>
{get_shared_css(theme_color="#991b1b", accent_color="#f59e0b", light_bg="#fff1f2")}
</head>
<body>
{''.join(pages)}
</body>
</html>
"""

    html_file = os.path.join(SCRATCH_DIR, "maths_e3_core_84p.html")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"Building {out_name} via Chromium headless...")
    cmd = [
        CHROME_BIN,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--no-pdf-header-footer",
        f"--print-to-pdf={target_downloads}",
        html_file
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Chromium error: {res.stderr}")
        return False

    shutil.copy2(target_downloads, target_documents)
    print(f"Copied to {target_documents}")

    info_cmd = ["pdfinfo", target_downloads]
    info_res = subprocess.run(info_cmd, capture_output=True, text=True)
    for line in info_res.stdout.splitlines():
        if "Pages:" in line:
            print(f"Entry Level 3 Core Guide PDF Result: {line}")

    return True

if __name__ == "__main__":
    build_e3_core_guide()
