#!/usr/bin/env python3
import maths_domain4_geometry

all_d4 = list(maths_domain4_geometry.TOPICS_DOMAIN4)

more_d4 = [
    {
        "filename": "functional-skills-angles.html",
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
                "question": "An emergency air ambulance takes off from hospital helipad H and flies directly to an accident site A on a bearing of <strong>074°</strong>.<br>(a) Is this bearing Acute, Right-Angled, Obtuse, or Reflex?<br>(b) Calculate the back bearing from the accident site A to return to helipad H.",
                "steps": [
                    ("Step 1", "Classify the angle size", "074° is between 0° and 90°; therefore, it is an ACUTE angle.", "A1: Correct angle classification"),
                    ("Step 2", "Apply back bearing rule (bearing is less than 180°)", "Since 074° < 180°, add 180°: 074° + 180° = 254°.", "M1: Back bearing addition method"),
                    ("Step 3", "State return bearing in 3-figure notation", "Back bearing = 254°.", "A1: Accurate 3-figure bearing")
                ],
                "final_answer": "(a) Acute angle | (b) Return bearing = 254°",
                "tutor_tip": "Always write bearings with 3 digits. If the answer is 45 degrees, write 045°."
            }
        ],
        "examiner_traps": [
            {
                "title": "Writing Bearings with Two Digits",
                "desc": "Writing '74°' instead of '074°' forfeits the bearing accuracy mark.",
                "fix": "Always pad with a leading zero if under 100°."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "Two straight roads cross at an intersection. One angle is 65°. What is the size of the obtuse angle on the straight line?",
                "solution_steps": "1. Angles on a straight line sum to 180°.<br>2. 180° - 65° = 115°.",
                "correct_answer": "115°",
                "tutor_tip": "180 - 65 = 115 degrees."
            }
        ]
    },
    {
        "filename": "functional-skills-angles-in-2d-shapes.html",
        "clean_topic": "Angles in Triangles, Quadrilaterals & Polygons",
        "intro_lead": "Calculate missing interior and exterior angles in equilateral, isosceles, and right-angled triangles, quadrilaterals, and regular polygons.",
        "next_file": "functional-skills-circles.html",
        "next_name": "Circles & Circumference",
        "spec_points": [
            ("L1.21 / L2.23", "Calculate interior angles of triangles, quadrilaterals, and regular polygons.")
        ],
        "golden_rules": [
            {
                "icon": "fa-draw-polygon",
                "title": "Golden Rule 1: Sum of Interior Angles = (n - 2) × 180°",
                "desc": "For any polygon with n sides: Triangle (3 sides) = 1 × 180° = 180°. Quadrilateral (4) = 2 × 180° = 360°. Pentagon (5) = 3 × 180° = 540°. Hexagon (6) = 4 × 180° = 720°.",
                "badge": "Interior Angle Sum = (Number of Sides - 2) × 180°"
            },
            {
                "icon": "fa-circle-notch",
                "title": "Golden Rule 2: Exterior Angles of ANY Polygon Sum to 360°",
                "desc": "If you walk all the way around the outside of any polygon, you make one full turn (360°). For a regular polygon: Each Exterior Angle = 360° ÷ Number of Sides.",
                "badge": "Each Exterior Angle = 360° ÷ n"
            }
        ],
        "skills": [
            {
                "title": "Triangle Angle Rules Summary",
                "summary": "Key properties of the four triangle types.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Equilateral:</strong> All 3 sides equal, all 3 angles = 60° (180 ÷ 3).</li>
                    <li><strong>Isosceles:</strong> 2 sides equal, 2 base angles opposite those sides are equal.</li>
                    <li><strong>Right-Angled:</strong> Contains one 90° angle; other two angles sum to 90°.</li>
                    <li><strong>Scalene:</strong> All 3 sides and all 3 angles are different; still sum to 180°.</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Architectural Roof Gable Truss Angle Calculation",
                "marks": "3 Marks (Pearson Edexcel Level 2)",
                "context": "Construction Timber Roof Truss Design",
                "question": "A timber roof truss forms an <strong>isosceles triangle</strong>. The top ridge angle between the two equal rafters is <strong>76°</strong>.<br>Calculate the size of each of the two identical base angles at the eaves.",
                "steps": [
                    ("Step 1", "Recall total interior angle sum of a triangle", "Interior angles of a triangle sum to 180°.", "B1: Triangle angle property"),
                    ("Step 2", "Subtract known ridge angle from 180°", "180° - 76° = 104° remaining for both base angles.", "M1: Angle difference calculation"),
                    ("Step 3", "Divide remainder by 2 for the identical base angles", "104° ÷ 2 = 52°.", "A1: Accurate base angle size (52°)")
                ],
                "final_answer": "Each base angle = 52°",
                "tutor_tip": "Check: 52° + 52° + 76° = 180°. Both base angles are equal because it is an isosceles triangle."
            }
        ],
        "examiner_traps": [
            {
                "title": "Assuming All Triangles Have 60° Angles",
                "desc": "Only equilateral triangles have 60° angles. Always inspect whether the triangle is isosceles, right-angled, or scalene.",
                "fix": "Look for tick marks on sides indicating equal side lengths."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "Calculate the size of one interior angle of a regular pentagon (5 sides).",
                "solution_steps": "1. Exterior angle = 360° ÷ 5 = 72°.<br>2. Interior angle = 180° - 72° = 108° (or (5-2)×180 ÷ 5 = 540 ÷ 5 = 108°).",
                "correct_answer": "108°",
                "tutor_tip": "Using exterior angles (360 ÷ n) then subtracting from 180 is the fastest method."
            }
        ]
    },
    {
        "filename": "functional-skills-circles.html",
        "clean_topic": "Circles: Radius, Diameter, Circumference & Area",
        "intro_lead": "Calculate the circumference (perimeter) and area of circles, semi-circles, and circular sectors using π (3.14 or 3.142) in landscaping and healthcare equipment design.",
        "next_file": "functional-skills-coordinates.html",
        "next_name": "Coordinates",
        "spec_points": [
            ("L2.25", "Calculate circumference and area of circles, using given values of pi (e.g. 3.14 or 22/7).")
        ],
        "golden_rules": [
            {
                "icon": "fa-circle",
                "title": "Golden Rule 1: The Two Core Circle Formulas",
                "desc": "Circumference = π × d (or 2πr) • Area = π × r². Remember: Radius is half the diameter (r = d ÷ 2).",
                "badge": "Circumference = πd | Area = πr²"
            },
            {
                "icon": "fa-arrows-left-right",
                "title": "Golden Rule 2: Square the Radius BEFORE Multiplying by π",
                "desc": "In Area = πr², calculate r × r first, THEN multiply by 3.14. Do NOT multiply π by r and square that result!",
                "badge": "Area = 3.14 × (r × r)"
            }
        ],
        "skills": [
            {
                "title": "Radius vs Diameter",
                "summary": "Never use diameter in the area formula without halving it first.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Radius (r):</strong> Distance from the exact center to the edge (e.g. 4 cm).</li>
                    <li><strong>Diameter (d):</strong> Distance all the way across through the center (e.g. 8 cm). d = 2r.</li>
                    <li><strong>Semi-Circle Perimeter:</strong> Half circumference + straight diameter line: <em>(πd ÷ 2) + d.</em></li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Hospital Sensory Garden Circular Turf & Edging",
                "marks": "3 Marks (Pearson Edexcel Level 2)",
                "context": "Healthcare Facility Therapeutic Garden Landscaping",
                "question": "A hospital wellbeing garden features a circular lawn with a <strong>diameter of 12 metres</strong>. Use <strong>π = 3.14</strong>.<br>(a) Calculate the area of turf needed in m².<br>(b) Calculate the length of metal edging required to surround the circular perimeter.",
                "steps": [
                    ("Step 1", "Calculate the radius of the lawn", "Radius = Diameter ÷ 2 = 12 m ÷ 2 = 6 metres.", "B1: Radius identification"),
                    ("Step 2", "Calculate Area = πr²", "Area = 3.14 × 6² = 3.14 × 36 = 113.04 m².", "M1: Area formula execution"),
                    ("Step 3", "Calculate Circumference = πd", "Circumference = 3.14 × 12 m = 37.68 metres.", "A1: Accurate circumference calculation")
                ],
                "final_answer": "(a) Area = 113.04 m² | (b) Edging Length = 37.68 m",
                "tutor_tip": "Notice that for area you square the radius (6² = 36), while for circumference you use the diameter (12)."
            }
        ],
        "examiner_traps": [
            {
                "title": "Using Diameter in the Area Formula",
                "desc": "Doing 3.14 × 12² = 452.16 m² is 4 times too big! You MUST halve diameter to find radius (6 m) first.",
                "fix": "Always write 'r = ...' before writing the area formula."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A circular pond has a radius of 2.5 metres. Using π = 3.14, calculate the circumference of the pond.",
                "solution_steps": "1. Diameter = 2.5 × 2 = 5 metres.<br>2. Circumference = π × d = 3.14 × 5 = 15.7 metres.",
                "correct_answer": "15.7 m",
                "tutor_tip": "Circumference = 2 × π × r = 2 × 3.14 × 2.5 = 15.7 m."
            }
        ]
    },
    {
        "filename": "functional-skills-coordinates.html",
        "clean_topic": "Coordinates: Positive & Four Quadrants",
        "intro_lead": "Plot and read coordinates in all four quadrants (x, y), find midpoints of line segments, and identify missing vertices of geometric shapes on Cartesian grids.",
        "next_file": "functional-skills-maps-and-scale-drawings.html",
        "next_name": "Maps & Scale Drawings",
        "spec_points": [
            ("L1.22 / L2.26", "Use coordinates in 2D grids (including all four quadrants) to specify position.")
        ],
        "golden_rules": [
            {
                "icon": "fa-crosshairs",
                "title": "Golden Rule 1: 'Along the Corridor, Up or Down the Stairs'",
                "desc": "The first number is always the X-coordinate (horizontal axis: left or right). The second number is always the Y-coordinate (vertical axis: up or down).",
                "badge": "(X, Y) = (Horizontal, Vertical)"
            },
            {
                "icon": "fa-arrows-to-dot",
                "title": "Golden Rule 2: Origin is (0, 0)",
                "desc": "All coordinates start at the origin (0, 0). Negative x goes left; negative y goes down.",
                "badge": "Left = -X | Right = +X | Down = -Y | Up = +Y"
            }
        ],
        "skills": [
            {
                "title": "The Four Quadrants",
                "summary": "Signs of coordinates in each quadrant.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Quadrant 1 (Top-Right):</strong> (+x, +y) e.g. (4, 3)</li>
                    <li><strong>Quadrant 2 (Top-Left):</strong> (-x, +y) e.g. (-4, 3)</li>
                    <li><strong>Quadrant 3 (Bottom-Left):</strong> (-x, -y) e.g. (-4, -3)</li>
                    <li><strong>Quadrant 4 (Bottom-Right):</strong> (+x, -y) e.g. (4, -3)</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Logistics Depot Automated Guided Vehicle (AGV) Grid Plotting",
                "marks": "3 Marks (Pearson Edexcel Level 2)",
                "context": "Automated Warehouse Robotics Grid",
                "question": "An automated warehouse dispatch floor is mapped on a Cartesian coordinate grid. Three charging bays form three corners of a rectangle:<br>Bay A: <strong>(-3, 2)</strong><br>Bay B: <strong>(5, 2)</strong><br>Bay C: <strong>(5, -4)</strong><br>(a) State the coordinates of the fourth corner, Bay D.<br>(b) Calculate the length and width of the rectangle in grid units.",
                "steps": [
                    ("Step 1", "Analyze x and y coordinate pairings for rectangle", "Side AB is horizontal from x = -3 to x = 5 (at y = 2).<br>Side BC is vertical from y = 2 to y = -4 (at x = 5).<br>Bay D must have x = -3 (aligned with A) and y = -4 (aligned with C).", "M1: Rectangle coordinate alignment"),
                    ("Step 2", "State coordinates of Bay D", "Bay D = (-3, -4).", "A1: Accurate 4th vertex coordinates"),
                    ("Step 3", "Calculate length and width", "Length = 5 - (-3) = 8 units.<br>Width = 2 - (-4) = 6 units.", "A1: Accurate dimensions (8 by 6 units)")
                ],
                "final_answer": "(a) Bay D = (-3, -4) | (b) Length = 8 units, Width = 6 units.",
                "tutor_tip": "Notice how the x-coordinates pair up (-3 and 5) and the y-coordinates pair up (2 and -4)."
            }
        ],
        "examiner_traps": [
            {
                "title": "Swapping X and Y Coordinates",
                "desc": "Writing (2, -3) instead of (-3, 2) plots the point on the opposite side of the diagonal axis.",
                "fix": "Always repeat: 'X first (horizontal), Y second (vertical)'."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "What is the midpoint between points P(-2, 4) and Q(6, 10)?",
                "solution_steps": "1. Midpoint x = (-2 + 6) ÷ 2 = 4 ÷ 2 = 2.<br>2. Midpoint y = (4 + 10) ÷ 2 = 14 ÷ 2 = 7.<br>3. Midpoint = (2, 7).",
                "correct_answer": "(2, 7)",
                "tutor_tip": "Average the x values, average the y values."
            }
        ]
    },
    {
        "filename": "functional-skills-maps-and-scale-drawings.html",
        "clean_topic": "Maps, Scale Ratios & Floor Plans",
        "intro_lead": "Interpret ratio scales (e.g. 1 : 50, 1 : 25,000), calculate real-world distances from map measurements, and draw scaled floor plans for ward layouts and interior design.",
        "next_file": "functional-skills-mean-median-mode-and-range.html",
        "next_name": "Averages (Mean, Median, Mode, Range)",
        "spec_points": [
            ("L1.19 / L2.27", "Use scale drawings and scale factors in familiar and unfamiliar contexts, including scale ratios.")
        ],
        "golden_rules": [
            {
                "icon": "fa-map",
                "title": "Golden Rule 1: The Ratio Scale Means '1 Unit on Map = N Units in Real Life'",
                "desc": "A scale of 1 : 50 means 1 cm on the plan represents 50 cm in reality. A scale of 1 : 25,000 means 1 cm represents 25,000 cm (= 250 m = 0.25 km).",
                "badge": "Real Distance = Map Measurement × Scale Factor"
            },
            {
                "icon": "fa-pencil-ruler",
                "title": "Golden Rule 2: Drawing to Scale: Real Distance ÷ Scale Factor",
                "desc": "To draw a 6-metre wall on a 1 : 50 plan: convert 6 m to 600 cm, then divide by 50 = 12 cm on paper.",
                "badge": "Drawing Length = Real Distance (cm) ÷ Scale Factor"
            }
        ],
        "skills": [
            {
                "title": "Converting Metric Units with Large Scale Ratios",
                "summary": "Handling large map scales (1 : 25,000 and 1 : 50,000).",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li>1 : 100 → 1 cm = 100 cm = 1 metre.</li>
                    <li>1 : 25,000 → 1 cm = 25,000 cm = 250 metres (4 cm = 1 km).</li>
                    <li>1 : 50,000 → 1 cm = 50,000 cm = 500 metres (2 cm = 1 km).</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Hospital Acute Ward Refurbishment Scale Floor Plan",
                "marks": "3 Marks (Pearson Edexcel Level 2)",
                "context": "Architectural Ward Redesign",
                "question": "A hospital architect produces a ward floor plan using a scale of <strong>1 : 50</strong>.<br>(a) On the drawing, Bay 3 measures <strong>14 cm long by 9 cm wide</strong>. What are the actual real-world dimensions in metres?<br>(b) A clinical consultation desk is <strong>2.5 metres long</strong> in reality. What length should it be drawn on the scale plan?",
                "steps": [
                    ("Step 1", "Multiply map measurements by scale factor (50)", "Real length = 14 cm × 50 = 700 cm.<br>Real width = 9 cm × 50 = 450 cm.", "M1: Scale multiplication"),
                    ("Step 2", "Convert real dimensions from centimetres to metres", "700 cm ÷ 100 = 7 metres.<br>450 cm ÷ 100 = 4.5 metres.", "A1: Accurate real dimensions (7 m × 4.5 m)"),
                    ("Step 3", "Calculate drawing length for the consultation desk", "Real length = 2.5 m = 250 cm.<br>Drawing length = 250 cm ÷ 50 = 5 cm.", "A1: Accurate drawing length (5 cm)")
                ],
                "final_answer": "(a) Real dimensions = 7 m long by 4.5 m wide | (b) Drawing length = 5 cm.",
                "tutor_tip": "Golden sanity check: Real room dimensions should be in metres (7 m × 4.5 m); drawings should be in centimetres (5 cm)."
            }
        ],
        "examiner_traps": [
            {
                "title": "Forgetting to Convert Centimetres to Metres",
                "desc": "Writing that a hospital room is '700 cm' without converting to metres when metres is requested forfeits the accuracy mark.",
                "fix": "Always check the required unit in the answer line."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "On an Ordnance Survey map with scale 1 : 25,000, the distance between two medical clinics measures 6 cm. What is the actual distance in kilometres?",
                "solution_steps": "1. Real distance = 6 cm × 25,000 = 150,000 cm.<br>2. Convert to metres: 150,000 ÷ 100 = 1,500 m.<br>3. Convert to kilometres: 1,500 ÷ 1,000 = 1.5 km.",
                "correct_answer": "1.5 km",
                "tutor_tip": "Divide cm by 100,000 to get kilometres directly (150,000 ÷ 100,000 = 1.5 km)."
            }
        ]
    }
]

all_d4.extend(more_d4)

with open("/home/subi/Projects/masterfunctionalskills.co.uk/maths_domain4_geometry.py", "w", encoding="utf-8") as f:
    f.write("#!/usr/bin/env python3\n")
    f.write('"""Maths Domain 4: Shape, Space & Geometry (10 Core Topics)"""\n\n')
    f.write("TOPICS_DOMAIN4 = " + repr(all_d4) + "\n")

print(f"Domain 4 complete with {len(all_d4)} topics!")
