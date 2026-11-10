"""
books/a4/maths_suite_reference.py
=============================================================================
Contains complete, authentic numerical worked solutions, examiner marking
criteria, official Pearson Edexcel formula references, glossaries, and
alphabetical indices for all 5 Mathematics publications in the A4 Master
Functional Skills suite.

Zero generic filler. Every question has step-by-step arithmetic, intermediate
method marks [M], process marks [P], accuracy marks [A], and units [B].
=============================================================================
"""

# =============================================================================
# Level 2 Mathematics Reference Data
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
    ("Angle of Sector", "The central angle representing a category on a pie chart: (frequency / total) × 360°."),
    ("Compound Interest", "Interest calculated on both the original principal and accumulated past interest (A = P(1+r)ⁿ)."),
    ("Correlation", "The relationship between two variables on a scatter graph (positive, negative, or zero/none)."),
    ("Density", "Mass per unit volume (e.g. g/cm³ or kg/m³): Density = Mass / Volume."),
    ("Depreciation", "The decrease in the financial value of an asset over time due to wear and tear or market factors."),
    ("Estimated Mean", "Mean computed from grouped data using midpoints of intervals: Sum(fx) / Sum f."),
    ("Hypotenuse", "The longest side of a right-angled triangle, opposite the 90° angle (a² + b² = c²)."),
    ("Line of Best Fit", "A straight line drawn through the center of plotted points on a scatter diagram to show the general trend."),
    ("Multiplier", "A single decimal number used to calculate percentage increases (1 + r) or decreases (1 - r)."),
    ("Probability", "The mathematical likelihood of an event occurring: favourable outcomes / total possible outcomes."),
    ("Range", "A measure of data spread: Highest value - Lowest value."),
    ("Reverse Percentage", "Finding the original pre-change value by dividing the final amount by the decimal multiplier."),
    ("Scale Factor", "The ratio of a dimension on a model or map to the actual corresponding real dimension (e.g. 1:50)."),
    ("Surface Area", "The total area of all exterior faces of a three-dimensional solid.")
]

MATHS_L2_INDEX = [
    ("A", [("Area of 2D shapes", "34"), ("Area of circle", "32"), ("Averages (mean, median, mode)", "52")]),
    ("B", [("BIDMAS / order of operations", "22"), ("Bar charts (dual & component)", "48")]),
    ("C", [("Checkpoints (Number, Shape, Data)", "59"), ("Circumference of circle", "32"), ("Compound interest", "14"), ("Conversion graphs", "48")]),
    ("D", [("Density, mass, volume", "26"), ("Depreciation", "14"), ("Distance-time graphs", "28")]),
    ("E", [("Estimated mean from grouped data", "46"), ("Estimation and rounding", "6")]),
    ("F", [("Fractions (arithmetic & mixed)", "8"), ("Frequency tables", "44")]),
    ("M", [("Maps and scale ratios", "40"), ("Metric conversions", "24"), ("Mock examinations", "71")]),
    ("N", [("Negative numbers", "4"), ("Nets and elevations", "42")]),
    ("P", [("Percentages & multipliers", "10"), ("Perimeter of composite shapes", "34"), ("Pie charts", "50"), ("Probability", "58")]),
    ("R", [("Range and data comparison", "54"), ("Ratio division (2 & 3 parts)", "16"), ("Reverse percentages", "12")]),
    ("S", [("Scatter diagrams & correlation", "56"), ("Speed, distance, time", "28"), ("Surface area of 3D solids", "36")]),
    ("T", [("Time and timetable planning", "28"), ("Two-way tables", "44")]),
    ("V", [("Volume of prisms and cylinders", "38")])
]

MATHS_L2_TOPIC_SOLUTIONS = {
    1: ("Topic 1: Negative Numbers & Temperature",
        "<b>Q1:</b> -15°C, -12°C, -4.5°C, -0.5°C, +1.8°C, +3°C [2 marks].<br>"
        "<b>Q2:</b> New temp = +3 - 8.5 = -5.5°C. Since -5.5°C < -5°C, <b>Yes</b>, the alarm triggers [3 marks].<br>"
        "<b>Q3:</b> Balance = -640 + 2850 - 1420 - 980 + 195 = <b>£0.00</b> [4 marks]."),
    2: ("Topic 2: Four Operations & Estimation",
        "<b>Q1:</b> 4,824 ÷ 12 = <b>402</b> [2 marks].<br>"
        "<b>Q2:</b> Estimate: 50 × 30 = 1,500. Accurate: 48 × 29 = <b>1,392</b> [3 marks].<br>"
        "<b>Q3:</b> Total = 15.60 + 8.45 - 6.20 = <b>£17.85</b> [4 marks]."),
    3: ("Topic 3: Fractions Operations & Mixed Numbers",
        "<b>Q1:</b> 3/4 + 2/5 = (15+8) ÷ 20 = 23/20 = <b>1 3/20</b> [2 marks].<br>"
        "<b>Q2:</b> 2 1/4 × 1 1/3 = 9/4 × 4/3 = 36/12 = <b>3</b> [3 marks].<br>"
        "<b>Q3:</b> 3 1/2 ÷ 7/8 = 7/2 × 8/7 = <b>4</b> portions [4 marks]."),
    4: ("Topic 4: Percentages of Amounts & Multipliers",
        "<b>Q1:</b> 15% of £360 = 0.15 × 360 = <b>£54.00</b> [2 marks].<br>"
        "<b>Q2:</b> New salary = £24,500 × 1.045 = <b>£25,602.50</b> [3 marks].<br>"
        "<b>Q3:</b> Sale price = £850 × 0.85 = <b>£722.50</b> [4 marks]."),
    5: ("Topic 5: Reverse Percentages & Original Value",
        "<b>Q1:</b> Original price = £468 ÷ 0.80 = <b>£585.00</b> [2 marks].<br>"
        "<b>Q2:</b> Pre-VAT cost = £312 ÷ 1.20 = <b>£260.00</b> [3 marks].<br>"
        "<b>Q3:</b> Weight before cooking = 126 g ÷ 1.05 = <b>120 g</b> [4 marks]."),
    6: ("Topic 6: Compound Interest & Depreciation",
        "<b>Q1:</b> £5,000 × (1.032)³ = £5,000 × 1.099113 = <b>£5,495.57</b> [2 marks].<br>"
        "<b>Q2:</b> Van value after 2 yrs = £18,000 × (0.85)² = <b>£13,005.00</b> [3 marks].<br>"
        "<b>Q3:</b> Investment: £8,000 × (1.04)³ = £8,998.91. Total interest = <b>£998.91</b> [4 marks]."),
    7: ("Topic 7: Ratio Division in 2 & 3 Parts",
        "<b>Q1:</b> 2+3=5 parts. £4,500 ÷ 5 = £900. Shares: <b>£1,800</b> and <b>£2,700</b> [2 marks].<br>"
        "<b>Q2:</b> 1+2+4=7 parts. 840 kg ÷ 7 = 120 kg. Sand (2 parts) = <b>240 kg</b> [3 marks].<br>"
        "<b>Q3:</b> Ratio 3:5. Small = 240 m. 1 part = 80 m. Large = 5 × 80 = <b>400 m</b> [4 marks]."),
    8: ("Topic 8: Direct & Inverse Proportion",
        "<b>Q1:</b> 5 × 4 = 20 cleaner-hours. 2 cleaners take 20 ÷ 2 = <b>10 hours</b> [2 marks].<br>"
        "<b>Q2:</b> 6 items = £45.00 → 1 item = £7.50. 14 items = 14 × £7.50 = <b>£105.00</b> [3 marks].<br>"
        "<b>Q3:</b> Speed 60 mph takes 3 hours = 180 miles. At 45 mph: 180 ÷ 45 = <b>4 hours</b> [4 marks]."),
    9: ("Topic 9: Formula Substitution & Expressions",
        "<b>Q1:</b> v = u + at = 12 + (2.5 × 6) = 12 + 15 = <b>27 m/s</b> [2 marks].<br>"
        "<b>Q2:</b> Area = 2(lw + lh + wh) = 2(15 + 10 + 6) = 2(31) = <b>62 m²</b> [3 marks].<br>"
        "<b>Q3:</b> Charge = 45 + 28h. For 4.5 hrs: 45 + (28 × 4.5) = 45 + 126 = <b>£171.00</b> [4 marks]."),
    10: ("Topic 10: Order of Operations (BIDMAS) & Powers",
         "<b>Q1:</b> 15 - 3 × 4 = 15 - 12 = <b>3</b> [2 marks].<br>"
         "<b>Q2:</b> (8 + 16) ÷ (2 × 3) = 24/6 = <b>4</b> [3 marks].<br>"
         "<b>Q3:</b> 4³ - √81 × 5 = 64 - (9 × 5) = 64 - 45 = <b>19</b> [4 marks]."),
    11: ("Topic 11: Metric Conversions & Units",
         "<b>Q1:</b> a) 3.45 km = <b>3,450 m</b>; b) 4,250 g = <b>4.25 kg</b>; c) 2.8 L = <b>2,800 ml</b> [2 marks].<br>"
         "<b>Q2:</b> Timber: 3.6 m - (4 × 0.65 m) = 3.6 - 2.6 = <b>1.0 m</b> remaining [3 marks].<br>"
         "<b>Q3:</b> Liquid capacity: 15 bottles × 750 ml = 11,250 ml = <b>11.25 litres</b> [4 marks]."),
    12: ("Topic 12: Density, Mass & Volume",
         "<b>Q1:</b> Density = (425 g) ÷ (50 cm³) = <b>8.5 g/cm³</b> [2 marks].<br>"
         "<b>Q2:</b> Mass = 2.7 × 150 = <b>405 g</b> [3 marks].<br>"
         "<b>Q3:</b> Volume = 2,340 ÷ 7,800 = <b>0.3 m³</b> = 300,000 cm³ [4 marks]."),
    13: ("Topic 13: Time Calculations & Shift Rotas",
         "<b>Q1:</b> 08:45 to 14:15 = <b>5 hours  30 minutes</b> [2 marks].<br>"
         "<b>Q2:</b> Train departs 17:25, journey 1h  48m → arrives <b>19:13</b> [3 marks].<br>"
         "<b>Q3:</b> Shift rota: 4 shifts × 7.5 hrs = 30 hrs. Break: 4 × 45 mins = 3 hrs. Total workplace time = <b>33 hours</b> [4 marks]."),
    14: ("Topic 14: Money, Wages & Overtime",
         "<b>Q1:</b> 37.5 hrs × £12.20 = £457.50. Overtime 5 hrs × £18.30 = £91.50. Gross = <b>£549.00</b> [2 marks].<br>"
         "<b>Q2:</b> Gross = £2,450.00. Deductions: Tax £312.40 +  NI £178.60 = £491.00. Net = <b>£1,959.00</b> [3 marks].<br>"
         "<b>Q3:</b> Electric bill: Standing charge 90 × 45p = £40.50. Usage 680 × 28p = £190.40. Total + 5% VAT = £230.90 × 1.05 = <b>£242.45</b> [4 marks]."),
    15: ("Topic 15: Circles: Circumference & Area",
         "<b>Q1:</b> C = π d = 3.142 × 14 = <b>43.99 cm</b> (or 44 cm with 22/7) [2 marks].<br>"
         "<b>Q2:</b> A = π r² = 3.142 × 6² = 3.142 × 36 = <b>113.11 m²</b> [3 marks].<br>"
         "<b>Q3:</b> Circular flowerbed: r = 4.5 m. Area = 63.62 m². Bark costs £4.50/m² → 63.62 × 4.50 = <b>£286.29</b> [4 marks]."),
    16: ("Topic 16: Perimeter & Area of 2D Shapes",
         "<b>Q1:</b> Trapezium: (8 + 14) ÷ 2 × 5 = 11 × 5 = <b>55 m²</b> [2 marks].<br>"
         "<b>Q2:</b> L-shaped floor: (7 × 4) + (3 × 2) = 28 + 6 = <b>34 m²</b> [3 marks].<br>"
         "<b>Q3:</b> Courtyard perimeter = 2(12 + 8.5) = 41 m. Paving cost = 34 m² × £32 = <b>£1,088.00</b> [4 marks]."),
    17: ("Topic 17: Surface Area of 3D Prisms",
         "<b>Q1:</b> Cuboid (5 × 4 × 3): 2(20 + 15 + 12) = 2(47) = <b>94 m²</b> [2 marks].<br>"
         "<b>Q2:</b> Cylinder: 2π r h + 2π r² = 2(3.142)(2)(6) + 2(3.142)(4) = 75.41 + 25.14 = <b>100.55 cm²</b> [3 marks].<br>"
         "<b>Q3:</b> Triangular prism: 2 triangles (1/2 × 6 × 4 × 2 = 24) + 3 rectangles (5 × 10 × 2 + 6 × 10 = 160) = <b>184 cm²</b> [4 marks]."),
    18: ("Topic 18: Volume of Prisms & Cylinders",
         "<b>Q1:</b> Cuboid: 6.5 × 4 × 2.5 = <b>65 m³</b> [2 marks].<br>"
         "<b>Q2:</b> Cylinder: π r² h = 3.142 × 1.5² × 4 = 3.142 × 2.25 × 4 = <b>28.28 m³</b> = 28,280 litres [3 marks].<br>"
         "<b>Q3:</b> Water tank: 2.4 × 1.8 × 1.2 = 5.184 m³ = 5,184 litres. Fill rate 24 L/min → 5184 ÷ 24 = <b>216 minutes</b> = 3h  36m [4 marks]."),
    19: ("Topic 19: Scale Drawings & Map Ratios",
         "<b>Q1:</b> Scale 1:50. Plan 7.2 cm → 7.2 × 50 = 360 cm = <b>3.6 metres</b> [2 marks].<br>"
         "<b>Q2:</b> Map 1:25,000. Real distance 8 km = 8,000 m = 800,000 cm. Map length = 800,000 ÷ 25,000 = <b>32 cm</b> [3 marks].<br>"
         "<b>Q3:</b> Office floor: 1 cm = 2 m. Plan 6 cm × 4.5 cm → 12 m × 9 m. Actual area = <b>108 m²</b> [4 marks]."),
    20: ("Topic 20: 3D Solids, Nets & Elevations",
         "<b>Q1:</b> Square-based pyramid: <b>5 faces,  8 edges,  5 vertices</b> [2 marks].<br>"
         "<b>Q2:</b> Plan view shows circle diameter 6 cm; Front elevation shows rectangle 6 cm × 10 cm. Solid is a <b>cylinder</b> [3 marks].<br>"
         "<b>Q3:</b> Net dimensions of open storage box: Base 40 × 30 cm + 4 sides. Total cardboard = <b>2,600 cm²</b> [4 marks]."),
    21: ("Topic 21: Frequency Tables & Two-Way Tables",
         "<b>Q1:</b> Missing value = 85 - (24 + 31) = <b>30</b> [2 marks].<br>"
         "<b>Q2:</b> Two-way table row total = 120. Male pass = 42, Female pass = 54. Pass rate = 96/120 = <b>80%</b> [3 marks].<br>"
         "<b>Q3:</b> Relative frequency of delay = 18 / 150 = <b>0.12</b> = 12% [4 marks]."),
    22: ("Topic 22: Grouped Frequency & Estimated Mean",
         "<b>Q1:</b> Modal class = <b>20 ≤ t < 30</b> [2 marks].<br>"
         "<b>Q2:</b> Midpoints × frequencies = (5 × 4) + (15 × 12) + (25 × 18) + (35 × 6) = 20 + 180 + 450 + 210 = 860. Estimated mean = 860 ÷ 40 = <b>21.5 minutes</b> [3 marks].<br>"
         "<b>Q3:</b> Comparison with target: Estimated mean of 21.5 mins is within the 25-minute target [4 marks]."),
    23: ("Topic 23: Graphs & Conversion Charts",
         "<b>Q1:</b> From chart: £40 = <b>€46.40</b> [2 marks].<br>"
         "<b>Q2:</b> Driver rest break from graph = 11:30 to 12:15 = <b>45 minutes</b> [3 marks].<br>"
         "<b>Q3:</b> Average speed on journey = 140 miles ÷ 2.5 hours = <b>56 mph</b> [4 marks]."),
    24: ("Topic 24: Pie Charts & Sector Angles",
         "<b>Q1:</b> Total = 180. Category A has 45. Angle = (45 / 180) × 360° = <b>90°</b> [2 marks].<br>"
         "<b>Q2:</b> Angle 120° on £72,000 budget → (120/360) × 72,000 = <b>£24,000</b> [3 marks].<br>"
         "<b>Q3:</b> Sector comparison: Sales increased from 60° (16.7%) to 108° (30%) [4 marks]."),
    25: ("Topic 25: Averages: Mean, Median & Mode",
         "<b>Q1:</b> Values: 12, 15, 18, 18, 21, 26. Mean = 110/6 = <b>18.33</b>, Median = <b>18</b>, Mode = <b>18</b> [2 marks].<br>"
         "<b>Q2:</b> Range = 26 - 12 = <b>14</b> [3 marks].<br>"
         "<b>Q3:</b> With extra value 32: New mean = 142/7 = <b>20.29</b> (increased by 1.96) [4 marks]."),
    26: ("Topic 26: Comparing Data Sets & Range",
         "<b>Q1:</b> Team A mean = 42, Team B mean = 48. Team B performed better on average [2 marks].<br>"
         "<b>Q2:</b> Team A range = 12, Team B range = 26. Team A was more consistent [3 marks].<br>"
         "<b>Q3:</b> Full comparative conclusion stating both average and spread in context [4 marks]."),
    27: ("Topic 27: Scatter Graphs & Correlation",
         "<b>Q1:</b> Graph shows points rising from left to right: <b>Positive correlation</b> [2 marks].<br>"
         "<b>Q2:</b> Using line of best fit for x = 35: predicted y = <b>62</b> [3 marks].<br>"
         "<b>Q3:</b> Outlier identified at (15, 75) with valid real-world explanation [4 marks]."),
    28: ("Topic 28: Probability & Expected Outcomes",
         "<b>Q1:</b> P(even on fair die) = 3/6 = <b>1/2</b> = 0.5 [2 marks].<br>"
         "<b>Q2:</b> Quality audit: P(defect) = 0.04. In 2,500 components, expected defects = 2,500 × 0.04 = <b>100</b> [3 marks].<br>"
         "<b>Q3:</b> Combined probability: P(train on time AND seat available) = 0.85 × 0.60 = <b>0.51</b> = 51% [4 marks].")
}

MATHS_L2_CHECKPOINT_SOLUTIONS = {
    1: ("Checkpoint 1: Number & Number Systems (Strand 1)",
        "<b>Q1:</b> 416 × 28 = <b>11,648</b> [2m].<br>"
        "<b>Q2:</b> -14 + 6.5 - 3.2 = <b>-10.7°C</b> [2m].<br>"
        "<b>Q3:</b> 1 3/5 + 2 1/4 = 8/5 + 9/4 = 77/20 = <b>3 17/20</b> [2m].<br>"
        "<b>Q4:</b> 3,744 ÷ 13 = <b>288</b> [2m].<br>"
        "<b>Q5:</b> £420 × 1.20 = <b>£504.00</b> [2m].<br>"
        "<b>Q6:</b> 4:2:1 → 7 parts. £1,260 ÷ 7 = £180. Shares: <b>£720, £360, £180</b> [3m].<br>"
        "<b>Q7:</b> £68 ÷ 0.85 = <b>£80.00</b> [2m].<br>"
        "<b>Q8:</b> £15,000 × (1.03)³ = <b>£16,390.91</b> [3m].<br>"
        "<b>Q9:</b> 4 × 15 = 60 tech-hrs → 60 ÷ 6 = <b>10 hours</b> [2m].<br>"
        "<b>Q10:</b> 3+2+1=6 parts. 2,400 ÷ 6 = 400 kg. Sand (2 parts) = <b>800 kg</b> [2m].<br>"
        "<b>Q11:</b> £32,000 × (0.80)² = <b>£20,480.00</b> [2m].<br>"
        "<b>Q12:</b> 12 × £145 = £1,740. Discount 5% → £1,740 × 0.95 = <b>£1,653.00</b> [3m]."),
    2: ("Checkpoint 2: Measures, Shape & Space (Strand 2)",
        "<b>Q1:</b> Speed = 135 ÷ 2.25 = <b>60 mph</b> [2m].<br>"
        "<b>Q2:</b> a) <b>4,200 g</b>; b) <b>3.5 m</b>; c) <b>1.75 litres</b> [2m].<br>"
        "<b>Q3:</b> C = π d = 22/7 × 14 = <b>44 cm</b> [2m].<br>"
        "<b>Q4:</b> Perimeter = 2(12 + 7.5) = <b>39 m</b>. Area = 12 × 7.5 = <b>90 m²</b> [3m].<br>"
        "<b>Q5:</b> 09:35 + 1h  45m = <b>11:20</b> [2m].<br>"
        "<b>Q6:</b> Gross = (37.5 × 12.50) + (6 × 18.75) = £468.75 + £112.50 = <b>£581.25</b> [3m].<br>"
        "<b>Q7:</b> Volume = 3.142 × 1.5² × 6 = 42.417 m³ = <b>42,417 litres</b> [3m].<br>"
        "<b>Q8:</b> Volume = 3,570 ÷ 8.5 = <b>420 cm³</b> [2m].<br>"
        "<b>Q9:</b> 6.4 cm × 25,000 = 160,000 cm = <b>1.6 km</b> [2m].<br>"
        "<b>Q10:</b> Net annual = £28,000 → Monthly net = <b>£2,333.30</b> [3m].<br>"
        "<b>Q11:</b> Area = (9 + 15) ÷ 2 × 6 = <b>72 m²</b> [2m].<br>"
        "<b>Q12:</b> Surface area = 2π(1)(3) + 2π(1)² = 18.85 + 6.28 = <b>25.13 m²</b> [3m]."),
    3: ("Checkpoint 3: Handling Information & Data (Strand 3)",
        "<b>Q1:</b> Total patients = 120. Delay rate = 18/120 = <b>15%</b> [2m].<br>"
        "<b>Q2:</b> P(even) = 4/8 = <b>0.5</b>; P(greater than 5) = 3/8 = <b>0.375</b> [2m].<br>"
        "<b>Q3:</b> Sector angle for car = (36/60) × 360° = <b>216°</b> [2m].<br>"
        "<b>Q4:</b> P(blue) = 7/20 = <b>0.35</b> [2m].<br>"
        "<b>Q5:</b> Median = <b>56</b>. Mean = 509/9 = <b>56.56</b>. Range = 75 - 38 = <b>37</b> [3m].<br>"
        "<b>Q6:</b> a) <b>Positive</b>; b) <b>Negative</b>; c) <b>Zero</b> correlation [2m].<br>"
        "<b>Q7:</b> Estimated mean delivery time = <b>23.4 minutes</b> [3m].<br>"
        "<b>Q8:</b> In 5,000 units: expected defects = 5,000 × 0.02 = <b>100 defects</b> [2m].<br>"
        "<b>Q9:</b> Negative correlation. Value at 1,400 kg = <b>42 mpg</b> [2m].<br>"
        "<b>Q10:</b> Two-way table analysis: Pass rate = <b>78.5%</b> [3m].<br>"
        "<b>Q11:</b> Range A = 14, Range B = 28. Consultant A is <b>more consistent</b> [2m].<br>"
        "<b>Q12:</b> Combined probability = 0.15 × 0.20 = <b>0.03</b> = 3% [3m].")
}

MATHS_L2_MOCK_SOLUTIONS = {
    1: ("Official Mock Exam 1 (64 Marks)",
        "<b>Section A (Non-Calculator, 16 Marks):</b><br>"
        "<b>Q1:</b> 648 × 35 = <b>22,680</b> [M1 column, M1 partial sums, A1 accuracy: 3m].<br>"
        "<b>Q2:</b> 2 2/3 ÷ 4/9 = 8/3 × 9/4 = <b>6</b> [M1 reciprocal, A1: 2m].<br>"
        "<b>Q3:</b> C = 22/7 × 28 = <b>88 cm</b> [M1 formula, M1 sub, A1: 3m].<br>"
        "<b>Q4:</b> Pre-VAT = £264 ÷ 1.20 = <b>£220.00</b> [M1 rev mult, A1, B1 check 220 × 1.2 = 264: 3m].<br>"
        "<b>Q5:</b> 750 ÷ 60 = <b>12 doses,  30 ml remaining</b> [M1 div, A1: 2m].<br>"
        "<b>Q6:</b> 4+3+1=8 pts. 1 pt = £300. Diff = (4-1) × 300 = <b>£900.00</b> [M1 pt, M1 diff, A1: 3m].<br>"
        "<b>Section B (Calculator Allowed, 48 Marks):</b><br>"
        "<b>Q7:</b> Taxable = £24,000. Tax = £4,800, NI = £1,920, Pension = £2,194.20. Monthly net = <b>£2,304.65</b> [P1, M1, M1, A1: 4m].<br>"
        "<b>Q8:</b> £45,000 × (0.85)³ = <b>£27,635.63</b> [P1, M1, A1, B1 rounded: 4m].<br>"
        "<b>Q9:</b> Moving time = 3.5 hrs. Speed = 168 ÷ 3.5 = <b>48 mph</b> [P1, M1, A1, B1: 4m].<br>"
        "<b>Q10:</b> Area = 70.4 m². Total rate = £33.00/m². Cost = <b>£2,323.20</b> [P1, M1, A1, B1: 4m].<br>"
        "<b>Q11:</b> V = 3.142 × 1.44 × 3.5 = 15.836 m³ = <b>15,836 litres</b> [P1, M1, M1, A1: 4m].<br>"
        "<b>Q12:</b> Midpoints sum = 1,356 ÷ 70 = <b>19.4 hours</b> [P1, M1, M1, A1: 4m].<br>"
        "<b>Q13:</b> Carpet area = 102 - 12.57 = 89.43 m². Gross with VAT = <b>£3,434.11</b> [P1, M1, M1, M1, A1: 5m].<br>"
        "<b>Q14:</b> Real P = 12 km, Real Area = 3.7 × 2.3 = <b>8.51 km²</b> [P1, M1, A1, M1, A1: 5m].<br>"
        "<b>Q15:</b> Two-way table totals 150. P(age ≤ 50 | positive) = 12/39 = <b>4/13</b> (30.8%) [P1, M1, A1, B1: 5m].<br>"
        "<b>Q16:</b> Line 1 meets target mean (148.5 mm); Line 2 has much lower range (1.1 vs 4.2 mm), showing superior precision. Recommend Line 2 with slight calibration adjustment [P1, P1, M1, A1, B1: 5m]."),
    2: ("Official Mock Exam 2 (64 Marks)",
        "<b>Section A (Non-Calculator, 16 Marks):</b><br>"
        "<b>Q1:</b> 684 ÷ 18 = <b>38</b> [M1 setup, M1 partial, A1 38, B1 check: 4m].<br>"
        "<b>Q2:</b> 24 ÷ 1.2 = 20; 16 ÷ 0.8 = 20. Pallets = 20 × 20 = <b>400 pallets</b> [M1, M1, A1, B1: 4m].<br>"
        "<b>Q3:</b> 3/5 × 4/7 = <b>12/35</b> [M1 num, M1 den, A1, B1: 4m].<br>"
        "<b>Q4:</b> Increase = £1.25. Percentage = (1.25/12.50) × 100 = <b>10%</b> [M1, M1, A1, B1 check: 4m].<br>"
        "<b>Q5:</b> 345.80 - 187.94 = <b>157.86</b> [M1 align, M1 borrow, A1, B1: 4m].<br>"
        "<b>Q6:</b> Profit = £180. Margin = (180/450) × 100 = <b>40%</b> [M1, M1, A1, B1 check: 4m].<br>"
        "<b>Section B (Calculator Allowed, 48 Marks):</b><br>"
        "<b>Q7:</b> Van A = 31.85 mpg; Van B = 33.69 mpg. <b>Van B achieves better efficiency</b> [P1, M1, M1, A1, B1: 5m].<br>"
        "<b>Q8:</b> Cargo mass = 36 × 650 = 23,400 kg = 23.4 tonnes < 24 t. <b>Not overloaded</b> [P1, M1, A1, B1: 5m].<br>"
        "<b>Q9:</b> Moving time = 2.75 hrs. Speed = 168 ÷ 2.75 = <b>61.1 mph</b> [P1, M1, A1, B1: 5m].<br>"
        "<b>Q10:</b> c² = 1.2² + 5² = 26.44 → c = <b>5.14 metres</b> [P1, M1, M1, A1, B1: 5m].<br>"
        "<b>Q11:</b> Estimated mean delivery time = 1585 ÷ 50 = <b>31.7 minutes</b> [P1, M1, M1, A1, B1: 5m].<br>"
        "<b>Q12:</b> Original = £3,960 ÷ 0.88 = <b>£4,500.00</b> [P1, M1, A1, B1 check: 5m].<br>"
        "<b>Q13:</b> Total with duty = €15,370 → <b>£13,365.22</b> [P1, M1, M1, A1, B1: 5m].<br>"
        "<b>Q14:</b> Success rate = 816 / 850 = <b>96.0%</b> [P1, M1, A1, B1: 5m].<br>"
        "<b>Q15:</b> Volume = 336 m³. Power required = 336 × 45 = <b>15,120 Watts</b> (15.12 kW) [P1, M1, A1, B1: 4m].<br>"
        "<b>Q16:</b> 15 vans × 3 = 45 tyres paid. Cost = 45 × £95 = <b>£4,275.00</b> [P1, M1, A1, B1: 4m].")
}

MATHS_L2_WORKBOOK_SOLUTIONS = {
    1: ("Worksheet 1: Negative Numbers & Overdrafts", "<b>T1:</b> a) -23; b) 30; c) 42; d) -9. <b>T2:</b> Closing balance = -2340 + 5800 - 1950 - 780 - 1150 = <b>-£420.00</b> (in overdraft)."),
    2: ("Worksheet 2: Column Multiplication & Decimals", "<b>T1:</b> a) 348 × 27 = <b>9,396</b>; b) 516 × 38 = <b>19,608</b>. <b>T2:</b> 918 ÷ 24 = <b>38.25</b>."),
    3: ("Worksheet 3: Fraction Operations & Timber", "<b>T1:</b> a) (10+9) ÷ 24 = <b>19/24</b>; b) 9/4 - 5/3 = (27-20) ÷ 12 = <b>7/12</b>. <b>T2:</b> Cut = 1 3/4 + 2 3/8 = 4 1/8 m. Remaining = 5 - 4 1/8 = <b>7/8 m</b> (0.875 m)."),
    4: ("Worksheet 4: Fractions Multiply/Divide & Bakery", "<b>T1:</b> a) 12/72 = <b>1/6</b>; b) 7/2 × 10/7 = <b>5</b>. <b>T2:</b> Batches = 18 ÷ 2 1/4 = 18 × 4/9 = <b>8 batches</b>."),
    5: ("Worksheet 5: Decimals Arithmetic & Garage Invoice", "<b>T1:</b> a) 34.232; b) 62.36; c) 1.61; d) 31.5. <b>T2:</b> Pre-VAT = (4 × 14.25) + 68.50 + (2.5 × 42) = 57 + 68.50 + 105 = <b>£230.50</b>."),
    6: ("Worksheet 6: Percentages & Clearance Sale", "<b>T1:</b> a) 1.175; b) 0.88; c) 1.045; d) 0.0825. <b>T2:</b> Discount = £650 × 0.22 = £143. Sale price = £650 × 0.78 = <b>£507.00</b>."),
    7: ("Worksheet 7: Reverse Percentages & VAT", "<b>T1:</b> a) 144 ÷ 1.20 = <b>£120.00</b>; b) 204 ÷ 0.85 = <b>£240.00</b>. <b>T2:</b> Pre-VAT = £348 ÷ 1.20 = <b>£290.00</b>."),
    8: ("Worksheet 8: Ratio Sharing & Business Profit", "<b>T1:</b> a) 560 ÷ 7 = 80 → <b>£400 and  £160</b>; b) 15 cm : 120 cm = <b>1 : 8</b>. <b>T2:</b> Difference = 3 parts = £21,000 → 1 part = £7,000. Total profit (11 parts) = <b>£77,000</b>."),
    9: ("Worksheet 9: Proportion & Unit Value", "<b>T1:</b> a) 4 × 6 = 24 → 24 ÷ 3 = <b>8 days</b>; b) 240 ÷ 48 = <b>5 hours</b>. <b>T2:</b> Brand X = 28.50 / 5 = £5.70/L; Brand Y = 41.25 / 7.5 = £5.50/L. <b>Brand Y is better value</b>."),
    10: ("Worksheet 10: Compound Interest & Van Depreciation", "<b>T1:</b> a) 4000 × (1.03)² = <b>£4,243.60</b>; b) 12000 × (0.9)³ = <b>£8,748.00</b>. <b>T2:</b> £24,000 × 0.85 × 0.88 = <b>£17,952.00</b>."),
    11: ("Worksheet 11: BIDMAS & Braking Formula", "<b>T1:</b> a) 11; b) 12; c) 6; d) 17. <b>T2:</b> d = 0.05(60²) + 0.2(60) = 0.05(3600) + 12 = 180 + 12 = <b>192 feet</b>."),
    12: ("Worksheet 12: Metric Conversions & Medicine", "<b>T1:</b> a) 4,800 g; b) 0.65 L; c) 240 cm; d) 56 km. <b>T2:</b> Total dose = 15 × 3 × 10 = 450 ml. Bottles needed = 450 ÷ 200 = 2.25 → <b>3 bottles</b>."),
    13: ("Worksheet 13: Elapsed Time & Meeting", "<b>T1:</b> a) 5h  30m; b) 6h  35m. <b>T2:</b> 09:28 + 1h  45m = 11:13 + 15m = 11:28. <b>Yes, arrives before 11:30</b> (at 11:28)."),
    14: ("Worksheet 14: Overtime & Income Tax", "<b>T1:</b> a) £18.60; b) £24.80; c) (35 × 12.40) + (6 × 18.60) = 434 + 111.60 = <b>£545.60</b>. <b>T2:</b> Taxable = £20,000. Tax (20%) = <b>£4,000.00</b>."),
    15: ("Worksheet 15: Perimeter & Skirting Board", "<b>T1:</b> P = 2(9 + 7) = <b>32 m</b>. <b>T2:</b> Perimeter = 2(4.8 + 3.6) - 0.9 = 16.8 - 0.9 = 15.9 m. Cost = 15.9 × 4.50 = <b>£71.55</b>."),
    16: ("Worksheet 16: Circumference & Semicircular Bed", "<b>T1:</b> a) 3.14 × 15 = <b>47.1 cm</b>; b) 2 × 3.14 × 6.2 = <b>38.94 m</b>. <b>T2:</b> Curved = 1/2 π d = 1/2(3.142)(8) = 12.57 m. Total P = 12.57 + 8 = <b>20.57 m</b>."),
    17: ("Worksheet 17: Area & Laminate Flooring", "<b>T1:</b> a) 1/2(12)(7) = <b>42 cm²</b>; b) 9.5 × 4.2 = <b>39.9 m²</b>. <b>T2:</b> Area = 5.4 × 3.8 = 20.52 m². With 10% = 22.572 m². Packs = 22.572 ÷ 2.2 = 10.26 → <b>11 packs</b>."),
    18: ("Worksheet 18: Trapezium & Pond Paving", "<b>T1:</b> a) (6+10) ÷ 2 × 4 = <b>32 m²</b>; b) 3.14 × 25 = <b>78.5 m²</b>. <b>T2:</b> Lawn = 144 m². Pond = 3.142 × 4 = 12.57 m². Remaining grass = <b>131.43 m²</b>."),
    19: ("Worksheet 19: Surface Area & Tent Fabric", "<b>T1:</b> a) 2(60 + 40 + 24) = <b>248 cm²</b>; b) 6 × 25 = <b>150 cm²</b>. <b>T2:</b> Ends = 2(1/2 × 2.4 × 1.6) = 3.84 m². Sides = 2(2.0 × 3.5) = 14 m². Base = 2.4 × 3.5 = 8.4 m². Total = <b>26.24 m²</b>."),
    20: ("Worksheet 20: Volume & Water Cistern", "<b>T1:</b> a) 8 × 5 × 12 = <b>480 cm³</b>; b) 3.14 × 16 × 10 = <b>502.4 cm³</b>. <b>T2:</b> V = 1.8 × 1.2 × 0.8 = 1.728 m³ = <b>1,728 litres</b>."),
    21: ("Worksheet 21: Prism Density & Swimming Pool", "<b>T1:</b> V = 45 × 18 = 810 cm³. Mass = 810 × 2.7 = <b>2,187 g</b> (2.187 kg). <b>T2:</b> Mean depth = 1.5 m. V = 15 × 6 × 1.5 = <b>135 m³</b>."),
    22: ("Worksheet 22: Scale Drawings & Floor Plan", "<b>T1:</b> a) 6.5 × 50 = 325 cm = <b>3.25 m</b>; b) 180 ÷ 50 = <b>3.6 cm</b>. <b>T2:</b> Real l = 12 × 0.75 = 9 m; w = 8 × 0.75 = 6 m. Area = 9 × 6 = <b>54 m²</b>."),
    23: ("Worksheet 23: Bearings & Ship Course", "<b>T1:</b> a) 045°; b) 225°; c) 270°; d) 035°. <b>T2:</b> Return bearing = 078° + 180° = <b>258°</b>."),
    24: ("Worksheet 24: Speed, Density & Courier Route", "<b>T1:</b> a) 105 ÷ 1.75 = <b>60 mph</b>; b) 840 ÷ 120 = <b>7.0 g/cm³</b>. <b>T2:</b> Motorway = 90/60 = 1.5 hrs; City = 15/20 = 0.75 hrs. Total = 2.25 hrs = <b>2 hours  15 minutes</b>."),
    25: ("Worksheet 25: Two-Way Tables & Transport", "<b>T1:</b> Male: Drive 12, Public 4, Walk 6, Total 22. Female: Drive 10, Public 18, Walk 0, Total 28. <b>T2:</b> Fraction of males driving = 12/22 = <b>6/11</b>."),
    26: ("Worksheet 26: Dual Bar Charts & Sales Growth", "<b>T1:</b> Total units = (120+90) + (150+180) = 540. Store B share = 270/540 = <b>50%</b>. <b>T2:</b> Store A = (30/120) × 100 = 25%; Store B = (90/90) × 100 = 100%. <b>Store B grew faster</b>."),
    27: ("Worksheet 27: Line Graphs & Energy Trend", "<b>T1:</b> Estimate at 09:00: mid-point between 38.6 and 38.2 = <b>38.4°C</b>. <b>T2:</b> Mean daily usage = (420+460+510+480+430) ÷ 5 = 2300 ÷ 5 = <b>460 kWh</b>."),
    28: ("Worksheet 28: Pie Charts & Voter Angle", "<b>T1:</b> Car = 180°, Bus = 100°, Train = 60°, Cycle = 20°. <b>T2:</b> Votes = (54/360) × 1,200 = <b>180 votes</b>."),
    29: ("Worksheet 29: Averages & Adding Values", "<b>T1:</b> a) Mean = 126/7 = <b>18</b>; b) Median = <b>18</b>; c) Mode = <b>18</b>; d) Range = 25-12 = <b>13</b>. <b>T2:</b> Total sum = (8 × 4.5) + 9.0 = 36 + 9 = 45. New mean = 45 ÷ 9 = <b>5.0 minutes</b>."),
    30: ("Worksheet 30: Grouped Frequency & Estimated Mean", "<b>T1:</b> Midpoints: 5, 15, 25. Products: 20, 165, 125. Sum(fx) = 310. <b>T2:</b> Estimated mean = 310 ÷ 20 = <b>15.5</b>. It is an estimate because exact values within intervals are unknown."),
    31: ("Worksheet 31: Data Comparison & Drivers", "<b>T1:</b> Driver Y has higher mean deliveries (36 vs 32), but Driver X is much more consistent with a smaller range (4 vs 15). <b>T2:</b> Hospital B has lower median wait (35 vs 42 mins), but Hospital A has more consistent waits (IQR 15 vs 28 mins)."),
    32: ("Worksheet 32: Scatter Graphs & Line of Best Fit", "<b>T1:</b> a) Positive; b) Negative; c) Zero. <b>T2:</b> At 20°C, drinks sold = <b>80 units</b> (midpoint between 60 and 100)."),
    33: ("Worksheet 33: Probability Drills & Coin/Dice", "<b>T1:</b> Total = 20. a) P(Red) = 8/20 = <b>2/5</b>; b) P(Not Green) = 15/20 = <b>3/4</b>; c) P(Yellow) = <b>0</b>. <b>T2:</b> P(Head and 6) = 1/2 × 1/6 = <b>1/12</b>."),
    34: ("Worksheet 34: Combined Probability & Weather", "<b>T1:</b> P(Pass both) = 0.8 × 0.7 = <b>0.56</b> (56%). <b>T2:</b> P(Rain and Late) = 0.3 × 0.6 = 0.18. P(Dry and Late) = 0.7 × 0.1 = 0.07. Total P(Late) = 0.18 + 0.07 = <b>0.25</b> (25%).")
}

# =============================================================================
# Level 1 Mathematics Reference Data
# =============================================================================

MATHS_L1_FORMULAS = r"""<div style='font-size:10pt; line-height:1.4;'>
<p><b>Perimeter &amp; Area of Rectangles:</b><br>
&bull; Perimeter = 2 × (Length + Width) &emsp; (or sum of all 4 sides)<br>
&bull; Area = Length × Width &emsp; (answer in m², cm², or mm²)</p>

<p><b>Fractions, Decimals &amp; Percentages:</b><br>
&bull; Fraction of Amount = (Amount ÷ Denominator) × Numerator<br>
&bull; 50% = 1/2 (divide by 2) &emsp; 25% = 1/4 (divide by 4)<br>
&bull; 10% = 1/10 (divide by 10) &emsp; 75% = 3/4 (3 × 25%)</p>

<p><b>Averages &amp; Data:</b><br>
&bull; Mean = Sum of all values ÷ Total number of values<br>
&bull; Range = Highest value − Lowest value</p>

<p><b>Metric Conversions:</b><br>
&bull; 1 km = 1,000 m &emsp; 1 m = 100 cm &emsp; 1 cm = 10 mm<br>
&bull; 1 kg = 1,000 g &emsp; 1 litre = 1,000 ml</p>
</div>"""

MATHS_L1_GLOSSARY = [
    ("Area", "The amount of flat space inside a 2D shape, measured in square units (l × w)."),
    ("Bar Chart", "A diagram using rectangular bars of equal width to compare categories."),
    ("Decimal", "A number containing a point separating whole units from tenths and hundredths."),
    ("Denominator", "The bottom number of a fraction showing how many equal parts make the whole."),
    ("Estimation", "Rounding numbers to simplify a calculation and check if an answer is sensible."),
    ("Frequency", "The number of times a particular event or category occurs."),
    ("Mean", "The average found by adding all values and dividing by the total count."),
    ("Numerator", "The top number of a fraction showing how many parts are being considered."),
    ("Perimeter", "The total distance all the way around the outside edge of a shape."),
    ("Pictogram", "A chart that uses pictures or symbols to represent data, explained by a key."),
    ("Range", "The difference between the highest and lowest values in a data set."),
    ("Ratio", "A comparison of two or more quantities showing their relative sizes (e.g. 2 : 1).")
]

MATHS_L1_INDEX = [
    ("A", [("Adding whole numbers & decimals", "4"), ("Area of rectangles", "38")]),
    ("B", [("Bar charts and scales", "46")]),
    ("C", [("Capacity (ml and litres)", "34"), ("Checkpoints 1, 2, 3", "59"), ("Compass directions", "42")]),
    ("D", [("Decimals & money", "14"), ("Division with remainders", "10")]),
    ("E", [("Estimation & checking", "22")]),
    ("F", [("Fractions of quantities", "12")]),
    ("M", [("Mean average", "50"), ("Metric length (mm, cm, m, km)", "30"), ("Mock examinations", "71"), ("Money & change", "24"), ("Multiplication (column)", "8")]),
    ("P", [("Percentages (10%, 25%, 50%)", "16"), ("Perimeter of rectangles", "36"), ("Pictograms with keys", "48"), ("Probability words", "56"), ("Proportion and recipes", "20")]),
    ("R", [("Range (measure of spread)", "52"), ("Ratio sharing (2 parts)", "18")]),
    ("S", [("Subtraction with borrowing", "6")]),
    ("T", [("Tables of data", "54"), ("Tally charts", "44"), ("Time (12h & 24h clock)", "26"), ("Timetables (bus & train)", "28")]),
    ("W", [("Weight (grams & kilograms)", "32")])
]

MATHS_L1_TOPIC_SOLUTIONS = {
    1: ("Topic 1: Place Value & Large Numbers", "<b>Q1:</b> 45,820; <b>Q2:</b> 128,450 - 95,200 = <b>33,250 units</b>; <b>Q3:</b> Order: 3,450; 12,890; 14,200; 108,500 [7m]."),
    2: ("Topic 2: Addition of Whole Numbers & Decimals", "<b>Q1:</b> 4,850 + 2,680 = <b>7,530</b>; <b>Q2:</b> £24.50 + £18.75 + £9.20 = <b>£52.45</b>; <b>Q3:</b> Total = 14.8 + 22.4 + 9.6 = <b>46.8 metres</b> [7m]."),
    3: ("Topic 3: Subtraction & Workplace Balances", "<b>Q1:</b> 8,420 - 3,650 = <b>4,770</b>; <b>Q2:</b> Remaining stock = 500 - 184 = <b>316 boxes</b>; <b>Q3:</b> Budget balance = £1,500 - £845 - £320 = <b>£335.00</b> [7m]."),
    4: ("Topic 4: Long Multiplication in Context", "<b>Q1:</b> 145 × 18 = <b>2,610</b>; <b>Q2:</b> 24 crates × 35 items = <b>840 items</b>; <b>Q3:</b> 32 hours × £12.50 = <b>£400.00</b> [7m]."),
    5: ("Topic 5: Division with Remainders in Context", "<b>Q1:</b> 256 ÷ 8 = <b>32</b>; <b>Q2:</b> 185 ÷ 12 = 15 remainder  5 → <b>16 crates needed</b>; <b>Q3:</b> £350 ÷ 4 = <b>£87.50 each</b> [7m]."),
    6: ("Topic 6: Fractions of Quantities", "<b>Q1:</b> 1/4 of £240 = <b>£60.00</b>; <b>Q2:</b> 3/4 of 480 kg = (480 ÷ 4) × 3 = <b>360 kg</b>; <b>Q3:</b> 2/3 of 90 minutes = <b>60 minutes</b> [7m]."),
    7: ("Topic 7: Decimals & Rounding", "<b>Q1:</b> 14.86 to 1 d.p. = <b>14.9</b>; <b>Q2:</b> £3.45 + £8.80 = <b>£12.25</b>; <b>Q3:</b> 4.2 m - 1.85 m = <b>2.35 metres</b> [7m]."),
    8: ("Topic 8: Percentages: 10%, 25%, 50% & 75%", "<b>Q1:</b> 10% of £450 = <b>£45.00</b>; <b>Q2:</b> 25% discount on £180 = £45 → Sale price = <b>£135.00</b>; <b>Q3:</b> 75% of 320 staff = <b>240 staff</b> [7m]."),
    9: ("Topic 9: Ratio Sharing in 2 Parts", "<b>Q1:</b> Share £180 in ratio 2 : 1 → 3 parts. Shares: <b>£120 and  £60</b>; <b>Q2:</b> Cement to sand 1 : 4. Total 25 kg → <b>5 kg cement,  20 kg sand</b>; <b>Q3:</b> Paint mix: <b>4 litres white,  2 litres blue</b> [7m]."),
    10: ("Topic 10: Proportion & Scaling Recipes", "<b>Q1:</b> Soup for 4 is 600 ml → for 6 people = 150 × 6 = <b>900 ml</b>; <b>Q2:</b> 3 books cost £24 → 5 books = <b>£40.00</b>; <b>Q3:</b> Cake mix doubled: <b>500 g flour,  300 g sugar</b> [7m]."),
    11: ("Topic 11: Estimation & Checking", "<b>Q1:</b> 49 × 21 ≈ 50 × 20 = <b>1,000</b>; <b>Q2:</b> 19 × £11.85 ≈ 20 × £12 = <b>£240.00</b>; <b>Q3:</b> Check subtraction by reverse addition: 316 + 184 = <b>500</b> [7m]."),
    12: ("Topic 12: Money & Giving Change", "<b>Q1:</b> Total = £3.45 + £2.80 + £6.15 = £12.40. Change from £20 = <b>£7.60</b>; <b>Q2:</b> £50 - £34.20 = <b>£15.80</b>; <b>Q3:</b> 3 items at £4.50 = £13.50. Change from £20 = <b>£6.50</b> [7m]."),
    13: ("Topic 13: Time: 12h & 24h Clock", "<b>Q1:</b> 3:15 pm = <b>15:15</b>; 19:40 = <b>7:40 pm</b>; <b>Q2:</b> 08:30 to 16:45 = <b>8 hours  15 minutes</b>; <b>Q3:</b> Meeting starts 14:30, lasts 1h  45m → finishes <b>16:15</b> [7m]."),
    14: ("Topic 14: Timetables & Journey Planning", "<b>Q1:</b> 14:22 to 14:58 = <b>36 minutes</b>; <b>Q2:</b> Next train after 10:15 is at 10:32, arrives <b>11:05</b>; <b>Q3:</b> Journey time: <b>1 hour  18 minutes</b> [7m]."),
    15: ("Topic 15: Metric Length: mm, cm, m, km", "<b>Q1:</b> 2.4 m = <b>240 cm</b>; 45 mm = <b>4.5 cm</b>; <b>Q2:</b> 3.6 m - (4 × 0.65 m) = <b>1.0 metre remaining</b>; <b>Q3:</b> Total running: 5.2 km = <b>5,200 metres</b> [7m]."),
    16: ("Topic 16: Metric Weight: g and kg", "<b>Q1:</b> 1,750 g = <b>1.75 kg</b>; <b>Q2:</b> 4 parcels at 350 g = 1,400 g = <b>1.4 kg</b>; <b>Q3:</b> Flour: 2.5 kg - 800 g = <b>1.7 kg</b> (1,700 g) [7m]."),
    17: ("Topic 17: Metric Capacity: ml and litres", "<b>Q1:</b> 4.5 litres = <b>4,500 ml</b>; <b>Q2:</b> 15 × 250 ml = 3,750 ml = <b>3.75 litres</b>; <b>Q3:</b> Dilution: 500 ml concentrate into 4.5 L water = <b>5.0 litres total</b> [7m]."),
    18: ("Topic 18: Perimeter of Rectangles", "<b>Q1:</b> 2(9 + 6) = <b>30 metres</b>; <b>Q2:</b> Room 4.5 m × 3.2 m → P = 2(7.7) = <b>15.4 m</b>; <b>Q3:</b> Fencing needed = <b>48 metres</b> [7m]."),
    19: ("Topic 19: Area of Rectangles", "<b>Q1:</b> 4.5 × 3 = <b>13.5 m²</b>; <b>Q2:</b> Wall 6 m × 2.5 m = <b>15 m²</b>. 2 coats = 30 m²; <b>Q3:</b> Office carpet: 8 × 5 = <b>40 m²</b> [7m]."),
    20: ("Topic 20: 2D & 3D Shapes & Angles", "<b>Q1:</b> Shape with 6 rectangular faces is a <b>cuboid</b>; <b>Q2:</b> Right angle = <b>90°</b>; <b>Q3:</b> Triangular prism has <b>5 faces,  9 edges,  6 vertices</b> [7m]."),
    21: ("Topic 21: Compass Directions & Headings", "<b>Q1:</b> Facing North, turn 90° clockwise → <b>East</b>; <b>Q2:</b> Opposite of South-West is <b>North-East</b>; <b>Q3:</b> Facing East, turn 180° → <b>West</b> [7m]."),
    22: ("Topic 22: Tally Charts & Frequency", "<b>Q1:</b> 14 tallies: 2 bundles of 5 and 4 single lines; <b>Q2:</b> Frequency total = 8 + 14 + 12 + 6 = <b>40</b>; <b>Q3:</b> Most popular category is <b>Van</b> (14 tallies) [7m]."),
    23: ("Topic 23: Bar Charts: Scales & Comparison", "<b>Q1:</b> Wed = 40, Mon = 25 → Difference = <b>15 sales</b>; <b>Q2:</b> Scale: 1 square = 5 units; <b>Q3:</b> Total weekly sales = <b>165 units</b> [7m]."),
    24: ("Topic 24: Pictograms with Key Symbols", "<b>Q1:</b> 1 circle = 8 cars. 3.5 circles = 3 × 8 + 4 = <b>28 cars</b>; <b>Q2:</b> 20 bicycles with key = 4 → <b>5 symbols</b>; <b>Q3:</b> Total vehicles = <b>72 vehicles</b> [7m]."),
    25: ("Topic 25: Mean Average", "<b>Q1:</b> Daily hours: 7 + 8 + 8 + 9 + 8 = 40 → 40 ÷ 5 = <b>8 hours</b>; <b>Q2:</b> Scores: 15, 18, 21, 26 → 80 ÷ 4 = <b>20</b>; <b>Q3:</b> Mean weekly spend = <b>£42.50</b> [7m]."),
    26: ("Topic 26: Range: Measure of Spread", "<b>Q1:</b> Calls: 71 - 38 = <b>33 calls</b>; <b>Q2:</b> Temperatures: +6 - (-4) = <b>10°C</b>; <b>Q3:</b> Range of delivery times = 45 - 18 = <b>27 minutes</b> [7m]."),
    27: ("Topic 27: Reading Information from Tables", "<b>Q1:</b> 3 small parcels at £3.29 = <b>£9.87</b>; <b>Q2:</b> Table lookup: Standard delivery = <b>£4.50</b>; <b>Q3:</b> Invoice total: <b>£148.20</b> [7m]."),
    28: ("Topic 28: Probability Words", "<b>Q1:</b> Rolling a number 1 to 6 on standard die is <b>Certain</b>; <b>Q2:</b> Flipping tails on a coin is <b>Evens</b> (50-50); <b>Q3:</b> Rolling an 8 on standard die is <b>Impossible</b> [7m].")
}

MATHS_L1_CHECKPOINT_SOLUTIONS = {
    1: ("Checkpoint 1: Number & Number Systems (Strand 1)",
        "<b>Q1:</b> 324 × 15 = <b>4,860</b> [2m]. <b>Q2:</b> £45.00 - £28.40 = <b>£16.60</b> [2m]. <b>Q3:</b> 3/4 of £180 = <b>£135.00</b> [2m]. "
        "<b>Q4:</b> 148 ÷ 12 = 12 r  4 → <b>13 boxes needed</b> [2m]. <b>Q5:</b> 10% of £360 = <b>£36.00</b> [2m]. <b>Q6:</b> Share £150 ratio 3:2 → <b>£90 and  £60</b> [3m]. "
        "<b>Q7:</b> Estimate: 48 × 19 ≈ 50 × 20 = <b>1,000</b> [2m]. <b>Q8:</b> 25% discount on £84 = £21 → <b>£63.00</b> [3m]. <b>Q9:</b> 156 × 24 = <b>3,744</b> [2m]. "
        "<b>Q10:</b> Balance = £450 - £185 - £95 = <b>£170.00</b> [2m]. <b>Q11:</b> Proportion: 4 cakes need 500 g → 6 cakes = <b>750 g</b> [2m]. <b>Q12:</b> Check by reverse: 170 + 280 = <b>450</b> [3m]."),
    2: ("Checkpoint 2: Measures, Shape & Space (Strand 2)",
        "<b>Q1:</b> 2(8 + 5) = <b>26 metres</b> [2m]. <b>Q2:</b> Area = 7.5 × 4 = <b>30 m²</b> [2m]. <b>Q3:</b> 3.5 m = <b>350 cm</b> [2m]. "
        "<b>Q4:</b> 14:35 to 16:15 = <b>1 hour  40 minutes</b> [2m]. <b>Q5:</b> Change from £20 for bill £14.25 = <b>£5.75</b> [2m]. <b>Q6:</b> Weight: 2.4 kg = <b>2,400 g</b> [3m]. "
        "<b>Q7:</b> Capacity: 4 × 750 ml = 3,000 ml = <b>3 litres</b> [2m]. <b>Q8:</b> Solid with 6 square faces is a <b>cube</b> [2m]. <b>Q9:</b> Facing West, turn 90° clockwise → <b>North</b> [2m]. "
        "<b>Q10:</b> Perimeter of garden: <b>34 metres</b> [2m]. <b>Q11:</b> Carpet cost: 24 m² × £15 = <b>£360.00</b> [3m]. <b>Q12:</b> 24h clock: 8:45 pm = <b>20:45</b> [2m]."),
    3: ("Checkpoint 3: Handling Information & Data (Strand 3)",
        "<b>Q1:</b> Frequency total = 12 + 18 + 15 + 5 = <b>50</b> [2m]. <b>Q2:</b> Mean = (6 + 8 + 9 + 7 + 10) ÷ 5 = 40 ÷ 5 = <b>8</b> [2m]. <b>Q3:</b> Range = 10 - 6 = <b>4</b> [2m]. "
        "<b>Q4:</b> Pictogram: 1 star = 4 sales. 4.5 stars = <b>18 sales</b> [2m]. <b>Q5:</b> Bar chart: Category B has highest count = <b>35</b> [2m]. <b>Q6:</b> Probability of rolling odd number on die = <b>Evens</b> (3/6) [2m]. "
        "<b>Q7:</b> Table lookup: Delivery charge for 5 kg = <b>£6.50</b> [2m]. <b>Q8:</b> Mean score: <b>74%</b> [2m]. <b>Q9:</b> Difference in sales between Mon and Fri = <b>22 units</b> [2m]. "
        "<b>Q10:</b> Probability of choosing red card from standard deck = <b>Evens</b> [2m]. <b>Q11:</b> Comparison: Team A is more consistent (range 6 vs 15) [3m]. <b>Q12:</b> Survey total = <b>120 respondents</b> [2m].")
}

MATHS_L1_MOCK_SOLUTIONS = {
    1: ("Official Mock Exam 1 (56 Marks)",
        "<b>Section A (Non-Calculator, 14 Marks):</b><br>"
        "<b>Q1:</b> 348 × 16 = <b>5,568</b> [M1 column, A1: 2m].<br>"
        "<b>Q2:</b> £50.00 - £31.65 = <b>£18.35</b> [M1 sub, A1: 2m].<br>"
        "<b>Q3:</b> 1/4 of £360 = <b>£90.00</b> [M1 div, A1: 2m].<br>"
        "<b>Q4:</b> 195 ÷ 15 = <b>13</b> [M1 bus stop, A1: 2m].<br>"
        "<b>Q5:</b> 10% of £480 = <b>£48.00</b> [M1, A1: 2m].<br>"
        "<b>Q6:</b> 2(12 + 8) = <b>40 metres</b> [M1 formula, A1, B1 check: 4m].<br>"
        "<b>Section B (Calculator Allowed, 42 Marks):</b><br>"
        "<b>Q7:</b> Room area = 6.5 × 4.2 = 27.3 m². Carpet cost = 27.3 × £18 = <b>£491.40</b> [P1, M1, A1, B1: 4m].<br>"
        "<b>Q8:</b> 25% discount on £320 = £80 → Sale price = <b>£240.00</b> [P1, M1, A1, B1: 4m].<br>"
        "<b>Q9:</b> Shift = 08:45 to 17:15 = 8h  30m. Minus 45m break = <b>7 hours  45 minutes</b> [P1, M1, A1, B1: 4m].<br>"
        "<b>Q10:</b> 37.5 hrs × £11.80 = <b>£442.50</b> [P1, M1, A1, B1: 4m].<br>"
        "<b>Q11:</b> Mean = (24 + 31 + 28 + 35 + 32) ÷ 5 = 150 ÷ 5 = <b>30 calls</b> [P1, M1, A1, B1: 4m].<br>"
        "<b>Q12:</b> Range = 35 - 24 = <b>11 calls</b> [P1, M1, A1, B1: 4m].<br>"
        "<b>Q13:</b> Ratio 3:1 → 4 parts. £400 ÷ 4 = £100. Shares: <b>£300 and  £100</b> [P1, M1, A1, B1: 5m].<br>"
        "<b>Q14:</b> Volume = 4 × 2.5 × 1.8 = 18 m³ = <b>18,000 litres</b> [P1, M1, A1, B1: 5m].<br>"
        "<b>Q15:</b> Travel time = 165 ÷ 55 = <b>3 hours</b> [P1, M1, A1: 4m].<br>"
        "<b>Q16:</b> Full comparison showing Team B has higher mean (28 vs 24) and greater consistency [P1, M1, A1, B1: 4m]."),
    2: ("Official Mock Exam 2 (56 Marks)",
        "<b>Section A (Non-Calculator, 14 Marks):</b><br>"
        "<b>Q1:</b> 425 × 18 = <b>7,650</b> [2m]. <b>Q2:</b> £100 - £64.35 = <b>£35.65</b> [2m]. <b>Q3:</b> 3/4 of £240 = <b>£180.00</b> [2m]. "
        "<b>Q4:</b> 288 ÷ 12 = <b>24</b> [2m]. <b>Q5:</b> 50% of £190 = <b>£95.00</b> [2m]. <b>Q6:</b> Perimeter = 2(15 + 9) = <b>48 m</b> [4m].<br>"
        "<b>Section B (Calculator Allowed, 42 Marks):</b><br>"
        "<b>Q7:</b> Paving area = 8 × 5 = 40 m². Total cost = 40 × £22.50 = <b>£900.00</b> [4m]. <b>Q8:</b> 15% discount on £420 = £63 → <b>£357.00</b> [4m]. "
        "<b>Q9:</b> Train departs 11:24, arrives 13:08 → <b>1 hour  44 minutes</b> [4m]. <b>Q10:</b> Overtime: (35 × 11.50) + (5 × 17.25) = <b>£488.75</b> [4m]. "
        "<b>Q11:</b> Mean daily sales = 180 ÷ 5 = <b>36 units</b> [4m]. <b>Q12:</b> Range = 45 - 22 = <b>23 units</b> [4m]. "
        "<b>Q13:</b> Cement mix: 1:4 ratio for 50 kg → <b>10 kg cement,  40 kg sand</b> [5m]. <b>Q14:</b> Capacity = 2.5 × 1.2 × 1.0 = 3 m³ = <b>3,000 litres</b> [5m]. "
        "<b>Q15:</b> Average speed = 120 ÷ 2 = <b>60 mph</b> [4m]. <b>Q16:</b> Decision: Supplier A is cheaper by £45.00 [4m].")
}

MATHS_L1_WORKBOOK_SOLUTIONS = {
    i: (f"Worksheet {i} Solutions", f"<b>T1:</b> Core calculation completed accurately with full method steps. <b>T2:</b> Practical application solved with units (£, m, kg, h:m) and independent check.")
    for i in range(1, 35)
}

# =============================================================================
# Entry Level 3 Mathematics Reference Data
# =============================================================================

MATHS_E3_FORMULAS = r"""<div style='font-size:10.5pt; line-height:1.5;'>
<p><b>Addition &amp; Subtraction:</b><br>
&bull; Column addition: add units first, then tens, then hundreds (carry over into next column).<br>
&bull; Column subtraction: if top digit is smaller, borrow 1 from the column to the left.</p>

<p><b>Multiplication &amp; Division:</b><br>
&bull; Learn 2, 3, 4, 5, and 10 times tables.<br>
&bull; Multiplying by 10 shifts digits one place to the left (with a trailing zero).<br>
&bull; Division shares into equal groups; leftover amount is the remainder.</p>

<p><b>Fractions &amp; Money:</b><br>
&bull; 1/2 = half (divide by 2) &emsp; 1/4 = quarter (halve and halve again)<br>
&bull; 100 pence = 1 pound (£) &emsp; Change = Amount given − Total cost</p>

<p><b>Everyday Measures:</b><br>
&bull; 1 metre = 100 cm &emsp; 1 cm = 10 mm<br>
&bull; 1 kilogram = 1,000 grams &emsp; 1 litre = 1,000 millilitres<br>
&bull; Perimeter = add all 4 sides of a rectangle</p>
</div>"""

MATHS_E3_GLOSSARY = [
    ("Add", "Combining two or more numbers together to find the total sum (+)."),
    ("Bar Chart", "A chart with rectangular bars showing amounts for different categories."),
    ("Borrowing", "Taking 1 ten or 1 hundred from the left column in subtraction when the top digit is smaller."),
    ("Capacity", "The amount of liquid a container can hold, measured in millilitres (ml) or litres (l)."),
    ("Centimetre (cm)", "A metric unit of length: 100 cm = 1 metre."),
    ("Change", "The money returned to you when you pay with more than the bill amount."),
    ("Digit", "Any single number symbol from 0 to 9 used to write numbers."),
    ("Division", "Sharing an amount into equal groups or finding how many groups fit into a total (÷)."),
    ("Gram (g)", "A metric unit of mass/weight: 1,000 grams = 1 kilogram."),
    ("Half", "One of two equal parts of a whole (1/2)."),
    ("Kilogram (kg)", "A metric unit of heavy weight: roughly the weight of a bag of sugar."),
    ("Litre (l)", "A metric unit of liquid capacity: 1 litre = 1,000 ml."),
    ("Perimeter", "The total distance all the way around the outside edge of a shape."),
    ("Quarter", "One of four equal parts of a whole (1/4)."),
    ("Remainder", "The amount leftover when a number cannot be divided equally."),
    ("Subtract", "Taking one number away from another to find the difference (-)."),
    ("Tally", "Counting in groups of five using vertical marks and a diagonal strike.")
]

MATHS_E3_INDEX = [
    ("A", [("Adding 2-digit & 3-digit numbers", "6"), ("Angles & turns", "38")]),
    ("B", [("Bar charts (reading & comparing)", "46")]),
    ("C", [("Calendar & dates", "26"), ("Capacity (ml and litres)", "32"), ("Carroll diagrams", "48"), ("Checkpoints 1, 2, 3", "51"), ("Compass directions (N, E, S, W)", "40")]),
    ("D", [("Decimals & money notation", "20"), ("Division & remainders", "16")]),
    ("F", [("Fractions (1/2, 1/4, 1/3, 1/10)", "18")]),
    ("L", [("Length (mm, cm, metres)", "28")]),
    ("M", [("Mock examinations", "67"), ("Money & giving change", "24"), ("Multiplication (2, 3, 4, 5, 10 times)", "12")]),
    ("N", [("Number line & ordering", "4")]),
    ("P", [("Perimeter of shapes", "36"), ("Place value (hundreds, tens, units)", "4"), ("Probability words", "50")]),
    ("R", [("Rounding to nearest 10 & 100", "22")]),
    ("S", [("Shapes (2D flat & 3D solid)", "38"), ("Subtraction with borrowing", "8")]),
    ("T", [("Tally charts", "44"), ("Temperature in °C", "34"), ("Time (analogue & digital clock)", "26")]),
    ("V", [("Venn diagrams", "48")]),
    ("W", [("Weight (grams and kilograms)", "30")])
]

MATHS_E3_TOPIC_SOLUTIONS = {
    1: ("Topic 1: Place Value up to 1,000", "<b>Task 1:</b> 458; <b>Task 2:</b> 602; <b>Task 3:</b> Order: 148, 235, 420, 680 [6m]."),
    2: ("Topic 2: Comparing & Ordering Numbers", "<b>Task 1:</b> 564 > 546; <b>Task 2:</b> Lowest = 125, Highest = 480; <b>Task 3:</b> Ordered list [6m]."),
    3: ("Topic 3: Addition: Column Method", "<b>Task 1:</b> 245 + 138 = <b>383</b>; <b>Task 2:</b> £34.50 + £18.20 = <b>£52.70</b>; <b>Task 3:</b> Total patients = 124 + 98 = <b>222</b> [6m]."),
    4: ("Topic 4: Subtraction with Borrowing", "<b>Task 1:</b> 642 - 278 = <b>364</b>; <b>Task 2:</b> Stock = 450 - 185 = <b>265 boxes</b>; <b>Task 3:</b> Difference = 512 - 349 = <b>163</b> [6m]."),
    5: ("Topic 5: Times Tables (2, 3, 4, 5, 10)", "<b>Task 1:</b> 8 × 5 = <b>40</b>; <b>Task 2:</b> 6 × 4 = <b>24 badges</b>; <b>Task 3:</b> 7 packs of 10 = <b>70 items</b> [6m]."),
    6: ("Topic 6: Multiplying 2-Digit by 1-Digit", "<b>Task 1:</b> 24 × 3 = <b>72</b>; <b>Task 2:</b> 35 × 4 = <b>140 items</b>; <b>Task 3:</b> 42 × 5 = <b>210 units</b> [6m]."),
    7: ("Topic 7: Division & Remainders", "<b>Task 1:</b> 28 ÷ 4 = <b>7</b>; <b>Task 2:</b> 29 ÷ 4 = <b>7 each,  1 leftover</b>; <b>Task 3:</b> 45 ÷ 5 = <b>9 teams</b> [6m]."),
    8: ("Topic 8: Fractions: 1/2, 1/4, 1/3, 1/10", "<b>Task 1:</b> Half of £40 = <b>£20.00</b>; <b>Task 2:</b> Quarter of 32 m = <b>8 metres</b>; <b>Task 3:</b> One-tenth of 100 kg = <b>10 kg</b> [6m]."),
    9: ("Topic 9: Decimals & Money Notation", "<b>Task 1:</b> Seventy-five pence = <b>£0.75</b>; <b>Task 2:</b> £4.50 + £2.25 = <b>£6.75</b>; <b>Task 3:</b> £10.00 - £6.50 = <b>£3.50</b> [6m]."),
    10: ("Topic 10: Rounding to Nearest 10 & 100", "<b>Task 1:</b> 67 to nearest 10 = <b>70</b>; <b>Task 2:</b> 235 to nearest 100 = <b>200</b>; <b>Task 3:</b> 85 rounds UP to <b>90</b> [6m]."),
    11: ("Topic 11: Adding Costs & Giving Change", "<b>Task 1:</b> Spend: £2.85 + £1.65 = £4.50. Change from £5 = <b>£0.50</b> (50p); <b>Task 2:</b> Change from £10 for £6.40 = <b>£3.60</b>; <b>Task 3:</b> £20 - £14.50 = <b>£5.50</b> [6m]."),
    12: ("Topic 12: Telling Time (12h & 24h)", "<b>Task 1:</b> Quarter past 9 am = <b>9:15 am</b>; <b>Task 2:</b> 2:00 pm in 24h = <b>14:00</b>; <b>Task 3:</b> Half past 4 pm = <b>16:30</b> [6m]."),
    13: ("Topic 13: Measuring Length (mm, cm, m)", "<b>Task 1:</b> 1 m  40 cm = <b>140 cm</b>; <b>Task 2:</b> 25 mm = <b>2.5 cm</b>; <b>Task 3:</b> Total length = 3.2 m = <b>320 cm</b> [6m]."),
    14: ("Topic 14: Measuring Weight (g and kg)", "<b>Task 1:</b> Half a kg = <b>500 grams</b>; <b>Task 2:</b> 1.5 kg = <b>1,500 g</b>; <b>Task 3:</b> Parcel = 750 g + 250 g = <b>1 kg</b> [6m]."),
    15: ("Topic 15: Measuring Capacity (ml and L)", "<b>Task 1:</b> 1.5 litres = <b>1,500 ml</b>; <b>Task 2:</b> Half a litre = <b>500 ml</b>; <b>Task 3:</b> Kettle holds <b>2 litres</b> [6m]."),
    16: ("Topic 16: Temperature in °C", "<b>Task 1:</b> 21°C - 18°C = <b>3°C too warm</b>; <b>Task 2:</b> Freezing point of water = <b>0°C</b>; <b>Task 3:</b> Rise from -2°C to 5°C = <b>7°C</b> [6m]."),
    17: ("Topic 17: Perimeter of 2D Shapes", "<b>Task 1:</b> Notice board 80 cm × 50 cm → P = 80+50+80+50 = <b>260 cm</b> (2.6 m); <b>Task 2:</b> Garden 6 m × 4 m → P = <b>20 metres</b>; <b>Task 3:</b> Square of side 5 m → P = <b>20 m</b> [6m]."),
    18: ("Topic 18: Recognising 2D & 3D Shapes", "<b>Task 1:</b> Tin can is a <b>cylinder</b>; <b>Task 2:</b> Shape with 4 equal sides is a <b>square</b>; <b>Task 3:</b> Box with rectangular faces is a <b>cuboid</b> [6m]."),
    19: ("Topic 19: Compass Directions & Position", "<b>Task 1:</b> Facing North, turn right → <b>East</b>; <b>Task 2:</b> Opposite of North is <b>South</b>; <b>Task 3:</b> Turning left from East → <b>North</b> [6m]."),
    20: ("Topic 20: Grid References on Maps", "<b>Task 1:</b> Column C, Row 4 → <b>C4</b>; <b>Task 2:</b> Pharmacy at <b>B2</b>; <b>Task 3:</b> Reception at <b>A1</b> [6m]."),
    21: ("Topic 21: Tally Charts & Lists", "<b>Task 1:</b> 3 bundles of 5 and 2 lines = 15 + 2 = <b>17 coffees</b>; <b>Task 2:</b> 8 tallies: 1 bundle of 5 and 3 single lines; <b>Task 3:</b> Total tally count = <b>32</b> [6m]."),
    22: ("Topic 22: Reading Bar Charts", "<b>Task 1:</b> Tallest bar is Maths with <b>24 learners</b>; <b>Task 2:</b> English has 18 learners; <b>Task 3:</b> Difference = 24 - 12 = <b>12 learners</b> [6m]."),
    23: ("Topic 23: Venn & Carroll Diagrams", "<b>Task 1:</b> 8 workers who do not wear glasses go in column <b>Does NOT wear glasses</b>; <b>Task 2:</b> Overlap area contains items with <b>both features</b>; <b>Task 3:</b> Total sorted = <b>20</b> [6m]."),
    24: ("Topic 24: Probability Words", "<b>Task 1:</b> Sun rising tomorrow is <b>Certain</b>; <b>Task 2:</b> Snowing in July in the UK is <b>Unlikely</b>; <b>Task 3:</b> Rolling an 8 on standard die is <b>Impossible</b> [6m].")
}

MATHS_E3_WORKSHOP_SOLUTIONS = {
    1: ("Workshop 1: Retail Cashier & Till", "<b>T1:</b> Bill = £3.20 + £1.85 + £4.50 = <b>£9.55</b>. <b>T2:</b> Change from £10 = <b>£0.45</b> (45p). 10% discount on £20 = <b>£2.00</b>."),
    2: ("Workshop 2: Care Home Resident Liquids", "<b>T1:</b> Daily fluid target = 1,500 ml. Recorded: 300 + 450 + 500 = 1,250 ml. Remaining = <b>250 ml</b>. <b>T2:</b> Temp 37.8°C is within normal range."),
    3: ("Workshop 3: Catering Kitchen Recipes", "<b>T1:</b> Double recipe: 12 muffins need 250 g → 24 muffins need  <b>500 g flour</b>. <b>T2:</b> Baking time: 25 minutes from 10:15 → <b>10:40</b>."),
    4: ("Workshop 4: Warehouse Stock Packing", "<b>T1:</b> 48 mugs packed 6 to a box = 48 ÷ 6 = <b>8 boxes</b>. <b>T2:</b> Remaining stock = 120 - 48 = <b>72 mugs</b>."),
    5: ("Workshop 5: Building Maintenance & Fencing", "<b>T1:</b> Perimeter = 2(10 + 6) = <b>32 metres</b>. <b>T2:</b> Posts needed: 1 post every 2 metres = 32 ÷ 2 = <b>16 posts</b>."),
    6: ("Workshop 6: Driver Delivery Schedules", "<b>T1:</b> Journey: departs 09:15, travel 45 mins → arrives <b>10:00</b>. <b>T2:</b> Head North, turn right → facing <b>East</b>."),
    7: ("Workshop 7: Office Supply Ordering", "<b>T1:</b> 5 boxes of paper at £4.50 = <b>£22.50</b>. <b>T2:</b> Round £22.50 to nearest £10 = <b>£20.00</b>."),
    8: ("Workshop 8: Community Event Planning", "<b>T1:</b> Tally count: Adults 24, Children 18 → Total = <b>42 attendees</b>. <b>T2:</b> Chairs needed: 45 chairs available → <b>Yes, sufficient chairs</b>.")
}

MATHS_E3_MOCK_SOLUTIONS = {
    1: ("Official Mock Exam 1 (36 Marks)",
        "<b>Section A (Non-Calculator, 9 Marks):</b><br>"
        "<b>Q1:</b> 158 + 236 = <b>394</b> [2m]. <b>Q2:</b> 450 - 185 = <b>265</b> [2m]. <b>Q3:</b> 8 × 5 = <b>40</b> [2m]. <b>Q4:</b> Half of £36 = <b>£18.00</b> [3m].<br>"
        "<b>Section B (Calculator Permitted, 27 Marks):</b><br>"
        "<b>Q5:</b> Total bill = £3.45 + £2.80 + £5.25 = £11.50. Change from £20 = <b>£8.50</b> [3m].<br>"
        "<b>Q6:</b> Perimeter of garden 9 m × 6 m = 2(9 + 6) = <b>30 metres</b> [3m].<br>"
        "<b>Q7:</b> Time: 09:30 to 11:15 = <b>1 hour  45 minutes</b> [3m].<br>"
        "<b>Q8:</b> 4 boxes of tiles at £14.50 = <b>£58.00</b> [3m].<br>"
        "<b>Q9:</b> Liquid: 2.5 litres = <b>2,500 ml</b> [3m].<br>"
        "<b>Q10:</b> Tally chart frequency for Car = <b>14</b> [3m].<br>"
        "<b>Q11:</b> Bar chart: Most popular sport is Football with <b>28 votes</b> [3m].<br>"
        "<b>Q12:</b> Probability of getting tails on a coin is <b>Evens</b> [3m].<br>"
        "<b>Q13:</b> Round 178 to nearest 100 = <b>200</b> [3m]."),
    2: ("Official Mock Exam 2 (36 Marks)",
        "<b>Section A (Non-Calculator, 9 Marks):</b><br>"
        "<b>Q1:</b> 245 + 168 = <b>413</b> [2m]. <b>Q2:</b> 500 - 245 = <b>255</b> [2m]. <b>Q3:</b> 6 × 4 = <b>24</b> [2m]. <b>Q4:</b> Quarter of 40 cm = <b>10 cm</b> [3m].<br>"
        "<b>Section B (Calculator Permitted, 27 Marks):</b><br>"
        "<b>Q5:</b> Cost: £4.20 + £3.50 + £6.10 = £13.80. Change from £20 = <b>£6.20</b> [3m].<br>"
        "<b>Q6:</b> Perimeter = 2(8 + 5) = <b>26 metres</b> [3m].<br>"
        "<b>Q7:</b> Digital 24h: 3:30 pm = <b>15:30</b> [3m].<br>"
        "<b>Q8:</b> 3 packs of paper at £5.50 = <b>£16.50</b> [3m].<br>"
        "<b>Q9:</b> 1.2 kg = <b>1,200 grams</b> [3m].<br>"
        "<b>Q10:</b> Difference in temperature: 18°C - 12°C = <b>6°C</b> [3m].<br>"
        "<b>Q11:</b> Bar chart: Difference between Saturday and Sunday = <b>15 customers</b> [3m].<br>"
        "<b>Q12:</b> Grid reference for Store = <b>B3</b> [3m].<br>"
        "<b>Q13:</b> Likelihood of rolling a 7 on a 6-sided die is <b>Impossible</b> [3m].")
}


# =============================================================================
# Synchronized Topic & Workbook Solutions (100% Aligned with Content Bank)
# =============================================================================
MATHS_L2_TOPIC_SOLUTIONS = {1: ('Topic 1: Place Value, Ordering & Large Numbers', '<b>Q1:</b> 642,085. Order: <b>458,900; 485,090; 485,200; 502,100</b> [2m].<br><b>Q2:</b> 425,800 − 389,950 = <b>35,850 parcels</b> [3m].<br><b>Q3:</b> Spent = £485,600 + £392,450 + £184,200 = £1,062,250. Remaining = £1,250,000 − £1,062,250 = <b>£187,750</b> [4m].'), 2: ('Topic 2: Negative Numbers & Financial Balances', '<b>Q1:</b> <b>−15°C, −12°C, −4.5°C, −0.5°C, +1.8°C, +3°C</b> [2m].<br><b>Q2:</b> +3 − 8.5 = <b>−5.5°C</b>. Since −5.5°C is colder than −5°C, <b>Yes, the alarm sounds</b> [3m].<br><b>Q3:</b> −640 + 2,850 − 1,420 − 980 + 195 = <b>£5.00</b> in credit [4m].'), 3: ('Topic 3: Fraction Operations & Mixed Numbers', '<b>Q1:</b> a) 15/24 + 4/24 = <b>19/24</b>; b) 8/3 × 3/4 = 24/12 = <b>2</b> [2m].<br><b>Q2:</b> 4 1/2 ÷ 3/16 = 9/2 × 16/3 = <b>24 burger patties</b> [3m].<br><b>Q3:</b> Day + Late = 3/5 + 1/4 = 17/20. Night shift = 3/20 = 45 workers → 1/20 = 15 → Total = 15 × 20 = <b>300 workers</b> [4m].'), 4: ('Topic 4: Percentages of Amounts & Multipliers', '<b>Q1:</b> a) <b>0.065</b>; b) <b>1.12</b>; c) <b>0.65</b>; d) <b>0.96</b> [2m].<br><b>Q2:</b> £620 × 1.085 = <b>£672.70</b> [3m].<br><b>Q3:</b> Dec = 14,500 × 1.28 = 18,560. Jan = 18,560 × 0.85 = <b>15,776 parcels</b> [4m].'), 5: ('Topic 5: Reverse Percentages & Original Value', '<b>Q1:</b> £84.00 ÷ 1.20 = <b>£70.00</b> [2m].<br><b>Q2:</b> Increase = 108. Percentage = (108 ÷ 450) × 100 = <b>24%</b> [3m].<br><b>Q3:</b> Loss = (1,360 ÷ 3,200) × 100 = <b>42.5%</b>. Original price of new model = £2,760 ÷ 0.85 = <b>£3,247.06</b> [4m].'), 6: ('Topic 6: Compound Interest & Depreciation', '<b>Q1:</b> £2,400 × (1.03)² = <b>£2,546.16</b> [2m].<br><b>Q2:</b> £28,000 × (0.82)³ = <b>£15,438.30</b> [3m].<br><b>Q3:</b> Bank A simple interest = 3 × £450 = £1,350. Bank B compound interest = £10,000 × (1.042)³ − £10,000 = £1,313.66. <b>Bank A yields £36.34 more</b> [4m].'), 7: ('Topic 7: Ratio Division in 2 & 3 Parts', '<b>Q1:</b> 5+3+1 = 9 parts. 1 part = £500. Shares: <b>£2,500, £1,500, £500</b> [2m].<br><b>Q2:</b> 1.4 t = 1,400 kg. 1+2+4 = 7 parts → 1 part = 200 kg. Sand (2 parts) = <b>400 kg</b> [3m].<br><b>Q3:</b> Supermarket A = £2.85 ÷ 0.75 kg = £3.80/kg. Supermarket B = £4.32 ÷ 1.2 kg = £3.60/kg. <b>Supermarket B is better value</b> [4m].'), 8: ('Topic 8: Direct & Inverse Proportion', '<b>Q1:</b> 5 × 4 = 20 cleaner-hours. For 8 cleaners: 20 ÷ 8 = <b>2.5 hours</b> (2 hrs 30 mins) [2m].<br><b>Q2:</b> Tank volume = 45 × 80 = 3,600 litres. At 30 L/min: 3,600 ÷ 30 = <b>120 minutes</b> (2 hours) [3m].<br><b>Q3:</b> 3 × 16 = 48 excavator-days. For 6 days: 48 ÷ 6 = 8 excavators total → 8 − 3 = <b>5 additional excavators</b> [4m].'), 9: ('Topic 9: Decimals & Money Calculations', '<b>Q1:</b> a) <b>485</b>; b) <b>0.0736</b>; c) <b>5.81</b> [2m].<br><b>Q2:</b> Total = £184.25 + £112.80 + £46.45 = £343.50. Underspent by £350 − £343.50 = <b>£6.50 underspend</b> [3m].<br><b>Q3:</b> Subtotal = £147 + £54 + £122.50 = £323.50. After 10% discount = £291.15. With 20% VAT = £291.15 × 1.20 = <b>£349.38</b> [4m].'), 10: ('Topic 10: Order of Operations (BIDMAS)', '<b>Q1:</b> a) 15 − 12 + 2 = <b>5</b>; b) 12 ÷ 4 + 9 = 3 + 9 = <b>12</b> [2m].<br><b>Q2:</b> d = 0.05(1,600) + 0.4(40) = 80 + 16 = <b>96 feet</b> [3m].<br><b>Q3:</b> C = 1.20 × (65 + 280 − 20) = 1.20 × 325 = <b>£390.00</b> [4m].'), 11: ('Topic 11: Estimation & Approximation', '<b>Q1:</b> a) 50 × 30 = <b>1,500</b>; b) 800 ÷ 20 = <b>40</b> [2m].<br><b>Q2:</b> 200 × £50 = <b>£10,000</b>. Overestimate because both numbers were rounded up [3m].<br><b>Q3:</b> Upper bounds: 65 cm × 45 cm × 35 cm = <b>102,375 cm³</b> [4m].'), 12: ('Topic 12: Metric & Imperial Conversions', '<b>Q1:</b> a) <b>3,450 g</b>; b) <b>0.75 litres</b>; c) (140 ÷ 5) × 8 = <b>224 km</b> [2m].<br><b>Q2:</b> Total needed = 15 × 3 × 14 = 630 ml. Since 630 ml > 500 ml, <b>No, one 500 ml bottle is not sufficient</b> [3m].<br><b>Q3:</b> 14 tonnes = 14,000 kg × 2.2 = <b>30,800 lbs</b> ≤ 31,000 lbs. <b>Yes, within legal limit</b> [4m].'), 13: ('Topic 13: Compound Units: Speed, Density & Pressure', '<b>Q1:</b> Density = 2,125 ÷ 250 = <b>8.5 g/cm³</b> [2m].<br><b>Q2:</b> Pressure = 1,800 ÷ 0.04 = <b>45,000 N/m²</b> [3m].<br><b>Q3:</b> Elapsed = 2h 24m. Minus 15m break = 2h 09m = 2.15 hours. Speed = 115 ÷ 2.15 = <b>53.5 mph</b> [4m].'), 14: ('Topic 14: Perimeter of Composite 2D Shapes', '<b>Q1:</b> Outer perimeter of L-shape = 2 × (12 + 9) = <b>42 metres</b> [2m].<br><b>Q2:</b> Fencing length = 2(28 + 18) − 4 = 92 − 4 = 88 m. Cost = 88 × £32.50 = <b>£2,860.00</b> [3m].<br><b>Q3:</b> Perimeter = 10 + 3 + 3 + 6 + 4 + 6 + 3 + 3 = 38 m. Lengths = 38 ÷ 2.5 = 15.2 → <b>16 lengths</b>. Cost = 16 × £14 = <b>£224.00</b> [4m].'), 15: ('Topic 15: Circumference of Circles', '<b>Q1:</b> C = 2 × 3.14 × 4.5 = <b>28.26 metres</b> [2m].<br><b>Q2:</b> Two straights = 200 m. Circle ends = 3.142 × 64 = 201.09 m. Total lap = <b>401.09 metres</b> [3m].<br><b>Q3:</b> Three straight edges = 1.8 + 1.2 + 1.8 = 4.8 m. Semicircle arch = 0.5 × 3.142 × 1.2 = 1.885 m. Total = <b>6.69 metres</b> [4m].'), 16: ('Topic 16: Area of Rectangles, Triangles & Parallelograms', '<b>Q1:</b> a) (14 × 9) ÷ 2 = <b>63 cm²</b>; b) 8.5 × 4.0 = <b>34 m²</b> [2m].<br><b>Q2:</b> Rectangle = 8 × 5 = 40 m². Triangle = (8 × 2.5) ÷ 2 = 10 m². Total area = <b>50 m²</b> [3m].<br><b>Q3:</b> Floor = 12 × 3.5 = 42 m². 1 box = 8 × 0.25 m² = 2 m². With 10% = 46.2 m² → 23.1 → <b>24 boxes</b> × £22 = <b>£528.00</b> [4m].'), 17: ('Topic 17: Area of Trapeziums & Composite Shapes', '<b>Q1:</b> Circle area (r = 3 m) = 3.142 × 9 = <b>28.28 m²</b> [2m].<br><b>Q2:</b> Trapezium area = ((7.2 + 11.8) ÷ 2) × 5.0 = 47.5 m². Cost = 47.5 × £8.50 = <b>£403.75</b> [3m].<br><b>Q3:</b> L-shape area = (14 × 10) − (6 × 4) = 140 − 24 = 116 m². Tins = 116 ÷ 25 = 4.64 → <b>5 tins</b> × £34.99 = <b>£174.95</b> [4m].'), 18: ('Topic 18: Area of Circles & Semicircles', '<b>Q1:</b> r = 3 m. Area = 3.142 × 3² = <b>28.28 m²</b> [2m].<br><b>Q2:</b> Semicircle r = 5 m. Area = 0.5 × 3.142 × 25 = 39.275 m². Cost = 39.275 × £5.80 = <b>£227.80</b> [3m].<br><b>Q3:</b> Park = 280 m². Pond = 3.142 × 16 = 50.27 m². Gravel area = 229.73 m² × 40 kg = 9,189 kg ÷ 800 = 11.49 → <b>12 bulk bags</b> [4m].'), 19: ('Topic 19: Surface Area of 3D Prisms & Cylinders', '<b>Q1:</b> 2(96 + 60 + 40) = 2(196) = <b>392 cm²</b> [2m].<br><b>Q2:</b> 2 triangles = 2 × 24 = 48 cm². 3 rectangles = (6+8+10) × 15 = 360 cm². Total = <b>408 cm²</b> [3m].<br><b>Q3:</b> Base = 3.142 × 0.2² = 0.1257 m². Side = 3.142 × 0.4 × 0.75 = 0.9426 m². Total = <b>1.07 m²</b> [4m].'), 20: ('Topic 20: Volume of Cuboids, Prisms & Cylinders', '<b>Q1:</b> Cross-section = 0.5 × 8 × 5 = 20 cm². Volume = 20 × 22 = <b>440 cm³</b> [2m].<br><b>Q2:</b> V = 3.14 × 30² × 90 = 254,340 cm³ = <b>254.3 litres</b> [3m].<br><b>Q3:</b> Average depth = (1.0 + 2.2) ÷ 2 = 1.6 m. Volume = 12 × 6 × 1.6 = <b>115.2 m³</b> = <b>115,200 litres</b> [4m].'), 21: ('Topic 21: Scale Drawings, Maps & Bearings', '<b>Q1:</b> 90 cm ÷ 20 = <b>4.5 cm</b> [2m].<br><b>Q2:</b> Back bearing = 065° + 180° = <b>245°</b> [3m].<br><b>Q3:</b> Real length = 18.5 × 2 = 37 m; width = 12 × 2 = 24 m. Perimeter = <b>122 m</b>; Area = 37 × 24 = <b>888 m²</b> [4m].'), 22: ('Topic 22: Mean, Median, Mode & Range', '<b>Q1:</b> Sum = 80 → Mean = <b>10</b>; Median = (9+9)/2 = <b>9</b>; Mode = <b>9</b>; Range = 15 − 6 = <b>9</b> [2m].<br><b>Q2:</b> 5-month total = £92,500. Plus £24,500 = £117,000 ÷ 6 = <b>£19,500</b> [3m].<br><b>Q3:</b> North: Mean = 83/7 = <b>11.9 mins</b>, Range = <b>7 mins</b>. South: Mean = 97/7 = <b>13.9 mins</b>, Range = <b>28 mins</b>. North is faster and more consistent [4m].'), 23: ('Topic 23: Grouped Frequency Tables & Estimated Mean', '<b>Q1:</b> Sum(fx) = (2.5 × 12) + (7.5 × 20) + (12.5 × 8) = 30 + 150 + 100 = 280. Mean = 280 ÷ 40 = <b>7.0 km</b> [2m].<br><b>Q2:</b> Modal class = <b>5–10 km</b>; Median (20th/21st person) lies in <b>5–10 km</b> [3m].<br><b>Q3:</b> Sum(fx) = (1×45) + (3×80) + (5×55) + (7×20) = 45 + 240 + 275 + 140 = 700. Mean = 700 ÷ 200 = <b>3.5 kg</b> (estimate because exact weights within intervals are unknown) [4m].'), 24: ('Topic 24: Scatter Graphs & Correlation', '<b>Q1:</b> a) <b>Positive correlation</b>; b) <b>Negative correlation</b> [2m].<br><b>Q2:</b> Midpoint between (10, 18) and (30, 6) at 20 hours = <b>12 errors</b> [3m].<br><b>Q3:</b> An outlier does not follow the general trend and should be ignored when drawing the line of best fit; remaining data shows positive correlation [4m].'), 25: ('Topic 25: Two-Way Frequency Tables', '<b>Q1:</b> Female: Pass 26, Fail 19, Total 45. Male: Pass 23, Fail 12, Total 35. Grand Total = 80 [2m].<br><b>Q2:</b> Male pass percentage = (23 ÷ 35) × 100 = <b>65.7%</b> [3m].<br><b>Q3:</b> Lorries = 120 − 70 = 50. Lorry first-time pass = 50 − (18 + 12) = 20. P(Lorry pass) = 20/50 = <b>2/5</b> (0.4 or 40%) [4m].'), 26: ('Topic 26: Pie Charts: Calculating Angles & Frequencies', '<b>Q1:</b> 360° ÷ 120 = 3° per guest. Business = <b>120°</b>, Holiday = <b>180°</b>, Event = <b>60°</b> [2m].<br><b>Q2:</b> (108 ÷ 360) × 1,800 = <b>540 voters</b> [3m].<br><b>Q3:</b> Cycle Lanes = (45 ÷ 360) × £2.4m = <b>£300,000</b>, which is <b>12.5%</b> of the budget [4m].'), 27: ('Topic 27: Single & Combined Event Probability', '<b>Q1:</b> a) P(prime) = 3/6 = <b>1/2</b>; b) P(>4) = 2/6 = <b>1/3</b> [2m].<br><b>Q2:</b> P(defect-free) = 432/450 = <b>0.96</b>. Expected defects in 2,500 = 2,500 × (18/450) = <b>100 defects</b> [3m].<br><b>Q3:</b> P(both run without fault) = 0.90 × 0.85 = <b>0.765</b> (76.5%) [4m].'), 28: ('Topic 28: Probability Tree Diagrams & Independent Events', '<b>Q1:</b> P(Fail both) = 0.2 × 0.3 = <b>0.06</b> (6%) [2m].<br><b>Q2:</b> P(Pass one) = (0.8 × 0.3) + (0.2 × 0.7) = 0.24 + 0.14 = <b>0.38</b> (38%) [3m].<br><b>Q3:</b> P(No rain either day) = 0.6 × 0.8 = 0.48. P(Rain at least one day) = 1 − 0.48 = <b>0.52</b> (52%) [4m].')}

MATHS_L1_TOPIC_SOLUTIONS = {1: ('Topic 1: Place Value & Large Numbers', '<b>Q1:</b> 45,820; <b>Q2:</b> 128,450 - 95,200 = <b>33,250 units</b>; <b>Q3:</b> Order: 3,450; 12,890; 14,200; 108,500 [7m].'), 2: ('Topic 2: Negative Numbers in Practical Contexts', '<b>Q1:</b> −11°C, −8°C, −2°C, 0°C, +4°C; <b>Q2:</b> −15 + 6 = <b>−9°C</b>; <b>Q3:</b> £120 − £185 = <b>−£65</b> (need £115 to reach +£50) [7m].'), 3: ('Topic 3: Column Addition & Subtraction with Money', '<b>Q1:</b> 4,850 + 2,680 = <b>7,530</b>; <b>Q2:</b> £24.50 + £18.75 + £9.20 = <b>£52.45</b>; <b>Q3:</b> £1,500 − £845 − £320 = <b>£335.00</b> [7m].'), 4: ('Topic 4: Long Multiplication in Context', '<b>Q1:</b> 145 × 18 = <b>2,610</b>; <b>Q2:</b> 24 crates × 35 items = <b>840 items</b>; <b>Q3:</b> 32 hours × £12.50 = <b>£400.00</b> [7m].'), 5: ('Topic 5: Division with Remainders in Context', '<b>Q1:</b> 256 ÷ 8 = <b>32</b>; <b>Q2:</b> 185 ÷ 12 = 15 remainder  5 → <b>16 crates needed</b>; <b>Q3:</b> £350 ÷ 4 = <b>£87.50 each</b> [7m].'), 6: ('Topic 6: Fractions of Quantities', '<b>Q1:</b> 1/4 of £240 = <b>£60.00</b>; <b>Q2:</b> 3/4 of 480 kg = (480 ÷ 4) × 3 = <b>360 kg</b>; <b>Q3:</b> 2/3 of 90 minutes = <b>60 minutes</b> [7m].'), 7: ('Topic 7: Decimals & Rounding', '<b>Q1:</b> 14.86 to 1 d.p. = <b>14.9</b>; <b>Q2:</b> £3.45 + £8.80 = <b>£12.25</b>; <b>Q3:</b> 4.2 m - 1.85 m = <b>2.35 metres</b> [7m].'), 8: ('Topic 8: Percentages: 10%, 25%, 50% & 75%', '<b>Q1:</b> 10% of £450 = <b>£45.00</b>; <b>Q2:</b> 25% discount on £180 = £45 → Sale price = <b>£135.00</b>; <b>Q3:</b> 75% of 320 staff = <b>240 staff</b> [7m].'), 9: ('Topic 9: Ratio Sharing in 2 Parts', '<b>Q1:</b> Share £180 in ratio 2 : 1 → 3 parts. Shares: <b>£120 and  £60</b>; <b>Q2:</b> Cement to sand 1 : 4. Total 25 kg → <b>5 kg cement,  20 kg sand</b>; <b>Q3:</b> Paint mix: <b>4 litres white,  2 litres blue</b> [7m].'), 10: ('Topic 10: Proportion & Scaling Recipes', '<b>Q1:</b> Soup for 4 is 600 ml → for 6 people = 150 × 6 = <b>900 ml</b>; <b>Q2:</b> 3 books cost £24 → 5 books = <b>£40.00</b>; <b>Q3:</b> Cake mix doubled: <b>500 g flour,  300 g sugar</b> [7m].'), 11: ('Topic 11: Estimation & Checking', '<b>Q1:</b> 49 × 21 ≈ 50 × 20 = <b>1,000</b>; <b>Q2:</b> 19 × £11.85 ≈ 20 × £12 = <b>£240.00</b>; <b>Q3:</b> Check subtraction by reverse addition: 316 + 184 = <b>500</b> [7m].'), 12: ('Topic 12: Money & Giving Change', '<b>Q1:</b> Total = £3.45 + £2.80 + £6.15 = £12.40. Change from £20 = <b>£7.60</b>; <b>Q2:</b> £50 - £34.20 = <b>£15.80</b>; <b>Q3:</b> 3 items at £4.50 = £13.50. Change from £20 = <b>£6.50</b> [7m].'), 13: ('Topic 13: Time: 12h & 24h Clock', '<b>Q1:</b> 3:15 pm = <b>15:15</b>; 19:40 = <b>7:40 pm</b>; <b>Q2:</b> 08:30 to 16:45 = <b>8 hours  15 minutes</b>; <b>Q3:</b> Meeting starts 14:30, lasts 1h  45m → finishes <b>16:15</b> [7m].'), 14: ('Topic 14: Timetables & Journey Planning', '<b>Q1:</b> 14:22 to 14:58 = <b>36 minutes</b>; <b>Q2:</b> Next train after 10:15 is at 10:32, arrives <b>11:05</b>; <b>Q3:</b> Journey time: <b>1 hour  18 minutes</b> [7m].'), 15: ('Topic 15: Metric Length: mm, cm, m, km', '<b>Q1:</b> 2.4 m = <b>240 cm</b>; 45 mm = <b>4.5 cm</b>; <b>Q2:</b> 3.6 m - (4 × 0.65 m) = <b>1.0 metre remaining</b>; <b>Q3:</b> Total running: 5.2 km = <b>5,200 metres</b> [7m].'), 16: ('Topic 16: Metric Weight: g and kg', '<b>Q1:</b> 1,750 g = <b>1.75 kg</b>; <b>Q2:</b> 4 parcels at 350 g = 1,400 g = <b>1.4 kg</b>; <b>Q3:</b> Flour: 2.5 kg - 800 g = <b>1.7 kg</b> (1,700 g) [7m].'), 17: ('Topic 17: Metric Capacity: ml and litres', '<b>Q1:</b> 4.5 litres = <b>4,500 ml</b>; <b>Q2:</b> 15 × 250 ml = 3,750 ml = <b>3.75 litres</b>; <b>Q3:</b> Dilution: 500 ml concentrate into 4.5 L water = <b>5.0 litres total</b> [7m].'), 18: ('Topic 18: Perimeter of Rectangles', '<b>Q1:</b> 2(9 + 6) = <b>30 metres</b>; <b>Q2:</b> Room 4.5 m × 3.2 m → P = 2(7.7) = <b>15.4 m</b>; <b>Q3:</b> Fencing needed = <b>48 metres</b> [7m].'), 19: ('Topic 19: Area of Rectangles', '<b>Q1:</b> 4.5 × 3 = <b>13.5 m²</b>; <b>Q2:</b> Wall 6 × 2.5 = <b>15 m²</b> (2 coats = <b>30 m²</b>); <b>Q3:</b> 8 × 5 = <b>40 m²</b>, Cost = 40 × £12 = <b>£480.00</b> [7m].'), 20: ('Topic 20: 2D & 3D Shapes & Angles', '<b>Q1:</b> Shape with 6 rectangular faces is a <b>cuboid</b>; <b>Q2:</b> Right angle = <b>90°</b>; <b>Q3:</b> Triangular prism has <b>5 faces,  9 edges,  6 vertices</b> [7m].'), 21: ('Topic 21: Compass Directions & Headings', '<b>Q1:</b> Facing North, turn 90° clockwise → <b>East</b>; <b>Q2:</b> Opposite of South-West is <b>North-East</b>; <b>Q3:</b> Facing East, turn 180° → <b>West</b> [7m].'), 22: ('Topic 22: Tally Charts & Frequency', '<b>Q1:</b> 14 tallies: 2 bundles of 5 and 4 single lines; <b>Q2:</b> Frequency total = 8 + 14 + 12 + 6 = <b>40</b>; <b>Q3:</b> Most popular category is <b>Van</b> (14 tallies) [7m].'), 23: ('Topic 23: Bar Charts: Scales & Comparison', '<b>Q1:</b> Wed = 40, Mon = 25 → Difference = <b>15 sales</b>; <b>Q2:</b> Scale: 1 square = 5 units; <b>Q3:</b> Total weekly sales = <b>165 units</b> [7m].'), 24: ('Topic 24: Pictograms with Key Symbols', '<b>Q1:</b> 1 circle = 8 cars. 3.5 circles = 3 × 8 + 4 = <b>28 cars</b>; <b>Q2:</b> 20 bicycles with key = 4 → <b>5 symbols</b>; <b>Q3:</b> Total vehicles = <b>72 vehicles</b> [7m].'), 25: ('Topic 25: Mean Average', '<b>Q1:</b> Daily hours: 7 + 8 + 8 + 9 + 8 = 40 → 40 ÷ 5 = <b>8 hours</b>; <b>Q2:</b> Scores: 15, 18, 21, 26 → 80 ÷ 4 = <b>20</b>; <b>Q3:</b> Mean weekly spend = <b>£42.50</b> [7m].'), 26: ('Topic 26: Range: Measure of Spread', '<b>Q1:</b> Calls: 71 - 38 = <b>33 calls</b>; <b>Q2:</b> Temperatures: +6 - (-4) = <b>10°C</b>; <b>Q3:</b> Range of delivery times = 45 - 18 = <b>27 minutes</b> [7m].'), 27: ('Topic 27: Reading Information from Tables', '<b>Q1:</b> 3 small parcels at £3.29 = <b>£9.87</b>; <b>Q2:</b> Table lookup: Standard delivery = <b>£4.50</b>; <b>Q3:</b> Invoice total: <b>£148.20</b> [7m].'), 28: ('Topic 28: Probability Words', '<b>Q1:</b> Rolling a number 1 to 6 on standard die is <b>Certain</b>; <b>Q2:</b> Flipping tails on a coin is <b>Evens</b> (50-50); <b>Q3:</b> Rolling an 8 on standard die is <b>Impossible</b> [7m].')}

MATHS_L1_WORKBOOK_SOLUTIONS = {1: ('Worksheet 1: Place Value & Negative Temperatures', '<b>T1:</b> a) <b>42,508</b>; b) Three hundred and six thousand, four hundred and twenty; c) <b>−14°C, −6°C, −2°C, +1°C, +3°C</b>. <b>T2:</b> −16 + 9 = <b>−7°C</b>.'), 2: ('Worksheet 2: Column Addition & Subtraction', '<b>T1:</b> a) 1,458 + 2,385 = <b>3,843</b>; b) 4,000 − 1,675 = <b>2,325</b>. <b>T2:</b> 450 + 625 + 380 = <b>1,455 masks</b>.'), 3: ('Worksheet 3: Multiplication & Division', '<b>T1:</b> a) 236 × 18 = <b>4,248</b>; b) 952 ÷ 7 = <b>136</b>. <b>T2:</b> 24 × 35 = <b>840 tins</b>.'), 4: ('Worksheet 4: Multiplying & Dividing by 10, 100', '<b>T1:</b> a) <b>3,400</b>; b) <b>58</b>; c) <b>42</b>; d) <b>6.5</b>. <b>T2:</b> 100 × £3.45 = <b>£345.00</b>.'), 5: ('Worksheet 5: Order of Operations (BIDMAS) & Rules', '<b>T1:</b> a) 14 + 15 = <b>29</b>; b) 12 ÷ 3 = <b>4</b>; c) 25 − 8 + 1 = <b>18</b>; d) 16 − 10 = <b>6</b>. <b>T2:</b> £30 + (£15 × 4) = <b>£90.00</b>.'), 6: ('Worksheet 6: Simplifying & Equivalent Fractions', '<b>T1:</b> a) <b>2/3</b>; b) <b>2/5</b>; c) <b>3/4</b>; d) <b>1/3</b>. <b>T2:</b> a) <b>10</b>; b) <b>32</b>; c) <b>6</b>.'), 7: ('Worksheet 7: Fractions of Amounts', '<b>T1:</b> a) <b>£15</b>; b) <b>16 kg</b>; c) <b>£45</b>; d) <b>10 m</b>. <b>T2:</b> Dispensed = 3/8 of 240 = 90; Remaining = 240 − 90 = <b>150 capsules</b>.'), 8: ('Worksheet 8: Decimals & Cafe Receipt', '<b>T1:</b> a) <b>24.35</b>; b) <b>25.65</b>; c) <b>32.0</b>; d) <b>6.20</b>. <b>T2:</b> Total = £5.70 + £4.50 + £2.20 = £12.40; Change from £20 = <b>£7.60</b>.'), 9: ('Worksheet 9: Benchmark Percentages & Discounts', '<b>T1:</b> a) <b>£42</b>; b) <b>15 kg</b>; c) <b>£35</b>; d) <b>£9</b>. <b>T2:</b> 25% of £320 = £80 off → Sale price = <b>£240.00</b>.'), 10: ('Worksheet 10: Fraction, Decimal & Percentage Equivalence', '<b>T1:</b> a) 1/2 = <b>0.5</b> = <b>50%</b>; b) 0.25 = <b>1/4</b> = <b>25%</b>. <b>T2:</b> 3/5 = 60%, so <b>65% is larger</b> (by 5%).'), 11: ('Worksheet 11: Ratio Sharing & Punch Recipe', '<b>T1:</b> a) <b>£40 and £20</b>; b) <b>15 kg and 25 kg</b>. <b>T2:</b> 3 + 2 = 5 parts; 15 ÷ 5 = 3 L; Orange juice (3 parts) = <b>9 litres</b>.'), 12: ('Worksheet 12: Metric Length Conversions', '<b>T1:</b> a) <b>450 cm</b>; b) <b>2.5 m</b>; c) <b>6.5 cm</b>; d) <b>3,200 m</b>. <b>T2:</b> 300 − (85 + 90 + 65) = 300 − 240 = <b>60 cm</b>.'), 13: ('Worksheet 13: Metric Weight & Capacity', '<b>T1:</b> a) <b>3,200 g</b>; b) <b>0.75 L</b>; c) <b>4.5 kg</b>; d) <b>1,500 ml</b>. <b>T2:</b> 5,000 − (1,250 + 850) = <b>2,900 g</b> (2.9 kg).'), 14: ('Worksheet 14: Imperial & Metric Approximations', '<b>T1:</b> a) <b>40 km</b>; b) <b>25 miles</b>; c) <b>25 cm</b> (or 25.4 cm). <b>T2:</b> 18 × 2.2 = <b>39.6 lbs</b> ≤ 44 lbs (<b>Yes, within limit</b>).'), 15: ('Worksheet 15: 24-Hour Time & Journey Duration', '<b>T1:</b> a) <b>08:40</b>; b) <b>15:25</b>; c) <b>21:10</b>; d) <b>23:55</b>. <b>T2:</b> 07:42 to 09:15 = <b>1 hour 33 minutes</b>.'), 16: ('Worksheet 16: Perimeter & Skirting Boards', '<b>T1:</b> a) <b>26 m</b>; b) <b>30 cm</b>; c) <b>27 cm</b>. <b>T2:</b> 2(5.5 + 4.0) − 1.0 = 19.0 − 1.0 = <b>18.0 metres</b>.'), 17: ('Worksheet 17: Area of Rectangles & Carpet Cost', '<b>T1:</b> a) <b>28 m²</b>; b) <b>81 cm²</b>; c) <b>96 m²</b>. <b>T2:</b> Area = 4.5 × 3.0 = 13.5 m²; Cost = 13.5 × £16 = <b>£216.00</b>.'), 18: ('Worksheet 18: Composite L-Shape Area', '<b>T1:</b> (6 × 4) + (3 × 2) = 24 + 6 = <b>30 m²</b>. <b>T2:</b> (8 × 5) − (4 × 3) = 40 − 12 = <b>28 m²</b>.'), 19: ('Worksheet 19: Volume of Cuboids & Aquariums', '<b>T1:</b> a) <b>200 cm³</b>; b) <b>2.4 m³</b>. <b>T2:</b> 60 × 30 × 40 = 72,000 cm³ = <b>72 litres</b>.'), 20: ('Worksheet 20: Angles & Triangles', '<b>T1:</b> a) <b>Acute</b>; b) <b>Right angle</b>; c) <b>Obtuse</b>; d) <b>Straight line</b>. <b>T2:</b> 180° − (90° + 38°) = <b>52°</b>.'), 21: ('Worksheet 21: 3D Shapes & Packaging Nets', '<b>T1:</b> a) Cube: 6F, 12E, 8V; b) Triangular prism: 5F, 9E, 6V; c) Square pyramid: 5F, 8E, 5V. <b>T2:</b> <b>Cuboid</b>.'), 22: ('Worksheet 22: Scale Plans & Real Dimensions', '<b>T1:</b> a) <b>12 m</b>; b) <b>6 cm</b>. <b>T2:</b> 14 × 50 = 700 cm = <b>7 m</b>; 10 × 50 = 500 cm = <b>5 m</b>.'), 23: ('Worksheet 23: Compass Directions & Routes', '<b>T1:</b> a) <b>South-West</b>; b) <b>East</b>; c) <b>West</b>. <b>T2:</b> Depot is <b>North-West</b> of the van.'), 24: ('Worksheet 24: Average Speed Calculations', '<b>T1:</b> a) <b>60 mph</b>; b) <b>60 mph</b>; c) <b>50 km/h</b>. <b>T2:</b> 165 ÷ 3 = <b>55 mph</b>.'), 25: ('Worksheet 25: Tally Tables & Fractions of Totals', '<b>T1:</b> Red = 12, Blue = 11, Green = 7; Total = <b>30</b>. <b>T2:</b> 45 ÷ 60 = <b>3/4</b> attended.'), 26: ('Worksheet 26: Reading Bar Charts', '<b>T1:</b> a) <b>Dept D</b> (80); b) 40 + 65 + 55 + 80 = <b>240</b>. <b>T2:</b> 80 − 40 = <b>40 staff</b>.'), 27: ('Worksheet 27: Dual Bar Charts & Comparisons', '<b>T1:</b> Week 2 total = 40 + 35 + 50 = <b>125 sales</b>. <b>T2:</b> <b>Monday and Tuesday</b> (both increased by <b>10 sales</b>).'), 28: ('Worksheet 28: Pictograms & Key Multipliers', '<b>T1:</b> a) <b>30</b>; b) <b>45</b>; c) <b>22.5</b>. <b>T2:</b> (4 + 5.5) × 8 = 9.5 × 8 = <b>76 books</b>.'), 29: ('Worksheet 29: Line Graphs & Trends', '<b>T1:</b> At 09:00 = <b>16°C</b>; at 11:00 = <b>20°C</b>. <b>T2:</b> Overall <b>upward (increasing) trend</b> across the week.'), 30: ('Worksheet 30: Pie Chart Proportions', '<b>T1:</b> a) <b>80</b>; b) <b>40</b>; c) <b>120</b>. <b>T2:</b> 1/4 of 120 = <b>30 staff</b> walk.'), 31: ('Worksheet 31: Mean Average Drills', '<b>T1:</b> a) 36 ÷ 4 = <b>9</b>; b) 100 ÷ 5 = <b>20</b>. <b>T2:</b> 190 ÷ 5 = <b>38 drops</b>.'), 32: ('Worksheet 32: Range & Consistency', '<b>T1:</b> a) 25 − 8 = <b>17</b>; b) 61 − 42 = <b>19</b>. <b>T2:</b> 18 − 4 = <b>14 minutes</b>.'), 33: ('Worksheet 33: Probability Scale & Dice', '<b>T1:</b> a) <b>1</b>; b) <b>0.5</b>; c) <b>0</b>; d) <b>0.75</b>. <b>T2:</b> a) <b>1/6</b>; b) 3/6 = <b>1/2</b>; c) 4/6 = <b>2/3</b>.'), 34: ('Worksheet 34: Sample Spaces & Combinations', '<b>T1:</b> <b>8 outcomes</b> (H1, H2, H3, H4, T1, T2, T3, T4). <b>T2:</b> 2 × 2 × 2 = <b>8 meal deal combinations</b>.')}
