#!/usr/bin/env python3
"""
Master Functional Skills - Core Maths Data for Skill Workouts (Procedural Fluency & Repetition).
Features high-repetition drill items (a-h) testing integers, money, decimals, units, and edge cases,
paired with realistic adult vocational application scenarios (NHS, construction, retail, warehousing).
"""

WORKOUT_CORE_MATHS = {
    # 1. PERCENTAGES
    "percentages": {
        "title": "Percentages",
        "spec_codes": "Pearson Edexcel: L1.10 • L2.11 • L2.12",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Core Rules & Mental Fluency Shortcuts",
            "points": [
                "10%: Divide by 10 (shift digits 1 place right).",
                "5%: Find 10% and divide by 2.",
                "1%: Divide by 100 (shift digits 2 places right).",
                "20%: Find 10% and multiply by 2 (or divide by 5).",
                "Percentage Increase: Original Amount + Calculated Percentage (or multiply by 1 + percentage/100).",
                "Percentage Decrease: Original Amount - Calculated Percentage (or multiply by 1 - percentage/100)."
            ],
            "calc_tip": "To find a percentage on a calculator, multiply by the decimal multiplier (e.g. 15% of £480 = 480 × 0.15 = £72. To increase by 8%, multiply by 1.08)."
        },
        "workout_blocks": [
            {
                "title": "Non-Calculator Percentage of Amounts (Mental Benchmarks)",
                "instruction": "Work out each percentage mentally using benchmark values (10%, 5%, 1%):",
                "prefix": "£",
                "items": [
                    ("a", "10% of £60", "£6.00"),
                    ("b", "10% of £180", "£18.00"),
                    ("c", "5% of £40", "£2.00"),
                    ("d", "5% of £120", "£6.00"),
                    ("e", "20% of £70", "£14.00"),
                    ("f", "20% of £250", "£50.00"),
                    ("g", "15% of £80", "£12.00"),
                    ("h", "15% of £240", "£36.00")
                ]
            },
            {
                "title": "Percentage Increases (Money & Metric Units)",
                "instruction": "Increase each amount by the percentage indicated:",
                "items": [
                    ("a", "Increase £40 by 10%", "£44.00"),
                    ("b", "Increase £90 by 20%", "£108.00"),
                    ("c", "Increase 60 kg by 5%", "63 kg"),
                    ("d", "Increase 120 litres by 15%", "138 litres"),
                    ("e", "Increase £250 by 8%", "£270.00"),
                    ("f", "Increase 80 m by 25%", "100 m"),
                    ("g", "Increase £450 by 20% (VAT)", "£540.00"),
                    ("h", "Increase 500 hours by 12%", "560 hours")
                ]
            },
            {
                "title": "Percentage Decreases (Discounts & Deductions)",
                "instruction": "Decrease each amount by the percentage indicated:",
                "items": [
                    ("a", "Decrease £80 by 10%", "£72.00"),
                    ("b", "Decrease £150 by 20%", "£120.00"),
                    ("c", "Decrease 200 kg by 5%", "190 kg"),
                    ("d", "Decrease 40 metres by 15%", "34 metres"),
                    ("e", "Decrease £320 by 25%", "£240.00"),
                    ("f", "Decrease £600 by 12.5%", "£525.00"),
                    ("g", "Decrease 90 ml by 30%", "63 ml"),
                    ("h", "Decrease £1,200 by 35%", "£780.00")
                ]
            },
            {
                "title": "Reverse Percentages & Calculator Multipliers (Level 2)",
                "instruction": "Find the original value before the percentage change occurred:",
                "items": [
                    ("a", "10% of a number is £14. Find the number.", "£140.00"),
                    ("b", "25% of a weight is 18 kg. Find total weight.", "72 kg"),
                    ("c", "A coat reduced by 20% costs £64. Find original price.", "£80.00"),
                    ("d", "A bill including 20% VAT is £108. Find cost before VAT.", "£90.00"),
                    ("e", "A salary after 5% raise is £25,200. Find previous salary.", "£24,000.00"),
                    ("f", "A fuel tank is 40% full with 28 litres. Find total capacity.", "70 litres")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "NHS Healthcare & Pay",
                "stem": "An NHS healthcare assistant earns an hourly rate of <strong>£11.80</strong>. She receives an agreed cost-of-living pay increase of <strong>5%</strong>.<br>Work out her new hourly rate of pay.",
                "marks": 2,
                "prefix": "£",
                "steps": [
                    ("Calculate 5% of £11.80: 11.80 × 0.05 = £0.59 (or 10% = £1.18, halve to get £0.59)", "[M1]"),
                    ("Add increase to original pay: £11.80 + £0.59 = £12.39", "[A1]")
                ],
                "final_answer": "£12.39 per hour",
                "reverse_check": "£12.39 - £0.59 = £11.80.",
                "pitfall": "Forgetting to add the increase back to the original base pay."
            },
            {
                "context_tag": "Retail & Trade Invoicing",
                "stem": "A plumbing merchant sells a commercial boiler for <strong>£850 excluding VAT</strong>.<br>VAT is charged at <strong>20%</strong>.<br>Calculate the total cost of the boiler including VAT.",
                "marks": 2,
                "prefix": "£",
                "steps": [
                    ("Calculate 20% VAT: 10% of £850 = £85; 20% = £85 × 2 = £170", "[M1]"),
                    ("Add VAT to net price: £850 + £170 = £1,020", "[A1]")
                ],
                "final_answer": "£1,020.00",
                "reverse_check": "£1,020 ÷ 1.20 = £850.00.",
                "pitfall": "Calculating 20% but failing to add it to the net figure."
            },
            {
                "context_tag": "Warehousing & Logistics",
                "stem": "A distribution centre received <strong>1,400 packages</strong> today. <strong>35%</strong> of the packages require refrigerated storage.<br>How many packages do not require refrigeration?",
                "marks": 3,
                "unit": "packages",
                "steps": [
                    ("Method 1: Refrigerated = 1,400 × 0.35 = 490 packages (or 10% = 140, 30% = 420, 5% = 70 → 490)", "[M1]"),
                    ("Subtract from total: 1,400 - 490 = 910 packages (or directly 65% of 1,400)", "[M1]"),
                    ("Final accuracy: 910 non-refrigerated packages", "[A1]")
                ],
                "final_answer": "910 packages",
                "reverse_check": "910 + 490 = 1,400 total packages.",
                "pitfall": "Providing the number of refrigerated packages (490) instead of the packages that DO NOT require refrigeration."
            },
            {
                "context_tag": "Catering & Hospitality Margin",
                "stem": "A restaurant purchases wine at <strong>£6.40 per bottle</strong>. The restaurant marks up the price by <strong>225%</strong> before selling.<br>Work out the selling price per bottle.",
                "marks": 3,
                "prefix": "£",
                "steps": [
                    ("Calculate 225% markup: 6.40 × 2.25 = £14.40", "[M1]"),
                    ("Add markup to cost price: £6.40 + £14.40 = £20.80", "[M1]"),
                    ("State definitive selling price: £20.80", "[A1]")
                ],
                "final_answer": "£20.80",
                "reverse_check": "£20.80 - £14.40 = £6.40.",
                "pitfall": "Thinking 225% is the selling price itself, rather than adding the markup to the original cost."
            },
            {
                "context_tag": "Construction Material Waste",
                "stem": "A site carpenter orders <strong>480 square metres</strong> of timber cladding. The supplier recommends ordering an additional <strong>15%</strong> to allow for cutting waste.<br>How many square metres of cladding should the carpenter order in total?",
                "marks": 2,
                "unit": "m²",
                "steps": [
                    ("Calculate 15% allowance: 480 × 0.15 = 72 m² (or 10% = 48, 5% = 24 → 48 + 24 = 72)", "[M1]"),
                    ("Add to baseline order: 480 + 72 = 552 m²", "[A1]")
                ],
                "final_answer": "552 m²",
                "reverse_check": "552 - 72 = 480 m².",
                "pitfall": "Rounding errors or omitting the 5% component."
            },
            {
                "context_tag": "Commercial Sales & Clearance",
                "stem": "During an end-of-season sale, a power drill is offered at <strong>£72</strong> after a <strong>20% discount</strong> has been applied.<br>What was the original price of the power drill before the sale?",
                "marks": 3,
                "prefix": "£",
                "steps": [
                    ("Recognize that £72 represents 80% of original price (100% - 20% = 80%)", "[M1]"),
                    ("Calculate 1%: 72 ÷ 80 = 0.90; Calculate 100%: 0.90 × 100 = 90 (or 72 ÷ 0.8)", "[M1]"),
                    ("State original price: £90.00", "[A1]")
                ],
                "final_answer": "£90.00",
                "reverse_check": "20% of £90 = £18; £90 - £18 = £72.",
                "pitfall": "Working out 20% of £72 (£14.40) and adding it (£86.40). The 20% discount was applied to the original price, not the sale price!"
            }
        ]
    },

    # 2. FRACTIONS
    "fractions": {
        "title": "Fractions",
        "spec_codes": "Pearson Edexcel: L1.9 • L2.8 • L2.9",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Core Rules & Operational Mechanics",
            "points": [
                "Fraction of an Amount: Divide by the denominator (bottom), then multiply by the numerator (top).",
                "Simplifying: Divide numerator and denominator by their Highest Common Factor (HCF).",
                "Adding & Subtracting: Match denominators first using a common multiple, then add/subtract numerators only.",
                "Multiplying: Multiply straight across (top × top, bottom × bottom).",
                "Dividing: Keep, Change, Flip (KCF) — multiply by the reciprocal of the second fraction."
            ],
            "calc_tip": "Use the fraction key [a b/c] or [x/y] on scientific calculators to verify mixed number operations."
        },
        "workout_blocks": [
            {
                "title": "Simplifying Fractions to Lowest Terms",
                "instruction": "Cancel down each fraction to its simplest form:",
                "items": [
                    ("a", "Simplify 12/16", "3/4"),
                    ("b", "Simplify 15/25", "3/5"),
                    ("c", "Simplify 18/24", "3/4"),
                    ("d", "Simplify 28/35", "4/5"),
                    ("e", "Simplify 24/60", "2/5"),
                    ("f", "Simplify 45/60", "3/4"),
                    ("g", "Simplify 36/48", "3/4"),
                    ("h", "Simplify 50/125", "2/5")
                ]
            },
            {
                "title": "Fraction of Amounts (Mental & Written)",
                "instruction": "Calculate the fraction of each quantity (divide by bottom, multiply by top):",
                "items": [
                    ("a", "1/4 of £80", "£20.00"),
                    ("b", "3/4 of £80", "£60.00"),
                    ("c", "1/3 of 90 kg", "30 kg"),
                    ("d", "2/3 of 90 kg", "60 kg"),
                    ("e", "1/5 of £150", "£30.00"),
                    ("f", "3/5 of £150", "£90.00"),
                    ("g", "3/8 of 64 litres", "24 litres"),
                    ("h", "5/8 of £320", "£200.00")
                ]
            },
            {
                "title": "Adding and Subtracting Proper Fractions",
                "instruction": "Find a common denominator, then calculate the result:",
                "items": [
                    ("a", "1/4 + 1/2", "3/4"),
                    ("b", "3/8 + 1/4", "5/8"),
                    ("c", "2/5 + 3/10", "7/10"),
                    ("d", "1/3 + 1/6", "1/2"),
                    ("e", "3/4 - 1/2", "1/4"),
                    ("f", "7/8 - 3/4", "1/8"),
                    ("g", "5/6 - 1/3", "1/2"),
                    ("h", "9/10 - 2/5", "1/2")
                ]
            },
            {
                "title": "Mixed Numbers & Fraction Multiplication (Level 2)",
                "instruction": "Work out each operation, simplifying your answer:",
                "items": [
                    ("a", "1 1/2 + 2 1/4", "3 3/4"),
                    ("b", "2 1/3 + 1 1/6", "3 1/2"),
                    ("c", "3 3/4 - 1 1/2", "2 1/4"),
                    ("d", "1/2 × 3/4", "3/8"),
                    ("e", "2/3 × 3/5", "2/5"),
                    ("f", "3/4 ÷ 1/2", "1 1/2")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "NHS Hospital Timesheet",
                "stem": "A staff nurse works <strong>37 1/2 hours</strong> per week. Over four weeks, she spends <strong>2/5</strong> of her total working hours in surgical triage.<br>How many hours does she spend in surgical triage over the four weeks?",
                "marks": 3,
                "unit": "hours",
                "steps": [
                    ("Calculate total hours worked over 4 weeks: 37.5 × 4 = 150 hours", "[M1]"),
                    ("Calculate 2/5 of 150 hours: (150 ÷ 5) × 2 = 30 × 2 = 60 hours", "[M1]"),
                    ("State final triage hours: 60 hours", "[A1]")
                ],
                "final_answer": "60 hours",
                "reverse_check": "60 ÷ 150 = 6/15 = 2/5.",
                "pitfall": "Calculating 2/5 of one week (15 hrs) and forgetting to multiply by 4 weeks."
            },
            {
                "context_tag": "Construction Timber Cutting",
                "stem": "A joiner has an oak timber beam measuring <strong>4 1/2 metres</strong> long. He cuts off a piece measuring <strong>1 3/4 metres</strong> for a door lintel.<br>What length of timber remains?",
                "marks": 2,
                "unit": "metres",
                "steps": [
                    ("Set up common denominator (quarters): 4 2/4 - 1 3/4 = 3 6/4 - 1 3/4 = 2 3/4 metres (or 4.5 - 1.75 = 2.75)", "[M1]"),
                    ("Give exact fraction answer: 2 3/4 metres (or 2.75 m)", "[A1]")
                ],
                "final_answer": "2 3/4 metres",
                "reverse_check": "2 3/4 + 1 3/4 = 3 + 6/4 = 4 2/4 = 4 1/2 metres.",
                "pitfall": "Subtracting whole numbers and numerators directly (4 - 1 = 3, 3 - 2 = 1) without borrowing."
            },
            {
                "context_tag": "Commercial Recipe Scaling",
                "stem": "A catering recipe for artisan bread requires <strong>3/8 kg of rye flour</strong> per batch. A baker plans to bake <strong>16 batches</strong> today.<br>How many kilograms of rye flour does the baker need?",
                "marks": 2,
                "unit": "kg",
                "steps": [
                    ("Multiply batch amount by 16: (3/8) × 16 = (3 × 16) ÷ 8 = 48 ÷ 8 = 6 kg", "[M1]"),
                    ("State required rye flour: 6 kg", "[A1]")
                ],
                "final_answer": "6 kg",
                "reverse_check": "6 ÷ 16 = 6/16 = 3/8 kg per batch.",
                "pitfall": "Inverting the fraction or dividing 16 by 3/8."
            },
            {
                "context_tag": "Retail Stock Inventory",
                "stem": "A warehouse holds <strong>480 electrical appliances</strong>.<br>• <strong>1/3</strong> are microwave ovens.<br>• <strong>3/8</strong> are air fryers.<br>• The remainder are kettle and toaster sets.<br>How many kettle and toaster sets are in stock?",
                "marks": 3,
                "unit": "appliances",
                "steps": [
                    ("Microwave count: 480 ÷ 3 = 160", "[M1]"),
                    ("Air fryer count: (480 ÷ 8) × 3 = 60 × 3 = 180", "[M1]"),
                    ("Remaining sets: 480 - (160 + 180) = 480 - 340 = 140", "[A1]")
                ],
                "final_answer": "140 appliances",
                "reverse_check": "160 + 180 + 140 = 480 appliances.",
                "pitfall": "Calculating 3/8 of the remaining stock rather than the total original stock."
            },
            {
                "context_tag": "Charity Fundraising Allocation",
                "stem": "A community fundraising event raises <strong>£2,400</strong>. The committee allocates <strong>5/12</strong> to a local foodbank and <strong>3/8</strong> to a youth centre.<br>How much money remains for administrative costs?",
                "marks": 3,
                "prefix": "£",
                "steps": [
                    ("Foodbank allocation: (2,400 ÷ 12) × 5 = 200 × 5 = £1,000", "[M1]"),
                    ("Youth centre allocation: (2,400 ÷ 8) × 3 = 300 × 3 = £900", "[M1]"),
                    ("Remaining balance: £2,400 - (£1,000 + £900) = £2,400 - £1,900 = £500", "[A1]")
                ],
                "final_answer": "£500.00",
                "reverse_check": "1,000 + 900 + 500 = £2,400.",
                "pitfall": "Adding numerators without finding common denominators."
            },
            {
                "context_tag": "Commercial Flooring Waste",
                "stem": "An office refurbishment project requires <strong>180 m²</strong> of carpet tiles. Due to layout cuts and wastage, the contractor must purchase <strong>1 1/10 times</strong> the net floor area.<br>How many square metres of carpet tiles must be purchased?",
                "marks": 2,
                "unit": "m²",
                "steps": [
                    ("Calculate 1 1/10 of 180: 180 × 1.1 = 198 m² (or 180 + 180/10 = 180 + 18 = 198)", "[M1]"),
                    ("State total carpet tiles to order: 198 m²", "[A1]")
                ],
                "final_answer": "198 m²",
                "reverse_check": "198 ÷ 1.1 = 180 m².",
                "pitfall": "Multiplying by 1.01 instead of 1.1 (1/10 = 0.1)."
            }
        ]
    },

    # 3. RATIO & PROPORTION
    "proportion": {
        "title": "Ratio and Proportion",
        "spec_codes": "Pearson Edexcel: L1.11 • L2.13 • L2.14",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Core Rules & Operational Mechanics",
            "points": [
                "Sharing into a Ratio: 1. Add all parts together. 2. Divide total amount by total parts to find value of 1 part. 3. Multiply 1 part by each ratio number.",
                "Simplifying Ratios: Divide all parts by the Highest Common Factor (HCF). Ratios have no units!",
                "Unit Proportion (Best Buys): Find cost of 1 unit (Price ÷ Quantity) to compare value.",
                "Scale Drawings: Map Distance × Scale Factor = Real Distance (keep units consistent)."
            ],
            "calc_tip": "When checking ratio shares, add your individual answers back together — they MUST sum to the original total!"
        },
        "workout_blocks": [
            {
                "title": "Simplifying Ratios to Lowest Terms",
                "instruction": "Simplify each ratio into its simplest whole number form:",
                "items": [
                    ("a", "Simplify 6 : 9", "2 : 3"),
                    ("b", "Simplify 10 : 25", "2 : 5"),
                    ("c", "Simplify 12 : 18", "2 : 3"),
                    ("d", "Simplify 15 : 20", "3 : 4"),
                    ("e", "Simplify 24 : 36", "2 : 3"),
                    ("f", "Simplify 30 : 45", "2 : 3"),
                    ("g", "Simplify 14 : 21 : 28", "2 : 3 : 4"),
                    ("h", "Simplify 50p : £2.50", "1 : 5")
                ]
            },
            {
                "title": "Sharing Amounts in 2-Part Ratios",
                "instruction": "Share the given amounts into the specified ratios:",
                "items": [
                    ("a", "Share £60 in ratio 1 : 2", "£20 : £40"),
                    ("b", "Share £80 in ratio 1 : 3", "£20 : £60"),
                    ("c", "Share 100 kg in ratio 2 : 3", "40 kg : 60 kg"),
                    ("d", "Share £140 in ratio 3 : 4", "£60 : £80"),
                    ("e", "Share 90 litres in ratio 1 : 4", "18 L : 72 L"),
                    ("f", "Share £240 in ratio 5 : 3", "£150 : £90"),
                    ("g", "Share 180 metres in ratio 4 : 5", "80 m : 100 m"),
                    ("h", "Share £350 in ratio 2 : 5", "£100 : £250")
                ]
            },
            {
                "title": "Sharing Amounts in 3-Part Ratios",
                "instruction": "Add all three parts, find 1 part, then calculate each share:",
                "items": [
                    ("a", "Share £90 in ratio 1 : 2 : 3", "£15 : £30 : £45"),
                    ("b", "Share £120 in ratio 1 : 1 : 2", "£30 : £30 : £60"),
                    ("c", "Share 140 kg in ratio 2 : 2 : 3", "40 : 40 : 60 kg"),
                    ("d", "Share £200 in ratio 3 : 2 : 5", "£60 : £40 : £100"),
                    ("e", "Share 180 litres in ratio 1 : 3 : 5", "20 : 60 : 100 L"),
                    ("f", "Share £360 in ratio 4 : 3 : 2", "£160 : £120 : £80")
                ]
            },
            {
                "title": "Direct Proportion & Recipes (Scaling)",
                "instruction": "Find the unit amount, then scale up or down proportionally:",
                "items": [
                    ("a", "3 pens cost £2.40. Find cost of 5 pens.", "£4.00"),
                    ("b", "4 kg of apples cost £6.00. Cost of 6 kg?", "£9.00"),
                    ("c", "Recipe for 4 needs 300g flour. For 6 people?", "450g"),
                    ("d", "Recipe for 6 needs 180ml milk. For 10 people?", "300ml"),
                    ("e", "A machine makes 120 parts in 2 hours. In 5 hrs?", "300 parts"),
                    ("f", "8 workers build a fence in 6 hrs. How many hours for 4 workers?", "12 hours (Inverse)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Building & Mortar Mixing",
                "stem": "A bricklayer mixes sand and cement in the ratio <strong>4 : 1</strong> by weight. He needs to produce <strong>350 kg</strong> of mortar mix.<br>Work out the weight of sand and the weight of cement required.",
                "marks": 3,
                "unit": "kg",
                "steps": [
                    ("Total parts: 4 + 1 = 5 parts", "[M1]"),
                    ("Value of 1 part (cement): 350 ÷ 5 = 70 kg", "[M1]"),
                    ("Value of 4 parts (sand): 70 × 4 = 280 kg", "[A1]")
                ],
                "final_answer": "Sand: 280 kg, Cement: 70 kg",
                "reverse_check": "280 + 70 = 350 kg; 280 : 70 = 4 : 1.",
                "pitfall": "Multiplying 350 by 4 and 1 without dividing by the total parts first."
            },
            {
                "context_tag": "Workplace Business Profits",
                "stem": "Three partners, Alex, Brian and Clara, invest in a catering business in the ratio <strong>2 : 3 : 5</strong>. At the end of the year, the business generates a net profit of <strong>£48,000</strong>.<br>How much profit does Clara receive?",
                "marks": 3,
                "prefix": "£",
                "steps": [
                    ("Calculate total ratio parts: 2 + 3 + 5 = 10 parts", "[M1]"),
                    ("Find value of 1 part: £48,000 ÷ 10 = £4,800", "[M1]"),
                    ("Multiply by Clara's share (5 parts): £4,800 × 5 = £24,000", "[A1]")
                ],
                "final_answer": "£24,000.00",
                "reverse_check": "Alex = £9,600, Brian = £14,400, Clara = £24,000. Total = £48,000.",
                "pitfall": "Dividing profit equally by 3 rather than using ratio shares."
            },
            {
                "context_tag": "Care Home Staff Ratios",
                "stem": "A specialist residential care home operates with a required staffing ratio of <strong>1 healthcare assistant for every 5 residents</strong>.<br>On Thursday night, there are <strong>42 residents</strong> in the facility.<br>What is the minimum number of healthcare assistants that must be on duty?",
                "marks": 2,
                "unit": "assistants",
                "steps": [
                    ("Divide residents by ratio factor: 42 ÷ 5 = 8.4", "[M1]"),
                    ("Round UP to nearest whole person to maintain mandatory compliance: 9 assistants", "[A1]")
                ],
                "final_answer": "9 assistants",
                "reverse_check": "8 assistants × 5 = 40 (insufficient for 42). 9 assistants × 5 = 45 (compliant).",
                "pitfall": "Rounding down to 8 assistants (leaving 2 residents unattended)."
            },
            {
                "context_tag": "Chemical Cleaning Dilution",
                "stem": "An industrial disinfectant concentrate must be diluted with water in the ratio <strong>1 : 25</strong> (1 part concentrate to 25 parts water).<br>A cleaning supervisor needs to make <strong>13 litres</strong> of ready-to-use cleaning solution.<br>How many millilitres of concentrate does she need?",
                "marks": 3,
                "unit": "ml",
                "steps": [
                    ("Convert 13 litres to millilitres: 13 × 1,000 = 13,000 ml", "[M1]"),
                    ("Total ratio parts: 1 + 25 = 26 parts", "[M1]"),
                    ("Concentrate required (1 part): 13,000 ÷ 26 = 500 ml", "[A1]")
                ],
                "final_answer": "500 ml",
                "reverse_check": "500 ml concentrate + (25 × 500 = 12,500 ml water) = 13,000 ml = 13 litres.",
                "pitfall": "Dividing by 25 instead of total parts (26)."
            },
            {
                "context_tag": "Architectural Scale Plan",
                "stem": "A warehouse building plan is drawn to a scale of <strong>1 : 50</strong>.<br>On the plan, the width of the loading bay is <strong>16.4 cm</strong>.<br>Work out the actual real-life width of the loading bay in metres.",
                "marks": 3,
                "unit": "metres",
                "steps": [
                    ("Multiply plan length by scale factor: 16.4 cm × 50 = 820 cm", "[M1]"),
                    ("Convert centimetres to metres (divide by 100): 820 ÷ 100 = 8.2 m", "[M1]"),
                    ("State real-life width: 8.2 metres", "[A1]")
                ],
                "final_answer": "8.2 metres",
                "reverse_check": "8.2 m = 820 cm; 820 ÷ 50 = 16.4 cm.",
                "pitfall": "Dividing by 50 instead of multiplying, or forgetting to convert cm to m."
            },
            {
                "context_tag": "Vehicle Fleet Fuel Efficiency",
                "stem": "A courier van travels <strong>270 miles</strong> on <strong>36 litres</strong> of diesel fuel.<br>At this rate of fuel consumption, how many litres of diesel will the van need to complete a route of <strong>450 miles</strong>?",
                "marks": 3,
                "unit": "litres",
                "steps": [
                    ("Find miles per litre (unit rate): 270 ÷ 36 = 7.5 miles per litre", "[M1]"),
                    ("Calculate fuel needed for 450 miles: 450 ÷ 7.5 = 60 litres (or (36/270) × 450)", "[M1]"),
                    ("State total fuel required: 60 litres", "[A1]")
                ],
                "final_answer": "60 litres",
                "reverse_check": "60 litres × 7.5 mpg = 450 miles.",
                "pitfall": "Multiplying 450 by 7.5 instead of dividing."
            }
        ]
    }
}

print(f"Loaded {len(WORKOUT_CORE_MATHS)} core maths workout datasets in workout_maths_core_data.py")
