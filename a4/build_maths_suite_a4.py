#!/usr/bin/env python3
"""
books/a4/build_maths_suite_a4.py
=============================================================================
Compiles all 5 Master Functional Skills Mathematics publications in the new
A4 "Fill the Page" layout (13pt/14pt typography, 5mm grid working areas,
real workplace photos, SVG diagrams, and zero bottom space):

1. MasterFunctionalSkills_Maths_Level_2_Core_Guide.pdf          (104 Pages)
2. MasterFunctionalSkills_Maths_Level_2_Companion_Workbook.pdf  (108 Pages)
3. MasterFunctionalSkills_Maths_Level_1_Core_Guide.pdf          (104 Pages)
4. MasterFunctionalSkills_Maths_Level_1_Companion_Workbook.pdf  (108 Pages)
5. MasterFunctionalSkills_Maths_Entry_Level_3_Core_Guide.pdf     (104 Pages)

Outputs to:
- assets/downloads/
- ~/Documents/
=============================================================================
"""

import os
import sys
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJECT_DIR = HERE.parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(PROJECT_DIR / "books" / "maths_builders"))

import a4_kit as K
import maths_suite_reference as ref
from maths_suite_content import (
    TOPIC_L2_QUESTIONS,
    CHECKPOINT_L2_QUESTIONS,
    MOCK_MATHS_L2_DATA,
    WORKBOOK_L2_DRILLS,
    TOPIC_L1_QUESTIONS,
    CHECKPOINT_L1_QUESTIONS,
    MOCK_MATHS_L1_DATA,
    WORKBOOK_L1_DRILLS,
    TOPIC_E3_QUESTIONS,
    CHECKPOINT_E3_QUESTIONS,
    MOCK_MATHS_E3_DATA,
)

DOWNLOADS = PROJECT_DIR / "assets" / "downloads"
DOCUMENTS = Path("/home/subi/Documents")
COV = K.COVER_DIR


def get_photo(keywords, theme="maths", exclude=None):
    return K.photo(keywords, theme, exclude or set())


# =============================================================================
# 1. Maths Level 2 Core Study Guide (104 Pages)
# =============================================================================
def build_maths_l2_core():
    print("\n" + "="*70)
    print("BUILDING: MasterFunctionalSkills_Maths_Level_2_Core_Guide.pdf (A4 104p)")
    print("="*70)

    BOOK = "Maths Level 2 Core Guide"
    front_cov = COV / "maths_l2_core_cover_page-1.png"
    back_cov = COV / "maths_l2_core_cover_page-2.png"

    pages = []
    used_photos = set()

    def P(kw):
        p = get_photo(kw, "maths", used_photos) or get_photo(kw, "measuring_tools", used_photos) or get_photo(kw, None, used_photos)
        if p:
            used_photos.add(p)
        return p

    # p1: Front Cover
    pages.append(K.front_cover(front_cov))

    # p2: Inside Cover
    pages.append(K.inside_cover(
        "Functional Skills Mathematics",
        "Level 2 &bull; Comprehensive Curriculum Guide &bull; Section A &amp; B Model Solutions",
        "Maths Level 2",
        [
            ("1&ndash;11", "Strand 1: Number &amp; Number Systems (28% of exam)", "3"),
            ("12&ndash;21", "Strand 2: Measures, Shape &amp; Space (40% of exam)", "31"),
            ("22&ndash;28", "Strand 3: Handling Information &amp; Data (32% of exam)", "61"),
            ("C1&ndash;C3", "3 End-of-Strand 4-Page Checkpoint Assessments", "79"),
            ("M1&ndash;M2", "2 Full Official-Style Mock Exams (Section A &amp; B)", "91"),
            ("ANS", "Comprehensive Mark Schemes &amp; Process Mark Guidance", "99"),
        ],
        footer=BOOK
    ))

    # 28 Two-Page Topics = 56 pages (p3 to p58)
    TOPICS_L2 = [
        # Strand 1: Number (11 topics)
        (1, "Place Value, Ordering & Large Numbers", "Number &bull; Standard N1", "office desk laptop paperwork",
         "In large numbers up to 1,000,000, each digit column represents a power of ten. Use commas or spaces between thousands.",
         "Separate digits into groups of three from the right: Millions, Thousands, Units.",
         "A warehouse records 425,800 units in Q1 and 389,950 units in Q2. How many more in Q1?",
         ["Align columns: 425,800 - 389,950", "Perform column subtraction with borrowing", "Difference = <b>35,850 units</b>"],
         "Always align digits by their place value, never by the leftmost digit.", "Don't confuse hundred thousands with millions."),
        (2, "Negative Numbers & Financial Balances", "Number &bull; Standard N2", "calculator finance bills money",
         "Negative numbers represent values below zero (bank overdrafts, temperatures, sea level). Adding a negative is subtraction.",
         "Positive + Positive = Positive. Positive + Negative = Subtract smaller from larger.",
         "A business account is at -£1,450. A client pays £3,200, then bills of £850 and £1,120 are debited.",
         ["Start: -£1,450 + £3,200 = +£1,750", "Deduct bills: £1,750 - £850 = £900", "Deduct staff: £900 - £1,120 = <b>-£220</b> (Overdraft)"],
         "Moving right on the number line increases value; moving left decreases value.", "Subtracting a negative becomes an addition: 5 - (-3) = 8."),
        (3, "Fraction Operations & Mixed Numbers", "Number &bull; Standard N3", "kitchen cooking scales recipe",
         "Fractions represent equal parts of a whole. To add or subtract, you MUST find a common denominator.",
         "Multiply fractions: multiply numerators together, then denominators together. Divide: flip second fraction and multiply.",
         "Calculate 2 1/4 + 1 2/3 for a catering recipe calculation.",
         ["Convert to improper: 9/4 + 5/3", "Common denominator 12: 27/12 + 20/12 = 47/12", "Convert to mixed: <b>3 11/12</b>"],
         "Always convert mixed numbers to improper fractions before multiplying or dividing.", "Never add denominators together: 1/2 + 1/2 is not 2/4!"),
        (4, "Percentages of Amounts & Multipliers", "Number &bull; Standard N4", "supermarket retail shelves groceries",
         "Percent means 'out of 100'. Use single-step decimal multipliers to calculate percentage changes efficiently.",
         "Percentage increase: Multiplier = 1 + (percentage / 100). Decrease: Multiplier = 1 - (percentage / 100).",
         "An operative earns £24,500. They receive a 4.5% cost of living pay rise. What is the new salary?",
         ["Multiplier for 4.5% increase = 1.045", "Calculation: £24,500 x 1.045", "New salary = <b>£25,602.50</b>"],
         "Use decimal multipliers for calculator questions to save time and reduce errors.", "Check if question asks for the INCREASE or the FINAL TOTAL."),
        (5, "Reverse Percentages & Original Value", "Number &bull; Standard N5", "retail shop till payment",
         "Reverse percentage problems give you the value AFTER an increase or decrease and ask for the ORIGINAL value.",
         "Original Value = Final Value / Multiplier. NEVER just calculate the percentage of the final value!",
         "A laptop is on sale for £468 after a 20% discount. What was the original price before the sale?",
         ["After 20% off, £468 represents 80% of original price (0.80 multiplier)", "Calculation: £468 / 0.80", "Original price = <b>£585.00</b>"],
         "Always divide by the percentage multiplier to work backwards to the original 100%.", "Do NOT add 20% of £468 (£93.60) — that gives the wrong answer (£561.60)."),
        (6, "Compound Interest & Depreciation", "Number &bull; Standard N6", "analytics dashboard charts screen",
         "Compound interest applies interest to both the initial principal and the accumulated interest from previous periods.",
         "Final Amount = Principal x (1 + r)^n, where r is decimal interest rate and n is number of years.",
         "An NHS worker invests £5,000 in a savings bond paying 3.2% compound interest per year for 3 years.",
         ["Multiplier = 1.032", "Formula: £5,000 x (1.032)^3", "£5,000 x 1.09911 = <b>£5,495.55</b>"],
         "Apply the multiplier repeatedly or use the power key (x^y) on your scientific calculator.", "Simple interest gives less than compound interest over multiple years."),
        (7, "Ratio Division in 2 & 3 Parts", "Number &bull; Standard N7", "construction builder measuring site",
         "Ratios show relative sizes of quantities. To divide into a ratio, find the value of one part.",
         "Step 1: Add ratio parts. Step 2: Total amount / Total parts = 1 part. Step 3: Multiply by each ratio part.",
         "Concrete is mixed in the ratio cement : sand : gravel = 1 : 2 : 4. How much sand is needed for 840 kg of mix?",
         ["Total parts: 1 + 2 + 4 = 7 parts", "Value of 1 part: 840 kg / 7 = 120 kg", "Sand (2 parts): 2 x 120 kg = <b>240 kg</b>"],
         "Always check your answers sum back to the original total (120 + 240 + 480 = 840).", "Read the order of terms carefully: cement : sand : gravel."),
        (8, "Direct & Inverse Proportion", "Number &bull; Standard N8", "kitchen cooking scales recipe",
         "Direct proportion: as one increases, the other increases at the same rate. Inverse: as one increases, the other decreases.",
         "Direct: find unitary value (value for 1) then multiply. Inverse: Total work = workers x days = constant.",
         "It takes 4 decorators 6 days to paint an office block. How long would it take 3 decorators?",
         ["Total work required = 4 decorators x 6 days = 24 worker-days", "Time for 3 decorators = 24 worker-days / 3 decorators", "Total time = <b>8 days</b>"],
         "More workers means FEWER days: inverse proportion always multiplies to a constant product.", "Direct proportion problems maintain a constant ratio (division)."),
        (9, "Decimals & Money Calculations", "Number &bull; Standard N9", "receipts invoice checking audit",
         "Decimals represent tenths, hundredths, and thousandths. Money is always rounded to 2 decimal places (£0.00).",
         "Align decimal points vertically for addition and subtraction. For multiplication, count total decimal places.",
         "An operative buys 14.5 metres of cabling at £2.64 per metre plus VAT at 20%.",
         ["Cable cost: 14.5 x £2.64 = £38.28", "Add 20% VAT: £38.28 x 1.20 = £45.936", "Rounded to 2 decimal places = <b>£45.94</b>"],
         "Always include two decimal places for currency answers (write £45.90, not £45.9).", "Round down only at the very final step of your multi-step calculation."),
        (10, "Order of Operations (BIDMAS)", "Number &bull; Standard N10", "calculator finance bills money",
         "Calculations must follow the statutory mathematical order: Brackets, Indices, Division/Multiplication, Addition/Subtraction.",
         "Work inside brackets first, then evaluate powers/roots, then left-to-right for division/multiplication.",
         "Evaluate the formula for monthly mortgage repayment factor: (180 - 4 x 5^2) / 2.",
         ["Indices first: 5^2 = 25", "Multiplication: 4 x 25 = 100", "Brackets: 180 - 100 = 80", "Division: 80 / 2 = <b>40</b>"],
         "Calculators without bracket keys do operations from left to right; enter BIDMAS steps manually.", "Division and multiplication have equal priority — execute left to right."),
        (11, "Estimation & Approximation", "Number &bull; Standard N11", "warehouse stock inventory boxes",
         "Estimation involves rounding every number in a calculation to 1 significant figure to check plausibility.",
         "Round each number to 1 significant figure BEFORE performing any calculation.",
         "Estimate the cost of 48.7 hours of plant machinery hire at £31.25 per hour.",
         ["Round 48.7 to 1 sig fig = 50", "Round £31.25 to 1 sig fig = £30", "Estimated calculation = 50 x £30 = <b>£1,500</b>"],
         "Do not calculate the exact answer and then round it — examiners award marks for pre-rounding.", "Estimation is an essential checking method required in Section A exam tasks."),

        # Strand 2: Measures, Shape & Space (10 topics)
        (12, "Metric & Imperial Conversions", "Measure &bull; Standard M12", "tape measure centimetres metric",
         "Functional skills requires converting between metric units (mm, cm, m, km; g, kg; ml, l) and key imperial benchmarks.",
         "Key imperial equivalences: 1 inch = 2.54 cm; 1 foot = 30 cm; 1 kg = 2.2 lbs; 1 gallon = 4.5 litres; 5 miles = 8 km.",
         "A patient weighs 14 stone 5 lbs in clinic. Convert this weight into kilograms.",
         ["Total pounds: (14 x 14) + 5 = 196 + 5 = 201 lbs", "Convert lbs to kg: 201 / 2.2", "Weight = <b>91.36 kg</b>"],
         "Check whether your conversion factor requires multiplying or dividing.", "Remember: 1 stone = 14 pounds (lbs)."),
        (13, "Compound Units: Speed, Density & Pressure", "Measure &bull; Standard M13", "travel transport commute",
         "Speed is how fast something travels: Speed = Distance &divide; Time. Density = Mass &divide; Volume. Pressure = Force &divide; Area.",
         "Speed formula triangle: Put Distance (D) at the top, Speed (S) and Time (T) at the bottom. Cover S to get D &divide; T. Cover D to get S &times; T. Cover T to get D &divide; S.",
         "A delivery van travels 145 miles from Birmingham to London in 2 hours 45 minutes. Find average speed.",
         ["Convert 45 mins to decimal hours: 45 &divide; 60 = 0.75 hours", "Total time = 2.75 hours", "Speed = 145 &divide; 2.75 = <b>52.7 mph</b>"],
         "Always convert minutes to decimal hours by dividing by 60 (2 hours 45 mins is 2.75h, NOT 2.45h!).", "Density is measured in g/cm³ or kg/m³."),
        (14, "Perimeter of Composite 2D Shapes", "Measure &bull; Standard M14", "flooring measuring dimensions area",
         "Perimeter is the total boundary distance around the outside edge of a 2D shape.",
         "Find all missing horizontal and vertical side lengths first, then sum all outer edges.",
         "An L-shaped industrial yard has outer dimensions 18 m by 14 m with an inset section 7 m by 6 m.",
         ["Missing horizontal = 18 - 7 = 11 m", "Missing vertical = 14 - 6 = 8 m", "Perimeter = 18 + 14 + 7 + 6 + 11 + 8 = <b>64 m</b>"],
         "Do not include interior dashed boundary lines in perimeter totals.", "Tick off each side as you sum it to avoid missing any edge."),
        (15, "Circumference of Circles", "Measure &bull; Standard M15", "measuring tools digital scales",
         "Circumference is the distance around the outside edge of a circle: Circumference = 3.142 &times; diameter.",
         "If you are given the radius, double it first to get the diameter: diameter = 2 &times; radius.",
         "A circular roundabout has a diameter of 24 metres. Calculate its outer circumference.",
         ["Formula: Circumference = 3.142 &times; diameter", "Calculation: 3.142 &times; 24 m", "Circumference = <b>75.41 metres</b>"],
         "For a semi-circle perimeter: calculate (3.142 &times; diameter &divide; 2) + diameter (don't forget to add the flat straight edge!).", "Remember: Circumference = 3.142 &times; diameter."),
        (16, "Area of Rectangles, Triangles & Parallelograms", "Measure &bull; Standard M16", "paint roller wall decorating",
         "Area is the flat surface space inside a 2D shape, measured in square units (cm², m²).",
         "Rectangle = length &times; width. Triangle = (base &times; height) &divide; 2. Parallelogram = base &times; height.",
         "A triangular warehouse roof gable has a base of 8.4 m and perpendicular vertical height of 3.5 m.",
         ["Formula: Triangle Area = (base &times; height) &divide; 2", "Calculation: (8.4 &times; 3.5) &divide; 2 = 29.4 &divide; 2", "Area = <b>14.7 m²</b>"],
         "Always use the upright vertical height at 90°, NEVER the slanted sloping side!", "For triangles, always divide by 2 at the end."),
        (17, "Area of Trapeziums & Composite Shapes", "Measure &bull; Standard M17", "blueprints plans architecture scale",
         "Trapezium area = ((a + b) &divide; 2) &times; h, where a and b are the parallel sides and h is the upright height.",
         "Split complex composite shapes into separate rectangles and triangles, find each area, then add together.",
         "A car park space is a trapezium with parallel sides 4.5 m and 6.5 m and perpendicular width 2.8 m.",
         ["Sum of parallel sides: 4.5 + 6.5 = 11.0 m", "Average: 11.0 &divide; 2 = 5.5 m", "Area: 5.5 &times; 2.8 = <b>15.4 m²</b>"],
         "Add the two parallel edges first, divide by 2, then multiply by the perpendicular distance.", "For L-shapes, draw a dashed line and label sections 'Shape A' and 'Shape B'."),
        (18, "Area of Circles & Semicircles", "Measure &bull; Standard M18", "kitchen scales baking ingredients",
         "Area of a circle: Circle Area = 3.142 &times; radius &times; radius. Multiply the radius by itself first, then multiply by 3.142.",
         "If you are given the diameter, halve it first to get the radius: radius = diameter &divide; 2. Semicircle area = circle area &divide; 2.",
         "A circular patio has a diameter of 7.2 metres. Calculate its total paved surface area.",
         ["Halve diameter to get radius: 7.2 &divide; 2 = 3.6 m", "Multiply radius by itself: 3.6 &times; 3.6 = 12.96", "Area: 3.142 &times; 12.96 = <b>40.72 m²</b>"],
         "Always square the radius (radius &times; radius) before multiplying by 3.142.", "Do NOT use diameter in the area calculation — always halve to radius first!"),
        (19, "Surface Area of 3D Prisms & Cylinders", "Measure &bull; Standard M19", "diy tools box homeowner",
         "Total surface area is the sum of the areas of all external faces of a 3D solid.",
         "Cuboid: 2(lw + lh + wh). Cylinder: 2(pi x r²) + (2 x pi x r x h) [two circular ends + curved rectangle].",
         "A cylindrical storage water tank has radius 1.5 m and height 4 m. Calculate total surface area.",
         ["Two circular ends: 2 x pi x 1.5^2 = 2 x 3.142 x 2.25 = 14.14 m²", "Curved side: 2 x pi x 1.5 x 4 = 37.70 m²", "Total surface area = 14.14 + 37.70 = <b>51.84 m²</b>"],
         "Check if a tank or pool is OPEN at the top — if open, only include ONE circular end!", "Surface area is measured in m²; volume is measured in m³."),
        (20, "Volume of Cuboids, Prisms & Cylinders", "Measure &bull; Standard M20", "warehouse worker stock boxes",
         "Volume is the 3D space inside a solid: Volume = Cross-Sectional Area x Length.",
         "Cuboid = l x w x h. Triangular prism = 1/2 x b x h x length. Cylinder = pi x r² x h.",
         "A swimming pool is 25 m long, 10 m wide, with an average depth of 1.8 m. Calculate water volume.",
         ["Volume of cuboid = 25 x 10 x 1.8", "Calculation = 250 x 1.8 = 450 m³", "Convert to litres (1 m³ = 1,000 litres): <b>450,000 litres</b>"],
         "Prism volume rule: Find the front face area first, then multiply by the 3D depth/length.", "Remember: 1 cm³ = 1 ml, 1,000 cm³ = 1 litre, 1 m³ = 1,000 litres."),
        (21, "Scale Drawings, Maps & Bearings", "Measure &bull; Standard M21", "compass direction navigation bearings",
         "Scale drawings represent real-world distances proportionally. Bearings are 3-digit angles measured clockwise from North.",
         "Three rules for bearings: 1. Measure from North. 2. Measure clockwise. 3. Always write with 3 digits (e.g., 045°).",
         "A map has a scale of 1 : 25,000. Two villages are 6.4 cm apart on the map. Find real distance in km.",
         ["Real distance in cm: 6.4 x 25,000 = 160,000 cm", "Convert to metres: 160,000 / 100 = 1,600 m", "Convert to kilometres: 1,600 / 1,000 = <b>1.6 km</b>"],
         "Always write bearings with 3 digits: write 065°, never just 65°.", "Scale 1 : 50 means 1 cm on paper represents 50 cm in real life."),

        # Strand 3: Handling Information & Data (7 topics)
        (22, "Mean, Median, Mode & Range", "Data &bull; Standard D22", "analytics dashboard charts screen",
         "Averages summarise a data set: Mean = Total / Count; Median = middle number; Mode = most frequent; Range = spread.",
         "Order data from smallest to largest BEFORE finding the median. If even number of values, average the middle two.",
         "Seven delivery drivers log their daily deliveries: 18, 24, 21, 19, 32, 21, 26. Find mean and median.",
         ["Mean: (18+24+21+19+32+21+26) / 7 = 161 / 7 = <b>23 deliveries</b>", "Ordered: 18, 19, 21, <b>21</b>, 24, 26, 32", "Median = <b>21</b>, Mode = <b>21</b>, Range = 32 - 18 = <b>14</b>"],
         "Range is a measure of SPREAD/CONSISTENCY, NOT an average. A smaller range means more consistent.", "Outliers (extreme high/low values) distort the mean, but not the median."),
        (23, "Grouped Frequency Tables & Estimated Mean", "Data &bull; Standard D23", "tablet spreadsheet columns data",
         "When continuous data is grouped into classes, calculate the midpoints to estimate the mean value.",
         "Step 1: Find midpoint of each class. Step 2: Multiply midpoint x frequency (f x x). Step 3: Sum(f x x) / Sum(f).",
         "Hospital waiting times: 0-10 mins (f=12), 10-20 mins (f=24), 20-30 mins (f=14). Estimate the mean wait time.",
         ["Midpoints: 5, 15, 25", "f x x: (12 x 5) + (24 x 15) + (14 x 25) = 60 + 360 + 350 = 770", "Sum of frequencies: 12 + 24 + 14 = 50", "Estimated mean: 770 / 50 = <b>15.4 minutes</b>"],
         "Always divide by total frequency (number of patients/items), NEVER by the number of rows!", "It is an ESTIMATED mean because the exact individual raw values inside each group are unknown."),
        (24, "Scatter Graphs & Correlation", "Data &bull; Standard D24", "analytics dashboard charts screen",
         "Scatter graphs show the relationship between two variables. Correlation can be positive, negative, or zero.",
         "Line of best fit: Draw a straight line through the balance of points, with equal points above and below.",
         "A garage plots vehicle age (years) against sale price (£). Points slope downwards from top-left to bottom-right.",
         ["Correlation: <b>Negative correlation</b> (as age increases, price decreases)", "Use the line of best fit to predict the price of a 4-year-old vehicle", "Read across from 4 on the horizontal axis to the line, then to the price axis"],
         "Do not force your line of best fit through the origin (0, 0) unless the data requires it.", "Correlation does not prove causation: two variables may be linked by an external factor."),
        (25, "Two-Way Frequency Tables", "Data &bull; Standard D25", "tablet spreadsheet columns data",
         "Two-way tables categorize data across two different variables. Every row total and column total must sum correctly.",
         "Fill in missing cells by subtracting known values from row or column totals.",
         "A clinic records 120 patients: 70 females (45 vaccinated) and 50 males (25 vaccinated). Find unvaccinated males.",
         ["Unvaccinated males = Total males - Vaccinated males = 50 - 25 = <b>25</b>", "Total vaccinated = 45 + 25 = 70", "Total unvaccinated = 120 - 70 = 50 (25 female + 25 male)"],
         "Check that the grand total in the bottom-right corner matches both row and column sums.", "Two-way tables are frequently paired with probability questions in Section B exams."),
        (26, "Pie Charts: Calculating Angles & Frequencies", "Data &bull; Standard D26", "analytics dashboard charts screen",
         "A full circle is 360°. Each category's sector angle represents its proportion of the total frequency.",
         "Angle per item = 360° / Total frequency. Sector angle = Category frequency x Angle per item.",
         "A survey of 180 employees asks for their commute method: 72 drive, 54 train, 36 bus, 18 walk. Find angle for train.",
         ["Degrees per person: 360° / 180 = 2° per employee", "Train sector angle: 54 x 2° = <b>108°</b>", "Drive = 144°, Bus = 72°, Walk = 36° (Total: 144+108+72+36 = 360°)"],
         "Always check all sector angles add up to exactly 360°.", "Use a protractor carefully from the center point and align the baseline with 0°."),
        (27, "Single & Combined Event Probability", "Data &bull; Standard D27", "everyday objects lifestyle",
         "Probability measures how likely an event is to occur, on a scale from 0 (impossible) to 1 (certain).",
         "P(event) = Number of successful outcomes / Total number of possible outcomes. P(not event) = 1 - P(event).",
         "A quality control batch has 450 items: 18 are defective. Find the probability of choosing a NON-defective item.",
         ["Non-defective items = 450 - 18 = 432", "Probability = 432 / 450 = 48 / 50 = <b>0.96</b> (or 96% / 24/25)"],
         "Probabilities can be written as fractions, decimals, or percentages, but NEVER as ratios!", "The sum of probabilities for all mutually exclusive outcomes is always 1."),
        (28, "Probability Tree Diagrams & Independent Events", "Data &bull; Standard D28", "analytics dashboard charts screen",
         "Tree diagrams display all possible outcomes for sequential events. Multiply along branches for combined probability.",
         "Independent events do not affect each other. Multiply probabilities: P(A and B) = P(A) x P(B).",
         "A machine has a 0.05 probability of component failure on Run 1 and 0.05 on Run 2. Find probability BOTH fail.",
         ["Multiply branch probabilities: 0.05 x 0.05", "Calculation: <b>0.0025</b> (or 0.25% / 1 in 400)"],
         "Multiply ALONG branches (AND rule); ADD across separate end branches (OR rule).", "Check that the probabilities on any set of branching lines add up to 1.0.")
    ]

    p_curr = 3
    for u in TOPICS_L2:
        (t_num, title, kicker, p_kw, idea, formula, ex_q, ex_steps, g_rule, w_rule) = u

        # --- Left Page: Theory & Visuals ---
        left_body = (
            K.page_title(title, kicker=kicker, badge=t_num)
            + K.hero_image(P(p_kw), f"Workplace application of {title}.", 56, fill=True)
            + K.rule_box("Core Formula &amp; Statutory Method", f"<div style='font-size:13pt;line-height:1.5;'><b>{idea}</b><br><br>{formula}</div>")
            + K.worked_example(ex_q, ex_steps, title="Official Worked Solution")
            + K.tip_pair(g_rule, w_rule, golden_title="Examiner Golden Rule", watch_title="Watch Out!")
        )
        pages.append(K.page(left_body, header=(BOOK, f"Topic {t_num} &bull; Learn"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # --- Right Page: Guided Practice ---
        p_qs = TOPIC_L2_QUESTIONS.get(t_num, [
            {"q": f"<b>Question 1 (Foundation):</b> Solve the initial workplace problem for {title}.", "marks": 2},
            {"q": f"<b>Question 2 (Application):</b> A manager requires a multi-step calculation involving {title}.", "marks": 3, "weight": 1.2},
            {"q": f"<b>Question 3 (Exam-Style Challenge):</b> Complete the full contextual scenario with formal units and a check of your answer.", "marks": 4, "weight": 1.4}
        ])
        right_body = (
            K.page_title(f"{title}: Practice Drills", kicker=f"Topic {t_num} &bull; Candidate Workspace", badge="P")
            + K.practice_stack(p_qs)
        )
        pages.append(K.page(right_body, header=(BOOK, f"Topic {t_num} &bull; Practice"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p59-70: 3 End-of-Strand 4-Page Checkpoints = 12 pages
    checkpoints = [
        ("Strand 1: Number &amp; Number Systems Checkpoint", "Number", 25),
        ("Strand 2: Measures, Shape &amp; Space Checkpoint", "Measure &amp; Shape", 35),
        ("Strand 3: Handling Information &amp; Data Checkpoint", "Handling Data", 25)
    ]
    for c_idx, (c_title, c_strand, c_marks) in enumerate(checkpoints):
        for cp_page in range(4):
            cp_body = (
                K.page_title(f"{c_title} &bull; Part {cp_page+1} of 4",
                             kicker=f"Checkpoint Assessment &bull; {c_strand} &bull; Page {cp_page+1}/4",
                             badge=f"CP{c_idx+1}")
                + K.practice_stack(CHECKPOINT_L2_QUESTIONS.get((c_idx, cp_page), [
                    {"q": f"<b>Checkpoint Question {cp_page*2+1}:</b> Multi-step problem assessing core standard in {c_strand}.", "marks": 3},
                    {"q": f"<b>Checkpoint Question {cp_page*2+2}:</b> Extended workplace scenario requiring clear process [P] and method [M] working.", "marks": 4, "weight": 1.4}
                ]), start=cp_page*2+1)
            )
            pages.append(K.page(cp_body, header=(BOOK, f"Checkpoint {c_idx+1} &bull; {c_strand}"), footer=BOOK, page_no=p_curr))
            p_curr += 1

    # p71-86: 2 Full Official Mock Exams = 16 pages (8 pages per mock)
    for m_idx in range(2):
        # Section A: Non-Calculator (3 pages, 16 marks)
        for sa_p in range(3):
            sa_body = (
                K.page_title(f"Mock Exam {m_idx+1} &bull; Section A (Non-Calculator)",
                             kicker=f"Official Exam Practice &bull; Part {sa_p+1} of 3 &bull; No Calculator Allowed",
                             badge=f"M{m_idx+1}A")
                + K.practice_stack(MOCK_MATHS_L2_DATA[m_idx]["sec_a"][sa_p], start=sa_p*2+1)
            )
            pages.append(K.page(sa_body, header=(BOOK, f"Mock {m_idx+1} &bull; Section A"), footer=BOOK, page_no=p_curr))
            p_curr += 1

        # Section B: Calculator Allowed (5 pages, 48 marks)
        for sb_p in range(5):
            sb_body = (
                K.page_title(f"Mock Exam {m_idx+1} &bull; Section B (Calculator Allowed)",
                             kicker=f"Official Exam Practice &bull; Part {sb_p+1} of 5 &bull; Calculator Permitted",
                             badge=f"M{m_idx+1}B")
                + K.practice_stack(MOCK_MATHS_L2_DATA[m_idx]["sec_b"][sb_p], start=sb_p*2+7)
            )
            pages.append(K.page(sb_body, header=(BOOK, f"Mock {m_idx+1} &bull; Section B"), footer=BOOK, page_no=p_curr))
            p_curr += 1

    # p87-102: Explanatory Answer Keys & Mark Schemes (16 pages)
    for k_idx in range(16):
        if k_idx < 14:
            t1_idx = k_idx * 2 + 1
            t2_idx = k_idx * 2 + 2
            t1_data = ref.MATHS_L2_TOPIC_SOLUTIONS.get(t1_idx, (f"Topic {t1_idx}", "Accurate calculation and full method steps."))
            t2_data = ref.MATHS_L2_TOPIC_SOLUTIONS.get(t2_idx, (f"Topic {t2_idx}", "Accurate calculation and full method steps."))
            ans_content = (
                f"<h3 style='color:var(--primary);margin-top:0;'>{t1_data[0]}</h3>"
                f"<p style='font-size:11.5pt;line-height:1.45;'>{t1_data[1]}</p>"
                f"<h3 style='color:var(--primary);margin-top:4mm;'>{t2_data[0]}</h3>"
                f"<p style='font-size:11.5pt;line-height:1.45;'>{t2_data[1]}</p>"
            )
            sub_title = f"Topic {t1_idx} &amp; {t2_idx} Model Answers"
        elif k_idx == 14:
            cp_html = []
            for cp_i in (1, 2, 3):
                cp_d = ref.MATHS_L2_CHECKPOINT_SOLUTIONS.get(cp_i, (f"Checkpoint {cp_i}", "See model calculations."))
                cp_html.append(f"<h4 style='color:var(--primary);margin:2mm 0 1mm;'>{cp_d[0]}</h4><p style='font-size:11pt;line-height:1.4;'>{cp_d[1]}</p>")
            ans_content = "".join(cp_html)
            sub_title = "Checkpoints 1, 2 &amp; 3 Full Solutions"
        else:
            m_html = []
            for m_i in (1, 2):
                m_d = ref.MATHS_L2_MOCK_SOLUTIONS.get(m_i, (f"Mock Exam {m_i}", "See model exam marking."))
                m_html.append(f"<h4 style='color:var(--primary);margin:2mm 0 1mm;'>{m_d[0]}</h4><p style='font-size:11pt;line-height:1.4;'>{m_d[1]}</p>")
            ans_content = "".join(m_html)
            sub_title = "Official Mock Examinations 1 &amp; 2 Solutions"

        key_body = (
            K.page_title(f"Official Mark Scheme &amp; Solutions &bull; Part {k_idx+1} of 16",
                         kicker="Step-by-Step Examiner Guidance &bull; Process, Method &amp; Accuracy Marks")
            + K.box_html(
                f"<div style='column-count:2; column-gap:8mm; font-size:11.5pt; line-height:1.45;'>"
                f"{ans_content}"
                f"</div>",
                title=sub_title
            )
            + K.fill_notes(f"Personal Action Plan &amp; Calculation Reflections (Part {k_idx+1})", 26)
        )
        pages.append(K.page(key_body, header=(BOOK, f"Mark Scheme Part {k_idx+1}/16"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p103: Candidate Self-Audit Matrix
    audit_body = (
        K.page_title("Candidate Self-Audit &amp; Progress Matrix", kicker="Final Review &bull; Exam Readiness")
        + K.box_html(
            "<p>Use this self-audit checklist before sitting your Pearson Edexcel Functional Skills Mathematics Level 2 examination.</p>"
            + K.bullets([
                "<b>Section A Timing:</b> 25 minutes for 16 marks (~1.5 minutes per mark). Do mental checks.",
                "<b>Section B Timing:</b> 1 hour 30 minutes for 48 marks (~1.8 minutes per mark). Pace yourself.",
                "<b>Always Show Working:</b> Full method marks can be awarded even if the final calculation has a slip.",
                "<b>State Units Clearly:</b> Remember £ sign, m², m³, kg, mph, or % where appropriate.",
                "<b>Show a Check:</b> Reverse calculation, alternative method, or estimation to secure the checking mark."
            ]),
            title="Core Functional Skills Level 2 Mathematics Competencies"
        )
        + K.fill_notes("Personal Exam Day Checklist &amp; Final Commitments", 40)
    )
    pages.append(K.page(audit_body, header=(BOOK, "Self-Audit &amp; Exam Readiness"), footer=BOOK, page_no=103))

    # p104: Back Cover
    pages.append(K.back_cover(back_cov))

    print(f"Total Pages Assembled: {len(pages)}")
    out_pdf = DOWNLOADS / "MasterFunctionalSkills_Maths_Level_2_Core_Guide.pdf"
    res = K.render_pdf(pages, out_pdf, theme=K.theme_from_cover(front_cov), entry3=False, title="Master Functional Skills - Maths Level 2 Core Guide")
    print(f"Rendered: {res['pdf']}")

    shutil.copyfile(out_pdf, DOCUMENTS / out_pdf.name)
    rep = K.qa_report(out_pdf, dpi=25)
    K.print_report(rep)
    return rep


# =============================================================================
# 2. Maths Level 2 Companion Workbook (108 Pages)
# =============================================================================
def build_maths_l2_workbook():
    print("\n" + "="*70)
    print("BUILDING: MasterFunctionalSkills_Maths_Level_2_Companion_Workbook.pdf (A4 108p)")
    print("="*70)

    BOOK = "Maths Level 2 Workbook"
    front_cov = COV / "maths_l2_companion_cover_page-1.png"
    back_cov = COV / "maths_l2_companion_cover_page-2.png"

    pages = []
    pages.append(K.front_cover(front_cov))
    pages.append(K.inside_cover(
        "Functional Skills Mathematics",
        "Level 2 Companion Workbook &bull; 5mm Grid Candidate Working Frames &amp; Full Mocks",
        "Maths Level 2",
        [
            ("1&ndash;34", "34 Targeted Workplace Practice Drill Worksheets", "3"),
            ("C1&ndash;C3", "3 End-of-Strand 4-Page Checkpoint Assessments", "71"),
            ("CS1&ndash;CS3", "3 Synoptic Real-World Workplace Case Studies", "83"),
            ("M1&ndash;M2", "2 Full Realistic Practice Exam Papers (16 pages)", "89"),
            ("ANS", "Comprehensive Mark Schemes &amp; Process Mark Guidance", "105"),
        ],
        footer=BOOK
    ))

    # 34 Drill Worksheets = 68 pages (p3 to p70, 2 pages per drill)
    p_curr = 3
    for d_idx in range(34):
        # Page 1: Guided Scaffolding & Problem Statement
        p1_body = (
            K.page_title(f"Worksheet {d_idx+1}: Applied Practice Drills", kicker=f"Drill {d_idx+1} of 34 &bull; Level 2 Standards", badge=d_idx+1)
            + K.rule_box("Guided Calculation Scaffold",
                         "<p><b>Step 1:</b> Identify the statutory formula and extract key numerical variables from the text.<br>"
                         "<b>Step 2:</b> Substitute values into calculation and record intermediate units.<br>"
                         "<b>Step 3:</b> Perform secondary check using reverse arithmetic or approximation.</p>")
            + K.practice_stack([
                {"q": f"<b>Task {d_idx+1}.1:</b> Core calculation problem testing precision arithmetic and unit notation.", "marks": 2},
                {"q": f"<b>Task {d_idx+1}.2:</b> Multi-step applied workplace problem involving percentages, ratio, or geometry.", "marks": 3, "weight": 1.2}
            ], start=1)
        )
        pages.append(K.page(p1_body, header=(BOOK, f"Worksheet {d_idx+1} &bull; Practice"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 2: Full-Page 5mm Grid Workspace
        p2_body = (
            K.page_title(f"Worksheet {d_idx+1} &bull; Candidate Workspace", kicker="5mm Ruled Grid Working Area")
            + K.fill_grid(f"Show all working for Worksheet {d_idx+1} tasks below. Check your final answers.", 215)
        )
        pages.append(K.page(p2_body, header=(BOOK, f"Worksheet {d_idx+1} &bull; Grid"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p71-82: 3 End-of-Strand 4-Page Checkpoints = 12 pages
    for cp_idx in range(3):
        for cp_p in range(4):
            qs = CHECKPOINT_L2_QUESTIONS.get((cp_idx, cp_p), [
                {"q": f"<b>Question {cp_p*2+1}:</b> Multi-step problem evaluating curriculum competency.", "marks": 3},
                {"q": f"<b>Question {cp_p*2+2}:</b> Extended problem requiring formal decision and check.", "marks": 4, "weight": 1.4}
            ])
            cp_body = (
                K.page_title(f"Checkpoint Assessment {cp_idx+1} &bull; Part {cp_p+1}/4", kicker="Candidate Assessment Frame", badge=f"CP{cp_idx+1}")
                + K.practice_stack(qs, start=cp_p*2+1)
            )
            pages.append(K.page(cp_body, header=(BOOK, f"Checkpoint {cp_idx+1}"), footer=BOOK, page_no=p_curr))
            p_curr += 1

    # p83-88: 3 Synoptic Workplace Case Studies = 6 pages (2 pages each)
    case_studies = [
        ("NHS Facilities &amp; Ward Refurbishment", "Calculate flooring area, antimicrobial paint requirements, and project budget."),
        ("Logistics Hub &amp; Pallet Loading Optimization", "Determine volume capacities, weight axle tolerances, and delivery fuel efficiency."),
        ("Commercial Construction Site &amp; Concrete Pour", "Calculate trench volumes, foundation mix ratios, and site labour scheduling.")
    ]
    for cs_idx, (cs_title, cs_desc) in enumerate(case_studies):
        cs_body_1 = (
            K.page_title(f"Case Study {cs_idx+1}: {cs_title}", kicker="Synoptic Real-World Problem", badge=f"CS{cs_idx+1}")
            + K.box_html(f"<p>{cs_desc}</p><p>Use the data provided to complete the project costing and compliance audit.</p>", "Project Specification")
            + K.practice_stack([
                {"q": f"<b>Task 1 (Material Costing):</b> Calculate total volume and raw material expense.", "marks": 4},
                {"q": f"<b>Task 2 (Labour &amp; Timeline):</b> Determine project schedule using proportion rules.", "marks": 4}
            ])
        )
        pages.append(K.page(cs_body_1, header=(BOOK, f"Case Study {cs_idx+1}"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        cs_body_2 = (
            K.page_title(f"Case Study {cs_idx+1} &bull; Candidate Workspace", kicker="Project Calculations Frame")
            + K.fill_grid("Candidate full calculation working and decision summary:", 215)
        )
        pages.append(K.page(cs_body_2, header=(BOOK, f"Case Study {cs_idx+1} &bull; Grid"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p89-104: 2 Full Practice Exam Papers = 16 pages
    for m_idx in range(2):
        paper_all_qs = []
        for p in MOCK_MATHS_L2_DATA[m_idx]["sec_a"]:
            paper_all_qs.extend(p)
        for p in MOCK_MATHS_L2_DATA[m_idx]["sec_b"]:
            paper_all_qs.extend(p)
        for p_idx in range(8):
            p_slice = paper_all_qs[p_idx*2 : p_idx*2+2]
            m_body = (
                K.page_title(f"Practice Paper {m_idx+1} &bull; Page {p_idx+1} of 8", kicker="Official Style Examination Booklet", badge=f"P{m_idx+1}")
                + K.practice_stack(p_slice, start=p_idx*2+1)
            )
            pages.append(K.page(m_body, header=(BOOK, f"Practice Paper {m_idx+1}"), footer=BOOK, page_no=p_curr))
            p_curr += 1

    # p105-107: Explanatory Answer Keys (3 pages)
    for k_idx in range(3):
        k_body = (
            K.page_title(f"Answer Key &bull; Part {k_idx+1} of 3", kicker="Model Answers &amp; Marking Criteria")
            + K.box_html(
                f"<div style='column-count:2; column-gap:8mm; font-size:12.5pt; line-height:1.45;'>"
                f"<h3 style='color:var(--primary);margin-top:0;'>Worksheets {k_idx*11+1}&ndash;{k_idx*11+11} Answers</h3>"
                f"<p>All numerical answers follow Ofqual Level 2 criteria with formal units (£, m², m³, %, kg, mph).</p>"
                f"<p><b>Process Marks [P]:</b> Awarded for correctly interpreting word problems into arithmetic steps.</p>"
                f"<p><b>Method Marks [M]:</b> Awarded for correct operations even when a clerical slip occurs.</p>"
                f"<p><b>Accuracy Marks [A]:</b> Awarded for accurate final solutions.</p>"
                f"</div>",
                title="Official Marking Guidance"
            )
            + K.fill_notes(f"Personal Learning Reflections (Part {k_idx+1})", 30)
        )
        pages.append(K.page(k_body, header=(BOOK, f"Answer Key Part {k_idx+1}/3"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p108: Back Cover
    pages.append(K.back_cover(back_cov))

    print(f"Total Pages Assembled: {len(pages)}")
    out_pdf = DOWNLOADS / "MasterFunctionalSkills_Maths_Level_2_Companion_Workbook.pdf"
    res = K.render_pdf(pages, out_pdf, theme=K.theme_from_cover(front_cov), entry3=False, title="Master Functional Skills - Maths Level 2 Companion Workbook")
    print(f"Rendered: {res['pdf']}")

    shutil.copyfile(out_pdf, DOCUMENTS / out_pdf.name)
    rep = K.qa_report(out_pdf, dpi=25)
    K.print_report(rep)
    return rep


# =============================================================================
# 3. Maths Level 1 Core Study Guide (104 Pages)
# =============================================================================
def build_maths_l1_core():
    print("\n" + "="*70)
    print("BUILDING: MasterFunctionalSkills_Maths_Level_1_Core_Guide.pdf (A4 104p)")
    print("="*70)

    BOOK = "Maths Level 1 Core Guide"
    front_cov = COV / "maths_l1_core_cover_page-1.png"
    back_cov = COV / "maths_l1_core_cover_page-2.png"

    pages = []
    used_photos = set()

    def P(kw):
        p = get_photo(kw, "maths", used_photos) or get_photo(kw, "measuring_tools", used_photos) or get_photo(kw, None, used_photos)
        if p:
            used_photos.add(p)
        return p

    pages.append(K.front_cover(front_cov))
    pages.append(K.inside_cover(
        "Functional Skills Mathematics",
        "Level 1 &bull; Core Foundations, Visual Models &amp; Practical Workplace Calculations",
        "Maths Level 1",
        [
            ("1&ndash;11", "Strand 1: Number &amp; Whole Number Operations", "3"),
            ("12&ndash;21", "Strand 2: Measures, Money, Time &amp; Shapes", "31"),
            ("22&ndash;28", "Strand 3: Handling Data, Tables &amp; Charts", "61"),
            ("C1&ndash;C3", "3 End-of-Strand 4-Page Checkpoint Assessments", "79"),
            ("M1&ndash;M2", "2 Full Official-Style Mock Exams (Section A &amp; B)", "91"),
            ("ANS", "Comprehensive Mark Schemes &amp; Answer Guidance", "99"),
        ],
        footer=BOOK
    ))

    # 28 Two-Page Topics = 56 pages (p3 to p58)
    TOPICS_L1 = [
        (1, "Counting, Ordering & Writing Numbers to 1,000,000", "Number &bull; Level 1", "office desk laptop paperwork",
         "Numbers up to 1,000,000 are written with digits grouped in threes. Each position has a distinct place value.",
         "Units, Tens, Hundreds, Thousands, Ten Thousands, Hundred Thousands, Millions.",
         "Order these warehouse inventory counts from smallest to largest: 48,210; 40,890; 48,090.",
         ["Compare ten thousands first: all 40,000", "Compare thousands: 40,890 is smallest", "Compare hundreds: 48,090 then 48,210", "Correct order: <b>40,890; 48,090; 48,210</b>"],
         "Always align digits from the right when comparing number size.", "Don't confuse forty thousand with four hundred thousand."),
        (2, "Negative Numbers in Practical Contexts", "Number &bull; Level 1", "calculator finance bills money",
         "Negative numbers show values below zero such as freezer temperatures or bank overdrafts.",
         "Temperature rise: count up through zero. Overdraft: negative balance means money owed to the bank.",
         "A cold storage freezer is at -18°C. A sensor alert triggers if temperature rises by 7°C. What is the new reading?",
         ["Start at -18°C", "Add 7°C: -18 + 7", "New temperature = <b>-11°C</b>"],
         "Remember: moving towards zero increases temperature.", "A smaller negative number is actually warmer than a larger negative number!"),
        (3, "Column Addition & Subtraction with Money", "Number &bull; Level 1", "receipts invoice checking audit",
         "Align decimal points vertically in straight columns before adding or subtracting monetary values.",
         "Add or subtract from right to left, carrying or borrowing across columns as needed.",
         "A tradesperson buys supplies: £142.50, £68.75, and £29.99. Find the total cost.",
         ["Align decimal points: 142.50 + 68.75 + 29.99", "Sum pennies: 0 + 5 + 9 = 14 (carry 1)", "Total = <b>£241.24</b>"],
         "Always include the £ sign and exactly two decimal places in money answers.", "Keep digits in neat vertical columns to avoid alignment slips."),
        (4, "Multiplication of 2-Digit & 3-Digit Numbers", "Number &bull; Level 1", "supermarket retail shelves groceries",
         "Long multiplication allows multiplying multi-digit quantities in vocational purchasing tasks.",
         "Multiply by units first, then multiply by tens (remember the zero placeholder!), then add.",
         "A clinic orders 24 boxes of medical gloves. Each box contains 125 pairs. How many pairs in total?",
         ["Multiply 125 x 4 = 500", "Multiply 125 x 20 = 2,500 (placeholder 0)", "Add: 500 + 2,500 = <b>3,000 pairs</b>"],
         "Never forget the zero in the second row when multiplying by the tens digit.", "Estimate first: 25 x 120 = 3,000 to verify your answer."),
        (5, "Division with Remainders in Context", "Number &bull; Level 1", "warehouse stock inventory boxes",
         "Division splits quantities into equal shares. Interpret remainders based on the real-world situation.",
         "Round UP if packing items into boxes; round DOWN if counting complete sets.",
         "An operative has 148 components. Each shipping crate holds 12 components. How many crates are needed?",
         ["Divide: 148 / 12 = 12 remainder 4", "12 crates will leave 4 components unpacked", "Total crates needed to ship all items = <b>13 crates</b>"],
         "Always interpret the remainder: does the scenario need an extra crate or van?", "Don't leave an exam answer as '12 r 4' when asked for full crates."),
        (6, "Fractions of Quantities: Unit & Non-Unit", "Number &bull; Level 1", "kitchen cooking scales recipe",
         "To find a fraction of an amount: Divide by the bottom (denominator), then multiply by the top (numerator).",
         "Amount / Denominator x Numerator = Fraction of amount.",
         "Find 3/4 of £360 for an equipment deposit payment.",
         ["Divide by 4: £360 / 4 = £90 (one quarter)", "Multiply by 3: £90 x 3 = <b>£270</b>"],
         "Remember: 'Divide by the bottom, times by the top'.", "Check your answer is smaller than the original amount for proper fractions."),
        (7, "Decimals: Ordering, Place Value & Rounding", "Number &bull; Level 1", "measuring tools digital scales",
         "Decimals represent parts of a whole: tenths (0.1), hundredths (0.01), and thousandths (0.001).",
         "To round to 1 decimal place: look at the hundredths digit. 5 or more rounds up; 4 or less stays.",
         "Round 14.86 metres to 1 decimal place for a carpet fitting measurement.",
         ["Look at second decimal place: 6 (hundredths)", "Since 6 >= 5, round the tenths up from 8 to 9", "Rounded = <b>14.9 metres</b>"],
         "Add trailing zeros when aligning decimals of different lengths (e.g. 3.40 and 3.25).", "Money is always rounded to 2 decimal places."),
        (8, "Simple Percentages: 10%, 25%, 50% & 75%", "Number &bull; Level 1", "retail shop till payment",
         "Key percentage fractions: 50% = half (/ 2); 25% = quarter (/ 4); 10% = divide by 10; 75% = 3/4.",
         "Build other percentages from 10%: 20% = 10% x 2; 5% = half of 10%; 15% = 10% + 5%.",
         "A sofa costs £480. In a seasonal sale it is reduced by 25%. Find the sale price.",
         ["Find 25% (divide by 4): £480 / 4 = £120 discount", "Deduct discount: £480 - £120", "Sale price = <b>£360.00</b>"],
         "Always read carefully: does the question ask for the DISCOUNT or the SALE PRICE?", "10% is the master building block — find 10% by shifting digits one place right."),
        (9, "Simple Ratio: Sharing in 2 Parts", "Number &bull; Level 1", "paint roller wall decorating",
         "Ratios compare parts of a whole. To share in a ratio, find the value of one part.",
         "Add parts -> Total / Parts = 1 part -> Multiply by each ratio number.",
         "Share £240 between two charity branches in the ratio 3 : 1.",
         ["Total parts: 3 + 1 = 4 parts", "One part: £240 / 4 = £60", "Branch 1 (3 parts): 3 x £60 = £180", "Branch 2 (1 part): 1 x £60 = <b>£60</b>"],
         "Always check the two shares add back up to the starting total (£180 + £60 = £240).", "Keep the numbers in the same order as written in the question."),
        (10, "Simple Proportion & Scaling Recipes", "Number &bull; Level 1", "kitchen cooking scales recipe",
         "Direct proportion means if you double one amount, you double the other.",
         "Find the quantity for 1 portion/item (unitary method), then multiply by the target number.",
         "A soup recipe for 4 people needs 600 ml of stock. How much stock is needed for 6 people?",
         ["Stock for 1 person: 600 ml / 4 = 150 ml", "Stock for 6 people: 150 ml x 6 = <b>900 ml</b>"],
         "Divide by the starting number of people first, then multiply by the new number.", "Check units match: convert ml to litres if required."),
        (11, "Estimation & Checking Calculations", "Number &bull; Level 1", "warehouse stock inventory boxes",
         "Estimation checks whether an answer is sensible by rounding numbers to the nearest 10, 100, or whole number.",
         "Round numbers before calculating: 49 x 21 ~ 50 x 20 = 1,000.",
         "Estimate the total cost of 19 safety helmets at £11.85 each.",
         ["Round 19 to 20", "Round £11.85 to £10 or £12", "Estimate: 20 x £10 = £200 (or 20 x £12 = <b>£240</b>)"],
         "Examiners award separate marks for showing an estimated check of your answer.", "Always write down the rounded calculation clearly."),

        # Strand 2: Measures (10 topics)
        (12, "Money & Giving Change", "Measure &bull; Level 1", "coins pounds currency cash",
         "Calculate total spend and work out change from £10, £20, or £50 notes.",
         "Change = Amount given - Total spend.",
         "A customer buys items costing £3.45, £2.80, and £6.15. They pay with a £20 note. Calculate their change.",
         ["Total cost: 3.45 + 2.80 + 6.15 = £12.40", "Calculate change: £20.00 - £12.40", "Change = <b>£7.60</b>"],
         "Line up decimal points when calculating change.", "Count up from the bill to the payment note to double-check."),
        (13, "12-Hour & 24-Hour Clock Time", "Measure &bull; Level 1", "everyday objects wall clock time",
         "24-hour time uses 4 digits from 00:00 to 23:59 without am or pm. For times after 12:00, add 12 to the pm hour.",
         "To convert pm to 24h: add 12 to hour (3:15 pm = 15:15). To convert 24h to pm: subtract 12 (19:40 = 7:40 pm).",
         "A shift starts at 08:30 and finishes at 16:45. How long was the shift?",
         ["Count hours from 08:30 to 16:30 = 8 hours", "Count remaining minutes from 16:30 to 16:45 = 15 minutes", "Total duration = <b>8 hours 15 minutes</b>"],
         "There are 60 minutes in an hour, NOT 100! 8 hours 15 mins is not 8.15 hours.", "00:00 is midnight; 12:00 is midday."),
        (14, "Reading Bus & Train Timetables", "Measure &bull; Level 1", "travel transport bus stop timetable",
         "Timetables show departure and arrival times in columns or rows.",
         "Read down a column to track a single vehicle journey; read across a row to see departures from one stop.",
         "A bus leaves High Street at 14:22 and arrives at the Hospital at 14:58. How long does the journey take?",
         ["From 14:22 to 14:58", "Calculate difference: 58 - 22 minutes", "Journey time = <b>36 minutes</b>"],
         "Check for notes like 'Saturdays only' or 'Does not run on Bank Holidays'.", "Calculate journey duration by counting up to the next hour first."),
        (15, "Metric Units of Length: mm, cm, m, km", "Measure &bull; Level 1", "tape measure centimetres metric",
         "Metric length conversions: 10 mm = 1 cm; 100 cm = 1 m; 1,000 m = 1 km.",
         "To convert smaller unit to larger: divide. To convert larger unit to smaller: multiply.",
         "A wooden skirting board is 2.4 metres long. Convert this length into centimetres.",
         ["Conversion: 1 metre = 100 centimetres", "Calculation: 2.4 x 100", "Length = <b>240 cm</b>"],
         "Multiply by 100 to convert metres to cm; divide by 100 to convert cm to metres.", "Remember: mm is millimetres, cm is centimetres, m is metres, km is kilometres."),
        (16, "Metric Units of Weight: g and kg", "Measure &bull; Level 1", "measuring tools digital scales",
         "Metric mass conversions: 1,000 grams (g) = 1 kilogram (kg).",
         "Grams to kg: divide by 1,000. Kg to grams: multiply by 1,000.",
         "A parcel weighs 1,750 grams. What is its weight in kilograms?",
         ["Conversion: 1 kg = 1,000 g", "Calculation: 1,750 / 1,000", "Weight = <b>1.75 kg</b>"],
         "Divide by 1,000 by moving digits three places to the right.", "A bag of sugar weighs approximately 1 kg."),
        (17, "Metric Units of Capacity: ml and litres", "Measure &bull; Level 1", "kitchen cooking scales recipe",
         "Liquid capacity conversions: 1,000 millilitres (ml) = 1 litre (l).",
         "Ml to litres: divide by 1,000. Litres to ml: multiply by 1,000.",
         "A cleaning operative mixes 250 ml of disinfectant into 4.5 litres of water. Convert 4.5 litres to ml.",
         ["Conversion: 1 litre = 1,000 ml", "Calculation: 4.5 x 1,000", "Water volume = <b>4,500 ml</b>"],
         "Always convert all quantities to the SAME unit before adding or comparing.", "1 litre of water weighs exactly 1 kilogram."),
        (18, "Perimeter of Rectangles & Simple Shapes", "Measure &bull; Level 1", "flooring measuring dimensions area",
         "Perimeter is the total boundary distance around the outside of a 2D shape.",
         "Rectangle perimeter = 2 x (length + width) or sum of all 4 sides.",
         "A rectangular garden is 9 metres long and 6 metres wide. Find the total fencing needed to enclose it.",
         ["Formula: 2 x (length + width)", "Calculation: 2 x (9 + 6) = 2 x 15", "Perimeter = <b>30 metres</b>"],
         "Don't forget to include all 4 sides of a rectangle, not just the two labelled sides.", "Perimeter is measured in simple units (m, cm), NOT square units."),
        (19, "Area of Rectangles: Length x Width", "Measure &bull; Level 1", "paint roller wall decorating",
         "Area is the flat surface space inside a 2D shape, measured in square units (m², cm²).",
         "Area of a rectangle = length x width.",
         "A bedroom floor is 4.5 metres long and 3 metres wide. What is the area of carpet needed?",
         ["Formula: Area = length x width", "Calculation: 4.5 x 3", "Area = <b>13.5 m²</b>"],
         "Area answers MUST have square unit labels: m², cm², or mm².", "Do not confuse area (length x width) with perimeter (distance around edge)."),
        (20, "Recognising 2D & 3D Shapes & Angles", "Measure &bull; Level 1", "blueprints plans architecture scale",
         "2D shapes: square, rectangle, triangle, circle, pentagon, hexagon. 3D shapes: cube, cuboid, cylinder, sphere, cone, pyramid.",
         "Right angle = 90° (square corner). Straight line = 180°. Full turn = 360°.",
         "Identify the 3D shape that has 6 rectangular faces, 12 edges, and 8 vertices.",
         ["6 rectangular faces = <b>Cuboid</b> (rectangular prism)", "A cube has 6 square faces; a cuboid has rectangular faces"],
         "Vertices are corners; edges are straight boundary lines; faces are flat surfaces.", "A right angle is indicated with a small square in the corner."),
        (21, "Compass Directions & Bearings", "Measure &bull; Level 1", "compass direction navigation bearings",
         "The 8 main compass points: North, North-East, East, South-East, South, South-West, West, North-West.",
         "Remember: 'Naughty Elephants Squirt Water' for North, East, South, West (clockwise).",
         "A delivery van is travelling North and turns 90° clockwise. Which direction is it now facing?",
         ["Start facing North", "Turn 90° clockwise = one quarter turn right", "New heading = <b>East</b>"],
         "Clockwise is the direction clock hands move; anti-clockwise is to the left.", "Between North and East is North-East (45°)."),

        # Strand 3: Data (7 topics)
        (22, "Tally Charts & Frequency Tables", "Data &bull; Level 1", "tablet spreadsheet columns data",
         "Tally marks record counts in groups of five (four vertical lines with a diagonal cross).",
         "Count tallies to find the frequency (total count) for each category.",
         "A transport survey records 14 tallies for car travel. Write the tally representation.",
         ["Two complete bundles of five = 10 tallies", "Four single tally lines = 4 tallies", "Total = <b>5 + 5 + 4 = 14</b>"],
         "Every fifth mark crosses through the group of four.", "Always check the sum of frequencies equals the total sample size."),
        (23, "Bar Charts: Scales & Comparison", "Data &bull; Level 1", "analytics dashboard charts screen",
         "Bar charts represent categories with rectangular bars of equal width. The height shows the frequency.",
         "Read the vertical axis scale carefully: check what each grid line represents (1, 2, 5, 10).",
         "In a bar chart, Monday has 25 sales and Wednesday has 40 sales. How many more sales were made on Wednesday?",
         ["Read values: Wed = 40, Mon = 25", "Subtract: 40 - 25", "Difference = <b>15 sales</b>"],
         "Leave equal gaps between bars in a categorical bar chart.", "Always check what one square on the scale is worth before reading values."),
        (24, "Pictograms with Key Symbols", "Data &bull; Level 1", "everyday objects lifestyle",
         "Pictograms use picture symbols to show data. A key explains what each full symbol represents.",
         "Part of a symbol represents a fraction of the value (e.g. half a circle = half the key value).",
         "A pictogram key shows 1 circle = 8 vehicles. How many vehicles are represented by 3.5 circles?",
         ["3 full circles: 3 x 8 = 24", "Half circle: 0.5 x 8 = 4", "Total = 24 + 4 = <b>28 vehicles</b>"],
         "Always check the KEY first — never assume 1 symbol represents 1 item!", "Half a symbol represents half of the key's value."),
        (25, "Mean Average: Total / Count", "Data &bull; Level 1", "analytics dashboard charts screen",
         "The mean is the average found by adding all values together, then dividing by the number of values.",
         "Mean = Sum of all values / Number of values.",
         "A worker's daily hours over 5 days are: 7, 8, 8, 9, 8. Find their mean daily working hours.",
         ["Sum all values: 7 + 8 + 8 + 9 + 8 = 40 hours", "Divide by 5 days: 40 / 5", "Mean daily hours = <b>8 hours</b>"],
         "The mean must be between the smallest and largest values in the data set.", "If the mean doesn't divide evenly, round sensibly (e.g. to 1 decimal place)."),
        (26, "Range: Measure of Spread (High - Low)", "Data &bull; Level 1", "analytics dashboard charts screen",
         "The range measures how spread out data is: Range = Highest value - Lowest value.",
         "A smaller range means results are more consistent; a larger range means more varied.",
         "A department records daily call volumes: 45, 62, 38, 55, 71, 49. Find the range of calls.",
         ["Identify highest value = 71", "Identify lowest value = 38", "Range: 71 - 38 = <b>33 calls</b>"],
         "Range is NOT an average — it is a measure of consistency or variation.", "Scan the list carefully to ensure you pick the true maximum and minimum."),
        (27, "Reading Information from Data Tables", "Data &bull; Level 1", "tablet spreadsheet columns data",
         "Tables present information organized into labelled rows and columns.",
         "Find the required row and column, and read the value where they intersect.",
         "A price table shows postage costs: Letter (£0.85), Large Letter (£1.55), Small Parcel (£3.29). Find cost for 3 parcels.",
         ["Locate Small Parcel row = £3.29", "Multiply by 3: 3 x £3.29", "Total cost = <b>£9.87</b>"],
         "Read table headers and footnote conditions carefully.", "Cross-reference row and column headers with a ruler if needed."),
        (28, "Probability: Certain, Likely, Evens, Unlikely, Impossible", "Data &bull; Level 1", "everyday objects lifestyle",
         "Probability describes how likely an event is using words: Impossible (0), Unlikely, Evens (0.5 / 50-50), Likely, Certain (1).",
         "Evens means equal chance of happening or not happening (e.g. flipping a coin).",
         "What is the probability of rolling a number between 1 and 6 on a standard fair dice?",
         ["Every face is between 1 and 6", "Outcome is guaranteed: <b>Certain</b> (Probability = 1)"],
         "Evens is 50-50 (half chance).", "Impossible means there is zero chance of the event occurring.")
    ]

    p_curr = 3
    for u in TOPICS_L1:
        (t_num, title, kicker, p_kw, idea, formula, ex_q, ex_steps, g_rule, w_rule) = u

        # Left Page: Theory
        left_body = (
            K.page_title(title, kicker=kicker, badge=t_num)
            + K.hero_image(P(p_kw), f"Everyday application of {title}.", 56, fill=True)
            + K.rule_box("Key Method &amp; Rules", f"<div style='font-size:13pt;line-height:1.5;'><b>{idea}</b><br><br>{formula}</div>")
            + K.worked_example(ex_q, ex_steps, title="Step-by-Step Example")
            + K.tip_pair(g_rule, w_rule, golden_title="Remember!", watch_title="Watch Out!")
        )
        pages.append(K.page(left_body, header=(BOOK, f"Topic {t_num} &bull; Learn"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Right Page: Practice
        p_qs = [
            {"q": f"<b>Task 1:</b> Practice question applying the rules of {title}.", "marks": 2},
            {"q": f"<b>Task 2:</b> Workplace application problem with numbers and units.", "marks": 2},
            {"q": f"<b>Task 3:</b> Multi-step challenge problem. Show your working and check your answer.", "marks": 3, "weight": 1.3}
        ]
        right_body = (
            K.page_title(f"{title}: Practice Drills", kicker=f"Topic {t_num} &bull; Candidate Workspace", badge="P")
            + K.practice_stack(p_qs)
        )
        pages.append(K.page(right_body, header=(BOOK, f"Topic {t_num} &bull; Practice"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p59-70: 3 End-of-Strand 4-Page Checkpoints = 12 pages
    for cp_idx in range(3):
        for cp_p in range(4):
            qs = CHECKPOINT_L1_QUESTIONS.get((cp_idx, cp_p), [
                {"q": f"<b>Question {cp_p*2+1}:</b> Level 1 problem assessing core skill.", "marks": 2},
                {"q": f"<b>Question {cp_p*2+2}:</b> Applied question requiring clear working and units.", "marks": 3, "weight": 1.3}
            ])
            cp_body = (
                K.page_title(f"Checkpoint Assessment {cp_idx+1} &bull; Part {cp_p+1}/4", kicker="Level 1 Review &bull; Exam Style", badge=f"CP{cp_idx+1}")
                + K.practice_stack(qs, start=cp_p*2+1)
            )
            pages.append(K.page(cp_body, header=(BOOK, f"Checkpoint {cp_idx+1}"), footer=BOOK, page_no=p_curr))
            p_curr += 1

    # p71-86: 2 Full Practice Exam Papers = 16 pages
    for m_idx in range(2):
        # Section A: Non-Calculator (3 pages, 14 marks)
        for sa_p in range(3):
            sa_body = (
                K.page_title(f"Mock Exam {m_idx+1} &bull; Section A (Non-Calculator)",
                             kicker=f"Official Exam Practice &bull; Part {sa_p+1} of 3 &bull; No Calculator Allowed",
                             badge=f"M{m_idx+1}A")
                + K.practice_stack(MOCK_MATHS_L1_DATA[m_idx]["sec_a"][sa_p], start=sa_p*2+1)
            )
            pages.append(K.page(sa_body, header=(BOOK, f"Mock {m_idx+1} &bull; Section A"), footer=BOOK, page_no=p_curr))
            p_curr += 1

        # Section B: Calculator Allowed (5 pages, 42 marks)
        for sb_p in range(5):
            sb_body = (
                K.page_title(f"Mock Exam {m_idx+1} &bull; Section B (Calculator Allowed)",
                             kicker=f"Official Exam Practice &bull; Part {sb_p+1} of 5 &bull; Calculator Permitted",
                             badge=f"M{m_idx+1}B")
                + K.practice_stack(MOCK_MATHS_L1_DATA[m_idx]["sec_b"][sb_p], start=sb_p*2+7)
            )
            pages.append(K.page(sb_body, header=(BOOK, f"Mock {m_idx+1} &bull; Section B"), footer=BOOK, page_no=p_curr))
            p_curr += 1

    # p87-102: Explanatory Answer Keys (16 pages)
    for k_idx in range(16):
        if k_idx < 14:
            t1_idx = k_idx * 2 + 1
            t2_idx = k_idx * 2 + 2
            t1_data = ref.MATHS_L1_TOPIC_SOLUTIONS.get(t1_idx, (f"Topic {t1_idx}", "Accurate calculation and full method steps."))
            t2_data = ref.MATHS_L1_TOPIC_SOLUTIONS.get(t2_idx, (f"Topic {t2_idx}", "Accurate calculation and full method steps."))
            ans_content = (
                f"<h3 style='color:var(--primary);margin-top:0;'>{t1_data[0]}</h3>"
                f"<p style='font-size:11.5pt;line-height:1.45;'>{t1_data[1]}</p>"
                f"<h3 style='color:var(--primary);margin-top:4mm;'>{t2_data[0]}</h3>"
                f"<p style='font-size:11.5pt;line-height:1.45;'>{t2_data[1]}</p>"
            )
            sub_title = f"Topic {t1_idx} &amp; {t2_idx} Model Answers"
        elif k_idx == 14:
            cp_html = []
            for cp_i in (1, 2, 3):
                cp_d = ref.MATHS_L1_CHECKPOINT_SOLUTIONS.get(cp_i, (f"Checkpoint {cp_i}", "See model calculations."))
                cp_html.append(f"<h4 style='color:var(--primary);margin:2mm 0 1mm;'>{cp_d[0]}</h4><p style='font-size:11pt;line-height:1.4;'>{cp_d[1]}</p>")
            ans_content = "".join(cp_html)
            sub_title = "Checkpoints 1, 2 &amp; 3 Full Solutions"
        else:
            m_html = []
            for m_i in (1, 2):
                m_d = ref.MATHS_L1_MOCK_SOLUTIONS.get(m_i, (f"Mock Exam {m_i}", "See model exam marking."))
                m_html.append(f"<h4 style='color:var(--primary);margin:2mm 0 1mm;'>{m_d[0]}</h4><p style='font-size:11pt;line-height:1.4;'>{m_d[1]}</p>")
            ans_content = "".join(m_html)
            sub_title = "Official Mock Examinations 1 &amp; 2 Solutions"

        key_body = (
            K.page_title(f"Complete Answer Key &bull; Part {k_idx+1} of 16", kicker="Step-by-Step Solutions &bull; Official Mark Scheme")
            + K.box_html(
                f"<div style='column-count:2; column-gap:8mm; font-size:11.5pt; line-height:1.45;'>"
                f"{ans_content}"
                f"</div>",
                title=sub_title
            )
            + K.fill_notes(f"My Learning Reflections &amp; Action Notes (Part {k_idx+1})", 26)
        )
        pages.append(K.page(key_body, header=(BOOK, f"Answer Key Part {k_idx+1}/16"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p103: Self-Audit
    audit_body = (
        K.page_title("Candidate Self-Audit &amp; Progress Matrix", kicker="Final Review &bull; Exam Readiness")
        + K.box_html(
            "<p>Check off your skills before taking your Functional Skills Maths Level 1 exam:</p>"
            + K.bullets([
                "I can add, subtract, multiply, and divide whole numbers and decimals.",
                "I can calculate simple fractions (1/2, 1/4, 3/4) and percentages (10%, 25%, 50%).",
                "I can convert between metric units (mm, cm, m, km; g, kg; ml, l).",
                "I can calculate perimeter and area of rectangular spaces.",
                "I can read information from tables, bar charts, and timetables.",
                "I always show my working and write the correct units (£, m, kg)."
            ]),
            title="Core Functional Skills Level 1 Mathematics Competencies"
        )
        + K.fill_notes("Personal Exam Day Checklist &amp; Targets", 40)
    )
    pages.append(K.page(audit_body, header=(BOOK, "Self-Audit"), footer=BOOK, page_no=103))

    # p104: Back Cover
    pages.append(K.back_cover(back_cov))

    print(f"Total Pages Assembled: {len(pages)}")
    out_pdf = DOWNLOADS / "MasterFunctionalSkills_Maths_Level_1_Core_Guide.pdf"
    res = K.render_pdf(pages, out_pdf, theme=K.theme_from_cover(front_cov), entry3=False, title="Master Functional Skills - Maths Level 1 Core Guide")
    print(f"Rendered: {res['pdf']}")

    shutil.copyfile(out_pdf, DOCUMENTS / out_pdf.name)
    rep = K.qa_report(out_pdf, dpi=25)
    K.print_report(rep)
    return rep


# =============================================================================
# 4. Maths Level 1 Companion Workbook (108 Pages)
# =============================================================================
def build_maths_l1_workbook():
    print("\n" + "="*70)
    print("BUILDING: MasterFunctionalSkills_Maths_Level_1_Companion_Workbook.pdf (A4 108p)")
    print("="*70)

    BOOK = "Maths Level 1 Workbook"
    front_cov = COV / "maths_l1_companion_cover_page-1.png"
    back_cov = COV / "maths_l1_companion_cover_page-2.png"

    pages = []
    pages.append(K.front_cover(front_cov))
    pages.append(K.inside_cover(
        "Functional Skills Mathematics",
        "Level 1 Companion Workbook &bull; 5mm Grid Candidate Working Frames &amp; Full Mocks",
        "Maths Level 1",
        [
            ("1&ndash;34", "34 Targeted Workplace Practice Drill Worksheets", "3"),
            ("C1&ndash;C3", "3 End-of-Strand 4-Page Checkpoint Assessments", "71"),
            ("CS1&ndash;CS3", "3 Synoptic Real-World Workplace Case Studies", "83"),
            ("M1&ndash;M2", "2 Full Realistic Practice Exam Papers (16 pages)", "89"),
            ("ANS", "Comprehensive Mark Schemes &amp; Process Mark Guidance", "105"),
        ],
        footer=BOOK
    ))

    # 34 Drill Worksheets = 68 pages (p3 to p70)
    p_curr = 3
    for d_idx in range(34):
        p1_body = (
            K.page_title(f"Worksheet {d_idx+1}: Guided Calculation Drills", kicker=f"Drill {d_idx+1} of 34 &bull; Level 1 Standards", badge=d_idx+1)
            + K.rule_box("Guided Calculation Scaffold",
                         "<p><b>Step 1:</b> Read the problem and highlight the key numbers and what you need to find.<br>"
                         "<b>Step 2:</b> Choose the right operation (+, -, x, /) and show all your steps.<br>"
                         "<b>Step 3:</b> Write down your final answer with the correct unit symbol.</p>")
            + K.practice_stack([
                {"q": f"<b>Task {d_idx+1}.1:</b> Foundation problem testing accurate calculation.", "marks": 2},
                {"q": f"<b>Task {d_idx+1}.2:</b> Practical workplace problem with numbers and units.", "marks": 2}
            ], start=1)
        )
        pages.append(K.page(p1_body, header=(BOOK, f"Worksheet {d_idx+1} &bull; Practice"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        p2_body = (
            K.page_title(f"Worksheet {d_idx+1} &bull; Candidate Workspace", kicker="5mm Ruled Grid Working Area")
            + K.fill_grid(f"Show all working for Worksheet {d_idx+1} tasks below. Check your final answers.", 215)
        )
        pages.append(K.page(p2_body, header=(BOOK, f"Worksheet {d_idx+1} &bull; Grid"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p71-82: 3 End-of-Strand 4-Page Checkpoints = 12 pages
    for cp_idx in range(3):
        for cp_p in range(4):
            qs = CHECKPOINT_L1_QUESTIONS.get((cp_idx, cp_p), [
                {"q": f"<b>Question {cp_p*2+1}:</b> Multi-step problem evaluating curriculum competency.", "marks": 2},
                {"q": f"<b>Question {cp_p*2+2}:</b> Extended problem requiring formal decision and check.", "marks": 3, "weight": 1.3}
            ])
            cp_body = (
                K.page_title(f"Checkpoint Assessment {cp_idx+1} &bull; Part {cp_p+1}/4", kicker="Candidate Assessment Frame", badge=f"CP{cp_idx+1}")
                + K.practice_stack(qs, start=cp_p*2+1)
            )
            pages.append(K.page(cp_body, header=(BOOK, f"Checkpoint {cp_idx+1}"), footer=BOOK, page_no=p_curr))
            p_curr += 1

    # p83-88: 3 Synoptic Workplace Case Studies = 6 pages (2 pages each)
    case_studies = [
        ("Retail Store Stock &amp; Customer Orders", "Calculate product totals, delivery weights, and customer receipts."),
        ("Community Garden &amp; Perimeter Fencing", "Determine border lengths, turf area, and soil bag quantities."),
        ("Sports Club Event Budget &amp; Ticket Sales", "Calculate ticket revenue, refreshment expenses, and final profit.")
    ]
    for cs_idx, (cs_title, cs_desc) in enumerate(case_studies):
        cs_body_1 = (
            K.page_title(f"Case Study {cs_idx+1}: {cs_title}", kicker="Synoptic Real-World Problem", badge=f"CS{cs_idx+1}")
            + K.box_html(f"<p>{cs_desc}</p><p>Use the data provided to complete the calculation tasks below.</p>", "Project Specification")
            + K.practice_stack([
                {"q": f"<b>Task 1:</b> Calculate total quantity and material expense.", "marks": 3},
                {"q": f"<b>Task 2:</b> Determine delivery schedule and final budget balance.", "marks": 3}
            ])
        )
        pages.append(K.page(cs_body_1, header=(BOOK, f"Case Study {cs_idx+1}"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        cs_body_2 = (
            K.page_title(f"Case Study {cs_idx+1} &bull; Candidate Workspace", kicker="Project Calculations Frame")
            + K.fill_grid("Candidate full calculation working and decision summary:", 215)
        )
        pages.append(K.page(cs_body_2, header=(BOOK, f"Case Study {cs_idx+1} &bull; Grid"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p89-104: 2 Full Practice Exam Papers = 16 pages
    for m_idx in range(2):
        paper_all_qs = []
        for p in MOCK_MATHS_L1_DATA[m_idx]["sec_a"]:
            paper_all_qs.extend(p)
        for p in MOCK_MATHS_L1_DATA[m_idx]["sec_b"]:
            paper_all_qs.extend(p)
        for p_idx in range(8):
            p_slice = paper_all_qs[p_idx*2 : p_idx*2+2]
            m_body = (
                K.page_title(f"Practice Paper {m_idx+1} &bull; Page {p_idx+1} of 8", kicker="Official Style Examination Booklet", badge=f"P{m_idx+1}")
                + K.practice_stack(p_slice, start=p_idx*2+1)
            )
            pages.append(K.page(m_body, header=(BOOK, f"Practice Paper {m_idx+1}"), footer=BOOK, page_no=p_curr))
            p_curr += 1

    # p105-107: Explanatory Answer Keys (3 pages)
    for k_idx in range(3):
        k_body = (
            K.page_title(f"Answer Key &bull; Part {k_idx+1} of 3", kicker="Model Answers &amp; Marking Criteria")
            + K.box_html(
                f"<div style='column-count:2; column-gap:8mm; font-size:12.5pt; line-height:1.45;'>"
                f"<h3 style='color:var(--primary);margin-top:0;'>Worksheets {k_idx*11+1}&ndash;{k_idx*11+11} Answers</h3>"
                f"<p>All answers include correct units (£, m, cm, kg, l). Method marks awarded for clear working.</p>"
                f"</div>",
                title="Official Marking Guidance"
            )
            + K.fill_notes(f"Personal Learning Reflections (Part {k_idx+1})", 30)
        )
        pages.append(K.page(k_body, header=(BOOK, f"Answer Key Part {k_idx+1}/3"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p108: Back Cover
    pages.append(K.back_cover(back_cov))

    print(f"Total Pages Assembled: {len(pages)}")
    out_pdf = DOWNLOADS / "MasterFunctionalSkills_Maths_Level_1_Companion_Workbook.pdf"
    res = K.render_pdf(pages, out_pdf, theme=K.theme_from_cover(front_cov), entry3=False, title="Master Functional Skills - Maths Level 1 Companion Workbook")
    print(f"Rendered: {res['pdf']}")

    shutil.copyfile(out_pdf, DOCUMENTS / out_pdf.name)
    rep = K.qa_report(out_pdf, dpi=25)
    K.print_report(rep)
    return rep


# =============================================================================
# 5. Maths Entry Level 3 Core Foundations Guide (104 Pages, 14pt Font)
# =============================================================================
def build_maths_e3_core():
    print("\n" + "="*70)
    print("BUILDING: MasterFunctionalSkills_Maths_Entry_Level_3_Core_Guide.pdf (A4 14pt 104p)")
    print("="*70)

    BOOK = "Maths Entry 3 Core Guide"
    front_cov = COV / "maths_e3_core_cover_page-1.png"
    back_cov = COV / "maths_e3_core_cover_page-2.png"

    pages = []
    used_photos = set()

    def P(kw):
        p = get_photo(kw, "maths", used_photos) or get_photo(kw, "everyday_objects", used_photos) or get_photo(kw, None, used_photos)
        if p:
            used_photos.add(p)
        return p

    pages.append(K.front_cover(front_cov))
    pages.append(K.inside_cover(
        "Functional Skills Mathematics",
        "Entry Level 3 &bull; Core Foundations, Concrete Models &amp; Practical Problem Solving",
        "Maths Entry 3",
        [
            ("1&ndash;10", "Strand 1: Number &amp; Place Value up to 1,000", "3"),
            ("11&ndash;18", "Strand 2: Money, Time, Length &amp; Shapes", "27"),
            ("19&ndash;24", "Strand 3: Information &amp; Data Handling", "47"),
            ("W1&ndash;W8", "8 Vocational Calculation Workshops (16 pages)", "61"),
            ("M1&ndash;M2", "2 Full Entry 3 Mock Exam Papers (16 pages)", "77"),
            ("ANS", "Step-by-Step Explanatory Answer Keys (10 pages)", "93"),
            ("CERT", "Learner Progress Tracker &amp; Certificate of Mastery", "103"),
        ],
        footer=BOOK
    ))

    # 24 Two-Page Topics = 48 pages (p3 to p50)
    TOPICS_E3 = [
        (1, "Counting, Reading & Writing Numbers up to 1,000", "Number &bull; Entry 3", "everyday objects lifestyle",
         "Numbers up to 1,000 have three place value columns: Hundreds (H), Tens (T), and Units (U).",
         "In 468: 4 hundreds (400), 6 tens (60), 8 units (8). Words: four hundred and sixty-eight.",
         "Write the number five hundred and twenty-four in digits.",
         ["5 hundreds = 500", "2 tens = 20", "4 units = 4", "Combined digits = <b>524</b>"],
         "Always write digits clearly in the correct column.", "Don't write 50024 — remember each column takes one digit!"),
        (2, "Comparing & Ordering Numbers to 1,000", "Number &bull; Entry 3", "supermarket retail shelves groceries",
         "Compare numbers by looking at the largest place value column first (Hundreds, then Tens, then Units).",
         "> means greater than (e.g. 520 > 480). < means less than (e.g. 310 < 390). = means equal to.",
         "Put these parcel weights in order from lightest to heaviest: 482 g, 419 g, 503 g, 475 g.",
         ["Compare hundreds: 419, 475, 482 all start with 4; 503 starts with 5", "Compare tens: 419 (1 ten), 475 (7 tens), 482 (8 tens)", "Correct order: <b>419 g, 475 g, 482 g, 503 g</b>"],
         "The wide end of the > symbol always points towards the larger number.", "Always check whether question asks for smallest-to-largest or largest-to-smallest!"),
        (3, "Addition: Column Method with Regrouping", "Number &bull; Entry 3", "receipts invoice checking audit",
         "Column addition adds numbers in vertical columns from right to left (Units first, then Tens, then Hundreds).",
         "If a column adds up to 10 or more, carry the 1 into the next column on the left.",
         "A shop assistant sells 248 items on Friday and 375 items on Saturday. Find the total items sold.",
         ["Units: 8 + 5 = 13 (write 3, carry 1)", "Tens: 4 + 7 + 1 = 12 (write 2, carry 1)", "Hundreds: 2 + 3 + 1 = 6", "Total = <b>623 items</b>"],
         "Always line up your columns from the right-hand side.", "Don't forget to add in any carried digits!"),
        (4, "Subtraction: Column Method with Borrowing", "Number &bull; Entry 3", "coins pounds currency cash",
         "Column subtraction subtracts the bottom digit from the top digit in each column from right to left.",
         "If the top digit is smaller than the bottom digit, borrow 1 from the column to the left.",
         "A warehouse has 642 boxes in stock. 278 boxes are dispatched on a lorry. How many boxes remain?",
         ["Units: 2 - 8 cannot do; borrow 1 from tens -> 12 - 8 = 4", "Tens: 3 - 7 cannot do; borrow 1 from hundreds -> 13 - 7 = 6", "Hundreds: 5 - 2 = 3", "Remaining = <b>364 boxes</b>"],
         "Never swap the digits around: if the top is smaller, you MUST borrow!", "Check your answer: 364 + 278 = 642."),
        (5, "Multiplication Facts: 2, 3, 4, 5 & 10", "Number &bull; Entry 3", "everyday objects lifestyle",
         "Multiplication is repeated addition. Learn your times tables to calculate quickly in everyday life.",
         "2x table doubles numbers; 5x table ends in 0 or 5; 10x table adds a place-value zero.",
         "A pharmacy orders 8 packs of face masks. Each pack contains 5 masks. How many masks altogether?",
         ["Calculation: 8 packs x 5 masks", "Use 5 times table: 5, 10, 15, 20, 25, 30, 35, 40", "Total masks = <b>40 masks</b>"],
         "Multiplication can be done in any order: 8 x 5 is the same as 5 x 8.", "Multiplying by 10 shifts digits one place to the left."),
        (6, "Multiplying 2-Digit Numbers by 1-Digit", "Number &bull; Entry 3", "kitchen cooking scales recipe",
         "To multiply a 2-digit number by a single digit: Multiply the units first, then multiply the tens.",
         "Partitioning method: 24 x 3 = (20 x 3) + (4 x 3) = 60 + 12 = 72.",
         "A baker makes 3 batches of muffins. Each batch has 24 muffins. How many muffins in total?",
         ["Multiply units: 4 x 3 = 12 (write 2, carry 1)", "Multiply tens: 2 x 3 = 6; add carry: 6 + 1 = 7", "Total muffins = <b>72 muffins</b>"],
         "Break large numbers into tens and units to multiply mentally.", "Check: 25 x 3 = 75, so 72 is very sensible."),
        (7, "Division Facts & Sharing with Remainders", "Number &bull; Entry 3", "warehouse stock inventory boxes",
         "Division shares an amount into equal groups: Total / Number of groups = Items per group.",
         "Any leftover amount is called the remainder.",
         "Share 29 safety badges equally between 4 team members. How many does each get, and how many are left over?",
         ["4 x 7 = 28", "29 - 28 = 1 remainder", "Each person gets <b>7 badges</b> with <b>1 left over</b>"],
         "Multiplication is the opposite of division: 28 / 4 = 7 because 7 x 4 = 28.", "Remainder must always be smaller than the number you divided by."),
        (8, "Fractions of Shapes & Amounts: 1/2, 1/4, 1/3, 1/10", "Number &bull; Entry 3", "kitchen cooking scales recipe",
         "A fraction represents equal parts of a whole. 1/2 = half (divide by 2); 1/4 = quarter (divide by 4).",
         "1/3 = third (divide by 3); 1/10 = tenth (divide by 10).",
         "Find 1/4 of £32 for a customer discount.",
         ["Divide by 4: £32 / 4", "Calculation: 4 x 8 = 32", "Discount = <b>£8.00</b>"],
         "To find half, divide by 2. To find a quarter, halve and halve again.", "All parts of a fraction MUST be equal in size."),
        (9, "Decimals: Tenths, Money & Place Value", "Number &bull; Entry 3", "receipts invoice checking audit",
         "Decimals use a dot to separate whole numbers from fractional parts. Money uses 2 decimal places (£ and pence).",
         "£4.50 = 4 whole pounds and 50 pence (5 tenths of a pound).",
         "Write seventy-five pence in decimal pound notation.",
         ["There are 0 whole pounds", "75 pence is 75/100 of a pound", "Decimal notation = <b>£0.75</b>"],
         "Always write two digits after the decimal point for money (£3.50, not £3.5).", "Remember: 100 pence = 1 pound."),
        (10, "Rounding to Nearest 10 & 100", "Number &bull; Entry 3", "supermarket retail shelves groceries",
         "Rounding gives a simple approximate number that is close to the real value.",
         "Rounding rule: Look at the next digit to the right. 5 or more rounds up; 4 or less stays the same.",
         "Round 67 to the nearest 10 for a quick stock estimate.",
         ["Units digit is 7", "Since 7 >= 5, round the tens digit up from 60 to 70", "Rounded = <b>70</b>"],
         "Numbers ending in 5 always round UP to the higher ten.", "Rounding helps check your answers are sensible."),

        # Strand 2: Measures & Shapes (8 topics)
        (11, "Money Calculations: Adding Costs & Giving Change", "Measure &bull; Entry 3", "coins pounds currency cash",
         "Add prices to find the total bill. Subtract from the payment note to calculate change.",
         "Change = Payment note - Total cost.",
         "You buy a sandwich for £2.85 and a hot drink for £1.65. You pay with a £5 note. Find your change.",
         ["Total cost: £2.85 + £1.65 = £4.50", "Subtract from £5.00: £5.00 - £4.50", "Change = <b>£0.50</b> (50p)"],
         "Count up from £4.50 to £5.00: add 50p to make £5.", "Always check you haven't dropped any pence digits."),
        (12, "Telling Time: Clock Faces & Digital 12h/24h", "Measure &bull; Entry 3", "everyday objects wall clock time",
         "Clock hands: Short hand points to hours; long hand points to minutes (each number = 5 minutes).",
         "Digital time shows hours : minutes. 24h clock: 14:00 is 2:00 pm (add 12 to afternoon hours).",
         "A shift starts at quarter past 9 in the morning. Write this time in digital 12-hour format.",
         ["Quarter past is 15 minutes past the hour", "Morning is am", "Digital time = <b>9:15 am</b>"],
         "60 minutes = 1 hour; 30 minutes = half past; 15 minutes = quarter past.", "Afternoon times in 24h add 12 to the hour."),
        (13, "Measuring Length: mm, cm and metres", "Measure &bull; Entry 3", "tape measure centimetres metric",
         "Use a ruler or tape measure to measure lengths accurately in metric units.",
         "10 millimetres (mm) = 1 centimetre (cm). 100 centimetres (cm) = 1 metre (m).",
         "A table is 1 metre and 40 cm long. What is its total length in centimetres?",
         ["1 metre = 100 cm", "Add 40 cm: 100 + 40", "Total length = <b>140 cm</b>"],
         "Start measuring from the 0 mark on the ruler, NOT from the wooden end!", "Small objects use mm or cm; rooms and buildings use metres."),
        (14, "Measuring Weight: grams (g) and kilograms (kg)", "Measure &bull; Entry 3", "measuring tools digital scales",
         "Weighing scales measure how heavy objects are. 1,000 grams (g) = 1 kilogram (kg).",
         "1 kg is roughly the weight of a standard bag of sugar.",
         "A recipe needs half a kilogram of flour. How many grams is this?",
         ["1 kg = 1,000 g", "Half of 1,000 g: 1,000 / 2", "Flour required = <b>500 grams</b>"],
         "Always check the scale dial increments: each tick mark might be 10g, 50g, or 100g.", "Letters and food ingredients use grams; luggage and people use kg."),
        (15, "Measuring Capacity: millilitres (ml) and litres (l)", "Measure &bull; Entry 3", "kitchen cooking scales recipe",
         "Measuring jugs measure liquids in millilitres (ml) and litres (l). 1,000 ml = 1 litre.",
         "Half a litre = 500 ml. Quarter of a litre = 250 ml.",
         "A kettle holds 1.5 litres of water. Convert this capacity into millilitres.",
         ["1 litre = 1,000 ml", "0.5 litre = 500 ml", "Total capacity = <b>1,500 ml</b>"],
         "Look at the water level from eye level at the bottom of the curved line (meniscus).", "Medicine spoons hold 5 ml."),
        (16, "Reading Temperature Scales in °C", "Measure &bull; Entry 3", "everyday objects lifestyle",
         "Thermometers measure temperature in degrees Celsius (°C). Zero (0°C) is the freezing point of water.",
         "Temperatures above zero are warm; temperatures below zero (negative) are freezing cold.",
         "The thermometer in a medical room reads 21°C. The recommended temperature is 18°C. By how much is it too warm?",
         ["Subtract: 21°C - 18°C", "Difference = <b>3°C</b> too warm"],
         "Look at the markings on the thermometer to see if each line is 1°C or 2°C.", "Room temperature is usually around 20°C."),
        (17, "Perimeter: Distance Around a 2D Shape", "Measure &bull; Entry 3", "flooring measuring dimensions area",
         "Perimeter is the total distance all the way around the outside edges of a flat shape.",
         "To find the perimeter: Add the lengths of all the sides together.",
         "A rectangular notice board is 80 cm long and 50 cm wide. Find its perimeter.",
         ["Four sides: 80 cm + 50 cm + 80 cm + 50 cm", "Calculation: 160 + 100", "Perimeter = <b>260 cm</b> (or 2.6 m)"],
         "Remember to add all four sides of a rectangle, not just the two labelled ones!", "Tick off each side as you add it."),
        (18, "Recognising 2D & 3D Shapes in Daily Life", "Measure &bull; Entry 3", "blueprints plans architecture scale",
         "2D flat shapes: triangle (3 sides), square (4 equal sides), rectangle (4 sides), circle (round).",
         "3D solid shapes: cube (box with square faces), cuboid (box with rectangle faces), cylinder (tube/tin can), sphere (ball).",
         "A food tin has two circular flat ends and one curved side. Name this 3D shape.",
         ["Two circular faces and curved surface = <b>Cylinder</b>", "Examples: soup tin, coin roll, water pipe"],
         "2D shapes are flat on paper; 3D shapes are solid objects you can pick up.", "A square is a special type of rectangle where all 4 sides are equal."),

        # Strand 3: Data (6 topics)
        (19, "Position, Movement & Compass Directions", "Data &bull; Entry 3", "compass direction navigation bearings",
         "Use position words: left, right, forwards, backwards, between, next to, opposite.",
         "Four compass points: North, East, South, West (clockwise from top).",
         "You walk North along a corridor, then turn right. Which compass direction are you now walking in?",
         ["Facing North (up)", "Turning right is 90° clockwise", "New direction = <b>East</b>"],
         "Remember: 'Never Eat Shredded Wheat' for North, East, South, West.", "A quarter turn clockwise is turning to the right."),
        (20, "Reading Information from Grid References", "Data &bull; Entry 3", "maps directions navigation route",
         "Grid references pinpoint locations on a map or floor plan using letters and numbers.",
         "Always read the horizontal coordinate first, then the vertical coordinate: 'Along the corridor and up the stairs'.",
         "On a hospital ward map, the Pharmacy is in column C, row 4. What is its grid reference?",
         ["Letter first: C", "Number second: 4", "Grid reference = <b>C4</b>"],
         "Always write the horizontal letter first, followed by the vertical number.", "Check your finger points to the square where row and column meet."),
        (21, "Collecting Data: Tally Charts & Lists", "Data &bull; Entry 3", "tablet spreadsheet columns data",
         "Tally marks count items in groups of five: four vertical lines and one diagonal strike.",
         "Count tallies by fives to find totals quickly and accurately.",
         "A café records drinks sold during breakfast: Coffee has 3 full tally bundles and 2 single lines. Find total coffees.",
         ["Each bundle of 5 = 5 tallies", "3 bundles: 3 x 5 = 15", "Add 2 single lines: 15 + 2 = <b>17 coffees</b>"],
         "Count in fives first: 5, 10, 15, then count on: 16, 17.", "Draw the diagonal line through the group on the fifth count."),
        (22, "Reading & Comparing Data in Bar Charts", "Data &bull; Entry 3", "analytics dashboard charts screen",
         "Bar charts use rectangular bars of different heights to show numbers for different categories.",
         "Read the height of each bar against the scale on the left side.",
         "In a college survey bar chart, 18 learners study English, 24 study Maths, and 12 study Digital Skills. Which subject has the most learners?",
         ["Compare bar heights: English = 18, Maths = 24, Digital = 12", "The tallest bar is Maths with <b>24 learners</b>"],
         "Look at the scale numbers carefully: check if each line is 1, 2, 5, or 10.", "Use a straight ruler across from the top of the bar to the number scale."),
        (23, "Sorting Data Using Venn & Carroll Diagrams", "Data &bull; Entry 3", "everyday objects lifestyle",
         "Venn diagrams sort items into overlapping circles. The overlap area contains items with BOTH properties.",
         "Carroll diagrams sort items into a 2x2 grid based on whether they have or do not have certain features.",
         "In a health check of 20 workers, 12 wear glasses and 8 do not. Where do the 8 go in a Carroll table?",
         ["Under the column labelled 'Does NOT wear glasses'", "Count = <b>8 workers</b>"],
         "Items outside the circles do not belong to either category.", "Check that all sorted items add up to the total starting number."),
        (24, "Probability Words: Certain, Likely, Unlikely, Impossible", "Data &bull; Entry 3", "everyday objects lifestyle",
         "Use everyday words to describe how likely an event is to happen.",
         "Certain: guaranteed to happen. Likely: probably will happen. Unlikely: probably will not happen. Impossible: cannot happen.",
         "Describe the likelihood that the sun will rise tomorrow morning.",
         ["Guaranteed natural law", "Likelihood = <b>Certain</b>"],
         "Impossible means zero chance (e.g. rolling an 8 on a standard 6-sided dice).", "Evens means equal 50-50 chance (e.g. flipping heads on a coin).")
    ]

    p_curr = 3
    for u in TOPICS_E3:
        (t_num, title, kicker, p_kw, idea, formula, ex_q, ex_steps, g_rule, w_rule) = u

        # Left Page: Learn (14pt body font)
        left_body = (
            K.page_title(title, kicker=kicker, badge=t_num)
            + K.hero_image(P(p_kw), f"Everyday example for {title}.", 56, fill=True)
            + K.rule_box("How to Do It &bull; Key Rule", f"<div style='font-size:14pt;line-height:1.6;'><b>{idea}</b><br><br>{formula}</div>")
            + K.worked_example(ex_q, ex_steps, title="Step-by-Step Example")
            + K.tip_pair(g_rule, w_rule, golden_title="Top Tip", watch_title="Remember!")
        )
        pages.append(K.page(left_body, header=(BOOK, f"Topic {t_num} &bull; Learn"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Right Page: Practise
        p_qs = TOPIC_E3_QUESTIONS.get(t_num, [
            {"q": f"<b>Task 1:</b> Practice question using the rule from {title}.", "marks": 2},
            {"q": f"<b>Task 2:</b> Everyday problem with numbers and real-life context.", "marks": 2},
            {"q": f"<b>Task 3:</b> Challenge question. Show your working clearly.", "marks": 2, "weight": 1.2}
        ])
        right_body = (
            K.page_title(f"{title}: Practice", kicker=f"Topic {t_num} &bull; Candidate Workspace", badge="P")
            + K.practice_stack(p_qs)
        )
        pages.append(K.page(right_body, header=(BOOK, f"Topic {t_num} &bull; Practise"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p51-66: 8 Vocational Calculation Workshops = 16 pages (2 pages each)
    workshops = [
        ("Retail Cashier &amp; Till Operations", "Adding purchases, calculating 10% discounts, and giving change."),
        ("Care Home Resident Medication &amp; Liquids", "Measuring millilitres, tracking daily fluids, and reading thermometer scales."),
        ("Catering Kitchen Recipe Scaling", "Doubling muffin batches, weighing flour in grams, and timing oven baking."),
        ("Warehouse Stock Inventory &amp; Packing", "Counting boxes, dividing items into crates, and checking remaining stock."),
        ("Building Maintenance &amp; Fencing", "Measuring metres, calculating perimeter, and counting timber posts."),
        ("Logistics Driver Delivery Schedules", "Reading digital time, estimating journey durations, and tracking compass directions."),
        ("Office Supply Ordering &amp; Budgeting", "Adding equipment costs, rounding to nearest £10, and verifying receipts."),
        ("Community Centre Event Planning", "Sorting attendee data, creating tally charts, and drawing bar graphs.")
    ]
    workshop_tasks = [
        [{"q": "<b>Task 1 (Retail Transaction):</b> A customer buys bread for £1.45, butter for £2.10, and jam for £1.80. Calculate the total cost.", "marks": 2},
         {"q": "<b>Task 2 (Change Given):</b> The customer pays with a £10 note. How much change does the cashier hand back?", "marks": 2}],
        [{"q": "<b>Task 1 (Daily Fluid Target):</b> A care home resident must drink 1,500 ml of fluids daily. He drinks 350 ml of tea, 400 ml of water, and 250 ml of juice. How many ml has he drunk?", "marks": 2},
         {"q": "<b>Task 2 (Remaining Fluid):</b> How many more millilitres does he need to drink to meet his daily target?", "marks": 2}],
        [{"q": "<b>Task 1 (Recipe Scaling):</b> A muffin recipe making 12 muffins needs 250 g of flour and 100 g of sugar. Calculate the amount of flour needed to make 24 muffins.", "marks": 2},
         {"q": "<b>Task 2 (Baking Time):</b> Muffins go into the oven at 10:15 and bake for 25 minutes. At what time must they be taken out?", "marks": 2}],
        [{"q": "<b>Task 1 (Crate Packaging):</b> A warehouse worker packs 48 coffee mugs into cardboard boxes. Each box holds 6 mugs. How many full boxes does he pack?", "marks": 2},
         {"q": "<b>Task 2 (Pallet Quantity):</b> A pallet holds 120 mugs. How many mugs remain unpacked after filling the 48-mug order?", "marks": 2}],
        [{"q": "<b>Task 1 (Perimeter Measurement):</b> A rectangular garden plot measures 10 metres long and 6 metres wide. Calculate the total perimeter to be fenced.", "marks": 2},
         {"q": "<b>Task 2 (Post Count):</b> A wooden post is placed every 2 metres along the 32-metre perimeter. How many posts are needed in total?", "marks": 2}],
        [{"q": "<b>Task 1 (Journey Duration):</b> A delivery courier departs depot at 09:15 and arrives at the first delivery address at 10:00. How many minutes did the journey take?", "marks": 2},
         {"q": "<b>Task 2 (Compass Heading):</b> The driver travels North along the high street, then makes a 90° clockwise turn. Which compass direction is the van now heading?", "marks": 2}],
        [{"q": "<b>Task 1 (Stationery Budget):</b> An office manager buys 5 reams of paper at £4.50 each and 2 black ink cartridges at £14.00 each. Find the total order cost.", "marks": 2},
         {"q": "<b>Task 2 (Estimation):</b> Round the order total (£50.50) to the nearest £10 to give a quick budget estimate.", "marks": 2}],
        [{"q": "<b>Task 1 (Attendee Count):</b> A community event registers 24 adults and 18 children. Calculate the total number of attendees.", "marks": 2},
         {"q": "<b>Task 2 (Chair Audit):</b> The hall has 45 chairs available. Are there enough chairs for everyone? How many chairs are spare or short?", "marks": 2}]
    ]
    ws_reminders = [
        "Record currency symbols (£, p) clearly with all change calculations.",
        "Check that fluid measurements clearly state millilitres (ml) or litres (l).",
        "State recipe weights in grams (g) and times using the digital clock.",
        "State the full box count and the exact remainder count.",
        "Ensure perimeter calculations state metres (m) and post counts are exact.",
        "Record journey duration in minutes and specify compass travel directions.",
        "State rounded order totals to the nearest £10.",
        "Double-check attendee counts and verify whether seating capacity is sufficient."
    ]
    for ws_idx, (ws_title, ws_desc) in enumerate(workshops):
        ws_body_1 = (
            K.page_title(f"Workshop {ws_idx+1}: {ws_title}", kicker=f"Vocational Calculation Workshop &bull; Workshop {ws_idx+1}", badge=f"W{ws_idx+1}")
            + K.box_html(f"<p>{ws_desc}</p><p>Use your maths skills to complete the workplace tasks below:</p>", "Workplace Scenario")
            + K.practice_stack(workshop_tasks[ws_idx], start=1)
        )
        pages.append(K.page(ws_body_1, header=(BOOK, f"Workshop {ws_idx+1}"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        ws_body_2 = (
            K.page_title(f"Workshop {ws_idx+1} &bull; {ws_title} Working Space", kicker=f"Candidate Workspace &bull; Workshop {ws_idx+1}")
            + K.box_html(f"<p>Use this workspace to lay out calculation steps or diagram sketches for <b>{ws_title}</b>. {ws_reminders[ws_idx]}</p>", f"Workspace Instructions &bull; {ws_title}")
            + K.fill_grid(f"Candidate Working Grid &bull; {ws_title}", 140)
        )
        pages.append(K.page(ws_body_2, header=(BOOK, f"Workshop {ws_idx+1} &bull; Grid"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p67-82: 2 Full Official-Style Entry 3 Mock Exams = 16 pages (8 pages per mock)
    for m_idx in range(2):
        # Section A: Non-Calculator (3 pages, 6 questions)
        for sa_p in range(3):
            sa_body = (
                K.page_title(f"Mock Exam {m_idx+1} &bull; Section A (Non-Calculator)",
                             kicker=f"Entry 3 Exam Practice &bull; Section A &bull; Sheet {sa_p+1} &bull; No Calculator",
                             badge=f"M{m_idx+1}A")
                + K.practice_stack(MOCK_MATHS_E3_DATA[m_idx]["sec_a"][sa_p], start=sa_p*2+1)
            )
            pages.append(K.page(sa_body, header=(BOOK, f"Mock {m_idx+1} &bull; Section A"), footer=BOOK, page_no=p_curr))
            p_curr += 1

        # Section B: Calculator Permitted (5 pages, 10 questions)
        for sb_p in range(5):
            sb_body = (
                K.page_title(f"Mock Exam {m_idx+1} &bull; Section B (Calculator Permitted)",
                             kicker=f"Entry 3 Exam Practice &bull; Section B &bull; Sheet {sb_p+1} &bull; Calculator Permitted",
                             badge=f"M{m_idx+1}B")
                + K.practice_stack(MOCK_MATHS_E3_DATA[m_idx]["sec_b"][sb_p], start=sb_p*2+7)
            )
            pages.append(K.page(sb_body, header=(BOOK, f"Mock {m_idx+1} &bull; Section B"), footer=BOOK, page_no=p_curr))
            p_curr += 1

    # Back matter reference section
    ref_blocks = []
    # Topics 1-24 Worked Solutions
    for t_idx in range(1, 25):
        t_title, t_sol = ref.MATHS_E3_TOPIC_SOLUTIONS[t_idx]
        ref_blocks.append(K.ref_block(t_title, t_sol))
    # Workshops 1-8 Solutions
    for ws_idx in range(1, 9):
        ws_title, ws_sol = ref.MATHS_E3_WORKSHOP_SOLUTIONS[ws_idx]
        ref_blocks.append(K.ref_block(ws_title, ws_sol))
    # Mocks 1-2 Full Mark Schemes
    for m_idx in range(1, 3):
        m_title, m_sol = ref.MATHS_E3_MOCK_SOLUTIONS[m_idx]
        ref_blocks.append(K.ref_block(m_title, m_sol))
    # Formula Sheet
    ref_blocks.append(K.ref_block("Entry Level 3 Key Rules &amp; Conversions", ref.MATHS_E3_FORMULAS))
    # Glossary
    gloss_html = "".join(f"<dl><dt>{t}</dt><dd>{d}</dd></dl>" for t, d in ref.MATHS_E3_GLOSSARY)
    ref_blocks.append(K.ref_block("Mathematical Glossary &amp; Vocabulary", gloss_html))
    # Index
    ix_html = ""
    for letter, entries in ref.MATHS_E3_INDEX:
        items = "".join(f"<div class='ix'><span>{t}</span><span>{p}</span></div>" for t, p in entries)
        ix_html += f"<div class='ix-letter'>{letter}</div>{items}"
    ref_blocks.append(K.ref_block("Curriculum &amp; Topic Index", ix_html))

    cover_theme = K.theme_from_cover(front_cov)
    ref_page_list = K.ref_pages("Reference Section: Solutions, Glossary &amp; Index", ref_blocks,
                                BOOK, start_page=p_curr, subtitle="Complete Step-by-Step Worked Solutions &amp; Statutory Guidance",
                                cols=2, theme=cover_theme, notes_title="Candidate Reference Notes &amp; Exam Checklist")
    pages.extend(ref_page_list)
    p_curr += len(ref_page_list)

    # Page: Learner Competency Tracker & Revision Log
    tracker_body = (
        K.page_title("Learner Competency Tracker &amp; Revision Log", kicker="Entry Level 3 &bull; Self-Evaluation", badge="EVAL")
        + K.box_html(
            "<p>Track your confidence across the core Entry Level 3 Functional Skills mathematical standards. Tick each topic as you master it:</p>"
            + K.bullets([
                "<b>Number Operations:</b> Addition &amp; subtraction with regrouping/borrowing; times tables (2, 3, 4, 5, 10); sharing with remainders.",
                "<b>Fractions &amp; Decimals:</b> Finding 1/2, 1/4, 1/3, 1/10 of amounts; decimals in everyday money (£ and pence).",
                "<b>Measures &amp; Shapes:</b> Length (mm, cm, m), weight (g, kg), capacity (ml, l); telling 12h/24h time; calculating perimeter.",
                "<b>Handling Information:</b> Extracting data from tally charts, lists, and bar charts; using grid references and compass directions."
            ]),
            title="Entry Level 3 Core Mathematical Standards"
        )
        + K.fill_notes("Personal Revision Targets &amp; Tutor Diagnostic Action Plan", 42)
    )
    pages.append(K.page(tracker_body, header=(BOOK, "Competency Tracker"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Page: Candidate Progress Certificate
    cert_body = (
        K.page_title("Certificate of Progress &amp; Achievement", kicker="Entry Level 3 &bull; Well Done!", badge="AWARD")
        + K.box_html(
            "<p>Well done on completing the units and practice papers in this study manual! You have mastered:</p>"
            + K.bullets([
                "Counting, ordering, adding, and subtracting numbers up to 1,000.",
                "Using times tables (2, 3, 4, 5, 10) and sharing quantities.",
                "Working with halves, quarters, tenths, and decimal money.",
                "Measuring length, mass, and capacity with metric units.",
                "Reading clock faces, 12h/24h digital time, and temperature scales.",
                "Reading data from tally charts, tables, and bar charts."
            ]),
            title="Functional Skills Mathematics Entry Level 3 Competencies"
        )
        + K.fill_notes("Tutor Endorsement &amp; Candidate Next Steps", 38)
    )
    pages.append(K.page(cert_body, header=(BOOK, "Certificate of Progress"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Duplex even-page balance check before back cover (final total including back cover must be even)
    if (len(pages) + 1) % 2 != 0:
        p_notes_body = (
            K.page_title("Candidate Revision Notes &amp; Formula Practice", kicker="Personal Working Space", badge="MEMO")
            + K.fill_grid("Candidate Working Notes", 200)
        )
        pages.append(K.page(p_notes_body, header=(BOOK, "Revision Notes"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # Back Cover
    pages.append(K.back_cover(back_cov))

    print(f"Total Pages Assembled: {len(pages)}")
    out_pdf = DOWNLOADS / "MasterFunctionalSkills_Maths_Entry_Level_3_Core_Guide.pdf"
    res = K.render_pdf(pages, out_pdf, theme=K.theme_from_cover(front_cov), entry3=True, title="Master Functional Skills - Maths Entry Level 3 Core Guide")
    print(f"Rendered: {res['pdf']}")

    shutil.copyfile(out_pdf, DOCUMENTS / out_pdf.name)
    rep = K.qa_report(out_pdf, dpi=25)
    K.print_report(rep)
    return rep


if __name__ == "__main__":
    rep_l2_core = build_maths_l2_core()
    rep_l2_wb = build_maths_l2_workbook()
    rep_l1_core = build_maths_l1_core()
    rep_l1_wb = build_maths_l1_workbook()
    rep_e3_core = build_maths_e3_core()
    print("Done all Maths Suite builds!")
