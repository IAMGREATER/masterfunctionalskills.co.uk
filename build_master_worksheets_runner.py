#!/usr/bin/env python3
"""
Master Functional Skills - Master Worksheet & Answer Suite Generator.
Generates all worksheets and answers into worksheets/ and links them to topic revision pages.
"""
import os, sys, glob, re
from worksheet_templates import render_worksheet, render_answers
from generate_all_worksheets_complete import get_svg_for_topic

WORK_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"
WORKSHEETS_DIR = os.path.join(WORK_DIR, "worksheets")
os.makedirs(WORKSHEETS_DIR, exist_ok=True)

# Full Curriculum Topic Registry
TOPIC_CATALOG = [
    # --- MATHS NUMBER & CALCULATION ---
    {
        "slug": "fractions",
        "title": "Fractions",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.7 • L2.6 • L2.7",
        "formula_hint": "To find a fraction of an amount: divide by the denominator (bottom), then multiply by the numerator (top). When adding or subtracting, always find a common denominator first.",
        "back_url": "../functional-skills-fractions.html",
        "total_marks": 18,
        "sections": [
            {
                "title": "Section A: Procedural Fluency Check",
                "meta": "Questions 1 & 2 • 4 Marks",
                "questions": [
                    {
                        "title": "Question 1 (Level 1 Simplifying)",
                        "marks": 2,
                        "stem": "Simplify the fraction <strong>36/48</strong> to its simplest form.",
                        "lines": 3,
                        "ans_label": "Simplest form =",
                        "choice_box": "____________________",
                        "step_rows": [
                            ("1. Identify Highest Common Factor (HCF = 12) or divide by 2, 3, 4", "[M1]"),
                            ("2. 36 ÷ 12 = 3; 48 ÷ 12 = 4; Result: 3/4", "[A1]")
                        ],
                        "final_answer": "3/4",
                        "pitfall": "Stopping at 18/24 or 9/12 without reducing to lowest terms.",
                        "reverse_check": "3/4 × 12/12 = 36/48."
                    },
                    {
                        "title": "Question 2 (Level 2 Adding Mixed Numbers)",
                        "marks": 2,
                        "stem": "Work out: <strong>2 1/3 + 1 3/4</strong>.<br>Give your answer as a mixed number in its simplest form.",
                        "lines": 3,
                        "ans_label": "Sum =",
                        "choice_box": "____________________",
                        "step_rows": [
                            ("1. Convert to improper: 7/3 + 7/4. Common denominator 12: 28/12 + 21/12 = 49/12", "[M1]"),
                            ("2. Convert to mixed number: 49 ÷ 12 = 4 remainder 1; Result: 4 1/12", "[A1]")
                        ],
                        "final_answer": "4 1/12",
                        "pitfall": "Adding numerators and denominators directly (3 4/7). Denominators must be matched!",
                        "reverse_check": "4 1/12 - 1 3/4 = 49/12 - 21/12 = 28/12 = 7/3 = 2 1/3."
                    }
                ]
            },
            {
                "title": "Section B: Workplace & Functional Scenarios",
                "meta": "Questions 3 & 4 • 6 Marks",
                "questions": [
                    {
                        "title": "Question 3 (Level 1 Hospital Pharmacy Dispatches)",
                        "marks": 3,
                        "stem": "A central hospital pharmacy stocks <strong>720 vials</strong> of specialized antibiotic.<br>• <strong>3/8</strong> of the vials are dispatched to Pediatric Intensive Care.<br>• <strong>2/5</strong> of the vials are dispatched to Emergency Assessment.<br><br>How many vials remain in central pharmacy stock?",
                        "lines": 4,
                        "ans_label": "Remaining vials =",
                        "choice_box": "_____________ vials",
                        "step_rows": [
                            ("1. PICU dispatches: 720 ÷ 8 = 90; 90 × 3 = 270 vials", "[M1]"),
                            ("2. Emergency dispatches: 720 ÷ 5 = 144; 144 × 2 = 288 vials", "[M1]"),
                            ("3. Remaining stock: 720 - (270 + 288) = 720 - 558 = 162 vials", "[A1]")
                        ],
                        "final_answer": "162 vials",
                        "pitfall": "Calculating 3/8 and 2/5 of remaining stock rather than original 720 vials.",
                        "reverse_check": "270 + 288 + 162 = 720 vials."
                    },
                    {
                        "title": "Question 4 (Level 2 Apprentice Construction Timber Cut)",
                        "marks": 3,
                        "stem": "A site carpenter cuts roof struts from a <strong>4.8 metre</strong> timber beam.<br>The first strut requires <strong>1 1/4 metres</strong>, the second requires <strong>1 3/5 metres</strong>, and <strong>1/10 metre</strong> is lost as saw cut waste.<br><br>Calculate the exact length of timber remaining on the beam. Give your answer as a decimal in metres.",
                        "lines": 4,
                        "ans_label": "Remaining timber =",
                        "choice_box": "_____________ m",
                        "step_rows": [
                            ("1. Convert to decimals or common denominator: 1 1/4 = 1.25 m; 1 3/5 = 1.60 m; 1/10 = 0.10 m", "[M1]"),
                            ("2. Sum used timber: 1.25 + 1.60 + 0.10 = 2.95 m", "[P1]"),
                            ("3. Subtract from total: 4.80 - 2.95 = 1.85 m", "[A1]")
                        ],
                        "final_answer": "1.85 m",
                        "pitfall": "Forgetting the 1/10 m saw waste, yielding 1.95 m.",
                        "reverse_check": "1.85 + 2.95 = 4.80 m."
                    }
                ]
            },
            {
                "title": "Section C: Pearson Edexcel Problem Solving & Justification",
                "meta": "Questions 5 & 6 • 8 Marks",
                "questions": [
                    {
                        "title": "Question 5 (Level 2 Ward Dietary Survey)",
                        "marks": 4,
                        "stem": "In an acute medical unit with <strong>96 patients</strong>:<br>• <strong>5/12</strong> require diabetic meal plans.<br>• <strong>1/4</strong> require low-sodium meal plans.<br>• <strong>1/6</strong> require texture-modified soft diets.<br>• The remaining patients receive standard hospital meals.<br><br>How many patients receive standard hospital meals?",
                        "lines": 5,
                        "ans_label": "Standard meals =",
                        "choice_box": "_____________ patients",
                        "step_rows": [
                            ("1. Diabetic: 96 ÷ 12 = 8; 8 × 5 = 40 patients", "[P1]"),
                            ("2. Low-sodium: 96 ÷ 4 = 24 patients; Soft diet: 96 ÷ 6 = 16 patients", "[P1]"),
                            ("3. Sum special diets: 40 + 24 + 16 = 80 patients", "[M1]"),
                            ("4. Standard meals: 96 - 80 = 16 patients", "[A1]")
                        ],
                        "final_answer": "16 patients",
                        "pitfall": "Adding fractions incorrectly without finding a common denominator (12).",
                        "reverse_check": "40 + 24 + 16 + 16 = 96 patients."
                    },
                    {
                        "title": "Question 6 (Level 2 Trust Target Justification)",
                        "marks": 4,
                        "stem": "A community trust aims for at least <strong>7/10</strong> of all clinical incident reviews to be completed within 14 days.<br>Last month, <strong>185 out of 250</strong> incident reviews were completed within 14 days.<br>The quality manager claims: <em>'We achieved our target fraction with room to spare.'</em><br><br>Is the quality manager correct?<br>Show full step-by-step working and state a clear conclusion with your reasoning.",
                        "lines": 5,
                        "ans_label": "Conclusion & Comparison =",
                        "choice_box": "Yes / No: Actual fraction is _______ vs Target 7/10",
                        "step_rows": [
                            ("1. Calculate target reviews: 7/10 of 250 = (250 ÷ 10) × 7 = 175 reviews", "[M1]"),
                            ("2. Or convert actual to decimal/percentage: 185 ÷ 250 = 0.74 (74%)", "[P1]"),
                            ("3. Compare target against actual: 74% > 70% (or 185 > 175)", "[M1]"),
                            ("4. Conclude: <strong>Yes, the manager is correct</strong>. The trust achieved 74% (185 reviews), exceeding the 70% target (175 reviews) by 10 reviews.", "[A1]")
                        ],
                        "final_answer": "Yes, correct (Achieved 74% / 185 reviews vs target 70% / 175 reviews)",
                        "pitfall": "Stating 'Yes' without calculating either the 7/10 count (175) or the 74% decimal comparison.",
                        "reverse_check": "185/250 = 37/50 = 74/100 = 0.74. Target 7/10 = 0.70. 0.74 > 0.70."
                    }
                ]
            }
        ]
    },
    {
        "slug": "decimals",
        "title": "Decimals",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: E3.5 • L1.8 • L2.8",
        "formula_hint": "Align numbers strictly by the decimal point when adding or subtracting. When multiplying decimals, multiply as whole numbers and place the total count of decimal digits back into the product.",
        "back_url": "../functional-skills-decimals.html",
        "total_marks": 18,
        "sections": [
            {
                "title": "Section A: Procedural Fluency Check",
                "meta": "Questions 1 & 2 • 4 Marks",
                "questions": [
                    {
                        "title": "Question 1 (Level 1 Decimal Addition)",
                        "marks": 2,
                        "stem": "Work out: <strong>48.65 + 7.9 + 134.08</strong>.",
                        "lines": 3,
                        "ans_label": "Sum =",
                        "choice_box": "____________________",
                        "step_rows": [
                            ("1. Align decimal points vertically with placeholder zeroes: 48.65 + 07.90 + 134.08", "[M1]"),
                            ("2. Accurate addition: 190.63", "[A1]")
                        ],
                        "final_answer": "190.63",
                        "pitfall": "Misaligning 7.9 with the hundredths column, calculating 48.65 + 7.09 + 134.08.",
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
                            ("1. Multiply numerator and denominator by 100 to make divisor whole: 1,470 ÷ 3", "[M1]"),
                            ("2. 1,470 ÷ 3 = 490", "[A1]")
                        ],
                        "final_answer": "490",
                        "pitfall": "Dividing 14.7 by 3 to get 4.9 without adjusting place value for 0.03.",
                        "reverse_check": "490 × 0.03 = 14.7."
                    }
                ]
            },
            {
                "title": "Section B: Workplace & Functional Scenarios",
                "meta": "Questions 3 & 4 • 6 Marks",
                "questions": [
                    {
                        "title": "Question 3 (Level 1 Medical Dosage Administration)",
                        "marks": 3,
                        "stem": "A nurse administers liquid analgesic at a dosage of <strong>3.75 ml</strong> per patient.<br>The medication bottle contains <strong>90 ml</strong>.<br><br>How many full patient doses are contained in the bottle?",
                        "lines": 4,
                        "ans_label": "Full doses =",
                        "choice_box": "_____________ doses",
                        "step_rows": [
                            ("1. Division method: 90 ÷ 3.75 (or 9,000 ÷ 375)", "[M1]"),
                            ("2. Simplify: 9,000 ÷ 375 = 24", "[P1]"),
                            ("3. State 24 full doses", "[A1]")
                        ],
                        "final_answer": "24 doses",
                        "pitfall": "Arithmetic slip when dividing decimals by hand.",
                        "reverse_check": "24 × 3.75 ml = 90 ml."
                    },
                    {
                        "title": "Question 4 (Level 2 Fuel Consumption & Cost)",
                        "marks": 3,
                        "stem": "A healthcare visitor travels <strong>348.5 miles</strong> across a rural community district.<br>Their hybrid car consumes <strong>0.082 litres</strong> of petrol per mile.<br>Petrol costs <strong>£1.45 per litre</strong>.<br><br>Work out the total fuel cost for the trip. Give your answer to the nearest penny.",
                        "lines": 5,
                        "ans_label": "Total Fuel Cost =",
                        "choice_box": "£ ____________________",
                        "step_rows": [
                            ("1. Calculate total fuel used: 348.5 × 0.082 = 28.577 litres", "[M1]"),
                            ("2. Multiply by fuel price: 28.577 × £1.45 = £41.43665", "[P1]"),
                            ("3. Round to 2 decimal places (nearest penny): £41.44", "[A1]")
                        ],
                        "final_answer": "£41.44",
                        "pitfall": "Premature rounding of intermediate fuel litres to 28.6 L before multiplying by £1.45.",
                        "reverse_check": "£41.44 ÷ £1.45 ≈ 28.58 L; 28.58 ÷ 348.5 ≈ 0.082 L/mile."
                    }
                ]
            },
            {
                "title": "Section C: Pearson Edexcel Problem Solving & Justification",
                "meta": "Questions 5 & 6 • 8 Marks",
                "questions": [
                    {
                        "title": "Question 5 (Level 2 Chemical Water Purification)",
                        "marks": 4,
                        "stem": "A hydrotherapy pool contains <strong>45,000 litres</strong> of water.<br>Water safety regulations require adding <strong>0.0035 litres</strong> of sanitising concentrate for every 100 litres of pool water.<br>Sanitising concentrate is sold in <strong>0.5 litre bottles</strong> at <strong>£18.20 per bottle</strong>.<br><br>How much does it cost to purchase enough concentrate for one complete pool treatment?",
                        "lines": 5,
                        "ans_label": "Total Cost =",
                        "choice_box": "£ ____________________",
                        "step_rows": [
                            ("1. Find hundreds of litres: 45,000 ÷ 100 = 450 units", "[P1]"),
                            ("2. Calculate required concentrate: 450 × 0.0035 = 1.575 litres", "[M1]"),
                            ("3. Find bottles needed: 1.575 ÷ 0.5 = 3.15 bottles → round UP to 4 whole bottles", "[P1]"),
                            ("4. Total cost: 4 × £18.20 = £72.80", "[A1]")
                        ],
                        "final_answer": "£72.80",
                        "pitfall": "Calculating 3.15 × £18.20 = £57.33, forgetting that bottles cannot be purchased in fractions.",
                        "reverse_check": "3 bottles = 1.5 L (insufficient for 1.575 L). 4 bottles required: 4 × £18.20 = £72.80."
                    },
                    {
                        "title": "Question 6 (Level 2 Precision Tolerance Evaluation)",
                        "marks": 4,
                        "stem": "An orthopedic implant pin must have a target diameter of <strong>4.50 mm</strong> with an allowable manufacturing tolerance of <strong>±0.04 mm</strong> (acceptable between 4.46 mm and 4.54 mm).<br>A batch inspector tests 4 sample pins: <strong>4.45 mm, 4.48 mm, 4.53 mm, 4.55 mm</strong>.<br><br>The quality controller claims: <em>'At least 75% of the inspected pins are within the safety tolerance.'</em><br><br>Is the quality controller's claim correct?<br>Show your evaluation of each pin, state which pins pass/fail, and give a clear conclusion.",
                        "lines": 5,
                        "ans_label": "Decision & Pass Rate =",
                        "choice_box": "Correct / Incorrect: Pass rate is _____ %",
                        "step_rows": [
                            ("1. Check tolerance bounds: 4.50 - 0.04 = 4.46 mm; 4.50 + 0.04 = 4.54 mm", "[P1]"),
                            ("2. Evaluate samples: 4.45 mm (< 4.46, FAIL); 4.48 mm (PASS); 4.53 mm (PASS); 4.55 mm (> 4.54, FAIL)", "[M1]"),
                            ("3. Calculate pass rate: 2 out of 4 pins pass = 2/4 = 50%", "[P1]"),
                            ("4. Conclude: <strong>No / Incorrect</strong>; only 50% of the pins are within tolerance, which is less than the claimed 75%.", "[A1]")
                        ],
                        "final_answer": "Incorrect (Only 50% pass tolerance, which is below 75%)",
                        "pitfall": "Assuming 4.45 mm passes because it rounds to 4.5 mm.",
                        "reverse_check": "2 out of 4 = 50% < 75%."
                    }
                ]
            }
        ]
    },
    {
        "slug": "percentages",
        "title": "Percentages",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.9 • L2.9 • L2.10",
        "formula_hint": "To calculate a percentage of an amount, divide by 100 and multiply by the percentage (or multiply by the decimal multiplier, e.g. 17.5% = 0.175). For percentage change: (Difference ÷ Original) × 100.",
        "back_url": "../functional-skills-percentages.html",
        "total_marks": 18,
        "sections": [
            {
                "title": "Section A: Procedural Fluency Check",
                "meta": "Questions 1 & 2 • 4 Marks",
                "questions": [
                    {
                        "title": "Question 1 (Level 1 Percentage of Amount)",
                        "marks": 2,
                        "stem": "Calculate <strong>15% of £3,600</strong> without a calculator.",
                        "lines": 3,
                        "ans_label": "Amount =",
                        "choice_box": "£ ____________________",
                        "step_rows": [
                            ("1. 10% of £3,600 = £360; 5% = £180", "[M1]"),
                            ("2. 15% = £360 + £180 = £540", "[A1]")
                        ],
                        "final_answer": "£540",
                        "pitfall": "Dividing by 15 instead of finding 15 hundredths.",
                        "reverse_check": "£540 ÷ £3,600 = 0.15 = 15%."
                    },
                    {
                        "title": "Question 2 (Level 2 Reverse Percentage / Pre-VAT)",
                        "marks": 2,
                        "stem": "An electronic medical monitor costs <strong>£756 including 20% VAT</strong>.<br>Work out the original price of the monitor before VAT was added.",
                        "lines": 3,
                        "ans_label": "Pre-VAT price =",
                        "choice_box": "£ ____________________",
                        "step_rows": [
                            ("1. Recognize £756 represents 120% (multiplier 1.20): £756 ÷ 1.20", "[M1]"),
                            ("2. Evaluate: £756 ÷ 1.2 = £630.00", "[A1]")
                        ],
                        "final_answer": "£630.00",
                        "pitfall": "Calculating 20% of £756 (£151.20) and subtracting (£604.80). That is the classic Pearson trap!",
                        "reverse_check": "£630 + 20% (£126) = £756. Confirmed."
                    }
                ]
            },
            {
                "title": "Section B: Workplace & Functional Scenarios",
                "meta": "Questions 3 & 4 • 6 Marks",
                "questions": [
                    {
                        "title": "Question 3 (Level 1 NHS Pay Award)",
                        "marks": 3,
                        "stem": "A healthcare support worker earns a gross annual salary of <strong>£24,500</strong>.<br>The NHS Agenda for Change pay settlement awards a <strong>5.5% pay increase</strong> across all bands.<br><br>Work out the worker's new annual salary.",
                        "lines": 4,
                        "ans_label": "New annual salary =",
                        "choice_box": "£ ____________________",
                        "step_rows": [
                            ("1. Calculate 5.5% increase: £24,500 × 0.055 = £1,347.50", "[M1]"),
                            ("2. Add to base salary: £24,500 + £1,347.50", "[P1]"),
                            ("3. Accurate new salary: £25,847.50", "[A1]")
                        ],
                        "final_answer": "£25,847.50",
                        "pitfall": "Calculating 55% instead of 5.5% (multiplying by 0.55 instead of 0.055).",
                        "reverse_check": "£24,500 × 1.055 = £25,847.50."
                    },
                    {
                        "title": "Question 4 (Level 2 Percentage Decrease in Waiting Times)",
                        "marks": 3,
                        "stem": "Following a clinical pathway review, an outpatient clinic reduces its average patient wait time from <strong>45 minutes</strong> down to <strong>36 minutes</strong>.<br><br>Calculate the percentage decrease in waiting time.",
                        "lines": 4,
                        "ans_label": "Percentage decrease =",
                        "choice_box": "_____________ %",
                        "step_rows": [
                            ("1. Calculate absolute decrease: 45 - 36 = 9 minutes", "[M1]"),
                            ("2. Divide difference by original value: 9 ÷ 45 = 0.20", "[P1]"),
                            ("3. Convert to percentage: 0.20 × 100 = 20%", "[A1]")
                        ],
                        "final_answer": "20%",
                        "pitfall": "Dividing by the new value (9 ÷ 36 = 25%) instead of the original 45 minutes.",
                        "reverse_check": "45 - (20% of 45) = 45 - 9 = 36 minutes."
                    }
                ]
            },
            {
                "title": "Section C: Pearson Edexcel Problem Solving & Justification",
                "meta": "Questions 5 & 6 • 8 Marks",
                "questions": [
                    {
                        "title": "Question 5 (Level 2 Medical Equipment Lease vs Buy)",
                        "marks": 4,
                        "stem": "A diagnostic ultrasound machine has a list price of <strong>£32,000</strong>.<br>The supplier offers two purchase arrangements:<br>• <strong>Option A (Outright Buy)</strong>: 15% promotional discount on list price, plus £450 delivery.<br>• <strong>Option B (2-Year Lease)</strong>: Deposit of £4,000, followed by 24 monthly payments of £1,050.<br><br>Which option is cheaper, and by exactly how much?",
                        "lines": 5,
                        "ans_label": "Cheaper Option & Difference =",
                        "choice_box": "Option _____ is cheaper by £ ____________",
                        "step_rows": [
                            ("1. Option A: 15% discount = £32,000 × 0.15 = £4,800. Net equipment price: £27,200. Total with delivery: £27,200 + £450 = £27,650", "[P1]"),
                            ("2. Option B: 24 × £1,050 = £25,200 monthly payments. Total with deposit: £25,200 + £4,000 = £29,200", "[P1]"),
                            ("3. Difference: £29,200 - £27,650 = £1,550", "[M1]"),
                            ("4. Conclude: <strong>Option A is cheaper by £1,550</strong>", "[A1]")
                        ],
                        "final_answer": "Option A is cheaper by £1,550",
                        "pitfall": "Forgetting to add the £4,000 deposit to Option B.",
                        "reverse_check": "Option A: £27,650; Option B: £29,200. Difference = £1,550."
                    },
                    {
                        "title": "Question 6 (Level 2 Audit Target Justification)",
                        "marks": 4,
                        "stem": "An NHS Trust targets reducing patient complaints by at least <strong>12%</strong> over one year.<br>• In 2025, the trust recorded <strong>850 complaints</strong>.<br>• In 2026, the trust recorded <strong>740 complaints</strong>.<br><br>The customer service lead reports: <em>'We achieved our target reduction of at least 12%.'</em><br><br>Is the report correct?<br>Show your calculations clearly and state a definitive conclusion.",
                        "lines": 5,
                        "ans_label": "Conclusion & Reduction Rate =",
                        "choice_box": "Correct / Incorrect: Reduction was _____ %",
                        "step_rows": [
                            ("1. Calculate required 12% reduction: 850 × 0.12 = 102 complaints reduction (Target ≤ 748)", "[P1]"),
                            ("2. Actual complaints reduction: 850 - 740 = 110 complaints", "[M1]"),
                            ("3. Actual percentage reduction: (110 ÷ 850) × 100 = 12.94% (or compare 740 < 748)", "[P1]"),
                            ("4. Conclude: <strong>Yes, the report is correct</strong>. The trust reduced complaints by 12.94% (110 complaints), which exceeds the 12% target (102 complaints).", "[A1]")
                        ],
                        "final_answer": "Correct (Reduced complaints by 12.94% / 110 complaints, exceeding 12% target)",
                        "pitfall": "Dividing 110 by 740 (14.86%) rather than the 2025 baseline of 850.",
                        "reverse_check": "850 - 102 = 748. Actual is 740, which is an even larger reduction."
                    }
                ]
            }
        ]
    }
]

print(f"Loaded {len(MATHS_CORE_TOPICS)} high-yield topics in runner.")
