#!/usr/bin/env python3
"""
Authentic Fluency Workouts: Maths Handling Data & Statistics
5 Core High-Yield Topics:
- probability
- scatter-graphs
- bar-charts
- pie-charts
- data-tables
"""

MATHS_DATA_WORKOUTS = {
    # 1. PROBABILITY
    "probability": {
        "title": "Probability Scale & Single Event Outcomes",
        "slug": "probability",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.30 • L2.27 • L2.28",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Probability Scale & Formula",
            "points": [
                "Probability scale runs from 0 (Impossible) to 1 (Certain).",
                "Probability formula: P(Event) = (Number of successful outcomes) ÷ (Total number of possible outcomes).",
                "Can be expressed as a Fraction, Decimal, or Percentage (e.g. 1/4 = 0.25 = 25%).",
                "Probabilities of all mutually exclusive outcomes ALWAYS add up to 1.",
                "P(Not Event) = 1 - P(Event)."
            ],
            "calc_tip": "In Functional Skills exams, simplify probability fractions unless told otherwise (e.g. 6/10 = 3/5)."
        },
        "workout_blocks": [
            {
                "title": "Probability Fractions & Simplifying",
                "instruction": "Express each probability as a simplified fraction:",
                "items": [
                    ("a", "Rolling a 4 on a standard 6-sided dice", "1/6"),
                    ("b", "Rolling an even number on a 6-sided dice", "1/2 (3/6)"),
                    ("c", "Rolling a number greater than 4 on a dice (5 or 6)", "1/3 (2/6)"),
                    ("d", "Picking a red counter from 4 red and 6 blue", "2/5 (4/10)"),
                    ("e", "Picking a yellow counter from 3 red, 5 green, 2 yellow", "1/5 (2/10)"),
                    ("f", "Tossing a coin and getting Tails", "1/2")
                ]
            },
            {
                "title": "Probability Sums to 1 (Decimals & Percentages)",
                "instruction": "Work out the missing probability:",
                "items": [
                    ("a", "P(Win) = 0.65. What is P(Lose)?", "0.35 (1 - 0.65)"),
                    ("b", "P(Rain) = 40%. What is P(No Rain)?", "60% (100% - 40%)"),
                    ("c", "P(Pass) = 0.82. What is P(Fail)?", "0.18"),
                    ("d", "Three outcomes: P(A) = 0.3, P(B) = 0.45. P(C) = ?", "0.25 (1 - 0.75)"),
                    ("e", "Probability of a train being on time is 7/10. Late?", "3/10"),
                    ("f", "Probability spinner lands on Red is 0.15, Blue 0.35. Green?", "0.50 (1 - 0.50)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Healthcare Outpatients Booking Probability",
                "stem": "An outpatient physiotherapy clinic reviews its appointment attendance records over <strong>200 scheduled sessions</strong>:<br>• 156 patients attended on time<br>• 28 patients arrived late<br>• 16 patients did not attend (DNA)<br>(a) What is the probability that a randomly chosen patient attended on time? Give your answer as a simplified fraction and as a percentage.<br>(b) What is the probability that a patient did NOT attend?",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Fraction on time: 156 ÷ 200 = 78/100 = 39/50", "[M1]"),
                    ("Convert to percentage: 78/100 = 78%", "[A1]"),
                    ("Probability of DNA = 16 ÷ 200 = 8/100 = 2/25 (or 8% / 0.08)", "[A1]")
                ],
                "final_answer": "(a) 39/50 (78%) | (b) 2/25 (0.08 or 8%)",
                "reverse_check": "78% + 14% late + 8% DNA = 100%.",
                "pitfall": "Giving probability as a ratio (e.g. 156 : 44) instead of a fraction, decimal, or percentage."
            }
        ]
    },

    # 2. SCATTER GRAPHS
    "scatter-graphs": {
        "title": "Scatter Graphs, Correlation & Lines of Best Fit",
        "slug": "scatter-graphs",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.27 • L2.26",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Types of Correlation & Line of Best Fit Rules",
            "points": [
                "Positive Correlation: As variable X increases, variable Y increases (points slope upwards from bottom-left to top-right).",
                "Negative Correlation: As variable X increases, variable Y decreases (points slope downwards from top-left to bottom-right).",
                "No Correlation / Zero Correlation: Points are scattered randomly with no clear linear pattern.",
                "Line of Best Fit: A straight line drawn through the middle of the plotted points with roughly an equal number of points above and below.",
                "Using the Line of Best Fit: Draw a dashed line from your known value up/across to the line, then read across to the other axis."
            ],
            "calc_tip": "Always use a ruler and sharp pencil to draw a line of best fit. It does NOT have to go through the origin (0,0)!"
        },
        "workout_blocks": [
            {
                "title": "Identifying Correlation Types",
                "instruction": "State whether the relationship exhibits Positive, Negative, or No Correlation:",
                "items": [
                    ("a", "Hours spent revising and exam marks scored", "Positive correlation"),
                    ("b", "Age of a used car and its market resale value", "Negative correlation"),
                    ("c", "Shoe size and IQ test score", "No correlation"),
                    ("d", "Outdoor summer temperature and ice cream sales", "Positive correlation"),
                    ("e", "Speed of a vehicle and time taken to complete a 50-mile trip", "Negative correlation"),
                    ("f", "Number of heaters turned on and room temperature", "Positive correlation")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Healthcare Hospital Emergency Triage Audit",
                "stem": "An accident and emergency department plots a scatter graph comparing <strong>Number of Emergency Doctors on Shift</strong> against <strong>Average Patient Triage Waiting Time (minutes)</strong>.<br>The points slope downwards from 60 minutes with 2 doctors down to 18 minutes with 8 doctors.<br>(a) What type of correlation does the scatter graph show?<br>(b) Write a one-sentence conclusion summarizing the relationship between doctor numbers and waiting time.",
                "marks": 2,
                "prefix": "",
                "steps": [
                    ("Identify correlation: Points slope downward from left to right = Negative Correlation.", "[A1]"),
                    ("Conclusion: As the number of doctors on shift increases, the average patient waiting time decreases.", "[A1]")
                ],
                "final_answer": "(a) Negative Correlation | (b) Increasing the number of doctors on duty decreases patient waiting times.",
                "reverse_check": "More staff results in faster processing.",
                "pitfall": "Stating positive correlation because having more doctors is 'a good thing'."
            }
        ]
    },

    # 3. BAR CHARTS
    "bar-charts": {
        "title": "Bar Charts: Dual, Component & Frequency",
        "slug": "bar-charts",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.26 • L2.22",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Bar Chart Features & Common Exam Pitfalls",
            "points": [
                "Bars must have equal widths and equal gaps between them (for discrete data).",
                "The vertical axis (Frequency) MUST start at 0 with a constant, evenly spaced scale.",
                "Both axes must have clear labels and units.",
                "Every chart must have an informative title.",
                "Dual bar charts must include a clear key/legend to distinguish between the two categories."
            ],
            "calc_tip": "When drawing bar charts in an exam, use a ruler and check your vertical scale intervals (e.g. going up in 2s, 5s, or 10s)."
        },
        "workout_blocks": [
            {
                "title": "Reading Bar Chart Scales",
                "instruction": "Work out the value represented by each bar height:",
                "items": [
                    ("a", "Scale goes 0, 10, 20... Bar is halfway between 30 and 40", "35"),
                    ("b", "Scale goes 0, 5, 10... Bar is 2 small marks above 15 (1 mark = 1)", "17"),
                    ("c", "Scale goes 0, 50, 100... Bar is 3 marks below 100 (1 mark = 10)", "70"),
                    ("d", "Dual bar chart: Blue bar = 45, Orange bar = 28. Difference?", "17 (45 - 28)"),
                    ("e", "Total of 4 bars with heights 12, 18, 25, 15", "70"),
                    ("f", "Fraction of total (70) represented by bar of height 25", "25/70 = 5/14")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Healthcare Staff Sickness Absence Audit",
                "stem": "A hospital HR department reviews a dual bar chart comparing staff sickness days between <strong>2024 and 2025</strong> across four departments:<br>• Emergency: 2024 = 120 days, 2025 = 95 days<br>• Surgery: 2024 = 85 days, 2025 = 90 days<br>• Outpatients: 2024 = 60 days, 2025 = 45 days<br>• Facilities: 2024 = 110 days, 2025 = 80 days<br>(a) Which department achieved the greatest reduction in sickness days?<br>(b) Calculate the total overall reduction in sickness days across all 4 departments.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Calculate reductions: Emergency = 120 - 95 = 25; Surgery = 85 - 90 = -5 (increase); Outpatients = 60 - 45 = 15; Facilities = 110 - 80 = 30 days", "[M1]"),
                    ("Greatest reduction: Facilities with 30 days reduction", "[A1]"),
                    ("Overall total 2024 = 120 + 85 + 60 + 110 = 375 days; 2025 = 95 + 90 + 45 + 80 = 310 days; Total reduction = 375 - 310 = 65 days", "[A1]")
                ],
                "final_answer": "(a) Facilities (reduced by 30 days) | (b) Total reduction = 65 days",
                "reverse_check": "25 - 5 + 15 + 30 = 65 days.",
                "pitfall": "Forgetting that Surgery increased by 5 days."
            }
        ]
    },

    # 4. PIE CHARTS
    "pie-charts": {
        "title": "Pie Charts & Proportional Angles",
        "slug": "pie-charts",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.27 • L2.22",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Pie Chart Calculations & 360° Angle Rules",
            "points": [
                "A full circle has 360 degrees (360°).",
                "Degrees per person/item = 360° ÷ Total Frequency.",
                "Sector Angle = Frequency × (Degrees per item).",
                "Finding frequency from an angle: (Sector Angle ÷ 360) × Total Frequency.",
                "Key fractions of a circle: 90° = 1/4 (25%); 180° = 1/2 (50%); 45° = 1/8 (12.5%); 120° = 1/3 (33.3%)."
            ],
            "calc_tip": "Always check that the angles of all your pie chart sectors add up to exactly 360°!"
        },
        "workout_blocks": [
            {
                "title": "Calculating Sector Angles from Frequencies",
                "instruction": "Work out the angle for each sector (Total circle = 360°):",
                "suffix": "°",
                "items": [
                    ("a", "Total frequency = 36. Frequency of category = 9", "90° ((360 ÷ 36) × 9)"),
                    ("b", "Total frequency = 60. Frequency of category = 15", "90° ((360 ÷ 60) × 15)"),
                    ("c", "Total frequency = 120. Frequency of category = 40", "120° ((360 ÷ 120) × 40)"),
                    ("d", "Total frequency = 72. Frequency of category = 18", "90°"),
                    ("e", "Total frequency = 90. Frequency of category = 30", "120°"),
                    ("f", "Total frequency = 200. Frequency of category = 50", "90° (1/4 of 360)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Healthcare Facility Energy Source Breakdown",
                "stem": "A regional healthcare facility displays its annual electricity sources in a pie chart.<br>The total annual electricity consumption is <strong>720,000 kilowatt-hours (kWh)</strong>.<br>On the pie chart, the sector representing <strong>Rooftop Solar Energy</strong> has an angle of <strong>54°</strong>.<br>Calculate the amount of electricity supplied by solar energy in kWh.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Calculate fraction of circle: 54° ÷ 360° = 0.15 (or 15%)", "[M1]"),
                    ("Multiply fraction by total energy: 0.15 × 720,000 kWh", "[M1]"),
                    ("Solar electricity = 108,000 kWh", "[A1]")
                ],
                "final_answer": "108,000 kWh",
                "reverse_check": "(108,000 ÷ 720,000) × 360° = 54°.",
                "pitfall": "Dividing 720,000 by 54 instead of (54 ÷ 360)."
            }
        ]
    },

    # 5. DATA TABLES
    "data-tables": {
        "title": "Data Tables & Two-Way Tables",
        "slug": "data-tables",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.26 • L2.22",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Two-Way Contingency Tables",
            "points": [
                "Two-way tables categorize data by two distinct criteria (e.g. Gender and Shift, or Treatment and Age).",
                "Row totals: The sum of each row adds up horizontally to the right-hand total.",
                "Column totals: The sum of each column adds up vertically to the bottom total.",
                "Grand Total: Bottom-right corner is the sum of all row totals AND the sum of all column totals.",
                "Work systematically to find cells that have only one missing number in their row or column."
            ],
            "calc_tip": "Double-check by adding both the row totals and column totals to confirm they equal the same grand total."
        },
        "workout_blocks": [
            {
                "title": "Completing Two-Way Contingency Tables",
                "instruction": "Find the missing value using row and column totals:",
                "items": [
                    ("a", "Row: 14 men, 18 women. Row total?", "32"),
                    ("b", "Column: Total is 50. Row 1 is 22. What is Row 2?", "28 (50 - 22)"),
                    ("c", "Row: 45 passed, total was 60. How many failed?", "15 (60 - 45)"),
                    ("d", "Table grand total = 100. Row 1 = 35, Row 2 = 40. Row 3?", "25 (100 - 75)"),
                    ("e", "Column 1 total = 42, Column 2 total = 58. Grand total?", "100"),
                    ("f", "Out of 80 patients, 48 are female. How many male?", "32 (80 - 48)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Healthcare Staff Training Records",
                "stem": "A community healthcare provider tracks mandatory resuscitation certification across <strong>150 healthcare workers</strong>.<br>The two-way table shows:<br>• <strong>Doctors:</strong> 25 Certified, 5 Pending (Total = 30)<br>• <strong>Nurses:</strong> 65 Certified, 15 Pending (Total = 80)<br>• <strong>Healthcare Assistants:</strong> 32 Certified, X Pending (Total = 40)<br>(a) Find the missing number X of Healthcare Assistants with pending certification.<br>(b) What percentage of all 150 workers are fully certified?",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Find X: 40 total HCAs - 32 certified = 8 pending", "[A1]"),
                    ("Calculate total certified: 25 + 65 + 32 = 122 certified workers", "[M1]"),
                    ("Calculate percentage: (122 ÷ 150) × 100 = 81.33% (or 81.3%)", "[A1]")
                ],
                "final_answer": "(a) X = 8 pending | (b) 81.3% certified",
                "reverse_check": "122 certified + 28 pending = 150 total staff.",
                "pitfall": "Calculating percentage of doctors rather than the grand total of 150 workers."
            }
        ]
    }
}
