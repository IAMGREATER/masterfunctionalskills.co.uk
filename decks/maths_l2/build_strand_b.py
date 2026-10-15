#!/usr/bin/env python3
"""
Builder for Maths L2 Strand B: Measures, Shape and Space (Cards 19-36)
"""
import pprint
import xml.etree.ElementTree as ET

def wrap_svg(inner_content, height=170):
    svg = f'<svg viewBox="0 0 460 {height}" width="100%" height="{height}" xmlns="http://www.w3.org/2000/svg">\n{inner_content}\n</svg>'
    ET.fromstring(svg) # validate XML
    return svg

CARDS = [
    # 19. Perimeter of Composite 2D Shapes
    {
        "id": "m-l2-19",
        "number": 19,
        "title": "Perimeter of Composite Shapes",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Shape & Space",
        "strand_theme": "emerald",
        "dfe_code": "DfE L2.MSS18",
        "rule_heading": "Find Missing Sides, Then Add All",
        "rule_body": "1. Find every missing side: Horizontal missing side = Total width - given width. Vertical missing side = Total height - given height. 2. Sum ALL outer sides.",
        "svg_html": wrap_svg("""
          <polygon points="50,30 250,30 250,80 170,80 170,140 50,140" fill="#ecfdf5" stroke="#059669" stroke-width="2.5"/>
          <text x="150" y="22" font-size="12" font-weight="800" fill="#065f46" text-anchor="middle">10 m</text>
          <text x="265" y="60" font-size="12" font-weight="800" fill="#065f46" text-anchor="middle">4 m</text>
          <text x="210" y="74" font-size="11" font-weight="800" fill="#dc2626" text-anchor="middle">? = 4 m</text>
          <text x="185" y="115" font-size="11" font-weight="800" fill="#dc2626" text-anchor="middle">? = 5 m</text>
          <text x="110" y="155" font-size="12" font-weight="800" fill="#065f46" text-anchor="middle">6 m</text>
          <text x="35" y="90" font-size="12" font-weight="800" fill="#065f46" text-anchor="middle">9 m</text>
          <g transform="translate(290, 45)">
            <rect x="0" y="0" width="150" height="75" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>
            <text x="75" y="24" font-size="11" font-weight="800" fill="#0f172a" text-anchor="middle">Missing Sides:</text>
            <text x="75" y="44" font-size="10" font-weight="700" fill="#dc2626" text-anchor="middle">Width = 10 - 6 = 4 m</text>
            <text x="75" y="62" font-size="10" font-weight="700" fill="#dc2626" text-anchor="middle">Height = 9 - 4 = 5 m</text>
          </g>"""),
        "golden_rule": "Tick off each side as you add it to avoid counting sides twice or skipping one!",
        "watch_out": "Never add internal dotted lines when finding perimeter — perimeter is ONLY the outside border!",
        "challenge_prompt": "An L-shaped lawn has outer dimensions 12 m by 8 m, with an inset cut of 5 m wide and 3 m deep. What is the perimeter?",
        "answer_text": "Missing horizontal = 12 - 5 = 7 m. Missing vertical = 8 - 3 = 5 m. Perimeter = 12 + 8 + 7 + 3 + 5 + 5 = 40 m."
    },

    # 20. Circumference of a Circle
    {
        "id": "m-l2-20",
        "number": 20,
        "title": "Circumference of a Circle",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Shape & Space",
        "strand_theme": "emerald",
        "dfe_code": "DfE L2.MSS19",
        "rule_heading": "Circumference = 3.142 × Diameter",
        "rule_body": "Circumference is the distance around the outside edge of a circle. Diameter (d) goes straight across through center. Radius (r) is from center to edge (d = 2r).",
        "svg_html": wrap_svg("""
          <circle cx="150" cy="85" r="55" fill="#f0fdf4" stroke="#16a34a" stroke-width="2.5"/>
          <line x1="95" y1="85" x2="205" y2="85" stroke="#16a34a" stroke-width="2" stroke-dasharray="3,3"/>
          <circle cx="150" cy="85" r="3.5" fill="#16a34a"/>
          <text x="150" y="78" font-size="11" font-weight="800" fill="#15803d" text-anchor="middle">d = 14 cm</text>
          <g transform="translate(225, 30)">
            <rect x="0" y="0" width="215" height="110" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="107" y="28" font-size="12" font-weight="800" fill="#1e40af" text-anchor="middle">CIRCUMFERENCE</text>
            <text x="107" y="55" font-size="11" font-weight="700" fill="#0f172a" text-anchor="middle">C = 3.142 × Diameter</text>
            <text x="107" y="78" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">C = 3.142 × 14</text>
            <text x="107" y="100" font-size="13" font-weight="800" fill="#059669" text-anchor="middle">= 43.99 cm</text>
          </g>"""),
        "golden_rule": "Distance around outside: Circumference = 3.142 × Diameter!",
        "watch_out": "If given radius (r), you MUST double it before multiplying by 3.142 (Diameter = 2 × r)!",
        "challenge_prompt": "A circular bicycle wheel has a radius of 35 cm. How far does the bicycle travel in 1 full rotation of the wheel? (Use π = 3.142)",
        "answer_text": "Diameter = 35 × 2 = 70 cm. Circumference = 3.142 × 70 = 219.94 cm (or 2.20 m)."
    },

    # 21. Area of Triangle & Parallelogram
    {
        "id": "m-l2-21",
        "number": 21,
        "title": "Area of Triangle &amp; Parallelogram",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Shape & Space",
        "strand_theme": "emerald",
        "dfe_code": "DfE L2.MSS20",
        "rule_heading": "Triangle: 1/2 × b × h  |  Parallelogram: b × h",
        "rule_body": "Both use PERPENDICULAR vertical height at 90° to the base. Triangle is halved because two identical triangles make a parallelogram/rectangle.",
        "svg_html": wrap_svg("""
          <g transform="translate(30, 25)">
            <polygon points="10,110 150,110 60,30" fill="#eff6ff" stroke="#2563eb" stroke-width="2.2"/>
            <line x1="60" y1="30" x2="60" y2="110" stroke="#dc2626" stroke-width="2" stroke-dasharray="3,3"/>
            <text x="80" y="75" font-size="11" font-weight="800" fill="#dc2626">h</text>
            <text x="80" y="125" font-size="11" font-weight="800" fill="#1e40af" text-anchor="middle">base (b)</text>
            <text x="80" y="145" font-size="11" font-weight="800" fill="#2563eb" text-anchor="middle">Area = (b × h) ÷ 2</text>
          </g>
          <g transform="translate(230, 25)">
            <polygon points="40,30 180,30 150,110 10,110" fill="#fefce8" stroke="#ca8a04" stroke-width="2.2"/>
            <line x1="40" y1="30" x2="40" y2="110" stroke="#dc2626" stroke-width="2" stroke-dasharray="3,3"/>
            <text x="50" y="75" font-size="11" font-weight="800" fill="#dc2626">h</text>
            <text x="80" y="125" font-size="11" font-weight="800" fill="#a16207" text-anchor="middle">base (b)</text>
            <text x="95" y="145" font-size="11" font-weight="800" fill="#ca8a04" text-anchor="middle">Area = b × h (NO ÷ 2!)</text>
          </g>"""),
        "golden_rule": "Always use the perpendicular vertical height, NEVER the slanted side!",
        "watch_out": "Don't divide by 2 for a parallelogram — only halve for a triangle!",
        "challenge_prompt": "A triangular roof truss has a base of 8.4 m, perpendicular height of 3.5 m, and sloping sides of 5.5 m. Find its area.",
        "answer_text": "Discard sloping side 5.5 m. Area = 1/2 × base × height = 0.5 × 8.4 × 3.5 = 14.7 m²."
    },

    # 22. Area of a Trapezium
    {
        "id": "m-l2-22",
        "number": 22,
        "title": "Area of a Trapezium",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Shape & Space",
        "strand_theme": "emerald",
        "dfe_code": "DfE L2.MSS20",
        "rule_heading": "Area = 1/2(a + b)h",
        "rule_body": "1. Add parallel top and bottom sides (a + b). 2. Divide by 2 to get average parallel width. 3. Multiply by perpendicular vertical height (h).",
        "svg_html": wrap_svg("""
          <polygon points="120,40 280,40 360,135 60,135" fill="#fef3c7" stroke="#d97706" stroke-width="2.5"/>
          <line x1="120" y1="40" x2="120" y2="135" stroke="#059669" stroke-width="2.2" stroke-dasharray="4,4"/>
          <rect x="130" y="80" width="50" height="20" rx="4" fill="#ffffff" stroke="#059669"/>
          <text x="155" y="94" font-size="11" font-weight="800" fill="#059669" text-anchor="middle">h = 4 m</text>
          <text x="200" y="32" font-size="12" font-weight="800" fill="#2563eb" text-anchor="middle">a = 6 m</text>
          <text x="210" y="152" font-size="12" font-weight="800" fill="#2563eb" text-anchor="middle">b = 10 m</text>
          <rect x="330" y="55" width="85" height="22" rx="4" fill="#ffe4e6" stroke="#f43f5e"/>
          <text x="372" y="70" font-size="10" font-weight="800" fill="#be123c" text-anchor="middle">IGNORE SLANT!</text>"""),
        "golden_rule": "Half the sum of parallel sides times vertical height!",
        "watch_out": "Examiners include slanted side lengths as a trap. Cross out the slant immediately.",
        "challenge_prompt": "A pedestrian walkway has parallel edges of 7 m and 11 m, vertical width of 4.5 m, and slant edge of 5.2 m. Calculate its area.",
        "answer_text": "Ignore slant 5.2 m! Area = ((7 + 11) ÷ 2) × 4.5 = 9 × 4.5 = 40.5 m²."
    },

    # 23. Area of a Circle & Semicircle
    {
        "id": "m-l2-23",
        "number": 23,
        "title": "Area of a Circle &amp; Semicircle",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Shape & Space",
        "strand_theme": "emerald",
        "dfe_code": "DfE L2.MSS21",
        "rule_heading": "Circle: π r² = 3.142 × r²  |  Semicircle: (3.142 × r²) ÷ 2",
        "rule_body": "The ² symbol means squared: r² means radius multiplied by itself (r × r). Calculate r² (r × r) first, then multiply by 3.142 (Area = 3.142 × r²). If given diameter, halve it first to get radius. Semicircle area is half the full circle: (3.142 × r²) ÷ 2.",
        "svg_html": wrap_svg("""
          <circle cx="120" cy="85" r="50" fill="#eff6ff" stroke="#2563eb" stroke-width="2.5"/>
          <line x1="120" y1="85" x2="170" y2="85" stroke="#2563eb" stroke-width="2.5"/>
          <circle cx="120" cy="85" r="3.5" fill="#2563eb"/>
          <text x="145" y="78" font-size="11" font-weight="800" fill="#1e40af">r = 5 cm</text>
          <text x="120" y="152" font-size="11" font-weight="800" fill="#1e3a8a" text-anchor="middle">A = π r² = 3.142 × 5² = 3.142 × 5 × 5 = 78.55 cm²</text>
          <g transform="translate(240, 35)">
            <path d="M 10,80 A 60,60 0 0,1 130,80 Z" fill="#fdf2f8" stroke="#db2777" stroke-width="2.5"/>
            <text x="70" y="100" font-size="10.5" font-weight="800" fill="#be185d" text-anchor="middle">Semicircle Area = (π r²) ÷ 2</text>
            <text x="70" y="118" font-size="10" font-weight="700" fill="#64748b" text-anchor="middle">(r² means r × r = 5 × 5)</text>
          </g>"""),
        "golden_rule": "Circle Area = 3.142 × r² (where r² means Radius × Radius)!",
        "watch_out": "Do NOT multiply diameter by itself! Always halve diameter first to find radius.",
        "challenge_prompt": "A semicircular patio has a straight diameter of 8 metres. Calculate the area of the patio. (Use π = 3.142)",
        "answer_text": "Radius = 8 ÷ 2 = 4 m. Full circle = 3.142 × 4² = 3.142 × 4 × 4 = 50.272 m². Semicircle = 50.272 ÷ 2 = 25.14 m²."
    },

    # 24. Area of Composite Shapes
    {
        "id": "m-l2-24",
        "number": 24,
        "title": "Area of Composite Shapes",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Shape & Space",
        "strand_theme": "emerald",
        "dfe_code": "DfE L2.MSS22",
        "rule_heading": "Split into Simpler Shapes, Then Add",
        "rule_body": "1. Split compound floor plan into non-overlapping rectangles and triangles with dashed lines. 2. Calculate area of each individual section. 3. Sum all areas.",
        "svg_html": wrap_svg("""
          <polygon points="50,40 220,40 220,130 50,130" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>
          <polygon points="220,40 330,85 220,130" fill="#fefce8" stroke="#ca8a04" stroke-width="2"/>
          <line x1="220" y1="40" x2="220" y2="130" stroke="#475569" stroke-width="2" stroke-dasharray="4,4"/>
          <text x="135" y="88" font-size="13" font-weight="800" fill="#1e40af" text-anchor="middle">Shape A: 60 m²</text>
          <text x="260" y="88" font-size="12" font-weight="800" fill="#a16207" text-anchor="middle">Shape B: 25 m²</text>
          <g transform="translate(140, 142)">
            <text x="80" y="15" font-size="13" font-weight="900" fill="#059669" text-anchor="middle">Total Area = 60 + 25 = 85 m²</text>
          </g>"""),
        "golden_rule": "Draw clear dotted split lines and label areas 'A' and 'B'!",
        "watch_out": "Check if a section is CUT OUT (e.g. pond in a lawn). If cut out, SUBTRACT its area.",
        "challenge_prompt": "A warehouse floor is a 15 m by 10 m rectangle with a semicircular loading bay of diameter 6 m extending outwards on one side. What is the total area? (π = 3.14)",
        "answer_text": "Rectangle = 15 × 10 = 150 m². Semicircle radius = 3 m. Semicircle area = (3.14 × 3²) ÷ 2 = 14.13 m². Total area = 150 + 14.13 = 164.13 m²."
    },

    # 25. Volume of Cuboid & Prism
    {
        "id": "m-l2-25",
        "number": 25,
        "title": "Volume of Cuboids &amp; Prisms",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Shape & Space",
        "strand_theme": "emerald",
        "dfe_code": "DfE L2.MSS23",
        "rule_heading": "Volume = Cross-Sectional Area × Length",
        "rule_body": "A prism has the same 2D shape all the way through: 1. Find area of the front face (cross-section). 2. Multiply by the 3D length/depth. Units are cubic (cm³, m³).",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <polygon points="10,40 100,40 100,110 10,110" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
            <polygon points="100,40 150,15 150,85 100,110" fill="#93c5fd" stroke="#2563eb" stroke-width="2"/>
            <polygon points="10,40 60,15 150,15 100,40" fill="#bfdbfe" stroke="#2563eb" stroke-width="2"/>
            <text x="55" y="80" font-size="11" font-weight="800" fill="#1e40af" text-anchor="middle">L × W × H</text>
            <text x="80" y="130" font-size="11" font-weight="800" fill="#1e3a8a" text-anchor="middle">Cuboid</text>
          </g>
          <g transform="translate(240, 20)">
            <polygon points="10,110 80,110 45,30" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
            <polygon points="80,110 150,75 115,10 45,30" fill="#fde68a" stroke="#d97706" stroke-width="2"/>
            <text x="45" y="85" font-size="10" font-weight="800" fill="#b45309" text-anchor="middle">Triangle</text>
            <text x="80" y="130" font-size="11" font-weight="800" fill="#b45309" text-anchor="middle">Triangular Prism: Area × Length</text>
          </g>"""),
        "golden_rule": "Always multiply the front face area by the full length/depth!",
        "watch_out": "Don't confuse Volume (3D space in m³) with Surface Area (2D skin in m²).",
        "challenge_prompt": "A triangular prism has a cross-section triangle with base 6 cm and height 4 cm. Its length is 15 cm. What is its volume?",
        "answer_text": "Triangle area = 1/2 × 6 × 4 = 12 cm². Volume = Cross-section × Length = 12 × 15 = 180 cm³."
    },

    # 26. Volume of a Cylinder
    {
        "id": "m-l2-26",
        "number": 26,
        "title": "Volume of a Cylinder",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Shape & Space",
        "strand_theme": "emerald",
        "dfe_code": "DfE L2.MSS24",
        "rule_heading": "Volume = π r² h = 3.142 × r² × h",
        "rule_body": "A cylinder is a circular prism: 1. Circular base area = π r² = 3.142 × r² (where r² means r × r). 2. Multiply by vertical height (h): Volume = 3.142 × r² × h. Units are cubic (cm³, m³), where ³ means cubed (x × x × x). 1,000 cm³ = 1 Litre.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <ellipse cx="60" cy="30" rx="55" ry="18" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
            <rect x="5" y="30" width="110" height="75" fill="#f0f9ff"/>
            <line x1="5" y1="30" x2="5" y2="105" stroke="#0284c7" stroke-width="2"/>
            <line x1="115" y1="30" x2="115" y2="105" stroke="#0284c7" stroke-width="2"/>
            <ellipse cx="60" cy="105" rx="55" ry="18" fill="#bae6fd" stroke="#0284c7" stroke-width="2"/>
            <line x1="60" y1="30" x2="115" y2="30" stroke="#0369a1" stroke-width="2"/>
            <text x="85" y="24" font-size="10" font-weight="800" fill="#0369a1">r</text>
            <text x="130" y="70" font-size="11" font-weight="800" fill="#0369a1">h</text>
          </g>
          <g transform="translate(210, 30)">
            <rect x="0" y="0" width="220" height="105" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="110" y="24" font-size="12" font-weight="900" fill="#1e40af" text-anchor="middle">CYLINDER FORMULA</text>
            <text x="110" y="48" font-size="11.5" font-weight="800" fill="#0f172a" text-anchor="middle">V = π r² h = 3.142 × r² × h</text>
            <text x="110" y="68" font-size="10" font-weight="700" fill="#2563eb" text-anchor="middle">(r² means radius × radius)</text>
            <text x="110" y="90" font-size="11" font-weight="700" fill="#059669" text-anchor="middle">1,000 cm³ = 1 Litre</text>
          </g>"""),
        "golden_rule": "Cylinder Volume = 3.142 × r² × h (where r² means Radius × Radius)!",
        "watch_out": "If given diameter, divide by 2 first to get radius! (r = d ÷ 2).",
        "challenge_prompt": "A hot water tank is a cylinder with diameter 60 cm and height 120 cm. Calculate its capacity in litres (π = 3.14).",
        "answer_text": "Radius = 60 ÷ 2 = 30 cm. Volume = 3.14 × 30² × 120 = 3.14 × (30 × 30) × 120 = 3.14 × 900 × 120 = 339,120 cm³. Litres = 339,120 ÷ 1,000 = 339.12 L."
    },

    # 27. Total Surface Area of a Cuboid
    {
        "id": "m-l2-27",
        "number": 27,
        "title": "Surface Area of a Cuboid",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Shape & Space",
        "strand_theme": "emerald",
        "dfe_code": "DfE L2.MSS25",
        "rule_heading": "SA = 2(lw + lh + wh)",
        "rule_body": "A cuboid has 6 rectangular faces in 3 identical opposite pairs: 1. Front &amp; Back (l × h) × 2. 2. Top &amp; Bottom (l × w) × 2. 3. Left &amp; Right (w × h) × 2. Sum all 6 faces.",
        "svg_html": wrap_svg("""
          <rect x="30" y="20" width="400" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
          <text x="230" y="42" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">Box dimensions: 5 m long, 4 m wide, 3 m high</text>
          <g transform="translate(60, 60)">
            <rect x="0" y="0" width="95" height="40" rx="4" fill="#dbeafe"/><text x="47" y="24" font-size="10" font-weight="800" fill="#1e40af" text-anchor="middle">Top/Bot: 2×(5×4)=40</text>
            <rect x="110" y="0" width="105" height="40" rx="4" fill="#dcfce7"/><text x="162" y="24" font-size="10" font-weight="800" fill="#15803d" text-anchor="middle">Front/Back: 2×(5×3)=30</text>
            <rect x="230" y="0" width="95" height="40" rx="4" fill="#fef3c7"/><text x="277" y="24" font-size="10" font-weight="800" fill="#b45309" text-anchor="middle">Sides: 2×(4×3)=24</text>
          </g>
          <text x="230" y="132" font-size="13" font-weight="900" fill="#2563eb" text-anchor="middle">Total Surface Area = 40 + 30 + 24 = 94 m²</text>"""),
        "golden_rule": "Calculate 3 faces, add them up, then multiply by 2!",
        "watch_out": "If painting a room, remember to EXCLUDE the floor (or ceiling and windows) if instructed!",
        "challenge_prompt": "A storage crate with an open top (no lid) is 2 m long, 1.5 m wide, and 1 m high. What is its outside surface area?",
        "answer_text": "Open top = 1 bottom + 2 front/backs + 2 sides. Bottom = 2 × 1.5 = 3 m². Front/Back = 2 × (2 × 1) = 4 m². Ends = 2 × (1.5 × 1) = 3 m². Total SA = 3 + 4 + 3 = 10 m²."
    },

    # 28. Total Surface Area of a Cylinder
    {
        "id": "m-l2-28",
        "number": 28,
        "title": "Surface Area of a Cylinder",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Shape & Space",
        "strand_theme": "emerald",
        "dfe_code": "DfE L2.MSS25",
        "rule_heading": "Total SA = 2πr² + πdh = (2 × 3.142 × r²) + (3.142 × d × h)",
        "rule_body": "A closed cylinder net has 3 parts: Two circular ends (2 × 3.142 × r², where r² means r × r) plus one unwrapped rectangular body (3.142 × d × h).",
        "svg_html": wrap_svg("""
          <g transform="translate(10, 0)">
            <!-- Cylinder Net Body -->
            <rect x="25" y="56" width="175" height="58" fill="#eff6ff" stroke="#3b82f6" stroke-width="2.2"/>
            <text x="112" y="83" font-size="11.5" font-weight="800" fill="#1e40af" text-anchor="middle">Body: 3.142 × d × h</text>
            <text x="112" y="98" font-size="9" font-weight="700" fill="#2563eb" text-anchor="middle">(Circumference × Height)</text>

            <!-- Top Circle End (Large & Proportional) -->
            <circle cx="112" cy="30" r="26" fill="#bfdbfe" stroke="#1d4ed8" stroke-width="2.2"/>
            <text x="112" y="34" font-size="11" font-weight="800" fill="#1e40af" text-anchor="middle">πr²</text>
            <text x="150" y="34" font-size="10" font-weight="800" fill="#1d4ed8">3.142×r²</text>

            <!-- Bottom Circle End (Large & Proportional) -->
            <circle cx="112" cy="140" r="26" fill="#bfdbfe" stroke="#1d4ed8" stroke-width="2.2"/>
            <text x="112" y="144" font-size="11" font-weight="800" fill="#1e40af" text-anchor="middle">πr²</text>
            <text x="150" y="144" font-size="10" font-weight="800" fill="#1d4ed8">3.142×r²</text>
          </g>

          <!-- Right Formula Card -->
          <g transform="translate(240, 24)">
            <rect x="0" y="0" width="205" height="122" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="102" y="24" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">CLOSED CYLINDER NET</text>
            <rect x="12" y="36" width="181" height="32" rx="6" fill="#dbeafe" stroke="#bfdbfe"/>
            <text x="102" y="56" font-size="10.5" font-weight="800" fill="#1e40af" text-anchor="middle">2 Ends = 2 × 3.142 × r²</text>
            <rect x="12" y="74" width="181" height="32" rx="6" fill="#dcfce7" stroke="#bbf7d0"/>
            <text x="102" y="94" font-size="10.5" font-weight="800" fill="#15803d" text-anchor="middle">+ Body = 3.142 × d × h</text>
            <text x="102" y="116" font-size="9" font-weight="700" fill="#64748b" text-anchor="middle">(r² means radius × radius)</text>
          </g>"""),
        "golden_rule": "Closed Cylinder: 2 circular ends (2 × 3.142 × r²) + curved body (3.142 × d × h)!",
        "watch_out": "Check if the pipe or can is OPEN at one or both ends — only add circular ends that actually exist.",
        "challenge_prompt": "A closed tin can has radius 4 cm and height 10 cm. Find total surface area to 1 decimal place (π = 3.142).",
        "answer_text": "2 Ends = 2 × 3.142 × 4² = 2 × 3.142 × 16 = 100.54 cm². Curved body = 3.142 × 8 × 10 = 251.36 cm². Total SA = 100.54 + 251.36 = 351.9 cm²."
    },

    # 29. Metric Unit Conversions
    {
        "id": "m-l2-29",
        "number": 29,
        "title": "Metric Unit Conversions",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Shape & Space",
        "strand_theme": "emerald",
        "dfe_code": "DfE L2.MSS26",
        "rule_heading": "Length, Mass &amp; Capacity Ladders",
        "rule_body": "Big unit to small unit = MULTIPLY (×). Small unit to big unit = DIVIDE (÷). Length: km (×1000) m (×100) cm (×10) mm. Mass: tonne (×1000) kg (×1000) g. Volume: L (×1000) mL.",
        "svg_html": wrap_svg("""
          <g transform="translate(30, 20)">
            <rect x="0" y="0" width="400" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="200" y="28" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">METRIC CONVERSION LADDERS</text>
            <text x="30" y="60" font-size="11" font-weight="700" fill="#2563eb">1 km = 1,000 m  •  1 m = 100 cm  •  1 cm = 10 mm</text>
            <text x="30" y="85" font-size="11" font-weight="700" fill="#059669">1 tonne = 1,000 kg  •  1 kg = 1,000 g</text>
            <text x="30" y="110" font-size="11" font-weight="700" fill="#d97706">1 Litre = 1,000 ml  •  1 Litre = 1,000 cm³</text>
          </g>"""),
        "golden_rule": "Kilo = 1,000 • Centi = 1/100 • Milli = 1/1,000.",
        "watch_out": "Don't divide 3.5 m by 100 to get cm! When going from metres to cm, you get MORE units (× 100 = 350 cm).",
        "challenge_prompt": "A patient requires 450 mg of medication per dose, 3 times a day. How many grams of medication is taken in 4 days?",
        "answer_text": "Per day = 450 × 3 = 1,350 mg. In 4 days = 1,350 × 4 = 5,400 mg. Grams = 5,400 ÷ 1,000 = 5.4 g."
    },

    # 30. Converting Square & Cubic Units
    {
        "id": "m-l2-30",
        "number": 30,
        "title": "Converting Square &amp; Cubic Units",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Shape & Space",
        "strand_theme": "emerald",
        "dfe_code": "DfE L2.MSS27",
        "rule_heading": "1 m² = 10,000 cm²  |  1 m³ = 1,000,000 cm³",
        "rule_body": "To convert square units, apply the linear conversion TWICE (100² = 10,000). To convert cubic units, apply conversion THREE TIMES (100³ = 1,000,000).",
        "svg_html": wrap_svg("""
          <g transform="translate(30, 20)">
            <rect x="0" y="0" width="190" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="95" y="26" font-size="12" font-weight="800" fill="#1e40af" text-anchor="middle">SQUARE UNITS (m²)</text>
            <text x="95" y="55" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">1 m = 100 cm</text>
            <text x="95" y="80" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">1 m² = 100 × 100 cm</text>
            <rect x="15" y="95" width="160" height="24" rx="4" fill="#3b82f6"/>
            <text x="95" y="111" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">1 m² = 10,000 cm²</text>
          </g>
          <g transform="translate(240, 20)">
            <rect x="0" y="0" width="190" height="130" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
            <text x="95" y="26" font-size="12" font-weight="800" fill="#15803d" text-anchor="middle">CUBIC UNITS (m³)</text>
            <text x="95" y="55" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">1 m = 100 cm</text>
            <text x="95" y="80" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">1 m³ = 100 × 100 × 100</text>
            <rect x="15" y="95" width="160" height="24" rx="4" fill="#16a34a"/>
            <text x="95" y="111" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">1 m³ = 1,000,000 cm³</text>
          </g>"""),
        "golden_rule": "Square the conversion factor for area; cube it for volume!",
        "watch_out": "1 m² is NOT 100 cm²! That is the most failed unit conversion in Level 2 exams.",
        "challenge_prompt": "Convert 3.5 m² into cm².",
        "answer_text": "1 m² = 10,000 cm². 3.5 × 10,000 = 35,000 cm²."
    },

    # 31. Metric to Imperial Approximations
    {
        "id": "m-l2-31",
        "number": 31,
        "title": "Metric to Imperial Approximations",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Shape & Space",
        "strand_theme": "emerald",
        "dfe_code": "DfE L2.MSS28",
        "rule_heading": "Core UK Benchmark Ratios",
        "rule_body": "Memorise standard conversion factors: 5 miles ≈ 8 km (1 mile ≈ 1.6 km). 1 inch ≈ 2.5 cm. 1 kg ≈ 2.2 lbs. 1 gallon ≈ 4.5 litres. 1 foot = 12 inches ≈ 30 cm.",
        "svg_html": wrap_svg("""
          <g transform="translate(30, 15)">
            <rect x="0" y="0" width="400" height="140" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="200" y="26" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">KEY IMPERIAL BENCHMARKS</text>
            <text x="40" y="55" font-size="11" font-weight="700" fill="#2563eb">Distance: 5 miles ≈ 8 km  (or 1 mile ≈ 1.6 km)</text>
            <text x="40" y="80" font-size="11" font-weight="700" fill="#059669">Weight: 1 kg ≈ 2.2 pounds (lbs)</text>
            <text x="40" y="105" font-size="11" font-weight="700" fill="#d97706">Liquid: 1 gallon ≈ 4.5 litres  •  1 pint ≈ 568 ml</text>
            <text x="40" y="128" font-size="11" font-weight="700" fill="#7c3aed">Length: 1 inch ≈ 2.54 cm  •  1 foot ≈ 30 cm</text>
          </g>"""),
        "golden_rule": "5 miles = 8 km. To convert km to miles, multiply by 5 then divide by 8.",
        "watch_out": "Kilograms are HEAVIER than pounds! 10 kg is about 22 lbs, NOT 4.5 lbs.",
        "challenge_prompt": "A UK highway speed limit is 70 mph. A foreign driver's speedometer is in km/h. What is 70 mph in km/h? (5 miles ≈ 8 km)",
        "answer_text": "70 ÷ 5 = 14. 14 × 8 = 112 km/h."
    },

    # 32. Speed, Distance, Time
    {
        "id": "m-l2-32",
        "number": 32,
        "title": "Speed, Distance &amp; Time",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Shape & Space",
        "strand_theme": "emerald",
        "dfe_code": "DfE L2.MSS29",
        "rule_heading": "D = S × T  |  Decimal Time Warning",
        "rule_body": "Distance = Speed × Time. Speed = Distance ÷ Time. Time = Distance ÷ Speed. Decimal hours must be converted: Multiply decimal minutes by 60 (0.4 hrs = 24 mins).",
        "svg_html": wrap_svg("""
          <g transform="translate(25, 12)">
            <polygon points="100,5 10,140 190,140" fill="#f8fafc" stroke="#0f172a" stroke-width="3"/>
            <line x1="45" y1="80" x2="155" y2="80" stroke="#0f172a" stroke-width="3"/>
            <line x1="100" y1="80" x2="100" y2="140" stroke="#0f172a" stroke-width="3"/>
            <text x="32" y="74" font-size="14" font-weight="900" fill="#64748b">÷</text>
            <text x="168" y="74" font-size="14" font-weight="900" fill="#64748b">÷</text>
            <text x="100" y="115" font-size="16" font-weight="900" fill="#64748b" text-anchor="middle">×</text>
            <circle cx="100" cy="46" r="24" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
            <text x="100" y="54" font-size="22" font-weight="900" fill="#1e40af" text-anchor="middle">D</text>
            <circle cx="58" cy="112" r="22" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
            <text x="58" y="119" font-size="20" font-weight="900" fill="#b45309" text-anchor="middle">S</text>
            <circle cx="142" cy="112" r="22" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
            <text x="142" y="119" font-size="20" font-weight="900" fill="#15803d" text-anchor="middle">T</text>
          </g>
          <g transform="translate(235, 15)">
            <rect x="0" y="0" width="200" height="135" rx="8" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.8"/>
            <text x="100" y="24" font-size="11.5" font-weight="900" fill="#b45309" text-anchor="middle">S-D-T FORMULAS</text>
            <rect x="10" y="32" width="180" height="24" rx="4" fill="#2563eb"/>
            <text x="100" y="48" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">Distance = Speed × Time</text>
            <rect x="10" y="60" width="180" height="24" rx="4" fill="#d97706"/>
            <text x="100" y="76" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">Speed = Distance ÷ Time</text>
            <rect x="10" y="88" width="180" height="24" rx="4" fill="#16a34a"/>
            <text x="100" y="104" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">Time = Distance ÷ Speed</text>
            <text x="100" y="125" font-size="9.5" font-weight="800" fill="#dc2626" text-anchor="middle">⚠️ 45m = 0.75h (NEVER 0.45!)</text>
          </g>"""),
        "golden_rule": "Minutes to decimal: Divide by 60. Decimal to minutes: Multiply by 60.",
        "watch_out": "2 hours 45 minutes on a calculator is 2.75, NEVER 2.45!",
        "challenge_prompt": "A train travels 140 miles at an average speed of 56 mph. How long does the journey take in hours and minutes?",
        "answer_text": "Time = Distance ÷ Speed = 140 ÷ 56 = 2.5 hours. 0.5 hours × 60 = 30 minutes. Journey time = 2 hours 30 minutes."
    },

    # 33. Density, Mass, Volume
    {
        "id": "m-l2-33",
        "number": 33,
        "title": "Density, Mass &amp; Volume",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Shape & Space",
        "strand_theme": "emerald",
        "dfe_code": "DfE L2.MSS30",
        "rule_heading": "M = D × V  (MDV Triangle)",
        "rule_body": "Mass = Density × Volume. Density = Mass ÷ Volume (written in g/cm³ or kg/m³). Volume = Mass ÷ Density. Density measures how tightly matter is packed.",
        "svg_html": wrap_svg("""
          <g transform="translate(25, 12)">
            <polygon points="100,5 10,140 190,140" fill="#f8fafc" stroke="#0f172a" stroke-width="3"/>
            <line x1="45" y1="80" x2="155" y2="80" stroke="#0f172a" stroke-width="3"/>
            <line x1="100" y1="80" x2="100" y2="140" stroke="#0f172a" stroke-width="3"/>
            <text x="32" y="74" font-size="14" font-weight="900" fill="#64748b">÷</text>
            <text x="168" y="74" font-size="14" font-weight="900" fill="#64748b">÷</text>
            <text x="100" y="115" font-size="16" font-weight="900" fill="#64748b" text-anchor="middle">×</text>
            <circle cx="100" cy="46" r="24" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
            <text x="100" y="54" font-size="22" font-weight="900" fill="#5b21b6" text-anchor="middle">M</text>
            <circle cx="58" cy="112" r="22" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
            <text x="58" y="119" font-size="20" font-weight="900" fill="#0369a1" text-anchor="middle">D</text>
            <circle cx="142" cy="112" r="22" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
            <text x="142" y="119" font-size="20" font-weight="900" fill="#15803d" text-anchor="middle">V</text>
          </g>
          <g transform="translate(235, 15)">
            <rect x="0" y="0" width="200" height="135" rx="8" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.8"/>
            <text x="100" y="24" font-size="11.5" font-weight="900" fill="#5b21b6" text-anchor="middle">M-D-V FORMULAS</text>
            <rect x="10" y="32" width="180" height="24" rx="4" fill="#7c3aed"/>
            <text x="100" y="48" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">Mass = Density × Volume</text>
            <rect x="10" y="60" width="180" height="24" rx="4" fill="#0284c7"/>
            <text x="100" y="76" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">Density = Mass ÷ Volume</text>
            <rect x="10" y="88" width="180" height="24" rx="4" fill="#16a34a"/>
            <text x="100" y="104" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">Volume = Mass ÷ Density</text>
            <text x="100" y="125" font-size="9.5" font-weight="800" fill="#4338ca" text-anchor="middle">⚖️ g with cm³ | kg with m³</text>
          </g>"""),
        "golden_rule": "Remember: 'Department of Motor Vehicles' (D-M-V) or Mass on top!",
        "watch_out": "Check units: If density is in g/cm³, volume must be in cm³ and mass must be in grams.",
        "challenge_prompt": "A solid brass statue has a volume of 450 cm³ and a density of 8.5 g/cm³. What is the mass of the statue in kilograms?",
        "answer_text": "Mass = Density × Volume = 8.5 × 450 = 3,825 grams. In kilograms = 3,825 ÷ 1,000 = 3.825 kg."
    },

    # 34. Scale Drawings & Maps
    {
        "id": "m-l2-34",
        "number": 34,
        "title": "Scale Drawings &amp; Maps",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Shape & Space",
        "strand_theme": "emerald",
        "dfe_code": "DfE L2.MSS31",
        "rule_heading": "Scale Ratios (1 : n)",
        "rule_body": "Scale 1 : 50 means 1 cm on paper represents 50 cm in real life (0.5 m). Scale 1 : 25,000 means 1 cm = 250 m. Map to Real: MULTIPLY. Real to Map: DIVIDE.",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="90" y="26" font-size="12" font-weight="800" fill="#1e40af" text-anchor="middle">ARCHITECTURAL: 1:50</text>
            <text x="15" y="55" font-size="11" font-weight="700" fill="#0f172a">1 cm on plan = 50 cm real</text>
            <text x="15" y="80" font-size="11" font-weight="700" fill="#0f172a">50 cm = 0.5 metres</text>
            <rect x="15" y="92" width="150" height="24" rx="4" fill="#3b82f6"/>
            <text x="90" y="108" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">6 cm on plan = 3.0 m</text>
          </g>
          <g transform="translate(240, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.8"/>
            <text x="90" y="26" font-size="12" font-weight="800" fill="#b45309" text-anchor="middle">MAP SCALE: 1:25,000</text>
            <text x="15" y="55" font-size="11" font-weight="700" fill="#0f172a">1 cm = 25,000 cm</text>
            <text x="15" y="80" font-size="11" font-weight="700" fill="#0f172a">25,000 cm ÷ 100 = 250 m</text>
            <rect x="15" y="92" width="150" height="24" rx="4" fill="#f59e0b"/>
            <text x="90" y="108" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">4 cm = 1,000 m (1 km)</text>
          </g>"""),
        "golden_rule": "Both sides of a scale ratio start in the SAME unit (centimetres)!",
        "watch_out": "Always convert cm to metres (÷ 100) or km (÷ 100,000) for real-world answers.",
        "challenge_prompt": "On an architectural blueprint with scale 1 : 200, a sports hall wall measures 8.5 cm. What is the actual length of the wall in metres?",
        "answer_text": "Real length = 8.5 × 200 = 1,700 cm. In metres = 1,700 ÷ 100 = 17 metres."
    },

    # 35. Bearings (3 Figures)
    {
        "id": "m-l2-35",
        "number": 35,
        "title": "Bearings (3-Figure Bearings)",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Shape & Space",
        "strand_theme": "emerald",
        "dfe_code": "DfE L2.MSS32",
        "rule_heading": "North • Clockwise • 3 Figures",
        "rule_body": "1. Measure angle clockwise starting from North line (000°). 2. Always write using THREE digits (e.g. 045°, 090°, 260°). Back bearing = Add or subtract 180°.",
        "svg_html": wrap_svg("""
          <g transform="translate(130, 20)">
            <circle cx="100" cy="65" r="55" fill="#f8fafc" stroke="#334155" stroke-width="2"/>
            <line x1="100" y1="10" x2="100" y2="65" stroke="#dc2626" stroke-width="2.5"/>
            <polygon points="100,5 96,15 104,15" fill="#dc2626"/>
            <text x="100" y="0" font-size="12" font-weight="900" fill="#dc2626" text-anchor="middle">N (000°)</text>
            <line x1="100" y1="65" x2="145" y2="30" stroke="#2563eb" stroke-width="2.5"/>
            <path d="M 100,35 A 30,30 0 0,1 125,48" fill="none" stroke="#2563eb" stroke-width="2"/>
            <text x="120" y="32" font-size="11" font-weight="800" fill="#2563eb">055°</text>
          </g>"""),
        "golden_rule": "Always 3 digits! 55° must be written as 055°.",
        "watch_out": "Check which location the bearing is measured FROM: 'Bearing of B from A' means draw North at A!",
        "challenge_prompt": "The bearing of town B from town A is 072°. What is the back-bearing of town A from town B?",
        "answer_text": "Since 072° < 180°, add 180°: Back bearing = 072° + 180° = 252°."
    },

    # 36. Plans and Elevations
    {
        "id": "m-l2-36",
        "number": 36,
        "title": "Plans &amp; Elevations",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Shape & Space",
        "strand_theme": "emerald",
        "dfe_code": "DfE L2.MSS33",
        "rule_heading": "Plan View • Front • Side Elevation",
        "rule_body": "Plan View = Looking straight down from the bird's eye view. Front Elevation = Looking straight from front. Side Elevation = Looking straight from side.",
        "svg_html": wrap_svg("""
          <g transform="translate(30, 20)">
            <rect x="0" y="0" width="120" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>
            <text x="60" y="24" font-size="11" font-weight="800" fill="#1e40af" text-anchor="middle">PLAN VIEW</text>
            <rect x="25" y="40" width="70" height="60" fill="#93c5fd" stroke="#2563eb"/>
            <text x="60" y="115" font-size="9.5" font-weight="700" fill="#64748b" text-anchor="middle">From Above</text>
          </g>
          <g transform="translate(170, 20)">
            <rect x="0" y="0" width="120" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>
            <text x="60" y="24" font-size="11" font-weight="800" fill="#15803d" text-anchor="middle">FRONT ELEVATION</text>
            <rect x="25" y="55" width="70" height="45" fill="#86efac" stroke="#16a34a"/>
            <text x="60" y="115" font-size="9.5" font-weight="700" fill="#64748b" text-anchor="middle">From Front</text>
          </g>
          <g transform="translate(310, 20)">
            <rect x="0" y="0" width="120" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>
            <text x="60" y="24" font-size="11" font-weight="800" fill="#b45309" text-anchor="middle">SIDE ELEVATION</text>
            <rect x="35" y="55" width="50" height="45" fill="#fde68a" stroke="#d97706"/>
            <text x="60" y="115" font-size="9.5" font-weight="700" fill="#64748b" text-anchor="middle">From Side</text>
          </g>"""),
        "golden_rule": "Draw each 2D projection as if you are standing directly in line with that face!",
        "watch_out": "Plan view NEVER shows height — it only shows width and depth.",
        "challenge_prompt": "A 3D stepped staircase block is 3 cubes wide, 2 cubes deep, and 3 cubes high. Which 2D elevation shows the step pattern?",
        "answer_text": "The side elevation shows the step profile (staircase outline)."
    }
]

if __name__ == "__main__":
    with open('decks/maths_l2/strand_b.py', 'w') as f:
        f.write('\"\"\"Strand B: Measures, Shape and Space (Cards 19-36)\"\"\"\n')
        f.write('CARDS = ' + pprint.pformat(CARDS, indent=2, width=120) + '\n')
    print(f"Successfully generated Strand B ({len(CARDS)} cards)!")
