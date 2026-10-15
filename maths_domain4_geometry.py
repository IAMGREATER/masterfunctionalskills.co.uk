#!/usr/bin/env python3
"""Maths Domain 4: Shape, Space & Geometry (8 Core Topics — functional-skills-nets.html is a bespoke interactive masterclass)"""

TOPICS_DOMAIN4 = [
    {
        'filename': 'functional-skills-surface-area.html',
        'clean_topic': 'Surface Area of Prisms & Cylinders',
        'intro_lead': 'Calculate the total surface area of cuboids, triangular prisms, and cylinders to determine painting, plastering, sheet metal, and packaging material requirements.',
        'next_file': 'functional-skills-2d-shapes.html',
        'next_name': '2D Shapes',
        'spec_points': [
            ('L1.22 / L2.24', 'Calculate the total surface area of cubes and cuboids in practical wrapping and painting contexts.'),
            ('L2.24', 'Calculate the surface area of triangular prisms, cylinders, and open-top containers.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-cubes',
                'title': 'Golden Rule 1: Surface Area is the Total Area of All Outside Faces',
                'desc': 'Surface area is 2D area (measured in cm² or m²), NOT 3D volume. For a closed cuboid: calculate the area of each pair of matching faces and add all 6 faces together: (2 × Top/Bottom) + (2 × Front/Back) + (2 × Left/Right).',
                'badge': 'Cuboid Surface Area = 2(lw) + 2(lh) + 2(wh)'
            },
            {
                'icon': 'fa-circle-notch',
                'title': 'Golden Rule 2: Cylinder Surface Area = Two Circles Plus One Unwrapped Rectangle',
                'desc': 'The curved body unrolls into a flat rectangle (length = π × Diameter, height = cylinder height). Add the two circular end caps: Total Surface Area = (2 × π × r²) + (π × d × h).',
                'badge': 'Cylinder SA = 2πr² + πdh'
            }
        ],
        'skills': [
            {
                'title': 'Cuboid 6-Face Method vs Open-Top Containers',
                'summary': 'Step-by-step breakdown of cuboid faces and how to adjust for 5-face open tanks or rooms.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">A closed rectangular box has <strong>6 rectangular faces</strong> arranged in 3 identical pairs:</p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Top &amp; Bottom Pair:</strong> 2 &times; (Length &times; Width)</li>
                    <li><strong>Front &amp; Back Pair:</strong> 2 &times; (Length &times; Height)</li>
                    <li><strong>Left &amp; Right Ends:</strong> 2 &times; (Width &times; Height)</li>
                    <li><strong>Open-Top / No-Base Containers (5 Faces):</strong> Only include <strong>1 &times; (Length &times; Width)</strong> plus the 4 vertical walls.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Surface Area of a Triangular Prism (5 Faces)',
                'summary': 'Adding two triangular end cross-sections to three rectangular side panels.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">A triangular prism (such as a roof tent or Toblerone-style package) has <strong>5 faces</strong>:</p>
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Two Triangular Ends:</strong> Each triangle is (Base &times; Vertical Height) &divide; 2. Together, the two ends equal <strong>Base &times; Vertical Height</strong>.</li>
                    <li><strong>Base Rectangle:</strong> Base Width &times; Prism Length.</li>
                    <li><strong>Two Sloping Roof Rectangles:</strong> Slant Edge &times; Prism Length (use the slanted edge length, NOT the vertical height!).</li>
                  </ol>
                </div>
                """
            },
            {
                'title': 'Curved & Total Surface Area of a Cylinder',
                'summary': 'Unrolling the curved wall into a rectangle and adding circular end caps.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:left;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Component</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Formula (using &pi; = 3.14)</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">When to Use</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">Curved Wall Only</td><td style="padding:8px; border:1px solid #cbd5e1;">3.14 &times; Diameter &times; Height</td><td style="padding:8px; border:1px solid #cbd5e1;">Pipe insulation, tin can paper labels, paint roller coverage</td></tr>
                      <tr><td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">One Circular End</td><td style="padding:8px; border:1px solid #cbd5e1;">3.14 &times; Radius &times; Radius</td><td style="padding:8px; border:1px solid #cbd5e1;">Open-top cylindrical bin or water butt (Curved Wall + 1 Circle)</td></tr>
                      <tr><td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">Closed Cylinder (All 3 Faces)</td><td style="padding:8px; border:1px solid #cbd5e1;">(2 &times; 3.14 &times; r&sup2;) + (3.14 &times; d &times; h)</td><td style="padding:8px; border:1px solid #cbd5e1;">Sealed oil drum, closed medical gas tank</td></tr>
                    </tbody>
                  </table>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Sterile Medical Instrument Crate Wrapping (Level 1 Foundation)',
                'marks': '3 Marks (Pearson Edexcel Level 1)',
                'context': 'Healthcare Supply Chain Packaging',
                'question': 'A sterile equipment crate is a closed cuboid measuring <strong>50 cm long, 40 cm wide, and 30 cm high</strong>.<br>Calculate the total external surface area of the crate in cm².',
                'steps': [
                    ('Step 1', 'Calculate Top & Bottom faces', '2 × (50 cm × 40 cm) = 2 × 2,000 = 4,000 cm².', 'M1: Top and bottom pair'),
                    ('Step 2', 'Calculate Front/Back and Left/Right faces', 'Front & Back = 2 × (50 cm × 30 cm) = 2 × 1,500 = 3,000 cm².<br>Left & Right = 2 × (40 cm × 30 cm) = 2 × 1,200 = 2,400 cm².', 'M1: Remaining four faces'),
                    ('Step 3', 'Sum all 6 faces', 'Total Surface Area = 4,000 + 3,000 + 2,400 = 9,400 cm².', 'A1: Accurate total surface area (9,400 cm²)')
                ],
                'final_answer': '9,400 cm²',
                'tutor_tip': 'Write down the three pairs clearly so the examiner can award method marks even if one multiplication slips.'
            },
            {
                'title': 'Hospital Waste Disposal Steel Container Enclosure Painting (Level 2 Multi-Step)',
                'marks': '4 Marks (Pearson Edexcel Level 2)',
                'context': 'Facility Maintenance Painting & Costing',
                'question': 'A facilities maintenance team must apply anti-rust primer to the <strong>5 external faces</strong> (four vertical sides and the top roof; NOT the base on the ground) of a steel container measuring <strong>3.5 m long, 2.0 m wide, and 1.8 m high</strong>.<br>• Anti-rust primer covers <strong>6 m² per tin</strong> and costs <strong>£18.50 per tin</strong>.<br>Calculate the total cost of the primer tins required.',
                'steps': [
                    ('Step 1', 'Calculate the single top roof face (no base)', 'Top = 3.5 m × 2.0 m = 7.0 m².', 'M1: Single top face area'),
                    ('Step 2', 'Calculate the 4 vertical side walls', 'Front & Back = 2 × (3.5 m × 1.8 m) = 2 × 6.3 = 12.6 m².<br>Left & Right = 2 × (2.0 m × 1.8 m) = 2 × 3.6 = 7.2 m².<br>Total 5-face Surface Area = 7.0 + 12.6 + 7.2 = 26.8 m².', 'M1: Total 5-face surface area (26.8 m²)'),
                    ('Step 3', 'Calculate whole tins of primer needed', 'Tins = 26.8 m² ÷ 6 m² = 4.466... → Round UP to 5 whole tins.', 'M1: Division by coverage and rounding up'),
                    ('Step 4', 'Calculate total purchase cost', '5 tins × £18.50 = £92.50.', 'A1: Accurate total cost (£92.50)')
                ],
                'final_answer': '£92.50 (5 tins required for 26.8 m²)',
                'tutor_tip': 'Notice the question specifies 5 EXTERNAL FACES (no base). Always round paint tins UP so you do not run out with 2.8 m² left unpainted.'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Calculating Volume Instead of Surface Area',
                'desc': 'Multiplying Length × Width × Height (e.g. 50 × 40 × 30 = 60,000 cm³) calculates 3D volume, scoring 0 marks on a surface area question.',
                'fix': 'Highlight the words "SURFACE AREA" and write down the 3 pairs of rectangles before touching your calculator.'
            },
            {
                'title': 'Using Diameter Instead of Radius for Cylinder Ends',
                'desc': 'When calculating the two circular ends of a cylinder, learners often forget to halve the diameter first.',
                'fix': 'Always write "Radius = Diameter ÷ 2" at the very top of your working box.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'Calculate the total surface area of a closed cardboard shipping box measuring <strong>40 cm long, 30 cm wide, and 20 cm high</strong>.',
                'solution_steps': '1. Top & Bottom: 2 × (40 × 30) = 2 × 1,200 = 2,400 cm².<br>2. Front & Back: 2 × (40 × 20) = 2 × 800 = 1,600 cm².<br>3. Left & Right: 2 × (30 × 20) = 2 × 600 = 1,200 cm².<br>4. Total Surface Area = 2,400 + 1,600 + 1,200 = 5,200 cm².',
                'correct_answer': '5,200 cm²',
                'tutor_tip': 'Sum the three pairs of matching rectangular faces.'
            },
            {
                'marks': '3 Marks',
                'question': 'A closed cylindrical chemical storage drum has a <strong>radius of 0.5 m</strong> and a <strong>height of 1.2 m</strong>. Using <strong>π = 3.14</strong>, calculate the total external surface area of the drum in m².',
                'solution_steps': '1. Two circular ends: 2 × 3.14 × 0.5 × 0.5 = 1.57 m².<br>2. Curved wall (Diameter = 1.0 m): 3.14 × 1.0 × 1.2 = 3.768 m².<br>3. Total Surface Area = 1.57 + 3.768 = 5.338 m².',
                'correct_answer': '5.338 m² (or 5.34 m²)',
                'tutor_tip': 'Unroll the cylinder into 2 circles (2 × 3.14 × r²) plus 1 rectangle (3.14 × d × h).'
            },
            {
                'marks': '4 Marks',
                'question': 'A waterproof canvas tent is shaped as a triangular prism of <strong>length 2.5 m</strong>. The triangular front and back ends each have a <strong>base of 1.6 m</strong>, a <strong>vertical height of 1.5 m</strong>, and two <strong>sloping roof edges of 1.7 m each</strong>.<br>Calculate the total surface area of canvas needed for all <strong>5 faces</strong> (including the groundsheet base).',
                'solution_steps': '1. Two triangular ends: 2 × ((1.6 × 1.5) ÷ 2) = 2.4 m².<br>2. Groundsheet base rectangle: 1.6 m × 2.5 m = 4.0 m².<br>3. Two sloping roof rectangles: 2 × (1.7 m × 2.5 m) = 2 × 4.25 = 8.5 m².<br>4. Total Canvas Surface Area = 2.4 + 4.0 + 8.5 = 14.9 m².',
                'correct_answer': '14.9 m²',
                'tutor_tip': 'Use the vertical height (1.5 m) for the triangles, and the slant edge (1.7 m) for the sloping rectangular roof panels.'
            }
        ]
    },
    {
        'filename': 'functional-skills-2d-shapes.html',
        'clean_topic': '2D Shapes & Polygons',
        'intro_lead': 'Identify and classify regular and irregular 2D polygons (triangles, quadrilaterals, pentagons, hexagons, octagons), identify lines of symmetry, and apply properties of parallel and perpendicular lines.',
        'next_file': 'functional-skills-3d-shapes.html',
        'next_name': '3D Shapes',
        'spec_points': [
            ('L1.20 / L2.22', 'Recognise and use 2D representations of 2D and 3D shapes.'),
            ('L1.21', 'Understand and use properties of regular and irregular polygons, including symmetry, side lengths, and angles.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-shapes',
                'title': 'Golden Rule 1: Regular Polygons Have Equal Sides AND Equal Angles',
                'desc': "A polygon is 'regular' ONLY if all its sides are of equal length AND all its interior angles are equal (e.g. an equilateral triangle or a square). A rectangle is NOT regular because its length and width differ.",
                'badge': 'Regular = All Sides Equal + All Angles Equal'
            },
            {
                'icon': 'fa-arrows-split-up-and-left',
                'title': 'Golden Rule 2: Parallel vs Perpendicular Lines',
                'desc': 'Parallel lines run in the same direction and never meet (marked with matching arrows >>). Perpendicular lines meet at an exact right angle of 90° (marked with a small corner square).',
                'badge': 'Parallel = Never Meet • Perpendicular = Meet at 90°'
            }
        ],
        'skills': [
            {
                'title': 'Quadrilateral Taxonomy & Symmetry Properties',
                'summary': 'Side, angle, and reflective symmetry properties of the six essential four-sided shapes.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Shape</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Side Properties</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Angle Properties</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Lines of Symmetry</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Square</td><td style="padding:6px; border:1px solid #cbd5e1;">4 equal sides, 2 pairs parallel</td><td style="padding:6px; border:1px solid #cbd5e1;">4 right angles (90°)</td><td style="padding:6px; border:1px solid #cbd5e1;">4 lines</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Rectangle</td><td style="padding:6px; border:1px solid #cbd5e1;">Opposite sides equal &amp; parallel</td><td style="padding:6px; border:1px solid #cbd5e1;">4 right angles (90°)</td><td style="padding:6px; border:1px solid #cbd5e1;">2 lines</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Rhombus</td><td style="padding:6px; border:1px solid #cbd5e1;">4 equal sides, opposite parallel</td><td style="padding:6px; border:1px solid #cbd5e1;">Opposite angles equal (not 90°)</td><td style="padding:6px; border:1px solid #cbd5e1;">2 diagonal lines</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Parallelogram</td><td style="padding:6px; border:1px solid #cbd5e1;">Opposite sides equal &amp; parallel</td><td style="padding:6px; border:1px solid #cbd5e1;">Opposite angles equal</td><td style="padding:6px; border:1px solid #cbd5e1;">0 lines</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Trapezium</td><td style="padding:6px; border:1px solid #cbd5e1;">Exactly 1 pair of parallel sides</td><td style="padding:6px; border:1px solid #cbd5e1;">Co-interior angles sum to 180°</td><td style="padding:6px; border:1px solid #cbd5e1;">0 (1 if isosceles)</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Kite</td><td style="padding:6px; border:1px solid #cbd5e1;">2 pairs of adjacent equal sides</td><td style="padding:6px; border:1px solid #cbd5e1;">1 pair of opposite equal angles</td><td style="padding:6px; border:1px solid #cbd5e1;">1 vertical line</td></tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                'title': 'Classification of Triangles by Sides and Angles',
                'summary': 'Distinguishing equilateral, isosceles, scalene, and right-angled triangles.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Equilateral Triangle:</strong> 3 equal sides, 3 equal 60° angles, 3 lines of symmetry.</li>
                    <li><strong>Isosceles Triangle:</strong> 2 equal sides (marked with tick lines), 2 equal base angles, 1 line of symmetry.</li>
                    <li><strong>Scalene Triangle:</strong> All 3 sides and all 3 angles are different; 0 lines of symmetry.</li>
                    <li><strong>Right-Angled Triangle:</strong> Contains one 90° perpendicular corner; can be isosceles (90°, 45°, 45°) or scalene.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Polygon Naming & Regular Symmetry Rule (3 to 10 Sides)',
                'summary': 'Memorizing polygon prefixes and the n-fold symmetry law for regular polygons.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">For any <strong>regular polygon with <em>n</em> sides</strong>, it has exactly <strong><em>n</em> lines of symmetry</strong> and rotational symmetry of <strong>order <em>n</em></strong>:</p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>5 Sides:</strong> Pentagon (Regular = 5 lines of symmetry, interior angle 108°)</li>
                    <li><strong>6 Sides:</strong> Hexagon (Regular = 6 lines of symmetry, interior angle 120°)</li>
                    <li><strong>8 Sides:</strong> Octagon (Regular = 8 lines of symmetry, interior angle 135°)</li>
                    <li><strong>10 Sides:</strong> Decagon (Regular = 10 lines of symmetry, interior angle 144°)</li>
                  </ul>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Hospital Signboard Geometry & Lines of Symmetry (Level 1 Foundation)',
                'marks': '3 Marks (Pearson Edexcel Level 1)',
                'context': 'Facility Signage Wayfinding Design',
                'question': 'An emergency stop signboard is manufactured in the shape of a <strong>regular octagon</strong>.<br>(a) How many sides does an octagon have?<br>(b) How many lines of reflective symmetry does a regular octagon possess?<br>(c) State the order of rotational symmetry of a regular octagon.',
                'steps': [
                    ('Step 1', 'State the number of sides of an octagon', 'An octagon has 8 straight sides.', 'A1: Correct polygon side count (8)'),
                    ('Step 2', 'Determine lines of reflective symmetry', 'A regular polygon with n sides has n lines of symmetry. An 8-sided regular octagon has 8 lines of symmetry.', 'A1: Correct lines of symmetry (8)'),
                    ('Step 3', 'Determine rotational symmetry order', 'A regular octagon matches its outline 8 times in a 360° turn. Order = 8.', 'A1: Correct rotational symmetry order (8)')
                ],
                'final_answer': '(a) 8 sides | (b) 8 lines of symmetry | (c) Rotational symmetry of order 8',
                'tutor_tip': 'For ANY regular polygon, number of sides = lines of symmetry = order of rotational symmetry!'
            },
            {
                'title': 'Architectural Paving Slab Polygon Tessellation Audit (Level 2 Multi-Step)',
                'marks': '4 Marks (Pearson Edexcel Level 2)',
                'context': 'Landscape Architecture & Tessellation',
                'question': 'A courtyard designer arranges <strong>regular hexagonal paving slabs</strong> of side length <strong>25 cm</strong> around a central square feature.<br>• Twenty-four outer edges of the hexagons form the external boundary of the patio.<br>• Steel edging strips are sold in <strong>1.5 m lengths</strong> at <strong>£9.20 per strip</strong>.<br>Calculate the total cost of the steel edging strips required for the 24 outer hexagon edges.',
                'steps': [
                    ('Step 1', 'Calculate total boundary perimeter in cm and convert to metres', '24 edges × 25 cm = 600 cm.<br>600 cm ÷ 100 = 6.0 metres.', 'M1: Boundary length in metres (6.0 m)'),
                    ('Step 2', 'Calculate number of 1.5 m steel strips required', '6.0 m ÷ 1.5 m = 4 strips.', 'M1: Division by strip length (4)'),
                    ('Step 3', 'Calculate total cost of steel edging', '4 × £9.20 = £36.80.', 'A1: Accurate total cost (£36.80)')
                ],
                'final_answer': '£36.80 (4 strips needed for 6.0 m boundary)',
                'tutor_tip': 'Because the hexagons are regular, every single side measures exactly 25 cm.'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Confusing a Parallelogram with Having 2 Lines of Symmetry',
                'desc': 'A standard non-rectangular parallelogram has ZERO lines of reflective symmetry, even though it has rotational symmetry of order 2.',
                'fix': 'Fold it mentally: the corners do not align when folded horizontally, vertically, or diagonally.'
            },
            {
                'title': 'Claiming a Rectangle Has 4 Lines of Symmetry',
                'desc': 'Only a square has 4 lines of symmetry. A rectangle has only 2 (vertical and horizontal midlines; folding along a diagonal does not line up the corners).',
                'fix': 'Remember: Rectangle = 2 lines; Square = 4 lines.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'A ceramic wall tile has <strong>6 equal sides</strong> and <strong>6 equal interior angles</strong>, each side measuring <strong>8 cm</strong>.<br>(a) What is the full mathematical name of this shape?<br>(b) Calculate the perimeter of one tile.',
                'solution_steps': '1. A 6-sided polygon with equal sides and equal angles is a Regular Hexagon.<br>2. Perimeter = 6 × 8 cm = 48 cm.',
                'correct_answer': '(a) Regular Hexagon | (b) 48 cm',
                'tutor_tip': 'Include the word "Regular" whenever all sides and angles are equal.'
            },
            {
                'marks': '3 Marks',
                'question': 'A quadrilateral has <strong>one pair of parallel sides</strong> of lengths <strong>12 cm and 18 cm</strong>, and two equal non-parallel sloping sides of <strong>7 cm each</strong>.<br>(a) Name this specific type of quadrilateral.<br>(b) How many lines of symmetry does it have?<br>(c) Calculate its perimeter.',
                'solution_steps': '1. One pair of parallel sides and equal sloping sides = Isosceles Trapezium.<br>2. An isosceles trapezium has 1 vertical line of symmetry.<br>3. Perimeter = 12 + 18 + 7 + 7 = 44 cm.',
                'correct_answer': '(a) Isosceles Trapezium | (b) 1 line of symmetry | (c) 44 cm',
                'tutor_tip': 'A standard trapezium has 0 lines of symmetry, but an isosceles trapezium (equal slanted sides) has 1.'
            },
            {
                'marks': '3 Marks',
                'question': 'A rectangular metal frame measures <strong>1.2 m long by 0.8 m wide</strong>, with one diagonal brace running from corner to corner of length <strong>1.44 m</strong>.<br>(a) How many right angles (90°) are in the outer rectangular frame?<br>(b) Calculate the total length of steel bar needed to make the outer frame plus the single diagonal brace.',
                'solution_steps': '1. A rectangle has 4 right angles (90°).<br>2. Outer frame perimeter = 2 × (1.2 + 0.8) = 4.0 m.<br>3. Add diagonal brace: 4.0 m + 1.44 m = 5.44 m.',
                'correct_answer': '(a) 4 right angles | (b) 5.44 m',
                'tutor_tip': 'Read carefully whether internal braces are included in the total steel length.'
            }
        ]
    },
    {
        'filename': 'functional-skills-3d-shapes.html',
        'clean_topic': '3D Solids: Faces, Edges & Vertices',
        'intro_lead': 'Identify and classify 3D solids (cuboids, prisms, pyramids, cylinders, cones, spheres), count vertices, edges, and faces accurately, and apply Euler’s polyhedral formula.',
        'next_file': 'functional-skills-nets.html',
        'next_name': 'Nets of 3D Shapes',
        'spec_points': [
            ('L1.20 / L2.22', 'Identify 3D shapes and their geometric properties (faces, edges, vertices) from 2D drawings and workplace models.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-cube',
                'title': 'Golden Rule 1: The Three Properties: Faces, Edges & Vertices',
                'desc': 'Faces = Flat or curved 2D surfaces. Edges = Straight or curved lines where two faces meet. Vertices = Sharp corners (points) where three or more edges meet.',
                'badge': 'Faces = Surfaces • Edges = Lines • Vertices = Corners'
            },
            {
                'icon': 'fa-diagram-project',
                'title': "Golden Rule 2: Prism vs Pyramid Rule & Euler's Formula (F + V - E = 2)",
                'desc': 'For an n-sided Prism: Faces = n + 2, Edges = 3n, Vertices = 2n. For an n-sided Pyramid: Faces = n + 1, Edges = 2n, Vertices = n + 1. For any flat-faced polyhedron: Faces + Vertices − Edges = 2.',
                'badge': 'Prism: F=n+2, E=3n, V=2n • Pyramid: F=n+1, E=2n, V=n+1'
            }
        ],
        'skills': [
            {
                'title': '3D Solids Property Reference Table',
                'summary': 'Complete census of faces, edges, and vertices for every exam solid.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:center;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">3D Solid</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Faces</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Edges</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Vertices</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Cube / Cuboid</td><td style="padding:6px; border:1px solid #cbd5e1;">6</td><td style="padding:6px; border:1px solid #cbd5e1;">12</td><td style="padding:6px; border:1px solid #cbd5e1;">8</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Triangular Prism</td><td style="padding:6px; border:1px solid #cbd5e1;">5</td><td style="padding:6px; border:1px solid #cbd5e1;">9</td><td style="padding:6px; border:1px solid #cbd5e1;">6</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Pentagonal Prism</td><td style="padding:6px; border:1px solid #cbd5e1;">7</td><td style="padding:6px; border:1px solid #cbd5e1;">15</td><td style="padding:6px; border:1px solid #cbd5e1;">10</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Hexagonal Prism</td><td style="padding:6px; border:1px solid #cbd5e1;">8</td><td style="padding:6px; border:1px solid #cbd5e1;">18</td><td style="padding:6px; border:1px solid #cbd5e1;">12</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Square-Based Pyramid</td><td style="padding:6px; border:1px solid #cbd5e1;">5</td><td style="padding:6px; border:1px solid #cbd5e1;">8</td><td style="padding:6px; border:1px solid #cbd5e1;">5</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Triangular Pyramid (Tetrahedron)</td><td style="padding:6px; border:1px solid #cbd5e1;">4</td><td style="padding:6px; border:1px solid #cbd5e1;">6</td><td style="padding:6px; border:1px solid #cbd5e1;">4</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Cylinder</td><td style="padding:6px; border:1px solid #cbd5e1;">3 (2 flat, 1 curved)</td><td style="padding:6px; border:1px solid #cbd5e1;">2 (curved)</td><td style="padding:6px; border:1px solid #cbd5e1;">0</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Cone</td><td style="padding:6px; border:1px solid #cbd5e1;">2 (1 flat, 1 curved)</td><td style="padding:6px; border:1px solid #cbd5e1;">1 (curved)</td><td style="padding:6px; border:1px solid #cbd5e1;">1 (apex)</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Sphere</td><td style="padding:6px; border:1px solid #cbd5e1;">1 (continuous curved)</td><td style="padding:6px; border:1px solid #cbd5e1;">0</td><td style="padding:6px; border:1px solid #cbd5e1;">0</td></tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                'title': 'Prisms vs Pyramids: Cross-Sections & Naming',
                'summary': 'How to distinguish a uniform prism from an apex-converging pyramid.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Prisms Have Uniform Cross-Sections:</strong> A prism has two identical parallel end polygons connected by rectangular sides. Slicing it parallel to the end always reveals the same 2D shape.</li>
                    <li><strong>Pyramids Converge to a Single Apex:</strong> A pyramid has one base polygon and triangular sides that meet at a single top vertex (apex).</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Calculating Total Wireframe / Edge Lengths of 3D Solids',
                'summary': 'Summing all 12 edges of a cuboid or 9 edges of a triangular prism for structural steelwork.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">When building a 3D metal frame or taping all edges of a box:</p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Cube (12 equal edges):</strong> Total Edge Length = <strong>12 &times; Side Length</strong>.</li>
                    <li><strong>Cuboid (4 lengths, 4 widths, 4 heights):</strong> Total Edge Length = <strong>4L + 4W + 4H</strong>.</li>
                    <li><strong>Square-Based Pyramid (8 edges):</strong> Total Edge Length = <strong>(4 &times; Base Edge) + (4 &times; Slant Edge)</strong>.</li>
                  </ul>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Clinical Sharps Bin 3D Geometry Specification (Level 1 Foundation)',
                'marks': '3 Marks (Pearson Edexcel Level 1)',
                'context': 'Healthcare Infection Control Equipment',
                'question': 'A clinical sharps disposal bin is shaped as a <strong>hexagonal prism</strong>.<br>(a) State the 2D shape of its two end faces.<br>(b) How many faces does the hexagonal prism have in total?<br>(c) How many edges and vertices does it have?',
                'steps': [
                    ('Step 1', 'Identify the cross-sectional end faces', 'A hexagonal prism has two identical end faces shaped as hexagons (6-sided polygons).', 'A1: Correct cross-sectional face shape'),
                    ('Step 2', 'Calculate total faces (n + 2)', '2 hexagonal end faces + 6 rectangular side faces = 8 faces in total.', 'A1: Accurate total faces (8)'),
                    ('Step 3', 'Calculate total edges (3n) and vertices (2n)', 'Edges: 6 top + 6 bottom + 6 vertical = 18 edges.<br>Vertices: 6 top + 6 bottom = 12 vertices.', 'A1: Accurate edges (18) and vertices (12)')
                ],
                'final_answer': '(a) Hexagons | (b) 8 faces | (c) 18 edges and 12 vertices',
                'tutor_tip': 'For any prism with an n-sided base: Faces = n + 2, Edges = 3n, Vertices = 2n.'
            },
            {
                'title': 'Exhibition Display Case Aluminium Edge Framing Cost (Level 2 Multi-Step)',
                'marks': '4 Marks (Pearson Edexcel Level 2)',
                'context': 'Retail & Museum Display Fabrication',
                'question': 'A fabricator builds the complete 12-edge aluminium frame for a cuboid glass display case measuring <strong>1.5 m long, 0.8 m wide, and 0.9 m high</strong>.<br>• Aluminium angle bar is sold in <strong>3.5 m lengths</strong> at <strong>£14.50 per length</strong>.<br>Calculate the minimum cost of the aluminium lengths required to build the frame.',
                'steps': [
                    ('Step 1', 'Calculate total length of all 12 edges of the cuboid', 'Total Edge Length = (4 × 1.5 m) + (4 × 0.8 m) + (4 × 0.9 m) = 6.0 + 3.2 + 3.6 = 12.8 metres.', 'M1: Accurate 12-edge sum (12.8 m)'),
                    ('Step 2', 'Divide by 3.5 m stock bar length and round UP', '12.8 m ÷ 3.5 m = 3.657... → Round UP to 4 lengths.', 'M1: Division and rounding up to 4 bars'),
                    ('Step 3', 'Calculate total cost', '4 lengths × £14.50 = £58.00.', 'A1: Accurate total cost (£58.00)')
                ],
                'final_answer': '£58.00 (4 lengths required for 12.8 m total edge framing)',
                'tutor_tip': 'Remember a cuboid has 12 edges in 3 sets of 4: 4 lengths + 4 widths + 4 heights!'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Confusing a Triangular Prism with a Pyramid',
                'desc': 'A triangular prism has 5 faces, 9 edges, and 6 vertices. A square-based pyramid has 5 faces, 8 edges, and 5 vertices.',
                'fix': 'Look for the uniform cross-section: prisms have matching parallel ends; pyramids come to a single point.'
            },
            {
                'title': 'Counting Only 4 Edges Instead of 12 on a Cuboid',
                'desc': 'Adding 1.5 + 0.8 + 0.9 = 3.2 m only counts 3 edges instead of all 12 edges.',
                'fix': 'Multiply the sum of (L + W + H) by 4 to account for all 12 edges.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'A ridge tent is shaped as a <strong>triangular prism</strong>.<br>(a) How many vertices (corners) does it have?<br>(b) How many edges does it have?',
                'solution_steps': '1. Vertices: 3 at front triangle + 3 at back triangle = 6 vertices.<br>2. Edges: 3 at front + 3 at back + 3 connecting ridge/ground poles = 9 edges.',
                'correct_answer': '(a) 6 vertices | (b) 9 edges',
                'tutor_tip': 'Verify with Euler’s formula: Faces (5) + Vertices (6) − Edges (9) = 2.'
            },
            {
                'marks': '3 Marks',
                'question': 'A glass paperweight is shaped as a <strong>square-based pyramid</strong>. Each side of the square base measures <strong>9 cm</strong>, and each of the four sloping edges measures <strong>11 cm</strong>.<br>(a) State the number of faces, edges, and vertices.<br>(b) Calculate the total length of all edges of the pyramid.',
                'solution_steps': '1. Square-based pyramid has 5 faces (1 square + 4 triangles), 8 edges, and 5 vertices.<br>2. Base edges = 4 × 9 cm = 36 cm.<br>3. Sloping edges = 4 × 11 cm = 44 cm.<br>4. Total edge length = 36 + 44 = 80 cm.',
                'correct_answer': '(a) 5 faces, 8 edges, 5 vertices | (b) 80 cm',
                'tutor_tip': 'A square-based pyramid has 4 base edges and 4 sloping edges meeting at the apex.'
            },
            {
                'marks': '3 Marks',
                'question': 'A heavy-duty steel cage is shaped as a cube of side length <strong>1.4 metres</strong>. Calculate the total length of steel bar required to weld all <strong>12 edges</strong> of the cube.',
                'solution_steps': '1. A cube has 12 equal edges.<br>2. Total steel length = 12 × 1.4 m = 16.8 metres.',
                'correct_answer': '16.8 m',
                'tutor_tip': 'Multiply the side length by 12 for a cube wireframe.'
            }
        ]
    },
    {
        'filename': 'functional-skills-plans-and-elevations.html',
        'clean_topic': 'Plans, Elevations & Front/Side Views',
        'intro_lead': 'Interpret and draw 2D orthographic projections: plan views (looking straight down from above), front elevations, and side elevations of architectural buildings and workplace structures.',
        'next_file': 'functional-skills-angles.html',
        'next_name': 'Angles & Bearings',
        'spec_points': [
            ('L1.20 / L2.22', 'Interpret and draw 2D representations of 3D objects including plan views, front elevations, and side elevations on scaled grids.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-eye',
                'title': 'Golden Rule 1: The Three Orthographic Viewing Directions',
                'desc': "Plan View = Looking straight down from above (bird's-eye view: shows Length & Width, NEVER Height). Front Elevation = Looking straight at the front (shows Width & Height). Side Elevation = Looking from the left or right side (shows Depth & Height).",
                'badge': 'Plan = Top (L×W) • Front = Ahead (W×H) • Side = Profile (D×H)'
            },
            {
                'icon': 'fa-border-all',
                'title': 'Golden Rule 2: Convert Real Dimensions Using the Grid Scale Before Drawing',
                'desc': 'Always read the grid key first (e.g. "1 square represents 0.5 m" means a 3 m wall requires 6 grid squares). Draw solid lines for visible step changes in surface level.',
                'badge': 'Grid Squares = Real Dimension ÷ Scale Value of 1 Square'
            }
        ],
        'skills': [
            {
                'title': 'Orthographic Projection Dimension Mapping',
                'summary': 'Which 3D dimensions appear in each of the three 2D views.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:left;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">2D View</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Camera Angle</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Dimensions Shown</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Hidden Dimension</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">Plan View</td><td style="padding:8px; border:1px solid #cbd5e1;">Directly above (Bird's eye)</td><td style="padding:8px; border:1px solid #cbd5e1;">Length (Width) &amp; Depth</td><td style="padding:8px; border:1px solid #cbd5e1;">Height is invisible</td></tr>
                      <tr><td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">Front Elevation</td><td style="padding:8px; border:1px solid #cbd5e1;">Horizontal facing front</td><td style="padding:8px; border:1px solid #cbd5e1;">Front Width &amp; Height</td><td style="padding:8px; border:1px solid #cbd5e1;">Depth is invisible</td></tr>
                      <tr><td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">Side Elevation</td><td style="padding:8px; border:1px solid #cbd5e1;">Horizontal facing side</td><td style="padding:8px; border:1px solid #cbd5e1;">Side Depth &amp; Height</td><td style="padding:8px; border:1px solid #cbd5e1;">Front Width is invisible</td></tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                'title': '2D Projections of Cylinders, Cones, Pyramids & Prisms',
                'summary': 'Recognizing how curved and sloped 3D solids flatten into 2D shapes.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Upright Cylinder:</strong> Plan View = <strong>Circle</strong>; Front Elevation = <strong>Rectangle</strong> (width = diameter, height = cylinder height); Side Elevation = <strong>Rectangle</strong>.</li>
                    <li><strong>Upright Cone:</strong> Plan View = <strong>Circle with central dot</strong> (apex); Front &amp; Side Elevations = <strong>Isosceles Triangle</strong>.</li>
                    <li><strong>Square-Based Pyramid:</strong> Plan View = <strong>Square with two intersecting diagonals</strong>; Front &amp; Side Elevations = <strong>Isosceles Triangle</strong>.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Stepped & L-Shaped Building Elevations',
                'summary': 'Drawing internal split lines where a surface steps back or changes height.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">When looking at a stepped building (e.g. a 2-storey block of height 6 m with a 1-storey porch of height 3 m sticking out at the front):</p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li>The <strong>Front Elevation</strong> shows the full outer rectangle PLUS a horizontal line at 3 m height where the porch roof meets the main wall.</li>
                    <li>The <strong>Plan View</strong> shows the main roof rectangle PLUS the porch roof rectangle separated by a solid line.</li>
                  </ul>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Hospital Emergency Generator Enclosure Orthographic Projections (Level 1 Foundation)',
                'marks': '3 Marks (Pearson Edexcel Level 1)',
                'context': 'Healthcare Facility Engineering Plans',
                'question': 'A backup diesel generator housing is a cuboid measuring <strong>4.0 m long (front), 2.5 m deep (side), and 2.0 m high</strong>.<br>(a) State the 2D shape and dimensions of the Plan View.<br>(b) State the 2D shape and dimensions of the Front Elevation.<br>(c) State the 2D shape and dimensions of the Side Elevation.',
                'steps': [
                    ('Step 1', 'Determine Plan View (Length × Depth)', 'Viewed from above: a rectangle measuring 4.0 m by 2.5 m.', 'A1: Accurate plan view (4.0 m × 2.5 m)'),
                    ('Step 2', 'Determine Front Elevation (Length × Height)', 'Viewed from the front: a rectangle measuring 4.0 m wide by 2.0 m high.', 'A1: Accurate front elevation (4.0 m × 2.0 m)'),
                    ('Step 3', 'Determine Side Elevation (Depth × Height)', 'Viewed from the side: a rectangle measuring 2.5 m deep by 2.0 m high.', 'A1: Accurate side elevation (2.5 m × 2.0 m)')
                ],
                'final_answer': '(a) Plan: 4.0 m × 2.5 m rectangle | (b) Front: 4.0 m × 2.0 m rectangle | (c) Side: 2.5 m × 2.0 m rectangle',
                'tutor_tip': 'Plan view NEVER includes height; front view NEVER includes depth.'
            },
            {
                'title': 'Gable-Roofed Modular Pharmacy Store Front Elevation Area & Cladding (Level 2 Multi-Step)',
                'marks': '4 Marks (Pearson Edexcel Level 2)',
                'context': 'Modular Healthcare Building Construction',
                'question': 'An architectural drawing shows the <strong>Front Elevation</strong> of a modular pharmacy building on a grid where <strong>1 square = 0.5 m</strong>.<br>• On the grid, the front wall is a rectangle <strong>12 squares wide by 6 squares high</strong>, topped by a triangular roof gable that rises an additional <strong>4 squares</strong> to a central peak.<br>• Insulated cladding panels for this front elevation cost <strong>£45.00 per m²</strong>.<br>Calculate the total cost to clad the entire front elevation.',
                'steps': [
                    ('Step 1', 'Convert grid squares into real-world metres (× 0.5 m)', 'Width = 12 × 0.5 m = 6.0 m.<br>Wall Height = 6 × 0.5 m = 3.0 m.<br>Triangle Gable Height = 4 × 0.5 m = 2.0 m.', 'M1: Accurate conversion from grid squares to metres'),
                    ('Step 2', 'Calculate area of rectangular wall + triangular gable', 'Rectangle Area = 6.0 m × 3.0 m = 18.0 m².<br>Triangle Area = (6.0 m × 2.0 m) ÷ 2 = 6.0 m².<br>Total Front Elevation Area = 18.0 + 6.0 = 24.0 m².', 'M1: Compound elevation area (24.0 m²)'),
                    ('Step 3', 'Multiply total area by £45.00 per m²', '24.0 m² × £45.00 = £1,080.00.', 'A1: Accurate total cladding cost (£1,080.00)')
                ],
                'final_answer': '£1,080.00 (Total front elevation area = 24.0 m²)',
                'tutor_tip': 'Convert grid squares into metres BEFORE calculating area so you do not get caught out by square grid units!'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Including Height in the Plan View',
                'desc': 'Drawing the vertical height on a plan view is a classic mistake—looking straight down from the sky only reveals length and width.',
                'fix': 'Think: Plan = Floorplan (Length and Width only).'
            },
            {
                'title': 'Forgetting the Internal Step Line on Stepped Blocks',
                'desc': 'Drawing only the outer outline of an L-shaped block in the front elevation without the horizontal step line loses 1 mark.',
                'fix': 'Any change in depth or height visible from your viewing direction must be drawn as a solid straight line.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'An upright cylindrical water storage tank has a <strong>diameter of 3.2 m</strong> and a <strong>height of 4.5 m</strong>.<br>(a) What 2D shape and measurement is its Plan View?<br>(b) What 2D shape and dimensions is its Front Elevation?',
                'solution_steps': '1. Plan view from above = Circle of diameter 3.2 m (radius 1.6 m).<br>2. Front elevation from the side = Rectangle measuring 3.2 m wide by 4.5 m high.',
                'correct_answer': '(a) Circle (diameter 3.2 m) | (b) Rectangle (3.2 m wide × 4.5 m high)',
                'tutor_tip': 'Looking horizontally at a cylinder from the front or side produces a flat rectangle.'
            },
            {
                'marks': '3 Marks',
                'question': 'An architect draws the Side Elevation of a warehouse measuring <strong>15 m deep by 6.5 m high</strong> on centimetre squared paper using a scale of <strong>1 cm represents 2.5 m</strong>. Calculate the width and height of the rectangle drawn on the grid in cm.',
                'solution_steps': '1. Grid width = 15 m ÷ 2.5 m = 6 cm.<br>2. Grid height = 6.5 m ÷ 2.5 m = 2.6 cm.',
                'correct_answer': '6 cm wide by 2.6 cm high',
                'tutor_tip': 'Divide each real-world dimension by 2.5 m to find the grid length in cm.'
            },
            {
                'marks': '3 Marks',
                'question': 'A concrete loading ramp is a right-angled triangular prism of <strong>width 2.0 m, horizontal base depth 4.8 m, vertical back height 1.4 m, and sloping ramp length 5.0 m</strong>. State the exact dimensions of the <strong>Plan View</strong> when viewed directly from above.',
                'solution_steps': '1. Looking straight down from above, the sloping ramp projects onto its horizontal base footprint.<br>2. Plan view is a rectangle of width 2.0 m by horizontal depth 4.8 m.',
                'correct_answer': 'Rectangle measuring 2.0 m by 4.8 m',
                'tutor_tip': 'From directly above, a sloped ramp appears as its horizontal footprint (4.8 m), not its 5.0 m slant length!'
            }
        ]
    },
    {
        'filename': 'functional-skills-angles.html',
        'clean_topic': 'Angles, Bearings & Turn Navigation',
        'intro_lead': 'Measure and calculate angles on straight lines, around a point, and vertically opposite angles, and calculate 3-figure compass bearings and back bearings for maritime and air ambulance navigation.',
        'next_file': 'functional-skills-angles-in-2d-shapes.html',
        'next_name': 'Angles in Polygons',
        'spec_points': [
            ('L1.21 / L2.23', 'Measure, classify, and calculate missing angles on straight lines (180°) and around a point (360°).'),
            ('L2.23', 'Understand and use 3-figure bearings measured clockwise from North, including reverse (back) bearings.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-compass',
                'title': 'Golden Rule 1: The Three Iron Rules of Three-Figure Bearings',
                'desc': '1. Always measure from NORTH (000°). 2. Always measure CLOCKWISE. 3. Always write as THREE DIGITS (e.g. 045°, 008°, 235°).',
                'badge': 'From North (000°) • Clockwise • 3 Digits (e.g. 065°)'
            },
            {
                'icon': 'fa-lines-leaning',
                'title': 'Golden Rule 2: Straight Line = 180° | Full Point = 360° | Back Bearing = ±180°',
                'desc': 'Angles on a straight line add to 180°. Angles around a point add to 360°. To find a reverse (back) bearing: if the forward bearing is under 180°, ADD 180°; if over 180°, SUBTRACT 180°.',
                'badge': 'Straight Line = 180° • Point = 360° • Back Bearing = Forward ± 180°'
            }
        ],
        'skills': [
            {
                'title': 'Angle Classification & Core Point/Line Rules',
                'summary': 'Acute, right, obtuse, straight, and reflex angle definitions and missing angle rules.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Acute Angle:</strong> Less than 90° (e.g. 42°).</li>
                    <li><strong>Right Angle:</strong> Exactly 90° (quarter turn, marked with a square corner).</li>
                    <li><strong>Obtuse Angle:</strong> Between 90° and 180° (e.g. 135°).</li>
                    <li><strong>Straight Line:</strong> Exactly 180° (half turn). Missing angle on a line = <strong>180° &minus; known angles</strong>.</li>
                    <li><strong>Reflex Angle:</strong> Between 180° and 360° (e.g. 240°).</li>
                    <li><strong>Vertically Opposite Angles:</strong> Where two straight lines cross (X-shape), opposite angles are equal.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': '8-Point Compass Bearings Reference Table',
                'summary': 'Converting cardinal and intercardinal compass directions into 3-figure bearings.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:center;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Compass Point</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">3-Figure Bearing</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Compass Point</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">3-Figure Bearing</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">North (N)</td><td style="padding:6px; border:1px solid #cbd5e1;">000° (or 360°)</td><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">South (S)</td><td style="padding:6px; border:1px solid #cbd5e1;">180°</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">North-East (NE)</td><td style="padding:6px; border:1px solid #cbd5e1;">045°</td><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">South-West (SW)</td><td style="padding:6px; border:1px solid #cbd5e1;">225°</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">East (E)</td><td style="padding:6px; border:1px solid #cbd5e1;">090°</td><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">West (W)</td><td style="padding:6px; border:1px solid #cbd5e1;">270°</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">South-East (SE)</td><td style="padding:6px; border:1px solid #cbd5e1;">135°</td><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">North-West (NW)</td><td style="padding:6px; border:1px solid #cbd5e1;">315°</td></tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                'title': 'Calculating Reverse (Back) Bearings',
                'summary': 'Finding the exact return bearing from destination B back to origin A.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Case 1 — Forward Bearing &lt; 180°:</strong> <strong>ADD 180°</strong>.<br><em>Example: Bearing of B from A is <strong>068°</strong> &rarr; Bearing of A from B = 068° + 180° = <strong>248°</strong>.</em></li>
                    <li><strong>Case 2 — Forward Bearing &gt; 180°:</strong> <strong>SUBTRACT 180°</strong> (and pad to 3 digits if under 100°).<br><em>Example: Bearing of B from A is <strong>252°</strong> &rarr; Bearing of A from B = 252° &minus; 180° = <strong>072°</strong>.</em></li>
                  </ul>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'CCTV Security Camera Sweep Angle Calculation (Level 1 Foundation)',
                'marks': '3 Marks (Pearson Edexcel Level 1)',
                'context': 'Hospital Perimeter Security Monitoring',
                'question': 'A 360° panoramic security dome camera is divided into four monitoring zones around a central point. Zone A covers <strong>95°</strong>, Zone B covers <strong>110°</strong>, and Zone C covers <strong>82°</strong>.<br>(a) Calculate the angle covered by Zone D.<br>(b) State whether Zone D is an acute, obtuse, or reflex angle.',
                'steps': [
                    ('Step 1', 'Sum the three known zone angles', '95° + 110° + 82° = 287°.', 'M1: Summing known angles around a point'),
                    ('Step 2', 'Subtract from 360° (full turn around a point)', '360° − 287° = 73°.', 'A1: Accurate angle for Zone D (73°)'),
                    ('Step 3', 'Classify 73°', 'Since 73° is less than 90°, it is an ACUTE angle.', 'A1: Correct classification (Acute)')
                ],
                'final_answer': '(a) Zone D = 73° | (b) Acute angle',
                'tutor_tip': 'Angles around a central point always add up to a full circle of 360°.'
            },
            {
                'title': 'Air Ambulance Flight Navigation & Back Bearing (Level 2 Multi-Step)',
                'marks': '4 Marks (Pearson Edexcel Level 2)',
                'context': 'Emergency Medical Helicopter Dispatch',
                'question': 'An emergency air ambulance takes off from Hospital Helipad H and flies <strong>45 km</strong> on a bearing of <strong>074°</strong> to an incident site A.<br>(a) Calculate the 3-figure back bearing required to fly directly from incident site A back to Hospital Helipad H.<br>(b) On a radar map with scale <strong>1 cm : 6 km</strong>, what is the plotted distance between H and A in cm?',
                'steps': [
                    ('Step 1', 'Apply the back-bearing rule for 074° (< 180°)', 'Since 074° is less than 180°, add 180°: 074° + 180° = 254°.', 'M1: Adding 180° for reverse bearing'),
                    ('Step 2', 'State return bearing in 3-figure format', 'Return bearing from A to H = 254°.', 'A1: Accurate 3-figure bearing (254°)'),
                    ('Step 3', 'Calculate radar map distance using scale 1 cm : 6 km', '45 km ÷ 6 km = 7.5 cm.', 'M1 / A1: Accurate scaled distance (7.5 cm)')
                ],
                'final_answer': '(a) Return bearing = 254° | (b) Map distance = 7.5 cm',
                'tutor_tip': 'Always check which location comes after the word "FROM": "bearing of H FROM A" means stand at A, face North, and turn clockwise.'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Writing Bearings with Only Two Digits',
                'desc': 'Writing "74°" instead of "074°" forfeits the bearing accuracy mark.',
                'fix': 'Always pad bearings under 100° with a leading zero (e.g. 009°, 045°, 074°).'
            },
            {
                'title': 'Measuring Anti-Clockwise from North or Measuring from South/East',
                'desc': 'Measuring 60° West of North and writing 060° instead of 360° − 60° = 300°.',
                'fix': 'If given an angle West of North (anti-clockwise), subtract it from 360° to get the clockwise bearing.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'Two straight conveyor tracks cross each other. One of the four angles formed at the intersection is <strong>64°</strong>. Calculate the size of the obtuse angle next to it on the straight line.',
                'solution_steps': '1. Angles on a straight line sum to 180°.<br>2. 180° − 64° = 116°.',
                'correct_answer': '116°',
                'tutor_tip': 'Check: 116° + 64° = 180°.'
            },
            {
                'marks': '2 Marks',
                'question': 'A coastguard lifeboat sails from Harbour P to a fishing vessel Q on a bearing of <strong>218°</strong>. Calculate the 3-figure bearing of Harbour P from vessel Q.',
                'solution_steps': '1. Since 218° > 180°, subtract 180°: 218° − 180° = 38°.<br>2. Write in mandatory 3-figure format: 038°.',
                'correct_answer': '038°',
                'tutor_tip': 'Do not forget the leading zero on 038°!'
            },
            {
                'marks': '3 Marks',
                'question': 'A radar dish points due North (000°). It rotates <strong>135° clockwise</strong>, then rotates <strong>48° anti-clockwise</strong>. What is its final 3-figure bearing?',
                'solution_steps': '1. Clockwise turn from 000° = 135°.<br>2. Anti-clockwise turn subtracts angle: 135° − 48° = 87°.<br>3. Write as 3-figure bearing: 087°.',
                'correct_answer': '087°',
                'tutor_tip': 'Clockwise = Add (+); Anti-clockwise = Subtract (−).'
            }
        ]
    },
    {
        'filename': 'functional-skills-angles-in-2d-shapes.html',
        'clean_topic': 'Angles in Triangles, Quadrilaterals & Polygons',
        'intro_lead': 'Calculate missing interior and exterior angles in equilateral, isosceles, and right-angled triangles, quadrilaterals, and regular polygons.',
        'next_file': 'functional-skills-circles.html',
        'next_name': 'Circles & Circumference',
        'spec_points': [
            ('L1.21 / L2.23', 'Calculate missing interior angles in triangles and quadrilaterals.'),
            ('L2.23', 'Calculate interior and exterior angles of regular and irregular polygons.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-draw-polygon',
                'title': 'Golden Rule 1: Total Interior Angles = (n − 2) × 180°',
                'desc': 'To find the sum of all interior angles inside any n-sided polygon: subtract 2 from the number of sides, then multiply by 180°. Triangle (3) = 180°; Quadrilateral (4) = 360°; Pentagon (5) = 540°; Hexagon (6) = 720°; Octagon (8) = 1,080°.',
                'badge': 'Sum of Interior Angles = (Sides − 2) × 180°'
            },
            {
                'icon': 'fa-circle',
                'title': 'Golden Rule 2: Exterior Angles Always Sum to 360° (Fastest Regular Polygon Trick)',
                'desc': 'The exterior angles of ANY polygon always add up to 360°. For a regular polygon with n sides: One Exterior Angle = 360° ÷ n, and One Interior Angle = 180° − Exterior Angle.',
                'badge': 'Exterior Angle = 360° ÷ n • Interior Angle = 180° − Exterior'
            }
        ],
        'skills': [
            {
                'title': 'Triangle Missing Angle Methods (Equilateral, Isosceles & Right-Angled)',
                'summary': 'Solving all three classic exam triangle configurations.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Scalene / General Triangle:</strong> Subtract the two known angles from 180° (e.g. 180° &minus; 65° &minus; 48° = 67°).</li>
                    <li><strong>Isosceles Given Top Apex Angle (e.g. 50°):</strong> Subtract from 180° and divide by 2 for the two equal base angles: (180° &minus; 50°) &divide; 2 = 65° each.</li>
                    <li><strong>Isosceles Given One Base Angle (e.g. 70°):</strong> The other base angle is also 70°; Top angle = 180° &minus; (70° + 70°) = 40°.</li>
                    <li><strong>Right-Angled Triangle:</strong> One angle is 90° (square symbol), so the other two acute angles sum to 90°.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Quadrilateral Interior Angles (Sum = 360°)',
                'summary': 'Finding missing angles in trapeziums, parallelograms, kites, and irregular 4-sided plots.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">Every 4-sided shape can be split into 2 triangles (2 &times; 180° = <strong>360°</strong>):</p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Irregular Quadrilateral:</strong> Add the 3 known angles and subtract from 360°.</li>
                    <li><strong>Parallelogram / Rhombus:</strong> Opposite angles are equal, and adjacent angles between parallel lines add up to <strong>180°</strong>.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Regular Polygon Angle Reference Table',
                'summary': 'Angle sums, single exterior angles, and single interior angles for key regular polygons.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:center;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Regular Polygon</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Sides (n)</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Total Interior Sum</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">1 Exterior Angle (360°&divide;n)</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">1 Interior Angle</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Equilateral Triangle</td><td style="padding:6px; border:1px solid #cbd5e1;">3</td><td style="padding:6px; border:1px solid #cbd5e1;">180°</td><td style="padding:6px; border:1px solid #cbd5e1;">120°</td><td style="padding:6px; border:1px solid #cbd5e1;">60°</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Square</td><td style="padding:6px; border:1px solid #cbd5e1;">4</td><td style="padding:6px; border:1px solid #cbd5e1;">360°</td><td style="padding:6px; border:1px solid #cbd5e1;">90°</td><td style="padding:6px; border:1px solid #cbd5e1;">90°</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Regular Pentagon</td><td style="padding:6px; border:1px solid #cbd5e1;">5</td><td style="padding:6px; border:1px solid #cbd5e1;">540°</td><td style="padding:6px; border:1px solid #cbd5e1;">72°</td><td style="padding:6px; border:1px solid #cbd5e1;">108°</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Regular Hexagon</td><td style="padding:6px; border:1px solid #cbd5e1;">6</td><td style="padding:6px; border:1px solid #cbd5e1;">720°</td><td style="padding:6px; border:1px solid #cbd5e1;">60°</td><td style="padding:6px; border:1px solid #cbd5e1;">120°</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Regular Octagon</td><td style="padding:6px; border:1px solid #cbd5e1;">8</td><td style="padding:6px; border:1px solid #cbd5e1;">1,080°</td><td style="padding:6px; border:1px solid #cbd5e1;">45°</td><td style="padding:6px; border:1px solid #cbd5e1;">135°</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Regular Decagon</td><td style="padding:6px; border:1px solid #cbd5e1;">10</td><td style="padding:6px; border:1px solid #cbd5e1;">1,440°</td><td style="padding:6px; border:1px solid #cbd5e1;">36°</td><td style="padding:6px; border:1px solid #cbd5e1;">144°</td></tr>
                    </tbody>
                  </table>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Architectural Roof Gable Truss Angle Calculation (Level 1 Foundation)',
                'marks': '3 Marks (Pearson Edexcel Level 1)',
                'context': 'Construction Timber Roof Truss Design',
                'question': 'A timber roof truss forms an <strong>isosceles triangle</strong>. The top ridge angle between the two equal rafters is <strong>76°</strong>.<br>Calculate the size of each of the two identical base angles at the eaves.',
                'steps': [
                    ('Step 1', 'Recall total interior angle sum of a triangle', 'Interior angles of a triangle sum to 180°.', 'B1: Triangle angle sum property (180°)'),
                    ('Step 2', 'Subtract known ridge angle from 180°', '180° − 76° = 104° remaining for both base angles.', 'M1: Angle difference calculation (104°)'),
                    ('Step 3', 'Divide remainder by 2 for the identical base angles', '104° ÷ 2 = 52°.', 'A1: Accurate base angle size (52°)')
                ],
                'final_answer': 'Each base angle = 52°',
                'tutor_tip': 'Check: 52° + 52° + 76° = 180°. Both base angles are equal because it is an isosceles triangle.'
            },
            {
                'title': 'Hexagonal Gazebo Paving & Mitre Saw Cut Angle (Level 2 Multi-Step)',
                'marks': '4 Marks (Pearson Edexcel Level 2)',
                'context': 'Hospital Garden Gazebo Carpentry',
                'question': 'A carpenter builds a timber gazebo deck in the shape of a <strong>regular hexagon (6 sides)</strong>.<br>(a) Calculate the total sum of the interior angles of the hexagon.<br>(b) Calculate the size of one interior corner angle.<br>(c) Each corner joint is made by mitre-cutting two timber beams equally so they meet at the corner angle. At what angle must each beam be cut?',
                'steps': [
                    ('Step 1', 'Calculate interior angle sum: (n − 2) × 180°', '(6 − 2) × 180° = 4 × 180° = 720°.', 'M1: Interior angle sum (720°)'),
                    ('Step 2', 'Divide by 6 sides to find one interior angle', '720° ÷ 6 = 120° (or Exterior = 360° ÷ 6 = 60°; Interior = 180° − 60° = 120°).', 'M1: Single interior angle (120°)'),
                    ('Step 3', 'Halve the corner angle for the two mitred beams', '120° ÷ 2 = 60° per timber beam.', 'A1: Accurate mitre cut angle (60°)')
                ],
                'final_answer': '(a) 720° | (b) 120° | (c) 60° mitre cut per beam',
                'tutor_tip': 'Using Exterior = 360° ÷ 6 = 60° then Interior = 180° − 60° = 120° is a lightning-fast check!'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Multiplying n × 180° Instead of (n − 2) × 180°',
                'desc': 'Doing 6 × 180° = 1,080° for a hexagon instead of (6 − 2) × 180° = 720°.',
                'fix': 'Always subtract 2 from the number of sides first, or use the exterior angle method (360° ÷ n).'
            },
            {
                'title': 'Forgetting the Right-Angle Square Symbol Means 90°',
                'desc': 'Diagrams rarely write "90°" in digits; they show a small square box in the corner.',
                'fix': 'As soon as you see a square corner symbol, write "90°" next to it on the diagram.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'An irregular four-sided parking bay (quadrilateral) has three interior angles measuring <strong>90°, 115°, and 78°</strong>. Calculate the size of the fourth interior angle.',
                'solution_steps': '1. Sum of known angles = 90° + 115° + 78° = 283°.<br>2. Fourth angle = 360° − 283° = 77°.',
                'correct_answer': '77°',
                'tutor_tip': 'Angles in any 4-sided quadrilateral always add up to 360°.'
            },
            {
                'marks': '3 Marks',
                'question': 'Calculate the size of:<br>(a) One exterior angle of a <strong>regular pentagon</strong> (5 sides).<br>(b) One interior angle of a <strong>regular pentagon</strong>.',
                'solution_steps': '1. Exterior angle = 360° ÷ 5 = 72°.<br>2. Interior angle = 180° − 72° = 108°.',
                'correct_answer': '(a) 72° | (b) 108°',
                'tutor_tip': 'Interior + Exterior at any vertex always lies on a straight line (180°).'
            },
            {
                'marks': '3 Marks',
                'question': 'A right-angled triangular ramp has a <strong>90° corner</strong> and an elevation angle of <strong>18°</strong> at the base. Calculate the size of the top acute angle.',
                'solution_steps': '1. Sum of known angles = 90° + 18° = 108°.<br>2. Top angle = 180° − 108° = 72°.',
                'correct_answer': '72°',
                'tutor_tip': 'In a right-angled triangle, the two acute angles always add up to 90° (90° − 18° = 72°).'
            }
        ]
    },
    {
        'filename': 'functional-skills-circles.html',
        'clean_topic': 'Circles: Radius, Diameter, Circumference & Area',
        'intro_lead': 'Calculate the circumference (perimeter) and area of circles, semi-circles, quarter-circles, and stadium compound shapes using π (3.14 or 3.142) in landscaping and healthcare equipment design.',
        'next_file': 'functional-skills-coordinates.html',
        'next_name': 'Coordinates',
        'spec_points': [
            ('L2.16 / L2.25', 'Calculate the circumference and arc lengths of circles and composite shapes using given approximations of pi (3.14 or 3.142).'),
            ('L2.17 / L2.25', 'Calculate the area of circles, semi-circles, and circular rings/sectors in practical costing scenarios.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-circle',
                'title': 'Golden Rule 1: Circumference = π × d | Area = π × r² (Halve Diameter First!)',
                'desc': 'Circumference (distance around the outside rim) = 3.14 × Diameter. Area (flat space inside) = 3.14 × Radius × Radius. If the question gives you the Diameter, you MUST divide it by 2 to get the Radius before calculating Area!',
                'badge': 'Circumference = π × d • Area = π × r × r (where r = d ÷ 2)'
            },
            {
                'icon': 'fa-arrows-left-right',
                'title': 'Golden Rule 2: Semi-Circle Perimeter Includes the Straight Diameter Edge',
                'desc': 'The curved arc of a semi-circle is (π × d) ÷ 2. To enclose a semi-circular patio with edging, you MUST add the straight flat diameter across the bottom: Total Perimeter = ((π × d) ÷ 2) + d.',
                'badge': 'Semi-Circle Perimeter = (π × d ÷ 2) + Diameter'
            }
        ],
        'skills': [
            {
                'title': 'Radius vs Diameter & Full Circle Formulas',
                'summary': 'Distinguishing radius from diameter and avoiding the squaring trap.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Radius (<em>r</em>):</strong> Distance from the center point to the outer edge (e.g. 5 m).</li>
                    <li><strong>Diameter (<em>d</em>):</strong> Full distance straight across through the center (e.g. 10 m). <strong><em>d</em> = 2<em>r</em></strong> and <strong><em>r</em> = <em>d</em> &divide; 2</strong>.</li>
                    <li><strong>Squaring Trap Warning:</strong> <em>r</em>&sup2; means <strong><em>r</em> &times; <em>r</em></strong> (e.g. 5 &times; 5 = 25), NEVER 5 &times; 2!</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Semi-Circles & Quarter-Circles (Sectors)',
                'summary': 'Calculating areas and full boundary perimeters of half and quarter circles.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:left;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Shape</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Area Formula</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Total Perimeter Formula</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">Full Circle</td><td style="padding:8px; border:1px solid #cbd5e1;">&pi; &times; r &times; r</td><td style="padding:8px; border:1px solid #cbd5e1;">&pi; &times; d</td></tr>
                      <tr><td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">Semi-Circle (Half)</td><td style="padding:8px; border:1px solid #cbd5e1;">(&pi; &times; r &times; r) &divide; 2</td><td style="padding:8px; border:1px solid #cbd5e1;">((&pi; &times; d) &divide; 2) + d</td></tr>
                      <tr><td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">Quarter-Circle</td><td style="padding:8px; border:1px solid #cbd5e1;">(&pi; &times; r &times; r) &divide; 4</td><td style="padding:8px; border:1px solid #cbd5e1;">((&pi; &times; d) &divide; 4) + 2r</td></tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                'title': 'Compound Stadium Shapes (Rectangle + Two Semi-Circular Ends)',
                'summary': 'Combining two semi-circles into one complete circle to save working time.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">A running track, conference table, or pill-shaped flowerbed consists of a central rectangle with <strong>two semi-circular ends</strong>:</p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Two Semi-Circles = 1 Full Circle!</strong> Do not halve and then double—simply calculate 1 full circle of diameter equal to the rectangle's width.</li>
                    <li><strong>Total Area:</strong> (Rectangle Length &times; Width) + (&pi; &times; r&sup2;).</li>
                    <li><strong>Total Outer Perimeter:</strong> (2 &times; Straight Length) + (&pi; &times; d). <em>(Do not include the internal dashed join lines!)</em></li>
                  </ul>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Hospital Sensory Garden Circular Turf & Edging (Level 1/2 Foundation)',
                'marks': '3 Marks (Pearson Edexcel Level 2)',
                'context': 'Healthcare Facility Therapeutic Garden Landscaping',
                'question': 'A hospital wellbeing garden features a circular lawn with a <strong>diameter of 12 metres</strong>. Use <strong>π = 3.14</strong>.<br>(a) Calculate the area of turf needed in m².<br>(b) Calculate the length of metal edging required to surround the circular perimeter.',
                'steps': [
                    ('Step 1', 'Halve diameter to find the radius', 'Radius = 12 m ÷ 2 = 6 metres.', 'B1: Radius identification (6 m)'),
                    ('Step 2', 'Calculate Area = 3.14 × r × r', 'Area = 3.14 × 6 × 6 = 3.14 × 36 = 113.04 m².', 'M1: Accurate area calculation (113.04 m²)'),
                    ('Step 3', 'Calculate Circumference = 3.14 × Diameter', 'Circumference = 3.14 × 12 m = 37.68 metres.', 'A1: Accurate circumference (37.68 m)')
                ],
                'final_answer': '(a) Area = 113.04 m² | (b) Edging Length = 37.68 m',
                'tutor_tip': 'For Area, multiply radius by itself first (6 × 6 = 36), then by 3.14. For Circumference, multiply 3.14 by the full diameter (12).'
            },
            {
                'title': 'Semi-Circular Therapy Patio Paving & Border Costing (Level 2 Multi-Step)',
                'marks': '4 Marks (Pearson Edexcel Level 2)',
                'context': 'Rehabilitation Courtyard Construction',
                'question': 'A builder constructs a <strong>semi-circular patio</strong> with a straight back wall of <strong>diameter 8.0 metres</strong>. Use <strong>π = 3.14</strong>.<br>• Flexible rubber safety edging is fitted around the entire boundary (both the curved arc AND the straight back edge).<br>• Edging is sold in <strong>3 m rolls</strong> at <strong>£16.50 per roll</strong>.<br>Calculate the total cost of the edging rolls required.',
                'steps': [
                    ('Step 1', 'Calculate the curved semi-circular arc length', 'Curved Arc = (3.14 × 8.0 m) ÷ 2 = 25.12 ÷ 2 = 12.56 metres.', 'M1: Curved arc calculation (12.56 m)'),
                    ('Step 2', 'Add the straight 8.0 m diameter edge for total perimeter', 'Total Perimeter = 12.56 m + 8.0 m = 20.56 metres.', 'M1: Adding straight diameter edge (20.56 m)'),
                    ('Step 3', 'Divide by 3 m roll length and round UP', 'Rolls = 20.56 m ÷ 3 m = 6.853... → Round UP to 7 rolls.', 'M1: Division and rounding up to 7 rolls'),
                    ('Step 4', 'Calculate total cost', '7 rolls × £16.50 = £115.50.', 'A1: Accurate total cost (£115.50)')
                ],
                'final_answer': '£115.50 (7 rolls required for 20.56 m perimeter)',
                'tutor_tip': 'Never forget the straight diameter edge when finding the total perimeter of a semi-circle!'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Using Diameter in the Area Formula Without Halving',
                'desc': 'Computing 3.14 × 12² = 452.16 m² instead of 3.14 × 6² = 113.04 m² makes your answer 4 times too large!',
                'fix': 'Always write "d = ... , r = ..." on your first line of working.'
            },
            {
                'title': 'Multiplying Radius by 2 Instead of Squaring It',
                'desc': 'Calculating r² for r = 6 as 6 × 2 = 12 instead of 6 × 6 = 36.',
                'fix': 'Write the formula out as "Area = 3.14 × r × r" so you physically type the radius twice.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'A circular rehabilitation hydrotherapy pool has a <strong>radius of 3.5 metres</strong>. Using <strong>π = 3.14</strong>, calculate:<br>(a) The circumference of the pool.<br>(b) The surface area of the pool (to 2 decimal places).',
                'solution_steps': '1. Diameter = 3.5 × 2 = 7.0 m. Circumference = 3.14 × 7.0 = 21.98 m.<br>2. Area = 3.14 × 3.5 × 3.5 = 3.14 × 12.25 = 38.465 m² → 38.47 m².',
                'correct_answer': '(a) 21.98 m | (b) 38.47 m² (or 38.465 m²)',
                'tutor_tip': 'Double the radius (3.5 × 2 = 7.0 m) before finding circumference.'
            },
            {
                'marks': '3 Marks',
                'question': 'A semi-circular reception desk top has a straight back edge (diameter) of <strong>2.4 metres</strong>. Using <strong>π = 3.14</strong>, calculate the top surface area of the desk in m² (to 2 decimal places).',
                'solution_steps': '1. Radius = 2.4 m ÷ 2 = 1.2 m.<br>2. Full circle area = 3.14 × 1.2 × 1.2 = 4.5216 m².<br>3. Semi-circle area = 4.5216 ÷ 2 = 2.2608 m² → 2.26 m².',
                'correct_answer': '2.26 m²',
                'tutor_tip': 'Remember to divide the full circle area by 2 for a semi-circle.'
            },
            {
                'marks': '4 Marks',
                'question': 'An athletics track consists of a central rectangle measuring <strong>80 m long by 40 m wide</strong>, with <strong>two semi-circular ends</strong> of diameter 40 m. Using <strong>π = 3.14</strong>, calculate:<br>(a) The total outer perimeter of the track.<br>(b) The total area enclosed inside the track.',
                'solution_steps': '1. Two semi-circular arcs = 1 full circle circumference: 3.14 × 40 m = 125.6 m.<br>2. Add the two straight 80 m sides: 125.6 + 80 + 80 = 285.6 m.<br>3. Rectangle area = 80 × 40 = 3,200 m².<br>4. Two semi-circles area = 1 full circle (r = 20 m): 3.14 × 20 × 20 = 1,256 m².<br>5. Total Area = 3,200 + 1,256 = 4,456 m².',
                'correct_answer': '(a) Perimeter = 285.6 m | (b) Total Area = 4,456 m²',
                'tutor_tip': 'Do NOT include the two 40 m internal join lines in the outer perimeter!'
            }
        ]
    },
    {
        'filename': 'functional-skills-coordinates.html',
        'clean_topic': 'Coordinates: Positive & Four Quadrants',
        'intro_lead': 'Plot and read coordinates in all four quadrants (x, y), find midpoints of line segments, and identify missing vertices of geometric shapes on Cartesian grids.',
        'next_file': 'functional-skills-maps-and-scale-drawings.html',
        'next_name': 'Maps & Scale Drawings',
        'spec_points': [
            ('L1.22 / L2.26', 'Use coordinates in 2D grids (both positive and all four quadrants) to specify positions, plot points, and complete geometric shapes.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-crosshairs',
                'title': "Golden Rule 1: 'Along the Corridor (X), Then Up or Down the Stairs (Y)'",
                'desc': 'Coordinates are always written as an ordered pair (x, y). The first number is the horizontal X-axis (right is +, left is −). The second number is the vertical Y-axis (up is +, down is −).',
                'badge': '(x, y) = (Horizontal Left/Right, Vertical Up/Down)'
            },
            {
                'icon': 'fa-arrows-to-dot',
                'title': 'Golden Rule 2: Midpoint Formula = Average the X-Values, Average the Y-Values',
                'desc': 'To find the exact halfway point (midpoint) between two coordinates (x₁, y₁) and (x₂, y₂): add the two x-coordinates and divide by 2, then add the two y-coordinates and divide by 2.',
                'badge': 'Midpoint = ((x₁ + x₂) ÷ 2 , (y₁ + y₂) ÷ 2)'
            }
        ],
        'skills': [
            {
                'title': 'Navigating the Four Quadrants from the Origin (0, 0)',
                'summary': 'Understanding positive and negative signs in each of the four Cartesian quadrants.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Origin (0, 0):</strong> The exact intersection where the X-axis and Y-axis cross.</li>
                    <li><strong>Quadrant 1 (Top-Right):</strong> (+x, +y) e.g. <strong>(4, 3)</strong> — Right 4, Up 3.</li>
                    <li><strong>Quadrant 2 (Top-Left):</strong> (&minus;x, +y) e.g. <strong>(&minus;4, 3)</strong> — Left 4, Up 3.</li>
                    <li><strong>Quadrant 3 (Bottom-Left):</strong> (&minus;x, &minus;y) e.g. <strong>(&minus;4, &minus;3)</strong> — Left 4, Down 3.</li>
                    <li><strong>Quadrant 4 (Bottom-Right):</strong> (+x, &minus;y) e.g. <strong>(4, &minus;3)</strong> — Right 4, Down 3.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Finding Missing Vertices of Rectangles, Squares & Parallelograms',
                'summary': 'Using coordinate alignment rules to deduce the 4th corner without guessing.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">For an axis-aligned <strong>rectangle</strong>, the four corners always share two pairs of x-coordinates and two pairs of y-coordinates:</p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li>If three corners are <strong>A(&minus;2, 5)</strong>, <strong>B(6, 5)</strong>, and <strong>C(6, &minus;1)</strong>:</li>
                    <li>X-values are &minus;2, 6, 6 &rarr; missing x-coordinate must be <strong>&minus;2</strong>.</li>
                    <li>Y-values are 5, 5, &minus;1 &rarr; missing y-coordinate must be <strong>&minus;1</strong>.</li>
                    <li>Therefore, the fourth corner D is <strong>(&minus;2, &minus;1)</strong>.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Calculating Midpoints & Grid Distances Across Zero',
                'summary': 'Finding horizontal/vertical side lengths and central sensor coordinates.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Distance Across Zero:</strong> From x = &minus;3 to x = 5 is a total distance of 3 + 5 = <strong>8 grid units</strong>.</li>
                    <li><strong>Midpoint Formula Example:</strong> Midpoint of (&minus;4, 2) and (6, &minus;8) = ((&minus;4 + 6) &divide; 2, (2 + &minus;8) &divide; 2) = (2 &divide; 2, &minus;6 &divide; 2) = <strong>(1, &minus;3)</strong>.</li>
                  </ul>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Logistics Depot Automated Guided Vehicle (AGV) Grid Plotting (Level 1/2 Foundation)',
                'marks': '3 Marks (Pearson Edexcel Level 1/2)',
                'context': 'Automated Warehouse Robotics Grid',
                'question': 'An automated warehouse dispatch floor is mapped on a Cartesian coordinate grid. Three charging bays form three corners of a rectangle:<br>• Bay A: <strong>(−3, 2)</strong><br>• Bay B: <strong>(5, 2)</strong><br>• Bay C: <strong>(5, −4)</strong><br>(a) State the coordinates of the fourth corner, Bay D.<br>(b) Calculate the area of the rectangle in square grid units.',
                'steps': [
                    ('Step 1', 'Align x and y coordinate pairs for the 4th corner D', 'X-coordinates pair as −3 and 5; Y-coordinates pair as 2 and −4. Bay D = (−3, −4).', 'A1: Accurate 4th vertex coordinates (−3, −4)'),
                    ('Step 2', 'Calculate horizontal length and vertical width across axes', 'Length (from −3 to 5) = 3 + 5 = 8 units.<br>Width (from −4 to 2) = 4 + 2 = 6 units.', 'M1: Accurate side lengths (8 and 6 units)'),
                    ('Step 3', 'Multiply length by width for area', 'Area = 8 × 6 = 48 square units.', 'A1: Accurate area (48 square units)')
                ],
                'final_answer': '(a) Bay D = (−3, −4) | (b) Area = 48 square units',
                'tutor_tip': 'Notice how the x-coordinates pair up (−3, −3 and 5, 5) and the y-coordinates pair up (2, 2 and −4, −4).'
            },
            {
                'title': 'Hospital Wi-Fi Router Central Midpoint & Cabling Scale (Level 2 Multi-Step)',
                'marks': '3 Marks (Pearson Edexcel Level 2)',
                'context': 'Healthcare IT Network Infrastructure',
                'question': 'On a hospital floor plan grid where <strong>1 grid unit = 2.5 metres</strong>, Nursing Station P is at <strong>(−6, 4)</strong> and Pharmacy Terminal Q is at <strong>(2, −2)</strong>.<br>(a) A relay router is installed at the exact midpoint M between P and Q. Find the coordinates of M.<br>(b) The straight-line distance from P to Q is <strong>10 grid units</strong>. Calculate the real-world cabling length if an extra <strong>15%</strong> is added for vertical drops.',
                'steps': [
                    ('Step 1', 'Calculate midpoint M by averaging x and y coordinates', 'x = (−6 + 2) ÷ 2 = −4 ÷ 2 = −2.<br>y = (4 + −2) ÷ 2 = 2 ÷ 2 = 1.<br>Midpoint M = (−2, 1).', 'M1 / A1: Accurate midpoint coordinates (−2, 1)'),
                    ('Step 2', 'Convert 10 grid units to real metres and add 15%', 'Real distance = 10 × 2.5 m = 25 metres.<br>With 15% extra = 25 m × 1.15 = 28.75 metres.', 'M1 / A1: Accurate real cable length (28.75 m)')
                ],
                'final_answer': '(a) Midpoint M = (−2, 1) | (b) Cable length = 28.75 metres',
                'tutor_tip': 'When averaging a negative and positive number, be careful with signs: −6 + 2 = −4, and −4 ÷ 2 = −2.'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Swapping X and Y Coordinates',
                'desc': 'Writing (2, −3) instead of (−3, 2) plots the point in Quadrant 4 instead of Quadrant 2.',
                'fix': 'Always write (x, y) above your answer box and check Horizontal first, Vertical second.'
            },
            {
                'title': 'Confusing Points on the Axes: (0, 4) vs (4, 0)',
                'desc': '(4, 0) lies on the horizontal X-axis; (0, 4) lies on the vertical Y-axis.',
                'fix': 'For (0, 4): move 0 along the corridor, then go 4 straight up the stairs.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'Calculate the coordinates of the midpoint between point P<strong>(−4, 6)</strong> and point Q<strong>(8, −2)</strong>.',
                'solution_steps': '1. Midpoint x = (−4 + 8) ÷ 2 = 4 ÷ 2 = 2.<br>2. Midpoint y = (6 + −2) ÷ 2 = 4 ÷ 2 = 2.<br>3. Midpoint = (2, 2).',
                'correct_answer': '(2, 2)',
                'tutor_tip': 'Add the x-coordinates and divide by 2; add the y-coordinates and divide by 2.'
            },
            {
                'marks': '3 Marks',
                'question': 'Three vertices of a square on a coordinate grid are <strong>(−1, −1), (4, −1), and (4, 4)</strong>.<br>(a) State the coordinates of the fourth vertex.<br>(b) Calculate the perimeter of the square in grid units.',
                'solution_steps': '1. Missing fourth vertex aligns with x = −1 and y = 4 → (−1, 4).<br>2. Side length = 4 − (−1) = 5 units.<br>3. Perimeter = 4 × 5 = 20 grid units.',
                'correct_answer': '(a) (−1, 4) | (b) 20 grid units',
                'tutor_tip': 'From −1 to 4 is 5 units (1 unit to zero plus 4 units past zero).'
            },
            {
                'marks': '2 Marks',
                'question': 'A drone starts at coordinates <strong>(−2, 3)</strong>. It flies <strong>7 units East (right)</strong> and <strong>5 units South (down)</strong>. What are its new coordinates?',
                'solution_steps': '1. New x-coordinate = −2 + 7 = 5.<br>2. New y-coordinate = 3 − 5 = −2.<br>3. New coordinates = (5, −2).',
                'correct_answer': '(5, −2)',
                'tutor_tip': 'East increases X (+7); South decreases Y (−5).'
            }
        ]
    },
    {
        'filename': 'functional-skills-maps-and-scale-drawings.html',
        'clean_topic': 'Maps, Scale Ratios & Floor Plans',
        'intro_lead': 'Interpret ratio scales (e.g. 1 : 50, 1 : 25,000), calculate real-world distances from map measurements, and draw scaled floor plans for ward layouts and interior design.',
        'next_file': 'functional-skills-mean-median-mode-and-range.html',
        'next_name': 'Averages (Mean, Median, Mode, Range)',
        'spec_points': [
            ('L1.19 / L2.27', 'Work out actual dimensions from scale drawings and calculate scale distances to draw plans.'),
            ('L2.27', 'Interpret ratio scales such as 1 : 50, 1 : 200, and 1 : 25,000 and convert between cm, m, and km.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-map',
                'title': "Golden Rule 1: Drawing to Real Life → MULTIPLY by Scale Factor",
                'desc': 'A ratio scale of 1 : 50 means 1 cm on the plan represents 50 cm (0.5 m) in reality. To find the real-world size: multiply the drawing measurement by the scale number, then convert cm to metres (÷ 100) or kilometres (÷ 100,000).',
                'badge': 'Real Distance = Map Length × Scale Factor (Convert 100 cm = 1 m)'
            },
            {
                'icon': 'fa-pencil-ruler',
                'title': 'Golden Rule 2: Real Life to Drawing → DIVIDE by Scale Factor',
                'desc': 'To draw a real-world object onto a scale plan: first convert the real dimension into centimetres (× 100), then divide by the scale number.',
                'badge': 'Plan Length (cm) = Real Distance (in cm) ÷ Scale Factor'
            }
        ],
        'skills': [
            {
                'title': 'Architectural & Map Ratio Scales Quick-Reference',
                'summary': 'Instant conversion equivalents for standard Pearson Edexcel scales.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:left;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Ratio Scale</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">1 cm on Paper Equals (cm)</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Practical Real-World Equivalent</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">1 : 20</td><td style="padding:6px; border:1px solid #cbd5e1;">20 cm</td><td style="padding:6px; border:1px solid #cbd5e1;">1 cm = 0.2 m (5 cm = 1 m)</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">1 : 50</td><td style="padding:6px; border:1px solid #cbd5e1;">50 cm</td><td style="padding:6px; border:1px solid #cbd5e1;">1 cm = 0.5 m (2 cm = 1 m)</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">1 : 100</td><td style="padding:6px; border:1px solid #cbd5e1;">100 cm</td><td style="padding:6px; border:1px solid #cbd5e1;">1 cm = 1.0 m</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">1 : 250</td><td style="padding:6px; border:1px solid #cbd5e1;">250 cm</td><td style="padding:6px; border:1px solid #cbd5e1;">1 cm = 2.5 m</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">1 : 25,000</td><td style="padding:6px; border:1px solid #cbd5e1;">25,000 cm</td><td style="padding:6px; border:1px solid #cbd5e1;">1 cm = 250 m = 0.25 km (4 cm = 1 km)</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">1 : 50,000</td><td style="padding:6px; border:1px solid #cbd5e1;">50,000 cm</td><td style="padding:6px; border:1px solid #cbd5e1;">1 cm = 500 m = 0.5 km (2 cm = 1 km)</td></tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                'title': 'Calculating Real-World Area from a Scale Plan (Convert Sides First!)',
                'summary': 'Why you must convert scaled cm into real metres BEFORE multiplying Length × Width.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;"><strong>Crucial Rule:</strong> Never calculate area in cm&sup2; and then multiply by the linear scale factor! Instead, always convert the length and width into real metres FIRST:</p>
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li>On a <strong>1 : 50</strong> plan, a room measures <strong>10 cm by 8 cm</strong>.</li>
                    <li>Convert Length: 10 cm &times; 50 = 500 cm = <strong>5.0 m</strong>.</li>
                    <li>Convert Width: 8 cm &times; 50 = 400 cm = <strong>4.0 m</strong>.</li>
                    <li>Calculate Real Area: 5.0 m &times; 4.0 m = <strong>20.0 m&sup2;</strong>.</li>
                  </ol>
                </div>
                """
            },
            {
                'title': 'Checking Furniture Clearance & Placement Rules on Scaled Grids',
                'summary': 'Verifying minimum walkway gaps and wall clearances on exam floor plans.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Convert Everything to Grid Squares:</strong> If 1 grid square = 0.5 m by 0.5 m, then a bed measuring 2.0 m by 1.0 m occupies <strong>4 squares by 2 squares</strong>.</li>
                    <li><strong>Check Clearance Constraints:</strong> If safety rules require "at least 1.0 m clearance from the door", block out <strong>2 full grid squares</strong> in front of the door before placing the bed.</li>
                  </ul>
                </div>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Hospital Acute Ward Refurbishment Scale Floor Plan (Level 1 Foundation)',
                'marks': '3 Marks (Pearson Edexcel Level 1)',
                'context': 'Architectural Ward Redesign',
                'question': 'A hospital architect produces a ward floor plan using a scale of <strong>1 : 50</strong>.<br>(a) On the drawing, Bay 3 measures <strong>14 cm long by 9 cm wide</strong>. What are the actual real-world dimensions in metres?<br>(b) A clinical consultation desk is <strong>2.5 metres long</strong> in reality. What length should it be drawn on the scale plan in cm?',
                'steps': [
                    ('Step 1', 'Multiply map measurements by scale factor (50)', 'Real length = 14 cm × 50 = 700 cm.<br>Real width = 9 cm × 50 = 450 cm.', 'M1: Scale multiplication'),
                    ('Step 2', 'Convert real dimensions from centimetres to metres (÷ 100)', '700 cm ÷ 100 = 7.0 metres.<br>450 cm ÷ 100 = 4.5 metres.', 'A1: Accurate real dimensions (7.0 m × 4.5 m)'),
                    ('Step 3', 'Calculate drawing length for the 2.5 m consultation desk', 'Real length = 2.5 m = 250 cm.<br>Drawing length = 250 cm ÷ 50 = 5 cm.', 'A1: Accurate drawing length (5 cm)')
                ],
                'final_answer': '(a) Real dimensions = 7.0 m long by 4.5 m wide | (b) Drawing length = 5 cm',
                'tutor_tip': 'Sanity check: Real room dimensions should be in metres (7 m × 4.5 m); paper drawings should be in centimetres (5 cm).'
            },
            {
                'title': 'Ordnance Survey Map Ambulance Route & Journey Time (Level 2 Multi-Step)',
                'marks': '4 Marks (Pearson Edexcel Level 2)',
                'context': 'Emergency Patient Transfer Dispatch',
                'question': 'On a regional map with a ratio scale of <strong>1 : 25,000</strong>, the road route from St Mary’s Hospital to the Community Rehabilitation Centre measures <strong>18 cm</strong>.<br>• The patient transfer ambulance travels at an average speed of <strong>36 km/h</strong>.<br>Calculate the journey time in <strong>minutes</strong>.',
                'steps': [
                    ('Step 1', 'Calculate real road distance in cm and convert to km', 'Real distance = 18 cm × 25,000 = 450,000 cm.<br>Convert cm to m (÷ 100) = 4,500 m.<br>Convert m to km (÷ 1,000) = 4.5 km.', 'M1 / A1: Accurate real distance (4.5 km)'),
                    ('Step 2', 'Calculate journey time in hours (Time = Distance ÷ Speed)', 'Time = 4.5 km ÷ 36 km/h = 0.125 hours.', 'M1: Speed-Distance-Time division'),
                    ('Step 3', 'Convert hours to minutes (× 60)', '0.125 × 60 = 7.5 minutes.', 'A1: Accurate time in minutes (7.5 minutes)')
                ],
                'final_answer': '7.5 minutes (Real distance = 4.5 km)',
                'tutor_tip': 'On a 1 : 25,000 map, every 1 cm = 0.25 km (or 4 cm = 1 km). So 18 cm ÷ 4 = 4.5 km immediately!'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Forgetting to Convert Centimetres to Metres or Kilometres',
                'desc': 'Writing that a hospital room is "700 m" or "700 cm" when the answer line specifies metres forfeits the accuracy mark.',
                'fix': 'Remember: 100 cm = 1 m, and 100,000 cm = 1 km.'
            },
            {
                'title': 'Scaling Area by the Linear Factor Instead of Converting Sides First',
                'desc': 'Multiplying 14 cm × 9 cm = 126 cm² and then multiplying by 50 gives the wrong area (area scales by 50², not 50).',
                'fix': 'Always convert length and width into real metres BEFORE multiplying them together for area!'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'On an Ordnance Survey map with scale <strong>1 : 50,000</strong>, the straight-line distance between two medical clinics measures <strong>7.4 cm</strong>. What is the actual distance in kilometres?',
                'solution_steps': '1. Real distance in cm = 7.4 × 50,000 = 370,000 cm.<br>2. Convert cm to km (÷ 100,000): 370,000 ÷ 100,000 = 3.7 km (or 1 cm = 0.5 km → 7.4 × 0.5 = 3.7 km).',
                'correct_answer': '3.7 km',
                'tutor_tip': 'On a 1 : 50,000 map, 1 cm = 500 m = 0.5 km.'
            },
            {
                'marks': '3 Marks',
                'question': 'A landscape gardener draws a rectangular lawn measuring <strong>16 m long by 11 m wide</strong> using a scale of <strong>1 : 200</strong>. Calculate the length and width of the lawn on the scale drawing in cm.',
                'solution_steps': '1. Convert real dimensions to cm: 16 m = 1,600 cm; 11 m = 1,100 cm.<br>2. Divide by 200: Length = 1,600 ÷ 200 = 8 cm; Width = 1,100 ÷ 200 = 5.5 cm.',
                'correct_answer': '8 cm long by 5.5 cm wide',
                'tutor_tip': 'Convert metres to cm (× 100) before dividing by the scale factor (200).'
            },
            {
                'marks': '4 Marks',
                'question': 'On a floor plan drawn to a scale of <strong>1 : 50</strong>, a rectangular office measures <strong>12 cm by 8 cm</strong>. Carpet tiles cost <strong>£15.00 per m²</strong>. Calculate the total cost to carpet the real office.',
                'solution_steps': '1. Real length = 12 × 50 = 600 cm = 6.0 m.<br>2. Real width = 8 × 50 = 400 cm = 4.0 m.<br>3. Real area = 6.0 m × 4.0 m = 24.0 m².<br>4. Total carpet cost = 24.0 × £15.00 = £360.00.',
                'correct_answer': '£360.00',
                'tutor_tip': 'Convert 12 cm and 8 cm into real metres (6 m and 4 m) FIRST, then multiply for area (24 m²).'
            }
        ]
    }
]
