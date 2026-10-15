#!/usr/bin/env python3
import maths_domain5_stats_prob

all_d5 = list(maths_domain5_stats_prob.TOPICS_DOMAIN5)

more_d5 = [
    {
        "filename": "functional-skills-bar-charts.html",
        "clean_topic": "Bar Charts: Dual, Component & Frequency",
        "intro_lead": "Construct and interpret single, dual (grouped), and component (stacked) bar charts, read linear vertical scales, and compare departmental statistics.",
        "next_file": "functional-skills-line-graphs.html",
        "next_name": "Line Graphs",
        "spec_points": [
            ("L1.25 / L2.31", "Draw and interpret bar charts, including dual bar charts and comparative charts, with appropriate titles, labels, and linear scales.")
        ],
        "golden_rules": [
            {
                "icon": "fa-chart-column",
                "title": "Golden Rule 1: S-L-A-P-T for Drawing Graphs",
                "desc": "Scale (linear and even) • Labels (both axes clearly labeled with units) • Axes (ruled with a straight ruler) • Points/Bars (accurate heights and equal widths) • Title (comprehensive title stating what the chart shows).",
                "badge": "Scale • Labels • Axes • Points/Bars • Title (SLAPT)"
            },
            {
                "icon": "fa-arrows-left-right",
                "title": "Golden Rule 2: Gaps Between Bars Must Be Equal",
                "desc": "In a bar chart for discrete data, leave an equal gap between categories. In a dual bar chart, touch the paired bars together, then leave an equal gap before the next pair.",
                "badge": "Equal bar widths • Equal gaps between categories"
            }
        ],
        "skills": [
            {
                "title": "Single vs Dual vs Component Bar Charts",
                "summary": "The three bar chart formats tested in Functional Skills.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Single Bar Chart:</strong> Compares one variable across categories (e.g. patients per ward).</li>
                    <li><strong>Dual (Grouped) Bar Chart:</strong> Compares two sets side-by-side with a key (e.g. admissions vs discharges).</li>
                    <li><strong>Component (Stacked) Bar Chart:</strong> Bars are divided into colored segments showing proportions of a total.</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Hospital Surgical Department Monthly Operations Audit Chart",
                "marks": "3 Marks (Pearson Edexcel Level 1/2)",
                "context": "Surgical Theatre Performance Reporting",
                "question": "A dual bar chart compares scheduled vs emergency operations across 4 months. In October, scheduled operations bar is at <strong>85</strong> and emergency operations bar is at <strong>40</strong>. In November, scheduled is <strong>70</strong> and emergency is <strong>55</strong>.<br>(a) In which month was the total number of operations highest?<br>(b) Calculate the percentage change in emergency operations from October to November.",
                "steps": [
                    ("Step 1", "Sum operations for October and November", "October Total = 85 + 40 = 125 operations.<br>November Total = 70 + 55 = 125 operations.<br>Both months had the exact same total (125 operations).", "M1: Reading bars and summing monthly totals"),
                    ("Step 2", "Calculate change in emergency operations", "Emergency rose from 40 to 55: Increase = 55 - 40 = 15 operations.", "M1: Difference calculation"),
                    ("Step 3", "Calculate percentage increase (Change ÷ Original × 100)", "Percentage Increase = (15 ÷ 40) × 100 = 37.5%.", "A1: Accurate percentage change calculation")
                ],
                "final_answer": "(a) Both months had an equal total of 125 operations | (b) Emergency operations increased by 37.5%.",
                "tutor_tip": "Notice you divide the increase (15) by the ORIGINAL October figure (40), NOT the new November figure."
            }
        ],
        "examiner_traps": [
            {
                "title": "Misreading Non-Zero or Uneven Scales",
                "desc": "Check whether each grid square represents 1, 2, 5, or 10 units. Count before reading bar heights.",
                "fix": "Always verify: 'How much is one small grid square worth?'"
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A bar chart shows sales for Monday (£450), Tuesday (£300), Wednesday (£550). What is the total sales revenue across the three days?",
                "solution_steps": "1. Total = 450 + 300 + 550.<br>2. Total = £1,300.00.",
                "correct_answer": "£1,300.00",
                "tutor_tip": "Sum the three values: 450 + 300 + 550 = 1,300."
            }
        ]
    },
    {
        "filename": "functional-skills-line-graphs.html",
        "clean_topic": "Line Graphs & Trend Analysis",
        "intro_lead": "Plot and read continuous line graphs, interpret upward and downward trends over time, interpolate between plotted points, and extract critical operational milestones.",
        "next_file": "functional-skills-pie-charts.html",
        "next_name": "Pie Charts",
        "spec_points": [
            ("L1.25 / L2.31", "Draw and interpret line graphs showing trends over time with appropriate scales and labels.")
        ],
        "golden_rules": [
            {
                "icon": "fa-chart-line",
                "title": "Golden Rule 1: Time Almost Always Belongs on the Horizontal X-Axis",
                "desc": "When plotting continuous time series data (hours, days, months, years), time is the independent variable and goes along the bottom horizontal X-axis.",
                "badge": "Time = Horizontal X-Axis | Measured Value = Vertical Y-Axis"
            },
            {
                "icon": "fa-arrow-trend-up",
                "title": "Golden Rule 2: Describing Trends: Direction + Context",
                "desc": "When asked to describe a trend, state both the general direction (e.g. 'steady increase') and cite specific data points (e.g. 'rising from 120 in January to peak at 340 in July').",
                "badge": "State Direction (Rise/Fall) + Cite Start/Peak Numbers"
            }
        ],
        "skills": [
            {
                "title": "Interpolation vs Extrapolation",
                "summary": "Reading between points vs predicting future values.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Interpolation:</strong> Estimating a value <em>inside</em> the recorded range (e.g. reading patient temperature at 14:30 from points at 14:00 and 15:00) — highly reliable.</li>
                    <li><strong>Extrapolation:</strong> Predicting a value <em>beyond</em> the recorded range by extending the trend line — less reliable.</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Hospital ICU Patient Body Temperature Monitoring Line Graph",
                "marks": "3 Marks (Pearson Edexcel Level 1/2)",
                "context": "Intensive Care Clinical Observation",
                "question": "A clinical line graph records an ICU patient's temperature every 2 hours from 08:00 to 18:00:<br>• 08:00: 38.8°C<br>• 10:00: 38.4°C<br>• 12:00: 37.8°C<br>• 14:00: 37.2°C<br>• 16:00: 36.9°C<br>• 18:00: 37.0°C<br>(a) Describe the overall trend in the patient's temperature over the 10-hour period.<br>(b) Estimate the patient's temperature at 11:00.",
                "steps": [
                    ("Step 1", "Analyze the overall trend direction with values", "The patient's temperature shows a steady downward trend, falling from a fever of 38.8°C at 08:00 to normal body temperature (37.0°C) by 18:00.", "A1: Accurate trend description with start/end data"),
                    ("Step 2", "Interpolate between 10:00 (38.4°C) and 12:00 (37.8°C)", "11:00 is halfway between 10:00 and 12:00.<br>Midpoint = (38.4 + 37.8) ÷ 2 = 76.2 ÷ 2 = 38.1°C.", "M1: Interpolation method"),
                    ("Step 3", "State estimated temperature with units", "Estimated Temperature at 11:00 = 38.1°C.", "A1: Accurate interpolated value with units")
                ],
                "final_answer": "(a) Steady downward trend from 38.8°C to 37.0°C | (b) Estimated temperature at 11:00 = 38.1°C.",
                "tutor_tip": "When describing a trend, always mention that it decreased and give the starting and ending numbers."
            }
        ],
        "examiner_traps": [
            {
                "title": "Writing Simply 'It Went Down' Without Numbers",
                "desc": "Exam rubrics require candidates to support trend statements with figures from the graph.",
                "fix": "Always include: '...decreasing from [X] to [Y]'."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A depot fuel usage line graph starts at 400 L on Monday and drops steadily to 100 L on Friday. Describe the trend in fuel remaining.",
                "solution_steps": "1. Trend: There is a steady decrease in fuel remaining.<br>2. Figures: Fuel drops by 300 litres, from 400 L on Monday to 100 L on Friday.",
                "correct_answer": "Steady decrease from 400 L on Monday to 100 L on Friday.",
                "tutor_tip": "State direction and cite starting and ending quantities."
            }
        ]
    },
    {
        "filename": "functional-skills-pie-charts.html",
        "clean_topic": "Pie Charts & Proportional Angles",
        "intro_lead": "Calculate pie chart sector angles (Degrees = Frequency ÷ Total × 360°), draw sectors using a protractor, and extract frequencies from proportional pie charts.",
        "next_file": "functional-skills-scatter-graphs.html",
        "next_name": "Scatter Graphs & Correlation",
        "spec_points": [
            ("L1.25 / L2.31", "Draw and interpret pie charts, calculating sector angles and converting angles to frequencies.")
        ],
        "golden_rules": [
            {
                "icon": "fa-chart-pie",
                "title": "Golden Rule 1: The Magic Multiplier: 360° ÷ Total Frequency",
                "desc": "Divide 360° by the total frequency to find how many degrees represent ONE person/item. Multiply each category's frequency by this magic number.",
                "badge": "Degrees per Item = 360° ÷ Total Frequency (N)"
            },
            {
                "icon": "fa-rotate",
                "title": "Golden Rule 2: Finding Frequency from an Angle: Angle ÷ 360 × Total",
                "desc": "If a question gives an angle (e.g. 90°) and a total of 200 people: Frequency = (Angle ÷ 360) × Total = (90 ÷ 360) × 200 = 1/4 × 200 = 50 people.",
                "badge": "Frequency = (Sector Angle ÷ 360°) × Total Frequency"
            }
        ],
        "skills": [
            {
                "title": "Pie Chart Angle Calculation Table",
                "summary": "Setting up the standard 4-column exam table.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">For 72 total hospital admissions: Magic Multiplier = 360° ÷ 72 = <strong>5° per patient</strong>.</p>
                  <table style="width:100%; border-collapse:collapse; text-align:center;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:6px; border:1px solid #cbd5e1;">Ward</th>
                        <th style="padding:6px; border:1px solid #cbd5e1;">Patients</th>
                        <th style="padding:6px; border:1px solid #cbd5e1;">Calculation (× 5°)</th>
                        <th style="padding:6px; border:1px solid #cbd5e1;">Angle (°)</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1;">Medical</td><td style="padding:6px; border:1px solid #cbd5e1;">36</td><td style="padding:6px; border:1px solid #cbd5e1;">36 × 5°</td><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">180°</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1;">Surgical</td><td style="padding:6px; border:1px solid #cbd5e1;">18</td><td style="padding:6px; border:1px solid #cbd5e1;">18 × 5°</td><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">90°</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1;">Orthopaedic</td><td style="padding:6px; border:1px solid #cbd5e1;">18</td><td style="padding:6px; border:1px solid #cbd5e1;">18 × 5°</td><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">90°</td></tr>
                      <tr style="background:#e0f2fe; font-weight:800; color:#0369a1;"><td style="padding:6px; border:1px solid #cbd5e1;">Total</td><td style="padding:6px; border:1px solid #cbd5e1;">72</td><td style="padding:6px; border:1px solid #cbd5e1;">72 × 5°</td><td style="padding:6px; border:1px solid #cbd5e1;">360°</td></tr>
                    </tbody>
                  </table>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Hospital Trust Energy Consumption Breakdown Pie Chart",
                "marks": "3 Marks (Pearson Edexcel Level 2)",
                "context": "Facility Environmental Sustainability",
                "question": "A hospital records its annual energy consumption by source:<br>• Gas: <strong>500 MWh</strong><br>• Electricity: <strong>300 MWh</strong><br>• Solar Panels: <strong>100 MWh</strong><br>• Biomass: <strong>100 MWh</strong><br>Total = 1,000 MWh.<br>Calculate the sector angle in degrees for each energy source on a pie chart.",
                "steps": [
                    ("Step 1", "Calculate degrees per MWh (360° ÷ Total)", "360° ÷ 1,000 MWh = 0.36° per MWh.", "M1: Angle multiplier calculation"),
                    ("Step 2", "Multiply each energy quantity by 0.36°", "Gas = 500 × 0.36° = 180°<br>Electricity = 300 × 0.36° = 108°<br>Solar = 100 × 0.36° = 36°<br>Biomass = 100 × 0.36° = 36°", "M1: Sector angle multiplications"),
                    ("Step 3", "Check that angles sum to 360°", "180° + 108° + 36° + 36° = 360°. Confirmed.", "A1: Accurate angles for all 4 sectors")
                ],
                "final_answer": "Gas = 180°, Electricity = 108°, Solar = 36°, Biomass = 36°",
                "tutor_tip": "Notice: Gas is 500 out of 1,000 (half of the total), so its angle is exactly half of 360° = 180°."
            }
        ],
        "examiner_traps": [
            {
                "title": "Angles Not Summing to 360°",
                "desc": "Rounding angles too early can result in 359° or 361°, which loses the check mark.",
                "fix": "Always sum your calculated sector angles before drawing."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "In a pie chart representing 120 staff members, the 'Full-Time' sector has an angle of 210°. How many staff members work full-time?",
                "solution_steps": "1. Fraction = 210° ÷ 360° = 7/12.<br>2. Staff = 7/12 × 120 = 7 × 10 = 70 staff members.",
                "correct_answer": "70 staff members",
                "tutor_tip": "210 ÷ 360 × 120 = 70."
            }
        ]
    },
    {
        "filename": "functional-skills-scatter-graphs.html",
        "clean_topic": "Scatter Graphs, Correlation & Lines of Best Fit",
        "intro_lead": "Plot bivariate data on scatter diagrams, identify positive, negative, and zero correlation, draw lines of best fit by eye, and make interpolative predictions.",
        "next_file": "functional-skills-conversion-graphs.html",
        "next_name": "Conversion Graphs",
        "spec_points": [
            ("L2.32", "Draw and interpret scatter diagrams and recognise positive, negative, and zero correlation, drawing lines of best fit.")
        ],
        "golden_rules": [
            {
                "icon": "fa-chart-simple",
                "title": "Golden Rule 1: Three Types of Correlation",
                "desc": "Positive Correlation: As X increases, Y increases (points slope upwards). Negative Correlation: As X increases, Y decreases (points slope downwards). Zero Correlation: Points are scattered randomly (no relationship).",
                "badge": "Positive (Slopes Up) • Negative (Slopes Down) • Zero (Random)"
            },
            {
                "icon": "fa-ruler",
                "title": "Golden Rule 2: Drawing the Line of Best Fit",
                "desc": "Use a clear straight ruler. The line should follow the general trend and have approximately equal numbers of plotted points above and below the line.",
                "badge": "Straight line • Equal points above and below • Extends across data"
            }
        ],
        "skills": [
            {
                "title": "Using the Line of Best Fit to Make Estimates",
                "summary": "Drawing dashed reading lines up and across.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li>Find the given value on the horizontal X-axis.</li>
                    <li>Use a ruler to draw a vertical dashed line straight up to hit your line of best fit.</li>
                    <li>Draw a horizontal dashed line directly across to the Y-axis and read the value.</li>
                    <li>Always show these dashed lines on your graph to secure method marks!</li>
                  </ol>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Logistics Van Fuel Consumption vs Cargo Payload Scatter Analysis",
                "marks": "3 Marks (Pearson Edexcel Level 2)",
                "context": "Fleet Fuel Efficiency Optimization",
                "question": "A fleet manager plots cargo payload (kg) on the X-axis against fuel consumption (litres per 100 km) on the Y-axis for 10 delivery vans.<br>(a) What type of correlation would you expect between vehicle cargo weight and fuel consumption? Give a real-world reason.<br>(b) Using a line of best fit where a 500 kg payload corresponds to 8.2 L/100km, estimate the fuel required for a 600 km round trip carrying a 500 kg load.",
                "steps": [
                    ("Step 1", "State correlation type and justification", "Positive correlation. As cargo weight increases, the engine requires more power to move the heavier vehicle, which increases fuel consumption.", "A1: Correct correlation with vocational reason"),
                    ("Step 2", "Extract fuel consumption rate from line of best fit", "At 500 kg payload, fuel rate = 8.2 litres per 100 km.", "M1: Line of best fit rate extraction"),
                    ("Step 3", "Calculate total fuel for 600 km", "Journey = 600 km = 6 × 100 km.<br>Total fuel = 6 × 8.2 litres = 49.2 litres.", "A1: Accurate total fuel calculation")
                ],
                "final_answer": "(a) Positive correlation (heavier vehicles consume more fuel) | (b) Total Fuel = 49.2 litres.",
                "tutor_tip": "Always link correlation to physical reality: 'Heavier load = more fuel needed = positive correlation'."
            }
        ],
        "examiner_traps": [
            {
                "title": "Joining the Dots Like a Dot-to-Dot Puzzle",
                "desc": "Never join plotted points with zigzag lines on a scatter graph! Draw a single straight line of best fit with a ruler.",
                "fix": "Always use a ruler to draw ONE straight line through the middle of the points."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A scatter graph plots outdoor temperature against winter heating oil consumption. What type of correlation is this?",
                "solution_steps": "1. As outdoor temperature increases, heating oil usage decreases.<br>2. This is Negative correlation.",
                "correct_answer": "Negative correlation",
                "tutor_tip": "When one variable goes up and the other goes down, it is negative correlation."
            }
        ]
    },
    {
        "filename": "functional-skills-conversion-graphs.html",
        "clean_topic": "Conversion Graphs & Currency Exchange",
        "intro_lead": "Read and use linear conversion graphs to convert between currencies (GBP to EUR/USD), metric and imperial units (miles to km, kg to lbs), and utility tariffs.",
        "next_file": "functional-skills-probability.html",
        "next_name": "Probability",
        "spec_points": [
            ("L1.25 / L2.31", "Use conversion graphs to convert between units and currencies.")
        ],
        "golden_rules": [
            {
                "icon": "fa-chart-line",
                "title": "Golden Rule 1: Use Scaling for Values Beyond the Graph",
                "desc": "If a graph only goes up to £50 (€60) and you need to convert £250: find £50 on the graph (€60) and multiply by 5 (5 × €60 = €300).",
                "badge": "Scale up: £250 = 5 × £50 on the graph"
            },
            {
                "icon": "fa-pencil",
                "title": "Golden Rule 2: Show Your Reading Lines on the Axis",
                "desc": "Always draw light pencil lines from the axis to the graph line and across to the other axis. Examiners give method marks for visible reading lines.",
                "badge": "Draw dashed lines from axis → graph line → target axis"
            }
        ],
        "skills": [
            {
                "title": "Miles to Kilometres Conversion Graph",
                "summary": "Using the 5 miles = 8 km linear relationship.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li>5 miles = 8 km</li>
                    <li>10 miles = 16 km</li>
                    <li>25 miles = 40 km</li>
                    <li>50 miles = 80 km</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Healthcare Supplies Currency Conversion (GBP to Euros)",
                "marks": "3 Marks (Pearson Edexcel Level 1/2)",
                "context": "International Medical Equipment Purchasing",
                "question": "A conversion graph between Pounds (£) and Euros (€) passes through the origin (0, 0) and the point <strong>(£40, €48)</strong>.<br>(a) Use the graph to convert £20 into Euros.<br>(b) A specialist diagnostic monitor costs <strong>€240</strong> from a German supplier. Use scaling from the graph to calculate its cost in Pounds.",
                "steps": [
                    ("Step 1", "Read/calculate £20 in Euros", "Since £40 = €48, halve both values: £20 = €48 ÷ 2 = €24.00.", "A1: Accurate direct conversion (€24)"),
                    ("Step 2", "Determine scaling factor for €240 from known point (€48)", "Scale factor = €240 ÷ €48 = 5.", "M1: Scaling factor calculation"),
                    ("Step 3", "Multiply known pound value by scale factor", "Cost in Pounds = 5 × £40 = £200.00.", "A1: Accurate scaled conversion (£200.00)")
                ],
                "final_answer": "(a) £20 = €24 | (b) €240 = £200.00",
                "tutor_tip": "Notice how scaling by 5 (€48 × 5 = €240, £40 × 5 = £200) allows you to convert amounts far larger than the graph's printed boundary."
            }
        ],
        "examiner_traps": [
            {
                "title": "Misreading the Non-Square Grid Gridlines",
                "desc": "Check the spacing: 10 grid lines on the horizontal axis might represent £20 (each line = £2), while on the vertical axis 10 lines represent €50 (each line = €5).",
                "fix": "Always calculate the value of 1 grid square for BOTH axes separately."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A conversion graph shows 5 gallons = 22.5 litres. How many litres are in 20 gallons?",
                "solution_steps": "1. Scaling factor: 20 gallons = 4 × 5 gallons.<br>2. Litres = 4 × 22.5 = 90 litres.",
                "correct_answer": "90 litres",
                "tutor_tip": "Multiply 22.5 litres by 4."
            }
        ]
    },
    {
        "filename": "functional-skills-probability.html",
        "clean_topic": "Probability Scale & Single Event Outcomes",
        "intro_lead": "Express probability as fractions, decimals, and percentages, place likelihoods on the 0-to-1 probability scale, and calculate theoretical vs experimental probabilities in clinical and safety audits.",
        "next_file": "functional-skills-probability-tables.html",
        "next_name": "Probability Outcomes & Tables",
        "spec_points": [
            ("L1.26 / L2.33", "Express probabilities of single events as fractions, decimals, and percentages on a scale from 0 to 1."),
            ("L2.34", "Understand that the sum of all mutually exclusive probabilities equals 1.")
        ],
        "golden_rules": [
            {
                "icon": "fa-dice",
                "title": "Golden Rule 1: Probability Formula: Successful Outcomes ÷ Total Possible",
                "desc": "Probability of an event P(E) = Number of successful outcomes ÷ Total number of possible outcomes. Always write as a simplified fraction or decimal.",
                "badge": "P(Event) = Favourable Outcomes ÷ Total Possible Outcomes"
            },
            {
                "icon": "fa-shield-halved",
                "title": "Golden Rule 2: Mutually Exclusive Probabilities Sum to Exactly 1",
                "desc": "If an event MUST happen, P(Happens) + P(Does not happen) = 1. Therefore, P(Failure) = 1 - P(Success).",
                "badge": "P(Not A) = 1 - P(A)"
            }
        ],
        "skills": [
            {
                "title": "The 0-to-1 Probability Continuum",
                "summary": "Vocabulary and numerical values on the probability scale.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:center;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Likelihood</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Fraction / Value</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Percentage</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Impossible</td><td style="padding:6px; border:1px solid #cbd5e1;">0</td><td style="padding:6px; border:1px solid #cbd5e1;">0%</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Unlikely</td><td style="padding:6px; border:1px solid #cbd5e1;">Between 0 and 0.5</td><td style="padding:6px; border:1px solid #cbd5e1;">&lt; 50%</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Evens</td><td style="padding:6px; border:1px solid #cbd5e1;">1/2 (0.5)</td><td style="padding:6px; border:1px solid #cbd5e1;">50%</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Likely</td><td style="padding:6px; border:1px solid #cbd5e1;">Between 0.5 and 1</td><td style="padding:6px; border:1px solid #cbd5e1;">&gt; 50%</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Certain</td><td style="padding:6px; border:1px solid #cbd5e1;">1</td><td style="padding:6px; border:1px solid #cbd5e1;">100%</td></tr>
                    </tbody>
                  </table>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Hospital Emergency Blood Bank Type Compatibility Selection",
                "marks": "3 Marks (Pearson Edexcel Level 1/2)",
                "context": "Transfusion Laboratory Blood Group Storage",
                "question": "A hospital blood bank refrigerator stores <strong>50 units of blood</strong>:<br>• Group O: <strong>22 units</strong><br>• Group A: <strong>18 units</strong><br>• Group B: <strong>7 units</strong><br>• Group AB: <strong>3 units</strong><br>A biomedical scientist selects one unit at random.<br>(a) What is the probability that the unit is Group O? Give your answer as a fraction in its simplest form.<br>(b) What is the probability that the unit is NOT Group AB? Give your answer as a decimal.",
                "steps": [
                    ("Step 1", "Calculate probability of Group O (22 out of 50)", "P(Group O) = 22 ÷ 50.<br>Simplify by dividing top and bottom by 2: 22/50 = 11/25.", "M1: Fraction formulation and simplification"),
                    ("Step 2", "Calculate probability of Group AB", "P(Group AB) = 3 ÷ 50 = 0.06.", "M1: Decimal conversion"),
                    ("Step 3", "Calculate probability of NOT Group AB (1 - P(AB))", "P(NOT Group AB) = 1 - 0.06 = 0.94 (or 47/50 = 0.94).", "A1: Accurate decimal answer (0.94)")
                ],
                "final_answer": "(a) P(Group O) = 11/25 | (b) P(NOT Group AB) = 0.94",
                "tutor_tip": "Notice: Probabilities can be given as simplified fractions (11/25) or decimals (0.94). Never write probability as a ratio like '11 to 25'!"
            }
        ],
        "examiner_traps": [
            {
                "title": "Writing Probabilities as Ratios (e.g. 1 : 4)",
                "desc": "Exam boards will NOT accept ratios for probability. You must write a fraction (1/5), a decimal (0.2), or a percentage (20%).",
                "fix": "Always write probability as a fraction: Successful ÷ Total."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A box contains 15 blue pens, 10 black pens, and 5 red pens. A pen is taken at random. What is the probability that it is black? Give your answer as a simplified fraction.",
                "solution_steps": "1. Total pens = 15 + 10 + 5 = 30.<br>2. Black pens = 10.<br>3. P(Black) = 10/30 = 1/3.",
                "correct_answer": "1/3",
                "tutor_tip": "Simplify 10/30 by dividing top and bottom by 10 to get 1/3."
            }
        ]
    },
    {
        "filename": "functional-skills-probability-tables.html",
        "clean_topic": "Probability Outcomes, Sample Space & Combined Events",
        "intro_lead": "List systematic outcomes using sample space diagrams and two-way grids, calculate probabilities of combined independent events, and calculate expected frequencies in risk assessments.",
        "next_file": "functional-skills-maths-level-2.html",
        "next_name": "Maths Level 2 Directory",
        "spec_points": [
            ("L2.34 / L2.35", "Calculate probabilities of combined independent events and use tree diagrams or sample space tables."),
            ("L2.35", "Calculate expected frequency of an outcome given its probability.")
        ],
        "golden_rules": [
            {
                "icon": "fa-table-cells",
                "title": "Golden Rule 1: Sample Space Grids Show ALL Combined Outcomes",
                "desc": "When combining two independent events (e.g. rolling two dice or testing two components), use a 2D grid where rows represent Event 1 and columns represent Event 2. Total outcomes = Rows × Columns.",
                "badge": "Total Outcomes = Outcomes(A) × Outcomes(B)"
            },
            {
                "icon": "fa-calculator",
                "title": "Golden Rule 2: Expected Frequency = Probability × Number of Trials",
                "desc": "To find how many times an outcome is expected to happen over 600 trials: Expected Number = P(Event) × Total Trials.",
                "badge": "Expected Frequency = P × N"
            }
        ],
        "skills": [
            {
                "title": "Sample Space Diagram for Two Events",
                "summary": "Systematically listing all combinations to avoid missing outcomes.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">When testing two medical machines (Machine 1: Pass/Fail; Machine 2: Pass/Fail):</p>
                  <table style="width:260px; border-collapse:collapse; text-align:center;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:6px; border:1px solid #cbd5e1;">M1 \ M2</th>
                        <th style="padding:6px; border:1px solid #cbd5e1;">Pass</th>
                        <th style="padding:6px; border:1px solid #cbd5e1;">Fail</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Pass</td><td style="padding:6px; border:1px solid #cbd5e1;">(P, P)</td><td style="padding:6px; border:1px solid #cbd5e1;">(P, F)</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Fail</td><td style="padding:6px; border:1px solid #cbd5e1;">(F, P)</td><td style="padding:6px; border:1px solid #cbd5e1;">(F, F)</td></tr>
                    </tbody>
                  </table>
                  <p style="margin-top:8px; font-size:0.9rem; color:#475569;">Total outcomes = 2 × 2 = 4 outcomes.</p>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Pharmaceutical Quality Assurance Batch Defect Probability",
                "marks": "3 Marks (Pearson Edexcel Level 2)",
                "context": "Pharmaceutical Quality Control Testing",
                "question": "A medical device manufacturing line has a known defect rate of <strong>0.02 (2%)</strong>.<br>(a) What is the probability that a randomly chosen device is NOT defective?<br>(b) In a production run of <strong>15,000 devices</strong>, how many defective units are expected?",
                "steps": [
                    ("Step 1", "Apply complement rule for non-defective probability", "P(Not defective) = 1 - P(Defective) = 1 - 0.02 = 0.98 (or 98%).", "A1: Accurate non-defective probability"),
                    ("Step 2", "Apply Expected Frequency formula (P × Total Trials)", "Expected Defective Devices = 0.02 × 15,000.", "M1: Expected frequency formula setup"),
                    ("Step 3", "Compute expected defective units", "0.02 × 15,000 = 300 devices.", "A1: Accurate expected defective count")
                ],
                "final_answer": "(a) P(Not defective) = 0.98 | (b) Expected Defective Units = 300 devices.",
                "tutor_tip": "Notice how 2% of 15,000 is calculated: 1% is 150, so 2% is 2 × 150 = 300 devices."
            }
        ],
        "examiner_traps": [
            {
                "title": "Confusing Probability with Expected Frequency",
                "desc": "If asked 'How many units are expected to fail?', answering 0.02 is wrong. 0.02 is the PROBABILITY; the expected count is 300 UNITS.",
                "fix": "Always multiply the probability by the total number of items."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "The probability that a bus arrives on time is 0.85. Out of 200 scheduled bus journeys, how many are expected to arrive on time?",
                "solution_steps": "1. Expected = Probability × Total = 0.85 × 200.<br>2. 0.85 × 200 = 170 journeys.",
                "correct_answer": "170 journeys",
                "tutor_tip": "Expected frequency = P × N = 0.85 × 200 = 170."
            }
        ]
    }
]

all_d5.extend(more_d5)

with open("/home/subi/Projects/masterfunctionalskills.co.uk/maths_domain5_stats_prob.py", "w", encoding="utf-8") as f:
    f.write("#!/usr/bin/env python3\n")
    f.write('"""Maths Domain 5: Statistics & Probability (11 Core Topics)"""\n\n')
    f.write("TOPICS_DOMAIN5 = " + repr(all_d5) + "\n")

print(f"Domain 5 complete with {len(all_d5)} topics!")
