#!/usr/bin/env python3
"""Maths Basics & Additional Revise Topics (15 Topics)"""

EXTRAS_MATHS = [
    {
        'filename': 'functional-skills-number-basics.html',
        'clean_topic': 'Number Basics: Place Value & Counting',
        'intro_lead': 'Build foundational confidence with whole numbers up to 10,000, understand thousands, hundreds, tens, and units columns, recognize odd/even and multiples, and solve workplace stock tally problems.',
        'next_file': 'functional-skills-numbers-and-place-value.html',
        'next_name': 'Numbers & Place Value',
        'spec_points': [
            ('E3.1 / L1.1', 'Count, read, write, order, and compare whole numbers up to 1,000 and beyond.'),
            ('E3.2 / L1.1', 'Understand place value in 3-digit and 4-digit numbers and use zero as a positional placeholder.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-cubes',
                'title': 'Golden Rule 1: The Thousands, Hundreds, Tens & Units Model',
                'desc': 'In a 4-digit number like 3,482: 3 means 3 thousands (3,000), 4 means 4 hundreds (400), 8 means 8 tens (80), and 2 means 2 units (2). If a column is empty, write 0 to hold the place!',
                'badge': 'Thousands (1,000) • Hundreds (100) • Tens (10) • Units (1)'
            },
            {
                'icon': 'fa-arrow-up-right-dots',
                'title': 'Golden Rule 2: Align Digits by the Right-Hand Units Column',
                'desc': 'When adding, subtracting, or comparing whole numbers of different lengths (e.g. 1,240 and 85), always line up the rightmost Units digits vertically.',
                'badge': 'Line up Units under Units, Tens under Tens, Hundreds under Hundreds'
            }
        ],
        'skills': [
            {
                'title': 'Partitioning & Place Value Breakdown up to 10,000',
                'summary': 'Splitting numbers into thousands, hundreds, tens, and units and using zero placeholders.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Expanded Partitioning:</strong> 4,658 = <strong>4,000 + 600 + 50 + 8</strong>.</li>
                    <li><strong>Zero Placeholders:</strong> "Two thousand and forty-seven" has no hundreds, so we write <strong>2,047</strong> (not 247!).</li>
                    <li><strong>Comparing Size:</strong> Compare the leftmost column first: 842 &gt; 799 because 8 hundreds is greater than 7 hundreds.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Counting in Multiples of 2, 5, 10, 25, 50, and 100',
                'summary': 'Rapidly counting boxed stock, coin bundles, and crate pallets.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:left;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Multiple Step</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Pattern Rule</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Workplace Application</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Multiples of 2 (Even)</td><td style="padding:6px; border:1px solid #cbd5e1;">Ends in 0, 2, 4, 6, or 8</td><td style="padding:6px; border:1px solid #cbd5e1;">Pairs of surgical gloves, twin-packs</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Multiples of 5 &amp; 10</td><td style="padding:6px; border:1px solid #cbd5e1;">Ends in 5 or 0 (10s end in 0)</td><td style="padding:6px; border:1px solid #cbd5e1;">Tally gates of 5, blister packs of 10 tablets</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Multiples of 25 &amp; 50</td><td style="padding:6px; border:1px solid #cbd5e1;">25, 50, 75, 100, 125, 150...</td><td style="padding:6px; border:1px solid #cbd5e1;">Catering trays, box crates of 25 or 50</td></tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                'title': 'Column Addition, Subtraction & Reverse Checking',
                'summary': 'Setting out vertical calculations and checking by doing the opposite operation.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Column Addition:</strong> Add units first; if the sum is 10 or more, write the unit digit and carry the 1 ten to the next column.</li>
                    <li><strong>Reverse Check for Subtraction:</strong> If 450 &minus; 185 = 265, check by adding <strong>265 + 185 = 450</strong>.</li>
                  </ul>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Care Home Resident Laundry Bag Count (Entry 3 / Level 1 Foundation)',
                'marks': '2 Marks (Entry Level 3 / Level 1)',
                'context': 'Care Facility Domestic Services',
                'question': 'A laundry assistant receives <strong>three deliveries</strong> of clean bath towels: <strong>240 towels, 185 towels, and 75 towels</strong>.<br>Calculate the total number of towels received and show a reverse subtraction check.',
                'steps': [
                    ('Step 1', 'Add the three delivery quantities in aligned columns', '240 + 185 = 425 towels.<br>425 + 75 = 500 towels.', 'M1 / A1: Accurate total (500 towels)'),
                    ('Step 2', 'Show a reverse operation check', '500 − 75 = 425; 425 − 185 = 240.', 'B1: Valid reverse check')
                ],
                'final_answer': '500 towels (Check: 500 − 75 − 185 = 240)',
                'tutor_tip': 'Spot number bonds to 100: 185 + 75 = 260, and 240 + 260 = 500.'
            },
            {
                'title': 'Hospital Central Stores PPE Stock Audit & Reorder Threshold (Level 1/2 Multi-Step)',
                'marks': '4 Marks (Pearson Edexcel Level 1/2)',
                'context': 'Healthcare Warehouse Stock Control',
                'question': 'At the start of the month, a hospital store holds <strong>3,050 boxes</strong> of disposable aprons.<br>• Week 1 issue: <strong>685 boxes</strong> | Week 2 issue: <strong>740 boxes</strong> | Week 3 issue: <strong>825 boxes</strong><br>• The procurement system automatically orders a restock of <strong>1,500 boxes</strong> if remaining stock falls <strong>below 850 boxes</strong>.<br>Determine whether the automatic restock is triggered at the end of Week 3, and calculate the final stock after any restock.',
                'steps': [
                    ('Step 1', 'Sum the boxes issued across Weeks 1, 2, and 3', '685 + 740 + 825 = 2,250 boxes issued.', 'M1: Total stock issued (2,250)'),
                    ('Step 2', 'Subtract issued stock from starting stock (3,050)', '3,050 − 2,250 = 800 boxes remaining.', 'M1: Remaining stock (800)'),
                    ('Step 3', 'Compare 800 with the 850 threshold and add 1,500 restock', 'Since 800 < 850, YES, the restock is triggered.<br>Final stock = 800 + 1,500 = 2,300 boxes.', 'M1 / A1: Yes decision and 2,300 final stock')
                ],
                'final_answer': 'Yes, restock triggered (800 < 850) — Final stock = 2,300 boxes',
                'tutor_tip': 'Notice how 685 + 825 = 1,510, plus 740 = 2,250.'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Misaligning Digits in Column Addition',
                'desc': 'Writing 75 underneath the hundreds and tens columns of 240 instead of the tens and units columns.',
                'fix': 'Always align the rightmost units digits vertically.'
            },
            {
                'title': 'Omitting the Zero Placeholder in Words-to-Figures Questions',
                'desc': 'Writing "three thousand and fifty" as 350 instead of 3,050.',
                'fix': 'Check that a thousand number always has 4 digits (3,050).'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'Write the number <strong>four thousand, and sixty-nine</strong> in figures, and state the value of the digit <strong>6</strong>.',
                'solution_steps': '1. Thousands = 4, Hundreds = 0, Tens = 6, Units = 9 → 4,069.<br>2. Digit 6 is in the tens column → 60 (sixty).',
                'correct_answer': '4,069; value of 6 is 60',
                'tutor_tip': 'Include the 0 in the hundreds column so the 4 stays in the thousands place.'
            },
            {
                'marks': '3 Marks',
                'question': 'A catering supplier packs soup tins in trays of <strong>25 tins</strong>. A care home orders <strong>14 full trays</strong>, plus <strong>18 loose tins</strong>. How many soup tins are delivered in total?',
                'solution_steps': '1. Tins in trays = 14 × 25 = 350 tins.<br>2. Add loose tins = 350 + 18 = 368 tins.',
                'correct_answer': '368 tins',
                'tutor_tip': '4 trays of 25 = 100, so 12 trays = 300, and 14 trays = 350.'
            },
            {
                'marks': '3 Marks',
                'question': 'Four regional clinics report their monthly patient registrations: <strong>Clinic A: 1,408, Clinic B: 1,084, Clinic C: 1,480, Clinic D: 1,048</strong>.<br>(a) Arrange the four numbers in ascending order (smallest to largest).<br>(b) Calculate the difference between the highest and lowest clinic registrations.',
                'solution_steps': '1. Ascending order: 1,048, 1,084, 1,408, 1,480.<br>2. Difference = 1,480 − 1,048 = 432 patients.',
                'correct_answer': '(a) 1,048, 1,084, 1,408, 1,480 | (b) 432',
                'tutor_tip': 'Compare the hundreds column first (0 vs 4), then compare the tens column.'
            }
        ]
    },
    {
        'filename': 'functional-skills-fraction-basics.html',
        'clean_topic': 'Fraction Basics: Halves, Quarters & Thirds',
        'intro_lead': 'Understand numerators and denominators, shade and read visual fraction diagrams, find unit and non-unit fractions of everyday quantities, and simplify equivalent fractions.',
        'next_file': 'functional-skills-fractions.html',
        'next_name': 'Fractions',
        'spec_points': [
            ('E3.3 / L1.8', 'Read, write, and understand common unit and non-unit fractions (1/2, 1/4, 3/4, 1/3, 2/3, 1/5, 1/10) and equivalent fractions.'),
            ('E3.4 / L1.9', 'Find fractions of whole-number quantities and measurements in practical contexts.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-pie-chart',
                'title': 'Golden Rule 1: Denominator (Bottom) = Total Equal Parts • Numerator (Top) = Selected Parts',
                'desc': 'The bottom number (denominator) tells you how many equal slices the whole is divided into. The top number (numerator) tells you how many of those slices you have.',
                'badge': 'Numerator (Top) ÷ Denominator (Bottom)'
            },
            {
                'icon': 'fa-divide',
                'title': 'Golden Rule 2: Divide by the Bottom, Multiply by the Top',
                'desc': 'To find a fraction of an amount (e.g. 3/4 of £60): first divide £60 by the bottom number 4 (= £15 for 1/4), then multiply by the top number 3 (3 × £15 = £45).',
                'badge': 'Fraction of Amount = (Amount ÷ Bottom) × Top'
            }
        ],
        'skills': [
            {
                'title': 'Unit Fractions (1/n) vs Non-Unit Fractions (a/b)',
                'summary': 'Finding 1 part first and scaling up to multiple parts.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>1/2 of an amount:</strong> Divide by 2 (Halve it).</li>
                    <li><strong>1/4 of an amount:</strong> Divide by 4 (Halve it, then halve it again).</li>
                    <li><strong>3/4 of an amount:</strong> Divide by 4 to find 1/4, then multiply that answer by 3.</li>
                    <li><strong>2/5 of an amount:</strong> Divide by 5 to find 1/5, then multiply that answer by 2.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Equivalent Fractions & Simplifying to Lowest Terms',
                'summary': 'Multiplying or dividing both top and bottom by the same number.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:center;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Simplest Form</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Equivalent Fractions</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Percentage Equivalent</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">1/2</td><td style="padding:6px; border:1px solid #cbd5e1;">2/4 = 3/6 = 5/10 = 50/100</td><td style="padding:6px; border:1px solid #cbd5e1;">50%</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">1/4</td><td style="padding:6px; border:1px solid #cbd5e1;">2/8 = 3/12 = 5/20 = 25/100</td><td style="padding:6px; border:1px solid #cbd5e1;">25%</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">3/4</td><td style="padding:6px; border:1px solid #cbd5e1;">6/8 = 9/12 = 15/20 = 75/100</td><td style="padding:6px; border:1px solid #cbd5e1;">75%</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">1/5</td><td style="padding:6px; border:1px solid #cbd5e1;">2/10 = 4/20 = 20/100</td><td style="padding:6px; border:1px solid #cbd5e1;">20%</td></tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                'title': 'Finding the Remaining Fraction of a Whole (1 − Fraction)',
                'summary': 'Working out what fraction is left over after portions are used.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">A whole unit is always equal to <strong>n/n</strong> (e.g. 4/4, 5/5, 8/8, 10/10):</p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li>If <strong>3/8</strong> of a ward budget is spent, the remaining fraction unspent is 8/8 &minus; 3/8 = <strong>5/8</strong>.</li>
                  </ul>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Hospital Kitchen Fruit Crate Allocation (Entry 3 / Level 1 Foundation)',
                'marks': '2 Marks (Entry Level 3 / Level 1)',
                'context': 'Catering Food Distribution',
                'question': 'A hospital kitchen receives a crate of <strong>72 apples</strong>. The chef uses <strong>3/4</strong> of the apples for patient lunch trays.<br>How many apples does the chef use, and how many are left over?',
                'steps': [
                    ('Step 1', 'Divide total apples (72) by denominator (4) to find 1/4', '72 ÷ 4 = 18 apples.', 'M1: Unit fraction division (18)'),
                    ('Step 2', 'Multiply by numerator (3) and find remainder', 'Used = 18 × 3 = 54 apples.<br>Left over = 72 − 54 = 18 apples.', 'A1: Accurate used (54) and remaining (18)')
                ],
                'final_answer': '54 apples used, 18 apples left over',
                'tutor_tip': 'Notice that if 3/4 are used, 1/4 (18 apples) is left over!'
            },
            {
                'title': 'Ward Shift Budget Allocation Across Three Expense Categories (Level 1/2 Multi-Step)',
                'marks': '4 Marks (Pearson Edexcel Level 1/2)',
                'context': 'Clinical Department Consumables Budget',
                'question': 'A clinic manager has a monthly consumables budget of <strong>£960</strong>.<br>• She spends <strong>1/3</strong> of the budget on sterile dressings.<br>• She spends <strong>3/8</strong> of the original £960 budget on PPE gloves.<br>• The rest of the money is kept for diagnostic test strips.<br>Calculate how much money (£) is kept for diagnostic test strips.',
                'steps': [
                    ('Step 1', 'Calculate 1/3 of £960 for sterile dressings', '£960 ÷ 3 = £320.', 'M1: Dressings cost (£320)'),
                    ('Step 2', 'Calculate 3/8 of £960 for PPE gloves', '(£960 ÷ 8) × 3 = £120 × 3 = £360.', 'M1: Gloves cost (£360)'),
                    ('Step 3', 'Subtract both expenses from £960', '£960 − (£320 + £360) = £960 − £680 = £280.', 'M1 / A1: Accurate remainder (£280)')
                ],
                'final_answer': '£280 kept for diagnostic test strips',
                'tutor_tip': 'Check by adding all three parts: £320 + £360 + £280 = £960.'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Dividing by the Top Number Instead of the Bottom Number',
                'desc': 'To find 3/4 of 60, dividing 60 by 3 (= 20) instead of dividing 60 by 4 (= 15).',
                'fix': 'Always memorise: "Divide by the BOTTOM, multiply by the TOP."'
            },
            {
                'title': 'Assuming 1/3 is Larger than 1/2 Because 3 is Bigger than 2',
                'desc': 'When a whole is cut into more pieces, each piece is smaller! 1/2 (50%) is larger than 1/3 (33.3%), and 1/3 is larger than 1/4 (25%).',
                'fix': 'For unit fractions (top number 1), the smaller the bottom number, the bigger the slice.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'Calculate <strong>2/5 of 85 metres</strong>.',
                'solution_steps': '1. Find 1/5: 85 ÷ 5 = 17 metres.<br>2. Find 2/5: 17 × 2 = 34 metres.',
                'correct_answer': '34 metres',
                'tutor_tip': '85 ÷ 5 = 17, then 17 × 2 = 34.'
            },
            {
                'marks': '2 Marks',
                'question': 'Out of <strong>40 staff members</strong> on a ward, <strong>28 are female</strong>. Write the fraction of staff who are female in its <strong>simplest form</strong>.',
                'solution_steps': '1. Initial fraction = 28 / 40.<br>2. Divide top and bottom by 4: 28 ÷ 4 = 7; 40 ÷ 4 = 10 → 7/10.',
                'correct_answer': '7/10',
                'tutor_tip': 'Divide both numerator and denominator by their highest common factor (4).'
            },
            {
                'marks': '3 Marks',
                'question': 'A charity fun run is <strong>24 km</strong> long. A paramedic cyclist has completed <strong>5/8</strong> of the route. How many <strong>kilometres does she still have left to cycle</strong>?',
                'solution_steps': '1. Completed = (24 ÷ 8) × 5 = 3 × 5 = 15 km.<br>2. Remaining = 24 − 15 = 9 km (or 3/8 of 24 = 9 km).',
                'correct_answer': '9 km',
                'tutor_tip': 'Read carefully: the question asks for the distance LEFT to cycle (3/8 of 24 = 9 km).'
            }
        ]
    },
    {
        'filename': 'functional-skills-decimal-basics.html',
        'clean_topic': 'Decimal Basics: Tenths, Hundredths & Money',
        'intro_lead': 'Read and write decimal numbers up to two decimal places, connect tenths and hundredths to pounds and pence, order decimals accurately, and round money to the nearest 10p or £1.',
        'next_file': 'functional-skills-decimals.html',
        'next_name': 'Decimals',
        'spec_points': [
            ('E3.5 / L1.10', 'Read, write, order, and compare decimals up to two decimal places in practical contexts such as money and metric length.'),
            ('E3.5 / L1.6', 'Round decimal currency and measurements to the nearest whole unit or tenth.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-coins',
                'title': 'Golden Rule 1: The Decimal Point Separates Whole Units from Tenths & Hundredths',
                'desc': 'In £4.75, the 4 is whole pounds, the 7 is tenths (7 × 10p = 70p), and the 5 is hundredths (5 × 1p = 5p). Single-digit pence from 1p to 9p MUST have a zero in the tenths column (e.g. 6p = £0.06, NEVER £0.6!).',
                'badge': 'Pounds . Tenths (10p) Hundredths (1p) • 6p = £0.06'
            },
            {
                'icon': 'fa-arrows-left-right',
                'title': 'Golden Rule 2: Pad with Trailing Zeros to Compare Decimals (0.5 = 0.50 > 0.08)',
                'desc': 'To compare 0.5 and 0.08, make both numbers have 2 decimal places by writing 0.5 as 0.50. Now it is obvious that 0.50 (50 hundredths) is much larger than 0.08 (8 hundredths).',
                'badge': '0.5 = 0.50 (50p) > 0.08 (8p)'
            }
        ],
        'skills': [
            {
                'title': 'Pounds & Pence Conversion Rules (Avoiding the Mixed-Unit Trap)',
                'summary': 'Writing currency properly with £ or p—never both at the same time.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Pence to Pounds (&divide; 100):</strong> 345p = <strong>&pound;3.45</strong>; 80p = <strong>&pound;0.80</strong>; 7p = <strong>&pound;0.07</strong>.</li>
                    <li><strong>Never Mix &pound; and p:</strong> Write <strong>&pound;0.85</strong> or <strong>85p</strong> — NEVER write <em>"&pound;0.85p"</em>!</li>
                    <li><strong>Always Two Decimal Places for Pounds:</strong> If your calculator shows <strong>4.5</strong> for money, write <strong>&pound;4.50</strong>.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Ordering Decimal Measurements (Metres, Kilograms & Litres)',
                'summary': 'Comparing whole units first, then tenths, then hundredths.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">To order <strong>1.4 m, 1.09 m, 1.45 m, 1.38 m</strong> from shortest to longest:</p>
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li>Pad 1.4 m with a trailing zero so all have 2 decimal places: <strong>1.40, 1.09, 1.45, 1.38</strong>.</li>
                    <li>Compare the hundredths after the dot (09, 38, 40, 45).</li>
                    <li>Ordered list: <strong>1.09 m, 1.38 m, 1.4 m, 1.45 m</strong>.</li>
                  </ol>
                </div>
                """
            },
            {
                'title': 'Rounding Decimals to the Nearest Whole Number or 1 Decimal Place',
                'summary': 'Using the decider digit to round prices and weights.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>To Nearest Whole Pound (&pound;1):</strong> Look at the tenths digit. &pound;14.62 &rarr; 6 is 5 or more &rarr; rounds UP to <strong>&pound;15.00</strong>.</li>
                    <li><strong>To 1 Decimal Place (Nearest 10p):</strong> Look at the hundredths digit. &pound;14.62 &rarr; 2 is less than 5 &rarr; rounds DOWN to <strong>&pound;14.60</strong>.</li>
                  </ul>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Care Home Tea Club Petty Cash Receipt & Change (Entry 3 / Level 1 Foundation)',
                'marks': '2 Marks (Entry Level 3 / Level 1)',
                'context': 'Activities Petty Cash Management',
                'question': 'A care home activity worker buys biscuits for <strong>£1.45</strong>, tea bags for <strong>£2.80</strong>, and milk for <strong>95p</strong>.<br>(a) Calculate the total cost in pounds (£).<br>(b) How much change will she receive from a <strong>£10.00 note</strong>?',
                'steps': [
                    ('Step 1', 'Convert 95p to £0.95 and add all three items', '£1.45 + £2.80 + £0.95 = £5.20.', 'M1: Converting 95p to £0.95 and adding (£5.20)'),
                    ('Step 2', 'Subtract £5.20 from £10.00', '£10.00 − £5.20 = £4.80.', 'A1: Accurate change (£4.80)')
                ],
                'final_answer': '(a) Total = £5.20 | (b) Change = £4.80',
                'tutor_tip': 'Always convert pence (95p) into pounds (£0.95) BEFORE adding to pound amounts!'
            },
            {
                'title': 'Hospital Staff Canteen Meal Deal Comparison (Level 1/2 Multi-Step)',
                'marks': '3 Marks (Pearson Edexcel Level 1/2)',
                'context': 'Workplace Catering Promotion',
                'question': 'A hospital canteen sells items individually:<br>• Sandwich: <strong>£2.65</strong> | Fruit Pot: <strong>£1.35</strong> | Bottled Water: <strong>85p</strong><br>• A "Healthy Shift Meal Deal" includes all three items for <strong>£4.20</strong>.<br>If a nurse buys this meal deal every shift for <strong>5 shifts</strong>, how much money does she save in total compared to buying the items separately?',
                'steps': [
                    ('Step 1', 'Convert 85p to £0.85 and sum the separate item prices', '£2.65 + £1.35 + £0.85 = £4.85 per day.', 'M1: Separate daily total (£4.85)'),
                    ('Step 2', 'Calculate daily saving with the £4.20 Meal Deal', '£4.85 − £4.20 = £0.65 (65p) saved per shift.', 'M1: Daily saving (£0.65)'),
                    ('Step 3', 'Multiply daily saving by 5 shifts', '5 × £0.65 = £3.25.', 'A1: Accurate 5-shift saving (£3.25)')
                ],
                'final_answer': '£3.25 saved over 5 shifts',
                'tutor_tip': 'Convert 85p to £0.85 first so you never add 85 whole pounds by mistake!'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Adding Pence Directly to Pounds (e.g. £2.65 + 85 = £87.65)',
                'desc': 'Failing to convert 85p into £0.85 before adding to £2.65.',
                'fix': 'Convert every pence figure into £0.XX before starting your calculation.'
            },
            {
                'title': 'Writing 5p as £0.5 Instead of £0.05',
                'desc': '£0.5 is £0.50 (50 pence)! Single-digit pence require a zero after the decimal point.',
                'fix': 'Remember: 10p = £0.10, while 1p = £0.01.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'Arrange these four parcel weights in ascending order (lightest to heaviest): <strong>2.4 kg, 2.08 kg, 2.45 kg, 2.39 kg</strong>.',
                'solution_steps': '1. Pad to 2 decimal places: 2.40, 2.08, 2.45, 2.39.<br>2. Order from smallest to largest: 2.08 kg, 2.39 kg, 2.4 kg, 2.45 kg.',
                'correct_answer': '2.08 kg, 2.39 kg, 2.4 kg, 2.45 kg',
                'tutor_tip': 'Writing 2.4 as 2.40 makes it easy to see that 2.39 is lighter than 2.40.'
            },
            {
                'marks': '2 Marks',
                'question': 'Round <strong>£27.46</strong>:<br>(a) To the nearest whole pound (£1).<br>(b) To 1 decimal place (nearest 10p).',
                'solution_steps': '1. Nearest £1: tenths digit is 4 (< 5), so it rounds down to £27.00.<br>2. Nearest 10p (1 dp): hundredths digit is 6 (≥ 5), so 4 tenths rounds up to 5 tenths → £27.50.',
                'correct_answer': '(a) £27.00 (or £27) | (b) £27.50 (or 27.5)',
                'tutor_tip': 'When rounding to the nearest £1, look only at the tenths digit (4), not the 6!'
            },
            {
                'marks': '3 Marks',
                'question': 'A receptionist buys <strong>3 packs of pens at £1.75 each</strong> and <strong>1 stapler for £3.40</strong>. How much change does he get from a <strong>£10.00 note</strong>?',
                'solution_steps': '1. Pens = 3 × £1.75 = £5.25.<br>2. Total spent = £5.25 + £3.40 = £8.65.<br>3. Change = £10.00 − £8.65 = £1.35.',
                'correct_answer': '£1.35',
                'tutor_tip': 'Check: £8.65 + £1.35 = £10.00.'
            }
        ]
    },
    {
        'filename': 'functional-skills-3d-shape-basics.html',
        'clean_topic': '3D Shape Basics: Cubes, Spheres & Cones',
        'intro_lead': 'Recognise and name common 3D solids in everyday healthcare and commercial environments, distinguish between 2D flat shapes and 3D solid objects, and identify flat vs curved surfaces.',
        'next_file': 'functional-skills-3d-shapes.html',
        'next_name': '3D Shapes',
        'spec_points': [
            ('E3.6 / L1.20', 'Recognise, name, and sort common 3D solids including cubes, cuboids, cylinders, cones, spheres, and pyramids.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-cube',
                'title': 'Golden Rule 1: Use 3D Names for Solids (Never Call a Cube a Square!)',
                'desc': '2D shapes are flat (Square, Rectangle, Circle, Triangle). 3D shapes have depth and volume (Cube, Cuboid, Sphere/Cylinder, Pyramid/Cone). Calling a cuboid box a "rectangle" loses the mark!',
                'badge': 'Flat 2D: Square, Rectangle, Circle • Solid 3D: Cube, Cuboid, Cylinder, Sphere'
            },
            {
                'icon': 'fa-shapes',
                'title': 'Golden Rule 2: Flat Faces Allow Stacking; Curved Surfaces Roll',
                'desc': 'Cubes and cuboids have 6 flat faces so they stack stably on warehouse pallets. Cylinders stack upright on their 2 flat circular ends, while spheres have 1 continuous curved surface and 0 flat faces.',
                'badge': 'Cylinder = 2 Flat Circular Ends + 1 Curved Wall • Sphere = 1 Curved Surface'
            }
        ],
        'skills': [
            {
                'title': 'Matching Everyday Workplace Objects to 3D Mathematical Names',
                'summary': 'Translating real-world packaging into formal exam terminology.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:left;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Everyday Workplace Object</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">3D Mathematical Name</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Key Surface Feature</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1;">Cardboard shipping carton / tissue box</td><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Cuboid</td><td style="padding:6px; border:1px solid #cbd5e1;">6 rectangular flat faces</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1;">Dice / equal-sided storage block</td><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Cube</td><td style="padding:6px; border:1px solid #cbd5e1;">6 identical square flat faces</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1;">Tin of soup / medical oxygen tank</td><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Cylinder</td><td style="padding:6px; border:1px solid #cbd5e1;">2 flat circles + 1 curved surface</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1;">Traffic bollard top / water cooler cup</td><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Cone</td><td style="padding:6px; border:1px solid #cbd5e1;">1 flat circle base + 1 apex point</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1;">Physiotherapy exercise ball</td><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Sphere</td><td style="padding:6px; border:1px solid #cbd5e1;">1 curved surface, 0 corners</td></tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                'title': 'Counting Faces, Edges & Vertices on Basic Solids',
                'summary': 'Quick visual counting rules for cubes, cuboids, cylinders, and cones.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Cube &amp; Cuboid:</strong> 6 flat faces, 12 straight edges, 8 corner vertices.</li>
                    <li><strong>Square-Based Pyramid:</strong> 1 square base + 4 triangular sides = <strong>5 faces, 8 edges, 5 vertices</strong>.</li>
                    <li><strong>Cylinder:</strong> 2 flat circular faces + 1 curved surface, 2 circular edges, <strong>0 vertices</strong>.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': '2D Footprints & Warehouse Pallet Stacking',
                'summary': 'How 3D cartons fit onto 2D shelf and pallet footprints.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">To find how many boxes fit on a shelf:</p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li>Divide the shelf length by the box length, divide the shelf width by the box width, and divide the shelf height by the box height.</li>
                    <li>Multiply the three whole numbers together: <strong>Boxes Along &times; Boxes Deep &times; Layers High</strong>.</li>
                  </ul>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Hospital Supply Equipment Packaging Shape Identification (Entry 3 / Level 1)',
                'marks': '3 Marks (Entry Level 3 / Level 1)',
                'context': 'Clinical Stores Inventory',
                'question': 'Give the correct mathematical 3D name for each of these three healthcare items:<br>(a) A roll of sterile surgical tape.<br>(b) A box of disposable nitrile gloves with rectangular sides.<br>(c) A pointed paper cup for a water dispenser.',
                'steps': [
                    ('Step 1', 'Identify shape of the surgical tape roll', 'Circular ends with straight sides = CYLINDER.', 'A1: Cylinder'),
                    ('Step 2', 'Identify shape of the rectangular glove box', 'Six rectangular faces = CUBOID.', 'A1: Cuboid'),
                    ('Step 3', 'Identify shape of the pointed paper cup', 'One circular opening tapering to a single point = CONE.', 'A1: Cone')
                ],
                'final_answer': '(a) Cylinder | (b) Cuboid | (c) Cone',
                'tutor_tip': 'Always write "Cuboid" rather than "box" or "rectangle".'
            },
            {
                'title': 'Pharmacy Shelf Stacking Capacity for Cuboid Medicine Boxes (Level 1/2 Multi-Step)',
                'marks': '3 Marks (Pearson Edexcel Level 1/2)',
                'context': 'Pharmacy Dispensary Shelving',
                'question': 'A pharmacy shelf space measures <strong>60 cm wide, 30 cm deep, and 24 cm high</strong>. A technician stacks cuboid medicine cartons that each measure <strong>12 cm wide, 10 cm deep, and 8 cm high</strong> (kept upright in the same orientation).<br>Calculate the maximum number of medicine cartons that will fit onto the shelf.',
                'steps': [
                    ('Step 1', 'Calculate how many cartons fit along the width and depth', 'Along width = 60 cm ÷ 12 cm = 5 cartons.<br>Along depth = 30 cm ÷ 10 cm = 3 cartons.', 'M1: Base layer counts (5 and 3)'),
                    ('Step 2', 'Calculate how many layers fit vertically in the 24 cm height', 'Layers high = 24 cm ÷ 8 cm = 3 layers.', 'M1: Vertical layer count (3)'),
                    ('Step 3', 'Multiply all three counts together', '5 × 3 × 3 = 45 cartons.', 'A1: Accurate total cartons (45)')
                ],
                'final_answer': '45 medicine cartons',
                'tutor_tip': 'Divide each dimension separately (5 × 3 × 3 = 45) so you are sure the boxes fit without cutting them!'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Writing 2D Names (Square, Circle, Rectangle) for 3D Objects',
                'desc': 'Calling a tin can a "circle" or a cardboard box a "rectangle" scores 0 marks.',
                'fix': 'Memorise: Circle → Cylinder/Sphere; Square → Cube; Rectangle → Cuboid.'
            },
            {
                'title': 'Confusing Cube and Cuboid',
                'desc': 'A cube has 6 identical square faces (all edges equal). If the length, width, and height are not all equal, it is a cuboid.',
                'fix': 'Check the dimensions: 10×10×10 is a Cube; 10×10×20 is a Cuboid.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'A container is shaped as a <strong>cylinder</strong>. State:<br>(a) How many flat faces and how many curved surfaces it has.<br>(b) What 2D shape its flat faces are.',
                'solution_steps': '1. A cylinder has 2 flat faces (top and bottom) and 1 curved surface.<br>2. The 2 flat faces are circles.',
                'correct_answer': '(a) 2 flat faces, 1 curved surface | (b) Circles',
                'tutor_tip': 'Think of a tin of beans: 2 flat circular ends and 1 curved label.'
            },
            {
                'marks': '2 Marks',
                'question': 'Which 3D solid has <strong>5 faces</strong> made up of <strong>1 square base and 4 triangles</strong> that meet at a top point?',
                'solution_steps': '1. A 4-sided square base with 4 triangular sides meeting at an apex is a Square-Based Pyramid.',
                'correct_answer': 'Square-based pyramid',
                'tutor_tip': 'Include "square-based" to distinguish it from a triangular pyramid.'
            },
            {
                'marks': '3 Marks',
                'question': 'A warehouse crate holds <strong>cube-shaped gift boxes</strong> of side length <strong>10 cm</strong>. The internal crate measures <strong>50 cm long, 40 cm wide, and 30 cm high</strong>. How many cube gift boxes can be packed inside the crate?',
                'solution_steps': '1. Along length = 50 ÷ 10 = 5.<br>2. Along width = 40 ÷ 10 = 4.<br>3. Layers high = 30 ÷ 10 = 3.<br>4. Total boxes = 5 × 4 × 3 = 60 boxes.',
                'correct_answer': '60 boxes',
                'tutor_tip': '5 along × 4 wide = 20 per layer; 3 layers × 20 = 60 boxes.'
            }
        ]
    },
    {
        'filename': 'functional-skills-scales.html',
        'clean_topic': 'Reading Gauges, Dials & Measuring Scales',
        'intro_lead': 'Read analogue and digital measuring scales with unnumbered division marks, calibrate medical weighing scales, and interpret pressure dials, syringes, and fuel gauges accurately.',
        'next_file': 'functional-skills-unit-conversions.html',
        'next_name': 'Unit Conversions',
        'spec_points': [
            ('L1.18 / L2.20', 'Read, estimate, and mark values on linear and circular measuring scales to the nearest labelled or unlabelled division.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-gauge',
                'title': 'Golden Rule 1: Value of 1 Small Division = (Gap Between Numbers) ÷ (Number of Spaces)',
                'desc': 'Never guess what each small tick mark is worth! Pick two adjacent numbered marks, subtract to find the gap, and divide by the number of SPACES (jumps) between them.',
                'badge': '1 Division = (Higher Number − Lower Number) ÷ Number of Spaces'
            },
            {
                'icon': 'fa-scale-balanced',
                'title': 'Golden Rule 2: Check the Units (kg vs g, L vs ml) Before Calculating',
                'desc': 'A scale marked 1, 2, 3 kg with 10 subdivisions has ticks worth 0.1 kg (= 100 g). Always check whether the question asks for the answer in kg or in grams!',
                'badge': '0.1 kg = 100 g • 0.1 L = 100 ml • Count SPACES, Not Tick Lines'
            }
        ],
        'skills': [
            {
                'title': 'The 4-Step Method for Unlabelled Scale Divisions',
                'summary': 'Counting spaces (jumps) rather than tick marks to avoid off-by-one errors.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Find two consecutive numbered marks:</strong> e.g. <strong>40</strong> and <strong>60</strong>.</li>
                    <li><strong>Subtract to find the gap:</strong> 60 &minus; 40 = <strong>20 units</strong>.</li>
                    <li><strong>Count the SPACES (jumps) from 40 to 60:</strong> e.g. <strong>4 spaces</strong> (which has 3 unnumbered tick lines inside).</li>
                    <li><strong>Divide Gap by Spaces:</strong> 20 &divide; 4 = <strong>5 units per division</strong> (40, 45, 50, 55, 60).</li>
                  </ol>
                </div>
                """
            },
            {
                'title': 'Common Scale Subdivisions Table (2, 4, 5, and 10 Spaces)',
                'summary': 'Instant recognition of standard dial and syringe intervals.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:center;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Major Jump</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Number of Spaces</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Value of 1 Small Division</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1;">100 units</td><td style="padding:6px; border:1px solid #cbd5e1;">5 spaces</td><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">20 units</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1;">100 units</td><td style="padding:6px; border:1px solid #cbd5e1;">4 spaces</td><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">25 units</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1;">10 units</td><td style="padding:6px; border:1px solid #cbd5e1;">5 spaces</td><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">2 units</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1;">1.0 kg (1,000 g)</td><td style="padding:6px; border:1px solid #cbd5e1;">5 spaces</td><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">0.2 kg (200 g)</td></tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                'title': 'Fractional Fuel Tank & Battery Gauges (1/8, 1/4, 1/2, 3/4, Full)',
                'summary': 'Converting needle positions on vehicle fuel dials into litres.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">Vehicle fuel gauges are usually split into <strong>8 equal subdivisions</strong> (each tick = 1/8 of a tank):</p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li>If a full tank holds <strong>64 litres</strong>, then 1 tick mark (1/8) = 64 &divide; 8 = <strong>8 litres</strong>.</li>
                    <li>If the needle rises from <strong>1/8 full to 7/8 full</strong>, you added 6/8 (3/4) of a tank = 6 &times; 8 L = <strong>48 litres</strong>.</li>
                  </ul>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Hospital Oxygen Cylinder Pressure Gauge Reading (Level 1 Foundation)',
                'marks': '3 Marks (Pearson Edexcel Level 1)',
                'context': 'Respiratory Ward Medical Gas Safety',
                'question': 'A ward oxygen cylinder pressure gauge has major numbered marks at <strong>100 bar and 150 bar</strong>, with <strong>10 equal spaces</strong> between them.<br>(a) What pressure does each small tick mark represent?<br>(b) The pointer sits <strong>7 small marks past 100 bar</strong>. What is the cylinder pressure, and is it above the minimum safe operating pressure of <strong>130 bar</strong>?',
                'steps': [
                    ('Step 1', 'Calculate value of 1 small division', '(150 − 100) ÷ 10 spaces = 50 ÷ 10 = 5 bar per mark.', 'M1 / A1: 5 bar per division'),
                    ('Step 2', 'Calculate pressure at 7 marks past 100 bar', '100 + (7 × 5) = 135 bar.', 'M1: Accurate reading (135 bar)'),
                    ('Step 3', 'Compare 135 bar with 130 bar safe minimum', 'Yes, 135 bar is above the 130 bar safe minimum.', 'A1: Valid comparison conclusion')
                ],
                'final_answer': '(a) 5 bar per mark | (b) 135 bar — Yes, above the 130 bar minimum',
                'tutor_tip': 'Count by 5s from 100 up to 150 to double-check your scale before reading the pointer.'
            },
            {
                'title': 'Ambulance Diesel Tank Gauge Refuelling Cost (Level 2 Multi-Step)',
                'marks': '4 Marks (Pearson Edexcel Level 2)',
                'context': 'Fleet Fuel Management',
                'question': 'An ambulance has a fuel tank capacity of <strong>80 litres</strong>. Its fuel gauge is divided into <strong>8 equal subdivisions</strong> from Empty (0) to Full (F).<br>• Before refuelling, the pointer is at <strong>1 subdivision above Empty</strong>.<br>• The driver pumps diesel until the pointer reaches <strong>7 subdivisions above Empty</strong>.<br>• Diesel costs <strong>145.9p per litre</strong>.<br>Calculate the total cost of the diesel added, rounded to the nearest penny.',
                'steps': [
                    ('Step 1', 'Calculate litres per subdivision (80 L ÷ 8)', '80 litres ÷ 8 subdivisions = 10 litres per subdivision.', 'M1: 10 litres per mark'),
                    ('Step 2', 'Calculate litres added from mark 1 to mark 7', 'Subdivisions added = 7 − 1 = 6 subdivisions.<br>Litres added = 6 × 10 L = 60 litres.', 'M1: 60 litres added'),
                    ('Step 3', 'Convert 145.9p to £1.459 and multiply by 60 litres', '60 × £1.459 = £87.54.', 'M1 / A1: Accurate fuel cost (£87.54)')
                ],
                'final_answer': '£87.54 (60 litres added)',
                'tutor_tip': 'Remember to convert 145.9p into £1.459 (divide by 100) so your final answer is in pounds and pence.'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Counting the Internal Tick Lines Instead of the Spaces',
                'desc': 'Between 0 and 100, if there are 3 internal lines, there are 4 SPACES (25 each). Dividing 100 by 3 gives 33.3 instead of 25!',
                'fix': 'Count the JUMPS from the first numbered line to the second numbered line.'
            },
            {
                'title': 'Assuming Every Small Mark Equals 1',
                'desc': 'Reading 3 marks past 20 as "23" when each mark actually represents 2 units (26) or 5 units (35).',
                'fix': 'Always write "1 mark = ..." before writing down your reading.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'A kitchen weighing scale has numbered marks at <strong>200 g and 400 g</strong>, with <strong>4 equal spaces</strong> between them. A parcel moves the pointer to <strong>3 marks past 200 g</strong>. What is the weight of the parcel?',
                'solution_steps': '1. 1 space = (400 − 200) ÷ 4 = 200 ÷ 4 = 50 g.<br>2. Weight = 200 g + (3 × 50 g) = 350 g.',
                'correct_answer': '350 g',
                'tutor_tip': 'Check: 200, 250, 300, 350, 400.'
            },
            {
                'marks': '2 Marks',
                'question': 'A clinical syringe is marked at <strong>1.0 ml and 2.0 ml</strong> with <strong>5 equal subdivisions</strong> between them. A nurse draws liquid up to <strong>4 subdivisions past 1.0 ml</strong>. How many ml of liquid are in the syringe?',
                'solution_steps': '1. 1 subdivision = (2.0 − 1.0) ÷ 5 = 0.2 ml.<br>2. Reading = 1.0 + (4 × 0.2) = 1.8 ml.',
                'correct_answer': '1.8 ml',
                'tutor_tip': 'With 5 spaces per whole unit, each tick mark is 0.2.'
            },
            {
                'marks': '3 Marks',
                'question': 'A boiler pressure dial has major marks at <strong>1.0 bar and 2.0 bar</strong> with <strong>4 equal spaces</strong> between them. Normal safe pressure is between <strong>1.2 bar and 1.8 bar</strong>. If the needle points exactly at <strong>3 marks past 1.0 bar</strong>, what is the pressure in bar and is the boiler within the safe range?',
                'solution_steps': '1. 1 space = (2.0 − 1.0) ÷ 4 = 0.25 bar.<br>2. Reading = 1.0 + (3 × 0.25) = 1.75 bar.<br>3. Since 1.75 bar is between 1.2 and 1.8 bar, YES, it is within the safe range.',
                'correct_answer': '1.75 bar; Yes, within the safe range (1.2 to 1.8 bar)',
                'tutor_tip': '1.0 ÷ 4 = 0.25 bar per mark.'
            }
        ]
    },
    {
        'filename': 'functional-skills-tally-charts.html',
        'clean_topic': 'Tally Charts & Frequency Tables',
        'intro_lead': 'Record raw survey data using 5-bar tally gates, convert tallies into numerical frequencies, verify grand totals, and analyse workplace feedback surveys.',
        'next_file': 'functional-skills-tables.html',
        'next_name': 'Data Tables',
        'spec_points': [
            ('E3.7 / L1.24', 'Record, organise, and interpret discrete categorical data using tally charts and frequency tables.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-bars',
                'title': 'Golden Rule 1: The Gate of 5 Tally System (4 Vertical + 1 Diagonal Slash)',
                'desc': 'Draw four upright lines |||| and cross the 5th line diagonally through them. Never draw 5 upright lines together—grouping in fives lets you count 5, 10, 15, 20 at a glance.',
                'badge': '1 Gate (<s>||||</s>) = 5 • Count in 5s, Then Add Loose Strokes'
            },
            {
                'icon': 'fa-check-double',
                'title': 'Golden Rule 2: Sum of Frequencies MUST Equal the Total Raw Data Count',
                'desc': 'Cross off each item in the raw list as you tally it. When finished, add up the Frequency column—if there were 30 items in the list, your frequencies must add up to 30!',
                'badge': 'Sum of Frequency Column = Total Items in Raw List'
            }
        ],
        'skills': [
            {
                'title': 'Converting Raw Data Lists into Tallies Without Missing Items',
                'summary': 'The cross-off-and-tally method for 100% accuracy.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li>Read the raw list from left to right, putting a neat slash through each word as you mark its tally stroke.</li>
                    <li>On every 5th mark in a row, draw the diagonal gate line.</li>
                    <li>Write the ordinary number (e.g. <strong>14</strong>) in the <strong>Frequency</strong> column.</li>
                  </ol>
                </div>
                """
            },
            {
                'title': 'Finding Missing Tallies & Frequencies from a Known Total',
                'summary': 'Working backwards when one row in a tally chart is torn or blank.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">If a survey of <strong>50 staff</strong> has four rows and the first three frequencies are <strong>16, 12, and 9</strong>:</p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li>Add known frequencies: 16 + 12 + 9 = <strong>37</strong>.</li>
                    <li>Subtract from 50: Missing frequency = 50 &minus; 37 = <strong>13</strong> (which is drawn as <strong>2 gates of 5 + 3 vertical lines</strong>: <s>||||</s> <s>||||</s> |||).</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Identifying the Mode & Proportions from a Tally Table',
                'summary': 'Answering follow-up analysis questions on tally charts.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Most Popular (Mode):</strong> The category name with the highest frequency.</li>
                    <li><strong>Fraction / Percentage of Total:</strong> Divide the category’s frequency by the Total Frequency.</li>
                  </ul>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Care Home Resident Lunch Menu Preference Tally (Entry 3 / Level 1 Foundation)',
                'marks': '3 Marks (Entry Level 3 / Level 1)',
                'context': 'Catering Service Quality Survey',
                'question': 'A catering assistant records lunch choices for <strong>40 residents</strong> in a tally chart:<br>• Roast Chicken: <strong><s>||||</s> <s>||||</s> <s>||||</s> |||</strong><br>• Fish &amp; Chips: <strong><s>||||</s> <s>||||</s> ||||</strong><br>• Vegetable Lasagne: <strong>?</strong><br>(a) Write the numerical frequencies for Roast Chicken and Fish &amp; Chips.<br>(b) Work out the frequency and tally for Vegetable Lasagne.',
                'steps': [
                    ('Step 1', 'Convert tallies to frequencies for Chicken and Fish', 'Roast Chicken = (3 × 5) + 3 = 18.<br>Fish & Chips = (2 × 5) + 4 = 14.', 'A1: Accurate frequencies (18 and 14)'),
                    ('Step 2', 'Subtract sum from 40 to find Vegetable Lasagne', '18 + 14 = 32.<br>Vegetable Lasagne = 40 − 32 = 8.', 'M1: Subtraction from 40 (8)'),
                    ('Step 3', 'Draw tally for 8', '1 gate of 5 plus 3 vertical lines: <s>||||</s> |||.', 'A1: Correct tally for 8')
                ],
                'final_answer': '(a) Chicken = 18, Fish = 14 | (b) Lasagne = 8 (<s>||||</s> |||)',
                'tutor_tip': 'Check: 18 + 14 + 8 = 40 residents.'
            },
            {
                'title': 'Outpatient Clinic Transport Survey & Car Park Space Planning (Level 1/2 Multi-Step)',
                'marks': '4 Marks (Pearson Edexcel Level 1/2)',
                'context': 'Hospital Travel Plan Audit',
                'question': 'An outpatient receptionist tallies how <strong>60 patients</strong> travelled to the clinic:<br>• Car: <strong><s>||||</s> <s>||||</s> <s>||||</s> <s>||||</s> <s>||||</s> ||</strong><br>• Bus: <strong><s>||||</s> <s>||||</s> <s>||||</s> |</strong><br>• Walk/Cycle: <strong><s>||||</s> <s>||||</s> ||</strong><br>• Taxi: <strong><s>||||</s></strong><br>(a) Find the frequency for each mode of transport and verify the total is 60.<br>(b) The hospital awards a green travel grant if <strong>at least 45%</strong> of patients travel by Bus or Walk/Cycle combined. Does the clinic qualify?',
                'steps': [
                    ('Step 1', 'Convert all four tallies to numbers and check sum', 'Car = 27 | Bus = 16 | Walk/Cycle = 12 | Taxi = 5.<br>Total = 27 + 16 + 12 + 5 = 60.', 'M1 / A1: All 4 frequencies accurate'),
                    ('Step 2', 'Combine Bus + Walk/Cycle frequencies', '16 + 12 = 28 patients.', 'M1: Combined green travel count (28)'),
                    ('Step 3', 'Calculate percentage of 60 and compare with 45%', '(28 ÷ 60) × 100 = 46.7%.<br>Yes, 46.7% is above the 45% threshold, so the clinic qualifies.', 'A1: 46.7% and valid Yes conclusion')
                ],
                'final_answer': '(a) Car: 27, Bus: 16, Walk/Cycle: 12, Taxi: 5 | (b) Yes, 46.7% used Bus or Walk/Cycle (> 45%)',
                'tutor_tip': 'Always convert every tally row into digits before doing percentage calculations.'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Drawing 5 Vertical Lines + 1 Slash (= 6) Instead of 4 Vertical Lines + 1 Slash (= 5)',
                'desc': 'Drawing ||||| and then crossing it makes 6 strokes instead of 5!',
                'fix': 'Chant: "1, 2, 3, 4, shut the gate on 5."'
            },
            {
                'title': 'Leaving the Frequency Column Blank',
                'desc': 'Completing the tally column but forgetting to write the numerical digits in the Frequency column loses 1 mark.',
                'fix': 'Check that both the Tally column and the Frequency column are filled in.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'A tally chart shows <strong><s>||||</s> <s>||||</s> <s>||||</s> <s>||||</s> ||||</strong> for PPE orders on Tuesday. What is the numerical frequency, and how many more orders are needed to reach <strong>30</strong>?',
                'solution_steps': '1. 4 gates of 5 + 4 strokes = 20 + 4 = 24.<br>2. Needed to reach 30: 30 − 24 = 6 more orders.',
                'correct_answer': 'Frequency = 24; 6 more orders needed',
                'tutor_tip': '4 × 5 = 20, plus 4 = 24.'
            },
            {
                'marks': '2 Marks',
                'question': 'How should a frequency of <strong>17</strong> be drawn as a tally?',
                'solution_steps': '1. 17 ÷ 5 = 3 full gates of 5 (15) with 2 remainder.<br>2. Tally: <s>||||</s> <s>||||</s> <s>||||</s> ||.',
                'correct_answer': '3 gates of 5 and 2 vertical strokes (<s>||||</s> <s>||||</s> <s>||||</s> ||)',
                'tutor_tip': '3 × 5 = 15, plus 2 = 17.'
            },
            {
                'marks': '3 Marks',
                'question': 'A staff satisfaction survey of <strong>50 employees</strong> records: <strong>Very Satisfied: 22, Satisfied: 19, Neutral: 6, Dissatisfied: ?</strong><br>Find the frequency for Dissatisfied and calculate what percentage of staff were either Very Satisfied or Satisfied.',
                'solution_steps': '1. Known sum = 22 + 19 + 6 = 47.<br>2. Dissatisfied = 50 − 47 = 3.<br>3. Very Satisfied + Satisfied = 22 + 19 = 41 out of 50 = 82%.',
                'correct_answer': 'Dissatisfied = 3; 82% were Very Satisfied or Satisfied',
                'tutor_tip': 'Out of 50, multiply by 2 to get a percentage out of 100 (41 × 2 = 82%).'
            }
        ]
    },
    {
        'filename': 'functional-skills-tables.html',
        'clean_topic': 'Data Tables & Information Retrieval',
        'intro_lead': 'Extract information from multi-column workplace tables, pricing matrices, bus and train timetables, and ward staffing rosters.',
        'next_file': 'functional-skills-data-tables.html',
        'next_name': 'Two-Way Data Tables',
        'spec_points': [
            ('E3.7 / L1.24', 'Extract, compare, and use numerical information from tables, price lists, and schedules.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-table',
                'title': 'Golden Rule 1: Check Header Units and Multipliers First (e.g. "in £000s" or "per 100")',
                'desc': 'Always read the table title, column headers, and footnotes before picking numbers! If a header says "Cost (£ per box of 50)", then ordering 100 items requires 2 boxes.',
                'badge': 'Read Row Header • Read Column Header • Check Footnotes & Units'
            },
            {
                'icon': 'fa-ruler',
                'title': 'Golden Rule 2: Trace Rows and Columns with a Straight Edge',
                'desc': 'In dense pricing or timetable grids, place your ruler horizontally under the target row so your eyes never slip onto the row above or below.',
                'badge': 'Intersect Target Row and Target Column Precisely'
            }
        ],
        'skills': [
            {
                'title': 'Two-Condition Pricing Matrices (Size × Delivery Speed)',
                'summary': 'Finding the exact charge where a weight band row meets a service level column.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:center;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Parcel Weight</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Standard (48h)</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Express (24h)</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Saturday Special</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Up to 2 kg</td><td style="padding:6px; border:1px solid #cbd5e1;">&pound;3.95</td><td style="padding:6px; border:1px solid #cbd5e1;">&pound;5.50</td><td style="padding:6px; border:1px solid #cbd5e1;">&pound;8.20</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">2.01 kg to 5 kg</td><td style="padding:6px; border:1px solid #cbd5e1;">&pound;5.40</td><td style="padding:6px; border:1px solid #cbd5e1; background:#dcfce7; font-weight:700;">&pound;7.25</td><td style="padding:6px; border:1px solid #cbd5e1;">&pound;10.50</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">5.01 kg to 10 kg</td><td style="padding:6px; border:1px solid #cbd5e1;">&pound;7.80</td><td style="padding:6px; border:1px solid #cbd5e1;">&pound;9.90</td><td style="padding:6px; border:1px solid #cbd5e1;">&pound;13.40</td></tr>
                    </tbody>
                  </table>
                  <p style="margin-top:8px; font-size:0.92rem; color:#334155;">Example: A <strong>3.6 kg</strong> parcel sent by <strong>Express (24h)</strong> sits in row 2, column 3 = <strong>&pound;7.25</strong>.</p>
                </div>
                """
            },
            {
                'title': 'Reading Bus, Train & Shift Timetables',
                'summary': 'Following a single vehicle down a column and calculating journey durations.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Each Column is One Bus/Train:</strong> Find the column that arrives at your destination <em>on or before</em> your appointment time, then read up that same column to find when it departs your starting station.</li>
                    <li><strong>Dash (—) in a Timetable:</strong> Means that specific bus or train does NOT stop at that station!</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Comparing Multi-Supplier Quotes from a Table',
                'summary': 'Including delivery charges and bulk discounts when comparing table rows.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">Never pick the supplier with the lowest unit price without checking the <strong>Delivery Fee</strong> column! Calculate <strong>(Quantity &times; Unit Price) + Delivery Fee</strong> for each row to prove which supplier is cheapest overall.</p>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Hospital Clinic Shift Cover Schedule Lookup (Entry 3 / Level 1 Foundation)',
                'marks': '2 Marks (Entry Level 3 / Level 1)',
                'context': 'Clinical Ward Operations',
                'question': 'A table shows nurse staffing across 3 hospital wards:<br>• Ward A: Morning <strong>6</strong>, Afternoon <strong>5</strong>, Night <strong>3</strong><br>• Ward B: Morning <strong>8</strong>, Afternoon <strong>6</strong>, Night <strong>4</strong><br>• Ward C: Morning <strong>5</strong>, Afternoon <strong>4</strong>, Night <strong>2</strong><br>(a) Which ward has the highest Afternoon staffing?<br>(b) What is the total number of Night nurses across all three wards?',
                'steps': [
                    ('Step 1', 'Compare the Afternoon numbers (5, 6, 4)', 'Highest is Ward B with 6 nurses.', 'A1: Ward B'),
                    ('Step 2', 'Sum the Night numbers (3 + 4 + 2)', '3 + 4 + 2 = 9 night nurses.', 'A1: 9 night nurses')
                ],
                'final_answer': '(a) Ward B (6 nurses) | (b) 9 night nurses',
                'tutor_tip': 'Circle the specific shift name (Afternoon / Night) before adding.'
            },
            {
                'title': 'Medical Equipment Supplier Table & Delivery Fee Comparison (Level 1/2 Multi-Step)',
                'marks': '4 Marks (Pearson Edexcel Level 1/2)',
                'context': 'GP Surgery Procurement',
                'question': 'A practice manager needs to order <strong>8 digital blood pressure monitors</strong>. Three suppliers quote in a table:<br>• <strong>MedEquip:</strong> £24.00 per monitor | Delivery: <strong>£12.00</strong><br>• <strong>HealthDirect:</strong> £25.50 per monitor | Delivery: <strong>Free on orders over £150</strong> (otherwise £15.00)<br>• <strong>CarePlus:</strong> £23.00 per monitor | Delivery: <strong>£22.00</strong><br>Calculate the total cost for each supplier and identify the cheapest option.',
                'steps': [
                    ('Step 1', 'Calculate MedEquip total for 8 monitors', '(8 × £24.00) + £12.00 = £192.00 + £12.00 = £204.00.', 'M1: MedEquip total (£204.00)'),
                    ('Step 2', 'Calculate HealthDirect total (checking free delivery threshold)', '8 × £25.50 = £204.00 (Over £150, so delivery is £0) → Total = £204.00.', 'M1: HealthDirect total (£204.00)'),
                    ('Step 3', 'Calculate CarePlus total and compare all three', '(8 × £23.00) + £22.00 = £184.00 + £22.00 = £206.00.<br>MedEquip and HealthDirect are tied as the cheapest at £204.00 each (£2.00 cheaper than CarePlus).', 'M1 / A1: CarePlus (£206.00) and correct comparison')
                ],
                'final_answer': 'MedEquip and HealthDirect are joint cheapest at £204.00 (CarePlus costs £206.00)',
                'tutor_tip': 'Notice that CarePlus had the cheapest monitor (£23), but its £22 delivery fee made it the most expensive overall!'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Ignoring Table Footnotes (e.g. "All prices exclude 20% VAT")',
                'desc': 'Missing a line below the table stating that delivery or VAT must be added.',
                'fix': 'Always read the small text directly underneath a table before starting your working.'
            },
            {
                'title': 'Picking a Bus That Arrives AFTER the Appointment Time',
                'desc': 'If an appointment is at 09:15 and buses arrive at 09:02 and 09:20, picking the 09:20 bus makes the passenger 5 minutes late!',
                'fix': 'You must arrive ON or BEFORE the appointment time (pick the 09:02 arrival).'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'Using the Parcel Weight table in Core Skill 1 above, calculate the total postage cost to send <strong>one 1.5 kg parcel by Standard (48h)</strong> and <strong>one 6.8 kg parcel by Saturday Special</strong>.',
                'solution_steps': '1. 1.5 kg (Up to 2 kg) Standard = £3.95.<br>2. 6.8 kg (5.01 to 10 kg) Saturday Special = £13.40.<br>3. Total = £3.95 + £13.40 = £17.35.',
                'correct_answer': '£17.35',
                'tutor_tip': 'Match each parcel weight to its correct row before reading across to the service column.'
            },
            {
                'marks': '3 Marks',
                'question': 'A hospital shuttle bus timetable shows:<br>• Bus 1: Departs Station <strong>07:45</strong> &rarr; Arrives Hospital <strong>08:18</strong><br>• Bus 2: Departs Station <strong>08:15</strong> &rarr; Arrives Hospital <strong>08:48</strong><br>• Bus 3: Departs Station <strong>08:40</strong> &rarr; Arrives Hospital <strong>09:13</strong><br>A nurse starts her shift at <strong>08:45</strong> and needs <strong>10 minutes</strong> to walk from the bus stop to her ward. Which is the latest bus she can catch, and what time does it depart the Station?',
                'solution_steps': '1. Latest arrival at Hospital bus stop = 08:45 − 10 mins = 08:35.<br>2. Bus 2 arrives at 08:48 (too late). She must catch Bus 1 (arrives 08:18).<br>3. Bus 1 departs Station at 07:45.',
                'correct_answer': 'Bus 1 (departs Station at 07:45)',
                'tutor_tip': 'Subtract the 10-minute walk from 08:45 first: she must arrive at the bus stop by 08:35.'
            },
            {
                'marks': '2 Marks',
                'question': 'In Question 2, how many minutes does the Bus 1 journey take from Station (07:45) to Hospital (08:18)?',
                'solution_steps': '1. From 07:45 to 08:00 = 15 minutes.<br>2. From 08:00 to 08:18 = 18 minutes.<br>3. Total = 15 + 18 = 33 minutes.',
                'correct_answer': '33 minutes',
                'tutor_tip': 'Bridge across the hour (08:00): 15 mins + 18 mins = 33 mins.'
            }
        ]
    },
    {
        'filename': 'functional-skills-lists.html',
        'clean_topic': 'Lists: Sorting & Information Extraction',
        'intro_lead': 'Sort lists alphabetically and numerically, filter records using multiple criteria (AND/OR conditions), and prioritize tasks in workplace handovers and dispatch manifests.',
        'next_file': 'functional-skills-tables.html',
        'next_name': 'Data Tables',
        'spec_points': [
            ('E3.7 / L1.24', 'Sort and organise lists alphabetically and numerically and filter records against multi-part criteria.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-arrow-down-a-z',
                'title': 'Golden Rule 1: Alphabetical Ordering: Compare 1st Letter → 2nd Letter → 3rd Letter',
                'desc': 'When words start with the same first letter, compare their second letters. If those match too, compare their third letters (e.g. Parker comes before Patel because r comes before t).',
                'badge': 'Compare 1st Letter → 2nd Letter → 3rd Letter (Shorter Word First: Hall before Halley)'
            },
            {
                'icon': 'fa-filter',
                'title': 'Golden Rule 2: Multi-Criteria Filtering — Cross Off Excluded Items One Rule at a Time',
                'desc': 'When a question gives 3 requirements (e.g. "Must be available on Friday, hold a First Aid certificate, and cost under £150"), apply Rule 1 and cross out failures, then Rule 2, then Rule 3.',
                'badge': 'Eliminate Rule by Rule Until Only Matching Candidates Remain'
            }
        ],
        'skills': [
            {
                'title': 'Alphabetical Filing Rules for Surnames & Codes',
                'summary': 'Sorting patient records and stock codes accurately.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Identical Surnames:</strong> Sort by Surname first; if two people share the same Surname (e.g. <em>Smith, David</em> and <em>Smith, Alice</em>), compare their First Names (<em>Smith, Alice</em> comes first).</li>
                    <li><strong>Alphanumeric Stock Codes:</strong> Sort the letters alphabetically first, then sort the numbers by numerical size (e.g. <strong>AB-104, AB-210, AC-050</strong>).</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Chronological Date & Time Sorting',
                'summary': 'Ordering expiry dates, appointments, and birthdates from earliest to latest.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">To sort dates in chronological order (earliest first), compare in this exact order:</p>
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Year first</strong> (e.g. 2025 before 2026)</li>
                    <li><strong>Month second</strong> (e.g. 03/2026 before 08/2026)</li>
                    <li><strong>Day third</strong> (e.g. 05/03/2026 before 19/03/2026)</li>
                  </ol>
                </div>
                """
            },
            {
                'title': 'Filtering Lists with Multiple Workplace Constraints',
                'summary': 'Selecting the right room, vehicle, or staff member from a specification list.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">Use a tick/cross checklist for each item against every constraint in the question so you can justify your choice clearly.</p>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Patient Medical Records Alphabetical Filing (Entry 3 / Level 1 Foundation)',
                'marks': '2 Marks (Entry Level 3 / Level 1)',
                'context': 'Health Records Management',
                'question': 'Arrange these five patient surnames in alphabetical order (A to Z):<br><strong>Patel, Parker, Phillips, Price, Pearce</strong>',
                'steps': [
                    ('Step 1', 'Group by 2nd letter (Pa, Pe, Ph, Pr)', 'Pa: Parker, Patel | Pe: Pearce | Ph: Phillips | Pr: Price.', 'M1: Grouping by second letter'),
                    ('Step 2', 'Compare 3rd letter of Parker (r) vs Patel (t)', 'r comes before t → Parker, Patel, Pearce, Phillips, Price.', 'A1: Exact alphabetical order')
                ],
                'final_answer': 'Parker, Patel, Pearce, Phillips, Price',
                'tutor_tip': 'Write down the 2nd and 3rd letters above each name to avoid slips.'
            },
            {
                'title': 'Conference Venue Multi-Criteria Filtering & Costing (Level 1/2 Multi-Step)',
                'marks': '4 Marks (Pearson Edexcel Level 1/2)',
                'context': 'NHS Training Day Venue Selection',
                'question': 'A training coordinator needs a venue for <strong>45 delegates</strong> that has <strong>Wheelchair Access</strong>, includes <strong>Free Parking</strong>, and costs <strong>under £900 in total</strong> (Room Hire + Catering at £12 per delegate):<br>• <strong>Hall A:</strong> Capacity 60 | Wheelchair: Yes | Parking: Free | Room Hire: <strong>£320</strong><br>• <strong>Hall B:</strong> Capacity 40 | Wheelchair: Yes | Parking: Free | Room Hire: <strong>£250</strong><br>• <strong>Hall C:</strong> Capacity 50 | Wheelchair: Yes | Parking: Paid (£5) | Room Hire: <strong>£280</strong><br>• <strong>Hall D:</strong> Capacity 55 | Wheelchair: Yes | Parking: Free | Room Hire: <strong>£390</strong><br>Identify which hall meets all criteria and state its total cost.',
                'steps': [
                    ('Step 1', 'Eliminate venues failing capacity or parking criteria', 'Hall B fails capacity (40 < 45 delegates).<br>Hall C fails Free Parking.', 'M1: Eliminating Halls B and C'),
                    ('Step 2', 'Calculate catering cost for 45 delegates at £12 each', '45 × £12 = £540 catering cost.', 'M1: Catering cost (£540)'),
                    ('Step 3', 'Check total cost for Hall A and Hall D against £900 limit', 'Hall A Total = £320 + £540 = £860 (< £900 — Passes).<br>Hall D Total = £390 + £540 = £930 (> £900 — Fails).<br>Select Hall A at £860.', 'M1 / A1: Hall A selected with £860 total')
                ],
                'final_answer': 'Hall A (Total cost = £860, meeting all criteria)',
                'tutor_tip': 'State clearly why each rejected option failed so you earn full process marks.'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Sorting Dates by the Day Number Instead of Year/Month First',
                'desc': 'Putting 02/11/2026 before 18/04/2026 because 02 is smaller than 18!',
                'fix': 'Always compare Year first, then Month (April = 04 comes before November = 11), then Day.'
            },
            {
                'title': 'Missing One Constraint in a Multi-Criteria Question',
                'desc': 'Picking Hall B because it is the cheapest without noticing its capacity is only 40 (< 45 needed).',
                'fix': 'Underline every single requirement in the question stem before checking the list.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'Arrange these five delivery towns in alphabetical order: <strong>Bolton, Bradford, Bristol, Bath, Barnsley</strong>.',
                'solution_steps': '1. Ba comes before Bo and Br: Barnsley (Bar) vs Bath (Bat) → r before t → Barnsley, Bath.<br>2. Bo: Bolton.<br>3. Br: Bradford (Bra) vs Bristol (Bri) → Bradford, Bristol.<br>4. Full order: Barnsley, Bath, Bolton, Bradford, Bristol.',
                'correct_answer': 'Barnsley, Bath, Bolton, Bradford, Bristol',
                'tutor_tip': 'Compare the 3rd letters for Barnsley (r) and Bath (t).'
            },
            {
                'marks': '2 Marks',
                'question': 'A pharmacy technician checks four medicine batch expiry dates so the earliest expiry is used first (FEFO): <strong>14/09/2026, 28/03/2026, 05/12/2025, 19/03/2026</strong>. List them from earliest to latest.',
                'solution_steps': '1. 2025 comes first: 05/12/2025.<br>2. March 2026 (03/2026): 19/03/2026 then 28/03/2026.<br>3. September 2026: 14/09/2026.',
                'correct_answer': '05/12/2025, 19/03/2026, 28/03/2026, 14/09/2026',
                'tutor_tip': 'Sort by Year (2025 before 2026), then Month (03 before 09), then Day (19 before 28).'
            },
            {
                'marks': '2 Marks',
                'question': 'From this list of staff: <strong> Ali (Band 5, Night, First Aid), Ben (Band 6, Day, First Aid), Cara (Band 6, Night, No First Aid), Dan (Band 6, Night, First Aid)</strong> — who meets ALL three rules: <strong>Band 6, Night Shift, and First Aid qualified</strong>?',
                'solution_steps': '1. Ali is Band 5 (Eliminated).<br>2. Ben is Day Shift (Eliminated).<br>3. Cara has No First Aid (Eliminated).<br>4. Dan meets all three criteria.',
                'correct_answer': 'Dan',
                'tutor_tip': 'Cross off candidates who fail any one of the three rules.'
            }
        ]
    },
    {
        'filename': 'functional-skills-movement-and-direction.html',
        'clean_topic': 'Movement, Direction & Compass Bearings',
        'intro_lead': 'Navigate workplace floor plans using 8-point compass directions (N, NE, E, SE, S, SW, W, NW), execute quarter, half, and three-quarter turns clockwise and anti-clockwise, and write grid route instructions.',
        'next_file': 'functional-skills-angles.html',
        'next_name': 'Angles & Bearings',
        'spec_points': [
            ('E3.8 / L1.21', 'Use cardinal and intercardinal compass directions and turns (quarter/90°, half/180°, three-quarter/270°, full/360°) to describe movement and position.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-compass',
                'title': 'Golden Rule 1: Never Eat Shredded Wheat (Clockwise N → E → S → W)',
                'desc': 'North is at the top (0°), East is to the right (90°), South is at the bottom (180°), and West is to the left (270°). Clockwise follows the hands of a clock (N → E → S → W); Anti-clockwise goes backwards (N → W → S → E).',
                'badge': 'Clockwise: N → E → S → W • Anti-Clockwise: N → W → S → E'
            },
            {
                'icon': 'fa-rotate',
                'title': 'Golden Rule 2: 1/4 Turn = 90° • 1/2 Turn = 180° • 3/4 Turn = 270°',
                'desc': 'A quarter turn is 1 main compass step (90° right angle). A half turn (180°) always faces the exact opposite direction regardless of whether you turn clockwise or anti-clockwise!',
                'badge': '1/4 Turn = 90° • 1/2 Turn = 180° (Opposite) • 3/4 Turn = 270°'
            }
        ],
        'skills': [
            {
                'title': 'The 8-Point Compass & Opposite Directions',
                'summary': 'Cardinal and intercardinal directions and their 180° opposites.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>North (N) &harr; South (S)</strong> are exact opposites (180° apart).</li>
                    <li><strong>East (E) &harr; West (W)</strong> are exact opposites (180° apart).</li>
                    <li><strong>North-East (NE) &harr; South-West (SW)</strong> are exact opposites.</li>
                    <li><strong>North-West (NW) &harr; South-East (SE)</strong> are exact opposites.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Left/Right Turns vs Compass Directions',
                'summary': 'Why "Turn Right" depends on which way you are currently facing!',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;"><strong>Crucial Distinction:</strong></p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Turning Right = 90° Clockwise</strong> from your current heading (e.g. if walking <strong>South</strong> and you turn <strong>Right</strong>, you are now facing <strong>West</strong>!).</li>
                    <li><strong>Turning Left = 90° Anti-Clockwise</strong> from your current heading (e.g. if walking <strong>South</strong> and you turn <strong>Left</strong>, you are now facing <strong>East</strong>!).</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Following & Reversing Grid Route Instructions',
                'summary': 'Tracing warehouse AGV paths and reversing directions for the return journey.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">To reverse a journey from B back to A, invert both the order of steps AND every direction (North becomes South, East becomes West, Left becomes Right).</p>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Hospital Emergency Evacuation Route Direction (Entry 3 / Level 1 Foundation)',
                'marks': '2 Marks (Entry Level 3 / Level 1)',
                'context': 'Facility Fire Safety Navigation',
                'question': 'A hospital porter is pushing a wheelchair facing <strong>North</strong> down Main Corridor. At the junction, she turns <strong>a quarter turn (90°) clockwise</strong>, walks 30 metres, then turns <strong>a three-quarter turn (270°) clockwise</strong>.<br>(a) In which compass direction is she facing after the first turn?<br>(b) In which compass direction is she facing after the second turn?',
                'steps': [
                    ('Step 1', 'Quarter turn (90°) clockwise from North', 'North + 90° clockwise = EAST.', 'A1: East'),
                    ('Step 2', 'Three-quarter turn (270°) clockwise from East', 'From East: 1/4 = South, 2/4 = West, 3/4 = NORTH.', 'A1: North')
                ],
                'final_answer': '(a) East | (b) North',
                'tutor_tip': 'A 3/4 turn clockwise is the exact same final position as a 1/4 turn anti-clockwise!'
            },
            {
                'title': 'Warehouse Forklift Grid Navigation & Net Displacement (Level 1/2 Multi-Step)',
                'marks': '3 Marks (Pearson Edexcel Level 1/2)',
                'context': 'Logistics Warehouse Floor Grid',
                'question': 'On a warehouse floor grid where <strong>1 square = 5 metres</strong>, a forklift starts at Loading Bay S and follows these instructions:<br>1. Drive <strong>6 squares North</strong>.<br>2. Turn 90° clockwise and drive <strong>4 squares</strong>.<br>3. Turn 90° clockwise and drive <strong>2 squares</strong>.<br>(a) How many metres in total has the forklift driven?<br>(b) How many squares North and how many squares East is the forklift from its starting point S?',
                'steps': [
                    ('Step 1', 'Sum total squares driven and multiply by 5 metres', 'Total squares = 6 + 4 + 2 = 12 squares.<br>Total distance = 12 × 5 m = 60 metres.', 'M1 / A1: 60 metres driven'),
                    ('Step 2', 'Track net North/South and East/West position', 'Step 1 goes 6 North; Step 2 goes 4 East; Step 3 turns clockwise from East to go 2 South.<br>Net North = 6 − 2 = 4 squares North; Net East = 4 squares East.', 'A1: 4 squares North and 4 squares East')
                ],
                'final_answer': '(a) 60 metres total driven | (b) 4 squares North and 4 squares East of S',
                'tutor_tip': 'Sketch the path on scrap grid paper with arrows so you can see that the third leg goes South.'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Assuming "Turn Right" Always Means East',
                'desc': 'If a person is walking South down a map and turns Right, they turn towards the West (left side of the page), NOT East!',
                'fix': 'Imagine yourself standing in the person’s shoes facing their direction before turning left or right.'
            },
            {
                'title': 'Confusing Clockwise with Anti-Clockwise',
                'desc': 'Turning West from North when asked to turn clockwise.',
                'fix': 'Draw a small clock face: 12 → 3 → 6 → 9 is Clockwise (N → E → S → W).'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'You are facing <strong>South-East (SE)</strong>. You make a <strong>half turn (180°)</strong>. Which compass direction are you now facing?',
                'solution_steps': '1. A half turn (180°) points in the exact opposite direction.<br>2. The opposite of South-East (SE) is North-West (NW).',
                'correct_answer': 'North-West (NW)',
                'tutor_tip': 'Swap both words: South becomes North, East becomes West → North-West!'
            },
            {
                'marks': '2 Marks',
                'question': 'A security guard is facing <strong>West</strong>. Through how many degrees <strong>clockwise</strong> must he turn to face <strong>South</strong>?',
                'solution_steps': '1. Clockwise from West (270°): West → North (90°) → East (180°) → South (270°).<br>2. Angle = 270° clockwise (a three-quarter turn).',
                'correct_answer': '270°',
                'tutor_tip': 'Going clockwise from West to South passes through North and East (3 quarter turns = 270°).'
            },
            {
                'marks': '3 Marks',
                'question': 'A delivery driver leaves the depot, drives <strong>3.5 km East</strong>, turns <strong>left (90° anti-clockwise)</strong> and drives <strong>2.0 km</strong>, then turns <strong>left again</strong> and drives <strong>3.5 km</strong>. In which compass direction is she now facing, and how far is she directly from the depot?',
                'solution_steps': '1. Starts East → turns left to face North (2.0 km) → turns left to face West (3.5 km).<br>2. The 3.5 km West cancels out the 3.5 km East, leaving her exactly 2.0 km North of the depot.',
                'correct_answer': 'Facing West; 2.0 km North of the depot',
                'tutor_tip': 'Draw the 3 sides of the rectangle: 3.5 km East, 2.0 km North, 3.5 km West.'
            }
        ]
    },
    {
        'filename': 'functional-skills-using-length-area-and-volume-in-calculations.html',
        'clean_topic': 'Multi-Step Spatial Calculations: Area & Volume',
        'intro_lead': 'Combine measurements of length, compound area, 3D volume, unit conversions (cm to m, m³ to litres), percentage wastage, and pack pricing to solve 5-mark and 6-mark exam problems.',
        'next_file': 'functional-skills-maths-level-2.html',
        'next_name': 'Maths Level 2 Directory',
        'spec_points': [
            ('L1.22 / L2.24', 'Solve multi-stage problems combining perimeter, compound area, surface area, and volume with unit conversions, wastage percentages, and financial costing.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-layer-group',
                'title': 'Golden Rule 1: Unify All Units FIRST Before Multiplying for Area or Volume',
                'desc': 'Never multiply metres by centimetres or millimetres! If a driveway is 8 m long, 3.5 m wide, and 5 cm deep, convert 5 cm into 0.05 m FIRST before calculating Volume = 8 × 3.5 × 0.05 = 1.4 m³.',
                'badge': 'Convert All Dimensions to the SAME Unit Before Multiplying!'
            },
            {
                'icon': 'fa-percent',
                'title': 'Golden Rule 2: Add Percentage Wastage BEFORE Dividing by Pack Coverage, Then Round UP',
                'desc': 'In construction and flooring questions: 1. Calculate Area/Volume. 2. Add wastage (e.g. × 1.10 for 10%). 3. Divide by pack coverage. 4. Always round UP to the next whole pack/bag/tin.',
                'badge': 'Area/Volume → Add Wastage → Divide by Pack Size → Round UP → × Price'
            }
        ],
        'skills': [
            {
                'title': 'The 5-Stage Construction & Renovation Costing Pipeline',
                'summary': 'How to structure 5-mark and 6-mark spatial costing questions.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Unify Units:</strong> Convert all cm/mm into metres (e.g. 50 cm = 0.5 m; 80 mm = 0.08 m).</li>
                    <li><strong>Calculate Area or Volume:</strong> Split compound shapes or multiply L &times; W &times; Depth.</li>
                    <li><strong>Add Wastage / Multiple Coats:</strong> Multiply by 1.10 (for +10% wastage) or &times; 2 (for 2 coats).</li>
                    <li><strong>Find Whole Packs Needed:</strong> Divide by coverage per pack and <strong>round UP to the next whole integer</strong>.</li>
                    <li><strong>Calculate Total Cost (+ VAT/Discount):</strong> Whole Packs &times; Price per Pack.</li>
                  </ol>
                </div>
                """
            },
            {
                'title': 'Volume-to-Capacity Bridges (cm³ ↔ Litres ↔ m³) & Flow Rates',
                'summary': 'The three essential 3D volume-to-liquid capacity conversions.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:center;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">3D Cubic Volume</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Liquid Capacity Equivalent</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Conversion Rule</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">1 cm&sup3;</td><td style="padding:6px; border:1px solid #cbd5e1;">1 ml</td><td style="padding:6px; border:1px solid #cbd5e1;">1 : 1 identical</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">1,000 cm&sup3;</td><td style="padding:6px; border:1px solid #cbd5e1;">1 Litre (1,000 ml)</td><td style="padding:6px; border:1px solid #cbd5e1;">Litres = cm&sup3; &divide; 1,000</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">1 m&sup3;</td><td style="padding:6px; border:1px solid #cbd5e1;">1,000 Litres</td><td style="padding:6px; border:1px solid #cbd5e1;">Litres = m&sup3; &times; 1,000</td></tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                'title': 'Mass, Density & Gravel/Concrete Tonnage Calculations',
                'summary': 'Converting cubic metres of soil, sand, or concrete into tonnes and skip bags.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">Once you know the volume in <strong>m&sup3;</strong>, multiply by the material density (e.g. <strong>1 m&sup3; of gravel weighs 1.6 tonnes</strong>):</p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Total Weight = Volume (m&sup3;) &times; Weight per m&sup3;</strong>.</li>
                  </ul>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Hospital Consultation Room Vinyl Flooring Installation (Level 2 Core)',
                'marks': '4 Marks (Pearson Edexcel Level 2)',
                'context': 'Healthcare Facility Renovation',
                'question': 'A clinical consultation room floor measures <strong>6.0 m long by 4.0 m wide</strong>. Non-slip vinyl tiles are sold in packs:<br>• Each pack covers <strong>2.5 m²</strong> and costs <strong>£28.50</strong>.<br>• The installer adds <strong>10% extra area</strong> for cutting wastage.<br>Calculate the total cost of the packs required to tile the room.',
                'steps': [
                    ('Step 1', 'Calculate floor area', '6.0 m × 4.0 m = 24.0 m².', 'M1: Floor area (24.0 m²)'),
                    ('Step 2', 'Add 10% cutting wastage', '24.0 m² × 1.10 = 26.4 m².', 'M1: Area including wastage (26.4 m²)'),
                    ('Step 3', 'Divide by 2.5 m² pack coverage and round UP', '26.4 ÷ 2.5 = 10.56 packs → Round UP to 11 whole packs.', 'A1: 11 packs'),
                    ('Step 4', 'Calculate total cost', '11 packs × £28.50 = £313.50.', 'A1: Accurate total cost (£313.50)')
                ],
                'final_answer': '£313.50 (11 packs required)',
                'tutor_tip': 'Always round packs UP (10.56 → 11 packs) so you do not leave 1.4 m² of floor bare!'
            },
            {
                'title': 'Car Park Gravel Resurfacing Depth, Tonnage & Bulk Bag Costing (Level 2 Multi-Step)',
                'marks': '5 Marks (Pearson Edexcel Level 2)',
                'context': 'Civil Engineering & Grounds Maintenance',
                'question': 'A clinic resurfaces a rectangular overflow car park measuring <strong>15 m long by 8 m wide</strong> with gravel laid to an even depth of <strong>6 cm</strong>.<br>• <strong>1 m³ of gravel weighs 1.6 tonnes</strong>.<br>• Gravel is sold in <strong>0.8-tonne bulk bags</strong> costing <strong>£64.00 per bag</strong>.<br>Calculate the total cost of the bulk bags required.',
                'steps': [
                    ('Step 1', 'Convert 6 cm depth into metres (÷ 100)', '6 cm = 0.06 m.', 'B1: Depth conversion (0.06 m)'),
                    ('Step 2', 'Calculate volume of gravel in m³', 'Volume = 15 m × 8 m × 0.06 m = 7.2 m³.', 'M1: Accurate volume (7.2 m³)'),
                    ('Step 3', 'Multiply volume by 1.6 tonnes per m³', 'Total weight = 7.2 × 1.6 = 11.52 tonnes.', 'M1: Total weight (11.52 tonnes)'),
                    ('Step 4', 'Divide by 0.8 tonnes per bag and round UP', '11.52 ÷ 0.8 = 14.4 bags → Round UP to 15 bags.', 'M1: 15 whole bags'),
                    ('Step 5', 'Multiply 15 bags by £64.00', '15 × £64.00 = £960.00.', 'A1: Accurate total cost (£960.00)')
                ],
                'final_answer': '£960.00 (15 bulk bags required for 11.52 tonnes / 7.2 m³)',
                'tutor_tip': 'Converting 6 cm to 0.06 m at Step 1 prevents the fatal error of calculating 15 × 8 × 6 = 720 m³!'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Multiplying Metres by Centimetres Without Converting First',
                'desc': 'Computing 15 m × 8 m × 6 cm = 720 m³ is 100 times too big!',
                'fix': 'Convert cm to m (÷ 100) before multiplying.'
            },
            {
                'title': 'Rounding Material Packs or Bags Down',
                'desc': 'Rounding 14.4 bags down to 14 bags leaves the job unfinished.',
                'fix': 'In construction and decorating, even .01 of a pack requires buying the next full pack.'
            }
        ],
        'practice_questions': [
            {
                'marks': '3 Marks',
                'question': 'A rectangular concrete base measures <strong>5.0 m long, 4.0 m wide, and 15 cm deep</strong>. Calculate the volume of concrete required in <strong>cubic metres (m³)</strong>.',
                'solution_steps': '1. Convert 15 cm to metres: 15 ÷ 100 = 0.15 m.<br>2. Volume = 5.0 × 4.0 × 0.15 = 3.0 m³.',
                'correct_answer': '3.0 m³ (or 3 m³)',
                'tutor_tip': '15 cm = 0.15 m; 20 m² × 0.15 m = 3.0 m³.'
            },
            {
                'marks': '3 Marks',
                'question': 'A rectangular fish tank measures <strong>80 cm long, 40 cm wide, and 50 cm high</strong>. It is filled with water to <strong>90% of its height</strong>. How many <strong>litres</strong> of water are in the tank? (1,000 cm³ = 1 litre).',
                'solution_steps': '1. Water height = 90% of 50 cm = 45 cm.<br>2. Water volume = 80 × 40 × 45 = 144,000 cm³.<br>3. Convert to litres: 144,000 ÷ 1,000 = 144 litres.',
                'correct_answer': '144 litres',
                'tutor_tip': 'Divide cm³ by 1,000 to convert directly into litres.'
            },
            {
                'marks': '4 Marks',
                'question': 'A painter needs to paint a wall measuring <strong>8.5 m long by 2.8 m high</strong> with <strong>2 coats of paint</strong>. One tin of paint covers <strong>12 m²</strong> and costs <strong>£21.50</strong>. Calculate the total cost of the paint tins required.',
                'solution_steps': '1. Wall area = 8.5 × 2.8 = 23.8 m².<br>2. Area for 2 coats = 23.8 × 2 = 47.6 m².<br>3. Tins needed = 47.6 ÷ 12 = 3.966... → Round UP to 4 tins.<br>4. Total cost = 4 × £21.50 = £86.00.',
                'correct_answer': '£86.00 (4 tins)',
                'tutor_tip': 'Remember to double the wall area for 2 coats before dividing by 12 m²!'
            }
        ]
    },
    {
        'filename': 'functional-skills-angles-and-bearings.html',
        'clean_topic': 'Angles, Bearings & Turn Navigation',
        'intro_lead': 'Measure and calculate angles on straight lines, around a point, and vertically opposite angles, and calculate 3-figure compass bearings, back bearings, and scaled radar vectors.',
        'next_file': 'functional-skills-angles-in-2d-shapes.html',
        'next_name': 'Angles in Polygons',
        'spec_points': [
            ('L1.21 / L2.23', 'Measure and calculate angles in degrees on straight lines (180°) and around a point (360°).'),
            ('L2.23', 'Use 3-figure bearings measured clockwise from North and combine bearings with scale drawings.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-compass',
                'title': 'Golden Rule 1: Three Rules of Three-Figure Bearings (North • Clockwise • 3 Digits)',
                'desc': '1. Always start pointing NORTH (000°). 2. Always measure CLOCKWISE. 3. Always write as THREE FIGURES (e.g. 045°, 008°, 230°).',
                'badge': 'From North (000°) • Clockwise • 3 Figures (e.g. 075°)'
            },
            {
                'icon': 'fa-lines-leaning',
                'title': 'Golden Rule 2: Reverse (Back) Bearing = Add or Subtract 180°',
                'desc': 'To find the return bearing from B back to A: if the outward bearing is less than 180°, ADD 180°. If the outward bearing is greater than 180°, SUBTRACT 180° (and pad with a leading zero if under 100°).',
                'badge': 'Outward < 180° → +180° • Outward > 180° → −180°'
            }
        ],
        'skills': [
            {
                'title': 'Angles on a Straight Line (180°), Around a Point (360°) & Vertically Opposite',
                'summary': 'Core deductive angle laws for workplace junctions and security sweeps.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Angles on a Straight Line:</strong> Sum to <strong>180°</strong>.</li>
                    <li><strong>Angles Around a Full Point:</strong> Sum to <strong>360°</strong>.</li>
                    <li><strong>Right Angle Split:</strong> Angles inside a perpendicular corner sum to <strong>90°</strong>.</li>
                    <li><strong>Vertically Opposite Angles:</strong> Where two straight lines cross, opposite angles are equal.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Measuring Bearings Clockwise from North (Including Westward Reflex Angles)',
                'summary': 'Converting anti-clockwise angles West of North into 3-figure clockwise bearings.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">If a diagram shows an angle of <strong>55° anti-clockwise (West) from North</strong>:</p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li>Because bearings MUST be measured clockwise from North, subtract 55° from a full 360° circle: 360° &minus; 55° = <strong>305°</strong>.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Combining Bearings with Map Scale Ratios',
                'summary': 'Plotting a target location using a protractor bearing and a ruler scale distance.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Step 1 — Angle:</strong> Place your protractor center on the starting town with 000° aligned on the North arrow, and mark the bearing clockwise.</li>
                    <li><strong>Step 2 — Distance:</strong> Convert the real distance into cm using the map scale (e.g. 12 km at 1 cm : 2 km = <strong>6 cm</strong>) and rule the line to that exact length.</li>
                  </ol>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Air Ambulance Flight Navigation & Return Bearing (Level 1/2 Foundation)',
                'marks': '3 Marks (Pearson Edexcel Level 1/2)',
                'context': 'Emergency Medical Helicopter Dispatch',
                'question': 'An emergency transfer helicopter flies from Helipad H on a bearing of <strong>074°</strong> to an accident site A.<br>(a) State whether 074° is an acute, right, obtuse, or reflex angle.<br>(b) Calculate the 3-figure back bearing required to fly from accident site A back to Helipad H.',
                'steps': [
                    ('Step 1', 'Classify 074°', 'Since 074° is between 0° and 90°, it is an ACUTE angle.', 'A1: Acute angle'),
                    ('Step 2', 'Add 180° for the reverse bearing', '074° + 180° = 254°.', 'M1 / A1: Return bearing = 254°')
                ],
                'final_answer': '(a) Acute angle | (b) 254°',
                'tutor_tip': 'Always write bearings with 3 figures (074° and 254°).'
            },
            {
                'title': 'Offshore Wind Farm Service Vessel Bearing & Scale Plot (Level 2 Multi-Step)',
                'marks': '4 Marks (Pearson Edexcel Level 2)',
                'context': 'Maritime Engineering Navigation',
                'question': 'A maintenance vessel sails from Harbour P to Turbine T. The angle measured <strong>anti-clockwise (West) from North is 65°</strong>, and the real-world distance is <strong>28 km</strong>.<br>(a) Calculate the 3-figure clockwise bearing of Turbine T from Harbour P.<br>(b) Calculate the 3-figure back bearing of Harbour P from Turbine T.<br>(c) On a sea chart with scale <strong>1 : 400,000</strong> (where 1 cm = 4 km), how many cm from P should Turbine T be plotted?',
                'steps': [
                    ('Step 1', 'Subtract 65° from 360° for the clockwise bearing from P', '360° − 65° = 295°.', 'M1 / A1: Outward bearing = 295°'),
                    ('Step 2', 'Subtract 180° for the back bearing from T to P', '295° − 180° = 115°.', 'A1: Back bearing = 115°'),
                    ('Step 3', 'Divide 28 km by 4 km/cm for the chart distance', '28 km ÷ 4 km = 7.0 cm.', 'A1: Chart distance = 7.0 cm')
                ],
                'final_answer': '(a) 295° | (b) 115° | (c) 7.0 cm',
                'tutor_tip': 'Whenever an angle is given to the West (left) of North, subtract it from 360° to get the clockwise bearing.'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Omitting the Leading Zero on Bearings Under 100°',
                'desc': 'Writing 65° instead of 065° loses the bearing accuracy mark.',
                'fix': 'Always write 3 digits for every bearing.'
            },
            {
                'title': 'Measuring from the Wrong End ("Bearing of A FROM B")',
                'desc': 'Measuring the angle at A instead of at B when asked for "the bearing of A from B".',
                'fix': 'Circle the letter after the word "FROM"—that is where your North line and protractor must sit!'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'A straight hospital corridor is met by an angled fire-exit passage. One angle at the wall is <strong>128°</strong>. Calculate the acute angle next to it on the straight wall.',
                'solution_steps': '1. Angles on a straight line sum to 180°.<br>2. 180° − 128° = 52°.',
                'correct_answer': '52°',
                'tutor_tip': '180° − 128° = 52°.'
            },
            {
                'marks': '2 Marks',
                'question': 'A delivery drone flies from Depot D to Drop-Zone Z on a bearing of <strong>242°</strong>. Calculate the 3-figure back bearing from Drop-Zone Z to Depot D.',
                'solution_steps': '1. Since 242° > 180°, subtract 180°: 242° − 180° = 62°.<br>2. Pad to 3 digits: 062°.',
                'correct_answer': '062°',
                'tutor_tip': 'Remember the leading zero: 062°!'
            },
            {
                'marks': '3 Marks',
                'question': 'Three cables meet at a central mast point. The angles between the first two pairs of cables are <strong>115° and 140°</strong>. Calculate the third angle around the point.',
                'solution_steps': '1. Sum of known angles = 115° + 140° = 255°.<br>2. Third angle = 360° − 255° = 105°.',
                'correct_answer': '105°',
                'tutor_tip': 'Angles around a full point always add up to 360°.'
            }
        ]
    },
    {
        'filename': 'functional-skills-comparing-data-sets.html',
        'clean_topic': 'Comparing Data Sets & Distribution Consistency',
        'intro_lead': 'Compare two statistical data distributions using an appropriate measure of average (mean or median) and the range to evaluate workplace performance and consistency.',
        'next_file': 'functional-skills-maths-level-2.html',
        'next_name': 'Maths Level 2 Directory',
        'spec_points': [
            ('L2.29', 'Compare two data sets using an appropriate measure of average (mean, median, or mode) and the range, making contextual conclusions.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-scale-balanced',
                'title': 'Golden Rule 1: Always Write TWO Distinct Comparison Statements (Average + Range)',
                'desc': 'Full marks on any Level 2 comparison question require: Statement 1 comparing the Average (mean or median) in context, AND Statement 2 comparing the Range and explaining what it means for consistency.',
                'badge': 'Statement 1: Compare Average • Statement 2: Compare Range / Consistency'
            },
            {
                'icon': 'fa-compress',
                'title': 'Golden Rule 2: Smaller Range = MORE Consistent (Less Variable)',
                'desc': 'A smaller range means all values are clustered closely together (more reliable/consistent). A larger range means values are widely spread out (less consistent/more unpredictable).',
                'badge': 'Smaller Range = More Consistent • Larger Range = More Variable'
            }
        ],
        'skills': [
            {
                'title': 'The Full-Mark 2-Sentence Comparison Template',
                'summary': 'Word-for-word sentence structures that guarantee full marks on Pearson Edexcel papers.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Sentence 1 (Average in Context):</strong> <em>"On average, [Group A] had a higher/lower [context metric] than [Group B], because its mean/median was [X] compared to [Y]."</em></li>
                    <li><strong>Sentence 2 (Range &amp; Consistency):</strong> <em>"[Group B] was more consistent than [Group A] because its range was smaller ([R₂] compared to [R₁])."</em></li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'When "Lower Mean" Means "Better Performance"',
                'summary': 'Distinguishing waiting times and defect rates from sales and test scores.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:left;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Metric Type</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Which Average is Better?</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Which Range is Better?</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Sales, Exam Scores, Output</td><td style="padding:6px; border:1px solid #cbd5e1;"><strong>Higher Mean/Median</strong> is better</td><td style="padding:6px; border:1px solid #cbd5e1;"><strong>Smaller Range</strong> = more consistent</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Waiting Time, Delivery Delay, Errors</td><td style="padding:6px; border:1px solid #cbd5e1;"><strong>Lower Mean/Median</strong> is better (faster/fewer errors)</td><td style="padding:6px; border:1px solid #cbd5e1;"><strong>Smaller Range</strong> = more predictable</td></tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                'title': 'Calculating Raw Data Stats Against a Pre-Calculated Summary Table',
                'summary': 'How exam questions give raw numbers for Team A and a summary table for Team B.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">If Team B's summary gives the <strong>Median and Range</strong>, then you should calculate the <strong>Median and Range</strong> for Team A so you are comparing like-for-like measures!</p>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Hospital Shift Medication Dispensing Accuracy Comparison (Level 2 Core)',
                'marks': '3 Marks (Pearson Edexcel Level 2)',
                'context': 'Clinical Pharmacy Audit',
                'question': 'A clinical audit compares dispensing accuracy rates across Day and Night shifts:<br>• <strong>Day Shift:</strong> Mean = <strong>96.5%</strong>, Range = <strong>4.0%</strong><br>• <strong>Night Shift:</strong> Mean = <strong>94.0%</strong>, Range = <strong>9.0%</strong><br>Compare the dispensing accuracy of the two shifts using both the mean and the range.',
                'steps': [
                    ('Step 1', 'Compare the Mean in context', 'Day Shift had a higher average dispensing accuracy than Night Shift (mean 96.5% vs 94.0%).', 'A1: Valid contextual mean comparison'),
                    ('Step 2', 'Compare the Range in terms of consistency', 'Day Shift was more consistent than Night Shift because its range was smaller (4.0% vs 9.0%).', 'A1: Valid range/consistency comparison'),
                    ('Step 3', 'State overall recommendation', 'Day Shift performed better both on average accuracy and consistency.', 'A1: Supporting figures cited clearly')
                ],
                'final_answer': 'Day Shift had higher average accuracy (mean 96.5% vs 94.0%) and was more consistent (smaller range of 4.0% vs 9.0%).',
                'tutor_tip': 'Always include the actual numbers (96.5% vs 94.0% and 4.0% vs 9.0%) inside your comparison sentences.'
            },
            {
                'title': 'Two Courier Companies Delivery Time Audit (Raw Data vs Summary) (Level 2 Multi-Step)',
                'marks': '4 Marks (Pearson Edexcel Level 2)',
                'context': 'Medical Pathology Sample Courier Selection',
                'question': 'A pathology lab tests two courier firms over <strong>6 urgent sample deliveries</strong> (time in minutes):<br>• <strong>SwiftMed (Raw times):</strong> <strong>28, 35, 24, 31, 42, 26</strong><br>• <strong>BioExpress (Summary):</strong> <strong>Mean = 34 minutes, Range = 8 minutes</strong>.<br>Calculate the mean and range for SwiftMed, and write two comparisons between the two couriers.',
                'steps': [
                    ('Step 1', 'Calculate SwiftMed Mean (Sum ÷ 6)', 'Sum = 28 + 35 + 24 + 31 + 42 + 26 = 186 minutes.<br>Mean = 186 ÷ 6 = 31 minutes.', 'M1: SwiftMed Mean (31 mins)'),
                    ('Step 2', 'Calculate SwiftMed Range (Highest − Lowest)', 'Range = 42 − 24 = 18 minutes.', 'A1: SwiftMed Range (18 mins)'),
                    ('Step 3', 'Compare Averages in context', 'SwiftMed was faster on average, with a lower mean delivery time (31 mins vs 34 mins).', 'A1: Valid average comparison'),
                    ('Step 4', 'Compare Consistency using Range', 'However, BioExpress had more consistent delivery times because its range was smaller (8 mins vs 18 mins).', 'A1: Valid consistency comparison')
                ],
                'final_answer': 'SwiftMed Mean = 31 mins, Range = 18 mins. SwiftMed is faster on average (31 vs 34 mins), but BioExpress is more consistent (range 8 vs 18 mins).',
                'tutor_tip': 'Notice the trade-off: SwiftMed has a faster average, whereas BioExpress is more consistent!'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Stating "Range is Smaller" Without Explaining It Means "More Consistent"',
                'desc': 'Writing "Day Shift has a smaller range of 4%" without interpreting what a smaller range means in real life loses the interpretation mark.',
                'fix': 'Always add the words "...which means their performance is more consistent."'
            },
            {
                'title': 'Comparing Mean of Group A with Median of Group B',
                'desc': 'You must compare like with like (Mean vs Mean, or Median vs Median).',
                'fix': 'Calculate the same type of average that is given for the second group.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': '<strong>Depot A:</strong> Mean daily parcels = 420, Range = 45. <strong>Depot B:</strong> Mean daily parcels = 465, Range = 130. Write two sentences comparing the daily parcel deliveries of Depot A and Depot B.',
                'solution_steps': '1. Average: Depot B delivers more parcels per day on average (mean 465 vs 420).<br>2. Consistency: Depot A has more consistent daily delivery numbers because its range is smaller (45 vs 130).',
                'correct_answer': 'Depot B has a higher average (465 vs 420), but Depot A is more consistent (smaller range of 45 vs 130).',
                'tutor_tip': 'Always write one sentence for the mean and one sentence for the range.'
            },
            {
                'marks': '3 Marks',
                'question': 'Nurse A records 5 blood pressure check times (in mins): <strong>6, 9, 5, 12, 8</strong>. Nurse B has a <strong>median of 7 mins</strong> and a <strong>range of 4 mins</strong>. Calculate the median and range for Nurse A and state which nurse is more consistent.',
                'solution_steps': '1. Nurse A ordered: 5, 6, 8, 9, 12 → Median = 8 mins.<br>2. Nurse A Range = 12 − 5 = 7 mins.<br>3. Nurse B is more consistent because Nurse B has a smaller range (4 mins vs 7 mins).',
                'correct_answer': 'Nurse A Median = 8 mins, Range = 7 mins; Nurse B is more consistent (range 4 vs 7 mins)',
                'tutor_tip': 'Since Nurse B’s summary uses the median, calculate the median for Nurse A.'
            },
            {
                'marks': '3 Marks',
                'question': 'Machine X produces bolts with a mean length of <strong>50.0 mm (Range = 0.4 mm)</strong>. Machine Y produces bolts with a mean length of <strong>50.0 mm (Range = 1.8 mm)</strong>. If the engineering specification requires bolts to be as close to 50.0 mm as possible, which machine should the factory keep and why?',
                'solution_steps': '1. Both machines have the exact same mean length (50.0 mm).<br>2. Machine X has a much smaller range (0.4 mm vs 1.8 mm), meaning its bolt lengths are much more consistent and closer to 50.0 mm.<br>3. Keep Machine X.',
                'correct_answer': 'Keep Machine X because it has a much smaller range (0.4 mm vs 1.8 mm), making bolt lengths far more consistent.',
                'tutor_tip': 'When averages are equal, the range (consistency) decides the winner!'
            }
        ]
    },
    {
        'filename': 'functional-skills-symmetry-and-2d-shapes.html',
        'clean_topic': 'Symmetry & 2D Shapes',
        'intro_lead': 'Identify reflective lines of symmetry, determine rotational symmetry orders, complete symmetrical patterns across mirror lines, and classify geometric 2D shapes.',
        'next_file': 'functional-skills-2d-shapes.html',
        'next_name': '2D Shapes',
        'spec_points': [
            ('E3.8 / L1.21', 'Identify lines of reflective symmetry and order of rotational symmetry in 2D shapes and workplace signage.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-lines-leaning',
                'title': 'Golden Rule 1: A Line of Symmetry is an Exact Mirror Fold Line',
                'desc': 'If you fold a shape along a line of symmetry, both halves must match up edge-to-edge and corner-to-corner. In a non-square rectangle, the diagonals are NOT lines of symmetry!',
                'badge': 'Reflective Symmetry = Both Halves Match When Folded'
            },
            {
                'icon': 'fa-rotate',
                'title': 'Golden Rule 2: Minimum Rotational Symmetry Order is ALWAYS 1 (Never 0!)',
                'desc': 'Rotational symmetry order is how many times a shape looks identical during a full 360° spin. Because every shape matches itself at 360°, the lowest possible order of rotational symmetry is 1 (never write 0).',
                'badge': 'Rotational Order = Matches in 360° (Minimum Order = 1)'
            }
        ],
        'skills': [
            {
                'title': 'Reflective & Rotational Symmetry Master Reference Table',
                'summary': 'Lines of symmetry and rotational order for all common 2D exam shapes.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:center;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">2D Shape</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Lines of Reflective Symmetry</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Order of Rotational Symmetry</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Equilateral Triangle</td><td style="padding:6px; border:1px solid #cbd5e1;">3</td><td style="padding:6px; border:1px solid #cbd5e1;">3</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Isosceles Triangle</td><td style="padding:6px; border:1px solid #cbd5e1;">1</td><td style="padding:6px; border:1px solid #cbd5e1;">1</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Scalene Triangle</td><td style="padding:6px; border:1px solid #cbd5e1;">0</td><td style="padding:6px; border:1px solid #cbd5e1;">1</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Square</td><td style="padding:6px; border:1px solid #cbd5e1;">4</td><td style="padding:6px; border:1px solid #cbd5e1;">4</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Rectangle (non-square)</td><td style="padding:6px; border:1px solid #cbd5e1;">2</td><td style="padding:6px; border:1px solid #cbd5e1;">2</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Rhombus</td><td style="padding:6px; border:1px solid #cbd5e1;">2 (diagonals)</td><td style="padding:6px; border:1px solid #cbd5e1;">2</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Parallelogram</td><td style="padding:6px; border:1px solid #cbd5e1;">0</td><td style="padding:6px; border:1px solid #cbd5e1;">2</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Kite</td><td style="padding:6px; border:1px solid #cbd5e1;">1</td><td style="padding:6px; border:1px solid #cbd5e1;">1</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Regular n-sided Polygon</td><td style="padding:6px; border:1px solid #cbd5e1;">n</td><td style="padding:6px; border:1px solid #cbd5e1;">n</td></tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                'title': 'Reflecting a Shape Across a Mirror Line on a Grid',
                'summary': 'Counting perpendicular grid squares to the mirror line.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li>Pick one vertex (corner) of the original shape and count how many grid squares it is from the mirror line.</li>
                    <li>Count that <strong>exact same number of grid squares</strong> on the opposite side of the mirror line and plot a dot.</li>
                    <li>Repeat for every corner and join the dots with a ruler.</li>
                  </ol>
                </div>
                """
            },
            {
                'title': 'Symmetry in Capital Letters, Logos & Road Signs',
                'summary': 'Identifying horizontal, vertical, and rotational symmetry in symbols.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Vertical Line of Symmetry Only:</strong> A, M, T, U, V, W, Y.</li>
                    <li><strong>Horizontal Line of Symmetry Only:</strong> B, C, D, E, K.</li>
                    <li><strong>Both Vertical &amp; Horizontal (2 Lines, Order 2):</strong> H, I, O, X.</li>
                    <li><strong>Zero Lines of Symmetry, Rotational Order 2:</strong> N, S, Z.</li>
                  </ul>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Safety Warning Symbol Symmetry Analysis (Entry 3 / Level 1 Foundation)',
                'marks': '2 Marks (Entry Level 3 / Level 1)',
                'context': 'Health and Safety Wayfinding',
                'question': 'A blank hazard warning sign is shaped as an <strong>equilateral triangle</strong>, while a first-aid cross has <strong>4 equal arms</strong>.<br>(a) How many lines of reflective symmetry does the equilateral triangle have?<br>(b) What is the order of rotational symmetry of the 4-armed first-aid cross?',
                'steps': [
                    ('Step 1', 'State reflective symmetry of an equilateral triangle', 'An equilateral triangle has 3 equal sides and 3 lines of symmetry.', 'A1: 3 lines of symmetry'),
                    ('Step 2', 'State rotational symmetry order of the 4-armed equal cross', 'A 4-armed equal cross matches itself every 90° (4 times in 360°) → Order 4.', 'A1: Order 4')
                ],
                'final_answer': '(a) 3 lines of symmetry | (b) Rotational symmetry of order 4',
                'tutor_tip': 'For any regular shape with n equal sides or arms, lines of symmetry = rotational order = n.'
            },
            {
                'title': 'Symmetrical Courtyard Tile Pattern Grid Completion & Costing (Level 1/2 Multi-Step)',
                'marks': '4 Marks (Pearson Edexcel Level 1/2)',
                'context': 'Architectural Floor Tiling Design',
                'question': 'A designer creates a square floor mosaic that is symmetrical across <strong>both the vertical midline and the horizontal midline</strong> (4 quadrants).<br>• In the <strong>top-left quadrant</strong>, the pattern uses <strong>6 navy tiles and 9 cream tiles</strong>.<br>• Navy tiles cost <strong>£2.50 each</strong> and cream tiles cost <strong>£1.80 each</strong>.<br>Calculate the total number of navy and cream tiles needed for the entire 4-quadrant mosaic, and work out the total tile cost.',
                'steps': [
                    ('Step 1', 'Multiply top-left quadrant counts by 4 for the full symmetrical pattern', 'Total Navy tiles = 4 × 6 = 24 tiles.<br>Total Cream tiles = 4 × 9 = 36 tiles.', 'M1 / A1: 24 navy and 36 cream tiles'),
                    ('Step 2', 'Calculate cost of navy tiles and cream tiles', 'Navy cost = 24 × £2.50 = £60.00.<br>Cream cost = 36 × £1.80 = £64.80.', 'M1: Individual tile costs'),
                    ('Step 3', 'Sum for total mosaic cost', '£60.00 + £64.80 = £124.80.', 'A1: Accurate total cost (£124.80)')
                ],
                'final_answer': '24 navy tiles, 36 cream tiles — Total Cost = £124.80',
                'tutor_tip': 'Symmetry across both horizontal and vertical midlines means all 4 quarters of the design have identical tile counts!'
            }
        ],
        'examiner_traps': [
            {
                'title': "Writing 'Order 0' for Rotational Symmetry",
                'desc': 'There is no such thing as rotational symmetry of order 0! Every shape looks identical after a full 360° turn, so the minimum order is 1.',
                'fix': 'Reflective lines of symmetry can be 0, but Rotational Order is ALWAYS at least 1.'
            },
            {
                'title': 'Drawing Diagonal Lines of Symmetry on a Non-Square Rectangle',
                'desc': 'A rectangle has only 2 lines of symmetry (horizontal and vertical).',
                'fix': 'Only a square or rhombus has diagonal lines of symmetry.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'State the number of lines of reflective symmetry and the order of rotational symmetry for a <strong>standard parallelogram</strong>.',
                'solution_steps': '1. Lines of reflective symmetry = 0.<br>2. Order of rotational symmetry = 2 (matches at 180° and 360°).',
                'correct_answer': '0 lines of symmetry; Rotational symmetry of order 2',
                'tutor_tip': 'A parallelogram is the classic shape with 0 mirror lines but rotational symmetry of order 2!'
            },
            {
                'marks': '2 Marks',
                'question': 'A regular polygon has an interior angle of <strong>120°</strong> and <strong>6 equal sides</strong>. How many lines of symmetry does it have, and through how many degrees do you rotate it before it first matches its outline?',
                'solution_steps': '1. A 6-sided regular hexagon has 6 lines of symmetry.<br>2. Angle of rotation = 360° ÷ 6 = 60°.',
                'correct_answer': '6 lines of symmetry; 60° rotation',
                'tutor_tip': 'Divide 360° by the rotational order (6) to find the smallest rotation angle (60°).'
            },
            {
                'marks': '2 Marks',
                'question': 'On a coordinate grid, point P is at <strong>(2, 5)</strong>. What are the coordinates of the reflected point P′ when reflected across the <strong>vertical Y-axis (x = 0)</strong>?',
                'solution_steps': '1. Point P(2, 5) is 2 units to the right of the Y-axis.<br>2. Reflecting across the Y-axis places P′ 2 units to the left at the same height: (−2, 5).',
                'correct_answer': '(−2, 5)',
                'tutor_tip': 'Reflecting across the vertical Y-axis flips the sign of the x-coordinate while keeping y unchanged.'
            }
        ]
    },
    {
        'filename': 'functional-skills-number-patterns.html',
        'clean_topic': 'Number Patterns & Linear Sequences',
        'intro_lead': 'Recognise, describe, and continue linear number patterns, decimal sequences, negative number sequences, and nth-term rules in workplace scheduling and stock replenishment.',
        'next_file': 'functional-skills-numbers-and-place-value.html',
        'next_name': 'Numbers & Place Value',
        'spec_points': [
            ('E3.6 / L1.1', 'Recognise, describe, and continue linear sequences of whole numbers, decimals, and negative numbers.'),
            ('L1.5 / L2.5', 'Apply term-to-term rules and simple position-to-term formulas to solve workplace scheduling and stock problems.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-arrow-up-9-1',
                'title': 'Golden Rule 1: Find the Step Difference Between TWO Pairs to Confirm the Rule',
                'desc': 'Subtract the 1st term from the 2nd term, and ALWAYS check that the gap from the 2nd to the 3rd term is identical (e.g. +7, −14, +0.25). Write the step rule (+ or −) above the arrows!',
                'badge': 'Step Rule = 2nd Term − 1st Term (Check with 3rd − 2nd)'
            },
            {
                'icon': 'fa-arrows-left-right',
                'title': 'Golden Rule 2: Jumping Multiple Steps = Start Term + (Number of Jumps × Step)',
                'desc': 'To go from the 1st term to the 10th term, there are 9 JUMPS (not 10!). So 10th Term = 1st Term + (9 × Step Difference).',
                'badge': 'Nth Term = 1st Term + ((N − 1) × Step)'
            }
        ],
        'skills': [
            {
                'title': 'Increasing, Decreasing, Decimal & Negative Sequences',
                'summary': 'Spotting constant addition and subtraction patterns across zero.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Increasing Whole Numbers:</strong> 14, 21, 28, 35, ... (Rule: <strong>Add 7</strong> &rarr; Next = <strong>42</strong>).</li>
                    <li><strong>Decreasing Whole Numbers:</strong> 90, 78, 66, 54, ... (Rule: <strong>Subtract 12</strong> &rarr; Next = <strong>42</strong>).</li>
                    <li><strong>Decimal Sequence:</strong> 1.50, 1.75, 2.00, 2.25, ... (Rule: <strong>Add 0.25</strong> &rarr; Next = <strong>2.50</strong>).</li>
                    <li><strong>Crossing Zero into Negatives:</strong> 8, 5, 2, &minus;1, &minus;4, ... (Rule: <strong>Subtract 3</strong> &rarr; Next = <strong>&minus;7</strong>).</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Finding Missing Middle Terms in a Sequence',
                'summary': 'Dividing the total jump by the number of steps when a middle box is blank.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">If a sequence has a missing middle number: <strong>18, ___, 34, 42</strong>:</p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li>From 18 to 34 is <strong>2 jumps</strong> covering 34 &minus; 18 = <strong>16</strong>.</li>
                    <li>1 jump = 16 &divide; 2 = <strong>+8</strong> (confirmed by 34 + 8 = 42).</li>
                    <li>Missing term = 18 + 8 = <strong>26</strong>.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Fixed Call-Out + Per-Unit Cost Sequences',
                'summary': 'Using linear sequences to model equipment hire and modular seating.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7; margin-top:0;">Example: 1 table seats 6 people; 2 joined tables seat 10 people; 3 joined tables seat 14 people (Rule: <strong>+4 people per extra table</strong>, or <strong>Seats = 4n + 2</strong>).</p>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Pharmacy Automated Medication Dispenser Schedule (Entry 3 / Level 1 Foundation)',
                'marks': '2 Marks (Entry Level 3 / Level 1)',
                'context': 'Clinical Pharmacy Stock Control',
                'question': 'A pharmacy stock counter records the remaining boxes of bandages at the end of each day:<br><strong>Monday: 85 • Tuesday: 71 • Wednesday: 57 • Thursday: 43</strong><br>If usage continues at the same daily rate, how many boxes will remain at the end of Friday and Saturday?',
                'steps': [
                    ('Step 1', 'Find the daily step rule', '85 − 71 = 14 boxes used per day (Rule: subtract 14).', 'M1: Step rule (−14)'),
                    ('Step 2', 'Apply rule for Friday and Saturday', 'Friday = 43 − 14 = 29 boxes.<br>Saturday = 29 − 14 = 15 boxes.', 'A1: Accurate terms (29 and 15)')
                ],
                'final_answer': 'Friday: 29 boxes | Saturday: 15 boxes',
                'tutor_tip': 'Check the difference between at least two pairs (85 − 71 = 14 and 71 − 57 = 14) before continuing.'
            },
            {
                'title': 'Modular Conference Table Seating Pattern Problem (Level 1/2 Multi-Step)',
                'marks': '4 Marks (Pearson Edexcel Level 1/2)',
                'context': 'Hospital Training Room Layout',
                'question': 'A training centre arranges rectangular tables end-to-end in a single long row:<br>• <strong>1 table</strong> seats <strong>6 delegates</strong> (2 on each side plus 1 at each end).<br>• <strong>2 tables</strong> joined end-to-end seat <strong>10 delegates</strong>.<br>• <strong>3 tables</strong> joined end-to-end seat <strong>14 delegates</strong>.<br>(a) How many delegates can sit at a row of <strong>8 joined tables</strong>?<br>(b) How many tables must be joined in a single row to seat <strong>50 delegates</strong>?',
                'steps': [
                    ('Step 1', 'Identify the sequence rule (+4 delegates for each extra table)', 'Sequence: 6, 10, 14, 18... Each additional table adds 4 seats (Rule: 4n + 2).', 'M1: Identifying +4 step rule'),
                    ('Step 2', 'Calculate seats for 8 tables', '1st table = 6, plus 7 extra tables × 4 = 6 + 28 = 34 delegates (or 4 × 8 + 2 = 34).', 'A1: 34 delegates'),
                    ('Step 3', 'Work backwards from 50 delegates to find number of tables', 'Subtract the 2 end seats: 50 − 2 = 48 side seats.<br>Divide by 4 seats per table: 48 ÷ 4 = 12 tables.', 'M1 / A1: 12 tables required')
                ],
                'final_answer': '(a) 34 delegates | (b) 12 tables',
                'tutor_tip': 'Notice that the 2 end seats stay constant at 2, while every table contributes 4 side seats (4n + 2 = 50 → 4n = 48 → n = 12).'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Adding Instead of Subtracting on a Decreasing Sequence',
                'desc': 'Spotting the gap of 14 on 85, 71, 57, 43 but adding 14 to 43 (= 57) instead of subtracting 14 (= 29).',
                'fix': 'Always write a plus (+) or minus (−) sign in front of the gap number.'
            },
            {
                'title': 'Doubling the 4th Term to Find the 8th Term When There Is a Fixed Offset',
                'desc': 'For 4 tables = 18 seats, doubling 18 to get 36 seats for 8 tables is wrong because it double-counts the 2 end seats (actual answer is 34)!',
                'fix': 'Count the number of JUMPS (+4 per table) or use the 4n + 2 rule.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'Find the next two numbers in this decimal sequence: <strong>0.4, 0.7, 1.0, 1.3, ___, ___</strong>',
                'solution_steps': '1. Step rule = 0.7 − 0.4 = +0.3.<br>2. Next terms: 1.3 + 0.3 = 1.6, and 1.6 + 0.3 = 1.9.',
                'correct_answer': '1.6 and 1.9',
                'tutor_tip': 'Think of the sequence in tenths: 4, 7, 10, 13, 16, 19 tenths.'
            },
            {
                'marks': '2 Marks',
                'question': 'Continue this decreasing temperature sequence for the next two terms: <strong>7°C, 3°C, −1°C, ___°C, ___°C</strong>',
                'solution_steps': '1. Step rule = subtract 4°C each time.<br>2. −1 − 4 = −5°C.<br>3. −5 − 4 = −9°C.',
                'correct_answer': '−5°C and −9°C',
                'tutor_tip': 'Going colder from −1°C by 4°C moves further below zero to −5°C.'
            },
            {
                'marks': '3 Marks',
                'question': 'A saver opens a Christmas club account with <strong>£45 in Week 1</strong> and adds <strong>£15 every week</strong> after that (Week 2 = £60, Week 3 = £75). How much money will be in the account in <strong>Week 12</strong>?',
                'solution_steps': '1. From Week 1 to Week 12 is 11 weekly jumps of £15.<br>2. Added amount = 11 × £15 = £165.<br>3. Total in Week 12 = £45 + £165 = £210.',
                'correct_answer': '£210',
                'tutor_tip': 'From Week 1 to Week 12 is 11 jumps (12 − 1 = 11), so £45 + (11 × £15) = £210.'
            }
        ]
    },
    {
        'filename': 'functional-skills-temperature.html',
        'clean_topic': 'Temperature, Negative Numbers & Thermometer Scales',
        'intro_lead': 'Read Celsius and Fahrenheit thermometer scales, calculate temperature rises and drops across zero (0°C), order negative temperatures, and apply conversion formulas.',
        'next_file': 'functional-skills-scales.html',
        'next_name': 'Reading Gauges, Dials & Measuring Scales',
        'spec_points': [
            ('E3.14 / L1.2', 'Use, order, and compare positive and negative temperatures in practical contexts.'),
            ('L1.2 / L2.1', 'Calculate temperature changes and differences across 0°C and use Celsius/Fahrenheit conversion formulas.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-temperature-half',
                'title': 'Golden Rule 1: Use Zero (0°C) as a Stepping Stone for Differences Across Zero',
                'desc': 'To find the difference between a negative temperature (e.g. −6°C) and a positive temperature (e.g. +15°C), find the distance from −6°C up to 0°C (6 degrees), then from 0°C up to +15°C (15 degrees), and ADD them together: 6 + 15 = 21°C.',
                'badge': 'Difference Across 0°C = Distance Below 0°C + Distance Above 0°C'
            },
            {
                'icon': 'fa-snowflake',
                'title': 'Golden Rule 2: Larger Negative Digits Mean COLDER (Lower) Temperatures',
                'desc': 'Below zero, the scale counts downwards: −20°C is much colder (lower) than −4°C because it is 20 degrees below freezing!',
                'badge': '−20°C is COLDER than −4°C • −4°C is WARMER than −20°C'
            }
        ],
        'skills': [
            {
                'title': 'Bridging Across 0°C for Temperature Rises, Drops & Differences',
                'summary': 'Visualising a vertical thermometer with 0°C in the middle.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Difference Between &minus;8°C and +14°C:</strong> 8 degrees to reach 0°C + 14 degrees above 0°C = <strong>22°C difference</strong>.</li>
                    <li><strong>Difference Between Two Negatives (&minus;18°C and &minus;5°C):</strong> Both are below zero, so find the gap between 18 and 5: 18 &minus; 5 = <strong>13°C difference</strong>.</li>
                    <li><strong>Rising from a Negative (&minus;12°C rises by 7°C):</strong> Moves closer to zero: &minus;12 + 7 = <strong>&minus;5°C</strong>.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Food Safety & Clinical Cold-Chain Benchmark Temperatures',
                'summary': 'Standard temperatures tested in catering and healthcare scenarios.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:left;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Benchmark Context</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Standard Celsius (°C)</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Safety Rule</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Commercial Freezer</td><td style="padding:6px; border:1px solid #cbd5e1;">&minus;18°C or colder</td><td style="padding:6px; border:1px solid #cbd5e1;">&minus;21°C is safe; &minus;12°C is too warm (unsafe!)</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Fridge / Vaccine Chiller</td><td style="padding:6px; border:1px solid #cbd5e1;">2°C to 8°C</td><td style="padding:6px; border:1px solid #cbd5e1;">Must not freeze (&le; 0°C) or exceed 8°C</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Normal Human Body</td><td style="padding:6px; border:1px solid #cbd5e1;">37.0°C</td><td style="padding:6px; border:1px solid #cbd5e1;">&ge; 38.0°C indicates clinical fever</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Hot Food Holding / Cooking</td><td style="padding:6px; border:1px solid #cbd5e1;">&ge; 63°C (Hold) / &ge; 75°C (Cook)</td><td style="padding:6px; border:1px solid #cbd5e1;">Water boils at 100°C</td></tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                'title': 'Celsius (°C) ↔ Fahrenheit (°F) Formula Conversions',
                'summary': 'Substituting positive and negative temperatures into F = 1.8C + 32.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Celsius to Fahrenheit:</strong> <strong>F = (1.8 &times; C) + 32</strong> (or C &times; 9 &divide; 5 + 32).<br><em>Example for 25°C: (1.8 &times; 25) + 32 = 45 + 32 = <strong>77°F</strong>.</em></li>
                    <li><strong>Fahrenheit to Celsius:</strong> <strong>C = (F &minus; 32) &divide; 1.8</strong>.<br><em>Example for 68°F: (68 &minus; 32) &divide; 1.8 = 36 &divide; 1.8 = <strong>20°C</strong>.</em></li>
                  </ul>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Hospital Catering Walk-In Freezer vs Kitchen Temperature Difference (Level 1 Foundation)',
                'marks': '3 Marks (Pearson Edexcel Level 1)',
                'context': 'Hospital Food Safety Compliance',
                'question': 'A catering supervisor checks the digital thermometer in the walk-in freezer, which reads <strong>−19°C</strong>. The main kitchen preparation room is at <strong>22°C</strong>.<br>(a) Work out the difference in temperature between the walk-in freezer and the kitchen.<br>(b) A defrost cycle raises the freezer temperature by <strong>5°C</strong>. What is the new freezer temperature, and is it still at or below the mandatory <strong>−18°C</strong> safety limit?',
                'steps': [
                    ('Step 1', 'Bridge across 0°C for total temperature difference', 'From −19°C to 0°C = 19°C; from 0°C to 22°C = 22°C.<br>Total difference = 19 + 22 = 41°C.', 'M1 / A1: 41°C difference'),
                    ('Step 2', 'Add 5°C rise to −19°C and compare with −18°C', '−19°C + 5°C = −14°C.<br>No, −14°C is warmer than −18°C, so it breaches the safety limit.', 'A1: −14°C and No conclusion')
                ],
                'final_answer': '(a) 41°C difference | (b) −14°C — No, warmer than the −18°C limit',
                'tutor_tip': 'When temperature rises from −19°C by 5°C, it moves UP towards zero to −14°C (not −24°C!).'
            },
            {
                'title': 'US Medical Autoclave Sterilisation Temperature Conversion (Level 2 Multi-Step)',
                'marks': '4 Marks (Pearson Edexcel Level 2)',
                'context': 'Surgical Instrument Sterilisation',
                'question': 'An American surgical autoclave manual states that instruments must be sterilised at a minimum temperature of <strong>250°F</strong>.<br>• The UK hospital autoclave displays temperatures in Celsius (°C) and is currently set to <strong>122°C</strong>.<br>• Use the formula <strong>F = 1.8C + 32</strong>.<br>Determine whether the UK setting of 122°C meets the minimum 250°F requirement.',
                'steps': [
                    ('Step 1', 'Substitute C = 122 into 1.8 × C', '1.8 × 122 = 219.6.', 'M1: Multiplication step (219.6)'),
                    ('Step 2', 'Add 32 to find temperature in °F', '219.6 + 32 = 251.6°F.', 'M1 / A1: Accurate Fahrenheit value (251.6°F)'),
                    ('Step 3', 'Compare 251.6°F with 250°F minimum', 'Yes, 251.6°F is above the 250°F minimum requirement (by 1.6°F).', 'A1: Valid Yes conclusion with figures')
                ],
                'final_answer': 'Yes — 122°C equals 251.6°F, which exceeds the 250°F minimum',
                'tutor_tip': 'Follow BIDMAS in F = 1.8C + 32: always multiply 1.8 by C FIRST, then add 32!'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Subtracting 19 from 22 Instead of Bridging Across Zero (22 − 19 = 3°C)',
                'desc': 'Ignoring the minus sign on −19°C and doing 22 − 19 = 3°C instead of 22 + 19 = 41°C.',
                'fix': 'If one temperature is negative and one is positive, ADD their distances from 0°C!'
            },
            {
                'title': 'Thinking −14°C is Colder Than −18°C',
                'desc': 'In freezer safety questions, −14°C is WARMER than −18°C (closer to 0°C), which means the freezer is too warm!',
                'fix': 'Draw a vertical thermometer: 0°C at the top, then −14°C, then −18°C below it.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'Overnight, the outside temperature at an ambulance station drops from <strong>4.5°C</strong> by <strong>11.2°C</strong>. What is the new temperature?',
                'solution_steps': '1. Drop 4.5°C to reach 0°C.<br>2. Remaining drop below zero = 11.2 − 4.5 = 6.7°C.<br>3. New temperature = −6.7°C.',
                'correct_answer': '−6.7°C',
                'tutor_tip': '4.5 − 11.2 = −6.7°C.'
            },
            {
                'marks': '3 Marks',
                'question': 'Five Cryo-Freezer compartments record temperatures of: <strong>−16.4°C, −21.0°C, −18.5°C, −15.9°C, −20.2°C</strong>.<br>(a) Arrange these temperatures from <strong>coldest to warmest</strong>.<br>(b) Find the range of these temperatures.',
                'solution_steps': '1. Coldest (most negative) to warmest: −21.0°C, −20.2°C, −18.5°C, −16.4°C, −15.9°C.<br>2. Range = difference between −21.0°C and −15.9°C = 21.0 − 15.9 = 5.1°C.',
                'correct_answer': '(a) −21.0°C, −20.2°C, −18.5°C, −16.4°C, −15.9°C | (b) Range = 5.1°C',
                'tutor_tip': 'Both extremes are below zero, so the range is 21.0 − 15.9 = 5.1°C.'
            },
            {
                'marks': '3 Marks',
                'question': 'Use the formula <strong>C = (F − 32) ÷ 1.8</strong> to convert a patient fever reading of <strong>102.2°F</strong> into degrees Celsius (°C).',
                'solution_steps': '1. Brackets first: 102.2 − 32 = 70.2.<br>2. Divide by 1.8: 70.2 ÷ 1.8 = 39.0°C.',
                'correct_answer': '39°C (or 39.0°C)',
                'tutor_tip': 'Subtract 32 FIRST before dividing by 1.8!'
            }
        ]
    }
]
