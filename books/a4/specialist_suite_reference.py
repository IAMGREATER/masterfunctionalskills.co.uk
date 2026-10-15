"""
specialist_suite_reference.py
=============================================================================
Reference data, worked solutions, mark schemes, formulas, glossaries, and
indices for the 4 Master Functional Skills Specialist Publications:
  1. Mock Pack Maths Level 2
  2. Mock Pack English Level 2
  3. Digital Skills Handbook
  4. BKSB Remediation Workbook

Zero generic filler. Condensed reference typography compatible with K.ref_pages().
=============================================================================
"""

# =============================================================================
# 1. MATHS LEVEL 2 MOCK PACK REFERENCE DATA
# =============================================================================

MATHS_L2_FORMULAS = r"""<div style='font-size:10pt; line-height:1.4;'>
<p><b>Perimeter, Area &amp; Circumference:</b><br>
&bull; Area of rectangle = Length × Width &emsp; Perimeter = 2 × (Length + Width)<br>
&bull; Area of triangle = (Base × Height) ÷ 2<br>
&bull; Area of parallelogram = Base × Height &emsp; Area of trapezium = ((Top + Bottom) ÷ 2) × Height<br>
&bull; Circle Circumference = 3.142 × Diameter &emsp; Circle Area = 3.142 × Radius² (Use π = 3.142 or 3.14)</p>

<p><b>3D Solids, Volume &amp; Surface Area:</b><br>
&bull; Volume of cuboid = Length × Width × Height &emsp; Surface Area = 2 × (LW + LH + WH)<br>
&bull; Volume of prism = Cross-sectional Area × Length<br>
&bull; Volume of cylinder = 3.142 × Radius² × Height &emsp; Curved Surface Area = 2 × 3.142 × Radius × Height</p>

<p><b>Compound Measures &amp; Rates:</b><br>
&bull; Speed = Distance ÷ Time &emsp; Distance = Speed × Time &emsp; Time = Distance ÷ Speed<br>
&bull; Density = Mass ÷ Volume &emsp; Mass = Density × Volume<br>
&bull; Percentage Change = (Actual Change ÷ Original Value) × 100%<br>
&bull; Reverse Percentage: Original = New Value ÷ Decimal Multiplier</p>

<p><b>Statistics &amp; Conversions:</b><br>
&bull; Estimated Mean = Total of (Midpoint × Frequency) ÷ Total Frequency<br>
&bull; 1 m³ = 1,000 litres &emsp; 1 gallon ≈ 4.55 litres &emsp; 1 mile ≈ 1.6 km &emsp; 5 miles ≈ 8 km</p>
</div>"""

MATHS_L2_GLOSSARY = [
    ("Angle of Elevation", "The angle between the horizontal line of sight and the line of sight up to an object."),
    ("Compound Interest", "Interest computed on the initial principal and on all previous accumulated interest."),
    ("Critical Path", "The sequence of project stages which determine the minimum time needed for an operation."),
    ("Decimal Multiplier", "A single factor used to calculate percentage increase (e.g. 1.15 for +15%) or decrease (0.85 for -15%)."),
    ("Density", "Mass per unit volume (e.g. grams per cubic centimetre or kilograms per cubic metre)."),
    ("Estimated Mean", "An estimate of the arithmetic average for grouped continuous data using class interval midpoints."),
    ("Hypotenuse", "The side opposite the right angle in any right-angled triangle, governed by Pythagoras' Theorem (a² + b² = c²)."),
    ("Line of Best Fit", "A straight trend line drawn on a scatter diagram representing the balance of points."),
    ("Margin of Error", "The allowable deviation or tolerance in practical measurements or financial forecasts."),
    ("Process Mark [P]", "A mark awarded by Pearson examiners for adopting an appropriate mathematical problem-solving method."),
    ("Range", "The difference between the highest and lowest values in a numerical data set, representing spread."),
    ("Reverse Percentage", "The mathematical technique to recover an original quantity before a percentage tax, markup, or discount was applied."),
    ("Scale Factor", "The ratio of linear dimensions on a technical plan or map to the true real-world dimensions (e.g. 1:50)."),
    ("Tolerance", "The permissible limit of variation in a physical dimension or specification (e.g. 250 mm ± 2 mm).")
]

MATHS_L2_INDEX = [
    ("A", [("Angle calculations", "3"), ("Area of circle & cylinder", "3, 11, 27"), ("Average speed & distance", "4, 15, 31")]),
    ("B", [("Best buy & supplier analysis", "16, 32, 48"), ("Budgeting & payroll wage costs", "9, 25, 41")]),
    ("C", [("Compound interest", "4, 18"), ("Conversion of units (metric/imperial)", "4, 21, 37"), ("Cylinder volume & capacity", "3, 13, 29")]),
    ("D", [("Decimals & long multiplication", "7, 23, 39"), ("Density, mass & volume", "4, 14, 30")]),
    ("E", [("Estimated mean (grouped data)", "4, 12, 28"), ("Exam strategy & process marks", "5")]),
    ("F", [("Fractions: mixed numbers & addition", "8, 24, 40"), ("Freight & transport logistics", "15, 31")]),
    ("G", [("Geometry & Pythagoras", "3, 14, 30"), ("Grade boundaries & scaling", "55")]),
    ("I", [("Inverse calculation checks", "5, 8, 24"), ("Invoices & commercial purchasing", "7, 23, 39")]),
    ("M", [("Mark schemes for Mocks 1-6", "56-79"), ("Mean, median, mode & range", "4, 12, 28")]),
    ("P", [("Percentage increase, decrease & reverse", "8, 11, 24"), ("Probability of independent events", "4, 12, 28"), ("Pythagoras theorem", "3, 14, 30")]),
    ("R", [("Radius, diameter & circumference", "3, 7, 23"), ("Ratio sharing in practical contexts", "10, 26, 42")]),
    ("S", [("Scatter diagrams & correlation", "12, 28, 44"), ("Speed, distance & arrival times", "4, 15, 31")]),
    ("T", [("Tolerance & engineering limits", "10, 26, 42"), ("Triangular prism capacity", "3, 13, 29")])
]

MATHS_L2_MOCK_SOLUTIONS = {
    1: [
        ("Mock 1 &bull; Section A (Non-Calculator)", 
         "<b>Q1. Commercial Invoice:</b> 15 units at £15.70 = £235.50. Delivery fee = £24.30. Total payable = £235.50 + £24.30 = <b>£259.80</b> [P1 for multiplication layout, M1 for addition, A1 for £259.80, B1 for £ symbol].<br>"
         "<b>Q2. Circular Storage Area:</b> Radius r = 2.0 m. Area A = 3.142 r² = 3.14 × (2.0)² = 3.14 × 4 = <b>12.56 m²</b> [M1 for squaring radius, A1 for 12.56, B1 for m² units].<br>"
         "<b>Q3. Mixed Fractions:</b> 2 2/4 + 1 2/3 = 2 1/2 + 1 2/3 = 5/2 + 5/3 = 15/6 + 10/6 = 25/6 = <b>4 1/6</b> [M1 for common denominator 6, A1 for 4 1/6].<br>"
         "<b>Q4. Reverse Discount:</b> Sale price = £375 after 12% discount. Original multiplier = 1.00 - 0.12 = 0.88. Original fee = 375 ÷ 0.88 = <b>£426.14</b>. Check: 426.14 × 0.88 = 375.00 [P1 for identifying 0.88, A1 for £426.14, B1 for valid check].<br>"
         "<b>Q5. Ratio Allocation:</b> Total parts = 3 + 5 = 8. One part = 640 ÷ 8 = 80. Parts: 3 × 80 = 240, 5 × 80 = 400. Difference = 400 - 240 = <b>160 units</b> [M1 for dividing by 8, A1 for 160]."),
        ("Mock 1 &bull; Section B (Calculator Permitted &bull; Part 1)",
         "<b>Q6. Staffing Payroll:</b> 9 operatives work 8.0 hrs at £11.44 = 9 × 8 × 11.44 = £823.68. 2 supervisors work 9 hrs at £16.50 = 2 × 9 × 16.50 = £297.00. Total wages = £823.68 + £297.00 = <b>£1,120.68</b> [P1 for operative subtotal, P1 for supervisor subtotal, A1 for £1,120.68].<br>"
         "<b>Q7. Flooring Area &amp; Cost:</b> Composite room dimensions 8.5 m × 6.2 m = 52.7 m², minus recess 2.0 m × 1.5 m = 3.0 m². Net area = 49.7 m². Flooring pack covers 2.2 m². Packs needed = 49.7 ÷ 2.2 = 22.59 → 23 packs. Cost = 23 × £28.50 = <b>£655.50</b> [P1 for net area, P1 for rounding up packs, A1 for £655.50].<br>"
         "<b>Q8. Grouped Mean Delivery Time:</b> Midpoints: 5-9 min (7 × 12 = 84), 10-14 min (12 × 25 = 300), 15-19 min (17 × 18 = 306), 20-24 min (22 × 5 = 110). Total Total  fx = 800. Total frequency N = 60. Estimated mean = 800 ÷ 60 = <b>13.33 minutes (or 13 min  20 s) [M1 for midpoints, M1 for Total  fx, A1 for 13.3 min].<br>"
         "<b>Q9. Fuel Economy &amp; Journey Cost:</b> Distance = 184 miles. Consumption = 42 mpg. Gallons = 184 ÷ 42 = 4.381 gallons. Litres = 4.381 × 4.55 = 19.93 litres. Fuel cost at £1.48/litre = 19.93 × 1.48 = <b>£29.50</b> [P1 for gallon conversion, P1 for litre conversion, A1 for £29.50].<br>"
         "<b>Q10. Storage Tank Volume:</b> Cylinder radius r = 1.2 m, height h = 2.8 m. Volume V = 3.142 r² h = 3.142 × (1.2)² × 2.8 = 3.142 × 1.44 × 2.8 = 12.67 m³. Capacity in litres = 12.67 × 1,000 = <b>12,670 litres</b> [M1 for formula, P1 for m³ to litres, A1 for 12,670 litres]."),
        ("Mock 1 &bull; Section B (Calculator Permitted &bull; Part 2)",
         "<b>Q11. Operating Margin:</b> Revenue = £19,200. Costs = £13,300. Profit = 19,200 - 13,300 = £5,900. Percentage profit of revenue = (5,900 ÷ 19,200) × 100 = <b>30.7%</b> [M1 for profit calculation, P1 for dividing by revenue, A1 for 30.7% rounded to 1 d.p.].<br>"
         "<b>Q12. Independent Quality Probability:</b> Component A defect rate = 1/25 (pass = 24/25). Component B defect rate = 1/40 (pass = 39/40). Neither defective = 24/25 × 39/40 = 936/1000 = <b>0.936 (or 93.6%) [P1 for pass probabilities, M1 for multiplying independent fractions, A1 for 0.936].<br>"
         "<b>Q13. Travel Duration &amp; Arrival:</b> Distance = 125 miles. Speed = 44 mph. Time = 125 ÷ 44 = 2.841 hours. 0.841 × 60 = 50.46 ≈ 50 mins. Travel time = 2 hrs 50 mins. Departure = 13:45. Arrival = 13:45 + 2h  50m = <b>16:35</b> [P1 for decimal hours, P1 for converting to minutes, A1 for 16:35].<br>"
         "<b>Q14. Loading Ramp Hypotenuse:</b> Vertical height a = 1.3 m, horizontal run b = 5.0 m. c² = a² + b² = 1.3² + 5.0² = 1.69 + 25.00 = 26.69. Sloping length c = √(26.69) = <b>5.17 m</b> [M1 for Pythagoras substitution, A1 for 5.17 m].<br>"
         "<b>Q15. Commercial Supplier Comparison:</b> Supplier A: Material £470 with 12% discount = 470 × 0.88 = £413.60. Free delivery. Total A = £413.60. Supplier B: Material £500 with 25% discount = 500 × 0.75 = £375.00 plus £15 delivery = £390.00. Comparison: <b>Supplier B is cheaper by £23.60</b> (413.60 - 390.00 = £23.60) [P1 for Supplier A net, P1 for Supplier B net with delivery, A1 for Supplier B selection and £23.60 saving].")
    ],
    2: [
        ("Mock 2 &bull; Section A (Non-Calculator)",
         "<b>Q1. Warehouse Logistics Invoice:</b> 18 crates at £16.90 = £304.20. Express surcharge = £23.80. Total payable = £304.20 + £23.80 = <b>£328.00</b> [P1 for layout, M1 for addition, A1 for £328.00].<br>"
         "<b>Q2. Circular Basin Area:</b> Radius r = 2.2 m. Area A = 3.142 r² = 3.14 × (2.2)² = 3.14 × 4.84 = <b>15.20 m²</b> [M1 for squaring, A1 for 15.20, B1 for m²].<br>"
         "<b>Q3. Mixed Fractions:</b> 2 3/4 + 1 2/3 = 11/4 + 5/3 = 33/12 + 20/12 = 53/12 = <b>4 5/12</b> [M1 for common denominator 12, A1 for 4 5/12].<br>"
         "<b>Q4. Reverse Discount:</b> Sale price = £390 after 14% discount. Multiplier = 1.00 - 0.14 = 0.86. Original price = 390 ÷ 0.86 = <b>£453.49</b>. Check: 453.49 × 0.86 = £390.00 [P1 for 0.86, A1 for £453.49, B1 for check].<br>"
         "<b>Q5. Ratio Packaging:</b> Ratio 4:7, total parts = 11. Total weight 880 kg. 1 part = 880 ÷ 11 = 80 kg. Batch 1 = 4 × 80 = 320 kg, Batch 2 = 7 × 80 = 560 kg. Difference = <b>240 kg</b> [M1 for division by 11, A1 for 240 kg]."),
        ("Mock 2 &bull; Section B (Calculator Permitted &bull; Part 1)",
         "<b>Q6. Fleet Driver Wages:</b> 10 drivers work 7.5 hrs at £11.44 = 10 × 7.5 × 11.44 = £858.00. 2 controllers work 8 hrs at £16.50 = 2 × 8 × 16.50 = £264.00. Total staffing = £858.00 + £264.00 = <b>£1,122.00</b> [P1 for subtotal, A1 for £1,122.00].<br>"
         "<b>Q7. Tarmac Resurfacing Area:</b> Base 12.4 m × 8.6 m = 106.64 m². Minus drainage island 3.0 m × 2.0 m = 6.0 m². Net tarmac = 100.64 m². Bag covers 1.8 m². Bags = 100.64 ÷ 1.8 = 55.91 → 56 bags. Total cost = 56 × £19.50 = <b>£1,092.00</b> [P1 for net area, P1 for rounding up, A1 for £1,092.00].<br>"
         "<b>Q8. Grouped Maintenance Times:</b> Midpoints: 10-19 min (14.5 × 8 = 116), 20-29 min (24.5 × 16 = 392), 30-39 min (34.5 × 22 = 759), 40-49 min (44.5 × 4 = 178). Total Total  fx = 1,445. N = 50. Estimated mean = 1,445 ÷ 50 = <b>28.9 minutes [M1 for midpoints, A1 for 28.9 mins].<br>"
         "<b>Q9. Van Route Fuel:</b> 210 miles at 38 mpg = 210 ÷ 38 = 5.526 gallons. Litres = 5.526 × 4.55 = 25.14 litres. At £1.52/litre = 25.14 × 1.52 = <b>£38.21</b> [P1 for gallon conversion, A1 for £38.21].<br>"
         "<b>Q10. Oil Drum Capacity:</b> r = 0.45 m, h = 0.95 m. V = 3.142 r² h = 3.142 × (0.45)² × 0.95 = 3.142 × 0.2025 × 0.95 = 0.6044 m³. Litres = 0.6044 × 1,000 = <b>604.4 litres [M1 for cylinder formula, A1 for 604.4 litres]."),
        ("Mock 2 &bull; Section B (Calculator Permitted &bull; Part 2)",
         "<b>Q11. Operating Margin:</b> Revenue = £20,400. Operating costs = £14,100. Operating profit = 20,400 - 14,100 = £6,300. Profit margin % = (6,300 ÷ 20,400) × 100 = <b>30.9%</b> [M1 for profit, P1 for division, A1 for 30.9%].<br>"
         "<b>Q12. Delivery Tracking Reliability:</b> GPS Sensor 1 reliability = 98% (0.98), Sensor 2 reliability = 95% (0.95). Both functional = 0.98 × 0.95 = <b>0.931</b> (or 93.1%) [P1 for independent product, A1 for 0.931].<br>"
         "<b>Q13. Distribution Speed &amp; Arrival:</b> Route = 140 miles at 42 mph. Time = 140 ÷ 42 = 3.333 hrs = 3 hrs 20 mins. Departure = 08:30. Arrival = 08:30 + 3h  20m = <b>11:50</b> [P1 for time conversion, A1 for 11:50].<br>"
         "<b>Q14. Warehouse Crane Cable:</b> Vertical rise a = 6.5 m, horizontal traverse b = 14.0 m. c = √(6.5² + 14.0²) = √(42.25 + 196.00) = √(238.25) = <b>15.44 m</b> [M1 for Pythagoras, A1 for 15.44 m].<br>"
         "<b>Q15. Pallet Supplier Comparison:</b> Supplier X: 500 pallets at £14.50 = £7,250 with 15% trade discount = 7,250 × 0.85 = £6,162.50 + £80 shipping = £6,242.50. Supplier Y: 500 pallets at £12.20 = £6,100 + £150 flat shipping = £6,250.00. Comparison: <b>Supplier X is cheaper by £7.50</b> [P1 for X net, P1 for Y net, A1 for Supplier X and £7.50 difference].")
    ],
    3: [
        ("Mock 3 &bull; Section A &amp; B Model Solutions",
         "<b>Section A Non-Calculator Summary:</b><br>"
         "&bull; Q1: Invoicing: 21 items at £18.10 + £23.30 delivery = 380.10 + 23.30 = <b>£403.40</b>.<br>"
         "&bull; Q2: Circular Plan: Radius 2.4 m. Area = 3.14 × 2.4² = 3.14 × 5.76 = <b>18.09 m²</b>.<br>"
         "&bull; Q3: Fractions: 2 1/4 + 1 2/3 = 9/4 + 5/3 = (27 + 20)/12 = 47/12 = <b>3 11/12</b>.<br>"
         "&bull; Q4: Reverse Discount: £405 at 16% discount = 405 ÷ 0.84 = <b>£482.14</b>.<br>"
         "&bull; Q5: Ratio Distribution: Ratio 2:3:5, total 10 parts of £1,500. One part = £150. Shares = £300, £450, £750.<br><br>"
         "<b>Section B Calculator Highlights:</b><br>"
         "&bull; Q6: Staffing wages = 11 staff × 8 hrs × £11.44 + 2 managers × 9 hrs × £16.50 = 1,006.72 + 297.00 = <b>£1,303.72</b>.<br>"
         "&bull; Q7: Commercial floor tiles = 145 tiles required at £4.20 = <b>£609.00</b>.<br>"
         "&bull; Q8: Estimated Mean from grouped data = <b>34.2 units</b>.<br>"
         "&bull; Q9: Fuel cost for 240 miles at 45 mpg and £1.45/litre = <b>£35.15</b>.<br>"
         "&bull; Q10: Cylindrical storage hopper volume = <b>18.85 m³ (18,850 litres).<br>"
         "&bull; Q11: Profit margin % on £21,600 revenue = <b>31.0%</b>.<br>"
         "&bull; Q12: Independent dual probability = <b>0.941</b>.<br>"
         "&bull; Q13: Delivery route arrival time = <b>14:22</b>.<br>"
         "&bull; Q14: Loading ramp diagonal hypotenuse = <b>5.38 m</b>.<br>"
         "&bull; Q15: Supplier procurement decision: <b>Supplier B saves £34.80</b>.")
    ],
    4: [
        ("Mock 4 &bull; Section A &amp; B Model Solutions",
         "<b>Section A Non-Calculator Summary:</b><br>"
         "&bull; Q1: Commercial invoice total: 24 × 19.30 + 22.80 = 463.20 + 22.80 = <b>£486.00</b>.<br>"
         "&bull; Q2: Circular reservoir base: r = 2.6 m, Area = 3.14 × 6.76 = <b>21.23 m²</b>.<br>"
         "&bull; Q3: Mixed numbers: 2 2/4 + 1 2/3 = 2 1/2 + 1 2/3 = <b>4 1/6</b>.<br>"
         "&bull; Q4: Reverse calculation: £420 after 18% reduction = 420 ÷ 0.82 = <b>£512.20</b>.<br>"
         "&bull; Q5: Concrete mortar ratio 1:2:4, total 7 parts of 1,400 kg. Cement = 200 kg, Sand = 400 kg, Aggregate = 800 kg.<br><br>"
         "<b>Section B Calculator Highlights:</b><br>"
         "&bull; Q6: Construction team wages: 12 operatives + 3 supervisors = <b>£1,532.16</b>.<br>"
         "&bull; Q7: Scaffold netting area net of window openings = 84.5 m². Cost = <b>£380.25</b>.<br>"
         "&bull; Q8: Estimated mean concrete setting time = <b>4.8 hours</b>.<br>"
         "&bull; Q9: Tipper truck fuel: 260 miles at 14 mpg = 18.57 gallons = 84.5 litres at £1.55 = <b>£130.98</b>.<br>"
         "&bull; Q10: Drainage culvert volume (pipe cylinder): V = 3.142 r² h = <b>7.85 m³</b>.<br>"
         "&bull; Q11: Operating contract margin: (7,200 ÷ 22,800) × 100 = <b>31.6%</b>.<br>"
         "&bull; Q12: Combined safety inspection pass rate: 0.96 × 0.98 = <b>0.9408</b>.<br>"
         "&bull; Q13: Haulage transit time: 170 miles at 40 mph = 4.25 hrs = 4 hrs 15 mins. Arrival = <b>17:15</b>.<br>"
         "&bull; Q14: Roof rafter diagonal length: √(2.4² + 6.8²) = √(5.76 + 46.24) = <b>7.21 m</b>.<br>"
         "&bull; Q15: Brick supplier evaluation: <b>Supplier A delivers saving of £56.00</b>.")
    ],
    5: [
        ("Mock 5 &bull; Section A &amp; B Model Solutions",
         "<b>Section A Non-Calculator Summary:</b><br>"
         "&bull; Q1: Clinical equipment order: 27 × 20.50 + 22.30 = 553.50 + 22.30 = <b>£575.80</b>.<br>"
         "&bull; Q2: Circular sterilization bay: r = 2.8 m, Area = 3.14 × 7.84 = <b>24.62 m²</b>.<br>"
         "&bull; Q3: Medical dosage fraction addition: 2 3/4 + 1 2/3 = <b>4 5/12</b>.<br>"
         "&bull; Q4: Reverse price indexing: £435 after 20% discount = 435 ÷ 0.80 = <b>£543.75</b>.<br>"
         "&bull; Q5: Disinfectant dilution ratio 1:9, total 10 parts for 50 litres. Concentrate = 5 L, Water = 45 L.<br><br>"
         "<b>Section B Calculator Highlights:</b><br>"
         "&bull; Q6: Healthcare auxiliary staffing: 13 nursing assistants + 2 ward leads = <b>£1,489.92</b>.<br>"
         "&bull; Q7: Antimicrobial flooring installation: Net 68.4 m², cost = <b>£1,231.20</b>.<br>"
         "&bull; Q8: Patient triage wait time estimated mean = <b>24.6 minutes</b>.<br>"
         "&bull; Q9: Medical courier transit fuel: 165 miles at 52 mpg = <b>£21.90</b>.<br>"
         "&bull; Q10: Oxygen cylinder capacity at pressure: V = <b>3.45 m³ (3,450 litres).<br>"
         "&bull; Q11: Clinical procurement operating margin = <b>32.1%</b>.<br>"
         "&bull; Q12: Dual diagnostic test accuracy: 0.99 × 0.97 = <b>0.9603 (96.03%).<br>"
         "&bull; Q13: Blood courier arrival time: 85 miles at 50 mph = 1 hr 42 mins. Arrival = <b>11:12</b>.<br>"
         "&bull; Q14: Access ramp incline length: √(0.8² + 9.6²) = <b>9.63 m</b>.<br>"
         "&bull; Q15: PPE Bulk Contract: <b>Supplier B provides net cost saving of £82.50</b>.")
    ],
    6: [
        ("Mock 6 &bull; Section A &amp; B Model Solutions",
         "<b>Section A Non-Calculator Summary:</b><br>"
         "&bull; Q1: Commercial catering supply: 30 × 21.70 + 21.80 = 651.00 + 21.80 = <b>£672.80</b>.<br>"
         "&bull; Q2: Circular dining banquet area: r = 3.0 m, Area = 3.14 × 9.0 = <b>28.26 m²</b>.<br>"
         "&bull; Q3: Fractional ingredient mixing: 2 1/4 + 1 2/3 = <b>3 11/12</b>.<br>"
         "&bull; Q4: Reverse commercial tariff: £450 after 22% deduction = 450 ÷ 0.78 = <b>£576.92</b>.<br>"
         "&bull; Q5: Banquet recipe scale ratio 3:5, scaling factor 4.5. New quantities = 13.5 kg and 22.5 kg.<br><br>"
         "<b>Section B Calculator Highlights:</b><br>"
         "&bull; Q6: Kitchen brigade payroll: 14 commis chefs + 2 sous chefs = <b>£1,624.40</b>.<br>"
         "&bull; Q7: Non-slip kitchen floor tiling: 54.2 m², cost = <b>£975.60</b>.<br>"
         "&bull; Q8: Estimated mean food preparation service time = <b>16.8 minutes</b>.<br>"
         "&bull; Q9: Refrigerated food delivery fuel: 195 miles at 34 mpg = <b>£38.92</b>.<br>"
         "&bull; Q10: Commercial water boiler tank volume: V = <b>0.85 m³ (850 litres).<br>"
         "&bull; Q11: Food &amp; Beverage gross profit margin = <b>68.4%</b>.<br>"
         "&bull; Q12: Temperature control compliance probability = <b>0.975</b>.<br>"
         "&bull; Q13: Event catering transport arrival time: 105 miles at 45 mph = 2 hrs 20 mins. Arrival = <b>16:05</b>.<br>"
         "&bull; Q14: Loading bay conveyor length: √(1.8² + 7.5²) = <b>7.71 m</b>.<br>"
         "&bull; Q15: Food wholesale contract evaluation: <b>Wholesaler A saves £114.00</b>.")
    ]
}


# =============================================================================
# 2. ENGLISH LEVEL 2 MOCK PACK REFERENCE DATA
# =============================================================================

ENGLISH_L2_GLOSSARY = [
    ("Alliteration", "Repetition of identical initial consonant sounds in consecutive words to create rhythm or emphasis."),
    ("Bias", "A one-sided inclination or perspective that prevents impartial consideration of an issue."),
    ("Call to Action", "A concluding directive urging the reader to take immediate, specific action."),
    ("Colloquial Language", "Informal conversational expressions used to establish familiarity with the reader."),
    ("Emotive Language", "Deliberate word choices designed to evoke strong feelings (sympathy, indignation, urgency) in the reader."),
    ("Hyperbole", "Intentional exaggeration used for rhetorical effect, emphasis, or humour."),
    ("Imperative Verb", "A command verb instructing the reader what to do (e.g. 'Register', 'Inspect', 'Submit')."),
    ("Juxtaposition", "Placing contrasting ideas, images, or arguments side by side to highlight differences."),
    ("Organizational Features", "Visual and structural tools including subheadings, bullet points, callout boxes, and bold text."),
    ("Passive Voice", "Grammatical construction where the object of an action becomes the subject, establishing an objective formal tone."),
    ("Rhetorical Question", "A question posed for persuasive effect where no verbal response is expected from the audience."),
    ("Rule of Three (Tricolon)", "Grouping three words, phrases, or arguments together to make them memorable and impactful."),
    ("Statistics & Evidence", "Factual data, numerical percentages, and survey findings cited to bolster credibility."),
    ("Tone", "The overall attitude or mood conveyed by the writer (e.g. authoritative, empathetic, critical, impassioned).")
]

ENGLISH_L2_INDEX = [
    ("A", [("Alliteration & sound devices", "4, 18"), ("Articles (workplace & community)", "2, 10, 22"), ("Audience & purpose analysis", "3, 12, 24")]),
    ("B", [("Bias detection & balanced reporting", "3, 8, 20"), ("Bullet points & formatting", "4, 14, 26")]),
    ("C", [("Call to action techniques", "4, 16"), ("Colloquial vs formal register", "3, 11, 23"), ("Comparative reading questions (Q6-9)", "9, 21, 33")]),
    ("D", [("Direct address ('You')", "4, 15"), ("Discursive essays & balance", "2, 12, 24")]),
    ("E", [("Emails (professional & formal)", "2, 10, 22"), ("Emotive language analysis", "3, 8, 20")]),
    ("F", [("Formal letters & layout conventions", "2, 10, 22"), ("Functional Skills Level 2 Criteria", "3-5")]),
    ("G", [("Glossary of linguistic techniques", "58"), ("Grade boundaries & scaling", "57")]),
    ("H", [("Headings & subheadings in reports", "4, 14, 26"), ("Hyperbole & emphasis", "4, 18")]),
    ("I", [("Imperative verbs in guidance leaflets", "4, 16, 28"), ("Implicit vs explicit meaning", "3, 7, 19")]),
    ("M", [("Mark schemes for Mocks 1-5", "59-78"), ("Model writing exemplars (Tasks 1 & 2)", "79-88")]),
    ("O", [("Organizational features identification", "3, 8, 20")]),
    ("P", [("Paragraph linking & cohesive devices", "4, 14, 26"), ("Persuasive rhetoric (AFOREST)", "4, 18, 30")]),
    ("R", [("Reading Section criteria & question types", "3"), ("Reports (formal workplace)", "2, 10, 22"), ("Rhetorical questions", "4, 18")]),
    ("S", [("SPaG marking rubrics & bands", "5"), ("Speeches & presentations", "2, 12, 24"), ("Synthesis of two texts", "9, 21, 33")]),
    ("T", [("Tone & register analysis", "3, 8, 20"), ("Topic sentences in essays", "4, 14")])
]

ENGLISH_L2_MOCK_SOLUTIONS = {
    1: [
        ("Mock 1 &bull; Reading Section Model Answers (Q1&ndash;Q9)",
         "<b>Q1. Fact vs Opinion in Text A:</b> Fact: <i>'Electric vans now account for 28% of our urban delivery fleet.'</i> (Verified verifiable statistic). Opinion: <i>'The transition has been an absolute triumph for driver morale.'</i> (Subjective value judgment).<br>"
         "<b>Q2. Implicit Meaning in Text A:</b> The phrase <i>'kicking the carbon can down the road'</i> implies that traditional courier companies are postponing necessary decarbonization measures and shifting the environmental burden to future generations without resolving systemic pollution.<br>"
         "<b>Q3. Organisational Features in Text A:</b> (1) Subheadings segment key discussion areas (e.g. Charging Infrastructure, Capital Expenditure). (2) Bullet points emphasize operational metrics clearly.<br>"
         "<b>Q4. Language Devices in Text B:</b> (1) Rhetorical question: <i>'Can small family hauliers realistically shoulder the cost of rapid electrification?'</i> (engages the reader and highlights financial strain). (2) Emotive adjective: <i>'crippling upfront battery costs'</i> (conveys severe economic pressure).<br>"
         "<b>Q5. Vocabulary in Context:</b> In paragraph 3 of Text B, <i>'prohibitive'</i> means excessively high or unaffordable, preventing hauliers from making capital investments.<br>"
         "<b>Q6. Author's Purpose in Text B:</b> To advocate for government transitional subsidies and protect independent transport businesses from rapid regulatory penalties.<br>"
         "<b>Q7. Synthesizing Text A and Text B:</b> While Text A celebrates the long-term operational savings and air quality benefits of electric fleets, Text B cautions that without public infrastructure funding, independent owner-drivers face bankruptcy.<br>"
         "<b>Q8. Comparing Ideas Across Both Texts:</b> Both texts acknowledge that charging network density is currently insufficient. Text A views depot rapid-chargers as the private solution, whereas Text B argues national public charging networks must be subsidized before mandates take effect.<br>"
         "<b>Q9. Critical Evaluation of Source Validity:</b> Text A provides verifiable fleet statistics from audited green logistics trials, whereas Text B relies heavily on anecdotal testimonies from individual hauliers, making Text A more empirically robust but Text B more representative of micro-business sentiment."),
        ("Mock 1 &bull; Writing Exemplar &bull; Task 1 (Formal Workplace Report)",
         "<b>Task 1 Benchmark Exemplar: Formal Recommendation Report</b><br>"
         "<b>To:</b> Board of Operations, GreenRoute Logistics<br>"
         "<b>From:</b> Abdul, Senior Logistics Analyst<br>"
         "<b>Date:</b> 14 October 2026<br>"
         "<b>Subject:</b> Fleet Electrification Feasibility Assessment &amp; Infrastructure Roadmap<br><br>"
         "<b>1. Executive Summary</b><br>"
         "This report evaluates the operational and commercial viability of transitioning our regional delivery fleet of 45 diesel vans to battery electric vehicles (BEVs) over a 24-month horizon. While initial capital expenditure is substantial, projected fuel and maintenance savings yield a break-even point at 38 months.<br><br>"
         "<b>2. Key Operational Findings</b><br>"
         "Analysis of urban distribution routes indicates average daily mileage of 82 miles, well within the 160-mile range of commercial BEVs. Furthermore, telematics data reveals that our depot dwell times (19:00 to 05:30) provide ideal low-tariff overnight charging windows.<br><br>"
         "<b>3. Risk Analysis &amp; Mitigation</b><br>"
         "Grid supply capacity at the Birmingham hub requires a 100 kVA substation upgrade (&pound;18,500). To mitigate downtime risks, a phased rollout of 15 vans per quarter is strongly advised alongside dual-socket 22 kW AC depot chargers.<br><br>"
         "<b>4. Strategic Recommendations</b><br>"
         "&bull; Secure government Workplace Charging Scheme grants prior to procurement.<br>"
         "&bull; Pilot 5 electric vans on inner-city routes starting Q1 2027.<br>"
         "&bull; Implement mandatory eco-driving and regenerative braking training for all delivery operatives."),
        ("Mock 1 &bull; Writing Exemplar &bull; Task 2 (Persuasive Public Article)",
         "<b>Task 2 Benchmark Exemplar: Community Newspaper Article</b><br>"
         "<b>Title: Charging Ahead: Why Our High Street Must Welcome Clean Transport</b><br>"
         "<b>Byline:</b> Local Business Correspondent<br><br>"
         "Picture this: a bustling Saturday afternoon where shoppers breathe crisp, fresh air instead of diesel particulates. Sound like an impossible utopia? In reality, sustainable urban transport is already transforming towns across Britain.<br><br>"
         "For decades, high street retailers have feared pedestrianization and clean air zones, worrying that delivery restrictions would choke trade. Yet evidence reveals the opposite: footfall increases by up to 16% in clean, quiet town centres. Customers linger longer in outdoor cafes when they are not subjected to idling delivery trucks.<br><br>"
         "Critics argue that small businesses cannot adapt. However, regional delivery co-operatives and electric cargo bike hubs have demonstrated that low-emission logistics are not only affordable but significantly faster through congested urban corridors.<br><br>"
         "The time for procrastination has passed. Local council leaders and business owners must unite to install shared fast-chargers and loading bays. Let us build a town centre that champions health, commerce, and future generations.")
    ],
    2: [
        ("Mock 2 &bull; Reading Section Model Answers (Q1&ndash;Q9)",
         "<b>Q1. Fact vs Opinion in Text A:</b> Fact: <i>'Over 4.4 million UK workers currently operate on hybrid schedules.'</i> (Empirical labor force survey datum). Opinion: <i>'Remote working has permanently destroyed spontaneous workplace innovation.'</i> (Unverified subjective viewpoint).<br>"
         "<b>Q2. Implicit Meaning in Text A:</b> The metaphor <i>'presenteeism in digital disguise'</i> implies that employees feel pressured to remain permanently visible online and answer emails after hours, creating an illusion of output rather than authentic productivity.<br>"
         "<b>Q3. Structural Features in Text A:</b> Clear numbered section headings, bold key terms for cognitive anchoring, and a concluding executive bullet-point summary.<br>"
         "<b>Q4. Persuasive Language in Text B:</b> (1) Triadic listing: <i>'flexibility, autonomy, and work-life balance'</i>. (2) High-modality modal verbs: <i>'employers must adapt or they will inevitably bleed top talent'</i>.<br>"
         "<b>Q5. Vocabulary in Context:</b> In paragraph 2 of Text B, <i>'retention'</i> denotes the capacity of a company to keep its employees and prevent them from resigning.<br>"
         "<b>Q6. The Writer's Purpose in Text B:</b> To persuade corporate leadership that offering agile working models is an indispensable recruitment strategy in competitive industries.<br>"
         "<b>Q7. Cross-Text Synthesis:</b> Text A emphasizes supervisory oversight and collaborative cohesion in office environments, whereas Text B prioritizes personal autonomy and mental wellbeing achieved through remote flexibility.<br>"
         "<b>Q8. Comparing Workplace Values:</b> Both texts concede that organizational trust is foundational. Text A posits that trust is reinforced through structured face-to-face mentorship, while Text B insists trust is proven by measuring task deliverables rather than desk hours.<br>"
         "<b>Q9. Evaluating Evidentiary Weight:</b> Text A draws upon multi-industry performance benchmarks and human resources audit metrics, giving it high evidential validity, whereas Text B leverages subjective employee sentiment polls."),
        ("Mock 2 &bull; Writing Exemplar &bull; Task 1 (Formal Workplace Policy Report)",
         "<b>Task 1 Benchmark Exemplar: Formal Hybrid Working Policy Report</b><br>"
         "<b>To:</b> Executive Management Board, Apex Global Enterprises<br>"
         "<b>From:</b> Abdul, Lead HR Strategy Consultant<br>"
         "<b>Date:</b> 18 October 2026<br>"
         "<b>Subject:</b> Enterprise Hybrid Working Framework &amp; Core Productivity Standards<br><br>"
         "<b>1. Purpose &amp; Scope</b><br>"
         "This policy document establishes standardized operational guidelines for hybrid working across all divisional departments, balancing individual autonomy with organizational performance.<br><br>"
         "<b>2. Proposed Core Attendance Model</b><br>"
         "Departmental teams will adopt a '3/2' agile structure: three days in office (including mandatory collaboration Tuesdays and Thursdays) and two days remote. Core collaboration hours are set between 10:00 and 15:00.<br><br>"
         "<b>3. Technology &amp; Ergonomic Compliance</b><br>"
         "Every remote employee must complete a DSE ergonomic workstation assessment. Apex will provide dual-screen monitors, encrypted VPN hardware keys, and noise-cancelling headsets to guarantee GDPR compliance.<br><br>"
         "<b>4. Accountability &amp; Output Metrics</b><br>"
         "Performance will be appraised through quarterly objective key results (OKRs) and project milestone completions rather than keystroke monitoring software.<br><br>"
         "<b>5. Recommendations for Implementation</b><br>"
         "&bull; Launch 60-day departmental trial starting November 2026.<br>"
         "&bull; Deliver line-manager workshops on asynchronous team leadership.<br>"
         "&bull; Review sickness absence and productivity indices after 6 months."),
        ("Mock 2 &bull; Writing Exemplar &bull; Task 2 (Persuasive Speech to Staff Forum)",
         "<b>Task 2 Benchmark Exemplar: Staff Forum Persuasive Speech</b><br>"
         "<b>Title: Embracing Agile Collaboration: Why Our Culture Thrives on Flexibility</b><br>"
         "<b>Delivered by:</b> Staff Employee Representative<br><br>"
         "Good morning colleagues and members of the leadership team.<br><br>"
         "We stand at a defining crossroads in our company's history. Behind us lies the rigid, outdated five-day office grind; ahead lies the opportunity to forge an agile, trust-based working culture where everyone can excel.<br><br>"
         "Let me be unequivocally clear: hybrid working is not about working less. It is about working smarter. When we eliminate the exhausting two-hour daily commute, we gain focus, renewed energy, and precious time with our families. We return to the office on team days energized, creative, and ready to collaborate.<br><br>"
         "Some voice concerns that team spirit will dissipate. But culture is built on mutual respect and shared objectives, not on sitting at adjacent desks wearing headphones in silence! By establishing structured in-person brainstorming sessions alongside dedicated remote focus days, we achieve the best of both worlds.<br><br>"
         "Let us champion this policy with professional accountability. Let us prove that autonomy drives excellence. Thank you.")
    ],
    3: [
        ("Mock 3 &bull; Reading Section Model Answers (Q1&ndash;Q9)",
         "<b>Q1. Fact vs Opinion in Text A:</b> Fact: <i>'Degree apprenticeships combine full-time salaried employment with debt-free university study.'</i> (Factual definition). Opinion: <i>'Traditional university degrees are obsolete relics of an elitist education system.'</i> (Polemical opinion).<br>"
         "<b>Q2. Implicit Meaning in Text A:</b> The phrase <i>'golden handcuffs of entry-level debt'</i> suggests that graduates are financially constrained for decades by student loan repayments, limiting their career and home-ownership prospects.<br>"
         "<b>Q3. Visual &amp; Typographical Features in Text A:</b> Callout case-study panels, bold comparative salary statistics, and clear tabular breakdowns of tuition fees.<br>"
         "<b>Q4. Language Devices in Text B:</b> (1) Metaphor: <i>'an intellectual incubator where critical minds are forged'</i>. (2) Alliteration: <i>'broadening horizons through borderless debate'</i>.<br>"
         "<b>Q5. Vocabulary in Context:</b> In paragraph 4 of Text B, <i>'versatility'</i> indicates the capacity to adapt across diverse intellectual disciplines and career trajectories.<br>"
         "<b>Q6. Writer's Purpose in Text B:</b> To defend the enduring academic, civic, and philosophical value of traditional campus-based degree education against purely vocational metrics.<br>"
         "<b>Q7. Synthesizing Educational Pathways:</b> Both texts emphasize that modern industry demands adaptable problem solvers. Text A argues that vocational apprenticeship embedding provides superior day-one readiness, while Text B maintains that academic theory fosters deeper analytical rigor.<br>"
         "<b>Q8. Comparison of Financial Arguments:</b> Text A presents compelling evidence that apprenticeship candidates graduate with &pound;0 debt and &pound;80,000 in accumulated earnings, whereas Text B contends that long-term graduate lifetime earnings still justify initial borrowing.<br>"
         "<b>Q9. Evaluating Tone and Credibility:</b> Text A maintains an objective, informational tone supported by Institute for Apprenticeships data, whereas Text B adopts an impassioned academic defense that borders on nostalgic rhetoric."),
        ("Mock 3 &bull; Writing Exemplar &bull; Task 1 (Formal Article for a National Careers Publication)",
         "<b>Task 1 Benchmark Exemplar: Careers Feature Article</b><br>"
         "<b>Title: Degree Apprenticeship or Traditional Campus? Navigating Modern Career Gateways</b><br>"
         "<b>Byline:</b> Abdul, Lead Vocational Education Specialist<br><br>"
         "For generations of school leavers, the path to professional success followed an unchanging script: finish Sixth Form, secure university admission, and graduate into the corporate world. Today, skyrocketing tuition fees and the rapid rise of Degree Apprenticeships have fundamentally disrupted that conventional narrative.<br><br>"
         "<b>The Apprenticeship Advantage: Earn While You Learn</b><br>"
         "Degree apprenticeships offer an undeniable financial proposition: zero tuition debt, a full employee salary from day one, and immediate immersion in corporate culture. In fields like software engineering, quantity surveying, and digital marketing, candidates accumulate four years of workplace experience while simultaneously earning a BSc or BEng.<br><br>"
         "<b>The Campus Experience: Intellectual Autonomy</b><br>"
         "Conversely, the traditional university journey fosters independent critical inquiry, cultural exploration, and networking beyond the constraints of a single employer's commercial remit. For careers in medicine, law, or academic research, the conventional degree remains essential.<br><br>"
         "<b>Verdict for the Modern Learner</b><br>"
         "Prospective candidates must audit their learning preferences. Those who thrive under practical mentorship and structured accountability should pursue apprenticeships; those seeking broad exploratory academic growth will find campus life irreplaceable."),
        ("Mock 3 &bull; Writing Exemplar &bull; Task 2 (Persuasive Email to Chamber of Commerce)",
         "<b>Task 2 Benchmark Exemplar: Business Consultation Email</b><br>"
         "<b>To:</b> chairperson@regionalchamber.org.uk<br>"
         "<b>From:</b> abdul.skills@workforcedevelopment.co.uk<br>"
         "<b>Date:</b> 21 October 2026<br>"
         "<b>Subject:</b> Urgent Proposal: Expanding SME Apprenticeship Consortium Grants<br><br>"
         "Dear Madam Chairperson,<br><br>"
         "I am writing on behalf of regional training providers to urge the Chamber of Commerce to spearhead an Apprenticeship Levy Transfer Consortium for local small and medium-sized enterprises (SMEs).<br><br>"
         "As our local business community grapples with severe technical skills shortages, over &pound;4.2 million in unspent Levy funds from large regional corporations continues to expire and return to the Treasury unutilized each year. By establishing an agile Chamber-led transfer hub, we can redirect these funds to cover 100% of training costs for 250 local SME apprentices across engineering, logistics, and digital services.<br><br>"
         "This initiative will provide three immediate regional dividends:<br>"
         "1. Close critical technician and engineering vacancies without capital cost to small firms.<br>"
         "2. Create high-value, salaried career pathways for school leavers from disadvantaged postcodes.<br>"
         "3. Retain top young talent within our regional economy.<br><br>"
         "I would welcome the opportunity to present a 15-minute briefing paper at the upcoming Executive Committee meeting on 5 November. Thank you for your leadership on regional economic growth.<br><br>"
         "Yours sincerely,<br><br>"
         "Abdul<br>"
         "Lead Vocational Workforce Consultant")
    ],
    4: [
        ("Mock 4 &bull; Reading Section Model Answers (Q1&ndash;Q9)",
         "<b>Q1. Fact vs Opinion in Text A:</b> Fact: <i>'Generative AI tools processed over 1.2 billion administrative queries in UK financial firms last year.'</i> (Quantifiable empirical metric). Opinion: <i>'Automation will eradicate all junior professional roles within five years.'</i> (Speculative prediction).<br>"
         "<b>Q2. Implicit Meaning in Text A:</b> The phrase <i>'algorithmic safety nets'</i> implies automated systems designed to intercept human errors before regulatory disclosures occur.<br>"
         "<b>Q3. Organisational Features in Text A:</b> Infographic workflow diagrams, bold technical nomenclature, and boxed compliance callouts.<br>"
         "<b>Q4. Language Devices in Text B:</b> (1) Emotive metaphor: <i>'surrendering our human intuition to black-box decision making'</i>. (2) Rhetorical antithesis: <i>'fast but flawed, efficient yet devoid of empathy'</i>.<br>"
         "<b>Q5. Vocabulary in Context:</b> In paragraph 2 of Text B, <i>'hallucination'</i> refers to an AI model producing plausible but entirely fabricated and inaccurate information.<br>"
         "<b>Q6. The Writer's Purpose in Text B:</b> To alert corporate governance teams to the ethical, legal, and copyright liabilities inherent in unchecked automated software integration.<br>"
         "<b>Q7. Synthesizing AI Integration Perspectives:</b> Text A focuses on exponential productivity leaps and repetitive task reduction, while Text B highlights risk mitigation, data privacy vulnerabilities, and the preservation of human critical thinking.<br>"
         "<b>Q8. Comparison of Regulatory Approaches:</b> Both authors concur that internal governance frameworks must be established. Text A advocates for agile vendor auditing, while Text B insists on mandatory human-in-the-loop sign-off protocols.<br>"
         "<b>Q9. Critical Evaluation of Source Validity:</b> Text A provides verifiable industry survey data from chartered accountants, whereas Text B relies on philosophical and ethical essays, making Text A superior for commercial planning but Text B vital for risk ethics."),
        ("Mock 4 &bull; Writing Exemplar &bull; Task 1 (Formal Contribution to a Government Consultation Review)",
         "<b>Task 1 Benchmark Exemplar: Government Consultation Submission</b><br>"
         "<b>To:</b> Parliamentary Select Committee on Science, Innovation and Technology<br>"
         "<b>From:</b> Abdul, Senior Digital Ethics &amp; Functional Skills Lead<br>"
         "<b>Date:</b> 25 October 2026<br>"
         "<b>Subject:</b> Written Evidence: AI Integration Standards in Vocational &amp; Enterprise Education<br><br>"
         "<b>1. Introduction &amp; Terms of Reference</b><br>"
         "This evidence submission addresses the urgent need to embed AI literacy and critical validation frameworks within the statutory national curriculum for adult and vocational education.<br><br>"
         "<b>2. Workplace Vulnerabilities &amp; The Skills Gap</b><br>"
         "While modern business software rapidly incorporates automated synthesis, frontline workers lack formal instruction in prompt engineering, data privacy, and output verification. Inadvertent disclosure of personal client data into public cloud models represents a catastrophic GDPR compliance vulnerability.<br><br>"
         "<b>3. The Critical Verification Protocol (CVP)</b><br>"
         "We recommend mandating the 3-step 'Critical Verification Protocol' across all accredited vocational training:<br>"
         "&bull; <i>Source Origin Verification:</i> Requiring human tracing of algorithmic outputs to primary authoritative records.<br>"
         "&bull; <i>Bias &amp; Hallucination Audit:</i> Cross-referencing numerical claims against certified national statistics.<br>"
         "&bull; <i>Ethical Attribution:</i> Transparent disclosure of automated drafting assistance in commercial documents.<br><br>"
         "<b>4. Conclusion &amp; Policy Recommendations</b><br>"
         "The UK can lead responsible technological adoption by establishing funded Level 2 and Level 3 Digital Safety modules within adult education budgets."),
        ("Mock 4 &bull; Writing Exemplar &bull; Task 2 (Informative Staff Guide / Review)",
         "<b>Task 2 Benchmark Exemplar: Internal Staff Guidance Article</b><br>"
         "<b>Title: Working Alongside AI: 5 Golden Rules for Daily Productivity &amp; Security</b><br>"
         "<b>Published in:</b> Enterprise Operations Monthly Newsletter<br><br>"
         "Artificial Intelligence is no longer sci-fi theory; it is embedded in the word processors, spreadsheets, and email clients we use daily. When harnessed strategically, these tools liberate us from repetitive drudgery. However, cutting corners can lead to costly blunders.<br><br>"
         "Here are the five mandatory golden rules every team member must adhere to:<br><br>"
         "<b>1. Never Paste Confidential Client Data into Public Tools</b><br>"
         "Any information uploaded to public web models enters the vendor's training corpus. Always use our corporate enterprise-licensed, closed-circuit software.<br><br>"
         "<b>2. You Are Legally Responsible for Every Word You Send</b><br>"
         "Saying 'the AI generated that error' is not a valid defense before our clients or regulators. Every summary, calculation, and document requires thorough human proofreading.<br><br>"
         "<b>3. Beware the Plausible Hallucination</b><br>"
         "Language models excel at generating fluent prose, but they can invent citations, case law, and statistics with convincing authority. Verify every datum independently.<br><br>"
         "<b>4. Treat Algorithms as Junior Assistants, Not Senior Directors</b><br>"
         "Use tools to generate outlines, brainstorm email drafts, or format raw data. Reserve strategic judgment, empathy, and final decisions for human expertise.<br><br>"
         "<b>5. Continually Upgrade Your Prompting Skills</b><br>"
         "Clear context yields precise answers. Attend our weekly Wednesday lunchtime digital skills drop-in workshops to master advanced prompt syntax!")
    ],
    5: [
        ("Mock 5 &bull; Reading Section Model Answers (Q1&ndash;Q9)",
         "<b>Q1. Fact vs Opinion in Text A:</b> Fact: <i>'Over 18,000 residents utilize local green recreational corridors weekly.'</i> (Empirical council footfall tally). Opinion: <i>'Converting wild parkland into leisure complexes is a heartless betrayal of community heritage.'</i> (Subjective moral judgment).<br>"
         "<b>Q2. Implicit Meaning in Text A:</b> The phrase <i>'concrete creep'</i> implies gradual, insidious urban encroachment that permanently destroys biodiverse habitats without explicit public consultation.<br>"
         "<b>Q3. Structural Features in Text A:</b> Quotation pull-quotes, bulleted biodiversity statistics, and a highlighted petition signature counter.<br>"
         "<b>Q4. Language Devices in Text B:</b> (1) Emotive appeal to civic pride: <i>'rejuvenating our forgotten industrial riverside into a thriving beacon of prosperity'</i>. (2) Contrast: <i>'derelict wasteland transformed into state-of-the-art facilities'</i>.<br>"
         "<b>Q5. Vocabulary in Context:</b> In paragraph 3 of Text B, <i>'regeneration'</i> denotes the economic and social revitalization of an urban area through capital development.<br>"
         "<b>Q6. Author's Purpose in Text B:</b> To persuade local council planning officers and business owners to approve commercial development by accentuating economic dividends.<br>"
         "<b>Q7. Synthesizing Environmental &amp; Commercial Priorities:</b> Text A champions ecological preservation, public health, and free access to open nature, whereas Text B prioritizes job creation, municipal tax revenue, and modern indoor leisure facilities.<br>"
         "<b>Q8. Comparison of Community Value:</b> Both texts claim to advocate for community wellbeing. Text A defines wellbeing as clean air, native trees, and tranquil walking spaces; Text B defines wellbeing as modern leisure centers, youth sports facilities, and employment opportunities.<br>"
         "<b>Q9. Critical Evaluation of Source Validity:</b> Text A includes certified botanical and ornithological survey data, establishing strong scientific credibility, whereas Text B relies heavily on developer promotional forecasts."),
        ("Mock 5 &bull; Writing Exemplar &bull; Task 1 (Formal Proposal Letter to National Lottery Community Fund)",
         "<b>Task 1 Benchmark Exemplar: Grant Funding Proposal Letter</b><br>"
         "<b>The Grant Assessment Committee</b><br>"
         "National Lottery Community Fund<br>"
         "100 Wharf Road, London, SE1 7NN<br><br>"
         "<b>From:</b> Abdul, Project Director, GreenCorridor Community Trust<br>"
         "<b>Date:</b> 28 October 2026<br>"
         "<b>Subject:</b> Grant Application: Riverside Wildlife &amp; Wellbeing Community Trail (&pound;48,500)<br><br>"
         "Dear Members of the Committee,<br><br>"
         "On behalf of the GreenCorridor Community Trust, I am proud to submit our funding proposal to establish the Riverside Wildlife &amp; Wellbeing Community Trail, transforming 3.5 kilometres of neglected riverbank into an accessible, biodiverse green haven for 25,000 local residents.<br><br>"
         "<b>1. Community Need &amp; Social Cohesion</b><br>"
         "Our ward ranks within the top 15% most deprived urban areas nationally for accessible green space. Over 40% of local families live in flats without private gardens. This project directly addresses post-pandemic social isolation and pediatric physical inactivity by creating an inclusive space for all ages.<br><br>"
         "<b>2. Proposed Capital Works &amp; Accessibility</b><br>"
         "The requested &pound;48,500 grant will fund:<br>"
         "&bull; <b>Accessible All-Weather Pathway:</b> Installing recycled permeable gravel pathways suitable for wheelchairs, mobility scooters, and prams (&pound;22,000).<br>"
         "&bull; <b>Sensory Community Garden &amp; Seating:</b> Designing native flower meadows, raised herb planters, and timber benches (&pound;16,500).<br>"
         "&bull; <b>Educational Signage &amp; Youth Wildlife Club:</b> Installing Braille-enabled interactive wildlife boards and funding 12 weekend nature workshops (&pound;10,000).<br><br>"
         "<b>3. Project Sustainability &amp; Volunteer Legacy</b><br>"
         "Over 65 local volunteers have pledged ongoing maintenance support, partnered with the local vocational college horticultural department. We enclose our detailed financial audit, risk assessments, and council planning letters for your review.<br><br>"
         "Thank you for considering our application to create a lasting green legacy.<br><br>"
         "Yours sincerely,<br><br>"
         "Abdul<br>"
         "Project Director, GreenCorridor Community Trust"),
        ("Mock 5 &bull; Writing Exemplar &bull; Task 2 (Inspiring Local Newspaper Article / Volunteer Appeal)",
         "<b>Task 2 Benchmark Exemplar: Local Gazette Feature Article</b><br>"
         "<b>Title: Reclaiming Our Riverbank: Join the Green Revolution on Your Doorstep!</b><br>"
         "<b>Byline:</b> Community Action Champion<br><br>"
         "Take a stroll down to the Old Mill Bridge this morning. What do you see? For years, the answer was heart-breaking: rusted shopping trolleys, discarded plastic bottles, and overgrown brambles choking what should be the crown jewel of our town.<br><br>"
         "Now, close your eyes and imagine something extraordinary: Kingfishers darting across clear water, children learning to identify bumblebees in wildflower meadows, and grandparents enjoying a peaceful, smooth stroll along an accessible sunlit boardwalk.<br><br>"
         "That vibrant dream is becoming reality—and YOU hold the power to make it happen!<br><br>"
         "This Saturday, 1 November, the Riverside Trust is hosting our Great Autumn Community Action Day. Armed with garden rakes, planting trowels, and sheer community pride, over 100 neighbors of all ages will unite to plant 500 native trees and clear historical litter from the riverbank.<br><br>"
         "No gardening expertise is necessary. Whether you can dig planting holes for an hour, serve hot tea and soup, or build hedgehog shelters with our youth club, every single pair of hands matters. Free gloves, high-vis vests, and refreshments are provided.<br><br>"
         "Let us refuse to leave our town's environment to chance. Meet us at Old Mill Wharf at 09:30 AM this Saturday. Let us plant the seeds of a greener, healthier community together!")
    ],
    6: [
        ("Mock 6 &bull; Reading Section Model Answers (Q1&ndash;Q9)",
         "<b>Q1. Fact vs Opinion in Text A:</b> Fact: <i>'Specialist geriatric bed capacity decreased by 14% over the preceding decade.'</i> (Audited NHS statistical record). Opinion: <i>'Decentralized community care is an unmitigated disaster created purely to cut funding.'</i> (Subjective polemical claim).<br>"
         "<b>Q2. Implicit Meaning in Text A:</b> The phrase <i>'bed-blocking through bureaucratic paralysis'</i> implies that vulnerable patients remain stranded in hospital wards not due to clinical illness, but because social care assessment paperwork is hopelessly delayed.<br>"
         "<b>Q3. Organisational Features in Text A:</b> Analytical bar charts comparing hospital stay durations, authoritative clinical footnotes, and clear institutional subheadings.<br>"
         "<b>Q4. Language Devices in Text B:</b> (1) Emotive anecdote: <i>'an 84-year-old widow clutching her teacup, thriving among her beloved garden memories'</i>. (2) High-modality vocabulary: <i>'dignity, autonomy, and familiar comfort'</i>.<br>"
         "<b>Q5. Vocabulary in Context:</b> In paragraph 3 of Text B, <i>'domiciliary'</i> refers to medical or supportive care delivered directly inside a patient's private home rather than a hospital.<br>"
         "<b>Q6. Author's Purpose in Text B:</b> To advocate for massive investment into professional home-care packages as the most humane, clinically effective, and cost-efficient care delivery model.<br>"
         "<b>Q7. Synthesizing Healthcare Reform Proposals:</b> Text A focuses on secondary care hospital bottlenecks, clinical bed management, and emergency ward pressures, while Text B provides the long-term solution: robust community-based social care that prevents hospital admissions altogether.<br>"
         "<b>Q8. Comparison of Fiscal Metrics:</b> Both authors recognize the current model is fiscally unsustainable. Text A demonstrates that an acute NHS bed costs &pound;480 per night, whereas Text B proves that equivalent comprehensive home-care support costs less than &pound;95 per day.<br>"
         "<b>Q9. Critical Evaluation of Source Validity:</b> Text A draws upon peer-reviewed clinical audit data from the British Medical Journal, ensuring highest empirical validity, whereas Text B offers inspiring qualitative case studies that capture patient dignity powerfully."),
        ("Mock 6 &bull; Writing Exemplar &bull; Task 1 (Formal Briefing Memo to Hospital Management Board)",
         "<b>Task 1 Benchmark Exemplar: Executive Healthcare Memo</b><br>"
         "<b>MEMORANDUM</b><br>"
         "<b>To:</b> Chief Executive &amp; Management Board, St Jude's NHS Healthcare Trust<br>"
         "<b>From:</b> Abdul, Clinical Operations Integration Manager<br>"
         "<b>Date:</b> 30 October 2026<br>"
         "<b>Subject:</b> Urgent Operational Strategy: Mitigating Delayed Discharge Through Hospital-to-Home Pathways<br><br>"
         "<b>1. Purpose of Briefing</b><br>"
         "This memorandum outlines immediate operational interventions to address delayed transfers of care (DTOC), which currently account for 18.4% of non-elective bed occupancy across acute wards.<br><br>"
         "<b>2. Current Capacity Crisis &amp; Bottlenecks</b><br>"
         "Over 62 medically optimized patients remain stranded in acute beds due to delays in securing adult social care assessments and medication delivery. This logjam creates severe emergency department ambulance handover delays (averaging 74 minutes).<br><br>"
         "<b>3. The 'Discharge to Assess' (D2A) Action Model</b><br>"
         "We propose implementing an integrated 4-tier Discharge to Assess protocol:<br>"
         "&bull; <i>Dedicated Trust Transport Fleet:</i> Guaranteeing same-day morning patient transfers with essential 48-hour medication packs.<br>"
         "&bull; <i>Co-Located Social Workers:</i> Embedding council social work coordinators directly on ward rounds at 08:30 daily.<br>"
         "&bull; <i>Rapid Community Response Team:</i> Conducting occupational therapy home visits within 4 hours of patient arrival.<br><br>"
         "<b>4. Financial &amp; Clinical Impact</b><br>"
         "Repurposing &pound;120,000 from temporary agency nursing into dedicated community bridge-carers will release 42 acute beds daily, saving &pound;640,000 in bed-day penalties within six months.<br><br>"
         "<b>5. Next Steps</b><br>"
         "Board authorization is requested to launch the D2A pathway across Wards 4, 7, and 9 effective Monday 10 November 2026."),
        ("Mock 6 &bull; Writing Exemplar &bull; Task 2 (Persuasive Opinion Article for Local Newspaper)",
         "<b>Task 2 Benchmark Exemplar: Regional Opinion Article</b><br>"
         "<b>Title: Caring for Our Elders: Why Home, Not Hospital, is Where Healing Happens</b><br>"
         "<b>Byline:</b> Health &amp; Society Columnist<br><br>"
         "Imagine spending six weeks trapped in a sterile, fluorescent-lit hospital ward. You are clinically recovered, yet the exit door remains firmly shut because nobody has arrived to assess your front doorstep for a wooden ramp.<br><br>"
         "This is not a dramatic fiction; it is the daily reality for hundreds of vulnerable pensioners across our county. Our hospitals are remarkable at saving lives in acute crises. But a noisy, impersonal ward is the worst possible place for an elderly patient to regain independence.<br><br>"
         "In a hospital bed, elderly muscles atrophy. Within ten days of bed rest, an older adult can lose up to 10% of muscle mass. Confusion and delirium spike. Yet back in their own armchair, surrounded by familiar tea mugs, family photos, and the radio playing softly, recovery accelerates dramatically.<br><br>"
         "Why then do we continue to pump millions into acute beds while starving community home-carers of fair wages and travel allowances? It defies both common humanity and economic sense.<br><br>"
         "Let us demand that our regional health commissioners redirect resources where they belong: into well-paid, highly respected domiciliary carers. Our parents and grandparents spent their lifetimes building our community. The very least they deserve is the dignity of growing old in the comfort of their own homes.")
    ]
}

DIGITAL_SKILLS_SOLUTIONS = {
    "units": [
        ("Unit 1 &bull; Device Setup &amp; Safety Drill",
         "<b>Step 1 (Workstation Ergonomics):</b> Position screen 50-70 cm from eyes at eye level. Adjust chair height so elbows rest at 90 degrees.<br>"
         "<b>Step 2 (Peripheral Cable Management):</b> Route cables through desk grommets; avoid trip hazards.<br>"
         "<b>Knowledge Check:</b> Minimum strong password length recommended by UK NCSC is <b>12-16 characters</b> (three random words method)."),
        ("Unit 2 &bull; File Management &amp; Hierarchy Drill",
         "<b>Folder Architecture:</b> <code>Company_Drive / 2026_Operations / Logistics / Invoices / 2026-10-14_Invoice_Apex.pdf</code>.<br>"
         "<b>Naming Convention Rule:</b> Use ISO date format <code>YYYY-MM-DD</code> followed by descriptive project name; never use spaces or special characters (#, %, &amp;)."),
        ("Unit 3 &bull; Digital Information &amp; Search Drill",
         "<b>Search Operators:</b> Use quotation marks for exact phrase (<code>&quot;fleet electrification case study&quot;</code>), minus sign to exclude (<code>-hybrid</code>), and <code>filetype:pdf</code> for technical reports.<br>"
         "<b>Evaluating Reliability:</b> Check author credentials, publication date, domain authority (.gov.uk, .ac.uk), and cross-reference corroborating sources."),
        ("Unit 4 &bull; Spreadsheet Formulas &amp; Functions Drill",
         "<b>Formulas:</b><br>"
         "&bull; Total Revenue: <code>=SUM(C2:C15)</code><br>"
         "&bull; Average Order Value: <code>=AVERAGE(D2:D15)</code><br>"
         "&bull; Bonus Threshold: <code>=IF(E2&gt;10000, E2*0.05, 0)</code><br>"
         "&bull; VAT Calculation: <code>=F2*B1</code> (where B1 holds 0.20)."),
        ("Unit 5 &bull; Professional Workplace Email Drill",
         "<b>Email Layout:</b> Clear subject line (<code>Project Update: Q3 Audit Report Complete</code>), formal salutation (<code>Dear Ms Henderson,</code>), concise three-paragraph body, attachment confirmation, polite sign-off (<code>Kind regards, Abdul</code>)."),
        ("Unit 6 &bull; Cloud Collaboration &amp; Permissions Drill",
         "<b>Sharing Tiers:</b> Assign <b>'Viewer'</b> for external clients, <b>'Commenter'</b> for review committees, and <b>'Editor'</b> strictly to assigned document authors. Enable link expiration after 14 days."),
        ("Unit 7 &bull; Cybersecurity &amp; Phishing Drill",
         "<b>Phishing Red Flags:</b> Mismatched sender domain (e.g. <code>@support-paypal-update.com</code> instead of official domain), artificial urgency (<i>'Account suspended within 2 hours!'</i>), generic greeting, and suspicious hyperlink target."),
        ("Unit 8 &bull; Online Safety &amp; GDPR Compliance Drill",
         "<b>GDPR Rules:</b> Obtain explicit consent before data capture, store personal identifiable information (PII) on encrypted servers, delete records once operational purpose expires, and report data breaches within 72 hours."),
        ("Unit 9 &bull; Video Conferencing &amp; Virtual Meetings Drill",
         "<b>Meeting Protocol:</b> Test microphone and webcam prior to joining, mute microphone when not speaking to eliminate background noise, use blurred or neutral background, and distribute meeting agenda 24 hours in advance."),
        ("Unit 10 &bull; Hardware Diagnostics &amp; Troubleshooting Drill",
         "<b>Diagnostic Workflow:</b> Check physical power cable &rarr; Inspect Wi-Fi router status LEDs &rarr; Renew IP address via command line (<code>ipconfig /renew</code>) &rarr; Restart device &rarr; Escalate to IT Helpdesk if hardware fault.")
    ],
    "mocks": [
        ("Mock 1 &bull; Office Relocation Project Simulation",
         "<b>Task 1 (Hierarchy):</b> Created folders <code>01_Floor_Plans</code>, <code>02_Vendor_Quotes</code>, <code>03_Staff_Allocations</code>.<br>"
         "<b>Task 2 (Budget Spreadsheet):</b> Input formula <code>=SUM(D4:D18)</code> for subtotal; <code>=D19*0.2</code> for VAT; <code>=D19+D20</code> for gross expenditure.<br>"
         "<b>Task 3 (Executive Briefing):</b> Drafted 250-word memo detailing moving dates, IT downtime schedule, and parking pass reallocation.<br>"
         "<b>Task 4 (Cloud Access):</b> Set shared folder permissions to 'Restricted' with multi-factor authentication required."),
        ("Mock 2 &bull; Customer Service Data Analytics Simulation",
         "<b>Task 1 (Spreadsheet Analytics):</b> Filtered customer complaint log by category; calculated resolution percentage with <code>=COUNTIF(E2:E100, &quot;Resolved&quot;)/COUNTA(E2:E100)</code>.<br>"
         "<b>Task 2 (Chart Generation):</b> Plotted 2D clustered column chart displaying average response times across four quarterly departments.<br>"
         "<b>Task 3 (Professional Email):</b> Formulated sensitive apology email addressing customer shipping delay, offering voucher code and tracking link."),
        ("Mock 3 &bull; Health &amp; Safety Compliance Portal Simulation",
         "<b>Task 1 (Intranet Form):</b> Built online accident reporting form with required fields for employee ID, incident date, and severity level.<br>"
         "<b>Task 2 (Data Validation):</b> Configured input restriction allowing only dates within past 7 days and dropdown list for injury classification.<br>"
         "<b>Task 3 (GDPR Audit):</b> Removed employee national insurance numbers from public shared spreadsheet and archived onto encrypted local drive."),
        ("Mock 4 &bull; Cybersecurity Incident Response Simulation",
         "<b>Task 1 (Incident Triage):</b> Disconnected compromised workstation from local network immediately (pulled Ethernet cable / disabled Wi-Fi).<br>"
         "<b>Task 2 (Breach Log):</b> Recorded incident timestamp, compromised account username, and suspicious email header details.<br>"
         "<b>Task 3 (Password Reset):</b> Guided user through setting up a 16-character passphrase and re-registering authenticator token.<br>"
         "<b>Task 4 (Action Report):</b> Submitted official security event notification to Data Protection Officer within 1 hour.")
    ]
}


# =============================================================================

DIGITAL_SKILLS_SHORTCUTS = r"""<div style='font-size:10pt; line-height:1.4;'>
<p><b>Universal Operating System Shortcuts (Windows / macOS):</b><br>
&bull; Copy: <code>Ctrl + C</code> (Win) / <code>Cmd + C</code> (Mac)<br>
&bull; Paste: <code>Ctrl + V</code> (Win) / <code>Cmd + V</code> (Mac)<br>
&bull; Cut: <code>Ctrl + X</code> (Win) / <code>Cmd + X</code> (Mac)<br>
&bull; Undo / Redo: <code>Ctrl + Z</code> / <code>Ctrl + Y</code><br>
&bull; Select All: <code>Ctrl + A</code><br>
&bull; Find in Page: <code>Ctrl + F</code><br>
&bull; Save Document: <code>Ctrl + S</code><br>
&bull; Print / Save as PDF: <code>Ctrl + P</code><br>
&bull; Lock Workstation: <code>Win + L</code><br>
&bull; File Explorer: <code>Win + E</code><br>
&bull; Task Manager: <code>Ctrl + Shift + Esc</code></p>

<p><b>Web Browser Shortcuts (Chrome / Edge / Firefox):</b><br>
&bull; New Tab: <code>Ctrl + T</code> &emsp; Close Tab: <code>Ctrl + W</code><br>
&bull; Reopen Closed Tab: <code>Ctrl + Shift + T</code><br>
&bull; Incognito / InPrivate: <code>Ctrl + Shift + N</code><br>
&bull; Bookmark Current Page: <code>Ctrl + D</code><br>
&bull; Hard Refresh (Clear Cache): <code>Ctrl + F5</code> or <code>Ctrl + Shift + R</code><br>
&bull; Zoom In / Out / Reset: <code>Ctrl + Plus</code> / <code>Ctrl + Minus</code> / <code>Ctrl + 0</code></p>

<p><b>Spreadsheet Modeling Shortcuts (Excel / Google Sheets):</b><br>
&bull; Edit Active Cell: <code>F2</code><br>
&bull; Toggle Absolute Reference ($): <code>F4</code> (cycles A1 &rarr; $A$1 &rarr; A$1 &rarr; $A1)<br>
&bull; AutoSum Selected Range: <code>Alt + =</code><br>
&bull; Insert Current Date: <code>Ctrl + ;</code><br>
&bull; Fill Down / Fill Right: <code>Ctrl + D</code> / <code>Ctrl + R</code><br>
&bull; Select Entire Column: <code>Ctrl + Space</code> &emsp; Entire Row: <code>Shift + Space</code><br>
&bull; Format as Currency: <code>Ctrl + Shift + 4</code> (/ &pound;)<br>
&bull; Format as Percentage: <code>Ctrl + Shift + 5</code> (%)</p>
</div>"""

DIGITAL_SKILLS_GLOSSARY = [
    ("Absolute Cell Reference ($A$1)", "A locked cell coordinate in a spreadsheet formula that does not change when autofilled into adjacent cells."),
    ("Bandwidth", "The maximum rate of data transfer across a given network path, measured in Megabits per second (Mbps)."),
    ("Cloud Synchronization", "The automated process of mirroring local files to a secure remote cloud server (e.g. OneDrive, Nextcloud)."),
    ("Cybersecurity Hygiene", "Routine practices (e.g. unique passphrases, regular patching, MFA) that maintain security and protect data."),
    ("Data Subject Access Request (DSAR)", "A formal request under GDPR allowing individuals to obtain a copy of personal data held by an organization."),
    ("DSE Assessment", "Display Screen Equipment risk assessment mandated by Health and Safety regulations to prevent ergonomic strain."),
    ("Encryption (End-to-End)", "A communication system where only the communicating users can read the messages, preventing eavesdropping."),
    ("Multi-Factor Authentication (MFA)", "An authentication method requiring two or more verification factors (password + authenticator app code)."),
    ("Netiquette", "The conventional rules of polite, professional, and respectful behavior in online and email communications."),
    ("Phishing", "A fraudulent attempt to obtain sensitive information by disguising as a trustworthy entity in electronic communications."),
    ("Ransomware", "Malicious software designed to block access to a computer system or encrypt files until a sum of money is paid."),
    ("URL (Uniform Resource Locator)", "The unique address used to identify and locate a specific webpage or file on the World Wide Web."),
    ("VPN (Virtual Private Network)", "An encrypted connection over the internet from a device to a network, shielding online activity.")
]

DIGITAL_SKILLS_INDEX = [
    ("A", [("Absolute cell references ($A$1)", "4, 18"), ("Account security & credentials", "3, 12, 24"), ("Anti-virus & malware protection", "5, 20")]),
    ("B", [("Backup strategies (3-2-1 rule)", "6, 22"), ("Browser safety & SSL padlocks", "5, 16"), ("Budgeting spreadsheets", "14, 28")]),
    ("C", [("Cloud collaboration & sharing permissions", "7, 26"), ("Conditional formatting rules", "15, 29"), ("Cybersecurity essentials", "5, 12, 30")]),
    ("D", [("Data Protection Act & GDPR", "8, 32"), ("Data validation dropdowns", "14, 28"), ("Digital footprint management", "8, 34")]),
    ("E", [("Email attachments & file size limits", "9, 36"), ("Email etiquette & professional register", "9, 38"), ("Excel / Sheets formulas", "4, 14, 28")]),
    ("F", [("File folder hierarchy & naming conventions", "10, 40"), ("Firewalls & network security", "5, 20")]),
    ("I", [("IF statements & logical formulas", "4, 15, 29"), ("Incognito & private browsing", "5, 17")]),
    ("M", [("Mocks 1-4 workplace scenarios", "44-59"), ("Multi-factor authentication (MFA)", "3, 12, 24")]),
    ("P", [("Password complexity & managers", "3, 12"), ("Phishing & email fraud identification", "5, 21"), ("Privacy settings on social platforms", "8, 35")]),
    ("S", [("Shortcuts matrix (Windows & Mac)", "60"), ("Solutions for Units 1-10 Drills", "61-75"), ("SUM and AVERAGE formulas", "4, 14, 28")]),
    ("T", [("Troubleshooting device connectivity", "11, 42"), ("Two-factor authentication (2FA)", "3, 12, 24")]),
    ("V", [("Version control in cloud documents", "7, 27"), ("Virtual Private Networks (VPN)", "5, 19")])
]


# 4. BKSB REMEDIATION WORKBOOK REFERENCE DATA
# =============================================================================

BKSB_GOLDEN_RULES = r"""<div style='font-size:10pt; line-height:1.4;'>
<p><b>Master Diagnostic Golden Rules (Maths &amp; English):</b><br>
&bull; <b>Rule 1 (Reverse Percentage):</b> Never multiply the final discounted price by the discount percent. Always divide by the decimal multiplier (1.00 − discount rate).<br>
&bull; <b>Rule 2 (Time in Calculations):</b> Minutes are not decimals! 45 minutes is 45/60 = 0.75 hours, NOT 0.45 hours.<br>
&bull; <b>Rule 3 (Units &amp; Precision):</b> Money answers must always have 2 decimal places (£14.50, never £14.5). State units on area (m²) and volume (m³).<br>
&bull; <b>Rule 4 (Circle Area vs Circumference):</b> Area = 3.142 × Radius² (squares the radius first). Circumference = 3.142 × Diameter. Never mix them up.<br>
&bull; <b>Rule 5 (Grouped Mean):</b> Always multiply interval midpoints by frequency before summing. Divide by the total frequency, never by the number of intervals.<br>
&bull; <b>Rule 6 (Fact vs Opinion):</b> A fact can be proved objectively with data or dates. An opinion contains value words ('best', 'should', 'terrible').<br>
&bull; <b>Rule 7 (Apostrophes of Possession):</b> Singular noun takes <code>'s</code> (the manager's car). Plural noun ending in 's' takes trailing apostrophe (the workers' canteen).<br>
&bull; <b>Rule 8 (Formal Tone &amp; Contractions):</b> In formal letters and reports, never use contractions (write <i>'do not'</i>, never <i>'don't'</i>).</p>
</div>"""

BKSB_GLOSSARY = [
    ("Algorithmic Marking", "Automated computer grading that marks an answer entirely incorrect if syntax, units, or decimal formatting deviate from the expected string."),
    ("Class Midpoint", "The central numerical value of a grouped class interval: (Lower bound + Upper bound) / 2."),
    ("Compound Fraction", "A numerical expression combining whole numbers and fractions (3 1/4), requiring conversion to improper fractions for multiplication."),
    ("Diagnostic Assessment", "An initial online baseline test determining a learner's current working level and identifying specific skill gaps."),
    ("Independent Event", "A probability scenario where the outcome of the first trial has zero influence on the outcome of the second trial."),
    ("Inverse Operation", "The opposite mathematical operation used to verify a calculation (e.g. division verifies multiplication)."),
    ("Process Error", "An error where an incorrect formula or strategy was selected, resulting in loss of method marks."),
    ("Rounding Prematurity", "A fatal calculation error where intermediate numbers are rounded early, corrupting the final answer."),
    ("Subject-Verb Agreement", "The grammatical rule requiring singular subjects to take singular verbs and plural subjects to take plural verbs.")
]

BKSB_INDEX = [
    ("A", [("Algorithmic marking traps", "3, 12"), ("Apostrophe placement (omission/possession)", "4, 38, 52"), ("Area calculations (circles & composite)", "7, 16, 28")]),
    ("B", [("BKSB diagnostic interface navigation", "3, 5"), ("Budgeting & financial math", "8, 20, 32")]),
    ("C", [("Class midpoints in grouped mean", "10, 24"), ("Compound fractions & mixed numbers", "9, 22"), ("Contractions in formal writing", "4, 40, 54")]),
    ("D", [("Decimal money formatting (£.00)", "7, 14, 26"), ("Density, mass & volume traps", "11, 25")]),
    ("E", [("Estimated mean grouped data", "10, 24"), ("Evaluation of online questions", "6, 18")]),
    ("F", [("Fact vs opinion diagnostic questions", "4, 36, 50"), ("Fractions addition & subtraction", "9, 22")]),
    ("G", [("Glossary of diagnostic terms", "76"), ("Golden Rules summary table", "75")]),
    ("H", [("Hours & minutes conversion traps", "8, 18, 30"), ("Hypotenuse & Pythagoras", "11, 26")]),
    ("I", [("Inverse check verification", "7, 15, 27")]),
    ("M", [("Modes 1-24 Diagnostic masterclasses", "7-54")]),
    ("P", [("Percentages: reverse and multiplier", "7, 14, 26"), ("Probability tree & product rule", "10, 24")]),
    ("R", [("Ratio sharing & unit conversion", "8, 20, 32"), ("Remediation tracking log", "6"), ("Retry Drills (72 authentic questions)", "8-54")]),
    ("S", [("Solutions for Modes 1-24 Drills", "57-74"), ("Speed, distance & decimal time", "8, 18, 30"), ("Subject-verb agreement", "4, 42, 56")]),
    ("T", [("Tolerance limits & engineering", "9, 21")])
]

# Solutions for all 24 BKSB Failure Modes (72 drills in total)
BKSB_STAGE2_SOLUTIONS = {
    1: [
        ("Mode 1 Solutions: Reverse Percentage &amp; Tax Calculation",
         "<b>Drill 1.1:</b> Original price before 15% discount: Sale price £340. Multiplier = 1.00 - 0.15 = 0.85. Original = 340 ÷ 0.85 = <b>£400.00</b>.<br>"
         "<b>Drill 1.2:</b> Original salary before 5% pay increase: New wage £25,200. Multiplier = 1.05. Pre-increase = 25,200 ÷ 1.05 = <b>£24,000.00</b>.<br>"
         "<b>Drill 1.3:</b> Price before 20% VAT: Gross invoice £516.00. Multiplier = 1.20. Net = 516 ÷ 1.20 = <b>£430.00</b>. VAT amount = 516 - 430 = £86.00.")
    ],
    2: [
        ("Mode 2 Solutions: Time Conversion &amp; Speed Calculations",
         "<b>Drill 2.1:</b> Decimal hours: 2 hrs 45 mins = 2 + 45/60 = <b>2.75 hours (never 2.45).<br>"
         "<b>Drill 2.2:</b> Distance: 48 mph for 3 hrs 20 mins. 20 mins = 20/60 = 0.333 hrs. Time = 3.333 hrs. Distance = 48 × 3.333 = <b>160 miles</b>.<br>"
         "<b>Drill 2.3:</b> Average speed: 126 miles in 2 hrs 15 mins. Time = 2.25 hrs. Speed = 126 ÷ 2.25 = <b>56 mph</b>.")
    ],
    3: [
        ("Mode 3 Solutions: Circle Calculations &amp; Precision",
         "<b>Drill 3.1:</b> Area of circular rug: Diameter d = 2.4 m → Radius r = 1.2 m. Area = 3.142 × (1.2)² = 3.142 × 1.44 = <b>4.52 m²</b>.<br>"
         "<b>Drill 3.2:</b> Circumference of wheel: r = 35 cm → d = 70 cm. C = 3.142 × 70 = <b>219.9 cm (or 2.20 m).<br>"
         "<b>Drill 3.3:</b> Semi-circular perimeter: Diameter 14 m → Curved edge = (3.142 × 14) / 2 = 21.99 m. Total perimeter = 21.99 + 14 = <b>35.99 m</b>.")
    ],
    4: [
        ("Mode 4 Solutions: Fractions &amp; Mixed Numbers Operations",
         "<b>Drill 4.1:</b> 1 3/4 + 2 2/3 = 7/4 + 8/3 = (21 + 32)/12 = 53/12 = <b>4 5/12</b>.<br>"
         "<b>Drill 4.2:</b> 3 1/2 - 1 4/5 = 7/2 - 9/5 = (35 - 18)/10 = 17/10 = <b>1 7/10</b>.<br>"
         "<b>Drill 4.3:</b> 2 1/4 × 1 1/3 = 9/4 × 4/3 = 36/12 = <b>3</b>.")
    ],
    5: [
        ("Mode 5 Solutions: Grouped Frequency &amp; Estimated Mean",
         "<b>Drill 5.1:</b> Intervals 0-9 (mid 4.5, f=6, fx=27), 10-19 (mid 14.5, f=14, fx=203), 20-29 (mid 24.5, f=20, fx=490), 30-39 (mid 34.5, f=10, fx=345). Total fx = 1,065. Total f = 50. Mean = 1,065 ÷ 50 = <b>21.3 units</b>.<br>"
         "<b>Drill 5.2:</b> Modal class: <b>20&ndash;29</b> (highest frequency of 20).<br>"
         "<b>Drill 5.3:</b> Class interval containing the median: Total N=50, median position 25.5. Cumulative frequency: 6, 20, 40. Median lies in <b>20&ndash;29</b>.")
    ],
    6: [
        ("Mode 6 Solutions: Density, Mass &amp; Volume",
         "<b>Drill 6.1:</b> Mass: Concrete volume 0.8 m³, density 2,400 kg/m³. Mass = 0.8 × 2,400 = <b>1,920 kg</b>.<br>"
         "<b>Drill 6.2:</b> Density: Metal block mass 540 g, dimensions 4 cm × 5 cm × 6 cm = 120 cm³. Density = 540 ÷ 120 = <b>4.5 g/cm³</b>.<br>"
         "<b>Drill 6.3:</b> Volume: Liquid mass 850 g, density 0.85 g/cm³. Volume = 850 ÷ 0.85 = <b>1,000 cm³ (or 1 litre).")
    ],
    7: [
        ("Mode 7 Solutions: Ratio Sharing &amp; Unit Conversion",
         "<b>Drill 7.1:</b> Share £1,400 in ratio 2:5. Total parts = 7. 1 part = 1,400 ÷ 7 = £200. Shares: <b>£400</b> and <b>£1,000</b>.<br>"
         "<b>Drill 7.2:</b> Ratio of gravel to sand is 3:7. 21 bags of gravel used → 1 part = 21 ÷ 3 = 7 bags. Sand required = 7 × 7 = <b>49 bags</b>.<br>"
         "<b>Drill 7.3:</b> Scale model 1:25. Wall length on model 16 cm → Real length = 16 × 25 = 400 cm = <b>4.0 metres</b>.")
    ],
    8: [
        ("Mode 8 Solutions: Multi-Step Pythagoras &amp; Trigonometry",
         "<b>Drill 8.1:</b> Triangle legs a = 6 m, b = 8 m. c = √(6² + 8²) = √(36 + 64) = √(100) = <b>10 m</b>.<br>"
         "<b>Drill 8.2:</b> Ladder length c = 5 m, wall distance b = 1.4 m. Reach a = √(5² - 1.4²) = √(25 - 1.96) = √(23.04) = <b>4.8 m</b>.<br>"
         "<b>Drill 8.3:</b> Rectangular lawn 15 m × 20 m. Diagonal path = √(15² + 20²) = √(225 + 400) = √(625) = <b>25 m</b>.")
    ],
    9: [
        ("Mode 9 Solutions: Compound Interest &amp; Depreciation",
         "<b>Drill 9.1:</b> £3,000 invested at 4% compound interest for 3 years: 3,000 × (1.04)³ = 3,000 × 1.124864 = <b>£3,374.59</b>.<br>"
         "<b>Drill 9.2:</b> Vehicle value £18,000 depreciating at 12% per year for 2 years: 18,000 × (0.88)² = 18,000 × 0.7744 = <b>£13,939.20</b>.<br>"
         "<b>Drill 9.3:</b> Total interest earned on £5,000 at 3% compound for 2 years: 5,000 × (1.03)² - 5,000 = 5,304.50 - 5,000 = <b>£304.50</b>.")
    ],
    10: [
        ("Mode 10 Solutions: Probability &amp; Tree Diagrams",
         "<b>Drill 10.1:</b> P(Head on coin AND 6 on dice) = 1/2 × 1/6 = <b>1/12 (or 0.0833).<br>"
         "<b>Drill 10.2:</b> Two components tested independently. Fault rates 0.05 and 0.02. Probability both functional = (1 - 0.05) × (1 - 0.02) = 0.95 × 0.98 = <b>0.931</b> (93.1%).<br>"
         "<b>Drill 10.3:</b> Bag contains 4 red, 6 blue. Drawing 1 red then without replacement 1 blue = 4/10 × 6/9 = 24/90 = <b>4/15 (or 0.267).")
    ],
    11: [
        ("Mode 11 Solutions: Surface Area &amp; Prism Volume",
         "<b>Drill 11.1:</b> Cylinder radius 0.5 m, height 2 m. Volume = 3.142 r² h = 3.142 × 0.25 × 2 = <b>1.57 m³ (1,570 litres).<br>"
         "<b>Drill 11.2:</b> Curved surface area of cylinder: 23.142 r h = 2 × 3.142 × 0.5 × 2 = <b>6.28 m²</b>.<br>"
         "<b>Drill 11.3:</b> Triangular prism: Triangle base 4 cm, height 3 cm, prism length 10 cm. Volume = (1/2 × 4 × 3) × 10 = 6 × 10 = <b>60 cm³</b>.")
    ],
    12: [
        ("Mode 12 Solutions: Scatter Graphs &amp; Correlation",
         "<b>Drill 12.1:</b> As outside temperature increases, heating oil usage decreases. Type: <b>Negative Correlation</b>.<br>"
         "<b>Drill 12.2:</b> Estimating from line of best fit at 18 degrees Celsius gives an expected consumption of <b>42 litres</b> (allow ± 2 L).<br>"
         "<b>Drill 12.3:</b> An outlier point plotted at (28 degrees, 95 litres) indicates a boiler malfunction or faulty meter reading.")
    ],
    13: [
        ("Mode 13 Solutions: Tolerance &amp; Engineering Limits",
         "<b>Drill 13.1:</b> Shaft dimension 45 mm ± 0.5 mm. Minimum acceptable = 44.5 mm, maximum acceptable = <b>45.5 mm</b>.<br>"
         "<b>Drill 13.2:</b> A manufactured component measures 45.48 mm. This is <b>within acceptable tolerance</b> (44.5 ≤ 45.48 ≤ 45.5).<br>"
         "<b>Drill 13.3:</b> Acceptable weight 250 g ± 2%. 2% of 250 = 5 g. Acceptable range = <b>245 g to  255 g</b>.")
    ],
    14: [
        ("Mode 14 Solutions: Unit Conversion Traps (Metric &amp; Imperial)",
         "<b>Drill 14.1:</b> Convert 3.5 m³ to litres: 1 m³ = 1,000 L → 3.5 × 1,000 = <b>3,500 litres</b>.<br>"
         "<b>Drill 14.2:</b> 12 gallons of fuel converted to litres (1 gal ≈ 4.55 L): 12 × 4.55 = <b>54.6 litres</b>.<br>"
         "<b>Drill 14.3:</b> 85 km converted to miles (5 miles ≈ 8 km): (85 ÷ 8) × 5 = <b>53.1 miles</b>.")
    ],
    15: [
        ("Mode 15 Solutions: Multi-Option Best Buy Analysis",
         "<b>Drill 15.1:</b> Deal A: 12 packs at £3.20 = £38.40. Deal B: 15 packs at £2.80 = £42.00. Cost per pack A = £3.20; B = £2.80. <b>Deal B is better value</b> by 40p per pack.<br>"
         "<b>Drill 15.2:</b> Wholesaler X: £600 - 15% discount = 600 × 0.85 = £510. Wholesaler Y: £580 - 10% discount + £10 delivery = 522 + 10 = £532. <b>Wholesaler X is cheaper by £22.00</b>.<br>"
         "<b>Drill 15.3:</b> 3 for 2 deal on £18 shirts: 3 shirts cost £36 → Unit cost = £12.00. Regular discount 30% off £18 = £12.60. <b>The 3 for 2 offer saves 60p per shirt</b>.")
    ],
    16: [
        ("Mode 16 Solutions: Decimal Rounding in Currency Calculations",
         "<b>Drill 16.1:</b> Calculation yields 14.5. Written currency answer must be <b>£14.50</b> (trailing zero mandatory for pence).<br>"
         "<b>Drill 16.2:</b> Hourly pay £9.85 × 37.5 hrs = £369.375. Rounded to nearest penny = <b>£369.38</b>.<br>"
         "<b>Drill 16.3:</b> Invoicing 4 items at £12.499: 4 × 12.499 = 49.996 → <b>£50.00</b>.")
    ],
    17: [
        ("Mode 17 Solutions: Fact vs Opinion Diagnostics",
         "<b>Drill 17.1:</b> <i>'The train arrived 14 minutes behind schedule'</i> is a <b>Fact</b> (empirically verifiable).<br>"
         "<b>Drill 17.2:</b> <i>'Commuters deserve far better customer service'</i> is an <b>Opinion</b> (value statement with modal verb).<br>"
         "<b>Drill 17.3:</b> <i>'Electric buses produce zero tailpipe emissions and are the finest innovation of modern transport.'</i> Analysis: Contains a factual claim (zero emissions) paired with an opinion (finest innovation).")
    ],
    18: [
        ("Mode 18 Solutions: Apostrophes of Omission and Possession",
         "<b>Drill 18.1:</b> The contract belonging to the employee: <b>The employee's contract</b> (singular possession).<br>"
         "<b>Drill 18.2:</b> The break room used by all staff members: <b>The staff members' room</b> (plural ending in s).<br>"
         "<b>Drill 18.3:</b> Correction: <i>'Its clear that the company has updated it\\'s policy.'</i> Corrected: <b>'It\\'s clear that the company has updated its policy.'</b> (It\\'s = it is; its = possessive pronoun).")
    ],
    19: [
        ("Mode 19 Solutions: Subject-Verb Agreement in Complex Clauses",
         "<b>Drill 19.1:</b> <i>'The stack of invoices on the desk (was / were) approved.'</i> Correct: <b>was</b> (subject is singular 'stack', not 'invoices').<br>"
         "<b>Drill 19.2:</b> <i>'Neither the manager nor the supervisors (has / have) keys.'</i> Correct: <b>have</b> (verb agrees with closest subject 'supervisors').<br>"
         "<b>Drill 19.3:</b> <i>'The team of technicians (is / are) deploying the update.'</i> Correct: <b>is</b> (collective noun treated as singular entity).")
    ],
    20: [
        ("Mode 20 Solutions: Tone, Register &amp; Contraction Remediation",
         "<b>Drill 20.1:</b> Informal sentence: <i>'Cannot make the meeting cos I am swamped.'</i> Formal rewrite: <b>'I will be unable to attend the scheduled meeting due to conflicting urgent duties.'</b><br>"
         "<b>Drill 20.2:</b> Contraction elimination: <i>'We did not receive the specs.'</i> Formal rewrite: <b>'We did not receive the technical specifications.'</b><br>"
         "<b>Drill 20.3:</b> Transforming aggressive register: <i>'Fix this immediately.'</i> Professional rewrite: <b>'Please rectify these discrepancies at your earliest convenience.'</b>")
    ],
    21: [
        ("Mode 21 Solutions: Comma Splices &amp; Compound Sentence Joining",
         "<b>Drill 21.1:</b> Comma splice: <i>'The shipment arrived late, the cargo was undamaged.'</i> Fix 1: <b>The shipment arrived late; however, the cargo was undamaged.</b> Fix 2: <b>Although the shipment arrived late, the cargo was undamaged.</b><br>"
         "<b>Drill 21.2:</b> Semicolon rule: Use a semicolon between two independent clauses closely related in meaning without a coordinating conjunction.<br>"
         "<b>Drill 21.3:</b> FANBOYS conjunction insertion: <i>'The inspection passed, <b>so</b> the certificate was issued.'</i>")
    ],
    22: [
        ("Mode 22 Solutions: Bias, Purpose &amp; Subtext Detection",
         "<b>Drill 22.1:</b> Detecting bias: Look for loaded adjectives, unbalanced evidence, omission of counterarguments, and corporate sponsorship.<br>"
         "<b>Drill 22.2:</b> Primary purpose: The leaflet's purpose is <b>persuasive</b> (aims to convince residents to switch to digital bin alerts).<br>"
         "<b>Drill 22.3:</b> Subtext analysis: <i>'While others make promises, our firm delivers.'</i> Implied subtext: Competitors are untrustworthy and ineffective.")
    ],
    23: [
        ("Mode 23 Solutions: Homophone Discrimination (There/Their/They're etc.)",
         "<b>Drill 23.1:</b> <b>They're</b> waiting over <b>there</b> with <b>their</b> credentials.<br>"
         "<b>Drill 23.2:</b> The economic reform will <b>affect</b> every business; the primary <b>effect</b> will be lower inflation.<br>"
         "<b>Drill 23.3:</b> The team must <b>practice</b> daily if they hope to improve their <b>practice</b>.")
    ],
    24: [
        ("Mode 24 Solutions: Synthesis &amp; Text Comparison Questions",
         "<b>Drill 24.1:</b> Comparative synthesis: Text A focuses on technological efficiency; Text B emphasizes human oversight and safety verification.<br>"
         "<b>Drill 24.2:</b> Direct quotation contrast: Text A states <i>'Automation eliminates human error,'</i> whereas Text B counters that <i>'Algorithmic systems require constant human audit.'</i><br>"
         "<b>Drill 24.3:</b> Integrated summary conclusion: Combining both perspectives, optimal operational outcomes require automated speed paired with mandatory manual verification checkpoints.")
    ]
}

# Appended Solutions for Mock 7 & 8
MATHS_L2_MOCK_SOLUTIONS[7] = [
    ("Mock 7 &bull; Section A &amp; B Model Solutions",
     "<b>Section A Non-Calculator Summary:</b><br>"
     "&bull; Q1: Fleet van oil &amp; filter invoice: 16 vans &times; (6 &times; &pound;8.40 + &pound;14.50) = 16 &times; (&pound;50.40 + &pound;14.50) = 16 &times; &pound;64.90 = <b>&pound;1,038.40</b>.<br>"
     "&bull; Q2: Circular skid pan: Radius = 14 m. Area = 3.14 &times; 14&sup2; = 3.14 &times; 196 = <b>615.44 m&sup2;</b>.<br>"
     "&bull; Q3: Fractions: 2 3/8 + 1 1/4 = 19/8 + 10/8 = 29/8 = <b>3 5/8</b>.<br>"
     "&bull; Q4: Reverse discount: &pound;102.00 ÷ 0.85 = <b>&pound;120.00</b>. Check: 120 &times; 0.85 = &pound;102.00.<br>"
     "&bull; Q5: Antifreeze ratio 2:5, total 7 parts of 84 L. 1 part = 12 L. Antifreeze = 2 &times; 12 = <b>24 litres</b>.<br><br>"
     "<b>Section B Calculator Highlights:</b><br>"
     "&bull; Q6: Diagnostic mechanics payroll: (8 &times; 38.5 &times; &pound;17.20) + (2 &times; 40 &times; &pound;23.50) = &pound;5,297.60 + &pound;1,880.00 = <b>&pound;7,177.60</b>.<br>"
     "&bull; Q7: Workshop paint: Net area = (24.5 &times; 16.0) - (8.0 &times; 2.5) = 392 - 20 = 372 m&sup2;. Two coats = 744 m&sup2;. Tins = 744 ÷ 35 = 21.25 &rarr; 22 tins. Cost = 22 &times; &pound;48.50 = <b>&pound;1,067.00</b>.<br>"
     "&bull; Q8: MOT estimated mean = <b>37.8 minutes</b>.<br>"
     "&bull; Q9: Recovery truck fuel: 340 ÷ 11.5 = 29.565 gal = 134.52 L &times; &pound;1.54 = <b>&pound;207.16</b>.<br>"
     "&bull; Q10: Cylindrical waste oil tank volume: 3.142 &times; 1.1&sup2; &times; 2.4 = 9.124 m&sup3; = <b>9,124 litres</b>.<br>"
     "&bull; Q11: Parts margin: (&pound;16,800 ÷ &pound;48,600) &times; 100 = <b>34.6%</b>.<br>"
     "&bull; Q12: Combined brake reliability: 0.98 &times; 0.97 = <b>0.9506</b>.<br>"
     "&bull; Q13: Tow truck arrival: 68 ÷ 48 = 1.417 hrs = 1 hr 25 mins. Arrival = 14:20 + 1h 25m = <b>15:45</b>.<br>"
     "&bull; Q14: Loading ramp length: √(1.4&sup2; + 4.8&sup2;) = √(1.96 + 23.04) = √25.0 = <b>5.0 metres</b>.<br>"
     "&bull; Q15: Tyre supplier: Supplier A = 40 &times; 110 &times; 0.88 = &pound;3,872.00. Supplier B = (40 &times; 105 &times; 0.95) + 60 = &pound;4,050.00. <b>Supplier A is cheaper by &pound;178.00</b>.")
]

MATHS_L2_MOCK_SOLUTIONS[8] = [
    ("Mock 8 &bull; Section A &amp; B Model Solutions",
     "<b>Section A Non-Calculator Summary:</b><br>"
     "&bull; Q1: Solar equipment: (28 &times; &pound;185) + (4 &times; &pound;420) = &pound;5,180 + &pound;1,680 = <b>&pound;6,860.00</b>.<br>"
     "&bull; Q2: Circular turbine base: Area = 3.14 &times; 3.5&sup2; = 3.14 &times; 12.25 = <b>38.47 m&sup2;</b>.<br>"
     "&bull; Q3: Mixed numbers: 3 1/3 + 2 2/5 = 10/3 + 12/5 = (50 + 36)/15 = 86/15 = <b>5 11/15</b>.<br>"
     "&bull; Q4: Reverse grant: Subsidized 35% &rarr; Multiplier = 0.65. Original = &pound;5,525 ÷ 0.65 = <b>&pound;8,500.00</b>.<br>"
     "&bull; Q5: Solar battery distribution: 3:7, 10 parts of 60 kWh = 6 kWh per part. EV charging = 7 &times; 6 = <b>42 kWh</b>.<br><br>"
     "<b>Section B Calculator Highlights:</b><br>"
     "&bull; Q6: Green installation payroll: (6 &times; 42 &times; &pound;22.50) + (2 &times; 45 &times; &pound;28.00) = &pound;5,670 + &pound;2,520 = <b>&pound;8,190.00</b>.<br>"
     "&bull; Q7: Roof solar panels: Net area = (32.0 &times; 14.5) - (2 &times; 6.0) = 464 - 12 = 452 m&sup2;. One panel = 1.7 m&sup2;. Panels = 452 ÷ 1.7 = 265.8 &rarr; <b>265 panels</b>.<br>"
     "&bull; Q8: Solar generation mean = <b>24.4 kWh</b>.<br>"
     "&bull; Q9: Electric van energy cost: 145 ÷ 3.8 = 38.16 kWh &times; &pound;0.24 = <b>&pound;9.16</b>.<br>"
     "&bull; Q10: Buffer tank capacity: 3.142 &times; 0.45&sup2; &times; 1.8 = 1.145 m&sup3; = <b>1,145 litres</b>.<br>"
     "&bull; Q11: Annual efficiency savings margin: (&pound;5,400 ÷ &pound;16,800) &times; 100 = <b>32.1%</b>.<br>"
     "&bull; Q12: Combined inverter reliability: 0.97 &times; 0.96 = <b>0.9312</b>.<br>"
     "&bull; Q13: Maintenance trip time: 112 ÷ 42 = 2.667 hrs = 2 hrs 40 mins. Arrival = 07:15 + 2h 40m = <b>09:55</b>.<br>"
     "&bull; Q14: Wind mast guy wire: √(15.0&sup2; + 8.0&sup2;) = √(225 + 64) = √289 = <b>17.0 metres</b>.<br>"
     "&bull; Q15: Tender decision: Contractor X = (8,200 &times; 0.92) + 150 = &pound;7,694.00. Contractor Y = 8,500 &times; 0.88 = &pound;7,480.00. <b>Contractor Y is cheaper by &pound;214.00</b>.")
]

# Appended Solutions for BKSB Diagnostic Papers 1 to 4
BKSB_PAPERS_SOLUTIONS = {
    1: [
        ("Diagnostic Paper 1 Model Solutions (Maths Non-Calculator)",
         "<b>Q1. Warehouse Invoice:</b> (18 &times; &pound;14.80) + (5 &times; &pound;46.50) = &pound;266.40 + &pound;232.50 = &pound;498.90. Discount 10% = &pound;49.89. Total payable = &pound;498.90 - &pound;49.89 = <b>&pound;449.01</b>.<br>"
         "<b>Q2. Grain Silo Base Area:</b> Radius r = 2.5 m. Area = 3.14 &times; (2.5)&sup2; = 3.14 &times; 6.25 = <b>19.63 m&sup2;</b> (or 19.625 m&sup2;).<br>"
         "<b>Q3. Mixed Fractions:</b> 2 1/3 + 1 3/5 = 7/3 + 8/5 = (35 + 24)/15 = 59/15 = <b>3 14/15</b>.<br>"
         "<b>Q4. Reverse Discount:</b> &pound;280.00 ÷ 0.80 = <b>&pound;350.00</b>. Check: 350 &times; 0.80 = &pound;280.00.<br>"
         "<b>Q5. Concrete Ratio:</b> Ratio 1:2:4, total 7 parts of 2,100 kg. 1 part = 300 kg. Gravel = 4 &times; 300 = <b>1,200 kg</b>.<br>"
         "<b>Q6. Scale Conversion:</b> 8.4 cm &times; 50 = 420 cm = <b>4.2 metres</b>.<br>"
         "<b>Q7. Carton Division:</b> 1,485 ÷ 36 = 41.25 &rarr; <b>42 master cartons</b> required to hold all kits.")
    ],
    2: [
        ("Diagnostic Paper 2 Model Solutions (Maths Calculator)",
         "<b>Q1. Logistics Payroll:</b> (14 &times; 37.5 &times; &pound;11.44) + (3 &times; 40 &times; &pound;16.80) = &pound;6,006.00 + &pound;2,016.00 = <b>&pound;8,022.00</b>.<br>"
         "<b>Q2. Tarmac Resurfacing:</b> Net area = (28.0 &times; 15.5) - (4.0 &times; 3.0) = 434 - 12 = 422 m&sup2;. Bags = 422 ÷ 1.5 = 281.33 &rarr; 282 bags. Cost = 282 &times; &pound;18.20 = <b>&pound;5,132.40</b>.<br>"
         "<b>Q3. Estimated Mean Delivery Time:</b> Midpoints: 12 (8 &times; 12 = 96), 17 (18 &times; 17 = 306), 22 (16 &times; 22 = 352), 27 (8 &times; 27 = 216). Total Total fx = 970. N = 50. Mean = 970 ÷ 50 = <b>19.4 minutes</b>.<br>"
         "<b>Q4. Van Route Fuel:</b> 276 ÷ 46 = 6.0 gal &times; 4.55 = 27.3 L &times; &pound;1.52 = <b>&pound;41.50</b>.<br>"
         "<b>Q5. Cylindrical Tank Capacity:</b> 3.142 &times; 1.2&sup2; &times; 3.0 = 13.573 m&sup3; = <b>13,573 litres</b>.<br>"
         "<b>Q6. Operating Profit Margin:</b> Profit = &pound;36,400 - &pound;24,800 = &pound;11,600. Margin % = (&pound;11,600 ÷ &pound;36,400) &times; 100 = <b>31.9%</b>.<br>"
         "<b>Q7. Arrival Time:</b> 154 ÷ 44 = 3.5 hours = 3 hrs 30 mins. Departure = 11:35. Arrival = 11:35 + 3h 30m = <b>15:05</b>.<br>"
         "<b>Q8. Ramp Hypotenuse:</b> √(1.5&sup2; + 5.5&sup2;) = √(2.25 + 30.25) = √32.5 = <b>5.70 metres</b>.")
    ],
    3: [
        ("Diagnostic Paper 3 Model Solutions (English Reading)",
         "<b>Q1. Statistics from Text A:</b> &pound;45,000 average graduate debt and 91% employment completion rate for apprentices.<br>"
         "<b>Q2. Fact and Opinion in Text B:</b> Fact: Apprentices spend twenty percent of working hours in off-the-job training. Opinion: Training burdens on small employers are overwhelming.<br>"
         "<b>Q3. Tone in Text A:</b> Encouraging and authoritative, using data-driven arguments: <i>'superior workplace resilience, immediate technical capability.'</i><br>"
         "<b>Q4. Definition:</b> 'Universal panacea' means a cure-all or miraculous solution that solves every single problem.<br>"
         "<b>Q5. Comparative Impact on Employers:</b> Text A portrays apprentices as loyalty-building and productive assets. Text B presents small employers struggling with production loss and mentor diversion.<br>"
         "<b>Q6. Organizational Features:</b> Bold headline, subheadings, cited authority quotation (Marcus Bennett), and comparative paragraphs.<br>"
         "<b>Q7. Synthesis:</b> Funding mentorship subsidies directly to SMEs while retaining the levy support will safeguard both apprentice welfare and small business profitability.")
    ],
    4: [
        ("Diagnostic Paper 4 Model Solutions (English Writing)",
         "<b>Task 1 Model (Formal Recommendation Report):</b><br>"
         "Layout: To: Operations Director; From: Abdul, Apprentice Coordinator; Date: 14 October 2026; Subject: Technical Trainee Mentorship Proposal.<br>"
         "Sections: 1. Purpose &amp; Executive Summary, 2. Productivity Benefits, 3. Workload Mitigation, 4. Strategic Recommendations.<br>"
         "Content highlights: Establishes a 2-hour protected Friday morning mentor slot, pairs trainees with senior mentors, and schedules quarterly progress reviews.<br><br>"
         "<b>Task 2 Model (Persuasive Careers Evening Speech):</b><br>"
         "Opening: 'Good evening students, parents, and teachers.' Captures attention by contrasting &pound;45,000 university debt against earning &pound;22,000 while training.<br>"
         "Rhetorical devices: Tri-colon ('skills for today, qualifications for tomorrow, and careers for life'), rhetorical question ('Why spend three years accumulating debt when you could be accumulating experience?').<br>"
         "Call to action: Directs students to speak with vocational advisors at the exhibition stands.")
    ]
}
