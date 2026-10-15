#!/usr/bin/env python3
"""Maths Domain 1: Number & Number Systems (10 Core Topics)"""

TOPICS_DOMAIN1 = [
    {
        'filename': 'functional-skills-numbers-and-place-value.html',
        'clean_topic': 'Numbers & Place Value',
        'intro_lead': 'Master place value columns from millions down to thousandths, understand the role of zero as a placeholder, and read/write large numbers accurately in healthcare and commercial reports.',
        'next_file': 'functional-skills-ordering-numbers.html',
        'next_name': 'Ordering Numbers',
        'spec_points': [
            ('L1.1 / L2.1', 'Read, write, order and compare large positive whole numbers up to 1,000,000 and beyond.'),
            ('L2.2', 'Recognise and use numbers given in figures and in words in workplace documents.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-table-columns',
                'title': 'Golden Rule 1: The Zero Placeholder Protects Positional Value',
                'desc': "A digit's value is determined entirely by its column. If a column has no value, you MUST write a zero as a placeholder (e.g. two million and five thousand is 2,005,000, NOT 2,5000).",
                'badge': 'Millions | H-Th | T-Th | Th | Hundreds | Tens | Units'
            },
            {
                'icon': 'fa-layer-group',
                'title': 'Golden Rule 2: Group Digits in Threes from the Decimal Point',
                'desc': 'When reading or writing large numbers, work in blocks of three digits separated by commas or thin spaces (e.g. 14,250,800).',
                'badge': '14,250,800 = 14 million, 250 thousand, 800'
            }
        ],
        'skills': [
            {
                'title': 'Skill 1: Place Value Hierarchy & Digit Values',
                'summary': 'The definitive 7-column place value chart for Functional Skills Mathematics.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:center;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:10px; border:1px solid #cbd5e1;">Millions (M)</th>
                        <th style="padding:10px; border:1px solid #cbd5e1;">Hundred Thousands (HT)</th>
                        <th style="padding:10px; border:1px solid #cbd5e1;">Ten Thousands (TT)</th>
                        <th style="padding:10px; border:1px solid #cbd5e1;">Thousands (Th)</th>
                        <th style="padding:10px; border:1px solid #cbd5e1;">Hundreds (H)</th>
                        <th style="padding:10px; border:1px solid #cbd5e1;">Tens (T)</th>
                        <th style="padding:10px; border:1px solid #cbd5e1;">Units (U)</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr style="font-weight:700; font-size:1.15rem; color:#0f172a;">
                        <td style="padding:10px; border:1px solid #cbd5e1;">3</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">0</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">4</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">8</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">5</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">2</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">0</td>
                      </tr>
                      <tr style="font-size:0.85rem; color:#64748b;">
                        <td style="padding:8px; border:1px solid #cbd5e1;">3,000,000</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">0</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">40,000</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">8,000</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">500</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">20</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">0</td>
                      </tr>
                    </tbody>
                  </table>
                  <p style="margin-top:12px; font-weight:600; color:#334155;">Spoken in words: <em>Three million, forty-eight thousand, five hundred and twenty.</em></p>
                </div>
                """
            },
            {
                'title': 'Skill 2: Translating Between Words and Figures Using Period Blocks',
                'summary': 'How to convert complex written figures into exact digits without dropping zeros.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">Always split large written numbers at the words <strong>"million"</strong> and <strong>"thousand"</strong> into three 3-digit blocks:</p>
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Millions Block:</strong> Write the number of millions (e.g. "Six million" &rarr; <code>6,___,___</code>).</li>
                    <li><strong>Thousands Block (3 digits):</strong> Pad with leading zeros if under 100 thousand (e.g. "nine thousand" &rarr; <code>009</code>, giving <code>6,009,___</code>).</li>
                    <li><strong>Units Block (3 digits):</strong> Pad with leading zeros if under 100 (e.g. "and forty-five" &rarr; <code>045</code>, giving <code>6,009,045</code>).</li>
                  </ol>
                </div>
                """
            },
            {
                'title': 'Skill 3: Multiplying & Dividing by Powers of 10 (10, 100, 1,000)',
                'summary': 'Shifting digits across place value columns in non-calculator papers.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:left;">
                    <thead>
                      <tr style="background:#f1f5f9; color:#0f172a;">
                        <th style="padding:10px; border:1px solid #cbd5e1;">Operation</th>
                        <th style="padding:10px; border:1px solid #cbd5e1;">Place Value Shift</th>
                        <th style="padding:10px; border:1px solid #cbd5e1;">Worked Example</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">Multiply by 10 / 100 / 1,000</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">Shift digits 1, 2, or 3 places LEFT</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;"><code>42.5 × 1,000 = 42,500</code></td>
                      </tr>
                      <tr>
                        <td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">Divide by 10 / 100 / 1,000</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">Shift digits 1, 2, or 3 places RIGHT</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;"><code>3,800 ÷ 100 = 38</code></td>
                      </tr>
                      <tr>
                        <td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">Converting "Million" Figures</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">Multiply decimal millions by 1,000,000 (shift 6 places)</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;"><code>£2.45 million = £2,450,000</code></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Model 1 (Level 1 Foundation): NHS Trust Equipment Procurement Audit',
                'marks': '3 Marks (Pearson Edexcel Level 1 Non-Calculator)',
                'context': 'Healthcare Capital Expenditure',
                'question': 'A hospital procurement circular states the capital investment in surgical imaging equipment is <strong>£4,082,500</strong>.<br>(a) Write this amount in words.<br>(b) State the exact value of the digit 8 in this number.',
                'steps': [
                    ('Step 1', 'Break the number into three-digit periods', '4 millions, 082 thousands, 500 units.', 'M1: Place value period identification'),
                    ('Step 2', 'Write in formal words', 'Four million, eighty-two thousand, five hundred pounds.', 'A1: Accurate word translation'),
                    ('Step 3', 'Determine the specific value of digit 8', 'The digit 8 is in the ten-thousands column: 8 × 10,000 = 80,000 (eighty thousand).', 'A1: Correct digit value')
                ],
                'final_answer': '(a) Four million, eighty-two thousand, five hundred pounds | (b) Eighty thousand (£80,000).',
                'tutor_tip': "Notice the hundred-thousands column has a 0. Do NOT say 'four million, eight hundred thousand'; it is eighty-two thousand."
            },
            {
                'title': 'Model 2 (Level 2 Decision): Regional Hospital Funding Allocation Check',
                'marks': '4 Marks (Pearson Edexcel Level 2 Problem Solving)',
                'context': 'Public Sector Budget Reconciliation',
                'question': 'A regional health authority receives a total grant of <strong>£3.4 million</strong>.<br>• Hospital A is allocated <strong>one million, six hundred and fifty thousand pounds (£1,650,000)</strong>.<br>• Hospital B is allocated <strong>£985,000</strong>.<br>• Hospital C requests <strong>eight hundred thousand pounds</strong> from the remaining balance.<br><br>Does the authority have enough remaining funding to approve Hospital C\'s full request? Show your working in figures.',
                'steps': [
                    ('Step 1', 'Convert all written amounts into full standard figures', 'Total grant: £3.4 million = £3,400,000.<br>Hospital A = £1,650,000.<br>Hospital C request = £800,000.', 'M1: Accurate conversion of decimal/word millions into digits'),
                    ('Step 2', 'Calculate total allocated to Hospital A and Hospital B', '£1,650,000 + £985,000 = £2,635,000.', 'M1: Combined allocation addition'),
                    ('Step 3', 'Calculate remaining balance and compare with Hospital C request', 'Remaining = £3,400,000 - £2,635,000 = £765,000.<br>Compare: £765,000 < £800,000 (shortfall of £35,000).', 'M1: Subtraction and comparison'),
                    ('Step 4', 'State final justified conclusion', 'No, the authority does not have enough funding; only £765,000 remains, which is £35,000 less than the £800,000 requested.', 'A1: Clear decision supported by exact figures')
                ],
                'final_answer': 'No (Only £765,000 remains, leaving a shortfall of £35,000 against the £800,000 request).',
                'tutor_tip': 'Converting £3.4 million to £3,400,000 first prevents decimal alignment mistakes when subtracting hundreds of thousands.'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Omitting Placeholder Zeros',
                'desc': "Writing 'four million and twelve' as 4,12 or 4012 instead of 4,000,012 loses the accuracy mark entirely.",
                'fix': 'Always sketch 7 column dashes (_ , _ _ _ , _ _ _) and populate from the units column.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'A logistics firm handled <strong>1,050,402</strong> parcels in November.<br>(a) Write this number in words.<br>(b) State the value of the digit 5.',
                'solution_steps': '1. In words: One million, fifty thousand, four hundred and two.<br>2. Digit 5 is in the ten-thousands column: 50,000 (fifty thousand).',
                'correct_answer': '(a) One million, fifty thousand, four hundred and two | (b) 50,000',
                'tutor_tip': 'Check that you do not omit the placeholder zero in the hundred-thousands and tens columns.'
            },
            {
                'marks': '2 Marks',
                'question': 'A council recycling report states that <strong>two million, three hundred and six thousand, and eighty</strong> glass bottles were collected. Write this number in figures and state what happens to the value of the digit 3 if the number is divided by 10.',
                'solution_steps': '1. Millions block: 2 | Thousands block: 306 | Units block: 080 &rarr; 2,306,080.<br>2. The digit 3 currently represents 300,000. Divided by 10, it shifts one column right to represent 30,000.',
                'correct_answer': '2,306,080 (Digit 3 changes value from 300,000 to 30,000)',
                'tutor_tip': 'Remember to write 080 for "eighty" in the final three-digit block.'
            },
            {
                'marks': '3 Marks',
                'question': 'An NHS vaccination hub receives <strong>1.25 million</strong> syringes. In Quarter 1 it distributes <strong>480,000</strong> syringes, and in Quarter 2 it distributes <strong>five hundred and five thousand</strong> syringes. How many syringes are left in central storage?',
                'solution_steps': '1. Convert to figures: Total = 1,250,000; Q1 = 480,000; Q2 = 505,000.<br>2. Total distributed = 480,000 + 505,000 = 985,000.<br>3. Remaining = 1,250,000 - 985,000 = 265,000 syringes.',
                'correct_answer': '265,000 syringes',
                'tutor_tip': '1.25 million has 6 digits after the 1: 1,250,000.'
            }
        ]
    },
    {
        'filename': 'functional-skills-ordering-numbers.html',
        'clean_topic': 'Ordering Numbers: Whole, Negative & Decimals',
        'intro_lead': 'Compare and sequence positive and negative numbers, temperatures, and decimal measurements in ascending and descending order.',
        'next_file': 'functional-skills-addition-and-subtraction.html',
        'next_name': 'Addition & Subtraction',
        'spec_points': [
            ('L1.2 / L2.1', 'Order and compare integers, decimals, and negative numbers.'),
            ('L1.4', 'Use inequality symbols (<, >, =) to express relationships between values.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-temperature-low',
                'title': 'Golden Rule 1: Negative Numbers Work in Reverse',
                'desc': 'The further to the left on a number line, the smaller the number. Therefore, -18°C is smaller (colder) than -4°C.',
                'badge': '-20 < -15 < -5 < 0 < 5'
            },
            {
                'icon': 'fa-align-left',
                'title': 'Golden Rule 2: Line Up Decimal Points and Pad with Trailing Zeros',
                'desc': 'To compare decimals such as 0.4, 0.375, and 0.09, pad them to equal lengths: 0.400, 0.375, 0.090 before ordering.',
                'badge': '0.090 < 0.375 < 0.400'
            }
        ],
        'skills': [
            {
                'title': 'Skill 1: Number Line Sequencing for Negative and Positive Values',
                'summary': 'How to align negative temperatures and bank balances from lowest to highest.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">When ordering mixed negative and positive values, follow this 3-step checklist:</p>
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Separate Negatives and Positives:</strong> All negative values are strictly smaller than zero and any positive value.</li>
                    <li><strong>Order Negatives in Reverse Magnitude:</strong> The negative number with the largest absolute digit is the smallest (e.g. -14.5 is smaller than -3.2).</li>
                    <li><strong>Find Temperature Differences Across Zero:</strong> Add the distance to zero and the distance above zero (e.g. from -6°C to +15°C = 6 + 15 = 21°C rise).</li>
                  </ol>
                </div>
                """
            },
            {
                'title': 'Skill 2: Padding Decimals with Trailing Zeros (Equalising Decimal Places)',
                'summary': 'Eliminating length bias when comparing thousandths, hundredths, and tenths.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:center;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Original Number</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Padded to 3 d.p.</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Thousandths Value</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Rank (1 = Smallest)</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">2.08</td><td style="padding:8px; border:1px solid #cbd5e1;">2.080</td><td style="padding:8px; border:1px solid #cbd5e1;">2,080</td><td style="padding:8px; border:1px solid #cbd5e1;">2nd</td></tr>
                      <tr><td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">2.4</td><td style="padding:8px; border:1px solid #cbd5e1;">2.400</td><td style="padding:8px; border:1px solid #cbd5e1;">2,400</td><td style="padding:8px; border:1px solid #cbd5e1;">4th (Largest)</td></tr>
                      <tr><td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">2.049</td><td style="padding:8px; border:1px solid #cbd5e1;">2.049</td><td style="padding:8px; border:1px solid #cbd5e1;">2,049</td><td style="padding:8px; border:1px solid #cbd5e1;">1st (Smallest)</td></tr>
                      <tr><td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">2.375</td><td style="padding:8px; border:1px solid #cbd5e1;">2.375</td><td style="padding:8px; border:1px solid #cbd5e1;">2,375</td><td style="padding:8px; border:1px solid #cbd5e1;">3rd</td></tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                'title': 'Skill 3: Using Inequality Symbols (<, >) & Interpreting Ascending/Descending',
                'summary': 'Correct notation for Pearson Edexcel Section A questions.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Ascending Order:</strong> Smallest to Largest (going UP, like climbing stairs: <em>-8, -2, 0, 4, 11</em>).</li>
                    <li><strong>Descending Order:</strong> Largest to Smallest (going DOWN: <em>11, 4, 0, -2, -8</em>).</li>
                    <li><strong>Less Than (<code>&lt;</code>) &amp; Greater Than (<code>&gt;</code>):</strong> The wide open mouth always points to the BIGGER number (e.g. <code>-3 &gt; -9</code> and <code>0.08 &lt; 0.4</code>).</li>
                  </ul>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Model 1 (Level 1 Foundation): Hospital Pharmacy Cold Storage Temperature Monitoring',
                'marks': '3 Marks (Pearson Edexcel Level 1 Non-Calculator)',
                'context': 'Vaccine Storage Compliance',
                'question': 'A pharmacy technician records five temperature readings in vaccine freezer units: <strong>-4.2°C, 3.1°C, -6.8°C, -1.5°C, 0.8°C</strong>.<br>(a) Arrange these temperatures in ascending order (coldest to warmest).<br>(b) Calculate the temperature difference between the coldest and warmest unit.',
                'steps': [
                    ('Step 1', 'Identify and order negative temperatures from coldest', '-6.8°C is furthest below zero, followed by -4.2°C, then -1.5°C.', 'M1: Accurate negative ordering'),
                    ('Step 2', 'Order remaining positive values and write complete ascending list', '0.8°C then 3.1°C. Full order: -6.8°C, -4.2°C, -1.5°C, 0.8°C, 3.1°C.', 'A1: Correct ascending sequence'),
                    ('Step 3', 'Calculate range from -6.8°C to +3.1°C across zero', 'Distance from -6.8 to 0 is 6.8°C. Distance from 0 to 3.1 is 3.1°C.<br>Total difference = 6.8 + 3.1 = 9.9°C.', 'A1: Correct temperature difference')
                ],
                'final_answer': '(a) -6.8°C, -4.2°C, -1.5°C, 0.8°C, 3.1°C | (b) 9.9°C',
                'tutor_tip': "'Ascending' always means smallest to largest. Always bridge through zero when finding the difference between a negative and a positive temperature."
            },
            {
                'title': 'Model 2 (Level 2 Decision): Precision Engineering Shaft Diameter Quality Audit',
                'marks': '4 Marks (Pearson Edexcel Level 2 Problem Solving)',
                'context': 'Manufacturing Quality Control',
                'question': 'An aerospace machinist inspects six steel bolts measured in millimetres:<br><strong>8.405 mm, 8.45 mm, 8.095 mm, 8.4 mm, 8.425 mm, 8.39 mm</strong>.<br>Any bolt strictly smaller than <strong>8.40 mm</strong> must be rejected.<br>(a) Order all six measurements in descending order (largest to smallest).<br>(b) State how many bolts must be rejected.',
                'steps': [
                    ('Step 1', 'Pad all decimal measurements to 3 decimal places', '8.405, 8.450, 8.095, 8.400, 8.425, 8.390.', 'M1: Equalising decimal places to 3 d.p.'),
                    ('Step 2', 'Sequence from largest to smallest (descending)', '8.450 (8.45), 8.425, 8.405, 8.400 (8.4), 8.390 (8.39), 8.095.', 'A1: Accurate descending sequence using original formatting'),
                    ('Step 3', 'Compare against minimum threshold of 8.400 mm', 'Bolts below 8.400 mm are 8.39 mm (8.390) and 8.095 mm.', 'M1: Threshold comparison'),
                    ('Step 4', 'Conclude number of rejected bolts', '2 bolts (8.39 mm and 8.095 mm) must be rejected.', 'A1: Correct rejection count and identification')
                ],
                'final_answer': '(a) 8.45 mm, 8.425 mm, 8.405 mm, 8.4 mm, 8.39 mm, 8.095 mm | (b) 2 bolts rejected (8.39 mm and 8.095 mm).',
                'tutor_tip': 'Notice that 8.4 mm = 8.400 mm, so it meets the minimum 8.40 mm standard and is NOT rejected.'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Assuming Longer Decimals Are Bigger',
                'desc': 'Learners often think 0.125 is bigger than 0.3 because 125 is bigger than 3. In reality, 0.3 = 0.300, which is larger than 0.125.',
                'fix': 'Always pad with zeros: compare 0.300 with 0.125.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'Arrange these warehouse crate weights in descending order: <strong>4.05 kg, 4.5 kg, 4.125 kg, 4.55 kg, 4.009 kg</strong>.',
                'solution_steps': '1. Pad to 3 decimal places: 4.050, 4.500, 4.125, 4.550, 4.009.<br>2. Arrange largest to smallest: 4.55 kg, 4.5 kg, 4.125 kg, 4.05 kg, 4.009 kg.',
                'correct_answer': '4.55 kg, 4.5 kg, 4.125 kg, 4.05 kg, 4.009 kg',
                'tutor_tip': "'Descending' means largest to smallest. Check the question wording carefully."
            },
            {
                'marks': '2 Marks',
                'question': 'Five business bank accounts show the following end-of-month balances: <strong>-£420, £150, -£85, -£1,020, £45</strong>.<br>List the balances in ascending order (lowest to highest).',
                'solution_steps': '1. Isolate negative balances: -£420, -£85, -£1,020. Largest negative is smallest: -£1,020, -£420, -£85.<br>2. Add positive balances in order: £45, £150.',
                'correct_answer': '-£1,020, -£420, -£85, £45, £150',
                'tutor_tip': 'An overdraft of -£1,020 is much lower (more in debt) than -£85.'
            },
            {
                'marks': '3 Marks',
                'question': 'Overnight, the temperature in a walk-in blast chiller drops from <strong>4.5°C</strong> by <strong>22.8°C</strong>. What is the new temperature inside the blast chiller, and is it colder than the target requirement of <strong>-18.0°C</strong>?',
                'solution_steps': '1. New temperature = 4.5 - 22.8 = -18.3°C.<br>2. Compare -18.3°C with -18.0°C: -18.3 < -18.0.<br>3. Conclusion: Yes, -18.3°C is 0.3°C colder than -18.0°C.',
                'correct_answer': '-18.3°C (Yes, it is 0.3°C colder than the -18.0°C target)',
                'tutor_tip': 'Remember that -18.3°C is further below zero than -18.0°C, so it is colder.'
            }
        ]
    },
    {
        'filename': 'functional-skills-addition-and-subtraction.html',
        'clean_topic': 'Addition & Subtraction',
        'intro_lead': 'Perform multi-digit column addition and subtraction with borrowing/carrying, calculate balance reconciliations, and verify solutions using reverse operations in non-calculator contexts.',
        'next_file': 'functional-skills-multiplication.html',
        'next_name': 'Multiplication',
        'spec_points': [
            ('L1.3 / L2.3', 'Add and subtract whole numbers and decimals up to 2 decimal places in practical contexts.'),
            ('L1.7', 'Check calculations using reverse operations and estimation.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-arrows-down-to-line',
                'title': 'Golden Rule 1: Vertical Column Alignment',
                'desc': 'Always align units over units, tens over tens, and decimal points over decimal points. Misaligned columns cause 80% of manual arithmetic errors.',
                'badge': 'Line up decimal points before adding or subtracting'
            },
            {
                'icon': 'fa-rotate-left',
                'title': 'Golden Rule 2: Mandatory Reverse Operation Check',
                'desc': 'In Pearson Edexcel Non-Calculator exams, 1 mark is often explicitly awarded for showing a reverse operation check (e.g. if A - B = C, prove that C + B = A).',
                'badge': 'Check: Result + Subtrahend = Starting Number'
            }
        ],
        'skills': [
            {
                'title': 'Skill 1: Column Addition with Carrying & Decimal Alignment',
                'summary': 'Setting up multi-item additions without shifting columns.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">To add <strong>£145.80 + £39.45 + £8.00</strong> without a calculator:</p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li>Write a vertical stack of decimal points first.</li>
                    <li>Pad whole pound figures with <code>.00</code> so every row has hundredths and tenths.</li>
                    <li>Add from right to left (hundredths &rarr; tenths &rarr; units &rarr; tens &rarr; hundreds), writing carried digits clearly below the answer bar: <code>145.80 + 39.45 + 08.00 = £193.25</code>.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Skill 2: Column Subtraction with Decomposition (Borrowing Across Zeros)',
                'summary': 'Step-by-step subtraction across multiple zeros.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">When subtracting across zeros (e.g. <strong>5,000 - 1,468</strong>):</p>
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li>Borrow from the thousands column (turn 5 into 4, making the hundreds column 10).</li>
                    <li>Borrow from hundreds (turn 10 into 9, making tens column 10).</li>
                    <li>Borrow from tens (turn 10 into 9, making units column 10).</li>
                    <li>Subtract each column cleanly: <code>10 - 8 = 2</code>; <code>9 - 6 = 3</code>; <code>9 - 4 = 5</code>; <code>4 - 1 = 3</code>. Result: <strong>3,532</strong>.</li>
                  </ol>
                </div>
                """
            },
            {
                'title': 'Skill 3: Writing a Valid Pearson Edexcel Reverse Operation Check',
                'summary': 'Securing the guaranteed [B1] check mark in Section A and Section B.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:left;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Original Calculation</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Inverse Operation Required</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Full Mark Written Check</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:8px; border:1px solid #cbd5e1;"><code>850 - 299 = 551</code></td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">Addition (Result + Subtracted)</td>
                        <td style="padding:8px; border:1px solid #cbd5e1; font-weight:700; color:#166534;"><code>551 + 299 = 850</code></td>
                      </tr>
                      <tr>
                        <td style="padding:8px; border:1px solid #cbd5e1;"><code>340 + 485 = 825</code></td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">Subtraction (Total - Part)</td>
                        <td style="padding:8px; border:1px solid #cbd5e1; font-weight:700; color:#166534;"><code>825 - 485 = 340</code></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Model 1 (Level 1 Foundation): NHS Ward Budget Reconciliation (Non-Calculator)',
                'marks': '3 Marks (Pearson Edexcel Level 1/2 Non-Calculator)',
                'context': 'Ward Petty Cash Management',
                'question': 'A ward sister starts the week with a petty cash float of <strong>£850.00</strong>. During the week, she makes three purchases: stationery for £46.75, emergency medical supplies for £189.40, and taxi vouchers for £62.85.<br>(a) Calculate the remaining cash balance.<br>(b) Show a reverse calculation to check your answer.',
                'steps': [
                    ('Step 1', 'Add the three expenditure amounts', '£46.75 + £189.40 + £62.85 = £299.00', 'M1: Total expenditure addition'),
                    ('Step 2', 'Subtract total expenditure from starting float', '£850.00 - £299.00 = £551.00', 'A1: Accurate remaining balance'),
                    ('Step 3', 'Perform reverse operation check', '£551.00 + £299.00 = £850.00 (matches starting float)', 'B1: Valid reverse operation check')
                ],
                'final_answer': '(a) Remaining balance = £551.00 | (b) Check: £551.00 + £299.00 = £850.00',
                'tutor_tip': "Always write down the full check equation with the answer after the equals sign. Stating 'I checked it' gets zero marks."
            },
            {
                'title': 'Model 2 (Level 2 Decision): Medical Warehouse Stock Audit & Re-Order Threshold',
                'marks': '4 Marks (Pearson Edexcel Level 2 Problem Solving)',
                'context': 'Supply Chain Inventory Control',
                'question': 'A central medical stores warehouse starts Monday with <strong>4,000 boxes</strong> of sterile surgical gloves. During the week, dispatches and deliveries occur:<br>• Monday dispatch: <strong>1,285 boxes</strong> sent to hospitals.<br>• Wednesday dispatch: <strong>940 boxes</strong> sent to clinics.<br>• Thursday delivery: <strong>650 new boxes</strong> received from manufacturer.<br>• Friday dispatch: <strong>1,195 boxes</strong> sent to care homes.<br><br>Procurement rules state an emergency order must be triggered if Friday\'s closing stock falls below <strong>1,250 boxes</strong>. Must an emergency order be triggered?',
                'steps': [
                    ('Step 1', 'Sum all outgoing dispatches across the week', '1,285 + 940 + 1,195 = 3,420 boxes dispatched.', 'M1: Total outgoing stock addition'),
                    ('Step 2', 'Calculate total available stock (opening stock + Thursday delivery)', '4,000 + 650 = 4,650 boxes available.', 'M1: Combining opening stock and incoming delivery'),
                    ('Step 3', 'Subtract total dispatches from total available stock', '4,650 - 3,420 = 1,230 boxes remaining on Friday.', 'M1: Accurate closing stock subtraction'),
                    ('Step 4', 'Compare against 1,250 threshold and state decision', '1,230 boxes < 1,250 boxes (short by 20 boxes). Yes, an emergency order must be triggered.', 'A1: Correct decision with exact stock figure (1,230)')
                ],
                'final_answer': 'Yes, trigger emergency order (Closing stock is 1,230 boxes, which is 20 boxes below the 1,250 minimum threshold).',
                'tutor_tip': 'Grouping all additions (4,000 + 650) and all subtractions (1,285 + 940 + 1,195) first is much less error-prone than alternating plus and minus.'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Subtracting Smaller Top Digit from Larger Bottom Digit',
                'desc': 'When computing 0 - 6 in column subtraction, students often mistakenly write 6 instead of borrowing 1 from the column to the left.',
                'fix': 'Remember: If the top digit is smaller than the bottom digit, you MUST borrow from the left.'
            }
        ],
        'practice_questions': [
            {
                'marks': '3 Marks',
                'question': 'A delivery depot had <strong>1,200 litres</strong> of diesel in its bulk tank. Over 3 days, drivers drew <strong>345 L, 280 L, and 415 L</strong>.<br>(a) How many litres remain in the tank?<br>(b) Show a reverse check of your working.',
                'solution_steps': '1. Total used = 345 + 280 + 415 = 1,040 litres.<br>2. Remaining = 1,200 - 1,040 = 160 litres.<br>3. Reverse check: 160 + 1,040 = 1,200 litres.',
                'correct_answer': '(a) 160 litres | (b) Check: 160 + 1,040 = 1,200 L',
                'tutor_tip': 'Include units (litres) in your final statement.'
            },
            {
                'marks': '2 Marks',
                'question': 'Without a calculator, work out <strong>6,004 - 2,758</strong>.',
                'solution_steps': '1. Borrow from 6 thousands across the two zeros: 6,004 becomes 5 thousands, 9 hundreds, 9 tens, 14 units.<br>2. Subtract column by column: 14 - 8 = 6; 9 - 5 = 4; 9 - 7 = 2; 5 - 2 = 3.<br>3. Result = 3,246.',
                'correct_answer': '3,246',
                'tutor_tip': 'Check by adding back: 3,246 + 2,758 = 6,004.'
            },
            {
                'marks': '3 Marks',
                'question': 'A charity fundraising account holds <strong>£3,420.50</strong>. It receives two donations of <strong>£685.75</strong> and <strong>£1,140.00</strong>, then pays venue hire of <strong>£890.40</strong>. Calculate the final account balance.',
                'solution_steps': '1. Total after donations = £3,420.50 + £685.75 + £1,140.00 = £5,246.25.<br>2. Subtract venue hire = £5,246.25 - £890.40 = £4,355.85.',
                'correct_answer': '£4,355.85',
                'tutor_tip': 'Keep two decimal places throughout for currency calculations.'
            }
        ]
    },
    {
        'filename': 'functional-skills-multiplication.html',
        'clean_topic': 'Multiplication & Scaling',
        'intro_lead': 'Master long multiplication (grid method and standard column method), multiply decimals, scale quantities, and solve multi-tier pricing problems under non-calculator conditions.',
        'next_file': 'functional-skills-division.html',
        'next_name': 'Division',
        'spec_points': [
            ('L1.3 / L2.3', 'Multiply whole numbers and decimals up to 2 decimal places by whole numbers and decimals.'),
            ('L1.7', 'Estimate and check answers using rounding.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-hashtag',
                'title': 'Golden Rule 1: The Total Decimal Places Rule',
                'desc': 'When multiplying decimals, count the total number of decimal places in BOTH numbers. Multiply as whole numbers, then put that exact total number of decimal places back into the answer.',
                'badge': '2.4 (1 dp) × 0.15 (2 dp) = 0.360 (3 dp) = 0.36'
            },
            {
                'icon': 'fa-table-cells',
                'title': 'Golden Rule 2: Grid Method Eliminates Carrying Errors',
                'desc': 'If column multiplication confuses you with carried digits, use the grid (box) method to partition numbers by tens and units before summing.',
                'badge': 'Partition: (30 + 4) × (20 + 7) = 600 + 210 + 80 + 28 = 918'
            }
        ],
        'skills': [
            {
                'title': 'Skill 1: The Partition Grid Method for Multi-Digit Numbers',
                'summary': 'Breaking 2-digit by 2-digit multiplications into four simple mental products.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:center;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">×</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">40</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">6</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Row Sum</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">30</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">1,200</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">180</td>
                        <td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">1,380</td>
                      </tr>
                      <tr>
                        <td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">5</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">200</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">30</td>
                        <td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">230</td>
                      </tr>
                      <tr style="background:#e0f2fe; font-weight:800; color:#0369a1;">
                        <td colspan="3" style="padding:10px; border:1px solid #cbd5e1; text-align:right;">Grand Total (46 × 35):</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">1,610</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                'title': 'Skill 2: Standard Column Multiplication & The Tens Row Zero',
                'summary': 'How to avoid the classic missing-zero error in two-line vertical multiplication.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">To compute <strong>138 × 24</strong> vertically:</p>
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Row 1 (Multiply by 4 units):</strong> <code>138 × 4 = 552</code>.</li>
                    <li><strong>Row 2 (Multiply by 2 tens = 20):</strong> Write down a <strong>0</strong> in the units column FIRST, then compute <code>138 × 2 = 276</code> &rarr; <code>2,760</code>.</li>
                    <li><strong>Add both rows:</strong> <code>552 + 2,760 = 3,312</code>.</li>
                  </ol>
                </div>
                """
            },
            {
                'title': 'Skill 3: Multiplying Decimals Without a Calculator',
                'summary': 'Strip the decimal points, multiply whole numbers, and count back total decimal places.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">Example: Work out <strong>3.6 × 0.25</strong></p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li>Count decimal digits in question: <code>3.6</code> (1 d.p.) + <code>0.25</code> (2 d.p.) = <strong>3 decimal places total</strong>.</li>
                    <li>Multiply as whole integers: <code>36 × 25 = 900</code>.</li>
                    <li>Count 3 places back from the right of 900: <code>0.900 = 0.9</code>.</li>
                  </ul>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Model 1 (Level 1 Foundation): Hospital Uniform Procurement Order (Non-Calculator)',
                'marks': '3 Marks (Pearson Edexcel Level 1/2 Non-Calculator)',
                'context': 'NHS Healthcare Staff Uniforms',
                'question': 'A care home orders <strong>48 tunic sets</strong> at a cost of <strong>£26.50</strong> each.<br>Calculate the total cost of the order without using a calculator.',
                'steps': [
                    ('Step 1', 'Partition or convert decimal to whole number multiplication', 'Multiply £26 × 48 and £0.50 × 48 separately (or 265 × 48 ÷ 10).', 'M1: Valid non-calculator multiplication method'),
                    ('Step 2', 'Compute the partial products', '48 × 20 = 960; 48 × 6 = 288; 48 × 0.50 = 24.<br>Sum = 960 + 288 + 24 = 1,272.', 'M1: Accurate partial products'),
                    ('Step 3', 'Format as currency to 2 decimal places', 'Total Cost = £1,272.00', 'A1: Accurate final currency answer')
                ],
                'final_answer': 'Total Cost = £1,272.00',
                'tutor_tip': 'Multiplying by £0.50 is simply halving the number (half of 48 is £24)!'
            },
            {
                'title': 'Model 2 (Level 2 Decision): Catering Shift Payroll & Budget Verification',
                'marks': '4 Marks (Pearson Edexcel Level 2 Problem Solving)',
                'context': 'Hospitality Staffing Budget',
                'question': 'An events manager has a weekend staffing budget of <strong>£2,100</strong>.<br>She employs:<br>• <strong>12 catering assistants</strong> working <strong>8.5 hours</strong> each at <strong>£12.40 per hour</strong>.<br>• <strong>4 shift supervisors</strong> working <strong>9.5 hours</strong> each at <strong>£16.50 per hour</strong>.<br><br>Is the £2,100 budget sufficient to cover the total weekend wage bill? Show full working.',
                'steps': [
                    ('Step 1', 'Calculate total hours and pay for catering assistants', 'Total assistant hours = 12 × 8.5 = 102 hours.<br>Assistant pay = 102 × £12.40 = £1,264.80.', 'M1: Assistant hours and wage calculation'),
                    ('Step 2', 'Calculate total hours and pay for shift supervisors', 'Total supervisor hours = 4 × 9.5 = 38 hours.<br>Supervisor pay = 38 × £16.50 = £627.00.', 'M1: Supervisor hours and wage calculation'),
                    ('Step 3', 'Sum total weekend wage bill', '£1,264.80 + £627.00 = £1,891.80.', 'M1: Total payroll summation'),
                    ('Step 4', 'Compare with £2,100 budget and conclude', '£1,891.80 < £2,100. Yes, the budget is sufficient with £208.20 remaining.', 'A1: Correct decision with £1,891.80 and £208.20 surplus')
                ],
                'final_answer': 'Yes, sufficient (Total wage bill is £1,891.80, which is £208.20 under the £2,100 budget).',
                'tutor_tip': 'Multiply the number of workers by the hours per worker first (12 × 8.5 = 102 whole hours) to eliminate a decimal before multiplying by the hourly rate!'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Forgetting the Zero in the Tens Row',
                'desc': 'In long column multiplication, when multiplying by the tens digit, you MUST put a 0 in the units column before multiplying.',
                'fix': "Always drop a '0' as your placeholder before multiplying by the tens digit."
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'A logistics operative works <strong>37.5 hours</strong> per week at an hourly rate of <strong>£14.00</strong>. Calculate their gross weekly pay without a calculator.',
                'solution_steps': '1. 37.5 × 14 = (37.5 × 10) + (37.5 × 4)<br>2. 375 + 150 = £525.00.',
                'correct_answer': '£525.00',
                'tutor_tip': 'Multiplying by 14 can be simplified into multiplying by 10 then by 4 and summing.'
            },
            {
                'marks': '2 Marks',
                'question': 'Without using a calculator, work out <strong>4.8 × 0.35</strong>.',
                'solution_steps': '1. Count decimal places: 4.8 (1 dp) + 0.35 (2 dp) = 3 dp total.<br>2. Multiply whole numbers: 48 × 35 = (48 × 30) + (48 × 5) = 1,440 + 240 = 1,680.<br>3. Restore 3 decimal places: 1.680 = 1.68.',
                'correct_answer': '1.68',
                'tutor_tip': '1,680 with 3 decimal places becomes 1.680, which simplifies to 1.68.'
            },
            {
                'marks': '3 Marks',
                'question': 'A conference centre sets up <strong>28 circular tables</strong>, each seating <strong>12 guests</strong>, and <strong>15 rectangular tables</strong>, each seating <strong>8 guests</strong>. Each guest meal costs the organisers <strong>£15.00</strong>. Calculate the total catering cost if every seat is filled.',
                'solution_steps': '1. Circular seats = 28 × 12 = 336 guests; Rectangular seats = 15 × 8 = 120 guests.<br>2. Total guests = 336 + 120 = 456 guests.<br>3. Total cost = 456 × £15 = (456 × 10) + (456 × 5) = £4,560 + £2,280 = £6,840.00.',
                'correct_answer': '£6,840.00',
                'tutor_tip': 'To multiply by 15 quickly without a calculator, multiply by 10 and add half of that result.'
            }
        ]
    },
    {
        'filename': 'functional-skills-division.html',
        'clean_topic': 'Division & Remainders',
        'intro_lead': 'Perform short and long bus-stop division, interpret remainders in practical vocational contexts (rounding up vs rounding down), and convert fractional remainders to decimals.',
        'next_file': 'functional-skills-bidmas.html',
        'next_name': 'BIDMAS / Order of Operations',
        'spec_points': [
            ('L1.3 / L2.3', 'Divide whole numbers and decimals by whole numbers up to 2-digit divisors.'),
            ('L1.8 / L2.4', 'Interpret remainders appropriately depending on context (e.g. packaging crates, transport minibuses).')
        ],
        'golden_rules': [
            {
                'icon': 'fa-van-shuttle',
                'title': 'Golden Rule 1: Practical Context Dictates How You Treat Remainders',
                'desc': 'If booking minibuses, buying paint tins, or ordering tile packs, you MUST round UP so nothing is left behind or uncovered. If calculating how many complete boxes can be filled or items afforded on a fixed budget, round DOWN.',
                'badge': 'People / Tins / Packs → Round UP | Complete Boxes / Affordability → Round DOWN'
            },
            {
                'icon': 'fa-circle-dot',
                'title': 'Golden Rule 2: Turn Remainders into Decimals with .00',
                'desc': 'To convert a remainder into an exact decimal or money figure, place a decimal point and add trailing zeros (.00) to the dividend under the bus stop.',
                'badge': '£145 ÷ 4 = 145.00 ÷ 4 = £36.25'
            }
        ],
        'skills': [
            {
                'title': 'Skill 1: The Short Division Bus-Stop Method with Decimals',
                'summary': 'Dividing step-by-step with carrying and trailing decimal zeros.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">To calculate <strong>£518 ÷ 4</strong> without a calculator:</p>
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li>4 into 5 goes <strong>1</strong> time, remainder 1 (carry 1 to make 11).</li>
                    <li>4 into 11 goes <strong>2</strong> times (8), remainder 3 (carry 3 to make 38).</li>
                    <li>4 into 38 goes <strong>9</strong> times (36), remainder 2. Add decimal point and trailing zeros: <code>.00</code> (carry 2 to make 20).</li>
                    <li>4 into 20 goes <strong>5</strong> times, 0 into 0. Result: <strong>£129.50</strong>.</li>
                  </ol>
                </div>
                """
            },
            {
                'title': 'Skill 2: Dividing by 2-Digit Numbers Using Chunking / Multiples List',
                'summary': 'Failsafe method for non-calculator division by numbers like 15, 16, or 24.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">Before dividing by a 2-digit divisor (e.g. <strong>432 ÷ 18</strong>), write a quick multiples ladder in the margin:</p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><code>1 × 18 = 18</code> | <code>2 × 18 = 36</code> | <code>4 × 18 = 72</code> | <code>10 × 18 = 180</code> | <code>20 × 18 = 360</code></li>
                    <li>Subtract the largest chunk: <code>432 - 360 (20 × 18) = 72 remaining</code>.</li>
                    <li>Spot the remaining chunk: <code>72 = 4 × 18</code>.</li>
                    <li>Combine chunks: <code>20 + 4 = 24</code>.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Skill 3: Contextual Remainder Decision Matrix (Round Up vs Round Down)',
                'summary': 'How to score the final accuracy mark on contextual division problems.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:left;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Workplace Scenario</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Raw Division</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Correct Action</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Final Answer</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:8px; border:1px solid #cbd5e1;">Minibuses for 142 patients (16 seats)</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;"><code>142 ÷ 16 = 8.875</code></td>
                        <td style="padding:8px; border:1px solid #cbd5e1; color:#dc2626; font-weight:700;">Round UP (cannot leave 14 behind)</td>
                        <td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">9 minibuses</td>
                      </tr>
                      <tr>
                        <td style="padding:8px; border:1px solid #cbd5e1;">Full boxes of 12 from 490 bottles</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;"><code>490 ÷ 12 = 40.833</code></td>
                        <td style="padding:8px; border:1px solid #cbd5e1; color:#0284c7; font-weight:700;">Round DOWN (only full boxes count)</td>
                        <td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">40 full boxes</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Model 1 (Level 1 Foundation): Patient Transport Booking Logistics',
                'marks': '3 Marks (Pearson Edexcel Level 1/2)',
                'context': 'Hospital Patient Shuttle Service',
                'question': 'An NHS outpatient centre needs to transport <strong>142 patients</strong> to an off-site clinic. Each patient shuttle minibus carries a maximum of <strong>16 passengers</strong>.<br>(a) How many minibuses must be booked?<br>(b) How many empty seats will be on the final minibus?',
                'steps': [
                    ('Step 1', 'Divide total patients by bus capacity', '142 ÷ 16 = 8 remainder 14 (or 8.875)', 'M1: Division setup'),
                    ('Step 2', 'Interpret remainder in practical transport context', '8 buses carry 128 passengers, leaving 14 patients stranded. Therefore, 9 minibuses must be booked.', 'A1: Correctly rounding UP to 9 buses'),
                    ('Step 3', 'Calculate empty seats on final minibus', 'Total capacity: 9 × 16 = 144 seats.<br>Empty seats: 144 - 142 = 2 empty seats (or 16 - 14 = 2).', 'B1: Correct empty seat calculation')
                ],
                'final_answer': '(a) 9 minibuses must be booked | (b) 2 empty seats on the final minibus.',
                'tutor_tip': 'In passenger transport problems, you can NEVER leave patients behind. You must always round up to the next whole vehicle.'
            },
            {
                'title': 'Model 2 (Level 2 Decision): Pharmaceutical Tablet Blister Pack Production Run',
                'marks': '4 Marks (Pearson Edexcel Level 2 Problem Solving)',
                'context': 'Pharmaceutical Packaging Line',
                'question': 'A pharmaceutical batch produces <strong>15,500 paracetamol caplets</strong>.<br>• Each blister strip holds <strong>16 caplets</strong>.<br>• Every carton holds <strong>6 complete blister strips</strong>.<br>• A hospital pharmacy orders <strong>160 cartons</strong>.<br><br>Does this single batch produce enough complete cartons to fulfil the hospital order?',
                'steps': [
                    ('Step 1', 'Calculate total caplets required per carton', '16 caplets/strip × 6 strips/carton = 96 caplets per carton.', 'M1: Caplets per carton calculation'),
                    ('Step 2', 'Divide total batch caplets by caplets per carton', '15,500 ÷ 96 = 161.458... cartons.', 'M1: Division of batch total by 96'),
                    ('Step 3', 'Round down to complete cartons and find leftover caplets', 'Only 161 complete cartons can be packed (161 × 96 = 15,456 caplets used; 44 left over).', 'M1: Contextual rounding down to 161 complete cartons'),
                    ('Step 4', 'Compare against 160-carton order and conclude', '161 complete cartons > 160 cartons ordered. Yes, the batch is sufficient with 1 complete carton (and 44 loose caplets) to spare.', 'A1: Valid conclusion supported by 161 complete cartons')
                ],
                'final_answer': 'Yes, sufficient (Produces 161 complete cartons, exceeding the 160-carton order by 1 carton).',
                'tutor_tip': 'You can also check by multiplying: 160 cartons × 96 caplets = 15,360 caplets needed, which is less than 15,500!'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Writing Decimal Remainders for Indivisible Units',
                'desc': "Answering '8.875 minibuses' earns zero marks for the final answer because you cannot book 0.875 of a vehicle.",
                'fix': 'Always round to a whole integer when dealing with people, vehicles, or physical packaging.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'A factory produces <strong>490 bottles</strong> of hand sanitizer. The bottles are packed into shipping boxes of <strong>12 bottles</strong> each. How many complete boxes can be shipped, and how many bottles are left over?',
                'solution_steps': '1. 490 ÷ 12 = 40 remainder 10 (since 40 × 12 = 480).<br>2. Complete boxes = 40; Leftover bottles = 10.',
                'correct_answer': '40 complete boxes (10 bottles left over)',
                'tutor_tip': "Notice the question asks for 'complete boxes', so here you round DOWN to 40."
            },
            {
                'marks': '2 Marks',
                'question': 'Six colleagues win a syndicate prize of <strong>£813</strong> and split it equally. How much does each person receive? Give your answer in pounds and pence.',
                'solution_steps': '1. Set up short division with decimals: 813.00 ÷ 6.<br>2. 813 ÷ 6 = 135 remainder 3; 3.00 ÷ 6 = 0.50.<br>3. Each colleague receives £135.50.',
                'correct_answer': '£135.50',
                'tutor_tip': 'Always include the trailing zero (£135.50, never £135.5).'
            },
            {
                'marks': '3 Marks',
                'question': 'A decorator needs to tile a clinic wall with an area of <strong>26 m²</strong>. Tiles are sold in boxes that cover <strong>1.5 m²</strong> each and cost <strong>£24.00 per box</strong>. Calculate the total cost of the boxes required.',
                'solution_steps': '1. Number of boxes = 26 ÷ 1.5 = 260 ÷ 15 = 17.333... boxes.<br>2. Round UP to 18 whole boxes so the wall is fully tiled.<br>3. Total cost = 18 × £24.00 = £432.00.',
                'correct_answer': '£432.00 (18 boxes)',
                'tutor_tip': 'Rounding down to 17 boxes would only cover 25.5 m², leaving 0.5 m² bare!'
            }
        ]
    },
    {
        'filename': 'functional-skills-bidmas.html',
        'clean_topic': 'BIDMAS / Order of Operations',
        'intro_lead': 'Apply the standard mathematical hierarchy of operations (Brackets, Indices, Division, Multiplication, Addition, Subtraction) to solve multi-stage financial and clinical calculations.',
        'next_file': 'functional-skills-rounding-and-estimating.html',
        'next_name': 'Rounding & Estimating',
        'spec_points': [
            ('L1.5 / L2.5', 'Follow the correct order of operations including brackets, powers, and roots in practical workplace calculations.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-arrow-down-1-9',
                'title': 'Golden Rule 1: Multiplication and Division Have Equal Precedence',
                'desc': 'Multiplication does NOT automatically come before Division. Work from left to right when both appear in an expression. The same applies to Addition and Subtraction.',
                'badge': 'Brackets → Indices → (Division & Multiplication) → (Addition & Subtraction)'
            },
            {
                'icon': 'fa-calculator',
                'title': 'Golden Rule 2: Brackets Group Multi-Part Formulas',
                'desc': 'Whenever calculating an average or total cost with discounts, calculate what is inside the brackets FIRST before multiplying or dividing.',
                'badge': '(£120 + £80) × 0.85 = £200 × 0.85 = £170'
            }
        ],
        'skills': [
            {
                'title': 'Skill 1: The BIDMAS Hierarchy Breakdown',
                'summary': 'The 4-tier priority system explained step-by-step.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>B – Brackets:</strong> Resolve everything inside <code>( )</code> first.</li>
                    <li><strong>I – Indices / Powers &amp; Roots:</strong> Calculate squares (<code>x²</code>), cubes (<code>x³</code>), and square roots (<code>√</code>).</li>
                    <li><strong>D &amp; M – Division and Multiplication:</strong> Equal priority — compute from <strong>left to right</strong> as they appear.</li>
                    <li><strong>A &amp; S – Addition and Subtraction:</strong> Equal priority — compute from <strong>left to right</strong> as they appear.</li>
                  </ol>
                </div>
                """
            },
            {
                'title': 'Skill 2: Handling Indices (Squares, Cubes) and Hidden Fraction Brackets',
                'summary': 'How to evaluate powers and horizontal fraction bars accurately.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Squares vs Doubling:</strong> <code>5² = 5 × 5 = 25</code> (NEVER <code>5 × 2 = 10</code>). Similarly, <code>4³ = 4 × 4 × 4 = 64</code>.</li>
                    <li><strong>Horizontal Division Bars Have Invisible Brackets:</strong> In <code>(18 + 12) ÷ (9 - 4)</code>, work out the entire top (<code>30</code>) and entire bottom (<code>5</code>) first before dividing: <code>30 ÷ 5 = 6</code>.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Skill 3: Left-to-Right Rule for Equal-Priority Operations',
                'summary': 'Preventing the classic subtraction-after-addition trap.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:left;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Expression</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Common Trap (Wrong)</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Correct Left-to-Right Method</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;"><code>30 - 12 + 8</code></td>
                        <td style="padding:8px; border:1px solid #cbd5e1; color:#dc2626;">Doing 12 + 8 = 20 first &rarr; 30 - 20 = 10</td>
                        <td style="padding:8px; border:1px solid #cbd5e1; color:#166534; font-weight:700;"><code>(30 - 12) + 8 = 18 + 8 = 26</code></td>
                      </tr>
                      <tr>
                        <td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;"><code>40 ÷ 5 × 2</code></td>
                        <td style="padding:8px; border:1px solid #cbd5e1; color:#dc2626;">Doing 5 × 2 = 10 first &rarr; 40 ÷ 10 = 4</td>
                        <td style="padding:8px; border:1px solid #cbd5e1; color:#166534; font-weight:700;"><code>(40 ÷ 5) × 2 = 8 × 2 = 16</code></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Model 1 (Level 1 Foundation): Overtime Payroll & Deductions Calculation (Non-Calculator)',
                'marks': '3 Marks (Pearson Edexcel Level 1/2 Non-Calculator)',
                'context': 'Payroll & Benefits Accounting',
                'question': "A healthcare assistant's gross pay formula is given as:<br><strong>Pay = 450 + 15 × (40 - 32) - 60</strong><br>Calculate the final pay value using the correct order of operations.",
                'steps': [
                    ('Step 1', 'Resolve Brackets first: (40 - 32)', '40 - 32 = 8. Formula becomes: 450 + 15 × 8 - 60.', 'M1: Correct bracket resolution'),
                    ('Step 2', 'Perform Multiplication before addition/subtraction', '15 × 8 = 120. Formula becomes: 450 + 120 - 60.', 'M1: Multiplication precedence'),
                    ('Step 3', 'Perform Addition and Subtraction from left to right', '450 + 120 = 570<br>570 - 60 = 510', 'A1: Accurate final answer')
                ],
                'final_answer': 'Final Pay = £510.00',
                'tutor_tip': 'If you added 450 + 15 first (= 465), you would obtain an erroneous answer of 3,660! Always follow BIDMAS.'
            },
            {
                'title': 'Model 2 (Level 2 Decision): Industrial Workshop Energy Consumption Tariff Formula',
                'marks': '4 Marks (Pearson Edexcel Level 2 Problem Solving)',
                'context': 'Commercial Utility Billing',
                'question': 'A workshop manager calculates daily electricity cost (£) using the formula:<br><strong>Cost = 25 + 0.15 × (4 × 5² + 20)</strong><br>The manager claims the daily electricity cost is under <strong>£40.00</strong>.<br>Evaluate the formula step-by-step without a calculator to determine if the manager is correct.',
                'steps': [
                    ('Step 1', 'Evaluate the index inside the bracket first: 5²', '5² = 5 × 5 = 25.<br>Bracket becomes: (4 × 25 + 20).', 'M1: Evaluating index 5² = 25'),
                    ('Step 2', 'Complete multiplication then addition inside the bracket', '4 × 25 = 100; 100 + 20 = 120.<br>Expression becomes: Cost = 25 + 0.15 × 120.', 'M1: Resolving bracket to 120'),
                    ('Step 3', 'Multiply before adding', '0.15 × 120 = 18.<br>Cost = 25 + 18 = £43.00.', 'M1: Correct multiplication and addition'),
                    ('Step 4', 'Compare against £40.00 claim', '£43.00 > £40.00. No, the manager is incorrect; the daily cost is £43.00, which is £3.00 over £40.00.', 'A1: Accurate value (£43.00) and clear conclusion')
                ],
                'final_answer': 'No, incorrect (Daily cost is £43.00, which exceeds £40.00 by £3.00).',
                'tutor_tip': 'Inside brackets, BIDMAS still applies! In (4 × 5² + 20), do the power (25), then multiply by 4 (100), then add 20 (120).'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Reading Left to Right Without Respecting Precedence',
                'desc': 'Computing 5 + 3 × 4 as 8 × 4 = 32 is incorrect. The multiplication MUST happen first: 3 × 4 = 12, then 5 + 12 = 17.',
                'fix': 'Underline all multiplication and division pairs before doing any addition or subtraction.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'Evaluate: <strong>24 ÷ (8 - 2) + 3² × 2</strong> without a calculator.',
                'solution_steps': '1. Brackets: (8 - 2) = 6.<br>2. Indices: 3² = 9.<br>3. Expression: 24 ÷ 6 + 9 × 2.<br>4. Division & Mult: 24 ÷ 6 = 4; 9 × 2 = 18.<br>5. Addition: 4 + 18 = 22.',
                'correct_answer': '22',
                'tutor_tip': 'Resolve brackets and indices on your first line of working.'
            },
            {
                'marks': '2 Marks',
                'question': 'Work out the value of: <strong>50 - 6 × (3 + 4) + 12</strong>.',
                'solution_steps': '1. Brackets: (3 + 4) = 7.<br>2. Multiplication: 6 × 7 = 42.<br>3. Left-to-right subtraction then addition: 50 - 42 + 12 = 8 + 12 = 20.',
                'correct_answer': '20',
                'tutor_tip': 'Do NOT add 42 + 12 first! Calculate 50 - 42 = 8, then add 12 to get 20.'
            },
            {
                'marks': '3 Marks',
                'question': 'Insert brackets into the statement below to make it mathematically true:<br><strong>18 + 6 ÷ 4 - 1 = 8</strong>',
                'solution_steps': '1. Target answer is 8. Notice that 24 ÷ 3 = 8.<br>2. Group the numerator (18 + 6) = 24 and denominator (4 - 1) = 3.<br>3. Check: (18 + 6) ÷ (4 - 1) = 24 ÷ 3 = 8.',
                'correct_answer': '(18 + 6) ÷ (4 - 1) = 8',
                'tutor_tip': 'Test factor pairs of the target number (e.g. 24 ÷ 3 = 8) to spot where brackets belong.'
            }
        ]
    },
    {
        'filename': 'functional-skills-rounding-and-estimating.html',
        'clean_topic': 'Rounding & Estimating',
        'intro_lead': 'Round whole numbers and decimals to significant figures, decimal places, and nearest tens/hundreds, and use front-end estimation to verify workplace calculations.',
        'next_file': 'functional-skills-fractions.html',
        'next_name': 'Fractions',
        'spec_points': [
            ('L1.6 / L2.6', 'Round numbers to a given power of 10, specified decimal places, or significant figures.'),
            ('L1.7 / L2.7', 'Estimate answers to multi-step calculations by rounding each value to 1 significant figure.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-hand-peace',
                'title': "Golden Rule 1: The '5 or More Round Up' Rule",
                'desc': 'Look at the decider digit immediately to the right of your target column. If it is 5, 6, 7, 8, or 9, round UP. If 0, 1, 2, 3, or 4, keep the target digit the same.',
                'badge': '0–4: Stay the Same | 5–9: Round UP by 1'
            },
            {
                'icon': 'fa-bullseye',
                'title': 'Golden Rule 2: 1 Significant Figure for Exam Estimations',
                'desc': "Whenever an exam question begins with 'Use estimation to check...' or 'Estimate the value of...', round EVERY number to 1 significant figure BEFORE performing any calculation.",
                'badge': 'Estimate: 489 × 3.12 ≈ 500 × 3 = 1,500'
            }
        ],
        'skills': [
            {
                'title': 'Skill 1: Decimal Places vs Significant Figures Comparison',
                'summary': 'Clarifying the two major rounding conventions in Level 1 and Level 2.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Original Value</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0284c7;">To 1 Decimal Place (1 dp)</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">To 1 Significant Figure (1 sf)</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#ea580c;">To 2 Significant Figures (2 sf)</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">47.86</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">47.9</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">50</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">48</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">0.0482</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">0.0</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">0.05</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">0.048</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">3,849</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">3,849.0</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">4,000</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">3,800</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                'title': 'Skill 2: Estimating Complex Calculations by Rounding to 1 s.f.',
                'summary': 'How to score full marks on estimation checks without doing long multiplication.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">To estimate <strong><code>(58.7 × 19.4) ÷ 0.48</code></strong>:</p>
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li>Round each number to 1 significant figure: <code>58.7 &rarr; 60</code>; <code>19.4 &rarr; 20</code>; <code>0.48 &rarr; 0.5</code>.</li>
                    <li>Write the rounded calculation clearly to secure the [M1] mark: <code>(60 × 20) ÷ 0.5</code>.</li>
                    <li>Compute numerator: <code>60 × 20 = 1,200</code>.</li>
                    <li>Divide by <code>0.5</code> (remember dividing by 0.5 doubles the number): <code>1,200 ÷ 0.5 = 2,400</code>.</li>
                  </ol>
                </div>
                """
            },
            {
                'title': 'Skill 3: Identifying Overestimates vs Underestimates',
                'summary': 'Explaining how rounding direction affects your estimated answer.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Overestimate:</strong> Occurs when you round both multiplied numbers <strong>UP</strong> (e.g. <code>194 × £4.85 &rarr; 200 × £5 = £1,000</code>; actual is £940.90).</li>
                    <li><strong>Underestimate:</strong> Occurs when you round both multiplied numbers <strong>DOWN</strong> (e.g. <code>312 × £2.15 &rarr; 300 × £2 = £600</code>; actual is £670.80).</li>
                  </ul>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Model 1 (Level 1 Foundation): Hospital Catering Supply Estimation (Non-Calculator)',
                'marks': '3 Marks (Pearson Edexcel Level 1/2 Non-Calculator)',
                'context': 'Healthcare Food Services Procurement',
                'question': 'The catering manager orders <strong>194 cartons</strong> of meal trays at <strong>£4.85</strong> each.<br>(a) Show an estimate of the total expenditure by rounding each value to 1 significant figure.<br>(b) State whether your estimate is an underestimate or overestimate, giving a reason.',
                'steps': [
                    ('Step 1', 'Round each value to 1 significant figure', '194 rounds to 200 (1 sf)<br>£4.85 rounds to £5.00 (1 sf)', 'M1: Rounding both values to 1 sf'),
                    ('Step 2', 'Compute estimated total', '200 × £5 = £1,000', 'A1: Correct estimated product (£1,000)'),
                    ('Step 3', 'Analyze whether overestimate or underestimate', 'Both numbers were rounded UP (194 → 200 and 4.85 → 5.00); therefore, £1,000 is an OVERESTIMATE.', 'B1: Valid comparative justification')
                ],
                'final_answer': '(a) Estimate = £1,000 | (b) Overestimate, because both 194 and £4.85 were rounded up.',
                'tutor_tip': 'If you calculate the exact answer (194 × 4.85 = £940.90) and then round that to £1,000, you score ZERO for step 1. You must round BEFORE multiplying.'
            },
            {
                'title': 'Model 2 (Level 2 Decision): Surgical Clinic Flooring Renovation Quote Check',
                'marks': '4 Marks (Pearson Edexcel Level 2 Problem Solving)',
                'context': 'Estates & Facilities Cost Verification',
                'question': 'A clinic room measures <strong>7.85 m long</strong> by <strong>4.12 m wide</strong>. Non-slip clinical vinyl flooring costs <strong>£29.50 per m²</strong>, plus a fixed fitting fee of <strong>£185.00</strong>.<br>The contractor quotes <strong>£1,148.20</strong>. Use estimation (rounding each figure to 1 significant figure) to check if the contractor\'s quote is sensible.',
                'steps': [
                    ('Step 1', 'Round room dimensions and unit cost to 1 significant figure', 'Length: 7.85 m ≈ 8 m | Width: 4.12 m ≈ 4 m | Cost/m²: £29.50 ≈ £30 | Fitting: £185 ≈ £200.', 'M1: Rounding values to 1 s.f.'),
                    ('Step 2', 'Calculate estimated floor area and material cost', 'Estimated Area = 8 m × 4 m = 32 m².<br>Estimated Vinyl Cost = 32 × £30 = £960.', 'M1: Area and material estimation'),
                    ('Step 3', 'Add estimated fitting fee', 'Total Estimated Cost = £960 + £200 = £1,160.', 'A1: Correct estimated total (£1,160)'),
                    ('Step 4', 'Compare estimate with contractor quote', '£1,160 is very close to the £1,148.20 quote. Yes, the contractor\'s quote is sensible.', 'B1: Valid comparison and confirmation')
                ],
                'final_answer': 'Estimated total = £1,160 (Yes, the £1,148.20 quote is sensible as it is very close to £1,160).',
                'tutor_tip': 'In Pearson Edexcel "Use estimation to check" questions, writing down the rounded numbers (8 × 4 × 30 + 200) is mandatory for full marks.'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Calculating Exact Value Before Rounding in Estimation Questions',
                'desc': 'Exam boards require you to demonstrate that you can estimate WITHOUT doing complex multi-digit arithmetic.',
                'fix': 'Always write down the rounded numbers first (e.g. 200 × 5) before calculating anything.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'Use 1 significant figure approximation to estimate the value of: <strong>(38.4 × 9.75) ÷ 0.48</strong>.',
                'solution_steps': '1. Round each to 1 sf: 38.4 ≈ 40; 9.75 ≈ 10; 0.48 ≈ 0.5.<br>2. Compute: (40 × 10) ÷ 0.5 = 400 ÷ 0.5 = 800.',
                'correct_answer': '800',
                'tutor_tip': 'Dividing by 0.5 is equivalent to multiplying by 2 (400 ÷ 0.5 = 800).'
            },
            {
                'marks': '2 Marks',
                'question': 'Round <strong>14,682.739</strong> to:<br>(a) 2 decimal places<br>(b) 2 significant figures.',
                'solution_steps': '1. (a) Look at 3rd decimal digit (9 ≥ 5): rounds .739 up to .74 &rarr; 14,682.74.<br>2. (b) Look at 3rd significant digit (6 ≥ 5): rounds 14,000 up to 15,000.',
                'correct_answer': '(a) 14,682.74 | (b) 15,000',
                'tutor_tip': 'When rounding whole numbers to 2 s.f., remember to keep placeholder zeros so 14,682 becomes 15,000 (NOT 15)!'
            },
            {
                'marks': '3 Marks',
                'question': 'A charity event sells <strong>392 tickets</strong> at <strong>£19.80</strong> each. Expenses are <strong>£1,895</strong>. Estimate the net profit by rounding each number to 1 significant figure.',
                'solution_steps': '1. Round to 1 sf: 392 ≈ 400 tickets; £19.80 ≈ £20; £1,895 ≈ £2,000.<br>2. Estimated revenue = 400 × £20 = £8,000.<br>3. Estimated net profit = £8,000 - £2,000 = £6,000.',
                'correct_answer': '£6,000',
                'tutor_tip': 'Show the rounded figures (400, £20, £2,000) clearly on your first line.'
            }
        ]
    },
    {
        'filename': 'functional-skills-fractions.html',
        'clean_topic': 'Fractions: Operations & Fractions of Amounts',
        'intro_lead': 'Add, subtract, multiply, and divide proper and mixed fractions, find fractions of workplace amounts, and convert improper fractions into mixed numbers.',
        'next_file': 'functional-skills-decimals.html',
        'next_name': 'Decimals',
        'spec_points': [
            ('L1.9 / L2.8', 'Find fractions of whole number quantities or measurements.'),
            ('L2.9', 'Add, subtract, multiply, and divide proper and mixed fractions.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-divide',
                'title': 'Golden Rule 1: Fraction of an Amount: Divide by Bottom, Multiply by Top',
                'desc': 'To find 3/8 of £480: divide £480 by 8 (denominator = £60), then multiply by 3 (numerator = £180).',
                'badge': 'Amount ÷ Denominator × Numerator'
            },
            {
                'icon': 'fa-rotate',
                'title': 'Golden Rule 2: Dividing Fractions: Keep, Change, Flip (KCF)',
                'desc': 'Keep the first fraction, Change division (÷) to multiplication (×), and Flip the second fraction upside down (its reciprocal).',
                'badge': 'Keep • Change • Flip (KCF)'
            }
        ],
        'skills': [
            {
                'title': 'Skill 1: Finding a Fraction of an Amount & Expressing One Number as a Fraction of Another',
                'summary': 'Essential Level 1 and Level 2 workplace fraction calculations.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Fraction of an Amount (Divide by Bottom, Times by Top):</strong> To find <code>5/9 of £630</code> &rarr; <code>£630 ÷ 9 = £70</code>, then <code>£70 × 5 = £350</code>.</li>
                    <li><strong>Finding the Original Whole (Reverse Fraction):</strong> If <code>3/5</code> of a budget is <code>£240</code>, divide by top (<code>£240 ÷ 3 = £80</code> for 1/5) and multiply by bottom (<code>£80 × 5 = £400</code> total).</li>
                    <li><strong>Simplifying Ratios/Fractions:</strong> Divide top and bottom by their Highest Common Factor (e.g. <code>45/60 ÷ 15/15 = 3/4</code>).</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Skill 2: Adding & Subtracting Fractions with Common Denominators',
                'summary': 'Finding the Lowest Common Multiple (LCM) before adding or subtracting.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">To calculate <strong><code>2 3/4 - 1 2/5</code></strong>:</p>
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Convert Mixed Numbers to Improper Fractions:</strong> <code>2 3/4 = 11/4</code> and <code>1 2/5 = 7/5</code>.</li>
                    <li><strong>Find Common Denominator (LCM of 4 and 5 is 20):</strong> <code>11/4 = 55/20</code> and <code>7/5 = 28/20</code>.</li>
                    <li><strong>Subtract Numerators Only:</strong> <code>(55 - 28)/20 = 27/20</code>.</li>
                    <li><strong>Convert Back to Mixed Number:</strong> <code>27 ÷ 20 = 1 remainder 7 &rarr; 1 7/20</code>.</li>
                  </ol>
                </div>
                """
            },
            {
                'title': 'Skill 3: Multiplying, Dividing (KCF) & Improper Fractions',
                'summary': 'Fast rules for multiplying numerators/denominators and Keep-Change-Flip.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:left;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Operation</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Method Rule</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Worked Example</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">Multiplication</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">Top × Top over Bottom × Bottom</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;"><code>3/4 × 2/5 = 6/20 = 3/10</code></td>
                      </tr>
                      <tr>
                        <td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">Division (KCF)</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">Keep 1st, Change ÷ to ×, Flip 2nd</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;"><code>3/4 ÷ 2/5 = 3/4 × 5/2 = 15/8 = 1 7/8</code></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Model 1 (Level 1 Foundation): Care Home Staffing Shift Allocation',
                'marks': '3 Marks (Pearson Edexcel Level 1/2)',
                'context': 'Residential Care Staff Scheduling',
                'question': 'A residential care provider employs <strong>72 care workers</strong>. On night duty, <strong>3/8</strong> of the workforce are deployed. Of the <strong>remaining</strong> staff, <strong>2/3</strong> work the day shift, and the rest are on scheduled leave.<br>How many staff members are on scheduled leave?',
                'steps': [
                    ('Step 1', 'Calculate staff on night duty (3/8 of 72)', '72 ÷ 8 = 9<br>9 × 3 = 27 staff on night shift', 'M1: Fraction of amount calculation'),
                    ('Step 2', 'Calculate remaining staff and day shift workers', 'Remaining staff = 72 - 27 = 45 staff.<br>Day shift = 2/3 of 45: (45 ÷ 3) × 2 = 15 × 2 = 30 staff.', 'M1: Subtraction and second fraction step'),
                    ('Step 3', 'Calculate staff on scheduled leave', '45 - 30 = 15 staff on scheduled leave.', 'A1: Accurate final staff count')
                ],
                'final_answer': '15 care workers on scheduled leave',
                'tutor_tip': "Always read carefully whether the second fraction applies to the 'original total' or the 'remaining staff'. Here it was of the remaining staff."
            },
            {
                'title': 'Model 2 (Level 2 Decision): Hospital Land Allocation & Car Park Expansion',
                'marks': '4 Marks (Pearson Edexcel Level 2 Problem Solving)',
                'context': 'Healthcare Estates Planning',
                'question': 'A hospital redevelops a <strong>240-space</strong> staff car park:<br>• <strong>1/6</strong> of spaces are reserved for emergency doctors.<br>• <strong>3/8</strong> of the total spaces are allocated to nursing staff.<br>• <strong>1/5</strong> of the total spaces are converted into electric vehicle (EV) bays.<br>• All remaining spaces are available for general visitors.<br><br>The estates director requires at least <strong>65 spaces</strong> for general visitors. Does this plan meet the requirement?',
                'steps': [
                    ('Step 1', 'Calculate spaces for emergency doctors and nursing staff', 'Doctors (1/6 of 240) = 240 ÷ 6 = 40 spaces.<br>Nurses (3/8 of 240) = (240 ÷ 8) × 3 = 30 × 3 = 90 spaces.', 'M1: First two fractional allocations'),
                    ('Step 2', 'Calculate spaces for EV bays', 'EV bays (1/5 of 240) = 240 ÷ 5 = 48 spaces.', 'M1: Third fractional allocation'),
                    ('Step 3', 'Subtract allocated spaces from 240 total', 'Allocated = 40 + 90 + 48 = 178 spaces.<br>General visitor spaces = 240 - 178 = 62 spaces.', 'M1: Remaining visitor space calculation'),
                    ('Step 4', 'Compare against 65-space requirement', '62 spaces < 65 spaces (3 spaces short). No, the plan does not meet the director\'s requirement.', 'A1: Accurate conclusion supported by 62 spaces')
                ],
                'final_answer': 'No (Only 62 visitor spaces remain, which is 3 spaces short of the 65-space target).',
                'tutor_tip': 'Because all three fractions are taken from the total 240 spaces, calculate each fraction directly from 240 and subtract their sum.'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Adding Denominators Together',
                'desc': 'Adding 1/4 + 1/4 = 2/8 is wrong! When denominators are identical, only add numerators: 1/4 + 1/4 = 2/4 = 1/2.',
                'fix': 'Never add or subtract denominators; only add or subtract numerators over a common denominator.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'Calculate <strong>1 3/5 + 2 1/4</strong>, giving your answer as a mixed number in its simplest form.',
                'solution_steps': '1. Common denominator for 5 and 4 is 20: 3/5 = 12/20; 1/4 = 5/20.<br>2. Add whole numbers: 1 + 2 = 3.<br>3. Add fractions: 12/20 + 5/20 = 17/20.<br>4. Combine: 3 17/20.',
                'correct_answer': '3 17/20',
                'tutor_tip': 'Keep whole numbers and fractions separate when adding to avoid large improper numerators.'
            },
            {
                'marks': '2 Marks',
                'question': 'Work out <strong>2 1/4 ÷ 3/5</strong> without a calculator. Give your answer as a mixed number in its simplest form.',
                'solution_steps': '1. Convert mixed number to improper fraction: 2 1/4 = 9/4.<br>2. Apply Keep-Change-Flip (KCF): 9/4 × 5/3 = 45/12.<br>3. Simplify by dividing by 3: 15/4 = 3 3/4.',
                'correct_answer': '3 3/4',
                'tutor_tip': 'Always convert mixed numbers into improper fractions BEFORE multiplying or dividing!'
            },
            {
                'marks': '3 Marks',
                'question': 'A charity grant of <strong>£1,800</strong> is split between three youth projects. Project A receives <strong>4/9</strong> of the grant, Project B receives <strong>1/3</strong> of the grant, and Project C receives the rest. How much money does Project C receive?',
                'solution_steps': '1. Project A = (1,800 ÷ 9) × 4 = 200 × 4 = £800.<br>2. Project B = 1,800 ÷ 3 = £600.<br>3. Project C = 1,800 - (800 + 600) = £400.',
                'correct_answer': '£400',
                'tutor_tip': 'Check: 4/9 + 3/9 = 7/9, leaving 2/9 for Project C (2/9 of £1,800 = £400).'
            }
        ]
    },
    {
        'filename': 'functional-skills-decimals.html',
        'clean_topic': 'Decimals: Four Operations & Place Value',
        'intro_lead': 'Perform addition, subtraction, multiplication, and division with decimals, round monetary figures to 2 decimal places, and solve real-world invoicing problems.',
        'next_file': 'functional-skills-percentages.html',
        'next_name': 'Percentages',
        'spec_points': [
            ('L1.10 / L2.10', 'Read, write, order and compare decimals up to three decimal places.'),
            ('L1.11 / L2.10', 'Perform the four operations with decimals up to two decimal places in practical contexts.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-sterling-sign',
                'title': 'Golden Rule 1: Always Write Money to 2 Decimal Places',
                'desc': 'In Functional Skills, writing £14.5 or £14.500 loses the final accuracy mark. Currency in pounds must ALWAYS have exactly 2 decimal places (£14.50).',
                'badge': 'Mandatory: £14.50 (NOT £14.5)'
            },
            {
                'icon': 'fa-calculator',
                'title': 'Golden Rule 2: Dividing by Decimals: Shift the Decimal Point',
                'desc': 'Never divide by a decimal divisor. Multiply both numbers by 10, 100, or 1,000 to turn the divisor into a whole number before using the bus stop.',
                'badge': '£18 ÷ 0.25 = £1,800 ÷ 25 = 72'
            }
        ],
        'skills': [
            {
                'title': 'Skill 1: Aligning Decimals for Column Addition & Subtraction',
                'summary': 'Preventing positional errors during decimal arithmetic.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">To calculate <strong>£142.60 - £58.45</strong>:</p>
                  <table style="width:240px; border-collapse:collapse; font-family:monospace; font-size:1.15rem; text-align:right;">
                    <tr><td style="padding:4px;">142.60</td></tr>
                    <tr style="border-bottom:2px solid #0f172a;"><td style="padding:4px;">- 58.45</td></tr>
                    <tr style="font-weight:800; color:#0284c7;"><td style="padding:4px;">£84.15</td></tr>
                  </table>
                  <p style="margin-top:10px; color:#475569; font-size:0.92rem;">Always pad whole numbers or 1-decimal-place numbers with trailing zeros (e.g. write <code>£19</code> as <code>19.00</code>) before subtracting.</p>
                </div>
                """
            },
            {
                'title': 'Skill 2: Multiplying Decimals & Restoring Decimal Places',
                'summary': 'How to multiply rates and weights with 1, 2, or 3 decimal places.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li>Ignore the decimal points and multiply the digits as whole numbers (e.g. for <code>2.45 × 1.2</code>, calculate <code>245 × 12 = 2,940</code>).</li>
                    <li>Count total digits after the decimal point in the original numbers (<code>.45</code> has 2 digits + <code>.2</code> has 1 digit = <strong>3 digits total</strong>).</li>
                    <li>Move the decimal point 3 places left from the end of <code>2940</code> &rarr; <code>2.940 = 2.94</code>.</li>
                  </ol>
                </div>
                """
            },
            {
                'title': 'Skill 3: Dividing by a Decimal (Equivalent Fraction Scaling)',
                'summary': 'Turning any decimal division into a straightforward whole-number division.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:left;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Decimal Division</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Scale Both Numbers By</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Equivalent Whole Division</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;"><code>14.4 ÷ 0.6</code></td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">× 10 (1 d.p. in divisor)</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;"><code>144 ÷ 6 = 24</code></td>
                      </tr>
                      <tr>
                        <td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;"><code>4.5 ÷ 0.15</code></td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">× 100 (2 d.p. in divisor)</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;"><code>450 ÷ 15 = 30</code></td>
                      </tr>
                      <tr>
                        <td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;"><code>3.6 ÷ 0.009</code></td>
                        <td style="padding:8px; border:1px solid #cbd5e1;">× 1,000 (3 d.p. in divisor)</td>
                        <td style="padding:8px; border:1px solid #cbd5e1;"><code>3,600 ÷ 9 = 400</code></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Model 1 (Level 1 Foundation): NHS Pharmacy Prescription Fluid Dilution',
                'marks': '3 Marks (Pearson Edexcel Level 1/2 Non-Calculator)',
                'context': 'Clinical Pharmacy Fluid Dispensing',
                'question': 'A clinical pharmacist has <strong>4.5 litres</strong> of sterile saline solution. She dispenses the solution into dose ampoules containing <strong>0.15 litres</strong> each.<br>How many complete dose ampoules can she fill?',
                'steps': [
                    ('Step 1', 'Set up the decimal division', '4.5 ÷ 0.15', 'M1: Division setup'),
                    ('Step 2', 'Multiply dividend and divisor by 100 to remove decimal in divisor', '4.5 × 100 = 450<br>0.15 × 100 = 15<br>Calculation becomes: 450 ÷ 15', 'M1: Decimal shift method'),
                    ('Step 3', 'Perform integer division', '450 ÷ 15 = 30 ampoules', 'A1: Accurate whole number answer')
                ],
                'final_answer': '30 complete dose ampoules',
                'tutor_tip': 'Notice how shifting the decimal point by two places turns an intimidating decimal problem into basic mental arithmetic (450 ÷ 15 = 30).'
            },
            {
                'title': 'Model 2 (Level 2 Decision): Medical Courier Fleet Mileage & Fuel Reimbursement',
                'marks': '4 Marks (Pearson Edexcel Level 2 Problem Solving)',
                'context': 'Healthcare Transport Expenses',
                'question': 'A pathology courier drives <strong>42.8 miles</strong> on Monday, <strong>38.65 miles</strong> on Tuesday, and <strong>53.55 miles</strong> on Wednesday.<br>• Her van uses <strong>0.08 litres</strong> of diesel per mile.<br>• Diesel costs <strong>£1.45 per litre</strong>.<br>• The hospital reimburses her at a flat rate of <strong>£0.15 per mile</strong>.<br><br>Does the hospital mileage reimbursement cover her actual diesel cost for these three days? Show exact figures.',
                'steps': [
                    ('Step 1', 'Calculate total mileage across the 3 days', '42.80 + 38.65 + 53.55 = 135.00 miles.', 'M1: Accurate decimal addition of miles'),
                    ('Step 2', 'Calculate total diesel used and actual fuel cost', 'Diesel used = 135 × 0.08 = 10.8 litres.<br>Actual fuel cost = 10.8 × £1.45 = £15.66.', 'M1: Fuel consumption and cost calculation'),
                    ('Step 3', 'Calculate hospital mileage reimbursement', 'Reimbursement = 135 miles × £0.15 = £20.25.', 'M1: Reimbursement calculation'),
                    ('Step 4', 'Compare reimbursement against actual cost', '£20.25 > £15.66 (surplus of £4.59). Yes, the reimbursement covers her diesel cost with £4.59 to spare.', 'A1: Correct decision with both exact currency figures')
                ],
                'final_answer': 'Yes (Reimbursement is £20.25 vs actual diesel cost of £15.66, leaving a £4.59 surplus).',
                'tutor_tip': 'Align the decimal points carefully when adding 42.80 + 38.65 + 53.55 so you spot that the hundredths (.80 + .65 + .55 = 2.00) sum to a clean whole number (135 miles).'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Dropping the Trailing Zero at the End of Currency',
                'desc': 'Writing £3.4 on an invoice instead of £3.40 will forfeit the accuracy mark on Pearson Edexcel marking schemes.',
                'fix': 'Always review money answers and ensure exactly two digits follow the decimal point.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'A parcel courier charges <strong>£6.50</strong> for the first kilogram, plus <strong>£1.85</strong> for each additional kilogram. Calculate the cost to deliver a <strong>7 kg</strong> package.',
                'solution_steps': '1. Additional kilograms = 7 - 1 = 6 kg.<br>2. Additional cost = 6 × £1.85 = £11.10.<br>3. Total cost = £6.50 + £11.10 = £17.60.',
                'correct_answer': '£17.60',
                'tutor_tip': "Don't forget to subtract the first 1 kg before multiplying by £1.85."
            },
            {
                'marks': '2 Marks',
                'question': 'Without a calculator, work out <strong>18.9 ÷ 0.07</strong>.',
                'solution_steps': '1. Multiply both numbers by 100 to clear the 2 decimal places in 0.07: 1,890 ÷ 7.<br>2. 1,890 ÷ 7 = 270.',
                'correct_answer': '270',
                'tutor_tip': 'Check using inverse multiplication: 270 × 0.07 = 18.9.'
            },
            {
                'marks': '3 Marks',
                'question': 'A laboratory technician has a <strong>2.5 litre</strong> bottle of reagent. She uses <strong>0.375 litres</strong> for Test A, <strong>0.85 litres</strong> for Test B, and fills <strong>4 sample tubes</strong> with <strong>0.125 litres</strong> each. How much reagent remains in the bottle?',
                'solution_steps': '1. Sample tubes = 4 × 0.125 = 0.500 litres.<br>2. Total used = 0.375 + 0.850 + 0.500 = 1.725 litres.<br>3. Remaining = 2.500 - 1.725 = 0.775 litres.',
                'correct_answer': '0.775 litres',
                'tutor_tip': 'Pad 2.5 to 2.500 and 0.85 to 0.850 so all numbers have 3 decimal places.'
            }
        ]
    },
    {
        'filename': 'functional-skills-fractions-decimals-and-percentages.html',
        'clean_topic': 'Fractions, Decimals & Percentages (FDP Conversions)',
        'intro_lead': 'Convert seamlessly between fractions, decimals, and percentages, compare values in different formats, and solve equivalence problems under exam conditions.',
        'next_file': 'functional-skills-ratio.html',
        'next_name': 'Ratio & Proportion',
        'spec_points': [
            ('L1.12 / L2.11', 'Recognise and use equivalences between common fractions, decimals, and percentages.'),
            ('L2.12', 'Order and compare fractions, decimals, and percentages across mixed representations.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-arrows-rotate',
                'title': 'Golden Rule 1: The FDP Conversion Triangle',
                'desc': 'Percentage to Decimal: Divide by 100. Decimal to Percentage: Multiply by 100. Fraction to Decimal: Top divided by Bottom.',
                'badge': 'Fraction → (Top ÷ Bottom) → Decimal → (× 100) → Percentage'
            },
            {
                'icon': 'fa-list-ol',
                'title': 'Golden Rule 2: Convert All to Decimals or Percentages Before Ordering',
                'desc': 'When asked to compare mixed values (e.g. 3/8, 0.35, 36%), convert EVERY value into a percentage or 3-digit decimal before comparing.',
                'badge': '3/8 = 37.5% | 0.35 = 35% | 36% = 36% → 0.35 < 36% < 3/8'
            }
        ],
        'skills': [
            {
                'title': 'Skill 1: Benchmark FDP Equivalences to Memorize',
                'summary': 'The high-frequency conversions that appear in every Functional Skills paper.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:center;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Fraction</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Decimal</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Percentage</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">1/2</td><td style="padding:6px; border:1px solid #cbd5e1;">0.5</td><td style="padding:6px; border:1px solid #cbd5e1;">50%</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">1/4 &bull; 3/4</td><td style="padding:6px; border:1px solid #cbd5e1;">0.25 &bull; 0.75</td><td style="padding:6px; border:1px solid #cbd5e1;">25% &bull; 75%</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">1/5 &bull; 2/5 &bull; 3/5 &bull; 4/5</td><td style="padding:6px; border:1px solid #cbd5e1;">0.2 &bull; 0.4 &bull; 0.6 &bull; 0.8</td><td style="padding:6px; border:1px solid #cbd5e1;">20% &bull; 40% &bull; 60% &bull; 80%</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">1/8 &bull; 3/8 &bull; 5/8 &bull; 7/8</td><td style="padding:6px; border:1px solid #cbd5e1;">0.125 &bull; 0.375 &bull; 0.625 &bull; 0.875</td><td style="padding:6px; border:1px solid #cbd5e1;">12.5% &bull; 37.5% &bull; 62.5% &bull; 87.5%</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">1/3 &bull; 2/3</td><td style="padding:6px; border:1px solid #cbd5e1;">0.333... &bull; 0.666...</td><td style="padding:6px; border:1px solid #cbd5e1;">33.3% &bull; 66.7%</td></tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                'title': 'Skill 2: Converting Any Fraction to a Percentage (Scaling vs Bus-Stop)',
                'summary': 'Two reliable methods depending on whether the denominator divides into 100.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Method A (Scale Denominator to 100):</strong> If the denominator is a factor of 100 (2, 4, 5, 10, 20, 25, 50), multiply top and bottom to make the denominator 100: <code>17/25 = (17 × 4)/(25 × 4) = 68/100 = 68%</code>.</li>
                    <li><strong>Method B (Numerator ÷ Denominator × 100):</strong> For denominators like 8 or 16, divide top by bottom using short division: <code>5/8 = 5.000 ÷ 8 = 0.625 = 62.5%</code>.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Skill 3: Converting Decimals & Percentages Back to Simplest Fractions',
                'summary': 'Writing over 10, 100, or 1,000 and cancelling common factors.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>2-Digit Decimal / Percentage:</strong> Write over 100 and divide by HCF: <code>0.36 = 36% = 36/100 &rarr; (÷ 4) = 9/25</code>.</li>
                    <li><strong>3-Digit Decimal:</strong> Write over 1,000 and simplify: <code>0.375 = 375/1000 &rarr; (÷ 125) = 3/8</code>.</li>
                  </ol>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Model 1 (Level 1 Foundation): Hospital Ward Hand Hygiene Audit Comparison',
                'marks': '3 Marks (Pearson Edexcel Level 1/2)',
                'context': 'Infection Prevention Compliance',
                'question': 'Three hospital wards reported their staff hand hygiene compliance rates:<br>• Ward A: <strong>4/5</strong><br>• Ward B: <strong>78%</strong><br>• Ward C: <strong>0.82</strong><br>(a) Convert all three scores to percentages.<br>(b) Which ward achieved the highest compliance score?',
                'steps': [
                    ('Step 1', 'Convert Ward A (4/5) to a percentage', '4/5 = 8/10 = 80/100 = 80% (or 4 ÷ 5 × 100 = 80%)', 'M1: Fraction to percentage conversion'),
                    ('Step 2', 'Convert Ward C (0.82) to a percentage', '0.82 × 100 = 82%', 'M1: Decimal to percentage conversion'),
                    ('Step 3', 'Compare all three percentage scores', 'Ward A = 80%, Ward B = 78%, Ward C = 82%. Since 82% > 80% > 78%, Ward C achieved the highest compliance.', 'A1: Correct comparison and conclusion')
                ],
                'final_answer': '(a) Ward A: 80%, Ward B: 78%, Ward C: 82% | (b) Ward C achieved the highest compliance.',
                'tutor_tip': 'Converting to percentages makes comparison immediate and avoids fractional common denominator complications.'
            },
            {
                'title': 'Model 2 (Level 2 Decision): Retail Supplier Discount Offer Evaluation',
                'marks': '4 Marks (Pearson Edexcel Level 2 Problem Solving)',
                'context': 'Commercial Purchasing Comparison',
                'question': 'A dental practice needs to order £600 worth of examination gloves. Three suppliers have identical list prices (£600) but offer different promotional reductions:<br>• <strong>Supplier X:</strong> <strong>3/8</strong> off the list price.<br>• <strong>Supplier Y:</strong> <strong>36%</strong> discount off the list price.<br>• <strong>Supplier Z:</strong> Pay only <strong>0.62</strong> of the list price.<br><br>Which supplier offers the largest saving, and how much will the practice pay with that supplier?',
                'steps': [
                    ('Step 1', 'Convert all three offers into comparable discount percentages', 'Supplier X discount: 3/8 = 0.375 = 37.5% off.<br>Supplier Y discount: 36% off.<br>Supplier Z: Paying 0.62 (62%) means a discount of 100% - 62% = 38% off.', 'M1: Converting all three offers to a common discount format'),
                    ('Step 2', 'Identify the supplier with the largest discount', 'Compare discounts: 38% (Supplier Z) > 37.5% (Supplier X) > 36% (Supplier Y).<br>Supplier Z gives the largest saving.', 'M1: Correct comparison identifying Supplier Z'),
                    ('Step 3', 'Calculate final amount payable with Supplier Z', '£600 × 0.62 = £372.00 (a saving of £228.00).', 'M1: Calculating exact cost with winning supplier'),
                    ('Step 4', 'State final conclusion clearly', 'Supplier Z offers the largest saving (38% off), and the practice will pay £372.00.', 'A1: Correct supplier and £372.00 payable')
                ],
                'final_answer': 'Supplier Z offers the largest saving (38% discount vs 37.5% and 36%), with a final price payable of £372.00.',
                'tutor_tip': 'Read wording traps carefully! Supplier Z says "Pay 0.62 of the price" (meaning 62% paid = 38% discount), whereas X and Y quote the discount directly.'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Confusing 0.05 with 50%',
                'desc': '0.05 = 5%, whereas 0.5 = 50%. A common error is assuming 0.05 is 50% because of the digit 5.',
                'fix': 'Always multiply the decimal by 100: 0.05 × 100 = 5%.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'Arrange in ascending order (smallest to largest): <strong>0.62, 3/5, 65%, 5/8</strong>.',
                'solution_steps': '1. Convert all to 3-digit decimals: 0.620; 3/5 = 0.600; 65% = 0.650; 5/8 = 0.625.<br>2. Sequence: 0.600 (3/5), 0.620 (0.62), 0.625 (5/8), 0.650 (65%).',
                'correct_answer': '3/5, 0.62, 5/8, 65%',
                'tutor_tip': 'Write the final answer using the original representations given in the question.'
            },
            {
                'marks': '2 Marks',
                'question': 'Convert <strong>44%</strong> into a fraction in its simplest form, and convert <strong>13/20</strong> into a percentage.',
                'solution_steps': '1. 44% = 44/100. Divide top and bottom by 4 = 11/25.<br>2. 13/20 = (13 × 5)/(20 × 5) = 65/100 = 65%.',
                'correct_answer': '44% = 11/25 | 13/20 = 65%',
                'tutor_tip': 'Always check if your fraction can be divided further by 2, 4, or 5.'
            },
            {
                'marks': '3 Marks',
                'question': 'In a staff survey of <strong>160 employees</strong>, <strong>35%</strong> travel by train, <strong>3/8</strong> travel by car, and the rest cycle. What decimal proportion of the staff cycle, and how many employees is this?',
                'solution_steps': '1. Train = 35% = 0.35; Car = 3/8 = 0.375.<br>2. Combined train + car = 0.35 + 0.375 = 0.725.<br>3. Cycle decimal = 1 - 0.725 = 0.275 (27.5%).<br>4. Number of cyclists = 0.275 × 160 = 44 employees.',
                'correct_answer': '0.275 (44 employees)',
                'tutor_tip': 'All proportions of a whole group must add up to 1 (or 100%).'
            }
        ]
    }
]
