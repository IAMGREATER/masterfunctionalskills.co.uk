#!/usr/bin/env python3
import maths_domain1_number

all_d1 = list(maths_domain1_number.TOPICS_DOMAIN1)

more_d1 = [
    {
        "filename": "functional-skills-bidmas.html",
        "clean_topic": "BIDMAS / Order of Operations",
        "intro_lead": "Apply the standard mathematical hierarchy of operations (Brackets, Indices, Division, Multiplication, Addition, Subtraction) to solve multi-stage financial and clinical calculations.",
        "next_file": "functional-skills-rounding-and-estimating.html",
        "next_name": "Rounding & Estimating",
        "spec_points": [
            ("L1.5 / L2.5", "Follow the correct order of operations including brackets, powers, and roots in practical workplace calculations.")
        ],
        "golden_rules": [
            {
                "icon": "fa-arrow-down-1-9",
                "title": "Golden Rule 1: Multiplication and Division Have Equal Precedence",
                "desc": "Multiplication does NOT automatically come before Division. Work from left to right when both appear in an expression. The same applies to Addition and Subtraction.",
                "badge": "Brackets → Indices → (Division & Multiplication) → (Addition & Subtraction)"
            },
            {
                "icon": "fa-calculator",
                "title": "Golden Rule 2: Brackets Group Multi-Part Formulas",
                "desc": "Whenever calculating an average or total cost with discounts, calculate what is inside the brackets FIRST before multiplying or dividing.",
                "badge": "(£120 + £80) × 0.85 = £200 × 0.85 = £170"
            }
        ],
        "skills": [
            {
                "title": "The BIDMAS Hierarchy Breakdown",
                "summary": "Order of operations explained step-by-step.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>B – Brackets:</strong> Resolve everything inside (parentheses) first.</li>
                    <li><strong>I – Indices / Powers:</strong> Calculate squares (x²), cubes (x³), and square roots (√).</li>
                    <li><strong>D &amp; M – Division and Multiplication:</strong> Compute from left to right as they appear.</li>
                    <li><strong>A &amp; S – Addition and Subtraction:</strong> Compute from left to right as they appear.</li>
                  </ol>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Overtime Payroll & Deductions Calculation (Non-Calculator)",
                "marks": "3 Marks (Pearson Edexcel Level 2)",
                "context": "Payroll & Benefits Accounting",
                "question": "A healthcare assistant's gross pay formula is given as:<br><strong>Pay = 450 + 15 × (40 - 32) - 60</strong><br>Calculate the final pay value using the correct order of operations.",
                "steps": [
                    ("Step 1", "Resolve Brackets first: (40 - 32)", "40 - 32 = 8. Formula becomes: 450 + 15 × 8 - 60.", "M1: Correct bracket resolution"),
                    ("Step 2", "Perform Multiplication before addition/subtraction", "15 × 8 = 120. Formula becomes: 450 + 120 - 60.", "M1: Multiplication precedence"),
                    ("Step 3", "Perform Addition and Subtraction from left to right", "450 + 120 = 570<br>570 - 60 = 510", "A1: Accurate final answer")
                ],
                "final_answer": "Final Pay = £510.00",
                "tutor_tip": "If you added 450 + 15 first (= 465), you would obtain an erroneous answer of 3,660! Always follow BIDMAS."
            }
        ],
        "examiner_traps": [
            {
                "title": "Reading Left to Right Without Respecting Precedence",
                "desc": "Computing 5 + 3 × 4 as 8 × 4 = 32 is incorrect. The multiplication MUST happen first: 3 × 4 = 12, then 5 + 12 = 17.",
                "fix": "Highlight all multiplication and division signs before starting."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "Evaluate: <strong>24 ÷ (8 - 2) + 3² × 2</strong> without a calculator.",
                "solution_steps": "1. Brackets: (8 - 2) = 6.<br>2. Indices: 3² = 9.<br>3. Expression: 24 ÷ 6 + 9 × 2.<br>4. Division & Mult: 24 ÷ 6 = 4; 9 × 2 = 18.<br>5. Addition: 4 + 18 = 22.",
                "correct_answer": "22",
                "tutor_tip": "Resolve indices and brackets in your first working line."
            }
        ]
    },
    {
        "filename": "functional-skills-rounding-and-estimating.html",
        "clean_topic": "Rounding & Estimating",
        "intro_lead": "Round whole numbers and decimals to significant figures, decimal places, and nearest tens/hundreds, and use front-end estimation to verify workplace calculations.",
        "next_file": "functional-skills-fractions.html",
        "next_name": "Fractions",
        "spec_points": [
            ("L1.6 / L2.6", "Round numbers to a given power of 10, specified decimal places, or significant figures."),
            ("L1.7 / L2.7", "Estimate answers to multi-step calculations by rounding each value to 1 significant figure.")
        ],
        "golden_rules": [
            {
                "icon": "fa-hand-peace",
                "title": "Golden Rule 1: The '5 or More Round Up' Rule",
                "desc": "Look at the decider digit immediately to the right of your target place. If it is 5, 6, 7, 8, or 9, round UP. If 0, 1, 2, 3, or 4, keep the digit the same.",
                "badge": "0-4: Stay | 5-9: Round UP"
            },
            {
                "icon": "fa-bullseye",
                "title": "Golden Rule 2: 1 Significant Figure for Exam Estimations",
                "desc": "Whenever an exam question begins with 'Show an estimate for...', round EVERY number to 1 significant figure BEFORE performing any calculation.",
                "badge": "Estimate: 489 × 3.12 ≈ 500 × 3 = 1,500"
            }
        ],
        "skills": [
            {
                "title": "Decimal Places vs Significant Figures",
                "summary": "Clarifying the two major rounding conventions.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Value</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0284c7;">To 1 Decimal Place (1 dp)</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">To 1 Significant Figure (1 sf)</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#ea580c;">To 2 Significant Figures (2 sf)</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">47.86</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">47.9</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">50</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">48</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">0.0482</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">0.0</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">0.05</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">0.048</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Hospital Catering Supply Estimation (Non-Calculator)",
                "marks": "3 Marks (Pearson Edexcel Level 2)",
                "context": "Healthcare Food Services Procurement",
                "question": "The catering manager orders <strong>194 cartons</strong> of meal trays at <strong>£4.85</strong> each.<br>(a) Show an estimate of the total expenditure by rounding each value to 1 significant figure.<br>(b) State whether your estimate is an underestimate or overestimate, giving a reason.",
                "steps": [
                    ("Step 1", "Round each value to 1 significant figure", "194 rounds to 200 (1 sf)<br>£4.85 rounds to £5.00 (1 sf)", "M1: Rounding both values to 1 sf"),
                    ("Step 2", "Compute estimated total", "200 × £5 = £1,000", "A1: Correct estimated product (£1,000)"),
                    ("Step 3", "Analyze whether overestimate or underestimate", "Both numbers were rounded UP (194 → 200 and 4.85 → 5.00); therefore, £1,000 is an OVERESTIMATE.", "B1: Valid comparative justification")
                ],
                "final_answer": "(a) Estimate = £1,000 | (b) Overestimate, because both 194 and £4.85 were rounded up.",
                "tutor_tip": "If you calculate the exact answer (194 × 4.85 = £940.90) and then round that to £1,000, you score ZERO for step 1. You must round BEFORE multiplying."
            }
        ],
        "examiner_traps": [
            {
                "title": "Calculating Exact Value Before Rounding in Estimation Questions",
                "desc": "Exam boards require you to demonstrate that you can estimate WITHOUT doing complex multi-digit arithmetic.",
                "fix": "Always write down the rounded numbers first (e.g. 200 × 5) before calculating anything."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "Use 1 significant figure approximation to estimate the value of: <strong>(38.4 × 9.75) ÷ 0.48</strong>.",
                "solution_steps": "1. Round each to 1 sf: 38.4 ≈ 40; 9.75 ≈ 10; 0.48 ≈ 0.5.<br>2. Compute: (40 × 10) ÷ 0.5 = 400 ÷ 0.5 = 800.",
                "correct_answer": "800",
                "tutor_tip": "Dividing by 0.5 is equivalent to multiplying by 2 (400 ÷ 0.5 = 800)."
            }
        ]
    },
    {
        "filename": "functional-skills-fractions.html",
        "clean_topic": "Fractions: Operations & Fractions of Amounts",
        "intro_lead": "Add, subtract, multiply, and divide proper and mixed fractions, find fractions of workplace amounts, and convert improper fractions into mixed numbers.",
        "next_file": "functional-skills-decimals.html",
        "next_name": "Decimals",
        "spec_points": [
            ("L1.9 / L2.8", "Find fractions of whole number quantities or measurements."),
            ("L2.9", "Add, subtract, multiply, and divide proper and mixed fractions.")
        ],
        "golden_rules": [
            {
                "icon": "fa-divide",
                "title": "Golden Rule 1: Fraction of an Amount: Divide by Bottom, Multiply by Top",
                "desc": "To find 3/8 of £480: divide £480 by 8 (denominator = £60), then multiply by 3 (numerator = £180).",
                "badge": "Amount ÷ Denominator × Numerator"
            },
            {
                "icon": "fa-rotate",
                "title": "Golden Rule 2: Dividing Fractions: Keep, Change, Flip (KCF)",
                "desc": "Keep the first fraction, Change division (÷) to multiplication (×), and Flip the second fraction upside down (its reciprocal).",
                "badge": "Keep • Change • Flip (KCF)"
            }
        ],
        "skills": [
            {
                "title": "The Four Operations with Fractions",
                "summary": "Core rules for adding, subtracting, multiplying, and dividing fractions.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Addition / Subtraction:</strong> Find a common denominator first! <em>1/3 + 2/5 = 5/15 + 6/15 = 11/15.</em></li>
                    <li><strong>Multiplication:</strong> Multiply tops together, multiply bottoms together: <em>2/3 × 4/5 = 8/15.</em></li>
                    <li><strong>Division:</strong> Use Keep-Change-Flip: <em>3/4 ÷ 2/5 = 3/4 × 5/2 = 15/8 = 1 7/8.</em></li>
                    <li><strong>Mixed Numbers to Improper:</strong> Multiply whole by bottom, add top: <em>2 3/4 = (2×4 + 3)/4 = 11/4.</em></li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Care Home Staffing Shift Allocation",
                "marks": "3 Marks (Pearson Edexcel Level 2)",
                "context": "Residential Care Staff Scheduling",
                "question": "A residential care provider employs <strong>72 care workers</strong>. On night duty, <strong>3/8</strong> of the workforce are deployed. Of the remaining staff, <strong>2/3</strong> work the day shift, and the rest are on scheduled leave.<br>How many staff members are on scheduled leave?",
                "steps": [
                    ("Step 1", "Calculate staff on night duty (3/8 of 72)", "72 ÷ 8 = 9<br>9 × 3 = 27 staff on night shift", "M1: Fraction of amount calculation"),
                    ("Step 2", "Calculate remaining staff and day shift workers", "Remaining staff = 72 - 27 = 45 staff.<br>Day shift = 2/3 of 45: (45 ÷ 3) × 2 = 15 × 2 = 30 staff.", "M1: Subtraction and second fraction step"),
                    ("Step 3", "Calculate staff on scheduled leave", "45 - 30 = 15 staff on scheduled leave.", "A1: Accurate final staff count")
                ],
                "final_answer": "15 care workers on scheduled leave",
                "tutor_tip": "Always read carefully whether the second fraction applies to the 'original total' or the 'remaining staff'. Here it was of the remaining staff."
            }
        ],
        "examiner_traps": [
            {
                "title": "Adding Denominators Together",
                "desc": "Adding 1/4 + 1/4 = 2/8 is wrong! When denominators are identical, only add numerators: 1/4 + 1/4 = 2/4 = 1/2.",
                "fix": "Never add or subtract denominators; only add or subtract numerators over a common denominator."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "Calculate <strong>1 3/5 + 2 1/4</strong>, giving your answer as a mixed number in its simplest form.",
                "solution_steps": "1. Common denominator for 5 and 4 is 20: 3/5 = 12/20; 1/4 = 5/20.<br>2. Add whole numbers: 1 + 2 = 3.<br>3. Add fractions: 12/20 + 5/20 = 17/20.<br>4. Combine: 3 17/20.",
                "correct_answer": "3 17/20",
                "tutor_tip": "Keep whole numbers and fractions separate to avoid massive improper numerators."
            }
        ]
    },
    {
        "filename": "functional-skills-decimals.html",
        "clean_topic": "Decimals: Four Operations & Place Value",
        "intro_lead": "Perform addition, subtraction, multiplication, and division with decimals, round monetary figures to 2 decimal places, and solve real-world invoicing problems.",
        "next_file": "functional-skills-percentages.html",
        "next_name": "Percentages",
        "spec_points": [
            ("L1.10 / L2.10", "Read, write, order and compare decimals up to three decimal places."),
            ("L1.11 / L2.10", "Perform the four operations with decimals up to two decimal places in practical contexts.")
        ],
        "golden_rules": [
            {
                "icon": "fa-sterling-sign",
                "title": "Golden Rule 1: Always Write Money to 2 Decimal Places",
                "desc": "In Functional Skills, writing £14.5 or £14.500 loses the final accuracy mark. Currency in pounds must ALWAYS have exactly 2 decimal places (£14.50).",
                "badge": "Mandatory: £14.50 (NOT £14.5)"
            },
            {
                "icon": "fa-calculator",
                "title": "Golden Rule 2: Dividing by Decimals: Shift the Decimal Point",
                "desc": "Never divide by a decimal divisor. Multiply both numbers by 10, 100, or 1,000 to turn the divisor into a whole number before using the bus stop.",
                "badge": "£18 ÷ 0.25 = £1,800 ÷ 25 = 72"
            }
        ],
        "skills": [
            {
                "title": "Aligning Decimals for Column Operations",
                "summary": "Preventing positional errors during decimal addition and subtraction.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">To calculate <strong>£142.60 - £58.45</strong>:</p>
                  <table style="width:240px; border-collapse:collapse; font-family:monospace; font-size:1.15rem; text-align:right;">
                    <tr><td style="padding:4px;">142.60</td></tr>
                    <tr style="border-bottom:2px solid #0f172a;"><td style="padding:4px;">- 58.45</td></tr>
                    <tr style="font-weight:800; color:#0284c7;"><td style="padding:4px;">84.15</td></tr>
                  </table>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "NHS Pharmacy Prescription Fluid Dilution",
                "marks": "3 Marks (Pearson Edexcel Level 2)",
                "context": "Clinical Pharmacy Fluid Dispensing",
                "question": "A clinical pharmacist has <strong>4.5 litres</strong> of sterile saline solution. She dispenses the solution into dose ampoules containing <strong>0.15 litres</strong> each.<br>How many complete dose ampoules can she fill?",
                "steps": [
                    ("Step 1", "Set up the decimal division", "4.5 ÷ 0.15", "M1: Division setup"),
                    ("Step 2", "Multiply dividend and divisor by 100 to remove decimal in divisor", "4.5 × 100 = 450<br>0.15 × 100 = 15<br>Calculation becomes: 450 ÷ 15", "M1: Decimal shift method"),
                    ("Step 3", "Perform integer division", "450 ÷ 15 = 30 ampoules", "A1: Accurate whole number answer")
                ],
                "final_answer": "30 complete dose ampoules",
                "tutor_tip": "Notice how shifting the decimal point by two places turns an intimidating decimal problem into basic mental arithmetic (450 ÷ 15 = 30)."
            }
        ],
        "examiner_traps": [
            {
                "title": "Dropping the Zero at the End of Currency",
                "desc": "Writing £3.4 on an invoice instead of £3.40 will forfeit the mark on Pearson Edexcel marking keys.",
                "fix": "Always review money answers and ensure two digits follow the decimal point."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A parcel courier charges £6.50 for the first kilogram, plus £1.85 for each additional kilogram. Calculate the cost to deliver a 7 kg package.",
                "solution_steps": "1. Additional kilograms = 7 - 1 = 6 kg.<br>2. Additional cost = 6 × £1.85 = £11.10.<br>3. Total cost = £6.50 + £11.10 = £17.60.",
                "correct_answer": "£17.60",
                "tutor_tip": "Don't forget to subtract the first 1 kg before multiplying by £1.85."
            }
        ]
    },
    {
        "filename": "functional-skills-fractions-decimals-and-percentages.html",
        "clean_topic": "Fractions, Decimals & Percentages (FDP Conversions)",
        "intro_lead": "Convert seamlessly between fractions, decimals, and percentages, compare values in different formats, and solve equivalence problems under exam conditions.",
        "next_file": "functional-skills-ratio.html",
        "next_name": "Ratio & Proportion",
        "spec_points": [
            ("L1.12 / L2.11", "Recognise and use equivalences between common fractions, decimals, and percentages."),
            ("L2.12", "Order and compare fractions, decimals, and percentages across mixed representations.")
        ],
        "golden_rules": [
            {
                "icon": "fa-arrows-rotate",
                "title": "Golden Rule 1: The FDP Conversion Triangle",
                "desc": "Percentage to Decimal: Divide by 100. Decimal to Percentage: Multiply by 100. Fraction to Decimal: Top divided by Bottom.",
                "badge": "Fraction → (Top ÷ Bottom) → Decimal → (× 100) → Percentage"
            },
            {
                "icon": "fa-list-ol",
                "title": "Golden Rule 2: Convert All to Decimals or Percentages Before Ordering",
                "desc": "When asked to compare mixed values (e.g. 3/8, 0.35, 36%), convert EVERY value into a percentage or decimal with 2 decimal places before comparing.",
                "badge": "3/8 = 37.5% | 0.35 = 35% | 36% = 36% → 0.35 < 36% < 3/8"
            }
        ],
        "skills": [
            {
                "title": "Benchmark FDP Equivalences to Memorize",
                "summary": "The high-frequency conversions that appear in every Functional Skills paper.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:center;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Fraction</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Decimal</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Percentage</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">1/2</td><td style="padding:6px; border:1px solid #cbd5e1;">0.5</td><td style="padding:6px; border:1px solid #cbd5e1;">50%</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">1/4</td><td style="padding:6px; border:1px solid #cbd5e1;">0.25</td><td style="padding:6px; border:1px solid #cbd5e1;">25%</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">3/4</td><td style="padding:6px; border:1px solid #cbd5e1;">0.75</td><td style="padding:6px; border:1px solid #cbd5e1;">75%</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">1/5</td><td style="padding:6px; border:1px solid #cbd5e1;">0.2</td><td style="padding:6px; border:1px solid #cbd5e1;">20%</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">1/8</td><td style="padding:6px; border:1px solid #cbd5e1;">0.125</td><td style="padding:6px; border:1px solid #cbd5e1;">12.5%</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">1/10</td><td style="padding:6px; border:1px solid #cbd5e1;">0.1</td><td style="padding:6px; border:1px solid #cbd5e1;">10%</td></tr>
                    </tbody>
                  </table>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Hospital Ward Hand Hygiene Audit Comparison",
                "marks": "3 Marks (Pearson Edexcel Level 2)",
                "context": "Infection Prevention Compliance",
                "question": "Three hospital wards reported their staff hand hygiene compliance rates:<br>Ward A: <strong>4/5</strong><br>Ward B: <strong>78%</strong><br>Ward C: <strong>0.82</strong><br>(a) Convert all three scores to percentages.<br>(b) Which ward achieved the highest compliance score?",
                "steps": [
                    ("Step 1", "Convert Ward A (4/5) to percentage", "4/5 = 8/10 = 80/100 = 80% (or 4 ÷ 5 × 100 = 80%)", "M1: Fraction to percentage conversion"),
                    ("Step 2", "Convert Ward C (0.82) to percentage", "0.82 × 100 = 82%", "M1: Decimal to percentage conversion"),
                    ("Step 3", "Compare all three percentage scores", "Ward A = 80%, Ward B = 78%, Ward C = 82%. 82% > 80% > 78%. Ward C achieved the highest compliance.", "A1: Correct comparison and conclusion")
                ],
                "final_answer": "(a) Ward A: 80%, Ward B: 78%, Ward C: 82% | (b) Ward C achieved the highest compliance.",
                "tutor_tip": "Converting to percentages makes comparison immediate and avoids fractional common denominator complications."
            }
        ],
        "examiner_traps": [
            {
                "title": "Confusing 0.05 with 50%",
                "desc": "0.05 = 5%, whereas 0.5 = 50%. A common error is assuming 0.05 is 50% because of the digit 5.",
                "fix": "Always multiply the decimal by 100: 0.05 × 100 = 5%."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "Arrange in ascending order: <strong>0.62, 3/5, 65%, 5/8</strong>.",
                "solution_steps": "1. Convert all to decimals: 0.62; 3/5 = 0.60; 65% = 0.65; 5/8 = 0.625.<br>2. Sequence: 0.60 (3/5), 0.62, 0.625 (5/8), 0.65 (65%).",
                "correct_answer": "3/5, 0.62, 5/8, 65%",
                "tutor_tip": "Write the final answer using the original numbers given in the question."
            }
        ]
    }
]

all_d1.extend(more_d1)

with open("/home/subi/Projects/masterfunctionalskills.co.uk/maths_domain1_number.py", "w", encoding="utf-8") as f:
    f.write("#!/usr/bin/env python3\n")
    f.write('"""Maths Domain 1: Number & Number Systems (10 Core Topics)"""\n\n')
    f.write("TOPICS_DOMAIN1 = " + repr(all_d1) + "\n")

print(f"Domain 1 complete with {len(all_d1)} topics!")
