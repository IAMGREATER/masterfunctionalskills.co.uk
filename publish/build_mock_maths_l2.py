#!/usr/bin/env python3
"""
build_mock_maths_l2.py
Compiles the complete 84-page publication:
MasterFunctionalSkills_Mock_Pack_Maths_L2.pdf

Contains 8 Complete Official-Style Exam Papers (Section A & Section B, 64 Marks each)
with Comprehensive Examiner Mark Schemes and Process Mark Allocations.

Mapped strictly to Ofqual Functional Skills Mathematics Level 2 Subject Content.
Full CGP-style visual pedagogy, dyslexia-friendly warm cream styling (#FDFBF7),
ruled and grid workspaces, and formula reference sheets.
"""

import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from book_framework import (
    SHARED_CSS, render_book_to_pdf, BOOKS_IMG_DIR
)

def build_mock_maths_l2_book():
    front_img = os.path.join(BOOKS_IMG_DIR, "mock_pack_maths_l2_cover_page-1.png")
    back_img = os.path.join(BOOKS_IMG_DIR, "mock_pack_maths_l2_cover_page-2.png")
    
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
    # PAGE 2: INSIDE COVER & BLUEPRINT
    # -------------------------------------------------------------
    pages.append("""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Maths Level 2</div>
    <div class="page-header-strand">Exam Specification &amp; Architecture</div>
  </div>

  <h2>Level 2 Mathematics Examination Blueprint</h2>
  <p>The Level 2 Functional Skills Mathematics qualification is equivalent to GCSE Grade 4/C. Regulated by Ofqual, it is awarded by Pearson Edexcel, City &amp; Guilds, AQA, NCFE, and Highfield. This 8-Mock Exam Pack reproduces the exact weighting, structure, and problem-solving complexity of official live examinations.</p>

  <div class="card-concept" style="border-left-color:#002046; background:#f0f9ff;">
    <h3 style="color:#002046; margin-top:0;">Official Examination Structure</h3>
    <table class="data-table" style="font-size:8pt;">
      <tr><th>Component</th><th>Duration</th><th>Marks Available</th><th>Permitted Equipment</th></tr>
      <tr>
        <td><strong>Section A: Non-Calculator</strong></td>
        <td>25 Minutes</td>
        <td>16 Marks (25%)</td>
        <td>Pen, pencil, ruler. <strong>NO CALCULATOR</strong>.</td>
      </tr>
      <tr>
        <td><strong>Section B: Calculator</strong></td>
        <td>1 Hour 20 Mins (80 mins)</td>
        <td>48 Marks (75%)</td>
        <td>Scientific / basic calculator, pen, pencil, ruler.</td>
      </tr>
      <tr style="background:#e0f2fe; font-weight:bold;">
        <td>TOTAL FULL PAPER</td>
        <td>1 Hour 45 Mins (105 mins)</td>
        <td>64 Marks (100%)</td>
        <td>Pass Mark: ~35–38 / 64 (approx. 55%–60%)</td>
      </tr>
    </table>
  </div>

  <div class="grid-2" style="margin-top:6px;">
    <div class="card-method">
      <h3 style="color:#16a34a; margin-top:0;">Examiner Mark Classifications</h3>
      <p><strong>[P] Process Marks:</strong> Awarded for choosing and carrying out appropriate mathematical strategies, even if an arithmetic slip occurs.</p>
      <p><strong>[M] Method Marks:</strong> Awarded for using standard formulas and showing correct intermediate steps.</p>
      <p><strong>[A] Accuracy Marks:</strong> Awarded for the correct final numerical answer with units.</p>
      <p><strong>[B] Unconditional Marks:</strong> Independent marks for specific statements or labels.</p>
    </div>
    <div class="card-tip">
      <h3 style="color:#d97706; margin-top:0;">Candidate Exam Record</h3>
      <table style="width:100%; border-collapse:collapse; font-size:7.5pt; margin-top:4px;">
        <tr><td style="padding:2.5px; border-bottom:1px solid #cbd5e1;"><strong>Candidate Name:</strong></td><td style="border-bottom:1px solid #cbd5e1;"></td></tr>
        <tr><td style="padding:2.5px; border-bottom:1px solid #cbd5e1;"><strong>Exam Centre:</strong></td><td style="border-bottom:1px solid #cbd5e1;"></td></tr>
        <tr><td style="padding:2.5px; border-bottom:1px solid #cbd5e1;"><strong>Mock 1 Score:</strong></td><td style="border-bottom:1px solid #cbd5e1;">&nbsp;&nbsp;&nbsp;&nbsp; / 64</td></tr>
        <tr><td style="padding:2.5px; border-bottom:1px solid #cbd5e1;"><strong>Mock 2 Score:</strong></td><td style="border-bottom:1px solid #cbd5e1;">&nbsp;&nbsp;&nbsp;&nbsp; / 64</td></tr>
        <tr><td style="padding:2.5px; border-bottom:1px solid #cbd5e1;"><strong>Mock 3 Score:</strong></td><td style="border-bottom:1px solid #cbd5e1;">&nbsp;&nbsp;&nbsp;&nbsp; / 64</td></tr>
        <tr><td style="padding:2.5px; border-bottom:1px solid #cbd5e1;"><strong>Mock 4 Score:</strong></td><td style="border-bottom:1px solid #cbd5e1;">&nbsp;&nbsp;&nbsp;&nbsp; / 64</td></tr>
        <tr><td style="padding:2.5px; border-bottom:1px solid #cbd5e1;"><strong>Mock 5 Score:</strong></td><td style="border-bottom:1px solid #cbd5e1;">&nbsp;&nbsp;&nbsp;&nbsp; / 64</td></tr>
        <tr><td style="padding:2.5px; border-bottom:1px solid #cbd5e1;"><strong>Mock 6 Score:</strong></td><td style="border-bottom:1px solid #cbd5e1;">&nbsp;&nbsp;&nbsp;&nbsp; / 64</td></tr>
        <tr><td style="padding:2.5px; border-bottom:1px solid #cbd5e1;"><strong>Mock 7 Score:</strong></td><td style="border-bottom:1px solid #cbd5e1;">&nbsp;&nbsp;&nbsp;&nbsp; / 64</td></tr>
        <tr><td style="padding:2.5px; border-bottom:1px solid #cbd5e1;"><strong>Mock 8 Score:</strong></td><td style="border-bottom:1px solid #cbd5e1;">&nbsp;&nbsp;&nbsp;&nbsp; / 64</td></tr>
      </table>
    </div>
  </div>

  <div class="card-trap" style="margin-top:6px;">
    <strong>The Golden Rule:</strong> ALWAYS show your working out. If you write only the final answer and make a simple calculation typo, you score 0 marks. Showing clear methods guarantees you secure Process [P] marks!
  </div>

  <div class="page-footer">
    <div>Maths Level 2 &bull; Official 8-Mock Exam Pack</div>
    <div class="page-num">Page 2</div>
  </div>
</div>
""")

    # -------------------------------------------------------------
    # PAGE 3: LEVEL 2 ESSENTIAL FORMULAE - GEOMETRY & TRIGONOMETRY
    # -------------------------------------------------------------
    pages.append("""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Maths Level 2</div>
    <div class="page-header-strand">Essential Formulae &amp; Geometry</div>
  </div>

  <h2>Level 2 Mathematics Formulae Sheet &bull; Geometry &amp; Space</h2>
  <p>You must memorize and confidently apply these core geometric and trigonometric formulas before sitting your examination:</p>

  <div class="grid-2" style="font-size:7.8pt;">
    <div class="card-method" style="padding:6px 10px;">
      <h3 style="color:#16a34a; margin-top:0;">2D Shapes: Perimeter &amp; Area</h3>
      <ul style="margin:2px 0 0 14px; padding:0;">
        <li><strong>Rectangle:</strong> Area = <code>l &times; w</code> &bull; Perimeter = <code>2(l + w)</code></li>
        <li><strong>Triangle:</strong> Area = <code>&frac12; &times; b &times; h = (b &times; h) &divide; 2</code></li>
        <li><strong>Parallelogram:</strong> Area = <code>base &times; perpendicular height</code></li>
        <li><strong>Trapezium:</strong> Area = <code>&frac12;(a + b) &times; h</code> (average of parallel sides &times; height)</li>
        <li><strong>Circle:</strong>
          <br>&bull; Area = <code>&pi;r&sup2;</code> (pi &times; radius &times; radius)
          <br>&bull; Circumference = <code>&pi;d = 2&pi;r</code>
          <br>&bull; Radius = diameter &divide; 2 &bull; Diameter = 2 &times; radius
          <br>&bull; Take &pi; = 3.14 or 3.142 or calculator &pi; key
        </li>
        <li><strong>Semicircle:</strong> Area = <code>&frac12;&pi;r&sup2;</code> &bull; Perimeter = <code>&frac12;&pi;d + d</code></li>
      </ul>
    </div>

    <div class="card-concept" style="border-left-color:#002046; padding:6px 10px;">
      <h3 style="color:#002046; margin-top:0;">3D Shapes: Volume &amp; Surface Area</h3>
      <ul style="margin:2px 0 0 14px; padding:0;">
        <li><strong>Cuboid Volume:</strong> <code>length &times; width &times; height</code></li>
        <li><strong>Cuboid Surface Area:</strong> <code>2(lw + lh + wh)</code></li>
        <li><strong>Prism Volume:</strong> <code>Area of cross-section &times; length</code></li>
        <li><strong>Cylinder Volume:</strong> <code>&pi;r&sup2;h</code> (Circular area &times; height)</li>
        <li><strong>Cylinder Curved Surface Area:</strong> <code>2&pi;rh</code></li>
        <li><strong>Total Cylinder Surface Area:</strong> <code>2&pi;rh + 2&pi;r&sup2;</code></li>
        <li><strong>Pythagoras' Theorem:</strong> <code>a&sup2; + b&sup2; = c&sup2;</code>
          <br>&bull; Finding Hypotenuse (c): <code>c = &radic;(a&sup2; + b&sup2;)</code>
          <br>&bull; Finding Shorter Side (a): <code>a = &radic;(c&sup2; - b&sup2;)</code>
        </li>
      </ul>
    </div>
  </div>

  <div class="card-exam" style="margin-top:6px;">
    <h3 style="color:#7c3aed; margin-top:0;">Exam Hall Trap: Radius vs Diameter</h3>
    <p style="font-size:8pt; margin:0;">Over 65% of candidate errors in circle questions occur because the question states the <em>diameter</em> (e.g., 1.4 m) and the candidate squares 1.4 directly! Always write down: <code>d = 1.4 m &rarr; r = 0.7 m</code> before substituting into <code>&pi;r&sup2;</code>.</p>
  </div>

  <div class="page-footer">
    <div>Maths Level 2 &bull; Official 8-Mock Exam Pack &bull; Formulae Sheet 1</div>
    <div class="page-num">Page 3</div>
  </div>
</div>
""")

    # -------------------------------------------------------------
    # PAGE 4: LEVEL 2 ESSENTIAL FORMULAE - MEASURES, CONVERSIONS & STATS
    # -------------------------------------------------------------
    pages.append("""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Maths Level 2</div>
    <div class="page-header-strand">Measures, Conversions &amp; Statistics</div>
  </div>

  <h2>Level 2 Mathematics Formulae Sheet &bull; Compound Measures &amp; Data</h2>
  <p>Standard conversion factors and statistical definitions tested across official awarding body examinations:</p>

  <div class="grid-2" style="font-size:7.8pt;">
    <div class="card-method" style="padding:6px 10px;">
      <h3 style="color:#16a34a; margin-top:0;">Compound Measures &amp; Rates</h3>
      <ul style="margin:2px 0 0 14px; padding:0;">
        <li><strong>Speed:</strong> <code>Speed = Distance &divide; Time</code>
          <br>&bull; <code>Distance = Speed &times; Time</code> &bull; <code>Time = Distance &divide; Speed</code>
        </li>
        <li><strong>Density:</strong> <code>Density = Mass &divide; Volume</code>
          <br>&bull; <code>Mass = Density &times; Volume</code> &bull; <code>Volume = Mass &divide; Density</code>
        </li>
        <li><strong>Pressure:</strong> <code>Pressure = Force &divide; Area</code> (N/m&sup2; or Pascals)</li>
        <li><strong>Decimal Time Conversions:</strong>
          <br>&bull; 15 mins = 0.25 hrs &bull; 30 mins = 0.5 hrs &bull; 45 mins = 0.75 hrs
          <br>&bull; Minutes to Decimal: <code>minutes &divide; 60</code> (e.g. 18 mins = 18/60 = 0.3 hrs)
          <br>&bull; Decimal to Minutes: <code>decimal &times; 60</code> (e.g. 0.4 hrs = 0.4 &times; 60 = 24 mins)
        </li>
        <li><strong>Metric Volume &amp; Capacity:</strong>
          <br>&bull; <code>1 m&sup3; = 1,000 litres</code> &bull; <code>1 litre = 1,000 ml = 1,000 cm&sup3;</code>
        </li>
      </ul>
    </div>

    <div class="card-concept" style="border-left-color:#002046; padding:6px 10px;">
      <h3 style="color:#002046; margin-top:0;">Financial Maths, Statistics &amp; Probability</h3>
      <ul style="margin:2px 0 0 14px; padding:0;">
        <li><strong>Percentage Change:</strong> <code>(Actual Change &divide; Original Value) &times; 100</code></li>
        <li><strong>Reverse Percentage:</strong> <code>Original Value = Final Value &divide; Multiplier</code></li>
        <li><strong>Simple Interest:</strong> <code>Interest = Principal &times; Rate &times; Time (years)</code></li>
        <li><strong>Compound Interest:</strong> <code>Total = P &times; (1 + r)&supt;</code></li>
        <li><strong>Mean from Frequency Table:</strong> <code>&Sigma;(fx) &divide; &Sigma;f</code> (Total &divide; Frequency)</li>
        <li><strong>Grouped Midpoint:</strong> <code>(Lower Bound + Upper Bound) &divide; 2</code></li>
        <li><strong>Range:</strong> <code>Highest Value - Lowest Value</code></li>
        <li><strong>Probability:</strong> <code>Favourable Outcomes &divide; Total Possible Outcomes</code></li>
        <li><strong>Independent Combined Events:</strong> <code>P(A and B) = P(A) &times; P(B)</code></li>
      </ul>
    </div>
  </div>

  <div class="card-tip" style="margin-top:6px;">
    <h3 style="color:#d97706; margin-top:0;">Metric Area &amp; Volume Conversion Traps</h3>
    <table class="data-table" style="font-size:7.5pt;">
      <tr><th>Linear Dimension</th><th>Area Dimension (Squared)</th><th>Volume Dimension (Cubed)</th></tr>
      <tr><td>1 m = 100 cm</td><td>1 m&sup2; = 100 &times; 100 = <strong>10,000 cm&sup2;</strong></td><td>1 m&sup3; = 100&sup3; = <strong>1,000,000 cm&sup3;</strong></td></tr>
      <tr><td>1 cm = 10 mm</td><td>1 cm&sup2; = 10 &times; 10 = <strong>100 mm&sup2;</strong></td><td>1 cm&sup3; = 10&sup3; = <strong>1,000 mm&sup3;</strong></td></tr>
      <tr><td>1 km = 1,000 m</td><td>1 km&sup2; = 1,000&sup2; = <strong>1,000,000 m&sup2;</strong></td><td>1 litre = 1,000 cm&sup3; &bull; 1 m&sup3; = 1,000 litres</td></tr>
    </table>
  </div>

  <div class="page-footer">
    <div>Maths Level 2 &bull; Official 8-Mock Exam Pack &bull; Formulae Sheet 2</div>
    <div class="page-num">Page 4</div>
  </div>
</div>
""")

    # -------------------------------------------------------------
    # PAGE 5: EXAM TECHNIQUE, PROBLEM SOLVING & MARK ALLOCATION
    # -------------------------------------------------------------
    pages.append("""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Maths Level 2</div>
    <div class="page-header-strand">Problem-Solving &amp; Examiner Secrets</div>
  </div>

  <h2>Mastering Multi-Step Problem Solving &amp; Mark Scheme Secrets</h2>
  <p>Functional Skills Level 2 is not just a test of arithmetic—it assesses your ability to navigate unstructured, real-world problems. Awarding body examiners follow strict mark schemes designed to reward clear logic.</p>

  <div class="grid-2" style="font-size:7.8pt;">
    <div class="card-concept" style="border-left-color:#002046; padding:6px 10px;">
      <h3 style="color:#002046; margin-top:0;">The 4-Step Problem-Solving Architecture</h3>
      <ol style="margin:2px 0 0 16px; padding:0;">
        <li><strong>Deconstruct the Scenario:</strong> Highlight the given facts, constraints (e.g. budgets, time limits, packaging minimums), and the exact question requirement.</li>
        <li><strong>Unit Harmonisation:</strong> Check all measurements immediately. If carpet is sold per square metre and room dimensions are in millimetres, convert before multiplying!</li>
        <li><strong>Execute with Annotation:</strong> Write down what each calculation represents (e.g., 'Area of walls = 42 m&sup2;', 'Tins needed = 42 / 12 = 3.5 &rarr; 4 tins').</li>
        <li><strong>Decision &amp; Context:</strong> If the question asks 'Can the company afford this?' or 'Does the heater meet regulations?', always conclude with a definitive <strong>Yes/No statement</strong> supported by your numerical comparison.</li>
      </ol>
    </div>

    <div class="card-method" style="padding:6px 10px;">
      <h3 style="color:#16a34a; margin-top:0;">Securing All 4 Mark Classifications</h3>
      <ul style="margin:2px 0 0 14px; padding:0;">
        <li><strong>[P] Process Marks:</strong> Awarded for choosing the correct operational strategy (e.g. identifying that a 15% discount requires dividing by 0.85). Even if your mental arithmetic fails, you secure [P] marks!</li>
        <li><strong>[M] Method Marks:</strong> Awarded for writing down recognized formulas with numbers substituted in place.</li>
        <li><strong>[A] Accuracy Marks:</strong> Awarded strictly for the correct numerical calculation. Cannot be awarded if earlier method was fundamentally flawed.</li>
        <li><strong>[B] Independent Marks:</strong> Awarded for non-method elements such as state units (£, m&sup2;, kg), correct rounding, or providing a valid written check.</li>
      </ul>
    </div>
  </div>

  <div class="card-trap" style="margin-top:6px;">
    <h3 style="color:#dc2626; margin-top:0;">How to Write an Official "Check" to Guarantee 1 Mark</h3>
    <p style="font-size:8pt; margin:0 0 4px 0;">Many 4-mark and 5-mark questions end with the prompt: <em>"Show a check of your answer."</em> To get this mark, you MUST show either:</p>
    <div class="grid-2" style="font-size:7.8pt;">
      <div><strong>1. Reverse Calculation (Inverse):</strong><br>If original was <code>45 &times; 12 = 540</code>, write: <code>Check: 540 &divide; 12 = 45</code>.</div>
      <div><strong>2. Estimation Check:</strong><br>Round inputs to 1 significant figure: <code>Check: 48.2 &times; 9.8 &asymp; 50 &times; 10 = 500</code>.</div>
    </div>
  </div>

  <div class="card-tip" style="margin-top:6px;">
    <strong>Examiner Warning:</strong> Simply rewriting the original calculation in reverse order (e.g. <code>12 &times; 45 = 540</code>) is NOT an inverse check and scores <strong>0 marks</strong>.
  </div>

  <div class="page-footer">
    <div>Maths Level 2 &bull; Official 8-Mock Exam Pack &bull; Problem Solving</div>
    <div class="page-num">Page 5</div>
  </div>
</div>
""")

    # -------------------------------------------------------------
    # 8 COMPLETE EXAM PAPERS (7 pages per paper = 56 pages, Pages 6 to 61)
    # -------------------------------------------------------------
    papers_data = [
        # Paper 1
        ("Mock Paper 1: Facilities Management & Event Operations",
         [
           ("Question 1", "[4 Marks]", "Calculate: <code>45.6 &times; 3.8</code> without using a calculator. Show your method.", 55),
           ("Question 2", "[4 Marks]", "An events hall carpet measures 8.5 m by 6 m. A circular dance floor with radius 2 m is placed in the centre. Calculate the remaining carpet area not covered by the dance floor (use &pi; = 3.14).", 65),
           ("Question 3", "[4 Marks]", "Solve: <code>2 &frac34; + 1 &frac23;</code>. Give your answer as a mixed number in its simplest form.", 55),
           ("Question 4", "[4 Marks]", "A supplier offers a 15% discount for early invoice payment. The discounted price is £510. Calculate the original price before the discount. Show an inverse check.", 65)
         ],
         [
           ("Question 5: Catering Budget", "[5 Marks]", "A conference caters for 160 delegates. Lunch costs £14.50 per head. Wine is served at 1 bottle per 4 delegates at £8.40 per bottle. A 10% service charge is added to the subtotal. Calculate the total catering invoice.", 60),
           ("Question 6: Staff Scheduling", "[5 Marks]", "The facility employs 12 stewards working 7.5 hours each at £11.44 per hour, and 3 supervisors working 8 hours each at £16.50 per hour. Calculate the total staffing wage cost for the event.", 60),
           ("Question 7: Marquee Heating", "[5 Marks]", "A marquee has volume 750 m&sup3;. A heater outputs 15 kW. It requires 0.025 kW of heating per cubic metre. Can this heater adequately heat the marquee? Support your answer with calculations.", 60),
           ("Question 8: Fuel Logistics", "[5 Marks]", "A generator burns diesel at 4.2 litres per hour. The generator runs continuously for 3 days and 8 hours. Diesel costs £1.42 per litre. Calculate total diesel cost.", 60),
           ("Question 9: Survey Statistics", "[5 Marks]", "Guest ratings for 40 events: 1–2 stars: 4; 3–4 stars: 12; 5–6 stars: 16; 7–8 stars: 8. Calculate an estimate of the mean rating.", 60),
           ("Question 10: Scale Plan", "[5 Marks]", "On a 1 : 200 plan, an outdoor terrace measures 12.5 cm by 8 cm. Paving slabs cost £24 per square metre. Calculate total paving cost.", 60),
           ("Question 11: Profit Margin", "[5 Marks]", "Total ticket revenue is £18,400. Total event costs are £12,800. Calculate the profit as a percentage of the total revenue. Round to 1 decimal place.", 60),
           ("Question 12: Probability", "[5 Marks]", "Two raffle draws are held. Ticket A has a 1 in 25 chance of winning. Ticket B has a 1 in 40 chance. What is the probability that neither ticket wins?", 60),
           ("Question 13: Journey Schedule", "[4 Marks]", "A coach departs Birmingham at 14:45 to travel 110 miles to London at an average speed of 44 mph. What time will the coach arrive in London?", 55),
           ("Question 14: Water Tank", "[4 Marks]", "A cylindrical water tank has diameter 1.2 m and height 2.5 m. Calculate its capacity in litres (1 m&sup3; = 1,000 litres). Use &pi; = 3.142.", 55)
         ]),

        # Paper 2
        ("Mock Paper 2: Logistics, Transport Fleet & Distribution",
         [
           ("Question 1", "[4 Marks]", "Calculate: <code>684 &divide; 18</code> without using a calculator. Show your full working.", 55),
           ("Question 2", "[4 Marks]", "A pallet measures 1.2 m by 0.8 m. A warehouse floor is 24 m by 16 m. Calculate the maximum number of pallets that can fit on the floor in a single layer.", 65),
           ("Question 3", "[4 Marks]", "Calculate: <code>3/5 &times; 4/7</code>. Express your answer in simplest form.", 55),
           ("Question 4", "[4 Marks]", "A delivery driver's hourly rate increased from £12.50 to £13.75. Calculate the percentage pay increase. Check your answer.", 65)
         ],
         [
           ("Question 5: Fleet Fuel Efficiency", "[5 Marks]", "Van A travels 420 miles on 60 litres of fuel. Van B travels 385 miles on 52 litres. Which van achieves better miles-per-gallon (mpg)? (1 gallon = 4.55 litres).", 60),
           ("Question 6: Cargo Weight & Density", "[5 Marks]", "A container has volume 36 m&sup3;. It is loaded with cargo having an average density of 650 kg/m&sup3;. The maximum payload limit is 24 tonnes. Is the container overloaded?", 60),
           ("Question 7: Courier Delivery Routes", "[5 Marks]", "Driver covers 168 miles in 3 hours 30 mins. A 45-minute delivery stop was included. What was the driving speed while moving?", 60),
           ("Question 8: Forklift Ramp Slope", "[5 Marks]", "A loading ramp rises 1.2 m over a horizontal distance of 5 m. Calculate the length of the sloping surface using Pythagoras (a&sup2; + b&sup2; = c&sup2;).", 60),
           ("Question 9: Delivery Time Statistics", "[5 Marks]", "Delivery times (mins): 10-19 (5), 20-29 (14), 30-39 (21), 40-49 (10). Calculate the estimated mean delivery time.", 60),
           ("Question 10: Warehouse Racking", "[5 Marks]", "Racking is offered with a 12% discount. The discounted cost is £3,960. Find the original price before discount.", 60),
           ("Question 11: Currency & Import", "[5 Marks]", "A consignment from Germany costs €14,500. Customs import duty is 6%. If £1 = €1.15, calculate the total cost in GBP including duty.", 60),
           ("Question 12: Delivery Success Rate", "[5 Marks]", "Out of 850 deliveries, 34 were failed deliveries. Calculate the percentage success rate to 1 decimal place.", 60),
           ("Question 13: Storage Space Volume", "[4 Marks]", "A cold storage room is 12m long, 8m wide, and 3.5m high. Industrial cooling requires 45 Watts per m&sup3;. What power cooling unit is required?", 55),
           ("Question 14: Van Tyre Replacement", "[4 Marks]", "Tyres cost £95 each. A fleet replaces all 4 tyres on 15 vans. The supplier offers 'Buy 3 get 1 free' on every van. Calculate total cost.", 55)
         ]),

        # Paper 3
        ("Mock Paper 3: Retail Business, Commercial Health & Sales",
         [
           ("Question 1", "[4 Marks]", "Calculate: <code>345.8 - 187.94</code> without a calculator. Show columnar working.", 55),
           ("Question 2", "[4 Marks]", "A retailer buys stock for £450 and sells it for £630. Calculate the percentage profit margin on cost.", 65),
           ("Question 3", "[4 Marks]", "Divide £720 in the ratio 5 : 3 : 1. Show all steps.", 55),
           ("Question 4", "[4 Marks]", "Evaluate: <code>18 - 4 &times; (6 - 2)&sup2; &divide; 8</code> following order of operations (BIDMAS).", 65)
         ],
         [
           ("Question 5: Staff Commission", "[5 Marks]", "Sales staff earn a basic salary of £1,800 per month plus 3.5% commission on all sales exceeding £15,000. Sarah generates £38,000 in sales. Calculate her monthly earnings.", 60),
           ("Question 6: Store Flooring & Underlay", "[5 Marks]", "A shop floor is a trapezium with parallel sides 14m and 18m, and perpendicular depth 10m. Carpet tiles cost £18.50 per m&sup2;. Calculate total flooring cost.", 60),
           ("Question 7: Sales Promotion Comparison", "[5 Marks]", "Option A: 25% off £80 coat. Option B: £80 coat with £15 voucher and an extra 10% off the remaining balance. Which option is cheaper and by how much?", 60),
           ("Question 8: Break-Even Analysis", "[5 Marks]", "Fixed store costs are £6,000 per month. An item is sold for £25 and costs £13 to produce. How many items must be sold each month to break even?", 60),
           ("Question 9: Customer Footfall Data", "[5 Marks]", "Daily footfall across two weeks: Mean = 450, Range = 120. Second store: Mean = 510, Range = 240. Compare the performance and consistency of the two stores.", 60),
           ("Question 10: VAT Reconciliation", "[5 Marks]", "Total gross sales takings are £43,200 including 20% VAT. Calculate the net sales takings and the amount of VAT owed to HMRC.", 60),
           ("Question 11: Stock Turnover Ratio", "[5 Marks]", "Cost of goods sold is £180,000. Average inventory held is £30,000. Calculate stock turnover rate and average days to sell stock (365 days).", 60),
           ("Question 12: Customer Survey Probability", "[5 Marks]", "In a survey of 200 customers, 140 rated service as excellent. If 2 customers are selected at random, what is the probability that both rated service as excellent?", 60),
           ("Question 13: Display Lighting", "[4 Marks]", "LED spotlights consume 12 Watts each. 40 spotlights run 10 hours a day for 30 days. Electricity costs 28p per kWh. Calculate lighting electricity cost.", 55),
           ("Question 14: Delivery Fuel Cost", "[4 Marks]", "Delivery van travels 1,200 miles a month averaging 35 mpg. Diesel costs £1.45 per litre (4.55 litres per gallon). Calculate monthly fuel expenditure.", 55)
         ]),

        # Paper 4
        ("Mock Paper 4: Healthcare Facilities & Community Wellbeing",
         [
           ("Question 1", "[4 Marks]", "Calculate: <code>2.4 &times; 0.15</code> without using a calculator. Show your method.", 55),
           ("Question 2", "[4 Marks]", "A medicine bottle holds 250 ml. A patient takes two 7.5 ml doses each day. How many full days will the bottle last?", 65),
           ("Question 3", "[4 Marks]", "Express 36 as a percentage of 150 without a calculator.", 55),
           ("Question 4", "[4 Marks]", "A community health budget was cut by 8% to £82,800. What was the budget before the cut? Check your answer.", 65)
         ],
         [
           ("Question 5: Hospital Staffing Rota", "[5 Marks]", "A ward requires 1 registered nurse per 6 patients. There are 42 patients. Nurses work 12-hour shifts. Over 7 days, how many nurse-shifts are needed in total?", 60),
           ("Question 6: Nutrition Energy Intake", "[5 Marks]", "A meal contains 45g protein (4 kcal/g), 60g carbohydrates (4 kcal/g), and 20g fat (9 kcal/g). Calculate the total calories and the percentage of calories from fat.", 60),
           ("Question 7: Clinic Refurbishment Plan", "[5 Marks]", "A clinic room is 7.5m by 5.2m with height 2.8m. Walls are to be painted. Windows and doors cover 12 m&sup2;. One 5-litre tin covers 35 m&sup2; with 2 coats. How many tins are needed?", 60),
           ("Question 8: Ambulance Response Times", "[5 Marks]", "Response times (mins): 0-7 (12), 8-15 (28), 16-23 (8), 24-31 (2). Calculate the estimated mean response time. Does it meet the 12-minute target?", 60),
           ("Question 9: Body Mass Index (BMI)", "[5 Marks]", "Formula: <code>BMI = Weight (kg) &divide; [Height (m)]&sup2;</code>. Patient weighs 84 kg and is 1.75 m tall. Calculate BMI and classify (Healthy: 18.5–24.9, Overweight: 25–29.9, Obese: 30+).", 60),
           ("Question 10: Medicine Dilution Ratio", "[5 Marks]", "Antiseptic solution is diluted with water in the ratio 1 : 19. A nurse prepares 4 litres of diluted solution. How many millilitres of concentrated antiseptic are needed?", 60),
           ("Question 11: Blood Pressure Statistics", "[5 Marks]", "Systolic readings for Group A: Mean = 128, Range = 18. Group B: Mean = 135, Range = 32. Compare the blood pressure levels and variation between the two groups.", 60),
           ("Question 12: Screening Diagnostic Probability", "[5 Marks]", "A test has a 95% accuracy rate. Two independent samples are tested. What is the probability that both tests produce an accurate result?", 60),
           ("Question 13: Hydrotherapy Pool Volume", "[4 Marks]", "A pool is 10m long, 4m wide, and has an average depth of 1.4m. Calculate pool water volume in litres (1 m&sup3; = 1,000 litres).", 55),
           ("Question 14: Equipment Loan Depreciation", "[4 Marks]", "A medical scanner bought for £45,000 depreciates by 15% each year. Calculate its book value after 2 years.", 55)
         ]),

        # Paper 5
        ("Mock Paper 5: Construction, Eco-Building & Solar Installation",
         [
           ("Question 1", "[4 Marks]", "Calculate: <code>4.8 &divide; 0.06</code> without a calculator. Show your method.", 55),
           ("Question 2", "[4 Marks]", "A roof slope forms a right-angled triangle with base 6m and rise 2.5m. Calculate the slope length using Pythagoras (use a calculator or exact method).", 65),
           ("Question 3", "[4 Marks]", "Calculate: <code>4 &frac12; &divide; 1 &frac14;</code>. Give your answer as a simplified fraction or mixed number.", 55),
           ("Question 4", "[4 Marks]", "A builder orders timber with a 20% trade discount. The discounted total is £1,440. Calculate the original cost.", 65)
         ],
         [
           ("Question 5: Solar Panel Array", "[5 Marks]", "A roof has dimensions 10m by 6m. Each solar panel is 1.6m by 1m. Panels must be placed with 0.5m clearance from roof edges. How many panels can be installed?", 60),
           ("Question 6: Solar Energy Generation", "[5 Marks]", "A 4 kW system generates 3,600 kWh annually. 60% of electricity is used on-site (saving 28p/kWh), and 40% is exported to the grid (earning 15p/kWh). Calculate total annual financial return.", 60),
           ("Question 7: Concrete Foundation Footing", "[5 Marks]", "A trench foundation is 25m long, 0.6m wide, and 0.8m deep. Concrete costs £115 per cubic metre. Calculate the cost of concrete required.", 60),
           ("Question 8: Insulation Payback Period", "[5 Marks]", "Cavity wall insulation costs £1,800. It reduces annual heating bills by 22%. Current annual heating bill is £1,500. Calculate the payback period in years.", 60),
           ("Question 9: Scaffold Load Safety", "[5 Marks]", "Scaffold platform area is 15 m&sup2;. Safe working load is 250 kg/m&sup2;. Total workers and equipment weigh 3.2 tonnes. Is the platform safely loaded?", 60),
           ("Question 10: Scale Site Plan", "[5 Marks]", "On a 1 : 50 architectural drawing, a driveway is 14 cm long. Asphalt surfacing costs £45 per linear metre. Calculate driveway surfacing cost.", 60),
           ("Question 11: Rainwater Harvesting Tank", "[5 Marks]", "A cylindrical rainwater tank has diameter 1.8m and height 2m. How many litres of rainwater can it store? (use &pi; = 3.142).", 60),
           ("Question 12: Heat Pump Efficiency (COP)", "[5 Marks]", "A heat pump consumes 2.4 kW of electrical power and produces 8.4 kW of thermal heat. Calculate the Coefficient of Performance (COP = Heat Output &divide; Power Input).", 60),
           ("Question 13: Timber Decking Perimeter", "[4 Marks]", "A rectangular deck is 7.5m by 4.8m. Timber fascia edging costs £6.50 per metre. Calculate the total cost of edging the deck.", 55),
           ("Question 14: Thermal Imaging Survey", "[4 Marks]", "Temperature readings (&deg;C) across 10 wall points: Mean = 16.5, Range = 4.2. After insulation: Mean = 19.8, Range = 1.1. Compare the wall temperature and thermal consistency.", 55)
         ]),

        # Paper 6
        ("Mock Paper 6: Hospitality, Catering Operations & Hotel Management",
         [
           ("Question 1", "[4 Marks]", "Calculate: <code>57.6 &divide; 1.2</code> without using a calculator. Show your method.", 55),
           ("Question 2", "[4 Marks]", "A circular banquet table has diameter 1.8 m. A tablecloth is cut to have a 0.2 m drop (overhang) all round the edge. Calculate the total area of the circular cloth (use &pi; = 3.14).", 65),
           ("Question 3", "[4 Marks]", "A baker scales a dessert recipe: <code>3 &frac12; &times; 2 &frac23;</code> kg of flour. Calculate the exact quantity in simplest fraction form.", 55),
           ("Question 4", "[4 Marks]", "A restaurant bill is £158.40 including 20% VAT. Calculate the net food and drink cost before VAT. Show a check.", 65)
         ],
         [
           ("Question 5: Hotel RevPAR & Occupancy", "[5 Marks]", "A hotel has 120 rooms. Over a 30-day month, 2,880 room-nights were sold, generating £244,800 room revenue. Calculate: a) Occupancy rate (%), b) Average Daily Rate (ADR), c) RevPAR (Revenue Per Available Room).", 60),
           ("Question 6: Chef Food Cost Percentage", "[5 Marks]", "A dish sells for £18.50 excluding VAT. Ingredients cost: 200g beef fillet (£28/kg), 150g potatoes (£1.20/kg), garnish & sauce (£0.85). Calculate the food cost percentage. Is it within the target 32% limit?", 60),
           ("Question 7: Walk-in Freezer Pull-Down", "[5 Marks]", "A commercial freezer room measures 4m &times; 3.5m &times; 2.4m. It cools air from 18&deg;C to -18&deg;C. Cooling rate is 0.75&deg;C per minute. How long will the pull-down take in minutes and seconds?", 60),
           ("Question 8: Wedding Beverage Ratio", "[5 Marks]", "A wedding reception prepares 240 drinks. The ratio of Prosecco to Sparkling Elderflower is 5 : 3. Prosecco bottles serve 6 glasses each. How many bottles of Prosecco must be uncorked?", 60),
           ("Question 9: Dining Satisfaction Survey", "[5 Marks]", "Ratings from 60 diners: 1-2 stars (3), 3-4 stars (9), 5-6 stars (18), 7-8 stars (22), 9-10 stars (8). Calculate the estimated mean score to 1 decimal place.", 60),
           ("Question 10: Energy Utility Audit", "[5 Marks]", "Commercial kitchen gas ovens use 35,000 kWh at 7.2p/kWh. Electric combi-steamers use 22,000 kWh at 24.5p/kWh. Calculate the total annual cooking utility bill.", 60),
           ("Question 11: Overseas Tour Currency", "[5 Marks]", "A French tour group pays a hotel deposit of &euro;8,500. The hotel exchange rate is &pound;1 = &euro;1.16, with a 2% foreign exchange handling fee deducted. Calculate the net GBP credited to hotel.", 60),
           ("Question 12: Cancellation Probability", "[5 Marks]", "Historical data shows a 12% probability that a weekend booking is cancelled. Two independent suites are booked for Saturday. What is the probability that BOTH suites arrive (neither cancels)?", 60),
           ("Question 13: Airport Shuttle Transit", "[4 Marks]", "A hotel shuttle van runs 38 miles to the airport at an average speed of 40 mph. It departs the hotel at 05:45. What time does it arrive at the terminal?", 55),
           ("Question 14: Weekend Overtime Pay", "[4 Marks]", "A sous-chef earns £14.00/hr basic for 35 hours. Overtime is paid at 1.5 &times; basic. The chef works 44 hours in a festival week. Calculate the total gross weekly pay.", 55)
         ]),

        # Paper 7
        ("Mock Paper 7: Manufacturing, Precision Engineering & Quality Control",
         [
           ("Question 1", "[4 Marks]", "Calculate: <code>142.045 - 89.378</code> without using a calculator. Show columnar alignment.", 55),
           ("Question 2", "[4 Marks]", "A steel mounting bracket is a trapezium with parallel edges 16 cm and 24 cm, and perpendicular height 12 cm. Calculate the bracket surface area.", 65),
           ("Question 3", "[4 Marks]", "Evaluate: <code>7/8 &divide; 3/16</code>. Express as a fully simplified mixed number.", 55),
           ("Question 4", "[4 Marks]", "A production process time was reduced by 15% to 68 seconds through automation. Calculate the original cycle time in seconds. Show a check.", 65)
         ],
         [
           ("Question 5: CNC Machining Kerf & Wastage", "[5 Marks]", "Steel bars of length 3.2 m are cut into pins of length 145 mm. The saw blade kerf wastes 3 mm per cut. How many full pins can be cut from 1 bar, and what length of offcut remains?", 60),
           ("Question 6: Bushing Mass & Density", "[5 Marks]", "A cylindrical brass bushing has outer diameter 50 mm, inner hole diameter 30 mm, and length 80 mm. Brass density is 8.5 g/cm&sup3;. Calculate the bushing mass in grams (use &pi; = 3.142).", 60),
           ("Question 7: Machine Tolerance Bounds", "[5 Marks]", "A shaft specification is 25.00 mm &plusmn; 0.08 mm. Five sample shafts measure: 24.94, 25.06, 25.09, 24.91, 25.02 mm. Which shafts fail quality inspection? Calculate the percentage pass rate.", 60),
           ("Question 8: Overall Equipment Effectiveness", "[5 Marks]", "Availability = 92%, Performance rate = 88%, Quality yield = 95%. Calculate the Overall Equipment Effectiveness percentage (OEE = A &times; P &times; Q). Is it above the world-class 75% benchmark?", 60),
           ("Question 9: Defect Frequency Distribution", "[5 Marks]", "Defects per 1,000 components across 50 production shifts: 0-4 (18 shifts), 5-9 (20 shifts), 10-14 (9 shifts), 15-19 (3 shifts). Calculate the estimated mean defect rate.", 60),
           ("Question 10: Epoxy Factory Flooring", "[5 Marks]", "A factory bay measures 32 m by 18 m on a 1 : 100 site blueprint. High-durability epoxy coating costs £28.50 per m&sup2; applied. Calculate the total cost to coat the bay.", 60),
           ("Question 11: Bulk Fastener Pricing", "[5 Marks]", "Bolts cost £0.45 each. Orders over 2,000 units receive a 12% bulk discount. Orders over 5,000 units receive an 18% discount. Calculate the invoice cost for 4,500 bolts.", 60),
           ("Question 12: Dual-Sensor Reliability", "[5 Marks]", "An automated robotic cell uses two independent optical sensors. Sensor 1 has a 0.98 reliability rating; Sensor 2 has a 0.95 reliability rating. What is the probability that both sensors trigger successfully?", 60),
           ("Question 13: Conveyor Velocity", "[4 Marks]", "A packaging conveyor moves at 0.45 m/s. A carton travels 36 metres along the belt. How many seconds does the transit take? Convert to minutes and seconds.", 55),
           ("Question 14: CNC Milling Depreciation", "[4 Marks]", "A 5-axis milling machine costs £85,000. It depreciates by 12% in Year 1 and 10% of its remaining value in Year 2. Calculate its book value at the end of Year 2.", 55)
         ]),

        # Paper 8
        ("Mock Paper 8: Renewable Energy, Agricultural Technology & Environmental Science",
         [
           ("Question 1", "[4 Marks]", "Calculate: <code>375 &times; 48</code> without using a calculator. Show your long multiplication working.", 55),
           ("Question 2", "[4 Marks]", "A farm irrigation reservoir is 45 m long and 30 m wide with vertical depth 3 m. Calculate the area of waterproof geomembrane needed to line the base and four vertical sides.", 65),
           ("Question 3", "[4 Marks]", "A fertilizer mix combines Nitrogen, Phosphorus, and Potassium in the ratio 4 : 2 : 1. A farmer needs 350 kg of mixed fertilizer. How many kg of Nitrogen are needed?", 55),
           ("Question 4", "[4 Marks]", "An environmental farm stewardship grant was reduced by 12% to £39,600. What was the grant amount before the reduction? Show an inverse check.", 65)
         ],
         [
           ("Question 5: Wind Turbine Capacity Factor", "[5 Marks]", "A 2.5 MW wind turbine operates for 30 days (720 hours). Maximum theoretical output is 1,800 MWh. Actual generation was 648 MWh. Calculate the turbine's capacity factor percentage.", 60),
           ("Question 6: Cylindrical Grain Silo", "[5 Marks]", "A grain silo is a cylinder with diameter 6 m and height 14 m. Grain has a bulk density of 0.78 tonnes/m&sup3;. Calculate maximum silo grain capacity in tonnes (use &pi; = 3.142).", 60),
           ("Question 7: Field Harvest Yield Comparison", "[5 Marks]", "Field North: 18 hectares, yields 153 tonnes of wheat. Field South: 24 hectares, yields 198 tonnes of wheat. Which field achieved the higher yield per hectare, and by how many tonnes/ha?", 60),
           ("Question 8: Solar Farm Ground Coverage", "[5 Marks]", "A 5-hectare solar field (1 hectare = 10,000 m&sup2;) contains 8,200 panels, each 1.95 m &times; 1.1 m. Calculate the percentage of field ground area directly covered by photovoltaic panels.", 60),
           ("Question 9: Annual Rainfall Comparison", "[5 Marks]", "Valley Station: Mean monthly rainfall = 74 mm, Range = 48 mm. Moorland Station: Mean = 112 mm, Range = 94 mm. Compare the rainfall levels and seasonal consistency between the two stations.", 60),
           ("Question 10: Biomass Heating & Carbon Offset", "[5 Marks]", "Wood pellets cost £280 per tonne and release 4,800 kWh/tonne. Heating oil costs 72p/litre and provides 10 kWh/litre. Calculate the cost to produce 96,000 kWh of heat with each fuel and state the saving.", 60),
           ("Question 11: Glamping Pod Diversification", "[5 Marks]", "A farm installs 3 glamping pods for £42,000 total. Each pod rents for £120/night, with projected occupancy of 140 nights per pod per year. Annual running costs are £7,500 total. Calculate the payback period in years.", 60),
           ("Question 12: Frost Damage Probability", "[5 Marks]", "During April blossom, probability of severe frost on any given night is 0.15. What is the probability that frost occurs on at least one of two consecutive nights?", 60),
           ("Question 13: Tractor Diesel Expenditure", "[4 Marks]", "A tractor uses 14.5 litres of diesel per hectare. It ploughs a 65-hectare field. Red diesel costs £0.88 per litre. Calculate the total fuel cost for ploughing the field.", 55),
           ("Question 14: Borehole Water Delivery", "[4 Marks]", "A borehole pump delivers 85 litres of water per minute into a 25,000-litre livestock storage header tank. How long will it take to fill the tank from empty? Give your answer in hours and minutes.", 55)
         ])
    ]

    for p_idx, (p_title, sec_a_qs, sec_b_qs) in enumerate(papers_data, 1):
        # 7 Pages per Paper: Pages 6 to 61
        base_page = 6 + (p_idx - 1) * 7

        # Paper Page 1: Sec A Q1, Q2
        pages.append(f"""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Maths L2 &bull; Paper {p_idx}</div>
    <div class="page-header-strand">Section A: Non-Calculator (16 Marks)</div>
  </div>

  <h2>{p_title}</h2>
  <div class="card-trap" style="margin-bottom:8px;">
    <strong>Section A Instructions:</strong> Duration: 25 minutes. <strong>NO CALCULATOR PERMITTED</strong>. Show all intermediate calculation steps to secure process marks.
  </div>

  <div style="margin-bottom:10px;">
    <div style="display:flex; justify-content:space-between;"><strong>{sec_a_qs[0][0]}:</strong> <span class="mark-badge">{sec_a_qs[0][1]}</span></div>
    <p style="margin:2px 0 4px 0;">{sec_a_qs[0][2]}</p>
    <div class="workspace-ruled" style="min-height:{sec_a_qs[0][3]}px;">Show working here...</div>
  </div>

  <div style="margin-bottom:8px;">
    <div style="display:flex; justify-content:space-between;"><strong>{sec_a_qs[1][0]}:</strong> <span class="mark-badge">{sec_a_qs[1][1]}</span></div>
    <p style="margin:2px 0 4px 0;">{sec_a_qs[1][2]}</p>
    <div class="workspace-grid" style="min-height:{sec_a_qs[1][3]}px;">Grid workspace...</div>
  </div>

  <div class="page-footer">
    <div>Paper {p_idx} &bull; Section A (Non-Calculator) &bull; Page 1 of 2</div>
    <div class="page-num">Page {base_page}</div>
  </div>
</div>
""")

        # Paper Page 2: Sec A Q3, Q4
        pages.append(f"""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Maths L2 &bull; Paper {p_idx}</div>
    <div class="page-header-strand">Section A: Non-Calculator (16 Marks)</div>
  </div>

  <div style="margin-bottom:10px;">
    <div style="display:flex; justify-content:space-between;"><strong>{sec_a_qs[2][0]}:</strong> <span class="mark-badge">{sec_a_qs[2][1]}</span></div>
    <p style="margin:2px 0 4px 0;">{sec_a_qs[2][2]}</p>
    <div class="workspace-ruled" style="min-height:{sec_a_qs[2][3]}px;">Show working here...</div>
  </div>

  <div style="margin-bottom:8px;">
    <div style="display:flex; justify-content:space-between;"><strong>{sec_a_qs[3][0]}:</strong> <span class="mark-badge">{sec_a_qs[3][1]}</span></div>
    <p style="margin:2px 0 4px 0;">{sec_a_qs[3][2]}</p>
    <div class="workspace-ruled" style="min-height:{sec_a_qs[3][3]}px;">Show working and check here...</div>
  </div>

  <div class="card-tip" style="margin-top:auto;">
    <strong>End of Section A:</strong> Ensure you check your calculations before proceeding to Section B. Calculator use is strictly prohibited for these 4 questions.
  </div>

  <div class="page-footer">
    <div>Paper {p_idx} &bull; Section A (Non-Calculator) &bull; Page 2 of 2</div>
    <div class="page-num">Page {base_page + 1}</div>
  </div>
</div>
""")

        # Paper Page 3: Sec B Q5, Q6
        pages.append(f"""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Maths L2 &bull; Paper {p_idx}</div>
    <div class="page-header-strand">Section B: Calculator (48 Marks)</div>
  </div>

  <div class="card-method" style="margin-bottom:8px;">
    <strong>Section B Instructions:</strong> Duration: 1 hour 20 minutes (80 mins). Marks: 48 Marks. Calculators <strong>permitted</strong>. Show all key formula substitutions.
  </div>

  <div style="margin-bottom:10px;">
    <div style="display:flex; justify-content:space-between;"><strong>{sec_b_qs[0][0]}:</strong> <span class="mark-badge">{sec_b_qs[0][1]}</span></div>
    <p style="margin:2px 0 4px 0;">{sec_b_qs[0][2]}</p>
    <div class="workspace-ruled" style="min-height:{sec_b_qs[0][3]}px;">Show working here...</div>
  </div>

  <div style="margin-bottom:8px;">
    <div style="display:flex; justify-content:space-between;"><strong>{sec_b_qs[1][0]}:</strong> <span class="mark-badge">{sec_b_qs[1][1]}</span></div>
    <p style="margin:2px 0 4px 0;">{sec_b_qs[1][2]}</p>
    <div class="workspace-ruled" style="min-height:{sec_b_qs[1][3]}px;">Show working here...</div>
  </div>

  <div class="page-footer">
    <div>Paper {p_idx} &bull; Section B (Calculator) &bull; Page 1 of 5</div>
    <div class="page-num">Page {base_page + 2}</div>
  </div>
</div>
""")

        # Paper Page 4: Sec B Q7, Q8
        pages.append(f"""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Maths L2 &bull; Paper {p_idx}</div>
    <div class="page-header-strand">Section B: Calculator (48 Marks)</div>
  </div>

  <div style="margin-bottom:10px;">
    <div style="display:flex; justify-content:space-between;"><strong>{sec_b_qs[2][0]}:</strong> <span class="mark-badge">{sec_b_qs[2][1]}</span></div>
    <p style="margin:2px 0 4px 0;">{sec_b_qs[2][2]}</p>
    <div class="workspace-grid" style="min-height:{sec_b_qs[2][3]}px;">Grid workspace...</div>
  </div>

  <div style="margin-bottom:8px;">
    <div style="display:flex; justify-content:space-between;"><strong>{sec_b_qs[3][0]}:</strong> <span class="mark-badge">{sec_b_qs[3][1]}</span></div>
    <p style="margin:2px 0 4px 0;">{sec_b_qs[3][2]}</p>
    <div class="workspace-ruled" style="min-height:{sec_b_qs[3][3]}px;">Show working here...</div>
  </div>

  <div class="page-footer">
    <div>Paper {p_idx} &bull; Section B (Calculator) &bull; Page 2 of 5</div>
    <div class="page-num">Page {base_page + 3}</div>
  </div>
</div>
""")

        # Paper Page 5: Sec B Q9, Q10
        pages.append(f"""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Maths L2 &bull; Paper {p_idx}</div>
    <div class="page-header-strand">Section B: Calculator (48 Marks)</div>
  </div>

  <div style="margin-bottom:10px;">
    <div style="display:flex; justify-content:space-between;"><strong>{sec_b_qs[4][0]}:</strong> <span class="mark-badge">{sec_b_qs[4][1]}</span></div>
    <p style="margin:2px 0 4px 0;">{sec_b_qs[4][2]}</p>
    <div class="workspace-ruled" style="min-height:{sec_b_qs[4][3]}px;">Show working here...</div>
  </div>

  <div style="margin-bottom:8px;">
    <div style="display:flex; justify-content:space-between;"><strong>{sec_b_qs[5][0]}:</strong> <span class="mark-badge">{sec_b_qs[5][1]}</span></div>
    <p style="margin:2px 0 4px 0;">{sec_b_qs[5][2]}</p>
    <div class="workspace-grid" style="min-height:{sec_b_qs[5][3]}px;">Grid workspace...</div>
  </div>

  <div class="page-footer">
    <div>Paper {p_idx} &bull; Section B (Calculator) &bull; Page 3 of 5</div>
    <div class="page-num">Page {base_page + 4}</div>
  </div>
</div>
""")

        # Paper Page 6: Sec B Q11, Q12
        pages.append(f"""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Maths L2 &bull; Paper {p_idx}</div>
    <div class="page-header-strand">Section B: Calculator (48 Marks)</div>
  </div>

  <div style="margin-bottom:10px;">
    <div style="display:flex; justify-content:space-between;"><strong>{sec_b_qs[6][0]}:</strong> <span class="mark-badge">{sec_b_qs[6][1]}</span></div>
    <p style="margin:2px 0 4px 0;">{sec_b_qs[6][2]}</p>
    <div class="workspace-ruled" style="min-height:{sec_b_qs[6][3]}px;">Show working here...</div>
  </div>

  <div style="margin-bottom:8px;">
    <div style="display:flex; justify-content:space-between;"><strong>{sec_b_qs[7][0]}:</strong> <span class="mark-badge">{sec_b_qs[7][1]}</span></div>
    <p style="margin:2px 0 4px 0;">{sec_b_qs[7][2]}</p>
    <div class="workspace-ruled" style="min-height:{sec_b_qs[7][3]}px;">Show working here...</div>
  </div>

  <div class="page-footer">
    <div>Paper {p_idx} &bull; Section B (Calculator) &bull; Page 4 of 5</div>
    <div class="page-num">Page {base_page + 5}</div>
  </div>
</div>
""")

        # Paper Page 7: Sec B Q13, Q14
        pages.append(f"""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Maths L2 &bull; Paper {p_idx}</div>
    <div class="page-header-strand">Section B: Calculator (48 Marks)</div>
  </div>

  <div style="margin-bottom:10px;">
    <div style="display:flex; justify-content:space-between;"><strong>{sec_b_qs[8][0]}:</strong> <span class="mark-badge">{sec_b_qs[8][1]}</span></div>
    <p style="margin:2px 0 4px 0;">{sec_b_qs[8][2]}</p>
    <div class="workspace-ruled" style="min-height:{sec_b_qs[8][3]}px;">Show working here...</div>
  </div>

  <div style="margin-bottom:8px;">
    <div style="display:flex; justify-content:space-between;"><strong>{sec_b_qs[9][0]}:</strong> <span class="mark-badge">{sec_b_qs[9][1]}</span></div>
    <p style="margin:2px 0 4px 0;">{sec_b_qs[9][2]}</p>
    <div class="workspace-grid" style="min-height:{sec_b_qs[9][3]}px;">Grid workspace...</div>
  </div>

  <div class="card-tip" style="margin-top:auto;">
    <strong>End of Paper {p_idx}:</strong> Review your units, check rounding instructions, and ensure all inverse checks are completed.
  </div>

  <div class="page-footer">
    <div>Paper {p_idx} &bull; Section B (Calculator) &bull; Page 5 of 5</div>
    <div class="page-num">Page {base_page + 6}</div>
  </div>
</div>
""")

    # -------------------------------------------------------------
    # 22 PAGES OF OFFICIAL EXAMINER MARK SCHEMES (Pages 62 to 83)
    # -------------------------------------------------------------
    mark_schemes = [
        # Page 62: Paper 1 Mark Scheme (Part 1 - Section A)
        ("Official Mark Scheme &bull; Paper 1 (Section A)",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Q</th><th>Mark Scheme &amp; Step-by-Step Method</th><th>Marks</th></tr>
           <tr><td><strong>1</strong></td><td>45.6 &times; 3.8 &rarr; 456 &times; 38 = 17,328. Count 2 decimal places: <strong>173.28</strong>. [P1] for integer multiplication method, [A1] for correct digits 17328, [A1] for correct decimal place 173.28, [B1] for clear columnar working.</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>2</strong></td><td>Hall Area = 8.5 &times; 6 = 51 m&sup2; [P1]. Dance floor Area = 3.14 &times; 2&sup2; = 3.14 &times; 4 = 12.56 m&sup2; [P1]. Carpet remaining = 51 - 12.56 = <strong>38.44 m&sup2;</strong> [A1]. [B1] for m&sup2; units.</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>3</strong></td><td>2 &frac34; + 1 &frac23; &rarr; 11/4 + 5/3 = (33 + 20) / 12 = 53/12 [P1, P1]. Convert to mixed number: <strong>4 <sup>5</sup>/<sub>12</sub></strong> [A1]. [B1] for simplest form.</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>4</strong></td><td>100% - 15% = 85% [P1]. £510 &divide; 0.85 = <strong>£600</strong> [P1, A1]. Check: 15% of 600 = £90 &rarr; 600 - 90 = £510 [B1].</td><td><strong>[4]</strong></td></tr>
         </table>"""),

        # Page 63: Paper 1 Mark Scheme (Part 2 - Section B Q5 to Q9)
        ("Official Mark Scheme &bull; Paper 1 (Section B Q5–Q9)",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Q</th><th>Mark Scheme &amp; Step-by-Step Method</th><th>Marks</th></tr>
           <tr><td><strong>5</strong></td><td>Lunch: 160 &times; £14.50 = £2,320 [P1]. Wine bottles: 160 &divide; 4 = 40 bottles [P1]. Wine cost: 40 &times; £8.40 = £336 [P1]. Subtotal: 2,320 + 336 = £2,656. Service charge: 10% of 2,656 = £265.60 [P1]. Total invoice = <strong>£2,921.60</strong> [A1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>6</strong></td><td>Stewards: 12 &times; 7.5 = 90 hours [P1]. Cost = 90 &times; £11.44 = £1,029.60 [P1]. Supervisors: 3 &times; 8 = 24 hours &times; £16.50 = £396 [P1]. Total wage bill: 1,029.60 + 396 = <strong>£1,425.60</strong> [A1]. [B1] for correct pence format.</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>7</strong></td><td>Required heating = 750 &times; 0.025 = 18.75 kW [P1, P1]. Compare: Heater output is 15 kW [P1]. <strong>No, heater is inadequate</strong> [A1] as it is 3.75 kW short of the 18.75 kW requirement [B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>8</strong></td><td>Total hours: (3 &times; 24) + 8 = 72 + 8 = 80 hours [P1]. Total litres: 80 &times; 4.2 = 336 litres [P1]. Total cost: 336 &times; £1.42 = <strong>£477.12</strong> [P1, A1]. [B1] for correct units.</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>9</strong></td><td>Midpoints: 1.5, 3.5, 5.5, 7.5 [P1]. fx products: (1.5&times;4)=6; (3.5&times;12)=42; (5.5&times;16)=88; (7.5&times;8)=60 [P1]. &Sigma;fx = 6 + 42 + 88 + 60 = 196 [P1]. Mean = 196 &divide; 40 = <strong>4.9 stars</strong> [A1, B1].</td><td><strong>[5]</strong></td></tr>
         </table>"""),

        # Page 64: Paper 1 Mark Scheme (Part 3 - Section B Q10 to Q14)
        ("Official Mark Scheme &bull; Paper 1 (Section B Q10–Q14)",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Q</th><th>Mark Scheme &amp; Step-by-Step Method</th><th>Marks</th></tr>
           <tr><td><strong>10</strong></td><td>Real dimensions: 12.5 &times; 200 = 2,500 cm = 25 m; 8 &times; 200 = 1,600 cm = 16 m [P1, P1]. Real Area = 25 &times; 16 = 400 m&sup2; [P1]. Paving cost = 400 &times; £24 = <strong>£9,600</strong> [A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>11</strong></td><td>Profit = 18,400 - 12,800 = £5,600 [P1]. Percentage = (5,600 &divide; 18,400) &times; 100 [P1, P1] = 30.434...% &rarr; <strong>30.4%</strong> [A1]. [B1] for rounding to 1 d.p.</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>12</strong></td><td>P(not winning A) = 24/25 = 0.96 [P1]. P(not winning B) = 39/40 = 0.975 [P1]. Combined: 0.96 &times; 0.975 [P1] = <strong>0.936 (or 117/125 or 93.6%)</strong> [A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>13</strong></td><td>Time = 110 &divide; 44 = 2.5 hours = 2 hours 30 mins [P1, P1]. Departure: 14:45 + 2h 30m = <strong>17:15</strong> [A1, B1].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>14</strong></td><td>Radius = 1.2 &divide; 2 = 0.6 m [P1]. Volume = 3.142 &times; 0.6&sup2; &times; 2.5 = 3.142 &times; 0.36 &times; 2.5 = 2.8278 m&sup3; [P1]. Litres = 2.8278 &times; 1,000 = <strong>2,827.8 litres (or 2,828 litres)</strong> [A1, B1].</td><td><strong>[4]</strong></td></tr>
         </table>"""),

        # Page 65: Paper 2 Mark Scheme (Part 1 - Section A)
        ("Official Mark Scheme &bull; Paper 2 (Section A)",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Q</th><th>Mark Scheme &amp; Step-by-Step Method</th><th>Marks</th></tr>
           <tr><td><strong>1</strong></td><td>684 &divide; 18 = <strong>38</strong>. [P1] for long division setup, [M1] for 18 &times; 3 = 54, remainder 14, [A1] for 18 &times; 8 = 144, [B1] for exact quotient 38.</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>2</strong></td><td>Along length: 24 &divide; 1.2 = 20 pallets [P1]. Along width: 16 &divide; 0.8 = 20 pallets [P1]. Total pallets = 20 &times; 20 = <strong>400 pallets</strong> [A1]. Alternative orientation: (24&divide;0.8)&times;(16&divide;1.2) = 30 &times; 13.33 = 390. Max is 400 [B1].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>3</strong></td><td>3/5 &times; 4/7 = (3 &times; 4) / (5 &times; 7) = <strong>12/35</strong>. [P1] for multiplying numerators, [P1] for multiplying denominators, [A1] for 12/35, [B1] for noting it cannot be simplified further.</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>4</strong></td><td>Increase = £13.75 - £12.50 = £1.25 [P1]. Percentage = (1.25 &divide; 12.50) &times; 100 = <strong>10%</strong> [A1, B1]. Check: 10% of £12.50 = £1.25; 12.50 + 1.25 = £13.75 [B1].</td><td><strong>[4]</strong></td></tr>
         </table>"""),

        # Page 66: Paper 2 Mark Scheme (Part 2 - Section B Q5 to Q9)
        ("Official Mark Scheme &bull; Paper 2 (Section B Q5–Q9)",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Q</th><th>Mark Scheme &amp; Step-by-Step Method</th><th>Marks</th></tr>
           <tr><td><strong>5</strong></td><td>Van A gallons = 60 &divide; 4.55 = 13.187 gal &rarr; mpg = 420 &divide; 13.187 = 31.85 mpg [P1, P1]. Van B gallons = 52 &divide; 4.55 = 11.429 gal &rarr; mpg = 385 &divide; 11.429 = 33.69 mpg [P1, P1]. <strong>Van B achieves better mpg (33.7 vs 31.9)</strong> [A1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>6</strong></td><td>Total mass = 36 &times; 650 = 23,400 kg [P1, P1]. Convert tonnes: 23,400 &divide; 1,000 = 23.4 tonnes [P1]. Payload limit = 24 tonnes [P1]. <strong>No, not overloaded</strong> (23.4 tonnes &le; 24 tonnes, 0.6 tonnes spare) [A1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>7</strong></td><td>Total time = 3.5 hrs. Driving time = 3h 30m - 45m = 2h 45m = 2.75 hrs [P1, P1]. Speed = 168 &divide; 2.75 = <strong>61.09 mph (or 61.1 mph)</strong> [P1, A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>8</strong></td><td>Pythagoras: c&sup2; = 1.2&sup2; + 5&sup2; = 1.44 + 25 = 26.44 [P1, P1, P1]. c = &radic;26.44 = <strong>5.14 m</strong> [A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>9</strong></td><td>Midpoints: 14.5, 24.5, 34.5, 44.5 [P1]. fx: (14.5&times;5)=72.5; (24.5&times;14)=343; (34.5&times;21)=724.5; (44.5&times;10)=445 [P1]. &Sigma;fx = 1,585 [P1]. &Sigma;f = 50. Mean = 1,585 &divide; 50 = <strong>31.7 minutes</strong> [A1, B1].</td><td><strong>[5]</strong></td></tr>
         </table>"""),

        # Page 67: Paper 2 Mark Scheme (Part 3 - Section B Q10 to Q14)
        ("Official Mark Scheme &bull; Paper 2 (Section B Q10–Q14)",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Q</th><th>Mark Scheme &amp; Step-by-Step Method</th><th>Marks</th></tr>
           <tr><td><strong>10</strong></td><td>100% - 12% = 88% [P1]. Original = £3,960 &divide; 0.88 = <strong>£4,500</strong> [P1, A1]. Check: 12% of £4,500 = £540 &rarr; 4,500 - 540 = £3,960 [B1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>11</strong></td><td>Duty = 6% of €14,500 = €870 &rarr; Total EUR = €15,370 [P1, P1]. Convert GBP: 15,370 &divide; 1.15 = <strong>£13,365.22</strong> [P1, A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>12</strong></td><td>Successful deliveries = 850 - 34 = 816 [P1]. Percentage = (816 &divide; 850) &times; 100 = <strong>96.0%</strong> [P1, A1, B1]. Rounding confirmed [B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>13</strong></td><td>Room volume = 12 &times; 8 &times; 3.5 = 336 m&sup3; [P1]. Power = 336 &times; 45 W = <strong>15,120 Watts (or 15.12 kW)</strong> [P1, A1, B1].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>14</strong></td><td>15 vans &times; 4 tyres = 60 tyres. Deal: Pay for 3 out of 4 per van = 15 &times; 3 = 45 tyres paid for [P1, P1]. Total cost = 45 &times; £95 = <strong>£4,275</strong> [A1, B1].</td><td><strong>[4]</strong></td></tr>
         </table>"""),

        # Page 68: Paper 3 Mark Scheme (Part 1 - Section A)
        ("Official Mark Scheme &bull; Paper 3 (Section A)",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Q</th><th>Mark Scheme &amp; Step-by-Step Method</th><th>Marks</th></tr>
           <tr><td><strong>1</strong></td><td>345.80 - 187.94: Align decimal point [P1]. Subtract hundredths, tenths, units, tens [P1, P1]. Answer = <strong>157.86</strong> [A1].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>2</strong></td><td>Profit = 630 - 450 = £180 [P1]. Profit margin on cost = (180 &divide; 450) &times; 100 [P1] = <strong>40%</strong> [A1, B1].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>3</strong></td><td>Total parts = 5 + 3 + 1 = 9 parts [P1]. 1 part = 720 &divide; 9 = £80 [P1]. Shares: 5 &times; 80 = £400; 3 &times; 80 = £240; 1 &times; 80 = £80 [A1]. <strong>£400 : £240 : £80</strong> [B1].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>4</strong></td><td>BIDMAS: Brackets: (6 - 2) = 4 [P1]. Indices: 4&sup2; = 16 [P1]. Multiplication/Division: 4 &times; 16 &divide; 8 = 64 &divide; 8 = 8 [P1]. Subtraction: 18 - 8 = <strong>10</strong> [A1].</td><td><strong>[4]</strong></td></tr>
         </table>"""),

        # Page 69: Paper 3 Mark Scheme (Part 2 - Section B Q5 to Q9)
        ("Official Mark Scheme &bull; Paper 3 (Section B Q5–Q9)",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Q</th><th>Mark Scheme &amp; Step-by-Step Method</th><th>Marks</th></tr>
           <tr><td><strong>5</strong></td><td>Qualifying sales = 38,000 - 15,000 = £23,000 [P1]. Commission = 0.035 &times; 23,000 = £805 [P1, P1]. Total earnings = 1,800 + 805 = <strong>£2,605</strong> [A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>6</strong></td><td>Trapezium Area = &frac12;(14 + 18) &times; 10 = &frac12;(32) &times; 10 = 160 m&sup2; [P1, P1, P1]. Cost = 160 &times; £18.50 = <strong>£2,960</strong> [A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>7</strong></td><td>Option A: 25% off £80 &rarr; 80 &times; 0.75 = £60 [P1]. Option B: 80 - 15 = £65; 10% off 65 &rarr; 65 &times; 0.90 = £58.50 [P1, P1]. <strong>Option B is cheaper by £1.50</strong> (£60 - £58.50) [A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>8</strong></td><td>Contribution margin per item = £25 - £13 = £12 [P1, P1]. Break-even units = Fixed costs &divide; Contribution = £6,000 &divide; 12 = <strong>500 items</strong> [P1, A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>9</strong></td><td>Store 2 has higher average footfall (510 vs 450) [P1]. Store 1 is more consistent / reliable because its range is smaller (120 vs 240) [P1, P1]. Full comparison statement awarded [A1, B1].</td><td><strong>[5]</strong></td></tr>
         </table>"""),

        # Page 70: Paper 3 Mark Scheme (Part 3 - Section B Q10 to Q14)
        ("Official Mark Scheme &bull; Paper 3 (Section B Q10–Q14)",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Q</th><th>Mark Scheme &amp; Step-by-Step Method</th><th>Marks</th></tr>
           <tr><td><strong>10</strong></td><td>Gross = 120%. Net = £43,200 &divide; 1.20 = <strong>£36,000</strong> [P1, P1]. VAT owed = 43,200 - 36,000 = <strong>£7,200</strong> [A1, B1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>11</strong></td><td>Stock turnover = 180,000 &divide; 30,000 = <strong>6 times per year</strong> [P1, P1]. Average days = 365 &divide; 6 = <strong>60.8 days (or 61 days)</strong> [P1, A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>12</strong></td><td>P(first) = 140/200 = 0.70 [P1]. P(second) = 139/199 &asymp; 0.6985 [P1, P1]. Combined = 0.70 &times; (139/199) = <strong>0.489 (or 48.9%)</strong> [A1, B1]. (Accept with replacement: 0.7 &times; 0.7 = 0.49).</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>13</strong></td><td>Total Watts = 40 &times; 12 = 480 W = 0.48 kW [P1]. Total kWh = 0.48 &times; 10 &times; 30 = 144 kWh [P1]. Cost = 144 &times; £0.28 = <strong>£40.32</strong> [A1, B1].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>14</strong></td><td>Gallons = 1,200 &divide; 35 = 34.2857 gal [P1]. Litres = 34.2857 &times; 4.55 = 156.0 litres [P1]. Cost = 156.0 &times; £1.45 = <strong>£226.20</strong> [A1, B1].</td><td><strong>[4]</strong></td></tr>
         </table>"""),

        # Page 71: Paper 4 Mark Scheme (Part 1 - Section A)
        ("Official Mark Scheme &bull; Paper 4 (Section A)",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Q</th><th>Mark Scheme &amp; Step-by-Step Method</th><th>Marks</th></tr>
           <tr><td><strong>1</strong></td><td>24 &times; 15 = 360 [P1]. Count 3 decimal places (1 in 2.4, 2 in 0.15): <strong>0.36</strong> [P1, A1, B1].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>2</strong></td><td>Daily dosage = 2 &times; 7.5 = 15 ml [P1]. Full days = 250 &divide; 15 = 16.666... [P1, P1]. Answer = <strong>16 full days</strong> (reject 17) [A1].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>3</strong></td><td>(36 &divide; 150) &times; 100: Divide by 3 = 12/50 [P1]. Multiply by 2 = 24/100 = <strong>24%</strong> [P1, A1, B1].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>4</strong></td><td>100% - 8% = 92% [P1]. Original = £82,800 &divide; 0.92 = <strong>£90,000</strong> [P1, A1]. Check: 8% of 90,000 = 7,200; 90,000 - 7,200 = £82,800 [B1].</td><td><strong>[4]</strong></td></tr>
         </table>"""),

        # Page 72: Paper 4 Mark Scheme (Part 2 - Section B Q5 to Q9)
        ("Official Mark Scheme &bull; Paper 4 (Section B Q5–Q9)",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Q</th><th>Mark Scheme &amp; Step-by-Step Method</th><th>Marks</th></tr>
           <tr><td><strong>5</strong></td><td>Nurses on duty at any time = 42 &divide; 6 = 7 nurses [P1]. 2 shifts per 24h = 14 shifts per day [P1, P1]. Over 7 days: 14 &times; 7 = <strong>98 nurse-shifts</strong> [A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>6</strong></td><td>Protein = 45 &times; 4 = 180 kcal; Carbs = 60 &times; 4 = 240 kcal; Fat = 20 &times; 9 = 180 kcal [P1, P1]. Total = 180 + 240 + 180 = <strong>600 kcal</strong> [P1]. Fat % = (180 &divide; 600) &times; 100 = <strong>30%</strong> [A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>7</strong></td><td>Total wall area = 2 &times; (7.5 + 5.2) &times; 2.8 = 2 &times; 12.7 &times; 2.8 = 71.12 m&sup2; [P1]. Paint area = 71.12 - 12 = 59.12 m&sup2; [P1]. Tins needed = 59.12 &divide; 35 = 1.689 tins [P1]. Rounded up to whole tins = <strong>2 tins</strong> [A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>8</strong></td><td>Midpoints: 3.5, 11.5, 19.5, 27.5 [P1]. fx: (3.5&times;12)=42; (11.5&times;28)=322; (19.5&times;8)=156; (27.5&times;2)=55 [P1]. &Sigma;fx = 575 [P1]. Total calls = 50. Mean = 575 &divide; 50 = <strong>11.5 minutes</strong> [A1]. <strong>Yes, target is met</strong> (11.5 &lt; 12 mins) [B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>9</strong></td><td>Height squared = 1.75&sup2; = 3.0625 [P1]. BMI = 84 &divide; 3.0625 = <strong>27.4</strong> [P1, A1]. Classification: <strong>Overweight (25–29.9)</strong> [B1, B1].</td><td><strong>[5]</strong></td></tr>
         </table>"""),

        # Page 73: Paper 4 Mark Scheme (Part 3 - Section B Q10 to Q14)
        ("Official Mark Scheme &bull; Paper 4 (Section B Q10–Q14)",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Q</th><th>Mark Scheme &amp; Step-by-Step Method</th><th>Marks</th></tr>
           <tr><td><strong>10</strong></td><td>Total parts = 1 + 19 = 20 parts [P1]. 4 litres = 4,000 ml [P1]. Concentrated antiseptic = 4,000 &divide; 20 = <strong>200 ml</strong> [P1, A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>11</strong></td><td>Group B has higher average blood pressure (135 vs 128 mmHg) [P1, P1]. Group A readings are more consistent / less variable (range 18 vs 32 mmHg) [P1, A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>12</strong></td><td>P(both accurate) = 0.95 &times; 0.95 = <strong>0.9025 (or 90.25%)</strong>. [P1] for multiplying, [P1] for 0.95&sup2;, [A1] for 0.9025, [B1] for correct percentage conversion.</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>13</strong></td><td>Volume = 10 &times; 4 &times; 1.4 = 56 m&sup3; [P1, P1]. Litres = 56 &times; 1,000 = <strong>56,000 litres</strong> [A1, B1].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>14</strong></td><td>Year 1: 45,000 &times; 0.85 = £38,250 [P1]. Year 2: 38,250 &times; 0.85 = <strong>£32,512.50</strong> [P1, A1, B1].</td><td><strong>[4]</strong></td></tr>
         </table>"""),

        # Page 74: Paper 5 Mark Scheme (Part 1 - Section A)
        ("Official Mark Scheme &bull; Paper 5 (Section A)",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Q</th><th>Mark Scheme &amp; Step-by-Step Method</th><th>Marks</th></tr>
           <tr><td><strong>1</strong></td><td>4.8 &divide; 0.06 = 480 &divide; 6 = <strong>80</strong>. [P1] for multiplying numerator and denominator by 100, [P1] for setup, [A1] for 80, [B1] for inverse check.</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>2</strong></td><td>c&sup2; = 6&sup2; + 2.5&sup2; = 36 + 6.25 = 42.25 [P1, P1]. c = &radic;42.25 = <strong>6.5 m</strong> [A1, B1].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>3</strong></td><td>4 &frac12; &divide; 1 &frac14; &rarr; 9/2 &divide; 5/4 = 9/2 &times; 4/5 = 36/10 = 18/5 = <strong>3 &frac35; (or 3.6)</strong> [P1, P1, A1, B1].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>4</strong></td><td>100% - 20% = 80% [P1]. Original = £1,440 &divide; 0.80 = <strong>£1,800</strong> [P1, A1]. Check: 20% of 1,800 = 360 &rarr; 1,800 - 360 = £1,440 [B1].</td><td><strong>[4]</strong></td></tr>
         </table>"""),

        # Page 75: Paper 5 Mark Scheme (Part 2 - Section B Q5 to Q9)
        ("Official Mark Scheme &bull; Paper 5 (Section B Q5–Q9)",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Q</th><th>Mark Scheme &amp; Step-by-Step Method</th><th>Marks</th></tr>
           <tr><td><strong>5</strong></td><td>Usable length = 10 - (2 &times; 0.5) = 9 m [P1]. Usable width = 6 - (2 &times; 0.5) = 5 m [P1]. Orientation 1: (9 &divide; 1.6 = 5) &times; (5 &divide; 1 = 5) = 25 panels [P1]. Orientation 2: (9 &divide; 1 = 9) &times; (5 &divide; 1.6 = 3) = 27 panels [P1]. <strong>Maximum = 27 panels</strong> [A1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>6</strong></td><td>On-site use: 3,600 &times; 0.60 = 2,160 kWh &times; £0.28 = £604.80 [P1, P1]. Grid export: 3,600 &times; 0.40 = 1,440 kWh &times; £0.15 = £216.00 [P1]. Total annual return: 604.80 + 216 = <strong>£820.80</strong> [A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>7</strong></td><td>Volume = 25 &times; 0.6 &times; 0.8 = 12 m&sup3; [P1, P1]. Total concrete cost = 12 &times; £115 = <strong>£1,380</strong> [P1, A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>8</strong></td><td>Annual savings = 22% of £1,500 = £330 [P1, P1]. Payback period = Cost &divide; Saving = £1,800 &divide; 330 = <strong>5.45 years (or 5 years 5 months)</strong> [P1, A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>9</strong></td><td>Total allowable capacity = 15 &times; 250 kg = 3,750 kg [P1, P1]. Platform load = 3.2 tonnes = 3,200 kg [P1]. <strong>Yes, safely loaded</strong> as 3,200 kg &lt; 3,750 kg capacity (by 550 kg) [A1, B1].</td><td><strong>[5]</strong></td></tr>
         </table>"""),

        # Page 76: Paper 5 Mark Scheme (Part 3 - Section B Q10 to Q14)
        ("Official Mark Scheme &bull; Paper 5 (Section B Q10–Q14)",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Q</th><th>Mark Scheme &amp; Step-by-Step Method</th><th>Marks</th></tr>
           <tr><td><strong>10</strong></td><td>Real length = 14 cm &times; 50 = 700 cm = 7 metres [P1, P1]. Asphalt cost = 7 &times; £45 = <strong>£315</strong> [P1, A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>11</strong></td><td>Radius = 1.8 &divide; 2 = 0.9 m [P1]. Volume = 3.142 &times; 0.9&sup2; &times; 2 = 3.142 &times; 0.81 &times; 2 = 5.090 m&sup3; [P1, P1]. Litres = 5.090 &times; 1,000 = <strong>5,090 litres</strong> [A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>12</strong></td><td>COP = 8.4 kW &divide; 2.4 kW = <strong>3.5</strong>. [P1] for formula, [P1] for substitution, [A1] for 3.5, [B1] for noting it is dimensionless, [B1] for stating this means 3.5 units of heat per 1 unit electricity.</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>13</strong></td><td>Perimeter = 2(7.5 + 4.8) = 2(12.3) = 24.6 m [P1, P1]. Edging cost = 24.6 &times; £6.50 = <strong>£159.90</strong> [A1, B1].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>14</strong></td><td>After insulation: Mean is higher (19.8&deg;C vs 16.5&deg;C) indicating warmer wall surface [P1]. Range is much lower (1.1&deg;C vs 4.2&deg;C) indicating superior thermal uniformity and elimination of cold spots [P1, A1, B1].</td><td><strong>[4]</strong></td></tr>
         </table>"""),

        # Page 77: Paper 6 Mark Scheme (Part 1 - Section A)
        ("Official Mark Scheme &bull; Paper 6 (Section A)",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Q</th><th>Mark Scheme &amp; Step-by-Step Method</th><th>Marks</th></tr>
           <tr><td><strong>1</strong></td><td>57.6 &divide; 1.2 = 576 &divide; 12 = <strong>48</strong>. [P1] for clearing decimal by &times;10, [P1] for division algorithm, [A1] for 48, [B1] for inverse check (48 &times; 1.2 = 57.6).</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>2</strong></td><td>Total cloth diameter = 1.8 + (2 &times; 0.2) = 2.2 m &rarr; Radius = 1.1 m [P1, P1]. Area = 3.14 &times; 1.1&sup2; = 3.14 &times; 1.21 = <strong>3.7994 m&sup2; (or 3.80 m&sup2;)</strong> [A1, B1].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>3</strong></td><td>3 &frac12; &times; 2 &frac23; = 7/2 &times; 8/3 = 56/6 = 28/3 = <strong>9 &frac13; kg</strong> [P1, P1, A1, B1].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>4</strong></td><td>Gross = 120% = £158.40 [P1]. Net = 158.40 &divide; 1.20 = <strong>£132.00</strong> [P1, A1]. Check: 20% of 132 = £26.40; 132 + 26.40 = £158.40 [B1].</td><td><strong>[4]</strong></td></tr>
         </table>"""),

        # Page 78: Paper 6 Mark Scheme (Part 2 - Section B Q5 to Q9)
        ("Official Mark Scheme &bull; Paper 6 (Section B Q5–Q9)",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Q</th><th>Mark Scheme &amp; Step-by-Step Method</th><th>Marks</th></tr>
           <tr><td><strong>5</strong></td><td>Available room nights = 120 &times; 30 = 3,600 [P1]. Occupancy = (2,880 &divide; 3,600) &times; 100 = <strong>80%</strong> [P1]. ADR = 244,800 &divide; 2,880 = <strong>£85.00</strong> [P1]. RevPAR = 244,800 &divide; 3,600 = <strong>£68.00</strong> [A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>6</strong></td><td>Beef: 0.20 &times; £28 = £5.60 [P1]. Potatoes: 0.15 &times; £1.20 = £0.18 [P1]. Total ingredient cost = 5.60 + 0.18 + 0.85 = £6.63 [P1]. Food cost % = (6.63 &divide; 18.50) &times; 100 = <strong>35.8%</strong> [A1]. <strong>No, exceeds 32% target limit</strong> [B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>7</strong></td><td>Total temp drop = 18 - (-18) = 36&deg;C [P1]. Minutes needed = 36 &divide; 0.75 = 48 minutes [P1, P1]. Answer = <strong>48 minutes 0 seconds</strong> [A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>8</strong></td><td>Total parts = 5 + 3 = 8 [P1]. Prosecco glasses = (5/8) &times; 240 = 150 glasses [P1, P1]. Bottles needed = 150 &divide; 6 = <strong>25 bottles</strong> [A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>9</strong></td><td>Midpoints: 1.5, 3.5, 5.5, 7.5, 9.5 [P1]. fx: (1.5&times;3)=4.5; (3.5&times;9)=31.5; (5.5&times;18)=99; (7.5&times;22)=165; (9.5&times;8)=76 [P1]. &Sigma;fx = 376 [P1]. Mean = 376 &divide; 60 = <strong>6.3 stars</strong> [A1, B1].</td><td><strong>[5]</strong></td></tr>
         </table>"""),

        # Page 79: Paper 6 Mark Scheme (Part 3 - Section B Q10 to Q14)
        ("Official Mark Scheme &bull; Paper 6 (Section B Q10–Q14)",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Q</th><th>Mark Scheme &amp; Step-by-Step Method</th><th>Marks</th></tr>
           <tr><td><strong>10</strong></td><td>Gas cost = 35,000 &times; £0.072 = £2,520 [P1, P1]. Electric cost = 22,000 &times; £0.245 = £5,390 [P1]. Total utility bill = 2,520 + 5,390 = <strong>£7,910</strong> [A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>11</strong></td><td>GBP value = &euro;8,500 &divide; 1.16 = £7,327.59 [P1, P1]. 2% fee = 0.02 &times; 7,327.59 = £146.55 [P1]. Net credited = 7,327.59 - 146.55 = <strong>£7,181.04</strong> [A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>12</strong></td><td>P(arrives) = 1 - 0.12 = 0.88 [P1, P1]. P(both arrive) = 0.88 &times; 0.88 = <strong>0.7744 (or 77.4%)</strong> [P1, A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>13</strong></td><td>Time = 38 &divide; 40 = 0.95 hours [P1]. Minutes = 0.95 &times; 60 = 57 minutes [P1]. Arrival time = 05:45 + 57 mins = <strong>06:42</strong> [A1, B1].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>14</strong></td><td>Basic pay: 35 &times; £14.00 = £490.00 [P1]. Overtime hours = 44 - 35 = 9 hours [P1]. Overtime rate = £14 &times; 1.5 = £21.00/hr &rarr; 9 &times; 21 = £189.00 [P1]. Total gross pay = 490 + 189 = <strong>£679.00</strong> [A1].</td><td><strong>[4]</strong></td></tr>
         </table>"""),

        # Page 80: Paper 7 Mark Scheme (Part 1 - Section A & Section B Q5–Q8)
        ("Official Mark Scheme &bull; Paper 7 (Section A &amp; Section B Part 1)",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Q</th><th>Mark Scheme &amp; Step-by-Step Method</th><th>Marks</th></tr>
           <tr><td><strong>1</strong></td><td>142.045 - 89.378: Column subtraction across boundaries. <strong>52.667</strong> [P1, P1, A1, B1].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>2</strong></td><td>Area = &frac12;(16 + 24) &times; 12 = &frac12;(40) &times; 12 = <strong>240 cm&sup2;</strong> [P1, P1, A1, B1].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>3</strong></td><td>7/8 &divide; 3/16 = 7/8 &times; 16/3 = 14/3 = <strong>4 &frac23;</strong> [P1, P1, A1, B1].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>4</strong></td><td>85% = 68 secs &rarr; 68 &divide; 0.85 = <strong>80 seconds</strong> [P1, P1, A1]. Check: 15% of 80 = 12 &rarr; 80 - 12 = 68 [B1].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>5</strong></td><td>Each cut uses 145 + 3 = 148 mm [P1]. Total length = 3,200 mm [P1]. Pins = 3,200 &divide; 148 = 21.62 &rarr; <strong>21 full pins</strong> [P1, A1]. Offcut: 3,200 - (21 &times; 148) = 3,200 - 3,108 = 92 mm (+ final 3mm uncut = <strong>95 mm</strong>) [B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>6</strong></td><td>Cross-section Area = &pi;(2.5&sup2; - 1.5&sup2;) = 3.142 &times; (6.25 - 2.25) = 3.142 &times; 4 = 12.568 cm&sup2; [P1, P1]. Volume = 12.568 &times; 8 = 100.544 cm&sup3; [P1]. Mass = 100.544 &times; 8.5 = <strong>854.6 g</strong> [A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>7</strong></td><td>Tolerance limits: 24.92 mm to 25.08 mm [P1]. Fails: 25.09 mm (too large) and 24.91 mm (too small) [P1, P1]. Pass count = 3 out of 5 &rarr; <strong>60% pass rate</strong> [A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>8</strong></td><td>OEE = 0.92 &times; 0.88 &times; 0.95 = 0.7691 &rarr; <strong>76.9%</strong> [P1, P1, P1, A1]. <strong>Yes, exceeds 75% world-class benchmark</strong> [B1].</td><td><strong>[5]</strong></td></tr>
         </table>"""),

        # Page 81: Paper 7 Mark Scheme (Part 2 - Section B Q9–Q14)
        ("Official Mark Scheme &bull; Paper 7 (Section B Q9–Q14)",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Q</th><th>Mark Scheme &amp; Step-by-Step Method</th><th>Marks</th></tr>
           <tr><td><strong>9</strong></td><td>Midpoints: 2, 7, 12, 17 [P1]. fx: (2&times;18)=36; (7&times;20)=140; (12&times;9)=108; (17&times;3)=51 [P1]. &Sigma;fx = 335 [P1]. Mean = 335 &divide; 50 = <strong>6.7 defects per 1,000 components</strong> [A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>10</strong></td><td>Area = 32 &times; 18 = 576 m&sup2; [P1, P1]. Epoxy cost = 576 &times; £28.50 = <strong>£16,416</strong> [P1, A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>11</strong></td><td>Gross = 4,500 &times; £0.45 = £2,025 [P1]. Discount band (over 2,000) = 12% [P1]. Multiplier = 0.88 &rarr; £2,025 &times; 0.88 = <strong>£1,782.00</strong> [P1, A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>12</strong></td><td>P(both trigger) = 0.98 &times; 0.95 = <strong>0.931 (or 93.1%)</strong>. [P1] for rule of multiplication, [P1] for calculation, [A1] for 0.931, [B1] for percentage form.</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>13</strong></td><td>Time = Distance &divide; Speed = 36 &divide; 0.45 = <strong>80 seconds = 1 minute 20 seconds</strong> [P1, P1, A1, B1].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>14</strong></td><td>Year 1: 85,000 &times; 0.88 = £74,800 [P1]. Year 2: 74,800 &times; 0.90 = <strong>£67,320</strong> [P1, A1, B1].</td><td><strong>[4]</strong></td></tr>
         </table>"""),

        # Page 82: Paper 8 Mark Scheme (Part 1 - Section A & Section B Q5–Q8)
        ("Official Mark Scheme &bull; Paper 8 (Section A &amp; Section B Part 1)",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Q</th><th>Mark Scheme &amp; Step-by-Step Method</th><th>Marks</th></tr>
           <tr><td><strong>1</strong></td><td>375 &times; 48: 375 &times; 40 = 15,000; 375 &times; 8 = 3,000; Total = <strong>18,000</strong> [P1, P1, A1, B1].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>2</strong></td><td>Base: 45 &times; 30 = 1,350 m&sup2; [P1]. Long sides: 2 &times; (45 &times; 3) = 270 m&sup2; [P1]. Short sides: 2 &times; (30 &times; 3) = 180 m&sup2; [P1]. Total membrane = 1,350 + 270 + 180 = <strong>1,800 m&sup2;</strong> [A1].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>3</strong></td><td>Total parts = 4 + 2 + 1 = 7 parts [P1]. 1 part = 350 &divide; 7 = 50 kg [P1]. Nitrogen = 4 &times; 50 = <strong>200 kg</strong> [A1, B1].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>4</strong></td><td>88% = £39,600 [P1]. Original = 39,600 &divide; 0.88 = <strong>£45,000</strong> [P1, A1]. Check: 12% of 45,000 = 5,400 &rarr; 45,000 - 5,400 = £39,600 [B1].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>5</strong></td><td>Capacity Factor = (648 &divide; 1,800) &times; 100 = <strong>36%</strong>. [P1] for identifying theoretical max, [P1] for division, [A1] for 36%, [B1] for correct units.</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>6</strong></td><td>Radius = 3 m. Volume = 3.142 &times; 3&sup2; &times; 14 = 3.142 &times; 9 &times; 14 = 395.892 m&sup3; [P1, P1]. Capacity = 395.892 &times; 0.78 = <strong>308.8 tonnes</strong> [P1, A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>7</strong></td><td>North yield = 153 &divide; 18 = 8.5 tonnes/ha [P1, P1]. South yield = 198 &divide; 24 = 8.25 tonnes/ha [P1]. <strong>North field achieved higher yield by 0.25 tonnes/ha</strong> [A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>8</strong></td><td>Total land area = 5 &times; 10,000 = 50,000 m&sup2; [P1]. 1 panel area = 1.95 &times; 1.1 = 2.145 m&sup2; [P1]. All panels = 8,200 &times; 2.145 = 17,589 m&sup2; [P1]. Coverage % = (17,589 &divide; 50,000) &times; 100 = <strong>35.18% (or 35.2%)</strong> [A1, B1].</td><td><strong>[5]</strong></td></tr>
         </table>"""),

        # Page 83: Paper 8 Mark Scheme (Part 2 - Section B Q9–Q14)
        ("Official Mark Scheme &bull; Paper 8 (Section B Q9–Q14)",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Q</th><th>Mark Scheme &amp; Step-by-Step Method</th><th>Marks</th></tr>
           <tr><td><strong>9</strong></td><td>Moorland station experiences significantly higher average rainfall (112 mm vs 74 mm) [P1, P1]. Valley station has much greater seasonal consistency / stability (range 48 mm vs 94 mm) [P1, A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>10</strong></td><td>Pellets needed = 96,000 &divide; 4,800 = 20 tonnes &times; £280 = £5,600 [P1, P1]. Oil needed = 96,000 &divide; 10 = 9,600 litres &times; £0.72 = £6,912 [P1]. <strong>Biomass saving = £1,312.00</strong> (£6,912 - £5,600) [A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>11</strong></td><td>Annual revenue = 3 &times; 140 nights &times; £120 = £50,400 [P1]. Net profit = 50,400 - 7,500 = £42,900 [P1, P1]. Payback period = £42,000 &divide; 42,900 = <strong>0.98 years (&asymp; 11.8 months)</strong> [A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>12</strong></td><td>P(no frost on either night) = 0.85 &times; 0.85 = 0.7225 [P1, P1, P1]. P(frost on at least one night) = 1 - 0.7225 = <strong>0.2775 (or 27.8%)</strong> [A1, B1].</td><td><strong>[5]</strong></td></tr>
           <tr><td><strong>13</strong></td><td>Total litres = 65 &times; 14.5 = 942.5 litres [P1, P1]. Total fuel cost = 942.5 &times; £0.88 = <strong>£829.40</strong> [A1, B1].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>14</strong></td><td>Minutes to fill = 25,000 &divide; 85 = 294.12 minutes [P1, P1]. Convert to hours: 294.12 &divide; 60 = <strong>4 hours 54 minutes</strong> [A1, B1].</td><td><strong>[4]</strong></td></tr>
         </table>""")
    ]

    for p_num, (p_title, p_content) in enumerate(mark_schemes, 62):
        pages.append(f"""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Maths Level 2</div>
    <div class="page-header-strand">Official Examiner Mark Scheme</div>
  </div>

  <h2>{p_title}</h2>
  <p style="margin-bottom:6px;">Review mark allocations: Process [P], Method [M], and Accuracy [A].</p>

  {p_content}

  <div class="page-footer">
    <div>Maths Level 2 &bull; Official 8-Mock Exam Pack &bull; Mark Scheme</div>
    <div class="page-num">Page {p_num}</div>
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
<title>Maths Level 2 Official 8-Mock Exam Pack</title>
{SHARED_CSS}
<style>
  :root {{
    --theme: #002046;
    --accent: #38bdf8;
  }}
</style>
</head>
<body>
{''.join(pages)}
</body>
</html>"""

    pdf_filename = "MasterFunctionalSkills_Mock_Pack_Maths_L2.pdf"
    count = render_book_to_pdf(full_html, pdf_filename)
    return count

if __name__ == "__main__":
    build_mock_maths_l2_book()
