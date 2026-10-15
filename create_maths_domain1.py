#!/usr/bin/env python3
import json

TOPICS_DOMAIN1 = [
    {
        "filename": "functional-skills-numbers-and-place-value.html",
        "clean_topic": "Numbers & Place Value",
        "intro_lead": "Master place value columns from millions down to thousandths, understand the role of zero as a placeholder, and read/write large numbers accurately in healthcare and commercial reports.",
        "next_file": "functional-skills-ordering-numbers.html",
        "next_name": "Ordering Numbers",
        "spec_points": [
            ("L1.1 / L2.1", "Read, write, order and compare large positive whole numbers up to 1,000,000 and beyond."),
            ("L2.2", "Recognise and use numbers given in figures and in words in workplace documents.")
        ],
        "golden_rules": [
            {
                "icon": "fa-table-columns",
                "title": "Golden Rule 1: The Zero Placeholder Protects Positional Value",
                "desc": "A digit's value is determined entirely by its column. If a column has no value, you MUST write a zero as a placeholder (e.g. two million and five thousand is 2,005,000, NOT 2,5000).",
                "badge": "Millions | H-Th | T-Th | Th | Hundreds | Tens | Units"
            },
            {
                "icon": "fa-layer-group",
                "title": "Golden Rule 2: Group Digits in Threes from the Decimal Point",
                "desc": "When reading or writing large numbers, work in blocks of three digits separated by commas or thin spaces (e.g. 14,250,800).",
                "badge": "14,250,800 = 14 million, 250 thousand, 800"
            }
        ],
        "skills": [
            {
                "title": "Place Value Hierarchy & Digit Values",
                "summary": "The definitive place value chart for Functional Skills Mathematics.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:center;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:10px; border:1px solid #cbd5e1;">Millions (M)</th>
                        <th style="padding:10px; border:1px solid #cbd5e1;">Hundred Thousands (HT)</th>
                        <th style="padding:10px; border:1px solid #cbd5e1;">Ten Thousands (TT)</th>
                        <th style="padding:10px; border:1px solid #cbd5e1;">Thousands (Th)</th>
                        <th style="padding:10px; border:1px solid #cbd5e1;">Hundreds (H)</th>
                        <th style="padding:10px; border:1px solid #cbd5e1;">Tens (T)</th>
                        <th style="padding:10px; border:1px solid #cbd5e1;">Units (U)</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr style="font-weight:700; font-size:1.15rem; color:#0f172a;">
                        <td style="padding:10px; border:1px solid #cbd5e1;">3</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">0</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">4</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">8</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">5</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">2</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">0</td>
                      </tr>
                      <tr style="font-size:0.85rem; color:#64748b;">
                        <td style="padding:8px; border:1px solid #cbd5e1;">3,000,000</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">0</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">40,000</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">8,000</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">500</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">20</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">0</td>
                      </tr>
                    </tbody>
                  </table>
                  <p style="margin-top:12px; font-weight:600; color:#334155;">Spoken in words: <em>Three million, forty-eight thousand, five hundred and twenty.</em></p>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "NHS Trust Equipment Procurement Audit",
                "marks": "3 Marks (Pearson Edexcel Level 2)",
                "context": "Healthcare Capital Expenditure",
                "question": "A hospital procurement circular states the capital investment in surgical robots is <strong>£4,082,500</strong>.<br>(a) Write this amount in words.<br>(b) State the value of the digit 8 in this number.",
                "steps": [
                    ("Step 1", "Break the number into three-digit periods", "4 millions, 082 thousands, 500 units.", "M1: Place value identification"),
                    ("Step 2", "Write in formal words", "Four million, eighty-two thousand, five hundred pounds.", "A1: Accurate word translation"),
                    ("Step 3", "Determine the specific value of digit 8", "The digit 8 is in the ten-thousands column: 8 × 10,000 = 80,000 (eighty thousand).", "A1: Correct digit value")
                ],
                "final_answer": "(a) Four million, eighty-two thousand, five hundred pounds | (b) Eighty thousand (£80,000).",
                "tutor_tip": "Notice the hundred-thousands column has a 0. Do NOT say 'four million, eight hundred thousand'; it is eighty-two thousand."
            }
        ],
        "examiner_traps": [
            {
                "title": "Omitting Placeholder Zeros",
                "desc": "Writing 'four million and twelve' as 4,12 or 4012 instead of 4,000,012 loses the accuracy mark entirely.",
                "fix": "Always sketch 7 column dashes (_ _ _ _ _ _ _) and populate from the units column."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A logistics firm handled <strong>1,050,402</strong> parcels in November.<br>(a) Write this number in words.<br>(b) State the value of the digit 5.",
                "solution_steps": "1. In words: One million, fifty thousand, four hundred and two.<br>2. Digit 5 is in the ten-thousands column: 50,000 (fifty thousand).",
                "correct_answer": "(a) One million, fifty thousand, four hundred and two | (b) 50,000",
                "tutor_tip": "Check that you do not omit the placeholder zero in the thousands column."
            }
        ]
    },
    {
        "filename": "functional-skills-ordering-numbers.html",
        "clean_topic": "Ordering Numbers: Whole, Negative & Decimals",
        "intro_lead": "Compare and sequence positive and negative numbers, temperatures, and decimal measurements in ascending and descending order.",
        "next_file": "functional-skills-addition-and-subtraction.html",
        "next_name": "Addition & Subtraction",
        "spec_points": [
            ("L1.2 / L2.1", "Order and compare integers, decimals, and negative numbers."),
            ("L1.4", "Use inequality symbols (<, >, =) to express relationships between values.")
        ],
        "golden_rules": [
            {
                "icon": "fa-temperature-low",
                "title": "Golden Rule 1: Negative Numbers Work in Reverse",
                "desc": "The further to the left on a number line, the smaller the number. Therefore, -18°C is smaller (colder) than -4°C.",
                "badge": "-20 < -15 < -5 < 0 < 5"
            },
            {
                "icon": "fa-align-left",
                "title": "Golden Rule 2: Line Up Decimal Points and Pad with Trailing Zeros",
                "desc": "To compare decimals such as 0.4, 0.375, and 0.09, pad them to equal lengths: 0.400, 0.375, 0.090 before ordering.",
                "badge": "0.090 < 0.375 < 0.400"
            }
        ],
        "skills": [
            {
                "title": "Number Line Sequencing for Negative and Decimal Values",
                "summary": "How to align values accurately from lowest to highest.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">When ordering mixed values, follow this 3-step checklist:</p>
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Separate Negatives and Positives:</strong> All negative values are strictly smaller than zero and any positive value.</li>
                    <li><strong>Order Negatives:</strong> The negative number with the largest absolute digit is the smallest (e.g. -12 is smaller than -3).</li>
                    <li><strong>Pad Decimals:</strong> Add trailing zeros so all numbers have the same number of decimal places before comparing.</li>
                  </ol>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Hospital Pharmacy Cold Storage Temperature Monitoring",
                "marks": "3 Marks (Pearson Edexcel Level 1/2)",
                "context": "Vaccine Storage Compliance",
                "question": "A pharmacy technician records five temperature readings in vaccine freezer units: <strong>-4.2°C, 3.1°C, -6.8°C, -1.5°C, 0.8°C</strong>.<br>Arrange these temperatures in ascending order (coldest to warmest).",
                "steps": [
                    ("Step 1", "Identify negative temperatures", "Negative numbers: -4.2°C, -6.8°C, -1.5°C.", "M1: Isolating negative values"),
                    ("Step 2", "Order negative values from coldest (furthest from zero)", "-6.8°C is coldest, followed by -4.2°C, then -1.5°C.", "M1: Accurate negative ordering"),
                    ("Step 3", "Order remaining positive values and combine", "0.8°C then 3.1°C. Complete sequence: -6.8°C, -4.2°C, -1.5°C, 0.8°C, 3.1°C.", "A1: Correct ascending order")
                ],
                "final_answer": "-6.8°C, -4.2°C, -1.5°C, 0.8°C, 3.1°C",
                "tutor_tip": "'Ascending' always means smallest to largest. 'Descending' means largest to smallest."
            }
        ],
        "examiner_traps": [
            {
                "title": "Assuming Longer Decimals Are Bigger",
                "desc": "Learners often think 0.125 is bigger than 0.3 because 125 is bigger than 3. In reality, 0.3 = 0.300, which is larger than 0.125.",
                "fix": "Always pad with zeros: compare 0.300 with 0.125."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "Arrange these warehouse crate weights in descending order: <strong>4.05 kg, 4.5 kg, 4.125 kg, 4.55 kg, 4.009 kg</strong>.",
                "solution_steps": "1. Pad to 3 decimal places: 4.050, 4.500, 4.125, 4.550, 4.009.<br>2. Arrange largest to smallest: 4.55 kg, 4.5 kg, 4.125 kg, 4.05 kg, 4.009 kg.",
                "correct_answer": "4.55 kg, 4.5 kg, 4.125 kg, 4.05 kg, 4.009 kg",
                "tutor_tip": "'Descending' means largest to smallest. Check the question wording carefully."
            }
        ]
    },
    {
        "filename": "functional-skills-addition-and-subtraction.html",
        "clean_topic": "Addition & Subtraction",
        "intro_lead": "Perform multi-digit column addition and subtraction with borrowing/carrying, calculate balance reconciliations, and verify solutions using reverse operations in non-calculator contexts.",
        "next_file": "functional-skills-multiplication.html",
        "next_name": "Multiplication",
        "spec_points": [
            ("L1.3 / L2.3", "Add and subtract whole numbers and decimals up to 2 decimal places in practical contexts."),
            ("L1.7", "Check calculations using reverse operations and estimation.")
        ],
        "golden_rules": [
            {
                "icon": "fa-arrows-down-to-line",
                "title": "Golden Rule 1: Vertical Column Alignment",
                "desc": "Always align units over units, tens over tens, and decimal points over decimal points. Misaligned columns cause 80% of manual arithmetic errors.",
                "badge": "Line up decimal points before adding or subtracting"
            },
            {
                "icon": "fa-rotate-left",
                "title": "Golden Rule 2: Mandatory Reverse Operation Check",
                "desc": "In Pearson Edexcel Non-Calculator exams, 1 mark is often explicitly awarded for showing a reverse operation check (e.g. if A - B = C, prove that C + B = A).",
                "badge": "Check: Result + Subtrahend = Starting Number"
            }
        ],
        "skills": [
            {
                "title": "Column Subtraction with Decomposition (Borrowing)",
                "summary": "Step-by-step subtraction across zeros.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">When subtracting across zeros (e.g. 5,000 - 1,468):</p>
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li>Borrow from the thousands column (turn 5 into 4, making the hundreds column 10).</li>
                    <li>Borrow from hundreds (turn 10 into 9, making tens column 10).</li>
                    <li>Borrow from tens (turn 10 into 9, making units column 10).</li>
                    <li>Subtract each column: 10 - 8 = 2; 9 - 6 = 3; 9 - 4 = 5; 4 - 1 = 3. Result: 3,532.</li>
                  </ol>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "NHS Ward Budget Reconciliation (Non-Calculator)",
                "marks": "3 Marks (Pearson Edexcel Level 1/2)",
                "context": "Ward Petty Cash Management",
                "question": "A ward sister starts the week with a petty cash float of <strong>£850.00</strong>. During the week, she makes three purchases: stationery for £46.75, emergency medical supplies for £189.40, and taxi vouchers for £62.85.<br>(a) Calculate the remaining cash balance.<br>(b) Show a reverse calculation to check your answer.",
                "steps": [
                    ("Step 1", "Add the three expenditure amounts", "£46.75 + £189.40 + £62.85 = £299.00", "M1: Total expenditure addition"),
                    ("Step 2", "Subtract total expenditure from starting float", "£850.00 - £299.00 = £551.00", "A1: Accurate remaining balance"),
                    ("Step 3", "Perform reverse operation check", "£551.00 + £299.00 = £850.00 (matches starting float)", "B1: Valid reverse operation check")
                ],
                "final_answer": "(a) Remaining balance = £551.00 | (b) Check: £551.00 + £299.00 = £850.00",
                "tutor_tip": "Always write down the full check sentence. Stating 'I checked on my calculator' gets zero marks."
            }
        ],
        "examiner_traps": [
            {
                "title": "Subtracting Smaller from Larger in Columns",
                "desc": "When computing 0 - 6, students often mistakenly write 6 instead of borrowing 1 from the next column.",
                "fix": "Remember: If top digit is smaller than bottom digit, you MUST borrow from the left."
            }
        ],
        "practice_questions": [
            {
                "marks": "3 Marks",
                "question": "A delivery driver had 1,200 litres of diesel in the depot tank. Over 3 days, drivers drew 345 L, 280 L, and 415 L.<br>(a) How many litres remain in the tank?<br>(b) Show a check of your working.",
                "solution_steps": "1. Total used = 345 + 280 + 415 = 1,040 litres.<br>2. Remaining = 1,200 - 1,040 = 160 litres.<br>3. Check: 160 + 1,040 = 1,200 litres.",
                "correct_answer": "(a) 160 litres | (b) Check: 160 + 1,040 = 1,200 L",
                "tutor_tip": "Include units (litres) in your final statement."
            }
        ]
    },
    {
        "filename": "functional-skills-multiplication.html",
        "clean_topic": "Multiplication & Scaling",
        "intro_lead": "Master long multiplication (grid method and standard column method), multiply decimals, scale quantities, and solve multi-tier pricing problems under non-calculator conditions.",
        "next_file": "functional-skills-division.html",
        "next_name": "Division",
        "spec_points": [
            ("L1.3 / L2.3", "Multiply whole numbers and decimals up to 2 decimal places by whole numbers and decimals."),
            ("L1.7", "Estimate and check answers using rounding.")
        ],
        "golden_rules": [
            {
                "icon": "fa-hashtag",
                "title": "Golden Rule 1: The Total Decimal Places Rule",
                "desc": "When multiplying decimals, count the total number of decimal places in BOTH numbers. The final answer must have that exact total number of decimal places.",
                "badge": "2.4 (1 dp) × 0.15 (2 dp) = 0.360 (3 dp) = 0.36"
            },
            {
                "icon": "fa-table-cells",
                "title": "Golden Rule 2: Grid Method Eliminates Carrying Errors",
                "desc": "If column multiplication confuses you with carried digits, use the grid (box) method to partition numbers by tens and units before summing.",
                "badge": "Partition: (30 + 4) × (20 + 7) = 600 + 210 + 80 + 28 = 918"
            }
        ],
        "skills": [
            {
                "title": "Grid Method vs Column Method for Multi-Digit Numbers",
                "summary": "Two proven pathways to error-free non-calculator multiplication.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:center;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">×</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">40</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">6</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Row Sum</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">30</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">1,200</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">180</td>
                        <td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">1,380</td>
                      </tr>
                      <tr>
                        <td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">5</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">200</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">30</td>
                        <td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">230</td>
                      </tr>
                      <tr style="background:#e0f2fe; font-weight:800; color:#0369a1;">
                        <td colspan="3" style="padding:10px; border:1px solid #cbd5e1; text-align:right;">Grand Total (46 × 35):</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">1,610</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Hospital Uniform Procurement Order (Non-Calculator)",
                "marks": "3 Marks (Pearson Edexcel Level 2)",
                "context": "NHS Healthcare Staff Uniforms",
                "question": "A care home orders <strong>48 tunic sets</strong> at a cost of <strong>£26.50</strong> each.<br>Calculate the total cost of the order without using a calculator.",
                "steps": [
                    ("Step 1", "Convert decimal to whole number calculation", "Multiply 2650 by 48 (removing 2 decimal places temporarily).", "M1: Method setup"),
                    ("Step 2", "Compute 2650 × 48", "2650 × 40 = 106,000<br>2650 × 8 = 21,200<br>106,000 + 21,200 = 127,200", "M1: Correct multiplication"),
                    ("Step 3", "Restore the two decimal places for currency", "127,200 ÷ 100 = £1,272.00", "A1: Accurate final currency answer")
                ],
                "final_answer": "Total Cost = £1,272.00",
                "tutor_tip": "Remember to write the pound sign and two decimal zeros (£1,272.00) when quoting money in Functional Skills."
            }
        ],
        "examiner_traps": [
            {
                "title": "Forgetting the Zero in the Tens Row",
                "desc": "In long column multiplication, when multiplying by the tens digit, you MUST put a 0 in the units column before multiplying.",
                "fix": "Always drop a '0' as your placeholder before multiplying by the tens digit."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A logistics operative works 37.5 hours per week at an hourly rate of £14.00. Calculate their gross weekly pay without a calculator.",
                "solution_steps": "1. 37.5 × 14 = (37.5 × 10) + (37.5 × 4)<br>2. 375 + 150 = £525.00.",
                "correct_answer": "£525.00",
                "tutor_tip": "Multiplying by 14 can be simplified into multiplying by 10 then by 4 and summing."
            }
        ]
    },
    {
        "filename": "functional-skills-division.html",
        "clean_topic": "Division & Remainders",
        "intro_lead": "Perform short and long bus-stop division, interpret remainders in practical vocational contexts (rounding up vs rounding down), and convert fractional remainders to decimals.",
        "next_file": "functional-skills-bidmas.html",
        "next_name": "BIDMAS / Order of Operations",
        "spec_points": [
            ("L1.3 / L2.3", "Divide whole numbers and decimals by whole numbers up to 2-digit divisors."),
            ("L1.8 / L2.4", "Interpret remainders appropriately depending on context (e.g. packaging crates, transport minibuses).")
        ],
        "golden_rules": [
            {
                "icon": "fa-van-shuttle",
                "title": "Golden Rule 1: Practical Context Dictates How You Treat Remainders",
                "desc": "If booking minibuses or buying paint tins, you MUST round UP to ensure everyone fits or enough paint is bought. If packing full boxes, round DOWN (ignore remaining loose items).",
                "badge": "People / Tins → Round UP | Complete Boxes / Portions → Round DOWN"
            },
            {
                "icon": "fa-circle-dot",
                "title": "Golden Rule 2: Turn Remainders into Decimals with .00",
                "desc": "To convert a remainder into an exact decimal, place a decimal point and add trailing zeros (.00) to the dividend under the bus stop.",
                "badge": "145 ÷ 4 = 145.00 ÷ 4 = 36.25"
            }
        ],
        "skills": [
            {
                "title": "The Short Division Bus-Stop Method",
                "summary": "Dividing step-by-step with carrying and decimals.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">To calculate <strong>£518 ÷ 4</strong>:</p>
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li>4 into 5 goes 1 time, remainder 1 (carry 1 to make 11).</li>
                    <li>4 into 11 goes 2 times, remainder 3 (carry 3 to make 38).</li>
                    <li>4 into 38 goes 9 times, remainder 2. Add decimal point: .0.</li>
                    <li>4 into 20 goes 5 times exactly. Result: £129.50.</li>
                  </ol>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Patient Transport Booking Logistics",
                "marks": "3 Marks (Pearson Edexcel Level 1/2)",
                "context": "Hospital Patient Shuttle Service",
                "question": "An NHS outpatient center needs to transport <strong>142 patients</strong> to an off-site clinic. Each patient shuttle minibus carries a maximum of <strong>16 passengers</strong>.<br>(a) How many minibuses must be booked?<br>(b) How many empty seats will be on the final minibus?",
                "steps": [
                    ("Step 1", "Divide total patients by bus capacity", "142 ÷ 16 = 8 remainder 14 (or 8.875)", "M1: Division setup"),
                    ("Step 2", "Interpret remainder in practical transport context", "8 buses carry 128 passengers, leaving 14 patients stranded. Therefore, 9 minibuses must be booked.", "A1: Correctly rounding UP to 9 buses"),
                    ("Step 3", "Calculate empty seats on final minibus", "Total capacity: 9 × 16 = 144 seats.<br>Empty seats: 144 - 142 = 2 empty seats (or 16 - 14 = 2).", "B1: Correct empty seat calculation")
                ],
                "final_answer": "(a) 9 minibuses must be booked | (b) 2 empty seats on the final minibus.",
                "tutor_tip": "In passenger transport problems, you can NEVER leave patients behind. You must always round up to the next whole vehicle."
            }
        ],
        "examiner_traps": [
            {
                "title": "Writing Decimal Remainders for Indivisible Units",
                "desc": "Answering '8.875 minibuses' earns zero marks for the final answer because you cannot book 0.875 of a vehicle.",
                "fix": "Always round to a whole integer when dealing with people, vehicles, or physical packaging."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A factory produces 490 bottles of hand sanitizer. The bottles are packed into shipping boxes of 12 bottles each. How many complete boxes can be shipped, and how many bottles are left over?",
                "solution_steps": "1. 490 ÷ 12 = 40 remainder 10.<br>2. Complete boxes = 40; Leftover bottles = 10.",
                "correct_answer": "40 complete boxes (10 bottles leftover)",
                "tutor_tip": "Notice the question asks for 'complete boxes', so here you round DOWN to 40."
            }
        ]
    }
]

# Write out domain 1
with open("/home/subi/Projects/masterfunctionalskills.co.uk/maths_domain1_number.py", "w", encoding="utf-8") as f:
    f.write("#!/usr/bin/env python3\n")
    f.write('"""Maths Domain 1: Number & Number Systems (Part 1)"""\n\n')
    f.write("TOPICS_DOMAIN1 = " + repr(TOPICS_DOMAIN1) + "\n")

print(f"Domain 1 Part 1 written with {len(TOPICS_DOMAIN1)} topics!")
