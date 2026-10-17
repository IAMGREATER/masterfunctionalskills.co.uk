#!/usr/bin/env python3
"""
Curriculum Topic Definitions: Maths - Number and The Number System.
Each topic includes:
- Formula / Golden Rule reminder
- Section A: Core Skills (Warm-Up) (2 questions)
- Section B: Workplace Functional Application (2 questions)
- Section C: Multi-Step Exam Problem Solving & Decision (2 questions)
- Complete examiner step-by-step mark breakdown, traps, and checks.
"""

TOPICS_MATHS_NUMBER = [
    {
        "slug": "numbers-and-place-value",
        "title": "Numbers & Place Value",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.1 • L1.2 • L2.1",
        "total_marks": 18,
        "formula_hint": "Place value determines the value of each digit based on its position (Millions, Hundred Thousands, Ten Thousands, Thousands, Hundreds, Tens, Units, tenths, hundredths, thousandths). Use commas or spaces to group digits into sets of three from the decimal point.",
        "back_url": "../functional-skills-numbers-and-place-value.html",
        "sections": [
            {
                "title": "Section A: Core Skills (Warm-Up)",
                "meta": "Questions 1 & 2 • 4 Marks",
                "questions": [
                    {
                        "title": "Question 1 (Level 1 Standard)",
                        "marks": 2,
                        "stem": "Write the number <strong>two million, forty-five thousand, six hundred and eight</strong> in figures.",
                        "lines": 2,
                        "ans_label": "Number in figures =",
                        "choice_box": "____________________",
                        "step_rows": [
                            ("1. Identify millions place (2,000,000) and thousands place (045,000)", "[M1]"),
                            ("2. Complete number with hundreds, tens, units: 2,045,608", "[A1]")
                        ],
                        "final_answer": "2,045,608",
                        "pitfall": "Candidates often omit the placeholder zero in the hundred-thousands column, erroneously writing 2,45,608 or 245,608.",
                        "reverse_check": "Break down by column: 2,000,000 + 40,000 + 5,000 + 600 + 8 = 2,045,608. Confirmed."
                    },
                    {
                        "title": "Question 2 (Level 1 Standard)",
                        "marks": 2,
                        "stem": "In the number <strong>4,839,271</strong>, state the value of the digit <strong>3</strong> both in words and as a number.",
                        "lines": 3,
                        "ans_label": "Value of digit 3 =",
                        "choice_box": "____________________",
                        "step_rows": [
                            ("1. Identify position as ten-thousands column", "[M1]"),
                            ("2. State value as 30,000 (thirty thousand)", "[A1]")
                        ],
                        "final_answer": "30,000 (Thirty Thousand)",
                        "pitfall": "Writing just 'ten thousands' (identifying the place instead of the value) or writing '3' loses the accuracy mark.",
                        "reverse_check": "3 × 10,000 = 30,000."
                    }
                ]
            },
            {
                "title": "Section B: Everyday & Workplace Maths",
                "meta": "Questions 3 & 4 • 6 Marks",
                "questions": [
                    {
                        "title": "Question 3 (Level 1 Workplace Stock Audit)",
                        "marks": 3,
                        "stem": "An NHS central distribution warehouse holds the following quantities of medical masks across four regional depots:<br>• Depot A: 340,500<br>• Depot B: 304,850<br>• Depot C: 345,000<br>• Depot D: 340,095<br><br>Write these depot stock figures in order of size, starting with the <strong>smallest</strong> stock quantity.",
                        "lines": 4,
                        "ans_label": "Ordered figures =",
                        "choice_box": "Smallest: ________________ to Largest: ________________",
                        "step_rows": [
                            ("1. Compare hundred-thousands and ten-thousands digits to identify lowest: Depot B (304,850)", "[P1]"),
                            ("2. Compare remaining three depots with 340k+: Depot D (340,095), Depot A (340,500), Depot C (345,000)", "[P1]"),
                            ("3. Correct full ascending list: 304,850; 340,095; 340,500; 345,000", "[A1]")
                        ],
                        "final_answer": "304,850  <  340,095  <  340,500  <  345,000",
                        "pitfall": "Misreading 340,095 as larger than 340,500 by overlooking the tens versus hundreds placeholder zero.",
                        "reverse_check": "Check reverse descending: 345,000 > 340,500 > 340,095 > 304,850."
                    },
                    {
                        "title": "Question 4 (Level 2 Decimals & Micro-Measurements)",
                        "marks": 3,
                        "stem": "A biomedical laboratory analyses blood serum sample concentrations in mg/dL: <strong>0.048, 0.408, 0.0408, 0.48, 0.084</strong>.<br>Arrange these concentrations in order of magnitude from <strong>largest</strong> to <strong>smallest</strong>.",
                        "lines": 4,
                        "ans_label": "Ordered concentrations =",
                        "choice_box": "Largest: ________________ to Smallest: ________________",
                        "step_rows": [
                            ("1. Pad numbers to 4 decimal places for alignment: 0.0480, 0.4080, 0.0408, 0.4800, 0.0840", "[M1]"),
                            ("2. Compare tenths and hundredths to find largest: 0.48, then 0.408", "[P1]"),
                            ("3. Order remaining values: 0.084, 0.048, 0.0408", "[A1]")
                        ],
                        "final_answer": "0.48,  0.408,  0.084,  0.048,  0.0408",
                        "pitfall": "Assuming longer decimal strings are bigger (e.g. thinking 0.0408 is larger than 0.48 because it has 4 digits).",
                        "reverse_check": "Convert to fractions over 10,000: 4800/10000 > 4080/10000 > 840/10000 > 480/10000 > 408/10000."
                    }
                ]
            },
            {
                "title": "Section C: Exam-Style Problem Solving",
                "meta": "Questions 5 & 6 • 8 Marks",
                "questions": [
                    {
                        "title": "Question 5 (Level 2 Budget Breakdown)",
                        "marks": 4,
                        "stem": "An Integrated Care Board (ICB) allocates an annual mental health modernization grant of <strong>£3,850,000</strong>.<br>The financial director reports that <em>'Three hundred and eighty-five thousand pounds'</em> will be spent on staff wellness, while <em>'Three million, four hundred and sixty thousand pounds'</em> is allocated to clinical facility upgrades.<br><br>Calculate whether the sum of these two allocations matches the total grant, or if there is an unallocated contingency balance. State the exact difference if any.",
                        "lines": 5,
                        "ans_label": "Difference / Balance =",
                        "choice_box": "£ ____________________",
                        "step_rows": [
                            ("1. Convert staff wellness to digits: £385,000", "[P1]"),
                            ("2. Convert clinical facilities to digits: £3,460,000", "[P1]"),
                            ("3. Sum allocations: £385,000 + £3,460,000 = £3,845,000", "[M1]"),
                            ("4. Compare with total grant: £3,850,000 - £3,845,000 = £5,000 unallocated contingency balance", "[A1]")
                        ],
                        "final_answer": "£5,000 unallocated contingency balance",
                        "pitfall": "Writing £385,000 as 38,500 or £3,460,000 as 3,046,000 when converting verbal financial statements.",
                        "reverse_check": "£3,460,000 + £385,000 + £5,000 = £3,850,000."
                    },
                    {
                        "title": "Question 6 (Level 2 Decision & Justification)",
                        "marks": 4,
                        "stem": "A procurement manager claims: <em>'Rounding our annual consumables expenditure of £1,496,250 to the nearest ten thousand gives £1,490,000.'</em><br><br>Is the manager's claim correct?<br>Show your rounding method clearly, explain why the claim is right or wrong, and state the correct rounded figure.",
                        "lines": 5,
                        "ans_label": "Decision & Rounded Value =",
                        "choice_box": "Correct / Incorrect: £ ________________",
                        "step_rows": [
                            ("1. Identify the ten-thousands digit (9, representing 90,000) and the deciding digit immediately to its right in thousands column (6)", "[P1]"),
                            ("2. Apply rounding rule: since the deciding digit is 6 (≥ 5), round UP: 90,000 + 10,000 = 100,000 (carrying 1 to hundred-thousands)", "[M1]"),
                            ("3. Correct rounded value: £1,500,000", "[A1]"),
                            ("4. Valid conclusion: <strong>No / Incorrect</strong>, the manager rounded down or truncated the number rather than rounding up to £1,500,000.", "[A1]")
                        ],
                        "final_answer": "Incorrect; Correct rounded value is £1,500,000",
                        "pitfall": "Learners often forget to carry over into the next place column when rounding a '9', resulting in £1,490,000 or £1,410,000.",
                        "reverse_check": "£1,496,250 is £6,250 away from £1,490,000, but only £3,750 away from £1,500,000. It is closer to £1,500,000."
                    }
                ]
            }
        ]
    },
    {
        "slug": "ordering-numbers",
        "title": "Ordering Numbers",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: E3.1 • L1.1 • L2.1",
        "total_marks": 18,
        "formula_hint": "When ordering large numbers, count the total digits first. If digit counts are equal, compare from the highest place value on the left to the right. For negative numbers, remember that numbers further to the left on a number line have smaller values (-15 is smaller than -4).",
        "back_url": "../functional-skills-ordering-numbers.html",
        "sections": [
            {
                "title": "Section A: Core Skills (Warm-Up)",
                "meta": "Questions 1 & 2 • 4 Marks",
                "questions": [
                    {
                        "title": "Question 1 (Level 1 Large Whole Numbers)",
                        "marks": 2,
                        "stem": "Write the following figures in ascending order (smallest to largest):<br><strong>842,500 &nbsp;|&nbsp; 824,900 &nbsp;|&nbsp; 842,050 &nbsp;|&nbsp; 829,400 &nbsp;|&nbsp; 840,999</strong>",
                        "lines": 3,
                        "ans_label": "Ascending order =",
                        "choice_box": "________________________________________________________",
                        "step_rows": [
                            ("1. Compare ten-thousands: 824k and 829k are smaller than 840k+", "[M1]"),
                            ("2. Complete exact ascending order: 824,900; 829,400; 840,999; 842,050; 842,500", "[A1]")
                        ],
                        "final_answer": "824,900  <  829,400  <  840,999  <  842,050  <  842,500",
                        "pitfall": "Swapping 842,050 and 842,500 by misreading the hundreds place.",
                        "reverse_check": "Verify pairwise: 824.9k < 829.4k < 841.0k < 842.05k < 842.5k."
                    },
                    {
                        "title": "Question 2 (Level 1 Negative Numbers & Temperature)",
                        "marks": 2,
                        "stem": "Place the following overnight freezer temperatures in order from <strong>coldest</strong> to <strong>warmest</strong>:<br><strong>-18.5°C &nbsp;|&nbsp; -22.0°C &nbsp;|&nbsp; -14.2°C &nbsp;|&nbsp; -22.8°C &nbsp;|&nbsp; -19.1°C</strong>",
                        "lines": 3,
                        "ans_label": "Coldest to warmest =",
                        "choice_box": "________________________________________________________",
                        "step_rows": [
                            ("1. Recognize coldest temperature corresponds to the most negative value: -22.8°C", "[M1]"),
                            ("2. Complete order from lowest to highest: -22.8°C, -22.0°C, -19.1°C, -18.5°C, -14.2°C", "[A1]")
                        ],
                        "final_answer": "-22.8°C,  -22.0°C,  -19.1°C,  -18.5°C,  -14.2°C",
                        "pitfall": "Treating negative numbers like positive numbers (e.g. thinking -14.2°C is coldest because 14.2 is the smallest number).",
                        "reverse_check": "-22.8 is furthest left on a horizontal Celsius thermometer."
                    }
                ]
            },
            {
                "title": "Section B: Everyday & Workplace Maths",
                "meta": "Questions 3 & 4 • 6 Marks",
                "questions": [
                    {
                        "title": "Question 3 (Level 1 Hospital Patient Admissions)",
                        "marks": 3,
                        "stem": "An acute hospital trust records quarterly attendances across five emergency departments:<br>• St Jude's: 148,620<br>• King's Cross: 146,890<br>• Queen's Park: 148,090<br>• Royal Victoria: 149,150<br>• City Central: 146,920<br><br>The operations manager needs to prioritize depot staffing from highest demand to lowest demand.<br>Rank the five departments in <strong>descending order</strong> of attendances.",
                        "lines": 4,
                        "ans_label": "Descending order =",
                        "choice_box": "1st: ________________  to  5th: ________________",
                        "step_rows": [
                            ("1. Identify highest attendance: Royal Victoria (149,150)", "[P1]"),
                            ("2. Compare remaining departments with 148k: St Jude's (148,620), Queen's Park (148,090)", "[P1]"),
                            ("3. Compare 146k departments and complete full descending order: Royal Victoria, St Jude's, Queen's Park, City Central (146,920), King's Cross (146,890)", "[A1]")
                        ],
                        "final_answer": "Royal Victoria (149,150) > St Jude's (148,620) > Queen's Park (148,090) > City Central (146,920) > King's Cross (146,890)",
                        "pitfall": "Ordering ascending instead of descending when the prompt asks from highest to lowest demand.",
                        "reverse_check": "149,150 > 148,620 > 148,090 > 146,920 > 146,890."
                    },
                    {
                        "title": "Question 4 (Level 2 Decimal Precision in Pharmacy Dispensing)",
                        "marks": 3,
                        "stem": "A pharmacy dispenser weighs five active compound samples in grams: <strong>0.375 g, 0.038 g, 0.308 g, 0.38 g, 0.0375 g</strong>.<br>The automated packaging machine requires the samples loaded in order from <strong>lightest</strong> to <strong>heaviest</strong>.<br>Set out the correct loading sequence.",
                        "lines": 4,
                        "ans_label": "Loading sequence =",
                        "choice_box": "Lightest: ________________  to  Heaviest: ________________",
                        "step_rows": [
                            ("1. Pad all values to four decimal places: 0.3750 g, 0.0380 g, 0.3080 g, 0.3800 g, 0.0375 g", "[M1]"),
                            ("2. Identify smallest: 0.0375 g, followed by 0.038 g", "[P1]"),
                            ("3. Order tenths values: 0.308 g, 0.375 g, 0.38 g", "[A1]")
                        ],
                        "final_answer": "0.0375 g,  0.038 g,  0.308 g,  0.375 g,  0.38 g",
                        "pitfall": "Placing 0.38 g before 0.375 g because 38 appears smaller than 375.",
                        "reverse_check": "375/10000 < 380/10000 < 3080/10000 < 3750/10000 < 3800/10000."
                    }
                ]
            },
            {
                "title": "Section C: Exam-Style Problem Solving",
                "meta": "Questions 5 & 6 • 8 Marks",
                "questions": [
                    {
                        "title": "Question 5 (Level 2 Financial Performance Comparison)",
                        "marks": 4,
                        "stem": "Four community social enterprises record their net annual trading balances (profit or loss):<br>• Enterprise Alpha: -£14,850<br>• Enterprise Beta: +£26,400<br>• Enterprise Gamma: -£18,200<br>• Enterprise Delta: -£9,750<br><br>The regional funding panel awards an emergency stabilization subsidy to the enterprise with the <strong>greatest financial loss</strong>.<br>Which enterprise receives the emergency subsidy, and what is the difference between the most financially distressed enterprise and the least distressed (highest profit) enterprise?",
                        "lines": 5,
                        "ans_label": "Subsidized Enterprise & Range =",
                        "choice_box": "Enterprise: ____________ | Difference: £ ____________",
                        "step_rows": [
                            ("1. Identify most negative trading balance (greatest loss): Enterprise Gamma (-£18,200)", "[P1]"),
                            ("2. Identify highest profit enterprise: Enterprise Beta (+£26,400)", "[P1]"),
                            ("3. Calculate span/difference between extremes: £26,400 - (-£18,200) = £26,400 + £18,200 = £44,600", "[M1]"),
                            ("4. State Enterprise Gamma receives subsidy with a difference of £44,600", "[A1]")
                        ],
                        "final_answer": "Enterprise Gamma receives subsidy; Difference is £44,600",
                        "pitfall": "Subtracting without double negatives (£26,400 - £18,200 = £8,200), ignoring that crossing zero requires adding the absolute values.",
                        "reverse_check": "Start at -£18,200: adding £18,200 reaches £0; adding further £26,400 reaches +£26,400. Total distance = £44,600."
                    },
                    {
                        "title": "Question 6 (Level 2 Combined Decimals & Fractions Evaluation)",
                        "marks": 4,
                        "stem": "An apprentice carpenter measures four timber lengths: <strong>1.65 m, 1 5/8 m, 1.625 m, 1 7/10 m</strong>.<br>The site supervisor states: <em>'1 5/8 metres and 1.625 metres are completely identical in length, and 1.65 m is the longest piece of timber.'</em><br><br>Evaluate both parts of the supervisor's statement.<br>Convert all lengths to decimals to show whether the supervisor is correct or incorrect.",
                        "lines": 5,
                        "ans_label": "Evaluation & Explanation =",
                        "choice_box": "Supervisor is: Partially Correct / Fully Correct / Incorrect",
                        "step_rows": [
                            ("1. Convert 1 5/8 to decimal: 5 ÷ 8 = 0.625, so 1 5/8 = 1.625 m", "[P1]"),
                            ("2. Convert 1 7/10 to decimal: 7 ÷ 10 = 0.70, so 1 7/10 = 1.70 m", "[P1]"),
                            ("3. Compare all four lengths: 1.625 m = 1.625 m < 1.65 m < 1.70 m", "[M1]"),
                            ("4. Conclude: The supervisor is <strong>partially correct</strong>. 1 5/8 m and 1.625 m are identical, BUT 1.65 m is NOT the longest; 1 7/10 m (1.70 m) is the longest.", "[A1]")
                        ],
                        "final_answer": "Partially correct; 1 5/8 m = 1.625 m, but 1 7/10 m (1.70 m) is the longest piece",
                        "pitfall": "Overlooking 1 7/10 m by treating 7/10 as 0.07 rather than 0.70 m.",
                        "reverse_check": "1.625 = 1 5/8; 1.65 = 1 13/20; 1.70 = 1 7/10. 1.70 > 1.65 > 1.625."
                    }
                ]
            }
        ]
    }
]

print(f"Loaded {len(TOPICS_MATHS_NUMBER)} topics in topics_maths_number.py")

TOPICS_MATHS_NUMBER.extend([
    {
        "slug": "addition-and-subtraction",
        "title": "Addition & Subtraction",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: E3.2 • L1.3 • L2.2",
        "total_marks": 18,
        "formula_hint": "Align digits strictly by decimal point or place value columns. Remember to carry over additions ≥ 10 into the left column, and decompose/borrow from the next column to the left during subtraction when the top digit is smaller than the bottom.",
        "back_url": "../functional-skills-addition-and-subtraction.html",
        "sections": [
            {
                "title": "Section A: Core Skills (Warm-Up)",
                "meta": "Questions 1 & 2 • 4 Marks",
                "questions": [
                    {
                        "title": "Question 1 (Level 1 Multi-Digit Arithmetic)",
                        "marks": 2,
                        "stem": "Calculate: <strong>£48,675 + £19,488</strong>.<br>Set out your column addition clearly.",
                        "lines": 3,
                        "ans_label": "Sum =",
                        "choice_box": "£ ____________________",
                        "step_rows": [
                            ("1. Correct column alignment and carry-overs shown", "[M1]"),
                            ("2. Final accurate sum: £68,163", "[A1]")
                        ],
                        "final_answer": "£68,163",
                        "pitfall": "Forgetting to add carried digits from tens and hundreds columns into the thousands column.",
                        "reverse_check": "£68,163 - £19,488 = £48,675."
                    },
                    {
                        "title": "Question 2 (Level 1 Decimal Subtraction)",
                        "marks": 2,
                        "stem": "Work out: <strong>524.3 kg - 187.65 kg</strong>.<br>Show your decomposition / borrowing clearly.",
                        "lines": 3,
                        "ans_label": "Difference =",
                        "choice_box": "_____________ kg",
                        "step_rows": [
                            ("1. Pad 524.3 with placeholder zero (524.30) and align decimal points", "[M1]"),
                            ("2. Complete subtraction: 336.65 kg", "[A1]")
                        ],
                        "final_answer": "336.65 kg",
                        "pitfall": "Subtracting '0 minus 5 = 5' without borrowing from the tenths column, giving 336.75 kg.",
                        "reverse_check": "336.65 + 187.65 = 524.30 kg."
                    }
                ]
            },
            {
                "title": "Section B: Everyday & Workplace Maths",
                "meta": "Questions 3 & 4 • 6 Marks",
                "questions": [
                    {
                        "title": "Question 3 (Level 1 Medical Stock Reconciliation)",
                        "marks": 3,
                        "stem": "A surgical pharmacy begins the week with <strong>12,450 ampoules</strong> of saline solution.<br>During the week:<br>• Monday to Wednesday deliveries dispatch 3,820 ampoules to Ward 4 and 4,165 ampoules to Intensive Care.<br>• On Thursday, a restock shipment of 5,500 ampoules arrives.<br>• On Friday, Emergency Care uses 2,980 ampoules.<br><br>How many saline ampoules remain in the pharmacy at the end of Friday?",
                        "lines": 4,
                        "ans_label": "Remaining ampoules =",
                        "choice_box": "_____________ ampoules",
                        "step_rows": [
                            ("1. Calculate total initial stock plus delivery: 12,450 + 5,500 = 17,950", "[P1]"),
                            ("2. Calculate total dispatches: 3,820 + 4,165 + 2,980 = 10,965 ampoules", "[M1]"),
                            ("3. Subtract total dispatches: 17,950 - 10,965 = 6,985 ampoules", "[A1]")
                        ],
                        "final_answer": "6,985 ampoules",
                        "pitfall": "Subtracting the 5,500 restock delivery instead of adding it to the available inventory.",
                        "reverse_check": "6,985 + 2,980 - 5,500 + 4,165 + 3,820 = 12,450 ampoules."
                    },
                    {
                        "title": "Question 4 (Level 2 Ward Operating Budget Tracking)",
                        "marks": 3,
                        "stem": "A healthcare ward has a quarterly operational budget of <strong>£95,000</strong>.<br>The ward clerk logs the following actual expenditures:<br>• Nurse agency staffing: £54,320.50<br>• Medical consumables & bandages: £18,745.25<br>• Equipment maintenance: £9,860.00<br>• Patient dietary supplies: £7,412.80<br><br>Calculate the exact surplus or deficit balance remaining on the budget at quarter end.",
                        "lines": 4,
                        "ans_label": "Budget Balance =",
                        "choice_box": "£ ________________ (Surplus / Deficit)",
                        "step_rows": [
                            ("1. Add all four expenditures: £54,320.50 + £18,745.25 + £9,860.00 + £7,412.80 = £90,338.55", "[M1]"),
                            ("2. Subtract total expenditure from budget: £95,000.00 - £90,338.55 = £4,661.45", "[P1]"),
                            ("3. Identify as a surplus (underspend): £4,661.45 surplus", "[A1]")
                        ],
                        "final_answer": "£4,661.45 Surplus",
                        "pitfall": "Arithmetic slip when aligning the decimal hundredths (.50 + .25 + .00 + .80 = 1.55).",
                        "reverse_check": "£90,338.55 + £4,661.45 = £95,000.00."
                    }
                ]
            },
            {
                "title": "Section C: Exam-Style Problem Solving",
                "meta": "Questions 5 & 6 • 8 Marks",
                "questions": [
                    {
                        "title": "Question 5 (Level 2 Multi-Step Solar Panel Cost Comparison)",
                        "marks": 4,
                        "stem": "A community clinic evaluates installing solar panels to reduce electricity bills.<br>• Current annual electricity bill: <strong>£16,420</strong>.<br>• The solar system will save £4,850 each year on electricity.<br>• Total installation cost: £18,500.<br>• The clinic secures an environmental grant of £6,200 towards installation.<br><br>How many whole years of electricity savings will it take to recover the clinic's out-of-pocket installation cost?",
                        "lines": 5,
                        "ans_label": "Payback Period =",
                        "choice_box": "_____________ whole years",
                        "step_rows": [
                            ("1. Calculate net out-of-pocket installation cost: £18,500 - £6,200 = £12,300", "[P1]"),
                            ("2. Divide net cost by annual saving: £12,300 ÷ £4,850 = 2.536... years", "[M1]"),
                            ("3. Interpret in context: 2 years only saves £9,700 (still £2,600 short); requires 3 years to fully recover out-of-pocket cost", "[P1]"),
                            ("4. Award mark for stating 3 whole years", "[A1]")
                        ],
                        "final_answer": "3 whole years",
                        "pitfall": "Using the gross £18,500 without deducting the £6,200 grant, or rounding down 2.536 years to 2 years.",
                        "reverse_check": "Year 2 savings: 2 × £4,850 = £9,700 (< £12,300). Year 3 savings: 3 × £4,850 = £14,550 (> £12,300)."
                    },
                    {
                        "title": "Question 6 (Level 2 Dispute & Justification)",
                        "marks": 4,
                        "stem": "A transport manager reviews quarterly diesel fuel expenditure across three depot delivery fleets:<br>• Fleet North: £34,820<br>• Fleet South: £42,150<br>• Fleet East: £29,980<br><br>The finance controller states: <em>'The combined expenditure for Fleet North and Fleet East was more than £3,000 greater than Fleet South alone.'</em><br><br>Is the finance controller correct?<br>Show your calculations clearly and state a definitive conclusion.",
                        "lines": 5,
                        "ans_label": "Decision & Margin =",
                        "choice_box": "Yes / No: Difference is £ ____________",
                        "step_rows": [
                            ("1. Sum Fleet North and Fleet East: £34,820 + £29,980 = £64,800", "[M1]"),
                            ("2. Compare against Fleet South: £64,800 - £42,150 = £22,650", "[P1]"),
                            ("3. Evaluate against claim of 'more than £3,000': £22,650 is substantially greater than £3,000", "[M1]"),
                            ("4. Conclude: <strong>Yes, the controller is correct</strong>. Fleet North and Fleet East combined exceed Fleet South by £22,650 (which is well over £3,000).", "[A1]")
                        ],
                        "final_answer": "Yes, correct (combined spend exceeds South by £22,650)",
                        "pitfall": "Comparing North alone against South (£34,820 - £42,150) rather than North and East combined.",
                        "reverse_check": "£42,150 + £22,650 = £64,800 = £34,820 + £29,980."
                    }
                ]
            }
        ]
    },
    {
        "slug": "multiplication",
        "title": "Multiplication",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: E3.3 • L1.4 • L2.3",
        "total_marks": 18,
        "formula_hint": "When multiplying large numbers, use grid method or traditional long multiplication with place-value zeroes. For decimals, count total decimal places in both factors, multiply as whole numbers, and restore decimal places in the product.",
        "back_url": "../functional-skills-multiplication.html",
        "sections": [
            {
                "title": "Section A: Core Skills (Warm-Up)",
                "meta": "Questions 1 & 2 • 4 Marks",
                "questions": [
                    {
                        "title": "Question 1 (Level 1 Long Multiplication)",
                        "marks": 2,
                        "stem": "Work out: <strong>438 × 26</strong>.<br>Show full working including intermediate rows.",
                        "lines": 4,
                        "ans_label": "Product =",
                        "choice_box": "____________________",
                        "step_rows": [
                            ("1. Multiply by 6: 438 × 6 = 2,628; Multiply by 20: 438 × 20 = 8,760", "[M1]"),
                            ("2. Sum rows: 2,628 + 8,760 = 11,388", "[A1]")
                        ],
                        "final_answer": "11,388",
                        "pitfall": "Omitting the placeholder zero in the second multiplication row (treating 2 as 2 instead of 20), yielding 2,628 + 876 = 3,504.",
                        "reverse_check": "11,388 ÷ 26 = 438."
                    },
                    {
                        "title": "Question 2 (Level 2 Decimal Multiplication)",
                        "marks": 2,
                        "stem": "Calculate: <strong>3.75 × 4.8</strong> without a calculator.",
                        "lines": 3,
                        "ans_label": "Product =",
                        "choice_box": "____________________",
                        "step_rows": [
                            ("1. Multiply whole numbers 375 × 48 = 18,000", "[M1]"),
                            ("2. Insert 3 decimal places (2 + 1): 18.000 = 18", "[A1]")
                        ],
                        "final_answer": "18 (or 18.0)",
                        "pitfall": "Miscounting decimal places (e.g. putting 1.8 or 180).",
                        "reverse_check": "3.75 × 4 = 15; 3.75 × 0.8 = 3; 15 + 3 = 18."
                    }
                ]
            },
            {
                "title": "Section B: Everyday & Workplace Maths",
                "meta": "Questions 3 & 4 • 6 Marks",
                "questions": [
                    {
                        "title": "Question 3 (Level 1 Care Home Nutrition Bulk Order)",
                        "marks": 3,
                        "stem": "A residential care home orders <strong>85 cases</strong> of medical nutritional drinks.<br>Each case contains <strong>24 bottles</strong>.<br>Each bottle contains <strong>200 ml</strong> of supplement.<br><br>Work out the total volume of nutritional supplement ordered in <strong>litres</strong>.<br>(1 litre = 1,000 ml)",
                        "lines": 4,
                        "ans_label": "Total Volume =",
                        "choice_box": "_____________ litres",
                        "step_rows": [
                            ("1. Multiply cases by bottles per case: 85 × 24 = 2,040 bottles", "[M1]"),
                            ("2. Multiply total bottles by volume: 2,040 × 200 ml = 408,000 ml", "[P1]"),
                            ("3. Convert ml to litres: 408,000 ÷ 1,000 = 408 litres", "[A1]")
                        ],
                        "final_answer": "408 litres",
                        "pitfall": "Stopping at 408,000 ml without converting to litres as required by the units.",
                        "reverse_check": "408 L ÷ 85 cases = 4.8 L per case. 4.8 L ÷ 24 bottles = 0.2 L = 200 ml per bottle."
                    },
                    {
                        "title": "Question 4 (Level 2 Facilities Flooring Labour & Materials)",
                        "marks": 3,
                        "stem": "A flooring specialist quotes for laying vinyl flooring in a health clinic.<br>• Clinic floor area: <strong>72 square metres</strong>.<br>• Vinyl flooring cost: <strong>£22.50 per square metre</strong>.<br>• Adhesive and underlay: <strong>£4.80 per square metre</strong>.<br>• Labour: 2 fitters working <strong>14 hours each</strong> at <strong>£18.50 per hour</strong>.<br><br>Work out the total cost quoted for materials and labour combined.",
                        "lines": 5,
                        "ans_label": "Total Quote =",
                        "choice_box": "£ ____________________",
                        "step_rows": [
                            ("1. Materials cost: 72 × (£22.50 + £4.80) = 72 × £27.30 = £1,965.60", "[M1]"),
                            ("2. Labour hours and cost: 2 × 14 = 28 hours; 28 × £18.50 = £518.00", "[P1]"),
                            ("3. Total combination: £1,965.60 + £518.00 = £2,483.60", "[A1]")
                        ],
                        "final_answer": "£2,483.60",
                        "pitfall": "Calculating labour for only 1 fitter (14 × £18.50 = £259) instead of 2 fitters.",
                        "reverse_check": "Materials £1,965.60 + Labour £518.00 = £2,483.60."
                    }
                ]
            },
            {
                "title": "Section C: Exam-Style Problem Solving",
                "meta": "Questions 5 & 6 • 8 Marks",
                "questions": [
                    {
                        "title": "Question 5 (Level 2 Staff Overtime Pay Rota)",
                        "marks": 4,
                        "stem": "In an ambulance control centre, 16 dispatchers work overtime over a public holiday weekend.<br>• 12 dispatchers each work <strong>9.5 hours</strong> at an enhanced overtime rate of <strong>£21.40 per hour</strong>.<br>• 4 senior dispatchers each work <strong>11.0 hours</strong> at a supervisor overtime rate of <strong>£26.50 per hour</strong>.<br><br>The operations director allocated an overtime contingency budget of <strong>£3,500</strong>.<br>Will this budget cover the total overtime cost? Show your working and state the exact difference.",
                        "lines": 5,
                        "ans_label": "Evaluation & Difference =",
                        "choice_box": "Sufficient / Insufficient: Difference £ ____________",
                        "step_rows": [
                            ("1. Calculate standard dispatcher overtime: 12 × 9.5 = 114 hours; 114 × £21.40 = £2,439.60", "[P1]"),
                            ("2. Calculate senior dispatcher overtime: 4 × 11 = 44 hours; 44 × £26.50 = £1,166.00", "[P1]"),
                            ("3. Sum total overtime: £2,439.60 + £1,166.00 = £3,605.60", "[M1]"),
                            ("4. Compare with budget: £3,605.60 > £3,500; Over budget by £105.60 (Insufficient)", "[A1]")
                        ],
                        "final_answer": "Insufficient (Over budget by £105.60)",
                        "pitfall": "Multiplying 12 by £21.40 without multiplying by the 9.5 hours worked.",
                        "reverse_check": "£2,439.60 + £1,166.00 = £3,605.60. £3,605.60 - £3,500 = £105.60 overspend."
                    },
                    {
                        "title": "Question 6 (Level 2 Bulk Buying Trade Discount)",
                        "marks": 4,
                        "stem": "A dental clinic purchases examination gloves in cases of 10 boxes (100 gloves per box).<br>Supplier A offers: <strong>£48.00 per case</strong> with the promotion: <em>'Buy 5 cases, get 1 free'</em>.<br>Supplier B offers: <strong>£41.50 per case</strong> with a flat <strong>10% trade discount</strong> on all orders.<br><br>The clinic needs <strong>18 cases</strong> of gloves.<br>Which supplier is cheaper, and by exactly how much?",
                        "lines": 5,
                        "ans_label": "Cheaper Supplier & Saving =",
                        "choice_box": "Supplier _____ is cheaper by £ ____________",
                        "step_rows": [
                            ("1. Supplier A deal: to get 18 cases, clinic buys 15 cases and gets 3 free (3 sets of 5+1 = 18 cases). Cost: 15 × £48.00 = £720.00", "[P1]"),
                            ("2. Supplier B deal: 18 × £41.50 = £747.00. 10% discount = £74.70. Net cost: £747.00 - £74.70 = £672.30", "[M1]"),
                            ("3. Calculate price difference: £720.00 - £672.30 = £47.70", "[P1]"),
                            ("4. State conclusion: Supplier B is cheaper by £47.70", "[A1]")
                        ],
                        "final_answer": "Supplier B is cheaper by £47.70",
                        "pitfall": "Charging for 18 cases at Supplier A (18 × £48 = £864) without applying the free cases earned.",
                        "reverse_check": "Supplier A: 15 × £48 = £720. Supplier B: 18 × £41.50 × 0.9 = £672.30. £720 - £672.30 = £47.70."
                    }
                ]
            }
        ]
    }
])
print(f"Total topics in topics_maths_number.py: {len(TOPICS_MATHS_NUMBER)}")
