#!/usr/bin/env python3
import json

TOPICS_DOMAIN3 = [
    {
        "filename": "functional-skills-time.html",
        "clean_topic": "Time, 24-Hour Clocks & Timetables",
        "intro_lead": "Convert between 12-hour and 24-hour time, calculate elapsed time across day boundaries, read complex healthcare and transport timetables, and schedule clinical appointments.",
        "next_file": "functional-skills-speed.html",
        "next_name": "Speed, Distance & Time",
        "spec_points": [
            ("L1.16 / L2.18", "Calculate with time in 12-hour and 24-hour clocks, including time intervals across hours and days."),
            ("L1.17", "Read, interpret and use information from complex timetables and schedules.")
        ],
        "golden_rules": [
            {
                "icon": "fa-clock",
                "title": "Golden Rule 1: Time is Base-60, NOT Base-100",
                "desc": "There are 60 minutes in an hour, not 100. 1 hour and 45 minutes is 1.75 hours (45/60 = 0.75), NOT 1.45 hours!",
                "badge": "15 mins = 0.25 hrs | 30 mins = 0.5 hrs | 45 mins = 0.75 hrs"
            },
            {
                "icon": "fa-calendar-days",
                "title": "Golden Rule 2: The Timeline Bridge for Elapsed Time",
                "desc": "When calculating time elapsed (e.g. from 09:45 to 13:20), jump forward to the next whole hour first (09:45 to 10:00 = 15m), count whole hours (10:00 to 13:00 = 3h), then add remaining minutes (13:00 to 13:20 = 20m). Total = 3h 35m.",
                "badge": "Jump to Next Hour → Count Whole Hours → Add Remaining Minutes"
            }
        ],
        "skills": [
            {
                "title": "Converting Decimal Hours to Minutes",
                "summary": "Avoiding the #1 time calculation error in Functional Skills.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Decimal to Minutes:</strong> Multiply the decimal fraction by 60: <em>0.4 hours = 0.4 × 60 = 24 minutes.</em></li>
                    <li><strong>Minutes to Decimal:</strong> Divide the minutes by 60: <em>36 minutes = 36 ÷ 60 = 0.6 hours.</em></li>
                    <li><strong>Common Fractions:</strong> 1/4 hr = 15 mins; 1/2 hr = 30 mins; 3/4 hr = 45 mins; 1/3 hr = 20 mins.</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Hospital Community Midwife Home Visit Timetable",
                "marks": "3 Marks (Pearson Edexcel Level 2)",
                "context": "Community Health Nursing Travel Schedule",
                "question": "A community midwife departs the clinic at <strong>08:35</strong>. She drives for <strong>40 minutes</strong> to Patient A, spends <strong>55 minutes</strong> conducting a post-natal examination, and drives for <strong>25 minutes</strong> to Patient B.<br>At what time in 24-hour format does she arrive at Patient B's home?",
                "steps": [
                    ("Step 1", "Sum total elapsed travel and appointment time", "40 mins drive + 55 mins appointment + 25 mins drive = 120 minutes.", "M1: Total minutes summation"),
                    ("Step 2", "Convert 120 minutes into hours", "120 ÷ 60 = exactly 2 hours.", "M1: Conversion to hours"),
                    ("Step 3", "Add 2 hours to departure time (08:35)", "08:35 + 2 hours = 10:35.", "A1: Accurate 24-hour arrival time")
                ],
                "final_answer": "Arrival Time = 10:35",
                "tutor_tip": "Notice how 40 + 55 + 25 = 120 minutes = exactly 2 hours. Adding whole hours to 08:35 is immediate."
            }
        ],
        "examiner_traps": [
            {
                "title": "Entering 1.35 on a Calculator to Represent 1 Hour 35 Minutes",
                "desc": "Calculators treat 1.35 as 1 and 35/100, whereas 35 minutes is 35/60 = 0.583 hours.",
                "fix": "Always convert minutes to fractions of 60 before using a calculator."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A staff training seminar starts at 14:45 and finishes at 17:20. How long did the seminar last in hours and minutes?",
                "solution_steps": "1. 14:45 to 15:00 = 15 minutes.<br>2. 15:00 to 17:00 = 2 hours.<br>3. 17:00 to 17:20 = 20 minutes.<br>4. Total = 2 hours and 35 minutes.",
                "correct_answer": "2 hours and 35 minutes",
                "tutor_tip": "Use the timeline bridge method to avoid subtraction errors across 60-minute thresholds."
            }
        ]
    },
    {
        "filename": "functional-skills-speed.html",
        "clean_topic": "Speed, Distance & Time",
        "intro_lead": "Apply the speed-distance-time triangle to calculate vehicle journey times, average driving speeds, delivery ETAs, and speed limit compliance in logistics and transport.",
        "next_file": "functional-skills-density.html",
        "next_name": "Density & Compound Units",
        "spec_points": [
            ("L2.19", "Calculate speed, distance, and time using compound measures and convert between compound units.")
        ],
        "golden_rules": [
            {
                "icon": "fa-gauge",
                "title": "Golden Rule 1: The S-D-T Formula Triangle",
                "desc": "Cover what you want to find: Speed = Distance ÷ Time; Distance = Speed × Time; Time = Distance ÷ Speed.",
                "badge": "Distance at the top: S = D ÷ T | T = D ÷ S | D = S × T"
            },
            {
                "icon": "fa-stopwatch",
                "title": "Golden Rule 2: Convert Minutes to Decimal Hours BEFORE Dividing",
                "desc": "If a vehicle travels for 45 minutes, you MUST divide by 0.75 hours (45 ÷ 60), NOT 45 or 0.45!",
                "badge": "Time in Hours = Minutes ÷ 60"
            }
        ],
        "skills": [
            {
                "title": "Handling Compound Speed Units (mph and km/h)",
                "summary": "Avoiding common unit mismatches in journey calculations.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Formula:</strong> <em>Average Speed = Total Distance (miles) ÷ Total Time (hours).</em></li>
                    <li><strong>Hours &amp; Minutes to Decimal:</strong> 2 hours 15 mins = 2 + (15/60) = 2.25 hours.</li>
                    <li><strong>Decimal Time to Minutes:</strong> If Time = 1.4 hours, Minutes = 0.4 × 60 = 24 mins → 1 hr 24 mins.</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Ambulance Inter-Hospital Emergency Transfer",
                "marks": "3 Marks (Pearson Edexcel Level 2)",
                "context": "Emergency Patient Transport Services",
                "question": "An emergency transfer ambulance travels <strong>84 miles</strong> between two regional specialist hospitals. The journey takes <strong>1 hour and 45 minutes</strong>.<br>(a) Calculate the average speed of the ambulance in miles per hour (mph).<br>(b) The driver was instructed not to exceed an average speed of 50 mph. Was this instruction followed?",
                "steps": [
                    ("Step 1", "Convert time into decimal hours", "45 minutes = 45 ÷ 60 = 0.75 hours.<br>Total time = 1.75 hours.", "M1: Time conversion to decimal hours"),
                    ("Step 2", "Calculate average speed (Distance ÷ Time)", "Speed = 84 miles ÷ 1.75 hours = 48 mph.", "M1: Speed formula calculation"),
                    ("Step 3", "Compare with instruction threshold and conclude", "48 mph is less than 50 mph. Yes, the driver followed the speed instruction.", "A1: Accurate speed and valid comparative conclusion")
                ],
                "final_answer": "(a) Average Speed = 48 mph | (b) Yes, 48 mph complies with the 50 mph limit.",
                "tutor_tip": "If you divided 84 by 1.45, you would get 57.9 mph — an error that forfeits both marks! Always convert 45 mins to 0.75 hrs."
            }
        ],
        "examiner_traps": [
            {
                "title": "Dividing by 1.45 Instead of 1.75",
                "desc": "This is the single most common error in Level 2 speed questions.",
                "fix": "Never use minutes as decimals directly: 45 mins = 45/60 = 0.75."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A freight delivery lorry travels 165 miles at an average speed of 55 mph. How long does the journey take in hours and minutes?",
                "solution_steps": "1. Time = Distance ÷ Speed = 165 ÷ 55 = 3 hours.<br>2. Journey duration = exactly 3 hours (0 minutes).",
                "correct_answer": "3 hours",
                "tutor_tip": "Distance ÷ Speed = 165 ÷ 55 = 3."
            }
        ]
    },
    {
        "filename": "functional-skills-density.html",
        "clean_topic": "Density & Compound Units",
        "intro_lead": "Calculate material density, mass, and volume using the density triangle (D = M ÷ V), understand pressure (P = F ÷ A), and solve warehouse storage weight capacity problems.",
        "next_file": "functional-skills-unit-conversions.html",
        "next_name": "Unit Conversions",
        "spec_points": [
            ("L2.19", "Calculate density, mass, and volume using compound measures in vocational contexts.")
        ],
        "golden_rules": [
            {
                "icon": "fa-cube",
                "title": "Golden Rule 1: The Density Formula Triangle (D-M-V)",
                "desc": "Mass is at the top of the triangle: Density = Mass ÷ Volume; Mass = Density × Volume; Volume = Mass ÷ Density.",
                "badge": "Mass at Top: D = M ÷ V | M = D × V | V = M ÷ D"
            },
            {
                "icon": "fa-weight-hanging",
                "title": "Golden Rule 2: Ensure Mass and Volume Units Match Density",
                "desc": "If density is given in g/cm³, mass MUST be in grams and volume in cm³. If density is kg/m³, convert mass to kg and volume to m³.",
                "badge": "g/cm³ → g and cm³ | kg/m³ → kg and m³"
            }
        ],
        "skills": [
            {
                "title": "Density, Pressure & Compound Measure Units",
                "summary": "Understanding what compound units represent.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Density:</strong> How tightly packed matter is inside an object: <em>Density = Mass (g) ÷ Volume (cm³).</em></li>
                    <li><strong>Pressure:</strong> Force applied over an area: <em>Pressure (N/m²) = Force (N) ÷ Area (m²).</em></li>
                    <li><strong>Conversion:</strong> 1 litre of pure water has a mass of exactly 1 kg (density = 1 kg/L).</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Hospital Facility Concrete Foundation Pier Density & Weight",
                "marks": "3 Marks (Pearson Edexcel Level 2)",
                "context": "Healthcare Construction Engineering",
                "question": "A concrete footing for an MRI machine foundation is a cuboid measuring <strong>1.5 m long, 0.8 m wide, and 0.5 m deep</strong>. The reinforced concrete has a density of <strong>2,400 kg/m³</strong>.<br>Calculate the total mass of the footing in kilograms.",
                "steps": [
                    ("Step 1", "Calculate the volume of the cuboid footing", "Volume = length × width × depth = 1.5 × 0.8 × 0.5 = 0.6 m³.", "M1: Cuboid volume calculation"),
                    ("Step 2", "Apply Mass = Density × Volume formula", "Mass = 2,400 kg/m³ × 0.6 m³ = 1,440 kg.", "M1: Density triangle multiplication"),
                    ("Step 3", "State final mass with correct units", "Total Mass = 1,440 kg (or 1.44 tonnes).", "A1: Accurate mass with unit")
                ],
                "final_answer": "Total Mass = 1,440 kg",
                "tutor_tip": "Notice the units matched: volume was in m³ and density was in kg/m³, so the answer is directly in kg."
            }
        ],
        "examiner_traps": [
            {
                "title": "Multiplying Instead of Dividing for Density",
                "desc": "Doing Mass × Volume to find density is a common error. Remember that Mass is at the top of the triangle (D = M ÷ V).",
                "fix": "Sketch the triangle: M at the top, D and V at the bottom."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A metal component has a volume of 80 cm³ and a mass of 632 grams. Calculate the density of the metal in g/cm³.",
                "solution_steps": "1. Density = Mass ÷ Volume = 632 ÷ 80.<br>2. 632 ÷ 80 = 7.9 g/cm³.",
                "correct_answer": "7.9 g/cm³",
                "tutor_tip": "Divide 632 by 80 to obtain 7.9."
            }
        ]
    },
    {
        "filename": "functional-skills-unit-conversions.html",
        "clean_topic": "Metric & Imperial Unit Conversions",
        "intro_lead": "Convert seamlessly between metric units (mm, cm, m, km; ml, cl, l; g, kg, tonnes) and handle common imperial conversions (inches, feet, miles; ounces, pounds, stone; pints, gallons).",
        "next_file": "functional-skills-length.html",
        "next_name": "Length & Dimensions",
        "spec_points": [
            ("L1.18 / L2.20", "Convert between metric units of length, weight, and capacity."),
            ("L2.21", "Convert between metric and common imperial units using given conversion factors.")
        ],
        "golden_rules": [
            {
                "icon": "fa-stairs",
                "title": "Golden Rule 1: Big Unit to Small Unit = MULTIPLY",
                "desc": "When going from a larger unit to a smaller unit (e.g. metres to centimetres), MULTIPLY (1 m = 100 cm, so 4.5 m = 450 cm). Smaller unit to larger = DIVIDE.",
                "badge": "Big to Small → Multiply | Small to Big → Divide"
            },
            {
                "icon": "fa-arrows-split-up-and-left",
                "title": "Golden Rule 2: Benchmark Metric-to-Imperial Conversion Factors",
                "desc": "5 miles ≈ 8 km • 1 inch ≈ 2.5 cm • 1 kg ≈ 2.2 lbs • 1 gallon ≈ 4.5 litres • 1 foot = 12 inches.",
                "badge": "5 miles ≈ 8 km | 1 kg ≈ 2.2 lbs | 1 gallon ≈ 4.5 L"
            }
        ],
        "skills": [
            {
                "title": "The Metric Conversion Staircase",
                "summary": "Powers of 10 for length, mass, and capacity.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Length:</strong> 1 km = 1,000 m • 1 m = 100 cm • 1 cm = 10 mm.</li>
                    <li><strong>Mass / Weight:</strong> 1 tonne = 1,000 kg • 1 kg = 1,000 g • 1 g = 1,000 mg.</li>
                    <li><strong>Capacity / Volume:</strong> 1 litre = 1,000 ml • 1 litre = 100 cl • 1 cl = 10 ml.</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "NHS Patient Medication Weight Dosage Conversion",
                "marks": "3 Marks (Pearson Edexcel Level 2)",
                "context": "Clinical Medication Administration",
                "question": "A patient's medical chart lists their weight in imperial as <strong>11 stone 4 lbs</strong>. Hospital clinical dosage guidelines for an intravenous antibiotic require the weight in kilograms.<br>Use: <strong>1 stone = 14 lbs</strong> and <strong>1 kg ≈ 2.2 lbs</strong>.<br>Calculate the patient's weight in kilograms to the nearest whole kg.",
                "steps": [
                    ("Step 1", "Convert stone into pounds", "11 stone × 14 lbs = 154 lbs.<br>Total weight in lbs = 154 + 4 = 158 lbs.", "M1: Imperial weight conversion to lbs"),
                    ("Step 2", "Convert pounds into kilograms (divide by 2.2)", "158 lbs ÷ 2.2 = 71.818... kg.", "M1: Metric conversion division"),
                    ("Step 3", "Round to nearest whole kilogram", "71.818... rounds UP to 72 kg.", "A1: Accurate rounded mass (72 kg)")
                ],
                "final_answer": "Patient Weight = 72 kg (to nearest whole kg)",
                "tutor_tip": "Always check that the answer is sensible: 11 stone is around 70 kg, so 72 kg is realistic."
            }
        ],
        "examiner_traps": [
            {
                "title": "Dividing by 10 or 100 Instead of 1,000 for Grams/Kilograms",
                "desc": "Assuming 1 kg = 100 g instead of 1,000 g causes factor-of-ten errors in medication or postal problems.",
                "fix": "Remember 'kilo' always means 1,000: 1 kilometre = 1,000 m; 1 kilogram = 1,000 g."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "Convert 3.45 metres into millimetres (mm).",
                "solution_steps": "1. 1 m = 1,000 mm (100 cm × 10 mm).<br>2. 3.45 × 1,000 = 3,450 mm.",
                "correct_answer": "3,450 mm",
                "tutor_tip": "To convert metres to millimetres, multiply by 1,000."
            }
        ]
    },
    {
        "filename": "functional-skills-length.html",
        "clean_topic": "Length & Dimensions",
        "intro_lead": "Measure, estimate, and calculate lengths, heights, widths, and perimeters in construction, interior decorating, and clinical patient positioning.",
        "next_file": "functional-skills-weight.html",
        "next_name": "Weight & Mass",
        "spec_points": [
            ("L1.18 / L2.20", "Estimate and measure length and solve problems involving dimensions.")
        ],
        "golden_rules": [
            {
                "icon": "fa-ruler",
                "title": "Golden Rule 1: Always Align with 0 on Measuring Tools",
                "desc": "When reading a ruler or tape measure, check whether measurement starts at 0 or at the physical end of the tool.",
                "badge": "Start at 0, NOT the end of the ruler"
            },
            {
                "icon": "fa-tape",
                "title": "Golden Rule 2: Convert All Dimensions to the Same Unit Before Calculating",
                "desc": "If room length is 4.2 m and skirting board is sold in 250 cm lengths, convert both to metres (4.2 m and 2.5 m) or centimetres (420 cm and 250 cm).",
                "badge": "Never add metres and centimetres directly"
            }
        ],
        "skills": [
            {
                "title": "Length Measurement Estimations",
                "summary": "Real-world physical benchmarks for rapid estimation.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li>1 millimetre (1 mm): Thickness of an ID card.</li>
                    <li>1 centimetre (1 cm): Width of an adult fingernail.</li>
                    <li>1 metre (1 m): Height of a standard door handle from the floor.</li>
                    <li>1 kilometre (1 km): Approximately 10–12 minutes of brisk walking.</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Ward Corridor Handrail Installation Dimensions",
                "marks": "3 Marks (Pearson Edexcel Level 1/2)",
                "context": "Hospital Facilities Maintenance",
                "question": "A hospital corridor handrail is <strong>14.4 metres</strong> long. Timber rails are sold in sections of <strong>240 cm</strong> each.<br>(a) How many sections are needed to cover the entire handrail length?<br>(b) If each section costs £18.50, calculate the total cost.",
                "steps": [
                    ("Step 1", "Convert dimensions to common units (metres to cm)", "14.4 m × 100 = 1,440 cm.", "M1: Unit conversion to centimetres"),
                    ("Step 2", "Divide total length by section length", "1,440 cm ÷ 240 cm = 6 sections.", "A1: Accurate section count"),
                    ("Step 3", "Calculate total expenditure", "6 sections × £18.50 = £111.00.", "A1: Accurate cost calculation")
                ],
                "final_answer": "(a) 6 sections needed | (b) Total cost = £111.00",
                "tutor_tip": "Dividing 14.4 by 240 without converting gives 0.06 — always ensure units match before dividing!"
            }
        ],
        "examiner_traps": [
            {
                "title": "Mixing Units in Division",
                "desc": "Dividing metres by centimetres directly produces a nonsensical answer.",
                "fix": "Always label units in every working line."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A roll of medical fabric tape is 5 metres long. A nurse cuts 8 strips measuring 35 cm each. How many centimetres of tape remain on the roll?",
                "solution_steps": "1. 5 m = 500 cm.<br>2. 8 strips × 35 cm = 280 cm used.<br>3. Remaining = 500 - 280 = 220 cm (or 2.2 m).",
                "correct_answer": "220 cm (or 2.2 m)",
                "tutor_tip": "Convert 5 metres to 500 cm first."
            }
        ]
    }
]

# Write out domain 3
with open("/home/subi/Projects/masterfunctionalskills.co.uk/maths_domain3_measures.py", "w", encoding="utf-8") as f:
    f.write("#!/usr/bin/env python3\n")
    f.write('"""Maths Domain 3: Measures, Time, Speed & Conversions (5 Core Topics)"""\n\n')
    f.write("TOPICS_DOMAIN3 = " + repr(TOPICS_DOMAIN3) + "\n")

print(f"Domain 3 written with {len(TOPICS_DOMAIN3)} topics!")
