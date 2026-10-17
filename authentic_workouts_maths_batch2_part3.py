#!/usr/bin/env python3
"""
Authentic Fluency Workouts: Maths Batch 2 (Part 3 - Handling Data, Charts & Statistics)
9 Curriculum Topics:
1. tally-charts
2. tables
3. lists
4. line-graphs
5. grouped-data
6. estimating-the-mean
7. comparing-data-sets
8. conversion-graphs
9. probability-tables
"""

MATHS_BATCH2_PART3_WORKOUTS = {
    # 1. TALLY CHARTS
    "tally-charts": {
        "title": "Tally Charts & Frequency Tables",
        "slug": "tally-charts",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: E3.8 • L1.27",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Recording Tallies & Calculating Frequency",
            "points": [
                "Tally marks are recorded in groups of 5: four vertical strokes with the fifth stroke crossing diagonally (卌).",
                "Frequency is the total count of tally marks for each category.",
                "Sum of frequencies: Always sum the frequency column to verify it matches the total number of data items.",
                "Mode category: The category with the highest frequency."
            ],
            "calc_tip": "Count tallies in groups of 5s first, then add any remaining single marks."
        },
        "workout_blocks": [
            {
                "title": "Reading and Converting Tally Marks",
                "instruction": "State the frequency represented by each tally group:",
                "items": [
                    ("a", "卌 ||", "7"),
                    ("b", "卌 卌 |", "11"),
                    ("c", "卌 卌 卌", "15"),
                    ("d", "卌 卌 卌 ||||", "19"),
                    ("e", "卌 卌 卌 卌 |||", "23")
                ]
            },
            {
                "title": "Completing Frequency Tables",
                "instruction": "Work out the missing frequency or total:",
                "items": [
                    ("a", "Category A: 14, Category B: 18, Category C: 9. Total frequency?", "41 (14 + 18 + 9)"),
                    ("b", "Total surveyed = 50. Car: 22, Bus: 16, Train: ?. Frequency of Train?", "12 (50 - 38)"),
                    ("c", "Which category has the highest frequency in (a)?", "Category B (18)"),
                    ("d", "What fraction of respondents chose Car in (b)?", "22/50 = 11/25 (44%)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Community Health Clinic Patient Survey",
                "stem": "A community clinic receptionist records patient arrival modes in a tally chart over one morning:<br>• On Foot: <strong>14 patients</strong><br>• By Bus: <strong>26 patients</strong><br>• By Car: <strong>35 patients</strong><br>• By Bicycle: <strong>5 patients</strong><br>(a) What was the total number of patients surveyed?<br>(b) What percentage of patients arrived by bus or bicycle?",
                "marks": 3,
                "prefix": "%",
                "steps": [
                    ("Calculate total patients: 14 + 26 + 35 + 5 = 80 patients", "[M1]"),
                    ("Sum Bus + Bicycle: 26 + 5 = 31 patients", "[M1]"),
                    ("Calculate percentage: 31 ÷ 80 = 0.3875 × 100 = 38.75%", "[A1]")
                ],
                "final_answer": "(a) 80 total patients | (b) 38.75%",
                "reverse_check": "80 × 0.3875 = 31 patients.",
                "pitfall": "Dividing 31 by 100 instead of dividing by the sample size of 80."
            }
        ]
    },

    # 2. TABLES
    "tables": {
        "title": "Data Tables & Information Retrieval",
        "slug": "tables",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: E3.9 • L1.27 • L2.25",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Two-Way Tables & Timetables",
            "points": [
                "Two-way table: Shows two variables simultaneously (rows and columns).",
                "Row totals and column totals must always add up to the Grand Total in the bottom-right cell.",
                "Reading bus/train timetables: Read down columns for one journey, read across rows for station arrival times.",
                "Time calculations: Remember there are 60 minutes in an hour, not 100!"
            ],
            "calc_tip": "When calculating time differences across timetables, count up to the next full hour first."
        },
        "workout_blocks": [
            {
                "title": "Completing Two-Way Table Cells",
                "instruction": "Find the missing values using row and column totals:",
                "items": [
                    ("a", "Row total = 45. Column 1 = 28. What is Column 2?", "17 (45 - 28)"),
                    ("b", "Column total = 60. Row 1 = 34. What is Row 2?", "26 (60 - 34)"),
                    ("c", "Men: 18 tea, 22 coffee. Total Men?", "40 (18 + 22)"),
                    ("d", "Women: 15 tea, 25 coffee. Total coffee drinkers (Men + Women)?", "47 (22 + 25)"),
                    ("e", "Grand Total for table (c) and (d)?", "80 (40 men + 40 women)")
                ]
            },
            {
                "title": "Reading Timetables and Elapsed Time",
                "instruction": "Work out the departure time or journey duration:",
                "items": [
                    ("a", "Bus departs 08:35, arrives 09:18. Journey duration?", "43 minutes"),
                    ("b", "Train departs 14:45, journey takes 1 hour 25 minutes. Arrival?", "16:10"),
                    ("c", "Shift starts at 07:15 and finishes at 15:45 with 45 min unpaid lunch. Working hours?", "7 hours 45 mins"),
                    ("d", "Meeting from 10:20 to 11:55. Meeting length?", "1 hour 35 mins (95 mins)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Medical Diagnostics Phlebotomy Clinic",
                "stem": "A diagnostic clinic tracks blood testing appointments in a two-way table across two days:<br>• Monday: <strong>48 Fasting tests</strong> and <strong>32 Routine tests</strong><br>• Tuesday: <strong>36 Fasting tests</strong> and <strong>44 Routine tests</strong><br>(a) Complete the grand total of all appointments across both days.<br>(b) What fraction of all appointments across both days were Fasting tests? Give your answer in simplest form.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Monday total: 48 + 32 = 80; Tuesday total: 36 + 44 = 80; Grand total: 80 + 80 = 160", "[M1]"),
                    ("Total Fasting tests: 48 + 36 = 84", "[M1]"),
                    ("Simplify fraction: 84 ÷ 160 = 42/80 = 21/40", "[A1]")
                ],
                "final_answer": "(a) 160 total appointments | (b) 21/40 (52.5%)",
                "reverse_check": "160 × 21/40 = 84 fasting tests.",
                "pitfall": "Simplifying only to 42/80 without reducing to simplest form 21/40."
            }
        ]
    },

    # 3. LISTS
    "lists": {
        "title": "Lists: Sorting & Information Extraction",
        "slug": "lists",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: E3.8 • L1.27",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Systematic Listing & Filtering",
            "points": [
                "Listing outcomes: Work systematically to avoid missing combinations (e.g. A1, A2, A3, B1, B2, B3).",
                "Total possible outcomes: Number of choices in category 1 × Number of choices in category 2.",
                "Filtering criteria: Check each item against all conditions (e.g. 'Must cost under £20 AND be in stock').",
                "Sorting: Alphabetical (A-Z) or Numerical (ascending/descending)."
            ],
            "calc_tip": "When listing combinations, keep one variable fixed while cycling through the others."
        },
        "workout_blocks": [
            {
                "title": "Systematic Combinations",
                "instruction": "Work out the total number of possible combinations:",
                "items": [
                    ("a", "3 sandwich options and 4 drink options. How many meal deals?", "12 combinations (3 × 4)"),
                    ("b", "4 starter options and 5 main course options. How many 2-course meals?", "20 combinations (4 × 5)"),
                    ("c", "2 coin choices (Heads/Tails) and a 6-sided dice. Outcomes?", "12 outcomes (2 × 6)"),
                    ("d", "List all combinations of T-shirt (Red, Blue) and Shorts (Black, White)", "(Red, Black), (Red, White), (Blue, Black), (Blue, White)")
                ]
            },
            {
                "title": "Data Filtering and Criteria Matching",
                "instruction": "Filter data against stated conditions:",
                "items": [
                    ("a", "Scores: 45, 62, 78, 55, 84, 91, 48. How many scored 60 or more?", "4 scores (62, 78, 84, 91)"),
                    ("b", "Prices: £14, £25, £19, £32, £18. How many are under £20?", "3 items (£14, £19, £18)"),
                    ("c", "Ages: 24, 17, 35, 18, 42, 16. How many are 18 or older?", "4 people (24, 35, 18, 42)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Commercial Catering Set Menu Combinations",
                "stem": "A hospital cafeteria offers a subsidised meal deal for clinical staff.<br>Staff choose <strong>one main dish</strong>, <strong>one side dish</strong>, and <strong>one dessert</strong>.<br>The menu has:<br>• <strong>4 main dishes</strong> (Chicken curry, Vegetable pasta, Baked cod, Vegan wrap)<br>• <strong>3 side dishes</strong> (Steamed rice, Garden salad, Roasted potatoes)<br>• <strong>3 desserts</strong> (Fruit bowl, Low-fat yogurt, Lemon cake)<br>(a) Work out the total number of different three-course meal combinations available.<br>(b) How many combinations include the Vegan wrap?",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Calculate total combinations: 4 × 3 × 3 = 36 combinations", "[M1]"),
                    ("Calculate combinations with Vegan wrap (1 main fixed): 1 × 3 × 3 = 9 combinations", "[M1]"),
                    ("State answers clearly", "[A1]")
                ],
                "final_answer": "(a) 36 total combinations | (b) 9 vegan wrap combinations",
                "reverse_check": "36 ÷ 4 = 9 combinations per main dish.",
                "pitfall": "Adding the options (4 + 3 + 3 = 10) instead of multiplying them."
            }
        ]
    },

    # 4. LINE GRAPHS
    "line-graphs": {
        "title": "Line Graphs & Trend Analysis",
        "slug": "line-graphs",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.27 • L2.26",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Reading Axes, Trends & Interpolation",
            "points": [
                "Line graphs show continuous data over time (e.g. temperature, sales, stock levels).",
                "Horizontal axis (x): Almost always represents Time (hours, days, months, years).",
                "Vertical axis (y): Represents the measured variable with a scaled unit.",
                "Trend: Describes the general direction over time (upward/increasing trend, downward/decreasing trend, or stable).",
                "To read a value: Locate time on the x-axis, move vertically to the line, and read directly across to the y-axis."
            ],
            "calc_tip": "Check the scale of each small grid square on the y-axis (e.g. does 1 square = 2 units, 5 units, or 10 units?)."
        },
        "workout_blocks": [
            {
                "title": "Determining Axis Scales and Intervals",
                "instruction": "Work out the value represented by one small grid square:",
                "items": [
                    ("a", "0 to 50 on y-axis marked across 10 grid squares. Value per square?", "5 units (50 ÷ 10)"),
                    ("b", "0 to 100 on y-axis marked across 5 major squares. Value per square?", "20 units (100 ÷ 5)"),
                    ("c", "0 to 20 on y-axis marked across 10 grid squares. Value per square?", "2 units (20 ÷ 10)"),
                    ("d", "10°C to 15°C marked across 5 squares. Value per square?", "1°C per square")
                ]
            },
            {
                "title": "Describing Trends and Rate of Change",
                "instruction": "State whether the trend is increasing, decreasing, or constant:",
                "items": [
                    ("a", "Patient visits rise from 40 in Jan to 85 in June. Trend?", "Increasing / upward trend"),
                    ("b", "Medication errors fall from 12 in Q1 to 2 in Q4. Trend?", "Decreasing / downward trend"),
                    ("c", "A line graph is completely horizontal. What does this mean?", "No change / value remained constant"),
                    ("d", "Between which two hours is change steepest: 08:00-09:00 (+5) or 09:00-10:00 (+18)?", "09:00 to 10:00 (steeper gradient)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Pharmacy Cold Storage Temperature Tracking",
                "stem": "An electronic data logger tracks the temperature inside a clinical vaccine storage unit over 6 hours:<br>• 08:00: <strong>3.2°C</strong><br>• 10:00: <strong>3.8°C</strong><br>• 12:00: <strong>5.4°C</strong><br>• 14:00: <strong>6.8°C</strong><br>(a) Describe the general trend in temperature between 08:00 and 14:00.<br>(b) Work out the total temperature increase from 08:00 to 14:00.<br>(c) Safe vaccine storage requires temperature to stay strictly below <strong>8.0°C</strong>. Did the temperature remain safe?",
                "marks": 3,
                "prefix": "°C",
                "steps": [
                    ("Identify trend: Upward / increasing trend over time", "[M1]"),
                    ("Calculate total increase: 6.8°C - 3.2°C = 3.6°C increase", "[M1]"),
                    ("Compare against limit: 6.8°C < 8.0°C, so Yes, it remained within the safe limit", "[A1]")
                ],
                "final_answer": "(a) Upward trend | (b) 3.6°C increase | (c) Yes, stayed under 8.0°C",
                "reverse_check": "3.2 + 3.6 = 6.8°C.",
                "pitfall": "Omitting the word 'increase' or failing to state the units."
            }
        ]
    },

    # 5. GROUPED DATA
    "grouped-data": {
        "title": "Grouped Frequency Tables",
        "slug": "grouped-data",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.28 • L2.23",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Intervals, Modal Class & Midpoints",
            "points": [
                "Grouped data groups numerical values into class intervals (e.g. 10 ≤ w < 20, 20 ≤ w < 30).",
                "Modal Class: The class interval with the highest frequency.",
                "Median Class: The interval containing the middle value (Total frequency ÷ 2).",
                "Midpoint of an interval: (Lower bound + Upper bound) ÷ 2 (e.g. midpoint of 10 to 20 is (10 + 20) ÷ 2 = 15).",
                "Continuous vs discrete data: Waiting time is continuous; number of children is discrete."
            ],
            "calc_tip": "Always check inequality signs: '10 ≤ x < 20' means 10 is included, but 20 belongs to the next group!"
        },
        "workout_blocks": [
            {
                "title": "Finding Midpoints of Class Intervals",
                "instruction": "Calculate the exact midpoint ((Lower + Upper) ÷ 2):",
                "items": [
                    ("a", "Interval: 0 to 10", "5"),
                    ("b", "Interval: 10 to 20", "15"),
                    ("c", "Interval: 20 to 30", "25"),
                    ("d", "Interval: 25 to 35", "30"),
                    ("e", "Interval: 40 to 60", "50"),
                    ("f", "Interval: 100 to 150", "125")
                ]
            },
            {
                "title": "Identifying Modal Class and Median Class",
                "instruction": "Determine the requested class interval from the frequency table (A: 0-10: 4, B: 10-20: 12, C: 20-30: 8):",
                "items": [
                    ("a", "What is the Modal Class?", "10 to 20 (Frequency = 12)"),
                    ("b", "Total frequency across all three groups?", "24 (4 + 12 + 8)"),
                    ("c", "Which group contains the median (12th/13th person)?", "10 to 20 (cumulative: 4 in first, next 12 in second)"),
                    ("d", "What percentage of values fall in the modal class?", "50% (12 ÷ 24)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Community Clinic Waiting Time Audit",
                "stem": "A healthcare manager audits patient waiting times (w minutes) across <strong>60 patients</strong>:<br>• 0 ≤ w < 10: <strong>14 patients</strong><br>• 10 ≤ w < 20: <strong>26 patients</strong><br>• 20 ≤ w < 30: <strong>15 patients</strong><br>• 30 ≤ w < 40: <strong>5 patients</strong><br>(a) State the modal class for waiting times.<br>(b) Work out the fraction of patients who waited <strong>20 minutes or longer</strong>. Give your answer in simplest form.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Identify highest frequency: 26 in interval 10 ≤ w < 20", "[M1]"),
                    ("Sum patients waiting ≥ 20 mins: 15 + 5 = 20 patients", "[M1]"),
                    ("Calculate fraction in simplest form: 20 ÷ 60 = 1/3", "[A1]")
                ],
                "final_answer": "(a) 10 ≤ w < 20 | (b) 1/3 (33.3%)",
                "reverse_check": "60 × 1/3 = 20 patients.",
                "pitfall": "Including the 10-20 interval when asked for 20 minutes or longer."
            }
        ]
    },

    # 6. ESTIMATING THE MEAN
    "estimating-the-mean": {
        "title": "Estimating the Mean from Grouped Data",
        "slug": "estimating-the-mean",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L2.23",
        "level": "Level 2",
        "method_card": {
            "title": "Step-by-Step Estimated Mean Algorithm",
            "points": [
                "Step 1: Calculate the midpoint (m) for each class interval.",
                "Step 2: Multiply each midpoint by its frequency: m × f.",
                "Step 3: Sum the products column: Total (m × f).",
                "Step 4: Sum the frequency column: Total Frequency (Σf).",
                "Step 5: Estimated Mean = Total (m × f) ÷ Total Frequency."
            ],
            "calc_tip": "We call it an 'estimate' because we do not know the exact raw values inside each interval, only the group boundaries."
        },
        "workout_blocks": [
            {
                "title": "Midpoint × Frequency Drills",
                "instruction": "Work out the product m × f for each group:",
                "items": [
                    ("a", "Midpoint = 5, Frequency = 8", "40 (5 × 8)"),
                    ("b", "Midpoint = 15, Frequency = 12", "180 (15 × 12)"),
                    ("c", "Midpoint = 25, Frequency = 6", "150 (25 × 6)"),
                    ("d", "Midpoint = 35, Frequency = 4", "140 (35 × 4)"),
                    ("e", "Sum of frequencies (8 + 12 + 6 + 4)?", "30"),
                    ("f", "Sum of products (40 + 180 + 150 + 140)?", "510"),
                    ("g", "Estimated mean (510 ÷ 30)?", "17")
                ]
            },
            {
                "title": "Estimated Mean Calculations",
                "instruction": "Divide Total (m × f) by Total Frequency:",
                "items": [
                    ("a", "Total (m × f) = 720, Total frequency = 40. Estimated mean?", "18 (720 ÷ 40)"),
                    ("b", "Total (m × f) = 1,450, Total frequency = 50. Estimated mean?", "29 (1,450 ÷ 50)"),
                    ("c", "Total (m × f) = 630, Total frequency = 25. Estimated mean?", "25.2 (630 ÷ 25)"),
                    ("d", "Why is this an 'estimate' rather than exact mean?", "Raw individual values are unknown; midpoints represent group averages")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Commercial Logistics Driver Shift Duration",
                "stem": "A delivery transport firm records daily driving hours for <strong>40 couriers</strong> in a grouped frequency table:<br>• 2 ≤ h < 4: Midpoint 3, Frequency 6<br>• 4 ≤ h < 6: Midpoint 5, Frequency 18<br>• 6 ≤ h < 8: Midpoint 7, Frequency 12<br>• 8 ≤ h < 10: Midpoint 9, Frequency 4<br>Calculate an estimate of the mean daily driving time for these couriers.",
                "marks": 4,
                "prefix": "hours",
                "steps": [
                    ("Calculate m × f products: (3 × 6 = 18) + (5 × 18 = 90) + (7 × 12 = 84) + (9 × 4 = 36)", "[M1]"),
                    ("Sum products: 18 + 90 + 84 + 36 = 228", "[M1]"),
                    ("Total frequency = 6 + 18 + 12 + 4 = 40 couriers", "[M1]"),
                    ("Divide total products by total frequency: 228 ÷ 40 = 5.7 hours", "[A1]")
                ],
                "final_answer": "5.7 hours (or 5 hours 42 minutes)",
                "reverse_check": "5.7 × 40 = 228.",
                "pitfall": "Dividing the sum of products by 4 (the number of groups) instead of 40 (the total frequency)."
            }
        ]
    },

    # 7. COMPARING DATA SETS
    "comparing-data-sets": {
        "title": "Comparing Data Sets & Distribution Consistency",
        "slug": "comparing-data-sets",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.29 • L2.24",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Pearson Edexcel 2-Statement Comparison Rule",
            "points": [
                "In Functional Skills exams, comparing two data sets ALWAYS requires TWO statements:",
                "Statement 1 (Average): Compare ONE average (Mean or Median) to state which group is higher on average, quoting both values.",
                "Statement 2 (Spread/Consistency): Compare the Range (or IQR) to state which group is more consistent / less varied, quoting both values.",
                "Golden rule: A smaller range means MORE consistent (less spread out). A larger range means LESS consistent (more spread out).",
                "Always include context words (e.g. 'Patients waited less on average in Ward B...')."
            ],
            "calc_tip": "Never write 'The range is better'. Write 'The range is smaller (4 mins vs 12 mins), so times were more consistent.'"
        },
        "workout_blocks": [
            {
                "title": "Interpreting Averages and Ranges",
                "instruction": "Compare the two sets and state the valid mathematical deduction:",
                "items": [
                    ("a", "Team A Mean = £420, Team B Mean = £480. Which team earned more on average?", "Team B (£480 vs £420)"),
                    ("b", "Depot 1 Range = 14 kg, Depot 2 Range = 6 kg. Which depot had more consistent parcel weights?", "Depot 2 (smaller range of 6 kg)"),
                    ("c", "Clinic X Median = 24 mins, Clinic Y Median = 18 mins. Which clinic had shorter typical wait?", "Clinic Y (18 mins vs 24 mins)"),
                    ("d", "Shift 1 Range = 8 hours, Shift 2 Range = 15 hours. Which shift was more variable?", "Shift 2 (larger range of 15 hours)")
                ]
            },
            {
                "title": "Formulating Comparative Sentences",
                "instruction": "Fill in the missing words (higher/lower, more/less consistent):",
                "items": [
                    ("a", "Mean A is 25, Mean B is 20. On average, A is ___ than B.", "higher (25 vs 20)"),
                    ("b", "Range A is 12, Range B is 5. Group B's results are ___ than Group A.", "more consistent (5 vs 12)"),
                    ("c", "Can the range ever be negative?", "No (Highest minus Lowest is always ≥ 0)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Healthcare Clinic Triage Performance Review",
                "stem": "A clinical operations lead compares patient triage times across two regional walk-in clinics:<br><strong>Clinic North:</strong> Mean = <strong>28 minutes</strong>, Range = <strong>14 minutes</strong><br><strong>Clinic South:</strong> Mean = <strong>22 minutes</strong>, Range = <strong>24 minutes</strong><br>Make two comparative comments comparing the performance of Clinic North and Clinic South. You must quote values to support your statements.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Comparison of average: Clinic South had a faster/lower average waiting time than Clinic North (Mean: 22 mins vs 28 mins)", "[M1]"),
                    ("Comparison of consistency: Clinic North had more consistent waiting times than Clinic South because its range was smaller (Range: 14 mins vs 24 mins)", "[M1]"),
                    ("Ensure context and accurate figures are cited in both statements", "[A1]")
                ],
                "final_answer": "1. Average: Clinic South was faster on average (Mean: 22 mins vs 28 mins). 2. Consistency: Clinic North was more consistent (Range: 14 mins vs 24 mins).",
                "reverse_check": "28 - 22 = 6 mins difference in mean; 24 - 14 = 10 mins difference in range.",
                "pitfall": "Stating only one comparison (e.g. comparing the means but forgetting the range) or stating that Clinic South has a 'better' range without explaining consistency."
            }
        ]
    },

    # 8. CONVERSION GRAPHS
    "conversion-graphs": {
        "title": "Conversion Graphs & Currency Exchange",
        "slug": "conversion-graphs",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.17 • L2.18",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Reading and Scaling Conversion Lines",
            "points": [
                "A conversion graph is a straight-line graph through the origin (0, 0) connecting two proportional units.",
                "To convert: Find the given value on one axis, draw a dashed line perpendicular to the axis until it hits the conversion line, then read across to the second axis.",
                "Extending beyond the graph: If the value is off the graph, convert an easy multiple and scale up (e.g. to find £500, find £50 on the graph and multiply the answer by 10).",
                "Common conversions: Miles to km (5 miles ≈ 8 km); Pounds to Euros or Dollars; Litres to Gallons."
            ],
            "calc_tip": "Always use a sharp pencil and ruler to follow grid lines accurately."
        },
        "workout_blocks": [
            {
                "title": "Currency Conversions from Rates",
                "instruction": "Use the exchange rate £1 = €1.15 to calculate the value:",
                "items": [
                    ("a", "Convert £20 into Euros (€)", "€23.00 (20 × 1.15)"),
                    ("b", "Convert £50 into Euros (€)", "€57.50 (50 × 1.15)"),
                    ("c", "Convert £100 into Euros (€)", "€115.00 (100 × 1.15)"),
                    ("d", "Convert €230 into Pounds (£)", "£200.00 (230 ÷ 1.15)"),
                    ("e", "Convert €46 into Pounds (£)", "£40.00 (46 ÷ 1.15)")
                ]
            },
            {
                "title": "Metric to Imperial Distance Conversions (5 miles ≈ 8 km)",
                "instruction": "Use the ratio 5 miles = 8 km to convert:",
                "items": [
                    ("a", "10 miles in kilometres", "16 km (2 × 8)"),
                    ("b", "25 miles in kilometres", "40 km (5 × 8)"),
                    ("c", "50 miles in kilometres", "80 km (10 × 8)"),
                    ("d", "24 km in miles", "15 miles (3 × 5)"),
                    ("e", "48 km in miles", "30 miles (6 × 5)"),
                    ("f", "400 km in miles", "250 miles (50 × 5)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "International Medical Conference Travel Budget",
                "stem": "A biomedical research officer attends a clinical symposium in Paris.<br>The officer books a hotel costing <strong>€575 (Euros)</strong>.<br>The exchange rate is <strong>£1 = €1.15</strong>.<br>The officer's maximum allowable accommodation budget is <strong>£520</strong>.<br>(a) Convert €575 into British Pounds (£).<br>(b) Is the hotel cost within the officer's allowable budget? State the difference.",
                "marks": 3,
                "prefix": "£",
                "steps": [
                    ("Convert Euros to Pounds by dividing by exchange rate: €575 ÷ 1.15", "[M1]"),
                    ("Accurate conversion: £500.00", "[M1]"),
                    ("Compare against budget: £500.00 < £520.00, so Yes, it is £20 under budget", "[A1]")
                ],
                "final_answer": "Yes, within budget (Cost = £500.00, £20.00 under limit)",
                "reverse_check": "£500 × 1.15 = €575.",
                "pitfall": "Multiplying €575 by 1.15 instead of dividing to convert back to Pounds."
            }
        ]
    },

    # 9. PROBABILITY TABLES
    "probability-tables": {
        "title": "Probability Outcomes, Sample Space & Combined Events",
        "slug": "probability-tables",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.30 • L2.27 • L2.28",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Sample Space Grids & Combined Events",
            "points": [
                "Sample space diagram: A grid showing ALL possible outcomes when two independent events happen together (e.g. rolling two dice or tossing a coin and rolling a dice).",
                "Total outcomes = (Outcomes of Event 1) × (Outcomes of Event 2) (e.g. 6 × 6 = 36 outcomes for two dice).",
                "Probability = (Number of favourable outcomes in the grid) ÷ (Total number of outcomes in the grid).",
                "Combined independent events: P(A and B) = P(A) × P(B)."
            ],
            "calc_tip": "When filling a two-dice sum table, values along diagonal lines will always be equal."
        },
        "workout_blocks": [
            {
                "title": "Sample Space Outcomes for Two Dice",
                "instruction": "For two standard 6-sided dice (total 36 outcomes), find the probability of each sum:",
                "items": [
                    ("a", "P(Sum of 2) [only 1+1]", "1/36"),
                    ("b", "P(Sum of 7) [1+6, 2+5, 3+4, 4+3, 5+2, 6+1]", "6/36 = 1/6"),
                    ("c", "P(Sum of 12) [only 6+6]", "1/36"),
                    ("d", "P(Sum of 10) [4+6, 5+5, 6+4]", "3/36 = 1/12"),
                    ("e", "P(Rolling a Double) [1,1 to 6,6]", "6/36 = 1/6"),
                    ("f", "P(Sum greater than 10) [sums 11 and 12: 3 outcomes]", "3/36 = 1/12")
                ]
            },
            {
                "title": "Independent Combined Events: P(A and B)",
                "instruction": "Multiply probabilities for two independent events:",
                "items": [
                    ("a", "Toss a coin (P(H)=1/2) and roll a 6 on a dice (1/6). P(H and 6)?", "1/12 (1/2 × 1/6)"),
                    ("b", "Two coins tossed. P(Heads and Heads)?", "1/4 (1/2 × 1/2)"),
                    ("c", "P(Bus on time) = 0.8; P(Train on time) = 0.9. P(Both on time)?", "0.72 (0.8 × 0.9)"),
                    ("d", "P(Machine A fails) = 0.05; P(Machine B fails) = 0.02. P(Both fail)?", "0.001 (0.05 × 0.02)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Medical Diagnostics Automated Screening",
                "stem": "An automated clinical laboratory system runs two sequential independent diagnostic checks on blood samples:<br>• Primary screening machine has an error rate of <strong>0.04 (4%)</strong><br>• Secondary confirmation scanner has an error rate of <strong>0.05 (5%)</strong><br>(a) Work out the probability that <strong>both machines fail</strong> simultaneously.<br>(b) Work out the probability that the primary machine operates successfully without error.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Multiply probabilities for independent failure: 0.04 × 0.05 = 0.002 (or 0.2% / 1 in 500)", "[M1]"),
                    ("Calculate success rate for primary machine: 1 - 0.04 = 0.96 (or 96%)", "[M1]"),
                    ("State answers clearly with correct decimal or percentage format", "[A1]")
                ],
                "final_answer": "(a) 0.002 (0.2%) | (b) 0.96 (96%)",
                "reverse_check": "0.002 ÷ 0.04 = 0.05.",
                "pitfall": "Adding the probabilities (0.04 + 0.05 = 0.09) instead of multiplying them for combined independent events."
            }
        ]
    }
}

if __name__ == "__main__":
    print(f"Loaded {len(MATHS_BATCH2_PART3_WORKOUTS)} topics in authentic_workouts_maths_batch2_part3.py")
