#!/usr/bin/env python3
"""
Authentic Fluency Workouts: Maths Number & Calculations
10 Core High-Yield Topics:
- addition-and-subtraction
- multiplication
- division-and-remainders
- decimals
- decimal-basics
- bidmas
- ratio
- rounding-and-estimating
- money-invoicing-payroll
- algebra
"""

MATHS_NUMBER_WORKOUTS = {
    # 1. ADDITION & SUBTRACTION
    "addition-and-subtraction": {
        "title": "Addition & Subtraction",
        "slug": "addition-and-subtraction",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.1 • L1.2 • L2.1",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Core Rules & Alignment",
            "points": [
                "Column Addition: Always align place values (units under units, tens under tens, hundreds under hundreds).",
                "Carry digits clearly into the next column to avoid losing values in multi-digit addition.",
                "Subtractions with regrouping (borrowing): Check by adding your answer to the subtracted value (Inverse check).",
                "Decimals: Line up decimal points vertically BEFORE calculating, and add trailing zeros where needed (£45.20, not £45.2)."
            ],
            "calc_tip": "When calculating differences in financial balance sheets, write down negative signs clearly: -£140 means an overdraft/loss."
        },
        "workout_blocks": [
            {
                "title": "Rapid Column Addition (Integers & Money)",
                "instruction": "Work out the sum of each calculation without a calculator:",
                "items": [
                    ("a", "468 + 325", "793"),
                    ("b", "1,245 + 870", "2,115"),
                    ("c", "£34.50 + £18.75", "£53.25"),
                    ("d", "£125.60 + £89.45", "£215.05"),
                    ("e", "4,890 + 3,450 + 620", "8,960"),
                    ("f", "£12.45 + £8.99 + £15.20", "£36.64"),
                    ("g", "15,400 + 8,950", "24,350"),
                    ("h", "£450.80 + £275.95", "£726.75")
                ]
            },
            {
                "title": "Multi-Digit Subtraction with Regrouping",
                "instruction": "Subtract each value, showing clear decomposition/borrowing:",
                "items": [
                    ("a", "852 - 347", "505"),
                    ("b", "1,500 - 685", "815"),
                    ("c", "4,020 - 1,385", "2,635"),
                    ("d", "£100.00 - £34.80", "£65.20"),
                    ("e", "£250.00 - £168.45", "£81.55"),
                    ("f", "10,000 - 3,475", "6,525"),
                    ("g", "£50.00 - £18.35", "£31.65"),
                    ("h", "2,405 - 899", "1,506")
                ]
            },
            {
                "title": "Mental Arithmetic & Cash Change Drills",
                "instruction": "Work out the change from £20, £50, or £100:",
                "items": [
                    ("a", "Change from £20 when spending £14.30", "£5.70"),
                    ("b", "Change from £20 when spending £7.85", "£12.15"),
                    ("c", "Change from £50 when spending £28.40", "£21.60"),
                    ("d", "Change from £50 when spending £36.75", "£13.25"),
                    ("e", "Change from £100 when spending £62.80", "£37.20"),
                    ("f", "Change from £100 when spending £84.15", "£15.85")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Healthcare Hospital Ward Stock Tracking",
                "stem": "A healthcare ward starts Monday with <strong>450 boxes of nitrile gloves</strong>.<br>During the week, the deliveries and usage are:<br>• Tuesday: Used 165 boxes<br>• Wednesday: New delivery received of 240 boxes<br>• Thursday: Used 195 boxes<br>• Friday: Used 110 boxes<br>Calculate how many boxes of gloves remain on the ward at the end of Friday.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Calculate total stock added: 450 + 240 = 690 boxes", "[M1]"),
                    ("Calculate total stock used: 165 + 195 + 110 = 470 boxes", "[M1]"),
                    ("Calculate remaining stock: 690 - 470 = 220 boxes", "[A1]")
                ],
                "final_answer": "220 boxes",
                "reverse_check": "220 remaining + 470 used = 690 total.",
                "pitfall": "Adding used boxes or subtracting deliveries."
            },
            {
                "context_tag": "Commercial Trade Cash Float",
                "stem": "A retail pharmacy assistant counts the cash drawer float at the end of the day.<br>The opening float was <strong>£150.00</strong>.<br>Cash sales recorded through the till total <strong>£1,248.50</strong>.<br>Cash paid out for emergency delivery postage was <strong>£24.80</strong>.<br>When counting the cash drawer, the assistant finds <strong>£1,370.00</strong>.<br>Is the cash drawer balanced, over, or short? State the exact amount of difference.",
                "marks": 3,
                "prefix": "£",
                "steps": [
                    ("Expected total = Opening float (£150.00) + Sales (£1,248.50) - Payout (£24.80)", "[M1]"),
                    ("Expected cash = £1,398.50 - £24.80 = £1,373.70", "[M1]"),
                    ("Compare actual (£1,370.00) with expected (£1,373.70): £1,370.00 - £1,373.70 = -£3.70 (Short by £3.70)", "[A1]")
                ],
                "final_answer": "Short by £3.70 (Expected £1,373.70, actual £1,370.00)",
                "reverse_check": "£1,370.00 + £3.70 = £1,373.70.",
                "pitfall": "Forgetting to add the opening float to the expected total."
            }
        ]
    },

    # 2. MULTIPLICATION
    "multiplication": {
        "title": "Multiplication",
        "slug": "multiplication",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.3 • L2.1",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Grid Method & Standard Long Multiplication",
            "points": [
                "Multiplying by 10, 100, 1,000: Shift digits left by 1, 2, or 3 places (add placeholder zeros).",
                "Long multiplication: Remember to write a placeholder '0' on the second row when multiplying by the tens digit.",
                "Multiplying decimals: Count the total decimal places in the factors, multiply as whole numbers, then put the same number of decimal places in the product.",
                "Always estimate using rounded values first (e.g. 39 × 52 ≈ 40 × 50 = 2,000)."
            ],
            "calc_tip": "On non-calculator exams, split tough multiplications: 18 × 15 = (18 × 10) + (18 × 5) = 180 + 90 = 270."
        },
        "workout_blocks": [
            {
                "title": "Powers of Ten & Rapid Times Tables",
                "instruction": "Work out each answer mentally:",
                "items": [
                    ("a", "45 × 10", "450"),
                    ("b", "128 × 100", "12,800"),
                    ("c", "3.4 × 10", "34"),
                    ("d", "0.65 × 100", "65"),
                    ("e", "2.15 × 1,000", "2,150"),
                    ("f", "60 × 40", "2,400"),
                    ("g", "800 × 50", "40,000"),
                    ("h", "120 × 30", "3,600")
                ]
            },
            {
                "title": "Standard Long Multiplication Drills",
                "instruction": "Calculate showing all working lines:",
                "items": [
                    ("a", "46 × 18", "828"),
                    ("b", "73 × 24", "1,752"),
                    ("c", "135 × 12", "1,620"),
                    ("d", "248 × 15", "3,720"),
                    ("e", "364 × 25", "9,100"),
                    ("f", "512 × 34", "17,408"),
                    ("g", "124 × 45", "5,580"),
                    ("h", "625 × 16", "10,000")
                ]
            },
            {
                "title": "Decimals & Money Multiplication",
                "instruction": "Work out the total cost or quantity:",
                "items": [
                    ("a", "14 items at £2.50 each", "£35.00"),
                    ("b", "8 items at £4.99 each", "£39.92"),
                    ("c", "25 litres at £1.40 per litre", "£35.00"),
                    ("d", "30 hours at £11.50 per hour", "£345.00"),
                    ("e", "16 metres at £3.25 per metre", "£52.00"),
                    ("f", "40 kg at £0.85 per kg", "£34.00")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Healthcare Staff Rota & Overtime",
                "stem": "A senior healthcare assistant works <strong>36 standard hours</strong> at an hourly rate of <strong>£12.50</strong>.<br>She also works <strong>8 hours of overtime</strong> paid at <strong>time-and-a-half</strong> (1.5 times the standard rate).<br>Calculate her total gross pay for the week.",
                "marks": 3,
                "prefix": "£",
                "steps": [
                    ("Standard pay = 36 × £12.50 = £450.00", "[M1]"),
                    ("Overtime rate = £12.50 × 1.5 = £18.75 per hour. Overtime pay = 8 × £18.75 = £150.00", "[M1]"),
                    ("Total gross pay = £450.00 + £150.00 = £600.00", "[A1]")
                ],
                "final_answer": "£600.00",
                "reverse_check": "£600 - £450 = £150; £150 ÷ 8 = £18.75.",
                "pitfall": "Calculating overtime at standard rate without applying the 1.5 factor."
            }
        ]
    },

    # 3. DIVISION & REMAINDERS
    "division-and-remainders": {
        "title": "Division & Remainders",
        "slug": "division-and-remainders",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.4 • L2.1",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Short Division (Bus Stop Method) & Practical Rounding",
            "points": [
                "Short Division: Divide digit by digit from left to right, carrying any remainder to the next digit.",
                "Dividing by 10, 100, 1,000: Shift digits right by 1, 2, or 3 places.",
                "Remainders in real-world contexts: Always consider whether you must round UP or round DOWN (e.g. you cannot hire half a bus; leftover tiles leave a floor incomplete).",
                "Money: Express remainders as decimals to 2 decimal places (£0.00)."
            ],
            "calc_tip": "If a question asks 'how many vehicles/tins/packs needed to cover all items', always ROUND UP to the next whole number."
        },
        "workout_blocks": [
            {
                "title": "Short Division (Whole Numbers & Decimals)",
                "instruction": "Work out each division accurately:",
                "items": [
                    ("a", "456 ÷ 3", "152"),
                    ("b", "728 ÷ 4", "182"),
                    ("c", "945 ÷ 5", "189"),
                    ("d", "876 ÷ 6", "146"),
                    ("e", "1,248 ÷ 8", "156"),
                    ("f", "2,466 ÷ 9", "274"),
                    ("g", "£85.50 ÷ 5", "£17.10"),
                    ("h", "£147.00 ÷ 6", "£24.50")
                ]
            },
            {
                "title": "Division with Remainders & Fractional Answers",
                "instruction": "State the quotient and whole remainder (e.g. 5 R 2):",
                "items": [
                    ("a", "43 ÷ 5", "8 R 3"),
                    ("b", "67 ÷ 8", "8 R 3"),
                    ("c", "85 ÷ 6", "14 R 1"),
                    ("d", "94 ÷ 7", "13 R 3"),
                    ("e", "125 ÷ 4", "31 R 1 (or 31.25)"),
                    ("f", "150 ÷ 8", "18 R 6 (or 18.75)"),
                    ("g", "200 ÷ 12", "16 R 8"),
                    ("h", "350 ÷ 15", "23 R 5")
                ]
            },
            {
                "title": "Practical Contextual Rounding (Up or Down)",
                "instruction": "Determine the practical whole-number answer needed:",
                "items": [
                    ("a", "75 students go on a trip. Each minibus holds 16. How many minibuses?", "5 minibuses (75 ÷ 16 = 4.68 → round UP)"),
                    ("b", "100 eggs placed in boxes of 6. How many full boxes?", "16 full boxes (100 ÷ 6 = 16 R 4 → round DOWN)"),
                    ("c", "140 m of rope cut into 8 m jump ropes. How many ropes?", "17 ropes (140 ÷ 8 = 17.5 → round DOWN)"),
                    ("d", "210 tiles needed. Packs contain 20 tiles. How many packs?", "11 packs (210 ÷ 20 = 10.5 → round UP)"),
                    ("e", "£50 budget. Books cost £7 each. How many books can be bought?", "7 books (£50 ÷ £7 = 7.14 → round DOWN)"),
                    ("f", "85 patients need transport. Ambulances carry 4 each. How many trips?", "22 trips (85 ÷ 4 = 21.25 → round UP)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Care Home Transport Outing",
                "stem": "A community care centre is organizing a day trip for <strong>58 residents</strong> and <strong>14 care staff</strong>.<br>They are hiring minibuses. Each minibus carries up to <strong>15 passengers</strong>.<br>Hiring each minibus costs <strong>£120 per day</strong>.<br>How many minibuses must be hired, and what is the total hire cost?",
                "marks": 3,
                "prefix": "£",
                "steps": [
                    ("Calculate total people: 58 residents + 14 staff = 72 people", "[M1]"),
                    ("Calculate minibuses: 72 ÷ 15 = 4.8 → Must round UP to 5 minibuses to transport everyone", "[M1]"),
                    ("Calculate total cost: 5 minibuses × £120 = £600.00", "[A1]")
                ],
                "final_answer": "5 minibuses costing £600.00",
                "reverse_check": "5 × 15 = 75 seats (covers 72 people with 3 spare seats).",
                "pitfall": "Rounding down to 4 minibuses, leaving 12 passengers behind."
            }
        ]
    },

    # 4. DECIMALS
    "decimals": {
        "title": "Decimals",
        "slug": "decimals",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.6 • L2.4",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Decimal Arithmetic & Trailing Zeros",
            "points": [
                "Adding/Subtracting: Keep decimal points in a straight vertical line.",
                "Multiplying Decimals: (e.g. 0.3 × 0.04): 3 × 4 = 12. Total decimal places = 1 + 2 = 3. Answer = 0.012.",
                "Dividing by Decimals: Shift the decimal point in both divisor and dividend until the divisor is a whole number (e.g. 15 ÷ 0.5 = 150 ÷ 5 = 30).",
                "Money rule: Always write two decimal places for currency (£4.50, never £4.5)."
            ],
            "calc_tip": "When calculating fuel consumption or dosage, never round intermediate decimal values until the final step."
        },
        "workout_blocks": [
            {
                "title": "Addition & Subtraction of Decimals",
                "instruction": "Calculate accurately without a calculator:",
                "items": [
                    ("a", "14.6 + 8.75", "23.35"),
                    ("b", "120.4 + 45.68", "166.08"),
                    ("c", "0.85 + 0.475", "1.325"),
                    ("d", "25.0 - 13.65", "11.35"),
                    ("e", "4.2 - 1.875", "2.325"),
                    ("f", "100 - 45.32", "54.68"),
                    ("g", "8.95 + 12.4 + 0.65", "22.00"),
                    ("h", "50 - 18.72", "31.28")
                ]
            },
            {
                "title": "Multiplying & Dividing Decimals",
                "instruction": "Work out each calculation:",
                "items": [
                    ("a", "0.4 × 0.6", "0.24"),
                    ("b", "0.05 × 0.8", "0.04"),
                    ("c", "1.2 × 0.3", "0.36"),
                    ("d", "2.5 × 4", "10.0"),
                    ("e", "14.4 ÷ 1.2", "12"),
                    ("f", "8.4 ÷ 0.4", "21"),
                    ("g", "3.6 ÷ 0.06", "60"),
                    ("h", "45 ÷ 0.5", "90")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Healthcare Clinical Syringe Dosage",
                "stem": "A patient requires a medication dosage of <strong>0.35 ml per kilogram of body weight</strong>.<br>The patient weighs <strong>68 kg</strong>.<br>Each ampoule contains <strong>10 ml</strong> of medicine.<br>(a) Calculate the total dosage required in ml.<br>(b) How many complete ampoules are needed?",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Multiply dose by weight: 68 × 0.35 = 23.8 ml", "[M1]"),
                    ("Determine ampoules: 23.8 ÷ 10 = 2.38 ampoules", "[M1]"),
                    ("Round up to whole ampoules: 3 ampoules needed (providing 30 ml)", "[A1]")
                ],
                "final_answer": "(a) 23.8 ml | (b) 3 ampoules",
                "reverse_check": "2 ampoules only provide 20 ml (insufficient for 23.8 ml dose).",
                "pitfall": "Rounding down to 2 ampoules."
            }
        ]
    },

    # 5. DECIMAL BASICS
    "decimal-basics": {
        "title": "Decimal Basics: Tenths, Hundredths & Money",
        "slug": "decimal-basics",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: E3.6 • L1.6",
        "level": "Entry 3 & Level 1",
        "method_card": {
            "title": "Tenths, Hundredths & Place Value",
            "points": [
                "The first digit after the decimal point is the tenths column (0.1).",
                "The second digit after the decimal point is the hundredths column (0.01).",
                "In UK currency: £1 = 100 pence. 50p = £0.50, 5p = £0.05.",
                "To compare decimals: Add placeholder zeros so all numbers have the same number of decimal digits (e.g. 0.4 becomes 0.40, which is larger than 0.35)."
            ],
            "calc_tip": "Beware 5 pence! Never write £0.5 for 5p; £0.5 means 50 pence. 5p is £0.05."
        },
        "workout_blocks": [
            {
                "title": "Pence to Pounds Conversions",
                "instruction": "Convert each pence amount into pounds with £ sign:",
                "items": [
                    ("a", "65p", "£0.65"),
                    ("b", "8p", "£0.08"),
                    ("c", "125p", "£1.25"),
                    ("d", "240p", "£2.40"),
                    ("e", "450p", "£4.50"),
                    ("f", "5p", "£0.05"),
                    ("g", "1,200p", "£12.00"),
                    ("h", "305p", "£3.05")
                ]
            },
            {
                "title": "Ordering Decimals",
                "instruction": "Order from smallest to largest:",
                "items": [
                    ("a", "0.4, 0.25, 0.35", "0.25, 0.35, 0.4"),
                    ("b", "1.2, 1.15, 1.08", "1.08, 1.15, 1.2"),
                    ("c", "0.09, 0.9, 0.19", "0.09, 0.19, 0.9"),
                    ("d", "£3.40, £3.04, £3.44", "£3.04, £3.40, £3.44"),
                    ("e", "0.5, 0.05, 0.55", "0.05, 0.5, 0.55"),
                    ("f", "2.6, 2.58, 2.65", "2.58, 2.6, 2.65")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Hospital Cafeteria Cash Float",
                "stem": "A cafeteria till assistant counts coins in the till drawer:<br>• 25 coins of 10p<br>• 40 coins of 5p<br>• 15 coins of 20p<br>Calculate the total cash value in pounds (£).",
                "marks": 3,
                "prefix": "£",
                "steps": [
                    ("10p coins: 25 × 10p = 250p = £2.50", "[M1]"),
                    ("5p coins: 40 × 5p = 200p = £2.00; 20p coins: 15 × 20p = 300p = £3.00", "[M1]"),
                    ("Sum total: £2.50 + £2.00 + £3.00 = £7.50", "[A1]")
                ],
                "final_answer": "£7.50",
                "reverse_check": "£7.50 = 750p = 250p + 200p + 300p.",
                "pitfall": "Calculating 40 × 5p as £20 instead of £2.00."
            }
        ]
    },

    # 6. BIDMAS
    "bidmas": {
        "title": "BIDMAS / Order of Operations",
        "slug": "bidmas",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.5 • L2.2",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Order of Operations Priority Hierarchy",
            "points": [
                "B - Brackets first: Always calculate everything inside ( ) before doing anything else.",
                "I - Indices / Powers: Square numbers (3² = 9), cubes, and roots.",
                "DM - Division and Multiplication: Equal priority from left to right.",
                "AS - Addition and Subtraction: Equal priority from left to right.",
                "Golden Rule: Never simply calculate from left to right if operations have different priorities (e.g. 5 + 3 × 2 is 11, NOT 16!)."
            ],
            "calc_tip": "Scientific calculators follow BIDMAS automatically. Basic desktop four-function calculators do NOT, so calculate multiplication and division first."
        },
        "workout_blocks": [
            {
                "title": "Basic Two-Operation Priority Drills",
                "instruction": "Work out the value of each calculation:",
                "items": [
                    ("a", "6 + 4 × 3", "18"),
                    ("b", "10 - 2 × 4", "2"),
                    ("c", "20 ÷ 4 + 6", "11"),
                    ("d", "15 - 12 ÷ 3", "11"),
                    ("e", "8 × 5 - 12", "28"),
                    ("f", "30 + 10 ÷ 2", "35"),
                    ("g", "5 × 4 + 3 × 2", "26"),
                    ("h", "24 ÷ 6 + 18 ÷ 2", "13")
                ]
            },
            {
                "title": "Calculations with Brackets & Indices",
                "instruction": "Solve brackets first, then indices:",
                "items": [
                    ("a", "(5 + 3) × 4", "32"),
                    ("b", "(18 - 6) ÷ 3", "4"),
                    ("c", "4 × (12 - 5)", "28"),
                    ("d", "(20 - 4) ÷ (2 + 2)", "4"),
                    ("e", "3² + 4²", "25 (9 + 16)"),
                    ("f", "(3 + 4)²", "49 (7²)"),
                    ("g", "5 + 2³ × 2", "21 (5 + 8 × 2 = 5 + 16)"),
                    ("h", "100 - 3 × (4 + 2)²", "-8 (100 - 3 × 36 = 100 - 108)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Building Maintenance Contract",
                "stem": "A plumbing engineer uses this formula to calculate the total charge for a callout:<br><strong>Charge = Callout Fee + (Hourly Rate × Hours Worked) + Materials</strong><br>• Callout Fee = <strong>£45.00</strong><br>• Hourly Rate = <strong>£32.00</strong><br>• Hours Worked = <strong>4.5 hours</strong><br>• Materials = <strong>£88.50</strong><br>Evaluate the total charge.",
                "marks": 3,
                "prefix": "£",
                "steps": [
                    ("Calculate labour multiplication first: £32.00 × 4.5 = £144.00", "[M1]"),
                    ("Add all components: £45.00 + £144.00 + £88.50", "[M1]"),
                    ("Total Charge = £277.50", "[A1]")
                ],
                "final_answer": "£277.50",
                "reverse_check": "£277.50 - £88.50 - £45.00 = £144.00; £144 ÷ 4.5 = £32.00.",
                "pitfall": "Adding callout fee to hourly rate before multiplying by hours."
            }
        ]
    },

    # 7. RATIO
    "ratio": {
        "title": "Ratio",
        "slug": "ratio",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.11 • L2.13 • L2.14",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Ratio Rules & 3-Step Sharing Method",
            "points": [
                "Simplifying Ratios: Divide both sides by their highest common factor (HCF).",
                "Sharing an amount into a ratio (A : B):",
                "Step 1: Add parts together (Total Parts = A + B).",
                "Step 2: Divide total quantity by total parts to find value of 1 Part (Value of 1 Part = Total ÷ Parts).",
                "Step 3: Multiply the 1-part value by each ratio number to find individual shares.",
                "1 : n notation: Divide both sides by the first number so the left side equals 1."
            ],
            "calc_tip": "Always check your shares add up to the original total amount!"
        },
        "workout_blocks": [
            {
                "title": "Simplifying Ratios & 1 : n Format",
                "instruction": "Simplify each ratio to its simplest integer form:",
                "items": [
                    ("a", "12 : 18", "2 : 3"),
                    ("b", "20 : 35", "4 : 7"),
                    ("c", "16 : 24 : 32", "2 : 3 : 4"),
                    ("d", "45 : 60", "3 : 4"),
                    ("e", "250 ml : 1 litre (convert to ml)", "1 : 4 (250 : 1,000)"),
                    ("f", "50 cm : 2 metres (convert to cm)", "1 : 4 (50 : 200)"),
                    ("g", "Write 4 : 14 in the form 1 : n", "1 : 3.5"),
                    ("h", "Write 5 : 32 in the form 1 : n", "1 : 6.4")
                ]
            },
            {
                "title": "Sharing Quantities into Ratios",
                "instruction": "Share the given amount into the ratio:",
                "items": [
                    ("a", "Share £60 in the ratio 2 : 3", "£24 and £36 (5 parts = £12 each)"),
                    ("b", "Share £120 in the ratio 1 : 3", "£30 and £90 (4 parts = £30 each)"),
                    ("c", "Share 150 kg in the ratio 2 : 1", "100 kg and 50 kg (3 parts = 50 kg each)"),
                    ("d", "Share £350 in the ratio 4 : 3", "£200 and £150 (7 parts = £50 each)"),
                    ("e", "Share 400 litres in the ratio 3 : 5", "150 L and 250 L (8 parts = 50 L each)"),
                    ("f", "Share £900 in the ratio 2 : 3 : 4", "£200, £300, £400 (9 parts = £100 each)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Healthcare Clinical Disinfectant Dilution",
                "stem": "Infection control guidelines state that concentrated surgical disinfectant must be diluted with water in the ratio <strong>1 : 9</strong> (1 part disinfectant to 9 parts water).<br>A healthcare cleaner needs to prepare <strong>15 litres</strong> of diluted disinfectant solution.<br>How many litres of concentrated disinfectant and how many litres of water are needed?",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Total parts = 1 + 9 = 10 parts", "[M1]"),
                    ("Value of 1 part = 15 litres ÷ 10 = 1.5 litres", "[M1]"),
                    ("Disinfectant = 1 × 1.5 L = 1.5 litres; Water = 9 × 1.5 L = 13.5 litres", "[A1]")
                ],
                "final_answer": "1.5 litres disinfectant and 13.5 litres water",
                "reverse_check": "1.5 L + 13.5 L = 15.0 L; 13.5 ÷ 1.5 = 9 (Ratio 1 : 9 verified).",
                "pitfall": "Dividing 15 by 9 instead of the total number of parts (10)."
            }
        ]
    },

    # 8. ROUNDING & ESTIMATING
    "rounding-and-estimating": {
        "title": "Rounding & Estimating",
        "slug": "rounding-and-estimating",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.7 • L2.3",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Rounding Rules & Pre-Check Estimation",
            "points": [
                "Rounding Rule: Look at the deciding digit immediately to the right. If it is 5 or more, round up (+1); if 4 or less, round down (leave digit unchanged).",
                "Nearest 10: Deciding digit is units column.",
                "Nearest 100: Deciding digit is tens column.",
                "Decimal Places (d.p.): Count digits after the decimal point.",
                "Significant Figures (s.f.): First significant figure is the first non-zero digit reading left to right.",
                "Estimating calculations: Round every number to 1 significant figure BEFORE calculating."
            ],
            "calc_tip": "In Functional Skills exam questions that ask 'Estimate the total by rounding...', you MUST show your rounded numbers. Calculating the exact answer scores 0 marks!"
        },
        "workout_blocks": [
            {
                "title": "Rounding to Nearest 10, 100 & 1,000",
                "instruction": "Round each number as specified:",
                "items": [
                    ("a", "Round 47 to the nearest 10", "50"),
                    ("b", "Round 184 to the nearest 10", "180"),
                    ("c", "Round 365 to the nearest 100", "400"),
                    ("d", "Round 1,438 to the nearest 100", "1,400"),
                    ("e", "Round 7,850 to the nearest 1,000", "8,000"),
                    ("f", "Round 14,290 to the nearest 1,000", "14,000"),
                    ("g", "Round £45.68 to the nearest pound (£)", "£46.00"),
                    ("h", "Round £129.40 to the nearest ten pounds", "£130.00")
                ]
            },
            {
                "title": "Rounding to Decimal Places (d.p.) and Significant Figures (s.f.)",
                "instruction": "Round each number to the indicated precision:",
                "items": [
                    ("a", "Round 4.738 to 1 decimal place", "4.7"),
                    ("b", "Round 12.865 to 2 decimal places", "12.87"),
                    ("c", "Round 0.0482 to 2 decimal places", "0.05"),
                    ("d", "Round 3.14159 to 2 decimal places", "3.14"),
                    ("e", "Round 48,200 to 1 significant figure", "50,000"),
                    ("f", "Round 3,485 to 2 significant figures", "3,500"),
                    ("g", "Round 0.00482 to 1 significant figure", "0.005"),
                    ("h", "Round 0.0763 to 2 significant figures", "0.076")
                ]
            },
            {
                "title": "Exam Estimation Drills (1 Significant Figure)",
                "instruction": "Estimate each answer by rounding every number to 1 significant figure:",
                "items": [
                    ("a", "Estimate: 49 × 21", "50 × 20 = 1,000"),
                    ("b", "Estimate: 395 × 18", "400 × 20 = 8,000"),
                    ("c", "Estimate: 785 ÷ 38", "800 ÷ 40 = 20"),
                    ("d", "Estimate: 19.8 × 4.2", "20 × 4 = 80"),
                    ("e", "Estimate: (48.5 + 31.2) ÷ 19.4", "(50 + 30) ÷ 20 = 80 ÷ 20 = 4"),
                    ("f", "Estimate: 512 × 0.48", "500 × 0.5 = 250")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Healthcare Procurement Order Estimation",
                "stem": "A procurement manager orders <strong>38 digital blood pressure monitors</strong> at <strong>£48.75 each</strong>.<br>(a) Use estimation (by rounding each number to 1 significant figure) to calculate an approximate total cost.<br>(b) The supplier sends an invoice for <strong>£2,450.00</strong>. Is this invoice reasonable based on your estimate?",
                "marks": 3,
                "prefix": "£",
                "steps": [
                    ("Round 38 to 1 s.f. = 40; Round £48.75 to 1 s.f. = £50", "[M1]"),
                    ("Estimate calculation: 40 × £50 = £2,000", "[M1]"),
                    ("Conclusion: No, the invoice for £2,450 is significantly too high (overcharged by ~£600; actual cost is 38 × £48.75 = £1,852.50).", "[A1]")
                ],
                "final_answer": "(a) Estimate = £2,000 | (b) No, £2,450 is unreasonable (much higher than estimate)",
                "reverse_check": "Exact = £1,852.50, which is close to the £2,000 estimate, confirming £2,450 is incorrect.",
                "pitfall": "Calculating the exact value (£1,852.50) instead of showing the 1 s.f. rounded values (40 × £50)."
            }
        ]
    },

    # 9. MONEY, INVOICING & PAYROLL
    "money-invoicing-payroll": {
        "title": "Money, Invoicing & Payroll",
        "slug": "money-invoicing-payroll",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.8 • L2.6",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Gross Pay, Net Pay, Deductions & Invoices",
            "points": [
                "Gross Pay: Total money earned BEFORE any deductions (Hours × Hourly Rate).",
                "Deductions: Income Tax, National Insurance (NI), Pension contributions, student loan.",
                "Net Pay ('Take-home pay'): Net Pay = Gross Pay - Total Deductions.",
                "Overtime Rates: 'Time-and-a-half' = Hourly Rate × 1.5; 'Double time' = Hourly Rate × 2.",
                "Invoice Totals: Subtotal + VAT (20%) - Discount = Grand Total Payable."
            ],
            "calc_tip": "When calculating weekly pay with 30-minute shifts, convert minutes to decimal hours (30 mins = 0.5 hours, 45 mins = 0.75 hours, 15 mins = 0.25 hours)."
        },
        "workout_blocks": [
            {
                "title": "Time to Decimal Hours Conversion",
                "instruction": "Convert the working hours and minutes to decimal hours:",
                "items": [
                    ("a", "7 hours 30 minutes", "7.5 hours"),
                    ("b", "8 hours 15 minutes", "8.25 hours"),
                    ("c", "6 hours 45 minutes", "6.75 hours"),
                    ("d", "37 hours 30 minutes", "37.5 hours"),
                    ("e", "4 hours 20 minutes (20 ÷ 60)", "4.33 hours (4 1/3)"),
                    ("f", "30 minutes", "0.5 hours")
                ]
            },
            {
                "title": "Gross Wages & Overtime Multipliers",
                "instruction": "Calculate the gross pay for each employee:",
                "items": [
                    ("a", "35 hours at £11.44 per hour (National Living Wage)", "£400.40"),
                    ("b", "40 hours at £12.50 per hour", "£500.00"),
                    ("c", "37.5 hours at £14.00 per hour", "£525.00"),
                    ("d", "8 hours overtime at time-and-a-half (standard rate £12.00)", "£144.00 (8 × £18.00)"),
                    ("e", "5 hours overtime at double time (standard rate £15.00)", "£150.00 (5 × £30.00)"),
                    ("f", "Gross pay: £620.00. Tax = £74.00, NI = £42.00. Net pay?", "£504.00")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Apprentice Monthly Payslip Audit",
                "stem": "A dental nursing apprentice reviews her monthly payslip:<br>• Basic Salary: <strong>£1,650.00</strong><br>• Saturday Weekend Enhancement: <strong>£180.00</strong><br>• Income Tax Deduction: <strong>£142.50</strong><br>• National Insurance Deduction: <strong>£88.20</strong><br>• Workplace Pension Contribution: <strong>5% of Basic Salary</strong><br>Calculate the apprentice's <strong>Net Pay</strong> for the month.",
                "marks": 3,
                "prefix": "£",
                "steps": [
                    ("Calculate Gross Pay = £1,650.00 + £180.00 = £1,830.00", "[M1]"),
                    ("Calculate Pension = 5% of £1,650.00 = 1,650 × 0.05 = £82.50", "[M1]"),
                    ("Total Deductions = £142.50 (Tax) + £88.20 (NI) + £82.50 (Pension) = £313.20. Net Pay = £1,830.00 - £313.20 = £1,516.80", "[A1]")
                ],
                "final_answer": "£1,516.80",
                "reverse_check": "£1,516.80 Net + £313.20 Deductions = £1,830.00 Gross.",
                "pitfall": "Calculating 5% pension on the enhanced total rather than basic salary."
            }
        ]
    },

    # 10. ALGEBRA
    "algebra": {
        "title": "Algebra, Formulas & Substitution",
        "slug": "algebra",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.9 • L2.7 • L2.8",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Algebraic Notation & Formula Substitution",
            "points": [
                "Numbers next to letters mean multiply: 4y means 4 × y; 2ab means 2 × a × b.",
                "Fractions mean divide: x / 3 means x ÷ 3.",
                "Powers apply only to the base: 3x² means 3 × (x²), NOT (3x)².",
                "Negative substitution: Be cautious with negative numbers: if y = -3, then y² = (-3) × (-3) = +9.",
                "Solving Linear Equations: Use inverse operations in reverse order (balance method)."
            ],
            "calc_tip": "When substituting into formulas on a calculator, always put negative values inside brackets, e.g. (-4)² = 16."
        },
        "workout_blocks": [
            {
                "title": "Substituting into Expressions",
                "instruction": "Find the value when a = 4, b = 5, and c = -2:",
                "items": [
                    ("a", "2a + 3b", "23 (2×4 + 3×5 = 8 + 15)"),
                    ("b", "4a - b", "11 (16 - 5)"),
                    ("c", "ab - c", "22 (20 - (-2) = 20 + 2)"),
                    ("d", "a² + b²", "41 (16 + 25)"),
                    ("e", "3c²", "12 (3 × 4)"),
                    ("f", "2(a + b)", "18 (2 × 9)"),
                    ("g", "5a + 4c", "12 (20 + (-8))"),
                    ("h", "(b - c) ÷ 7", "1 (7 ÷ 7)")
                ]
            },
            {
                "title": "Solving One-Step & Two-Step Equations",
                "instruction": "Solve for x showing inverse operations:",
                "items": [
                    ("a", "x + 7 = 19", "x = 12"),
                    ("b", "x - 8 = 15", "x = 23"),
                    ("c", "4x = 36", "x = 9"),
                    ("d", "x ÷ 5 = 7", "x = 35"),
                    ("e", "2x + 5 = 21", "x = 8 (2x = 16)"),
                    ("f", "3x - 4 = 23", "x = 9 (3x = 27)"),
                    ("g", "5x + 12 = 47", "x = 7 (5x = 35)"),
                    ("h", "4(x - 2) = 24", "x = 8 (x - 2 = 6)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Healthcare Clinical Body Mass Index (BMI)",
                "stem": "A clinical nurse calculates a patient's Body Mass Index (BMI) using this formula:<br><strong>BMI = Weight ÷ Height²</strong><br>Where Weight is in kilograms (kg) and Height is in metres (m).<br>• Patient weight = <strong>78 kg</strong><br>• Patient height = <strong>1.75 m</strong><br>(a) Calculate the patient's BMI to 1 decimal place.<br>(b) Healthy BMI is between 18.5 and 24.9. Is the patient within the healthy range?",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Calculate Height² = 1.75 × 1.75 = 3.0625", "[M1]"),
                    ("Calculate BMI = 78 ÷ 3.0625 = 25.469...", "[M1]"),
                    ("Round to 1 d.p. = 25.5. Conclusion: No, 25.5 is slightly above the healthy upper limit (24.9).", "[A1]")
                ],
                "final_answer": "(a) BMI = 25.5 | (b) No, 25.5 is slightly overweight (above 24.9)",
                "reverse_check": "25.5 × 1.75² = 25.5 × 3.0625 ≈ 78.1 kg.",
                "pitfall": "Dividing weight by height first and then squaring the result."
            }
        ]
    }
}
