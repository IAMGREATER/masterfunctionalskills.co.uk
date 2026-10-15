#!/usr/bin/env python3
import json

TOPICS_DOMAIN4 = [
    {
        "filename": "functional-skills-surface-area.html",
        "clean_topic": "Surface Area of Prisms & Cylinders",
        "intro_lead": "Calculate the total surface area of cuboids, triangular prisms, and cylinders to determine painting, plastering, sheet metal, and packaging material requirements.",
        "next_file": "functional-skills-2d-shapes.html",
        "next_name": "2D Shapes",
        "spec_points": [
            ("L2.24", "Calculate surface area of rectangular and triangular prisms and cylinders in vocational contexts.")
        ],
        "golden_rules": [
            {
                "icon": "fa-cube",
                "title": "Golden Rule 1: Surface Area is the Sum of ALL Outside Faces",
                "desc": "Surface area is 2D area (measured in cm² or m²), NOT 3D volume. For a cuboid: calculate Top & Bottom (2 × lw), Front & Back (2 × lh), and Left & Right (2 × wh), then sum all six faces.",
                "badge": "Cuboid SA = 2(lw + lh + wh)"
            },
            {
                "icon": "fa-cylinder",
                "title": "Golden Rule 2: Cylinder Surface Area: Two Circles Plus One Rectangle",
                "desc": "The curved surface unrolls into a rectangle whose width is the circumference (2πr) and height is h: Curved SA = 2πrh. Add two circular ends: Total SA = 2πrh + 2πr².",
                "badge": "Cylinder SA = 2πrh + 2πr²"
            }
        ],
        "skills": [
            {
                "title": "Cuboid 6-Face Method vs Formula",
                "summary": "Step-by-step breakdown of faces to prevent missed sides.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Top &amp; Bottom:</strong> 2 × (Length × Width)</li>
                    <li><strong>Front &amp; Back:</strong> 2 × (Length × Height)</li>
                    <li><strong>Left &amp; Right Ends:</strong> 2 × (Width × Height)</li>
                    <li><strong>Total Surface Area:</strong> Sum of all 6 faces in m² or cm².</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Hospital Waste Disposal Steel Container Enclosure Painting",
                "marks": "3 Marks (Pearson Edexcel Level 2)",
                "context": "Facility Maintenance Painting",
                "question": "A facilities maintenance team must apply anti-rust paint to all <strong>5 external faces</strong> (four sides and top; no base) of a steel container unit measuring <strong>3 m long, 2 m wide, and 1.8 m high</strong>.<br>(a) Calculate the total surface area to be painted in m².<br>(b) Paint covers 8 m² per litre. How many 1-litre tins must be purchased?",
                "steps": [
                    ("Step 1", "Calculate the area of the top face (no base)", "Top = 3 m × 2 m = 6 m².", "M1: Top face area"),
                    ("Step 2", "Calculate the 4 vertical side walls", "Front & Back = 2 × (3 m × 1.8 m) = 2 × 5.4 = 10.8 m².<br>Left & Right = 2 × (2 m × 1.8 m) = 2 × 3.6 = 7.2 m².<br>Total Walls = 10.8 + 7.2 = 18 m².", "M1: Four wall faces calculation"),
                    ("Step 3", "Sum 5 faces and calculate paint tins", "Total SA = 6 m² (top) + 18 m² (walls) = 24 m².<br>Tins required = 24 ÷ 8 = exactly 3 tins.", "A1: Accurate surface area (24 m²) and tin count (3 tins)")
                ],
                "final_answer": "(a) Surface Area = 24 m² | (b) 3 tins of paint needed",
                "tutor_tip": "Notice the question says 5 EXTERNAL FACES (no base). If you calculated all 6 faces (= 30 m²), you would lose marks."
            }
        ],
        "examiner_traps": [
            {
                "title": "Calculating Volume Instead of Surface Area",
                "desc": "Doing 3 × 2 × 1.8 = 10.8 m³ calculates capacity, not surface area. Area is always in square units (m²).",
                "fix": "Highlight the word 'SURFACE' in the question."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "Calculate the total surface area of a closed cardboard shipping box measuring 40 cm by 30 cm by 20 cm.",
                "solution_steps": "1. Faces: 2(40×30) + 2(40×20) + 2(30×20).<br>2. 2(1200) + 2(800) + 2(600) = 2400 + 1600 + 1200 = 5,200 cm².",
                "correct_answer": "5,200 cm²",
                "tutor_tip": "Sum the three pairs of matching faces."
            }
        ]
    },
    {
        "filename": "functional-skills-2d-shapes.html",
        "clean_topic": "2D Shapes & Polygons",
        "intro_lead": "Identify and classify regular and irregular 2D polygons (triangles, quadrilaterals, pentagons, hexagons), identify lines of symmetry, and apply properties of parallel and perpendicular lines.",
        "next_file": "functional-skills-3d-shapes.html",
        "next_name": "3D Shapes",
        "spec_points": [
            ("L1.20 / L2.22", "Recognise and use 2D representations of 2D and 3D shapes."),
            ("L1.21", "Understand and use properties of regular and irregular polygons, including symmetry and angles.")
        ],
        "golden_rules": [
            {
                "icon": "fa-shapes",
                "title": "Golden Rule 1: Regular Polygons Have Equal Sides AND Equal Angles",
                "desc": "A polygon is 'regular' only if ALL sides are of equal length and ALL interior angles are identical (e.g. an equilateral triangle or a regular hexagon).",
                "badge": "Regular = Equal Sides + Equal Angles"
            },
            {
                "icon": "fa-arrows-split-up-and-left",
                "title": "Golden Rule 2: Quadrilateral Interior Angles Always Sum to 360°",
                "desc": "Every four-sided polygon (square, rectangle, parallelogram, rhombus, trapezium, kite) has interior angles that sum to 360°.",
                "badge": "Triangles = 180° | Quadrilaterals = 360°"
            }
        ],
        "skills": [
            {
                "title": "Quadrilateral Taxonomy",
                "summary": "Key properties of the six essential quadrilaterals.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Shape</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Sides</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Angles</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Lines of Symmetry</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Square</td><td style="padding:6px; border:1px solid #cbd5e1;">4 equal sides, 2 pairs parallel</td><td style="padding:6px; border:1px solid #cbd5e1;">4 right angles (90°)</td><td style="padding:6px; border:1px solid #cbd5e1;">4 lines</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Rectangle</td><td style="padding:6px; border:1px solid #cbd5e1;">Opposite sides equal &amp; parallel</td><td style="padding:6px; border:1px solid #cbd5e1;">4 right angles (90°)</td><td style="padding:6px; border:1px solid #cbd5e1;">2 lines</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Parallelogram</td><td style="padding:6px; border:1px solid #cbd5e1;">Opposite sides equal &amp; parallel</td><td style="padding:6px; border:1px solid #cbd5e1;">Opposite angles equal</td><td style="padding:6px; border:1px solid #cbd5e1;">0 lines</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Trapezium</td><td style="padding:6px; border:1px solid #cbd5e1;">Exactly 1 pair of parallel sides</td><td style="padding:6px; border:1px solid #cbd5e1;">Varies</td><td style="padding:6px; border:1px solid #cbd5e1;">0 (or 1 if isosceles)</td></tr>
                    </tbody>
                  </table>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Hospital Signboard Geometry & Lines of Symmetry",
                "marks": "3 Marks (Pearson Edexcel Level 1/2)",
                "context": "Facility Signage Wayfinding Design",
                "question": "An emergency exit signboard is manufactured in the shape of a <strong>regular octagon</strong>.<br>(a) How many sides does an octagon have?<br>(b) How many lines of symmetry does a regular octagon possess?<br>(c) State the order of rotational symmetry of a regular octagon.",
                "steps": [
                    ("Step 1", "State the number of sides of an octagon", "An octagon has 8 sides.", "A1: Correct polygon side count"),
                    ("Step 2", "Determine lines of reflective symmetry", "A regular polygon with n sides has exactly n lines of symmetry. An 8-sided regular octagon has 8 lines of symmetry.", "A1: Correct lines of symmetry"),
                    ("Step 3", "Determine rotational symmetry order", "A regular polygon with n sides has rotational symmetry of order n. Therefore, order = 8.", "A1: Correct rotational symmetry order")
                ],
                "final_answer": "(a) 8 sides | (b) 8 lines of symmetry | (c) Rotational symmetry of order 8.",
                "tutor_tip": "Golden rule: For ANY regular polygon (equilateral triangle, square, regular pentagon, hexagon, octagon), the number of sides = lines of symmetry = order of rotational symmetry!"
            }
        ],
        "examiner_traps": [
            {
                "title": "Confusing a Parallelogram with Having 2 Lines of Symmetry",
                "desc": "A standard parallelogram has ZERO lines of reflective symmetry, even though it has rotational symmetry of order 2.",
                "fix": "Fold it mentally: the corners do not align when folded along the diagonals or middle."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A tile has 6 equal sides and 6 equal interior angles.<br>(a) What is the mathematical name of this shape?<br>(b) How many lines of symmetry does it have?",
                "solution_steps": "1. A 6-sided regular polygon is a Regular Hexagon.<br>2. A regular hexagon has 6 lines of symmetry.",
                "correct_answer": "(a) Regular Hexagon | (b) 6 lines of symmetry",
                "tutor_tip": "Remember 'hex' = 6."
            }
        ]
    },
    {
        "filename": "functional-skills-3d-shapes.html",
        "clean_topic": "3D Solids: Faces, Edges & Vertices",
        "intro_lead": "Identify and classify 3D solids (cuboids, prisms, pyramids, cylinders, cones, spheres), identify vertices, edges, and faces, and understand geometric cross-sections.",
        "next_file": "functional-skills-nets.html",
        "next_name": "Nets of 3D Shapes",
        "spec_points": [
            ("L1.20 / L2.22", "Identify 3D shapes and their properties (faces, edges, vertices) from 2D representations.")
        ],
        "golden_rules": [
            {
                "icon": "fa-cube",
                "title": "Golden Rule 1: The Three Properties: Faces, Edges & Vertices",
                "desc": "Faces = Flat or curved surfaces. Edges = Lines where two faces meet. Vertices = Sharp corners where edges meet.",
                "badge": "Faces = Surfaces | Edges = Lines | Vertices = Corners"
            },
            {
                "icon": "fa-diagram-project",
                "title": "Golden Rule 2: Euler's Formula for Polyhedra (F + V - E = 2)",
                "desc": "For any 3D solid with flat polygon faces: Faces + Vertices - Edges = 2. A cube has 6 faces, 8 vertices, and 12 edges (6 + 8 - 12 = 2).",
                "badge": "Faces + Vertices - Edges = 2"
            }
        ],
        "skills": [
            {
                "title": "3D Solids Property Reference Table",
                "summary": "Faces, edges, and vertices for common exam solids.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:center;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Solid</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Faces</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Edges</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Vertices</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Cube / Cuboid</td><td style="padding:6px; border:1px solid #cbd5e1;">6</td><td style="padding:6px; border:1px solid #cbd5e1;">12</td><td style="padding:6px; border:1px solid #cbd5e1;">8</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Triangular Prism</td><td style="padding:6px; border:1px solid #cbd5e1;">5</td><td style="padding:6px; border:1px solid #cbd5e1;">9</td><td style="padding:6px; border:1px solid #cbd5e1;">6</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Square-Based Pyramid</td><td style="padding:6px; border:1px solid #cbd5e1;">5</td><td style="padding:6px; border:1px solid #cbd5e1;">8</td><td style="padding:6px; border:1px solid #cbd5e1;">5</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Cylinder</td><td style="padding:6px; border:1px solid #cbd5e1;">3 (2 flat, 1 curved)</td><td style="padding:6px; border:1px solid #cbd5e1;">2 (curved)</td><td style="padding:6px; border:1px solid #cbd5e1;">0</td></tr>
                    </tbody>
                  </table>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Clinical Sharps Bin 3D Geometry Specification",
                "marks": "3 Marks (Pearson Edexcel Level 1/2)",
                "context": "Healthcare Infection Control Equipment",
                "question": "A clinical sharps disposal container is shaped as a <strong>hexagonal prism</strong>.<br>(a) State the shape of its two end faces.<br>(b) How many faces does the sharps container have in total?<br>(c) How many edges does it have?",
                "steps": [
                    ("Step 1", "Identify the cross-sectional end faces", "A hexagonal prism has two identical end faces shaped as hexagons (6-sided polygons).", "A1: Correct cross-sectional face shape"),
                    ("Step 2", "Calculate total faces", "2 hexagonal end faces + 6 rectangular side faces = 8 faces in total.", "A1: Accurate total faces (8)"),
                    ("Step 3", "Calculate total edges", "6 edges on top hexagon + 6 edges on bottom hexagon + 6 vertical connecting edges = 18 edges.", "A1: Accurate total edges (18)")
                ],
                "final_answer": "(a) Hexagons | (b) 8 faces | (c) 18 edges",
                "tutor_tip": "For any prism with an n-sided base: Faces = n + 2, Edges = 3n, Vertices = 2n."
            }
        ],
        "examiner_traps": [
            {
                "title": "Confusing a Triangular Prism with a Pyramid",
                "desc": "A triangular prism has 5 faces (2 triangular ends and 3 rectangles). A triangular pyramid (tetrahedron) has 4 triangular faces meeting at a single apex.",
                "fix": "Look for the uniform cross-section: prisms have matching ends, pyramids come to a point."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A tent is shaped as a triangular prism.<br>(a) How many vertices does it have?<br>(b) How many edges does it have?",
                "solution_steps": "1. Vertices: 3 at front triangle + 3 at back triangle = 6 vertices.<br>2. Edges: 3 at front + 3 at back + 3 connecting lengths = 9 edges.",
                "correct_answer": "(a) 6 vertices | (b) 9 edges",
                "tutor_tip": "Vertices are corners (3 on each end = 6)."
            }
        ]
    },
    {
        "filename": "functional-skills-nets.html",
        "clean_topic": "Nets of 3D Shapes & Packaging",
        "intro_lead": "Visualize and construct 2D nets of cubes, cuboids, prisms, and pyramids, and identify which unfolded templates correctly fold into closed 3D solids for commercial packaging.",
        "next_file": "functional-skills-plans-and-elevations.html",
        "next_name": "Plans & Elevations",
        "spec_points": [
            ("L1.20 / L2.22", "Identify and draw nets of 3D solids including cuboids, prisms, and cylinders.")
        ],
        "golden_rules": [
            {
                "icon": "fa-box-open",
                "title": "Golden Rule 1: Opposite Faces in a Cube Net Must Not Touch",
                "desc": "In any valid net of a cube, opposite faces are always separated by exactly one intervening square (or situated on opposite sides of a row). Two adjacent squares cannot both fold into opposite faces.",
                "badge": "Opposite faces have exactly 1 square between them"
            },
            {
                "icon": "fa-scissors",
                "title": "Golden Rule 2: Check Edge Matchings Before Folding",
                "desc": "When folding a net, check that adjacent edges that meet are of identical length and that flaps don't overlap to leave an open hole.",
                "badge": "Matching perimeter lengths must align when folded"
            }
        ],
        "skills": [
            {
                "title": "Valid Cube Net Configurations",
                "summary": "There are exactly 11 distinct valid nets that fold into a closed cube.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">The most common valid cube nets in exams are:</p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>The Cross Net (1-4-1):</strong> A central row of 4 squares, with 1 square above and 1 square below.</li>
                    <li><strong>The T-Shape:</strong> 3 squares vertical with a horizontal bar of 4.</li>
                    <li><strong>The Stepped Net (2-2-2 / 3-3):</strong> Stepped arrangements where no 4 squares form a 2×2 block (a 2×2 block can NEVER form a cube!).</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Pharmaceutical Medicine Box Carton Packaging Net",
                "marks": "3 Marks (Pearson Edexcel Level 2)",
                "context": "Pharmaceutical Commercial Packaging",
                "question": "A pharmaceutical company manufactures tablet boxes measuring <strong>8 cm long, 5 cm wide, and 3 cm deep</strong>.<br>(a) How many rectangular faces must the net contain?<br>(b) State the dimensions of the three pairs of matching faces in the net.<br>(c) Explain why a 2×2 block of squares cannot form part of a valid cube net.",
                "steps": [
                    ("Step 1", "State total faces for a closed cuboid", "A closed cuboid box requires exactly 6 rectangular faces.", "A1: Correct face count"),
                    ("Step 2", "Identify dimensions of the three pairs of faces", "Pair 1 (Top/Bottom): 8 cm × 5 cm.<br>Pair 2 (Front/Back): 8 cm × 3 cm.<br>Pair 3 (Ends): 5 cm × 3 cm.", "M1: Accurate dimensions for all 3 pairs"),
                    ("Step 3", "Explain why 2×2 block fails", "In a 2×2 block, four faces share a single central vertex. When folded, two faces will overlap each other, leaving another side of the cube open.", "A1: Valid geometrical explanation")
                ],
                "final_answer": "(a) 6 faces | (b) Two 8×5 cm, two 8×3 cm, two 5×3 cm | (c) A 2×2 block causes overlapping faces, leaving an open side.",
                "tutor_tip": "If you see a 2×2 block anywhere in a proposed cube net, you can immediately rule it out as invalid!"
            }
        ],
        "examiner_traps": [
            {
                "title": "Drawing Only 5 Faces for a Closed Box",
                "desc": "Forgetting the top lid or one end face results in an open container, losing accuracy marks.",
                "fix": "Count: Top, Bottom, Front, Back, Left, Right = 6 faces."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A net for a triangular prism is drawn. How many triangular faces and how many rectangular faces must it contain?",
                "solution_steps": "1. Triangular ends = 2 triangular faces.<br>2. Connecting sides = 3 rectangular faces.<br>3. Total = 2 triangles and 3 rectangles (5 faces).",
                "correct_answer": "2 triangular faces and 3 rectangular faces",
                "tutor_tip": "A triangular prism has 5 faces in total."
            }
        ]
    },
    {
        "filename": "functional-skills-plans-and-elevations.html",
        "clean_topic": "Plans, Elevations & Front/Side Views",
        "intro_lead": "Interpret and draw 2D orthographic projections: plan views (looking straight down from above), front elevations, and side elevations of architectural buildings and workplace structures.",
        "next_file": "functional-skills-angles.html",
        "next_name": "Angles & Bearings",
        "spec_points": [
            ("L1.20 / L2.22", "Draw 2D representations of 3D objects including plan views, front elevations, and side elevations.")
        ],
        "golden_rules": [
            {
                "icon": "fa-eye",
                "title": "Golden Rule 1: The Three Viewing Directions",
                "desc": "Plan View = Looking down from above (bird's eye view). Front Elevation = Looking directly at the front. Side Elevation = Looking directly from the left or right.",
                "badge": "Plan = Looking Down | Front = Looking Ahead | Side = Looking from Side"
            },
            {
                "icon": "fa-border-all",
                "title": "Golden Rule 2: Use the Grid Scale Accurately",
                "desc": "Check grid scale: 1 square may represent 1 metre or 50 cm. Count grid units carefully and draw with a straight ruler.",
                "badge": "Always use a ruler and label dimensions"
            }
        ],
        "skills": [
            {
                "title": "Orthographic Projection Conventions",
                "summary": "Translating 3D solid coordinates into 2D projections.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Plan View shows:</strong> Width and Length (No height).</li>
                    <li><strong>Front Elevation shows:</strong> Width and Height (No length/depth).</li>
                    <li><strong>Side Elevation shows:</strong> Length/Depth and Height (No width).</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Hospital Emergency Generator Enclosure Orthographic Projections",
                "marks": "3 Marks (Pearson Edexcel Level 2)",
                "context": "Healthcare Facility Engineering Plans",
                "question": "A backup diesel generator housing is a cuboid measuring <strong>4 m long, 2.5 m wide, and 2 m high</strong>.<br>(a) State the 2D shape and dimensions of the Plan View.<br>(b) State the 2D shape and dimensions of the Front Elevation (viewed from the 4 m front).<br>(c) State the 2D shape and dimensions of the Side Elevation.",
                "steps": [
                    ("Step 1", "Determine Plan View dimensions (Length × Width)", "Plan view is viewed from above: a rectangle measuring 4 m long by 2.5 m wide.", "A1: Accurate plan view"),
                    ("Step 2", "Determine Front Elevation dimensions (Width × Height)", "Front elevation is viewed facing the 4 m side: a rectangle measuring 4 m wide by 2 m high.", "A1: Accurate front elevation"),
                    ("Step 3", "Determine Side Elevation dimensions (Depth × Height)", "Side elevation is viewed from the side: a rectangle measuring 2.5 m deep by 2 m high.", "A1: Accurate side elevation")
                ],
                "final_answer": "(a) Plan: 4 m × 2.5 m rectangle | (b) Front: 4 m × 2 m rectangle | (c) Side: 2.5 m × 2 m rectangle.",
                "tutor_tip": "Remember: Plan view NEVER includes height; front view NEVER includes depth."
            }
        ],
        "examiner_traps": [
            {
                "title": "Including Height in the Plan View",
                "desc": "Drawing the height on a plan view is impossible because you are looking straight down from above.",
                "fix": "Plan = Floor layout only (Length and Width)."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A cylindrical water storage tank has a diameter of 3 m and a height of 4 m.<br>(a) What 2D shape is its plan view?<br>(b) What 2D shape is its front elevation?",
                "solution_steps": "1. Plan view from above = Circle of diameter 3 m.<br>2. Front elevation from the side = Rectangle of 3 m wide by 4 m high.",
                "correct_answer": "(a) Circle (diameter 3 m) | (b) Rectangle (3 m wide by 4 m high)",
                "tutor_tip": "Looking at a cylinder from the side produces a flat rectangular projection."
            }
        ]
    }
]

# Write out domain 4
with open("/home/subi/Projects/masterfunctionalskills.co.uk/maths_domain4_geometry.py", "w", encoding="utf-8") as f:
    f.write("#!/usr/bin/env python3\n")
    f.write('"""Maths Domain 4: Shape, Space & Geometry (5 Core Topics)"""\n\n')
    f.write("TOPICS_DOMAIN4 = " + repr(TOPICS_DOMAIN4) + "\n")

print(f"Domain 4 written with {len(TOPICS_DOMAIN4)} topics!")
