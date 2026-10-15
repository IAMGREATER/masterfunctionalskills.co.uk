#!/usr/bin/env python3
import json

TOPICS_DOMAIN5 = [
    {
        "filename": "functional-skills-mean-median-mode-and-range.html",
        "clean_topic": "Averages (Mean, Median, Mode) & Range",
        "intro_lead": "Calculate the mean, median, mode, and range for raw data sets, compare distributions using an average AND the range, and interpret workplace performance metrics.",
        "next_file": "functional-skills-estimating-the-mean.html",
        "next_name": "Estimating the Mean",
        "spec_points": [
            ("L1.23 / L2.28", "Calculate the mean, median, mode, and range for a set of quantities."),
            ("L2.29", "Compare two data sets using an appropriate measure of average and the range.")
        ],
        "golden_rules": [
            {
                "icon": "fa-calculator",
                "title": "Golden Rule 1: The Four Statistical Measures Defined",
                "desc": "Mean = Total ÷ Count. Median = Middle value when numbers are put in order. Mode = Most frequent number. Range = Highest minus Lowest (measure of spread, NOT an average!).",
                "badge": "Mean (Sum ÷ N) • Median (Middle) • Mode (Most) • Range (High - Low)"
            },
            {
                "icon": "fa-code-compare",
                "title": "Golden Rule 2: Comparing Two Data Sets Requires TWO Statements",
                "desc": "In Pearson Edexcel exams, a comparison question ALWAYS requires: 1. A comparison of an average (e.g. 'Ward A has a higher mean waiting time than Ward B'). 2. A comparison of consistency using range (e.g. 'Ward B has a smaller range, meaning waiting times are more consistent').",
                "badge": "Statement 1: Compare Average | Statement 2: Compare Range / Consistency"
            }
        ],
        "skills": [
            {
                "title": "Median with an Even Number of Values",
                "summary": "Finding the middle value when there is no single middle number.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Put the data in ascending order:</strong> <em>4, 7, 9, 12, 15, 18.</em></li>
                    <li><strong>Identify the two middle numbers:</strong> For 6 numbers, the 3rd (9) and 4th (12) are the middle pair.</li>
                    <li><strong>Find their midpoint:</strong> Add the two middle numbers and divide by 2: <em>(9 + 12) ÷ 2 = 21 ÷ 2 = 10.5.</em></li>
                  </ol>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Hospital Emergency A&E Triage Waiting Times Comparison",
                "marks": "4 Marks (Pearson Edexcel Level 2)",
                "context": "Healthcare Clinical Performance Management",
                "question": "A hospital trust records the waiting times in minutes for <strong>6 triage patients</strong> on Monday and Tuesday:<br>• Monday: <strong>45, 62, 38, 55, 70, 42</strong><br>• Tuesday has a <strong>mean waiting time of 48 minutes</strong> and a <strong>range of 15 minutes</strong>.<br>(a) Calculate the mean waiting time for Monday.<br>(b) Calculate the range for Monday.<br>(c) Compare the waiting times between Monday and Tuesday.",
                "steps": [
                    ("Step 1", "Calculate Monday Mean (Sum ÷ Count)", "Sum = 45 + 62 + 38 + 55 + 70 + 42 = 312 minutes.<br>Mean = 312 ÷ 6 = 52 minutes.", "M1: Sum and division for mean"),
                    ("Step 2", "Calculate Monday Range (Highest - Lowest)", "Highest = 70, Lowest = 38.<br>Range = 70 - 38 = 32 minutes.", "A1: Accurate range calculation (32 mins)"),
                    ("Step 3", "Compare Average (Statement 1)", "Monday had a higher mean waiting time than Tuesday (52 mins vs 48 mins), meaning patients waited longer on average on Monday.", "A1: Valid average comparison"),
                    ("Step 4", "Compare Consistency using Range (Statement 2)", "Tuesday had a much smaller range than Monday (15 mins vs 32 mins), meaning waiting times on Tuesday were more consistent.", "A1: Valid range consistency comparison")
                ],
                "final_answer": "(a) Monday Mean = 52 mins | (b) Monday Range = 32 mins | (c) Tuesday had shorter average waits (48 vs 52 mins) and more consistent wait times (range 15 vs 32 mins).",
                "tutor_tip": "Notice: Smaller range ALWAYS means MORE CONSISTENT (or less spread out). Larger range means MORE VARIABLE."
            }
        ],
        "examiner_traps": [
            {
                "title": "Calling the Range an 'Average'",
                "desc": "The range is a measure of SPREAD, not an average. Never write 'The average range was 32'.",
                "fix": "Always say 'The range was 32 minutes, indicating greater variability'."
            }
        ],
        "practice_questions": [
            {
                "marks": "3 Marks",
                "question": "Find the median, mode, and range for: <strong>14, 18, 12, 14, 22, 19, 14</strong>.",
                "solution_steps": "1. In order: 12, 14, 14, 14, 18, 19, 22.<br>2. Middle (4th) number = 14 (Median).<br>3. Most frequent = 14 (Mode).<br>4. Range = 22 - 12 = 10.",
                "correct_answer": "Median = 14, Mode = 14, Range = 10",
                "tutor_tip": "Put numbers in order first before identifying the median."
            }
        ]
    },
    {
        "filename": "functional-skills-estimating-the-mean.html",
        "clean_topic": "Estimating the Mean from Grouped Data",
        "intro_lead": "Calculate estimated means from grouped frequency tables using midpoints (mid-interval values), multiply by frequencies (fx), and divide by total frequency (Σfx ÷ Σf).",
        "next_file": "functional-skills-grouped-data.html",
        "next_name": "Grouped Frequency Tables",
        "spec_points": [
            ("L2.30", "Estimate the mean of grouped frequency distributions using class midpoints.")
        ],
        "golden_rules": [
            {
                "icon": "fa-calculator",
                "title": "Golden Rule 1: The 4-Step Grouped Mean Formula (Σfx ÷ Σf)",
                "desc": "1. Find the Midpoint (x) of each group: (Lower + Upper) ÷ 2. 2. Multiply each Midpoint by Frequency: f × x = fx. 3. Sum all fx values (Σfx). 4. Divide by Total Frequency (Σf).",
                "badge": "Estimated Mean = Total fx ÷ Total Frequency (Σf)"
            },
            {
                "icon": "fa-circle-exclamation",
                "title": "Golden Rule 2: NEVER Divide by the Number of Groups",
                "desc": "If there are 4 class intervals and 50 total patients, you divide by 50 (the total frequency), NEVER by 4! Dividing by 4 is the most fatal exam error on this topic.",
                "badge": "Divide by Total People/Frequency (Σf), NOT Number of Rows"
            }
        ],
        "skills": [
            {
                "title": "Why is it Called an 'Estimated' Mean?",
                "summary": "Because raw individual values are grouped into intervals.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">When data is in groups like <em>'10 to 20 minutes'</em>, we do not know whether the 8 patients waited 11 minutes or 19 minutes. We assume they all waited at the midpoint (15 minutes). Because this assumes an average within each group, the final calculated mean is an <strong>estimate</strong>.</p>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Care Home Call Bell Response Times Estimated Mean",
                "marks": "4 Marks (Pearson Edexcel Level 2)",
                "context": "Residential Care Quality Auditing",
                "question": "A care home audits the response times in seconds for <strong>40 emergency call bells</strong>:<br>• 0 to 30s: <strong>6 calls</strong><br>• 30 to 60s: <strong>14 calls</strong><br>• 60 to 90s: <strong>12 calls</strong><br>• 90 to 120s: <strong>8 calls</strong><br>Calculate an estimate of the mean call bell response time.",
                "steps": [
                    ("Step 1", "Find the midpoint (x) of each interval", "0 to 30: (0 + 30) ÷ 2 = 15s<br>30 to 60: (30 + 60) ÷ 2 = 45s<br>60 to 90: (60 + 90) ÷ 2 = 75s<br>90 to 120: (90 + 120) ÷ 2 = 105s", "M1: Finding correct midpoints"),
                    ("Step 2", "Multiply each Midpoint by Frequency (fx)", "15 × 6 = 90<br>45 × 14 = 630<br>75 × 12 = 900<br>105 × 8 = 840", "M1: Multiplying midpoints by frequencies"),
                    ("Step 3", "Sum the fx column (Σfx) and confirm total frequency (Σf)", "Σfx = 90 + 630 + 900 + 840 = 2,460.<br>Total frequency Σf = 6 + 14 + 12 + 8 = 40 calls.", "M1: Summing fx and total frequency"),
                    ("Step 4", "Divide Σfx by Σf to calculate estimated mean", "Estimated Mean = 2,460 ÷ 40 = 61.5 seconds.", "A1: Accurate estimated mean (61.5s)")
                ],
                "final_answer": "Estimated Mean = 61.5 seconds",
                "tutor_tip": "Notice that 61.5 seconds falls in the middle of the response data (between 30 and 90s), which confirms your answer is completely plausible."
            }
        ],
        "examiner_traps": [
            {
                "title": "Dividing by 4 Rows Instead of 40 Calls",
                "desc": "Doing 2,460 ÷ 4 = 615 seconds is impossible because no call took longer than 120 seconds!",
                "fix": "Sanity check: the mean MUST fall inside the range of your data (between 0 and 120)."
            }
        ],
        "practice_questions": [
            {
                "marks": "3 Marks",
                "question": "A delivery firm records parcel weights: 0–2 kg (freq 5), 2–4 kg (freq 10), 4–6 kg (freq 5). Calculate an estimate of the mean parcel weight.",
                "solution_steps": "1. Midpoints: 1 kg, 3 kg, 5 kg.<br>2. fx: (1×5) + (3×10) + (5×5) = 5 + 30 + 25 = 60.<br>3. Total parcels = 5 + 10 + 5 = 20.<br>4. Estimated mean = 60 ÷ 20 = 3 kg.",
                "correct_answer": "3 kg",
                "tutor_tip": "Midpoints are 1, 3, 5; total fx is 60; total frequency is 20."
            }
        ]
    },
    {
        "filename": "functional-skills-grouped-data.html",
        "clean_topic": "Grouped Frequency Tables",
        "intro_lead": "Organize continuous and discrete data into grouped frequency distributions, determine modal class intervals, and extract median groups in workplace audits.",
        "next_file": "functional-skills-data-tables.html",
        "next_name": "Data Tables",
        "spec_points": [
            ("L1.24 / L2.30", "Represent discrete and continuous data in grouped frequency tables and identify modal class.")
        ],
        "golden_rules": [
            {
                "icon": "fa-table",
                "title": "Golden Rule 1: Modal Class is the Interval with the HIGHEST Frequency",
                "desc": "The modal class is the interval with the greatest number of occurrences. Write the FULL interval (e.g. '20 < t ≤ 30'), NOT just the frequency number.",
                "badge": "Modal Class = Interval with highest frequency"
            },
            {
                "icon": "fa-ruler-combined",
                "title": "Golden Rule 2: Continuous Data Inequality Signs (< and ≤)",
                "desc": "In continuous groups like '10 < w ≤ 20', a weight of exactly 20.0 kg belongs in this group. A weight of 20.1 kg belongs in the next group ('20 < w ≤ 30').",
                "badge": "≤ includes the boundary number"
            }
        ],
        "skills": [
            {
                "title": "Locating the Median Class Interval",
                "summary": "Using running cumulative frequency to locate the middle value.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Find total frequency (N):</strong> e.g. N = 60.</li>
                    <li><strong>Find the middle position:</strong> N ÷ 2 = 60 ÷ 2 = 30th value.</li>
                    <li><strong>Keep a running total of frequencies:</strong> Look for the group that contains the 30th value.</li>
                  </ol>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Hospital Phlebotomy Outpatient Waiting Time Distribution",
                "marks": "3 Marks (Pearson Edexcel Level 2)",
                "context": "Clinical Phlebotomy Clinic Auditing",
                "question": "A blood testing clinic records waiting times for <strong>80 outpatients</strong>:<br>• 0 < t ≤ 10 mins: 14 patients<br>• 10 < t ≤ 20 mins: 38 patients<br>• 20 < t ≤ 30 mins: 22 patients<br>• 30 < t ≤ 40 mins: 6 patients<br>(a) State the modal class interval.<br>(b) In which class interval does the median waiting time lie?",
                "steps": [
                    ("Step 1", "Identify the group with highest frequency for modal class", "The highest frequency is 38 patients, which corresponds to the interval 10 < t ≤ 20 mins.", "A1: Correct modal class interval"),
                    ("Step 2", "Calculate the median position (N ÷ 2)", "Total patients = 80. Median position = 80 ÷ 2 = 40th patient.", "M1: Median position calculation"),
                    ("Step 3", "Determine which interval contains the 40th patient", "Cumulative frequencies:<br>Group 1: 14 patients (patients 1 to 14)<br>Group 2: 14 + 38 = 52 patients (patients 15 to 52).<br>Since 40 lies between 15 and 52, the median lies in the interval 10 < t ≤ 20 mins.", "A1: Accurate median interval identification")
                ],
                "final_answer": "(a) Modal Class = 10 < t ≤ 20 mins | (b) Median Class = 10 < t ≤ 20 mins.",
                "tutor_tip": "Always write the full inequality notation (10 < t ≤ 20) as your answer, not just '38'."
            }
        ],
        "examiner_traps": [
            {
                "title": "Writing the Frequency Instead of the Interval",
                "desc": "Answering '38' instead of '10 < t ≤ 20 mins' for the modal class is an automatic error.",
                "fix": "Modal class is the GROUP, not the number of times it happened."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A delivery firm records parcel counts: 1–5 kg (freq 8), 6–10 kg (freq 15), 11–15 kg (freq 7). State the modal class.",
                "solution_steps": "1. Frequencies: 8, 15, 7.<br>2. Highest frequency is 15.<br>3. Modal class is 6–10 kg.",
                "correct_answer": "6–10 kg",
                "tutor_tip": "Identify the interval with the highest frequency (15)."
            }
        ]
    },
    {
        "filename": "functional-skills-data-tables.html",
        "clean_topic": "Data Tables & Two-Way Tables",
        "intro_lead": "Extract, cross-reference, and complete information in complex two-way tables, flight schedules, mileage charts, and multi-factor staff rotas.",
        "next_file": "functional-skills-bar-charts.html",
        "next_name": "Bar Charts",
        "spec_points": [
            ("L1.24 / L2.31", "Extract and interpret information from complex data tables, including two-way frequency tables.")
        ],
        "golden_rules": [
            {
                "icon": "fa-table-cells",
                "title": "Golden Rule 1: Row Totals and Column Totals Must Cross-Check",
                "desc": "In any two-way table, the sum of the row totals MUST equal the sum of the column totals. This grand total in the bottom-right corner confirms accuracy.",
                "badge": "Sum of Row Totals = Sum of Column Totals = Grand Total"
            },
            {
                "icon": "fa-magnifying-glass",
                "title": "Golden Rule 2: Intersect Rows and Columns with Your Finger/Ruler",
                "desc": "To find the data point for 'Male Day Shift Nurses', place one finger on 'Male' and one on 'Day Shift', and bring them together at the intersection cell.",
                "badge": "Row Header × Column Header = Intersection Value"
            }
        ],
        "skills": [
            {
                "title": "Completing a Two-Way Table with Missing Values",
                "summary": "Working backwards using row and column totals.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">To solve missing cells in a two-way table:</p>
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li>Find a row or column that has only ONE missing value.</li>
                    <li>Subtract the known values from the total for that row/column.</li>
                    <li>Fill in that cell and repeat until all cells are complete.</li>
                  </ol>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Hospital Clinical Shift Staff Attendance Two-Way Table",
                "marks": "3 Marks (Pearson Edexcel Level 2)",
                "context": "Healthcare Staffing Workforce Management",
                "question": "A hospital ward employs <strong>60 nursing staff</strong> across Day and Night shifts. <strong>35 staff are Registered Nurses (RNs)</strong> and the rest are Healthcare Assistants (HCAs). <strong>20 RNs work Day shifts</strong>. In total, <strong>38 staff work Day shifts</strong>.<br>Complete the two-way table and find how many HCAs work Night shifts.",
                "steps": [
                    ("Step 1", "Calculate total HCAs", "Total HCAs = 60 (grand total) - 35 (RNs) = 25 HCAs.", "M1: Total HCA deduction"),
                    ("Step 2", "Calculate Day HCAs and Night RNs", "Day HCAs = 38 (total Day) - 20 (Day RNs) = 18 HCAs.<br>Night RNs = 35 (total RNs) - 20 (Day RNs) = 15 RNs.", "M1: Row/column deduction"),
                    ("Step 3", "Calculate Night HCAs", "Night HCAs = 25 (total HCAs) - 18 (Day HCAs) = 7 HCAs.<br>(Check: Total Night = 60 - 38 = 22 staff; 15 RNs + 7 HCAs = 22. Confirmed).", "A1: Accurate Night HCA count (7)")
                ],
                "final_answer": "7 Healthcare Assistants work Night shifts.",
                "tutor_tip": "Notice how the cross-check verified everything: 15 RNs + 7 HCAs = 22 Night staff. 38 Day + 22 Night = 60 total staff."
            }
        ],
        "examiner_traps": [
            {
                "title": "Guessing Missing Numbers Without Checking Totals",
                "desc": "Failing to check that rows and columns sum to the stated totals leads to multiple cascading errors.",
                "fix": "Always sum every row and column to check that they match before moving on."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "In a logistics hub of 100 drivers, 65 drive daytime routes and 35 drive night routes. 40 of the daytime drivers operate articulated lorries, and 20 of the night drivers operate articulated lorries. How many total drivers operate rigid vans?",
                "solution_steps": "1. Total articulated drivers = 40 + 20 = 60.<br>2. Total van drivers = 100 - 60 = 40 drivers.",
                "correct_answer": "40 drivers",
                "tutor_tip": "Subtract the total articulated drivers from the grand total (100 - 60 = 40)."
            }
        ]
    }
]

# Write out domain 5
with open("/home/subi/Projects/masterfunctionalskills.co.uk/maths_domain5_stats_prob.py", "w", encoding="utf-8") as f:
    f.write("#!/usr/bin/env python3\n")
    f.write('"""Maths Domain 5: Statistics & Probability (4 Core Topics)"""\n\n')
    f.write("TOPICS_DOMAIN5 = " + repr(TOPICS_DOMAIN5) + "\n")

print(f"Domain 5 written with {len(TOPICS_DOMAIN5)} topics!")
