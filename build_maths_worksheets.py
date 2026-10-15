#!/usr/bin/env python3
"""
Master Functional Skills - Maths Worksheets & Mark Schemes Generator.
Builds complete, original, Pearson Edexcel aligned worksheets and answers
for all 48 Maths topics.
"""
import os
from worksheet_templates import render_worksheet, render_answers

MATHS_TOPICS = [
    # 1. Place value & numbers
    {
        "slug": "numbers-and-place-value",
        "title": "Numbers & Place Value",
        "subject": "Mathematics",
        "spec_codes": "Pearson Edexcel: L1.1 • L1.2 • L2.1",
        "total_marks": 18,
        "formula_hint": "Place value determines digit worth. Use grouping commas from the decimal point: Millions, Thousands, Units, tenths, hundredths, thousandths.",
        "back_url": "../functional-skills-numbers-and-place-value.html",
        "sections": [
            {
                "title": "Section A: Procedural Fluency Check",
                "meta": "Questions 1 & 2 • 4 Marks",
                "questions": [
                    {
                        "title": "Question 1 (Level 1 Standard)",
                        "marks": 2,
                        "stem": "Write the number <strong>two million, forty-five thousand, six hundred and eight</strong> in figures.",
                        "lines": 2,
                        "ans_label": "Number in figures =",
                        "choice_box": "____________________",
                        "step_rows": [
                            ("1. Identify millions (2,000,000) and thousands (045,000)", "[M1]"),
                            ("2. Complete number with hundreds, tens, units: 2,045,608", "[A1]")
                        ],
                        "final_answer": "2,045,608",
                        "pitfall": "Omitting the placeholder zero in the hundred-thousands column, erroneously writing 2,45,608.",
                        "reverse_check": "2,000,000 + 40,000 + 5,000 + 600 + 8 = 2,045,608."
                    },
                    {
                        "title": "Question 2 (Level 1 Standard)",
                        "marks": 2,
                        "stem": "In the number <strong>4,839,271</strong>, state the value of the digit <strong>3</strong> both in words and as a number.",
                        "lines": 3,
                        "ans_label": "Value of digit 3 =",
                        "choice_box": "____________________",
                        "step_rows": [
                            ("1. Identify position as ten-thousands column", "[M1]"),
                            ("2. State value as 30,000 (thirty thousand)", "[A1]")
                        ],
                        "final_answer": "30,000 (Thirty Thousand)",
                        "pitfall": "Writing just 'ten thousands' (the position) rather than the value 30,000.",
                        "reverse_check": "3 × 10,000 = 30,000."
                    }
                ]
            },
            {
                "title": "Section B: Workplace & Functional Scenarios",
                "meta": "Questions 3 & 4 • 6 Marks",
                "questions": [
                    {
                        "title": "Question 3 (Level 1 NHS Depot Audit)",
                        "marks": 3,
                        "stem": "An NHS central distribution warehouse holds medical mask stock across four regional depots:<br>• Depot A: 340,500<br>• Depot B: 304,850<br>• Depot C: 345,000<br>• Depot D: 340,095<br><br>Write these depot stock quantities in ascending order (smallest to largest).",
                        "lines": 4,
                        "ans_label": "Ascending order =",
                        "choice_box": "________________________________________________________",
                        "step_rows": [
                            ("1. Compare hundred-thousands and ten-thousands: Depot B (304,850) is lowest", "[P1]"),
                            ("2. Compare 340k+ depots: Depot D (340,095), Depot A (340,500), Depot C (345,000)", "[P1]"),
                            ("3. Full correct order: 304,850; 340,095; 340,500; 345,000", "[A1]")
                        ],
                        "final_answer": "304,850  <  340,095  <  340,500  <  345,000",
                        "pitfall": "Misreading 340,095 as larger than 340,500 by overlooking the tens versus hundreds column zero.",
                        "reverse_check": "345,000 > 340,500 > 340,095 > 304,850."
                    },
                    {
                        "title": "Question 4 (Level 2 Laboratory Decimal Ordering)",
                        "marks": 3,
                        "stem": "A biomedical laboratory analyses blood serum concentrations in mg/dL: <strong>0.048, 0.408, 0.0408, 0.48, 0.084</strong>.<br>Arrange these concentrations in order from <strong>largest</strong> to <strong>smallest</strong>.",
                        "lines": 4,
                        "ans_label": "Ordered concentrations =",
                        "choice_box": "________________________________________________________",
                        "step_rows": [
                            ("1. Pad numbers to 4 decimal places: 0.0480, 0.4080, 0.0408, 0.4800, 0.0840", "[M1]"),
                            ("2. Compare tenths and hundredths to identify largest: 0.48, then 0.408", "[P1]"),
                            ("3. Order remaining values: 0.084, 0.048, 0.0408", "[A1]")
                        ],
                        "final_answer": "0.48,  0.408,  0.084,  0.048,  0.0408",
                        "pitfall": "Assuming longer decimal strings are automatically larger (e.g. thinking 0.0408 > 0.48).",
                        "reverse_check": "4800/10000 > 4080/10000 > 840/10000 > 480/10000 > 408/10000."
                    }
                ]
            },
            {
                "title": "Section C: Pearson Edexcel Problem Solving & Justification",
                "meta": "Questions 5 & 6 • 8 Marks",
                "questions": [
                    {
                        "title": "Question 5 (Level 2 Capital Grant Modernization)",
                        "marks": 4,
                        "stem": "An Integrated Care Board awards an annual modernization grant of <strong>£3,850,000</strong>.<br>The financial director states that <em>'Three hundred and eighty-five thousand pounds'</em> is allocated to wellness, while <em>'Three million, four hundred and sixty thousand pounds'</em> is spent on clinical upgrades.<br><br>Calculate the unallocated contingency balance remaining on the grant, if any.",
                        "lines": 5,
                        "ans_label": "Contingency balance =",
                        "choice_box": "£ ____________________",
                        "step_rows": [
                            ("1. Convert wellness to figures: £385,000", "[P1]"),
                            ("2. Convert clinical upgrades to figures: £3,460,000", "[P1]"),
                            ("3. Sum allocations: £385,000 + £3,460,000 = £3,845,000", "[M1]"),
                            ("4. Subtract from grant: £3,850,000 - £3,845,000 = £5,000 contingency balance", "[A1]")
                        ],
                        "final_answer": "£5,000 unallocated contingency balance",
                        "pitfall": "Writing £385,000 as 38,500 when converting verbal financial statements.",
                        "reverse_check": "£3,460,000 + £385,000 + £5,000 = £3,850,000."
                    },
                    {
                        "title": "Question 6 (Level 2 Rounding Justification)",
                        "marks": 4,
                        "stem": "A procurement manager claims: <em>'Rounding our annual consumables expenditure of £1,496,250 to the nearest ten thousand gives £1,490,000.'</em><br><br>Is the manager's claim correct?<br>Show your rounding method, state whether the claim is correct, and give the true rounded figure.",
                        "lines": 5,
                        "ans_label": "Decision & Rounded Figure =",
                        "choice_box": "Correct / Incorrect: £ ________________",
                        "step_rows": [
                            ("1. Identify ten-thousands column (9) and deciding digit (6) in thousands place", "[P1]"),
                            ("2. Since 6 ≥ 5, round up: 90,000 + 10,000 = 100,000 (carrying 1 to hundred-thousands)", "[M1]"),
                            ("3. True rounded figure: £1,500,000", "[A1]"),
                            ("4. Conclude: <strong>Incorrect</strong>; the manager truncated the number rather than rounding up to £1,500,000.", "[A1]")
                        ],
                        "final_answer": "Incorrect; Correct rounded value is £1,500,000",
                        "pitfall": "Forgetting to carry over into the next place column when rounding a '9'.",
                        "reverse_check": "£1,496,250 is £3,750 away from £1,500,000, but £6,250 away from £1,490,000."
                    }
                ]
            }
        ]
    }
]

print("Maths builder module initialized.")
