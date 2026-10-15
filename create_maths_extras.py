#!/usr/bin/env python3

EXTRAS_MATHS = [
    {
        "filename": "functional-skills-number-basics.html",
        "clean_topic": "Number Basics: Place Value & Counting",
        "intro_lead": "Build foundational confidence with whole numbers up to 1,000, understand unit and tens columns, count in multiples of 2, 5, 10, and 100, and solve everyday workplace tally problems.",
        "next_file": "functional-skills-numbers-and-place-value.html",
        "next_name": "Numbers & Place Value",
        "spec_points": [
            ("E3.1 / L1.1", "Count, read, write, order and compare numbers up to 1,000."),
            ("E3.2", "Understand place value in numbers with up to three digits.")
        ],
        "golden_rules": [
            {
                "icon": "fa-cubes",
                "title": "Golden Rule 1: The Hundreds, Tens & Units Model",
                "desc": "In a 3-digit number like 482: 4 means 4 hundreds (400), 8 means 8 tens (80), and 2 means 2 units (2).",
                "badge": "Hundreds • Tens • Units"
            },
            {
                "icon": "fa-arrow-up-right-dots",
                "title": "Golden Rule 2: Skip Counting by 10s and 100s",
                "desc": "Adding 10 only changes the tens column (unless passing a hundred boundary). Adding 100 only changes the hundreds column.",
                "badge": "340 + 10 = 350 | 340 + 100 = 440"
            }
        ],
        "skills": [
            {
                "title": "Place Value Breakdown up to 1,000",
                "summary": "Partitioning 2-digit and 3-digit numbers.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Partitioning:</strong> 658 = 600 + 50 + 8.</li>
                    <li><strong>Comparing:</strong> Compare the hundreds first: 540 is greater than 490 because 5 hundreds > 4 hundreds.</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Care Home Resident Laundry Bag Count",
                "marks": "2 Marks (Entry Level 3 / Level 1)",
                "context": "Care Facility Domestic Services",
                "question": "A laundry assistant receives <strong>three deliveries</strong> of towels: 120 towels, 85 towels, and 45 towels.<br>Calculate the total number of towels received.",
                "steps": [
                    ("Step 1", "Add the first two quantities", "120 + 85 = 205 towels.", "M1: Column addition setup"),
                    ("Step 2", "Add the third quantity to find total", "205 + 45 = 250 towels.", "A1: Accurate final sum (250)")
                ],
                "final_answer": "Total = 250 towels",
                "tutor_tip": "Check using mental partitioning: 120 + 80 + 40 = 240, plus (5 + 5 = 10) = 250."
            }
        ],
        "examiner_traps": [
            {
                "title": "Misaligning Digits in Column Addition",
                "desc": "Writing 85 with the 8 under the hundreds column of 120 gives an erroneous total of 970.",
                "fix": "Always align units over units, tens over tens."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "Write the number <strong>seven hundred and four</strong> in figures.",
                "solution_steps": "1. Hundreds = 7, Tens = 0 (placeholder), Units = 4.<br>2. Figures = 704.",
                "correct_answer": "704",
                "tutor_tip": "Remember the zero placeholder in the tens column."
            }
        ]
    },
    {
        "filename": "functional-skills-fraction-basics.html",
        "clean_topic": "Fraction Basics: Halves, Quarters & Thirds",
        "intro_lead": "Understand numerators and denominators, shade visual fraction diagrams, find unit fractions of everyday quantities, and recognize simple equivalent fractions.",
        "next_file": "functional-skills-fractions.html",
        "next_name": "Fractions",
        "spec_points": [
            ("E3.3 / L1.9", "Read, write, and understand common fractions (1/2, 1/4, 3/4, 1/3, 1/10)."),
            ("E3.4", "Find unit fractions of whole number quantities.")
        ],
        "golden_rules": [
            {
                "icon": "fa-pie-chart",
                "title": "Golden Rule 1: Denominator is TOTAL Equal Parts",
                "desc": "The bottom number (denominator) tells you how many equal parts the whole is cut into. The top number (numerator) tells you how many parts you have.",
                "badge": "Top = Parts you have | Bottom = Total equal parts"
            },
            {
                "icon": "fa-divide",
                "title": "Golden Rule 2: Finding a Unit Fraction: Divide by the Bottom",
                "desc": "To find 1/4 of £36: divide £36 by 4 = £9. To find 1/3 of 60 kg: divide 60 by 3 = 20 kg.",
                "badge": "1/n of an amount = Amount ÷ n"
            }
        ],
        "skills": [
            {
                "title": "Visualizing Common Fractions",
                "summary": "Core benchmark unit and non-unit fractions.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>1/2 (One Half):</strong> 1 out of 2 equal parts (50%).</li>
                    <li><strong>1/4 (One Quarter):</strong> 1 out of 4 equal parts (25%).</li>
                    <li><strong>3/4 (Three Quarters):</strong> 3 out of 4 equal parts (75%).</li>
                    <li><strong>1/10 (One Tenth):</strong> 1 out of 10 equal parts (10%).</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Hospital Kitchen Fruit Basket Portion Allocation",
                "marks": "2 Marks (Entry Level 3 / Level 1)",
                "context": "Catering Food Distribution",
                "question": "A hospital kitchen receives a crate of <strong>48 oranges</strong>. The chef uses <strong>1/4</strong> of the oranges for patient breakfast trays.<br>How many oranges does the chef use?",
                "steps": [
                    ("Step 1", "Divide total quantity by denominator (4)", "48 ÷ 4 = 12 oranges.", "M1: Unit fraction division method"),
                    ("Step 2", "Multiply by numerator (1)", "12 × 1 = 12 oranges.", "A1: Accurate portion count (12)")
                ],
                "final_answer": "12 oranges used",
                "tutor_tip": "Finding 1/4 is the same as halving and halving again: half of 48 is 24, half of 24 is 12."
            }
        ],
        "examiner_traps": [
            {
                "title": "Confusing 1/3 and 1/4",
                "desc": "Dividing by 3 instead of 4 is a frequent reading error.",
                "fix": "Highlight the denominator: 1/4 means divide by 4."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "What is <strong>1/3 of 45 metres</strong>?",
                "solution_steps": "1. Divide 45 by 3.<br>2. 45 ÷ 3 = 15 metres.",
                "correct_answer": "15 metres",
                "tutor_tip": "45 ÷ 3 = 15."
            }
        ]
    },
    {
        "filename": "functional-skills-decimal-basics.html",
        "clean_topic": "Decimal Basics: Tenths, Hundredths & Money",
        "intro_lead": "Read and write decimal numbers, connect decimal tenths and hundredths to currency, order simple decimals, and round money to the nearest pound.",
        "next_file": "functional-skills-decimals.html",
        "next_name": "Decimals",
        "spec_points": [
            ("E3.5 / L1.10", "Read, write, and understand decimals up to two decimal places in practical contexts such as money.")
        ],
        "golden_rules": [
            {
                "icon": "fa-coins",
                "title": "Golden Rule 1: The Decimal Point Separates Wholes from Parts",
                "desc": "In £4.75, the 4 represents whole pounds, the 7 represents tenths of a pound (70p), and the 5 represents hundredths of a pound (5p).",
                "badge": "Pounds . Tenths Hundredths (£ . 10p 1p)"
            },
            {
                "icon": "fa-arrows-left-right",
                "title": "Golden Rule 2: 0.5 is Bigger than 0.05",
                "desc": "0.5 represents 5 tenths (50p). 0.05 represents 5 hundredths (5p). Always compare the first decimal digit immediately after the dot.",
                "badge": "0.5 = 50p > 0.05 = 5p"
            }
        ],
        "skills": [
            {
                "title": "Money to Decimal Representation",
                "summary": "Converting pence to pounds and decimals.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li>80p = £0.80</li>
                    <li>5p = £0.05 (Note the zero placeholder!)</li>
                    <li>£2 and 4p = £2.04</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Care Home Tea Club Receipt Total",
                "marks": "2 Marks (Entry Level 3 / Level 1)",
                "context": "Activities Petty Cash",
                "question": "A care home activity worker buys biscuits for <strong>£1.45</strong> and tea bags for <strong>£2.80</strong>.<br>(a) What is the total cost?<br>(b) How much change from a £5.00 note?",
                "steps": [
                    ("Step 1", "Add the two decimal amounts", "£1.45 + £2.80 = £4.25.", "M1: Column decimal addition"),
                    ("Step 2", "Subtract total from £5.00", "£5.00 - £4.25 = £0.75 (or 75p).", "A1: Accurate change calculation")
                ],
                "final_answer": "(a) Total = £4.25 | (b) Change = £0.75 (75p)",
                "tutor_tip": "Line up decimal points: 1.45 + 2.80 = 4.25."
            }
        ],
        "examiner_traps": [
            {
                "title": "Writing 5p as £0.5",
                "desc": "£0.5 is 50p! Five pence must be written as £0.05.",
                "fix": "Always use two digits after the decimal point for pence."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "Round £18.65 to the nearest whole pound.",
                "solution_steps": "1. Look at the tenths digit (6).<br>2. Since 6 is 5 or more, round UP.<br>3. £18.65 rounds to £19.00.",
                "correct_answer": "£19.00",
                "tutor_tip": "Round up because 65p is more than 50p."
            }
        ]
    },
    {
        "filename": "functional-skills-3d-shape-basics.html",
        "clean_topic": "3D Shape Basics: Cubes, Spheres & Cones",
        "intro_lead": "Recognize and name common 3D solids in everyday healthcare and domestic environments, identifying cubes, spheres, cylinders, and pyramids.",
        "next_file": "functional-skills-3d-shapes.html",
        "next_name": "3D Shapes",
        "spec_points": [
            ("E3.6 / L1.20", "Recognise and name common 3D solids including cubes, cuboids, cylinders, cones, and spheres.")
        ],
        "golden_rules": [
            {
                "icon": "fa-cube",
                "title": "Golden Rule 1: Prisms Have Constant Cross-Sections",
                "desc": "If you slice a prism anywhere along its length, the exposed slice has the exact same 2D shape (e.g. slicing a cylinder always reveals a circle).",
                "badge": "Prisms = Uniform cross-section"
            },
            {
                "icon": "fa-shapes",
                "title": "Golden Rule 2: Spheres Have No Vertices and No Edges",
                "desc": "A sphere (ball) has 1 continuous curved surface, 0 edges, and 0 vertices.",
                "badge": "Sphere: 1 Curved Surface • 0 Edges • 0 Vertices"
            }
        ],
        "skills": [
            {
                "title": "Matching Everyday Objects to 3D Shapes",
                "summary": "Real-world examples of common 3D solids.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Tin of Baked Beans:</strong> Cylinder</li>
                    <li><strong>Shoe Box:</strong> Cuboid</li>
                    <li><strong>Football:</strong> Sphere</li>
                    <li><strong>Party Hat:</strong> Cone</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Hospital Supply Equipment Packaging Shape Identification",
                "marks": "2 Marks (Entry Level 3 / Level 1)",
                "context": "Clinical Stores Inventory",
                "question": "Identify the 3D mathematical shapes of these two healthcare items:<br>(a) A roll of sterile surgical gauze tape.<br>(b) A box containing disposable nitrile gloves.",
                "steps": [
                    ("Step 1", "Analyze the shape of the tape roll", "The tape roll is circular at both ends with a curved outer body. It is a CYLINDER.", "A1: Correct solid identification (Cylinder)"),
                    ("Step 2", "Analyze the shape of the glove box", "The glove box has 6 rectangular flat faces. It is a CUBOID.", "A1: Correct solid identification (Cuboid)")
                ],
                "final_answer": "(a) Cylinder | (b) Cuboid",
                "tutor_tip": "Use standard mathematical names: write 'cuboid', not 'rectangular box'."
            }
        ],
        "examiner_traps": [
            {
                "title": "Writing 2D Names for 3D Shapes",
                "desc": "Calling a cube a 'square' or a cylinder a 'circle' is an automatic loss of marks.",
                "fix": "Remember: Squares are flat (2D); cubes and cuboids are solid (3D)."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A container is shaped as a cylinder. How many flat faces and how many curved surfaces does it have?",
                "solution_steps": "1. Flat circular faces: Top and bottom = 2 flat faces.<br>2. Curved body = 1 curved surface.",
                "correct_answer": "2 flat faces and 1 curved surface",
                "tutor_tip": "A cylinder has 3 faces in total: 2 flat circles + 1 curved side."
            }
        ]
    },
    {
        "filename": "functional-skills-scales.html",
        "clean_topic": "Reading Gauges, Dials & Measuring Scales",
        "intro_lead": "Read analogue and digital measuring scales with unnumbered division marks, calibrate medical weighing scales, and read pressure dials and clinical thermometers accurately.",
        "next_file": "functional-skills-unit-conversions.html",
        "next_name": "Unit Conversions",
        "spec_points": [
            ("L1.18 / L2.20", "Read scales to the nearest labelled or unlabelled division in practical contexts.")
        ],
        "golden_rules": [
            {
                "icon": "fa-gauge",
                "title": "Golden Rule 1: Find the Value of ONE Division First",
                "desc": "Count the number of spaces between two numbered markings. Subtract the numbers and divide by the count: Difference ÷ Number of Spaces = Value of 1 mark.",
                "badge": "Value per Mark = (Mark B - Mark A) ÷ Number of Divisions"
            },
            {
                "icon": "fa-eye",
                "title": "Golden Rule 2: Avoid Parallax Error by Reading at Eye Level",
                "desc": "Read measuring cylinders and gauges looking straight on at eye level at the bottom of the liquid meniscus.",
                "badge": "Read perpendicular to the scale at eye level"
            }
        ],
        "skills": [
            {
                "title": "Calculating Unlabelled Scale Markings",
                "summary": "Step-by-step method to read any dial or thermometer.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li>Pick two consecutive numbered lines (e.g. 20 and 30).</li>
                    <li>Find the difference: 30 - 20 = 10 units.</li>
                    <li>Count the spaces between them: e.g. 5 spaces.</li>
                    <li>Divide: 10 ÷ 5 = 2 units per tick mark.</li>
                  </ol>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Hospital Oxygen Cylinder Pressure Gauge Reading",
                "marks": "3 Marks (Pearson Edexcel Level 1/2)",
                "context": "Respiratory Ward Medical Gas Safety",
                "question": "A ward oxygen cylinder pressure gauge has major marks at <strong>100 bar and 150 bar</strong>. There are <strong>10 equal divisions</strong> between 100 and 150 bar.<br>(a) What pressure does each small tick mark represent?<br>(b) The pointer indicates 4 divisions past 100 bar. What is the current cylinder pressure?",
                "steps": [
                    ("Step 1", "Calculate the difference between major marks", "150 bar - 100 bar = 50 bar.", "M1: Difference calculation"),
                    ("Step 2", "Divide by the number of divisions", "50 bar ÷ 10 divisions = 5 bar per tick mark.", "A1: Accurate value per division (5 bar)"),
                    ("Step 3", "Calculate indicated pressure", "100 bar + (4 × 5 bar) = 100 + 20 = 120 bar.", "A1: Accurate indicated pressure (120 bar)")
                ],
                "final_answer": "(a) Each mark represents 5 bar | (b) Pressure = 120 bar.",
                "tutor_tip": "Count the SPACES between lines, not the lines themselves."
            }
        ],
        "examiner_traps": [
            {
                "title": "Assuming Each Line Represents 1 Unit",
                "desc": "Assuming tick marks represent 1 without checking the scale causes significant reading errors.",
                "fix": "Always do (High - Low) ÷ Spaces."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A measuring jug has marks at 200 ml and 300 ml, with 5 equal subdivisions between them. What does each tick mark represent?",
                "solution_steps": "1. Difference = 300 - 200 = 100 ml.<br>2. Value per mark = 100 ÷ 5 = 20 ml.",
                "correct_answer": "20 ml",
                "tutor_tip": "100 ÷ 5 = 20 ml."
            }
        ]
    },
    {
        "filename": "functional-skills-tally-charts.html",
        "clean_topic": "Tally Charts & Frequency Tables",
        "intro_lead": "Record survey data using 5-bar tally groups, convert tallies into numerical frequencies, check totals, and analyze workplace satisfaction feedback.",
        "next_file": "functional-skills-tables.html",
        "next_name": "Data Tables",
        "spec_points": [
            ("E3.7 / L1.24", "Record and organise discrete data using tally charts and frequency tables.")
        ],
        "golden_rules": [
            {
                "icon": "fa-bars",
                "title": "Golden Rule 1: The Gate of 5 Tally System",
                "desc": "Draw four vertical strokes and a diagonal strike-through across them for the fifth mark: |||| with a slash = 5. This enables rapid counting in 5s.",
                "badge": "4 vertical bars + 1 diagonal cross = 5"
            },
            {
                "icon": "fa-check-double",
                "title": "Golden Rule 2: Frequency Must Match Sum of Raw Data Items",
                "desc": "Always count the total raw data items first. The sum of your frequency column MUST equal the total count of survey responses.",
                "badge": "Total Frequency = Total Survey Responses"
            }
        ],
        "skills": [
            {
                "title": "Converting Raw Data to Tally and Frequency",
                "summary": "Cross off items systematically as you record.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">To avoid missing or double-counting data:</p>
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li>Put a light pencil slash through each data point as you log its tally stroke.</li>
                    <li>Group tallies in fives.</li>
                    <li>Write the final frequency count in digits in the right-hand column.</li>
                  </ol>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Care Home Resident Lunch Menu Preference Tally",
                "marks": "2 Marks (Entry Level 3 / Level 1)",
                "context": "Catering Service Quality Survey",
                "question": "A catering assistant records lunch choices for <strong>25 residents</strong>:<br>Roast Chicken, Fish & Chips, Roast Chicken, Pasta, Fish & Chips, Roast Chicken, Roast Chicken, Pasta, Fish & Chips, Roast Chicken, Roast Chicken, Pasta, Fish & Chips, Roast Chicken, Roast Chicken, Fish & Chips, Pasta, Roast Chicken, Fish & Chips, Roast Chicken, Pasta, Fish & Chips, Roast Chicken, Fish & Chips, Roast Chicken.<br>How many residents chose Roast Chicken?",
                "steps": [
                    ("Step 1", "Count Roast Chicken choices systematically", "Roast Chicken appears 12 times (two gates of 5 plus 2 strokes: <s>||||</s> <s>||||</s> ||).", "M1: Systematic tally counting"),
                    ("Step 2", "State final numerical frequency", "12 residents chose Roast Chicken.", "A1: Accurate frequency count (12)")
                ],
                "final_answer": "12 residents chose Roast Chicken",
                "tutor_tip": "Check that the tallies sum to 25: 12 (Chicken) + 8 (Fish) + 5 (Pasta) = 25 total."
            }
        ],
        "examiner_traps": [
            {
                "title": "Writing 5 Vertical Strokes Without a Cross-Bar",
                "desc": "Drawing 5 parallel lines without a diagonal strike-through is non-standard and makes counting slow and prone to errors.",
                "fix": "Always cross the 5th stroke diagonally across the first 4."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A tally chart shows: <s>||||</s> <s>||||</s> <s>||||</s> ||| for patient transport requests on Friday. What is the total numerical frequency?",
                "solution_steps": "1. 3 full gates of 5 = 3 × 5 = 15.<br>2. Plus 3 strokes = 15 + 3 = 18.",
                "correct_answer": "18",
                "tutor_tip": "(3 × 5) + 3 = 18."
            }
        ]
    },
    {
        "filename": "functional-skills-tables.html",
        "clean_topic": "Data Tables & Information Retrieval",
        "intro_lead": "Extract information from complex tables, bus and train schedules, ward shift rosters, and multi-column delivery manifests.",
        "next_file": "functional-skills-data-tables.html",
        "next_name": "Two-Way Data Tables",
        "spec_points": [
            ("E3.7 / L1.24", "Extract and use information from simple and complex tables and lists.")
        ],
        "golden_rules": [
            {
                "icon": "fa-table",
                "title": "Golden Rule 1: Read Header Labels First",
                "desc": "Before looking at numbers, read the column and row titles to understand what the data represents and check the units (e.g. 'Cost in £', 'Weight in kg').",
                "badge": "Check units in table headers before calculating"
            },
            {
                "icon": "fa-ruler",
                "title": "Golden Rule 2: Use a Ruler to Trace Across Dense Tables",
                "desc": "Place a physical ruler along the row you are reading to prevent your eye from slipping onto the row above or below.",
                "badge": "Align rows with a straight edge"
            }
        ],
        "skills": [
            {
                "title": "Multi-Column Table Navigation",
                "summary": "Finding specific data points using two criteria.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Criteria 1:</strong> Locate the correct row (e.g. 'Ward 4').</li>
                    <li><strong>Criteria 2:</strong> Trace horizontally to the correct column (e.g. 'Night Shift Staffing').</li>
                    <li><strong>Extract Value:</strong> Read the intersecting figure with units.</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Hospital Clinic Shift Cover Schedule Lookup",
                "marks": "2 Marks (Entry Level 3 / Level 1)",
                "context": "Clinical Ward Operations",
                "question": "A table shows nurse staffing across 3 hospital wards:<br>• Ward A: Morning 6, Afternoon 5, Night 3<br>• Ward B: Morning 8, Afternoon 6, Night 4<br>• Ward C: Morning 5, Afternoon 4, Night 2<br>(a) Which ward has the highest afternoon staffing?<br>(b) What is the total number of night nurses across all three wards?",
                "steps": [
                    ("Step 1", "Compare afternoon staffing column", "Ward A = 5, Ward B = 6, Ward C = 4. Highest is Ward B with 6 nurses.", "A1: Accurate table lookup"),
                    ("Step 2", "Sum night staffing column", "3 (Ward A) + 4 (Ward B) + 2 (Ward C) = 9 nurses.", "A1: Accurate column sum")
                ],
                "final_answer": "(a) Ward B (6 nurses) | (b) Total Night Nurses = 9",
                "tutor_tip": "Read straight down the afternoon and night columns."
            }
        ],
        "examiner_traps": [
            {
                "title": "Reading Morning Instead of Afternoon",
                "desc": "A common slip is looking at the wrong column when columns are closely spaced.",
                "fix": "Highlight the requested column header before reading numbers."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "In a depot schedule: Van 1 carries 14 parcels, Van 2 carries 22 parcels, Van 3 carries 19 parcels. How many parcels do Vans 1 and 3 carry combined?",
                "solution_steps": "1. Van 1 = 14; Van 3 = 19.<br>2. Combined = 14 + 19 = 33 parcels.",
                "correct_answer": "33 parcels",
                "tutor_tip": "14 + 19 = 33."
            }
        ]
    },
    {
        "filename": "functional-skills-lists.html",
        "clean_topic": "Lists: Sorting & Information Extraction",
        "intro_lead": "Sort lists alphabetically and numerically, extract items based on multiple criteria, and prioritize tasks in workplace handovers and dispatch manifests.",
        "next_file": "functional-skills-tables.html",
        "next_name": "Data Tables",
        "spec_points": [
            ("E3.7 / L1.24", "Sort and organise lists alphabetically and numerically to locate information.")
        ],
        "golden_rules": [
            {
                "icon": "fa-arrow-down-a-z",
                "title": "Golden Rule 1: Alphabetical Ordering: Compare Letter by Letter",
                "desc": "If words share the same first letter, compare the second letter. If second letters are identical, compare the third letter (e.g. Baker, Bennett, Brown).",
                "badge": "Compare 1st letter → 2nd letter → 3rd letter"
            },
            {
                "icon": "fa-list-ol",
                "title": "Golden Rule 2: Numerical Ordering: Line Up Digits",
                "desc": "Order numbers by comparing the largest place value column first.",
                "badge": "Ascending = Smallest to Largest | Descending = Largest to Smallest"
            }
        ],
        "skills": [
            {
                "title": "Alphabetical Filing Rules",
                "summary": "Standard workplace sorting procedures for patient and customer files.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li>Surname first: e.g. <em>Smith, John</em> before <em>Smith, Sarah</em>.</li>
                    <li>Shorter word comes first: e.g. <em>Hall</em> comes before <em>Halley</em>.</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Patient Medical Records Alphabetical Filing",
                "marks": "2 Marks (Entry Level 3 / Level 1)",
                "context": "Health Records Management",
                "question": "Arrange these five patient surnames in alphabetical order: <strong>Patel, Parker, Phillips, Price, Pearce</strong>.",
                "steps": [
                    ("Step 1", "Compare second letter of each surname (Pa, Ph, Pr, Pe)", "Pa: Parker, Patel<br>Pe: Pearce<br>Ph: Phillips<br>Pr: Price", "M1: Grouping by second letter"),
                    ("Step 2", "Compare third letter for Parker vs Patel", "Parker has 'r'; Patel has 't'. 'r' comes before 't', so Parker is first, Patel second.", "M1: Third-letter differentiation"),
                    ("Step 3", "Assemble final sequence", "Parker, Patel, Pearce, Phillips, Price.", "A1: Accurate alphabetical sequence")
                ],
                "final_answer": "Parker, Patel, Pearce, Phillips, Price",
                "tutor_tip": "Notice how all start with P, but the second letters (a, e, h, r) establish the main order."
            }
        ],
        "examiner_traps": [
            {
                "title": "Stopping at the First Letter",
                "desc": "Assuming all P names are already sorted without checking second and third letters.",
                "fix": "Always write down the alphabet (A-Z) if you are unsure."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "Arrange these four delivery towns alphabetically: <strong>Bolton, Bradford, Bristol, Bath</strong>.",
                "solution_steps": "1. All start with B.<br>2. Compare 2nd letters: Bath (a), then Bolton (o), Bradford (r), Bristol (r).<br>3. Compare Bradford vs Bristol: 'a' before 'i'.<br>4. Sequence: Bath, Bolton, Bradford, Bristol.",
                "correct_answer": "Bath, Bolton, Bradford, Bristol",
                "tutor_tip": "Bath is first because 'a' is the earliest second letter."
            }
        ]
    },
    {
        "filename": "functional-skills-movement-and-direction.html",
        "clean_topic": "Movement, Direction & Compass Bearings",
        "intro_lead": "Navigate workplace layouts using compass directions (N, S, E, W), understand clockwise and anti-clockwise turns, and follow route instructions on emergency escape plans.",
        "next_file": "functional-skills-angles.html",
        "next_name": "Angles & Bearings",
        "spec_points": [
            ("E3.8 / L1.21", "Use cardinal compass directions (N, S, E, W) and turns (quarter, half, full turns) to describe movement.")
        ],
        "golden_rules": [
            {
                "icon": "fa-compass",
                "title": "Golden Rule 1: Never Eat Shredded Wheat (Clockwise N-E-S-W)",
                "desc": "North is at the top (0°/360°), East is at 90° (Right), South is at 180° (Down), and West is at 270° (Left).",
                "badge": "North → East → South → West (Clockwise)"
            },
            {
                "icon": "fa-rotate",
                "title": "Golden Rule 2: Quarter Turns Equal 90°",
                "desc": "A 1/4 turn = 90° (Right angle). A 1/2 turn = 180° (Opposite direction). A 3/4 turn = 270°. A full turn = 360° (Back to start).",
                "badge": "1/4 turn = 90° | 1/2 turn = 180° | Full turn = 360°"
            }
        ],
        "skills": [
            {
                "title": "The 8-Point Compass Rose",
                "summary": "Intermediate compass points between the 4 cardinals.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>North-East (NE):</strong> Halfway between North and East (45°).</li>
                    <li><strong>South-East (SE):</strong> Halfway between South and East (135°).</li>
                    <li><strong>South-West (SW):</strong> Halfway between South and West (225°).</li>
                    <li><strong>North-West (NW):</strong> Halfway between North and West (315°).</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Hospital Emergency Evacuation Route Direction",
                "marks": "2 Marks (Entry Level 3 / Level 1)",
                "context": "Facility Fire Safety Navigation",
                "question": "A hospital porter is pushing a wheelchair facing <strong>North</strong> down Main Corridor. At the junction, she turns <strong>a quarter turn clockwise</strong>, walks 30 metres, then turns <strong>a half turn</strong>.<br>(a) In which compass direction is she facing after the first turn?<br>(b) In which direction is she facing after the half turn?",
                "steps": [
                    ("Step 1", "Determine direction after a quarter turn clockwise from North", "Turning 90° clockwise from North faces EAST.", "A1: First direction identification (East)"),
                    ("Step 2", "Determine direction after a half turn from East", "A half turn (180°) reverses direction: opposite of East is WEST.", "A1: Second direction identification (West)")
                ],
                "final_answer": "(a) East | (b) West",
                "tutor_tip": "Visualize the compass: North + quarter turn clockwise = East. East + half turn = West."
            }
        ],
        "examiner_traps": [
            {
                "title": "Confusing Clockwise with Anti-Clockwise",
                "desc": "Clockwise moves in the direction of clock hands (N → E → S → W). Anti-clockwise moves backwards (N → W → S → E).",
                "fix": "Always look at your watch or clock hands to verify direction."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "You are facing South. You make a three-quarter turn clockwise. In which direction are you now facing?",
                "solution_steps": "1. Start at South.<br>2. 1/4 turn clockwise = West.<br>3. 2/4 (half) turn = North.<br>4. 3/4 turn = East.",
                "correct_answer": "East",
                "tutor_tip": "Turning 3/4 clockwise is identical to turning 1/4 anti-clockwise."
            }
        ]
    },
    {
        "filename": "functional-skills-using-length-area-and-volume-in-calculations.html",
        "clean_topic": "Multi-Step Spatial Calculations: Area & Volume",
        "intro_lead": "Combine measurements of length, compound area, volume, and unit pricing to solve multi-stage flooring, tiling, and fluid storage projects.",
        "next_file": "functional-skills-maths-level-2.html",
        "next_name": "Maths Level 2 Directory",
        "spec_points": [
            ("L2.24", "Calculate perimeter, area, surface area and volume of composite shapes and apply in multi-step costing problems.")
        ],
        "golden_rules": [
            {
                "icon": "fa-layer-group",
                "title": "Golden Rule 1: Break Multi-Step Problems into Sequential Stages",
                "desc": "Stage 1: Find dimensions. Stage 2: Calculate Area or Volume. Stage 3: Account for wastage or pack sizes. Stage 4: Multiply by unit cost.",
                "badge": "Dimensions → Area/Volume → Quantity Needed → Total Cost"
            },
            {
                "icon": "fa-percent",
                "title": "Golden Rule 2: Add Wastage to Area BEFORE Finding Pack Count",
                "desc": "If a job requires 10% extra for cuts and wastage: Area with wastage = Area × 1.10. Then divide by pack coverage and round UP.",
                "badge": "Area × 1.10 → Divide by Pack Size → Round UP"
            }
        ],
        "skills": [
            {
                "title": "The 4-Stage Construction Costing Formula",
                "summary": "Standard layout for 5-mark and 6-mark spatial questions.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Compound Area:</strong> Split L-shapes into rectangles and sum areas in m².</li>
                    <li><strong>Add Wastage:</strong> Multiply by 1.10 (for 10% wastage).</li>
                    <li><strong>Pack Count:</strong> Total Area ÷ Coverage per box (round UP to whole boxes).</li>
                    <li><strong>Total Cost:</strong> Boxes × Price per box.</li>
                  </ol>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Hospital Consultation Room Vinyl Flooring Installation",
                "marks": "4 Marks (Pearson Edexcel Level 2)",
                "context": "Healthcare Facility Renovation",
                "question": "A clinical consultation room floor measures <strong>6 m long by 4 m wide</strong>. Non-slip vinyl tiles are sold in packs:<br>• Each pack covers <strong>2.5 m²</strong><br>• Cost per pack: <strong>£28.50</strong><br>• The installer adds <strong>10% extra area</strong> for cutting wastage.<br>Calculate the total cost to tile the room.",
                "steps": [
                    ("Step 1", "Calculate floor area", "Area = length × width = 6 m × 4 m = 24 m².", "M1: Floor area calculation"),
                    ("Step 2", "Add 10% cutting wastage", "10% of 24 m² = 2.4 m².<br>Total area needed = 24 + 2.4 = 26.4 m².", "M1: Wastage percentage addition"),
                    ("Step 3", "Calculate packs required and round UP", "Packs = 26.4 m² ÷ 2.5 m² = 10.56 packs.<br>Must buy whole packs: round UP to 11 packs.", "A1: Accurate pack count rounded UP (11)"),
                    ("Step 4", "Calculate total expenditure", "11 packs × £28.50 = £313.50.", "A1: Accurate final cost (£313.50)")
                ],
                "final_answer": "Total Cost = £313.50 (11 packs required)",
                "tutor_tip": "Always round packs UP! 10.56 packs means 10 packs would leave part of the floor bare."
            }
        ],
        "examiner_traps": [
            {
                "title": "Rounding Packs Down to 10",
                "desc": "Buying 10 packs leaves you short of materials. You must purchase 11 full packs.",
                "fix": "In construction materials, always round UP to the next integer."
            }
        ],
        "practice_questions": [
            {
                "marks": "3 Marks",
                "question": "A room floor is 5 m by 3 m (Area = 15 m²). Floor tiles cost £18 per m². How much will it cost to tile the room without wastage?",
                "solution_steps": "1. Area = 15 m².<br>2. Cost = 15 × £18 = £270.00.",
                "correct_answer": "£270.00",
                "tutor_tip": "15 × 18 = 270."
            }
        ]
    },
    {
        "filename": "functional-skills-angles-and-bearings.html",
        "clean_topic": "Angles, Bearings & Turn Navigation",
        "intro_lead": "Measure and calculate angles on straight lines, around a point, vertically opposite angles, and measure 3-figure compass bearings for maritime and air ambulance navigation.",
        "next_file": "functional-skills-angles-in-2d-shapes.html",
        "next_name": "Angles in Polygons",
        "spec_points": [
            ("L1.21 / L2.23", "Measure and draw angles in degrees up to 360°."),
            ("L2.23", "Understand and use 3-figure bearings measured clockwise from North.")
        ],
        "golden_rules": [
            {
                "icon": "fa-compass",
                "title": "Golden Rule 1: Three Rules of Three-Figure Bearings",
                "desc": "1. Always start pointing NORTH. 2. Always measure CLOCKWISE. 3. Always write as THREE FIGURES (e.g. 045°, 008°, 230°).",
                "badge": "From North • Clockwise • 3 Figures (e.g. 075°)"
            },
            {
                "icon": "fa-lines-leaning",
                "title": "Golden Rule 2: Core Angle Sum Relationships",
                "desc": "Angles on a straight line sum to 180°. Angles around a full point sum to 360°. Vertically opposite angles are equal.",
                "badge": "Straight Line = 180° | Full Circle = 360°"
            }
        ],
        "skills": [
            {
                "title": "Calculating Reverse (Back) Bearings",
                "summary": "Finding the bearing for the return journey.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li>If the forward bearing is <strong>less than 180°</strong>: ADD 180°.<br><em>Forward = 065° → Return = 065° + 180° = 245°.</em></li>
                    <li>If the forward bearing is <strong>greater than 180°</strong>: SUBTRACT 180°.<br><em>Forward = 290° → Return = 290° - 180° = 110°.</em></li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Air Ambulance Flight Navigation Bearing",
                "marks": "3 Marks (Pearson Edexcel Level 2)",
                "context": "Emergency Medical Helicopter Dispatch",
                "question": "An emergency transfer ambulance flies on a bearing of <strong>074°</strong> to an accident site A.<br>(a) Is this bearing Acute, Right-Angled, Obtuse, or Reflex?<br>(b) Calculate the back bearing from the accident site A to return to the helipad.",
                "steps": [
                    ("Step 1", "Classify angle size", "074° is between 0° and 90°; therefore, it is an ACUTE angle.", "A1: Correct angle classification"),
                    ("Step 2", "Apply back bearing rule", "074° + 180° = 254°.", "M1: Back bearing addition"),
                    ("Step 3", "State return bearing in 3-figure notation", "Back bearing = 254°.", "A1: Accurate 3-figure bearing")
                ],
                "final_answer": "(a) Acute angle | (b) Return bearing = 254°",
                "tutor_tip": "Bearings are always 3 figures: 074°."
            }
        ],
        "examiner_traps": [
            {
                "title": "Omitting the Leading Zero",
                "desc": "Writing 74° instead of 074° loses the bearing format mark.",
                "fix": "Always use 3 digits."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "Angles on a straight line are x and 125°. Find x.",
                "solution_steps": "1. 180° - 125° = 55°.",
                "correct_answer": "55°",
                "tutor_tip": "180 - 125 = 55."
            }
        ]
    },
    {
        "filename": "functional-skills-comparing-data-sets.html",
        "clean_topic": "Comparing Data Sets & Distribution Consistency",
        "intro_lead": "Compare two statistical data distributions using an appropriate average (mean or median) and the range to evaluate workplace consistency.",
        "next_file": "functional-skills-maths-level-2.html",
        "next_name": "Maths Level 2 Directory",
        "spec_points": [
            ("L2.29", "Compare two data sets using an appropriate measure of average and the range.")
        ],
        "golden_rules": [
            {
                "icon": "fa-scale-balanced",
                "title": "Golden Rule 1: Always Write Two Distinct Comparison Statements",
                "desc": "Statement 1: Compare the averages (mean or median) and what it means in context. Statement 2: Compare the ranges and state which is more consistent.",
                "badge": "Average Statement + Consistency/Range Statement"
            },
            {
                "icon": "fa-compress",
                "title": "Golden Rule 2: Smaller Range = Greater Consistency",
                "desc": "A smaller range means numbers are clustered closer together, showing more reliable, consistent performance.",
                "badge": "Smaller range = more consistent | Larger range = more variable"
            }
        ],
        "skills": [
            {
                "title": "The 2-Point Comparison Formula",
                "summary": "Full mark sentence structures for Pearson Edexcel papers.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><em>"On average, Group A scored higher than Group B (mean 72 vs 65)."</em></li>
                    <li><em>"Group B was more consistent because their range was smaller (range 10 vs 24)."</em></li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Hospital Shift Medication Dispensing Accuracy Comparison",
                "marks": "3 Marks (Pearson Edexcel Level 2)",
                "context": "Clinical Pharmacy Audit",
                "question": "A clinical audit compares dispensing accuracy rates across Day and Night shifts:<br>• Day Shift: Mean = 96.5%, Range = 4%<br>• Night Shift: Mean = 94.0%, Range = 9%<br>Compare the dispensing accuracy of the two shifts using the mean and range.",
                "steps": [
                    ("Step 1", "Compare the averages (Mean)", "Day Shift had a higher mean accuracy rate than Night Shift (96.5% vs 94.0%), meaning Day Shift was more accurate on average.", "A1: Valid mean comparison"),
                    ("Step 2", "Compare the spread / consistency (Range)", "Day Shift had a smaller range than Night Shift (4% vs 9%), meaning Day Shift dispensing accuracy was more consistent.", "A1: Valid range comparison"),
                    ("Step 3", "Overall conclusion", "Day Shift demonstrated both higher average accuracy and greater consistency.", "A1: Comprehensive synthesis")
                ],
                "final_answer": "Day Shift had higher average accuracy (96.5% vs 94.0%) and more consistent performance (range 4% vs 9%).",
                "tutor_tip": "Remember to cite the actual numbers in your written sentences."
            }
        ],
        "examiner_traps": [
            {
                "title": "Comparing Only the Mean and Forgetting the Range",
                "desc": "Omitting the range comparison caps your mark at 1 out of 2 or 2 out of 3.",
                "fix": "Always write TWO separate sentences: one for Mean, one for Range."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "Depot A: Mean parcels = 420, Range = 50. Depot B: Mean parcels = 450, Range = 120. Which depot has more consistent daily parcel deliveries?",
                "solution_steps": "1. Consistency is determined by the range.<br>2. Depot A range (50) is smaller than Depot B range (120).<br>3. Depot A is more consistent.",
                "correct_answer": "Depot A (smaller range of 50 vs 120)",
                "tutor_tip": "Smaller range = more consistent."
            }
        ]
    },
    {
        "filename": "functional-skills-symmetry-and-2d-shapes.html",
        "clean_topic": "Symmetry & 2D Shapes",
        "intro_lead": "Identify reflective lines of symmetry, determine rotational symmetry orders, and classify geometric 2D shapes.",
        "next_file": "functional-skills-2d-shapes.html",
        "next_name": "2D Shapes",
        "spec_points": [
            ("E3.8 / L1.21", "Recognise lines of symmetry and rotational symmetry in 2D shapes.")
        ],
        "golden_rules": [
            {
                "icon": "fa-lines-leaning",
                "title": "Golden Rule 1: A Line of Symmetry is a Mirror Line",
                "desc": "If you fold a shape along a line of symmetry, both halves match up perfectly edge-to-edge.",
                "badge": "Reflective Symmetry = Mirror Fold Line"
            },
            {
                "icon": "fa-rotate",
                "title": "Golden Rule 2: Rotational Symmetry is How Many Times it Looks the Same in 360°",
                "desc": "Rotate the shape 360° around its center. The number of times it looks identical to its starting position is its rotational symmetry order (all shapes have at least order 1).",
                "badge": "Rotational Order = Times identical in 360°"
            }
        ],
        "skills": [
            {
                "title": "Symmetry in Common Shapes",
                "summary": "Lines and rotational order of standard shapes.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li>Square: 4 lines, order 4.</li>
                    <li>Rectangle: 2 lines, order 2.</li>
                    <li>Equilateral Triangle: 3 lines, order 3.</li>
                    <li>Isosceles Triangle: 1 line, order 1.</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Safety Warning Symbol Symmetry Analysis",
                "marks": "2 Marks (Entry Level 3 / Level 1)",
                "context": "Health and Safety Wayfinding",
                "question": "A hazard warning sign is an equilateral triangle.<br>(a) How many lines of reflective symmetry does it have?<br>(b) What is its order of rotational symmetry?",
                "steps": [
                    ("Step 1", "Recall symmetry of equilateral triangle", "An equilateral triangle has 3 lines of symmetry passing from each vertex through the opposite midpoint.", "A1: Correct lines of symmetry (3)"),
                    ("Step 2", "Determine rotational order", "An equilateral triangle matches itself 3 times during a 360° rotation (every 120°). Order = 3.", "A1: Correct rotational order (3)")
                ],
                "final_answer": "(a) 3 lines of symmetry | (b) Order 3 rotational symmetry",
                "tutor_tip": "For regular polygons: sides = lines of symmetry = rotational order."
            }
        ],
        "examiner_traps": [
            {
                "title": "Saying a Shape Has '0' Rotational Symmetry",
                "desc": "Every shape looks like itself once after a full 360° turn. The minimum rotational order is 1.",
                "fix": "Never write order 0; write order 1."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "How many lines of symmetry does a standard non-square rectangle have?",
                "solution_steps": "1. A rectangle has 2 lines of symmetry (one horizontal, one vertical through the centers of opposite sides).<br>2. Note: diagonal lines are NOT lines of symmetry in a rectangle.",
                "correct_answer": "2 lines of symmetry",
                "tutor_tip": "A rectangle has 2 lines of symmetry, NOT 4 (diagonals do not match when folded)."
            }
        ]
    },
    {
        "filename": "functional-skills-number-patterns.html",
        "clean_topic": "Number Patterns & Linear Sequences",
        "intro_lead": "Recognise, describe, and continue linear number patterns, decimal sequences, and term-to-term rules in workplace scheduling and stock replenishment.",
        "next_file": "functional-skills-numbers-and-place-value.html",
        "next_name": "Numbers & Place Value",
        "spec_points": [
            ("E3.6 / L1.1", "Recognise and continue linear sequences of whole numbers up to 100 and beyond."),
            ("E3.9 / L1.10", "Recognise and continue sequences that involve decimals and negative numbers.")
        ],
        "golden_rules": [
            {
                "icon": "fa-arrow-up-9-1",
                "title": "Golden Rule 1: Always Find the Term-to-Term Difference First",
                "desc": "Subtract the first number from the second number (and check with the third number) to find the constant step rule (e.g. +4, -7, +0.25).",
                "badge": "Step Rule = 2nd Term − 1st Term (Verify with 3rd Term − 2nd Term)"
            },
            {
                "icon": "fa-arrows-left-right",
                "title": "Golden Rule 2: Check Whether the Sequence Is Increasing or Decreasing",
                "desc": "If numbers get larger, the rule is addition (+). If numbers get smaller, the rule is subtraction (−). Watch carefully when a decreasing sequence crosses zero into negative numbers.",
                "badge": "Getting Larger = Add (+) | Getting Smaller = Subtract (−)"
            }
        ],
        "skills": [
            {
                "title": "Whole Number, Decimal & Negative Sequences",
                "summary": "Identifying common step patterns tested in Entry Level 3, Level 1, and Level 2.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Increasing Whole Number Sequence:</strong> 14, 21, 28, 35, ... (Rule: <strong>Add 7</strong> each time → Next term = <strong>42</strong>).</li>
                    <li><strong>Decreasing Whole Number Sequence:</strong> 90, 78, 66, 54, ... (Rule: <strong>Subtract 12</strong> each time → Next term = <strong>42</strong>).</li>
                    <li><strong>Decimal Sequence:</strong> 1.5, 1.75, 2.0, 2.25, ... (Rule: <strong>Add 0.25</strong> each time → Next term = <strong>2.5</strong>).</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Pharmacy Automated Medication Dispenser Schedule",
                "marks": "2 Marks (Entry Level 3 / Level 1)",
                "context": "Clinical Pharmacy Stock Control",
                "question": "A pharmacy stock counter records the remaining boxes of bandages at the end of each day:<br><strong>Monday: 85 &bull; Tuesday: 71 &bull; Wednesday: 57 &bull; Thursday: 43</strong><br>If usage continues at the same daily rate, how many boxes will remain at the end of Friday?",
                "steps": [
                    ("Step 1", "Find the daily step rule", "85 − 71 = 14 boxes used per day (check: 71 − 57 = 14; 57 − 43 = 14). Rule is subtract 14.", "M1: Correct term-to-term rule (−14)"),
                    ("Step 2", "Apply rule to Thursday's stock", "43 − 14 = 29 boxes remaining on Friday.", "A1: Accurate next term (29)")
                ],
                "final_answer": "29 boxes remaining",
                "tutor_tip": "Always check the difference between at least two pairs of consecutive terms to confirm the pattern is linear."
            }
        ],
        "examiner_traps": [
            {
                "title": "Adding Instead of Subtracting on a Decreasing Sequence",
                "desc": "Students often spot the gap of 14 correctly but add 14 to 43 (giving 57) instead of subtracting 14.",
                "fix": "Write an arrow with '+14' or '−14' above the gap between numbers before calculating."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "Find the next two numbers in this decimal sequence: <strong>0.4, 0.7, 1.0, 1.3, ___, ___</strong>",
                "solution_steps": "1. Difference between terms: 0.7 − 0.4 = +0.3.<br>2. Next term: 1.3 + 0.3 = 1.6.<br>3. Following term: 1.6 + 0.3 = 1.9.",
                "correct_answer": "1.6 and 1.9",
                "tutor_tip": "Think of 0.4, 0.7, 1.0, 1.3 as 4 tenths, 7 tenths, 10 tenths, 13 tenths (+3 tenths each time)."
            }
        ]
    },
    {
        "filename": "functional-skills-temperature.html",
        "clean_topic": "Temperature, Negative Numbers & Thermometer Scales",
        "intro_lead": "Read Celsius and Fahrenheit thermometer scales, calculate temperature rises and drops across zero (0°C), and monitor clinical cold-chain and catering storage limits.",
        "next_file": "functional-skills-scales.html",
        "next_name": "Reading Gauges, Dials & Measuring Scales",
        "spec_points": [
            ("E3.14 / L1.2", "Use and compare measures of temperature including negative numbers in practical contexts."),
            ("L1.2 / L2.1", "Read, write, order and calculate with positive and negative temperatures across 0°C.")
        ],
        "golden_rules": [
            {
                "icon": "fa-temperature-half",
                "title": "Golden Rule 1: Use Zero (0°C) as a Stepping Stone for Negative Temperatures",
                "desc": "To find the difference between a negative temperature (e.g. −6°C) and a positive temperature (e.g. +15°C), find the distance from −6°C up to 0°C (6 degrees), then from 0°C up to 15°C (15 degrees), and add them together: 6 + 15 = 21°C.",
                "badge": "Across Zero Difference = Distance to 0°C + Distance from 0°C"
            },
            {
                "icon": "fa-snowflake",
                "title": "Golden Rule 2: Larger Negative Numbers Are COLDER (Smaller Value)",
                "desc": "Below zero, the scale counts backwards: −18°C is colder (lower) than −4°C because −18 is further below 0°C.",
                "badge": "−18°C is COLDER than −4°C | −4°C is WARMER than −18°C"
            }
        ],
        "skills": [
            {
                "title": "Calculating Temperature Changes & Cold-Chain Limits",
                "summary": "Key benchmark temperatures and number-line jumps across 0°C.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Commercial Freezer Target:</strong> −18°C or colder.</li>
                    <li><strong>Clinical Fridge / Catering Chiller Target:</strong> Between 2°C and 8°C (0°C is the freezing point of water).</li>
                    <li><strong>Normal Human Body Temperature:</strong> 37°C (100°C is the boiling point of water).</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Hospital Catering Walk-In Freezer vs Kitchen Temperature Difference",
                "marks": "3 Marks (Pearson Edexcel Level 1 / Level 2)",
                "context": "Hospital Food Safety Compliance",
                "question": "A catering supervisor checks the digital thermometer in the walk-in freezer, which reads <strong>−19°C</strong>. The main kitchen preparation room temperature is <strong>22°C</strong>.<br>(a) Work out the difference in temperature between the walk-in freezer and the kitchen.<br>(b) The freezer defrost cycle raises its temperature by <strong>5°C</strong>. What is the new freezer temperature?",
                "steps": [
                    ("Step 1", "Bridge across 0°C to find the total difference", "From −19°C up to 0°C = 19°C.<br>From 0°C up to 22°C = 22°C.<br>Total difference = 19 + 22 = 41°C.", "M1 / A1: Accurate bridge across zero (41°C)"),
                    ("Step 2", "Add 5°C rise to −19°C", "Moving 5°C warmer (closer to zero) from −19°C: −19 + 5 = −14°C.", "A1: Accurate negative addition (−14°C)")
                ],
                "final_answer": "(a) Difference = 41°C | (b) New temperature = −14°C",
                "tutor_tip": "When temperature rises from a negative number, the number gets closer to zero (−19°C + 5°C = −14°C, NOT −24°C)."
            }
        ],
        "examiner_traps": [
            {
                "title": "Subtracting 19 from 22 Instead of Bridging Across Zero",
                "desc": "Writing 22 − 19 = 3°C ignores the negative sign on −19°C! Since one temperature is below zero and one is above zero, you must add their distances from zero (22 + 19 = 41°C).",
                "fix": "Sketch a quick vertical thermometer line with 0°C in the middle whenever a question involves negative temperatures."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "Overnight, the outside temperature at an ambulance station drops from <strong>4°C</strong> by <strong>11°C</strong>. What is the new temperature?",
                "solution_steps": "1. Drop 4°C from 4°C to reach 0°C.<br>2. Drop the remaining 7°C below zero (11 − 4 = 7).<br>3. New temperature = −7°C.",
                "correct_answer": "−7°C",
                "tutor_tip": "4 − 11 = −7°C."
            }
        ]
    }
]

with open("/home/subi/Projects/masterfunctionalskills.co.uk/maths_extras.py", "w", encoding="utf-8") as f:
    f.write("#!/usr/bin/env python3\n")
    f.write('"""Maths Basics & Additional Revise Topics (15 Topics)"""\n\n')
    f.write("EXTRAS_MATHS = " + repr(EXTRAS_MATHS) + "\n")

print(f"Maths extras written with {len(EXTRAS_MATHS)} topics!")

