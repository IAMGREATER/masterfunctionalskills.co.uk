#!/usr/bin/env python3
"""
Populate authentic Master Functional Skills revision content for high-yield topics.
Generates:
- Revision topic HTML
- worksheets/<slug>-worksheet.html
- worksheets/<slug>-answers.html
"""

import os
from generate_modern_topic import build_topic_page, build_printable_worksheet, build_printable_answers

TOPICS = [
    {
        "slug": "fractions",
        "title": "Fractions",
        "subject": "Maths",
        "levels": ["Level 1", "Level 2"],
        "spec_codes": "Pearson Edexcel: L1.1, L1.2, L2.1, L2.2",
        "intro_summary": "Master fractions for Functional Skills Maths. Learn how to simplify fractions, calculate fractions of amounts in workplace contexts, add and subtract with common denominators, and convert between improper fractions and mixed numbers without losing method marks.",
        "video_duration": "16:45",
        "video_chapters": [
            {"time": "00:00", "title": "Introduction & Pearson Edexcel Specification"},
            {"time": "02:15", "title": "Simplifying Fractions & Highest Common Factors"},
            {"time": "05:10", "title": "Fractions of Workplace Amounts (NHS & Retail)"},
            {"time": "08:45", "title": "Adding & Subtracting Fractions (LCM Method)"},
            {"time": "12:20", "title": "Mixed Numbers & Improper Conversions"},
            {"time": "14:40", "title": "Examiner Pitfalls & Lost Mark Warnings"}
        ],
        "key_rules": [
            {
                "icon": "fa-solid fa-divide",
                "title": "Golden Rule for Fractions of Amounts: 'Divide by Bottom, Times by Top'",
                "desc": "To calculate a fraction of a quantity (e.g. 3/8 of £480), divide the total amount by the denominator (bottom number) to find 1 part: £480 ÷ 8 = £60. Then multiply that answer by the numerator (top number): £60 × 3 = £180."
            },
            {
                "icon": "fa-solid fa-arrows-split-up-and-left",
                "title": "Adding & Subtracting: Never Add Denominators!",
                "desc": "You cannot add or subtract fractions until their denominators (bottom numbers) match. Find the Lowest Common Multiple (LCM) to create equivalent fractions before adding or subtracting only the top numbers."
            },
            {
                "icon": "fa-solid fa-arrows-rotate",
                "title": "Converting Mixed Numbers to Improper Fractions",
                "desc": "Multiply the whole number by the denominator, then add the numerator. Place the result over the original denominator. For 3 2/5: (3 × 5) + 2 = 17, giving 17/5."
            }
        ],
        "worked_examples": [
            {
                "level": "Level 2 Exam Standard (4 Marks)",
                "question": "A community health clinic has an annual staffing budget of £72,000. 5/12 of the budget is allocated to nursing staff, and 1/6 is allocated to administrative support. The remaining budget is spent on medical supplies. Calculate the exact amount allocated to medical supplies.",
                "steps": [
                    {
                        "step": "Step 1",
                        "action": "Calculate the nursing staff allocation (5/12 of £72,000)",
                        "math": "£72,000 ÷ 12 = £6,000 | £6,000 × 5 = £30,000",
                        "mark": "M1 (Method mark for finding 1/12 and multiplying by 5)"
                    },
                    {
                        "step": "Step 2",
                        "action": "Calculate the administrative support allocation (1/6 of £72,000)",
                        "math": "£72,000 ÷ 6 = £12,000",
                        "mark": "M1 (Method mark for dividing total by 6)"
                    },
                    {
                        "step": "Step 3",
                        "action": "Sum allocated costs and subtract from total budget",
                        "math": "£30,000 + £12,000 = £42,000 | £72,000 - £42,000 = £30,000",
                        "mark": "M1 (Method mark for subtraction from £72,000)"
                    },
                    {
                        "step": "Step 4",
                        "action": "State final answer with pound sterling (£) units",
                        "math": "Final Answer = £30,000",
                        "mark": "A1 (Accuracy mark for correct numerical value and units)"
                    }
                ],
                "final_answer": "£30,000"
            }
        ],
        "examiner_traps": [
            {
                "title": "Adding the denominators across (e.g. 1/4 + 1/4 = 2/8)",
                "desc": "The most common error on Pearson Edexcel Non-Calculator papers is adding both top and bottom numbers. 1/4 + 1/4 = 2/4 = 1/2, NOT 2/8.",
                "solution": "Keep the common denominator identical. Only add or subtract the numerators."
            },
            {
                "title": "Forgetting to write the fraction in its simplest form",
                "desc": "Exam questions often specify: 'Give your fraction in its simplest form'. An unsimplified answer (e.g. 12/16 instead of 3/4) loses the final Accuracy Mark (A1).",
                "solution": "Always check if both top and bottom can be divided by 2, 3, or their Highest Common Factor."
            }
        ],
        "practice_questions": [
            {
                "marks": 3,
                "question": "A warehouse manager receives a delivery of 480 cartons. 3/8 of the cartons contain medical PPE, and 2/5 contain hand sanitiser bottles. How many cartons are left for other supplies?",
                "solution_steps": "1. PPE cartons: 480 ÷ 8 = 60; 60 × 3 = 180 cartons (M1)<br>2. Sanitiser cartons: 480 ÷ 5 = 96; 96 × 2 = 192 cartons (M1)<br>3. Total allocated: 180 + 192 = 372 cartons.<br>4. Remaining: 480 - 372 = 108 cartons (A1).",
                "correct_answer": "108 cartons",
                "tutor_tip": "Calculate each fraction separately first. Double check: 180 + 192 + 108 = 480."
            },
            {
                "marks": 3,
                "question": "Work out 2 1/3 + 1 3/4. Give your answer as a mixed number in its simplest form.",
                "solution_steps": "1. Convert to improper fractions: 2 1/3 = 7/3 and 1 3/4 = 7/4 (M1)<br>2. Find common denominator (12): 7/3 = 28/12 and 7/4 = 21/12 (M1)<br>3. Add: 28/12 + 21/12 = 49/12 = 4 1/12 (A1)",
                "correct_answer": "4 1/12",
                "tutor_tip": "49 ÷ 12 = 4 with a remainder of 1, so the answer is 4 1/12."
            },
            {
                "marks": 2,
                "question": "In a care home with 60 residents, 45 residents choose chicken for lunch. What fraction of residents choose chicken? Give your answer in its simplest form.",
                "solution_steps": "1. Write as a fraction: 45/60 (B1)<br>2. Divide numerator and denominator by 15 (HCF): 45 ÷ 15 = 3, 60 ÷ 15 = 4 -> 3/4 (A1)",
                "correct_answer": "3/4",
                "tutor_tip": "Both numbers end in 0 and 5, so you can divide by 5 first (9/12), then divide by 3 to reach 3/4."
            }
        ]
    },
    {
        "slug": "percentages",
        "title": "Percentages",
        "subject": "Maths",
        "levels": ["Level 1", "Level 2"],
        "spec_codes": "Pearson Edexcel: L1.3, L2.3, L2.4",
        "intro_summary": "Master percentages for Functional Skills Maths. Learn percentage of amounts, percentage increase and decrease, reverse percentages, and comparing interest rates for workplace and financial exam scenarios.",
        "video_duration": "18:10",
        "video_chapters": [
            {"time": "00:00", "title": "Introduction to Functional Skills Percentages"},
            {"time": "02:30", "title": "Mental Percentages: 50%, 10%, 5%, 1% (Non-Calc)"},
            {"time": "06:15", "title": "Percentage Increase & Decrease (Multiplier Method)"},
            {"time": "10:20", "title": "Reverse Percentages (Working Backwards from VAT)"},
            {"time": "14:10", "title": "Compound Interest & Loan Comparison Scenarios"},
            {"time": "16:30", "title": "Examiner Marking Schemes & Model Answers"}
        ],
        "key_rules": [
            {
                "icon": "fa-solid fa-percent",
                "title": "Building Blocks for Non-Calculator Papers",
                "desc": "To find 10%, divide by 10. To find 5%, halve your 10%. To find 1%, divide by 100. You can combine these to find any percentage: 15% = 10% + 5%."
            },
            {
                "icon": "fa-solid fa-calculator",
                "title": "Calculator Multiplier Method",
                "desc": "For percentage increase, add to 100% and convert to decimal (e.g. 15% increase = × 1.15). For decrease, subtract from 100% (e.g. 20% discount = × 0.80)."
            },
            {
                "icon": "fa-solid fa-backward",
                "title": "Reverse Percentages Rule",
                "desc": "If a price includes 20% VAT (£240), it represents 120% of the original. To find the original price before VAT, divide by 1.20: £240 ÷ 1.20 = £200. NEVER simply subtract 20% of £240!"
            }
        ],
        "worked_examples": [
            {
                "level": "Level 2 Exam Standard (4 Marks)",
                "question": "A specialist laptop is priced at £850 excluding VAT. A seasonal promotion offers a 15% trade discount on the net price before VAT is applied. VAT is charged at 20%. Calculate the final price of the laptop including VAT.",
                "steps": [
                    {
                        "step": "Step 1",
                        "action": "Calculate 15% discount on £850",
                        "math": "15% of £850 = £850 × 0.15 = £127.50 | Net Price = £850 - £127.50 = £722.50",
                        "mark": "M1 (Method mark for discount calculation)"
                    },
                    {
                        "step": "Step 2",
                        "action": "Calculate 20% VAT on discounted net price",
                        "math": "20% of £722.50 = £722.50 × 0.20 = £144.50",
                        "mark": "M1 (Method mark for calculating 20% of discounted figure)"
                    },
                    {
                        "step": "Step 3",
                        "action": "Add VAT to discounted net price",
                        "math": "£722.50 + £144.50 = £867.00",
                        "mark": "M1 (Method mark for addition)"
                    },
                    {
                        "step": "Step 4",
                        "action": "Write final currency answer to 2 decimal places",
                        "math": "Final Total = £867.00",
                        "mark": "A1 (Accuracy mark for correct £867.00 with trailing zero)"
                    }
                ],
                "final_answer": "£867.00"
            }
        ],
        "examiner_traps": [
            {
                "title": "Writing currency with one decimal place (e.g. £867.5 instead of £867.50)",
                "desc": "Pearson Edexcel examiners penalise answers that omit the trailing zero for pence. Money must always have two decimal places.",
                "solution": "Always write pounds and pence with two decimal digits: £144.50, never £144.5."
            },
            {
                "title": "Applying VAT before subtracting the discount",
                "desc": "Read the question carefully. Trade discount is almost always applied to the pre-VAT subtotal first.",
                "solution": "Follow the sequence stated in the question: Subtotal → Discount → Subtotal after discount → VAT."
            }
        ],
        "practice_questions": [
            {
                "marks": 3,
                "question": "A training provider has 240 apprentices enrolled. In the first term, 15% of apprentices achieve early distinction grades. How many apprentices achieve early distinction?",
                "solution_steps": "1. 10% of 240 = 24 (M1)<br>2. 5% of 240 = 12 (M1)<br>3. 15% = 24 + 12 = 36 apprentices (A1).<br>Alternative: 240 × 0.15 = 36.",
                "correct_answer": "36 apprentices",
                "tutor_tip": "On non-calculator papers, break 15% into 10% and 5%."
            },
            {
                "marks": 4,
                "question": "A vehicle hire company charges £360 for a weekend van rental. The price includes 20% VAT. Calculate the cost of the van hire before VAT was added.",
                "solution_steps": "1. Recognise that £360 represents 120% of original price (M1)<br>2. Set up reverse calculation: 1% = £360 ÷ 120 = £3 (M1)<br>3. Original (100%) = £3 × 100 = £300 (A1)<br>Or: £360 ÷ 1.20 = £300 (M2, A1)",
                "correct_answer": "£300.00",
                "tutor_tip": "Never calculate 20% of £360 and subtract! £360 - £72 = £288, which is WRONG."
            }
        ]
    },
    {
        "slug": "ratio",
        "title": "Ratio and Proportion",
        "subject": "Maths",
        "levels": ["Level 1", "Level 2"],
        "spec_codes": "Pearson Edexcel: L1.4, L2.5, L2.6",
        "intro_summary": "Master ratio and direct proportion for Functional Skills Maths. Learn the 3-step ratio method (Add parts, Divide to find 1 part, Multiply), scaling recipes, mixing building mortar, and solving sharing problems.",
        "video_duration": "15:30",
        "video_chapters": [
            {"time": "00:00", "title": "Introduction & Simplifying Ratios"},
            {"time": "03:10", "title": "The Golden 3-Step Sharing Rule (Add, Divide, Multiply)"},
            {"time": "07:00", "title": "Workplace Mortar & Paint Mixing Questions"},
            {"time": "10:30", "title": "'One Part Given' Problem Solving"},
            {"time": "13:15", "title": "Direct Proportion & Recipe Scaling"}
        ],
        "key_rules": [
            {
                "icon": "fa-solid fa-shapes",
                "title": "The Universal 3-Step Ratio Formula",
                "desc": "1. ADD the parts of the ratio together.<br>2. DIVIDE the total quantity by the total parts to find the value of ONE part.<br>3. MULTIPLY the value of one part by each part of the ratio."
            },
            {
                "icon": "fa-solid fa-scale-balanced",
                "title": "When One Share is Already Given",
                "desc": "If the question says 'Sarah receives £120 and the ratio is 3:5', Sarah's £120 corresponds to 3 parts. Divide £120 by 3 to find 1 part (£40), then multiply by 5 for the other share (£200)."
            }
        ],
        "worked_examples": [
            {
                "level": "Level 2 Exam Standard (4 Marks)",
                "question": "A construction site needs 1,200 kg of concrete. Concrete is mixed in the ratio cement : sand : gravel = 1 : 2 : 3. Cement costs £8 per 25 kg bag. Calculate how much the cement will cost for this job.",
                "steps": [
                    {
                        "step": "Step 1",
                        "action": "Add the ratio parts together",
                        "math": "1 + 2 + 3 = 6 parts in total",
                        "mark": "M1 (Method mark for summing parts)"
                    },
                    {
                        "step": "Step 2",
                        "action": "Find the mass of 1 part (cement)",
                        "math": "1,200 kg ÷ 6 = 200 kg of cement needed",
                        "mark": "M1 (Method mark for finding 1 part)"
                    },
                    {
                        "step": "Step 3",
                        "action": "Calculate number of 25 kg bags required",
                        "math": "200 kg ÷ 25 kg = 8 bags",
                        "mark": "M1 (Method mark for bag division)"
                    },
                    {
                        "step": "Step 4",
                        "action": "Calculate total cost of cement bags",
                        "math": "8 bags × £8 = £64.00",
                        "mark": "A1 (Accuracy mark with currency)"
                    }
                ],
                "final_answer": "£64.00"
            }
        ],
        "examiner_traps": [
            {
                "title": "Dividing by the wrong number when one person's share is given",
                "desc": "Students often add all parts together even when the question only gave ONE person's amount instead of the total.",
                "solution": "Check: Does the total amount belong to EVERYONE (sum parts), or to just ONE person (divide by that person's ratio part)?"
            }
        ],
        "practice_questions": [
            {
                "marks": 3,
                "question": "Two colleagues, Liam and Priya, share a bonus of £750 in the ratio 2 : 3. How much money does Priya receive?",
                "solution_steps": "1. Total parts = 2 + 3 = 5 (M1)<br>2. Value of 1 part = £750 ÷ 5 = £150 (M1)<br>3. Priya's share (3 parts) = 3 × £150 = £450 (A1)",
                "correct_answer": "£450.00",
                "tutor_tip": "Check: Liam gets 2 × £150 = £300. £300 + £450 = £750. Total balances perfectly!"
            }
        ]
    }
]

def main():
    base_dir = "/home/subi/Projects/masterfunctionalskills.co.uk"
    worksheets_dir = os.path.join(base_dir, "worksheets")
    os.makedirs(worksheets_dir, exist_ok=True)
    
    for t in TOPICS:
        slug = t['slug']
        print(f"Generating Master Functional Skills topic: {slug}...")
        
        # 1. Topic page
        topic_html = build_topic_page(t)
        topic_path = os.path.join(base_dir, f"functional-skills-{slug}.html")
        with open(topic_path, "w", encoding="utf-8") as f:
            f.write(topic_html)
        print(f"  -> Created {topic_path} ({len(topic_html)} bytes)")
        
        # 2. Printable worksheet
        sheet_html = build_printable_worksheet(t)
        sheet_path = os.path.join(worksheets_dir, f"{slug}-worksheet.html")
        with open(sheet_path, "w", encoding="utf-8") as f:
            f.write(sheet_html)
        print(f"  -> Created {sheet_path} ({len(sheet_html)} bytes)")
        
        # 3. Printable answers
        ans_html = build_printable_answers(t)
        ans_path = os.path.join(worksheets_dir, f"{slug}-answers.html")
        with open(ans_path, "w", encoding="utf-8") as f:
            f.write(ans_html)
        print(f"  -> Created {ans_path} ({len(ans_html)} bytes)")

if __name__ == "__main__":
    main()
