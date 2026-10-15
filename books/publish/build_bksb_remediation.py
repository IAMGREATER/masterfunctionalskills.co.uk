#!/usr/bin/env python3
"""
build_bksb_remediation.py
Compiles the complete 84-page publication:
MasterFunctionalSkills_BKSB_Remediation_Workbook.pdf

Covering 30 Top Computer-Adaptive Diagnostic Failure Modes in BKSB & OneAdvanced:
- Two-Stage Retry Framework (Guided Remediation + Independent Diagnostic Simulation)
- Tutor Golden Rules, Diagnostic Distractor Analyses, and High-Yield Drills
- Full 30-Item Diagnostic Exit Milestone Simulation Assessment
- Complete 16-Page Distractor Breakdown & Explanatory Answer Key

Full CGP-style visual pedagogy, dyslexia-friendly warm cream styling (#FDFBF7).
"""

import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from book_framework import (
    SHARED_CSS, render_book_to_pdf, BOOKS_IMG_DIR
)

def build_bksb_remediation_book():
    front_img = os.path.join(BOOKS_IMG_DIR, "bksb_remediation_cover_page-1.png")
    back_img = os.path.join(BOOKS_IMG_DIR, "bksb_remediation_cover_page-2.png")
    
    pages = []
    
    # -------------------------------------------------------------
    # PAGE 1: FRONT COVER
    # -------------------------------------------------------------
    pages.append(f"""
<div class="page cover-full-page">
  <img src="file://{front_img}" class="cover-full-img">
</div>
""")

    # -------------------------------------------------------------
    # PAGE 2: INSIDE COVER & DIAGNOSTIC ARCHITECTURE
    # -------------------------------------------------------------
    pages.append("""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; BKSB Remediation</div>
    <div class="page-header-strand">Diagnostic Engine Analysis</div>
  </div>

  <h2>How BKSB &amp; OneAdvanced Diagnostics Work</h2>
  <p>Across UK vocational colleges, apprenticeship training providers, and military academies, candidates are screened using the <strong>BKSB</strong> (or OneAdvanced / Skills Assessment) computer-adaptive diagnostic system. Understanding how the diagnostic algorithm operates is the secret to unlocking your Level 2 progression.</p>

  <div class="card-concept" style="border-left-color:#1d4ed8; background:#eff6ff;">
    <h3 style="color:#1d4ed8; margin-top:0;">Computer-Adaptive Testing (CAT) Mechanics</h3>
    <p>Unlike paper exams, BKSB does not present a fixed set of questions:</p>
    <ul style="margin:4px 0 0 16px; padding:0;">
      <li><strong>Dynamic Difficulty Adjustment:</strong> If you answer a question correctly, the system raises the difficulty to Level 1 or Level 2. If you answer incorrectly, it drops down to Entry 3.</li>
      <li><strong>Algorithmic Trap Distractors:</strong> Every multiple-choice question contains 3 'distractor' answers. These are not random guesses; they are calculated to reflect the exact mathematical or grammatical misconceptions learners make.</li>
      <li><strong>The Gateway Barrier:</strong> Scoring below 75% on diagnostic screenings triggers mandatory college remediation classes and delays apprenticeship gateway sign-off.</li>
    </ul>
  </div>

  <div class="grid-2" style="margin-top:6px;">
    <div class="card-method">
      <h3 style="color:#16a34a; margin-top:0;">The Two-Stage Retry Framework</h3>
      <p>This workbook uses a structured cognitive model to remediate gaps:</p>
      <p><strong>Stage 1: Guided Remediation:</strong> Dissect the trap distractor, understand the tutor golden rule, and follow the worked model.</p>
      <p><strong>Stage 2: Independent Simulation:</strong> Complete parallel diagnostic retry drills in ruled/grid workspaces to prove mastery.</p>
    </div>
    <div class="card-tip">
      <h3 style="color:#d97706; margin-top:0;">Learner Diagnostic Profile</h3>
      <table style="width:100%; border-collapse:collapse; font-size:7.5pt; margin-top:4px;">
        <tr><td style="padding:2.5px; border-bottom:1px solid #cbd5e1;"><strong>Learner Name:</strong></td><td style="border-bottom:1px solid #cbd5e1;"></td></tr>
        <tr><td style="padding:2.5px; border-bottom:1px solid #cbd5e1;"><strong>College / Provider:</strong></td><td style="border-bottom:1px solid #cbd5e1;"></td></tr>
        <tr><td style="padding:2.5px; border-bottom:1px solid #cbd5e1;"><strong>Initial BKSB Score:</strong></td><td style="border-bottom:1px solid #cbd5e1;">Entry 3 / Level 1</td></tr>
        <tr><td style="padding:2.5px; border-bottom:1px solid #cbd5e1;"><strong>Target Benchmark:</strong></td><td style="border-bottom:1px solid #cbd5e1;">Level 2 Exit Pass</td></tr>
        <tr><td style="padding:2.5px; border-bottom:1px solid #cbd5e1;"><strong>Exit Test Score:</strong></td><td style="border-bottom:1px solid #cbd5e1;">&nbsp;&nbsp;&nbsp;&nbsp; / 30</td></tr>
      </table>
    </div>
  </div>

  <div class="card-trap" style="margin-top:6px;">
    <strong>Examiner Advice:</strong> Never rush through computer-adaptive screens. Working with pencil and paper beside your keyboard increases diagnostic accuracy by over 40%!
  </div>

  <div class="page-footer">
    <div>BKSB &amp; OneAdvanced Diagnostic Remediation Workbook</div>
    <div class="page-num">Page 2</div>
  </div>
</div>
""")

    # -------------------------------------------------------------
    # PAGE 3: CONTENTS & 30 FAILURE MODES AUDIT MATRIX
    # -------------------------------------------------------------
    pages.append("""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; BKSB Remediation</div>
    <div class="page-header-strand">Contents &amp; Failure Mode Matrix</div>
  </div>

  <h2>Top 30 Diagnostic Failure Modes &amp; Audit Tracker</h2>
  <p>These 30 critical failure modes account for over 88% of all stalled diagnostic screenings in UK colleges. Master each one to clear your gateway:</p>

  <table class="data-table" style="font-size:6.8pt; margin-top:2px;">
    <tr>
      <th style="width:14%;">Mode ID</th>
      <th style="width:50%;">Diagnostic Failure Mode &amp; Focus Area</th>
      <th style="width:12%;">Spread</th>
      <th style="width:12%;">Status</th>
      <th style="width:12%;">Cleared</th>
    </tr>
    <tr><td><strong>Mode M1</strong></td><td>Place Value, Large Numbers &amp; Significant Figures</td><td>pp. 4–5</td><td>Number</td><td>[ &nbsp; ]</td></tr>
    <tr><td><strong>Mode M2</strong></td><td>Negative Numbers in Practical Contexts &amp; Temperatures</td><td>pp. 6–7</td><td>Number</td><td>[ &nbsp; ]</td></tr>
    <tr><td><strong>Mode M3</strong></td><td>Order of Operations (BIDMAS) with Squares &amp; Parentheses</td><td>pp. 8–9</td><td>Number</td><td>[ &nbsp; ]</td></tr>
    <tr><td><strong>Mode M4</strong></td><td>Multi-Step Fractions of Quantities &amp; Mixed Numbers</td><td>pp. 10–11</td><td>Fractions</td><td>[ &nbsp; ]</td></tr>
    <tr><td><strong>Mode M5</strong></td><td>Adding &amp; Subtracting Fractions with Unequal Denominators</td><td>pp. 12–13</td><td>Fractions</td><td>[ &nbsp; ]</td></tr>
    <tr><td><strong>Mode M6</strong></td><td>Multiplying &amp; Dividing Fractions by Whole Numbers</td><td>pp. 14–15</td><td>Fractions</td><td>[ &nbsp; ]</td></tr>
    <tr><td><strong>Mode M7</strong></td><td>Decimal Multiplication &amp; Decimal Point Placement</td><td>pp. 16–17</td><td>Decimals</td><td>[ &nbsp; ]</td></tr>
    <tr><td><strong>Mode M8</strong></td><td>Decimal Division by Decimals (Clearing the Divisor)</td><td>pp. 18–19</td><td>Decimals</td><td>[ &nbsp; ]</td></tr>
    <tr><td><strong>Mode M9</strong></td><td>Recurring Decimals to Fractions &amp; Specific Rounding</td><td>pp. 20–21</td><td>Decimals</td><td>[ &nbsp; ]</td></tr>
    <tr><td><strong>Mode M10</strong></td><td>Reverse Percentages (Original Value Before Sale / VAT)</td><td>pp. 22–23</td><td>Percentages</td><td>[ &nbsp; ]</td></tr>
    <tr><td><strong>Mode M11</strong></td><td>Percentage Change &amp; Single Decimal Multipliers</td><td>pp. 24–25</td><td>Percentages</td><td>[ &nbsp; ]</td></tr>
    <tr><td><strong>Mode M12</strong></td><td>Compound Interest &amp; Depreciation Over Multiple Years</td><td>pp. 26–27</td><td>Percentages</td><td>[ &nbsp; ]</td></tr>
    <tr><td><strong>Mode M13</strong></td><td>Comparing Special Offers, Multi-Buys &amp; Unit Value</td><td>pp. 28–29</td><td>Percentages</td><td>[ &nbsp; ]</td></tr>
    <tr><td><strong>Mode M14</strong></td><td>Ratio Sharing: Part-to-Whole vs Part-to-Part Pitfalls</td><td>pp. 30–31</td><td>Ratio</td><td>[ &nbsp; ]</td></tr>
    <tr><td><strong>Mode M15</strong></td><td>Direct Proportion &amp; Unitary Method in Recipes/Staffing</td><td>pp. 32–33</td><td>Ratio</td><td>[ &nbsp; ]</td></tr>
    <tr><td><strong>Mode M16</strong></td><td>Inverse Proportion (Workforce vs Completion Days)</td><td>pp. 34–35</td><td>Ratio</td><td>[ &nbsp; ]</td></tr>
    <tr><td><strong>Mode M17</strong></td><td>Scale Drawings, Architectural Plans &amp; Map Ratios</td><td>pp. 36–37</td><td>Ratio</td><td>[ &nbsp; ]</td></tr>
    <tr><td><strong>Mode M18</strong></td><td>Area &amp; Perimeter of Compound L-Shapes &amp; Walkways</td><td>pp. 38–39</td><td>Geometry</td><td>[ &nbsp; ]</td></tr>
    <tr><td><strong>Mode M19</strong></td><td>Circle Geometry: Radius vs Diameter in Area (&pi;r&sup2;)</td><td>pp. 40–41</td><td>Geometry</td><td>[ &nbsp; ]</td></tr>
    <tr><td><strong>Mode M20</strong></td><td>Volume &amp; Surface Area of Prisms, Cylinders &amp; Tanks</td><td>pp. 42–43</td><td>Geometry</td><td>[ &nbsp; ]</td></tr>
    <tr><td><strong>Mode M21</strong></td><td>Metric Conversions: Area (m&sup2; to cm&sup2;) &amp; Volume (m&sup3; to Litres)</td><td>pp. 44–45</td><td>Measures</td><td>[ &nbsp; ]</td></tr>
    <tr><td><strong>Mode M22</strong></td><td>Compound Measures: Speed, Distance &amp; Time (Decimal Hours)</td><td>pp. 46–47</td><td>Measures</td><td>[ &nbsp; ]</td></tr>
    <tr><td><strong>Mode M23</strong></td><td>Compound Measures: Density, Mass &amp; Volume / Pressure</td><td>pp. 48–49</td><td>Measures</td><td>[ &nbsp; ]</td></tr>
    <tr><td><strong>Mode M24</strong></td><td>Pythagoras' Theorem: Hypotenuse &amp; Sloping Ramp Lengths</td><td>pp. 50–51</td><td>Geometry</td><td>[ &nbsp; ]</td></tr>
    <tr><td><strong>Mode M25</strong></td><td>Mean from Grouped Frequency Tables (Midpoint Estimating)</td><td>pp. 52–53</td><td>Data</td><td>[ &nbsp; ]</td></tr>
    <tr><td><strong>Mode M26</strong></td><td>Comparing Data Sets: Interpreting Mean and Range</td><td>pp. 54–55</td><td>Data</td><td>[ &nbsp; ]</td></tr>
    <tr><td><strong>Mode M27</strong></td><td>Combined Probability of Independent Events &amp; Trees</td><td>pp. 56–57</td><td>Data</td><td>[ &nbsp; ]</td></tr>
    <tr><td><strong>Mode E28</strong></td><td>Comma Splices vs Semicolons &amp; Sentence Boundaries</td><td>pp. 58–59</td><td>SPaG</td><td>[ &nbsp; ]</td></tr>
    <tr><td><strong>Mode E29</strong></td><td>Apostrophes of Omission vs Possession (its / it's &amp; Plurals)</td><td>pp. 60–61</td><td>SPaG</td><td>[ &nbsp; ]</td></tr>
    <tr><td><strong>Mode E30</strong></td><td>Subject-Verb Agreement with Collective &amp; Indefinite Pronouns</td><td>pp. 62–63</td><td>SPaG</td><td>[ &nbsp; ]</td></tr>
    <tr style="background:#fef3c7;"><td><strong>Exit Exam</strong></td><td>Full BKSB Diagnostic Exit Milestone Assessment (30 Items)</td><td>pp. 64–67</td><td>Milestone</td><td>[ &nbsp; ]</td></tr>
    <tr style="background:#e0f2fe;"><td><strong>Answers</strong></td><td>Distractor Breakdown &amp; Explanatory Answer Key (16 Pages)</td><td>pp. 68–83</td><td>Key</td><td>[ &nbsp; ]</td></tr>
  </table>

  <div class="page-footer">
    <div>BKSB &amp; OneAdvanced Diagnostic Remediation Workbook</div>
    <div class="page-num">Page 3</div>
  </div>
</div>
""")

    # -------------------------------------------------------------
    # 30 DIAGNOSTIC FAILURE MODES (2 Pages each = 60 pages, Pages 4 to 63)
    # -------------------------------------------------------------
    bksb_modes_data = [
        # Mode M1
        ("Mode M1: Place Value, Ordering &amp; Significant Figures", "Diagnostic Number &bull; Level 2 Threshold",
         """BKSB diagnostics frequently present large numbers and decimals requiring rounding to 1 or 2 significant figures. Over 68% of candidates confuse significant figures with decimal places.""",
         """<strong>The Algorithmic Failure Trap:</strong><br>
         <em>Round 0.04076 to 2 significant figures.</em><br>
         &bull; <strong>The Trap Distractor:</strong> 0.04 (incorrectly counted decimal places instead of significant figures).<br>
         <strong>Why It Fails:</strong> Leading zeros are never significant; they are merely place value holders!<br><br>
         <strong>The Tutor Golden Rule:</strong><br>
         1. The first significant figure is the <strong>first non-zero digit</strong> reading from left to right (here, 4).<br>
         2. The second significant figure is the next digit (0).<br>
         3. Look at the deciding third digit (7): since 7 &ge; 5, round the 0 up to 1 &rarr; <strong>0.041</strong>.""",
         "Round <strong>34,862</strong> to 2 significant figures and <strong>0.00785</strong> to 2 significant figures.",
         """1. For 34,862: 1st sig fig is 3, 2nd is 4. Deciding digit is 8 (rounds up) &rarr; <strong>35,000</strong>.<br>2. For 0.00785: 1st sig fig is 7, 2nd is 8. Deciding digit is 5 (rounds up) &rarr; <strong>0.0079</strong>.<br><strong>Check:</strong> Both numbers now carry exactly 2 significant figures.""",
         "Never drop trailing zeros in whole numbers! Rounding 34,862 to 35 turns £34,862 into £35!",
         "Leading zeros after a decimal point are NOT significant: 0.005 has only 1 significant figure.",
         [
           ("Round 0.05629 to 2 significant figures.", "[2 Marks]"),
           ("Round 48,290 to 1 significant figure.", "[2 Marks]"),
           ("Explain the difference between rounding 4.076 to 2 decimal places versus 2 significant figures.", "[2 Marks]"),
           ("Write forty-five thousand and sixty-two in figures, then round to 2 significant figures.", "[2 Marks]")
         ]),

        # Mode M2
        ("Mode M2: Negative Numbers in Practical Contexts", "Diagnostic Number &bull; Level 2 Threshold",
         """Computer-adaptive diagnostics present multi-step temperature swings and financial overdraft changes. Learners frequently stumble when subtracting a negative number.""",
         """<strong>The Algorithmic Failure Trap:</strong><br>
         <em>At midnight the temperature in a cold store was -6&deg;C. By 06:00 it had fallen by 8&deg;C. What is the new temperature?</em><br>
         &bull; <strong>The Trap Distractor:</strong> 2&deg;C (wrongly added 8, or calculated 8 - 6).<br>
         <strong>Why It Fails:</strong> Falling temperature means moving further left on the number line: <code>-6 - 8 = -14&deg;C</code>.<br><br>
         <strong>The Tutor Golden Rule:</strong><br>
         1. Subtracting a positive moves LEFT on the number line.<br>
         2. Subtracting a negative turns into ADDITION: <code>5 - (-3) = 5 + 3 = 8</code>.<br>
         3. Temperature difference: <code>Highest - Lowest</code> (e.g. difference between 12&deg;C and -5&deg;C is <code>12 - (-5) = 17&deg;C</code>).""",
         "A bank account has a balance of <strong>-£145</strong>. The customer deposits £220 and then pays a bill of £95. What is the final balance?",
         """1. Starting balance: <code>-145</code>.<br>2. After deposit: <code>-145 + 220 = +£75</code>.<br>3. After bill: <code>75 - 95 = -£20</code>.<br><strong>Final Balance: -£20 (overdrawn by £20)</strong>.""",
         "Minus followed by minus becomes a plus: 15 - (-4) = 19, NOT 11!",
         "Always sketch a vertical thermometer line when solving temperature difference questions.",
         [
           ("Calculate the difference in temperature between 18&deg;C and -7&deg;C.", "[2 Marks]"),
           ("A freezer operates at -18&deg;C. During a defrost cycle, the temperature rises by 12&deg;C. What is the temperature now?", "[2 Marks]"),
           ("Solve: -45 - (-18) + (-12).", "[2 Marks]"),
           ("A bank account balance is -£80. How much must be deposited to bring the balance to +£150?", "[2 Marks]")
         ]),

        # Mode M3
        ("Mode M3: Order of Operations (BIDMAS / BODMAS)", "Diagnostic Number &bull; Level 2 Threshold",
         """BKSB diagnostics test order of operations with combined squares and division. Over 70% of learners calculate strictly left-to-right, falling into calculated traps.""",
         """<strong>The Algorithmic Failure Trap:</strong><br>
         <em>Evaluate: 20 - 4 &times; 3&sup2; &divide; 6</em><br>
         &bull; <strong>The Trap Distractor:</strong> 24 (calculated 20 - 4 = 16, then multiplied).<br>
         <strong>Why It Fails:</strong> BIDMAS dictates Indices first, then Multiplication/Division, then Subtraction!<br><br>
         <strong>The Tutor Golden Rule (BIDMAS Sequence):</strong><br>
         1. <strong>B</strong>rackets first &bull; 2. <strong>I</strong>ndices (powers/roots) &bull; 3. <strong>D</strong>ivision &amp; <strong>M</strong>ultiplication (left to right) &bull; 4. <strong>A</strong>ddition &amp; <strong>S</strong>ubtraction.<br>
         &bull; Step 1 (Index): <code>3&sup2; = 9</code> &rarr; <code>20 - 4 &times; 9 &divide; 6</code>.<br>
         &bull; Step 2 (Mult/Div): <code>4 &times; 9 = 36 &rarr; 36 &divide; 6 = 6</code>.<br>
         &bull; Step 3 (Sub): <code>20 - 6 = 14</code>.""",
         "Evaluate: <strong>(15 - 3) &times; 2&sup2; + 18 &divide; 3</strong>.",
         """1. Brackets: <code>(15 - 3) = 12</code>.<br>2. Indices: <code>2&sup2; = 4</code>.<br>3. Multiply and Divide: <code>12 &times; 4 = 48</code> and <code>18 &divide; 3 = 6</code>.<br>4. Add: <code>48 + 6 = 54</code>.<br><strong>Result: 54</strong>.""",
         "Never calculate left-to-right if multiplication or indices appear later in the expression!",
         "In expressions like 12 &divide; 2 &times; 3, do division and multiplication from left to right: 6 &times; 3 = 18.",
         [
           ("Evaluate: 14 + 6 &times; 5 - 12 &divide; 4.", "[2 Marks]"),
           ("Evaluate: 3 &times; (4 + 2)&sup2; - 20.", "[2 Marks]"),
           ("Insert brackets to make this statement correct: 5 + 3 &times; 4 - 2 = 30.", "[2 Marks]"),
           ("Evaluate: 40 - 2 &times; 3&sup3;.", "[2 Marks]")
         ]),

        # Mode M4
        ("Mode M4: Multi-Step Fractions of Quantities", "Diagnostic Fractions &bull; Level 2 Threshold",
         """Diagnostics present word problems where a fraction of a remaining balance is required. Learners habitually calculate all fractions from the original total.""",
         """<strong>The Algorithmic Failure Trap:</strong><br>
         <em>A company has £1,200. It spends 1/4 on rent and 2/3 of the REMAINDER on wages. How much is left?</em><br>
         &bull; <strong>The Trap Distractor:</strong> £100 (wrongly calculated 2/3 of the ORIGINAL 1,200 = 800; 1,200 - 300 - 800 = 100).<br>
         <strong>Why It Fails:</strong> The question specified 2/3 of the <em>remainder</em>, not the starting sum!<br><br>
         <strong>The Tutor Golden Rule:</strong><br>
         1. Find rent: <code>1/4 of 1,200 = 1,200 &divide; 4 = £300</code>.<br>
         2. Find remainder: <code>1,200 - 300 = £900</code>.<br>
         3. Find wages: <code>2/3 of 900 = (900 &divide; 3) &times; 2 = £600</code>.<br>
         4. Left over: <code>900 - 600 = £300</code>.""",
         "A warehouse holds 840 pallets. <strong>3/7 are shipped on Monday</strong>. On Tuesday, <strong>1/4 of the remaining pallets</strong> are shipped. How many pallets remain?",
         """1. Monday: <code>(840 &divide; 7) &times; 3 = 120 &times; 3 = 360 pallets</code> shipped.<br>2. Remainder after Monday: <code>840 - 360 = 480 pallets</code>.<br>3. Tuesday: <code>1/4 of 480 = 480 &divide; 4 = 120 pallets</code> shipped.<br>4. Final remaining: <code>480 - 120 = 360 pallets</code>.<br><strong>Answer: 360 pallets</strong>.""",
         "Always circle the word 'REMAINDER' in fraction word problems. Calculate the intermediate balance before taking the next fraction!",
         "To find a fraction of a quantity: divide by denominator, multiply by numerator.",
         [
           ("A bakery bakes 360 loaves. 2/5 are white bread. 1/3 of the remaining loaves are wholemeal. How many loaves are wholemeal?", "[2 Marks]"),
           ("Find 5/8 of £960.", "[2 Marks]"),
           ("A lottery prize of £2,400 is split: Alex takes 1/3, Ben takes 3/8 of the remainder. How much is left for Clara?", "[2 Marks]"),
           ("Explain why 2/3 of 60 is NOT the same as 60 &divide; 2 &times; 3.", "[2 Marks]")
         ]),

        # Mode M5
        ("Mode M5: Adding &amp; Subtracting Mixed Numbers", "Diagnostic Fractions &bull; Level 2 Threshold",
         """Learners attempt to add numerators and denominators directly, or struggle with borrowing when subtracting mixed numbers.""",
         """<strong>The Algorithmic Failure Trap:</strong><br>
         <em>Calculate: 3 1/4 - 1 2/3</em><br>
         &bull; <strong>The Trap Distractor:</strong> 2 1/1 (subtracted whole numbers 3-1=2, and reversed fractions 2/3 - 1/4).<br>
         <strong>Why It Fails:</strong> 1/4 is smaller than 2/3, so you cannot simply subtract numerators!<br><br>
         <strong>The Tutor Golden Rule (Improper Fraction Method):</strong><br>
         1. Convert to improper fractions: <code>3 1/4 = 13/4</code> and <code>1 2/3 = 5/3</code>.<br>
         2. Common denominator of 4 and 3 is 12: <code>13/4 = 39/12</code> and <code>5/3 = 20/12</code>.<br>
         3. Subtract: <code>39/12 - 20/12 = 19/12</code>.<br>
         4. Convert back to mixed number: <code>19/12 = 1 7/12</code>.""",
         "Calculate: <strong>2 3/5 + 1 3/4</strong>. Give your answer as a mixed number in simplest form.",
         """1. Convert to improper: <code>2 3/5 = 13/5</code>; <code>1 3/4 = 7/4</code>.<br>2. Common denominator is 20: <code>(13&times;4)/20 = 52/20</code>; <code>(7&times;5)/20 = 35/20</code>.<br>3. Add numerators: <code>52/20 + 35/20 = 87/20</code>.<br>4. Convert: <code>87 &divide; 20 = 4</code> remainder 7 &rarr; <strong>4 7/20</strong>.""",
         "NEVER add denominators: 1/2 + 1/3 is NOT 2/5! Find the lowest common multiple first.",
         "Converting mixed numbers to improper fractions completely eliminates borrowing errors in subtraction.",
         [
           ("Calculate: 2 1/3 + 3 2/5.", "[2 Marks]"),
           ("Calculate: 4 1/6 - 2 3/4.", "[2 Marks]"),
           ("Solve: 5 - 2 4/7.", "[2 Marks]"),
           ("Express 47/8 as a mixed number.", "[1 Mark]")
         ]),

        # Mode M6
        ("Mode M6: Multiplying &amp; Dividing Fractions", "Diagnostic Fractions &bull; Level 2 Threshold",
         """Diagnostics test fraction division using recipes and scaling. Learners forget to invert the second fraction or forget to convert mixed numbers first.""",
         """<strong>The Algorithmic Failure Trap:</strong><br>
         <em>Calculate: 3/4 &divide; 2/5</em><br>
         &bull; <strong>The Trap Distractor:</strong> 6/20 = 3/10 (multiplied across instead of dividing).<br>
         <strong>Why It Fails:</strong> Division requires multiplying by the reciprocal ('Keep, Change, Flip')!<br><br>
         <strong>The Tutor Golden Rule:</strong><br>
         1. <strong>Keep:</strong> Leave the first fraction unchanged: <code>3/4</code>.<br>
         2. <strong>Change:</strong> Change division sign to multiplication: <code>&times;</code>.<br>
         3. <strong>Flip:</strong> Invert the second fraction: <code>2/5 &rarr; 5/2</code>.<br>
         4. Multiply across: <code>(3 &times; 5) / (4 &times; 2) = 15/8 = 1 7/8</code>.""",
         "A chef has <strong>4 1/2 kg</strong> of sugar. Each cake requires <strong>3/8 kg</strong>. How many cakes can be baked?",
         """1. Convert 4 1/2 to improper: <code>9/2 kg</code>.<br>2. Set up division: <code>9/2 &divide; 3/8</code>.<br>3. Keep, Change, Flip: <code>9/2 &times; 8/3</code>.<br>4. Simplify before multiplying: (9 &divide; 3 = 3) and (8 &divide; 2 = 4) &rarr; <code>3 &times; 4 = 12 cakes</code>.<br><strong>Answer: 12 cakes</strong>.""",
         "Always convert mixed numbers to improper fractions BEFORE multiplying or dividing: 2 1/2 &times; 1 1/3 = 5/2 &times; 4/3 = 20/6 = 3 1/3.",
         "Never flip the first fraction! Only flip the second fraction.",
         [
           ("Calculate: 5/6 &times; 3/10. Simplify your answer.", "[2 Marks]"),
           ("Calculate: 2 2/3 &divide; 4/9.", "[2 Marks]"),
           ("A ribbon is 7 1/2 m long. It is cut into pieces of 3/4 m. How many full pieces can be cut?", "[2 Marks]"),
           ("Solve: 1 1/2 &times; 2 2/3.", "[2 Marks]")
         ]),

        # Mode M7
        ("Mode M7: Decimal Multiplication &amp; Decimal Places", "Diagnostic Decimals &bull; Level 2 Threshold",
         """Over 65% of diagnostic errors in decimals occur from misplacing the decimal point after multi-digit multiplication.""",
         """<strong>The Algorithmic Failure Trap:</strong><br>
         <em>Calculate: 0.4 &times; 0.08</em><br>
         &bull; <strong>The Trap Distractor:</strong> 0.32 (counted only 2 decimal places instead of 3).<br>
         <strong>Why It Fails:</strong> 0.4 has 1 decimal place; 0.08 has 2 decimal places. Total decimal places must be 1 + 2 = 3!<br><br>
         <strong>The Tutor Golden Rule:</strong><br>
         1. Ignore decimals and multiply integers: <code>4 &times; 8 = 32</code>.<br>
         2. Count TOTAL decimal places in the question: 1 + 2 = 3 places.<br>
         3. Place decimal point 3 positions from the right: <code>32 &rarr; 0.032</code>.""",
         "Calculate: <strong>3.25 &times; 0.6</strong> without a calculator.",
         """1. Multiply as integers: <code>325 &times; 6 = 1,950</code>.<br>2. Count decimal places: 3.25 has 2; 0.6 has 1 &rarr; Total = 3 decimal places.<br>3. Count 3 places from right: <code>1.950 = 1.95</code>.<br><strong>Answer: 1.95</strong>.""",
         "Do not align decimal points when multiplying! Multiply as normal whole numbers, then count total decimal places.",
         "Add placeholder zeros if the answer has fewer digits than required: 2 digits for 3 decimal places becomes 0.032.",
         [
           ("Calculate: 0.7 &times; 0.09.", "[2 Marks]"),
           ("Calculate: 4.5 &times; 1.8.", "[2 Marks]"),
           ("A fuel price is £1.428 per litre. What is the cost of 50 litres? (Round to nearest penny).", "[2 Marks]"),
           ("State how many decimal places will be in the product of 0.045 and 1.2.", "[1 Mark]")
         ]),

        # Mode M8
        ("Mode M8: Decimal Division by Decimals", "Diagnostic Decimals &bull; Level 2 Threshold",
         """Learners attempt long division with decimal points in the divisor, resulting in chaotic miscalculations.""",
         """<strong>The Algorithmic Failure Trap:</strong><br>
         <em>Calculate: 3.6 &divide; 0.04</em><br>
         &bull; <strong>The Trap Distractor:</strong> 0.9 or 9 (divided 36 by 4 without shifting both numbers equally).<br>
         <strong>Why It Fails:</strong> You must multiply BOTH numerator and denominator by 100 to make the divisor a whole number!<br><br>
         <strong>The Tutor Golden Rule:</strong><br>
         1. Write as a fraction: <code>3.6 / 0.04</code>.<br>
         2. Multiply top and bottom by 100 to make bottom a whole number: <code>(3.6 &times; 100) / (0.04 &times; 100) = 360 / 4</code>.<br>
         3. Divide: <code>360 &divide; 4 = 90</code>.""",
         "A metal rod is <strong>4.8 metres</strong> long. It is cut into pins of length <strong>0.15 metres</strong>. How many full pins can be cut?",
         """1. Set up division: <code>4.8 &divide; 0.15 = 4.8 / 0.15</code>.<br>2. Multiply top and bottom by 100: <code>480 &divide; 15</code>.<br>3. Divide: <code>480 &divide; 15 = 32</code>.<br><strong>Answer: 32 full pins</strong>.""",
         "Never divide by a decimal! Always shift the decimal point equally in both numbers until the divisor is an integer.",
         "Check with estimation: 4.8 &divide; 0.15 &asymp; 5 &divide; 0.2 = 25. An answer of 32 makes complete sense.",
         [
           ("Calculate: 5.4 &divide; 0.09.", "[2 Marks]"),
           ("Calculate: 18 &divide; 0.4.", "[2 Marks]"),
           ("A dosing syringe holds 0.25 ml. A bottle contains 6 ml. How many doses are in the bottle?", "[2 Marks]"),
           ("Show why 7.2 &divide; 0.08 equals 90, not 9.", "[2 Marks]")
         ]),

        # Mode M9
        ("Mode M9: Recurring Decimals to Fractions", "Diagnostic Decimals &bull; Level 2 Threshold",
         """BKSB screens present recurring decimals (0.333..., 0.666..., 0.1666...). Learners round too early, creating significant downstream errors.""",
         """<strong>The Algorithmic Failure Trap:</strong><br>
         <em>A machine runs for 2 hours and 20 minutes at £18/hour. What is the cost?</em><br>
         &bull; <strong>The Trap Distractor:</strong> £39.60 (entered 2.2 hours &rarr; 2.2 &times; 18 = 39.60).<br>
         <strong>Why It Fails:</strong> 20 minutes is 20/60 = 1/3 hour = 0.333... hours, NOT 0.2 hours!<br><br>
         <strong>The Tutor Golden Rule:</strong><br>
         1. Convert minutes to exact fractions: <code>20 mins = 20/60 = 1/3 hour</code>.<br>
         2. Total hours: <code>2 1/3 hours = 7/3 hours</code>.<br>
         3. Multiply: <code>(7/3) &times; 18 = 7 &times; 6 = £42.00</code>.""",
         "Convert <strong>0.375</strong> to a fraction in simplest form, and convert <strong>0.8333... (0.83&#775;)</strong> to a fraction.",
         """1. 0.375 = 375/1000. Divide top and bottom by 125 &rarr; <strong>3/8</strong>.<br>2. 0.8333... = 5/6 (Check: 5 &divide; 6 = 0.8333...).<br><strong>Common Equivalents:</strong> 1/3 = 0.333..., 2/3 = 0.666..., 1/6 = 0.1666..., 5/6 = 0.8333...""",
         "Never round 1/3 to 0.33 or 2/3 to 0.67 in intermediate steps! Use the fraction button on your calculator or keep exact fractions.",
         "Remember: 15 mins = 0.25 hrs; 30 mins = 0.5 hrs; 45 mins = 0.75 hrs; 20 mins = 1/3 hr; 40 mins = 2/3 hr.",
         [
           ("Express 0.625 as a simplified fraction.", "[2 Marks]"),
           ("A worker is paid £15 per hour. How much do they earn for working 3 hours and 40 minutes?", "[2 Marks]"),
           ("Convert 7/12 to a decimal rounded to 3 decimal places.", "[2 Marks]"),
           ("Explain why 40 minutes is NOT 0.4 hours.", "[2 Marks]")
         ]),

        # Mode M10
        ("Mode M10: Reverse Percentages (Original Value)", "Diagnostic Percentages &bull; Level 2 Threshold",
         """BKSB diagnostics frequently test original prices before a sale discount or price increase. Over 74% of candidates fail because they calculate the percentage of the NEW price and add/subtract it.""",
         """<strong>The Algorithmic Failure Trap:</strong><br>
         <em>A coat costs £72 in a 20% off sale. What was the original price?</em><br>
         &bull; <strong>The Trap Distractor:</strong> £86.40 (calculated 20% of 72 = 14.40 &rarr; 72 + 14.40 = 86.40).<br>
         <strong>Why It Fails:</strong> The 20% discount was taken off the ORIGINAL price, not the sale price!<br><br>
         <strong>The Tutor Golden Rule:</strong><br>
         1. The original price is always <strong>100%</strong>.<br>
         2. After a 20% reduction, the sale price represents <code>100% - 20% = 80%</code>.<br>
         3. Set up the equation: <code>80% = £72 &rarr; 0.80 &times; Original = 72</code>.<br>
         4. Divide by the multiplier: <code>72 &divide; 0.80 = £90.00</code>.""",
         "A laptop is priced at <strong>£612 after a 15% discount</strong>. Calculate the original price before the sale.",
         """1. Original = 100%.<br>2. Sale price percentage = 100% - 15% = 85%.<br>3. Multiplier = 0.85.<br>4. Divide: <code>612 &divide; 0.85 = £720</code>.<br><strong>Original Price: £720</strong>. (Check: 15% of 720 = 108; 720 - 108 = 612).""",
         "NEVER calculate percentage of the sale price and add it back. Always divide by the remaining percentage multiplier.",
         "Original = New Value &divide; Percentage Multiplier.",
         [
           ("A microwave is sold for £162 after a 10% reduction. What was the original price?", "[2 Marks]"),
           ("A salary increased by 5% to £25,200. What was the salary before the pay rise?", "[2 Marks]"),
           ("Explain why calculating 20% of £80 and adding it back does NOT reverse a 20% discount.", "[2 Marks]"),
           ("A restaurant bill is £96 including 20% VAT. Find the bill before VAT was added.", "[2 Marks]")
         ]),

        # Mode M11
        ("Mode M11: Percentage Change &amp; Single Multipliers", "Diagnostic Percentages &bull; Level 2 Threshold",
         """In BKSB diagnostic assessments, candidates lose valuable time calculating multi-step percentages using basic 10% chunks. High-scoring candidates use single decimal multipliers.""",
         """<strong>The Decimal Multiplier System:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>Percentage Increase:</strong> Add percentage to 100% and convert to decimal.
             <br>&bull; Increase by 15%: <code>100% + 15% = 115% &rarr; &times; 1.15</code>
             <br>&bull; Increase by 3.5%: <code>100% + 3.5% = 103.5% &rarr; &times; 1.035</code> (Notice the zero!)
           </li>
           <li><strong>Percentage Decrease:</strong> Subtract percentage from 100% and convert to decimal.
             <br>&bull; Decrease by 25%: <code>100% - 25% = 75% &rarr; &times; 0.75</code>
             <br>&bull; Decrease by 8%: <code>100% - 8% = 92% &rarr; &times; 0.92</code>
           </li>
           <li><strong>Percentage Change Formula:</strong> <code>(Difference &divide; Original) &times; 100</code>.</li>
         </ul>""",
         "A company's energy bill increased from <strong>£450</strong> to <strong>£522</strong>. Calculate the percentage increase.",
         """1. Find the absolute increase: <code>522 - 450 = £72</code>.<br>2. Divide by the ORIGINAL value: <code>72 &divide; 450 = 0.16</code>.<br>3. Multiply by 100: <code>0.16 &times; 100 = 16%</code>.<br><strong>Percentage Increase: 16%</strong>.""",
         "Watch the zero when working with single-digit percentages! An increase of 4% uses multiplier 1.04, NOT 1.4 (which is a 40% increase!).",
         "Always divide by the ORIGINAL (starting) amount, never the final amount.",
         [
           ("Write the single decimal multiplier used to: a) Increase by 18% &nbsp;&nbsp; b) Decrease by 12% &nbsp;&nbsp; c) Increase by 6%", "[3 Marks]"),
           ("Use a multiplier to calculate £850 increased by 14%.", "[2 Marks]"),
           ("A car bought for £12,000 is sold for £9,600. Calculate the percentage loss.", "[2 Marks]"),
           ("What is the decimal multiplier for a 2.5% pay increase?", "[1 Mark]")
         ]),

        # Mode M12
        ("Mode M12: Compound Interest &amp; Depreciation", "Diagnostic Percentages &bull; Level 2 Threshold",
         """Learners treat compound interest as simple interest, calculating the interest for Year 1 and simply multiplying by the number of years.""",
         """<strong>The Algorithmic Failure Trap:</strong><br>
         <em>£4,000 is invested at 5% compound interest per year for 3 years. Calculate the final balance.</em><br>
         &bull; <strong>The Trap Distractor:</strong> £4,600 (calculated simple interest: 5% of 4,000 = 200 &times; 3 = 600 &rarr; 4,600).<br>
         <strong>Why It Fails:</strong> In compound interest, you earn interest on previous years' interest!<br><br>
         <strong>The Tutor Golden Rule:</strong><br>
         Use the power formula: <code>Total = Principal &times; (Multiplier)^years</code>.<br>
         &bull; Multiplier for 5% increase = 1.05.<br>
         &bull; Final balance: <code>4,000 &times; (1.05)&sup3; = 4,000 &times; 1.157625 = £4,630.50</code>.""",
         "A company van bought for <strong>£24,000</strong> depreciates by <strong>15% per year</strong>. Calculate its book value after 2 years.",
         """1. Depreciation multiplier: <code>100% - 15% = 85% &rarr; 0.85</code>.<br>2. Year 1: <code>24,000 &times; 0.85 = £20,400</code>.<br>3. Year 2: <code>20,400 &times; 0.85 = £17,340</code>.<br><em>Quick power method:</em> <code>24,000 &times; (0.85)&sup2; = £17,340</code>.<br><strong>Value after 2 years: £17,340</strong>.""",
         "Never confuse compound interest with simple interest! Use the multiplier raised to the power of years.",
         "Depreciation always decreases value: use multiplier (1 - r), e.g. 15% depreciation uses 0.85.",
         [
           ("Calculate the compound interest on £5,000 invested at 4% per year for 2 years.", "[2 Marks]"),
           ("A machine costing £16,000 depreciates by 20% each year. Find its value after 3 years.", "[2 Marks]"),
           ("Explain why compound interest yields more money than simple interest over 5 years.", "[2 Marks]"),
           ("Write the calculation in one line using a power to find £2,000 invested at 3% for 4 years.", "[1 Mark]")
         ]),

        # Mode M13
        ("Mode M13: Comparing Special Offers &amp; Unit Value", "Diagnostic Percentages &bull; Level 2 Threshold",
         """Diagnostics present complex promotional offers (e.g. '3 for 2', 'Buy one get 50% off second', '25% extra free'). Learners fail to compare identical quantities.""",
         """<strong>The Algorithmic Failure Trap:</strong><br>
         <em>Offer A: 500g cereal for £2.40. Offer B: 750g cereal for £3.30. Which is better value?</em><br>
         &bull; <strong>The Trap Distractor:</strong> Offer A because £2.40 is cheaper.<br>
         <strong>Why It Fails:</strong> Offer A has less cereal! You must calculate cost per unit weight (e.g. per 100g or per kg).<br><br>
         <strong>The Tutor Golden Rule (Unitary Comparison Method):</strong><br>
         &bull; Offer A: <code>£2.40 &divide; 5 = £0.48 per 100g</code>.<br>
         &bull; Offer B: <code>£3.30 &divide; 7.5 = £0.44 per 100g</code>.<br>
         &bull; <strong>Offer B is better value by 4p per 100g.</strong>""",
         "A coffee shop offers: <strong>Deal 1:</strong> Buy 2 bags at £6.50 each, get a 3rd free. <strong>Deal 2:</strong> 30% off all bags priced at £6.50 each. Which deal is cheaper for 3 bags?",
         """1. Deal 1: Pay for 2 bags = <code>2 &times; £6.50 = £13.00</code>.<br>2. Deal 2: 30% off £6.50 = <code>6.50 &times; 0.70 = £4.55 per bag</code>. For 3 bags: <code>3 &times; 4.55 = £13.65</code>.<br>3. Compare: £13.00 vs £13.65.<br><strong>Deal 1 is cheaper by £0.65</strong>.""",
         "Always compare cost per unit (e.g. pence per 100g, pence per ml) or the total cost for the exact same quantity.",
         "'Buy 2 get 1 free' is equivalent to a 33.3% discount on 3 items.",
         [
           ("Juice Brand A: 1.5 litres for £1.80. Brand B: 2 litres for £2.30. Which offers better value per litre?", "[2 Marks]"),
           ("A coat costs £80. Store A offers 25% off. Store B offers £15 off plus an extra 10% off the discounted price. Which store is cheaper?", "[2 Marks]"),
           ("Explain why 'Buy 1 get 1 half price' is equivalent to a 25% discount across two items.", "[2 Marks]"),
           ("Calculate the unit price in pence per 100g for a 400g pasta jar costing £1.16.", "[1 Mark]")
         ]),

        # Mode M14
        ("Mode M14: Ratio Sharing &ndash; Part-to-Whole Pitfalls", "Diagnostic Ratio &bull; Level 2 Threshold",
         """Diagnostics present word problems where a known individual share is given rather than the total. Over 62% of learners add the ratio parts and divide the given share by the sum.""",
         """<strong>The Algorithmic Failure Trap:</strong><br>
         <em>A bonus is shared between Sarah and Tom in the ratio 3 : 5. Tom receives £450. What was the total bonus?</em><br>
         &bull; <strong>The Trap Distractor:</strong> £450 &divide; 8 = £56.25 (divided Tom's share by the sum of parts).<br>
         <strong>Why It Fails:</strong> £450 belongs ONLY to Tom (5 parts), not all 8 parts!<br><br>
         <strong>The Tutor Golden Rule:</strong><br>
         1. Identify who the given number belongs to: Tom = 5 parts = £450.<br>
         2. Find the value of <strong>ONE part</strong>: <code>450 &divide; 5 = £90</code>.<br>
         3. Sarah's share (3 parts): <code>3 &times; 90 = £270</code>.<br>
         4. Total bonus (8 parts): <code>8 &times; 90 = £720</code> (or 270 + 450 = £720).""",
         "Concrete is mixed using cement, sand, and gravel in the ratio <strong>1 : 2 : 4</strong>. A builder has <strong>150 kg of sand</strong>. What is the maximum total concrete that can be mixed?",
         """1. Sand represents 2 parts = 150 kg.<br>2. Find 1 part: <code>150 &divide; 2 = 75 kg</code>.<br>3. Total parts in mix = <code>1 + 2 + 4 = 7 parts</code>.<br>4. Total concrete = <code>7 &times; 75 = 525 kg</code>.<br><strong>Total Concrete: 525 kg</strong> (Cement: 75 kg, Sand: 150 kg, Gravel: 300 kg).""",
         "Read carefully: Does the amount represent the TOTAL or ONE PERSON'S SHARE? Never divide by total parts if given a single share!",
         "Check your answer by summing individual shares: 75 + 150 + 300 = 525 kg.",
         [
           ("Share £480 in the ratio 5 : 3.", "[2 Marks]"),
           ("Paints are mixed in the ratio blue : yellow = 3 : 2. A painter uses 18 litres of blue paint. How much yellow paint is needed?", "[2 Marks]"),
           ("In a factory, the ratio of daytime workers to night workers is 7 : 2. There are 42 night workers. How many daytime workers are there?", "[2 Marks]"),
           ("Three partners split profits in ratio 2 : 3 : 5. The highest share is £6,000. Find the total profit shared.", "[2 Marks]")
         ]),

        # Mode M15
        ("Mode M15: Direct Proportion &amp; The Unitary Method", "Diagnostic Ratio &bull; Level 2 Threshold",
         """Scaling recipes, staffing rotas, and manufacturing rates requires the unitary method: finding the value for ONE unit first.""",
         """<strong>The Algorithmic Failure Trap:</strong><br>
         <em>A recipe for 6 people requires 450g of flour. How much flour is needed for 15 people?</em><br>
         &bull; <strong>The Trap Distractor:</strong> 900g (doubled for 12, but guessed the remaining 3).<br>
         <strong>Why It Fails:</strong> Inexact scaling leads to guesswork. Use the unitary method!<br><br>
         <strong>The Tutor Golden Rule (The Unitary Method):</strong><br>
         1. Find the amount for <strong>1 person</strong>: <code>450 &divide; 6 = 75g</code>.<br>
         2. Multiply by target quantity (15 people): <code>75 &times; 15 = 1,125g (or 1.125 kg)</code>.<br>
         <em>Alternative multiplier:</em> <code>15 &divide; 6 = 2.5 &rarr; 450 &times; 2.5 = 1,125g</code>.""",
         "A printing machine prints <strong>420 leaflets in 14 minutes</strong>. How many leaflets does it print in <strong>35 minutes</strong> at the same rate?",
         """1. Find leaflets printed per 1 minute: <code>420 &divide; 14 = 30 leaflets/min</code>.<br>2. Multiply by 35 minutes: <code>30 &times; 35 = 1,050 leaflets</code>.<br><strong>Answer: 1,050 leaflets</strong>.""",
         "Always find the value of ONE unit first (divide), then multiply by the target number.",
         "Direct proportion means if one quantity doubles, the other quantity also doubles.",
         [
           ("8 identical bottles of juice cost £14.40. How much do 13 bottles cost?", "[2 Marks]"),
           ("A car travels 165 miles on 15 litres of fuel. How far can it travel on 22 litres?", "[2 Marks]"),
           ("A catering recipe for 8 portions uses 600g of beef. How much beef is needed for 20 portions?", "[2 Marks]"),
           ("5 workers take 6 hours to paint a hall. Explain why doubling workers does NOT double the hours taken.", "[2 Marks]")
         ]),

        # Mode M16
        ("Mode M16: Inverse Proportion (Workforce vs Time)", "Diagnostic Ratio &bull; Level 2 Threshold",
         """BKSB diagnostics test workforce logistics. Learners habitually use direct proportion, concluding that more workers will take MORE time!""",
         """<strong>The Algorithmic Failure Trap:</strong><br>
         <em>4 builders take 6 days to build a wall. How long would 8 builders take?</em><br>
         &bull; <strong>The Trap Distractor:</strong> 12 days (calculated directly: double builders = double days).<br>
         <strong>Why It Fails:</strong> More builders do the work faster, taking FEWER days! This is inverse proportion.<br><br>
         <strong>The Tutor Golden Rule (The 'Worker-Days' Total Method):</strong><br>
         1. Calculate total effort required: <code>4 builders &times; 6 days = 24 worker-days</code>.<br>
         2. Divide by the new workforce: <code>24 &divide; 8 builders = 3 days</code>.""",
         "It takes <strong>6 cleaners 4 hours</strong> to clean an office building. How many hours would it take <strong>8 cleaners</strong> working at the same speed?",
         """1. Total cleaning effort: <code>6 cleaners &times; 4 hours = 24 cleaner-hours</code>.<br>2. Divide by 8 cleaners: <code>24 &divide; 8 = 3 hours</code>.<br><strong>Answer: 3 hours</strong>.""",
         "In inverse proportion: as one variable INCREASES, the other DECREASES. The product of the two variables remains constant!",
         "Formula: <code>Workers &times; Time = Constant Total Work</code>.",
         [
           ("3 bricklayers take 10 days to build a conservatory. How many days will 5 bricklayers take?", "[2 Marks]"),
           ("A coach travels at 60 mph and completes a journey in 4 hours. How long will the journey take at 80 mph?", "[2 Marks]"),
           ("12 machines take 9 hours to produce a batch of components. How many hours would 4 machines take?", "[2 Marks]"),
           ("Explain the difference between direct proportion and inverse proportion using practical examples.", "[2 Marks]")
         ]),

        # Mode M17
        ("Mode M17: Scale Drawings &amp; Map Ratios", "Diagnostic Ratio &bull; Level 2 Threshold",
         """Diagnostics present scale drawings (1:50, 1:200, 1:25,000). Candidates fail to convert units between centimetres and metres/kilometres.""",
         """<strong>The Algorithmic Failure Trap:</strong><br>
         <em>On a 1 : 50 plan, a wall is 8 cm long. What is the real length in metres?</em><br>
         &bull; <strong>The Trap Distractor:</strong> 400 metres (multiplied 8 &times; 50 = 400, but forgot to convert cm to metres!).<br>
         <strong>Why It Fails:</strong> 400 cm must be divided by 100 to convert to metres: <code>400 &divide; 100 = 4 m</code>.<br><br>
         <strong>The Tutor Golden Rule:</strong><br>
         1. Multiply drawing measurement by scale factor: <code>8 cm &times; 50 = 400 cm</code>.<br>
         2. Convert to metres: <code>400 &divide; 100 = 4 metres</code>.<br>
         3. For 1 : 25,000 maps: <code>1 cm = 25,000 cm = 250 m = 0.25 km</code> (4 cm = 1 km).""",
         "A driveway is <strong>12 metres</strong> long in real life. What length will it be on an architectural drawing with scale <strong>1 : 50</strong>?",
         """1. Convert real length to centimetres: <code>12 m = 1,200 cm</code>.<br>2. Divide by scale factor: <code>1,200 &divide; 50 = 24 cm</code>.<br><strong>Drawing Length: 24 cm</strong>.""",
         "Always convert real metres to cm (multiply by 100) before dividing by the scale factor to find the drawing length.",
         "Scale ratio 1 : n means 1 unit on paper represents n units in the real world in the SAME unit.",
         [
           ("On a 1 : 200 site plan, a garden measures 7.5 cm by 4 cm. Find the real dimensions in metres.", "[2 Marks]"),
           ("A real room length of 6.5 m is drawn on a plan with scale 1 : 20. How long is the line on paper?", "[2 Marks]"),
           ("On a 1 : 25,000 Ordnance Survey map, two villages are 8 cm apart. What is the real distance in kilometres?", "[2 Marks]"),
           ("Explain what a scale ratio of 1 : 100 means in architecture.", "[1 Mark]")
         ]),

        # Mode M18
        ("Mode M18: Area &amp; Perimeter of Compound L-Shapes", "Diagnostic Geometry &bull; Level 2 Threshold",
         """Over 72% of candidates miss missing edge lengths on L-shaped diagrams or confuse area with perimeter.""",
         """<strong>The Algorithmic Failure Trap:</strong><br>
         <em>An L-shape has bottom edge 10m, left edge 8m, top horizontal 4m, right vertical 3m. Find missing edges and area.</em><br>
         &bull; <strong>The Trap Distractor:</strong> Missing edges guessed; or calculating perimeter by adding only the 4 given numbers.<br>
         <strong>Why It Fails:</strong> An L-shape has 6 sides, not 4! You must calculate missing inner edges first.<br><br>
         <strong>The Tutor Golden Rule:</strong><br>
         1. <strong>Find Missing Edges:</strong>
           <br>&bull; Horizontal missing = <code>10 - 4 = 6m</code>.
           <br>&bull; Vertical missing = <code>8 - 3 = 5m</code>.
         2. <strong>Perimeter:</strong> Sum all 6 sides: <code>10 + 8 + 4 + 5 + 6 + 3 = 36m</code>.<br>
         3. <strong>Split into 2 Rectangles for Area:</strong>
           <br>&bull; Block A: <code>8 &times; 4 = 32 m&sup2;</code>.
           <br>&bull; Block B: <code>6 &times; 3 = 18 m&sup2;</code>.
           <br>&bull; Total Area: <code>32 + 18 = 50 m&sup2;</code>.""",
         "A compound workshop floor is composed of a rectangle <strong>12m &times; 8m</strong> with an internal rectangular cutout <strong>4m &times; 3m</strong> removed from one corner. Calculate the remaining floor area.",
         """1. Total outer area: <code>12 &times; 8 = 96 m&sup2;</code>.<br>2. Area of corner cutout: <code>4 &times; 3 = 12 m&sup2;</code>.<br>3. Remaining area: <code>96 - 12 = 84 m&sup2;</code>.<br><strong>Floor Area: 84 m&sup2;</strong>.""",
         "Count the sides! An L-shape has 6 sides. Make sure you have 6 numbers when calculating perimeter.",
         "To find compound area: either split into two smaller rectangles and ADD, or treat as one large rectangle and SUBTRACT the cutout.",
         [
           ("An L-shaped lawn has edges 9m, 7m, 3m, 4m, 6m, 3m. Calculate the total perimeter.", "[2 Marks]"),
           ("Calculate the area of an L-shape formed by a 10m &times; 6m rectangle joined to a 4m &times; 5m rectangle.", "[2 Marks]"),
           ("Turf costs £6.50 per m&sup2;. Calculate the cost to turf a 48 m&sup2; lawn.", "[2 Marks]"),
           ("Explain how to find the missing horizontal width of an L-shape if the overall base is 14m and the top width is 6m.", "[1 Mark]")
         ]),

        # Mode M19
        ("Mode M19: Circle Geometry &ndash; Radius vs Diameter", "Diagnostic Geometry &bull; Level 2 Threshold",
         """Diagnostics state the diameter (e.g. 1.6m) and candidates square 1.6 directly in &pi;r&sup2;, over-calculating circle area by a factor of 4!""",
         """<strong>The Algorithmic Failure Trap:</strong><br>
         <em>A circular hot tub has diameter 2 m. Calculate its surface area (&pi; = 3.14).</em><br>
         &bull; <strong>The Trap Distractor:</strong> 3.14 &times; 2&sup2; = 12.56 m&sup2; (squared the diameter!).<br>
         <strong>Why It Fails:</strong> Formula is &pi;r&sup2;, NOT &pi;d&sup2;! Radius is half the diameter: <code>r = 2 &divide; 2 = 1 m</code>.<br><br>
         <strong>The Tutor Golden Rule:</strong><br>
         1. Always write down radius first: <code>Radius = Diameter &divide; 2</code>.<br>
         2. <strong>Area:</strong> <code>&pi; &times; r &times; r = 3.14 &times; 1&sup2; = 3.14 m&sup2;</code>.<br>
         3. <strong>Circumference (Perimeter):</strong> <code>&pi; &times; d = 3.14 &times; 2 = 6.28 m</code>.""",
         "A circular roundabout has <strong>diameter 12 metres</strong>. Calculate its circumference and area (use &pi; = 3.142).",
         """1. Radius = <code>12 &divide; 2 = 6 metres</code>.<br>2. Circumference: <code>&pi; &times; d = 3.142 &times; 12 = 37.704 metres</code>.<br>3. Area: <code>&pi; &times; r&sup2; = 3.142 &times; 6&sup2; = 3.142 &times; 36 = 113.112 m&sup2;</code>.<br><strong>Circumference: 37.7 m &bull; Area: 113.1 m&sup2;</strong>.""",
         "Before touching the calculator, write: d = ... and r = ... to ensure you never square the diameter.",
         "Circumference uses diameter (&pi;d); Area uses radius squared (&pi;r&sup2;).",
         [
           ("A circular pizza has diameter 30 cm. Calculate its area (use &pi; = 3.14).", "[2 Marks]"),
           ("A bicycle wheel has radius 35 cm. Calculate the distance travelled in one full revolution (Circumference).", "[2 Marks]"),
           ("Calculate the perimeter of a semicircle with diameter 14 cm. (Include the straight diameter edge!).", "[2 Marks]"),
           ("Explain why squaring diameter instead of radius makes the calculated area 4 times too large.", "[2 Marks]")
         ]),

        # Mode M20
        ("Mode M20: Volume &amp; Capacity of Prisms &amp; Cylinders", "Diagnostic Geometry &bull; Level 2 Threshold",
         """Learners confuse 2D area with 3D volume, or fail to convert cubic metres to litres (1 m&sup3; = 1,000 litres).""",
         """<strong>The Algorithmic Failure Trap:</strong><br>
         <em>A water tank measures 2m by 1.5m by 1.2m. How many litres of water does it hold?</em><br>
         &bull; <strong>The Trap Distractor:</strong> 3.6 litres (forgot that 1 m&sup3; = 1,000 litres, not 1 litre!).<br>
         <strong>Why It Fails:</strong> 1 cubic metre contains 1,000 litres of water!<br><br>
         <strong>The Tutor Golden Rule:</strong><br>
         1. Cuboid Volume: <code>length &times; width &times; height = 2 &times; 1.5 &times; 1.2 = 3.6 m&sup3;</code>.<br>
         2. Convert to litres: <code>3.6 &times; 1,000 = 3,600 litres</code>.<br>
         3. Cylinder Volume: <code>&pi;r&sup2;h</code> (Area of circular cross-section &times; height).""",
         "A cylindrical oil barrel has <strong>radius 0.4 m</strong> and <strong>height 1.2 m</strong>. Calculate its volume in litres (use &pi; = 3.142).",
         """1. Cross-section area: <code>&pi;r&sup2; = 3.142 &times; 0.4&sup2; = 3.142 &times; 0.16 = 0.50272 m&sup2;</code>.<br>2. Volume: <code>Area &times; height = 0.50272 &times; 1.2 = 0.603264 m&sup3;</code>.<br>3. Litres: <code>0.603264 &times; 1,000 = 603.3 litres</code>.<br><strong>Capacity: 603.3 litres (or 603 litres)</strong>.""",
         "1 m&sup3; = 1,000 litres. 1 litre = 1,000 ml = 1,000 cm&sup3;.",
         "Cylinder volume formula is always: &pi; &times; r&sup2; &times; h.",
         [
           ("A fish tank measures 80 cm by 40 cm by 50 cm. Find its volume in litres (1,000 cm&sup3; = 1 litre).", "[2 Marks]"),
           ("A cylindrical silo has diameter 4 m and height 10 m. Calculate its volume in m&sup3; (&pi; = 3.142).", "[2 Marks]"),
           ("A swimming pool holds 120 m&sup3; of water. How many litres is this?", "[1 Mark]"),
           ("State the formula for the volume of a triangular prism.", "[1 Mark]")
         ]),

        # Mode M21
        ("Mode M21: Metric Area &amp; Volume Conversions", "Diagnostic Measures &bull; Level 2 Threshold",
         """The single most failed question in Functional Skills Maths: converting square metres to square centimetres (dividing by 100 instead of 10,000).""",
         """<strong>The Algorithmic Failure Trap:</strong><br>
         <em>Convert 4 square metres (m&sup2;) to square centimetres (cm&sup2;).</em><br>
         &bull; <strong>The Trap Distractor:</strong> 400 cm&sup2; (multiplied by 100 because 1 m = 100 cm).<br>
         <strong>Why It Fails:</strong> 1 m&sup2; is 100 cm &times; 100 cm = 10,000 cm&sup2;! Linear conversion does not apply to areas.<br><br>
         <strong>The Tutor Golden Rule:</strong><br>
         1. <strong>Linear:</strong> 1 m = 100 cm.<br>
         2. <strong>Area (Squared):</strong> <code>1 m&sup2; = 100 &times; 100 = 10,000 cm&sup2;</code>.<br>
         3. <strong>Volume (Cubed):</strong> <code>1 m&sup3; = 100 &times; 100 &times; 100 = 1,000,000 cm&sup3;</code>.<br>
         &bull; <code>4 m&sup2; = 4 &times; 10,000 = 40,000 cm&sup2;</code>.""",
         "A mosaic tile is <strong>20 cm by 20 cm</strong>. A patio has area <strong>18 m&sup2;</strong>. How many tiles are needed to pave the patio?",
         """1. Tile area: <code>20 &times; 20 = 400 cm&sup2;</code>.<br>2. Convert patio area to cm&sup2;: <code>18 m&sup2; &times; 10,000 = 180,000 cm&sup2;</code>.<br>3. Tiles needed: <code>180,000 &divide; 400 = 450 tiles</code>.<br><em>Alternative method:</em> Tile = 0.2m &times; 0.2m = 0.04 m&sup2; &rarr; 18 &divide; 0.04 = 450 tiles.<br><strong>Answer: 450 tiles</strong>.""",
         "Always square the linear conversion factor for area (100&sup2; = 10,000) and cube it for volume (100&sup3; = 1,000,000).",
         "It is usually much easier to convert all measurements to metres BEFORE calculating area!",
         [
           ("Convert 3.5 m&sup2; to cm&sup2;.", "[2 Marks]"),
           ("Convert 50,000 cm&sup2; to m&sup2;.", "[2 Marks]"),
           ("A small tile is 10 cm &times; 10 cm. How many tiles cover a wall of 6 m&sup2;?", "[2 Marks]"),
           ("Explain why 1 cubic metre equals 1,000,000 cubic centimetres, not 100 cm&sup3;.", "[2 Marks]")
         ]),

        # Mode M22
        ("Mode M22: Speed, Distance &amp; Time (Decimal Hours)", "Diagnostic Measures &bull; Level 2 Threshold",
         """Learners write 2 hours 45 minutes as 2.45 hours on their calculator, resulting in major speed and distance errors.""",
         """<strong>The Algorithmic Failure Trap:</strong><br>
         <em>A driver travels 140 miles in 2 hours and 30 minutes. Calculate average speed.</em><br>
         &bull; <strong>The Trap Distractor:</strong> 60.87 mph (entered 140 &divide; 2.30 on calculator).<br>
         <strong>Why It Fails:</strong> 30 minutes is half an hour = 0.5 hours! 2h 30m = 2.5 hours.<br><br>
         <strong>The Tutor Golden Rule (Converting Minutes to Decimal Hours):</strong><br>
         1. Divide minutes by 60: <code>minutes &divide; 60</code>.<br>
           &bull; 15 mins = 0.25 hrs &bull; 30 mins = 0.5 hrs &bull; 45 mins = 0.75 hrs<br>
           &bull; 24 mins = 24/60 = 0.4 hrs &bull; 18 mins = 18/60 = 0.3 hrs.<br>
         2. Speed formula: <code>Speed = Distance &divide; Time (decimal)</code>.<br>
         &bull; <code>140 &divide; 2.5 = 56 mph</code>.""",
         "A courier drives <strong>168 miles</strong> at an average speed of <strong>48 mph</strong>. How long does the journey take in hours and minutes?",
         """1. Time = <code>Distance &divide; Speed = 168 &divide; 48 = 3.5 hours</code>.<br>2. Convert decimal to minutes: <code>0.5 &times; 60 = 30 minutes</code>.<br><strong>Journey Time: 3 hours 30 minutes</strong>.""",
         "NEVER use hours.minutes on a calculator! 1 hour 45 mins is 1.75 hours, NOT 1.45 hours.",
         "To convert decimal hours to minutes: multiply the decimal part by 60 (e.g. 0.35 &times; 60 = 21 mins).",
         [
           ("A train travels 210 miles in 2 hours 45 minutes. Calculate its average speed in mph.", "[2 Marks]"),
           ("Convert 3.6 hours into hours and minutes.", "[2 Marks]"),
           ("A van travels at 55 mph for 4 hours and 12 minutes. How far does it travel?", "[2 Marks]"),
           ("Explain why 2 hours 15 minutes is 2.25 hours, not 2.15 hours.", "[1 Mark]")
         ]),

        # Mode M23
        ("Mode M23: Compound Measures &ndash; Density &amp; Mass", "Diagnostic Measures &bull; Level 2 Threshold",
         """Diagnostics present density and mass calculations. Learners confuse which variable to divide or multiply.""",
         """<strong>The Algorithmic Failure Trap:</strong><br>
         <em>A block of oak has volume 400 cm&sup3; and mass 320 grams. Find its density.</em><br>
         &bull; <strong>The Trap Distractor:</strong> 1.25 g/cm&sup3; (divided volume by mass: 400 &divide; 320).<br>
         <strong>Why It Fails:</strong> Density is Mass per unit Volume: <code>Density = Mass &divide; Volume</code>!<br><br>
         <strong>The Tutor Golden Rule (The DMV Triangle):</strong><br>
         1. Cover <strong>D</strong> (Density): <code>Density = Mass &divide; Volume</code>.<br>
         2. Cover <strong>M</strong> (Mass): <code>Mass = Density &times; Volume</code>.<br>
         3. Cover <strong>V</strong> (Volume): <code>Volume = Mass &divide; Density</code>.<br>
         &bull; <code>Density = 320 &divide; 400 = 0.8 g/cm&sup3;</code>.""",
         "A steel girder has volume <strong>0.25 m&sup3;</strong>. Steel has a density of <strong>7,850 kg/m&sup3;</strong>. Calculate the mass of the girder in tonnes.",
         """1. Mass = <code>Density &times; Volume = 7,850 &times; 0.25 = 1,962.5 kg</code>.<br>2. Convert to tonnes: <code>1,962.5 &divide; 1,000 = 1.9625 tonnes</code>.<br><strong>Mass: 1.96 tonnes</strong>.""",
         "Look at the units for the formula clue: 'kg/m&sup3;' means kilograms (mass) divided by cubic metres (volume).",
         "Check sensible weights: a steel girder cannot weigh 0.0003 tonnes or 50,000 tonnes!",
         [
           ("A concrete block has volume 0.05 m&sup3; and mass 115 kg. Calculate its density in kg/m&sup3;.", "[2 Marks]"),
           ("Gold has a density of 19.3 g/cm&sup3;. What is the mass of a gold bar with volume 50 cm&sup3;?", "[2 Marks]"),
           ("A liquid has density 0.9 kg/litre. What volume does 18 kg of liquid occupy?", "[2 Marks]"),
           ("What formula connects Pressure, Force, and Area?", "[1 Mark]")
         ]),

        # Mode M24
        ("Mode M24: Pythagoras' Theorem &amp; Slopes", "Diagnostic Geometry &bull; Level 2 Threshold",
         """Diagnostics present right-angled triangles in roofing, ramps, and ladders. Learners add squares when finding a shorter side instead of subtracting.""",
         """<strong>The Algorithmic Failure Trap:</strong><br>
         <em>A ladder of length 5m rests against a wall. The foot of the ladder is 3m from the wall. How high up the wall does it reach?</em><br>
         &bull; <strong>The Trap Distractor:</strong> 5.83m (added 5&sup2; + 3&sup2; = 25 + 9 = 34 &rarr; &radic;34 = 5.83).<br>
         <strong>Why It Fails:</strong> 5m is the HYPOTENUSE (longest side). When finding a shorter side, you must SUBTRACT!<br><br>
         <strong>The Tutor Golden Rule:</strong><br>
         1. Finding the Hypotenuse (c): <code>c&sup2; = a&sup2; + b&sup2; &rarr; c = &radic;(a&sup2; + b&sup2;)</code>.<br>
         2. Finding a Shorter Side (a): <code>a&sup2; = c&sup2; - b&sup2; &rarr; a = &radic;(c&sup2; - b&sup2;)</code>.<br>
         &bull; <code>Wall height = &radic;(5&sup2; - 3&sup2;) = &radic;(25 - 9) = &radic;16 = 4 metres</code>.""",
         "A wheelchair access ramp has a horizontal run of <strong>6 metres</strong> and rises vertically by <strong>0.8 metres</strong>. Calculate the sloping length of the ramp.",
         """1. Ramp slope is the hypotenuse: <code>c&sup2; = a&sup2; + b&sup2;</code>.<br>2. <code>c&sup2; = 6&sup2; + 0.8&sup2; = 36 + 0.64 = 36.64</code>.<br>3. <code>c = &radic;36.64 = 6.053 metres</code>.<br><strong>Ramp Length: 6.05 metres</strong>.""",
         "The hypotenuse is ALWAYS the side opposite the 90-degree right angle and is always the longest side.",
         "If your calculated wall height is longer than the ladder itself, you mistakenly added instead of subtracting!",
         [
           ("A right-angled triangle has base 8 cm and height 15 cm. Calculate the hypotenuse length.", "[2 Marks]"),
           ("A 10m flagpole has a support wire anchored 6m from its base. How long is the wire?", "[2 Marks]"),
           ("A roof truss has a slope length of 6.5m and horizontal span of 6m. Calculate the vertical height.", "[2 Marks]"),
           ("Explain how to identify the hypotenuse on any right-angled triangle.", "[1 Mark]")
         ]),

        # Mode M25
        ("Mode M25: Mean from Grouped Frequency Tables", "Diagnostic Data &bull; Level 2 Threshold",
         """Over 75% of candidates average the class intervals or average the frequencies directly, scoring 0 marks.""",
         """<strong>The Algorithmic Failure Trap:</strong><br>
         <em>Times (mins): 0-10 (4), 10-20 (12), 20-30 (16), 30-40 (8). Calculate the estimated mean.</em><br>
         &bull; <strong>The Trap Distractor:</strong> (4 + 12 + 16 + 8) &divide; 4 = 10 (calculated average frequency).<br>
         <strong>Why It Fails:</strong> You must calculate midpoints and multiply by frequencies: <code>&Sigma;(fx) &divide; &Sigma;f</code>!<br><br>
         <strong>The Tutor Golden Rule:</strong><br>
         1. Find the <strong>Midpoint (x)</strong> of each interval: <code>(Lower + Upper) &divide; 2</code> (5, 15, 25, 35).<br>
         2. Multiply Midpoint &times; Frequency: <code>fx = (5&times;4=20), (15&times;12=180), (25&times;16=400), (35&times;8=280)</code>.<br>
         3. Sum all fx products: <code>&Sigma;fx = 20 + 180 + 400 + 280 = 880</code>.<br>
         4. Divide by total frequency: <code>880 &divide; 40 = 22 minutes</code>.""",
         "Test scores: 1-5 (2 students), 6-10 (6 students), 11-15 (14 students), 16-20 (8 students). Calculate estimated mean.",
         """1. Midpoints: 3, 8, 13, 18.<br>2. Products (fx): (3&times;2=6); (8&times;6=48); (13&times;14=182); (18&times;8=144).<br>3. &Sigma;fx = 6 + 48 + 182 + 144 = 380.<br>4. Total students (&Sigma;f) = 2 + 6 + 14 + 8 = 30.<br>5. Estimated Mean = <code>380 &divide; 30 = 12.67 (or 12.7)</code>.<br><strong>Estimated Mean: 12.7 marks</strong>.""",
         "Never divide by the number of rows in the table! Always divide by the TOTAL FREQUENCY (&Sigma;f).",
         "Check your answer: the mean MUST fall within the range of the table (between 1 and 20).",
         [
           ("Delivery times: 0–9 mins (5), 10–19 mins (15), 20–29 mins (20), 30–39 mins (10). Calculate estimated mean.", "[3 Marks]"),
           ("Find the midpoint of the group '£40 to £59'.", "[1 Mark]"),
           ("Why is the mean calculated from a grouped table called an 'estimate'?", "[1 Mark]"),
           ("State the modal group from the table in Question 1.", "[1 Mark]")
         ]),

        # Mode M26
        ("Mode M26: Comparing Data &ndash; Mean vs Range", "Diagnostic Data &bull; Level 2 Threshold",
         """Diagnostics present two data sets and ask for a comparison. Candidates state numbers without interpreting what they mean in reality.""",
         """<strong>The Algorithmic Failure Trap:</strong><br>
         <em>Shift A: Mean = 45, Range = 12. Shift B: Mean = 52, Range = 28. Compare the two shifts.</em><br>
         &bull; <strong>The Trap Distractor:</strong> Writing only 'Shift B has mean 52 and Shift A has range 12'.<br>
         <strong>Why It Fails:</strong> Awarding bodies award zero marks for just copying numbers! You must use comparative language.<br><br>
         <strong>The Tutor Golden Rule:</strong><br>
         1. <strong>Compare the Averages (Mean/Median):</strong>
           <br>&bull; Shift B has a higher average output than Shift A (52 vs 45).
         2. <strong>Compare the Consistency / Variation (Range):</strong>
           <br>&bull; Shift A is more consistent / less variable than Shift B because its range is smaller (12 vs 28).""",
         "Branch North: Mean sales = £1,450, Range = £280. Branch South: Mean sales = £1,420, Range = £650. Compare the performance and consistency of the branches.",
         """1. <strong>Average:</strong> Branch North achieved slightly higher average sales on average (£1,450 vs £1,420).<br>2. <strong>Consistency:</strong> Branch North was significantly more consistent and reliable in its daily sales than Branch South because its range was much smaller (£280 vs £650).<br><strong>Verdict: Branch North performed better overall.</strong>""",
         "A smaller range ALWAYS means MORE consistent, more reliable, and less spread out.",
         "You must make TWO comparative statements: one comparing the average and one comparing the spread/range.",
         [
           ("Machine A: Mean cycle = 18.2s, Range = 1.4s. Machine B: Mean cycle = 18.4s, Range = 4.8s. Compare the two machines.", "[3 Marks]"),
           ("Calculate the range of these figures: 14, 28, 9, 35, 22, 41, 16.", "[1 Mark]"),
           ("Explain why a low range is desirable in manufacturing component dimensions.", "[1 Mark]"),
           ("What does the median tell you about a data set?", "[1 Mark]")
         ]),

        # Mode M27
        ("Mode M27: Combined Probability &amp; Tree Diagrams", "Diagnostic Data &bull; Level 2 Threshold",
         """Candidates add probabilities for consecutive independent events instead of multiplying them.""",
         """<strong>The Algorithmic Failure Trap:</strong><br>
         <em>A coin is flipped and a standard 6-sided die is rolled. What is the probability of getting a Head and a 6?</em><br>
         &bull; <strong>The Trap Distractor:</strong> 1/2 + 1/6 = 4/6 = 2/3 (added probabilities).<br>
         <strong>Why It Fails:</strong> Getting both events combined is LESS likely than either one alone! You must MULTIPLY probabilities.<br><br>
         <strong>The Tutor Golden Rule (The Product Rule for Independent Events):</strong><br>
         1. Probability of Head: <code>P(H) = 1/2</code>.<br>
         2. Probability of rolling a 6: <code>P(6) = 1/6</code>.<br>
         3. Combined probability: <code>P(H and 6) = 1/2 &times; 1/6 = 1/12</code>.<br>
         4. For decimal probabilities: <code>0.9 &times; 0.8 = 0.72</code>.""",
         "Two machines operate independently. Machine 1 has a <strong>0.95</strong> probability of passing inspection. Machine 2 has a <strong>0.90</strong> probability. What is the probability that <strong>BOTH pass</strong>?",
         """1. Both pass: <code>P(Both) = 0.95 &times; 0.90</code>.<br>2. Multiply: <code>0.95 &times; 0.90 = 0.855 (or 85.5%)</code>.<br>3. Probability that at least one fails: <code>1 - 0.855 = 0.145 (or 14.5%)</code>.<br><strong>Probability both pass: 0.855</strong>.""",
         "The AND rule means MULTIPLY: P(A and B) = P(A) &times; P(B).",
         "Probabilities can NEVER exceed 1 (or 100%). If your answer is greater than 1, you added when you should have multiplied!",
         [
           ("A bag contains 3 red balls and 5 blue balls. A ball is drawn and replaced. A second ball is drawn. Find P(Blue, Blue).", "[2 Marks]"),
           ("The probability of rain on Saturday is 0.4 and on Sunday is 0.3. What is the probability that it rains on both days?", "[2 Marks]"),
           ("What is the probability of rolling two sixes on a pair of fair dice?", "[2 Marks]"),
           ("Explain why the combined probability of two independent events is smaller than either individual probability.", "[1 Mark]")
         ]),

        # Mode E28
        ("Mode E28: Comma Splices &amp; Sentence Boundaries", "Diagnostic SPaG &bull; Level 2 Threshold",
         """In English diagnostic screening, comma splices are the #1 reason candidates fail Level 2 SPaG threshold tests.""",
         """<strong>The Algorithmic Failure Trap:</strong><br>
         <em>Identify the grammatically correct sentence:</em><br>
         &bull; <strong>Option A:</strong> The report is finished, I will email it now.<br>
         &bull; <strong>Option B:</strong> The report is finished; I will email it now.<br>
         &bull; <strong>The Trap Distractor:</strong> Option A (the comma splice).<br>
         <strong>Why It Fails:</strong> A comma cannot link two independent complete sentences!<br><br>
         <strong>The Tutor Golden Rule (3 Ways to Fix a Comma Splice):</strong><br>
         1. <strong>Use a Full Stop:</strong> <em>The report is finished. I will email it now.</em><br>
         2. <strong>Use a Semicolon:</strong> <em>The report is finished; I will email it now.</em><br>
         3. <strong>Use a Coordinating Conjunction:</strong> <em>The report is finished, and I will email it now.</em>""",
         "Correct this sentence: <em>'The meeting was postponed, the director was unwell.'</em>",
         """1. Semicolon fix: <code>The meeting was postponed; the director was unwell.</code><br>2. Conjunction fix: <code>The meeting was postponed because the director was unwell.</code><br>3. Connective fix: <code>The meeting was postponed; consequently, we rescheduled the presentation.</code>""",
         "If both parts of your sentence could stand alone as complete sentences with their own subject and verb, do NOT join them with a simple comma!",
         "Semicolons link two closely related complete thoughts without needing a conjunction.",
         [
           ("Fix this comma splice using a semicolon: 'The warehouse was closed, deliveries were delayed.'", "[1 Mark]"),
           ("Fix this sentence using a coordinating conjunction: 'She wanted to apply for the apprenticeship, she lacked the paperwork.'", "[1 Mark]"),
           ("Explain what a 'comma splice' is.", "[2 Marks]"),
           ("Identify which punctuation mark correctly completes: 'The training course was intense ____ however, it was rewarding.'", "[1 Mark]")
         ]),

        # Mode E29
        ("Mode E29: Apostrophes &ndash; Omission vs Possession", "Diagnostic SPaG &bull; Level 2 Threshold",
         """Learners routinely confuse 'its' and 'it's', or add apostrophes to simple plural nouns (the 'greengrocer's apostrophe').""",
         """<strong>The Algorithmic Failure Trap:</strong><br>
         <em>The company updated (its / it's) website because (its / it's) launching a new app.</em><br>
         &bull; <strong>The Trap Distractor:</strong> 'The company updated it's website...'<br>
         <strong>Why It Fails:</strong> 'its' is a possessive pronoun (like 'his' or 'her'). 'it's' ONLY means 'it is' or 'it has'!<br><br>
         <strong>The Tutor Golden Rule:</strong><br>
         1. <strong>The 'It Is' Test:</strong> Replace the word with 'it is'. If it makes sense, use <strong>it's</strong>. If it does not make sense, use <strong>its</strong>.<br>
         2. <strong>Singular Possession:</strong> <em>the worker's badge</em> (one worker).<br>
         3. <strong>Plural Possession:</strong> <em>the workers' badges</em> (multiple workers &rarr; apostrophe after the s).<br>
         4. <strong>Never use apostrophes for simple plurals:</strong> <em>Two laptops</em>, NOT <em>Two laptop's</em>!""",
         "Insert apostrophes correctly: <em>The managers assistant checked the three trainees files before its too late.</em>",
         """1. Manager's assistant: singular possession &rarr; <code>manager's</code>.<br>2. Trainees' files: plural possession &rarr; <code>trainees'</code>.<br>3. Before it's too late: it is too late &rarr; <code>it's</code>.<br><strong>Corrected:</strong> <em>The manager's assistant checked the three trainees' files before it's too late.</em>""",
         "Plural words ending in 's' take the apostrophe AFTER the 's': 'all the teachers' cars'.",
         "Never write 'apple's and banana's' &mdash; plurals NEVER take apostrophes!",
         [
           ("Choose the correct word: 'The dog wagged (its / it's) tail.' Explain your choice.", "[2 Marks]"),
           ("Correct this sentence: 'The client's arrived with three box's of document's.'", "[2 Marks]"),
           ("Where does the apostrophe go in: 'The doctors surgeries were newly renovated' (referring to multiple doctors)?", "[1 Mark]"),
           ("State the two words contracted in: 'they've' and 'who's'.", "[2 Marks]")
         ]),

        # Mode E30
        ("Mode E30: Subject-Verb Agreement with Collective Nouns", "Diagnostic SPaG &bull; Level 2 Threshold",
         """BKSB diagnostics test tricky subject-verb agreement where words separate the subject from the verb, or with indefinite pronouns like 'everyone'.""",
         """<strong>The Algorithmic Failure Trap:</strong><br>
         <em>A box of heavy industrial tools (was / were) delivered to the workshop yesterday.</em><br>
         &bull; <strong>The Trap Distractor:</strong> 'were' (mistakenly agreed with the nearest plural noun 'tools').<br>
         <strong>Why It Fails:</strong> The true grammatical subject is singular: 'A BOX', not 'tools'!<br><br>
         <strong>The Tutor Golden Rule:</strong><br>
         1. Ignore the prepositional phrase ('of heavy industrial tools').<br>
         2. Check the real subject: <code>A box [was] delivered</code>.<br>
         3. <strong>Indefinite Pronouns:</strong> <em>Everyone, everybody, neither, each, anyone</em> are grammatically <strong>SINGULAR</strong>:
           <br>&bull; <em>'Everyone is ready'</em> (NOT <em>'Everyone are ready'</em>).
           <br>&bull; <em>'Neither of the managers was available'</em> (NOT <em>'were available'</em>).""",
         "Select the correct verb: <em>Each of the new apprentice candidates (has / have) completed their initial diagnostic test.</em>",
         """1. Ignore 'of the new apprentice candidates'.<br>2. The subject is <strong>'Each'</strong> (singular pronoun).<br>3. Correct verb is <strong>has</strong>.<br><strong>Corrected:</strong> <em>Each of the new apprentice candidates <strong>has</strong> completed their initial diagnostic test.</em>""",
         "Watch out for words that come between the subject and verb! Identify the core noun first.",
         "'Everyone', 'Neither', and 'Each' take singular verbs (is, has, was).",
         [
           ("Choose the correct verb: 'A team of experienced auditors (was / were) inspecting the site.'", "[1 Mark]"),
           ("Choose the correct verb: 'Neither of the laptops (is / are) connecting to the Wi-Fi network.'", "[1 Mark]"),
           ("Choose the correct verb: 'The collection of rare books (has / have) been catalogued.'", "[1 Mark]"),
           ("Explain why 'The group of students were loud' is grammatically incorrect in formal English.", "[2 Marks]")
         ])
    ]

    for m_idx, (m_title, strand, trap_desc, trap_anatomy, exam_q, model_sol, pitfall, tip, retry_drills) in enumerate(bksb_modes_data, 1):
        # 2 Pages per Failure Mode: Pages 4 to 63
        base_page = 4 + (m_idx - 1) * 2

        # Mode Page 1: Algorithmic Failure Trap & Tutor Golden Rule
        pages.append(f"""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; BKSB Remediation</div>
    <div class="page-header-strand">{strand}</div>
  </div>

  <h2>{m_title}</h2>
  <div class="card-trap" style="margin-bottom:6px;">
    <strong>The Diagnostic Misconception:</strong><br>
    {trap_desc}
  </div>

  <div class="card-concept" style="margin-bottom:6px;">
    {trap_anatomy}
  </div>

  <div class="card-exam" style="margin-bottom:6px;">
    <h3 style="color:#7c3aed; margin-top:0;">Model Diagnostic Screen &bull; Remediation Walkthrough</h3>
    <p style="margin:2px 0;"><strong>Problem:</strong> {exam_q}</p>
    <div style="background:#ffffff; border:1px solid #e9d5ff; padding:5px 8px; border-radius:4px; font-size:7.8pt;">
      {model_sol}
    </div>
  </div>

  <div class="grid-2" style="margin-top:auto;">
    <div class="card-trap" style="margin-bottom:0;">
      <strong>Exam Hall Trap:</strong> {pitfall}
    </div>
    <div class="card-tip" style="margin-bottom:0;">
      <strong>Tutor Golden Rule:</strong> {tip}
    </div>
  </div>

  <div class="page-footer">
    <div>Diagnostic Failure Mode {m_idx} &bull; Analysis &amp; Golden Rules</div>
    <div class="page-num">Page {base_page}</div>
  </div>
</div>
""")

        # Mode Page 2: Two-Stage Retry Drills & Independent Workspace
        retry_html = ""
        for r_idx, (r_q, r_marks) in enumerate(retry_drills, 1):
            retry_html += f"""
<div style="margin-bottom:8px;">
  <div style="display:flex; justify-content:space-between;"><strong>Stage 2 Drill {r_idx}:</strong> <span class="mark-badge" style="background:#1d4ed8;">{r_marks}</span></div>
  <p style="margin:2px 0 4px 0; font-size:8pt;">{r_q}</p>
  <div class="workspace-ruled" style="min-height:50px;">Show working and bust the trap here...</div>
</div>
"""

        pages.append(f"""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; BKSB Remediation</div>
    <div class="page-header-strand">{strand} &bull; Stage 2 Retry Drills</div>
  </div>

  <h2>{m_title} &bull; Independent Retry Drills</h2>
  <p style="margin-bottom:8px;">Bust the diagnostic distractors below. Show clear calculations to prove you have mastered the underlying rule.</p>

  {retry_html}

  <div class="card-tip" style="margin-top:auto; display:flex; justify-content:space-between; align-items:center;">
    <div><strong>Diagnostic Gateway Verification:</strong> I can recognize and avoid this failure mode.</div>
    <div style="font-weight:700; color:#1d4ed8;">Mastery Check: [ &nbsp; ] Cleared</div>
  </div>

  <div class="page-footer">
    <div>Diagnostic Failure Mode {m_idx} &bull; Independent Retry Drills</div>
    <div class="page-num">Page {base_page + 1}</div>
  </div>
</div>
""")

    # -------------------------------------------------------------
    # PART II: BKSB DIAGNOSTIC EXIT MILESTONE SIMULATION (4 Pages, Pages 64 to 67)
    # -------------------------------------------------------------
    exit_tests = [
        # Page 64: Exit Items 1 to 8 (Number, BIDMAS & Fractions)
        ("Diagnostic Exit Milestone Simulation &bull; Part 1 (Items 1 to 8)",
         [
           ("Item 1 (Mode M1)", "Round 0.08472 to 2 significant figures. A) 0.08 &nbsp; B) 0.084 &nbsp; C) 0.085 &nbsp; D) 0.09"),
           ("Item 2 (Mode M2)", "At 02:00, the temperature was -8&deg;C. By midday, it had risen by 14&deg;C. What was the temperature at midday?"),
           ("Item 3 (Mode M3)", "Calculate: <code>24 - 3 &times; (5 - 1)&sup2; &divide; 6</code> following order of operations."),
           ("Item 4 (Mode M4)", "A charity raises £1,800. It spends 1/3 on marketing and 3/5 of the remainder on medical supplies. How much remains?"),
           ("Item 5 (Mode M5)", "Evaluate: <code>3 2/3 - 1 3/4</code>. Give your answer as a mixed number in simplest form."),
           ("Item 6 (Mode M6)", "A catering pack contains 6 3/4 kg of rice. Each portion requires 3/8 kg. How many full portions can be served?"),
           ("Item 7 (Mode M7)", "Calculate: <code>0.45 &times; 0.08</code> without using a calculator."),
           ("Item 8 (Mode M8)", "Calculate: <code>7.2 &divide; 0.16</code>. Show your method.")
         ]),

        # Page 65: Exit Items 9 to 16 (Decimals, Percentages & Ratio)
        ("Diagnostic Exit Milestone Simulation &bull; Part 2 (Items 9 to 16)",
         [
           ("Item 9 (Mode M9)", "A mechanic works for 2 hours and 40 minutes at £36 per hour. Calculate total labour charges."),
           ("Item 10 (Mode M10)", "A television is sold for £408 in a 15% discount sale. What was the original price before the sale?"),
           ("Item 11 (Mode M11)", "A company's monthly turnover increased from £48,000 to £55,200. Calculate the percentage increase."),
           ("Item 12 (Mode M12)", "£6,000 is invested in a bond yielding 4% compound interest annually. Find the value after 2 years."),
           ("Item 13 (Mode M13)", "Option A: 400g coffee for £3.20. Option B: 650g coffee for £4.80. Which option offers better value per 100g?"),
           ("Item 14 (Mode M14)", "A grant is shared between Youth Club and Sports Club in ratio 4 : 5. Sports Club receives £750. What is the total grant?"),
           ("Item 15 (Mode M15)", "12 identical machine parts weigh 54 kg. What is the weight of 20 identical parts?"),
           ("Item 16 (Mode M16)", "6 painters take 8 days to paint an office complex. How many days would 4 painters take at the same pace?")
         ]),

        # Page 66: Exit Items 17 to 24 (Geometry, Measures & Pythagoras)
        ("Diagnostic Exit Milestone Simulation &bull; Part 3 (Items 17 to 24)",
         [
           ("Item 17 (Mode M17)", "On a 1 : 100 site plan, a garden pond is 8.5 cm long. What is the actual length of the pond in metres?"),
           ("Item 18 (Mode M18)", "An L-shaped room has outer dimensions 12m by 9m, with a corner section 5m by 4m removed. Find the floor area."),
           ("Item 19 (Mode M19)", "A circular patio has diameter 4.2 metres. Calculate its area (use &pi; = 3.142)."),
           ("Item 20 (Mode M20)", "A water tank is a cylinder with radius 0.6m and height 1.5m. How many litres does it hold? (1 m&sup3; = 1,000L)."),
           ("Item 21 (Mode M21)", "Convert 6.2 m&sup2; into square centimetres (cm&sup2;)."),
           ("Item 22 (Mode M22)", "A driver covers 165 miles in 3 hours and 45 minutes. Calculate average speed in mph."),
           ("Item 23 (Mode M23)", "A metal casting has volume 250 cm&sup3; and mass 2.125 kg. Calculate its density in g/cm&sup3;."),
           ("Item 24 (Mode M24)", "A ladder 6.5m long leans against a vertical wall with its base 2.5m away. How high up the wall does it reach?")
         ]),

        # Page 67: Exit Items 25 to 30 (Data, Probability & SPaG)
        ("Diagnostic Exit Milestone Simulation &bull; Part 4 (Items 25 to 30)",
         [
           ("Item 25 (Mode M25)", "Delivery times: 0–9 mins (6), 10–19 mins (14), 20–29 mins (16), 30–39 mins (4). Calculate estimated mean time."),
           ("Item 26 (Mode M26)", "Shift 1: Mean = 82, Range = 6. Shift 2: Mean = 84, Range = 22. Compare the output and consistency of both shifts."),
           ("Item 27 (Mode M27)", "Two independent components have reliability rates of 0.96 and 0.90. What is the probability that both function?"),
           ("Item 28 (Mode E28)", "Correct this comma splice: <em>'The system backup completed successfully, the server rebooted automatically.'</em>"),
           ("Item 29 (Mode E29)", "Insert the correct forms of 'its' or 'it\'s': <em>'The company updated _____ policy because _____ committed to safety.'</em>"),
           ("Item 30 (Mode E30)", "Choose the grammatically correct verb: <em>'Neither of the delivery drivers (was / were) available for overtime.'</em>")
         ])
    ]

    for p_offset, (p_title, p_items) in enumerate(exit_tests, 64):
        items_html = ""
        for i_title, i_text in p_items:
            items_html += f"""
<div style="margin-bottom:8px;">
  <div style="display:flex; justify-content:space-between;"><strong>{i_title}:</strong> <span class="mark-badge" style="background:#1d4ed8;">[1 Mark]</span></div>
  <p style="margin:2px 0 4px 0; font-size:7.8pt;">{i_text}</p>
  <div class="workspace-ruled" style="min-height:38px; padding:3px 6px;">Enter final answer and working...</div>
</div>
"""

        pages.append(f"""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Exit Simulation</div>
    <div class="page-header-strand">Full Diagnostic Milestone Assessment</div>
  </div>

  <h2>{p_title}</h2>
  <p style="margin-bottom:6px;">Complete each diagnostic test item under exam conditions. No calculators for Items 1 to 8.</p>

  {items_html}

  <div class="page-footer">
    <div>Diagnostic Exit Simulation &bull; Benchmark Assessment</div>
    <div class="page-num">Page {p_offset}</div>
  </div>
</div>
""")

    # -------------------------------------------------------------
    # PART III: 16 PAGES OF COMPREHENSIVE ANSWER KEYS (Pages 68 to 83)
    # -------------------------------------------------------------
    # Pages 68 to 79: Modes 1 to 30 Answer Keys (12 pages)
    mode_answers = [
        # Page 68: Modes 1 to 3 Answers
        ("Diagnostic Answer Key &bull; Modes M1, M2 &amp; M3",
         """<div class="card-practice" style="padding:5px 8px; margin-bottom:5px; font-size:7.5pt;">
           <strong style="color:#1d4ed8;">Mode M1: Place Value &amp; Significant Figures (Page 5)</strong><br>
           1. 1st non-zero is 5, 2nd is 6. Deciding digit is 2 &rarr; <strong>0.056</strong> [2m].<br>
           2. 1st sig fig is 4. Deciding is 8 (rounds up) &rarr; <strong>50,000</strong> [2m].<br>
           3. 2 d.p. counts positions after decimal point (4.08); 2 sig figs counts first 2 significant digits from left (4.1) [2m].<br>
           4. 45,062 &rarr; rounds to <strong>45,000</strong> [2m].
         </div>
         <div class="card-practice" style="padding:5px 8px; margin-bottom:5px; font-size:7.5pt;">
           <strong style="color:#1d4ed8;">Mode M2: Negative Numbers in Practical Contexts (Page 7)</strong><br>
           1. 18 - (-7) = 18 + 7 = <strong>25&deg;C</strong> [2m].<br>
           2. -18 + 12 = <strong>-6&deg;C</strong> [2m].<br>
           3. -45 - (-18) = -45 + 18 = -27. -27 + (-12) = <strong>-39</strong> [2m].<br>
           4. Distance from -80 to +150: 150 - (-80) = 150 + 80 = <strong>£230</strong> [2m].
         </div>
         <div class="card-practice" style="padding:5px 8px; font-size:7.5pt;">
           <strong style="color:#1d4ed8;">Mode M3: Order of Operations (BIDMAS) (Page 9)</strong><br>
           1. Mult/Div: 6 &times; 5 = 30; 12 &divide; 4 = 3. Add/Sub: 14 + 30 - 3 = <strong>41</strong> [2m].<br>
           2. Brackets: (4+2)=6. Index: 6&sup2;=36. Multiply: 3 &times; 36 = 108. Subtract: 108 - 20 = <strong>88</strong> [2m].<br>
           3. <strong>(5 + 3 &times; 4) - 2</strong>? No: (5 + 3) &times; 4 - 2 = 8 &times; 4 - 2 = 32 - 2 = 30 &rarr; <strong>(5 + 3) &times; 4 - 2 = 30</strong> [2m].<br>
           4. Index: 3&sup3; = 27. Multiply: 2 &times; 27 = 54. Sub: 40 - 54 = <strong>-14</strong> [2m].
         </div>"""),

        # Page 69: Modes 4 to 6 Answers
        ("Diagnostic Answer Key &bull; Modes M4, M5 &amp; M6",
         """<div class="card-practice" style="padding:5px 8px; margin-bottom:5px; font-size:7.5pt;">
           <strong style="color:#1d4ed8;">Mode M4: Multi-Step Fractions of Quantities (Page 11)</strong><br>
           1. White: (360 &divide; 5) &times; 2 = 144. Remainder: 360 - 144 = 216. Wholemeal: 1/3 of 216 = <strong>72 loaves</strong> [2m].<br>
           2. (960 &divide; 8) &times; 5 = 120 &times; 5 = <strong>£600</strong> [2m].<br>
           3. Alex: 1/3 of 2,400 = £800. Remainder = £1,600. Ben: 3/8 of 1,600 = £600. Clara: 1,600 - 600 = <strong>£1,000</strong> [2m].<br>
           4. 2/3 of 60 means (60 &divide; 3) &times; 2 = 40. 60 &divide; 2 &times; 3 = 30 &times; 3 = 90 [2m].
         </div>
         <div class="card-practice" style="padding:5px 8px; margin-bottom:5px; font-size:7.5pt;">
           <strong style="color:#1d4ed8;">Mode M5: Adding &amp; Subtracting Mixed Numbers (Page 13)</strong><br>
           1. 7/3 + 17/5 = 35/15 + 51/15 = 86/15 = <strong>5 11/15</strong> [2m].<br>
           2. 25/6 - 11/4 = 50/12 - 33/12 = 17/12 = <strong>1 5/12</strong> [2m].<br>
           3. 5 - 18/7 = 35/7 - 18/7 = 17/7 = <strong>2 3/7</strong> [2m].<br>
           4. 47 &divide; 8 = 5 remainder 7 &rarr; <strong>5 7/8</strong> [1m].
         </div>
         <div class="card-practice" style="padding:5px 8px; font-size:7.5pt;">
           <strong style="color:#1d4ed8;">Mode M6: Multiplying &amp; Dividing Fractions (Page 15)</strong><br>
           1. (5 &times; 3) / (6 &times; 10) = 15/60 = <strong>1/4</strong> [2m].<br>
           2. 8/3 &divide; 4/9 = 8/3 &times; 9/4 = 72/12 = <strong>6</strong> [2m].<br>
           3. 15/2 &divide; 3/4 = 15/2 &times; 4/3 = 60/6 = <strong>10 full pieces</strong> [2m].<br>
           4. 3/2 &times; 8/3 = 24/6 = <strong>4</strong> [2m].
         </div>"""),

        # Page 70: Modes 7 to 9 Answers
        ("Diagnostic Answer Key &bull; Modes M7, M8 &amp; M9",
         """<div class="card-practice" style="padding:5px 8px; margin-bottom:5px; font-size:7.5pt;">
           <strong style="color:#1d4ed8;">Mode M7: Decimal Multiplication (Page 17)</strong><br>
           1. 7 &times; 9 = 63. Count 3 decimal places (1 in 0.7, 2 in 0.09) &rarr; <strong>0.063</strong> [2m].<br>
           2. 45 &times; 18 = 810. Count 2 places &rarr; <strong>8.10 = 8.1</strong> [2m].<br>
           3. 1.428 &times; 50 = £71.40 [2m].<br>
           4. 0.045 (3 places) + 1.2 (1 place) = <strong>4 decimal places</strong> [1m].
         </div>
         <div class="card-practice" style="padding:5px 8px; margin-bottom:5px; font-size:7.5pt;">
           <strong style="color:#1d4ed8;">Mode M8: Decimal Division (Page 19)</strong><br>
           1. Shift 2 places: 540 &divide; 9 = <strong>60</strong> [2m].<br>
           2. Shift 1 place: 180 &divide; 4 = <strong>45</strong> [2m].<br>
           3. Shift 2 places: 600 &divide; 25 = <strong>24 doses</strong> [2m].<br>
           4. 7.2 / 0.08 = (7.2 &times; 100) / (0.08 &times; 100) = 720 &divide; 8 = 90 [2m].
         </div>
         <div class="card-practice" style="padding:5px 8px; font-size:7.5pt;">
           <strong style="color:#1d4ed8;">Mode M9: Recurring Decimals to Fractions (Page 21)</strong><br>
           1. 625/1000 = divide by 125 &rarr; <strong>5/8</strong> [2m].<br>
           2. 40 mins = 40/60 = 2/3 hr. Total = 3 2/3 hrs = 11/3 hrs. Pay: (11/3) &times; 15 = 11 &times; 5 = <strong>£55.00</strong> [2m].<br>
           3. 7 &divide; 12 = 0.58333... &rarr; <strong>0.583</strong> [2m].<br>
           4. Hours are based on 60 minutes: 40/60 = 4/6 = 0.666... hours, not 0.4 hours (which is 24 mins) [2m].
         </div>"""),

        # Page 71: Modes 10 to 12 Answers
        ("Diagnostic Answer Key &bull; Modes M10, M11 &amp; M12",
         """<div class="card-practice" style="padding:5px 8px; margin-bottom:5px; font-size:7.5pt;">
           <strong style="color:#1d4ed8;">Mode M10: Reverse Percentages (Page 23)</strong><br>
           1. 90% = £162 &rarr; 162 &divide; 0.90 = <strong>£180.00</strong> [2m].<br>
           2. 105% = £25,200 &rarr; 25,200 &divide; 1.05 = <strong>£24,000.00</strong> [2m].<br>
           3. 20% of 80 is £16, giving £96. But 20% of 100 was £20. The percentage was taken off the larger original sum [2m].<br>
           4. 120% = £96 &rarr; 96 &divide; 1.20 = <strong>£80.00</strong> [2m].
         </div>
         <div class="card-practice" style="padding:5px 8px; margin-bottom:5px; font-size:7.5pt;">
           <strong style="color:#1d4ed8;">Mode M11: Percentage Change &amp; Multipliers (Page 25)</strong><br>
           1. a) <strong>&times; 1.18</strong> &bull; b) <strong>&times; 0.88</strong> &bull; c) <strong>&times; 1.06</strong> [3m].<br>
           2. 850 &times; 1.14 = <strong>£969.00</strong> [2m].<br>
           3. Loss = 12,000 - 9,600 = £2,400. % Loss = (2,400 &divide; 12,000) &times; 100 = <strong>20%</strong> [2m].<br>
           4. 100% + 2.5% = 102.5% &rarr; <strong>1.025</strong> [1m].
         </div>
         <div class="card-practice" style="padding:5px 8px; font-size:7.5pt;">
           <strong style="color:#1d4ed8;">Mode M12: Compound Interest &amp; Depreciation (Page 27)</strong><br>
           1. Year 1: 5,000 &times; 1.04 = 5,200. Year 2: 5,200 &times; 1.04 = £5,408. Interest = 5,408 - 5,000 = <strong>£408.00</strong> [2m].<br>
           2. 16,000 &times; (0.80)&sup3; = 16,000 &times; 0.512 = <strong>£8,192.00</strong> [2m].<br>
           3. In compound interest, each year's interest is added to the principal, so subsequent interest is calculated on a growing balance [2m].<br>
           4. <code>2,000 &times; (1.03)&sup4;</code> [1m].
         </div>"""),

        # Page 72: Modes 13 to 15 Answers
        ("Diagnostic Answer Key &bull; Modes M13, M14 &amp; M15",
         """<div class="card-practice" style="padding:5px 8px; margin-bottom:5px; font-size:7.5pt;">
           <strong style="color:#1d4ed8;">Mode M13: Comparing Special Offers (Page 29)</strong><br>
           1. Brand A: 1.80 &divide; 1.5 = £1.20/L. Brand B: 2.30 &divide; 2 = £1.15/L. <strong>Brand B is better value by 5p/L</strong> [2m].<br>
           2. Store A: 80 &times; 0.75 = £60. Store B: 80 - 15 = £65 &rarr; 65 &times; 0.90 = £58.50. <strong>Store B is cheaper by £1.50</strong> [2m].<br>
           3. Two items cost 1 + 0.5 = 1.5 items. Average price per item = 1.5 &divide; 2 = 0.75 (25% off each) [2m].<br>
           4. 116p &divide; 4 = <strong>29p per 100g</strong> [1m].
         </div>
         <div class="card-practice" style="padding:5px 8px; margin-bottom:5px; font-size:7.5pt;">
           <strong style="color:#1d4ed8;">Mode M14: Ratio Sharing &bull; Part-to-Whole (Page 31)</strong><br>
           1. 8 parts = 480 &rarr; 1 part = 60. Shares: 5 &times; 60 = £300, 3 &times; 60 = £180. <strong>£300 : £180</strong> [2m].<br>
           2. Blue = 3 parts = 18 litres &rarr; 1 part = 6 litres. Yellow = 2 &times; 6 = <strong>12 litres</strong> [2m].<br>
           3. Night = 2 parts = 42 &rarr; 1 part = 21. Day = 7 &times; 21 = <strong>147 workers</strong> [2m].<br>
           4. Highest = 5 parts = 6,000 &rarr; 1 part = 1,200. Total = 10 parts &times; 1,200 = <strong>£12,000</strong> [2m].
         </div>
         <div class="card-practice" style="padding:5px 8px; font-size:7.5pt;">
           <strong style="color:#1d4ed8;">Mode M15: Direct Proportion &amp; Unitary Method (Page 33)</strong><br>
           1. 1 bottle = 14.40 &divide; 8 = £1.80. 13 bottles = 13 &times; 1.80 = <strong>£23.40</strong> [2m].<br>
           2. 1 litre = 165 &divide; 15 = 11 miles. 22 litres = 22 &times; 11 = <strong>242 miles</strong> [2m].<br>
           3. 1 portion = 600 &divide; 8 = 75g. 20 portions = 20 &times; 75 = 1,500g = <strong>1.5 kg</strong> [2m].<br>
           4. Workers and time are in inverse proportion; more workers complete the job in less time, not more [2m].
         </div>"""),

        # Page 73: Modes 16 to 18 Answers
        ("Diagnostic Answer Key &bull; Modes M16, M17 &amp; M18",
         """<div class="card-practice" style="padding:5px 8px; margin-bottom:5px; font-size:7.5pt;">
           <strong style="color:#1d4ed8;">Mode M16: Inverse Proportion (Workforce vs Time) (Page 35)</strong><br>
           1. Total worker-days = 3 &times; 10 = 30. For 5 bricklayers: 30 &divide; 5 = <strong>6 days</strong> [2m].<br>
           2. Total distance = 60 &times; 4 = 240 miles. Time at 80 mph: 240 &divide; 80 = <strong>3 hours</strong> [2m].<br>
           3. Total machine-hours = 12 &times; 9 = 108. For 4 machines: 108 &divide; 4 = <strong>27 hours</strong> [2m].<br>
           4. Direct proportion: when one increases, the other increases proportionally. Inverse: when one increases, the other decreases [2m].
         </div>
         <div class="card-practice" style="padding:5px 8px; margin-bottom:5px; font-size:7.5pt;">
           <strong style="color:#1d4ed8;">Mode M17: Scale Drawings &amp; Map Ratios (Page 37)</strong><br>
           1. Length: 7.5 &times; 200 = 1,500 cm = 15m. Width: 4 &times; 200 = 800 cm = 8m. <strong>15m by 8m</strong> [2m].<br>
           2. 6.5m = 650 cm &rarr; 650 &divide; 20 = <strong>32.5 cm</strong> [2m].<br>
           3. 8 &times; 25,000 = 200,000 cm = 2,000m = <strong>2 kilometres</strong> [2m].<br>
           4. 1 unit on the drawing represents 100 of the same units in real life (e.g. 1 cm = 100 cm = 1 m) [1m].
         </div>
         <div class="card-practice" style="padding:5px 8px; font-size:7.5pt;">
           <strong style="color:#1d4ed8;">Mode M18: Area &amp; Perimeter of Compound Shapes (Page 39)</strong><br>
           1. Perimeter = 9 + 7 + 3 + 4 + 6 + 3 = <strong>32 metres</strong> [2m].<br>
           2. Area = (10 &times; 6) + (4 &times; 5) = 60 + 20 = <strong>80 m&sup2;</strong> [2m].<br>
           3. Cost = 48 &times; £6.50 = <strong>£312.00</strong> [2m].<br>
           4. Missing width = overall base minus top width = 14 - 6 = <strong>8 metres</strong> [1m].
         </div>"""),

        # Page 74: Modes 19 to 21 Answers
        ("Diagnostic Answer Key &bull; Modes M19, M20 &amp; M21",
         """<div class="card-practice" style="padding:5px 8px; margin-bottom:5px; font-size:7.5pt;">
           <strong style="color:#1d4ed8;">Mode M19: Circle Geometry &bull; Radius vs Diameter (Page 41)</strong><br>
           1. Radius = 30 &divide; 2 = 15 cm. Area = 3.14 &times; 15&sup2; = 3.14 &times; 225 = <strong>706.5 cm&sup2;</strong> [2m].<br>
           2. d = 2 &times; 35 = 70 cm. Circumference = &pi;d = (22/7)&times;70 = <strong>220 cm (or 2.2 m)</strong> [2m].<br>
           3. Curved = &frac12;&pi;d = &frac12;(3.142&times;14) = 22 cm. Total perimeter = 22 + 14 = <strong>36 cm</strong> [2m].<br>
           4. Since d = 2r, squaring diameter gives (2r)&sup2; = 4r&sup2;, which is 4 times larger than r&sup2; [2m].
         </div>
         <div class="card-practice" style="padding:5px 8px; margin-bottom:5px; font-size:7.5pt;">
           <strong style="color:#1d4ed8;">Mode M20: Volume of Prisms &amp; Cylinders (Page 43)</strong><br>
           1. Volume = 80 &times; 40 &times; 50 = 160,000 cm&sup3; &rarr; 160,000 &divide; 1,000 = <strong>160 litres</strong> [2m].<br>
           2. Radius = 2m. Volume = 3.142 &times; 2&sup2; &times; 10 = 3.142 &times; 4 &times; 10 = <strong>125.68 m&sup3;</strong> [2m].<br>
           3. 120 &times; 1,000 = <strong>120,000 litres</strong> [1m].<br>
           4. Volume = <code>&frac12; &times; base &times; height &times; length</code> [1m].
         </div>
         <div class="card-practice" style="padding:5px 8px; font-size:7.5pt;">
           <strong style="color:#1d4ed8;">Mode M21: Metric Area &amp; Volume Conversions (Page 45)</strong><br>
           1. 3.5 &times; 10,000 = <strong>35,000 cm&sup2;</strong> [2m].<br>
           2. 50,000 &divide; 10,000 = <strong>5 m&sup2;</strong> [2m].<br>
           3. Tile = 10 &times; 10 = 100 cm&sup2;. Wall = 6 &times; 10,000 = 60,000 cm&sup2;. Tiles = 60,000 &divide; 100 = <strong>600 tiles</strong> [2m].<br>
           4. 1m = 100cm. A cube of 1m&sup3; is 100cm &times; 100cm &times; 100cm = 1,000,000 cm&sup3; [2m].
         </div>"""),

        # Page 75: Modes 22 to 24 Answers
        ("Diagnostic Answer Key &bull; Modes M22, M23 &amp; M24",
         """<div class="card-practice" style="padding:5px 8px; margin-bottom:5px; font-size:7.5pt;">
           <strong style="color:#1d4ed8;">Mode M22: Speed, Distance &amp; Time (Page 47)</strong><br>
           1. 2h 45m = 2.75 hrs. Speed = 210 &divide; 2.75 = <strong>76.36 mph (or 76.4 mph)</strong> [2m].<br>
           2. 0.6 &times; 60 = 36 mins &rarr; <strong>3 hours 36 minutes</strong> [2m].<br>
           3. 12 mins = 12/60 = 0.2 hrs &rarr; 4.2 hrs. Distance = 55 &times; 4.2 = <strong>231 miles</strong> [2m].<br>
           4. 15 minutes is 15/60 = 1/4 = 0.25 of an hour, not 0.15 of an hour [1m].
         </div>
         <div class="card-practice" style="padding:5px 8px; margin-bottom:5px; font-size:7.5pt;">
           <strong style="color:#1d4ed8;">Mode M23: Density, Mass &amp; Volume (Page 49)</strong><br>
           1. Density = 115 &divide; 0.05 = <strong>2,300 kg/m&sup3;</strong> [2m].<br>
           2. Mass = 19.3 &times; 50 = <strong>965 grams</strong> [2m].<br>
           3. Volume = 18 &divide; 0.9 = <strong>20 litres</strong> [2m].<br>
           4. <code>Pressure = Force &divide; Area</code> [1m].
         </div>
         <div class="card-practice" style="padding:5px 8px; font-size:7.5pt;">
           <strong style="color:#1d4ed8;">Mode M24: Pythagoras' Theorem (Page 51)</strong><br>
           1. c&sup2; = 8&sup2; + 15&sup2; = 64 + 225 = 289 &rarr; c = &radic;289 = <strong>17 cm</strong> [2m].<br>
           2. c&sup2; = 10&sup2; + 6&sup2; = 100 + 36 = 136 &rarr; c = &radic;136 = <strong>11.66 metres</strong> [2m].<br>
           3. a&sup2; = 6.5&sup2; - 6&sup2; = 42.25 - 36 = 6.25 &rarr; a = &radic;6.25 = <strong>2.5 metres</strong> [2m].<br>
           4. The hypotenuse is always the longest side, located directly opposite the right angle [1m].
         </div>"""),

        # Page 76: Modes 25 to 27 Answers
        ("Diagnostic Answer Key &bull; Modes M25, M26 &amp; M27",
         """<div class="card-practice" style="padding:5px 8px; margin-bottom:5px; font-size:7.5pt;">
           <strong style="color:#1d4ed8;">Mode M25: Mean from Grouped Tables (Page 53)</strong><br>
           1. Midpoints: 4.5, 14.5, 24.5, 34.5. Products: (4.5&times;5=22.5); (14.5&times;15=217.5); (24.5&times;20=490); (34.5&times;10=345). &Sigma;fx = 1,075. Total = 50. Mean = 1,075 &divide; 50 = <strong>21.5 minutes</strong> [3m].<br>
           2. (40 + 59) &divide; 2 = 99 &divide; 2 = <strong>£49.50</strong> [1m].<br>
           3. We do not know individual exact values within each group, so the midpoint is assumed for all data in that bracket [1m].<br>
           4. Modal group: <strong>20–29 minutes</strong> (highest frequency 20) [1m].
         </div>
         <div class="card-practice" style="padding:5px 8px; margin-bottom:5px; font-size:7.5pt;">
           <strong style="color:#1d4ed8;">Mode M26: Comparing Data Sets (Page 55)</strong><br>
           1. Machine A is slightly faster on average (18.2s vs 18.4s) [1m]. Machine A is significantly more consistent/reliable because its range is much smaller (1.4s vs 4.8s) [2m].<br>
           2. 41 - 9 = <strong>32</strong> [1m].<br>
           3. A low range ensures components are manufactured to identical specifications with minimal variation/defects [1m].<br>
           4. The middle value when data is ordered from lowest to highest [1m].
         </div>
         <div class="card-practice" style="padding:5px 8px; font-size:7.5pt;">
           <strong style="color:#1d4ed8;">Mode M27: Combined Probability (Page 57)</strong><br>
           1. P(Blue) = 5/8. P(Blue and Blue) = 5/8 &times; 5/8 = <strong>25/64</strong> [2m].<br>
           2. 0.4 &times; 0.3 = <strong>0.12 (or 12%)</strong> [2m].<br>
           3. 1/6 &times; 1/6 = <strong>1/36</strong> [2m].<br>
           4. Multiplying fractions (values less than 1) results in a smaller product because both conditions must occur simultaneously [1m].
         </div>"""),

        # Page 77: Modes 28 to 30 Answers
        ("Diagnostic Answer Key &bull; Modes E28, E29 &amp; E30",
         """<div class="card-practice" style="padding:5px 8px; margin-bottom:5px; font-size:7.5pt;">
           <strong style="color:#1d4ed8;">Mode E28: Comma Splices &amp; Boundaries (Page 59)</strong><br>
           1. <em>The warehouse was closed; deliveries were delayed.</em> [1m].<br>
           2. <em>She wanted to apply for the apprenticeship, but she lacked the paperwork.</em> [1m].<br>
           3. An error where two independent complete clauses are joined by only a comma without a coordinating conjunction [2m].<br>
           4. Semicolon: <em>The training course was intense<strong>;</strong> however, it was rewarding.</em> [1m].
         </div>
         <div class="card-practice" style="padding:5px 8px; margin-bottom:5px; font-size:7.5pt;">
           <strong style="color:#1d4ed8;">Mode E29: Apostrophes &bull; Omission vs Possession (Page 61)</strong><br>
           1. <strong>its</strong>. 'The dog wagged it is tail' makes no sense, so it is the possessive pronoun without apostrophe [2m].<br>
           2. <em>The clients arrived with three boxes of documents.</em> (Remove all three incorrect plural apostrophes!) [2m].<br>
           3. <em>The <strong>doctors'</strong> surgeries were newly renovated.</em> [1m].<br>
           4. they've = they have; who's = who is (or who has) [2m].
         </div>
         <div class="card-practice" style="padding:5px 8px; font-size:7.5pt;">
           <strong style="color:#1d4ed8;">Mode E30: Subject-Verb Agreement (Page 63)</strong><br>
           1. <strong>was</strong> (subject is singular: 'A team') [1m].<br>
           2. <strong>is</strong> (subject 'Neither' is singular) [1m].<br>
           3. <strong>has</strong> (subject 'The collection' is singular) [1m].<br>
           4. 'group' is a singular collective noun; the formal verb must be 'was', not plural 'were' [2m].
         </div>"""),

        # Page 78: BKSB Algorithmic Cheat-Sheet (Summary Table)
        ("BKSB Algorithmic Diagnostic Secrets &bull; Quick Lookup Table",
         """<table class="data-table" style="font-size:7.2pt;">
           <tr><th>Failure Mode</th><th>Trap Distractor</th><th>The Golden Correction</th></tr>
           <tr><td><strong>Reverse Percentages</strong></td><td>Calculating % of sale price &amp; adding</td><td>Divide by percentage multiplier: <code>New &divide; 0.80</code></td></tr>
           <tr><td><strong>Percentage Increase</strong></td><td>Calculating in 10% steps</td><td>Use single multiplier: +15% &rarr; <code>&times; 1.15</code></td></tr>
           <tr><td><strong>Compound Interest</strong></td><td>Multiplying Year 1 by years</td><td>Use power formula: <code>Principal &times; (Multiplier)&supt;</code></td></tr>
           <tr><td><strong>Time Conversion</strong></td><td>Entering 2h 45m as 2.45</td><td>Divide minutes by 60: 45/60 = 0.75 &rarr; <code>2.75 hrs</code></td></tr>
           <tr><td><strong>Metric Area</strong></td><td>Multiplying m&sup2; by 100 to get cm&sup2;</td><td>Multiply by 10,000 (100 &times; 100)</td></tr>
           <tr><td><strong>Metric Volume</strong></td><td>Assuming 1 m&sup3; = 1 litre</td><td>Multiply by 1,000 (1 m&sup3; = 1,000 litres)</td></tr>
           <tr><td><strong>Circle Area</strong></td><td>Squaring diameter</td><td>Halve to radius first: <code>r = d/2 &rarr; &pi;r&sup2;</code></td></tr>
           <tr><td><strong>Ratio Sharing</strong></td><td>Dividing given share by total parts</td><td>Find 1 part using only that person's ratio number</td></tr>
           <tr><td><strong>Grouped Mean</strong></td><td>Averaging frequencies</td><td>Calculate &Sigma;(Midpoint &times; Frequency) &divide; Total Frequency</td></tr>
           <tr><td><strong>Data Comparison</strong></td><td>Copying numbers without words</td><td>State: Higher average (mean) AND more consistent (lower range)</td></tr>
           <tr><td><strong>Comma Splice</strong></td><td>Joining sentences with a comma</td><td>Use semicolon (;), full stop (.), or conjunction</td></tr>
           <tr><td><strong>its vs it's</strong></td><td>Using it's for possession</td><td>it's = it is; its = possessive (its tail, its logo)</td></tr>
         </table>"""),

        # Page 79: Tutor Remediation Rubric & Progression Milestones
        ("Tutor Remediation Rubric &amp; Gateway Milestones",
         """<div class="card-concept" style="border-left-color:#1d4ed8; font-size:7.5pt; margin-bottom:6px;">
           <strong style="color:#1d4ed8;">BKSB Exit Gateway Score Criteria:</strong><br>
           Colleges and employers assess candidates using computer-adaptive bands:
           <table class="data-table" style="font-size:7pt; margin-top:4px;">
             <tr><th>Diagnostic Assessment Score</th><th>Diagnostic Level Achieved</th><th>Apprenticeship Gateway Status</th></tr>
             <tr><td>0 – 14 / 30 Marks (&lt; 50%)</td><td>Entry Level 3</td><td>Mandatory intensive college remediation</td></tr>
             <tr><td>15 – 21 / 30 Marks (50% – 70%)</td><td>Level 1 Proficient</td><td>Targeted support required in failed strands</td></tr>
             <tr><td>22 – 25 / 30 Marks (73% – 85%)</td><td>Level 2 Gateway Ready</td><td>Cleared for official Level 2 Functional Skills exam</td></tr>
             <tr style="background:#e0f2fe; font-weight:bold;"><td>26 – 30 / 30 Marks (87% – 100%)</td><td>Level 2 Advanced Distinction</td><td>Full Gateway exemption; GCSE Grade 4/5 equivalent</td></tr>
           </table>
         </div>
         <div class="card-tip" style="font-size:7.5pt;">
           <strong>Advice for Trainees Re-sitting BKSB Diagnostic Screenings:</strong><br>
           The computer-adaptive algorithm increases question difficulty when you answer correctly. If questions begin to feel challenging and involve multi-step word scenarios, congratulations &mdash; that indicates you are operating at Level 2! Take your time, sketch diagrams on your rough paper, and double-check your arithmetic before submitting each screen.
         </div>""")
    ]

    for p_num, (ans_title, ans_content) in enumerate(mode_answers, 68):
        pages.append(f"""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; BKSB Remediation</div>
    <div class="page-header-strand">Complete Explanatory Answer Key &bull; Retry Drills</div>
  </div>

  <h2>{ans_title}</h2>
  <p style="margin-bottom:6px;">Step-by-step marking solutions and distractor breakdowns:</p>

  {ans_content}

  <div class="page-footer">
    <div>BKSB Remediation Workbook &bull; Explanatory Answer Key</div>
    <div class="page-num">Page {p_num}</div>
  </div>
</div>
""")

    # Pages 80 to 83: Exit Simulation 30-Item Mark Scheme (4 pages)
    pages.append("""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Exit Simulation Key</div>
    <div class="page-header-strand">Milestone Mark Scheme &bull; Items 1 to 8</div>
  </div>

  <h2>Exit Milestone Simulation &bull; Items 1 to 8 Solutions</h2>
  <p style="margin-bottom:6px;">Award 1 mark per correct item. Fully worked solutions and distractor analyses below:</p>

  <div class="card-practice" style="padding:6px 10px; margin-bottom:5px; font-size:7.5pt;">
    <strong>Item 1: Significant Figures &rarr; C) 0.085 [1 Mark]</strong><br>
    First non-zero digit is 8, second is 4. Deciding digit is 7 (&ge; 5, rounds up 4 to 5) &rarr; <strong>0.085</strong>. Trap: 0.084 (failed to round) or 0.08 (counted decimal places).
  </div>

  <div class="card-practice" style="padding:6px 10px; margin-bottom:5px; font-size:7.5pt;">
    <strong>Item 2: Temperature Rise &rarr; 6&deg;C [1 Mark]</strong><br>
    -8 + 14 = <strong>+6&deg;C</strong>. Trap: -22&deg;C (subtracted 14) or -6&deg;C (arithmetic error).
  </div>

  <div class="card-practice" style="padding:6px 10px; margin-bottom:5px; font-size:7.5pt;">
    <strong>Item 3: BIDMAS Order of Operations &rarr; 16 [1 Mark]</strong><br>
    Brackets: (5 - 1) = 4. Indices: 4&sup2; = 16. Multiply/Divide: 3 &times; 16 = 48 &rarr; 48 &divide; 6 = 8. Subtract: 24 - 8 = <strong>16</strong>. Trap: 56 (calculated left-to-right).
  </div>

  <div class="card-practice" style="padding:6px 10px; margin-bottom:5px; font-size:7.5pt;">
    <strong>Item 4: Fractions of Remainder &rarr; £480 [1 Mark]</strong><br>
    Marketing: 1/3 of 1,800 = £600. Remainder = 1,800 - 600 = £1,200. Medical: 3/5 of 1,200 = £720. Remaining: 1,200 - 720 = <strong>£480</strong>. Trap: £120 (calculated 3/5 of original total).
  </div>

  <div class="card-practice" style="padding:6px 10px; margin-bottom:5px; font-size:7.5pt;">
    <strong>Item 5: Mixed Number Subtraction &rarr; 1 11/12 [1 Mark]</strong><br>
    11/3 - 7/4 = 44/12 - 21/12 = 23/12 = <strong>1 11/12</strong>. Trap: 2 1/1 (subtracted whole numbers and numerators directly).
  </div>

  <div class="card-practice" style="padding:6px 10px; margin-bottom:5px; font-size:7.5pt;">
    <strong>Item 6: Fraction Division &rarr; 18 portions [1 Mark]</strong><br>
    27/4 &divide; 3/8 = 27/4 &times; 8/3 = (27 &divide; 3 = 9) &times; (8 &divide; 4 = 2) = 9 &times; 2 = <strong>18 portions</strong>. Trap: 81/32 (multiplied without inverting).
  </div>

  <div class="card-practice" style="padding:6px 10px; margin-bottom:5px; font-size:7.5pt;">
    <strong>Item 7: Decimal Multiplication &rarr; 0.036 [1 Mark]</strong><br>
    45 &times; 8 = 360. Decimal places: 2 in 0.45, 2 in 0.08 &rarr; 4 places. 0.0360 = <strong>0.036</strong>. Trap: 0.36 (missed 1 place).
  </div>

  <div class="card-practice" style="padding:6px 10px; font-size:7.5pt;">
    <strong>Item 8: Decimal Division &rarr; 45 [1 Mark]</strong><br>
    7.2 / 0.16 = (7.2 &times; 100) / (0.16 &times; 100) = 720 &divide; 16 = <strong>45</strong>. Trap: 4.5 or 0.45.
  </div>

  <div class="page-footer">
    <div>Diagnostic Exit Simulation &bull; Mark Scheme 1 to 8</div>
    <div class="page-num">Page 80</div>
  </div>
</div>
""")

    pages.append("""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Exit Simulation Key</div>
    <div class="page-header-strand">Milestone Mark Scheme &bull; Items 9 to 16</div>
  </div>

  <h2>Exit Milestone Simulation &bull; Items 9 to 16 Solutions</h2>
  <p style="margin-bottom:6px;">Award 1 mark per correct item. Fully worked solutions and distractor analyses below:</p>

  <div class="card-practice" style="padding:6px 10px; margin-bottom:5px; font-size:7.5pt;">
    <strong>Item 9: Decimal Time Conversion &rarr; £96.00 [1 Mark]</strong><br>
    40 mins = 40/60 = 2/3 hr. Total time = 2 2/3 hrs = 8/3 hrs. Cost = (8/3) &times; 36 = 8 &times; 12 = <strong>£96.00</strong>. Trap: £86.40 (calculated 2.4 &times; 36).
  </div>

  <div class="card-practice" style="padding:6px 10px; margin-bottom:5px; font-size:7.5pt;">
    <strong>Item 10: Reverse Percentages &rarr; £480.00 [1 Mark]</strong><br>
    85% = £408. Original = 408 &divide; 0.85 = <strong>£480.00</strong>. Trap: £469.20 (calculated 15% of 408 and added back).
  </div>

  <div class="card-practice" style="padding:6px 10px; margin-bottom:5px; font-size:7.5pt;">
    <strong>Item 11: Percentage Change &rarr; 15% [1 Mark]</strong><br>
    Increase = 55,200 - 48,000 = £7,200. Percentage = (7,200 &divide; 48,000) &times; 100 = <strong>15%</strong>. Trap: 13.04% (divided by new value).
  </div>

  <div class="card-practice" style="padding:6px 10px; margin-bottom:5px; font-size:7.5pt;">
    <strong>Item 12: Compound Interest &rarr; £6,489.60 [1 Mark]</strong><br>
    6,000 &times; (1.04)&sup2; = 6,000 &times; 1.0816 = <strong>£6,489.60</strong>. Trap: £6,480.00 (calculated simple interest: 240 &times; 2).
  </div>

  <div class="card-practice" style="padding:6px 10px; margin-bottom:5px; font-size:7.5pt;">
    <strong>Item 13: Best Value Comparison &rarr; Option B is better value [1 Mark]</strong><br>
    Option A: 320p &divide; 4 = 80p per 100g. Option B: 480p &divide; 6.5 = 73.8p per 100g. <strong>Option B is cheaper by 6.2p per 100g</strong>.
  </div>

  <div class="card-practice" style="padding:6px 10px; margin-bottom:5px; font-size:7.5pt;">
    <strong>Item 14: Ratio Unknown Total &rarr; £1,350 [1 Mark]</strong><br>
    Sports = 5 parts = £750 &rarr; 1 part = 750 &divide; 5 = £150. Total = 9 parts &times; 150 = <strong>£1,350</strong>. Trap: £1,687.50 (divided 750 by 4).
  </div>

  <div class="card-practice" style="padding:6px 10px; margin-bottom:5px; font-size:7.5pt;">
    <strong>Item 15: Direct Proportion &rarr; 90 kg [1 Mark]</strong><br>
    1 part = 54 &divide; 12 = 4.5 kg. 20 parts = 20 &times; 4.5 = <strong>90 kg</strong>. Trap: 84 kg.
  </div>

  <div class="card-practice" style="padding:6px 10px; font-size:7.5pt;">
    <strong>Item 16: Inverse Proportion &rarr; 12 days [1 Mark]</strong><br>
    Total work = 6 &times; 8 = 48 painter-days. For 4 painters: 48 &divide; 4 = <strong>12 days</strong>. Trap: 5.33 days (used direct proportion).
  </div>

  <div class="page-footer">
    <div>Diagnostic Exit Simulation &bull; Mark Scheme 9 to 16</div>
    <div class="page-num">Page 81</div>
  </div>
</div>
""")

    pages.append("""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Exit Simulation Key</div>
    <div class="page-header-strand">Milestone Mark Scheme &bull; Items 17 to 24</div>
  </div>

  <h2>Exit Milestone Simulation &bull; Items 17 to 24 Solutions</h2>
  <p style="margin-bottom:6px;">Award 1 mark per correct item. Fully worked solutions and distractor analyses below:</p>

  <div class="card-practice" style="padding:6px 10px; margin-bottom:5px; font-size:7.5pt;">
    <strong>Item 17: Scale Drawing &rarr; 8.5 metres [1 Mark]</strong><br>
    8.5 &times; 100 = 850 cm &rarr; 850 &divide; 100 = <strong>8.5 metres</strong>. Trap: 85m or 850m.
  </div>

  <div class="card-practice" style="padding:6px 10px; margin-bottom:5px; font-size:7.5pt;">
    <strong>Item 18: Compound L-Shape Area &rarr; 88 m&sup2; [1 Mark]</strong><br>
    Total rectangle = 12 &times; 9 = 108 m&sup2;. Cutout = 5 &times; 4 = 20 m&sup2;. Area = 108 - 20 = <strong>88 m&sup2;</strong>. Trap: 108 m&sup2; (forgot cutout).
  </div>

  <div class="card-practice" style="padding:6px 10px; margin-bottom:5px; font-size:7.5pt;">
    <strong>Item 19: Circle Area &rarr; 13.85 m&sup2; [1 Mark]</strong><br>
    Radius = 4.2 &divide; 2 = 2.1m. Area = 3.142 &times; 2.1&sup2; = 3.142 &times; 4.41 = <strong>13.856 m&sup2; (or 13.86 m&sup2;)</strong>. Trap: 55.43 m&sup2; (squared diameter).
  </div>

  <div class="card-practice" style="padding:6px 10px; margin-bottom:5px; font-size:7.5pt;">
    <strong>Item 20: Cylinder Capacity &rarr; 1,697 litres [1 Mark]</strong><br>
    Volume = &pi;r&sup2;h = 3.142 &times; 0.6&sup2; &times; 1.5 = 3.142 &times; 0.36 &times; 1.5 = 1.69668 m&sup3;. Litres = 1.69668 &times; 1,000 = <strong>1,697 litres</strong>. Trap: 1.7L.
  </div>

  <div class="card-practice" style="padding:6px 10px; margin-bottom:5px; font-size:7.5pt;">
    <strong>Item 21: Area Metric Conversion &rarr; 62,000 cm&sup2; [1 Mark]</strong><br>
    6.2 &times; 10,000 = <strong>62,000 cm&sup2;</strong>. Trap: 620 cm&sup2; (multiplied only by 100).
  </div>

  <div class="card-practice" style="padding:6px 10px; margin-bottom:5px; font-size:7.5pt;">
    <strong>Item 22: Average Speed &rarr; 44 mph [1 Mark]</strong><br>
    3h 45m = 3.75 hrs. Speed = 165 &divide; 3.75 = <strong>44 mph</strong>. Trap: 47.8 mph (entered 165 &divide; 3.45).
  </div>

  <div class="card-practice" style="padding:6px 10px; margin-bottom:5px; font-size:7.5pt;">
    <strong>Item 23: Density Calculation &rarr; 8.5 g/cm&sup3; [1 Mark]</strong><br>
    Mass = 2.125 kg = 2,125 g. Density = 2,125 &divide; 250 = <strong>8.5 g/cm&sup3;</strong>. Trap: 0.0085 g/cm&sup3; (forgot kg to g conversion).
  </div>

  <div class="card-practice" style="padding:6px 10px; font-size:7.5pt;">
    <strong>Item 24: Pythagoras' Wall Height &rarr; 6 metres [1 Mark]</strong><br>
    a&sup2; = 6.5&sup2; - 2.5&sup2; = 42.25 - 6.25 = 36 &rarr; a = &radic;36 = <strong>6 metres</strong>. Trap: 6.96m (added instead of subtracting).
  </div>

  <div class="page-footer">
    <div>Diagnostic Exit Simulation &bull; Mark Scheme 17 to 24</div>
    <div class="page-num">Page 82</div>
  </div>
</div>
""")

    pages.append("""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Exit Simulation Key</div>
    <div class="page-header-strand">Milestone Mark Scheme &bull; Items 25 to 30</div>
  </div>

  <h2>Exit Milestone Simulation &bull; Items 25 to 30 Solutions</h2>
  <p style="margin-bottom:6px;">Award 1 mark per correct item. Fully worked solutions and distractor analyses below:</p>

  <div class="card-practice" style="padding:6px 10px; margin-bottom:5px; font-size:7.5pt;">
    <strong>Item 25: Grouped Mean &rarr; 19.5 minutes [1 Mark]</strong><br>
    Midpoints: 4.5, 14.5, 24.5, 34.5. Products: (4.5&times;6=27); (14.5&times;14=203); (24.5&times;16=392); (34.5&times;4=138). &Sigma;fx = 760. Total = 40. Mean = 760 &divide; 40 = <strong>19.0 minutes</strong>. Trap: 10 (averaged frequencies).
  </div>

  <div class="card-practice" style="padding:6px 10px; margin-bottom:5px; font-size:7.5pt;">
    <strong>Item 26: Data Comparison &rarr; Valid Comparison Statement [1 Mark]</strong><br>
    Shift 2 had a slightly higher average output (84 vs 82), but Shift 1 was substantially more consistent and reliable due to its smaller range (6 vs 22). (Award 1 mark only if both average and consistency are stated).
  </div>

  <div class="card-practice" style="padding:6px 10px; margin-bottom:5px; font-size:7.5pt;">
    <strong>Item 27: Combined Probability &rarr; 0.864 (or 86.4%) [1 Mark]</strong><br>
    0.96 &times; 0.90 = <strong>0.864 (or 86.4% or 108/125)</strong>. Trap: 1.86 (added probabilities).
  </div>

  <div class="card-practice" style="padding:6px 10px; margin-bottom:5px; font-size:7.5pt;">
    <strong>Item 28: Comma Splice Correction &rarr; Valid Boundary [1 Mark]</strong><br>
    <em>The system backup completed successfully; the server rebooted automatically.</em> (Accept full stop or conjunction: <em>...successfully, and the server...</em>).
  </div>

  <div class="card-practice" style="padding:6px 10px; margin-bottom:5px; font-size:7.5pt;">
    <strong>Item 29: Apostrophe Selection &rarr; its ... it's [1 Mark]</strong><br>
    <em>'The company updated <strong>its</strong> policy because <strong>it\'s</strong> committed to safety.'</em> (First is possessive pronoun, second is contraction of 'it is').
  </div>

  <div class="card-practice" style="padding:6px 10px; margin-bottom:6px; font-size:7.5pt;">
    <strong>Item 30: Subject-Verb Agreement &rarr; was [1 Mark]</strong><br>
    <strong>was</strong>. The subject is 'Neither' (singular pronoun), which requires the singular verb 'was'. Trap: 'were' (mistakenly agreed with 'drivers').
  </div>

  <div class="card-concept" style="border-left-color:#1d4ed8; font-size:7.5pt;">
    <strong style="color:#1d4ed8;">Diagnostic Pass Certification Threshold:</strong><br>
    Learners scoring <strong>22 or more / 30 marks</strong> have successfully cleared the BKSB Level 2 Gateway barrier and demonstrate robust mastery across all curriculum failure modes.
  </div>

  <div class="page-footer">
    <div>Diagnostic Exit Simulation &bull; Mark Scheme 25 to 30</div>
    <div class="page-num">Page 83</div>
  </div>
</div>
""")

    # -------------------------------------------------------------
    # PAGE 84: BACK COVER
    # -------------------------------------------------------------
    pages.append(f"""
<div class="page cover-full-page">
  <img src="file://{back_img}" class="cover-full-img">
</div>
""")

    full_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>BKSB Diagnostic Remediation Workbook</title>
{SHARED_CSS}
<style>
  :root {{
    --theme: #1d4ed8;
    --accent: #60a5fa;
  }}
</style>
</head>
<body>
{''.join(pages)}
</body>
</html>"""

    pdf_filename = "MasterFunctionalSkills_BKSB_Remediation_Workbook.pdf"
    count = render_book_to_pdf(full_html, pdf_filename)
    return count

if __name__ == "__main__":
    build_bksb_remediation_book()
