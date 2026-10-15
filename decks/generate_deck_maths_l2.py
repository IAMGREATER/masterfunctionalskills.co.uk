#!/usr/bin/env python3
"""
Generator for Deck 1: Maths Level 2 (Cards 1-50)
Produces decks/deck_maths_l2.py
"""
import sys
import os
import xml.etree.ElementTree as ET

def wrap_svg(inner_content, height=170):
    svg = f'<svg viewBox="0 0 460 {height}" width="100%" height="{height}" xmlns="http://www.w3.org/2000/svg">\n{inner_content}\n</svg>'
    # Validate XML
    try:
        ET.fromstring(svg)
    except Exception as e:
        print(f"SVG Validation Error: {e}\n{svg}")
        raise
    return svg

def build_maths_l2():
    cards = []

    # 1. BIDMAS
    cards.append({
        "id": "m-l2-01",
        "number": 1,
        "title": "Order of Operations (BIDMAS)",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Number System",
        "strand_theme": "blue",
        "dfe_code": "DfE L2.N1",
        "rule_heading": "B - I - D/M - A/S",
        "rule_body": "Operations must be completed in order: 1. Brackets (), 2. Indices (², ³, √), 3. Division &amp; Multiplication (left-to-right), 4. Addition &amp; Subtraction (left-to-right).",
        "svg_html": wrap_svg("""
          <rect x="20" y="15" width="420" height="140" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
          <g transform="translate(35, 30)">
            <rect x="0" y="0" width="60" height="35" rx="6" fill="#1e3a8a"/><text x="30" y="24" fill="#ffffff" font-size="16" font-weight="900" text-anchor="middle">B</text>
            <rect x="68" y="0" width="60" height="35" rx="6" fill="#1d4ed8"/><text x="98" y="24" fill="#ffffff" font-size="16" font-weight="900" text-anchor="middle">I</text>
            <rect x="136" y="0" width="60" height="35" rx="6" fill="#2563eb"/><text x="166" y="24" fill="#ffffff" font-size="16" font-weight="900" text-anchor="middle">D</text>
            <rect x="204" y="0" width="60" height="35" rx="6" fill="#3b82f6"/><text x="234" y="24" fill="#ffffff" font-size="16" font-weight="900" text-anchor="middle">M</text>
            <rect x="272" y="0" width="60" height="35" rx="6" fill="#60a5fa"/><text x="302" y="24" fill="#0f172a" font-size="16" font-weight="900" text-anchor="middle">A</text>
            <rect x="340" y="0" width="60" height="35" rx="6" fill="#93c5fd"/><text x="370" y="24" fill="#0f172a" font-size="16" font-weight="900" text-anchor="middle">S</text>
          </g>
          <g transform="translate(35, 78)">
            <rect x="0" y="0" width="390" height="60" rx="8" fill="#ffffff" stroke="#cbd5e1"/>
            <text x="15" y="25" font-size="13" font-weight="700" fill="#0f172a">Example: 5 + 3 × (4 - 2)²</text>
            <text x="15" y="48" font-size="12" font-weight="800" fill="#2563eb">1. (4-2)=2 → 2. 2²=4 → 3. 3×4=12 → 4. 5+12 = <tspan fill="#059669">17</tspan></text>
          </g>"""),
        "golden_rule": "Always solve brackets and powers first before multiplying or adding!",
        "watch_out": "Don't just calculate left-to-right! 5 + 3 × 2 is 11, NOT 16.",
        "challenge_prompt": "Evaluate: 8 + 4 × (7 - 4)² ÷ 6",
        "answer_text": "1. Brackets: (7 - 4) = 3. 2. Index: 3² = 9. 3. Multiply: 4 × 9 = 36. 4. Divide: 36 ÷ 6 = 6. 5. Add: 8 + 6 = 14."
    })

    # 2. Negative Numbers
    cards.append({
        "id": "m-l2-02",
        "number": 2,
        "title": "Negative Numbers in Context",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Number System",
        "strand_theme": "blue",
        "dfe_code": "DfE L2.N2",
        "rule_heading": "Rules of Signs &amp; Difference",
        "rule_body": "Difference between positive &amp; negative = Add their absolute values (|a| + |b|). Multiplying/Dividing: Same signs = POSITIVE (+). Different signs = NEGATIVE (-).",
        "svg_html": wrap_svg("""
          <line x1="40" y1="85" x2="420" y2="85" stroke="#334155" stroke-width="3"/>
          <line x1="230" y1="65" x2="230" y2="105" stroke="#0f172a" stroke-width="3"/>
          <text x="230" y="55" font-size="14" font-weight="900" fill="#0f172a" text-anchor="middle">0°C</text>
          <circle cx="110" cy="85" r="7" fill="#ef4444"/>
          <text x="110" y="115" font-size="13" font-weight="800" fill="#dc2626" text-anchor="middle">-6°C</text>
          <circle cx="350" cy="85" r="7" fill="#059669"/>
          <text x="350" y="115" font-size="13" font-weight="800" fill="#059669" text-anchor="middle">+8°C</text>
          <path d="M 110,70 Q 230,20 350,70" fill="none" stroke="#2563eb" stroke-width="2.5" stroke-dasharray="5,5"/>
          <rect x="180" y="18" width="100" height="24" rx="5" fill="#2563eb"/>
          <text x="230" y="35" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">Difference = 14°C</text>
          <text x="230" y="152" font-size="12" font-weight="700" fill="#475569" text-anchor="middle">(-6) to (+8) = 6 steps to zero + 8 steps = 14</text>"""),
        "golden_rule": "Subtracting a negative is the same as ADDING! 5 - (-3) = 5 + 3 = 8.",
        "watch_out": "-5°C is COLDER than -2°C. The larger the numeral after the minus sign, the lower the value.",
        "challenge_prompt": "A vaccine freezer is at -18°C. A power failure causes it to rise to -4°C. By how many degrees did the temperature rise?",
        "answer_text": "Rise = -4 - (-18) = -4 + 18 = 14°C."
    })

    # 3. FDP Equivalence
    cards.append({
        "id": "m-l2-03",
        "number": 3,
        "title": "Fractions, Decimals &amp; % Equivalence",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Number System",
        "strand_theme": "blue",
        "dfe_code": "DfE L2.N3",
        "rule_heading": "Conversion Benchmarks",
        "rule_body": "To compare values, convert them all to percentages or decimals: Fraction to %: (Numerator ÷ Denominator) × 100. Decimal to %: Multiply by 100.",
        "svg_html": wrap_svg("""
          <g transform="translate(30, 15)">
            <rect x="0" y="0" width="400" height="140" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>
            <line x1="0" y1="35" x2="400" y2="35" stroke="#cbd5e1" stroke-width="1.5"/>
            <line x1="130" y1="0" x2="130" y2="140" stroke="#cbd5e1" stroke-width="1.5"/>
            <line x1="260" y1="0" x2="260" y2="140" stroke="#cbd5e1" stroke-width="1.5"/>
            <text x="65" y="24" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">Fraction</text>
            <text x="195" y="24" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">Decimal</text>
            <text x="330" y="24" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">Percentage</text>
            <text x="65" y="60" font-size="13" font-weight="700" fill="#2563eb" text-anchor="middle">1/8</text><text x="195" y="60" font-size="13" font-weight="700" fill="#059669" text-anchor="middle">0.125</text><text x="330" y="60" font-size="13" font-weight="800" fill="#d97706" text-anchor="middle">12.5%</text>
            <text x="65" y="90" font-size="13" font-weight="700" fill="#2563eb" text-anchor="middle">3/8</text><text x="195" y="90" font-size="13" font-weight="700" fill="#059669" text-anchor="middle">0.375</text><text x="330" y="90" font-size="13" font-weight="800" fill="#d97706" text-anchor="middle">37.5%</text>
            <text x="65" y="120" font-size="13" font-weight="700" fill="#2563eb" text-anchor="middle">5/8</text><text x="195" y="120" font-size="13" font-weight="700" fill="#059669" text-anchor="middle">0.625</text><text x="330" y="120" font-size="13" font-weight="800" fill="#d97706" text-anchor="middle">62.5%</text>
          </g>"""),
        "golden_rule": "Eighths are common exam traps: 1/8 = 12.5% (0.125), not 18%!",
        "watch_out": "0.4 is 40%, NOT 4%! 0.04 is 4%. Count your decimal places carefully.",
        "challenge_prompt": "Put in order from smallest to largest: 3/8, 35%, 0.36, 1/3.",
        "answer_text": "Convert all to decimals: 1/3 = 0.333..., 35% = 0.35, 0.36 = 0.36, 3/8 = 0.375. Order: 1/3, 35%, 0.36, 3/8."
    })

    # 4. Fraction of an Amount
    cards.append({
        "id": "m-l2-04",
        "number": 4,
        "title": "Fraction of an Amount (Non-Calc)",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Number System",
        "strand_theme": "blue",
        "dfe_code": "DfE L2.N4",
        "rule_heading": "Divide by Bottom, Times by Top",
        "rule_body": "To find a fraction (a/b) of any amount: 1. Divide total by denominator (b) to find 1 part. 2. Multiply result by numerator (a) to get required parts.",
        "svg_html": wrap_svg("""
          <rect x="30" y="20" width="400" height="45" rx="8" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
          <text x="230" y="48" font-size="16" font-weight="800" fill="#0369a1" text-anchor="middle">Find 3/5 of £180</text>
          <g transform="translate(50, 80)">
            <rect x="0" y="0" width="170" height="60" rx="8" fill="#f0fdf4" stroke="#16a34a"/>
            <text x="85" y="25" font-size="12" font-weight="800" fill="#15803d" text-anchor="middle">Step 1: Divide by 5</text>
            <text x="85" y="48" font-size="13" font-weight="700" fill="#0f172a" text-anchor="middle">£180 ÷ 5 = £36 (1 part)</text>
          </g>
          <g transform="translate(240, 80)">
            <rect x="0" y="0" width="170" height="60" rx="8" fill="#fefce8" stroke="#ca8a04"/>
            <text x="85" y="25" font-size="12" font-weight="800" fill="#a16207" text-anchor="middle">Step 2: Multiply by 3</text>
            <text x="85" y="48" font-size="14" font-weight="800" fill="#0f172a" text-anchor="middle">£36 × 3 = <tspan fill="#059669">£108</tspan></text>
          </g>"""),
        "golden_rule": "Divide by the denominator, multiply by the numerator!",
        "watch_out": "If a question asks for the REMAINING amount, remember to subtract your answer from the original total.",
        "challenge_prompt": "A clinic orders 240 boxes of gloves. 5/8 of them are size Medium. How many boxes are NOT size Medium?",
        "answer_text": "Non-Medium fraction = 1 - 5/8 = 3/8. 240 ÷ 8 = 30. 30 × 3 = 90 boxes."
    })

    # 5. Adding & Subtracting Mixed Fractions
    cards.append({
        "id": "m-l2-05",
        "number": 5,
        "title": "Adding &amp; Subtracting Mixed Fractions",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Number System",
        "strand_theme": "blue",
        "dfe_code": "DfE L2.N4",
        "rule_heading": "Improper &amp; Common Denominator",
        "rule_body": "1. Convert mixed numbers to improper fractions (Whole × Denom + Num). 2. Find lowest common denominator (LCM). 3. Add or subtract numerators only. 4. Simplify.",
        "svg_html": wrap_svg("""
          <rect x="30" y="15" width="400" height="140" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
          <text x="230" y="40" font-size="15" font-weight="800" fill="#1e293b" text-anchor="middle">2 1/4 + 1 2/3</text>
          <g transform="translate(50, 55)">
            <text x="0" y="25" font-size="12" font-weight="700" fill="#2563eb">1. Improper: 9/4 + 5/3</text>
            <text x="0" y="50" font-size="12" font-weight="700" fill="#475569">2. Common Denom (12): 27/12 + 20/12</text>
            <text x="0" y="75" font-size="13" font-weight="800" fill="#059669">3. Add numerators: 47/12 = 3 11/12</text>
          </g>"""),
        "golden_rule": "NEVER add denominators together! 1/4 + 2/3 is NEVER 3/7.",
        "watch_out": "When subtracting, always convert to top-heavy improper fractions first to prevent negative fractional parts.",
        "challenge_prompt": "Work out 3 1/3 - 1 3/4. Give your answer as a mixed number in simplest form.",
        "answer_text": "1. Convert: 10/3 - 7/4. 2. Common denom 12: 40/12 - 21/12 = 19/12. 3. Mixed: 1 7/12."
    })

    # 6. Multiplying & Dividing Fractions
    cards.append({
        "id": "m-l2-06",
        "number": 6,
        "title": "Multiplying &amp; Dividing Fractions",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Number System",
        "strand_theme": "blue",
        "dfe_code": "DfE L2.N5",
        "rule_heading": "Multiply Straight / Keep-Change-Flip",
        "rule_body": "Multiplication: Multiply tops, multiply bottoms (cross-cancel if possible). Division: KEEP the first fraction, CHANGE ÷ to ×, FLIP the second fraction (reciprocal).",
        "svg_html": wrap_svg("""
          <g transform="translate(30, 20)">
            <rect x="0" y="0" width="190" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="95" y="28" font-size="13" font-weight="800" fill="#1e40af" text-anchor="middle">MULTIPLY</text>
            <text x="95" y="60" font-size="14" font-weight="800" fill="#0f172a" text-anchor="middle">2/3 × 5/7</text>
            <text x="95" y="90" font-size="12" font-weight="700" fill="#475569" text-anchor="middle">Top: 2 × 5 = 10</text>
            <text x="95" y="110" font-size="12" font-weight="700" fill="#475569" text-anchor="middle">Bottom: 3 × 7 = 21 → <tspan fill="#2563eb" font-weight="800">10/21</tspan></text>
          </g>
          <g transform="translate(240, 20)">
            <rect x="0" y="0" width="190" height="130" rx="8" fill="#fdf2f8" stroke="#ec4899" stroke-width="1.8"/>
            <text x="95" y="28" font-size="13" font-weight="800" fill="#9d174d" text-anchor="middle">DIVIDE (K-C-F)</text>
            <text x="95" y="60" font-size="14" font-weight="800" fill="#0f172a" text-anchor="middle">3/4 ÷ 2/5</text>
            <text x="95" y="90" font-size="12" font-weight="700" fill="#475569" text-anchor="middle">Keep 3/4 • Change × • Flip 5/2</text>
            <text x="95" y="110" font-size="12" font-weight="800" fill="#be185d" text-anchor="middle">3/4 × 5/2 = 15/8 = 1 7/8</text>
          </g>"""),
        "golden_rule": "Dividing by a fraction is the same as multiplying by its reciprocal!",
        "watch_out": "Never flip the FIRST fraction — only flip the SECOND fraction after changing the sign.",
        "challenge_prompt": "Work out 2/5 ÷ 4/15. Give your answer in its simplest form.",
        "answer_text": "Keep 2/5, change to ×, flip to 15/4: (2 × 15) ÷ (5 × 4) = 30 ÷ 20 = 3/2 = 1 1/2."
    })

    # 7. Percentage Increase & Decrease (Multiplier)
    cards.append({
        "id": "m-l2-07",
        "number": 7,
        "title": "Percentage Increase &amp; Decrease (Multiplier)",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Number System",
        "strand_theme": "blue",
        "dfe_code": "DfE L2.N6",
        "rule_heading": "Single Multiplier Method",
        "rule_body": "Increase: Add % to 100%, divide by 100. (e.g. +17.5% = × 1.175). Decrease: Subtract % from 100%, divide by 100. (e.g. -15% = × 0.85).",
        "svg_html": wrap_svg("""
          <g transform="translate(30, 20)">
            <rect x="0" y="0" width="190" height="130" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
            <text x="95" y="28" font-size="13" font-weight="800" fill="#15803d" text-anchor="middle">INCREASE (+20%)</text>
            <text x="95" y="60" font-size="12" font-weight="700" fill="#475569" text-anchor="middle">100% + 20% = 120%</text>
            <rect x="25" y="75" width="140" height="30" rx="5" fill="#16a34a"/>
            <text x="95" y="95" font-size="13" font-weight="800" fill="#ffffff" text-anchor="middle">Multiplier = × 1.20</text>
          </g>
          <g transform="translate(240, 20)">
            <rect x="0" y="0" width="190" height="130" rx="8" fill="#fef2f2" stroke="#dc2626" stroke-width="1.8"/>
            <text x="95" y="28" font-size="13" font-weight="800" fill="#b91c1c" text-anchor="middle">DECREASE (-15%)</text>
            <text x="95" y="60" font-size="12" font-weight="700" fill="#475569" text-anchor="middle">100% - 15% = 85%</text>
            <rect x="25" y="75" width="140" height="30" rx="5" fill="#dc2626"/>
            <text x="95" y="95" font-size="13" font-weight="800" fill="#ffffff" text-anchor="middle">Multiplier = × 0.85</text>
          </g>"""),
        "golden_rule": "Using a single multiplier is faster and eliminates rounding errors on calculator papers!",
        "watch_out": "Be careful with single digit percentages: +5% is × 1.05, NOT × 1.5 (which is +50%)!",
        "challenge_prompt": "A laptop originally costs £640. In a sale, it is reduced by 18%. Use a single multiplier to calculate the sale price.",
        "answer_text": "Multiplier = 1 - 0.18 = 0.82. Sale price = £640 × 0.82 = £524.80."
    })

    # 8. Percentage Change Formula
    cards.append({
        "id": "m-l2-08",
        "number": 8,
        "title": "Percentage Change Formula",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Number System",
        "strand_theme": "blue",
        "dfe_code": "DfE L2.N7",
        "rule_heading": "(Change ÷ Original) × 100",
        "rule_body": "Percentage Change = (Actual Difference ÷ Original Starting Value) × 100. Works for percentage profit, loss, discount, and inflation.",
        "svg_html": wrap_svg("""
          <rect x="40" y="20" width="380" height="60" rx="8" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>
          <text x="230" y="45" font-size="15" font-weight="800" fill="#1e3a8a" text-anchor="middle">% Change = (Change ÷ Original) × 100</text>
          <text x="230" y="68" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">Always divide by the STARTING value, never the new value!</text>
          <g transform="translate(60, 95)">
            <rect x="0" y="0" width="340" height="55" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>
            <text x="170" y="24" font-size="12" font-weight="700" fill="#0f172a" text-anchor="middle">Car bought for £8,000, sold for £6,800</text>
            <text x="170" y="44" font-size="12" font-weight="800" fill="#dc2626" text-anchor="middle">Change = £1,200 → (1,200 ÷ 8,000) × 100 = 15% Loss</text>
          </g>"""),
        "golden_rule": "Denominator is ALWAYS the original starting value before the change occurred!",
        "watch_out": "Don't divide by the new price! Dividing 1,200 by 6,800 gives 17.6%, which is incorrect.",
        "challenge_prompt": "A gym membership increases from £35 per month to £42 per month. Calculate the percentage increase.",
        "answer_text": "Change = £42 - £35 = £7. % Increase = (7 ÷ 35) × 100 = 1/5 × 100 = 20%."
    })

    # 9. Reverse Percentages
    cards.append({
        "id": "m-l2-09",
        "number": 9,
        "title": "Reverse Percentages (Original Value)",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Number System",
        "strand_theme": "blue",
        "dfe_code": "DfE L2.N8",
        "rule_heading": "Divide by Multiplier",
        "rule_body": "To find the original price before VAT or sale: 1. Identify the new percentage (e.g. Price + 20% VAT = 120% = 1.20). 2. Divide final price by multiplier (Price ÷ 1.20).",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 25)">
            <rect x="0" y="0" width="220" height="45" rx="6" fill="#3b82f6"/>
            <text x="110" y="28" font-size="13" font-weight="800" fill="#ffffff" text-anchor="middle">Original Price = 100%</text>
            <rect x="220" y="0" width="60" height="45" fill="#f59e0b"/>
            <text x="250" y="28" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">+20%</text>
            <rect x="295" y="5" width="95" height="35" rx="6" fill="#1e293b"/>
            <text x="342" y="27" font-size="12" font-weight="800" fill="#38bdf8" text-anchor="middle">120% = £144</text>
          </g>
          <g transform="translate(70, 95)">
            <rect x="0" y="0" width="320" height="50" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
            <text x="160" y="22" font-size="12" font-weight="800" fill="#15803d" text-anchor="middle">DO NOT CALCULATE 20% OF £144!</text>
            <text x="160" y="40" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">Original = £144 ÷ 1.20 = <tspan fill="#059669">£120</tspan></text>
          </g>"""),
        "golden_rule": "To go BACKWARDS to the original, DIVIDE by the multiplier!",
        "watch_out": "Never calculate the percentage of the sale/final price and subtract! 20% of £144 is £28.80 (£115.20 = WRONG).",
        "challenge_prompt": "A coat costs £136 in a 15% off sale. What was its original price before the sale?",
        "answer_text": "Sale price = 100% - 15% = 85% = 0.85. Original = £136 ÷ 0.85 = £160."
    })

    # 10. Simple vs Compound Interest
    cards.append({
        "id": "m-l2-10",
        "number": 10,
        "title": "Simple vs Compound Interest",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Number System",
        "strand_theme": "blue",
        "dfe_code": "DfE L2.N9",
        "rule_heading": "Fixed Amount vs Interest on Interest",
        "rule_body": "Simple: Same fixed interest paid every year. Compound: Total = Principal × (Multiplier)^Years. Interest is earned on accumulated interest.",
        "svg_html": wrap_svg("""
          <g transform="translate(30, 20)">
            <rect x="0" y="0" width="190" height="130" rx="8" fill="#f8fafc" stroke="#64748b" stroke-width="1.8"/>
            <text x="95" y="26" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">SIMPLE INTEREST</text>
            <text x="95" y="52" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">£1,000 at 5% for 3 yrs</text>
            <text x="95" y="78" font-size="11" font-weight="700" fill="#2563eb" text-anchor="middle">£50 + £50 + £50 = £150</text>
            <rect x="25" y="95" width="140" height="24" rx="4" fill="#e2e8f0"/>
            <text x="95" y="111" font-size="11" font-weight="800" fill="#0f172a" text-anchor="middle">Total = £1,150</text>
          </g>
          <g transform="translate(240, 20)">
            <rect x="0" y="0" width="190" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="95" y="26" font-size="12" font-weight="800" fill="#1e40af" text-anchor="middle">COMPOUND INTEREST</text>
            <text x="95" y="52" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">£1,000 × (1.05)³</text>
            <text x="95" y="78" font-size="11" font-weight="700" fill="#059669" text-anchor="middle">£1,000 × 1.157625</text>
            <rect x="25" y="95" width="140" height="24" rx="4" fill="#3b82f6"/>
            <text x="95" y="111" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">Total = £1,157.63</text>
          </g>"""),
        "golden_rule": "Compound formula: Total = Principal × (1 + r/100)ⁿ",
        "watch_out": "Check whether the question asks for the TOTAL ACCUMULATED AMOUNT or just the INTEREST EARNED!",
        "challenge_prompt": "£4,000 is invested in a bond paying 4% compound interest annually. What is the total value after 3 years?",
        "answer_text": "Multiplier = 1.04. Total = £4,000 × (1.04)³ = £4,000 × 1.124864 = £4,499.46."
    })

    # 11. Sharing in 3-Part Ratio
    cards.append({
        "id": "m-l2-11",
        "number": 11,
        "title": "Sharing in a 3-Part Ratio",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Number System",
        "strand_theme": "blue",
        "dfe_code": "DfE L2.N10",
        "rule_heading": "Add Parts, Divide, Multiply",
        "rule_body": "1. Add all parts together to find total parts (e.g. 2 + 3 + 5 = 10 parts). 2. Divide total amount by total parts to find value of 1 part. 3. Multiply 1 part by each share.",
        "svg_html": wrap_svg("""
          <rect x="30" y="20" width="400" height="135" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
          <text x="230" y="45" font-size="14" font-weight="800" fill="#0f172a" text-anchor="middle">Share £480 in ratio 2 : 3 : 5</text>
          <g transform="translate(50, 65)">
            <rect x="0" y="0" width="105" height="40" rx="4" fill="#dbeafe"/><text x="52" y="25" font-size="11" font-weight="800" fill="#1e40af" text-anchor="middle">1. Total: 10 parts</text>
            <rect x="120" y="0" width="105" height="40" rx="4" fill="#dcfce7"/><text x="172" y="25" font-size="11" font-weight="800" fill="#15803d" text-anchor="middle">2. £480÷10 = £48</text>
            <rect x="240" y="0" width="120" height="40" rx="4" fill="#fef3c7"/><text x="300" y="25" font-size="10" font-weight="800" fill="#b45309" text-anchor="middle">3. ×2, ×3, ×5</text>
          </g>
          <text x="230" y="135" font-size="12" font-weight="800" fill="#2563eb" text-anchor="middle">Shares: £96 : £144 : £240 (Sum = £480 ✓)</text>"""),
        "golden_rule": "Check your work: Add the final shares together — they must equal the starting total!",
        "watch_out": "Don't divide the total by just one number! Always sum ALL parts first.",
        "challenge_prompt": "Three partners invest in a business in the ratio 3 : 4 : 5. Profits of £72,000 are shared in this ratio. What is the largest share?",
        "answer_text": "Total parts = 3 + 4 + 5 = 12. Value of 1 part = £72,000 ÷ 12 = £6,000. Largest share (5 parts) = 5 × £6,000 = £30,000."
    })

    # 12. Reverse Ratios
    cards.append({
        "id": "m-l2-12",
        "number": 12,
        "title": "Reverse Ratios (Difference / One Share)",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Number System",
        "strand_theme": "blue",
        "dfe_code": "DfE L2.N11",
        "rule_heading": "Find 1 Part from the Difference",
        "rule_body": "When told 'Person A gets £X more than Person B': 1. Find difference in ratio parts. 2. Divide given money by difference in parts = 1 part. 3. Multiply by required share.",
        "svg_html": wrap_svg("""
          <rect x="30" y="15" width="400" height="140" rx="8" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.8"/>
          <text x="230" y="40" font-size="13" font-weight="800" fill="#92400e" text-anchor="middle">Ratio 5 : 3 • Liam gets £40 more than Maya</text>
          <g transform="translate(60, 60)">
            <text x="0" y="20" font-size="12" font-weight="700" fill="#0f172a">1. Difference in parts: 5 - 3 = <tspan font-weight="800" fill="#d97706">2 parts</tspan></text>
            <text x="0" y="45" font-size="12" font-weight="700" fill="#0f172a">2. Value of 1 part: £40 ÷ 2 = <tspan font-weight="800" fill="#059669">£20</tspan></text>
            <text x="0" y="70" font-size="12" font-weight="800" fill="#2563eb">3. Total money: (5 + 3) = 8 parts × £20 = £160</text>
          </g>"""),
        "golden_rule": "Match the given amount to its specific parts, NEVER the total parts!",
        "watch_out": "Don't divide £40 by 8! The £40 represents the DIFFERENCE (2 parts), not the total.",
        "challenge_prompt": "In a bakery, loaves to rolls are baked in the ratio 4 : 7. There are 45 more rolls than loaves. How many loaves were baked?",
        "answer_text": "Difference in parts = 7 - 4 = 3 parts. 1 part = 45 ÷ 3 = 15 items. Loaves (4 parts) = 4 × 15 = 60 loaves."
    })

    # 13. Direct & Inverse Proportion
    cards.append({
        "id": "m-l2-13",
        "number": 13,
        "title": "Direct &amp; Inverse Proportion",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Number System",
        "strand_theme": "blue",
        "dfe_code": "DfE L2.N12",
        "rule_heading": "Direct (Both Up) vs Inverse (One Up, One Down)",
        "rule_body": "Direct: As X doubles, Y doubles (Scale factor or Unitary method). Inverse: As workers increase, time decreases! Workers × Time = Constant Total Work.",
        "svg_html": wrap_svg("""
          <g transform="translate(30, 20)">
            <rect x="0" y="0" width="190" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="95" y="26" font-size="12" font-weight="800" fill="#1e40af" text-anchor="middle">DIRECT PROPORTION</text>
            <text x="95" y="55" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">4 books cost £18</text>
            <text x="95" y="80" font-size="11" font-weight="700" fill="#2563eb" text-anchor="middle">1 book = 18 ÷ 4 = £4.50</text>
            <text x="95" y="110" font-size="12" font-weight="800" fill="#059669" text-anchor="middle">7 books = 7 × 4.5 = £31.50</text>
          </g>
          <g transform="translate(240, 20)">
            <rect x="0" y="0" width="190" height="130" rx="8" fill="#fef2f2" stroke="#ef4444" stroke-width="1.8"/>
            <text x="95" y="26" font-size="12" font-weight="800" fill="#991b1b" text-anchor="middle">INVERSE PROPORTION</text>
            <text x="95" y="55" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">3 painters take 8 hours</text>
            <text x="95" y="80" font-size="11" font-weight="700" fill="#dc2626" text-anchor="middle">Total = 3 × 8 = 24 hrs</text>
            <text x="95" y="110" font-size="12" font-weight="800" fill="#059669" text-anchor="middle">6 painters = 24 ÷ 6 = 4 hrs</text>
          </g>"""),
        "golden_rule": "More workers take LESS time! Multiply workers by hours to get total person-hours.",
        "watch_out": "Don't scale inverse proportion by multiplying both! If 3 workers take 8 hrs, 6 workers do NOT take 16 hrs!",
        "challenge_prompt": "4 technicians take 6 hours to test a server system. How long would 3 technicians take working at the same rate?",
        "answer_text": "Total work = 4 × 6 = 24 person-hours. For 3 technicians: 24 ÷ 3 = 8 hours."
    })

    # 14. Best Buy & Unit Pricing
    cards.append({
        "id": "m-l2-14",
        "number": 14,
        "title": "Best Buy &amp; Unit Pricing",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Number System",
        "strand_theme": "blue",
        "dfe_code": "DfE L2.N13",
        "rule_heading": "Cost per Unit (Price ÷ Quantity)",
        "rule_body": "To compare value for money, find the cost for 1 unit (100g, 1ml, or 1 item): Cost per 100g = (Price in pence ÷ Grams) × 100. The lowest cost per unit is the best value.",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="180" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="90" y="26" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">Pack A: 500g for £2.40</text>
            <text x="90" y="60" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">240p ÷ 5 =</text>
            <rect x="35" y="75" width="110" height="30" rx="5" fill="#e2e8f0"/>
            <text x="90" y="95" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">48p per 100g</text>
          </g>
          <g transform="translate(240, 20)">
            <rect x="0" y="0" width="180" height="130" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
            <text x="90" y="26" font-size="13" font-weight="800" fill="#15803d" text-anchor="middle">Pack B: 800g for £3.60</text>
            <text x="90" y="60" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">360p ÷ 8 =</text>
            <rect x="35" y="75" width="110" height="30" rx="5" fill="#16a34a"/>
            <text x="90" y="95" font-size="13" font-weight="800" fill="#ffffff" text-anchor="middle">45p per 100g ★</text>
          </g>"""),
        "golden_rule": "Convert pounds to pence first to avoid difficult decimal calculations!",
        "watch_out": "Don't just pick the cheaper price tag — a smaller pack might cost more per 100g.",
        "challenge_prompt": "Cereal Brand X: 450g costs £2.25. Brand Y: 600g costs £2.88. Which is better value for money?",
        "answer_text": "Brand X: 225p ÷ 4.5 = 50p per 100g. Brand Y: 288p ÷ 6 = 48p per 100g. Brand Y is better value by 2p per 100g."
    })

    # 15. Rounding to Significant Figures
    cards.append({
        "id": "m-l2-15",
        "number": 15,
        "title": "Rounding to Significant Figures",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Number System",
        "strand_theme": "blue",
        "dfe_code": "DfE L2.N14",
        "rule_heading": "Count from First Non-Zero Digit",
        "rule_body": "1st sig fig is the first digit that is NOT zero reading left-to-right. Look at next digit: 5 or more rounds UP, 4 or less rounds DOWN. Fill trailing spaces with placeholder zeroes.",
        "svg_html": wrap_svg("""
          <g transform="translate(30, 20)">
            <rect x="0" y="0" width="400" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="20" y="30" font-size="13" font-weight="800" fill="#0f172a">Round 0.004782 to 2 sig figs:</text>
            <text x="20" y="60" font-size="12" font-weight="700" fill="#64748b">Leading zeros do NOT count! First non-zero = 4 (1st), 7 (2nd).</text>
            <text x="20" y="85" font-size="12" font-weight="700" fill="#2563eb">Next digit is 8 (rounds 7 UP to 8) → <tspan font-weight="800" fill="#059669">0.0048</tspan></text>
            <line x1="20" y1="98" x2="380" y2="98" stroke="#cbd5e1"/>
            <text x="20" y="118" font-size="12" font-weight="800" fill="#b91c1c">Round 48,290 to 1 sig fig: 48,290 → 50,000 (keep placeholder zeroes!)</text>
          </g>"""),
        "golden_rule": "Leading zeros in decimals NEVER count as significant figures!",
        "watch_out": "Don't turn 48,290 into 5! You must keep the placeholder zeros (50,000).",
        "challenge_prompt": "Round: (a) 63,740 to 2 significant figures. (b) 0.05084 to 2 significant figures.",
        "answer_text": "(a) 63,740 → 64,000 (7 rounds 3 up). (b) 0.05084 → 0.051 (8 rounds 0 up; first non-zero is 5)."
    })

    # 16. Estimation & Approximation
    cards.append({
        "id": "m-l2-16",
        "number": 16,
        "title": "Estimation &amp; Approximation",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Number System",
        "strand_theme": "blue",
        "dfe_code": "DfE L2.N15",
        "rule_heading": "Round Every Number to 1 Sig Fig",
        "rule_body": "To estimate calculations and verify checks in Section A: Round EACH number to 1 significant figure BEFORE performing any multiplication or division.",
        "svg_html": wrap_svg("""
          <rect x="30" y="15" width="400" height="140" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
          <text x="230" y="42" font-size="14" font-weight="800" fill="#1e40af" text-anchor="middle">Estimate: (48.7 × 19.3) ÷ 0.49</text>
          <g transform="translate(60, 60)">
            <text x="0" y="22" font-size="12" font-weight="700" fill="#0f172a">1. Round to 1 sig fig: 48.7 → 50, 19.3 → 20, 0.49 → 0.5</text>
            <text x="0" y="47" font-size="12" font-weight="700" fill="#0f172a">2. Calculate numerator: 50 × 20 = 1,000</text>
            <text x="0" y="72" font-size="13" font-weight="800" fill="#059669">3. Divide: 1,000 ÷ 0.5 = 2,000 (Dividing by 0.5 doubles!)</text>
          </g>"""),
        "golden_rule": "Dividing by 0.5 is the exact same as multiplying by 2!",
        "watch_out": "Do NOT calculate the exact answer first and round at the end! Examiners award zero marks if unrounded values are used.",
        "challenge_prompt": "Use approximation to 1 significant figure to estimate: (312 × 4.89) ÷ 0.19.",
        "answer_text": "Round to 1 sf: 300 × 5 ÷ 0.2. 300 × 5 = 1,500. 1,500 ÷ 0.2 = 1,500 × 5 = 7,500."
    })

    # 17. Powers, Roots & Indices
    cards.append({
        "id": "m-l2-017",
        "number": 17,
        "title": "Powers, Roots &amp; Indices",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Number System",
        "strand_theme": "blue",
        "dfe_code": "DfE L2.N16",
        "rule_heading": "Square, Cube &amp; Roots",
        "rule_body": "x² = x × x. x³ = x × x × x. Square root (√x) is inverse of squaring. Cube root (∛x) is the number multiplied by itself 3 times to give x.",
        "svg_html": wrap_svg("""
          <g transform="translate(30, 20)">
            <rect x="0" y="0" width="190" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="95" y="26" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">SQUARE ROOTS</text>
            <text x="95" y="55" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">8² = 64 → √64 = 8</text>
            <text x="95" y="80" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">11² = 121 → √121 = 11</text>
            <text x="95" y="108" font-size="12" font-weight="800" fill="#2563eb" text-anchor="middle">√144 = 12</text>
          </g>
          <g transform="translate(240, 20)">
            <rect x="0" y="0" width="190" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="95" y="26" font-size="12" font-weight="800" fill="#1e40af" text-anchor="middle">CUBE ROOTS</text>
            <text x="95" y="55" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">2³ = 2×2×2 = 8 → ∛8 = 2</text>
            <text x="95" y="80" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">3³ = 3×3×3 = 27 → ∛27 = 3</text>
            <text x="95" y="108" font-size="12" font-weight="800" fill="#059669" text-anchor="middle">5³ = 125 → ∛125 = 5</text>
          </g>"""),
        "golden_rule": "5³ is NOT 5 × 3 = 15! 5³ is 5 × 5 × 5 = 125.",
        "watch_out": "Square root of a number between 0 and 1 gets BIGGER! √0.25 = 0.5.",
        "challenge_prompt": "Evaluate: 4³ - √169 + 2⁴.",
        "answer_text": "4³ = 64. √169 = 13. 2⁴ = 16. Calculation: 64 - 13 + 16 = 51 + 16 = 67."
    })

    # 18. Formula Substitution
    cards.append({
        "id": "m-l2-18",
        "number": 18,
        "title": "Formula Substitution",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Number System",
        "strand_theme": "blue",
        "dfe_code": "DfE L2.N17",
        "rule_heading": "Replace Letters with Numbers",
        "rule_body": "1. Replace each variable with given numbers (use brackets around negatives!). 2. Follow BIDMAS: Multiply adjacent terms before adding. 3. Check units.",
        "svg_html": wrap_svg("""
          <rect x="30" y="15" width="400" height="140" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
          <text x="230" y="40" font-size="14" font-weight="800" fill="#0f172a" text-anchor="middle">Wage Formula: W = 12h + 1.5(oh)</text>
          <g transform="translate(60, 60)">
            <text x="0" y="20" font-size="12" font-weight="700" fill="#475569">If regular hours h = 35 and overtime hours oh = 6:</text>
            <text x="0" y="45" font-size="12" font-weight="700" fill="#2563eb">W = (12 × 35) + 1.5 × (12 × 6)</text>
            <text x="0" y="70" font-size="13" font-weight="800" fill="#059669">W = £420 + £108 = £528 Total Wage</text>
          </g>"""),
        "golden_rule": "Letters side-by-side mean MULTIPLY: 4ab means 4 × a × b!",
        "watch_out": "Squaring a negative number gives a positive: (-4)² = +16, NOT -16.",
        "challenge_prompt": "Kinematics: v² = u² + 2as. Find v when u = 3, a = 4, and s = 5.",
        "answer_text": "v² = 3² + (2 × 4 × 5) = 9 + 40 = 49. v = √49 = 7."
    })

    # Save to deck_maths_l2.py
    return cards

if __name__ == "__main__":
    cards = build_maths_l2()
    print(f"Successfully generated and validated {len(cards)} cards for Strand A!")
