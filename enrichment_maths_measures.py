# Enrichment blocks for Maths Measures, Shape & Space topics to guarantee >= 30 questions per worksheet.

ENRICHMENT_MATHS_MEASURES = {
    "2d-shapes": [
        {
            "title": "Question 3: Perimeter & Missing Side Dimensions of Polygons",
            "instruction": "Calculate the perimeter or missing side of each 2D shape:",
            "items": [
                ("a", "Equilateral triangle with sides of 8 cm. Perimeter = ?", "24 cm (8 × 3)"),
                ("b", "Regular hexagon with sides of 6 cm. Perimeter = ?", "36 cm (6 × 6)"),
                ("c", "Regular octagon with sides of 5 m. Perimeter = ?", "40 m (5 × 8)"),
                ("d", "Regular pentagon with perimeter of 45 cm. One side = ?", "9 cm (45 ÷ 5)"),
                ("e", "Isosceles triangle: Two sides of 10 cm, perimeter is 26 cm. Base = ?", "6 cm (26 - 20)"),
                ("f", "Rectangle: Length 14m, Width 7m. Perimeter = ?", "42 m (2×14 + 2×7)"),
                ("g", "Square with perimeter of 52 mm. Side length = ?", "13 mm (52 ÷ 4)"),
                ("h", "Rhombus with sides of 9.5 cm. Perimeter = ?", "38 cm (9.5 × 4)"),
                ("i", "Parallelogram: Sides 12cm and 8cm. Perimeter = ?", "40 cm (24 + 16)"),
                ("j", "Kite: Sides 15cm and 7cm. Perimeter = ?", "44 cm (2×15 + 2×7)")
            ]
        },
        {
            "title": "Question 4: Polygon Angle Sums & Classification Drills",
            "instruction": "Identify the shape property or calculate angle sum:",
            "items": [
                ("a", "Sum of interior angles in any triangle", "180°"),
                ("b", "Sum of interior angles in any quadrilateral", "360°"),
                ("c", "Sum of interior angles in a regular pentagon (n-2)×180", "540° (3 × 180)"),
                ("d", "Each angle in an equilateral triangle", "60° (180 ÷ 3)"),
                ("e", "Each angle in a regular hexagon (720 ÷ 6)", "120°"),
                ("f", "How many parallel pairs in a parallelogram?", "2 pairs"),
                ("g", "How many parallel pairs in a trapezium?", "1 pair"),
                ("h", "Name a 4-sided shape with 4 equal sides and NO right angles", "Rhombus")
            ]
        }
    ],
    "3d-shape-basics": [
        {
            "title": "Question 3: Faces, Edges and Vertices Calculations",
            "instruction": "State the number of faces (F), edges (E), and vertices (V):",
            "items": [
                ("a", "Cube: Faces = ?", "6 faces"),
                ("b", "Cube: Edges = ?", "12 edges"),
                ("c", "Cube: Vertices = ?", "8 vertices"),
                ("d", "Square-based pyramid: Faces = ?", "5 faces (1 square, 4 triangles)"),
                ("e", "Square-based pyramid: Edges = ?", "8 edges"),
                ("f", "Square-based pyramid: Vertices = ?", "5 vertices"),
                ("g", "Triangular prism: Faces = ?", "5 faces (2 triangles, 3 rectangles)"),
                ("h", "Triangular prism: Edges = ?", "9 edges"),
                ("i", "Triangular prism: Vertices = ?", "6 vertices"),
                ("j", "Cylinder: Number of flat circular faces", "2 flat faces")
            ]
        },
        {
            "title": "Question 4: Real-Life Packaging Solids & Flat Nets",
            "instruction": "Match the packaging object to its 3D solid name or net:",
            "items": [
                ("a", "Soup tin", "Cylinder"),
                ("b", "Cereal packet", "Cuboid"),
                ("c", "Football", "Sphere"),
                ("d", "Party hat", "Cone"),
                ("e", "Toblerone box", "Triangular prism"),
                ("f", "Egyptian landmark", "Square-based pyramid"),
                ("g", "Dice", "Cube"),
                ("h", "How many rectangles make up the net of a cuboid?", "6 rectangles"),
                ("i", "How many triangles make up the net of a tetrahedron?", "4 triangles"),
                ("j", "A shape with 1 curved surface and 1 flat circular face", "Cone")
            ]
        }
    ],
    "3d-shapes": [
        {
            "title": "Question 3: Surface Area of Prisms & Pyramids",
            "instruction": "Work out total surface area by summing individual faces:",
            "items": [
                ("a", "Cube with side length 4 cm. Total surface area = ?", "96 cm² (6 × 4²)"),
                ("b", "Cube with side length 5 m. Total surface area = ?", "150 m² (6 × 5²)"),
                ("c", "Cuboid: 6cm × 4cm × 3cm. Total surface area = ?", "108 cm² (2(24 + 18 + 12))"),
                ("d", "Cuboid: 10m × 5m × 2m. Total surface area = ?", "160 m² (2(50 + 20 + 10))"),
                ("e", "Triangular prism: Two 6cm×4cm triangles (area 12 each) + three 10cm rectangles (lengths 5, 5, 6). Total area?", "184 cm² (24 + 50 + 50 + 60)"),
                ("f", "Square pyramid: 6m × 6m base + four triangles of base 6m, height 8m (area 24 each). Total area?", "132 m² (36 + 4×24)"),
                ("g", "Open-top cube box with sides of 10 cm (5 faces). Area = ?", "500 cm² (5 × 100)"),
                ("h", "Cube with surface area 24 cm². Area of 1 face = ?", "4 cm² (24 ÷ 6)"),
                ("i", "Cube with surface area 24 cm². Side length = ?", "2 cm (√4)"),
                ("j", "Cuboid packaging: 20cm × 15cm × 10cm. Cardboard area?", "1,300 cm² (2(300 + 200 + 150))")
            ]
        },
        {
            "title": "Question 4: Cross-Sections & Euler's Formula (F + V - E = 2)",
            "instruction": "Verify Euler's formula or determine cross-section shape:",
            "items": [
                ("a", "Horizontal slice through a cylinder parallel to base", "Circle"),
                ("b", "Vertical slice through a cylinder through centre", "Rectangle"),
                ("c", "Horizontal slice through a cone parallel to base", "Circle"),
                ("d", "Cross-section along length of a triangular prism", "Triangle"),
                ("e", "Verify Euler for cuboid: F=6, V=8, E=12 (6 + 8 - 12)", "2 (verified)"),
                ("f", "Verify Euler for triangular prism: F=5, V=6, E=9 (5 + 6 - 9)", "2 (verified)"),
                ("g", "Verify Euler for pyramid: F=5, V=5, E=8 (5 + 5 - 8)", "2 (verified)"),
                ("h", "Can a sphere form a polygon cross-section? (Yes / No)", "No (only circular)")
            ]
        }
    ],
    "angles": [
        {
            "title": "Question 3: Angles on Parallel Lines (Alternate & Corresponding)",
            "instruction": "Identify the angle rule and calculate missing degrees:",
            "items": [
                ("a", "Angle on a straight line next to 115°. Missing angle = ?", "65° (180 - 115)"),
                ("b", "Angle around a point next to 140° and 110°. Missing angle = ?", "110° (360 - 250)"),
                ("c", "Opposite vertically opposite angle to 78°", "78° (vertically opposite angles are equal)"),
                ("d", "Z-angle (Alternate angle) to 54° between parallel lines", "54° (alternate angles are equal)"),
                ("e", "F-angle (Corresponding angle) to 122° between parallel lines", "122° (corresponding angles are equal)"),
                ("f", "Co-interior angle supplementary to 75° between parallel lines", "105° (180 - 75)"),
                ("g", "Right angle has how many degrees?", "90°"),
                ("h", "Reflex angle is an angle greater than what degrees?", "180° (between 180° and 360°)")
            ]
        },
        {
            "title": "Question 4: Triangles & Quadrilateral Angle Drills",
            "instruction": "Calculate the missing angle in each shape:",
            "items": [
                ("a", "Triangle with angles 45° and 85°. Third angle = ?", "50° (180 - 130)"),
                ("b", "Right-angled triangle with one angle 38°. Third angle = ?", "52° (90 - 38)"),
                ("c", "Isosceles triangle with apex angle 40°. Two base angles = ?", "70° each (140 ÷ 2)"),
                ("d", "Isosceles triangle with base angle 55°. Apex angle = ?", "70° (180 - 110)"),
                ("e", "Quadrilateral with angles 95°, 110°, 80°. Fourth angle = ?", "75° (360 - 285)"),
                ("f", "Parallelogram with one angle 65°. Adjacent angle = ?", "115° (180 - 65)"),
                ("g", "Parallelogram with one angle 65°. Opposite angle = ?", "65°"),
                ("h", "Rhombus with one angle 130°. Remaining three angles = ?", "130°, 50°, 50°")
            ]
        }
    ],
    "angles-and-bearings": [
        {
            "title": "Question 3: 3-Figure Compass Directions & Bearings",
            "instruction": "Write each compass direction as a 3-figure bearing (000° to 360°):",
            "items": [
                ("a", "North", "000° (or 360°)"),
                ("b", "East", "090°"),
                ("c", "South", "180°"),
                ("d", "West", "270°"),
                ("e", "North-East (NE)", "045°"),
                ("f", "South-East (SE)", "135°"),
                ("g", "South-West (SW)", "225°"),
                ("h", "North-West (NW)", "315°"),
                ("i", "North-North-East (NNE)", "022.5° (or 023°)"),
                ("j", "East-South-East (ESE)", "112.5° (or 113°)")
            ]
        },
        {
            "title": "Question 4: Reverse / Back Bearings Calculations (± 180°)",
            "instruction": "Add 180° if under 180°, or subtract 180° if over 180°:",
            "items": [
                ("a", "Forward bearing 040°. Back bearing = ?", "220° (040 + 180)"),
                ("b", "Forward bearing 085°. Back bearing = ?", "265° (085 + 180)"),
                ("c", "Forward bearing 120°. Back bearing = ?", "300° (120 + 180)"),
                ("d", "Forward bearing 175°. Back bearing = ?", "355° (175 + 180)"),
                ("e", "Forward bearing 210°. Back bearing = ?", "030° (210 - 180)"),
                ("f", "Forward bearing 290°. Back bearing = ?", "110° (290 - 180)"),
                ("g", "Forward bearing 340°. Back bearing = ?", "160° (340 - 180)"),
                ("h", "Ship sails on bearing 065° from Port A to B. Bearing from B to A?", "245° (065 + 180)")
            ]
        }
    ],
    "angles-in-2d-shapes": [
        {
            "title": "Question 3: Missing Angles in Special Triangles & Polygons",
            "instruction": "Calculate the unknown angles:",
            "items": [
                ("a", "Equilateral triangle: All three angles = ?", "60°, 60°, 60°"),
                ("b", "Right-angled isosceles triangle: Two acute angles = ?", "45°, 45°"),
                ("c", "Isosceles triangle: Peak 50°. Base angles = ?", "65°, 65° (130 ÷ 2)"),
                ("d", "Isosceles triangle: Base angle 72°. Peak angle = ?", "36° (180 - 144)"),
                ("e", "Scalene triangle: Angles 35° and 65°. Third angle = ?", "80° (180 - 100)"),
                ("f", "Exterior angle of a triangle equals the sum of two opposite interior angles. If opposites are 40° and 70°, exterior = ?", "110°"),
                ("g", "Regular pentagon: Sum of interior angles = ?", "540°"),
                ("h", "Regular pentagon: Each interior angle = ?", "108° (540 ÷ 5)"),
                ("i", "Regular hexagon: Sum of interior angles = ?", "720°"),
                ("j", "Regular hexagon: Each interior angle = ?", "120° (720 ÷ 6)")
            ]
        },
        {
            "title": "Question 4: Exterior Angles & Full Polygon Properties",
            "instruction": "Use the rule that exterior angles of ANY polygon sum to 360°:",
            "items": [
                ("a", "Regular pentagon: Exterior angle (360 ÷ 5) = ?", "72°"),
                ("b", "Regular hexagon: Exterior angle (360 ÷ 6) = ?", "60°"),
                ("c", "Regular octagon: Exterior angle (360 ÷ 8) = ?", "45°"),
                ("d", "Regular decagon: Exterior angle (360 ÷ 10) = ?", "36°"),
                ("e", "If exterior angle is 30°, number of sides of polygon = ?", "12 sides (360 ÷ 30)"),
                ("f", "If exterior angle is 40°, number of sides of polygon = ?", "9 sides (360 ÷ 40)"),
                ("g", "Interior + Exterior angle on any polygon straight edge = ?", "180°"),
                ("h", "If interior angle of regular polygon is 144°, exterior angle = ?", "36° (180 - 144)"),
                ("i", "Number of sides for regular polygon with interior 144° = ?", "10 sides (360 ÷ 36)"),
                ("j", "Sum of exterior angles of a 20-sided polygon = ?", "360° (always 360°)")
            ]
        }
    ],
    "circles": [
        {
            "title": "Question 3: Circumference of Circles (C = πd or 2πr)",
            "instruction": "Calculate circumference (use π = 3.14):",
            "items": [
                ("a", "Diameter = 10 cm. Circumference = ?", "31.4 cm (3.14 × 10)"),
                ("b", "Diameter = 20 m. Circumference = ?", "62.8 m (3.14 × 20)"),
                ("c", "Radius = 5 cm (d = 10cm). Circumference = ?", "31.4 cm"),
                ("d", "Radius = 7 m (d = 14m). Circumference = ?", "43.96 m (3.14 × 14)"),
                ("e", "Diameter = 50 mm. Circumference = ?", "157 mm (3.14 × 50)"),
                ("f", "Radius = 100 m. Circumference = ?", "628 m (3.14 × 200)"),
                ("g", "Circular running track diameter = 60 m. Distance for 1 lap?", "188.4 m (3.14 × 60)"),
                ("h", "Bicycle wheel diameter = 70 cm. Distance in 1 rotation?", "219.8 cm (or 2.2 m)")
            ]
        },
        {
            "title": "Question 4: Area of Circles & Semi-Circles (A = πr²)",
            "instruction": "Calculate circle area (use π = 3.14):",
            "items": [
                ("a", "Radius = 4 cm. Area = ?", "50.24 cm² (3.14 × 16)"),
                ("b", "Radius = 6 m. Area = ?", "113.04 m² (3.14 × 36)"),
                ("c", "Diameter = 10 cm (r = 5cm). Area = ?", "78.5 cm² (3.14 × 25)"),
                ("d", "Diameter = 20 m (r = 10m). Area = ?", "314 m² (3.14 × 100)"),
                ("e", "Semi-circle with radius 4 cm. Area = ?", "25.12 cm² (50.24 ÷ 2)"),
                ("f", "Quarter circle with radius 10 m. Area = ?", "78.5 m² (314 ÷ 4)"),
                ("g", "Circular lawn diameter 8m. Grass seed covers 10m²/box. Boxes needed?", "6 boxes (Area 50.24m² ÷ 10 = 5.02 → 6 boxes)"),
                ("h", "Difference between diameter and radius", "Diameter is twice the radius (d = 2r)")
            ]
        }
    ],
    "capacity": [
        {
            "title": "Question 3: Litres, Millilitres & Centilitres Conversions",
            "instruction": "Convert between units (1 L = 1000 ml; 1 cl = 10 ml):",
            "items": [
                ("a", "Convert 2.5 litres to millilitres", "2,500 ml"),
                ("b", "Convert 0.75 litres to millilitres", "750 ml"),
                ("c", "Convert 450 millilitres to litres", "0.45 litres"),
                ("d", "Convert 1,800 millilitres to litres", "1.8 litres"),
                ("e", "Convert 50 millilitres to litres", "0.05 litres"),
                ("f", "Convert 30 centilitres to millilitres", "300 ml"),
                ("g", "Convert 75 centilitres to litres", "0.75 litres"),
                ("h", "Convert 1.2 litres to centilitres", "120 cl"),
                ("i", "How many 250ml cups can be filled from a 2-litre bottle?", "8 cups (2000 ÷ 250)"),
                ("j", "How many 50ml medicine doses in a 500ml bottle?", "10 doses")
            ]
        },
        {
            "title": "Question 4: Dilution Rates & Practical Tank Capacities",
            "instruction": "Calculate required liquids for recipes and mixtures:",
            "items": [
                ("a", "Dilution ratio 1 : 4. Water needed for 100ml concentrate?", "400 ml"),
                ("b", "Dilution ratio 1 : 4. Total squash made with 100ml concentrate?", "500 ml (100 + 400)"),
                ("c", "Dilution 1 : 9. Total liquid made with 50ml cleaning chemical?", "500 ml (50 × 10)"),
                ("d", "Water tank capacity: 1.2m × 1.0m × 0.5m = 0.6 m³. Litres (1 m³ = 1000L)?", "600 litres"),
                ("e", "Fish tank: 50cm × 30cm × 20cm = 30,000 cm³. Litres (1000 cm³ = 1L)?", "30 litres"),
                ("f", "Kettle boils 1.7 L. If 3 mugs take 300ml each, volume left in kettle?", "800 ml (1700 - 900)"),
                ("g", "4 people drink 250ml each from 1 litre jug. Jug state?", "Empty (0 ml remaining)"),
                ("h", "Catering: 60 guests need 150ml soup each. Total litres needed?", "9 litres (9000 ml ÷ 1000)"),
                ("i", "Paint: 5 litres covers 60 m². Litres needed for 120 m²?", "10 litres"),
                ("j", "Syrup bottle 750ml. 15ml per coffee. How many coffees?", "50 coffees (750 ÷ 15)")
            ]
        }
    ],
    "coordinates": [
        {
            "title": "Question 3: Four-Quadrant Coordinate Reading (x, y)",
            "instruction": "Identify the coordinates or quadrant for each point:",
            "items": [
                ("a", "Point 3 units right, 4 units up from origin", "(3, 4)"),
                ("b", "Point 5 units left, 2 units up from origin", "(-5, 2)"),
                ("c", "Point 4 units left, 6 units down from origin", "(-4, -6)"),
                ("d", "Point 7 units right, 3 units down from origin", "(7, -3)"),
                ("e", "Point located on origin", "(0, 0)"),
                ("f", "Point 5 units left on the horizontal axis", "(-5, 0)"),
                ("g", "Point 4 units up on the vertical axis", "(0, 4)"),
                ("h", "Which coordinate comes first: horizontal x or vertical y?", "x coordinate (horizontal)"),
                ("i", "In which quadrant are both x and y negative?", "Quadrant 3 (bottom-left)"),
                ("j", "In which quadrant is x positive and y negative?", "Quadrant 4 (bottom-right)")
            ]
        },
        {
            "title": "Question 4: Midpoints & Missing Vertex of Shapes",
            "instruction": "Find the midpoint or missing vertex coordinate:",
            "items": [
                ("a", "Midpoint between (2, 4) and (6, 8)", "(4, 6)"),
                ("b", "Midpoint between (1, 5) and (7, 1)", "(4, 3)"),
                ("c", "Midpoint between (-4, 2) and (2, 8)", "(-1, 5)"),
                ("d", "Midpoint between (-3, -5) and (5, 1)", "(1, -2)"),
                ("e", "Rectangle vertices: (1, 1), (5, 1), (1, 4). Fourth vertex?", "(5, 4)"),
                ("f", "Square vertices: (0, 0), (4, 0), (0, 4). Fourth vertex?", "(4, 4)"),
                ("g", "Parallelogram: (2, 2), (6, 2), (4, 5). Fourth vertex?", "(0, 5) or (8, 5)"),
                ("h", "Distance between (2, 3) and (8, 3)", "6 units (horizontal line)"),
                ("i", "Distance between (4, -2) and (4, 5)", "7 units (vertical line)"),
                ("j", "Reflect point (3, 2) in the y-axis. New coordinates?", "(-3, 2)")
            ]
        }
    ],
    "density": [
        {
            "title": "Question 3: Density, Mass & Volume Formula (D = M ÷ V)",
            "instruction": "Calculate the missing quantity (ensure correct units):",
            "items": [
                ("a", "Mass = 400 g, Volume = 50 cm³. Density = ?", "8 g/cm³ (400 ÷ 50)"),
                ("b", "Mass = 1,200 kg, Volume = 2 m³. Density = ?", "600 kg/m³ (1200 ÷ 2)"),
                ("c", "Mass = 250 g, Volume = 100 cm³. Density = ?", "2.5 g/cm³ (250 ÷ 100)"),
                ("d", "Density = 3 g/cm³, Volume = 40 cm³. Mass = ?", "120 g (3 × 40)"),
                ("e", "Density = 800 kg/m³, Volume = 5 m³. Mass = ?", "4,000 kg (800 × 5)"),
                ("f", "Mass = 900 g, Density = 1.5 g/cm³. Volume = ?", "600 cm³ (900 ÷ 1.5)"),
                ("g", "Mass = 5,000 kg, Density = 2,500 kg/m³. Volume = ?", "2 m³ (5000 ÷ 2500)"),
                ("h", "Water density is 1.0 g/cm³. Does an object of density 0.85 g/cm³ float or sink?", "Floats (density is less than water)"),
                ("i", "Does gold with density 19.3 g/cm³ float or sink in water?", "Sinks (much denser than water)"),
                ("j", "Cube of edge 2 cm (Volume 8 cm³) has mass 72 g. Density = ?", "9 g/cm³ (72 ÷ 8)")
            ]
        },
        {
            "title": "Question 4: Workplace Density & Material Weight Estimation",
            "instruction": "Solve practical material density problems:",
            "items": [
                ("a", "Concrete density = 2,400 kg/m³. Mass of a 0.5 m³ slab?", "1,200 kg"),
                ("b", "Steel beam volume = 0.2 m³, density = 7,850 kg/m³. Weight?", "1,570 kg"),
                ("c", "Liquid fuel density = 0.8 kg/L. Mass of 50 litres in fuel tank?", "40 kg (0.8 × 50)"),
                ("d", "Oil mass = 72 kg, density = 0.9 kg/L. Volume in litres?", "80 litres (72 ÷ 0.9)"),
                ("e", "Sand density = 1.6 tonnes/m³. Weight of 4 m³ tipper truck load?", "6.4 tonnes"),
                ("f", "Packaging block: 10cm × 5cm × 4cm = 200 cm³. Mass = 50g. Density?", "0.25 g/cm³ (50 ÷ 200)"),
                ("g", "Solid aluminium bar volume = 150 cm³, density = 2.7 g/cm³. Mass?", "405 g (150 × 2.7)"),
                ("h", "Van weight limit is 1,000 kg. Can it carry 0.4 m³ of concrete (2400 kg/m³ = 960 kg)?", "Yes (960 kg is under the 1,000 kg limit)"),
                ("i", "Formula triangle for Density, Mass, Volume", "Mass at top; Density and Volume at bottom"),
                ("j", "Unit of density when mass is in kg and volume in m³", "kg/m³")
            ]
        }
    ],
    "length": [
        {
            "title": "Question 3: Metric Length Conversions & Scale Reading",
            "instruction": "Convert between mm, cm, m, and km:",
            "items": [
                ("a", "Convert 45 cm to millimetres", "450 mm (45 × 10)"),
                ("b", "Convert 120 mm to centimetres", "12 cm (120 ÷ 10)"),
                ("c", "Convert 3.5 metres to centimetres", "350 cm (3.5 × 100)"),
                ("d", "Convert 85 centimetres to metres", "0.85 m (85 ÷ 100)"),
                ("e", "Convert 2,400 metres to kilometres", "2.4 km (2400 ÷ 1000)"),
                ("f", "Convert 0.75 kilometres to metres", "750 m (0.75 × 1000)"),
                ("g", "Convert 15 millimetres to centimetres", "1.5 cm"),
                ("h", "Convert 6.2 metres to millimetres", "6,200 mm (6.2 × 1000)"),
                ("i", "How many 50cm fence panels needed for 12m boundary?", "24 panels (1200 ÷ 50)"),
                ("j", "Roll of ribbon 5m. Pieces of 40cm cut. How many full pieces?", "12 pieces (500 ÷ 40 = 12.5)")
            ]
        },
        {
            "title": "Question 4: Adding Mixed Lengths & Perimeter Checks",
            "instruction": "Convert to common units and calculate:",
            "items": [
                ("a", "1.4 m + 85 cm (140cm + 85cm)", "225 cm (or 2.25 m)"),
                ("b", "2.5 km - 800 m (2500m - 800m)", "1,700 m (or 1.7 km)"),
                ("c", "45 mm + 3.8 cm (4.5cm + 3.8cm)", "8.3 cm (or 83 mm)"),
                ("d", "3 pieces of wood: 1.2m, 95cm, 1.85m. Total length?", "4.0 m (1.2 + 0.95 + 1.85)"),
                ("e", "Timber plank 3m long. Cut off 65cm and 1.1m. Length left?", "1.25 m (300 - 65 - 110 = 125cm)"),
                ("f", "Height difference: Adult 1.82 m, child 115 cm", "67 cm (182 - 115)"),
                ("g", "Skirting board needed for room perimeter 28m. Boards are 2.4m each. Boards needed?", "12 boards (28 ÷ 2.4 = 11.66 → 12)"),
                ("h", "Distance around 400m track for 5 laps", "2,000 m (or 2 km)")
            ]
        }
    ],
    "maps-and-scale-drawings": [
        {
            "title": "Question 3: Scale Drawing Calculations (1 cm : n metres)",
            "instruction": "Calculate actual distance from map measurement:",
            "items": [
                ("a", "Scale 1 cm = 2 m. Map length 6 cm. Actual distance = ?", "12 m (6 × 2)"),
                ("b", "Scale 1 cm = 5 m. Map length 8 cm. Actual distance = ?", "40 m (8 × 5)"),
                ("c", "Scale 1 cm = 10 m. Map length 4.5 cm. Actual distance = ?", "45 m (4.5 × 10)"),
                ("d", "Scale 1 cm = 50 m. Map length 7.2 cm. Actual distance = ?", "360 m (7.2 × 50)"),
                ("e", "Scale 1 cm = 2 m. Actual room length 16 m. Map length = ?", "8 cm (16 ÷ 2)"),
                ("f", "Scale 1 cm = 5 m. Actual garden width 35 m. Map width = ?", "7 cm (35 ÷ 5)"),
                ("g", "Scale 1 cm = 10 m. Actual length 125 m. Map length = ?", "12.5 cm (125 ÷ 10)"),
                ("h", "Scale 1 : 100. Map length 4 cm. Actual length in metres?", "4 m (400 cm = 4m)"),
                ("i", "Scale 1 : 50. Map length 6 cm. Actual length in metres?", "3 m (300 cm = 3m)"),
                ("j", "Scale 1 : 25,000 (Ordnance Survey). Map distance 4 cm. Actual km?", "1 km (100,000 cm = 1 km)")
            ]
        },
        {
            "title": "Question 4: Ratio Scales & Grid Plan Dimensions",
            "instruction": "Solve plan dimensions using ratio scales:",
            "items": [
                ("a", "Ratio scale 1 : 20. Actual desk width 1.4 m (140 cm). Drawing cm?", "7 cm (140 ÷ 20)"),
                ("b", "Ratio scale 1 : 50. Drawing doorway 1.8 cm. Actual height in metres?", "0.9 m (90 cm)"),
                ("c", "Ratio scale 1 : 500. Map path 12 cm. Actual distance in metres?", "60 m (6000 cm)"),
                ("d", "Grid plan where 1 square = 0.5 m. Room is 8 squares by 6 squares. Dimensions?", "4 m by 3 m"),
                ("e", "Grid plan where 1 square = 2 m. Building is 15 squares long. Actual length?", "30 m"),
                ("f", "Convert scale '1 cm to 4 m' into ratio form 1 : n", "1 : 400 (4m = 400cm)"),
                ("g", "Convert scale '1 cm to 2.5 km' into ratio form 1 : n", "1 : 250,000 (2.5km = 250,000cm)"),
                ("h", "Scale 1 : 50,000. Actual hiking distance 15 km. Map distance cm?", "30 cm (1,500,000 ÷ 50,000)"),
                ("i", "Scale 1 : 100. Floor area on drawing is 4cm × 5cm = 20cm². Actual area m²?", "20 m² (4m × 5m)"),
                ("j", "Drawing scale 2 : 1 (enlargement). Object is 14mm. Drawing size?", "28 mm (2.8 cm)")
            ]
        }
    ],
    "money": [
        {
            "title": "Question 3: Retail Transactions & Percentage Discounts",
            "instruction": "Calculate final prices after discounts or vouchers:",
            "items": [
                ("a", "Item £40 with 10% discount. Sale price?", "£36.00 (£40 - £4)"),
                ("b", "Item £80 with 25% discount. Sale price?", "£60.00 (£80 - £20)"),
                ("c", "Item £150 with 20% discount. Sale price?", "£120.00 (£150 - £30)"),
                ("d", "Item £65 with 5% loyalty discount. Sale price?", "£61.75 (£65 - £3.25)"),
                ("e", "Voucher £15 off when spending £60. Final total for £75 spend?", "£60.00 (£75 - £15)"),
                ("f", "Two items at £24.99 and £18.50. Total cost?", "£43.49"),
                ("g", "Change from £50 note after spending £38.45", "£11.55"),
                ("h", "Change from £20 note after spending £6.80 and £7.45", "£5.75 (£20 - £14.25)"),
                ("i", "Split restaurant bill of £144 equally among 6 people", "£24.00 each"),
                ("j", "Split cab fare of £38.50 equally between 2 people", "£19.25 each")
            ]
        },
        {
            "title": "Question 4: VAT, Invoicing & Service Charges",
            "instruction": "Calculate VAT at 20% and gross invoice totals:",
            "items": [
                ("a", "Net price £50. VAT at 20% = ?", "£10.00"),
                ("b", "Net price £50. Gross total including 20% VAT = ?", "£60.00"),
                ("c", "Net price £180. VAT at 20% = ?", "£36.00"),
                ("d", "Net price £180. Gross total including 20% VAT = ?", "£216.00"),
                ("e", "Net labour £240 + parts £160. Total net = ?", "£400.00"),
                ("f", "Total net £400 + 20% VAT (£80). Gross invoice = ?", "£480.00"),
                ("g", "Restaurant bill £80 with 10% service charge added. Total?", "£88.00 (£80 + £8)"),
                ("h", "Gross price is £120 including 20% VAT. Net price (÷ 1.2)?", "£100.00"),
                ("i", "Car repair: 3 hours labour at £45/hr + £85 parts. Subtotal?", "£220.00 (135 + 85)"),
                ("j", "Delivery fee £4.50 on £32 order. Total amount payable?", "£36.50")
            ]
        }
    ],
    "money-invoicing-payroll": [
        {
            "title": "Question 3: Gross Pay, Overtime & Wage Slips",
            "instruction": "Work out gross wages and overtime pay:",
            "items": [
                ("a", "Standard hours: 35 hours at £11.50/hr. Basic pay?", "£402.50"),
                ("b", "Standard hours: 40 hours at £12.00/hr. Basic pay?", "£480.00"),
                ("c", "Overtime rate is 'time and a half' on £12.00/hr. Overtime hourly rate?", "£18.00/hr (12 × 1.5)"),
                ("d", "5 hours overtime at £18.00/hr. Overtime pay?", "£90.00"),
                ("e", "Gross pay: Basic £480 + Overtime £90. Total gross pay?", "£570.00"),
                ("f", "Double time on £14.00/hr for Sunday shift. Sunday hourly rate?", "£28.00/hr"),
                ("g", "6 hours Sunday shift at double time (£28/hr). Total Sunday pay?", "£168.00"),
                ("h", "Salary £24,000 per year. Monthly gross pay (÷ 12)?", "£2,000.00"),
                ("i", "Salary £31,200 per year. Weekly gross pay (÷ 52)?", "£600.00"),
                ("j", "Shift bonus £25 added to 8 hours at £10.50/hr. Total shift earnings?", "£109.00 (84 + 25)")
            ]
        },
        {
            "title": "Question 4: Net Pay Deductions (Tax, National Insurance, Pension)",
            "instruction": "Calculate deductions and net take-home pay:",
            "items": [
                ("a", "Gross pay £2,200. Income tax deduction £240. Pay after tax?", "£1,960.00"),
                ("b", "National Insurance deduction £145 on £2,200 gross. Total deductions so far?", "£385.00 (240 + 145)"),
                ("c", "Pension contribution 5% on £2,200 gross pay = ?", "£110.00"),
                ("d", "Total deductions: Tax £240 + NI £145 + Pension £110 = ?", "£495.00"),
                ("e", "Net take-home pay: Gross £2,200 - Total deductions £495 = ?", "£1,705.00"),
                ("f", "Gross pay £550. Deductions: Tax £60, NI £35. Net pay?", "£455.00"),
                ("g", "Student loan deduction: 9% of earnings above £1,750 threshold. Earnings £2,000. Deduction?", "£22.50 (9% of £250)"),
                ("h", "Union fee £12 deducted monthly. Total union fees per year?", "£144.00"),
                ("i", "Difference between Gross pay and Net pay", "Net pay is take-home pay after all statutory deductions"),
                ("j", "Take-home percentage: Net £1,600 on Gross £2,000. What %?", "80% (1600 ÷ 2000)")
            ]
        }
    ],
    "movement-and-direction": [
        {
            "title": "Question 3: Grid Movements & Vector Translations",
            "instruction": "Determine new coordinate position after given movement:",
            "items": [
                ("a", "Start at (3, 2). Move 4 units Right, 2 units Up. New position?", "(7, 4)"),
                ("b", "Start at (5, 6). Move 3 units Left, 4 units Down. New position?", "(2, 2)"),
                ("c", "Start at (-2, 4). Move 5 units Right, 3 units Down. New position?", "(3, 1)"),
                ("d", "Start at (1, -3). Move 4 units Left, 5 units Up. New position?", "(-3, 2)"),
                ("e", "Start at (0, 0). Move 6 units South (Down). New position?", "(0, -6)"),
                ("f", "Start at (2, 5). Move 8 units East (Right). New position?", "(10, 5)"),
                ("g", "Start at (-4, -1). Move 4 units North, 4 units East. New position?", "(0, 3)"),
                ("h", "Movement vector from (2, 3) to (7, 9)", "5 units Right, 6 units Up"),
                ("i", "Movement vector from (6, 8) to (1, 4)", "5 units Left, 4 units Down"),
                ("j", "Movement vector from (-3, 2) to (3, -2)", "6 units Right, 4 units Down")
            ]
        },
        {
            "title": "Question 4: Compass Bearings & Rotations (Clockwise / Anti-clockwise)",
            "instruction": "State the new facing direction after the turn:",
            "items": [
                ("a", "Facing North. Turn 90° clockwise. New direction?", "East"),
                ("b", "Facing East. Turn 90° clockwise. New direction?", "South"),
                ("c", "Facing North. Turn 180°. New direction?", "South"),
                ("d", "Facing West. Turn 90° anti-clockwise. New direction?", "South"),
                ("e", "Facing North. Turn 45° clockwise. New direction?", "North-East (NE)"),
                ("f", "Facing South. Turn 135° anti-clockwise. New direction?", "North-East (NE)"),
                ("g", "Facing East. Turn 270° clockwise. New direction?", "North"),
                ("h", "Angle between North and South-East", "135° clockwise"),
                ("i", "Angle between West and North-East", "135° clockwise (or 225° anti-clockwise)"),
                ("j", "Full revolution in degrees", "360°")
            ]
        }
    ],
    "nets": [
        {
            "title": "Question 3: Identifying Solids from Flat Nets",
            "instruction": "Name the 3D solid that folds from each described net:",
            "items": [
                ("a", "Net of 6 identical connected squares", "Cube"),
                ("b", "Net of 6 connected rectangles in 3 matching pairs", "Cuboid"),
                ("c", "Net of 2 identical circles and 1 large rectangle", "Cylinder"),
                ("d", "Net of 1 circle and 1 circular sector", "Cone"),
                ("e", "Net of 2 identical triangles and 3 rectangles", "Triangular prism"),
                ("f", "Net of 1 central square and 4 surrounding triangles", "Square-based pyramid"),
                ("g", "Net of 4 identical equilateral triangles", "Tetrahedron (triangular pyramid)"),
                ("h", "Net of 2 regular pentagons and 5 rectangles", "Pentagonal prism"),
                ("i", "Net of 2 regular hexagons and 6 rectangles", "Hexagonal prism"),
                ("j", "Can 6 squares in a straight line form a closed cube? (Yes / No)", "No (overlapping ends, missing top/bottom)")
            ]
        },
        {
            "title": "Question 4: Opposite Faces on a Cube Net",
            "instruction": "Identify which faces fold opposite to each other on standard nets:",
            "items": [
                ("a", "On a standard dice, opposite faces always sum to what number?", "7"),
                ("b", "Face 1 is opposite to which number on a standard die?", "6 (7 - 1)"),
                ("c", "Face 2 is opposite to which number on a standard die?", "5 (7 - 2)"),
                ("d", "Face 3 is opposite to which number on a standard die?", "4 (7 - 3)"),
                ("e", "In a T-shaped cube net with horizontal row (A, B, C, D), face A is opposite to?", "Face C (skip one face)"),
                ("f", "In a T-shaped cube net, face B is opposite to?", "Face D (skip one face)"),
                ("g", "Top flap (E) is opposite to which flap?", "Bottom flap (F)"),
                ("h", "How many corners (vertices) meet when folding a square pyramid?", "5 vertices (4 base corners + 1 apex)"),
                ("i", "How many edges meet when folding a triangular prism?", "9 edges"),
                ("j", "Does a cylinder have vertices? (Yes / No)", "No (0 vertices)")
            ]
        }
    ],
    "plans-and-elevations": [
        {
            "title": "Question 3: Identifying Plan, Front & Side Elevations",
            "instruction": "Identify the view direction (Plan / Front / Side):",
            "items": [
                ("a", "Bird's-eye view looking directly down from above", "Plan view"),
                ("b", "View looking straight at the front face of a building", "Front elevation"),
                ("c", "View looking at the side profile of an object", "Side elevation"),
                ("d", "Plan view of a cylindrical water tank", "Circle"),
                ("e", "Front elevation of a cylindrical water tank standing upright", "Rectangle"),
                ("f", "Side elevation of a cylindrical water tank standing upright", "Rectangle"),
                ("g", "Plan view of a cone (with dot at center for apex)", "Circle with central dot"),
                ("h", "Front elevation of a cone", "Triangle"),
                ("i", "Plan view of a square-based pyramid", "Square with diagonal cross (apex)"),
                ("j", "Side elevation of a square-based pyramid", "Triangle")
            ]
        },
        {
            "title": "Question 4: Calculating Object Dimensions from 2D Elevations",
            "instruction": "Extract the 3D dimensions (Length, Width, Height):",
            "items": [
                ("a", "Plan is 6m × 4m, Front elevation height is 3m. Length?", "6 m"),
                ("b", "Plan is 6m × 4m, Front elevation height is 3m. Width?", "4 m"),
                ("c", "Plan is 6m × 4m, Front elevation height is 3m. Height?", "3 m"),
                ("d", "Volume of cuboid from elevations: 6m × 4m × 3m = ?", "72 m³"),
                ("e", "Plan is 10cm × 8cm, Side elevation is 8cm × 5cm. Height?", "5 cm"),
                ("f", "Plan of steps: 3 equal steps of 30cm depth. Total depth?", "90 cm (3 × 30)"),
                ("g", "Front elevation of steps: 3 risers of 18cm. Total step height?", "54 cm (3 × 18)"),
                ("h", "Plan view of garage: 7m × 3.5m. Floor area = ?", "24.5 m² (7 × 3.5)"),
                ("i", "Front elevation of garage: 3.5m wide, 2.8m high. Wall area?", "9.8 m² (3.5 × 2.8)"),
                ("j", "True or False: Plan view shows the height of an object.", "False (plan only shows length and width/depth)")
            ]
        }
    ],
    "problems-involving-money": [
        {
            "title": "Question 3: Multi-Item Budgeting & Petty Cash Reconciliations",
            "instruction": "Calculate remaining balance or total expenditure:",
            "items": [
                ("a", "Budget £150. Spend: £34.50, £42.80, £18.20. Total spend?", "£95.50"),
                ("b", "Budget £150. Total spend £95.50. Remaining budget?", "£54.50"),
                ("c", "Staff training budget £1,000. 4 courses at £195 each. Total cost?", "£780.00"),
                ("d", "Remaining training budget (£1,000 - £780) = ?", "£220.00"),
                ("e", "Petty cash box has: 4 × £20, 5 × £10, 6 × £5, 12 × £1. Total?", "£172.00 (80 + 50 + 30 + 12)"),
                ("f", "Till cash float started with £150. Total at end is £845. Total takings?", "£695.00 (£845 - £150)"),
                ("g", "Refund £24.50 given on £60 purchase. Net sale amount?", "£35.50"),
                ("h", "Catering: 25 sandwich platters at £16.50 each. Total cost?", "£412.50"),
                ("i", "Deposit of 15% paid on £800 sofa. Deposit amount?", "£120.00 (800 × 0.15)"),
                ("j", "Balance remaining on sofa (£800 - £120) = ?", "£680.00")
            ]
        },
        {
            "title": "Question 4: Hire Purchase, Installments & Loan Cost Comparisons",
            "instruction": "Compare total payment plans against cash price:",
            "items": [
                ("a", "Laptop cash price: £450. Plan: £45 deposit + 10 monthly payments of £45. Plan total?", "£495.00 (45 + 450)"),
                ("b", "Difference between plan total (£495) and cash price (£450)?", "£45.00 extra (credit cost)"),
                ("c", "Washing machine: £30/month for 24 months. Total cost?", "£720.00 (30 × 24)"),
                ("d", "Washing machine cash price £550. Extra paid on 24-month plan?", "£170.00 (£720 - £550)"),
                ("e", "Car loan: Borrow £5,000, repay £160/month for 36 months. Repayment total?", "£5,760.00 (160 × 36)"),
                ("f", "Total interest paid on the £5,000 car loan?", "£760.00 (£5,760 - £5,000)"),
                ("g", "Gym membership: £35/month for 12 months vs £360 upfront. Upfront saving?", "£60.00 saving (£420 - £360)"),
                ("h", "Insurance: £45/month (12 months = £540) vs £490 annual one-off. Saving?", "£50.00 saving"),
                ("i", "Hire car: £25/day + £0.15/mile. Cost for 3 days and 200 miles?", "£105.00 (£75 + £30)"),
                ("j", "Van hire: £60/day. Hire for 4 days with 10% weekend surcharge. Total?", "£264.00 (£240 + £24)")
            ]
        }
    ],
    "scales": [
        {
            "title": "Question 3: Reading Analogue Measuring Scales & Gauges",
            "instruction": "Determine the value indicated on the measuring scale:",
            "items": [
                ("a", "Scale from 0 to 100 with 10 divisions. Each division represents?", "10 units"),
                ("b", "Scale from 0 to 1 kg with 10 divisions. Each division represents?", "100 g (0.1 kg)"),
                ("c", "Scale from 0 to 500 ml with 5 divisions. Each division represents?", "100 ml"),
                ("d", "Needle points 3 divisions past 200 on scale with 10-unit intervals", "230"),
                ("e", "Thermometer scale from -10 to +30 with 2° intervals. 4 marks above 0?", "8°C"),
                ("f", "Weighing scales needle halfway between 400g and 500g", "450 g"),
                ("g", "Speedometer needle between 40 and 60 mph, 3/4 way along", "55 mph"),
                ("h", "Measuring jug level halfway between 600ml and 800ml", "700 ml"),
                ("i", "Pressure gauge reading 2 divisions below 4 bar (0.2 bar intervals)", "3.6 bar"),
                ("j", "Fuel gauge has 4 quarters (E, 1/4, 1/2, 3/4, F). Tank 60L. Litres at 3/4?", "45 litres (60 × 0.75)")
            ]
        },
        {
            "title": "Question 4: Ratio Scales & Enlargement Factors",
            "instruction": "Work out actual or enlarged dimensions:",
            "items": [
                ("a", "Scale factor 3 enlargement on a 5 cm by 4 cm rectangle. New length?", "15 cm (5 × 3)"),
                ("b", "Scale factor 3 enlargement on a 5 cm by 4 cm rectangle. New width?", "12 cm (4 × 3)"),
                ("c", "Scale factor 2.5 on a triangle with base 8 cm. New base?", "20 cm (8 × 2.5)"),
                ("d", "Scale factor 1/2 (reduction) on a 60 cm line. New length?", "30 cm"),
                ("e", "Scale factor 1/4 on a 24 m room. Drawing size in metres?", "6 m (24 ÷ 4)"),
                ("f", "Original shape perimeter 18 cm, enlarged by factor 2. New perimeter?", "36 cm (18 × 2)"),
                ("g", "Original photo 10cm × 15cm. Enlarged to length 30cm (factor 2). Width?", "20 cm (10 × 2)"),
                ("h", "Map ratio 1 : 25,000. 2 cm on map represents how many km?", "0.5 km (50,000 cm = 500m = 0.5km)"),
                ("i", "Model train scale 1 : 76. Model is 25 cm long. Actual train length?", "19 m (1,900 cm = 19m)"),
                ("j", "Architect scale 1 : 20. Actual window 1.6m (160cm). Plan cm?", "8 cm (160 ÷ 20)")
            ]
        }
    ],
    "speed": [
        {
            "title": "Question 3: Average Speed Calculations (Speed = Distance ÷ Time)",
            "instruction": "Calculate speed in miles per hour (mph) or km/h:",
            "items": [
                ("a", "120 miles in 2 hours. Speed = ?", "60 mph (120 ÷ 2)"),
                ("b", "150 miles in 3 hours. Speed = ?", "50 mph (150 ÷ 3)"),
                ("c", "210 km in 3 hours. Speed = ?", "70 km/h (210 ÷ 3)"),
                ("d", "90 miles in 1.5 hours (1 hr 30 mins). Speed = ?", "60 mph (90 ÷ 1.5)"),
                ("e", "45 miles in 45 minutes (0.75 hours). Speed = ?", "60 mph (45 ÷ 0.75)"),
                ("f", "10 miles in 15 minutes (0.25 hours). Speed = ?", "40 mph (10 ÷ 0.25)"),
                ("g", "25 miles in 30 minutes (0.5 hours). Speed = ?", "50 mph (25 ÷ 0.5)"),
                ("h", "300 km in 4 hours. Speed = ?", "75 km/h (300 ÷ 4)")
            ]
        },
        {
            "title": "Question 4: Distance & Travel Time Calculations (D = S × T; T = D ÷ S)",
            "instruction": "Calculate distance or travel time accurately:",
            "items": [
                ("a", "Speed 40 mph, Time 2.5 hours. Distance = ?", "100 miles (40 × 2.5)"),
                ("b", "Speed 60 mph, Time 3 hours 15 mins (3.25h). Distance = ?", "195 miles (60 × 3.25)"),
                ("c", "Speed 50 mph, Time 1 hour 45 mins (1.75h). Distance = ?", "87.5 miles (50 × 1.75)"),
                ("d", "Distance 180 miles, Speed 60 mph. Time = ?", "3 hours (180 ÷ 60)"),
                ("e", "Distance 140 miles, Speed 40 mph. Time = ?", "3.5 hours (3 hours 30 mins)"),
                ("f", "Distance 35 miles, Speed 70 mph. Time = ?", "0.5 hours (30 minutes)"),
                ("g", "Leave at 09:15, drive 90 miles at 60 mph (1.5h). Arrival time?", "10:45"),
                ("h", "Meeting at 14:00, journey is 80 miles at 40 mph (2h). Latest departure time?", "12:00")
            ]
        }
    ],
    "surface-area": [
        {
            "title": "Question 2: Surface Area of Cubes and Cuboids",
            "instruction": "Calculate the total exterior surface area (sum of all 6 faces):",
            "items": [
                ("a", "Cube with side length 3 cm. Area = ?", "54 cm² (6 × 3² = 6 × 9)"),
                ("b", "Cube with side length 6 m. Area = ?", "216 m² (6 × 36)"),
                ("c", "Cube with side length 10 cm. Area = ?", "600 cm² (6 × 100)"),
                ("d", "Cuboid: 5cm × 3cm × 2cm. Area = ?", "62 cm² (2(15 + 10 + 6))"),
                ("e", "Cuboid: 8m × 4m × 2m. Area = ?", "112 m² (2(32 + 16 + 8))"),
                ("f", "Cuboid: 10cm × 6cm × 4cm. Area = ?", "248 cm² (2(60 + 40 + 24))"),
                ("g", "Cuboid: 12m × 5m × 3m. Area = ?", "222 m² (2(60 + 36 + 15))"),
                ("h", "Open-top cuboid box: 6m × 4m base, 2m high (1 base + 4 sides). Area?", "64 m² (24 + 2(12) + 2(8))"),
                ("i", "Closed cardboard box: 40cm × 30cm × 20cm. Cardboard area?", "5,200 cm² (2(1200 + 800 + 600))"),
                ("j", "Brick: 20cm × 10cm × 5cm. Surface area?", "700 cm² (2(200 + 100 + 50))")
            ]
        },
        {
            "title": "Question 3: Surface Area of Triangular Prisms & Cylinders",
            "instruction": "Work out the total surface area by summing individual faces:",
            "items": [
                ("a", "Triangular prism: 2 triangles (area 15 each) + 3 rectangles (areas 40, 50, 30). Total?", "150 cm² (30 + 120)"),
                ("b", "Triangular prism: 2 triangles (area 24 each) + 3 rectangles (areas 60, 60, 80). Total?", "248 cm² (48 + 200)"),
                ("c", "Cylinder: Radius 5 cm, Height 10 cm. Curved surface area (2πrh, π=3.14)?", "314 cm² (2 × 3.14 × 5 × 10)"),
                ("d", "Cylinder: Radius 5 cm. Area of two circular ends (2 × πr²)?", "157 cm² (2 × 3.14 × 25)"),
                ("e", "Cylinder: Radius 5 cm, Height 10 cm. Total surface area (curved + 2 ends)?", "471 cm² (314 + 157)"),
                ("f", "Closed cylinder can: Diameter 10 cm (r=5), Height 15 cm. Curved area?", "471 cm² (3.14 × 10 × 15)"),
                ("g", "Total area of can: Curved 471 cm² + two ends (157 cm²)?", "628 cm²"),
                ("h", "Square-based pyramid: 4m × 4m base + 4 triangles of base 4m, height 6m (12 each). Total?", "64 m² (16 + 48)")
            ]
        },
        {
            "title": "Question 4: Practical Painting & Wrapping Surface Areas",
            "instruction": "Calculate surface area for materials, wrapping and paint coats:",
            "items": [
                ("a", "Paint 4 walls of room: Each wall 5m long, 2.5m high (12.5m² each). Total area?", "50 m² (4 × 12.5)"),
                ("b", "Subtract window and door totaling 6 m² from 50 m². Paintable wall area?", "44 m²"),
                ("c", "Paint tin covers 10 m². How many tins needed for 44 m²?", "5 tins (44 ÷ 10 = 4.4 → 5)"),
                ("d", "Two coats of paint required on 44 m². Total coverage needed?", "88 m² (44 × 2)"),
                ("e", "Tins needed for two coats (88 m² ÷ 10 m²/tin)?", "9 tins (8.8 → 9)"),
                ("f", "Wrapping gift cuboid 15cm × 10cm × 8cm (Surface area 700 cm²). Need 10% extra for overlap. Total wrapping paper?", "770 cm² (700 + 70)")
            ]
        }
    ],
    "symmetry-and-2d-shapes": [
        {
            "title": "Question 3: Lines of Symmetry of Standard 2D Shapes",
            "instruction": "State the number of lines of reflective symmetry:",
            "items": [
                ("a", "Equilateral triangle", "3 lines of symmetry"),
                ("b", "Isosceles triangle", "1 line of symmetry"),
                ("c", "Scalene triangle", "0 lines of symmetry"),
                ("d", "Square", "4 lines of symmetry"),
                ("e", "Rectangle (non-square)", "2 lines of symmetry"),
                ("f", "Rhombus", "2 lines of symmetry"),
                ("g", "Parallelogram (non-rectangle)", "0 lines of symmetry"),
                ("h", "Kite", "1 line of symmetry"),
                ("i", "Regular hexagon", "6 lines of symmetry"),
                ("j", "Circle", "Infinite lines of symmetry")
            ]
        },
        {
            "title": "Question 4: Order of Rotational Symmetry",
            "instruction": "State the order of rotational symmetry (number of times it fits onto itself in 360°):",
            "items": [
                ("a", "Square", "Order 4"),
                ("b", "Rectangle", "Order 2"),
                ("c", "Equilateral triangle", "Order 3"),
                ("d", "Isosceles triangle", "Order 1 (no rotational symmetry beyond 360°)"),
                ("e", "Parallelogram", "Order 2"),
                ("f", "Rhombus", "Order 2"),
                ("g", "Regular pentagon", "Order 5"),
                ("h", "Regular octagon", "Order 8")
            ]
        }
    ],
    "temperature": [
        {
            "title": "Question 3: Temperature Changes & Negative Degrees",
            "instruction": "Calculate the temperature difference or new temperature:",
            "items": [
                ("a", "Temperature is -4°C, rises by 9°C. New temperature = ?", "5°C (-4 + 9)"),
                ("b", "Temperature is 6°C, drops by 11°C. New temperature = ?", "-5°C (6 - 11)"),
                ("c", "Temperature is -8°C, rises by 5°C. New temperature = ?", "-3°C (-8 + 5)"),
                ("d", "Temperature is -2°C, drops by 7°C. New temperature = ?", "-9°C (-2 - 7)"),
                ("e", "Difference between -6°C and +8°C = ?", "14°C (8 - (-6))"),
                ("f", "Difference between -12°C and -3°C = ?", "9°C (-3 - (-12))"),
                ("g", "Freezer target is -18°C. Actual reading is -14°C. How many degrees too warm?", "4°C too warm"),
                ("h", "Clinical fridge range: +2°C to +8°C. Is 5.5°C within safe range? (Yes / No)", "Yes (between 2°C and 8°C)"),
                ("i", "Clinical fridge reading is 9.2°C. Is this safe? (Yes / No)", "No (exceeds 8°C upper limit)"),
                ("j", "Body temperature drops from 37.0°C to 35.2°C. Temperature drop?", "1.8°C drop")
            ]
        },
        {
            "title": "Question 4: Celsius and Fahrenheit Practical Benchmarks",
            "instruction": "Identify standard temperature points or convert using F = 1.8C + 32:",
            "items": [
                ("a", "Freezing point of water in Celsius", "0°C"),
                ("b", "Boiling point of water in Celsius", "100°C"),
                ("c", "Freezing point of water in Fahrenheit", "32°F"),
                ("d", "Boiling point of water in Fahrenheit", "212°F"),
                ("e", "Normal human body temperature in Celsius", "37°C"),
                ("f", "Comfortable room temperature in Celsius", "20°C to 21°C"),
                ("g", "Convert 10°C to Fahrenheit: (1.8 × 10) + 32 = ?", "50°F (18 + 32)"),
                ("h", "Convert 25°C to Fahrenheit: (1.8 × 25) + 32 = ?", "77°F (45 + 32)"),
                ("i", "Oven cooking temperature 180°C converted to Gas Mark (Gas Mark 4 is 180°C)", "Gas Mark 4"),
                ("j", "Which is colder: -15°C or 0°F (-17.8°C)?", "0°F is colder (-17.8°C < -15°C)")
            ]
        }
    ],
    "time": [
        {
            "title": "Question 3: 12-Hour and 24-Hour Clock Conversions",
            "instruction": "Convert between 12-hour (am/pm) and 24-hour clock formats:",
            "items": [
                ("a", "Convert 08:25 am to 24-hour clock", "08:25"),
                ("b", "Convert 2:40 pm to 24-hour clock", "14:40 (2 + 12)"),
                ("c", "Convert 6:15 pm to 24-hour clock", "18:15"),
                ("d", "Convert 11:50 pm to 24-hour clock", "23:50"),
                ("e", "Convert 12:30 pm (afternoon) to 24-hour clock", "12:30"),
                ("f", "Convert 12:15 am (midnight period) to 24-hour clock", "00:15"),
                ("g", "Convert 17:35 to 12-hour clock (am/pm)", "5:35 pm"),
                ("h", "Convert 21:05 to 12-hour clock (am/pm)", "9:05 pm"),
                ("i", "Convert 00:45 to 12-hour clock (am/pm)", "12:45 am"),
                ("j", "Convert 12:00 (midday) to 12-hour clock", "12:00 pm (noon)")
            ]
        },
        {
            "title": "Question 4: Elapsed Time, Shift Durations & Timetable Intervals",
            "instruction": "Calculate elapsed time between start and finish:",
            "items": [
                ("a", "From 08:30 to 12:15. Elapsed time?", "3 hours 45 minutes"),
                ("b", "From 13:45 to 17:20. Elapsed time?", "3 hours 35 minutes"),
                ("c", "From 21:50 to 02:10 next morning. Elapsed time?", "4 hours 20 minutes"),
                ("d", "Shift starts at 07:30, duration is 8 hours 30 mins. Finish time?", "16:00"),
                ("e", "Meeting starts at 14:15, lasts 1 hour 50 mins. End time?", "16:05"),
                ("f", "Train departs 10:28, arrives 12:04. Journey time?", "1 hour 36 minutes"),
                ("g", "Nurse shift 12 hours with 1h 15m unpaid breaks. Paid hours?", "10 hours 45 mins (10.75h)"),
                ("h", "Cooking timer: Roast takes 2h 20m. Put in oven at 11:50. Ready time?", "14:10")
            ]
        }
    ],
    "unit-conversions": [
        {
            "title": "Question 3: Converting Between Metric Mass & Capacity",
            "instruction": "Convert between units (g, kg, tonnes; ml, cl, litres):",
            "items": [
                ("a", "Convert 3,500 g to kg", "3.5 kg (3500 ÷ 1000)"),
                ("b", "Convert 0.65 kg to g", "650 g (0.65 × 1000)"),
                ("c", "Convert 4.2 tonnes to kg", "4,200 kg (4.2 × 1000)"),
                ("d", "Convert 850 kg to tonnes", "0.85 tonnes (850 ÷ 1000)"),
                ("e", "Convert 250 ml to litres", "0.25 litres (250 ÷ 1000)"),
                ("f", "Convert 1.75 litres to ml", "1,750 ml (1.75 × 1000)"),
                ("g", "Convert 45 cl to ml", "450 ml (45 × 10)"),
                ("h", "Convert 500 ml to cl", "50 cl (500 ÷ 10)")
            ]
        },
        {
            "title": "Question 4: Metric and Imperial Approximations (Functional Skills Rules)",
            "instruction": "Use official Functional Skills conversion factors:",
            "items": [
                ("a", "5 miles ≈ 8 km. Convert 15 miles to km", "24 km (15 × 8 ÷ 5)"),
                ("b", "5 miles ≈ 8 km. Convert 40 km to miles", "25 miles (40 × 5 ÷ 8)"),
                ("c", "1 kg ≈ 2.2 lbs. Convert 10 kg to pounds", "22 lbs (10 × 2.2)"),
                ("d", "1 kg ≈ 2.2 lbs. Convert 44 lbs to kg", "20 kg (44 ÷ 2.2)"),
                ("e", "1 litre ≈ 1.75 pints. Convert 4 litres to pints", "7 pints (4 × 1.75)"),
                ("f", "1 gallon ≈ 4.5 litres. Convert 10 gallons to litres", "45 litres (10 × 4.5)"),
                ("g", "1 inch ≈ 2.5 cm. Convert 6 inches to cm", "15 cm (6 × 2.5)"),
                ("h", "1 foot ≈ 30 cm. Convert 5 feet to cm", "150 cm (5 × 30)")
            ]
        }
    ],
    "using-length-area-and-volume-in-calculations": [
        {
            "title": "Question 3: Compound Geometric Calculations (Perimeter, Area & Cost)",
            "instruction": "Work out the required compound property:",
            "items": [
                ("a", "Lawn 12m × 8m. Perimeter for fencing = ?", "40 m (2×12 + 2×8)"),
                ("b", "Fence panels cost £15 per metre. Total fencing cost for 40m?", "£600.00 (40 × 15)"),
                ("c", "Lawn area = 12m × 8m = 96 m². Turf costs £6/m². Total turf cost?", "£576.00 (96 × 6)"),
                ("d", "Room 5m × 4m. Carpet tiles 50cm × 50cm (0.25 m²). Tiles needed?", "80 tiles (20 ÷ 0.25)"),
                ("e", "Wall 6m × 3m = 18 m². Tiles 20cm × 20cm (0.04 m²). Tiles needed?", "450 tiles (18 ÷ 0.04)"),
                ("f", "Swimming pool: 10m × 5m × 2m. Volume = ?", "100 m³"),
                ("g", "Pool capacity in litres (1 m³ = 1000 litres)?", "100,000 litres"),
                ("h", "Water flow rate is 5,000 L/hour. Hours to fill 100,000 L pool?", "20 hours (100,000 ÷ 5000)"),
                ("i", "Garden flower bed: 4m × 2m × 0.2m deep. Compost volume in m³?", "1.6 m³"),
                ("j", "Compost bags hold 50 litres (0.05 m³). Bags needed for 1.6 m³?", "32 bags (1.6 ÷ 0.05)")
            ]
        },
        {
            "title": "Question 4: Dimension Matching & Unit Consistency Rules",
            "instruction": "Convert all dimensions to common units before calculating:",
            "items": [
                ("a", "Rectangle 2.4 m by 80 cm. Area in m² (2.4 × 0.8)", "1.92 m²"),
                ("b", "Rectangle 1.5 m by 60 cm. Area in cm² (150 × 60)", "9,000 cm²"),
                ("c", "Cuboid: 2 m by 50 cm by 40 cm. Volume in m³ (2 × 0.5 × 0.4)", "0.4 m³"),
                ("d", "Cuboid volume 0.4 m³ converted to cm³ (0.4 × 1,000,000)", "400,000 cm³"),
                ("e", "Ribbon needed for 6 gifts: each gift needs 85 cm. Total metres?", "5.1 m (510 cm)"),
                ("f", "Planks 2.4m each. Total length of 15 planks in metres?", "36 m"),
                ("g", "Table top 1.8m × 0.9m. Varnish covers 8 m²/litre. Litres needed for 1 coat?", "0.2 litres (1.62 ÷ 8)"),
                ("h", "Packaging box: 30cm × 20cm × 15cm. How many in crate 120cm × 80cm × 60cm?", "64 boxes ((120÷30) × (80÷20) × (60÷15) = 4×4×4)"),
                ("i", "Why must all dimensions be in identical units before multiplying?", "To ensure unit consistency and avoid dimensional errors"),
                ("j", "If Length is in metres and Width is in metres, unit of Area is?", "Square metres (m²)")
            ]
        }
    ],
    "volume": [
        {
            "title": "Question 3: Volume of Prisms & Cylinders (V = Base Area × Height)",
            "instruction": "Calculate volume using V = Base Area × Height:",
            "items": [
                ("a", "Cuboid: Base 8cm × 5cm (area 40 cm²), Height 6cm. Volume = ?", "240 cm³ (40 × 6)"),
                ("b", "Triangular prism: Triangle base area 25 cm², Length 12 cm. Volume = ?", "300 cm³ (25 × 12)"),
                ("c", "Triangular prism: Base 6m, height 4m (area 12 m²), Length 10m. Volume = ?", "120 m³ (12 × 10)"),
                ("d", "Cylinder: Base area 50 cm², Height 8 cm. Volume = ?", "400 cm³ (50 × 8)"),
                ("e", "Cylinder: Radius 3 cm (Area = πr² = 3.14 × 9 = 28.26), Height 10 cm. Volume?", "282.6 cm³ (28.26 × 10)"),
                ("f", "Cylinder: Radius 5 m, Height 4 m (π = 3.14). Volume = ?", "314 m³ (3.14 × 25 × 4)"),
                ("g", "Cube with side length 4 cm. Volume = ?", "64 cm³ (4³)"),
                ("h", "Cube with side length 10 m. Volume = ?", "1,000 m³ (10³)"),
                ("i", "Cuboid volume is 180 cm³, Base is 6cm × 5cm (30 cm²). Height = ?", "6 cm (180 ÷ 30)"),
                ("j", "Liquid volume: 1 cm³ = 1 ml. A bottle of 750 cm³ holds how many ml?", "750 ml (0.75 L)")
            ]
        },
        {
            "title": "Question 4: Real-Life Packaging & Container Capacities",
            "instruction": "Solve volume and packing problems:",
            "items": [
                ("a", "Storage container: 6m × 2.5m × 2.4m. Volume = ?", "36 m³"),
                ("b", "Delivery van cargo space: 4m × 2m × 1.8m. Volume = ?", "14.4 m³"),
                ("c", "Small carton: 20cm × 10cm × 10cm = 2,000 cm³. How many fit in 24,000 cm³ box?", "12 cartons (24000 ÷ 2000)"),
                ("d", "Water trough: 2m × 0.5m × 0.4m = 0.4 m³. Capacity in litres (1 m³ = 1000L)?", "400 litres"),
                ("e", "Oil drum cylinder holds 200 litres. If 150 litres filled, litres remaining?", "50 litres"),
                ("f", "Soil needed for planter: 1.5m × 0.6m × 0.4m. Volume in m³?", "0.36 m³"),
                ("g", "Compost bags hold 60 litres (0.06 m³). Bags needed for 0.36 m³ planter?", "6 bags (0.36 ÷ 0.06)"),
                ("h", "Ice block: 10cm × 10cm × 5cm = 500 cm³. Density 0.92 g/cm³. Mass?", "460 g (500 × 0.92)")
            ]
        }
    ],
    "weight": [
        {
            "title": "Question 3: Grams, Kilograms & Tonnes Conversions",
            "instruction": "Convert between metric weight units (1 tonne = 1,000 kg; 1 kg = 1,000 g):",
            "items": [
                ("a", "Convert 2.4 kg to grams", "2,400 g (2.4 × 1000)"),
                ("b", "Convert 850 g to kilograms", "0.85 kg (850 ÷ 1000)"),
                ("c", "Convert 45 g to kilograms", "0.045 kg (45 ÷ 1000)"),
                ("d", "Convert 0.3 kg to grams", "300 g (0.3 × 1000)"),
                ("e", "Convert 1,750 kg to tonnes", "1.75 tonnes (1750 ÷ 1000)"),
                ("f", "Convert 0.8 tonnes to kilograms", "800 kg (0.8 × 1000)"),
                ("g", "Convert 3.25 tonnes to kilograms", "3,250 kg (3.25 × 1000)"),
                ("h", "Convert 500 kg to tonnes", "0.5 tonnes (500 ÷ 1000)"),
                ("i", "How many 250g butter blocks in a 2 kg catering tub?", "8 blocks (2000 ÷ 250)"),
                ("j", "How many 50kg cement sacks make 1 tonne (1,000 kg)?", "20 sacks (1000 ÷ 50)")
            ]
        },
        {
            "title": "Question 4: Workplace Load Limits & Baggage Allowances",
            "instruction": "Calculate total weights and check against threshold limits:",
            "items": [
                ("a", "Elevator weight limit 600 kg. 8 passengers average 72 kg each (576 kg). Is elevator overloaded?", "No (576 kg is within 600 kg limit)"),
                ("b", "Pallet holds 40 boxes weighing 12.5 kg each. Total load weight?", "500 kg (40 × 12.5)"),
                ("c", "Van tare weight 1,800 kg, gross vehicle weight limit 3,500 kg. Max payload?", "1,700 kg (3500 - 1800)"),
                ("d", "Van carries 30 sacks at 25 kg each (750 kg). Payload capacity remaining?", "950 kg (1700 - 750)"),
                ("e", "Airline baggage limit is 23 kg. Suitcase weighs 24.6 kg. Excess weight?", "1.6 kg overweight"),
                ("f", "Excess baggage fee is £12 per kg. Fee for 2 kg excess?", "£24.00"),
                ("g", "Parcel weighs 3.2 kg. Courier charge: £4 for first kg + £1.50 per extra kg. Total?", "£7.30 (£4 + £3.30)"),
                ("h", "Baby weight gain: 3.4 kg at birth, now 4.15 kg. Weight gained?", "0.75 kg (750 g)")
            ]
        }
    ]
}
