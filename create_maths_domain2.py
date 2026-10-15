#!/usr/bin/env python3
import json

TOPICS_DOMAIN2 = [
    {
        "filename": "functional-skills-ratio.html",
        "clean_topic": "Ratio & Sharing into Parts",
        "intro_lead": "Simplify ratios, write ratios in the unitary form 1 : n, and divide quantities into two or three-part ratios using the total parts method in healthcare and trade scenarios.",
        "next_file": "functional-skills-proportion.html",
        "next_name": "Direct & Inverse Proportion",
        "spec_points": [
            ("L1.11 / L2.11", "Understand and calculate ratio, direct proportion, and scaling."),
            ("L2.11", "Divide an amount into a given ratio of two or three parts.")
        ],
        "golden_rules": [
            {
                "icon": "fa-shapes",
                "title": "Golden Rule 1: The 3-Step Ratio Sharing Blueprint (A-D-M)",
                "desc": "1. Add the ratio parts to find the Total Parts. 2. Divide the total quantity by total parts to find the Value of 1 Part. 3. Multiply by each ratio term.",
                "badge": "1. Add Parts → 2. Divide Total by Parts → 3. Multiply by Each Part"
            },
            {
                "icon": "fa-flask",
                "title": "Golden Rule 2: Dilutions and Ratios: Concentrate vs Water",
                "desc": "In a 1 : 4 dilution ratio, there is 1 part concentrate and 4 parts water, giving 5 TOTAL parts (Concentrate is 1/5 of the total liquid, NOT 1/4).",
                "badge": "Ratio 1 : 4 = 1 + 4 = 5 Total Parts"
            }
        ],
        "skills": [
            {
                "title": "Simplifying Ratios & The Unitary Ratio (1 : n)",
                "summary": "Dividing by Highest Common Factors and expressing ratios with a leading 1.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Simplifying:</strong> Divide both numbers by their highest common factor (HCF): <em>24 : 36 = 2 : 3 (dividing by 12).</em></li>
                    <li><strong>Unitary Ratio (1 : n):</strong> Divide both parts by the first number: <em>4 : 18 = 1 : 4.5 (dividing both by 4).</em></li>
                    <li><strong>Units Must Match:</strong> Convert to the same units before simplifying: <em>50p : £2.50 = 50p : 250p = 1 : 5.</em></li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "NHS Disinfectant Dilution & Ward Cleaning Allocation",
                "marks": "3 Marks (Pearson Edexcel Level 2)",
                "context": "Clinical Decontamination Protocol",
                "question": "An infection control housekeeper must prepare <strong>15 litres</strong> of sanitizing solution. The clinical guidelines require hospital disinfectant concentrate and water to be mixed in the ratio <strong>1 : 4</strong>.<br>(a) How many litres of disinfectant concentrate are needed?<br>(b) How many litres of water are needed?",
                "steps": [
                    ("Step 1", "Add the ratio parts to find the total parts", "1 part concentrate + 4 parts water = 5 total parts.", "M1: Total parts calculation"),
                    ("Step 2", "Find the volume of 1 part", "15 litres ÷ 5 parts = 3 litres per part.", "M1: Value of 1 part division"),
                    ("Step 3", "Multiply by each ratio term", "Concentrate = 1 × 3 L = 3 litres.<br>Water = 4 × 3 L = 12 litres.", "A1: Accurate component volumes")
                ],
                "final_answer": "Disinfectant Concentrate = 3 litres | Water = 12 litres",
                "tutor_tip": "Quick check: 3 L + 12 L = 15 L total. 3 : 12 simplifies to 1 : 4. Both conditions verified."
            }
        ],
        "examiner_traps": [
            {
                "title": "Dividing by One of the Ratio Terms Instead of the Total",
                "desc": "A common blunder is dividing 15 L by 4 (= 3.75 L). You must divide by the SUM of the parts (1 + 4 = 5).",
                "fix": "Always write: 'Total parts = [part 1] + [part 2]' before touching your calculator."
            }
        ],
        "practice_questions": [
            {
                "marks": "3 Marks",
                "question": "A construction firm mixes concrete using cement, sand, and gravel in the ratio <strong>1 : 2 : 4</strong> by weight. The builder needs to prepare <strong>560 kg</strong> of concrete.<br>Calculate the weight of sand required.",
                "solution_steps": "1. Total parts = 1 + 2 + 4 = 7 parts.<br>2. 1 part = 560 ÷ 7 = 80 kg.<br>3. Sand has 2 parts: 2 × 80 kg = 160 kg.",
                "correct_answer": "160 kg of sand",
                "tutor_tip": "Identify which term in the ratio corresponds to sand (the middle term, 2 parts)."
            }
        ]
    },
    {
        "filename": "functional-skills-proportion.html",
        "clean_topic": "Direct & Inverse Proportion",
        "intro_lead": "Solve recipe scaling, workforce scheduling, and machine output problems using unitary proportion and inverse proportion principles.",
        "next_file": "functional-skills-formulas.html",
        "next_name": "Algebra & Formulas",
        "spec_points": [
            ("L1.11 / L2.11", "Calculate direct proportion and scaling in vocational situations."),
            ("L2.11", "Understand and solve problems involving inverse proportion (e.g. workers and time).")
        ],
        "golden_rules": [
            {
                "icon": "fa-scale-balanced",
                "title": "Golden Rule 1: The Unitary Method for Direct Proportion",
                "desc": "Find the value of ONE unit first by dividing, then multiply by the required quantity. If 6 uniforms cost £150, 1 uniform costs £25; 10 uniforms cost £250.",
                "badge": "Total ÷ Known Quantity = 1 Unit → 1 Unit × Desired Quantity"
            },
            {
                "icon": "fa-person-digging",
                "title": "Golden Rule 2: Inverse Proportion: More Workers = Less Time",
                "desc": "When workers increase, the time taken DECREASES proportionally. Multiply workers by hours to get total 'person-hours', then divide by the new workforce.",
                "badge": "Total Person-Hours = Workers × Time → New Time = Total ÷ New Workers"
            }
        ],
        "skills": [
            {
                "title": "Direct vs Inverse Proportion Comparison",
                "summary": "Recognising whether values increase together or move inversely.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Type</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0284c7;">Direct Proportion</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#ea580c;">Inverse Proportion</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Relationship</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">As one quantity increases, the other increases at the same rate.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">As one quantity increases, the other decreases at the same rate.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Classic Scenarios</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Catering recipes, fuel consumption, currency exchange.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Staffing a ward shift, building a wall, packaging crates.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Core Method</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Divide to find 1, then multiply up.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Multiply to find total work, then divide by new team size.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Depot Parcel Sorting Shift Workforce Allocation",
                "marks": "3 Marks (Pearson Edexcel Level 2)",
                "context": "Logistics Hub Operations",
                "question": "It takes <strong>4 warehouse operatives</strong> a total of <strong>6 hours</strong> to unload and sort a freight delivery. If the depot manager brings in <strong>2 additional operatives</strong> (6 operatives in total working at the same pace), how long will the job take?",
                "steps": [
                    ("Step 1", "Calculate total person-hours required", "Total effort = 4 operatives × 6 hours = 24 person-hours.", "M1: Inverse proportion total effort calculation"),
                    ("Step 2", "Determine new workforce size", "4 + 2 = 6 operatives.", "B1: Identifying new worker count"),
                    ("Step 3", "Divide total person-hours by new workforce", "24 person-hours ÷ 6 operatives = 4 hours.", "A1: Accurate reduced duration")
                ],
                "final_answer": "4 hours (a reduction of 2 hours)",
                "tutor_tip": "Notice: 6 operatives must take LESS time than 4. If your answer is more than 6 hours, you used direct proportion by mistake!"
            }
        ],
        "examiner_traps": [
            {
                "title": "Applying Direct Proportion to Staffing Problems",
                "desc": "Calculating 6 ÷ 4 × 6 = 9 hours is a catastrophic error because adding workers should speed up the work, not make it take longer!",
                "fix": "Always ask: 'Should more workers take more time or less time?'"
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A hospital kitchen recipe for 8 resident portions requires 600 grams of minced beef. How many grams of beef are required to prepare 20 resident portions?",
                "solution_steps": "1. 1 portion = 600 ÷ 8 = 75 grams.<br>2. 20 portions = 75 × 20 = 1,500 grams (or 1.5 kg).",
                "correct_answer": "1,500 g (or 1.5 kg)",
                "tutor_tip": "Find the amount for 1 portion first using unitary method."
            }
        ]
    },
    {
        "filename": "functional-skills-formulas.html",
        "clean_topic": "Algebra, Formulas & Substitution",
        "intro_lead": "Substitute numerical values into word and algebraic formulas, rearrange simple formulas, and solve vocational trade and NHS dosage equations.",
        "next_file": "functional-skills-money.html",
        "next_name": "Money & Finance",
        "spec_points": [
            ("L1.13 / L2.13", "Substitute values into given words and symbols formulas in familiar and unfamiliar contexts."),
            ("L2.14", "Rearrange simple linear equations to change the subject of a formula.")
        ],
        "golden_rules": [
            {
                "icon": "fa-square-root-variable",
                "title": "Golden Rule 1: Letters Next to Letters Mean Multiplication",
                "desc": "In algebra, 4h means 4 × h; 2lw means 2 × l × w. Always write in the invisible multiplication signs before substituting values.",
                "badge": "C = 50 + 25h → C = 50 + (25 × h)"
            },
            {
                "icon": "fa-bracket-round",
                "title": "Golden Rule 2: Wrap Negative Substitutions in Brackets",
                "desc": "When substituting a negative number into a squared variable, (-3)² = +9, NOT -9. Always enclose negative values in brackets.",
                "badge": "(-4)² = (-4) × (-4) = +16"
            }
        ],
        "skills": [
            {
                "title": "Step-by-Step Substitution Method",
                "summary": "Converting formulas into solvable numerical equations.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Write the formula clearly:</strong> e.g. <em>Cost = Callout + (Hourly Rate × Hours).</em></li>
                    <li><strong>Replace letters with numbers:</strong> Write numbers directly below the corresponding variables.</li>
                    <li><strong>Apply BIDMAS:</strong> Perform bracketed terms and multiplications before additions.</li>
                  </ol>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Clinical BMI & Paediatric Dosage Formulation",
                "marks": "3 Marks (Pearson Edexcel Level 2)",
                "context": "Healthcare Clinical Calculations",
                "question": "The formula for patient drug dose in milligrams is:<br><strong>Dose = (Age in years ÷ [Age in years + 12]) × Adult Dose</strong><br>A 6-year-old child requires medicine where the adult dose is <strong>240 mg</strong>. Calculate the child's dose.",
                "steps": [
                    ("Step 1", "Substitute Age = 6 and Adult Dose = 240 into formula", "Dose = (6 ÷ [6 + 12]) × 240", "M1: Correct numerical substitution"),
                    ("Step 2", "Resolve the bracketed denominator: 6 + 12 = 18", "Dose = (6 ÷ 18) × 240", "M1: Order of operations"),
                    ("Step 3", "Simplify fraction and calculate final dose", "6/18 = 1/3.<br>Dose = 1/3 × 240 = 240 ÷ 3 = 80 mg.", "A1: Accurate medication dosage")
                ],
                "final_answer": "Child Dose = 80 mg",
                "tutor_tip": "Notice how 6/18 simplifies to 1/3, making 240 ÷ 3 = 80 straightforward without a calculator."
            }
        ],
        "examiner_traps": [
            {
                "title": "Adding Before Multiplying in Pricing Formulas",
                "desc": "In Cost = 40 + 20h with h = 3, adding 40 + 20 = 60 then 60 × 3 = 180 is wrong. The multiplication must be done first: 20 × 3 = 60, then 40 + 60 = 100.",
                "fix": "Always underline the multiplication term first: Cost = 40 + [20 × h]."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A plumber uses the formula: <strong>Total Charge = 45 + 32h</strong>, where h is the number of hours worked. Calculate the total charge for a job lasting 4.5 hours.",
                "solution_steps": "1. Substitute h = 4.5: Total = 45 + (32 × 4.5).<br>2. 32 × 4.5 = 144.<br>3. Total = 45 + 144 = £189.00.",
                "correct_answer": "£189.00",
                "tutor_tip": "Remember to write the answer as currency with a pound sign (£189.00)."
            }
        ]
    },
    {
        "filename": "functional-skills-money.html",
        "clean_topic": "Money, Invoicing & Payroll Calculations",
        "intro_lead": "Calculate gross pay, net pay, wage slip deductions (PAYE tax, National Insurance, pension), balance workplace budgets, and compute customer invoices with VAT.",
        "next_file": "functional-skills-best-buys.html",
        "next_name": "Best Buys & Unit Pricing",
        "spec_points": [
            ("L1.14 / L2.15", "Calculate with money and solve problems involving wage slips, invoices, and household/workplace budgets."),
            ("L2.16", "Calculate percentage discounts, VAT, and National Insurance deductions.")
        ],
        "golden_rules": [
            {
                "icon": "fa-receipt",
                "title": "Golden Rule 1: Net Pay = Gross Pay - Total Deductions",
                "desc": "Gross pay is your earnings before anything is taken off. Deductions (Income Tax, NI, Pension) are subtracted from Gross to leave Net Pay ('take-home pay').",
                "badge": "Net Pay = Gross Pay - (Tax + NI + Pension)"
            },
            {
                "icon": "fa-percent",
                "title": "Golden Rule 2: Adding 20% Standard UK VAT",
                "desc": "To add 20% VAT to a net amount, multiply by 1.20 (or find 10%, double it to get 20%, and add).",
                "badge": "Gross Price with VAT = Net Price × 1.20"
            }
        ],
        "skills": [
            {
                "title": "Understanding the Standard Workplace Payslip",
                "summary": "Key lines and calculations on an employee payslip.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Earnings</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Amount</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Deductions</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Amount</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:8px; border:1px solid #cbd5e1;">Basic Salary (37.5 hrs)</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">£1,850.00</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">PAYE Income Tax</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">£164.20</td>
                      </tr>
                      <tr>
                        <td style="padding:8px; border:1px solid #cbd5e1;">Overtime (10 hrs @ 1.5×)</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">£220.00</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">National Insurance</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">£112.50</td>
                      </tr>
                      <tr>
                        <td style="padding:8px; border:1px solid #cbd5e1;"><strong>Total Gross Pay</strong></td>
                        <td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">£2,070.00</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">Workplace Pension (5%)</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">£103.50</td>
                      </tr>
                      <tr style="background:#e0f2fe; font-weight:800; color:#0369a1;">
                        <td colspan="2" style="padding:10px; border:1px solid #cbd5e1; text-align:right;">Total Deductions:</td>
                        <td colspan="2" style="padding:10px; border:1px solid #cbd5e1;">£380.20</td>
                      </tr>
                      <tr style="background:#dcfce7; font-weight:800; color:#166534;">
                        <td colspan="2" style="padding:10px; border:1px solid #cbd5e1; text-align:right;">Final Net Take-Home Pay:</td>
                        <td colspan="2" style="padding:10px; border:1px solid #cbd5e1;">£1,689.80</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Hospital Facility Maintenance Contractor Invoice",
                "marks": "3 Marks (Pearson Edexcel Level 2)",
                "context": "Healthcare Facility Contract Billing",
                "question": "A facilities contractor completes electrical safety testing across Ward 2. The invoice details are:<br>• Labour: 14 hours at £32.50 per hour<br>• Replacement parts: £145.00<br>• VAT: 20% on the subtotal<br>Calculate the total amount payable on the invoice.",
                "steps": [
                    ("Step 1", "Calculate total labour cost", "14 hours × £32.50 = £455.00", "M1: Labour multiplication"),
                    ("Step 2", "Calculate subtotal before VAT", "£455.00 + £145.00 = £600.00", "M1: Subtotal addition"),
                    ("Step 3", "Calculate 20% VAT and total invoice amount", "20% of £600 = 0.20 × 600 = £120.00.<br>Total payable = £600.00 + £120.00 = £720.00.", "A1: Accurate final total with VAT")
                ],
                "final_answer": "Total Amount Payable = £720.00",
                "tutor_tip": "You can also calculate the total in a single step: £600.00 × 1.20 = £720.00."
            }
        ],
        "examiner_traps": [
            {
                "title": "Applying VAT Only to Materials and Forgetting Labour",
                "desc": "Unless explicitly stated otherwise, VAT applies to the TOTAL subtotal of labour PLUS parts.",
                "fix": "Always sum all line items first before applying the VAT percentage."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "An employee has a gross monthly salary of £2,400. Deductions are: Income Tax £285.40, National Insurance £168.20, and Pension £120.00. Calculate their net take-home pay.",
                "solution_steps": "1. Total deductions = 285.40 + 168.20 + 120.00 = £573.60.<br>2. Net pay = 2,400.00 - 573.60 = £1,826.40.",
                "correct_answer": "£1,826.40",
                "tutor_tip": "Double check your subtraction: 2,400 - 573.60 = £1,826.40."
            }
        ]
    },
    {
        "filename": "functional-skills-best-buys.html",
        "clean_topic": "Best Buys & Unit Pricing",
        "intro_lead": "Compare supermarket multi-buys, packaging sizes, and trade discounts by calculating the unit price (price per gram, per kilogram, or per unit) to determine the best financial value.",
        "next_file": "functional-skills-interest-and-compound-interest.html",
        "next_name": "Simple & Compound Interest",
        "spec_points": [
            ("L1.15 / L2.17", "Compare costs and unit pricing (e.g. price per 100g, per litre) to determine the best value option.")
        ],
        "golden_rules": [
            {
                "icon": "fa-tag",
                "title": "Golden Rule 1: Unit Price = Cost ÷ Quantity",
                "desc": "Always divide the PRICE by the QUANTITY to find the cost of 1 unit (1 gram, 1 kg, 1 litre). The option with the LOWEST unit price is the best value.",
                "badge": "Unit Price = £ Price ÷ Quantity"
            },
            {
                "icon": "fa-scale-unbalanced-flip",
                "title": "Golden Rule 2: Convert to Common Units Before Dividing",
                "desc": "Never compare a 750g tub with a 2 kg tub directly. Convert 2 kg to 2,000g, or compare both per 100g.",
                "badge": "Match units first: grams to grams, ml to ml"
            }
        ],
        "skills": [
            {
                "title": "Two Comparison Methods: Unit Cost vs Common Quantity",
                "summary": "Comparing multi-pack promotions mathematically.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Method 1: Unit Cost (Price ÷ Weight):</strong> 500g for £2.50 = 250p ÷ 500 = 0.50p per gram.</li>
                    <li><strong>Method 2: Scaling to Common Quantity:</strong> If comparing 400g for £1.60 and 800g for £3.00, double the 400g pack: 2 × £1.60 = £3.20. Since £3.00 < £3.20, the 800g pack is better value.</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Care Home Laundry Detergent Procurement Comparison",
                "marks": "3 Marks (Pearson Edexcel Level 2)",
                "context": "Care Facility Commercial Purchasing",
                "question": "A care home procurement manager must purchase commercial laundry detergent. Two brands are available:<br>• Brand A: <strong>4.5 litres</strong> for <strong>£14.40</strong><br>• Brand B: <strong>6 litres</strong> for <strong>£18.60</strong><br>(a) Calculate the cost per litre for each brand.<br>(b) Which brand offers the best value for money?",
                "steps": [
                    ("Step 1", "Calculate cost per litre for Brand A", "£14.40 ÷ 4.5 litres = £3.20 per litre.", "M1: Brand A unit division"),
                    ("Step 2", "Calculate cost per litre for Brand B", "£18.60 ÷ 6 litres = £3.10 per litre.", "M1: Brand B unit division"),
                    ("Step 3", "Compare unit prices and conclude", "Brand B is £3.10 per litre, which is 10p cheaper per litre than Brand A (£3.20). Therefore, Brand B offers the best value.", "A1: Correct comparison and conclusion")
                ],
                "final_answer": "(a) Brand A = £3.20/L, Brand B = £3.10/L | (b) Brand B is the best value (10p cheaper per litre).",
                "tutor_tip": "Always conclude with a written sentence naming the winning option and stating the cost difference."
            }
        ],
        "examiner_traps": [
            {
                "title": "Dividing Quantity by Price Instead of Price by Quantity",
                "desc": "Calculating 4.5 ÷ 14.40 = 0.3125 gives litres per pound, not cost per litre. While mathematically valid, it leads to confusion about whether higher or lower is better.",
                "fix": "Always do Money ÷ Amount: Cost per Litre = £ ÷ Litres."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A supermarket sells olive oil in two bottle sizes: 250 ml for £2.80, and 750 ml for £7.20. Which size is better value?",
                "solution_steps": "1. Scale 250 ml up to 750 ml: 3 × £2.80 = £8.40.<br>2. Compare: £7.20 for 750 ml is cheaper than £8.40.<br>3. Conclusion: The 750 ml bottle is better value.",
                "correct_answer": "750 ml bottle is better value (£7.20 vs £8.40 for 750 ml).",
                "tutor_tip": "Multiplying 250 ml by 3 is faster and cleaner than dividing."
            }
        ]
    },
    {
        "filename": "functional-skills-interest-and-compound-interest.html",
        "clean_topic": "Simple & Compound Interest",
        "intro_lead": "Calculate annual simple interest, compound interest over multi-year periods, compare savings accounts and loan repayments, and compute investment growth.",
        "next_file": "functional-skills-time.html",
        "next_name": "Time & Timetables",
        "spec_points": [
            ("L2.16", "Calculate simple interest and compound interest on loans and savings over multiple periods.")
        ],
        "golden_rules": [
            {
                "icon": "fa-coins",
                "title": "Golden Rule 1: Simple Interest Remains Constant Every Year",
                "desc": "Simple interest is calculated only on the original principal amount. If £2,000 earns 5% simple interest, it earns £100 every single year.",
                "badge": "Simple Interest = Principal × Rate × Time"
            },
            {
                "icon": "fa-chart-line",
                "title": "Golden Rule 2: Compound Interest: Interest on Interest",
                "desc": "Compound interest adds each year's interest to the balance before calculating the next year's interest. Use the multiplier method: Balance × (1 + r)^n.",
                "badge": "Compound: Principal × (Multiplier)^Years"
            }
        ],
        "skills": [
            {
                "title": "Year-by-Year vs Multiplier Method for Compound Interest",
                "summary": "Two reliable methods for non-calculator and calculator papers.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">To calculate £5,000 invested at 4% compound interest for 2 years:</p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Year-by-Year Method:</strong><br>
                    Year 1: 4% of £5,000 = £200 → New balance = £5,200.<br>
                    Year 2: 4% of £5,200 = £208 → Final balance = £5,408.</li>
                    <li><strong>Multiplier Method (Calculator):</strong><br>
                    Multiplier for +4% = 1.04.<br>
                    Final Balance = £5,000 × (1.04)² = £5,000 × 1.0816 = £5,408.00.</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Care Home Capital Equipment Reserve Investment",
                "marks": "3 Marks (Pearson Edexcel Level 2)",
                "context": "Healthcare Reserve Fund Management",
                "question": "A care home trustees board invests <strong>£12,000</strong> in a fixed-rate savings bond paying <strong>3% compound interest per annum</strong> for <strong>3 years</strong>.<br>Calculate the total interest earned over the 3 years.",
                "steps": [
                    ("Step 1", "Calculate Year 1 interest and balance", "3% of £12,000 = 0.03 × 12,000 = £360.<br>Balance at end of Year 1 = £12,000 + £360 = £12,360.", "M1: Year 1 calculation"),
                    ("Step 2", "Calculate Year 2 interest and balance", "3% of £12,360 = 0.03 × 12,360 = £370.80.<br>Balance at end of Year 2 = £12,360 + £370.80 = £12,730.80.", "M1: Year 2 compound step"),
                    ("Step 3", "Calculate Year 3 interest and total interest earned", "3% of £12,730.80 = 0.03 × 12,730.80 = £381.92.<br>Final Balance = £13,112.72.<br>Total Interest Earned = £13,112.72 - £12,000 = £1,112.72.", "A1: Accurate total interest earned")
                ],
                "final_answer": "Total Interest Earned = £1,112.72",
                "tutor_tip": "Notice the question asks for the TOTAL INTEREST EARNED, not the final balance! Always subtract the starting principal (£12,000)."
            }
        ],
        "examiner_traps": [
            {
                "title": "Giving the Final Balance Instead of the Interest",
                "desc": "If the question asks 'How much interest was earned?', stating £13,112.72 forfeits the final accuracy mark.",
                "fix": "Highlight the word 'interest' or 'total balance' in the question stem."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A worker takes a loan of £3,500 at 6% simple interest per year. How much total interest will they pay over 4 years?",
                "solution_steps": "1. 1 year interest = 6% of £3,500 = 0.06 × 3,500 = £210.<br>2. 4 years total interest = £210 × 4 = £840.00.",
                "correct_answer": "£840.00",
                "tutor_tip": "Simple interest is the same every year: £210 × 4."
            }
        ]
    },
    {
        "filename": "functional-skills-problems-involving-money.html",
        "clean_topic": "Problems Involving Money & Multi-Tier Pricing",
        "intro_lead": "Solve complex, multi-stage financial problems involving travel fares, group admissions, discounts, currency exchange, and household utility bill comparisons.",
        "next_file": "functional-skills-time.html",
        "next_name": "Time & Timetables",
        "spec_points": [
            ("L1.14 / L2.15", "Solve multi-step problems involving money and budgeting in everyday contexts.")
        ],
        "golden_rules": [
            {
                "icon": "fa-list-check",
                "title": "Golden Rule 1: Deconstruct Multi-Tier Pricing into Line Items",
                "desc": "Break pricing into: 1. Base fee / Callout. 2. Per-unit or hourly charge. 3. Discounts. 4. VAT or taxes. Sum systematically.",
                "badge": "Base Fee + (Rate × Units) - Discounts + Taxes"
            },
            {
                "icon": "fa-sterling-sign",
                "title": "Golden Rule 2: Mind the Pence-to-Pounds Conversion",
                "desc": "Never mix pounds and pence without converting. 45p + £3.20 is NOT 48.20! Convert 45p to £0.45 before adding (£0.45 + £3.20 = £3.65).",
                "badge": "45p = £0.45 (Divide pence by 100)"
            }
        ],
        "skills": [
            {
                "title": "Currency Exchange Calculations",
                "summary": "Converting between GBP and foreign currencies.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>GBP to Foreign Currency:</strong> Multiply by exchange rate: <em>£500 × 1.15 = €575.00.</em></li>
                    <li><strong>Foreign Currency to GBP:</strong> Divide by exchange rate: <em>€460 ÷ 1.15 = £400.00.</em></li>
                    <li><strong>Deduct Commission:</strong> If an agency charges 2% commission, subtract 2% before exchanging.</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Care Home Resident Day Trip Outing Budget",
                "marks": "3 Marks (Pearson Edexcel Level 2)",
                "context": "Care Home Activities Coordination",
                "question": "An activities coordinator organizes a botanical garden trip for <strong>18 residents and 4 care assistants</strong>. Admission costs:<br>• Adult: £15.00<br>• Senior (resident): £10.50<br>• Group discount: 15% off total ticket price for groups over 20 people.<br>Calculate the total discounted ticket cost.",
                "steps": [
                    ("Step 1", "Calculate gross ticket costs before discount", "4 adults × £15.00 = £60.00<br>18 seniors × £10.50 = £189.00<br>Total gross = £60.00 + £189.00 = £249.00", "M1: Line item multiplication and sum"),
                    ("Step 2", "Verify group size qualification for discount", "18 + 4 = 22 people. Since 22 > 20, the 15% discount applies.", "B1: Qualification check"),
                    ("Step 3", "Calculate 15% discount and net payable", "15% of £249 = 0.15 × 249 = £37.35.<br>Discounted total = £249.00 - £37.35 = £211.65.", "A1: Accurate discounted total")
                ],
                "final_answer": "Total Discounted Cost = £211.65",
                "tutor_tip": "You can also calculate 85% of £249.00 directly: 249 × 0.85 = £211.65."
            }
        ],
        "examiner_traps": [
            {
                "title": "Forgetting Staff in Group Counts",
                "desc": "Counting only the 18 residents and failing to realize that staff count towards the 20-person group qualification.",
                "fix": "Always sum total attendees (residents + staff) first."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A staff canteen offers a 10% discount on orders over £25. A department orders 6 sandwiches at £3.50 each and 4 coffees at £2.25 each. What is the total discounted cost?",
                "solution_steps": "1. 6 × 3.50 = £21.00; 4 × 2.25 = £9.00.<br>2. Subtotal = £21 + £9 = £30.00 (qualifies for 10% discount).<br>3. 10% discount = £3.00. Total = £30 - £3 = £27.00.",
                "correct_answer": "£27.00",
                "tutor_tip": "Check that the subtotal exceeds £25 before applying the discount."
            }
        ]
    }
]

# Write out domain 2
with open("/home/subi/Projects/masterfunctionalskills.co.uk/maths_domain2_finance_ratio.py", "w", encoding="utf-8") as f:
    f.write("#!/usr/bin/env python3\n")
    f.write('"""Maths Domain 2: Ratio, Proportion & Financial Maths (7 Core Topics)"""\n\n')
    f.write("TOPICS_DOMAIN2 = " + repr(TOPICS_DOMAIN2) + "\n")

print(f"Domain 2 written with {len(TOPICS_DOMAIN2)} topics!")
