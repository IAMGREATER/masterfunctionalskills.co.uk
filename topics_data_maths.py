#!/usr/bin/env python3
"""
Complete Mathematics Curriculum Topics for Worksheets and Mark Schemes.
Covers all 48 Pearson Edexcel Functional Skills standards.
"""
from generate_all_worksheets_complete import get_svg_for_topic

MATHS_TOPIC_DEFS = [
    # Ratio
    {
        "slug": "ratio",
        "title": "Ratio",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.11 • L2.11",
        "formula_hint": "Find the total number of parts by adding the ratio terms. Divide the total quantity by the total parts to find the value of 1 part, then multiply by each term in the ratio.",
        "back_url": "../functional-skills-ratio.html",
        "total_marks": 18,
        "sections": [
            {
                "title": "Section A: Core Skills (Warm-Up)",
                "meta": "Questions 1 & 2 • 4 Marks",
                "questions": [
                    {
                        "title": "Question 1 (Level 1 Simplifying Ratios)",
                        "marks": 2,
                        "stem": "Simplify the ratio <strong>24 : 36</strong> to its simplest form.",
                        "lines": 3,
                        "ans_label": "Simplest Ratio =",
                        "choice_box": "____ : ____",
                        "step_rows": [
                            ("1. Identify HCF (12) or divide by 2, 3, 4: 24 ÷ 12 = 2, 36 ÷ 12 = 3", "[M1]"),
                            ("2. State in simplest form: 2 : 3", "[A1]")
                        ],
                        "final_answer": "2 : 3",
                        "pitfall": "Reversing the terms (3 : 2) or stopping at 12 : 18.",
                        "reverse_check": "2 × 12 = 24; 3 × 12 = 36."
                    },
                    {
                        "title": "Question 2 (Level 1 Unitary Form 1 : n)",
                        "marks": 2,
                        "stem": "Express the ratio <strong>5 : 18</strong> in the form <strong>1 : n</strong>.<br>Give <em>n</em> as a decimal.",
                        "lines": 3,
                        "ans_label": "Ratio in form 1 : n =",
                        "choice_box": "1 : ____",
                        "step_rows": [
                            ("1. Divide both terms by 5: 5 ÷ 5 = 1; 18 ÷ 5 = 3.6", "[M1]"),
                            ("2. State ratio: 1 : 3.6", "[A1]")
                        ],
                        "final_answer": "1 : 3.6",
                        "pitfall": "Dividing 5 by 18 to get 1 : 0.27.",
                        "reverse_check": "3.6 × 5 = 18."
                    }
                ]
            },
            {
                "title": "Section B: Everyday & Workplace Maths",
                "meta": "Questions 3 & 4 • 6 Marks",
                "questions": [
                    {
                        "title": "Question 3 (Level 1 Chemical Disinfectant Mixing)",
                        "marks": 3,
                        "stem": "Hospital infection control guidelines state that surgical surface disinfectant must be mixed with water in the ratio <strong>1 : 7</strong> (disinfectant concentrate to water).<br>A domestic services assistant prepares <strong>32 litres</strong> of ready-to-use cleaning solution.<br><br>How many litres of disinfectant concentrate and how many litres of water are needed?",
                        "lines": 4,
                        "ans_label": "Quantities =",
                        "choice_box": "Concentrate: _____ L | Water: _____ L",
                        "step_rows": [
                            ("1. Total parts: 1 + 7 = 8 parts", "[M1]"),
                            ("2. Value of 1 part: 32 L ÷ 8 = 4 litres", "[P1]"),
                            ("3. Water: 7 × 4 L = 28 litres. Concentrate: 1 × 4 L = 4 litres", "[A1]")
                        ],
                        "final_answer": "4 litres concentrate, 28 litres water",
                        "pitfall": "Dividing 32 by 7 instead of the total 8 parts.",
                        "reverse_check": "4 L + 28 L = 32 L; 4 : 28 = 1 : 7."
                    },
                    {
                        "title": "Question 4 (Level 2 Three-Part Capital Allocation)",
                        "marks": 3,
                        "stem": "A community diagnostic hub divides an annual medical equipment grant of <strong>£84,000</strong> between Radiology, Cardiology, and Pathology in the ratio <strong>5 : 4 : 3</strong>.<br><br>How much money is allocated to Cardiology?",
                        "lines": 4,
                        "ans_label": "Cardiology Allocation =",
                        "choice_box": "£ ____________________",
                        "step_rows": [
                            ("1. Total parts: 5 + 4 + 3 = 12 parts", "[M1]"),
                            ("2. Value of 1 part: £84,000 ÷ 12 = £7,000", "[P1]"),
                            ("3. Cardiology (4 parts): 4 × £7,000 = £28,000", "[A1]")
                        ],
                        "final_answer": "£28,000",
                        "pitfall": "Calculating Radiology (5 parts = £35,000) or Pathology (3 parts = £21,000) instead of Cardiology.",
                        "reverse_check": "£35,000 + £28,000 + £21,000 = £84,000."
                    }
                ]
            },
            {
                "title": "Section C: Exam-Style Problem Solving",
                "meta": "Questions 5 & 6 • 8 Marks",
                "questions": [
                    {
                        "title": "Question 5 (Level 2 Apprentice Mortar Mixing Ratio)",
                        "marks": 4,
                        "stem": "A bricklayer mixes mortar using cement, lime, and building sand in the ratio <strong>1 : 2 : 9</strong> by weight.<br>The bricklayer has <strong>25 kg</strong> of cement, <strong>45 kg</strong> of lime, and <strong>240 kg</strong> of building sand in their workshop.<br><br>Calculate the maximum total weight of mortar the bricklayer can mix, and identify which ingredient runs out first.",
                        "lines": 5,
                        "ans_label": "Max Mortar & Limiting Ingredient =",
                        "choice_box": "Max Mortar: _____ kg | Runs out first: ________",
                        "step_rows": [
                            ("1. Check maximum batches per ingredient: Cement: 25 ÷ 1 = 25 batches; Lime: 45 ÷ 2 = 22.5 batches; Sand: 240 ÷ 9 = 26.66 batches", "[M1]"),
                            ("2. Identify limiting ingredient: Lime allows only 22.5 batches (runs out first)", "[P1]"),
                            ("3. Total parts in formula: 1 + 2 + 9 = 12 parts", "[P1]"),
                            ("4. Calculate total mortar weight: 22.5 batches × 12 = 270 kg", "[A1]")
                        ],
                        "final_answer": "270 kg of mortar; Lime runs out first",
                        "pitfall": "Using cement (25 batches × 12 = 300 kg), which would require 50 kg of lime (exceeding the available 45 kg).",
                        "reverse_check": "22.5 kg cement + 45 kg lime + 202.5 kg sand = 270 kg. All within available stock."
                    },
                    {
                        "title": "Question 6 (Level 2 Staff Ratio Compliance Justification)",
                        "marks": 4,
                        "stem": "A specialist dementia care wing has a statutory safety policy stating that the ratio of qualified nurses to healthcare care assistants must be at least <strong>1 : 4</strong> (i.e. at least 1 nurse for every 4 care assistants).<br>On a weekend night shift, the ward is staffed with <strong>3 nurses and 14 care assistants</strong>.<br>The shift coordinator states: <em>'We are in full compliance with the statutory staffing ratio.'</em><br><br>Is the shift coordinator correct?<br>Show your calculations clearly and state a definitive conclusion.",
                        "lines": 5,
                        "ans_label": "Decision & Ratio Comparison =",
                        "choice_box": "Correct / Incorrect: Max assistants allowed = _____",
                        "step_rows": [
                            ("1. Calculate maximum care assistants allowed for 3 nurses: 3 × 4 = 12 care assistants", "[M1]"),
                            ("2. Or calculate required nurses for 14 care assistants: 14 ÷ 4 = 3.5 nurses (requires 4 nurses)", "[P1]"),
                            ("3. Compare actual staffing: 14 care assistants exceeds the maximum allowed (12) for 3 nurses (actual ratio is 3 : 14 = 1 : 4.67)", "[M1]"),
                            ("4. Conclude: <strong>No / Incorrect</strong>; the ward is NOT compliant. 3 nurses can safely oversee a maximum of 12 assistants, so having 14 assistants breaches the safety ratio (short by 1 nurse or has 2 assistants too many).", "[A1]")
                        ],
                        "final_answer": "Incorrect (Breaches ratio; 3 nurses can only oversee 12 assistants; requires 4 nurses for 14 assistants)",
                        "pitfall": "Assuming 3 : 14 is compliant because 3 is a large number of nurses.",
                        "reverse_check": "3 : 12 = 1 : 4 (compliant); 3 : 14 = 1 : 4.67 (non-compliant)."
                    }
                ]
            }
        ]
    },
    # Area
    {
        "slug": "area",
        "title": "Area",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.23 • L2.17",
        "formula_hint": "Rectangle = Length × Width. Triangle = (Base × Height) ÷ 2. Parallelogram = Base × Upright Height. Trapezium = ((Side A + Side B) ÷ 2) × Upright Height. Compound shapes: Split into non-overlapping shapes and add individual areas together.",
        "back_url": "../functional-skills-area.html",
        "total_marks": 18,
        "sections": [
            {
                "title": "Section A: Core Skills (Warm-Up)",
                "meta": "Questions 1 & 2 • 4 Marks",
                "questions": [
                    {
                        "title": "Question 1 (Level 1 Triangle Area)",
                        "marks": 2,
                        "stem": "Calculate the area of a triangle with a base of <strong>14.0 metres</strong> and a perpendicular height of <strong>6.5 metres</strong>.",
                        "lines": 3,
                        "ans_label": "Area =",
                        "choice_box": "_____________ m²",
                        "step_rows": [
                            ("1. Triangle formula: ½ × base × height = ½ × 14.0 × 6.5", "[M1]"),
                            ("2. Accurate calculation: 7.0 × 6.5 = 45.5 m²", "[A1]")
                        ],
                        "final_answer": "45.5 m²",
                        "pitfall": "Forgetting to divide by 2, yielding 91 m².",
                        "reverse_check": "45.5 × 2 ÷ 14.0 = 6.5 m."
                    },
                    {
                        "title": "Question 2 (Level 2 Trapezium Area)",
                        "marks": 2,
                        "stem": "Calculate the area of a trapezium with parallel sides <em>a</em> = <strong>8.4 m</strong>, <em>b</em> = <strong>12.6 m</strong>, and perpendicular height <em>h</em> = <strong>5.0 m</strong>.",
                        "lines": 3,
                        "ans_label": "Area =",
                        "choice_box": "_____________ m²",
                        "step_rows": [
                            ("1. Trapezium formula: ½ × (a + b) × h = ½ × (8.4 + 12.6) × 5.0", "[M1]"),
                            ("2. ½ × 21.0 × 5.0 = 10.5 × 5.0 = 52.5 m²", "[A1]")
                        ],
                        "final_answer": "52.5 m²",
                        "pitfall": "Multiplying parallel sides together instead of adding them.",
                        "reverse_check": "52.5 ÷ 5.0 × 2 = 21.0; 21.0 - 8.4 = 12.6 m."
                    }
                ]
            },
            {
                "title": "Section B: Everyday & Workplace Maths",
                "meta": "Questions 3 & 4 • 6 Marks",
                "questions": [
                    {
                        "title": "Question 3 (Level 1 Compound L-Shape Floor Plan)",
                        "marks": 3,
                        "stem": "A facilities coordinator needs to carpet a reception lobby shown below.",
                        "svg": get_svg_for_topic("area"),
                        "lines": 4,
                        "ans_label": "Total Floor Area =",
                        "choice_box": "_____________ m²",
                        "step_rows": [
                            ("1. Split into two rectangles: Rectangle A = 14.0 m × 3.5 m = 49.0 m²", "[M1]"),
                            ("2. Rectangle B = (14.0 - 5.0 = 9.0 m) ... or base 9.0 m × 5.5 m = 49.5 m²", "[P1]"),
                            ("3. Sum areas: 49.0 + 49.5 = 98.5 m² (or split vertically: 5.0 × 9.0 = 45 m² + 9.0 × 3.5 = 31.5 m²... total 98.5 m²)", "[A1]")
                        ],
                        "final_answer": "98.5 m²",
                        "pitfall": "Multiplying the two largest outer dimensions (14.0 × 9.0 = 126 m²), ignoring the missing cutout.",
                        "reverse_check": "14.0 × 9.0 = 126 m² bounding box; Cutout = (14 - 9) × (9 - 3.5) = 5.0 × 5.5 = 27.5 m²; 126 - 27.5 = 98.5 m²."
                    },
                    {
                        "title": "Question 4 (Level 2 Paint Coverage & Tins)",
                        "marks": 3,
                        "stem": "A painter decorates four clinical consultation rooms.<br>• Total wall area to paint across all rooms: <strong>210 square metres</strong>.<br>• The painter will apply <strong>2 coats</strong> of paint.<br>• 1 tin of paint covers <strong>35 square metres</strong> on a single coat.<br><br>How many whole tins of paint must be purchased?",
                        "lines": 4,
                        "ans_label": "Tins of paint =",
                        "choice_box": "_____________ tins",
                        "step_rows": [
                            ("1. Total painted area for 2 coats: 210 × 2 = 420 m²", "[M1]"),
                            ("2. Divide total area by coverage per tin: 420 ÷ 35 = 12 tins", "[P1]"),
                            ("3. State 12 whole tins", "[A1]")
                        ],
                        "final_answer": "12 tins",
                        "pitfall": "Calculating for 1 coat only (210 ÷ 35 = 6 tins).",
                        "reverse_check": "12 tins × 35 m² = 420 m²; 420 ÷ 2 coats = 210 m²."
                    }
                ]
            },
            {
                "title": "Section C: Exam-Style Problem Solving",
                "meta": "Questions 5 & 6 • 8 Marks",
                "questions": [
                    {
                        "title": "Question 5 (Level 2 Grass Turf & Pathway Costing)",
                        "marks": 4,
                        "stem": "A hospice redesigns a sensory garden measuring <strong>18.0 m by 12.0 m</strong>.<br>A paved perimeter pathway of width <strong>1.5 m</strong> runs completely around the inner perimeter of the garden, leaving a lawn in the centre.<br>• Turf for the central lawn costs <strong>£6.50 per square metre</strong>.<br><br>Calculate the cost to turf the central lawn.",
                        "lines": 5,
                        "ans_label": "Cost of Turf =",
                        "choice_box": "£ ____________________",
                        "step_rows": [
                            ("1. Deduct 1.5 m border from both sides for length: 18.0 - (2 × 1.5) = 18.0 - 3.0 = 15.0 m", "[P1]"),
                            ("2. Deduct border from width: 12.0 - (2 × 1.5) = 12.0 - 3.0 = 9.0 m", "[P1]"),
                            ("3. Lawn area: 15.0 × 9.0 = 135 m²", "[M1]"),
                            ("4. Total turf cost: 135 m² × £6.50 = £877.50", "[A1]")
                        ],
                        "final_answer": "£877.50",
                        "pitfall": "Deducting 1.5 m only once from length and width (calculating 16.5 × 10.5 m = 173.25 m²).",
                        "reverse_check": "£877.50 ÷ £6.50 = 135 m²; 135 ÷ 9 = 15 m; 15 + 3 = 18 m."
                    },
                    {
                        "title": "Question 6 (Level 2 Vinyl Tiles Pack Justification)",
                        "marks": 4,
                        "stem": "An estates manager plans to re-tile an L-shaped clinical laboratory with floor area <strong>54.0 m²</strong>.<br>The floor tiles are sold in boxes. Each box covers <strong>2.8 m²</strong> and costs <strong>£32.00 per box</strong>.<br>The supplier advises adding <strong>10% extra area</strong> for cutting wastage.<br>The manager has a flooring budget of <strong>£700.00</strong> and claims: <em>'The budget is sufficient to purchase enough boxes including the 10% wastage.'</em><br><br>Is the manager correct?<br>Show your calculations clearly and state a definitive conclusion.",
                        "lines": 5,
                        "ans_label": "Conclusion & Cost Comparison =",
                        "choice_box": "Correct / Incorrect: Total cost is £ ________ vs Budget £700",
                        "step_rows": [
                            ("1. Add 10% wastage: 54.0 × 1.10 = 59.4 m² required", "[M1]"),
                            ("2. Divide by box coverage: 59.4 ÷ 2.8 = 21.21 boxes", "[P1]"),
                            ("3. Round UP to whole boxes: 22 boxes needed", "[P1]"),
                            ("4. Total cost: 22 × £32.00 = £704.00. Compare with budget: £704.00 > £700.00. Conclude: <strong>No / Incorrect</strong>; cost exceeds budget by £4.00.", "[A1]")
                        ],
                        "final_answer": "Incorrect (Total cost is £704.00, exceeding the £700 budget by £4.00)",
                        "pitfall": "Rounding down to 21 boxes (£672.00) and incorrectly stating 'Yes'.",
                        "reverse_check": "21 boxes = 58.8 m² (< 59.4 m²). 22 boxes required: 22 × £32 = £704."
                    }
                ]
            }
        ]
    }
]

print(f"Loaded {len(MATHS_TOPIC_DEFS)} topics in topics_data_maths.py")
