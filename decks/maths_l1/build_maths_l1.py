#!/usr/bin/env python3
"""
Builder for Deck 2: Functional Skills Maths - Level 1 (38 Cards)
Full curriculum alignment with UK DfE and Pearson Edexcel / City & Guilds standards.
"""
import pprint
import xml.etree.ElementTree as ET

def wrap_svg(inner_content, height=170):
    svg = f'<svg viewBox="0 0 460 {height}" width="100%" height="{height}" xmlns="http://www.w3.org/2000/svg">\n{inner_content}\n</svg>'
    ET.fromstring(svg)
    return svg

CARDS_A = [
    # 1. Place Value up to 1,000,000
    {
        "id": "m-l1-01",
        "number": 1,
        "title": "Place Value up to 1,000,000",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Number System",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.N1",
        "rule_heading": "Millions, Thousands &amp; Ones",
        "rule_body": "Numbers are grouped in 3-digit periods separated by commas or spaces: Millions (M), Hundred Thousands (HTh), Ten Thousands (TTh), Thousands (Th), Hundreds (H), Tens (T), Units (U).",
        "svg_html": wrap_svg("""
          <g transform="translate(20, 20)">
            <rect x="0" y="0" width="420" height="130" rx="8" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.8"/>
            <text x="210" y="28" font-size="13" font-weight="900" fill="#0369a1" text-anchor="middle">482,519 (Four Hundred &amp; Eighty-Two Thousand...)</text>
            <g transform="translate(10, 45)">
              <rect x="0" y="0" width="60" height="40" fill="#bae6fd"/><text x="30" y="25" font-size="12" font-weight="800" fill="#0369a1" text-anchor="middle">4 HTh</text>
              <rect x="68" y="0" width="60" height="40" fill="#bae6fd"/><text x="98" y="25" font-size="12" font-weight="800" fill="#0369a1" text-anchor="middle">8 TTh</text>
              <rect x="136" y="0" width="60" height="40" fill="#bae6fd"/><text x="166" y="25" font-size="12" font-weight="800" fill="#0369a1" text-anchor="middle">2 Th</text>
              <rect x="204" y="0" width="60" height="40" fill="#e0f2fe"/><text x="234" y="25" font-size="12" font-weight="800" fill="#0369a1" text-anchor="middle">5 H</text>
              <rect x="272" y="0" width="60" height="40" fill="#e0f2fe"/><text x="302" y="25" font-size="12" font-weight="800" fill="#0369a1" text-anchor="middle">1 T</text>
              <rect x="340" y="0" width="60" height="40" fill="#e0f2fe"/><text x="370" y="25" font-size="12" font-weight="800" fill="#0369a1" text-anchor="middle">9 U</text>
            </g>
            <text x="210" y="115" font-size="12" font-weight="800" fill="#0c4a6e" text-anchor="middle">The digit '8' has a value of 80,000 (Eighty Thousand)</text>
          </g>"""),
        "golden_rule": "Read large numbers in groups of three digits from left to right!",
        "watch_out": "Don't confuse 'Eight Thousand' (8,000) with 'Eighty Thousand' (80,000).",
        "challenge_prompt": "What is the value of the digit 7 in the number 574,820?",
        "answer_text": "The digit 7 is in the ten thousands column, so its value is 70,000 (Seventy Thousand)."
    },

    # 2. Four Operations with Whole Numbers
    {
        "id": "m-l1-02",
        "number": 2,
        "title": "Four Operations with Whole Numbers",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Number System",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.N2",
        "rule_heading": "Column Methods &amp; Checking",
        "rule_body": "Addition &amp; Subtraction: Line up unit digits strictly on the right. Carry over when sum ≥ 10; borrow from next column to the left for subtraction. Multiplication: Long column. Division: Short 'bus stop'.",
        "svg_html": wrap_svg("""
          <g transform="translate(50, 15)">
            <rect x="0" y="0" width="160" height="135" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="80" y="22" font-size="11" font-weight="800" fill="#1e40af" text-anchor="middle">SUBTRACTION (BORROW)</text>
            <text x="56" y="42" font-size="10.5" font-weight="900" fill="#dc2626" text-anchor="middle">4</text>
            <text x="86" y="42" font-size="10.5" font-weight="900" fill="#dc2626" text-anchor="middle">11</text>
            <text x="116" y="42" font-size="10.5" font-weight="900" fill="#dc2626" text-anchor="middle">14</text>
            <text x="56" y="62" font-size="15" font-weight="800" fill="#94a3b8" text-anchor="middle">5</text>
            <line x1="48" y1="67" x2="64" y2="51" stroke="#dc2626" stroke-width="2" stroke-linecap="round"/>
            <text x="86" y="62" font-size="15" font-weight="800" fill="#94a3b8" text-anchor="middle">2</text>
            <line x1="78" y1="67" x2="94" y2="51" stroke="#dc2626" stroke-width="2" stroke-linecap="round"/>
            <text x="116" y="62" font-size="15" font-weight="800" fill="#94a3b8" text-anchor="middle">4</text>
            <line x1="108" y1="67" x2="124" y2="51" stroke="#dc2626" stroke-width="2" stroke-linecap="round"/>
            <text x="26" y="84" font-size="18" font-weight="900" fill="#0284c7" text-anchor="middle">&minus;</text>
            <text x="56" y="84" font-size="15" font-weight="800" fill="#0f172a" text-anchor="middle">1</text>
            <text x="86" y="84" font-size="15" font-weight="800" fill="#0f172a" text-anchor="middle">6</text>
            <text x="116" y="84" font-size="15" font-weight="800" fill="#0f172a" text-anchor="middle">8</text>
            <line x1="20" y1="94" x2="140" y2="94" stroke="#0f172a" stroke-width="2"/>
            <text x="56" y="118" font-size="16" font-weight="900" fill="#059669" text-anchor="middle">3</text>
            <text x="86" y="118" font-size="16" font-weight="900" fill="#059669" text-anchor="middle">5</text>
            <text x="116" y="118" font-size="16" font-weight="900" fill="#059669" text-anchor="middle">6</text>
          </g>
          <g transform="translate(250, 15)">
            <rect x="0" y="0" width="160" height="135" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="80" y="22" font-size="11" font-weight="800" fill="#15803d" text-anchor="middle">SHORT BUS-STOP DIVISION</text>
            <text x="64" y="52" font-size="16" font-weight="900" fill="#15803d" text-anchor="middle">1</text>
            <text x="92" y="52" font-size="16" font-weight="900" fill="#15803d" text-anchor="middle">4</text>
            <text x="120" y="52" font-size="16" font-weight="900" fill="#15803d" text-anchor="middle">2</text>
            <path d="M 46 95 L 46 58 L 136 58" fill="none" stroke="#0f172a" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
            <text x="30" y="85" font-size="16" font-weight="900" fill="#0369a1" text-anchor="middle">6</text>
            <text x="64" y="85" font-size="15" font-weight="800" fill="#0f172a" text-anchor="middle">8</text>
            <text x="80" y="73" font-size="10" font-weight="900" fill="#dc2626" text-anchor="middle">&sup2;</text>
            <text x="92" y="85" font-size="15" font-weight="800" fill="#0f172a" text-anchor="middle">5</text>
            <text x="108" y="73" font-size="10" font-weight="900" fill="#dc2626" text-anchor="middle">&sup1;</text>
            <text x="120" y="85" font-size="15" font-weight="800" fill="#0f172a" text-anchor="middle">2</text>
            <rect x="20" y="104" width="120" height="22" rx="4" fill="#dcfce7" stroke="#86efac"/>
            <text x="80" y="119" font-size="10.5" font-weight="800" fill="#15803d" text-anchor="middle">852 &divide; 6 = 142 &check;</text>
          </g>"""),
        "golden_rule": "Always check subtraction by adding your answer to the smaller number!",
        "watch_out": "Don't subtract smaller from larger in the same column! If top digit is smaller, borrow 1 from left.",
        "challenge_prompt": "Calculate: 735 - 289. Show your check using addition.",
        "answer_text": "735 - 289 = 446. Check: 446 + 289 = 735 ✓."
    },

    # 3. Negative Numbers (Temperature & Debt)
    {
        "id": "m-l1-03",
        "number": 3,
        "title": "Negative Numbers (Temp &amp; Debt)",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Number System",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.N3",
        "rule_heading": "Below Zero &amp; Bank Overdrafts",
        "rule_body": "Numbers below 0 have a minus sign (-). Moving RIGHT on the number line = getting warmer / paying in money (+). Moving LEFT = getting colder / spending money (-).",
        "svg_html": wrap_svg("""
          <line x1="30" y1="85" x2="430" y2="85" stroke="#334155" stroke-width="2.5"/>
          <line x1="230" y1="70" x2="230" y2="100" stroke="#0f172a" stroke-width="2.5"/>
          <text x="230" y="60" font-size="13" font-weight="900" fill="#0f172a" text-anchor="middle">£0 / 0°C</text>
          <text x="90" y="110" font-size="12" font-weight="800" fill="#dc2626" text-anchor="middle">-£15</text>
          <text x="370" y="110" font-size="12" font-weight="800" fill="#059669" text-anchor="middle">+£20</text>
          <path d="M 90,75 Q 230,30 370,75" fill="none" stroke="#2563eb" stroke-width="2" stroke-dasharray="4,4"/>
          <text x="230" y="35" font-size="12" font-weight="800" fill="#2563eb" text-anchor="middle">Difference = £35</text>
          <text x="230" y="145" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">-£15 is DEEPER in debt than -£5</text>"""),
        "golden_rule": "-8°C is COLDER than -3°C!",
        "watch_out": "Overdraft balance: If balance is -£25 and you spend £10, new balance is -£35 (NOT -£15).",
        "challenge_prompt": "A bank account is overdrawn by -£45. A deposit of £70 is paid in. What is the new bank balance?",
        "answer_text": "New balance = -45 + 70 = +£25."
    },

    # 4. Rounding to Nearest 10, 100, 1000
    {
        "id": "m-l1-04",
        "number": 4,
        "title": "Rounding to 10, 100, 1000",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Number System",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.N4",
        "rule_heading": "Look at the Neighbour on the Right",
        "rule_body": "Find the rounding place: Look at the next digit to the right: If 5 or more (5, 6, 7, 8, 9), ROUND UP. If 4 or less (0, 1, 2, 3, 4), ROUND DOWN (stay same). Fill trailing places with 0.",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="380" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="190" y="28" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">Round 4,763 to the nearest 100:</text>
            <text x="190" y="58" font-size="12" font-weight="700" fill="#475569" text-anchor="middle">Hundreds digit is 7. Neighbour is 6.</text>
            <rect x="90" y="75" width="200" height="35" rx="6" fill="#0284c7"/>
            <text x="190" y="98" font-size="14" font-weight="900" fill="#ffffff" text-anchor="middle">6 is ≥ 5 → Round up to 4,800</text>
          </g>"""),
        "golden_rule": "5 to 9 climbs the vine; 0 to 4 stays on the floor!",
        "watch_out": "Don't delete digits! When rounding 3,428 to the nearest 10, it becomes 3,430, NOT 343.",
        "challenge_prompt": "Round 18,450: (a) To the nearest 1,000. (b) To the nearest 100.",
        "answer_text": "(a) To nearest 1,000: 4 is &lt; 5 → 18,000. (b) To nearest 100: 5 is ≥ 5 → 18,500."
    },

    # 5. Decimals: Place Value & Ordering
    {
        "id": "m-l1-05",
        "number": 5,
        "title": "Decimals: Place Value &amp; Ordering",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Number System",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.N5",
        "rule_heading": "Tenths, Hundredths &amp; Thousandths",
        "rule_body": "To compare decimals: Line up decimal points vertically and pad with trailing zeros so all numbers have the same number of digits after the dot (e.g. 0.4 becomes 0.400).",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="380" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="190" y="28" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">Which is bigger: 0.35 or 0.4?</text>
            <text x="190" y="55" font-size="13" font-weight="700" fill="#475569" text-anchor="middle">Pad with a zero: 0.4 → 0.40</text>
            <text x="190" y="85" font-size="13" font-weight="800" fill="#2563eb" text-anchor="middle">Compare 35 hundredths vs 40 hundredths</text>
            <text x="190" y="112" font-size="14" font-weight="900" fill="#059669" text-anchor="middle">0.4 is BIGGER than 0.35!</text>
          </g>"""),
        "golden_rule": "Add trailing zeroes to level the playing field before comparing decimals!",
        "watch_out": "0.35 has more digits than 0.4, but 0.4 is LARGER! (0.40 > 0.35).",
        "challenge_prompt": "Put in order from smallest to largest: 0.08, 0.8, 0.75, 0.079.",
        "answer_text": "Pad to 3 decimal places: 0.080, 0.800, 0.750, 0.079. Order: 0.079, 0.08, 0.75, 0.8."
    },

    # 6. Operations with Decimals & Money
    {
        "id": "m-l1-06",
        "number": 6,
        "title": "Operations with Decimals &amp; Money",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Number System",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.N6",
        "rule_heading": "Line Up the Decimal Points",
        "rule_body": "Always align the decimal points directly under each other when adding or subtracting money. Money must ALWAYS have TWO decimal places (e.g. £4.50, NEVER £4.5).",
        "svg_html": wrap_svg("""
          <g transform="translate(130, 20)">
            <rect x="0" y="0" width="200" height="130" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
            <text x="100" y="26" font-size="12" font-weight="800" fill="#15803d" text-anchor="middle">LINE UP THE DOTS</text>
            <text x="100" y="55" font-size="14" font-weight="800" fill="#0f172a" text-anchor="middle">£ 1 4 . 5 0</text>
            <text x="100" y="80" font-size="14" font-weight="800" fill="#0f172a" text-anchor="middle">+ £   3 . 8 5</text>
            <line x1="30" y1="92" x2="170" y2="92" stroke="#15803d" stroke-width="1.8"/>
            <text x="100" y="115" font-size="15" font-weight="900" fill="#15803d" text-anchor="middle">£ 1 8 . 3 5</text>
          </g>"""),
        "golden_rule": "Always write pounds with 2 decimal places: £6.20, NOT £6.2!",
        "watch_out": "Don't mix pounds and pence without converting! £5 + 40p = £5.40, NOT £45.",
        "challenge_prompt": "You buy items costing £3.45, £8.20, and £0.95. You pay with a £20 note. How much change do you receive?",
        "answer_text": "Total = £3.45 + £8.20 + £0.95 = £12.60. Change = £20.00 - £12.60 = £7.40."
    },

    # 7. Common Fractions, Decimals & % Equivalence
    {
        "id": "m-l1-07",
        "number": 7,
        "title": "FDP Common Benchmarks",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Number System",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.N7",
        "rule_heading": "Halves, Quarters &amp; Tenths",
        "rule_body": "1/2 = 0.5 = 50%. 1/4 = 0.25 = 25%. 3/4 = 0.75 = 75%. 1/10 = 0.1 = 10%. 1/5 = 0.2 = 20%. Memorising these visual equivalents saves time in exams.",
        "svg_html": wrap_svg("""
          <g transform="translate(30, 20)">
            <rect x="0" y="0" width="400" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="65" y="26" font-size="11" font-weight="800" fill="#0f172a" text-anchor="middle">Fraction</text>
            <text x="195" y="26" font-size="11" font-weight="800" fill="#0f172a" text-anchor="middle">Decimal</text>
            <text x="330" y="26" font-size="11" font-weight="800" fill="#0f172a" text-anchor="middle">Percentage</text>
            <line x1="20" y1="36" x2="380" y2="36" stroke="#cbd5e1"/>
            <text x="65" y="60" font-size="12" font-weight="700" fill="#2563eb" text-anchor="middle">1/2</text><text x="195" y="60" font-size="12" font-weight="700" fill="#059669" text-anchor="middle">0.5</text><text x="330" y="60" font-size="12" font-weight="800" fill="#d97706" text-anchor="middle">50%</text>
            <text x="65" y="85" font-size="12" font-weight="700" fill="#2563eb" text-anchor="middle">1/4</text><text x="195" y="85" font-size="12" font-weight="700" fill="#059669" text-anchor="middle">0.25</text><text x="330" y="85" font-size="12" font-weight="800" fill="#d97706" text-anchor="middle">25%</text>
            <text x="65" y="110" font-size="12" font-weight="700" fill="#2563eb" text-anchor="middle">3/4</text><text x="195" y="110" font-size="12" font-weight="700" fill="#059669" text-anchor="middle">0.75</text><text x="330" y="110" font-size="12" font-weight="800" fill="#d97706" text-anchor="middle">75%</text>
          </g>"""),
        "golden_rule": "1/5 is 20% (0.2), NOT 15%!",
        "watch_out": "Don't confuse 0.1 (10%) with 0.01 (1%).",
        "challenge_prompt": "Which is greater: 0.3 or 1/4? Show your working.",
        "answer_text": "1/4 = 0.25. Since 0.30 > 0.25, 0.3 is greater."
    },

    # 8. Simplifying & Equivalent Fractions
    {
        "id": "m-l1-08",
        "number": 8,
        "title": "Simplifying Fractions",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Number System",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.N8",
        "rule_heading": "Divide Top and Bottom Equally",
        "rule_body": "To simplify a fraction, divide both the numerator (top) and denominator (bottom) by their Highest Common Factor (HCF). Keep dividing until no common factors remain.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="170" y="30" font-size="14" font-weight="800" fill="#1e40af" text-anchor="middle">Simplify 12/18</text>
            <text x="170" y="65" font-size="12" font-weight="700" fill="#475569" text-anchor="middle">Divide top and bottom by 6 (HCF):</text>
            <rect x="90" y="80" width="160" height="35" rx="6" fill="#3b82f6"/>
            <text x="170" y="103" font-size="15" font-weight="900" fill="#ffffff" text-anchor="middle">12 ÷ 6 / 18 ÷ 6 = 2/3</text>
          </g>"""),
        "golden_rule": "Whatever you do to the top, you MUST do to the bottom!",
        "watch_out": "Never subtract numbers to simplify fractions — you can ONLY divide or multiply.",
        "challenge_prompt": "Write 24/36 in its simplest form.",
        "answer_text": "Divide by 12: 24 ÷ 12 = 2. 36 ÷ 12 = 3. Simplest form = 2/3."
    },

    # 9. Fraction of an Amount (Basic)
    {
        "id": "m-l1-09",
        "number": 9,
        "title": "Fraction of an Amount (Basic)",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Number System",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.N9",
        "rule_heading": "Divide by Denominator, Times by Numerator",
        "rule_body": "To find a unit fraction (1/n): Divide by n. To find a non-unit fraction (e.g. 3/4): 1. Divide by 4 to get 1 quarter. 2. Multiply result by 3 to get 3 quarters.",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="380" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="190" y="28" font-size="14" font-weight="800" fill="#0f172a" text-anchor="middle">Find 3/4 of 48 kg</text>
            <text x="190" y="60" font-size="12" font-weight="700" fill="#2563eb" text-anchor="middle">Step 1: 48 ÷ 4 = 12 kg (1/4)</text>
            <rect x="110" y="75" width="160" height="35" rx="6" fill="#16a34a"/>
            <text x="190" y="98" font-size="14" font-weight="900" fill="#ffffff" text-anchor="middle">Step 2: 12 × 3 = 36 kg</text>
          </g>"""),
        "golden_rule": "Divide by bottom, multiply by top!",
        "watch_out": "Don't stop after step 1! Dividing by 4 gives only ONE quarter (12 kg), you need THREE.",
        "challenge_prompt": "A community group has 60 members. 2/5 of them are volunteers. How many volunteers are there?",
        "answer_text": "60 ÷ 5 = 12 (1/5). 12 × 2 = 24 volunteers."
    },

    # 10. Percentages of Amounts (Building Blocks)
    {
        "id": "m-l1-10",
        "number": 10,
        "title": "Percentages (Building Blocks)",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Number System",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.N10",
        "rule_heading": "10%, 5%, 1% Breakdown Method",
        "rule_body": "Non-calculator percentage hacks: 10% = Divide by 10. 5% = Half of 10%. 1% = Divide by 100. 50% = Half (÷ 2). Combine blocks to find any percentage (e.g. 15% = 10% + 5%).",
        "svg_html": wrap_svg("""
          <g transform="translate(30, 20)">
            <rect x="0" y="0" width="400" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="200" y="26" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">Find 15% of £80 without calculator</text>
            <text x="50" y="55" font-size="12" font-weight="700" fill="#2563eb">10% of £80 = £80 ÷ 10 = £8.00</text>
            <text x="50" y="80" font-size="12" font-weight="700" fill="#059669">5% of £80 = Half of £8 = £4.00</text>
            <rect x="50" y="92" width="300" height="26" rx="4" fill="#d97706"/>
            <text x="200" y="110" font-size="12" font-weight="800" fill="#ffffff" text-anchor="middle">15% = £8.00 + £4.00 = £12.00</text>
          </g>"""),
        "golden_rule": "Find 10% first — it unlocks 5%, 20%, 30%, and 15% instantly!",
        "watch_out": "Don't divide by 15 to find 15%! You find 10% and add 5%.",
        "challenge_prompt": "Work out 35% of £240 without using a calculator.",
        "answer_text": "10% = £24. 30% = 24 × 3 = £72. 5% = half of £24 = £12. 35% = £72 + £12 = £84."
    },

    # 11. Simple Ratios (Simplifying & Sharing)
    {
        "id": "m-l1-11",
        "number": 11,
        "title": "Simple Ratios (2 Parts)",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Number System",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.N11",
        "rule_heading": "Add Parts, Divide Total, Multiply",
        "rule_body": "To share £60 in ratio 1 : 3: 1. Add parts: 1 + 3 = 4 parts. 2. Divide total: £60 ÷ 4 = £15 (value of 1 part). 3. Multiply: Share 1 = £15, Share 2 = 3 × £15 = £45.",
        "svg_html": wrap_svg("""
          <rect x="40" y="20" width="380" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
          <text x="230" y="42" font-size="13" font-weight="800" fill="#1e40af" text-anchor="middle">Share £60 in ratio 1 : 3</text>
          <g transform="translate(60, 60)">
            <rect x="0" y="0" width="60" height="35" rx="4" fill="#bfdbfe"/><text x="30" y="22" font-size="11" font-weight="800" fill="#1e40af" text-anchor="middle">£15</text>
            <rect x="70" y="0" width="60" height="35" rx="4" fill="#93c5fd"/><text x="100" y="22" font-size="11" font-weight="800" fill="#1e40af" text-anchor="middle">£15</text>
            <rect x="140" y="0" width="60" height="35" rx="4" fill="#93c5fd"/><text x="170" y="22" font-size="11" font-weight="800" fill="#1e40af" text-anchor="middle">£15</text>
            <rect x="210" y="0" width="60" height="35" rx="4" fill="#93c5fd"/><text x="240" y="22" font-size="11" font-weight="800" fill="#1e40af" text-anchor="middle">£15</text>
          </g>
          <text x="230" y="125" font-size="12" font-weight="800" fill="#059669" text-anchor="middle">Result = £15 and £45 (Total = £60 ✓)</text>"""),
        "golden_rule": "Ratios must always be simplified to lowest whole numbers!",
        "watch_out": "Keep the order of the ratio correct: Person A : Person B must match the order in the text.",
        "challenge_prompt": "Simplify the ratio 15 : 25 to its simplest form.",
        "answer_text": "Divide both by 5: 15 ÷ 5 = 3, 25 ÷ 5 = 5. Simplified ratio = 3 : 5."
    },

    # 12. Direct Proportion (Recipes & Scaling)
    {
        "id": "m-l1-12",
        "number": 12,
        "title": "Direct Proportion (Recipes)",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Number System",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.N12",
        "rule_heading": "Unitary Method: Find for 1 First",
        "rule_body": "To scale a recipe: 1. Divide ingredients by the original number of servings to find the amount for 1 person. 2. Multiply by the new number of people needed.",
        "svg_html": wrap_svg("""
          <g transform="translate(30, 20)">
            <rect x="0" y="0" width="400" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="200" y="26" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">Recipe for 4 people: 200g flour. Need for 6 people?</text>
            <text x="50" y="58" font-size="12" font-weight="700" fill="#2563eb">Step 1 (For 1 person): 200g ÷ 4 = 50g</text>
            <rect x="50" y="75" width="300" height="35" rx="6" fill="#16a34a"/>
            <text x="200" y="98" font-size="13" font-weight="900" fill="#ffffff" text-anchor="middle">Step 2 (For 6 people): 50g × 6 = 300g flour</text>
          </g>"""),
        "golden_rule": "Find the quantity for ONE person first, then multiply!",
        "watch_out": "Don't just add 2 to the flour because 6 is 4 + 2 — you must scale proportionally!",
        "challenge_prompt": "A soup recipe for 8 people needs 600 ml of stock. How much stock is needed for 12 people?",
        "answer_text": "For 1 person: 600 ÷ 8 = 75 ml. For 12 people: 75 × 12 = 900 ml."
    },

    # 13. Multiples, Factors & Prime Numbers
    {
        "id": "m-l1-13",
        "number": 13,
        "title": "Multiples, Factors &amp; Primes",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Number System",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.N13",
        "rule_heading": "Definitions &amp; Factor Pairs",
        "rule_body": "Multiple = In the times table (Multiples of 5: 5, 10, 15...). Factor = Numbers that divide in exactly with no remainder. Prime = EXACTLY two factors: 1 and itself (2, 3, 5, 7, 11...).",
        "svg_html": wrap_svg("""
          <g transform="translate(30, 20)">
            <rect x="0" y="0" width="190" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="95" y="26" font-size="12" font-weight="800" fill="#1e40af" text-anchor="middle">FACTORS OF 12</text>
            <text x="95" y="55" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">1 × 12</text>
            <text x="95" y="78" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">2 × 6</text>
            <text x="95" y="101" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">3 × 4</text>
          </g>
          <g transform="translate(240, 20)">
            <rect x="0" y="0" width="190" height="130" rx="8" fill="#fef2f2" stroke="#ef4444" stroke-width="1.8"/>
            <text x="95" y="26" font-size="12" font-weight="800" fill="#991b1b" text-anchor="middle">PRIME NUMBERS &lt; 20</text>
            <text x="95" y="60" font-size="13" font-weight="800" fill="#dc2626" text-anchor="middle">2, 3, 5, 7, 11, 13, 17, 19</text>
            <text x="95" y="95" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">⚠️ 1 is NOT prime!</text>
            <text x="95" y="112" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">2 is the ONLY even prime</text>
          </g>"""),
        "golden_rule": "1 is NOT a prime number because it only has 1 factor!",
        "watch_out": "Factors are smaller (or equal); multiples are larger (or equal).",
        "challenge_prompt": "List all the factors of 20.",
        "answer_text": "Factor pairs: 1 × 20, 2 × 10, 4 × 5. Factors of 20: 1, 2, 4, 5, 10, 20."
    },

    # 14. Inverse Operations for Checking
    {
        "id": "m-l1-14",
        "number": 14,
        "title": "Inverse Operations for Checking",
        "subject": "maths",
        "level": "l1",
        "subject_label": "Maths",
        "level_label": "Level 1",
        "strand_name": "Number System",
        "strand_theme": "cyan",
        "dfe_code": "DfE L1.N14",
        "rule_heading": "Reverse Your Calculation for 1 Mark",
        "rule_body": "Pearson exams award a dedicated mark for 'Show a check of your answer': Addition check with SUBTRACTION. Subtraction check with ADDITION. Multiplication check with DIVISION. Division check with MULTIPLICATION.",
        "svg_html": wrap_svg("""
          <rect x="30" y="20" width="400" height="130" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
          <text x="230" y="42" font-size="13" font-weight="900" fill="#15803d" text-anchor="middle">PEARSON SECTION A CHECKING HACK</text>
          <g transform="translate(60, 60)">
            <text x="0" y="22" font-size="12" font-weight="700" fill="#0f172a">Main Calculation: 45 × 8 = 360</text>
            <rect x="0" y="35" width="320" height="30" rx="4" fill="#16a34a"/>
            <text x="160" y="55" font-size="12" font-weight="800" fill="#ffffff" text-anchor="middle">Written Check: 360 ÷ 8 = 45 ✓</text>
          </g>"""),
        "golden_rule": "Always write down an inverse check when the paper asks 'Show a check of your working'!",
        "watch_out": "Don't just repeat the exact same calculation — it MUST be the reverse operation or an approximation.",
        "challenge_prompt": "You calculated: 156 + 89 = 245. Write down a valid check of your working using inverse operations.",
        "answer_text": "Check: 245 - 89 = 156 (or 245 - 156 = 89)."
    }
]

print(f"Validated Strand A: {len(CARDS_A)} cards")
