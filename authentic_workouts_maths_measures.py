#!/usr/bin/env python3
"""
Authentic Fluency Workouts: Maths Measures, Shape and Space
10 Core High-Yield Topics:
- speed
- time
- unit-conversions
- volume
- surface-area
- circles
- scales
- angles
- 2d-shapes
- temperature
"""

MATHS_MEASURES_WORKOUTS = {
    # 1. SPEED, DISTANCE & TIME
    "speed": {
        "title": "Speed, Distance & Time",
        "slug": "speed",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.16 • L2.17",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "The Speed Triangle & Time Conversion Rules",
            "points": [
                "Speed Triangle: Distance = Speed × Time; Speed = Distance ÷ Time; Time = Distance ÷ Speed.",
                "Time in Decimals: Always convert minutes to fractions of an hour before calculating!",
                "15 mins = 0.25 hrs (1/4 hr); 30 mins = 0.5 hrs (1/2 hr); 45 mins = 0.75 hrs (3/4 hr).",
                "Other minutes: Minutes ÷ 60 (e.g. 24 mins = 24 ÷ 60 = 0.4 hrs; 1 hr 24 mins = 1.4 hrs).",
                "Never write 1 hour 30 minutes as 1.3 hours!"
            ],
            "calc_tip": "If a calculator displays 2.4 hours, to find minutes multiply the decimal part by 60: 0.4 × 60 = 24 minutes (2 hours 24 mins)."
        },
        "workout_blocks": [
            {
                "title": "Time Conversions (Hours & Minutes to Decimals)",
                "instruction": "Convert the time to decimal hours:",
                "items": [
                    ("a", "30 minutes", "0.5 hours"),
                    ("b", "15 minutes", "0.25 hours"),
                    ("c", "45 minutes", "0.75 hours"),
                    ("d", "1 hour 30 minutes", "1.5 hours"),
                    ("e", "2 hours 15 minutes", "2.25 hours"),
                    ("f", "12 minutes (12 ÷ 60)", "0.2 hours"),
                    ("g", "36 minutes (36 ÷ 60)", "0.6 hours"),
                    ("h", "2 hours 48 minutes", "2.8 hours (48 ÷ 60 = 0.8)")
                ]
            },
            {
                "title": "Calculating Speed, Distance & Time",
                "instruction": "Use Speed = D ÷ T, Distance = S × T, or Time = D ÷ S:",
                "items": [
                    ("a", "Distance = 120 miles, Time = 2 hours. Speed = ?", "60 mph"),
                    ("b", "Speed = 45 mph, Time = 3 hours. Distance = ?", "135 miles"),
                    ("c", "Distance = 180 km, Speed = 60 km/h. Time = ?", "3 hours"),
                    ("d", "Distance = 75 miles, Time = 1 hour 30 minutes. Speed = ?", "50 mph (75 ÷ 1.5)"),
                    ("e", "Speed = 56 mph, Time = 2 hours 15 minutes. Distance = ?", "126 miles (56 × 2.25)"),
                    ("f", "Distance = 140 miles, Speed = 50 mph. Time in hours & mins?", "2 hours 48 mins (2.8 hrs)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "NHS Emergency Blood Courier",
                "stem": "An emergency medical motorcycle courier carries urgent blood supplies between two hospital trauma centres <strong>84 miles apart</strong>.<br>The courier leaves at <strong>14:15</strong> and must arrive before <strong>15:45</strong>.<br>(a) What is the maximum journey time allowed in hours and minutes, and in decimal hours?<br>(b) Calculate the minimum average speed the courier must maintain to arrive on time.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Time available: 14:15 to 15:45 = 1 hour 30 minutes = 1.5 hours", "[M1]"),
                    ("Calculate Speed: Speed = Distance ÷ Time = 84 miles ÷ 1.5 hours", "[M1]"),
                    ("Speed = 56 mph", "[A1]")
                ],
                "final_answer": "(a) 1 hour 30 mins (1.5 hrs) | (b) 56 mph",
                "reverse_check": "56 mph × 1.5 hours = 84 miles.",
                "pitfall": "Dividing 84 by 1.3 instead of 1.5."
            }
        ]
    },

    # 2. TIME & TIMETABLES
    "time": {
        "title": "Time, 24-Hour Clocks & Timetables",
        "slug": "time",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.15 • L2.16",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "12-Hour vs 24-Hour Clocks & Journey Schedules",
            "points": [
                "24-Hour Clock: Add 12 to PM hours (e.g. 3:45 pm = 15:45; 11:20 pm = 23:20).",
                "Midnight: 00:00 (or 24:00); 12:30 am = 00:30.",
                "Elapsed Time: Count forward in chunks: count minutes to the next whole hour, count full hours, then add remaining minutes.",
                "Reading Timetables: Follow columns down for individual bus/train services, and rows across for stop arrival times."
            ],
            "calc_tip": "Remember there are 60 minutes in an hour, NOT 100! 08:45 plus 30 minutes is 09:15, NOT 08:75!"
        },
        "workout_blocks": [
            {
                "title": "12-Hour to 24-Hour Clock Conversions",
                "instruction": "Convert each time to 24-hour clock format (e.g. 14:30):",
                "items": [
                    ("a", "8:15 am", "08:15"),
                    ("b", "2:40 pm", "14:40"),
                    ("c", "7:05 pm", "19:05"),
                    ("d", "11:50 pm", "23:50"),
                    ("e", "12:15 pm (noon)", "12:15"),
                    ("f", "12:30 am (night)", "00:30"),
                    ("g", "9:45 pm", "21:45"),
                    ("h", "10:08 am", "10:08")
                ]
            },
            {
                "title": "Elapsed Time Calculations",
                "instruction": "Calculate the duration between the two times:",
                "items": [
                    ("a", "08:40 to 10:15", "1 hour 35 minutes"),
                    ("b", "13:25 to 16:10", "2 hours 45 minutes"),
                    ("c", "19:50 to 22:30", "2 hours 40 minutes"),
                    ("d", "23:45 to 02:15 (next day)", "2 hours 30 minutes"),
                    ("e", "Start 09:20, duration 45 mins. Finish time?", "10:05"),
                    ("f", "Start 14:45, duration 1 hr 50 mins. Finish time?", "16:35")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "NHS Shift Handover & Travel",
                "stem": "A clinical support worker must arrive at the hospital ward for a shift briefing starting at <strong>07:15</strong>.<br>Her morning routine and journey take:<br>• Getting dressed and breakfast: <strong>35 minutes</strong><br>• Walking to the bus stop: <strong>10 minutes</strong><br>• Bus journey: <strong>28 minutes</strong><br>• Walking from bus stop to ward: <strong>7 minutes</strong><br>What is the latest time she can wake up in the morning to arrive exactly on time?",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Sum total preparation & journey time: 35 + 10 + 28 + 7 = 80 minutes", "[M1]"),
                    ("Convert 80 minutes to hours and minutes: 1 hour 20 minutes", "[M1]"),
                    ("Count backwards from 07:15: 07:15 minus 1 hour = 06:15; 06:15 minus 20 mins = 05:55", "[A1]")
                ],
                "final_answer": "05:55 (or 5:55 am)",
                "reverse_check": "05:55 + 1 hour 20 minutes = 07:15.",
                "pitfall": "Counting backwards incorrectly (e.g. 07:15 minus 80 mins as 06:35)."
            }
        ]
    },

    # 3. UNIT CONVERSIONS
    "unit-conversions": {
        "title": "Metric & Imperial Unit Conversions",
        "slug": "unit-conversions",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.14 • L2.15",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Metric Prefixes & Conversion Factors",
            "points": [
                "Length: 1 km = 1,000 m; 1 m = 100 cm; 1 cm = 10 mm (1 m = 1,000 mm).",
                "Mass: 1 tonne = 1,000 kg; 1 kg = 1,000 g; 1 g = 1,000 mg.",
                "Capacity: 1 litre = 1,000 ml; 1 cl = 10 ml.",
                "Big unit to smaller unit: MULTIPLY (e.g. 3.5 m × 100 = 350 cm).",
                "Smaller unit to bigger unit: DIVIDE (e.g. 450 g ÷ 1,000 = 0.45 kg).",
                "Common Imperial Approximations: 1 inch ≈ 2.5 cm; 1 kg ≈ 2.2 lbs; 1 gallon ≈ 4.5 litres; 5 miles ≈ 8 km."
            ],
            "calc_tip": "Always check units before doing area or volume! Convert all lengths to the same unit BEFORE multiplying."
        },
        "workout_blocks": [
            {
                "title": "Metric Length Conversions",
                "instruction": "Convert each length:",
                "items": [
                    ("a", "4.5 m into cm", "450 cm (× 100)"),
                    ("b", "75 cm into m", "0.75 m (÷ 100)"),
                    ("c", "12 cm into mm", "120 mm (× 10)"),
                    ("d", "85 mm into cm", "8.5 cm (÷ 10)"),
                    ("e", "2.4 km into m", "2,400 m (× 1,000)"),
                    ("f", "650 m into km", "0.65 km (÷ 1,000)"),
                    ("g", "1.8 m into mm", "1,800 mm (× 1,000)"),
                    ("h", "350 mm into m", "0.35 m (÷ 1,000)")
                ]
            },
            {
                "title": "Metric Mass & Capacity Conversions",
                "instruction": "Convert the weight or liquid capacity:",
                "items": [
                    ("a", "3.2 kg into grams", "3,200 g"),
                    ("b", "450 g into kg", "0.45 kg"),
                    ("c", "2.5 tonnes into kg", "2,500 kg"),
                    ("d", "1.75 litres into ml", "1,750 ml"),
                    ("e", "250 ml into litres", "0.25 litres"),
                    ("f", "500 mg into grams", "0.5 g"),
                    ("g", "80 ml into litres", "0.08 litres"),
                    ("h", "0.05 kg into grams", "50 g")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Commercial Joinery Flooring Trim",
                "stem": "A carpenter fits metal transition strips across <strong>6 doorways</strong>.<br>Each doorway opening is <strong>85 centimetres wide</strong>.<br>Transition strip is sold in <strong>2.4-metre lengths</strong>.<br>How many 2.4-metre lengths must the carpenter purchase?",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Convert doorway width to metres: 85 cm = 0.85 m", "[M1]"),
                    ("Calculate cuts from one 2.4 m length: 2.4 ÷ 0.85 = 2.82 → Each length provides 2 complete strips (0.85 × 2 = 1.7 m, with 0.7 m offcut)", "[M1]"),
                    ("Lengths needed for 6 doorways: 6 doorways ÷ 2 per length = 3 lengths", "[A1]")
                ],
                "final_answer": "3 lengths",
                "reverse_check": "3 lengths × 2 doorways each = 6 doorways covered.",
                "pitfall": "Dividing total length (6 × 0.85 = 5.1 m) by 2.4 m to get 2.125 and rounding up to 2 lengths (which fails because you cannot join small offcuts across a doorway!)."
            }
        ]
    },

    # 4. VOLUME
    "volume": {
        "title": "Volume & Capacity",
        "slug": "volume",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.25 • L2.21",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Volume Formulas & Liquid Capacity",
            "points": [
                "Cuboid Volume = Length × Width × Height (V = L × W × H).",
                "Cube Volume = Side³ (V = s × s × s).",
                "Prism Volume = Cross-Sectional Area × Length (V = A × L).",
                "Cylinder Volume = π × r² × Height (V = πr²h).",
                "Volume to Liquid Capacity: 1 cm³ = 1 ml; 1,000 cm³ = 1 litre; 1 m³ = 1,000 litres."
            ],
            "calc_tip": "Always ensure all 3 dimensions are in the same unit (all cm or all m) BEFORE multiplying!"
        },
        "workout_blocks": [
            {
                "title": "Volume of Cuboids and Cubes",
                "instruction": "Calculate the volume (L × W × H):",
                "suffix": "cm³",
                "items": [
                    ("a", "Cuboid: 8 cm × 5 cm × 3 cm", "120 cm³"),
                    ("b", "Cuboid: 12 cm × 4 cm × 5 cm", "240 cm³"),
                    ("c", "Cube with side length 5 cm", "125 cm³ (5³)"),
                    ("d", "Cuboid: 10 m × 4 m × 2.5 m", "100 m³"),
                    ("e", "Cuboid: 15 cm × 6 cm × 4 cm", "360 cm³"),
                    ("f", "Cube with side length 4 m", "64 m³ (4³)")
                ]
            },
            {
                "title": "Volume of Cylinders & Triangular Prisms (Level 2)",
                "instruction": "Use V = Area of base × Length (use π = 3.14):",
                "items": [
                    ("a", "Cylinder: Radius 3 cm, Height 10 cm", "282.6 cm³ (3.14 × 9 × 10)"),
                    ("b", "Cylinder: Radius 5 m, Height 4 m", "314 m³ (3.14 × 25 × 4)"),
                    ("c", "Cylinder: Diameter 8 cm (r = 4), Height 12 cm", "602.88 cm³ (3.14 × 16 × 12)"),
                    ("d", "Triangular prism: Triangle base 6 cm, height 4 cm, length 15 cm", "180 cm³ ((6×4÷2) × 15)"),
                    ("e", "Convert 4,500 cm³ into litres", "4.5 litres (4,500 ÷ 1,000)"),
                    ("f", "Convert 2.8 m³ into litres", "2,800 litres (2.8 × 1,000)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "NHS Clinical Hydrotherapy Pool",
                "stem": "An NHS rehabilitation hospital builds a rectangular hydrotherapy exercise pool.<br>The pool dimensions are: <strong>12 metres long by 5 metres wide by 1.5 metres deep</strong>.<br>(a) Calculate the volume of the pool in cubic metres (m³).<br>(b) 1 cubic metre holds 1,000 litres of water. How many litres of water are needed to fill the pool?",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Calculate volume: 12 × 5 × 1.5 = 90 m³", "[M1]"),
                    ("Convert to litres: 90 m³ × 1,000 litres/m³ = 90,000 litres", "[A1]")
                ],
                "final_answer": "(a) 90 m³ | (b) 90,000 litres",
                "reverse_check": "90,000 ÷ 1,000 = 90 m³; 90 ÷ 1.5 ÷ 5 = 12 m.",
                "pitfall": "Forgetting to multiply by 1,000 to convert cubic metres to litres."
            }
        ]
    },

    # 5. SURFACE AREA
    "surface-area": {
        "title": "Surface Area of Prisms & Cylinders",
        "slug": "surface-area",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L2.20",
        "level": "Level 2",
        "method_card": {
            "title": "Total Surface Area of 3D Solids",
            "points": [
                "Surface area is the total area of all 2D outer faces added together (measured in cm², m²).",
                "Cuboid (6 faces): 2(LW) + 2(LH) + 2(WH).",
                "Cube: 6 × side².",
                "Triangular Prism: 2 triangular ends + 3 rectangular side faces.",
                "Cylinder: 2 circular ends (2 × πr²) + curved surface area (2πrh or πdh)."
            ],
            "calc_tip": "If a question involves an open box or tank without a lid, count only 5 faces (1 base + 4 walls)!"
        },
        "workout_blocks": [
            {
                "title": "Surface Area of Cuboids and Cubes",
                "instruction": "Work out the total surface area of each solid:",
                "suffix": "cm²",
                "items": [
                    ("a", "Cube with side length 5 cm", "150 cm² (6 × 25)"),
                    ("b", "Cube with side length 8 cm", "384 cm² (6 × 64)"),
                    ("c", "Cuboid: 6 cm × 4 cm × 3 cm", "108 cm² (2×24 + 2×18 + 2×12)"),
                    ("d", "Cuboid: 10 cm × 5 cm × 2 cm", "160 cm² (2×50 + 2×20 + 2×10)"),
                    ("e", "Open-top box (no lid): 8 cm × 5 cm × 4 cm", "144 cm² (40 + 2×32 + 2×20)"),
                    ("f", "Cuboid: 2 m × 1.5 m × 3 m", "27 m² (2×3 + 2×6 + 2×4.5)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Warehouse Cardboard Box Manufacturing",
                "stem": "A medical supplies warehouse orders custom cardboard packaging boxes.<br>Each box is a closed cuboid measuring <strong>40 cm long by 30 cm wide by 20 cm high</strong>.<br>(a) Calculate the total surface area of one box in cm².<br>(b) A production run manufactures <strong>500 boxes</strong>. What is the total area of cardboard required in square metres (m²)? (1 m² = 10,000 cm²).",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Face areas: Front/Back = 2 × (40×20) = 1,600 cm²; Top/Bottom = 2 × (40×30) = 2,400 cm²; Left/Right = 2 × (30×20) = 1,200 cm²", "[M1]"),
                    ("Total surface area 1 box = 1,600 + 2,400 + 1,200 = 5,200 cm²", "[M1]"),
                    ("500 boxes = 500 × 5,200 = 2,600,000 cm². Convert to m²: 2,600,000 ÷ 10,000 = 260 m²", "[A1]")
                ],
                "final_answer": "(a) 5,200 cm² | (b) 260 m²",
                "reverse_check": "260 m² ÷ 500 = 0.52 m² = 5,200 cm² per box.",
                "pitfall": "Dividing by 100 instead of 10,000 when converting cm² to m²."
            }
        ]
    },

    # 6. CIRCLES
    "circles": {
        "title": "Circles: Radius, Diameter, Circumference & Area",
        "slug": "circles",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L2.19 • L2.20",
        "level": "Level 2",
        "method_card": {
            "title": "Circle Formulas & Radius vs Diameter",
            "points": [
                "Radius (r): Distance from centre to edge.",
                "Diameter (d): Distance straight across through centre (d = 2r; r = d ÷ 2).",
                "Circumference (perimeter around circle): C = π × d (or 2 × π × r).",
                "Area (space inside circle): Area = π × r² (π ≈ 3.14 or 3.142).",
                "Golden Rule: In Area, always square the radius BEFORE multiplying by π. Never square the diameter!"
            ],
            "calc_tip": "If given the diameter, IMMEDIATELY divide by 2 to write down the radius before doing any Area calculation."
        },
        "workout_blocks": [
            {
                "title": "Radius and Diameter Relationships",
                "instruction": "Find the missing radius or diameter:",
                "items": [
                    ("a", "Radius = 6 cm. Diameter = ?", "12 cm"),
                    ("b", "Radius = 8.5 m. Diameter = ?", "17 m"),
                    ("c", "Diameter = 14 cm. Radius = ?", "7 cm"),
                    ("d", "Diameter = 25 m. Radius = ?", "12.5 m"),
                    ("e", "Diameter = 9 cm. Radius = ?", "4.5 cm"),
                    ("f", "Radius = 11 mm. Diameter = ?", "22 mm")
                ]
            },
            {
                "title": "Circumference & Area Calculations (use π = 3.14)",
                "instruction": "Calculate the circumference or area:",
                "items": [
                    ("a", "Circumference: Diameter = 10 cm", "31.4 cm (3.14 × 10)"),
                    ("b", "Circumference: Radius = 5 m (d = 10)", "31.4 m"),
                    ("c", "Circumference: Diameter = 20 cm", "62.8 cm"),
                    ("d", "Area: Radius = 3 cm", "28.26 cm² (3.14 × 9)"),
                    ("e", "Area: Radius = 10 m", "314 m² (3.14 × 100)"),
                    ("f", "Area: Diameter = 8 cm (r = 4 cm)", "50.24 cm² (3.14 × 16)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Landscape Gardening Circular Lawn",
                "stem": "A landscape gardener designs a circular flower bed with a <strong>diameter of 6 metres</strong>.<br>The perimeter of the bed will have decorative stone edging costing <strong>£8.50 per metre</strong>.<br>The interior of the bed will be covered with mulch costing <strong>£4.00 per square metre</strong>.<br>(a) Work out the cost of the stone edging (Use π = 3.14).<br>(b) Work out the cost of the mulch.",
                "marks": 4,
                "prefix": "£",
                "steps": [
                    ("Circumference = π × d = 3.14 × 6 = 18.84 metres", "[M1]"),
                    ("Edging cost = 18.84 × £8.50 = £160.14", "[A1]"),
                    ("Radius = 6 ÷ 2 = 3 m. Area = π × r² = 3.14 × 3² = 3.14 × 9 = 28.26 m²", "[M1]"),
                    ("Mulch cost = 28.26 × £4.00 = £113.04", "[A1]")
                ],
                "final_answer": "(a) Edging = £160.14 | (b) Mulch = £113.04",
                "reverse_check": "Radius 3m gives area ~28m² × £4 ≈ £112 (sensible).",
                "pitfall": "Using diameter 6 in the area formula (3.14 × 36), which quadruples the area!"
            }
        ]
    },

    # 7. SCALES
    "scales": {
        "title": "Reading Gauges, Dials & Measuring Scales",
        "slug": "scales",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.13 • L2.15",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Scale Divisions & Scale Drawings",
            "points": [
                "Step 1 to read any scale: Find the value between two labeled marks.",
                "Step 2: Count how many small intervals/divisions are between them.",
                "Step 3: Divide the value by the number of divisions to find the value of 1 division.",
                "Map Scales (e.g. 1 : 20,000): 1 cm on the map represents 20,000 cm in real life (20,000 cm ÷ 100 = 200 m).",
                "Grid Plans (e.g. 1 cm = 2 m): Multiply grid measurements by 2 to get real dimensions."
            ],
            "calc_tip": "Always count the SPACES between marks, not the tick lines!"
        },
        "workout_blocks": [
            {
                "title": "Reading Value of One Division",
                "instruction": "Work out the value of 1 small division on each scale:",
                "items": [
                    ("a", "Between 0 and 10 there are 5 equal divisions", "2 units per division (10 ÷ 5)"),
                    ("b", "Between 0 and 100 there are 10 equal divisions", "10 units per division (100 ÷ 10)"),
                    ("c", "Between 20 and 30 there are 10 equal divisions", "1 unit per division (10 ÷ 10)"),
                    ("d", "Between 0 and 1 litre there are 4 equal divisions", "250 ml (0.25 L per division)"),
                    ("e", "Between 0 and 5 kg there are 10 equal divisions", "0.5 kg (500 g per division)"),
                    ("f", "Between 60 and 80 there are 4 equal divisions", "5 units per division (20 ÷ 4)")
                ]
            },
            {
                "title": "Scale Plan Drawings (Ratio Scales)",
                "instruction": "Calculate the real-world distance:",
                "items": [
                    ("a", "Scale 1 cm = 2 m. Drawing length = 5 cm. Real length?", "10 metres"),
                    ("b", "Scale 1 cm = 5 m. Drawing length = 8 cm. Real length?", "40 metres"),
                    ("c", "Scale 1 : 50. Drawing length = 6 cm. Real length in metres?", "3 metres (300 cm)"),
                    ("d", "Scale 1 : 100. Drawing length = 12.5 cm. Real length in metres?", "12.5 metres (1,250 cm)"),
                    ("e", "Real length = 20 m. Scale 1 cm = 4 m. Drawing length?", "5 cm (20 ÷ 4)"),
                    ("f", "Real length = 15 m. Scale 1 : 100. Drawing length?", "15 cm (1,500 ÷ 100)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "NHS Hospital Ward Floor Plan",
                "stem": "An estates surveyor draws a floor plan for a new hospital treatment room.<br>The scale on the architectural drawing is <strong>1 : 50</strong>.<br>On the plan, the rectangular room measures <strong>14 cm long by 9 cm wide</strong>.<br>(a) Calculate the real-world length and width of the room in metres.<br>(b) Work out the actual floor area of the room in square metres (m²).",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Real length: 14 cm × 50 = 700 cm = 7.0 metres", "[M1]"),
                    ("Real width: 9 cm × 50 = 450 cm = 4.5 metres", "[M1]"),
                    ("Actual floor area = 7.0 m × 4.5 m = 31.5 m²", "[A1]")
                ],
                "final_answer": "(a) Length = 7.0 m, Width = 4.5 m | (b) Area = 31.5 m²",
                "reverse_check": "Area on plan = 14 × 9 = 126 cm². Real area = 126 × 50² = 126 × 2,500 = 315,000 cm² = 31.5 m².",
                "pitfall": "Calculating area on the plan (126 cm²) and multiplying by 50 instead of 50² (2,500)."
            }
        ]
    },

    # 8. ANGLES
    "angles": {
        "title": "Angles: Types, Measuring & Bearings",
        "slug": "angles",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.21 • L2.18",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Angle Rules & Facts",
            "points": [
                "Acute angle: Less than 90°.",
                "Right angle: Exactly 90° (perpendicular lines).",
                "Obtuse angle: Between 90° and 180°.",
                "Reflex angle: Between 180° and 360°.",
                "Angles on a straight line add up to 180°.",
                "Angles around a point add up to 360°.",
                "Angles inside any triangle add up to 180°.",
                "Angles inside any quadrilateral add up to 360°."
            ],
            "calc_tip": "When measuring with a protractor, align the centre crosshair exactly over the vertex and start reading from the '0' that lies on your baseline."
        },
        "workout_blocks": [
            {
                "title": "Classifying Angles",
                "instruction": "State whether each angle is Acute, Right, Obtuse, or Reflex:",
                "items": [
                    ("a", "45°", "Acute"),
                    ("b", "90°", "Right angle"),
                    ("c", "135°", "Obtuse"),
                    ("d", "180°", "Straight line"),
                    ("e", "210°", "Reflex"),
                    ("f", "89°", "Acute"),
                    ("g", "91°", "Obtuse"),
                    ("h", "315°", "Reflex")
                ]
            },
            {
                "title": "Missing Angles on Lines & in Triangles",
                "instruction": "Calculate the missing angle x:",
                "items": [
                    ("a", "Straight line: 125° and x", "x = 55° (180 - 125)"),
                    ("b", "Straight line: 72° and x", "x = 108° (180 - 72)"),
                    ("c", "Right angle: 38° and x", "x = 52° (90 - 38)"),
                    ("d", "Around a point: 110°, 120°, and x", "x = 130° (360 - 230)"),
                    ("e", "Triangle: 65°, 55°, and x", "x = 60° (180 - 120)"),
                    ("f", "Right-angled triangle: 90°, 34°, and x", "x = 56° (90 - 34)"),
                    ("g", "Equilateral triangle: all angles are", "60° each (180 ÷ 3)"),
                    ("h", "Quadrilateral: 100°, 85°, 95°, and x", "x = 80° (360 - 280)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Carpentry Roof Truss Construction",
                "stem": "A site carpenter constructs an isosceles timber roof truss.<br>The apex angle at the top of the roof is <strong>70°</strong>.<br>The two base angles at the bottom are equal.<br>Calculate the size of each base angle.",
                "marks": 2,
                "prefix": "",
                "steps": [
                    ("Remaining degrees in triangle: 180° - 70° = 110°", "[M1]"),
                    ("Divide equally between the two base angles: 110° ÷ 2 = 55°", "[A1]")
                ],
                "final_answer": "55°",
                "reverse_check": "70° + 55° + 55° = 180°.",
                "pitfall": "Dividing 180 by 2 without subtracting the 70° apex angle first."
            }
        ]
    },

    # 9. 2D SHAPES
    "2d-shapes": {
        "title": "2D Shapes & Polygons",
        "slug": "2d-shapes",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.22 • L2.19",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Polygon Properties & Symmetry",
            "points": [
                "Triangle (3 sides), Quadrilateral (4 sides), Pentagon (5 sides), Hexagon (6 sides), Heptagon (7 sides), Octagon (8 sides), Decagon (10 sides).",
                "Regular Polygon: All sides are equal in length and all interior angles are equal.",
                "Line Symmetry: Mirror line that splits the shape into two identical halves.",
                "Rotational Symmetry: The number of times a shape looks identical to itself in one full 360° turn.",
                "A regular polygon with n sides has exactly n lines of symmetry and rotational symmetry of order n."
            ],
            "calc_tip": "A regular hexagon has 6 lines of symmetry; a regular octagon has 8 lines of symmetry."
        },
        "workout_blocks": [
            {
                "title": "Naming Polygons & Counting Sides",
                "instruction": "State the number of sides and shape name:",
                "items": [
                    ("a", "Polygon with 5 straight sides", "Pentagon (5 sides)"),
                    ("b", "Polygon with 6 straight sides", "Hexagon (6 sides)"),
                    ("c", "Polygon with 8 straight sides", "Octagon (8 sides)"),
                    ("d", "Polygon with 4 equal sides and 4 right angles", "Square"),
                    ("e", "Polygon with 4 sides and only 1 pair of parallel sides", "Trapezium"),
                    ("f", "Quadrilateral with 2 pairs of parallel sides and no right angles", "Parallelogram / Rhombus")
                ]
            },
            {
                "title": "Symmetry & Shape Properties",
                "instruction": "State the number of lines of symmetry:",
                "items": [
                    ("a", "Equilateral triangle", "3 lines of symmetry"),
                    ("b", "Isosceles triangle", "1 line of symmetry"),
                    ("c", "Scalene triangle", "0 lines of symmetry"),
                    ("d", "Square", "4 lines of symmetry"),
                    ("e", "Rectangle (non-square)", "2 lines of symmetry"),
                    ("f", "Regular hexagon", "6 lines of symmetry"),
                    ("g", "Circle", "Infinite lines of symmetry"),
                    ("h", "Parallelogram", "0 lines of symmetry (Rotational order 2)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "NHS Clinic Paving Design",
                "stem": "An NHS healthcare facility installs safety signboards and paving.<br>An emergency stop sign is manufactured in the shape of a <strong>regular octagon</strong>.<br>Each side of the octagon measures <strong>35 centimetres</strong>.<br>(a) Calculate the perimeter of the signboard in metres.<br>(b) How many lines of reflective symmetry does the sign have?",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("An octagon has 8 equal sides. Total perimeter in cm = 8 × 35 cm = 280 cm", "[M1]"),
                    ("Convert to metres: 280 cm ÷ 100 = 2.8 metres", "[A1]"),
                    ("A regular octagon has 8 lines of symmetry.", "[A1]")
                ],
                "final_answer": "(a) 2.8 metres | (b) 8 lines of symmetry",
                "reverse_check": "2.8 m = 280 cm; 280 ÷ 8 = 35 cm.",
                "pitfall": "Confusing an octagon (8 sides) with a hexagon (6 sides)."
            }
        ]
    },

    # 10. TEMPERATURE
    "temperature": {
        "title": "Temperature, Negative Numbers & Thermometer Scales",
        "slug": "temperature",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: E3.7 • L1.17",
        "level": "Entry 3 & Level 1",
        "method_card": {
            "title": "Negative Numbers & Temperature Differences",
            "points": [
                "On a thermometer scale, numbers below zero have a minus sign (-).",
                "The further below zero, the colder the temperature (-8°C is colder than -2°C).",
                "Rise in temperature: Add (+); Drop/fall in temperature: Subtract (-).",
                "Finding temperature difference crossing zero: Add distance below zero to distance above zero (e.g. from -5°C to 12°C = 5 + 12 = 17°C difference)."
            ],
            "calc_tip": "When finding temperature difference between a negative and positive value: Highest - Lowest = 14 - (-6) = 14 + 6 = 20°C."
        },
        "workout_blocks": [
            {
                "title": "Comparing & Ordering Temperatures",
                "instruction": "Order from coldest to warmest:",
                "items": [
                    ("a", "-4°C, 3°C, -8°C, 0°C", "-8°C, -4°C, 0°C, 3°C"),
                    ("b", "-12°C, -15°C, -2°C, 5°C", "-15°C, -12°C, -2°C, 5°C"),
                    ("c", "Which is colder: -7°C or -3°C?", "-7°C"),
                    ("d", "Which is warmer: -1°C or -5°C?", "-1°C"),
                    ("e", "Which temperature is below freezing: 2°C or -1°C?", "-1°C"),
                    ("f", "Order: 14°C, -6°C, -1°C, 8°C", "-6°C, -1°C, 8°C, 14°C")
                ]
            },
            {
                "title": "Temperature Changes & Differences",
                "instruction": "Calculate the new temperature or difference:",
                "items": [
                    ("a", "Temperature is -3°C. It rises by 8°C. New temp?", "5°C (-3 + 8)"),
                    ("b", "Temperature is 4°C. It drops by 9°C. New temp?", "-5°C (4 - 9)"),
                    ("c", "Temperature is -6°C. It falls by 4°C. New temp?", "-10°C (-6 - 4)"),
                    ("d", "Difference between -5°C and 7°C", "12°C (5 + 7)"),
                    ("e", "Difference between -12°C and -4°C", "8°C (12 - 4)"),
                    ("f", "Difference between -2°C and 18°C", "20°C (2 + 18)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "NHS Vaccine Cold-Chain Storage",
                "stem": "An NHS hospital pharmacy stores temperature-sensitive vaccines in a specialist freezer.<br>The target storage temperature is <strong>-18°C</strong>.<br>The safety regulations allow a tolerance of <strong>±3°C</strong>.<br>(a) What are the minimum and maximum acceptable temperatures?<br>(b) During a power interruption, the freezer temperature rises to <strong>-11°C</strong>. Did the freezer breach the safety limit? State the difference.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Minimum acceptable = -18°C - 3°C = -21°C; Maximum acceptable = -18°C + 3°C = -15°C", "[M1]"),
                    ("Tolerance range is -21°C to -15°C", "[M1]"),
                    ("At -11°C, the temperature is warmer than -15°C. Conclusion: Yes, breached by 4°C (-11 - (-15) = +4°C).", "[A1]")
                ],
                "final_answer": "(a) -21°C to -15°C | (b) Yes, breached (4°C too warm)",
                "reverse_check": "-15°C + 4°C = -11°C.",
                "pitfall": "Thinking -11°C is colder than -15°C."
            }
        ]
    }
}
