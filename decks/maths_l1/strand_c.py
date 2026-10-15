"""Maths L1 Strand C: Handling Information and Data (Cards 29-38)"""
CARDS = [ { 'answer_text': 'Total = 14 + 18 + 12 + 20 + 16 = 80. Count = 5. Mean = 80 ÷ 5 = 16.',
    'challenge_prompt': 'Five friends score 14, 18, 12, 20, and 16 in a quiz. What is their mean score?',
    'dfe_code': 'DfE L1.HD28',
    'golden_rule': 'Divide by how many items you added up!',
    'id': 'm-l1-29',
    'level': 'l1',
    'level_label': 'Level 1',
    'number': 29,
    'rule_body': '1. Add all numbers together to find total sum. 2. Count how many numbers there are. 3. Divide total '
                 'sum by the count. Mean is the fair share.',
    'rule_heading': 'Add All Up, Divide by Count',
    'strand_name': 'Handling Data',
    'strand_theme': 'cyan',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(40, 20)">\n'
                '            <rect x="0" y="0" width="380" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" '
                'stroke-width="1.8"/>\n'
                '            <text x="190" y="28" font-size="13" font-weight="800" fill="#1e40af" '
                'text-anchor="middle">Find Mean of: 6, 8, 12, 14</text>\n'
                '            <text x="190" y="60" font-size="12" font-weight="700" fill="#475569" '
                'text-anchor="middle">Step 1: Total = 6 + 8 + 12 + 14 = 40</text>\n'
                '            <text x="190" y="85" font-size="12" font-weight="700" fill="#475569" '
                'text-anchor="middle">Step 2: There are 4 numbers</text>\n'
                '            <rect x="110" y="95" width="160" height="25" rx="4" fill="#3b82f6"/>\n'
                '            <text x="190" y="112" font-size="12" font-weight="900" fill="#ffffff" '
                'text-anchor="middle">Step 3: 40 ÷ 4 = 10</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Mean Average (Step-by-Step)',
    'watch_out': "Don't forget to press equals (=) before dividing on your calculator, or use brackets."},
  { 'answer_text': 'Order: 6, 9, 12, 15, 21. Middle value is 12 (Median = 12).',
    'challenge_prompt': 'Find the median of: 15, 6, 21, 9, 12.',
    'dfe_code': 'DfE L1.HD29',
    'golden_rule': 'You MUST sort the numbers from smallest to largest first!',
    'id': 'm-l1-30',
    'level': 'l1',
    'level_label': 'Level 1',
    'number': 30,
    'rule_body': '1. Put numbers in numerical order from smallest to largest. 2. Cross off one from each end until you '
                 'reach the middle number. If two remain in middle, find their midpoint.',
    'rule_heading': 'Line Up Low to High, Pick Middle',
    'strand_name': 'Handling Data',
    'strand_theme': 'cyan',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(40, 20)">\n'
                '            <rect x="0" y="0" width="380" height="130" rx="8" fill="#f0fdf4" stroke="#16a34a" '
                'stroke-width="1.8"/>\n'
                '            <text x="190" y="28" font-size="12" font-weight="800" fill="#15803d" '
                'text-anchor="middle">Raw Data: 9, 3, 7, 2, 8</text>\n'
                '            <text x="190" y="60" font-size="13" font-weight="700" fill="#475569" '
                'text-anchor="middle">1. Put in order: 2, 3, <tspan font-weight="900" fill="#16a34a">7</tspan>, 8, '
                '9</text>\n'
                '            <rect x="110" y="78" width="160" height="35" rx="6" fill="#16a34a"/>\n'
                '            <text x="190" y="100" font-size="14" font-weight="900" fill="#ffffff" '
                'text-anchor="middle">Median = 7</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Median (Middle Value)',
    'watch_out': "Never pick the middle number of the unsorted list (in 9, 3, 7, 2, 8, '7' happens to be middle, but "
                 'never rely on luck!).'},
  { 'answer_text': '7 appears three times (more than any other number). Mode = 7.',
    'challenge_prompt': 'What is the modal value of this dataset: 4, 7, 2, 7, 5, 9, 7, 2?',
    'dfe_code': 'DfE L1.HD30',
    'golden_rule': "'MO'de = 'MO'st often!",
    'id': 'm-l1-31',
    'level': 'l1',
    'level_label': 'Level 1',
    'number': 31,
    'rule_body': 'Mode is the number or category that appears MOST OFTEN in the data. There can be one mode, more than '
                 'one mode (bimodal), or no mode if all values appear once.',
    'rule_heading': 'The Most Common Item',
    'strand_name': 'Handling Data',
    'strand_theme': 'cyan',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(40, 20)">\n'
                '            <rect x="0" y="0" width="380" height="130" rx="8" fill="#fdf2f8" stroke="#ec4899" '
                'stroke-width="1.8"/>\n'
                '            <text x="190" y="28" font-size="13" font-weight="800" fill="#9d174d" '
                'text-anchor="middle">Shoe Sizes: 5, 6, 6, 7, 6, 8, 5</text>\n'
                '            <text x="190" y="60" font-size="12" font-weight="700" fill="#475569" '
                'text-anchor="middle">Size 5 appears 2 times • Size 6 appears 3 times</text>\n'
                '            <rect x="110" y="78" width="160" height="35" rx="6" fill="#db2777"/>\n'
                '            <text x="190" y="100" font-size="14" font-weight="900" fill="#ffffff" '
                'text-anchor="middle">Mode = Size 6 ★</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Mode (Most Frequent)',
    'watch_out': 'The mode can be words (e.g. Blue, Coffee) — it is the only average that works for non-numbers.'},
  { 'answer_text': 'Highest = £310. Lowest = £150. Range = £310 - £150 = £160.',
    'challenge_prompt': 'Weekly sales figures are: £180, £240, £150, £310, £220. Calculate the range.',
    'dfe_code': 'DfE L1.HD31',
    'golden_rule': 'Range = Highest minus Lowest!',
    'id': 'm-l1-32',
    'level': 'l1',
    'level_label': 'Level 1',
    'number': 32,
    'rule_body': 'Range is NOT an average — it measures how spread out the numbers are. Subtract the smallest number '
                 'from the largest number. Smaller range = more consistent.',
    'rule_heading': 'Range = Highest - Lowest',
    'strand_name': 'Handling Data',
    'strand_theme': 'cyan',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(40, 20)">\n'
                '            <rect x="0" y="0" width="380" height="130" rx="8" fill="#fffbeb" stroke="#f59e0b" '
                'stroke-width="1.8"/>\n'
                '            <text x="190" y="28" font-size="13" font-weight="800" fill="#b45309" '
                'text-anchor="middle">Temperatures: 12°C, 25°C, 18°C, 14°C</text>\n'
                '            <text x="190" y="60" font-size="12" font-weight="700" fill="#475569" '
                'text-anchor="middle">Highest = 25°C   •   Lowest = 12°C</text>\n'
                '            <rect x="100" y="78" width="180" height="35" rx="6" fill="#f59e0b"/>\n'
                '            <text x="190" y="100" font-size="14" font-weight="900" fill="#ffffff" '
                'text-anchor="middle">Range = 25 - 12 = 13°C</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Range (Spread of Data)',
    'watch_out': "Don't write '12 to 25' — the range is a SINGLE number obtained by subtracting (13)."},
  { 'answer_text': 'Three bundles of 5 plus 2: (3 × 5) + 2 = 15 + 2 = 17.',
    'challenge_prompt': 'A tally chart shows three 5-bar tally gates and 2 single vertical strokes. What frequency '
                        'number does this represent?',
    'dfe_code': 'DfE L1.HD32',
    'golden_rule': 'The 5th tally stroke always gates diagonally across the bundle of 4!',
    'id': 'm-l1-33',
    'level': 'l1',
    'level_label': 'Level 1',
    'number': 33,
    'rule_body': 'Tallies are grouped in bundles of five: four vertical marks (||||) with the fifth mark crossing '
                 'diagonally as a gate across the bundle. Frequency is the total count written as a number.',
    'rule_heading': 'Bundles of 5 (4 Vertical + 1 Diagonal Gate)',
    'strand_name': 'Handling Data',
    'strand_theme': 'cyan',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '          <g transform="translate(60, 20)">\n'
                '            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>\n'
                '            <text x="170" y="26" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">TALLY SYSTEM (5-BAR GATE)</text>\n'
                '            <text x="45" y="64" font-size="12" font-weight="700" fill="#475569">Item: Car</text>\n'
                '            <g stroke="#2563eb" stroke-width="2.5" stroke-linecap="round">\n'
                '              <line x1="140" y1="46" x2="140" y2="70"/><line x1="148" y1="46" x2="148" y2="70"/>\n'
                '              <line x1="156" y1="46" x2="156" y2="70"/><line x1="164" y1="46" x2="164" y2="70"/>\n'
                '              <line x1="136" y1="66" x2="168" y2="50" stroke="#dc2626"/>\n'
                '              <line x1="180" y1="46" x2="180" y2="70"/><line x1="188" y1="46" x2="188" y2="70"/><line x1="196" y1="46" x2="196" y2="70"/>\n'
                '            </g>\n'
                '            <text x="265" y="64" font-size="13" font-weight="900" fill="#059669">Freq: 8</text>\n'
                '            <text x="170" y="105" font-size="11" font-weight="700" fill="#64748b" text-anchor="middle">Count tallies in 5s: 5 + 3 = 8</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Tally Charts &amp; Frequency',
    'watch_out': 'Check your raw data twice by crossing off each item as you record its tally mark.'},
  { 'answer_text': '1. Equal bar widths with equal gaps. 2. Labelled axes with an evenly-spaced linear number scale '
                   'starting at zero.',
    'challenge_prompt': 'State two things every bar chart must have to receive full marks in an exam.',
    'dfe_code': 'DfE L1.HD33',
    'golden_rule': 'Bars must NOT touch each other in a categorical bar chart!',
    'id': 'm-l1-34',
    'level': 'l1',
    'level_label': 'Level 1',
    'number': 34,
    'rule_body': 'To draw a bar chart for full marks: 1. Evenly spaced linear scale on vertical axis starting at 0. 2. '
                 "Label both axes (e.g. 'Days' and 'Frequency'). 3. Equal width bars with equal gaps between them.",
    'rule_heading': 'Equal Widths, Equal Gaps, Labelled Axes',
    'strand_name': 'Handling Data',
    'strand_theme': 'cyan',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(60, 20)">\n'
                '            <line x1="20" y1="110" x2="300" y2="110" stroke="#334155" stroke-width="2"/>\n'
                '            <line x1="20" y1="20" x2="20" y2="110" stroke="#334155" stroke-width="2"/>\n'
                '            <rect x="50" y="40" width="40" height="70" fill="#3b82f6"/>\n'
                '            <rect x="130" y="60" width="40" height="50" fill="#3b82f6"/>\n'
                '            <rect x="210" y="25" width="40" height="85" fill="#3b82f6"/>\n'
                '            <text x="70" y="125" font-size="10" font-weight="700" fill="#0f172a" '
                'text-anchor="middle">Tea</text>\n'
                '            <text x="150" y="125" font-size="10" font-weight="700" fill="#0f172a" '
                'text-anchor="middle">Coffee</text>\n'
                '            <text x="230" y="125" font-size="10" font-weight="700" fill="#0f172a" '
                'text-anchor="middle">Water</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Bar Charts &amp; Scales',
    'watch_out': 'Check what 1 grid square represents on the vertical axis (e.g. 1 square might be 2 or 5 units).'},
  { 'answer_text': '28 ÷ 8 = 3.5. Draw 3 whole circles and 1 half circle.',
    'challenge_prompt': 'On a pictogram, a circle represents 8 cars. How many circles should you draw to represent 28 '
                        'cars?',
    'dfe_code': 'DfE L1.HD34',
    'golden_rule': 'Always check the KEY first — one picture is rarely just 1 item!',
    'id': 'm-l1-35',
    'level': 'l1',
    'level_label': 'Level 1',
    'number': 35,
    'rule_body': 'A pictogram uses pictures or symbols to represent quantities. Look at the key: 1 whole symbol = n '
                 'items. A half symbol = n ÷ 2. A quarter symbol = n ÷ 4.',
    'rule_heading': 'Always Check the Symbol Key',
    'strand_name': 'Handling Data',
    'strand_theme': 'cyan',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(60, 20)">\n'
                '            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" '
                'stroke-width="1.8"/>\n'
                '            <text x="170" y="26" font-size="12" font-weight="800" fill="#0f172a" '
                'text-anchor="middle">KEY: [★] = 4 BOOKS</text>\n'
                '            <text x="40" y="60" font-size="12" font-weight="700" fill="#475569">Monday: [★] [★] = 2 × '
                '4 = 8 books</text>\n'
                '            <text x="40" y="90" font-size="12" font-weight="700" fill="#475569">Tuesday: [★] [★] '
                '[half] = 4 + 4 + 2 = 10 books</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Pictograms (Using a Key)',
    'watch_out': "Don't count the number of symbols without multiplying by the key value."},
  { 'answer_text': 'Rise = 22°C - 14°C = 8°C.',
    'challenge_prompt': 'Between 9 am (14°C) and 1 pm (22°C), what was the rise in temperature?',
    'dfe_code': 'DfE L1.HD35',
    'golden_rule': 'Time always goes along the bottom horizontal axis!',
    'id': 'm-l1-36',
    'level': 'l1',
    'level_label': 'Level 1',
    'number': 36,
    'rule_body': 'Line graphs show how continuous data changes over time (temperature, sales, patient heart rate). '
                 'Time is plotted along the horizontal axis. Read points by looking across to vertical axis.',
    'rule_heading': 'Plot Points &amp; Join with Straight Lines',
    'strand_name': 'Handling Data',
    'strand_theme': 'cyan',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(60, 20)">\n'
                '            <line x1="20" y1="110" x2="300" y2="110" stroke="#334155" stroke-width="2"/>\n'
                '            <line x1="20" y1="20" x2="20" y2="110" stroke="#334155" stroke-width="2"/>\n'
                '            <polyline points="40,90 100,70 160,80 220,40 280,30" fill="none" stroke="#2563eb" '
                'stroke-width="2.5"/>\n'
                '            <circle cx="40" cy="90" r="4" fill="#2563eb"/><circle cx="100" cy="70" r="4" '
                'fill="#2563eb"/><circle cx="160" cy="80" r="4" fill="#2563eb"/><circle cx="220" cy="40" r="4" '
                'fill="#2563eb"/><circle cx="280" cy="30" r="4" fill="#2563eb"/>\n'
                '            <text x="160" y="130" font-size="10" font-weight="700" fill="#0f172a" '
                'text-anchor="middle">Months (Jan to May) → Overall Upward Trend</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Line Graphs (Trends over Time)',
    'watch_out': 'Join the plotted data points with neat straight ruler lines from point to point.'},
  { 'answer_text': '(a) Certain. (b) Impossible.',
    'challenge_prompt': 'Match the word to the event: (a) Tomorrow will be Wednesday if today is Tuesday. (b) Rolling '
                        'an 8 on a standard 6-sided die.',
    'dfe_code': 'DfE L1.HD36',
    'golden_rule': 'Probabilities on a number scale run strictly from 0 to 1!',
    'id': 'm-l1-37',
    'level': 'l1',
    'level_label': 'Level 1',
    'number': 37,
    'rule_body': '0 = Impossible (can never happen). 0.5 (1/2 or 50%) = Even Chance (e.g. flipping heads). 1 = Certain '
                 '(guaranteed to happen). Unlikely is between 0 and 0.5; Likely is between 0.5 and 1.',
    'rule_heading': 'Impossible to Certain',
    'strand_name': 'Handling Data',
    'strand_theme': 'cyan',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
          <line x1="50" y1="85" x2="410" y2="85" stroke="#334155" stroke-width="2.5"/>
          <circle cx="50" cy="85" r="5" fill="#dc2626"/>
          <text x="50" y="115" font-size="11" font-weight="800" fill="#dc2626" text-anchor="middle">0 (Impossible)</text>
          <circle cx="140" cy="85" r="4" fill="#f59e0b"/>
          <text x="140" y="115" font-size="10" font-weight="700" fill="#b45309" text-anchor="middle">Unlikely</text>
          <circle cx="230" cy="85" r="5" fill="#2563eb"/>
          <text x="230" y="115" font-size="11" font-weight="800" fill="#1e40af" text-anchor="middle">0.5 (Evens)</text>
          <circle cx="320" cy="85" r="4" fill="#059669"/>
          <text x="320" y="115" font-size="10" font-weight="700" fill="#047857" text-anchor="middle">Likely</text>
          <circle cx="410" cy="85" r="5" fill="#16a34a"/>
          <text x="410" y="115" font-size="11" font-weight="800" fill="#15803d" text-anchor="middle">1 (Certain)</text>
</svg>""",
    'title': 'Probability Words &amp; Scale',
    'watch_out': "Don't use words like 'Good chance' or 'Fifty-fifty' on an exam — use 'Likely' or 'Even chance'."},
  { 'answer_text': 'Group 2 was more consistent because its range was smaller (2 kg compared to 6 kg).',
    'challenge_prompt': 'Group 1: Mean = 24 kg, Range = 6 kg. Group 2: Mean = 20 kg, Range = 2 kg. Which group was '
                        'more consistent in weight?',
    'dfe_code': 'DfE L1.HD37',
    'golden_rule': 'Always state the numbers AND the real-world context (sales, time)!',
    'id': 'm-l1-38',
    'level': 'l1',
    'level_label': 'Level 1',
    'number': 38,
    'rule_body': 'To compare two groups for 2 marks: 1. State which group has a higher/lower mean or median. 2. State '
                 'which group is more consistent by comparing their range (smaller range = more consistent).',
    'rule_heading': 'Compare One Average &amp; One Range',
    'strand_name': 'Handling Data',
    'strand_theme': 'cyan',
    'subject': 'maths',
    'subject_label': 'Maths',
    'svg_html': """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
          <rect x="30" y="20" width="400" height="130" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
          <text x="230" y="42" font-size="13" font-weight="900" fill="#15803d" text-anchor="middle">LEVEL 1 EXAM COMPARISON TEMPLATE</text>
          <g transform="translate(45, 60)">
            <text x="0" y="22" font-size="11" font-weight="700" fill="#0f172a">1. "Team A scored higher on average (Mean 18 vs 14)."</text>
            <text x="0" y="50" font-size="11" font-weight="700" fill="#0f172a">2. "Team B was more consistent (smaller range 4 vs 10)."</text>
          </g>
</svg>""",
    'title': 'Comparing Two Data Sets (L1)',
    'watch_out': 'A larger range means LESS consistent results — not better performance!'}]
