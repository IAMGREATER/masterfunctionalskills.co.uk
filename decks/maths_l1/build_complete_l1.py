#!/usr/bin/env python3
"""
Complete Builder for Deck 2: Functional Skills Maths - Level 1 (38 Cards)
Generates strand_a.py, strand_b.py, strand_c.py and __init__.py.
"""
import pprint
import xml.etree.ElementTree as ET

def wrap_svg(inner_content, height=170):
    svg = f'<svg viewBox="0 0 460 {height}" width="100%" height="{height}" xmlns="http://www.w3.org/2000/svg">\n{inner_content}\n</svg>'
    ET.fromstring(svg)
    return svg

# Import Strand A from build_maths_l1.py
from build_maths_l1 import CARDS_A

CARDS_B = [
    # 15. Perimeter of a Rectangle & Square
    {
        "id": "m-l1-15",
        "number": 15,
        "title": "Perimeter of Rectangle &amp; Square",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Measures & Space",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.MSS15",
        "rule_heading": "Add All Four Outside Edges",
        "rule_body": "Perimeter is the total boundary distance around a 2D shape. Rectangle: Perimeter = Length + Width + Length + Width = 2l + 2w. Units are linear (cm, m).",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="25" width="220" height="90" rx="6" fill="#f0f9ff" stroke="#0284c7" stroke-width="2.5"/>
            <text x="110" y="15" font-size="12" font-weight="800" fill="#0369a1" text-anchor="middle">8 m</text>
            <text x="110" y="130" font-size="12" font-weight="800" fill="#0369a1" text-anchor="middle">8 m</text>
            <text x="-15" y="75" font-size="12" font-weight="800" fill="#0369a1" text-anchor="middle">5 m</text>
            <text x="235" y="75" font-size="12" font-weight="800" fill="#0369a1" text-anchor="middle">5 m</text>
            <text x="110" y="75" font-size="13" font-weight="900" fill="#0f172a" text-anchor="middle">P = 8 + 5 + 8 + 5 = 26 m</text>
          </g>"""),
        "golden_rule": "Perimeter is the border fence around the shape!",
        "watch_out": "Don't just add 8 + 5 = 13! A rectangle has FOUR sides, so you must add all 4 sides.",
        "challenge_prompt": "A square garden has a side length of 7.5 metres. How many metres of fencing are needed to go all the way around?",
        "answer_text": "A square has 4 equal sides. Perimeter = 4 × 7.5 = 30 metres."
    },

    # 16. Perimeter of Simple Regular Polygons
    {
        "id": "m-l1-16",
        "number": 16,
        "title": "Perimeter of Regular Polygons",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Measures & Space",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.MSS15",
        "rule_heading": "Side Length × Number of Sides",
        "rule_body": "A 'regular' polygon has sides that are ALL EQUAL in length: Equilateral Triangle = 3 × side. Pentagon = 5 × side. Hexagon = 6 × side. Octagon = 8 × side.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <polygon points="60,20 120,20 150,70 120,120 60,120 30,70" fill="#f0fdf4" stroke="#16a34a" stroke-width="2.5"/>
            <text x="90" y="15" font-size="11" font-weight="800" fill="#15803d" text-anchor="middle">4 cm</text>
            <g transform="translate(200, 35)">
              <rect x="0" y="0" width="170" height="75" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>
              <text x="85" y="24" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">Regular Hexagon</text>
              <text x="85" y="46" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">6 equal sides of 4 cm</text>
              <text x="85" y="65" font-size="12" font-weight="900" fill="#16a34a" text-anchor="middle">Perimeter = 6 × 4 = 24 cm</text>
            </g>
          </g>"""),
        "golden_rule": "Regular means all sides and angles are identical!",
        "watch_out": "Don't count the sides incorrectly: Hexagon = 6, Octagon = 8, Pentagon = 5.",
        "challenge_prompt": "A stop sign is a regular octagon with each side measuring 25 cm. What is the total perimeter in metres?",
        "answer_text": "Octagon has 8 sides. Perimeter = 8 × 25 cm = 200 cm = 2.0 metres."
    },

    # 17. Area of a Rectangle
    {
        "id": "m-l1-17",
        "number": 17,
        "title": "Area of a Rectangle",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Measures & Space",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.MSS16",
        "rule_heading": "Area = Length × Width",
        "rule_body": "Area measures the flat 2D space inside a shape. Multiply length by width. Answers are ALWAYS written in square units (cm², m², mm²).",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="20" width="220" height="95" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="2.5"/>
            <text x="110" y="12" font-size="12" font-weight="800" fill="#1e40af" text-anchor="middle">Length = 7 m</text>
            <text x="-15" y="70" font-size="12" font-weight="800" fill="#1e40af" text-anchor="middle">4 m</text>
            <text x="110" y="65" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">Area = 7 m × 4 m</text>
            <text x="110" y="90" font-size="15" font-weight="900" fill="#059669" text-anchor="middle">= 28 m²</text>
          </g>"""),
        "golden_rule": "Area is flat surface (carpet/grass), measured in square units (m²)!",
        "watch_out": "Don't confuse Area (L × W) with Perimeter (L + W + L + W).",
        "challenge_prompt": "A living room floor is 6.5 m long and 4 m wide. How many square metres of carpet are needed to cover it?",
        "answer_text": "Area = 6.5 × 4 = 26 m²."
    },

    # 18. Area of a Triangle
    {
        "id": "m-l1-18",
        "number": 18,
        "title": "Area of a Triangle",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Measures & Space",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.MSS17",
        "rule_heading": "Area = (Base × Height) ÷ 2",
        "rule_body": "1. Multiply base by perpendicular vertical height. 2. HALVE the answer (divide by 2) because a triangle is half of a rectangle.",
        "svg_html": wrap_svg("""
          <g transform="translate(130, 20)">
            <polygon points="10,110 180,110 60,30" fill="#fefce8" stroke="#ca8a04" stroke-width="2.2"/>
            <line x1="60" y1="30" x2="60" y2="110" stroke="#dc2626" stroke-width="2" stroke-dasharray="3,3"/>
            <text x="80" y="70" font-size="11" font-weight="800" fill="#dc2626">h = 6 cm</text>
            <text x="95" y="125" font-size="11" font-weight="800" fill="#a16207" text-anchor="middle">base = 10 cm</text>
            <text x="95" y="145" font-size="12" font-weight="900" fill="#ca8a04" text-anchor="middle">Area = (10 × 6) ÷ 2 = 30 cm²</text>
          </g>"""),
        "golden_rule": "Always remember to divide by 2 for a triangle!",
        "watch_out": "Never use the slanted side length for area — only use vertical perpendicular height.",
        "challenge_prompt": "A triangular banner has a base of 12 cm and a vertical height of 8 cm. What is its area?",
        "answer_text": "Area = (12 × 8) ÷ 2 = 96 ÷ 2 = 48 cm²."
    },

    # 19. Volume of a Simple Cuboid
    {
        "id": "m-l1-19",
        "number": 19,
        "title": "Volume of a Cuboid",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Measures & Space",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.MSS18",
        "rule_heading": "Volume = Length × Width × Height",
        "rule_body": "Volume measures the 3D space inside a solid box. Multiply all three dimensions together: Length × Width × Height. Written in cubic units (cm³, m³).",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <polygon points="10,40 140,40 140,110 10,110" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
            <polygon points="140,40 190,15 190,85 140,110" fill="#93c5fd" stroke="#2563eb" stroke-width="2"/>
            <polygon points="10,40 60,15 190,15 140,40" fill="#bfdbfe" stroke="#2563eb" stroke-width="2"/>
            <text x="75" y="125" font-size="11" font-weight="800" fill="#1e40af" text-anchor="middle">5 cm</text>
            <text x="175" y="105" font-size="11" font-weight="800" fill="#1e40af" text-anchor="middle">2 cm</text>
            <text x="-5" y="75" font-size="11" font-weight="800" fill="#1e40af" text-anchor="middle">3 cm</text>
            <g transform="translate(230, 45)">
              <rect x="0" y="0" width="150" height="60" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>
              <text x="75" y="24" font-size="11" font-weight="700" fill="#0f172a" text-anchor="middle">V = 5 × 2 × 3</text>
              <text x="75" y="46" font-size="13" font-weight="900" fill="#059669" text-anchor="middle">= 30 cm³</text>
            </g>
          </g>"""),
        "golden_rule": "Volume is 3D capacity, measured in cubic units (cm³ or m³)!",
        "watch_out": "Don't add the three dimensions — you must MULTIPLY them.",
        "challenge_prompt": "A packing box is 40 cm long, 25 cm wide, and 20 cm high. What is its volume in cm³?",
        "answer_text": "Volume = 40 × 25 × 20 = 1,000 × 20 = 20,000 cm³."
    },

    # 20. Metric Length Conversions
    {
        "id": "m-l1-20",
        "number": 20,
        "title": "Metric Length Conversions",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Measures & Space",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.MSS19",
        "rule_heading": "mm • cm • m • km",
        "rule_body": "1 cm = 10 mm. 1 m = 100 cm. 1 km = 1,000 m. Big to small unit = MULTIPLY (×). Small to big unit = DIVIDE (÷).",
        "svg_html": wrap_svg("""
          <g transform="translate(30, 20)">
            <rect x="0" y="0" width="400" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="200" y="26" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">METRIC LENGTH STEPS</text>
            <text x="50" y="58" font-size="12" font-weight="700" fill="#2563eb">1 km = 1,000 m  (e.g. 3.2 km = 3,200 m)</text>
            <text x="50" y="83" font-size="12" font-weight="700" fill="#059669">1 m = 100 cm  (e.g. 4.5 m = 450 cm)</text>
            <text x="50" y="108" font-size="12" font-weight="700" fill="#d97706">1 cm = 10 mm  (e.g. 8 cm = 80 mm)</text>
          </g>"""),
        "golden_rule": "Metres to cm: MULTIPLY by 100. cm to metres: DIVIDE by 100.",
        "watch_out": "Don't confuse mm and cm: 45 mm is 4.5 cm, NOT 450 cm.",
        "challenge_prompt": "Convert 275 cm into metres.",
        "answer_text": "275 ÷ 100 = 2.75 metres."
    },

    # 21. Metric Weight/Mass Conversions
    {
        "id": "m-l1-21",
        "number": 21,
        "title": "Metric Weight Conversions",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Measures & Space",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.MSS20",
        "rule_heading": "1 kg = 1,000 g  |  1 tonne = 1,000 kg",
        "rule_body": "To convert kg to g: MULTIPLY by 1,000. To convert g to kg: DIVIDE by 1,000. For medicine: 1 g = 1,000 mg.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
            <text x="170" y="30" font-size="14" font-weight="800" fill="#15803d" text-anchor="middle">MASS: KILOGRAMS &amp; GRAMS</text>
            <text x="170" y="65" font-size="13" font-weight="700" fill="#0f172a" text-anchor="middle">kg → (× 1,000) → grams</text>
            <text x="170" y="90" font-size="13" font-weight="700" fill="#0f172a" text-anchor="middle">grams → (÷ 1,000) → kg</text>
            <text x="170" y="115" font-size="12" font-weight="800" fill="#2563eb" text-anchor="middle">Example: 2.5 kg = 2,500 g</text>
          </g>"""),
        "golden_rule": "'Kilo' always means 1,000!",
        "watch_out": "Half a kilogram is 500 grams, NOT 50 grams.",
        "challenge_prompt": "A postal parcel weighs 1,450 grams. What is its weight in kilograms?",
        "answer_text": "1,450 ÷ 1,000 = 1.45 kg."
    },

    # 22. Metric Capacity Conversions
    {
        "id": "m-l1-22",
        "number": 22,
        "title": "Metric Capacity Conversions",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Measures & Space",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.MSS21",
        "rule_heading": "1 Litre = 1,000 ml",
        "rule_body": "Litres to millilitres: MULTIPLY by 1,000. Millilitres to litres: DIVIDE by 1,000. Common amounts: 1/2 Litre = 500 ml. 1/4 Litre = 250 ml. 3/4 Litre = 750 ml.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="170" y="30" font-size="14" font-weight="800" fill="#1e40af" text-anchor="middle">CAPACITY: LITRES &amp; MILLILITRES</text>
            <text x="170" y="65" font-size="13" font-weight="700" fill="#0f172a" text-anchor="middle">1 L = 1,000 ml</text>
            <text x="170" y="90" font-size="12" font-weight="700" fill="#475569" text-anchor="middle">1/4 L = 250 ml  •  1/2 L = 500 ml  •  3/4 L = 750 ml</text>
            <text x="170" y="115" font-size="12" font-weight="800" fill="#059669" text-anchor="middle">e.g. 1.8 Litres = 1,800 ml</text>
          </g>"""),
        "golden_rule": "Milli means one-thousandth!",
        "watch_out": "Don't divide by 100 — there are 1,000 millilitres in a litre.",
        "challenge_prompt": "A bottle contains 2 Litres of water. 350 ml is poured out. How many ml remain in the bottle?",
        "answer_text": "2 Litres = 2,000 ml. Remaining = 2,000 - 350 = 1,650 ml (or 1.65 L)."
    },

    # 23. Time: 12-Hour & 24-Hour Clock
    {
        "id": "m-l1-23",
        "number": 23,
        "title": "Time: 12-Hour &amp; 24-Hour Clock",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Measures & Space",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.MSS22",
        "rule_heading": "Converting &amp; Timetables",
        "rule_body": "To convert PM time to 24-hour: ADD 12 hours (e.g. 4:15 pm + 12 = 16:15). To convert 24-hour to PM: SUBTRACT 12 hours (e.g. 21:40 - 12 = 9:40 pm).",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="180" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="90" y="26" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">12-HOUR CLOCK</text>
            <text x="90" y="60" font-size="14" font-weight="800" fill="#2563eb" text-anchor="middle">8:30 pm</text>
            <text x="90" y="90" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">Add 12 hours for PM</text>
          </g>
          <g transform="translate(240, 20)">
            <rect x="0" y="0" width="180" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="90" y="26" font-size="12" font-weight="800" fill="#1e40af" text-anchor="middle">24-HOUR CLOCK</text>
            <text x="90" y="60" font-size="14" font-weight="900" fill="#059669" text-anchor="middle">20:30</text>
            <text x="90" y="90" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">Always 4 digits, NO 'pm'</text>
          </g>"""),
        "golden_rule": "Never write 'pm' after a 24-hour time (e.g. 20:30, NOT 20:30 pm)!",
        "watch_out": "12:30 pm is afternoon (lunchtime) = 12:30. 12:30 am is midnight = 00:30.",
        "challenge_prompt": "A train departs at 14:45 and arrives at 16:10. How long was the journey in hours and minutes?",
        "answer_text": "From 14:45 to 15:00 is 15 mins. From 15:00 to 16:10 is 1 hr 10 mins. Total = 1 hour 25 minutes."
    },

    # 24. Money: Calculating Change & Best Buys
    {
        "id": "m-l1-24",
        "number": 24,
        "title": "Money: Change &amp; Best Buys",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Measures & Space",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.MSS23",
        "rule_heading": "Multi-Item Totals &amp; Change",
        "rule_body": "1. Multiply quantities by unit price. 2. Sum all items carefully. 3. Change = Amount paid - Total bill. Compare deals by finding price for the same amount.",
        "svg_html": wrap_svg("""
          <rect x="30" y="20" width="400" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
          <text x="230" y="42" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">Shopping Bill &amp; Change</text>
          <g transform="translate(60, 60)">
            <text x="0" y="20" font-size="11.5" font-weight="700" fill="#475569">3 sandwiches @ £2.50 = £7.50</text>
            <text x="0" y="42" font-size="11.5" font-weight="700" fill="#475569">2 drinks @ £1.25 = £2.50  →  Total = £10.00</text>
            <text x="0" y="65" font-size="12" font-weight="900" fill="#059669">Paid with £20 note → Change = £20 - £10 = £10.00</text>
          </g>"""),
        "golden_rule": "Always write both decimal places for currency: £10.00, NOT £10!",
        "watch_out": "Don't add items without multiplying by quantity first.",
        "challenge_prompt": "You buy 4 notebooks at £1.75 each and a pack of pens for £2.80. You pay with a £10 note. What change do you get?",
        "answer_text": "Notebooks = 4 × £1.75 = £7.00. Total = £7.00 + £2.80 = £9.80. Change = £10.00 - £9.80 = £0.20 (20p)."
    },

    # 25. Properties of 2D Shapes
    {
        "id": "m-l1-25",
        "number": 25,
        "title": "Properties of 2D Shapes",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Measures & Space",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.MSS24",
        "rule_heading": "Sides, Angles &amp; Symmetry",
        "rule_body": "Right Angle = 90°. Triangle angles sum to 180°. Quadrilateral angles sum to 360°. Parallel lines never meet. Perpendicular lines meet at 90°.",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="90" y="24" font-size="12" font-weight="800" fill="#1e40af" text-anchor="middle">TRIANGLES (180°)</text>
            <text x="15" y="55" font-size="10.5" font-weight="700" fill="#0f172a">Equilateral: 3 equal sides</text>
            <text x="15" y="78" font-size="10.5" font-weight="700" fill="#0f172a">Isosceles: 2 equal sides</text>
            <text x="15" y="101" font-size="10.5" font-weight="700" fill="#0f172a">Scalene: 0 equal sides</text>
          </g>
          <g transform="translate(240, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
            <text x="90" y="24" font-size="12" font-weight="800" fill="#15803d" text-anchor="middle">QUADRILATERALS (360°)</text>
            <text x="15" y="55" font-size="10.5" font-weight="700" fill="#0f172a">Square: 4 equal sides, 90°</text>
            <text x="15" y="78" font-size="10.5" font-weight="700" fill="#0f172a">Rectangle: Opposite equal</text>
            <text x="15" y="101" font-size="10.5" font-weight="700" fill="#0f172a">Trapezium: 1 pair parallel</text>
          </g>"""),
        "golden_rule": "All angles in ANY triangle add up to 180°!",
        "watch_out": "A rhombus has 4 equal sides, but its angles are NOT 90° (a square has 90° angles).",
        "challenge_prompt": "Two angles in a triangle are 65° and 45°. What is the size of the third angle?",
        "answer_text": "Sum of known angles = 65° + 45° = 110°. Third angle = 180° - 110° = 70°."
    },

    # 26. Properties of 3D Solids
    {
        "id": "m-l1-26",
        "number": 26,
        "title": "Properties of 3D Solids",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Measures & Space",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.MSS25",
        "rule_heading": "Faces, Edges &amp; Vertices",
        "rule_body": "Face = Flat or curved surface. Edge = Line where two faces meet. Vertex (Vertices) = Corner point where edges meet. A cube/cuboid has 6 faces, 12 edges, 8 vertices.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="170" y="26" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">CUBOID 3D PROPERTIES</text>
            <text x="40" y="55" font-size="12" font-weight="700" fill="#2563eb">Faces = 6 flat rectangular faces</text>
            <text x="40" y="80" font-size="12" font-weight="700" fill="#059669">Edges = 12 straight lines</text>
            <text x="40" y="105" font-size="12" font-weight="700" fill="#d97706">Vertices = 8 corner points</text>
          </g>"""),
        "golden_rule": "Vertices = Corners • Edges = Creases • Faces = Surfaces.",
        "watch_out": "A cylinder has 3 faces (2 flat circles, 1 curved), 2 edges, and 0 vertices!",
        "challenge_prompt": "How many vertices (corners) does a triangular prism have?",
        "answer_text": "A triangular prism has 6 vertices (3 at each triangular end)."
    },

    # 27. Coordinates in First Quadrant
    {
        "id": "m-l1-27",
        "number": 27,
        "title": "Coordinates (x, y)",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Measures & Space",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.MSS26",
        "rule_heading": "Along the Corridor, Up the Stairs",
        "rule_body": "Coordinates are written as (x, y): 1. First number (x) goes HORIZONTALLY along the bottom axis. 2. Second number (y) goes VERTICALLY up the side axis. Origin is (0, 0).",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <line x1="20" y1="120" x2="160" y2="120" stroke="#0f172a" stroke-width="2"/>
            <line x1="20" y1="20" x2="20" y2="120" stroke="#0f172a" stroke-width="2"/>
            <text x="160" y="135" font-size="11" font-weight="800" fill="#0f172a">x</text>
            <text x="10" y="25" font-size="11" font-weight="800" fill="#0f172a">y</text>
            <circle cx="100" cy="50" r="5" fill="#dc2626"/>
            <text x="110" y="45" font-size="12" font-weight="800" fill="#dc2626">(4, 3)</text>
            <g transform="translate(190, 40)">
              <rect x="0" y="0" width="160" height="65" rx="6" fill="#eff6ff" stroke="#3b82f6"/>
              <text x="80" y="24" font-size="11" font-weight="800" fill="#1e40af" text-anchor="middle">Point (4, 3):</text>
              <text x="80" y="46" font-size="10.5" font-weight="700" fill="#475569" text-anchor="middle">4 along (x), 3 up (y)</text>
            </g>
          </g>"""),
        "golden_rule": "'x' comes before 'y' in the alphabet, and in coordinates (x, y)!",
        "watch_out": "Don't mix up (2, 5) with (5, 2) — always read the bottom horizontal axis first.",
        "challenge_prompt": "What are the coordinates of the origin where the two axes cross?",
        "answer_text": "The coordinates of the origin are (0, 0)."
    },

    # 28. Simple Scale Drawings on Grid Paper
    {
        "id": "m-l1-28",
        "number": 28,
        "title": "Scale Drawings on Grid Paper",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Measures & Space",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.MSS27",
        "rule_heading": "Count Squares &amp; Use the Key",
        "rule_body": "Always check the scale key (e.g. 1 square = 1 metre, or 1 square = 2 metres). Real dimension = Number of squares counted × Scale key value.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="10" width="160" height="110" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
            <line x1="40" y1="10" x2="40" y2="120" stroke="#e2e8f0"/>
            <line x1="80" y1="10" x2="80" y2="120" stroke="#e2e8f0"/>
            <line x1="120" y1="10" x2="120" y2="120" stroke="#e2e8f0"/>
            <rect x="0" y="10" width="120" height="80" fill="#bae6fd" stroke="#0284c7" stroke-width="2"/>
            <g transform="translate(190, 35)">
              <rect x="0" y="0" width="170" height="75" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>
              <text x="85" y="24" font-size="11" font-weight="800" fill="#0f172a" text-anchor="middle">Key: 1 sq = 2 metres</text>
              <text x="85" y="46" font-size="10.5" font-weight="700" fill="#475569" text-anchor="middle">Room is 3 sq × 2 sq</text>
              <text x="85" y="65" font-size="11" font-weight="900" fill="#0284c7" text-anchor="middle">Actual: 6 m by 4 m</text>
            </g>
          </g>"""),
        "golden_rule": "Always read the scale key: 1 square is rarely 1 cm in real life!",
        "watch_out": "If 1 square = 2 metres, 4 squares = 8 metres, NOT 4 metres.",
        "challenge_prompt": "On a grid plan where 1 square = 0.5 metres, a desk is drawn 4 squares long. What is the real length of the desk?",
        "answer_text": "Real length = 4 × 0.5 m = 2.0 metres."
    }
]

CARDS_C = [
    # 29. Mean Average (Step-by-Step)
    {
        "id": "m-l1-29",
        "number": 29,
        "title": "Mean Average (Step-by-Step)",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Handling Data",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.HD28",
        "rule_heading": "Add All Up, Divide by Count",
        "rule_body": "1. Add all numbers together to find total sum. 2. Count how many numbers there are. 3. Divide total sum by the count. Mean is the fair share.",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="380" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="190" y="28" font-size="13" font-weight="800" fill="#1e40af" text-anchor="middle">Find Mean of: 6, 8, 12, 14</text>
            <text x="190" y="60" font-size="12" font-weight="700" fill="#475569" text-anchor="middle">Step 1: Total = 6 + 8 + 12 + 14 = 40</text>
            <text x="190" y="85" font-size="12" font-weight="700" fill="#475569" text-anchor="middle">Step 2: There are 4 numbers</text>
            <rect x="110" y="95" width="160" height="25" rx="4" fill="#3b82f6"/>
            <text x="190" y="112" font-size="12" font-weight="900" fill="#ffffff" text-anchor="middle">Step 3: 40 ÷ 4 = 10</text>
          </g>"""),
        "golden_rule": "Divide by how many items you added up!",
        "watch_out": "Don't forget to press equals (=) before dividing on your calculator, or use brackets.",
        "challenge_prompt": "Five friends score 14, 18, 12, 20, and 16 in a quiz. What is their mean score?",
        "answer_text": "Total = 14 + 18 + 12 + 20 + 16 = 80. Count = 5. Mean = 80 ÷ 5 = 16."
    },

    # 30. Median (Ordering Required)
    {
        "id": "m-l1-30",
        "number": 30,
        "title": "Median (Middle Value)",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Handling Data",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.HD29",
        "rule_heading": "Line Up Low to High, Pick Middle",
        "rule_body": "1. Put numbers in numerical order from smallest to largest. 2. Cross off one from each end until you reach the middle number. If two remain in middle, find their midpoint.",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="380" height="130" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
            <text x="190" y="28" font-size="12" font-weight="800" fill="#15803d" text-anchor="middle">Raw Data: 9, 3, 7, 2, 8</text>
            <text x="190" y="60" font-size="13" font-weight="700" fill="#475569" text-anchor="middle">1. Put in order: 2, 3, <tspan font-weight="900" fill="#16a34a">7</tspan>, 8, 9</text>
            <rect x="110" y="78" width="160" height="35" rx="6" fill="#16a34a"/>
            <text x="190" y="100" font-size="14" font-weight="900" fill="#ffffff" text-anchor="middle">Median = 7</text>
          </g>"""),
        "golden_rule": "You MUST sort the numbers from smallest to largest first!",
        "watch_out": "Never pick the middle number of the unsorted list (in 9, 3, 7, 2, 8, '7' happens to be middle, but never rely on luck!).",
        "challenge_prompt": "Find the median of: 15, 6, 21, 9, 12.",
        "answer_text": "Order: 6, 9, 12, 15, 21. Middle value is 12 (Median = 12)."
    },

    # 31. Mode & Modal Value
    {
        "id": "m-l1-31",
        "number": 31,
        "title": "Mode (Most Frequent)",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Handling Data",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.HD30",
        "rule_heading": "The Most Common Item",
        "rule_body": "Mode is the number or category that appears MOST OFTEN in the data. There can be one mode, more than one mode (bimodal), or no mode if all values appear once.",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="380" height="130" rx="8" fill="#fdf2f8" stroke="#ec4899" stroke-width="1.8"/>
            <text x="190" y="28" font-size="13" font-weight="800" fill="#9d174d" text-anchor="middle">Shoe Sizes: 5, 6, 6, 7, 6, 8, 5</text>
            <text x="190" y="60" font-size="12" font-weight="700" fill="#475569" text-anchor="middle">Size 5 appears 2 times • Size 6 appears 3 times</text>
            <rect x="110" y="78" width="160" height="35" rx="6" fill="#db2777"/>
            <text x="190" y="100" font-size="14" font-weight="900" fill="#ffffff" text-anchor="middle">Mode = Size 6 ★</text>
          </g>"""),
        "golden_rule": "'MO'de = 'MO'st often!",
        "watch_out": "The mode can be words (e.g. Blue, Coffee) — it is the only average that works for non-numbers.",
        "challenge_prompt": "What is the modal value of this dataset: 4, 7, 2, 7, 5, 9, 7, 2?",
        "answer_text": "7 appears three times (more than any other number). Mode = 7."
    },

    # 32. Range (Measure of Spread)
    {
        "id": "m-l1-32",
        "number": 32,
        "title": "Range (Spread of Data)",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Handling Data",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.HD31",
        "rule_heading": "Range = Highest - Lowest",
        "rule_body": "Range is NOT an average — it measures how spread out the numbers are. Subtract the smallest number from the largest number. Smaller range = more consistent.",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="380" height="130" rx="8" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.8"/>
            <text x="190" y="28" font-size="13" font-weight="800" fill="#b45309" text-anchor="middle">Temperatures: 12°C, 25°C, 18°C, 14°C</text>
            <text x="190" y="60" font-size="12" font-weight="700" fill="#475569" text-anchor="middle">Highest = 25°C   •   Lowest = 12°C</text>
            <rect x="100" y="78" width="180" height="35" rx="6" fill="#f59e0b"/>
            <text x="190" y="100" font-size="14" font-weight="900" fill="#ffffff" text-anchor="middle">Range = 25 - 12 = 13°C</text>
          </g>"""),
        "golden_rule": "Range = Highest minus Lowest!",
        "watch_out": "Don't write '12 to 25' — the range is a SINGLE number obtained by subtracting (13).",
        "challenge_prompt": "Weekly sales figures are: £180, £240, £150, £310, £220. Calculate the range.",
        "answer_text": "Highest = £310. Lowest = £150. Range = £310 - £150 = £160."
    },

    # 33. Tally Charts & Frequency Tables
    {
        "id": "m-l1-33",
        "number": 33,
        "title": "Tally Charts &amp; Frequency",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Handling Data",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.HD32",
        "rule_heading": "Bundles of 5",
        "rule_body": "Tallies are grouped in bundles of five: Four vertical marks and the fifth mark crossing diagonally through the bundle (卌). Frequency is the total count as a number.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">TALLY SYSTEM</text>
            <text x="60" y="60" font-size="12" font-weight="700" fill="#475569">Item: Car</text>
            <text x="170" y="60" font-size="13" font-weight="900" fill="#2563eb">卌 |||</text>
            <text x="270" y="60" font-size="13" font-weight="900" fill="#059669">Freq: 8</text>
            <text x="170" y="105" font-size="11" font-weight="700" fill="#64748b" text-anchor="middle">Count tallies in 5s: 5 + 3 = 8</text>
          </g>"""),
        "golden_rule": "The 5th tally stroke always gates across the bundle of 4!",
        "watch_out": "Check your raw data twice by crossing off each item as you record its tally mark.",
        "challenge_prompt": "What frequency number does '卌 卌 卌 ||' represent?",
        "answer_text": "Three bundles of 5 plus 2: (3 × 5) + 2 = 15 + 2 = 17."
    },

    # 34. Bar Charts: Drawing & Reading Scales
    {
        "id": "m-l1-34",
        "number": 34,
        "title": "Bar Charts &amp; Scales",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Handling Data",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.HD33",
        "rule_heading": "Equal Widths, Equal Gaps, Labelled Axes",
        "rule_body": "To draw a bar chart for full marks: 1. Evenly spaced linear scale on vertical axis starting at 0. 2. Label both axes (e.g. 'Days' and 'Frequency'). 3. Equal width bars with equal gaps between them.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <line x1="20" y1="110" x2="300" y2="110" stroke="#334155" stroke-width="2"/>
            <line x1="20" y1="20" x2="20" y2="110" stroke="#334155" stroke-width="2"/>
            <rect x="50" y="40" width="40" height="70" fill="#3b82f6"/>
            <rect x="130" y="60" width="40" height="50" fill="#3b82f6"/>
            <rect x="210" y="25" width="40" height="85" fill="#3b82f6"/>
            <text x="70" y="125" font-size="10" font-weight="700" fill="#0f172a" text-anchor="middle">Tea</text>
            <text x="150" y="125" font-size="10" font-weight="700" fill="#0f172a" text-anchor="middle">Coffee</text>
            <text x="230" y="125" font-size="10" font-weight="700" fill="#0f172a" text-anchor="middle">Water</text>
          </g>"""),
        "golden_rule": "Bars must NOT touch each other in a categorical bar chart!",
        "watch_out": "Check what 1 grid square represents on the vertical axis (e.g. 1 square might be 2 or 5 units).",
        "challenge_prompt": "State two things every bar chart must have to receive full marks in an exam.",
        "answer_text": "1. Equal bar widths with equal gaps. 2. Labelled axes with an evenly-spaced linear number scale starting at zero."
    },

    # 35. Pictograms (Using a Key)
    {
        "id": "m-l1-35",
        "number": 35,
        "title": "Pictograms (Using a Key)",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Handling Data",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.HD34",
        "rule_heading": "Always Check the Symbol Key",
        "rule_body": "A pictogram uses pictures or symbols to represent quantities. Look at the key: 1 whole symbol = n items. A half symbol = n ÷ 2. A quarter symbol = n ÷ 4.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">KEY: [★] = 4 BOOKS</text>
            <text x="40" y="60" font-size="12" font-weight="700" fill="#475569">Monday: [★] [★] = 2 × 4 = 8 books</text>
            <text x="40" y="90" font-size="12" font-weight="700" fill="#475569">Tuesday: [★] [★] [half] = 4 + 4 + 2 = 10 books</text>
          </g>"""),
        "golden_rule": "Always check the KEY first — one picture is rarely just 1 item!",
        "watch_out": "Don't count the number of symbols without multiplying by the key value.",
        "challenge_prompt": "On a pictogram, a circle represents 8 cars. How many circles should you draw to represent 28 cars?",
        "answer_text": "28 ÷ 8 = 3.5. Draw 3 whole circles and 1 half circle."
    },

    # 36. Line Graphs (Trends over Time)
    {
        "id": "m-l1-36",
        "number": 36,
        "title": "Line Graphs (Trends over Time)",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Handling Data",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.HD35",
        "rule_heading": "Plot Points &amp; Join with Straight Lines",
        "rule_body": "Line graphs show how continuous data changes over time (temperature, sales, patient heart rate). Time is plotted along the horizontal axis. Read points by looking across to vertical axis.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <line x1="20" y1="110" x2="300" y2="110" stroke="#334155" stroke-width="2"/>
            <line x1="20" y1="20" x2="20" y2="110" stroke="#334155" stroke-width="2"/>
            <polyline points="40,90 100,70 160,80 220,40 280,30" fill="none" stroke="#2563eb" stroke-width="2.5"/>
            <circle cx="40" cy="90" r="4" fill="#2563eb"/><circle cx="100" cy="70" r="4" fill="#2563eb"/><circle cx="160" cy="80" r="4" fill="#2563eb"/><circle cx="220" cy="40" r="4" fill="#2563eb"/><circle cx="280" cy="30" r="4" fill="#2563eb"/>
            <text x="160" y="130" font-size="10" font-weight="700" fill="#0f172a" text-anchor="middle">Months (Jan to May) → Overall Upward Trend</text>
          </g>"""),
        "golden_rule": "Time always goes along the bottom horizontal axis!",
        "watch_out": "Join the plotted data points with neat straight ruler lines from point to point.",
        "challenge_prompt": "Between 9 am (14°C) and 1 pm (22°C), what was the rise in temperature?",
        "answer_text": "Rise = 22°C - 14°C = 8°C."
    },

    # 37. Probability Scale (0 to 1)
    {
        "id": "m-l1-37",
        "number": 37,
        "title": "Probability Words &amp; Scale",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Handling Data",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.HD36",
        "rule_heading": "Impossible to Certain",
        "rule_body": "0 = Impossible (can never happen). 0.5 (1/2 or 50%) = Even Chance (e.g. flipping heads). 1 = Certain (guaranteed to happen). Unlikely is between 0 and 0.5; Likely is between 0.5 and 1.",
        "svg_html": wrap_svg("""
          <line x1="30" y1="85" x2="430" y2="85" stroke="#334155" stroke-width="2.5"/>
          <circle cx="30" cy="85" r="5" fill="#dc2626"/>
          <text x="30" y="115" font-size="11" font-weight="800" fill="#dc2626" text-anchor="middle">0 (Impossible)</text>
          <circle cx="130" cy="85" r="4" fill="#f59e0b"/>
          <text x="130" y="115" font-size="10" font-weight="700" fill="#b45309" text-anchor="middle">Unlikely</text>
          <circle cx="230" cy="85" r="5" fill="#2563eb"/>
          <text x="230" y="115" font-size="11" font-weight="800" fill="#1e40af" text-anchor="middle">0.5 (Evens)</text>
          <circle cx="330" cy="85" r="4" fill="#059669"/>
          <text x="330" y="115" font-size="10" font-weight="700" fill="#047857" text-anchor="middle">Likely</text>
          <circle cx="430" cy="85" r="5" fill="#16a34a"/>
          <text x="430" y="115" font-size="11" font-weight="800" fill="#15803d" text-anchor="middle">1 (Certain)</text>"""),
        "golden_rule": "Probabilities on a number scale run strictly from 0 to 1!",
        "watch_out": "Don't use words like 'Good chance' or 'Fifty-fifty' on an exam — use 'Likely' or 'Even chance'.",
        "challenge_prompt": "Match the word to the event: (a) Tomorrow will be Wednesday if today is Tuesday. (b) Rolling an 8 on a standard 6-sided die.",
        "answer_text": "(a) Certain. (b) Impossible."
    },

    # 38. Comparing Two Data Sets at Level 1
    {
        "id": "m-l1-38",
        "number": 38,
        "title": "Comparing Two Data Sets (L1)",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Handling Data",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.HD37",
        "rule_heading": "Compare One Average &amp; One Range",
        "rule_body": "To compare two groups for 2 marks: 1. State which group has a higher/lower mean or median. 2. State which group is more consistent by comparing their range (smaller range = more consistent).",
        "svg_html": wrap_svg("""
          <rect x="30" y="20" width="400" height="130" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
          <text x="230" y="42" font-size="13" font-weight="900" fill="#15803d" text-anchor="middle">LEVEL 1 EXAM COMPARISON TEMPLATE</text>
          <g transform="translate(60, 60)">
            <text x="0" y="22" font-size="11.5" font-weight="700" fill="#0f172a">1. "Team A scored higher on average (Mean 18 vs 14)."</text>
            <text x="0" y="50" font-size="11.5" font-weight="700" fill="#0f172a">2. "Team B was more consistent because its range is smaller (4 vs 10)."</text>
          </g>"""),
        "golden_rule": "Always include the actual values and mention which group was more consistent!",
        "watch_out": "A bigger range does NOT mean better — it means more variable / less consistent.",
        "challenge_prompt": "Group 1: Mean = 24 kg, Range = 6 kg. Group 2: Mean = 20 kg, Range = 2 kg. Which group was more consistent in weight?",
        "answer_text": "Group 2 was more consistent because its range was smaller (2 kg compared to 6 kg)."
    }
]

def main():
    import os
    base_dir = "/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk/decks/maths_l1"
    os.makedirs(base_dir, exist_ok=True)

    with open(os.path.join(base_dir, "strand_a.py"), "w") as f:
        f.write('\"\"\"Maths L1 Strand A: Number and the Number System (Cards 1-14)\"\"\"\n')
        f.write('CARDS = ' + pprint.pformat(CARDS_A, indent=2, width=120) + '\n')

    with open(os.path.join(base_dir, "strand_b.py"), "w") as f:
        f.write('\"\"\"Maths L1 Strand B: Measures, Shape and Space (Cards 15-28)\"\"\"\n')
        f.write('CARDS = ' + pprint.pformat(CARDS_B, indent=2, width=120) + '\n')

    with open(os.path.join(base_dir, "strand_c.py"), "w") as f:
        f.write('\"\"\"Maths L1 Strand C: Handling Information and Data (Cards 29-38)\"\"\"\n')
        f.write('CARDS = ' + pprint.pformat(CARDS_C, indent=2, width=120) + '\n')

    with open(os.path.join(base_dir, "__init__.py"), "w") as f:
        f.write('from .strand_a import CARDS as STRAND_A\n')
        f.write('from .strand_b import CARDS as STRAND_B\n')
        f.write('from .strand_c import CARDS as STRAND_C\n\n')
        f.write('CARDS = STRAND_A + STRAND_B + STRAND_C\n')

    print(f"✓ Maths Level 1 Complete: {len(CARDS_A) + len(CARDS_B) + len(CARDS_C)} cards generated!")

if __name__ == "__main__":
    main()
