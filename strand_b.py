"""Strand B: Measures, Shape and Space (Cards 19-36)"""
CARDS = [ { 'answer_text': 'Missing horizontal = 12 - 5 = 7 m. Missing vertical = 8 - 3 = 5 m. Perimeter = 12 + 8 + 7 + 3 + 5 '
                   '+ 5 = 40 m.',
    'challenge_prompt': 'An L-shaped lawn has outer dimensions 12 m by 8 m, with an inset cut of 5 m wide and 3 m '
                        'deep. What is the perimeter?',
    'dfe_code': 'DfE L2.MSS18',
    'golden_rule': 'Tick off each side as you add it to avoid counting sides twice or skipping one!',
    'id': 'm-l2-19',
    'level': 'l2',
    'level_label': 'Level 2',
    'number': 19,
    'rule_body': '1. Find every missing side: Horizontal missing side = Total width - given width. Vertical missing '
                 'side = Total height - given height. 2. Sum ALL outer sides.',
    'rule_heading': 'Find Missing Sides, Then Add All',
    'strand_name': 'Shape & Space',
    'strand_theme': 'emerald',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <polygon points="50,30 250,30 250,80 170,80 170,140 50,140" fill="#ecfdf5" stroke="#059669" '
                'stroke-width="2.5"/>\n'
                '          <text x="150" y="22" font-size="12" font-weight="800" fill="#065f46" '
                'text-anchor="middle">10 m</text>\n'
                '          <text x="265" y="60" font-size="12" font-weight="800" fill="#065f46" text-anchor="middle">4 '
                'm</text>\n'
                '          <text x="210" y="74" font-size="11" font-weight="800" fill="#dc2626" text-anchor="middle">? '
                '= 4 m</text>\n'
                '          <text x="185" y="115" font-size="11" font-weight="800" fill="#dc2626" '
                'text-anchor="middle">? = 5 m</text>\n'
                '          <text x="110" y="155" font-size="12" font-weight="800" fill="#065f46" '
                'text-anchor="middle">6 m</text>\n'
                '          <text x="35" y="90" font-size="12" font-weight="800" fill="#065f46" text-anchor="middle">9 '
                'm</text>\n'
                '          <g transform="translate(290, 45)">\n'
                '            <rect x="0" y="0" width="150" height="75" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>\n'
                '            <text x="75" y="24" font-size="11" font-weight="800" fill="#0f172a" '
                'text-anchor="middle">Missing Sides:</text>\n'
                '            <text x="75" y="44" font-size="10" font-weight="700" fill="#dc2626" '
                'text-anchor="middle">Width = 10 - 6 = 4 m</text>\n'
                '            <text x="75" y="62" font-size="10" font-weight="700" fill="#dc2626" '
                'text-anchor="middle">Height = 9 - 4 = 5 m</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Perimeter of Composite Shapes',
    'watch_out': 'Never add internal dotted lines when finding perimeter — perimeter is ONLY the outside border!'},
  { 'answer_text': 'Diameter = 35 × 2 = 70 cm. Circumference = 3.142 × 70 = 219.94 cm (or 2.20 m).',
    'challenge_prompt': 'A circular bicycle wheel has a radius of 35 cm. How far does the bicycle travel in 1 full '
                        'rotation of the wheel? (Use π = 3.142)',
    'dfe_code': 'DfE L2.MSS19',
    'golden_rule': 'Distance around outside: Circumference = 3.142 × Diameter!',
    'id': 'm-l2-20',
    'level': 'l2',
    'level_label': 'Level 2',
    'number': 20,
    'rule_body': 'Circumference is the distance around the outside edge of a circle. Diameter (d) goes straight across '
                 'through center. Radius (r) is from center to edge (d = 2r).',
    'rule_heading': 'Circumference = 3.142 × Diameter',
    'strand_name': 'Shape & Space',
    'strand_theme': 'emerald',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <circle cx="150" cy="85" r="55" fill="#f0fdf4" stroke="#16a34a" stroke-width="2.5"/>\n'
                '          <line x1="95" y1="85" x2="205" y2="85" stroke="#16a34a" stroke-width="2" '
                'stroke-dasharray="3,3"/>\n'
                '          <circle cx="150" cy="85" r="3.5" fill="#16a34a"/>\n'
                '          <text x="150" y="78" font-size="11" font-weight="800" fill="#15803d" text-anchor="middle">d '
                '= 14 cm</text>\n'
                '          <g transform="translate(225, 30)">\n'
                '            <rect x="0" y="0" width="215" height="110" rx="8" fill="#eff6ff" stroke="#3b82f6" '
                'stroke-width="1.8"/>\n'
                '            <text x="107" y="28" font-size="12" font-weight="800" fill="#1e40af" '
                'text-anchor="middle">CIRCUMFERENCE</text>\n'
                '            <text x="107" y="55" font-size="11" font-weight="700" fill="#0f172a" '
                'text-anchor="middle">C = 3.142 × Diameter</text>\n'
                '            <text x="107" y="78" font-size="11" font-weight="700" fill="#475569" '
                'text-anchor="middle">C = 3.142 × 14</text>\n'
                '            <text x="107" y="100" font-size="13" font-weight="800" fill="#059669" '
                'text-anchor="middle">= 43.99 cm</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Circumference of a Circle',
    'watch_out': 'If given radius (r), you MUST double it before multiplying by 3.142 (Diameter = 2 × r)!'},
  { 'answer_text': 'Discard sloping side 5.5 m. Area = 1/2 × base × height = 0.5 × 8.4 × 3.5 = 14.7 m².',
    'challenge_prompt': 'A triangular roof truss has a base of 8.4 m, perpendicular height of 3.5 m, and sloping sides '
                        'of 5.5 m. Find its area.',
    'dfe_code': 'DfE L2.MSS20',
    'golden_rule': 'Always use the perpendicular vertical height, NEVER the slanted side!',
    'id': 'm-l2-21',
    'level': 'l2',
    'level_label': 'Level 2',
    'number': 21,
    'rule_body': 'Both use PERPENDICULAR vertical height at 90° to the base. Triangle is halved because two identical '
                 'triangles make a parallelogram/rectangle.',
    'rule_heading': 'Triangle: 1/2 × b × h  |  Parallelogram: b × h',
    'strand_name': 'Shape & Space',
    'strand_theme': 'emerald',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(30, 25)">\n'
                '            <polygon points="10,110 150,110 60,30" fill="#eff6ff" stroke="#2563eb" '
                'stroke-width="2.2"/>\n'
                '            <line x1="60" y1="30" x2="60" y2="110" stroke="#dc2626" stroke-width="2" '
                'stroke-dasharray="3,3"/>\n'
                '            <text x="80" y="75" font-size="11" font-weight="800" fill="#dc2626">h</text>\n'
                '            <text x="80" y="125" font-size="11" font-weight="800" fill="#1e40af" '
                'text-anchor="middle">base (b)</text>\n'
                '            <text x="80" y="145" font-size="11" font-weight="800" fill="#2563eb" '
                'text-anchor="middle">Area = (b × h) ÷ 2</text>\n'
                '          </g>\n'
                '          <g transform="translate(230, 25)">\n'
                '            <polygon points="40,30 180,30 150,110 10,110" fill="#fefce8" stroke="#ca8a04" '
                'stroke-width="2.2"/>\n'
                '            <line x1="40" y1="30" x2="40" y2="110" stroke="#dc2626" stroke-width="2" '
                'stroke-dasharray="3,3"/>\n'
                '            <text x="50" y="75" font-size="11" font-weight="800" fill="#dc2626">h</text>\n'
                '            <text x="80" y="125" font-size="11" font-weight="800" fill="#a16207" '
                'text-anchor="middle">base (b)</text>\n'
                '            <text x="95" y="145" font-size="11" font-weight="800" fill="#ca8a04" '
                'text-anchor="middle">Area = b × h (NO ÷ 2!)</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Area of Triangle &amp; Parallelogram',
    'watch_out': "Don't divide by 2 for a parallelogram — only halve for a triangle!"},
  { 'answer_text': 'Ignore slant 5.2 m! Area = ((7 + 11) ÷ 2) × 4.5 = 9 × 4.5 = 40.5 m².',
    'challenge_prompt': 'A pedestrian walkway has parallel edges of 7 m and 11 m, vertical width of 4.5 m, and slant '
                        'edge of 5.2 m. Calculate its area.',
    'dfe_code': 'DfE L2.MSS20',
    'golden_rule': 'Half the sum of parallel sides times vertical height!',
    'id': 'm-l2-22',
    'level': 'l2',
    'level_label': 'Level 2',
    'number': 22,
    'rule_body': '1. Add parallel top and bottom sides (a + b). 2. Divide by 2 to get average parallel width. 3. '
                 'Multiply by perpendicular vertical height (h).',
    'rule_heading': 'Area = 1/2(a + b)h',
    'strand_name': 'Shape & Space',
    'strand_theme': 'emerald',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <polygon points="120,40 280,40 360,135 60,135" fill="#fef3c7" stroke="#d97706" '
                'stroke-width="2.5"/>\n'
                '          <line x1="120" y1="40" x2="120" y2="135" stroke="#059669" stroke-width="2.2" '
                'stroke-dasharray="4,4"/>\n'
                '          <rect x="130" y="80" width="50" height="20" rx="4" fill="#ffffff" stroke="#059669"/>\n'
                '          <text x="155" y="94" font-size="11" font-weight="800" fill="#059669" text-anchor="middle">h '
                '= 4 m</text>\n'
                '          <text x="200" y="32" font-size="12" font-weight="800" fill="#2563eb" text-anchor="middle">a '
                '= 6 m</text>\n'
                '          <text x="210" y="152" font-size="12" font-weight="800" fill="#2563eb" '
                'text-anchor="middle">b = 10 m</text>\n'
                '          <rect x="330" y="55" width="85" height="22" rx="4" fill="#ffe4e6" stroke="#f43f5e"/>\n'
                '          <text x="372" y="70" font-size="10" font-weight="800" fill="#be123c" '
                'text-anchor="middle">IGNORE SLANT!</text>\n'
                '</svg>',
    'title': 'Area of a Trapezium',
    'watch_out': 'Examiners include slanted side lengths as a trap. Cross out the slant immediately.'},
  { 'answer_text': 'Radius = 8 ÷ 2 = 4 m. Full circle = 3.142 × 4² = 3.142 × 4 × 4 = 50.272 m². Semicircle = 50.272 ÷ '
                   '2 = 25.14 m².',
    'challenge_prompt': 'A semicircular patio has a straight diameter of 8 metres. Calculate the area of the patio. '
                        '(Use π = 3.142)',
    'dfe_code': 'DfE L2.MSS21',
    'golden_rule': 'Circle Area = 3.142 × r² (where r² means Radius × Radius)!',
    'id': 'm-l2-23',
    'level': 'l2',
    'level_label': 'Level 2',
    'number': 23,
    'rule_body': 'The ² symbol means squared: r² means radius multiplied by itself (r × r). Calculate r² (r × r) '
                 'first, then multiply by 3.142 (Area = 3.142 × r²). If given diameter, halve it first to get radius. '
                 'Semicircle area is half the full circle: (3.142 × r²) ÷ 2.',
    'rule_heading': 'Circle: π r² = 3.142 × r²  |  Semicircle: (3.142 × r²) ÷ 2',
    'strand_name': 'Shape & Space',
    'strand_theme': 'emerald',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <circle cx="120" cy="85" r="50" fill="#eff6ff" stroke="#2563eb" stroke-width="2.5"/>\n'
                '          <line x1="120" y1="85" x2="170" y2="85" stroke="#2563eb" stroke-width="2.5"/>\n'
                '          <circle cx="120" cy="85" r="3.5" fill="#2563eb"/>\n'
                '          <text x="145" y="78" font-size="11" font-weight="800" fill="#1e40af">r = 5 cm</text>\n'
                '          <text x="120" y="152" font-size="11" font-weight="800" fill="#1e3a8a" '
                'text-anchor="middle">A = π r² = 3.142 × 5² = 3.142 × 5 × 5 = 78.55 cm²</text>\n'
                '          <g transform="translate(240, 35)">\n'
                '            <path d="M 10,80 A 60,60 0 0,1 130,80 Z" fill="#fdf2f8" stroke="#db2777" '
                'stroke-width="2.5"/>\n'
                '            <text x="70" y="100" font-size="10.5" font-weight="800" fill="#be185d" '
                'text-anchor="middle">Semicircle Area = (π r²) ÷ 2</text>\n'
                '            <text x="70" y="118" font-size="10" font-weight="700" fill="#64748b" '
                'text-anchor="middle">(r² means r × r = 5 × 5)</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Area of a Circle &amp; Semicircle',
    'watch_out': 'Do NOT multiply diameter by itself! Always halve diameter first to find radius.'},
  { 'answer_text': 'Rectangle = 15 × 10 = 150 m². Semicircle radius = 3 m. Semicircle area = (3.14 × 3²) ÷ 2 = 14.13 '
                   'm². Total area = 150 + 14.13 = 164.13 m².',
    'challenge_prompt': 'A warehouse floor is a 15 m by 10 m rectangle with a semicircular loading bay of diameter 6 m '
                        'extending outwards on one side. What is the total area? (π = 3.14)',
    'dfe_code': 'DfE L2.MSS22',
    'golden_rule': "Draw clear dotted split lines and label areas 'A' and 'B'!",
    'id': 'm-l2-24',
    'level': 'l2',
    'level_label': 'Level 2',
    'number': 24,
    'rule_body': '1. Split compound floor plan into non-overlapping rectangles and triangles with dashed lines. 2. '
                 'Calculate area of each individual section. 3. Sum all areas.',
    'rule_heading': 'Split into Simpler Shapes, Then Add',
    'strand_name': 'Shape & Space',
    'strand_theme': 'emerald',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <polygon points="50,40 220,40 220,130 50,130" fill="#eff6ff" stroke="#2563eb" '
                'stroke-width="2"/>\n'
                '          <polygon points="220,40 330,85 220,130" fill="#fefce8" stroke="#ca8a04" stroke-width="2"/>\n'
                '          <line x1="220" y1="40" x2="220" y2="130" stroke="#475569" stroke-width="2" '
                'stroke-dasharray="4,4"/>\n'
                '          <text x="135" y="88" font-size="13" font-weight="800" fill="#1e40af" '
                'text-anchor="middle">Shape A: 60 m²</text>\n'
                '          <text x="260" y="88" font-size="12" font-weight="800" fill="#a16207" '
                'text-anchor="middle">Shape B: 25 m²</text>\n'
                '          <g transform="translate(140, 142)">\n'
                '            <text x="80" y="15" font-size="13" font-weight="900" fill="#059669" '
                'text-anchor="middle">Total Area = 60 + 25 = 85 m²</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Area of Composite Shapes',
    'watch_out': 'Check if a section is CUT OUT (e.g. pond in a lawn). If cut out, SUBTRACT its area.'},
  { 'answer_text': 'Triangle area = 1/2 × 6 × 4 = 12 cm². Volume = Cross-section × Length = 12 × 15 = 180 cm³.',
    'challenge_prompt': 'A triangular prism has a cross-section triangle with base 6 cm and height 4 cm. Its length is '
                        '15 cm. What is its volume?',
    'dfe_code': 'DfE L2.MSS23',
    'golden_rule': 'Always multiply the front face area by the full length/depth!',
    'id': 'm-l2-25',
    'level': 'l2',
    'level_label': 'Level 2',
    'number': 25,
    'rule_body': 'A prism has the same 2D shape all the way through: 1. Find area of the front face (cross-section). '
                 '2. Multiply by the 3D length/depth. Units are cubic (cm³, m³).',
    'rule_heading': 'Volume = Cross-Sectional Area × Length',
    'strand_name': 'Shape & Space',
    'strand_theme': 'emerald',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(40, 20)">\n'
                '            <polygon points="10,40 100,40 100,110 10,110" fill="#dbeafe" stroke="#2563eb" '
                'stroke-width="2"/>\n'
                '            <polygon points="100,40 150,15 150,85 100,110" fill="#93c5fd" stroke="#2563eb" '
                'stroke-width="2"/>\n'
                '            <polygon points="10,40 60,15 150,15 100,40" fill="#bfdbfe" stroke="#2563eb" '
                'stroke-width="2"/>\n'
                '            <text x="55" y="80" font-size="11" font-weight="800" fill="#1e40af" '
                'text-anchor="middle">L × W × H</text>\n'
                '            <text x="80" y="130" font-size="11" font-weight="800" fill="#1e3a8a" '
                'text-anchor="middle">Cuboid</text>\n'
                '          </g>\n'
                '          <g transform="translate(240, 20)">\n'
                '            <polygon points="10,110 80,110 45,30" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>\n'
                '            <polygon points="80,110 150,75 115,10 45,30" fill="#fde68a" stroke="#d97706" '
                'stroke-width="2"/>\n'
                '            <text x="45" y="85" font-size="10" font-weight="800" fill="#b45309" '
                'text-anchor="middle">Triangle</text>\n'
                '            <text x="80" y="130" font-size="11" font-weight="800" fill="#b45309" '
                'text-anchor="middle">Triangular Prism: Area × Length</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Volume of Cuboids &amp; Prisms',
    'watch_out': "Don't confuse Volume (3D space in m³) with Surface Area (2D skin in m²)."},
  { 'answer_text': 'Radius = 60 ÷ 2 = 30 cm. Volume = 3.14 × 30² × 120 = 3.14 × (30 × 30) × 120 = 3.14 × 900 × 120 = '
                   '339,120 cm³. Litres = 339,120 ÷ 1,000 = 339.12 L.',
    'challenge_prompt': 'A hot water tank is a cylinder with diameter 60 cm and height 120 cm. Calculate its capacity '
                        'in litres (π = 3.14).',
    'dfe_code': 'DfE L2.MSS24',
    'golden_rule': 'Cylinder Volume = 3.142 × r² × h (where r² means Radius × Radius)!',
    'id': 'm-l2-26',
    'level': 'l2',
    'level_label': 'Level 2',
    'number': 26,
    'rule_body': 'A cylinder is a circular prism: 1. Circular base area = π r² = 3.142 × r² (where r² means r × r). 2. '
                 'Multiply by vertical height (h): Volume = 3.142 × r² × h. Units are cubic (cm³, m³), where ³ means '
                 'cubed (x × x × x). 1,000 cm³ = 1 Litre.',
    'rule_heading': 'Volume = π r² h = 3.142 × r² × h',
    'strand_name': 'Shape & Space',
    'strand_theme': 'emerald',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(60, 20)">\n'
                '            <ellipse cx="60" cy="30" rx="55" ry="18" fill="#e0f2fe" stroke="#0284c7" '
                'stroke-width="2"/>\n'
                '            <rect x="5" y="30" width="110" height="75" fill="#f0f9ff"/>\n'
                '            <line x1="5" y1="30" x2="5" y2="105" stroke="#0284c7" stroke-width="2"/>\n'
                '            <line x1="115" y1="30" x2="115" y2="105" stroke="#0284c7" stroke-width="2"/>\n'
                '            <ellipse cx="60" cy="105" rx="55" ry="18" fill="#bae6fd" stroke="#0284c7" '
                'stroke-width="2"/>\n'
                '            <line x1="60" y1="30" x2="115" y2="30" stroke="#0369a1" stroke-width="2"/>\n'
                '            <text x="85" y="24" font-size="10" font-weight="800" fill="#0369a1">r</text>\n'
                '            <text x="130" y="70" font-size="11" font-weight="800" fill="#0369a1">h</text>\n'
                '          </g>\n'
                '          <g transform="translate(210, 30)">\n'
                '            <rect x="0" y="0" width="220" height="105" rx="8" fill="#eff6ff" stroke="#3b82f6" '
                'stroke-width="1.8"/>\n'
                '            <text x="110" y="24" font-size="12" font-weight="900" fill="#1e40af" '
                'text-anchor="middle">CYLINDER FORMULA</text>\n'
                '            <text x="110" y="48" font-size="11.5" font-weight="800" fill="#0f172a" '
                'text-anchor="middle">V = π r² h = 3.142 × r² × h</text>\n'
                '            <text x="110" y="68" font-size="10" font-weight="700" fill="#2563eb" '
                'text-anchor="middle">(r² means radius × radius)</text>\n'
                '            <text x="110" y="90" font-size="11" font-weight="700" fill="#059669" '
                'text-anchor="middle">1,000 cm³ = 1 Litre</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Volume of a Cylinder',
    'watch_out': 'If given diameter, divide by 2 first to get radius! (r = d ÷ 2).'},
  { 'answer_text': 'Open top = 1 bottom + 2 front/backs + 2 sides. Bottom = 2 × 1.5 = 3 m². Front/Back = 2 × (2 × 1) = '
                   '4 m². Ends = 2 × (1.5 × 1) = 3 m². Total SA = 3 + 4 + 3 = 10 m².',
    'challenge_prompt': 'A storage crate with an open top (no lid) is 2 m long, 1.5 m wide, and 1 m high. What is its '
                        'outside surface area?',
    'dfe_code': 'DfE L2.MSS25',
    'golden_rule': 'Calculate 3 faces, add them up, then multiply by 2!',
    'id': 'm-l2-27',
    'level': 'l2',
    'level_label': 'Level 2',
    'number': 27,
    'rule_body': 'A cuboid has 6 rectangular faces in 3 identical opposite pairs: 1. Front &amp; Back (l × h) × 2. 2. '
                 'Top &amp; Bottom (l × w) × 2. 3. Left &amp; Right (w × h) × 2. Sum all 6 faces.',
    'rule_heading': 'SA = 2(lw + lh + wh)',
    'strand_name': 'Shape & Space',
    'strand_theme': 'emerald',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <rect x="30" y="20" width="400" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" '
                'stroke-width="1.8"/>\n'
                '          <text x="230" y="42" font-size="13" font-weight="800" fill="#0f172a" '
                'text-anchor="middle">Box dimensions: 5 m long, 4 m wide, 3 m high</text>\n'
                '          <g transform="translate(60, 60)">\n'
                '            <rect x="0" y="0" width="95" height="40" rx="4" fill="#dbeafe"/><text x="47" y="24" '
                'font-size="10" font-weight="800" fill="#1e40af" text-anchor="middle">Top/Bot: 2×(5×4)=40</text>\n'
                '            <rect x="110" y="0" width="105" height="40" rx="4" fill="#dcfce7"/><text x="162" y="24" '
                'font-size="10" font-weight="800" fill="#15803d" text-anchor="middle">Front/Back: 2×(5×3)=30</text>\n'
                '            <rect x="230" y="0" width="95" height="40" rx="4" fill="#fef3c7"/><text x="277" y="24" '
                'font-size="10" font-weight="800" fill="#b45309" text-anchor="middle">Sides: 2×(4×3)=24</text>\n'
                '          </g>\n'
                '          <text x="230" y="132" font-size="13" font-weight="900" fill="#2563eb" '
                'text-anchor="middle">Total Surface Area = 40 + 30 + 24 = 94 m²</text>\n'
                '</svg>',
    'title': 'Surface Area of a Cuboid',
    'watch_out': 'If painting a room, remember to EXCLUDE the floor (or ceiling and windows) if instructed!'},
  { 'answer_text': '2 Ends = 2 × 3.142 × 4² = 2 × 3.142 × 16 = 100.54 cm². Curved body = 3.142 × 8 × 10 = 251.36 cm². '
                   'Total SA = 100.54 + 251.36 = 351.9 cm².',
    'challenge_prompt': 'A closed tin can has radius 4 cm and height 10 cm. Find total surface area to 1 decimal place '
                        '(π = 3.142).',
    'dfe_code': 'DfE L2.MSS25',
    'golden_rule': 'Closed Cylinder: 2 circular ends (2 × 3.142 × r²) + curved body (3.142 × d × h)!',
    'id': 'm-l2-28',
    'level': 'l2',
    'level_label': 'Level 2',
    'number': 28,
    'rule_body': 'A closed cylinder net has 3 parts: Two circular ends (2 × 3.142 × r², where r² means r × r) plus one '
                 'unwrapped rectangular body (3.142 × d × h).',
    'rule_heading': 'Total SA = 2πr² + πdh = (2 × 3.142 × r²) + (3.142 × d × h)',
    'strand_name': 'Shape & Space',
    'strand_theme': 'emerald',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(30, 20)">\n'
                '            <rect x="50" y="35" width="180" height="70" fill="#eff6ff" stroke="#3b82f6" '
                'stroke-width="2"/>\n'
                '            <circle cx="140" cy="18" r="16" fill="#bfdbfe" stroke="#1d4ed8" stroke-width="2"/>\n'
                '            <circle cx="140" cy="122" r="16" fill="#bfdbfe" stroke="#1d4ed8" stroke-width="2"/>\n'
                '            <text x="140" y="74" font-size="10.5" font-weight="800" fill="#1e40af" '
                'text-anchor="middle">Body: 3.142 × d × h</text>\n'
                '            <text x="190" y="22" font-size="9" font-weight="800" fill="#1d4ed8">3.142×r²</text>\n'
                '            <text x="190" y="126" font-size="9" font-weight="800" fill="#1d4ed8">3.142×r²</text>\n'
                '          </g>\n'
                '          <g transform="translate(280, 45)">\n'
                '            <rect x="0" y="0" width="155" height="75" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>\n'
                '            <text x="77" y="24" font-size="11" font-weight="800" fill="#0f172a" '
                'text-anchor="middle">Closed Cylinder:</text>\n'
                '            <text x="77" y="46" font-size="9.5" font-weight="800" fill="#2563eb" '
                'text-anchor="middle">2 Ends = 2 × 3.142 × r²</text>\n'
                '            <text x="77" y="64" font-size="9.5" font-weight="800" fill="#059669" '
                'text-anchor="middle">+ Body = 3.142 × d × h</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Surface Area of a Cylinder',
    'watch_out': 'Check if the pipe or can is OPEN at one or both ends — only add circular ends that actually exist.'},
  { 'answer_text': 'Per day = 450 × 3 = 1,350 mg. In 4 days = 1,350 × 4 = 5,400 mg. Grams = 5,400 ÷ 1,000 = 5.4 g.',
    'challenge_prompt': 'A patient requires 450 mg of medication per dose, 3 times a day. How many grams of medication '
                        'is taken in 4 days?',
    'dfe_code': 'DfE L2.MSS26',
    'golden_rule': 'Kilo = 1,000 • Centi = 1/100 • Milli = 1/1,000.',
    'id': 'm-l2-29',
    'level': 'l2',
    'level_label': 'Level 2',
    'number': 29,
    'rule_body': 'Big unit to small unit = MULTIPLY (×). Small unit to big unit = DIVIDE (÷). Length: km (×1000) m '
                 '(×100) cm (×10) mm. Mass: tonne (×1000) kg (×1000) g. Volume: L (×1000) mL.',
    'rule_heading': 'Length, Mass &amp; Capacity Ladders',
    'strand_name': 'Shape & Space',
    'strand_theme': 'emerald',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(30, 20)">\n'
                '            <rect x="0" y="0" width="400" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" '
                'stroke-width="1.8"/>\n'
                '            <text x="200" y="28" font-size="12" font-weight="800" fill="#0f172a" '
                'text-anchor="middle">METRIC CONVERSION LADDERS</text>\n'
                '            <text x="30" y="60" font-size="11" font-weight="700" fill="#2563eb">1 km = 1,000 m  •  1 '
                'm = 100 cm  •  1 cm = 10 mm</text>\n'
                '            <text x="30" y="85" font-size="11" font-weight="700" fill="#059669">1 tonne = 1,000 kg  '
                '•  1 kg = 1,000 g</text>\n'
                '            <text x="30" y="110" font-size="11" font-weight="700" fill="#d97706">1 Litre = 1,000 ml  '
                '•  1 Litre = 1,000 cm³</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Metric Unit Conversions',
    'watch_out': "Don't divide 3.5 m by 100 to get cm! When going from metres to cm, you get MORE units (× 100 = 350 "
                 'cm).'},
  { 'answer_text': '1 m² = 10,000 cm². 3.5 × 10,000 = 35,000 cm².',
    'challenge_prompt': 'Convert 3.5 m² into cm².',
    'dfe_code': 'DfE L2.MSS27',
    'golden_rule': 'Square the conversion factor for area; cube it for volume!',
    'id': 'm-l2-30',
    'level': 'l2',
    'level_label': 'Level 2',
    'number': 30,
    'rule_body': 'To convert square units, apply the linear conversion TWICE (100² = 10,000). To convert cubic units, '
                 'apply conversion THREE TIMES (100³ = 1,000,000).',
    'rule_heading': '1 m² = 10,000 cm²  |  1 m³ = 1,000,000 cm³',
    'strand_name': 'Shape & Space',
    'strand_theme': 'emerald',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(30, 20)">\n'
                '            <rect x="0" y="0" width="190" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" '
                'stroke-width="1.8"/>\n'
                '            <text x="95" y="26" font-size="12" font-weight="800" fill="#1e40af" '
                'text-anchor="middle">SQUARE UNITS (m²)</text>\n'
                '            <text x="95" y="55" font-size="11" font-weight="700" fill="#475569" '
                'text-anchor="middle">1 m = 100 cm</text>\n'
                '            <text x="95" y="80" font-size="11" font-weight="700" fill="#475569" '
                'text-anchor="middle">1 m² = 100 × 100 cm</text>\n'
                '            <rect x="15" y="95" width="160" height="24" rx="4" fill="#3b82f6"/>\n'
                '            <text x="95" y="111" font-size="11" font-weight="800" fill="#ffffff" '
                'text-anchor="middle">1 m² = 10,000 cm²</text>\n'
                '          </g>\n'
                '          <g transform="translate(240, 20)">\n'
                '            <rect x="0" y="0" width="190" height="130" rx="8" fill="#f0fdf4" stroke="#16a34a" '
                'stroke-width="1.8"/>\n'
                '            <text x="95" y="26" font-size="12" font-weight="800" fill="#15803d" '
                'text-anchor="middle">CUBIC UNITS (m³)</text>\n'
                '            <text x="95" y="55" font-size="11" font-weight="700" fill="#475569" '
                'text-anchor="middle">1 m = 100 cm</text>\n'
                '            <text x="95" y="80" font-size="11" font-weight="700" fill="#475569" '
                'text-anchor="middle">1 m³ = 100 × 100 × 100</text>\n'
                '            <rect x="15" y="95" width="160" height="24" rx="4" fill="#16a34a"/>\n'
                '            <text x="95" y="111" font-size="11" font-weight="800" fill="#ffffff" '
                'text-anchor="middle">1 m³ = 1,000,000 cm³</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Converting Square &amp; Cubic Units',
    'watch_out': '1 m² is NOT 100 cm²! That is the most failed unit conversion in Level 2 exams.'},
  { 'answer_text': '70 ÷ 5 = 14. 14 × 8 = 112 km/h.',
    'challenge_prompt': "A UK highway speed limit is 70 mph. A foreign driver's speedometer is in km/h. What is 70 mph "
                        'in km/h? (5 miles ≈ 8 km)',
    'dfe_code': 'DfE L2.MSS28',
    'golden_rule': '5 miles = 8 km. To convert km to miles, multiply by 5 then divide by 8.',
    'id': 'm-l2-31',
    'level': 'l2',
    'level_label': 'Level 2',
    'number': 31,
    'rule_body': 'Memorise standard conversion factors: 5 miles ≈ 8 km (1 mile ≈ 1.6 km). 1 inch ≈ 2.5 cm. 1 kg ≈ 2.2 '
                 'lbs. 1 gallon ≈ 4.5 litres. 1 foot = 12 inches ≈ 30 cm.',
    'rule_heading': 'Core UK Benchmark Ratios',
    'strand_name': 'Shape & Space',
    'strand_theme': 'emerald',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(30, 15)">\n'
                '            <rect x="0" y="0" width="400" height="140" rx="8" fill="#f8fafc" stroke="#cbd5e1" '
                'stroke-width="1.8"/>\n'
                '            <text x="200" y="26" font-size="13" font-weight="800" fill="#0f172a" '
                'text-anchor="middle">KEY IMPERIAL BENCHMARKS</text>\n'
                '            <text x="40" y="55" font-size="11" font-weight="700" fill="#2563eb">Distance: 5 miles ≈ 8 '
                'km  (or 1 mile ≈ 1.6 km)</text>\n'
                '            <text x="40" y="80" font-size="11" font-weight="700" fill="#059669">Weight: 1 kg ≈ 2.2 '
                'pounds (lbs)</text>\n'
                '            <text x="40" y="105" font-size="11" font-weight="700" fill="#d97706">Liquid: 1 gallon ≈ '
                '4.5 litres  •  1 pint ≈ 568 ml</text>\n'
                '            <text x="40" y="128" font-size="11" font-weight="700" fill="#7c3aed">Length: 1 inch ≈ '
                '2.54 cm  •  1 foot ≈ 30 cm</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Metric to Imperial Approximations',
    'watch_out': 'Kilograms are HEAVIER than pounds! 10 kg is about 22 lbs, NOT 4.5 lbs.'},
  { 'answer_text': 'Time = Distance ÷ Speed = 140 ÷ 56 = 2.5 hours. 0.5 hours × 60 = 30 minutes. Journey time = 2 '
                   'hours 30 minutes.',
    'challenge_prompt': 'A train travels 140 miles at an average speed of 56 mph. How long does the journey take in '
                        'hours and minutes?',
    'dfe_code': 'DfE L2.MSS29',
    'golden_rule': 'Minutes to decimal: Divide by 60. Decimal to minutes: Multiply by 60.',
    'id': 'm-l2-32',
    'level': 'l2',
    'level_label': 'Level 2',
    'number': 32,
    'rule_body': 'Distance = Speed × Time. Speed = Distance ÷ Time. Time = Distance ÷ Speed. Decimal hours must be '
                 'converted: Multiply decimal minutes by 60 (0.4 hrs = 24 mins).',
    'rule_heading': 'D = S × T  |  Decimal Time Warning',
    'strand_name': 'Shape & Space',
    'strand_theme': 'emerald',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(25, 12)">\n'
                '            <polygon points="100,5 10,140 190,140" fill="#f8fafc" stroke="#0f172a" '
                'stroke-width="3"/>\n'
                '            <line x1="45" y1="80" x2="155" y2="80" stroke="#0f172a" stroke-width="3"/>\n'
                '            <line x1="100" y1="80" x2="100" y2="140" stroke="#0f172a" stroke-width="3"/>\n'
                '            <text x="32" y="74" font-size="14" font-weight="900" fill="#64748b">÷</text>\n'
                '            <text x="168" y="74" font-size="14" font-weight="900" fill="#64748b">÷</text>\n'
                '            <text x="100" y="115" font-size="16" font-weight="900" fill="#64748b" '
                'text-anchor="middle">×</text>\n'
                '            <circle cx="100" cy="46" r="24" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>\n'
                '            <text x="100" y="54" font-size="22" font-weight="900" fill="#1e40af" '
                'text-anchor="middle">D</text>\n'
                '            <circle cx="58" cy="112" r="22" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>\n'
                '            <text x="58" y="119" font-size="20" font-weight="900" fill="#b45309" '
                'text-anchor="middle">S</text>\n'
                '            <circle cx="142" cy="112" r="22" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>\n'
                '            <text x="142" y="119" font-size="20" font-weight="900" fill="#15803d" '
                'text-anchor="middle">T</text>\n'
                '          </g>\n'
                '          <g transform="translate(235, 15)">\n'
                '            <rect x="0" y="0" width="200" height="135" rx="8" fill="#fffbeb" stroke="#f59e0b" '
                'stroke-width="1.8"/>\n'
                '            <text x="100" y="24" font-size="11.5" font-weight="900" fill="#b45309" '
                'text-anchor="middle">S-D-T FORMULAS</text>\n'
                '            <rect x="10" y="32" width="180" height="24" rx="4" fill="#2563eb"/>\n'
                '            <text x="100" y="48" font-size="11" font-weight="800" fill="#ffffff" '
                'text-anchor="middle">Distance = Speed × Time</text>\n'
                '            <rect x="10" y="60" width="180" height="24" rx="4" fill="#d97706"/>\n'
                '            <text x="100" y="76" font-size="11" font-weight="800" fill="#ffffff" '
                'text-anchor="middle">Speed = Distance ÷ Time</text>\n'
                '            <rect x="10" y="88" width="180" height="24" rx="4" fill="#16a34a"/>\n'
                '            <text x="100" y="104" font-size="11" font-weight="800" fill="#ffffff" '
                'text-anchor="middle">Time = Distance ÷ Speed</text>\n'
                '            <text x="100" y="125" font-size="9.5" font-weight="800" fill="#dc2626" '
                'text-anchor="middle">⚠️ 45m = 0.75h (NEVER 0.45!)</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Speed, Distance &amp; Time',
    'watch_out': '2 hours 45 minutes on a calculator is 2.75, NEVER 2.45!'},
  { 'answer_text': 'Mass = Density × Volume = 8.5 × 450 = 3,825 grams. In kilograms = 3,825 ÷ 1,000 = 3.825 kg.',
    'challenge_prompt': 'A solid brass statue has a volume of 450 cm³ and a density of 8.5 g/cm³. What is the mass of '
                        'the statue in kilograms?',
    'dfe_code': 'DfE L2.MSS30',
    'golden_rule': "Remember: 'Department of Motor Vehicles' (D-M-V) or Mass on top!",
    'id': 'm-l2-33',
    'level': 'l2',
    'level_label': 'Level 2',
    'number': 33,
    'rule_body': 'Mass = Density × Volume. Density = Mass ÷ Volume (written in g/cm³ or kg/m³). Volume = Mass ÷ '
                 'Density. Density measures how tightly matter is packed.',
    'rule_heading': 'M = D × V  (MDV Triangle)',
    'strand_name': 'Shape & Space',
    'strand_theme': 'emerald',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(25, 12)">\n'
                '            <polygon points="100,5 10,140 190,140" fill="#f8fafc" stroke="#0f172a" '
                'stroke-width="3"/>\n'
                '            <line x1="45" y1="80" x2="155" y2="80" stroke="#0f172a" stroke-width="3"/>\n'
                '            <line x1="100" y1="80" x2="100" y2="140" stroke="#0f172a" stroke-width="3"/>\n'
                '            <text x="32" y="74" font-size="14" font-weight="900" fill="#64748b">÷</text>\n'
                '            <text x="168" y="74" font-size="14" font-weight="900" fill="#64748b">÷</text>\n'
                '            <text x="100" y="115" font-size="16" font-weight="900" fill="#64748b" '
                'text-anchor="middle">×</text>\n'
                '            <circle cx="100" cy="46" r="24" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>\n'
                '            <text x="100" y="54" font-size="22" font-weight="900" fill="#5b21b6" '
                'text-anchor="middle">M</text>\n'
                '            <circle cx="58" cy="112" r="22" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>\n'
                '            <text x="58" y="119" font-size="20" font-weight="900" fill="#0369a1" '
                'text-anchor="middle">D</text>\n'
                '            <circle cx="142" cy="112" r="22" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>\n'
                '            <text x="142" y="119" font-size="20" font-weight="900" fill="#15803d" '
                'text-anchor="middle">V</text>\n'
                '          </g>\n'
                '          <g transform="translate(235, 15)">\n'
                '            <rect x="0" y="0" width="200" height="135" rx="8" fill="#f5f3ff" stroke="#7c3aed" '
                'stroke-width="1.8"/>\n'
                '            <text x="100" y="24" font-size="11.5" font-weight="900" fill="#5b21b6" '
                'text-anchor="middle">M-D-V FORMULAS</text>\n'
                '            <rect x="10" y="32" width="180" height="24" rx="4" fill="#7c3aed"/>\n'
                '            <text x="100" y="48" font-size="11" font-weight="800" fill="#ffffff" '
                'text-anchor="middle">Mass = Density × Volume</text>\n'
                '            <rect x="10" y="60" width="180" height="24" rx="4" fill="#0284c7"/>\n'
                '            <text x="100" y="76" font-size="11" font-weight="800" fill="#ffffff" '
                'text-anchor="middle">Density = Mass ÷ Volume</text>\n'
                '            <rect x="10" y="88" width="180" height="24" rx="4" fill="#16a34a"/>\n'
                '            <text x="100" y="104" font-size="11" font-weight="800" fill="#ffffff" '
                'text-anchor="middle">Volume = Mass ÷ Density</text>\n'
                '            <text x="100" y="125" font-size="9.5" font-weight="800" fill="#4338ca" '
                'text-anchor="middle">⚖️ g with cm³ | kg with m³</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Density, Mass &amp; Volume',
    'watch_out': 'Check units: If density is in g/cm³, volume must be in cm³ and mass must be in grams.'},
  { 'answer_text': 'Real length = 8.5 × 200 = 1,700 cm. In metres = 1,700 ÷ 100 = 17 metres.',
    'challenge_prompt': 'On an architectural blueprint with scale 1 : 200, a sports hall wall measures 8.5 cm. What is '
                        'the actual length of the wall in metres?',
    'dfe_code': 'DfE L2.MSS31',
    'golden_rule': 'Both sides of a scale ratio start in the SAME unit (centimetres)!',
    'id': 'm-l2-34',
    'level': 'l2',
    'level_label': 'Level 2',
    'number': 34,
    'rule_body': 'Scale 1 : 50 means 1 cm on paper represents 50 cm in real life (0.5 m). Scale 1 : 25,000 means 1 cm '
                 '= 250 m. Map to Real: MULTIPLY. Real to Map: DIVIDE.',
    'rule_heading': 'Scale Ratios (1 : n)',
    'strand_name': 'Shape & Space',
    'strand_theme': 'emerald',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(40, 20)">\n'
                '            <rect x="0" y="0" width="180" height="125" rx="8" fill="#eff6ff" stroke="#3b82f6" '
                'stroke-width="1.8"/>\n'
                '            <text x="90" y="26" font-size="12" font-weight="800" fill="#1e40af" '
                'text-anchor="middle">ARCHITECTURAL: 1:50</text>\n'
                '            <text x="15" y="55" font-size="11" font-weight="700" fill="#0f172a">1 cm on plan = 50 cm '
                'real</text>\n'
                '            <text x="15" y="80" font-size="11" font-weight="700" fill="#0f172a">50 cm = 0.5 '
                'metres</text>\n'
                '            <rect x="15" y="92" width="150" height="24" rx="4" fill="#3b82f6"/>\n'
                '            <text x="90" y="108" font-size="11" font-weight="800" fill="#ffffff" '
                'text-anchor="middle">6 cm on plan = 3.0 m</text>\n'
                '          </g>\n'
                '          <g transform="translate(240, 20)">\n'
                '            <rect x="0" y="0" width="180" height="125" rx="8" fill="#fffbeb" stroke="#f59e0b" '
                'stroke-width="1.8"/>\n'
                '            <text x="90" y="26" font-size="12" font-weight="800" fill="#b45309" '
                'text-anchor="middle">MAP SCALE: 1:25,000</text>\n'
                '            <text x="15" y="55" font-size="11" font-weight="700" fill="#0f172a">1 cm = 25,000 '
                'cm</text>\n'
                '            <text x="15" y="80" font-size="11" font-weight="700" fill="#0f172a">25,000 cm ÷ 100 = 250 '
                'm</text>\n'
                '            <rect x="15" y="92" width="150" height="24" rx="4" fill="#f59e0b"/>\n'
                '            <text x="90" y="108" font-size="11" font-weight="800" fill="#ffffff" '
                'text-anchor="middle">4 cm = 1,000 m (1 km)</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Scale Drawings &amp; Maps',
    'watch_out': 'Always convert cm to metres (÷ 100) or km (÷ 100,000) for real-world answers.'},
  { 'answer_text': 'Since 072° < 180°, add 180°: Back bearing = 072° + 180° = 252°.',
    'challenge_prompt': 'The bearing of town B from town A is 072°. What is the back-bearing of town A from town B?',
    'dfe_code': 'DfE L2.MSS32',
    'golden_rule': 'Always 3 digits! 55° must be written as 055°.',
    'id': 'm-l2-35',
    'level': 'l2',
    'level_label': 'Level 2',
    'number': 35,
    'rule_body': '1. Measure angle clockwise starting from North line (000°). 2. Always write using THREE digits (e.g. '
                 '045°, 090°, 260°). Back bearing = Add or subtract 180°.',
    'rule_heading': 'North • Clockwise • 3 Figures',
    'strand_name': 'Shape & Space',
    'strand_theme': 'emerald',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(130, 20)">\n'
                '            <circle cx="100" cy="65" r="55" fill="#f8fafc" stroke="#334155" stroke-width="2"/>\n'
                '            <line x1="100" y1="10" x2="100" y2="65" stroke="#dc2626" stroke-width="2.5"/>\n'
                '            <polygon points="100,5 96,15 104,15" fill="#dc2626"/>\n'
                '            <text x="100" y="0" font-size="12" font-weight="900" fill="#dc2626" '
                'text-anchor="middle">N (000°)</text>\n'
                '            <line x1="100" y1="65" x2="145" y2="30" stroke="#2563eb" stroke-width="2.5"/>\n'
                '            <path d="M 100,35 A 30,30 0 0,1 125,48" fill="none" stroke="#2563eb" stroke-width="2"/>\n'
                '            <text x="120" y="32" font-size="11" font-weight="800" fill="#2563eb">055°</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Bearings (3-Figure Bearings)',
    'watch_out': "Check which location the bearing is measured FROM: 'Bearing of B from A' means draw North at A!"},
  { 'answer_text': 'The side elevation shows the step profile (staircase outline).',
    'challenge_prompt': 'A 3D stepped staircase block is 3 cubes wide, 2 cubes deep, and 3 cubes high. Which 2D '
                        'elevation shows the step pattern?',
    'dfe_code': 'DfE L2.MSS33',
    'golden_rule': 'Draw each 2D projection as if you are standing directly in line with that face!',
    'id': 'm-l2-36',
    'level': 'l2',
    'level_label': 'Level 2',
    'number': 36,
    'rule_body': "Plan View = Looking straight down from the bird's eye view. Front Elevation = Looking straight from "
                 'front. Side Elevation = Looking straight from side.',
    'rule_heading': 'Plan View • Front • Side Elevation',
    'strand_name': 'Shape & Space',
    'strand_theme': 'emerald',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(30, 20)">\n'
                '            <rect x="0" y="0" width="120" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>\n'
                '            <text x="60" y="24" font-size="11" font-weight="800" fill="#1e40af" '
                'text-anchor="middle">PLAN VIEW</text>\n'
                '            <rect x="25" y="40" width="70" height="60" fill="#93c5fd" stroke="#2563eb"/>\n'
                '            <text x="60" y="115" font-size="9.5" font-weight="700" fill="#64748b" '
                'text-anchor="middle">From Above</text>\n'
                '          </g>\n'
                '          <g transform="translate(170, 20)">\n'
                '            <rect x="0" y="0" width="120" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>\n'
                '            <text x="60" y="24" font-size="11" font-weight="800" fill="#15803d" '
                'text-anchor="middle">FRONT ELEVATION</text>\n'
                '            <rect x="25" y="55" width="70" height="45" fill="#86efac" stroke="#16a34a"/>\n'
                '            <text x="60" y="115" font-size="9.5" font-weight="700" fill="#64748b" '
                'text-anchor="middle">From Front</text>\n'
                '          </g>\n'
                '          <g transform="translate(310, 20)">\n'
                '            <rect x="0" y="0" width="120" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>\n'
                '            <text x="60" y="24" font-size="11" font-weight="800" fill="#b45309" '
                'text-anchor="middle">SIDE ELEVATION</text>\n'
                '            <rect x="35" y="55" width="50" height="45" fill="#fde68a" stroke="#d97706"/>\n'
                '            <text x="60" y="115" font-size="9.5" font-weight="700" fill="#64748b" '
                'text-anchor="middle">From Side</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Plans &amp; Elevations',
    'watch_out': 'Plan view NEVER shows height — it only shows width and depth.'}]
