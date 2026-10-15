#!/usr/bin/env python3
"""Maths Domain 2: Financial Maths, Ratio & Proportion (7 Core Topics)"""

TOPICS_DOMAIN2 = [
    {
        'filename': 'functional-skills-ratio.html',
        'clean_topic': 'Ratio & Sharing into Parts',
        'intro_lead': 'Simplify ratios, write ratios in the unitary form 1 : n, and divide quantities into two or three-part ratios using the total parts method in healthcare and trade scenarios.',
        'next_file': 'functional-skills-proportion.html',
        'next_name': 'Direct & Inverse Proportion',
        'spec_points': [
            ('L1.11 / L2.11', 'Understand and calculate ratio, direct proportion, and scaling.'),
            ('L2.11', 'Divide an amount into a given ratio of two or three parts.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-arrows-split-up-and-left',
                'title': 'Golden Rule 1: The 3-Step Ratio Sharing Rule (Add, Divide, Multiply)',
                'desc': '1. <strong>Add</strong> the ratio numbers together to find the total number of parts.<br>2. <strong>Divide</strong> the total money or items by the total parts to find the value of 1 part.<br>3. <strong>Multiply</strong> the 1-part value by each ratio number.',
                'badge': '1. Add Parts → 2. Divide Total by Parts → 3. Multiply by Each Part'
            },
            {
                'icon': 'fa-flask',
                'title': 'Golden Rule 2: Dilutions and Ratios: Concentrate vs Water',
                'desc': 'In a 1 : 4 dilution ratio, there is 1 part concentrate and 4 parts water, giving 5 TOTAL parts (Concentrate is 1/5 of the total liquid, NOT 1/4).',
                'badge': 'Ratio 1 : 4 = 1 + 4 = 5 Total Parts'
            }
        ],
        'skills': [
            {
                'title': 'Skill 1: Simplifying Ratios & Converting to Unitary Form (1 : n)',
                'summary': 'Dividing by Highest Common Factors and expressing ratios with a leading 1.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Simplifying to Lowest Whole Terms:</strong> Divide both sides by their Highest Common Factor (HCF): <em>24 : 36 = 2 : 3 (dividing both by 12).</em></li>
                    <li><strong>Unitary Ratio (<code>1 : n</code>):</strong> Divide BOTH numbers by the first number: <em>4 : 18 = 1 : 4.5 (dividing both by 4).</em></li>
                    <li><strong>Match Units First:</strong> Never simplify mixed units! Convert to the smaller unit first: <em>50p : £2.50 &rarr; 50p : 250p = 1 : 5.</em></li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Skill 2: Sharing a Total into a Two-Part or Three-Part Ratio (ADM Method)',
                'summary': 'When you know the grand total and need to find each share.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">To share <strong>£720</strong> in the ratio <strong>2 : 3 : 4</strong>:</p>
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Add parts:</strong> <code>2 + 3 + 4 = 9 total parts</code>.</li>
                    <li><strong>Divide total by parts:</strong> <code>£720 ÷ 9 = £80 per part</code>.</li>
                    <li><strong>Multiply each part:</strong> <code>2 × £80 = £160</code> | <code>3 × £80 = £240</code> | <code>4 × £80 = £320</code>.</li>
                    <li><strong>Sanity Check:</strong> <code>£160 + £240 + £320 = £720</code>.</li>
                  </ol>
                </div>
                """
            },
            {
                'title': 'Skill 3: Scaling from One Known Part or the Difference Between Parts',
                'summary': 'When the question gives you ONE share or the difference, NOT the grand total.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:left;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Given Information</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">How to Find 1 Part</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Worked Example (Ratio 3 : 7)</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">Known Share (e.g. First share = £60)</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">Divide known value by its own parts (3)</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;"><code>1 part = £60 ÷ 3 = £20</code> &rarr; Second share = <code>7 × £20 = £140</code></td>
                      </tr>
                      <tr>
                        <td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">Known Difference (e.g. B gets £80 more than A)</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">Divide difference by difference in parts (7 - 3 = 4)</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;"><code>1 part = £80 ÷ 4 = £20</code> &rarr; Total = <code>10 × £20 = £200</code></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Model 1 (Level 1 Foundation): NHS Disinfectant Dilution & Ward Cleaning Allocation',
                'marks': '3 Marks (Pearson Edexcel Level 1/2)',
                'context': 'Clinical Decontamination Protocol',
                'question': 'An infection control housekeeper must prepare <strong>15 litres</strong> of sanitizing solution. The clinical guidelines require hospital disinfectant concentrate and water to be mixed in the ratio <strong>1 : 4</strong>.<br>(a) How many litres of disinfectant concentrate are needed?<br>(b) How many litres of water are needed?',
                'steps': [
                    ('Step 1', 'Add the ratio parts to find the total parts', '1 part concentrate + 4 parts water = 5 total parts.', 'M1: Total parts calculation'),
                    ('Step 2', 'Find the volume of 1 part', '15 litres ÷ 5 parts = 3 litres per part.', 'M1: Value of 1 part division'),
                    ('Step 3', 'Multiply by each ratio term', 'Concentrate = 1 × 3 L = 3 litres.<br>Water = 4 × 3 L = 12 litres.', 'A1: Accurate component volumes')
                ],
                'final_answer': 'Disinfectant Concentrate = 3 litres | Water = 12 litres',
                'tutor_tip': 'Quick check: 3 L + 12 L = 15 L total. 3 : 12 simplifies to 1 : 4. Both conditions verified.'
            },
            {
                'title': 'Model 2 (Level 2 Decision): Care Home Safe Staffing Ratio & Agency Cost Evaluation',
                'marks': '4 Marks (Pearson Edexcel Level 2 Problem Solving)',
                'context': 'Healthcare Workforce Compliance',
                'question': 'CQC inspection guidelines for an acute dementia unit require a minimum ratio of <strong>senior nurses to healthcare assistants (HCAs) of 2 : 5</strong>, and at least <strong>1 staff member for every 4 residents</strong>.<br>On Saturday, there are <strong>84 residents</strong> on the unit. The roster currently has <strong>6 senior nurses</strong> booked.<br>(a) Based on the 6 senior nurses and the 2 : 5 ratio, how many HCAs should be rostered?<br>(b) Will this combined team of senior nurses and HCAs meet the overall 1 : 4 staff-to-resident requirement?',
                'steps': [
                    ('Step 1', 'Use the 2 : 5 ratio to find the number of HCAs matching 6 senior nurses', '2 parts = 6 senior nurses → 1 part = 6 ÷ 2 = 3.<br>HCAs (5 parts) = 5 × 3 = 15 HCAs.', 'M1: Scaling from known part (6 ÷ 2 × 5 = 15)'),
                    ('Step 2', 'Calculate total staff on the unit', 'Total staff = 6 senior nurses + 15 HCAs = 21 staff members.', 'M1: Summing total rostered staff'),
                    ('Step 3', 'Calculate minimum staff required for 84 residents (1 : 4)', '84 residents ÷ 4 = 21 staff members required.', 'M1: Resident ratio division'),
                    ('Step 4', 'Compare and conclude', '21 rostered staff = 21 minimum required staff. Yes, 15 HCAs are needed and the combined team of 21 staff meets the 1 : 4 requirement.', 'A1: Accurate HCA count (15) and justified confirmation')
                ],
                'final_answer': '(a) 15 HCAs | (b) Yes, total staff is 6 + 15 = 21, which exactly meets the 84 ÷ 4 = 21 requirement.',
                'tutor_tip': 'Notice that in part (a), 6 is the number of senior nurses (2 parts), NOT the total staff!'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Dividing by One of the Ratio Terms Instead of the Total',
                'desc': 'When sharing a total of 15 L in the ratio 1 : 4, a common blunder is dividing 15 L by 4 (= 3.75 L). You must divide by the SUM of the parts (1 + 4 = 5).',
                'fix': "Always write: 'Total parts = [part 1] + [part 2]' before touching your calculator."
            }
        ],
        'practice_questions': [
            {
                'marks': '3 Marks',
                'question': 'A construction firm mixes concrete using cement, sand, and gravel in the ratio <strong>1 : 2 : 4</strong> by weight. The builder needs to prepare <strong>560 kg</strong> of concrete.<br>Calculate the weight of sand required.',
                'solution_steps': '1. Total parts = 1 + 2 + 4 = 7 parts.<br>2. 1 part = 560 ÷ 7 = 80 kg.<br>3. Sand has 2 parts: 2 × 80 kg = 160 kg.',
                'correct_answer': '160 kg of sand',
                'tutor_tip': 'Identify which term in the ratio corresponds to sand (the middle term, 2 parts).'
            },
            {
                'marks': '2 Marks',
                'question': 'A landscaping nursery mixes compost and topsoil in the ratio <strong>400 g : 1.8 kg</strong>. Write this ratio in its simplest whole-number form, and also in the unitary form <strong>1 : n</strong>.',
                'solution_steps': '1. Convert to common units (grams): 400 g : 1,800 g.<br>2. Divide both by 200 to simplify: 2 : 9.<br>3. Divide both by 2 for 1 : n form: 1 : 4.5.',
                'correct_answer': 'Simplest form = 2 : 9 | Unitary form = 1 : 4.5',
                'tutor_tip': 'Always convert 1.8 kg to 1,800 g before simplifying!'
            },
            {
                'marks': '3 Marks',
                'question': 'Two business partners, Maya and Liam, share annual profits in the ratio <strong>3 : 7</strong>. This year, Liam receives <strong>£14,000 more</strong> than Maya. Calculate the total profit made by the business.',
                'solution_steps': '1. Difference in ratio parts = 7 - 3 = 4 parts.<br>2. Value of 1 part = £14,000 ÷ 4 = £3,500.<br>3. Total parts = 3 + 7 = 10 parts &rarr; Total profit = 10 × £3,500 = £35,000.',
                'correct_answer': '£35,000',
                'tutor_tip': 'When given the difference ("£14,000 more"), divide by the difference in parts (7 - 3 = 4).'
            }
        ]
    },
    {
        'filename': 'functional-skills-proportion.html',
        'clean_topic': 'Direct & Inverse Proportion',
        'intro_lead': 'Solve recipe scaling, workforce scheduling, and machine output problems using unitary proportion and inverse proportion principles.',
        'next_file': 'functional-skills-formulas.html',
        'next_name': 'Algebra & Formulas',
        'spec_points': [
            ('L1.11 / L2.11', 'Calculate direct proportion and scaling in vocational situations.'),
            ('L2.11', 'Understand and solve problems involving inverse proportion (e.g. workers and time).')
        ],
        'golden_rules': [
            {
                'icon': 'fa-scale-balanced',
                'title': 'Golden Rule 1: The Unitary Method for Direct Proportion',
                'desc': 'Find the value of ONE unit first by dividing, then multiply by the required quantity. If 6 uniforms cost £150, 1 uniform costs £25; 10 uniforms cost £250.',
                'badge': 'Total ÷ Known Quantity = 1 Unit → 1 Unit × Desired Quantity'
            },
            {
                'icon': 'fa-person-digging',
                'title': 'Golden Rule 2: Inverse Proportion: More Workers = Less Time',
                'desc': "When workers increase, the time taken DECREASES proportionally. Multiply workers by hours to get total 'person-hours', then divide by the new workforce.",
                'badge': 'Total Person-Hours = Workers × Time → New Time = Total ÷ New Workers'
            }
        ],
        'skills': [
            {
                'title': 'Skill 1: Direct vs Inverse Proportion Comparison Matrix',
                'summary': 'Recognising whether values increase together or move in opposite directions.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Feature</th>
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
                        <td style="padding:10px; border:1px solid #cbd5e1;">Catering recipes, fuel consumption, currency exchange, hourly wages.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Staffing a ward clean, building a wall, pumps emptying a tank.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Core Formula</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><strong>Divide</strong> to find 1 unit, then <strong>Multiply</strong> up.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><strong>Multiply</strong> to find total work, then <strong>Divide</strong> by new team size.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                'title': 'Skill 2: Recipe & Ingredient Limiting-Factor Problems',
                'summary': 'Checking whether available store cupboard stock is enough for a scaled recipe.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">To find the maximum number of portions you can make from fixed stock (e.g. recipe for <strong>12 scones</strong> needs <strong>300 g flour</strong>; you have <strong>1,250 g flour</strong>):</p>
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li>Find flour per 1 scone: <code>300 g ÷ 12 = 25 g per scone</code>.</li>
                    <li>Divide available flour by 1-scone weight: <code>1,250 g ÷ 25 g = 50 scones maximum</code>.</li>
                  </ol>
                </div>
                """
            },
            {
                'title': 'Skill 3: Multi-Variable Workforce & Machine Rate Scaling',
                'summary': 'Calculating output when both machine count and operating hours change.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">If <strong>3 printers</strong> produce <strong>1,800 leaflets in 2 hours</strong>, how many leaflets will <strong>5 printers</strong> produce in <strong>4 hours</strong>?</p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>1 printer in 2 hours:</strong> <code>1,800 ÷ 3 = 600 leaflets</code>.</li>
                    <li><strong>1 printer in 1 hour:</strong> <code>600 ÷ 2 = 300 leaflets per printer-hour</code>.</li>
                    <li><strong>5 printers in 4 hours:</strong> <code>300 × 5 × 4 = 6,000 leaflets</code>.</li>
                  </ul>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Model 1 (Level 1 Foundation): Hospital Kitchen Recipe Scaling',
                'marks': '3 Marks (Pearson Edexcel Level 1)',
                'context': 'Healthcare Catering Production',
                'question': 'A hospital canteen recipe for <strong>15 portions</strong> of vegetable soup requires <strong>450 grams</strong> of carrots and <strong>1.2 litres</strong> of stock.<br>Calculate the weight of carrots (in grams) and volume of stock (in litres) needed to make <strong>40 portions</strong>.',
                'steps': [
                    ('Step 1', 'Find the multiplier or unitary amount for 1 portion', 'Carrots for 1 portion = 450 g ÷ 15 = 30 g.<br>Stock for 1 portion = 1.2 L ÷ 15 = 0.08 L.', 'M1: Unitary division by 15'),
                    ('Step 2', 'Multiply carrots by 40 portions', '30 g × 40 = 1,200 grams of carrots.', 'A1: Accurate carrot mass (1,200 g)'),
                    ('Step 3', 'Multiply stock by 40 portions', '0.08 L × 40 = 3.2 litres of stock.', 'A1: Accurate stock volume (3.2 L)')
                ],
                'final_answer': 'Carrots = 1,200 g | Stock = 3.2 litres',
                'tutor_tip': 'Always find 1 portion first (450 ÷ 15 = 30 g) so you avoid awkward fractions.'
            },
            {
                'title': 'Model 2 (Level 2 Decision): Depot Parcel Sorting Shift Workforce Allocation',
                'marks': '4 Marks (Pearson Edexcel Level 2 Problem Solving)',
                'context': 'Logistics Hub Operations',
                'question': 'It takes <strong>6 warehouse operatives</strong> working at the same pace <strong>3 hours and 20 minutes</strong> to unload and scan a freight container.<br>On Friday, the container arrives at <strong>13:30</strong> and must be completely unloaded by <strong>16:00</strong>.<br>What is the minimum number of warehouse operatives needed to finish on time?',
                'steps': [
                    ('Step 1', 'Convert original duration to minutes and find total person-minutes', '3 hours 20 mins = (3 × 60) + 20 = 200 minutes.<br>Total workload = 6 operatives × 200 mins = 1,200 person-minutes.', 'M1: Inverse proportion total effort in person-minutes'),
                    ('Step 2', 'Calculate available time window on Friday', 'From 13:30 to 16:00 = 2 hours 30 minutes = 150 minutes.', 'M1: Available time calculation'),
                    ('Step 3', 'Divide total person-minutes by available minutes', '1,200 person-minutes ÷ 150 minutes = 8 operatives.', 'M1: Inverse proportion division'),
                    ('Step 4', 'State final staffing conclusion', '8 warehouse operatives are required (2 additional operatives above the standard team of 6).', 'A1: Accurate workforce requirement (8 operatives)')
                ],
                'final_answer': '8 warehouse operatives required (total workload is 1,200 person-minutes ÷ 150 available minutes).',
                'tutor_tip': 'Converting hours and minutes into total minutes (200 mins and 150 mins) avoids recurring decimals like 3.333 hours!'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Applying Direct Proportion to Staffing Problems',
                'desc': 'Calculating 6 ÷ 4 × 6 = 9 hours when increasing from 4 to 6 workers is a catastrophic error because adding workers should speed up the work, not make it take longer!',
                'fix': "Always ask: 'Should more workers take more time or less time?'"
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'A hospital kitchen recipe for <strong>8 resident portions</strong> requires <strong>600 grams</strong> of minced beef. How many grams of beef are required to prepare <strong>20 resident portions</strong>?',
                'solution_steps': '1. 1 portion = 600 ÷ 8 = 75 grams.<br>2. 20 portions = 75 × 20 = 1,500 grams (or 1.5 kg).',
                'correct_answer': '1,500 g (or 1.5 kg)',
                'tutor_tip': 'Find the amount for 1 portion first using the unitary method.'
            },
            {
                'marks': '2 Marks',
                'question': 'It takes <strong>5 industrial pumps 12 hours</strong> to drain a flooded basement. How long would it take <strong>8 identical pumps</strong> to drain the same basement? Give your answer in hours and minutes.',
                'solution_steps': '1. Total pump-hours = 5 × 12 = 60 pump-hours.<br>2. Time for 8 pumps = 60 ÷ 8 = 7.5 hours.<br>3. 0.5 hours = 30 minutes &rarr; 7 hours 30 minutes.',
                'correct_answer': '7 hours 30 minutes (7.5 hours)',
                'tutor_tip': 'Remember that 0.5 hours is 30 minutes, NOT 50 minutes.'
            },
            {
                'marks': '3 Marks',
                'question': 'A delivery van travels <strong>210 miles</strong> on <strong>17.5 litres</strong> of diesel. How many litres of diesel will the van need for a journey of <strong>336 miles</strong> at the same consumption rate?',
                'solution_steps': '1. Miles per litre = 210 ÷ 17.5 = 12 miles per litre.<br>2. Litres needed for 336 miles = 336 ÷ 12 = 28 litres.',
                'correct_answer': '28 litres',
                'tutor_tip': 'Dividing miles by litres (210 ÷ 17.5 = 12 miles/L) gives a clean whole number!'
            }
        ]
    },
    {
        'filename': 'functional-skills-formulas.html',
        'clean_topic': 'Algebra, Formulas & Substitution',
        'intro_lead': 'Substitute numerical values into word and algebraic formulas, rearrange simple formulas, and solve vocational trade and NHS dosage equations.',
        'next_file': 'functional-skills-money.html',
        'next_name': 'Money & Finance',
        'spec_points': [
            ('L1.13 / L2.13', 'Substitute values into given words and symbols formulas in familiar and unfamiliar contexts.'),
            ('L2.14', 'Rearrange simple linear equations to change the subject of a formula.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-square-root-variable',
                'title': 'Golden Rule 1: Letters Next to Letters Mean Multiplication',
                'desc': 'In algebra, 4h means 4 × h; 2lw means 2 × l × w. Always write in the invisible multiplication signs before substituting values.',
                'badge': 'C = 50 + 25h → C = 50 + (25 × h)'
            },
            {
                'icon': 'fa-bracket-round',
                'title': 'Golden Rule 2: Wrap Negative Substitutions in Brackets',
                'desc': 'When substituting a negative number into a squared variable, (-3)² = +9, NOT -9. Always enclose negative values in brackets.',
                'badge': '(-4)² = (-4) × (-4) = +16'
            }
        ],
        'skills': [
            {
                'title': 'Skill 1: Step-by-Step Substitution Method',
                'summary': 'Converting algebraic and word formulas into solvable numerical equations.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Write out the formula with multiplication signs visible:</strong> e.g. <code>P = 2L + 2W</code> &rarr; <code>P = (2 × L) + (2 × W)</code>.</li>
                    <li><strong>Replace each letter with its given number in brackets:</strong> Make sure units match the formula specification (e.g. convert minutes to hours if the formula requires hours).</li>
                    <li><strong>Apply BIDMAS strictly:</strong> Resolve brackets and powers first, then multiplications/divisions, then additions/subtractions.</li>
                  </ol>
                </div>
                """
            },
            {
                'title': 'Skill 2: Formula Triangles: Speed (SDT) & Density (MDV)',
                'summary': 'Two essential formula triangles frequently assessed in Level 1 & Level 2 Functional Skills.',
                'content_html': """
    <div class="big-formula-diagram-container" style="background:#ffffff; border:2px solid #cbd5e1; border-radius:14px; padding:24px 20px; margin:20px 0; box-shadow:0 6px 18px rgba(15, 23, 42, 0.08);">
      <div style="text-align:center; margin-bottom:16px;">
        <span style="display:inline-block; background:#eff6ff; color:#1e40af; border:1px solid #bfdbfe; font-size:0.82rem; font-weight:800; padding:5px 16px; border-radius:999px; text-transform:uppercase; letter-spacing:0.05em;">
          <i class="fa-solid fa-gauge" style="margin-right:6px; color:#2563eb;"></i> Master Formula Triangle
        </span>
        <h3 style="margin:10px 0 6px 0; color:#0f172a; font-size:1.45rem; font-weight:900;">The Speed, Distance &amp; Time (S-D-T) Triangle</h3>
        <p style="margin:0; color:#64748b; font-size:0.98rem; max-width:620px; margin:0 auto; line-height:1.5;">
          Place your finger or thumb over the letter you want to find. The remaining letters give you the exact calculation formula.
        </p>
      </div>

      <div style="display:flex; justify-content:center; width:100%;">
        <svg viewBox="0 0 700 350" width="100%" style="max-width:720px; height:auto; display:block; font-family:system-ui, -apple-system, sans-serif;" xmlns="http://www.w3.org/2000/svg">
          <!-- Background glow for triangle -->
          <polygon points="160,18 15,295 305,295" fill="#f8fafc" stroke="#0f172a" stroke-width="4.5" stroke-linejoin="round"/>
          
          <!-- Dividing Horizontal Bar -->
          <line x1="68" y1="175" x2="252" y2="175" stroke="#0f172a" stroke-width="4.5"/>
          <!-- Division indicators -->
          <circle cx="48" cy="175" r="14" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
          <text x="48" y="181" font-size="16" font-weight="900" fill="#1d4ed8" text-anchor="middle">÷</text>
          <circle cx="272" cy="175" r="14" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
          <text x="272" y="181" font-size="16" font-weight="900" fill="#1d4ed8" text-anchor="middle">÷</text>

          <!-- Vertical Dividing Line between S and T -->
          <line x1="160" y1="175" x2="160" y2="295" stroke="#0f172a" stroke-width="4.5"/>
          <!-- Multiplication indicator -->
          <circle cx="160" cy="245" r="15" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
          <text x="160" y="251" font-size="16" font-weight="900" fill="#b45309" text-anchor="middle">×</text>

          <!-- Top Chamber: Distance (D) -->
          <circle cx="160" cy="98" r="44" fill="#dbeafe" stroke="#2563eb" stroke-width="3.5"/>
          <text x="160" y="108" font-size="38" font-weight="900" fill="#1e40af" text-anchor="middle">D</text>
          <text x="160" y="128" font-size="11" font-weight="900" fill="#1d4ed8" text-anchor="middle">DISTANCE</text>
          <text x="160" y="141" font-size="9" font-weight="700" fill="#3b82f6" text-anchor="middle">(miles, km, m)</text>

          <!-- Bottom Left Chamber: Speed (S) -->
          <circle cx="95" cy="235" r="40" fill="#fef3c7" stroke="#d97706" stroke-width="3.5"/>
          <text x="95" y="246" font-size="34" font-weight="900" fill="#b45309" text-anchor="middle">S</text>
          <text x="95" y="264" font-size="11" font-weight="900" fill="#92400e" text-anchor="middle">SPEED</text>
          <text x="95" y="277" font-size="8.5" font-weight="700" fill="#b45309" text-anchor="middle">(mph, km/h)</text>

          <!-- Bottom Right Chamber: Time (T) -->
          <circle cx="225" cy="235" r="40" fill="#dcfce7" stroke="#16a34a" stroke-width="3.5"/>
          <text x="225" y="246" font-size="34" font-weight="900" fill="#15803d" text-anchor="middle">T</text>
          <text x="225" y="264" font-size="11" font-weight="900" fill="#166534" text-anchor="middle">TIME</text>
          <text x="225" y="277" font-size="8.5" font-weight="700" fill="#15803d" text-anchor="middle">(hours, mins)</text>

          <!-- Right: Clear Operational Explanations Panel -->
          <g transform="translate(330, 18)">
            <rect x="0" y="0" width="355" height="295" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="177" y="26" font-size="12.5" font-weight="900" fill="#0f172a" text-anchor="middle" letter-spacing="0.05em">HOW TO READ THE TRIANGLE</text>
            
            <!-- Box 1: Distance -->
            <rect x="14" y="38" width="327" height="56" rx="8" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1.5"/>
            <text x="26" y="60" font-size="11" font-weight="900" fill="#1d4ed8">1. COVER DISTANCE (D)</text>
            <text x="26" y="80" font-size="13.5" font-weight="900" fill="#0f172a">Distance = Speed × Time</text>
            <rect x="238" y="50" width="92" height="30" rx="6" fill="#2563eb"/>
            <text x="284" y="70" font-size="12" font-weight="900" fill="#ffffff" text-anchor="middle">D = S × T</text>

            <!-- Box 2: Speed -->
            <rect x="14" y="102" width="327" height="56" rx="8" fill="#fffbeb" stroke="#fde68a" stroke-width="1.5"/>
            <text x="26" y="124" font-size="11" font-weight="900" fill="#b45309">2. COVER SPEED (S)</text>
            <text x="26" y="144" font-size="13.5" font-weight="900" fill="#0f172a">Speed = Distance ÷ Time</text>
            <rect x="238" y="114" width="92" height="30" rx="6" fill="#d97706"/>
            <text x="284" y="134" font-size="12" font-weight="900" fill="#ffffff" text-anchor="middle">S = D ÷ T</text>

            <!-- Box 3: Time -->
            <rect x="14" y="166" width="327" height="56" rx="8" fill="#f0fdf4" stroke="#bbf7d0" stroke-width="1.5"/>
            <text x="26" y="188" font-size="11" font-weight="900" fill="#15803d">3. COVER TIME (T)</text>
            <text x="26" y="208" font-size="13.5" font-weight="900" fill="#0f172a">Time = Distance ÷ Speed</text>
            <rect x="238" y="178" width="92" height="30" rx="6" fill="#16a34a"/>
            <text x="284" y="198" font-size="12" font-weight="900" fill="#ffffff" text-anchor="middle">T = D ÷ S</text>

            <!-- Decimal Time Banner -->
            <rect x="14" y="230" width="327" height="52" rx="8" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.2"/>
            <text x="177" y="249" font-size="11" font-weight="900" fill="#991b1b" text-anchor="middle">⏱️ DECIMAL TIME RULE (DIVIDE MINS BY 60):</text>
            <text x="177" y="268" font-size="11" font-weight="800" fill="#b91c1c" text-anchor="middle">15m = 0.25h &bull; 30m = 0.5h &bull; 45m = 0.75h (NEVER 0.45!)</text>
          </g>
        </svg>
      </div>
    </div>
    <div style='height:20px;'></div>
    <div class="big-formula-diagram-container" style="background:#ffffff; border:2px solid #cbd5e1; border-radius:14px; padding:24px 20px; margin:20px 0; box-shadow:0 6px 18px rgba(15, 23, 42, 0.08);">
      <div style="text-align:center; margin-bottom:16px;">
        <span style="display:inline-block; background:#f5f3ff; color:#5b21b6; border:1px solid #ddd6fe; font-size:0.82rem; font-weight:800; padding:5px 16px; border-radius:999px; text-transform:uppercase; letter-spacing:0.05em;">
          <i class="fa-solid fa-cube" style="margin-right:6px; color:#7c3aed;"></i> Master Formula Triangle
        </span>
        <h3 style="margin:10px 0 6px 0; color:#0f172a; font-size:1.45rem; font-weight:900;">The Mass, Density &amp; Volume (M-D-V) Triangle</h3>
        <p style="margin:0; color:#64748b; font-size:0.98rem; max-width:620px; margin:0 auto; line-height:1.5;">
          Remember: <strong>Mass is always on top (M)</strong>. Cover the quantity you need to find with your finger.
        </p>
      </div>

      <div style="display:flex; justify-content:center; width:100%;">
        <svg viewBox="0 0 700 350" width="100%" style="max-width:720px; height:auto; display:block; font-family:system-ui, -apple-system, sans-serif;" xmlns="http://www.w3.org/2000/svg">
          <!-- Background glow for triangle -->
          <polygon points="160,18 15,295 305,295" fill="#f8fafc" stroke="#0f172a" stroke-width="4.5" stroke-linejoin="round"/>
          
          <!-- Dividing Horizontal Bar -->
          <line x1="68" y1="175" x2="252" y2="175" stroke="#0f172a" stroke-width="4.5"/>
          <!-- Division indicators -->
          <circle cx="48" cy="175" r="14" fill="#f5f3ff" stroke="#8b5cf6" stroke-width="1.5"/>
          <text x="48" y="181" font-size="16" font-weight="900" fill="#6d28d9" text-anchor="middle">÷</text>
          <circle cx="272" cy="175" r="14" fill="#f5f3ff" stroke="#8b5cf6" stroke-width="1.5"/>
          <text x="272" y="181" font-size="16" font-weight="900" fill="#6d28d9" text-anchor="middle">÷</text>

          <!-- Vertical Dividing Line between D and V -->
          <line x1="160" y1="175" x2="160" y2="295" stroke="#0f172a" stroke-width="4.5"/>
          <!-- Multiplication indicator -->
          <circle cx="160" cy="245" r="15" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5"/>
          <text x="160" y="251" font-size="16" font-weight="900" fill="#0369a1" text-anchor="middle">×</text>

          <!-- Top Chamber: Mass (M) -->
          <circle cx="160" cy="98" r="44" fill="#ede9fe" stroke="#7c3aed" stroke-width="3.5"/>
          <text x="160" y="108" font-size="38" font-weight="900" fill="#5b21b6" text-anchor="middle">M</text>
          <text x="160" y="128" font-size="11" font-weight="900" fill="#4c1d95" text-anchor="middle">MASS</text>
          <text x="160" y="141" font-size="9" font-weight="700" fill="#7c3aed" text-anchor="middle">(grams, kg, tonnes)</text>

          <!-- Bottom Left Chamber: Density (D) -->
          <circle cx="95" cy="235" r="40" fill="#e0f2fe" stroke="#0284c7" stroke-width="3.5"/>
          <text x="95" y="246" font-size="34" font-weight="900" fill="#0369a1" text-anchor="middle">D</text>
          <text x="95" y="264" font-size="11" font-weight="900" fill="#075985" text-anchor="middle">DENSITY</text>
          <text x="95" y="277" font-size="8.5" font-weight="700" fill="#0284c7" text-anchor="middle">(g/cm³, kg/m³)</text>

          <!-- Bottom Right Chamber: Volume (V) -->
          <circle cx="225" cy="235" r="40" fill="#dcfce7" stroke="#16a34a" stroke-width="3.5"/>
          <text x="225" y="246" font-size="34" font-weight="900" fill="#15803d" text-anchor="middle">V</text>
          <text x="225" y="264" font-size="11" font-weight="900" fill="#166534" text-anchor="middle">VOLUME</text>
          <text x="225" y="277" font-size="8.5" font-weight="700" fill="#15803d" text-anchor="middle">(cm³, m³, litres)</text>

          <!-- Right: Clear Operational Explanations Panel -->
          <g transform="translate(330, 18)">
            <rect x="0" y="0" width="355" height="295" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="177" y="26" font-size="12.5" font-weight="900" fill="#0f172a" text-anchor="middle" letter-spacing="0.05em">HOW TO READ THE TRIANGLE</text>
            
            <!-- Box 1: Mass -->
            <rect x="14" y="38" width="327" height="56" rx="8" fill="#f5f3ff" stroke="#ddd6fe" stroke-width="1.5"/>
            <text x="26" y="60" font-size="11" font-weight="900" fill="#5b21b6">1. COVER MASS (M)</text>
            <text x="26" y="80" font-size="13.5" font-weight="900" fill="#0f172a">Mass = Density × Volume</text>
            <rect x="238" y="50" width="92" height="30" rx="6" fill="#7c3aed"/>
            <text x="284" y="70" font-size="12" font-weight="900" fill="#ffffff" text-anchor="middle">M = D × V</text>

            <!-- Box 2: Density -->
            <rect x="14" y="102" width="327" height="56" rx="8" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1.5"/>
            <text x="26" y="124" font-size="11" font-weight="900" fill="#0369a1">2. COVER DENSITY (D)</text>
            <text x="26" y="144" font-size="13.5" font-weight="900" fill="#0f172a">Density = Mass ÷ Volume</text>
            <rect x="238" y="114" width="92" height="30" rx="6" fill="#0284c7"/>
            <text x="284" y="134" font-size="12" font-weight="900" fill="#ffffff" text-anchor="middle">D = M ÷ V</text>

            <!-- Box 3: Volume -->
            <rect x="14" y="166" width="327" height="56" rx="8" fill="#f0fdf4" stroke="#bbf7d0" stroke-width="1.5"/>
            <text x="26" y="188" font-size="11" font-weight="900" fill="#15803d">3. COVER VOLUME (V)</text>
            <text x="26" y="208" font-size="13.5" font-weight="900" fill="#0f172a">Volume = Mass ÷ Density</text>
            <rect x="238" y="178" width="92" height="30" rx="6" fill="#16a34a"/>
            <text x="284" y="198" font-size="12" font-weight="900" fill="#ffffff" text-anchor="middle">V = M ÷ D</text>

            <!-- Units Matching Banner -->
            <rect x="14" y="230" width="327" height="52" rx="8" fill="#f0fdf4" stroke="#86efac" stroke-width="1.2"/>
            <text x="177" y="249" font-size="11" font-weight="900" fill="#166534" text-anchor="middle">⚖️ CHECK MATCHING UNITS BEFORE CALCULATING:</text>
            <text x="177" y="268" font-size="10.5" font-weight="800" fill="#15803d" text-anchor="middle">g with cm³ &rarr; g/cm³  |  kg with m³ &rarr; kg/m³ (1 L water = 1 kg)</text>
          </g>
        </svg>
      </div>
    </div>
    """
            },
            {
                'title': 'Skill 3: Rearranging Two-Step Formulas (Working Backwards)',
                'summary': 'Finding an unknown input when you are given the final output.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">Suppose a hire formula is <strong><code>Cost = 40 + 25h</code></strong> and a customer is billed <strong>£190</strong>. To find the hours (<code>h</code>):</p>
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Undo the addition first (subtract fixed callout fee):</strong> <code>£190 - £40 = £150</code>.</li>
                    <li><strong>Undo the multiplication second (divide by hourly rate):</strong> <code>£150 ÷ £25 = 6 hours</code>.</li>
                  </ol>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Model 1 (Level 1 Foundation): Clinical Paediatric Dosage Formulation',
                'marks': '3 Marks (Pearson Edexcel Level 1/2)',
                'context': 'Healthcare Clinical Calculations',
                'question': "The formula for a child's drug dose in milligrams is:<br><strong>Dose = (Age in years ÷ [Age in years + 12]) × Adult Dose</strong><br>A 6-year-old child requires medicine where the adult dose is <strong>240 mg</strong>. Calculate the child's dose.",
                'steps': [
                    ('Step 1', 'Substitute Age = 6 and Adult Dose = 240 into formula', 'Dose = (6 ÷ [6 + 12]) × 240', 'M1: Correct numerical substitution'),
                    ('Step 2', 'Resolve the bracketed denominator: 6 + 12 = 18', 'Dose = (6 ÷ 18) × 240', 'M1: Order of operations'),
                    ('Step 3', 'Simplify fraction and calculate final dose', '6/18 = 1/3.<br>Dose = 1/3 × 240 = 240 ÷ 3 = 80 mg.', 'A1: Accurate medication dosage')
                ],
                'final_answer': 'Child Dose = 80 mg',
                'tutor_tip': 'Notice how 6/18 simplifies to 1/3, making 240 ÷ 3 = 80 straightforward without a calculator.'
            },
            {
                'title': 'Model 2 (Level 2 Decision): Cardiology BMI & BSA Clinical Eligibility Check',
                'marks': '4 Marks (Pearson Edexcel Level 2 Problem Solving)',
                'context': 'Clinical Assessment Protocol',
                'question': 'A clinical trial uses the Body Mass Index formula: <strong>BMI = m ÷ h²</strong>, where <strong>m</strong> is mass in kilograms and <strong>h</strong> is height in metres.<br>Patients are eligible for the trial only if their BMI is between <strong>25.0 and 29.9</strong>.<br>A patient has a mass of <strong>91.8 kg</strong> and a height of <strong>180 cm</strong>. Is this patient eligible for the trial?',
                'steps': [
                    ('Step 1', 'Convert height from centimetres to metres', '180 cm ÷ 100 = 1.8 m.', 'M1: Metric unit conversion to match formula'),
                    ('Step 2', 'Square the height (h²)', '1.8² = 1.8 × 1.8 = 3.24 m².', 'M1: Squaring height'),
                    ('Step 3', 'Divide mass by squared height', 'BMI = 91.8 ÷ 3.24 = 28.33 (to 2 d.p.).', 'M1: Accurate division for BMI'),
                    ('Step 4', 'Compare against eligibility range (25.0 to 29.9)', '28.33 lies between 25.0 and 29.9. Yes, the patient is eligible for the clinical trial.', 'A1: Correct BMI (28.33) and clear conclusion')
                ],
                'final_answer': 'Yes, eligible (BMI = 28.33, which is within the 25.0 to 29.9 range).',
                'tutor_tip': 'Always check units in formula questions! The formula requires height in metres (1.8 m), whereas the patient was measured in centimetres (180 cm).'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Adding Before Multiplying in Pricing Formulas',
                'desc': 'In Cost = 40 + 20h with h = 3, adding 40 + 20 = 60 then 60 × 3 = 180 is wrong. The multiplication must be done first: 20 × 3 = 60, then 40 + 60 = 100.',
                'fix': 'Always underline the multiplication term first: Cost = 40 + [20 × h].'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'A plumber uses the formula: <strong>Total Charge = 45 + 32h</strong>, where <strong>h</strong> is the number of hours worked. Calculate the total charge for a job lasting <strong>4.5 hours</strong>.',
                'solution_steps': '1. Substitute h = 4.5: Total = 45 + (32 × 4.5).<br>2. 32 × 4.5 = 144.<br>3. Total = 45 + 144 = £189.00.',
                'correct_answer': '£189.00',
                'tutor_tip': 'Remember to write the answer as currency with a pound sign (£189.00).'
            },
            {
                'marks': '2 Marks',
                'question': 'The formula to convert Celsius (C) to Fahrenheit (F) is <strong>F = 1.8C + 32</strong>. Calculate the temperature in Fahrenheit when a clinical incubator is set to <strong>35°C</strong>.',
                'solution_steps': '1. Substitute C = 35: F = (1.8 × 35) + 32.<br>2. 1.8 × 35 = 63.<br>3. F = 63 + 32 = 95°F.',
                'correct_answer': '95°F',
                'tutor_tip': 'Multiply 1.8 by 35 first (63), then add 32.'
            },
            {
                'marks': '3 Marks',
                'question': 'An equipment hire company charges using the formula <strong>C = 65 + 18d</strong>, where <strong>C</strong> is the total cost in pounds and <strong>d</strong> is the number of days hired. A building contractor receives an invoice for <strong>£299</strong>. For how many days did the contractor hire the equipment?',
                'solution_steps': '1. Substitute C = 299: 299 = 65 + 18d.<br>2. Subtract fixed fee: 299 - 65 = 234.<br>3. Divide by daily rate: d = 234 ÷ 18 = 13 days.',
                'correct_answer': '13 days',
                'tutor_tip': 'Work backwards using inverse operations: subtract 65 first, then divide by 18.'
            }
        ]
    },
    {
        'filename': 'functional-skills-money.html',
        'clean_topic': 'Money, Invoicing & Payroll Calculations',
        'intro_lead': 'Calculate gross pay, net pay, wage slip deductions (PAYE tax, National Insurance, pension), balance workplace budgets, and compute customer invoices with VAT.',
        'next_file': 'functional-skills-best-buys.html',
        'next_name': 'Best Buys & Unit Pricing',
        'spec_points': [
            ('L1.14 / L2.15', 'Calculate with money and solve problems involving wage slips, invoices, and household/workplace budgets.'),
            ('L2.16', 'Calculate percentage discounts, VAT, and National Insurance deductions.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-receipt',
                'title': 'Golden Rule 1: Net Pay = Gross Pay - Total Deductions',
                'desc': "Gross pay is your earnings before anything is taken off. Deductions (Income Tax, NI, Pension) are subtracted from Gross to leave Net Pay ('take-home pay').",
                'badge': 'Net Pay = Gross Pay - (Tax + NI + Pension)'
            },
            {
                'icon': 'fa-percent',
                'title': 'Golden Rule 2: Adding 20% Standard UK VAT',
                'desc': 'To add 20% VAT to a net amount, multiply by 1.20 (or find 10%, double it to get 20%, and add).',
                'badge': 'Gross Price with VAT = Net Price × 1.20'
            }
        ],
        'skills': [
            {
                'title': 'Skill 1: Understanding the Standard Workplace Payslip',
                'summary': 'Key lines and calculations on an employee payslip.',
                'content_html': """
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
            },
            {
                'title': 'Skill 2: Calculating Overtime Rates (Time-and-a-Half & Double Time)',
                'summary': 'How to compute enhanced hourly rates for weekend and night shifts.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Time-and-a-half (<code>1.5×</code>):</strong> Multiply basic hourly rate by <code>1.5</code> (or add half the rate onto the basic rate). If basic rate is <code>£14.00/hr</code>, overtime rate = <code>£14 + £7 = £21.00/hr</code>.</li>
                    <li><strong>Time-and-a-quarter (<code>1.25×</code>):</strong> Multiply basic rate by <code>1.25</code> (e.g. <code>£12.00 × 1.25 = £15.00/hr</code>).</li>
                    <li><strong>Double time (<code>2×</code>):</strong> Multiply basic rate by <code>2</code> (e.g. <code>£14.00 × 2 = £28.00/hr</code>).</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Skill 3: Commercial Invoices, Trade Discounts & VAT Order',
                'summary': 'Always deduct trade discounts BEFORE calculating VAT on the discounted net subtotal.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Goods &amp; Labour Subtotal:</strong> Sum all line items (quantity × unit price).</li>
                    <li><strong>Subtract Trade Discount:</strong> Deduct any promotional percentage to get the <strong>Net Subtotal</strong>.</li>
                    <li><strong>Add 20% VAT:</strong> Calculate 20% of the Net Subtotal and add it to obtain the <strong>Total Payable</strong>.</li>
                  </ol>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Model 1 (Level 1 Foundation): Hospital Facility Maintenance Contractor Invoice',
                'marks': '3 Marks (Pearson Edexcel Level 1/2)',
                'context': 'Healthcare Facility Contract Billing',
                'question': 'A facilities contractor completes electrical safety testing across Ward 2. The invoice details are:<br>• Labour: <strong>14 hours at £32.50 per hour</strong><br>• Replacement parts: <strong>£145.00</strong><br>• VAT: <strong>20% on the subtotal</strong><br>Calculate the total amount payable on the invoice.',
                'steps': [
                    ('Step 1', 'Calculate total labour cost', '14 hours × £32.50 = £455.00', 'M1: Labour multiplication'),
                    ('Step 2', 'Calculate subtotal before VAT', '£455.00 + £145.00 = £600.00', 'M1: Subtotal addition'),
                    ('Step 3', 'Calculate 20% VAT and total invoice amount', '20% of £600 = 0.20 × 600 = £120.00.<br>Total payable = £600.00 + £120.00 = £720.00.', 'A1: Accurate final total with VAT')
                ],
                'final_answer': 'Total Amount Payable = £720.00',
                'tutor_tip': 'You can also calculate the total in a single step: £600.00 × 1.20 = £720.00.'
            },
            {
                'title': 'Model 2 (Level 2 Decision): Paramedic Monthly Net Pay & Mortgage Affordability Check',
                'marks': '4 Marks (Pearson Edexcel Level 2 Problem Solving)',
                'context': 'Personal Finance & Payroll',
                'question': 'A paramedic works <strong>150 basic hours</strong> this month at <strong>£16.00 per hour</strong>, plus <strong>12 overtime hours</strong> paid at <strong>time-and-a-half (1.5×)</strong>.<br>From her total gross pay, she has the following deductions:<br>• Income Tax: <strong>15% of total gross pay</strong><br>• National Insurance: <strong>£184.00</strong><br>• NHS Pension: <strong>8% of total gross pay</strong><br><br>Her mortgage lender requires her monthly net take-home pay to be at least <strong>£1,900</strong>. Does she meet the lender\'s requirement?',
                'steps': [
                    ('Step 1', 'Calculate basic pay, overtime pay, and total gross pay', 'Basic = 150 × £16 = £2,400.<br>Overtime rate = £16 × 1.5 = £24/hr → Overtime pay = 12 × £24 = £288.<br>Total Gross Pay = £2,400 + £288 = £2,688.00.', 'M1: Accurate gross pay calculation'),
                    ('Step 2', 'Calculate Income Tax (15%) and Pension (8%) deductions', 'Tax = 0.15 × £2,688 = £403.20.<br>Pension = 0.08 × £2,688 = £215.04.', 'M1: Percentage deductions on gross pay'),
                    ('Step 3', 'Sum all deductions and subtract from gross pay', 'Total deductions = £403.20 + £184.00 + £215.04 = £802.24.<br>Net Pay = £2,688.00 - £802.24 = £1,885.76.', 'M1: Net pay subtraction'),
                    ('Step 4', 'Compare against £1,900 requirement', '£1,885.76 < £1,900 (short by £14.24). No, she does not meet the lender\'s £1,900 net pay requirement.', 'A1: Accurate net pay (£1,885.76) and clear conclusion')
                ],
                'final_answer': 'No (Net take-home pay is £1,885.76, which is £14.24 below the £1,900 requirement).',
                'tutor_tip': 'Since both Tax (15%) and Pension (8%) apply to total gross pay, you can add their percentages together (23% of £2,688 = £618.24) plus £184 NI = £802.24!'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Applying VAT Only to Materials and Forgetting Labour',
                'desc': 'Unless explicitly stated otherwise, VAT applies to the TOTAL subtotal of labour PLUS parts.',
                'fix': 'Always sum all line items first before applying the VAT percentage.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'An employee has a gross monthly salary of <strong>£2,400</strong>. Deductions are: Income Tax <strong>£285.40</strong>, National Insurance <strong>£168.20</strong>, and Pension <strong>£120.00</strong>. Calculate their net take-home pay.',
                'solution_steps': '1. Total deductions = 285.40 + 168.20 + 120.00 = £573.60.<br>2. Net pay = 2,400.00 - 573.60 = £1,826.40.',
                'correct_answer': '£1,826.40',
                'tutor_tip': 'Double check your subtraction: 2,400.00 - 573.60 = £1,826.40.'
            },
            {
                'marks': '2 Marks',
                'question': 'A care worker earns <strong>£12.80 per hour</strong> for a standard <strong>35-hour week</strong>, plus <strong>6 hours of overtime</strong> paid at <strong>time-and-a-half (1.5×)</strong>. Calculate their total gross weekly wage.',
                'solution_steps': '1. Basic pay = 35 × £12.80 = £448.00.<br>2. Overtime rate = £12.80 × 1.5 = £19.20/hr &rarr; 6 × £19.20 = £115.20.<br>3. Total gross pay = £448.00 + £115.20 = £563.20.',
                'correct_answer': '£563.20',
                'tutor_tip': 'Alternatively, 6 hours at 1.5× equals 9 standard hours: (35 + 9) × £12.80 = 44 × £12.80 = £563.20.'
            },
            {
                'marks': '3 Marks',
                'question': 'A trade wholesaler supplies plumbing fittings with a list price of <strong>£450.00</strong>. The plumber receives a <strong>10% trade discount</strong>, and then <strong>20% VAT</strong> is added to the discounted amount. Calculate the final invoice total.',
                'solution_steps': '1. 10% trade discount = £45.00 &rarr; Net subtotal = £450 - £45 = £405.00.<br>2. 20% VAT on £405.00 = 0.20 × £405 = £81.00.<br>3. Final invoice total = £405.00 + £81.00 = £486.00.',
                'correct_answer': '£486.00',
                'tutor_tip': 'Never just add 10% (-10% + 20% is NOT +10%)! Calculate the discounted price first, then add 20% VAT.'
            }
        ]
    },
    {
        'filename': 'functional-skills-best-buys.html',
        'clean_topic': 'Best Buys & Unit Pricing',
        'intro_lead': 'Compare supermarket multi-buys, packaging sizes, and trade discounts by calculating the unit price (price per gram, per kilogram, or per unit) to determine the best financial value.',
        'next_file': 'functional-skills-interest-and-compound-interest.html',
        'next_name': 'Simple & Compound Interest',
        'spec_points': [
            ('L1.15 / L2.17', 'Compare costs and unit pricing (e.g. price per 100g, per litre) to determine the best value option.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-tag',
                'title': 'Golden Rule 1: Unit Price = Cost ÷ Quantity',
                'desc': 'Always divide the PRICE by the QUANTITY to find the cost of 1 unit (1 gram, 100g, 1 kg, 1 litre). The option with the LOWEST unit price is the best value.',
                'badge': 'Unit Price = £ Price ÷ Quantity'
            },
            {
                'icon': 'fa-scale-unbalanced-flip',
                'title': 'Golden Rule 2: Convert to Common Units Before Dividing',
                'desc': 'Never compare a 750g tub with a 2 kg tub directly. Convert 2 kg to 2,000g, or compare both per 100g or per 1 kg.',
                'badge': 'Match units first: grams to grams, ml to ml'
            }
        ],
        'skills': [
            {
                'title': 'Skill 1: The Unit Cost Method (Cost per Litre, per kg, or per Item)',
                'summary': 'The universal calculator method for any pack size comparison.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Cost per 1 Litre / 1 kg:</strong> Divide price by litres or kilograms (e.g. <code>2.5 L for £4.50 &rarr; £4.50 ÷ 2.5 = £1.80 per litre</code>).</li>
                    <li><strong>Cost per 100g / 100ml:</strong> Divide price by the number of 100g units (e.g. <code>600g for £2.70 &rarr; £2.70 ÷ 6 = £0.45 (45p) per 100g</code>).</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Skill 2: Scaling to a Common Quantity (Non-Calculator Best Method)',
                'summary': 'Multiplying up to a common weight or volume without doing awkward divisions.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">When comparing <strong>400 g for £1.65</strong> and <strong>600 g for £2.40</strong>, scale both to their Lowest Common Multiple (<strong>1,200 g</strong>):</p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>400 g pack × 3 (1,200 g):</strong> <code>3 × £1.65 = £4.95</code>.</li>
                    <li><strong>600 g pack × 2 (1,200 g):</strong> <code>2 × £2.40 = £4.80</code>.</li>
                    <li>Since <code>£4.80 &lt; £4.95</code>, the <strong>600 g pack</strong> is better value by 15p per 1.2 kg.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Skill 3: Evaluating Multi-Buy Offers ("3 for 2" & "Buy One Get One Half Price")',
                'summary': 'How to find the true effective unit price of promotional bundles.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:left;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Promotional Offer</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">How to Calculate Bundle Cost</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Example (Base Price £6.00)</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">3 for the Price of 2</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">Pay for 2 items, receive 3 items</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;"><code>2 × £6 = £12 for 3 &rarr; £4.00 each</code></td>
                      </tr>
                      <tr>
                        <td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">Buy 1, Get 2nd Half Price</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">Pay 1.5× single price for 2 items</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;"><code>£6 + £3 = £9 for 2 &rarr; £4.50 each</code></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Model 1 (Level 1 Foundation): Care Home Laundry Detergent Procurement Comparison',
                'marks': '3 Marks (Pearson Edexcel Level 1/2)',
                'context': 'Care Facility Commercial Purchasing',
                'question': 'A care home procurement manager must purchase commercial laundry detergent. Two brands are available:<br>• Brand A: <strong>4.5 litres</strong> for <strong>£14.40</strong><br>• Brand B: <strong>6 litres</strong> for <strong>£18.60</strong><br>(a) Calculate the cost per litre for each brand.<br>(b) Which brand offers the best value for money?',
                'steps': [
                    ('Step 1', 'Calculate cost per litre for Brand A', '£14.40 ÷ 4.5 litres = £3.20 per litre.', 'M1: Brand A unit division'),
                    ('Step 2', 'Calculate cost per litre for Brand B', '£18.60 ÷ 6 litres = £3.10 per litre.', 'M1: Brand B unit division'),
                    ('Step 3', 'Compare unit prices and conclude', 'Brand B is £3.10 per litre, which is 10p cheaper per litre than Brand A (£3.20). Therefore, Brand B offers the best value.', 'A1: Correct comparison and conclusion')
                ],
                'final_answer': '(a) Brand A = £3.20/L, Brand B = £3.10/L | (b) Brand B is the best value (10p cheaper per litre).',
                'tutor_tip': 'Always conclude with a written sentence naming the winning option and stating both unit prices.'
            },
            {
                'title': 'Model 2 (Level 2 Decision): Clinic Paper Towel Bulk Order Multi-Buy Comparison',
                'marks': '4 Marks (Pearson Edexcel Level 2 Problem Solving)',
                'context': 'Clinical Supplies Procurement',
                'question': 'A dental practice needs to buy <strong>24 rolls</strong> of clinical couch roll. Three wholesalers offer the following deals:<br>• <strong>Wholesaler A:</strong> Packs of <strong>6 rolls for £19.50</strong>, with a <strong>"Buy 3 packs, get 4th pack free"</strong> promotion.<br>• <strong>Wholesaler B:</strong> Packs of <strong>8 rolls for £24.00</strong>, with a <strong>15% trade discount</strong> on all orders.<br>• <strong>Wholesaler C:</strong> A bulk box of <strong>24 rolls for £59.50</strong>.<br><br>Which wholesaler is the cheapest way to buy 24 rolls, and what is the lowest total cost?',
                'steps': [
                    ('Step 1', 'Calculate cost for 24 rolls with Wholesaler A', '24 rolls ÷ 6 rolls/pack = 4 packs needed.<br>With "Buy 3, get 4th free", the practice pays for 3 packs: 3 × £19.50 = £58.50.', 'M1: Wholesaler A cost (£58.50)'),
                    ('Step 2', 'Calculate cost for 24 rolls with Wholesaler B', '24 rolls ÷ 8 rolls/pack = 3 packs needed.<br>List price = 3 × £24.00 = £72.00.<br>After 15% discount: £72.00 × 0.85 = £61.20.', 'M1: Wholesaler B discounted cost (£61.20)'),
                    ('Step 3', 'Compare all three totals for 24 rolls', 'Wholesaler A = £58.50 | Wholesaler B = £61.20 | Wholesaler C = £59.50.', 'M1: Direct comparison of all 3 options'),
                    ('Step 4', 'State final decision and lowest cost', 'Wholesaler A is the cheapest option at £58.50 (£1.00 cheaper than Wholesaler C and £2.70 cheaper than Wholesaler B).', 'A1: Correct wholesaler (A) and £58.50 total')
                ],
                'final_answer': 'Wholesaler A is cheapest at £58.50 (vs £61.20 for B and £59.50 for C).',
                'tutor_tip': 'When a target quantity is given (24 rolls), comparing the total cost for all 24 rolls is much faster and more accurate than finding the price of 1 single roll!'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Dividing Quantity by Price Instead of Price by Quantity',
                'desc': 'Calculating 4.5 ÷ 14.40 = 0.3125 gives litres per pound, not cost per litre. While mathematically valid, learners frequently misinterpret whether the higher or lower number is better.',
                'fix': 'Always do Money ÷ Amount: Cost per Litre = £ ÷ Litres (lower cost is better).'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'A supermarket sells olive oil in two bottle sizes: <strong>250 ml for £2.80</strong>, and <strong>750 ml for £7.20</strong>. Which size is better value for money? Show working to support your answer.',
                'solution_steps': '1. Scale 250 ml up to 750 ml (multiply by 3): 3 × £2.80 = £8.40.<br>2. Compare: £7.20 for 750 ml is £1.20 cheaper than £8.40.<br>3. Conclusion: The 750 ml bottle is better value.',
                'correct_answer': '750 ml bottle is better value (£7.20 vs £8.40 for 750 ml).',
                'tutor_tip': 'Multiplying 250 ml by 3 is faster and cleaner than dividing.'
            },
            {
                'marks': '3 Marks',
                'question': 'Coffee granules are sold in three jar sizes:<br>• Small: <strong>200 g for £3.60</strong><br>• Medium: <strong>500 g for £8.50</strong><br>• Large: <strong>1.2 kg for £21.00</strong><br>Work out the cost per 100 g for each jar to determine which jar offers the best value.',
                'solution_steps': '1. Small (200 g): £3.60 ÷ 2 = £1.80 per 100 g.<br>2. Medium (500 g): £8.50 ÷ 5 = £1.70 per 100 g.<br>3. Large (1.2 kg = 1,200 g): £21.00 ÷ 12 = £1.75 per 100 g.<br>4. Best value: The Medium (500 g) jar is cheapest at £1.70 per 100 g.',
                'correct_answer': 'Medium 500 g jar is best value (£1.70 per 100g vs £1.75 for Large and £1.80 for Small).',
                'tutor_tip': 'Never assume the largest pack is automatically the cheapest! Examiners love designing questions where the middle size wins.'
            },
            {
                'marks': '3 Marks',
                'question': 'An office manager needs <strong>30 A4 notebooks</strong>. Shop X sells them at <strong>£2.40 each</strong> with a <strong>"3 for the price of 2"</strong> offer. Shop Y sells packs of <strong>10 notebooks for £16.50</strong> with a <strong>10% discount</strong>. Which shop is cheaper for 30 notebooks?',
                'solution_steps': '1. Shop X: 30 notebooks = 10 groups of 3 &rarr; pay for 20 notebooks: 20 × £2.40 = £48.00.<br>2. Shop Y: 3 packs of 10 = 3 × £16.50 = £49.50. Less 10% (£4.95) = £44.55.<br>3. Conclusion: Shop Y is cheaper (£44.55 vs £48.00).',
                'correct_answer': 'Shop Y is cheaper (£44.55 vs £48.00 at Shop X).',
                'tutor_tip': 'In a "3 for 2" deal on 30 items, you pay for 2/3 of the items (20 items).'
            }
        ]
    },
    {
        'filename': 'functional-skills-interest-and-compound-interest.html',
        'clean_topic': 'Simple & Compound Interest',
        'intro_lead': 'Calculate annual simple interest, compound interest over multi-year periods, compare savings accounts and loan repayments, and compute investment growth.',
        'next_file': 'functional-skills-time.html',
        'next_name': 'Time & Timetables',
        'spec_points': [
            ('L2.16', 'Calculate simple interest and compound interest on loans and savings over multiple periods.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-coins',
                'title': 'Golden Rule 1: Simple Interest Remains Constant Every Year',
                'desc': 'Simple interest is calculated only on the original principal amount. If £2,000 earns 5% simple interest, it earns £100 every single year.',
                'badge': 'Simple Interest = Principal × Rate × Time'
            },
            {
                'icon': 'fa-chart-line',
                'title': 'Golden Rule 2: Compound Interest: Calculate Year by Year or Use a Multiplier',
                'desc': "Compound interest adds each year's interest to the balance before calculating the next year's interest. Or multiply by the decimal multiplier for each year: Starting Balance × (1 + r)ⁿ.",
                'badge': 'Final Balance = Principal × (Multiplier)ⁿ'
            }
        ],
        'skills': [
            {
                'title': 'Skill 1: Year-by-Year vs Multiplier Method for Compound Interest',
                'summary': 'Two reliable methods for non-calculator and calculator papers.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">To calculate <strong>£5,000</strong> invested at <strong>4% compound interest for 2 years</strong>:</p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Year-by-Year Method:</strong><br>
                    Year 1: <code>4% of £5,000 = £200</code> &rarr; End of Year 1 Balance = <code>£5,200</code>.<br>
                    Year 2: <code>4% of £5,200 = £208</code> &rarr; End of Year 2 Balance = <code>£5,408.00</code>.</li>
                    <li><strong>Multiplier Method (Calculator):</strong><br>
                    Multiplier for +4% is <code>1 + 0.04 = 1.04</code>.<br>
                    Final Balance = <code>£5,000 × 1.04² = £5,000 × 1.0816 = £5,408.00</code>.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Skill 2: Simple Interest vs Compound Interest Direct Comparison',
                'summary': 'Why compound interest grows faster over multi-year terms.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:center;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Year (on £1,000 at 10%)</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">10% Simple Interest Balance</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">10% Compound Interest Balance</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Year 1</td><td style="padding:6px; border:1px solid #cbd5e1;">£1,100.00 (+£100)</td><td style="padding:6px; border:1px solid #cbd5e1;">£1,100.00 (+£100)</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Year 2</td><td style="padding:6px; border:1px solid #cbd5e1;">£1,200.00 (+£100)</td><td style="padding:6px; border:1px solid #cbd5e1;">£1,210.00 (+£110)</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Year 3</td><td style="padding:6px; border:1px solid #cbd5e1;">£1,300.00 (+£100)</td><td style="padding:6px; border:1px solid #cbd5e1;">£1,331.00 (+£121)</td></tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                'title': 'Skill 3: Compound Depreciation (Decreasing Value Over Time)',
                'summary': 'Using a subtraction multiplier (1 - r)ⁿ for vehicle and equipment depreciation.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">When an asset loses value each year (e.g. a medical van bought for <strong>£20,000</strong> depreciates by <strong>15% per year</strong> for 2 years):</p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Multiplier:</strong> <code>100% - 15% = 85% = 0.85</code>.</li>
                    <li><strong>Value after 2 years:</strong> <code>£20,000 × 0.85² = £20,000 × 0.7225 = £14,450.00</code>.</li>
                  </ul>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Model 1 (Level 1/2 Foundation): Care Home Capital Equipment Reserve Investment',
                'marks': '3 Marks (Pearson Edexcel Level 2)',
                'context': 'Healthcare Reserve Fund Management',
                'question': 'A care home trustees board invests <strong>£12,000</strong> in a fixed-rate savings bond paying <strong>3% compound interest per annum</strong> for <strong>3 years</strong>.<br>Calculate the <strong>total interest earned</strong> over the 3 years.',
                'steps': [
                    ('Step 1', 'Calculate Year 1 interest and balance', '3% of £12,000 = 0.03 × 12,000 = £360.<br>Balance at end of Year 1 = £12,000 + £360 = £12,360.', 'M1: Year 1 calculation'),
                    ('Step 2', 'Calculate Year 2 interest and balance', '3% of £12,360 = 0.03 × 12,360 = £370.80.<br>Balance at end of Year 2 = £12,360 + £370.80 = £12,730.80.', 'M1: Year 2 compound step'),
                    ('Step 3', 'Calculate Year 3 interest and total interest earned', '3% of £12,730.80 = 0.03 × 12,730.80 = £381.92.<br>Final Balance = £13,112.72.<br>Total Interest Earned = £13,112.72 - £12,000 = £1,112.72.', 'A1: Accurate total interest earned')
                ],
                'final_answer': 'Total Interest Earned = £1,112.72',
                'tutor_tip': 'Notice the question asks for the TOTAL INTEREST EARNED, not the final balance! Always subtract the starting principal (£12,000).'
            },
            {
                'title': 'Model 2 (Level 2 Decision): Savings Bond Comparison (Compound vs Simple Interest)',
                'marks': '4 Marks (Pearson Edexcel Level 2 Problem Solving)',
                'context': 'Personal Savings Account Selection',
                'question': 'A clinical nurse specialist wants to invest <strong>£8,000</strong> for <strong>2 years</strong>. She compares two accounts:<br>• <strong>Account A (Platinum Bond):</strong> Pays <strong>4.5% compound interest</strong> per annum.<br>• <strong>Account B (Fixed Income Bond):</strong> Pays <strong>4.6% simple interest</strong> per annum.<br><br>Which account will yield the higher balance at the end of 2 years, and by how much?',
                'steps': [
                    ('Step 1', 'Calculate final balance for Account A (4.5% compound for 2 years)', 'Multiplier = 1.045.<br>Balance A = £8,000 × 1.045 × 1.045 = £8,736.20.', 'M1: Compound interest calculation for Account A'),
                    ('Step 2', 'Calculate final balance for Account B (4.6% simple for 2 years)', '1 year simple interest = £8,000 × 0.046 = £368.00.<br>2 years interest = 2 × £368.00 = £736.00.<br>Balance B = £8,000 + £736.00 = £8,736.00.', 'M1: Simple interest calculation for Account B'),
                    ('Step 3', 'Find the exact difference between the two balances', '£8,736.20 - £8,736.00 = £0.20 (20p).', 'M1: Difference calculation'),
                    ('Step 4', 'State final justified conclusion', 'Account A yields the higher balance by 20p (£8,736.20 vs £8,736.00).', 'A1: Correct account (A) and exact difference (£0.20 / 20p)')
                ],
                'final_answer': 'Account A yields a higher balance by £0.20 / 20p (£8,736.20 vs £8,736.00).',
                'tutor_tip': 'Do not round intermediate decimals when squaring 1.045 (1.045² = 1.092025) so you capture the exact 20p difference!'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Giving the Final Balance Instead of the Interest',
                'desc': "If the question asks 'How much interest was earned?', stating £13,112.72 instead of £1,112.72 forfeits the final accuracy mark.",
                'fix': "Highlight the word 'interest' or 'total balance' in the question stem."
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'A worker takes a loan of <strong>£3,500</strong> at <strong>6% simple interest</strong> per year. How much total interest will they pay over <strong>4 years</strong>?',
                'solution_steps': '1. 1 year interest = 6% of £3,500 = 0.06 × 3,500 = £210.<br>2. 4 years total interest = £210 × 4 = £840.00.',
                'correct_answer': '£840.00',
                'tutor_tip': 'Simple interest is identical every year: £210 × 4.'
            },
            {
                'marks': '3 Marks',
                'question': 'A saver deposits <strong>£6,500</strong> into an ISA paying <strong>4% compound interest per year</strong>. Calculate the total balance in the account after <strong>2 years</strong>.',
                'solution_steps': '1. Year 1: £6,500 × 1.04 = £6,760.00.<br>2. Year 2: £6,760.00 × 1.04 = £7,030.40.',
                'correct_answer': '£7,030.40',
                'tutor_tip': 'Remember to write the trailing zero (£7,030.40, not £7,030.4).'
            },
            {
                'marks': '3 Marks',
                'question': 'A hospital buys an electric delivery van for <strong>£25,000</strong>. The van depreciates in value by <strong>20% each year</strong> (compound depreciation). What is the value of the van after <strong>3 years</strong>?',
                'solution_steps': '1. Multiplier for 20% decrease = 1 - 0.20 = 0.80.<br>2. After Year 1: £25,000 × 0.8 = £20,000.<br>3. After Year 2: £20,000 × 0.8 = £16,000.<br>4. After Year 3: £16,000 × 0.8 = £12,800.00.',
                'correct_answer': '£12,800.00',
                'tutor_tip': 'Do NOT subtract 60% (3 × 20%)! Apply the 20% reduction year by year.'
            }
        ]
    },
    {
        'filename': 'functional-skills-problems-involving-money.html',
        'clean_topic': 'Problems Involving Money & Multi-Tier Pricing',
        'intro_lead': 'Solve complex, multi-stage financial problems involving travel fares, group admissions, discounts, currency exchange, and household utility bill comparisons.',
        'next_file': 'functional-skills-time.html',
        'next_name': 'Time & Timetables',
        'spec_points': [
            ('L1.14 / L2.15', 'Solve multi-step problems involving money and budgeting in everyday contexts.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-list-check',
                'title': 'Golden Rule 1: Deconstruct Multi-Tier Pricing into Line Items',
                'desc': 'Break pricing into: 1. Base fee / Standing charge. 2. Per-unit or hourly charge. 3. Promotional discounts. 4. VAT or taxes. Sum systematically.',
                'badge': 'Standing Charge + (Rate × Units) - Discounts + Taxes'
            },
            {
                'icon': 'fa-sterling-sign',
                'title': 'Golden Rule 2: Mind the Pence-to-Pounds Conversion',
                'desc': 'Never mix pounds and pence without converting. 45p + £3.20 is NOT 48.20! Convert 45p to £0.45 before adding (£0.45 + £3.20 = £3.65).',
                'badge': '14.5p per kWh = £0.145 per kWh (Divide pence by 100)'
            }
        ],
        'skills': [
            {
                'title': 'Skill 1: Foreign Currency Exchange Calculations (Buying & Selling)',
                'summary': 'Converting between GBP (£) and foreign currencies (€ / $) with commission.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>GBP (£) to Foreign Currency:</strong> MULTIPLY by the exchange rate: <em>£500 × 1.16 = €580.00.</em></li>
                    <li><strong>Foreign Currency back to GBP (£):</strong> DIVIDE by the exchange rate: <em>€464 ÷ 1.16 = £400.00.</em></li>
                    <li><strong>Handling Commission:</strong> If a travel bureau charges 2% commission, deduct 2% before converting (or multiply by <code>0.98</code>).</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Skill 2: Household & Commercial Utility Bills (Electricity & Gas Meters)',
                'summary': 'Calculating unit consumption from meter readings, standing charges, and 5% energy VAT.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Units Used (kWh):</strong> <code>Present Meter Reading − Previous Meter Reading</code>.</li>
                    <li><strong>Usage Charge:</strong> <code>Units Used × Cost per kWh</code> (convert pence to pounds by dividing by 100!).</li>
                    <li><strong>Standing Charge:</strong> <code>Number of Days × Daily Standing Charge</code>.</li>
                    <li><strong>Total Bill:</strong> Sum Usage + Standing Charge, then add <strong>5% domestic energy VAT</strong> (<code>× 1.05</code>).</li>
                  </ol>
                </div>
                """
            },
            {
                'title': 'Skill 3: Group Booking Tariffs & Family/Multi-Ticket Combinations',
                'summary': 'Checking whether a family/group pass is cheaper than individual tickets.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">When booking for a mixed group (e.g. <strong>2 Adults and 3 Children</strong> where Adult = £18, Child = £11, and a Family Ticket for 2 Adults + 2 Children = £48):</p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Option 1 (All Individual):</strong> <code>(2 × £18) + (3 × £11) = £36 + £33 = £69.00</code>.</li>
                    <li><strong>Option 2 (1 Family Ticket + 1 Extra Child):</strong> <code>£48 + £11 = £59.00</code> (Saves £10.00!).</li>
                  </ul>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Model 1 (Level 1 Foundation): Care Home Resident Day Trip Outing Budget',
                'marks': '3 Marks (Pearson Edexcel Level 1/2)',
                'context': 'Care Home Activities Coordination',
                'question': 'An activities coordinator organizes a botanical garden trip for <strong>18 residents and 4 care assistants</strong>. Admission costs:<br>• Adult: <strong>£15.00</strong><br>• Senior (resident): <strong>£10.50</strong><br>• Group discount: <strong>15% off total ticket price for groups over 20 people</strong>.<br>Calculate the total discounted ticket cost.',
                'steps': [
                    ('Step 1', 'Calculate gross ticket costs before discount', '4 adults × £15.00 = £60.00<br>18 seniors × £10.50 = £189.00<br>Total gross = £60.00 + £189.00 = £249.00', 'M1: Line item multiplication and sum'),
                    ('Step 2', 'Verify group size qualification for discount', '18 + 4 = 22 people. Since 22 > 20, the 15% discount applies.', 'B1: Qualification check'),
                    ('Step 3', 'Calculate 15% discount and net payable', '15% of £249 = 0.15 × 249 = £37.35.<br>Discounted total = £249.00 - £37.35 = £211.65.', 'A1: Accurate discounted total')
                ],
                'final_answer': 'Total Discounted Cost = £211.65',
                'tutor_tip': 'You can also calculate 85% of £249.00 directly: 249 × 0.85 = £211.65.'
            },
            {
                'title': 'Model 2 (Level 2 Decision): Clinic Quarterly Electricity Meter Bill Audit',
                'marks': '4 Marks (Pearson Edexcel Level 2 Problem Solving)',
                'context': 'Commercial Utility Cost Verification',
                'question': 'A physiotherapy clinic checks its 90-day quarterly electricity bill:<br>• Previous meter reading: <strong>14,280 kWh</strong> | Present meter reading: <strong>16,680 kWh</strong><br>• Unit rate: <strong>24p per kWh</strong><br>• Daily standing charge: <strong>45p per day</strong> (for 90 days)<br>• VAT: <strong>5% on the total bill</strong><br><br>The clinic manager has budgeted <strong>£650.00</strong> for this quarter\'s electricity. Is the budget sufficient?',
                'steps': [
                    ('Step 1', 'Calculate electricity units (kWh) used and unit cost in pounds', 'Units used = 16,680 - 14,280 = 2,400 kWh.<br>Unit cost = 2,400 × £0.24 = £576.00.', 'M1: Meter subtraction and pence-to-pounds unit cost'),
                    ('Step 2', 'Calculate 90-day standing charge and pre-VAT subtotal', 'Standing charge = 90 × £0.45 = £40.50.<br>Subtotal = £576.00 + £40.50 = £616.50.', 'M1: Standing charge and subtotal addition'),
                    ('Step 3', 'Add 5% VAT and round to nearest penny', '5% VAT = £616.50 × 0.05 = £30.825.<br>Total bill = £616.50 + £30.825 = £647.325 → £647.33.', 'M1: Adding 5% VAT'),
                    ('Step 4', 'Compare against £650.00 budget', '£647.33 < £650.00. Yes, the £650 budget is sufficient with £2.67 remaining.', 'A1: Accurate total (£647.33) and valid decision')
                ],
                'final_answer': 'Yes, sufficient (Total electricity bill is £647.33, which is £2.67 under the £650.00 budget).',
                'tutor_tip': 'Always convert 24p to £0.24 and 45p to £0.45 before multiplying so you don\'t mix pence and pounds!'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Forgetting Staff in Group Counts or Mixing Pence and Pounds',
                'desc': 'Adding 2,400 × 24 = 57,600 onto £40.50 without dividing pence by 100 is a classic exam error.',
                'fix': 'Convert every pence figure into pounds (£0.24) before starting your calculations.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'A staff canteen offers a <strong>10% discount</strong> on orders over <strong>£25</strong>. A department orders <strong>6 sandwiches at £3.50 each</strong> and <strong>4 coffees at £2.25 each</strong>. What is the total discounted cost?',
                'solution_steps': '1. 6 × £3.50 = £21.00; 4 × £2.25 = £9.00.<br>2. Subtotal = £21 + £9 = £30.00 (qualifies for 10% discount).<br>3. 10% discount = £3.00. Total = £30.00 - £3.00 = £27.00.',
                'correct_answer': '£27.00',
                'tutor_tip': 'Check that the subtotal exceeds £25 before applying the discount.'
            },
            {
                'marks': '2 Marks',
                'question': 'A nurse travels to a medical conference in Dublin. She exchanges <strong>£450</strong> into Euros (€) at an exchange rate of <strong>£1 = €1.16</strong>. During the trip she spends <strong>€382.80</strong> and converts the remaining Euros back into pounds at the same rate. How many pounds (£) does she get back?',
                'solution_steps': '1. GBP to Euros: £450 × 1.16 = €522.00.<br>2. Remaining Euros: €522.00 - €382.80 = €139.20.<br>3. Euros back to GBP: €139.20 ÷ 1.16 = £120.00.',
                'correct_answer': '£120.00',
                'tutor_tip': 'Multiply to go from £ to €, and divide by the rate to convert € back to £.'
            },
            {
                'marks': '3 Marks',
                'question': 'A car hire firm charges <strong>£38.00 per day</strong> plus <strong>15p per mile</strong> for every mile driven over a free allowance of <strong>100 miles per day</strong>. Calculate the total cost to hire a car for <strong>3 days</strong> and drive a total of <strong>460 miles</strong>.',
                'solution_steps': '1. 3-day hire fee = 3 × £38.00 = £114.00.<br>2. Free mileage allowance for 3 days = 3 × 100 = 300 miles.<br>3. Excess miles = 460 - 300 = 160 miles @ £0.15/mile = £24.00.<br>4. Total cost = £114.00 + £24.00 = £138.00.',
                'correct_answer': '£138.00',
                'tutor_tip': 'Remember the free mileage allowance is 100 miles PER DAY (300 miles over 3 days), not 100 miles total!'
            }
        ]
    }
]
