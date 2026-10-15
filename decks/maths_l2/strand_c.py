"""Strand C: Handling Information and Data (Cards 37-50)"""
CARDS = [ { 'answer_text': 'Ordered: 8, 11, 14, 14, 19, 22, 27 (7 numbers). Middle is 4th number = 14 (Median). Range = 27 - 8 '
                   '= 19.',
    'challenge_prompt': 'Find the median and range of this dataset: 14, 8, 22, 19, 14, 27, 11.',
    'dfe_code': 'DfE L2.HD34',
    'golden_rule': 'Range is a measure of consistency/spread, NEVER an average!',
    'id': 'm-l2-37',
    'level': 'l2',
    'level_label': 'Level 2',
    'number': 37,
    'rule_body': 'Mean = Sum of values ÷ Count. Median = Middle value after ordering low to high. Mode = Most frequent '
                 'value. Range = Highest - Lowest (spread, NOT an average).',
    'rule_heading': 'The 4 Core Statistics',
    'strand_name': 'Handling Data',
    'strand_theme': 'purple',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(30, 15)">\n'
                '            <rect x="0" y="0" width="190" height="65" rx="6" fill="#eff6ff" stroke="#3b82f6"/>\n'
                '            <text x="95" y="24" font-size="12" font-weight="800" fill="#1e40af" '
                'text-anchor="middle">MEAN = Total ÷ Count</text>\n'
                '            <text x="95" y="48" font-size="10.5" font-weight="700" fill="#475569" '
                'text-anchor="middle">Add all up and share equally</text>\n'
                '          </g>\n'
                '          <g transform="translate(240, 15)">\n'
                '            <rect x="0" y="0" width="190" height="65" rx="6" fill="#f0fdf4" stroke="#16a34a"/>\n'
                '            <text x="95" y="24" font-size="12" font-weight="800" fill="#15803d" '
                'text-anchor="middle">MEDIAN = Middle Value</text>\n'
                '            <text x="95" y="48" font-size="10.5" font-weight="700" fill="#475569" '
                'text-anchor="middle">MUST put in order first!</text>\n'
                '          </g>\n'
                '          <g transform="translate(30, 90)">\n'
                '            <rect x="0" y="0" width="190" height="65" rx="6" fill="#fdf2f8" stroke="#ec4899"/>\n'
                '            <text x="95" y="24" font-size="12" font-weight="800" fill="#9d174d" '
                'text-anchor="middle">MODE = Most Common</text>\n'
                '            <text x="95" y="48" font-size="10.5" font-weight="700" fill="#475569" '
                'text-anchor="middle">Number that appears most often</text>\n'
                '          </g>\n'
                '          <g transform="translate(240, 90)">\n'
                '            <rect x="0" y="0" width="190" height="65" rx="6" fill="#fffbeb" stroke="#f59e0b"/>\n'
                '            <text x="95" y="24" font-size="12" font-weight="800" fill="#b45309" '
                'text-anchor="middle">RANGE = High - Low</text>\n'
                '            <text x="95" y="48" font-size="10.5" font-weight="700" fill="#dc2626" '
                'text-anchor="middle">Spread of data (NOT an average!)</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Averages: Mean, Median, Mode &amp; Range',
    'watch_out': 'For the median with an even count of numbers, add the middle two and divide by 2.'},
  { 'answer_text': 'fx: (0×4) + (1×10) + (2×6) = 0 + 10 + 12 = 22. Total frequency Σf = 4 + 10 + 6 = 20. Mean = 22 ÷ '
                   '20 = 1.1 cars.',
    'challenge_prompt': 'Cars per household: 0 cars (f=4), 1 car (f=10), 2 cars (f=6). Calculate the mean number of '
                        'cars per household.',
    'dfe_code': 'DfE L2.HD35',
    'golden_rule': 'Divide by total frequency (Σf), NEVER by the number of rows in the table!',
    'id': 'm-l2-38',
    'level': 'l2',
    'level_label': 'Level 2',
    'number': 38,
    'rule_body': '1. Multiply value (x) by frequency (f) to make an fx column. 2. Sum the fx column (Total score Σfx). '
                 '3. Sum the frequency column (Total count Σf). 4. Divide: Σfx ÷ Σf.',
    'rule_heading': 'Mean = Σfx ÷ Σf',
    'strand_name': 'Handling Data',
    'strand_theme': 'purple',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(30, 20)">\n'
                '            <rect x="0" y="0" width="400" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" '
                'stroke-width="1.8"/>\n'
                '            <text x="70" y="26" font-size="11" font-weight="800" fill="#0f172a" '
                'text-anchor="middle">Score (x)</text>\n'
                '            <text x="170" y="26" font-size="11" font-weight="800" fill="#0f172a" '
                'text-anchor="middle">Freq (f)</text>\n'
                '            <text x="290" y="26" font-size="11" font-weight="800" fill="#2563eb" '
                'text-anchor="middle">x × f (fx)</text>\n'
                '            <line x1="20" y1="35" x2="380" y2="35" stroke="#cbd5e1"/>\n'
                '            <text x="70" y="55" font-size="11" font-weight="700" fill="#475569" '
                'text-anchor="middle">1</text><text x="170" y="55" font-size="11" font-weight="700" fill="#475569" '
                'text-anchor="middle">3</text><text x="290" y="55" font-size="11" font-weight="700" fill="#2563eb" '
                'text-anchor="middle">1 × 3 = 3</text>\n'
                '            <text x="70" y="75" font-size="11" font-weight="700" fill="#475569" '
                'text-anchor="middle">2</text><text x="170" y="75" font-size="11" font-weight="700" fill="#475569" '
                'text-anchor="middle">5</text><text x="290" y="75" font-size="11" font-weight="700" fill="#2563eb" '
                'text-anchor="middle">2 × 5 = 10</text>\n'
                '            <line x1="20" y1="90" x2="380" y2="90" stroke="#cbd5e1"/>\n'
                '            <text x="170" y="112" font-size="11" font-weight="800" fill="#059669" '
                'text-anchor="middle">Total f = 8</text>\n'
                '            <text x="290" y="112" font-size="11" font-weight="800" fill="#059669" '
                'text-anchor="middle">Total fx = 13</text>\n'
                '            <text x="70" y="112" font-size="11" font-weight="800" fill="#dc2626" '
                'text-anchor="middle">13 ÷ 8 = 1.625</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Mean from a Frequency Table',
    'watch_out': "Don't just average the 'x' column — that ignores how many times each value occurred."},
  { 'answer_text': 'Total (mp × f) = (5×2) + (15×6) + (25×2) = 10 + 90 + 50 = 150. Total f = 2 + 6 + 2 = 10. Estimated '
                   'Mean = 150 ÷ 10 = 15 mins.',
    'challenge_prompt': 'Times: 0–10 mins (f=2, mp=5), 10–20 mins (f=6, mp=15), 20–30 mins (f=2, mp=25). Calculate '
                        'estimated mean.',
    'dfe_code': 'DfE L2.HD36',
    'golden_rule': "It is an 'ESTIMATE' because the exact individual raw values inside the group are unknown!",
    'id': 'm-l2-39',
    'level': 'l2',
    'level_label': 'Level 2',
    'number': 39,
    'rule_body': '1. Find midpoint of each group: (Lower bound + Upper bound) ÷ 2. 2. Multiply midpoint by frequency '
                 '(mp × f). 3. Sum (mp × f). 4. Divide by total frequency.',
    'rule_heading': 'Midpoints × Frequency ÷ Total Frequency',
    'strand_name': 'Handling Data',
    'strand_theme': 'purple',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <rect x="30" y="20" width="400" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" '
                'stroke-width="1.8"/>\n'
                '          <text x="230" y="42" font-size="13" font-weight="800" fill="#0f172a" '
                'text-anchor="middle">Grouped Data: 10 &lt; t ≤ 20 (f = 4)</text>\n'
                '          <g transform="translate(60, 60)">\n'
                '            <text x="0" y="20" font-size="11" font-weight="700" fill="#2563eb">1. Midpoint = (10 + '
                '20) ÷ 2 = 15</text>\n'
                '            <text x="0" y="45" font-size="11" font-weight="700" fill="#059669">2. mp × f = 15 × 4 = '
                '60</text>\n'
                '            <text x="0" y="70" font-size="12" font-weight="800" fill="#0f172a">Estimated Mean = Total '
                '(mp × f) ÷ Total Frequency</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Estimated Mean (Grouped Data)',
    'watch_out': 'Be careful finding midpoints: for 0 to 10, midpoint is 5. For 20 to 50, midpoint is 35 (not 30).'},
  { 'answer_text': '(a) Modal class = £20k–£25k (highest frequency 12). (b) Total f = 20. Middle is 10.5th person. 5 '
                   'in 1st group, next 12 in 2nd group. Median group = £20k–£25k.',
    'challenge_prompt': 'Salaries: £15k–£20k (f=5), £20k–£25k (f=12), £25k–£30k (f=3). State: (a) Modal class, (b) '
                        'Median group.',
    'dfe_code': 'DfE L2.HD37',
    'golden_rule': 'Always write the ENTIRE interval inequality (e.g. 20 < t ≤ 30), not just one number!',
    'id': 'm-l2-40',
    'level': 'l2',
    'level_label': 'Level 2',
    'number': 40,
    'rule_body': 'Modal Class = The group interval with the HIGHEST frequency number. Median Group = The interval that '
                 'contains the middle position ((Total f + 1) ÷ 2).',
    'rule_heading': 'Identifying Class Intervals',
    'strand_name': 'Handling Data',
    'strand_theme': 'purple',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(30, 20)">\n'
                '            <rect x="0" y="0" width="190" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" '
                'stroke-width="1.8"/>\n'
                '            <text x="95" y="28" font-size="12" font-weight="800" fill="#1e40af" '
                'text-anchor="middle">MODAL CLASS</text>\n'
                '            <text x="95" y="58" font-size="11" font-weight="700" fill="#475569" '
                'text-anchor="middle">Look down frequency column</text>\n'
                '            <rect x="20" y="75" width="150" height="28" rx="4" fill="#3b82f6"/>\n'
                '            <text x="95" y="94" font-size="11" font-weight="800" fill="#ffffff" '
                'text-anchor="middle">HIGHEST Frequency</text>\n'
                '          </g>\n'
                '          <g transform="translate(240, 20)">\n'
                '            <rect x="0" y="0" width="190" height="130" rx="8" fill="#f0fdf4" stroke="#16a34a" '
                'stroke-width="1.8"/>\n'
                '            <text x="95" y="28" font-size="12" font-weight="800" fill="#15803d" '
                'text-anchor="middle">MEDIAN GROUP</text>\n'
                '            <text x="95" y="58" font-size="11" font-weight="700" fill="#475569" '
                'text-anchor="middle">Find position: (n + 1) ÷ 2</text>\n'
                '            <rect x="20" y="75" width="150" height="28" rx="4" fill="#16a34a"/>\n'
                '            <text x="95" y="94" font-size="11" font-weight="800" fill="#ffffff" '
                'text-anchor="middle">Cumulative Count</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Modal Class &amp; Median Group',
    'watch_out': 'The modal class is the interval itself, NOT the frequency count.'},
  { 'answer_text': '1. Shift 1 produced more units on average (mean of 45 vs 41). 2. Shift 2 was more consistent '
                   'because its range was smaller (range of 5 vs 12).',
    'challenge_prompt': 'Shift 1: Mean = 45 units, Range = 12. Shift 2: Mean = 41 units, Range = 5. Compare the two '
                        'shifts.',
    'dfe_code': 'DfE L2.HD38',
    'golden_rule': 'Smaller range = more consistent / reliable results!',
    'id': 'm-l2-41',
    'level': 'l2',
    'level_label': 'Level 2',
    'number': 41,
    'rule_body': 'To earn full marks on Pearson comparison questions, you MUST state: 1. One Average comparison in '
                 "context ('Branch A has a higher mean sales by £50'). 2. One Range/Spread comparison ('Branch B is "
                 "more consistent because its range is smaller').",
    'rule_heading': 'Average + Spread in Context',
    'strand_name': 'Handling Data',
    'strand_theme': 'purple',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
          <rect x="25" y="14" width="410" height="142" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
          <text x="230" y="36" font-size="12.5" font-weight="900" fill="#1e40af" text-anchor="middle">PEARSON GOLDEN 2-PART COMPARISON</text>
          <g transform="translate(42, 50)">
            <text x="0" y="20" font-size="10.5" font-weight="800" fill="#0f172a">1. AVERAGE: "Group A on average is higher because mean is..."</text>
            <text x="0" y="46" font-size="10.5" font-weight="800" fill="#0f172a">2. SPREAD: "Group B is more consistent because range is smaller..."</text>
            <text x="0" y="72" font-size="10" font-weight="700" fill="#dc2626">⚠️ Must mention numbers AND the real-world context!</text>
          </g>
</svg>""",
    'title': 'Comparing Two Data Sets',
    'watch_out': 'Always write comparison words (higher, lower, more consistent) in context!'},
  { 'answer_text': 'Total tokens = 5 + 7 + 8 = 20. Non-red tokens = 7 + 8 = 15. Probability = 15/20 = 3/4.',
    'challenge_prompt': 'A bag contains 5 red, 7 blue, and 8 green tokens. What is the probability of picking a token '
                        'that is NOT red? Give as a simplified fraction.',
    'dfe_code': 'DfE L2.HD39',
    'golden_rule': 'Probabilities can NEVER be greater than 1 or negative!',
    'id': 'm-l2-42',
    'level': 'l2',
    'level_label': 'Level 2',
    'number': 42,
    'rule_body': 'Probability is always between 0 (Impossible) and 1 (Certain). Can be written as a fraction, decimal, '
                 'or percentage. P(Not event) = 1 - P(Event).',
    'rule_heading': 'P(Event) = Favourable ÷ Total',
    'strand_name': 'Handling Data',
    'strand_theme': 'purple',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <line x1="40" y1="85" x2="420" y2="85" stroke="#334155" stroke-width="3"/>\n'
                '          <circle cx="40" cy="85" r="6" fill="#dc2626"/>\n'
                '          <text x="40" y="115" font-size="12" font-weight="800" fill="#dc2626" text-anchor="middle">0 '
                '(Impossible)</text>\n'
                '          <circle cx="230" cy="85" r="6" fill="#f59e0b"/>\n'
                '          <text x="230" y="115" font-size="12" font-weight="800" fill="#b45309" '
                'text-anchor="middle">0.5 (Even chance)</text>\n'
                '          <circle cx="420" cy="85" r="6" fill="#16a34a"/>\n'
                '          <text x="420" y="115" font-size="12" font-weight="800" fill="#15803d" '
                'text-anchor="middle">1 (Certain)</text>\n'
                '          <rect x="110" y="20" width="240" height="35" rx="6" fill="#eff6ff" stroke="#3b82f6"/>\n'
                '          <text x="230" y="42" font-size="12" font-weight="800" fill="#1e40af" text-anchor="middle">P '
                '= Favourable Outcomes ÷ Total</text>\n'
                '</svg>',
    'title': 'Probability of Single Events',
    'watch_out': "Don't write probability as a ratio (e.g. 1 : 4 is WRONG). Write as a fraction (1/5), decimal (0.2), "
                 'or % (20%).'},
  { 'answer_text': 'P(Both delayed) = 0.2 × 0.15 = 0.03 (or 3%).',
    'challenge_prompt': 'The probability that train A is delayed is 0.2. The probability that train B is delayed is '
                        '0.15. What is the probability that BOTH trains are delayed?',
    'dfe_code': 'DfE L2.HD40',
    'golden_rule': "'AND' means MULTIPLY; 'OR' means ADD!",
    'id': 'm-l2-43',
    'level': 'l2',
    'level_label': 'Level 2',
    'number': 43,
    'rule_body': "Independent events do not affect each other (e.g. flipping a coin and rolling a die). 'AND' rule = "
                 "MULTIPLY probabilities. 'OR' rule = ADD probabilities.",
    'rule_heading': 'P(A and B) = P(A) × P(B)',
    'strand_name': 'Handling Data',
    'strand_theme': 'purple',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <rect x="30" y="20" width="400" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" '
                'stroke-width="1.8"/>\n'
                '          <text x="230" y="45" font-size="14" font-weight="900" fill="#0f172a" '
                'text-anchor="middle">P(A and B) = P(A) × P(B)</text>\n'
                '          <g transform="translate(60, 65)">\n'
                '            <text x="0" y="20" font-size="12" font-weight="700" fill="#2563eb">Flipping Heads AND '
                'rolling a 6:</text>\n'
                '            <text x="0" y="45" font-size="12" font-weight="800" fill="#059669">P(Heads) = 1/2   •   '
                'P(Rolling a 6) = 1/6</text>\n'
                '            <text x="0" y="70" font-size="13" font-weight="900" fill="#1e40af">Combined: 1/2 × 1/6 = '
                '1/12</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Combined Independent Events',
    'watch_out': "Don't add when you need both to happen: 1/2 + 1/6 = 4/6 (which is much too high for both happening "
                 'together).'},
  { 'answer_text': 'P(Fails both) = (1 - 0.8) × (1 - 0.7) = 0.2 × 0.3 = 0.06. P(At least one pass) = 1 - 0.06 = 0.94 '
                   '(or 94%).',
    'challenge_prompt': 'A student has an 80% (0.8) chance of passing Theory, and a 70% (0.7) chance of passing '
                        'Practical. What is the probability of passing AT LEAST ONE test?',
    'dfe_code': 'DfE L2.HD41',
    'golden_rule': 'Every pair of branch splits MUST add up to 1 (100%)!',
    'id': 'm-l2-44',
    'level': 'l2',
    'level_label': 'Level 2',
    'number': 44,
    'rule_body': '1. Branches from any single node must add up to 1. 2. MULTIPLY along branches to find outcome '
                 'probability. 3. ADD individual outcome probabilities together if multiple paths satisfy the '
                 'question.',
    'rule_heading': 'Multiply Across, Add Down',
    'strand_name': 'Handling Data',
    'strand_theme': 'purple',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(40, 20)">\n'
                '            <line x1="20" y1="65" x2="100" y2="30" stroke="#334155" stroke-width="2"/>\n'
                '            <line x1="20" y1="65" x2="100" y2="100" stroke="#334155" stroke-width="2"/>\n'
                '            <text x="60" y="38" font-size="10" font-weight="800" fill="#2563eb">0.7</text>\n'
                '            <text x="60" y="98" font-size="10" font-weight="800" fill="#dc2626">0.3</text>\n'
                '            <text x="110" y="32" font-size="10" font-weight="800" fill="#0f172a">Pass</text>\n'
                '            <text x="110" y="104" font-size="10" font-weight="800" fill="#0f172a">Fail</text>\n'
                '            <line x1="140" y1="30" x2="220" y2="15" stroke="#334155" stroke-width="1.8"/>\n'
                '            <line x1="140" y1="30" x2="220" y2="45" stroke="#334155" stroke-width="1.8"/>\n'
                '            <text x="230" y="18" font-size="10" font-weight="700" fill="#059669">P, P = 0.7 × 0.7 = '
                '0.49</text>\n'
                '            <text x="230" y="48" font-size="10" font-weight="700" fill="#d97706">P, F = 0.7 × 0.3 = '
                '0.21</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Probability Tree Diagrams',
    'watch_out': 'Check whether picking is WITH replacement or WITHOUT replacement (fractions change on 2nd pick!).'},
  { 'answer_text': 'Men who walk = 12. Grand total = 80. Probability = 12/80 = 3/20 (or 0.15 / 15%).',
    'challenge_prompt': 'In a staff survey of 80 people (30 Men: 18 Bus, 12 Walk; 50 Women: 22 Bus, 28 Walk), what is '
                        'the probability that a random person is a man who walks to work?',
    'dfe_code': 'DfE L2.HD42',
    'golden_rule': 'Find the cell with only ONE missing number in its row or column first!',
    'id': 'm-l2-45',
    'level': 'l2',
    'level_label': 'Level 2',
    'number': 45,
    'rule_body': '1. Every row must add up to its row total. 2. Every column must add up to its column total. 3. Grand '
                 'total bottom-right must match both row totals and column totals.',
    'rule_heading': 'Row Totals + Column Totals',
    'strand_name': 'Handling Data',
    'strand_theme': 'purple',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(30, 15)">\n'
                '            <rect x="0" y="0" width="400" height="140" rx="8" fill="#f8fafc" stroke="#cbd5e1" '
                'stroke-width="1.8"/>\n'
                '            <line x1="0" y1="35" x2="400" y2="35" stroke="#cbd5e1"/>\n'
                '            <line x1="0" y1="70" x2="400" y2="70" stroke="#cbd5e1"/>\n'
                '            <line x1="0" y1="105" x2="400" y2="105" stroke="#cbd5e1"/>\n'
                '            <line x1="120" y1="0" x2="120" y2="140" stroke="#cbd5e1"/>\n'
                '            <line x1="210" y1="0" x2="210" y2="140" stroke="#cbd5e1"/>\n'
                '            <line x1="300" y1="0" x2="300" y2="140" stroke="#cbd5e1"/>\n'
                '            <text x="60" y="24" font-size="11" font-weight="800" fill="#0f172a">Group</text><text '
                'x="165" y="24" font-size="11" font-weight="800" fill="#0f172a">Bus</text><text x="255" y="24" '
                'font-size="11" font-weight="800" fill="#0f172a">Walk</text><text x="350" y="24" font-size="11" '
                'font-weight="900" fill="#1e40af">Total</text>\n'
                '            <text x="60" y="58" font-size="11" font-weight="700" fill="#475569">Men</text><text '
                'x="165" y="58" font-size="11" font-weight="700" fill="#475569">18</text><text x="255" y="58" '
                'font-size="11" font-weight="700" fill="#475569">12</text><text x="350" y="58" font-size="11" '
                'font-weight="800" fill="#0f172a">30</text>\n'
                '            <text x="60" y="92" font-size="11" font-weight="700" fill="#475569">Women</text><text '
                'x="165" y="92" font-size="11" font-weight="700" fill="#475569">22</text><text x="255" y="92" '
                'font-size="11" font-weight="700" fill="#475569">28</text><text x="350" y="92" font-size="11" '
                'font-weight="800" fill="#0f172a">50</text>\n'
                '            <text x="60" y="126" font-size="11" font-weight="900" fill="#1e40af">Total</text><text '
                'x="165" y="126" font-size="11" font-weight="800" fill="#0f172a">40</text><text x="255" y="126" '
                'font-size="11" font-weight="800" fill="#0f172a">40</text><text x="350" y="126" font-size="12" '
                'font-weight="900" fill="#059669">80</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Two-Way Tables &amp; Probability',
    'watch_out': "For conditional probability ('Given that the person is a woman...'), divide by the WOMEN TOTAL (50), "
                 'not the grand total (80)!'},
  { 'answer_text': 'Negative correlation (as temperature increases, heating fuel used decreases).',
    'challenge_prompt': 'Describe the relationship between temperature and heating fuel consumption: As temperature '
                        'rises, heating fuel usage drops.',
    'dfe_code': 'DfE L2.HD43',
    'golden_rule': 'Draw a line of best fit with an equal balance of points above and below the line!',
    'id': 'm-l2-46',
    'level': 'l2',
    'level_label': 'Level 2',
    'number': 46,
    'rule_body': 'Positive: As X goes up, Y goes up (slopes uphill). Negative: As X goes up, Y goes down (slopes '
                 'downhill). Zero: Scattered random cloud with no trend.',
    'rule_heading': 'Positive • Negative • Zero Correlation',
    'strand_name': 'Handling Data',
    'strand_theme': 'purple',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(30, 20)">\n'
                '            <rect x="0" y="0" width="120" height="120" rx="6" fill="#eff6ff" stroke="#3b82f6"/>\n'
                '            <line x1="20" y1="100" x2="100" y2="20" stroke="#2563eb" stroke-width="2"/>\n'
                '            <text x="60" y="112" font-size="10" font-weight="800" fill="#1e40af" '
                'text-anchor="middle">POSITIVE (+)</text>\n'
                '          </g>\n'
                '          <g transform="translate(170, 20)">\n'
                '            <rect x="0" y="0" width="120" height="120" rx="6" fill="#fef2f2" stroke="#ef4444"/>\n'
                '            <line x1="20" y1="20" x2="100" y2="100" stroke="#dc2626" stroke-width="2"/>\n'
                '            <text x="60" y="112" font-size="10" font-weight="800" fill="#991b1b" '
                'text-anchor="middle">NEGATIVE (-)</text>\n'
                '          </g>\n'
                '          <g transform="translate(310, 20)">\n'
                '            <rect x="0" y="0" width="120" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>\n'
                '            <circle cx="35" cy="40" r="3" fill="#64748b"/><circle cx="85" cy="35" r="3" '
                'fill="#64748b"/><circle cx="50" cy="80" r="3" fill="#64748b"/><circle cx="95" cy="75" r="3" '
                'fill="#64748b"/>\n'
                '            <text x="60" y="112" font-size="10" font-weight="800" fill="#475569" '
                'text-anchor="middle">NO CORRELATION</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Scatter Diagrams &amp; Correlation',
    'watch_out': 'Correlation does NOT prove causation! (e.g. ice cream sales and sunburn both correlate with hot '
                 'weather).'},
  { 'answer_text': 'No, it is unreliable because 2035 is an extrapolation far beyond the recorded data range, and '
                   'market conditions may change.',
    'challenge_prompt': 'A company measures sales between 2018 and 2023. They predict sales for 2035 using their line '
                        'of best fit. Is this reliable?',
    'dfe_code': 'DfE L2.HD44',
    'golden_rule': 'Predictions outside the original data range are UNRELIABLE because trends may flatten or reverse!',
    'id': 'm-l2-47',
    'level': 'l2',
    'level_label': 'Level 2',
    'number': 47,
    'rule_body': 'Interpolation: Estimating a value INSIDE the given data range (Reliable). Extrapolation: Extending '
                 'line of best fit BEYOND the data points (Unreliable / Risky).',
    'rule_heading': 'Inside Range (Reliable) vs Beyond (Unreliable)',
    'strand_name': 'Handling Data',
    'strand_theme': 'purple',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(40, 20)">\n'
                '            <rect x="0" y="0" width="180" height="125" rx="8" fill="#f0fdf4" stroke="#16a34a" '
                'stroke-width="1.8"/>\n'
                '            <text x="90" y="26" font-size="12" font-weight="800" fill="#15803d" '
                'text-anchor="middle">INTERPOLATION</text>\n'
                '            <text x="15" y="55" font-size="11" font-weight="700" fill="#0f172a">Within tested '
                'range</text>\n'
                '            <text x="15" y="80" font-size="11" font-weight="700" fill="#475569">e.g. data for 10–50 '
                'yrs</text>\n'
                '            <rect x="15" y="92" width="150" height="24" rx="4" fill="#16a34a"/>\n'
                '            <text x="90" y="108" font-size="11" font-weight="800" fill="#ffffff" '
                'text-anchor="middle">RELIABLE PREDICTION</text>\n'
                '          </g>\n'
                '          <g transform="translate(240, 20)">\n'
                '            <rect x="0" y="0" width="180" height="125" rx="8" fill="#fef2f2" stroke="#dc2626" '
                'stroke-width="1.8"/>\n'
                '            <text x="90" y="26" font-size="12" font-weight="800" fill="#b91c1c" '
                'text-anchor="middle">EXTRAPOLATION</text>\n'
                '            <text x="15" y="55" font-size="11" font-weight="700" fill="#0f172a">Outside data '
                'range</text>\n'
                '            <text x="15" y="80" font-size="11" font-weight="700" fill="#475569">Predicting at 90 '
                'yrs</text>\n'
                '            <rect x="15" y="92" width="150" height="24" rx="4" fill="#dc2626"/>\n'
                '            <text x="90" y="108" font-size="11" font-weight="800" fill="#ffffff" '
                'text-anchor="middle">UNRELIABLE / RISKY</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Interpolation vs Extrapolation',
    'watch_out': "Examiners will ask 'Why might this prediction be unreliable?' — answer: 'It is extrapolated beyond "
                 "the data range.'"},
  { 'answer_text': 'Degrees per patient = 360° ÷ 120 = 3° per patient. Bus angle = 45 × 3° = 135°.',
    'challenge_prompt': 'In a survey of 120 hospital patients, 45 travelled by bus. What angle should represent bus '
                        'travel on a pie chart?',
    'dfe_code': 'DfE L2.HD45',
    'golden_rule': 'Sum of all pie chart sector angles MUST equal exactly 360°!',
    'id': 'm-l2-48',
    'level': 'l2',
    'level_label': 'Level 2',
    'number': 48,
    'rule_body': 'Total degrees in any circle = 360°. Degrees per item = 360° ÷ Total Frequency. To find angle for a '
                 'category: Multiply its frequency by degrees per item.',
    'rule_heading': 'Angle = (Value ÷ Total) × 360°',
    'strand_name': 'Handling Data',
    'strand_theme': 'purple',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(60, 20)">\n'
                '            <circle cx="65" cy="65" r="55" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>\n'
                '            <path d="M 65,65 L 65,10 A 55,55 0 0,1 120,65 Z" fill="#93c5fd"/>\n'
                '            <text x="85" y="45" font-size="11" font-weight="800" fill="#1e3a8a">90°</text>\n'
                '            <text x="65" y="95" font-size="11" font-weight="800" fill="#1e3a8a" '
                'text-anchor="middle">270°</text>\n'
                '          </g>\n'
                '          <g transform="translate(210, 30)">\n'
                '            <rect x="0" y="0" width="210" height="100" rx="8" fill="#f8fafc" stroke="#cbd5e1" '
                'stroke-width="1.8"/>\n'
                '            <text x="105" y="26" font-size="12" font-weight="800" fill="#0f172a" '
                'text-anchor="middle">Degrees per 1 item:</text>\n'
                '            <text x="105" y="50" font-size="13" font-weight="900" fill="#2563eb" '
                'text-anchor="middle">360° ÷ Total Frequency</text>\n'
                '            <text x="105" y="78" font-size="11" font-weight="700" fill="#059669" '
                'text-anchor="middle">e.g. 360° ÷ 72 people = 5° each</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Pie Charts: Angles &amp; Frequencies',
    'watch_out': 'A pie chart only shows PROPORTIONS, not raw quantities, unless the total sample size is given!'},
  { 'answer_text': 'Increase = £45k - £35k = £10k. % Increase = (10 ÷ 35) × 100 = 28.57% (or 28.6%).',
    'challenge_prompt': 'In Quarter 1: 2023 sales were £35k, 2024 sales were £45k. What was the percentage increase '
                        'from 2023 to 2024?',
    'dfe_code': 'DfE L2.HD46',
    'golden_rule': 'Read the key carefully to avoid mixing up years or cohorts!',
    'id': 'm-l2-49',
    'level': 'l2',
    'level_label': 'Level 2',
    'number': 49,
    'rule_body': 'Dual bar charts place two bars side-by-side for each category to compare groups (e.g. Male vs '
                 'Female, 2023 vs 2024). Always check the legend key and vertical axis scale.',
    'rule_heading': 'Side-by-Side Comparison with Key',
    'strand_name': 'Handling Data',
    'strand_theme': 'purple',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(50, 15)">\n'
                '            <line x1="20" y1="120" x2="360" y2="120" stroke="#334155" stroke-width="2"/>\n'
                '            <line x1="20" y1="20" x2="20" y2="120" stroke="#334155" stroke-width="2"/>\n'
                '            <rect x="60" y="50" width="30" height="70" fill="#3b82f6"/>\n'
                '            <rect x="92" y="30" width="30" height="90" fill="#10b981"/>\n'
                '            <rect x="180" y="65" width="30" height="55" fill="#3b82f6"/>\n'
                '            <rect x="212" y="45" width="30" height="75" fill="#10b981"/>\n'
                '            <text x="91" y="135" font-size="10" font-weight="700" fill="#0f172a" '
                'text-anchor="middle">Quarter 1</text>\n'
                '            <text x="211" y="135" font-size="10" font-weight="700" fill="#0f172a" '
                'text-anchor="middle">Quarter 2</text>\n'
                '            <rect x="280" y="30" width="12" height="12" fill="#3b82f6"/>\n'
                '            <text x="300" y="40" font-size="10" font-weight="700" fill="#0f172a">2023</text>\n'
                '            <rect x="280" y="55" width="12" height="12" fill="#10b981"/>\n'
                '            <text x="300" y="65" font-size="10" font-weight="700" fill="#0f172a">2024</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Dual &amp; Grouped Bar Charts',
    'watch_out': 'Check the vertical axis scale increments — each grid square may represent 2, 5, 10, or 20 units.'},
  { 'answer_text': 'The vertical axis does not start at zero (truncated/broken axis), which exaggerates the visual '
                   'difference between the bars.',
    'challenge_prompt': 'Explain one way a bar chart comparing company satisfaction could be misleading if one bar '
                        'appears 4 times taller than another.',
    'dfe_code': 'DfE L2.HD47',
    'golden_rule': 'Always check if the vertical axis starts at ZERO (0)!',
    'id': 'm-l2-50',
    'level': 'l2',
    'level_label': 'Level 2',
    'number': 50,
    'rule_body': 'Common tricks used to deceive: 1. Broken vertical axis (not starting at 0) exaggerates tiny '
                 'differences. 2. Unequal scale increments. 3. 3D distortion making front slices look bigger.',
    'rule_heading': 'Non-Zero Baselines &amp; Uneven Scales',
    'strand_name': 'Handling Data',
    'strand_theme': 'purple',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(30, 20)">\n'
                '            <rect x="0" y="0" width="180" height="140" rx="8" fill="#fef2f2" stroke="#dc2626" '
                'stroke-width="1.8"/>\n'
                '            <text x="90" y="24" font-size="11" font-weight="800" fill="#b91c1c" '
                'text-anchor="middle">MISLEADING (Truncated)</text>\n'
                '            <text x="15" y="50" font-size="10" font-weight="700" fill="#0f172a">Y-axis starts at '
                '90%</text>\n'
                '            <rect x="40" y="80" width="30" height="35" fill="#dc2626"/>\n'
                '            <rect x="90" y="60" width="30" height="55" fill="#dc2626"/>\n'
                '            <text x="90" y="132" font-size="9" font-weight="800" fill="#dc2626" '
                'text-anchor="middle">Looks like 2x difference!</text>\n'
                '          </g>\n'
                '          <g transform="translate(240, 20)">\n'
                '            <rect x="0" y="0" width="180" height="140" rx="8" fill="#f0fdf4" stroke="#16a34a" '
                'stroke-width="1.8"/>\n'
                '            <text x="90" y="24" font-size="11" font-weight="800" fill="#15803d" '
                'text-anchor="middle">HONEST (Starts at 0)</text>\n'
                '            <text x="15" y="50" font-size="10" font-weight="700" fill="#0f172a">Y-axis starts at '
                '0%</text>\n'
                '            <rect x="40" y="65" width="30" height="50" fill="#16a34a"/>\n'
                '            <rect x="90" y="62" width="30" height="53" fill="#16a34a"/>\n'
                '            <text x="90" y="132" font-size="9" font-weight="800" fill="#15803d" '
                'text-anchor="middle">Shows true 92% vs 95%</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Misleading Graphs &amp; Traps',
    'watch_out': 'A graph that looks dramatic often only represents a 1% or 2% actual difference.'}]
