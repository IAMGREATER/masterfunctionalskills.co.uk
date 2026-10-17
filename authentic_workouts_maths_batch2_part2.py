#!/usr/bin/env python3
"""
Authentic Fluency Workouts: Maths Batch 2 (Part 2 - Measures, Space, Shape & Geometry)
15 Curriculum Topics:
1. length
2. weight
3. capacity
4. density
5. using-length-area-and-volume-in-calculations
6. 3d-shape-basics
7. 3d-shapes
8. nets
9. angles-and-bearings
10. angles-in-2d-shapes
11. coordinates
12. movement-and-direction
13. maps-and-scale-drawings
14. plans-and-elevations
15. symmetry-and-2d-shapes
"""

MATHS_BATCH2_PART2_WORKOUTS = {
    # 1. LENGTH
    "length": {
        "title": "Length & Dimensions",
        "slug": "length",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.18 • L2.20",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Metric Length Hierarchy & Conversions",
            "points": [
                "1 kilometre (km) = 1,000 metres (m).",
                "1 metre (m) = 100 centimetres (cm).",
                "1 centimetre (cm) = 10 millimetres (mm).",
                "Converting smaller unit to larger unit: Divide (e.g. 450 mm ÷ 10 = 45 cm; 250 cm ÷ 100 = 2.5 m).",
                "Converting larger unit to smaller unit: Multiply (e.g. 1.8 m × 100 = 180 cm; 3.5 km × 1,000 = 3,500 m)."
            ],
            "calc_tip": "Always ensure all dimensions in an area or perimeter calculation are converted to the same unit before calculating."
        },
        "workout_blocks": [
            {
                "title": "Metric Length Conversions",
                "instruction": "Convert to the requested unit:",
                "items": [
                    ("a", "4.5 m into cm", "450 cm"),
                    ("b", "120 cm into metres", "1.2 m"),
                    ("c", "85 mm into cm", "8.5 cm"),
                    ("d", "6.2 cm into mm", "62 mm"),
                    ("e", "2.8 km into metres", "2,800 m"),
                    ("f", "750 m into km", "0.75 km"),
                    ("g", "0.35 m into mm", "350 mm"),
                    ("h", "1,850 mm into metres", "1.85 m")
                ]
            },
            {
                "title": "Adding and Subtracting Lengths",
                "instruction": "Convert to a common unit before calculating:",
                "items": [
                    ("a", "1.4 m + 85 cm (answer in metres)", "2.25 m (1.4 + 0.85)"),
                    ("b", "3.2 m - 90 cm (answer in metres)", "2.3 m (3.2 - 0.9)"),
                    ("c", "45 cm + 120 mm (answer in cm)", "57 cm (45 + 12)"),
                    ("d", "2.5 km - 600 m (answer in km)", "1.9 km (2.5 - 0.6)"),
                    ("e", "Cut 4 pieces of 35 cm from 2 m of timber. Wood left?", "60 cm (200 - 140)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Carpentry & Joinery Door Trim",
                "stem": "A joiner is installing architrave moulding around a standard doorway.<br>The doorway requires <strong>two vertical side pieces of 2.1 metres each</strong> and <strong>one top horizontal piece of 95 centimetres</strong>.<br>The moulding is sold in <strong>2.4-metre timber lengths</strong> at <strong>£8.40 per length</strong>.<br>(a) Work out the total length of moulding needed in metres.<br>(b) How many 2.4-metre lengths must the joiner purchase, and what is the total cost?",
                "marks": 3,
                "prefix": "£",
                "steps": [
                    ("Convert top piece: 95 cm = 0.95 m", "[M1]"),
                    ("Total required: 2.1 + 2.1 + 0.95 = 5.15 m", "[M1]"),
                    ("Determine lengths: 5.15 ÷ 2.4 = 2.14 → 3 lengths needed (one for each upright, one for header); Cost: 3 × £8.40 = £25.20", "[A1]")
                ],
                "final_answer": "3 lengths costing £25.20 (5.15 m total)",
                "reverse_check": "3 × 2.4 m = 7.2 m (covers 5.15 m).",
                "pitfall": "Adding 2.1 + 0.95 directly as 3.05 without converting centimetres to metres or omitting the second vertical jamb."
            }
        ]
    },

    # 2. WEIGHT
    "weight": {
        "title": "Weight & Mass",
        "slug": "weight",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.18 • L2.20 • L2.21",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Metric Mass Conversions & Scales",
            "points": [
                "1 tonne (t) = 1,000 kilograms (kg).",
                "1 kilogram (kg) = 1,000 grams (g).",
                "1 gram (g) = 1,000 milligrams (mg).",
                "Kilograms to grams: Multiply by 1,000; Grams to kilograms: Divide by 1,000.",
                "Reading dial/spring scales: Always find the value of one division marker before reading."
            ],
            "calc_tip": "When reading medical dosages or recipes, double check whether the unit is mg, g, or kg."
        },
        "workout_blocks": [
            {
                "title": "Metric Mass Conversions",
                "instruction": "Convert each mass into the specified unit:",
                "items": [
                    ("a", "3.5 kg into grams", "3,500 g"),
                    ("b", "450 g into kilograms", "0.45 kg"),
                    ("c", "2,400 g into kilograms", "2.4 kg"),
                    ("d", "0.85 kg into grams", "850 g"),
                    ("e", "2.5 tonnes into kilograms", "2,500 kg"),
                    ("f", "4,200 kg into tonnes", "4.2 tonnes"),
                    ("g", "500 mg into grams", "0.5 g"),
                    ("h", "1.2 g into milligrams", "1,200 mg")
                ]
            },
            {
                "title": "Practical Scaling and Batch Portions",
                "instruction": "Work out the total mass or number of portions:",
                "items": [
                    ("a", "12 parcels weighing 250 g each. Total weight in kg?", "3 kg (3,000 g)"),
                    ("b", "A 5 kg sack of flour used in 200 g portions. Portions?", "25 portions (5,000 ÷ 200)"),
                    ("c", "Max van load is 850 kg. 6 pallets weigh 130 kg each. Safe?", "Yes, 780 kg is under 850 kg limit"),
                    ("d", "Total luggage: 18.5 kg, 14.2 kg, 6.8 kg. Overall mass?", "39.5 kg")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Commercial Bakery Ingredient Batching",
                "stem": "A commercial bakery produces artisan sourdough loaves.<br>Each loaf requires <strong>450 grams of white flour</strong> and <strong>75 grams of rye flour</strong>.<br>The bakery receives a large order for <strong>80 identical loaves</strong>.<br>(a) Work out the total mass of white flour needed in kilograms.<br>(b) White flour is sold in <strong>16 kg sacks</strong>. How many sacks must the baker open?",
                "marks": 3,
                "prefix": "kg",
                "steps": [
                    ("White flour in grams: 80 × 450 g = 36,000 g", "[M1]"),
                    ("Convert grams to kilograms: 36,000 ÷ 1,000 = 36 kg", "[M1]"),
                    ("Sacks required: 36 ÷ 16 = 2.25 → 3 whole sacks", "[A1]")
                ],
                "final_answer": "(a) 36 kg | (b) 3 sacks opened",
                "reverse_check": "3 × 16 kg = 48 kg (sufficient for 36 kg with 12 kg spare).",
                "pitfall": "Dividing 36,000 by 16 without converting grams to kilograms first."
            }
        ]
    },

    # 3. CAPACITY
    "capacity": {
        "title": "Capacity & Liquid Volume Units",
        "slug": "capacity",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.18 • L2.20 • L2.24",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Metric Capacity Equivalences",
            "points": [
                "1 litre (L) = 1,000 millilitres (ml).",
                "1 centilitre (cl) = 10 millilitres (ml) = 0.01 litres.",
                "1 cubic centimetre (1 cm³) = 1 millilitre (1 ml).",
                "1 cubic metre (1 m³) = 1,000 litres.",
                "Reading measuring jugs: Count the sub-divisions between major numbered marks."
            ],
            "calc_tip": "Remember: Litres to millilitres = multiply by 1,000. Millilitres to litres = divide by 1,000."
        },
        "workout_blocks": [
            {
                "title": "Capacity Conversions",
                "instruction": "Convert between litres and millilitres:",
                "items": [
                    ("a", "2.5 litres into ml", "2,500 ml"),
                    ("b", "750 ml into litres", "0.75 L"),
                    ("c", "1,800 ml into litres", "1.8 L"),
                    ("d", "0.35 litres into ml", "350 ml"),
                    ("e", "50 ml into litres", "0.05 L"),
                    ("f", "4.2 litres into ml", "4,200 ml")
                ]
            },
            {
                "title": "Portions and Dilution Rates",
                "instruction": "Calculate liquid servings and doses:",
                "items": [
                    ("a", "A 2-litre bottle of cordial. Serving size is 250 ml. How many servings?", "8 servings (2,000 ÷ 250)"),
                    ("b", "A medical liquid dose is 15 ml, taken 3 times a day. Total ml per day?", "45 ml"),
                    ("c", "Dilute disinfectant 1 part concentrate to 9 parts water. For 100 ml concentrate, how much water?", "900 ml"),
                    ("d", "A water dispenser holds 15 litres. 40 cups of 200 ml are drawn. Water left?", "7 litres (15 - 8 L)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Medical Diagnostics Reagent Preparation",
                "stem": "A clinical laboratory technician prepares liquid disinfectant for laboratory workbenches.<br>The manufacturer states the concentrate must be diluted with water in the ratio <strong>1 : 19</strong> (1 part chemical to 19 parts water).<br>The technician needs to make a total of <strong>5 litres (5,000 ml)</strong> of diluted disinfectant solution.<br>Work out the exact volume of chemical concentrate in millilitres (ml) required.",
                "marks": 3,
                "prefix": "ml",
                "steps": [
                    ("Total parts: 1 + 19 = 20 parts", "[M1]"),
                    ("Value of one part: 5,000 ml ÷ 20 = 250 ml", "[M1]"),
                    ("Concentrate volume (1 part) = 250 ml", "[A1]")
                ],
                "final_answer": "250 ml chemical concentrate (and 4,750 ml water)",
                "reverse_check": "250 + (19 × 250) = 250 + 4,750 = 5,000 ml = 5 L.",
                "pitfall": "Dividing 5,000 by 19 instead of the total number of parts (20)."
            }
        ]
    },

    # 4. DENSITY
    "density": {
        "title": "Density & Compound Units",
        "slug": "density",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L2.19",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Density Triangle & Formulas",
            "points": [
                "Density = Mass ÷ Volume (D = M ÷ V). Typical units: g/cm³ or kg/m³.",
                "Mass = Density × Volume (M = D × V).",
                "Volume = Mass ÷ Density (V = M ÷ D).",
                "Check unit compatibility: if volume is in cm³, mass must be in grams (g); if volume is in m³, mass must be in kg.",
                "Compound units always tell you the formula: g/cm³ means grams DIVIDED by cm³."
            ],
            "calc_tip": "Cover the letter you want in the DMV formula triangle: Mass is on top, Density and Volume on the bottom."
        },
        "workout_blocks": [
            {
                "title": "Calculating Density (Mass ÷ Volume)",
                "instruction": "Work out the density of each material:",
                "items": [
                    ("a", "Mass = 120 g, Volume = 40 cm³", "3 g/cm³ (120 ÷ 40)"),
                    ("b", "Mass = 450 g, Volume = 50 cm³", "9 g/cm³ (450 ÷ 50)"),
                    ("c", "Mass = 2,400 kg, Volume = 3 m³", "800 kg/m³"),
                    ("d", "Mass = 85 g, Volume = 100 cm³", "0.85 g/cm³"),
                    ("e", "Mass = 1,350 kg, Volume = 0.5 m³", "2,700 kg/m³")
                ]
            },
            {
                "title": "Calculating Mass and Volume",
                "instruction": "Use Mass = Density × Volume or Volume = Mass ÷ Density:",
                "items": [
                    ("a", "Density = 2.5 g/cm³, Volume = 60 cm³. Find Mass.", "150 g (2.5 × 60)"),
                    ("b", "Density = 8 g/cm³, Volume = 25 cm³. Find Mass.", "200 g (8 × 25)"),
                    ("c", "Density = 0.8 g/cm³, Mass = 400 g. Find Volume.", "500 cm³ (400 ÷ 0.8)"),
                    ("d", "Density = 1.2 kg/m³, Mass = 60 kg. Find Volume.", "50 m³ (60 ÷ 1.2)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Estates Construction Concrete Loading",
                "stem": "An estates construction team casts a solid rectangular concrete pillar.<br>The dimensions of the pillar are: <strong>0.4 metres wide, 0.4 metres long, and 2.5 metres high</strong>.<br>The density of cured concrete is <strong>2,400 kg/m³</strong>.<br>A site crane has a maximum safe working lifting capacity of <strong>1,000 kg</strong>.<br>Can the crane safely lift the concrete pillar? You must show full working out.",
                "marks": 4,
                "prefix": "kg",
                "steps": [
                    ("Calculate pillar volume: 0.4 × 0.4 × 2.5 = 0.4 m³", "[M1]"),
                    ("Calculate total mass: Mass = Density × Volume = 2,400 kg/m³ × 0.4 m³ = 960 kg", "[M1]"),
                    ("Compare against crane limit: 960 kg < 1,000 kg", "[M1]"),
                    ("State definitive conclusion: Yes, safe to lift (pillar is 40 kg under limit)", "[A1]")
                ],
                "final_answer": "Yes, safe (Pillar mass = 960 kg, within 1,000 kg capacity)",
                "reverse_check": "960 ÷ 2,400 = 0.4 m³; 0.4 ÷ 2.5 ÷ 0.4 = 0.4 m.",
                "pitfall": "Forgetting to calculate the volume first before multiplying by density."
            }
        ]
    },

    # 5. USING LENGTH, AREA AND VOLUME IN CALCULATIONS
    "using-length-area-and-volume-in-calculations": {
        "title": "Multi-Step Spatial Calculations: Area & Volume",
        "slug": "using-length-area-and-volume-in-calculations",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.24 • L2.19 • L2.20",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Integrating Length, Area & Volume",
            "points": [
                "Perimeter (1D): Distance around outside border (metres, cm). Used for skirting, fencing, piping.",
                "Area (2D): Surface covering (m², cm²). Used for paint, tiles, turf, vinyl.",
                "Volume (3D): Internal capacity or solid space (m³, cm³). Used for liquids, soil, concrete, air exchange.",
                "Always check units: 1 m² = 10,000 cm²; 1 m³ = 1,000,000 cm³ = 1,000 litres.",
                "Multi-step problems often require: Step 1 (Measure) → Step 2 (Material units required) → Step 3 (Pack quantities) → Step 4 (Total cost)."
            ],
            "calc_tip": "Break multi-step questions into distinct numbered steps with explicit labels."
        },
        "workout_blocks": [
            {
                "title": "Distinguishing Metric Dimension Units",
                "instruction": "State whether each measurement is Length, Area, or Volume:",
                "items": [
                    ("a", "The skirting board around a room", "Length (m)"),
                    ("b", "The carpet needed to cover an office floor", "Area (m²)"),
                    ("c", "The water needed to fill a swimming pool", "Volume (m³ or litres)"),
                    ("d", "The fencing around a community garden", "Length (m)"),
                    ("e", "The grass seed needed for a lawn", "Area (m²)"),
                    ("f", "The air flow ventilation in a medical clinic", "Volume (m³/hour)")
                ]
            },
            {
                "title": "Material Pack Coverage Calculations",
                "instruction": "Work out the number of packs required (round UP for partial packs):",
                "items": [
                    ("a", "Floor area = 28 m². Tile packs cover 2.5 m² each. Packs needed?", "12 packs (28 ÷ 2.5 = 11.2)"),
                    ("b", "Wall area = 45 m². Paint tins cover 12 m² each. Tins needed?", "4 tins (45 ÷ 12 = 3.75)"),
                    ("c", "Trench length = 32 m. Drainage pipe sold in 3 m lengths. Pipes needed?", "11 pipes (32 ÷ 3 = 10.67)"),
                    ("d", "Planter volume = 1.2 m³. Compost sold in 60-litre bags (0.06 m³). Bags?", "20 bags (1.2 ÷ 0.06)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Estates Refurbishment Consultation Room",
                "stem": "An estates team refits a clinical consultation room.<br>The room is rectangular, measuring <strong>5 metres long by 4 metres wide with a ceiling height of 2.6 metres</strong>.<br>The team carries out two jobs:<br>• Job 1: Install vinyl flooring at <strong>£18.50 per m²</strong>.<br>• Job 2: Paint the four walls. The total wall area (after subtracting doors and windows) is <strong>42 m²</strong>. Paint tins cost <strong>£22.00 each</strong> and cover <strong>10 m² per tin</strong>.<br>Work out the total cost for the flooring and paint.",
                "marks": 4,
                "prefix": "£",
                "steps": [
                    ("Floor area: 5 × 4 = 20 m²", "[M1]"),
                    ("Flooring cost: 20 m² × £18.50 = £370.00", "[M1]"),
                    ("Paint tins needed: 42 ÷ 10 = 4.2 → 5 whole tins; Paint cost: 5 × £22.00 = £110.00", "[M1]"),
                    ("Combined total cost: £370.00 + £110.00 = £480.00", "[A1]")
                ],
                "final_answer": "£480.00 total cost",
                "reverse_check": "£480 - £370 = £110; £110 ÷ £22 = 5 tins.",
                "pitfall": "Rounding paint down to 4 tins (leaving 2 m² of wall unpainted) or using the ceiling height in the floor area."
            }
        ]
    },

    # 6. 3D SHAPE BASICS
    "3d-shape-basics": {
        "title": "3D Shape Basics: Cubes, Spheres & Cones",
        "slug": "3d-shape-basics",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: E3.6 • L1.21 • L2.21",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Identifying 3D Solids & Everyday Examples",
            "points": [
                "Cube: 6 square faces of equal size, 12 edges, 8 vertices (e.g. dice, storage box).",
                "Cuboid (rectangular prism): 6 rectangular faces, 12 edges, 8 vertices (e.g. brick, shoe box, book).",
                "Cylinder: 2 flat circular faces and 1 curved surface (e.g. soup can, pipe, battery).",
                "Sphere: 1 continuous curved surface, 0 edges, 0 vertices (e.g. ball, globe).",
                "Cone: 1 flat circular base, 1 curved surface tapering to an apex vertex (e.g. traffic cone, funnel)."
            ],
            "calc_tip": "Remember: A face is a flat surface, an edge is where two faces meet, and a vertex (corner) is where edges meet."
        },
        "workout_blocks": [
            {
                "title": "Naming 3D Solids from Real-World Objects",
                "instruction": "Name the 3D solid that best describes each object:",
                "items": [
                    ("a", "A tin of baked beans", "Cylinder"),
                    ("b", "A cardboard shoe box", "Cuboid"),
                    ("c", "A standard playing dice", "Cube"),
                    ("d", "An orange or football", "Sphere"),
                    ("e", "A road safety traffic pylon", "Cone"),
                    ("f", "A Toblerone chocolate box", "Triangular prism")
                ]
            },
            {
                "title": "Properties of 3D Solids",
                "instruction": "State the number of faces, edges, and vertices:",
                "items": [
                    ("a", "Number of faces on a cuboid", "6 faces"),
                    ("b", "Number of vertices on a cube", "8 vertices"),
                    ("c", "Number of edges on a cuboid", "12 edges"),
                    ("d", "Number of circular faces on a cylinder", "2 faces"),
                    ("e", "Number of vertices on a sphere", "0 vertices"),
                    ("f", "Number of flat faces on a square-based pyramid", "5 faces (1 square base + 4 triangles)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Warehouse Packaging & Space Efficiency",
                "stem": "A shipping depot packages medical supplies into two types of containers:<br>Container A is a <strong>cube with sides of 30 cm</strong>.<br>Container B is a <strong>cuboid measuring 40 cm long, 30 cm wide, and 20 cm high</strong>.<br>(a) Calculate the volume of Container A in cm³.<br>(b) Calculate the volume of Container B in cm³.<br>(c) Which container has the larger internal capacity, and by how much?",
                "marks": 3,
                "prefix": "cm³",
                "steps": [
                    ("Container A volume: 30 × 30 × 30 = 27,000 cm³", "[M1]"),
                    ("Container B volume: 40 × 30 × 20 = 24,000 cm³", "[M1]"),
                    ("Compare and find difference: 27,000 - 24,000 = 3,000 cm³", "[A1]")
                ],
                "final_answer": "Container A has greater capacity by 3,000 cm³",
                "reverse_check": "27,000 - 3,000 = 24,000 cm³.",
                "pitfall": "Adding dimensions instead of multiplying to find volume (30 + 30 + 30 = 90)."
            }
        ]
    },

    # 7. 3D SHAPES
    "3d-shapes": {
        "title": "3D Solids: Faces, Edges & Vertices",
        "slug": "3d-shapes",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.21 • L2.21",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Euler's Formula & Prisms vs Pyramids",
            "points": [
                "Prism: A 3D solid with the same 2D cross-section along its entire length (e.g. triangular prism, hexagonal prism).",
                "Pyramid: Has a polygon base with triangular faces meeting at a single top point (apex).",
                "Euler's Formula for polyhedra: Faces + Vertices - Edges = 2 (F + V - E = 2).",
                "Prism edge rule: Edges = 3 × (number of sides of cross-section); Vertices = 2 × sides; Faces = sides + 2."
            ],
            "calc_tip": "To count faces of a prism: count the 2 identical end faces, then add the rectangular sides around the perimeter."
        },
        "workout_blocks": [
            {
                "title": "Prisms and Pyramids Audit",
                "instruction": "Complete the geometric properties for each 3D shape:",
                "items": [
                    ("a", "Triangular prism: Faces, Vertices, Edges", "5 faces, 6 vertices, 9 edges"),
                    ("b", "Square-based pyramid: Faces, Vertices, Edges", "5 faces, 5 vertices, 8 edges"),
                    ("c", "Hexagonal prism: Faces, Vertices, Edges", "8 faces, 12 vertices, 18 edges"),
                    ("d", "Tetrahedron (triangular pyramid): Faces, Vertices, Edges", "4 faces, 4 vertices, 6 edges"),
                    ("e", "Verify Euler's rule for a cube: F + V - E", "6 + 8 - 12 = 2 (Verified)")
                ]
            },
            {
                "title": "Cross-Sections of 3D Solids",
                "instruction": "State the 2D shape produced by a perpendicular cross-section cut:",
                "items": [
                    ("a", "Horizontal slice through a vertical cylinder", "Circle"),
                    ("b", "Slice parallel to the base of a square-based pyramid", "Square"),
                    ("c", "Vertical slice parallel to the end face of a cuboid", "Rectangle"),
                    ("d", "Vertical slice through the apex of a cone", "Triangle")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Industrial Fabrication Framework Design",
                "stem": "An engineering metalworker fabricates an open structural support frame in the shape of a <strong>triangular prism</strong>.<br>The two triangular ends are equilateral triangles with sides of <strong>60 cm</strong>. The three connecting horizontal steel beams are each <strong>1.5 metres (150 cm)</strong> long.<br>Steel strut rod is sold in <strong>3-metre lengths</strong> at <strong>£16.00 per length</strong>.<br>(a) How many steel edges make up the frame in total?<br>(b) Work out the total length of steel needed in metres.<br>(c) How many 3-metre lengths of steel must be ordered?",
                "marks": 3,
                "prefix": "m",
                "steps": [
                    ("Count edges: 3 + 3 + 3 = 9 edges", "[M1]"),
                    ("Calculate total steel length: (6 × 0.6 m) + (3 × 1.5 m) = 3.6 m + 4.5 m = 8.1 metres", "[M1]"),
                    ("Lengths required: 8.1 ÷ 3 = 2.7 → 3 lengths needed", "[A1]")
                ],
                "final_answer": "(a) 9 edges | (b) 8.1 metres | (c) 3 lengths",
                "reverse_check": "3 × 3 m = 9 m (covers 8.1 m).",
                "pitfall": "Counting only 6 edges instead of 9 edges on a triangular prism."
            }
        ]
    },

    # 8. NETS
    "nets": {
        "title": "3D Nets, Folding Geometry & Packaging Layout",
        "slug": "nets",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.22 • L1.24 • L2.21",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Identifying Valid Nets & Surface Fold Lines",
            "points": [
                "A net is a 2D pattern that can be cut out and folded along dashed lines to form a closed 3D solid.",
                "A valid cube net has EXACTLY 6 squares. Opposite faces can never share a common folding edge.",
                "The classic 'T' shape and 'cross' shape are standard valid cube nets.",
                "A cuboid net consists of 3 pairs of matching rectangular faces (Top/Bottom, Front/Back, Left/Right).",
                "A cylinder net consists of 1 rectangle (curved surface) and 2 circles (top and bottom lids). The length of the rectangle equals the circumference of the circle (C = πd)."
            ],
            "calc_tip": "Mentally fold adjacent faces 90 degrees to check if two flaps overlap or if a side is left open."
        },
        "workout_blocks": [
            {
                "title": "Valid vs Invalid Nets",
                "instruction": "State whether each description forms a valid closed 3D solid:",
                "items": [
                    ("a", "6 squares in a single straight row", "Invalid (faces overlap when folded)"),
                    ("b", "4 squares in a line with 1 square on the top row and 1 on the bottom row (Latin cross)", "Valid cube net"),
                    ("c", "A square with 4 triangles attached to each of its 4 edges", "Valid square-based pyramid net"),
                    ("d", "A rectangle with 2 identical circles attached to opposite sides", "Valid cylinder net"),
                    ("e", "2 equilateral triangles and 3 rectangles", "Valid triangular prism net"),
                    ("f", "5 squares joined in a cross shape", "Invalid for cube (needs 6 squares; makes an open box)")
                ]
            },
            {
                "title": "Surface Area from Nets",
                "instruction": "Calculate the total surface area by summing the areas of the net faces:",
                "suffix": "cm²",
                "items": [
                    ("a", "Cube net with 6 square faces of 5 cm × 5 cm", "150 cm² (6 × 25)"),
                    ("b", "Cube net with 6 square faces of 8 cm × 8 cm", "384 cm² (6 × 64)"),
                    ("c", "Cuboid net: two 6×4 cm, two 6×3 cm, two 4×3 cm", "108 cm² (48 + 36 + 24)"),
                    ("d", "Cuboid net: two 10×5 cm, two 10×2 cm, two 5×2 cm", "160 cm² (100 + 40 + 20)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Commercial Packaging Die-Cut Printing",
                "stem": "A packaging company prints flat cardboard nets for shipping medicine bottles.<br>The folded box is a cuboid measuring <strong>12 cm high, 8 cm wide, and 5 cm deep</strong>.<br>The manufacturer adds an extra <strong>10% card allowance</strong> around the edges for folding glue tabs and overlapping seams.<br>(a) Calculate the total surface area of the 6 box faces in cm².<br>(b) Work out the total cardboard area needed per box, including the 10% glue tab allowance.",
                "marks": 3,
                "prefix": "cm²",
                "steps": [
                    ("Front/Back faces: 2 × (12 × 8) = 192 cm²; Side faces: 2 × (12 × 5) = 120 cm²; Top/Bottom faces: 2 × (8 × 5) = 80 cm²", "[M1]"),
                    ("Total surface area: 192 + 120 + 80 = 392 cm²", "[M1]"),
                    ("Add 10% allowance: 392 × 1.10 = 431.2 cm²", "[A1]")
                ],
                "final_answer": "(a) 392 cm² surface area | (b) 431.2 cm² card per box",
                "reverse_check": "431.2 ÷ 1.10 = 392 cm².",
                "pitfall": "Calculating only 3 faces instead of all 6 faces of the cuboid net."
            }
        ]
    },

    # 9. ANGLES AND BEARINGS
    "angles-and-bearings": {
        "title": "Angles, Bearings & Turn Navigation",
        "slug": "angles-and-bearings",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.25 • L2.22",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Three Golden Rules of Bearings",
            "points": [
                "Rule 1: Always measure from North (000°).",
                "Rule 2: Always measure in a CLOCKWISE direction.",
                "Rule 3: Always write bearings as THREE DIGITS (e.g. 45° must be written as 045°, 9° as 009°).",
                "Back Bearing (reverse direction): If bearing is < 180°, add 180°. If bearing is ≥ 180°, subtract 180°."
            ],
            "calc_tip": "Align the 0° line of your circular protractor directly with the North arrow."
        },
        "workout_blocks": [
            {
                "title": "Writing 3-Figure Bearings",
                "instruction": "Express each direction as a standard 3-figure bearing:",
                "items": [
                    ("a", "Due North", "000° (or 360°)"),
                    ("b", "Due East", "090°"),
                    ("c", "Due South", "180°"),
                    ("d", "Due West", "270°"),
                    ("e", "North-East (halfway between N and E)", "045°"),
                    ("f", "South-East (halfway between S and E)", "135°"),
                    ("g", "South-West (halfway between S and W)", "225°"),
                    ("h", "North-West (halfway between N and W)", "315°")
                ]
            },
            {
                "title": "Calculating Back Bearings",
                "instruction": "Calculate the return (back) bearing by adding or subtracting 180°:",
                "items": [
                    ("a", "Outward bearing: 060°. Return bearing?", "240° (60 + 180)"),
                    ("b", "Outward bearing: 110°. Return bearing?", "290° (110 + 180)"),
                    ("c", "Outward bearing: 220°. Return bearing?", "040° (220 - 180)"),
                    ("d", "Outward bearing: 315°. Return bearing?", "135° (315 - 180)"),
                    ("e", "Outward bearing: 015°. Return bearing?", "195° (15 + 180)"),
                    ("f", "Outward bearing: 285°. Return bearing?", "105° (285 - 180)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Maritime Coastguard Navigation",
                "stem": "A search-and-rescue patrol vessel departs from harbour harbour station H.<br>The vessel navigates towards an offshore lighthouse L on a bearing of <strong>074°</strong>.<br>After completing the inspection, the vessel turns around to return straight back to harbour H.<br>State the 3-figure bearing the navigator must follow to return from L to H.",
                "marks": 2,
                "prefix": "",
                "steps": [
                    ("Check if bearing is less than 180°: 74° < 180°", "[M1]"),
                    ("Calculate back bearing: 074° + 180° = 254°", "[A1]")
                ],
                "final_answer": "254°",
                "reverse_check": "254° - 180° = 074°.",
                "pitfall": "Writing 74° or measuring counter-clockwise from North."
            }
        ]
    },

    # 10. ANGLES IN 2D SHAPES
    "angles-in-2d-shapes": {
        "title": "Angles in Triangles, Quadrilaterals & Polygons",
        "slug": "angles-in-2d-shapes",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.25 • L2.22",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Angle Sum Rules & Properties",
            "points": [
                "Angles on a straight line add up to 180°.",
                "Angles around a point add up to 360°.",
                "Angles in any triangle add up to 180°.",
                "Equilateral triangle: All 3 angles are 60°; Isosceles triangle: 2 equal angles opposite equal sides.",
                "Angles in any quadrilateral (4-sided shape) add up to 360°."
            ],
            "calc_tip": "To find an unknown angle in a triangle: add the known angles together, then subtract from 180°."
        },
        "workout_blocks": [
            {
                "title": "Missing Angles in Triangles",
                "instruction": "Work out the missing angle x in each triangle (sum = 180°):",
                "suffix": "°",
                "items": [
                    ("a", "Angles: 65°, 55°, x°", "60° (180 - 120)"),
                    ("b", "Right-angled triangle: 90°, 38°, x°", "52° (180 - 128)"),
                    ("c", "Isosceles triangle with base angles of 42°. Top angle x°?", "96° (180 - 84)"),
                    ("d", "Isosceles triangle with top angle 70°. Base angles x°?", "55° ((180 - 70) ÷ 2)"),
                    ("e", "Right-angled isosceles triangle: 90°, x°, x°", "45° each (90 ÷ 2)")
                ]
            },
            {
                "title": "Missing Angles in Quadrilaterals & Straight Lines",
                "instruction": "Calculate the unknown angle:",
                "suffix": "°",
                "items": [
                    ("a", "Straight line: 124° and x°", "56° (180 - 124)"),
                    ("b", "Straight line: 45°, 70°, and x°", "65° (180 - 115)"),
                    ("c", "Around a point: 110°, 130°, and x°", "120° (360 - 240)"),
                    ("d", "Quadrilateral: 100°, 85°, 75°, x°", "100° (360 - 260)"),
                    ("e", "Parallelogram: opposite angle is 115°. Adjacent angle x°?", "65° (180 - 115)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Carpentry Roof Truss Fabrication",
                "stem": "A carpenter builds a timber A-frame roof truss in the shape of a symmetrical isosceles triangle.<br>The apex pitch angle at the top peak is measured as <strong>68°</strong>.<br>The two base angles where the rafters meet the ceiling joist are identical.<br>Calculate the size of each base angle.",
                "marks": 2,
                "prefix": "",
                "steps": [
                    ("Subtract apex angle from triangle sum: 180° - 68° = 112°", "[M1]"),
                    ("Divide equally between the two base angles: 112° ÷ 2 = 56°", "[A1]")
                ],
                "final_answer": "56° each",
                "reverse_check": "56° + 56° + 68° = 180°.",
                "pitfall": "Dividing 68 by 2 instead of subtracting from 180 first."
            }
        ]
    },

    # 11. COORDINATES
    "coordinates": {
        "title": "Coordinates: Positive & Four Quadrants",
        "slug": "coordinates",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: E3.7 • L1.26 • L2.25",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Grid Axes & Coordinate Notation",
            "points": [
                "Coordinates are written as (x, y) inside brackets separated by a comma.",
                "The first number is the X-coordinate (horizontal axis: left or right).",
                "The second number is the Y-coordinate (vertical axis: up or down).",
                "Golden rule: 'Along the corridor, then up (or down) the stairs.'",
                "The origin is the intersection point (0, 0)."
            ],
            "calc_tip": "If plotting (-3, 4): start at (0,0), move 3 units left, then 4 units up."
        },
        "workout_blocks": [
            {
                "title": "First Quadrant Positive Coordinates",
                "instruction": "Identify the coordinates or state the movement from (0,0):",
                "items": [
                    ("a", "From (0,0), move 4 units right and 6 units up", "(4, 6)"),
                    ("b", "From (0,0), move 7 units right and 2 units up", "(7, 2)"),
                    ("c", "From (0,0), move 5 units right and 0 units up", "(5, 0)"),
                    ("d", "From (0,0), move 0 units right and 8 units up", "(0, 8)")
                ]
            },
            {
                "title": "Four Quadrants & Negative Coordinates",
                "instruction": "Determine the coordinate pair:",
                "items": [
                    ("a", "Move 3 units left and 5 units up from origin", "(-3, 5)"),
                    ("b", "Move 4 units left and 6 units down from origin", "(-4, -6)"),
                    ("c", "Move 2 units right and 7 units down from origin", "(2, -7)"),
                    ("d", "Midpoint between (2, 4) and (6, 4)", "(4, 4)"),
                    ("e", "Midpoint between (-2, 1) and (4, 1)", "(1, 1)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Warehouse Robotic Automated Guided Vehicle (AGV)",
                "stem": "An automated robotic picker in a fulfilment depot operates on a coordinate grid system.<br>The robot starts at charging station C located at <strong>(2, -3)</strong>.<br>It receives an instruction to move <strong>5 units North (positive y)</strong> and <strong>4 units West (negative x)</strong> to pick a batch of clinical supplies.<br>Work out the new coordinates of the robot.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Apply horizontal movement: West means subtract 4 from x: 2 - 4 = -2", "[M1]"),
                    ("Apply vertical movement: North means add 5 to y: -3 + 5 = +2", "[M1]"),
                    ("Write combined coordinate pair inside brackets: (-2, 2)", "[A1]")
                ],
                "final_answer": "(-2, 2)",
                "reverse_check": "-2 + 4 = 2; 2 - 5 = -3 → returns to (2, -3).",
                "pitfall": "Swapping the x and y adjustments or adding instead of subtracting for West."
            }
        ]
    },

    # 12. MOVEMENT AND DIRECTION
    "movement-and-direction": {
        "title": "Movement, Direction & Compass Bearings",
        "slug": "movement-and-direction",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: E3.7 • L1.25",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Compass Points & Rotational Turns",
            "points": [
                "4 cardinal directions: North (N), East (E), South (S), West (W).",
                "4 intercardinal directions: North-East (NE), South-East (SE), South-West (SW), North-West (NW).",
                "Angles between compass points: 90° between adjacent cardinal points (e.g. N to E is 90° clockwise).",
                "45° between cardinal and intercardinal points (e.g. N to NE is 45°).",
                "Full turn = 360°; Half turn = 180°; Quarter turn = 90°."
            ],
            "calc_tip": "Remember: Clockwise is the direction clock hands turn (rightward from 12); Anticlockwise is leftward."
        },
        "workout_blocks": [
            {
                "title": "Compass Directions and Angles of Turn",
                "instruction": "State the new direction after the described turn:",
                "items": [
                    ("a", "Facing North, turn 90° clockwise", "East"),
                    ("b", "Facing North, turn 180°", "South"),
                    ("c", "Facing East, turn 90° anticlockwise", "North"),
                    ("d", "Facing South, turn 45° clockwise", "South-West (SW)"),
                    ("e", "Facing West, turn 90° clockwise", "North"),
                    ("f", "Facing NE, turn 180°", "South-West (SW)")
                ]
            },
            {
                "title": "Grid Steps and Displacement",
                "instruction": "Calculate net displacement from starting position:",
                "items": [
                    ("a", "Walk 5 m North, then 3 m South. Net position?", "2 m North"),
                    ("b", "Walk 8 m East, then 6 m West. Net position?", "2 m East"),
                    ("c", "Walk 10 m North, turn right 90°, walk 5 m. Final direction from start?", "North-East"),
                    ("d", "Turn 270° clockwise from North. Equivalent to?", "90° anticlockwise (Facing West)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Healthcare Clinic Porter Transit Route",
                "stem": "A facilities porter delivers medical equipment along clinic corridors.<br>Starting from the main pharmacy, the porter travels <strong>40 metres East</strong> down Corridor A, turns <strong>90° clockwise</strong> and travels <strong>25 metres South</strong> down Corridor B.<br>At the end of Corridor B, the porter turns <strong>90° clockwise</strong> again and travels <strong>40 metres West</strong>.<br>Describe the porter's position relative to the starting point at the pharmacy.",
                "marks": 2,
                "prefix": "",
                "steps": [
                    ("Track horizontal movement: 40 m East followed by 40 m West cancels out to 0 m horizontal displacement", "[M1]"),
                    ("Track vertical movement: 25 m South remains", "[A1]")
                ],
                "final_answer": "25 metres directly South of the pharmacy",
                "reverse_check": "40 - 40 = 0 m; 0 m East/West, 25 m South.",
                "pitfall": "Adding all distances (40 + 25 + 40 = 105 m) instead of determining relative displacement."
            }
        ]
    },

    # 13. MAPS AND SCALE DRAWINGS
    "maps-and-scale-drawings": {
        "title": "Maps, Scale Ratios & Floor Plans",
        "slug": "maps-and-scale-drawings",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.19 • L2.21",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Scale Ratios & Measurement Conversion",
            "points": [
                "Scale ratio 1 : N means 1 unit on the drawing represents N units in real life.",
                "To find Real Life distance: Multiply drawing measurement by the scale factor (e.g. 5 cm on 1:50 plan = 5 × 50 = 250 cm = 2.5 m).",
                "To find Drawing length: Divide real-life distance by the scale factor.",
                "Grid scales (e.g. '1 square = 2 metres'): Multiply the number of squares by the stated value per square.",
                "Always convert measurements into requested final units (usually metres or kilometres)."
            ],
            "calc_tip": "Convert real-world metres into centimetres before dividing when finding drawing lengths."
        },
        "workout_blocks": [
            {
                "title": "Converting Drawing Lengths to Real Distances",
                "instruction": "Calculate the actual real-life distance in metres:",
                "items": [
                    ("a", "Scale 1 : 50. Drawing measurement = 6 cm. Real distance?", "3 m (6 × 50 = 300 cm)"),
                    ("b", "Scale 1 : 100. Drawing measurement = 8.5 cm. Real distance?", "8.5 m (8.5 × 100 = 850 cm)"),
                    ("c", "Scale 1 : 20. Drawing measurement = 14 cm. Real distance?", "2.8 m (14 × 20 = 280 cm)"),
                    ("d", "Scale 1 : 200. Drawing measurement = 4 cm. Real distance?", "8 m (4 × 200 = 800 cm)"),
                    ("e", "Scale 1 : 25,000 (map). 4 cm on map. Real distance in km?", "1 km (4 × 25,000 = 100,000 cm)")
                ]
            },
            {
                "title": "Converting Real Dimensions to Drawing Scale",
                "instruction": "Calculate the length to draw on the plan in centimetres:",
                "suffix": "cm",
                "items": [
                    ("a", "Real length = 6 metres. Scale 1 : 100. Drawing length?", "6 cm (600 ÷ 100)"),
                    ("b", "Real length = 4.5 metres. Scale 1 : 50. Drawing length?", "9 cm (450 ÷ 50)"),
                    ("c", "Real length = 1.8 metres. Scale 1 : 20. Drawing length?", "9 cm (180 ÷ 20)"),
                    ("d", "Real length = 12 metres. Scale 1 : 200. Drawing length?", "6 cm (1,200 ÷ 200)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Community Health Clinic Architectural Plan",
                "stem": "An architectural floor plan of a new consultation clinic is drawn to a scale of <strong>1 : 50</strong>.<br>On the plan, the consultation room measures <strong>9.6 cm long by 7.4 cm wide</strong>.<br>The clinic requires that all new clinical rooms have a minimum real-world floor area of at least <strong>16 square metres</strong>.<br>Does this consultation room meet the minimum space requirement? Show full working out.",
                "marks": 4,
                "prefix": "m²",
                "steps": [
                    ("Convert drawing length to real metres: 9.6 cm × 50 = 480 cm = 4.8 m", "[M1]"),
                    ("Convert drawing width to real metres: 7.4 cm × 50 = 370 cm = 3.7 m", "[M1]"),
                    ("Calculate real floor area: 4.8 m × 3.7 m = 17.76 m²", "[M1]"),
                    ("Compare against standard and conclude: Yes, 17.76 m² is greater than 16 m²", "[A1]")
                ],
                "final_answer": "Yes (Real area = 17.76 m², exceeding the 16 m² threshold)",
                "reverse_check": "17.76 m² ÷ 4.8 m = 3.7 m.",
                "pitfall": "Calculating area in cm² (9.6 × 7.4 = 71.04) and multiplying by 50 instead of 50² (2,500)."
            }
        ]
    },

    # 14. PLANS AND ELEVATIONS
    "plans-and-elevations": {
        "title": "Plans, Elevations & Front/Side Views",
        "slug": "plans-and-elevations",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.22 • L2.21",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Three Orthographic Projections",
            "points": [
                "Plan View: The view of a 3D object looking directly DOWN from above (bird's-eye view).",
                "Front Elevation: The view of the object looking straight at the FRONT face.",
                "Side Elevation: The view of the object looking straight from the LEFT or RIGHT side.",
                "All views are 2D drawings showing true heights, widths, and lengths without perspective distortion."
            ],
            "calc_tip": "The Plan view shows Length × Width; the Front view shows Length × Height; the Side view shows Width × Height."
        },
        "workout_blocks": [
            {
                "title": "Identifying Views of 3D Objects",
                "instruction": "State which 2D view (Plan, Front Elevation, or Side Elevation) is described:",
                "items": [
                    ("a", "Looking directly down from the ceiling at a table", "Plan view"),
                    ("b", "Looking directly at the front door of a house from the street", "Front elevation"),
                    ("c", "Looking at the gable end wall of a building from the driveway", "Side elevation"),
                    ("d", "Looking directly down at a cylinder standing on its base", "Plan view (Circle)"),
                    ("e", "Looking directly at the side of a standing cylinder", "Side elevation (Rectangle)")
                ]
            },
            {
                "title": "Dimensions from Elevations",
                "instruction": "State the dimensions shown on each view of a box (Length 8m, Width 5m, Height 3m):",
                "items": [
                    ("a", "Dimensions shown on the Plan view", "8 m by 5 m"),
                    ("b", "Dimensions shown on the Front elevation", "8 m by 3 m"),
                    ("c", "Dimensions shown on the Side elevation", "5 m by 3 m"),
                    ("d", "Which view shows the total building height?", "Front and Side elevations")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Estates Facilities Storage Shed Design",
                "stem": "An estates team designs a timber maintenance equipment store.<br>The store has a rectangular base measuring <strong>4 metres wide by 6 metres long</strong>.<br>The front and back vertical walls are <strong>2.2 metres high</strong>, and the roof slopes up to a central ridge line of <strong>3.0 metres high</strong> running lengthwise.<br>(a) What 2D geometric shape is the side elevation view?<br>(b) Work out the total wall area of the front elevation (6 m long by 2.2 m high).",
                "marks": 2,
                "prefix": "",
                "steps": [
                    ("Identify side elevation shape: A vertical rectangle topped by a triangular gable (a pentagon / house shape)", "[M1]"),
                    ("Calculate front elevation area: 6 m × 2.2 m = 13.2 m²", "[A1]")
                ],
                "final_answer": "(a) Pentagon / house shape (rectangle + triangle) | (b) 13.2 m²",
                "reverse_check": "13.2 ÷ 6 = 2.2 m.",
                "pitfall": "Assuming the side elevation is a simple rectangle and ignoring the triangular gable roof."
            }
        ]
    },

    # 15. SYMMETRY AND 2D SHAPES
    "symmetry-and-2d-shapes": {
        "title": "Symmetry & 2D Shapes",
        "slug": "symmetry-and-2d-shapes",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: E3.6 • L1.20 • L2.21",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Line Symmetry & Rotational Symmetry",
            "points": [
                "Line (Reflective) Symmetry: A mirror line where one half folds exactly onto the other half.",
                "Rotational Symmetry: The number of times a shape looks identical to its starting position during a full 360° turn.",
                "Regular polygons: A regular polygon with n sides has n lines of symmetry and rotational symmetry of order n.",
                "Square: 4 lines of symmetry, rotational symmetry order 4.",
                "Rectangle (non-square): 2 lines of symmetry, rotational symmetry order 2. (Diagonals are NOT lines of symmetry!)."
            ],
            "calc_tip": "If a shape only looks the same after a complete 360° turn, its rotational symmetry order is 1 (no rotational symmetry)."
        },
        "workout_blocks": [
            {
                "title": "Lines of Symmetry in 2D Polygons",
                "instruction": "State the number of lines of reflective symmetry:",
                "items": [
                    ("a", "Equilateral triangle", "3 lines"),
                    ("b", "Isosceles triangle", "1 line"),
                    ("c", "Scalene triangle", "0 lines"),
                    ("d", "Square", "4 lines"),
                    ("e", "Rectangle", "2 lines"),
                    ("f", "Regular pentagon", "5 lines"),
                    ("g", "Regular hexagon", "6 lines"),
                    ("h", "Circle", "Infinite lines")
                ]
            },
            {
                "title": "Order of Rotational Symmetry",
                "instruction": "State the order of rotational symmetry for each shape:",
                "items": [
                    ("a", "Square", "Order 4"),
                    ("b", "Rectangle", "Order 2"),
                    ("c", "Equilateral triangle", "Order 3"),
                    ("d", "Parallelogram", "Order 2"),
                    ("e", "Rhombus", "Order 2"),
                    ("f", "Isosceles triangle", "Order 1")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Commercial Clinic Safety Signage",
                "stem": "A facilities compliance officer reviews emergency road and safety signage around a clinic estate.<br>A priority warning sign is manufactured as a <strong>regular octagon</strong>.<br>(a) State the number of lines of reflective symmetry on the octagonal sign.<br>(b) State the order of rotational symmetry of the sign.<br>(c) What is the angle of rotational symmetry (the minimum turn angle before the sign looks identical)?",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Regular octagon has 8 equal sides and 8 lines of symmetry", "[M1]"),
                    ("Rotational symmetry order is 8", "[M1]"),
                    ("Angle of rotation: 360° ÷ 8 = 45°", "[A1]")
                ],
                "final_answer": "(a) 8 lines of symmetry | (b) Order 8 | (c) 45° turn",
                "reverse_check": "45° × 8 = 360°.",
                "pitfall": "Stating that a regular octagon has only 4 lines of symmetry instead of 8."
            }
        ]
    }
}

if __name__ == "__main__":
    print(f"Loaded {len(MATHS_BATCH2_PART2_WORKOUTS)} topics in authentic_workouts_maths_batch2_part2.py")
