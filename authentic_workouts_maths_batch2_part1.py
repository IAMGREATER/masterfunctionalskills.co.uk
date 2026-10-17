#!/usr/bin/env python3
"""
Authentic Fluency Workouts: Maths Batch 2 (Part 1 - Number, Money, FDP & Algebra)
13 Curriculum Topics:
1. numbers-and-place-value
2. ordering-numbers
3. division
4. fractions-decimals-and-percentages
5. fdp-conversions
6. fraction-basics
7. number-basics
8. number-patterns
9. money
10. problems-involving-money
11. best-buys
12. interest-and-compound-interest
13. formulas
"""

MATHS_BATCH2_PART1_WORKOUTS = {
    # 1. NUMBERS AND PLACE VALUE
    "numbers-and-place-value": {
        "title": "Numbers & Place Value",
        "slug": "numbers-and-place-value",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.1 • L1.2 • L2.1",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Place Value Hierarchy & Column Worth",
            "points": [
                "Each column is worth 10 times the column to its right: Millions (M), Hundred Thousands (HTh), Ten Thousands (TTh), Thousands (Th), Hundreds (H), Tens (T), Units (U).",
                "Decimal place columns to the right of the decimal point: Tenths (0.1), Hundredths (0.01), Thousandths (0.001).",
                "When multiplying by 10, 100, 1000, digits move left; when dividing, digits move right.",
                "Zero acts as a critical placeholder (e.g. four thousand and six is 4,006, not 46).",
                "To state the value of a digit, write the column value (e.g. in 54,821 the 4 represents 4,000 or four thousands)."
            ],
            "calc_tip": "Do not enter commas when typing large numbers into a calculator (enter 45200, not 45,200)."
        },
        "workout_blocks": [
            {
                "title": "Identifying Digit Values",
                "instruction": "State the value of the underlined digit in words or numbers:",
                "items": [
                    ("a", "In <strong>5<u>4</u>,821</strong>, what is the value of the 4?", "4,000 (four thousands)"),
                    ("b", "In <strong><u>3</u>82,910</strong>, what is the value of the 3?", "300,000 (three hundred thousands)"),
                    ("c", "In <strong>1,<u>7</u>04,500</strong>, what is the value of the 7?", "700,000 (seven hundred thousands)"),
                    ("d", "In <strong>42.<u>8</u>5</strong>, what is the value of the 8?", "0.8 or 8 tenths (8/10)"),
                    ("e", "In <strong>6.3<u>7</u>2</strong>, what is the value of the 7?", "0.07 or 7 hundredths (7/100)"),
                    ("f", "In <strong>10.0<u>4</u>8</strong>, what is the value of the 4?", "0.04 or 4 hundredths (4/100)")
                ]
            },
            {
                "title": "Writing Numbers in Figures and Words",
                "instruction": "Convert between word form and figures:",
                "items": [
                    ("a", "Write in figures: Thirty-six thousand, four hundred and eight", "36,408"),
                    ("b", "Write in figures: One hundred and five thousand, two hundred", "105,200"),
                    ("c", "Write in figures: One million, forty thousand and seventy", "1,040,070"),
                    ("d", "Write in words: 24,015", "Twenty-four thousand and fifteen"),
                    ("e", "Write in words: 508,300", "Five hundred and eight thousand, three hundred"),
                    ("f", "Write in figures: Seven tenths and four hundredths as a decimal", "0.74")
                ]
            },
            {
                "title": "Multiplying and Dividing by 10, 100 and 1,000",
                "instruction": "Shift digits left or right using place value rules:",
                "items": [
                    ("a", "48 × 100", "4,800"),
                    ("b", "3.6 × 10", "36"),
                    ("c", "0.45 × 1,000", "450"),
                    ("d", "7,200 ÷ 100", "72"),
                    ("e", "350 ÷ 1,000", "0.35"),
                    ("f", "4.8 ÷ 10", "0.48")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Medical Diagnostics Record Keeping",
                "stem": "A medical diagnostics laboratory processed <strong>three hundred and forty-two thousand, and seventy-five</strong> blood sample vials in one calendar year.<br>The laboratory supervisor records this total in an electronic audit register.<br>(a) Write this number in figures.<br>(b) In the following year, the total number of processed vials was <strong>352,000</strong>. Work out how many more samples were processed in the second year.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Convert words to digits: 342,075", "[M1]"),
                    ("Subtract baseline year from second year: 352,000 - 342,075", "[M1]"),
                    ("Accurate difference: 9,925 vials", "[A1]")
                ],
                "final_answer": "(a) 342,075 | (b) 9,925 more samples",
                "reverse_check": "342,075 + 9,925 = 352,000 vials.",
                "pitfall": "Omitting the zero placeholder in the hundreds column (e.g. writing 342,75)."
            }
        ]
    },

    # 2. ORDERING NUMBERS
    "ordering-numbers": {
        "title": "Ordering Numbers",
        "slug": "ordering-numbers",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: E3.1 • L1.1 • L2.1",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Ordering Whole Numbers, Decimals & Negatives",
            "points": [
                "Ascending order means smallest to largest (increasing); Descending order means largest to smallest (decreasing).",
                "To order decimals, align decimal points and add trailing zeros so all numbers have the same number of decimal places (e.g. compare 0.400, 0.045, 0.450).",
                "Negative numbers: The larger the digit following the minus sign, the smaller the actual value (e.g. -8°C is colder than -2°C).",
                "Inequality symbols: '<' means strictly less than; '>' means strictly greater than. The wide opening always faces the larger number."
            ],
            "calc_tip": "Pad decimal numbers with zeros on paper before entering them into any calculation."
        },
        "workout_blocks": [
            {
                "title": "Ordering Large Whole Numbers",
                "instruction": "Write each set of numbers in ascending order (smallest first):",
                "items": [
                    ("a", "4,502; 4,205; 4,520; 4,025", "4,025; 4,205; 4,502; 4,520"),
                    ("b", "12,450; 12,045; 12,504; 12,405", "12,045; 12,405; 12,450; 12,504"),
                    ("c", "89,000; 98,000; 80,900; 90,800", "80,900; 89,000; 90,800; 98,000"),
                    ("d", "305,400; 350,040; 304,500; 354,000", "304,500; 305,400; 350,040; 354,000")
                ]
            },
            {
                "title": "Ordering Decimals",
                "instruction": "Write each set of decimal numbers in ascending order (smallest first):",
                "items": [
                    ("a", "0.45, 0.405, 0.5, 0.054", "0.054, 0.405, 0.45, 0.5"),
                    ("b", "3.2, 3.02, 3.25, 3.19", "3.02, 3.19, 3.2, 3.25"),
                    ("c", "0.08, 0.8, 0.088, 0.808", "0.08, 0.088, 0.8, 0.808"),
                    ("d", "14.6, 14.58, 14.605, 14.09", "14.09, 14.58, 14.6, 14.605")
                ]
            },
            {
                "title": "Negative Numbers & Temperatures",
                "instruction": "Order from coldest to warmest (smallest to largest):",
                "items": [
                    ("a", "-4°C, 2°C, -7°C, 0°C, 5°C", "-7°C, -4°C, 0°C, 2°C, 5°C"),
                    ("b", "-12°C, -3°C, -15°C, -8°C", "-15°C, -12°C, -8°C, -3°C"),
                    ("c", "-1.5°C, -0.8°C, -2.1°C, 0.4°C", "-2.1°C, -1.5°C, -0.8°C, 0.4°C"),
                    ("d", "Insert < or > : -6 ___ -2", "-6 < -2")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Pharmacy Cold-Chain Monitoring",
                "stem": "A clinical dispensary records overnight temperature readings in four biomedical vaccine freezers:<br>Freezer A: <strong>-18.4°C</strong><br>Freezer B: <strong>-19.1°C</strong><br>Freezer C: <strong>-17.8°C</strong><br>Freezer D: <strong>-18.9°C</strong><br>(a) List the freezers in order of temperature, starting from the <strong>coldest</strong>.<br>(b) Work out the difference in temperature between the coldest and warmest freezer.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Identify coldest to warmest by greatest negative value: Freezer B (-19.1°C), Freezer D (-18.9°C), Freezer A (-18.4°C), Freezer C (-17.8°C)", "[M1]"),
                    ("Calculate difference between coldest (-19.1°C) and warmest (-17.8°C): -17.8 - (-19.1) = 1.3°C", "[M1]"),
                    ("State clear final answer with unit", "[A1]")
                ],
                "final_answer": "(a) B, D, A, C | (b) 1.3°C difference",
                "reverse_check": "-19.1 + 1.3 = -17.8°C.",
                "pitfall": "Confusing greater absolute magnitude with warmer temperature (thinking -17.8°C is colder than -19.1°C)."
            }
        ]
    },

    # 3. DIVISION
    "division": {
        "title": "Division & Remainders",
        "slug": "division",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: E3.4 • L1.5 • L2.4",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Short Bus-Stop Division & Handling Remainders",
            "points": [
                "Short division (bus-stop method): divide each digit from left to right, carrying any remainder into the next column.",
                "Express remainders according to context: as a whole remainder (r), as a fraction, as a decimal, or rounded up/down for real-world constraints.",
                "Contextual rounding: When packing boxes, coaches, or pallets, always round UP to ensure everyone/everything fits (e.g. 145 people on 40-seat coaches = 3.625 → 4 coaches).",
                "When calculating complete portions or full packs, round DOWN (e.g. 100 eggs in 6-egg boxes = 16 full boxes)."
            ],
            "calc_tip": "To convert a calculator decimal remainder back to whole items: multiply the decimal part by the divisor."
        },
        "workout_blocks": [
            {
                "title": "Short Division (Exact Whole Numbers)",
                "instruction": "Work out the exact quotient without a calculator:",
                "items": [
                    ("a", "84 ÷ 4", "21"),
                    ("b", "135 ÷ 5", "27"),
                    ("c", "248 ÷ 8", "31"),
                    ("d", "462 ÷ 6", "77"),
                    ("e", "756 ÷ 9", "84"),
                    ("f", "1,248 ÷ 4", "312")
                ]
            },
            {
                "title": "Division with Decimal Quotients",
                "instruction": "Continue dividing past the decimal point:",
                "items": [
                    ("a", "75 ÷ 2", "37.5"),
                    ("b", "93 ÷ 4", "23.25"),
                    ("c", "148 ÷ 5", "29.6"),
                    ("d", "315 ÷ 6", "52.5"),
                    ("e", "£54 ÷ 4", "£13.50"),
                    ("f", "£125 ÷ 8", "£15.625 → £15.63")
                ]
            },
            {
                "title": "Practical Rounding Up or Down",
                "instruction": "Decide whether to round up or down based on context:",
                "items": [
                    ("a", "140 delegates attend a conference. Each table seats 8. Tables required?", "18 tables (140 ÷ 8 = 17.5 → round UP)"),
                    ("b", "250 cupcakes made. Boxes hold 6 cupcakes. How many full boxes?", "41 full boxes (250 ÷ 6 = 41 r4 → round DOWN)"),
                    ("c", "75 metres of cable. Cut into 8-metre pieces. How many complete pieces?", "9 complete pieces (75 ÷ 8 = 9 r3)"),
                    ("d", "210 students travel by minibus. Each bus holds 16. Minibuses needed?", "14 minibuses (210 ÷ 16 = 13.125 → round UP)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Care Home Transport Logistics",
                "stem": "A community care group organises an excursion for <strong>86 residents and support carers</strong>.<br>The group hires accessible minibuses with <strong>14 passenger seats</strong> each.<br>The hire cost for one minibus is <strong>£165 per day</strong>.<br>(a) How many minibuses must be hired so that all 86 people can travel?<br>(b) Work out the total hire cost for the day.",
                "marks": 3,
                "prefix": "£",
                "steps": [
                    ("Divide total passengers by bus capacity: 86 ÷ 14 = 6.142...", "[M1]"),
                    ("Apply real-world constraint: Round up to 7 minibuses", "[M1]"),
                    ("Calculate total cost: 7 × £165 = £1,155", "[A1]")
                ],
                "final_answer": "7 minibuses costing £1,155.00",
                "reverse_check": "7 × 14 = 98 seats (sufficient for 86 people with 12 spare seats).",
                "pitfall": "Rounding down to 6 minibuses, leaving 2 passengers behind."
            }
        ]
    },

    # 4. FRACTIONS, DECIMALS AND PERCENTAGES (FDP)
    "fractions-decimals-and-percentages": {
        "title": "Fractions, Decimals & Percentages Equivalences",
        "slug": "fractions-decimals-and-percentages",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.12 • L2.13",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Master FDP Conversion Rules",
            "points": [
                "Fraction to Decimal: Divide the numerator by the denominator (e.g. 3/8 = 3 ÷ 8 = 0.375).",
                "Decimal to Percentage: Multiply by 100 and add '%' (e.g. 0.375 × 100 = 37.5%).",
                "Percentage to Decimal: Divide by 100 (e.g. 45% = 45 ÷ 100 = 0.45).",
                "Percentage to Fraction: Place over 100 and simplify (e.g. 45% = 45/100 = 9/20).",
                "To compare values in different formats, convert all numbers to decimals or percentages first."
            ],
            "calc_tip": "Type the numerator, press divide, then the denominator to immediately obtain the decimal equivalence."
        },
        "workout_blocks": [
            {
                "title": "Fraction to Decimal and Percentage Conversions",
                "instruction": "Convert each fraction to an equivalent decimal and percentage:",
                "items": [
                    ("a", "1/2 as a decimal and percentage", "0.5 and 50%"),
                    ("b", "1/4 as a decimal and percentage", "0.25 and 25%"),
                    ("c", "3/4 as a decimal and percentage", "0.75 and 75%"),
                    ("d", "1/5 as a decimal and percentage", "0.2 and 20%"),
                    ("e", "2/5 as a decimal and percentage", "0.4 and 40%"),
                    ("f", "1/10 as a decimal and percentage", "0.1 and 10%"),
                    ("g", "3/10 as a decimal and percentage", "0.3 and 30%"),
                    ("h", "1/8 as a decimal and percentage", "0.125 and 12.5%")
                ]
            },
            {
                "title": "Percentage to Simplified Fraction",
                "instruction": "Write each percentage as a fraction in its simplest form:",
                "items": [
                    ("a", "50% as a fraction", "1/2"),
                    ("b", "25% as a fraction", "1/4"),
                    ("c", "75% as a fraction", "3/4"),
                    ("d", "20% as a fraction", "1/5"),
                    ("e", "40% as a fraction", "2/5"),
                    ("f", "60% as a fraction", "3/5"),
                    ("g", "80% as a fraction", "4/5"),
                    ("h", "15% as a fraction", "3/20 (15/100)")
                ]
            },
            {
                "title": "Comparing Mixed Formats",
                "instruction": "Compare and state the largest value:",
                "items": [
                    ("a", "Which is larger: 3/5 or 65%?", "65% (3/5 = 60%)"),
                    ("b", "Which is larger: 0.28 or 1/4?", "0.28 (1/4 = 0.25)"),
                    ("c", "Which is larger: 7/10 or 68%?", "7/10 (7/10 = 70%)"),
                    ("d", "Which is larger: 0.35 or 3/8?", "3/8 (3/8 = 0.375)"),
                    ("e", "Order ascending: 0.4, 35%, 1/2", "35% (0.35), 0.4 (0.40), 1/2 (0.50)"),
                    ("f", "Order ascending: 3/4, 0.72, 78%", "0.72, 3/4 (0.75), 78% (0.78)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Commercial Sales Performance Audit",
                "stem": "Three regional branch managers report their quarterly sales growth against target:<br>• Northern Branch achieved <strong>3/8</strong> above target<br>• Central Branch achieved <strong>36%</strong> above target<br>• Southern Branch achieved <strong>0.385</strong> above target<br>Determine which branch achieved the greatest growth above target. You must show conversions to support your answer.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Convert Northern Branch to decimal: 3 ÷ 8 = 0.375 (or 37.5%)", "[M1]"),
                    ("Convert Central Branch to decimal: 36% = 0.360 (or 36%)", "[M1]"),
                    ("Compare all three decimals: 0.385 > 0.375 > 0.360 and state branch", "[A1]")
                ],
                "final_answer": "Southern Branch (0.385 / 38.5% is the greatest)",
                "reverse_check": "0.385 (38.5%) > 0.375 (37.5%) > 0.36 (36%).",
                "pitfall": "Comparing numerators directly without converting to a common format."
            }
        ]
    },

    # 5. FDP CONVERSIONS (Specific Drill Booklet)
    "fdp-conversions": {
        "title": "FDP Conversions & Benchmark Drills",
        "slug": "fdp-conversions",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.10 • L1.14 • L2.10 • L2.11",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Key Benchmarks & Conversion Strategies",
            "points": [
                "Common thirds: 1/3 ≈ 0.333 (33.3%), 2/3 ≈ 0.667 (66.7%).",
                "Common eighths: 1/8 = 0.125 (12.5%), 3/8 = 0.375 (37.5%), 5/8 = 0.625 (62.5%), 7/8 = 0.875 (87.5%).",
                "To express one quantity as a fraction of another: write Part / Whole, then convert to percentage by multiplying by 100.",
                "Always simplify fractions by finding the highest common factor (HCF)."
            ],
            "calc_tip": "To convert a recurring decimal like 0.333333 on a calculator, press the fraction key [a b/c] or [S-D] to reveal 1/3."
        },
        "workout_blocks": [
            {
                "title": "Core Eighths and Twentieths Fluency",
                "instruction": "Calculate the exact decimal and percentage values:",
                "items": [
                    ("a", "3/8 as a decimal", "0.375"),
                    ("b", "5/8 as a percentage", "62.5%"),
                    ("c", "7/8 as a decimal", "0.875"),
                    ("d", "7/20 as a percentage", "35% (7 × 5 / 100)"),
                    ("e", "9/20 as a percentage", "45%"),
                    ("f", "13/20 as a decimal", "0.65")
                ]
            },
            {
                "title": "Expressing as a Percentage of a Total",
                "instruction": "Write the first quantity as a percentage of the second:",
                "items": [
                    ("a", "18 out of 20 marks", "90%"),
                    ("b", "12 out of 50 attendees", "24%"),
                    ("c", "9 out of 25 staff members", "36%"),
                    ("d", "35 out of 70 patients", "50%"),
                    ("e", "42 out of 60 orders", "70%"),
                    ("f", "15 out of 120 components", "12.5%")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Workplace Quality Compliance Audit",
                "stem": "An electronics manufacturing assembly line tests <strong>160 circuit boards</strong>.<br>Technicians record that <strong>28 boards</strong> required minor soldering rework.<br>The plant manager states that less than <strong>18%</strong> of tested boards required rework.<br>Is the manager correct? You must show your calculation as a percentage.",
                "marks": 3,
                "prefix": "%",
                "steps": [
                    ("Formulate fraction of reworked boards: 28 ÷ 160", "[M1]"),
                    ("Convert to percentage: 28 ÷ 160 = 0.175 × 100 = 17.5%", "[M1]"),
                    ("Compare with manager's threshold: 17.5% < 18%, confirm statement is correct", "[A1]")
                ],
                "final_answer": "Yes, correct (17.5% is less than 18%)",
                "reverse_check": "160 × 0.175 = 28 boards.",
                "pitfall": "Calculating 160 ÷ 28 instead of Part ÷ Whole."
            }
        ]
    },

    # 6. FRACTION BASICS
    "fraction-basics": {
        "title": "Fraction Basics: Halves, Quarters & Thirds",
        "slug": "fraction-basics",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: E3.5 • L1.8 • L1.9",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Numerator, Denominator & Visual Fractions",
            "points": [
                "Denominator (bottom number): The total number of equal parts the whole is divided into.",
                "Numerator (top number): The number of parts selected or shaded.",
                "Equivalent fractions: Multiply or divide both numerator and denominator by the SAME number.",
                "Unit fractions (1/2, 1/3, 1/4, 1/5): Divide the amount by the denominator.",
                "Non-unit fractions (e.g. 3/4): Divide by the denominator, then multiply by the numerator."
            ],
            "calc_tip": "Remember: 'Divide by the bottom, times by the top!'"
        },
        "workout_blocks": [
            {
                "title": "Simplifying Fractions",
                "instruction": "Divide numerator and denominator by their highest common factor:",
                "items": [
                    ("a", "4/8 in simplest form", "1/2"),
                    ("b", "6/9 in simplest form", "2/3"),
                    ("c", "10/15 in simplest form", "2/3"),
                    ("d", "12/16 in simplest form", "3/4"),
                    ("e", "15/20 in simplest form", "3/4"),
                    ("f", "8/24 in simplest form", "1/3"),
                    ("g", "14/21 in simplest form", "2/3"),
                    ("h", "25/100 in simplest form", "1/4")
                ]
            },
            {
                "title": "Fractions of Quantities (Unit & Non-Unit)",
                "instruction": "Calculate the fraction of each amount:",
                "items": [
                    ("a", "1/2 of £48", "£24.00"),
                    ("b", "1/4 of 36 kg", "9 kg"),
                    ("c", "3/4 of 40 metres", "30 m"),
                    ("d", "1/3 of 27 hours", "9 hours"),
                    ("e", "2/3 of 60 litres", "40 litres"),
                    ("f", "1/5 of £85", "£17.00"),
                    ("g", "3/5 of 50 mm", "30 mm"),
                    ("h", "2/5 of 120 staff", "48 staff")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Commercial Catering Recipe Scaling",
                "stem": "A catering supervisor prepares a large batch of fruit punch requiring <strong>36 litres</strong> of liquid ingredients.<br>The recipe specifies that <strong>3/4</strong> of the total volume is chilled sparkling water, and the remaining <strong>1/4</strong> is pure fruit concentrate.<br>Work out the volume of sparkling water and fruit concentrate required.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Calculate 1/4 of total volume: 36 ÷ 4 = 9 litres", "[M1]"),
                    ("Calculate 3/4 for sparkling water: 9 × 3 = 27 litres", "[M1]"),
                    ("Confirm remaining volume for fruit concentrate: 9 litres", "[A1]")
                ],
                "final_answer": "27 litres sparkling water and 9 litres fruit concentrate",
                "reverse_check": "27 + 9 = 36 litres.",
                "pitfall": "Dividing by 3 instead of dividing by the denominator 4."
            }
        ]
    },

    # 7. NUMBER BASICS
    "number-basics": {
        "title": "Number Basics: Place Value & Counting",
        "slug": "number-basics",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: E3.1 • E3.2 • L1.1",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Odd, Even, Multiples & Factors",
            "points": [
                "Even numbers end in 0, 2, 4, 6, or 8; Odd numbers end in 1, 3, 5, 7, or 9.",
                "Multiples are numbers in a given times table (e.g. multiples of 6: 6, 12, 18, 24...).",
                "Factors are whole numbers that divide exactly into a number without a remainder (e.g. factors of 12: 1, 2, 3, 4, 6, 12).",
                "Prime numbers have EXACTLY two factors: 1 and itself (2, 3, 5, 7, 11, 13, 17, 19...). 1 is NOT a prime number."
            ],
            "calc_tip": "To find all factors of a number, list them systematically in pairs starting with 1 × N."
        },
        "workout_blocks": [
            {
                "title": "Factors and Multiples",
                "instruction": "Identify factors and multiples:",
                "items": [
                    ("a", "List all factors of 20", "1, 2, 4, 5, 10, 20"),
                    ("b", "List all factors of 24", "1, 2, 3, 4, 6, 8, 12, 24"),
                    ("c", "List all factors of 36", "1, 2, 3, 4, 6, 9, 12, 18, 36"),
                    ("d", "Write the first five multiples of 7", "7, 14, 21, 28, 35"),
                    ("e", "Write the first five multiples of 8", "8, 16, 24, 32, 40"),
                    ("f", "Which of these is a prime number: 9, 15, 19, 21?", "19")
                ]
            },
            {
                "title": "Squares, Square Roots & Cubes",
                "instruction": "Evaluate the power or root:",
                "items": [
                    ("a", "4² (4 squared)", "16"),
                    ("b", "7² (7 squared)", "49"),
                    ("c", "10² (10 squared)", "100"),
                    ("d", "12² (12 squared)", "144"),
                    ("e", "√64 (square root of 64)", "8"),
                    ("f", "√121 (square root of 121)", "11"),
                    ("g", "2³ (2 cubed = 2 × 2 × 2)", "8"),
                    ("h", "5³ (5 cubed = 5 × 5 × 5)", "125")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Estates Maintenance Paving Layout",
                "stem": "A facilities supervisor arranges square paving slabs around a square courtyard.<br>The total area of the courtyard floor is <strong>144 m²</strong>.<br>Each square paving slab measures <strong>1 metre by 1 metre</strong>.<br>(a) What is the length of one side of the courtyard in metres?<br>(b) How many 1-metre slabs are needed to create a single border along one side?",
                "marks": 3,
                "prefix": "m",
                "steps": [
                    ("Calculate square root of area: √144 = 12 metres", "[M1]"),
                    ("Side length equals 12 metres", "[A1]"),
                    ("State slabs required along one side: 12 slabs", "[A1]")
                ],
                "final_answer": "12 metres (12 slabs per side)",
                "reverse_check": "12 × 12 = 144 m².",
                "pitfall": "Dividing 144 by 4 instead of taking the square root."
            }
        ]
    },

    # 8. NUMBER PATTERNS
    "number-patterns": {
        "title": "Number Patterns & Linear Sequences",
        "slug": "number-patterns",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: E3.3 • L1.6 • L2.6",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Term-to-Term Rules & Sequence Patterns",
            "points": [
                "Find the difference between consecutive terms to determine the term-to-term rule.",
                "Arithmetic sequence: Adds or subtracts a constant value each time (e.g. +4, -3).",
                "Geometric sequence: Multiplies or divides by a constant factor each time (e.g. ×2, ÷10).",
                "Position-to-term rule (nth term): nth term = (Common difference × n) + adjustment."
            ],
            "calc_tip": "Check the difference across at least 3 terms to verify that the pattern is consistent."
        },
        "workout_blocks": [
            {
                "title": "Finding the Next Two Terms",
                "instruction": "Identify the pattern and write the next two numbers:",
                "items": [
                    ("a", "4, 7, 10, 13, ___, ___", "16, 19 (Rule: +3)"),
                    ("b", "3, 8, 13, 18, ___, ___", "23, 28 (Rule: +5)"),
                    ("c", "40, 34, 28, 22, ___, ___", "16, 10 (Rule: -6)"),
                    ("d", "2, 4, 8, 16, ___, ___", "32, 64 (Rule: ×2)"),
                    ("e", "100, 50, 25, 12.5, ___", "6.25 (Rule: ÷2)"),
                    ("f", "1, 4, 9, 16, 25, ___, ___", "36, 49 (Square numbers)")
                ]
            },
            {
                "title": "Missing Intermediate Terms",
                "instruction": "Fill in the missing values within the sequence:",
                "items": [
                    ("a", "5, ___, 15, 20, ___", "10, 25"),
                    ("b", "12, 19, ___, 33, 40", "26 (Rule: +7)"),
                    ("c", "50, ___, 34, 26, ___", "42, 18 (Rule: -8)"),
                    ("d", "-8, -5, ___, 1, 4", "-2 (Rule: +3)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Warehouse Stacking & Pallet Logistics",
                "stem": "A logistics warehouse stores pallet crates in stepped triangular stacks.<br>The number of crates in the bottom 4 rows is:<br>Row 1: <strong>6 crates</strong><br>Row 2: <strong>11 crates</strong><br>Row 3: <strong>16 crates</strong><br>Row 4: <strong>21 crates</strong><br>(a) State the term-to-term rule for this stack pattern.<br>(b) Work out how many crates will be in <strong>Row 7</strong>.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Calculate common difference: 11 - 6 = +5 crates per row", "[M1]"),
                    ("Continue sequence for rows 5, 6, 7: Row 5 = 26, Row 6 = 31, Row 7 = 36", "[M1]"),
                    ("State answer clearly", "[A1]")
                ],
                "final_answer": "(a) Add 5 crates each row | (b) 36 crates in Row 7",
                "reverse_check": "Formula: 5n + 1 → 5(7) + 1 = 36 crates.",
                "pitfall": "Calculating only up to Row 5 or Row 6 instead of Row 7."
            }
        ]
    },

    # 9. MONEY
    "money": {
        "title": "Money, Invoicing & Payroll",
        "slug": "money",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.14 • L2.15 • L2.16",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Currency Rules & Decimal Precision",
            "points": [
                "In UK currency, money values MUST always have exactly 2 decimal places (e.g. £14.50, never £14.5 or £14.500).",
                "Do NOT combine '£' and 'p' in the same value (write £0.65 or 65p, never £0.65p).",
                "Calculating change: Total tendered minus Total cost.",
                "Gross pay: Total hours worked × Hourly rate (plus overtime).",
                "Net pay: Gross pay minus Deductions (Tax, National Insurance, Pension)."
            ],
            "calc_tip": "If a calculator displays 18.2, write it as £18.20. If it displays 6.75, write £6.75."
        },
        "workout_blocks": [
            {
                "title": "Adding and Subtracting Money",
                "instruction": "Work out the totals and change:",
                "prefix": "£",
                "items": [
                    ("a", "£14.25 + £8.60", "22.85"),
                    ("b", "£35.40 + £19.85", "55.25"),
                    ("c", "£120.00 - £47.60", "72.40"),
                    ("d", "£50.00 - £23.18", "26.82"),
                    ("e", "£3.45 + £12.80 + £0.95", "17.20"),
                    ("f", "Change from £20 note when spending £13.65", "6.35")
                ]
            },
            {
                "title": "Multiplying and Dividing Money",
                "instruction": "Calculate unit costs and batch totals:",
                "prefix": "£",
                "items": [
                    ("a", "8 items at £3.50 each", "28.00"),
                    ("b", "15 items at £2.40 each", "36.00"),
                    ("c", "6 hours work at £11.44 per hour", "68.64"),
                    ("d", "£84.00 shared equally between 5 people", "16.80"),
                    ("e", "£210.60 divided by 6 invoices", "35.10"),
                    ("f", "7 meals at £8.95 each", "62.65")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Commercial Catering Weekly Payroll",
                "stem": "A restaurant chef works <strong>38 standard hours</strong> at an hourly rate of <strong>£12.50 per hour</strong>.<br>On Sunday, the chef works <strong>6 hours overtime</strong> paid at <strong>time-and-a-half</strong> (1.5 times the standard rate).<br>Mandatory payroll deductions for income tax and national insurance total <strong>£94.20</strong>.<br>Work out the chef's <strong>take-home (net) pay</strong> for the week.",
                "marks": 4,
                "prefix": "£",
                "steps": [
                    ("Standard pay: 38 × £12.50 = £475.00", "[M1]"),
                    ("Overtime rate: £12.50 × 1.5 = £18.75 per hour; Overtime pay: 6 × £18.75 = £112.50", "[M1]"),
                    ("Total gross pay: £475.00 + £112.50 = £587.50", "[M1]"),
                    ("Deduct taxes: £587.50 - £94.20 = £493.30", "[A1]")
                ],
                "final_answer": "£493.30",
                "reverse_check": "£493.30 + £94.20 = £587.50 gross.",
                "pitfall": "Forgetting to multiply the standard hourly rate by 1.5 for the overtime rate."
            }
        ]
    },

    # 10. PROBLEMS INVOLVING MONEY
    "problems-involving-money": {
        "title": "Problems Involving Money & Multi-Tier Pricing",
        "slug": "problems-involving-money",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.14 • L2.15 • L2.16",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Multi-Step Quotations, Deposits & VAT",
            "points": [
                "VAT (Value Added Tax) in the UK is 20%. To calculate 20% VAT: multiply by 0.20 (or divide by 5).",
                "To add 20% VAT directly: multiply by 1.20.",
                "Deposit and Balance: Balance remaining = Total Price - Deposit paid.",
                "Installment payments: Total hire purchase cost = Deposit + (Number of months × Monthly payment)."
            ],
            "calc_tip": "When calculating installments, write down the monthly product before adding the deposit."
        },
        "workout_blocks": [
            {
                "title": "VAT and Percentage Surcharges",
                "instruction": "Work out the 20% VAT and total gross price:",
                "prefix": "£",
                "items": [
                    ("a", "20% VAT on net price of £60.00", "12.00 (Total £72.00)"),
                    ("b", "20% VAT on net price of £140.00", "28.00 (Total £168.00)"),
                    ("c", "20% VAT on net price of £450.00", "90.00 (Total £540.00)"),
                    ("d", "Net price £85.00 + 20% VAT. Total cost?", "102.00 (85 × 1.20)"),
                    ("e", "Net price £320.00 + 20% VAT. Total cost?", "384.00 (320 × 1.20)")
                ]
            },
            {
                "title": "Deposits and Monthly Repayments",
                "instruction": "Work out the total cost including deposit and installments:",
                "prefix": "£",
                "items": [
                    ("a", "£100 deposit + 12 monthly payments of £25. Total cost?", "400.00 (100 + 300)"),
                    ("b", "£250 deposit + 24 monthly payments of £40. Total cost?", "1,210.00 (250 + 960)"),
                    ("c", "Cash price £800 vs Credit: £150 deposit + 10 payments of £75. Extra cost of credit?", "100.00 (900 - 800)"),
                    ("d", "Total quote £1,500. Pay 15% deposit. Deposit amount?", "225.00")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Estates Maintenance Boiler Replacement",
                "stem": "A community facility replaces a heating boiler. A contractor provides two payment options:<br><strong>Option A (Cash Payment):</strong> <strong>£2,400 + 20% VAT</strong>, with a <strong>5% prompt payment discount</strong> off the gross total.<br><strong>Option B (Credit Plan):</strong> Deposit of <strong>£300</strong> followed by <strong>24 monthly installments of £115</strong> (VAT included).<br>Work out which option is cheaper and by how much.",
                "marks": 4,
                "prefix": "£",
                "steps": [
                    ("Option A gross total: £2,400 × 1.20 = £2,880", "[M1]"),
                    ("Option A with 5% discount: £2,880 × 0.95 = £2,736.00", "[M1]"),
                    ("Option B total: £300 + (24 × £115) = £300 + £2,760 = £3,060.00", "[M1]"),
                    ("Compare and find difference: £3,060 - £2,736 = £324.00 cheaper", "[A1]")
                ],
                "final_answer": "Option A is cheaper by £324.00",
                "reverse_check": "£3,060 - £324 = £2,736.",
                "pitfall": "Applying the 5% discount before adding 20% VAT or failing to compare both final amounts."
            }
        ]
    },

    # 11. BEST BUYS
    "best-buys": {
        "title": "Best Buys & Unit Pricing",
        "slug": "best-buys",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.15 • L2.17",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Unit Cost & Value Comparison Methods",
            "points": [
                "Method 1 (Unit Cost): Cost ÷ Quantity = Price per unit (e.g. pence per gram or £ per litre). The lowest cost per unit is the best value.",
                "Method 2 (Quantity per £): Quantity ÷ Cost = Amount received per £1. The higher quantity per £1 is the best value.",
                "Method 3 (Common Multiple): Scale up both packs to a common quantity (e.g. compare cost for 1,000 g or 10 litres).",
                "Always ensure currency units match (convert all to pence or all to pounds before comparing)."
            ],
            "calc_tip": "Round unit prices to at least 3 or 4 decimal places to avoid false equality when differences are small."
        },
        "workout_blocks": [
            {
                "title": "Calculating Unit Costs (Cost ÷ Quantity)",
                "instruction": "Work out the price per single item, gram, or litre:",
                "items": [
                    ("a", "6 pens for £3.60. Price per pen?", "£0.60 (60p)"),
                    ("b", "12 cans for £7.20. Price per can?", "£0.60 (60p)"),
                    ("c", "500 g butter for £2.50. Cost per 100 g?", "£0.50 (50p)"),
                    ("d", "750 g cereal for £3.00. Cost per 100 g?", "£0.40 (40p)"),
                    ("e", "2 litres milk for £1.50. Cost per litre?", "£0.75 (75p)"),
                    ("f", "5 litres paint for £32.50. Cost per litre?", "£6.50")
                ]
            },
            {
                "title": "Direct Best Buy Comparisons",
                "instruction": "Determine which pack offers better value for money:",
                "items": [
                    ("a", "Pack A: 4 batteries for £3.20. Pack B: 10 batteries for £7.50.", "Pack B is better value (75p each vs 80p each)"),
                    ("b", "Pack A: 800 g rice for £1.60. Pack B: 1.5 kg rice for £2.85.", "Pack B is better value (£1.90/kg vs £2.00/kg)"),
                    ("c", "Coffee A: 200 g for £4.50. Coffee B: 500 g for £10.50.", "Coffee B is better value (£2.10/100g vs £2.25/100g)"),
                    ("d", "Washing liquid A: 1.2 litres for £4.20. Liquid B: 2.5 litres for £8.00.", "Liquid B is better value (£3.20/L vs £3.50/L)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Medical Clinic Hand Sanitiser Procurement",
                "stem": "A procurement manager at a community clinic buys antibacterial hand sanitiser.<br>Two supply options are available from contracted medical wholesalers:<br>• <strong>Supplier X:</strong> <strong>6 bottles of 500 ml</strong> for a total cost of <strong>£14.40</strong><br>• <strong>Supplier Y:</strong> <strong>2 containers of 2 litres (2,000 ml)</strong> for a total cost of <strong>£18.00</strong><br>Which supplier offers the best value per litre? Show full calculations to justify your answer.",
                "marks": 3,
                "prefix": "£",
                "steps": [
                    ("Supplier X total volume: 6 × 500 ml = 3,000 ml = 3 litres", "[M1]"),
                    ("Supplier X cost per litre: £14.40 ÷ 3 = £4.80 per litre", "[M1]"),
                    ("Supplier Y total volume: 2 × 2 L = 4 litres; Cost per litre: £18.00 ÷ 4 = £4.50 per litre. Compare and state conclusion", "[A1]")
                ],
                "final_answer": "Supplier Y is better value (£4.50/L compared to £4.80/L)",
                "reverse_check": "3 L at £4.50 = £13.50 (cheaper than £14.40).",
                "pitfall": "Dividing the price by the number of bottles without converting to total litres."
            }
        ]
    },

    # 12. INTEREST AND COMPOUND INTEREST
    "interest-and-compound-interest": {
        "title": "Simple & Compound Interest",
        "slug": "interest-and-compound-interest",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.13 • L2.14",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Simple vs Compound Interest Formulas",
            "points": [
                "Simple Interest: Interest is earned ONLY on the initial principal. Formula: Interest = Principal × Rate × Time (I = P × R × T).",
                "Compound Interest: Interest is added to the principal each year, so you earn 'interest on interest'.",
                "Compound multiplier method: Future Value = Principal × (1 + r)^n (where r is interest rate as decimal, n is number of years).",
                "Year-by-year method: Calculate year 1 interest, add to balance; then calculate year 2 interest on the NEW balance."
            ],
            "calc_tip": "For a 4% compound interest rate over 3 years: multiply by 1.04 cubed (1.04³)."
        },
        "workout_blocks": [
            {
                "title": "Simple Interest Calculations",
                "instruction": "Work out the simple interest earned:",
                "prefix": "£",
                "items": [
                    ("a", "£500 invested at 3% simple interest for 1 year", "15.00"),
                    ("b", "£1,200 invested at 4% simple interest for 2 years", "96.00 (48 × 2)"),
                    ("c", "£2,500 invested at 5% simple interest for 3 years", "375.00 (125 × 3)"),
                    ("d", "£8,000 loan at 6% simple interest for 4 years", "1,920.00")
                ]
            },
            {
                "title": "Compound Interest (Step-by-Step)",
                "instruction": "Work out the total account balance after compound interest:",
                "prefix": "£",
                "items": [
                    ("a", "£1,000 at 5% compound interest for 2 years (Year 1: £1,050; Year 2?)", "1,102.50 (1,050 × 1.05)"),
                    ("b", "£2,000 at 3% compound interest for 2 years", "2,121.80 (2,000 × 1.03²)"),
                    ("c", "£5,000 at 4% compound interest for 2 years", "5,408.00 (5,000 × 1.04²)"),
                    ("d", "£3,000 at 2% compound interest for 3 years", "3,183.62 (3,000 × 1.02³)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Commercial Facility Capital Investment",
                "stem": "An estates management cooperative invests <strong>£15,000</strong> in a fixed-rate green energy bond paying <strong>4% compound interest per year</strong> for <strong>3 years</strong>.<br>(a) Work out the total value of the investment at the end of the 3 years.<br>(b) Calculate the total amount of interest earned over the 3 years.",
                "marks": 3,
                "prefix": "£",
                "steps": [
                    ("Identify compound multiplier: 1 + 0.04 = 1.04", "[M1]"),
                    ("Calculate 3-year compounded balance: £15,000 × 1.04³ = £15,000 × 1.124864 = £16,872.96", "[M1]"),
                    ("Subtract original principal to find interest earned: £16,872.96 - £15,000 = £1,872.96", "[A1]")
                ],
                "final_answer": "(a) £16,872.96 total value | (b) £1,872.96 interest earned",
                "reverse_check": "£16,872.96 ÷ (1.04³) = £15,000.",
                "pitfall": "Calculating simple interest (£15,000 × 0.04 × 3 = £1,800), which ignores compound growth."
            }
        ]
    },

    # 13. FORMULAS
    "formulas": {
        "title": "Algebra, Formulas & Substitution",
        "slug": "formulas",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.13 • L2.13 • L2.14",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Substitution, BIDMAS & Rearranging",
            "points": [
                "Substitution: Replace letters in a formula with their given numerical values.",
                "Multiplication is implied when a number and letter are written together (e.g. 5h means 5 × h).",
                "Always apply BIDMAS: evaluate brackets and powers BEFORE multiplying or adding.",
                "Rearranging formulas: Do the inverse operation to both sides to isolate the unknown letter."
            ],
            "calc_tip": "When substituting negative numbers into a formula on a calculator, always put them inside brackets: (-3)²."
        },
        "workout_blocks": [
            {
                "title": "Single-Step Substitution",
                "instruction": "Substitute the value of x = 5 into each expression:",
                "items": [
                    ("a", "3x", "15 (3 × 5)"),
                    ("b", "4x + 7", "27 (20 + 7)"),
                    ("c", "10 - 2x", "0 (10 - 10)"),
                    ("d", "x²", "25 (5 × 5)"),
                    ("e", "2x²", "50 (2 × 25)"),
                    ("f", "(x + 3) ÷ 2", "4 (8 ÷ 2)")
                ]
            },
            {
                "title": "Vocational Workplace Formulas",
                "instruction": "Use the formula to calculate the outcome:",
                "items": [
                    ("a", "Hire Cost = £30 + £15h. Find cost when h = 4 hours.", "£90.00 (30 + 60)"),
                    ("b", "Wage = £12.50 × hours + £20 bonus. Find wage for 8 hours.", "£120.00 (100 + 20)"),
                    ("c", "Catering: Time (minutes) = 45 × weight (kg) + 20. Find time for 3 kg meat.", "155 minutes (2 hrs 35 mins)"),
                    ("d", "Electrical: Power (Watts) = Current (I) × Voltage (V). Find P when I = 5A, V = 230V.", "1,150 Watts")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Healthcare Clinic BMI Health Assessment",
                "stem": "A community occupational health nurse calculates Body Mass Index (BMI) using the standard clinical formula:<br><strong>BMI = Weight in kg ÷ (Height in metres)²</strong><br>A care worker has a weight of <strong>84 kg</strong> and a height of <strong>1.75 metres</strong>.<br>(a) Calculate the worker's BMI to 1 decimal place.<br>(b) Healthy BMI is defined as 18.5 to 24.9. Is the worker within the healthy range?",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Calculate height squared: 1.75² = 3.0625 m²", "[M1]"),
                    ("Divide weight by height squared: 84 ÷ 3.0625 = 27.428...", "[M1]"),
                    ("Round to 1 decimal place (27.4) and conclude: No, outside healthy range (overweight category)", "[A1]")
                ],
                "final_answer": "(a) BMI = 27.4 | (b) No, above the 24.9 healthy threshold",
                "reverse_check": "27.428 × 3.0625 = 84 kg.",
                "pitfall": "Dividing 84 by 1.75 and then squaring the result (84 ÷ 1.75 = 48 → 48² = 2304)."
            }
        ]
    }
}

if __name__ == "__main__":
    print(f"Loaded {len(MATHS_BATCH2_PART1_WORKOUTS)} topics in authentic_workouts_maths_batch2_part1.py")
