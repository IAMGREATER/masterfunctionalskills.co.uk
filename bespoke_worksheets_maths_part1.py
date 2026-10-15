#!/usr/bin/env python3
"""
Master Functional Skills - Bespoke Maths Worksheets Part 1 (17 Core Topics).
100% genuine, number-rich, Pearson Edexcel aligned 6-question worksheets and mark schemes.
"""

from build_topic_dataset import make_maths_topic
from generate_all_worksheets_complete import get_svg_for_topic

WORKSHEETS_MATHS_PART1 = [
    # 1. FRACTIONS
    make_maths_topic(
        "fractions",
        "Fractions",
        "L1.9 • L2.8 • L2.9",
        "To find a fraction of an amount: divide by the denominator (bottom), then multiply by the numerator (top). When adding or subtracting fractions, always find a common denominator first.",
        {
            "title": "Question 1 (Level 1 Simplifying & Equivalence)",
            "marks": 2,
            "stem": "Simplify the fraction <strong>36/48</strong> to its simplest form.",
            "lines": 3,
            "ans_label": "Simplest form =",
            "choice_box": "____________________",
            "step_rows": [
                ("1. Identify Highest Common Factor (HCF = 12) or divide numerator and denominator successively by 2, 2, and 3", "[M1]"),
                ("2. 36 ÷ 12 = 3; 48 ÷ 12 = 4; Result: 3/4", "[A1]")
            ],
            "final_answer": "3/4",
            "pitfall": "Stopping at 18/24 or 9/12 without reducing fully to lowest terms.",
            "reverse_check": "3/4 × 12/12 = 36/48."
        },
        {
            "title": "Question 2 (Level 2 Adding Mixed Numbers)",
            "marks": 2,
            "stem": "Work out: <strong>2 1/3 + 1 3/4</strong> without a calculator.<br>Give your answer as a mixed number in its simplest form.",
            "lines": 3,
            "ans_label": "Sum =",
            "choice_box": "____________________",
            "step_rows": [
                ("1. Convert to improper fractions (7/3 + 7/4) with common denominator 12: 28/12 + 21/12 = 49/12", "[M1]"),
                ("2. Convert improper fraction to mixed number: 49 ÷ 12 = 4 remainder 1 → 4 1/12", "[A1]")
            ],
            "final_answer": "4 1/12",
            "pitfall": "Adding numerators and denominators directly (3 4/7). Denominators must be matched first!",
            "reverse_check": "4 1/12 - 1 3/4 = 49/12 - 21/12 = 28/12 = 7/3 = 2 1/3."
        },
        {
            "title": "Question 3 (Level 1 Hospital Pharmacy Dispatches)",
            "marks": 3,
            "stem": "A central hospital pharmacy stocks <strong>720 vials</strong> of specialized antibiotic.<br>• <strong>3/8</strong> of the vials are dispatched to Paediatric Intensive Care.<br>• <strong>2/5</strong> of the vials are dispatched to Emergency Assessment.<br><br>How many vials remain in central pharmacy stock?",
            "lines": 4,
            "ans_label": "Remaining vials =",
            "choice_box": "_____________ vials",
            "step_rows": [
                ("1. PICU dispatches: (720 ÷ 8) × 3 = 90 × 3 = 270 vials", "[M1]"),
                ("2. Emergency dispatches: (720 ÷ 5) × 2 = 144 × 2 = 288 vials", "[M1]"),
                ("3. Remaining stock: 720 - (270 + 288) = 720 - 558 = 162 vials", "[A1]")
            ],
            "final_answer": "162 vials",
            "pitfall": "Calculating 2/5 of the remaining stock (450) rather than 2/5 of the original 720 vials.",
            "reverse_check": "270 + 288 + 162 = 720 vials."
        },
        {
            "title": "Question 4 (Level 2 Apprentice Construction Timber Cut)",
            "marks": 3,
            "stem": "A site carpenter cuts roof struts from a <strong>4.8 metre</strong> timber beam.<br>The first strut requires <strong>1 1/4 metres</strong>, the second requires <strong>1 3/5 metres</strong>, and <strong>1/10 metre</strong> is lost as saw-cut waste.<br><br>Calculate the exact length of timber remaining on the beam. Give your answer in metres.",
            "lines": 4,
            "ans_label": "Remaining timber =",
            "choice_box": "_____________ m",
            "step_rows": [
                ("1. Convert fractions to decimals (or twentieths): 1 1/4 = 1.25 m; 1 3/5 = 1.60 m; 1/10 = 0.10 m", "[M1]"),
                ("2. Sum used and wasted timber: 1.25 + 1.60 + 0.10 = 2.95 m", "[P1]"),
                ("3. Subtract from total beam length: 4.80 - 2.95 = 1.85 m (or 1 17/20 m)", "[A1]")
            ],
            "final_answer": "1.85 m (or 1 17/20 m)",
            "pitfall": "Forgetting to deduct the 1/10 m saw-cut waste, which yields 1.95 m.",
            "reverse_check": "1.85 + 1.25 + 1.60 + 0.10 = 4.80 m."
        },
        {
            "title": "Question 5 (Level 2 Ward Dietary Survey)",
            "marks": 4,
            "stem": "In an acute medical unit with <strong>96 patients</strong>:<br>• <strong>5/12</strong> require diabetic meal plans.<br>• <strong>1/4</strong> require low-sodium meal plans.<br>• <strong>1/6</strong> require texture-modified soft diets.<br>• The remaining patients receive standard hospital meals.<br><br>How many patients receive standard hospital meals?",
            "lines": 5,
            "ans_label": "Standard meals =",
            "choice_box": "_____________ patients",
            "step_rows": [
                ("1. Diabetic meals: (96 ÷ 12) × 5 = 8 × 5 = 40 patients", "[P1]"),
                ("2. Low-sodium: 96 ÷ 4 = 24 patients; Soft diet: 96 ÷ 6 = 16 patients", "[P1]"),
                ("3. Sum specialist diets: 40 + 24 + 16 = 80 patients", "[M1]"),
                ("4. Standard meals: 96 - 80 = 16 patients", "[A1]")
            ],
            "final_answer": "16 patients",
            "pitfall": "Adding denominators instead of using a common denominator of 12 (5/12 + 3/12 + 2/12 = 10/12).",
            "reverse_check": "40 + 24 + 16 + 16 = 96 patients."
        },
        {
            "title": "Question 6 (Level 2 Trust Target Justification)",
            "marks": 4,
            "stem": "A community trust aims for at least <strong>7/10</strong> of all clinical incident reviews to be completed within 14 days.<br>Last month, <strong>185 out of 250</strong> incident reviews were completed within 14 days.<br>The quality manager claims: <em>'We achieved our target fraction with room to spare.'</em><br><br>Is the quality manager correct? Show full step-by-step working and state a clear conclusion.",
            "lines": 5,
            "ans_label": "Conclusion & Comparison =",
            "choice_box": "Yes / No: Actual is _______ vs Target 7/10",
            "step_rows": [
                ("1. Calculate target number of reviews: 7/10 of 250 = (250 ÷ 10) × 7 = 175 reviews", "[M1]"),
                ("2. Or convert actual to percentage/decimal: 185 ÷ 250 = 0.74 (74% vs 70% target)", "[P1]"),
                ("3. Compare actual against target: 185 > 175 (or 74% > 70%)", "[M1]"),
                ("4. Conclude: Yes, the manager is correct; 185 reviews (74%) exceeds the 7/10 target of 175 reviews (70%) by 10 reviews.", "[A1]")
            ],
            "final_answer": "Yes, correct (Achieved 185 reviews / 74% vs target of 175 reviews / 70%)",
            "pitfall": "Ticking 'Yes' without showing numerical values for both the target and actual performance.",
            "reverse_check": "185/250 = 37/50 = 74/100 = 0.74 > 0.70."
        }
    ),

    # 2. DECIMALS
    make_maths_topic(
        "decimals",
        "Decimals",
        "E3.5 • L1.10 • L2.10",
        "Align numbers strictly by the decimal point when adding or subtracting. When dividing by a decimal, multiply both numbers by 10, 100, or 1,000 so the divisor becomes a whole number.",
        {
            "title": "Question 1 (Level 1 Decimal Addition)",
            "marks": 2,
            "stem": "Work out: <strong>48.65 + 7.9 + 134.08</strong> without a calculator.",
            "lines": 3,
            "ans_label": "Sum =",
            "choice_box": "____________________",
            "step_rows": [
                ("1. Align decimal points vertically with trailing placeholder zero: 48.65 + 07.90 + 134.08", "[M1]"),
                ("2. Accurate column addition: 190.63", "[A1]")
            ],
            "final_answer": "190.63",
            "pitfall": "Misaligning 7.9 into the hundredths column as 0.79 or 7.09.",
            "reverse_check": "190.63 - 134.08 - 7.90 = 48.65."
        },
        {
            "title": "Question 2 (Level 2 Decimal Division)",
            "marks": 2,
            "stem": "Calculate: <strong>14.7 ÷ 0.03</strong> without a calculator.",
            "lines": 3,
            "ans_label": "Quotient =",
            "choice_box": "____________________",
            "step_rows": [
                ("1. Multiply dividend and divisor by 100 to clear the decimal divisor: 1,470 ÷ 3", "[M1]"),
                ("2. Compute 1,470 ÷ 3 = 490", "[A1]")
            ],
            "final_answer": "490",
            "pitfall": "Dividing 14.7 by 3 to get 4.9 without shifting the decimal point two places.",
            "reverse_check": "490 × 0.03 = 14.7."
        },
        {
            "title": "Question 3 (Level 1 Medical Dosage Administration)",
            "marks": 3,
            "stem": "A nurse administers liquid analgesic at a dosage of <strong>3.75 ml</strong> per patient.<br>The medication bottle contains <strong>90 ml</strong>.<br><br>How many full patient doses are contained in the bottle?",
            "lines": 4,
            "ans_label": "Full doses =",
            "choice_box": "_____________ doses",
            "step_rows": [
                ("1. Set up division: 90 ÷ 3.75", "[M1]"),
                ("2. Multiply both by 100 to divide whole numbers: 9,000 ÷ 375", "[P1]"),
                ("3. Evaluate: 9,000 ÷ 375 = 24 doses", "[A1]")
            ],
            "final_answer": "24 doses",
            "pitfall": "Multiplying 90 × 3.75 (= 337.5) instead of dividing total bottle volume by single dose volume.",
            "reverse_check": "24 × 3.75 ml = 90 ml."
        },
        {
            "title": "Question 4 (Level 2 Fuel Consumption & Cost)",
            "marks": 3,
            "stem": "A community health visitor travels <strong>348.5 miles</strong> across a rural district.<br>Her hybrid car consumes <strong>0.082 litres</strong> of petrol per mile, and petrol costs <strong>£1.45 per litre</strong>.<br><br>Work out the total fuel cost for the trip. Give your answer to the nearest penny.",
            "lines": 4,
            "ans_label": "Total Fuel Cost =",
            "choice_box": "£ ____________________",
            "step_rows": [
                ("1. Calculate total fuel used: 348.5 × 0.082 = 28.577 litres", "[M1]"),
                ("2. Multiply by fuel price: 28.577 × £1.45 = £41.43665", "[P1]"),
                ("3. Round to 2 decimal places (nearest penny): £41.44", "[A1]")
            ],
            "final_answer": "£41.44",
            "pitfall": "Prematurely rounding 28.577 litres to 28.6 litres before multiplying by £1.45 (which gives £41.47).",
            "reverse_check": "£41.44 ÷ £1.45 ≈ 28.58 L; 28.58 ÷ 348.5 ≈ 0.082 L/mile."
        },
        {
            "title": "Question 5 (Level 2 Chemical Water Purification)",
            "marks": 4,
            "stem": "A hydrotherapy pool contains <strong>45,000 litres</strong> of water.<br>Safety regulations require adding <strong>0.0035 litres</strong> of sanitising concentrate for every <strong>100 litres</strong> of pool water.<br>Sanitising concentrate is sold in <strong>0.5-litre bottles</strong> at <strong>£18.20 per bottle</strong>.<br><br>How much does it cost to purchase enough whole bottles for one complete pool treatment?",
            "lines": 5,
            "ans_label": "Total Cost =",
            "choice_box": "£ ____________________",
            "step_rows": [
                ("1. Find number of 100-litre units: 45,000 ÷ 100 = 450 units", "[P1]"),
                ("2. Calculate required concentrate: 450 × 0.0035 = 1.575 litres", "[M1]"),
                ("3. Find bottles needed: 1.575 ÷ 0.5 = 3.15 bottles → round UP to 4 whole bottles", "[P1]"),
                ("4. Total cost: 4 × £18.20 = £72.80", "[A1]")
            ],
            "final_answer": "£72.80",
            "pitfall": "Multiplying 3.15 × £18.20 = £57.33, forgetting that bottles can only be bought as whole units.",
            "reverse_check": "3 bottles = 1.5 L (short by 0.075 L). 4 bottles = 2.0 L at 4 × £18.20 = £72.80."
        },
        {
            "title": "Question 6 (Level 2 Precision Tolerance Evaluation)",
            "marks": 4,
            "stem": "An orthopaedic implant pin must have a target diameter of <strong>4.50 mm</strong> with an allowable tolerance of <strong>±0.04 mm</strong> (acceptable between 4.46 mm and 4.54 mm inclusive).<br>A batch inspector tests 4 sample pins: <strong>4.45 mm, 4.48 mm, 4.53 mm, 4.55 mm</strong>.<br>The quality controller claims: <em>'At least 75% of the inspected pins are within the safety tolerance.'</em><br><br>Is the quality controller's claim correct? Show your evaluation of each pin and state a clear conclusion.",
            "lines": 5,
            "ans_label": "Decision & Pass Rate =",
            "choice_box": "Correct / Incorrect: Pass rate is _____ %",
            "step_rows": [
                ("1. Establish tolerance bounds: 4.50 - 0.04 = 4.46 mm to 4.50 + 0.04 = 4.54 mm", "[P1]"),
                ("2. Test pins: 4.45 mm (FAIL, < 4.46); 4.48 mm (PASS); 4.53 mm (PASS); 4.55 mm (FAIL, > 4.54)", "[M1]"),
                ("3. Calculate pass percentage: 2 out of 4 pass = 2/4 = 50%", "[P1]"),
                ("4. Conclude: Incorrect; only 50% (2 out of 4) of the pins pass, which is below the 75% claim.", "[A1]")
            ],
            "final_answer": "Incorrect (Only 50% / 2 of 4 pins pass, which is less than 75%)",
            "pitfall": "Assuming 4.45 mm passes because it rounds to 4.5 mm.",
            "reverse_check": "2 ÷ 4 × 100 = 50% < 75%."
        }
    ),

    # 3. PERCENTAGES
    make_maths_topic(
        "percentages",
        "Percentages",
        "L1.12 • L2.11 • L2.16",
        "To find a percentage of an amount: divide by 100 and multiply by the percentage (or use a decimal multiplier). Percentage change = (Difference ÷ Original Value) × 100.",
        {
            "title": "Question 1 (Level 1 Percentage of an Amount)",
            "marks": 2,
            "stem": "Calculate <strong>15% of £3,600</strong> without a calculator.",
            "lines": 3,
            "ans_label": "Amount =",
            "choice_box": "£ ____________________",
            "step_rows": [
                ("1. Find 10% (£3,600 ÷ 10 = £360) and 5% (half of £360 = £180)", "[M1]"),
                ("2. Add 10% + 5%: £360 + £180 = £540.00", "[A1]")
            ],
            "final_answer": "£540.00",
            "pitfall": "Dividing £3,600 by 15 instead of finding 15 hundredths.",
            "reverse_check": "£540 ÷ £3,600 = 0.15 = 15%."
        },
        {
            "title": "Question 2 (Level 2 Reverse Percentage / Pre-VAT Price)",
            "marks": 2,
            "stem": "An electronic medical monitor costs <strong>£756.00 including 20% VAT</strong>.<br>Work out the original price of the monitor before VAT was added.",
            "lines": 3,
            "ans_label": "Pre-VAT price =",
            "choice_box": "£ ____________________",
            "step_rows": [
                ("1. Recognise £756 represents 120% of the pre-VAT price: divide £756 by 1.20 (or ÷ 120 × 100)", "[M1]"),
                ("2. Evaluate: £756 ÷ 1.20 = £630.00", "[A1]")
            ],
            "final_answer": "£630.00",
            "pitfall": "Finding 20% of £756 (£151.20) and subtracting it to get £604.80 — the classic reverse percentage trap!",
            "reverse_check": "£630.00 + 20% (£126.00) = £756.00."
        },
        {
            "title": "Question 3 (Level 1 NHS Pay Award Increase)",
            "marks": 3,
            "stem": "A healthcare support worker earns a gross annual salary of <strong>£24,500</strong>.<br>The annual pay settlement awards a <strong>5.5% pay increase</strong>.<br><br>Work out the worker's new gross annual salary.",
            "lines": 4,
            "ans_label": "New annual salary =",
            "choice_box": "£ ____________________",
            "step_rows": [
                ("1. Calculate 5.5% increase: £24,500 × 0.055 = £1,347.50", "[M1]"),
                ("2. Add increase to original salary: £24,500 + £1,347.50", "[P1]"),
                ("3. State new salary: £25,847.50", "[A1]")
            ],
            "final_answer": "£25,847.50",
            "pitfall": "Multiplying by 0.55 (55%) instead of 0.055 (5.5%).",
            "reverse_check": "£24,500 × 1.055 = £25,847.50."
        },
        {
            "title": "Question 4 (Level 2 Percentage Decrease in Waiting Times)",
            "marks": 3,
            "stem": "Following a clinical pathway review, an outpatient clinic reduces its average patient waiting time from <strong>45 minutes</strong> down to <strong>36 minutes</strong>.<br><br>Calculate the percentage decrease in waiting time.",
            "lines": 4,
            "ans_label": "Percentage decrease =",
            "choice_box": "_____________ %",
            "step_rows": [
                ("1. Calculate time reduction: 45 - 36 = 9 minutes", "[M1]"),
                ("2. Divide reduction by ORIGINAL time: 9 ÷ 45 = 0.20", "[P1]"),
                ("3. Convert to percentage: 0.20 × 100 = 20%", "[A1]")
            ],
            "final_answer": "20%",
            "pitfall": "Dividing by the new time (9 ÷ 36 = 25%) instead of the original 45 minutes.",
            "reverse_check": "45 mins - 20% (9 mins) = 36 mins."
        },
        {
            "title": "Question 5 (Level 2 Medical Equipment Lease vs Buy)",
            "marks": 4,
            "stem": "A diagnostic ultrasound machine has a list price of <strong>£32,000</strong>.<br>The supplier offers two purchase options:<br>• <strong>Option A (Outright Buy):</strong> 15% promotional discount off list price, plus £450 delivery.<br>• <strong>Option B (2-Year Lease):</strong> Deposit of £4,000, followed by 24 monthly payments of £1,050.<br><br>Which option is cheaper, and by how much?",
            "lines": 5,
            "ans_label": "Cheaper Option & Saving =",
            "choice_box": "Option _____ is cheaper by £ ____________",
            "step_rows": [
                ("1. Option A: £32,000 × 0.85 = £27,200; plus £450 delivery = £27,650", "[P1]"),
                ("2. Option B: £4,000 + (24 × £1,050) = £4,000 + £25,200 = £29,200", "[P1]"),
                ("3. Calculate difference: £29,200 - £27,650 = £1,550", "[M1]"),
                ("4. Conclude: Option A is cheaper by £1,550.00", "[A1]")
            ],
            "final_answer": "Option A is cheaper by £1,550.00",
            "pitfall": "Omitting the £4,000 deposit in Option B.",
            "reverse_check": "£27,650 + £1,550 = £29,200."
        },
        {
            "title": "Question 6 (Level 2 Audit Target Justification)",
            "marks": 4,
            "stem": "An NHS Trust targets reducing patient complaints by at least <strong>12%</strong> over one year.<br>• In 2025, the trust recorded <strong>850 complaints</strong>.<br>• In 2026, the trust recorded <strong>740 complaints</strong>.<br>The customer service lead reports: <em>'We achieved our target reduction of at least 12%.'</em><br><br>Is the report correct? Show your calculations clearly and state a definitive conclusion.",
            "lines": 5,
            "ans_label": "Conclusion & Reduction Rate =",
            "choice_box": "Correct / Incorrect: Reduction was _____ %",
            "step_rows": [
                ("1. Actual reduction in complaints: 850 - 740 = 110 complaints", "[P1]"),
                ("2. Required 12% reduction: 850 × 0.12 = 102 complaints (or max 748 complaints)", "[M1]"),
                ("3. Actual percentage reduction: (110 ÷ 850) × 100 = 12.94%", "[P1]"),
                ("4. Conclude: Correct; the trust achieved a 12.94% reduction (110 complaints), exceeding the 12% (102 complaints) target.", "[A1]")
            ],
            "final_answer": "Correct (Achieved 12.94% / 110 reduction vs 12% / 102 target)",
            "pitfall": "Dividing 110 by 740 (14.86%) instead of dividing by the original 2025 figure of 850.",
            "reverse_check": "850 - 102 = 748; actual 740 is 8 complaints better than target."
        }
    ),

    # 4. PROPORTION
    make_maths_topic(
        "proportion",
        "Direct & Inverse Proportion",
        "L1.11 • L2.11",
        "For Direct Proportion (recipes, unit costs): divide to find 1 unit, then multiply up. For Inverse Proportion (workers vs time): multiply workers × time to find total person-hours, then divide by the new number of workers.",
        {
            "title": "Question 1 (Level 1 Unitary Direct Proportion)",
            "marks": 2,
            "stem": "A clinic purchases <strong>8 boxes</strong> of sterile dressings for <strong>£116.00</strong>.<br>Work out the cost of purchasing <strong>15 boxes</strong> of the same dressings.",
            "lines": 3,
            "ans_label": "Cost of 15 boxes =",
            "choice_box": "£ ____________________",
            "step_rows": [
                ("1. Cost of 1 box: £116.00 ÷ 8 = £14.50", "[M1]"),
                ("2. Cost of 15 boxes: 15 × £14.50 = £217.50", "[A1]")
            ],
            "final_answer": "£217.50",
            "pitfall": "Dividing 8 by 116 instead of dividing price by quantity.",
            "reverse_check": "£217.50 ÷ 15 = £14.50; £14.50 × 8 = £116.00."
        },
        {
            "title": "Question 2 (Level 2 Inverse Proportion Workforce Time)",
            "marks": 2,
            "stem": "It takes <strong>4 maintenance painters 9 hours</strong> to repaint a hospital corridor.<br>How long would it take <strong>6 painters</strong> working at the same rate to repaint the corridor?",
            "lines": 3,
            "ans_label": "Time for 6 painters =",
            "choice_box": "_____________ hours",
            "step_rows": [
                ("1. Calculate total person-hours required: 4 painters × 9 hours = 36 person-hours", "[M1]"),
                ("2. Divide by 6 painters: 36 ÷ 6 = 6 hours", "[A1]")
            ],
            "final_answer": "6 hours",
            "pitfall": "Using direct proportion (9 ÷ 4 × 6 = 13.5 hours) — more painters must take LESS time!",
            "reverse_check": "6 painters × 6 hours = 36 person-hours = 4 × 9."
        },
        {
            "title": "Question 3 (Level 1 Catering Recipe Scaling)",
            "marks": 3,
            "stem": "A care home kitchen recipe for <strong>12 portions</strong> of cottage pie requires <strong>900 g</strong> of minced beef and <strong>1.5 kg</strong> of potatoes.<br><br>Calculate the weight of minced beef (in grams) and potatoes (in kg) required to make <strong>30 portions</strong>.",
            "lines": 4,
            "ans_label": "Beef & Potatoes =",
            "choice_box": "Beef: _______ g | Potatoes: _______ kg",
            "step_rows": [
                ("1. Scaling multiplier: 30 ÷ 12 = 2.5 (or find 1 portion: 75 g beef and 0.125 kg potatoes)", "[M1]"),
                ("2. Minced beef for 30 portions: 900 g × 2.5 = 2,250 g", "[A1]"),
                ("3. Potatoes for 30 portions: 1.5 kg × 2.5 = 3.75 kg", "[A1]")
            ],
            "final_answer": "Beef: 2,250 g | Potatoes: 3.75 kg",
            "pitfall": "Doubling for 24 portions and adding a fixed amount instead of scaling by 2.5.",
            "reverse_check": "2,250 ÷ 30 = 75 g/portion; 75 × 12 = 900 g."
        },
        {
            "title": "Question 4 (Level 2 Fleet Fuel Consumption Rate)",
            "marks": 3,
            "stem": "An ambulance patient transport van uses <strong>22.5 litres</strong> of diesel to travel <strong>270 miles</strong>.<br>Diesel costs <strong>£1.48 per litre</strong>.<br><br>Calculate the fuel cost for the van to travel <strong>420 miles</strong> at the same consumption rate.",
            "lines": 4,
            "ans_label": "Fuel cost =",
            "choice_box": "£ ____________________",
            "step_rows": [
                ("1. Calculate miles per litre: 270 ÷ 22.5 = 12 miles per litre", "[M1]"),
                ("2. Calculate litres needed for 420 miles: 420 ÷ 12 = 35 litres", "[P1]"),
                ("3. Multiply by diesel price: 35 × £1.48 = £51.80", "[A1]")
            ],
            "final_answer": "£51.80",
            "pitfall": "Rounding intermediate litre per mile figures (0.0833) instead of using exact 12 miles per litre.",
            "reverse_check": "£51.80 ÷ £1.48 = 35 L; 35 × 12 = 420 miles."
        },
        {
            "title": "Question 5 (Level 2 Limiting Ingredient Bakery Production)",
            "marks": 4,
            "stem": "A commercial bakery recipe for <strong>20 protein flapjacks</strong> uses:<br>• <strong>400 g</strong> rolled oats<br>• <strong>250 g</strong> honey<br>• <strong>160 g</strong> butter<br>The kitchen store has <strong>3.6 kg of oats</strong>, <strong>2.0 kg of honey</strong>, and <strong>1.5 kg of butter</strong>.<br><br>What is the maximum number of flapjacks the bakery can make from this stock?",
            "lines": 5,
            "ans_label": "Maximum flapjacks =",
            "choice_box": "_____________ flapjacks",
            "step_rows": [
                ("1. Convert stock to grams: 3,600 g oats, 2,000 g honey, 1,500 g butter", "[P1]"),
                ("2. Find batches of 20 possible per ingredient: Oats = 3,600 ÷ 400 = 9 batches; Honey = 2,000 ÷ 250 = 8 batches; Butter = 1,500 ÷ 160 = 9.375 batches", "[M1]"),
                ("3. Identify limiting ingredient: Honey limits production to 8 batches of 20", "[P1]"),
                ("4. Calculate max flapjacks: 8 × 20 = 160 flapjacks", "[A1]")
            ],
            "final_answer": "160 flapjacks (limited by 2,000 g of honey)",
            "pitfall": "Picking the highest batch count (9.375 × 20 = 187) instead of the lowest limiting ingredient (honey = 160).",
            "reverse_check": "160 flapjacks (8 batches) uses 3,200 g oats, 2,000 g honey (all used), and 1,280 g butter."
        },
        {
            "title": "Question 6 (Level 2 Warehouse Unloading Deadline Decision)",
            "marks": 4,
            "stem": "It takes <strong>5 warehouse operatives 4 hours and 48 minutes</strong> to unpack and label a clinical equipment delivery.<br>Today, the delivery arrives at <strong>09:30</strong> and must be completely unpacked by <strong>12:30</strong>.<br>The supervisor assigns <strong>8 warehouse operatives</strong> (all working at the normal rate).<br><br>Will the 8 operatives finish unpacking the delivery by <strong>12:30</strong>? Show your working clearly.",
            "lines": 5,
            "ans_label": "Decision & Finish Time =",
            "choice_box": "Yes / No: Takes _______ hours (Finishes at _______)",
            "step_rows": [
                ("1. Convert 4 hours 48 minutes to decimal hours (4 + 48/60 = 4.8 hours) or minutes (288 mins)", "[P1]"),
                ("2. Calculate total person-hours: 5 operatives × 4.8 hours = 24 person-hours (or 1,440 person-minutes)", "[M1]"),
                ("3. Divide by 8 operatives: 24 ÷ 8 = 3.0 hours (180 minutes)", "[P1]"),
                ("4. Conclude: 09:30 + 3 hours = 12:30. Yes, the 8 operatives will finish at exactly 12:30.", "[A1]")
            ],
            "final_answer": "Yes (Takes 3 hours, finishing at exactly 12:30)",
            "pitfall": "Writing 4 hours 48 minutes as 4.48 hours instead of 4.8 hours.",
            "reverse_check": "8 operatives × 3 hours = 24 person-hours = 5 × 4.8 hours."
        }
    ),

    # 5. FORMULAS
    make_maths_topic(
        "formulas",
        "Algebra, Formulas & Substitution",
        "L1.13 • L2.13 • L2.14",
        "Replace letters with their given numerical values in brackets, then follow BIDMAS (Brackets, Indices, Multiplication/Division, Addition/Subtraction). To find an unknown input, use inverse operations in reverse order.",
        {
            "title": "Question 1 (Level 1 Linear Formula Substitution)",
            "marks": 2,
            "stem": "A medical courier firm calculates delivery charges (£) using the formula:<br><strong>C = 18.50 + 0.45m</strong>, where <strong>m</strong> is the distance in miles.<br>Calculate the delivery charge for a journey of <strong>40 miles</strong>.",
            "lines": 3,
            "ans_label": "Delivery Charge C =",
            "choice_box": "£ ____________________",
            "step_rows": [
                ("1. Substitute m = 40 and multiply first: 0.45 × 40 = £18.00", "[M1]"),
                ("2. Add fixed fee: £18.50 + £18.00 = £36.50", "[A1]")
            ],
            "final_answer": "£36.50",
            "pitfall": "Adding 18.50 + 0.45 first (18.95) and multiplying the sum by 40.",
            "reverse_check": "(£36.50 - £18.50) ÷ 0.45 = £18.00 ÷ 0.45 = 40 miles."
        },
        {
            "title": "Question 2 (Level 2 Rearranging / Inverse Formula)",
            "marks": 2,
            "stem": "An industrial oven heats up according to the formula <strong>T = 22 + 14m</strong>, where <strong>T</strong> is the temperature in °C and <strong>m</strong> is the time in minutes.<br>How many minutes does it take for the oven to reach <strong>204°C</strong>?",
            "lines": 3,
            "ans_label": "Time m =",
            "choice_box": "_____________ minutes",
            "step_rows": [
                ("1. Subtract starting temperature: 204 - 22 = 182", "[M1]"),
                ("2. Divide by heating rate: 182 ÷ 14 = 13 minutes", "[A1]")
            ],
            "final_answer": "13 minutes",
            "pitfall": "Dividing 204 by 14 before subtracting 22.",
            "reverse_check": "22 + (14 × 13) = 22 + 182 = 204°C."
        },
        {
            "title": "Question 3 (Level 1 Paediatric Clinical Dose Rule)",
            "marks": 3,
            "stem": "A hospital pharmacist uses Clark's Rule to calculate a child's medication dose:<br><strong>Child Dose (mg) = (Child Weight in lbs × Adult Dose in mg) ÷ 150</strong><br><br>Calculate the child dose for a child weighing <strong>45 lbs</strong> when the adult dose is <strong>500 mg</strong>.",
            "lines": 4,
            "ans_label": "Child Dose =",
            "choice_box": "_____________ mg",
            "step_rows": [
                ("1. Substitute values into numerator: 45 × 500 = 22,500", "[M1]"),
                ("2. Divide by 150: 22,500 ÷ 150", "[P1]"),
                ("3. Evaluate: 150 mg", "[A1]")
            ],
            "final_answer": "150 mg",
            "pitfall": "Dividing 150 by 45 instead of following numerator ÷ 150.",
            "reverse_check": "(150 × 150) ÷ 500 = 22,500 ÷ 500 = 45 lbs."
        },
        {
            "title": "Question 4 (Level 2 Stopping Distance Formula with Squaring)",
            "marks": 3,
            "stem": "The stopping distance <strong>d</strong> (in feet) of a vehicle travelling at speed <strong>v</strong> (in mph) is modelled by the formula:<br><strong>d = v + (v² ÷ 20)</strong><br><br>Calculate the stopping distance when a driver is travelling at <strong>30 mph</strong>.",
            "lines": 4,
            "ans_label": "Stopping distance d =",
            "choice_box": "_____________ feet",
            "step_rows": [
                ("1. Calculate v²: 30² = 30 × 30 = 900", "[M1]"),
                ("2. Divide by 20: 900 ÷ 20 = 45", "[P1]"),
                ("3. Add v (30): 30 + 45 = 75 feet", "[A1]")
            ],
            "final_answer": "75 feet",
            "pitfall": "Calculating 30² as 30 × 2 = 60 instead of 30 × 30 = 900.",
            "reverse_check": "30 + (900 ÷ 20) = 30 + 45 = 75 feet."
        },
        {
            "title": "Question 5 (Level 2 Wind Turbine Power Output Formula)",
            "marks": 4,
            "stem": "An energy engineer calculates the electrical power <strong>P</strong> (in kilowatts, kW) generated by a wind turbine using the formula:<br><strong>P = 0.0006 × A × v³</strong><br>where <strong>A = 400 m²</strong> is the blade sweep area and <strong>v</strong> is the wind speed in m/s.<br><br>Calculate the power generated when the wind speed is <strong>10 m/s</strong>, and find the value of electricity produced in <strong>5 hours</strong> if electricity is worth <strong>£0.25 per kWh</strong>.",
            "lines": 5,
            "ans_label": "5-Hour Electricity Value =",
            "choice_box": "£ ____________________",
            "step_rows": [
                ("1. Evaluate v³: 10³ = 10 × 10 × 10 = 1,000", "[P1]"),
                ("2. Substitute into formula: P = 0.0006 × 400 × 1,000 = 240 kW", "[M1]"),
                ("3. Energy in 5 hours: 240 kW × 5 hours = 1,200 kWh", "[P1]"),
                ("4. Value at £0.25/kWh: 1,200 × £0.25 = £300.00", "[A1]")
            ],
            "final_answer": "£300.00 (Power = 240 kW; Energy = 1,200 kWh)",
            "pitfall": "Evaluating 10³ as 30 instead of 1,000.",
            "reverse_check": "£300 ÷ £0.25 = 1,200 kWh; 1,200 ÷ 5 = 240 kW."
        },
        {
            "title": "Question 6 (Level 2 Crane Safe Working Load Radius Evaluation)",
            "marks": 4,
            "stem": "The maximum safe load <strong>L</strong> (in tonnes) for a mobile crane at a horizontal boom radius <strong>r</strong> (in metres) is given by:<br><strong>L = (180 ÷ r) - 4.5</strong><br>A site manager needs to lift a prefabricated modular clinic unit weighing <strong>10.2 tonnes</strong> at a horizontal radius of <strong>12 metres</strong>.<br><br>Is it safe for the crane to lift this modular unit at a 12-metre radius? Show your substitution and state a clear conclusion.",
            "lines": 5,
            "ans_label": "Decision & Max Load =",
            "choice_box": "Yes / No: Max safe load L = _______ tonnes",
            "step_rows": [
                ("1. Substitute r = 12 into formula: L = (180 ÷ 12) - 4.5", "[P1]"),
                ("2. Perform division first: 180 ÷ 12 = 15", "[M1]"),
                ("3. Subtract 4.5: L = 15 - 4.5 = 10.5 tonnes maximum safe load", "[P1]"),
                ("4. Compare and conclude: 10.2 tonnes ≤ 10.5 tonnes. Yes, it is safe to lift the unit (with 0.3 tonnes margin).", "[A1]")
            ],
            "final_answer": "Yes, safe (Max safe load is 10.5 tonnes, which exceeds the 10.2-tonne unit by 0.3 tonnes)",
            "pitfall": "Subtracting 12 - 4.5 = 7.5 before dividing 180.",
            "reverse_check": "(10.5 + 4.5) × 12 = 15 × 12 = 180."
        }
    ),

    # 6. MONEY
    make_maths_topic(
        "money",
        "Money, Invoicing & Payroll",
        "L1.14 • L2.15 • L2.16",
        "Always format final money answers to 2 decimal places (e.g. £14.50). Net Pay = Gross Pay − Total Deductions. On invoices, deduct trade discounts before calculating 20% VAT.",
        {
            "title": "Question 1 (Level 1 Payslip Net Pay Reconciliation)",
            "marks": 2,
            "stem": "A dental receptionist earns a monthly gross pay of <strong>£1,945.00</strong>.<br>Her monthly deductions are: Income Tax <strong>£158.40</strong>, National Insurance <strong>£96.80</strong>, and Pension <strong>£97.25</strong>.<br>Calculate her monthly net take-home pay.",
            "lines": 3,
            "ans_label": "Net Take-Home Pay =",
            "choice_box": "£ ____________________",
            "step_rows": [
                ("1. Sum total deductions: £158.40 + £96.80 + £97.25 = £352.45", "[M1]"),
                ("2. Subtract from gross pay: £1,945.00 - £352.45 = £1,592.55", "[A1]")
            ],
            "final_answer": "£1,592.55",
            "pitfall": "Adding deductions onto gross pay instead of subtracting.",
            "reverse_check": "£1,592.55 + £352.45 = £1,945.00."
        },
        {
            "title": "Question 2 (Level 2 Weekly Wage with Overtime)",
            "marks": 2,
            "stem": "A medical laboratory technician works <strong>37.5 basic hours</strong> at <strong>£14.00 per hour</strong>, plus <strong>8 overtime hours</strong> paid at <strong>time-and-a-half (1.5×)</strong>.<br>Calculate the technician's total gross weekly pay.",
            "lines": 3,
            "ans_label": "Total Gross Pay =",
            "choice_box": "£ ____________________",
            "step_rows": [
                ("1. Basic pay = 37.5 × £14.00 = £525.00; Overtime rate = £14 × 1.5 = £21.00/hr → Overtime pay = 8 × £21 = £168.00", "[M1]"),
                ("2. Total gross pay = £525.00 + £168.00 = £693.00", "[A1]")
            ],
            "final_answer": "£693.00",
            "pitfall": "Paying overtime at standard £14.00/hr instead of £21.00/hr.",
            "reverse_check": "(37.5 + 12 equivalent hrs) × £14 = 49.5 × £14 = £693.00."
        },
        {
            "title": "Question 3 (Level 1 Commercial Equipment Invoice with VAT)",
            "marks": 3,
            "stem": "A care home orders <strong>6 adjustable profiling beds</strong> at <strong>£420.00 each</strong> and <strong>6 pressure-relief mattresses</strong> at <strong>£130.00 each</strong>.<br>Standard UK VAT at <strong>20%</strong> is added to the subtotal.<br><br>Calculate the total invoice amount payable.",
            "lines": 4,
            "ans_label": "Total Invoice Payable =",
            "choice_box": "£ ____________________",
            "step_rows": [
                ("1. Calculate net subtotal: (6 × £420) + (6 × £130) = £2,520 + £780 = £3,300.00", "[M1]"),
                ("2. Calculate 20% VAT: £3,300.00 × 0.20 = £660.00", "[P1]"),
                ("3. Add VAT to subtotal: £3,300.00 + £660.00 = £3,960.00", "[A1]")
            ],
            "final_answer": "£3,960.00",
            "pitfall": "Calculating VAT on only 1 bed and 1 mattress instead of all 6.",
            "reverse_check": "£3,960.00 ÷ 1.20 = £3,300.00; £3,300 ÷ 6 = £550 per set (£420 + £130)."
        },
        {
            "title": "Question 4 (Level 2 Trade Discount Followed by VAT)",
            "marks": 3,
            "stem": "An electrical wholesaler quotes a list price of <strong>£1,250.00</strong> (excluding VAT) for LED hospital lighting panels.<br>The contractor receives a <strong>12% trade discount</strong> off the list price, and then <strong>20% VAT</strong> is added to the discounted subtotal.<br><br>Calculate the final total payable including VAT.",
            "lines": 4,
            "ans_label": "Final Total Payable =",
            "choice_box": "£ ____________________",
            "step_rows": [
                ("1. Deduct 12% trade discount: £1,250 × 0.12 = £150 discount → Net price = £1,250 - £150 = £1,100.00", "[M1]"),
                ("2. Calculate 20% VAT on discounted net price: £1,100.00 × 0.20 = £220.00", "[P1]"),
                ("3. Final total payable: £1,100.00 + £220.00 = £1,320.00", "[A1]")
            ],
            "final_answer": "£1,320.00",
            "pitfall": "Adding 8% (+20% - 12% = +8%) to £1,250 to get £1,350 — percentages apply sequentially, not additively!",
            "reverse_check": "£1,250 × 0.88 × 1.20 = £1,320.00."
        },
        {
            "title": "Question 5 (Level 2 Annual Tax Threshold & Take-Home Pay)",
            "marks": 4,
            "stem": "A senior physiotherapist earns a gross annual salary of <strong>£38,570</strong>.<br>• The first <strong>£12,570</strong> of income is a tax-free Personal Allowance (0% tax).<br>• Income Tax is charged at <strong>20%</strong> on all earnings above £12,570.<br>• In addition, she pays <strong>£1,980</strong> per year in National Insurance and <strong>6% of her total gross salary</strong> into her workplace pension.<br><br>Calculate her annual net take-home pay.",
            "lines": 5,
            "ans_label": "Annual Net Pay =",
            "choice_box": "£ ____________________",
            "step_rows": [
                ("1. Taxable income: £38,570 - £12,570 = £26,000 → Income Tax (20%) = £26,000 × 0.20 = £5,200.00", "[P1]"),
                ("2. Pension contribution (6% of total £38,570): £38,570 × 0.06 = £2,314.20", "[P1]"),
                ("3. Total annual deductions: £5,200.00 (Tax) + £1,980.00 (NI) + £2,314.20 (Pension) = £9,494.20", "[M1]"),
                ("4. Annual Net Pay: £38,570.00 - £9,494.20 = £29,075.80", "[A1]")
            ],
            "final_answer": "£29,075.80",
            "pitfall": "Charging 20% Income Tax on the entire £38,570 without subtracting the £12,570 tax-free allowance first.",
            "reverse_check": "£29,075.80 + £9,494.20 = £38,570.00."
        },
        {
            "title": "Question 6 (Level 2 Clinic Refurbishment Quote Comparison)",
            "marks": 4,
            "stem": "A GP practice manager receives two quotes to repaint the reception area:<br>• <strong>Contractor A:</strong> 32 hours of labour at <strong>£28.00/hour</strong>, plus <strong>£245.00</strong> for paint. (Contractor A is not VAT-registered, so <strong>no VAT</strong> is charged).<br>• <strong>Contractor B:</strong> Fixed labour &amp; materials package of <strong>£1,050.00</strong> with a <strong>10% promotional discount</strong>, <strong>plus 20% VAT</strong> on the discounted price.<br><br>Which contractor is cheaper, and by how much?",
            "lines": 5,
            "ans_label": "Cheaper Contractor & Saving =",
            "choice_box": "Contractor _____ is cheaper by £ ____________",
            "step_rows": [
                ("1. Contractor A total: (32 × £28.00) + £245.00 = £896.00 + £245.00 = £1,141.00", "[P1]"),
                ("2. Contractor B discounted net: £1,050.00 × 0.90 = £945.00", "[P1]"),
                ("3. Contractor B with 20% VAT: £945.00 × 1.20 = £1,134.00", "[M1]"),
                ("4. Compare and conclude: Contractor B (£1,134.00) is cheaper than Contractor A (£1,141.00) by £7.00.", "[A1]")
            ],
            "final_answer": "Contractor B is cheaper by £7.00 (£1,134.00 vs £1,141.00)",
            "pitfall": "Forgetting to add 20% VAT to Contractor B after taking off the 10% discount.",
            "reverse_check": "£1,141.00 - £1,134.00 = £7.00."
        }
    ),

    # 7. BEST BUYS
    make_maths_topic(
        "best-buys",
        "Best Buys & Unit Pricing",
        "L1.15 • L2.17",
        "To find the unit price: divide Cost (£) by Quantity (weight, volume, or count). Always convert quantities to the same unit (e.g. grams or litres) before comparing.",
        {
            "title": "Question 1 (Level 1 Unit Price per Litre)",
            "marks": 2,
            "stem": "A catering supplier sells sunflower oil in two drums:<br>• <strong>Drum A:</strong> 5 litres for <strong>£11.50</strong><br>• <strong>Drum B:</strong> 8 litres for <strong>£17.60</strong><br>Calculate the cost per litre for each drum and state which is better value.",
            "lines": 3,
            "ans_label": "Better Value Drum =",
            "choice_box": "Drum _____ (A: £_____/L vs B: £_____/L)",
            "step_rows": [
                ("1. Drum A = £11.50 ÷ 5 = £2.30/L; Drum B = £17.60 ÷ 8 = £2.20/L", "[M1]"),
                ("2. Conclude: Drum B is better value (£2.20/L is 10p per litre cheaper than £2.30/L)", "[A1]")
            ],
            "final_answer": "Drum B (£2.20/L vs Drum A £2.30/L)",
            "pitfall": "Choosing Drum A because £11.50 is a lower total ticket price than £17.60.",
            "reverse_check": "8 × £2.20 = £17.60; 5 × £2.30 = £11.50."
        },
        {
            "title": "Question 2 (Level 2 Mixed Metric Units Best Buy)",
            "marks": 2,
            "stem": "Hand sanitiser gel is sold in two dispenser sizes:<br>• <strong>Standard Pump:</strong> 400 ml for <strong>£3.20</strong><br>• <strong>Bulk Refill:</strong> 1.5 litres for <strong>£11.25</strong><br>Work out the cost per 100 ml for both options to determine the best buy.",
            "lines": 3,
            "ans_label": "Best Buy =",
            "choice_box": "____________________ (£_____ vs £_____ per 100ml)",
            "step_rows": [
                ("1. Standard (400 ml = 4 × 100 ml): £3.20 ÷ 4 = £0.80 (80p) per 100 ml. Bulk (1.5 L = 15 × 100 ml): £11.25 ÷ 15 = £0.75 (75p) per 100 ml", "[M1]"),
                ("2. Conclude: Bulk Refill (1.5 L) is better value at 75p per 100 ml (vs 80p per 100 ml)", "[A1]")
            ],
            "final_answer": "Bulk Refill 1.5 L (75p per 100 ml vs 80p per 100 ml)",
            "pitfall": "Dividing £11.25 by 1.5 without converting 400 ml to 0.4 litres.",
            "reverse_check": "£0.75 × 15 = £11.25; £0.80 × 4 = £3.20."
        },
        {
            "title": "Question 3 (Level 1 Three-Way Pack Size Comparison)",
            "marks": 3,
            "stem": "A care home buys decaffeinated tea bags. Three box sizes are sold:<br>• <strong>Small Box:</strong> 80 tea bags for <strong>£2.40</strong><br>• <strong>Medium Box:</strong> 160 tea bags for <strong>£4.48</strong><br>• <strong>Large Box:</strong> 240 tea bags for <strong>£6.96</strong><br><br>Which box gives the lowest cost per tea bag? Show the cost per bag (in pence) for all three boxes.",
            "lines": 4,
            "ans_label": "Best Value Box =",
            "choice_box": "_____________ Box (Small: ___p, Med: ___p, Large: ___p)",
            "step_rows": [
                ("1. Small: 240p ÷ 80 = 3.0p per bag", "[M1]"),
                ("2. Medium: 448p ÷ 160 = 2.8p per bag; Large: 696p ÷ 240 = 2.9p per bag", "[P1]"),
                ("3. Conclude: The Medium Box (160 bags) is best value at 2.8p per bag", "[A1]")
            ],
            "final_answer": "Medium Box (2.8p per bag vs 2.9p Large and 3.0p Small)",
            "pitfall": "Assuming the 240-bag Large Box is cheapest without checking the arithmetic.",
            "reverse_check": "Scale all to 480 bags: Small = 6 × £2.40 = £14.40; Medium = 3 × £4.48 = £13.44; Large = 2 × £6.96 = £13.92."
        },
        {
            "title": "Question 4 (Level 2 Multi-Buy Promotional Bundle Comparison)",
            "marks": 3,
            "stem": "A hospital ward sister needs to buy <strong>12 boxes</strong> of tissues.<br>• <strong>Chemist A:</strong> Normal price <strong>£1.80 per box</strong>, on a <strong>'3 for the price of 2'</strong> offer.<br>• <strong>Chemist B:</strong> Normal price <strong>£1.60 per box</strong>, on a <strong>'Buy one, get a second half price'</strong> offer.<br><br>Which chemist is cheaper for 12 boxes, and by how much?",
            "lines": 4,
            "ans_label": "Cheaper Chemist & Saving =",
            "choice_box": "Chemist _____ is cheaper by £ ____________",
            "step_rows": [
                ("1. Chemist A (4 groups of 3 = pay for 8 boxes): 8 × £1.80 = £14.40", "[M1]"),
                ("2. Chemist B (6 pairs of 2 at £1.60 + £0.80 = £2.40 per pair): 6 × £2.40 = £14.40", "[P1]"),
                ("3. Wait — let's check: both cost exactly £14.40! State that both chemists cost the exact same (£14.40, difference £0.00)", "[A1]")
            ],
            "final_answer": "Both cost exactly £14.40 (Difference = £0.00 / £1.20 per box at both)",
            "pitfall": "Misinterpreting 'Buy 1 get 2nd half price' as half price on all 12 boxes instead of every second box.",
            "reverse_check": "Chemist A: £3.60 for 3 = £1.20/box. Chemist B: £2.40 for 2 = £1.20/box. 12 × £1.20 = £14.40."
        },
        {
            "title": "Question 5 (Level 2 Printer Toner Cost per 1,000 Pages)",
            "marks": 4,
            "stem": "An NHS administration office compares two laser toner cartridges:<br>• <strong>Standard Cartridge:</strong> Costs <strong>£49.50</strong> and prints <strong>2,200 pages</strong>.<br>• <strong>High-Yield Cartridge:</strong> Costs <strong>£84.00</strong> (with a <strong>10% corporate discount</strong>) and prints <strong>4,000 pages</strong>.<br><br>Calculate the cost per 1,000 pages for each cartridge and state how much money the office saves over <strong>20,000 pages</strong> by choosing the better-value cartridge.",
            "lines": 5,
            "ans_label": "20,000-Page Saving =",
            "choice_box": "Saves £ ____________ using High-Yield",
            "step_rows": [
                ("1. Standard cost for 20,000 pages (or per 1,000): £49.50 ÷ 2.2 = £22.50 per 1,000 pages (× 20 = £450.00)", "[P1]"),
                ("2. High-Yield discounted price: £84.00 × 0.90 = £75.60 for 4,000 pages", "[P1]"),
                ("3. High-Yield cost per 1,000 pages: £75.60 ÷ 4 = £18.90 per 1,000 pages (× 20 = £378.00 for 5 cartridges)", "[M1]"),
                ("4. Saving over 20,000 pages: £450.00 - £378.00 = £72.00", "[A1]")
            ],
            "final_answer": "Saves £72.00 (Standard = £22.50/1,000 pages vs High-Yield = £18.90/1,000 pages)",
            "pitfall": "Forgetting to apply the 10% corporate discount to the High-Yield cartridge.",
            "reverse_check": "(£22.50 - £18.90) × 20 = £3.60 × 20 = £72.00."
        },
        {
            "title": "Question 6 (Level 2 Wholesale Tile Pack Optimisation)",
            "marks": 4,
            "stem": "A facilities manager needs exactly <strong>36 m²</strong> of ceiling tiles. Two suppliers offer different pack sizes:<br>• <strong>Supplier P:</strong> Packs covering <strong>2.4 m²</strong> at <strong>£31.20 per pack</strong>, plus a flat <strong>£25.00 delivery fee</strong>.<br>• <strong>Supplier Q:</strong> Packs covering <strong>3.0 m²</strong> at <strong>£42.00 per pack</strong>, with <strong>free delivery</strong> and a <strong>'Buy 10 packs, get 2 packs free'</strong> deal.<br><br>Which supplier is cheaper for the 36 m² job, and by how much?",
            "lines": 5,
            "ans_label": "Cheaper Supplier & Difference =",
            "choice_box": "Supplier _____ is cheaper by £ ____________",
            "step_rows": [
                ("1. Supplier P packs needed: 36 ÷ 2.4 = 15 packs", "[P1]"),
                ("2. Supplier P total cost: (15 × £31.20) + £25.00 = £468.00 + £25.00 = £493.00", "[M1]"),
                ("3. Supplier Q packs needed: 36 ÷ 3.0 = 12 packs. With 'Buy 10 get 2 free', pay for 10 packs: 10 × £42.00 = £420.00", "[P1]"),
                ("4. Compare and conclude: Supplier Q (£420.00) is cheaper than Supplier P (£493.00) by £73.00.", "[A1]")
            ],
            "final_answer": "Supplier Q is cheaper by £73.00 (£420.00 vs £493.00)",
            "pitfall": "Multiplying 12 × £42.00 = £504.00 for Supplier Q without deducting the 2 free packs.",
            "reverse_check": "£493.00 - £420.00 = £73.00."
        }
    ),

    # 8. PROBLEMS INVOLVING MONEY
    make_maths_topic(
        "problems-involving-money",
        "Problems Involving Money & Multi-Tier Pricing",
        "L1.14 • L2.15 • L2.16",
        "Break multi-tier problems into clear line items: Standing Charge/Base Fee + Usage Charges − Discounts + Tax/VAT. Always convert pence (p) into pounds (£) by dividing by 100 before adding.",
        {
            "title": "Question 1 (Level 1 Foreign Currency Exchange)",
            "marks": 2,
            "stem": "A radiographer exchanges <strong>£650</strong> into US Dollars ($) before a training trip.<br>The exchange rate is <strong>£1 = $1.28</strong>, and the travel desk deducts a flat <strong>$12.00 service fee</strong> after conversion.<br>How many US Dollars ($) does the radiographer receive?",
            "lines": 3,
            "ans_label": "US Dollars received =",
            "choice_box": "$ ____________________",
            "step_rows": [
                ("1. Convert GBP to USD: 650 × 1.28 = $832.00", "[M1]"),
                ("2. Deduct $12.00 fee: $832.00 - $12.00 = $820.00", "[A1]")
            ],
            "final_answer": "$820.00",
            "pitfall": "Dividing £650 by 1.28 instead of multiplying.",
            "reverse_check": "($820 + $12) ÷ 1.28 = $832 ÷ 1.28 = £650."
        },
        {
            "title": "Question 2 (Level 2 Domestic Gas Meter Bill)",
            "marks": 2,
            "stem": "A household gas bill over a <strong>60-day period</strong> shows <strong>1,400 kWh</strong> of gas used.<br>Gas is charged at <strong>7.5p per kWh</strong> plus a standing charge of <strong>30p per day</strong>.<br>Calculate the total pre-VAT charge in pounds (£).",
            "lines": 3,
            "ans_label": "Pre-VAT gas charge =",
            "choice_box": "£ ____________________",
            "step_rows": [
                ("1. Usage charge: 1,400 × £0.075 = £105.00; Standing charge: 60 × £0.30 = £18.00", "[M1]"),
                ("2. Total pre-VAT charge: £105.00 + £18.00 = £123.00", "[A1]")
            ],
            "final_answer": "£123.00",
            "pitfall": "Using 0.75 instead of 0.075 for 7.5p per kWh.",
            "reverse_check": "(£123 - £18) ÷ £0.075 = £105 ÷ 0.075 = 1,400 kWh."
        },
        {
            "title": "Question 3 (Level 1 Van Hire Mileage Tariff)",
            "marks": 3,
            "stem": "A hospital charity hires a Luton van for <strong>4 days</strong> to collect donated furniture.<br>• Daily hire rate: <strong>£45.00 per day</strong> (includes <strong>80 free miles per day</strong>).<br>• Excess mileage charge: <strong>25p for every mile</strong> over the total free allowance.<br>The driver covers a total of <strong>460 miles</strong> over the 4 days. Calculate the total hire cost.",
            "lines": 4,
            "ans_label": "Total Hire Cost =",
            "choice_box": "£ ____________________",
            "step_rows": [
                ("1. Base hire for 4 days: 4 × £45.00 = £180.00", "[M1]"),
                ("2. Free mileage = 4 × 80 = 320 miles → Excess miles = 460 - 320 = 140 miles", "[P1]"),
                ("3. Excess charge = 140 × £0.25 = £35.00 → Total cost = £180.00 + £35.00 = £215.00", "[A1]")
            ],
            "final_answer": "£215.00",
            "pitfall": "Deducting only 80 free miles instead of 4 × 80 = 320 free miles.",
            "reverse_check": "(£215 - £180) ÷ £0.25 = 140 excess miles + 320 free miles = 460 miles."
        },
        {
            "title": "Question 4 (Level 2 Group Conference Catering Package)",
            "marks": 3,
            "stem": "A training centre hosts a clinical governance day for <strong>35 delegates</strong>.<br>• Venue room hire: <strong>£220.00</strong><br>• Lunch &amp; refreshments: <strong>£14.00 per delegate</strong><br>• Promotional offer: <strong>10% discount on food only</strong> when booking for 30 or more delegates.<br><br>Calculate the total cost of the event.",
            "lines": 4,
            "ans_label": "Total Event Cost =",
            "choice_box": "£ ____________________",
            "step_rows": [
                ("1. Gross food cost: 35 × £14.00 = £490.00", "[M1]"),
                ("2. Discounted food cost (10% off food): £490.00 - £49.00 = £441.00", "[P1]"),
                ("3. Add room hire: £441.00 + £220.00 = £661.00", "[A1]")
            ],
            "final_answer": "£661.00",
            "pitfall": "Taking 10% off the £220 room hire as well, when the discount applies to food only.",
            "reverse_check": "£661 - £220 = £441; £441 ÷ 0.90 = £490 = 35 × £14."
        },
        {
            "title": "Question 5 (Level 2 Compound vs Simple Interest Investment)",
            "marks": 4,
            "stem": "A community health credit union invests <strong>£15,000</strong> for <strong>2 years</strong>.<br>• <strong>Bond X:</strong> Pays <strong>4% compound interest</strong> per year.<br>• <strong>Bond Y:</strong> Pays <strong>4.1% simple interest</strong> per year, plus a <strong>£15.00</strong> welcome bonus added at the end of Year 2.<br><br>Which bond gives the greater total return after 2 years, and by how much?",
            "lines": 5,
            "ans_label": "Better Bond & Difference =",
            "choice_box": "Bond _____ by £ ____________",
            "step_rows": [
                ("1. Bond X (4% compound): Year 1 = £15,000 × 1.04 = £15,600; Year 2 = £15,600 × 1.04 = £16,224.00 (Interest = £1,224.00)", "[P1]"),
                ("2. Bond Y (4.1% simple + £15): 2 × (£15,000 × 0.041) = 2 × £615 = £1,230; plus £15 bonus = £1,245.00 return (Total = £16,245.00)", "[P1]"),
                ("3. Calculate difference: £16,245.00 - £16,224.00 = £21.00", "[M1]"),
                ("4. Conclude: Bond Y gives the greater total return by £21.00.", "[A1]")
            ],
            "final_answer": "Bond Y by £21.00 (£16,245.00 vs £16,224.00)",
            "pitfall": "Forgetting to add the £15.00 welcome bonus to Bond Y.",
            "reverse_check": "£1,245.00 - £1,224.00 = £21.00."
        },
        {
            "title": "Question 6 (Level 2 Fundraising Gala Profit Target Evaluation)",
            "marks": 4,
            "stem": "A hospital charity organises a fundraising dinner with a target net profit of at least <strong>£3,500</strong>.<br>• <strong>180 tickets</strong> are sold at <strong>£45.00 each</strong>.<br>• A corporate sponsor donates <strong>£750.00</strong>.<br>• The hotel charges <strong>£24.50 per meal</strong> for each of the 180 guests, plus <strong>£650.00</strong> for audio-visual hire.<br>• Raffle prizes cost the charity <strong>£280.00</strong>.<br><br>Did the charity achieve its £3,500 net profit target? Show all income and expenditure figures.",
            "lines": 5,
            "ans_label": "Decision & Net Profit =",
            "choice_box": "Yes / No: Net profit is £ ____________",
            "step_rows": [
                ("1. Total income: (180 × £45.00) + £750.00 = £8,100.00 + £750.00 = £8,850.00", "[P1]"),
                ("2. Total expenditure: (180 × £24.50) + £650.00 + £280.00 = £4,410.00 + £930.00 = £5,340.00", "[P1]"),
                ("3. Net profit: £8,850.00 - £5,340.00 = £3,510.00", "[M1]"),
                ("4. Conclude: Yes, the charity achieved its target with a net profit of £3,510.00 (£10.00 above the £3,500 target).", "[A1]")
            ],
            "final_answer": "Yes (Net profit is £3,510.00, exceeding the £3,500 target by £10.00)",
            "pitfall": "Omitting the £750 corporate sponsorship or £280 raffle prize cost.",
            "reverse_check": "£3,510 + £5,340 = £8,850."
        }
    ),

    # 9. TIME
    make_maths_topic(
        "time",
        "Time, 24-Hour Clocks & Timetables",
        "L1.16 • L1.17 • L2.18",
        "Time is base-60 (60 minutes = 1 hour). Never type 1 hr 45 mins as 1.45! Use the timeline bridge method (jump to next whole hour, count whole hours, add remaining minutes) for elapsed time.",
        {
            "title": "Question 1 (Level 1 Elapsed Shift Duration)",
            "marks": 2,
            "stem": "A phlebotomist starts her morning clinic at <strong>07:45</strong> and finishes at <strong>13:20</strong>.<br>How long is her clinic session in hours and minutes?",
            "lines": 3,
            "ans_label": "Duration =",
            "choice_box": "_______ hours _______ minutes",
            "step_rows": [
                ("1. Bridge across hours: 07:45 to 08:00 = 15 mins; 08:00 to 13:00 = 5 hours; 13:00 to 13:20 = 20 mins", "[M1]"),
                ("2. Sum duration: 5 hours 35 minutes (or 335 minutes)", "[A1]")
            ],
            "final_answer": "5 hours 35 minutes",
            "pitfall": "Subtracting 13.20 - 7.45 as base-100 decimals to get 5 hours 75 minutes.",
            "reverse_check": "07:45 + 5 hrs = 12:45; 12:45 + 35 mins = 13:20."
        },
        {
            "title": "Question 2 (Level 2 Decimal Hours Conversion)",
            "marks": 2,
            "stem": "A flight data recorder logs a total airborne time of <strong>3.65 hours</strong>.<br>Convert <strong>3.65 hours</strong> into hours and minutes.",
            "lines": 3,
            "ans_label": "Hours & Minutes =",
            "choice_box": "_______ hours _______ minutes",
            "step_rows": [
                ("1. Multiply decimal fraction of an hour by 60: 0.65 × 60 = 39 minutes", "[M1]"),
                ("2. Combine with whole hours: 3 hours 39 minutes", "[A1]")
            ],
            "final_answer": "3 hours 39 minutes",
            "pitfall": "Writing 3 hours 65 minutes (or 4 hours 5 minutes) by treating .65 as 65 minutes.",
            "reverse_check": "39 ÷ 60 = 0.65; 3 + 0.65 = 3.65 hours."
        },
        {
            "title": "Question 3 (Level 1 Multi-Stage Surgical Theatre Schedule)",
            "marks": 3,
            "stem": "An operating theatre starts pre-op preparation at <strong>08:50</strong>.<br>• Pre-op preparation takes <strong>35 minutes</strong>.<br>• The surgical procedure lasts <strong>2 hours 40 minutes</strong>.<br>• Post-op theatre deep-cleaning takes <strong>25 minutes</strong>.<br><br>At what time (in 24-hour clock format) is the theatre ready for the next patient?",
            "lines": 4,
            "ans_label": "Ready Time (24-hr) =",
            "choice_box": "____________________",
            "step_rows": [
                ("1. Sum total minutes: 35 mins + 160 mins (2h 40m) + 25 mins = 220 minutes", "[M1]"),
                ("2. Convert 220 minutes to hours and minutes: 220 ÷ 60 = 3 hours 40 minutes", "[P1]"),
                ("3. Add to 08:50 start time: 08:50 + 3 hrs = 11:50; 11:50 + 40 mins = 12:30", "[A1]")
            ],
            "final_answer": "12:30",
            "pitfall": "Adding 50 mins + 40 mins = 90 mins and writing 11:90 instead of carrying 60 minutes into 12:30.",
            "reverse_check": "12:30 - 3 hrs 40 mins = 08:50."
        },
        {
            "title": "Question 4 (Level 2 Overnight Shift Pay Calculation)",
            "marks": 3,
            "stem": "A night security officer works from <strong>20:45 on Friday</strong> until <strong>06:15 on Saturday</strong>.<br>Each shift includes an <strong>unpaid break of 30 minutes</strong>.<br>The officer is paid <strong>£13.60 per paid hour</strong>.<br><br>Calculate the officer's gross pay for this night shift.",
            "lines": 4,
            "ans_label": "Shift Gross Pay =",
            "choice_box": "£ ____________________",
            "step_rows": [
                ("1. Total shift duration across midnight: 20:45 to 24:00 = 3 hrs 15 mins; 00:00 to 06:15 = 6 hrs 15 mins → Total = 9 hrs 30 mins", "[M1]"),
                ("2. Deduct 30-minute unpaid break: 9 hrs 30 mins - 30 mins = 9.0 paid hours", "[P1]"),
                ("3. Multiply paid hours by hourly rate: 9 × £13.60 = £122.40", "[A1]")
            ],
            "final_answer": "£122.40",
            "pitfall": "Forgetting to deduct the 30-minute unpaid break (paying for 9.5 hours = £129.20).",
            "reverse_check": "£122.40 ÷ £13.60 = 9 paid hours + 0.5 hr break = 9.5 hrs (20:45 to 06:15)."
        },
        {
            "title": "Question 5 (Level 2 Timetable Backward Planning)",
            "marks": 4,
            "stem": "A medical rep must attend a hospital presentation in Birmingham starting at <strong>11:15</strong>.<br>• It takes <strong>18 minutes</strong> to walk from Birmingham New Street station to the hospital.<br>• Train departures from London Euston (and arrival times at Birmingham) are:<br>  – <strong>Train A:</strong> Departs 08:40 → Arrives 10:02<br>  – <strong>Train B:</strong> Departs 09:10 → Arrives 10:32<br>  – <strong>Train C:</strong> Departs 09:40 → Arrives 11:02<br>• It takes the rep <strong>35 minutes</strong> to travel from home to London Euston, and she wants to arrive at Euston at least <strong>10 minutes before</strong> her train departs.<br><br>What is the latest time she can leave home to arrive at the hospital on time?",
            "lines": 5,
            "ans_label": "Latest Home Departure =",
            "choice_box": "_____________ (catching Train _____)",
            "step_rows": [
                ("1. Latest station arrival at Birmingham: 11:15 - 18 mins walk = 10:57", "[P1]"),
                ("2. Select latest valid train: Train C (arrives 11:02) is 5 mins too late; must catch Train B (departs 09:10, arrives 10:32)", "[M1]"),
                ("3. Latest arrival at London Euston: 09:10 - 10 mins buffer = 09:00", "[P1]"),
                ("4. Subtract 35 mins travel from home: 09:00 - 35 mins = 08:25", "[A1]")
            ],
            "final_answer": "08:25 (catching Train B at 09:10)",
            "pitfall": "Selecting Train C (11:02 arrival + 18 mins walk = 11:20, which is 5 minutes late).",
            "reverse_check": "08:25 + 35m = 09:00 (+10m buffer = 09:10 Train B) → arrives 10:32 + 18m walk = 10:50 (before 11:15)."
        },
        {
            "title": "Question 6 (Level 2 Clinic Appointment Scheduling Capacity)",
            "marks": 4,
            "stem": "An optometrist runs a testing clinic from <strong>09:00 to 16:30</strong>.<br>• Each patient appointment lasts <strong>25 minutes</strong>, followed by a mandatory <strong>5-minute room sanitisation</strong> turnaround before the next patient.<br>• The optometrist takes a <strong>45-minute lunch break</strong> and two <strong>15-minute admin breaks</strong> during the day.<br><br>The receptionist has booked <strong>13 patients</strong> for today. Does the schedule have enough time to see all 13 patients?",
            "lines": 5,
            "ans_label": "Decision & Max Patients =",
            "choice_box": "Yes / No: Available time is _______ mins vs _______ mins needed",
            "step_rows": [
                ("1. Total clinic window (09:00 to 16:30): 7 hours 30 minutes = 450 minutes", "[P1]"),
                ("2. Total breaks: 45 + 15 + 15 = 75 minutes → Available clinical time = 450 - 75 = 375 minutes", "[P1]"),
                ("3. Time per patient slot (appointment + turnaround): 25 + 5 = 30 minutes per patient", "[M1]"),
                ("4. Compare: 13 patients × 30 mins = 390 mins needed > 375 mins available (or 375 ÷ 30 = 12.5 → max 12 patients). No, there is not enough time (short by 15 minutes).", "[A1]")
            ],
            "final_answer": "No (13 patients require 390 mins [or 385 mins if last turnaround omitted], exceeding the 375 available minutes)",
            "pitfall": "Dividing 375 by 25 minutes and forgetting the 5-minute sanitisation turnaround per patient.",
            "reverse_check": "12 patients × 30 mins = 360 mins + 75 mins breaks = 435 mins (fits in 450 mins; 13th needs 465 mins)."
        }
    ),

    # 10. SPEED
    make_maths_topic(
        "speed",
        "Speed, Distance & Time",
        "L2.19",
        "Distance = Speed × Time | Speed = Distance ÷ Time | Time = Distance ÷ Speed. Always convert minutes to decimal hours by dividing by 60 (e.g. 45 mins = 0.75 hours) before using the formula!",
        {
            "title": "Question 1 (Level 2 Average Speed with Minutes)",
            "marks": 2,
            "stem": "A medical courier motorcycle travels <strong>63 miles</strong> in <strong>1 hour and 15 minutes</strong>.<br>Calculate the average speed of the motorcycle in miles per hour (mph).",
            "lines": 3,
            "ans_label": "Average Speed =",
            "choice_box": "_____________ mph",
            "step_rows": [
                ("1. Convert 1 hour 15 minutes to decimal hours: 1 + (15 ÷ 60) = 1.25 hours", "[M1]"),
                ("2. Speed = Distance ÷ Time = 63 ÷ 1.25 = 50.4 mph", "[A1]")
            ],
            "final_answer": "50.4 mph",
            "pitfall": "Dividing 63 by 1.15 (= 54.78 mph) instead of 1.25 hours.",
            "reverse_check": "50.4 mph × 1.25 hours = 63 miles."
        },
        {
            "title": "Question 2 (Level 2 Journey Time in Hours & Minutes)",
            "marks": 2,
            "stem": "A delivery van travels <strong>154 miles</strong> along a motorway at an average speed of <strong>56 mph</strong>.<br>How long does the journey take? Give your answer in <strong>hours and minutes</strong>.",
            "lines": 3,
            "ans_label": "Journey Time =",
            "choice_box": "_______ hours _______ minutes",
            "step_rows": [
                ("1. Time = Distance ÷ Speed = 154 ÷ 56 = 2.75 hours", "[M1]"),
                ("2. Convert 0.75 hours to minutes (0.75 × 60 = 45 mins): 2 hours 45 minutes", "[A1]")
            ],
            "final_answer": "2 hours 45 minutes",
            "pitfall": "Writing 2.75 hours as 2 hours 75 minutes (or 3 hours 15 minutes).",
            "reverse_check": "56 mph × 2.75 hours = 154 miles."
        },
        {
            "title": "Question 3 (Level 2 Distance Travelled in Minutes)",
            "marks": 3,
            "stem": "An air ambulance helicopter flies from its base to an incident scene at an average speed of <strong>135 mph</strong>.<br>The flight takes <strong>24 minutes</strong>.<br><br>Calculate the distance flown by the air ambulance in miles.",
            "lines": 4,
            "ans_label": "Distance flown =",
            "choice_box": "_____________ miles",
            "step_rows": [
                ("1. Convert 24 minutes into decimal hours: 24 ÷ 60 = 0.4 hours", "[M1]"),
                ("2. Apply Distance = Speed × Time: 135 mph × 0.4 hours", "[P1]"),
                ("3. Evaluate: 54 miles", "[A1]")
            ],
            "final_answer": "54 miles",
            "pitfall": "Multiplying 135 × 24 = 3,240 miles without converting minutes into hours.",
            "reverse_check": "54 miles ÷ 135 mph = 0.4 hours = 24 minutes."
        },
        {
            "title": "Question 4 (Level 2 Metric-Imperial Speed Conversion)",
            "marks": 3,
            "stem": "A European freight driver is driving on a UK dual carriageway where the speed limit for his vehicle is <strong>60 mph</strong>.<br>His digital speedometer is set to kilometres per hour and reads <strong>92 km/h</strong>.<br>Use the conversion factor: <strong>5 miles = 8 km</strong>.<br><br>By how many mph is the driver below the 60 mph speed limit?",
            "lines": 4,
            "ans_label": "Margin below 60 mph =",
            "choice_box": "_____________ mph below limit",
            "step_rows": [
                ("1. Convert 92 km/h to mph: (92 ÷ 8) × 5", "[M1]"),
                ("2. Evaluate speed in mph: 11.5 × 5 = 57.5 mph", "[P1]"),
                ("3. Subtract from 60 mph limit: 60 - 57.5 = 2.5 mph below the limit", "[A1]")
            ],
            "final_answer": "2.5 mph (travelling at 57.5 mph)",
            "pitfall": "Multiplying 92 by 8 and dividing by 5 (= 147.2 mph).",
            "reverse_check": "57.5 mph ÷ 5 × 8 = 92 km/h."
        },
        {
            "title": "Question 5 (Level 2 Two-Stage Journey Overall Average Speed)",
            "marks": 4,
            "stem": "A mobile screening unit drives from Leeds to Birmingham in two stages:<br>• <strong>Stage 1:</strong> Drives <strong>75 miles</strong> in <strong>1 hour 30 minutes</strong>.<br>• <strong>Stage 2:</strong> Drives the remaining <strong>45 miles</strong> at an average speed of <strong>30 mph</strong>.<br><br>Calculate the unit's <strong>overall average speed</strong> for the entire 120-mile journey in mph.",
            "lines": 5,
            "ans_label": "Overall Average Speed =",
            "choice_box": "_____________ mph",
            "step_rows": [
                ("1. Stage 1 time = 1.5 hours; Stage 2 time = Distance ÷ Speed = 45 ÷ 30 = 1.5 hours", "[P1]"),
                ("2. Total distance = 75 + 45 = 120 miles; Total time = 1.5 + 1.5 = 3.0 hours", "[P1]"),
                ("3. Overall Average Speed = Total Distance ÷ Total Time = 120 ÷ 3.0", "[M1]"),
                ("4. Evaluate: 40 mph", "[A1]")
            ],
            "final_answer": "40 mph",
            "pitfall": "Wait — here Stage 1 speed is 50 mph and Stage 2 is 30 mph, and since times are equal (1.5h each) the average is 40 mph, but students must show Total Distance (120) ÷ Total Time (3) to earn method marks!",
            "reverse_check": "40 mph × 3 hours = 120 miles (75 + 45)."
        },
        {
            "title": "Question 6 (Level 2 Cold-Chain Vaccine Delivery ETA Verification)",
            "marks": 4,
            "stem": "A refrigerated vaccine van leaves the depot at <strong>07:50</strong> to make a delivery <strong>132 miles</strong> away.<br>• The driver must take a mandatory <strong>30-minute rest break</strong> en route.<br>• Due to heavy traffic, the van achieves an average driving speed of <strong>48 mph</strong>.<br>• The hospital pharmacy closes its loading bay at <strong>11:00</strong>.<br><br>Will the vaccine van arrive before the loading bay closes at 11:00? Show full working.",
            "lines": 5,
            "ans_label": "Decision & Arrival Time =",
            "choice_box": "Yes / No: Arrives at _____________",
            "step_rows": [
                ("1. Calculate driving time: Time = 132 ÷ 48 = 2.75 hours", "[M1]"),
                ("2. Convert 2.75 hours to hours and minutes: 2 hours + (0.75 × 60) = 2 hours 45 minutes", "[P1]"),
                ("3. Add 30-minute rest break: 2 hrs 45 mins + 30 mins = 3 hours 15 minutes total journey time", "[P1]"),
                ("4. Add to 07:50 departure: 07:50 + 3 hrs 15 mins = 11:05. Conclude: No, the van arrives at 11:05, which is 5 minutes after the 11:00 closure.", "[A1]")
            ],
            "final_answer": "No (Arrives at 11:05, which is 5 minutes late)",
            "pitfall": "Forgetting to add the 30-minute mandatory rest break (which gives 10:35).",
            "reverse_check": "11:05 - 30m break = 10:35 driving finish; 07:50 to 10:35 = 2h 45m = 2.75h; 2.75 × 48 = 132 miles."
        }
    ),

    # 11. DENSITY
    make_maths_topic(
        "density",
        "Density & Compound Units",
        "L2.19",
        "Mass = Density × Volume | Density = Mass ÷ Volume | Volume = Mass ÷ Density. Always check that Mass and Volume units match the Density unit (e.g. g and cm³ for g/cm³; kg and m³ for kg/m³).",
        {
            "title": "Question 1 (Level 2 Finding Density)",
            "marks": 2,
            "stem": "A solid brass medical valve has a volume of <strong>45 cm³</strong> and a mass of <strong>382.5 grams</strong>.<br>Calculate the density of the brass in <strong>g/cm³</strong>.",
            "lines": 3,
            "ans_label": "Density =",
            "choice_box": "_____________ g/cm³",
            "step_rows": [
                ("1. Apply Density = Mass ÷ Volume: 382.5 ÷ 45", "[M1]"),
                ("2. Evaluate: 8.5 g/cm³", "[A1]")
            ],
            "final_answer": "8.5 g/cm³",
            "pitfall": "Multiplying 382.5 × 45 instead of dividing Mass by Volume.",
            "reverse_check": "8.5 g/cm³ × 45 cm³ = 382.5 g."
        },
        {
            "title": "Question 2 (Level 2 Finding Volume from Mass & Density)",
            "marks": 2,
            "stem": "A laboratory flask contains <strong>1,030 grams</strong> of sterile glycerine solution.<br>The glycerine solution has a density of <strong>1.25 g/cm³</strong>.<br>Calculate the volume of the glycerine solution in <strong>cm³</strong>.",
            "lines": 3,
            "ans_label": "Volume =",
            "choice_box": "_____________ cm³",
            "step_rows": [
                ("1. Apply Volume = Mass ÷ Density: 1,030 ÷ 1.25", "[M1]"),
                ("2. Evaluate: 824 cm³", "[A1]")
            ],
            "final_answer": "824 cm³",
            "pitfall": "Multiplying 1,030 × 1.25 (= 1,287.5) instead of dividing by density.",
            "reverse_check": "824 cm³ × 1.25 g/cm³ = 1,030 g."
        },
        {
            "title": "Question 3 (Level 2 Cuboid Volume & Mass in Kilograms)",
            "marks": 3,
            "stem": "A radiation-shielding lead brick is shaped as a cuboid measuring <strong>20 cm long, 10 cm wide, and 5 cm high</strong>.<br>Lead has a density of <strong>11.3 g/cm³</strong>.<br><br>Calculate the mass of the lead brick in <strong>kilograms (kg)</strong>.",
            "lines": 4,
            "ans_label": "Mass of brick =",
            "choice_box": "_____________ kg",
            "step_rows": [
                ("1. Calculate cuboid volume: 20 × 10 × 5 = 1,000 cm³", "[M1]"),
                ("2. Calculate mass in grams: 1,000 cm³ × 11.3 g/cm³ = 11,300 grams", "[P1]"),
                ("3. Convert grams to kilograms: 11,300 ÷ 1,000 = 11.3 kg", "[A1]")
            ],
            "final_answer": "11.3 kg",
            "pitfall": "Leaving the final answer as 11,300 when the question specifies kilograms.",
            "reverse_check": "11.3 kg = 11,300 g; 11,300 ÷ 1,000 cm³ = 11.3 g/cm³."
        },
        {
            "title": "Question 4 (Level 2 Floor Loading Pressure Compound Measure)",
            "marks": 3,
            "stem": "A heavy autoclave steriliser exerts a downward force of <strong>14,400 Newtons (N)</strong> on a hospital plant-room floor.<br>The rectangular base of the autoclave measures <strong>1.6 m long by 1.2 m wide</strong>.<br>Use the formula: <strong>Pressure (N/m²) = Force (N) ÷ Area (m²)</strong>.<br><br>Calculate the pressure exerted on the floor in <strong>N/m²</strong>.",
            "lines": 4,
            "ans_label": "Floor Pressure =",
            "choice_box": "_____________ N/m²",
            "step_rows": [
                ("1. Calculate contact base area: 1.6 m × 1.2 m = 1.92 m²", "[M1]"),
                ("2. Substitute into Pressure = Force ÷ Area: 14,400 ÷ 1.92", "[P1]"),
                ("3. Evaluate: 7,500 N/m²", "[A1]")
            ],
            "final_answer": "7,500 N/m²",
            "pitfall": "Dividing 14,400 by perimeter (5.6 m) instead of area (1.92 m²).",
            "reverse_check": "7,500 N/m² × 1.92 m² = 14,400 N."
        },
        {
            "title": "Question 5 (Level 2 Concrete Driveway Ready-Mix Tonnage & Cost)",
            "marks": 4,
            "stem": "A civil engineer is pouring a concrete ambulance bay slab measuring <strong>12 m long, 5 m wide, and 0.15 m deep</strong>.<br>• Wet concrete has a density of <strong>2,400 kg/m³</strong>.<br>• Ready-mix concrete is sold at <strong>£85.00 per tonne</strong> (1 tonne = 1,000 kg).<br><br>Calculate the total cost of the concrete required for the ambulance bay slab.",
            "lines": 5,
            "ans_label": "Total Concrete Cost =",
            "choice_box": "£ ____________________",
            "step_rows": [
                ("1. Calculate volume of concrete slab: 12 × 5 × 0.15 = 9 m³", "[P1]"),
                ("2. Calculate mass in kg: 9 m³ × 2,400 kg/m³ = 21,600 kg", "[M1]"),
                ("3. Convert mass to tonnes: 21,600 ÷ 1,000 = 21.6 tonnes", "[P1]"),
                ("4. Calculate total cost: 21.6 × £85.00 = £1,836.00", "[A1]")
            ],
            "final_answer": "£1,836.00 (21.6 tonnes)",
            "pitfall": "Forgetting to convert 15 cm (0.15 m) or forgetting to divide kg by 1,000 to get tonnes.",
            "reverse_check": "£1,836 ÷ £85 = 21.6 tonnes = 21,600 kg; 21,600 ÷ 9 m³ = 2,400 kg/m³."
        },
        {
            "title": "Question 6 (Level 2 Cylindrical Liquid Nitrogen Tank Trailer Limit)",
            "marks": 4,
            "stem": "A cylindrical storage tank has an internal radius of <strong>0.5 metres</strong> and a height of <strong>2.0 metres</strong>.<br>• The tank is filled completely with liquid medical oxygen, which has a density of <strong>1,140 kg/m³</strong>.<br>• The empty steel tank itself weighs <strong>215 kg</strong>.<br>• Use <strong>π = 3.14</strong>.<br><br>A transport trailer has a maximum payload limit of <strong>2,000 kg</strong>. Can the trailer legally carry the full tank? Show full working.",
            "lines": 5,
            "ans_label": "Decision & Total Mass =",
            "choice_box": "Yes / No: Total loaded mass is _______ kg",
            "step_rows": [
                ("1. Calculate cylinder volume (V = π × r² × h): 3.14 × 0.5² × 2.0 = 3.14 × 0.25 × 2.0 = 1.57 m³", "[P1]"),
                ("2. Calculate mass of liquid oxygen: 1.57 m³ × 1,140 kg/m³ = 1,789.8 kg", "[M1]"),
                ("3. Add empty steel tank mass: 1,789.8 + 215 = 2,004.8 kg", "[P1]"),
                ("4. Compare and conclude: 2,004.8 kg > 2,000 kg (exceeds limit by 4.8 kg). No, the trailer cannot legally carry the full tank.", "[A1]")
            ],
            "final_answer": "No (Total mass is 2,004.8 kg, exceeding the 2,000 kg limit by 4.8 kg)",
            "pitfall": "Forgetting to add the 215 kg empty tank weight (which would give 1,789.8 kg and a false 'Yes').",
            "reverse_check": "(2,004.8 - 215) ÷ 1,140 = 1.57 m³."
        }
    ),

    # 12. UNIT CONVERSIONS
    make_maths_topic(
        "unit-conversions",
        "Metric & Imperial Unit Conversions",
        "L1.18 • L2.20 • L2.21",
        "Big unit to small unit = MULTIPLY; Small unit to big unit = DIVIDE. Key metric factors: 1 km = 1,000 m, 1 m = 100 cm, 1 cm = 10 mm; 1 t = 1,000 kg, 1 kg = 1,000 g; 1 L = 1,000 ml.",
        {
            "title": "Question 1 (Level 1 Metric Length & Mass Conversion)",
            "marks": 2,
            "stem": "Complete both metric conversions below:<br>(a) Convert <strong>4.08 kilometres</strong> into <strong>metres</strong>.<br>(b) Convert <strong>650 grams</strong> into <strong>kilograms</strong>.",
            "lines": 3,
            "ans_label": "Conversions =",
            "choice_box": "(a) _________ m | (b) _________ kg",
            "step_rows": [
                ("1. (a) Multiply km by 1,000: 4.08 × 1,000 = 4,080 m", "[A1]"),
                ("2. (b) Divide grams by 1,000: 650 ÷ 1,000 = 0.65 kg", "[A1]")
            ],
            "final_answer": "(a) 4,080 m | (b) 0.65 kg",
            "pitfall": "Multiplying or dividing by 100 instead of 1,000.",
            "reverse_check": "4,080 ÷ 1,000 = 4.08 km; 0.65 × 1,000 = 650 g."
        },
        {
            "title": "Question 2 (Level 2 Miles and Kilometres Conversion)",
            "marks": 2,
            "stem": "An organ transplant courier drives <strong>104 kilometres</strong> from an airport to a specialist hospital.<br>Using the conversion <strong>5 miles = 8 kilometres</strong>, calculate this distance in <strong>miles</strong>.",
            "lines": 3,
            "ans_label": "Distance in miles =",
            "choice_box": "_____________ miles",
            "step_rows": [
                ("1. Divide kilometres by 8 to find 1 unit: 104 ÷ 8 = 13", "[M1]"),
                ("2. Multiply by 5: 13 × 5 = 65 miles", "[A1]")
            ],
            "final_answer": "65 miles",
            "pitfall": "Calculating (104 ÷ 5) × 8 = 166.4 miles (miles must be smaller than km!).",
            "reverse_check": "65 ÷ 5 × 8 = 13 × 8 = 104 km."
        },
        {
            "title": "Question 3 (Level 1 Liquid Capacity Unit Mixing)",
            "marks": 3,
            "stem": "A hospital catering team prepares a fruit punch by mixing:<br>• <strong>3.5 litres</strong> of orange juice<br>• <strong>75 centilitres (cl)</strong> of cranberry juice<br>• <strong>450 millilitres (ml)</strong> of ginger ale<br><br>Calculate the total volume of fruit punch in <strong>millilitres (ml)</strong>.",
            "lines": 4,
            "ans_label": "Total Volume =",
            "choice_box": "_____________ ml",
            "step_rows": [
                ("1. Convert 3.5 L to ml: 3.5 × 1,000 = 3,500 ml", "[M1]"),
                ("2. Convert 75 cl to ml: 75 × 10 = 750 ml", "[P1]"),
                ("3. Sum all three volumes in ml: 3,500 + 750 + 450 = 4,700 ml", "[A1]")
            ],
            "final_answer": "4,700 ml (or 4.7 litres)",
            "pitfall": "Converting 75 cl as 75 ml instead of 750 ml (remember 1 cl = 10 ml).",
            "reverse_check": "3.5 L + 0.75 L + 0.45 L = 4.7 L = 4,700 ml."
        },
        {
            "title": "Question 4 (Level 2 Stone & Pounds to Kilograms Clinical Dosage)",
            "marks": 3,
            "stem": "A patient weighs <strong>12 stone 10 lbs</strong>.<br>Use the conversions: <strong>1 stone = 14 lbs</strong> and <strong>1 kg = 2.2 lbs</strong>.<br><br>Calculate the patient's weight in <strong>kilograms (kg)</strong>.",
            "lines": 4,
            "ans_label": "Patient Weight =",
            "choice_box": "_____________ kg",
            "step_rows": [
                ("1. Convert 12 stone to lbs: 12 × 14 = 168 lbs", "[M1]"),
                ("2. Add remaining 10 lbs: 168 + 10 = 178 lbs total", "[P1]"),
                ("3. Divide by 2.2 to convert to kg: 178 ÷ 2.2 = 80.91 kg (accept 80.9 kg or 81 kg)", "[A1]")
            ],
            "final_answer": "80.91 kg (or 81 kg)",
            "pitfall": "Treating 12 stone 10 lbs as 12.10 stone or assuming 10 lbs is 1 stone.",
            "reverse_check": "80.909 × 2.2 = 178 lbs = (12 × 14) + 10."
        },
        {
            "title": "Question 5 (Level 2 Imported Medical Fridge Clearance Check)",
            "marks": 4,
            "stem": "A pharmacy orders an imported American vaccine refrigerator with dimensions:<br>• Height: <strong>6 feet 4 inches</strong><br>• Width: <strong>30 inches</strong><br>The pharmacy alcove where it will stand measures <strong>198 cm high</strong> by <strong>80 cm wide</strong>.<br>Use: <strong>1 foot = 12 inches</strong> and <strong>1 inch = 2.54 cm</strong>.<br><br>Will the refrigerator fit into the alcove? Check both height and width in centimetres.",
            "lines": 5,
            "ans_label": "Decision & Metric Dimensions =",
            "choice_box": "Yes / No: Height = _____ cm, Width = _____ cm",
            "step_rows": [
                ("1. Convert height to inches: (6 × 12) + 4 = 76 inches", "[P1]"),
                ("2. Convert height to cm: 76 × 2.54 = 193.04 cm", "[M1]"),
                ("3. Convert width to cm: 30 × 2.54 = 76.2 cm", "[P1]"),
                ("4. Compare both with alcove (198 cm × 80 cm): Height 193.04 cm < 198 cm and Width 76.2 cm < 80 cm. Yes, the refrigerator will fit.", "[A1]")
            ],
            "final_answer": "Yes, fits (Height = 193.04 cm < 198 cm; Width = 76.2 cm < 80 cm)",
            "pitfall": "Converting 6 feet 4 inches as 6.4 feet × 12 = 76.8 inches.",
            "reverse_check": "193.04 ÷ 2.54 = 76 inches = 6 ft 4 in; 76.2 ÷ 2.54 = 30 in."
        },
        {
            "title": "Question 6 (Level 2 Fuel Tanker Gallons vs Litres Cost Comparison)",
            "marks": 4,
            "stem": "A backup hospital generator requires <strong>250 gallons</strong> of red diesel.<br>• <strong>Supplier A</strong> quotes <strong>£5.22 per gallon</strong>.<br>• <strong>Supplier B</strong> quotes <strong>£1.12 per litre</strong>.<br>• Use the conversion: <strong>1 gallon = 4.54 litres</strong>.<br><br>Which supplier is cheaper for the 250-gallon order, and by how much?",
            "lines": 5,
            "ans_label": "Cheaper Supplier & Saving =",
            "choice_box": "Supplier _____ is cheaper by £ ____________",
            "step_rows": [
                ("1. Supplier A total cost: 250 gallons × £5.22 = £1,305.00", "[P1]"),
                ("2. Convert 250 gallons into litres: 250 × 4.54 = 1,135 litres", "[M1]"),
                ("3. Supplier B total cost: 1,135 litres × £1.12 = £1,271.20", "[P1]"),
                ("4. Compare and conclude: Supplier B (£1,271.20) is cheaper than Supplier A (£1,305.00) by £33.80.", "[A1]")
            ],
            "final_answer": "Supplier B is cheaper by £33.80 (£1,271.20 vs £1,305.00)",
            "pitfall": "Dividing 250 by 4.54 instead of multiplying gallons by 4.54 to get litres.",
            "reverse_check": "£1,305.00 - £1,271.20 = £33.80."
        }
    ),

    # 13. LENGTH
    make_maths_topic(
        "length",
        "Length & Dimensions",
        "L1.18 • L2.20",
        "Convert all measurements into the same unit (all in cm or all in m) BEFORE adding, subtracting, or dividing. When cutting rigid lengths (shelves, pipes), offcuts cannot be joined together!",
        {
            "title": "Question 1 (Level 1 Metric Length Subtraction)",
            "marks": 2,
            "stem": "An electrician has a <strong>15-metre</strong> drum of armoured cable.<br>She cuts two lengths measuring <strong>4.65 metres</strong> and <strong>680 centimetres</strong>.<br>How many metres of cable remain on the drum?",
            "lines": 3,
            "ans_label": "Remaining cable =",
            "choice_box": "_____________ m",
            "step_rows": [
                ("1. Convert 680 cm to metres: 680 ÷ 100 = 6.8 m; Total cut = 4.65 + 6.80 = 11.45 m", "[M1]"),
                ("2. Remaining cable: 15.00 - 11.45 = 3.55 m", "[A1]")
            ],
            "final_answer": "3.55 m (or 355 cm)",
            "pitfall": "Subtracting 680 directly from 15 without converting cm to metres.",
            "reverse_check": "3.55 m + 4.65 m + 6.80 m = 15.00 m."
        },
        {
            "title": "Question 2 (Level 2 Precision Millimetre Stack Thickness)",
            "marks": 2,
            "stem": "A vertical storage rack holds <strong>35 acrylic medical clipboards</strong> stacked flat on top of each other.<br>Each clipboard is <strong>4.2 mm</strong> thick.<br>Calculate the total height of the stack in <strong>centimetres (cm)</strong>.",
            "lines": 3,
            "ans_label": "Stack height =",
            "choice_box": "_____________ cm",
            "step_rows": [
                ("1. Total height in mm: 35 × 4.2 mm = 147 mm", "[M1]"),
                ("2. Convert mm to cm (÷ 10): 147 ÷ 10 = 14.7 cm", "[A1]")
            ],
            "final_answer": "14.7 cm",
            "pitfall": "Dividing by 100 (1.47 cm) instead of 10 when converting mm to cm.",
            "reverse_check": "14.7 cm = 147 mm; 147 ÷ 35 = 4.2 mm."
        },
        {
            "title": "Question 3 (Level 1 Ward Curtain Track Cut-List)",
            "marks": 3,
            "stem": "A hospital maintenance technician needs to cut <strong>6 privacy curtain rails</strong>, each measuring <strong>185 cm</strong> long.<br>Aluminium track is supplied in <strong>4-metre</strong> lengths.<br>Offcuts cannot be joined together.<br><br>How many 4-metre lengths of aluminium track must be ordered?",
            "lines": 4,
            "ans_label": "4-metre lengths needed =",
            "choice_box": "_____________ lengths",
            "step_rows": [
                ("1. Convert 4 m to 400 cm and find rails per length: 400 ÷ 185 = 2.16 → 2 full rails per 4 m length (30 cm offcut)", "[M1]"),
                ("2. Divide 6 required rails by 2 rails per length: 6 ÷ 2", "[P1]"),
                ("3. State 3 lengths of 4 m track needed", "[A1]")
            ],
            "final_answer": "3 lengths",
            "pitfall": "Adding 6 × 185 = 1,110 cm and dividing by 400 = 2.775 (which happens to round up to 3, but fails if 7 rails are needed).",
            "reverse_check": "3 lengths × 2 rails per length = 6 full 185 cm rails."
        },
        {
            "title": "Question 4 (Level 2 Corridor Equipment Bay Spacing with Gaps)",
            "marks": 3,
            "stem": "A ward manager wants to line up <strong>5 mobile diagnostic trolleys</strong> along a wall measuring <strong>4.5 metres</strong> long.<br>• Each trolley is <strong>68 cm</strong> wide.<br>• Fire safety regulations require a minimum gap of <strong>20 cm</strong> between adjacent trolleys, and at least <strong>15 cm</strong> clearance at each end of the wall.<br><br>Calculate the total length required (in cm) and state how much spare wall length remains.",
            "lines": 4,
            "ans_label": "Spare wall length =",
            "choice_box": "_____________ cm spare",
            "step_rows": [
                ("1. Width of 5 trolleys = 5 × 68 cm = 340 cm", "[M1]"),
                ("2. 4 internal gaps between 5 trolleys = 4 × 20 cm = 80 cm; plus 2 end clearances = 2 × 15 cm = 30 cm → Total required = 340 + 80 + 30 = 450 cm", "[P1]"),
                ("3. Compare with 4.5 m (450 cm) wall: 450 cm - 450 cm = 0 cm spare (fits with 0 cm remaining)", "[A1]")
            ],
            "final_answer": "0 cm spare (Total required is exactly 450 cm / 4.5 m)",
            "pitfall": "Counting 5 internal gaps between 5 trolleys instead of 4 internal gaps.",
            "reverse_check": "15 + 68 + 20 + 68 + 20 + 68 + 20 + 68 + 20 + 68 + 15 = 450 cm."
        },
        {
            "title": "Question 5 (Level 2 Timber Stud Partition Frame Costing)",
            "marks": 4,
            "stem": "A carpenter builds a rectangular stud partition frame measuring <strong>4.2 m wide by 2.4 m high</strong>.<br>• The frame requires a top plate (4.2 m), a bottom plate (4.2 m), and <strong>8 vertical studs</strong> (each 2.4 m high).<br>• Timber is sold in <strong>2.4 m lengths at £4.80 each</strong> and <strong>4.2 m lengths at £8.20 each</strong>.<br><br>Calculate the total length of timber used (in metres) and the total cost of the timber.",
            "lines": 5,
            "ans_label": "Total Length & Cost =",
            "choice_box": "Length: _______ m | Cost: £ ____________",
            "step_rows": [
                ("1. Top and bottom plates: 2 × 4.2 m = 8.4 m; 8 vertical studs: 8 × 2.4 m = 19.2 m", "[P1]"),
                ("2. Total timber length: 8.4 + 19.2 = 27.6 metres", "[M1]"),
                ("3. Cost of two 4.2 m lengths: 2 × £8.20 = £16.40; Cost of eight 2.4 m lengths: 8 × £4.80 = £38.40", "[P1]"),
                ("4. Total cost: £16.40 + £38.40 = £54.80", "[A1]")
            ],
            "final_answer": "Length: 27.6 m | Total Cost: £54.80",
            "pitfall": "Counting only 2 vertical studs instead of all 8 vertical studs.",
            "reverse_check": "£16.40 + £38.40 = £54.80; 8.4 m + 19.2 m = 27.6 m."
        },
        {
            "title": "Question 6 (Level 2 Wheelchair Ramp Gradient Compliance)",
            "marks": 4,
            "stem": "Building regulations state that a permanent wheelchair access ramp must have a maximum gradient of <strong>1 : 12</strong> (for every 1 cm of vertical rise, the horizontal run must be at least 12 cm).<br>• A clinic entrance step has a vertical rise of <strong>45 cm</strong>.<br>• Furthermore, for any rise over 30 cm, a flat mid-ramp resting landing measuring <strong>1.5 metres</strong> long must be added to the total horizontal length.<br>• The clinic forecourt has <strong>6.8 metres</strong> of horizontal space available.<br><br>Is the 6.8-metre forecourt long enough to install a compliant ramp? Show full working in metres.",
            "lines": 5,
            "ans_label": "Decision & Required Length =",
            "choice_box": "Yes / No: Minimum length needed is _______ m",
            "step_rows": [
                ("1. Calculate minimum horizontal ramp run: 45 cm × 12 = 540 cm", "[P1]"),
                ("2. Convert 540 cm to metres: 540 ÷ 100 = 5.4 metres", "[M1]"),
                ("3. Add mandatory 1.5 m resting landing (since 45 cm > 30 cm): 5.4 m + 1.5 m = 6.9 metres", "[P1]"),
                ("4. Compare against 6.8 m forecourt: 6.9 m > 6.8 m (short by 0.1 m / 10 cm). No, the forecourt is not long enough.", "[A1]")
            ],
            "final_answer": "No (Requires 6.9 m including landing, which is 0.1 m / 10 cm longer than the 6.8 m forecourt)",
            "pitfall": "Forgetting to include the mandatory 1.5 m resting landing required for rises over 30 cm.",
            "reverse_check": "5.4 m + 1.5 m = 6.9 m > 6.8 m."
        }
    ),

    # 14. WEIGHT
    make_maths_topic(
        "weight",
        "Weight & Mass",
        "L1.18 • L2.20 • L2.21",
        "1 tonne = 1,000 kg • 1 kg = 1,000 g • 1 g = 1,000 mg. Gross Weight = Net Weight of Goods + Tare Weight of Empty Container/Vehicle.",
        {
            "title": "Question 1 (Level 1 Parcel Gross Weight in Kilograms)",
            "marks": 2,
            "stem": "A medical dispatch box weighs <strong>450 grams</strong> when empty.<br>A technician packs <strong>8 bottles</strong> of saline (each weighing <strong>325 grams</strong>) into the box.<br>Calculate the total gross weight of the packed box in <strong>kilograms (kg)</strong>.",
            "lines": 3,
            "ans_label": "Gross Weight =",
            "choice_box": "_____________ kg",
            "step_rows": [
                ("1. Total weight in grams: (8 × 325 g) + 450 g = 2,600 g + 450 g = 3,050 g", "[M1]"),
                ("2. Convert to kilograms (÷ 1,000): 3,050 ÷ 1,000 = 3.05 kg", "[A1]")
            ],
            "final_answer": "3.05 kg",
            "pitfall": "Forgetting to add the 450 g empty box weight.",
            "reverse_check": "3.05 kg = 3,050 g; (3,050 - 450) ÷ 8 = 325 g."
        },
        {
            "title": "Question 2 (Level 2 Milligram to Gram Tablet Batch Mass)",
            "marks": 2,
            "stem": "Each ibuprofen tablet contains <strong>400 mg</strong> of active ingredient.<br>How many <strong>grams (g)</strong> of active ingredient are needed to manufacture a batch of <strong>2,500 tablets</strong>?",
            "lines": 3,
            "ans_label": "Active ingredient =",
            "choice_box": "_____________ g",
            "step_rows": [
                ("1. Total mg: 2,500 × 400 mg = 1,000,000 mg", "[M1]"),
                ("2. Convert mg to grams (÷ 1,000): 1,000,000 ÷ 1,000 = 1,000 g (or 1 kg)", "[A1]")
            ],
            "final_answer": "1,000 g",
            "pitfall": "Dividing by 100 instead of 1,000 when converting mg to g.",
            "reverse_check": "400 mg = 0.4 g; 2,500 × 0.4 g = 1,000 g."
        },
        {
            "title": "Question 3 (Level 1 Laundry Roll-Cage Safe Load)",
            "marks": 3,
            "stem": "A hospital laundry roll-cage has a maximum gross weight limit of <strong>250 kg</strong>.<br>The empty roll-cage weighs <strong>28 kg</strong>.<br>It is loaded with laundry bags that each weigh <strong>12 kg</strong>.<br><br>What is the maximum number of full laundry bags that can be loaded into the cage without exceeding the 250 kg limit?",
            "lines": 4,
            "ans_label": "Maximum bags =",
            "choice_box": "_____________ bags",
            "step_rows": [
                ("1. Subtract empty cage tare weight: 250 kg - 28 kg = 222 kg available for bags", "[M1]"),
                ("2. Divide available weight by 12 kg per bag: 222 ÷ 12 = 18.5 bags", "[P1]"),
                ("3. Round DOWN for safety: 18 full bags", "[A1]")
            ],
            "final_answer": "18 bags",
            "pitfall": "Rounding up to 19 bags (19 × 12 + 28 = 256 kg, which exceeds the 250 kg safety limit!).",
            "reverse_check": "(18 × 12 kg) + 28 kg = 216 + 28 = 244 kg ≤ 250 kg."
        },
        {
            "title": "Question 4 (Level 2 Catering Meat Joint Roasting Time)",
            "marks": 3,
            "stem": "A care home chef is roasting a beef joint weighing <strong>3.25 kg</strong>.<br>The cooking instructions state: <strong>'Roast at 190°C for 20 minutes per 500 g, plus an extra 25 minutes.'</strong><br>If the beef must come out of the oven at <strong>12:45 pm</strong>, at what time must the chef put it into the oven?",
            "lines": 4,
            "ans_label": "Oven Start Time =",
            "choice_box": "____________________",
            "step_rows": [
                ("1. Find number of 500 g (0.5 kg) units in 3.25 kg: 3.25 ÷ 0.5 = 6.5 units", "[M1]"),
                ("2. Calculate cooking time: (6.5 × 20 mins) + 25 mins = 130 + 25 = 155 minutes (2 hours 35 minutes)", "[P1]"),
                ("3. Subtract 2 hrs 35 mins from 12:45 pm: 12:45 - 2 hrs 35 mins = 10:10 am", "[A1]")
            ],
            "final_answer": "10:10 am",
            "pitfall": "Multiplying 3.25 × 20 mins instead of finding how many 500 g blocks are in 3,250 g (6.5 blocks).",
            "reverse_check": "10:10 am + 2 hrs 35 mins = 12:45 pm."
        },
        {
            "title": "Question 5 (Level 2 Delivery Van Weighbridge Axle & Payload Compliance)",
            "marks": 4,
            "stem": "A 3.5-tonne Luton delivery van has a maximum legal Gross Vehicle Weight (GVW) of <strong>3.5 tonnes</strong>.<br>• The unladen (empty) van weighs <strong>2,140 kg</strong>.<br>• The driver and passenger weigh <strong>165 kg</strong> combined, and a sack barrow weighs <strong>25 kg</strong>.<br>• The van is being loaded with <strong>28 identical crates</strong> of medical equipment, each weighing <strong>42.5 kg</strong>.<br><br>Will the fully loaded van be within the legal 3.5-tonne weight limit? Show exact figures in kilograms.",
            "lines": 5,
            "ans_label": "Decision & Loaded Weight =",
            "choice_box": "Yes / No: Total Gross Weight is _______ kg",
            "step_rows": [
                ("1. Convert 3.5 tonnes limit to kg: 3.5 × 1,000 = 3,500 kg", "[P1]"),
                ("2. Calculate weight of 28 crates: 28 × 42.5 kg = 1,190 kg", "[M1]"),
                ("3. Sum total gross weight: 2,140 (van) + 165 (crew) + 25 (barrow) + 1,190 (crates) = 3,520 kg", "[P1]"),
                ("4. Compare and conclude: 3,520 kg > 3,500 kg. No, the van is overweight by 20 kg.", "[A1]")
            ],
            "final_answer": "No, overweight by 20 kg (Total weight is 3,520 kg vs 3,500 kg limit)",
            "pitfall": "Omitting the 165 kg crew weight or 25 kg sack barrow weight.",
            "reverse_check": "3,520 - 3,500 = 20 kg over limit."
        },
        {
            "title": "Question 6 (Level 2 Paediatric Intravenous Dosage by Body Weight)",
            "marks": 4,
            "stem": "A paediatrician prescribes an intravenous medication for a child weighing <strong>44 lbs</strong>.<br>• Clinical guidelines specify a daily dosage of <strong>15 mg per kg of body weight</strong>, divided into <strong>3 equal doses</strong> per day.<br>• The medication solution has a concentration of <strong>25 mg per ml</strong>.<br>• Use: <strong>1 kg = 2.2 lbs</strong>.<br><br>How many <strong>millilitres (ml)</strong> of solution should the nurse administer for <strong>one single dose</strong>?",
            "lines": 5,
            "ans_label": "Single Dose Volume =",
            "choice_box": "_____________ ml",
            "step_rows": [
                ("1. Convert child weight from lbs to kg: 44 lbs ÷ 2.2 = 20 kg", "[P1]"),
                ("2. Calculate total daily dosage in mg: 20 kg × 15 mg/kg = 300 mg per day", "[M1]"),
                ("3. Divide by 3 for one single dose: 300 mg ÷ 3 = 100 mg per dose", "[P1]"),
                ("4. Convert 100 mg to ml using concentration (25 mg/ml): 100 ÷ 25 = 4 ml", "[A1]")
            ],
            "final_answer": "4 ml",
            "pitfall": "Giving the full daily volume (12 ml) instead of dividing by 3 for a single dose.",
            "reverse_check": "4 ml × 25 mg/ml = 100 mg/dose × 3 = 300 mg/day ÷ 20 kg = 15 mg/kg."
        }
    ),

    # 15. CAPACITY
    make_maths_topic(
        "capacity",
        "Capacity & Liquid Volume Units",
        "L1.18 • L2.20 • L2.24",
        "1 litre = 1,000 ml = 100 cl = 1,000 cm³. 1 m³ = 1,000 litres. Always convert all volumes into the same unit before dividing.",
        {
            "title": "Question 1 (Level 1 Millilitre Dispensing Cups)",
            "marks": 2,
            "stem": "A hospital catering urn holds <strong>4.5 litres</strong> of hot water.<br>How many full <strong>180 ml</strong> cups of tea can be poured from the urn?",
            "lines": 3,
            "ans_label": "Full cups =",
            "choice_box": "_____________ cups",
            "step_rows": [
                ("1. Convert 4.5 litres to millilitres: 4.5 × 1,000 = 4,500 ml", "[M1]"),
                ("2. Divide by 180 ml: 4,500 ÷ 180 = 25 cups", "[A1]")
            ],
            "final_answer": "25 cups",
            "pitfall": "Dividing 4.5 by 180 without converting litres into millilitres.",
            "reverse_check": "25 × 180 ml = 4,500 ml = 4.5 litres."
        },
        {
            "title": "Question 2 (Level 2 IV Infusion Flow Rate)",
            "marks": 2,
            "stem": "A patient is prescribed <strong>1.2 litres</strong> of saline via an intravenous drip over <strong>5 hours</strong>.<br>Calculate the required infusion pump flow rate in <strong>millilitres per hour (ml/hr)</strong>.",
            "lines": 3,
            "ans_label": "Flow Rate =",
            "choice_box": "_____________ ml/hr",
            "step_rows": [
                ("1. Convert 1.2 litres to millilitres: 1.2 × 1,000 = 1,200 ml", "[M1]"),
                ("2. Divide by 5 hours: 1,200 ÷ 5 = 240 ml/hr", "[A1]")
            ],
            "final_answer": "240 ml/hr",
            "pitfall": "Dividing 1.2 by 5 = 0.24 without converting to millilitres.",
            "reverse_check": "240 ml/hr × 5 hours = 1,200 ml = 1.2 L."
        },
        {
            "title": "Question 3 (Level 1 Disinfectant Dilution Ratio & Capacity)",
            "marks": 3,
            "stem": "A domestic supervisor mixes surface sanitiser using concentrate and water in the ratio <strong>1 : 9</strong>.<br>She needs to fill <strong>8 spray bottles</strong>, each with a capacity of <strong>750 ml</strong>.<br><br>How many <strong>millilitres (ml)</strong> of neat concentrate does she need in total?",
            "lines": 4,
            "ans_label": "Concentrate needed =",
            "choice_box": "_____________ ml",
            "step_rows": [
                ("1. Total mixed solution required: 8 × 750 ml = 6,000 ml", "[M1]"),
                ("2. Total ratio parts: 1 + 9 = 10 parts", "[P1]"),
                ("3. Concentrate (1 part): 6,000 ml ÷ 10 = 600 ml", "[A1]")
            ],
            "final_answer": "600 ml",
            "pitfall": "Dividing 6,000 ml by 9 instead of 10 total parts.",
            "reverse_check": "600 ml concentrate + 5,400 ml water = 6,000 ml = 8 × 750 ml."
        },
        {
            "title": "Question 4 (Level 2 3D Cuboid Tank Volume to Litres)",
            "marks": 3,
            "stem": "A stainless-steel ultrasonic cleaning bath is a cuboid measuring <strong>50 cm long, 30 cm wide, and 24 cm deep</strong>.<br>For safe operation, the bath is filled to <strong>75% of its total depth</strong>.<br>Use: <strong>1,000 cm³ = 1 litre</strong>.<br><br>How many <strong>litres</strong> of cleaning fluid are needed?",
            "lines": 4,
            "ans_label": "Cleaning fluid =",
            "choice_box": "_____________ litres",
            "step_rows": [
                ("1. Calculate full volume (or 75% depth = 18 cm): 50 × 30 × 24 = 36,000 cm³", "[M1]"),
                ("2. Calculate 75% volume: 36,000 × 0.75 = 27,000 cm³", "[P1]"),
                ("3. Convert cm³ to litres (÷ 1,000): 27,000 ÷ 1,000 = 27 litres", "[A1]")
            ],
            "final_answer": "27 litres",
            "pitfall": "Forgetting to multiply by 75% (giving 36 litres).",
            "reverse_check": "50 cm × 30 cm × 18 cm (75% of 24 cm) = 27,000 cm³ = 27 L."
        },
        {
            "title": "Question 5 (Level 2 Ward 24-Hour Patient Fluid Balance Audit)",
            "marks": 4,
            "stem": "A nurse completes a 24-hour fluid balance chart for a post-operative patient:<br>• <strong>Fluid Intake:</strong> Two <strong>1.25-litre</strong> IV saline bags; <strong>3 cups</strong> of water (<strong>220 ml</strong> each); <strong>1 bowl</strong> of soup (<strong>300 ml</strong>).<br>• <strong>Fluid Output:</strong> Morning urine <strong>850 ml</strong>; Afternoon urine <strong>920 ml</strong>; Overnight catheter bag <strong>1.15 litres</strong>; Surgical wound drain <strong>180 ml</strong>.<br><br>Calculate the patient's net fluid balance in <strong>millilitres (ml)</strong> (Intake minus Output) and state whether it is positive or negative.",
            "lines": 5,
            "ans_label": "Net Fluid Balance =",
            "choice_box": "+ / - _____________ ml",
            "step_rows": [
                ("1. Convert and sum Intake in ml: (2 × 1,250) + (3 × 220) + 300 = 2,500 + 660 + 300 = 3,460 ml", "[P1]"),
                ("2. Convert and sum Output in ml: 850 + 920 + 1,150 + 180 = 3,100 ml", "[P1]"),
                ("3. Subtract Output from Intake: 3,460 - 3,100 = +360 ml", "[M1]"),
                ("4. State final balance: +360 ml (Positive fluid balance of 360 ml)", "[A1]")
            ],
            "final_answer": "+360 ml (Positive fluid balance: 3,460 ml intake vs 3,100 ml output)",
            "pitfall": "Counting only one 1.25 L saline bag or forgetting to convert 1.15 L to 1,150 ml.",
            "reverse_check": "3,100 ml + 360 ml = 3,460 ml."
        },
        {
            "title": "Question 6 (Level 2 Cylindrical Heating Oil Tank Refill Budget)",
            "marks": 4,
            "stem": "A rural care home has a cylindrical heating oil tank with a <strong>diameter of 1.6 metres</strong> and a <strong>length of 2.5 metres</strong>.<br>• The tank is currently <strong>1/4 full</strong>.<br>• The manager orders enough oil to fill the tank to <strong>90% of its total capacity</strong>.<br>• Heating oil costs <strong>68p per litre</strong>.<br>• Use <strong>π = 3.14</strong> and <strong>1 m³ = 1,000 litres</strong>.<br><br>Calculate the cost of the heating oil order. Give your answer to the nearest penny.",
            "lines": 5,
            "ans_label": "Heating Oil Order Cost =",
            "choice_box": "£ ____________________",
            "step_rows": [
                ("1. Radius = 1.6 ÷ 2 = 0.8 m. Full tank volume = 3.14 × 0.8² × 2.5 = 3.14 × 0.64 × 2.5 = 5.024 m³ = 5,024 litres", "[P1]"),
                ("2. Percentage of capacity to add: 90% - 25% (1/4) = 65% of full capacity", "[M1]"),
                ("3. Litres required: 5,024 × 0.65 = 3,265.6 litres", "[P1]"),
                ("4. Total cost at £0.68/L: 3,265.6 × £0.68 = £2,220.608 → £2,220.61", "[A1]")
            ],
            "final_answer": "£2,220.61 (3,265.6 litres needed)",
            "pitfall": "Using diameter (1.6 m) instead of radius (0.8 m) in the cylinder volume formula.",
            "reverse_check": "90% of 5,024 L = 4,521.6 L; 25% = 1,256 L; 4,521.6 - 1,256 = 3,265.6 L × £0.68 = £2,220.61."
        }
    ),

    # 16. SURFACE AREA
    make_maths_topic(
        "surface-area",
        "Surface Area of Prisms & Cylinders",
        "L2.24 • L2.25",
        "Surface Area is the total 2D area of all outer faces (in cm² or m²). For a closed cuboid: 2(LW) + 2(LH) + 2(WH). Always check if the container has an open top or unpainted base!",
        {
            "title": "Question 1 (Level 2 Cube Surface Area)",
            "marks": 2,
            "stem": "A sterile instrument storage box is a closed <strong>cube</strong> with side length <strong>30 cm</strong>.<br>Calculate the total external surface area of the cube in <strong>cm²</strong>.",
            "lines": 3,
            "ans_label": "Total Surface Area =",
            "choice_box": "_____________ cm²",
            "step_rows": [
                ("1. Area of 1 square face: 30 cm × 30 cm = 900 cm²", "[M1]"),
                ("2. Multiply by 6 identical faces: 6 × 900 cm² = 5,400 cm²", "[A1]")
            ],
            "final_answer": "5,400 cm²",
            "pitfall": "Calculating volume (30 × 30 × 30 = 27,000 cm³) instead of surface area.",
            "reverse_check": "5,400 ÷ 6 = 900 cm²; √900 = 30 cm."
        },
        {
            "title": "Question 2 (Level 2 Closed Cuboid Packaging Carton)",
            "marks": 2,
            "stem": "A pharmaceutical shipping carton is a closed cuboid measuring <strong>50 cm long, 40 cm wide, and 20 cm high</strong>.<br>Calculate the total external surface area of the carton in <strong>cm²</strong>.",
            "lines": 3,
            "ans_label": "Total Surface Area =",
            "choice_box": "_____________ cm²",
            "step_rows": [
                ("1. Pairs of faces: 2×(50×40) + 2×(50×20) + 2×(40×20) = 4,000 + 2,000 + 1,600", "[M1]"),
                ("2. Sum all 6 faces: 7,600 cm²", "[A1]")
            ],
            "final_answer": "7,600 cm²",
            "pitfall": "Adding only 3 faces (2,000 + 1,000 + 800 = 3,800 cm²) and forgetting to double them for all 6 faces.",
            "reverse_check": "(2,000 + 1,000 + 800) × 2 = 3,800 × 2 = 7,600 cm²."
        },
        {
            "title": "Question 3 (Level 2 Open-Top Steel Tank Coating)",
            "marks": 3,
            "stem": "An industrial water trough is an <strong>open-top cuboid</strong> (4 vertical sides and 1 flat base; <strong>no lid</strong>) measuring <strong>2.5 m long, 1.2 m wide, and 0.8 m high</strong>.<br><br>Calculate the total external surface area of the 5 faces in <strong>m²</strong>.",
            "lines": 4,
            "ans_label": "5-Face Surface Area =",
            "choice_box": "_____________ m²",
            "step_rows": [
                ("1. Base area (1 face only): 2.5 m × 1.2 m = 3.0 m²", "[M1]"),
                ("2. Front & Back walls: 2 × (2.5 × 0.8) = 4.0 m²; Left & Right ends: 2 × (1.2 × 0.8) = 1.92 m²", "[P1]"),
                ("3. Sum all 5 faces: 3.0 + 4.0 + 1.92 = 8.92 m²", "[A1]")
            ],
            "final_answer": "8.92 m²",
            "pitfall": "Including a top lid (2 × 3.0 = 6.0 m²) to get 11.92 m² when the trough is open-topped.",
            "reverse_check": "Full 6-face cuboid = 11.92 m² minus 3.0 m² open top = 8.92 m²."
        },
        {
            "title": "Question 4 (Level 2 Cylindrical Pillar Painting)",
            "marks": 3,
            "stem": "A hospital atrium has <strong>4 concrete support pillars</strong>. Each pillar is a cylinder with a <strong>diameter of 0.6 metres</strong> and a <strong>height of 3.5 metres</strong>.<br>Only the <strong>curved vertical surface</strong> of each pillar is painted (not the top or bottom ends).<br>Use <strong>π = 3.14</strong>.<br><br>Calculate the total curved surface area to be painted across all 4 pillars in <strong>m²</strong>.",
            "lines": 4,
            "ans_label": "Total Curved Area =",
            "choice_box": "_____________ m²",
            "step_rows": [
                ("1. Curved surface area of 1 cylinder (π × d × h): 3.14 × 0.6 × 3.5", "[M1]"),
                ("2. Evaluate 1 pillar: 6.594 m²", "[P1]"),
                ("3. Multiply by 4 pillars: 4 × 6.594 = 26.376 m² (accept 26.38 m²)", "[A1]")
            ],
            "final_answer": "26.376 m² (or 26.38 m²)",
            "pitfall": "Adding circular top/bottom areas (2πr²) when the pillars touch the floor and ceiling.",
            "reverse_check": "26.376 ÷ 4 = 6.594; 6.594 ÷ 3.5 ÷ 0.6 = 3.14."
        },
        {
            "title": "Question 5 (Level 2 Room Walls & Ceiling Plasterboard & Paint Cost)",
            "marks": 4,
            "stem": "A decorator is painting the <strong>4 walls and the ceiling</strong> (not the floor) of a rectangular clinic room measuring <strong>6.0 m long, 4.5 m wide, and 2.8 m high</strong>.<br>• The room has a door and window with a combined area of <strong>5.8 m²</strong> (which are not painted).<br>• The walls and ceiling require <strong>2 coats</strong> of hygienic scrubbable paint.<br>• Each 5-litre tin of paint covers <strong>40 m²</strong> and costs <strong>£34.50</strong>.<br><br>Calculate the total cost of the paint tins required.",
            "lines": 5,
            "ans_label": "Total Paint Cost =",
            "choice_box": "£ ____________________",
            "step_rows": [
                ("1. Ceiling area = 6.0 × 4.5 = 27.0 m²; 4 walls = 2×(6.0×2.8) + 2×(4.5×2.8) = 33.6 + 25.2 = 58.8 m²", "[P1]"),
                ("2. Net paintable area (1 coat): 27.0 + 58.8 - 5.8 (door/window) = 80.0 m²", "[M1]"),
                ("3. Area for 2 coats: 80.0 × 2 = 160.0 m² → Tins needed: 160 ÷ 40 = 4 tins", "[P1]"),
                ("4. Total cost: 4 × £34.50 = £138.00", "[A1]")
            ],
            "final_answer": "£138.00 (4 tins required for 160 m²)",
            "pitfall": "Forgetting to double the net area for 2 coats of paint.",
            "reverse_check": "4 tins × 40 m² = 160 m² ÷ 2 coats = 80 m² net area."
        },
        {
            "title": "Question 6 (Level 2 Triangular Prism Roof Tent Canvas Verification)",
            "marks": 4,
            "stem": "An emergency medical triage tent is shaped as a <strong>triangular prism</strong> (including a sewn-in groundsheet base):<br>• Length of tent: <strong>8.0 m</strong><br>• Width of flat groundsheet base: <strong>6.0 m</strong><br>• Vertical height from ground to ridge: <strong>4.0 m</strong><br>• Sloping roof sides: two rectangles each measuring <strong>8.0 m long by 5.0 m wide</strong>.<br><br>The manufacturer has <strong>180 m²</strong> of waterproof canvas in stock. If <strong>10% extra canvas</strong> must be added to the total surface area for seams and wastage, is 180 m² of canvas enough to make the tent?",
            "lines": 5,
            "ans_label": "Decision & Canvas Needed =",
            "choice_box": "Yes / No: Total canvas required is _______ m²",
            "step_rows": [
                ("1. Two triangular end faces (2 × 1/2 × base × height): 2 × (0.5 × 6.0 × 4.0) = 24.0 m²", "[P1]"),
                ("2. Three rectangular faces (2 sloping roof sides + 1 base): 2×(8.0×5.0) + (8.0×6.0) = 80.0 + 48.0 = 128.0 m²", "[P1]"),
                ("3. Total surface area = 24.0 + 128.0 = 152.0 m²; plus 10% wastage: 152.0 × 1.10 = 167.2 m²", "[M1]"),
                ("4. Compare and conclude: 167.2 m² ≤ 180 m². Yes, 180 m² of canvas is enough (with 12.8 m² to spare).", "[A1]")
            ],
            "final_answer": "Yes (Requires 167.2 m² including 10% wastage, which is under the 180 m² available)",
            "pitfall": "Using the 5.0 m sloping edge as the vertical height of the triangle instead of 4.0 m.",
            "reverse_check": "24 + 80 + 48 = 152 m²; 152 + 15.2 = 167.2 m² < 180 m²."
        }
    ),

    # 17. PERIMETER
    make_maths_topic(
        "perimeter",
        "Perimeter & Compound Shapes",
        "E3.8 • L1.22 • L2.24",
        "Perimeter is the total distance all the way around the outside boundary of a 2D shape. Always find any missing horizontal or vertical step lengths BEFORE adding the sides together!",
        {
            "title": "Question 1 (Level 1 Rectangular Perimeter)",
            "marks": 2,
            "stem": "A rectangular hospital sensory garden measures <strong>18.5 metres long</strong> by <strong>11.2 metres wide</strong>.<br>Calculate the total perimeter of the garden.",
            "lines": 3,
            "ans_label": "Perimeter =",
            "choice_box": "_____________ m",
            "step_rows": [
                ("1. Apply Perimeter = 2 × (Length + Width): 2 × (18.5 + 11.2) = 2 × 29.7", "[M1]"),
                ("2. Evaluate: 59.4 m", "[A1]")
            ],
            "final_answer": "59.4 m",
            "pitfall": "Multiplying 18.5 × 11.2 (= 207.2 m² area) instead of adding all four sides.",
            "reverse_check": "18.5 + 11.2 + 18.5 + 11.2 = 59.4 m."
        },
        {
            "title": "Question 2 (Level 2 Finding Missing Width from Known Perimeter)",
            "marks": 2,
            "stem": "A rectangular physiotherapy exercise mat has a total perimeter of <strong>16.4 metres</strong>.<br>The length of the mat is <strong>5.4 metres</strong>.<br>Calculate the width of the mat.",
            "lines": 3,
            "ans_label": "Width =",
            "choice_box": "_____________ m",
            "step_rows": [
                ("1. Subtract both lengths from perimeter: 16.4 - (2 × 5.4) = 16.4 - 10.8 = 5.6 m (or halve perimeter: 8.2 - 5.4)", "[M1]"),
                ("2. Divide remaining length by 2: 5.6 ÷ 2 = 2.8 m", "[A1]")
            ],
            "final_answer": "2.8 m",
            "pitfall": "Subtracting only one length (16.4 - 5.4 = 11.0 m) instead of two lengths.",
            "reverse_check": "2 × (5.4 + 2.8) = 2 × 8.2 = 16.4 m."
        },
        {
            "title": "Question 3 (Level 1/2 L-Shaped Ward Floor Perimeter)",
            "marks": 3,
            "stem": "The diagram below shows an L-shaped clinical reception floor.<br>Work out the missing side lengths <strong>a</strong> and <strong>b</strong>, and calculate the <strong>total perimeter</strong> of the floor.",
            "svg": get_svg_for_topic("perimeter"),
            "lines": 4,
            "ans_label": "Total Perimeter =",
            "choice_box": "_____________ m (a = _____ m, b = _____ m)",
            "step_rows": [
                ("1. Find missing vertical side a: 10.2 m - 4.8 m = 5.4 m", "[M1]"),
                ("2. Find missing horizontal side b: 12.5 m - 5.5 m = 7.0 m", "[M1]"),
                ("3. Sum all 6 sides: 12.5 + 4.8 + 5.5 + 5.4 + 7.0 + 10.2 = 45.4 m", "[A1]")
            ],
            "final_answer": "45.4 m (a = 5.4 m, b = 7.0 m)",
            "pitfall": "Adding only the 4 printed numbers (12.5 + 4.8 + 5.5 + 10.2 = 33.0 m) and omitting sides a and b.",
            "reverse_check": "Outer bounding box perimeter = 2 × (12.5 + 10.2) = 2 × 22.7 = 45.4 m."
        },
        {
            "title": "Question 4 (Level 2 Skirting Board Packs with Doorway Deduction)",
            "marks": 3,
            "stem": "A joiner is fitting timber skirting board around a rectangular treatment room measuring <strong>6.4 m long by 4.2 m wide</strong>.<br>• The room has two doorways measuring <strong>0.9 m</strong> and <strong>1.1 m</strong> wide (which do not require skirting board).<br>• Skirting board is sold in <strong>2.4-metre lengths</strong> (offcuts can be used on straight walls).<br><br>How many 2.4-metre lengths of skirting board must the joiner purchase?",
            "lines": 4,
            "ans_label": "Lengths needed =",
            "choice_box": "_____________ lengths",
            "step_rows": [
                ("1. Full room perimeter: 2 × (6.4 + 4.2) = 21.2 m", "[M1]"),
                ("2. Deduct both doorways: 21.2 - (0.9 + 1.1) = 19.2 m net skirting required", "[P1]"),
                ("3. Divide by 2.4 m pack length: 19.2 ÷ 2.4 = 8 lengths", "[A1]")
            ],
            "final_answer": "8 lengths",
            "pitfall": "Forgetting to subtract the two doorway widths (21.2 ÷ 2.4 = 8.83 → 9 lengths).",
            "reverse_check": "8 × 2.4 m = 19.2 m + 2.0 m doorways = 21.2 m."
        },
        {
            "title": "Question 5 (Level 2 Semi-Circular Courtyard Edging Cost)",
            "marks": 4,
            "stem": "A hospital wellbeing courtyard is shaped as a <strong>rectangle with a semi-circle</strong> joined to one end:<br>• The rectangular section has two long parallel sides of <strong>15.0 metres</strong> each, and one straight end wall of <strong>8.0 metres</strong>.<br>• The opposite end is a <strong>semi-circle of diameter 8.0 metres</strong>.<br>• Flexible steel lawn edging is installed around the entire outer boundary.<br>• Edging is sold in <strong>5-metre rolls</strong> at <strong>£24.50 per roll</strong>. Use <strong>π = 3.14</strong>.<br><br>Calculate the total cost of the steel edging rolls required.",
            "lines": 5,
            "ans_label": "Total Edging Cost =",
            "choice_box": "£ ____________________",
            "step_rows": [
                ("1. Curved semi-circular arc length (1/2 × π × d): 0.5 × 3.14 × 8.0 = 12.56 m", "[P1]"),
                ("2. Add the 3 straight outer sides: 12.56 + 15.0 + 15.0 + 8.0 = 50.56 m total perimeter", "[M1]"),
                ("3. Calculate 5 m rolls needed: 50.56 ÷ 5 = 10.112 → round UP to 11 whole rolls", "[P1]"),
                ("4. Total cost: 11 × £24.50 = £269.50", "[A1]")
            ],
            "final_answer": "£269.50 (11 rolls required for 50.56 m perimeter)",
            "pitfall": "Including the internal 8.0 m dashed join line inside the courtyard, or rounding 10.112 rolls down to 10 rolls.",
            "reverse_check": "10 rolls = 50 m (short by 0.56 m). 11 rolls × £24.50 = £269.50."
        },
        {
            "title": "Question 6 (Level 2 Security Fencing Posts & Panels Budget Verification)",
            "marks": 4,
            "stem": "A medical oxygen storage compound is a rectangle measuring <strong>14 m long by 10 m wide</strong>.<br>• Security fencing is erected around all four sides, except for a <strong>4-metre</strong> security gate opening on one wall.<br>• Fence panels are <strong>2 metres wide</strong> and cost <strong>£42.00 each</strong>.<br>• A steel fence post (costing <strong>£18.00 each</strong>) is required at both ends of the fence and between every adjacent panel (so the number of posts is <strong>1 more than the number of panels</strong>).<br>• The security gate itself costs <strong>£310.00</strong>.<br><br>The estates manager has a total materials budget of <strong>£1,700.00</strong>. Is the budget sufficient?",
            "lines": 5,
            "ans_label": "Decision & Total Cost =",
            "choice_box": "Yes / No: Total cost is £ ____________",
            "step_rows": [
                ("1. Total perimeter = 2 × (14 + 10) = 48 m; Net fencing length = 48 m - 4 m gate = 44 m", "[P1]"),
                ("2. Number of 2 m panels = 44 ÷ 2 = 22 panels; Number of posts = 22 + 1 = 23 posts", "[M1]"),
                ("3. Calculate total cost: (22 × £42.00) + (23 × £18.00) + £310.00 = £924.00 + £414.00 + £310.00 = £1,648.00", "[P1]"),
                ("4. Compare and conclude: £1,648.00 ≤ £1,700.00. Yes, the budget is sufficient with £52.00 remaining.", "[A1]")
            ],
            "final_answer": "Yes, sufficient (Total cost is £1,648.00, leaving £52.00 under the £1,700 budget)",
            "pitfall": "Using 22 posts instead of 23 posts, or forgetting to deduct the 4 m gate before dividing by 2 m.",
            "reverse_check": "£924 + £414 + £310 = £1,648; £1,700 - £1,648 = £52 surplus."
        }
    )
]

if __name__ == "__main__":
    print(f"Loaded {len(WORKSHEETS_MATHS_PART1)} bespoke Maths Part 1 worksheets.")
