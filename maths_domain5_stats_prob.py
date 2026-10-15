#!/usr/bin/env python3
"""Maths Domain 5: Statistics & Probability (11 Core Topics)"""

TOPICS_DOMAIN5 = [
    {
        'filename': 'functional-skills-mean-median-mode-and-range.html',
        'clean_topic': 'Averages (Mean, Median, Mode) & Range',
        'intro_lead': 'Calculate the mean, median, mode, and range for raw data sets, find missing data values from a given mean, and compare distributions using an average AND the range.',
        'next_file': 'functional-skills-estimating-the-mean.html',
        'next_name': 'Estimating the Mean',
        'spec_points': [
            ('L1.23 / L2.28', 'Calculate the mean, median, mode, and range for a discrete set of quantities.'),
            ('L2.29', 'Compare two data sets using an appropriate measure of average (mean or median) and the range.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-calculator',
                'title': 'Golden Rule 1: The Four Statistical Measures Defined',
                'desc': 'Mean = Total Sum ÷ Number of Values. Median = Exact middle value AFTER putting numbers in ascending order. Mode = Most frequent value. Range = Highest − Lowest (a measure of spread/consistency, NOT an average!).',
                'badge': 'Mean (Sum ÷ N) • Median (Ordered Middle) • Mode (Most) • Range (High − Low)'
            },
            {
                'icon': 'fa-code-compare',
                'title': 'Golden Rule 2: Comparing Two Data Sets Requires TWO Statements',
                'desc': "In Pearson Edexcel exams, a comparison question ALWAYS requires: 1. Compare an average in context (e.g. 'Ward A has a higher mean waiting time than Ward B'). 2. Compare consistency using the range (e.g. 'Ward B has a smaller range, meaning waiting times are more consistent').",
                'badge': 'Statement 1: Compare Average • Statement 2: Compare Range (Smaller = More Consistent)'
            }
        ],
        'skills': [
            {
                'title': 'Median with an Odd vs Even Number of Values',
                'summary': 'Ordering data first and finding the midpoint when two numbers share the middle.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Step 1 — Order the Numbers:</strong> Always sort from smallest to largest first!</li>
                    <li><strong>Odd Count (e.g. 7 numbers):</strong> Cross off equally from both ends; the 4th number is the exact median.</li>
                    <li><strong>Even Count (e.g. 6 numbers: 4, 7, 9, 12, 15, 18):</strong> Add the two middle numbers (9 and 12) and divide by 2: <em>(9 + 12) &divide; 2 = 21 &divide; 2 = <strong>10.5</strong></em>.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Working Backwards from a Given Mean (Reverse Mean)',
                'summary': 'Finding a missing score or target figure when the required mean is known.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">Because <strong>Mean = Total &divide; Count</strong>, we can reverse the formula to <strong>Total = Mean &times; Count</strong>:</p>
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li>Multiply the target mean by the total number of items: e.g. Mean of 5 days is 40 parcels &rarr; <strong>Total = 5 &times; 40 = 200 parcels</strong>.</li>
                    <li>Add up the known 4 days: e.g. 38 + 42 + 35 + 41 = <strong>156 parcels</strong>.</li>
                    <li>Subtract to find the missing 5th day: 200 &minus; 156 = <strong>44 parcels</strong>.</li>
                  </ol>
                </div>
                """
            },
            {
                'title': 'Choosing Between Mean, Median, and Mode (Handling Outliers)',
                'summary': 'Knowing which average best represents skewed workplace data.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:left;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Measure</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Best Used When...</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Limitation</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">Mean</td><td style="padding:8px; border:1px solid #cbd5e1;">Data is evenly spread with no extreme outliers (uses every value)</td><td style="padding:8px; border:1px solid #cbd5e1;">Distorted by one extreme high or low outlier</td></tr>
                      <tr><td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">Median</td><td style="padding:8px; border:1px solid #cbd5e1;">Salaries or house prices where 1 extreme outlier would skew the mean</td><td style="padding:8px; border:1px solid #cbd5e1;">Ignores the exact size of outer values</td></tr>
                      <tr><td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">Mode</td><td style="padding:8px; border:1px solid #cbd5e1;">Shoe/uniform sizes or categorical stock orders (most popular item)</td><td style="padding:8px; border:1px solid #cbd5e1;">May be no mode or more than one mode</td></tr>
                    </tbody>
                  </table>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Paramedic Crew Response Time Audit (Level 1 Foundation)',
                'marks': '3 Marks (Pearson Edexcel Level 1)',
                'context': 'Ambulance Dispatch Performance',
                'question': 'An ambulance station logs response times (in minutes) for <strong>7 emergency calls</strong>:<br><strong>8, 12, 7, 15, 8, 11, 9</strong><br>(a) Find the mode.<br>(b) Find the median.<br>(c) Calculate the mean and the range.',
                'steps': [
                    ('Step 1', 'Identify the mode and sort data in ascending order', 'Ordered list: 7, 8, 8, 9, 11, 12, 15.<br>Mode (most frequent) = 8 minutes.', 'A1: Correct mode (8 mins)'),
                    ('Step 2', 'Extract the middle (4th) value for the median', 'The 4th value in the ordered list of 7 numbers is 9 minutes.', 'A1: Correct median (9 mins)'),
                    ('Step 3', 'Calculate Mean (Sum ÷ 7) and Range (High − Low)', 'Sum = 7 + 8 + 8 + 9 + 11 + 12 + 15 = 70.<br>Mean = 70 ÷ 7 = 10 minutes.<br>Range = 15 − 7 = 8 minutes.', 'M1 / A1: Accurate mean (10 mins) and range (8 mins)')
                ],
                'final_answer': '(a) Mode = 8 mins | (b) Median = 9 mins | (c) Mean = 10 mins, Range = 8 mins',
                'tutor_tip': 'Always write your ordered list down and count that you still have all 7 numbers before picking the middle value!'
            },
            {
                'title': 'Hospital Emergency A&E Triage Waiting Times Comparison (Level 2 Multi-Step)',
                'marks': '4 Marks (Pearson Edexcel Level 2)',
                'context': 'Healthcare Clinical Performance Management',
                'question': 'A hospital trust records the waiting times in minutes for <strong>6 triage patients</strong> on Monday and compares them with Tuesday’s summary:<br>• Monday: <strong>45, 62, 38, 55, 70, 42</strong><br>• Tuesday Summary: <strong>Mean = 48 minutes, Range = 15 minutes</strong>.<br>Calculate the mean and range for Monday, and write two comparative statements comparing waiting times on Monday and Tuesday.',
                'steps': [
                    ('Step 1', 'Calculate Monday Mean (Sum ÷ 6)', 'Sum = 45 + 62 + 38 + 55 + 70 + 42 = 312 minutes.<br>Mean = 312 ÷ 6 = 52 minutes.', 'M1: Accurate Monday mean (52 mins)'),
                    ('Step 2', 'Calculate Monday Range (Highest − Lowest)', 'Range = 70 − 38 = 32 minutes.', 'A1: Accurate Monday range (32 mins)'),
                    ('Step 3', 'Statement 1 — Compare Averages in Context', 'Tuesday had a lower mean waiting time than Monday (48 mins vs 52 mins), so patients waited less time on average on Tuesday.', 'A1: Valid contextual average comparison'),
                    ('Step 4', 'Statement 2 — Compare Consistency using Range', 'Tuesday had a smaller range than Monday (15 mins vs 32 mins), meaning waiting times on Tuesday were much more consistent.', 'A1: Valid range consistency comparison')
                ],
                'final_answer': 'Monday Mean = 52 mins, Range = 32 mins. Tuesday had shorter average waits (48 vs 52 mins) and more consistent wait times (range 15 vs 32 mins).',
                'tutor_tip': 'Smaller range ALWAYS means MORE CONSISTENT. Cite the actual numbers (52 vs 48 and 32 vs 15) in your sentences.'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Picking the Middle Number Without Putting the List in Order First',
                'desc': 'Selecting 55 or 38 from the raw unsorted list instead of sorting from smallest to largest first forfeits all median marks.',
                'fix': 'Always write "Ordered:" and tick off each number as you rewrite it.'
            },
            {
                'title': "Calling the Range an 'Average'",
                'desc': 'The range measures SPREAD (consistency), not average performance.',
                'fix': 'Never write "The average range was..."; write "The range was..., showing greater consistency."'
            }
        ],
        'practice_questions': [
            {
                'marks': '3 Marks',
                'question': 'Find the median, mode, and range for these 8 daily parcel deliveries: <strong>14, 18, 12, 14, 22, 19, 14, 16</strong>.',
                'solution_steps': '1. Ordered: 12, 14, 14, 14, 16, 18, 19, 22.<br>2. Median (4th & 5th values: 14 and 16): (14 + 16) ÷ 2 = 15.<br>3. Mode (most frequent) = 14.<br>4. Range = 22 − 12 = 10.',
                'correct_answer': 'Median = 15, Mode = 14, Range = 10',
                'tutor_tip': 'For 8 numbers, average the 4th and 5th ordered values for the median.'
            },
            {
                'marks': '3 Marks',
                'question': 'A student needs a <strong>mean score of 75 marks</strong> across <strong>5 mock tests</strong> to qualify for an award. Their first 4 test scores are <strong>72, 68, 81, and 74</strong>. Calculate the score they must achieve on the 5th test.',
                'solution_steps': '1. Required total across 5 tests = 5 × 75 = 375 marks.<br>2. Sum of first 4 tests = 72 + 68 + 81 + 74 = 295 marks.<br>3. Required 5th test score = 375 − 295 = 80 marks.',
                'correct_answer': '80 marks',
                'tutor_tip': 'Use Total = Mean × Count (75 × 5 = 375) and subtract the known 4 scores.'
            },
            {
                'marks': '3 Marks',
                'question': 'A clinic employs 4 receptionists earning <strong>£21,000, £22,000, £22,000, and £23,000</strong>, plus 1 consultant surgeon earning <strong>£112,000</strong>.<br>(a) Calculate the mean salary and the median salary of the 5 staff.<br>(b) Explain which average is fairer to represent a typical worker at the clinic.',
                'solution_steps': '1. Total salary = 21,000 + 22,000 + 22,000 + 23,000 + 112,000 = £200,000. Mean = £200,000 ÷ 5 = £40,000.<br>2. Median (3rd ordered value) = £22,000.<br>3. The median (£22,000) is fairer because the mean (£40,000) is heavily skewed upward by the consultant’s £112,000 outlier salary.',
                'correct_answer': '(a) Mean = £40,000, Median = £22,000 | (b) Median, as it is not distorted by the £112,000 outlier',
                'tutor_tip': 'Whenever there is an extreme outlier, the median is the best average to choose.'
            }
        ]
    },
    {
        'filename': 'functional-skills-estimating-the-mean.html',
        'clean_topic': 'Estimating the Mean from Grouped Data',
        'intro_lead': 'Calculate estimated means from grouped frequency tables using class midpoints (x), multiply by frequencies (fx), and divide by total frequency (Σfx ÷ Σf).',
        'next_file': 'functional-skills-grouped-data.html',
        'next_name': 'Grouped Frequency Tables',
        'spec_points': [
            ('L2.30', 'Estimate the mean of a grouped frequency distribution from discrete or continuous data using class midpoints.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-calculator',
                'title': 'Golden Rule 1: The 4-Step Grouped Mean Formula (Σfx ÷ Σf)',
                'desc': '1. Find the Midpoint (x) of each group: (Lower + Upper) ÷ 2. 2. Multiply each Midpoint by its Frequency: f × x = fx. 3. Add up the fx column (Σfx). 4. Divide Σfx by the Total Frequency (Σf).',
                'badge': 'Estimated Mean = Total fx (Σfx) ÷ Total Frequency (Σf)'
            },
            {
                'icon': 'fa-circle-exclamation',
                'title': 'Golden Rule 2: NEVER Divide by the Number of Rows/Groups!',
                'desc': 'If there are 4 class intervals and 50 total patients, you MUST divide by 50 (the total frequency Σf), NEVER by 4! Your final answer must lie comfortably inside the lowest and highest group boundaries.',
                'badge': 'Divide by Total Frequency (Σf), NEVER by Number of Rows'
            }
        ],
        'skills': [
            {
                'title': 'Finding Class Midpoints (x) & Why It Is an Estimate',
                'summary': 'Averaging the lower and upper bounds of each interval.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">To find the midpoint of any interval, <strong>add the two boundary numbers and divide by 2</strong>:</p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>0 &lt; t &le; 15:</strong> (0 + 15) &divide; 2 = <strong>7.5</strong></li>
                    <li><strong>15 &lt; t &le; 30:</strong> (15 + 30) &divide; 2 = <strong>22.5</strong></li>
                    <li><strong>Why is it an "Estimate"?</strong> We do not know the exact individual values inside each group, so we assume every item in a group equals that group's midpoint.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Setting Up the 4-Column Exam Working Table (Group | f | x | fx)',
                'summary': 'How to structure your working table to guarantee all 4 marks.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:center;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Wait Time (mins)</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Frequency (f)</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Midpoint (x)</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">f &times; x (fx)</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1;">0 to 10</td><td style="padding:6px; border:1px solid #cbd5e1;">6</td><td style="padding:6px; border:1px solid #cbd5e1;">5</td><td style="padding:6px; border:1px solid #cbd5e1;">30</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1;">10 to 20</td><td style="padding:6px; border:1px solid #cbd5e1;">14</td><td style="padding:6px; border:1px solid #cbd5e1;">15</td><td style="padding:6px; border:1px solid #cbd5e1;">210</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1;">20 to 30</td><td style="padding:6px; border:1px solid #cbd5e1;">10</td><td style="padding:6px; border:1px solid #cbd5e1;">25</td><td style="padding:6px; border:1px solid #cbd5e1;">250</td></tr>
                      <tr style="background:#e0f2fe; font-weight:800; color:#0369a1;"><td style="padding:6px; border:1px solid #cbd5e1;">Totals</td><td style="padding:6px; border:1px solid #cbd5e1;">&Sigma;f = 30</td><td style="padding:6px; border:1px solid #cbd5e1;">—</td><td style="padding:6px; border:1px solid #cbd5e1;">&Sigma;fx = 490</td></tr>
                    </tbody>
                  </table>
                  <p style="margin-top:10px; font-weight:700; color:#0f172a;">Estimated Mean = 490 &divide; 30 = 16.33 minutes.</p>
                </div>
                """
            },
            {
                'title': 'Unequal Class Widths & Comparing Estimated Means to Targets',
                'summary': 'Handling wider final intervals (e.g. 40 to 80) and evaluating SLA performance.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Watch Out for Unequal Intervals:</strong> Exam tables often widen the last row (e.g. 0–10, 10–20, 20–40, 40–80). Never guess midpoints by pattern—always compute <strong>(Lower + Upper) &divide; 2</strong> for every single row!</li>
                    <li><strong>Plausibility Check:</strong> If your groups run from 0 to 80, your estimated mean MUST be between 0 and 80.</li>
                  </ul>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Care Home Call Bell Response Times Estimated Mean (Level 2 Core)',
                'marks': '4 Marks (Pearson Edexcel Level 2)',
                'context': 'Residential Care Quality Auditing',
                'question': 'A care home audits the response times in seconds for <strong>40 emergency call bells</strong>:<br>• 0 to 30s: <strong>6 calls</strong><br>• 30 to 60s: <strong>14 calls</strong><br>• 60 to 90s: <strong>12 calls</strong><br>• 90 to 120s: <strong>8 calls</strong><br>Calculate an estimate of the mean call bell response time.',
                'steps': [
                    ('Step 1', 'Find the midpoint (x) of each interval', '0–30: 15s | 30–60: 45s | 60–90: 75s | 90–120: 105s.', 'M1: Correct class midpoints'),
                    ('Step 2', 'Multiply each Midpoint by Frequency (fx)', '(15 × 6 = 90) + (45 × 14 = 630) + (75 × 12 = 900) + (105 × 8 = 840).', 'M1: Multiplying midpoints by frequencies'),
                    ('Step 3', 'Sum fx (Σfx) and verify total frequency (Σf)', 'Σfx = 90 + 630 + 900 + 840 = 2,460.<br>Total frequency Σf = 6 + 14 + 12 + 8 = 40 calls.', 'M1: Summing fx (2,460)'),
                    ('Step 4', 'Divide Σfx by Σf', 'Estimated Mean = 2,460 ÷ 40 = 61.5 seconds.', 'A1: Accurate estimated mean (61.5s)')
                ],
                'final_answer': '61.5 seconds',
                'tutor_tip': '61.5 seconds sits right in the middle of the 0–120s range, confirming the calculation is sensible.'
            },
            {
                'title': 'Outpatient Pharmacy Prescription Wait Target Decision (Level 2 Multi-Step)',
                'marks': '4 Marks (Pearson Edexcel Level 2)',
                'context': 'Hospital Outpatient Pharmacy SLA Audit',
                'question': 'A hospital pharmacy charter states that the mean prescription waiting time must be <strong>under 18 minutes</strong>. An audit of <strong>50 prescriptions</strong> shows:<br>• 0 &lt; t &le; 10 mins: <strong>12 prescriptions</strong><br>• 10 &lt; t &le; 20 mins: <strong>23 prescriptions</strong><br>• 20 &lt; t &le; 30 mins: <strong>10 prescriptions</strong><br>• 30 &lt; t &le; 50 mins: <strong>5 prescriptions</strong><br>Calculate an estimate of the mean waiting time and state whether the pharmacy met its charter target.',
                'steps': [
                    ('Step 1', 'Calculate midpoints (noting the wider 30–50 final interval!)', 'Midpoints: 5, 15, 25, and (30 + 50) ÷ 2 = 40 mins.', 'M1: Accurate midpoints including 40'),
                    ('Step 2', 'Compute fx and sum Σfx', '(12 × 5 = 60) + (23 × 15 = 345) + (10 × 25 = 250) + (5 × 40 = 200) = 855.', 'M1: Accurate Σfx = 855'),
                    ('Step 3', 'Divide by total prescriptions (50) and compare with 18 mins', 'Estimated Mean = 855 ÷ 50 = 17.1 minutes.<br>Since 17.1 mins < 18 mins, YES, the pharmacy met its charter target.', 'M1 / A1: 17.1 minutes and valid YES conclusion')
                ],
                'final_answer': 'Estimated Mean = 17.1 minutes — Yes, the pharmacy met its target (< 18 mins)',
                'tutor_tip': 'Watch the last interval carefully: 30 to 50 has a width of 20, so its midpoint is 40, not 35!'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Dividing by the Number of Groups (4) Instead of Total Frequency (40)',
                'desc': 'Computing 2,460 ÷ 4 = 615 seconds is impossible because no call lasted longer than 120 seconds!',
                'fix': 'Always cross-out the midpoint total—only sum the Frequency (f) column and the (fx) column.'
            },
            {
                'title': 'Dividing Total Frequency by Number of Groups',
                'desc': 'Doing 40 ÷ 4 = 10 completely ignores the time intervals and scores 0 marks.',
                'fix': 'You must calculate Midpoint × Frequency for every row.'
            }
        ],
        'practice_questions': [
            {
                'marks': '4 Marks',
                'question': 'A courier depot records the weights of <strong>25 parcels</strong>:<br>• 0 &lt; w &le; 2 kg: <strong>5 parcels</strong><br>• 2 &lt; w &le; 4 kg: <strong>12 parcels</strong><br>• 4 &lt; w &le; 6 kg: <strong>8 parcels</strong><br>Calculate an estimate of the mean parcel weight.',
                'solution_steps': '1. Midpoints: 1 kg, 3 kg, 5 kg.<br>2. fx: (5 × 1 = 5) + (12 × 3 = 36) + (8 × 5 = 40) = 81 kg.<br>3. Total frequency = 25.<br>4. Estimated Mean = 81 ÷ 25 = 3.24 kg.',
                'correct_answer': '3.24 kg',
                'tutor_tip': 'Sum fx = 81; divide by 25 parcels = 3.24 kg.'
            },
            {
                'marks': '4 Marks',
                'question': 'A solar array logs daily energy output over <strong>30 days</strong>:<br>• 10 to 20 kWh: <strong>6 days</strong><br>• 20 to 30 kWh: <strong>15 days</strong><br>• 30 to 40 kWh: <strong>9 days</strong><br>Calculate an estimate of the mean daily energy output.',
                'solution_steps': '1. Midpoints: 15, 25, 35.<br>2. fx: (6 × 15 = 90) + (15 × 25 = 375) + (9 × 35 = 315) = 780 kWh.<br>3. Estimated Mean = 780 ÷ 30 = 26 kWh.',
                'correct_answer': '26 kWh',
                'tutor_tip': '780 ÷ 30 = 26 kWh.'
            },
            {
                'marks': '4 Marks',
                'question': 'A call center audits <strong>80 customer calls</strong>:<br>• 0 &lt; t &le; 4 mins: <strong>20 calls</strong><br>• 4 &lt; t &le; 8 mins: <strong>36 calls</strong><br>• 8 &lt; t &le; 12 mins: <strong>16 calls</strong><br>• 12 &lt; t &le; 20 mins: <strong>8 calls</strong><br>Calculate an estimate of the mean call duration in minutes.',
                'solution_steps': '1. Midpoints: 2, 6, 10, 16 (note 12 to 20 midpoint is 16!).<br>2. fx: (20 × 2 = 40) + (36 × 6 = 216) + (16 × 10 = 160) + (8 × 16 = 128) = 544.<br>3. Estimated Mean = 544 ÷ 80 = 6.8 minutes.',
                'correct_answer': '6.8 minutes',
                'tutor_tip': 'Check the final group (12 to 20): (12 + 20) ÷ 2 = 16.'
            }
        ]
    },
    {
        'filename': 'functional-skills-grouped-data.html',
        'clean_topic': 'Grouped Frequency Tables',
        'intro_lead': 'Organize continuous and discrete data into grouped frequency distributions, determine modal class intervals, locate the median class interval, and calculate percentage proportions.',
        'next_file': 'functional-skills-data-tables.html',
        'next_name': 'Data Tables',
        'spec_points': [
            ('L1.24 / L2.30', 'Group discrete and continuous data into non-overlapping class intervals and identify the modal class and median class interval.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-table',
                'title': 'Golden Rule 1: Modal Class is the Interval Label with the HIGHEST Frequency',
                'desc': "The modal class is the group that has the largest frequency. Always write the FULL interval label (e.g. '10 < t ≤ 20'), NEVER just the frequency number!",
                'badge': 'Modal Class = Copy the exact group interval with the highest frequency'
            },
            {
                'icon': 'fa-ruler-combined',
                'title': 'Golden Rule 2: Non-Overlapping Inequality Signs (< and ≤)',
                'desc': "In continuous groups like '10 < w ≤ 20' and '20 < w ≤ 30', the symbol '≤' means 'less than or equal to'. Therefore, an exact boundary value of 20.0 belongs in the '10 < w ≤ 20' group, NOT the '20 < w ≤ 30' group.",
                'badge': '≤ includes the boundary number • < strictly excludes it'
            }
        ],
        'skills': [
            {
                'title': 'Designing Non-Overlapping Discrete vs Continuous Intervals',
                'summary': 'Why intervals like "10–20" and "20–30" fail for continuous measurements.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Discrete Whole Numbers (e.g. people, items):</strong> Use non-overlapping integer ranges: <strong>0–9, 10–19, 20–29, 30–39</strong>.</li>
                    <li><strong>Continuous Measurements (e.g. time, weight, length):</strong> Use strict inequalities so there are no gaps and no overlaps: <strong>0 &lt; t &le; 10, 10 &lt; t &le; 20, 20 &lt; t &le; 30</strong>.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Locating the Median Class Interval Using Cumulative Frequency',
                'summary': 'Keeping a running total of frequencies to find which group holds the middle person.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Find the Median Position:</strong> Divide the total frequency by 2 (e.g. for 80 patients, 80 &divide; 2 = <strong>40th patient</strong>).</li>
                    <li><strong>Keep a Running Total (Cumulative Frequency):</strong> Add frequencies down the rows until your running total reaches or passes 40.</li>
                    <li><strong>Write the Interval:</strong> State the group label where the running total first reaches 40.</li>
                  </ol>
                </div>
                """
            },
            {
                'title': 'Calculating Fractions & Percentages Above/Below a Threshold',
                'summary': 'Summing frequencies across multiple rows to evaluate compliance targets.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">If a question asks: <em>"What percentage of patients waited more than 20 minutes?"</em></p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li>Add the frequencies of all groups strictly above 20 minutes (e.g. 20–30 mins + 30–40 mins = 22 + 6 = <strong>28 patients</strong>).</li>
                    <li>Divide by total patients (80) and multiply by 100: (28 &divide; 80) &times; 100 = <strong>35%</strong>.</li>
                  </ul>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Hospital Phlebotomy Outpatient Waiting Time Distribution (Level 1/2 Foundation)',
                'marks': '3 Marks (Pearson Edexcel Level 1/2)',
                'context': 'Clinical Phlebotomy Clinic Auditing',
                'question': 'A blood testing clinic records waiting times for <strong>80 outpatients</strong>:<br>• 0 &lt; t &le; 10 mins: <strong>14 patients</strong><br>• 10 &lt; t &le; 20 mins: <strong>38 patients</strong><br>• 20 &lt; t &le; 30 mins: <strong>22 patients</strong><br>• 30 &lt; t &le; 40 mins: <strong>6 patients</strong><br>(a) State the modal class interval.<br>(b) In which class interval does the median waiting time lie?<br>(c) What percentage of patients waited more than 20 minutes?',
                'steps': [
                    ('Step 1', 'Identify the interval with highest frequency (38)', 'Modal class = 10 < t ≤ 20 mins.', 'A1: Correct modal class interval'),
                    ('Step 2', 'Find median position (40th) using cumulative frequency', 'Group 1 ends at 14; Group 2 ends at 14 + 38 = 52. The 40th patient lies in 10 < t ≤ 20 mins.', 'A1: Accurate median class interval'),
                    ('Step 3', 'Calculate percentage waiting > 20 mins', 'Patients > 20 mins = 22 + 6 = 28.<br>Percentage = (28 ÷ 80) × 100 = 35%.', 'A1: Accurate percentage (35%)')
                ],
                'final_answer': '(a) Modal Class: 10 < t ≤ 20 | (b) Median Class: 10 < t ≤ 20 | (c) 35%',
                'tutor_tip': 'Always copy the exact inequality interval (10 < t ≤ 20) rather than writing the frequency (38).'
            },
            {
                'title': 'Raw Call Duration Data Tally & SLA Compliance Audit (Level 2 Multi-Step)',
                'marks': '4 Marks (Pearson Edexcel Level 2)',
                'context': 'IT Helpdesk Ticket Resolution',
                'question': 'An IT helpdesk logs the resolution time (in minutes) for <strong>15 support tickets</strong>:<br><strong>8, 14, 20, 6, 25, 12, 10, 18, 32, 15, 9, 22, 11, 28, 16</strong><br>• Group 1: <strong>0 &lt; t &le; 10</strong> | Group 2: <strong>10 &lt; t &le; 20</strong> | Group 3: <strong>20 &lt; t &le; 35</strong><br>(a) Determine the frequency for each of the three groups.<br>(b) State the modal class and determine whether at least 70% of tickets were resolved within 20 minutes or less.',
                'steps': [
                    ('Step 1', 'Sort or classify the 15 values carefully (noting 10 goes in Group 1 and 20 goes in Group 2)', '0 < t ≤ 10: {6, 8, 9, 10} → Frequency = 4.<br>10 < t ≤ 20: {11, 12, 14, 15, 16, 18, 20} → Frequency = 7.<br>20 < t ≤ 35: {22, 25, 28, 32} → Frequency = 4.<br>(Check sum: 4 + 7 + 4 = 15).', 'M1 / A1: Accurate frequencies (4, 7, 4)'),
                    ('Step 2', 'Identify the modal class', 'Highest frequency is 7 → Modal class is 10 < t ≤ 20.', 'A1: Modal class (10 < t ≤ 20)'),
                    ('Step 3', 'Calculate percentage ≤ 20 minutes and compare with 70%', 'Tickets ≤ 20 mins = 4 + 7 = 11 tickets.<br>(11 ÷ 15) × 100 = 73.3%. Yes, 73.3% exceeds the 70% target.', 'A1: 73.3% and valid Yes conclusion')
                ],
                'final_answer': '(a) Frequencies: 4, 7, 4 | (b) Modal class: 10 < t ≤ 20; Yes (73.3% resolved in ≤ 20 mins)',
                'tutor_tip': 'Pay close attention to boundary numbers: 10 belongs in 0 < t ≤ 10, and 20 belongs in 10 < t ≤ 20!'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Writing the Frequency Instead of the Class Interval for Modal Class',
                'desc': 'Answering "38" instead of "10 < t ≤ 20" scores zero marks.',
                'fix': 'Modal CLASS means the name of the group.'
            },
            {
                'title': 'Placing Boundary Values (e.g. 20.0) in the Wrong Group',
                'desc': 'Putting 20 into "20 < t ≤ 30" instead of "10 < t ≤ 20".',
                'fix': 'Look for the line under the inequality sign (≤ means "includes this number").'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'A logistics hub records parcel weights: <strong>0 &lt; w &le; 5 kg (freq 12), 5 &lt; w &le; 10 kg (freq 29), 10 &lt; w &le; 15 kg (freq 19)</strong>.<br>(a) State the modal class.<br>(b) In which group should a parcel weighing exactly <strong>5.0 kg</strong> be recorded?',
                'solution_steps': '1. Highest frequency is 29 → Modal class is 5 < w ≤ 10 kg.<br>2. Because 0 < w ≤ 5 kg has the "≤" (less than or equal to) sign on 5, 5.0 kg belongs in 0 < w ≤ 5 kg.',
                'correct_answer': '(a) 5 < w ≤ 10 kg | (b) 0 < w ≤ 5 kg',
                'tutor_tip': 'The ≤ symbol shows which interval owns the exact boundary value.'
            },
            {
                'marks': '3 Marks',
                'question': 'A staff age table shows: <strong>20–29 (11 staff), 30–39 (18 staff), 40–49 (14 staff), 50–59 (7 staff)</strong>. Total = 50 staff.<br>Find the class interval that contains the <strong>median age</strong>.',
                'solution_steps': '1. Median position = 50 ÷ 2 = 25th staff member.<br>2. Cumulative frequencies: Group 1 = 11; Group 1 + Group 2 = 11 + 18 = 29.<br>3. The 25th staff member falls inside the 30–39 interval.',
                'correct_answer': '30–39',
                'tutor_tip': 'Add frequencies from the top row until you pass N ÷ 2.'
            },
            {
                'marks': '3 Marks',
                'question': 'In a speed survey of <strong>120 vehicles</strong>: 0–20 mph (18), 21–30 mph (66), 31–40 mph (27), 41–50 mph (9). Calculate the percentage of vehicles exceeding the <strong>30 mph speed limit</strong>.',
                'solution_steps': '1. Vehicles over 30 mph = 27 + 9 = 36 vehicles.<br>2. Percentage = (36 ÷ 120) × 100 = 30%.',
                'correct_answer': '30%',
                'tutor_tip': 'Combine both groups above 30 mph (27 + 9 = 36) before dividing by 120.'
            }
        ]
    },
    {
        'filename': 'functional-skills-data-tables.html',
        'clean_topic': 'Data Tables & Two-Way Tables',
        'intro_lead': 'Extract, cross-reference, and complete missing cells in complex two-way frequency tables, mileage charts, and multi-factor clinical rotas, and extract conditional probabilities.',
        'next_file': 'functional-skills-bar-charts.html',
        'next_name': 'Bar Charts',
        'spec_points': [
            ('L1.24 / L2.31', 'Construct, complete, and interpret two-way frequency tables and complex multi-column workplace schedules.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-table-cells',
                'title': 'Golden Rule 1: Row Totals and Column Totals Must Cross-Check to the Grand Total',
                'desc': 'In every two-way table, the sum of the row totals MUST equal the sum of the column totals in the bottom-right Grand Total cell. Start with any row or column that has only ONE missing number.',
                'badge': 'Sum of Row Totals = Sum of Column Totals = Grand Total'
            },
            {
                'icon': 'fa-magnifying-glass',
                'title': 'Golden Rule 2: Read Conditional Probability Denominators Carefully',
                'desc': 'If asked for the probability from "all staff", divide by the Grand Total. If asked "Given that a nurse works the Night Shift...", divide ONLY by the Night Shift row/column total!',
                'badge': '"Of all..." → Divide by Grand Total • "Of the Night Shift..." → Divide by Subgroup Total'
            }
        ],
        'skills': [
            {
                'title': 'Completing a Two-Way Table Step-by-Step',
                'summary': 'Finding rows or columns with a single unknown and working outwards.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:center;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Role \\ Shift</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Day Shift</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Night Shift</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Total</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Registered Nurses (RN)</td><td style="padding:6px; border:1px solid #cbd5e1;">20</td><td style="padding:6px; border:1px solid #cbd5e1; color:#0284c7; font-weight:700;">15</td><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">35</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Healthcare Assistants (HCA)</td><td style="padding:6px; border:1px solid #cbd5e1; color:#0284c7; font-weight:700;">18</td><td style="padding:6px; border:1px solid #cbd5e1; color:#0284c7; font-weight:700;">7</td><td style="padding:6px; border:1px solid #cbd5e1; color:#0284c7; font-weight:700;">25</td></tr>
                      <tr style="background:#e0f2fe; font-weight:800; color:#0369a1;"><td style="padding:6px; border:1px solid #cbd5e1;">Total</td><td style="padding:6px; border:1px solid #cbd5e1;">38</td><td style="padding:6px; border:1px solid #cbd5e1;">22</td><td style="padding:6px; border:1px solid #cbd5e1;">60</td></tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                'title': 'Extracting Percentages & Fractions from Two-Way Tables',
                'summary': 'Selecting the right cell and the right total denominator.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Fraction of ALL staff who are Night RNs:</strong> 15 / 60 = <strong>1/4 (25%)</strong>.</li>
                    <li><strong>Percentage of RNs who work Nights:</strong> (15 &divide; 35) &times; 100 = <strong>42.9%</strong> (Denominator is 35 RNs, not 60!).</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Triangular Distance / Mileage Charts & Multi-Criteria Tariff Tables',
                'summary': 'Intersecting row and column headers in depot mileage grids.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">To read a triangular mileage table between two towns (e.g. Oxford and Bristol):</p>
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li>Locate <strong>Oxford</strong> along the horizontal row and <strong>Bristol</strong> along the vertical column.</li>
                    <li>Follow both lines straight until they meet at the single intersecting cell.</li>
                    <li>For a multi-stop round trip (Depot &rarr; Town A &rarr; Town B &rarr; Depot), extract all three leg distances and add them together.</li>
                  </ol>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Hospital Clinical Shift Staff Attendance Two-Way Table (Level 1/2 Foundation)',
                'marks': '3 Marks (Pearson Edexcel Level 1/2)',
                'context': 'Healthcare Staffing Workforce Management',
                'question': 'A hospital ward employs <strong>60 nursing staff</strong> across Day and Night shifts. <strong>35 staff are Registered Nurses (RNs)</strong> and the rest are Healthcare Assistants (HCAs). <strong>20 RNs work Day shifts</strong>. In total, <strong>38 staff work Day shifts</strong>.<br>(a) Find how many HCAs work Night shifts.<br>(b) What percentage of the total 60 staff work Night shifts (to 1 decimal place)?',
                'steps': [
                    ('Step 1', 'Calculate total HCAs and Day HCAs', 'Total HCAs = 60 − 35 = 25 HCAs.<br>Day HCAs = 38 − 20 = 18 HCAs.', 'M1: Row/column subtraction'),
                    ('Step 2', 'Calculate Night HCAs', 'Night HCAs = 25 − 18 = 7 HCAs (Check: Total Night = 60 − 38 = 22; Night RNs = 35 − 20 = 15; 15 + 7 = 22).', 'A1: Accurate Night HCA count (7)'),
                    ('Step 3', 'Calculate percentage of total staff on Night shift', '(22 ÷ 60) × 100 = 36.66...% → 36.7%.', 'A1: Accurate percentage (36.7%)')
                ],
                'final_answer': '(a) 7 HCAs work Night shifts | (b) 36.7%',
                'tutor_tip': 'Always cross-check that both row totals (35 + 25 = 60) and column totals (38 + 22 = 60) add up to the Grand Total.'
            },
            {
                'title': 'Medical Training Exam Pass Rate Conditional Audit (Level 2 Multi-Step)',
                'marks': '4 Marks (Pearson Edexcel Level 2)',
                'context': 'Clinical Mandatory Training Compliance',
                'question': '120 staff sat a mandatory resuscitation assessment after choosing either <strong>In-Person Training</strong> or <strong>Online E-Learning</strong>:<br>• <strong>75 staff</strong> chose In-Person Training, and <strong>66 of them passed</strong>.<br>• Overall across both methods, <strong>96 staff passed</strong> in total.<br>Compare the percentage pass rate of In-Person Training against Online E-Learning.',
                'steps': [
                    ('Step 1', 'Calculate Online E-Learning total candidates and passes', 'Online Total = 120 − 75 = 45 staff.<br>Online Passes = 96 − 66 = 30 staff.', 'M1: Deducting online subgroup totals (30 out of 45)'),
                    ('Step 2', 'Calculate In-Person percentage pass rate', '(66 ÷ 75) × 100 = 88%.', 'M1: In-Person pass rate (88%)'),
                    ('Step 3', 'Calculate Online percentage pass rate and compare', '(30 ÷ 45) × 100 = 66.7%.<br>In-Person Training achieved a much higher pass rate (88% vs 66.7%).', 'M1 / A1: Online pass rate (66.7%) and comparative conclusion')
                ],
                'final_answer': 'In-Person Pass Rate = 88% vs Online Pass Rate = 66.7% (In-Person was higher by 21.3%)',
                'tutor_tip': 'To find the pass rate OF In-Person candidates, divide 66 by 75 (not 120!).'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Dividing by the Grand Total Instead of the Subgroup Total',
                'desc': 'When asked "What percentage of the Night Shift staff are RNs?", dividing 15 by 60 instead of 15 by 22.',
                'fix': 'The group immediately following "of the..." is always your bottom denominator!'
            },
            {
                'title': 'Leaving Blank Cells in a Two-Way Table Question',
                'desc': 'Even if the question only asks for one specific cell at the end, examiners award method marks for filling in the entire table.',
                'fix': 'Fill in every single cell in the printed two-way table and check all row and column sums.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'In a logistics hub of <strong>100 drivers</strong>, 65 drive daytime routes and 35 drive night routes. <strong>40 of the daytime drivers</strong> operate articulated lorries, and <strong>20 of the night drivers</strong> operate articulated lorries. The rest drive rigid vans. How many night drivers operate rigid vans?',
                'solution_steps': '1. Total night drivers = 35.<br>2. Night articulated drivers = 20.<br>3. Night rigid van drivers = 35 − 20 = 15 drivers.',
                'correct_answer': '15 drivers',
                'tutor_tip': 'Subtract the 20 night articulated drivers from the 35 total night drivers.'
            },
            {
                'marks': '3 Marks',
                'question': 'A café records <strong>200 drink orders</strong> (Hot or Cold, Eat-In or Takeaway). <strong>130 drinks are Hot</strong>. <strong>85 orders are Eat-In</strong>, of which <strong>60 are Hot</strong>.<br>Calculate how many <strong>Cold Takeaway</strong> drinks were ordered.',
                'solution_steps': '1. Total Cold drinks = 200 − 130 = 70.<br>2. Eat-In Cold drinks = 85 − 60 = 25.<br>3. Takeaway Cold drinks = 70 − 25 = 45 drinks.',
                'correct_answer': '45 Cold Takeaway drinks',
                'tutor_tip': 'Sketch a quick 2×2 grid to keep Hot/Cold and Eat-In/Takeaway clear.'
            },
            {
                'marks': '3 Marks',
                'question': 'Using the café data in Question 2, if one Eat-In customer is chosen at random, what is the probability that they ordered a Cold drink? Give your answer as a simplified fraction.',
                'solution_steps': '1. Total Eat-In customers = 85.<br>2. Eat-In Cold customers = 25.<br>3. Probability = 25 / 85 = 5 / 17 (dividing top and bottom by 5).',
                'correct_answer': '5/17',
                'tutor_tip': 'Since the customer is chosen from Eat-In customers, the denominator is 85, not 200.'
            }
        ]
    },
    {
        'filename': 'functional-skills-bar-charts.html',
        'clean_topic': 'Bar Charts: Dual, Component & Frequency',
        'intro_lead': 'Construct and interpret single, dual (comparative), and component (stacked) bar charts, read linear vertical scales accurately, and compare departmental performance.',
        'next_file': 'functional-skills-line-graphs.html',
        'next_name': 'Line Graphs',
        'spec_points': [
            ('L1.25 / L2.31', 'Draw and interpret single, dual (grouped), and composite (stacked) bar charts with appropriate titles, axis labels, keys, and linear scales.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-chart-column',
                'title': 'Golden Rule 1: Follow S-L-A-P-T Every Time You Draw a Bar Chart',
                'desc': 'Scale (even linear steps starting at 0) • Labels (both X and Y axes labelled with units) • Axes (ruled straight) • Points/Bars (accurate heights, equal widths, equal gaps) • Title & Key (clear chart title plus a legend/key for dual or stacked bars).',
                'badge': 'Scale • Labels • Axes • Bars (Equal Gaps) • Title & Key (SLAPT)'
            },
            {
                'icon': 'fa-layer-group',
                'title': 'Golden Rule 2: Stacked (Component) Bars Require Subtraction for Top Segments',
                'desc': 'In a stacked bar chart, the bottom section is read directly from 0, but upper sections sit on top of lower sections. To find an upper section’s value: Top of Segment − Bottom of Segment.',
                'badge': 'Stacked Segment Value = Top Reading − Bottom Reading'
            }
        ],
        'skills': [
            {
                'title': 'Single vs Dual (Grouped) vs Component (Stacked) Bar Charts',
                'summary': 'How to read and draw the three bar chart formats tested in exams.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Single Bar Chart:</strong> One bar per category, with equal spaces between every bar.</li>
                    <li><strong>Dual (Comparative) Bar Chart:</strong> Two bars touching side-by-side for each category (e.g. Target vs Actual), with a clear gap before the next category pair and a shaded <strong>Key/Legend</strong>.</li>
                    <li><strong>Component (Stacked) Bar Chart:</strong> One bar per category divided into stacked segments; the top of the whole bar shows the category total.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Choosing a Sensible Linear Scale for the Vertical Axis',
                'summary': 'Avoiding uneven jumps and awkward grid subdivisions.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">Always start the vertical frequency axis at <strong>0</strong> and go up in clean multiples of <strong>1, 2, 5, 10, 20, 50, or 100</strong>:</p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li>Never just copy the table numbers (e.g. 14, 29, 38, 65) unevenly up the axis—that loses the scale mark immediately!</li>
                    <li>If 1 major grid square (5 small squares) represents 10 units, then each small square = 10 &divide; 5 = <strong>2 units</strong>.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Calculating Percentage Changes & Ratios from Bar Heights',
                'summary': 'Combining bar chart extraction with Level 2 percentage calculations.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">After reading two bar heights (e.g. Q1 = 80 units, Q2 = 100 units):</p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Percentage Increase:</strong> ((New &minus; Original) &divide; Original) &times; 100 = ((100 &minus; 80) &divide; 80) &times; 100 = <strong>25%</strong>.</li>
                    <li><strong>Ratio in Simplest Form:</strong> 80 : 100 &rarr; divide both by 20 = <strong>4 : 5</strong>.</li>
                  </ul>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Hospital Surgical Department Dual Bar Chart Audit (Level 1/2 Foundation)',
                'marks': '3 Marks (Pearson Edexcel Level 1/2)',
                'context': 'Surgical Theatre Performance Reporting',
                'question': 'A dual bar chart compares Scheduled vs Emergency operations. In October, Scheduled is <strong>85</strong> and Emergency is <strong>40</strong>. In November, Scheduled is <strong>70</strong> and Emergency is <strong>55</strong>.<br>(a) Compare the total number of operations in October and November.<br>(b) Calculate the percentage increase in Emergency operations from October to November.',
                'steps': [
                    ('Step 1', 'Sum Scheduled + Emergency for each month', 'October Total = 85 + 40 = 125 operations.<br>November Total = 70 + 55 = 125 operations.<br>Both months had the exact same total (125 operations).', 'M1: Summing paired bars (125 each)'),
                    ('Step 2', 'Find the increase in Emergency operations', 'Increase = 55 − 40 = 15 operations.', 'M1: Difference calculation (15)'),
                    ('Step 3', 'Divide by October original (40) and multiply by 100', '(15 ÷ 40) × 100 = 37.5%.', 'A1: Accurate percentage increase (37.5%)')
                ],
                'final_answer': '(a) Equal total of 125 operations in both months | (b) 37.5% increase',
                'tutor_tip': 'Always divide the change (15) by the ORIGINAL starting month (40), never the new month (55).'
            },
            {
                'title': 'Stacked Recycling Waste Bar Chart Extraction & Target Check (Level 2 Multi-Step)',
                'marks': '4 Marks (Pearson Edexcel Level 2)',
                'context': 'Hospital Environmental Waste Audit',
                'question': 'A stacked (component) bar chart shows weekly hospital waste in tonnes across General Waste (bottom section), Recycling (middle section), and Clinical Waste (top section):<br>• For Week 1, the General Waste section goes from <strong>0 to 12 tonnes</strong>, the Recycling section goes from <strong>12 to 27 tonnes</strong>, and the Clinical Waste section goes from <strong>27 to 30 tonnes</strong>.<br>(a) How many tonnes of Recycling waste were collected in Week 1?<br>(b) Did Recycling achieve the sustainability target of <strong>at least 45%</strong> of total Week 1 waste?',
                'steps': [
                    ('Step 1', 'Subtract bottom of Recycling segment from top of Recycling segment', 'Recycling = 27 − 12 = 15 tonnes.', 'M1 / A1: Accurate stacked segment extraction (15 tonnes)'),
                    ('Step 2', 'Identify total Week 1 waste from the top of the stacked bar', 'Total waste = 30 tonnes.', 'B1: Correct total height reading (30 tonnes)'),
                    ('Step 3', 'Calculate Recycling percentage and compare with 45% target', '(15 ÷ 30) × 100 = 50%.<br>Yes, 50% exceeds the 45% sustainability target.', 'A1: 50% and valid Yes conclusion')
                ],
                'final_answer': '(a) 15 tonnes of Recycling | (b) Yes, Recycling was 50% of total waste (> 45% target)',
                'tutor_tip': 'In a stacked bar chart, NEVER read the top of a middle segment (27) as its value—always subtract the base of that segment (27 − 12 = 15)!'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Forgetting to Subtract the Lower Segment in a Stacked Bar Chart',
                'desc': 'Reading 27 tonnes instead of 27 − 12 = 15 tonnes for the middle segment.',
                'fix': 'Always do: Top of Coloured Block − Bottom of Coloured Block.'
            },
            {
                'title': 'Omitting the Key/Legend on a Dual or Stacked Bar Chart',
                'desc': 'Drawing two sets of bars without a key showing which shading represents which group loses 1 mark automatically.',
                'fix': 'Always draw a small box labelled "Key" in the corner of your chart.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'On a bar chart vertical axis, major grid lines are labelled <strong>0, 20, 40, 60, 80</strong>, with <strong>4 equal subdivisions</strong> between each major label. A bar reaches <strong>3 subdivisions above 40</strong>. What value does this bar represent?',
                'solution_steps': '1. Value of 1 subdivision = (20 − 0) ÷ 4 = 5 units.<br>2. Bar height = 40 + (3 × 5) = 40 + 15 = 55.',
                'correct_answer': '55',
                'tutor_tip': 'Divide the jump (20) by the number of spaces (4) to get 5 per line.'
            },
            {
                'marks': '3 Marks',
                'question': 'A bar chart shows clinic attendances over 4 days: <strong>Monday: 42, Tuesday: 56, Wednesday: 38, Thursday: 60</strong>. Calculate the <strong>mean daily attendance</strong> across the 4 days.',
                'solution_steps': '1. Total = 42 + 56 + 38 + 60 = 196 patients.<br>2. Mean = 196 ÷ 4 = 49 patients per day.',
                'correct_answer': '49 patients per day',
                'tutor_tip': 'Extract all four bar heights first, sum them, and divide by 4.'
            },
            {
                'marks': '3 Marks',
                'question': 'In a component (stacked) bar chart for staff transport, a bar reaches a total height of <strong>80 staff</strong>. Car drivers occupy <strong>0 to 44</strong>, Bus users occupy <strong>44 to 68</strong>, and Cyclists occupy <strong>68 to 80</strong>. How many more staff travel by Bus than by Bicycle?',
                'solution_steps': '1. Bus users = 68 − 44 = 24 staff.<br>2. Cyclists = 80 − 68 = 12 staff.<br>3. Difference = 24 − 12 = 12 more staff.',
                'correct_answer': '12 more staff',
                'tutor_tip': 'Find the size of each stacked segment by subtracting its bottom reading from its top reading.'
            }
        ]
    },
    {
        'filename': 'functional-skills-line-graphs.html',
        'clean_topic': 'Line Graphs & Trend Analysis',
        'intro_lead': 'Plot and read continuous time-series line graphs, interpret upward, downward, and seasonal trends with supporting figures, interpolate between plotted points, and compare dual trend lines.',
        'next_file': 'functional-skills-pie-charts.html',
        'next_name': 'Pie Charts',
        'spec_points': [
            ('L1.25 / L2.31', 'Draw and interpret time-series line graphs, describe trends supported by numerical data, and interpolate values between points.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-chart-line',
                'title': 'Golden Rule 1: Time Belongs on the Horizontal X-Axis; Join Points with Ruled Segments',
                'desc': 'When plotting time-series data (hours, days, months, years), always place Time along the bottom horizontal X-axis and the measured variable up the vertical Y-axis. Plot points as neat crosses (×) and join consecutive points with straight ruler lines.',
                'badge': 'Time = Horizontal X-Axis • Plot with × • Join Consecutive Points'
            },
            {
                'icon': 'fa-arrow-trend-up',
                'title': 'Golden Rule 2: Describing a Trend Requires Direction + Specific Numbers',
                'desc': "Never write just 'it went up' or 'it went down'. Always state the overall direction AND quote starting/ending/peak figures from the graph (e.g. 'Overall downward trend, falling from 38.8°C at 08:00 to 37.0°C at 18:00').",
                'badge': 'Trend Mark = Direction (Rise/Fall/Fluctuate) + Start & End Figures'
            }
        ],
        'skills': [
            {
                'title': 'Interpolation vs Extrapolation on Time-Series Graphs',
                'summary': 'Reading values halfway between plotted time intervals vs projecting into the future.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Interpolation (Between Plotted Points):</strong> To estimate the reading at 11:00 when points are plotted at 10:00 (38.4°C) and 12:00 (37.8°C), read up from 11:00 to the straight line joining them: <em>(38.4 + 37.8) &divide; 2 = <strong>38.1°C</strong></em>.</li>
                    <li><strong>Extrapolation (Beyond the Graph):</strong> Continuing a trend line into future months assumes current conditions remain unchanged.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Finding the Steepest Rate of Change',
                'summary': 'Identifying which time period had the fastest increase or decrease.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">The <strong>steepest line segment</strong> represents the fastest rate of change per hour or per month:</p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li>Calculate the vertical drop or rise across each equal time step to confirm which interval changed by the largest amount.</li>
                    <li>A <strong>horizontal flat line</strong> means the value remained constant (zero change) during that period.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Comparing Dual Line Graphs (Two Lines on the Same Axes)',
                'summary': 'Finding crossover points and maximum differences between two competing series.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Intersection Point (Crossover):</strong> Where the two lines cross, both categories had the exact same value at that time.</li>
                    <li><strong>Vertical Gap:</strong> To find the difference between Branch A and Branch B in March, read both values at March and subtract: <strong>Top Line &minus; Bottom Line</strong>.</li>
                  </ul>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Hospital ICU Patient Body Temperature Monitoring Line Graph (Level 1/2 Foundation)',
                'marks': '3 Marks (Pearson Edexcel Level 1/2)',
                'context': 'Intensive Care Clinical Observation',
                'question': "A clinical line graph records an ICU patient's temperature every 2 hours from 08:00 to 18:00:<br>• 08:00: <strong>38.8°C</strong> | 10:00: <strong>38.4°C</strong> | 12:00: <strong>37.8°C</strong> | 14:00: <strong>37.2°C</strong> | 16:00: <strong>36.9°C</strong> | 18:00: <strong>37.0°C</strong><br>(a) Describe the overall trend in the patient's temperature over the 10-hour period.<br>(b) Estimate the patient's temperature at 11:00.",
                'steps': [
                    ('Step 1', 'State overall trend direction with start and end figures', "Steady downward trend, falling from 38.8°C at 08:00 to 36.9°C at 16:00 before stabilising at 37.0°C at 18:00.", 'A1: Accurate trend description with figures'),
                    ('Step 2', 'Interpolate halfway between 10:00 (38.4°C) and 12:00 (37.8°C)', '(38.4 + 37.8) ÷ 2 = 76.2 ÷ 2 = 38.1°C.', 'M1: Midpoint interpolation'),
                    ('Step 3', 'State estimated temperature with units', '38.1°C.', 'A1: Accurate interpolated value (38.1°C)')
                ],
                'final_answer': '(a) Downward trend from 38.8°C at 08:00 to 37.0°C at 18:00 | (b) 38.1°C',
                'tutor_tip': 'Always include starting and ending figures when describing a line graph trend.'
            },
            {
                'title': 'Cold-Room Vaccine Fridge Power Outage Threshold Analysis (Level 2 Multi-Step)',
                'marks': '4 Marks (Pearson Edexcel Level 2)',
                'context': 'Pharmacy Cold-Chain Safety Monitoring',
                'question': 'During a power cut, a vaccine fridge temperature is logged every hour:<br>• 01:00: <strong>3.0°C</strong> | 02:00: <strong>4.5°C</strong> | 03:00: <strong>6.5°C</strong> | 04:00: <strong>9.5°C</strong> | 05:00: <strong>7.0°C</strong> | 06:00: <strong>4.0°C</strong><br>• Vaccines must be quarantined if the temperature stays <strong>above 8.0°C for more than 45 minutes</strong>.<br>Using linear interpolation between the plotted points, determine the exact times when the fridge was above 8.0°C and decide whether the vaccines must be quarantined.',
                'steps': [
                    ('Step 1', 'Find when temperature crossed 8.0°C rising between 03:00 (6.5°C) and 04:00 (9.5°C)', 'Rise from 6.5°C to 9.5°C is 3.0°C in 60 mins (1°C every 20 mins).<br>From 6.5°C to 8.0°C is 1.5°C → 1.5 × 20 mins = 30 mins → Crosses 8.0°C at 03:30.', 'M1: Rising crossover at 03:30'),
                    ('Step 2', 'Find when temperature dropped back to 8.0°C between 04:00 (9.5°C) and 05:00 (7.0°C)', 'Drop from 9.5°C to 7.0°C is 2.5°C in 60 mins.<br>Drop from 9.5°C to 8.0°C is 1.5°C → (1.5 ÷ 2.5) × 60 = 36 mins → Drops to 8.0°C at 04:36.', 'M1: Falling crossover at 04:36'),
                    ('Step 3', 'Calculate total minutes above 8.0°C and compare with 45-minute limit', 'From 03:30 to 04:36 = 30 + 36 = 66 minutes.<br>Since 66 mins > 45 mins, YES, the vaccines must be quarantined.', 'M1 / A1: 66 minutes and valid quarantine decision')
                ],
                'final_answer': 'Above 8.0°C for 66 minutes (03:30 to 04:36) — Yes, vaccines must be quarantined (> 45 mins)',
                'tutor_tip': 'Draw a horizontal line across the graph at 8.0°C to see exactly where the graph rises above and drops below the threshold.'
            }
        ],
        'examiner_traps': [
            {
                'title': "Writing Simply 'It Went Down' Without Supporting Numbers",
                'desc': 'Vague trend statements without figures from the axes score 0 marks.',
                'fix': 'Always write: "Decreased from [Start Value] in [Start Time] to [End Value] in [End Time]."'
            },
            {
                'title': 'Drawing Bars Instead of Plotted Points Joined by Lines',
                'desc': 'When asked to draw a line graph, drawing vertical bars loses the format mark.',
                'fix': 'Plot neat crosses (×) at each coordinate and connect them point-to-point with a ruler.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'A depot diesel tank line graph shows <strong>420 litres at 08:00</strong> and <strong>180 litres at 16:00</strong>, decreasing at a steady linear rate. How many litres were in the tank at <strong>12:00</strong>?',
                'solution_steps': '1. 12:00 is halfway between 08:00 and 16:00.<br>2. Midpoint = (420 + 180) ÷ 2 = 600 ÷ 2 = 300 litres.',
                'correct_answer': '300 litres',
                'tutor_tip': 'Average the 08:00 and 16:00 readings (drops by 30 litres per hour).'
            },
            {
                'marks': '3 Marks',
                'question': 'A dual line graph compares quarterly sales (£000s) for Store A and Store B:<br>• Store A: Q1 = 40, Q2 = 55, Q3 = 50, Q4 = 75<br>• Store B: Q1 = 50, Q2 = 45, Q3 = 65, Q4 = 60<br>In which quarter was the difference in sales between the two stores greatest, and what was that difference in £?',
                'solution_steps': '1. Differences: Q1 = 10k; Q2 = 10k; Q3 = 65 − 50 = 15k; Q4 = 75 − 60 = 15k.<br>2. Greatest difference is in Q3 and Q4, with a difference of £15,000.',
                'correct_answer': 'Q3 and Q4 (£15,000 difference)',
                'tutor_tip': 'Remember the axis is in £000s (thousands), so 15 represents £15,000!'
            },
            {
                'marks': '3 Marks',
                'question': 'Using the Store A sales figures from Question 2 (Q1: £40k, Q2: £55k, Q3: £50k, Q4: £75k), calculate the mean quarterly sales for Store A in £.',
                'solution_steps': '1. Sum = 40 + 55 + 50 + 75 = 220 (£000s) = £220,000.<br>2. Mean = £220,000 ÷ 4 = £55,000.',
                'correct_answer': '£55,000',
                'tutor_tip': '220 ÷ 4 = 55 thousand pounds (£55,000).'
            }
        ]
    },
    {
        'filename': 'functional-skills-pie-charts.html',
        'clean_topic': 'Pie Charts & Proportional Angles',
        'intro_lead': 'Calculate pie chart sector angles (Angle = Frequency ÷ Total × 360°), draw sectors accurately using a protractor, and extract frequencies and percentages from existing pie charts.',
        'next_file': 'functional-skills-scatter-graphs.html',
        'next_name': 'Scatter Graphs & Correlation',
        'spec_points': [
            ('L1.25 / L2.31', 'Construct and interpret pie charts, calculating sector angles from frequencies and extracting quantities from angles.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-chart-pie',
                'title': 'Golden Rule 1: The Magic Multiplier: Degrees per Item = 360° ÷ Total Frequency',
                'desc': "Divide 360° by the total frequency to find how many degrees represent ONE item. Multiply each category's frequency by this magic multiplier, and check that all your angles add up to exactly 360°!",
                'badge': 'Sector Angle = (Frequency ÷ Total) × 360° • Check Sum = 360°'
            },
            {
                'icon': 'fa-rotate',
                'title': 'Golden Rule 2: Working Backwards from an Angle: (Angle ÷ 360°) × Total',
                'desc': 'If given a sector angle (e.g. 90° or 108°) and the total number of items (e.g. 200 people): Frequency = (Angle ÷ 360°) × Total.',
                'badge': 'Frequency = (Sector Angle ÷ 360°) × Total Frequency'
            }
        ],
        'skills': [
            {
                'title': 'Pie Chart Angle Calculation Table (Check Sum = 360°)',
                'summary': 'Setting up the standard 4-column table for full method and accuracy marks.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">For <strong>72 total hospital admissions</strong>: Magic Multiplier = 360° &divide; 72 = <strong>5° per patient</strong>.</p>
                  <table style="width:100%; border-collapse:collapse; text-align:center;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:6px; border:1px solid #cbd5e1;">Ward</th>
                        <th style="padding:6px; border:1px solid #cbd5e1;">Patients</th>
                        <th style="padding:6px; border:1px solid #cbd5e1;">Calculation (&times; 5°)</th>
                        <th style="padding:6px; border:1px solid #cbd5e1;">Sector Angle (°)</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1;">Medical</td><td style="padding:6px; border:1px solid #cbd5e1;">36</td><td style="padding:6px; border:1px solid #cbd5e1;">36 &times; 5°</td><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">180°</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1;">Surgical</td><td style="padding:6px; border:1px solid #cbd5e1;">21</td><td style="padding:6px; border:1px solid #cbd5e1;">21 &times; 5°</td><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">105°</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1;">Orthopaedic</td><td style="padding:6px; border:1px solid #cbd5e1;">15</td><td style="padding:6px; border:1px solid #cbd5e1;">15 &times; 5°</td><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">75°</td></tr>
                      <tr style="background:#e0f2fe; font-weight:800; color:#0369a1;"><td style="padding:6px; border:1px solid #cbd5e1;">Total</td><td style="padding:6px; border:1px solid #cbd5e1;">72</td><td style="padding:6px; border:1px solid #cbd5e1;">72 &times; 5°</td><td style="padding:6px; border:1px solid #cbd5e1;">360°</td></tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                'title': 'Extracting Frequencies When Given One Sector’s Value (Without the Total)',
                'summary': 'Using proportional scaling per degree when the grand total is not stated.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">Sometimes a question tells you: <em>"The 60° sector represents 30 patients. How many patients are in the 150° sector?"</em></p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Find Degrees per Patient:</strong> 60° &divide; 30 patients = <strong>2° per patient</strong> (or 0.5 patients per degree).</li>
                    <li><strong>Scale the Target Sector:</strong> 150° &divide; 2° = <strong>75 patients</strong> (and Total = 360° &divide; 2° = 180 patients).</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Comparing Two Pie Charts with Different Total Frequencies',
                'summary': 'Why a larger angle does NOT automatically mean a larger number of people!',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;"><strong>Classic Level 2 Exam Trap:</strong></p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li>Clinic A (Total = <strong>100 patients</strong>) has a <strong>90°</strong> sector &rarr; (90 &divide; 360) &times; 100 = <strong>25 patients</strong>.</li>
                    <li>Clinic B (Total = <strong>400 patients</strong>) has a <strong>72°</strong> sector &rarr; (72 &divide; 360) &times; 400 = <strong>80 patients</strong>.</li>
                    <li>Even though Clinic B has a smaller angle (72° vs 90°), it has <strong>more patients</strong> (80 vs 25) because its total population is four times larger!</li>
                  </ul>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Hospital Trust Energy Consumption Breakdown Pie Chart (Level 1/2 Foundation)',
                'marks': '3 Marks (Pearson Edexcel Level 1/2)',
                'context': 'Facility Environmental Sustainability',
                'question': 'A hospital records its annual energy consumption of <strong>1,000 MWh</strong> by source:<br>• Gas: <strong>500 MWh</strong> | Electricity: <strong>300 MWh</strong> | Solar: <strong>120 MWh</strong> | Biomass: <strong>80 MWh</strong><br>Calculate the sector angle in degrees for each of the four energy sources on a pie chart.',
                'steps': [
                    ('Step 1', 'Calculate degrees per MWh (360° ÷ 1,000)', '360° ÷ 1,000 MWh = 0.36° per MWh.', 'M1: Angle multiplier (0.36° per MWh)'),
                    ('Step 2', 'Multiply each energy quantity by 0.36°', 'Gas = 500 × 0.36° = 180°<br>Electricity = 300 × 0.36° = 108°<br>Solar = 120 × 0.36° = 43.2°<br>Biomass = 80 × 0.36° = 28.8°', 'M1: Sector multiplications'),
                    ('Step 3', 'Check that all four angles sum to 360°', '180° + 108° + 43.2° + 28.8° = 360°. Confirmed.', 'A1: All 4 angles accurate')
                ],
                'final_answer': 'Gas = 180°, Electricity = 108°, Solar = 43.2°, Biomass = 28.8°',
                'tutor_tip': 'Always add your final angles together to verify they sum to 360°.'
            },
            {
                'title': 'Comparing Two Regional Depots’ Electric Van Fleet Pie Charts (Level 2 Multi-Step)',
                'marks': '4 Marks (Pearson Edexcel Level 2)',
                'context': 'Logistics Fleet Decarbonisation Audit',
                'question': 'Two regional delivery depots display pie charts of their vehicle fleets:<br>• <strong>North Depot (Total = 180 vehicles):</strong> The Electric Van sector angle is <strong>100°</strong>.<br>• <strong>South Depot (Total = 300 vehicles):</strong> The Electric Van sector angle is <strong>72°</strong>.<br>The fleet director claims: <em>"North Depot has a greater number of Electric Vans than South Depot because its pie chart sector angle is larger (100° vs 72°)."</em><br>Is the fleet director correct? Show full calculations for both depots.',
                'steps': [
                    ('Step 1', 'Calculate number of Electric Vans at North Depot', 'North = (100° ÷ 360°) × 180 = 50 electric vans.', 'M1 / A1: North Depot count (50 vans)'),
                    ('Step 2', 'Calculate number of Electric Vans at South Depot', 'South = (72° ÷ 360°) × 300 = 0.2 × 300 = 60 electric vans.', 'M1: South Depot count (60 vans)'),
                    ('Step 3', 'Compare counts and state conclusion', 'No, the director is incorrect. North Depot has a higher proportion, but South Depot has 60 electric vans compared to 50 at North Depot (10 more vans).', 'A1: Valid comparison and No conclusion')
                ],
                'final_answer': 'Incorrect — South Depot has 60 electric vans vs 50 at North Depot',
                'tutor_tip': 'Pie chart angles only show PROPORTIONS. You must multiply by each depot’s total fleet size to compare actual vehicle counts!'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Using 100 Instead of 360° for Pie Chart Angles',
                'desc': 'Calculating percentages (out of 100) and plotting those directly as degrees leaves two-thirds of the circle empty!',
                'fix': 'A full circle is 360°, not 100°.'
            },
            {
                'title': 'Measuring Each New Sector from the Original Top Vertical Line',
                'desc': 'When drawing a pie chart with a protractor, you must measure each new sector starting from the line of the PREVIOUS sector you just drew.',
                'fix': 'Rotate your protractor so its zero line sits on the edge of the sector you just completed.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'In a pie chart representing <strong>120 staff members</strong>, the "Full-Time" sector has an angle of <strong>210°</strong>. How many staff members work full-time?',
                'solution_steps': '1. Fraction of circle = 210° ÷ 360° = 7/12.<br>2. Number of staff = (210 ÷ 360) × 120 = 70 staff members.',
                'correct_answer': '70 staff members',
                'tutor_tip': '(210 ÷ 360) × 120 = 70.'
            },
            {
                'marks': '3 Marks',
                'question': 'A care home survey of <strong>90 residents</strong> shows: <strong>38 chose Gardening, 27 chose Music, and 25 chose Bingo</strong>. Calculate the pie chart sector angle for each activity.',
                'solution_steps': '1. Multiplier = 360° ÷ 90 = 4° per resident.<br>2. Gardening = 38 × 4° = 152°.<br>3. Music = 27 × 4° = 108°.<br>4. Bingo = 25 × 4° = 100°.<br>5. Check: 152° + 108° + 100° = 360°.',
                'correct_answer': 'Gardening = 152°, Music = 108°, Bingo = 100°',
                'tutor_tip': '360° ÷ 90 = 4° per resident makes the multiplications super fast!'
            },
            {
                'marks': '3 Marks',
                'question': 'On a budget pie chart, the "IT Software" sector has an angle of <strong>54°</strong> and represents <strong>£13,500</strong>. Calculate the <strong>total budget</strong> represented by the entire 360° pie chart.',
                'solution_steps': '1. Value per degree = £13,500 ÷ 54° = £250 per degree.<br>2. Total 360° budget = £250 × 360 = £90,000.',
                'correct_answer': '£90,000',
                'tutor_tip': 'Divide £13,500 by 54° to find the value of 1° (£250), then multiply by 360°.'
            }
        ]
    },
    {
        'filename': 'functional-skills-scatter-graphs.html',
        'clean_topic': 'Scatter Graphs, Correlation & Lines of Best Fit',
        'intro_lead': 'Plot bivariate data on scatter diagrams, identify positive, negative, and zero correlation, draw lines of best fit by eye, identify outliers, and make interpolative predictions.',
        'next_file': 'functional-skills-conversion-graphs.html',
        'next_name': 'Conversion Graphs',
        'spec_points': [
            ('L2.32', 'Draw and interpret scatter diagrams, recognise positive, negative, and zero correlation, identify outliers, and draw/use a line of best fit.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-chart-simple',
                'title': 'Golden Rule 1: Positive (Upward) • Negative (Downward) • Zero (Random)',
                'desc': 'Positive Correlation: As X increases, Y increases (points slope upwards left-to-right). Negative Correlation: As X increases, Y decreases (points slope downwards left-to-right). Zero Correlation: No relationship (random cloud).',
                'badge': 'Positive = Both Increase • Negative = One Up, One Down • Zero = No Pattern'
            },
            {
                'icon': 'fa-ruler',
                'title': 'Golden Rule 2: Line of Best Fit Must Be ONE Straight Ruled Line (Never Join Dots!)',
                'desc': 'Use a clear ruler to draw a single straight line through the center of the data trend, with roughly equal numbers of points above and below (ignoring any extreme outlier). Never force it through (0, 0) unless the points point there!',
                'badge': 'One Straight Ruled Line • Balance Points Above/Below • Ignore Outliers'
            }
        ],
        'skills': [
            {
                'title': 'Stating Correlation Type vs Contextual Relationship',
                'summary': 'How to answer "State the type of correlation" vs "Describe the relationship".',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>"State the type of correlation":</strong> Write <strong>Positive correlation</strong>, <strong>Negative correlation</strong>, or <strong>No correlation</strong>.</li>
                    <li><strong>"Describe the relationship":</strong> Link both real-world variables in a sentence: <em>"As outdoor temperature increases, daily heating gas consumption decreases (negative correlation)."</em></li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Drawing & Using the Line of Best Fit for Interpolation',
                'summary': 'Showing dashed reading lines on the grid to secure method marks.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li>Draw your straight <strong>Line of Best Fit</strong> across the data range with a ruler.</li>
                    <li>Locate the given X-value on the horizontal axis, rule a dashed line straight UP to your line of best fit, and straight ACROSS to the Y-axis.</li>
                    <li><strong>Ignore Outliers:</strong> If one point sits far away from the main trend cluster, circle it as an outlier and ignore it when positioning your line of best fit.</li>
                  </ol>
                </div>
                """
            },
            {
                'title': 'Why Extrapolation Beyond the Data Range Is Unreliable',
                'summary': 'Explaining the danger of predicting far outside the plotted points.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">If a scatter graph plots car ages from 1 to 8 years against value, using the line of best fit to predict the value of a <strong>20-year-old car</strong> is <strong>unreliable</strong> because:</p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li>20 years lies <strong>outside the range of the collected data</strong> (extrapolation).</li>
                    <li>The linear trend may not continue (e.g. the line would eventually predict a negative car value!).</li>
                  </ul>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Logistics Van Fuel Consumption vs Cargo Payload Scatter Analysis (Level 2 Core)',
                'marks': '3 Marks (Pearson Edexcel Level 2)',
                'context': 'Fleet Fuel Efficiency Optimization',
                'question': 'A fleet manager plots cargo payload (kg) on the X-axis against fuel consumption (litres per 100 km) on the Y-axis for 10 delivery vans.<br>(a) What type of correlation is shown if fuel consumption rises as payload increases?<br>(b) Using the line of best fit, a <strong>500 kg payload</strong> corresponds to <strong>8.2 litres per 100 km</strong>. Estimate the total fuel required for a <strong>600 km round trip</strong> carrying a 500 kg load.',
                'steps': [
                    ('Step 1', 'State correlation type', 'Positive correlation (as payload increases, fuel consumption increases).', 'A1: Correct correlation (Positive)'),
                    ('Step 2', 'Extract fuel rate at 500 kg payload', 'Rate = 8.2 litres per 100 km.', 'M1: Rate extraction'),
                    ('Step 3', 'Scale up to 600 km (× 6)', '6 × 8.2 litres = 49.2 litres.', 'A1: Accurate total fuel (49.2 litres)')
                ],
                'final_answer': '(a) Positive correlation | (b) 49.2 litres',
                'tutor_tip': '600 km is 6 lots of 100 km, so multiply the 100 km rate (8.2 L) by 6.'
            },
            {
                'title': 'Hospital Solar Panel Output vs Sunshine Hours Outlier & Budget Check (Level 2 Multi-Step)',
                'marks': '4 Marks (Pearson Edexcel Level 2)',
                'context': 'Hospital Renewable Energy Auditing',
                'question': 'An energy manager records daily sunshine hours and solar electricity generated (kWh) across 7 days:<br>• (2 hrs, 30 kWh), (3 hrs, 45 kWh), (4 hrs, 60 kWh), (5 hrs, 12 kWh), (6 hrs, 90 kWh), (7 hrs, 105 kWh), (8 hrs, 120 kWh).<br>(a) Identify the coordinates of the outlier day (when an inverter fault occurred).<br>(b) Ignoring the outlier, use the linear trend to estimate the electricity generated on a day with <strong>5.5 hours of sunshine</strong>, and calculate the financial saving if electricity costs <strong>£0.24 per kWh</strong>.',
                'steps': [
                    ('Step 1', 'Identify the outlier point that breaks the upward trend', 'At 5 hours, output dropped to 12 kWh instead of 75 kWh. Outlier = (5, 12).', 'A1: Correct outlier identification (5 hrs, 12 kWh)'),
                    ('Step 2', 'Determine the trend rate and interpolate at 5.5 hours', 'Trend increases by 15 kWh per hour of sunshine (e.g. 2×15=30, 4×15=60, 6×15=90).<br>At 5.5 hours: 5.5 × 15 = 82.5 kWh.', 'M1 / A1: Accurate interpolation (82.5 kWh)'),
                    ('Step 3', 'Multiply 82.5 kWh by £0.24 per kWh', '82.5 × £0.24 = £19.80.', 'A1: Accurate financial saving (£19.80)')
                ],
                'final_answer': '(a) Outlier = (5 hrs, 12 kWh) | (b) 82.5 kWh generated, saving £19.80',
                'tutor_tip': 'Always exclude the outlier before finding the line of best fit!'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Joining the Plotted Points Dot-to-Dot',
                'desc': 'Connecting scatter points with a zigzag line instead of drawing ONE straight line with a ruler scores 0 marks for the line of best fit.',
                'fix': 'Use a ruler to draw a single straight line through the middle of the cluster.'
            },
            {
                'title': 'Forcing the Line of Best Fit Through (0, 0)',
                'desc': 'A negative correlation line (or a positive line with a baseline offset) does NOT pass through the origin (0, 0).',
                'fix': 'Only pass through (0, 0) if the plotted points clearly aim at the origin.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'A scatter graph plots the age of second-hand delivery vans (years) against their resale value (£).<br>(a) State the type of correlation you would expect.<br>(b) Describe the relationship in words.',
                'solution_steps': '1. Type: Negative correlation.<br>2. Relationship: As the age of the van increases, its resale value decreases.',
                'correct_answer': '(a) Negative correlation | (b) As van age increases, resale value decreases',
                'tutor_tip': 'State both the statistical name (Negative) and the real-world meaning.'
            },
            {
                'marks': '3 Marks',
                'question': 'On a scatter graph of Patient Age (X-axis) against Blood Pressure (Y-axis), the line of best fit passes through <strong>(30 years, 118 mmHg)</strong> and <strong>(60 years, 136 mmHg)</strong>. Use linear interpolation to estimate the blood pressure for a <strong>45-year-old patient</strong>.',
                'solution_steps': '1. 45 years is the exact midpoint between 30 and 60 years.<br>2. Midpoint Y = (118 + 136) ÷ 2 = 254 ÷ 2 = 127 mmHg.',
                'correct_answer': '127 mmHg',
                'tutor_tip': 'Since 45 is halfway between 30 and 60, the reading on the straight line of best fit is halfway between 118 and 136.'
            },
            {
                'marks': '2 Marks',
                'question': 'A scatter diagram plots staff height (cm) against their monthly overtime hours for 25 nurses. The points are scattered randomly across the grid. State the type of correlation and whether height can be used to predict overtime.',
                'solution_steps': '1. Zero (or no) correlation.<br>2. No, height cannot be used to predict overtime hours because there is no relationship between the variables.',
                'correct_answer': 'No (zero) correlation; height cannot predict overtime',
                'tutor_tip': 'When points form a random cloud with no upward or downward slope, state "No correlation".'
            }
        ]
    },
    {
        'filename': 'functional-skills-conversion-graphs.html',
        'clean_topic': 'Conversion Graphs & Currency Exchange',
        'intro_lead': 'Read and use linear conversion graphs to convert between currencies (GBP to EUR/USD), metric and imperial units (miles to km, kg to lbs), and dual-tariff utility graphs.',
        'next_file': 'functional-skills-probability.html',
        'next_name': 'Probability',
        'spec_points': [
            ('L1.25 / L2.31', 'Read, construct, and use linear conversion graphs to convert between units, currencies, and tariffs, including scaling for large values.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-chart-line',
                'title': 'Golden Rule 1: Scale Up Multiples for Values Beyond the Printed Graph',
                'desc': 'Conversion graphs for units and currencies pass through (0, 0) in direct proportion. If a graph only goes up to £50 (€60) and you need to convert £250: read the value at £50 (€60) and multiply by 5 (5 × €60 = €300).',
                'badge': 'For Large Values: Read a Clean Factor (e.g. £50 or £10) and Multiply'
            },
            {
                'icon': 'fa-pencil',
                'title': 'Golden Rule 2: Check the Small Grid Square Scale on BOTH Axes Separately',
                'desc': 'The horizontal X-axis and vertical Y-axis almost always have different scales! Calculate what 1 small grid square represents on the X-axis and what 1 small square represents on the Y-axis before reading.',
                'badge': 'Check X-Axis Small Square Value AND Y-Axis Small Square Value'
            }
        ],
        'skills': [
            {
                'title': 'Direct Proportion Scaling Using a Conversion Graph',
                'summary': 'Converting large amounts accurately by reading at 10, 20, or 50.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">Pick a point where the conversion line crosses an exact grid intersection (a "lattice point"):</p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Miles &harr; Kilometres:</strong> Line passes through <strong>(5 miles, 8 km)</strong> and <strong>(50 miles, 80 km)</strong>.</li>
                    <li><strong>Kilograms &harr; Pounds (lbs):</strong> Line passes through <strong>(10 kg, 22 lbs)</strong>.</li>
                    <li><strong>Litres &harr; Gallons:</strong> Line passes through <strong>(9 litres, 2 gallons)</strong> (1 gallon = 4.5 litres).</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Fixed-Charge + Per-Unit Tariff Graphs (Non-Zero Y-Intercept)',
                'summary': 'Why taxi and utility graphs start above (0, 0) on the vertical axis.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;"><strong>Warning:</strong> If a graph shows a courier or taxi fare starting at <strong>(0 miles, £4.00)</strong>, the £4.00 is a fixed call-out charge:</p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li>Because it does NOT start at (0, 0), you <strong>cannot</strong> simply double the 10-mile total fare to find a 20-mile fare!</li>
                    <li>Instead, find the per-mile rate (slope) by subtracting the £4.00 standing charge first.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Bidirectional Currency Exchange & Commission Deductions',
                'summary': 'Converting Pounds to foreign currency and converting leftover currency back.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Pounds (&pound;) &rarr; Euros (&euro;):</strong> Start on the Pounds axis, go to the line, read across to the Euros axis.</li>
                    <li><strong>Euros (&euro;) &rarr; Pounds (&pound;):</strong> Start on the Euros axis, go to the line, read across to the Pounds axis.</li>
                  </ol>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Healthcare Supplies Currency Conversion (GBP to Euros) (Level 1/2 Foundation)',
                'marks': '3 Marks (Pearson Edexcel Level 1/2)',
                'context': 'International Medical Equipment Purchasing',
                'question': 'A conversion graph between Pounds (£) and Euros (€) passes through <strong>(0, 0)</strong> and the point <strong>(£40, €48)</strong>.<br>(a) Use the relationship to convert <strong>£25</strong> into Euros.<br>(b) A specialist diagnostic monitor costs <strong>€360</strong> from a German supplier. Calculate its cost in Pounds (£).',
                'steps': [
                    ('Step 1', 'Find the unit exchange rate (1 Pound in Euros)', '€48 ÷ £40 = €1.20 per £1.', 'M1: Unit exchange rate (€1.20 per £1)'),
                    ('Step 2', 'Convert £25 into Euros', '25 × €1.20 = €30.00.', 'A1: Accurate conversion (€30)'),
                    ('Step 3', 'Convert €360 into Pounds (÷ 1.20 or scale from €48)', '€360 ÷ 1.20 = £300.00 (or 360 ÷ 48 = 7.5; 7.5 × £40 = £300.00).', 'A1: Accurate cost in Pounds (£300.00)')
                ],
                'final_answer': '(a) €30 | (b) £300.00',
                'tutor_tip': 'Finding the exact lattice point (£40, €48) lets you scale any value with 100% accuracy.'
            },
            {
                'title': 'Surgical Patient Weight Conversion (Stones/Pounds to kg) & Medication Dose (Level 2 Multi-Step)',
                'marks': '4 Marks (Pearson Edexcel Level 2)',
                'context': 'Anaesthetic Drug Dosage Calculation',
                'question': 'An anaesthetist calculates a patient’s medication dose at <strong>1.5 mg per kg of body weight</strong>.<br>• The patient weighs <strong>11 stone 6 lbs</strong> (where <strong>1 stone = 14 lbs</strong>).<br>• A conversion graph between kilograms (kg) and pounds (lbs) passes through <strong>(0, 0)</strong> and <strong>(20 kg, 44 lbs)</strong>.<br>Calculate the patient’s weight in kg and the required medication dose in mg.',
                'steps': [
                    ('Step 1', 'Convert 11 stone 6 lbs entirely into pounds (lbs)', '(11 × 14 lbs) + 6 lbs = 154 + 6 = 160 lbs.', 'M1: Total weight in lbs (160 lbs)'),
                    ('Step 2', 'Use the conversion graph point (20 kg = 44 lbs → 1 kg = 2.2 lbs) to convert to kg', '160 lbs ÷ 2.2 = 72.73 kg (or 160 ÷ 44 × 20 = 72.73 kg).', 'M1: Conversion to kg (72.73 kg)'),
                    ('Step 3', 'Multiply weight in kg by 1.5 mg/kg', '72.727... × 1.5 = 109.09 mg (or 109.1 mg).', 'M1 / A1: Accurate dose (109.1 mg)')
                ],
                'final_answer': 'Weight = 72.73 kg | Required Dose = 109.1 mg',
                'tutor_tip': 'Convert stones and pounds into total pounds FIRST (11 × 14 + 6 = 160 lbs) before using the lbs-to-kg conversion graph.'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Scaling a Non-Zero Intercept Tariff Graph by Multiplication',
                'desc': 'If a taxi graph starts at £3.50 for 0 miles and costs £13.50 for 5 miles, doubling £13.50 to £27.00 for 10 miles double-counts the £3.50 flag fall!',
                'fix': 'Only multiply directly when the conversion line passes through the origin (0, 0).'
            },
            {
                'title': 'Reading from the Wrong Axis (e.g. Reading 50 on X instead of 50 on Y)',
                'desc': 'Looking up 50 km on the miles axis instead of the kilometres axis.',
                'fix': 'Circle the axis label that matches the unit given in the question before drawing your reading line.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'A conversion graph between gallons and litres passes through <strong>(0, 0)</strong> and <strong>(10 gallons, 45.5 litres)</strong>. How many litres are in <strong>35 gallons</strong>?',
                'solution_steps': '1. 1 gallon = 45.5 ÷ 10 = 4.55 litres.<br>2. 35 gallons = 35 × 4.55 = 159.25 litres.',
                'correct_answer': '159.25 litres',
                'tutor_tip': 'Multiply the 10-gallon reading (45.5 L) by 3.5 to get 35 gallons.'
            },
            {
                'marks': '3 Marks',
                'question': 'A miles-to-kilometres conversion graph passes through <strong>(0, 0)</strong> and <strong>(50 miles, 80 km)</strong>. A courier drives <strong>280 km</strong> in France. Convert this distance into <strong>miles</strong>.',
                'solution_steps': '1. Scale factor: 8 km = 5 miles (or 1.6 km = 1 mile).<br>2. Miles = 280 ÷ 1.6 = 175 miles (or (280 ÷ 80) × 50 = 3.5 × 50 = 175 miles).',
                'correct_answer': '175 miles',
                'tutor_tip': 'Divide km by 8 and multiply by 5 (280 ÷ 8 = 35; 35 × 5 = 175 miles).'
            },
            {
                'marks': '3 Marks',
                'question': 'A conversion graph between Pounds (£) and US Dollars ($) passes through <strong>(£50, $64)</strong>. A nurse returning from New York exchanges <strong>$192</strong> back into Pounds, and the bureau deducts a <strong>£3.50 handling fee</strong>. How many Pounds does the nurse receive?',
                'solution_steps': '1. Scale factor from $64 to $192: 192 ÷ 64 = 3.<br>2. Gross Pounds = 3 × £50 = £150.00.<br>3. Subtract £3.50 fee: £150.00 − £3.50 = £146.50.',
                'correct_answer': '£146.50',
                'tutor_tip': '$192 is exactly 3 times $64, so it converts to 3 × £50 = £150 before the fee.'
            }
        ]
    },
    {
        'filename': 'functional-skills-probability.html',
        'clean_topic': 'Probability Scale & Single Event Outcomes',
        'intro_lead': 'Express probabilities as fractions, decimals, and percentages on the 0-to-1 scale, apply the complement rule (P(not A) = 1 − P(A)), and calculate relative frequency in quality audits.',
        'next_file': 'functional-skills-probability-tables.html',
        'next_name': 'Probability Outcomes & Tables',
        'spec_points': [
            ('L1.26 / L2.33', 'Express probabilities of single events as fractions, decimals, or percentages on a scale from 0 (impossible) to 1 (certain).'),
            ('L2.34', 'Use the property that the probabilities of all mutually exclusive outcomes sum to 1.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-dice',
                'title': 'Golden Rule 1: P(Event) = Favourable Outcomes ÷ Total Possible Outcomes',
                'desc': 'Probability is ALWAYS a number between 0 and 1 (or 0% and 100%). Write probabilities as a fraction (e.g. 3/10), a decimal (0.3), or a percentage (30%)—NEVER as a ratio (3 : 10) or words ("3 out of 10")!',
                'badge': 'P(A) = Successful Outcomes ÷ Total Outcomes (Fraction, Decimal, or %)'
            },
            {
                'icon': 'fa-shield-halved',
                'title': 'Golden Rule 2: Complement Rule — Mutually Exclusive Probabilities Sum to 1',
                'desc': 'If an event either happens or does not happen, their probabilities add up to 1 (or 100%). Therefore: P(Not A) = 1 − P(A).',
                'badge': 'P(Not A) = 1 − P(A)'
            }
        ],
        'skills': [
            {
                'title': 'The 0-to-1 Probability Scale & Equivalent Formats',
                'summary': 'Mapping likelihood terms to exact fractions, decimals, and percentages.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:center;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Likelihood Word</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Decimal Scale</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Fraction</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Percentage</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Impossible</td><td style="padding:6px; border:1px solid #cbd5e1;">0</td><td style="padding:6px; border:1px solid #cbd5e1;">0</td><td style="padding:6px; border:1px solid #cbd5e1;">0%</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Unlikely</td><td style="padding:6px; border:1px solid #cbd5e1;">0 &lt; P &lt; 0.5</td><td style="padding:6px; border:1px solid #cbd5e1;">e.g. 1/5</td><td style="padding:6px; border:1px solid #cbd5e1;">20%</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Evens (Equally Likely)</td><td style="padding:6px; border:1px solid #cbd5e1;">0.5</td><td style="padding:6px; border:1px solid #cbd5e1;">1/2</td><td style="padding:6px; border:1px solid #cbd5e1;">50%</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Likely</td><td style="padding:6px; border:1px solid #cbd5e1;">0.5 &lt; P &lt; 1</td><td style="padding:6px; border:1px solid #cbd5e1;">e.g. 4/5</td><td style="padding:6px; border:1px solid #cbd5e1;">80%</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Certain</td><td style="padding:6px; border:1px solid #cbd5e1;">1.0</td><td style="padding:6px; border:1px solid #cbd5e1;">1/1</td><td style="padding:6px; border:1px solid #cbd5e1;">100%</td></tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                'title': 'Mutually Exclusive Probability Tables (Sum = 1)',
                'summary': 'Finding missing probabilities when all possible outcomes are listed.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">When a table lists every mutually exclusive outcome (e.g. Early = 0.15, On Time = 0.72, Late = ?):</p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li>Add the known probabilities: 0.15 + 0.72 = <strong>0.87</strong>.</li>
                    <li>Subtract from 1.00: P(Late) = 1.00 &minus; 0.87 = <strong>0.13</strong>.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Experimental Probability (Relative Frequency) & Sample Size',
                'summary': 'Why larger trial counts produce more reliable probability estimates.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Relative Frequency Formula:</strong> Number of observed times event occurred &divide; Total number of trials conducted.</li>
                    <li><strong>Reliability Rule:</strong> Increasing the number of trials (e.g. testing 500 items instead of 20 items) makes the experimental probability much more reliable.</li>
                  </ul>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Hospital Emergency Blood Bank Type Selection (Level 1/2 Foundation)',
                'marks': '3 Marks (Pearson Edexcel Level 1/2)',
                'context': 'Transfusion Laboratory Blood Group Storage',
                'question': 'A hospital blood bank refrigerator stores <strong>50 units of blood</strong>:<br>• Group O: <strong>22 units</strong> | Group A: <strong>18 units</strong> | Group B: <strong>7 units</strong> | Group AB: <strong>3 units</strong><br>One unit is selected at random.<br>(a) What is the probability that the unit is Group O? Give your answer as a simplified fraction.<br>(b) What is the probability that the unit is NOT Group AB? Give your answer as a decimal.',
                'steps': [
                    ('Step 1', 'Calculate P(Group O) and simplify fraction', 'P(Group O) = 22 / 50 = 11 / 25.', 'M1 / A1: Simplified fraction (11/25)'),
                    ('Step 2', 'Calculate P(Group AB) as a decimal', 'P(Group AB) = 3 ÷ 50 = 0.06.', 'M1: Decimal conversion (0.06)'),
                    ('Step 3', 'Subtract from 1 for P(NOT Group AB)', '1 − 0.06 = 0.94 (or 47 ÷ 50 = 0.94).', 'A1: Accurate decimal answer (0.94)')
                ],
                'final_answer': '(a) 11/25 | (b) 0.94',
                'tutor_tip': 'Never write probability as a ratio like "11 : 25"—always write 11/25, 0.44, or 44%.'
            },
            {
                'title': 'Quality Control Component Testing & Expected Batch Failures (Level 2 Multi-Step)',
                'marks': '4 Marks (Pearson Edexcel Level 2)',
                'context': 'Medical Device Manufacturing QA',
                'question': 'A quality engineer tests a random sample of <strong>250 digital thermometers</strong>:<br>• <strong>235 Pass Grade A</strong>, <strong>9 Pass Grade B</strong>, and the rest <strong>Fail</strong>.<br>(a) Calculate the experimental probability (relative frequency) that a thermometer Fails, as a decimal.<br>(b) The factory manufactures a batch of <strong>4,000 thermometers</strong>. Each failed thermometer costs <strong>£8.50</strong> to scrap and replace. Calculate the expected cost of failed thermometers in this batch.',
                'steps': [
                    ('Step 1', 'Find number of failed thermometers in the 250 sample', 'Failed = 250 − (235 + 9) = 250 − 244 = 6 failed thermometers.', 'M1: Sample failure count (6)'),
                    ('Step 2', 'Calculate relative frequency of failure', 'P(Fail) = 6 ÷ 250 = 0.024 (or 2.4%).', 'A1: Accurate decimal probability (0.024)'),
                    ('Step 3', 'Calculate expected failures in 4,000 batch and multiply by £8.50', 'Expected failures = 0.024 × 4,000 = 96 thermometers.<br>Expected scrap cost = 96 × £8.50 = £816.00.', 'M1 / A1: 96 units and £816.00 total cost')
                ],
                'final_answer': '(a) P(Fail) = 0.024 | (b) £816.00 (96 expected failures)',
                'tutor_tip': 'Expected Frequency = Probability × Batch Size (0.024 × 4,000 = 96 units).'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Writing Probabilities as Ratios (e.g. 1 : 4) or Words ("1 in 5")',
                'desc': 'Pearson Edexcel mark schemes explicitly reject ratios (1 : 4) and verbal phrases ("likely" or "1 out of 5") when a numerical probability is requested.',
                'fix': 'Always write a fraction (1/5), a decimal (0.2), or a percentage (20%).'
            },
            {
                'title': 'Giving a Probability Greater Than 1',
                'desc': 'Dividing Total by Favourable (e.g. 50 ÷ 22 = 2.27) produces a number greater than 1, which is impossible for any probability.',
                'fix': 'The smaller number (part) always goes on top of the larger number (total).'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'A medical supply drawer contains <strong>15 blue tourniquets, 10 green tourniquets, and 5 yellow tourniquets</strong>. One is selected at random. What is the probability that it is <strong>green</strong>? Give your answer as a simplified fraction.',
                'solution_steps': '1. Total tourniquets = 15 + 10 + 5 = 30.<br>2. P(Green) = 10 / 30 = 1 / 3.',
                'correct_answer': '1/3',
                'tutor_tip': 'Add all categories first (15 + 10 + 5 = 30) to find the denominator.'
            },
            {
                'marks': '3 Marks',
                'question': 'A staff charity spinner has four sections: <strong>£5 Prize (P = 0.25), £10 Prize (P = 0.10), £20 Prize (P = 3x), and No Prize (P = 10x)</strong>. Calculate the value of <em>x</em> and the probability of winning a <strong>£20 Prize</strong>.',
                'solution_steps': '1. Sum of known probabilities = 0.25 + 0.10 = 0.35.<br>2. Remainder for 3x + 10x (13x) = 1.00 − 0.35 = 0.65.<br>3. x = 0.65 ÷ 13 = 0.05.<br>4. P(£20 Prize) = 3 × 0.05 = 0.15.',
                'correct_answer': 'x = 0.05; P(£20 Prize) = 0.15',
                'tutor_tip': 'All mutually exclusive sectors on a spinner must sum to 1.00.'
            },
            {
                'marks': '2 Marks',
                'question': 'Two quality inspectors test batches from the same machine. Inspector A tests <strong>20 items</strong> and finds 1 fault. Inspector B tests <strong>500 items</strong> and finds 18 faults. Whose estimate of the fault probability is more reliable, and why?',
                'solution_steps': '1. Inspector B’s estimate (18/500 = 0.036) is more reliable.<br>2. Reason: Inspector B used a much larger sample size (500 trials vs 20 trials).',
                'correct_answer': 'Inspector B, because a larger sample size (500 vs 20) gives a more reliable estimate',
                'tutor_tip': 'In statistics, a larger sample size always gives a more reliable relative frequency.'
            }
        ]
    },
    {
        'filename': 'functional-skills-probability-tables.html',
        'clean_topic': 'Probability Outcomes, Sample Space & Combined Events',
        'intro_lead': 'List systematic outcomes using sample space grids and probability tree diagrams, calculate AND/OR combined probabilities of independent events, and compute expected frequencies.',
        'next_file': 'functional-skills-maths-level-2.html',
        'next_name': 'Maths Level 2 Directory',
        'spec_points': [
            ('L2.34 / L2.35', 'Calculate probabilities of combined independent events using sample space tables, two-way grids, and tree diagrams.'),
            ('L2.35', 'Calculate expected frequencies from theoretical or experimental probabilities.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-diagram-project',
                'title': "Golden Rule 1: The AND / OR Laws — 'AND = Multiply (×)' • 'OR = Add (+)'",
                'desc': 'For two independent events A and B: the probability that BOTH happen (A AND B) is P(A) × P(B). The probability that one OR the other mutually exclusive outcome happens is P(A) + P(B).',
                'badge': 'P(A and B) = P(A) × P(B) • P(A or B) = P(A) + P(B)'
            },
            {
                'icon': 'fa-table-cells',
                'title': 'Golden Rule 2: Sample Space Grids Show Every Equally Likely Combination',
                'desc': 'When combining two spinners, two dice, or two menu choices, draw a 2D sample space grid. Total possible outcomes = Rows × Columns. Count the matching cells and divide by total cells.',
                'badge': 'Total Grid Outcomes = Outcomes(Event 1) × Outcomes(Event 2)'
            }
        ],
        'skills': [
            {
                'title': 'Sample Space Grids for Two Combined Events',
                'summary': 'Systematically listing all combinations in a 2D table so none are missed.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">When two 4-sided spinners (numbered 1 to 4) are spun and their scores are added together, there are <strong>4 &times; 4 = 16 equally likely outcomes</strong>:</p>
                  <table style="width:100%; max-width:360px; border-collapse:collapse; text-align:center;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:6px; border:1px solid #cbd5e1;">+</th>
                        <th style="padding:6px; border:1px solid #cbd5e1;">1</th>
                        <th style="padding:6px; border:1px solid #cbd5e1;">2</th>
                        <th style="padding:6px; border:1px solid #cbd5e1;">3</th>
                        <th style="padding:6px; border:1px solid #cbd5e1;">4</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700; background:#f1f5f9;">1</td><td style="padding:6px; border:1px solid #cbd5e1;">2</td><td style="padding:6px; border:1px solid #cbd5e1;">3</td><td style="padding:6px; border:1px solid #cbd5e1;">4</td><td style="padding:6px; border:1px solid #cbd5e1;">5</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700; background:#f1f5f9;">2</td><td style="padding:6px; border:1px solid #cbd5e1;">3</td><td style="padding:6px; border:1px solid #cbd5e1;">4</td><td style="padding:6px; border:1px solid #cbd5e1;">5</td><td style="padding:6px; border:1px solid #cbd5e1;">6</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700; background:#f1f5f9;">3</td><td style="padding:6px; border:1px solid #cbd5e1;">4</td><td style="padding:6px; border:1px solid #cbd5e1;">5</td><td style="padding:6px; border:1px solid #cbd5e1;">6</td><td style="padding:6px; border:1px solid #cbd5e1; background:#dcfce7; font-weight:700;">7</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700; background:#f1f5f9;">4</td><td style="padding:6px; border:1px solid #cbd5e1;">5</td><td style="padding:6px; border:1px solid #cbd5e1;">6</td><td style="padding:6px; border:1px solid #cbd5e1; background:#dcfce7; font-weight:700;">7</td><td style="padding:6px; border:1px solid #cbd5e1; background:#dcfce7; font-weight:700;">8</td></tr>
                    </tbody>
                  </table>
                  <p style="margin-top:8px; font-size:0.92rem; color:#334155;">Outcomes scoring <strong>7 or more</strong>: 3 cells out of 16 &rarr; <strong>P(Score &ge; 7) = 3/16</strong>.</p>
                </div>
                """
            },
            {
                'title': 'Probability Tree Diagrams & Multiplying Along Branches',
                'summary': 'How to calculate "Both Pass", "Both Fail", and "Exactly One Passes".',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Each Pair of Branches Sums to 1:</strong> If P(Pass) = 0.9, then the lower branch P(Fail) = <strong>0.1</strong>.</li>
                    <li><strong>Multiply Along Branches:</strong> P(Pass AND Pass) = 0.9 &times; 0.9 = <strong>0.81</strong>.</li>
                    <li><strong>Add Separate End Outcomes:</strong> P(Exactly One Fails) = P(Pass, Fail) + P(Fail, Pass) = (0.9 &times; 0.1) + (0.1 &times; 0.9) = 0.09 + 0.09 = <strong>0.18</strong>.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'At Least One Event Shortcut: 1 − P(None)',
                'summary': 'The fastest way to find the probability that at least one alarm or backup triggers.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">Instead of adding three separate branches for "at least one passes", simply calculate <strong>P(Both Fail)</strong> and subtract from 1:</p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>P(At Least One Works) = 1 &minus; P(Both Fail)</strong>.</li>
                  </ul>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Backup Hospital Generator Independent Reliability (Level 2 Core)',
                'marks': '3 Marks (Pearson Edexcel Level 2)',
                'context': 'Critical Care Power Redundancy',
                'question': 'A hospital intensive care unit has two independent backup generators, Generator A and Generator B.<br>• The probability that Generator A fails during a storm is <strong>0.05</strong>.<br>• The probability that Generator B fails during a storm is <strong>0.04</strong>.<br>(a) Calculate the probability that <strong>both</strong> generators fail at the same time.<br>(b) Calculate the probability that <strong>neither</strong> generator fails (both work).',
                'steps': [
                    ('Step 1', 'Multiply failure probabilities for P(Both Fail)', 'P(A fails AND B fails) = 0.05 × 0.04 = 0.002.', 'M1 / A1: Accurate combined failure probability (0.002)'),
                    ('Step 2', 'Find working probabilities for each generator', 'P(A works) = 1 − 0.05 = 0.95.<br>P(B works) = 1 − 0.04 = 0.96.', 'M1: Complement probabilities (0.95 and 0.96)'),
                    ('Step 3', 'Multiply working probabilities for P(Both Work)', 'P(Both work) = 0.95 × 0.96 = 0.912 (or 91.2%).', 'A1: Accurate combined working probability (0.912)')
                ],
                'final_answer': '(a) P(Both fail) = 0.002 | (b) P(Both work) = 0.912',
                'tutor_tip': 'Notice that 0.05 × 0.04 = 0.002 (three decimal places), NOT 0.02! Never add probabilities when asked for "BOTH" (AND).'
            },
            {
                'title': 'Fundraising Fair Two-Spinner Game Financial Profit Projection (Level 2 Multi-Step)',
                'marks': '4 Marks (Pearson Edexcel Level 2)',
                'context': 'Charity Fundraising Event Planning',
                'question': 'At a hospital charity fair, players pay <strong>£2.00 per game</strong> to spin two fair spinners:<br>• <strong>Spinner A</strong> has 3 equal sections numbered <strong>1, 2, 3</strong>.<br>• <strong>Spinner B</strong> has 4 equal sections numbered <strong>2, 4, 6, 8</strong>.<br>• The player wins a <strong>£5.00 cash prize</strong> if the <strong>sum of the two spinners is 9 or more</strong>.<br>If <strong>180 people</strong> play the game, calculate the expected net profit raised for the hospital charity.',
                'steps': [
                    ('Step 1', 'Determine total outcomes in the sample space and winning combinations (Sum ≥ 9)', 'Total outcomes = 3 × 4 = 12 equally likely combinations.<br>Sums ≥ 9: (1+8=9), (2+8=10), (3+6=9), (3+8=11) → 4 winning outcomes.', 'M1: Sample space 4 out of 12 (1/3)'),
                    ('Step 2', 'Calculate expected number of winners out of 180 players', 'P(Win) = 4/12 = 1/3.<br>Expected winners = (1/3) × 180 = 60 winners.', 'M1: Expected winners (60)'),
                    ('Step 3', 'Calculate total entry revenue minus total prize payouts', 'Total Revenue = 180 × £2.00 = £360.00.<br>Total Prize Payout = 60 × £5.00 = £300.00.<br>Expected Net Profit = £360.00 − £300.00 = £60.00.', 'M1 / A1: Accurate net profit (£60.00)')
                ],
                'final_answer': '£60.00 expected net profit (P(Win) = 4/12 = 1/3; 60 expected winners)',
                'tutor_tip': 'List all 12 pairs in a 3×4 grid so you do not miss any winning combination!'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Adding Probabilities Instead of Multiplying for "Both Happen" (AND)',
                'desc': 'Computing P(A and B) as 0.05 + 0.04 = 0.09 instead of 0.05 × 0.04 = 0.002.',
                'fix': 'Remember: AND = Multiply (×); OR = Add (+).'
            },
            {
                'title': 'Decimal Place Error When Multiplying Small Decimals (0.2 × 0.3 = 0.06, NOT 0.6)',
                'desc': 'Writing 0.2 × 0.3 as 0.6 instead of 0.06.',
                'fix': 'Count total decimal digits: 1 dp + 1 dp = 2 decimal places in the product (0.06).'
            }
        ],
        'practice_questions': [
            {
                'marks': '3 Marks',
                'question': 'The probability that a delivery train arrives on time on Monday is <strong>0.8</strong>, and the probability it arrives on time on Tuesday is <strong>0.7</strong> (independent events). Calculate:<br>(a) The probability that it arrives on time on <strong>both</strong> days.<br>(b) The probability that it is <strong>late on both</strong> days.',
                'solution_steps': '1. P(Both on time) = 0.8 × 0.7 = 0.56.<br>2. P(Late Mon) = 1 − 0.8 = 0.2; P(Late Tue) = 1 − 0.7 = 0.3.<br>3. P(Both late) = 0.2 × 0.3 = 0.06.',
                'correct_answer': '(a) 0.56 | (b) 0.06',
                'tutor_tip': 'Find the individual late probabilities first (0.2 and 0.3), then multiply them together (0.06).'
            },
            {
                'marks': '3 Marks',
                'question': 'Using the train probabilities from Question 1 (On time Mon = 0.8, On time Tue = 0.7), calculate the probability that the train arrives on time on <strong>exactly one</strong> of the two days.',
                'solution_steps': '1. Way 1 (On time Mon AND Late Tue) = 0.8 × 0.3 = 0.24.<br>2. Way 2 (Late Mon AND On time Tue) = 0.2 × 0.7 = 0.14.<br>3. Total P(Exactly one day on time) = 0.24 + 0.14 = 0.38.',
                'correct_answer': '0.38',
                'tutor_tip': 'Check: 0.56 (both on time) + 0.06 (both late) + 0.38 (one of each) = 1.00!'
            },
            {
                'marks': '3 Marks',
                'question': 'Two fair 6-sided dice are rolled and their scores are added together. Out of the <strong>36 possible outcomes</strong>, how many outcomes give a total score of <strong>10 or more</strong>, and what is the probability as a simplified fraction?',
                'solution_steps': '1. Sums ≥ 10: (4,6), (5,5), (6,4) [sum 10]; (5,6), (6,5) [sum 11]; (6,6) [sum 12] → 6 outcomes.<br>2. Probability = 6 / 36 = 1 / 6.',
                'correct_answer': '6 outcomes; Probability = 1/6',
                'tutor_tip': 'List the pairs systematically: three ways to make 10, two ways to make 11, one way to make 12 = 6/36 = 1/6.'
            }
        ]
    }
]
