#!/usr/bin/env python3
"""
Update maths domain files to use plain, easy-to-understand language and simplified formulas.
"""
import re

def update_domain4():
    import maths_domain4_geometry as d4
    topics = d4.TOPICS_DOMAIN4

    for t in topics:
        if t['filename'] == 'functional-skills-circles.html':
            t['golden_rules'] = [
                {
                    'icon': 'fa-circle',
                    'title': 'Golden Rule 1: The Two Circle Formulas in Plain English',
                    'desc': '• Distance around outside (Circumference) = 3.142 × Diameter.<br>• Flat surface inside (Area) = 3.142 × Radius × Radius.<br>Golden Check: If given the diameter, halve it first to get the radius ($Radius = Diameter \\div 2$)!',
                    'badge': 'Circumference = 3.142 × Diameter | Area = 3.142 × Radius × Radius'
                },
                {
                    'icon': 'fa-arrows-left-right',
                    'title': 'Golden Rule 2: Multiply the Radius by Itself First',
                    'desc': 'To find circle area: calculate Radius × Radius first, then multiply by 3.142. Never multiply 3.142 by the radius and then square that result!',
                    'badge': 'Area = 3.142 × Radius × Radius'
                }
            ]
            t['skills'] = [
                {
                    'title': 'Radius vs Diameter & Semi-Circles',
                    'summary': 'Never use diameter in the area formula without halving it first.',
                    'content_html': '''
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Radius (r):</strong> Distance from the exact center to the edge (e.g. 4 cm).</li>
                    <li><strong>Diameter (d):</strong> Distance all the way across through the center (e.g. 8 cm). Diameter = 2 × Radius.</li>
                    <li><strong>Semi-Circle Perimeter:</strong> Half the outer curve plus the straight flat edge: <em>(3.142 × Diameter ÷ 2) + Diameter.</em></li>
                    <li><strong>Semi-Circle Area:</strong> Exactly half the full circle area: <em>(3.142 × Radius × Radius) ÷ 2.</em></li>
                  </ul>
                </div>
                '''
                }
            ]
            t['worked_models'][0]['steps'] = [
                ('Step 1', 'Find the radius of the circular lawn', 'Radius = Diameter ÷ 2 = 12 m ÷ 2 = 6 metres.', 'B1: Radius identification'),
                ('Step 2', 'Calculate Area = 3.14 × Radius × Radius', 'Area = 3.14 × 6 × 6 = 3.14 × 36 = 113.04 m².', 'M1: Plain area formula execution'),
                ('Step 3', 'Calculate Circumference = 3.14 × Diameter', 'Circumference = 3.14 × 12 m = 37.68 metres.', 'A1: Accurate circumference calculation')
            ]
            t['worked_models'][0]['tutor_tip'] = 'Remember the plain English rule: For Area, multiply radius by itself first (6 × 6 = 36), then by 3.14. For Circumference, multiply 3.14 by the full diameter (12)!'
            t['practice_questions'][0]['solution_steps'] = '1. Diameter = 2.5 × 2 = 5 metres.<br>2. Circumference = 3.14 × Diameter = 3.14 × 5 = 15.7 metres.'
            t['practice_questions'][0]['tutor_tip'] = 'Circumference = 3.14 × Diameter = 3.14 × 5 = 15.7 m.'

        elif t['filename'] == 'functional-skills-surface-area.html':
            t['golden_rules'] = [
                {
                    'icon': 'fa-cubes',
                    'title': 'Golden Rule 1: Surface Area is the Total Area of All Outside Faces',
                    'desc': 'Surface area is 2D area (measured in cm² or m²), NOT 3D volume. For a cuboid: calculate the area of each face and add all 6 faces together: (2 × Top/Bottom) + (2 × Front/Back) + (2 × Left/Right).',
                    'badge': 'Cuboid Surface Area = Sum of all 6 faces'
                },
                {
                    'icon': 'fa-circle-notch',
                    'title': 'Golden Rule 2: Cylinder Surface Area = Two Circles Plus One Unwrapped Rectangle',
                    'desc': 'The curved body unrolls into a flat rectangle (length = circumference = 3.142 × Diameter, height = cylinder height). Add the two circle ends (2 × π r² = 2 × 3.142 × r², where r² means radius squared: r × r): Total Surface Area = 2πr² + πdh = (2 × 3.142 × r²) + (3.142 × d × h).',
                    'badge': 'Cylinder SA = 2πr² + πdh = (2 × 3.142 × r²) + (3.142 × d × h) (r² = r × r)'
                }
            ]

        elif t['filename'] == 'functional-skills-angles-in-2d-shapes.html':
            t['golden_rules'] = [
                {
                    'icon': 'fa-draw-polygon',
                    'title': 'Golden Rule 1: Total Inside Angles = (Number of Sides - 2) × 180°',
                    'desc': 'To find the total degrees inside any straight-sided shape: subtract 2 from the number of sides, then multiply by 180°. Triangle (3 sides) = 1 × 180° = 180°. Quadrilateral (4 sides) = 2 × 180° = 360°. Pentagon (5 sides) = 3 × 180° = 540°. Hexagon (6 sides) = 4 × 180° = 720°.',
                    'badge': 'Total Inside Angles = (Sides - 2) × 180°'
                },
                {
                    'icon': 'fa-circle',
                    'title': 'Golden Rule 2: Outside Angles Always Add Up to 360°',
                    'desc': 'If you walk all the way around the outside of any polygon, you make one full turn (360°). For a regular shape where all sides are equal: Each Outside Angle = 360° ÷ Number of Sides.',
                    'badge': 'Each Outside Angle = 360° ÷ Number of Sides'
                }
            ]

    with open('maths_domain4_geometry.py', 'w', encoding='utf-8') as f:
        f.write('#!/usr/bin/env python3\n"""Maths Domain 4: Shape, Space & Geometry (10 Core Topics)"""\n')
        f.write('TOPICS_DOMAIN4 = ' + repr(topics) + '\n')
    print('✓ Updated maths_domain4_geometry.py')

def update_domain3():
    import maths_domain3_measures as d3
    topics = d3.TOPICS_DOMAIN3

    for t in topics:
        if t['filename'] == 'functional-skills-speed.html':
            t['golden_rules'] = [
                {
                    'icon': 'fa-gauge',
                    'title': 'Golden Rule 1: Speed, Distance & Time Formula Triangle',
                    'desc': 'Cover what you want to find with your thumb:<br>• <strong>Distance = Speed × Time</strong><br>• <strong>Speed = Distance ÷ Time</strong><br>• <strong>Time = Distance ÷ Speed</strong>',
                    'badge': 'Distance = Speed × Time | Speed = Distance ÷ Time | Time = Distance ÷ Speed'
                },
                {
                    'icon': 'fa-stopwatch',
                    'title': 'Golden Rule 2: Divide Minutes by 60 to Get Decimal Hours',
                    'desc': 'Never write 45 minutes as 0.45! To turn minutes into decimal hours, divide by 60 (15 mins = 0.25 hrs, 30 mins = 0.5 hrs, 45 mins = 0.75 hrs). To turn decimal hours back into minutes, multiply by 60 (0.4 hrs × 60 = 24 mins).',
                    'badge': 'Decimal Hours = Minutes ÷ 60 | Minutes = Decimal Hours × 60'
                }
            ]
        elif t['filename'] == 'functional-skills-density.html':
            t['golden_rules'] = [
                {
                    'icon': 'fa-cube',
                    'title': 'Golden Rule 1: Density, Mass & Volume Formula Triangle',
                    'desc': 'Mass is at the top of the triangle:<br>• <strong>Mass = Density × Volume</strong><br>• <strong>Density = Mass ÷ Volume</strong><br>• <strong>Volume = Mass ÷ Density</strong>',
                    'badge': 'Mass = Density × Volume | Density = Mass ÷ Volume | Volume = Mass ÷ Density'
                },
                {
                    'icon': 'fa-weight-hanging',
                    'title': 'Golden Rule 2: Ensure Mass and Volume Units Match Density',
                    'desc': 'If density is given in g/cm³, mass MUST be in grams and volume in cm³. If density is kg/m³, convert mass to kg and volume to m³.',
                    'badge': 'g/cm³ → g and cm³ | kg/m³ → kg and m³'
                }
            ]

    with open('maths_domain3_measures.py', 'w', encoding='utf-8') as f:
        f.write('#!/usr/bin/env python3\n"""Maths Domain 3: Measures, Instruments & Compound Units (7 Core Topics)"""\n')
        f.write('TOPICS_DOMAIN3 = ' + repr(topics) + '\n')
    print('✓ Updated maths_domain3_measures.py')

def update_domain2():
    import maths_domain2_finance_ratio as d2
    topics = d2.TOPICS_DOMAIN2

    for t in topics:
        if t['filename'] == 'functional-skills-ratio.html':
            t['golden_rules'][0] = {
                'icon': 'fa-arrows-split-up-and-left',
                'title': 'Golden Rule 1: The 3-Step Ratio Sharing Rule (Add, Divide, Multiply)',
                'desc': '1. <strong>Add</strong> the ratio numbers together to find the total number of parts.<br>2. <strong>Divide</strong> the total money or items by the total parts to find the value of 1 part.<br>3. <strong>Multiply</strong> the 1-part value by each ratio number.',
                'badge': '1. Add Parts → 2. Divide Total by Parts → 3. Multiply by Each Part'
            }
        elif t['filename'] == 'functional-skills-interest-and-compound-interest.html':
            t['golden_rules'][1] = {
                'icon': 'fa-chart-line',
                'title': 'Golden Rule 2: Compound Interest: Calculate Year by Year',
                'desc': 'Compound interest adds each year\'s interest to the balance before calculating the next year\'s interest. Year 1: Starting Money × Rate. Year 2: Calculate interest on the NEW combined balance! Or multiply by the decimal multiplier for each year: Starting Balance × Multiplier × Multiplier.',
                'badge': 'Starting Balance × Multiplier for Each Year'
            }

    with open('maths_domain2_finance_ratio.py', 'w', encoding='utf-8') as f:
        f.write('#!/usr/bin/env python3\n"""Maths Domain 2: Financial Maths, Ratio & Proportion (7 Core Topics)"""\n')
        f.write('TOPICS_DOMAIN2 = ' + repr(topics) + '\n')
    print('✓ Updated maths_domain2_finance_ratio.py')

if __name__ == '__main__':
    update_domain4()
    update_domain3()
    update_domain2()
