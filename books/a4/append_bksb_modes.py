#!/usr/bin/env python3
"""
Appends BKSB_REMEDIATION_DATA (24 Modes) to books/a4/specialist_suite_content.py.
"""
import sys

bksb_code = '''
# =============================================================================
# BKSB & OneAdvanced Diagnostic Remediation Modes (24 Modes)
# =============================================================================

BKSB_MODES = [
    # Mode 1: Place Value & Significant Figures
    {
        "mode": 1,
        "title": "Place Value, Ordering Decimals & Significant Figures",
        "strand": "Number & Place Value",
        "badge": "M01",
        "kw": "calculator digits cash accounting figures",
        "diagnosis": (
            "On online BKSB diagnostic screens, learners frequently confuse the number of decimal places with significant figures, "
            "or incorrectly believe that longer decimal numbers (e.g. 0.125) are larger than shorter decimals (e.g. 0.4). "
            "Another widespread error is failing to maintain trailing place-value zeros when rounding to specific significant figures."
        ),
        "golden_rule": (
            "Rule: Pad decimals with trailing zeros to make them the same length before comparing (e.g. 0.400 is larger than 0.125). "
            "For significant figures, start counting from the FIRST non-zero digit on the left!"
        ),
        "model_fix": (
            "<b>Faulty Student Attempt:</b> Round 0.04085 to 2 significant figures. Student writes: 0.04 (incorrectly stopped at 2 decimal places).<br>"
            "<b>Correct Model Method:</b> First non-zero digit is 4 (1st sig fig). Next digit is 0 (2nd sig fig). The next digit is 8 (rounds up).<br>"
            "Answer: <b>0.041</b>. Check: Has exactly 2 significant figures."
        ),
        "drills": [
            "Order these decimals from smallest to largest: 0.082, 0.4, 0.19, 0.09, 0.305.",
            "Round 4,728 to 1 significant figure, and round 0.00562 to 2 significant figures.",
            "A digital micrometer measures a component thickness of 0.0485 mm. Express this to 2 significant figures."
        ]
    },

    # Mode 2: Negative Numbers in Practical Scenarios
    {
        "mode": 2,
        "title": "Negative Numbers, Overdrafts & Temperature Drops",
        "strand": "Number & Place Value",
        "badge": "M02",
        "kw": "thermometer cold winter temperature gauge",
        "diagnosis": (
            "Learners consistently stumble on directional arithmetic with negative numbers, often adding when calculating temperature differences "
            "or misunderstanding overdraft repayments (e.g. treating -£180 + £250 as -£430 or +£430 instead of +£70)."
        ),
        "golden_rule": (
            "Rule: Draw a vertical temperature line or money ladder! Going warmer/paying in moves UP (+); going colder/spending moves DOWN (-). "
            "Difference between a positive and negative number is always found by ADDING their absolute distances to zero!"
        ),
        "model_fix": (
            "<b>Faulty Student Attempt:</b> A commercial freezer is at -18&deg;C. A malfunction causes the temperature to rise by 7&deg;C. Student writes: -25&deg;C.<br>"
            "<b>Correct Model Method:</b> Rising temperature moves UP toward zero. -18 + 7 = <b>-11&deg;C</b>. Check: -11 is 7 degrees warmer than -18."
        ),
        "drills": [
            "At 05:00, the temperature was -4&deg;C. By 13:00, it had risen by 11&deg;C. What was the temperature at 13:00?",
            "A business bank account is overdrawn at -&pound;420. The owner pays in &pound;650 and pays a direct debit of &pound;180. What is the closing balance?",
            "Calculate the temperature difference between an industrial blast chiller at -22&deg;C and a kitchen at +21&deg;C."
        ]
    },

    # Mode 3: Order of Operations (BIDMAS) with Squares
    {
        "mode": 3,
        "title": "Order of Operations (BIDMAS / BODMAS)",
        "strand": "Number & Operations",
        "badge": "M03",
        "kw": "calculator operations calculation equations",
        "diagnosis": (
            "Candidates read calculations strictly from left to right, performing addition or subtraction before multiplication or division. "
            "This is heavily penalised in BKSB multi-step questions where operations are deliberately placed in mixed order."
        ),
        "golden_rule": (
            "Rule: Follow BIDMAS strictly: Brackets &rarr; Indices (powers/roots) &rarr; Division &amp; Multiplication &rarr; Addition &amp; Subtraction. "
            "Highlight multiplication and division blocks first!"
        ),
        "model_fix": (
            "<b>Faulty Student Attempt:</b> Evaluate 20 - 4 &times; 3 + 2. Student calculates 20 - 4 = 16, 16 &times; 3 = 48, 48 + 2 = 50. (0 marks!)<br>"
            "<b>Correct Model Method:</b> Multiplication first: 4 &times; 3 = 12. Expression becomes: 20 - 12 + 2 = 8 + 2 = <b>10</b>."
        ),
        "drills": [
            "Evaluate without a calculator: a) 15 + 5 &times; 4 &emsp; b) (18 &minus; 6) &divide; 3 &emsp; c) 40 &minus; 2 &times; 3&sup2;.",
            "A car hire company uses the formula: Total Cost = &pound;35 + &pound;22 &times; days. Calculate the cost for 6 days.",
            "Evaluate: 5 &times; (4 + 3&sup2;) &minus; 10 &divide; 2."
        ]
    },

    # Mode 4: Fractions of Quantities & Mixed Numbers
    {
        "mode": 4,
        "title": "Fractions of Quantities & Mixed Number Arithmetic",
        "strand": "Fractions",
        "badge": "M04",
        "kw": "measuring tape ruler fractions workshop",
        "diagnosis": (
            "Learners struggle when finding non-unit fractions (e.g. 3/8 of £480), often dividing by the numerator instead of denominator. "
            "When adding mixed numbers, learners frequently add numerators and denominators straight across (e.g. 1/2 + 1/3 = 2/5)."
        ),
        "golden_rule": (
            "Rule: Divide by the bottom (denominator), multiply by the top (numerator)! "
            "For adding/subtracting fractions, you MUST find a common denominator first!"
        ),
        "model_fix": (
            "<b>Faulty Student Attempt:</b> Calculate <sup>3</sup>/<sub>5</sub> of &pound;250. Student does 250 &times; 5 &divide; 3 = 416.66.<br>"
            "<b>Correct Model Method:</b> Divide by 5: 250 &divide; 5 = &pound;50 (1 part). Multiply by 3: 50 &times; 3 = <b>&pound;150</b>."
        ),
        "drills": [
            "A warehouse holds 720 boxes. <sup>5</sup>/<sub>8</sub> of the boxes are dispatched. How many boxes remain?",
            "Work out: 2 <sup>1</sup>/<sub>3</sub> + 1 <sup>1</sup>/<sub>4</sub>. Give your answer as a mixed number in simplest form.",
            "A joiner cuts a piece of timber of length <sup>3</sup>/<sub>4</sub> m from a plank of length 2 <sup>1</sup>/<sub>2</sub> m. What length of plank remains?"
        ]
    },

    # Mode 5: Decimal Multiplication & Division
    {
        "mode": 5,
        "title": "Decimal Multiplication & Dividing by Decimals",
        "strand": "Decimals",
        "badge": "M05",
        "kw": "cash register currency shopping receipt",
        "diagnosis": (
            "When multiplying decimals (e.g. 0.4 &times; 0.03), learners miscount decimal places and give answers like 0.12 instead of 0.012. "
            "When dividing by a decimal (e.g. 24 &divide; 0.6), learners get confused and try to divide without clearing the decimal divisor."
        ),
        "golden_rule": (
            "Rule: Multiply without decimals as whole numbers, then count TOTAL decimal places in both numbers and count back from the right! "
            "For division by a decimal: Multiply BOTH numbers by 10, 100, or 1000 to make the divisor a whole number before dividing!"
        ),
        "model_fix": (
            "<b>Faulty Student Attempt:</b> Work out 0.6 &times; 0.04. Student writes: 0.24 (only counted 2 decimal places).<br>"
            "<b>Correct Model Method:</b> Whole numbers: 6 &times; 4 = 24. Total decimal places: 1 + 2 = 3 decimal places. Answer: <b>0.024</b>."
        ),
        "drills": [
            "Calculate without a calculator: a) 0.8 &times; 0.07 &emsp; b) 1.5 &times; 0.04 &emsp; c) 3.6 &divide; 0.09.",
            "A roll of electrical wire is 45 metres long. An electrician cuts pieces measuring 1.5 metres each. How many pieces can be cut?",
            "Diesel costs &pound;1.45 per litre. A commercial vehicle takes 30.5 litres. Calculate the total cost to 2 decimal places."
        ]
    },

    # Mode 6: Reverse Percentages (Original Value)
    {
        "mode": 6,
        "title": "Reverse Percentages: Original Value Before Discount or VAT",
        "strand": "Percentages",
        "badge": "M06",
        "kw": "sale discount price tag store retail",
        "diagnosis": (
            "This is the #1 most failed maths question on BKSB Level 2. "
            "When a price is discounted by 20% to £80, learners incorrectly calculate 20% of £80 (£16) and ADD it back to get £96. "
            "This is fundamentally wrong because the 20% was deducted from the ORIGINAL (larger) amount, not the sale price!"
        ),
        "golden_rule": (
            "Rule: The original value is ALWAYS 100%. "
            "If discounted by 20%, the sale price represents 80% (0.80). "
            "To find the original: Original = New Value &divide; Percentage Multiplier!"
        ),
        "model_fix": (
            "<b>Faulty Student Attempt:</b> A coat costs &pound;120 after a 20% discount. Student calculates 20% of 120 = &pound;24, so original = 120 + 24 = &pound;144. (0 marks!)<br>"
            "<b>Correct Model Method:</b> Original = 100%. Sale price = 100% - 20% = 80% = 0.80.<br>"
            "Original = 120 &divide; 0.80 = <b>&pound;150.00</b>. Check: 20% of &pound;150 = &pound;30 &rarr; &pound;150 - &pound;30 = &pound;120. (Matches!)"
        ),
        "drills": [
            "A sofa costs &pound;510.00 in a 15% off sale. Calculate the original price before the sale. Show a check of your answer.",
            "An invoice total is &pound;744.00 including VAT at 20%. Calculate the cost of the goods before VAT was added.",
            "A gym membership fee increased by 8% to &pound;43.20 per month. What was the original monthly fee before the increase?"
        ]
    },

    # Mode 7: Percentage Change & Single Multipliers
    {
        "mode": 7,
        "title": "Percentage Increase, Decrease & Percentage Change",
        "strand": "Percentages",
        "badge": "M07",
        "kw": "business profit growth financial report",
        "diagnosis": (
            "Learners get confused between calculating an increased amount vs calculating the percentage change between two figures. "
            "When calculating % change, learners frequently divide by the NEW value instead of the ORIGINAL value."
        ),
        "golden_rule": (
            "Rule: % Change = (Difference &divide; Original Value) &times; 100. Always divide by the starting (original) figure!"
        ),
        "model_fix": (
            "<b>Faulty Student Attempt:</b> A business revenue grew from &pound;40,000 to &pound;50,000. Student writes: (10,000 &divide; 50,000) &times; 100 = 20%.<br>"
            "<b>Correct Model Method:</b> Difference = &pound;10,000. Original = &pound;40,000.<br>"
            "% Increase = (10,000 &divide; 40,000) &times; 100 = <b>25%</b>."
        ),
        "drills": [
            "A commercial property was purchased for &pound;180,000 and sold for &pound;207,000. Calculate the percentage profit.",
            "A delivery driver's daily mileage decreased from 120 miles to 102 miles. Calculate the percentage decrease.",
            "Increase &pound;350 by 18% using a single decimal multiplier."
        ]
    },

    # Mode 8: Ratio Sharing (Part-to-Part vs Part-to-Whole)
    {
        "mode": 8,
        "title": "Ratio Sharing: Part-to-Part vs Part-to-Whole Traps",
        "strand": "Ratio & Proportion",
        "badge": "M08",
        "kw": "paint mixing colours decorator workshop",
        "diagnosis": (
            "On BKSB, questions often state: 'A and B share money in the ratio 3 : 2. Person A receives £60. How much does Person B receive?' "
            "Learners habitually add 3 + 2 = 5 and divide £60 by 5! This fails because £60 is Person A's share (3 parts), NOT the total money!"
        ),
        "golden_rule": (
            "Rule: Read carefully: Is the given number the TOTAL amount, or ONE PERSON'S SHARE? "
            "If it is one person's share, divide by THEIR ratio parts to find the value of 1 part!"
        ),
        "model_fix": (
            "<b>Faulty Student Attempt:</b> Sand and cement are mixed 4 : 1. A builder uses 20 kg of cement. Total mortar? Student does 20 &divide; 5 = 4 kg. (0 marks!)<br>"
            "<b>Correct Model Method:</b> Cement is 1 part = 20 kg. Sand is 4 parts = 4 &times; 20 = 80 kg. Total mortar = 80 + 20 = <b>100 kg</b>."
        ),
        "drills": [
            "Two partners share business profits in the ratio 5 : 3. The majority partner receives &pound;15,000. How much does the other partner receive?",
            "Share &pound;450 between three charities in the ratio 4 : 3 : 2.",
            "A paint shade mixes blue and yellow paint in the ratio 3 : 7. A decorator has 12 litres of blue paint. How much yellow paint is needed?"
        ]
    },

    # Mode 9: Scale Drawings & Map Ratios
    {
        "mode": 9,
        "title": "Scale Drawings, Architectural Plans & Map Ratios",
        "strand": "Ratio & Measures",
        "badge": "M09",
        "kw": "architectural blueprint floor plan ruler",
        "diagnosis": (
            "Learners get confused converting between scale plan units (cm or mm) and real-life dimensions (metres). "
            "On a 1 : 50 plan, multiplying 8 cm by 50 gives 400, but learners write 400 metres instead of 400 cm (4.0 metres)."
        ),
        "golden_rule": (
            "Rule: Real length = Plan length &times; Scale factor (in the same units). Then convert cm to metres by dividing by 100!"
        ),
        "model_fix": (
            "<b>Faulty Student Attempt:</b> On a 1 : 100 plan, a room is 6.5 cm long. Student writes real length = 650 metres.<br>"
            "<b>Correct Model Method:</b> Real length = 6.5 cm &times; 100 = 650 cm. Divide by 100 = <b>6.5 metres</b>."
        ),
        "drills": [
            "On an architectural plan drawn to 1 : 50, a patio measures 9.2 cm by 6.0 cm. Calculate the real-world perimeter and area in metres.",
            "A walking map has a scale of 1 : 25,000. Two landmarks are 4.8 cm apart on the map. What is the actual distance in kilometres?",
            "A warehouse room is 18 metres long in reality. On a 1 : 200 plan, what should its length be in centimetres?"
        ]
    },

    # Mode 10: Compound Area (L-Shapes & Cutouts)
    {
        "mode": 10,
        "title": "Compound Area & Perimeter of L-Shapes",
        "strand": "Geometry & Measures",
        "badge": "M10",
        "kw": "flooring carpet tiling room renovation",
        "diagnosis": (
            "When given an L-shape with missing side lengths, learners fail to calculate the missing sides before finding perimeter, "
            "or multiply outer dimensions together without splitting the shape into separate rectangles."
        ),
        "golden_rule": (
            "Rule: For L-shapes, vertical sides balance (Top vertical = Bottom vertical + Step). "
            "Horizontal sides balance (Total width = Left width + Right width). "
            "Split the shape into two rectangles, find each area, and add them!"
        ),
        "model_fix": (
            "<b>Faulty Student Attempt:</b> L-shape outer dimensions 8 m by 6 m with cutout 4 m by 3 m. Student writes: Area = 8 &times; 6 = 48 m&sup2;.<br>"
            "<b>Correct Model Method:</b> Outer box = 8 &times; 6 = 48 m&sup2;. Cutout = 4 &times; 3 = 12 m&sup2;. Net Area = 48 &minus; 12 = <b>36 m&sup2;</b>."
        ),
        "drills": [
            "An L-shaped lawn has outer dimensions: 12 m, 9 m, 5 m, 4 m, 7 m, 5 m. Calculate the total perimeter and total lawn area.",
            "A rectangular room measuring 6.5 m by 4.2 m has a rectangular hearth tiled area measuring 1.5 m by 0.8 m. Carpet is laid over the rest. Find the carpet area.",
            "Tiling costs &pound;24.00 per square metre. Calculate the cost to tile an L-shaped kitchen floor with rectangles 5m &times; 3m and 4m &times; 2m."
        ]
    },

    # Mode 11: Circle Geometry (&pi;r&sup2; vs &pi;d)
    {
        "mode": 11,
        "title": "Circle Geometry: Area (&pi;r&sup2;) vs Circumference (&pi;d)",
        "strand": "Geometry",
        "badge": "M11",
        "kw": "circular lawn garden landscape design",
        "diagnosis": (
            "Learners constantly mix up radius and diameter, or confuse Area (&pi;r&sup2;) with Circumference (&pi;d). "
            "When given a diameter of 6m, learners frequently calculate &pi; &times; 6&sup2; without halving the diameter first!"
        ),
        "golden_rule": (
            "Rule: Circumference is distance around = &pi; &times; diameter. "
            "Area is space inside = &pi; &times; radius&sup2;. "
            "Always check: Did the question give RADIUS or DIAMETER? If diameter, halve it first to get radius!"
        ),
        "model_fix": (
            "<b>Faulty Student Attempt:</b> Find the area of a circular rug of diameter 4 m. Student does: 3.14 &times; 4&sup2; = 50.24 m&sup2;.<br>"
            "<b>Correct Model Method:</b> Diameter = 4 m &rarr; Radius = 2 m. Area = &pi;r&sup2; = 3.14 &times; 2&sup2; = 3.14 &times; 4 = <b>12.56 m&sup2;</b>."
        ),
        "drills": [
            "A circular hot tub has a radius of 1.4 metres. Calculate the surface area of the water using &pi; = 3.14. Include units.",
            "A circular bicycle wheel has a diameter of 70 cm. Calculate the circumference of the wheel. How far does the bicycle travel in 10 full turns?",
            "A semicircular patio has a straight diameter edge of 8.0 metres. Calculate the total perimeter (curved arc + straight edge)."
        ]
    },

    # Mode 12: Volume of Prisms & Cylinders
    {
        "mode": 12,
        "title": "Volume & Capacity of Prisms and Cylinders",
        "strand": "Geometry & Measures",
        "badge": "M12",
        "kw": "storage tank cylinder industrial warehouse",
        "diagnosis": (
            "When calculating the volume of a triangular prism or cylinder, learners forget that Volume = Area of Cross-Section &times; Length. "
            "For triangular prisms, learners forget to divide by 2 for the triangle. For cylinders, they forget 1 m&sup3; = 1,000 litres."
        ),
        "golden_rule": (
            "Rule: Volume of cylinder = &pi;r&sup2;h. Volume of triangular prism = (<sup>1</sup>/<sub>2</sub> &times; base &times; height) &times; length. "
            "Convert cubic metres to litres by multiplying by 1,000!"
        ),
        "model_fix": (
            "<b>Faulty Student Attempt:</b> Water tank 2 m &times; 1.5 m &times; 1.2 m. Student writes: Capacity = 3.6 litres.<br>"
            "<b>Correct Model Method:</b> Volume = 2 &times; 1.5 &times; 1.2 = 3.6 m&sup3;. Multiply by 1,000 = <b>3,600 litres</b>."
        ),
        "drills": [
            "A cylindrical rainwater collection barrel has radius 0.4 metres and height 1.2 metres. Calculate its capacity in litres (&pi; = 3.14).",
            "A steel triangular prism bar has base 6 cm, height 4 cm, and length 50 cm. Calculate its volume in cubic centimetres.",
            "A rectangular swimming pool measures 15 m long, 6 m wide, and has an average depth of 1.6 m. How many litres of water does it contain?"
        ]
    },

    # Mode 13: Compound Measures: Speed, Distance & Time
    {
        "mode": 13,
        "title": "Speed, Distance & Time: Decimal Hours Trap",
        "strand": "Measures & Rates",
        "badge": "M13",
        "kw": "speedometer highway delivery transport van",
        "diagnosis": (
            "The classic BKSB time trap: when a journey takes 2 hours 15 minutes, learners calculate using 2.15 hours! "
            "This gives completely incorrect speeds and arrival times because time is base-60, not base-100!"
        ),
        "golden_rule": (
            "Rule: Never use minutes as decimals directly! Divide minutes by 60 to get decimal hours (15 mins = 0.25 hrs, 30 mins = 0.5 hrs, 45 mins = 0.75 hrs, 20 mins = 0.333 hrs). "
            "Speed = Distance &divide; Time. Time = Distance &divide; Speed!"
        ),
        "model_fix": (
            "<b>Faulty Student Attempt:</b> A driver covers 110 miles in 2 hours 30 minutes. Student calculates 110 &divide; 2.30 = 47.8 mph.<br>"
            "<b>Correct Model Method:</b> 30 minutes = 30 &divide; 60 = 0.5 hours. Total time = 2.5 hours. Speed = 110 &divide; 2.5 = <b>44 mph</b>."
        ),
        "drills": [
            "A delivery van travels 156 miles at an average speed of 48 mph. Calculate the travel time in hours and minutes.",
            "A train departs at 10:35 and completes a 95-mile journey arriving at 12:20. Calculate the average train speed in mph.",
            "Convert to decimal hours: a) 1 hour 45 mins &emsp; b) 3 hours 12 mins &emsp; c) 40 minutes."
        ]
    },

    # Mode 14: Compound Measures: Density, Mass & Volume
    {
        "mode": 14,
        "title": "Density, Mass, Volume & Pressure Formulas",
        "strand": "Measures & Rates",
        "badge": "M14",
        "kw": "laboratory scale weighing chemical sample",
        "diagnosis": (
            "Learners confuse the formula triangle relationships for Density = Mass / Volume and Pressure = Force / Area. "
            "When asked to calculate mass, learners divide instead of multiplying."
        ),
        "golden_rule": (
            "Rule: Remember the triangle: Mass on top, Density and Volume on the bottom (M = D &times; V). "
            "Force on top, Pressure and Area on the bottom (F = P &times; A)!"
        ),
        "model_fix": (
            "<b>Faulty Student Attempt:</b> A block of concrete has volume 0.5 m&sup3; and density 2,400 kg/m&sup3;. Student calculates Mass = 2400 &divide; 0.5 = 4800.<br>"
            "<b>Correct Model Method:</b> Mass = Density &times; Volume = 2,400 &times; 0.5 = <b>1,200 kg</b>."
        ),
        "drills": [
            "A metal casting has mass 4.2 kg and volume 0.0006 m&sup3;. Calculate the density in kg/m&sup3;.",
            "A hydraulic press applies a force of 6,000 N over a piston area of 0.25 m&sup2;. Calculate the pressure in N/m&sup2;.",
            "Oak timber has a density of 750 kg/m&sup3;. A timber beam measures 4 m by 0.2 m by 0.15 m. Calculate the weight of the beam in kg."
        ]
    },

    # Mode 15: Mean from Grouped Frequency Tables
    {
        "mode": 15,
        "title": "Estimated Mean from Grouped Frequency Tables",
        "strand": "Statistics",
        "badge": "M15",
        "kw": "statistical charts graph survey data",
        "diagnosis": (
            "When given grouped intervals (e.g. 10-19: 5 items), learners add the frequencies and divide by the number of rows, "
            "completely ignoring the interval midpoints and total sample size!"
        ),
        "golden_rule": (
            "Rule: 1. Find midpoint of each interval (add boundaries and divide by 2). "
            "2. Multiply midpoint &times; frequency for each row. "
            "3. Sum all (midpoint &times; frequency) products. "
            "4. Divide by total frequency (&Sigma;f)!"
        ),
        "model_fix": (
            "<b>Faulty Student Attempt:</b> Intervals 0-9 (4), 10-19 (6). Student calculates (4 + 6) &divide; 2 = 5. (0 marks!)<br>"
            "<b>Correct Model Method:</b> Midpoints: 4.5 and 14.5. Products: (4.5 &times; 4) + (14.5 &times; 6) = 18 + 87 = 105. "
            "Total count = 4 + 6 = 10. Estimated Mean = 105 &divide; 10 = <b>10.5</b>."
        ),
        "drills": [
            "Calculate an estimated mean score for: 1&ndash;5 (6), 6&ndash;10 (14), 11&ndash;15 (12), 16&ndash;20 (8).",
            "A depot logs delivery delays: 0&ndash;9 mins (15), 10&ndash;19 mins (25), 20&ndash;29 mins (10). Find the estimated mean delay.",
            "Explain why calculations from grouped frequency tables produce an 'estimate' rather than an exact mean."
        ]
    },

    # Mode 16: Combined Probability of Independent Events
    {
        "mode": 16,
        "title": "Combined Probability: Independent Events & Trees",
        "strand": "Statistics & Probability",
        "badge": "M16",
        "kw": "probability raffle tickets dice chance",
        "diagnosis": (
            "When asked to calculate the probability of two independent events happening (e.g. P(A and B)), "
            "learners mistakenly ADD the probabilities instead of MULTIPLYING them, yielding values greater than 1."
        ),
        "golden_rule": (
            "Rule: For independent events happening together: P(A and B) = P(A) &times; P(B). "
            "Multiply probabilities! Also remember: P(Not A) = 1 &minus; P(A)!"
        ),
        "model_fix": (
            "<b>Faulty Student Attempt:</b> Chance of rain on Sat is 0.4 and Sun is 0.3. Probability of rain on BOTH days? Student does 0.4 + 0.3 = 0.7.<br>"
            "<b>Correct Model Method:</b> Multiply independent probabilities: 0.4 &times; 0.3 = <b>0.12</b> (12% chance)."
        ),
        "drills": [
            "A machine has two independent safety sensors. Sensor 1 has a 1 in 50 failure rate. Sensor 2 has a 1 in 100 failure rate. Calculate the probability that both fail.",
            "A fair 6-sided dice is rolled, and a fair coin is tossed. Calculate the probability of rolling an even number AND flipping heads.",
            "A candidate has a 0.85 chance of passing a test. What is the probability that they FAIL the test?"
        ]
    },

    # Mode 17: Comma Splices & Sentence Boundaries
    {
        "mode": 17,
        "title": "Comma Splices & Run-On Sentences",
        "strand": "SPaG & Punctuation",
        "badge": "E17",
        "kw": "writing notes pen paper office desk",
        "diagnosis": (
            "Learners join two independent main clauses with only a comma (e.g. 'The report is ready, I will email it today.'). "
            "This is called a comma splice and is one of the most heavily penalised SPaG errors on BKSB English."
        ),
        "golden_rule": (
            "Rule: A comma cannot glue two complete sentences together! Use one of three fixes: "
            "1. Full stop. 2. Semicolon (;). 3. Coordinating conjunction (and, but, so, because)!"
        ),
        "model_fix": (
            "<b>Incorrect Comma Splice:</b> The training course was challenging, we learned valuable new skills.<br>"
            "<b>Three Correct Alternatives:</b><br>"
            "1. <i>The training course was challenging. We learned valuable new skills.</i> (Full stop)<br>"
            "2. <i>The training course was challenging; we learned valuable new skills.</i> (Semicolon)<br>"
            "3. <i>The training course was challenging, but we learned valuable new skills.</i> (Conjunction)"
        ),
        "drills": [
            "Correct this sentence in two different ways: 'The equipment arrived late, the project deadline was met.'",
            "Identify the comma splice and fix it: 'Staff attended the briefing, however the new rota was not approved.'",
            "Write a complex sentence using a semicolon to link two closely related independent clauses."
        ]
    },

    # Mode 18: Apostrophes of Omission vs Possession
    {
        "mode": 18,
        "title": "Apostrophes: Omission vs Possession & Its/It's",
        "strand": "SPaG & Punctuation",
        "badge": "E18",
        "kw": "library books studying reading proofreading",
        "diagnosis": (
            "Learners confuse 'it's' (it is / it has) with 'its' (belonging to it), or insert apostrophes into regular plurals (the 'greengrocer's apostrophe' e.g. 'apple's for sale')."
        ),
        "golden_rule": (
            "Rule: It's ONLY has an apostrophe if it stands for 'it is' or 'it has'! "
            "If it shows ownership, it has NO apostrophe (the dog wagged its tail). Plurals NEVER take an apostrophe!"
        ),
        "model_fix": (
            "<b>Incorrect Usage:</b> The company updated it's website, but customer's complained about errors.<br>"
            "<b>Correct Model Method:</b> <i>'The company updated <b>its</b> website, but <b>customers</b> complained about errors.'</i>"
        ),
        "drills": [
            "Insert apostrophes correctly: 'The supervisors report confirmed that the departments budget was approved.'",
            "Choose between its and it's: '______ essential that the vehicle has ______ brakes inspected.'",
            "Correct the apostrophe errors: 'All driver's must return their key's to the office.'"
        ]
    },

    # Mode 19: Commonly Confused Homophones
    {
        "mode": 19,
        "title": "Commonly Confused Homophones (Their / There / They're)",
        "strand": "SPaG & Spelling",
        "badge": "E19",
        "kw": "spelling dictionary grammar books study",
        "diagnosis": (
            "BKSB frequently tests homophones that sound identical but differ in spelling and meaning: "
            "their (ownership), there (location/pointer), they're (they are); practice (noun) vs practise (verb); affect (verb) vs effect (noun)."
        ),
        "golden_rule": (
            "Rule: Substitute words to test! If you can say 'they are', use they're. If it has 'here' inside, it's about place (t-here). "
            "Practice is the noun (with a c like advice); practise is the verb (with an s like advise)!"
        ),
        "model_fix": (
            "<b>Incorrect Usage:</b> There going to submit there reports over their.<br>"
            "<b>Correct Model Method:</b> <i>'<b>They're</b> going to submit <b>their</b> reports over <b>there</b>.'</i>"
        ),
        "drills": [
            "Select the correct homophone: 'The new regulations will (affect/effect) all staff members.'",
            "Select the correct form: 'Doctors must (practice/practise) medical hygiene daily.'",
            "Fill in blanks with their, there, or they're: '______ waiting in the reception for ______ manager.'"
        ]
    },

    # Mode 20: Subject-Verb Agreement
    {
        "mode": 20,
        "title": "Subject-Verb Agreement with Collective Nouns",
        "strand": "SPaG & Grammar",
        "badge": "E20",
        "kw": "classroom discussion tutor student whiteboard",
        "diagnosis": (
            "Learners struggle matching singular subjects with singular verbs when separated by prepositional phrases (e.g. 'A box of tools were stolen' instead of 'was stolen')."
        ),
        "golden_rule": (
            "Rule: Identify the TRUE head noun subject! Ignore intervening phrases (like 'of tools' or 'as well as the staff'). "
            "Singular subject = singular verb (has/is/was); plural subject = plural verb (have/are/were)!"
        ),
        "model_fix": (
            "<b>Incorrect Usage:</b> The team of clinical nurses were commended for their work.<br>"
            "<b>Correct Model Method:</b> Head noun is singular ('The team'). Correct: <i>'The team of clinical nurses <b>was</b> commended for its work.'</i>"
        ),
        "drills": [
            "Select correct verb: 'Neither the manager nor the supervisor (was/were) available.'",
            "Select correct verb: 'A delivery of 50 parcels (has/have) arrived at the loading bay.'",
            "Fix the agreement error: 'The list of candidate names are posted on the noticeboard.'"
        ]
    },

    # Mode 21: Integrating Quotations without Plagiarism
    {
        "mode": 21,
        "title": "Synthesising Direct & Indirect Evidence Smoothly",
        "strand": "Reading & Writing",
        "badge": "E21",
        "kw": "research reading notes highlighter library",
        "diagnosis": (
            "On reading comparison questions, learners copy entire paragraphs verbatim from the text without quotation marks, "
            "or 'dump' floating quotes without introductory framing."
        ),
        "golden_rule": (
            "Rule: Never dump a quote as an isolated sentence! Embed short 3-5 word snippets into your own grammatical sentence, "
            "or paraphrase in your own words while citing the author!"
        ),
        "model_fix": (
            "<b>Clunky Quoting:</b> The author thinks pollution is bad. 'Air pollution contributes to 36,000 deaths annually.' This shows it is serious.<br>"
            "<b>Smooth Synthesised Integration:</b> Vance underscores the severity of the crisis by highlighting that airborne toxins contribute to <i>'approximately 36,000 premature deaths annually'</i> across the UK."
        ),
        "drills": [
            "Embed this quote into a single analytical sentence: 'remote staff experience chronic professional isolation'",
            "Paraphrase this statistic accurately without using the original phrasing: '74% of employers operate hybrid frameworks'",
            "Explain the difference between direct quoting and accurate paraphrasing."
        ]
    },

    # Mode 22: Formal Letter Structure & Architecture
    {
        "mode": 22,
        "title": "Formal Letter Formatting & Salutation Conventions",
        "strand": "Writing Architecture",
        "badge": "E22",
        "kw": "envelope letter postal mail office writing",
        "diagnosis": (
            "Learners mix up formal letter salutations and sign-offs, writing 'Yours sincerely' when addressing an unknown recipient ('Dear Sir/Madam'), "
            "or omitting the recipient and sender addresses entirely."
        ),
        "golden_rule": (
            "Rule: Dear Sir/Madam &rarr; Yours faithfully (You don't know their name, so keep faith!). "
            "Dear Mr/Ms [Surname] &rarr; Yours sincerely (You know their name, so be sincere!)."
        ),
        "model_fix": (
            "<b>Incorrect Mismatch:</b> Opening: 'Dear Sir/Madam,' &rarr; Ending: 'Yours sincerely, John Smith.'<br>"
            "<b>Correct Pairing:</b> Opening: 'Dear Sir or Madam,' &rarr; Ending: <b>'Yours faithfully, John Smith.'</b>"
        ),
        "drills": [
            "Draw a layout diagram showing the standard positions for sender address, date, recipient address, subject line, and sign-off.",
            "Which sign-off is required for: a) 'Dear Councillor Sterling,' &emsp; b) 'Dear Recruitment Manager,'",
            "Write an effective subject heading for a formal letter complaining about delayed public transport."
        ]
    },

    # Mode 23: Persuasive Language Devices & Rhetorical Impact
    {
        "mode": 23,
        "title": "Persuasive Techniques: Rhetoric, Rule of Three & Emotive Tone",
        "strand": "Writing Craft",
        "badge": "E23",
        "kw": "public speaking microphone speech presentation",
        "diagnosis": (
            "Learners attempt to write persuasively by merely asserting opinions or using aggressive demands, "
            "lacking rhetorical devices (AFOREST: Alliteration, Facts, Opinions, Rhetorical questions, Emotive language, Statistics, Tripling)."
        ),
        "golden_rule": (
            "Rule: Persuasion blends logic and emotion! Back emotional appeals with credible facts, and use a triadic structure (Rule of Three) "
            "to make key arguments memorable!"
        ),
        "model_fix": (
            "<b>Weak Statement:</b> We need a new sports centre because kids are bored.<br>"
            "<b>Persuasive Rhetorical Model:</b> A modern sports pavilion will not merely provide a gym; it will instil discipline, foster lasting friendships, and revitalise our entire community."
        ),
        "drills": [
            "Write a persuasive sentence using the Rule of Three to support flexible working hours.",
            "Construct a rhetorical question designed to make a council committee reconsider leisure cuts.",
            "Rewrite this informal sentence in a persuasive, professional tone: 'The canteen food is rubbish and costs too much.'"
        ]
    },

    # Mode 24: Proofreading Strategies for High-Frequency Errors
    {
        "mode": 24,
        "title": "Proofreading Protocols & High-Frequency Spelling Slips",
        "strand": "SPaG & Proofreading",
        "badge": "E24",
        "kw": "proofreading red pen corrections checklist document",
        "diagnosis": (
            "Learners finish written tasks and immediately close their paper without proofreading, throwing away up to 12 SPaG marks "
            "on preventable slips like missing capital letters on proper nouns, doubled consonants (accommodation, necessary), and missing full stops."
        ),
        "golden_rule": (
            "Rule: Reserve 5 minutes at the end of every exam specifically for proofreading! "
            "Read your text backwards sentence by sentence to focus exclusively on punctuation and spelling without getting distracted by narrative flow!"
        ),
        "model_fix": (
            "<b>Unchecked Draft:</b> on wednesday me and sarah went to manchester for a buisness conferance it was realy usefull.<br>"
            "<b>Proofread Model:</b> <i>'On Wednesday, Sarah and I travelled to Manchester for a <b>business</b> <b>conference</b>; it was <b>really</b> <b>useful</b>.'</i>"
        ),
        "drills": [
            "Proofread and correct 5 errors in this sentence: 'The goverment offical reccommended that every buisness update there fire safety plan.'",
            "Spell these high-frequency words correctly: a) accomodation &emsp; b) neccessary &emsp; c) definitly &emsp; d) seperate.",
            "Explain the backward reading technique and why it improves proofreading accuracy."
        ]
    }
]

print("BKSB_MODES (24) defined successfully!")
'''

with open('books/a4/specialist_suite_content.py', 'a') as f:
    f.write(bksb_code)

print("Appended BKSB_REMEDIATION_DATA to specialist_suite_content.py!")
