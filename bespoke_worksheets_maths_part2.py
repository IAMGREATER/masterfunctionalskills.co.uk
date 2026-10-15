#!/usr/bin/env python3
"""
Master Functional Skills - Bespoke Maths Worksheets Part 2 (35 Topics).
Covers Geometry (Domain 4), Statistics & Probability (Domain 5), Maths Extras,
plus fdp-conversions and nets.
Every single question (Q1-Q6) contains genuine numbers, workplace scenarios,
full [M1]/[P1]/[A1] step-by-step mark schemes, exact final answers, pitfalls, and checks.
"""

import re
from build_topic_dataset import make_maths_topic
from generate_all_worksheets_complete import get_svg_for_topic
import maths_domain1_number
import maths_domain2_finance_ratio
import maths_domain3_measures
import maths_domain4_geometry
import maths_domain5_stats_prob
import maths_extras

# Build lookup of upgraded revision topics
_MATHS_REV_MAP = {}
for _mod_list in [
    maths_domain1_number.TOPICS_DOMAIN1,
    maths_domain2_finance_ratio.TOPICS_DOMAIN2,
    maths_domain3_measures.TOPICS_DOMAIN3,
    maths_domain4_geometry.TOPICS_DOMAIN4,
    maths_domain5_stats_prob.TOPICS_DOMAIN5,
    maths_extras.EXTRAS_MATHS,
]:
    for _item in _mod_list:
        _slug = _item["filename"].replace("functional-skills-", "").replace(".html", "")
        _MATHS_REV_MAP[_slug] = _item


def _parse_solution_steps(steps_html, marks_int):
    """Convert HTML solution_steps string into structured (step_text, mark_code) tuples."""
    parts = [re.sub(r"<[^>]+>", "", p).strip() for p in re.split(r"<br\s*/?>", steps_html) if p.strip()]
    if not parts:
        parts = ["1. Apply standard mathematical method", "2. State accurate final value"]
    rows = []
    for idx, p in enumerate(parts):
        clean_p = re.sub(r"^\d+\.\s*", "", p)
        if idx == len(parts) - 1:
            code = "[A1]"
        elif idx == 0:
            code = "[M1]"
        else:
            code = "[P1]" if marks_int >= 3 else "[M1]"
        rows.append((f"{idx + 1}. {clean_p}", code))
    return rows


def _parse_model_steps(model_steps):
    """Convert worked_model['steps'] tuples into worksheet step_rows."""
    rows = []
    for idx, st in enumerate(model_steps, 1):
        # st is (step_num_label, step_title, step_body_html, mark_badge)
        title = re.sub(r"<[^>]+>", "", st[1]).strip()
        body = re.sub(r"<br\s*/?>", " | ", st[2])
        body = re.sub(r"<[^>]+>", "", body).strip()
        badge = st[3].split(":")[0].strip() if ":" in st[3] else st[3].strip()
        if not badge.startswith("["):
            badge = f"[{badge}]"
        rows.append((f"{idx}. {title}: {body}", badge))
    return rows


# Bespoke Foundation Question 1 (2 Marks) for each of the 33 Maths Part 2 slugs
BESPOKE_MATHS_Q1 = {
    "2d-shapes": {
        "title": "Question 1 (Polygon Interior & Exterior Properties)",
        "marks": 2,
        "stem": "A clinical courtyard paving slab is shaped as a <strong>regular hexagon</strong> with each side measuring <strong>45 cm</strong>.<br>Calculate the total perimeter of one hexagonal slab in metres.",
        "lines": 3,
        "ans_label": "Perimeter =",
        "choice_box": "_____________ m",
        "step_rows": [
            ("1. Multiply 6 equal sides by 45 cm: 6 × 45 = 270 cm", "[M1]"),
            ("2. Convert centimetres to metres: 270 ÷ 100 = 2.7 m", "[A1]")
        ],
        "final_answer": "2.7 m",
        "pitfall": "Multiplying by 5 (pentagon) or 8 (octagon) instead of 6 for a hexagon.",
        "reverse_check": "2.7 m = 270 cm; 270 ÷ 6 = 45 cm per side."
    },
    "3d-shape-basics": {
        "title": "Question 1 (Identifying Faces, Edges & Vertices)",
        "marks": 2,
        "stem": "A sterile medical supply box is shaped as a <strong>triangular prism</strong>.<br>Write down the exact number of <strong>faces</strong> and the exact number of <strong>edges</strong> on a triangular prism.",
        "lines": 3,
        "ans_label": "Faces & Edges =",
        "choice_box": "Faces: ________ | Edges: ________",
        "step_rows": [
            ("1. Count faces (2 triangular ends + 3 rectangular sides = 5 faces)", "[M1]"),
            ("2. Count edges (3 on front triangle + 3 on back triangle + 3 connecting = 9 edges)", "[A1]")
        ],
        "final_answer": "5 faces, 9 edges",
        "pitfall": "Confusing a triangular prism (5 faces, 9 edges) with a square-based pyramid (5 faces, 8 edges).",
        "reverse_check": "Euler's formula check: F + V - E = 5 + 6 - 9 = 2."
    },
    "3d-shapes": {
        "title": "Question 1 (3D Solid Properties & Euler's Rule)",
        "marks": 2,
        "stem": "An architectural glass roof lantern is shaped as a <strong>square-based pyramid</strong>.<br>Calculate the sum of its <strong>faces, edges, and vertices</strong>.",
        "lines": 3,
        "ans_label": "Total (F + E + V) =",
        "choice_box": "____________________",
        "step_rows": [
            ("1. Identify F = 5 faces (1 square base + 4 triangles), E = 8 edges, V = 5 vertices", "[M1]"),
            ("2. Sum properties: 5 + 8 + 5 = 18", "[A1]")
        ],
        "final_answer": "18 (5 faces, 8 edges, 5 vertices)",
        "pitfall": "Counting only the 4 triangular faces and forgetting the square base.",
        "reverse_check": "F + V - E = 5 + 5 - 8 = 2."
    },
    "angles-and-bearings": {
        "title": "Question 1 (Three-Figure Compass Bearings)",
        "marks": 2,
        "stem": "An air ambulance helicopter flies due <strong>South-East (SE)</strong> from Base Hospital A to Clinic B.<br>Write down the three-figure bearing of Clinic B from Base Hospital A, and calculate the back-bearing from Clinic B to Base Hospital A.",
        "lines": 3,
        "ans_label": "Outward & Back Bearing =",
        "choice_box": "Outward: ________° | Back: ________°",
        "step_rows": [
            ("1. Outward bearing for South-East (halfway between 090° East and 180° South): 135°", "[M1]"),
            ("2. Back-bearing: 135° + 180° = 315° (North-West)", "[A1]")
        ],
        "final_answer": "Outward: 135°, Back-bearing: 315°",
        "pitfall": "Omitting the leading zero on bearings under 100° or adding 90° instead of 180° for the reverse bearing.",
        "reverse_check": "315° - 180° = 135°."
    },
    "angles": {
        "title": "Question 1 (Angles on a Straight Line & Around a Point)",
        "marks": 2,
        "stem": "A security camera mounted on a flat wall rotates through three adjacent angles along a straight 180° arc.<br>Sector A is <strong>64°</strong> and Sector B is <strong>78°</strong>. Calculate the angle of <strong>Sector C</strong>.",
        "lines": 3,
        "ans_label": "Angle of Sector C =",
        "choice_box": "_____________ °",
        "step_rows": [
            ("1. Sum known angles on the straight line: 64° + 78° = 142°", "[M1]"),
            ("2. Subtract from 180°: 180° - 142° = 38°", "[A1]")
        ],
        "final_answer": "38°",
        "pitfall": "Subtracting from 360° instead of 180° for angles on a straight line.",
        "reverse_check": "64° + 78° + 38° = 180°."
    },
    "angles-in-2d-shapes": {
        "title": "Question 1 (Interior Angles of a Quadrilateral)",
        "marks": 2,
        "stem": "A four-sided hospital reception desk (quadrilateral) has three known interior angles measuring <strong>90°</strong>, <strong>115°</strong>, and <strong>82°</strong>.<br>Calculate the size of the fourth interior angle.",
        "lines": 3,
        "ans_label": "Fourth angle =",
        "choice_box": "_____________ °",
        "step_rows": [
            ("1. Sum the three known angles: 90° + 115° + 82° = 287°", "[M1]"),
            ("2. Subtract from 360° (sum of angles in a quadrilateral): 360° - 287° = 73°", "[A1]")
        ],
        "final_answer": "73°",
        "pitfall": "Using 180° (triangle total) instead of 360° for a 4-sided shape.",
        "reverse_check": "90° + 115° + 82° + 73° = 360°."
    },
    "bar-charts": {
        "title": "Question 1 (Reading & Comparing Dual Bar Chart Frequencies)",
        "marks": 2,
        "stem": "A dual bar chart records urgent blood test requests across three days:<br>• <strong>Monday:</strong> Morning = 45, Afternoon = 30<br>• <strong>Tuesday:</strong> Morning = 52, Afternoon = 38<br>• <strong>Wednesday:</strong> Morning = 48, Afternoon = 42<br><br>Calculate the difference between total Morning requests and total Afternoon requests across the three days.",
        "lines": 3,
        "ans_label": "Difference =",
        "choice_box": "_____________ requests",
        "step_rows": [
            ("1. Total Morning = 45 + 52 + 48 = 145; Total Afternoon = 30 + 38 + 42 = 110", "[M1]"),
            ("2. Difference: 145 - 110 = 35 requests", "[A1]")
        ],
        "final_answer": "35 requests",
        "pitfall": "Comparing only one day instead of summing all three days first.",
        "reverse_check": "(45-30) + (52-38) + (48-42) = 15 + 14 + 6 = 35."
    },
    "comparing-data-sets": {
        "title": "Question 1 (Comparing Consistency Using the Range)",
        "marks": 2,
        "stem": "Two pathology couriers record their daily delivery times (in minutes):<br>• <strong>Courier A:</strong> Mean = 34 mins, Range = 8 mins<br>• <strong>Courier B:</strong> Mean = 31 mins, Range = 22 mins<br><br>State which courier is <strong>faster on average</strong> and which courier is <strong>more consistent</strong>, giving a numerical reason for each.",
        "lines": 3,
        "ans_label": "Faster & More Consistent =",
        "choice_box": "Faster: ____________ | More Consistent: ____________",
        "step_rows": [
            ("1. Faster on average: Courier B because their mean delivery time is lower (31 mins < 34 mins)", "[M1]"),
            ("2. More consistent: Courier A because their range is smaller (8 mins < 22 mins)", "[A1]")
        ],
        "final_answer": "Faster: Courier B (mean 31 mins). More consistent: Courier A (smaller range of 8 mins).",
        "pitfall": "Claiming a higher range means higher consistency (a smaller range always means more consistent).",
        "reverse_check": "Lower mean time = faster speed; smaller range = tighter consistency."
    },
    "conversion-graphs": {
        "title": "Question 1 (Scaling Values Using a Linear Conversion Rate)",
        "marks": 2,
        "stem": "A linear conversion graph between Kilograms (kg) and Pounds (lb) passes through the origin <strong>(0, 0)</strong> and the point <strong>(10 kg, 22 lb)</strong>.<br>Use this conversion relationship to calculate the weight in pounds (lb) of an <strong>85 kg</strong> hospital bed frame.",
        "lines": 3,
        "ans_label": "Weight in pounds =",
        "choice_box": "_____________ lb",
        "step_rows": [
            ("1. Find unit rate from graph coordinate: 22 ÷ 10 = 2.2 lb per kg", "[M1]"),
            ("2. Multiply 85 kg by 2.2: 85 × 2.2 = 187 lb", "[A1]")
        ],
        "final_answer": "187 lb",
        "pitfall": "Dividing 85 by 2.2 instead of multiplying.",
        "reverse_check": "187 ÷ 85 = 2.2 lb/kg (matches 22 ÷ 10)."
    },
    "coordinates": {
        "title": "Question 1 (Four-Quadrant Coordinate Midpoints)",
        "marks": 2,
        "stem": "On a site grid plan, Emergency Generator A is located at coordinates <strong>(-4, 6)</strong> and Transformer B is located at <strong>(8, -2)</strong>.<br>Calculate the coordinates of the exact <strong>midpoint</strong> between Generator A and Transformer B.",
        "lines": 3,
        "ans_label": "Midpoint coordinates =",
        "choice_box": "( ______ , ______ )",
        "step_rows": [
            ("1. Average x-coordinates: (-4 + 8) ÷ 2 = 4 ÷ 2 = 2", "[M1]"),
            ("2. Average y-coordinates: (6 + -2) ÷ 2 = 4 ÷ 2 = 2 → Midpoint (2, 2)", "[A1]")
        ],
        "final_answer": "(2, 2)",
        "pitfall": "Subtracting coordinates instead of adding them before dividing by 2.",
        "reverse_check": "From (-4, 6) to (2, 2) is (+6, -4); from (2, 2) to (8, -2) is also (+6, -4)."
    },
    "data-tables": {
        "title": "Question 1 (Completing a Two-Way Clinical Audit Table)",
        "marks": 2,
        "stem": "A clinic records <strong>150 patient appointments</strong> across Morning and Afternoon sessions:<br>• Total Morning appointments = <strong>85</strong> (of which <strong>72</strong> attended on time).<br>• Total Late arrivals across the whole day = <strong>28</strong>.<br><br>Calculate how many <strong>Afternoon appointments attended on time</strong>.",
        "lines": 3,
        "ans_label": "Afternoon on-time =",
        "choice_box": "_____________ patients",
        "step_rows": [
            ("1. Afternoon total = 150 - 85 = 65; Morning late = 85 - 72 = 13", "[M1]"),
            ("2. Afternoon late = 28 - 13 = 15; Afternoon on-time = 65 - 15 = 50 patients", "[A1]")
        ],
        "final_answer": "50 patients",
        "pitfall": "Subtracting total late (28) directly from Afternoon total (65).",
        "reverse_check": "On-time total = 72 + 50 = 122; 122 + 28 late = 150 total."
    },
    "decimal-basics": {
        "title": "Question 1 (Ordering & Subtracting Decimals Without a Calculator)",
        "marks": 2,
        "stem": "A laboratory digital scale records three chemical sample weights: <strong>4.08 g</strong>, <strong>4.8 g</strong>, and <strong>4.085 g</strong>.<br>Write the weights in order from <strong>smallest to largest</strong>, and calculate the difference between the largest and smallest weight.",
        "lines": 3,
        "ans_label": "Order & Difference =",
        "choice_box": "Order: __________________ | Diff: ________ g",
        "step_rows": [
            ("1. Pad to 3 decimal places (4.080, 4.800, 4.085) → Order: 4.08 g, 4.085 g, 4.8 g", "[M1]"),
            ("2. Difference (largest minus smallest): 4.800 - 4.080 = 0.72 g", "[A1]")
        ],
        "final_answer": "Order: 4.08 g, 4.085 g, 4.8 g | Difference: 0.72 g",
        "pitfall": "Assuming 4.085 is larger than 4.8 because it has more digits.",
        "reverse_check": "4.08 + 0.72 = 4.80 g."
    },
    "estimating-the-mean": {
        "title": "Question 1 (Finding Midpoints & fx in Grouped Data)",
        "marks": 2,
        "stem": "A pharmacy tracks patient waiting times (t minutes) in two intervals:<br>• <strong>0 &lt; t ≤ 10 mins:</strong> 12 patients<br>• <strong>10 &lt; t ≤ 20 mins:</strong> 18 patients<br><br>Using interval midpoints, calculate the <strong>estimated mean waiting time</strong> across these 30 patients.",
        "lines": 3,
        "ans_label": "Estimated mean =",
        "choice_box": "_____________ minutes",
        "step_rows": [
            ("1. Midpoints: 5 and 15. Multiply Σ(f × x) = (12 × 5) + (18 × 15) = 60 + 270 = 330", "[M1]"),
            ("2. Divide Σ(fx) by total frequency (30): 330 ÷ 30 = 11 minutes", "[A1]")
        ],
        "final_answer": "11 minutes",
        "pitfall": "Dividing 330 by 2 (the number of rows) instead of 30 (total patients).",
        "reverse_check": "11 mins lies sensibly between the two midpoints (5 and 15), closer to 15."
    },
    "fraction-basics": {
        "title": "Question 1 (Unit & Non-Unit Fractions of a Ward Budget)",
        "marks": 2,
        "stem": "A rehabilitation unit has a weekly refreshment budget of <strong>£180</strong>.<br>The unit spends <strong>1/4</strong> of the budget on fresh fruit and <strong>1/3</strong> of the budget on tea and coffee.<br>How much money is spent in total on these two items?",
        "lines": 3,
        "ans_label": "Total spent =",
        "choice_box": "£ ____________________",
        "step_rows": [
            ("1. Fruit = 180 ÷ 4 = £45; Tea/Coffee = 180 ÷ 3 = £60", "[M1]"),
            ("2. Combined spend: £45 + £60 = £105", "[A1]")
        ],
        "final_answer": "£105",
        "pitfall": "Dividing £180 by 7 (adding denominators 4 + 3).",
        "reverse_check": "£105 / £180 = 7/12 = 3/12 + 4/12."
    },
    "grouped-data": {
        "title": "Question 1 (Identifying Modal Class & Median Class Interval)",
        "marks": 2,
        "stem": "A grouped frequency table records the ages of <strong>40 volunteer blood donors</strong>:<br>• 18–29 yrs: <strong>9</strong> | 30–39 yrs: <strong>16</strong> | 40–49 yrs: <strong>10</strong> | 50–59 yrs: <strong>5</strong><br><br>Write down the <strong>modal class interval</strong> and state what percentage of donors are aged <strong>under 40</strong>.",
        "lines": 3,
        "ans_label": "Modal class & Percentage =",
        "choice_box": "Modal class: ________ | Under 40: ________%",
        "step_rows": [
            ("1. Modal class (highest frequency of 16): 30–39 yrs", "[M1]"),
            ("2. Donors under 40 = 9 + 16 = 25; Percentage = (25 ÷ 40) × 100 = 62.5%", "[A1]")
        ],
        "final_answer": "Modal class: 30–39 yrs | Under 40: 62.5%",
        "pitfall": "Writing '16' as the modal class instead of the interval '30–39 yrs'.",
        "reverse_check": "62.5% of 40 = 0.625 × 40 = 25 donors (9 + 16)."
    },
    "line-graphs": {
        "title": "Question 1 (Calculating Rate of Change from a Line Graph)",
        "marks": 2,
        "stem": "A vaccine cold-storage line graph shows the internal temperature rising from <strong>2.4°C at 08:00</strong> to <strong>6.0°C at 11:00</strong> during a power cut.<br>Calculate the mean rate of temperature rise in <strong>°C per hour</strong>.",
        "lines": 3,
        "ans_label": "Rate of rise =",
        "choice_box": "_____________ °C/hour",
        "step_rows": [
            ("1. Temperature increase: 6.0 - 2.4 = 3.6°C over 3 hours (08:00 to 11:00)", "[M1]"),
            ("2. Rate per hour: 3.6 ÷ 3 = 1.2°C per hour", "[A1]")
        ],
        "final_answer": "1.2°C per hour",
        "pitfall": "Dividing 6.0°C by 3 hours without subtracting the starting temperature of 2.4°C.",
        "reverse_check": "2.4°C + (3 × 1.2°C) = 2.4 + 3.6 = 6.0°C."
    },
    "lists": {
        "title": "Question 1 (Filtering & Ordering Multi-Criteria Lists)",
        "marks": 2,
        "stem": "Four agency nurses submit their hourly rates and weekend availability:<br>• <strong>Nurse A:</strong> £24.50/hr (Weekdays only)<br>• <strong>Nurse B:</strong> £26.00/hr (Weekends available)<br>• <strong>Nurse C:</strong> £23.75/hr (Weekends available)<br>• <strong>Nurse D:</strong> £25.20/hr (Weekends available)<br><br>Select the <strong>two lowest-cost nurses</strong> who can work a <strong>10-hour Sunday shift</strong>, and calculate their combined wages for that Sunday.",
        "lines": 3,
        "ans_label": "Selected Nurses & Combined Cost =",
        "choice_box": "Nurses: ________ | Total: £ ____________",
        "step_rows": [
            ("1. Exclude Nurse A (weekdays only); select cheapest two weekend nurses: Nurse C (£23.75) and Nurse D (£25.20)", "[M1]"),
            ("2. Combined 10-hour shift cost: (£23.75 + £25.20) × 10 = £48.95 × 10 = £489.50", "[A1]")
        ],
        "final_answer": "Nurse C and Nurse D (£489.50)",
        "pitfall": "Including Nurse A (£24.50) despite being unavailable on weekends.",
        "reverse_check": "£237.50 + £252.00 = £489.50."
    },
    "maps-and-scale-drawings": {
        "title": "Question 1 (Converting Map Distance to Real-World Metres)",
        "marks": 2,
        "stem": "A hospital campus map is drawn to a scale of <strong>1 : 2,500</strong>.<br>The straight-line distance on the map between the Ambulance Bay and the Radiology Entrance measures <strong>6.4 cm</strong>.<br>Calculate the actual real-world distance in <strong>metres</strong>.",
        "lines": 3,
        "ans_label": "Actual distance =",
        "choice_box": "_____________ m",
        "step_rows": [
            ("1. Multiply map distance by scale factor: 6.4 cm × 2,500 = 16,000 cm", "[M1]"),
            ("2. Convert centimetres to metres (÷ 100): 16,000 ÷ 100 = 160 m", "[A1]")
        ],
        "final_answer": "160 m",
        "pitfall": "Dividing by 1,000 instead of 100 when converting centimetres to metres.",
        "reverse_check": "160 m = 16,000 cm; 16,000 ÷ 2,500 = 6.4 cm."
    },
    "mean-median-mode-and-range": {
        "title": "Question 1 (Calculating Median & Range of an Even Data Set)",
        "marks": 2,
        "stem": "Six outpatient physiotherapy sessions lasted the following times (in minutes):<br><strong>28, 42, 35, 24, 39, 48</strong><br>Calculate the <strong>median</strong> session duration and the <strong>range</strong>.",
        "lines": 3,
        "ans_label": "Median & Range =",
        "choice_box": "Median: ________ mins | Range: ________ mins",
        "step_rows": [
            ("1. Order data (24, 28, 35, 39, 42, 48) → Median is average of 35 and 39 = 37 mins", "[M1]"),
            ("2. Range = Highest (48) - Lowest (24) = 24 mins", "[A1]")
        ],
        "final_answer": "Median = 37 mins, Range = 24 mins",
        "pitfall": "Finding the middle of the unordered list (35 and 24) without sorting first.",
        "reverse_check": "37 is halfway between 35 and 39; 24 + 24 = 48."
    },
    "movement-and-direction": {
        "title": "Question 1 (Compass Turns & Grid Navigation)",
        "marks": 2,
        "stem": "A Automated Guided Vehicle (AGV) in a pharmacy warehouse is facing <strong>North-East (045°)</strong>.<br>It makes a <strong>three-quarter turn (270°) clockwise</strong>.<br>Which compass direction and three-figure bearing is the AGV now facing?",
        "lines": 3,
        "ans_label": "Direction & Bearing =",
        "choice_box": "Direction: ________ | Bearing: ________°",
        "step_rows": [
            ("1. Add 270° clockwise to 045°: 45° + 270° = 315°", "[M1]"),
            ("2. Identify compass direction for 315°: North-West (NW)", "[A1]")
        ],
        "final_answer": "North-West (315°)",
        "pitfall": "Turning anticlockwise instead of clockwise.",
        "reverse_check": "270° clockwise is equivalent to 90° anticlockwise: 360° + 45° - 90° = 315°."
    },
    "number-basics": {
        "title": "Question 1 (Place Value & Rounding Large Integers)",
        "marks": 2,
        "stem": "An regional NHS logistics hub dispatched <strong>348,650</strong> sterile dressings in Quarter 1.<br>Write down the value represented by the digit <strong>4</strong>, and round <strong>348,650</strong> to the nearest <strong>ten thousand</strong>.",
        "lines": 3,
        "ans_label": "Value of 4 & Rounded Total =",
        "choice_box": "Value: ____________ | Rounded: ____________",
        "step_rows": [
            ("1. Value of digit 4 in ten-thousands column: 40,000 (forty thousand)", "[M1]"),
            ("2. Round 348,650 to nearest 10,000 (thousands digit is 8 ≥ 5): 350,000", "[A1]")
        ],
        "final_answer": "Value = 40,000 | Rounded = 350,000",
        "pitfall": "Rounding to the nearest thousand (349,000) instead of ten thousand (350,000).",
        "reverse_check": "348,650 is 1,350 away from 350,000 vs 8,650 away from 340,000."
    },
    "number-patterns": {
        "title": "Question 1 (Term-to-Term & nth Term Linear Sequences)",
        "marks": 2,
        "stem": "A clinic installs modular waiting-room seating bays. The number of seats follows the linear sequence:<br><strong>6, 10, 14, 18, ...</strong><br>State the term-to-term rule and calculate how many seats are in a row of <strong>12 bays</strong> (the 12th term).",
        "lines": 3,
        "ans_label": "Rule & 12th Term =",
        "choice_box": "Rule: ____________ | 12th Term: ________ seats",
        "step_rows": [
            ("1. Identify constant difference (+4 seats per bay); nth term formula = 4n + 2", "[M1]"),
            ("2. Evaluate 12th term: (4 × 12) + 2 = 48 + 2 = 50 seats", "[A1]")
        ],
        "final_answer": "Add 4 each time; 12th term = 50 seats",
        "pitfall": "Multiplying the 1st term (6) by 12 = 72 instead of applying the common difference +4.",
        "reverse_check": "6 + (11 × 4) = 6 + 44 = 50 seats."
    },
    "pie-charts": {
        "title": "Question 1 (Calculating Sector Angles & Proportions)",
        "marks": 2,
        "stem": "A pie chart represents <strong>90 staff members</strong> surveyed about hospital transport.<br>If the sector for <strong>Cycle to Work</strong> measures an angle of <strong>108°</strong>, how many staff members cycle to work?",
        "lines": 3,
        "ans_label": "Number of staff =",
        "choice_box": "_____________ staff",
        "step_rows": [
            ("1. Find fraction of full circle: 108° ÷ 360° = 0.3 (or 3/10)", "[M1]"),
            ("2. Multiply by total staff (90): 0.3 × 90 = 27 staff members", "[A1]")
        ],
        "final_answer": "27 staff members",
        "pitfall": "Dividing 360° by 90 (= 4° per person) and multiplying instead of dividing 108° by 4°.",
        "reverse_check": "360° ÷ 90 = 4° per person; 27 × 4° = 108°."
    },
    "plans-and-elevations": {
        "title": "Question 1 (Interpreting 2D Orthographic Views of 3D Solids)",
        "marks": 2,
        "stem": "A modular storage unit has a <strong>rectangular plan view (bird's-eye view)</strong> measuring <strong>3 m by 1.5 m</strong>, and a <strong>rectangular front elevation</strong> measuring <strong>3 m wide by 2 m high</strong>.<br>Name the 3D shape of the storage unit and calculate its volume in m³.",
        "lines": 3,
        "ans_label": "Shape & Volume =",
        "choice_box": "Shape: ____________ | Volume: ________ m³",
        "step_rows": [
            ("1. Identify 3D solid from rectangular orthographic projections: Cuboid", "[M1]"),
            ("2. Volume = 3 m × 1.5 m × 2 m = 9 m³", "[A1]")
        ],
        "final_answer": "Cuboid; 9 m³",
        "pitfall": "Multiplying 3 m twice (3 × 3 × 1.5 × 2) instead of extracting L=3, W=1.5, H=2.",
        "reverse_check": "Base area = 3 × 1.5 = 4.5 m²; 4.5 × 2 m height = 9 m³."
    },
    "probability": {
        "title": "Question 1 (Mutually Exclusive Probabilities Summing to 1)",
        "marks": 2,
        "stem": "When a patient calls an out-of-hours triage line, the probability of being connected immediately is <strong>0.35</strong>, and the probability of waiting under 2 minutes is <strong>0.48</strong>.<br>Calculate the probability that a caller waits <strong>2 minutes or longer</strong>.",
        "lines": 3,
        "ans_label": "Probability =",
        "choice_box": "____________________",
        "step_rows": [
            ("1. Sum the known mutually exclusive probabilities: 0.35 + 0.48 = 0.83", "[M1]"),
            ("2. Subtract from 1.00: 1.00 - 0.83 = 0.17 (or 17%)", "[A1]")
        ],
        "final_answer": "0.17 (or 17/100 or 17%)",
        "pitfall": "Multiplying 0.35 × 0.48 instead of subtracting their sum from 1.",
        "reverse_check": "0.35 + 0.48 + 0.17 = 1.00."
    },
    "probability-tables": {
        "title": "Question 1 (Sample Space & Combined Independent Events)",
        "marks": 2,
        "stem": "An automated quality scanner tests two independent batches of blood vials. The probability that Batch 1 passes is <strong>0.9</strong> and the probability that Batch 2 passes is <strong>0.8</strong>.<br>Calculate the probability that <strong>both batches pass</strong> first time.",
        "lines": 3,
        "ans_label": "P(Both Pass) =",
        "choice_box": "____________________",
        "step_rows": [
            ("1. Apply multiplication rule for independent events: P(A and B) = P(A) × P(B)", "[M1]"),
            ("2. Calculate 0.9 × 0.8 = 0.72 (or 72%)", "[A1]")
        ],
        "final_answer": "0.72 (or 18/25 or 72%)",
        "pitfall": "Adding 0.9 + 0.8 = 1.7 (probabilities can never exceed 1!).",
        "reverse_check": "0.72 + (0.9×0.2) + (0.1×0.8) + (0.1×0.2) = 0.72 + 0.18 + 0.08 + 0.02 = 1.00."
    },
    "scales": {
        "title": "Question 1 (Reading Subdivisions on a Medical Dial Scale)",
        "marks": 2,
        "stem": "An oxygen cylinder pressure gauge has major markings at <strong>100 bar</strong> and <strong>150 bar</strong>, separated into <strong>10 equal subdivisions</strong>.<br>If the needle points exactly <strong>7 subdivisions</strong> past 100 bar, what is the exact pressure reading?",
        "lines": 3,
        "ans_label": "Pressure reading =",
        "choice_box": "_____________ bar",
        "step_rows": [
            ("1. Value of 1 subdivision = (150 - 100) ÷ 10 = 50 ÷ 10 = 5 bar per division", "[M1]"),
            ("2. Reading at 7 divisions past 100: 100 + (7 × 5) = 135 bar", "[A1]")
        ],
        "final_answer": "135 bar",
        "pitfall": "Assuming each minor tick represents 1 bar (giving 107 bar) or 10 bar.",
        "reverse_check": "135 bar + (3 × 5 bar) = 150 bar."
    },
    "scatter-graphs": {
        "title": "Question 1 (Identifying Correlation & Using a Line of Best Fit)",
        "marks": 2,
        "stem": "A scatter graph plots <strong>Outdoor Temperature (°C)</strong> on the horizontal axis against <strong>Daily Hospital Heating Gas Usage (m³)</strong> on the vertical axis.<br>As outdoor temperature increases, gas usage decreases steadily.<br>State the <strong>type of correlation</strong> shown, and use the line of best fit equation <strong>y = 400 - 12x</strong> to estimate gas usage when the outdoor temperature (x) is <strong>15°C</strong>.",
        "lines": 3,
        "ans_label": "Correlation & Estimate =",
        "choice_box": "Correlation: ____________ | Usage: ________ m³",
        "step_rows": [
            ("1. Identify correlation: Negative correlation (as x increases, y decreases)", "[M1]"),
            ("2. Substitute x = 15: y = 400 - (12 × 15) = 400 - 180 = 220 m³", "[A1]")
        ],
        "final_answer": "Negative correlation; 220 m³",
        "pitfall": "Calling a downward-sloping relationship 'weak positive' instead of 'negative correlation'.",
        "reverse_check": "At x = 0°C, usage = 400 m³; dropping 12 m³ per degree over 15°C drops by 180 m³ to 220 m³."
    },
    "symmetry-and-2d-shapes": {
        "title": "Question 1 (Lines of Symmetry & Rotational Order)",
        "marks": 2,
        "stem": "Compare a <strong>rectangle</strong> (non-square) and a <strong>rhombus</strong> (non-square).<br>Write down the number of <strong>lines of symmetry</strong> and the <strong>order of rotational symmetry</strong> for a rectangle.",
        "lines": 3,
        "ans_label": "Symmetry of Rectangle =",
        "choice_box": "Lines of symmetry: ________ | Rotational order: ________",
        "step_rows": [
            ("1. Lines of symmetry of a non-square rectangle: 2 (horizontal and vertical bisectors; diagonals are NOT lines of symmetry)", "[M1]"),
            ("2. Order of rotational symmetry: Order 2 (matches at 180° and 360°)", "[A1]")
        ],
        "final_answer": "2 lines of symmetry; rotational symmetry of order 2",
        "pitfall": "Claiming a rectangle has 4 lines of symmetry by counting the two diagonals.",
        "reverse_check": "Folding a rectangular A4 sheet along its diagonal does not align the corners."
    },
    "tables": {
        "title": "Question 1 (Multi-Condition Lookup in a Tariff Table)",
        "marks": 2,
        "stem": "A courier parcel tariff table charges:<br>• <strong>Up to 2 kg:</strong> Standard £4.50 | Express £7.20<br>• <strong>2.01 kg to 5 kg:</strong> Standard £6.80 | Express £10.50<br>• <strong>Over 5 kg:</strong> Standard £9.40 | Express £14.00<br><br>Calculate the total cost of sending <strong>two 3.5 kg parcels by Express</strong> and <strong>one 1.8 kg parcel by Standard</strong>.",
        "lines": 3,
        "ans_label": "Total postage =",
        "choice_box": "£ ____________________",
        "step_rows": [
            ("1. Lookup rates: 3.5 kg Express = £10.50 each (× 2 = £21.00); 1.8 kg Standard = £4.50", "[M1]"),
            ("2. Total postage: £21.00 + £4.50 = £25.50", "[A1]")
        ],
        "final_answer": "£25.50",
        "pitfall": "Summing the weights first (3.5 + 3.5 + 1.8 = 8.8 kg) instead of pricing each parcel individually.",
        "reverse_check": "£25.50 - £4.50 = £21.00; £21.00 ÷ 2 = £10.50."
    },
    "tally-charts": {
        "title": "Question 1 (Converting Five-Bar Tallies to Frequencies & Percentages)",
        "marks": 2,
        "stem": "A canteen feedback tally chart records votes for three lunch specials:<br>• <strong>Roast Chicken:</strong> 4 five-bar gates + 3 single strokes<br>• <strong>Vegetable Curry:</strong> 3 five-bar gates + 2 single strokes<br>• <strong>Salmon Salad:</strong> 2 five-bar gates<br><br>Calculate the total number of votes cast and the percentage of voters who chose <strong>Salmon Salad</strong>.",
        "lines": 3,
        "ans_label": "Total Votes & Percentage =",
        "choice_box": "Total: ________ | Salmon Salad: ________%",
        "step_rows": [
            ("1. Convert tallies: Chicken = 23, Curry = 17, Salmon = 10 → Total = 23 + 17 + 10 = 50 votes", "[M1]"),
            ("2. Percentage for Salmon Salad: (10 ÷ 50) × 100 = 20%", "[A1]")
        ],
        "final_answer": "Total = 50 votes; Salmon Salad = 20%",
        "pitfall": "Counting a five-bar tally gate as 4 or 6 instead of 5.",
        "reverse_check": "23 (46%) + 17 (34%) + 10 (20%) = 50 (100%)."
    },
    "temperature": {
        "title": "Question 1 (Negative Temperature Differences Across Zero)",
        "marks": 2,
        "stem": "A laboratory deep-freezer is maintained at <strong>-18.5°C</strong>, while a chilled blood fridge is kept at <strong>+4.2°C</strong>.<br>Calculate the temperature difference between the two storage units.",
        "lines": 3,
        "ans_label": "Temperature difference =",
        "choice_box": "_____________ °C",
        "step_rows": [
            ("1. Calculate distance across zero: 4.2 - (-18.5) = 4.2 + 18.5", "[M1]"),
            ("2. Evaluate sum: 22.7°C", "[A1]")
        ],
        "final_answer": "22.7°C",
        "pitfall": "Subtracting 18.5 - 4.2 = 14.3°C by ignoring the negative sign.",
        "reverse_check": "-18.5°C + 22.7°C = +4.2°C."
    },
    "using-length-area-and-volume-in-calculations": {
        "title": "Question 1 (Converting Linear Measurements Before Area Calculation)",
        "marks": 2,
        "stem": "A rectangular clinic corridor measures <strong>15 metres long</strong> by <strong>180 centimetres wide</strong>.<br>Calculate the floor area of the corridor in <strong>square metres (m²)</strong>.",
        "lines": 3,
        "ans_label": "Floor area =",
        "choice_box": "_____________ m²",
        "step_rows": [
            ("1. Convert width from centimetres to metres first: 180 cm ÷ 100 = 1.8 m", "[M1]"),
            ("2. Multiply length by width: 15 m × 1.8 m = 27 m²", "[A1]")
        ],
        "final_answer": "27 m²",
        "pitfall": "Multiplying 15 × 180 = 2,700 without converting 180 cm to 1.8 m first.",
        "reverse_check": "27 m² ÷ 15 m = 1.8 m = 180 cm."
    }
}

WORKSHEETS_MATHS_PART2 = []

# 1. Build the 33 topics from _MATHS_REV_MAP + BESPOKE_MATHS_Q1
for _slug, _q1 in BESPOKE_MATHS_Q1.items():
    _rev = _MATHS_REV_MAP[_slug]
    _title = _rev["clean_topic"]
    _spec_list = [s["code"] for s in _rev.get("spec_This", [])]
    _spec_codes = " • ".join(_spec_list[:4]) if _spec_list else "Pearson Edexcel L1 & L2 Mathematics"
    _rules = _rev.get("golden_rules", [])
    _r0 = f"{_rules[0].get('title', '')}: {_rules[0].get('desc', '')}" if (_rules and isinstance(_rules[0], dict)) else (_rules[0] if _rules else "")
    _formula_hint = re.sub(r"<[^>]+>", "", _r0).strip() if _r0 else f"Always show full step-by-step working and units for {_title}."
    _pqs = _rev["practice_questions"]
    _wms = _rev["worked_models"]
    _traps = _rev.get("examiner_traps", [])
    _svg = get_svg_for_topic(_slug)

    _q2 = {
        "title": f"Question 2 (Level 1 Foundation — {_pqs[0]['marks']})",
        "marks": 2,
        "stem": _pqs[0]["question"],
        "lines": 3,
        "ans_label": "Answer =",
        "choice_box": "____________________",
        "step_rows": _parse_solution_steps(_pqs[0]["solution_steps"], 2),
        "final_answer": _pqs[0]["correct_answer"],
        "pitfall": _traps[0]["desc"] if _traps else "Rushing arithmetic without checking units.",
        "reverse_check": _pqs[0]["tutor_tip"]
    }

    _q3 = {
        "title": f"Question 3 ({_wms[0]['title']})",
        "marks": 3,
        "stem": _wms[0]["question"],
        "svg": _svg,
        "lines": 4,
        "ans_label": "Final Value =",
        "choice_box": "____________________",
        "step_rows": _parse_model_steps(_wms[0]["steps"]),
        "final_answer": _wms[0]["final_answer"],
        "pitfall": _traps[0]["fix"] if _traps else "Ensure all intermediate steps are clearly written.",
        "reverse_check": _wms[0]["tutor_tip"]
    }

    _q4 = {
        "title": f"Question 4 (Workplace Application — {_pqs[1]['marks']})",
        "marks": 3,
        "stem": _pqs[1]["question"],
        "lines": 4,
        "ans_label": "Calculated Result =",
        "choice_box": "____________________",
        "step_rows": _parse_solution_steps(_pqs[1]["solution_steps"], 3),
        "final_answer": _pqs[1]["correct_answer"],
        "pitfall": _traps[1]["desc"] if len(_traps) > 1 else "Check that all units are consistent before multiplying or dividing.",
        "reverse_check": _pqs[1]["tutor_tip"]
    }

    _q5 = {
        "title": f"Question 5 ({_wms[1]['title']})",
        "marks": 4,
        "stem": _wms[1]["question"],
        "lines": 5,
        "ans_label": "Model Solution =",
        "choice_box": "____________________",
        "step_rows": _parse_model_steps(_wms[1]["steps"]),
        "final_answer": _wms[1]["final_answer"],
        "pitfall": _traps[1]["fix"] if len(_traps) > 1 else "Double-check all multi-step values against the question stem.",
        "reverse_check": _wms[1]["tutor_tip"]
    }

    _q6 = {
        "title": f"Question 6 (Level 2 Multi-Step Problem Solving — {_pqs[2]['marks']})",
        "marks": 4,
        "stem": _pqs[2]["question"],
        "lines": 5,
        "ans_label": "Conclusion & Answer =",
        "choice_box": "____________________",
        "step_rows": _parse_solution_steps(_pqs[2]["solution_steps"], 4),
        "final_answer": _pqs[2]["correct_answer"],
        "pitfall": "Stating a conclusion without showing the full numerical comparison values.",
        "reverse_check": _pqs[2]["tutor_tip"]
    }

    WORKSHEETS_MATHS_PART2.append(
        make_maths_topic(
            slug=_slug,
            title=_title,
            spec_codes=_spec_codes,
            formula_hint=_formula_hint,
            q1=_q1,
            q2=_q2,
            q3=_q3,
            q4=_q4,
            q5=_q5,
            q6=_q6
        )
    )

# 2. Add full 6-question bespoke definitions for 'fdp-conversions' and 'nets'
WORKSHEETS_MATHS_PART2.extend([
    make_maths_topic(
        slug="fdp-conversions",
        title="Fractions, Decimals & Percentages (FDP) Conversions",
        spec_codes="L1.10 • L1.14 • L2.10 • L2.11",
        formula_hint="Fraction → Decimal: divide numerator by denominator. Decimal → Percentage: multiply by 100. Always convert all values into the same format (usually decimals) before ordering or comparing.",
        q1={
            "title": "Question 1 (Non-Calculator FDP Benchmark Conversions)",
            "marks": 2,
            "stem": "Complete the following equivalences without a calculator:<br>(a) Write <strong>3/8</strong> as a decimal.<br>(b) Write <strong>35%</strong> as a fraction in its simplest form.",
            "lines": 3,
            "ans_label": "(a) & (b) =",
            "choice_box": "(a) ________ | (b) ________",
            "step_rows": [
                ("1. (a) Divide 3 by 8: 3.000 ÷ 8 = 0.375", "[M1]"),
                ("2. (b) Write 35/100 and divide top and bottom by 5: 7/20", "[A1]")
            ],
            "final_answer": "(a) 0.375, (b) 7/20",
            "pitfall": "Writing 3/8 as 0.38 instead of dividing 3 by 8 (= 0.375).",
            "reverse_check": "0.375 × 8 = 3; 7 ÷ 20 = 0.35 = 35%."
        },
        q2={
            "title": "Question 2 (Ordering Mixed Fractions, Decimals & Percentages)",
            "marks": 2,
            "stem": "Arrange these four clinical audit scores in ascending order (from smallest to largest):<br><strong>68% , 7/10 , 0.66 , 13/20</strong>",
            "lines": 3,
            "ans_label": "Smallest to largest =",
            "choice_box": "________ , ________ , ________ , ________",
            "step_rows": [
                ("1. Convert all four to decimals: 68% = 0.68; 7/10 = 0.70; 0.66 = 0.66; 13/20 = 0.65", "[M1]"),
                ("2. Order smallest to largest using original values: 13/20, 0.66, 68%, 7/10", "[A1]")
            ],
            "final_answer": "13/20 (0.65), 0.66, 68% (0.68), 7/10 (0.70)",
            "pitfall": "Listing the converted decimals without writing the original numbers given in the question.",
            "reverse_check": "0.65 < 0.66 < 0.68 < 0.70."
        },
        q3={
            "title": "Question 3 (Hospital Staff Vaccination Uptake Comparison)",
            "marks": 3,
            "stem": "Three hospital wards report their seasonal flu vaccination uptake:<br>• <strong>Ward A:</strong> 19 out of 25 staff vaccinated<br>• <strong>Ward B:</strong> 74% of staff vaccinated<br>• <strong>Ward C:</strong> 0.78 of staff vaccinated<br><br>Which ward achieved the <strong>highest vaccination uptake</strong>? Show all three values as percentages.",
            "svg": get_svg_for_topic("fdp-conversions"),
            "lines": 4,
            "ans_label": "Highest Ward & Percentages =",
            "choice_box": "Ward: ________ (A=____%, B=74%, C=____%)",
            "step_rows": [
                ("1. Convert Ward A to percentage: (19 ÷ 25) × 100 = 76%", "[M1]"),
                ("2. Convert Ward C to percentage: 0.78 × 100 = 78%", "[M1]"),
                ("3. Compare (Ward A = 76%, Ward B = 74%, Ward C = 78%) → Highest is Ward C", "[A1]")
            ],
            "final_answer": "Ward C (78% vs Ward A 76% and Ward B 74%)",
            "pitfall": "Assuming 19/25 is 19% or 81% without multiplying numerator and denominator by 4.",
            "reverse_check": "78% of 100 > 76% of 100 > 74% of 100."
        },
        q4={
            "title": "Question 4 (Retail Supplier Discount Comparison)",
            "marks": 3,
            "stem": "A dental practice needs to order <strong>£600</strong> worth of nitrile gloves. Three suppliers offer different promotional discounts off the £600 list price:<br>• <strong>Supplier X:</strong> <strong>1/6</strong> off the list price<br>• <strong>Supplier Y:</strong> <strong>18%</strong> discount<br>• <strong>Supplier Z:</strong> <strong>0.15</strong> off the list price plus a <strong>£15</strong> loyalty voucher<br><br>Calculate the cash discount for each supplier and state which supplier gives the <strong>biggest saving</strong>.",
            "lines": 4,
            "ans_label": "Best Supplier & Saving =",
            "choice_box": "Supplier: ________ | Saving: £ ____________",
            "step_rows": [
                ("1. Supplier X saving: £600 ÷ 6 = £100.00", "[M1]"),
                ("2. Supplier Y saving: 0.18 × £600 = £108.00; Supplier Z saving: (0.15 × £600) + £15 = £90 + £15 = £105.00", "[P1]"),
                ("3. Compare savings (£108 > £105 > £100) → Supplier Y gives the biggest saving (£108)", "[A1]")
            ],
            "final_answer": "Supplier Y (£108 saving)",
            "pitfall": "Forgetting to add the £15 loyalty voucher to Supplier Z's 0.15 (£90) discount.",
            "reverse_check": "108 / 600 = 18%; 105 / 600 = 17.5%; 100 / 600 = 16.67%."
        },
        q5={
            "title": "Question 5 (Multi-Stage Budget Allocation & Remaining Fraction)",
            "marks": 4,
            "stem": "A community health project receives a grant of <strong>£12,000</strong>:<br>• <strong>35%</strong> is allocated to mobile screening equipment.<br>• <strong>3/8</strong> is allocated to specialist nursing hours.<br>• <strong>0.15</strong> is allocated to printed patient leaflets.<br>• The remainder is kept as an emergency contingency reserve.<br><br>Calculate the exact cash value of the <strong>contingency reserve</strong> and express it as a <strong>fraction of the total grant in its simplest form</strong>.",
            "lines": 5,
            "ans_label": "Cash Reserve & Fraction =",
            "choice_box": "£ ____________ | Fraction: ____________",
            "step_rows": [
                ("1. Convert all allocations to decimals/percentages: 35% = 0.35; 3/8 = 0.375; leaflets = 0.15", "[P1]"),
                ("2. Total proportion spent: 0.35 + 0.375 + 0.15 = 0.875 (87.5%); Remaining proportion = 1 - 0.875 = 0.125", "[M1]"),
                ("3. Cash value of contingency reserve: 0.125 × £12,000 = £1,500", "[A1]"),
                ("4. Express 0.125 (or 1,500/12,000) as simplest fraction: 1/8", "[A1]")
            ],
            "final_answer": "£1,500 and 1/8",
            "pitfall": "Rounding 3/8 (0.375) to 0.38, which causes an error of £60 in the final cash total.",
            "reverse_check": "£4,200 (35%) + £4,500 (3/8) + £1,800 (0.15) + £1,500 (1/8) = £12,000."
        },
        q6={
            "title": "Question 6 (Compliance Audit Decision & Justification)",
            "marks": 4,
            "stem": "An apprenticeship provider passes its annual quality audit only if at least <strong>17/20</strong> of learners pass their first exam sitting.<br>This year, out of <strong>320 learners</strong>:<br>• <strong>0.65</strong> passed in the Autumn window.<br>• A further <strong>68 learners</strong> passed their first sitting in the Spring window.<br><br>Did the provider meet the <strong>17/20</strong> benchmark? Show full FDP comparisons to justify your decision.",
            "lines": 5,
            "ans_label": "Decision & Achieved % =",
            "choice_box": "Yes / No | Target: ____% vs Achieved: ____%",
            "step_rows": [
                ("1. Convert target 17/20 to percentage: (17 ÷ 20) × 100 = 85% (or 272 learners)", "[P1]"),
                ("2. Calculate Autumn passes: 0.65 × 320 = 208 learners", "[M1]"),
                ("3. Total passes = 208 + 68 = 276 learners; Achieved percentage = (276 ÷ 320) × 100 = 86.25%", "[P1]"),
                ("4. Conclusion: Yes, 86.25% > 85% (or 276 > 272 required passes, exceeding target by 4 learners)", "[A1]")
            ],
            "final_answer": "Yes — achieved 86.25% (276/320), beating the 85% (17/20) benchmark by 1.25% (4 learners).",
            "pitfall": "Adding 68% instead of 68 learners to 65%.",
            "reverse_check": "208 + 68 = 276; 276 ÷ 320 = 0.8625 > 0.85."
        }
    ),
    make_maths_topic(
        slug="nets",
        title="3D Nets, Folding Geometry & Packaging Layout",
        spec_codes="L1.22 • L1.24 • L2.21",
        formula_hint="A closed cuboid net has 6 rectangular faces arranged in 3 matching pairs (Top/Bottom, Front/Back, Left/Right). Total length of the flat net = sum of adjacent folded panels.",
        q1={
            "title": "Question 1 (Identifying Faces on a 2D Net)",
            "marks": 2,
            "stem": "A flat cardboard net consists of <strong>1 square central base</strong> surrounded by <strong>4 identical isosceles triangles</strong> attached to its four sides.<br>Name the 3D solid formed when this net is folded, and write down the number of <strong>vertices</strong> on the finished 3D solid.",
            "lines": 3,
            "ans_label": "3D Solid & Vertices =",
            "choice_box": "Solid: ________________ | Vertices: ________",
            "step_rows": [
                ("1. Identify 3D solid from 1 square + 4 triangular faces: Square-based pyramid", "[M1]"),
                ("2. Count vertices on folded solid (4 base corners + 1 apex): 5 vertices", "[A1]")
            ],
            "final_answer": "Square-based pyramid; 5 vertices",
            "pitfall": "Counting the 4 outer tips of the flat net as 4 separate apexes (they meet at 1 single apex when folded!).",
            "reverse_check": "4 base corners + 1 top point = 5 vertices."
        },
        q2={
            "title": "Question 2 (Calculating Overall Dimensions of a Unfolded Cuboid Net)",
            "marks": 2,
            "stem": "A closed medical vial box is a cuboid measuring <strong>length 12 cm, width 8 cm, and height 5 cm</strong>.<br>When unfolded into a standard cross-shaped net, the central strip consists of: <strong>Height (5 cm) + Length (12 cm) + Height (5 cm) + Length (12 cm)</strong>.<br>Calculate the total length and total width of the flat cross-shaped net.",
            "lines": 3,
            "ans_label": "Net Length & Width =",
            "choice_box": "Length: ________ cm | Width: ________ cm",
            "step_rows": [
                ("1. Total net length (4 panels in row): 5 + 12 + 5 + 12 = 34 cm", "[M1]"),
                ("2. Total net width (central width 8 cm + two side flaps of 5 cm each): 5 + 8 + 5 = 18 cm", "[A1]")
            ],
            "final_answer": "Total length = 34 cm, Total width = 18 cm",
            "pitfall": "Forgetting that both the left and right side flaps add 5 cm each to the 8 cm central width.",
            "reverse_check": "34 cm = 2×(12+5); 18 cm = 8 + 2×5."
        },
        q3={
            "title": "Question 3 (Cardboard Area Required for a Closed Cuboid Net)",
            "marks": 3,
            "stem": "A sterile dressings box measures <strong>20 cm long, 15 cm wide, and 10 cm high</strong>.<br>Calculate the total surface area of the 6-face net in <strong>cm²</strong>.",
            "svg": get_svg_for_topic("nets"),
            "lines": 4,
            "ans_label": "Net surface area =",
            "choice_box": "_____________ cm²",
            "step_rows": [
                ("1. Top & Bottom faces: 2 × (20 × 15) = 2 × 300 = 600 cm²", "[M1]"),
                ("2. Front/Back: 2 × (20 × 10) = 400 cm²; Left/Right: 2 × (15 × 10) = 300 cm²", "[M1]"),
                ("3. Sum all 6 faces of the net: 600 + 400 + 300 = 1,300 cm²", "[A1]")
            ],
            "final_answer": "1,300 cm²",
            "pitfall": "Calculating volume (20 × 15 × 10 = 3,000) instead of summing the 6 rectangular faces of the net.",
            "reverse_check": "2 × (300 + 200 + 150) = 2 × 650 = 1,300 cm²."
        },
        q4={
            "title": "Question 4 (Open-Top Storage Tray Net Calculation)",
            "marks": 3,
            "stem": "A pharmacy shelf tray has <strong>no lid (open top)</strong> and measures <strong>30 cm long, 20 cm wide, and 8 cm high</strong>.<br>The tray is stamped from a single rectangular sheet of plastic measuring <strong>50 cm by 40 cm</strong>.<br>Calculate the area of plastic <strong>wasted</strong> after stamping out the 5-face net.",
            "lines": 4,
            "ans_label": "Waste plastic area =",
            "choice_box": "_____________ cm²",
            "step_rows": [
                ("1. Area of 5-face open tray net: 1 Base (30×20 = 600) + 2 Long sides (2×30×8 = 480) + 2 Short sides (2×20×8 = 320) = 1,400 cm²", "[M1]"),
                ("2. Area of rectangular plastic sheet: 50 cm × 40 cm = 2,000 cm²", "[P1]"),
                ("3. Waste area: 2,000 - 1,400 = 600 cm²", "[A1]")
            ],
            "final_answer": "600 cm²",
            "pitfall": "Including a second 30×20 top face when the question states the tray has an open top (no lid).",
            "reverse_check": "1,400 cm² tray + 600 cm² waste = 2,000 cm² sheet."
        },
        q5={
            "title": "Question 5 (Cylinder Net Dimensions & Surface Area)",
            "marks": 4,
            "stem": "A cylindrical sharps bin has a circular base of <strong>radius 10 cm</strong> and a vertical <strong>height of 25 cm</strong>.<br>Its net consists of <strong>two circles</strong> (top and bottom) and <strong>one curved rectangular wrap</strong> whose width equals the circumference of the circle (<strong>2 × π × r</strong>).<br>Using <strong>π = 3.14</strong>, calculate the total surface area of the cylinder net.",
            "lines": 5,
            "ans_label": "Total net area =",
            "choice_box": "_____________ cm²",
            "step_rows": [
                ("1. Area of two circular ends: 2 × (3.14 × 10²) = 2 × 314 = 628 cm²", "[P1]"),
                ("2. Width of rectangular wrap (circumference): 2 × 3.14 × 10 = 62.8 cm", "[M1]"),
                ("3. Area of rectangular wrap: 62.8 cm × 25 cm = 1,570 cm²", "[P1]"),
                ("4. Total net surface area: 628 + 1,570 = 2,198 cm²", "[A1]")
            ],
            "final_answer": "2,198 cm²",
            "pitfall": "Using diameter (20) instead of radius (10) in πr², or forgetting to double the circular area for both top and bottom.",
            "reverse_check": "2πr(r + h) = 62.8 × (10 + 25) = 62.8 × 35 = 2,198 cm²."
        },
        q6={
            "title": "Question 6 (Cardboard Sheet Nesting & Cost Justification)",
            "marks": 4,
            "stem": "A medical packaging designer needs to stamp out <strong>60 closed cube nets</strong>. Each cube has side length <strong>10 cm</strong>.<br>Each unfolded cross-shaped net requires a bounding rectangle measuring <strong>40 cm long by 30 cm wide</strong> on the stamping press.<br>Master cardboard sheets measure <strong>120 cm by 90 cm</strong> and cost <strong>£3.50 per sheet</strong>.<br>The designer claims: <em>'We can stamp all 60 nets for no more than £25.00.'</em><br><br>Is the designer correct? Show full calculations to justify your answer.",
            "lines": 5,
            "ans_label": "Conclusion & Cost =",
            "choice_box": "Yes / No | Cost = £ ____________",
            "step_rows": [
                ("1. Nets per master sheet: Along 120 cm = 120 ÷ 40 = 3; Along 90 cm = 90 ÷ 30 = 3 → 3 × 3 = 9 nets per sheet", "[P1]"),
                ("2. Number of master sheets required for 60 nets: 60 ÷ 9 = 6.67 → Round UP to 7 whole sheets", "[M1]"),
                ("3. Total cost of 7 sheets: 7 × £3.50 = £24.50", "[P1]"),
                ("4. Conclusion: Yes, the designer is correct because £24.50 is £0.50 below the £25.00 limit", "[A1]")
            ],
            "final_answer": "Yes — 9 nets fit per sheet, requiring 7 sheets at £3.50 = £24.50 (which is under £25.00).",
            "pitfall": "Multiplying 6.67 × £3.50 = £23.33 without rounding up to 7 whole master sheets first.",
            "reverse_check": "7 sheets × 9 nets = 63 nets (covers 60 required); 7 × £3.50 = £24.50."
        }
    )
])

print(f"Loaded {len(WORKSHEETS_MATHS_PART2)} bespoke maths worksheet topics in bespoke_worksheets_maths_part2.py")
