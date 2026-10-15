#!/usr/bin/env python3
"""
Maths Core Number & Calculation Curriculum Data for Worksheets & Mark Schemes.
Topics: Division, BIDMAS, Rounding/Estimating, Fractions, Decimals, Percentages, FDP, Ratio, Proportion, Formulas, Money, Best Buys, Compound Interest.
"""

MATHS_CORE_TOPICS = [
    {
        "slug": "division",
        "title": "Division & Remainders",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: E3.4 • L1.5 • L2.4",
        "total_marks": 18,
        "formula_hint": "In Functional Skills context questions, remainders cannot simply be left as 'r 3'. You must interpret whether to round UP (e.g. hiring coaches, ordering boxes) or round DOWN (e.g. full items made).",
        "back_url": "../functional-skills-division.html",
        "sections": [
            {
                "title": "Section A: Procedural Fluency Check",
                "meta": "Questions 1 & 2 • 4 Marks",
                "questions": [
                    {
                        "title": "Question 1 (Level 1 Short Division)",
                        "marks": 2,
                        "stem": "Work out: <strong>1,848 ÷ 7</strong> without a calculator.",
                        "lines": 3,
                        "ans_label": "Quotient =",
                        "choice_box": "____________________",
                        "step_rows": [
                            ("1. Set up bus stop method: 18 ÷ 7 = 2 r 4; 44 ÷ 7 = 6 r 2; 28 ÷ 7 = 4", "[M1]"),
                            ("2. State accurate quotient: 264", "[A1]")
                        ],
                        "final_answer": "264",
                        "pitfall": "Losing track of remainders carried to the next digit.",
                        "reverse_check": "264 × 7 = 1,848."
                    },
                    {
                        "title": "Question 2 (Level 2 Long Division / Decimal Quotient)",
                        "marks": 2,
                        "stem": "Work out: <strong>315 ÷ 12</strong>.<br>Give your answer as a decimal.",
                        "lines": 3,
                        "ans_label": "Decimal Quotient =",
                        "choice_box": "____________________",
                        "step_rows": [
                            ("1. 315 ÷ 12: 12 into 31 goes 2 times (24) r 7; into 75 goes 6 times (72) r 3", "[M1]"),
                            ("2. Convert remainder to decimal: 3/12 = 0.25; Final answer 26.25", "[A1]")
                        ],
                        "final_answer": "26.25",
                        "pitfall": "Writing remainder 3 as .3 instead of 3/12 = 0.25.",
                        "reverse_check": "26.25 × 12 = 315."
                    }
                ]
            },
            {
                "title": "Section B: Workplace & Functional Scenarios",
                "meta": "Questions 3 & 4 • 6 Marks",
                "questions": [
                    {
                        "title": "Question 3 (Level 1 Event Coach Transport)",
                        "marks": 3,
                        "stem": "A community youth charity organizes a trip for <strong>214 attendees</strong> and staff.<br>Each hired minibus can safely seat a maximum of <strong>16 passengers</strong>.<br><br>How many minibuses must the charity hire to transport everyone?",
                        "lines": 4,
                        "ans_label": "Minibuses needed =",
                        "choice_box": "_____________ minibuses",
                        "step_rows": [
                            ("1. Divide total passengers by capacity: 214 ÷ 16 = 13.375", "[M1]"),
                            ("2. Interpret remainder in context: 13 buses carry 208 people, leaving 6 people behind", "[P1]"),
                            ("3. Round UP to guarantee seating for all: 14 minibuses", "[A1]")
                        ],
                        "final_answer": "14 minibuses",
                        "pitfall": "Rounding down to 13 minibuses, leaving 6 passengers without transport.",
                        "reverse_check": "13 × 16 = 208 (< 214); 14 × 16 = 224 (seats all 214 with 10 spare seats)."
                    },
                    {
                        "title": "Question 4 (Level 2 Pharmacy Batch Packaging)",
                        "marks": 3,
                        "stem": "An automated pharmaceutical machine produces <strong>4,500 vitamin tablets</strong> per hour.<br>Tablets are packed into blister packs of <strong>14 tablets</strong> each.<br>The blister packs are then packed into cartons of <strong>10 packs</strong> each.<br><br>How many complete cartons can be produced from one hour's production run?",
                        "lines": 4,
                        "ans_label": "Complete cartons =",
                        "choice_box": "_____________ cartons",
                        "step_rows": [
                            ("1. Calculate tablets per carton: 14 × 10 = 140 tablets per carton", "[M1]"),
                            ("2. Divide total production: 4,500 ÷ 140 = 32.14... cartons (or 4500 ÷ 14 = 321 packs; 321 ÷ 10 = 32.1)", "[P1]"),
                            ("3. State number of COMPLETE cartons (round DOWN): 32 cartons", "[A1]")
                        ],
                        "final_answer": "32 complete cartons",
                        "pitfall": "Rounding up to 33 cartons when incomplete cartons cannot be sold.",
                        "reverse_check": "32 × 140 = 4,480 tablets used; 4,500 - 4,480 = 20 spare tablets (insufficient for another carton)."
                    }
                ]
            },
            {
                "title": "Section C: Pearson Edexcel Problem Solving & Justification",
                "meta": "Questions 5 & 6 • 8 Marks",
                "questions": [
                    {
                        "title": "Question 5 (Level 2 Equal Weekly Pay Deduction)",
                        "marks": 4,
                        "stem": "An employee undertakes an accredited Level 4 training qualification costing <strong>£2,184</strong>.<br>The employer agrees to pay the fee upfront. The employee will repay the total cost via equal deductions from their weekly payslip over a <strong>9-month period</strong>.<br>Assume exactly <strong>39 weekly pay cycles</strong> in the 9-month repayment period.<br><br>Calculate the exact weekly deduction from the employee's pay.",
                        "lines": 5,
                        "ans_label": "Weekly deduction =",
                        "choice_box": "£ _____________ per week",
                        "step_rows": [
                            ("1. Identify total loan (£2,184) and total installments (39 weeks)", "[P1]"),
                            ("2. Division method: £2,184 ÷ 39", "[M1]"),
                            ("3. Long division: 39 into 218 goes 5 times (195) r 23; into 234 goes exactly 6 times", "[P1]"),
                            ("4. State exact weekly deduction: £56.00", "[A1]")
                        ],
                        "final_answer": "£56.00 per week",
                        "pitfall": "Dividing by 9 months (£242.67) instead of 39 weekly pay cycles.",
                        "reverse_check": "39 × £56.00 = £2,184.00."
                    },
                    {
                        "title": "Question 6 (Level 2 Catering Recipe Scaling Justification)",
                        "marks": 4,
                        "stem": "A hospital head chef has <strong>25 kg</strong> of diced stewing beef.<br>The standard hospital casserole recipe requires <strong>180 grams</strong> of beef per adult portion.<br>The ward manager states: <em>'We have enough beef here to serve 140 patients for today's lunch.'</em><br><br>Is the ward manager correct?<br>Show your calculations clearly with units and state a definitive conclusion.",
                        "lines": 5,
                        "ans_label": "Conclusion & Portion Count =",
                        "choice_box": "Correct / Incorrect: Can serve _____ portions",
                        "step_rows": [
                            ("1. Convert kg to grams: 25 kg = 25,000 g", "[P1]"),
                            ("2. Divide total beef by portion size: 25,000 ÷ 180 = 138.88... portions", "[M1]"),
                            ("3. Contextual rounding: only 138 full adult portions can be made", "[P1]"),
                            ("4. Conclude: <strong>No / Incorrect</strong>; 138 full portions is less than the required 140 (short by 2 portions or 200 g of beef).", "[A1]")
                        ],
                        "final_answer": "Incorrect; Only 138 full portions can be made (short by 2 portions)",
                        "pitfall": "Rounding 138.88 up to 139 and saying 'yes', forgetting that 140 portions requires 140 × 180 = 25,200 g.",
                        "reverse_check": "140 × 180 g = 25,200 g = 25.2 kg. 25.0 kg < 25.2 kg. Cannot serve 140."
                    }
                ]
            }
        ]
    },
    {
        "slug": "bidmas",
        "title": "BIDMAS / Order of Operations",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.6 • L2.5",
        "total_marks": 18,
        "formula_hint": "B - Brackets, I - Indices/Powers, D - Division, M - Multiplication, A - Addition, S - Subtraction. Operations of equal priority (D/M and A/S) are calculated from left to right.",
        "back_url": "../functional-skills-bidmas.html",
        "sections": [
            {
                "title": "Section A: Procedural Fluency Check",
                "meta": "Questions 1 & 2 • 4 Marks",
                "questions": [
                    {
                        "title": "Question 1 (Level 1 Arithmetic Order)",
                        "marks": 2,
                        "stem": "Work out: <strong>15 + 8 × 4 - 6</strong>.",
                        "lines": 3,
                        "ans_label": "Result =",
                        "choice_box": "____________________",
                        "step_rows": [
                            ("1. Multiplication first: 8 × 4 = 32", "[M1]"),
                            ("2. Addition and subtraction left to right: 15 + 32 = 47; 47 - 6 = 41", "[A1]")
                        ],
                        "final_answer": "41",
                        "pitfall": "Calculating strictly from left to right: (15 + 8) = 23; 23 × 4 = 92; 92 - 6 = 86 (incorrect).",
                        "reverse_check": "41 + 6 - (8 × 4) = 47 - 32 = 15."
                    },
                    {
                        "title": "Question 2 (Level 2 Brackets & Indices)",
                        "marks": 2,
                        "stem": "Evaluate: <strong>(14 - 5)² ÷ 3 + 7</strong>.",
                        "lines": 3,
                        "ans_label": "Result =",
                        "choice_box": "____________________",
                        "step_rows": [
                            ("1. Brackets first: 14 - 5 = 9; Indices: 9² = 81", "[M1]"),
                            ("2. Division: 81 ÷ 3 = 27; Addition: 27 + 7 = 34", "[A1]")
                        ],
                        "final_answer": "34",
                        "pitfall": "Multiplying 9 by 2 instead of squaring (9² = 81), or adding before dividing (81 ÷ 10).",
                        "reverse_check": "(34 - 7) × 3 = 81; √81 = 9; 9 + 5 = 14."
                    }
                ]
            },
            {
                "title": "Section B: Workplace & Functional Scenarios",
                "meta": "Questions 3 & 4 • 6 Marks",
                "questions": [
                    {
                        "title": "Question 3 (Level 1 Shift Wage Calculation)",
                        "marks": 3,
                        "stem": "A delivery driver's daily pay is calculated using the formula:<br><strong>Pay = £45 + (£12 × Hours) - £8 (Vehicle charge)</strong><br><br>Calculate the driver's pay for a day where they work <strong>7.5 hours</strong>.",
                        "lines": 4,
                        "ans_label": "Driver's Pay =",
                        "choice_box": "£ ____________________",
                        "step_rows": [
                            ("1. Calculate hourly earnings: £12 × 7.5 = £90.00", "[M1]"),
                            ("2. Add base pay: £45 + £90 = £135.00", "[P1]"),
                            ("3. Deduct vehicle charge: £135.00 - £8.00 = £127.00", "[A1]")
                        ],
                        "final_answer": "£127.00",
                        "pitfall": "Adding £45 + £12 first to get £57, then multiplying by 7.5 (£427.50).",
                        "reverse_check": "£127 + £8 - £45 = £90; £90 ÷ £12 = 7.5 hours."
                    },
                    {
                        "title": "Question 4 (Level 2 Warehouse Pallet Volumetric Formula)",
                        "marks": 3,
                        "stem": "An export shipping container charges storage fees based on the formula:<br><strong>Fee = £35 + 4 × (Length + Width) × Height</strong><br>For a pallet measuring: Length = 1.2 m, Width = 0.8 m, Height = 1.5 m.<br><br>Calculate the storage fee in pounds (£).",
                        "lines": 4,
                        "ans_label": "Storage Fee =",
                        "choice_box": "£ ____________________",
                        "step_rows": [
                            ("1. Evaluate brackets: Length + Width = 1.2 + 0.8 = 2.0 m", "[M1]"),
                            ("2. Multiply factors: 4 × 2.0 × 1.5 = 12.0", "[P1]"),
                            ("3. Add base charge: £35 + £12 = £47.00", "[A1]")
                        ],
                        "final_answer": "£47.00",
                        "pitfall": "Adding £35 + 4 first (getting 39) before multiplying by the bracketed terms.",
                        "reverse_check": "£47 - £35 = £12; £12 ÷ (4 × 1.5) = 2.0; 2.0 - 0.8 = 1.2 m."
                    }
                ]
            },
            {
                "title": "Section C: Pearson Edexcel Problem Solving & Justification",
                "meta": "Questions 5 & 6 • 8 Marks",
                "questions": [
                    {
                        "title": "Question 5 (Level 2 Heating Energy Cost Audit)",
                        "marks": 4,
                        "stem": "A community leisure centre heating cost is determined by:<br><strong>Cost = Daily Standing Charge + (Day Units × Day Rate) + (Night Units × Night Rate)</strong><br><br>For one billing period:<br>• Daily standing charge: 30 days at £0.85 per day<br>• Day units: 4,200 kWh at £0.24 per kWh<br>• Night units: 1,800 kWh at £0.15 per kWh<br><br>Work out the total heating cost for the billing period.",
                        "lines": 5,
                        "ans_label": "Total Energy Bill =",
                        "choice_box": "£ ____________________",
                        "step_rows": [
                            ("1. Calculate standing charge: 30 × £0.85 = £25.50", "[P1]"),
                            ("2. Calculate day units cost: 4,200 × £0.24 = £1,008.00", "[P1]"),
                            ("3. Calculate night units cost: 1,800 × £0.15 = £270.00", "[M1]"),
                            ("4. Sum all three components: £25.50 + £1,008.00 + £270.00 = £1,303.50", "[A1]")
                        ],
                        "final_answer": "£1,303.50",
                        "pitfall": "Adding day and night units together (6,000 kWh) and multiplying by an average rate.",
                        "reverse_check": "£1,303.50 - £25.50 = £1,278.00; £1,278 - £1,008 = £270.00."
                    },
                    {
                        "title": "Question 6 (Level 2 Calculator Input Error Evaluation)",
                        "marks": 4,
                        "stem": "An administrative apprentice calculates the average material cost across three work packages.<br>The invoices are £450, £620, and £580.<br>The apprentice enters into their calculator: <strong>450 + 620 + 580 ÷ 3</strong> and records an average of <strong>£1,263.33</strong>.<br><br>Explain the mathematical error the apprentice made using BIDMAS.<br>Show the correct formula that should have been used, and calculate the true average cost.",
                        "lines": 5,
                        "ans_label": "Explanation & True Average =",
                        "choice_box": "True Average = £ ____________",
                        "step_rows": [
                            ("1. Explain error: Due to BIDMAS, the calculator divides only the 580 by 3 (193.33) and then adds 450 + 620, instead of dividing the entire sum.", "[P1]"),
                            ("2. State required formula with brackets: (450 + 620 + 580) ÷ 3", "[M1]"),
                            ("3. Evaluate correct sum: 450 + 620 + 580 = £1,650", "[P1]"),
                            ("4. Calculate accurate average: £1,650 ÷ 3 = £550.00", "[A1]")
                        ],
                        "final_answer": "Error: Omitted brackets around the sum. True average is £550.00",
                        "pitfall": "Not recognizing that £1,263.33 is impossible as an average of three numbers between £450 and £620.",
                        "reverse_check": "£550 × 3 = £1,650; £1,650 - £450 - £620 = £580."
                    }
                ]
            }
        ]
    }
]

print(f"Loaded {len(MATHS_CORE_TOPICS)} topics in data_maths_core.py")
