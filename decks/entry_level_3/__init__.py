"""
Master Functional Skills - Entry Level 3 Visual Revision Cards Deck (30 Cards)
Covers DfE Entry Level 3 Mathematics (#1-#14), English (#15-#24), and Digital Functional Skills (#25-#30).
"""

CARDS = [
    # =========================================================================
    # ENTRY LEVEL 3 MATHEMATICS (#1 - #14)
    # =========================================================================
    {
        "id": "e3-01",
        "number": 1,
        "subject": "maths",
        "subject_label": "Maths",
        "level": "e3",
        "level_label": "Entry Level 3",
        "strand_name": "Number System",
        "strand_theme": "amber",
        "dfe_code": "DfE E3.N1",
        "title": "Place Value up to 1,000",
        "rule_heading": "Hundreds • Tens • Ones (H-T-O)",
        "rule_body": "Every digit in a 3-digit number has a value based on its column: Hundreds (×100), Tens (×10), and Ones (×1). Zero (0) holds an empty column in place.",
        "golden_rule": "Read 3-digit numbers from left to right: 407 is Four hundred and seven!",
        "watch_out": "Never drop the middle zero: 'Six hundred and five' is 605, NOT 65!",
        "challenge_prompt": "What is the value of the digit 8 in the number 842, and how do you write 'seven hundred and nine' in digits?",
        "answer_text": "Value of 8 = 800 (8 hundreds). 'Seven hundred and nine' = 709.",
        "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(30, 18)">
            <rect x="0" y="0" width="400" height="132" rx="8" fill="#fffbeb" stroke="#f59e0b" stroke-width="2"/>
            <text x="200" y="24" font-size="12" font-weight="900" fill="#92400e" text-anchor="middle">PLACE VALUE CHART (NUMBER: 749)</text>
            <rect x="25" y="36" width="110" height="80" rx="6" fill="#ffffff" stroke="#d97706"/>
            <text x="80" y="55" font-size="11" font-weight="800" fill="#b45309" text-anchor="middle">HUNDREDS</text>
            <text x="80" y="84" font-size="22" font-weight="900" fill="#0f172a" text-anchor="middle">7</text>
            <text x="80" y="106" font-size="10.5" font-weight="800" fill="#059669" text-anchor="middle">= 700</text>
            <rect x="145" y="36" width="110" height="80" rx="6" fill="#ffffff" stroke="#d97706"/>
            <text x="200" y="55" font-size="11" font-weight="800" fill="#b45309" text-anchor="middle">TENS</text>
            <text x="200" y="84" font-size="22" font-weight="900" fill="#0f172a" text-anchor="middle">4</text>
            <text x="200" y="106" font-size="10.5" font-weight="800" fill="#2563eb" text-anchor="middle">= 40</text>
            <rect x="265" y="36" width="110" height="80" rx="6" fill="#ffffff" stroke="#d97706"/>
            <text x="320" y="55" font-size="11" font-weight="800" fill="#b45309" text-anchor="middle">ONES</text>
            <text x="320" y="84" font-size="22" font-weight="900" fill="#0f172a" text-anchor="middle">9</text>
            <text x="320" y="106" font-size="10.5" font-weight="800" fill="#dc2626" text-anchor="middle">= 9</text>
          </g>
        </svg>"""
    },
    {
        "id": "e3-02",
        "number": 2,
        "subject": "maths",
        "subject_label": "Maths",
        "level": "e3",
        "level_label": "Entry Level 3",
        "strand_name": "Number System",
        "strand_theme": "amber",
        "dfe_code": "DfE E3.N2",
        "title": "Column Addition &amp; Subtraction",
        "rule_heading": "Align Right • Start at Ones • Regroup",
        "rule_body": "Always line up Hundreds, Tens, and Ones on the right. Start at the Ones column. In addition, carry 10 to the next column; in subtraction, borrow from the left if the top digit is smaller.",
        "golden_rule": "Always start adding or subtracting from the ONES column on the far right!",
        "watch_out": "In 342 - 158, do NOT do 8 - 2 = 6! You must borrow 1 ten from the 4 so 12 - 8 = 4.",
        "challenge_prompt": "Calculate: (a) 468 + 275   (b) 604 - 238",
        "answer_text": "(a) 468 + 275 = 743 (carry 1 ten and 1 hundred). (b) 604 - 238 = 366.",
        "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(25, 18)">
            <rect x="0" y="0" width="195" height="132" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
            <text x="97" y="22" font-size="11.5" font-weight="900" fill="#15803d" text-anchor="middle">ADDITION (CARRYING)</text>
            <text x="36" y="74" font-size="18" font-weight="900" fill="#0284c7" text-anchor="middle">+</text>
            <text x="75" y="52" font-size="15" font-weight="800" fill="#0f172a" text-anchor="middle">3</text>
            <text x="105" y="52" font-size="15" font-weight="800" fill="#0f172a" text-anchor="middle">6</text>
            <text x="135" y="52" font-size="15" font-weight="800" fill="#0f172a" text-anchor="middle">7</text>
            <text x="75" y="74" font-size="15" font-weight="800" fill="#0f172a" text-anchor="middle">1</text>
            <text x="105" y="74" font-size="15" font-weight="800" fill="#0f172a" text-anchor="middle">5</text>
            <text x="135" y="74" font-size="15" font-weight="800" fill="#0f172a" text-anchor="middle">8</text>
            <line x1="30" y1="84" x2="165" y2="84" stroke="#15803d" stroke-width="2"/>
            <text x="75" y="106" font-size="16" font-weight="900" fill="#059669" text-anchor="middle">5</text>
            <text x="105" y="106" font-size="16" font-weight="900" fill="#059669" text-anchor="middle">2</text>
            <text x="135" y="106" font-size="16" font-weight="900" fill="#059669" text-anchor="middle">5</text>
            <text x="97" y="123" font-size="9.5" font-weight="700" fill="#475569" text-anchor="middle">Carry: 1 hundred, 1 ten</text>
          </g>
          <g transform="translate(240, 18)">
            <rect x="0" y="0" width="195" height="132" rx="8" fill="#eff6ff" stroke="#2563eb" stroke-width="1.8"/>
            <text x="97" y="22" font-size="11.5" font-weight="900" fill="#1e40af" text-anchor="middle">SUBTRACTION (BORROW)</text>
            <text x="105" y="38" font-size="10.5" font-weight="900" fill="#dc2626" text-anchor="middle">3</text>
            <text x="135" y="38" font-size="10.5" font-weight="900" fill="#dc2626" text-anchor="middle">12</text>
            <text x="36" y="74" font-size="18" font-weight="900" fill="#0284c7" text-anchor="middle">&minus;</text>
            <text x="75" y="52" font-size="15" font-weight="800" fill="#0f172a" text-anchor="middle">5</text>
            <text x="105" y="52" font-size="15" font-weight="800" fill="#94a3b8" text-anchor="middle">4</text>
            <line x1="97" y1="57" x2="113" y2="43" stroke="#dc2626" stroke-width="2" stroke-linecap="round"/>
            <text x="135" y="52" font-size="15" font-weight="800" fill="#94a3b8" text-anchor="middle">2</text>
            <line x1="127" y1="57" x2="143" y2="43" stroke="#dc2626" stroke-width="2" stroke-linecap="round"/>
            <text x="75" y="74" font-size="15" font-weight="800" fill="#0f172a" text-anchor="middle">2</text>
            <text x="105" y="74" font-size="15" font-weight="800" fill="#0f172a" text-anchor="middle">1</text>
            <text x="135" y="74" font-size="15" font-weight="800" fill="#0f172a" text-anchor="middle">7</text>
            <line x1="30" y1="84" x2="165" y2="84" stroke="#1e40af" stroke-width="2"/>
            <text x="75" y="106" font-size="16" font-weight="900" fill="#2563eb" text-anchor="middle">3</text>
            <text x="105" y="106" font-size="16" font-weight="900" fill="#2563eb" text-anchor="middle">2</text>
            <text x="135" y="106" font-size="16" font-weight="900" fill="#2563eb" text-anchor="middle">5</text>
            <text x="97" y="123" font-size="9.5" font-weight="700" fill="#475569" text-anchor="middle">4 tens &rarr; 3 tens, 12 - 7 = 5</text>
          </g>
        </svg>"""
    },
    {
        "id": "e3-03",
        "number": 3,
        "subject": "maths",
        "subject_label": "Maths",
        "level": "e3",
        "level_label": "Entry Level 3",
        "strand_name": "Number System",
        "strand_theme": "amber",
        "dfe_code": "DfE E3.N3",
        "title": "Multiplying 2-Digit Numbers",
        "rule_heading": "Partition into Tens &amp; Ones (Grid Method)",
        "rule_body": "To multiply a 2-digit number by a single digit (e.g. 24 × 6), split 24 into 20 and 4. Multiply each part by 6 (20×6 = 120, 4×6 = 24), then add the answers together.",
        "golden_rule": "When multiplying by 10, move digits one place left and place a 0 at the end!",
        "watch_out": "Don't forget the zero when multiplying the Tens part: 30 × 4 = 120, NOT 12!",
        "challenge_prompt": "A crate holds 36 bottles of water. How many bottles are in 4 crates?",
        "answer_text": "Partition 36 into 30 + 6. (30 × 4 = 120) + (6 × 4 = 24) = 144 bottles.",
        "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(30, 18)">
            <rect x="0" y="0" width="400" height="132" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="200" y="24" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle">GRID METHOD: 24 × 6 = 144</text>
            <rect x="30" y="38" width="60" height="34" fill="#e2e8f0" stroke="#94a3b8"/>
            <text x="60" y="60" font-size="13" font-weight="900" fill="#0f172a" text-anchor="middle">×</text>
            <rect x="90" y="38" width="100" height="34" fill="#dbeafe" stroke="#3b82f6"/>
            <text x="140" y="60" font-size="13" font-weight="900" fill="#1e40af" text-anchor="middle">20</text>
            <rect x="190" y="38" width="80" height="34" fill="#dbeafe" stroke="#3b82f6"/>
            <text x="230" y="60" font-size="13" font-weight="900" fill="#1e40af" text-anchor="middle">4</text>
            <rect x="30" y="72" width="60" height="42" fill="#fef3c7" stroke="#f59e0b"/>
            <text x="60" y="98" font-size="13" font-weight="900" fill="#92400e" text-anchor="middle">6</text>
            <rect x="90" y="72" width="100" height="42" fill="#ffffff" stroke="#cbd5e1"/>
            <text x="140" y="98" font-size="13" font-weight="800" fill="#059669" text-anchor="middle">120</text>
            <rect x="190" y="72" width="80" height="42" fill="#ffffff" stroke="#cbd5e1"/>
            <text x="230" y="98" font-size="13" font-weight="800" fill="#059669" text-anchor="middle">24</text>
            <text x="335" y="78" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">120 + 24</text>
            <text x="335" y="102" font-size="15" font-weight="900" fill="#059669" text-anchor="middle">= 144</text>
          </g>
        </svg>"""
    },
    {
        "id": "e3-04",
        "number": 4,
        "subject": "maths",
        "subject_label": "Maths",
        "level": "e3",
        "level_label": "Entry Level 3",
        "strand_name": "Number System",
        "strand_theme": "amber",
        "dfe_code": "DfE E3.N4",
        "title": "Division &amp; Interpreting Remainders",
        "rule_heading": "Bus Stop Division • Round Up or Down in Context",
        "rule_body": "Divide from left to right. Any leftover amount is the remainder (r). In real-life problems, decide whether to round UP (e.g. minibuses/boxes needed) or round DOWN (what you can afford).",
        "golden_rule": 'Round UP when booking seats or buying tins so nothing is left short!',
        "watch_out": "If asked for 'full packs', ignore remainder and round DOWN.",
        "challenge_prompt": "50 care home residents are going on a trip. Each minibus holds 8 people. How many minibuses are needed?",
        "answer_text": "50 ÷ 8 = 6 remainder 2. Because 2 people cannot be left behind, round UP to 7 minibuses.",
        "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(30, 18)">
            <rect x="0" y="0" width="400" height="132" rx="8" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.8"/>
            <text x="200" y="24" font-size="12" font-weight="900" fill="#92400e" text-anchor="middle">REAL-LIFE REMAINDER: 50 ÷ 8 = 6 r 2</text>
            <rect x="20" y="40" width="170" height="75" rx="6" fill="#ffffff" stroke="#d97706"/>
            <text x="105" y="64" font-size="11" font-weight="800" fill="#0f172a" text-anchor="middle">6 × 8 = 48 people</text>
            <text x="105" y="86" font-size="11" font-weight="800" fill="#dc2626" text-anchor="middle">2 people left over (r 2)</text>
            <rect x="210" y="40" width="170" height="75" rx="6" fill="#ecfdf5" stroke="#10b981"/>
            <text x="295" y="64" font-size="11" font-weight="900" fill="#047857" text-anchor="middle">Boxes / Buses Needed?</text>
            <text x="295" y="88" font-size="12" font-weight="900" fill="#059669" text-anchor="middle">ROUND UP → 7 Buses!</text>
          </g>
        </svg>"""
    },
    {
        "id": "e3-05",
        "number": 5,
        "subject": "maths",
        "subject_label": "Maths",
        "level": "e3",
        "level_label": "Entry Level 3",
        "strand_name": "Number System",
        "strand_theme": "amber",
        "dfe_code": "DfE E3.N5",
        "title": "Rounding to Nearest 10 &amp; 100",
        "rule_heading": "5 or More Rounds Up • 4 or Less Stays Same",
        "rule_body": "To round to the nearest 10, look at the Ones digit. To round to the nearest 100, look at the Tens digit. If that neighbour digit is 5, 6, 7, 8, or 9, round UP; if 0–4, stay the same.",
        "golden_rule": "Use rounded numbers to ESTIMATE and check if your calculator answer is sensible!",
        "watch_out": "When rounding 674 to the nearest 100, look at the Tens digit (7), NOT the Ones digit (4)!",
        "challenge_prompt": "Round 463: (a) to the nearest 10, and (b) to the nearest 100.",
        "answer_text": "(a) Nearest 10: Ones digit is 3 (< 5) → 460. (b) Nearest 100: Tens digit is 6 (≥ 5) → 500.",
        "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(30, 18)">
            <rect x="0" y="0" width="400" height="132" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="200" y="26" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle">ROUNDING RULE: CHECK THE NEIGHBOUR DIGIT</text>
            <rect x="20" y="42" width="170" height="72" rx="6" fill="#eff6ff" stroke="#3b82f6"/>
            <text x="105" y="64" font-size="11" font-weight="900" fill="#1e40af" text-anchor="middle">0, 1, 2, 3, 4</text>
            <text x="105" y="88" font-size="11" font-weight="800" fill="#475569" text-anchor="middle">ROUND DOWN (Stay)</text>
            <text x="105" y="106" font-size="10" font-weight="700" fill="#1e40af" text-anchor="middle">342 → 340 (nearest 10)</text>
            <rect x="210" y="42" width="170" height="72" rx="6" fill="#ecfdf5" stroke="#10b981"/>
            <text x="295" y="64" font-size="11" font-weight="900" fill="#047857" text-anchor="middle">5, 6, 7, 8, 9</text>
            <text x="295" y="88" font-size="11" font-weight="800" fill="#047857" text-anchor="middle">ROUND UP (+1)</text>
            <text x="295" y="106" font-size="10" font-weight="700" fill="#059669" text-anchor="middle">368 → 400 (nearest 100)</text>
          </g>
        </svg>"""
    },
    {
        "id": "e3-06",
        "number": 6,
        "subject": "maths",
        "subject_label": "Maths",
        "level": "e3",
        "level_label": "Entry Level 3",
        "strand_name": "Number System",
        "strand_theme": "amber",
        "dfe_code": "DfE E3.N7",
        "title": "Fractions: Thirds, Quarters, Fifths &amp; Tenths",
        "rule_heading": "Divide by the Bottom • Multiply by the Top",
        "rule_body": "A fraction splits a whole into equal parts. To find a fraction of an amount (e.g. 3/4 of £20): Step 1: Divide the amount by the bottom number (20 ÷ 4 = 5). Step 2: Multiply by the top number (5 × 3 = £15).",
        "golden_rule": "Divide by the bottom (denominator), then times by the top (numerator)!",
        "watch_out": "1/3 is BIGGER than 1/5 — a smaller bottom number means larger slices!",
        "challenge_prompt": "A jacket costs £45. It is reduced by 1/5 in a sale. How much money is taken off?",
        "answer_text": "1/5 of £45 = 45 ÷ 5 = £9 taken off.",
        "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(30, 18)">
            <rect x="0" y="0" width="400" height="132" rx="8" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.8"/>
            <text x="200" y="24" font-size="12" font-weight="900" fill="#92400e" text-anchor="middle">FIND 3/4 OF £20 = £15</text>
            <rect x="30" y="38" width="85" height="40" fill="#fde68a" stroke="#d97706" stroke-width="1.8"/>
            <text x="72" y="63" font-size="13" font-weight="900" fill="#92400e" text-anchor="middle">£5</text>
            <rect x="115" y="38" width="85" height="40" fill="#fde68a" stroke="#d97706" stroke-width="1.8"/>
            <text x="157" y="63" font-size="13" font-weight="900" fill="#92400e" text-anchor="middle">£5</text>
            <rect x="200" y="38" width="85" height="40" fill="#fde68a" stroke="#d97706" stroke-width="1.8"/>
            <text x="242" y="63" font-size="13" font-weight="900" fill="#92400e" text-anchor="middle">£5</text>
            <rect x="285" y="38" width="85" height="40" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="327" y="63" font-size="13" font-weight="700" fill="#94a3b8" text-anchor="middle">£5</text>
            <text x="200" y="102" font-size="11" font-weight="800" fill="#0f172a" text-anchor="middle">Step 1: £20 ÷ 4 = £5 per quarter   |   Step 2: £5 × 3 = £15</text>
          </g>
        </svg>"""
    },
    {
        "id": "e3-07",
        "number": 7,
        "subject": "maths",
        "subject_label": "Maths",
        "level": "e3",
        "level_label": "Entry Level 3",
        "strand_name": "Number System",
        "strand_theme": "amber",
        "dfe_code": "DfE E3.N8",
        "title": "Decimals up to 2 Decimal Places",
        "rule_heading": "Line Up the Decimal Points Vertically",
        "rule_body": "Decimals show tenths (0.1) and hundredths (0.01), just like pounds and pence (£3.45). When adding or subtracting decimals, always line up the decimal points in a straight vertical column.",
        "golden_rule": 'Add a trailing zero (0.5 = 0.50) so both numbers have 2 decimals!',
        "watch_out": '0.4 is larger than 0.25 because 0.40 has 4 tenths while 0.25 has 2.',
        "challenge_prompt": "Put these lengths in order from shortest to longest: 1.45 m, 1.8 m, 1.09 m.",
        "answer_text": "Write with 2 decimal places: 1.45 m, 1.80 m, 1.09 m. Order: 1.09 m, 1.45 m, 1.8 m.",
        "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(30, 18)">
            <rect x="0" y="0" width="400" height="132" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="200" y="25" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle">COMPARING DECIMALS: PAD WITH ZEROES</text>
            <text x="200" y="58" font-family="monospace" font-size="14" font-weight="800" fill="#2563eb" text-anchor="middle">1.8 m  →  1.80 m (Largest)</text>
            <text x="200" y="84" font-family="monospace" font-size="14" font-weight="800" fill="#059669" text-anchor="middle">1.45 m →  1.45 m (Middle) </text>
            <text x="200" y="110" font-family="monospace" font-size="14" font-weight="800" fill="#d97706" text-anchor="middle">1.09 m →  1.09 m (Smallest)</text>
          </g>
        </svg>"""
    },
    {
        "id": "e3-08",
        "number": 8,
        "subject": "maths",
        "subject_label": "Maths",
        "level": "e3",
        "level_label": "Entry Level 3",
        "strand_name": "Measures & Money",
        "strand_theme": "emerald",
        "dfe_code": "DfE E3.M10",
        "title": "Money: Pounds, Pence &amp; Change",
        "rule_heading": "£1 = 100p • Never Mix £ and p Signs",
        "rule_body": "Convert pence to pounds by dividing by 100 (e.g. 245p = £2.45). Write money with either a £ sign and 2 decimal places (£0.65) OR a p sign (65p), never both (£0.65p is wrong).",
        "golden_rule": "Always write two digits after the dot for pounds: £4.5 on a calculator must be written as £4.50!",
        "watch_out": "Before adding 85p and £2.40, convert 85p into £0.85 so both are in pounds!",
        "challenge_prompt": "You buy a sandwich for £3.25 and a tea for 90p. How much change do you get from a £10 note?",
        "answer_text": "90p = £0.90. Total cost = £3.25 + £0.90 = £4.15. Change = £10.00 - £4.15 = £5.85.",
        "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(30, 18)">
            <rect x="0" y="0" width="400" height="132" rx="8" fill="#ecfdf5" stroke="#10b981" stroke-width="1.8"/>
            <text x="200" y="25" font-size="12" font-weight="900" fill="#047857" text-anchor="middle">MONEY NOTATION &amp; CHANGE</text>
            <rect x="20" y="40" width="170" height="72" rx="6" fill="#ffffff" stroke="#10b981"/>
            <text x="105" y="64" font-size="11.5" font-weight="900" fill="#059669" text-anchor="middle">✓ CORRECT</text>
            <text x="105" y="88" font-size="11" font-weight="800" fill="#0f172a" text-anchor="middle">£0.75  or  75p</text>
            <text x="105" y="106" font-size="11" font-weight="800" fill="#0f172a" text-anchor="middle">£4.50 (2 dec places)</text>
            <rect x="210" y="40" width="170" height="72" rx="6" fill="#fff1f2" stroke="#f43f5e"/>
            <text x="295" y="64" font-size="11.5" font-weight="900" fill="#be123c" text-anchor="middle">✗ WRONG</text>
            <text x="295" y="88" font-size="11" font-weight="800" fill="#be123c" text-anchor="middle">£0.75p (mixed signs)</text>
            <text x="295" y="106" font-size="11" font-weight="800" fill="#be123c" text-anchor="middle">£4.5 (missing zero)</text>
          </g>
        </svg>"""
    },
    {
        "id": "e3-09",
        "number": 9,
        "subject": "maths",
        "subject_label": "Maths",
        "level": "e3",
        "level_label": "Entry Level 3",
        "strand_name": "Measures & Money",
        "strand_theme": "emerald",
        "dfe_code": "DfE E3.M12",
        "title": "Time: Roman Numerals, 12-Hour &amp; 24-Hour",
        "rule_heading": "Add 12 to PM Hours • 1 Hour = 60 Minutes",
        "rule_body": "On clock faces: IV = 4, VI = 6, IX = 9, XII = 12. For 24-hour time, add 12 to afternoon (pm) hours from 1:00 pm onwards (e.g. 3:15 pm → 15:15). Count time intervals across the top of the hour (:00).",
        "golden_rule": "There are 60 minutes in 1 hour — never use column subtraction as if 1 hour had 100 minutes!",
        "watch_out": "12:30 pm stays 12:30 in 24-hour time; 12:30 am (midnight) becomes 00:30.",
        "challenge_prompt": "A shift starts at 9:40 am and finishes at 2:15 pm (14:15). How long is the shift in hours and minutes?",
        "answer_text": "9:40 am to 10:00 am = 20 mins. 10:00 am to 2:00 pm = 4 hours. 2:00 pm to 2:15 pm = 15 mins. Total = 4 hours 35 minutes.",
        "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(30, 18)">
            <rect x="0" y="0" width="400" height="132" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="200" y="25" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle">TIME JUMP LINE: 09:40 TO 14:15</text>
            <line x1="40" y1="78" x2="360" y2="78" stroke="#2563eb" stroke-width="3"/>
            <circle cx="40" cy="78" r="5" fill="#1e40af"/><text x="40" y="102" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">09:40</text>
            <circle cx="140" cy="78" r="5" fill="#1e40af"/><text x="140" y="102" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">10:00</text>
            <circle cx="270" cy="78" r="5" fill="#1e40af"/><text x="270" y="102" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">14:00</text>
            <circle cx="360" cy="78" r="5" fill="#1e40af"/><text x="360" y="102" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">14:15</text>
            <text x="90" y="62" font-size="10.5" font-weight="800" fill="#059669" text-anchor="middle">+20m</text>
            <text x="205" y="62" font-size="10.5" font-weight="800" fill="#2563eb" text-anchor="middle">+4 hrs</text>
            <text x="315" y="62" font-size="10.5" font-weight="800" fill="#059669" text-anchor="middle">+15m</text>
            <text x="200" y="122" font-size="11" font-weight="900" fill="#059669" text-anchor="middle">Total = 4 hours 35 minutes</text>
          </g>
        </svg>"""
    },
    {
        "id": "e3-10",
        "number": 10,
        "subject": "maths",
        "subject_label": "Maths",
        "level": "e3",
        "level_label": "Entry Level 3",
        "strand_name": "Measures & Money",
        "strand_theme": "emerald",
        "dfe_code": "DfE E3.M14",
        "title": "Metric Units: Length, Weight &amp; Capacity",
        "rule_heading": "1 m = 100 cm • 1 kg = 1,000 g • 1 L = 1,000 ml",
        "rule_body": "Length: 1 cm = 10 mm, 1 m = 100 cm, 1 km = 1,000 m. Weight: 1 kg = 1,000 g. Capacity: 1 Litre = 1,000 ml. Always convert to the SAME unit before adding or comparing.",
        "golden_rule": "'Kilo' (km, kg) and 'Milli' (ml, mm in a m) mean 1,000; 'Centi' (cm) means 100!",
        "watch_out": "1 metre is 100 cm (NOT 1,000 cm!). Half a kilogram (0.5 kg) is 500 g.",
        "challenge_prompt": "A jug holds 2 Litres of juice. You pour out three 250 ml glasses. How many millilitres (ml) are left in the jug?",
        "answer_text": "2 Litres = 2,000 ml. Poured out: 3 × 250 ml = 750 ml. Left: 2,000 - 750 = 1,250 ml (or 1.25 L).",
        "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(20, 18)">
            <rect x="0" y="0" width="132" height="132" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="66" y="25" font-size="11" font-weight="900" fill="#1e40af" text-anchor="middle">LENGTH</text>
            <text x="66" y="55" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">1 cm = 10 mm</text>
            <text x="66" y="80" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">1 m = 100 cm</text>
            <text x="66" y="105" font-size="10.5" font-weight="800" fill="#1e40af" text-anchor="middle">1 km = 1,000 m</text>
          </g>
          <g transform="translate(164, 18)">
            <rect x="0" y="0" width="132" height="132" rx="8" fill="#ecfdf5" stroke="#10b981" stroke-width="1.8"/>
            <text x="66" y="25" font-size="11" font-weight="900" fill="#047857" text-anchor="middle">WEIGHT</text>
            <text x="66" y="60" font-size="11" font-weight="800" fill="#0f172a" text-anchor="middle">1 kg = 1,000 g</text>
            <text x="66" y="95" font-size="10.5" font-weight="800" fill="#059669" text-anchor="middle">½ kg = 500 g</text>
          </g>
          <g transform="translate(308, 18)">
            <rect x="0" y="0" width="132" height="132" rx="8" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.8"/>
            <text x="66" y="25" font-size="11" font-weight="900" fill="#92400e" text-anchor="middle">CAPACITY</text>
            <text x="66" y="60" font-size="11" font-weight="800" fill="#0f172a" text-anchor="middle">1 L = 1,000 ml</text>
            <text x="66" y="95" font-size="10.5" font-weight="800" fill="#d97706" text-anchor="middle">½ L = 500 ml</text>
          </g>
        </svg>"""
    },
    {
        "id": "e3-11",
        "number": 11,
        "subject": "maths",
        "subject_label": "Maths",
        "level": "e3",
        "level_label": "Entry Level 3",
        "strand_name": "Measures & Money",
        "strand_theme": "emerald",
        "dfe_code": "DfE E3.M18",
        "title": "Reading Scales &amp; Dials",
        "rule_heading": "Find the Gap Divided by the Number of Steps",
        "rule_body": "To read an unlabelled tick mark on a scale, thermometer, or weighing dial: (1) Subtract two neighbouring numbered marks to find the gap, then (2) Divide by the number of spaces between them.",
        "golden_rule": "Count the SPACES (jumps) between numbered marks, not the lines!",
        "watch_out": "If there are 5 spaces between 0 g and 100 g, each mark is 100 ÷ 5 = 20 g (not 10 g!).",
        "challenge_prompt": "A kitchen scale has 4 equal spaces between 200 g and 400 g. The pointer is 1 mark past 200 g. What is the weight?",
        "answer_text": "Gap = 400 - 200 = 200 g. Step size = 200 ÷ 4 = 50 g per mark. Weight = 200 + 50 = 250 g.",
        "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(30, 18)">
            <rect x="0" y="0" width="400" height="132" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="200" y="25" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle">READING UNLABELLED DIVISIONS (200g TO 400g)</text>
            <line x1="60" y1="75" x2="340" y2="75" stroke="#334155" stroke-width="3"/>
            <line x1="60" y1="60" x2="60" y2="90" stroke="#0f172a" stroke-width="3"/><text x="60" y="108" font-size="11" font-weight="900" fill="#0f172a" text-anchor="middle">200 g</text>
            <line x1="130" y1="65" x2="130" y2="85" stroke="#dc2626" stroke-width="3"/><text x="130" y="54" font-size="11" font-weight="900" fill="#dc2626" text-anchor="middle">▼ 250 g</text>
            <line x1="200" y1="65" x2="200" y2="85" stroke="#475569" stroke-width="2"/><text x="200" y="108" font-size="10" font-weight="700" fill="#64748b" text-anchor="middle">300 g</text>
            <line x1="270" y1="65" x2="270" y2="85" stroke="#475569" stroke-width="2"/><text x="270" y="108" font-size="10" font-weight="700" fill="#64748b" text-anchor="middle">350 g</text>
            <line x1="340" y1="60" x2="340" y2="90" stroke="#0f172a" stroke-width="3"/><text x="340" y="108" font-size="11" font-weight="900" fill="#0f172a" text-anchor="middle">400 g</text>
            <text x="200" y="125" font-size="10.5" font-weight="800" fill="#059669" text-anchor="middle">Gap = 200 g ÷ 4 spaces = 50 g per division</text>
          </g>
        </svg>"""
    },
    {
        "id": "e3-12",
        "number": 12,
        "subject": "maths",
        "subject_label": "Maths",
        "level": "e3",
        "level_label": "Entry Level 3",
        "strand_name": "Shape & Space",
        "strand_theme": "emerald",
        "dfe_code": "DfE E3.M19",
        "title": "2D &amp; 3D Shapes, Right Angles &amp; Symmetry",
        "rule_heading": "Faces, Edges &amp; Vertices • 90° Right Angles",
        "rule_body": "A right angle (90°) is a square corner like a book edge. A line of symmetry folds a 2D shape into two matching halves. 3D shapes have flat/curved Faces, Edges, and Vertices (corners).",
        "golden_rule": "A cuboid (box) has 6 rectangular faces, 12 edges, and 8 vertices (corners)!",
        "watch_out": "A rectangle has 2 lines of symmetry (vertical & horizontal), NOT 4 — folding diagonally does not match!",
        "challenge_prompt": "How many faces, edges, and vertices does a cube have, and how many right angles are inside a rectangle?",
        "answer_text": "Cube: 6 faces, 12 edges, 8 vertices. A rectangle has 4 right angles (90° corners).",
        "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(25, 18)">
            <rect x="0" y="0" width="195" height="132" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="97" y="24" font-size="11" font-weight="900" fill="#1e40af" text-anchor="middle">RIGHT ANGLE &amp; SYMMETRY</text>
            <rect x="45" y="42" width="105" height="58" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2"/>
            <line x1="97.5" y1="35" x2="97.5" y2="108" stroke="#dc2626" stroke-width="2" stroke-dasharray="4,3"/>
            <rect x="45" y="88" width="12" height="12" fill="none" stroke="#059669" stroke-width="2"/>
            <text x="97" y="122" font-size="10" font-weight="800" fill="#0f172a" text-anchor="middle">4 Right Angles (90° corners)</text>
          </g>
          <g transform="translate(240, 18)">
            <rect x="0" y="0" width="195" height="132" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
            <text x="97" y="24" font-size="11" font-weight="900" fill="#15803d" text-anchor="middle">3D SHAPE PROPERTIES</text>
            <text x="15" y="54" font-size="10.5" font-weight="800" fill="#0f172a">• Cube/Cuboid: 6 Faces,</text>
            <text x="25" y="70" font-size="10" font-weight="700" fill="#475569">12 Edges, 8 Vertices</text>
            <text x="15" y="94" font-size="10.5" font-weight="800" fill="#0f172a">• Cylinder: 3 Faces (2 flat,</text>
            <text x="25" y="110" font-size="10" font-weight="700" fill="#475569">1 curved), 2 Edges, 0 Vertices</text>
          </g>
        </svg>"""
    },
    {
        "id": "e3-13",
        "number": 13,
        "subject": "maths",
        "subject_label": "Maths",
        "level": "e3",
        "level_label": "Entry Level 3",
        "strand_name": "Shape & Space",
        "strand_theme": "emerald",
        "dfe_code": "DfE E3.M20",
        "title": "Compass Directions &amp; Turns",
        "rule_heading": "Never Eat Shredded Wheat (N • E • S • W)",
        "rule_body": "The 8 compass points go clockwise: North (N), North-East (NE), East (E), South-East (SE), South (S), South-West (SW), West (W), North-West (NW). A quarter turn is 1 right angle (90°).",
        "golden_rule": 'Clockwise follows clock hands; Anti-clockwise turns the opposite way!',
        "watch_out": 'Check the facing direction before calculating quarter or half turns.',
        "challenge_prompt": "You are facing North. You turn a quarter-turn (90°) anti-clockwise. Which direction are you facing now?",
        "answer_text": "Facing West (1 quarter-turn anti-clockwise from North).",
        "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(30, 18)">
            <rect x="0" y="0" width="400" height="132" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <g transform="translate(105, 66)">
              <circle cx="0" cy="0" r="42" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>
              <line x1="0" y1="-42" x2="0" y2="42" stroke="#2563eb" stroke-width="2"/>
              <line x1="-42" y1="0" x2="42" y2="0" stroke="#2563eb" stroke-width="2"/>
              <text x="0" y="-46" font-size="11" font-weight="900" fill="#dc2626" text-anchor="middle">N</text>
              <text x="50" y="4" font-size="11" font-weight="900" fill="#1e40af" text-anchor="middle">E</text>
              <text x="0" y="55" font-size="11" font-weight="900" fill="#1e40af" text-anchor="middle">S</text>
              <text x="-52" y="4" font-size="11" font-weight="900" fill="#1e40af" text-anchor="middle">W</text>
            </g>
            <g transform="translate(205, 25)">
              <text x="0" y="20" font-size="11" font-weight="900" fill="#0f172a">8-POINT COMPASS &amp; TURNS</text>
              <text x="0" y="44" font-size="10" font-weight="700" fill="#475569">• Quarter turn = 1 right angle (N → E)</text>
              <text x="0" y="66" font-size="10" font-weight="700" fill="#475569">• Half turn = Opposite way (N → S)</text>
              <text x="0" y="88" font-size="10" font-weight="800" fill="#059669">• Diagonal points: NE, SE, SW, NW</text>
            </g>
          </g>
        </svg>"""
    },
    {
        "id": "e3-14",
        "number": 14,
        "subject": "maths",
        "subject_label": "Maths",
        "level": "e3",
        "level_label": "Entry Level 3",
        "strand_name": "Handling Data",
        "strand_theme": "purple",
        "dfe_code": "DfE E3.HD21",
        "title": "Bar Charts, Pictograms &amp; Tally Tables",
        "rule_heading": "Always Check the Pictogram Key First!",
        "rule_body": "In a pictogram, one symbol often stands for 2, 4, or 10 items — always read the Key first! In a bar chart, read across from the top of the bar to the vertical frequency axis.",
        "golden_rule": "If 1 circle = 4 items, then half a circle = 2 items and a quarter circle = 1 item!",
        "watch_out": "Never count pictogram symbols as '1 each' without checking the Key box!",
        "challenge_prompt": "In a pictogram, Key: 1 star = 4 books. Monday shows 3 full stars and a half star. How many books were borrowed on Monday?",
        "answer_text": "3 full stars = 3 × 4 = 12 books. Half star = 4 ÷ 2 = 2 books. Total = 12 + 2 = 14 books.",
        "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(30, 18)">
            <rect x="0" y="0" width="400" height="132" rx="8" fill="#f5f3ff" stroke="#8b5cf6" stroke-width="1.8"/>
            <text x="200" y="24" font-size="12" font-weight="900" fill="#5b21b6" text-anchor="middle">PICTOGRAM KEY RULE: 1 CIRCLE (●) = 4 ITEMS</text>
            <rect x="25" y="38" width="350" height="44" rx="6" fill="#ffffff" stroke="#c4b5fd"/>
            <text x="45" y="65" font-size="12" font-weight="800" fill="#0f172a">Monday:</text>
            <circle cx="135" cy="60" r="11" fill="#7c3aed"/>
            <circle cx="165" cy="60" r="11" fill="#7c3aed"/>
            <circle cx="195" cy="60" r="11" fill="#7c3aed"/>
            <path d="M 225,49 A 11,11 0 0,0 225,71 Z" fill="#7c3aed"/>
            <text x="305" y="65" font-size="12" font-weight="900" fill="#059669" text-anchor="middle">4 + 4 + 4 + 2 = 14</text>
            <text x="200" y="108" font-size="10.5" font-weight="800" fill="#4c1d95" text-anchor="middle">Full symbol = 4   |   Half symbol = 2   |   Quarter symbol = 1</text>
          </g>
        </svg>"""
    },

    # =========================================================================
    # ENTRY LEVEL 3 ENGLISH (#15 - #24)
    # =========================================================================
    {
        "id": "e3-15",
        "number": 15,
        "subject": "english",
        "subject_label": "English",
        "level": "e3",
        "level_label": "Entry Level 3",
        "strand_name": "Reading Basics",
        "strand_theme": "blue",
        "dfe_code": "DfE E3.R8",
        "title": "Main Purpose of a Text",
        "rule_heading": "To Inform • To Instruct • To Persuade",
        "rule_body": "Every text has a main purpose: To Inform (gives facts, dates, or news), To Instruct (step-by-step recipes or safety rules using command verbs), or To Persuade (adverts encouraging you to buy or join).",
        "golden_rule": 'When naming purpose, state both the verb AND topic (e.g. To warn about)!',
        "watch_out": "Never just write 'To inform' — write 'To inform staff about fire rules'.",
        "challenge_prompt": "A leaflet titled '5 Easy Steps to Reset Your Work Password' uses numbered steps. What is its main purpose?",
        "answer_text": "To instruct (or explain to) staff how to reset their work password step by step.",
        "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(20, 18)">
            <rect x="0" y="0" width="132" height="132" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="66" y="26" font-size="11" font-weight="900" fill="#1e40af" text-anchor="middle">INFORM</text>
            <text x="66" y="55" font-size="10" font-weight="700" fill="#0f172a" text-anchor="middle">Gives facts, times</text>
            <text x="66" y="72" font-size="10" font-weight="700" fill="#0f172a" text-anchor="middle">&amp; details</text>
            <text x="66" y="102" font-size="9.5" font-weight="800" fill="#2563eb" text-anchor="middle">Notice / Timetable</text>
          </g>
          <g transform="translate(164, 18)">
            <rect x="0" y="0" width="132" height="132" rx="8" fill="#ecfdf5" stroke="#10b981" stroke-width="1.8"/>
            <text x="66" y="26" font-size="11" font-weight="900" fill="#047857" text-anchor="middle">INSTRUCT</text>
            <text x="66" y="55" font-size="10" font-weight="700" fill="#0f172a" text-anchor="middle">Numbered steps &amp;</text>
            <text x="66" y="72" font-size="10" font-weight="700" fill="#0f172a" text-anchor="middle">command verbs</text>
            <text x="66" y="102" font-size="9.5" font-weight="800" fill="#059669" text-anchor="middle">Recipe / Manual</text>
          </g>
          <g transform="translate(308, 18)">
            <rect x="0" y="0" width="132" height="132" rx="8" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.8"/>
            <text x="66" y="26" font-size="11" font-weight="900" fill="#92400e" text-anchor="middle">PERSUADE</text>
            <text x="66" y="55" font-size="10" font-weight="700" fill="#0f172a" text-anchor="middle">Encourages you to</text>
            <text x="66" y="72" font-size="10" font-weight="700" fill="#0f172a" text-anchor="middle">buy, join, or act</text>
            <text x="66" y="102" font-size="9.5" font-weight="800" fill="#d97706" text-anchor="middle">Poster / Advert</text>
          </g>
        </svg>"""
    },
    {
        "id": "e3-16",
        "number": 16,
        "subject": "english",
        "subject_label": "English",
        "level": "e3",
        "level_label": "Entry Level 3",
        "strand_name": "Reading Basics",
        "strand_theme": "blue",
        "dfe_code": "DfE E3.R9",
        "title": "Organizational Features (Headings &amp; Bullets)",
        "rule_heading": "Headings, Subheadings, Bullet Points &amp; Boxes",
        "rule_body": "Writers use organizational features to help readers find information fast: Headings show the main topic, Subheadings divide sections, Bullet points list key facts, and Text boxes highlight warnings or prices.",
        "golden_rule": 'Use subheadings like signposts to jump straight to the needed section!',
        "watch_out": 'Name the specific feature (e.g. Subheading, Table, Bullet points).',
        "challenge_prompt": "Why does a safety poster use bullet points instead of one long paragraph?",
        "answer_text": "Bullet points break up the text so key safety rules are quick and easy to read at a glance.",
        "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(30, 18)">
            <rect x="0" y="0" width="400" height="132" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="200" y="25" font-size="12" font-weight="900" fill="#1e40af" text-anchor="middle">LAYOUT FEATURES THAT HELP THE READER</text>
            <text x="25" y="54" font-size="10.5" font-weight="800" fill="#0f172a">• Main Heading: Grabs attention &amp; states overall topic</text>
            <text x="25" y="76" font-size="10.5" font-weight="800" fill="#2563eb">• Subheadings: Split text into clear, easy-to-scan sections</text>
            <text x="25" y="98" font-size="10.5" font-weight="800" fill="#059669">• Bullet Points / Numbered Lists: Make key steps stand out</text>
            <text x="25" y="120" font-size="10.5" font-weight="800" fill="#d97706">• Bold Text &amp; Captions: Highlight important words &amp; photos</text>
          </g>
        </svg>"""
    },
    {
        "id": "e3-17",
        "number": 17,
        "subject": "english",
        "subject_label": "English",
        "level": "e3",
        "level_label": "Entry Level 3",
        "strand_name": "Reading Basics",
        "strand_theme": "blue",
        "dfe_code": "DfE E3.R10",
        "title": "Using a Dictionary &amp; Alphabetical Order",
        "rule_heading": "Compare the 1st, 2nd, then 3rd Letter",
        "rule_body": "To put words in alphabetical (A–Z) order or look them up in a dictionary/index: compare the first letter. If the first letters are the same, compare the second letter (or third letter).",
        "golden_rule": 'Check the 3rd and 4th letters when words start with the same letters!',
        "watch_out": "'Staff' comes before 'Store' because 'a' precedes 'o' in the alphabet.",
        "challenge_prompt": "Put these four words in alphabetical order: Printer, Paper, Postcode, Folder.",
        "answer_text": "1. Folder (F), 2. Paper (Pa), 3. Postcode (Po), 4. Printer (Pr).",
        "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(30, 18)">
            <rect x="0" y="0" width="400" height="132" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="200" y="25" font-size="12" font-weight="900" fill="#1e40af" text-anchor="middle">ALPHABETICAL ORDER: CHECK THE NEXT LETTER</text>
            <rect x="25" y="38" width="350" height="24" rx="4" fill="#ffffff" stroke="#93c5fd"/>
            <text x="200" y="54" font-size="10.5" font-weight="800" fill="#1e3a8a" text-anchor="middle">A B C D E F G H I J K L M N O P Q R S T U V W X Y Z</text>
            <text x="200" y="84" font-size="11" font-weight="800" fill="#0f172a" text-anchor="middle">Compare: P<tspan fill="#dc2626">a</tspan>per  •  P<tspan fill="#dc2626">o</tspan>stcode  •  P<tspan fill="#dc2626">r</tspan>inter</text>
            <text x="200" y="110" font-size="11" font-weight="900" fill="#059669" text-anchor="middle">Since A → O → R: Paper, then Postcode, then Printer!</text>
          </g>
        </svg>"""
    },
    {
        "id": "e3-18",
        "number": 18,
        "subject": "english",
        "subject_label": "English",
        "level": "e3",
        "level_label": "Entry Level 3",
        "strand_name": "Everyday Writing",
        "strand_theme": "cyan",
        "dfe_code": "DfE E3.W18",
        "title": "Writing Emails &amp; Short Notes",
        "rule_heading": "To • Subject Line • Greeting • Paragraphs • Sign-Off",
        "rule_body": "Every Entry 3 email needs: (1) A clear Subject Line, (2) A polite greeting ('Dear Mr Patel,' or 'Hi Sarah,'), (3) Short paragraphs answering every bullet point in the task, and (4) A polite sign-off ('Kind regards,').",
        "golden_rule": 'Tick off each task bullet point to ensure full content marks are won!',
        "watch_out": 'Never leave the email Subject line blank — it costs an easy mark.',
        "challenge_prompt": "Write a clear Subject Line and Greeting for an email to your manager, Mrs Singh, requesting Friday off.",
        "answer_text": "Subject: Annual Leave Request – Friday 18 October | Greeting: Dear Mrs Singh,",
        "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(30, 15)">
            <rect x="0" y="0" width="400" height="138" rx="8" fill="#ffffff" stroke="#0891b2" stroke-width="2"/>
            <rect x="0" y="0" width="400" height="26" rx="8 8 0 0" fill="#cffafe"/>
            <text x="15" y="17" font-size="10.5" font-weight="900" fill="#155e75">✉️ EMAIL CHECKLIST (ENTRY LEVEL 3)</text>
            <text x="15" y="45" font-size="10.5" font-weight="800" fill="#0f172a">Subject: <tspan fill="#0891b2">Shift Swap Request – Tuesday 14 May</tspan></text>
            <line x1="15" y1="53" x2="385" y2="53" stroke="#e2e8f0"/>
            <text x="15" y="72" font-size="10.5" font-weight="800" fill="#0f172a">Dear Manager,</text>
            <text x="15" y="92" font-size="10" font-weight="600" fill="#475569">I am writing to ask if I can swap my Tuesday morning shift...</text>
            <text x="15" y="114" font-size="10.5" font-weight="800" fill="#059669">Kind regards,   Alex Carter</text>
          </g>
        </svg>"""
    },
    {
        "id": "e3-19",
        "number": 19,
        "subject": "english",
        "subject_label": "English",
        "level": "e3",
        "level_label": "Entry Level 3",
        "strand_name": "Everyday Writing",
        "strand_theme": "cyan",
        "dfe_code": "DfE E3.W19",
        "title": "Paragraphs &amp; Sequencing Ideas",
        "rule_heading": "Start a New Paragraph for Each New Topic",
        "rule_body": "Break your writing into at least 3 clear paragraphs: (1) Opening (why you are writing), (2) Middle (details and examples), and (3) Ending (what happens next). Use time linkers like First, Next, Then, Finally.",
        "golden_rule": 'Leave a clear blank line between paragraphs to show structure clearly!',
        "watch_out": 'Writing one giant block of text without breaks loses layout marks.',
        "challenge_prompt": "Give three sequencing words you can use to order instructions for a new colleague.",
        "answer_text": "First (or Firstly), Next (or Then / After that), and Finally.",
        "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(30, 18)">
            <rect x="0" y="0" width="400" height="132" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="200" y="24" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle">3-PARAGRAPH STRUCTURE + SEQUENCING WORDS</text>
            <rect x="20" y="38" width="110" height="76" rx="6" fill="#eff6ff" stroke="#3b82f6"/>
            <text x="75" y="58" font-size="10.5" font-weight="900" fill="#1e40af" text-anchor="middle">1. OPENING</text>
            <text x="75" y="78" font-size="9.5" font-weight="700" fill="#475569" text-anchor="middle">Why you are</text>
            <text x="75" y="94" font-size="9.5" font-weight="700" fill="#475569" text-anchor="middle">writing</text>
            <rect x="145" y="38" width="110" height="76" rx="6" fill="#ecfdf5" stroke="#10b981"/>
            <text x="200" y="58" font-size="10.5" font-weight="900" fill="#047857" text-anchor="middle">2. DETAILS</text>
            <text x="200" y="78" font-size="9.5" font-weight="700" fill="#475569" text-anchor="middle">First, Next,</text>
            <text x="200" y="94" font-size="9.5" font-weight="700" fill="#475569" text-anchor="middle">Also, Because</text>
            <rect x="270" y="38" width="110" height="76" rx="6" fill="#fffbeb" stroke="#f59e0b"/>
            <text x="325" y="58" font-size="10.5" font-weight="900" fill="#92400e" text-anchor="middle">3. ENDING</text>
            <text x="325" y="78" font-size="9.5" font-weight="700" fill="#475569" text-anchor="middle">Finally, action</text>
            <text x="325" y="94" font-size="9.5" font-weight="700" fill="#475569" text-anchor="middle">&amp; thank you</text>
          </g>
        </svg>"""
    },
    {
        "id": "e3-20",
        "number": 20,
        "subject": "english",
        "subject_label": "English",
        "level": "e3",
        "level_label": "Entry Level 3",
        "strand_name": "SPaG Foundations",
        "strand_theme": "teal",
        "dfe_code": "DfE E3.W13",
        "title": "Sentence Punctuation &amp; Capital Letters",
        "rule_heading": "M.I.N.T.S. Capitals • Full Stops • Question Marks",
        "rule_body": "Start every sentence with a Capital Letter and end with a Full Stop (.), Question Mark (?), or Exclamation Mark (!). Always capitalise Months/Days, the word 'I', Names of people, and Places (Oxford, Tuesday).",
        "golden_rule": 'Every question must end with a question mark (?), not a full stop!',
        "watch_out": "Don't join two complete sentences with a comma — use a full stop.",
        "challenge_prompt": "Fix the 4 errors in this sentence: 'on monday i am going to london, when does the train leave.'",
        "answer_text": "'On Monday I am going to London. When does the train leave?' (Capitals for On, Monday, I, London + Full Stop + Question Mark).",
        "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(30, 18)">
            <rect x="0" y="0" width="400" height="132" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
            <text x="200" y="25" font-size="12" font-weight="900" fill="#15803d" text-anchor="middle">M.I.N.T.S. CAPITAL LETTER CHECKLIST</text>
            <text x="25" y="52" font-size="10.5" font-weight="800" fill="#0f172a">M — Months &amp; Days: <tspan fill="#059669">Friday, November</tspan></text>
            <text x="25" y="74" font-size="10.5" font-weight="800" fill="#0f172a">I — The word 'I': <tspan fill="#059669">I work at the clinic.</tspan></text>
            <text x="25" y="96" font-size="10.5" font-weight="800" fill="#0f172a">N — Names &amp; Places: <tspan fill="#059669">Subi, Oxford, High Street</tspan></text>
            <text x="25" y="118" font-size="10.5" font-weight="800" fill="#0f172a">S — Start of Every Sentence (+ end with <tspan fill="#dc2626">.  ?  !</tspan>)</text>
          </g>
        </svg>"""
    },
    {
        "id": "e3-21",
        "number": 21,
        "subject": "english",
        "subject_label": "English",
        "level": "e3",
        "level_label": "Entry Level 3",
        "strand_name": "SPaG Foundations",
        "strand_theme": "teal",
        "dfe_code": "DfE E3.W14",
        "title": "Commas in Lists &amp; Apostrophes",
        "rule_heading": "Commas Separate List Items • Apostrophes for Missing Letters",
        "rule_body": "Use commas to separate items in a list ('We need pens, paper, folders and tape'). Use an apostrophe (') to show where letters are missing in contractions (don't = do not, can't = cannot, I'm = I am).",
        "golden_rule": "Put the apostrophe in the exact spot where the missing letter was taken out!",
        "watch_out": "Never put an apostrophe in simple plural words: 'Three coffees and two cakes' has NO apostrophe!",
        "challenge_prompt": "Add commas and an apostrophe to fix this sentence: 'Weve packed sandwiches apples crisps and water.'",
        "answer_text": "'We've packed sandwiches, apples, crisps and water.'",
        "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(25, 18)">
            <rect x="0" y="0" width="195" height="132" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="97" y="25" font-size="11" font-weight="900" fill="#1e40af" text-anchor="middle">COMMAS IN A LIST</text>
            <text x="15" y="55" font-size="10" font-weight="700" fill="#0f172a">"Bring a pen<tspan fill="#dc2626" font-weight="900">,</tspan> a notepad<tspan fill="#dc2626" font-weight="900">,</tspan></text>
            <text x="15" y="73" font-size="10" font-weight="700" fill="#0f172a">your ID badge and water."</text>
            <text x="15" y="104" font-size="9.5" font-weight="800" fill="#2563eb">Separates 3 or more items</text>
          </g>
          <g transform="translate(240, 18)">
            <rect x="0" y="0" width="195" height="132" rx="8" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.8"/>
            <text x="97" y="25" font-size="11" font-weight="900" fill="#92400e" text-anchor="middle">APOSTROPHE (OMISSION)</text>
            <text x="15" y="55" font-size="10.5" font-weight="800" fill="#0f172a">do not  →  don't</text>
            <text x="15" y="78" font-size="10.5" font-weight="800" fill="#0f172a">it is   →  it's</text>
            <text x="15" y="101" font-size="10.5" font-weight="800" fill="#059669">you are →  you're</text>
          </g>
        </svg>"""
    },
    {
        "id": "e3-22",
        "number": 22,
        "subject": "english",
        "subject_label": "English",
        "level": "e3",
        "level_label": "Entry Level 3",
        "strand_name": "SPaG Foundations",
        "strand_theme": "teal",
        "dfe_code": "DfE E3.W15",
        "title": "Subject-Verb Agreement (Was/Were &amp; Is/Are)",
        "rule_heading": "Singular Takes 'Is/Was' • Plural Takes 'Are/Were'",
        "rule_body": "Match the verb to the subject: One person/thing (I, he, she, it, the bus) takes 'is' or 'was'. More than one (we, they, the buses) and 'you' ALWAYS take 'are' or 'were' ('We were happy', NEVER 'We was').",
        "golden_rule": "Always write 'We were', 'They were', and 'You were' (never 'We was')!",
        "watch_out": "'There is' is for one item; 'There are' is for multiple items.",
        "challenge_prompt": "Choose the correct verbs: 'We (was / were) waiting at the stop because the buses (was / were) delayed.'",
        "answer_text": "'We were waiting at the stop because the buses were delayed.'",
        "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(25, 18)">
            <rect x="0" y="0" width="195" height="132" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="97" y="25" font-size="11" font-weight="900" fill="#1e40af" text-anchor="middle">SINGULAR (ONE)</text>
            <text x="15" y="54" font-size="10.5" font-weight="800" fill="#0f172a">• I was / He was / She was</text>
            <text x="15" y="78" font-size="10.5" font-weight="800" fill="#0f172a">• The train is / was late</text>
            <text x="15" y="102" font-size="10.5" font-weight="800" fill="#2563eb">• There is one seat left</text>
          </g>
          <g transform="translate(240, 18)">
            <rect x="0" y="0" width="195" height="132" rx="8" fill="#ecfdf5" stroke="#10b981" stroke-width="1.8"/>
            <text x="97" y="25" font-size="11" font-weight="900" fill="#047857" text-anchor="middle">PLURAL (2+ OR 'YOU')</text>
            <text x="15" y="54" font-size="10.5" font-weight="800" fill="#059669">• We were / They were</text>
            <text x="15" y="78" font-size="10.5" font-weight="800" fill="#059669">• You were (NEVER 'you was')</text>
            <text x="15" y="102" font-size="10.5" font-weight="800" fill="#047857">• There are many options</text>
          </g>
        </svg>"""
    },
    {
        "id": "e3-23",
        "number": 23,
        "subject": "english",
        "subject_label": "English",
        "level": "e3",
        "level_label": "Entry Level 3",
        "strand_name": "SPaG Foundations",
        "strand_theme": "teal",
        "dfe_code": "DfE E3.W17",
        "title": "Plurals (-s, -es, -ies) &amp; Common Spellings",
        "rule_heading": "Ch/Sh/S/X Add -es • Consonant + Y Changes to -ies",
        "rule_body": "Most nouns add -s for plurals. Words ending in -ch, -sh, -s, -x, or -z add -es (box → boxes, bus → buses). Words ending in a consonant + y drop the y and add -ies (baby → babies, city → cities).",
        "golden_rule": 'Consonant + y becomes -ies (party → parties); vowel + y adds -s!',
        "watch_out": 'Irregular plurals change completely: child → children, person → people.',
        "challenge_prompt": "Write the plural of these three words: (a) box   (b) family   (c) key",
        "answer_text": "(a) boxes (add -es)   (b) families (consonant + y → -ies)   (c) keys (vowel + y → add -s).",
        "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(30, 18)">
            <rect x="0" y="0" width="400" height="132" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="200" y="25" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle">THE 3 PLURAL SPELLING RULES</text>
            <text x="25" y="54" font-size="10.5" font-weight="800" fill="#2563eb">1. Ends in -s, -sh, -ch, -x → Add -ES:  box → boxes, watch → watches</text>
            <text x="25" y="80" font-size="10.5" font-weight="800" fill="#059669">2. Consonant + Y → Drop Y, add -IES:  city → cities, lorry → lorries</text>
            <text x="25" y="106" font-size="10.5" font-weight="800" fill="#d97706">3. Vowel + Y → Keep Y, add -S:  day → days, trolley → trolleys</text>
          </g>
        </svg>"""
    },
    {
        "id": "e3-24",
        "number": 24,
        "subject": "english",
        "subject_label": "English",
        "level": "e3",
        "level_label": "Entry Level 3",
        "strand_name": "Speaking & Listening",
        "strand_theme": "cyan",
        "dfe_code": "DfE E3.SLC1",
        "title": "SLC E3: Listening, Questions &amp; Turns",
        "rule_heading": "Listen Actively • Ask Relevant Questions • Take Turns",
        "rule_body": "In your Entry 3 Speaking & Listening discussion: (1) Listen carefully without interrupting, (2) State your views clearly with a reason ('I think... because...'), and (3) Ask at least two relevant questions to others.",
        "golden_rule": "Always add 'because...' to explain your reasons during discussions!",
        "watch_out": "Don't stay silent after speaking — invite others to share views.",
        "challenge_prompt": "Give one polite question you could ask a classmate during a discussion about local recycling.",
        "answer_text": '"How easy do you find it to use the recycling bins on your street?" (or "What could the council do to help people recycle more?").',
        "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(30, 18)">
            <rect x="0" y="0" width="400" height="132" rx="8" fill="#ecfdf5" stroke="#10b981" stroke-width="1.8"/>
            <text x="200" y="25" font-size="12" font-weight="900" fill="#047857" text-anchor="middle">ENTRY 3 SPEAKING &amp; LISTENING SUCCESS</text>
            <text x="25" y="54" font-size="10.5" font-weight="800" fill="#0f172a">✓ Speak Clearly: "I think we should... because..."</text>
            <text x="25" y="78" font-size="10.5" font-weight="800" fill="#2563eb">✓ Ask Questions: "What do you think is the best day for...?"</text>
            <text x="25" y="102" font-size="10.5" font-weight="800" fill="#059669">✓ Respect Turns: Nod, keep eye contact, and don't interrupt</text>
          </g>
        </svg>"""
    },

    # =========================================================================
    # ENTRY LEVEL 3 DIGITAL FUNCTIONAL SKILLS (#25 - #30)
    # =========================================================================
    {
        "id": "e3-25",
        "number": 25,
        "subject": "digital",
        "subject_label": "Digital Skills",
        "level": "e3",
        "level_label": "Entry Level 3",
        "strand_name": "Using Devices",
        "strand_theme": "orange",
        "dfe_code": "DFSQ E3.1",
        "title": "Device Settings, Wi-Fi &amp; Accessibility",
        "rule_heading": "Wi-Fi Padlock • Display Zoom • Volume &amp; Contrast",
        "rule_body": "Use your device Settings app to connect to secure Wi-Fi (look for the padlock icon), adjust screen brightness/text size for readability, and install system updates to fix security bugs.",
        "golden_rule": "Only connect to Wi-Fi networks that show a padlock icon and require a password!",
        "watch_out": "Never log into online banking on an open, unlocked public Wi-Fi network!",
        "challenge_prompt": "A colleague finds the text on their tablet screen too small to read. Which device setting should they adjust?",
        "answer_text": "Open Settings → Display / Accessibility → Increase Font Size (or Screen Zoom).",
        "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(30, 18)">
            <rect x="0" y="0" width="400" height="132" rx="8" fill="#fff7ed" stroke="#f97316" stroke-width="1.8"/>
            <text x="200" y="25" font-size="12" font-weight="900" fill="#9a3412" text-anchor="middle">ESSENTIAL DEVICE SETTINGS (ENTRY 3)</text>
            <text x="25" y="54" font-size="10.5" font-weight="800" fill="#0f172a">🔒 Secure Wi-Fi: Look for the padlock icon &amp; enter password</text>
            <text x="25" y="78" font-size="10.5" font-weight="800" fill="#2563eb">🔍 Accessibility: Increase Text Size, Zoom, or High Contrast</text>
            <text x="25" y="102" font-size="10.5" font-weight="800" fill="#059669">🔄 Software Updates: Install updates to patch security risks</text>
          </g>
        </svg>"""
    },
    {
        "id": "e3-26",
        "number": 26,
        "subject": "digital",
        "subject_label": "Digital Skills",
        "level": "e3",
        "level_label": "Entry Level 3",
        "strand_name": "Using Devices",
        "strand_theme": "orange",
        "dfe_code": "DFSQ E3.2",
        "title": "Files, Folders &amp; Keyboard Shortcuts",
        "rule_heading": "Clear File Names • Ctrl+C (Copy) • Ctrl+V (Paste)",
        "rule_body": "Save files into named folders with clear, descriptive filenames (e.g. 'CV_Alex_Carter.pdf', not 'doc1'). Essential shortcuts: Ctrl+C = Copy, Ctrl+X = Cut, Ctrl+V = Paste, Ctrl+Z = Undo, Ctrl+S = Save.",
        "golden_rule": 'Press Ctrl + Z immediately if you make a mistake to undo your action!',
        "watch_out": 'Know file extensions: .docx = Word, .pdf = Print, .png = Image.',
        "challenge_prompt": "Which keyboard shortcut copies selected text, and which shortcut pastes it into a new place?",
        "answer_text": "Ctrl + C copies the selected text; Ctrl + V pastes it.",
        "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(30, 18)">
            <rect x="0" y="0" width="400" height="132" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="200" y="25" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle">THE 4 GOLDEN KEYBOARD SHORTCUTS</text>
            <rect x="20" y="38" width="170" height="36" rx="6" fill="#eff6ff" stroke="#3b82f6"/>
            <text x="105" y="61" font-size="11" font-weight="900" fill="#1e40af" text-anchor="middle">Ctrl + C  =  COPY</text>
            <rect x="210" y="38" width="170" height="36" rx="6" fill="#ecfdf5" stroke="#10b981"/>
            <text x="295" y="61" font-size="11" font-weight="900" fill="#047857" text-anchor="middle">Ctrl + V  =  PASTE</text>
            <rect x="20" y="82" width="170" height="36" rx="6" fill="#fffbeb" stroke="#f59e0b"/>
            <text x="105" y="105" font-size="11" font-weight="900" fill="#92400e" text-anchor="middle">Ctrl + Z  =  UNDO</text>
            <rect x="210" y="82" width="170" height="36" rx="6" fill="#f5f3ff" stroke="#8b5cf6"/>
            <text x="295" y="105" font-size="11" font-weight="900" fill="#5b21b6" text-anchor="middle">Ctrl + S  =  SAVE</text>
          </g>
        </svg>"""
    },
    {
        "id": "e3-27",
        "number": 27,
        "subject": "digital",
        "subject_label": "Digital Skills",
        "level": "e3",
        "level_label": "Entry Level 3",
        "strand_name": "Creating & Editing",
        "strand_theme": "orange",
        "dfe_code": "DFSQ E3.6",
        "title": "Word Processing &amp; Formatting Documents",
        "rule_heading": "Bold (B) • Centre Align • Bullet Lists • Spellcheck",
        "rule_body": "In a poster or notice: make the main title Larger (18–24pt), Bold (B), and Centre-aligned. Keep body text Left-aligned (11–12pt) so it is easy to read, and use Bullet Points for lists.",
        "golden_rule": 'Right-click red wavy underlines to correct spellings before saving!',
        "watch_out": 'Keep body text left-aligned — never centre-align long paragraphs.',
        "challenge_prompt": "How should you format the main heading of a workplace safety notice so it stands out clearly?",
        "answer_text": "Make the heading Bold, increase the font size (e.g. 18–22pt), and Centre-align it at the top of the page.",
        "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(30, 18)">
            <rect x="0" y="0" width="400" height="132" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.8"/>
            <rect x="0" y="0" width="400" height="30" rx="8 8 0 0" fill="#f1f5f9"/>
            <text x="200" y="20" font-size="11" font-weight="900" fill="#0f172a" text-anchor="middle">[B] Bold   |   [I] Italic   |   [U] Underline   |   [•] Bullets</text>
            <text x="200" y="54" font-size="13" font-weight="900" fill="#1e40af" text-anchor="middle">STAFF FIRE SAFETY NOTICE (Bold, 18pt, Centred)</text>
            <text x="25" y="80" font-size="10.5" font-weight="700" fill="#0f172a">• Leave the building calmly via the nearest green exit sign.</text>
            <text x="25" y="100" font-size="10.5" font-weight="700" fill="#0f172a">• Report to Assembly Point B in the main car park.</text>
            <text x="25" y="120" font-size="9.5" font-weight="800" fill="#059669">(Body text: Left-aligned, 12pt, clean bullet points)</text>
          </g>
        </svg>"""
    },
    {
        "id": "e3-28",
        "number": 28,
        "subject": "digital",
        "subject_label": "Digital Skills",
        "level": "e3",
        "level_label": "Entry Level 3",
        "strand_name": "Creating & Editing",
        "strand_theme": "orange",
        "dfe_code": "DFSQ E3.8",
        "title": "Simple Spreadsheets &amp; Totals (=SUM)",
        "rule_heading": "Columns (A, B, C) • Rows (1, 2, 3) • Always Start with =",
        "rule_body": "Each box in a spreadsheet is a cell named by its Column letter and Row number (e.g. B4). Every formula MUST start with an equals sign (=): use =B2+B3 or =SUM(B2:B5) to add numbers.",
        "golden_rule": "Always begin spreadsheet formulas with '=' (e.g. =SUM(A1:A5))!",
        "watch_out": "Use '*' for multiply and '/' for divide — never type the letter 'x'.",
        "challenge_prompt": "Write the spreadsheet formula to add the costs in cells B2, B3, B4, and B5.",
        "answer_text": "=SUM(B2:B5)  (or =B2+B3+B4+B5).",
        "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(30, 18)">
            <rect x="0" y="0" width="400" height="132" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="200" y="24" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle">SPREADSHEET FORMULA SYMBOLS</text>
            <text x="25" y="54" font-family="monospace" font-size="11.5" font-weight="800" fill="#059669">=SUM(B2:B5)   → Adds all cells from B2 down to B5</text>
            <text x="25" y="78" font-family="monospace" font-size="11.5" font-weight="800" fill="#2563eb">=B2-C2        → Subtracts C2 from B2</text>
            <text x="25" y="102" font-family="monospace" font-size="11.5" font-weight="800" fill="#d97706">=B2*C2        → Multiplies B2 by C2 (* means ×)</text>
            <text x="25" y="122" font-family="monospace" font-size="11.5" font-weight="800" fill="#7c3aed">=B2/C2        → Divides B2 by C2 (/ means ÷)</text>
          </g>
        </svg>"""
    },
    {
        "id": "e3-29",
        "number": 29,
        "subject": "digital",
        "subject_label": "Digital Skills",
        "level": "e3",
        "level_label": "Entry Level 3",
        "strand_name": "Communicating Online",
        "strand_theme": "orange",
        "dfe_code": "DFSQ E3.10",
        "title": "Email Attachments, Reply vs Reply All",
        "rule_heading": "Paperclip = Attach File • Check Recipient Before Sending",
        "rule_body": "Click the Paperclip icon to attach a file (like a PDF or photo) to an email. Use 'Reply' to answer ONLY the sender; use 'Reply All' only when everyone on the thread needs to see your answer.",
        "golden_rule": "Always attach the file before sending if writing 'please find attached'!",
        "watch_out": "Never click 'Reply All' when sending sensitive personal information.",
        "challenge_prompt": "You receive a company-wide email from HR asking you to send your private bank details. Should you click 'Reply' or 'Reply All'?",
        "answer_text": "Click 'Reply' (so only HR receives your private details, NOT the entire company).",
        "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(25, 18)">
            <rect x="0" y="0" width="195" height="132" rx="8" fill="#ecfdf5" stroke="#10b981" stroke-width="1.8"/>
            <text x="97" y="25" font-size="11.5" font-weight="900" fill="#047857" text-anchor="middle">↩️ REPLY (ONE PERSON)</text>
            <text x="15" y="55" font-size="10" font-weight="700" fill="#0f172a">Sends your message ONLY</text>
            <text x="15" y="73" font-size="10" font-weight="700" fill="#0f172a">to the person who emailed</text>
            <text x="15" y="102" font-size="9.5" font-weight="800" fill="#059669">✓ Safe for private info</text>
          </g>
          <g transform="translate(240, 18)">
            <rect x="0" y="0" width="195" height="132" rx="8" fill="#fff7ed" stroke="#f97316" stroke-width="1.8"/>
            <text x="97" y="25" font-size="11.5" font-weight="900" fill="#9a3412" text-anchor="middle">📎 ATTACHMENTS</text>
            <text x="15" y="55" font-size="10" font-weight="700" fill="#0f172a">Click Paperclip icon (📎)</text>
            <text x="15" y="73" font-size="10" font-weight="700" fill="#0f172a">to attach a PDF or photo</text>
            <text x="15" y="102" font-size="9.5" font-weight="800" fill="#c2410c">✓ Check file name &amp; size</text>
          </g>
        </svg>"""
    },
    {
        "id": "e3-30",
        "number": 30,
        "subject": "digital",
        "subject_label": "Digital Skills",
        "level": "e3",
        "level_label": "Entry Level 3",
        "strand_name": "Being Safe & Secure",
        "strand_theme": "rose",
        "dfe_code": "DFSQ E3.12",
        "title": "Online Safety: Passwords &amp; Scams",
        "rule_heading": "3 Random Words + Symbols • Check HTTPS Padlock",
        "rule_body": "Create strong passwords using three random words plus numbers/symbols (e.g. 'Green#kettle42!'). When shopping or banking online, check the browser address bar starts with 'https://' and has a padlock icon.",
        "golden_rule": 'Never click links in unexpected security alerts or parcel texts!',
        "watch_out": "Never use obvious passwords like 'password123' or your date of birth.",
        "challenge_prompt": "State two signs that a text message claiming 'Your parcel is held—click here to pay £1.99' is a phishing scam.",
        "answer_text": "1. Urgent demand for payment via an unfamiliar web link. 2. Sent from an unknown mobile number with a generic greeting.",
        "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(30, 18)">
            <rect x="0" y="0" width="400" height="132" rx="8" fill="#fff1f2" stroke="#f43f5e" stroke-width="1.8"/>
            <text x="200" y="25" font-size="12" font-weight="900" fill="#9f1239" text-anchor="middle">3 GOLDEN RULES FOR STAYING SAFE ONLINE</text>
            <text x="25" y="54" font-size="10.5" font-weight="800" fill="#059669">1. Strong Password: 3 random words + numbers/symbols + 2FA code</text>
            <text x="25" y="78" font-size="10.5" font-weight="800" fill="#2563eb">2. Safe Websites: Check for https:// and the Padlock icon in URL bar</text>
            <text x="25" y="102" font-size="10.5" font-weight="800" fill="#be123c">3. Spot Phishing: Ignore urgent panic links &amp; fake sender addresses</text>
          </g>
        </svg>"""
    }
]
